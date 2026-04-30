import os
from pathlib import Path

from py8dis.commands import *
import py8dis.acorn as acorn
import py8dis.trace as trace

init(assembler_name="beebasm", lower_case=True)

# ============================================================
# ANFS 4.21 (variant 1) — Acorn Advanced Network Filing System
# ============================================================
# 16KB service ROM (&8000-&BFFF). Successor to NFS 3.65.
# Incorporates filing system commands (previously on server),
# printer support, and other improvements.
# Authors: B Cockburn, J Dunn, B Robertson, J Wills.

# Paths are resolved relative to this script's location in the repo
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get(
    "ACORN_NFS_ROM",
    str(_version_dirpath / "rom" / "anfs-4.21_variant_1.rom"),
)
_output_dirpath = Path(os.environ.get(
    "ACORN_NFS_OUTPUT",
    str(_version_dirpath / "output"),
))

load(0x8000, _rom_filepath, "65c02")
trace.cpu.default_subroutine_hook = None

# ============================================================
# Relocated code blocks
# ============================================================
# The ANFS ROM copies code from ROM into RAM at initialisation.
# These blocks execute at different addresses than their storage locations.
# move(dest, src, length) tells py8dis the runtime address for each block.
#
# The page copy loop (&BE9C) copies 256 bytes of pages 4, 5, 6
# using DEY/BNE wrapping through &FF..&01. In 4.18 the page 4 source
# is at &BF04, so bytes &04FC-&04FF come from MOS ROM (unreferenced).
#
# The workspace init (&BEB8) copies X=&41 downto 0 (BPL) = 66 bytes.

# BRK handler + NMI workspace init code (&BEC3 -> &0016-&0057)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): move(0x0016, 0xBEC3, 0x42)

# NMI handler / page 4-6 relocated code
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): move(0x0400, 0xBF04, 0xFC)     # Page 4: 252 bytes (&04FC-&04FF from MOS, unreferenced)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): move(0x0500, 0xBC94, 0x100)    # Page 5: Tube host code
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): move(0x0600, 0xBD94, 0x100)    # Page 6: Econet protocol handlers

# ROM-address labels for move() block origins (referenced by copy routines)
# UNMAPPED: label(0xBEC3, "reloc_zp_src")        # ROM source of zero-page relocated code
# UNMAPPED: label(0xBF04, "reloc_p4_src")        # ROM source of page 4 code
# UNMAPPED: label(0xBC94, "reloc_p5_src")        # ROM source of page 5 code
# UNMAPPED: label(0xBD94, "reloc_p6_src")        # ROM source of page 6 code

byte(0xBFC7)  # Force padding byte onto its own line for annotation

# acorn.bbc() provides OS vectors, entry points, zero page labels.
# acorn.is_sideways_rom() provides ROM header labels.
acorn.bbc()
acorn.is_sideways_rom()

# ============================================================
# Inline string subroutine hooks
# ============================================================
# print_inline (&9131) prints an inline string following the JSR, terminated
# by a byte with bit 7 set. The high-bit byte is the opcode of the next
# instruction — the routine jumps there via JMP (fs_error_ptr).
hook_subroutine(0x9261, "print_inline", stringhi_hook)

# error_inline (&96BE) builds a BRK error block from a null-terminated inline
# string following the JSR. The error number is passed in A. Never returns.
hook_subroutine(0x99C3, "error_inline", stringz_hook)

# error_inline_log (&96BB) is identical to error_inline but first logs the
# error code via sub_c95fb. Never returns.
hook_subroutine(0x99C0, "error_inline_log", stringz_hook)

# error_bad_inline (&96A2) prepends "Bad " to the inline string before
# building the BRK error block. The error number is passed in A. Never returns.
hook_subroutine(0x99A7, "error_bad_inline", stringz_hook)


# ============================================================
# Hardware registers
# ============================================================

# MC6854 ADLC registers (active at &FEA0-&FEA3 when active Econet station)
constant(0xFEA0, "adlc_cr1")   # Write: CR1 (or CR3 if AC=1). Read: SR1
constant(0xFEA1, "adlc_cr2")   # Write: CR2 (or CR4 if AC=1). Read: SR2
constant(0xFEA2, "adlc_tx")    # Write: TX FIFO (continue frame). Read: RX FIFO
constant(0xFEA3, "adlc_tx2")   # Write: TX FIFO (last byte). Read: RX FIFO

# Econet hardware on the 1MHz bus
constant(0xFE18, "econet_station_id")  # Read: station DIP switches AND INTOFF
constant(0xFE20, "econet_nmi_enable")  # Read: INTON (re-enable NMIs)

# Tube ULA registers (&FEE0-&FEE7) — named by acorn.bbc()

# ============================================================
# Protocol constants
# ============================================================

# Econet port numbers
constant(0x99, "port_command")        # PCMND: command port
constant(0x90, "port_reply")          # PREPLY: reply port
constant(0x91, "port_save_ack")       # PSAACK: save acknowledge port
constant(0x92, "port_load_data")      # PLDATA: load data port
constant(0x93, "port_remote")         # PREMOT: remote operation port
constant(0xD1, "port_printer")        # PBLOCK: printer block port

# Econet error codes
constant(0xA0, "err_line_jammed")     # LINJAM
constant(0xA1, "err_net_error")       # NETER
constant(0xA2, "err_not_listening")   # NOLISE
constant(0xA3, "err_no_clock")        # NOCLK
constant(0xA4, "err_tx_cb_error")     # TXCBER
constant(0xA5, "err_no_reply")        # NOREPE
constant(0xA8, "err_fs_cutoff")       # ERRCUT: FS errors >= this

# Protocol flags
constant(0x80, "tx_flag")             # TXFLAG
constant(0x7F, "rx_ready")            # RXRDY

# FS handle base
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): constant(0x20, "handle_base")         # HAND: base value for file handles

# Control block template markers
constant(0xFE, "cb_stop")             # CBSTOP
constant(0xFD, "cb_skip")             # CBSKIP
constant(0xFC, "cb_fill")             # CBFILL

# ============================================================
# Named constants for OSBYTE/OS values
# ============================================================
constant(20,  "osbyte_explode_chars")
constant(120, "osbyte_write_keys_pressed")
constant(143, "osbyte_issue_service_request")
constant(168, "osbyte_read_rom_ptr_table_low")

# ============================================================
# Zero page — Econet workspace (&90-&A9)
# ============================================================

label(0x0097, "escapable")           # b7=respond to Escape flag
label(0x0098, "need_release_tube")   # b7=need to release Tube
label(0x0099, "prot_flags")          # PFLAGS: printer/protocol status flags
label(0x009A, "net_tx_ptr")          # NetTx control block pointer (low)
label(0x009B, "net_tx_ptr_hi")       # NetTx control block pointer (high)
label(0x009C, "net_rx_ptr")          # NetRx control blocks pointer (low)
label(0x009D, "net_rx_ptr_hi")       # NetRx control blocks pointer (high)
label(0x009E, "nfs_workspace")       # General NFS workspace pointer (low)
label(0x009F, "nfs_workspace_hi")    # General NFS workspace pointer (high)
label(0x00A0, "nmi_tx_block")        # Block to be transmitted (low)
label(0x00A1, "nmi_tx_block_hi")     # Block to be transmitted (high)
label(0x00A2, "port_buf_len")        # Open port buffer length (low)
label(0x00A3, "port_buf_len_hi")     # Open port buffer length (high)
label(0x00A4, "open_port_buf")       # Open port buffer address (low)
label(0x00A5, "open_port_buf_hi")    # Open port buffer address (high)
label(0x00A6, "port_ws_offset")      # Port workspace offset
label(0x00A7, "rx_buf_offset")       # Receive buffer offset
label(0x00A8, "ws_page")             # Multi-purpose workspace page
label(0x00A9, "svc_state")           # Multi-purpose service state
label(0x00AA, "osword_flag")         # OSWORD param byte
label(0x00AB, "ws_ptr_lo")           # Workspace indirect pointer (lo)
label(0x00AC, "ws_ptr_hi")           # Workspace indirect pointer (hi)
label(0x00AD, "table_idx")           # OSBYTE/palette table index counter
label(0x00AE, "work_ae")             # Indexed workspace (multi-purpose scratch)
label(0x00AF, "addr_work")           # Address work byte for comparison (indexed)

# ============================================================
# Zero page — Filing system workspace (&B0-&CF)
# ============================================================

label(0x00B0, "fs_load_addr")        # WORK: load/start address (4 bytes)
label(0x00B1, "fs_load_addr_hi")
label(0x00B2, "fs_load_addr_2")
label(0x00B3, "fs_load_addr_3")
label(0x00B4, "fs_work_4")
label(0x00B5, "fs_work_5")
label(0x00B6, "fs_work_6")
label(0x00B7, "fs_work_7")
label(0x00B8, "fs_error_ptr")
label(0x00B9, "fs_crflag")
label(0x00BA, "fs_spool_handle")
label(0x00BB, "fs_options")
label(0x00BC, "fs_block_offset")
label(0x00BD, "fs_last_byte_flag")
label(0x00BE, "fs_crc_lo")
label(0x00BF, "fs_crc_hi")
label(0x00CC, "fs_ws_ptr")            # FS workspace page pointer (lo, always 0)
label(0x00C0, "txcb_ctrl")
label(0x00C1, "txcb_port")
label(0x00C2, "txcb_dest")
label(0x00C4, "txcb_start")
label(0x00C7, "txcb_pos")
label(0x00C8, "txcb_end")
label(0x00CD, "nfs_temp")
label(0x00CE, "rom_svc_num")
label(0x00CF, "fs_spool0")
label(0x00D0, "vdu_status")           # VDU status register (OSBYTE &75)

# Zero page — Additional OS locations
label(0x0000, "zp_ptr_lo")
label(0x0001, "zp_ptr_hi")
label(0x0002, "zp_work_2")
label(0x0003, "zp_work_3")
label(0x0010, "zp_temp_10")
label(0x0011, "zp_temp_11")
label(0x0012, "tube_data_ptr")
label(0x0013, "tube_data_ptr_hi")
label(0x0014, "tube_claim_flag")
label(0x0015, "tube_claimed_id")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0016, "nmi_workspace_start")
label(0x0063, "zp_0063")             # (false ref from inline string data)
label(0x0078, "zp_0078")             # (false ref from inline string data)

# Zero page — MOS locations (&EF-&FF)
label(0x00EF, "osbyte_a_copy")
label(0x00F0, "osword_pb_ptr")
label(0x00F1, "osword_pb_ptr_hi")
label(0x00F3, "os_text_ptr_hi")
label(0x00F7, "osrdsc_ptr_hi")
label(0x00FD, "brk_ptr")
label(0x00FF, "escape_flag")

# Page 1 — Stack page
# UNMAPPED: label(0x0100, "error_block")
# UNMAPPED: label(0x0101, "error_text")
# UNMAPPED: label(0x0102, "stack_page_2")         # Stack-relative access at SP+2
# UNMAPPED: label(0x0103, "stack_page_3")         # Stack-relative access at SP+3
# UNMAPPED: label(0x0104, "stack_page_4")         # Stack-relative access at SP+4
# UNMAPPED: label(0x0106, "stack_page_6")         # Stack-relative access at SP+6
# UNMAPPED: label(0x0128, "tube_osword_pb")       # Tube host: OSWORD parameter block

# Page 2 — OS workspace
# UNMAPPED: label(0x026A, "vdu_queue_count")      # OSBYTE &DA: 256 - VDU queue items
# UNMAPPED: label(0x028D, "last_break_type")      # OSBYTE &FD: last BREAK type
# UNMAPPED: label(0x02A0, "rom_type_table")       # Paged ROM type table (16 entries)

# Page 3 — VDU variables
# UNMAPPED: label(0x0350, "vdu_screen_mode")
# UNMAPPED: label(0x0351, "vdu_display_start_hi") # 6845 screen display start address hi
# UNMAPPED: label(0x0355, "vdu_mode")             # Current screen mode

# Page 7 — String buffer
# UNMAPPED: label(0x0700, "string_buf")
# UNMAPPED: label(0x072C, "tube_vdu_stream_end")  # Tube VDU relay: end-of-stream target
# UNMAPPED: label(0x072E, "tube_vdu_normal_byte") # Tube VDU relay: normal byte target

# Page &0C — NMI shim write base
# UNMAPPED: label(0x0CFF, "nmi_code_base")

# ============================================================
# Page &0D — NMI handler workspace (&0D00-&0DFF)
# ============================================================

label(0x0D07, "nmi_romsel")           # ROM bank number patched into NMI shim
label(0x0D0C, "nmi_jmp_lo")
label(0x0D0D, "nmi_jmp_hi")
# NMI exit entry points (RAM shim, copied from rom_set_nmi_vector):
#   set_nmi_vector  (&0D0E): STY &0D0D; STA &0D0C — writes both bytes
#   install_nmi_handler (&0D11): STA &0D0C — writes low byte only
#     (same-page optimisation: keeps existing high byte at &0D0D)
#   nmi_rti (&0D14): restore ROM bank, PLA Y, PLA A, BIT &FE20
#     (INTON), RTI
# All three converge on the INTON/RTI at &0D1C/&0D1F.
label(0x0D0E, "set_nmi_vector")       # Update JMP target (both bytes) + nmi_rti
label(0x0D11, "install_nmi_handler")  # Update JMP target (lo byte only) + nmi_rti
label(0x0D14, "nmi_rti")              # Restore ROM, PLA, INTON, RTI
label(0x0D1A, "imm_param_base")       # Base for indexed imm-op TXCB param copy
label(0x0D1E, "tx_addr_base")         # Base for 4-byte TX transfer address

# Scout/acknowledge packet buffer (&0D20-&0D25)
label(0x0D20, "tx_dst_stn")
label(0x0D21, "tx_dst_net")
label(0x0D22, "tx_src_stn")
label(0x0D23, "tx_src_net")
label(0x0D24, "tx_ctrl_byte")
label(0x0D25, "tx_port")
label(0x0D26, "tx_data_start")

# TX control
label(0x0D2A, "tx_data_len")

# RX scout buffer (&0D2E-&0D39)
label(0x0D2E, "scout_buf")            # Base of 12-byte RX scout data buffer
label(0x0D2F, "scout_src_net")        # Scout: source network (scout_buf+1)
label(0x0D30, "scout_ctrl")           # Scout: control byte (scout_buf+2)
label(0x0D31, "scout_port")           # Scout: port byte (scout_buf+3)
label(0x0D32, "scout_data")           # Scout: data payload base (scout_buf+4)

# Received scout
label(0x0D3D, "rx_src_stn")
label(0x0D3E, "rx_src_net")
label(0x0D3F, "rx_ctrl")
label(0x0D40, "rx_port")
label(0x0D41, "rx_remote_addr")
label(0x0D42, "rx_extra_byte")        # Extra trailing RX data byte
label(0x0D43, "saved_nmi_lo")         # Saved next NMI handler address lo
label(0x0D44, "saved_nmi_hi")         # Saved next NMI handler address hi

# TX state
label(0x0D4A, "tx_flags")
label(0x0D4B, "nmi_next_lo")
label(0x0D4C, "nmi_next_hi")
label(0x0D4F, "tx_index")
label(0x0D50, "tx_length")

# ANFS-specific workspace (identified from references in ROM)
label(0x0D60, "tx_complete_flag")     # TX completion semaphore (b7: set by NMI handler on TX done)
label(0x0D61, "econet_flags")         # Econet control flags (b7: port list, b2: halt)
label(0x0D62, "econet_init_flag")     # Econet initialised flag (b7: NMI shim installed)
label(0x0D63, "tube_present")         # Tube co-processor presence flag
label(0x0D64, "ws_0d64")
label(0x0D65, "tx_op_type")
label(0x0D66, "exec_addr_lo")         # Remote execution address lo
label(0x0D67, "exec_addr_hi")         # Remote execution address hi
label(0x0D68, "ws_0d68")
label(0x0D69, "ws_0d69")
label(0x0D6A, "ws_0d6a")
label(0x0D6B, "spool_buf_idx")        # Spool/printer buffer write index
label(0x0D6C, "fs_flags")             # FS status flags (b7: selected/active)
label(0x0D6D, "tx_retry_count")       # Transmit retry count (default &FF = 255); OSWORD &13 PB[1]
label(0x0D6E, "rx_wait_timeout")      # Receive wait timeout (default &28 = 40); OSWORD &13 PB[2]
label(0x0D6F, "peek_retry_count")    # Machine peek retry count (default &0A = 10); OSWORD &13 PB[3]
label(0x0D72, "bridge_status")        # Bridge station number (&FF = no bridge)

# Page &0D — workspace pointers
label(0x0DE6, "txcb_default_base")    # Base for indexed read of default TXCB values
label(0x0DF0, "rom_ws_pages")         # MOS per-ROM workspace page table (16 bytes)
label(0x0DFA, "fs_context_save")      # Saved FS context block (station, handles)
label(0x0DFE, "osword_ws_base")       # Base for OSWORD &14 workspace-to-PB copy
label(0x0DFF, "fs_server_base")       # Base for Y-indexed file server stn/net

# ============================================================
# Page &0E — FS context workspace (&0E00-&0EFF)
# ============================================================

label(0x0E00, "fs_server_stn")        # Current file server station number
label(0x0E01, "fs_server_net")        # Current file server network number
label(0x0E02, "fs_urd_handle")        # URD handle / station byte for handle 1
label(0x0E03, "fs_csd_handle")        # CSD handle / station byte for handle 2
label(0x0E04, "fs_lib_handle")        # Library handle / station byte for handle 3
label(0x0E05, "fs_boot_option")       # Boot option / display flag
label(0x0E06, "fs_messages_flag")     # Display control / messages flag
label(0x0E07, "fs_eof_flags")         # Pending operation marker / FS state byte
label(0x0E09, "fs_last_error")        # Last error code
label(0x0E0A, "fs_cmd_context")       # Command tail pointer lo / reply data source
label(0x0E0B, "fs_context_hi")        # Command tail pointer hi
label(0x0E16, "fs_work_16")           # OSWORD parameter size storage
label(0x0E2F, "fs_filename_buf_m1")   # Byte before filename buffer (trim indexing)
label(0x0E30, "fs_filename_buf")      # Parsed filename buffer
label(0x0E31, "fs_filename_buf_1")    # fs_filename_buf + 1
label(0x0E32, "fs_filename_buf_2")    # fs_filename_buf + 2
label(0x0E38, "fs_filename_backup")   # Filename backup for library path retry
label(0x0EF7, "fs_reply_data")        # File info reply data

# ============================================================
# Page &0F — TX buffer / FS command workspace (&0F00-&0FFF)
# ============================================================

# TX buffer fields (&0F00-&0F16)
label(0x0F00, "txcb_reply_port")      # TXCB reply port / command type
label(0x0F01, "fs_cmd_y_param")       # TXCB function code / Y parameter
label(0x0F02, "fs_cmd_urd")           # TXCB station byte / URD / port number
label(0x0F03, "fs_cmd_csd")           # TXCB port byte / CSD handle
label(0x0F04, "fs_cmd_lib")           # TXCB lib handle / terminator byte
label(0x0F05, "fs_cmd_data")          # TX buffer data start / FS reply data
label(0x0F06, "fs_func_code")         # Function code / direction flag / offset
label(0x0F07, "fs_data_count")        # Data count / lock flag / position byte
label(0x0F08, "fs_reply_cmd")         # Transfer size lo / result byte
label(0x0F09, "fs_load_vector")       # Transfer size hi / indirect dispatch vector
label(0x0F0A, "fs_handle_check")      # Handle validity check / BCD minutes
label(0x0F0B, "fs_load_upper")        # Tube transfer check / BCD seconds
label(0x0F0C, "fs_addr_check")        # Tube transfer check (second byte)
label(0x0F0D, "fs_file_len")          # File length / address offset buffer (4 bytes)
label(0x0F0E, "fs_file_attrs")        # File access/attributes byte
label(0x0F10, "fs_file_len_3")        # File length hi / offset copy source
label(0x0F11, "fs_obj_type")          # Object type / reply handle
label(0x0F12, "fs_access_level")      # Access level / owner-public flag
label(0x0F13, "fs_reply_stn")         # Reply station / cycle number
label(0x0F14, "fs_len_clear")         # Cleared workspace byte
label(0x0F16, "fs_boot_data")         # OSBPUT display flag copy

# Examine response offsets
label(0x0F2F, "fs_exam_attr_char")    # File attribute char in examine response
label(0x0F30, "fs_exam_dir_flag")     # Directory contents flag in examine response

# OSBPUT send buffer (&0FDC-&0FE0)
label(0x0FDC, "fs_putb_buf")          # OSBPUT send buffer (function code)
label(0x0FDD, "fs_getb_buf")          # OSBPUT reply port / reply status
label(0x0FDE, "fs_handle_mask")       # Reply port for addressing
label(0x0FDF, "fs_error_flags")       # Data byte in send buffer
label(0x0FE0, "fcb_xfer_count_lo")    # FCB transfer count lo (per-slot table)
label(0x0FF0, "fcb_xfer_count_mid")   # FCB transfer count mid (per-slot table)

# ============================================================
# Page &10 — Channel/FCB table workspace (&1000-&10FF)
# ============================================================

# FCB parallel arrays with &10-byte stride (16 entries each)
label(0x1000, "fcb_count_lo")         # Byte count / position lo; shadow ws base
label(0x1010, "fcb_attr_or_count_mid")  # Channel attribute / byte count mid
label(0x1020, "fcb_station_or_count_hi")  # Station number / byte count hi
label(0x1030, "fcb_net_or_port")      # Network number / reply port
label(0x1040, "fcb_flags")            # FCB flags (handle assignment, state)
label(0x1050, "fcb_net_num")          # FCB network number (station matching)
label(0x1060, "chan_status")           # Channel status flags (per-slot)

# Scalar handle/flag variables
label(0x1070, "cur_dir_handle")       # Current directory handle
label(0x1071, "fs_lib_flags")         # FS/library flags byte
label(0x1072, "handle_1_fcb")         # Handle 1 FCB index
label(0x1073, "handle_2_fcb")         # Handle 2 FCB index
label(0x1074, "handle_3_fcb")         # Handle 3 FCB index

# FCB station/buffer parallel arrays (&10-byte stride)
label(0x1078, "fcb_stn_lo")           # FCB station lo byte
label(0x1088, "fcb_stn_hi")           # FCB station hi byte (network)
label(0x1098, "fcb_buf_offset")       # FCB buffer offset (negated)
label(0x10A8, "fcb_attr_ref")         # FCB attribute reference
label(0x10B8, "fcb_status")           # FCB status flags

# FCB processing temporaries
label(0x10C8, "cur_fcb_index")        # Current FCB slot index
label(0x10C9, "cur_chan_attr")         # Current channel attribute
label(0x10CA, "cur_attr_ref")         # Current attribute reference
label(0x10CB, "xfer_count_lo")        # Byte counter lo (wipe/transfer)
label(0x10CC, "fcb_buf_page")         # Buffer page address hi byte
label(0x10CD, "xfer_sentinel_1")      # Sentinel byte 1 (wipe/transfer)
label(0x10CE, "xfer_sentinel_2")      # Sentinel byte 2 (wipe/transfer)
label(0x10CF, "xfer_offset")          # Offset counter (wipe/transfer)
label(0x10D0, "xfer_pass_count")      # Pass counter (wipe/transfer)
label(0x10D1, "xfer_counter")         # 3-byte counter array
label(0x10D4, "work_stn_lo")          # Working station lo byte
label(0x10D5, "work_stn_hi")          # Working station hi byte (network)
label(0x10D6, "xfer_flag")            # Transfer flag
label(0x10D7, "osbput_saved_byte")    # Saved data byte for OSBPUT
label(0x10D8, "quote_mode")           # Quote mode tracking flag
label(0x10D9, "fcb_ctx_save")         # FCB context save buffer (13 bytes)

# Display buffer
label(0x10F3, "filename_buf")         # Filename display buffer (12 bytes)

# Other
# UNMAPPED: label(0x6F6E, "false_ref_6f6e")       # (false ref from inline string data)

# ============================================================
# Entry points for relocated code
# ============================================================

# Zero-page relocated code entry points
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0016)

# Page 4 entry points
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0400)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0403)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0406)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0421)

# Page 5 entry points
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0500)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0520)   # tube_osbput
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0527)   # tube_poll_r1_wrch
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x052D)   # tube_osbget
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0537)   # tube_osrdch
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x053A)   # tube_rdch_reply
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x055E)   # tube_osargs
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0562)   # tube_read_params
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0596)   # tube_oscli
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x05A9)   # tube_osfile
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x05D1)   # tube_osgbpb
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x05F2)   # tube_osbyte_2param

# Page 6 entry points
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0600)


# ============================================================
# Code label renames (Phase 3)
# ============================================================

# Data and shared-tail label renames (Phase 3b)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0026, "tube_send_error_num")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0400, "tube_page4_vectors")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0500, "tube_r2_dispatch_table")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0600, "tube_osbyte_reply_block")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06DF, "loop_poll_r1_vdu")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06EF, "setup_tube_vectors")
label(0x8001, "rom_header_byte1")
label(0x8002, "rom_header_byte2")
# UNMAPPED: label(0x8032, "save_registers")
# UNMAPPED: label(0x805D, "set_jsr_protection")
label(0x806C, "econet_restore")
label(0x809A, "adlc_init_done")
label(0x83D4, "loop_count_rxcb_slot")
expr_label(0x83ED, "imm_op_dispatch_lo-&81")  # = &847E - &81
label(0x83FF, "return_from_discard_reset")
label(0x84AE, "jmp_send_data_rx_ack")
label(0x84BE, "set_rx_buf_len_hi")
label(0x853A, "return_from_advance_buf")
label(0x85F8, "reload_inactive_mask")
# UNMAPPED: label(0x8600, "intoff_disable_nmi_op")
label(0x87C4, "tx_check_tdra_ready")
label(0x87EF, "check_tdra_status")
label(0x8924, "check_tx_in_progress")
label(0x8A85, "clear_workspace_byte")
label(0x8A8A, "restore_rom_slot")
# UNMAPPED: label(0x8A3C, "dispatch_service")
label(0x8A9A, "set_adlc_absent")
label(0x8AA1, "check_adlc_flag")
# UNMAPPED: label(0x8A62, "handle_vectors_claimed")
# UNMAPPED: label(0x8A6E, "init_rom_scan")
# UNMAPPED: label(0x8A71, "loop_scan_net_roms")
# UNMAPPED: label(0x8A98, "next_rom_slot")
label(0x8AA9, "dispatch_svc_with_state")
label(0x8AD0, "dispatch_svc_index")
label(0x8AE1, "restore_svc_state")
label(0x8AE7, "restore_romsel_rts")
label(0x8B04, "loop_scan_key_range")
label(0x8B11, "clear_svc_and_ws")
label(0x8B22, "return_from_save_text_ptr")
label(0x8B2F, "loop_sum_rom_bytes")
label(0x8B60, "done_rom_checksum")
label(0x8B65, "loop_copy_fs_ctx")
label(0x8B78, "loop_set_vectors")
label(0x8BA4, "loop_copy_ws_page")
label(0x8BD2, "print_table_newline")
label(0x8BD8, "loop_next_entry")
label(0x8BE0, "print_indent")
# UNMAPPED: label(0x8BC0, "loop_print_name")
label(0x8BF4, "loop_pad_spaces")
label(0x8C06, "loop_print_syntax")
label(0x8C16, "print_syntax_char")
# UNMAPPED: label(0x8BF6, "print_shared_prefix")
# UNMAPPED: label(0x8C00, "loop_next_shared")
# UNMAPPED: label(0x8C06, "loop_print_shared")
# UNMAPPED: label(0x8C12, "print_last_char")
# UNMAPPED: label(0x8C1F, "skip_syntax_bytes")
# UNMAPPED: label(0x8C24, "done_shared_cmds")
label(0x8C1C, "done_entry_newline")
label(0x8C25, "done_print_table")
label(0x8C3A, "loop_indent_spaces")
label(0x8C41, "return_from_help_wrap")
label(0x8C64, "svc_return_unclaimed")
label(0x8C67, "check_help_topic")
label(0x8C71, "match_help_topic")
label(0x8C74, "loop_dispatch_help")
label(0x8C8C, "skip_if_no_match")
label(0x8C96, "version_string_cr")
label(0x8CC6, "return_from_setup_ws_ptr")
label(0x8CD7, "write_key_state")
label(0x8CDD, "select_net_fs")
label(0x8D04, "issue_svc_osbyte")
label(0x8D28, "loop_match_credits")
label(0x8D33, "done_credits_check")
label(0x8D39, "loop_emit_credits")
label(0x8D44, "return_from_credits_check")
label(0x8D45, "credits_keyword_start")
label(0x8D6E, "ps_template_base")
label(0x8DC0, "skip_no_fs_addr")
label(0x8DC7, "loop_copy_logon_cmd")
label(0x8DD8, "scan_pass_prompt")
label(0x8DDA, "loop_scan_colon")
label(0x8DEB, "read_pw_char")
label(0x8DFD, "loop_erase_pw")
label(0x8E04, "check_pw_special")
label(0x8E13, "send_pass_to_fs")
# UNMAPPED: label(0x8E54, "svc_dispatch_lo_offset")
label(0x8E70, "dispatch_rts")
label(0x8ECD, "jmp_osbyte")
label(0x8EEF, "return_from_svc_1_workspace")
label(0x8EF8, "done_cap_ws_count")
label(0x8F56, "loop_zero_workspace")
label(0x8F84, "loop_copy_init_data")
label(0x8FA9, "loop_alloc_handles")
# UNMAPPED: label(0x8F40, "read_station_id")
# UNMAPPED: label(0x8F46, "error_bad_station")
# UNMAPPED: label(0x8F48, "ws_init_data")

# Split the 3 workspace init bytes into individual entries.
# ws_init_data label overlaps the JMP operand high byte at &8F48;
# the actual data bytes at &8F49-&8F4B are read via LDA ws_init_data,X
# with X=3..1 (X=0 never read due to BNE loop exit).
# NB: In 4.08.53 the store base was net_context (&0D6D); in 4.18 it
# changed to fs_flags (&0D6C), shifting all three targets down by one.
# UNMAPPED: for i in range(3):
# UNMAPPED:     byte(0x8F49 + i)
# UNMAPPED: label(0x8F4C, "store_station_id")
label(0x9066, "loop_restore_ctx")
label(0x9083, "loop_checksum_byte")
label(0x908D, "loop_copy_to_ws")
label(0x9090, "store_ws_byte")
label(0x909D, "return_from_fs_shutdown")
label(0x90A6, "loop_sum_ws")
label(0x90F4, "done_print_newline")
label(0x90F8, "cmd_syntax_strings")
label(0x90F8, "syn_opt_dir")     # "(<dir>)"
label(0x9100, "syn_iam")         # "(<stn. id.>) <user id.>..."
label(0x912D, "syn_object")      # "<object>"
# UNMAPPED: label(0x9060, "syn_file_offset") # "<filename> (<offset>...)"
label(0x9159, "syn_dir")         # "<dir>"
# UNMAPPED: label(0x9089, "syn_dir_num")     # "<dir> (<number>)"
label(0x9170, "syn_password")    # "(:<CR>) <password>..."
# UNMAPPED: label(0x90BD, "syn_ps_type")     # "(<stn. id.>|<ps type>)"
label(0x91AA, "syn_access")      # "<object> (L)(W)(R)..."
label(0x91C6, "syn_rename")      # "<filename> <new filename>"
label(0x91E0, "syn_opt_stn")     # "(<stn. id.>)"
# UNMAPPED: label(0x9117, "syn_filename")    # "<filename>"
label(0x91ED, "cmd_syntax_table")
# 12 entries (idx 0-11) in 4.21_v1; 4.18 had 13 because it included
# syn_filename at idx 12. The Master variant drops that command, so the
# byte that follows the table at &91F9 is now the entry point of the
# print_no_spool helper rather than a table value.
for i in range(12):
    byte(0x91ED + i)
# Symbolic expressions: offset = string_start - cmd_syntax_strings - 1
# (the print loop does INY before LDA, so offset points to byte before string)
expr(0x91ED, "syn_iam - cmd_syntax_strings - 2")
# UNMAPPED: expr(0x9123, "(syn_opt_dir - cmd_syntax_strings - 1) AND &FF")
expr(0x91EF, "syn_iam - cmd_syntax_strings - 1")
expr(0x91F0, "syn_object - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x9126, "syn_file_offset - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x9127, "syn_dir - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x9128, "syn_dir_num - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x9129, "syn_password - cmd_syntax_strings - 1")
# UNMAPPED (broken ref): expr(0x91F5, "syn_ps_type - cmd_syntax_strings - 1")
expr(0x91F6, "syn_access - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x912C, "syn_rename - cmd_syntax_strings - 1")
expr(0x91F8, "syn_opt_stn - cmd_syntax_strings - 1")
# UNMAPPED: expr(0x912E, "syn_filename - cmd_syntax_strings - 1")
label(0x9203, "save_regs_for_print_no_spool")  # shared body of print_*_no_spool
label(0x921D, "do_print_no_spool")              # PLP/PLA/PHA + OSASCI/OSWRCH branch
label(0x9227, "print_via_oswrch")               # OSWRCH branch from BVC at &9220
label(0x922A, "restore_spool_and_return")       # final OSBYTE 199 + register pull/RTS
label(0x9769, "always_set_v_byte")              # &FF byte used as `BIT $abs` to set V
label(0x9247, "add_ascii_base")
label(0x9269, "loop_next_char")
label(0x926F, "load_char")
label(0x9287, "resume_caller")
label(0x92BF, "next_hex_char")
label(0x92CA, "check_digit_range")
label(0x92DA, "skip_if_not_hex")
label(0x92DC, "extract_digit_value")
label(0x92F0, "next_dec_char")
label(0x931C, "done_parse_num")
label(0x9325, "validate_station")
label(0x933B, "return_parsed")
label(0x933D, "handle_dot_sep")
label(0x9353, "error_overflow")
label(0x936B, "error_bad_number")
label(0x9377, "error_bad_param")
label(0x9386, "error_bad_net_num")
label(0x93A8, "return_from_digit_test")
label(0x93A9, "not_a_digit")
label(0x93B9, "begin_prot_encode")
label(0x93BD, "loop_encode_prot")
label(0x93C5, "skip_clear_prot")
label(0x93C8, "prot_bit_encode_table")
for i in range(11):
    byte(0x93C8 + i)
label(0x93E8, "loop_cmp_handle")
label(0x93F1, "return_from_cmp_handle")
label(0x93F2, "fscv_7_read_handles")
# UNMAPPED: label(0x92E1, "done_conn_flag")
label(0x9464, "loop_scan_flag")
label(0x946D, "loop_copy_name")
label(0x9479, "append_space")
label(0x9482, "return_from_copy_cmd_name")
label(0x9489, "loop_skip_spaces")
label(0x9492, "check_open_quote")
label(0x949D, "loop_copy_arg_char")
label(0x94AB, "store_arg_char")
label(0x94D3, "loop_copy_rename")
label(0x94DA, "error_bad_rename")
label(0x94E6, "store_rename_char")
label(0x94F3, "skip_rename_spaces")
label(0x9523, "setup_fs_root")
label(0x9525, "loop_copy_fs_num")
label(0x953A, "check_fs_dot")
label(0x9541, "parse_fs_dot_dir")
label(0x9571, "dir_found_send")
label(0x9597, "dir_pass_simple")
label(0x974E, "loop_init_txcb")
label(0x975E, "skip_txcb_dest")
label(0x9763, "txcb_init_template")
for i in range(12):
    byte(0x9763 + i)
label(0x976A, "bit_test_ff")
label(0x9791, "txcb_copy_carry_clr")
label(0x9792, "txcb_copy_carry_set")
label(0x9798, "loop_copy_vset_stn")
label(0x97B0, "use_lib_station")
label(0x97B6, "done_vset_station")
label(0x97D5, "loop_next_reply")
label(0x97DF, "process_reply_code")
label(0x97E1, "return_from_recv_reply")
label(0x97E2, "handle_disconnect")
label(0x97EB, "store_reply_status")
label(0x97F8, "check_data_loss")
label(0x9800, "loop_scan_channels")
# UNMAPPED: label(0x9547, "reload_reply_status")
label(0x9831, "build_error_block")
label(0x983B, "setup_error_copy")
label(0x983D, "loop_copy_error")
label(0x9850, "lang_1_remote_boot")
label(0x9856, "done_commit_state")
label(0x9859, "init_remote_session")
label(0x987E, "lang_3_execute_at_0100")
label(0x989F, "lang_4_remote_validated")
label(0x98AF, "lang_0_insert_remote_key")
label(0x98CF, "init_poll_counters")
label(0x98D5, "loop_poll_tx")
label(0x98F6, "done_poll_tx")
label(0x9908, "return_from_cond_save_err")
label(0x9909, "build_no_reply_error")
label(0x9919, "loop_copy_no_reply_msg")
label(0x9925, "done_no_reply_msg")
label(0x9938, "skip_if_not_a")
label(0x9940, "mask_error_class")
label(0x9957, "loop_copy_station_msg")
label(0x9963, "done_station_msg")
label(0x9975, "suffix_not_listening")
label(0x9977, "load_suffix_offset")
label(0x997B, "loop_copy_suffix")
label(0x9987, "done_suffix")
label(0x9989, "build_simple_error")
label(0x9998, "loop_copy_error_msg")
label(0x999E, "check_msg_terminator")
label(0x99B3, "loop_copy_bad_prefix")
label(0x99CC, "write_error_num_and_str")
label(0x99D6, "loop_copy_inline_str")
label(0x99E9, "trigger_brk")
label(0x99EC, "handle_net_error")
# UNMAPPED: label(0x971F, "close_exec_file")
label(0x9A10, "close_spool_exec")
label(0x9A19, "done_close_files")
label(0x9A21, "loop_copy_channel_msg")
label(0x9A2D, "append_error_number")
label(0x9A54, "append_station_num")
label(0x9A81, "loop_count_digit")
label(0x9A91, "store_digit")
label(0x9A99, "return_from_store_digit")
label(0x9A9A, "net_error_lookup_data")
for i in range(12):
    byte(0x9A9A + i)
# Symbolic offsets into error_msg_table
# UNMAPPED (broken ref): expr(0x9A9A, "error_msg_table - error_msg_table")
# UNMAPPED (broken ref): expr(0x9A9B, "msg_net_error - error_msg_table")
# UNMAPPED: expr(0x97AF, "msg_station - error_msg_table")
# UNMAPPED: expr(0x97B0, "msg_no_clock - error_msg_table")
# UNMAPPED (broken ref): expr(0x9A9E, "msg_escape - error_msg_table")
# UNMAPPED (broken ref): expr(0x9A9F, "msg_escape - error_msg_table")
# UNMAPPED (broken ref): expr(0x9AA0, "msg_escape - error_msg_table")
# UNMAPPED (broken ref): expr(0x9AA1, "msg_bad_option - error_msg_table")
# UNMAPPED (broken ref): expr(0x9AA2, "msg_no_reply - error_msg_table")
# UNMAPPED (broken ref): expr(0x9AA3, "msg_not_listening - error_msg_table")
# UNMAPPED: expr(0x97B7, "msg_on_channel - error_msg_table")
# UNMAPPED (broken ref): expr(0x9AA5, "msg_not_present - error_msg_table")
label(0x9B33, "set_timeout")
label(0x9B3C, "start_tx_attempt")
label(0x9B52, "loop_retry_tx")
label(0x9B58, "loop_tx_delay")
label(0x9B60, "try_alternate_phase")
label(0x9B6B, "tx_send_error")
label(0x9B6F, "tx_success")
label(0x9B75, "pass_txbuf_init_table")
for i in range(12):
    byte(0x9B75 + i)
label(0x9B8B, "loop_copy_template")
label(0x9B98, "skip_template_byte")
label(0x9BA5, "start_pass_tx")
label(0x9BB1, "done_pass_retries")
label(0x9BC6, "loop_poll_pass_tx")
label(0x9BCB, "restore_retry_state")
label(0x9BD8, "loop_pass_tx_delay")
label(0x9BE0, "pass_tx_success")
label(0x9BE5, "loop_restore_txbuf")
label(0x9BEF, "skip_restore_byte")
label(0x9BF7, "loop_copy_text_ptr")
label(0x9C08, "loop_gsread_char")
label(0x9C13, "terminate_buf")
label(0x9C39, "copy_arg_and_enum")
label(0x9C56, "copy_ws_then_fsopts")
label(0x9C5C, "setup_txcb_addrs")
label(0x9C5E, "loop_copy_addrs")
label(0x9C79, "loop_copy_offsets")
label(0x9C8E, "loop_swap_and_send")
label(0x9C90, "loop_copy_start_end")
label(0x9CA4, "loop_verify_addrs")
label(0x9CAF, "return_from_txcb_swap")
label(0x9CB0, "check_display_type")
label(0x9CB5, "setup_dir_display")
label(0x9CBA, "loop_compute_diffs")
label(0x9CD8, "loop_copy_fs_options")
label(0x9CF9, "send_info_request")
label(0x9D06, "setup_txcb_transfer")
label(0x9D0C, "recv_reply")
label(0x9D0F, "store_result")
label(0x9D1C, "loop_copy_file_info")
label(0x9D1F, "store_prot_byte")
label(0x9D2D, "loop_print_filename")
label(0x9D51, "loop_print_hex_byte")
label(0x9D61, "loop_copy_fsopts_byte")
label(0x9D70, "return_from_advance_y")
label(0x9D74, "loop_copy_ws_byte")
label(0x9D83, "discard_handle_match")
label(0x9D8D, "init_transfer_addrs")
label(0x9D98, "loop_copy_addr_offset")
label(0x9DAA, "loop_check_vs_limit")
label(0x9DB6, "clamp_end_to_limit")
label(0x9DB8, "loop_copy_limit")
label(0x9DBF, "set_port_and_ctrl")
label(0x9DDC, "dispatch_osword_op")
label(0x9DE8, "dispatch_ops_1_to_6")
label(0x9E00, "loop_copy_fsopts_4")
label(0x9E0D, "setup_save_access")
label(0x9E17, "loop_copy_fsopts_8")
label(0x9E22, "send_save_or_access")
label(0x9E29, "send_delete_request")
label(0x9E2E, "send_request_vset")
label(0x9E34, "skip_if_error")
label(0x9E39, "setup_write_access")
label(0x9E43, "read_cat_info")
label(0x9E65, "loop_copy_cat_info")
label(0x9E72, "loop_copy_ext_info")
label(0x9E7E, "return_with_handle")
label(0x9E7F, "done_osword_op")
label(0x9E89, "loop_copy_cmdline_char")
label(0x9E95, "pad_with_spaces")
label(0x9EA0, "loop_copy_buf_char")
label(0x9EA2, "copy_from_buf_entry")
label(0x9EBD, "validate_chan_close")
label(0x9EC2, "error_invalid_chan")
label(0x9EC5, "check_chan_range")
label(0x9ED5, "loop_copy_fcb_fields")
label(0x9EE5, "dispatch_osfind_op")
label(0x9EF0, "osfind_with_channel")
label(0x9F22, "loop_copy_zp_to_buf")
label(0x9F38, "done_return_flag")
label(0x9F3B, "osargs_read_op")
label(0x9F4A, "loop_copy_reply_to_zp")
label(0x9F57, "osargs_ptr_dispatch")
label(0x9F79, "osargs_write_ptr")
label(0x9F80, "loop_copy_ptr_to_buf")
label(0x9FB1, "close_all_fcbs")
label(0x9FC2, "osfind_close_or_open")
# UNMAPPED: label(0x9CE0, "loop_copy_reply_data")
label(0x9FCD, "done_file_open")
label(0x9FCF, "clear_result")
label(0x9FD1, "shift_and_finalise")
label(0x9FD4, "alloc_fcb_for_open")
label(0xA00B, "loop_shift_filename")
label(0xA04C, "check_open_mode")
label(0xA05E, "alloc_fcb_with_flags")
label(0xA062, "store_fcb_flags")
label(0xA068, "done_osfind")
label(0xA06B, "close_all_channels")
label(0xA084, "close_specific_chan")
label(0xA08A, "send_close_request")
label(0xA09C, "done_close")
label(0xA09F, "clear_single_fcb")
label(0xA0A9, "fscv_0_opt_entry")
label(0xA0B3, "osargs_dispatch")
label(0xA0B6, "store_display_flag")
label(0xA0BB, "error_osargs")
label(0xA0C0, "send_osargs_request")
label(0xA10B, "fscv_1_eof")
label(0xA126, "mark_not_found")
label(0xA128, "restore_and_return")
label(0xA136, "loop_adjust_byte")
label(0xA142, "subtract_ws_byte")
label(0xA145, "store_adjusted_byte")
label(0xA15F, "skip_if_out_of_range")
label(0xA162, "valid_osgbpb_op")
label(0xA16D, "load_chan_handle")
label(0xA1AC, "set_write_active")
label(0xA1AF, "setup_gbpb_request")
label(0xA205, "loop_copy_opts_to_buf")
label(0xA210, "skip_struct_hole")
label(0xA219, "store_direction_flag")
label(0xA227, "store_port_and_send")
label(0xA244, "loop_setup_addr_bytes")
label(0xA25B, "loop_copy_offset")
label(0xA26F, "send_with_swap")
label(0xA272, "recv_and_update")
label(0xA28A, "send_osbput_data")
label(0xA29F, "write_block_entry")
label(0xA2AD, "store_station_result")
label(0xA2AF, "loop_copy_opts_to_ws")
label(0xA2C1, "handle_cat_update")
label(0xA2F5, "loop_copy_to_host")
label(0xA302, "tube_write_setup")
label(0xA30F, "set_tube_addr")
label(0xA314, "loop_write_to_tube")
label(0xA31D, "loop_tube_delay")
label(0xA32C, "update_cat_position")
label(0xA368, "clear_buf_after_write")
label(0xA36A, "loop_clear_buf")
label(0xA384, "loop_check_remaining")
label(0xA38D, "done_write_block")
label(0xA3B8, "print_current_fs")
label(0xA3DA, "store_station_lo")
label(0xA3E1, "skip_if_no_station")
# UNMAPPED: label(0xA0C9, "done_parse_fs_ps")
label(0xA3FF, "net_1_read_handle")
label(0xA405, "net_2_read_handle_entry")
label(0xA410, "return_zero_uninit")
label(0xA412, "store_pb_result")
label(0xA415, "net_3_close_handle")
label(0xA424, "mark_ws_uninit")
label(0xA44E, "dispatch_fs_cmd")
label(0xA45D, "restart_table_scan")
label(0xA465, "loop_match_char")
label(0xA474, "skip_entry_chars")
label(0xA480, "loop_skip_to_next")
label(0xA485, "check_separator")
label(0xA48B, "loop_check_sep_table")
label(0xA497, "sep_table_data")
# UNMAPPED: for i in range(9):
# UNMAPPED (orphan body):     byte(0xA497 + i)
# UNMAPPED: label(0xA185, "separator_matched")
label(0xA4A2, "loop_skip_trail_spaces")
label(0xA4A8, "skip_dot_and_spaces")
label(0xA4AC, "check_cmd_flags")
label(0xA4BD, "clear_v_flag")
label(0xA4BE, "clear_c_flag")
label(0xA4BF, "return_with_result")
label(0xA4C3, "loop_scan_past_word")
label(0xA4C4, "check_char_type")
label(0xA4D2, "skip_sep_spaces")
label(0xA4D9, "set_c_and_return")
label(0xA4E4, "fscv_2_star_run")
label(0xA4FF, "open_file_for_run")
label(0xA517, "loop_check_handles")
label(0xA51F, "alloc_run_fcb")
label(0xA53B, "done_run_dispatch")
label(0xA53E, "try_library_path")
label(0xA552, "loop_find_name_end")
label(0xA55A, "loop_shift_name_right")
label(0xA565, "loop_copy_lib_prefix")
label(0xA576, "retry_with_library")
label(0xA578, "restore_filename")
label(0xA57A, "loop_restore_name")
label(0xA58F, "library_tried")
label(0xA5AE, "check_exec_addr")
label(0xA5B0, "loop_check_exec_bytes")
label(0xA5C3, "alloc_run_channel")
label(0xA5D7, "library_dir_prefix")
# UNMAPPED: label(0xA299, "setup_oscli_arg")
label(0xA5E8, "loop_read_gs_string")
label(0xA5EE, "loop_skip_trailing")
label(0xA633, "dispatch_via_vector")
label(0xA63E, "fsreply_5_set_lib")
label(0xA647, "loop_search_stn_bit2")
label(0xA65D, "done_search_bit2")
label(0xA66B, "set_flags_bit2")
label(0xA672, "loop_search_stn_bit3")
label(0xA688, "done_search_bit3")
label(0xA696, "set_flags_bit3")
label(0xA6A9, "loop_search_stn_boot")
label(0xA6BF, "done_search_boot")
label(0xA6CD, "set_flags_boot")
label(0xA6CF, "store_stn_flags_restore")
label(0xA6D2, "jmp_restore_fs_ctx")
label(0xA6D5, "fsreply_1_copy_handles_boot")
label(0xA6E5, "fsreply_2_copy_handles")
label(0xA726, "check_auto_boot_flag")
# UNMAPPED: label(0xA3DF, "boot_oscli_lo_table")

# Split the 4-byte boot OSCLI address table into individual bytes.
# Low bytes of boot command string addresses in page &A3.
# Indexed by boot option (1-3); entry 0 is a don't-care (BEQ skips).
# UNMAPPED: for i in range(4):
# UNMAPPED:     byte(0xA3DF + i)
# UNMAPPED: label(0xA3E3, "load_boot_type")
# UNMAPPED: label(0xA3F1, "cmd_table_fs_lo")
# UNMAPPED: label(0xA3F2, "cmd_table_fs_hi")
label(0xA7C9, "cmd_table_nfs_iam")
label(0xBEEB, "loop_copy_osword_data")
# Removed in 4.18: loop_copy_osword_flag (copy-back loop eliminated)
label(0xA870, "return_from_osword_setup")
# UNMAPPED: comment(0xA523, """\
# UNMAPPED: OSWORD dispatch table (7 entries, split lo/hi).
# UNMAPPED: PHA/PHA/RTS dispatch used by svc_8_osword.
# UNMAPPED: Maps OSWORD codes &0E-&14 to handler routines.""")

# UNMAPPED: label(0xA523, "osword_dispatch_lo_table")
# UNMAPPED: label(0xA52A, "osword_dispatch_hi_table")

# Mark OSWORD dispatch table entries as symbolic address pairs.
# UNMAPPED: for i in range(7):
# UNMAPPED:     rts_code_ptr(0xA523 + i, 0xA52A + i)

# UNMAPPED: comment(0xA523, "lo-&0E: Read clock", inline=True)
# UNMAPPED: comment(0xA523, "lo-&13: Misc operations", inline=True)
# UNMAPPED: comment(0xA52B, "hi-&0E: Read clock", inline=True)
# UNMAPPED: comment(0xA52C, "hi-&0F: (unimplemented)", inline=True)
# UNMAPPED: comment(0xA52D, "hi-&10: Transmit", inline=True)
# UNMAPPED: comment(0xA52F, "hi-&12: Read station info", inline=True)
comment(0xA874, "hi-&14: Bridge/net config", inline=True)

label(0xA874, "osword_0e_handler")
label(0xA890, "return_from_osword_0e")
label(0xA891, "save_txcb_and_convert")
label(0xA8DE, "loop_copy_bcd_to_pb")
label(0xA908, "loop_bcd_add")
label(0xA90E, "done_bcd_convert")
label(0xA910, "osword_10_handler")
label(0xA919, "setup_ws_rx_ptrs")
label(0xA92D, "osword_11_handler")
label(0xA93D, "loop_find_rx_slot")
label(0xA951, "store_rx_slot_found")
label(0xA956, "use_specified_slot")
label(0xA96C, "loop_copy_slot_data")
label(0xA96D, "copy_pb_and_mark")
label(0xA97A, "increment_and_retry")
label(0xA97F, "store_rx_result")
label(0xA981, "osword_11_done")
label(0xA985, "osword_12_handler")
label(0xA99A, "osword_13_dispatch")
label(0xA9A7, "return_from_osword_13")
# UNMAPPED: label(0xA63C, "osword_13_lo_table")
# UNMAPPED: label(0xA64E, "osword_13_hi_table")

# OSWORD &13 PHA/PHA/RTS dispatch table (18 entries, sub-codes 0-&11).
# UNMAPPED: for i in range(18):
# UNMAPPED:     rts_code_ptr(0xA63C + i, 0xA64E + i)

# Entry points for handlers in the &A663-&A6EA region (currently data).
# UNMAPPED: entry(0xA660)   # Sub 0
# UNMAPPED: entry(0xA673)   # Sub 1
entry(0xAA72)   # Sub 12
entry(0xAA75)   # Sub 13

# UNMAPPED: label(0xA665, "nfs_inactive_exit")
label(0xA9CF, "read_station_bytes")
label(0xA9D1, "loop_copy_station")
label(0xA9E4, "loop_store_station")
label(0xA9FB, "scan_fcb_entry")
label(0xAA2A, "check_handle_2")
label(0xAA44, "check_handle_3")
label(0xAA5E, "store_updated_status")
label(0xAA62, "next_fcb_entry")
label(0xAA76, "setup_csd_copy")
label(0xAA88, "copy_ws_byte_to_pb")
label(0xAAB1, "return_from_write_ws_pair")
label(0xAAC7, "loop_copy_handles")
# UNMAPPED: label(0xA749, "return_zero_in_pb")
label(0xAAD3, "start_set_handles")
label(0xAAD5, "validate_handle")
label(0xAAE5, "handle_invalid")
label(0xAAEC, "check_handle_alloc")
label(0xAB12, "next_handle_slot")
label(0xAB19, "assign_handle_2")
label(0xAB30, "assign_handle_3")
label(0xAB47, "loop_scan_fcb_flags")
label(0xAB59, "no_flag_match")
label(0xAB5A, "clear_flag_bits")
label(0xAB62, "next_flag_entry")
label(0xAB82, "store_a_to_pb_1")
label(0xABBB, "bridge_found")
label(0xABC4, "compare_bridge_status")
# UNMAPPED: label(0xA841, "bridge_ws_init_data")
label(0xABCB, "use_default_station")
label(0xABCE, "store_bridge_station")
label(0xABD0, "return_from_bridge_query")
label(0xABD1, "bridge_txcb_init_table")
label(0xABDD, "bridge_rxcb_init_data")
for i in range(4):
    byte(0xABD1 + i)
# bytes 4-9 are "BRIDGE" — leave as equs
# UNMAPPED: for i in range(14):
# UNMAPPED:     byte(0xA857 + i)
label(0xABF9, "loop_copy_bridge_init")
label(0xAC0D, "loop_wait_ws_status")
label(0xAC21, "loop_wait_tx_done")
label(0xAC37, "bridge_responded")
label(0xAC46, "return_from_bridge_poll")
label(0xAC47, "osword_14_handler")
label(0xAC55, "loop_copy_txcb_init")
label(0xAC5D, "store_txcb_init_byte")
label(0xAC85, "loop_copy_ws_to_pb")
label(0xACB7, "handle_tx_request")
label(0xACCE, "loop_send_pb_chars")
label(0xACE4, "loop_bridge_tx_delay")
label(0xACED, "handle_burst_xfer")
label(0xAD0E, "restore_regs_return")
# UNMAPPED: label(0xA99E, "osword_handler_lo_table")
# UNMAPPED: label(0xA9A7, "osword_handler_hi_table")

# OSWORD handler PHA/PHA/RTS dispatch table (9 entries, OSWORDs 0-8).
# Dispatched via push_osword_handler_addr (&A981). Each pair of lo/hi bytes
# encodes handler_address-1 for the PHA/PHA/RTS idiom.
# UNMAPPED: for i in range(9):
# UNMAPPED:     rts_code_ptr(0xA99E + i, 0xA9A7 + i)
# UNMAPPED: comment(0xA99E, "OSWORD handler dispatch table\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "9-entry PHA/PHA/RTS table for OSWORD numbers\n"
# UNMAPPED:     "0-8. push_osword_handler_addr indexes by the\n"
# UNMAPPED:     "OSWORD number, pushes the handler address-1,\n"
# UNMAPPED:     "then RTS dispatches to the handler with the\n"
# UNMAPPED:     "OSWORD number reloaded in A.")
# UNMAPPED: comment(0xA9A7, "hi OSWORD 0: no-op (RTS)", inline=True)
# UNMAPPED: comment(0xA9A8, "hi OSWORD 1: printer spool data", inline=True)
# UNMAPPED: comment(0xA9A9, "hi OSWORD 2: printer spool data", inline=True)
# UNMAPPED: comment(0xA9AA, "hi OSWORD 3: printer spool data", inline=True)
# UNMAPPED: comment(0xA9AB, "hi OSWORD 4: clear carry + abort", inline=True)
# UNMAPPED: comment(0xA9AC, "hi OSWORD 5: spool buffer check", inline=True)
# UNMAPPED: comment(0xA9AD, "hi OSWORD 6: no-op (RTS)", inline=True)
# UNMAPPED: comment(0xA9AE, "hi OSWORD 7: claim/release handler", inline=True)
# UNMAPPED: comment(0xA9AF, "hi OSWORD 8: copy PB + abort", inline=True)

label(0xAD64, "netv_claim_release")
label(0xAD7D, "process_match_result")
label(0xAD86, "save_tube_state")
label(0xAD88, "loop_save_tube_bytes")
label(0xAD9F, "loop_poll_ws_status")
label(0xADAC, "loop_restore_stack")
label(0xADB0, "store_stack_byte")
label(0xADB7, "return_from_claim_release")
label(0xADC0, "return_from_match_rx_code")
label(0xADC1, "osword_claim_codes")

# Split the 18-byte claim codes table into individual bytes for annotation.
for i in range(18):
    byte(0xADC1 + i)
label(0xADDD, "copy_pb_to_ws")
label(0xADE1, "loop_copy_pb_to_ws")
label(0xAE0C, "loop_copy_ws_template")
label(0xAE21, "store_tx_ptr_hi")
label(0xAE23, "select_store_target")
label(0xAE29, "store_via_rx_ptr")
label(0xAE2B, "advance_template_idx")
label(0xAE2F, "done_ws_template_copy")
label(0xAE33, "ws_txcb_template_data")

# Split the 39-byte workspace TXCB template into individual bytes.
# Three overlapping regions indexed by different callers:
#   Wide  (X=&0D, Y=&7C, V=1): bytes [0..13]  → ws+&6F..&7C via net_rx_ptr
#   Narrow (X=&1A, Y=&17, V=0): bytes [14..26] → ws+&0C..&17 via nfs_workspace
#   Spool (X=&26, Y=&0B, V=0): bytes [27..38] → ws+&01..&0B via nfs_workspace
# Markers: &FE=terminate, &FD=skip, &FC=substitute page pointer.
for i in range(39):
    byte(0xAE33 + i)

label(0xAE5A, "netv_spool_check")
label(0xAE6E, "return_from_spool_reset")
label(0xAE6F, "netv_print_data")
label(0xAE7E, "loop_drain_printer_buf")
label(0xAEB5, "done_spool_ctrl")
label(0xAEF7, "check_spool_state")
label(0xAF06, "start_spool_retry")
label(0xAF0B, "loop_copy_spool_tx")
label(0xAF2A, "loop_copy_spool_rx")
label(0xAF37, "store_spool_rx_byte")
label(0xAF39, "advance_spool_rx_idx")
label(0xAF60, "spool_tx_succeeded")
label(0xAF75, "spool_tx_retry")
# UNMAPPED: label(0xAC10, "error_printer_jammed")
label(0xAFB2, "loop_scan_disconnect")
label(0xAFC1, "verify_stn_match")
label(0xAFCC, "send_disconnect_status")
label(0xAFE9, "store_tx_ctrl_byte")
label(0xAFF1, "loop_wait_disc_tx_ack")
label(0xB002, "tx_econet_txcb_template")

# Split the 12-byte spool TX control block template into individual bytes.
# Simple copy (no marker processing) to workspace offset &21..&2C via
# (net_rx_ptr),Y. Destination station/network filled in afterwards.
for i in range(12):
    byte(0xB002 + i)

label(0xB00E, "rx_palette_txcb_template")

# Split the 12-byte spool RX control block template into individual bytes.
# Copied with marker processing: &FD=skip, &FC=substitute net_rx_ptr_hi.
for i in range(12):
    byte(0xB00E + i)
label(0xB01A, "lang_2_save_palette_vdu")
label(0xB031, "loop_read_palette")
# UNMAPPED: label(0xAD0D, "osbyte_mode_read_codes")

# Split the 3-byte OSBYTE code table into individual bytes.
# Indexed by read_osbyte_to_ws to read display mode state.
# UNMAPPED: for i in range(3):
# UNMAPPED:     byte(0xAD0D + i)
label(0xB0B1, "parse_cdir_size")
label(0xB0BA, "loop_find_alloc_size")
label(0xB0C0, "done_cdir_size")
# UNMAPPED: label(0xAD43, "cdir_alloc_size_table")

# Split the 27-byte *CDir allocation size threshold table into
# individual bytes for annotation. Table base (cdir_dispatch_col+2) overlaps
# with the JMP operand high byte; data bytes run &AD32-&AD4C.
for i in range(27):
    byte(0xB0D5 + i)

label(0xB107, "ex_set_lib_flag")
label(0xB118, "fscv_5_cat")
label(0xB121, "cat_set_lib_flag")
label(0xB12E, "setup_ex_request")
label(0xB14A, "store_owner_flags")
label(0xB17B, "print_public_label")
# UNMAPPED: label(0xADED, "send_dir_info_req")
# UNMAPPED: label(0xAE1C, "loop_print_option_str")
label(0xB1BF, "print_dir_header")
label(0xB1E7, "setup_ex_pagination")
label(0xB207, "loop_scan_entry_data")
label(0xB227, "jmp_osnewl")
label(0xB255, "loop_shift_str_left")
label(0xB263, "loop_trim_trailing")
label(0xB272, "done_strip_prefix")
label(0xB274, "return_from_strip_prefix")
label(0xB275, "check_hash_prefix")
label(0xB279, "error_bad_prefix")
label(0xB27C, "check_colon_prefix")
label(0xB28B, "set_fs_select_flag")
label(0xB298, "option_str_offset_data")
# UNMAPPED: label(0xAEFF, "roff_off_string")
label(0xB2A4, "loop_copy_char")
label(0xB2B1, "restore_after_check")
label(0xB2B3, "advance_positions")
# UNMAPPED: label(0xAF3E, "fsreply_0_print_dir")
label(0xB2DD, "loop_scan_entries")
# UNMAPPED: label(0xAF5A, "print_col_newline")
# UNMAPPED: label(0xAF5C, "print_entry_char")
# UNMAPPED: label(0xAF5F, "next_col_entry")
# UNMAPPED: label(0xAF72, "done_extra_arg_check")
label(0xB33F, "loop_divide_digit")
label(0xB34F, "print_nonzero_digit")
label(0xB37E, "loop_advance_char")
label(0xB38B, "loop_skip_space_chars")
label(0xB3B6, "done_ps_available")
label(0xB3D9, "loop_copy_ps_tmpl")
label(0xB3E3, "no_ps_name_given")
label(0xB3E6, "save_ps_cmd_ptr")
label(0xB3F0, "loop_pad_ps_name")
label(0xB408, "loop_read_ps_char")
label(0xB416, "done_ps_name_parse")
label(0xB429, "loop_pop_ps_slot")
label(0xB44F, "done_ps_slot_mark")
label(0xB457, "done_ps_scan")
label(0xB46C, "print_ps_now")
# UNMAPPED: label(0xB0B6, "done_ps_status_msg")
label(0xB477, "store_ps_station")
label(0xB498, "print_server_is_suffix")
label(0xB4C6, "loop_scan_ps_slots")
label(0xB4D6, "skip_next_ps_slot")
label(0xB4DA, "reinit_ps_slot")
# UNMAPPED: label(0xB13F, "write_ps_slot_link_addr")
label(0xB502, "done_ps_slot_scan")
label(0xB511, "loop_ps_delay")
label(0xB52D, "loop_push_ps_name")
label(0xB537, "loop_pop_ps_name")
label(0xB549, "loop_copy_tx_hdr")
label(0xB552, "ps_tx_header_template")

# Split the 4-byte PS TX header template into individual bytes.
for i in range(4):
    byte(0xB552 + i)

label(0xB566, "skip_if_local_net")
# UNMAPPED: label(0xB1B1, "print_station_only")
label(0xB575, "ps_slot_txcb_template")

# Split the 12-byte PS slot TXCB template into individual bytes.
for i in range(12):
    byte(0xB575 + i)
label(0xB5C3, "no_poll_name_given")
label(0xB5C6, "skip_if_no_poll_arg")
label(0xB5CE, "loop_pad_poll_name")
label(0xB5E6, "loop_read_poll_char")
label(0xB5F4, "done_poll_name_parse")
label(0xB611, "loop_print_poll_name")
label(0xB61F, "done_poll_name_print")
# UNMAPPED: label(0xB267, "loop_pop_poll_slot")
label(0xB65A, "check_poll_jammed")
label(0xB65E, "print_poll_jammed")
label(0xB66A, "check_poll_busy")
label(0xB69A, "done_poll_status_line")
label(0xB69D, "done_poll_slot_mark")
label(0xB6A8, "loop_copy_slot_tmpl")
label(0xB6B3, "subst_rx_page_byte")
label(0xB6B5, "store_slot_tmpl_byte")
label(0xB6CB, "done_uppercase_store")
# UNMAPPED: label(0xB316, "parse_prot_keywords")
label(0xB6EE, "loop_match_prot_attr")
# UNMAPPED: label(0xB32C, "prot_check_arg_end")
# UNMAPPED: label(0xB335, "done_prot_args")
# UNMAPPED: label(0xB336, "store_prot_mask")
# UNMAPPED: label(0xB347, "loop_match_unprot_attr")
label(0xB703, "request_next_wipe")
label(0xB736, "check_wipe_attr")
label(0xB739, "loop_check_if_locked")
label(0xB73D, "skip_wipe_locked")
label(0xB742, "check_wipe_dir")
label(0xB74B, "show_wipe_prompt")
label(0xB74F, "loop_copy_wipe_name")
label(0xB773, "loop_print_wipe_info")
label(0xB787, "check_wipe_response")
label(0xB799, "loop_build_wipe_cmd")
label(0xB7A2, "skip_if_not_space")
label(0xB7A6, "set_wipe_cr_end")
label(0xB7A8, "store_wipe_tx_char")
label(0xB7B7, "skip_wipe_to_next")
label(0xB7BD, "use_wipe_leaf_name")
label(0xB7BE, "loop_copy_wipe_leaf")
label(0xB7E6, "loop_clear_chan_table")
label(0xB7F6, "loop_mark_chan_avail")
label(0xB80F, "error_chan_out_of_range")
label(0xB811, "return_chan_index")
label(0xB81D, "error_chan_not_found")
# UNMAPPED: label(0xB487, "net_channel_err_string")
label(0xB85B, "error_chan_not_here")
label(0xB866, "loop_copy_chan_err_str")
label(0xB879, "loop_append_err_suffix")
label(0xB8AB, "loop_scan_fcb_slots")
label(0xB8B9, "done_found_free_slot")
label(0xB8F6, "return_alloc_success")
label(0xB8F9, "skip_set_carry")
label(0xB8FE, "loop_scan_fcb_down")
label(0xB902, "skip_if_slots_done")
label(0xB916, "done_check_station")
label(0xB93A, "loop_find_fcb")
label(0xB941, "skip_if_no_wrap")
label(0xB94B, "done_check_fcb_status")
label(0xB955, "done_select_fcb")
label(0xB956, "loop_scan_empty_fcb")
label(0xB95D, "done_test_empty_slot")
label(0xB96C, "skip_if_modified_fcb")
label(0xB989, "loop_clear_counters")
label(0xB9DA, "done_restore_offset")
label(0xBA00, "done_clear_fcb_active")
label(0xBA0B, "loop_save_tx_context")
label(0xBA1E, "done_save_context")
label(0xBA21, "loop_find_pending_fcb")
label(0xBA65, "done_init_wipe")
label(0xBA89, "done_calc_offset")
label(0xBAA8, "loop_clear_buffer")
label(0xBAAD, "done_set_fcb_active")
label(0xBAB7, "loop_restore_workspace")
label(0xBAC2, "loop_restore_tx_buf")
label(0xBACC, "loop_save_before_match")
label(0xBAD1, "loop_reload_attr")
label(0xBAD4, "loop_next_fcb_slot")
label(0xBAEE, "done_test_fcb_active")
label(0xBB27, "return_test_offset")
label(0xBB48, "loop_process_fcb")
label(0xBB53, "done_flush_fcb")
label(0xBB58, "done_advance_fcb")
label(0xBB87, "done_read_fcb_byte")
label(0xBBB1, "error_end_of_file")
label(0xBBC2, "done_load_from_buf")
label(0xBC14, "done_test_write_flag")
label(0xBC22, "done_find_write_fcb")
label(0xBC32, "done_check_buf_offset")
label(0xBC46, "done_set_dirty_flag")
label(0xBC65, "done_inc_byte_count")
label(0xBCEF, "loop_copy_wipe_err_msg")
label(0xBCFC, "done_terminate_wipe_err")
label(0xBD05, "done_toggle_station")
# UNMAPPED: label(0xB9A0, "open_and_read_file")


# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0406, "tube_addr_data_dispatch")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0421, "clear_tube_claim")
label(0x83E5, "discard_reset_rx")
label(0x83E8, "reset_adlc_rx_listen")
label(0x83EB, "set_nmi_rx_scout")
label(0x8512, "setup_sr_tx")
# UNMAPPED: label(0x853E, "tx_done_dispatch_lo")
label(0x8549, "tx_done_econet_event")
label(0x8551, "tx_done_fire_event")
label(0x8B00, "scan_remote_keys")
label(0x8B18, "save_text_ptr")
label(0x8BBB, "help_print_nfs_cmds")
label(0x8BC6, "print_cmd_table")
label(0x8BD5, "print_cmd_table_loop")
label(0x8C29, "help_wrap_if_serial")
label(0x8C93, "print_version_header")
# UNMAPPED: label(0x8CB9, "get_ws_page")
label(0x8CBD, "setup_ws_ptr")
label(0x8CFD, "notify_new_fs")
label(0x8CFF, "call_fscv")
label(0x8D02, "issue_svc_15")
# UNMAPPED: label(0x8D17, "check_credits_easter_egg")
label(0x8E21, "clear_if_station_match")
label(0x8E2C, "return_from_station_match")
label(0x8E38, "pass_send_cmd")
label(0x8E3C, "send_cmd_and_dispatch")
label(0x8E5B, "dir_op_dispatch")
label(0x8E6A, "push_dispatch_lo")
# UNMAPPED: label(0x8E8C, "osbyte_x0_y0")
label(0x8EF0, "store_ws_page_count")
label(0x903C, "init_adlc_and_vectors")
label(0x904F, "write_vector_entry")
label(0x9064, "restore_fs_context")
label(0x9071, "fscv_6_shutdown")
label(0x909E, "verify_ws_checksum")
label(0x90B5, "error_net_checksum")
# UNMAPPED: label(0x8FF1, "print_station_id")
label(0x9236, "print_hex_byte")
label(0x923F, "print_hex_nybble")
# UNMAPPED: label(0x916E, "parse_addr_arg")
label(0x934A, "err_bad_hex")
label(0x9357, "err_bad_station_num")
label(0x939A, "is_decimal_digit")
label(0x93A2, "is_dec_digit_only")
label(0x93AB, "get_access_bits")
label(0x93B5, "get_prot_bits")
label(0x93D3, "set_text_and_xfer_ptr")
label(0x93D7, "set_xfer_params")
label(0x93DD, "set_options_ptr")
label(0x93E1, "clear_escapable")
label(0x93E6, "cmp_5byte_handle")
label(0x93F7, "set_conn_active")
label(0x940D, "clear_conn_active")
label(0x9437, "error_bad_filename")
label(0x9446, "check_not_ampersand")
label(0x944E, "read_filename_char")
label(0x945E, "send_fs_request")
# UNMAPPED: label(0x9327, "copy_fs_cmd_name")
label(0x9483, "parse_quoted_arg")
label(0x973D, "init_txcb_bye")
label(0x973F, "init_txcb_port")
label(0x974B, "init_txcb")
label(0x976F, "send_request_nowrite")
label(0x9773, "send_request_write")
label(0x978A, "save_net_tx_cb")
label(0x978B, "save_net_tx_cb_vset")
label(0x97B7, "prep_send_tx_cb")
label(0x97CD, "recv_and_process_reply")
# UNMAPPED: label(0x9570, "check_escape")
# UNMAPPED: label(0x9576, "raise_escape_error")
label(0x98BE, "wait_net_tx_ack")
label(0x9900, "cond_save_error_code")
label(0x9930, "fixup_reply_status_a")
label(0x993B, "load_reply_and_classify")
label(0x993D, "classify_reply_error")
label(0x99A2, "bad_str_anchor")
label(0x99DF, "check_net_error_code")
label(0x9A3A, "append_drv_dot_num")
label(0x9A5E, "append_space_and_num")
label(0x9A69, "append_decimal_num")
label(0x9A7A, "append_decimal_digit")
label(0x9B24, "init_tx_ptr_and_send")
label(0x9B2C, "send_net_packet")
label(0x9B81, "init_tx_ptr_for_pass")
label(0x9B89, "setup_pass_txbuf")
label(0x9BF5, "load_text_ptr_and_parse")
label(0x9C00, "gsread_to_buf")
label(0x9C3E, "do_fs_cmd_iteration")
label(0x9C85, "send_txcb_swap_addrs")
label(0x9D44, "print_load_exec_addrs")
label(0x9D4F, "print_5_hex_bytes")
label(0x9D5F, "copy_fsopts_to_zp")
label(0x9D6B, "skip_one_and_advance5")
label(0x9D6C, "advance_y_by_4")
label(0x9D71, "copy_workspace_to_fsopts")
label(0x9D7E, "retreat_y_by_4")
label(0x9D7F, "retreat_y_by_3")
label(0x9D87, "check_and_setup_txcb")
label(0x9E82, "format_filename_field")
label(0x9FB4, "return_with_last_flag")
label(0x9FB6, "finalise_and_return")
label(0xA12C, "update_addr_from_offset9")
label(0xA131, "update_addr_from_offset1")
label(0xA133, "add_workspace_to_fsopts")
label(0xA134, "adjust_fsopts_4bytes")
label(0xA1EF, "lookup_cat_entry_0")
label(0xA1F3, "lookup_cat_slot_data")
label(0xA1FA, "setup_transfer_workspace")
label(0xA2ED, "write_data_block")
label(0xA329, "tail_update_catalogue")
label(0xA390, "tube_claim_c3")
label(0xA3BB, "print_fs_info_newline")
# UNMAPPED: label(0xA0A7, "parse_fs_ps_args")
label(0xA3E7, "get_pb_ptr_as_index")
label(0xA3E9, "byte_to_2bit_index")
label(0xA3FE, "return_from_2bit_index")
label(0xA42F, "fscv_3_star_cmd")
label(0xA440, "cmd_fs_reentry")
label(0xA442, "error_syntax")
label(0xA45B, "match_fs_cmd")
label(0xA592, "error_bad_command")
label(0xA638, "fsreply_3_set_csd")
label(0xA644, "find_station_bit2")
label(0xA66F, "find_station_bit3")
label(0xA6A6, "flip_set_station_boot")
label(0xA764, "boot_cmd_oscli")
label(0xA864, "osword_setup_handler")
label(0xA901, "bin_to_bcd")
label(0xAC67, "store_osword_pb_ptr")
label(0xACAD, "store_ptr_at_ws_y")
label(0xABE9, "init_bridge_poll")
label(0xACF8, "enable_irq_and_poll")
label(0xAD15, "push_osword_handler_addr")
label(0xAD40, "tx_econet_abort")
label(0xADFE, "init_ws_copy_wide")
label(0xAE07, "init_ws_copy_narrow")
label(0xAE0B, "ws_copy_vclr_entry")
label(0xAE64, "reset_spool_buf_state")
label(0xAE94, "append_byte_to_rxbuf")
label(0xAE9D, "handle_spool_ctrl_byte")
label(0xAF80, "err_printer_busy")
label(0xAFA6, "send_disconnect_reply")
label(0xB05F, "commit_state_byte")
label(0xB066, "serialise_palette_entry")
label(0xB081, "read_osbyte_to_ws_x0")
label(0xB083, "read_osbyte_to_ws")
label(0xB0D2, "cdir_dispatch_col")
label(0xB21A, "print_10_chars")
label(0xB22A, "parse_cmd_arg_y0")
label(0xB22C, "parse_filename_arg")
label(0xB22F, "parse_access_prefix")
label(0xB251, "strip_token_prefix")
label(0xB29F, "copy_arg_to_buf_x0")
label(0xB2A1, "copy_arg_to_buf")
label(0xB2A3, "copy_arg_validated")
label(0xB2CA, "return_from_copy_arg")
# UNMAPPED: label(0xAF32, "mask_owner_access")
label(0xB2E4, "ex_print_col_sep")
label(0xB327, "print_num_no_leading")
label(0xB32A, "print_decimal_3dig")
label(0xB338, "print_decimal_digit")
label(0xB356, "return_from_print_digit")
label(0xB373, "save_ptr_to_os_text")
label(0xB37F, "skip_to_next_arg")
label(0xB392, "return_from_skip_arg")
label(0xB393, "save_ptr_to_spool_buf")
label(0xB39E, "init_spool_drive")
label(0xB3D5, "copy_ps_data_y1c")
label(0xB3D7, "copy_ps_data")
label(0xB483, "print_file_server_is")
label(0xB48D, "print_printer_server_is")
label(0xB4A8, "load_ps_server_addr")
label(0xB4B4, "pop_requeue_ps_scan")
label(0xB4FC, "write_ps_slot_hi_link")
label(0xB51C, "write_ps_slot_byte_ff")
label(0xB523, "write_two_bytes_inc_y")
label(0xB52B, "reverse_ps_name_to_tx")
label(0xB556, "print_station_addr")
label(0xB6A5, "return_from_poll_slots")
label(0xB6A6, "init_ps_slot_from_rx")
label(0xB6BD, "store_char_uppercase")
label(0xB7D3, "flush_and_read_char")
# Removed in 4.18: return_from_flush_read, unused_clear_ws_78,
# loop_clear_ws_78 (dead code removed)
label(0xB7E3, "init_channel_table")
label(0xB805, "attr_to_chan_index")
label(0xB814, "check_chan_char")
label(0xB81C, "err_net_chan_invalid")
label(0xB81F, "err_net_chan_not_found")
label(0xB847, "lookup_chan_by_char")
label(0xB886, "store_result_check_dir")
label(0xB88C, "check_not_dir")
# UNMAPPED: label(0xB508, "return_from_dir_check")
label(0xB8A8, "alloc_fcb_slot")
label(0xB8DC, "alloc_fcb_or_error")
label(0xB8F8, "close_all_net_chans")
label(0xB8FC, "scan_fcb_flags")
label(0xB925, "match_station_net")
label(0xB933, "return_from_match_stn")
label(0xB934, "find_open_fcb")
label(0xB977, "init_wipe_counters")
label(0xB99A, "start_wipe_pass")
label(0xBA09, "save_fcb_context")
label(0xBAC0, "restore_catalog_entry")
label(0xBACF, "find_matching_fcb")
label(0xBB2A, "inc_fcb_byte_count")
label(0xBB37, "return_from_inc_fcb_count")
# UNMAPPED: label(0xB799, "process_all_fcbs")
label(0xBCBC, "send_wipe_request")
label(0xBD15, "send_and_receive")
# UNMAPPED: label(0xB9AA, "loop_read_print_byte")
# UNMAPPED: label(0xB9B6, "done_print_escape")
# UNMAPPED: label(0xB9C5, "done_store_prev_char")
# UNMAPPED: label(0xB9C7, "loop_write_char")
# UNMAPPED: label(0xB9CD, "done_handle_line_end")
# UNMAPPED: label(0xB9DA, "done_normalise_crlf")
# UNMAPPED: label(0xB9E7, "done_write_newline")
# UNMAPPED: label(0xB9ED, "done_check_cr_lf")
# UNMAPPED: label(0xB9F4, "done_check_lf_cr")
# UNMAPPED: label(0xB9F9, "done_consume_pair")
label(0xBD25, "abort_if_escape")
label(0xBD2A, "error_escape_pressed")
label(0xBD48, "loop_push_zero_buf")
label(0xBD59, "loop_dump_line")
label(0xBD60, "loop_read_dump_byte")
label(0xBD72, "done_check_dump_eof")
label(0xBD79, "loop_pop_stack_buf")
label(0xBD80, "done_check_boundary")
label(0xBD8B, "done_start_dump_addr")
label(0xBD8D, "loop_print_addr_byte")
label(0xBD9E, "loop_inc_dump_addr")
label(0xBDB6, "loop_print_dump_hex")
label(0xBDBB, "loop_next_dump_col")
label(0xBDCF, "done_print_separator")
label(0xBDDA, "loop_print_dump_ascii")
label(0xBDE2, "skip_non_printable")
label(0xBDE4, "done_test_del")
label(0xBDF3, "done_end_dump_line")
label(0xBDFC, "done_dump_eof")
label(0xBE01, "print_dump_header")
label(0xBE37, "print_hex_and_space")
label(0xBF71, "close_ws_file")
label(0xBF78, "open_file_for_read")
label(0xBE40, "done_print_hex_space")
label(0xBFA6, "loop_skip_filename")
label(0xBFB1, "loop_skip_fn_spaces")
# UNMAPPED: label(0xBB0B, "osasci_offset")
label(0xBE42, "parse_dump_range")
label(0xBE47, "loop_clear_hex_accum")
label(0xBE4E, "loop_parse_hex_digit")
label(0xBE6D, "done_mask_hex_digit")
label(0xBE74, "loop_shift_nibble")
label(0xBE77, "loop_rotate_hex_accum")
label(0xBE98, "error_hex_overflow")
label(0xBE9C, "error_bad_hex_value")
label(0xBEA2, "loop_skip_hex_spaces")
label(0xBEA3, "done_test_hex_space")
label(0xBEAB, "init_dump_buffer")
label(0xBEC4, "loop_cmp_file_length")
label(0xBED0, "done_check_outside")
label(0xBED6, "error_outside_file")
label(0xBEEB, "loop_copy_start_addr")
label(0xBEF0, "done_advance_start")
label(0xBF08, "loop_copy_osfile_ptr")
label(0xBF1B, "loop_shift_osfile_data")
label(0xBF2A, "loop_check_ff_addr")
label(0xBF37, "loop_zero_load_addr")
label(0xBF3E, "done_parse_disp_base")
label(0xBF53, "done_add_disp_base")
label(0xBF58, "loop_add_disp_bytes")
label(0xBF68, "loop_store_disp_addr")
label(0xBFBA, "advance_x_by_8")
label(0xBFBD, "advance_x_by_4")
label(0xBFC0, "inx4")
# UNMAPPED: label(0xBE62, "tube_vdu_dispatch")
# UNMAPPED: label(0xBE73, "loop_poll_r1_vdu_rom")
# UNMAPPED: label(0xBE9E, "loop_copy_reloc_pages")
# UNMAPPED: label(0xBEB8, "loop_copy_zp_workspace")

# ============================================================
# ROM entry points and subroutines
# ============================================================

# Located in 4.21_v1 at &8028 (same address as 4.18). The body
# differs significantly from 4.18: instead of checking VIA IFR bit 2
# for SR-complete, 4.21 reads the workspace byte at &0D65 (a deferred-
# work flag), TRB &FE34 (the Master ACCCON register, clearing bit 7),
# STZ &0D65, then dispatches through the dispatch_svc5 PHA/PHA/RTS at
# &8048 if Y was negative on entry, or fires the Econet RX event
# (&FE) via generate_event and JMPs to &8582 otherwise. The 4.18
# description is preserved with caveats; full re-annotation pending.
entry(0x8028)
subroutine(0x8028, "svc5_irq_check",
    title="Service 5: unrecognised interrupt (Master 128 dispatch)",
    description="Reads the deferred-work flag at &0D65; if zero, returns "
    "early via PLX/PLY/RTS. Otherwise clears bit 7 of the Master 128 "
    "ACCCON register at &FE34 (TRB), zeros &0D65, then dispatches "
    "either via the PHA/PHA/RTS table at dispatch_svc5 (&8048) when "
    "Y had bit 7 set on entry, or fires Econet RX event &FE via "
    "generate_event and JMPs to &8582 (post-event handler).\n"
    "\n"
    "Note: 4.18's equivalent at the same address tested VIA IFR bit 2 "
    "for shift-register completion; the 4.21 version is rewritten "
    "around the Master 128's deferred-work flag pattern. Detailed "
    "re-annotation deferred.",
    on_entry={"a": "5 (service call number)",
              "x": "ROM slot",
              "y": "parameter (high bit selects dispatch path)"})
subroutine(0x8045, "generate_event",
    title="Generate event via event vector",
    description="Dispatches through the event vector (EVNTV)\n"
    "to notify event handlers. Called with the event\n"
    "number in A.",
    on_entry={"A": "event number"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"})

subroutine(0x8A54, "service_handler",
    title="Service call dispatch (Master 128)",
    description="Handles service calls 1, 4, 8, 9, 13, 14, and 15.\n"
    "Service 1: absolute workspace claim.\n"
    "Service 4: unrecognised star command.\n"
    "Service 8: unrecognised OSWORD.\n"
    "Service 9: *HELP.\n"
    "Service 13: ROM initialisation.\n"
    "Service 14: ROM initialisation complete.\n"
    "Service 15: vectors claimed.\n"
    "\n"
    "On Service 15 the ROM verifies the host OS via OSBYTE 0.\n"
    "Only Master 128 (OS 3.2/3.5, X=3) and Master Econet Terminal\n"
    "(OS 4.0, X=4) are supported. Any other version (OS 1.00,\n"
    "OS 1.20, OS 2.00 BBC B+, or OS 5.0 Master Compact) gets a\n"
    "'Bad ROM <slot>' message printed and its workspace byte\n"
    "cleared at &02A0 + adjusted-slot, effectively rejecting the\n"
    "ROM. The 4.18 equivalent at &8A15 instead silently skipped\n"
    "ROM rejection for OS 1.20 and OS 2.00.",
    on_entry={"a": "service call number", "x": "ROM slot", "y": "parameter"})


# ============================================================
# Relocated code labels (from NFS 3.65 correspondence)
# ============================================================
# Pages 4-5 are 100% opcode-identical to NFS 3.65.
# Page 6 is 74% matching. Zero page block is 70% matching.

# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0020, "tube_send_zero_r2")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0029, "tube_brk_send_loop")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x002A, "tube_send_error_byte")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0032, "tube_reset_stack")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0036, "tube_main_loop")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x003B, "tube_handle_wrch")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0041, "tube_poll_r2")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0050, "tube_dispatch_cmd")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0051, "tube_cmd_lo")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0053, "tube_transfer_addr")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0054, "tube_xfer_page")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0055, "tube_xfer_addr_2")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0056, "tube_xfer_addr_3")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0414, "tube_release_claim")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0428, "addr_claim_external")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0432, "accept_new_claim")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0434, "return_tube_init")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0435, "tube_transfer_setup")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0437, "setup_data_transfer")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0446, "send_xfer_addr_bytes")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0463, "skip_r3_flush")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0466, "poll_r4_copro_ack")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0471, "tube_sendw_complete")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x047A, "copro_ack_nmi_check")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0482, "skip_nmi_release")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0483, "return_tube_xfer")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0484, "tube_begin")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x048C, "check_break_type")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0491, "claim_addr_ff")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x049D, "next_rom_page")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04A6, "send_rom_page_bytes")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04BC, "skip_addr_carry")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04C7, "tube_claim_default")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04CE, "tube_init_reloc")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04E1, "scan_copyright_end")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x04F7, "store_xfer_end_addr")
# tube_ctrl_values: 8-byte table of ULA control register values
# (writes to &FEE0) indexed by transfer type (0-7). The LSR/LSR/BCC
# sequence at tube_transfer_setup tests bit 2 of the ctrl byte to
# decide whether a 2-byte R3 FIFO flush is required before the final
# R4 trigger write. Bit 2 is set only for types 0 (&86) and 2 (&96),
# both parasite-to-host transfers -- the flush drains stale bytes
# from the 2-byte R3 FIFO before the parasite starts filling it.
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0518, "tube_ctrl_values")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0520, "tube_osbput")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0527, "tube_poll_r1_wrch")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x052D, "tube_osbget")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0537, "tube_osrdch")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x053A, "tube_rdch_reply")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0542, "tube_osfind")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0552, "tube_osfind_close")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x055E, "tube_osargs")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0562, "tube_read_params")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0564, "read_osargs_params")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0577, "send_osargs_result")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0582, "tube_read_string")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0586, "strnh")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0593, "string_buf_done")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0596, "tube_oscli")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x059C, "tube_reply_ack")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x059E, "tube_reply_byte")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05A6, "mj")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05A9, "tube_osfile")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05AB, "argsw")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05C7, "send_osfile_ctrl_blk")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05D1, "tube_osgbpb")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05D3, "read_osgbpb_ctrl_blk")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05E6, "send_osgbpb_result")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05F2, "tube_osbyte_2param")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x05FC, "tube_poll_r2_result")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0604, "bytex")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0607, "tube_osbyte_long")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x061D, "tube_osbyte_send_y")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0625, "tube_osbyte_short")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0627, "tube_osword")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x062B, "tube_osword_read")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0630, "tube_osbyte_send_x")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0636, "tube_osword_read_lp")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0645, "skip_param_read")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x064C, "poll_r2_osword_result")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0657, "tube_osword_write")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x065A, "tube_osword_write_lp")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0665, "tube_return_main")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0668, "tube_osword_rdln")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x066A, "read_rdln_ctrl_block")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0680, "tube_rdln_send_line")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0687, "tube_rdln_send_loop")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x068A, "tube_rdln_send_byte")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x0695, "tube_send_r2")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x069E, "tube_send_r4")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06A7, "tube_escape_check")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06AD, "tube_event_handler")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06BC, "tube_send_r1")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06C5, "tube_read_r2")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x06EC, "svc_11_nmi_claim")

# ============================================================
# ROM code labels (from NFS 3.65 correspondence)
# ============================================================
# About 27% of NFS 3.65 main ROM opcodes match in ANFS.

# UNMAPPED: label(0x8004, "service_handler_lo")
label(0x801A, "copyright_string")
label(0x8048, "dispatch_svc5")
label(0x804F, "svc_5_unknown_irq")
label(0x8070, "init_nmi_workspace")
label(0x8072, "copy_nmi_shim")
label(0x80B3, "accept_frame")
label(0x80C6, "scout_reject")
label(0x80CE, "accept_local_net")
label(0x80D1, "accept_scout_net")
label(0x80E5, "scout_discard")
label(0x80ED, "scout_loop_rda")
label(0x80FD, "scout_loop_second")
label(0x8138, "scout_no_match")
label(0x813B, "scout_match_port")
label(0x8145, "scan_port_list")
label(0x814E, "scan_nfs_port_list")
label(0x8152, "check_port_slot")
label(0x8154, "scout_ctrl_check")
label(0x8166, "check_station_filter")
label(0x8170, "scout_port_match")
label(0x817A, "next_port_slot")
label(0x8187, "discard_no_match")
label(0x818A, "try_nfs_port_list")
label(0x8195, "port_match_found")
label(0x81A7, "send_data_rx_ack")
label(0x81B8, "data_rx_setup")
label(0x81D6, "nmi_data_rx_net")
label(0x81EC, "nmi_data_rx_skip")
label(0x81F7, "install_data_rx_handler")
label(0x820A, "install_tube_rx")
label(0x8215, "nmi_error_dispatch")
label(0x821D, "rx_error_reset")
label(0x8228, "data_rx_loop")
label(0x8241, "read_sr2_between_pairs")
label(0x8248, "read_second_rx_byte")
label(0x825C, "check_sr2_loop_again")
label(0x827F, "read_last_rx_byte")
label(0x828E, "send_ack")
label(0x8291, "nmi_data_rx_tube")
label(0x8294, "rx_tube_data")
label(0x82B1, "data_rx_tube_error")
label(0x82B4, "data_rx_tube_complete")
label(0x82EA, "ack_tx_configure")
label(0x82F8, "ack_tx_write_dest")
label(0x8339, "start_data_tx")
label(0x833C, "dispatch_nmi_error")
label(0x833F, "advance_rx_buffer_ptr")
label(0x834A, "add_rxcb_ptr")
label(0x8378, "inc_rxcb_ptr")
label(0x8383, "skip_tube_update")
label(0x8385, "return_rx_complete")
label(0x8395, "rx_complete_update_rxcb")
label(0x839A, "add_buf_to_base")
label(0x83A1, "inc_rxcb_buf_hi")
label(0x83A3, "store_buf_ptr_lo")
label(0x83A5, "store_rxcb_buf_ptr")
label(0x83AA, "store_rxcb_buf_hi")
label(0x83AC, "skip_buf_ptr_update")
label(0x8400, "copy_scout_to_buffer")
label(0x8406, "copy_scout_select")
label(0x8416, "copy_scout_bytes")
label(0x8424, "next_scout_byte")
label(0x842B, "scout_copy_done")
label(0x8436, "copy_scout_via_tube")
label(0x8448, "release_tube")
label(0x8451, "clear_release_flag")
label(0x846B, "rotate_prot_mask")
label(0x8471, "dispatch_imm_op")
label(0x847C, "scout_page_overflow")
label(0x8482, "check_scout_done")
label(0x8488, "imm_op_out_of_range")
label(0x84A5, "copy_addr_loop")
label(0x84B1, "svc5_dispatch_lo")
label(0x84E0, "set_tx_reply_flag")
label(0x84E8, "rx_imm_halt_cont")
label(0x84ED, "tx_cr2_setup")
label(0x84F2, "tx_nmi_setup")
label(0x84F9, "imm_op_build_reply")
label(0x8529, "imm_op_discard")
label(0x8573, "halt_spin_loop")
label(0x8582, "tx_done_exit")
label(0x8589, "tx_begin")
label(0x85A1, "tx_imm_op_setup")
label(0x85B5, "calc_peek_poke_size")
label(0x85CC, "tx_ctrl_range_check")
label(0x85D0, "check_imm_range")
label(0x85D6, "copy_imm_params")
label(0x85E0, "tx_line_idle_check")
label(0x85FA, "test_inactive_retry")
label(0x85FC, "intoff_test_inactive")
label(0x8602, "test_line_idle")
label(0x8616, "inactive_retry")
label(0x862C, "tx_bad_ctrl_error")
label(0x863C, "tx_no_clock_error")
label(0x863E, "store_tx_error")
label(0x8697, "add_bytes_loop")
# UNMAPPED: label(0x8681, "tx_ctrl_dispatch_lo")
# UNMAPPED: label(0x8689, "tx_ctrl_machine_type")
label(0x86A9, "setup_data_xfer")
label(0x86BF, "copy_bcast_addr")
label(0x86CB, "setup_unicast_xfer")
label(0x86D0, "proc_op_status2")
label(0x86D2, "store_status_copy_ptr")
label(0x86D5, "skip_buf_setup")
label(0x86E0, "tx_ctrl_exit")
label(0x86ED, "tx_fifo_write")
label(0x870D, "tx_error")
label(0x8711, "tx_fifo_not_ready")
label(0x8718, "tx_store_error")
label(0x871B, "delay_nmi_disable")
label(0x873C, "check_handshake_bit")
label(0x8746, "install_reply_scout")
label(0x8773, "reject_reply")
label(0x87CE, "data_tx_begin")
label(0x87DC, "install_imm_data_nmi")
label(0x87F2, "data_tx_check_fifo")
label(0x880B, "write_second_tx_byte")
label(0x881F, "check_irq_loop")
label(0x882B, "data_tx_last")
label(0x883C, "install_saved_handler")
label(0x8845, "nmi_data_tx_tube")
label(0x8848, "tube_tx_fifo_write")
label(0x8860, "write_second_tube_byte")
label(0x886A, "tube_tx_inc_byte2")
label(0x886E, "tube_tx_inc_byte3")
# UNMAPPED: label(0x8861, "tube_tx_inc_operand")
label(0x8872, "tube_tx_inc_byte4")
label(0x8876, "check_tube_irq_loop")
# UNMAPPED: label(0x8869, "tube_tx_sr1_operand")
label(0x887E, "tx_tdra_error")
label(0x88A6, "nmi_final_ack_net")
label(0x88D7, "check_fv_final_ack")
label(0x88E2, "tx_result_fail")
label(0x8935, "calc_transfer_size")
label(0x8965, "restore_x_and_return")
label(0x8968, "fallback_calc_transfer")
label(0x898B, "nmi_shim_rom_src")
label(0x89A6, "wait_idle_and_reset")
label(0x89AB, "poll_nmi_idle")
label(0x89C7, "reset_enter_listen")
# UNMAPPED: label(0x89A6, "listen_jmp_hi")

# Entry points from NFS 3.65 correspondence
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0032)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0036)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0607)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0625)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0627)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0668)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x06A7)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x06AD)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x06BC)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x06EF)
entry(0x804F)
entry(0x809B)
entry(0x80B8)
entry(0x80E8)
entry(0x81B8)
entry(0x81C2)
entry(0x81D6)
entry(0x81EC)
entry(0x8223)
entry(0x8291)
entry(0x8316)
entry(0x8360)
entry(0x8386)
entry(0x84F9)
entry(0x85F1)
entry(0x86E7)
entry(0x870D)
entry(0x8723)
entry(0x872F)
entry(0x874B)
entry(0x875F)
entry(0x8776)
entry(0x87BE)
entry(0x87E3)
entry(0x8845)
entry(0x8886)
entry(0x8892)
entry(0x88A6)
entry(0x88BA)
entry(0x88DE)
entry(0x88E4)
entry(0x8968)
entry(0x89CA)
entry(0x89D8)

# ============================================================
# Subroutines (from NFS 3.65 correspondence)
# ============================================================

# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0406, "tube_addr_data_dispatch",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube address/data dispatch",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Called by 10 sites across the Tube host and Econet\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "code. Routes requests based on the value of A:\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  A < &80: R4 transfer setup at &0435 -- A is the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    transfer type (0-7), used both as the first\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    R4 byte and as the index into tube_ctrl_values.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    Types: 0/1 = 1-byte R3 P-to-H/H-to-P,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    2/3 = 2-byte R3 P-to-H/H-to-P,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    4 = execute at address, 5 = release claim,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    6 = event handler, 7 = SENDW transfer+release.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  &80 <= A < &C0: release -- maps A via ORA #&40\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    and compares with tube_claimed_id; if we own\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "    this address, falls through to tube_release_claim\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  A >= &C0: external address claim from another host\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Falls through to tube_release_claim when releasing our\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "current claim.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_entry={"a": "request type (<&80 data, &80-&BF release, &C0+ claim)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):               "x": "transfer address low (data transfer only)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):               "y": "transfer address high (data transfer only)"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0414, "tube_release_claim",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Release Tube address claim via R4 command 5",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Saves interrupt state (PHP/SEI) to protect the R4\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "protocol sequence, sends R4 command 5 (release) followed\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "by the currently-claimed address from tube_claimed_id\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(&15), then restores interrupts (PLP). Falls through to\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "clear_tube_claim to reset the claimed-address state to\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "the &80 sentinel.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0421, "clear_tube_claim",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Reset Tube address claim state",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Stores &80 into both tube_claimed_id (&15) and\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_claim_flag (&14). The &80 sentinel indicates no\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "address is currently claimed and no claim is in\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "progress. Called after tube_release_claim (via\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "fall-through) and during initial workspace setup.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0435, "tube_transfer_setup",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Set up R4 transfer protocol (7-byte sequence)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Initiates a Tube R4 transfer by sending a 7-byte\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "protocol sequence to R4, each write BVC-polled for\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "H-to-P space. PHP/SEI at entry and PLP at return\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "protect the sequence from IRQs.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "R4 byte sequence:\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  1. Transfer type byte (A on entry, 0-7)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  2. tube_claimed_id (Econet host ownership byte,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "     an Econet-specific addition to the standard\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "     Acorn Tube R4 protocol)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  3-6. 4-byte transfer address, big-endian\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "     (from (tube_data_ptr),Y=3..0)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  7. Trigger byte (post-LSR remnant of\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "     tube_ctrl_values[type]); parasite resumes\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "     after reading this\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Between writes 6 and 7, if bit 2 of the ULA ctrl\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "byte is set (types 0 and 2, both parasite-to-host),\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "performs two dummy BIT reads of R3 to drain the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "2-byte R3 FIFO.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "After the final write, polls R4 for the parasite\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "ack (BVC/BCS at poll_r4_copro_ack). Dispatches on\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "X (= transfer type):\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  X=4: tube_sendw_complete (release, sync via R2,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "       reset stack)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "  Other: if bit 0 of ctrl byte is set, write &88\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "         to &FEE0 to release Tube NMI; PLP; RTS")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0484, "tube_begin",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube host startup entry (BEGIN)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Entry point via JMP from &0400. Enables interrupts, checks\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "break type via OSBYTE &FD: soft break re-initialises Tube and\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "restarts, hard break claims address &FF. Sends ROM contents\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "to co-processor page by page via SENDW, then claims the final\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "transfer address.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x04C7, "tube_claim_default",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Claim default Tube transfer address",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Sets Y=0, X=&53 (address &0053), then JMP tube_addr_claim\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "to initiate a Tube address claim for the default transfer\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "address. Called from the BEGIN startup path and after the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "page transfer loop completes.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x04CE, "tube_init_reloc",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Initialise relocation address for ROM transfer",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Sets the Tube transfer source page to &8000\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(tube_xfer_page = &80) and the page counter to &80.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Checks ROM type bit 5 for a relocation address in the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "ROM header. If set, scans past the null-terminated\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "copyright string and extracts the 4-byte relocation\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "address into tube_transfer_addr (&53), tube_xfer_page\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(&54), tube_xfer_addr_2 (&55), and tube_xfer_addr_3\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(&56). If clear, uses the default &8000 start address.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Called twice during tube_begin: once for initial setup\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "and once after each page transfer completes.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0582, "tube_read_string",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Read string from Tube R2 into buffer",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Loops reading bytes from tube_read_r2 into the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "string buffer at &0700, storing at string_buf+Y.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Terminates on CR (&0D) or when Y wraps to zero\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(256-byte overflow). Returns with X=0, Y=7 so that\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "XY = &0700, ready for OSCLI or OSFIND dispatch.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Called by the Tube OSCLI and OSFIND handlers.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_exit={"x": "0 (low byte of &0700)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):              "y": "7 (high byte of &0700)"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0695, "tube_send_r2",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Send byte to Tube data register R2",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Polls Tube status register 2 until bit 6 (TDRA)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "is set, then writes A to the data register. Uses a\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tight BIT/BVC polling loop. Called by 12 sites\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "across the Tube host code for all R2 data\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "transmission: command responses, file data, OSBYTE\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "results, and control block bytes.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_entry={"a": "byte to send"},
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_exit={"a": "preserved (value written)"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x069E, "tube_send_r4",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Send byte to Tube data register R4",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Polls Tube status register 4 until bit 6 is set,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "then writes A to the data register. Uses a tight\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "BIT/BVC polling loop. R4 is the command/control\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "channel used for address claims (ADRR), data transfer\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "setup (SENDW), and release commands. Called by 7\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "sites, primarily during tube_release_claim and\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_transfer_setup sequences.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_entry={"a": "byte to send"},
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_exit={"a": "preserved (value written)"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x06BC, "tube_send_r1",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Send byte to Tube data register R1",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Polls Tube status register 1 until bit 6 is set,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "then writes A to the data register. Uses a tight\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "BIT/BVC polling loop. R1 is used for asynchronous\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "event and escape notification to the co-processor.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Called by tube_event_handler to forward event type,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Y, and X parameters, and reached via BMI from\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_escape_check when the escape flag is set.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_entry={"a": "byte to send"},
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_exit={"a": "preserved (value written)"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x06C5, "tube_read_r2",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Read a byte from Tube data register R2",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Polls Tube status register 2 until bit 7 (RDA)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "is set, then loads and returns the byte from Tube\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "data register 2. Uses a BIT/BPL polling loop (testing\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "the N flag). R2 is the primary data channel from the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "co-processor. Called by 14 sites across the Tube host\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "code for command dispatch, OSFILE/OSGBPB control block\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "reads, string reads, and OSBYTE parameter reception.",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     on_exit={"a": "byte read from R2"})

# UNMAPPED: subroutine(0x805D, "set_jsr_protection",
# UNMAPPED:     title="Set JSR protection and dispatch via table",
# UNMAPPED:     description=
# UNMAPPED:     "Validates the TX operation type in Y against the\n"
# UNMAPPED:     "dispatch table range, saves the current JSR protection\n"
# UNMAPPED:     "mask, sets protection bits 2-4, then dispatches through\n"
# UNMAPPED:     "the PHA/RTS trampoline using the table at\n"
# UNMAPPED:     "set_rx_buf_len_hi. If Y >= &86, skips the protection\n"
# UNMAPPED:     "setup and dispatches directly.",
# UNMAPPED:     on_entry={"y": "TX operation type (dispatch index)"})

comment(0x8000, """\
ANFS ROM 4.08.53 disassembly (Acorn Advanced Network Filing System)
===================================================================""")

# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0520, "tube_osbput",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSBPUT handler (R2 cmd 8)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads file handle and data byte from R2, then\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "calls OSBPUT (&FFD4) to write the byte. Falls through\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "to tube_reply_ack to send &7F acknowledgement.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x052D, "tube_osbget",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSBGET handler (R2 cmd 7)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads file handle from R2, calls OSBGET (&FFD7)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "to read a byte, then falls through to tube_rdch_reply\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "which encodes the carry flag (error) into bit 7 and\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "sends the result byte via R2.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0537, "tube_osrdch",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSRDCH handler (R2 cmd 0)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Calls OSRDCH (&FFE0) to read a character from\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "the current input stream, then falls through to\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_rdch_reply which encodes the carry flag (error)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "into bit 7 and sends the result byte via R2.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0542, "tube_osfind",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSFIND handler (R2 cmd 9)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads open mode from R2. If zero, reads a file\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "handle and closes that file. Otherwise saves the mode,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "reads a filename string into &0700 via tube_read_string,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "then calls OSFIND (&FFCE) to open the file. Sends the\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "resulting file handle (or &00) via tube_reply_byte.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x055E, "tube_osargs",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSARGS handler (R2 cmd 6)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads file handle from R2 into Y, then reads\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "a 4-byte argument and reason code into zero page.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Calls OSARGS (&FFDA), sends the result A and 4-byte\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "return value via R2, then returns to the main loop.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0596, "tube_oscli",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSCLI handler (R2 cmd 1)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads a command string from R2 into &0700 via\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_read_string, then calls OSCLI (&FFF7) to execute\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "it. Falls through to tube_reply_ack to send &7F\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "acknowledgement.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x05A9, "tube_osfile",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSFILE handler (R2 cmd 10)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads a 16-byte control block into zero page,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "a filename string into &0700 via tube_read_string,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "and a reason code from R2. Calls OSFILE (&FFDD),\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "then sends the result A and updated 16-byte control\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "block back via R2. Returns to the main loop via mj.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x05D1, "tube_osgbpb",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSGBPB handler (R2 cmd 11)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads a 13-byte control block and reason code\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "from R2 into zero page. Calls OSGBPB (&FFD1), then\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "sends 12 result bytes and the carry+result byte\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(via tube_rdch_reply) back via R2.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x05F2, "tube_osbyte_2param",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSBYTE 2-param handler (R2 cmd 2)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads X and A from R2, calls OSBYTE (&FFF4)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "with Y=0, then sends the result X via\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "tube_reply_byte. Used for OSBYTE calls that take\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "only A and X parameters.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0607, "tube_osbyte_long",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSBYTE 3-param handler (R2 cmd 3)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads X, Y, and A from R2, calls OSBYTE\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "(&FFF4), then sends carry+Y and X as result bytes\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "via R2. Used for OSBYTE calls needing all three\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "parameters and returning both X and Y results.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0627, "tube_osword",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSWORD handler (R2 cmd 4)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Reads OSWORD number A and in-length from R2,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "then reads the parameter block into &0128. Calls\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "OSWORD (&FFF1), then sends the out-length result\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "bytes from the parameter block back via R2.\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "Returns to the main loop via tube_return_main.")
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): subroutine(0x0668, "tube_osword_rdln",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     title="Tube OSWORD 0 handler (R2 cmd 5)",
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     description="Handles OSWORD 0 (read line) specially. Reads\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "4 parameter bytes from R2 into &0128 (max length,\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "min char, max char, flags). Calls OSWORD 0 (&FFF1)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "to read a line, then sends &7F+CR or the input line\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "byte-by-byte via R2, followed by &80 (error/escape)\n"
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     "or &7F (success).")
subroutine(0x8050, "adlc_init",
    title="ADLC initialisation",
    description="Initialise ADLC hardware and Econet workspace.\n"
    "Reads station ID via &FE18 (INTOFF side effect),\n"
    "performs a full ADLC reset (adlc_full_reset), then\n"
    "checks for Tube co-processor via OSBYTE &EA and\n"
    "stores the result in l0d63. Issues NMI claim service\n"
    "request (OSBYTE &8F, X=&0C). Falls through to\n"
    "init_nmi_workspace to copy the NMI shim to RAM.")
subroutine(0x8070, "init_nmi_workspace",
    title="Initialise NMI workspace (skip service request)",
    description="Copies 32 bytes of NMI shim code from ROM\n"
    "(listen_jmp_hi) to &0D00, then patches the current\n"
    "ROM bank number into the self-modifying code at\n"
    "&0D07. The shim includes the INTOFF/INTON pair\n"
    "(BIT &FE18 at entry, BIT &FE20 before RTI) that\n"
    "toggles the IC97 NMI enable flip-flop to guarantee\n"
    "edge re-triggering on /NMI. Clears tx_src_net,\n"
    "need_release_tube, and tx_op_type to zero. Reads\n"
    "station ID into tx_src_stn (&0D22). Sets\n"
    "tx_complete_flag and econet_init_flag to &80.\n"
    "Finally re-enables NMIs via INTON (&FE20 read).")
subroutine(0x809B, "nmi_rx_scout",
    title="NMI RX scout handler (initial byte)",
    description="Default NMI handler for incoming scout frames. Checks if the frame\n"
    "is addressed to us or is a broadcast. Installed as the NMI target\n"
    "during idle RX listen mode.\n"
    "Tests SR2 bit0 (AP = Address Present) to detect incoming data.\n"
    "Reads the first byte (destination station) from the RX FIFO and\n"
    "compares against our station ID. Reading &FE18 also disables NMIs\n"
    "(INTOFF side effect).")
subroutine(0x80B8, "nmi_rx_scout_net",
    title="RX scout second byte handler",
    description="Reads the second byte of an incoming scout (destination network).\n"
    "Checks for network match: 0 = local network (accept), &FF = broadcast\n"
    "(accept and flag), anything else = reject.\n"
    "Installs the scout data reading loop handler at &8102.")
subroutine(0x80D8, "scout_error",
    title="Scout error/discard handler",
    description="Handles scout reception errors and end-of-frame\n"
    "conditions. Reads SR2 and tests AP|RDA (bits 0|7):\n"
    "if neither set, the frame ended cleanly and is\n"
    "simply discarded. If unexpected data is present,\n"
    "performs a full ADLC reset. Also serves as the\n"
    "common discard path for address/network mismatches\n"
    "from nmi_rx_scout and scout_complete -- reached by\n"
    "5 branch sites across the scout reception chain.")
subroutine(0x8112, "scout_complete",
    title="Scout completion handler",
    description="Processes a completed scout frame. Writes CR1=&00\n"
    "and CR2=&84 to disable PSE and suppress FV, then\n"
    "tests SR2 for FV (frame valid). If FV is set with\n"
    "RDA, reads the remaining scout data bytes in pairs\n"
    "into the buffer at &0D3D. Matches the port byte\n"
    "(&0D40) against open receive control blocks to find\n"
    "a listener. On match, calculates the transfer size\n"
    "via tx_calc_transfer, sets up the data RX handler\n"
    "chain, and sends a scout ACK. On no match or error,\n"
    "discards the frame via scout_error.")
subroutine(0x81C2, "nmi_data_rx",
    title="Data frame RX handler (four-way handshake)",
    description="Receives the data frame after the scout ACK has been sent.\n"
    "First checks AP (Address Present) for the start of the data frame.\n"
    "Reads and validates the first two address bytes (dest_stn, dest_net)\n"
    "against our station address, then installs continuation handlers\n"
    "to read the remaining data payload into the open port buffer.\n"
    "\n"
    "Handler chain: &81E7 (AP+addr check) -> &81FB (net=0 check) ->\n"
    "&8211 (skip ctrl+port) -> &8239 (bulk data read) -> &8278 (completion)")
subroutine(0x81F7, "install_data_rx_handler",
    title="Install data RX bulk or Tube handler",
    description="Selects between the normal bulk RX handler (&8239)\n"
    "and the Tube RX handler based on bit 1 of rx_src_net\n"
    "(tx_flags). If normal mode, loads the handler address\n"
    "&8239 and checks SR1 bit 7: if IRQ is already asserted\n"
    "(more data waiting), jumps directly to nmi_data_rx_bulk\n"
    "to avoid NMI re-entry overhead. Otherwise installs the\n"
    "handler via set_nmi_vector and returns via RTI.")
subroutine(0x8215, "nmi_error_dispatch",
    title="NMI error handler dispatch",
    description="Common error/abort entry used by 12 call sites. Checks\n"
    "tx_flags bit 7: if clear, does a full ADLC reset and returns\n"
    "to idle listen (RX error path); if set, jumps to tx_result_fail\n"
    "(TX not-listening path).")
subroutine(0x8223, "nmi_data_rx_bulk",
    title="Data frame bulk read loop",
    description="Reads data payload bytes from the RX FIFO and stores them into\n"
    "the open port buffer at (open_port_buf),Y. Reads bytes in pairs\n"
    "(like the scout data loop), checking SR2 between each pair.\n"
    "SR2 non-zero (FV or other) -> frame completion at &8278.\n"
    "SR2 = 0 -> RTI, wait for next NMI to continue.")
subroutine(0x8268, "data_rx_complete",
    title="Data frame completion",
    description="Reached when SR2 non-zero during data RX (FV detected).\n"
    "Same pattern as scout completion (&8137): disables PSE (CR2=&84,\n"
    "CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.\n"
    "If extra data available and buffer space remains, stores it.\n"
    "Proceeds to send the final ACK via &82E4.")
subroutine(0x82DF, "ack_tx",
    title="ACK transmission",
    description="Sends a scout ACK or final ACK frame as part of the four-way handshake.\n"
    "If bit7 of &0D4A is set, this is a final ACK -> completion (&88C6).\n"
    "Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK\n"
    "frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).\n"
    "The ACK frame has no data payload -- just address bytes.\n"
    "\n"
    "After writing the address bytes to the TX FIFO, installs the next\n"
    "NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)\n"
    "and sends TX_LAST_DATA (CR2=&3F) to close the frame.")
subroutine(0x8316, "nmi_ack_tx_src",
    title="ACK TX continuation",
    description="Continuation of ACK frame transmission. Reads our\n"
    "station ID from &FE18 (INTOFF side effect), tests\n"
    "TDRA via SR1, and writes station + network=0 to the\n"
    "TX FIFO, completing the 4-byte ACK address header.\n"
    "Then checks rx_src_net bit 7: if set, branches to\n"
    "start_data_tx to begin the data phase. Otherwise\n"
    "writes CR2=&3F (TX_LAST_DATA) and falls through to\n"
    "post_ack_scout for scout processing.")
subroutine(0x832D, "post_ack_scout",
    title="Post-ACK scout processing",
    description="Called after the scout ACK has been transmitted. Processes the\n"
    "received scout data stored in the buffer at &0D3D-&0D48.\n"
    "Checks the port byte (&0D40) against open receive blocks to\n"
    "find a matching listener. If a match is found, sets up the\n"
    "data RX handler chain for the four-way handshake data phase.\n"
    "If no match, discards the frame.")
subroutine(0x833F, "advance_rx_buffer_ptr",
    title="Advance RX buffer pointer after transfer",
    description="Adds the transfer count to the RXCB buffer pointer (4-byte\n"
    "addition). If a Tube transfer is active, re-claims the Tube\n"
    "address and sends the extra RX byte via R3, incrementing the\n"
    "Tube pointer by 1.\n"
    "\n"
    "Reads tx_flags bit 1 (data transfer in progress) and bit 5\n"
    "(Tube transfer). Reads the 4-byte transfer count from\n"
    "net_tx_ptr,Y (Y=8..&0B) and the RXCB pointer at\n"
    "(port_ws_offset),Y. Updates RXCB in place. Clobbers A and Y;\n"
    "preserves X across the Tube branch (saved/restored via stack).",
    on_entry={"port_ws_offset, rx_buf_offset": "RXCB workspace pointer",
              "net_tx_ptr+8..+11": "transfer count (4-byte LE)",
              "tx_flags (rx_src_net)": "bit1 transfer-active, bit5 Tube"},
    on_exit={"a": "&FF when transfer was active, else preserved entry value",
             "rxcb buffer pointer": "advanced by transfer count"})
subroutine(0x8386, "nmi_post_ack_dispatch",
    title="Post-ACK frame-complete NMI handler",
    description="Installed by ack_tx_configure via saved_nmi_lo/hi.\n"
    "Fires as an NMI after the ACK frame (CRC and\n"
    "closing flag) has been fully transmitted by the\n"
    "ADLC. Dispatches on scout_port: port != 0 goes\n"
    "to rx_complete_update_rxcb to finalise the data\n"
    "transfer and mark the RXCB complete; port = 0\n"
    "with ctrl &82 (POKE) also goes to\n"
    "rx_complete_update_rxcb; other port-0 ops go to\n"
    "imm_op_build_reply.")
subroutine(0x8395, "rx_complete_update_rxcb",
    title="Complete RX and update RXCB",
    description="Called from nmi_post_ack_dispatch after the\n"
    "final ACK has been transmitted. Finalises the\n"
    "received data transfer: calls advance_rx_buffer_ptr\n"
    "to update the 4-byte buffer pointer with the\n"
    "transfer count (and handle Tube re-claim if\n"
    "needed). Stores the source station, network, and\n"
    "port into the RXCB, then ORs &80 into the control\n"
    "byte (bit 7 = complete). This is the NMI-to-\n"
    "foreground synchronisation point: wait_net_tx_ack\n"
    "polls this bit to detect that the reply has\n"
    "arrived. Falls through to discard_reset_rx to\n"
    "reset the ADLC to idle RX listen mode.")
subroutine(0x83F2, "discard_reset_listen",
    title="Discard with Tube release",
    description="Checks whether a Tube transfer is active by\n"
    "ANDing bit 1 of l0d63 with rx_src_net (tx_flags).\n"
    "If a Tube claim is held, calls release_tube to\n"
    "free it before returning. Used as the clean-up\n"
    "path after RXCB completion and after ADLC reset\n"
    "to ensure no stale Tube claims persist.")
label(0x83F7, "imm_op_jump_table")
subroutine(0x8400, "copy_scout_to_buffer",
    title="Copy scout data to port buffer",
    description="Copies scout data bytes (offsets 4-11) from the\n"
    "RX scout buffer at &0D3D into the open port buffer.\n"
    "Checks bit 1 of rx_src_net (tx_flags) to select the\n"
    "write path: direct memory store via (open_port_buf),Y\n"
    "for normal transfers, or Tube data register 3 write\n"
    "for Tube transfers. Calls advance_buffer_ptr after\n"
    "each byte. Falls through to release_tube on\n"
    "completion. Handles page overflow (Y wrap) by\n"
    "branching to scout_page_overflow.")
subroutine(0x8448, "release_tube",
    title="Release Tube co-processor claim",
    description="Tests need_release_tube (&98) bit 7: if set, the\n"
    "Tube has already been released and the subroutine\n"
    "just clears the flag. If clear (Tube claim held),\n"
    "calls tube_addr_data_dispatch with A=&82 to release\n"
    "the claim, then clears the release flag via LSR\n"
    "(which shifts bit 7 to 0). Called after completed\n"
    "RX transfers and during discard paths to ensure no\n"
    "stale Tube claims persist.\n"
    "\n"
    "Idempotent: safe to call when the Tube has already been\n"
    "released. Clobbers A; preserves X and Y.",
    on_entry={"prot_flags": "bit 7 clear if Tube claim is currently held"},
    on_exit={"prot_flags": "bit 7 clear (LSR also shifts other bits down)",
             "a": "clobbered"})
subroutine(0x8454, "immediate_op",
    title="Immediate operation handler (port = 0)",
    description="Checks the control byte at l0d30 for immediate\n"
    "operation codes (&81-&88). Codes below &81 or above\n"
    "&88 are out of range and discarded. Codes &87-&88\n"
    "(HALT/CONTINUE) bypass the protection mask check.\n"
    "For &81-&86, converts to a 0-based index and tests\n"
    "against the immediate operation mask at &0D61 to\n"
    "determine if this station accepts the operation.\n"
    "If accepted, dispatches via the immediate operation\n"
    "table. Builds the reply by storing data length,\n"
    "station/network, and control byte into the RX buffer.")

# Immediate operation dispatch lo-byte table.
# In 4.21_v1 the table moved by +3 to &848B-&8492 (the &8488 area is now
# the JMP nmi_error_dispatch trampoline). 8 lo-byte entries indexed by
# the immediate-op control byte ($81-$88) via LDA imm_op_dispatch_lo-$81,Y.
# Each entry is the low byte of (handler-1) so that PHA/PHA/RTS dispatch
# lands on the handler.
label(0x848B, "imm_op_dispatch_lo")
for addr in range(0x848B, 0x8493):
    byte(addr)
expr(0x848B, "<(rx_imm_peek-1)")            # ctrl &81: PEEK
expr(0x848C, "<(rx_imm_poke-1)")            # ctrl &82: POKE
expr(0x848D, "<(rx_imm_exec-1)")            # ctrl &83: JSR
expr(0x848E, "<(rx_imm_exec-1)")            # ctrl &84: UserProc
expr(0x848F, "<(rx_imm_exec-1)")            # ctrl &85: OSProc
expr(0x8490, "<(rx_imm_halt_cont-1)")       # ctrl &86: HALT
expr(0x8491, "<(rx_imm_halt_cont-1)")       # ctrl &87: CONTINUE
expr(0x8492, "<(rx_imm_machine_type-1)")    # ctrl &88: machine-type

subroutine(0x8493, "rx_imm_exec",
    title="RX immediate: JSR/UserProc/OSProc setup",
    description="Sets up the port buffer to receive remote procedure\n"
    "data. Copies the 2-byte remote address from &0D32\n"
    "into the execution address workspace at &0D66, then\n"
    "jumps to the common receive path at c81c1. Used for\n"
    "operation types &83 (JSR), &84 (UserProc), and\n"
    "&85 (OSProc).")
subroutine(0x84B1, "rx_imm_poke",
    title="RX immediate: POKE setup",
    description="Sets up workspace offsets for receiving POKE data.\n"
    "port_ws_offset=&2E, rx_buf_offset=&0D, then jumps to\n"
    "the common data-receive path at c81af.")
subroutine(0x84BC, "rx_imm_machine_type",
    title="RX immediate: machine type query",
    description="Sets up a buffer at &88C1 (length #&01FC) for the\n"
    "machine type query response. Falls through to\n"
    "set_rx_buf_len_hi to configure buffer dimensions,\n"
    "then branches to set_tx_reply_flag.")
subroutine(0x84CE, "rx_imm_peek",
    title="RX immediate: PEEK setup",
    description="Writes &0D2E to port_ws_offset/rx_buf_offset, sets\n"
    "scout_status=2, then calls tx_calc_transfer to send\n"
    "the PEEK response data back to the requesting station.")
subroutine(0x852C, "advance_buffer_ptr",
    title="Increment 4-byte receive buffer pointer",
    description="Adds one to the counter at &A2-&A5 (port_buf_len\n"
    "low/high, open_port_buf low/high), cascading\n"
    "overflow through all four bytes. Called after each\n"
    "byte is stored during scout data copy and data\n"
    "frame reception to track the current write position\n"
    "in the receive buffer.\n"
    "\n"
    "Preserves A, X, Y (uses INC zp throughout).",
    on_exit={"port_buf_len, open_port_buf": "incremented as 4-byte LE counter"})
subroutine(0x84F9, "imm_op_build_reply",
    title="Build immediate operation reply header",
    description="Stores data length, source station/network, and control byte\n"
    "into the RX buffer header area for port-0 immediate operations.\n"
    "Then disables SR interrupts and configures the VIA shift\n"
    "register for shift-in mode before returning to\n"
    "idle listen.")
# Located in 4.21_v1 at &8540 (was &8543 in 4.18 -- moved -3 because
# of layout shifts in the surrounding TX-done handlers). Reached only
# via PHA/PHA/RTS dispatch from the tx_done_dispatch table; needs an
# explicit entry().
entry(0x8540)
subroutine(0x8540, "tx_done_jsr",
    title="TX done: remote JSR execution",
    description="Pushes (tx_done_exit - 1) on the stack so RTS returns "
    "to tx_done_exit when the remote routine completes, then does "
    "JMP (l0d66) to call the remote-supplied JSR target. When that "
    "routine returns via RTS, control resumes at tx_done_exit which "
    "tidies up TX state.",
    on_entry={"l0d66, l0d67": "remote routine address (low, high)"})
subroutine(0x8549, "tx_done_econet_event",
    title="TX done: fire Econet event",
    description="Handler for TX operation type &84. Loads the\n"
    "remote address from l0d66/l0d67 into X/A and\n"
    "sets Y=8 (Econet event number), then falls\n"
    "through to tx_done_fire_event to call OSEVEN.\n"
    "\n"
    "Reached only via PHA/PHA/RTS dispatch from\n"
    "tx_done_dispatch_lo/hi. The dispatcher pushed the\n"
    "caller's X and Y onto the stack before transferring\n"
    "control, and the shared tx_done_exit at &8582 restores\n"
    "them via PLA/TAY/PLA/TAX before returning A=0.",
    on_entry={"exec_addr_lo, exec_addr_hi (l0d66/l0d67)":
              "remote routine address (low, high)",
              "stack": "caller's Y on top, then caller's X (pushed by dispatcher)"},
    on_exit={"a": "0 (success status)",
             "x, y": "restored from stack via tx_done_exit"})
subroutine(0x8557, "tx_done_os_proc",
    title="TX done: OSProc call",
    description="Calls the ROM service entry point with X=l0d66,\n"
    "Y=l0d67. This invokes an OS-level procedure on\n"
    "behalf of the remote station, then exits via\n"
    "tx_done_exit.\n"
    "\n"
    "Reached only via PHA/PHA/RTS dispatch from\n"
    "tx_done_dispatch_lo/hi.",
    on_entry={"exec_addr_lo, exec_addr_hi (l0d66/l0d67)":
              "OSProc address (X low, Y high)",
              "stack": "caller's Y, then caller's X (pushed by dispatcher)"},
    on_exit={"a": "0 (success status)",
             "x, y": "restored from stack via tx_done_exit"})
subroutine(0x8563, "tx_done_halt",
    title="TX done: HALT",
    description="Sets bit 2 of rx_flags (&0D61), enables interrupts,\n"
    "and spin-waits until bit 2 is cleared (by a CONTINUE\n"
    "from the remote station). If bit 2 is already set,\n"
    "skips to exit.\n"
    "\n"
    "Reached only via PHA/PHA/RTS dispatch from\n"
    "tx_done_dispatch_lo/hi. Falls through to tx_done_continue\n"
    "after the spin completes; on the already-halted path it\n"
    "branches directly to tx_done_exit.",
    on_entry={"econet_flags (&0D61)": "bit 2 = halt-active flag",
              "stack": "caller's Y, then caller's X (pushed by dispatcher)"},
    on_exit={"a": "0 (success status, set by tx_done_exit)",
             "econet_flags": "bit 2 may be set during spin, cleared on exit",
             "i flag": "interrupts enabled (CLI inside the spin)",
             "x, y": "restored from stack via tx_done_exit"})
subroutine(0x857A, "tx_done_continue",
    title="TX done: CONTINUE",
    description="Clears bit 2 of rx_flags (&0D61), releasing any\n"
    "station that is halted and spinning in tx_done_halt.\n"
    "\n"
    "Reached either as a fall-through from tx_done_halt or\n"
    "directly via PHA/PHA/RTS dispatch from\n"
    "tx_done_dispatch_lo/hi. Falls through to tx_done_exit\n"
    "which restores X and Y from the stack and returns A=0.",
    on_entry={"econet_flags (&0D61)": "bit 2 may be set (from a previous HALT)",
              "stack": "caller's Y, then caller's X (pushed by dispatcher)"},
    on_exit={"a": "0 (success status)",
             "econet_flags": "bit 2 cleared",
             "x, y": "restored from stack via tx_done_exit"})
subroutine(0x8589, "tx_begin",
    title="Begin TX operation",
    description="Main TX initiation entry point (called via trampoline at &06CE).\n"
    "Copies dest station/network from the TXCB to the scout buffer,\n"
    "dispatches to immediate op setup (ctrl >= &81) or normal data\n"
    "transfer, calculates transfer sizes, copies extra parameters,\n"
    "then enters the INACTIVE polling loop.")
subroutine(0x85F1, "inactive_poll",
    title="INACTIVE polling loop",
    description="Entry point for the Econet line idle detection\n"
    "loop. Saves the TX index in rx_remote_addr, pushes\n"
    "two timeout counter bytes onto the stack, and loads\n"
    "Y=&E7 (CR2 value for TX preparation). Loads the\n"
    "INACTIVE bit mask (&04) into A and falls through to\n"
    "intoff_test_inactive to begin polling SR2 with\n"
    "interrupts disabled.")
subroutine(0x85FC, "intoff_test_inactive",
    title="Disable NMIs and test INACTIVE",
    description="Disables NMIs via two reads of &FE18 (INTOFF),\n"
    "then polls SR2 for the INACTIVE bit (bit 2). If\n"
    "INACTIVE is detected, reads SR1 and writes CR2=&67\n"
    "to clear status, then tests CTS (SR1 bit 4): if\n"
    "CTS is present, branches to tx_prepare to begin\n"
    "transmission. If INACTIVE is not set, re-enables\n"
    "NMIs via &FE20 (INTON) and decrements the 3-byte\n"
    "timeout counter on the stack. On timeout, falls\n"
    "through to tx_line_jammed.")
subroutine(0x8630, "tx_line_jammed",
    title="TX timeout error handler (Line Jammed)",
    description="Reached when the INACTIVE polling loop times\n"
    "out without detecting a quiet line. Writes\n"
    "CR2=&07 (FC_TDRA|2_1_BYTE|PSE) to abort the TX\n"
    "attempt, pulls the 3-byte timeout state from the\n"
    "stack, and stores error code &40 ('Line Jammed')\n"
    "in the TX control block via store_tx_error.")
subroutine(0x864A, "tx_prepare",
    title="TX preparation",
    description="Configures the ADLC for frame transmission.\n"
    "Writes CR2=Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|\n"
    "2_1_BYTE|PSE) and CR1=&44 (RX_RESET|TIE) to enable\n"
    "TX with interrupts. Installs the nmi_tx_data handler\n"
    "at &86E0. Sets need_release_tube flag via SEC/ROR.\n"
    "Writes the 4-byte destination address (dst_stn,\n"
    "dst_net, src_stn, src_net=0) to the TX FIFO. For\n"
    "Tube transfers, claims the Tube address; for direct\n"
    "transfers, sets up the buffer pointer from the TXCB.")
# UNMAPPED: subroutine(0x8689, "tx_ctrl_machine_type",
# UNMAPPED:     title="TX ctrl: machine type query setup",
# UNMAPPED:     description="Handler for control byte &88. Sets scout_status=3\n"
# UNMAPPED:     "and branches to store_status_copy_ptr, skipping\n"
# UNMAPPED:     "the 4-byte address addition (no address parameters\n"
# UNMAPPED:     "needed for a machine type query).")
subroutine(0x868A, "tx_ctrl_peek",
    title="TX ctrl: PEEK transfer setup",
    description="Sets A=3 (scout_status for PEEK) and branches\n"
    "to tx_ctrl_store_and_add to store the status and\n"
    "perform the 4-byte transfer address addition.")
subroutine(0x868E, "tx_ctrl_poke",
    title="TX ctrl: POKE transfer setup",
    description="Sets A=2 (scout_status for POKE) and falls\n"
    "through to tx_ctrl_store_and_add to store the\n"
    "status and perform the 4-byte transfer address\n"
    "addition.")
subroutine(0x8690, "tx_ctrl_store_and_add",
    title="TX ctrl: store status and add transfer address",
    description="Shared path for PEEK (A=3) and POKE (A=2).\n"
    "Stores A as the scout status byte at rx_port\n"
    "(&0D40), then performs a 4-byte addition with\n"
    "carry propagation, adding bytes from the TXCB\n"
    "(nmi_tx_block+&0C to +&0F) into the transfer\n"
    "address workspace at &0D1E-&0D21. Falls through\n"
    "to tx_ctrl_proc which checks the loop boundary,\n"
    "then continues to tx_calc_transfer and\n"
    "tx_ctrl_exit.",
    on_entry={"a": "scout status (3=PEEK, 2=POKE)"})
subroutine(0x86A2, "tx_ctrl_proc",
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="Sets scout_status=2 and calls tx_calc_transfer\n"
    "directly (no 4-byte address addition needed for\n"
    "procedure calls). Shared by operation types &83-&85.")
subroutine(0x86E7, "nmi_tx_data",
    title="NMI TX data handler",
    description="Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the\n"
    "BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).\n"
    "After writing 2 bytes, checks if the frame is complete. If more data,\n"
    "tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes\n"
    "without returning from NMI (tight loop). Otherwise returns via RTI.")
subroutine(0x8723, "tx_last_data",
    title="TX_LAST_DATA and frame completion",
    description="Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs\n"
    "the TX completion NMI handler at &8728 (nmi_tx_complete).\n"
    "CR2=&3F = 0011_1111:\n"
    "  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)\n"
    "  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte\n"
    "  bit3: FLAG_IDLE -- send flags/idle after frame\n"
    "  bit2: FC_TDRA -- force clear TDRA\n"
    "  bit1: 2_1_BYTE -- two-byte transfer mode\n"
    "  bit0: PSE -- prioritised status enable\n"
    "Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)\n"
    "Exits via JMP set_nmi_vector which installs nmi_tx_complete,\n"
    "then falls through to nmi_rti. The INTON (BIT &FE20) in\n"
    "nmi_rti creates the /NMI edge for the frame-complete interrupt\n"
    "-- essential because the ADLC IRQ may transition atomically\n"
    "from TDRA to frame-complete without de-asserting.")
subroutine(0x872F, "nmi_tx_complete",
    title="TX completion: switch to RX mode",
    description="Called via NMI after the frame (including CRC\n"
    "and closing flag) has been fully transmitted.\n"
    "Writes CR1=&82 (TX_RESET|RIE) to clear RX_RESET\n"
    "and enable RX interrupts -- the TX-to-RX pivot in\n"
    "the four-way handshake. The scout ACK can only be\n"
    "received after this point. Full CR1 sequence through\n"
    "a handshake: &44 (scout TX) -> &82 (await scout ACK)\n"
    "-> &44 (data TX) -> &82 (await data ACK).\n"
    "Dispatches on rx_src_net flags: bit6=broadcast\n"
    "(tx_result_ok), bit0=handshake data pending\n"
    "(handshake_await_ack), both clear=install\n"
    "nmi_reply_scout for scout ACK reception.")
subroutine(0x874B, "nmi_reply_scout",
    title="RX reply scout handler",
    description="Handles reception of the reply scout frame after transmission.\n"
    "Checks SR2 bit0 (AP) for incoming data, reads the first byte\n"
    "(destination station) and compares to our station ID via &FE18\n"
    "(which also disables NMIs as a side effect).")
subroutine(0x875F, "nmi_reply_cont",
    title="RX reply continuation handler",
    description="Reads the second byte of the reply scout (destination network) and\n"
    "validates it is zero (local network). Installs nmi_reply_validate\n"
    "(&8779) for the remaining two bytes (source station and network).\n"
    "Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &8767.\n"
    "If IRQ is still set, falls through directly to &8779 without an RTI,\n"
    "avoiding NMI re-entry overhead for short frames where all bytes arrive\n"
    "in quick succession.")
subroutine(0x8776, "nmi_reply_validate",
    title="RX reply validation (Path 2 for FV/PSE interaction)",
    description="Reads the source station and source network from the reply scout and\n"
    "validates them against the original TX destination (&0D20/&0D21).\n"
    "Sequence:\n"
    "  1. Check SR2 bit7 (RDA) at &8779 -- must see data available\n"
    "  2. Read source station at &877E, compare to &0D20 (tx_dst_stn)\n"
    "  3. Read source network at &877C, compare to &0D21 (tx_dst_net)\n"
    "  4. Check SR2 bit1 (FV) at &8786 -- must see frame complete\n"
    "If all checks pass, the reply scout is valid and the ROM proceeds\n"
    "to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).")
subroutine(0x87BE, "nmi_scout_ack_src",
    title="TX scout ACK: write source address",
    description="Continuation of the TX-side scout ACK. Reads our\n"
    "station ID from &FE18 (INTOFF), tests TDRA via SR1,\n"
    "and writes station + network=0 to the TX FIFO. Then\n"
    "checks bit 1 of rx_src_net to select between the\n"
    "immediate-op data NMI handler and the normal\n"
    "nmi_data_tx handler at &87EE. Installs the chosen\n"
    "handler via set_nmi_vector. Shares the tx_check_tdra\n"
    "entry at &87C7 with ack_tx.")
subroutine(0x87E3, "nmi_data_tx",
    title="TX data phase: send payload",
    description="Transmits the data payload of a four-way\n"
    "handshake. Loads bytes from (open_port_buf),Y or\n"
    "from Tube R3 depending on the transfer mode, writing\n"
    "pairs to the TX FIFO. After each pair, decrements\n"
    "the byte count (port_buf_len). If the count reaches\n"
    "zero, branches to tx_last_data to signal end of\n"
    "frame. Otherwise tests SR1 bit 7 (IRQ): if still\n"
    "asserted, writes another pair without returning from\n"
    "NMI (tight loop optimisation). If IRQ clears, returns\n"
    "via RTI.")
subroutine(0x8886, "handshake_await_ack",
    title="Four-way handshake: switch to RX for final ACK",
    description="Called via JMP from nmi_tx_complete when bit 0 of\n"
    "&0D4A is set (four-way handshake in progress). Writes\n"
    "CR1=&82 (TX_RESET|RIE) to switch the ADLC from TX\n"
    "mode to RX mode, listening for the final ACK from the\n"
    "remote station. Installs the nmi_final_ack handler at\n"
    "&887A via set_nmi_vector.")
subroutine(0x8892, "nmi_final_ack",
    title="RX final ACK handler",
    description="Receives the final ACK in a four-way handshake. Same validation\n"
    "pattern as the reply scout handler (&874E-&8779):\n"
    "  &887A: Check AP, read dest_stn, compare to our station\n"
    "  &888E: Check RDA, read dest_net, validate = 0\n"
    "  &88A2: Check RDA, read src_stn/net, compare to TX dest\n"
    "  &88C1: Check FV for frame completion\n"
    "On success, stores result=0 at tx_result_ok. On failure, error &41.")
subroutine(0x88BA, "nmi_final_ack_validate",
    title="Final ACK validation",
    description="Continuation of nmi_final_ack. Tests SR2 for RDA,\n"
    "then reads the source station and source network\n"
    "bytes from the RX FIFO, comparing each against the\n"
    "original TX destination at tx_dst_stn (&0D20) and\n"
    "tx_dst_net (&0D21). Finally tests SR2 bit 1 (FV)\n"
    "for frame completion. Any mismatch or missing FV\n"
    "branches to tx_result_fail. On success, falls\n"
    "through to tx_result_ok.")
subroutine(0x88DE, "tx_result_ok",
    title="TX completion handler",
    description="Loads A=0 (success) and branches unconditionally to\n"
    "tx_store_result (BEQ is always taken since A=0). This\n"
    "two-instruction entry point exists so that JMP sites\n"
    "can target the success path without needing to set A.\n"
    "Called from ack_tx (&82EC) for final-ACK completion\n"
    "and from nmi_tx_complete (&8732) for immediate-op\n"
    "completion where no ACK is expected.")
subroutine(0x88E2, "tx_result_fail",
    title="TX failure: not listening",
    description="Loads error code &41 (not listening) and falls through to\n"
    "tx_store_result. The most common TX error path — reached from\n"
    "11 sites across the final-ACK validation chain when the remote\n"
    "station doesn't respond or the frame is malformed.")
subroutine(0x88E4, "tx_store_result",
    title="TX result store and completion",
    description="Stores the TX result code (in A) at offset 0 of\n"
    "the TX control block via (nmi_tx_block),Y=0. Sets\n"
    "ws_0d60 to &80 to signal TX completion to the\n"
    "foreground polling loop. Then jumps to\n"
    "discard_reset_rx for a full ADLC reset and return\n"
    "to idle RX listen mode.",
    on_entry={"a": "result code (0=success, &40=jammed, &41=not listening)"})
# Located in 4.21_v1 at &8900 (was at &88F2 in 4.18). Reached via 3
# JSR sites; not preceded by a clean RTS/JMP boundary which is why
# the carry-over fingerprint missed it.
subroutine(0x8900, "tx_calc_transfer",
    title="Calculate transfer size and reclaim Tube buffer",
    description="Inspects RXCB[6..7] (buffer end address byte 2 and "
    "high) to detect a Tube buffer (high=&FF, byte 2 in [&FE,&FF]). "
    "For Tube buffers, computes the 4-byte transfer size by "
    "subtracting RXCB[8..&B] (start) from RXCB[4..7] (end), stores "
    "the result via (port_ws_offset),Y, and re-claims the Tube via "
    "JSR &0406 with claim type &C2. For non-Tube buffers, falls "
    "through to fallback_calc_transfer which does a 1-byte size "
    "subtraction without the Tube reclaim.\n"
    "\n"
    "Three callers: scout_complete (&819A), rx_imm_peek (&84DB), "
    "tx_ctrl_proc (&86DD).",
    on_entry={"y": "0 -- caller convention"},
    on_exit={"a": "transfer status",
             "c": "set if Tube address claimed, clear otherwise"})
subroutine(0x898C, "adlc_full_reset",
    title="ADLC full reset",
    description="Performs a full ADLC hardware reset. Writes\n"
    "CR1=&C1 (TX_RESET|RX_RESET|AC) to put both TX and\n"
    "RX sections in reset with address control enabled.\n"
    "Then configures CR4=&1E (8-bit RX word, abort extend,\n"
    "NRZ encoding) and CR3=&00 (no loopback, no AEX, NRZ,\n"
    "no DTR). Falls through to adlc_rx_listen to re-enter\n"
    "RX listen mode.")
subroutine(0x899B, "adlc_rx_listen",
    title="Enter RX listen mode",
    description="Configures the ADLC for passive RX listen mode.\n"
    "Writes CR1=&82 (TX_RESET|RIE): TX section held in\n"
    "reset, RX interrupts enabled. Writes CR2=&67\n"
    "(CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE) to clear\n"
    "all pending status and enable prioritised status.\n"
    "This is the idle state where the ADLC listens for\n"
    "incoming scout frames via NMI.")
subroutine(0x89A6, "wait_idle_and_reset",
    title="Wait for idle NMI state and reset Econet",
    description="Service 12 handler: NMI release. Checks ws_0d62\n"
    "to see if Econet has been initialised; if not, skips\n"
    "straight to adlc_rx_listen. Otherwise spins in a\n"
    "tight loop comparing the NMI handler vector at\n"
    "&0D0C/&0D0D against the address of nmi_rx_scout\n"
    "(&80BE). When the NMI handler returns to idle, falls\n"
    "through to save_econet_state to clear the initialised\n"
    "flags and re-enter RX listen mode.")
subroutine(0x89B9, "save_econet_state",
    title="Reset Econet flags and enter RX listen",
    description="Disables NMIs via two reads of &FE18 (INTOFF),\n"
    "then clears ws_0d60 (TX complete) and ws_0d62\n"
    "(Econet initialised) by storing the current A value.\n"
    "Sets Y=5 (service call workspace page) and jumps to\n"
    "adlc_rx_listen to configure the ADLC for passive\n"
    "listening. Used during NMI release (service 12) to\n"
    "safely tear down the Econet state before another\n"
    "ROM can claim the NMI workspace.")
subroutine(0x89CA, "nmi_bootstrap_entry",
    title="Bootstrap NMI entry point (in ROM)",
    description="An alternate NMI handler that lives in the ROM itself rather than\n"
    "in the RAM workspace at &0D00. Unlike the RAM shim (which uses a\n"
    "self-modifying JMP to dispatch to different handlers), this one\n"
    "hardcodes JMP nmi_rx_scout (&80BE). Used as the initial NMI handler\n"
    "before the workspace has been properly set up during initialisation.\n"
    "Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,\n"
    "LDA romsel, STA &FE30, JMP &80BE.\n"
    "\n"
    "The BIT &FE18 (INTOFF) at entry and BIT &FE20 (INTON) before RTI\n"
    "in nmi_rti are essential for edge-triggered NMI re-delivery.\n"
    "The 6502 /NMI is falling-edge triggered; the Econet NMI enable\n"
    "flip-flop (IC97) gates the ADLC IRQ onto /NMI. INTOFF clears\n"
    "the flip-flop, forcing /NMI high; INTON sets it, allowing the\n"
    "ADLC IRQ through. This creates a guaranteed high-to-low edge on\n"
    "/NMI even when the ADLC IRQ is continuously asserted (e.g. when\n"
    "it transitions atomically from TDRA to frame-complete without\n"
    "de-asserting). Without this mechanism, nmi_tx_complete would\n"
    "never fire after tx_last_data.")
subroutine(0x89D8, "rom_set_nmi_vector",
    title="ROM copy of set_nmi_vector + nmi_rti",
    description="ROM-resident version of the NMI exit sequence, also\n"
    "the source for the initial copy to RAM at &0D0E.\n"
    "set_nmi_vector (&0D0E): writes both hi and lo bytes\n"
    "of the JMP target at &0D0C/&0D0D. nmi_rti (&0D14):\n"
    "restores the original ROM bank, pulls Y and A from\n"
    "the stack, then BIT &FE20 (INTON) to re-enable the\n"
    "NMI flip-flop before RTI. The INTON creates a\n"
    "guaranteed falling edge on /NMI if the ADLC IRQ is\n"
    "already asserted, ensuring the next handler fires\n"
    "immediately.")
# UNMAPPED: label(0x8A6F, "start_rom_scan")
subroutine(0x8B00, "scan_remote_keys",
    title="Scan keyboard for remote operation keys",
    description="Uses OSBYTE &7A with Y=&7F to check whether\n"
    "remote operation keys (&CE-&CF) are currently\n"
    "pressed. If neither key is detected, clears\n"
    "svc_state and nfs_workspace to zero via the\n"
    "clear_svc_and_ws entry point, which is also used\n"
    "directly by cmd_roff. Called by check_escape.\n"
    "\n"
    "X is saved into nfs_workspace across the OSBYTE call\n"
    "and restored each iteration -- the loop reuses A as the\n"
    "key-code counter without needing X. clear_svc_and_ws\n"
    "is also entered directly (label) by cmd_roff with no\n"
    "register pre-conditions.",
    on_exit={"a": "0 (when no key pressed -- the cleared path)",
             "x": "may be modified by OSBYTE",
             "y": "&7F (left over from OSBYTE call setup)",
             "svc_state, nfs_workspace": "both zeroed when no remote key was pressed"})
subroutine(0x8B18, "save_text_ptr",
    title="Save OS text pointer for later retrieval",
    description="Copies &F2/&F3 into fs_crc_lo/fs_crc_hi. Called by\n"
    "svc_4_star_command and svc_9_help before attempting\n"
    "command matches, and by match_fs_cmd during\n"
    "iterative help topic matching. Preserves A via\n"
    "PHA/PLA.",
    on_entry={"os_text_ptr (&F2/&F3)": "the OS text pointer to snapshot"},
    on_exit={"a": "preserved",
             "fs_crc_lo, fs_crc_hi (&BE/&BF)":
             "snapshot of os_text_ptr at call time"})
subroutine(0x8BC6, "print_cmd_table",
    title="Print *HELP command listing with optional header",
    description="If V flag is set, saves X/Y, calls\n"
    "print_version_header to show the ROM version\n"
    "string and station number, then restores X/Y.\n"
    "If V flag is clear, outputs a newline only.\n"
    "Either path then falls through to\n"
    "print_cmd_table_loop to enumerate commands.",
    on_entry={"x": "offset into cmd_table_fs",
              "v": "set=print version header, clear=newline only"})
subroutine(0x8BD5, "print_cmd_table_loop",
    title="Enumerate and print command table entries",
    description="Walks the ANFS command table from offset X,\n"
    "printing each command name padded to 9 characters\n"
    "followed by its syntax description. Entries with\n"
    "bit 7 set mark end-of-table. The syntax descriptor\n"
    "byte's low 5 bits index into cmd_syntax_table;\n"
    "index &0E triggers special handling that lists\n"
    "shared command names in parentheses. Calls\n"
    "help_wrap_if_serial to handle line continuation\n"
    "on serial output streams. Preserves Y.",
    on_entry={"x": "offset into cmd_table_fs"})
subroutine(0x8C29, "help_wrap_if_serial",
    title="Wrap *HELP syntax lines for serial output",
    description="Checks the output destination via &0355. Returns\n"
    "immediately for VDU (stream 0) or printer\n"
    "(stream 3) output. For serial streams, outputs a\n"
    "newline followed by 12 spaces of indentation to\n"
    "align continuation lines with the syntax\n"
    "description column.",
    on_entry={"&0355 (current output stream)":
              "0 = VDU, 3 = printer (no-op for both); other = serial"},
    on_exit={"y": "preserved (saved/restored via PHY/PLY)",
             "a": "clobbered (last char written via OSWRCH)"})
subroutine(0x8C93, "print_version_header",
    title="Print ANFS version string and station number",
    description="Uses an inline string after JSR print_inline:\n"
    "CR + \"Advanced  4.08.53\" + CR. After the inline\n"
    "string, JMPs to print_station_id to append the\n"
    "local Econet station number.")
# Located in 4.21_v1 at &8CAD (was &8CB9 in 4.18) by following the
# JSR site at &8B23 (which maps from 4.18 &8B1A). Already classified
# as code (sub_c8cad with 3 callers from &8B23, &8CBD, &B3A0). The
# 4.21 body extends the 4.18 simple lookup with a ROL/PHP/ROR/PLP
# trick to also extract bit 7 (ADLC-absent flag) from the same byte.
subroutine(0x8CAD, "get_ws_page",
    title="Read workspace page number for current ROM slot",
    description="Indexes into the MOS per-ROM workspace table at\n"
    "&0DF0 using romsel_copy (&F4) as the ROM slot.\n"
    "Returns the allocated page number in both A and Y\n"
    "for caller convenience. The 4.21 version also\n"
    "OR's bit 7 of the slot flag back into A on exit\n"
    "(ADLC-absent flag) — see &8CB7-&8CB9.",
    on_entry={"romsel_copy (&F4)": "current ROM slot (used as table index)"},
    on_exit={"a": "workspace page number (with bit 7 = ADLC-absent flag)",
             "y": "workspace page number (low 7 bits)"})
subroutine(0x8CBD, "setup_ws_ptr",
    title="Set up zero-page pointer to workspace page",
    description="Calls get_ws_page to read the page number, stores\n"
    "it as the high byte in nfs_temp (&CD), and clears\n"
    "the low byte at &CC to zero. This gives a\n"
    "page-aligned pointer used by FS initialisation and\n"
    "cmd_net_fs to access the private workspace.",
    on_entry={"romsel_copy (&F4)":
              "current ROM slot (consumed by get_ws_page)"},
    on_exit={"a": "0",
             "y": "workspace page number",
             "nfs_temp lo/hi (&CC/&CD)":
             "&00, ws_page -> page-aligned pointer to private workspace"})
subroutine(0x8CFD, "notify_new_fs",
    title="Notify OS of filing system selection",
    description="Calls FSCV with A=6 to announce the FS change,\n"
    "then issues paged ROM service call 10 via OSBYTE\n"
    "&8F to inform other ROMs. Sets X=&0A and branches\n"
    "to issue_svc_osbyte which falls through from the\n"
    "call_fscv subroutine.",
    on_exit={"a": "clobbered (FSCV reason 6 then OSBYTE &8F)",
             "x": "&0A (the service number passed to OSBYTE &8F)"})
subroutine(0x8CFF, "call_fscv",
    title="Dispatch to filing system control vector (FSCV)",
    description="Indirect JMP through FSCV at &021E, providing\n"
    "OS-level filing system services such as FS\n"
    "selection notification (A=6) and *RUN handling.\n"
    "Also contains issue_svc_15 and issue_svc_osbyte\n"
    "entry points that issue paged ROM service requests\n"
    "via OSBYTE &8F.",
    on_entry={"a": "FSCV reason code"})
# Located in 4.21_v1 at &8D24 (was &8D17 in 4.18). Initial fingerprint
# hit &8D21 but a 3-byte preamble (`STZ &0D` and a stray byte) shifts
# the actual entry point to &8D24, where the body matches the 4.18
# routine (LDY ws_page / LDX #5 / LDA (text_ptr),Y / CMP credits,X ...).
# Already classified as code by py8dis (existing &8D24 reference from
# &8C51) — only the subroutine() declaration was missing.
subroutine(0x8D24, "check_credits_easter_egg",
    title="Easter egg: match *HELP keyword to author credits",
    description="Matches the *HELP argument against a keyword\n"
    "embedded in the credits data at\n"
    "credits_keyword_start. Starts matching from offset\n"
    "5 in the data (X=5) and checks each byte against\n"
    "the command line text until a mismatch or X reaches\n"
    "&0D. On a full match, prints the ANFS author\n"
    "credits string: B Cockburn, J Dunn, B Robertson,\n"
    "and J Wills, each terminated by CR.")
subroutine(0x8E21, "clear_if_station_match",
    title="Clear stored station if parsed argument matches",
    description="Parses a station number from the command line via\n"
    "init_bridge_poll and compares it with the expected\n"
    "station at &0E01 using EOR. If the parsed value\n"
    "matches (EOR result is zero), clears &0E01. Called\n"
    "by cmd_iam when processing a file server address\n"
    "in the logon command.",
    on_entry={"os_text_ptr (&F2/&F3)":
              "command-line text pointer (consumed by init_bridge_poll)",
              "&0E01": "expected file-server station number"},
    on_exit={"a": "0 if matched, non-zero if different",
             "&0E01": "zeroed when parsed station matches"})
label(0x8E2D, "check_urd_prefix")
subroutine(0x8E5B, "dir_op_dispatch",
    title="Dispatch directory operation via PHA/PHA/RTS",
    description="Validates X < 5 and sets Y=&0E as the directory\n"
    "dispatch offset, then falls through to svc_dispatch\n"
    "for PHA/PHA/RTS table dispatch. Called by\n"
    "tx_done_os_proc to handle directory operations\n"
    "(e.g. FILEV, ARGSV) from the remote JSR service.",
    on_entry={"x": "directory operation code (0-4)"})
# Located in 4.21_v1 at &8ED2 (was &8E8C in 4.18). Same body
# (LDX #0 / LDY #0 / BEQ jmp_osbyte). Already classified as code
# (sub_c8ed2 with 1 caller from &9A10).
subroutine(0x8ED2, "osbyte_x0_y0",
    title="OSBYTE wrapper with X=0, Y=0",
    description="Sets X=0 and Y=0 then branches to jmp_osbyte.\n"
    "Called from the Econet OSBYTE dispatch chain to\n"
    "handle OSBYTEs that require both X and Y cleared.\n"
    "The unconditional BEQ (after LDY #0 sets Z)\n"
    "reaches the JMP osbyte instruction.",
    on_entry={"a": "OSBYTE number"},
    on_exit={"x": "0", "y": "0"})
subroutine(0x8EF0, "store_ws_page_count",
    title="Record workspace page count (capped at &21)",
    description="Stores the workspace allocation from service 1\n"
    "into offset &0B of the receive control block,\n"
    "capping the value at &21 to prevent overflow into\n"
    "adjacent workspace areas. Called by\n"
    "svc_2_private_workspace after issuing the absolute\n"
    "workspace claim service call.",
    on_entry={"y": "workspace page count from service 1"})
label(0x8FB8, "done_alloc_handles")
subroutine(0x903C, "init_adlc_and_vectors",
    title="Initialise ADLC and install extended vectors",
    description="Reads the ROM pointer table via OSBYTE &A8,\n"
    "writes vector addresses and ROM ID into the\n"
    "extended vector table for NETV and one additional\n"
    "vector, then restores any previous FS context.",
    on_entry={"romsel_copy (&F4)":
              "current ROM slot (written into each vector entry as the "
              "ROM ID byte)"},
    on_exit={"a, x, y": "clobbered (falls through into write_vector_entry)",
             "extended vector table": "NETV (and the next vector) point at "
             "this ROM's handlers; &0D72 set to &FF as install marker"})
subroutine(0x904F, "write_vector_entry",
    title="Install extended vector table entries",
    description="Copies vector addresses from the dispatch table at\n"
    "svc_dispatch_lo_offset+Y into the MOS extended\n"
    "vector table pointed to by fs_error_ptr. For each\n"
    "entry, writes address low, high, then the current\n"
    "ROM ID from romsel_copy (&F4). Loops X times.\n"
    "After the loop, stores &FF at &0D72 as an\n"
    "installed flag, calls deselect_fs_if_active and\n"
    "get_ws_page to restore FS state.",
    on_entry={"x": "number of vectors to install",
              "y": "starting offset in extended vector table"},
    on_exit={"y": "workspace page number + 1"})
subroutine(0x9064, "restore_fs_context",
    title="Restore FS context from saved workspace",
    description="Copies 8 bytes (offsets 2 to 9) from the saved\n"
    "workspace at &0DFA back into the receive control\n"
    "block via (net_rx_ptr). This restores the station\n"
    "identity, directory handles, and library path after\n"
    "a filing system reselection. Called by\n"
    "svc_2_private_workspace during init,\n"
    "deselect_fs_if_active during FS teardown, and\n"
    "flip_set_station_boot.",
    on_entry={"net_rx_ptr (&A6/&A7)":
              "page-aligned pointer to the receive control block",
              "&0DFA..&0E01": "saved 8-byte FS context to restore"},
    on_exit={"a, y": "clobbered (loop counter / data byte)",
             "(net_rx_ptr)+2..+9": "FS context bytes restored from &0DFA+2..+9"})
subroutine(0x9071, "fscv_6_shutdown",
    title="Deselect filing system and save workspace",
    description="If the filing system is currently selected\n"
    "(bit 7 of &0D6C set), closes all open FCBs,\n"
    "closes SPOOL/EXEC files via OSBYTE &77,\n"
    "saves the FS workspace to page &10 shadow\n"
    "with checksum, and clears the selected flag.")
subroutine(0x909E, "verify_ws_checksum",
    title="Verify workspace checksum integrity",
    description="Sums bytes 0 to &76 of the workspace page via the\n"
    "zero-page pointer at &CC/&CD and compares with the\n"
    "stored value at offset &77. On mismatch, raises a\n"
    "'net sum' error (&AA). The checksummed page holds\n"
    "open file information (preserved when NFS is not\n"
    "the current filing system) and the current printer\n"
    "type. Can only be reset by a control BREAK.\n"
    "Preserves A, Y, and processor flags using PHP/PHA.\n"
    "Called by 5 sites across format_filename_field,\n"
    "adjust_fsopts_4bytes, and start_wipe_pass before\n"
    "workspace access.",
    on_exit={"a": "preserved", "y": "preserved"})
# Located in 4.21_v1 at &90C7 (was &8FF1 in 4.18). Found by searching
# for the inline "Econet Station " string at &90CA and reading back to
# the JSR print_inline at &90C7. Already classified as code (c90c7
# auto-label, 2 callers from &8CAA and &8CE4).
subroutine(0x90C7, "print_station_id",
    title="Print Econet station number and clock status",
    description="Uses print_inline to output 'Econet Station ',\n"
    "then reads the station ID from offset 1 of the\n"
    "receive control block and prints it as a decimal\n"
    "number via print_num_no_leading. Tests ADLC\n"
    "status register 2 (&FEA1) to detect the Econet\n"
    "clock; if absent, appends ' No Clock' via a\n"
    "second inline string. Finishes with OSNEWL.\n"
    "Called by print_version_header and svc_3_auto_boot.")
subroutine(0x91F9, "print_newline_no_spool",
    title="Print CR via OSASCI, bypassing any open *SPOOL file",
    description="Loads A=&0D and falls into print_char_no_spool. The "
    "underlying mechanism temporarily writes 0 to the *SPOOL file "
    "handle (OSBYTE &C7 with X=0, Y=0) so the printed CR is not "
    "captured by spool, then restores the previous handle on exit. "
    "Called from service_handler (&8A7C) after the 'Bad ROM <slot>' "
    "message, and from two other diagnostic sites (&8E10, &9D3E).",
    on_exit={"a, x, y, p": "preserved (print_char_no_spool brackets the call "
             "with full register save/restore via PHA/PHP/PLP/PLA)",
             "side effect": "OSASCI prints CR; *SPOOL handle is briefly cleared "
             "and restored if it was an NFS-issued handle (&21-&2F)"})

subroutine(0x91FB, "print_char_no_spool",
    title="Print A via OSASCI, bypassing any open *SPOOL file",
    description="Pushes the caller's flags, then forces V=1 via the "
    "BIT &9769 / BVS trick (&9769 is a constant &FF byte in ROM). "
    "Saves X, Y, A and a copy of the (now V=1) flags. Calls OSBYTE "
    "&C7 with X=0, Y=0 to write 0 to the *SPOOL file handle, "
    "returning the previous handle in X. If the previous handle was "
    "in the NFS-issued range &21-&2F, calls OSBYTE &C7 again with "
    "X=OLD, Y=0 to restore the spool BEFORE the print (so the print "
    "is captured); otherwise leaves spool closed for the duration of "
    "the print. PLPs the inner P, then routes to OSASCI (because the "
    "BIT trick set V=1 -> BVC at &9220 not taken). Final OSBYTE &C7 "
    "with Y=&FF either no-ops (if spool already restored) or writes "
    "OLD back (if it was deferred). Pulls A, Y, X, P and returns.\n"
    "\n"
    "Eight inner-ROM callers: &925F, &92A4, &9D30, &9D5C, &B21F, "
    "&B2F9, &B321, &B752.",
    on_entry={"a": "byte to print as ASCII char (CR is translated by OSASCI)"})

subroutine(0x9201, "print_byte_no_spool",
    title="Print A via OSWRCH (raw, no CR translation), bypass *SPOOL",
    description="As print_char_no_spool but the inner PHP/CLV at &9201 "
    "forces V=0 in the saved flags, so the BVC at &9220 takes the "
    "OSWRCH branch instead of OSASCI. Used when the caller wants to "
    "emit a raw byte (e.g. a VDU control code) without CR translation. "
    "Sole caller in this ROM is at &8DE6.",
    on_entry={"a": "raw byte to print via OSWRCH"})

subroutine(0x9236, "print_hex_byte",
    title="Print A as two hexadecimal digits",
    description="Saves A on the stack, shifts right four times\n"
    "to isolate the high nybble, calls\n"
    "print_hex_nybble to print it, then restores\n"
    "the full byte and falls through to\n"
    "print_hex_nybble for the low nybble. Called by\n"
    "print_5_hex_bytes, cmd_ex, cmd_dump, and\n"
    "print_dump_header.",
    on_entry={"a": "byte to print"},
    on_exit={"a": "original byte value"})
subroutine(0x923F, "print_hex_nybble",
    title="Print low nybble of A as hex digit",
    description="Masks A to the low 4 bits, then converts to\n"
    "ASCII: adds 7 for letters A-F (via ADC #6 with\n"
    "carry set from the CMP), then ADC #&30 for the\n"
    "final '0'-'F' character. Outputs via JMP OSASCI.",
    on_entry={"a": "value (low nybble used)"})
subroutine(0x92B2, "parse_addr_arg",
    title="Parse decimal or hex station address argument",
    description="Located at &92B2 in 4.21_v1 (was &916E in 4.18, +&144 "
    "shift). Reads characters from the command argument at "
    "(fs_crc_lo),Y. Supports `&` prefix for hex, `.` separator for "
    "net.station addresses, and plain decimal. Returns the result in "
    "fs_load_addr_2 (and A). Raises 'Bad hex' / 'Bad number' / "
    "'Bad station number' / overflow errors as appropriate. The body "
    "uses the standard 6502 idioms: ASL ASL ASL ASL + ADC for hex "
    "digit accumulation, and result*2 + result*8 for decimal *10. "
    "Two named callers: sub_c92b2 from &A3C9 and &A3DE.",
    on_entry={
        "y": "index into command-string buffer at (fs_crc_lo),Y",
        "a": "ignored",
    },
    on_exit={
        "fs_load_addr_2": "parsed numeric value",
        "c": "set if a number was parsed",
    })
subroutine(0x939A, "is_decimal_digit",
    title="Test for digit, '&', or '.' separator",
    description="Compares A against '&' and '.' first; if\n"
    "either matches, returns with carry set via the\n"
    "shared return_12 exit. Otherwise falls through\n"
    "to is_dec_digit_only for the '0'-'9' range\n"
    "test. Called by cmd_iam, cmd_ps, and\n"
    "cmd_pollps when parsing station addresses.",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if digit/&/., clear otherwise"})
subroutine(0x93A2, "is_dec_digit_only",
    title="Test for decimal digit '0'-'9'",
    description="Uses two CMPs to bracket-test A against the\n"
    "range &30-&39. CMP #&3A sets carry if A >= ':'\n"
    "(above digits), then CMP #&30 sets carry if\n"
    "A >= '0'. The net effect: carry set only for\n"
    "'0'-'9'. Called by parse_addr_arg.",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if '0'-'9', clear otherwise"})
subroutine(0x93AB, "get_access_bits",
    title="Read and encode directory entry access byte",
    description="Loads the access byte from offset &0E of the\n"
    "directory entry via (fs_options),Y, masks to 6\n"
    "bits (AND #&3F), then sets X=4 and branches to\n"
    "begin_prot_encode to map through the protection\n"
    "bit encode table at &9286. Called by\n"
    "check_and_setup_txcb for owner and public access.",
    on_entry={"fs_options (&BB/&BC)":
              "pointer to start of directory entry "
              "(access byte is read at offset &0E)"},
    on_exit={"a": "encoded access flags",
             "x": "&FF + bits-set (left in this state by get_prot_bits "
             "fall-through)"})
subroutine(0x93B5, "get_prot_bits",
    title="Encode protection bits via lookup table",
    description="Masks A to 5 bits (AND #&1F), sets X=&FF to\n"
    "start at table index 0, then enters the shared\n"
    "encoding loop at begin_prot_encode. Shifts out\n"
    "each source bit and ORs in the corresponding\n"
    "value from prot_bit_encode_table (&9286). Called\n"
    "by send_txcb_swap_addrs and check_and_setup_txcb.",
    on_entry={"a": "raw protection bits (low 5 used)"},
    on_exit={"a": "encoded protection flags"})
subroutine(0x93D3, "set_text_and_xfer_ptr",
    title="Set OS text pointer then transfer parameters",
    description="Stores X/Y into the MOS text pointer at\n"
    "&F2/&F3, then falls through to set_xfer_params\n"
    "and set_options_ptr to configure the full FS\n"
    "transfer context. Called by byte_to_2bit_index.",
    on_entry={"x": "text pointer low byte",
              "y": "text pointer high byte"})
subroutine(0x93D7, "set_xfer_params",
    title="Set FS transfer byte count and source pointer",
    description="Stores A into fs_last_byte_flag (&BD) as the\n"
    "transfer byte count, and X/Y into fs_crc_lo/hi\n"
    "(&BE/&BF) as the source data pointer. Falls\n"
    "through to set_options_ptr to complete the\n"
    "transfer context setup. Called by 5 sites across\n"
    "cmd_ex, format_filename_field, and gsread_to_buf.",
    on_entry={"a": "transfer byte count",
              "x": "source pointer low",
              "y": "source pointer high"})
subroutine(0x93DD, "set_options_ptr",
    title="Set FS options pointer and clear escape flag",
    description="Stores X/Y into fs_options/fs_block_offset\n"
    "(&BB/&BC) as the options block pointer. Then\n"
    "enters clear_escapable which uses PHP/LSR/PLP\n"
    "to clear bit 0 of the escape flag at &97 without\n"
    "disturbing processor flags. Called by\n"
    "format_filename_field and send_and_receive.",
    on_entry={"x": "options pointer low",
              "y": "options pointer high"})
subroutine(0x93E6, "cmp_5byte_handle",
    title="Compare 5-byte handle buffers for equality",
    description="Loops X from 4 down to 1, comparing each byte\n"
    "of l00af+X with fs_load_addr_3+X using EOR.\n"
    "Returns on the first mismatch (Z=0) or after\n"
    "all 5 bytes match (Z=1). Called by\n"
    "send_txcb_swap_addrs and check_and_setup_txcb\n"
    "to verify station/handle identity.",
    on_entry={"l00af+1..+4": "first 5-byte handle buffer (offset 0 is skipped)",
              "fs_load_addr_3+1..+4": "second 5-byte handle buffer"},
    on_exit={"z": "set if bytes 1..4 match (byte 0 is not compared)",
             "a": "EOR of last compared bytes",
             "x": "0 if all matched, else mismatch index"})
subroutine(0x93F7, "set_conn_active",
    title="Set connection-active flag in channel table",
    description="Saves registers on the stack, recovers the\n"
    "original A from the stack via TSX/LDA &0102,X,\n"
    "then calls attr_to_chan_index to find the channel\n"
    "slot. ORs bit 6 (&40) into the channel status\n"
    "byte at &1060+X. Preserves A, X, and processor\n"
    "flags via PHP/PHA/PLA/PLP. Called by\n"
    "format_filename_field and adjust_fsopts_4bytes.",
    on_entry={"a": "channel attribute byte"})
subroutine(0x940D, "clear_conn_active",
    title="Clear connection-active flag in channel table",
    description="Mirror of set_conn_active but ANDs the channel\n"
    "status byte with &BF (bit 6 clear mask) instead\n"
    "of ORing. Uses the same register-preservation\n"
    "pattern: PHP/PHA/TSX to recover A, then\n"
    "attr_to_chan_index to find the slot. Shares the\n"
    "done_conn_flag exit with set_conn_active.",
    on_entry={"a": "channel attribute byte"})
subroutine(0x9446, "check_not_ampersand",
    title="Reject '&' as filename character",
    description="Loads the first character from the parse buffer\n"
    "at &0E30 and compares with '&' (&26). Branches\n"
    "to error_bad_filename if matched, otherwise\n"
    "returns. Also contains read_filename_char which\n"
    "loops reading characters from the command line\n"
    "into the TX buffer at &0F05, calling\n"
    "strip_token_prefix on each byte and terminating\n"
    "on CR. Used by cmd_fs_operation and cmd_rename.",
    on_entry={"&0E30": "first byte of the parsed filename buffer"},
    on_exit={"a": "first byte of parse buffer (preserved unchanged on the "
             "non-error path)",
             "behaviour": "raises 'Bad filename' error and does not return "
             "if the first character is '&'"})
# Located in 4.21_v1 at &9463 (was &9327 in 4.18). Initial fingerprint
# hit &945E (which is `send_fs_request`) — the body match pushed the
# entry 5 bytes earlier than the actual prologue. The 4.21 prologue
# uses 65C12 PHY in place of 4.18's TYA / PHA. Already classified as
# code (sub_c9463 with 2 callers from &9425 and &94c5).
subroutine(0x9463, "copy_fs_cmd_name",
    title="Copy matched command name to TX buffer",
    description="Scans backwards in cmd_table_fs from the\n"
    "current position to find the bit-7 flag byte\n"
    "marking the start of the command name. Copies\n"
    "each character forward into the TX buffer at\n"
    "&C105 (was &0F05 in 4.18) until the next bit-7\n"
    "byte (end of name), then appends a space\n"
    "separator. Uses 65C12 PHY in 4.21 in place of\n"
    "4.18's TYA / PHA prologue.",
    on_entry={"x": "byte offset within cmd_table_fs (just past the matched "
              "command's last name char)",
              "y": "current command-line offset (saved/restored)"},
    on_exit={"x": "TX buffer offset past name+space",
             "y": "command line offset (restored)",
             "a": "clobbered",
             "TX buffer at &C105+": "command name + trailing space"})
subroutine(0x9483, "parse_quoted_arg",
    title="Parse possibly-quoted filename argument",
    description="Reads from the command line at (&BE),Y. Handles\n"
    "double-quote delimiters and stores the result\n"
    "in the parse buffer at &0E30. Raises 'Bad string'\n"
    "on unbalanced quotes.",
    on_entry={"fs_crc_lo, fs_crc_hi (&BE/&BF)":
              "command-line text pointer (saved by save_text_ptr)",
              "y": "current offset within the command line"},
    on_exit={"&0E30": "parsed argument (without surrounding quotes)",
             "y": "advanced past the parsed argument",
             "a": "clobbered (last byte read)",
             "behaviour": "raises 'Bad string' on unbalanced quotes; "
             "falls through to cmd_rename on the success path"})
subroutine(0x973D, "init_txcb_bye",
    title="Set up open receive for FS reply on port &90",
    description="Loads A=&90 (the FS command/reply port) and\n"
    "falls through to init_txcb_port, which creates\n"
    "an open receive control block: the template sets\n"
    "txcb_ctrl to &80, then DEC makes it &7F (bit 7\n"
    "clear = awaiting reply). The NMI RX handler sets\n"
    "bit 7 when a reply arrives on this port, which\n"
    "wait_net_tx_ack polls for.",
    on_exit={"txcb at &00C0":
             "12-byte template copied; port = &90; "
             "ctrl = &7F (open-receive, bit 7 clear = awaiting reply); "
             "start = 3"})
subroutine(0x973F, "init_txcb_port",
    title="Create open receive control block on specified port",
    description="Calls init_txcb to copy the 12-byte template\n"
    "into the TXCB workspace at &00C0, then stores A\n"
    "as the port (txcb_port at &C1) and sets\n"
    "txcb_start to 3. The DEC txcb_ctrl changes the\n"
    "control byte from &80 to &7F (bit 7 clear),\n"
    "creating an open receive: the NMI RX handler\n"
    "will set bit 7 when a reply frame arrives on\n"
    "this port, which wait_net_tx_ack polls for.",
    on_entry={"a": "port number"})
subroutine(0x974B, "init_txcb",
    title="Initialise TX control block from ROM template",
    description="Copies 12 bytes from txcb_init_template (&948B)\n"
    "into the TXCB workspace at &00C0. For the first\n"
    "two bytes (Y=0,1), also copies the destination\n"
    "station/network from &0E00 into txcb_dest (&C2).\n"
    "Preserves A via PHA/PLA. Called by 4 sites\n"
    "including cmd_pass, init_txcb_port,\n"
    "prep_send_tx_cb, and send_wipe_request.",
    on_entry={"&0E00, &0E01": "destination station, network "
              "(also written to txcb_dest)"},
    on_exit={"a": "preserved",
             "x, y": "clobbered (Y left at &FF on loop exit)",
             "txcb at &00C0..&00CB":
             "12-byte template loaded; bytes 2/3 are dst station/network"})
subroutine(0x976F, "send_request_nowrite",
    title="Send read-only FS request (carry set)",
    description="Pushes A and sets carry to indicate no-write\n"
    "mode, then branches to txcb_copy_carry_set to\n"
    "enter the common TXCB copy, send, and reply\n"
    "processing path. The carry flag controls whether\n"
    "a disconnect is sent on certain reply codes.\n"
    "Called by setup_transfer_workspace.",
    on_entry={"y": "FS function code (stored as TX[1] = txcb_func by "
              "txcb_copy_carry_set)",
              "a": "saved on stack at entry (consumed by the txcb "
              "send/receive path)"})
subroutine(0x9773, "send_request_write",
    title="Send read-write FS request (V clear)",
    description="Clears V flag and branches unconditionally to\n"
    "txcb_copy_carry_clr (via BVC, always taken after\n"
    "CLV) to enter the common TXCB copy, send, and\n"
    "reply processing path with carry clear (write\n"
    "mode). Called by do_fs_cmd_iteration and\n"
    "send_txcb_swap_addrs.",
    on_entry={"y": "FS function code (stored as TX[1] = txcb_func by "
              "txcb_copy_carry_clr)",
              "a": "request payload byte (used by the txcb send path)"})
subroutine(0x978A, "save_net_tx_cb",
    title="Save FS state and send command to file server",
    description="Copies station address and function code (Y)\n"
    "to the TX buffer, builds the TXCB, sends the\n"
    "packet, and waits for the reply. V is clear\n"
    "for standard mode.",
    on_entry={"y": "FS function code (becomes TX[1] = txcb_func)",
              "x": "TX buffer payload length "
              "(prep_send_tx_cb uses X+5 as txcb_end)",
              "&0E02, &0E03": "FS station/network (copied to &0F02/&0F03)"},
    on_exit={"a": "FS reply status",
             "behaviour":
             "performs full send/receive via prep_send_tx_cb -> "
             "recv_and_process_reply; may BRK with FS-reported error"})
subroutine(0x978B, "save_net_tx_cb_vset",
    title="Save and send TXCB with V flag set",
    description="Variant of save_net_tx_cb for callers that have\n"
    "already set V. Copies the FS station address\n"
    "from &0E02 to &0F02, then falls through to\n"
    "txcb_copy_carry_clr which clears carry and enters\n"
    "the common TXCB copy, send, and reply path.\n"
    "Called by check_and_setup_txcb,\n"
    "format_filename_field, and cmd_remove.",
    on_entry={"y": "FS function code",
              "x": "TX buffer payload length",
              "v flag": "set by caller (selects this variant via the "
              "'no CLV' fall-through from save_net_tx_cb)",
              "&0E02, &0E03": "FS station/network"},
    on_exit={"a": "FS reply status",
             "behaviour":
             "see save_net_tx_cb -- same send/receive cycle, "
             "with V left set across the txcb-copy phase"})
subroutine(0x97B7, "prep_send_tx_cb",
    title="Build TXCB from scratch, send, and receive reply",
    description="Full send/receive cycle comprising two separate\n"
    "Econet transactions. Saves flags, sets reply\n"
    "port &90, calls init_txcb, computes txcb_end\n"
    "from X+5. C set dispatches to handle_disconnect;\n"
    "C clear calls init_tx_ptr_and_send for a\n"
    "client-initiated four-way handshake (scout, ACK,\n"
    "data, ACK) to deliver the command. After TX\n"
    "completes the ADLC returns to idle RX listen.\n"
    "Then falls through to recv_and_process_reply\n"
    "which waits for the server to independently\n"
    "initiate a new four-way handshake with the\n"
    "reply on port &90. There is no reply data in\n"
    "the original ACK payload.",
    on_entry={"x": "TX buffer payload length (txcb_end = X + 5)",
              "y": "FS function code (already stashed by the txcb-copy "
              "entry path)",
              "c flag": "set = disconnect path (handle_disconnect); "
              "clear = normal four-way handshake send",
              "txcb at &00C0": "destination station/network already populated"},
    on_exit={"a": "FS reply status (or doesn't return on error)",
             "txcb_end (&C8)": "TX buffer end offset"})
subroutine(0x97CD, "recv_and_process_reply",
    title="Receive FS reply and dispatch on status codes",
    description="Waits for a server-initiated reply transaction.\n"
    "After the command TX completes (a separate\n"
    "client-initiated four-way handshake), calls\n"
    "init_txcb_bye to set up an open receive on\n"
    "port &90 (txcb_ctrl = &7F). The server\n"
    "independently initiates a new four-way handshake\n"
    "to deliver the reply; the NMI RX handler matches\n"
    "the incoming scout against this RXCB and sets\n"
    "bit 7 on completion. wait_net_tx_ack polls for\n"
    "this. Iterates over reply bytes: zero terminates,\n"
    "V-set codes are adjusted by +&2B, and non-zero\n"
    "codes dispatch to store_reply_status. Handles\n"
    "disconnect requests (C set from prep_send_tx_cb)\n"
    "and 'Data Lost' warnings when channel status\n"
    "bits indicate pending writes were interrupted.",
    on_entry={"c flag": "set = disconnect mode (caller sent a disconnect "
              "scout; handle the server's matching reply)",
              "txcb at &00C0": "still set up by prep_send_tx_cb (port &90)"},
    on_exit={"a": "FS reply status byte",
             "behaviour":
             "may BRK on FS-reported errors (via classify_reply_error / "
             "build_simple_error). 'No reply' is raised if the open "
             "receive times out in wait_net_tx_ack."})
# UNMAPPED: subroutine(0x9570, "check_escape",
# UNMAPPED:     title="Check for pending escape condition",
# UNMAPPED:     description="ANDs the MOS escape flag (&FF) with the\n"
# UNMAPPED:     "escapable flag at &97. If bit 7 of the result\n"
# UNMAPPED:     "is clear (no escape or escape disabled), returns\n"
# UNMAPPED:     "immediately. Otherwise enters raise_escape_error:\n"
# UNMAPPED:     "acknowledges the escape via OSBYTE &7E, then\n"
# UNMAPPED:     "jumps to classify_reply_error with A=6 to raise\n"
# UNMAPPED:     "the Escape error. Called by cmd_pass and\n"
# UNMAPPED:     "send_net_packet.")
subroutine(0x98BE, "wait_net_tx_ack",
    title="Wait for reply on open receive with timeout",
    description="Despite the name, this does not wait for a TX\n"
    "acknowledgment. It polls an open receive control\n"
    "block (bit 7 of txcb_ctrl, set to &7F by\n"
    "init_txcb_port) until the NMI RX handler delivers\n"
    "a reply frame and sets bit 7. Uses a three-level\n"
    "nested polling loop: inner and middle counters\n"
    "start at 0 (wrapping to 256 iterations each),\n"
    "outer counter from rx_wait_timeout (&0D6E,\n"
    "default &28 = 40). Total: 256 x 256 x 40 =\n"
    "2,621,440 poll iterations. At ~17 cycles per\n"
    "poll on a 2 MHz 6502, the default gives ~22\n"
    "seconds. On timeout, branches to\n"
    "build_no_reply_error to raise 'No reply'.\n"
    "Called by 6 sites across the protocol stack.",
    on_entry={"txcb at &00C0":
              "open-receive control block with txcb_ctrl bit 7 clear "
              "(set to &7F by init_txcb_port)",
              "rx_wait_timeout (&0D6E)":
              "outer-loop count (default &28 ~ 22 s on 2 MHz 6502)"},
    on_exit={"behaviour":
             "returns when txcb_ctrl bit 7 becomes set (reply received); "
             "on timeout, tail-jumps to build_no_reply_error which raises "
             "'No reply' via BRK and does not return"})
subroutine(0x9900, "cond_save_error_code",
    title="Conditionally store error code to workspace",
    description="Tests bit 7 of &0D6C (FS selected flag). If\n"
    "clear, returns immediately. If set, stores A\n"
    "into &0E09 as the last error code. This guards\n"
    "against writing error state when no filing system\n"
    "is active. Called internally by the error\n"
    "classification chain and by error_inline_log.",
    on_entry={"a": "error code to store"})
# UNMAPPED: label(0x971E, "close_exec_via_y")
subroutine(0x9A3A, "append_drv_dot_num",
    title="Append 'net.station' decimal string to error text",
    description="Reads network and station numbers from the TX\n"
    "control block at offsets 3 and 2. Writes a space\n"
    "separator then the network number (if non-zero),\n"
    "a dot, and the station number as decimal digits\n"
    "into the error text buffer at the current position.",
    on_entry={"x": "error text buffer index"},
    on_exit={"x": "updated buffer index past appended text"})
subroutine(0x9A5E, "append_space_and_num",
    title="Append space and decimal number to error text",
    description="Writes a space character to the error text buffer\n"
    "at the current position (fs_load_addr_2), then falls\n"
    "through to append_decimal_num to convert the value\n"
    "in A to decimal digits with leading zero suppression.",
    on_entry={"a": "number to append (0-255)"})
subroutine(0x9A69, "append_decimal_num",
    title="Convert byte to decimal and append to error text",
    description="Extracts hundreds, tens and units digits by three\n"
    "successive calls to append_decimal_digit. Uses the\n"
    "V flag to suppress leading zeros — hundreds and tens\n"
    "are skipped when zero, but the units digit is always\n"
    "emitted.",
    on_entry={"a": "number to convert (0-255)"})
subroutine(0x9A7A, "append_decimal_digit",
    title="Extract and append one decimal digit",
    description="Divides Y by A using repeated subtraction to extract\n"
    "a single decimal digit. Stores the ASCII digit in the\n"
    "error text buffer at fs_load_addr_2 unless V is set\n"
    "and the quotient is zero (leading zero suppression).\n"
    "Returns the remainder in Y for subsequent digit\n"
    "extraction.",
    on_entry={"a": "divisor (100, 10, or 1)",
              "y": "number to divide",
              "v": "set to suppress leading zero"},
    on_exit={"y": "remainder after division",
             "v": "clear once a non-zero digit is emitted"})
subroutine(0x9B24, "init_tx_ptr_and_send",
    title="Point TX at zero-page TXCB and send",
    description="Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the\n"
    "standard TXCB location in zero page), then falls\n"
    "through to send_net_packet for transmission with\n"
    "retry logic.")
subroutine(0x9B2C, "send_net_packet",
    title="Transmit Econet packet with retry",
    description="Two-phase transmit with retry. Loads retry count\n"
    "from tx_retry_count (&0D6D, default &FF = 255;\n"
    "0 means retry forever). Each failed attempt waits\n"
    "in a nested delay loop: X = TXCB control byte\n"
    "(typically &80), Y = &60; total ~61 ms at 2 MHz\n"
    "(ROM-only fetches, unaffected by video mode).\n"
    "Phase 1 runs the full count with escape disabled.\n"
    "Phase 2 only activates when tx_retry_count = 0:\n"
    "sets need_release_tube to enable escape checking\n"
    "and retries indefinitely. With default &FF, phase\n"
    "2 is never entered. Failures go to\n"
    "load_reply_and_classify (Line jammed, Net error,\n"
    "etc.), distinct from the 'No reply' timeout in\n"
    "wait_net_tx_ack.")
subroutine(0x9B81, "init_tx_ptr_for_pass",
    title="Set up TX pointer and send pass-through packet",
    description="Copies the template into the TX buffer (skipping\n"
    "&FD markers), saves original values on stack,\n"
    "then polls the ADLC and retries until complete.")
subroutine(0x9B89, "setup_pass_txbuf",
    title="Initialise TX buffer from pass-through template",
    description="Copies 12 bytes from pass_txbuf_init_table into the\n"
    "TX control block, pushing the original values on the\n"
    "stack for later restoration. Skips offsets marked &FD\n"
    "in the template. Starts transmission via\n"
    "poll_adlc_tx_status and retries on failure, restoring\n"
    "the original TX buffer contents when done.")
subroutine(0x9BB6, "poll_adlc_tx_status",
    title="Wait for TX ready, then start new transmission",
    description="Polls tx_complete_flag via ASL (testing bit 7)\n"
    "until set, indicating any previous TX operation\n"
    "has completed and the ADLC is back in idle RX\n"
    "listen mode. Then copies the TX control block\n"
    "pointer from net_tx_ptr to nmi_tx_block and\n"
    "calls tx_begin, which performs a complete\n"
    "transmission from scratch: copies destination\n"
    "from TXCB to scout buffer, polls for INACTIVE,\n"
    "configures ADLC (CR1=&44 RX_RESET|TIE, CR2=&E7\n"
    "RTS|CLR), and runs the full four-way handshake\n"
    "via NMI. After tx_begin returns, polls the TXCB\n"
    "first byte until bit 7 clears (NMI handler\n"
    "stores result there). Returns result in A:\n"
    "&00=success, &40=jammed, &41=not listening,\n"
    "&43=no clock, &44=bad control byte.")
subroutine(0x9BF5, "load_text_ptr_and_parse",
    title="Copy text pointer from FS options and parse string",
    description="Reads a 2-byte address from (fs_options)+0/1 into\n"
    "os_text_ptr (&00F2), resets Y to zero, then falls\n"
    "through to gsread_to_buf to parse the string at that\n"
    "address into the &0E30 buffer.")
subroutine(0x9C00, "gsread_to_buf",
    title="Parse command line via GSINIT/GSREAD into &0E30",
    description="Calls GSINIT to initialise string reading, then\n"
    "loops calling GSREAD to copy characters into the\n"
    "l0e30 buffer until end-of-string. Appends a CR\n"
    "terminator and sets fs_crc_lo/hi to point at &0E30\n"
    "for subsequent parsing routines.")
subroutine(0x9C3E, "do_fs_cmd_iteration",
    title="Execute one iteration of a multi-step FS command",
    description="Called by match_fs_cmd for commands that enumerate\n"
    "directory entries. Sets port &92, sends the initial\n"
    "request via send_request_write, then synchronises the\n"
    "FS options and workspace state (order depends on the\n"
    "cycle flag at offset 6). Copies 4 address bytes,\n"
    "formats the filename field, sends via\n"
    "send_txcb_swap_addrs, and receives the reply.")
subroutine(0x9C85, "send_txcb_swap_addrs",
    title="Send TXCB and swap start/end addresses",
    description="If the 5-byte handle matches, returns\n"
    "immediately. Otherwise sets port &92, copies\n"
    "addresses, sends, waits for acknowledgment,\n"
    "and retries on address mismatch.")
subroutine(0x9D44, "print_load_exec_addrs",
    title="Print exec address and file length in hex",
    description="Prints the exec address as 5 hex bytes from\n"
    "(fs_options) offset 9 downwards, then the file\n"
    "length as 3 hex bytes from offset &0C. Each group\n"
    "is followed by a space separator via OSASCI.")
subroutine(0x9D4F, "print_5_hex_bytes",
    title="Print hex byte sequence from FS options",
    description="Outputs X+1 bytes from (fs_options) starting at\n"
    "offset Y, decrementing Y for each byte (big-endian\n"
    "display order). Each byte is printed as two hex\n"
    "digits via print_hex_byte. Finishes with a trailing\n"
    "space via OSASCI. The default entry with X=4 prints\n"
    "5 bytes (a full 32-bit address plus extent).",
    on_entry={"x": "byte count minus 1 (default 4 for 5 bytes)",
              "y": "starting offset in (fs_options)"})
subroutine(0x9D5F, "copy_fsopts_to_zp",
    title="Copy FS options address bytes to zero page",
    description="Copies 4 bytes from (fs_options) at offsets 2-5\n"
    "into zero page at &00AE+Y. Used by\n"
    "do_fs_cmd_iteration to preserve the current address\n"
    "state. Falls through to skip_one_and_advance5 to\n"
    "advance Y past the copied region.")
subroutine(0x9D6B, "skip_one_and_advance5",
    title="Advance Y by 5",
    description="Entry point one INY before advance_y_by_4, giving\n"
    "a total Y increment of 5. Used to skip past a\n"
    "5-byte address/length structure in the FS options\n"
    "block.")
subroutine(0x9D6C, "advance_y_by_4",
    title="Advance Y by 4",
    description="Four consecutive INY instructions. Used as a\n"
    "subroutine to step Y past a 4-byte address field\n"
    "in the FS options or workspace structure.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 4"})
subroutine(0x9D71, "copy_workspace_to_fsopts",
    title="Copy workspace reply data to FS options",
    description="Copies bytes from the reply buffer at &0F02+Y\n"
    "into (fs_options) at offsets &0D down to 2. Used\n"
    "to update the FS options block with data returned\n"
    "from the file server. Falls through to\n"
    "retreat_y_by_4.")
subroutine(0x9D7E, "retreat_y_by_4",
    title="Retreat Y by 4",
    description="Four consecutive DEY instructions. Companion to\n"
    "advance_y_by_4 for reverse traversal of address\n"
    "structures.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 4"})
subroutine(0x9D7F, "retreat_y_by_3",
    title="Retreat Y by 3",
    description="Three consecutive DEY instructions. Used by\n"
    "setup_transfer_workspace to step back through\n"
    "interleaved address pairs in the FS options block.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 3"})
subroutine(0x9D87, "check_and_setup_txcb",
    title="Set up data transfer TXCB and dispatch reply",
    description="Compares the 5-byte handle; if unchanged,\n"
    "returns. Otherwise computes start/end addresses\n"
    "with overflow clamping, sets the port and control\n"
    "byte, sends the packet, and dispatches on the\n"
    "reply sub-operation code.")
subroutine(0x9E82, "format_filename_field",
    title="Format filename into fixed-width display field",
    description="Builds a 12-character space-padded filename at\n"
    "&10F3 for directory listing output. Sources the\n"
    "name from either the command line or the l0f05\n"
    "reply buffer depending on the value in l0f03.\n"
    "Truncates or pads to exactly 12 characters.")
subroutine(0x9FB6, "finalise_and_return",
    title="Clear receive-attribute and restore caller's X/Y",
    description="Common 7-byte exit sequence used at the end of "
    "format_filename_field, several FS reply handlers, and "
    "match_fs_cmd. Saves A across a call to store_rx_attribute(0) "
    "(which clears the receive-attribute byte), then restores X "
    "from fs_options and Y from fs_block_offset before returning. "
    "Effectively: 'finish processing, clear network state, restore "
    "caller's pointers'.\n"
    "\n"
    "One JSR caller (match_fs_cmd at &A599) plus 6 branch entries "
    "from format_filename_field's various exit paths.",
    on_entry={"a": "result code to return"},
    on_exit={"a": "preserved",
             "x": "fs_options low byte",
             "y": "fs_block_offset low byte"})

subroutine(0xA12C, "update_addr_from_offset9",
    title="Update both address fields in FS options",
    description="Calls add_workspace_to_fsopts for offset 9 (the\n"
    "high address / exec address field), then falls\n"
    "through to update_addr_from_offset1 to process\n"
    "offset 1 (the low address / load address field).")
subroutine(0xA131, "update_addr_from_offset1",
    title="Update low address field in FS options",
    description="Sets Y=1 and falls through to\n"
    "add_workspace_to_fsopts to add the workspace\n"
    "adjustment bytes to the load address field at\n"
    "offset 1 in the FS options block.",
    on_entry={"c": "carry state passed to add_workspace_to_fsopts"})
subroutine(0xA133, "add_workspace_to_fsopts",
    title="Add workspace bytes to FS options with clear carry",
    description="Clears carry and falls through to\n"
    "adjust_fsopts_4bytes. Provides a convenient entry\n"
    "point when the caller needs addition without a\n"
    "preset carry.",
    on_entry={"y": "FS options offset for first byte"})
subroutine(0xA134, "adjust_fsopts_4bytes",
    title="Add or subtract 4 workspace bytes from FS options",
    description="Processes 4 consecutive bytes at (fs_options)+Y,\n"
    "adding or subtracting the corresponding workspace\n"
    "bytes from &0E0A-&0E0D. The direction is controlled\n"
    "by bit 7 of fs_load_addr_2: set for subtraction,\n"
    "clear for addition. Carry propagates across all 4\n"
    "bytes for correct multi-byte arithmetic.",
    on_entry={"y": "FS options offset for first byte",
              "c": "carry input for first byte"})
label(0xA1EA, "return_success")
subroutine(0xA1EF, "lookup_cat_entry_0",
    title="Look up channel from FS options offset 0",
    description="Loads the channel handle from (fs_options) at\n"
    "offset 0, then falls through to lookup_cat_slot_data\n"
    "to find the corresponding FCB entry.",
    on_exit={"a": "FCB flag byte from &1030+X",
             "x": "channel slot index"})
subroutine(0xA1F3, "lookup_cat_slot_data",
    title="Look up channel and return FCB flag byte",
    description="Calls lookup_chan_by_char to find the channel\n"
    "slot for handle A in the channel table, then\n"
    "loads the FCB flag byte from &1030+X.",
    on_entry={"a": "channel handle"},
    on_exit={"a": "FCB flag byte",
             "x": "channel slot index"})
subroutine(0xA1FA, "setup_transfer_workspace",
    title="Prepare workspace for OSGBPB data transfer",
    description="Orchestrates the setup for OSGBPB (get/put\n"
    "multiple bytes) operations. Looks up the channel,\n"
    "copies the 6-byte address structure from FS options\n"
    "(skipping the hole at offset 8), determines transfer\n"
    "direction from the operation code (even=read,\n"
    "odd=write), selects port &91 or &92 accordingly,\n"
    "and sends the FS request. Then configures the TXCB\n"
    "address pairs for the actual data transfer phase\n"
    "and dispatches to the appropriate handler.")
subroutine(0xA284, "recv_reply_preserve_flags",
    title="Receive and process reply, preserving flags",
    description="Wrapper around recv_and_process_reply that\n"
    "saves and restores the processor status register,\n"
    "so the caller\'s flag state is not affected by\n"
    "the reply processing.",
    on_entry={"txcb at &00C0": "open-receive control block from "
              "init_txcb_port (caller's setup)"},
    on_exit={"a": "FS reply status",
             "p (flags)": "preserved across the call (PHP/PLP)",
             "behaviour": "may BRK on FS-reported errors via "
             "recv_and_process_reply"})
subroutine(0xA2ED, "write_data_block",
    title="Write data block to destination or Tube",
    description="If no Tube present, copies directly from\n"
    "the l0f05 buffer via (fs_crc_lo). If Tube\n"
    "is active, claims the Tube, sets up the\n"
    "transfer address, and writes via R3.")
subroutine(0xA390, "tube_claim_c3",
    title="Claim the Tube via protocol &C3",
    description="Loops calling tube_addr_data_dispatch with\n"
    "protocol byte &C3 until the claim succeeds\n"
    "(carry set on return). Used before Tube data\n"
    "transfers to ensure exclusive access to the\n"
    "Tube co-processor interface.",
    on_exit={"a": "&C3 (the claim protocol byte left in A)",
             "c flag": "set (the claim succeeded -- this is the loop "
             "termination condition)",
             "Tube state": "exclusive claim held; matching release via "
             "tube_addr_data_dispatch with &C2 expected from caller"})
subroutine(0xA3BB, "print_fs_info_newline",
    title="Print station address and newline",
    description="Sets V (suppressing leading-zero padding on\n"
    "the network number) then prints the station\n"
    "address followed by a newline via OSNEWL.\n"
    "Used by *FS and *PS output formatting.",
    on_entry={"fs_work_6 (&B6)": "network number (consumed by "
              "print_station_addr)",
              "fs_work_7 (&B7)": "station number"},
    on_exit={"a, x, y": "clobbered (print_station_addr + OSNEWL)",
             "side effect": "writes 'NN.SSS' or 'SSS' followed by CR/LF "
             "to the current output stream"})
# Located in 4.21_v1 at &A3C4 (was &A0A7 in 4.18). Body matches with
# 65C12 PHX/PHY replacing 4.18's TXA/PHA and TYA/PHA, plus the
# parsed-station storage moves from fs_work_6 (&B6) to fs_work_7
# (&B7). Already classified as code (sub_ca3c4 with 3 callers from
# &A3A8, &B3CF, &B5A6).
subroutine(0xA3C4, "parse_fs_ps_args",
    title="Parse station address from *FS/*PS arguments",
    description="Reads a station address in 'net.station' format\n"
    "from the command line, with the network number\n"
    "optional (defaults to local network). Calls\n"
    "init_bridge_poll to ensure the bridge routing\n"
    "table is populated, then validates the parsed\n"
    "address against known stations. 4.21 version uses\n"
    "65C12 PHX/PHY in place of TXA/PHA, TYA/PHA, and\n"
    "stores the result in fs_work_7 (was fs_work_6 in\n"
    "4.18).",
    on_entry={"os_text_ptr (&F2/&F3)":
              "command-line text pointer (consumed by parse_addr_arg)",
              "y": "current command-line offset"},
    on_exit={"fs_work_7 (&B7)": "parsed station number",
             "fs_work_6 (&B6)": "parsed network number (0 if not specified)",
             "x, y": "preserved (saved/restored via PHX/PHY)",
             "behaviour": "raises 'Bad station' via parse_addr_arg on "
             "malformed input"})
subroutine(0xA3E7, "get_pb_ptr_as_index",
    title="Convert parameter block pointer to table index",
    description="Reads the first byte from the OSWORD parameter\n"
    "block pointer and falls through to\n"
    "byte_to_2bit_index to produce a 12-byte-aligned\n"
    "table index in Y.")
subroutine(0xA3E9, "byte_to_2bit_index",
    title="Convert byte to 12-byte-aligned table index",
    description="Computes Y = A * 6 (via A*12/2) for indexing\n"
    "into the OSWORD handler workspace tables.\n"
    "Clamps Y to zero if the result exceeds &48,\n"
    "preventing out-of-bounds access.",
    on_entry={"a": "table entry number"},
    on_exit={"y": "byte offset (0, 6, 12, ... up to &42)"})
subroutine(0xA45B, "match_fs_cmd",
    title="Match command name against FS command table",
    description="Case-insensitive compare of the command line\n"
    "against table entries with bit-7-terminated\n"
    "names. Returns with the matched entry address\n"
    "on success.")
subroutine(0xA644, "find_station_bit2",
    title="Find printer server station in table (bit 2)",
    description="Scans the 16-entry station table for a slot\n"
    "matching the current station/network address\n"
    "with bit 2 set (printer server active). Sets V\n"
    "if found, clears V if not. Falls through to\n"
    "allocate or update the matching slot with the\n"
    "new station address and status flags.",
    on_entry={"&0E00, &0E01": "station, network address to look up",
              "fs_work_6, fs_work_7": "current PS station/network for "
              "fall-through update"},
    on_exit={"v flag": "set if matching slot already had bit 2; clear if "
             "newly allocated",
             "x": "table slot index of the matched/allocated entry"})
subroutine(0xA66F, "find_station_bit3",
    title="Find file server station in table (bit 3)",
    description="Scans the 16-entry station table for a slot\n"
    "matching the current station/network address\n"
    "with bit 3 set (file server active). Sets V\n"
    "if found, clears V if not. Falls through to\n"
    "allocate or update the matching slot with the\n"
    "new station address and status flags.",
    on_entry={"&0E00, &0E01": "FS station, network to look up"},
    on_exit={"v flag": "set if matching slot already had bit 3; clear if "
             "newly allocated",
             "x": "table slot index of the matched/allocated entry"})
subroutine(0xA6A6, "flip_set_station_boot",
    title="Set boot option for a station in the table",
    description="Scans up to 16 station table entries for one\n"
    "matching the current address with bit 4 set\n"
    "(boot-eligible). Stores the requested boot type\n"
    "in the matching entry and calls\n"
    "restore_fs_context to re-establish the filing\n"
    "system state.",
    on_entry={"a": "boot type code to store",
              "&0E00, &0E01": "station, network whose boot entry to update"},
    on_exit={"FS context": "restored from saved workspace via "
             "restore_fs_context",
             "a, x, y": "clobbered"})
subroutine(0xA864, "osword_setup_handler",
    title="Push OSWORD handler address for RTS dispatch",
    description="Indexes the OSWORD dispatch table by X to\n"
    "push a handler address (hi then lo) onto the\n"
    "stack. Copies 3 bytes from the osword_flag\n"
    "workspace into the RX buffer, loads PB byte 0\n"
    "(the OSWORD sub-code), and clears svc_state.\n"
    "The subsequent RTS dispatches to the pushed\n"
    "handler address.",
    on_entry={"x": "OSWORD handler index (0-6)"})
subroutine(0xA901, "bin_to_bcd",
    title="Convert binary byte to BCD",
    description="Uses decimal mode (SED) with a count-up loop:\n"
    "starts at BCD 0 and adds 1 in decimal mode for\n"
    "each decrement of the binary input. Saves and\n"
    "restores the processor flags to avoid leaving\n"
    "decimal mode active. Called 6 times by\n"
    "save_txcb_and_convert for clock date/time\n"
    "conversion.",
    on_entry={"a": "binary value (0-99)"},
    on_exit={"a": "BCD equivalent"})
subroutine(0xAC67, "store_osword_pb_ptr",
    title="Store workspace pointer+1 to NFS workspace",
    description="Computes ws_ptr_hi + 1 and stores the resulting\n"
    "16-bit address at workspace offset &1C via\n"
    "store_ptr_at_ws_y. Then reads PB byte 1 (the\n"
    "transfer length) and adds ws_ptr_hi to compute\n"
    "the buffer end pointer, stored at workspace\n"
    "offset &20.",
    on_entry={"ws_ptr_hi (workspace ptr lo/hi)":
              "OSWORD parameter block pointer",
              "PB[1]": "transfer length (used to compute end pointer)"},
    on_exit={"NFS workspace +&1C, +&1D": "PB pointer + 1 "
             "(skips the sub-function-code byte)",
             "NFS workspace +&20, +&21": "PB pointer + PB[1] "
             "(end-of-buffer pointer)"})
subroutine(0xACAD, "store_ptr_at_ws_y",
    title="Store 16-bit pointer at workspace offset Y",
    description="Writes a 16-bit address to (nfs_workspace)+Y.\n"
    "The low byte comes from A; the high byte is\n"
    "computed from table_idx plus carry,\n"
    "supporting pointer arithmetic across page\n"
    "boundaries.",
    on_entry={"a": "pointer low byte",
              "y": "workspace offset",
              "c": "carry for high byte addition"})
subroutine(0xAA82, "copy_pb_byte_to_ws",
    title="Conditionally copy parameter block byte to workspace",
    description="If carry is set, loads a byte from the OSWORD\n"
    "parameter block at offset Y; if clear, uses\n"
    "the value already in A. Stores the result to\n"
    "workspace at the current offset. Decrements X\n"
    "and loops until the requested byte count is\n"
    "transferred.",
    on_entry={"c": "set to load from PB, clear to use A",
              "x": "byte count",
              "y": "PB source offset"})
# Located in 4.21_v1 at &A9CC (was &A660 in 4.18). Identified via the
# OSWORD &13 dispatch lo/hi table at &A9A8/&A9BA (sub 0: lo=CB,
# hi=A9 -> +1 = &A9CC). Like sub 1, the prologue calls sub_c8b4d for
# the FS-active check before the body.
entry(0xA9CC)
subroutine(0xA9CC, "osword_13_read_station",
    title="OSWORD &13 sub 0: read file server station",
    description="Returns the current file server station and\n"
    "network numbers in PB[1..2]. If the NFS is not\n"
    "active, sub_c8b4d returns early with zero in\n"
    "PB[0] (carrying over the 4.18 semantics).",
    on_entry={"ws_ptr_hi (workspace ptr)": "OSWORD parameter block pointer "
              "(set up by osword_13_dispatch via store_osword_pb_ptr)"},
    on_exit={"PB[0]": "0 if NFS not active",
             "PB[1]": "FS station number",
             "PB[2]": "FS network number",
             "behaviour": "in 4.21, ensure_fs_selected auto-selects ANFS "
             "rather than aborting on inactive FS"})
# Located in 4.21_v1 at &A9DA (was &A673 in 4.18). Reached via the
# OSWORD &13 sub-1 dispatch entry in the lo/hi table at &A9A8/&A9BA
# (lo=D9, hi=A9 -> +1 = &A9DA). 4.18 had the FS-active check
# (BIT &0D6C / BPL) inline; 4.21 factors it out into sub_c8b4d
# (BIT fs_flags / BMI) called from the prologue at &A9DA, with the
# body of the actual handler beginning at &A9DD.
entry(0xA9DA)
subroutine(0xA9DA, "osword_13_set_station",
    title="OSWORD &13 sub 1: set file server station",
    description="Sets the file server station and network numbers\n"
    "from PB[1..2]. The prologue at &A9DA calls\n"
    "sub_c8b4d to verify the FS is active, then the\n"
    "body at &A9DD processes all FCBs and scans the\n"
    "16-entry FCB table to reassign handles matching\n"
    "the new station.",
    on_entry={"PB[1]": "new FS station number",
              "PB[2]": "new FS network number"},
    on_exit={"&0E00, &0E01": "updated FS station/network",
             "FCB table at l1060": "handles reassigned to new station",
             "behaviour": "in 4.21, ensure_fs_selected auto-selects ANFS "
             "if not already active"})
label(0xA9DD, "osword_13_set_station_body")

# Shared FS-selection prologue used by OSWORD &13 sub-handlers. 4.18
# inlined `BIT &0D6C / BPL <return>` (abort if FS not active); 4.21
# factors that into ensure_fs_selected with INVERTED behaviour:
# instead of aborting, it AUTOMATICALLY SELECTS the FS by calling
# cmd_net_fs, raising 'net checksum' error only if selection fails.
# 5 callers: &A9CC (read_station), &A9DA (set_station), &AAC2
# (read_handles), &AAD0 (set_handles), &AC4C (?).
subroutine(0x8B4D, "ensure_fs_selected",
    title="Ensure ANFS is the active filing system",
    description="If bit 7 of fs_flags is set (FS already active),\n"
    "RTS via return_from_save_text_ptr. Otherwise calls\n"
    "cmd_net_fs to select the FS now; on failure JMPs to\n"
    "error_net_checksum to raise the 'net checksum'\n"
    "error. After successful selection, falls through to\n"
    "the body at &8B5A which sets up the OSWORD parameter\n"
    "block pointer and continues the caller's work.\n"
    "\n"
    "Behaviour change from 4.18: inline `BIT &0D6C / BPL`\n"
    "in 4.18 OSWORD handlers ABORTED when FS was inactive\n"
    "(returning zero in PB[0]); 4.21 instead auto-selects.")
subroutine(0xAA72, "osword_13_read_csd",
    title="OSWORD &13 sub 12: read CSD path",
    description="Reads 5 current selected directory path bytes\n"
    "from the RX workspace at offset &17 into\n"
    "PB[1..5]. Sets carry clear to select the\n"
    "workspace-to-PB copy direction.",
    on_exit={"PB[1..5]": "5-byte CSD path from RX workspace +&17"})
subroutine(0xAA75, "osword_13_write_csd",
    title="OSWORD &13 sub 13: write CSD path",
    description="Writes 5 current selected directory path bytes\n"
    "from PB[1..5] into the RX workspace at offset\n"
    "&17. Sets carry to select the PB-to-workspace\n"
    "copy direction.",
    on_entry={"PB[1..5]": "5-byte CSD path to install"},
    on_exit={"RX workspace +&17..+&1B": "= PB[1..5]"})
subroutine(0xAA91, "osword_13_read_ws_pair",
    title="OSWORD &13 sub 2: read workspace byte pair",
    description="Reads 2 bytes from the NFS workspace page\n"
    "starting at offset 1 into PB[1..2]. Uses\n"
    "nfs_workspace_hi as the page and\n"
    "copy_pb_byte_to_ws with carry clear for the\n"
    "workspace-to-PB direction.",
    on_exit={"PB[1..2]": "2 bytes from NFS workspace +1..+2"})
subroutine(0xAA9D, "osword_13_write_ws_pair",
    title="OSWORD &13 sub 3: write workspace byte pair",
    description="Writes 2 bytes from PB[1..2] into the NFS\n"
    "workspace at offsets 2 and 3. Then calls\n"
    "init_bridge_poll and conditionally clears\n"
    "the workspace byte if the bridge status\n"
    "changed.",
    on_entry={"PB[1..2]": "2 bytes to write to NFS workspace"},
    on_exit={"NFS workspace +2..+3": "= PB[1..2]",
             "bridge poll table": "refreshed via init_bridge_poll"})
subroutine(0xAAB2, "osword_13_read_prot",
    title="OSWORD &13 sub 4: read protection mask",
    description="Returns the current protection mask (ws_0d68)\n"
    "in PB[1].",
    on_exit={"PB[1]": "current immediate-op protection mask (ws_0d68)"})
subroutine(0xAAB8, "osword_13_write_prot",
    title="OSWORD &13 sub 5: write protection mask",
    description="Sets the protection mask from PB[1] via\n"
    "store_prot_mask.",
    on_entry={"PB[1]": "new immediate-op protection mask"},
    on_exit={"ws_0d68, ws_0d69": "updated to PB[1]"})
# Located in 4.21_v1 at &AAC2 (was &A734 in 4.18). OSWORD &13 sub 6
# from the dispatch table (lo=C1, hi=AA -> +1 = &AAC2). FS-active
# check via sub_c8b4d in prologue.
entry(0xAAC2)
subroutine(0xAAC2, "osword_13_read_handles",
    title="OSWORD &13 sub 6: read FCB handle info",
    description="Returns the 3-byte FCB handle/port data from\n"
    "the workspace at C271[1..3] (was l1071[1..3] in\n"
    "4.18) into PB[1..3]. If the NFS is not active,\n"
    "returns zero in PB[0] via the sub_c8b4d prologue.",
    on_exit={"PB[1..3]": "3 bytes from fs_lib_flags+1..+3 (C271+1..+3)",
             "PB[0]": "0 if NFS not active (auto-selected in 4.21)"})
# Located in 4.21_v1 at &AAD0 (was &A744 in 4.18). OSWORD &13 sub 7
# from the dispatch table (lo=CF, hi=AA -> +1 = &AAD0).
entry(0xAAD0)
subroutine(0xAAD0, "osword_13_set_handles",
    title="OSWORD &13 sub 7: set FCB handles",
    description="Validates and assigns up to 3 FCB handles\n"
    "from PB[1..3]. Each handle value (&20-&2F)\n"
    "indexes the channel tables. For valid handles\n"
    "with the appropriate flag bit, stores the\n"
    "station and FCB index, then updates flag bits\n"
    "across all FCB entries via update_fcb_flag_bits.",
    on_entry={"PB[1..3]": "three new FCB handle values (&20-&2F)"},
    on_exit={"FCB table at l1060": "flag bits updated to reflect new "
             "handle assignments",
             "behaviour": "in 4.21, ensure_fs_selected auto-selects "
             "ANFS if not active"})
subroutine(0xAB43, "update_fcb_flag_bits",
    title="Update FCB flag bits across all entries",
    description="Scans all 16 FCB entries in l1060. For each\n"
    "entry with bit 6 set, tests the Y-specified\n"
    "bit mask: if matching, ORs bit 5 into the\n"
    "flags; if not, leaves bit 5 clear. In both\n"
    "cases, inverts and clears the tested bits.\n"
    "Preserves X.",
    on_entry={"y": "flag bit mask to test",
              "x": "current FCB index (preserved)"})
subroutine(0xAB68, "osword_13_read_rx_flag",
    title="OSWORD &13 sub 8: read RX control block flag",
    description="Returns byte 1 of the current RX control\n"
    "block in PB[1].",
    on_exit={"PB[1]": "RXCB[1] (current open-receive flags)"})
subroutine(0xAB71, "osword_13_read_rx_port",
    title="OSWORD &13 sub 9: read RX port byte",
    description="Returns byte &7F of the current RX control\n"
    "block in PB[1], and stores &80 in PB[2].",
    on_exit={"PB[1]": "RXCB byte at &7F",
             "PB[2]": "&80 (sentinel)"})
subroutine(0xAB7F, "osword_13_read_error",
    title="OSWORD &13 sub 10: read error flag",
    description="Returns the error flag (l0e09) in PB[1].",
    on_exit={"PB[1]": "last error code stored in l0e09"})
subroutine(0xAB82, "store_a_to_pb_1",
    title="Store A to OSWORD parameter block at offset 1",
    description="Increments Y to 1 and stores A into the\n"
    "OSWORD parameter block via (ws_ptr_hi),Y.\n"
    "Used by OSWORD 13 sub-handlers to return a\n"
    "single result byte.",
    on_entry={"A": "value to store"},
    on_exit={"Y": "1"})
subroutine(0xAB86, "osword_13_read_context",
    title="OSWORD &13 sub 11: read context byte",
    description="Returns the context byte (l0d6d) in PB[1].",
    on_exit={"PB[1]": "current context byte from l0d6d"})
subroutine(0xAB8B, "osword_13_read_free_bufs",
    title="OSWORD &13 sub 14: read printer buffer free space",
    description="Returns the number of free bytes remaining in\n"
    "the printer spool buffer (&6F minus spool_buf_idx)\n"
    "in PB[1]. The buffer starts at offset &25 and can\n"
    "hold up to &4A bytes of spool data.",
    on_exit={"PB[1]": "free bytes in printer spool buffer "
             "(&6F minus spool_buf_idx)"})
subroutine(0xAB93, "osword_13_read_ctx_3",
    title="OSWORD &13 sub 15: read retry counts",
    description="Returns the three retry count values in\n"
    "PB[1..3]: PB[1] = transmit retry count\n"
    "(default &FF = 255), PB[2] = receive poll\n"
    "count (default &28 = 40), PB[3] = machine\n"
    "peek retry count (default &0A = 10). Setting\n"
    "transmit retries to 0 means retry forever.",
    on_exit={"PB[1]": "tx_retry_count (default &FF; 0 = retry forever)",
             "PB[2]": "rx_wait_timeout (default &28 = 40)",
             "PB[3]": "machine peek retry count (default &0A = 10)"})
subroutine(0xAB9E, "osword_13_write_ctx_3",
    title="OSWORD &13 sub 16: write retry counts",
    description="Sets the three retry count values from\n"
    "PB[1..3]: PB[1] = transmit retry count,\n"
    "PB[2] = receive poll count, PB[3] = machine\n"
    "peek retry count.",
    on_entry={"PB[1]": "new tx_retry_count (0 = retry forever)",
              "PB[2]": "new rx_wait_timeout",
              "PB[3]": "new machine peek retry count"})
subroutine(0xABA9, "osword_13_bridge_query",
    title="OSWORD &13 sub 17: query bridge status",
    description="Calls init_bridge_poll, then returns the\n"
    "bridge status. If l0d72 is &FF (no bridge),\n"
    "stores 0 in PB[0]. Otherwise stores l0d72\n"
    "in PB[1] and conditionally updates PB[3]\n"
    "based on station comparison.",
    on_exit={"PB[0]": "0 if no bridge present (l0d72 = &FF)",
             "PB[1]": "bridge station number when present",
             "PB[3]": "conditionally updated based on station match"})
subroutine(0xABE9, "init_bridge_poll",
    title="Initialise Econet bridge routing table",
    description="Checks the bridge status byte: if &FF\n"
    "(uninitialised), broadcasts a bridge query\n"
    "packet and polls for replies. Each reply\n"
    "adds a network routing entry to the bridge\n"
    "table. Skips the broadcast if the table has\n"
    "already been populated from a previous call.")
subroutine(0xACF8, "enable_irq_and_poll",
    title="Enable interrupts and send Econet packet",
    description="Executes CLI to re-enable interrupts, then\n"
    "falls through to send_net_packet. Used after\n"
    "a sequence that ran with interrupts disabled\n"
    "to ensure the packet is sent with normal\n"
    "interrupt handling active.",
    on_entry={"txcb at &00C0": "TX control block populated by caller",
              "i flag": "may be set (caller had IRQs off); CLI clears it"},
    on_exit={"i flag": "clear (interrupts enabled)",
             "behaviour": "tail-calls send_net_packet -- result depends on "
             "Econet TX outcome (may BRK on escape via "
             "check_escape_and_classify)"})
subroutine(0xACFC, "netv_handler",
    title="NETV handler: OSWORD dispatch",
    description="Installed as the NETV handler via\n"
    "write_vector_entry. Saves all registers, reads\n"
    "the OSWORD number from the stack, and dispatches\n"
    "OSWORDs 0-8 via push_osword_handler_addr. OSWORDs\n"
    ">= 9 are ignored (registers restored, RTS returns\n"
    "to MOS). Address stored at netv_handler_addr\n"
    "(&8E8A) in the extended vector data area.",
    on_entry={"a": "OSWORD number (read from stacked A on entry)",
              "x, y": "PB pointer low/high (per OSWORD calling convention)",
              "stack": "MOS-prepared NETV stack frame "
              "(P, A, ROM-bank-select, return address)"},
    on_exit={"a, x, y, p": "restored from stack",
             "behaviour": "OSWORDs >= 9 are passed through unchanged "
             "(MOS continues to next NETV ROM); OSWORDs 0-8 are dispatched "
             "to per-call handlers and may issue Econet TX/abort packets"})
subroutine(0xAD15, "push_osword_handler_addr",
    title="Push OSWORD handler address for RTS dispatch",
    description="Indexes the OSWORD handler dispatch table\n"
    "using the current OSWORD number to push the\n"
    "handler's address (hi/lo) onto the stack.\n"
    "Reloads the OSWORD number from osbyte_a_copy\n"
    "so the dispatched handler can identify the\n"
    "specific call.",
    on_entry={"a": "OSWORD number (0-8) -- table index",
              "osbyte_a_copy": "saved OSWORD number for handler reload"},
    on_exit={"stack": "(handler-1) hi byte then lo byte pushed; caller's "
             "subsequent RTS lands on the handler",
             "a": "OSWORD number (re-loaded for the handler's use)"})
# UNMAPPED: subroutine(0xA9B0, "osword_4_handler",
# UNMAPPED:     title="OSWORD 4 handler: clear carry and send abort",
# UNMAPPED:     description="Clears the carry flag in the stacked processor\n"
# UNMAPPED:     "status, stores the original Y to workspace at\n"
# UNMAPPED:     "offset &DA, and falls through to tx_econet_abort\n"
# UNMAPPED:     "with A=0. Called via OSWORD handler dispatch\n"
# UNMAPPED:     "table for OSWORD 4 (write interval timer).")
subroutine(0xAD40, "tx_econet_abort",
    title="Send Econet abort/disconnect packet",
    description="Stores the abort code in workspace, configures\n"
    "the TX control block with control byte &80\n"
    "(immediate operation flag), and transmits the\n"
    "abort packet. Used to cleanly disconnect from\n"
    "a remote station during error recovery.",
    on_entry={"a": "abort code (stored in workspace before TX)",
              "&0E00, &0E01": "destination station, network"},
    on_exit={"behaviour": "Econet abort packet sent; this is a "
             "fire-and-forget packet (no reply expected); caller "
             "typically returns to MOS via NETV"})
subroutine(0xAD64, "netv_claim_release",
    title="OSWORD 7 handler: claim/release network resources",
    description="Handles OSWORD 7 (SOUND) intercepted via NETV.\n"
    "Searches the claim code table in two passes:\n"
    "first 11 entries (state 2), then all 18 (state\n"
    "3). On match, saves 3 tube state bytes to\n"
    "workspace and sends an abort with the state\n"
    "code. For state 3 matches, also polls workspace\n"
    "for a response and restores the caller's stack\n"
    "frame from the saved bytes.")
subroutine(0xADB8, "match_rx_code",
    title="Search receive code table for match",
    description="Scans a table of receive operation codes\n"
    "starting at index X, comparing each against A.\n"
    "Returns with Z set if a match is found, Z clear\n"
    "if the end-of-table marker is reached.",
    on_entry={"a": "receive code to match",
              "x": "starting table index"},
    on_exit={"z": "set if match found"})
subroutine(0xADD3, "osword_8_handler",
    title="OSWORD 7/8 handler: copy PB to workspace and abort",
    description="Handles OSWORD 7 or 8 by copying 15 bytes from\n"
    "the parameter block to workspace at offset &DB,\n"
    "storing the OSWORD number at offset &DA, setting\n"
    "control value &E9, and sending an abort packet.\n"
    "Returns via tx_econet_abort. Rejects other\n"
    "OSWORD numbers by returning immediately.",
    on_entry={"a": "OSWORD number (must be 7 or 8 to be processed)",
              "PB pointer (X/Y or workspace ptr)":
              "OSWORD parameter block (15 bytes copied to workspace +&DB)"},
    on_exit={"NFS workspace +&DA": "= OSWORD number",
             "NFS workspace +&DB..+&E9": "= 15 bytes copied from PB",
             "behaviour": "abort packet sent via tx_econet_abort with "
             "control = &E9; OSWORD numbers other than 7/8 return "
             "immediately with no side effect"})
subroutine(0xADFE, "init_ws_copy_wide",
    title="Initialise workspace copy in wide mode (14 bytes)",
    description="Copies 14 bytes to workspace offset &7C.\n"
    "Falls through to the template-driven copy\n"
    "loop which handles &FD (skip), &FE (end),\n"
    "and &FC (page pointer) markers.",
    on_entry={"x": "template source offset (within ws_txcb_template_data)"},
    on_exit={"NFS workspace +&7C..": "14 bytes from template (with "
             "&FC -> workspace page pointer substitution applied)"})
subroutine(0xAE07, "init_ws_copy_narrow",
    title="Initialise workspace copy in narrow mode (27 bytes)",
    description="Sets up a 27-byte copy to workspace offset &17,\n"
    "then falls through to ws_copy_vclr_entry for\n"
    "the template-driven copy loop. Used for the\n"
    "compact workspace initialisation variant.",
    on_entry={"x": "template source offset"},
    on_exit={"NFS workspace +&17..": "27 bytes from template (with "
             "marker substitution applied)"})
subroutine(0xAE0B, "ws_copy_vclr_entry",
    title="Template-driven workspace copy with V clear",
    description="Processes a template byte array to initialise\n"
    "workspace. Special marker bytes: &FE terminates\n"
    "the copy, &FD skips the current offset, and &FC\n"
    "substitutes the workspace page pointer. All\n"
    "other values are stored directly to the\n"
    "workspace at the current offset.",
    on_entry={"x": "template source offset",
              "y": "destination offset within NFS workspace",
              "v flag": "clear (controls a downstream branch in the "
              "shared body; init_ws_copy_wide / _narrow enter with V=0)"},
    on_exit={"NFS workspace at +Y..": "template data copied with marker "
             "expansion (&FC -> page pointer; &FD skip; &FE end)",
             "a, x, y": "clobbered"})
subroutine(0xAE5A, "netv_spool_check",
    title="OSWORD 5 handler: check spool PB and reset buffer",
    description="Handles OSWORD 5 intercepted via NETV. Checks\n"
    "if X-1 matches osword_pb_ptr and bit 0 of\n"
    "&00D0 is clear. If both conditions are met,\n"
    "falls through to reset_spool_buf_state to\n"
    "reinitialise the spool buffer for new data.")
subroutine(0xAE6F, "netv_print_data",
    title="OSWORD 1-3 handler: drain printer buffer",
    description="Handles OSWORDs 1-3 intercepted via NETV.\n"
    "When X=1, drains the printer buffer (OSBYTE\n"
    "&91, buffer 3) into the receive buffer, sending\n"
    "packets via process_spool_data when the buffer\n"
    "exceeds &6E bytes. When X>1, routes to\n"
    "handle_spool_ctrl_byte for spool state control.")
subroutine(0xAE64, "reset_spool_buf_state",
    title="Reset spool buffer to initial state",
    description="Sets the spool buffer pointer to &25 (first\n"
    "available data position) and the control state\n"
    "byte to &41 (ready for new data). Called after\n"
    "processing a complete spool data block.")
subroutine(0xAE94, "append_byte_to_rxbuf",
    title="Append byte to receive buffer",
    description="Stores A in the receive buffer at the current\n"
    "buffer index (ws_ptr_lo), then increments the\n"
    "index. Used to accumulate incoming spool data\n"
    "bytes before processing.",
    on_entry={"a": "byte to append"})
subroutine(0xAE9D, "handle_spool_ctrl_byte",
    title="Handle spool control byte and flush buffer",
    description="Rotates bit 0 of the control byte into carry\n"
    "for mode selection (print vs spool), appends\n"
    "the byte to the buffer, calls process_spool_data\n"
    "to transmit the accumulated data, and resets\n"
    "the buffer state ready for the next block.")
subroutine(0xAEB8, "process_spool_data",
    title="Transmit accumulated spool buffer data",
    description="Copies the workspace state to the TX control\n"
    "block, sends a disconnect reply if the previous\n"
    "transfer requires acknowledgment, then handles\n"
    "the spool output sequence by setting up and\n"
    "sending the pass-through TX buffer.")
subroutine(0xAFA6, "send_disconnect_reply",
    title="Send Econet disconnect reply packet",
    description="Sets up the TX pointer, copies station\n"
    "addresses, matches the station in the table,\n"
    "and sends the response. Waits for\n"
    "acknowledgment before returning.")
subroutine(0xB05F, "commit_state_byte",
    title="Copy current state byte to committed state",
    description="Reads the working state byte from workspace and\n"
    "stores it to the committed state location. Used\n"
    "to finalise a state transition after all related\n"
    "workspace fields have been updated.")
subroutine(0xB066, "serialise_palette_entry",
    title="Serialise palette register to workspace",
    description="Reads the current logical colour for a palette\n"
    "register via OSBYTE &0B and stores both the\n"
    "palette value and the display mode information\n"
    "in the workspace block. Used during remote\n"
    "screen state capture.")
subroutine(0xB081, "read_osbyte_to_ws_x0",
    title="Read OSBYTE with X=0 and store to workspace",
    description="Sets X=0 then falls through to read_osbyte_to_ws\n"
    "to issue the OSBYTE call and store the result.\n"
    "Used when the OSBYTE parameter X must be zero.")
subroutine(0xB083, "read_osbyte_to_ws",
    title="Issue OSBYTE from table and store result",
    description="Loads the OSBYTE function code from the next\n"
    "entry in the OSBYTE table, issues the call, and\n"
    "stores the Y result in workspace at the current\n"
    "offset. Advances the table pointer for the next\n"
    "call.")

# --- cmd_ex subroutines ---

subroutine(0xB21A, "print_10_chars",
    title="Print 10 characters from reply buffer",
    description="Sets Y=10 and falls through to\n"
    "print_chars_from_buf. Used by cmd_ex to print\n"
    "fixed-width directory title, directory name, and\n"
    "library name fields.",
    on_entry={"x": "buffer offset to start printing from"})
subroutine(0xB21C, "print_chars_from_buf",
    title="Print Y characters from buffer via OSASCI",
    description="Loops Y times, loading each byte from l0f05+X\n"
    "and printing it via OSASCI. Advances X after\n"
    "each character, leaving X pointing past the\n"
    "last printed byte.",
    on_entry={"x": "buffer offset", "y": "character count"})
subroutine(0xB22A, "parse_cmd_arg_y0",
    title="Parse command argument from offset zero",
    description="Sets Y=0 and falls through to parse_filename_arg\n"
    "for GSREAD-based filename parsing with prefix\n"
    "character handling.",
    on_exit={"y": "advanced past the parsed argument",
             "&C030 (parse buffer)": "the parsed (and prefix-stripped) "
             "filename, CR-terminated"})
subroutine(0xB22C, "parse_filename_arg",
    title="Parse filename via GSREAD with prefix handling",
    description="Calls gsread_to_buf to read the command line\n"
    "string into the &0E30 buffer, then falls through\n"
    "to parse_access_prefix to process '&', ':', '.',\n"
    "and '#' prefix characters.",
    on_entry={"y": "current command-line offset (consumed by gsread_to_buf)"},
    on_exit={"y": "advanced past the parsed argument",
             "&C030 (parse buffer)": "the parsed filename, CR-terminated; "
             "fs_lib_flags updated for '&'/':' prefix handling"})
subroutine(0xB22F, "parse_access_prefix",
    title="Parse access and FS selection prefix characters",
    description="Examines the first character(s) of the parsed\n"
    "buffer at &0E30 for prefix characters: '&' sets\n"
    "the FS selection flag (bit 6 of l1071) and strips\n"
    "the prefix, ':' with '.' also triggers FS\n"
    "selection, '#' is accepted as a channel prefix.\n"
    "Raises 'Bad file name' for invalid combinations\n"
    "like '&.' followed by CR.")
subroutine(0xB251, "strip_token_prefix",
    title="Strip first character from parsed token buffer",
    description="Shifts all bytes in the &C030 buffer left by\n"
    "one position (removing the first character),\n"
    "then trims any trailing spaces by replacing\n"
    "them with CR terminators. Used after consuming\n"
    "a prefix character like '&' or ':'.",
    on_entry={"&C030 (parse buffer)":
              "first byte will be discarded; buffer is CR-terminated"},
    on_exit={"x": "preserved (saved/restored via PHA/PLA)",
             "a": "clobbered",
             "&C030 (parse buffer)": "shifted left by one byte; "
             "any trailing spaces replaced by CR"})
subroutine(0xB29F, "copy_arg_to_buf_x0",
    title="Copy argument to TX buffer from offset zero",
    description="Sets X=0 and falls through to copy_arg_to_buf\n"
    "then copy_arg_validated. Provides the simplest\n"
    "entry point for copying a single parsed argument\n"
    "into the TX buffer at position zero.",
    on_entry={"fs_crc_lo, fs_crc_hi (&BE/&BF)":
              "command-line text pointer (already snapshot)"},
    on_exit={"x": "TX buffer offset just past the copied argument",
             "y": "advanced past the source argument",
             "TX buffer at &C105+0..": "argument bytes (CR-terminated)"})
subroutine(0xB2A1, "copy_arg_to_buf",
    title="Copy argument to TX buffer with Y=0",
    description="Sets Y=0 and falls through to copy_arg_validated\n"
    "with carry set, enabling '&' character validation.\n"
    "X must already contain the destination offset\n"
    "within the TX buffer.",
    on_entry={"x": "destination offset within the TX buffer"},
    on_exit={"x": "TX buffer offset just past the copied argument",
             "y": "advanced past the source argument"})
subroutine(0xB2A3, "copy_arg_validated",
    title="Copy command line characters to TX buffer",
    description="Copies characters from (fs_crc_lo)+Y to l0f05+X\n"
    "until a CR terminator is reached. With carry set,\n"
    "validates each character against '&' — raising\n"
    "'Bad file name' if found — to prevent FS selector\n"
    "characters from being embedded in filenames.",
    on_entry={"x": "TX buffer destination offset",
              "y": "command line source offset",
              "c": "set to enable '&' validation"})
label(0xB2C8, "done_trim_spaces")
# Located in 4.21_v1 at &B2CF (was &AF32 in 4.18). Same 4-instruction
# body (LDA / AND #&1F / STA / RTS); only the workspace address moved
# from &1071 to &C271 with the rest of fs_lib_flags. Already classified
# as code (sub_cb2cf with 12 callers).
subroutine(0xB2CF, "mask_owner_access",
    title="Clear FS selection flags from options word",
    description="ANDs the &C271 flags byte (was &1071 in 4.18) with\n"
    "&1F, clearing the FS selection flag (bit 6) and\n"
    "other high bits to retain only the 5-bit owner\n"
    "access mask. Called before parsing to reset the\n"
    "prefix state from a previous command. 12 callers.")
subroutine(0xB2E4, "ex_print_col_sep",
    title="Print column separator or newline for *Ex/*Cat",
    description="In *Cat mode, increments a column counter modulo 4\n"
    "and prints a two-space separator between entries,\n"
    "with a newline at the end of each row. In *Ex\n"
    "mode (fs_spool_handle negative), prints a newline\n"
    "after every entry. Scans the entry data and loops\n"
    "back to print the next entry's characters.")

# --- cmd_remove subroutines ---

subroutine(0xB327, "print_num_no_leading",
    title="Print decimal number with leading zero suppression",
    description="Sets V via BIT bit_test_ff to enable leading\n"
    "zero suppression, then falls through to\n"
    "print_decimal_3dig. Used by print_station_id\n"
    "for compact station number display.",
    on_entry={"a": "number to print (0-255)"})
subroutine(0xB32A, "print_decimal_3dig",
    title="Print byte as 3-digit decimal via OSASCI",
    description="Extracts hundreds, tens and units digits by\n"
    "successive calls to print_decimal_digit. The V\n"
    "flag controls leading zero suppression: if set,\n"
    "zero digits are skipped until a non-zero digit\n"
    "appears. V is always cleared before the units\n"
    "digit to ensure at least one digit is printed.",
    on_entry={"a": "number to print (0-255)",
              "v": "set to suppress leading zeros"})
subroutine(0xB338, "print_decimal_digit",
    title="Print one decimal digit by repeated subtraction",
    description="Initialises X to '0'-1 and loops, incrementing X\n"
    "while subtracting the divisor from Y. On underflow,\n"
    "adds back the divisor to get the remainder in Y.\n"
    "If V is set, suppresses leading zeros by skipping\n"
    "the OSASCI call when the digit is '0'.",
    on_entry={"a": "divisor", "y": "value to divide"},
    on_exit={"y": "remainder after division"})
subroutine(0xB373, "save_ptr_to_os_text",
    title="Copy text pointer to OS text pointer workspace",
    description="Saves fs_crc_lo/hi into the MOS text pointer\n"
    "locations at &00F2/&00F3. Preserves A on the\n"
    "stack. Called before GSINIT/GSREAD sequences\n"
    "that need to parse from the current command\n"
    "line position.",
    on_entry={"fs_crc_lo, fs_crc_hi (&BE/&BF)":
              "current command-line text pointer to publish"},
    on_exit={"a": "preserved (PHA/PLA)",
             "os_text_ptr (&F2/&F3)": "= fs_crc_lo, fs_crc_hi on entry"})
subroutine(0xB37F, "skip_to_next_arg",
    title="Advance past spaces to the next command argument",
    description="Scans (fs_crc_lo)+Y for space characters,\n"
    "advancing Y past each one. Returns with A\n"
    "holding the first non-space character, or CR\n"
    "if the end of line is reached. Used by *CDir\n"
    "and *Remove to detect extra arguments.",
    on_entry={"fs_crc_lo, fs_crc_hi (&BE/&BF)":
              "command-line text pointer base",
              "y": "starting offset (where to begin scanning)"},
    on_exit={"a": "first non-space character or CR",
             "y": "offset of that character"})
subroutine(0xB393, "save_ptr_to_spool_buf",
    title="Copy text pointer to spool buffer pointer",
    description="Saves fs_crc_lo/hi into fs_options/fs_block_offset\n"
    "for use as the spool buffer pointer. Preserves A\n"
    "on the stack. Called by *PS and *PollPS before\n"
    "parsing their arguments.",
    on_entry={"fs_crc_lo, fs_crc_hi (&BE/&BF)":
              "command-line text pointer to publish as spool buf pointer"},
    on_exit={"a": "preserved (PHA/PLA)",
             "fs_options, fs_block_offset (&BB/&BC)":
             "= fs_crc_lo, fs_crc_hi on entry"})
subroutine(0xB39E, "init_spool_drive",
    title="Initialise spool drive page pointers",
    description="Calls get_ws_page to read the workspace page\n"
    "number for the current ROM slot, stores it as\n"
    "the spool drive page high byte (l00af), and\n"
    "clears the low byte (l00ae) to zero. Preserves\n"
    "Y on the stack.",
    on_entry={"romsel_copy (&F4)":
              "ROM slot (consumed by get_ws_page)"},
    on_exit={"a": "0",
             "y": "preserved (PHY/PLY)",
             "l00ae, l00af": "&00, ws_page -- page-aligned spool drive ptr"})

# --- cmd_ps subroutines ---

subroutine(0xB3D5, "copy_ps_data_y1c",
    title="Copy printer server template at offset &18",
    description="Sets Y=&18 and falls through to copy_ps_data.\n"
    "Called during workspace initialisation\n"
    "(svc_2_private_workspace) to set up the printer\n"
    "server template at the standard offset.")
subroutine(0xB3D7, "copy_ps_data",
    title="Copy 8-byte printer server template to RX buffer",
    description="Copies 8 bytes of default printer server data\n"
    "into the RX buffer at the current Y offset.\n"
    "Uses indexed addressing: LDA ps_template_base,X\n"
    "with X starting at &F8, so the effective read\n"
    "address is ps_template_base+&F8 = ps_template_data\n"
    "(&8E59). This 6502 trick reaches data 248 bytes\n"
    "past the base label using a single instruction.")
label(0xB441, "read_ps_station_addr")
# UNMAPPED: label(0xB0B9, "store_ps_station_addr")
subroutine(0xB483, "print_file_server_is",
    title="Print 'File server ' prefix",
    description="Uses print_inline to output 'File' then falls through\n"
    "to the shared ' server is ' suffix at\n"
    "print_printer_server_is.",
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)",
             "side effect": "writes 'File server is ' to current output stream"})
subroutine(0xB48D, "print_printer_server_is",
    title="Print 'Printer server is ' prefix",
    description="Uses print_inline to output the full label\n"
    "'Printer server is ' with trailing space.",
    on_exit={"a, x, y": "clobbered (OSASCI via print_inline)",
             "side effect": "writes 'Printer server is ' to current output stream"})
subroutine(0xB4A8, "load_ps_server_addr",
    title="Load printer server address from workspace",
    description="Reads the station and network bytes from workspace\n"
    "offsets 2 and 3 into the station/network variables.",
    on_entry={"nfs_workspace": "page-aligned NFS workspace pointer "
              "(offsets 2/3 hold the saved PS address)"},
    on_exit={"&0E00, &0E01": "PS station, network",
             "a, y": "clobbered"})
subroutine(0xB4B4, "pop_requeue_ps_scan",
    title="Pop return address and requeue PS slot scan",
    description="Converts the PS slot flags to a workspace index,\n"
    "writes slot data, and jumps back into the PS scan\n"
    "loop to continue processing.")
subroutine(0xB51C, "write_ps_slot_byte_ff",
    title="Write buffer page byte and two &FF markers",
    description="Stores the buffer page byte at the current Y offset\n"
    "in workspace, followed by two &FF sentinel bytes.\n"
    "Advances Y after each write.",
    on_entry={"a": "buffer page byte to store at workspace+Y",
              "y": "starting workspace offset"},
    on_exit={"a": "&FF (the sentinel value left in A)",
             "y": "workspace offset advanced by 3 (one byte + two markers)"})
subroutine(0xB523, "write_two_bytes_inc_y",
    title="Write A to two consecutive workspace bytes",
    description="Stores A at the current Y offset via (nfs_workspace),Y\n"
    "then again at Y+1, advancing Y after each write.",
    on_entry={"a": "byte to store", "y": "workspace offset"})
subroutine(0xB52B, "reverse_ps_name_to_tx",
    title="Reverse-copy printer server name to TX buffer",
    description="Copies 8 bytes from the RX buffer (offsets &1C-&23)\n"
    "to the TX buffer (offsets &13-&1B) in reversed byte\n"
    "order, pushing onto the stack then popping back.",
    on_entry={"RX buffer at +&1C..+&23":
              "8-byte printer server name from server reply"},
    on_exit={"TX buffer at +&13..+&1B":
             "8-byte name in reverse byte order",
             "a, x, y": "clobbered"})
subroutine(0xB556, "print_station_addr",
    title="Print station address as decimal net.station",
    description="If the network number is zero, prints only the\n"
    "station number. Otherwise prints network.station\n"
    "separated by a dot. V flag controls padding with\n"
    "leading spaces for column alignment.",
    on_entry={"fs_work_6 (&B6)": "network number (0 = local, no 'NN.' printed)",
              "fs_work_7 (&B7)": "station number (printed as 3-digit decimal)",
              "v flag": "set = no leading-space padding; "
              "clear = pad to align in a column"},
    on_exit={"a, x, y": "clobbered (print_decimal_3dig and OSASCI)",
             "side effect": "writes 'NNN.SSS' or 'SSS' to current output"})

# --- cmd_pollps subroutines ---

subroutine(0xB6A6, "init_ps_slot_from_rx",
    title="Initialise PS slot buffer from template data",
    description="Copies the 12-byte ps_slot_txcb_template (&B1B7)\n"
    "into workspace at offsets &78-&83 via indexed\n"
    "addressing from write_ps_slot_link_addr (write_ps_slot_hi_link+1).\n"
    "Substitutes net_rx_ptr_hi at offsets &7D and &81\n"
    "(the hi bytes of the two buffer pointers) so they\n"
    "point into the current RX buffer page.")
subroutine(0xB6BD, "store_char_uppercase",
    title="Convert to uppercase and store in RX buffer",
    description="If the character in A is lowercase (&61-&7A), converts\n"
    "to uppercase by clearing bit 5. Stores the result in\n"
    "the RX buffer at the current position, advances the\n"
    "buffer pointer, and decrements the character count.",
    on_entry={"a": "character to store"})

# --- cmd_wipe subroutines ---

subroutine(0xB7D3, "flush_and_read_char",
    title="Flush keyboard buffer and read one character",
    description="Calls OSBYTE &0F to flush the input buffer, then\n"
    "OSRDCH to read a single character. Raises an escape\n"
    "error if escape was pressed (carry set on return).",
    on_exit={"a": "character read from keyboard",
             "x, y": "clobbered (OSBYTE/OSRDCH)",
             "behaviour": "raises 'Escape' error if escape was pressed "
             "(OSRDCH returns C set)"})
# Removed in 4.18: unused_clear_ws_78 (dead code removed)
subroutine(0xB7E3, "init_channel_table",
    title="Initialise channel allocation table",
    description="Clears all 256 bytes of the table, then marks\n"
    "available channel slots based on the count from\n"
    "the receive buffer. Sets the first slot to &C0\n"
    "(active channel marker).")
subroutine(0xB805, "attr_to_chan_index",
    title="Convert channel attribute to table index",
    description="Subtracts &20 from the attribute byte and clamps\n"
    "to the range 0-&0F. Returns &FF if out of range.\n"
    "Preserves processor flags via PHP/PLP.",
    on_entry={"a": "channel attribute byte"},
    on_exit={"a": "table index (0-&0F) or &FF if invalid"})
subroutine(0xB814, "check_chan_char",
    title="Validate channel character and look up entry",
    description="Characters below '0' are looked up directly in\n"
    "the channel table. Characters '0' and above are\n"
    "converted to a table index via attr_to_chan_index.\n"
    "Raises 'Net channel' error if invalid.",
    on_entry={"a": "channel character"})
subroutine(0xB847, "lookup_chan_by_char",
    title="Look up channel by character code",
    description="Converts the character to a table index via\n"
    "attr_to_chan_index, checks the station/network\n"
    "match via match_station_net, and returns the\n"
    "channel flags in A.",
    on_entry={"a": "channel character"},
    on_exit={"a": "channel flags"})
subroutine(0xB886, "store_result_check_dir",
    title="Store channel attribute and check not directory",
    description="Writes the current channel attribute to the receive\n"
    "buffer, then tests the directory flag (bit 1). Raises\n"
    "'Is a dir.' error if the attribute refers to a\n"
    "directory rather than a file.")
subroutine(0xB88C, "check_not_dir",
    title="Validate channel is not a directory",
    description="Calls check_chan_char to validate the channel, then\n"
    "tests the directory flag (bit 1). Raises 'Is a dir.'\n"
    "error if the channel refers to a directory.")
subroutine(0xB8A8, "alloc_fcb_slot",
    title="Allocate a free file control block slot",
    description="Scans FCB slots &20-&2F for an empty entry.\n"
    "Returns Z=0 with X=slot index on success, or\n"
    "Z=1 with A=0 if all slots are occupied.",
    on_exit={"x": "slot index (if Z=0)", "z": "0=success, 1=no free slot"})
subroutine(0xB8DC, "alloc_fcb_or_error",
    title="Allocate FCB slot or raise error",
    description="Calls alloc_fcb_slot and raises 'No more FCBs'\n"
    "if no free slot is available. Preserves the\n"
    "caller's argument on the stack.")
subroutine(0xB8F8, "close_all_net_chans",
    title="Close all network channels for current station",
    description="Scans FCB slots &0F down to 0, closing those\n"
    "matching the current station. C=0 closes all\n"
    "matching entries; C=1 closes with write-flush.",
    on_entry={"c": "0=close all, 1=close with write-flush"})
subroutine(0xB8FC, "scan_fcb_flags",
    title="Scan FCB slot flags from &10 downward",
    description="Iterates through FCB slots starting at &10,\n"
    "checking each slot's flags byte. Returns when\n"
    "all slots have been processed.")
subroutine(0xB925, "match_station_net",
    title="Check FCB slot matches current station/network",
    description="Compares the station and network numbers in the\n"
    "FCB at slot X against the current values using\n"
    "EOR. Returns Z=1 if both match, Z=0 if either\n"
    "differs.",
    on_entry={"x": "FCB slot index"},
    on_exit={"z": "1=match, 0=no match"})
subroutine(0xB934, "find_open_fcb",
    title="Find next open FCB slot for current connection",
    description="Scans from the current index, wrapping around at\n"
    "the end. On the first pass finds active entries\n"
    "matching the station; on the second pass finds\n"
    "empty slots for new allocations.")
subroutine(0xB977, "init_wipe_counters",
    title="Initialise byte counters for wipe/transfer",
    description="Clears the pass counter, byte counter, offset\n"
    "counter, and transfer flag. Stores &FF sentinels\n"
    "in l10cd/l10ce. Returns with X/Y pointing at\n"
    "workspace offset &10CA.",
    on_exit={"x": "&CA (workspace offset low)", "y": "&10 (workspace page)"})
subroutine(0xB99A, "start_wipe_pass",
    title="Start wipe pass for current FCB",
    description="Verifies the workspace checksum, saves the station\n"
    "context (pushing station low/high), initialises\n"
    "transfer counters via init_wipe_counters, and sends\n"
    "the initial request via send_and_receive. Clears the\n"
    "active and offset flags on completion.",
    on_entry={"x": "FCB slot index"})
subroutine(0xBA09, "save_fcb_context",
    title="Save FCB context and process pending slots",
    description="Copies 13 bytes from the TX buffer (&0F00) and\n"
    "fs_load_addr workspace to temporary storage at\n"
    "&10D9. If Y=0, skips to the restore loop. Otherwise\n"
    "scans for pending FCB slots (bits 7+6 set), flushes\n"
    "each via start_wipe_pass, allocates new slots via\n"
    "find_open_fcb, and sends directory requests. Falls\n"
    "through to restore_catalog_entry.",
    on_entry={"y": "filter attribute (0=process all)"})
subroutine(0xBAC0, "restore_catalog_entry",
    title="Restore saved catalog entry to TX buffer",
    description="Copies 13 bytes from the context buffer at &10D9\n"
    "back to the TX buffer at &0F00. Falls through to\n"
    "find_matching_fcb.")
subroutine(0xBACF, "find_matching_fcb",
    title="Find FCB slot matching channel attribute",
    description="Scans FCB slots 0-&0F for an active entry whose\n"
    "attribute reference matches l10c9. Converts the\n"
    "attribute to a channel index, then verifies the\n"
    "station and network numbers. On the first scan\n"
    "past slot &0F, saves context via save_fcb_context\n"
    "and restarts. Returns Z=0 if the FCB has saved\n"
    "offset data (bit 5 set).",
    on_exit={"x": "matching FCB index", "z": "0=has offset data, 1=no offset"})
subroutine(0xBB2A, "inc_fcb_byte_count",
    title="Increment 3-byte FCB transfer count",
    description="Increments l1000+X (low), cascading overflow to\n"
    "l1010+X (mid) and l1020+X (high).",
    on_entry={"x": "FCB slot index"})
# Located in 4.21_v1 at &BB38 (was &B799 in 4.18). The fingerprint
# initially mis-pointed to &BB2A (which is `inc_fcb_byte_count`); the
# real entry is &BB38, distinguishable by the 9-byte workspace save
# loop at &BB3A (`LDX #&F7 / loop: LDA &FFBD,X / PHA / INX / BMI`) —
# the 4.21 version preserves &FFB7-&FFBF rather than just fs_options
# and fs_block_offset (see CHANGES-FROM-4.18 §5).
# Already classified as code (`sub_cbb38`, 7 callers) so no entry()
# needed.
subroutine(0xBB38, "process_all_fcbs",
    title="Process all active FCB slots",
    description="Saves 9 workspace bytes (&FFB7-&FFBF) on the stack\n"
    "via a PHX/PHY/loop preamble, then scans FCB slots\n"
    "&0F down to 0. Calls start_wipe_pass for each\n"
    "active entry matching the filter attribute in Y\n"
    "(0=match all). Restores all saved context on\n"
    "completion. Also contains the OSBGET/OSBPUT inline\n"
    "logic for reading and writing bytes through file\n"
    "channels. The 4.18 equivalent at &B799 saved only\n"
    "fs_options + fs_block_offset (2 bytes); 4.21 saves\n"
    "9 bytes to prevent cross-FCB workspace corruption.",
    on_entry={"y": "filter attribute (0=process all)"})
subroutine(0xBC74, "flush_fcb_if_station_known",
    title="Flush FCB byte count to server if station is set",
    description="Saves all registers, checks if the FCB has a\n"
    "known station. If yes, sends the accumulated byte\n"
    "count as a flush request to the file server. If no\n"
    "station is set, falls through to flush_fcb_with_init\n"
    "which saves FCB context first.",
    on_entry={"Y": "channel index (FCB slot)"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"})
subroutine(0xBC7C, "flush_fcb_with_init",
    title="Save FCB context and flush byte count to server",
    description="Saves all registers and the current FCB context,\n"
    "copies the FCB byte count into the TX command buffer,\n"
    "and sends a flush/close request to the file server.\n"
    "Restores the catalog entry and all registers on return.",
    on_entry={"Y": "channel index (FCB slot)"},
    on_exit={"A": "preserved", "X": "preserved", "Y": "preserved"})
label(0xBC89, "store_station_and_flush")
subroutine(0xBCBC, "send_wipe_request",
    title="Send wipe/close request packet",
    description="Sets up the TX control block with function code\n"
    "&90, the reply port from Y, and the data byte from\n"
    "A. Sends via send_disconnect_reply, then checks the\n"
    "error code — raises the server error if non-zero.",
    on_entry={"a": "data byte to send", "y": "reply port"})
subroutine(0xBD15, "send_and_receive",
    title="Set up FS options and transfer workspace",
    description="Calls set_options_ptr to configure the FS options\n"
    "pointer, then jumps to setup_transfer_workspace to\n"
    "initialise the transfer and send the request.",
    on_entry={"a": "transfer mode", "x": "workspace offset low", "y": "workspace page"})
subroutine(0xBD1B, "read_rx_attribute",
    title="Read receive attribute byte from RX buffer",
    description="Reads byte at offset &0A in the network receive\n"
    "control block, used to track which channel owns the\n"
    "current receive buffer.",
    on_entry={},
    on_exit={"A": "receive attribute byte", "Y": "&0A"})
subroutine(0xBD20, "store_rx_attribute",
    title="Store receive attribute byte to RX buffer",
    description="Writes A to offset &0A in the network receive\n"
    "control block, marking which channel owns the\n"
    "current receive buffer.",
    on_entry={"A": "attribute byte to store"},
    on_exit={"Y": "&0A"})

# --- cmd_print subroutines ---

subroutine(0xBD25, "abort_if_escape",
    title="Test escape flag and abort if pressed",
    description="Checks the escape flag byte; returns immediately\n"
    "if bit 7 is clear. If escape has been pressed,\n"
    "falls through to the escape abort handler which\n"
    "acknowledges the escape via OSBYTE &7E.",
    on_entry={"escape_flag (&FF)":
              "MOS escape pending flag (bit 7 set = escape pressed)"},
    on_exit={"behaviour": "returns with no side effects on the no-escape "
             "path; on escape, acknowledges via OSBYTE &7E and raises "
             "'Escape' via the error_inline chain (does not return)"})

# --- cmd_dump subroutines ---

subroutine(0xBE01, "print_dump_header",
    title="Print hex dump column header line",
    description="Outputs the starting address followed by 16 hex\n"
    "column numbers (00-0F), each separated by a space.\n"
    "Provides the column alignment header for *Dump\n"
    "output.")
subroutine(0xBE37, "print_hex_and_space",
    title="Print hex byte followed by space",
    description="Saves A, prints it as a 2-digit hex value via\n"
    "print_hex_byte, outputs a space character, then\n"
    "restores A from the stack. Used by cmd_dump and\n"
    "print_dump_header for column-aligned hex output.",
    on_entry={"a": "byte value to print"})
subroutine(0xBF71, "close_ws_file",
    title="Close file handle stored in workspace",
    description="Loads the file handle from ws_page and closes it\n"
    "via OSFIND with A=0.")
subroutine(0xBF78, "open_file_for_read",
    title="Open file for reading via OSFIND",
    description="Computes the filename address from the command text\n"
    "pointer plus the Y offset, calls OSFIND with A=&40\n"
    "(open for input). Stores the handle in ws_page.\n"
    "Raises 'Not found' if the returned handle is zero.")
label(0xBF9E, "restore_text_ptr")
label(0xBFB8, "done_skip_filename")
subroutine(0xBE42, "parse_dump_range",
    title="Parse hex address for dump range",
    description="Reads up to 4 hex digits from the command line\n"
    "into a 4-byte accumulator, stopping at CR or\n"
    "space. Each digit shifts the accumulator left\n"
    "by 4 bits before ORing in the new nybble.")
subroutine(0xBEAB, "init_dump_buffer",
    title="Initialise dump buffer and parse address range",
    description="Parses the start and end addresses from the command\n"
    "line via parse_dump_range. If no end address is given,\n"
    "defaults to the file extent. Validates both addresses\n"
    "against the file size, raising 'Outside file' if either\n"
    "exceeds the extent.")
subroutine(0xBFBA, "advance_x_by_8",
    title="Advance X by 8 via nested JSR chain",
    description="Calls advance_x_by_4 (which itself JSRs inx4 then\n"
    "falls through to inx4), then falls through to inx4\n"
    "for a total of 4+4=8 INX operations.",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 8",
             "a, y": "preserved",
             "n, z flags": "reflect new X (last INX)"})
subroutine(0xBFBD, "advance_x_by_4",
    title="Advance X by 4 via JSR and fall-through",
    description="JSRs to inx4 for 4 INX operations, then falls\n"
    "through to inx4 for another 4 — but when called\n"
    "directly (not from advance_x_by_8), the caller\n"
    "returns after the first inx4, yielding X+4.",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 4 (+8 when reached via fall-through from "
             "advance_x_by_8)",
             "a, y": "preserved"})
subroutine(0xBFC0, "inx4",
    title="Increment X four times",
    description="Four consecutive INX instructions. Used as a\n"
    "building block by advance_x_by_4 and\n"
    "advance_x_by_8 via JSR/fall-through chaining.",
    on_entry={"x": "value to advance"},
    on_exit={"x": "input + 4",
             "a, y": "preserved",
             "n, z flags": "reflect new X"})
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): label(0x049B, "send_next_rom_page")

# ============================================================
# Inline comments (from NFS 3.65 correspondence)
# ============================================================

# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0016, "A=&FF: signal error to co-processor via R4", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0018, "Send &FF error signal to Tube R4", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x001B, "Flush any pending R2 byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x001E, "A=0: send zero prefix to R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0020, "Send zero prefix byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0023, "Y=0: start of error block at (&FD)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0024, "Load error number from (&FD),0", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0026, "Send error number via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0029, "Advance to next error string byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x002A, "Load next error string byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x002C, "Send error string byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x002F, "Zero byte = end of error string", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0030, "Loop until zero terminator sent", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0032, "Reset stack pointer to top", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0034, "TXS: set stack pointer from X", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0035, "Enable interrupts for main loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0036, "BIT R1 status: check WRCH request", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0039, "R1 not ready: check R2 instead", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x003B, "Read character from Tube R1 data", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0041, "BIT R2 status: check command byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0044, "R2 not ready: loop back to R1 check", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0046, "Re-check R1: WRCH has priority over R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0049, "R1 ready: handle WRCH first", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x004B, "Read command byte from Tube R2 data", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x004E, "Self-modify JMP low byte for dispatch", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0050, "Dispatch to handler via indirect JMP", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0053, "Tube transfer address low byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0054, "Tube transfer page (default &80)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0055, "Tube transfer address byte 2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0056, "Tube transfer address byte 3", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0400, "JMP to BEGIN startup entry", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0403, "JMP to tube_escape_check (&06A7)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0406, "A>=&80: address claim; A<&80: data transfer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0408, "A<&80: data transfer setup (SENDW)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x040A, "A>=&C0: new address claim from another host", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x040C, "C=1: external claim, check ownership", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x040E, "Map &80-&BF range to &C0-&FF for comparison", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0410, "Is this for our currently-claimed address?", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0412, "Not our address: return", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0414, "PHP: save interrupt state for release", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0415, "SEI: disable interrupts during R4 protocol", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0416, "R4 cmd 5: release our address claim", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0418, "Send release command to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x041B, "Load our currently-claimed address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x041D, "Send our address as release parameter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0420, "Restore interrupt state", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0421, "&80 sentinel: clear address claim", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0423, "&80 sentinel = no address currently claimed", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0425, "Store to claim-in-progress flag", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0427, "Return from tube_post_init", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0428, "Another host claiming; check if we're owner", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x042A, "C=1: we have an active claim", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x042C, "Compare with our claimed address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x042E, "Match: return (we already have it)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0430, "Not ours: CLC = we don't own this address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0431, "Return with C=0 (claim denied)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0432, "Accept new claim: update our address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0434, "Return with address updated", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0435, "PHP: save interrupt state", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0436, "SEI: disable interrupts for R4 protocol", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0437, "Save 16-bit transfer address from (X,Y)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0439, "Store address pointer low byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x043B, "R4 byte 1 of 7: transfer type (A on entry)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x043E, "X = transfer type for tube_ctrl_values lookup", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x043F, "Y=3: loop counter for 4 address bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0441, "Load tube_claimed_id (Econet host ownership)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0443, "R4 byte 2 of 7: claimed_id (Econet extension)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0446, "Load address byte at offset Y (big-endian)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0448, "R4 bytes 3-6 of 7: address Y=3,2,1,0", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x044B, "Y--: next address byte (3->2->1->0)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x044C, "Y>=0: loop for all 4 address bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x044E, "Y=&18: enable Tube control register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0450, "Enable Tube interrupt generation", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0453, "Look up Tube control bits for this xfer type", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0456, "Apply transfer-specific control bits", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0459, "LSR 1: shift ctrl bit 1 into C (discarded)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x045A, "LSR 2: shift ctrl bit 2 into C (flush flag)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x045B, "C=0: not a P-to-H type (only 0/2 flush)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x045D, "Drain R3 FIFO byte 1 (stale data from last xfer)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0460, "Drain R3 FIFO byte 2 (2-byte FIFO ready for fresh data)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0463, "R4 byte 7 of 7: trigger/sync (post-LSR ctrl value)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0466, "Poll R4 status for co-processor response", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0469, "Bit 6 clear: not ready, keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x046B, "R4 bit 7: co-processor acknowledged transfer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x046D, "Type 4 = SENDW (host-to-parasite word xfer)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x046F, "Not SENDW type: skip release path", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0471, "SENDW complete: release, sync, restart", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0474, "Sync via R2 send", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0477, "Restart Tube main loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x047A, "LSR: check bit 0 (NMI used?)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x047B, "C=0: NMI not used, skip NMI release", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x047D, "Release Tube NMI (transfer used interrupts)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x047F, "Write &88 to Tube control to release NMI", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0482, "Restore interrupt state", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0483, "Return from transfer setup", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0484, "BEGIN: enable interrupts for Tube host code", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0485, "C=1: hard break, claim addr &FF", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0487, "C=0, A!=0: re-init path", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0489, "Z=1 from C=0 path: just acknowledge", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x048C, "Read last break type from OS workspace", inline=True)
# 4.18 uses LDX &028D directly instead of OSBYTE &FD
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x048F, "Soft break (X=0): re-init Tube and restart", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0491, "Claim address &FF (startup = highest prio)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0493, "Request address claim from Tube system", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0496, "C=0: claim failed, retry", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0498, "Init reloc pointers from ROM header", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x049B, "Save interrupt state", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x049D, "R4 cmd 7: SENDW to send ROM to parasite", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x049C, "Disable interrupts during ROM transfer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x049F, "Set up Tube for SENDW transfer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04A2, "Y=0: start at beginning of page", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04A4, "Store to zero page pointer low byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04A6, "Send 256-byte page via R3, byte at a time", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04A8, "Write byte to Tube R3 data register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04AB, "Timing delay: Tube data register needs NOPs", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04AC, "NOP delay (2)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04AD, "NOP delay (3)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04AE, "Next byte in page", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04AF, "Loop for all 256 bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04B1, "Restore interrupt state after page sent", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04B2, "Increment 24-bit destination addr", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04B4, "No carry: skip higher bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04B6, "Carry into second byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04B8, "No carry: skip third byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04BA, "Carry into third byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04BC, "Increment page counter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04BE, "Bit 6 set = all pages transferred", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04C0, "More pages: loop back to SENDW", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04C2, "Re-init reloc pointers for final claim", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04C5, "A=4: transfer type for final address claim", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04C7, "Y=0: transfer address low byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04C9, "X=&53: transfer address high byte (&0053)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04CB, "Claim Tube address for transfer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04CE, "Init: start sending from &8000", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04D0, "Store &80 as source page high byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04D2, "Store &80 as page counter initial value", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04D4, "A=&20: bit 5 mask for ROM type check", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04D6, "ROM type bit 5: reloc address in header?", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04D9, "Y = 0 or &20 (reloc flag)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04DA, "Store as transfer address selector", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04DC, "No reloc addr: use defaults", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04DE, "Skip past copyright string to find reloc addr", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04E1, "Skip past null-terminated copyright string", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04E2, "Load next byte from ROM header", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04E5, "Loop until null terminator found", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04E7, "Read 4-byte reloc address from ROM header", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04EA, "Store reloc addr byte 1 as transfer addr", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04EC, "Load reloc addr byte 2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04EF, "Store as source page start", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04F1, "Load reloc addr byte 3", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04F4, "Load reloc addr byte 4 (highest)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04F7, "Store high byte of end address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04F9, "Store byte 3 of end address", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x04FB, "Return with pointers initialised", inline=True)
# Tube R2 command dispatch table: 12 entries mapping R2 command
# codes 0-11 to handler addresses in pages 5-6.
_tube_r2_entries = [
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0500, "tube_osrdch",        "R2 cmd 0: OSRDCH"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0502, "tube_oscli",         "R2 cmd 1: OSCLI"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0504, "tube_osbyte_2param", "R2 cmd 2: OSBYTE (2-param)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0506, "tube_osbyte_long",   "R2 cmd 3: OSBYTE (3-param)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0508, "tube_osword",        "R2 cmd 4: OSWORD"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x050A, "tube_osword_rdln",   "R2 cmd 5: OSWORD 0 (read line)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x050C, "tube_osargs",        "R2 cmd 6: OSARGS"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x050E, "tube_osbget",        "R2 cmd 7: OSBGET"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0510, "tube_osbput",        "R2 cmd 8: OSBPUT"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0512, "tube_osfind",        "R2 cmd 9: OSFIND"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0514, "tube_osfile",        "R2 cmd 10: OSFILE"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0516, "tube_osgbpb",        "R2 cmd 11: OSGBPB"),
]
# UNMAPPED: for addr, target_label, desc in _tube_r2_entries:
# UNMAPPED (orphan body):     word(addr)
# UNMAPPED (orphan body):     expr(addr, target_label)
# UNMAPPED (orphan body):     comment(addr, desc, inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0518, """\
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): Tube ULA control register values, indexed by transfer
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): type (0-7). Written to &FEE0 after clearing V+M with
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): &18. Bit layout: S=set/clear, T=reset regs, P=PRST,
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): V=2-byte R3, M=PNMI(R3), J=PIRQ(R4), I=PIRQ(R1),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): Q=HIRQ(R4). Bits 1-7 select flags; bit 0 (S) is the
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): value to set or clear.""")
_tube_ctrl_entries = [
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0518, "Type 0: set I+J (1-byte R3, parasite to host)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x0519, "Type 1: set M (1-byte R3, host to parasite)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051A, "Type 2: set V+I+J (2-byte R3, parasite to host)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051B, "Type 3: set V+M (2-byte R3, host to parasite)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051C, "Type 4: clear V+M (execute code at address)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051D, "Type 5: clear V+M (release address claim)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051E, "Type 6: set I (define event handler)"),
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF):     (0x051F, "Type 7: clear V+M (transfer and release)"),
]
# UNMAPPED: for addr, desc in _tube_ctrl_entries:
# UNMAPPED (orphan body):     byte(addr)
# UNMAPPED (orphan body):     comment(addr, desc, inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0520, "Read channel handle from R2 for BPUT", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0523, "Y=channel handle for OSBPUT", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0524, "Read data byte from R2 for OSBPUT", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x052A, "Reply with &7F ack after OSBPUT", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x052D, "Read channel handle from R2 for BGET", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0534, "Reply with carry+byte via RDCH protocol", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x053A, "ROR A: encode carry (error flag) into bit 7", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x053B, "Send carry+data byte to Tube R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x053E, "ROL A: restore carry flag", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x053F, "Return via tube_reply_byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0542, "Read open mode from R2 for OSFIND", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0545, "Mode=0: close file(s)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0547, "Save open mode on stack", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0548, "Read filename string from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x054B, "Restore open mode", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x054F, "Reply with file handle via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0552, "OSFIND close: read handle from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0555, "Transfer handle to Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0556, "A=0: close file", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x055B, "Reply with acknowledgement via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x055E, "Read file handle from R2 for OSARGS", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0561, "Y=file handle for OSARGS", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0562, "Read 4-byte arg + reason from R2 into ZP", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0564, "Read next param byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0567, "Store param at ZP+X (escape_flag downward)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0569, "Decrement index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x056A, "More params: continue reading", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x056C, "Read OSARGS reason code from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0572, "Send result A via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0575, "X=3: send 4 result bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0577, "Load result byte from zero page", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0579, "Send result byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x057C, "Decrement byte counter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x057D, "More bytes: continue sending", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x057F, "Return to Tube main loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0582, "X=0: initialise string buffer index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0584, "Y=0: initialise string offset", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0586, "Read next string byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0589, "Store in string buffer at &0700+Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x058C, "Advance string index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x058D, "Buffer full (256 bytes): done", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x058F, "Check for CR terminator", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0591, "Not CR: continue reading", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0593, "Y=7: set XY=&0700 for OSCLI/OSFIND", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0595, "Return with XY pointing to string buffer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0596, "Read command string from R2 into &0700", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0599, "Execute command string via OSCLI", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x059C, "&7F = success acknowledgement", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x059E, "Poll R2 status until ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05A1, "Bit 6 clear: not ready, loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05A3, "Write byte to R2 data register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05A6, "Return to Tube main loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05A9, "Read 16-byte OSFILE control block from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05AB, "Read next control block byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05AE, "Store at ZP+X (control block)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05B0, "Decrement index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05B1, "More bytes: continue reading", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05B3, "Read filename string from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05B6, "Set filename ptr low = 0", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05B8, "Set filename ptr high = &07", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05BA, "Y=0: OSFILE reason code index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05BC, "Read OSFILE reason code from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05BF, "Execute OSFILE", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05C2, "Send result A via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05C5, "X=&10: send 16 result bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05C7, "Load control block byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05C9, "Send control block byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05CC, "Decrement byte counter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05CD, "More bytes: continue sending", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05D1, "X=&0D: read 13-byte OSGBPB ctrl block", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05D3, "Read next control block byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05D6, "Store at ZP+X (escape_flag downward)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05D8, "Decrement index", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05D9, "More bytes: continue reading", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05DB, "Read OSGBPB reason code from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05DE, "Y=0: OSGBPB direction/count", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05E3, "Save result A on stack", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05E4, "X=&0C: send 12 result bytes", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05E6, "Load result byte from zero page", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05E8, "Send result byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05EB, "Decrement byte counter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05EC, "More bytes: continue sending", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05EE, "Recover completion status from stack", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05EF, "Reply with RDCH-style result", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05F2, "Read X parameter from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05F5, "Transfer to X register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05F6, "Read A (OSBYTE function code) from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05F9, "Execute OSBYTE A,X", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05FC, "Poll R2 status for result send", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x05FF, "BVC: page 5/6 boundary straddle", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0600, "Send carry+status to co-processor via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0601, "Send X result for 2-param OSBYTE", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0604, "Return to main event loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0607, "Read X, Y, A from R2 for 3-param OSBYTE", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x060A, "Save in X", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x060B, "Read Y parameter from co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x060E, "Save in Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x060F, "Read A (OSBYTE function code)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0612, "Execute OSBYTE A,X,Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0615, "Test for OSBYTE &9D (fast Tube BPUT)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0617, "OSBYTE &9D (fast Tube BPUT): no result needed", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0619, "Encode carry (error flag) into bit 7", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x061A, "Send carry+status byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x061D, "Poll R2 status for ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0620, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0622, "Send Y result, then fall through to send X", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0625, "BVS always: jump to send X via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0627, "Overlapping entry: &20 = JSR c06c5 (OSWORD)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x062A, "Save OSWORD number in Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x062B, "Poll R2 status for data ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x062E, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0630, "Read param block length from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0633, "DEX: length 0 means no params to read", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0634, "No params (length=0): skip read loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0636, "Poll R2 status for data ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0639, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x063B, "Read param byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x063E, "Store param bytes into block at &0128", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0641, "Next param byte (descending)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0642, "Loop until all params read", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0644, "Restore OSWORD number from Y", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0645, "XY=&0128: param block address for OSWORD", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0647, "Y=&01: param block at &0128", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0649, "Execute OSWORD with XY=&0128", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x064C, "Poll R2 status for ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x064F, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0651, "Read result block length from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0654, "Decrement result byte counter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0655, "No results to send: return to main loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0657, "Send result block bytes from &0128 via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x065A, "Poll R2 status for ready", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x065D, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x065F, "Send result byte via R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0662, "Next result byte (descending)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0663, "Loop until all results sent", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0665, "Return to main event loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0668, "Read 5-byte OSWORD 0 control block from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x066A, "Read control block byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x066D, "Store in zero page params", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x066F, "Next byte (descending)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0670, "Loop until all 5 bytes read", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0672, "X=0 after loop, A=0 for OSWORD 0 (read line)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0673, "Y=0 for OSWORD 0", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0675, "A=0: OSWORD 0 (read line)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0676, "Read input line from keyboard", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0679, "C=0: line read OK; C=1: escape pressed", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x067B, "&FF = escape/error signal to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x067D, "Escape: send &FF error to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0680, "X=0: start of input buffer at &0700", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0682, "&7F = line read successfully", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0684, "Send &7F (success) to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0687, "Load char from input buffer", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x068A, "Send char to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x068D, "Next character", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x068E, "Check for CR terminator", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0690, "Loop until CR terminator sent", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0692, "Return to main event loop", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0695, "Poll R2 status (bit 6 = ready)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x0698, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x069A, "Write A to Tube R2 data register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x069D, "Return to caller", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x069E, "Poll R4 status (bit 6 = ready)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06A1, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06A3, "Write A to Tube R4 data register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06A6, "Return to caller", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06A7, "Check OS escape flag at &FF", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06A9, "SEC+ROR: put bit 7 of &FF into carry+bit 7", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06AA, "ROR: shift escape bit 7 to carry", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06AB, "Escape set: forward to co-processor via R1", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06AD, "EVNTV: forward event A, Y, X to co-processor", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06AE, "Send &00 prefix (event notification)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06B0, "Send zero prefix via R1", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06B3, "Y value for event", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06B4, "Send Y via R1", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06B7, "X value for event", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06B8, "Send X via R1", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06BB, "Restore A (event type)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06BC, "Poll R1 status (bit 6 = ready)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06BF, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06C1, "Write A to Tube R1 data register", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06C4, "Return to caller", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06C5, "Poll R2 status (bit 7 = ready)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06C8, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06CA, "Read data byte from R2", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06CD, "Return with byte in A", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06CE, "Is byte &FE (VDU stream start)?", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06D0, "Below &FE: normal byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06D2, "&FF: set up event/break vectors", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06D4, "&FE: check Y parameter", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06D6, "Y=0: treat as normal byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06D8, "X=6: six extra pages", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06DA, "OSBYTE &14: explode char defs", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06DF, "Poll R1 status (bit 6 = ready)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06E2, "Not ready: keep polling", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06E4, "Read byte from Tube R1", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06E7, "Zero: end of VDU stream", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06EC, "Loop back to read next R1 byte", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06EF, "EVNTV low byte (&AD)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06F1, "Store in EVNTV vector low", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06F4, "EVNTV high byte (page 6)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06F6, "Store in EVNTV vector high", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06F9, "BRKV low byte (&16)", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06FB, "Store in BRKV vector", inline=True)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): comment(0x06FE, "A=0", inline=True)
comment(0x8003, "JMP service_handler", inline=True)
comment(0x8006, "ROM type: service + language", inline=True)
comment(0x8019, "Null terminator before copyright", inline=True)
# UNMAPPED: comment(0x8028, "A=4: SR bit mask for IFR test", inline=True)
# UNMAPPED: comment(0x802A, "Test IFR bit 2: SR complete", inline=True)
comment(0x802D, "SR set: shift register complete", inline=True)
comment(0x8032, "A=5: not our interrupt, pass on", inline=True)
# UNMAPPED: comment(0x8031, "Return service code 5 to MOS", inline=True)
# UNMAPPED: comment(0x8032, "Save X on stack", inline=True)
# UNMAPPED: comment(0x8033, "Push saved X", inline=True)
# UNMAPPED: comment(0x8034, "Save Y on stack", inline=True)
# UNMAPPED: comment(0x8035, "Push saved Y", inline=True)
# UNMAPPED: comment(0x8036, "Read ACR for shift register restore", inline=True)
# UNMAPPED: comment(0x8039, "Clear SR mode bits (2-4)", inline=True)
# UNMAPPED: comment(0x803B, "Restore saved SR mode from ws_0d64", inline=True)
# UNMAPPED: comment(0x803E, "Write restored ACR to system VIA", inline=True)
# UNMAPPED: comment(0x8041, "Read SR to clear shift register IRQ", inline=True)
# UNMAPPED: comment(0x8044, "A=4: SR bit mask", inline=True)
# UNMAPPED: comment(0x8046, "Clear SR interrupt flag in IFR", inline=True)
# UNMAPPED: comment(0x8049, "Disable SR interrupt in IER", inline=True)
# UNMAPPED: comment(0x804C, "Load TX operation type for dispatch", inline=True)
comment(0x803A, "Copy to A for sign test", inline=True)
comment(0x803B, "Bit 7 set: dispatch via table", inline=True)
comment(0x803D, "A=&FE: Econet receive event", inline=True)
comment(0x8042, "Fire event (enable: *FX52,150)", inline=True)
comment(0x8045, "Dispatch through event vector", inline=True)
comment(0x803F, "Call event vector handler", inline=True)
# UNMAPPED: comment(0x805D, "Y >= &86: above dispatch range", inline=True)
# UNMAPPED: comment(0x805F, "Out of range: skip protection", inline=True)
# UNMAPPED: comment(0x8061, "Save current JSR protection mask", inline=True)
# UNMAPPED: comment(0x8064, "Backup to saved_jsr_mask", inline=True)
# UNMAPPED: comment(0x8067, "Set protection bits 2-4", inline=True)
# UNMAPPED: comment(0x8069, "Apply protection during dispatch", inline=True)
comment(0x8048, "Push return addr high (&85)", inline=True)
comment(0x804A, "High byte on stack for RTS", inline=True)
comment(0x804B, "Load dispatch target low byte", inline=True)
comment(0x804E, "Low byte on stack for RTS", inline=True)
comment(0x804F, "RTS = dispatch to PHA'd address", inline=True)
comment(0x8050, "INTOFF: read station ID, disable NMIs", inline=True)
comment(0x8053, "Full ADLC hardware reset", inline=True)
comment(0x8056, "OSBYTE &EA: check Tube co-processor", inline=True)
comment(0x8058, "X=0 for OSBYTE", inline=True)
comment(0x805A, "Clear Econet init flag before setup", inline=True)
comment(0x8063, "OSBYTE &8F: issue service request", inline=True)
comment(0x8065, "X=&0C: NMI claim service", inline=True)
comment(0x805D, "Check Tube presence via OSBYTE &EA", inline=True)
comment(0x8060, "Store Tube presence flag from OSBYTE &EA", inline=True)
comment(0x8067, "Issue NMI claim service request", inline=True)
comment(0x806A, "Y=5: NMI claim service number", inline=True)
comment(0x806C, "Check if NMI service was claimed (Y changed)", inline=True)
comment(0x806E, "Service claimed by other ROM: skip init", inline=True)
comment(0x8070, "Copy 32 bytes of NMI shim from ROM to &0D00", inline=True)
comment(0x8072, "Read byte from NMI shim ROM source", inline=True)
comment(0x8075, "Write to NMI shim RAM at &0D00", inline=True)
comment(0x8078, "Next byte (descending)", inline=True)
comment(0x8079, "Loop until all 32 bytes copied", inline=True)
comment(0x807B, "Patch current ROM bank into NMI shim", inline=True)
comment(0x807D, "Self-modifying code: ROM bank at &0D07", inline=True)
comment(0x8080, "Clear source network (Y=0 from copy loop)", inline=True)
comment(0x8083, "Clear Tube release flag", inline=True)
comment(0x8085, "Clear TX operation type", inline=True)
# UNMAPPED: comment(0x80AC, "Read station ID (and disable NMIs)", inline=True)
# UNMAPPED: comment(0x80AF, "Set own station as TX source", inline=True)
comment(0x808F, "&80 = Econet initialised", inline=True)
comment(0x8091, "Mark TX as complete (ready)", inline=True)
comment(0x8094, "Mark Econet as initialised", inline=True)
comment(0x8097, "INTON: re-enable NMIs (&FE20 read side effect)", inline=True)
comment(0x809A, "Return", inline=True)
comment(0x809B, "A=&01: mask for SR2 bit0 (AP = Address Present)", inline=True)
comment(0x809D, "BIT SR2: Z = A AND SR2 -- tests if AP is set", inline=True)
comment(0x80A0, "AP not set, no incoming data -- check for errors", inline=True)
comment(0x80A2, "Read first RX byte (destination station address)", inline=True)
comment(0x80A5, "Compare to our station ID (&FE18 read = INTOFF, disables NMIs)", inline=True)
comment(0x80A8, "Match -- accept frame", inline=True)
comment(0x80AA, "Check for broadcast address (&FF)", inline=True)
comment(0x80AC, "Neither our address nor broadcast -- reject frame", inline=True)
comment(0x80AE, "Flag &40 = broadcast frame", inline=True)
comment(0x80B0, "Store broadcast flag in rx_src_net", inline=True)
comment(0x80B3, "Install nmi_rx_scout_net NMI handler", inline=True)
comment(0x80B5, "Install next handler and RTI", inline=True)
comment(0x80B8, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x80BB, "No RDA -- check errors", inline=True)
comment(0x80BD, "Read destination network byte", inline=True)
comment(0x80C0, "Network = 0 -- local network, accept", inline=True)
comment(0x80C2, "EOR &FF: test if network = &FF (broadcast)", inline=True)
comment(0x80C4, "Broadcast network -- accept", inline=True)
comment(0x80C6, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", inline=True)
comment(0x80C8, "Write CR1 to discontinue RX", inline=True)
comment(0x80CB, "Return to idle scout listening", inline=True)
comment(0x80CE, "Network = 0 (local): clear tx_flags", inline=True)
comment(0x80D1, "Store Y offset for scout data buffer", inline=True)
comment(0x80D3, "Install scout data handler (&8102)", inline=True)
# UNMAPPED: comment(0x80F8, "High byte of scout data handler", inline=True)
comment(0x80D5, "Install scout data loop and RTI", inline=True)
comment(0x80D8, "Read SR2", inline=True)
comment(0x80DB, "Test AP (b0) | RDA (b7)", inline=True)
comment(0x80DD, "Neither set -- clean end, discard frame", inline=True)
comment(0x80DF, "Unexpected data/status: full ADLC reset", inline=True)
comment(0x80E2, "Discard and return to idle", inline=True)
comment(0x80E5, "Gentle discard: RX_DISCONTINUE", inline=True)
comment(0x80E8, "Y = buffer offset", inline=True)
comment(0x80EA, "Read SR2", inline=True)
comment(0x80ED, "No RDA -- error handler", inline=True)
comment(0x80EF, "Read data byte from RX FIFO", inline=True)
comment(0x80F2, "Store at &0D3D+Y (scout buffer)", inline=True)
comment(0x80F5, "Advance buffer index", inline=True)
comment(0x80F6, "Read SR2 again (FV detection point)", inline=True)
comment(0x80F9, "RDA set -- more data, read second byte", inline=True)
comment(0x80FB, "SR2 non-zero (FV or other) -- scout completion", inline=True)
comment(0x80FD, "Read second byte of pair", inline=True)
comment(0x8100, "Store at &0D3D+Y", inline=True)
comment(0x8103, "Advance and check buffer limit", inline=True)
comment(0x8104, "Copied all 12 scout bytes?", inline=True)
comment(0x8106, "Buffer full (Y=12) -- force completion", inline=True)
comment(0x8108, "Save final buffer offset", inline=True)
comment(0x810A, "Read SR2 for next pair", inline=True)
comment(0x810D, "SR2 non-zero -- loop back for more bytes", inline=True)
comment(0x810F, "SR2 = 0 -- RTI, wait for next NMI", inline=True)
comment(0x8112, "Save Y for next iteration", inline=True)
comment(0x8114, "Write CR1", inline=True)
comment(0x8117, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", inline=True)
comment(0x8119, "Write CR2", inline=True)
comment(0x811C, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x811E, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x8121, "No FV -- not a valid frame end, error", inline=True)
comment(0x8123, "FV set but no RDA -- missing last byte, error", inline=True)
comment(0x8125, "Read last byte from RX FIFO", inline=True)
comment(0x8128, "Store last byte at &0D3D+Y", inline=True)
comment(0x812B, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", inline=True)
comment(0x812D, "Write CR1: switch to TX mode", inline=True)
comment(0x8130, "Set bit7 of need_release_tube flag", inline=True)
comment(0x8131, "Rotate C=1 into bit7: mark Tube release needed", inline=True)
comment(0x8133, "Check port byte: 0 = immediate op, non-zero = data transfer", inline=True)
comment(0x8136, "Port non-zero -- look for matching receive block", inline=True)
comment(0x8138, "Port = 0 -- immediate operation handler", inline=True)
comment(0x813B, "Check if broadcast (bit6 of tx_flags)", inline=True)
comment(0x813E, "Not broadcast -- skip CR2 setup", inline=True)
comment(0x8140, "CR2=&07: broadcast prep", inline=True)
comment(0x8142, "Write CR2: broadcast frame prep", inline=True)
comment(0x8145, "Check if RX port list active (bit7)", inline=True)
comment(0x8148, "No active ports -- try NFS workspace", inline=True)
comment(0x814A, "Start scanning port list at page &C0", inline=True)
comment(0x814C, "Y=0: start offset within each port slot", inline=True)
comment(0x814E, "Store page to workspace pointer low", inline=True)
comment(0x8150, "Store page high byte for slot scanning", inline=True)
comment(0x8152, "Y=0: read control byte from start of slot", inline=True)
comment(0x8154, "Read port control byte from slot", inline=True)
comment(0x8156, "Zero = end of port list, no match", inline=True)
comment(0x8158, "&7F = any-port wildcard", inline=True)
comment(0x815A, "Not wildcard -- check specific port match", inline=True)
comment(0x815C, "Y=1: advance to port byte in slot", inline=True)
comment(0x815D, "Read port number from slot (offset 1)", inline=True)
comment(0x815F, "Zero port in slot = match any port", inline=True)
comment(0x8161, "Check if port matches this slot", inline=True)
comment(0x8164, "Port mismatch -- try next slot", inline=True)
comment(0x8166, "Y=2: advance to station byte", inline=True)
comment(0x8167, "Read station filter from slot (offset 2)", inline=True)
comment(0x8169, "Zero station = match any station, accept", inline=True)
comment(0x816B, "Check if source station matches", inline=True)
comment(0x816E, "Station mismatch -- try next slot", inline=True)
comment(0x8170, "Y=3: advance to network byte", inline=True)
comment(0x8171, "Read network filter from slot (offset 3)", inline=True)
comment(0x8173, "Zero = accept any network", inline=True)
comment(0x8175, "Check if source network matches", inline=True)
comment(0x8178, "Network matches or zero = accept", inline=True)
comment(0x817A, "Check if NFS workspace search pending", inline=True)
comment(0x817C, "No NFS workspace -- try fallback path", inline=True)
comment(0x817E, "Load current slot base address", inline=True)
comment(0x8180, "CLC for 12-byte slot advance", inline=True)
comment(0x8181, "Advance to next 12-byte port slot", inline=True)
comment(0x8183, "Update workspace pointer to next slot", inline=True)
comment(0x8185, "Always branches (page &C0 won't overflow)", inline=True)
comment(0x8187, "No match found -- discard frame", inline=True)
comment(0x818A, "Try NFS workspace if paged list exhausted", inline=True)
comment(0x818D, "No NFS workspace RX (bit6 clear) -- discard", inline=True)
comment(0x818F, "NFS workspace starts at offset 0 in page", inline=True)
comment(0x8191, "NFS workspace high byte for port list", inline=True)
comment(0x8193, "Scan NFS workspace port list", inline=True)
comment(0x8195, "Match found: set scout_status = 3", inline=True)
comment(0x8197, "Record match for completion handler", inline=True)
comment(0x819A, "Calculate transfer parameters", inline=True)
comment(0x819D, "C=0: no Tube claimed -- discard", inline=True)
comment(0x819F, "Check broadcast flag for ACK path", inline=True)
comment(0x81A2, "Not broadcast -- normal ACK path", inline=True)
comment(0x81A4, "Broadcast: different completion path", inline=True)
comment(0x81A7, "CR1=&44: RX_RESET | TIE", inline=True)
comment(0x81A9, "Write CR1: TX mode for ACK", inline=True)
comment(0x81AC, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", inline=True)
comment(0x81AE, "Write CR2: enable TX with PSE", inline=True)
comment(0x81B1, "Install data_rx_setup at &81DD", inline=True)
comment(0x81B3, "High byte of data_rx_setup handler", inline=True)
comment(0x81B5, "Send ACK with data_rx_setup as next NMI", inline=True)
comment(0x81B8, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", inline=True)
comment(0x81BA, "Write CR1: switch to RX for data frame", inline=True)
comment(0x81BD, "Install nmi_data_rx at &81E7", inline=True)
comment(0x81BF, "Install nmi_data_rx and return from NMI", inline=True)
comment(0x81C2, "A=1: AP mask for SR2 bit test", inline=True)
comment(0x81C4, "BIT SR2: test AP bit", inline=True)
comment(0x81C7, "No AP: wrong frame or error", inline=True)
comment(0x81C9, "Read first byte (dest station)", inline=True)
comment(0x81CC, "Compare to our station ID (INTOFF)", inline=True)
comment(0x81CF, "Not for us: error path", inline=True)
comment(0x81D1, "Install net check handler at &81FB", inline=True)
comment(0x81D3, "Set NMI vector via RAM shim", inline=True)
comment(0x81D6, "Validate source network = 0", inline=True)
comment(0x81D9, "SR2 bit7 clear: no data ready -- error", inline=True)
comment(0x81DB, "Read dest network byte", inline=True)
comment(0x81DE, "Network != 0: wrong network -- error", inline=True)
comment(0x81E0, "Install skip handler at &8211", inline=True)
comment(0x81E2, "High byte of &8211 handler", inline=True)
comment(0x81E4, "SR1 bit7: IRQ, data already waiting", inline=True)
comment(0x81E7, "Data ready: skip directly, no RTI", inline=True)
comment(0x81E9, "Install handler and return via RTI", inline=True)
comment(0x81EC, "Skip control and port bytes (already known from scout)", inline=True)
comment(0x81EF, "SR2 bit7 clear: error", inline=True)
comment(0x81F1, "Discard control byte", inline=True)
comment(0x81F4, "Discard port byte", inline=True)
comment(0x81F7, "A=2: Tube transfer flag mask", inline=True)
comment(0x81F9, "Check if Tube transfer active", inline=True)
comment(0x81FC, "Tube active: use Tube RX path", inline=True)
comment(0x81FE, "Install bulk read at &8239", inline=True)
comment(0x8200, "High byte of &8239 handler", inline=True)
comment(0x8202, "SR1 bit7: more data already waiting?", inline=True)
comment(0x8205, "Yes: enter bulk read directly", inline=True)
comment(0x8207, "No: install handler and RTI", inline=True)
comment(0x820A, "Tube: install Tube RX at &8296", inline=True)
comment(0x820C, "High byte of &8296 handler", inline=True)
comment(0x820E, "Install Tube handler and RTI", inline=True)
comment(0x8215, "Check tx_flags for error path", inline=True)
comment(0x8218, "Bit7 clear: RX error path", inline=True)
comment(0x821A, "Bit7 set: TX result = not listening", inline=True)
comment(0x821D, "Full ADLC reset on RX error", inline=True)
comment(0x8220, "Discard and return to idle listen", inline=True)
comment(0x8223, "Y = buffer offset, resume from last position", inline=True)
comment(0x8225, "Read SR2 for next pair", inline=True)
comment(0x8228, "SR2 bit7 clear: frame complete (FV)", inline=True)
comment(0x8233, "Read first byte of pair from RX FIFO", inline=True)
comment(0x8236, "Store byte to buffer", inline=True)
comment(0x8238, "Advance buffer offset", inline=True)
comment(0x8239, "Y != 0: no page boundary crossing", inline=True)
comment(0x823B, "Crossed page: increment buffer high byte", inline=True)
comment(0x823D, "Decrement remaining page count", inline=True)
comment(0x823F, "No pages left: handle as complete", inline=True)
comment(0x8241, "Read SR2 between byte pairs", inline=True)
comment(0x8244, "SR2 bit7 set: more data available", inline=True)
comment(0x8246, "SR2 non-zero, bit7 clear: frame done", inline=True)
comment(0x8248, "Read second byte of pair from RX FIFO", inline=True)
comment(0x824B, "Store byte to buffer", inline=True)
comment(0x824D, "Advance buffer offset", inline=True)
comment(0x824E, "Save updated buffer position", inline=True)
comment(0x8250, "Y != 0: no page boundary crossing", inline=True)
comment(0x8252, "Crossed page: increment buffer high byte", inline=True)
comment(0x8254, "Decrement remaining page count", inline=True)
comment(0x8256, "No pages left: frame complete", inline=True)
comment(0x825C, "Read SR2 for next iteration", inline=True)
comment(0x825F, "SR2 non-zero: more data, loop back", inline=True)
comment(0x8261, "SR2=0: no more data yet, wait for NMI", inline=True)
comment(0x8268, "CR1=&00: disable all interrupts", inline=True)
comment(0x826A, "Write CR2: disable PSE for bit testing", inline=True)
comment(0x826D, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x826F, "Write CR1: disable all interrupts", inline=True)
comment(0x8272, "Save Y (byte count from data RX loop)", inline=True)
comment(0x8274, "A=&02: FV mask", inline=True)
comment(0x8276, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x8279, "No FV -- error", inline=True)
comment(0x827B, "FV set, no RDA -- proceed to ACK", inline=True)
comment(0x827D, "Check if buffer space remains", inline=True)
comment(0x827F, "No buffer space: error/discard frame", inline=True)
comment(0x8281, "FV+RDA: read and store last data byte", inline=True)
comment(0x8284, "Y = current buffer write offset", inline=True)
comment(0x8286, "Store last byte in port receive buffer", inline=True)
comment(0x8288, "Advance buffer write offset", inline=True)
comment(0x828A, "No page wrap: proceed to send ACK", inline=True)
comment(0x828C, "Page boundary: advance buffer page", inline=True)
comment(0x828E, "Send ACK frame to complete handshake", inline=True)
comment(0x8291, "Read SR2 for Tube data receive path", inline=True)
comment(0x8294, "RDA clear: no more data, frame complete", inline=True)
comment(0x8296, "Read data byte from ADLC RX FIFO", inline=True)
comment(0x8299, "Check buffer limits and transfer size", inline=True)
comment(0x829C, "Zero: buffer full, handle as error", inline=True)
comment(0x829E, "Send byte to Tube data register 3", inline=True)
comment(0x82A1, "Read second data byte (paired transfer)", inline=True)
comment(0x82A4, "Send second byte to Tube", inline=True)
comment(0x82A7, "Check limits after byte pair", inline=True)
comment(0x82AA, "Zero: Tube transfer complete", inline=True)
comment(0x82AC, "Re-read SR2 for next byte pair", inline=True)
comment(0x82AF, "More data available: continue loop", inline=True)
comment(0x82B1, "Unexpected end: return from NMI", inline=True)
comment(0x82B4, "CR1=&00: disable all interrupts", inline=True)
comment(0x82B6, "Write CR1 for individual bit testing", inline=True)
comment(0x82B9, "CR2=&84: disable PSE", inline=True)
comment(0x82BB, "Write CR2: same pattern as main path", inline=True)
comment(0x82BE, "A=&02: FV mask for Tube completion", inline=True)
comment(0x82C0, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x82C3, "No FV: incomplete frame, error", inline=True)
comment(0x82C5, "FV set, no RDA: proceed to ACK", inline=True)
comment(0x82C7, "Check if any buffer was allocated", inline=True)
comment(0x82C9, "OR all 4 buffer pointer bytes together", inline=True)
comment(0x82CB, "Check buffer low byte", inline=True)
comment(0x82CD, "Check buffer high byte", inline=True)
comment(0x82CF, "All zero (null buffer): error", inline=True)
comment(0x82D1, "Read extra trailing byte from FIFO", inline=True)
comment(0x82D4, "Save extra byte at &0D5D for later use", inline=True)
comment(0x82D7, "Bit5 = extra data byte available flag", inline=True)
comment(0x82D9, "Set extra byte flag in tx_flags", inline=True)
comment(0x82DC, "Store updated flags", inline=True)
comment(0x82DF, "Load TX flags to check ACK type", inline=True)
comment(0x82E2, "Bit7 clear: normal scout ACK", inline=True)
comment(0x82E4, "Final ACK: call completion handler", inline=True)
comment(0x82E7, "Jump to TX success result", inline=True)
comment(0x82EA, "CR1=&44: RX_RESET | TIE (switch to TX mode)", inline=True)
comment(0x82EC, "Write CR1: switch to TX mode", inline=True)
comment(0x82EF, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x82F1, "Write CR2: enable TX with status clear", inline=True)
comment(0x82F4, "Install saved next handler (&8396 for scout ACK)", inline=True)
comment(0x82F6, "High byte of post-ACK handler", inline=True)
comment(0x82F8, "Store next handler low byte", inline=True)
comment(0x82FB, "Store next handler high byte", inline=True)
comment(0x82FE, "Load dest station from RX scout buffer", inline=True)
comment(0x8301, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x8304, "TDRA not ready -- error", inline=True)
comment(0x8306, "Write dest station to TX FIFO", inline=True)
comment(0x8309, "Write dest network to TX FIFO", inline=True)
comment(0x830C, "Write dest net byte to FIFO", inline=True)
comment(0x830F, "Install handler at &8326 (write src addr)", inline=True)
comment(0x8311, "High byte of nmi_ack_tx_src", inline=True)
comment(0x8313, "Set NMI vector to ack_tx_src handler", inline=True)
comment(0x8316, "Load our station ID (also INTOFF)", inline=True)
comment(0x8319, "BIT SR1: test TDRA", inline=True)
comment(0x831C, "TDRA not ready -- error", inline=True)
comment(0x831E, "Write our station to TX FIFO", inline=True)
comment(0x8321, "Write network=0 to TX FIFO", inline=True)
comment(0x8323, "Write network=0 (local) to TX FIFO", inline=True)
comment(0x8326, "Check tx_flags for data phase", inline=True)
comment(0x8329, "bit7 set: start data TX phase", inline=True)
comment(0x832B, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x832D, "Write CR2 to clear status after ACK TX", inline=True)
comment(0x8330, "Install saved handler from &0D4B/&0D4C", inline=True)
comment(0x8333, "Load saved next handler high byte", inline=True)
comment(0x8336, "Install next NMI handler", inline=True)
comment(0x8339, "Jump to start data TX phase", inline=True)
comment(0x833C, "Jump to error handler", inline=True)
comment(0x833F, "A=2: test bit1 of tx_flags", inline=True)
comment(0x8341, "BIT tx_flags: check data transfer bit", inline=True)
comment(0x8344, "Bit1 clear: no transfer -- return", inline=True)
comment(0x8346, "CLC: init carry for 4-byte add", inline=True)
comment(0x8347, "Save carry on stack for loop", inline=True)
comment(0x8348, "Y=8: RXCB high pointer offset", inline=True)
comment(0x834A, "Load RXCB[Y] (buffer pointer byte)", inline=True)
comment(0x834C, "Restore carry from stack", inline=True)
comment(0x834D, "Add transfer count byte", inline=True)
comment(0x8350, "Store updated pointer back to RXCB", inline=True)
comment(0x8352, "Next byte", inline=True)
comment(0x8353, "Save carry for next iteration", inline=True)
comment(0x8354, "Done 4 bytes? (Y reaches &0C)", inline=True)
comment(0x8356, "No: continue adding", inline=True)
comment(0x8358, "Discard final carry", inline=True)
comment(0x8359, "A=&20: test bit5 of tx_flags", inline=True)
comment(0x835B, "BIT tx_flags: check Tube bit", inline=True)
comment(0x835E, "No Tube: skip Tube update", inline=True)
comment(0x8360, "Save X on stack", inline=True)
comment(0x8361, "Push X", inline=True)
comment(0x8362, "A=8: offset for Tube address", inline=True)
comment(0x8364, "CLC for address calculation", inline=True)
comment(0x8365, "Add workspace base offset", inline=True)
comment(0x8367, "X = address low for Tube claim", inline=True)
comment(0x8368, "Y = address high for Tube claim", inline=True)
comment(0x836A, "A=1: Tube claim type (read)", inline=True)
comment(0x836C, "Claim Tube address for transfer", inline=True)
comment(0x836F, "Load extra RX data byte", inline=True)
comment(0x8372, "Send to Tube via R3", inline=True)
comment(0x8375, "SEC: init carry for increment", inline=True)
comment(0x8376, "Y=8: start at high pointer", inline=True)
comment(0x8378, "A=0: add carry only (increment)", inline=True)
comment(0x837A, "Add carry to pointer byte", inline=True)
comment(0x837C, "Store back to RXCB", inline=True)
comment(0x837E, "Next byte", inline=True)
comment(0x837F, "Keep going while carry propagates", inline=True)
comment(0x8381, "Restore X from stack", inline=True)
comment(0x8382, "Transfer to X register", inline=True)
comment(0x8383, "A=&FF: return value (transfer done)", inline=True)
comment(0x8385, "Return", inline=True)
comment(0x8386, "Load received port byte", inline=True)
comment(0x8389, "Port != 0: data transfer frame", inline=True)
comment(0x838B, "Port=0: load control byte", inline=True)
comment(0x838E, "Ctrl = &82 (POKE)?", inline=True)
comment(0x8390, "Yes: POKE also needs data transfer", inline=True)
comment(0x8392, "Other port-0 ops: immediate dispatch", inline=True)
comment(0x8395, "Update buffer pointer and check for Tube", inline=True)
comment(0x8398, "Transfer not done: skip buffer update", inline=True)
comment(0x839A, "Load buffer bytes remaining", inline=True)
comment(0x839C, "CLC for address add", inline=True)
comment(0x839D, "Add to buffer base address", inline=True)
comment(0x839F, "No carry: skip high byte increment", inline=True)
comment(0x83A1, "Carry: increment buffer high byte", inline=True)
comment(0x83A3, "Y=8: store updated buffer position", inline=True)
comment(0x83A5, "Store updated low byte to RXCB", inline=True)
comment(0x83A7, "Y=9: buffer high byte offset", inline=True)
comment(0x83A8, "Load updated buffer high byte", inline=True)
comment(0x83AA, "Store high byte to RXCB", inline=True)
comment(0x83AC, "Check port byte again", inline=True)
comment(0x83AF, "Port=0: immediate op, discard+listen", inline=True)
comment(0x83B1, "Load source network from scout buffer", inline=True)
comment(0x83B4, "Y=3: RXCB source network offset", inline=True)
comment(0x83B6, "Store source network to RXCB", inline=True)
comment(0x83B8, "Y=2: source station offset", inline=True)
comment(0x83B9, "Load source station from scout buffer", inline=True)
comment(0x83BC, "Store source station to RXCB", inline=True)
comment(0x83BE, "Y=1: port byte offset", inline=True)
comment(0x83BF, "Load port byte", inline=True)
comment(0x83C2, "Store port to RXCB", inline=True)
comment(0x83C4, "Y=0: control/flag byte offset", inline=True)
comment(0x83C5, "Load control byte from scout", inline=True)
comment(0x83C8, "Set bit7: signals wait_net_tx_ack that reply arrived", inline=True)
comment(0x83CA, "Store to RXCB byte 0 (bit 7 set = complete)", inline=True)
comment(0x83CC, "Load callback event flags", inline=True)
comment(0x83CF, "Shift bit 0 into carry", inline=True)
comment(0x83D0, "Bit 0 clear: no callback, skip to reset", inline=True)
comment(0x83D2, "Set carry for subtraction", inline=True)
comment(0x83D2, "Load RXCB workspace pointer low byte", inline=True)
comment(0x83D4, "Count slots", inline=True)
comment(0x83D5, "Subtract 12 bytes per RXCB slot", inline=True)
comment(0x83D7, "Loop until pointer exhausted", inline=True)
comment(0x83D9, "Adjust for off-by-one", inline=True)
comment(0x83DA, "Check slot index >= 3", inline=True)
comment(0x83DC, "Slot < 3: no callback, skip to reset", inline=True)
comment(0x83DE, "Discard scout and reset listen state", inline=True)
comment(0x83E1, "Pass slot index as callback parameter", inline=True)
comment(0x83E2, "Jump to TX completion with slot index", inline=True)
comment(0x83E5, "Discard scout and reset RX listen", inline=True)
comment(0x83E8, "Reset ADLC and return to RX listen", inline=True)
comment(0x83EB, "A=&BE: low byte of nmi_rx_scout", inline=True)
comment(0x83ED, "Y=&80: high byte of nmi_rx_scout", inline=True)
comment(0x83EF, "Install nmi_rx_scout as NMI handler", inline=True)
comment(0x83F2, "Tube flag bit 1 AND tx_flags bit 1", inline=True)
comment(0x83F4, "Check if Tube transfer active", inline=True)
comment(0x83F7, "Test tx_flags for Tube transfer", inline=True)
comment(0x83FA, "No Tube transfer active -- skip release", inline=True)
comment(0x83FC, "Release Tube claim before discarding", inline=True)
comment(0x83FF, "Return", inline=True)
comment(0x8400, "Save X on stack", inline=True)
comment(0x8401, "Push X", inline=True)
comment(0x8402, "X=4: start at scout byte offset 4", inline=True)
comment(0x8404, "A=2: Tube transfer check mask", inline=True)
comment(0x8406, "BIT tx_flags: check Tube bit", inline=True)
comment(0x8409, "Tube active: use R3 write path", inline=True)
comment(0x8414, "Y = current buffer position", inline=True)
comment(0x8416, "Load scout data byte", inline=True)
comment(0x8419, "Store to port buffer", inline=True)
comment(0x841B, "Advance buffer pointer", inline=True)
comment(0x841C, "No page crossing", inline=True)
comment(0x841E, "Page crossing: inc buffer high byte", inline=True)
comment(0x8420, "Decrement remaining page count", inline=True)
comment(0x8422, "No pages left: overflow", inline=True)
comment(0x8424, "Next scout data byte", inline=True)
comment(0x8425, "Save updated buffer position", inline=True)
comment(0x8427, "Done all scout data? (X reaches &0C)", inline=True)
comment(0x8429, "No: continue copying", inline=True)
comment(0x842B, "Restore X from stack", inline=True)
comment(0x8430, "Transfer to X register", inline=True)
comment(0x8431, "Jump to completion handler", inline=True)
comment(0x8436, "Tube path: load scout data byte", inline=True)
comment(0x8439, "Send byte to Tube via R3", inline=True)
comment(0x843C, "Increment buffer position counters", inline=True)
comment(0x843F, "Counter overflow: handle end of buffer", inline=True)
comment(0x8441, "Next scout data byte", inline=True)
comment(0x8442, "Done all scout data?", inline=True)
comment(0x8444, "No: continue Tube writes", inline=True)
comment(0x8448, "Check if Tube needs releasing", inline=True)
comment(0x844A, "Bit7 set: already released", inline=True)
comment(0x844C, "A=&82: Tube release claim type", inline=True)
comment(0x844E, "Release Tube address claim", inline=True)
comment(0x8451, "Clear release flag (LSR clears bit7)", inline=True)
comment(0x8453, "Return", inline=True)
comment(0x8454, "Control byte &81-&88 range check", inline=True)
comment(0x8457, "Below &81: not an immediate op", inline=True)
comment(0x8459, "Out of range low: jump to discard", inline=True)
comment(0x845B, "Above &88: not an immediate op", inline=True)
comment(0x845D, "Out of range high: jump to discard", inline=True)
comment(0x845F, "HALT(&87)/CONTINUE(&88) skip protection", inline=True)
comment(0x8461, "Ctrl >= &87: dispatch without mask check", inline=True)
comment(0x8463, "Convert ctrl byte to 0-based index for mask", inline=True)
comment(0x8464, "SEC for subtract", inline=True)
comment(0x8465, "A = ctrl - &81 (0-based operation index)", inline=True)
comment(0x8467, "Y = index for mask rotation count", inline=True)
comment(0x8468, "Load protection mask from LSTAT", inline=True)
comment(0x846B, "Rotate mask right by control byte index", inline=True)
comment(0x846C, "Decrement rotation counter", inline=True)
comment(0x846D, "Loop until bit aligned", inline=True)
comment(0x846F, "Bit set = operation disabled, discard", inline=True)
comment(0x8471, "Reload ctrl byte for dispatch table", inline=True)
comment(0x8474, "Hi byte: all handlers are in page &84", inline=True)
comment(0x8476, "Push hi byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x8477, "Load handler low byte from jump table", inline=True)
comment(0x847A, "Push handler low byte", inline=True)
comment(0x847B, "RTS dispatches to handler", inline=True)
comment(0x847C, "Increment port buffer length", inline=True)
comment(0x8482, "Check if scout data index reached 11", inline=True)
comment(0x8484, "Yes: loop back to continue reading", inline=True)
comment(0x8486, "Restore A from stack", inline=True)
comment(0x8487, "Transfer to X", inline=True)
comment(0x8488, "Jump to discard handler", inline=True)
comment(0x8493, "A=0: port buffer lo at page boundary", inline=True)
comment(0x8495, "Set port buffer lo", inline=True)
comment(0x8497, "Buffer length lo = &82", inline=True)
comment(0x8499, "Set buffer length lo", inline=True)
comment(0x849B, "Buffer length hi = 1", inline=True)
comment(0x849D, "Set buffer length hi", inline=True)
comment(0x849F, "Load RX page hi for buffer", inline=True)
comment(0x84A1, "Set port buffer hi", inline=True)
comment(0x84A3, "Y=1: copy 2 bytes (1 down to 0)", inline=True)
comment(0x84A5, "Load remote address byte", inline=True)
comment(0x84A8, "Store to exec address workspace", inline=True)
comment(0x84AB, "Next byte (descending)", inline=True)
comment(0x84AC, "Loop until all 4 bytes copied", inline=True)
comment(0x84AE, "Enter common data-receive path", inline=True)
comment(0x84B1, "Port workspace offset = &3D", inline=True)
comment(0x84B3, "Store workspace offset lo", inline=True)
comment(0x84B5, "RX buffer page = &0D", inline=True)
comment(0x84B7, "Store workspace offset hi", inline=True)
comment(0x84B9, "Enter POKE data-receive path", inline=True)
comment(0x84BC, "Buffer length hi = 1", inline=True)
comment(0x84BE, "Set buffer length hi", inline=True)
comment(0x84C0, "Buffer length lo = &FC", inline=True)
comment(0x84C2, "Set buffer length lo", inline=True)
comment(0x84C4, "Buffer start lo = &25", inline=True)
comment(0x84C6, "Set port buffer lo", inline=True)
comment(0x84C8, "Buffer hi = &7F (below screen)", inline=True)
comment(0x84CA, "Set port buffer hi", inline=True)
comment(0x84CE, "Port workspace offset = &3D", inline=True)
comment(0x84D0, "Store workspace offset lo", inline=True)
comment(0x84D2, "RX buffer page = &0D", inline=True)
comment(0x84D4, "Store workspace offset hi", inline=True)
comment(0x84D6, "Scout status = 2 (PEEK response)", inline=True)
comment(0x84D8, "Store scout status", inline=True)
comment(0x84DB, "Calculate transfer size for response", inline=True)
comment(0x84DE, "C=0: transfer not set up, discard", inline=True)
comment(0x84E0, "Mark TX flags bit 7 (reply pending)", inline=True)
comment(0x84E3, "Set reply pending flag", inline=True)
comment(0x84E5, "Store updated TX flags", inline=True)
comment(0x84E8, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
comment(0x84EA, "Write CR1: enable TX interrupts", inline=True)
comment(0x84ED, "CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE", inline=True)
comment(0x84EF, "Write CR2 for TX setup", inline=True)
comment(0x84F2, "NMI handler lo byte (self-modifying)", inline=True)
comment(0x84F4, "Y=&85: NMI handler high byte", inline=True)
comment(0x84F6, "Acknowledge and write TX dest", inline=True)
comment(0x84F9, "Get buffer position for reply header", inline=True)
comment(0x84FB, "Clear carry for offset addition", inline=True)
comment(0x84FC, "Data offset = buf_len + &80 (past header)", inline=True)
comment(0x84FE, "Y=&7F: reply data length slot", inline=True)
comment(0x8500, "Store reply data length in RX buffer", inline=True)
comment(0x8502, "Y=&80: source station slot", inline=True)
comment(0x8504, "Load requesting station number", inline=True)
comment(0x8507, "Store source station in reply header", inline=True)
comment(0x850A, "Load requesting network number", inline=True)
comment(0x850D, "Store source network in reply header", inline=True)
comment(0x850F, "Load control byte from received frame", inline=True)
comment(0x8512, "Save TX operation type for SR dispatch", inline=True)
# UNMAPPED: comment(0x8512, "IER bit 2: disable SR interrupt", inline=True)
comment(0x851C, "Write IER to disable SR", inline=True)
# UNMAPPED: comment(0x8517, "Read ACR for shift register config", inline=True)
# UNMAPPED: comment(0x851A, "Isolate shift register mode bits (2-4)", inline=True)
# UNMAPPED: comment(0x851C, "Save original SR mode for later restore", inline=True)
# UNMAPPED: comment(0x851F, "Reload ACR for modification", inline=True)
# UNMAPPED: comment(0x8522, "Clear SR mode bits (keep other bits)", inline=True)
comment(0x851F, "SR mode 2: shift in under φ2", inline=True)
comment(0x8521, "Apply new shift register mode", inline=True)
# UNMAPPED: comment(0x8529, "Read SR to clear pending interrupt", inline=True)
comment(0x8529, "Return to idle listen mode", inline=True)
comment(0x852C, "Increment buffer length low byte", inline=True)
comment(0x852E, "No overflow: done", inline=True)
comment(0x8530, "Increment buffer length high byte", inline=True)
comment(0x8532, "No overflow: done", inline=True)
comment(0x8534, "Increment buffer pointer low byte", inline=True)
comment(0x8536, "No overflow: done", inline=True)
comment(0x8538, "Increment buffer pointer high byte", inline=True)
comment(0x853A, "Return", inline=True)
# UNMAPPED: comment(0x8543, "Hi byte of tx_done_exit-1", inline=True)
comment(0x8542, "Push hi byte on stack", inline=True)
comment(0x8543, "Push lo of (tx_done_exit-1)", inline=True)
comment(0x8545, "Push lo byte on stack", inline=True)
comment(0x8546, "Call remote JSR; RTS to tx_done_exit", inline=True)

# tx_done_dispatch_lo (&8534): 5-byte dispatch table.
# Low bytes of PHA/PHA/RTS targets for TX operation types &83-&87.
# Read by LDA set_rx_buf_len_hi,Y at &8064 (hi byte always &85).
# UNMAPPED: comment(0x853E, "TX done dispatch table (lo bytes)\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "Low bytes of PHA/PHA/RTS dispatch targets for TX\n"
# UNMAPPED:     "operation types &83-&87. Read by the dispatch at\n"
# UNMAPPED:     "&8064 via LDA set_rx_buf_len_hi,Y (base &84BB\n"
# UNMAPPED:     "+ Y). High byte is always &85, so targets are\n"
# UNMAPPED:     "&85xx+1. Entries for Y < &83 read from preceding\n"
# UNMAPPED:     "code bytes and are not valid operation types.")

# tx_done_econet_event (&8542): TX operation type &84 handler.
comment(0x8549, "X = remote address lo from l0d66", inline=True)
comment(0x854C, "A = remote address hi from l0d67", inline=True)
comment(0x854F, "Y = 8: Econet event number", inline=True)

comment(0x8554, "Exit TX done handler", inline=True)
comment(0x8557, "X = remote address lo", inline=True)
comment(0x855A, "Y = remote address hi", inline=True)
comment(0x855D, "Call ROM entry point at &8000", inline=True)
comment(0x8560, "Exit TX done handler", inline=True)
comment(0x8563, "A=&04: bit 2 mask for rx_flags", inline=True)
comment(0x8565, "Test if already halted", inline=True)
comment(0x8568, "Already halted: skip to exit", inline=True)
comment(0x856A, "Set bit 2 in rx_flags", inline=True)
comment(0x856D, "Store halt flag", inline=True)
comment(0x8570, "A=4: re-load halt bit mask", inline=True)
comment(0x8572, "Enable interrupts during halt wait", inline=True)
comment(0x8573, "Test halt flag", inline=True)
comment(0x8576, "Still halted: keep spinning", inline=True)
comment(0x857A, "Load current RX flags", inline=True)
comment(0x857D, "Clear bit 2: release halted station", inline=True)
comment(0x857F, "Store updated flags", inline=True)
comment(0x8582, "Restore Y from stack", inline=True)
comment(0x8583, "Transfer to Y register", inline=True)
comment(0x8584, "Restore X from stack", inline=True)
comment(0x8585, "Transfer to X register", inline=True)
comment(0x8586, "A=0: success status", inline=True)
comment(0x8588, "Return with A=0 (success)", inline=True)
comment(0x8589, "Save X on stack", inline=True)
comment(0x858A, "Push X", inline=True)
comment(0x858B, "Y=2: TXCB offset for dest station", inline=True)
comment(0x858D, "Load dest station from TX control block", inline=True)
comment(0x858F, "Store to TX scout buffer", inline=True)
comment(0x8593, "Load dest network from TX control block", inline=True)
comment(0x8595, "Store to TX scout buffer", inline=True)
comment(0x8598, "Y=0: first byte of TX control block", inline=True)
comment(0x859A, "Load control/flag byte", inline=True)
comment(0x859C, "Bit7 set: immediate operation ctrl byte", inline=True)
comment(0x859E, "Bit7 clear: normal data transfer", inline=True)
comment(0x85A1, "Store control byte to TX scout buffer", inline=True)
comment(0x85A4, "X = control byte for range checks", inline=True)
comment(0x85A5, "Y=1: port byte offset", inline=True)
comment(0x85A6, "Load port byte from TX control block", inline=True)
comment(0x85A8, "Store port byte to TX scout buffer", inline=True)
comment(0x85AB, "Port != 0: skip immediate op setup", inline=True)
comment(0x85AD, "Ctrl < &83: PEEK/POKE need address calc", inline=True)
comment(0x85AF, "Ctrl >= &83: skip to range check", inline=True)
comment(0x85B1, "SEC: init borrow for 4-byte subtract", inline=True)
comment(0x85B2, "Save carry on stack for loop", inline=True)
comment(0x85B3, "Y=8: high pointer offset in TXCB", inline=True)
comment(0x85B5, "Load TXCB[Y] (end addr byte)", inline=True)
comment(0x85B7, "Y -= 4: back to start addr offset", inline=True)
comment(0x85B8, "(continued)", inline=True)
comment(0x85B9, "(continued)", inline=True)
comment(0x85BA, "(continued)", inline=True)
comment(0x85BB, "Restore borrow from stack", inline=True)
comment(0x85BC, "end - start = transfer size byte", inline=True)
comment(0x85BE, "Store result to tx_data_start", inline=True)
comment(0x85C1, "Y += 5: advance to next end byte", inline=True)
comment(0x85C2, "(continued)", inline=True)
comment(0x85C3, "(continued)", inline=True)
comment(0x85C4, "(continued)", inline=True)
comment(0x85C5, "(continued)", inline=True)
comment(0x85C6, "Save borrow for next byte", inline=True)
comment(0x85C7, "Done all 4 bytes? (Y reaches &0C)", inline=True)
comment(0x85C9, "No: next byte pair", inline=True)
comment(0x85CB, "Discard final borrow", inline=True)
comment(0x85CC, "Ctrl < &81: not an immediate op", inline=True)
comment(0x85CE, "Below range: normal data transfer", inline=True)
comment(0x85D0, "Ctrl >= &89: out of immediate range", inline=True)
comment(0x85D2, "Above range: normal data transfer", inline=True)
comment(0x85D4, "Y=&0C: start of extra data in TXCB", inline=True)
comment(0x85D6, "Load extra parameter byte from TXCB", inline=True)
comment(0x85D8, "Copy to NMI shim workspace at &0D1A+Y", inline=True)
comment(0x85DB, "Next byte", inline=True)
comment(0x85DC, "Done 4 bytes? (Y reaches &10)", inline=True)
comment(0x85DE, "No: continue copying", inline=True)
comment(0x85E0, "A=&20: mask for SR2 INACTIVE bit", inline=True)
comment(0x85E2, "BIT SR2: test if line is idle", inline=True)
comment(0x85E5, "Line not idle: handle as line jammed", inline=True)
comment(0x85E7, "A=&FD: high byte of timeout counter", inline=True)
comment(0x85E9, "Push timeout high byte to stack", inline=True)
comment(0x85EA, "Scout frame = 6 address+ctrl bytes", inline=True)
comment(0x85EC, "Store scout frame length", inline=True)
comment(0x85EF, "A=0: init low byte of timeout counter", inline=True)
comment(0x85F1, "Save TX index", inline=True)
comment(0x85F4, "Push timeout byte 1 on stack", inline=True)
comment(0x85F5, "Push timeout byte 2 on stack", inline=True)
comment(0x85F6, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x85F8, "A=&04: INACTIVE bit mask for SR2 test", inline=True)
comment(0x85FA, "Save interrupt state", inline=True)
comment(0x85FB, "Disable interrupts for ADLC access", inline=True)
comment(0x85FC, "INTOFF -- disable NMIs", inline=True)
comment(0x85FF, "INTOFF again (belt-and-braces)", inline=True)
comment(0x8602, "BIT SR2: Z = &04 AND SR2 -- tests INACTIVE", inline=True)
comment(0x8605, "INACTIVE not set -- re-enable NMIs and loop", inline=True)
comment(0x8607, "Read SR1 (acknowledge pending interrupt)", inline=True)
comment(0x860A, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x860C, "Write CR2: clear status, prepare TX", inline=True)
comment(0x860F, "A=&10: CTS mask for SR1 bit4", inline=True)
comment(0x8611, "BIT SR1: tests CTS present", inline=True)
comment(0x8614, "CTS set -- clock hardware detected, start TX", inline=True)
comment(0x8616, "INTON -- re-enable NMIs (&FE20 read)", inline=True)
comment(0x8619, "Restore interrupt state", inline=True)
comment(0x861A, "3-byte timeout counter on stack", inline=True)
comment(0x861B, "Increment timeout counter byte 1", inline=True)
comment(0x861E, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x8620, "Increment timeout counter byte 2", inline=True)
comment(0x8623, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x8625, "Increment timeout counter byte 3", inline=True)
comment(0x8628, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x862C, "Error &44: control byte out of valid range", inline=True)
comment(0x8630, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", inline=True)
comment(0x8632, "Write CR2 to abort TX", inline=True)
comment(0x8635, "Clean 3 bytes of timeout loop state", inline=True)
comment(0x8636, "Pop saved register", inline=True)
comment(0x8637, "Pop saved register", inline=True)
comment(0x8638, "Error &40 = 'Line Jammed'", inline=True)
comment(0x863A, "ALWAYS branch to shared error handler", inline=True)
comment(0x863C, "Error &43 = 'No Clock'", inline=True)
comment(0x863E, "Offset 0 = error byte in TX control block", inline=True)
comment(0x8640, "Store error code in TX CB byte 0", inline=True)
comment(0x8642, "&80 = TX complete flag", inline=True)
comment(0x8644, "Signal TX operation complete", inline=True)
comment(0x8647, "Restore X saved by caller", inline=True)
comment(0x8648, "Move to X register", inline=True)
comment(0x8649, "Return to TX caller", inline=True)
comment(0x864A, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x864D, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", inline=True)
comment(0x864F, "Write to ADLC CR1", inline=True)
comment(0x8652, "Install NMI handler at &86E0 (TX data handler)", inline=True)
comment(0x8654, "High byte of NMI handler address", inline=True)
comment(0x8656, "Write NMI vector low byte directly", inline=True)
comment(0x8659, "Write NMI vector high byte directly", inline=True)
comment(0x865C, "Set need_release_tube flag (SEC/ROR = bit7)", inline=True)
comment(0x865D, "Rotate carry into bit 7 of flag", inline=True)
comment(0x865F, "INTON -- NMIs now fire for TDRA (&FE20 read)", inline=True)
comment(0x8662, "Load destination port number", inline=True)
comment(0x8665, "Port != 0: standard data transfer", inline=True)
comment(0x8667, "Port 0: load control byte for table lookup", inline=True)
comment(0x866A, "Look up tx_flags from table", inline=True)
comment(0x866D, "Store operation flags", inline=True)
comment(0x8670, "Look up tx_length from table", inline=True)
comment(0x8673, "Store expected transfer length", inline=True)
comment(0x8676, "Push high byte of return address (&9C)", inline=True)
comment(0x8678, "Push high byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x8679, "Look up handler address low from table", inline=True)
comment(0x867C, "Push low byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x867D, "RTS dispatches to control-byte handler", inline=True)

# tx_ctrl_dispatch_lo (&8677): 8-byte dispatch table.
# Low bytes of PHA/PHA/RTS targets for TX control byte handlers
# &81-&88. Read by LDA intoff_disable_nmi_op,Y at &867C (base
# intoff_test_inactive+1 + Y). High byte always &86, targets are &86xx+1.
# The last entry (&88) dispatches to tx_ctrl_machine_type at
# &867F, which is the 4 bytes immediately after the table.
# UNMAPPED: comment(0x8681, "TX ctrl dispatch table (lo bytes)\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "Low bytes of PHA/PHA/RTS dispatch targets for TX\n"
# UNMAPPED:     "control byte types &81-&88. Read by the dispatch\n"
# UNMAPPED:     "at &867C via LDA intoff_disable_nmi_op,Y (base\n"
# UNMAPPED:     "intoff_test_inactive+1). High byte is always &86,\n"
# UNMAPPED:     "so targets are &86xx+1. Last entry dispatches to\n"
# UNMAPPED:     "tx_ctrl_machine_type at &867F, immediately after\n"
# UNMAPPED:     "the table.")
# UNMAPPED: comment(0x8689, "scout_status=3 (machine type query)", inline=True)
comment(0x8688, "Skip address addition, store status", inline=True)
comment(0x868A, "A=3: scout_status for PEEK op", inline=True)
comment(0x868E, "Scout status = 2 (POKE transfer)", inline=True)
comment(0x8690, "Store scout status", inline=True)
comment(0x8693, "Clear carry for 4-byte addition", inline=True)
comment(0x8694, "Save carry on stack", inline=True)
comment(0x8695, "Y=&0C: start at offset 12", inline=True)
comment(0x8697, "Load workspace address byte", inline=True)
comment(0x869A, "Restore carry from previous byte", inline=True)
comment(0x869B, "Add TXCB address byte", inline=True)
comment(0x869D, "Store updated address byte", inline=True)
comment(0x86A0, "Next byte", inline=True)
comment(0x86A1, "Save carry for next addition", inline=True)
comment(0x86A2, "Compare Y with 16-byte boundary", inline=True)
comment(0x86A4, "Below boundary: continue addition", inline=True)
comment(0x86A6, "Restore processor flags", inline=True)
comment(0x86A7, "Skip buffer setup if transfer size is zero", inline=True)
comment(0x86A9, "Load dest station for broadcast check", inline=True)
comment(0x86AC, "AND with dest network", inline=True)
comment(0x86AF, "Both &FF = broadcast address?", inline=True)
comment(0x86B1, "Not broadcast: unicast path", inline=True)
comment(0x86B3, "Broadcast scout: 14 bytes total", inline=True)
comment(0x86B5, "Store broadcast scout length", inline=True)
comment(0x86B8, "A=&40: broadcast flag", inline=True)
comment(0x86BA, "Set broadcast flag in tx_flags", inline=True)
comment(0x86BD, "Y=4: start of address data in TXCB", inline=True)
comment(0x86BF, "Copy TXCB address bytes to scout buffer", inline=True)
comment(0x86C1, "Store to TX source/data area", inline=True)
comment(0x86C4, "Next byte", inline=True)
comment(0x86C5, "Done 8 bytes? (Y reaches &0C)", inline=True)
comment(0x86C7, "No: continue copying", inline=True)
comment(0x86CB, "A=0: clear flags for unicast", inline=True)
comment(0x86CD, "Clear tx_flags", inline=True)
comment(0x86D0, "scout_status=2: data transfer pending", inline=True)
comment(0x86D2, "Store scout status", inline=True)
comment(0x86D5, "Copy TX block pointer to workspace ptr", inline=True)
comment(0x86D7, "Store low byte", inline=True)
comment(0x86D9, "Copy TX block pointer high byte", inline=True)
comment(0x86DB, "Store high byte", inline=True)
comment(0x86DD, "Calculate transfer size from RXCB", inline=True)
comment(0x86E0, "Restore processor status from stack", inline=True)
comment(0x86E1, "Restore stacked registers (4 PLAs)", inline=True)
comment(0x86E2, "Second PLA", inline=True)
comment(0x86E3, "Third PLA", inline=True)
comment(0x86E4, "Fourth PLA", inline=True)
comment(0x86E5, "Restore X from A", inline=True)
comment(0x86E6, "Return to caller", inline=True)
comment(0x86E7, "Load TX buffer index", inline=True)
comment(0x86EA, "BIT SR1: V=bit6(TDRA), N=bit7(IRQ)", inline=True)
comment(0x86ED, "TDRA not set -- TX error", inline=True)
comment(0x86EF, "Load byte from TX buffer", inline=True)
comment(0x86F2, "Write to TX_DATA (continue frame)", inline=True)
comment(0x86F5, "Next TX buffer byte", inline=True)
comment(0x86F6, "Load second byte from TX buffer", inline=True)
comment(0x86F9, "Advance TX index past second byte", inline=True)
comment(0x86FA, "Save updated TX buffer index", inline=True)
comment(0x86FD, "Write second byte to TX_DATA", inline=True)
comment(0x8700, "Compare index to TX length", inline=True)
comment(0x8703, "Frame complete -- go to TX_LAST_DATA", inline=True)
comment(0x8705, "Check if we can send another pair", inline=True)
comment(0x8708, "IRQ set -- send 2 more bytes (tight loop)", inline=True)
comment(0x870A, "RTI -- wait for next NMI", inline=True)
comment(0x870D, "Error &42", inline=True)
comment(0x8711, "CR2=&67: clear status, return to listen", inline=True)
comment(0x8713, "Write CR2: clear status, idle listen", inline=True)
comment(0x8716, "Error &41 (TDRA not ready)", inline=True)
comment(0x8718, "INTOFF (also loads station ID)", inline=True)
comment(0x871B, "PHA/PLA delay loop (256 iterations for NMI disable)", inline=True)
comment(0x871C, "PHA/PLA delay (~7 cycles each)", inline=True)
comment(0x871D, "Increment delay counter", inline=True)
comment(0x871E, "Loop 256 times for NMI disable", inline=True)
comment(0x8720, "Store error and return to idle", inline=True)
comment(0x8723, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x8725, "Write to ADLC CR2", inline=True)
comment(0x8728, "Install NMI handler at &8728 (TX completion)", inline=True)
comment(0x872A, "High byte of handler address", inline=True)
comment(0x872C, "Install and return via set_nmi_vector", inline=True)
comment(0x872F, "Jump to error handler", inline=True)
comment(0x8731, "Write CR1 to switch from TX to RX", inline=True)
comment(0x8734, "Test workspace flags", inline=True)
comment(0x8737, "bit6 not set -- check bit0", inline=True)
comment(0x8739, "bit6 set -- TX completion", inline=True)
comment(0x873C, "A=1: mask for bit0 test", inline=True)
comment(0x873E, "Test tx_flags bit0 (handshake)", inline=True)
comment(0x8741, "bit0 clear: install reply handler", inline=True)
comment(0x8743, "bit0 set -- four-way handshake data phase", inline=True)
comment(0x8746, "Install RX reply handler at &8744", inline=True)
comment(0x8748, "Install handler and RTI", inline=True)
comment(0x874B, "A=&01: AP mask for SR2", inline=True)
comment(0x874D, "BIT SR2: test AP (Address Present)", inline=True)
comment(0x8750, "No AP -- error", inline=True)
comment(0x8752, "Read first RX byte (destination station)", inline=True)
comment(0x8755, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x8758, "Not our station -- error/reject", inline=True)
comment(0x875A, "Install next handler at &8758 (reply continuation)", inline=True)
comment(0x875C, "Install continuation handler", inline=True)
comment(0x875F, "Read RX byte (destination station)", inline=True)
comment(0x8762, "No RDA -- error", inline=True)
comment(0x8764, "Read destination network byte", inline=True)
comment(0x8767, "Non-zero -- network mismatch, error", inline=True)
comment(0x8769, "Install next handler at &8779 (reply validation)", inline=True)
comment(0x876B, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
comment(0x876E, "IRQ set -- fall through to &8779 without RTI", inline=True)
comment(0x8770, "IRQ not set -- install handler and RTI", inline=True)
comment(0x8773, "Store error and return to idle", inline=True)
comment(0x8776, "BIT SR2: test RDA (bit7). Must be set for valid reply.", inline=True)
comment(0x8779, "No RDA -- error (FV masking RDA via PSE would cause this)", inline=True)
comment(0x877B, "Read source station", inline=True)
comment(0x877E, "Compare to original TX destination station (&0D20)", inline=True)
comment(0x8781, "Mismatch -- not the expected reply, error", inline=True)
comment(0x8783, "Read source network", inline=True)
comment(0x8786, "Compare to original TX destination network (&0D21)", inline=True)
comment(0x8789, "Mismatch -- error", inline=True)
comment(0x878B, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x878D, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x8790, "No FV -- incomplete frame, error", inline=True)
comment(0x8792, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", inline=True)
comment(0x8794, "Write CR2: enable RTS for TX handshake", inline=True)
comment(0x8797, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", inline=True)
comment(0x8799, "Write CR1: reset RX, enable TX interrupt", inline=True)
comment(0x879C, "Install next handler at &8878 (four-way data phase) into &0D43/&0D44", inline=True)
comment(0x879E, "High byte &88 of next handler address", inline=True)
comment(0x87A0, "Store low byte to nmi_next_lo", inline=True)
comment(0x87A3, "Store high byte to nmi_next_hi", inline=True)
comment(0x87A6, "Load dest station for scout ACK TX", inline=True)
comment(0x87A9, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x87AC, "TDRA not ready -- error", inline=True)
comment(0x87AE, "Write dest station to TX FIFO", inline=True)
comment(0x87B1, "Write dest network to TX FIFO", inline=True)
comment(0x87B4, "Write dest network to TX FIFO", inline=True)
comment(0x87B7, "Install handler at &87B7 (write src addr for scout ACK)", inline=True)
comment(0x87B9, "High byte &87 of handler address", inline=True)
comment(0x87BB, "Set NMI vector and return", inline=True)
comment(0x87BE, "Load our station ID (also INTOFF)", inline=True)
comment(0x87C1, "BIT SR1: test TDRA", inline=True)
comment(0x87C4, "TDRA not ready -- error", inline=True)
comment(0x87C6, "Write our station to TX FIFO", inline=True)
comment(0x87C9, "Write network=0 to TX FIFO", inline=True)
comment(0x87CB, "Write network byte to TX FIFO", inline=True)
comment(0x87CE, "Test bit 1 of tx_flags", inline=True)
comment(0x87D0, "Check if immediate-op or data-transfer", inline=True)
comment(0x87D3, "Bit 1 set: immediate op, use alt handler", inline=True)
comment(0x87D5, "Install nmi_data_tx at &87EE", inline=True)
comment(0x87D7, "High byte of handler address", inline=True)
comment(0x87D9, "Install and return via set_nmi_vector", inline=True)
comment(0x87DC, "Install nmi_imm_data at &8837", inline=True)
comment(0x87DE, "High byte of handler address", inline=True)
comment(0x87E0, "Install and return via set_nmi_vector", inline=True)
comment(0x87E3, "Y = buffer offset, resume from last position", inline=True)
comment(0x87E5, "No pages left: send final partial page", inline=True)
comment(0x87E7, "Load remaining byte count", inline=True)
comment(0x87E9, "Zero bytes left: skip to TDRA check", inline=True)
comment(0x87EB, "Load remaining byte count (alt entry)", inline=True)
comment(0x87ED, "Zero: loop back to top of handler", inline=True)
comment(0x87EF, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x87F2, "TDRA not ready -- error", inline=True)
comment(0x87FD, "Write data byte to TX FIFO", inline=True)
comment(0x87FF, "Write first byte of pair to FIFO", inline=True)
comment(0x8802, "Advance buffer offset", inline=True)
comment(0x8803, "No page crossing", inline=True)
comment(0x8805, "Page crossing: decrement page count", inline=True)
comment(0x8807, "No pages left: send last data", inline=True)
comment(0x8809, "Increment buffer high byte", inline=True)
comment(0x880B, "Load second byte of pair", inline=True)
comment(0x880D, "Write second byte to FIFO", inline=True)
comment(0x8810, "Advance buffer offset", inline=True)
comment(0x8811, "Save updated buffer position", inline=True)
comment(0x8813, "No page crossing", inline=True)
comment(0x8815, "Page crossing: decrement page count", inline=True)
comment(0x8817, "No pages left: send last data", inline=True)
comment(0x8819, "Increment buffer high byte", inline=True)
comment(0x881F, "BIT SR1: test IRQ (N=bit7) for tight loop", inline=True)
comment(0x8822, "IRQ still set: write 2 more bytes", inline=True)
comment(0x8824, "No IRQ: return, wait for next NMI", inline=True)
comment(0x882B, "CR2=&3F: TX_LAST_DATA (close data frame)", inline=True)
comment(0x882D, "Write CR2 to close frame", inline=True)
comment(0x8830, "Check tx_flags for next action", inline=True)
comment(0x8833, "Bit7 clear: error, install saved handler", inline=True)
comment(0x8835, "Install discard_reset_listen at &83F5", inline=True)
comment(0x8837, "High byte of &83F5 handler", inline=True)
comment(0x8839, "Set NMI vector and return", inline=True)
comment(0x883C, "Load saved next handler low byte", inline=True)
comment(0x883F, "Load saved next handler high byte", inline=True)
comment(0x8842, "Install saved handler and return", inline=True)
comment(0x8845, "Tube TX: BIT SR1 test TDRA", inline=True)
comment(0x8848, "TDRA not ready -- error", inline=True)
comment(0x884A, "Read byte from Tube R3", inline=True)
comment(0x884D, "Write to TX FIFO", inline=True)
comment(0x8850, "Increment 4-byte buffer counter", inline=True)
comment(0x8852, "Low byte didn't wrap", inline=True)
comment(0x8854, "Carry into second byte", inline=True)
comment(0x8856, "No further carry", inline=True)
comment(0x8858, "Carry into third byte", inline=True)
comment(0x885A, "No further carry", inline=True)
comment(0x885C, "Carry into fourth byte", inline=True)
comment(0x885E, "Counter wrapped to zero: last data", inline=True)
comment(0x8860, "Read second Tube byte from R3", inline=True)
comment(0x8863, "Write second byte to TX FIFO", inline=True)
comment(0x8866, "Increment 4-byte counter (second byte)", inline=True)
comment(0x8868, "Low byte didn't wrap", inline=True)
comment(0x886A, "Carry into second byte", inline=True)
comment(0x886C, "No further carry", inline=True)
comment(0x886E, "Carry into third byte", inline=True)
comment(0x8870, "No further carry", inline=True)
comment(0x8872, "Carry into fourth byte", inline=True)
comment(0x8874, "Counter wrapped to zero: last data", inline=True)
comment(0x8876, "BIT SR1: test IRQ for tight loop", inline=True)
comment(0x8879, "IRQ still set: write 2 more bytes", inline=True)
comment(0x887B, "No IRQ: return, wait for next NMI", inline=True)
comment(0x887E, "TX error: check flags for path", inline=True)
comment(0x8881, "Bit7 clear: TX result = not listening", inline=True)
comment(0x8883, "Bit7 set: discard and return to listen", inline=True)
comment(0x8886, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", inline=True)
comment(0x8888, "Write to ADLC CR1", inline=True)
comment(0x888B, "Install nmi_final_ack handler", inline=True)
comment(0x888D, "High byte of handler address", inline=True)
comment(0x888F, "Install and return via set_nmi_vector", inline=True)
comment(0x8892, "A=&01: AP mask", inline=True)
comment(0x8894, "BIT SR2: test AP", inline=True)
comment(0x8897, "No AP -- error", inline=True)
comment(0x8899, "Read dest station", inline=True)
comment(0x889C, "Compare to our station (INTOFF side effect)", inline=True)
comment(0x889F, "Not our station -- error", inline=True)
comment(0x88A1, "Install nmi_final_ack_net handler", inline=True)
comment(0x88A3, "Install continuation handler", inline=True)
comment(0x88A6, "BIT SR2: test RDA", inline=True)
comment(0x88A9, "No RDA -- error", inline=True)
comment(0x88AB, "Read dest network", inline=True)
comment(0x88AE, "Non-zero -- network mismatch, error", inline=True)
comment(0x88B0, "Install nmi_final_ack_validate handler", inline=True)
comment(0x88B2, "BIT SR1: test IRQ -- more data ready?", inline=True)
comment(0x88B5, "IRQ set -- fall through to validate", inline=True)
comment(0x88B7, "Install handler and RTI", inline=True)
comment(0x88BA, "BIT SR2: test RDA", inline=True)
comment(0x88BD, "No RDA -- error", inline=True)
comment(0x88BF, "Read source station", inline=True)
comment(0x88C2, "Compare to TX dest station (&0D20)", inline=True)
comment(0x88C5, "Mismatch -- error", inline=True)
comment(0x88C7, "Read source network", inline=True)
comment(0x88CA, "Compare to TX dest network (&0D21)", inline=True)
comment(0x88CD, "Mismatch -- error", inline=True)
comment(0x88CF, "Load TX flags for next action", inline=True)
comment(0x88D2, "bit7 clear: no data phase", inline=True)
comment(0x88D4, "Install data RX handler", inline=True)
comment(0x88D7, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x88D9, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x88DC, "No FV -- error", inline=True)
comment(0x88DE, "A=0: success result code", inline=True)
comment(0x88E0, "BEQ: always taken (A=0)", inline=True)
comment(0x88E2, "A=&41: not listening error code", inline=True)
comment(0x88E4, "Y=0: index into TX control block", inline=True)
comment(0x88E6, "Store result/error code at (nmi_tx_block),0", inline=True)
comment(0x88E8, "&80: completion flag for &0D3A", inline=True)
comment(0x88EA, "Signal TX complete", inline=True)
comment(0x88ED, "Full ADLC reset and return to idle listen", inline=True)
# Unreferenced dead data: 16 bytes between JMP at &88DF and
# tx_calc_transfer at &88F2. No code or data reference points here.
comment(0x88F0, "Unreferenced dead data (16 bytes)\n"
    "\n"
    "16 bytes between JMP discard_reset_rx (&88DF) and\n"
    "tx_calc_transfer (&88F2). Unreachable as code (after\n"
    "an unconditional JMP) and unreferenced as data. No\n"
    "label, index, or indirect pointer targets any address\n"
    "in the &88E2-&88F1 range. Likely unused remnant from\n"
    "development.")
comment(0x88F0, "Dead data: &0E", inline=True)
# UNMAPPED: comment(0x88E3, "Dead data: &0E", inline=True)
# UNMAPPED: comment(0x88E4, "Dead data: &0A", inline=True)
comment(0x88F3, "Dead data: &0A", inline=True)
comment(0x88F4, "Dead data: &0A", inline=True)
comment(0x88F5, "Dead data: &06", inline=True)
# UNMAPPED: comment(0x88E8, "Dead data: &06", inline=True)
comment(0x88F7, "Dead data: &0A", inline=True)
comment(0x88F8, "Dead data: &81", inline=True)
# UNMAPPED: comment(0x88EB, "Dead data: &00", inline=True)
comment(0x88FA, "Dead data: &00", inline=True)
comment(0x88FB, "Dead data: &00", inline=True)
comment(0x88FC, "Dead data: &00", inline=True)
comment(0x88FD, "Dead data: &01", inline=True)
# UNMAPPED: comment(0x88F0, "Dead data: &01", inline=True)
comment(0x88FF, "Dead data: &81", inline=True)
# UNMAPPED: comment(0x88F2, "Y=7: offset to RXCB buffer addr byte 3", inline=True)
comment(0x8909, "Read RXCB[7] (buffer addr high byte)", inline=True)
comment(0x890B, "Compare to &FF", inline=True)
comment(0x890D, "Not &FF: normal buffer, skip Tube check", inline=True)
comment(0x8910, "Read RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x8912, "Check if addr byte 2 >= &FE (Tube range)", inline=True)
# UNMAPPED: comment(0x88FF, "Tube/IO address: use fallback path", inline=True)
comment(0x8924, "Transmit in progress?", inline=True)
comment(0x8927, "No: fallback path", inline=True)
comment(0x8929, "Load TX flags for transfer setup", inline=True)
comment(0x892C, "Set bit 1 (transfer complete)", inline=True)
comment(0x892E, "Store with bit 1 set (Tube xfer)", inline=True)
comment(0x8931, "Init borrow for 4-byte subtract", inline=True)
comment(0x8932, "Save carry on stack", inline=True)
comment(0x8933, "Y=4: start at RXCB offset 4", inline=True)
comment(0x8935, "Load RXCB[Y] (current ptr byte)", inline=True)
comment(0x8937, "Y += 4: advance to RXCB[Y+4]", inline=True)
comment(0x8938, "(continued)", inline=True)
comment(0x8939, "(continued)", inline=True)
comment(0x893A, "(continued)", inline=True)
comment(0x893B, "Restore borrow from previous byte", inline=True)
comment(0x893C, "Subtract RXCB[Y+4] (start ptr byte)", inline=True)
comment(0x893E, "Store result byte", inline=True)
comment(0x8941, "Y -= 3: next source byte", inline=True)
comment(0x8942, "(continued)", inline=True)
comment(0x8943, "(continued)", inline=True)
comment(0x8944, "Save borrow for next byte", inline=True)
comment(0x8945, "Done all 4 bytes?", inline=True)
comment(0x8947, "No: next byte pair", inline=True)
comment(0x8949, "Discard final borrow", inline=True)
comment(0x894A, "Save X", inline=True)
comment(0x894B, "Save X", inline=True)
comment(0x894C, "Compute address of RXCB+4", inline=True)
comment(0x894E, "CLC for base pointer addition", inline=True)
comment(0x894F, "Add RXCB base to get RXCB+4 addr", inline=True)
comment(0x8951, "X = low byte of RXCB+4", inline=True)
comment(0x8952, "Y = high byte of RXCB ptr", inline=True)
comment(0x8954, "Tube claim type &C2", inline=True)
comment(0x8956, "Claim Tube transfer address", inline=True)
comment(0x8959, "No Tube: skip reclaim", inline=True)
comment(0x895B, "Tube: reclaim with scout status", inline=True)
comment(0x895E, "Reclaim with scout status type", inline=True)
comment(0x8961, "Release Tube claim after reclaim", inline=True)
comment(0x8964, "C=1: Tube address claimed", inline=True)
comment(0x8965, "Restore X", inline=True)
comment(0x8966, "Restore X from stack", inline=True)
comment(0x8967, "Return with C = transfer status", inline=True)
comment(0x8968, "Y=4: RXCB current pointer offset", inline=True)
comment(0x896A, "Load RXCB[4] (current ptr lo)", inline=True)
comment(0x896C, "Y=8: RXCB start address offset", inline=True)
comment(0x896E, "Set carry for subtraction", inline=True)
comment(0x896F, "Subtract RXCB[8] (start ptr lo)", inline=True)
comment(0x8971, "Store transfer size lo", inline=True)
comment(0x8973, "Y=5: current ptr hi offset", inline=True)
comment(0x8975, "Load RXCB[5] (current ptr hi)", inline=True)
comment(0x8977, "Propagate borrow only", inline=True)
comment(0x8979, "Temp store of adjusted hi byte", inline=True)
comment(0x897B, "Y=8: start address lo offset", inline=True)
comment(0x897D, "Copy RXCB[8] to open port buffer lo", inline=True)
comment(0x897F, "Store to scratch (side effect)", inline=True)
comment(0x8981, "Y=9: start address hi offset", inline=True)
comment(0x8983, "Load RXCB[9]", inline=True)
comment(0x8985, "Set carry for subtraction", inline=True)
comment(0x8986, "Subtract adjusted hi byte", inline=True)
comment(0x8988, "Store transfer size hi", inline=True)
comment(0x898A, "Return with C=1", inline=True)
comment(0x898B, "Return with C=1 (success)", inline=True)
comment(0x898C, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", inline=True)
comment(0x898E, "Write CR1 to ADLC register 0", inline=True)
comment(0x8991, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", inline=True)
comment(0x8993, "Write CR4 to ADLC register 3", inline=True)
comment(0x8996, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", inline=True)
comment(0x8998, "Write CR3 to ADLC register 1", inline=True)
comment(0x899B, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", inline=True)
comment(0x899D, "Write to ADLC CR1", inline=True)
comment(0x89A0, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x89A2, "Write to ADLC CR2", inline=True)
comment(0x89A5, "Return; ADLC now in RX listen mode", inline=True)
comment(0x89A6, "Check if Econet has been initialised", inline=True)
comment(0x89A9, "Not initialised: skip to RX listen", inline=True)
comment(0x89AB, "Read current NMI handler low byte", inline=True)
comment(0x89AE, "Expected: &B3 (nmi_rx_scout low)", inline=True)
comment(0x89B0, "Not idle: spin and wait", inline=True)
comment(0x89B2, "Read current NMI handler high byte", inline=True)
comment(0x89B5, "Test if high byte = &80 (page of nmi_rx_scout)", inline=True)
comment(0x89B7, "Not idle: spin and wait", inline=True)
comment(0x89B9, "INTOFF: disable NMIs", inline=True)
comment(0x89BC, "INTOFF again (belt-and-braces)", inline=True)
comment(0x89BF, "TX not in progress", inline=True)
comment(0x89C2, "Econet not initialised", inline=True)
comment(0x89C5, "Y=5: service call workspace page", inline=True)
comment(0x89C7, "Set ADLC to RX listen mode", inline=True)
comment(0x89CA, "INTOFF: force /NMI high (IC97 flip-flop clear)", inline=True)
comment(0x89CD, "Save A", inline=True)
comment(0x89CE, "Transfer Y to A", inline=True)
comment(0x89CF, "Save Y (via A)", inline=True)
comment(0x89D0, "ROM bank 0 (patched during init for actual bank)", inline=True)
comment(0x89D2, "Select Econet ROM bank via ROMSEL", inline=True)
comment(0x89D5, "Jump to scout handler in ROM", inline=True)
comment(0x89D8, "Store handler high byte at &0D0D", inline=True)
comment(0x89DB, "Store handler low byte at &0D0C", inline=True)
comment(0x89DE, "Restore NFS ROM bank", inline=True)
comment(0x89E0, "Page in via hardware latch", inline=True)
comment(0x89E3, "Restore Y from stack", inline=True)
comment(0x89E4, "Transfer ROM bank to Y", inline=True)
comment(0x89E5, "Restore A from stack", inline=True)
comment(0x89E6, "INTON: guaranteed /NMI edge if ADLC IRQ asserted", inline=True)
comment(0x89E9, "Return from interrupt", inline=True)

# Dead data between rom_set_nmi_vector RTI and svc_dispatch_lo.
# The NMI shim copy (Y=1..&20) ends at &89C6; these 3 bytes at
# &89BD-&89BF are outside the copy range and unreferenced.
# UNMAPPED: comment(0x89C7, "Unreferenced dead data (3 bytes)\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "3 bytes between the RTI at &89C6 (end of the NMI\n"
# UNMAPPED:     "shim ROM source) and svc_dispatch_lo at &89CA.\n"
# UNMAPPED:     "The init copy loop (Y=1..&20) copies &89A7-&89C6\n"
# UNMAPPED:     "to &0D00-&0D1F; these bytes are outside that range\n"
# UNMAPPED:     "and unreferenced. Likely unused development remnant.")
# UNMAPPED: comment(0x89C7, "Dead data: &01", inline=True)
# UNMAPPED: comment(0x89C8, "Dead data: &00", inline=True)

# Inline comments: service/infrastructure layer (&8A0B-&9130)
comment(0x8A54, "Save service call number", inline=True)
comment(0x8A55, "Is it service 15 (vectors claimed)?", inline=True)
comment(0x8A57, "No: skip vectors-claimed handling", inline=True)
# UNMAPPED: comment(0x8A1A, "Save Y parameter", inline=True)
# UNMAPPED: comment(0x8A1B, "Save Y on stack", inline=True)
comment(0x8A5A, "OSBYTE 0: read OS version", inline=True)
comment(0x8A5C, "X=1 to request version number", inline=True)
comment(0x8A61, "OS 3.2/3.5 (Master 128)?", inline=True)
comment(0x8A63, "Yes: target OS, skip Bad ROM message", inline=True)
comment(0x8A65, "OS 4.0 (Master Econet Terminal)?", inline=True)
comment(0x8A67, "Yes: target OS, skip Bad ROM message", inline=True)
comment(0x8A69, "Transfer OS version to A", inline=True)
comment(0x8A6A, "Save flags (Z set if OS 1.00) across print", inline=True)
comment(0x8A6B, "Print '<CR>Bad ROM ' to mark non-Master OS", inline=True)
comment(0x8A77, "Load this ROM's slot number", inline=True)
comment(0x8A79, "Print slot number as decimal", inline=True)
comment(0x8A7C, "Print trailing newline, bypassing *SPOOL", inline=True)
comment(0x8A7F, "Reload ROM slot for workspace clearing", inline=True)
comment(0x8A81, "Restore flags", inline=True)
comment(0x8A82, "OS 1.00: skip INX (table starts at slot 0)", inline=True)
comment(0x8A84, "Adjust index for OS 1.20/2.00/5.00 layout", inline=True)
comment(0x8A85, "A=0", inline=True)
comment(0x8A87, "Clear workspace byte for this ROM", inline=True)
comment(0x8A8A, "Restore ROM slot to X", inline=True)
comment(0x8A8D, "Restore Y parameter", inline=True)
# UNMAPPED: comment(0x8A3B, "Transfer to Y", inline=True)
# UNMAPPED: comment(0x8A3C, "Restore service call number", inline=True)
# UNMAPPED: comment(0x8A3D, "Check relocated code service dispatch", inline=True)
comment(0x8A8E, "Save service call number", inline=True)

# svc_18_fs_select inline comments (4 items)
comment(0x8B45, "Service 18 carries FS number in Y; Econet is FS 5", inline=True)
comment(0x8B47, "Not us: pass the call on (RTS via shared return)", inline=True)
comment(0x8B49, "A=0 to claim the service", inline=True)
comment(0x8B4B, "Clear svc_state and fall into ensure_fs_selected", inline=True)

# osbyte_x0 inline comment (1 item)
comment(0x8EC9, "Force X=0; the LDY #&FF in osbyte_yff sets Z, so the BEQ "
        "after this is unconditional", inline=True)

# is_decimal_digit inline comments (4 items)
comment(0x939A, "Hex prefix '&'?", inline=True)
comment(0x939C, "Yes: treat as digit-like (carry set on exit)", inline=True)
comment(0x939E, "Network/station separator '.'?", inline=True)
comment(0x93A0, "Yes: also digit-like; else fall through to decimal test",
        inline=True)

# is_dec_digit_only inline comments (6 items)
comment(0x93A2, "Above '9'? (CMP #':')", inline=True)
comment(0x93A4, "Yes: not a digit -- jump to clear-carry exit", inline=True)
comment(0x93A6, "Below '0'? (CMP sets carry if A >= '0')", inline=True)
comment(0x93A8, "Carry now reflects '0'-'9' membership; return", inline=True)
comment(0x93A9, "Out-of-range exit: clear carry to signal not-a-digit",
        inline=True)
comment(0x93AA, "Return", inline=True)

# get_access_bits inline comments (5 items)
comment(0x93AB, "Y=&0E: directory entry access byte offset", inline=True)
comment(0x93AD, "Read access byte through fs_options pointer", inline=True)
comment(0x93AF, "Mask to 6 protection bits (clears the unused top two)",
        inline=True)
comment(0x93B1, "X=4: encode-table column index for owner-access bits",
        inline=True)
comment(0x93B3, "Always taken: LDX #4 cleared Z, so BNE is "
        "unconditional", inline=True)

# get_prot_bits / begin_prot_encode inline comments (10 items)
comment(0x93B5, "Mask to 5 protection bits (low 5)", inline=True)
comment(0x93B7, "X=&FF; INX inside the loop bumps to 0 for column 0",
        inline=True)
comment(0x93B9, "Park source bits in fs_error_ptr -- the LSR target",
        inline=True)
comment(0x93BB, "A=0: accumulator for encoded result", inline=True)
comment(0x93BD, "Advance table column index", inline=True)
comment(0x93BE, "Shift next source bit into carry", inline=True)
comment(0x93C0, "Source bit was 0: skip the OR for this column", inline=True)
comment(0x93C2, "Source bit was 1: OR in this column's encoded mask",
        inline=True)
comment(0x93C5, "Continue while either fs_error_ptr or A is non-zero "
        "(loop ends when source exhausted and result still 0)", inline=True)
comment(0x93C7, "Return with encoded value in A", inline=True)

# set_text_and_xfer_ptr inline comments (2 items)
comment(0x93D3, "Save text pointer low byte (where caller wants OS to "
        "scan from)", inline=True)
comment(0x93D5, "Save text pointer high byte; fall through to "
        "set_xfer_params", inline=True)

# set_xfer_params inline comments (3 items)
comment(0x93D7, "Stash transfer byte count (in A)", inline=True)
comment(0x93D9, "Source pointer low byte", inline=True)
comment(0x93DB, "Source pointer high byte; fall through to set_options_ptr",
        inline=True)

# set_options_ptr / clear_escapable inline comments (4 items shared)
comment(0x93DD, "Options pointer low byte (parameter block base)",
        inline=True)
comment(0x93DF, "Options pointer high byte; fall through to clear_escapable",
        inline=True)
comment(0x93E1, "Save flags so the LSR doesn't disturb caller's NZC",
        inline=True)
comment(0x93E2, "Shift bit 0 of need_release_tube into carry, clearing "
        "the bit", inline=True)
comment(0x93E4, "Restore caller's flags", inline=True)
comment(0x93E5, "Return", inline=True)

# cmp_5byte_handle inline comments (7 items)
comment(0x93E6, "X=4: loop from offset 4 down to 1 (skips offset 0)",
        inline=True)
comment(0x93E8, "Load saved-handle byte from addr_work[X]", inline=True)
comment(0x93EA, "EOR with parsed handle byte; Z set iff bytes match",
        inline=True)
comment(0x93EC, "Mismatch: bail out with Z clear", inline=True)
comment(0x93EE, "Decrement to next byte", inline=True)
comment(0x93EF, "Loop while X != 0 (offset 0 is intentionally not "
        "compared)", inline=True)
comment(0x93F1, "Return; Z reflects last EOR (set = match, clear = "
        "mismatch)", inline=True)

# get_pb_ptr_as_index inline comments (1 item)
comment(0xA3E7, "Read PB[0] (the OSWORD sub-function code in most calls); "
        "fall into byte_to_2bit_index", inline=True)

# push_osword_handler_addr inline comments (6 items)
comment(0xAD15, "Load handler high byte from hi-table column X", inline=True)
comment(0xAD18, "Push for the eventual RTS dispatch", inline=True)
comment(0xAD19, "Load handler low byte from lo-table column X", inline=True)
comment(0xAD1C, "Push lo so RTS pulls (lo, hi)+1 -> handler entry",
        inline=True)
comment(0xAD1D, "Reload original OSWORD number into A for the handler",
        inline=True)
comment(0xAD1F, "RTS jumps to handler with A=OSWORD number", inline=True)

# match_rx_code inline comments (5 items, including loop)
comment(0xADB8, "Compare A with table entry at index X", inline=True)
comment(0xADBB, "Match: return with Z set", inline=True)
comment(0xADBD, "Step to next earlier table entry", inline=True)
comment(0xADBE, "Loop while X >= 0 (table walked top-down)", inline=True)
comment(0xADC0, "Return; Z reflects last CMP", inline=True)

# init_ws_copy_wide inline comments (4 items)
comment(0xADFE, "X=&0D: 14 template bytes to process", inline=True)
comment(0xAE00, "Y=&7C: workspace destination offset for wide variant",
        inline=True)
comment(0xAE02, "BIT &FF unconditionally sets V (the always_set_v_byte "
        "trick)", inline=True)
comment(0xAE05, "V=1 always: skip the narrow-mode prologue and CLV",
        inline=True)

# init_ws_copy_narrow inline comments (2 items)
comment(0xAE07, "Y=&17: workspace destination offset for narrow variant",
        inline=True)
comment(0xAE09, "X=&1A: 27 template bytes to process; fall into "
        "ws_copy_vclr_entry which CLVs", inline=True)

# ws_copy_vclr_entry / loop_copy_ws_template inline comments (16 items)
comment(0xAE0B, "Clear V: narrow mode (writes via nfs_workspace pointer)",
        inline=True)
comment(0xAE0C, "Read next template byte", inline=True)
comment(0xAE0F, "&FE: end-of-template marker?", inline=True)
comment(0xAE11, "Yes: finalise and return", inline=True)
comment(0xAE13, "&FD: skip-this-offset marker?", inline=True)
comment(0xAE15, "Yes: advance index without storing", inline=True)
comment(0xAE17, "&FC: substitute-workspace-page-pointer marker?",
        inline=True)
comment(0xAE19, "No special marker: store this byte verbatim", inline=True)
comment(0xAE1B, "Wide path: page pointer is net_rx_ptr's high byte",
        inline=True)
comment(0xAE1D, "V=1 (wide): keep the rx_ptr high byte", inline=True)
comment(0xAE1F, "V=0 (narrow): use nfs_workspace high byte instead",
        inline=True)
comment(0xAE21, "Stash whichever page byte we picked into net_tx_ptr_hi",
        inline=True)
comment(0xAE23, "V=1 (wide): store via net_rx_ptr,Y", inline=True)
comment(0xAE25, "V=0 (narrow): store via nfs_workspace,Y", inline=True)
comment(0xAE27, "Always branch: V is still clear here", inline=True)
comment(0xAE29, "Wide-mode store via net_rx_ptr", inline=True)
comment(0xAE2B, "Step Y down (workspace offset)", inline=True)
comment(0xAE2C, "Step X down (template index)", inline=True)
comment(0xAE2D, "Loop while X >= 0", inline=True)
comment(0xAE2F, "Bump Y back to first written offset", inline=True)
comment(0xAE30, "Save it as net_tx_ptr low for the caller", inline=True)
comment(0xAE32, "Return", inline=True)

# print_10_chars / print_chars_from_buf inline comments
comment(0xB21A, "Y=10: ten characters to print (fixed-width field)",
        inline=True)
comment(0xB21C, "Read next character from reply buffer at offset X",
        inline=True)
comment(0xB21F, "Print via OSASCI, bypassing the *SPOOL file", inline=True)
comment(0xB222, "Step buffer offset", inline=True)
comment(0xB223, "Step character counter", inline=True)
comment(0xB224, "Loop until Y=0", inline=True)
comment(0xB226, "Return; X points just past the last printed byte",
        inline=True)

# parse_cmd_arg_y0 inline comment (1 item)
comment(0xB22A, "Y=0: scan from start of command line", inline=True)

# strip_token_prefix inline comments (16 items)
comment(0xB251, "Save caller's X (TX buffer offset)", inline=True)
comment(0xB252, "Push it", inline=True)
comment(0xB253, "X=&FF: INX in loop bumps to 0 for first byte", inline=True)
comment(0xB255, "Step to next byte position", inline=True)
comment(0xB256, "Read byte X+1 (the next character)", inline=True)
comment(0xB259, "Store it back at byte X (shifting left by one)",
        inline=True)
comment(0xB25C, "EOR with CR; Z set if we just shifted the terminator",
        inline=True)
comment(0xB25E, "More to shift: continue", inline=True)
comment(0xB260, "X is now the buffer length (excluding CR)", inline=True)
comment(0xB261, "Empty after shift: skip trim, restore X, return",
        inline=True)
comment(0xB263, "Read last buffer byte (X-1 because we count from 0)",
        inline=True)
comment(0xB266, "EOR with space; Z set iff it's a trailing space",
        inline=True)
comment(0xB268, "Not a space: trim done, restore X, return", inline=True)
comment(0xB26A, "It is a space: replace with CR (truncate the string)",
        inline=True)
comment(0xB26C, "Store CR at the now-trimmed position", inline=True)
comment(0xB26F, "Step backwards", inline=True)
comment(0xB270, "Loop while X > 0", inline=True)
comment(0xB272, "Restore caller's TX buffer offset", inline=True)
comment(0xB273, "Transfer back to X", inline=True)
comment(0xB274, "Return", inline=True)

# copy_arg_to_buf_x0 inline comment (1 item)
comment(0xB29F, "X=0: place the argument at the start of the TX buffer; "
        "fall into copy_arg_to_buf", inline=True)

# get_ws_page: complete the existing partial annotation
comment(0x8CAD, "Y = current ROM slot number from MOS copy at &F4",
        inline=True)
comment(0x8CB2, "Hold a copy of the slot byte in Y while we test bit 6",
        inline=True)
comment(0x8CB3, "ROL puts pre-ROL bit 6 into the post-ROL N flag (and "
        "pre-ROL bit 7 into C)", inline=True)
comment(0x8CB4, "Save those flags so the upcoming ROR doesn't lose N",
        inline=True)
comment(0x8CB5, "ROR restores A to its original value (using the saved "
        "C)", inline=True)
comment(0x8CB6, "Restore the ROL flags: N is now pre-ROL bit 6", inline=True)
comment(0x8CB7, "Bit 6 clear: skip the OR (no ADLC-absent flag)",
        inline=True)
comment(0x8CB9, "Bit 6 set: re-set bit 7 in the returned page byte (the "
        "ADLC-absent flag uses bit 7 in callers)", inline=True)

# mask_owner_access inline comments (4 items)
comment(0xB2CF, "Read fs_lib_flags (now at &C271 in 4.21)", inline=True)
comment(0xB2D2, "Keep only the 5-bit owner access mask", inline=True)
comment(0xB2D4, "Store back, clearing FS-selection and other high bits",
        inline=True)
comment(0xB2D7, "Return", inline=True)

# prompt_yn inline comments (3 items)
comment(0xB7CB, "Print 'Y/N) ' via the inline-string helper", inline=True)
comment(0xB7CE, "Inline string body — bytes consumed by sub_c928a (above)",
        inline=True)
comment(0xB7D1, "Force lower-case (bit 5 = ' ' bit) for case-insensitive "
        "Y/N test", inline=True)

# close_ws_file inline comments (3 items)
comment(0xBF71, "Y = saved file handle from ws_page", inline=True)
comment(0xBF73, "A=0: OSFIND close", inline=True)
comment(0xBF75, "Tail-call OSFIND to close the handle", inline=True)

# advance_x_by_8 / advance_x_by_4 / inx4 inline comments
comment(0xBFBA, "First INX-by-4 via JSR; falls into advance_x_by_4 for "
        "the second four", inline=True)
comment(0xBFBD, "JSR inx4 (4 INX); RTS returns here, then falls into "
        "inx4 again for the implicit second four", inline=True)
comment(0xBFC0, "First INX", inline=True)
comment(0xBFC1, "Second INX", inline=True)
comment(0xBFC2, "Third INX", inline=True)
comment(0xBFC3, "Fourth INX", inline=True)
comment(0xBFC4, "Return; caller is either an explicit JSR (so X has "
        "advanced by 4) or advance_x_by_8's fall-through (so X has "
        "advanced by 8 total)", inline=True)

# copy_arg_to_buf inline comment (1 item)
comment(0xB2A1, "Y=0: scan from start of command line (CLC entry skips "
        "'&' validation)", inline=True)

# copy_arg_validated inline comments (15 items in body)
comment(0xB2A3, "Set C: this entry validates against '&'", inline=True)
comment(0xB2A4, "Read next source byte through fs_crc_lo pointer",
        inline=True)
comment(0xB2A6, "Store into TX buffer at offset X", inline=True)
comment(0xB2A9, "Validation off (C clear): just advance positions",
        inline=True)
comment(0xB2AB, "Test against '!' to bias the EOR comparison", inline=True)
comment(0xB2AD, "EOR with '&'; Z set iff source byte was '&'", inline=True)
comment(0xB2AF, "'&' inside the argument is illegal: raise 'Bad filename'",
        inline=True)
comment(0xB2B1, "Restore A by undoing the EOR (so the loop terminator "
        "test below sees the original byte)", inline=True)
comment(0xB2B3, "Advance TX buffer offset", inline=True)
comment(0xB2B4, "Advance command-line offset", inline=True)
comment(0xB2B5, "EOR with CR; Z set iff we just stored the terminator",
        inline=True)
comment(0xB2B7, "More to copy: continue", inline=True)
# Trailing-space trim (4.21 addition)
comment(0xB2B9, "Look at the byte just before the CR we stopped on",
        inline=True)
comment(0xB2BC, "EOR with space; Z set iff that byte was a trailing space",
        inline=True)
comment(0xB2BE, "Not a space: trim done", inline=True)
comment(0xB2C0, "Step back over the space", inline=True)
comment(0xB2C1, "A=&0D: replace the trailing space with CR", inline=True)
comment(0xB2C3, "Store CR at the now-truncated end", inline=True)
comment(0xB2C6, "Always taken (A=&0D from LDA #&0D so Z is clear); look "
        "at the next byte back", inline=True)
comment(0xB2C8, "All trailing spaces consumed (or none present)",
        inline=True)
comment(0xB2CA, "Return", inline=True)

# copy_ps_data_y1c inline comment (1 item)
comment(0xB3D5, "Y=&18: standard offset for the PS template; fall into "
        "copy_ps_data", inline=True)

# load_ps_server_addr inline comments (6 items)
comment(0xB4A8, "Y=2: workspace offset of PS station byte", inline=True)
comment(0xB4AA, "Read station byte", inline=True)
comment(0xB4AC, "Stash in fs_work_5 (PS station)", inline=True)
comment(0xB4AE, "Y=3: workspace offset of PS network byte", inline=True)
comment(0xB4AF, "Read network byte", inline=True)
comment(0xB4B1, "Stash in fs_work_6 (PS network)", inline=True)

# write_ps_slot_byte_ff inline comments (4 items)
comment(0xB51C, "Step Y to next workspace slot byte", inline=True)
comment(0xB51D, "Load buffer page byte from addr_work", inline=True)
comment(0xB51F, "Write at offset Y", inline=True)
comment(0xB521, "A=&FF: sentinel; fall into write_two_bytes_inc_y to "
        "store two of them", inline=True)

# write_two_bytes_inc_y inline comments (5 items)
comment(0xB523, "Step Y to next destination", inline=True)
comment(0xB524, "Write A at workspace offset Y", inline=True)
comment(0xB526, "Step Y again", inline=True)
comment(0xB527, "Write A at the next offset (two consecutive copies)",
        inline=True)
comment(0xB529, "Final INY leaves Y pointing past the second write",
        inline=True)

# reverse_ps_name_to_tx inline comments (16 items)
comment(0xB52B, "Y=&18: source offset (start of PS name in RX buffer)",
        inline=True)
comment(0xB52D, "Read RX byte at offset Y", inline=True)
comment(0xB52F, "Push it (the stack reverses the order)", inline=True)
comment(0xB530, "Step source", inline=True)
comment(0xB531, "Reached &20 (one past the 8-byte name)?", inline=True)
comment(0xB533, "No: continue pushing", inline=True)
comment(0xB535, "Y=&17: destination offset for the reversed name",
        inline=True)
comment(0xB537, "Pull next pushed byte (LIFO -> reversed order)",
        inline=True)
comment(0xB538, "Store at destination offset Y", inline=True)
comment(0xB53A, "Step destination back", inline=True)
comment(0xB53B, "Reached &0F (one before the destination range)?",
        inline=True)
comment(0xB53D, "No: continue popping", inline=True)
comment(0xB53F, "Copy net_rx_ptr_hi as the TX page (TX shares the same "
        "page as RX for this packet)", inline=True)
comment(0xB541, "Set net_tx_ptr_hi", inline=True)
comment(0xB543, "TX low byte = &0C: skip past the TX header to where "
        "the reversed name lives", inline=True)
comment(0xB545, "Set net_tx_ptr lo", inline=True)
comment(0xB547, "Y=3: copy 4-byte TX header (offsets 3..0)", inline=True)
comment(0xB549, "Read template byte", inline=True)
comment(0xB54C, "Write to TX buffer at offset Y", inline=True)
comment(0xB54E, "Step backwards", inline=True)
comment(0xB54F, "Loop while Y >= 0", inline=True)
comment(0xB551, "Return", inline=True)

# save_net_tx_cb inline comment (1 item)
comment(0x978A, "Clear V: standard send mode (callers set V via "
        "save_net_tx_cb_vset for the lib-flag variant)", inline=True)

# save_net_tx_cb_vset inline comments (15 items, including shared body)
comment(0x978B, "Read FS station from &C002 (saved from selection time)",
        inline=True)
comment(0x978E, "Copy into TX buffer at &C102 (dest station for header)",
        inline=True)
comment(0x9791, "Clear C: caller wants four-way handshake (not "
        "disconnect)", inline=True)
comment(0x9792, "Save flags so we can keep V across the loop", inline=True)
comment(0x9793, "Save Y -- the entry function code -- into TX[1]",
        inline=True)
comment(0x9796, "Y=1: copy 2 bytes (network/control) starting at index 1",
        inline=True)
comment(0x9798, "Read source byte at &C003+Y", inline=True)
comment(0x979B, "Write to TX buffer at &C103+Y", inline=True)
comment(0x979E, "Step backwards", inline=True)
comment(0x979F, "Loop while Y >= 0 (covers indices 1, 0)", inline=True)
comment(0x97A1, "Test fs_lib_flags: bit 6 = use library, bit 7 = "
        "*-prefix-stripped", inline=True)
comment(0x97A4, "V (bit 6) set: use the library station instead",
        inline=True)
comment(0x97A6, "Neither bit set: leave the FS station copy intact",
        inline=True)
comment(0x97A8, "Bit 7 (FS-prefix) set: substitute the saved-prefix "
        "station from &C004", inline=True)
comment(0x97AB, "Override TX[3]'s station byte", inline=True)
comment(0x97AE, "Always taken: V was clear when we entered (BVS at "
        "&97A4 didn't fire)", inline=True)
comment(0x97B0, "use_lib_station: substitute the library station from "
        "&C002 (the original FS station, but bit 6 of fs_lib_flags "
        "redirects via lib path)", inline=True)
comment(0x97B3, "Override TX[3] with the library station byte",
        inline=True)
comment(0x97B6, "Restore the saved flags (V/C control downstream "
        "init_txcb behaviour)", inline=True)

# wait_net_tx_ack inline comments (28 items in body)
comment(0x98BE, "Read the configurable rx-wait timeout (&0D6E, default "
        "&28 = ~22s on 2 MHz)", inline=True)
comment(0x98C1, "Push it as the outermost counter (read back via "
        "stack-X indexing later)", inline=True)
comment(0x98C2, "Read econet_flags so we can preserve it across the wait",
        inline=True)
comment(0x98C5, "Push it (we'll temporarily set bit 7 to mark waiting)",
        inline=True)
comment(0x98C6, "Check whether net_tx_ptr_hi is non-zero (TX in flight?)",
        inline=True)
comment(0x98C8, "Yes: skip the flag-set; counters initialise either way",
        inline=True)
comment(0x98CA, "TX idle: set bit 7 of econet_flags (signal RX-only wait)",
        inline=True)
comment(0x98CC, "Write the modified flags back", inline=True)
comment(0x98CF, "A=0: initial value for inner+middle counters", inline=True)
comment(0x98D1, "Push it -- middle counter at stack[X+2]", inline=True)
comment(0x98D2, "Push it again -- inner counter at stack[X+1]",
        inline=True)
comment(0x98D3, "Y=0: indirect index for net_tx_ptr poll", inline=True)
comment(0x98D4, "Capture S into X so we can address the stack counters",
        inline=True)
comment(0x98D5, "Read RX/TX flags through net_tx_ptr -- bit 7 set means "
        "complete", inline=True)
comment(0x98D7, "Bit 7 set: reply received, exit poll", inline=True)
comment(0x98D9, "Decrement inner counter at stack[X+1]", inline=True)
comment(0x98DC, "Inner not zero yet: poll again", inline=True)
comment(0x98DE, "Inner wrapped: decrement middle at stack[X+2]",
        inline=True)
comment(0x98E1, "Middle not zero: poll again", inline=True)
comment(0x98E3, "Middle wrapped: decrement outer at stack[X+4] (the "
        "saved timeout value)", inline=True)
comment(0x98E6, "Outer not zero: poll again", inline=True)
comment(0x98E8, "Reload the original timeout to test for timeout=0 mode",
        inline=True)
comment(0x98EB, "Configured timeout was non-zero: declare timeout",
        inline=True)
comment(0x98ED, "Timeout=0 (poll forever): check escape flag", inline=True)
comment(0x98EF, "Escape pressed: jump to escape handler at &9895",
        inline=True)
comment(0x98F1, "Reset outer counter so we keep polling", inline=True)
comment(0x98F4, "Always taken (INC's result is always non-zero here): "
        "back to inner", inline=True)
comment(0x98F6, "done_poll_tx: discard inner counter (PLA)", inline=True)
comment(0x98F7, "Discard middle counter", inline=True)
comment(0x98F8, "Pull saved econet_flags", inline=True)
comment(0x98F9, "Restore them (clearing bit 7 if we set it)", inline=True)
comment(0x98FC, "Pull saved rx_wait_timeout into A", inline=True)
comment(0x98FD, "If timeout reached zero, raise 'No reply'", inline=True)
comment(0x98FF, "Reply received normally: return", inline=True)

# set_conn_active inline comments (11 items)
comment(0x93F7, "Save flags so the rest of the routine is transparent",
        inline=True)
comment(0x93F8, "Save A (the attribute byte we need to recover via stack)",
        inline=True)
comment(0x93F9, "Save X", inline=True)
comment(0x93FA, "Capture S into X to address stack from below",
        inline=True)
comment(0x93FB, "Re-read the original A from stack[X+2] (above PHX/PHA)",
        inline=True)
comment(0x93FE, "Convert attribute byte to channel-table index", inline=True)
comment(0x9401, "No matching channel: skip the flag set, just restore",
        inline=True)
comment(0x9403, "A=&40: bit 6 = connection-active mask", inline=True)
comment(0x9405, "OR with current status byte for this channel",
        inline=True)
comment(0x9408, "Write back the updated status", inline=True)
comment(0x940B, "Always taken (A is non-zero after the OR with &40); "
        "join shared exit", inline=True)

# clear_conn_active inline comments (8 body items, shares c9421 exit)
comment(0x940D, "Save flags", inline=True)
comment(0x940E, "Save A", inline=True)
comment(0x940F, "Save X", inline=True)
comment(0x9410, "Capture S into X for stack-relative reads", inline=True)
comment(0x9411, "Re-read the attribute byte from stack[X+2]", inline=True)
comment(0x9414, "Convert attribute to channel index", inline=True)
comment(0x9417, "No matching channel: just restore", inline=True)
comment(0x9419, "A=&BF: bit 6 clear mask", inline=True)
comment(0x941B, "AND with current status byte", inline=True)
comment(0x941E, "Write back the updated status", inline=True)

# Shared exit at &9421 (4 items)
comment(0x9421, "Restore X (saved at PHX)", inline=True)
comment(0x9422, "Restore A", inline=True)
comment(0x9423, "Restore flags", inline=True)
comment(0x9424, "Return; A and X preserved across the call", inline=True)

# prep_send_tx_cb inline comments (12 items)
comment(0x97B7, "Save flags so C survives the init_txcb call", inline=True)
comment(0x97B8, "Reply port = &90 (FS reply port)", inline=True)
comment(0x97BA, "Stash port in TXCB[0]", inline=True)
comment(0x97BD, "Build the rest of the TXCB (control, dest stn/net, "
        "etc.)", inline=True)
comment(0x97C0, "Move TX-buffer end pointer (returned in X) into A",
        inline=True)
comment(0x97C1, "Add 5 bytes of slack for trailing reply data", inline=True)
comment(0x97C3, "Stash the resulting end-of-buffer offset", inline=True)
comment(0x97C5, "Restore the original C flag from caller", inline=True)
comment(0x97C6, "C set: this is a disconnect; jump to handle_disconnect",
        inline=True)
comment(0x97C8, "Save flags again across the actual TX (TX clobbers them)",
        inline=True)
comment(0x97C9, "Send the four-way-handshake-initiated command packet",
        inline=True)
comment(0x97CC, "Restore caller's flags before falling into "
        "recv_and_process_reply", inline=True)

# parse_access_prefix inline comments (15 items)
comment(0xB22F, "Read first parsed-buffer character (the candidate prefix)",
        inline=True)
comment(0xB232, "EOR with '&'; Z set iff the byte was '&'", inline=True)
comment(0xB234, "Not '&': try ':' (and '#') instead", inline=True)
comment(0xB236, "Read fs_lib_flags", inline=True)
comment(0xB239, "Set bit 6 (URD-relative resolution flag)", inline=True)
comment(0xB23B, "Write back updated flags", inline=True)
comment(0xB23E, "Strip the '&' from the buffer (shift left + trim)",
        inline=True)
comment(0xB241, "Step caller's X back to account for the consumed "
        "character", inline=True)
comment(0xB242, "Re-read the (now first) buffer byte after the strip",
        inline=True)
comment(0xB245, "EOR with '.'; Z set iff '&.' pair (URD root)", inline=True)
comment(0xB247, "Not '&.': just '&' alone -- check for trailing '#'",
        inline=True)
comment(0xB249, "It was '&.': peek the byte after the dot", inline=True)
comment(0xB24C, "EOR with CR; Z set iff '&.<CR>' (illegal: dot needs a "
        "name to follow)", inline=True)
comment(0xB24E, "'&.<CR>' is invalid: raise 'Bad filename'", inline=True)
comment(0xB250, "Valid '&.<name>': step X back for the dot too", inline=True)

# print_file_server_is inline comments (3 items)
comment(0xB483, "Print 'File' via inline string", inline=True)
comment(0xB48A, "Clear V so the BVC below is taken", inline=True)
comment(0xB48B, "Always taken (V was just cleared); skip the 'Printer' "
        "prologue and reach the shared ' server is ' suffix",
        inline=True)

# print_printer_server_is inline comments (3 items)
comment(0xB48D, "Print 'Printer' via inline string", inline=True)
# 0xB497 is the inline-string terminator NOP that print_inline jumps
# back to; it consumes 1 cycle and then falls into the suffix
comment(0xB497, "Inline-string fallthrough lands here on terminator",
        inline=True)

# print_server_is_suffix inline comments (3 items)
comment(0xB498, "Print ' server is ' via inline string", inline=True)
comment(0xB4A6, "Inline-string fallthrough lands here", inline=True)
comment(0xB4A7, "Return; caller now prints the actual server "
        "(file or printer) address", inline=True)

# print_hex_and_space inline comments (5 items)
comment(0xBE37, "Save A so the caller can re-use the value", inline=True)
comment(0xBE38, "Print A as two hex digits", inline=True)
comment(0xBE3B, "A=' ': trailing column separator", inline=True)
comment(0xBE3D, "Print the space via OSASCI", inline=True)
comment(0xBE40, "Restore caller's A", inline=True)
comment(0xBE41, "Return", inline=True)

# print_fs_info_newline inline comments (3 items)
comment(0xA3BB, "Set V so print_station_addr suppresses the leading "
        "'0.' when the network number is zero", inline=True)
comment(0xA3BE, "Print the station/network address", inline=True)
comment(0xA3C1, "Tail-call OSNEWL for the trailing CR/LF", inline=True)

# parse_filename_arg inline comment (1 item)
comment(0xB22C, "Read the GSREAD-style filename argument into the "
        "&C030 buffer, then fall into parse_access_prefix",
        inline=True)

# print_station_addr inline comments (12 items)
comment(0xB556, "Save caller's V (controls leading-zero padding via the "
        "BVS at &B566)", inline=True)
comment(0xB557, "Read network number (fs_work_6)", inline=True)
comment(0xB559, "Network 0 means local: skip the 'NN.' prefix", inline=True)
comment(0xB55B, "Network non-zero: print as 3-digit decimal", inline=True)
comment(0xB55E, "A='.': separator between network and station",
        inline=True)
comment(0xB560, "Print the dot", inline=True)
comment(0xB563, "Set V so the next BVS branches over the padding "
        "(we just printed digits, no padding needed)", inline=True)
comment(0xB566, "V set: skip leading-space padding", inline=True)
comment(0xB568, "V clear (caller wanted padding): print 4 leading spaces "
        "via inline string", inline=True)
comment(0xB56F, "Read station number (fs_work_5)", inline=True)
comment(0xB571, "Restore caller's V (so print_decimal_3dig honours its "
        "own leading-zero suppression)", inline=True)
comment(0xB572, "Tail-call print_decimal_3dig for the station number",
        inline=True)

# print_version_header inline comments (3 items)
# 0x8C93 already has 'Print version string via inline' inline comment
comment(0x8CA9, "Inline-string fallthrough lands here on terminator",
        inline=True)
comment(0x8CAA, "Tail-call print_station_id to append ' Econet "
        "Station <n>' (and ' No Clock' if appropriate)", inline=True)

# ex_print_col_sep inline comments (8 items in body)
comment(0xB2E4, "Read fs_spool_handle (also column counter in *Cat mode)",
        inline=True)
comment(0xB2E6, "Negative: *Ex mode (one-per-line) -- skip column logic, "
        "just print newline", inline=True)
comment(0xB2E8, "Bump column counter", inline=True)
comment(0xB2E9, "Get the new value into A", inline=True)
comment(0xB2EA, "Wrap to 0..3 (4 columns per row)", inline=True)
comment(0xB2EC, "Save the new column index", inline=True)
comment(0xB2EE, "Wrapped to 0: end of row, print newline", inline=True)
comment(0xB2F0, "Mid-row: print 2-space column separator via inline",
        inline=True)

# print_decimal_3dig inline comments (5 items)
comment(0xB303, "Y = value to convert (digits read off via successive "
        "divisions)", inline=True)
comment(0xB304, "Divisor for hundreds digit", inline=True)
comment(0xB306, "Print hundreds digit", inline=True)
comment(0xB309, "Divisor for tens digit", inline=True)
comment(0xB30B, "Print tens digit", inline=True)
comment(0xB30E, "Divisor for units digit (always print at least the "
        "units to avoid the empty 0 case)", inline=True)

# print_decimal_digit inline comments (the body at &B310-&B326)
comment(0xB310, "Stash divisor in fs_error_ptr (the SBC target below)",
        inline=True)
# &B312 was previously misnamed cmd_remove; it's actually TYA
comment(0xB313, "X = '0'-1: digit counter, INX in the loop steps to '0' "
        "first", inline=True)
comment(0xB315, "Set carry for SBC", inline=True)
comment(0xB316, "Step quotient digit", inline=True)
comment(0xB317, "Subtract divisor", inline=True)
comment(0xB319, "No underflow: keep dividing", inline=True)
comment(0xB31B, "Underflow: add divisor back to recover the remainder",
        inline=True)
comment(0xB31D, "Remainder -> Y, ready for the next digit", inline=True)
comment(0xB31E, "Move digit ('0'-'9') from X into A for printing",
        inline=True)
comment(0xB31F, "Save divisor in X across the print (print_char_no_spool "
        "preserves X is not guaranteed)", inline=True)
comment(0xB321, "Print the digit, bypassing *SPOOL", inline=True)
comment(0xB324, "Restore divisor from X", inline=True)
comment(0xB326, "Return", inline=True)

# open_file_for_read inline comments (~28 items)
comment(0xBF78, "Save flags so caller's NZC survive", inline=True)
comment(0xBF79, "Move command-line offset Y into A for the add",
        inline=True)
comment(0xBF7A, "Clear C for the 16-bit add", inline=True)
comment(0xBF7B, "A = os_text_ptr_lo + Y (filename address low byte)",
        inline=True)
comment(0xBF7D, "Push it (we need to restore os_text_ptr after OSFIND)",
        inline=True)
comment(0xBF7E, "Move filename low into X (OSFIND wants the address in X/Y)",
        inline=True)
comment(0xBF7F, "A=0: zero high byte before the carry-add", inline=True)
comment(0xBF81, "Add os_text_ptr_hi with carry from the low add",
        inline=True)
comment(0xBF83, "Push filename high byte for the restore", inline=True)
comment(0xBF84, "Move filename high into Y", inline=True)
comment(0xBF85, "A=&40: OSFIND open-for-input mode", inline=True)
comment(0xBF87, "Open the file; returns handle in A (zero on failure)",
        inline=True)
comment(0xBF8A, "Copy returned handle into Y (also sets Z if zero)",
        inline=True)
comment(0xBF8B, "Stash the handle in ws_page for later close", inline=True)
comment(0xBF8D, "Non-zero: open succeeded, skip error path", inline=True)
comment(0xBF8F, "A=&D6: 'Not found' error code", inline=True)
comment(0xBF91, "Raise the error with the inline string below; never "
        "returns", inline=True)
# &BF94 inline string body
comment(0xBF9E, "Restore the saved filename high byte into "
        "os_text_ptr_hi -- but wait, this writes the FILENAME "
        "address into os_text_ptr; the caller intentionally moves "
        "os_text_ptr to scan past the filename below", inline=True)
comment(0xBFA1, "Restore filename low byte into os_text_ptr_lo (so "
        "(os_text_ptr) now points at the filename)", inline=True)
comment(0xBFA4, "Y=0: scan from start of filename", inline=True)
comment(0xBFA6, "Step to next byte", inline=True)
comment(0xBFA7, "Read filename byte", inline=True)
comment(0xBFA9, "Hit CR? End of command line", inline=True)
comment(0xBFAB, "Yes: filename ended at CR (no trailing spaces)",
        inline=True)
comment(0xBFAD, "Hit space? End of filename", inline=True)
comment(0xBFAF, "No (still inside filename): keep scanning", inline=True)
comment(0xBFB1, "Step past spaces", inline=True)
comment(0xBFB2, "Read next byte", inline=True)
comment(0xBFB4, "Still a space?", inline=True)
comment(0xBFB6, "Yes: keep skipping", inline=True)
comment(0xBFB8, "Done: Y points just past the filename and any spaces",
        inline=True)
comment(0xBFB9, "Restore caller's flags", inline=True)

# tx_econet_abort inline comments (~16 items)
comment(0xAD40, "Y=&D9: workspace offset for the abort code byte",
        inline=True)
comment(0xAD42, "Store the abort code (passed in A) at workspace[&D9]",
        inline=True)
comment(0xAD44, "A=&80: control = immediate-operation flag", inline=True)
comment(0xAD46, "Y=&0C: TXCB control-byte offset", inline=True)
comment(0xAD48, "Set TXCB[&0C] = &80 (immediate / abort)", inline=True)
comment(0xAD4A, "Save current net_tx_ptr low (we'll repoint TX at the "
        "abort packet)", inline=True)
comment(0xAD4C, "Push it for restore on exit", inline=True)
comment(0xAD4D, "Save net_tx_ptr high too", inline=True)
comment(0xAD4F, "Push it", inline=True)
comment(0xAD50, "TX low = &0C (abort packet starts at workspace[&0C])",
        inline=True)
comment(0xAD52, "Get nfs_workspace high byte", inline=True)
comment(0xAD54, "TX high = workspace page (so net_tx_ptr now points at "
        "the abort packet in workspace)", inline=True)
comment(0xAD56, "Send the abort packet via the standard TX path",
        inline=True)
comment(0xAD59, "A=&3F: TXCB status = abort-complete sentinel",
        inline=True)
comment(0xAD5B, "Write status via (net_tx_ptr,X) -- mark TX done",
        inline=True)
comment(0xAD5D, "Pull saved net_tx_ptr high", inline=True)
comment(0xAD5E, "Restore", inline=True)
comment(0xAD60, "Pull saved net_tx_ptr low", inline=True)
comment(0xAD61, "Restore -- caller's TX state intact", inline=True)
comment(0xAD63, "Return", inline=True)

# print_dump_header inline comments (14 items)
comment(0xBE01, "Read low nibble of starting address from (work_ae),Y",
        inline=True)
comment(0xBE03, "Save it (we'll print it 16 times incrementing each "
        "iteration)", inline=True)
comment(0xBE04, "Print '<CR>Address  : ' header via inline string",
        inline=True)
comment(0xBE13, "X=&0F: print 16 column-number digits", inline=True)
comment(0xBE15, "Pull the starting low nibble back into A", inline=True)
comment(0xBE16, "Print A as two hex digits + space", inline=True)
comment(0xBE19, "Set C ready for the increment", inline=True)
comment(0xBE1A, "ADC #0 with C set: A += 1 (the column index increments)",
        inline=True)
comment(0xBE1C, "Wrap to nibble (0..15)", inline=True)
comment(0xBE1E, "Step column counter", inline=True)
comment(0xBE1F, "Loop while X >= 0 (16 iterations)", inline=True)
comment(0xBE21, "Print ':    ASCII data<CR><CR>' trailer via inline",
        inline=True)
comment(0xBE35, "Inline-string fallthrough", inline=True)
comment(0xBE36, "Return", inline=True)

# parse_dump_range inline comments (~52 items)
# Phase 1: clear the 4-byte accumulator at (work_ae)
comment(0xBE42, "Move command-line offset Y into A for the X copy",
        inline=True)
comment(0xBE43, "X = current command-line offset (live cursor)",
        inline=True)
comment(0xBE44, "A=0: zero-fill value", inline=True)
comment(0xBE46, "Y=0: accumulator index", inline=True)
comment(0xBE47, "Zero accumulator byte at (work_ae)+Y", inline=True)
comment(0xBE49, "Step accumulator", inline=True)
comment(0xBE4A, "Done all 4 bytes?", inline=True)
comment(0xBE4C, "No: continue clearing", inline=True)
# Phase 2: read next character
comment(0xBE4E, "Reload command-line offset", inline=True)
comment(0xBE4F, "Step cursor", inline=True)
comment(0xBE50, "Y = stepped cursor (for the indirect read)", inline=True)
comment(0xBE51, "Read next command-line byte", inline=True)
comment(0xBE53, "CR? (end of address)", inline=True)
comment(0xBE55, "Yes: range parsed -- exit via space-skip", inline=True)
comment(0xBE57, "Space?", inline=True)
comment(0xBE59, "Yes: also a separator -- exit", inline=True)
comment(0xBE5B, "Below '0'?", inline=True)
comment(0xBE5D, "Yes: not hex -- raise 'Bad hex'", inline=True)
comment(0xBE5F, "Above '9'?", inline=True)
comment(0xBE61, "No: it's '0'-'9' -- skip the letter handling",
        inline=True)
comment(0xBE63, "Force uppercase via AND #&5F", inline=True)
comment(0xBE65, "Add &B8: 'A' (=&41) becomes &F9 with C set; 'F' becomes "
        "&FE; this maps 'A'-'F' to &FA-&FF in C", inline=True)
comment(0xBE67, "Carry out of ADC: digit was below 'A' -> bad hex",
        inline=True)
comment(0xBE69, "Below &FA? (i.e. before 'A' in mapped range)",
        inline=True)
comment(0xBE6B, "Yes (out of [&FA,&FF]): bad hex", inline=True)
# Mask to nibble and rotate accumulator
comment(0xBE6D, "Keep low nibble (0-15)", inline=True)
comment(0xBE6F, "Push the new nibble", inline=True)
comment(0xBE70, "Push X (current command-line offset)", inline=True)
comment(0xBE72, "X=4: rotate the 4-byte accumulator left 4 times",
        inline=True)
comment(0xBE74, "Y=0: byte index for the rotate", inline=True)
comment(0xBE76, "A=0 (and C clear from TYA's flags)", inline=True)
comment(0xBE77, "Save A onto stack so we can use PHP/PLP to round-trip "
        "carry through the rotate", inline=True)
comment(0xBE78, "Pull flags (effectively C clear from the TYA above; on "
        "later iterations C carries the bit shifted out)", inline=True)
comment(0xBE79, "Read next accumulator byte", inline=True)
comment(0xBE7B, "ROL: shift in C from below, shift out top bit to C",
        inline=True)
comment(0xBE7C, "Write back", inline=True)
comment(0xBE7E, "Save the new C", inline=True)
comment(0xBE7F, "Pull A back (PHA earlier)", inline=True)
comment(0xBE80, "Step accumulator byte", inline=True)
comment(0xBE81, "Done all 4 bytes?", inline=True)
comment(0xBE83, "No: rotate next byte", inline=True)
comment(0xBE85, "PHA/PLP: bring saved C into flag register", inline=True)
comment(0xBE86, "PLP", inline=True)
comment(0xBE87, "C set: a bit fell off the top -- overflow",
        inline=True)
comment(0xBE89, "Step rotate counter", inline=True)
comment(0xBE8A, "Loop while X != 0 (4 rotates total)", inline=True)
# OR new nibble into accumulator low byte
comment(0xBE8C, "Pull saved X (command-line offset)", inline=True)
comment(0xBE8D, "Restore X", inline=True)
comment(0xBE8E, "Pull saved nibble into A", inline=True)
comment(0xBE8F, "Y=0: low byte of accumulator", inline=True)
comment(0xBE91, "OR new nibble into accumulator[0]", inline=True)
comment(0xBE93, "Write back", inline=True)
comment(0xBE95, "Loop for next hex digit", inline=True)
# Overflow exit
comment(0xBE98, "Discard saved nibble", inline=True)
comment(0xBE99, "Discard saved X", inline=True)
comment(0xBE9A, "Set C: signal overflow to caller", inline=True)
comment(0xBE9B, "Return with C=1", inline=True)
# Bad-hex error path
comment(0xBE9C, "Close the dump file before raising the error",
        inline=True)
comment(0xBE9F, "Raise 'Bad hex' error; never returns", inline=True)
# Trailing-space skip
comment(0xBEA2, "Step past current space", inline=True)
comment(0xBEA3, "Read next byte", inline=True)
comment(0xBEA5, "Still a space?", inline=True)
comment(0xBEA7, "Yes: keep skipping", inline=True)
comment(0xBEA9, "Clear C: signal success", inline=True)
comment(0xBEAA, "Return", inline=True)

# svc5_irq_check inline comments (complete the partial)
comment(0x8028, "Save X (the ROM slot we're being called on behalf of)",
        inline=True)
comment(0x8029, "Save Y (the dispatch-path selector via its high bit)",
        inline=True)
comment(0x802A, "Read deferred-work flag at &0D65 (set by NMI when work "
        "queued)", inline=True)
comment(0x802D, "Non-zero: there's work to dispatch", inline=True)
comment(0x802F, "Zero: no work; restore Y", inline=True)
comment(0x8030, "Restore X", inline=True)
comment(0x8031, "Return to MOS (service unclaimed)", inline=True)
comment(0x8032, "A=&80: bit 7 -- the bit to clear in ACCCON", inline=True)
comment(0x8034, "TRB ACCCON: clear bit 7 (release IRR mask)",
        inline=True)
comment(0x8037, "Zero the deferred-work flag (we're handling it now)",
        inline=True)
comment(0x803A, "Bring saved Y back into A so BMI can test bit 7",
        inline=True)
comment(0x803B, "Bit 7 of caller's Y set: dispatch via PHA/PHA/RTS table",
        inline=True)
comment(0x803D, "Bit 7 clear: A=&FE = Econet RX event code", inline=True)
comment(0x803F, "Fire the event through EVNTV", inline=True)
comment(0x8042, "Tail-jump to tx_done_exit which restores X/Y and "
        "claims the service", inline=True)

# osword_8_handler inline comments (~22 items)
comment(0xADD3, "Y=&0E: scan 15 bytes (offsets 14..0) of the PB",
        inline=True)
comment(0xADD5, "Is the OSWORD number 7?", inline=True)
comment(0xADD7, "Yes: handle as either 7 or 8 -- both copy PB to ws",
        inline=True)
comment(0xADD9, "Is the OSWORD number 8?", inline=True)
comment(0xADDB, "Neither 7 nor 8: return early (other OSWORDs handled "
        "elsewhere)", inline=True)
comment(0xADDD, "X=&DB: workspace offset for the PB copy",
        inline=True)
comment(0xADDF, "Temporarily reuse nfs_workspace as the destination "
        "low byte (high byte already points at the workspace page)",
        inline=True)
comment(0xADE1, "Read PB[Y]", inline=True)
comment(0xADE3, "Write to (nfs_workspace),Y -- effectively writes to "
        "workspace[&DB+Y]", inline=True)
comment(0xADE5, "Step backwards through the 15 bytes", inline=True)
comment(0xADE6, "Loop while Y >= 0", inline=True)
comment(0xADE8, "INY: bring Y back to 0 for the next single-byte write",
        inline=True)
comment(0xADE9, "Decrement nfs_workspace low byte: now points at "
        "workspace[&DA] (one before the copied region)", inline=True)
comment(0xADEB, "Read original OSWORD number from osbyte_a_copy",
        inline=True)
comment(0xADED, "Store at workspace[&DA] -- so the abort packet header "
        "carries the OSWORD number", inline=True)
comment(0xADEF, "Restore nfs_workspace to its proper low byte (Y=0)",
        inline=True)
comment(0xADF1, "Y=&14: TXCB control offset", inline=True)
comment(0xADF3, "A=&E9: status code for OSWORD-passthrough abort",
        inline=True)
comment(0xADF5, "Store status at TXCB[&14]", inline=True)
comment(0xADF7, "A=1: abort code for tx_econet_abort", inline=True)
comment(0xADF9, "Send the abort packet", inline=True)
comment(0xADFC, "Restore nfs_workspace from X (X is unchanged across "
        "tx_econet_abort)", inline=True)

# parse_fs_ps_args inline comments (~17 items)
comment(0xA3C4, "Save caller's X (command-line offset cursor)",
        inline=True)
comment(0xA3C5, "A=0: clear the dot-seen flag for parse_addr_arg",
        inline=True)
comment(0xA3C7, "Store cleared dot-seen flag", inline=True)
comment(0xA3C9, "Parse first number (network or standalone station)",
        inline=True)
comment(0xA3CC, "C set: parse_addr_arg saw an empty argument -- skip "
        "station storage", inline=True)
comment(0xA3CE, "Save the network number in fs_work_7", inline=True)
comment(0xA3D0, "Save Y (current command-line cursor) for after the "
        "bridge poll", inline=True)
comment(0xA3D1, "Populate the bridge routing table -- returns local "
        "network number in A", inline=True)
comment(0xA3D4, "EOR with parsed network: Z set iff parse matched local",
        inline=True)
comment(0xA3D6, "Match: keep A=0 to mark local network", inline=True)
comment(0xA3D8, "Mismatch: A = parsed network number", inline=True)
comment(0xA3DA, "Store network number into fs_work_6 (the canonical "
        "form: 0=local, non-zero=remote)", inline=True)
comment(0xA3DC, "Restore Y", inline=True)
comment(0xA3DD, "Step Y past the dot separator", inline=True)
comment(0xA3DE, "Parse station number after the dot", inline=True)
comment(0xA3E1, "C set: no station after dot -- leave fs_work_5 alone",
        inline=True)
comment(0xA3E3, "Store parsed station in fs_work_5", inline=True)
comment(0xA3E5, "Restore caller's X", inline=True)
comment(0xA3E6, "Return", inline=True)

# cmd_bye inline comments (8 items)
comment(0x9776, "Y=0: process_all_fcbs filter (0 = all FCBs)",
        inline=True)
comment(0x9778, "Walk all 16 FCB slots, calling start_wipe_pass on each",
        inline=True)
comment(0x977B, "OSBYTE &77 = close *SPOOL and *EXEC files", inline=True)
comment(0x977D, "Close any open *SPOOL/*EXEC handles", inline=True)
comment(0x9780, "A=&40: bit 6 of fs_flags = 'FS in active session'",
        inline=True)
comment(0x9782, "TRB clears bit 6: mark FS session inactive", inline=True)
comment(0x9785, "Close every Econet client channel", inline=True)
comment(0x9788, "Y=&17: FS function code 'Bye' (logoff request)",
        inline=True)

# cmd_fs inline comments (~14 items)
comment(0xA398, "Read current FS station from workspace", inline=True)
comment(0xA39B, "Save in fs_work_5 (so 'no-arg' path can print it)",
        inline=True)
comment(0xA39D, "Read current FS network", inline=True)
comment(0xA3A0, "Save in fs_work_6", inline=True)
comment(0xA3A2, "Look at the first command-line byte", inline=True)
comment(0xA3A4, "Is it CR (no argument)?", inline=True)
comment(0xA3A6, "Yes: print the current FS address", inline=True)
comment(0xA3A8, "Parse 'net.station' arg into fs_work_5/6", inline=True)
comment(0xA3AB, "A=1: OSWORD &13 sub-function 1 = set file server "
        "station", inline=True)
comment(0xA3AD, "Store sub-function in PB[0]", inline=True)
comment(0xA3AF, "A=&13: OSWORD &13", inline=True)
comment(0xA3B1, "X = lo of PB pointer (fs_work_4 = &B4)", inline=True)
comment(0xA3B3, "Y = hi of PB pointer (=0, since fs_work_4 is in "
        "zero page)", inline=True)
comment(0xA3B5, "Tail-jump into OSWORD; the OS routes us back through "
        "osword_13_set_station", inline=True)

# parse_addr_arg inline comments (~73 items)
# Prologue: detect '&' (hex prefix) vs digit
comment(0x92B2, "Zero the accumulator (fs_load_addr_2)", inline=True)
comment(0x92B4, "Read first command-line byte", inline=True)
comment(0x92B6, "Hex prefix '&'?", inline=True)
comment(0x92B8, "No: try decimal path", inline=True)
comment(0x92BA, "Yes: skip the '&'", inline=True)
comment(0x92BB, "Read first hex digit", inline=True)
comment(0x92BD, "Always taken (CMP #'&' set C if A>='&'); jump into "
        "the hex digit-range check", inline=True)
# Hex digit loop
comment(0x92BF, "Step to next character", inline=True)
comment(0x92C0, "Read next hex digit candidate", inline=True)
comment(0x92C2, "Dot? Net.station separator", inline=True)
comment(0x92C4, "Yes: switch to station-parsing mode", inline=True)
comment(0x92C6, "Below '!' (CR/space)? End of argument", inline=True)
comment(0x92C8, "Yes: number complete", inline=True)
# Hex digit range validation
comment(0x92CA, "Below '0'?", inline=True)
comment(0x92CC, "Yes: not a hex digit", inline=True)
comment(0x92CE, "Above '9'? (CMP #':')", inline=True)
comment(0x92D0, "No (it's '0'-'9'): straight to digit extraction",
        inline=True)
comment(0x92D2, "Force uppercase via AND #&5F", inline=True)
comment(0x92D4, "Map 'A'-'F' to &FA-&FF (ADC #&B8 with C from earlier "
        "CMP #':' which set C)", inline=True)
comment(0x92D6, "Carry out of ADC: was below 'A' -- bad hex", inline=True)
comment(0x92D8, "Below &FA? (digit > 'F' overflowed past)", inline=True)
comment(0x92DA, "Yes: bad hex (out of [&FA,&FF])", inline=True)
# Extract and accumulate hex digit
comment(0x92DC, "Mask to nibble", inline=True)
comment(0x92DE, "Stash digit value in fs_load_addr_3", inline=True)
comment(0x92E0, "Load accumulator", inline=True)
comment(0x92E2, "Above 16? (would overflow when shifted left 4)",
        inline=True)
comment(0x92E4, "Yes: overflow", inline=True)
comment(0x92E6, "Shift accumulator left 4 (multiply by 16)", inline=True)
comment(0x92E7, "(shift 2)", inline=True)
comment(0x92E8, "(shift 3)", inline=True)
comment(0x92E9, "(shift 4)", inline=True)
comment(0x92EA, "Add new nibble", inline=True)
comment(0x92EC, "Save updated accumulator", inline=True)
comment(0x92EE, "No carry: continue (always taken since accumulator "
        "was checked < 16 above)", inline=True)
# Decimal digit loop
comment(0x92F0, "Read next decimal-digit candidate", inline=True)
comment(0x92F2, "Dot? Net.station separator", inline=True)
comment(0x92F4, "Yes: switch to station-parsing mode", inline=True)
comment(0x92F6, "Below '!' (CR/space)?", inline=True)
comment(0x92F8, "Yes: number complete", inline=True)
comment(0x92FA, "Test for '0'-'9' and reject '&'/'.'", inline=True)
comment(0x92FD, "Not a decimal digit: bad number", inline=True)
comment(0x92FF, "Mask to nibble", inline=True)
comment(0x9301, "Stash digit", inline=True)
comment(0x9303, "ASL accumulator (* 2)", inline=True)
comment(0x9305, "Overflowed: too big for byte", inline=True)
comment(0x9307, "Reload doubled value", inline=True)
comment(0x9309, "* 2 again (now * 4)", inline=True)
comment(0x930A, "Overflow check", inline=True)
comment(0x930C, "* 2 again (now * 8)", inline=True)
comment(0x930D, "Overflow check", inline=True)
comment(0x930F, "+ accumulator (now * 8 + * 2 = * 10)", inline=True)
comment(0x9311, "Overflow check", inline=True)
comment(0x9313, "+ new digit", inline=True)
comment(0x9315, "Overflow check", inline=True)
comment(0x9317, "Save * 10 + digit", inline=True)
comment(0x9319, "Step input cursor", inline=True)
comment(0x931A, "Always taken (Y wraps at 256, never zero in practice)",
        inline=True)
# Termination / validation
comment(0x931C, "Read mode flag", inline=True)
comment(0x931E, "Bit 7 clear: in net.station mode -- validate result",
        inline=True)
comment(0x9320, "Decimal-only mode: get result", inline=True)
comment(0x9322, "Result is zero: bad parameter", inline=True)
comment(0x9324, "Return with parsed result in A (decimal-only path)",
        inline=True)
# Station validation
comment(0x9325, "Reload result", inline=True)
comment(0x9327, "Station 255 is reserved (broadcast)", inline=True)
comment(0x9329, "Yes: bad station number", inline=True)
comment(0x932B, "Reload result for the next test", inline=True)
comment(0x932D, "Non-zero: valid station, return", inline=True)
comment(0x932F, "Zero result: must have followed a dot to be valid",
        inline=True)
comment(0x9331, "No dot was seen: bad station number", inline=True)
comment(0x9333, "Dot seen: peek the byte before current cursor",
        inline=True)
comment(0x9334, "Read previous byte", inline=True)
comment(0x9336, "Restore Y", inline=True)
comment(0x9337, "Was previous char '.'?", inline=True)
comment(0x9339, "No: bad station number", inline=True)
comment(0x933B, "All checks passed: C=1 marks 'parsed successfully'",
        inline=True)
comment(0x933C, "Return", inline=True)
# Dot separator handler
comment(0x933D, "Dot already seen?", inline=True)
comment(0x933F, "Yes: 'Bad number' (multiple dots)", inline=True)
comment(0x9341, "Set dot-seen flag", inline=True)
comment(0x9343, "Get parsed network number (before dot)", inline=True)
comment(0x9345, "Network 255 is reserved", inline=True)
comment(0x9347, "Yes: 'Bad network number'", inline=True)
comment(0x9349, "Return; caller continues parsing the station", inline=True)

# netv_claim_release inline comments (~37 items)
comment(0xAD64, "Y = OSWORD parameter-block pointer high byte (used as "
        "an 'unrecognised' sentinel below)", inline=True)
comment(0xAD66, "Code &81? (compatibility shortcut for one specific "
        "claim type)", inline=True)
comment(0xAD68, "Yes: skip table scan, use match-result with Y already "
        "set non-zero", inline=True)
comment(0xAD6A, "Y=1: state 2 marker", inline=True)
comment(0xAD6C, "X=&0A: scan first 11 entries (table indices 0..&0A)",
        inline=True)
comment(0xAD6E, "Look up A in the claim code table", inline=True)
comment(0xAD71, "Match: handle as state 2", inline=True)
comment(0xAD73, "DEY: Y=0 (state 3 marker, two DEYs from 1)", inline=True)
comment(0xAD74, "(second DEY)", inline=True)
comment(0xAD75, "X=&11: scan all 18 entries (state 3 also accepts "
        "the extended range)", inline=True)
comment(0xAD77, "Look up A again with extended range", inline=True)
comment(0xAD7A, "Match: handle as state 3", inline=True)
comment(0xAD7C, "INY: Y=1 again (no match found, will return below)",
        inline=True)
# process_match_result
comment(0xAD7D, "X=2: default state code passed to tx_econet_abort",
        inline=True)
comment(0xAD7F, "Move match marker (Y) into A for the BEQ test",
        inline=True)
comment(0xAD80, "Y=0 (no match): return without action", inline=True)
comment(0xAD82, "Save flags so we can branch later on Y's sign",
        inline=True)
comment(0xAD83, "Y > 0 (state 2): skip the X bump", inline=True)
comment(0xAD85, "State 3: X=3 (different abort code)", inline=True)
# save_tube_state
comment(0xAD86, "Y=&DC: workspace offset for tube state bytes",
        inline=True)
comment(0xAD88, "Read tube_claimed_id,Y", inline=True)
comment(0xAD8B, "Save in workspace[&DC..]", inline=True)
comment(0xAD8D, "Step backwards", inline=True)
comment(0xAD8E, "Done at &DA?", inline=True)
comment(0xAD90, "Loop while Y > &DA (saves &DA, &DB, &DC -- 3 bytes)",
        inline=True)
comment(0xAD92, "Move state code (2 or 3) into A for the abort",
        inline=True)
comment(0xAD93, "Send abort with the state code", inline=True)
comment(0xAD96, "Restore the saved flags (Y's sign)", inline=True)
comment(0xAD97, "Y was positive (state 2): just return", inline=True)
# State 3 polling path
comment(0xAD99, "A=&7F: 'pending response' control value", inline=True)
comment(0xAD9B, "Y=&0C: TXCB control offset", inline=True)
comment(0xAD9D, "Mark TXCB as pending", inline=True)
comment(0xAD9F, "Read TXCB status byte", inline=True)
comment(0xADA1, "Bit 7 still clear: keep polling for response",
        inline=True)
comment(0xADA3, "Capture S so we can patch the caller's stack frame",
        inline=True)
comment(0xADA4, "Y=&DD: highest workspace offset for the response copy",
        inline=True)
comment(0xADA6, "Read first response byte (workspace[&DD])", inline=True)
comment(0xADA8, "OR with 'D' (&44): some flag bit?", inline=True)
comment(0xADAA, "Always taken (after ORA result is non-zero); store "
        "into stack[&106+X] then walk down", inline=True)
# Restore-stack loop
comment(0xADAC, "Step Y down", inline=True)
comment(0xADAD, "Step X down (stack offset)", inline=True)
comment(0xADAE, "Read next workspace byte", inline=True)
comment(0xADB0, "Patch caller's stack frame at &106+X", inline=True)
comment(0xADB3, "Reached &DA (lower workspace bound)?", inline=True)
comment(0xADB5, "No: keep restoring", inline=True)
comment(0xADB7, "Return", inline=True)

# cmd_wipe inline comments (~30 items in classified body)
comment(0xB6F3, "Reset access flags before parsing the new argument",
        inline=True)
comment(0xB6F6, "A=0: clear the file-iteration counter", inline=True)
comment(0xB6F8, "Store iteration counter (steps to next file each loop)",
        inline=True)
comment(0xB6FA, "Save text pointer for re-reading the wildcard each "
        "iteration", inline=True)
comment(0xB6FD, "Parse the wildcard filename into the &C030 buffer",
        inline=True)
comment(0xB700, "Step X past the CR terminator (so X = filename length+1)",
        inline=True)
comment(0xB701, "Save end-of-buffer offset", inline=True)
# request_next_wipe
comment(0xB703, "FS function code byte 0 = 1 (examine)", inline=True)
comment(0xB705, "TXCB[5] = 1: 'examine directory entry'", inline=True)
comment(0xB708, "TXCB[7] = 1: ditto for the second buffer slot",
        inline=True)
comment(0xB70B, "Load current iteration index", inline=True)
comment(0xB70D, "TXCB[6] = iteration index (which directory entry)",
        inline=True)
comment(0xB710, "X=3: copy starting at TX[3] (after the FS header bytes)",
        inline=True)
comment(0xB712, "Copy the parsed filename into the TX buffer", inline=True)
comment(0xB715, "Y=3: FS function code 'Examine'", inline=True)
comment(0xB717, "A=&80: set bit 7 of need_release_tube to flag long-lived "
        "TX", inline=True)
comment(0xB719, "Store flag", inline=True)
comment(0xB71B, "Send the examine request and wait for reply",
        inline=True)
comment(0xB71E, "Read FS reply byte 0 (status code)", inline=True)
comment(0xB721, "Non-zero status: process the response", inline=True)
# No-more-files exit path
comment(0xB723, "OSBYTE &0F: flush input buffer class", inline=True)
comment(0xB725, "X=1: flush keyboard buffer", inline=True)
comment(0xB727, "Flush keyboard buffer (clear pending Y/N keypress)",
        inline=True)
comment(0xB72A, "OSBYTE &7A: scan keyboard from key 16 (clear keypress "
        "queue)", inline=True)
comment(0xB72C, "Run the scan", inline=True)
comment(0xB72F, "Y=0: no key", inline=True)
comment(0xB731, "OSBYTE &78: write keys-pressed state", inline=True)
comment(0xB733, "Tail-call OSBYTE: clean up and return", inline=True)
# check_wipe_attr loop
comment(0xB736, "Read attribute byte from FS reply (TXCB[&2F])",
        inline=True)
comment(0xB739, "Is it 'L' (locked)?", inline=True)
comment(0xB73B, "Not locked: check for directory", inline=True)
comment(0xB73D, "Locked: skip this file, advance to next", inline=True)
comment(0xB73F, "Loop back to request the next directory entry",
        inline=True)
comment(0xB742, "Is it 'D' (directory)?", inline=True)
comment(0xB744, "Not a directory: prompt the user", inline=True)
comment(0xB746, "Directory: check second attribute byte (size)",
        inline=True)
comment(0xB749, "Loop back to attribute test (re-checks if non-empty)",
        inline=True)
# Display filename + Y/N prompt
comment(0xB74B, "X=1: scan name starting at TX[1]", inline=True)
comment(0xB74D, "Y = end-of-buffer offset (saved earlier in fs_work_6)",
        inline=True)
comment(0xB74F, "Read filename byte from TX[6+X]", inline=True)
comment(0xB752, "Print via *SPOOL-bypassing OSASCI", inline=True)
comment(0xB755, "Also store into the parse buffer for later use",
        inline=True)
comment(0xB758, "Step parse-buffer offset", inline=True)
comment(0xB759, "Step TX-buffer offset", inline=True)
comment(0xB75A, "Reached &0C (12 chars)?", inline=True)
comment(0xB75C, "No: continue copying", inline=True)
comment(0xB75E, "Print '(Y/N/?) ' prompt and read response", inline=True)
comment(0xB761, "Restore caller's flags (saved by sub_c928a)",
        inline=True)

# byte_to_2bit_index inline comments (12 items)
# This computes A * 12 with overflow clamping. The PHA/TSX/PHP/ADC
# stack-X trick is the standard 6502 idiom for adding a saved value
# without using zero-page scratch.
comment(0xA3E9, "Multiply A by 2", inline=True)
comment(0xA3EA, "Multiply A by 2 again -- A is now A_orig * 4",
        inline=True)
comment(0xA3EB, "Stash A_orig * 4 on the stack", inline=True)
comment(0xA3EC, "Multiply A by 2 -- A is now A_orig * 8 (C = bit 7 of "
        "A_orig*4)", inline=True)
comment(0xA3ED, "Capture S so we can read the just-pushed value",
        inline=True)
comment(0xA3EE, "Save the C flag from the third ASL", inline=True)
comment(0xA3EF, "ADC stack[X+1] = A_orig*4 (with C from the ASL): "
        "A = A_orig*8 + A_orig*4 + C = A_orig*12 + C", inline=True)
comment(0xA3F2, "ROR halves the result, putting the new C as bit 7",
        inline=True)
comment(0xA3F3, "Restore the saved C (from the third ASL)", inline=True)
comment(0xA3F4, "ASL doubles the halved value (effectively undoes the "
        "ROR's divide while reusing C)", inline=True)
comment(0xA3F5, "Y = A_orig * 12 (the 12-byte-aligned index)",
        inline=True)
comment(0xA3F6, "Recover A_orig * 4 (left on the stack at &A3EB)",
        inline=True)
comment(0xA3F7, "Above &48 (i.e. A_orig * 4 >= 72, A_orig >= 18)?",
        inline=True)
comment(0xA3F9, "No: keep computed Y", inline=True)
comment(0xA3FB, "Yes: clamp Y to 0 (out of range)", inline=True)
comment(0xA3FD, "Mirror Y -> A so callers can test Z", inline=True)
comment(0xA3FE, "Return; Y holds 12-byte-aligned offset, A is "
        "non-zero on success", inline=True)

# copy_ps_data inline comments (5 items)
comment(0xB3D7, "X=&F8: walks 0..7 via wraparound (loads from "
        "&8DA7+&F8=&8E9F, the ps_template_data base)", inline=True)
comment(0xB3D9, "Read template byte from ps_template_data + (X-&F8)",
        inline=True)
comment(0xB3DC, "Store into RX buffer at offset Y", inline=True)
comment(0xB3DE, "Step destination", inline=True)
comment(0xB3DF, "Step source -- wraps from &FF to &00 to terminate",
        inline=True)
comment(0xB3E0, "Loop while X != 0 (8 iterations: &F8..&FF)", inline=True)
comment(0xB3E2, "Return", inline=True)

# init_dump_buffer inline comments (~50 items)
comment(0xBEAB, "Step Y past the *Dump command name into the argument",
        inline=True)
comment(0xBEAC, "Save the cursor offset", inline=True)
comment(0xBEAE, "Set bit 0 of addr_work to 1 -- 'mode' flag for "
        "parse_dump_range below", inline=True)
comment(0xBEB0, "Save mode flag", inline=True)
comment(0xBEB2, "Parse the start address (max 4 hex digits)",
        inline=True)
comment(0xBEB5, "Overflow: too many digits", inline=True)
comment(0xBEB7, "Save current Y (cursor after start address)",
        inline=True)
comment(0xBEB8, "Push it", inline=True)
comment(0xBEB9, "Y = file handle saved in ws_page", inline=True)
comment(0xBEBB, "X=&AA: zero-page address for OSARGS result", inline=True)
comment(0xBEBD, "A=2: OSARGS sub-fn 2 = read sequential file extent",
        inline=True)
comment(0xBEBF, "Get file size into 4 bytes at &AA", inline=True)
comment(0xBEC2, "Y=3: compare 4-byte values (high to low)", inline=True)
comment(0xBEC4, "Read file size byte at &AA+Y", inline=True)
comment(0xBEC7, "Compare with parsed start address (work_ae+Y)",
        inline=True)
comment(0xBEC9, "Mismatch: branch decides which is bigger", inline=True)
comment(0xBECB, "Step to next byte", inline=True)
comment(0xBECC, "Loop while Y >= 0 (covers indices 3, 2, 1, 0)",
        inline=True)
comment(0xBECE, "All bytes equal: start = extent (allowed); jump to "
        "the post-validation path", inline=True)
comment(0xBED0, "C clear: parsed_start > file_size -- reject",
        inline=True)
comment(0xBED2, "Y=&FF: signal 'no copy needed' to the loop below",
        inline=True)
comment(0xBED4, "Always taken: skip directly to advance phase",
        inline=True)
# Outside-file error
comment(0xBED6, "Close the file before raising", inline=True)
comment(0xBED9, "A=&B7: 'Outside file' error code", inline=True)
comment(0xBEDB, "Raise via inline string; never returns", inline=True)
# Copy/advance phase
comment(0xBEEB, "Copy file-extent byte from osword_flag to (work_ae)",
        inline=True)
comment(0xBEED, "Store it (used as default end address)", inline=True)
comment(0xBEF0, "Step Y", inline=True)
comment(0xBEF1, "Done all 4 bytes?", inline=True)
comment(0xBEF3, "No: continue copying", inline=True)
comment(0xBEF5, "X=&AA: zero-page source for the OSARGS write-back",
        inline=True)
comment(0xBEF7, "Y = file handle", inline=True)
comment(0xBEF9, "A=1: OSARGS sub-fn 1 = write sequential file pointer",
        inline=True)
comment(0xBEFB, "Set the file's read pointer to the parsed start",
        inline=True)
comment(0xBEFE, "Pull saved cursor offset", inline=True)
comment(0xBEFF, "Restore into Y", inline=True)
# Optional second argument or default-base setup
comment(0xBF00, "Read next command-line byte", inline=True)
comment(0xBF02, "CR (end of args)?", inline=True)
comment(0xBF04, "No: there's a second arg -- handle below", inline=True)
comment(0xBF06, "Y=1: copy os_text_ptr (2 bytes) to work_ae as a "
        "displacement-base hint", inline=True)
comment(0xBF08, "Read os_text_ptr+Y", inline=True)
comment(0xBF0B, "Save in work_ae+Y", inline=True)
comment(0xBF0D, "Step backwards", inline=True)
comment(0xBF0E, "Loop while Y >= 0", inline=True)
comment(0xBF10, "A=5: OSFILE sub-fn 5 = read catalogue info", inline=True)
comment(0xBF12, "X = filename pointer low (work_ae)", inline=True)
comment(0xBF14, "Y = filename pointer high (addr_work)", inline=True)
comment(0xBF16, "Read load address into work_ae+0..3", inline=True)
# Shift OSFILE returned data
comment(0xBF19, "Y=2: shift 3 bytes down 2 positions to drop the "
        "first 2 bytes (action code + a flag)", inline=True)
comment(0xBF1B, "Read source byte", inline=True)
comment(0xBF1D, "Y -= 2 (destination)", inline=True)
comment(0xBF1E, "(second DEY)", inline=True)
comment(0xBF1F, "Store at destination", inline=True)
comment(0xBF21, "Y += 3 to advance to next source", inline=True)
comment(0xBF22, "(second INY)", inline=True)
comment(0xBF23, "(third INY)", inline=True)
comment(0xBF24, "Done 6 bytes shifted?", inline=True)
comment(0xBF26, "No: continue", inline=True)
# Detect &FF-pad load address
comment(0xBF28, "Y -= 2: position at high byte of load address",
        inline=True)
comment(0xBF29, "(second DEY)", inline=True)
comment(0xBF2A, "Read load-address byte at Y", inline=True)
comment(0xBF2C, "Is it &FF (signals no real load address)?", inline=True)
comment(0xBF2E, "No: have a real load address; add it as displacement",
        inline=True)
comment(0xBF30, "Yes: step back to next higher byte", inline=True)
comment(0xBF31, "Loop until Y=0", inline=True)
comment(0xBF33, "All four bytes were &FF: zero out the load address",
        inline=True)
comment(0xBF35, "A=0", inline=True)
comment(0xBF37, "Zero work_ae+Y", inline=True)
comment(0xBF39, "Step backwards", inline=True)
comment(0xBF3A, "Loop while Y >= 0", inline=True)
comment(0xBF3C, "Always taken (after BPL drops out): skip second-arg "
        "path", inline=True)
# Second-argument path
comment(0xBF3E, "Parse end-address argument", inline=True)
comment(0xBF41, "Success: continue with displacement-add", inline=True)
comment(0xBF43, "Parse error: close file then raise 'Bad address'",
        inline=True)
comment(0xBF46, "A=&FC: 'Bad address' error code", inline=True)
comment(0xBF48, "Raise; never returns", inline=True)
# Add displacement base
comment(0xBF53, "Y=0: start of work_ae", inline=True)
comment(0xBF55, "X=4: 4-byte add", inline=True)
comment(0xBF57, "Clear C for the add", inline=True)

# cmd_dump inline comments (~80 items)
# Setup
comment(0xBD41, "Open the file (handle stored in ws_page)", inline=True)
comment(0xBD44, "X=&14: 21-byte stack buffer for dump line state",
        inline=True)
comment(0xBD46, "A=0: zero-fill", inline=True)
comment(0xBD48, "Push zero", inline=True)
comment(0xBD49, "Step counter", inline=True)
comment(0xBD4A, "Loop while X >= 0 (21 zeros)", inline=True)
comment(0xBD4C, "Capture stack pointer for later restore", inline=True)
comment(0xBD4D, "Parse address range and validate against file extent",
        inline=True)
comment(0xBD50, "Read low nibble of starting address", inline=True)
comment(0xBD52, "Mask high nibble (top 4 bits)", inline=True)
comment(0xBD54, "Aligned (high nibble zero): skip the header print",
        inline=True)
comment(0xBD56, "Print 'Address: 00 01 ... 0F: ASCII data' header",
        inline=True)
# Outer line loop
comment(0xBD59, "Test escape and abort if pressed", inline=True)
comment(0xBD5C, "A=&FF: count counter starts here so first INC -> 0",
        inline=True)
comment(0xBD5E, "Save counter (-1)", inline=True)
comment(0xBD60, "Y = file handle", inline=True)
comment(0xBD62, "Read one byte via OSBGET (C set on EOF)", inline=True)
comment(0xBD65, "EOF: finish off this line then exit", inline=True)
comment(0xBD67, "Increment count counter", inline=True)
comment(0xBD69, "Y = current count (also buffer offset)", inline=True)
comment(0xBD6B, "Store byte in 16-byte line buffer at (work_ae)+Y",
        inline=True)
comment(0xBD6D, "Done all 16 bytes?", inline=True)
comment(0xBD6F, "No: read next byte", inline=True)
comment(0xBD71, "C clear: not EOF (clean line)", inline=True)
# Test for early exit
comment(0xBD72, "Save the EOF/clean flag", inline=True)
comment(0xBD73, "Reload counter byte", inline=True)
comment(0xBD75, "Bit 7 clear (counter is 0..&7F): bytes were read",
        inline=True)
comment(0xBD77, "EOF and no bytes: clean up and exit", inline=True)
comment(0xBD79, "Restore one stack byte", inline=True)
comment(0xBD7A, "Step", inline=True)
comment(0xBD7B, "Loop while X >= 0 (22 pulls)", inline=True)
comment(0xBD7D, "Tail-jump to close_ws_file", inline=True)
# Header on 256-byte boundary
comment(0xBD80, "Y=&10: read displayed-address byte 0", inline=True)
comment(0xBD82, "Read low byte", inline=True)
comment(0xBD84, "Top nibble", inline=True)
comment(0xBD86, "Non-zero: not a 256-byte boundary, skip header",
        inline=True)
comment(0xBD88, "Boundary: print column header", inline=True)
# Print 4-byte hex address
comment(0xBD8B, "Y=&13: highest byte of 4-byte address", inline=True)
comment(0xBD8D, "Read address byte (highest first)", inline=True)
comment(0xBD8F, "Save it (print_hex_byte clobbers A)", inline=True)
comment(0xBD90, "Print as 2 hex digits", inline=True)
comment(0xBD93, "Restore A", inline=True)
comment(0xBD94, "Step backwards", inline=True)
comment(0xBD95, "Reached low byte (offset &0F)?", inline=True)
comment(0xBD97, "No: continue printing", inline=True)
# Increment 4-byte address by 16
comment(0xBD99, "Y=&10: low byte of address", inline=True)
comment(0xBD9A, "Clear C", inline=True)
comment(0xBD9B, "ADC #&10: bump address by 16 bytes for next line",
        inline=True)
comment(0xBD9D, "Save C from the add", inline=True)
comment(0xBD9E, "Restore C from previous step", inline=True)
comment(0xBD9F, "Store updated address byte", inline=True)
comment(0xBDA1, "Step Y up", inline=True)
comment(0xBDA2, "Read next byte", inline=True)
comment(0xBDA4, "Add carry from below", inline=True)
comment(0xBDA6, "Save C", inline=True)
comment(0xBDA7, "Done all 4 bytes (Y=&14)?", inline=True)
comment(0xBDA9, "No: continue propagating", inline=True)
comment(0xBDAB, "Restore final C", inline=True)
comment(0xBDAC, "Print ' : ' separator before hex byte field",
        inline=True)
# Print 16 hex bytes
comment(0xBDB2, "Y=0: start of buffer", inline=True)
comment(0xBDB4, "X = byte counter (-1 initially, INC'd to 0..&0F)",
        inline=True)
comment(0xBDB6, "Read byte from buffer", inline=True)
comment(0xBDB8, "Print as hex + space", inline=True)
comment(0xBDBB, "Step buffer offset", inline=True)
comment(0xBDBC, "Done all 16?", inline=True)
comment(0xBDBE, "Yes: print separator before ASCII field", inline=True)
comment(0xBDC0, "Step counter (Y was off-by-one from line read)",
        inline=True)
comment(0xBDC1, "Have a real byte? Print it", inline=True)
comment(0xBDC3, "End of partial line: pad with 3 spaces", inline=True)
comment(0xBDC4, "Print '   ' inline", inline=True)
comment(0xBDCA, "Inline-string fallthrough", inline=True)
comment(0xBDCB, "Restore Y", inline=True)
comment(0xBDCC, "Continue padding the rest of the hex column",
        inline=True)
# Separator + ASCII field
comment(0xBDCF, "Counter has finished -- step it once more for the "
        "ASCII test", inline=True)
comment(0xBDD0, "Print ': ' inline (ASCII field separator)", inline=True)
comment(0xBDD5, "Y=0: rewind to start of line buffer", inline=True)
comment(0xBDD7, "Skip 8 padding spaces if needed (advance_x_by_8)",
        inline=True)
comment(0xBDDA, "Read line buffer byte", inline=True)
comment(0xBDDC, "Mask off bit 7 (DEL/inverted)", inline=True)
comment(0xBDDE, "Below ' '? (control char)", inline=True)
comment(0xBDE0, "Yes: skip to substitution", inline=True)
comment(0xBDE2, "Substitute '.' for non-printables", inline=True)
comment(0xBDE4, "Compare with DEL", inline=True)
comment(0xBDE6, "Equal: also non-printable, substitute '.'", inline=True)
comment(0xBDE8, "Print the (possibly substituted) character", inline=True)
comment(0xBDEB, "Step Y", inline=True)
comment(0xBDEC, "Done 16 chars?", inline=True)
comment(0xBDEE, "Yes: end this line", inline=True)
comment(0xBDF0, "Step counter back", inline=True)
comment(0xBDF1, "Loop while X >= 0", inline=True)
comment(0xBDF3, "Print newline at end of line", inline=True)
comment(0xBDF6, "Restore EOF flag", inline=True)
comment(0xBDF7, "EOF: tidy up and exit", inline=True)
comment(0xBDF9, "More to dump: jump to next line", inline=True)
comment(0xBDFC, "X=&14: balance the loop_pop_stack_buf counter",
        inline=True)
comment(0xBDFE, "Tail-jump to clean up the 21-byte stack buffer and "
        "close the file", inline=True)

# pop_requeue_ps_scan inline comments (~50 items)
# Restore caller's stack-saved state and prepare to walk PS slots
comment(0xB4B4, "Pull saved upper byte of ws_ptr_lo+osword_flag pair",
        inline=True)
comment(0xB4B5, "Save into osword_flag", inline=True)
comment(0xB4B7, "Pull lower byte", inline=True)
comment(0xB4B8, "Save into ws_ptr_lo", inline=True)
comment(0xB4BA, "Push 0 -- placeholder, will be the stacked return "
        "marker", inline=True)
comment(0xB4BC, "Push it", inline=True)
comment(0xB4BD, "ws_ptr_hi base = &84 (start of PS slot table area)",
        inline=True)
comment(0xB4BF, "Save base", inline=True)
comment(0xB4C1, "Shift bit 0 of econet_flags into C (saved scan state)",
        inline=True)
comment(0xB4C4, "A=3: PS slot index counter", inline=True)
# Slot scan loop
comment(0xB4C6, "Convert slot index to 12-byte-aligned table offset",
        inline=True)
comment(0xB4C9, "Out of range (clamped to 0): all slots scanned",
        inline=True)
comment(0xB4CB, "A /= 2 (shift down)", inline=True)
comment(0xB4CC, "A /= 2 again (now slot index * 4 / 4 = slot index)",
        inline=True)
comment(0xB4CD, "X = slot index", inline=True)
comment(0xB4CE, "Read slot's status byte at workspace[Y]", inline=True)
comment(0xB4D0, "Slot empty (0): scan done", inline=True)
comment(0xB4D2, "Slot is '?' (uninitialised marker)?", inline=True)
comment(0xB4D4, "Yes: re-init this slot's data", inline=True)
# Skip-next-slot
comment(0xB4D6, "Step slot index", inline=True)
comment(0xB4D7, "Move to A for next iteration", inline=True)
comment(0xB4D8, "Loop while X != 0 (wraps when all slots done)",
        inline=True)
# Re-init '?' slot
comment(0xB4DA, "Save Y (slot table offset)", inline=True)
comment(0xB4DB, "Push it", inline=True)
comment(0xB4DC, "A=&7F: slot status 'busy/active'", inline=True)
comment(0xB4DE, "Mark slot active", inline=True)
comment(0xB4E0, "Step Y to control byte", inline=True)
comment(0xB4E1, "A=&9E: control byte (Master 128 PS-init pattern)",
        inline=True)
comment(0xB4E3, "Store control byte", inline=True)
comment(0xB4E5, "A=0: zero-fill the next two bytes", inline=True)
comment(0xB4E7, "Write two zeros, advance Y", inline=True)
comment(0xB4EA, "Read current ws_ptr_hi", inline=True)
comment(0xB4EC, "Store as buffer-link low byte", inline=True)
comment(0xB4EE, "Clear C ready for the +3", inline=True)
comment(0xB4EF, "Save flags so the ADC's C doesn't leak", inline=True)
comment(0xB4F0, "Bump ws_ptr_hi by 3 (next slot's base)", inline=True)
comment(0xB4F2, "Restore flags", inline=True)
comment(0xB4F3, "Save updated ws_ptr_hi", inline=True)
comment(0xB4F5, "Write buffer page + two &FF sentinels", inline=True)
comment(0xB4F8, "Read ws_ptr_hi (now updated)", inline=True)
comment(0xB4FA, "Store as second-link byte", inline=True)
comment(0xB4FC, "Write another buffer page + two &FF sentinels",
        inline=True)
comment(0xB4FF, "Continue scanning slots", inline=True)
# Done scanning -- delay loop
comment(0xB502, "Restore bit 0 of econet_flags via ASL (recovers from "
        "the LSR at &B4C1)", inline=True)
comment(0xB505, "Pull saved ws_ptr_lo", inline=True)
comment(0xB507, "Push it back (the caller's return-resume sequence)",
        inline=True)
comment(0xB508, "Pull saved osword_flag", inline=True)
comment(0xB50A, "Push it back", inline=True)
comment(0xB50B, "A=&0A: outer counter", inline=True)
comment(0xB50D, "Y=&0A: inner counter", inline=True)
comment(0xB50E, "X=&0A: middle counter", inline=True)
comment(0xB50F, "Save outer in fs_work_4", inline=True)
comment(0xB511, "Decrement inner counter", inline=True)
comment(0xB512, "Inner not zero: keep delaying", inline=True)
comment(0xB514, "Decrement middle", inline=True)
comment(0xB515, "Middle not zero: refresh inner and continue",
        inline=True)
comment(0xB517, "Decrement outer in fs_work_4", inline=True)
comment(0xB519, "Outer not zero: another full sweep (~1000 cycles)",
        inline=True)
comment(0xB51B, "Return", inline=True)

# cond_save_error_code inline comments (4 items)
comment(0x9900, "Test bit 7 of fs_flags (FS-active flag)", inline=True)
comment(0x9903, "FS not active: skip the save", inline=True)
comment(0x9905, "FS active: store error code at &C009 (last-error byte)",
        inline=True)
comment(0x9908, "Return", inline=True)

# build_no_reply_error inline comments (~15 items)
comment(0x9909, "X=8: net_error_lookup_data offset for 'No reply' "
        "message", inline=True)
comment(0x990B, "Y = message offset within the string table (&9AA6 "
        "base)", inline=True)
comment(0x990E, "X=0: error-text buffer index", inline=True)
comment(0x9910, "Zero the &0100 length byte (length will be filled in "
        "later)", inline=True)
comment(0x9913, "Read first message byte (the error code)", inline=True)
comment(0x9916, "Conditionally save it as last-error", inline=True)
comment(0x9919, "Read next message byte", inline=True)
comment(0x991C, "Append to error-text buffer at &0101+X", inline=True)
comment(0x991F, "Null terminator: message done", inline=True)
comment(0x9921, "Step buffer index", inline=True)
comment(0x9922, "Step source offset", inline=True)
comment(0x9923, "Loop while Y != 0 (Y wraps at 256, not expected)",
        inline=True)
comment(0x9925, "Append ' on drive <num>' or similar context",
        inline=True)
comment(0x9928, "A=0: null terminator", inline=True)
comment(0x992A, "Store at end of message", inline=True)
comment(0x992D, "Tail-jump to dispatch the BRK error", inline=True)

# fixup_reply_status_a inline comments (5 items)
comment(0x9930, "Read FS reply status byte at (net_tx_ptr,X)",
        inline=True)
comment(0x9932, "Status 'A'? (Acknowledge with no error)", inline=True)
comment(0x9934, "Not 'A': pass through unchanged", inline=True)
comment(0x9936, "Substitute 'B' for 'A' (handle ACK as a soft error)",
        inline=True)
comment(0x9938, "Clear V to take the standard mask path", inline=True)
comment(0x9939, "Always taken: use the standard masked-error path",
        inline=True)

# classify_reply_error inline comments (~15 items)
comment(0x993B, "Read FS reply status byte", inline=True)
comment(0x993D, "BIT $always_set_v_byte: force V=1 (extended-error "
        "path)", inline=True)
comment(0x9940, "Mask to 3 bits (error class 0..7)", inline=True)
comment(0x9942, "Save error class on stack", inline=True)
comment(0x9943, "Class 2 = 'station-related' family?", inline=True)
comment(0x9945, "No: build a simple one-line error", inline=True)
comment(0x9947, "Class 2 yes: save flags so we can branch on V later",
        inline=True)
comment(0x9948, "X = error class (=2)", inline=True)
comment(0x9949, "Y = lookup-table offset", inline=True)
comment(0x994C, "Read first message byte (error code)", inline=True)
comment(0x994F, "Conditionally save it", inline=True)
comment(0x9952, "X=0: text-buffer index", inline=True)
comment(0x9954, "Zero length byte", inline=True)
comment(0x9957, "Read message byte", inline=True)
comment(0x995A, "Append to buffer", inline=True)
comment(0x995D, "Null terminator -- station message done", inline=True)
comment(0x9963, "Append ' on drive <num>' suffix", inline=True)
comment(0x9966, "Restore the saved class flags", inline=True)
comment(0x9967, "V was set: use 'not listening' suffix", inline=True)
comment(0x9969, "A=&A4: 'station <n> not available' error code",
        inline=True)
comment(0x996B, "Save the alternative error code", inline=True)
comment(0x996E, "Patch error-text buffer length byte", inline=True)
comment(0x9971, "Y=&0B: lookup index for the listening-station suffix",
        inline=True)
comment(0x9973, "Always taken (Y is non-zero); jump to load_suffix_offset",
        inline=True)
comment(0x9975, "V was clear: 'not listening' suffix variant",
        inline=True)
comment(0x9977, "Read suffix offset from lookup", inline=True)
comment(0x997A, "Y = suffix offset", inline=True)
comment(0x997B, "Read suffix byte", inline=True)
comment(0x997E, "Append", inline=True)
comment(0x9981, "Null: suffix done", inline=True)
comment(0x9983, "Step Y", inline=True)
comment(0x9984, "Step X", inline=True)
comment(0x9985, "Loop while X != 0 (max 255 chars)", inline=True)
comment(0x9987, "Always taken (Z still set from BEQ): final terminator "
        "check", inline=True)

# build_simple_error inline comments
comment(0x9989, "X = error class", inline=True)
comment(0x998A, "Y = lookup-table offset", inline=True)
comment(0x998D, "X=0: buffer index", inline=True)
comment(0x998F, "Zero length", inline=True)
comment(0x9992, "Read first message byte (error code)", inline=True)
comment(0x9995, "Conditionally save it", inline=True)
comment(0x9998, "Read next message byte", inline=True)
comment(0x999B, "Append to buffer", inline=True)
comment(0x999E, "Null terminator -> dispatch", inline=True)
comment(0x99A0, "Step Y", inline=True)
comment(0x99A1, "Step X", inline=True)
comment(0x99A2, "Loop while X != 0", inline=True)

# send_disconnect_reply inline comments (~50 items in body)
comment(0xAFA6, "X = caller's TX-ptr low byte", inline=True)
comment(0xAFA8, "Y = caller's TX-ptr high byte", inline=True)
comment(0xAFAA, "Save A (the disconnect status to send)", inline=True)
comment(0xAFAB, "Test if A=0 (broadcast disconnect)", inline=True)
comment(0xAFAD, "Yes: skip the per-station scan", inline=True)
comment(0xAFAF, "X=&FF: scan counter -- INX in loop bumps to 0",
        inline=True)
comment(0xAFB1, "Y=A: status code (also used as station-table key)",
        inline=True)
comment(0xAFB2, "Restore status into A for the compare", inline=True)
comment(0xAFB3, "Step station-table index", inline=True)
comment(0xAFB4, "Compare with table[X] at &C230 (per-station status)",
        inline=True)
comment(0xAFB7, "Match: verify station address still matches", inline=True)
comment(0xAFB9, "Reached end of 16-slot table?", inline=True)
comment(0xAFBB, "No: keep scanning", inline=True)
comment(0xAFBD, "All slots tested, no match: A=0", inline=True)
comment(0xAFBF, "Always taken: jump to send-status", inline=True)
# verify_stn_match
comment(0xAFC1, "Y = matching index", inline=True)
comment(0xAFC2, "Verify station/network at this slot still matches "
        "caller", inline=True)
comment(0xAFC5, "Mismatch: station moved, keep scanning", inline=True)
comment(0xAFC7, "Read connection-active flag at &C260+X", inline=True)
comment(0xAFCA, "Mask to bit 0 (active flag)", inline=True)
# Send the status
comment(0xAFCC, "Y=0: TX[0] = control byte", inline=True)
comment(0xAFCE, "OR active-flag bit into the status", inline=True)
comment(0xAFD0, "Save the combined status", inline=True)
comment(0xAFD1, "Write it to TX[0]", inline=True)
comment(0xAFD3, "Send the disconnect packet via four-way handshake",
        inline=True)
comment(0xAFD6, "A=&FF: sentinel", inline=True)
comment(0xAFD8, "Y=8: TX[8] / TX[9] = packet trailer markers", inline=True)
comment(0xAFDA, "Write &FF at TX[8]", inline=True)
comment(0xAFDC, "Step Y", inline=True)
comment(0xAFDD, "Write &FF at TX[9]", inline=True)
comment(0xAFDF, "Pull the saved status", inline=True)
comment(0xAFE0, "Move into X for the test", inline=True)
comment(0xAFE1, "Y=&D1: control byte for ack-mode TXCB[1]", inline=True)
comment(0xAFE3, "Pull caller's original A again (was double-saved)",
        inline=True)
comment(0xAFE4, "Push it back", inline=True)
comment(0xAFE5, "A=0: skip the override", inline=True)
comment(0xAFE7, "Non-zero: use Y=&90 (FS reply port instead)",
        inline=True)
# store_tx_ctrl_byte
comment(0xAFE9, "Move chosen control/port into A", inline=True)
comment(0xAFEA, "Y=1: TX[1] is the port byte", inline=True)
comment(0xAFEC, "Write to TX[1]", inline=True)
comment(0xAFEE, "Move saved status into A", inline=True)
comment(0xAFEF, "Y=0: TX[0] for ack poll", inline=True)
comment(0xAFF0, "Push the status (we'll EOR with reply below)",
        inline=True)
# Wait for ACK with bit-flip detection
comment(0xAFF1, "A=&7F: marker pattern", inline=True)
comment(0xAFF3, "Write to TX[0]", inline=True)
comment(0xAFF5, "Wait for the TX/RX flip", inline=True)
comment(0xAFF8, "Pull saved status (peek without consuming)",
        inline=True)
comment(0xAFF9, "Push it back", inline=True)
comment(0xAFFA, "EOR with TX[0]: zero iff reply matches saved",
        inline=True)
comment(0xAFFC, "Rotate result; C set if bit 0 differs",
        inline=True)
comment(0xAFFD, "C set: keep waiting", inline=True)
comment(0xAFFF, "Discard saved status", inline=True)
comment(0xB000, "Discard caller's saved A", inline=True)
comment(0xB001, "Return", inline=True)

# net_1_read_handle / net_2_read_handle_entry inline comments
comment(0xA3FF, "Y=&6F: net_rx_ptr offset for the 'inline' handle byte",
        inline=True)
comment(0xA401, "Read handle byte directly from RX buffer", inline=True)
comment(0xA403, "C clear: read-handle path -- store directly to PB",
        inline=True)
# net_2_read_handle_entry
comment(0xA405, "Convert PB pointer to workspace table offset",
        inline=True)
comment(0xA408, "Out of range: return zero (uninitialised)", inline=True)
comment(0xA40A, "Read workspace handle byte", inline=True)
comment(0xA40C, "Slot marked '?' (uninitialised)?", inline=True)
comment(0xA40E, "Has a real handle: keep it and store", inline=True)
comment(0xA410, "Force result to zero (uninitialised marker)",
        inline=True)
comment(0xA412, "Write into PB[0] (handle return slot)", inline=True)
comment(0xA414, "Return", inline=True)

# net_3_close_handle inline comments
comment(0xA415, "Convert PB pointer to workspace table offset",
        inline=True)
comment(0xA418, "Out of range: mark as uninitialised", inline=True)
comment(0xA41A, "Shift bit 0 of fs_flags into C (save state)",
        inline=True)
comment(0xA41D, "Read PB[0] (the handle to close)", inline=True)
comment(0xA41F, "ROL: shift bit 7 of A into C", inline=True)
comment(0xA420, "Restore C into bit 0 of fs_flags", inline=True)
comment(0xA423, "Return; the close action is dispatched elsewhere "
        "based on the saved C state", inline=True)

# mark_ws_uninit inline comments
comment(0xA424, "Save bit 0 of econet_flags via ROR", inline=True)
comment(0xA427, "A='?': uninitialised marker", inline=True)
comment(0xA429, "Write '?' to workspace[Y] (the slot is now free)",
        inline=True)
comment(0xA42B, "Restore bit 0 of econet_flags", inline=True)
comment(0xA42E, "Return", inline=True)

# recv_and_process_reply inline comments (~70 items)
# Setup
comment(0x97CD, "Save flags so caller's V/C survive the receive",
        inline=True)
comment(0x97CE, "Set up open RX on port &90 for the FS reply (TXCB[0] "
        "= &90, ctrl = &7F)", inline=True)
comment(0x97D1, "Wait for the reply via the 3-level stack timer",
        inline=True)
comment(0x97D4, "Restore caller's flags", inline=True)
# Reply byte iteration
comment(0x97D5, "Step Y to next reply byte", inline=True)
comment(0x97D6, "Read reply byte at txcb_start+Y", inline=True)
comment(0x97D8, "Stash for the dispatch tests below", inline=True)
comment(0x97D9, "Zero terminates: return", inline=True)
comment(0x97DB, "V clear (caller's V): use code as-is", inline=True)
comment(0x97DD, "V set: shift the code by +&2A (extended-error mapping)",
        inline=True)
comment(0x97DF, "Non-zero: dispatch as an error", inline=True)
comment(0x97E1, "Return", inline=True)
# handle_disconnect
comment(0x97E2, "Pull caller's pushed return state", inline=True)
comment(0x97E3, "X=&C0: 'remote disconnect' status", inline=True)
comment(0x97E5, "Step Y past the disconnect byte", inline=True)
comment(0x97E6, "Send disconnect notification to remote", inline=True)
comment(0x97E9, "C clear (success): continue scanning replies",
        inline=True)
# store_reply_status
comment(0x97EB, "Save the error code into &C009", inline=True)
comment(0x97EE, "Read FS state byte at &C007", inline=True)
comment(0x97F1, "Save flags so we can branch later", inline=True)
comment(0x97F2, "FS state non-zero: data-loss check needed", inline=True)
comment(0x97F4, "Reply was &BF (special: not a real error)?",
        inline=True)
comment(0x97F6, "No: build error block", inline=True)
# check_data_loss path
comment(0x97F8, "A=&40: 'channel-active' bitmask", inline=True)
comment(0x97FA, "Push it onto the OR-accumulator", inline=True)
comment(0x97FB, "Clear the FS-active bit (we're losing the connection)",
        inline=True)
comment(0x97FE, "X=&F0: scan from channel offset &F0 upwards",
        inline=True)
# loop_scan_channels
comment(0x9800, "Pull current OR accumulator", inline=True)
comment(0x9801, "OR with channel status byte at &C1C8+X", inline=True)
comment(0x9804, "Push back updated accumulator", inline=True)
comment(0x9805, "Reload channel byte", inline=True)
comment(0x9808, "Mask to top 2 bits (preserve TX/RX state)",
        inline=True)
comment(0x980A, "Write back trimmed status", inline=True)
comment(0x980D, "Step channel index", inline=True)
comment(0x980E, "Loop while X bit 7 set (covers &F0..&FF)", inline=True)
comment(0x9810, "Clear the FS state byte (no longer active)",
        inline=True)
comment(0x9813, "Force-close all client channels", inline=True)
comment(0x9816, "Pull final OR accumulator", inline=True)
comment(0x9817, "ROR: bit 0 (was bit 6 of any &40 byte) -> C",
        inline=True)
comment(0x9818, "Any channel was active: skip the warning", inline=True)
comment(0x981A, "No active channels were lost: print 'Data Lost' "
        "warning via inline string", inline=True)
# After warning / data-loss return
comment(0x9827, "Reload error code from &C009", inline=True)
comment(0x982A, "Restore saved flags (was bit 7 of fs_flags)",
        inline=True)
comment(0x982B, "Z set (no error): build the error block anyway",
        inline=True)
comment(0x982D, "Pull caller's saved return state (3 bytes from PHP "
        "earlier)", inline=True)
comment(0x982E, "(2nd PLA)", inline=True)
comment(0x982F, "(3rd PLA)", inline=True)
comment(0x9830, "Return -- caller dispatched on a non-error reply",
        inline=True)
# build_error_block
comment(0x9831, "Y=1: skip past the leading TXCB control byte",
        inline=True)
comment(0x9833, "Error code below &A8 (extended)?", inline=True)
comment(0x9835, "No (>= &A8): proceed to copy", inline=True)
comment(0x9837, "Yes: clamp to &A8 (truncate range)", inline=True)
comment(0x9839, "Write clamped code back into TXCB", inline=True)
comment(0x983B, "Y=&FF: INY in loop bumps to 0", inline=True)
comment(0x983D, "Step Y", inline=True)
comment(0x983E, "Read TXCB byte (error block content)", inline=True)
comment(0x9840, "Copy to BRK error block at &0100+Y", inline=True)
comment(0x9843, "EOR with CR; Z set when we just copied the terminator",
        inline=True)
comment(0x9845, "Not yet at CR: continue copying", inline=True)
comment(0x9847, "Write the CR terminator (Z still set so A=0; ensures "
        "cleanly terminated)", inline=True)
comment(0x984A, "Step Y back so it points at the CR position",
        inline=True)
comment(0x984B, "Move Y into A for the BRK", inline=True)
comment(0x984C, "Move Y into X (caller convention)", inline=True)
comment(0x984D, "Tail-jump into the BRK-dispatch error path",
        inline=True)
comment(0x8A8F, "Service 1 (workspace claim)?", inline=True)
comment(0x8A91, "No: skip ADLC check", inline=True)
comment(0x8A93, "Read ADLC status register 1", inline=True)
comment(0x8A96, "Mask relevant status bits", inline=True)
comment(0x8A98, "Non-zero: ADLC absent, set flag", inline=True)
# UNMAPPED: comment(0x8A4C, "Read ADLC status register 2", inline=True)
# UNMAPPED: comment(0x8A4F, "Mask relevant status bits", inline=True)
# UNMAPPED: comment(0x8A51, "Zero: ADLC present, skip", inline=True)
comment(0x8A9A, "Shift bit 7 into carry", inline=True)
comment(0x8A9D, "Set carry to mark ADLC absent", inline=True)
comment(0x8A9E, "Rotate carry into bit 7 of slot flag", inline=True)
comment(0x8AA1, "Load ROM slot flag byte", inline=True)
comment(0x8AA4, "Shift bit 7 (ADLC absent) into carry", inline=True)
comment(0x8AA5, "Restore service call number", inline=True)
comment(0x8AA6, "ADLC present: continue dispatch", inline=True)
comment(0x8AA8, "ADLC absent: decline service, return", inline=True)
# UNMAPPED: comment(0x8A62, "Service 15 (vectors claimed)?", inline=True)
# UNMAPPED: comment(0x8A64, "No: handle other services", inline=True)
# UNMAPPED: comment(0x8A66, "Already initialised?", inline=True)
# UNMAPPED: comment(0x8A69, "Yes: skip first-time init", inline=True)
# UNMAPPED: comment(0x8A6B, "X=1 (mark as initialised)", inline=True)
# UNMAPPED: comment(0x8A6C, "Set ROM present flag", inline=True)
# UNMAPPED: comment(0x8A6F, "A=service call number; use as ROM counter", inline=True)
# UNMAPPED: comment(0x8A71, "Point to ROM header copyright offset", inline=True)
# UNMAPPED: comment(0x8A73, "Set high byte of OSRDSC pointer", inline=True)
# UNMAPPED: comment(0x8A75, "Offset &0C: copyright string offset", inline=True)
# UNMAPPED: comment(0x8A77, "Set low byte of OSRDSC pointer", inline=True)
# UNMAPPED: comment(0x8A79, "Read next ROM title char", inline=True)
# UNMAPPED: comment(0x8A7C, "First char 'N'?", inline=True)
# UNMAPPED: comment(0x8A7E, "No: not a NET ROM, try next", inline=True)
# UNMAPPED: comment(0x8A80, "Read next ROM title char", inline=True)
# UNMAPPED: comment(0x8A83, "Second char 'E'?", inline=True)
# UNMAPPED: comment(0x8A85, "No: not a NET ROM, try next", inline=True)
# UNMAPPED: comment(0x8A87, "Read next ROM title char", inline=True)
# UNMAPPED: comment(0x8A8A, "Third char 'T'?", inline=True)
# UNMAPPED: comment(0x8A8C, "No: not a NET ROM, try next", inline=True)
# UNMAPPED: comment(0x8A8E, "X=ROM slot for indexed store", inline=True)
# UNMAPPED: comment(0x8A90, "Load its slot flag byte", inline=True)
# UNMAPPED: comment(0x8A93, "Set bit 7 to mark as NET ROM", inline=True)
# UNMAPPED: comment(0x8A95, "Store updated flag", inline=True)
# UNMAPPED: comment(0x8A98, "Previous ROM slot", inline=True)
# UNMAPPED: comment(0x8A9A, "More ROMs to check: loop", inline=True)
# UNMAPPED: comment(0x8A9C, "A=&0F: restore service call number", inline=True)
# UNMAPPED: comment(0x8AA0, "Advance read pointer to next byte", inline=True)
comment(0x8AA9, "Transfer service number to X", inline=True)
comment(0x8AAA, "Save current service state", inline=True)
comment(0x8AAC, "Push old state", inline=True)
comment(0x8AAD, "Restore service number to A", inline=True)
comment(0x8AAE, "Store as current service state", inline=True)
comment(0x8AB0, "Service < 13?", inline=True)
comment(0x8AB2, "Yes: use as dispatch index directly", inline=True)
comment(0x8AB4, "Subtract 5 (map 13-17 to 8-12)", inline=True)
comment(0x8AB6, "Mapped value = 13? (original was 18)", inline=True)
comment(0x8AB8, "Yes: valid service 18 (FS select)", inline=True)
comment(0x8ACE, "Unknown service: set index to 0", inline=True)
comment(0x8AD0, "Transfer dispatch index to X", inline=True)
comment(0x8AD1, "Index 0: unhandled service, skip", inline=True)
comment(0x8AD3, "Save current workspace page", inline=True)
comment(0x8AD5, "Push old page", inline=True)
comment(0x8AD6, "Set workspace page from Y parameter", inline=True)
comment(0x8AD8, "Transfer Y to A", inline=True)
comment(0x8AD9, "Y=0 for dispatch offset", inline=True)
comment(0x8ADB, "Dispatch to service handler via table", inline=True)
comment(0x8ADE, "Restore old workspace page", inline=True)
comment(0x8ADF, "Store it back", inline=True)
comment(0x8AE1, "Get service state (return code)", inline=True)
comment(0x8AE3, "Restore old service state", inline=True)
comment(0x8AE4, "Store it back", inline=True)
comment(0x8AE6, "Transfer return code to A", inline=True)
comment(0x8AE7, "Restore ROM slot to X", inline=True)
comment(0x8AE9, "Return to MOS", inline=True)
comment(0x8AEA, "Offset 0 in receive block", inline=True)
comment(0x8AEC, "Load remote operation flag", inline=True)
comment(0x8AEE, "Zero: already off, skip to cleanup", inline=True)
comment(0x8AF0, "A=0", inline=True)
comment(0x8AF3, "Clear remote operation flag", inline=True)
comment(0x8AF6, "OSBYTE &C9: keyboard disable", inline=True)
comment(0x8AFB, "A=&0A: workspace init parameter", inline=True)
comment(0x8AFD, "Initialise workspace area", inline=True)
comment(0x8B00, "Save X in workspace", inline=True)
comment(0x8B02, "A=&CE: start of key range", inline=True)
comment(0x8B04, "Restore X from workspace", inline=True)
comment(0x8B06, "Y=&7F: OSBYTE scan parameter", inline=True)
comment(0x8B08, "OSBYTE: scan keyboard", inline=True)
comment(0x8B0B, "Advance to next key code", inline=True)
comment(0x8B0D, "Reached &D0?", inline=True)
comment(0x8B0F, "No: loop back (scan &CE and &CF)", inline=True)
comment(0x8B11, "A=0", inline=True)
comment(0x8B13, "Clear service state", inline=True)
comment(0x8B15, "Clear workspace byte", inline=True)
comment(0x8B17, "Return", inline=True)
comment(0x8B18, "Save A", inline=True)
comment(0x8B19, "Copy OS text pointer low", inline=True)
comment(0x8B1B, "to fs_crc_lo", inline=True)
comment(0x8B1D, "Copy OS text pointer high", inline=True)
comment(0x8B1F, "to fs_crc_hi", inline=True)
comment(0x8B21, "Restore A", inline=True)
comment(0x8B22, "Return", inline=True)
# UNMAPPED: comment(0x8B0D, "Y=5 (Econet filing system)?", inline=True)
# UNMAPPED: comment(0x8B0F, "No: not ours, return unclaimed", inline=True)
# UNMAPPED: comment(0x8B11, "A=0: clear service state", inline=True)
# UNMAPPED: comment(0x8B15, "Already selected?", inline=True)
# UNMAPPED: comment(0x8B13, "Reset service processing state", inline=True)
# UNMAPPED: comment(0x8B18, "Yes (bit 7 set): return unclaimed", inline=True)
comment(0x8B23, "Get workspace page for this ROM slot", inline=True)
comment(0x8B26, "Store as high byte of load address", inline=True)
comment(0x8B28, "A=0", inline=True)
comment(0x8B2A, "Clear low byte of load address", inline=True)
comment(0x8B2C, "Clear carry for addition", inline=True)
comment(0x8B2D, "Y=&76: checksum range end", inline=True)
comment(0x8B2F, "Add byte to running checksum", inline=True)
comment(0x8B31, "Decrement index", inline=True)
comment(0x8B32, "Loop until all bytes summed", inline=True)
comment(0x8B34, "Y=&77: checksum storage offset", inline=True)
comment(0x8B36, "Compare with stored checksum", inline=True)
comment(0x8B55, "Match: checksum valid", inline=True)
comment(0x8B57, "Mismatch: raise checksum error", inline=True)
comment(0x8B60, "Call FSCV with A=6 (new FS)", inline=True)
comment(0x8B63, "Y=9: end of FS context block", inline=True)
comment(0x8B65, "Load byte from receive block", inline=True)
comment(0x8B67, "Store into FS workspace", inline=True)
comment(0x8B6A, "Decrement index", inline=True)
comment(0x8B6B, "Reached offset 1?", inline=True)
comment(0x8B6D, "No: continue copying", inline=True)
comment(0x8B6F, "Shift bit 7 of FS flags into carry", inline=True)
comment(0x8B72, "Clear carry", inline=True)
comment(0x8B73, "Clear bit 7 of FS flags", inline=True)
comment(0x8B76, "Y=&0D: vector table size - 1", inline=True)
comment(0x8B78, "Load FS vector address", inline=True)
comment(0x8B7B, "Store into FILEV vector table", inline=True)
comment(0x8B7E, "Decrement index", inline=True)
comment(0x8B7F, "Loop until all vectors installed", inline=True)
comment(0x8B81, "Initialise ADLC and NMI workspace", inline=True)
comment(0x8B84, "Y=&1B: extended vector offset", inline=True)
comment(0x8B86, "X=7: two more vectors to set up", inline=True)
comment(0x8B88, "Set up extended vectors", inline=True)
comment(0x8B8B, "A=0", inline=True)
comment(0x8B8D, "Clear FS state byte", inline=True)
comment(0x8B90, "Clear workspace byte", inline=True)
comment(0x8B93, "Clear workspace byte", inline=True)
# UNMAPPED: comment(0x8B6A, "Clear service state", inline=True)
comment(0x8B96, "Clear receive attribute byte", inline=True)
comment(0x8B99, "Clear workspace byte", inline=True)
comment(0x8B9C, "Set up workspace pointers", inline=True)
comment(0x8B9F, "Initialise FS state", inline=True)
comment(0x8BA2, "Y=&77: workspace block size - 1", inline=True)
comment(0x8BA4, "Load byte from source workspace", inline=True)
comment(0x8BA6, "Store to page &10 shadow copy", inline=True)
comment(0x8BA9, "Decrement index", inline=True)
comment(0x8BAA, "Loop until all bytes copied", inline=True)
comment(0x8BAC, "A=&80: FS selected flag", inline=True)
# UNMAPPED: comment(0x8B84, "Set bit 7 of FS flags", inline=True)
# UNMAPPED: comment(0x8B87, "Store updated flags", inline=True)
# UNMAPPED: comment(0x8B8A, "Issue service 15 (FS initialised)", inline=True)
comment(0x8BBB, "X=&4A: NFS command table offset", inline=True)
comment(0x8BBD, "Print help for NFS commands", inline=True)
comment(0x8BC0, "X=0: utility command table offset", inline=True)
comment(0x8BC4, "X=&4A: NFS command table offset", inline=True)
comment(0x8BC6, "V clear: need to print header first", inline=True)
# UNMAPPED: comment(0x8B9A, "Save X (table offset)", inline=True)
# UNMAPPED: comment(0x8B9B, "Push it", inline=True)
# UNMAPPED: comment(0x8B9C, "Save Y", inline=True)
# UNMAPPED: comment(0x8B9D, "Push it", inline=True)
comment(0x8BCA, "Print version string header", inline=True)
# UNMAPPED: comment(0x8BA1, "Restore Y", inline=True)
# UNMAPPED: comment(0x8BA2, "Transfer to Y", inline=True)
# UNMAPPED: comment(0x8BA3, "Restore X", inline=True)
# UNMAPPED: comment(0x8BA4, "Transfer to X", inline=True)
comment(0x8BCF, "Clear overflow flag", inline=True)
comment(0x8BD5, "Save Y (command line offset)", inline=True)
comment(0x8BD6, "Push it", inline=True)
comment(0x8BD7, "Save processor status", inline=True)
comment(0x8BD8, "Load byte from command table", inline=True)
comment(0x8BDB, "Bit 7 clear: valid entry, continue", inline=True)
comment(0x8BDD, "End of table: finish up", inline=True)
comment(0x8BE0, "Print two-space indent", inline=True)
# UNMAPPED: comment(0x8BBB, "Y=9: max command name length", inline=True)
# UNMAPPED: comment(0x8BBD, "Load first byte of command name", inline=True)
comment(0x8BED, "Advance table pointer", inline=True)
comment(0x8BEE, "Decrement padding counter", inline=True)
comment(0x8BEF, "Load next character", inline=True)
comment(0x8BF2, "Bit 7 clear: more chars, continue", inline=True)
comment(0x8BF4, "Pad with spaces", inline=True)
comment(0x8BF9, "Decrement remaining pad count", inline=True)
comment(0x8BFA, "More padding needed: loop", inline=True)
comment(0x8BFC, "Load syntax descriptor byte", inline=True)
comment(0x8BFF, "Mask to get syntax string index", inline=True)
# UNMAPPED: comment(0x8BD7, "Index &0E: shared commands?", inline=True)
# UNMAPPED: comment(0x8BD9, "Yes: handle shared commands list", inline=True)
comment(0x8C01, "Use index as Y", inline=True)
comment(0x8C02, "Look up syntax string offset", inline=True)
comment(0x8C05, "Transfer offset to Y", inline=True)
comment(0x8C06, "Advance to next character", inline=True)
comment(0x8C07, "Load syntax string character", inline=True)
comment(0x8C0A, "Zero terminator: end of syntax", inline=True)
comment(0x8C0C, "Carriage return: line continuation", inline=True)
comment(0x8C0E, "No: print the character", inline=True)
comment(0x8C10, "Handle line wrap in syntax output", inline=True)
comment(0x8C13, "Continue with next character", inline=True)
comment(0x8C19, "Continue with next character", inline=True)
# UNMAPPED: comment(0x8BF6, "Save table pointer", inline=True)
# UNMAPPED: comment(0x8BF7, "Push it", inline=True)
# UNMAPPED: comment(0x8BF8, "Print opening parenthesis", inline=True)
# UNMAPPED: comment(0x8BFC, "Y=0: shared command counter", inline=True)
# UNMAPPED: comment(0x8BFE, "X=&D3: shared command table start", inline=True)
# UNMAPPED: comment(0x8C00, "Load byte from shared command table", inline=True)
# UNMAPPED: comment(0x8C03, "Bit 7 set: end of shared commands", inline=True)
# UNMAPPED: comment(0x8C05, "Back up one position", inline=True)
# UNMAPPED: comment(0x8C06, "Advance to next character", inline=True)
# UNMAPPED: comment(0x8C07, "Load command name character", inline=True)
# UNMAPPED: comment(0x8C0A, "Bit 7 set: end of this name", inline=True)
# UNMAPPED: comment(0x8C0F, "Print more characters of name", inline=True)
# UNMAPPED: comment(0x8C12, "Strip bit 7 from final character", inline=True)
# UNMAPPED: comment(0x8C17, "Count this shared command", inline=True)
# UNMAPPED: comment(0x8C18, "Printed 4 commands?", inline=True)
# UNMAPPED: comment(0x8C1A, "No: continue on same line", inline=True)
# UNMAPPED: comment(0x8C1C, "Handle line wrap after 4 commands", inline=True)
# UNMAPPED: comment(0x8C1F, "X += 3: skip syntax descriptor and address", inline=True)
# UNMAPPED: comment(0x8C20, "(continued)", inline=True)
# UNMAPPED: comment(0x8C21, "(continued)", inline=True)
# UNMAPPED: comment(0x8C22, "Loop for more shared commands", inline=True)
# UNMAPPED: comment(0x8C24, "Restore original table pointer", inline=True)
# UNMAPPED: comment(0x8C25, "Transfer to X", inline=True)
comment(0x8C1F, "X += 3: skip syntax descriptor and address", inline=True)
comment(0x8C20, "(continued)", inline=True)
comment(0x8C21, "(continued)", inline=True)
comment(0x8C22, "Loop for next command", inline=True)
comment(0x8C25, "Restore processor status", inline=True)
comment(0x8C26, "Restore Y", inline=True)
comment(0x8C27, "Transfer to Y", inline=True)
comment(0x8C28, "Return", inline=True)
comment(0x8C29, "Read output stream type", inline=True)
comment(0x8C2C, "Stream 0 (VDU): no wrapping", inline=True)
comment(0x8C2E, "Stream 3 (printer)?", inline=True)
comment(0x8C30, "Yes: no wrapping", inline=True)
# UNMAPPED: comment(0x8C3C, "Save Y", inline=True)
# UNMAPPED: comment(0x8C3D, "Push it", inline=True)
comment(0x8C36, "Y=&0B: indent width - 1", inline=True)
comment(0x8C38, "Space character", inline=True)
comment(0x8C3D, "Decrement indent counter", inline=True)
comment(0x8C3E, "More spaces needed: loop", inline=True)
# UNMAPPED: comment(0x8C4B, "Restore Y", inline=True)
# UNMAPPED: comment(0x8C4C, "Transfer to Y", inline=True)
comment(0x8C41, "Return", inline=True)
comment(0x8C42, "X=0: start of utility command table", inline=True)
comment(0x8C44, "Get command line offset", inline=True)
comment(0x8C46, "Save text pointer to fs_crc", inline=True)
comment(0x8C49, "Try to match command in table", inline=True)
comment(0x8C4C, "No match: return to caller", inline=True)
comment(0x8C4E, "Match found: execute command", inline=True)
comment(0x8C51, "Check for credits Easter egg", inline=True)
comment(0x8C54, "Get command line offset", inline=True)
comment(0x8C56, "Load character at offset", inline=True)
comment(0x8C58, "Is it CR (bare *HELP)?", inline=True)
comment(0x8C5A, "No: check for specific topic", inline=True)
comment(0x8C5C, "Print version string", inline=True)
comment(0x8C5F, "X=&C4: start of help command list", inline=True)
comment(0x8C61, "Print command list from table", inline=True)
comment(0x8C64, "Restore Y (command line offset)", inline=True)
comment(0x8C66, "Return unclaimed", inline=True)
comment(0x8C67, "Test for topic match (sets flags)", inline=True)
comment(0x8C6A, "Is first char '.' (abbreviation)?", inline=True)
comment(0x8C6C, "No: try topic-specific help", inline=True)
comment(0x8C6E, "'.' found: show full command list", inline=True)
comment(0x8C71, "Save text pointer to fs_crc", inline=True)
comment(0x8C74, "Save flags", inline=True)
comment(0x8C75, "X=&C4: help command table start", inline=True)
comment(0x8C77, "Try to match help topic in table", inline=True)
comment(0x8C7A, "No match: try next topic", inline=True)
comment(0x8C7C, "Restore flags", inline=True)
comment(0x8C7D, "Push return address high (&8C)", inline=True)
comment(0x8C7F, "Push it for RTS dispatch", inline=True)
comment(0x8C80, "Push return address low (&74)", inline=True)
comment(0x8C82, "Push it for RTS dispatch", inline=True)
comment(0x8C83, "Load dispatch address high", inline=True)
comment(0x8C86, "Push dispatch high for RTS", inline=True)
comment(0x8C87, "Load dispatch address low", inline=True)
comment(0x8C8A, "Push dispatch low for RTS", inline=True)
comment(0x8C8B, "Dispatch via RTS (returns to &8C80)", inline=True)
comment(0x8C8C, "Restore flags from before match", inline=True)
comment(0x8C8D, "End of command line?", inline=True)
comment(0x8C8F, "No: try matching next topic", inline=True)
comment(0x8C93, "Print version string via inline", inline=True)
# UNMAPPED: comment(0x8CB5, "NOP (string terminator)", inline=True)
# UNMAPPED: comment(0x8CB6, "Print station number after version", inline=True)
# UNMAPPED: comment(0x8CB9, "Get current ROM slot number", inline=True)
comment(0x8CAF, "Load workspace page for this slot", inline=True)
comment(0x8CBB, "Transfer to Y", inline=True)
comment(0x8CBC, "Return with page in A and Y", inline=True)
comment(0x8CBD, "Get workspace page for ROM slot", inline=True)
comment(0x8CC0, "Store page in nfs_temp", inline=True)
comment(0x8CC2, "A=0", inline=True)
comment(0x8CC4, "Clear low byte of pointer", inline=True)
comment(0x8CC6, "Return", inline=True)
comment(0x8CC7, "OSBYTE &7A: scan keyboard from key 16", inline=True)
comment(0x8CCD, "No key pressed: select Net FS", inline=True)
comment(0x8CCF, "Key &19 (N)?", inline=True)
comment(0x8CD1, "Yes: write key state and boot", inline=True)
comment(0x8CD3, "EOR with &55: maps to zero if 'N'", inline=True)
comment(0x8CD5, "Not N key: return unclaimed", inline=True)
comment(0x8CD8, "OSBYTE &78: write keys pressed", inline=True)
comment(0x8CDD, "Select NFS as current filing system", inline=True)
comment(0x8CE4, "Print station number", inline=True)
comment(0x8CEA, "Get workspace page", inline=True)
comment(0x8CEC, "Non-zero: already initialised, return", inline=True)
comment(0x8CEE, "Load boot flags", inline=True)
comment(0x8CF1, "Set bit 2 (auto-boot in progress)", inline=True)
comment(0x8CF3, "Store updated boot flags", inline=True)
comment(0x8CF6, "X=&0F: boot filename address low", inline=True)
comment(0x8CF8, "Y=&8D: boot filename address high", inline=True)
comment(0x8CFA, "Execute boot file", inline=True)
comment(0x8CFD, "A=6: notify new filing system", inline=True)
# UNMAPPED: comment(0x8CFE, "Call FSCV", inline=True)
# UNMAPPED: comment(0x8D01, "X=&0A: service 10 parameter", inline=True)
comment(0x8CFF, "Dispatch via FSCV", inline=True)
comment(0x8D02, "X=&0F: service 15 parameter", inline=True)
comment(0x8D04, "OSBYTE &8F: issue service request", inline=True)
# UNMAPPED: comment(0x8D17, "Get command line offset", inline=True)
comment(0x8D26, "X=5: start of credits keyword", inline=True)
comment(0x8D28, "Load character from command line", inline=True)
comment(0x8D2A, "Compare with credits keyword", inline=True)
comment(0x8D2D, "Mismatch: check if keyword complete", inline=True)
comment(0x8D2F, "Advance command line pointer", inline=True)
comment(0x8D30, "Advance keyword pointer", inline=True)
comment(0x8D31, "Continue matching", inline=True)
comment(0x8D33, "Reached end of keyword (X=&0D)?", inline=True)
comment(0x8D35, "No: keyword not fully matched, return", inline=True)
comment(0x8D37, "X=0: start of credits text", inline=True)
comment(0x8D39, "Load character from credits string", inline=True)
comment(0x8D3C, "Zero terminator: done printing", inline=True)
comment(0x8D41, "Advance string pointer", inline=True)
comment(0x8D42, "Continue printing", inline=True)
comment(0x8D44, "Return", inline=True)
# UNMAPPED: comment(0x8D79, "Save Y (command line offset)", inline=True)
comment(0x8D8E, "Push it", inline=True)
comment(0x8D91, "OSBYTE &77: close SPOOL/EXEC", inline=True)
comment(0x8D93, "Store as pending operation marker", inline=True)
comment(0x8D99, "Y=0", inline=True)
comment(0x8D9B, "Clear password entry flag", inline=True)
comment(0x8D9D, "Reset FS connection state", inline=True)
# UNMAPPED: comment(0x8D8A, "A=0", inline=True)
# UNMAPPED: comment(0x8D8C, "Clear pending operation marker", inline=True)
comment(0x8DA5, "Restore command line offset", inline=True)
# UNMAPPED: comment(0x8D90, "Transfer to Y", inline=True)
comment(0x8DAA, "Load first option byte", inline=True)
comment(0x8DAC, "Parse station number if present", inline=True)
comment(0x8DAF, "Not a digit: skip to password entry", inline=True)
comment(0x8DB1, "Parse user ID string", inline=True)
comment(0x8DB4, "No user ID: go to password", inline=True)
comment(0x8DC0, "No FS address: skip to password", inline=True)
comment(0x8DB6, "Store file server station low", inline=True)
comment(0x8DB9, "Check and store FS network", inline=True)
comment(0x8DBC, "Skip separator", inline=True)
comment(0x8DBD, "Parse next argument", inline=True)
comment(0x8DC2, "Store file server station high", inline=True)
comment(0x8DC5, "X=&FF: pre-decrement for loop", inline=True)
comment(0x8DC7, "Advance index", inline=True)
comment(0x8DC8, "Load logon command template byte", inline=True)
comment(0x8DCB, "Store into transmit buffer", inline=True)
comment(0x8DCE, "Bit 7 clear: more bytes, loop", inline=True)
comment(0x8DD0, "Send logon with file server lookup", inline=True)
comment(0x8DD3, "Success: skip to password entry", inline=True)
comment(0x8DD5, "Build FS command packet", inline=True)
comment(0x8DD8, "Y=&FF: pre-increment for loop", inline=True)
comment(0x8DDA, "Advance to next byte", inline=True)
comment(0x8DDB, "Load byte from reply buffer", inline=True)
comment(0x8DDE, "Is it CR (end of prompt)?", inline=True)
comment(0x8DE0, "Yes: no colon found, skip to send", inline=True)
comment(0x8DE2, "Is it ':' (password prompt)?", inline=True)
comment(0x8DE4, "No: keep scanning", inline=True)
comment(0x8DE9, "Save position of colon", inline=True)
comment(0x8DEB, "A=&FF: mark as escapable", inline=True)
comment(0x8DED, "Set escape flag", inline=True)
comment(0x8DEF, "Check for escape condition", inline=True)
comment(0x8DF7, "Not NAK (&15): check other chars", inline=True)
comment(0x8DF9, "Restore colon position", inline=True)
comment(0x8DFB, "Non-zero: restart from colon", inline=True)
comment(0x8DFD, "At colon position?", inline=True)
comment(0x8DFF, "Yes: restart password input", inline=True)
comment(0x8E01, "Backspace: move back one character", inline=True)
comment(0x8E02, "If not at start: restart input", inline=True)
comment(0x8E04, "Delete key (&7F)?", inline=True)
comment(0x8E06, "Yes: handle backspace", inline=True)
comment(0x8E08, "Store character in password buffer", inline=True)
comment(0x8E0B, "Advance buffer pointer", inline=True)
comment(0x8E0C, "Is it CR (end of password)?", inline=True)
comment(0x8E0E, "No: read another character", inline=True)
comment(0x8E13, "Transfer string length to A", inline=True)
comment(0x8E14, "Save string length", inline=True)
comment(0x8E15, "Set up transmit control block", inline=True)
comment(0x8E18, "Send to file server and get reply", inline=True)
# UNMAPPED: comment(0x8E02, "Restore string length", inline=True)
# UNMAPPED: comment(0x8E03, "Transfer to X (byte count)", inline=True)
comment(0x8E1C, "Include terminator", inline=True)
comment(0x8E1D, "Y=0", inline=True)
comment(0x8E21, "Parse station number from cmd line", inline=True)
comment(0x8E24, "Compare with expected station", inline=True)
comment(0x8E27, "Different: return without clearing", inline=True)
comment(0x8E29, "Same: clear station byte", inline=True)
comment(0x8E2C, "Return", inline=True)
comment(0x8E2D, "Y=0: first character offset", inline=True)
comment(0x8E38, "Build FS command packet", inline=True)
comment(0x8E2F, "Load first character of command text", inline=True)
comment(0x8E3B, "Transfer result to Y", inline=True)
comment(0x8E31, "Is it '&' (URD prefix)?", inline=True)
comment(0x8E3C, "Set up command and send to FS", inline=True)
comment(0x8E33, "No: send as normal FS command", inline=True)
comment(0x8E3F, "Load reply function code", inline=True)
comment(0x8E35, "Yes: route via *RUN for URD prefix handling", inline=True)
comment(0x8E42, "Zero: no reply, return", inline=True)
comment(0x8E44, "Load first reply byte", inline=True)
comment(0x8E47, "Y=&17: logon dispatch offset", inline=True)
comment(0x8E4B, "Parse reply as decimal number", inline=True)
comment(0x8E4E, "Result >= 8?", inline=True)
comment(0x8E50, "Yes: out of range, return", inline=True)
comment(0x8E52, "Transfer handle to X", inline=True)
comment(0x8E53, "Look up in open files table", inline=True)
comment(0x8E56, "Transfer result to A", inline=True)
comment(0x8E57, "Y=&13: handle dispatch offset", inline=True)
comment(0x8E5B, "Handle >= 5?", inline=True)
comment(0x8E5D, "Yes: out of range, return", inline=True)
comment(0x8E5F, "Y=&0E: directory dispatch offset", inline=True)
comment(0x8E61, "Advance X to target index", inline=True)
comment(0x8E63, "Y still positive: continue counting", inline=True)
comment(0x8E62, "Decrement Y offset counter", inline=True)
comment(0x8E65, "Y=&FF: will be ignored by caller", inline=True)
comment(0x8E66, "Load dispatch address high byte", inline=True)
comment(0x8E69, "Push high byte for RTS dispatch", inline=True)
comment(0x8E6A, "Load dispatch address low byte", inline=True)
comment(0x8E6D, "Push low byte for RTS dispatch", inline=True)
comment(0x8E6E, "Load FS options pointer", inline=True)
comment(0x8E70, "Dispatch via RTS", inline=True)

# Printer server template data (8 bytes). Read indirectly by
# copy_ps_data via LDA ps_template_base,X with X=&F8..&FF,
# reaching ps_template_base+&F8 = &8E59. Default PS name
# "PRINT " followed by status bytes &01, &00.
comment(0x8E9F, "Printer server template (8 bytes)\n"
    "\n"
    "Default printer server configuration data, read\n"
    "indirectly by copy_ps_data via LDA ps_template_base,X\n"
    "with X=&F8..&FF (reaching ps_template_base+&F8 =\n"
    "&8E59). Contains \"PRINT \" (6 bytes) as the default\n"
    "printer server name, followed by &01 and &00 as\n"
    "default status bytes. Absent from NFS versions;\n"
    "unique to ANFS.")
comment(0x8E9F, "PS template: default name \"PRINT \"", inline=True)

# UNMAPPED: comment(0x8E83, "X=0", inline=True)
comment(0x8ECB, "Y=&FF", inline=True)
comment(0x8ECD, "Execute OSBYTE and return", inline=True)

# NETV handler address pair at &8E8A. Read by write_vector_entry
# via LDA svc_dispatch_lo_offset,Y at Y=&36/&37. Interleaved
# with OSBYTE wrapper code at svc_dispatch_lo_offset + &30..&35.
# UNMAPPED: comment(0x8E8A, "NETV handler address\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "2-byte handler address for the NETV extended\n"
# UNMAPPED:     "vector, read by write_vector_entry at Y=&36\n"
# UNMAPPED:     "from svc_dispatch_lo_offset. Points to\n"
# UNMAPPED:     "netv_handler which dispatches OSWORDs\n"
# UNMAPPED:     "0-8 to Econet handlers. Interleaved with the\n"
# UNMAPPED:     "OSBYTE wrapper code in the data area.")

# UNMAPPED: comment(0x8E8C, "X=0", inline=True)
comment(0x8ED4, "Y=0", inline=True)
comment(0x8ED8, "Get original OSBYTE A parameter", inline=True)
comment(0x8EDA, "Subtract &31 (map &32-&35 to 1-4)", inline=True)
comment(0x8EDC, "In range 0-3?", inline=True)
comment(0x8EDE, "No: not ours, return unclaimed", inline=True)
comment(0x8EE0, "Transfer to X as dispatch index", inline=True)
# UNMAPPED: comment(0x8E9B, "A=0: claim the service call", inline=True)
# UNMAPPED: comment(0x8E9D, "Set return value to 0 (claimed)", inline=True)
comment(0x8EE3, "Transfer Y to A (OSBYTE Y param)", inline=True)
comment(0x8EE4, "Y=&21: OSBYTE dispatch offset", inline=True)
comment(0x8EE6, "Dispatch to OSBYTE handler via table", inline=True)
comment(0x8EE9, "Need at least &16 pages?", inline=True)
comment(0x8EEB, "Already enough: return", inline=True)
comment(0x8EED, "Request &16 pages of workspace", inline=True)
comment(0x8EEF, "Return", inline=True)
comment(0x8EF0, "Transfer Y to A", inline=True)
comment(0x8EF2, "Y >= &21?", inline=True)
comment(0x8EF4, "No: use Y as-is", inline=True)
comment(0x8EF6, "Cap at &21", inline=True)
comment(0x8EF8, "Offset &0B in receive block", inline=True)
comment(0x8EFA, "Store workspace page count", inline=True)
comment(0x8EFD, "Return", inline=True)
# UNMAPPED: comment(0x8EB8, "Store Y as receive block page", inline=True)
# UNMAPPED: comment(0x8EBA, "Advance to next page", inline=True)
# UNMAPPED: comment(0x8EBB, "Store as NFS workspace page", inline=True)
# UNMAPPED: comment(0x8EBD, "Advance to next page", inline=True)
comment(0x8EFE, "Transfer page to A", inline=True)
comment(0x8EFF, "Get current ROM slot number", inline=True)
comment(0x8F04, "Store workspace page for this slot", inline=True)
comment(0x8F07, "Load break type from hardware register", inline=True)
comment(0x8F29, "A=0", inline=True)
comment(0x8F2B, "Clear receive block pointer low", inline=True)
comment(0x8F2D, "Clear NFS workspace pointer low", inline=True)
comment(0x8F3A, "Clear workspace page counter", inline=True)
comment(0x8F3C, "Clear workspace byte", inline=True)
comment(0x8F3F, "Offset 0 in receive block", inline=True)
comment(0x8F41, "Clear remote operation flag", inline=True)
comment(0x8F48, "OSBYTE &8F: issue service request", inline=True)
# UNMAPPED: comment(0x8ED8, "X=1: workspace claim service", inline=True)
# UNMAPPED: comment(0x8EDA, "Y=&0E: requested pages", inline=True)
# UNMAPPED: comment(0x8EDF, "Record final workspace allocation", inline=True)
# UNMAPPED: comment(0x8EE2, "Load ROM present flag", inline=True)
comment(0x8F4D, "Zero: first ROM init, skip FS setup", inline=True)
comment(0x8F4F, "Set up workspace pointers", inline=True)
comment(0x8F52, "Clear FS flags", inline=True)
comment(0x8F55, "A=0, transfer to Y", inline=True)
comment(0x8F56, "Clear byte in FS workspace", inline=True)
# UNMAPPED: comment(0x8EF0, "Clear byte in NFS workspace", inline=True)
comment(0x8F58, "Advance index", inline=True)
comment(0x8F59, "Loop until full page zeroed", inline=True)
comment(0x8F74, "Offset 8 in receive block", inline=True)
comment(0x8F76, "Clear protection flags", inline=True)
comment(0x8F7A, "Initialise station identity block", inline=True)
comment(0x8F7E, "Offset 2 in receive block", inline=True)
# UNMAPPED: comment(0x8EFE, "A=&FE: default station ID marker", inline=True)
# UNMAPPED: comment(0x8F00, "Store default station low", inline=True)
# UNMAPPED: comment(0x8F03, "Store into receive block", inline=True)
# UNMAPPED: comment(0x8F05, "A=0", inline=True)
# UNMAPPED: comment(0x8F07, "Clear station high byte", inline=True)
# UNMAPPED: comment(0x8F0B, "Store into receive block", inline=True)
# UNMAPPED: comment(0x8F0D, "Offset 3 in NFS workspace", inline=True)
# UNMAPPED: comment(0x8F0F, "Clear NFS workspace byte 3", inline=True)
# UNMAPPED: comment(0x8F12, "A=&EB: default listen state", inline=True)
comment(0x8F80, "Store at NFS workspace offset 2", inline=True)
comment(0x8F82, "X=3: init data byte count", inline=True)
comment(0x8F84, "Load initialisation data byte", inline=True)
comment(0x8F87, "Store in workspace", inline=True)
comment(0x8F8A, "Decrement counter", inline=True)
comment(0x8F8B, "More bytes: loop", inline=True)
comment(0x8F8D, "Clear workspace flag", inline=True)
comment(0x8F90, "Clear workspace byte", inline=True)
# ws_init_data (&8F48): 3 workspace initialisation bytes.
# Label overlaps last byte of JMP at &8F46 (classic 6502 trick).
# Loop reads ws_init_data+X with X=3,2,1, storing to fs_flags+X.
# UNMAPPED: comment(0x8F49, "Workspace init data\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "3 bytes read via LDA ws_init_data,X with X=3\n"
# UNMAPPED:     "down to 1. ws_init_data at &8F48 overlaps the\n"
# UNMAPPED:     "high byte of JMP err_bad_station_num; byte at\n"
# UNMAPPED:     "&8F48 itself (&92) is never read (BNE exits\n"
# UNMAPPED:     "when X=0). Stores to tx_retry_count (&0D6D),\n"
# UNMAPPED:     "rx_wait_timeout (&0D6E), peek_retry_count\n"
# UNMAPPED:     "(&0D6F).")
# UNMAPPED: comment(0x8F49, "tx_retry_count: init=&FF (255 retries)", inline=True)
# UNMAPPED: comment(0x8F4A, "rx_wait_timeout: init=&28 (40, reply wait)", inline=True)
# UNMAPPED: comment(0x8F4B, "peek_retry_count: init=&0A (10, peek retries)", inline=True)
comment(0x8F93, "Initialise ADLC protection table", inline=True)
comment(0x8F96, "X=&FF (underflow from X=0)", inline=True)
comment(0x8FA9, "Get current workspace page", inline=True)
comment(0x8F97, "Initialise workspace flag to &FF", inline=True)
comment(0x8FAB, "Allocate FS handle page", inline=True)
comment(0x8FAE, "Allocation failed: finish init", inline=True)
comment(0x8FB0, "A=&3F: default handle permissions", inline=True)
comment(0x8FB2, "Store handle permissions", inline=True)
comment(0x8FB4, "Advance to next page", inline=True)
comment(0x8FB6, "Continue allocating: loop", inline=True)
comment(0x8FB8, "Restore FS context from saved state", inline=True)
# UNMAPPED: comment(0x8F40, "Read station ID from hardware", inline=True)
comment(0x8FBE, "Transfer to A", inline=True)
comment(0x8FBF, "Non-zero: station ID valid", inline=True)
# UNMAPPED: comment(0x8F46, "Station 0: report error", inline=True)
# UNMAPPED: comment(0x8F4C, "Increment station ID", inline=True)
comment(0x9000, "Overflow to 0: report error", inline=True)
comment(0x9004, "Offset 1: station ID in recv block", inline=True)
comment(0x9006, "Store station ID", inline=True)
comment(0x9008, "X=&40: Econet flag byte", inline=True)
comment(0x900A, "Store Econet control flag", inline=True)
comment(0x901D, "A=3: protection level", inline=True)
comment(0x901F, "Set up Econet protection", inline=True)
comment(0x903C, "Initialise ADLC hardware", inline=True)
comment(0x903F, "OSBYTE &A8: read ROM pointer table", inline=True)
comment(0x9041, "Read ROM pointer table address", inline=True)
comment(0x9044, "Store table pointer low", inline=True)
comment(0x9046, "Store table pointer high", inline=True)
comment(0x9048, "Y=&36: NETV vector offset", inline=True)
comment(0x904A, "Set NETV address", inline=True)
comment(0x904D, "X=1: one more vector pair to set", inline=True)
comment(0x904F, "Load vector address low byte", inline=True)
comment(0x9052, "Store into extended vector table", inline=True)
comment(0x9054, "Advance to high byte", inline=True)
comment(0x9055, "Load vector address high byte", inline=True)
comment(0x9058, "Store into extended vector table", inline=True)
comment(0x905A, "Advance to ROM ID byte", inline=True)
comment(0x905B, "Load current ROM slot number", inline=True)
comment(0x905D, "Store ROM ID in extended vector", inline=True)
comment(0x905F, "Advance to next vector entry", inline=True)
comment(0x9060, "Decrement vector counter", inline=True)
comment(0x9061, "More vectors to set: loop", inline=True)
# UNMAPPED: comment(0x8F84, "X=&FF", inline=True)
# UNMAPPED: comment(0x8F84, "Restore FS state if previously active", inline=True)
# UNMAPPED: comment(0x8F87, "Get workspace page for ROM slot", inline=True)
# UNMAPPED: comment(0x8F8A, "Advance Y past workspace page", inline=True)
comment(0x9063, "Return", inline=True)
comment(0x9064, "Y=9: end of FS context block", inline=True)
comment(0x9066, "Load FS context byte", inline=True)
comment(0x9069, "Store into receive block", inline=True)
comment(0x906B, "Decrement index", inline=True)
comment(0x906C, "Reached offset 1?", inline=True)
comment(0x906E, "No: continue copying", inline=True)
comment(0x9070, "Return", inline=True)
comment(0x9071, "FS currently selected?", inline=True)
comment(0x9074, "No (bit 7 clear): return", inline=True)
comment(0x9076, "Y=0", inline=True)
# UNMAPPED: comment(0x8FA0, "Reset FS connection state", inline=True)
# UNMAPPED: comment(0x8FA3, "OSBYTE &77: close SPOOL/EXEC", inline=True)
comment(0x907B, "Restore FS context to receive block", inline=True)
comment(0x907E, "Y=&76: checksum range end", inline=True)
comment(0x9080, "A=0: checksum accumulator", inline=True)
comment(0x9082, "Clear carry for addition", inline=True)
comment(0x9083, "Add byte from page &10 shadow", inline=True)
comment(0x9086, "Decrement index", inline=True)
comment(0x9087, "Loop until all bytes summed", inline=True)
comment(0x9089, "Y=&77: checksum storage offset", inline=True)
comment(0x908D, "Load byte from page &10 shadow", inline=True)
comment(0x9090, "Copy to FS workspace", inline=True)
comment(0x9092, "Decrement index", inline=True)
comment(0x9093, "Loop until all bytes copied", inline=True)
comment(0x9095, "Load FS flags", inline=True)
comment(0x9098, "Clear bit 7 (FS no longer selected)", inline=True)
comment(0x909A, "Store updated flags", inline=True)
comment(0x909D, "Return", inline=True)
comment(0x909E, "Save processor status", inline=True)
comment(0x909F, "Save A", inline=True)
# UNMAPPED: comment(0x8FCD, "Transfer Y to A", inline=True)
# UNMAPPED: comment(0x8FCE, "Save Y", inline=True)
comment(0x90A1, "Y=&76: checksum range end", inline=True)
comment(0x90A3, "A=0: checksum accumulator", inline=True)
comment(0x90A5, "Clear carry for addition", inline=True)
comment(0x90A6, "Add byte from FS workspace", inline=True)
comment(0x90A8, "Decrement index", inline=True)
comment(0x90A9, "Loop until all bytes summed", inline=True)
comment(0x90AB, "Y=&77: checksum storage offset", inline=True)
comment(0x90AD, "Compare with stored checksum", inline=True)
comment(0x90AF, "Mismatch: raise checksum error", inline=True)
# UNMAPPED: comment(0x8FDF, "Restore Y", inline=True)
# UNMAPPED: comment(0x8FE0, "Transfer to Y", inline=True)
comment(0x90B2, "Restore A", inline=True)
comment(0x90B3, "Restore processor status", inline=True)
comment(0x90B4, "Return (checksum valid)", inline=True)
comment(0x90B5, "Error number &AA", inline=True)
comment(0x90B7, "Raise 'net checksum' error", inline=True)
# UNMAPPED: comment(0x8FF1, "Print 'Econet Station ' prefix", inline=True)
comment(0x90CC, "Print 'Econet Station ' via inline", inline=True)
# UNMAPPED: comment(0x9003, "Y=1: station number offset in RX block", inline=True)
# UNMAPPED: comment(0x9005, "Load station ID from receive block", inline=True)
# UNMAPPED: comment(0x9007, "Print station number as decimal", inline=True)
comment(0x90E0, "Space character", inline=True)
comment(0x90E2, "Check ADLC status register 2", inline=True)
comment(0x90E5, "Clock present: skip warning", inline=True)
comment(0x90E7, "Print ' No Clock' via inline", inline=True)
comment(0x90F3, "NOP (string terminator)", inline=True)
comment(0x90F7, "Return", inline=True)

# cmd_syntax_strings (&9022-&910D): null-terminated *HELP syntax
# strings. Multi-line strings use &0D as a line break. Indexed
# via cmd_syntax_table offsets from the low 5 bits of each
# command table syntax descriptor byte.
comment(0x90F8, "*HELP command syntax strings\n"
    "\n"
    "13 null-terminated syntax help strings displayed\n"
    "by *HELP after each command name. Multi-line\n"
    "entries use &0D as a line break. Indexed by\n"
    "cmd_syntax_table via the low 5 bits of each\n"
    "command's syntax descriptor byte.")
comment(0x90F8, "Syn 1: *Dir, *LCat, *LEx, *Wipe", inline=True)
# UNMAPPED: comment(0x9029, "Null terminator", inline=True)
comment(0x9100, "Syn 2: *I Am (login)", inline=True)
comment(0x9118, "Line break", inline=True)
# UNMAPPED: comment(0x9043, "Syn 2 continued: password clause", inline=True)
# UNMAPPED: comment(0x9056, "Null terminator", inline=True)
comment(0x912D, "Syn 3: *Delete, *FS, *Remove", inline=True)
# UNMAPPED: comment(0x905F, "Null terminator", inline=True)
# UNMAPPED: comment(0x9060, "Syn 4: *Dump", inline=True)
# UNMAPPED: comment(0x9075, "Line break", inline=True)
comment(0x914C, "Syn 4 continued: address clause", inline=True)
comment(0x9158, "Null terminator", inline=True)
comment(0x9159, "Syn 5: *Lib", inline=True)
# UNMAPPED: comment(0x9088, "Null terminator", inline=True)
# UNMAPPED: comment(0x9089, "Syn 6: *CDir", inline=True)
# UNMAPPED: comment(0x9099, "Null terminator", inline=True)
comment(0x9170, "Syn 7: *Pass", inline=True)
# UNMAPPED: comment(0x90AD, "Line break", inline=True)
comment(0x9184, "Syn 7 continued: new password", inline=True)
# UNMAPPED: comment(0x90BC, "Null terminator", inline=True)
# UNMAPPED: comment(0x90BD, "Syn 8: *PS, *Pollps", inline=True)
# UNMAPPED: comment(0x90D3, "Null terminator", inline=True)
comment(0x91AA, "Syn 9: *Access", inline=True)
# UNMAPPED: comment(0x90EF, "Null terminator", inline=True)
comment(0x91C6, "Syn 10: *Rename", inline=True)
comment(0x91DF, "Null terminator", inline=True)
comment(0x91E0, "Syn 11: (station id. argument)", inline=True)
comment(0x91EC, "Null terminator", inline=True)
# UNMAPPED: comment(0x9117, "Syn 12: *Print, *Type", inline=True)
# UNMAPPED: comment(0x9121, "Null terminator", inline=True)

# cmd_syntax_table (&910E): 13-entry offset table for *HELP syntax.
# Each byte is an offset into cmd_syntax_strings (&9022). The print
# loop does INY before LDA, so the offset points to the byte before
# the first character of each syntax string.
comment(0x91ED, "Command syntax string offset table\n"
    "\n"
    "13 offsets into cmd_syntax_strings (&9022).\n"
    "Indexed by the low 5 bits of each command table\n"
    "syntax descriptor byte. Index &0E is handled\n"
    "separately as a shared-commands list. The print\n"
    "loop at &8BD5 does INY before LDA, so each offset\n"
    "points to the byte before the first character.")
comment(0x91ED, "Idx 0: (no syntax)", inline=True)
# UNMAPPED: comment(0x9123, "Idx 1: \"(<dir>)\" (Y wraps via &FF)", inline=True)
comment(0x91EF, "Idx 2: \"(<stn.id.>) <user id.>...\"", inline=True)
comment(0x91F0, "Idx 3: \"<object>\"", inline=True)
# UNMAPPED: comment(0x9126, "Idx 4: \"<filename> (<offset>...)\"", inline=True)
# UNMAPPED: comment(0x9127, "Idx 5: \"<dir>\"", inline=True)
# UNMAPPED: comment(0x9128, "Idx 6: \"<dir> (<number>)\"", inline=True)
# UNMAPPED: comment(0x9129, "Idx 7: \"(:<CR>) <password>...\"", inline=True)
comment(0x91F5, "Idx 8: \"(<stn.id.>|<ps type>)\"", inline=True)
comment(0x91F6, "Idx 9: \"<object> (L)(W)(R)...\"", inline=True)
# UNMAPPED: comment(0x912C, "Idx 10: \"<filename> <new filename>\"", inline=True)
comment(0x91F8, "Idx 11: \"(<stn. id.>)\"", inline=True)
# UNMAPPED: comment(0x912E, "Idx 12: \"<filename>\"", inline=True)

comment(0x9236, "Save full byte", inline=True)
comment(0x9237, "Shift high nybble to low", inline=True)
comment(0x9238, "Continue shifting", inline=True)
comment(0x9239, "Continue shifting", inline=True)
comment(0x923A, "High nybble now in bits 0-3", inline=True)
comment(0x923B, "Print high nybble as hex digit", inline=True)
comment(0x923E, "Restore full byte", inline=True)
comment(0x923F, "Mask to low nybble", inline=True)
comment(0x9241, "Digit >= &0A?", inline=True)
comment(0x9243, "No: skip letter adjustment", inline=True)
comment(0x9245, "Add 7 to get 'A'-'F' (6 + carry)", inline=True)
comment(0x9247, "Add &30 for ASCII '0'-'9' or 'A'-'F'", inline=True)
# txcb_init_template (&948B) — 12-byte TXCB template
comment(0x9763, "TXCB initialisation template (12 bytes)\n"
    "\n"
    "Copied by init_txcb into the TXCB workspace at\n"
    "&00C0. For offsets 0-1, the destination station\n"
    "bytes are also copied from l0e00 into txcb_dest.\n"
    "\n"
    "The &FF byte at offset 6 (bit_test_ff, &9491)\n"
    "serves double duty: it is part of this template\n"
    "AND a BIT target used by 22 callers to set the\n"
    "V and N flags without clobbering A.")
comment(0x9763, "Offset 0: txcb_ctrl = &80 (transmit)", inline=True)
# UNMAPPED: comment(0x948C, "Offset 1: txcb_port = &99 (FS reply)", inline=True)
# UNMAPPED: comment(0x948D, "Offset 2: txcb_dest lo (overwritten)", inline=True)
# UNMAPPED: comment(0x948E, "Offset 3: txcb_dest hi (overwritten)", inline=True)
comment(0x9765, "Offset 4: txcb_start = 0", inline=True)
# UNMAPPED: comment(0x9490, "Offset 5: buffer start hi (page &0F)", inline=True)
comment(0x976A, "Offset 6: BIT target / buffer end lo", inline=True)
comment(0x976B, "Offset 7: txcb_pos = &FF", inline=True)
# UNMAPPED: comment(0x9493, "Offset 8: txcb_end = &FF", inline=True)
# UNMAPPED: comment(0x9494, "Offset 9: buffer end hi (page &0F)", inline=True)
# UNMAPPED: comment(0x9495, "Offset 10: extended addr fill (&FF)", inline=True)
comment(0x976E, "Offset 11: extended addr fill (&FF)", inline=True)

# ============================================================
# Service dispatch table (&89CA/&89EF)
# ============================================================
# 37-entry PHA/PHA/RTS dispatch table used by svc_dispatch.
# Indices 0-14: service dispatch (index = mapped service code + 1).
# Indices 15-36: extended dispatch for FS commands and OSWORD routing.
# Service codes 1-12 map directly; 18 maps to index 14 via SBC #5.
# Indices 1, 7, 11 point to dispatch_rts (RTS = no-op).

# UNMAPPED: comment(0x89CA, """\
# UNMAPPED: Service dispatch table (37 entries, split lo/hi).
# UNMAPPED: PHA/PHA/RTS dispatch used by svc_dispatch.
# UNMAPPED: Indices 0-14: service calls (index = service + 1).
# UNMAPPED: Indices 15-36: FS command and OSWORD routing.
# UNMAPPED: Indices 1, 7, 11 point to return_4 (no-op RTS).""")

# UNMAPPED: label(0x89CA, "svc_dispatch_lo")
# UNMAPPED: label(0x89EF, "svc_dispatch_hi")

# Mark dispatch table entries as symbolic address pairs.
# Skip index 0 (outside ROM range, unused dispatch slot).
# UNMAPPED: for i in range(1, 37):
# UNMAPPED:     rts_code_ptr(0x89CA + i, 0x89EF + i)

# Inline comments describing each dispatch slot's purpose.
# Applied to both lo and hi byte entries with "lo - " / "hi - " prefix.
svc_dispatch_comments = [
    # Index 0: dummy entry
    "dummy entry (outside ROM range)",
    # Service calls (Y=&00, indices 1-14)
    "Svc 0: already claimed (no-op)",
    "Svc 1: absolute workspace",
    "Svc 2: private workspace",
    "Svc 3: auto-boot",
    "Svc 4: unrecognised star command",
    "Svc 5: unrecognised interrupt",
    "Svc 6: BRK (no-op)",
    "Svc 7: unrecognised OSBYTE",
    "Svc 8: unrecognised OSWORD",
    "Svc 9: *HELP",
    "Svc 10: static workspace (no-op)",
    "Svc 11: NMI release (reclaim NMIs)",
    "Svc 12: NMI claim (save NMI state)",
    "Svc 18: filing system selection",
    # Language entry handlers (Y=&0E, indices 15-19)
    "Lang 0: no language / Tube",
    "Lang 1: normal startup",
    "Lang 2: softkey byte (Electron)",
    "Lang 3: softkey length (Electron)",
    "Lang 4: remote validated",
    # FSCV handlers (Y=&13, indices 20-27)
    "FSCV 0: *OPT",
    "FSCV 1: EOF check",
    "FSCV 2: */ (run)",
    "FSCV 3: unrecognised star command",
    "FSCV 4: *RUN",
    "FSCV 5: *CAT",
    "FSCV 6: shutdown",
    "FSCV 7: read handle range",
    # FS reply handlers (Y=&17, indices 28-33)
    "FS reply: print directory name",
    "FS reply: copy handles + boot",
    "FS reply: copy handles",
    "FS reply: set CSD handle",
    "FS reply: notify + execute",
    "FS reply: set library handle",
    # *NET sub-command handlers (Y=&21, indices 34-36)
    "*NET1: read handle from packet",
    "*NET2: read handle from workspace",
    "*NET3: close handle",
]
# UNMAPPED: for i, body in enumerate(svc_dispatch_comments):
# UNMAPPED:     comment(0x89CA + i, f"lo - {body}", inline=True)
# UNMAPPED:     comment(0x89EF + i, f"hi - {body}", inline=True)

# Service dispatch targets — already labelled
# Index 6 (svc 5): &8023 = svc5_irq_check (unrecognised interrupt)
# Index 12 (svc 11): &8085 = svc_11_nmi_claim (NMI claim)
# Index 13 (svc 12): &8979 = wait_idle_and_reset (NMI release)

# Service dispatch targets — new entry points
entry(0x8EE9)   # Index 2 (svc 1): absolute workspace claim
# UNMAPPED: entry(0x8EB8)   # Index 3 (svc 2): private workspace
entry(0x8CC7)   # Index 4 (svc 3): auto-boot
entry(0x8C42)   # Index 5 (svc 4): unrecognised star command
entry(0x8ED8)   # Index 8 (svc 7): unrecognised OSBYTE
# UNMAPPED: entry(0xA4EE)   # Index 9 (svc 8): unrecognised OSWORD
entry(0x8C51)   # Index 10 (svc 9): *HELP
# UNMAPPED: entry(0x8B0D)   # Index 14 (svc 18): filing system selection

label(0x8EE9, "svc_1_abs_workspace")
# UNMAPPED: label(0x8EB8, "svc_2_private_workspace")
label(0x8CC7, "svc_3_autoboot")
label(0x8C42, "svc_4_star_command")
label(0x8ED8, "svc_7_osbyte")
# UNMAPPED: label(0xA4EE, "svc_8_osword")
label(0x8C51, "svc_9_help")
# UNMAPPED: label(0x8B0D, "svc_18_fs_select")

subroutine(0x8EE9, "svc_1_abs_workspace",
    title="Service 1: absolute workspace claim",
    description="Ensures the NFS workspace allocation is at least\n"
    "&16 pages by checking Y on entry. If Y < &16,\n"
    "sets Y = &16 to claim the required pages;\n"
    "otherwise returns Y unchanged. This is a passive\n"
    "claim — NFS only raises the allocation, never\n"
    "lowers it.",
    on_entry={"y": "current highest workspace page claim"},
    on_exit={"y": ">= &16 (NFS minimum requirement)"})
# UNMAPPED: subroutine(0x8EB8, "svc_2_private_workspace",
# UNMAPPED:     title="Service 2: claim private workspace and initialise NFS",
# UNMAPPED:     description="Handles MOS service call 2 (private workspace\n"
# UNMAPPED:     "claim). Allocates two workspace pages starting\n"
# UNMAPPED:     "at Y: the receive block page (net_rx_ptr_hi) and\n"
# UNMAPPED:     "NFS workspace page (nfs_workspace_hi), plus a\n"
# UNMAPPED:     "per-ROM workspace page stored at &0DF0+ROM slot.\n"
# UNMAPPED:     "Zeroes all workspace, initialises the station ID\n"
# UNMAPPED:     "from the Econet hardware register at &FE18,\n"
# UNMAPPED:     "allocates FS handle pages, copies initial state\n"
# UNMAPPED:     "to page &10, and falls through to\n"
# UNMAPPED:     "init_adlc_and_vectors.",
# UNMAPPED:     on_entry={"y": "first available private workspace page"})
subroutine(0x8CC7, "svc_3_autoboot",
    title="Service 3: auto-boot on reset",
    description="Scans the keyboard via OSBYTE &7A for the 'N' key\n"
    "(&19 or &55 EOR'd with &55). If pressed, records\n"
    "the key state via OSBYTE &78. Selects the network\n"
    "filing system by calling cmd_net_fs, prints the\n"
    "station ID, then checks if this is the first boot\n"
    "(ws_page = 0). If so, sets the auto-boot flag in\n"
    "&1071 and JMPs to cmd_fs_entry to execute the boot\n"
    "file.")
subroutine(0x8C42, "svc_4_star_command",
    title="Service 4: unrecognised star command",
    description="Saves the OS text pointer, then calls match_fs_cmd\n"
    "to search the command table starting at offset 0\n"
    "(all command sub-tables). If no match is found (carry\n"
    "set), returns with the service call unclaimed. On\n"
    "a match, JMPs to cmd_fs_reentry to execute the\n"
    "matched command handler via the PHA/PHA/RTS\n"
    "dispatch mechanism.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8ED8, "svc_7_osbyte",
    title="Service 7: unrecognised OSBYTE",
    description="Maps Econet OSBYTE codes &32-&35 to dispatch\n"
    "indices 0-3 by subtracting &31 (with carry from\n"
    "a preceding SBC). Returns unclaimed if the OSBYTE\n"
    "number is outside this range. For valid codes,\n"
    "claims the service (sets svc_state to 0) and\n"
    "JMPs to svc_dispatch with Y=&21 to reach the\n"
    "Econet OSBYTE handler table.",
    on_entry={"a": "OSBYTE number (from osbyte_a_copy at &EF)"})
# Located in 4.21_v1 at &A83B (was &A4EE in 4.18) by opcode fingerprint
# (ratio 0.952 over 21 opcodes). Reached via PHA/PHA/RTS dispatch.
entry(0xA83B)
subroutine(0xA83B, "svc_8_osword",
    title="Service 8: unrecognised OSWORD",
    description="Handles MOS service call 8 (unrecognised OSWORD).\n"
    "Filters OSWORD codes &0E-&14 by subtracting &0E (via\n"
    "CLC/SBC &0D) and rejecting values outside 0-6. For\n"
    "valid codes, calls osword_setup_handler to push the\n"
    "dispatch address, then copies 3 bytes from the RX\n"
    "buffer to osword_flag workspace.")
subroutine(0x8C51, "svc_9_help",
    title="Service 9: *HELP",
    description="Handles MOS service call 9 (*HELP). First checks\n"
    "for the credits Easter egg. For bare *HELP (CR\n"
    "at text pointer), prints the version header and\n"
    "full command list starting at table offset &C4.\n"
    "For *HELP with an argument, handles '.' as a\n"
    "shortcut to list all NFS commands, otherwise\n"
    "iterates through help topics using PHA/PHA/RTS\n"
    "dispatch to print matching command groups.\n"
    "Returns with Y = ws_page (unclaimed).")
# Located in 4.21_v1 at &8B45 (was &8B0D in 4.18) by opcode fingerprint.
# Reached via PHA/PHA/RTS dispatch from the service table — no direct
# JSR/JMP, so an explicit entry() is required to classify it as code.
entry(0x8B45)
subroutine(0x8B52, "select_fs_via_cmd_net_fs",
    title="Force ANFS selection (raise net checksum on failure)",
    description="Tail-fragment of ensure_fs_selected used directly by "
    "svc_3_autoboot when an autoboot needs to force-select ANFS as "
    "the active filing system. Calls cmd_net_fs to perform the actual "
    "selection; on failure (BEQ not taken), JMPs to error_net_checksum "
    "to raise the 'net checksum' error. Used when there is no clean "
    "BIT fs_flags / BMI shortcut for early-return.",
    on_exit={"a": "current FS state byte if selection succeeded, "
                  "else this routine never returns"})

subroutine(0x924C, "print_hex_byte_no_spool",
    title="Print A as two hex digits, *SPOOL-bypassing",
    description="As print_hex_byte (&9236) but emits each digit via "
    "print_char_no_spool (the *SPOOL-bypassing OSASCI wrapper), so the "
    "digits don't appear in any active spool capture. Saves A, "
    "extracts the high nibble (LSR x4), prints it via "
    "print_hex_nybble_no_spool, then restores A and falls through "
    "for the low nibble. Sole caller: print_5_hex_bytes at &9D53.",
    on_entry={"a": "byte to print"},
    on_exit={"a": "preserved"})

subroutine(0x9255, "print_hex_nybble_no_spool",
    title="Print low nybble of A as one hex digit, *SPOOL-bypassing",
    description="As print_hex_nybble (&923F) but emits via the "
    "print_char_no_spool tail-call instead of OSASCI directly, so the "
    "digit is not captured by any active *SPOOL file. Standard "
    "AND #&0F / CMP #&0A / +6-or-not / + #&30 mapping for hex "
    "digits 0-9 / A-F. Tail-jumps to print_char_no_spool via BRA.",
    on_entry={"a": "value (low nybble used)"})

subroutine(0x9612, "osbyte_a2",
    title="OSBYTE &A2 (write Master CMOS RAM byte)",
    description="Three-instruction wrapper: LDA #&A2 / JSR OSBYTE / "
    "BRA c95be. Writes the Master 128 CMOS RAM byte indexed by X "
    "with the value in Y. Sole caller: format_filename_field at "
    "&A0FE. Counterpart of osbyte_a1 at &8E9A (read).",
    on_entry={"x": "CMOS RAM byte index", "y": "value to write"})

subroutine(0x8B45, "svc_18_fs_select",
    title="Service 18: filing system selection request",
    description="Checks if Y=5 (Econet filing system number);\n"
    "returns unclaimed if not. Also returns if bit 7\n"
    "of &0D6C is already set, indicating the FS is\n"
    "already selected. Otherwise falls through to\n"
    "cmd_net_fs to perform the full network filing\n"
    "system selection sequence.",
    on_entry={"y": "filing system number requested"})

# Extended dispatch table entries (indices 15-36).
# These may be reached via FS command dispatch or OSWORD dispatch
# with non-zero Y offsets through c8e33.
entry(0x98AF)
entry(0x9850)
entry(0xB01A)
entry(0x987E)
entry(0x989F)
entry(0xA0A9)
entry(0x9E7F)
entry(0xA10B)
entry(0xA4E4)
entry(0xA42F)
entry(0xB118)
entry(0x9071)
entry(0x93F2)
# UNMAPPED: entry(0xAF3E)
entry(0xA6D5)
entry(0xA6E5)
entry(0xA638)
entry(0xA63E)
entry(0xA3FF)
entry(0xA405)
entry(0xA415)


# ============================================================
# Star command table (&A3D8-&A4D5)
# ============================================================
# Four sub-tables of star command entries. Each entry:
# ASCII command name + flag byte (>= &80) + dispatch word (EQUW).
# Tables separated by &80 sentinel bytes.
# Flag byte: bit 7 = end of name, bit 6 = set V if no arg,
# bits 0-4 = syntax string index into cmd_syntax_table.

# UNMAPPED: comment(0xA3F0, """\
# UNMAPPED: Star command table (4 interleaved sub-tables).
# UNMAPPED: Each entry: ASCII name + flag byte (&80+) +
# UNMAPPED: dispatch address word (PHA/PHA/RTS, addr-1).
# UNMAPPED: Sub-tables separated by &80 sentinel bytes.
# UNMAPPED: Flag byte: bit 7 = end of name marker,
# UNMAPPED: bit 6 = set V on return if no argument,
# UNMAPPED: bits 0-4 = *HELP syntax string index.
# UNMAPPED: 1: Utility cmds  2: NFS commands
# UNMAPPED: 3: Help topics  4: Copro/attributes""")

# UNMAPPED: label(0xA3F0, "cmd_table_fs")
label(0xA7A1, "cmd_table_nfs")
# UNMAPPED: label(0xA4B2, "cmd_table_help")
# UNMAPPED: label(0xA4C3, "cmd_table_copro")

# Force short command name fragments to display as equs strings.
# py8dis auto-classifies these as equb when adjacent to flag bytes.
# UNMAPPED: string(0xA3F0, 1)    # "C" (first char of *Close)
# UNMAPPED: string(0xA3F1, 1)    # "l" (dispatch lo base byte of *Close)
string(0xA782, 2)    # "PS"
byte(0xA784)
# UNMAPPED: string(0xA45F, 2)    # "Ex"
# UNMAPPED: byte(0xA461)
# UNMAPPED: string(0xA46B, 2)    # "FS"
byte(0xA7C6)

# Sub-table 1: utility commands
# Table stores address-1 for PHA/PHA/RTS dispatch; actual targets are +1.
# UNMAPPED: entry(0xB994)   # *Close
entry(0xBD41)   # *Dump
entry(0x8B23)   # *Net (select NFS)
entry(0xB581)   # *Pollps
# UNMAPPED: entry(0xB99D)   # *Print
# UNMAPPED: entry(0xB30C)   # *Prot
entry(0xB3AC)   # *PS
# UNMAPPED: entry(0xB99A)   # *Type
# UNMAPPED: entry(0xB33D)   # *Unprot
entry(0x8AEA)   # *Roff

# Mark dispatch address words as symbolic label expressions.
# Each entry: (addr, target_label). Uses EQUW (little-endian word).
_cmd_entries = [
    # Sub-table 1: utility commands
# UNMAPPED:     (0xA3F6, "cmd_close"),
# UNMAPPED:     (0xA3FD, "cmd_dump"),
# UNMAPPED:     (0xA403, "cmd_net_fs"),
# UNMAPPED:     (0xA40C, "cmd_pollps"),
# UNMAPPED:     (0xA414, "cmd_print"),
# UNMAPPED:     (0xA41B, "cmd_prot"),
# UNMAPPED:     (0xA420, "cmd_ps"),
# UNMAPPED:     (0xA427, "cmd_roff"),
# UNMAPPED:     (0xA42E, "cmd_type"),
# UNMAPPED:     (0xA437, "cmd_unprot"),
    # Sub-table 2: NFS commands
# UNMAPPED:     (0xA441, "cmd_fs_operation"),   # *Access
# UNMAPPED:     (0xA447, "cmd_bye"),
# UNMAPPED:     (0xA44E, "cmd_cdir"),
# UNMAPPED:     (0xA457, "cmd_fs_operation"),   # *Delete
# UNMAPPED:     (0xA45D, "cmd_dir"),
# UNMAPPED:     (0xA462, "cmd_ex"),
# UNMAPPED:     (0xA469, "cmd_flip"),
# UNMAPPED:     (0xA46E, "cmd_fs"),
# UNMAPPED:     (0xA475, "cmd_fs_operation"),   # *Info
# UNMAPPED:     (0xA47C, "cmd_iam"),
# UNMAPPED:     (0xA483, "cmd_lcat"),
# UNMAPPED:     (0xA489, "cmd_lex"),
# UNMAPPED:     (0xA48F, "cmd_fs_operation"),   # *Lib
# UNMAPPED:     (0xA496, "cmd_pass"),
# UNMAPPED:     (0xA49F, "cmd_remove"),
# UNMAPPED:     (0xA4A8, "cmd_rename"),
# UNMAPPED:     (0xA4AF, "cmd_wipe"),
    # Sub-table 3: help topic handlers
# UNMAPPED:     (0xA4B8, "help_net"),
# UNMAPPED:     (0xA4C0, "help_utils"),
    # Sub-table 4 (copro) skipped — targets outside ROM range
]
for addr, target_label in _cmd_entries:
    word(addr)
    expr(addr, target_label + "-1")

# Inline comments for every item in the command table.
# Name strings: command identification.
# Flag bytes: decode bit 6 (V if no arg) and syntax index.
# Dispatch words: PHA/PHA/RTS target.
# Sentinels: sub-table terminators.

# Sub-table 1: utility commands (&A3D8-&A421)
# UNMAPPED: comment(0xA3F0, "*Close (first char)", inline=True)
# UNMAPPED: comment(0xA3F1, "*Close cont (dispatch lo base)", inline=True)
# UNMAPPED: comment(0xA3F2, "*Close cont (dispatch hi base)", inline=True)
# UNMAPPED: comment(0xA3F5, "No syntax", inline=True)
# UNMAPPED: comment(0xA3F8, "*Dump", inline=True)
comment(0xA76C, "*Net (select NFS)", inline=True)
comment(0xA76F, "No syntax", inline=True)
# UNMAPPED: comment(0xA405, "*Pollps", inline=True)
comment(0xA778, "Syn 8: (<stn. id.>|<ps type>)", inline=True)
# UNMAPPED: comment(0xA40E, "*Print", inline=True)
# UNMAPPED: comment(0xA413, "V no arg; syn 12: <filename>", inline=True)
comment(0xA77B, "*Prot", inline=True)
# UNMAPPED: comment(0xA41A, "Syn 14: (attribute keywords)", inline=True)
comment(0xA782, "*PS; syn 8: (<stn. id.>|<ps type>)", inline=True)
# UNMAPPED: comment(0xA422, "*Roff", inline=True)
comment(0xA78B, "No syntax", inline=True)
# UNMAPPED: comment(0xA429, "*Type", inline=True)
# UNMAPPED: comment(0xA42D, "V no arg; syn 12: <filename>", inline=True)
comment(0xA78E, "*Unprot", inline=True)
# UNMAPPED: comment(0xA436, "Syn 14: (attribute keywords)", inline=True)
# UNMAPPED: comment(0xA439, "End of utility sub-table", inline=True)

# Sub-table 2: NFS commands (&A422-&A499)
comment(0xA7A1, "*Access", inline=True)
comment(0xA7A7, "V no arg; syn 9: <obj> (L)(W)(R)...", inline=True)
# UNMAPPED: comment(0xA443, "*Bye", inline=True)
# UNMAPPED: comment(0xA446, "No syntax", inline=True)
# UNMAPPED: comment(0xA449, "*Cdir", inline=True)
# UNMAPPED: comment(0xA44D, "V no arg; syn 6: <dir> (<number>)", inline=True)
# UNMAPPED: comment(0xA450, "*Delete", inline=True)
# UNMAPPED: comment(0xA456, "V no arg; syn 3: <object>", inline=True)
comment(0xA7B7, "*Dir", inline=True)
comment(0xA7BA, "Syn 1: (<dir>)", inline=True)
# UNMAPPED: comment(0xA45F, "*Ex; syn 1: (<dir>)", inline=True)
# UNMAPPED: comment(0xA464, "*Flip", inline=True)
comment(0xA7C1, "No syntax", inline=True)
# UNMAPPED: comment(0xA46B, "*FS; syn 11: (<stn. id.>)", inline=True)
# UNMAPPED: comment(0xA470, "*Info", inline=True)
# UNMAPPED: comment(0xA474, "V no arg; syn 3: <object>", inline=True)
comment(0xA7C9, "*I am", inline=True)
comment(0xA7CD, "V no arg; syn 2: (<stn>) <user>...", inline=True)
# UNMAPPED: comment(0xA47E, "*Lcat", inline=True)
# UNMAPPED: comment(0xA482, "Syn 1: (<dir>)", inline=True)
# UNMAPPED: comment(0xA485, "*Lex", inline=True)
# UNMAPPED: comment(0xA488, "Syn 1: (<dir>)", inline=True)
# UNMAPPED: comment(0xA48B, "*Lib", inline=True)
# UNMAPPED: comment(0xA48E, "V no arg; syn 5: <dir>", inline=True)
# UNMAPPED: comment(0xA491, "*Pass", inline=True)
comment(0xA7E7, "V no arg; syn 7: <pass> ...", inline=True)
# UNMAPPED: comment(0xA498, "*Remove", inline=True)
# UNMAPPED: comment(0xA4A2, "V no arg; syn 3: <object>", inline=True)
# UNMAPPED: comment(0xA4A1, "*Rename", inline=True)
# UNMAPPED: comment(0xA4A7, "V no arg; syn 10: <file> <new file>", inline=True)
comment(0xA7F3, "*Wipe", inline=True)
comment(0xA7FA, "End of NFS sub-table", inline=True)

# Sub-table 3: help topic handlers (&A49A-&A4AA)
# UNMAPPED: comment(0xA4B4, "*Net (local)", inline=True)
# UNMAPPED: comment(0xA4B7, "No syntax", inline=True)
comment(0xA803, "*Utils", inline=True)
comment(0xA808, "No syntax", inline=True)
comment(0xA80B, "End of help topic sub-table", inline=True)

# Sub-table 4: protection attribute keywords (&A4AB-&A4D5)
# Dual-purpose table: entries are keyword names for *Prot/*Unprot
# attribute matching, and also printed by the shared commands
# handler (syn 14) in *HELP Prot/*HELP Unprot output.
# Each entry: ASCII name + flag byte + OR mask + AND mask.
# *Prot ORs the lo byte into the protection mask.
# *Unprot ANDs the hi byte to clear the corresponding bit.
# Protection bits: 0=Peek, 1=Poke, 2=JSR, 3=Proc, 4=Utils, 5=Halt.

# UNMAPPED: comment(0xA4C3, """\
# UNMAPPED: Protection attribute keyword table. Each entry:
# UNMAPPED: ASCII name + flag byte (&80+) + OR mask + AND mask.
# UNMAPPED: Used by *Prot (ORA lo byte) and *Unprot (AND hi
# UNMAPPED: byte) to set/clear individual protection bits.
# UNMAPPED: Also listed by *HELP Prot/*HELP Unprot via the
# UNMAPPED: shared commands handler (syntax index 14).
# UNMAPPED: Bits: 0=Peek 1=Poke 2=JSR 3=Proc 4=Utils 5=Halt""")

# Split multi-byte equb groups so each byte gets its own line.
_attr_entries = [
    # (flag_addr, or_addr, and_addr)
# UNMAPPED:     (0xA4C7, 0xA4C8, 0xA4C9),   # Halt
# UNMAPPED:     (0xA4CD, 0xA4CE, 0xA4CF),   # JSR
# UNMAPPED:     (0xA4D4, 0xA4D5, 0xA4D6),   # Peek
# UNMAPPED:     (0xA4DB, 0xA4DC, 0xA4DD),   # Poke
# UNMAPPED:     (0xA4E2, 0xA4E3, 0xA4E4),   # Proc
# UNMAPPED:     (0xA4EA, 0xA4EB, 0xA4EC),   # Utils
]
for flag_addr, or_addr, and_addr in _attr_entries:
    byte(flag_addr)
    byte(or_addr)
    byte(and_addr)
# &A83B was a 1-byte sentinel in 4.18; in 4.21_v1 it's the start of
# svc_8_osword (relocated from 4.18 &A4EE). The byte() directive has
# been removed so py8dis classifies it as code.

# Inline comments for sub-table 4
# UNMAPPED: comment(0xA4C3, "Halt", inline=True)
# UNMAPPED: comment(0xA4C7, "Flag &FC: V no arg, syn 28 (unused)", inline=True)
# UNMAPPED: comment(0xA4C8, "*Prot OR mask: bit 5", inline=True)
# UNMAPPED: comment(0xA4C9, "*Unprot AND mask: ~bit 5", inline=True)
# UNMAPPED: comment(0xA4CA, "JSR", inline=True)
# UNMAPPED: comment(0xA4CD, "Flag &FC: V no arg, syn 28 (unused)", inline=True)
# UNMAPPED: comment(0xA4CE, "*Prot OR mask: bit 2", inline=True)
# UNMAPPED: comment(0xA4CF, "*Unprot AND mask: ~bit 2", inline=True)
# UNMAPPED: comment(0xA4D0, "Peek", inline=True)
# UNMAPPED: comment(0xA4D4, "Flag &FC: V no arg, syn 28 (unused)", inline=True)
# UNMAPPED: comment(0xA4D5, "*Prot OR mask: bit 0", inline=True)
# UNMAPPED: comment(0xA4D6, "*Unprot AND mask: ~bit 0", inline=True)
# UNMAPPED: comment(0xA4D7, "Poke", inline=True)
# UNMAPPED: comment(0xA4DB, "Flag &FC: V no arg, syn 28 (unused)", inline=True)
# UNMAPPED: comment(0xA4DC, "*Prot OR mask: bit 1", inline=True)
# UNMAPPED: comment(0xA4DD, "*Unprot AND mask: ~bit 1", inline=True)
# UNMAPPED: comment(0xA4DE, "Proc", inline=True)
# UNMAPPED: comment(0xA4E2, "Flag &FC: V no arg, syn 28 (unused)", inline=True)
# UNMAPPED: comment(0xA4E3, "*Prot OR mask: bit 3", inline=True)
# UNMAPPED: comment(0xA4E4, "*Unprot AND mask: ~bit 3", inline=True)
# UNMAPPED: comment(0xA4E5, "Utils", inline=True)
# UNMAPPED: comment(0xA4EA, "Flag &A9: syn 9 (unused)", inline=True)
# UNMAPPED: comment(0xA4EB, "*Prot OR mask: bit 4", inline=True)
# UNMAPPED: comment(0xA4EC, "*Unprot AND mask: ~bit 4", inline=True)
comment(0xA83B, "End of attribute keyword table", inline=True)

# UNMAPPED: label(0xB994, "cmd_close")
label(0xBD41, "cmd_dump")
label(0x8B23, "cmd_net_fs")
label(0xB581, "cmd_pollps")
# UNMAPPED: label(0xB99D, "cmd_print")
# UNMAPPED: label(0xB30C, "cmd_prot")
label(0xB3AC, "cmd_ps")
# UNMAPPED: label(0xB99A, "cmd_type")
# UNMAPPED: label(0xB33D, "cmd_unprot")
label(0x8AEA, "cmd_roff")

# UNMAPPED: subroutine(0xB994, "cmd_close",
# UNMAPPED:     title="*Close command handler",
# UNMAPPED:     description="Loads A=0 and Y=0, then jumps to OSFIND to close\n"
# UNMAPPED:     "all open files on the current file server (equivalent\n"
# UNMAPPED:     "to CLOSE#0). Files open on other file servers are\n"
# UNMAPPED:     "not affected.")
subroutine(0xBD41, "cmd_dump",
    title="*Dump command handler",
    description="Opens the file via open_file_for_read, allocates a\n"
    "21-byte buffer on the stack, and parses the address\n"
    "range via init_dump_buffer. Loops reading 16 bytes\n"
    "per line, printing each as a 4-byte hex address,\n"
    "16 hex bytes with spaces, and a 16-character ASCII\n"
    "column (non-printable chars shown as '.'). Prints\n"
    "a column header at every 256-byte boundary.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8B23, "cmd_net_fs",
    title="Select Econet network filing system",
    description="Computes a checksum over the first &77 bytes of\n"
    "the workspace page and verifies against the stored\n"
    "value; raises an error on mismatch. On success,\n"
    "notifies the OS via FSCV reason 6, copies the FS\n"
    "context block from the receive block to &0DFA,\n"
    "installs 7 filing system vectors (FILEV etc.)\n"
    "from fs_vector_table, initialises the ADLC and\n"
    "extended vectors, sets up the channel table, and\n"
    "copies the workspace page to &1000 as a shadow.\n"
    "Sets bit 7 of &0D6C to mark the FS as selected,\n"
    "then issues service call 15.",
    on_entry={"y": "command line offset in text pointer "
              "(unused for *NET FS but supplied by star-cmd dispatch)"},
    on_exit={"a, x, y": "clobbered",
             "&0D6C bit 7": "set (FS active)",
             "behaviour": "raises 'Net checksum' via error_inline_log on "
             "workspace checksum mismatch"})
subroutine(0xB581, "cmd_pollps",
    title="*Pollps command handler",
    description="Initialises the spool drive, copies the PS name to\n"
    "the TX buffer, and parses an optional station number\n"
    "or PS name argument. Sends a poll request, then\n"
    "prints the server address and name. Iterates through\n"
    "PS slots, displaying each station's status as\n"
    "'ready', 'busy' (with client station), or 'jammed'.\n"
    "Marks processed slots with &3F.",
    on_entry={"y": "command line offset in text pointer"})
# UNMAPPED: subroutine(0xB99D, "cmd_print",
# UNMAPPED:     title="*Print command handler",
# UNMAPPED:     description="Sets V flag (distinguishing from *Type which clears V),\n"
# UNMAPPED:     "then opens the file for reading. Loops reading bytes\n"
# UNMAPPED:     "via OSBGET, checking for escape between each. In type\n"
# UNMAPPED:     "mode (V clear), normalises CR/LF pairs to single\n"
# UNMAPPED:     "newlines by tracking the previous character. In print\n"
# UNMAPPED:     "mode (V set), outputs all bytes raw via OSWRCH. Closes\n"
# UNMAPPED:     "the file and prints a final newline on EOF.",
# UNMAPPED:     on_entry={"y": "command line offset in text pointer"})
# UNMAPPED: subroutine(0xB30C, "cmd_prot",
# UNMAPPED:     title="*Prot command handler",
# UNMAPPED:     description="With no arguments, sets all protection bits (&FF).\n"
# UNMAPPED:     "Otherwise parses attribute keywords via match_fs_cmd\n"
# UNMAPPED:     "with table offset &D3, accumulating bits via ORA.\n"
# UNMAPPED:     "Stores the final protection mask in ws_0d68 and\n"
# UNMAPPED:     "ws_0d69.",
# UNMAPPED:     on_entry={"y": "command line offset in text pointer"})
subroutine(0xB3AC, "cmd_ps",
    title="*PS command handler",
    description="Checks the printer server availability flag; raises\n"
    "'Printer busy' if unavailable. Initialises the spool\n"
    "drive and buffer pointer, then dispatches on argument\n"
    "type: no argument branches to no_ps_name_given, a\n"
    "leading digit branches to save_ps_cmd_ptr as a station\n"
    "number, otherwise parses a named PS address via\n"
    "load_ps_server_addr and parse_fs_ps_args.",
    on_entry={"y": "command line offset in text pointer"})
# UNMAPPED: subroutine(0xB99A, "cmd_type",
# UNMAPPED:     title="*Type command handler",
# UNMAPPED:     description="Clears V and branches to the shared open_and_read_file\n"
# UNMAPPED:     "entry in cmd_print. The V-clear state selects line-\n"
# UNMAPPED:     "ending normalisation mode: CR, LF, CR+LF, and LF+CR\n"
# UNMAPPED:     "are all treated as a single newline. Designed for\n"
# UNMAPPED:     "displaying text files.",
# UNMAPPED:     on_entry={"y": "command line offset in text pointer"})
# UNMAPPED: subroutine(0xB33D, "cmd_unprot",
# UNMAPPED:     title="*Unprot command handler",
# UNMAPPED:     description="With no arguments, clears all protection bits (EOR\n"
# UNMAPPED:     "yields 0). Otherwise parses attribute keywords, clearing\n"
# UNMAPPED:     "bits via AND with the complement. Shares the protection\n"
# UNMAPPED:     "mask storage path with cmd_prot. Falls through to\n"
# UNMAPPED:     "cmd_wipe.",
# UNMAPPED:     on_entry={"y": "command line offset in text pointer"})
subroutine(0x8AEA, "cmd_roff",
    title="*ROFF command handler",
    description="Disables remote operation by clearing the flag at\n"
    "offset 0 in the receive block. If remote operation\n"
    "was active, re-enables the keyboard via OSBYTE &C9\n"
    "(with X=0, Y=0) and calls tx_econet_abort with\n"
    "A=&0A to reinitialise the workspace area. Falls\n"
    "through to scan_remote_keys which clears svc_state\n"
    "and nfs_workspace.",
    on_entry={"y": "command line offset (unused -- *ROFF takes no args)"},
    on_exit={"a, x, y": "clobbered",
             "remote-op flag (RX block offset 0)": "cleared",
             "svc_state, nfs_workspace": "zeroed (via fall-through to "
             "scan_remote_keys / clear_svc_and_ws)"})

# Sub-table 2: NFS commands
entry(0x9425)   # *Access, *Delete, *Info, *Lib (shared entry)
entry(0x9776)   # *Bye
# UNMAPPED: entry(0xAD10)   # *Cdir
entry(0x9512)   # *Dir
entry(0xB103)   # *Ex
entry(0xA69A)   # *Flip
entry(0xA398)   # *FS
# UNMAPPED: entry(0x8D79)   # *I am
entry(0xB0F2)   # *Lcat
entry(0xB0F8)   # *Lex
entry(0x8DD5)   # *Pass
entry(0xB312)   # *Remove
entry(0x94C5)   # *Rename
entry(0xB6F3)   # *Wipe

label(0x9425, "cmd_fs_operation")
label(0x9776, "cmd_bye")
# UNMAPPED: label(0xAD10, "cmd_cdir")
label(0x9512, "cmd_dir")
label(0xB103, "cmd_ex")
label(0xA69A, "cmd_flip")
label(0xA398, "cmd_fs")
# UNMAPPED: label(0x8D79, "cmd_iam")
label(0xB0F2, "cmd_lcat")
label(0xB0F8, "cmd_lex")
label(0x8DD5, "cmd_pass")
# &B312 in 4.21_v1 is print_decimal_digit's body, not cmd_remove
# (4.18's cmd_remove was at a different address that didn't carry
# over). Real cmd_remove location pending fingerprint.
# UNMAPPED: label(0xB312, "cmd_remove")
label(0x94C5, "cmd_rename")
label(0xB6F3, "cmd_wipe")

subroutine(0x9425, "cmd_fs_operation",
    title="Shared *Access/*Delete/*Info/*Lib command handler",
    description="Copies the command name to the TX buffer, parses a\n"
    "quoted filename argument via parse_quoted_arg, and\n"
    "checks the access prefix. Validates the filename\n"
    "does not start with '&', then falls through to\n"
    "read_filename_char to copy remaining characters and\n"
    "send the request. Raises 'Bad file name' if a bare\n"
    "CR is found where a filename was expected.",
    on_entry={"y": "command line offset in text pointer",
              "x": "byte offset within cmd_table_fs identifying which "
              "of the four shared commands was matched (Access, Delete, "
              "Info, or Lib)"},
    on_exit={"behaviour": "completes via the FS reply path; raises "
             "'Bad file name' on malformed argument and returns A = reply "
             "status from the file server, or BRKs on FS-reported errors"})
subroutine(0x9776, "cmd_bye",
    title="*Bye command handler",
    description="Closes all open file control blocks via\n"
    "process_all_fcbs, shuts down any *SPOOL/*EXEC files\n"
    "with OSBYTE &77, and closes all network channels.\n"
    "Falls through to save_net_tx_cb with function code\n"
    "&17 to send the bye request to the file server.",
    on_entry={"&0E00, &0E01": "FS station/network "
              "(stays as the 'Bye' destination across handle teardown)"},
    on_exit={"behaviour":
             "tail-call into save_net_tx_cb with Y = &17 -- "
             "completes via the FS reply path and returns A = reply status, "
             "or never returns on FS-reported errors (BRK via error_inline)"})
# Located in 4.21_v1 at &B0A0 (was &AD10 in 4.18). Initial fingerprint
# hit &B09F but the byte there is the &60 RTS terminating the previous
# routine; cmd_cdir's TYA/PHA prologue starts at &B0A0. Reached via
# PHA/PHA/RTS dispatch from the star-command table — needs entry().
entry(0xB0A0)
subroutine(0xB0A0, "cmd_cdir",
    title="*CDir command handler",
    description="Parses an optional allocation size argument: if absent,\n"
    "defaults to index 2 (standard 19-entry directory, &200\n"
    "bytes); if present, parses the decimal value and searches\n"
    "a 26-entry threshold table to find the matching allocation\n"
    "size index. Parses the directory name via parse_filename_arg,\n"
    "copies it to the TX buffer, and sends FS command code &1B\n"
    "to create the directory.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x9512, "cmd_dir",
    title="*Dir command handler",
    description="Handles three argument syntaxes: a plain path\n"
    "(delegates to pass_send_cmd), '&' alone for the root\n"
    "directory, and '&N.dir' for cross-filesystem directory\n"
    "changes. The cross-FS form sends a file server\n"
    "selection command (code &12) to locate the target\n"
    "server, raising 'Not found' on failure, then sends\n"
    "the directory change (code 6) and calls\n"
    "find_fs_and_exit to update the active FS context.",
    on_entry={"y": "command line offset in text pointer"},
    on_exit={"behaviour": "completes via the FS reply; on the cross-FS "
             "path, may raise 'Not found' or update the active FS station "
             "to the targeted server before returning"})
subroutine(0xB103, "cmd_ex",
    title="*Ex command handler",
    description="Unified handler for *Ex, *LCat, and *LEx. Sets the\n"
    "library flag from carry (CLC for current, SEC for library).\n"
    "Configures column format: 1 entry per line for Ex\n"
    "(command 3), 3 per column for Cat (command &0B). Sends the\n"
    "examine request (code &12), then prints the directory\n"
    "header: title, cycle number, Owner/Public label, option\n"
    "name, Dir. and Lib. paths. Paginates through entries,\n"
    "printing each via ex_print_col_sep until the server\n"
    "returns zero entries.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xA69A, "cmd_flip",
    title="*Flip command handler",
    description="Exchanges the CSD and CSL (library) handles.\n"
    "Saves the current CSD handle (&0E03), loads the\n"
    "library handle (&0E04) into Y, and calls\n"
    "find_station_bit3 to install it as the new CSD.\n"
    "Restores the original CSD handle and falls through\n"
    "to flip_set_station_boot to install it as the new\n"
    "library. Useful when files to be LOADed are in the\n"
    "library and *DIR/*LIB would be inconvenient.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xA398, "cmd_fs",
    title="*FS command handler",
    description="Saves the current file server station address, then\n"
    "checks for a command-line argument. With no argument,\n"
    "falls through to print_current_fs to display the active\n"
    "server. With an argument, parses the station number via\n"
    "parse_fs_ps_args and issues OSWORD &13 (sub-function 1)\n"
    "to select the new file server.",
    on_entry={"y": "command line offset in text pointer"})
# Located in 4.21_v1 at &8D91 (was &8D79 in 4.18). The 4.18 prologue
# saved Y on the stack via TYA/PHA before doing OSBYTE &77; the 4.21
# version drops the save (caller-preserved Y, presumably). Reached
# via PHA/PHA/RTS dispatch — needs entry().
entry(0x8D91)
subroutine(0x8D91, "cmd_iam",
    title="*I AM command handler (file server logon)",
    description="Closes any *SPOOL/*EXEC files via OSBYTE &77,\n"
    "resets all file control blocks via\n"
    "process_all_fcbs, then parses the command line\n"
    "for an optional station number and file server\n"
    "address. If a station number is present, stores\n"
    "it and calls clear_if_station_match to validate.\n"
    "Copies the logon command template from\n"
    "cmd_table_nfs_iam into the transmit buffer and\n"
    "sends via copy_arg_validated. Falls through to\n"
    "cmd_pass for password entry.",
    on_entry={"y": "command line offset in text pointer"},
    on_exit={"behaviour": "falls through to cmd_pass which prompts for "
             "a password and completes the logon via save_net_tx_cb; "
             "may raise 'Bad station' on parse failure"})
subroutine(0xB0F2, "cmd_lcat",
    title="*LCat command handler",
    description="Sets the library flag by rotating SEC into bit 7 of\n"
    "l1071, then branches to cat_set_lib_flag inside cmd_ex\n"
    "to catalogue the library directory with three entries\n"
    "per column.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB0F8, "cmd_lex",
    title="*LEx command handler",
    description="Sets the library flag by rotating SEC into bit 7 of\n"
    "l1071, then branches to ex_set_lib_flag inside cmd_ex\n"
    "to examine the library directory with one entry per line.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8D02, "issue_svc_15",
    title="Issue OSBYTE 143 service 15 (vectors-claimed) request",
    description="Tail-call wrapper that loads X=&0F (service number 15) "
    "and tail-jumps to OSBYTE 143 (issue paged ROM service request), "
    "which broadcasts service 15 to all sideways ROMs. ANFS calls "
    "this from svc_2_private_workspace after claiming its workspace, "
    "to give other ROMs a chance to react.",
    on_entry={"a": "OSBYTE result is irrelevant -- this is fire-and-forget"})

subroutine(0x8E9A, "osbyte_a1",
    title="OSBYTE &A1 (read Master CMOS RAM byte)",
    description="Loads A=&A1 and tail-jumps to OSBYTE -- reads the "
    "Master 128 CMOS RAM byte indexed by X. Two callers: format_"
    "filename_field (&A0E3) and flip_set_station_boot (&A70D). The "
    "5 bytes A9 A1 4C F4 FF also serve as the leading slot of the "
    "vector-dispatch table that write_vector_entry reads via "
    "LDA c8e9a,Y -- a deliberate dual-use byte sequence.",
    on_entry={"x": "CMOS RAM byte index"},
    on_exit={"y": "CMOS byte read", "x": "preserved"})

subroutine(0x988F, "check_escape_and_classify",
    title="Acknowledge escape (if pressed) and classify reply",
    description="If escape_flag bit 7 is clear OR need_release_tube bit "
    "7 is clear (so AND result has bit 7 clear), returns immediately "
    "via return_1. Otherwise acknowledges escape via OSBYTE &7E "
    "(clears the escape condition and runs escape effects), loads "
    "A=6 (a synthesized 'Escape' error class), and tail-jumps to "
    "classify_reply_error to build the 'Escape' BRK error block.\n"
    "\n"
    "Two callers: cmd_pass (&8DEF) for password-entry escape, and "
    "send_net_packet (&9B48) for in-flight TX escape.",
    on_entry={},
    on_exit={"a": "preserved (return) or never returns (escape path)"})

subroutine(0x8DD5, "cmd_pass",
    title="*PASS command handler (change password)",
    description="Builds the FS command packet via copy_arg_to_buf_x0,\n"
    "then scans the reply buffer for a ':' separator\n"
    "indicating a password prompt. If found, reads\n"
    "characters from the keyboard without echo, handling\n"
    "Delete (&7F) for backspace and NAK (&15) to restart\n"
    "from the colon position. Sends the completed\n"
    "password to the file server via save_net_tx_cb and\n"
    "branches to send_cmd_and_dispatch for the reply.",
    on_entry={"y": "command line offset in text pointer "
              "(also the entry point for cmd_iam fall-through)"},
    on_exit={"behaviour": "completes via the FS reply path; raises "
             "'Escape' if the user aborts password entry"})
# UNMAPPED: subroutine(0xB312, "cmd_remove", ...)
# That address is print_decimal_digit's body in 4.21_v1, not cmd_remove.
# The actual *Remove handler lives at a yet-to-be-located address;
# fingerprinting deferred to a later session.

# 4.21 has TWO copies of the print-decimal pair: an OSASCI version at
# &B32A/&B338 (the LCS-mapped 4.18 carry-over with leading-zero
# suppression), and a no-spool variant at &B303/&B310 that uses
# print_char_no_spool instead so status output bypasses any open
# *SPOOL file. The no-spool variant has no leading-zero suppression.
subroutine(0xB303, "print_decimal_3dig_no_spool",
    title="Print 3-digit decimal via *SPOOL-bypassing print",
    description="As print_decimal_3dig (&B32A) but each digit is "
    "emitted via print_char_no_spool, which closes the *SPOOL "
    "handle around OSASCI so the digit doesn't appear in any "
    "active capture. Always prints all three digits (no "
    "leading-zero suppression).",
    on_entry={"a": "value 0-255"})
subroutine(0xB310, "print_decimal_digit_no_spool",
    title="Print one decimal digit, *SPOOL-bypassing",
    description="As print_decimal_digit (&B338) but emits via "
    "print_char_no_spool. fs_error_ptr is used as scratch "
    "storage for the divisor and is preserved across the print.",
    on_entry={"a": "divisor (100, 10, or 1)",
              "y": "value to divide"},
    on_exit={"y": "remainder after division"})
subroutine(0x94C5, "cmd_rename",
    title="*Rename command handler",
    description="Parses two space-separated filenames from the\n"
    "command line, each with its own access prefix.\n"
    "Sets the owner-only access mask before parsing each\n"
    "name. Validates that both names resolve to the same\n"
    "file server by comparing the FS options word —\n"
    "raises 'Bad rename' if they differ. Falls through\n"
    "to read_filename_char to copy the second filename\n"
    "into the TX buffer and send the request.",
    on_entry={"y": "command line offset in text pointer"},
    on_exit={"behaviour": "completes via the FS reply path; raises "
             "'Bad rename' if the two filenames target different file "
             "servers, or 'Bad file name' on parse error"})
subroutine(0xB6F3, "cmd_wipe",
    title="*Wipe command handler",
    description="Masks owner access, parses a wildcard filename, and\n"
    "loops sending examine requests to the file server.\n"
    "Skips locked files and non-empty directories. Shows\n"
    "each filename with a '(Y/N/?) ' prompt — '?' shows\n"
    "full file info with a '(Y/N) ' reprompt, 'Y' builds\n"
    "the delete command in the TX buffer. Falls through to\n"
    "flush_and_read_char on completion.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB7CB, "prompt_yn",
    title="Print Y/N prompt and read user response",
    description="Prints \'Y/N) \' via inline string, flushes\n"
    "the input buffer, and reads a single character\n"
    "from the keyboard.",
    on_exit={"A": "character read from keyboard (after the 'Y/N) ' prompt)",
             "behaviour": "may raise 'Escape' via flush_and_read_char on "
             "escape press; otherwise returns the keystroke unchanged"})

# Sub-table 3: help topic handlers
entry(0x8BC4)   # *Net (second variant)
entry(0x8BC0)   # *Utils

label(0x8BC4, "help_net")
label(0x8BC0, "help_utils")

subroutine(0x8BC4, "help_net",
    title="*HELP NET topic handler",
    description="Sets X to &4A (the NFS command sub-table offset)\n"
    "and falls through to print_cmd_table to display\n"
    "the NFS command list with version header.")
subroutine(0x8BC0, "help_utils",
    title="*HELP UTILS topic handler",
    description="Sets X=0 to select the utility command sub-table\n"
    "and branches to print_cmd_table to display the\n"
    "command list. Prints the version header followed\n"
    "by all utility commands.")


# ============================================================
# Additional code entry points (undecoded blocks)
# ============================================================
# These blocks follow decoded code (usually after an RTS or inline
# data) and start with valid 6502 opcodes. Adding entry points
# causes py8dis to trace execution from these addresses.

entry(0x8C29)   # After svc_9_help return
entry(0x93F7)   # After cmd_fs_operation utility code
entry(0x9C22)   # Referenced from FS option handler table
entry(0x9EAB)   # Large undecoded block (266 bytes)
entry(0x9FC2)   # After &9CB8 block
entry(0xA14C)   # Large undecoded block (157 bytes)
entry(0xA28A)   # Large undecoded block (203 bytes)
entry(0xAC47)   # Large undecoded block (220 bytes)
entry(0xAD64)   # After &A9CF code
entry(0xAE6F)   # After &AACF data table
entry(0xBB68)   # File operation handler
# entry(0xB865) removed — was mid-instruction; &B865 is byte 2 of
# LDA #&C1 at &B864, part of the inline error call to error_inline_log.

# TX done dispatch table (5 bytes) and event handler (8 bytes)
entry(0x8549)   # tx_done_econet_event: TX operation type &84 handler
# UNMAPPED: for i in range(5):
# UNMAPPED:     byte(0x853E + i)

# Use symbolic label expressions for PHA/PHA/RTS dispatch lo bytes.
# UNMAPPED: expr(0x853E, "<(tx_done_jsr-1)")
# UNMAPPED: expr(0x853F, "<(tx_done_econet_event-1)")
# UNMAPPED: expr(0x8540, "<(tx_done_os_proc-1)")
# UNMAPPED: expr(0x8541, "<(tx_done_halt-1)")
# UNMAPPED: expr(0x8542, "<(tx_done_continue-1)")

# TX ctrl dispatch table (8 bytes) and machine type handler (4 bytes)
# UNMAPPED: entry(0x8689)   # tx_ctrl_machine_type: ctrl &88 handler
# UNMAPPED: for i in range(8):
# UNMAPPED:     byte(0x8681 + i)

# Use symbolic label expressions for PHA/PHA/RTS dispatch lo bytes.
# UNMAPPED: expr(0x8681, "<(tx_ctrl_peek-1)")
# UNMAPPED: expr(0x8682, "<(tx_ctrl_poke-1)")
# UNMAPPED: expr(0x8683, "<(proc_op_status2-1)")
# UNMAPPED: expr(0x8684, "<(proc_op_status2-1)")
# UNMAPPED: expr(0x8685, "<(proc_op_status2-1)")
# UNMAPPED: expr(0x8686, "<(tx_ctrl_exit-1)")
# UNMAPPED: expr(0x8687, "<(tx_ctrl_exit-1)")
# UNMAPPED: expr(0x8688, "<(tx_ctrl_machine_type-1)")

# Dead data between tx_store_result and tx_calc_transfer (16 bytes)
# Unreferenced and unreachable — force to individual data bytes.
for i in range(16):
    byte(0x88F0 + i)

# Dead data between rom_set_nmi_vector RTI and svc_dispatch_lo (3 bytes)
# UNMAPPED: for i in range(3):
# UNMAPPED:     byte(0x89C7 + i)

# Smaller undecoded blocks with valid first opcodes
entry(0x84BE)   # After dispatch table data
entry(0x84CE)   # After &84BB block
entry(0x88F0)   # 16 bytes after NMI code
entry(0xA910)   # 118-byte undecoded block
entry(0xA985)   # 552-byte undecoded block (largest remaining)
entry(0xACFC)   # 68-byte undecoded block
# entry(0xAA9F) removed — classified as data via byte() declarations
entry(0xBBE7)   # 21-byte file handler block
# Removed in 4.18: entry(0xB42F) — dead code removed

# Page 5 relocated code — ANFS-specific entry points
# Runtime addresses for undecoded blocks in page 5 source (&BC90)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0542)   # tube_osfind (ANFS variant)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x0564)   # read_osargs_params (ANFS variant)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x05AB)   # argsw (ANFS variant)
# UNMAPPED (dead range &0016-&0057 / &0400-&06FF): entry(0x05D3)   # read_osgbpb_ctrl_blk (ANFS variant)


# ============================================================
# Data tables in main ROM
# ============================================================

# ============================================================
# FS vector dispatch and handler addresses (&8E61)
# ============================================================
subroutine(0x8EA7, "fs_vector_table",
    title="FS vector dispatch and handler addresses (34 bytes)",
    description="""\
Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by loop_set_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the extended vector table.

Bytes 14-33: handler address pairs read by write_vector_entry.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (write_vector_entry writes the current ROM
bank number instead). The last entry (FSCV) has no padding
byte.""")

# Part 1: extended vector dispatch addresses (7 x 2 bytes)
# Each value is &FF1B, &FF1E, &FF21, ... &FF2D — the MOS extended
# vector dispatch entries. These get installed at &0212-&021F by
# loop_set_vectors and route filing-system OS calls into the per-ROM
# extended vector table at &0D9F+, where ANFS plants the real handlers.
for i, name in enumerate(["FILEV", "ARGSV", "BGETV", "BPUTV",
                           "GBPBV", "FINDV", "FSCV"]):
    addr = 0x8EA7 + i * 2
    word(addr)
    comment(addr, f"{name} dispatch (&FF{0x1B + i * 3:02X})",
            inline=True)

# Part 2: handler address entries (7 x {lo, hi, pad})
# write_vector_entry (&904F) reads bytes from c8e9a+Y starting at Y=&1B,
# which means the table starts at &8E9A+&1B = &8EB5 in 4.21_v1.
# (4.18 had this table at &8E6F; the +&46 shift comes from the longer
# ROM title string and earlier code insertions.)
handler_names = [
    ("FILEV",  0x9C22),
    ("ARGSV",  0x9EAB),
    ("BGETV",  0xBB68),
    ("BPUTV",  0xBBE7),
    ("GBPBV",  0xA14C),
    ("FINDV",  0xA02F),
    ("FSCV",   0x8E4B),
]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x8EB5 + i * 3
    word(base_addr)
    comment(base_addr, f"{name} handler (&{handler_addr:04X})", inline=True)
    if i < 6:  # pad byte for all but last entry
        byte(base_addr + 2, 1)
        comment(base_addr + 2, "(ROM bank — not read)", inline=True)

# Printer server template data: "PRINT " + &01 &00 (8 bytes)
# Read by copy_ps_data via indexed addressing from ps_template_base.
label(0x8E9F, "ps_template_data")
# UNMAPPED: byte(0x8E5F)
# UNMAPPED: byte(0x8E60)

# NETV handler address pair at &8E8A (read by write_vector_entry)
# UNMAPPED: label(0x8E8A, "netv_handler_addr")
label(0xACFC, "netv_handler")
# UNMAPPED: word(0x8E8A)
# UNMAPPED: expr(0x8E8A, "netv_handler")

# Command syntax help strings (&900D-&910C)
label(0x90F7, "syntax_strings")

# Error message table (&97B9)
# UNMAPPED: label(0x97B9, "error_msg_table")
label(0x9AB3, "msg_net_error")
label(0x9ABE, "msg_station")
# UNMAPPED: label(0x97DA, "msg_no_clock")
label(0x9AD1, "msg_escape")
label(0x9AD9, "msg_bad_option")
# UNMAPPED: label(0x97F8, "msg_no_reply")
# UNMAPPED: label(0x980F, "msg_not_listening")
label(0x9B0B, "msg_on_channel")
label(0x9B17, "msg_not_present")
# Split error number and null terminator bytes
# UNMAPPED: byte(0x97B9)   # error &A0
# UNMAPPED: byte(0x97DA)   # null
byte(0x9AC8)   # error &A3
byte(0x9AD0)   # null
byte(0x9AD1)   # error &11
# UNMAPPED: byte(0x97EB)   # null
byte(0x9AD9)   # error &CB
# UNMAPPED: byte(0x97F8)   # null
byte(0x9AE6)   # error &A5
# UNMAPPED: byte(0x980E)   # null
byte(0x9B0A)   # null
byte(0x9B16)   # null
# UNMAPPED: byte(0x9836)   # null

# Credits string — force each CR (&0D) onto its own line and
# ensure "nn" (end of "J Dunn") displays as equs not equb.
# UNMAPPED: label(0x8CA3, "version_string")
# UNMAPPED: label(0x8D39, "credits_string")
byte(0x8D45)
comment(0x8D45, "CR", inline=True)
byte(0x8D5E)
comment(0x8D5E, "CR", inline=True)
# UNMAPPED: byte(0x8D5C)
# UNMAPPED: comment(0x8D5C, "CR", inline=True)
string(0x8D6E, 2)
# UNMAPPED: byte(0x8D63)
# UNMAPPED: comment(0x8D63, "CR", inline=True)
# UNMAPPED: byte(0x8D6F)
# UNMAPPED: comment(0x8D6F, "CR", inline=True)
byte(0x8D84)
comment(0x8D84, "CR", inline=True)
# UNMAPPED: byte(0x8D78)
# UNMAPPED: comment(0x8D78, "String terminator", inline=True)

# Boot command strings
label(0xA740, "boot_load_cmd")
# UNMAPPED: label(0xA3D7, "boot_exec_cmd")


# ============================================================
# Additional ROM subroutines (from code analysis)
# ============================================================

# Subroutine at &8E33: PHA/PHA/RTS dispatch via svc_dispatch tables.
# On entry: X=base index, Y=offset. Dispatches to table[X+Y+1].
subroutine(0x8E61, "svc_dispatch",
    title="PHA/PHA/RTS table dispatch",
    description="Computes a target index by incrementing X and\n"
    "decrementing Y until Y goes negative, effectively\n"
    "calculating X+Y+1. Pushes the target address\n"
    "(high then low byte) from svc_dispatch_lo/hi\n"
    "tables onto the stack, loads fs_options into X,\n"
    "then returns via RTS to dispatch to the target\n"
    "subroutine. Used for all service dispatch, FS\n"
    "command execution, and OSBYTE handler routing.",
    on_entry={"x": "base dispatch index",
              "y": "additional offset"},
    on_exit={"x": "fs_options value"})
label(0x8E61, "svc_dispatch")

# sub_c8a97: read byte from paged ROM via OSRDSC
# UNMAPPED: subroutine(0x8AA0, "read_paged_rom",
# UNMAPPED:     title="Read next byte from paged ROM via OSRDSC",
# UNMAPPED:     description="Increments the read pointer at osrdsc_ptr (&F6)\n"
# UNMAPPED:     "first, then calls OSRDSC (&FFB9) with the ROM\n"
# UNMAPPED:     "number from error_block (&0100) in Y. Called\n"
# UNMAPPED:     "three times by service_handler during ROM\n"
# UNMAPPED:     "identification to read the copyright string and\n"
# UNMAPPED:     "ROM type byte.",
# UNMAPPED:     on_exit={"a": "byte read from ROM"})
# UNMAPPED: label(0x8AA0, "read_paged_rom")

# Located in 4.21_v1 at &8EC9 (was &8E83 in 4.18). Single-instruction
# `LDX #0` that falls through to osbyte_yff at &8ECB. Already
# classified as code (sub_c8ec9 with 3 callers from &805D, &9041,
# &99FD).
subroutine(0x8EC9, "osbyte_x0",
    title="OSBYTE wrapper with X=0, Y=&FF",
    description="Sets X=0 and falls through to osbyte_yff to also\n"
    "set Y=&FF. Provides a single call to execute\n"
    "OSBYTE with A as the function code. Used by\n"
    "adlc_init, init_adlc_and_vectors, and Econet\n"
    "OSBYTE handling.",
    on_entry={"a": "OSBYTE function code"},
    on_exit={"x": "0", "y": "&FF"})
subroutine(0x8ECB, "osbyte_yff",
    title="OSBYTE wrapper with Y=&FF",
    description="Sets Y=&FF and JMPs to the MOS OSBYTE entry\n"
    "point. X must already be set by the caller. The\n"
    "osbyte_x0 entry point falls through to here after\n"
    "setting X=0.",
    on_entry={"a": "OSBYTE function code",
              "x": "OSBYTE X parameter"},
    on_exit={"y": "&FF"})
label(0x8EC9, "osbyte_x0")
label(0x8ECB, "osbyte_yff")


# ============================================================
# Inline string subroutines — descriptions and comments
# ============================================================
# Label and code-tracing hooks created by hook_subroutine() above.

subroutine(0x9261, "print_inline",
    title="Print inline string, high-bit terminated",
    description="""\
Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. Common terminators are
&EA (NOP) for fall-through and &B8 (CLV) followed by BVC for an
unconditional forward branch.""",
    on_entry={"stack": "JSR return address points one byte BEFORE the "
              "inline string (the routine increments past it)",
              "inline string": "ASCII bytes immediately following the JSR, "
              "terminated by a byte with bit 7 set (which is the NEXT opcode)"},
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)",
             "x": "corrupted (by OSASCI)",
             "y": "0",
             "control flow": "RTS does NOT return to JSR; instead a JMP "
             "lands on the terminator byte's address as the next instruction"})

subroutine(0x928A, "print_inline_no_spool",
    title="Print inline string, high-bit terminated, *SPOOL-bypassing",
    description="""\
As print_inline (&9261), but each character is emitted via
print_char_no_spool instead of OSASCI directly, so the printed text
does not appear in any active *SPOOL capture. Used by status output
that should not be saved to a spool file (e.g. *Wipe '(Y/N) ' prompts,
*Ex column separators, the 'Bad ROM' service-handler message via the
recv_and_process_reply 'Data Lost' warning, and inline-string
arguments inside cmd_ex's directory listing).

Six callers: &981A (recv_and_process_reply), &B158/&B162 (cmd_ex),
&B2F0 (ex_print_col_sep), &B75E (cmd_wipe), &B7CB (prompt_yn).""",
    on_entry={"stack": "JSR return address points just before the "
              "inline string",
              "inline string": "ASCII bytes immediately following the JSR, "
              "bit-7 terminated"},
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)",
             "x": "corrupted (by print_char_no_spool)",
             "y": "0",
             "control flow": "JMPs onto the terminator byte; RTS does NOT "
             "return to caller's JSR site"})

comment(0x9261, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x9264, "Pop return address (high)", inline=True)
comment(0x9269, "Advance pointer to next character", inline=True)
comment(0x926F, "Load next byte from inline string", inline=True)
comment(0x9271, "Bit 7 set? Done — this byte is the next opcode", inline=True)
comment(0x9279, "Reload character (pointer may have been clobbered)", inline=True)
comment(0x927B, "Print character via OSASCI", inline=True)
comment(0x9287, "Jump to address of high-bit byte (resumes code)", inline=True)

subroutine(0x99C3, "error_inline",
    title="Generate BRK error from inline string",
    description="""\
Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""",
    on_entry={"a": "error number (stored in error block at &0101)",
              "stack": "JSR return address points just before the "
              "null-terminated error message text",
              "inline string": "NUL-terminated ASCII immediately following "
              "the JSR site"},
    on_exit={"behaviour": "DOES NOT RETURN -- the routine builds the "
             "MOS error block at &0100..&01FE and triggers the error "
             "via JMP error_block, which transfers control to BRKV"})

comment(0x99C3, "Save error number in Y", inline=True)
comment(0x99C4, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x99C7, "Pop return address (high)", inline=True)

subroutine(0x99C0, "error_inline_log",
    title="Generate BRK error from inline string (with logging)",
    description="""\
Like error_inline, but first conditionally logs the error code to
workspace via sub_c95fb before building the error block.""",
    on_entry={"a": "error number",
              "stack": "JSR return address points just before the "
              "null-terminated error message text"},
    on_exit={"&0E09": "= A (logged when fs_flags bit 7 is set)",
             "behaviour": "DOES NOT RETURN -- triggers BRK via "
             "error_inline / error_block"})

comment(0x99C0, "Conditionally log error code to workspace", inline=True)

subroutine(0x99A7, "error_bad_inline",
    title="Generate 'Bad ...' BRK error from inline string",
    description="""\
Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""",
    on_entry={"a": "error number",
              "stack": "JSR return address points just before the "
              "null-terminated error suffix (the 'Bad ' prefix is "
              "prepended internally from a lookup table)",
              "inline string": "NUL-terminated suffix (e.g. 'station')"},
    on_exit={"behaviour": "DOES NOT RETURN -- builds the 'Bad <suffix>' "
             "error message in the MOS error block and triggers BRK via "
             "error_inline_log / error_block"})

comment(0x99A7, "Conditionally log error code to workspace", inline=True)
comment(0x99AA, "Save error number in Y", inline=True)
comment(0x99AB, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x99AC, "Store return address low", inline=True)
comment(0x99AE, "Pop return address (high)", inline=True)
comment(0x99AF, "Store return address high", inline=True)
comment(0x99B1, "X=0: start of prefix string", inline=True)
comment(0x99B3, "Copy 'Bad ' prefix from lookup table", inline=True)
comment(0x99B4, "Get next prefix character", inline=True)
comment(0x99B7, "Store in error text buffer", inline=True)
comment(0x99BA, "Is it space (end of 'Bad ')?", inline=True)
comment(0x99BC, "No: copy next prefix character", inline=True)
comment(0x99CC, "Store error number in error block", inline=True)
comment(0x99D3, "Zero the BRK byte at &0100", inline=True)
comment(0x99D6, "Copy inline string into error block", inline=True)
comment(0x99D8, "Read next byte from inline string", inline=True)
comment(0x99DD, "Loop until null terminator", inline=True)
comment(0x99DF, "Read receive attribute byte", inline=True)

# "Bad " prefix table
# UNMAPPED: label(0x96B4, "bad_prefix")


# ============================================================
# FS command inline comments (Phase 4)
# ============================================================

# cmd_cdir (&ACFE) — *CDir: create directory
# UNMAPPED: comment(0xAD10, "Save command line offset", inline=True)
# UNMAPPED: comment(0xAD11, "Push onto stack", inline=True)
comment(0xB0A3, "Set owner-only access mask", inline=True)
comment(0xB0A6, "Skip to optional size argument", inline=True)
comment(0xB0A9, "End of line?", inline=True)
comment(0xB0AB, "No: parse size argument", inline=True)
comment(0xB0AD, "Default allocation size index = 2", inline=True)
comment(0xB0B1, "A=&FF: mark as decimal parse", inline=True)
comment(0xB0B3, "Store decimal parse flag", inline=True)
comment(0xB0B5, "Parse numeric size argument", inline=True)
comment(0xB0B8, "X=&1B: top of 26-entry size table", inline=True)
comment(0xB0BA, "Try next lower index", inline=True)
comment(0xB0BB, "Compare size with threshold", inline=True)
comment(0xB0BE, "A < threshold: keep searching", inline=True)
comment(0xB0C0, "Store allocation size index", inline=True)
comment(0xB0C3, "Restore command line offset", inline=True)
comment(0xB0C4, "Transfer to Y", inline=True)
comment(0xB0C5, "Save text pointer for filename parse", inline=True)
comment(0xB0C8, "Parse directory name argument", inline=True)
comment(0xB0CB, "X=1: one argument to copy", inline=True)
comment(0xB0CD, "Copy directory name to TX buffer", inline=True)
comment(0xB0D0, "Y=&1B: *CDir FS command code", inline=True)
comment(0xB0D2, "Send command to file server", inline=True)

# cdir_alloc_size_table (&AD32): *CDir allocation size thresholds.
# Table base is at cdir_dispatch_col+2 (overlapping the JMP operand high
# byte at &AD2F). The search loop (LDX #&1B / DEX / CMP table,X /
# BCC) scans indices 26 down to 0; index 0 reads &94 from the JMP
# but is unreachable because index 1 (threshold &00) always matches.
# Result X (1-26) is the allocation size class sent to the FS.
comment(0xB0D5, "*CDir allocation size threshold table\n"
    "\n"
    "26 thresholds dividing 0-255 into size classes.\n"
    "Table base (cdir_dispatch_col+2) overlaps with\n"
    "the JMP high byte (entry 0, never reached). Searched\n"
    "from index 26 down to 0; the result index (1-26)\n"
    "is stored as the directory allocation size class.\n"
    "Default when no size argument given: index 2.")
comment(0xB0D5, "Index 1: threshold 0 (catch-all)", inline=True)
comment(0xB0D6, "Index 2: threshold 10 (default)", inline=True)
comment(0xB0D7, "Index 3: threshold 20", inline=True)
# UNMAPPED: comment(0xAD47, "Index 4: threshold 29", inline=True)
# UNMAPPED: comment(0xAD48, "Index 5: threshold 39", inline=True)
# UNMAPPED: comment(0xAD49, "Index 6: threshold 49", inline=True)
# UNMAPPED: comment(0xAD4A, "Index 7: threshold 59", inline=True)
comment(0xB0DC, "Index 8: threshold 69", inline=True)
# UNMAPPED: comment(0xAD4C, "Index 9: threshold 79", inline=True)
comment(0xB0DE, "Index 10: threshold 88", inline=True)
comment(0xB0DF, "Index 11: threshold 98", inline=True)
comment(0xB0E0, "Index 12: threshold 108", inline=True)
# UNMAPPED: comment(0xAD50, "Index 13: threshold 118", inline=True)
# UNMAPPED: comment(0xAD51, "Index 14: threshold 128", inline=True)
comment(0xB0E3, "Index 15: threshold 138", inline=True)
comment(0xB0E4, "Index 16: threshold 148", inline=True)
# UNMAPPED: comment(0xAD54, "Index 17: threshold 157", inline=True)
comment(0xB0E6, "Index 18: threshold 167", inline=True)
comment(0xB0E7, "Index 19: threshold 177", inline=True)
# UNMAPPED: comment(0xAD57, "Index 20: threshold 187", inline=True)
comment(0xB0E9, "Index 21: threshold 197", inline=True)
# UNMAPPED: comment(0xAD59, "Index 22: threshold 207", inline=True)
comment(0xB0EB, "Index 23: threshold 216", inline=True)
comment(0xB0EC, "Index 24: threshold 226", inline=True)
comment(0xB0ED, "Index 25: threshold 236", inline=True)
# UNMAPPED: comment(0xAD5D, "Index 26: threshold 246", inline=True)
# UNMAPPED: comment(0xAD5E, "Unused (index 27, never accessed)", inline=True)

# cmd_lcat (&AD4D) — *LCat: library catalogue
comment(0xB0F2, "Rotate carry into lib flag bit 7", inline=True)
comment(0xB0F5, "Set carry (= library directory)", inline=True)

# cmd_lex (&AD53) — *LEx: library examine
comment(0xB0F8, "Rotate carry into lib flag bit 7", inline=True)
comment(0xB0FB, "Set carry (= library directory)", inline=True)

# cmd_prot (&B2F0) — *Prot: set file protection
# UNMAPPED: comment(0xB30C, "Get next char from command line", inline=True)
# UNMAPPED: comment(0xB30E, "Compare with CR (end of line)", inline=True)
comment(0xB6D4, "Not CR: attribute keywords follow", inline=True)
comment(0xB6D6, "A=&FF: protect all attributes", inline=True)
# UNMAPPED: comment(0xB316, "Load current protection mask", inline=True)
# UNMAPPED: comment(0xB319, "Save as starting value", inline=True)
comment(0xB6EE, "X=&D3: attribute keyword table offset", inline=True)
# UNMAPPED: comment(0xB31C, "Get next char from command line", inline=True)
# UNMAPPED: comment(0xB31E, "Save for end-of-args check", inline=True)
# UNMAPPED: comment(0xB320, "Match attribute keyword in table", inline=True)
# UNMAPPED: comment(0xB323, "No match: check if end of arguments", inline=True)
# UNMAPPED: comment(0xB325, "Retrieve accumulated mask", inline=True)
# UNMAPPED: comment(0xB326, "OR in attribute bit for keyword", inline=True)
# UNMAPPED: comment(0xB329, "Save updated mask", inline=True)
# UNMAPPED: comment(0xB32A, "Always non-zero after ORA: loop", inline=True)
# UNMAPPED: comment(0xB32C, "Get the unmatched character", inline=True)
# UNMAPPED: comment(0xB32E, "Is it CR?", inline=True)
# UNMAPPED: comment(0xB330, "Yes: arguments ended correctly", inline=True)
comment(0xB6F0, "No: invalid attribute keyword", inline=True)
# UNMAPPED: comment(0xB335, "Retrieve final protection mask", inline=True)
# UNMAPPED: comment(0xB336, "Store protection mask", inline=True)
# UNMAPPED: comment(0xB339, "Store protection mask copy", inline=True)
# UNMAPPED: comment(0xB33C, "Return", inline=True)

# cmd_unprot (&B321) — *Unprot: remove file protection
# UNMAPPED: comment(0xB33D, "Get next char from command line", inline=True)
# UNMAPPED: comment(0xB33F, "Compare with CR (end of line)", inline=True)
# UNMAPPED: comment(0xB341, "No args: A=0 clears all protection", inline=True)
# UNMAPPED: comment(0xB343, "Load current protection mask", inline=True)
# UNMAPPED: comment(0xB346, "Save as starting value", inline=True)
# UNMAPPED: comment(0xB347, "X=&D3: attribute keyword table offset", inline=True)
# UNMAPPED: comment(0xB349, "Get next char from command line", inline=True)
# UNMAPPED: comment(0xB34B, "Save for end-of-args check", inline=True)
# UNMAPPED: comment(0xB34D, "Match attribute keyword in table", inline=True)
# UNMAPPED: comment(0xB350, "No match: check if end of arguments", inline=True)
# UNMAPPED: comment(0xB352, "Retrieve accumulated mask", inline=True)
# UNMAPPED: comment(0xB353, "AND to clear matched attribute bit", inline=True)
# UNMAPPED: comment(0xB356, "Save updated mask", inline=True)

# cmd_fs_operation (&92D2) — shared handler for *Access, *Delete, *Info, *Lib
comment(0x9425, "Copy command name to TX buffer", inline=True)
# UNMAPPED: comment(0x92E9, "Save buffer position", inline=True)
# UNMAPPED: comment(0x92EA, "Push it", inline=True)
comment(0x9429, "Parse filename (handles quoting)", inline=True)
comment(0x942C, "Parse owner/public access prefix", inline=True)
# UNMAPPED: comment(0x92F1, "Restore buffer position", inline=True)
# UNMAPPED: comment(0x92F2, "Transfer to X", inline=True)
comment(0x9430, "Reject '&' character in filename", inline=True)
comment(0x9433, "End of line?", inline=True)
comment(0x9435, "No: copy filename chars to buffer", inline=True)
comment(0x9437, "Error number &CC", inline=True)
comment(0x9439, "Raise 'Bad file name' error", inline=True)
comment(0x9446, "Load first parsed character", inline=True)
comment(0x9449, "Is it '&'?", inline=True)
comment(0x944B, "Yes: invalid filename", inline=True)
comment(0x944D, "Return", inline=True)
comment(0x944E, "Reject '&' in current char", inline=True)
comment(0x9451, "Store character in TX buffer", inline=True)
comment(0x9454, "Advance buffer pointer", inline=True)
comment(0x9455, "End of line?", inline=True)
comment(0x9457, "Yes: send request to file server", inline=True)
comment(0x9459, "Strip BASIC token prefix byte", inline=True)
# UNMAPPED: comment(0x931F, "Continue reading filename chars", inline=True)
comment(0x945E, "Y=0: no extra dispatch offset", inline=True)
comment(0x9460, "Send command and dispatch reply", inline=True)
# UNMAPPED: comment(0x9327, "Save command line offset", inline=True)
# UNMAPPED: comment(0x9328, "Push it", inline=True)
comment(0x9464, "Scan backwards in command table", inline=True)
comment(0x9465, "Load table byte", inline=True)
comment(0x9468, "Bit 7 clear: keep scanning", inline=True)
comment(0x946A, "Point past flag byte to name start", inline=True)
comment(0x946B, "Y=0: TX buffer offset", inline=True)
comment(0x946D, "Load command name character", inline=True)
comment(0x9470, "Bit 7 set: end of name", inline=True)
comment(0x9472, "Store character in TX buffer", inline=True)
comment(0x9475, "Advance table pointer", inline=True)
comment(0x9476, "Advance buffer pointer", inline=True)
comment(0x9477, "Continue copying name", inline=True)
comment(0x9479, "Space separator", inline=True)
comment(0x947B, "Append space after command name", inline=True)
comment(0x947E, "Advance buffer pointer", inline=True)
comment(0x947F, "Transfer length to A", inline=True)
comment(0x9480, "And to X (buffer position)", inline=True)
# UNMAPPED: comment(0x9346, "Restore command line offset", inline=True)
# UNMAPPED: comment(0x9347, "Transfer to Y", inline=True)
comment(0x9482, "Return", inline=True)
comment(0x9483, "A=0: no quote mode", inline=True)
comment(0x9486, "Clear quote tracking flag", inline=True)
comment(0x9489, "Load char from command line", inline=True)
comment(0x948B, "Space?", inline=True)
comment(0x948D, "No: check for opening quote", inline=True)
comment(0x948F, "Skip leading space", inline=True)
comment(0x9490, "Continue skipping spaces", inline=True)
comment(0x9492, "Double-quote character?", inline=True)
comment(0x9494, "No: start reading filename", inline=True)
comment(0x9496, "Skip opening quote", inline=True)
comment(0x9497, "Toggle quote mode flag", inline=True)
comment(0x949A, "Store updated quote mode", inline=True)
comment(0x949D, "Load char from command line", inline=True)
comment(0x949F, "Double-quote?", inline=True)
comment(0x94A1, "No: store character as-is", inline=True)
comment(0x94A3, "Toggle quote mode", inline=True)
comment(0x94A6, "Store updated quote mode", inline=True)
comment(0x94A9, "Replace closing quote with space", inline=True)
comment(0x94AB, "Store character in parse buffer", inline=True)
comment(0x94AE, "Advance command line pointer", inline=True)
comment(0x94AF, "Advance buffer pointer", inline=True)
comment(0x94B0, "End of line?", inline=True)
comment(0x94B2, "No: continue parsing", inline=True)
comment(0x94B4, "Check quote balance flag", inline=True)
comment(0x94B7, "Balanced: return OK", inline=True)
comment(0x94B9, "Unbalanced: use BRK ptr for error", inline=True)
comment(0x94BB, "Raise 'Bad string' error", inline=True)

# cmd_rename (&9377) — *Rename: rename file on server
comment(0x94C5, "Copy 'Rename ' to TX buffer", inline=True)
# UNMAPPED: comment(0x938E, "Save buffer position", inline=True)
# UNMAPPED: comment(0x938F, "Push it", inline=True)
comment(0x94C9, "Set owner-only access mask", inline=True)
comment(0x94CC, "Parse first filename (quoted)", inline=True)
comment(0x94CF, "Parse access prefix", inline=True)
# UNMAPPED: comment(0x9399, "Restore buffer position", inline=True)
# UNMAPPED: comment(0x939A, "Transfer to X", inline=True)
comment(0x94D3, "Load next parsed character", inline=True)
comment(0x94D6, "End of line?", inline=True)
comment(0x94D8, "No: store character", inline=True)
comment(0x94DA, "Error number &B0", inline=True)
comment(0x94DC, "Raise 'Bad rename' error", inline=True)
comment(0x94E6, "Store character in TX buffer", inline=True)
comment(0x94E9, "Advance buffer pointer", inline=True)
comment(0x94EA, "Space (name separator)?", inline=True)
comment(0x94EC, "Yes: first name complete", inline=True)
comment(0x94EE, "Strip BASIC token prefix byte", inline=True)
# UNMAPPED: comment(0x93B9, "Continue copying first filename", inline=True)
comment(0x94F3, "Strip token from next char", inline=True)
comment(0x94F6, "Load next parsed character", inline=True)
comment(0x94F9, "Still a space?", inline=True)
comment(0x94FB, "Yes: skip multiple spaces", inline=True)
comment(0x94FD, "Save current FS options", inline=True)
comment(0x9500, "Push them", inline=True)
comment(0x9501, "Reset access mask for second name", inline=True)
# UNMAPPED: comment(0x93CD, "Save buffer position", inline=True)
# UNMAPPED: comment(0x93CE, "Push it", inline=True)
comment(0x9505, "Parse access prefix for second name", inline=True)
# UNMAPPED: comment(0x93D2, "Restore buffer position", inline=True)
# UNMAPPED: comment(0x93D3, "Transfer to X", inline=True)
comment(0x9509, "Restore original FS options", inline=True)
comment(0x950A, "Options changed (cross-FS)?", inline=True)
comment(0x950D, "Yes: error (can't rename across FS)", inline=True)
comment(0x950F, "Copy second filename and send", inline=True)

# cmd_dir (&93C9) — *Dir: set current directory
comment(0x9512, "Get first char of argument", inline=True)
comment(0x9514, "Is it '&' (FS selector prefix)?", inline=True)
comment(0x9516, "No: simple dir change", inline=True)
comment(0x9518, "Skip '&'", inline=True)
comment(0x9519, "Get char after '&'", inline=True)
comment(0x951B, "End of line?", inline=True)
comment(0x951D, "Yes: '&' alone (root directory)", inline=True)
comment(0x951F, "Space?", inline=True)
comment(0x9521, "No: check for '.' separator", inline=True)
comment(0x9523, "Y=&FF: pre-increment for loop", inline=True)
comment(0x9525, "Advance index", inline=True)
comment(0x9526, "Load char from command line", inline=True)
comment(0x9528, "Copy to TX buffer", inline=True)
comment(0x952B, "Is it '&' (end of FS path)?", inline=True)
comment(0x952D, "No: keep copying", inline=True)
comment(0x952F, "Replace '&' with CR terminator", inline=True)
comment(0x9531, "Store CR in buffer", inline=True)
comment(0x9534, "Point past CR", inline=True)
comment(0x9535, "Transfer length to A", inline=True)
comment(0x9536, "And to X (byte count)", inline=True)
comment(0x9537, "Send directory request to server", inline=True)
comment(0x953A, "Is char after '&' a dot?", inline=True)
comment(0x953C, "Yes: &FS.dir format", inline=True)
comment(0x953E, "No: invalid syntax", inline=True)
comment(0x9541, "Skip '.'", inline=True)
comment(0x9542, "Save dir path start position", inline=True)
comment(0x9544, "FS command 4: examine directory", inline=True)
comment(0x9546, "Store in TX buffer", inline=True)
comment(0x9549, "Load FS flags", inline=True)
comment(0x954C, "Set bit 6 (FS selection active)", inline=True)
comment(0x954E, "Store updated flags", inline=True)
comment(0x9551, "X=1: buffer offset", inline=True)
comment(0x9553, "Copy FS number to buffer", inline=True)
comment(0x9556, "Y=&12: select FS command code", inline=True)
comment(0x9558, "Send FS selection command", inline=True)
comment(0x955B, "Load reply status", inline=True)
comment(0x955E, "Status 2 (found)?", inline=True)
comment(0x9560, "Yes: proceed to dir change", inline=True)
comment(0x9562, "Error number &D6", inline=True)
comment(0x9564, "Raise 'Not found' error", inline=True)
comment(0x9571, "Load current FS station byte", inline=True)
comment(0x9574, "Store in TX buffer", inline=True)
comment(0x9577, "X=1: buffer offset", inline=True)
comment(0x9579, "Y=7: change directory command code", inline=True)
comment(0x957B, "Send directory change request", inline=True)
comment(0x957E, "X=1", inline=True)
comment(0x9580, "Store start marker in buffer", inline=True)
comment(0x9583, "Store start marker in buffer+1", inline=True)
comment(0x9587, "Restore dir path start position", inline=True)
comment(0x9589, "Copy directory path to buffer", inline=True)
comment(0x958C, "Y=6: set directory command code", inline=True)
comment(0x958E, "Send set directory command", inline=True)
comment(0x9591, "Load reply handle", inline=True)
comment(0x9594, "Select FS and return", inline=True)
comment(0x9597, "Simple: pass command to FS", inline=True)

# init_txcb_bye / init_txcb_port / init_txcb (&9451-&9476)
comment(0x973D, "A=&90: bye command port", inline=True)
comment(0x973F, "Initialise TXCB from template", inline=True)
comment(0x9742, "Set transmit port", inline=True)
comment(0x9744, "A=3: data start offset", inline=True)
comment(0x9746, "Set TXCB start offset", inline=True)
comment(0x9748, "Open receive: &80->&7F (bit 7 clear = awaiting reply)", inline=True)
comment(0x974A, "Return", inline=True)
comment(0x974B, "Save A", inline=True)
comment(0x974C, "Y=&0B: template size - 1", inline=True)
comment(0x974E, "Load byte from TXCB template", inline=True)
comment(0x9751, "Store to TXCB workspace", inline=True)
comment(0x9754, "Index >= 2?", inline=True)
comment(0x9756, "Yes: skip dest station copy", inline=True)
comment(0x9758, "Load dest station byte", inline=True)
comment(0x975B, "Store to TXCB destination", inline=True)
comment(0x975E, "Decrement index", inline=True)
comment(0x975F, "More bytes: continue", inline=True)
comment(0x9761, "Restore A", inline=True)
comment(0x9762, "Return", inline=True)

# send_request_nowrite / send_request_write (&9483-&9488)
comment(0x976F, "Save A", inline=True)
comment(0x9770, "Set carry (read-only mode)", inline=True)
comment(0x9773, "Clear V", inline=True)

# cmd_flip (&A33E) — *Flip: toggle auto-boot configuration
comment(0xA69A, "Load current CSD handle", inline=True)
comment(0xA69D, "Save CSD handle", inline=True)
comment(0xA69E, "Load library handle into Y", inline=True)
comment(0xA6A1, "Install library as new CSD", inline=True)
comment(0xA6A4, "Restore original CSD handle", inline=True)
comment(0xA6A5, "Y = original CSD (becomes library)", inline=True)
comment(0xA6A6, "X=&10: max 16 station entries", inline=True)
comment(0xA6A8, "Clear V (no match found yet)", inline=True)
comment(0xA6A9, "Decrement station index", inline=True)
comment(0xA6AA, "All searched: exit loop", inline=True)
comment(0xA6AC, "Check if station[X] matches", inline=True)
comment(0xA6AF, "No match: try next station", inline=True)
comment(0xA6B1, "Load station flags byte", inline=True)
comment(0xA6B4, "Test bit 4 (active flag)", inline=True)
comment(0xA6B6, "Not active: try next station", inline=True)
comment(0xA6B8, "Transfer boot type to A", inline=True)
comment(0xA6B9, "Store boot setting for station", inline=True)
comment(0xA6BC, "Set V flag (station match found)", inline=True)
comment(0xA6BF, "Store boot type", inline=True)
comment(0xA6C2, "V set (matched): skip allocation", inline=True)
comment(0xA6C4, "Boot type to A", inline=True)
comment(0xA6C5, "Allocate FCB slot for new entry", inline=True)
comment(0xA6C8, "Store allocation result", inline=True)
comment(0xA6CB, "Zero: allocation failed, exit", inline=True)
comment(0xA6CD, "A=&32: station flags (active+boot)", inline=True)
comment(0xA6CF, "Store station flags", inline=True)
comment(0xA6D2, "Restore FS context and return", inline=True)
comment(0xA6D5, "Close all network channels", inline=True)
comment(0xA6DD, "Set carry flag", inline=True)
comment(0xA6DE, "Load reply boot type", inline=True)
comment(0xA6E1, "Store as current boot type", inline=True)
comment(0xA6E5, "Save processor status", inline=True)
comment(0xA6E6, "Load station number from reply", inline=True)
comment(0xA6E9, "Find station entry with bit 2", inline=True)
comment(0xA6EC, "Load network number from reply", inline=True)
comment(0xA6EF, "Find station entry with bit 3", inline=True)
comment(0xA6F2, "Load boot type from reply", inline=True)
comment(0xA6F5, "Set boot config for station", inline=True)
comment(0xA6F8, "Restore processor status", inline=True)
comment(0xA6F9, "Carry set: proceed with boot", inline=True)
comment(0xA6FB, "Return with last flag", inline=True)
comment(0xA726, "Load config flags", inline=True)
comment(0xA729, "Save copy in X", inline=True)
comment(0xA72A, "Test bit 2 (auto-boot flag)", inline=True)
comment(0xA72C, "Save bit 2 test result", inline=True)
comment(0xA72D, "Restore full flags", inline=True)
comment(0xA72E, "Clear bit 2 (consume flag)", inline=True)
comment(0xA730, "Store cleared flags", inline=True)
comment(0xA733, "Restore bit 2 test result", inline=True)
comment(0xA734, "Bit 2 was set: skip to boot cmd", inline=True)
comment(0xA736, "OSBYTE &79: scan keyboard", inline=True)
comment(0xA73E, "CTRL not pressed: proceed to boot", inline=True)
comment(0xA740, "CTRL pressed: cancel boot, return", inline=True)
# boot_oscli_lo_table (&A3C7): 4-byte boot command address table.
# Low bytes of OSCLI string addresses (all in page &A3).
# Entry 0 is never used (BEQ at &A3CE exits before lookup).
# Entry 2 cleverly points into "L.!BOOT" at &A3B9 = "!BOOT"
# which MOS treats as *RUN !BOOT.
# UNMAPPED: comment(0xA3DF, "Boot option OSCLI address table\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "Low bytes of boot command string addresses,\n"
# UNMAPPED:     "all in page &A3. Indexed by boot option 0-3\n"
# UNMAPPED:     "(option 0 is never reached due to BEQ).\n"
# UNMAPPED:     "Entry 2 reuses the tail of 'L.!BOOT' to\n"
# UNMAPPED:     "get '!BOOT' (*RUN equivalent).")
# UNMAPPED: comment(0xA3E3, "Load boot type", inline=True)
# UNMAPPED: comment(0xA3E6, "Type 0: no command, just return", inline=True)
comment(0xA764, "Look up boot command address low", inline=True)
comment(0xA767, "Boot command address high (&A3xx)", inline=True)
comment(0xA769, "Execute boot command via OSCLI", inline=True)

# cmd_remove (&AF46) — *Remove: delete file from server
comment(0xB312, "Convert remaining value to A", inline=True)
# UNMAPPED: comment(0xAF67, "Push onto stack", inline=True)
comment(0xB321, "Skip to check for extra arguments", inline=True)
# UNMAPPED: comment(0xAF6B, "End of line?", inline=True)
# UNMAPPED: comment(0xAF6D, "Yes: single arg, proceed", inline=True)
# UNMAPPED: comment(0xAF6F, "No: extra args, syntax error", inline=True)
# UNMAPPED: comment(0xAF72, "Restore command line offset", inline=True)
# UNMAPPED: comment(0xAF73, "Transfer to Y", inline=True)
# UNMAPPED: comment(0xAF74, "Save text pointer for parsing", inline=True)
# UNMAPPED: comment(0xAF77, "Parse filename argument", inline=True)
# UNMAPPED: comment(0xAF7A, "Copy filename to TX buffer", inline=True)
# UNMAPPED: comment(0xAF7D, "Y=&14: *Delete FS command code", inline=True)
# UNMAPPED: comment(0xAF7F, "Set V flag (via BIT #&FF)", inline=True)
# UNMAPPED: comment(0xAF82, "Send to FS with V-flag dispatch", inline=True)

# print_num_no_leading / print_decimal_3dig / print_decimal_digit
# Decimal number printing utility (&AF65-&AF94)
comment(0xB327, "Set V (suppress leading zeros)", inline=True)
comment(0xB32A, "Transfer value to Y (remainder)", inline=True)
comment(0xB32B, "A=100: hundreds divisor", inline=True)
comment(0xB32D, "Print hundreds digit", inline=True)
comment(0xB330, "A=10: tens divisor", inline=True)
comment(0xB332, "Print tens digit", inline=True)
comment(0xB335, "Clear V (always print units)", inline=True)
comment(0xB336, "A=1: units divisor", inline=True)
comment(0xB338, "Store divisor", inline=True)
comment(0xB33A, "Get remaining value", inline=True)
comment(0xB33B, "X='0'-1: digit counter", inline=True)
comment(0xB33D, "Set carry for subtraction", inline=True)
comment(0xB33E, "Save V flag for leading zero check", inline=True)
comment(0xB33F, "Count quotient digit", inline=True)
comment(0xB340, "Subtract divisor", inline=True)
comment(0xB342, "No underflow: continue dividing", inline=True)
comment(0xB344, "Add back divisor (get remainder)", inline=True)
comment(0xB346, "Remainder to Y for next digit", inline=True)
comment(0xB347, "Digit character to A", inline=True)
comment(0xB348, "Restore V flag", inline=True)
comment(0xB349, "V clear: always print digit", inline=True)
comment(0xB34B, "V set: is digit '0'?", inline=True)
comment(0xB34D, "Yes: suppress leading zero", inline=True)
comment(0xB34F, "Save divisor across OSASCI call", inline=True)
comment(0xB354, "Restore divisor", inline=True)
comment(0xB356, "Return", inline=True)

# save_ptr_to_os_text (&AF95-&AF9F)
comment(0xB373, "Save A", inline=True)
comment(0xB374, "Copy text pointer low byte", inline=True)
comment(0xB376, "To OS text pointer low", inline=True)
comment(0xB378, "Copy text pointer high byte", inline=True)
comment(0xB37A, "To OS text pointer high", inline=True)
comment(0xB37C, "Restore A", inline=True)
comment(0xB37D, "Return", inline=True)

# skip_to_next_arg (&AFA0-&AFB4)
comment(0xB37E, "Advance past current character", inline=True)
comment(0xB37F, "Load char from command line", inline=True)
comment(0xB381, "Space?", inline=True)
comment(0xB383, "Yes: skip trailing spaces", inline=True)
comment(0xB385, "CR (end of line)?", inline=True)
comment(0xB387, "Yes: return (at end)", inline=True)
comment(0xB38B, "Advance past space", inline=True)
comment(0xB38C, "Load next character", inline=True)
comment(0xB38E, "Still a space?", inline=True)
comment(0xB390, "Yes: skip multiple spaces", inline=True)
comment(0xB392, "Return (at next argument)", inline=True)

# save_ptr_to_spool_buf (&AFB5-&AFBF)
comment(0xB393, "Save A", inline=True)
comment(0xB394, "Copy text pointer low byte", inline=True)
comment(0xB396, "To spool buffer pointer low", inline=True)
comment(0xB398, "Copy text pointer high byte", inline=True)
comment(0xB39A, "To spool buffer pointer high", inline=True)
comment(0xB39C, "Restore A", inline=True)
comment(0xB39D, "Return", inline=True)

# init_spool_drive (&AFC0-&AFCD)
comment(0xB39E, "Save Y", inline=True)
comment(0xB39F, "Push it", inline=True)
comment(0xB3A0, "Get workspace page number", inline=True)
comment(0xB3A3, "Store as spool drive page high", inline=True)
comment(0xB3A5, "Restore Y", inline=True)
comment(0xB3A6, "Transfer to Y", inline=True)
comment(0xB3A7, "A=0", inline=True)
comment(0xB3A9, "Clear spool drive page low", inline=True)
comment(0xB3AB, "Return", inline=True)

# cmd_close (&B97F) — *Close: close all files
# UNMAPPED: comment(0xB994, "A=0: close all open files", inline=True)

# cmd_type (&B985) — *Type: display file contents
# UNMAPPED: comment(0xB99A, "Clear V for unconditional BVC", inline=True)

# cmd_print (&B988) — *Print: send file to printer
# UNMAPPED: comment(0xB99D, "Set V flag (= print mode)", inline=True)

# open_and_read_file (&B98B) — shared entry for Print/Type
# UNMAPPED: comment(0xB9A0, "Open file for reading", inline=True)
# UNMAPPED: comment(0xB9A5, "A = 0", inline=True)
# UNMAPPED: comment(0xB9A7, "Clear previous-character tracker", inline=True)
# UNMAPPED: comment(0xB9A9, "Save V flag (print/type mode)", inline=True)
# UNMAPPED: comment(0xB9AD, "Branch if not end of file", inline=True)
# UNMAPPED: comment(0xB9AF, "EOF: restore processor status", inline=True)
# UNMAPPED: comment(0xB9B0, "Close the file", inline=True)

# Process character
# UNMAPPED: comment(0xB9B6, "Check for escape key pressed", inline=True)
# UNMAPPED: comment(0xB9B9, "Restore V (print/type mode)", inline=True)
# UNMAPPED: comment(0xB9BA, "Re-save for next iteration", inline=True)
# UNMAPPED: comment(0xB9BB, "Print mode: skip CR/LF handling", inline=True)
# UNMAPPED: comment(0xB9BD, "Is it a carriage return?", inline=True)
# UNMAPPED: comment(0xB9BF, "Yes: handle line ending", inline=True)
# UNMAPPED: comment(0xB9C1, "Is it a line feed?", inline=True)
# UNMAPPED: comment(0xB9C3, "Yes: handle line ending", inline=True)

# Output character
# UNMAPPED: comment(0xB9C5, "Save as previous character", inline=True)
# UNMAPPED: comment(0xB9CA, "Loop for next byte", inline=True)

# CR/LF handling in type mode
# UNMAPPED: comment(0xB9CD, "Save the CR or LF character", inline=True)
# UNMAPPED: comment(0xB9CE, "Check output destination flag", inline=True)
# UNMAPPED: comment(0xB9D1, "Zero: normalise line endings", inline=True)
# UNMAPPED: comment(0xB9D3, "Non-zero: output raw", inline=True)
# UNMAPPED: comment(0xB9D5, "Clear previous-character tracker", inline=True)
# UNMAPPED: comment(0xB9D7, "Retrieve CR/LF", inline=True)
# UNMAPPED: comment(0xB9D8, "Output it directly; ALWAYS branch", inline=True)

# Line ending normalisation (l00ad tracks previous char)
# UNMAPPED: comment(0xB9DA, "Get previous character", inline=True)
# UNMAPPED: comment(0xB9DC, "Was previous a CR?", inline=True)
# UNMAPPED: comment(0xB9DE, "Yes: check for CR+LF pair", inline=True)
# UNMAPPED: comment(0xB9E0, "Was previous a LF?", inline=True)
# UNMAPPED: comment(0xB9E2, "Yes: check for LF+CR pair", inline=True)
# UNMAPPED: comment(0xB9E4, "Retrieve CR/LF from stack", inline=True)
# UNMAPPED: comment(0xB9E5, "Save as previous character", inline=True)
# UNMAPPED: comment(0xB9EA, "Loop for next byte", inline=True)

# Previous was CR — check for CR+LF pair
# UNMAPPED: comment(0xB9ED, "Retrieve current character", inline=True)
# UNMAPPED: comment(0xB9EE, "Is it LF? (CR+LF pair)", inline=True)
# UNMAPPED: comment(0xB9F0, "Yes: consume LF, no extra newline", inline=True)
# UNMAPPED: comment(0xB9F2, "No: output extra newline", inline=True)

# Previous was LF — check for LF+CR pair
# UNMAPPED: comment(0xB9F4, "Retrieve current character", inline=True)
# UNMAPPED: comment(0xB9F5, "Is it CR? (LF+CR pair)", inline=True)
# UNMAPPED: comment(0xB9F7, "No: output extra newline", inline=True)

# Consume paired character
# UNMAPPED: comment(0xB9F9, "Pair consumed: A = 0", inline=True)
# UNMAPPED: comment(0xB9FB, "Clear previous-character tracker", inline=True)
# UNMAPPED: comment(0xB9FD, "Loop for next byte; ALWAYS branch", inline=True)

# abort_if_escape (&B9EA) — abort file read on Escape
comment(0xBD25, "Test bit 7 of escape flag", inline=True)
comment(0xBD27, "Escape pressed: handle abort", inline=True)
comment(0xBD29, "No escape: return", inline=True)
comment(0xBD2A, "Close the open file", inline=True)
comment(0xBD30, "Acknowledge escape condition", inline=True)
comment(0xBD35, "Error number &11", inline=True)
comment(0xBD37, "Generate 'Escape' BRK error", inline=True)

# cmd_pollps (&B19F) — *PollPS: poll printer server status
# Entry and setup
comment(0xB581, "Save command line pointer high", inline=True)
comment(0xB583, "Initialise spool/print drive", inline=True)
comment(0xB586, "Save spool drive number", inline=True)
comment(0xB588, "Copy PS name to TX buffer", inline=True)
comment(0xB58B, "Init PS slot from RX data", inline=True)
comment(0xB58E, "Restore command line pointer", inline=True)
comment(0xB590, "Save pointer to spool buffer", inline=True)
comment(0xB593, "Get first argument character", inline=True)
comment(0xB595, "End of command line?", inline=True)
comment(0xB597, "Yes: no argument given", inline=True)

# Argument parsing: check if PS name or station number
comment(0xB599, "Clear V (= explicit PS name given)", inline=True)
comment(0xB59A, "Is first char a decimal digit?", inline=True)
comment(0xB59D, "Yes: station number, skip PS name", inline=True)
comment(0xB59F, "PS name follows", inline=True)
comment(0xB5A0, "Save Y", inline=True)
comment(0xB5A1, "Load PS server address", inline=True)
comment(0xB5A4, "Restore Y", inline=True)
comment(0xB5A5, "Back to Y register", inline=True)
comment(0xB5A6, "Parse FS/PS arguments", inline=True)
comment(0xB5A9, "Offset &7A in slot buffer", inline=True)
comment(0xB5AB, "Get parsed station low", inline=True)
comment(0xB5AD, "Store station number low", inline=True)
comment(0xB5B0, "Get parsed network number", inline=True)
comment(0xB5B2, "Store station number high", inline=True)
comment(0xB5B4, "Offset &14 in TX buffer", inline=True)
comment(0xB5B6, "Copy PS data to TX buffer", inline=True)
comment(0xB5B9, "Get buffer page high", inline=True)
comment(0xB5BB, "Set TX pointer high byte", inline=True)
comment(0xB5BD, "Offset &78 in buffer", inline=True)
comment(0xB5BF, "Set TX pointer low byte", inline=True)

# No argument path: set V flag
comment(0xB5C3, "Set V (= no explicit PS name)", inline=True)

# Station number path: fill PS name buffer
comment(0xB5C6, "V set (no arg): skip to send", inline=True)
comment(0xB5C8, "Max 6 characters for PS name", inline=True)
comment(0xB5CA, "Buffer offset for PS name", inline=True)
comment(0xB5CC, "Space character", inline=True)
comment(0xB5CE, "Fill buffer position with space", inline=True)
comment(0xB5D0, "Next position", inline=True)
comment(0xB5D1, "Count down", inline=True)
comment(0xB5D2, "Loop until 6 spaces filled", inline=True)
comment(0xB5D4, "Save pointer to OS text", inline=True)
comment(0xB5D7, "Restore command line pointer", inline=True)
comment(0xB5D9, "Initialise string reading", inline=True)
comment(0xB5DC, "Empty string: skip to send", inline=True)
comment(0xB5DE, "Max 6 characters", inline=True)
comment(0xB5E0, "Save updated string pointer", inline=True)
comment(0xB5E2, "Buffer offset for PS name", inline=True)
comment(0xB5E4, "Save buffer position", inline=True)

# Copy PS name from command line, uppercased
comment(0xB5E6, "Restore string pointer", inline=True)
comment(0xB5E8, "Read next char from string", inline=True)
comment(0xB5EB, "Save updated string pointer", inline=True)
comment(0xB5ED, "End of string: go to send", inline=True)
comment(0xB5EF, "Store char uppercased in buffer", inline=True)
comment(0xB5F2, "Loop if more chars to copy", inline=True)

# Send poll request and display header
comment(0xB5F4, "Enable escape checking", inline=True)
comment(0xB5F6, "Set escapable flag", inline=True)
comment(0xB5F8, "Send the poll request packet", inline=True)
comment(0xB5FB, "Pop and requeue PS scan", inline=True)
comment(0xB5FE, "Print 'Printer server '", inline=True)
comment(0xB601, "Load PS server address", inline=True)
comment(0xB604, "Set V and N flags", inline=True)
comment(0xB607, "Print station address", inline=True)
comment(0xB60A, "Print ' \"'", inline=True)
# UNMAPPED: comment(0xB251, "Y=&18: name field offset in RX buffer", inline=True)

# Display PS name from RX buffer
comment(0xB611, "Get character from name field", inline=True)
comment(0xB613, "Is it a space?", inline=True)
comment(0xB615, "Yes: end of name", inline=True)
comment(0xB61A, "Next character", inline=True)
comment(0xB61B, "Past end of name field?", inline=True)
comment(0xB61D, "No: continue printing name", inline=True)
comment(0xB61F, "Print '\"' + CR", inline=True)
# UNMAPPED: comment(0xB266, "Padding byte", inline=True)

# Poll each printer slot
# UNMAPPED: comment(0xB267, "Get slot offset from stack", inline=True)
comment(0xB626, "Zero: all slots done, return", inline=True)
comment(0xB628, "Save slot offset", inline=True)
comment(0xB629, "Transfer to Y", inline=True)
comment(0xB62A, "Read slot status byte", inline=True)
comment(0xB62C, "Bit 7 clear: slot inactive", inline=True)
comment(0xB62E, "Advance to station number", inline=True)
comment(0xB62F, "Offset+2 in slot", inline=True)
comment(0xB630, "Read station number low", inline=True)
comment(0xB632, "Store station low", inline=True)
comment(0xB634, "Next byte (offset+3)", inline=True)
comment(0xB635, "Read network number", inline=True)
comment(0xB637, "Store network number", inline=True)
comment(0xB639, "Next byte (offset+4)", inline=True)
comment(0xB63A, "Read status page pointer", inline=True)
comment(0xB63C, "Store pointer low", inline=True)
comment(0xB63E, "Clear V flag", inline=True)
comment(0xB63F, "Print station address (V=0)", inline=True)
comment(0xB642, "Print ' is '", inline=True)

# Display printer status
# UNMAPPED: comment(0xB28B, "X=0 for indirect indexed access", inline=True)
comment(0xB64B, "Read printer status byte", inline=True)
comment(0xB64D, "Non-zero: not ready", inline=True)
comment(0xB64F, "Print 'ready'", inline=True)
# UNMAPPED: comment(0xB299, "Clear V", inline=True)
comment(0xB65A, "Status = 2?", inline=True)
comment(0xB65C, "No: check for busy", inline=True)
comment(0xB65E, "Print 'jammed'", inline=True)
comment(0xB667, "Clear V", inline=True)
comment(0xB66A, "Status = 1?", inline=True)
comment(0xB66C, "Not 1 or 2: default to jammed", inline=True)
comment(0xB66E, "Print 'busy'", inline=True)

# Display client station for busy printer
# UNMAPPED: comment(0xB2B7, "Advance past status byte", inline=True)
comment(0xB677, "Read client station number", inline=True)
comment(0xB679, "Store station low", inline=True)
comment(0xB67B, "Zero: no client info, skip", inline=True)
comment(0xB67D, "Print ' with station '", inline=True)
# UNMAPPED: comment(0xB2C8, "Advance pointer to network byte", inline=True)
comment(0xB692, "Store network number", inline=True)
# UNMAPPED: comment(0xB2CA, "Load client network number", inline=True)
comment(0xB694, "Set V flag", inline=True)
comment(0xB697, "Print client station address", inline=True)

# Advance to next slot
comment(0xB69D, "Retrieve slot offset", inline=True)
comment(0xB69E, "Transfer to Y", inline=True)
comment(0xB69F, "Mark slot as processed (&3F)", inline=True)
comment(0xB6A1, "Write marker to workspace", inline=True)
comment(0xB6A5, "Return", inline=True)

# init_ps_slot_from_rx (&B2C4) — initialise PS slot from RX data
comment(0xB6A6, "Start at offset &78", inline=True)
comment(0xB6A8, "Load template byte", inline=True)
comment(0xB6AB, "At offset &7D?", inline=True)
comment(0xB6AD, "Yes: substitute RX page", inline=True)
comment(0xB6AF, "At offset &81?", inline=True)
comment(0xB6B1, "No: use template byte", inline=True)
comment(0xB6B3, "Use RX buffer page instead", inline=True)
comment(0xB6B5, "Store byte in slot buffer", inline=True)
comment(0xB6B7, "Next offset", inline=True)
comment(0xB6B8, "Past end of slot (&84)?", inline=True)
comment(0xB6BA, "No: continue copying", inline=True)
comment(0xB6BC, "Return", inline=True)

# store_char_uppercase (&B2DB) — store char to buffer, uppercased
comment(0xB6BD, "Y = current buffer position", inline=True)
comment(0xB6BF, "Strip high bit", inline=True)
comment(0xB6C1, "Is it lowercase 'a' or above?", inline=True)
comment(0xB6C3, "Below 'a': not lowercase", inline=True)
comment(0xB6C5, "Above 'z'?", inline=True)
comment(0xB6C7, "Yes: not lowercase", inline=True)
comment(0xB6C9, "Convert to uppercase", inline=True)
comment(0xB6CB, "Store in RX buffer", inline=True)
comment(0xB6CD, "Next buffer position", inline=True)
comment(0xB6CE, "Update buffer position", inline=True)
comment(0xB6D0, "Decrement character count", inline=True)
comment(0xB6D1, "Return (Z set if count=0)", inline=True)

# cmd_ex (&AD59) — *Ex: examine directory listing
# Entry: set up for Ex mode (1 entry per line, FS code 3)
comment(0xB103, "Rotate carry into lib flag bit 7", inline=True)
comment(0xB106, "Clear carry (= current directory)", inline=True)
comment(0xB107, "Rotate carry back, clearing bit 7", inline=True)
comment(0xB10A, "A=&FF: initial column counter", inline=True)
comment(0xB10C, "Store column counter", inline=True)
comment(0xB10E, "One entry per line (Ex format)", inline=True)
comment(0xB110, "Store entries per page", inline=True)
comment(0xB112, "FS command code 3: Examine", inline=True)
comment(0xB114, "Store command code", inline=True)

# Cat entry (&AD6E) — *Cat: catalogue directory
comment(0xB118, "Set transfer parameters", inline=True)
comment(0xB11B, "Y=0: start from entry 0", inline=True)
comment(0xB11D, "Rotate carry into lib flag", inline=True)
comment(0xB120, "Clear carry (= current directory)", inline=True)
comment(0xB121, "Rotate carry back, clearing bit 7", inline=True)
comment(0xB124, "Three entries per column (Cat)", inline=True)
comment(0xB126, "Store column counter", inline=True)
comment(0xB128, "Store entries per page", inline=True)
comment(0xB12A, "FS command code &0B: Catalogue", inline=True)
comment(0xB12C, "Store command code", inline=True)

# Shared Ex/Cat setup
comment(0xB12E, "Save text pointer", inline=True)
comment(0xB131, "A=&FF: enable escape checking", inline=True)
comment(0xB133, "Set escapable flag", inline=True)
comment(0xB135, "Command code 6", inline=True)
comment(0xB137, "Store in TX buffer", inline=True)
comment(0xB13A, "Parse directory argument", inline=True)
comment(0xB13D, "X=1: offset in buffer", inline=True)
comment(0xB13F, "Copy argument to TX buffer", inline=True)
comment(0xB142, "Get library/FS flags", inline=True)
comment(0xB145, "Shift bit 0 to carry", inline=True)
comment(0xB146, "Bit 0 clear: skip", inline=True)
comment(0xB148, "Set bit 6 (owner access flag)", inline=True)
comment(0xB14A, "Rotate back", inline=True)
comment(0xB14B, "Store modified flags", inline=True)
comment(0xB14E, "Y=&12: FS command for examine", inline=True)
comment(0xB150, "Send request to file server", inline=True)
comment(0xB153, "X=3: offset to directory title", inline=True)
comment(0xB155, "Print directory title (10 chars)", inline=True)
comment(0xB158, "Print '('", inline=True)

# Directory header: cycle number and access
comment(0xADB2, "Get cycle number", inline=True)
comment(0xADB8, "Print ')     '", inline=True)
# UNMAPPED: comment(0xADD3, "Get owner/public flag", inline=True)
# UNMAPPED: comment(0xADD6, "Non-zero: public access", inline=True)
comment(0xB170, "Print 'Owner' + CR", inline=True)
# UNMAPPED: comment(0xADE1, "Skip public; ALWAYS branch", inline=True)
comment(0xB17B, "Print 'Public' + CR", inline=True)

# Directory info: option, dir name, lib name
# UNMAPPED: comment(0xADED, "Get flags", inline=True)
# UNMAPPED: comment(0xADF0, "Save flags", inline=True)
comment(0xB189, "Mask owner access bits", inline=True)
comment(0xB18C, "Y=&15: FS command for dir info", inline=True)
comment(0xB18E, "Send request to file server", inline=True)
comment(0xB191, "Advance X past header", inline=True)
comment(0xB192, "Y=&10: print 16 chars", inline=True)
comment(0xB194, "Print file entry", inline=True)
comment(0xB197, "Print '    Option '", inline=True)
# UNMAPPED: comment(0xAE0D, "Get option byte", inline=True)
comment(0xB1A8, "Transfer to X for table lookup", inline=True)
comment(0xB1A9, "Print option as hex", inline=True)
comment(0xB1AC, "Print ' ('", inline=True)
comment(0xAE19, "Y=string offset for boot option X", inline=True)
comment(0xAE31, "Offset &11: directory name", inline=True)
comment(0xAE33, "Print directory name (10 chars)", inline=True)
comment(0xAE1C, "Load option description character", inline=True)
comment(0xAE3A, "Print '     Lib. '", inline=True)
comment(0xAE36, "Print '     Lib. '", inline=True)
comment(0xAE1F, "Bit 7 set: end of option string", inline=True)
comment(0xAE43, "Offset &1B: library name", inline=True)
comment(0xAE45, "Print library name (10 chars)", inline=True)
comment(0xAE4B, "Restore flags", inline=True)
comment(0xAE4C, "Store restored flags", inline=True)

# Entry listing loop
comment(0xAE4F, "Store entry count", inline=True)
comment(0xAE52, "Also store in work_4", inline=True)
comment(0xAE54, "Get command code", inline=True)
comment(0xAE56, "Store in buffer", inline=True)
comment(0xAE59, "Get entries per page", inline=True)
comment(0xAE5B, "Store in buffer", inline=True)
comment(0xAE5E, "X=3: buffer offset", inline=True)
comment(0xAE60, "Copy argument to buffer", inline=True)
comment(0xAE63, "Y=3: FS command for examine/cat", inline=True)
comment(0xAE65, "Send request to file server", inline=True)
comment(0xAE68, "Advance past header", inline=True)
comment(0xAE69, "Get number of entries returned", inline=True)
comment(0xAE6C, "Zero: no more entries", inline=True)
comment(0xAE6E, "Save entry count", inline=True)

# Scan for end-of-entry marker
comment(0xAE6F, "Advance Y", inline=True)
comment(0xAE70, "Get entry data byte", inline=True)
comment(0xAE73, "Bit 7 clear: more data", inline=True)
comment(0xAE75, "Store terminator byte", inline=True)
comment(0xAE78, "Print entry with column separator", inline=True)
comment(0xAE7B, "Restore entry count", inline=True)
comment(0xAE7C, "Clear carry for addition", inline=True)
comment(0xAE7D, "Add entries processed", inline=True)
comment(0xAE7F, "Transfer to Y", inline=True)
comment(0xAE80, "More entries: loop", inline=True)

# print_10_chars (&AE70) — print 10 chars from buffer at X
comment(0xAE82, "Y=10: characters to print", inline=True)
comment(0xAE84, "Get character from buffer", inline=True)
comment(0xAE8A, "Next buffer position", inline=True)
comment(0xAE8B, "Decrement count", inline=True)
comment(0xAE8C, "Loop until 10 printed", inline=True)
comment(0xAE8E, "Return", inline=True)

# parse_cmd_arg_y0 (&AE80)
comment(0xAE92, "Y=0: start of command line", inline=True)

# parse_filename_arg (&AE82)
comment(0xAE94, "Read string to buffer via GSREAD", inline=True)

# parse_access_prefix (&AE85) — parse '&' or ':' FS prefix
comment(0xAE97, "Get first parsed character", inline=True)
comment(0xAE9A, "Is it '&'?", inline=True)
comment(0xAE9C, "No: check for ':' prefix", inline=True)
comment(0xAE9E, "Get flags", inline=True)
comment(0xAEA1, "Set FS selection flag (bit 6)", inline=True)
comment(0xAEA3, "Store updated flags", inline=True)
comment(0xAEA6, "Remove '&' prefix character", inline=True)
comment(0xAEA9, "Get next character", inline=True)
comment(0xAEAC, "Is it '.'?", inline=True)
comment(0xAEAE, "No: check for '#'", inline=True)
comment(0xAEB0, "Get char after '.'", inline=True)
comment(0xAEB3, "Is it CR (end of line)?", inline=True)
comment(0xAEB5, "Yes: '&.' + CR only = bad filename", inline=True)

# strip_token_prefix (&AEA5) — shift buffer left by 1 char
comment(0xAEB7, "Save X", inline=True)
comment(0xAEB8, "Push X", inline=True)
comment(0xAEB9, "X=&FF, will increment to 0", inline=True)
comment(0xAEBB, "Increment X", inline=True)
comment(0xAEBC, "Get character at offset+1", inline=True)
comment(0xAEBF, "Store at offset (shift left)", inline=True)
comment(0xAEC2, "Is it CR (end of line)?", inline=True)
comment(0xAEC4, "No: continue shifting", inline=True)
comment(0xAEC6, "Get shifted string length", inline=True)
comment(0xAEC7, "Zero length: skip trailing trim", inline=True)
comment(0xAEC9, "Get character at end of string", inline=True)
comment(0xAECC, "Is it a space?", inline=True)
comment(0xAECE, "No: done trimming", inline=True)
comment(0xAED0, "Replace trailing space with CR", inline=True)
comment(0xAED2, "Store CR", inline=True)
comment(0xAED5, "Move back", inline=True)
comment(0xAED6, "Loop while more trailing spaces", inline=True)
comment(0xAED8, "Restore X", inline=True)
comment(0xAED9, "Transfer back to X", inline=True)
comment(0xAEDA, "Return", inline=True)

# Error paths for parse_access_prefix
comment(0xAEDB, "Is it '#'?", inline=True)
comment(0xAEDD, "Yes: '#' prefix accepted", inline=True)
comment(0xAEDF, "Bad filename error", inline=True)

# Alternative ':' prefix path
comment(0xAEE2, "Check for ':' prefix", inline=True)
comment(0xAEE4, "Neither '&' nor ':': no prefix", inline=True)
comment(0xAEE6, "Get character after ':'", inline=True)
comment(0xAEE9, "Is it '.'?", inline=True)
comment(0xAEEB, "Yes: ':.' qualified prefix", inline=True)
comment(0xAEED, "Is it CR (end of line)?", inline=True)
comment(0xAEEF, "No: no FS prefix, return", inline=True)
comment(0xAEF1, "Get flags", inline=True)
comment(0xAEF4, "Set FS selection flag (bit 6)", inline=True)
comment(0xAEF6, "Store updated flags", inline=True)
comment(0xAEFB, "Data: option string offset table", inline=True)

# copy_arg_to_buf_x0 (&AEF0) — copy argument to buffer
comment(0xAF02, "X=0: start of buffer", inline=True)
comment(0xAF04, "Y=0: start of argument", inline=True)
comment(0xAF06, "Set carry: enable '&' validation", inline=True)
comment(0xAF07, "Get character from command line", inline=True)
comment(0xAF09, "Store in TX buffer", inline=True)
comment(0xAF0C, "Carry clear: skip validation", inline=True)
comment(0xAF0E, "Is it '!' or above?", inline=True)
comment(0xAF10, "Is it '&'?", inline=True)
comment(0xAF12, "Yes: '&' not allowed in filenames", inline=True)
comment(0xAF14, "'&' in filename: bad filename", inline=True)
comment(0xAF14, "Restore A (undo '&' EOR)", inline=True)
comment(0xAF16, "Advance buffer position", inline=True)
comment(0xAF17, "Advance source position", inline=True)
comment(0xAF18, "Is it CR (end of line)?", inline=True)
comment(0xAF1A, "No: continue copying", inline=True)
comment(0xAF1C, "Load character from end of buffer", inline=True)
comment(0xAF2D, "Return", inline=True)
comment(0xAF1F, "Test for space (&20)", inline=True)

comment(0xAF21, "Not a space: done trimming", inline=True)
# mask_owner_access (&AF12) — clear owner/FS bits from flags
comment(0xAF23, "Back up one position", inline=True)
comment(0xAF32, "Get flags", inline=True)
comment(0xAF24, "CR terminator", inline=True)
comment(0xAF35, "Mask to low 5 bits only", inline=True)
comment(0xAF26, "Replace trailing space with CR", inline=True)
comment(0xAF37, "Store masked flags", inline=True)
comment(0xAF29, "ALWAYS: trim next character back", inline=True)
comment(0xAF3A, "Return", inline=True)
comment(0xAF2B, "A=0: success return code", inline=True)

# ex_print_col_sep (&AF27) — print column separator or newline
comment(0xAF3E, "X=0: start from first entry", inline=True)
comment(0xAF40, "Get entry byte from buffer", inline=True)
comment(0xAF43, "High bit set: end of entries", inline=True)
comment(0xAF45, "Non-zero: printable character", inline=True)
comment(0xAF47, "Get column counter", inline=True)
comment(0xAF49, "Negative: newline mode (Ex)", inline=True)
comment(0xAF4B, "Increment column counter", inline=True)
comment(0xAF4C, "Transfer to A", inline=True)
comment(0xAF4D, "Modulo 4 (Cat: 3 per row)", inline=True)
comment(0xAF4F, "Store updated counter", inline=True)
comment(0xAF51, "Zero: row full, print newline", inline=True)
comment(0xAF53, "Print '  ' column separator", inline=True)
comment(0xAF58, "Skip newline; ALWAYS branch", inline=True)
comment(0xAF5A, "CR character for newline", inline=True)
comment(0xAF5F, "Advance to next entry", inline=True)
comment(0xAF60, "Loop for more entries", inline=True)
comment(0xAF62, "Embedded string data 'Exec'", inline=True)
comment(0xAF64, "Embedded string data (contd)", inline=True)

# cmd_ps (&AFCE) — *PS: list printer server status
# Entry: check printer available
comment(0xAFEE, "A=1: check printer ready", inline=True)
comment(0xAFF0, "Test printer server workspace flag", inline=True)
comment(0xAFF3, "Non-zero: printer available", inline=True)
comment(0xAFF5, "Printer not available: error", inline=True)

# Initialise and parse argument
comment(0xAFF8, "Initialise spool drive", inline=True)
comment(0xAFFB, "Save pointer to spool buffer", inline=True)
comment(0xAFFE, "Get first argument character", inline=True)
comment(0xB000, "End of command line?", inline=True)
comment(0xB002, "Yes: no argument given", inline=True)
comment(0xB004, "Clear V (= explicit PS name given)", inline=True)
comment(0xB005, "Is first char a decimal digit?", inline=True)
comment(0xB008, "Yes: station number, skip PS name", inline=True)
comment(0xB00A, "PS name follows", inline=True)
comment(0xB00B, "Save Y", inline=True)
comment(0xB00C, "Load PS server address", inline=True)
comment(0xB00F, "Restore Y", inline=True)
comment(0xB010, "Back to Y register", inline=True)
comment(0xB011, "Parse FS/PS arguments", inline=True)
comment(0xB014, "Jump to store station address", inline=True)

# copy_ps_data (&AFF7) — copy PS data from template
comment(0xB017, "Start at offset &1C", inline=True)
comment(0xB019, "X=&F8: offset into template", inline=True)
comment(0xB01B, "Get template byte", inline=True)
comment(0xB01E, "Store in RX buffer", inline=True)
comment(0xB020, "Next destination offset", inline=True)
comment(0xB021, "Next source offset", inline=True)
comment(0xB022, "Loop until X wraps to 0", inline=True)
comment(0xB024, "Return", inline=True)

# No argument: set V and skip PS name
comment(0xB025, "Set V (= no explicit PS name)", inline=True)

# Station number path: fill PS name buffer
comment(0xB028, "Save command line pointer", inline=True)
comment(0xB02A, "V set: skip PS name parsing", inline=True)
comment(0xB02C, "Max 6 characters for PS name", inline=True)
comment(0xB02E, "Buffer offset &1C for PS name", inline=True)
comment(0xB030, "Space character", inline=True)
comment(0xB032, "Fill buffer with space", inline=True)
comment(0xB034, "Next position", inline=True)
comment(0xB035, "Count down", inline=True)
comment(0xB036, "Loop until 6 spaces filled", inline=True)
comment(0xB038, "Save text pointer", inline=True)
comment(0xB03B, "Restore command line pointer", inline=True)
comment(0xB03D, "Initialise string reading", inline=True)
comment(0xB040, "Empty string: skip to send", inline=True)
comment(0xB042, "Max 6 characters", inline=True)
comment(0xB044, "Save updated string pointer", inline=True)
comment(0xB046, "Buffer offset for PS name", inline=True)
comment(0xB048, "Save buffer position", inline=True)

# Copy PS name from command line
comment(0xB04A, "Restore string pointer", inline=True)
comment(0xB04C, "Read next character", inline=True)
comment(0xB04F, "Save updated pointer", inline=True)
comment(0xB051, "End of string: go to send", inline=True)
comment(0xB053, "Store char uppercased in buffer", inline=True)
comment(0xB056, "Loop for more characters", inline=True)

# Send PS status request
comment(0xB058, "Copy reversed PS name to TX", inline=True)
comment(0xB05B, "Send PS status request", inline=True)
comment(0xB05E, "Pop and requeue PS scan", inline=True)
comment(0xB061, "Load PS server address", inline=True)
comment(0xB064, "A=0", inline=True)
comment(0xB067, "Offset &24 in buffer", inline=True)
comment(0xB069, "Clear PS status byte", inline=True)

# Scan PS slots for ready printer
comment(0xB06B, "Get slot offset from stack", inline=True)
comment(0xB06C, "Zero: all slots done", inline=True)
comment(0xB06E, "Save slot offset", inline=True)
comment(0xB06F, "Transfer to Y", inline=True)
comment(0xB070, "Read slot status", inline=True)
comment(0xB072, "Bit 7 clear: slot inactive", inline=True)
comment(0xB074, "Advance Y by 4 (to status page)", inline=True)
comment(0xB077, "Read status page pointer", inline=True)
comment(0xB079, "Store pointer low", inline=True)
comment(0xB07B, "Read printer status byte", inline=True)
comment(0xB07D, "Zero (idle): show station info", inline=True)
comment(0xB081, "Non-zero (busy): skip", inline=True)
comment(0xB07F, "Status 3 (paused)?", inline=True)
comment(0xB083, "Back to network number", inline=True)
comment(0xB084, "Read network number", inline=True)
comment(0xB086, "Store network number", inline=True)
comment(0xB088, "Back to station number", inline=True)
comment(0xB089, "Read station number", inline=True)
comment(0xB08B, "Store station low", inline=True)
comment(0xB08D, "Offset &24 in buffer", inline=True)
comment(0xB08F, "Store ready station in buffer", inline=True)

# Mark slot and advance
comment(0xB091, "Retrieve slot offset", inline=True)
comment(0xB092, "Transfer to Y", inline=True)
comment(0xB093, "Mark slot as processed (&3F)", inline=True)
comment(0xB095, "Write marker to workspace", inline=True)

# Display PS status
comment(0xB099, "Print 'Printer server is '", inline=True)
comment(0xB09C, "Offset &24: PS station number", inline=True)
comment(0xB09E, "Get stored station number", inline=True)
comment(0xB0A0, "Non-zero: server changed", inline=True)
comment(0xB0A2, "Print 'still '", inline=True)
comment(0xB0AB, "Clear V", inline=True)
comment(0xB0AE, "Print 'now '", inline=True)
comment(0xB0B5, "Padding", inline=True)

# Store new PS address in workspace
comment(0xB0B8, "Workspace offset 2", inline=True)
comment(0xB0B9, "Y=2: workspace offset for station", inline=True)
comment(0xB0BB, "Get station low", inline=True)
comment(0xB0BD, "Store in workspace", inline=True)
comment(0xB0C0, "Get network number", inline=True)
comment(0xB0C2, "Store in workspace", inline=True)
comment(0xB0C4, "Return", inline=True)

# print_file_server_is (&B0A1)
comment(0xB0C5, "Print 'File'", inline=True)
comment(0xB0CC, "Clear V", inline=True)

# print_printer_server_is (&B0AB)
comment(0xB0CF, "Print 'Printer'", inline=True)
comment(0xB0D9, "Padding", inline=True)
comment(0xB0DA, "Print ' server is '", inline=True)
comment(0xB0E8, "Padding", inline=True)
comment(0xB0E9, "Return", inline=True)

# load_ps_server_addr (&B0C6) — load PS address from workspace
comment(0xB0EA, "Workspace offset 2", inline=True)
comment(0xB0EC, "Read station low", inline=True)
comment(0xB0EE, "Store station low", inline=True)
comment(0xB0F1, "Read network number", inline=True)
comment(0xB0F3, "Store network number", inline=True)
comment(0xB0F5, "Return", inline=True)

# pop_requeue_ps_scan (&B0D2) — requeue print server scan
comment(0xB0F6, "Pop return address low", inline=True)
comment(0xB0F7, "Save return address low", inline=True)
comment(0xB0F9, "Pop return address high", inline=True)
comment(0xB0FA, "Save return address high", inline=True)
comment(0xB0FC, "Push 0 as end-of-list marker", inline=True)
comment(0xB0FE, "Push it", inline=True)
comment(0xB0FF, "Start scanning from offset &84", inline=True)
comment(0xB101, "Store scan position", inline=True)
comment(0xB103, "Shift PS slot flags right", inline=True)
comment(0xB106, "Counter: 3 PS slots", inline=True)

# Slot scanning loop
comment(0xB108, "Convert to 2-bit workspace index", inline=True)
comment(0xB10B, "Carry set: no more slots", inline=True)
comment(0xB10D, "Shift right twice", inline=True)
comment(0xB10E, "To get slot offset", inline=True)
comment(0xB10F, "Transfer to X", inline=True)
comment(0xB110, "Read slot status byte", inline=True)
comment(0xB112, "Zero: empty slot, done", inline=True)
comment(0xB114, "Is it processed marker (&3F)?", inline=True)
comment(0xB116, "Yes: re-initialise this slot", inline=True)
comment(0xB118, "Try next slot", inline=True)
comment(0xB119, "Transfer slot index to A", inline=True)
comment(0xB11A, "Loop for more slots", inline=True)

# Re-initialise PS slot
comment(0xB11C, "Y = workspace offset of slot", inline=True)
comment(0xB11D, "Push slot offset for scan list", inline=True)
comment(0xB11E, "Set active status (&7F)", inline=True)
comment(0xB120, "Write status byte", inline=True)
comment(0xB122, "Next byte", inline=True)
comment(0xB123, "Low byte: workspace page", inline=True)
comment(0xB125, "Write workspace pointer low", inline=True)
comment(0xB127, "A=0", inline=True)
comment(0xB129, "Write two zero bytes + advance Y", inline=True)
comment(0xB12C, "Get current scan page", inline=True)
comment(0xB12E, "Write RX buffer page low", inline=True)
comment(0xB130, "Clear carry for addition", inline=True)
comment(0xB131, "Save processor status", inline=True)
comment(0xB132, "Advance by 3 pages", inline=True)
comment(0xB134, "Restore processor status", inline=True)
comment(0xB135, "Update scan position", inline=True)
comment(0xB137, "Write buffer page + &FF bytes", inline=True)
comment(0xB13A, "Get updated scan position", inline=True)
comment(0xB13C, "Write RX buffer page high", inline=True)
comment(0xB13E, "Write another page + &FF bytes", inline=True)
comment(0xB141, "Continue scanning slots", inline=True)

# Done scanning: restore return addr and delay
comment(0xB144, "Shift PS slot flags back", inline=True)
comment(0xB147, "Restore return address high", inline=True)
comment(0xB149, "Push onto stack", inline=True)
comment(0xB14A, "Restore return address low", inline=True)
comment(0xB14C, "Push onto stack", inline=True)
comment(0xB14D, "Delay counter: 10", inline=True)
comment(0xB151, "Outer loop counter = 10", inline=True)
comment(0xB153, "Decrement Y (inner loop)", inline=True)
comment(0xB154, "Inner loop: 10 iterations", inline=True)
comment(0xB156, "Decrement X (middle loop)", inline=True)
comment(0xB157, "Middle loop: 10 iterations", inline=True)
comment(0xB159, "Decrement outer counter", inline=True)
comment(0xB15B, "Outer loop: ~1000 delay cycles", inline=True)
comment(0xB15D, "Return", inline=True)

# write_ps_slot_byte_ff (&B13A) — write page + two &FF bytes
comment(0xB15E, "Advance Y", inline=True)
comment(0xB15F, "Get buffer page", inline=True)
comment(0xB161, "Store in workspace", inline=True)
comment(0xB163, "A=&FF", inline=True)
comment(0xB165, "Advance Y", inline=True)
comment(0xB166, "Write byte to workspace", inline=True)
comment(0xB168, "Advance Y", inline=True)
comment(0xB169, "Write byte to workspace", inline=True)
comment(0xB16B, "Advance Y", inline=True)
comment(0xB16C, "Return", inline=True)

# reverse_ps_name_to_tx (&B149) — reverse PS name for TX buffer
comment(0xB16D, "Start of PS name at offset &1C", inline=True)
comment(0xB16F, "Load byte from RX buffer", inline=True)
comment(0xB171, "Push to stack (for reversal)", inline=True)
comment(0xB172, "Next source byte", inline=True)
comment(0xB173, "End of PS name field (&20)?", inline=True)
comment(0xB175, "No: continue pushing", inline=True)
comment(0xB177, "End of TX name field at &1B", inline=True)
comment(0xB179, "Pop byte (reversed order)", inline=True)
comment(0xB17A, "Store in RX buffer", inline=True)
comment(0xB17C, "Previous position", inline=True)
comment(0xB17D, "Start of TX field (&0F)?", inline=True)
comment(0xB17F, "No: continue popping", inline=True)
comment(0xB181, "Copy RX page to TX", inline=True)
comment(0xB183, "Set TX pointer high", inline=True)
comment(0xB185, "TX offset &10", inline=True)
comment(0xB187, "Set TX pointer low", inline=True)
comment(0xB189, "Copy 4 header bytes", inline=True)
comment(0xB18B, "Get header template byte", inline=True)
comment(0xB18E, "Store in TX buffer", inline=True)
comment(0xB190, "Previous byte", inline=True)
comment(0xB191, "Loop until all 4 copied", inline=True)
comment(0xB193, "Return", inline=True)

# ps_tx_header_template (&B170): 4-byte PS transmit header.
comment(0xB194, "Printer server TX header template\n"
    "\n"
    "4-byte header copied to the TX control block by\n"
    "reverse_ps_name_to_tx. Sets up an immediate\n"
    "transmit on port &9F (PS port) to any station.")
comment(0xB194, "Control byte &80 (immediate TX)", inline=True)
comment(0xB195, "Port &9F (printer server)", inline=True)
comment(0xB196, "Station &FF (any)", inline=True)
comment(0xB197, "Network &FF (any)", inline=True)

# print_station_addr (&B174) — print net.station address
comment(0xB198, "Save V flag (controls padding)", inline=True)
comment(0xB199, "Get network number", inline=True)
comment(0xB19B, "Zero: no network prefix", inline=True)
comment(0xB19D, "Print network as 3 digits", inline=True)
comment(0xB1A0, "'.' separator", inline=True)
comment(0xB1A5, "Set V (suppress station padding)", inline=True)
comment(0xB1A8, "V set: skip padding spaces", inline=True)
comment(0xB1AA, "Print 4 spaces (padding)", inline=True)
comment(0xB1B1, "Get station number", inline=True)
comment(0xB1B3, "Restore flags", inline=True)
comment(0xB1B4, "Print station as 3 digits", inline=True)

# ps_slot_txcb_template (&B1B7): 12-byte TXCB template for PS slots.
# Accessed indirectly by init_ps_slot_from_rx (&B2C4) via:
#   LDA write_ps_slot_link_addr,Y  (base write_ps_slot_hi_link+1 + Y=&78 = &B1B7)
# This is the same 12-byte TXCB structure used by
# tx_econet_txcb_template (&AC6E) and rx_palette_txcb_template
# (&AC7A). Bytes at workspace offsets &7D and &81 (positions 5
# and 9: the hi bytes of the two buffer pointers) are
# substituted with net_rx_ptr_hi during the copy.
comment(0xB1B7, "PS slot transmit control block template\n"
    "\n"
    "12-byte Econet TXCB initialisation template for\n"
    "printer server slot buffers. Not referenced by\n"
    "label; accessed indirectly by init_ps_slot_from_rx\n"
    "via LDA write_ps_slot_link_addr,Y where the base\n"
    "address write_ps_slot_hi_link+1 plus Y offset &78 computes to &B1B7.\n"
    "\n"
    "Structure: 4-byte header (control, port, station,\n"
    "network) followed by two 4-byte buffer descriptors\n"
    "(lo address, hi page, end lo, end hi). The hi page\n"
    "bytes at positions 5 and 9 are overwritten with\n"
    "net_rx_ptr_hi during the copy to point into the\n"
    "actual RX buffer page. End bytes &FF are\n"
    "placeholders filled in later by the caller.")
comment(0xB1B7, "Control byte &80 (immediate TX)", inline=True)
comment(0xB1B8, "Port &9F (printer server)", inline=True)
comment(0xB1B9, "Station 0 (filled in later)", inline=True)
comment(0xB1BA, "Network 0 (filled in later)", inline=True)
comment(0xB1BC, "Data buffer start hi (= rx page)", inline=True)
comment(0xB1BD, "Data buffer end lo (placeholder)", inline=True)
comment(0xB1BE, "Data buffer end hi (placeholder)", inline=True)
comment(0xB1C0, "Reply buffer start hi (= rx page)", inline=True)
comment(0xB1C1, "Reply buffer end lo (placeholder)", inline=True)
comment(0xB1C2, "Reply buffer end hi (placeholder)", inline=True)

# cmd_bye (&948A) — *Bye: logoff from file server
comment(0x949E, "Y=0: close all files", inline=True)
comment(0x94A0, "Process all file control blocks", inline=True)
comment(0x94A3, "OSBYTE &77: close spool/exec", inline=True)
comment(0x94A8, "Close all network channels", inline=True)
comment(0x94AB, "Y=&17: *Bye function code", inline=True)

# save_net_tx_cb (&9499) — save state and build TX control block
comment(0x94AD, "Clear V (standard mode)", inline=True)
comment(0x94AE, "Copy FS station to TX control block", inline=True)
comment(0x94B1, "Store in TXCB", inline=True)
comment(0x94B4, "Clear carry", inline=True)
comment(0x94B5, "Save flags (carry = mode)", inline=True)
comment(0x94B6, "Store function code in TXCB", inline=True)
comment(0x94B9, "Copy 2 bytes (indices 0-1)", inline=True)
comment(0x94BB, "Load source byte", inline=True)
comment(0x94BE, "Store to TXCB", inline=True)
comment(0x94C1, "Next byte", inline=True)
comment(0x94C2, "Loop until all copied", inline=True)
comment(0x94C4, "Test library flag bits 6-7", inline=True)
comment(0x94C7, "Bit 6 set: use station as port", inline=True)
comment(0x94C9, "Bit 7 clear: skip port override", inline=True)
comment(0x94CB, "Bit 7 set: load alternative port", inline=True)
comment(0x94CE, "Override TXCB port byte", inline=True)
comment(0x94D3, "Bit 6: load station byte", inline=True)
comment(0x94D6, "Use station as TXCB port", inline=True)
comment(0x94D9, "Restore flags (carry = mode)", inline=True)

# prep_send_tx_cb (&94C6) — prepare TXCB and send
comment(0x94DA, "Save flags", inline=True)
comment(0x94DB, "Port &90: FS command port", inline=True)
comment(0x94DD, "Set reply port in TXCB", inline=True)
comment(0x94E0, "Initialise TXCB workspace", inline=True)
comment(0x94E3, "Get TXCB data end offset", inline=True)
comment(0x94E4, "Add 5 for header size", inline=True)
comment(0x94E6, "Set TXCB end pointer", inline=True)
comment(0x94E8, "Restore flags", inline=True)
comment(0x94E9, "C set: send disconnect instead", inline=True)
comment(0x94EB, "Save flags", inline=True)
comment(0x94EC, "Initialise TX pointer and send", inline=True)
comment(0x94EF, "Restore flags", inline=True)

# recv_and_process_reply (&94DC) — wait for reply and dispatch
comment(0x94F0, "Save flags", inline=True)
comment(0x94F1, "Set up receive TXCB", inline=True)
comment(0x94F4, "Wait for TX acknowledgment", inline=True)
comment(0x94F7, "Restore flags", inline=True)
comment(0x94F8, "Advance to next reply byte", inline=True)
comment(0x94F9, "Load reply byte", inline=True)
comment(0x94FB, "Save in X", inline=True)
comment(0x94FC, "Zero: no more replies, return", inline=True)
comment(0x94FE, "V clear: use code directly", inline=True)
comment(0x9500, "V set: adjust reply code (+&2B)", inline=True)
comment(0x9502, "Non-zero: process reply", inline=True)
comment(0x9504, "Return", inline=True)

# Disconnect path — send disconnect if carry was set
comment(0x9505, "Discard saved flags", inline=True)
comment(0x9506, "X=&C0: disconnect command", inline=True)
comment(0x9508, "Advance reply offset", inline=True)
comment(0x9509, "Send disconnect reply", inline=True)
comment(0x950C, "Successful: process next reply", inline=True)

# Process reply status — handle reply code and data loss
comment(0x950E, "Store reply status code", inline=True)
comment(0x9511, "Load pending operation marker", inline=True)
comment(0x9514, "Save pending operation flag (Z)", inline=True)
comment(0x9515, "Pending: go to data loss check", inline=True)
comment(0x9517, "Reply &BF (normal bye response)?", inline=True)
comment(0x9519, "No: build error from reply", inline=True)
comment(0x951B, "A=&40: initial data-loss flag", inline=True)
comment(0x951D, "Push data-loss accumulator", inline=True)
comment(0x951E, "Scan 16 channel entries (15 to 0)", inline=True)
comment(0x9520, "Pop accumulator", inline=True)
comment(0x9521, "OR in channel status bits", inline=True)
comment(0x9524, "Push updated accumulator", inline=True)
comment(0x9525, "Load channel status", inline=True)
comment(0x9528, "Keep only bits 6-7 (close flags)", inline=True)
comment(0x952A, "Clear data bits, keep state flags", inline=True)
comment(0x952D, "Advance to next channel slot", inline=True)
comment(0x9533, "Close all network channels", inline=True)
comment(0x952E, "Bit 7 set: more channels to scan", inline=True)
comment(0x9536, "Pop data-loss accumulator", inline=True)
comment(0x9530, "Store last channel scanned", inline=True)
comment(0x9537, "Bit 0 to carry (data lost?)", inline=True)
comment(0x9538, "No data lost: skip message", inline=True)
comment(0x953A, "Print 'Data Lost' + CR", inline=True)
comment(0x9547, "Reload reply status code", inline=True)
comment(0x954A, "Restore pending operation flag", inline=True)
comment(0x954D, "No pending: build error from reply", inline=True)
comment(0x954B, "No pending operation: build error", inline=True)
comment(0x954D, "Pending: clean up stack (3 bytes)", inline=True)
comment(0x954E, "(second byte)", inline=True)
comment(0x954F, "(third byte)", inline=True)
comment(0x9550, "Return to pending operation caller", inline=True)

# Build server error — copy error from server reply
comment(0x9551, "Y=1: error code offset in reply", inline=True)
comment(0x9553, "Reply code >= &A8?", inline=True)
comment(0x9555, "Yes: keep server error code", inline=True)
comment(0x9557, "No: use minimum error code &A8", inline=True)
comment(0x9559, "Overwrite error code in reply", inline=True)
comment(0x955B, "Y=&FF: pre-increment index", inline=True)
comment(0x955D, "Advance to next byte", inline=True)
comment(0x955E, "Load reply byte", inline=True)
comment(0x9560, "Copy to error block", inline=True)
comment(0x9563, "Is it CR (end of message)?", inline=True)
comment(0x9565, "No: copy next byte", inline=True)
comment(0x9567, "Store null terminator (A=0 from EOR)", inline=True)
comment(0x956A, "Get message length", inline=True)
comment(0x956B, "Transfer to A", inline=True)
comment(0x956C, "Length in X", inline=True)
comment(0x956D, "Go to error dispatch", inline=True)

# check_escape (&955A) — test for escape condition
comment(0x9570, "Load MOS escape flag", inline=True)
comment(0x9572, "Mask with escape-enabled flag", inline=True)
comment(0x9574, "No escape: return", inline=True)

# raise_escape_error (&9560) — acknowledge and raise escape error
comment(0x9576, "OSBYTE &7E: acknowledge escape", inline=True)
comment(0x957B, "Error class 6: Escape", inline=True)
comment(0x957D, "Classify as network error", inline=True)

# Remote station handler (&956A) — handle Econet remote control
comment(0x9580, "Offset 0: remote state byte", inline=True)
comment(0x9582, "Load remote state", inline=True)
comment(0x9584, "Zero: initialise remote session", inline=True)
comment(0x9586, "Non-zero: commit state and return", inline=True)
comment(0x9589, "Set bits 0,3: remote active flags", inline=True)
comment(0x958B, "Store updated remote state", inline=True)
comment(0x958D, "X=&80: flag for vector setup", inline=True)
comment(0x958F, "Offset &80 in RX buffer", inline=True)
comment(0x9591, "Load remote station low", inline=True)
comment(0x9593, "Save on stack", inline=True)
comment(0x9595, "Load remote station high", inline=True)
comment(0x9597, "Workspace offset &0F", inline=True)
comment(0x9599, "Store remote station high", inline=True)
comment(0x959B, "Y=&0E", inline=True)
comment(0x959C, "Restore remote station low", inline=True)
comment(0x959D, "Store remote station low", inline=True)
comment(0x959F, "Set up remote keyboard scanning", inline=True)
comment(0x95A2, "Initialise workspace copy", inline=True)
comment(0x95A5, "X=1: disable keyboard", inline=True)
comment(0x95A7, "Y=0", inline=True)
comment(0x95A9, "OSBYTE &C9: Econet keyboard disable", inline=True)
comment(0x95AE, "Commit state change", inline=True)
comment(0x95B1, "Error code 0", inline=True)
comment(0x95B3, "Generate 'Remoted' error", inline=True)

# Remote key injection (&95A8)
comment(0x95BE, "Offset 0: remote state byte", inline=True)
comment(0x95C0, "Load remote state", inline=True)
comment(0x95C2, "Zero: reinitialise session", inline=True)
comment(0x95C4, "Offset &80: station low", inline=True)
comment(0x95C6, "Load station low from RX", inline=True)
comment(0x95C8, "Workspace offset &0E", inline=True)
comment(0x95CA, "Compare with stored station", inline=True)
comment(0x95CC, "Different station: commit state", inline=True)
comment(0x95CE, "Offset &82: keypress byte", inline=True)
comment(0x95D0, "Load remote keypress", inline=True)
comment(0x95D2, "Key code to Y", inline=True)
comment(0x95D3, "X=0: keyboard buffer", inline=True)
comment(0x95D5, "Commit state change", inline=True)
comment(0x95D8, "OSBYTE &99: insert into buffer", inline=True)

# wait_net_tx_ack (&95DD) — poll TX status with 3-level timeout
comment(0x95DD, "Save TX timeout counter", inline=True)
comment(0x95E0, "Push (used as outer loop counter)", inline=True)
comment(0x95E1, "Save TX control state", inline=True)
comment(0x95E4, "Push (preserved during wait)", inline=True)
comment(0x95E5, "Check if TX in progress", inline=True)
comment(0x95E7, "Non-zero: skip force-wait", inline=True)
comment(0x95E9, "Set bit 7 to force wait mode", inline=True)
comment(0x95EB, "Store updated control state", inline=True)
comment(0x95EE, "A=0: initial counter values", inline=True)
comment(0x95F0, "Push inner loop counter", inline=True)
comment(0x95F1, "Push middle loop counter", inline=True)
comment(0x95F3, "X=SP for stack-relative DECs", inline=True)
comment(0x95F4, "Poll TX completion status", inline=True)
comment(0x95F6, "Bit 7 set: TX complete", inline=True)
comment(0x95F8, "Decrement inner counter", inline=True)
comment(0x95FB, "Not zero: keep polling", inline=True)
comment(0x95FD, "Decrement middle counter", inline=True)
comment(0x9600, "Not zero: keep polling", inline=True)
comment(0x9602, "Decrement outer counter", inline=True)
comment(0x9605, "Not zero: keep polling", inline=True)
comment(0x9607, "Discard inner counter", inline=True)
comment(0x9608, "Discard middle counter", inline=True)
comment(0x9609, "Restore l0d61 control state", inline=True)
comment(0x960A, "Write back TX control state", inline=True)
comment(0x960D, "Pop outer counter (0 if timed out)", inline=True)
comment(0x960E, "Zero: TX timed out", inline=True)
comment(0x9610, "Return (TX acknowledged)", inline=True)

# cond_save_error_code (&95FB) — conditionally store error code
comment(0x9611, "Test error logging flag", inline=True)
comment(0x9614, "Bit 7 clear: skip save", inline=True)
comment(0x9616, "Save error code to workspace", inline=True)
comment(0x9619, "Return", inline=True)

# TX timeout error builder (&9604) — build 'No reply' error
comment(0x961A, "X=8: 'No reply' error index", inline=True)
comment(0x961C, "Look up message table offset", inline=True)
comment(0x961F, "X=0: error text start", inline=True)
comment(0x9621, "Clear BRK byte in error block", inline=True)
comment(0x9624, "Load error number from table", inline=True)
comment(0x9627, "Conditionally save error code", inline=True)
comment(0x962A, "Load message byte", inline=True)
comment(0x962D, "Store in error text buffer", inline=True)
comment(0x9630, "Null terminator?", inline=True)
comment(0x9632, "Advance destination", inline=True)
comment(0x9633, "Advance source", inline=True)
comment(0x9634, "Loop until end of message", inline=True)
comment(0x9636, "Append ' net.station' to message", inline=True)
comment(0x9639, "A=0: null terminator", inline=True)
comment(0x963B, "Terminate error text", inline=True)
comment(0x963E, "Check and raise network error", inline=True)

# fixup_reply_status_a (&962B) — remap status 'A' to 'B'
comment(0x9641, "Load first reply byte", inline=True)
comment(0x9643, "Is it 'A' (status &41)?", inline=True)
comment(0x9645, "No: keep original", inline=True)
comment(0x9647, "Yes: change to 'B' (&42)", inline=True)
comment(0x9649, "Clear V flag", inline=True)

# load_reply_and_classify (&9636) — load reply and classify error
comment(0x964C, "Load first reply byte", inline=True)
# classify_reply_error (&9638) — main error classification
comment(0x964E, "Set V flag (via BIT &FF)", inline=True)
comment(0x9651, "Mask to error class (0-7)", inline=True)
comment(0x9653, "Save error class on stack", inline=True)
comment(0x9654, "Class 2 (station error)?", inline=True)
comment(0x9656, "No: build simple error message", inline=True)
comment(0x9658, "Save flags (V state for suffix)", inline=True)
comment(0x9659, "Error class to X", inline=True)
comment(0x965A, "Look up message table offset", inline=True)
comment(0x965D, "Load error number from table", inline=True)
comment(0x9660, "Conditionally save error code", inline=True)
comment(0x9663, "X=0: error text start", inline=True)
comment(0x9665, "Clear BRK byte", inline=True)
comment(0x9668, "Load message byte", inline=True)
comment(0x966B, "Store in error text", inline=True)
comment(0x966E, "Null terminator?", inline=True)
comment(0x9670, "Advance source", inline=True)
comment(0x9671, "Advance destination", inline=True)
comment(0x9672, "Loop until end of message", inline=True)
comment(0x9674, "Append ' net.station' suffix", inline=True)
comment(0x9677, "Restore flags", inline=True)
comment(0x9678, "V set: append 'not listening'", inline=True)
comment(0x967A, "Error code &A4", inline=True)
comment(0x967C, "Conditionally save error code", inline=True)
comment(0x967F, "Replace error number in block", inline=True)
comment(0x9682, "Y=&0B: 'not present' suffix index", inline=True)
comment(0x9686, "Y=9: 'not listening' suffix index", inline=True)
comment(0x9688, "Look up suffix table offset", inline=True)
comment(0x968B, "Offset to Y for indexing", inline=True)
comment(0x968C, "Load suffix byte", inline=True)
comment(0x968F, "Append to error text", inline=True)
comment(0x9692, "Null terminator?", inline=True)
comment(0x9694, "Advance source", inline=True)
comment(0x9695, "Advance destination", inline=True)
comment(0x9696, "Loop until end of suffix", inline=True)
comment(0x9698, "ALWAYS branch to error dispatch", inline=True)

# Simple error path — build error from class lookup
comment(0x969A, "Error class to X", inline=True)
comment(0x969B, "Look up message table offset", inline=True)
comment(0x969E, "X=0: error text start", inline=True)
comment(0x96A0, "Clear BRK byte", inline=True)
comment(0x96A3, "Load error number from table", inline=True)
comment(0x96A6, "Conditionally save error code", inline=True)
comment(0x96A9, "Load message byte", inline=True)
comment(0x96AC, "Store in error text", inline=True)
comment(0x96AF, "Null terminator? Go to error", inline=True)
comment(0x96B1, "Advance source", inline=True)
comment(0x96B2, "Advance destination", inline=True)
comment(0x96B3, "Loop until end of message", inline=True)

# cmd_fs (&A063) — *FS: select file server by number
comment(0xA07B, "Load current FS station high", inline=True)
comment(0xA07E, "Save to fs_work_5", inline=True)
comment(0xA080, "Load current FS station low", inline=True)
comment(0xA083, "Save to l00b6", inline=True)
comment(0xA085, "Get first character of argument", inline=True)
comment(0xA087, "Is it CR (no argument)?", inline=True)
comment(0xA089, "No arg: print current FS info", inline=True)
comment(0xA08B, "Parse FS/PS station arguments", inline=True)
comment(0xA08E, "A=1: write NFS info", inline=True)
comment(0xA090, "Store OSWORD sub-function", inline=True)
comment(0xA092, "OSWORD &13: NFS information", inline=True)
comment(0xA094, "Parameter block low", inline=True)
comment(0xA096, "Parameter block high", inline=True)

# Print current FS info
comment(0xA09B, "Print 'File server '", inline=True)
comment(0xA09E, "Set V (suppress padding)", inline=True)
comment(0xA0A1, "Print station address", inline=True)

# parse_fs_ps_args (&A08F) — parse net.station arguments for FS/PS
comment(0xA0A7, "Save X on stack", inline=True)
comment(0xA0A8, "Push X", inline=True)
comment(0xA0A9, "A=0: initialise dot-seen flag", inline=True)
comment(0xA0AB, "Clear dot-seen flag", inline=True)
comment(0xA0AD, "Parse first number (network)", inline=True)
comment(0xA0B0, "C set: number found, check for dot", inline=True)
comment(0xA0B2, "Save Y (command line offset)", inline=True)
comment(0xA0B3, "Push Y", inline=True)
comment(0xA0B4, "Initialise bridge polling", inline=True)
comment(0xA0B7, "Compare bridge result with parsed value", inline=True)
comment(0xA0B9, "Same: keep bridge result", inline=True)
comment(0xA0BB, "Different: use parsed value", inline=True)
comment(0xA0BD, "Store station low byte", inline=True)
comment(0xA0BF, "Restore Y", inline=True)
comment(0xA0C0, "Transfer back to Y", inline=True)
comment(0xA0C1, "Skip dot separator", inline=True)
comment(0xA0C2, "Parse second number (station)", inline=True)
comment(0xA0C5, "Zero result: skip store", inline=True)
comment(0xA0C7, "Store station high byte", inline=True)
comment(0xA0C9, "Restore X", inline=True)
comment(0xA0CA, "Transfer back to X", inline=True)
comment(0xA0CB, "Return", inline=True)

# get_pb_ptr_as_index (&A0B4) — convert PB pointer to 2-bit index
comment(0xA0CC, "Load parameter block pointer", inline=True)
# byte_to_2bit_index (&A0B6) — map byte to 2-bit index in Y
comment(0xA0CE, "Shift left (A * 2)", inline=True)
comment(0xA0CF, "Shift left (A * 4)", inline=True)
comment(0xA0D0, "Save A * 4 on stack", inline=True)
comment(0xA0D1, "Shift left (A * 8)", inline=True)
comment(0xA0D2, "Get stack pointer", inline=True)
comment(0xA0D3, "Save flags (carry from shift)", inline=True)
comment(0xA0D4, "A*8 + A*4 (from stack) = A*12", inline=True)
comment(0xA0D7, "Divide by 2 with carry", inline=True)
comment(0xA0D8, "Restore original flags", inline=True)
comment(0xA0D9, "Shift left again", inline=True)
comment(0xA0DA, "Result to Y as index", inline=True)
comment(0xA0DB, "Pop saved A * 4", inline=True)
comment(0xA0DC, "A * 4 >= &48 (out of range)?", inline=True)
comment(0xA0DE, "In range: return", inline=True)
comment(0xA0E0, "Out of range: Y=0", inline=True)
comment(0xA0E2, "A=&00", inline=True)
comment(0xA0E3, "Return with A=index, Y=index", inline=True)

# OSWORD read handler (&A0CC)
comment(0xA0E4, "Y=&6F: source offset", inline=True)
comment(0xA0E6, "Load byte from RX buffer", inline=True)
comment(0xA0E8, "C clear: store directly", inline=True)
comment(0xA0EA, "Get index from PB pointer", inline=True)
comment(0xA0ED, "C set (out of range): clear value", inline=True)
comment(0xA0EF, "Load workspace byte at index", inline=True)
comment(0xA0F1, "Is it '?' (uninitialised)?", inline=True)
comment(0xA0F3, "No: use value from RX buffer", inline=True)
comment(0xA0F5, "A=0: return zero for uninitialised", inline=True)
comment(0xA0F7, "Store result to PB pointer", inline=True)
comment(0xA0F9, "Return", inline=True)

# OSWORD write handler (&A0E2)
comment(0xA0FA, "Get index from PB pointer", inline=True)
comment(0xA0FD, "C clear: store to workspace", inline=True)
comment(0xA0FF, "Save carry to l0d6c bit 7", inline=True)
comment(0xA102, "Load PB pointer value", inline=True)
comment(0xA104, "Shift carry back in", inline=True)
comment(0xA105, "Restore l0d6c bit 7", inline=True)
comment(0xA108, "Return", inline=True)
comment(0xA109, "Save carry to l0d61 bit 7", inline=True)
comment(0xA10C, "A='?': mark as uninitialised", inline=True)
comment(0xA10E, "Store '?' to workspace", inline=True)
comment(0xA110, "Restore l0d61 bit 7", inline=True)
comment(0xA113, "Return", inline=True)

# cmd_fs_entry (&A0FC) — FS command dispatch entry
comment(0xA114, "Set text and transfer pointers", inline=True)
comment(0xA117, "Y=&FF: prepare for INY to 0", inline=True)
comment(0xA119, "Clear spool handle (no spool active)", inline=True)
comment(0xA11B, "Set escapable flag (&FF)", inline=True)
comment(0xA11E, "X=&4A: FS command table offset", inline=True)
comment(0xA120, "Match command in FS table", inline=True)
comment(0xA123, "C set: command found", inline=True)

# cmd_fs_reentry (&A10D)
comment(0xA125, "V clear: syntax error", inline=True)
# error_syntax (&A10F)
comment(0xA127, "Error code &DC", inline=True)
comment(0xA129, "Generate 'Syntax' error", inline=True)

# Dispatch matched command (&A11B)
comment(0xA133, "A=0: clear service state", inline=True)
comment(0xA135, "Store cleared service state", inline=True)
comment(0xA137, "Load command handler address high", inline=True)
comment(0xA13A, "Push high byte", inline=True)
comment(0xA13B, "Load command handler address low", inline=True)
comment(0xA13E, "Push low byte", inline=True)
comment(0xA13F, "RTS dispatches to command handler", inline=True)

# match_fs_cmd (&A128) — match command name in table
comment(0xA140, "Save Y (command line offset)", inline=True)
comment(0xA141, "Push on stack", inline=True)
comment(0xA142, "Restore saved Y", inline=True)
comment(0xA143, "Push back (keep on stack)", inline=True)
comment(0xA144, "Transfer to Y", inline=True)
comment(0xA145, "Load table entry byte", inline=True)
comment(0xA148, "Bit 7 set: end of table names", inline=True)

# Command name comparison loop
comment(0xA14A, "Load table byte", inline=True)
comment(0xA14D, "Bit 7 set: end of this name", inline=True)
comment(0xA14F, "Compare with command line char", inline=True)
comment(0xA151, "Case-insensitive compare", inline=True)
comment(0xA153, "Mismatch: skip to next entry", inline=True)
comment(0xA155, "Match: advance command line", inline=True)
comment(0xA156, "Advance table pointer", inline=True)
comment(0xA157, "Loop for next character", inline=True)

# Skip to next table entry on mismatch
comment(0xA159, "Advance past remaining table chars", inline=True)
comment(0xA15A, "Load next table byte", inline=True)
comment(0xA15D, "Bit 7 clear: more chars to skip", inline=True)
comment(0xA15F, "Check command line terminator", inline=True)
comment(0xA161, "Is it '.' (abbreviation)?", inline=True)
comment(0xA163, "Yes: skip spaces after dot", inline=True)

# Try next table entry
comment(0xA165, "X += 3: skip flags and address bytes", inline=True)
comment(0xA166, "(continued)", inline=True)
comment(0xA167, "(continued)", inline=True)
comment(0xA168, "Try next table entry", inline=True)

# End of table names — check separators
comment(0xA16A, "Save Y (end of matched name)", inline=True)
comment(0xA16B, "Push position", inline=True)
comment(0xA16C, "Load char after matched portion", inline=True)
comment(0xA16E, "Y=9: check 10 separator chars", inline=True)
comment(0xA170, "Compare with separator table", inline=True)
comment(0xA173, "Match: valid command separator", inline=True)
comment(0xA175, "Try next separator", inline=True)
comment(0xA176, "Loop through separator list", inline=True)
comment(0xA178, "No separator match: restore Y", inline=True)
comment(0xA179, "Transfer back to Y", inline=True)
comment(0xA17A, "Try next table entry", inline=True)
# sep_table_data (&A164) — command separator characters
comment(0xA17C, "Command separator table (9 bytes)\n"
    "\n"
    "Characters that terminate a command name in the\n"
    "star command parser. loop_check_sep_table scans\n"
    "Y down from 8 to 0, comparing each input char\n"
    "against this table.")
comment(0xA17C, "Space", inline=True)
comment(0xA17D, "'\"' double quote", inline=True)
comment(0xA17E, "'#' hash", inline=True)
comment(0xA17F, "'$' dollar", inline=True)
comment(0xA180, "'&' ampersand", inline=True)
comment(0xA181, "'*' asterisk", inline=True)
comment(0xA182, "':' colon", inline=True)
comment(0xA183, "'@' at-sign", inline=True)
comment(0xA184, "CR (carriage return)", inline=True)

# Valid separator found
comment(0xA185, "Restore saved Y", inline=True)
comment(0xA186, "Transfer to Y", inline=True)

# Skip spaces after command name
comment(0xA187, "Load next char", inline=True)
comment(0xA189, "Is it space?", inline=True)
comment(0xA18B, "No: done skipping", inline=True)
comment(0xA18D, "Advance past space", inline=True)
comment(0xA18E, "Loop for more spaces", inline=True)

# Check command flags
comment(0xA191, "Load command flags byte", inline=True)
comment(0xA194, "Shift: check 'no-arg' bit", inline=True)
comment(0xA195, "Bit clear: allow arguments", inline=True)
comment(0xA197, "Check if line ends here", inline=True)
comment(0xA199, "Is it CR?", inline=True)
comment(0xA19B, "No: argument present, V clear", inline=True)
comment(0xA19D, "CR found: set V (no argument)", inline=True)
comment(0xA1A0, "V set: command is valid", inline=True)
comment(0xA1A2, "Clear V (argument present)", inline=True)
comment(0xA1A3, "C=0: command not found", inline=True)
comment(0xA1A4, "Pop saved Y from stack", inline=True)
comment(0xA1A5, "Load command line char at Y", inline=True)
comment(0xA1A7, "Return (C and V set per result)", inline=True)

# No match in table — scan to next command word
comment(0xA1A8, "Advance past character", inline=True)
comment(0xA1A9, "Load current char", inline=True)
comment(0xA1AB, "Is it CR (end of line)?", inline=True)
comment(0xA1AD, "Yes: end of input", inline=True)
comment(0xA1AF, "Is it '.' (abbreviation dot)?", inline=True)
comment(0xA1B1, "Yes: skip to next word", inline=True)
comment(0xA1B3, "Is it space?", inline=True)
comment(0xA1B5, "No: keep scanning", inline=True)
comment(0xA1B7, "Skip past separator", inline=True)
comment(0xA1B8, "Load next char", inline=True)
comment(0xA1BA, "Is it space?", inline=True)
comment(0xA1BC, "Yes: skip consecutive spaces", inline=True)
comment(0xA1BE, "C=1: have more text to match", inline=True)

# FS command: save pointer and parse filename
comment(0xA1C1, "Save text pointer", inline=True)
comment(0xA1C4, "Set owner-only access mask", inline=True)
comment(0xA1C7, "Parse command argument (Y=0)", inline=True)

# Open file for command (&A1B2)
comment(0xA1CA, "X=1: buffer index", inline=True)
comment(0xA1CC, "Copy argument to buffer", inline=True)
comment(0xA1CF, "A=2: open for update", inline=True)
comment(0xA1D1, "Store open mode", inline=True)
comment(0xA1D4, "Y=&12: open file command", inline=True)
comment(0xA1D6, "Send open request to server", inline=True)
comment(0xA1D9, "Load reply status", inline=True)
comment(0xA1DC, "Status 1 (success)?", inline=True)
comment(0xA1DE, "No: file not found, try library", inline=True)

# Check if file handle is available
comment(0xA1E0, "X=3: check 4 handle bytes", inline=True)
comment(0xA1E2, "Increment handle byte", inline=True)
comment(0xA1E5, "Was &FF (overflow to 0): try next", inline=True)
comment(0xA1E7, "Non-zero: handle valid, execute", inline=True)
comment(0xA1EA, "Try next handle byte", inline=True)
comment(0xA1EB, "Loop until all checked", inline=True)
comment(0xA1ED, "Allocate new FCB or raise error", inline=True)
comment(0xA1F0, "X=1: open mode index", inline=True)
comment(0xA1F2, "Store in l0f05", inline=True)
comment(0xA1F5, "Store in l0f06", inline=True)
comment(0xA1F8, "X=2", inline=True)
comment(0xA1F9, "Copy argument to buffer", inline=True)
comment(0xA1FC, "Y=6: re-open command", inline=True)
comment(0xA1FE, "Send re-open request", inline=True)
comment(0xA201, "C set: error on re-open", inline=True)
comment(0xA203, "C clear: finalise file opening", inline=True)
comment(0xA206, "Jump to finalise and return", inline=True)

# File not found — try library path (&A1F1)
comment(0xA209, "Load first char of filename", inline=True)
comment(0xA20C, "Is it '$' (root dir)?", inline=True)
comment(0xA20E, "Yes: no library search, error", inline=True)
comment(0xA210, "Load library flag byte", inline=True)
comment(0xA213, "Bit 7 set: library already tried", inline=True)
comment(0xA215, "Rotate bits to check library state", inline=True)
comment(0xA216, "Rotate again", inline=True)
comment(0xA217, "Bit 7 set: restore from backup", inline=True)
comment(0xA219, "Carry set: bad command", inline=True)

# Shift filename right to prepend "Library."
comment(0xA21B, "X=&FF: pre-increment for loop", inline=True)
comment(0xA21D, "Find end of filename", inline=True)
comment(0xA21E, "Load filename byte", inline=True)
comment(0xA221, "Is it CR (end)?", inline=True)
comment(0xA223, "No: continue scanning", inline=True)
comment(0xA225, "Shift filename right by 8 bytes", inline=True)
comment(0xA228, "Store shifted byte", inline=True)
comment(0xA22B, "Previous byte", inline=True)
comment(0xA22C, "Loop until all shifted", inline=True)
comment(0xA22E, "X=7: 'Library.' is 8 bytes", inline=True)
comment(0xA230, "Copy 'Library.' prefix", inline=True)
comment(0xA233, "Store prefix byte", inline=True)
comment(0xA236, "Previous byte", inline=True)
comment(0xA237, "Loop until prefix copied", inline=True)
comment(0xA239, "Load library flag", inline=True)
comment(0xA23C, "Set bits 5-6: library path active", inline=True)
comment(0xA23E, "Store updated flag", inline=True)
comment(0xA241, "Retry file open with library path", inline=True)

# Restore original filename after library attempt
comment(0xA243, "X=&FF: pre-increment for loop", inline=True)
comment(0xA245, "Restore original filename", inline=True)
comment(0xA246, "Load backup byte", inline=True)
comment(0xA249, "Store to filename buffer", inline=True)
comment(0xA24C, "Is it CR (end)?", inline=True)
comment(0xA24E, "No: continue restoring", inline=True)
comment(0xA250, "Set owner-only access mask", inline=True)
comment(0xA253, "Set bit 7: library tried", inline=True)
comment(0xA255, "Store updated flag", inline=True)

# error_bad_command
comment(0xA25A, "Set owner-only access mask", inline=True)
comment(0xA25D, "Error code &FE", inline=True)
comment(0xA25F, "Generate 'Bad command' error", inline=True)

# Execute file with handle (&A252)
comment(0xA26A, "X=3: check 4 execution bytes", inline=True)
comment(0xA26C, "Increment execution address byte", inline=True)
comment(0xA26F, "Non-zero: valid, go to OSCLI", inline=True)
comment(0xA271, "Try next byte", inline=True)
comment(0xA272, "Loop until all checked", inline=True)
comment(0xA274, "Error code &93", inline=True)
comment(0xA276, "Generate 'No!' error", inline=True)

# Finalise file opening (&A265)
comment(0xA27D, "Load open mode result", inline=True)
comment(0xA280, "Allocate FCB slot", inline=True)
comment(0xA283, "Transfer to Y", inline=True)
comment(0xA284, "A=0: clear channel status", inline=True)
comment(0xA286, "Clear status in channel table", inline=True)
comment(0xA289, "Store handle in l1070", inline=True)
comment(0xA28C, "Y=3: OSCLI execution", inline=True)
comment(0xA28E, "Execute via boot/OSCLI path", inline=True)
comment(0xA299, "Copy command argument to buffer", inline=True)

# OSCLI argument parsing (&A281)
comment(0xA29C, "Y=0", inline=True)
comment(0xA29E, "C=0 for GSINIT", inline=True)
comment(0xA29F, "Initialise GS string read", inline=True)
comment(0xA2A2, "Read next GS character", inline=True)
comment(0xA2A5, "C clear: more chars", inline=True)
comment(0xA2A7, "Back up one position", inline=True)
comment(0xA2A8, "Skip trailing spaces", inline=True)
comment(0xA2A9, "Load next char", inline=True)
comment(0xA2AB, "Is it space?", inline=True)
comment(0xA2AD, "Yes: skip it", inline=True)
comment(0xA2AF, "Check for CR (end of line)", inline=True)
comment(0xA2B1, "C=0 for addition", inline=True)
comment(0xA2B2, "Transfer Y offset to A", inline=True)
comment(0xA2B3, "Add to text pointer low", inline=True)
comment(0xA2B5, "Store as command tail pointer low", inline=True)
comment(0xA2B8, "Load text pointer high", inline=True)
comment(0xA2BA, "Add carry", inline=True)
comment(0xA2BC, "Store as command tail pointer high", inline=True)
comment(0xA2BF, "Save text pointer for later", inline=True)
comment(0xA2C2, "X=&0E: OSWORD parameter offset", inline=True)
comment(0xA2C4, "Store as block offset high", inline=True)
comment(0xA2C6, "A=&0E: OSWORD parameter size", inline=True)
comment(0xA2C8, "Store as options pointer", inline=True)
comment(0xA2CA, "Store to l0e16", inline=True)
comment(0xA2CD, "X=&4A: FS command table offset", inline=True)
comment(0xA2CF, "Y=5", inline=True)
comment(0xA2D1, "Execute FS command iteration", inline=True)
comment(0xA2D4, "Load tube flag", inline=True)
comment(0xA2D7, "Zero: no tube transfer needed", inline=True)
comment(0xA2D9, "AND with l0f0b", inline=True)
comment(0xA2DC, "AND with l0f0c", inline=True)
comment(0xA2DF, "All &FF?", inline=True)
comment(0xA2E1, "Yes: no tube transfer needed", inline=True)
comment(0xA2E3, "Claim tube for data transfer", inline=True)
comment(0xA2E6, "X=9: parameter count", inline=True)
comment(0xA2E8, "Y=&0F: parameter offset", inline=True)
comment(0xA2EA, "A=4: tube transfer type", inline=True)
comment(0xA2EC, "Dispatch tube address/data", inline=True)
comment(0xA2EF, "A=1", inline=True)
comment(0xA2F1, "Dispatch via indirect vector", inline=True)

# find_fs_and_exit (&A2DC)
comment(0xA2F4, "Find station with bit 3 set", inline=True)
comment(0xA2F7, "Return with last flag state", inline=True)

# Unnamed: flip/set station boot (&A2E2)
comment(0xA2FA, "Flip/set station boot config", inline=True)
comment(0xA2FD, "Return with last flag state", inline=True)

# find_station_bit2 (&A2E8) — find station with bit 2 set
comment(0xA300, "X=&10: scan 16 slots (15 to 0)", inline=True)
comment(0xA302, "Clear V", inline=True)
comment(0xA303, "Try next slot", inline=True)
comment(0xA304, "All slots checked: not found", inline=True)
comment(0xA306, "Compare station/network", inline=True)
comment(0xA309, "No match: try next", inline=True)
comment(0xA30B, "Load slot status byte", inline=True)
comment(0xA30E, "Test bit 2 (PS active flag)?", inline=True)
comment(0xA310, "Not set: try next", inline=True)
comment(0xA312, "Transfer Y to A", inline=True)
comment(0xA313, "Store Y in slot data", inline=True)
comment(0xA316, "Set V (found match)", inline=True)
comment(0xA319, "Store Y to l0e02", inline=True)
comment(0xA31C, "V set: found, skip allocation", inline=True)
comment(0xA31E, "Transfer Y to A", inline=True)
comment(0xA31F, "Allocate FCB slot", inline=True)
comment(0xA322, "Store allocation result", inline=True)
comment(0xA325, "Zero: failed, restore context", inline=True)
comment(0xA327, "A=&26: station flags value", inline=True)

# find_station_bit3 (&A313) — find station with bit 3 set
comment(0xA32B, "X=&10: scan 16 slots (15 to 0)", inline=True)
comment(0xA32D, "Clear V", inline=True)
comment(0xA32E, "Try next slot", inline=True)
comment(0xA32F, "All slots checked: not found", inline=True)
comment(0xA331, "Compare station/network", inline=True)
comment(0xA334, "No match: try next", inline=True)
comment(0xA336, "Load slot status byte", inline=True)
comment(0xA339, "Test bit 3 (FS active flag)?", inline=True)
comment(0xA33B, "Not set: try next", inline=True)
comment(0xA33D, "Transfer Y to A", inline=True)
comment(0xA33E, "Store Y in slot data", inline=True)
comment(0xA341, "Set V (found match)", inline=True)
comment(0xA344, "Store Y to l0e03", inline=True)
comment(0xA347, "V set: found, skip allocation", inline=True)
comment(0xA349, "Transfer Y to A", inline=True)
comment(0xA34A, "Allocate FCB slot", inline=True)
comment(0xA34D, "Store allocation result", inline=True)
comment(0xA350, "Zero: failed, restore context", inline=True)
comment(0xA352, "A=&2A: station flags value", inline=True)

# print_inline gaps (&9132-&9154) — fill remaining items
comment(0x9146, "Store as string pointer low", inline=True)
comment(0x9149, "Store as string pointer high", inline=True)
comment(0x914B, "Y=0: index for indirect loads", inline=True)
comment(0x914F, "No page crossing", inline=True)
comment(0x9151, "Carry into high byte", inline=True)
comment(0x9157, "Save string pointer on stack", inline=True)
comment(0x9159, "(push low byte)", inline=True)
comment(0x915A, "Save pointer high byte", inline=True)
comment(0x915C, "(push high byte)", inline=True)
comment(0x9162, "Restore string pointer high", inline=True)
comment(0x9163, "Store pointer high", inline=True)
comment(0x9165, "Restore string pointer low", inline=True)
comment(0x9166, "Store pointer low", inline=True)
comment(0x9168, "Loop for next character", inline=True)

# &916E-&91F8 in 4.21_v1 is entirely syntax-string data and the
# cmd_syntax_table — there is no parse_addr_arg routine here. The 4.18
# carry-over comments for parse_addr_arg / accumulate-hex / accumulate-
# decimal landed inside string bytes and have been removed. parse_addr_arg
# in 4.21_v1, if it still exists, will live at a different address; finding
# it is a separate task.

# ============================================================
# print_*_no_spool inline comments (&91F9-&9235)
# ============================================================
comment(0x91F9, "A=&0D (CR) for OSASCI translation; fall through", inline=True)
comment(0x91FB, "Save caller's flags (V from caller is irrelevant — see &91FC)", inline=True)
comment(0x91FC, "BIT &FF unconditionally sets V=1 (bit 6 of operand)", inline=True)
comment(0x91FF, "V=1 always, branch always taken (skips the CLV path)", inline=True)
comment(0x9201, "Alt entry: save caller's flags BEFORE forcing V=0", inline=True)
comment(0x9202, "Force V=0 -> OSWRCH path at &9220 (raw byte)", inline=True)
comment(0x9203, "Save X", inline=True)
comment(0x9204, "Save Y", inline=True)
comment(0x9205, "Save A (the byte to print)", inline=True)
comment(0x9206, "Save inner P — V here picks OSASCI vs OSWRCH later", inline=True)
comment(0x9207, "OSBYTE 199 (read/write *SPOOL file handle)", inline=True)
comment(0x9209, "X=0: handle value to write", inline=True)
comment(0x920B, "Y=0: write mode (NEW = (OLD AND 0) EOR X = X = 0)", inline=True)
comment(0x920D, "Closes spool; X returns OLD handle", inline=True)
comment(0x9210, "OLD < ' '? (likely 0 = was already closed)", inline=True)
comment(0x9212, "Yes: leave spool closed for the print", inline=True)
comment(0x9214, "OLD >= '0'?", inline=True)
comment(0x9216, "Yes (>= &30): leave spool closed", inline=True)
comment(0x9218, "OLD in [&20,&2F] (NFS handle range): re-open spool with X=OLD", inline=True)
comment(0x921B, "Clear X for the post-print restore", inline=True)
comment(0x921D, "Restore inner P (V=1 OSASCI / V=0 OSWRCH)", inline=True)
comment(0x921E, "Pull A (the byte)", inline=True)
comment(0x921F, "Push it back so the final epilogue PLA still works", inline=True)
comment(0x9220, "V=0 -> OSWRCH (raw); V=1 -> OSASCI (CR translation)", inline=True)
comment(0x9222, "OSASCI: writes A, translating CR to CR/LF", inline=True)
comment(0x9225, "Skip OSWRCH branch", inline=True)
comment(0x9227, "OSWRCH: writes A as a raw byte", inline=True)
comment(0x922A, "OSBYTE 199 again to restore spool state", inline=True)
comment(0x922C, "Y=&FF (read mode): NEW = OLD EOR X", inline=True)
comment(0x922E, "X=0 -> no change; X=OLD -> writes OLD back", inline=True)
comment(0x9231, "Pull A (preserved across the call)", inline=True)
comment(0x9232, "Pull Y", inline=True)
comment(0x9233, "Pull X", inline=True)
comment(0x9234, "Pull caller's original flags", inline=True)
comment(0x9235, "Return", inline=True)

# is_decimal_digit (&9244) — test if char is decimal digit
# Also rejects '&' and '.' as non-decimal
comment(0x9258, "Is it '&' (hex prefix)?", inline=True)
comment(0x925A, "Yes: return C set (not decimal)", inline=True)
comment(0x925C, "Is it '.' (separator)?", inline=True)
comment(0x925E, "Yes: return C set (not decimal)", inline=True)
# is_dec_digit_only entry — pure digit test
comment(0x9260, "Above '9'?", inline=True)
comment(0x9262, "Yes: not a digit", inline=True)
comment(0x9264, "Below '0'? C clear if so", inline=True)
comment(0x9266, "Return: C set if '0'-'9'", inline=True)
comment(0x9267, "C=0: not a digit", inline=True)
comment(0x9268, "Return", inline=True)

# get_access_bits (&9255) — encode directory access byte
comment(0x9269, "Offset &0E in directory entry", inline=True)
comment(0x926B, "Load raw access byte", inline=True)
comment(0x926D, "Mask to 6 access bits", inline=True)
comment(0x926F, "X=4: start encoding at bit 4", inline=True)
comment(0x9271, "ALWAYS branch to encoder", inline=True)

# get_prot_bits (&925F) — encode protection attribute
comment(0x9273, "Mask to 5 protection bits", inline=True)
comment(0x9275, "X=&FF: start encoding at bit 0", inline=True)

# Shared encoder loop — maps source bits via lookup table
comment(0x9277, "Save remaining bits", inline=True)
comment(0x9279, "Clear encoded result", inline=True)
comment(0x927B, "Advance to next table position", inline=True)
comment(0x927C, "Shift out lowest source bit", inline=True)
comment(0x927E, "Bit clear: skip this position", inline=True)
comment(0x9280, "Bit set: OR in encoded value", inline=True)
comment(0x9283, "More bits to process", inline=True)
comment(0x9285, "Return encoded access in A", inline=True)

# prot_bit_encode_table (&9286) — bit remapping table
comment(0x9286, "Protection/access bit encode table\n"
    "\n"
    "11-entry lookup table used by get_prot_bits and\n"
    "get_access_bits to remap attribute bits between\n"
    "the file server protocol format and the local\n"
    "representation. The encoding loop shifts out each\n"
    "source bit; for each set bit, the corresponding\n"
    "table entry is ORed into the result.\n"
    "\n"
    "Indices 0-4: used by get_prot_bits (5-bit input).\n"
    "Some entries set multiple output bits (expansion).\n"
    "\n"
    "Indices 5-10: used by get_access_bits (6-bit input\n"
    "from directory entry offset &0E). Each entry sets\n"
    "exactly one output bit (pure permutation).")
# &9286-&9290 stale carry-over comments removed -- they were for
# prot_bit_encode_table entries that lived at these addresses in 4.18.
# The actual prot_bit_encode_table in 4.21_v1 is annotated wherever it
# now lives. Addresses &9286-&9290 here are inside print_inline's body.

# Stale 4.18 carry-overs (set_text_and_xfer_ptr, set_xfer_params,
# set_options_ptr, clear_escapable, cmp_5byte_handle) are at &93D3-
# &93F1 in 4.21 and have already been annotated there. Removing the
# misplaced duplicates at this address range.

# print_inline_no_spool inline comments (~22 items)
comment(0x928A, "Pop return-addr low byte (-> string pointer low)",
        inline=True)
comment(0x928B, "Save in fs_error_ptr (the loop's pointer low)",
        inline=True)
comment(0x928D, "Pop return-addr high byte", inline=True)
comment(0x928E, "Save in fs_crflag (the loop's pointer high)",
        inline=True)
comment(0x9290, "Y=0: indirect index for (fs_error_ptr),Y", inline=True)
comment(0x9292, "Step pointer low byte to next char", inline=True)
comment(0x9294, "No carry: skip high-byte INC", inline=True)
comment(0x9296, "Page wrap: bump pointer high", inline=True)
comment(0x9298, "Read next character from inline string", inline=True)
comment(0x929A, "Bit 7 set: terminator -- this byte is the next opcode",
        inline=True)
comment(0x929C, "Save pointer low (print_char_no_spool may clobber)",
        inline=True)
comment(0x929E, "Push it", inline=True)
comment(0x929F, "Save pointer high", inline=True)
comment(0x92A1, "Push it", inline=True)
comment(0x92A2, "Reload the character we're about to print", inline=True)
comment(0x92A4, "Print it via the *SPOOL-bypassing OSASCI wrapper",
        inline=True)
comment(0x92A7, "Pop pointer high back", inline=True)
comment(0x92A8, "Restore", inline=True)
comment(0x92AA, "Pop pointer low back", inline=True)
comment(0x92AB, "Restore", inline=True)
comment(0x92AD, "Always taken (BRA-style; A is non-zero from print)",
        inline=True)
comment(0x92AF, "Resume execution at the terminator byte's address "
        "(JMP indirect via fs_error_ptr)", inline=True)

# set_conn_active (&92A1) — set channel connection active flag
comment(0x92B5, "Save processor flags", inline=True)
comment(0x92B6, "Save A", inline=True)
comment(0x92B7, "Transfer X to A", inline=True)
comment(0x92B8, "Save original X", inline=True)
comment(0x92B9, "Get stack pointer", inline=True)
comment(0x92BA, "Read original A from stack", inline=True)
comment(0x92BD, "Convert to channel index", inline=True)
comment(0x92C0, "No channel found: skip", inline=True)
comment(0x92C2, "Bit 6: connection active flag", inline=True)
comment(0x92C4, "Set active flag in channel table", inline=True)
comment(0x92C7, "Store updated status", inline=True)
comment(0x92CA, "ALWAYS branch to exit", inline=True)

# clear_conn_active (&92B8) — clear channel connection active flag
comment(0x92CC, "Save processor flags", inline=True)
comment(0x92CD, "Save A", inline=True)
comment(0x92CE, "Transfer X to A", inline=True)
comment(0x92CF, "Save original X", inline=True)
comment(0x92D0, "Get stack pointer", inline=True)
comment(0x92D1, "Read original A from stack", inline=True)
comment(0x92D4, "Convert to channel index", inline=True)
comment(0x92D7, "No channel found: skip", inline=True)
comment(0x92D9, "Bit 6 clear mask (&BF = ~&40)", inline=True)
comment(0x92DB, "Clear active flag in channel table", inline=True)
comment(0x92DE, "Store updated status", inline=True)

# Shared exit for set/clear_conn_active
comment(0x92E1, "Restore X", inline=True)
comment(0x92E2, "Transfer back to X", inline=True)
comment(0x92E3, "Restore A", inline=True)
comment(0x92E4, "Restore processor flags", inline=True)
comment(0x92E5, "Return", inline=True)

# svc_8_osword (&A4D6): Service 8 — OSWORD dispatch
# Handles OSWORD &0E-&14: clock read, transmit, receive, etc.
# Primary dispatch via PHA/PHA/RTS from tables at &A508/&A50F

# Entry: validate OSWORD number and dispatch
comment(0xA4EE, "CLC so SBC subtracts value+1", inline=True)
comment(0xA4EF, "A = OSWORD number", inline=True)
comment(0xA4F1, "A = OSWORD - &0E (CLC+SBC = -&0E)", inline=True)
comment(0xA4F3, "Below &0E: not ours, return", inline=True)
comment(0xA4F5, "Index >= 7? (OSWORD > &14)", inline=True)
comment(0xA4F7, "Above &14: not ours, return", inline=True)
comment(0xA4F9, "X=OSWORD handler index (0-6)", inline=True)
comment(0xA509, "Set up dispatch and save state", inline=True)
comment(0xA4FA, "Y=6: save 6 workspace bytes", inline=True)

comment(0xA4FC, "Load current workspace byte", inline=True)
# Copy osword_flag to parameter block on return
comment(0xA4FF, "Save on stack", inline=True)
comment(0xA50C, "Y=&FA: restore 6 workspace bytes", inline=True)
comment(0xA50E, "Restore saved workspace byte", inline=True)
comment(0xA500, "Load OSWORD parameter byte", inline=True)
comment(0xA50F, "Store to osword_flag workspace", inline=True)
comment(0xA512, "Next byte", inline=True)
comment(0xA503, "Copy parameter to workspace", inline=True)
comment(0xA515, "Return from svc_8_osword", inline=True)
comment(0xA513, "Loop until all 6 restored", inline=True)
comment(0xA506, "Next byte down", inline=True)

comment(0xA507, "Loop for all 6 bytes", inline=True)
# osword_setup_handler: push handler address and save state
comment(0xA516, "X = OSWORD index (0-6)", inline=True)
comment(0xA516, "Load handler address high byte", inline=True)
comment(0xA519, "Push high byte for RTS dispatch", inline=True)
comment(0xA51A, "Load handler address low byte", inline=True)
comment(0xA51D, "Push low byte for RTS dispatch", inline=True)
comment(0xA51E, "Copy 3 bytes (Y=2,1,0)", inline=True)

# Save osword_flag to RX buffer (reverse of return copy)
comment(0xA520, "Load from osword_flag workspace", inline=True)
comment(0xA523, "Store to RX buffer", inline=True)
comment(0xA51E, "Load PB byte 0 (OSWORD sub-code)", inline=True)
comment(0xA520, "Clear service state", inline=True)
comment(0xA522, "RTS dispatches to pushed handler", inline=True)

# Dispatch tables at &A508 (lo) and &A50F (hi) are handled by
# rts_code_ptr() calls which produce symbolic label expressions.

# OSWORD &0E handler (&A516): read clock
# Copies clock data and converts binary to BCD
comment(0xA531, "Test station active flag", inline=True)
comment(0xA534, "Not active: just return", inline=True)
comment(0xA536, "Restore A (OSWORD sub-code)", inline=True)
comment(0xA536, "Sub-code = 4? (read clock)", inline=True)
comment(0xA538, "Yes: handle clock read", inline=True)
comment(0xA53A, "Other sub-codes: set state = 8", inline=True)
comment(0xA53C, "Store service state", inline=True)
comment(0xA53E, "Return", inline=True)

# Clock read handler (&A526): read time from workspace, convert to BCD
comment(0xA53F, "X=0: start of TX control block", inline=True)
comment(0xA541, "Y=&10: length of TXCB to save", inline=True)
comment(0xA543, "Save current TX control block", inline=True)
comment(0xA546, "Load seconds from clock workspace", inline=True)
comment(0xA549, "Convert binary to BCD", inline=True)
comment(0xA54C, "Store BCD seconds", inline=True)
comment(0xA54F, "Load minutes from clock workspace", inline=True)
comment(0xA552, "Convert binary to BCD", inline=True)
comment(0xA555, "Store BCD minutes", inline=True)
comment(0xA558, "Load hours from clock workspace", inline=True)
comment(0xA55B, "Convert binary to BCD", inline=True)
comment(0xA55E, "Store BCD hours", inline=True)
comment(0xA561, "Clear hours high position", inline=True)
comment(0xA563, "Store zero", inline=True)
comment(0xA566, "Load day+month byte", inline=True)
comment(0xA569, "Save for later high nibble extract", inline=True)
comment(0xA56A, "Load day value", inline=True)
comment(0xA56D, "Convert day to BCD", inline=True)
comment(0xA570, "Store BCD day", inline=True)
comment(0xA573, "Restore day+month byte", inline=True)
comment(0xA574, "Save again for month extract", inline=True)
comment(0xA575, "Mask low nibble (month low bits)", inline=True)
comment(0xA577, "Convert to BCD", inline=True)
comment(0xA57A, "Store BCD month", inline=True)
comment(0xA57D, "Restore day+month byte", inline=True)
comment(0xA57E, "Shift high nibble down", inline=True)
comment(0xA57F, "Continue shifting", inline=True)
comment(0xA580, "Continue shifting", inline=True)
comment(0xA581, "4th shift: isolate high nibble", inline=True)
comment(0xA582, "Add &51 for year offset + carry", inline=True)
comment(0xA584, "Convert year to BCD", inline=True)
comment(0xA587, "Store BCD year", inline=True)
comment(0xA58A, "Copy 7 bytes (Y=6 down to 0)", inline=True)

# Copy BCD result to OSWORD parameter block
comment(0xA58C, "Load BCD byte from workspace", inline=True)
comment(0xA58F, "Store to parameter block", inline=True)
comment(0xA591, "Next byte down", inline=True)
comment(0xA592, "Loop for all 7 bytes", inline=True)
comment(0xA594, "Return", inline=True)

# bin_to_bcd: convert binary value in A to BCD
comment(0xA595, "Save processor flags (decimal mode)", inline=True)
comment(0xA596, "X = binary count", inline=True)
comment(0xA597, "Zero: result is 0, skip loop", inline=True)
comment(0xA599, "Set decimal mode for BCD add", inline=True)
comment(0xA59A, "Start BCD result at 0", inline=True)
comment(0xA59C, "Clear carry for BCD add", inline=True)
comment(0xA59D, "Add 1 in decimal mode", inline=True)
comment(0xA59F, "Count down binary value", inline=True)
comment(0xA5A0, "Loop until zero", inline=True)
comment(0xA5A2, "Restore flags (clears decimal mode)", inline=True)
comment(0xA5A3, "Return with BCD result in A", inline=True)

# OSWORD &10 handler (&A58B): transmit
comment(0xA5A4, "Shift ws_0d60 left (status flag)", inline=True)
comment(0xA5A7, "A = Y (saved index)", inline=True)
comment(0xA5A8, "C=1: transmit active path", inline=True)
comment(0xA5AA, "C=0: store Y to parameter block", inline=True)
comment(0xA5AC, "Return (transmit not active)", inline=True)

# Transmit active: set up and begin
comment(0xA5AD, "Set workspace high byte", inline=True)
comment(0xA5AF, "Copy to ws_ptr_lo", inline=True)
comment(0xA5B1, "Also set as NMI TX block high", inline=True)
comment(0xA5B3, "Low byte = &6F", inline=True)
comment(0xA5B5, "Set osword_flag", inline=True)
comment(0xA5B7, "Set NMI TX block low", inline=True)
comment(0xA5B9, "X=&0F: byte count for copy", inline=True)
comment(0xA5BB, "Copy data and begin transmission", inline=True)
comment(0xA5BE, "Jump to begin Econet transmission", inline=True)
comment(0xA5C1, "Load NFS workspace page high byte", inline=True)
comment(0xA5C3, "Set workspace pointer high", inline=True)
comment(0xA5C5, "Set workspace pointer low from Y", inline=True)
comment(0xA5C7, "Rotate Econet flags (save interrupt state)", inline=True)
comment(0xA5CA, "Y=OSWORD flag (slot specifier)", inline=True)
comment(0xA5CB, "Store OSWORD flag", inline=True)
comment(0xA5CD, "Non-zero: use specified slot", inline=True)
comment(0xA5CF, "A=3: start searching from slot 3", inline=True)
comment(0xA5D1, "Convert slot to 2-bit workspace index", inline=True)
comment(0xA5D4, "C set: slot invalid, store result", inline=True)
comment(0xA5D6, "Shift index right (divide by 4)", inline=True)
comment(0xA5D7, "Continue shift", inline=True)
comment(0xA5D8, "Transfer to X as workspace offset", inline=True)
comment(0xA5D9, "Load workspace byte at offset", inline=True)
comment(0xA5DB, "Zero: slot empty, store result", inline=True)
comment(0xA5DD, "Compare with &3F ('?' marker)", inline=True)
comment(0xA5DF, "Match: slot found for receive", inline=True)
comment(0xA5E1, "Try next slot index", inline=True)
comment(0xA5E2, "Transfer back to A", inline=True)
comment(0xA5E3, "Loop back (A != 0)", inline=True)
comment(0xA5E5, "Transfer found slot to A", inline=True)
comment(0xA5E6, "X=0: index for indirect store", inline=True)
comment(0xA5E8, "Store slot number to PB byte 0", inline=True)
comment(0xA5EA, "Convert specified slot to workspace index", inline=True)
comment(0xA5ED, "C set: slot invalid, store result", inline=True)
comment(0xA5EF, "Y=Y-1: adjust workspace offset", inline=True)
comment(0xA5F0, "Update workspace pointer low", inline=True)
comment(0xA5F2, "A=&C0: slot active marker", inline=True)
comment(0xA5F4, "Y=1: workspace byte offset", inline=True)
comment(0xA5F6, "X=&0B: byte count for PB copy", inline=True)
comment(0xA5F8, "Compare Y with OSWORD flag", inline=True)
comment(0xA5FA, "Add workspace byte (check slot state)", inline=True)
comment(0xA5FC, "Zero: slot ready, copy PB and mark", inline=True)
comment(0xA5FE, "Negative: slot busy, increment and retry", inline=True)
comment(0xA600, "Clear carry for PB copy", inline=True)
comment(0xA601, "Copy PB byte to workspace slot", inline=True)
comment(0xA604, "C set: copy done, finish", inline=True)
comment(0xA606, "A=&3F: mark slot as pending ('?')", inline=True)
comment(0xA608, "Y=1: workspace flag offset", inline=True)
comment(0xA60A, "Store pending marker to workspace", inline=True)
comment(0xA60E, "Increment retry counter", inline=True)
comment(0xA610, "Non-zero: retry copy loop", inline=True)
comment(0xA612, "Decrement Y (adjust offset)", inline=True)
comment(0xA613, "Store result A to PB via Y", inline=True)
comment(0xA615, "Rotate Econet flags back (restore state)", inline=True)
comment(0xA618, "Return from OSWORD 11 handler", inline=True)

# store_osword_pb_ptr: store parameter block pointers to workspace

# store_ptr_at_ws_y: store 16-bit pointer to workspace

# OSWORD &12 handler (&A61C): receive setup
comment(0xA619, "Set workspace from RX ptr high", inline=True)
comment(0xA61B, "Store to ws_ptr_lo", inline=True)
comment(0xA61D, "Y=&7F: last byte of RX buffer", inline=True)
comment(0xA61F, "Load port/count from RX buffer", inline=True)
comment(0xA621, "Y=&80: set workspace pointer", inline=True)
comment(0xA622, "Store as osword_flag", inline=True)
comment(0xA624, "X = port/count value", inline=True)
comment(0xA625, "X-1: adjust count", inline=True)
comment(0xA626, "Y=0 for copy", inline=True)
comment(0xA628, "Copy workspace data", inline=True)
comment(0xA62B, "Update state and return", inline=True)

# osword_13_dispatch (&A631): dispatch by sub-code
comment(0xA62E, "X = sub-code", inline=True)
comment(0xA62F, "Sub-code < &13?", inline=True)
comment(0xA631, "Out of range: return", inline=True)
comment(0xA633, "Load handler address high byte", inline=True)
comment(0xA636, "Push high byte", inline=True)
comment(0xA637, "Load handler address low byte", inline=True)
comment(0xA63A, "Push low byte", inline=True)
comment(0xA63B, "RTS dispatches to handler", inline=True)

# OSWORD &13 dispatch table: lo bytes

# OSWORD &13 dispatch table: hi bytes
comment(0xA64E, "hi-sub 0: read FS station", inline=True)
comment(0xA64F, "hi-sub 1: set FS station", inline=True)
comment(0xA650, "hi-sub 2: read workspace pair", inline=True)
comment(0xA651, "hi-sub 3: write workspace pair", inline=True)
comment(0xA652, "hi-sub 4: read protection mask", inline=True)
comment(0xA653, "hi-sub 5: write protection mask", inline=True)
comment(0xA654, "hi-sub 6: read FCB handles", inline=True)
comment(0xA655, "hi-sub 7: set FCB handles", inline=True)
comment(0xA656, "hi-sub 8: read RX flag", inline=True)
comment(0xA657, "hi-sub 9: read RX port", inline=True)
comment(0xA658, "hi-sub 10: read error flag", inline=True)
comment(0xA659, "hi-sub 11: read context byte", inline=True)
comment(0xA65A, "hi-sub 12: read CSD path", inline=True)
comment(0xA65B, "hi-sub 13: write CSD path", inline=True)
comment(0xA65C, "hi-sub 14: read free buffers", inline=True)
comment(0xA65D, "hi-sub 15: read 3 context bytes", inline=True)
comment(0xA65E, "hi-sub 16: write 3 context bytes", inline=True)
comment(0xA65F, "hi-sub 17: query bridge status", inline=True)

# ca6fb: copy between workspace and parameter block
comment(0xA6F8, "C=0: skip PB-to-WS copy", inline=True)
comment(0xA6FA, "C=1: load from parameter block", inline=True)
comment(0xA6FC, "Store to workspace", inline=True)
comment(0xA6FE, "Load from workspace", inline=True)
comment(0xA700, "Store to parameter block", inline=True)
comment(0xA702, "Next byte", inline=True)
comment(0xA703, "Count down", inline=True)
comment(0xA704, "Loop for all bytes", inline=True)
comment(0xA706, "Return", inline=True)

# osword_13_read_station (&A663): sub 0 — read FS station
comment(0xA660, "NFS active?", inline=True)
comment(0xA663, "Yes: read station data", inline=True)
comment(0xA665, "No: return zero", inline=True)
comment(0xA668, "Y=2: copy 2 bytes", inline=True)
comment(0xA66A, "Load station byte", inline=True)
comment(0xA66D, "Store to PB[Y]", inline=True)
comment(0xA66F, "Previous byte", inline=True)
comment(0xA670, "Loop for bytes 2..1", inline=True)
comment(0xA672, "Return", inline=True)

# osword_13_set_station (&A676): sub 1 — set FS station
comment(0xA673, "NFS active?", inline=True)
comment(0xA676, "No: return zero", inline=True)
comment(0xA678, "Y=0 for process_all_fcbs", inline=True)
comment(0xA67A, "Close all open FCBs", inline=True)
comment(0xA67D, "Y=2: copy 2 bytes", inline=True)
comment(0xA67F, "Load new station byte from PB", inline=True)
comment(0xA681, "Store to l0dff", inline=True)
comment(0xA684, "Previous byte", inline=True)
comment(0xA685, "Loop for bytes 2..1", inline=True)
comment(0xA687, "Clear handles if station matches", inline=True)
comment(0xA68A, "X=&0F: scan 16 FCB entries", inline=True)
comment(0xA68C, "Load FCB flags", inline=True)
comment(0xA68F, "Save flags in Y", inline=True)
comment(0xA690, "Test bit 1 (FCB allocated?)", inline=True)
comment(0xA692, "No: skip to next entry", inline=True)
comment(0xA694, "Restore flags", inline=True)
comment(0xA695, "Clear bit 5 (pending update)", inline=True)
comment(0xA697, "Store updated flags", inline=True)
comment(0xA69A, "Save in Y", inline=True)
comment(0xA69B, "Does FCB match new station?", inline=True)
comment(0xA69E, "No match: skip to next", inline=True)
comment(0xA6A0, "Clear carry for ADC", inline=True)
comment(0xA6A1, "Restore flags", inline=True)
comment(0xA6A2, "Test bit 2 (handle 1 active?)", inline=True)
comment(0xA6A4, "No: check handle 2", inline=True)
comment(0xA6A6, "Restore flags", inline=True)
comment(0xA6A7, "Set bit 5 (handle reassigned)", inline=True)
comment(0xA6A9, "Save updated flags", inline=True)
comment(0xA6AA, "Get FCB high byte", inline=True)
comment(0xA6AD, "Store as handle 1 station", inline=True)
comment(0xA6B0, "FCB index", inline=True)
comment(0xA6B1, "Add &20 for FCB table offset", inline=True)
comment(0xA6B3, "Store as handle 1 FCB index", inline=True)
comment(0xA6B6, "Restore flags", inline=True)
comment(0xA6B7, "Test bit 3 (handle 2 active?)", inline=True)
comment(0xA6B9, "No: check handle 3", inline=True)
comment(0xA6BB, "Restore flags", inline=True)
comment(0xA6BC, "Set bit 5", inline=True)
comment(0xA6BE, "Save updated flags", inline=True)
comment(0xA6BF, "Get FCB high byte", inline=True)
comment(0xA6C2, "Store as handle 2 station", inline=True)
comment(0xA6C5, "FCB index", inline=True)
comment(0xA6C6, "Add &20 for FCB table offset", inline=True)
comment(0xA6C8, "Store as handle 2 FCB index", inline=True)
comment(0xA6CB, "Restore flags", inline=True)
comment(0xA6CC, "Test bit 4 (handle 3 active?)", inline=True)
comment(0xA6CE, "No: store final flags", inline=True)
comment(0xA6D0, "Restore flags", inline=True)
comment(0xA6D1, "Set bit 5", inline=True)
comment(0xA6D3, "Save updated flags", inline=True)
comment(0xA6D4, "Get FCB high byte", inline=True)
comment(0xA6D7, "Store as handle 3 station", inline=True)
comment(0xA6DA, "FCB index", inline=True)
comment(0xA6DB, "Add &20 for FCB table offset", inline=True)
comment(0xA6DD, "Store as handle 3 FCB index", inline=True)
comment(0xA6E0, "Store final flags for this FCB", inline=True)
comment(0xA6E1, "Update l1060[X]", inline=True)
comment(0xA6E4, "Next FCB entry", inline=True)
comment(0xA6E5, "Loop for all 16 entries", inline=True)
comment(0xA6E7, "Return", inline=True)

# osword_13_read_csd (&A6EB): sub 12 — read CSD path
comment(0xA6E8, "C=0: workspace-to-PB direction", inline=True)
comment(0xA6E9, "Skip SEC", inline=True)

# osword_13_write_csd (&A6EE): sub 13 — write CSD path
comment(0xA6EB, "C=1: PB-to-workspace direction", inline=True)
comment(0xA6EC, "Workspace offset &17", inline=True)
comment(0xA6EE, "Set ws_ptr_lo", inline=True)
comment(0xA6F0, "Page from RX pointer high byte", inline=True)
comment(0xA6F2, "Set ws_ptr_hi", inline=True)
comment(0xA6F4, "Y=1: first PB data byte", inline=True)
comment(0xA6F6, "X=5: copy 5 bytes", inline=True)

# osword_13_read_ws_pair (&A70A): sub 2 — read workspace bytes
comment(0xA707, "Load workspace page high byte", inline=True)
comment(0xA709, "Set ws_ptr_hi", inline=True)
comment(0xA70B, "Y=1", inline=True)
comment(0xA70C, "A=1", inline=True)
comment(0xA70D, "Set ws_ptr_lo = 1", inline=True)
comment(0xA70F, "X=1: copy 2 bytes", inline=True)
comment(0xA710, "C=0: workspace-to-PB direction", inline=True)
comment(0xA711, "Copy via copy_pb_byte_to_ws", inline=True)

# osword_13_write_ws_pair (&A716): sub 3 — write workspace bytes
comment(0xA713, "Y=1: first PB data byte", inline=True)
comment(0xA714, "Load PB[1]", inline=True)
comment(0xA716, "Y=2", inline=True)
comment(0xA717, "Store to (nfs_workspace)+2", inline=True)
comment(0xA719, "Load PB[2]", inline=True)
comment(0xA71B, "Y=3", inline=True)
comment(0xA71C, "Store to (nfs_workspace)+3", inline=True)
comment(0xA71E, "Reinitialise bridge routing", inline=True)
comment(0xA721, "Compare result with workspace", inline=True)
comment(0xA723, "Different: leave unchanged", inline=True)
comment(0xA725, "Same: clear workspace byte", inline=True)
comment(0xA727, "Return", inline=True)

# osword_13_read_prot (&A72B): sub 4 — read protection mask
comment(0xA728, "Load protection mask", inline=True)
comment(0xA72B, "Store to PB[1] and return", inline=True)

# osword_13_write_prot (&A731): sub 5 — write protection mask
comment(0xA72E, "Y=1: PB data offset", inline=True)
comment(0xA72F, "Load new mask from PB[1]", inline=True)
comment(0xA731, "Store via store_prot_mask", inline=True)

# osword_13_read_handles (&A737): sub 6 — read FCB handle info
comment(0xA734, "NFS active?", inline=True)
comment(0xA737, "No: return zero", inline=True)
comment(0xA739, "Y=3: copy 3 bytes", inline=True)
comment(0xA73B, "Load handle byte", inline=True)
comment(0xA73E, "Store to PB[Y]", inline=True)
comment(0xA740, "Previous byte", inline=True)
comment(0xA741, "Loop for bytes 3..1", inline=True)
comment(0xA743, "Return", inline=True)

# return_zero_in_pb (&A74C): return zero status
comment(0xA749, "A=0", inline=True)
comment(0xA74C, "Store 0 to PB[0]", inline=True)
comment(0xA74E, "Return", inline=True)

# osword_13_set_handles (&A747): sub 7 — validate and set FCB handles
comment(0xA744, "NFS active?", inline=True)
comment(0xA747, "Yes: process handles", inline=True)
comment(0xA74F, "Y=1: first handle in PB", inline=True)
comment(0xA751, "Load handle value from PB[Y]", inline=True)
comment(0xA753, "Must be >= &20", inline=True)
comment(0xA755, "Below range: invalid", inline=True)
comment(0xA757, "Must be < &30", inline=True)
comment(0xA759, "Above range: invalid", inline=True)
comment(0xA75B, "X = handle value", inline=True)
comment(0xA75C, "Load l1010[handle]", inline=True)
comment(0xA75F, "Non-zero: FCB exists", inline=True)
comment(0xA761, "Invalid: store 0 to PB[0]", inline=True)
comment(0xA764, "Clear PB[0] status", inline=True)
comment(0xA766, "Skip to next handle", inline=True)
comment(0xA768, "Load l1040[handle] flags", inline=True)
comment(0xA76B, "Test bit 1 (allocated?)", inline=True)
comment(0xA76D, "Not allocated: invalid", inline=True)
comment(0xA76F, "X = handle value", inline=True)
comment(0xA770, "Store handle to l1071+Y", inline=True)
comment(0xA773, "Load station from l1010", inline=True)
comment(0xA776, "Store station to l0e01+Y", inline=True)
comment(0xA779, "Is this handle 1 (Y=1)?", inline=True)
comment(0xA77B, "No: check handle 2", inline=True)
comment(0xA77D, "Save Y", inline=True)
comment(0xA77E, "Push Y", inline=True)
comment(0xA77F, "Bit mask &04 for handle 1", inline=True)
comment(0xA781, "Update flags across all FCBs", inline=True)
comment(0xA784, "Restore Y", inline=True)
comment(0xA785, "Back to Y", inline=True)
comment(0xA786, "Reload l1040 flags", inline=True)
comment(0xA789, "Set bits 2+5 (active+updated)", inline=True)
comment(0xA78B, "Store updated flags", inline=True)
comment(0xA78E, "Next handle slot", inline=True)
comment(0xA78F, "Done all 3 handles?", inline=True)
comment(0xA791, "No: process next handle", inline=True)
comment(0xA793, "Y=3 for return", inline=True)
comment(0xA794, "Return", inline=True)
comment(0xA795, "Is this handle 2 (Y=2)?", inline=True)
comment(0xA797, "No: must be handle 3", inline=True)
comment(0xA799, "Save Y", inline=True)
comment(0xA79A, "Push Y", inline=True)
comment(0xA79B, "Bit mask &08 for handle 2", inline=True)
comment(0xA79D, "Update flags across all FCBs", inline=True)
comment(0xA7A0, "Restore Y", inline=True)
comment(0xA7A1, "Back to Y", inline=True)
comment(0xA7A2, "Reload l1040 flags", inline=True)
comment(0xA7A5, "Set bits 3+5 (active+updated)", inline=True)
comment(0xA7A7, "Store updated flags", inline=True)
comment(0xA7AA, "Next handle slot", inline=True)
comment(0xA7AC, "Handle 3: save Y", inline=True)
comment(0xA7AD, "Push Y", inline=True)
comment(0xA7AE, "Bit mask &10 for handle 3", inline=True)
comment(0xA7B0, "Update flags across all FCBs", inline=True)
comment(0xA7B3, "Restore Y", inline=True)
comment(0xA7B4, "Back to Y", inline=True)
comment(0xA7B5, "Reload l1040 flags", inline=True)
comment(0xA7B8, "Set bits 4+5 (active+updated)", inline=True)
comment(0xA7BA, "Store updated flags", inline=True)
comment(0xA7BD, "Next handle slot", inline=True)

# update_fcb_flag_bits (&A7C2): update flags across FCB entries
comment(0xA7BF, "Save X (current FCB index)", inline=True)
comment(0xA7C0, "Push X", inline=True)
comment(0xA7C1, "X=&0F: scan 16 FCB entries", inline=True)
comment(0xA7C3, "Load FCB flags", inline=True)
comment(0xA7C6, "Shift bits 6-7 into bits 7-0", inline=True)
comment(0xA7C7, "Bit 6 now in bit 7 (N flag)", inline=True)
comment(0xA7C8, "Bit 6 clear: skip entry", inline=True)
comment(0xA7CA, "Restore Y (bit mask)", inline=True)
comment(0xA7CB, "Test mask bits against flags", inline=True)
comment(0xA7CE, "Zero: no matching bits", inline=True)
comment(0xA7D0, "Matching: restore Y", inline=True)
comment(0xA7D1, "Set bit 5 (updated)", inline=True)
comment(0xA7D3, "Skip clear path", inline=True)
comment(0xA7D5, "No match: restore Y", inline=True)
comment(0xA7D6, "Invert all bits", inline=True)
comment(0xA7D8, "Clear tested bits in flags", inline=True)
comment(0xA7DB, "Store updated flags", inline=True)
comment(0xA7DE, "Next FCB entry", inline=True)
comment(0xA7DF, "Loop for all 16 entries", inline=True)
comment(0xA7E1, "Restore original X", inline=True)
comment(0xA7E2, "Back to X", inline=True)
comment(0xA7E3, "Return", inline=True)

# osword_13_read_rx_flag (&A7E7): sub 8 — read RX flag
comment(0xA7E4, "Y=1: RX control block offset", inline=True)
comment(0xA7E6, "Load (net_rx_ptr)+1", inline=True)
comment(0xA7E8, "Y=0", inline=True)
comment(0xA7EA, "Store to PB[1] and return", inline=True)

# osword_13_read_rx_port (&A7F0): sub 9 — read RX port
comment(0xA7ED, "Y=&7F: port byte offset", inline=True)
comment(0xA7EF, "Load (net_rx_ptr)+&7F", inline=True)
comment(0xA7F1, "Y=1", inline=True)
comment(0xA7F3, "Store to PB[1]", inline=True)
comment(0xA7F6, "A=&80", inline=True)
comment(0xA7F8, "Store &80 to PB[2]", inline=True)
comment(0xA7FA, "Return", inline=True)

# osword_13_read_error (&A7FE): sub 10 — read error flag
comment(0xA7FB, "Load error flag", inline=True)
comment(0xA7FE, "Y=1: parameter block offset 1", inline=True)

comment(0xA7FF, "Store result to PB[1]", inline=True)
# osword_13_read_context (&A804): sub 11 — read context byte
comment(0xA801, "Return", inline=True)
comment(0xA802, "Load context byte", inline=True)
comment(0xA805, "Bit 7 clear: store context to PB", inline=True)

# osword_13_read_free_bufs (&A80A): sub 14 — free buffer count
comment(0xA807, "Total buffers = &6F", inline=True)
comment(0xA809, "Subtract used count", inline=True)
comment(0xA80A, "Free = &6F - l0d6b", inline=True)
comment(0xA80D, "Non-negative: store free count to PB", inline=True)

# store_a_to_pb_1 (&A810): store A to PB[1] and return
comment(0xA810, "Return", inline=True)

# osword_13_read_ctx_3 (&A814): sub 15 — read 3 context bytes
comment(0xA80F, "Next byte offset", inline=True)
comment(0xA810, "Load l0d6d[Y]", inline=True)
comment(0xA813, "Store to PB[Y]", inline=True)
comment(0xA815, "Done 3 bytes?", inline=True)
comment(0xA817, "No: loop", inline=True)
comment(0xA819, "Return", inline=True)

# osword_13_write_ctx_3 (&A81F): sub 16 — write 3 context bytes
comment(0xA81A, "Next byte offset", inline=True)
comment(0xA81B, "Load PB[Y]", inline=True)
comment(0xA81D, "Store to l0d6d[Y]", inline=True)
comment(0xA820, "Done 3 bytes?", inline=True)
comment(0xA822, "No: loop", inline=True)
comment(0xA824, "Return", inline=True)

# osword_13_bridge_query (&A82A): sub 17 — query bridge
comment(0xA825, "Poll for bridge", inline=True)
comment(0xA828, "Y=0", inline=True)
comment(0xA82A, "Load bridge status", inline=True)
comment(0xA82D, "Is it &FF (no bridge)?", inline=True)
comment(0xA82F, "No: bridge found", inline=True)
comment(0xA832, "PB[0] = 0 (no bridge)", inline=True)
comment(0xA837, "Y=1", inline=True)
comment(0xA838, "PB[1] = bridge status", inline=True)
comment(0xA83A, "Y=2", inline=True)
comment(0xA83B, "Y=3", inline=True)
comment(0xA83C, "Load PB[3] (caller value)", inline=True)
comment(0xA83E, "Zero: use default station", inline=True)
comment(0xA840, "Compare with bridge status", inline=True)
comment(0xA843, "Different: return unchanged", inline=True)
comment(0xA845, "Same: confirm station", inline=True)
comment(0xA847, "Load default from l0e01", inline=True)
comment(0xA84A, "Store to PB[3]", inline=True)
comment(0xA84C, "Return", inline=True)

# bridge_txcb_init_table (&A850) — bridge discovery templates
comment(0xA84D, "Bridge discovery init data (24 bytes)\n"
    "\n"
    "Two 12-byte templates copied simultaneously by\n"
    "loop_copy_bridge_init. X counts down &0B to 0,\n"
    "copying the TXCB template into &C0. Y counts up\n"
    "&18 to &23, copying the RXCB data into workspace\n"
    "via bridge_ws_init_data (compare_bridge_status+1)\n"
    "+ Y to reach the RXCB data area.\n"
    "\n"
    "The TX broadcasts \"BRIDGE\" as immediate data on\n"
    "port &9C to all stations (FF.FF). The RX listens\n"
    "on the same port for a reply into the bridge\n"
    "status bytes at &0D72.")
comment(0xA84D, "TX 0: ctrl = &82 (immediate mode)", inline=True)
comment(0xA84E, "TX 1: port = &9C (bridge discovery)", inline=True)
comment(0xA84F, "TX 2: dest station = &FF (broadcast)", inline=True)
comment(0xA850, "TX 3: dest network = &FF (all nets)", inline=True)
comment(0xA851, "TX 4-9: immediate data payload", inline=True)
comment(0xA857, "TX 10: &9C (port echo)", inline=True)
comment(0xA858, "TX 11: &00 (terminator)", inline=True)
comment(0xA859, "RX 0: ctrl = &7F (receive)", inline=True)
comment(0xA85A, "RX 1: port = &9C (bridge discovery)", inline=True)
comment(0xA85B, "RX 2: station = &00 (any)", inline=True)
comment(0xA85C, "RX 3: network = &00 (any)", inline=True)
comment(0xA85E, "RX 5: buf start hi (&0D) -> &0D72", inline=True)
comment(0xA85F, "RX 6: extended addr fill (&FF)", inline=True)
comment(0xA860, "RX 7: extended addr fill (&FF)", inline=True)
comment(0xA862, "RX 9: buf end hi (&0D) -> &0D74", inline=True)
comment(0xA863, "RX 10: extended addr fill (&FF)", inline=True)
comment(0xA864, "RX 11: extended addr fill (&FF)", inline=True)

# init_bridge_poll (&A868): initialise bridge polling
comment(0xA865, "Check bridge status", inline=True)
comment(0xA868, "Is it &FF (uninitialised)?", inline=True)
comment(0xA86A, "No: bridge already active, return", inline=True)
comment(0xA86C, "Save Y", inline=True)
comment(0xA86D, "Preserve Y on stack", inline=True)
comment(0xA86E, "Y=&18: workspace offset for init", inline=True)
comment(0xA870, "X=&0B: 12 bytes to copy", inline=True)
comment(0xA872, "Rotate l0d61 right (save flag)", inline=True)

# Copy bridge init data to workspace and TXCB
comment(0xA875, "Load init data byte", inline=True)
comment(0xA878, "Store to workspace", inline=True)
comment(0xA87A, "Load TXCB template byte", inline=True)
comment(0xA87D, "Store to TX control block", inline=True)
comment(0xA87F, "Next workspace byte", inline=True)
comment(0xA880, "Next template byte", inline=True)
comment(0xA881, "Loop for all 12 bytes", inline=True)
comment(0xA883, "Store X (-1) as bridge counter", inline=True)
comment(0xA886, "Restore l0d61 flag", inline=True)

# Poll loop: wait for line idle, transmit, check response
comment(0xA889, "Shift ws_0d60 left (check status)", inline=True)
comment(0xA88C, "C=0: status clear, retry", inline=True)
comment(0xA88E, "Control byte &82 for TX", inline=True)
comment(0xA890, "Set in TX control block", inline=True)
comment(0xA892, "Data block at &00C0", inline=True)
comment(0xA894, "Set NMI TX block low", inline=True)
comment(0xA896, "High byte = 0 (page 0)", inline=True)
comment(0xA898, "Set NMI TX block high", inline=True)
comment(0xA89A, "Begin Econet transmission", inline=True)

# Wait for TX complete
comment(0xA89D, "Test TX control block bit 7", inline=True)
comment(0xA89F, "Negative: TX still in progress", inline=True)
comment(0xA8A1, "Transfer TX completion status to A", inline=True)
comment(0xA8A2, "Save TX status", inline=True)
comment(0xA8A3, "OSBYTE &13: wait for VSYNC", inline=True)
comment(0xA8A5, "Wait for vertical sync", inline=True)
comment(0xA8A8, "Restore TX status", inline=True)
comment(0xA8A9, "Back to X", inline=True)
comment(0xA8AA, "Y=&18: check workspace response", inline=True)
comment(0xA8AC, "Load bridge response", inline=True)
comment(0xA8AE, "Negative: bridge responded", inline=True)
comment(0xA8B0, "Advance retry counter by 8", inline=True)
comment(0xA8B3, "Positive: retry poll loop", inline=True)

# Bridge response received
comment(0xA8B5, "Set response to &3F (OK)", inline=True)
comment(0xA8B7, "Store to workspace", inline=True)
comment(0xA8B9, "Restore saved Y", inline=True)
comment(0xA8BA, "Back to Y", inline=True)
comment(0xA8BB, "Load bridge status", inline=True)
comment(0xA8BE, "X = bridge status", inline=True)
comment(0xA8BF, "Complement status", inline=True)
comment(0xA8C1, "Status was &FF: return (no bridge)", inline=True)
comment(0xA8C3, "Return bridge station in A", inline=True)
comment(0xA8C4, "Return", inline=True)

# OSWORD &14 handler (&A8D0): network file operation
comment(0xA8C5, "Compare sub-code with 1", inline=True)
comment(0xA8C7, "Sub-code >= 1: handle TX request", inline=True)
comment(0xA8C9, "Test station active flag", inline=True)
comment(0xA8CC, "Not active: return", inline=True)
comment(0xA8CE, "Y=&23: workspace offset for params", inline=True)
comment(0xA8D0, "Set owner access mask", inline=True)

# Copy init_txcb template to workspace
comment(0xA8D3, "Load TXCB init byte", inline=True)
comment(0xA8D6, "Non-zero: use template value", inline=True)
comment(0xA8D8, "Zero: use workspace default value", inline=True)
comment(0xA8DB, "Store to workspace", inline=True)
comment(0xA8DD, "Next byte down", inline=True)
comment(0xA8DE, "Until Y reaches &17", inline=True)
comment(0xA8E0, "Loop for all bytes", inline=True)
comment(0xA8E2, "Y=&18 (INY from &17)", inline=True)
comment(0xA8E3, "Set net_tx_ptr low byte", inline=True)
comment(0xA8E5, "Y=&1C: workspace offset for PB pointer", inline=True)
comment(0xA8F6, "Store PB pointer to workspace", inline=True)
comment(0xA8E7, "Load PB page number", inline=True)
comment(0xA8F9, "Y=2: parameter offset", inline=True)
comment(0xA8E9, "PB starts at next page boundary (+1)", inline=True)
comment(0xA8FB, "Control byte &90", inline=True)
comment(0xA8EB, "Store PB start pointer at ws[&1C]", inline=True)
comment(0xA8FD, "Set escapable flag", inline=True)
comment(0xA8EE, "Y=1: PB byte 1 (transfer length)", inline=True)
comment(0xA8FF, "Store control byte to PB", inline=True)
comment(0xA8F0, "Load transfer length from PB", inline=True)
comment(0xA903, "Load workspace data", inline=True)
comment(0xA8F2, "Y=&20: workspace offset for buffer end", inline=True)
comment(0xA906, "Store to parameter block", inline=True)
comment(0xA8F4, "Add PB base for buffer end address", inline=True)
comment(0xA908, "Next byte", inline=True)
comment(0xA909, "Until Y reaches 7", inline=True)
comment(0xA90B, "Loop for 3 bytes (Y=4,5,6)", inline=True)
comment(0xA90D, "Set TX pointer high byte", inline=True)
comment(0xA90F, "Store to net_tx_ptr_hi", inline=True)
comment(0xA911, "Enable interrupts", inline=True)
comment(0xA911, "Send the network packet", inline=True)
comment(0xA914, "Y=&20: workspace offset", inline=True)
comment(0xA916, "Set to &FF (pending)", inline=True)
comment(0xA918, "Mark send pending in workspace", inline=True)
comment(0xA91B, "Also mark offset &21", inline=True)
comment(0xA91D, "Y=&19: control offset", inline=True)
comment(0xA91F, "Control byte &90", inline=True)
comment(0xA921, "Store to workspace", inline=True)
comment(0xA923, "Y=&18: RX control offset", inline=True)
comment(0xA924, "Control byte &7F", inline=True)
comment(0xA926, "Store RX control", inline=True)
comment(0xA928, "Wait for TX acknowledgement", inline=True)
comment(0xA92B, "Store address low byte at ws[Y]", inline=True)

comment(0xA92D, "Advance to high byte offset", inline=True)
# TX request handler (&A926)
comment(0xA92E, "Load high byte base (table_idx)", inline=True)
comment(0xA935, "Save processor flags", inline=True)
comment(0xA930, "Add carry for page crossing", inline=True)
comment(0xA936, "Y=1: PB offset for station", inline=True)
comment(0xA932, "Store address high byte at ws[Y+1]", inline=True)
comment(0xA938, "Load station number from PB", inline=True)
comment(0xA934, "Return", inline=True)
comment(0xA93A, "X = station number", inline=True)
comment(0xA93C, "Load network number from PB", inline=True)
comment(0xA93E, "Y=3: workspace start offset", inline=True)
comment(0xA93F, "Store Y as ws_ptr_lo", inline=True)
comment(0xA941, "Y=&72: workspace offset for dest", inline=True)
comment(0xA943, "Store network to workspace", inline=True)
comment(0xA945, "Y=&71", inline=True)
comment(0xA946, "A = station (from X)", inline=True)
comment(0xA947, "Store station to workspace", inline=True)
comment(0xA949, "Restore flags from PHP", inline=True)
comment(0xA94A, "Non-zero sub-code: handle burst", inline=True)

# Sub-code 0: character-by-character send loop
comment(0xA94C, "Load current offset", inline=True)
comment(0xA94E, "Advance offset for next byte", inline=True)
comment(0xA950, "Load next char from PB", inline=True)
comment(0xA952, "Zero: end of data, return", inline=True)
comment(0xA954, "Y=&7D: workspace char offset", inline=True)
comment(0xA956, "Store char to RX buffer", inline=True)
comment(0xA958, "Save char for later test", inline=True)
comment(0xA959, "Init workspace copy for wide xfer", inline=True)
comment(0xA95C, "Set carry for flag set", inline=True)
comment(0xA95F, "Enable IRQ and send packet", inline=True)
comment(0xA95D, "Set bit 7: Tube needs release", inline=True)

# Short delay loop
comment(0xA962, "Delay countdown", inline=True)
comment(0xA963, "Loop for short delay", inline=True)
comment(0xA965, "Restore char", inline=True)
comment(0xA966, "Test if char was CR (&0D)", inline=True)
comment(0xA968, "Not CR: send next char", inline=True)
comment(0xA96A, "CR sent: return", inline=True)

# Sub-code != 0: burst transmit (&A959)
comment(0xA96B, "Init workspace for wide copy", inline=True)
comment(0xA96E, "Y=&7B: workspace offset", inline=True)
comment(0xA970, "Load buffer size", inline=True)
comment(0xA972, "Add 3 for header", inline=True)
comment(0xA974, "Store adjusted size", inline=True)

# enable_irq_and_poll
comment(0xA976, "Enable interrupts", inline=True)
comment(0xA977, "Send packet and return", inline=True)

# Dispatch interceptor (&A968): hook into OSWORD processing
comment(0xA97A, "Save processor flags", inline=True)
comment(0xA97B, "Save A", inline=True)
comment(0xA97C, "Save X", inline=True)
comment(0xA97D, "Push X", inline=True)
comment(0xA97E, "Save Y", inline=True)
comment(0xA97F, "Push Y", inline=True)
comment(0xA980, "Get stack pointer", inline=True)
comment(0xA981, "Read OSWORD number from stack", inline=True)
comment(0xA984, "OSWORD >= 9?", inline=True)
comment(0xA986, "Yes: out of range, restore + return", inline=True)
comment(0xA988, "X = OSWORD number", inline=True)
comment(0xA989, "Push handler address for dispatch", inline=True)

# Restore registers and return
comment(0xA98C, "Restore Y", inline=True)
comment(0xA98D, "Back to Y", inline=True)
comment(0xA98E, "Restore X", inline=True)
comment(0xA98F, "Back to X", inline=True)
comment(0xA990, "Restore A", inline=True)
comment(0xA991, "Restore processor flags", inline=True)
comment(0xA992, "RTS dispatches via pushed address", inline=True)

# push_osword_handler_addr
comment(0xA993, "Load handler high byte from table", inline=True)
comment(0xA996, "Push for RTS dispatch", inline=True)
comment(0xA997, "Load handler low byte from table", inline=True)
comment(0xA99A, "Push for RTS dispatch", inline=True)
comment(0xA99B, "Reload OSWORD number for handler", inline=True)
comment(0xA99D, "RTS will dispatch to handler", inline=True)

# tx_econet_abort: send abort to remote station
comment(0xA9BE, "Y=&D9: workspace abort offset", inline=True)
comment(0xA9C0, "Store abort code to workspace", inline=True)
comment(0xA9C2, "Control byte &80 (abort)", inline=True)
comment(0xA9C4, "Y=&0C: control offset", inline=True)
comment(0xA9C6, "Store control byte", inline=True)
comment(0xA9C8, "Save current TX ptr low", inline=True)
comment(0xA9CA, "Push on stack", inline=True)
comment(0xA9CB, "Save current TX ptr high", inline=True)
comment(0xA9CD, "Push on stack", inline=True)
comment(0xA9CE, "Set TX ptr to workspace offset", inline=True)
comment(0xA9D0, "Load workspace high byte", inline=True)
comment(0xA9D2, "Set TX ptr high", inline=True)
comment(0xA9D4, "Send the abort packet", inline=True)
comment(0xA9D7, "Set status to &3F (complete)", inline=True)
comment(0xA9D9, "Store at TX ptr offset 0", inline=True)
comment(0xA9DB, "Restore TX ptr high", inline=True)
comment(0xA9DC, "Back to net_tx_ptr_hi", inline=True)
comment(0xA9DE, "Restore TX ptr low", inline=True)
comment(0xA9DF, "Back to net_tx_ptr", inline=True)
comment(0xA9E1, "Return", inline=True)

# netv_claim_release (&A9D0): OSWORD 7 handler
comment(0xA9E2, "Load PB pointer high", inline=True)
comment(0xA9E4, "Compare with &81 (special case)", inline=True)
comment(0xA9E6, "Match: skip to processing", inline=True)
comment(0xA9E8, "Y=1: first claim code position", inline=True)
comment(0xA9EA, "X=&0A: 11 codes to check", inline=True)
comment(0xA9EC, "Search claim code table", inline=True)
comment(0xA9EF, "Found: skip to processing", inline=True)
comment(0xA9F1, "Try second table range", inline=True)
comment(0xA9F2, "Y=-1: flag second range", inline=True)
comment(0xA9F3, "X=&11: 18 codes to check", inline=True)
comment(0xA9F5, "Search claim code table", inline=True)
comment(0xA9F8, "Found: skip to processing", inline=True)
comment(0xA9FA, "Not found: increment Y", inline=True)

# Process claim result
comment(0xA9FB, "X=2: default state", inline=True)
comment(0xA9FD, "A = Y (search result)", inline=True)
comment(0xA9FE, "Zero: not found, return", inline=True)
comment(0xAA00, "Save result flags", inline=True)
comment(0xAA01, "Positive: use state X=2", inline=True)
comment(0xAA04, "Y=&DC: workspace offset for save", inline=True)

# Save tube claim data to workspace
comment(0xAA06, "Load tube claim ID byte", inline=True)
comment(0xAA09, "Store to workspace", inline=True)
comment(0xAA0B, "Next byte down", inline=True)
comment(0xAA0C, "Until Y reaches &DA", inline=True)
comment(0xAA0E, "Loop for 3 bytes", inline=True)
comment(0xAA10, "A = state (2 or 3)", inline=True)
comment(0xAA11, "Send abort with state code", inline=True)
comment(0xAA14, "Restore flags", inline=True)
comment(0xAA15, "Positive: return without poll", inline=True)
comment(0xAA17, "Set control to &7F", inline=True)
comment(0xAA19, "Y=&0C: control offset", inline=True)
comment(0xAA1B, "Store control byte", inline=True)

# Wait for response
comment(0xAA1D, "Load status from workspace", inline=True)
comment(0xAA1F, "Positive: keep waiting", inline=True)
comment(0xAA21, "Get stack pointer", inline=True)
comment(0xAA22, "Y=&DD: workspace result offset", inline=True)
comment(0xAA24, "Load result byte", inline=True)
comment(0xAA26, "Set bit 6 and bit 2", inline=True)
comment(0xAA28, "Always branch (NZ from ORA)", inline=True)

# Copy result back to caller's stack
comment(0xAA2A, "Previous workspace byte", inline=True)
comment(0xAA2B, "Previous stack position", inline=True)
comment(0xAA2C, "Load workspace byte", inline=True)
comment(0xAA2E, "Store to caller's stack frame", inline=True)
comment(0xAA31, "Reached start of save area?", inline=True)
comment(0xAA33, "No: copy next byte", inline=True)
comment(0xAA35, "Return", inline=True)

# match_rx_code (&AA24): search claim code table
comment(0xAA36, "Compare A with code at index X", inline=True)
comment(0xAA39, "Match: return with Z set", inline=True)
comment(0xAA3B, "Try next code", inline=True)
comment(0xAA3C, "More codes: continue search", inline=True)
comment(0xAA3E, "Return (Z clear = not found)", inline=True)

# osword_claim_codes (&AA2D): 18-byte OSWORD number table.
# Searched by match_rx_code from the OSWORD 7 dispatch handler.
# Two search ranges select different processing paths:
#   Range 1 (indices 0-&0A, 11 entries): match → Y=1 → state 2
#   Range 2 (indices 0-&11, all 18):     match → Y=-1 → state 3
# No match → Y=0 → return without action.
comment(0xAA3F, "OSWORD claim code table\n"
    "\n"
    "Table of OSWORD numbers that trigger NMI\n"
    "claim processing. Searched in two passes by\n"
    "the OSWORD 7 handler: first the 11-entry\n"
    "range (indices 0-&0A), then the full 18-entry\n"
    "range (indices 0-&11). A match in the first\n"
    "range sets state 2 (standard claim); a match\n"
    "only in the extended range sets state 3.")
comment(0xAA3F, "Range 1+2: OSWORD &04", inline=True)
comment(0xAA40, "Range 1+2: OSWORD &09", inline=True)
comment(0xAA41, "Range 1+2: OSWORD &0A", inline=True)
comment(0xAA42, "Range 1+2: OSWORD &14", inline=True)
comment(0xAA43, "Range 1+2: OSWORD &15", inline=True)
comment(0xAA44, "Range 1+2: OSWORD &9A", inline=True)
comment(0xAA45, "Range 1+2: OSWORD &9B", inline=True)
comment(0xAA46, "Range 1+2: OSWORD &E1", inline=True)
comment(0xAA47, "Range 1+2: OSWORD &E2", inline=True)
comment(0xAA48, "Range 1+2: OSWORD &E3", inline=True)
comment(0xAA49, "Range 1+2: OSWORD &E4", inline=True)
comment(0xAA4A, "Range 2 only: OSWORD &0B", inline=True)
comment(0xAA4B, "Range 2 only: OSWORD &0C", inline=True)
comment(0xAA4C, "Range 2 only: OSWORD &0F", inline=True)
comment(0xAA4D, "Range 2 only: OSWORD &79", inline=True)
comment(0xAA4E, "Range 2 only: OSWORD &7A", inline=True)
comment(0xAA4F, "Range 2 only: OSWORD &86", inline=True)
comment(0xAA50, "Range 2 only: OSWORD &87", inline=True)

# osword_8_handler (&AA3F): OSWORD 7/8 — copy PB and abort
comment(0xAA51, "Y=&0E: copy 15 bytes (0-14)", inline=True)
comment(0xAA53, "OSWORD 7?", inline=True)
comment(0xAA55, "Yes: handle", inline=True)
comment(0xAA57, "OSWORD 8?", inline=True)
comment(0xAA59, "No: return", inline=True)
comment(0xAA5B, "Workspace low = &DB", inline=True)
comment(0xAA5D, "Set nfs_workspace low byte", inline=True)
comment(0xAA5F, "Load PB[Y]", inline=True)
comment(0xAA61, "Store to workspace[Y]", inline=True)
comment(0xAA63, "Next byte down", inline=True)
comment(0xAA64, "Loop for 15 bytes", inline=True)
comment(0xAA66, "Y=0", inline=True)
comment(0xAA67, "Workspace low = &DA", inline=True)
comment(0xAA69, "Load OSWORD number", inline=True)
comment(0xAA6B, "Store at workspace+0 (= &DA)", inline=True)
comment(0xAA6D, "Workspace low = 0 (restore)", inline=True)
comment(0xAA6F, "Y=&14: control offset", inline=True)
comment(0xAA71, "Control value &E9", inline=True)
comment(0xAA73, "Store to workspace+&14", inline=True)
comment(0xAA75, "Abort code = 1", inline=True)
comment(0xAA77, "Send abort packet", inline=True)
comment(0xAA7A, "Restore nfs_workspace low", inline=True)

# osword_4_handler (&A99E): OSWORD 4 — clear carry, abort
comment(0xA9B0, "Get stack pointer", inline=True)
comment(0xA9B1, "Clear bit 0 of stacked P (carry)", inline=True)
comment(0xA9B4, "Shift back (clears carry flag)", inline=True)
comment(0xA9B7, "A = original Y", inline=True)
comment(0xA9B8, "Y=&DA: workspace offset", inline=True)
comment(0xA9BA, "Store Y to workspace", inline=True)
comment(0xA9BC, "Abort code = 0", inline=True)

# init_ws_copy_wide: copy template to workspace (wide mode)
comment(0xAA7C, "X=&0D: 14 bytes to copy", inline=True)
comment(0xAA7E, "Y=&7C: workspace destination offset", inline=True)
comment(0xAA80, "Test bit 6 via BIT (V flag check)", inline=True)
comment(0xAA83, "V=1: skip to wide mode copy", inline=True)

# init_ws_copy_narrow: copy template to workspace (narrow mode)
comment(0xAA85, "Y=&17: narrow mode dest offset", inline=True)
comment(0xAA87, "X=&1A: 27 bytes to copy", inline=True)
comment(0xAA89, "Clear V flag for narrow mode", inline=True)

# Template copy loop with special marker handling
comment(0xAA8A, "Load template byte", inline=True)
comment(0xAA8D, "Is it &FE? (end marker)", inline=True)
comment(0xAA8F, "Yes: finished, set TX ptr", inline=True)
comment(0xAA91, "Is it &FD? (skip marker)", inline=True)
comment(0xAA93, "Yes: skip store, just advance", inline=True)
comment(0xAA95, "Is it &FC? (page ptr marker)", inline=True)
comment(0xAA97, "No: use literal value", inline=True)
comment(0xAA99, "&FC: load RX buffer page", inline=True)
comment(0xAA9B, "V=1: use net_rx_ptr_hi", inline=True)
comment(0xAA9D, "V=0: use nfs_workspace_hi", inline=True)
comment(0xAA9F, "Store as TX ptr high", inline=True)
comment(0xAAA1, "V=1: store to net_rx_ptr target", inline=True)
comment(0xAAA3, "V=0: store to nfs_workspace", inline=True)
comment(0xAAA5, "Continue to next byte", inline=True)
comment(0xAAA7, "V=1: store to net_rx_ptr", inline=True)
comment(0xAAA9, "Advance workspace offset down", inline=True)
comment(0xAAAA, "Advance template index", inline=True)
comment(0xAAAB, "More bytes: continue copy", inline=True)

# End: set TX pointer
comment(0xAAAD, "Adjust Y for start of TX data", inline=True)
comment(0xAAAE, "Set net_tx_ptr from Y", inline=True)
comment(0xAAB0, "Return", inline=True)
# ws_txcb_template_data (&AA9F): 39-byte workspace init template.
# Three overlapping regions shared via indexed access:
#   Wide  (init_ws_copy_wide):    X=&0D → bytes [0..13]
#   Narrow (init_ws_copy_narrow): X=&1A → bytes [14..26]
#   Spool (process_spool_data):   X=&26 → bytes [27..38]
# Markers: &FE=end, &FD=skip, &FC=page pointer.
comment(0xAAB1, "Workspace TXCB init template\n"
    "\n"
    "39-byte template with three overlapping\n"
    "regions, each a TXCB/RXCB structure:\n"
    "  Wide  [0..13]:  ws+&6F..&7C via net_rx_ptr\n"
    "  Narrow [14..26]: ws+&0C..&17 via workspace\n"
    "  Spool [27..38]:  ws+&01..&0B via workspace\n"
    "Markers: &FE=end, &FD=skip, &FC=page ptr.")
comment(0xAAB1, "Wide &6F: ctrl=&85", inline=True)
comment(0xAAB2, "Wide &70: port=&00", inline=True)
comment(0xAAB3, "Wide &71: skip (dest station)", inline=True)
comment(0xAAB4, "Wide &72: skip (dest network)", inline=True)
comment(0xAAB5, "Wide &73: buf start lo=&7D", inline=True)
comment(0xAAB6, "Wide &74: buf start hi=page ptr", inline=True)
comment(0xAAB7, "Wide &75: buf start ext lo", inline=True)
comment(0xAAB8, "Wide &76: buf start ext hi", inline=True)
comment(0xAAB9, "Wide &77: buf end lo=&7E", inline=True)
comment(0xAABA, "Wide &78: buf end hi=page ptr", inline=True)
comment(0xAABB, "Wide &79: buf end ext lo", inline=True)
comment(0xAABC, "Wide &7A: buf end ext hi", inline=True)
comment(0xAABD, "Wide &7B: zero", inline=True)
comment(0xAABE, "Wide &7C: zero", inline=True)
comment(0xAABF, "Narrow stop (&FE terminator)", inline=True)
comment(0xAAC0, "Narrow &0C: ctrl=&80 (standard)", inline=True)
comment(0xAAC1, "Narrow &0D: port=&93", inline=True)
comment(0xAAC2, "Narrow &0E: skip (dest station)", inline=True)
comment(0xAAC3, "Narrow &0F: skip (dest network)", inline=True)
comment(0xAAC4, "Narrow &10: buf start lo=&D9", inline=True)
comment(0xAAC5, "Narrow &11: buf start hi=page ptr", inline=True)
comment(0xAAC6, "Narrow &12: buf start ext lo", inline=True)
comment(0xAAC7, "Narrow &13: buf start ext hi", inline=True)
comment(0xAAC8, "Narrow &14: buf end lo=&DE", inline=True)
comment(0xAAC9, "Narrow &15: buf end hi=page ptr", inline=True)
comment(0xAACA, "Narrow &16: buf end ext lo", inline=True)
comment(0xAACB, "Narrow &17: buf end ext hi", inline=True)
comment(0xAACC, "Spool stop (&FE terminator)", inline=True)
comment(0xAACD, "Spool &01: port=&D1", inline=True)
comment(0xAACF, "Spool &03: skip (dest network)", inline=True)
comment(0xAAD1, "Spool &05: skip (buf start hi)", inline=True)
comment(0xAAD2, "Spool &06: buf start ext lo", inline=True)
comment(0xAAD3, "Spool &07: buf start ext hi", inline=True)
comment(0xAAD4, "Spool &08: skip (buf end lo)", inline=True)
comment(0xAAD5, "Spool &09: skip (buf end hi)", inline=True)
comment(0xAAD6, "Spool &0A: buf end ext lo", inline=True)
comment(0xAAD7, "Spool &0B: buf end ext hi", inline=True)

# netv_spool_check (&AAC6): OSWORD 5 handler
comment(0xAAD8, "X = X - 1", inline=True)
comment(0xAAD9, "Match osword_pb_ptr?", inline=True)
comment(0xAADB, "No: return (not our PB)", inline=True)
comment(0xAADD, "Load spool state byte", inline=True)
comment(0xAADF, "Rotate bit 0 into carry", inline=True)
comment(0xAAE0, "C=1: already active, return", inline=True)

# reset_spool_buf_state: reset printer spool buffer
comment(0xAAE2, "Buffer start at &25", inline=True)
comment(0xAAE4, "Store as buffer pointer", inline=True)
comment(0xAAE7, "Control state &41", inline=True)
comment(0xAAE9, "Store as spool control state", inline=True)
comment(0xAAEC, "Return", inline=True)

# netv_print_data (&AADB): OSWORD 1-3 handler
comment(0xAAED, "Check Y == 4", inline=True)
comment(0xAAEF, "No: return", inline=True)
comment(0xAAF1, "A = X (control byte)", inline=True)
comment(0xAAF2, "Decrement X", inline=True)
comment(0xAAF3, "Non-zero: handle spool ctrl byte", inline=True)
comment(0xAAF5, "Get stack pointer", inline=True)
comment(0xAAF6, "OR with stack value", inline=True)
comment(0xAAF9, "Store back to stack", inline=True)

# Read printer buffer loop
comment(0xAAFC, "OSBYTE &91: read buffer", inline=True)
comment(0xAAFE, "X=3: printer buffer", inline=True)
comment(0xAB00, "Read character from buffer", inline=True)
comment(0xAB03, "C=1: buffer empty, return", inline=True)
comment(0xAB05, "A = extracted character", inline=True)
comment(0xAB06, "Add byte to RX buffer", inline=True)
comment(0xAB09, "Buffer past &6E limit?", inline=True)
comment(0xAB0B, "No: read more from buffer", inline=True)
comment(0xAB0D, "Buffer full: send packet", inline=True)
comment(0xAB10, "More room: continue reading", inline=True)

# append_byte_to_rxbuf: add byte to receive buffer
comment(0xAB12, "Load current buffer index", inline=True)
comment(0xAB15, "Store byte at buffer position", inline=True)
comment(0xAB17, "Advance buffer index", inline=True)
comment(0xAB1A, "Return", inline=True)

# handle_spool_ctrl_byte: process spool control byte
comment(0xAB1B, "Rotate bit 0 into carry", inline=True)
comment(0xAB1C, "Bit 0 clear: not active path", inline=True)
comment(0xAB1E, "Load spool control state", inline=True)
comment(0xAB21, "Save for bit test", inline=True)
comment(0xAB22, "Rotate bit 0 into carry", inline=True)
comment(0xAB23, "Restore state", inline=True)
comment(0xAB24, "C=1: already started, reset", inline=True)
comment(0xAB26, "Set bits 0-1 (active + pending)", inline=True)
comment(0xAB28, "Store updated state", inline=True)
comment(0xAB2B, "Control byte 3 for header", inline=True)
comment(0xAB2D, "Add to RX buffer", inline=True)
comment(0xAB30, "Send current buffer", inline=True)
comment(0xAB33, "Reset spool buffer state", inline=True)

# cab24: prepare and send spool buffer packet
comment(0xAB36, "Y=8: workspace offset for length", inline=True)
comment(0xAB38, "Load buffer index (=length)", inline=True)
comment(0xAB3B, "Store length to workspace", inline=True)
comment(0xAB3D, "Set data page high byte", inline=True)
comment(0xAB40, "Store to workspace+9", inline=True)
comment(0xAB42, "Y=5: workspace offset", inline=True)
comment(0xAB44, "Store page to workspace+5", inline=True)
comment(0xAB46, "Y=&0B: template start offset", inline=True)
comment(0xAB48, "X=&26: template index", inline=True)
comment(0xAB4A, "Copy template to workspace", inline=True)
comment(0xAB4D, "Adjust Y down", inline=True)
comment(0xAB4E, "Load spool control state", inline=True)
comment(0xAB51, "Save state", inline=True)
comment(0xAB52, "Rotate to get carry (bit 7)", inline=True)
comment(0xAB53, "Restore state", inline=True)
comment(0xAB54, "Toggle bit 7", inline=True)
comment(0xAB56, "Store updated state", inline=True)
comment(0xAB59, "Shift to get both flag bits", inline=True)
comment(0xAB5A, "Store flags to workspace", inline=True)
comment(0xAB5C, "Save l00d0 (exec flag)", inline=True)
comment(0xAB5E, "Push for later restore", inline=True)
comment(0xAB5F, "Clear bit 0 of exec flag", inline=True)
comment(0xAB61, "Store modified exec flag", inline=True)
comment(0xAB63, "Reset buffer start to &25", inline=True)
comment(0xAB65, "Store reset buffer index", inline=True)
comment(0xAB68, "A=0 for disconnect reply", inline=True)
comment(0xAB6A, "X=0", inline=True)
comment(0xAB6B, "Y = workspace page", inline=True)
comment(0xAB6D, "Enable interrupts", inline=True)
comment(0xAB6E, "Send disconnect reply packet", inline=True)
comment(0xAB71, "Restore exec flag", inline=True)
comment(0xAB72, "Store original exec flag", inline=True)
comment(0xAB74, "Return", inline=True)

# cab63: spool not-active path
comment(0xAB75, "Load spool control state", inline=True)
comment(0xAB78, "Rotate bit 0 to carry", inline=True)
comment(0xAB79, "C=0: send current buffer", inline=True)
comment(0xAB7B, "Save exec flag", inline=True)
comment(0xAB7D, "Push for restore", inline=True)
comment(0xAB7E, "Clear bit 0", inline=True)
comment(0xAB80, "Store modified flag", inline=True)
comment(0xAB82, "Control byte &14 (repeat count)", inline=True)

# cab72: transmit spool data with retry
comment(0xAB84, "Save retry count", inline=True)
comment(0xAB85, "X=&0B: 12 bytes of template", inline=True)
comment(0xAB87, "Y=&2C: workspace offset for TXCB", inline=True)

# Copy TX template to workspace
comment(0xAB89, "Load template byte", inline=True)
comment(0xAB8C, "Store to workspace", inline=True)
comment(0xAB8E, "Next byte down", inline=True)
comment(0xAB8F, "Next template byte", inline=True)
comment(0xAB90, "Loop for 12 bytes", inline=True)
comment(0xAB92, "X=-1: disable escape checking", inline=True)
comment(0xAB94, "Y=2: workspace offset for station", inline=True)
comment(0xAB96, "Load station number", inline=True)
comment(0xAB98, "Save station", inline=True)
comment(0xAB9A, "Load network number", inline=True)
comment(0xAB9C, "Y=&24: TXCB dest network offset", inline=True)
comment(0xAB9E, "Store network to TXCB", inline=True)
comment(0xABA0, "Y=&23", inline=True)
comment(0xABA1, "Restore station", inline=True)
comment(0xABA2, "Store station to TXCB", inline=True)
comment(0xABA4, "X=&0B: 12 bytes of RX template", inline=True)
comment(0xABA6, "Y=&0B: workspace RX offset", inline=True)

# Copy RX palette template with marker substitution
comment(0xABA8, "Load RX template byte", inline=True)
comment(0xABAB, "Is it &FD? (skip marker)", inline=True)
comment(0xABAD, "Yes: skip store", inline=True)
comment(0xABAF, "Is it &FC? (page ptr marker)", inline=True)
comment(0xABB1, "No: use literal value", inline=True)
comment(0xABB3, "&FC: substitute RX buffer page", inline=True)
comment(0xABB5, "Store to workspace", inline=True)
comment(0xABB7, "Next byte down", inline=True)
comment(0xABB8, "Next template byte", inline=True)
comment(0xABB9, "Loop for 12 bytes", inline=True)

# Set up pointers and send packet
comment(0xABBB, "TX data start at &25", inline=True)
comment(0xABBD, "Set net_tx_ptr low", inline=True)
comment(0xABBF, "Set data page high byte", inline=True)
comment(0xABC1, "Set net_tx_ptr high", inline=True)
comment(0xABC3, "Set up password in TX buffer", inline=True)
comment(0xABC6, "Send the packet", inline=True)
comment(0xABC9, "Clear net_tx_ptr low (page base)", inline=True)
comment(0xABCB, "Store zero", inline=True)
comment(0xABCD, "Set TX high to workspace page", inline=True)
comment(0xABCF, "Store workspace high byte", inline=True)
comment(0xABD1, "Wait for TX acknowledgement", inline=True)
comment(0xABD4, "Y=&2D: reply status offset", inline=True)
comment(0xABD6, "Load reply byte", inline=True)
comment(0xABD8, "Zero: success", inline=True)
comment(0xABDA, "Status = 3? (busy, can retry)", inline=True)
comment(0xABDC, "Other error: handle failure", inline=True)

# Success: clean up and return
comment(0xABDE, "Discard retry count", inline=True)
comment(0xABDF, "Discard saved exec flag", inline=True)
comment(0xABE0, "Restore l00d0", inline=True)
comment(0xABE2, "A=0: null terminator", inline=True)
comment(0xABE4, "Add zero to RX buffer (end marker)", inline=True)
comment(0xABE7, "Send final buffer", inline=True)
comment(0xABEA, "Load spool state", inline=True)
comment(0xABED, "Clear low nibble", inline=True)
comment(0xABEF, "Store cleaned state", inline=True)
comment(0xABF2, "Return", inline=True)

# Error: retry or report
comment(0xABF3, "X = error code", inline=True)
comment(0xABF4, "Restore retry count", inline=True)
comment(0xABF5, "Set carry for subtract", inline=True)
comment(0xABF6, "Decrement retry count", inline=True)
comment(0xABF8, "Non-zero: retry send", inline=True)
comment(0xABFA, "Error code = 1? (busy)", inline=True)
comment(0xABFC, "No: printer jammed error", inline=True)
comment(0xABFE, "A=&A6: printer busy error number", inline=True)
comment(0xAC00, "Generate 'Printer busy' error", inline=True)
comment(0xAC10, "A=&A7: printer jammed error number", inline=True)
comment(0xAC12, "Generate 'Printer jammed' error", inline=True)

# send_disconnect_reply: send disconnect/status reply
comment(0xAC24, "Set TX ptr low byte", inline=True)
comment(0xAC26, "Set TX ptr high byte", inline=True)
comment(0xAC28, "Save disconnect code", inline=True)
comment(0xAC29, "Test if zero", inline=True)
comment(0xAC2B, "Zero: skip station search", inline=True)
comment(0xAC2D, "X=&FF: start search from -1", inline=True)
comment(0xAC2F, "Y = disconnect code", inline=True)

# Search station table for matching station
comment(0xAC30, "A = disconnect code", inline=True)
comment(0xAC31, "Next station index", inline=True)
comment(0xAC32, "Compare with station table entry", inline=True)
comment(0xAC35, "Match: verify station/network", inline=True)
comment(0xAC37, "Past last station?", inline=True)
comment(0xAC39, "No: try next", inline=True)
comment(0xAC3B, "Not found: A=0", inline=True)
comment(0xAC3D, "Skip to status update", inline=True)

# Verify matching station
comment(0xAC3F, "Y = disconnect code for compare", inline=True)
comment(0xAC40, "Check station and network match", inline=True)
comment(0xAC43, "No match: try next station", inline=True)
comment(0xAC45, "Load station status flags", inline=True)
comment(0xAC48, "Isolate bit 0 (active flag)", inline=True)

# Update TX buffer and send status
comment(0xAC4A, "Y=0: TX buffer status offset", inline=True)
comment(0xAC4C, "OR with existing status byte", inline=True)
comment(0xAC4E, "Save combined status", inline=True)
comment(0xAC4F, "Store to TX buffer", inline=True)
comment(0xAC51, "Send the packet", inline=True)
comment(0xAC54, "Set end markers to &FF", inline=True)
comment(0xAC56, "Y=8: first end marker offset", inline=True)
comment(0xAC58, "Store &FF", inline=True)
comment(0xAC5B, "Store &FF at offset 9 too", inline=True)
comment(0xAC5D, "Restore disconnect code", inline=True)
comment(0xAC5E, "X = status for control byte", inline=True)
comment(0xAC5F, "Y=&D1: default control", inline=True)
comment(0xAC61, "Check original disconnect code", inline=True)
comment(0xAC62, "Peek but keep on stack", inline=True)
comment(0xAC63, "Zero: use &D1 control", inline=True)
comment(0xAC65, "Non-zero: use &90 control", inline=True)

# Store control byte and set up wait loop
comment(0xAC67, "A = control byte (Y)", inline=True)
comment(0xAC68, "Y=1: control byte offset", inline=True)
comment(0xAC6A, "Store control byte", inline=True)
comment(0xAC6C, "A = X (status)", inline=True)
comment(0xAC6D, "Y=0", inline=True)
comment(0xAC6E, "Save status on stack", inline=True)

# Wait for acknowledgement with retry
comment(0xAC6F, "Set status to &7F (waiting)", inline=True)
comment(0xAC71, "Store at TX buffer offset 0", inline=True)
comment(0xAC73, "Wait for TX acknowledgement", inline=True)
comment(0xAC76, "Restore status", inline=True)
comment(0xAC77, "Keep on stack for next check", inline=True)
comment(0xAC78, "Compare with current TX buffer", inline=True)
comment(0xAC7A, "Rotate result bit 0 to carry", inline=True)
comment(0xAC7B, "C=1: status changed, retry", inline=True)
comment(0xAC7D, "Done: discard status", inline=True)
comment(0xAC7E, "Discard disconnect code", inline=True)
comment(0xAC7F, "Return", inline=True)

# tx_econet_txcb_template (&AC80): 12-byte spool TX control block.
# Simple copy to workspace offset &21..&2C via (net_rx_ptr),Y.
# Station/network at offsets &23/&24 filled in after copy.
comment(0xAC80, "Spool TX control block template\n"
    "\n"
    "12-byte TXCB template copied directly (no\n"
    "marker processing) to workspace at offset\n"
    "&21..&2C. Destination station and network\n"
    "(&23/&24) are filled in from (nfs_workspace)\n"
    "after the copy.")
comment(0xAC80, "ctrl=&80 (standard TX)", inline=True)
comment(0xAC81, "port=&9F", inline=True)
comment(0xAC82, "dest station=&00 (filled later)", inline=True)
comment(0xAC83, "dest network=&00 (filled later)", inline=True)
comment(0xAC85, "buf start hi=&8E", inline=True)
comment(0xAC86, "buf start ext lo=&FF", inline=True)
comment(0xAC87, "buf start ext hi=&FF", inline=True)
comment(0xAC89, "buf end hi=&8E", inline=True)
comment(0xAC8A, "buf end ext lo=&FF", inline=True)
comment(0xAC8B, "buf end ext hi=&FF", inline=True)

# rx_palette_txcb_template (&AC7A): 12-byte spool RX control block.
# Copied with marker processing by loop_copy_spool_rx.
# &FD=skip (preserve dest station/network), &FC=net_rx_ptr_hi.
comment(0xAC8C, "Spool RX control block template\n"
    "\n"
    "12-byte RXCB template with marker processing:\n"
    "&FD skips the offset (preserves existing value)\n"
    "and &FC substitutes net_rx_ptr_hi. Copied to\n"
    "workspace at offset &00..&0B. Sets up a 3-byte\n"
    "receive buffer at &xx31..&xx34.")
comment(0xAC8C, "ctrl=&7F (RX listen)", inline=True)
comment(0xAC8D, "port=&9E", inline=True)
comment(0xAC8E, "skip: preserve dest station", inline=True)
comment(0xAC91, "buf start hi=page ptr (&FC)", inline=True)
comment(0xAC92, "buf start ext lo=&FF", inline=True)
comment(0xAC93, "buf start ext hi=&FF", inline=True)
comment(0xAC95, "buf end hi=page ptr (&FC)", inline=True)
comment(0xAC96, "buf end ext lo=&FF", inline=True)
comment(0xAC97, "buf end ext hi=&FF", inline=True)

# Palette read handler (&AC86)
comment(0xAC98, "Save l00ad counter", inline=True)
comment(0xAC9A, "Push for later restore", inline=True)
comment(0xAC9B, "Set workspace low to &E9", inline=True)
comment(0xAC9D, "Store to nfs_workspace low", inline=True)
comment(0xAC9F, "Y=0: initial palette index", inline=True)
comment(0xACA1, "Clear palette counter", inline=True)
comment(0xACA3, "Load current screen mode", inline=True)
comment(0xACA6, "Store mode to workspace", inline=True)
comment(0xACA8, "Advance workspace ptr", inline=True)
comment(0xACAA, "Load video ULA copy", inline=True)
comment(0xACAD, "Save for later restore", inline=True)
comment(0xACAE, "A=0 for first palette entry", inline=True)

# Palette read loop
comment(0xACAF, "Store logical colour to workspace", inline=True)
comment(0xACB1, "X = workspace ptr low", inline=True)
comment(0xACB3, "Y = workspace ptr high", inline=True)
comment(0xACB5, "OSWORD &0B: read palette", inline=True)
comment(0xACB7, "Read palette entry", inline=True)
comment(0xACBA, "Restore previous ULA value", inline=True)
comment(0xACBB, "Y=0: reset index", inline=True)
comment(0xACBD, "Store ULA value to workspace", inline=True)
comment(0xACBF, "Y=1: physical colour offset", inline=True)
comment(0xACC0, "Load physical colour", inline=True)
comment(0xACC2, "Save for next iteration", inline=True)
comment(0xACC3, "X = workspace ptr", inline=True)
comment(0xACC5, "Advance workspace ptr", inline=True)
comment(0xACC7, "Advance palette counter", inline=True)
comment(0xACC9, "Y=0", inline=True)
comment(0xACCA, "Load counter", inline=True)
comment(0xACCC, "Reached &F9 workspace limit?", inline=True)
comment(0xACCE, "No: read next palette entry", inline=True)
comment(0xACD0, "Discard last ULA value", inline=True)
comment(0xACD1, "Clear counter", inline=True)
comment(0xACD3, "Advance workspace ptr", inline=True)
comment(0xACD5, "Store extra palette info", inline=True)
comment(0xACD8, "Advance workspace ptr again", inline=True)
comment(0xACDA, "Restore original l00ad", inline=True)
comment(0xACDB, "Store restored counter", inline=True)

# commit_state_byte: copy state to committed state
comment(0xACDD, "Load current state", inline=True)
comment(0xACE0, "Store as committed state", inline=True)
comment(0xACE3, "Return", inline=True)

# serialise_palette_entry
comment(0xACE4, "Load palette register value", inline=True)
comment(0xACE7, "Store to workspace", inline=True)
comment(0xACE9, "X = palette register", inline=True)
comment(0xACEC, "Read OSBYTE for this mode", inline=True)
comment(0xACEF, "Advance workspace ptr", inline=True)
comment(0xACF1, "A=0", inline=True)
comment(0xACF2, "Store zero to workspace", inline=True)
comment(0xACF4, "Read OSBYTE with X=0", inline=True)

# read_osbyte_to_ws_x0
comment(0xACF7, "X=0: read mode info", inline=True)

# read_osbyte_to_ws
comment(0xACF9, "Load OSBYTE code index", inline=True)
comment(0xACFB, "Advance index counter", inline=True)
comment(0xACFD, "Advance workspace ptr", inline=True)
comment(0xACFF, "Load OSBYTE number from table", inline=True)
comment(0xAD02, "Y=&FF: read current value", inline=True)
comment(0xAD04, "Call OSBYTE to read value", inline=True)
comment(0xAD07, "A = result (from X)", inline=True)
comment(0xAD08, "X=0 for indexed store", inline=True)
comment(0xAD0A, "Store result to workspace", inline=True)
comment(0xAD0C, "Return", inline=True)

# osbyte_mode_read_codes (&ACFB): 3-byte OSBYTE number table.
# Indexed by read_osbyte_to_ws to save display mode state.
comment(0xAD0D, "OSBYTE mode read codes\n"
    "\n"
    "Three OSBYTE numbers used by read_osbyte_to_ws\n"
    "to save display mode state to workspace before\n"
    "a language 2 file transfer.")
comment(0xAD0E, "OSBYTE &C2: read video ULA ctrl", inline=True)
comment(0xAD0F, "OSBYTE &C3: read video ULA palette", inline=True)

# cmd_dump (&BA06): *DUMP command — hex/ASCII file dump
# Buffer layout: 21 bytes on stack (page 1), pointed to by l00ae/l00af
#   buf[&00-&0F]: 16 data bytes read from file
#   buf[&10-&13]: 4-byte display address (little-endian)
#   buf[&14]:     flags/counter byte (high nibble for header control)
# osword_flag (&AA) reused as byte counter during dump loop (-1 to 15)

# Entry: open file and allocate stack buffer
comment(0xBA1B, "Open file for reading, set ws_page", inline=True)
comment(0xBA1E, "21 bytes to push (0-&14)", inline=True)
comment(0xBA20, "Zero fill value", inline=True)
comment(0xBA22, "Push zero onto stack", inline=True)
comment(0xBA23, "Count down", inline=True)
comment(0xBA24, "Loop until all 21 bytes pushed", inline=True)
comment(0xBA26, "X = stack pointer (buffer base - 1)", inline=True)
comment(0xBA27, "Set up buffer pointer and parse args", inline=True)

# Check start alignment and maybe print header
comment(0xBA2A, "Load display address low byte", inline=True)
comment(0xBA2C, "Test high nibble", inline=True)
comment(0xBA2E, "Skip header if 16-byte aligned", inline=True)
comment(0xBA30, "Print column header for offset start", inline=True)

# Main line loop: read up to 16 bytes per line
comment(0xBA33, "Check for Escape key", inline=True)
comment(0xBA36, "Start byte counter at -1", inline=True)
comment(0xBA38, "Reset counter", inline=True)

# OSBGET read loop: fill buffer with up to 16 bytes
comment(0xBA3F, "C=1 from OSBGET: end of file", inline=True)
comment(0xBA41, "Increment byte counter (0-15)", inline=True)
comment(0xBA43, "Use counter as buffer index", inline=True)
comment(0xBA45, "Store byte in data buffer", inline=True)
comment(0xBA47, "Read 16 bytes? (index 0-15)", inline=True)
comment(0xBA49, "No: read next byte", inline=True)
comment(0xBA4B, "C=0: not EOF, full line read", inline=True)

# EOF/empty check
comment(0xBA4C, "Save C: EOF status", inline=True)
comment(0xBA4D, "Check byte counter", inline=True)
comment(0xBA4F, "Counter >= 0: have data to display", inline=True)
comment(0xBA51, "22 bytes to pop (21 buffer + PHP)", inline=True)

# Stack cleanup loop (shared by EOF-no-data and last-line)
comment(0xBA53, "Pop one byte from stack", inline=True)
comment(0xBA54, "Count down", inline=True)
comment(0xBA55, "Loop until stack cleaned up", inline=True)
comment(0xBA57, "Close file and return", inline=True)

# Check if header needed at 256-byte boundary
comment(0xBA5A, "Point to display address low byte", inline=True)
comment(0xBA5C, "Load display address low byte", inline=True)
comment(0xBA5E, "Test high nibble", inline=True)
comment(0xBA60, "Non-zero: header already current", inline=True)
comment(0xBA62, "Crossed 256-byte boundary: new header", inline=True)

# Print 4-byte address big-endian
comment(0xBA65, "Start from highest address byte", inline=True)
comment(0xBA67, "Load address byte", inline=True)
comment(0xBA69, "Save for address increment later", inline=True)
comment(0xBA6A, "Print as two hex digits", inline=True)
comment(0xBA6D, "Restore address byte", inline=True)
comment(0xBA6E, "Next byte down", inline=True)
comment(0xBA6F, "Printed all 4 address bytes?", inline=True)
comment(0xBA71, "No: print next address byte", inline=True)

# Advance display address by 16 for next line
comment(0xBA73, "Y=&10: point to address byte 0", inline=True)
comment(0xBA74, "Prepare for 16-byte add", inline=True)
comment(0xBA75, "Add 16 to lowest address byte", inline=True)
comment(0xBA77, "Save carry for propagation", inline=True)

# 4-byte address increment loop (carry propagation)
comment(0xBA78, "Restore carry from previous byte", inline=True)
comment(0xBA79, "Store updated address byte", inline=True)
comment(0xBA7B, "Next address byte up", inline=True)
comment(0xBA7C, "Load next address byte", inline=True)
comment(0xBA7E, "Add carry", inline=True)
comment(0xBA80, "Save carry for next byte", inline=True)
comment(0xBA81, "Past all 4 address bytes?", inline=True)
comment(0xBA83, "No: continue propagation", inline=True)
comment(0xBA85, "Discard final carry", inline=True)
comment(0xBA86, "Print address/data separator", inline=True)

# Hex byte display: print each data byte as hex
comment(0xBA8C, "Start from first data byte", inline=True)
comment(0xBA8E, "X = bytes read (counter for display)", inline=True)
comment(0xBA90, "Load data byte from buffer", inline=True)
comment(0xBA92, "Print as two hex digits", inline=True)
comment(0xBA95, "Space separator", inline=True)

# Advance to next column position
comment(0xBA95, "Next column", inline=True)
comment(0xBA96, "All 16 columns done?", inline=True)
comment(0xBA98, "Yes: go to ASCII separator", inline=True)
comment(0xBA9A, "Decrement remaining data bytes", inline=True)
comment(0xBA9B, "More data: print next hex byte", inline=True)

# Pad missing hex columns with spaces
comment(0xBA9D, "Save column position", inline=True)
comment(0xBA9E, "Preserve Y across print", inline=True)
comment(0xBA9F, "Print 3-space padding", inline=True)
comment(0xBAA5, "Inline string terminator (NOP)", inline=True)
comment(0xBAA6, "Restore column position", inline=True)
comment(0xBAA7, "Back to Y", inline=True)
comment(0xBAA8, "Check next column", inline=True)

# ASCII section separator
comment(0xBAAB, "Adjust X for advance_x_by_8", inline=True)
comment(0xBAAC, "Print hex/ASCII separator", inline=True)
comment(0xBAB1, "Y=0: start ASCII section from byte 0", inline=True)

comment(0xBAB3, "Advance X to ASCII display column", inline=True)
# ASCII display: print printable chars, '.' for others
comment(0xBAB6, "Load data byte", inline=True)
comment(0xBAB8, "Strip high bit", inline=True)
comment(0xBABA, "Printable? (>= space)", inline=True)
comment(0xBABC, "Yes: check for DEL", inline=True)
comment(0xBABE, "Non-printable: substitute '.'", inline=True)
comment(0xBAC0, "Is it DEL (&7F)?", inline=True)
comment(0xBAC2, "Yes: substitute '.'", inline=True)
comment(0xBAC4, "Print ASCII character", inline=True)
comment(0xBAC7, "Next column", inline=True)
comment(0xBAC8, "All 16 columns done?", inline=True)
comment(0xBACA, "Yes: end of line", inline=True)
comment(0xBACC, "Decrement remaining data bytes", inline=True)
comment(0xBACD, "More data: print next ASCII char", inline=True)

# End of line: check for EOF
comment(0xBACF, "Print newline", inline=True)
comment(0xBAD2, "Restore EOF status from &BA4C", inline=True)
comment(0xBAD3, "C=1: EOF reached, clean up", inline=True)
comment(0xBAD5, "Not EOF: continue with next line", inline=True)

# EOF on last partial line: clean up stack
comment(0xBAD8, "21 bytes to pop (buffer only, PHP done)", inline=True)
comment(0xBADA, "Reuse stack cleanup loop", inline=True)

# print_dump_header: print column offset header
comment(0xBADD, "Load display address low byte", inline=True)
comment(0xBADF, "Save as starting column number", inline=True)
comment(0xBAE0, "Print header label with leading CR", inline=True)
comment(0xBAEF, "X=&0F: 16 column numbers to print", inline=True)

comment(0xBAF1, "Restore starting column number", inline=True)
# Column header print loop
comment(0xBAF2, "Print as two hex digits", inline=True)
comment(0xBAF5, "Space separator", inline=True)
comment(0xBAFA, "Restore column number", inline=True)
comment(0xBAF5, "SEC for +1 via ADC", inline=True)
comment(0xBAF6, "Increment column number (SEC+ADC 0=+1)", inline=True)
comment(0xBAF8, "Wrap to low nibble (0-F)", inline=True)
comment(0xBAFA, "Count down", inline=True)
comment(0xBAFB, "Loop for all 16 columns", inline=True)
comment(0xBAFD, "Print trailer with ASCII label", inline=True)
comment(0xBB03, "Save byte value on stack", inline=True)

# close_ws_file: close file handle stored in ws_page

# open_file_for_read: open file, advance past filename
# On entry: Y = offset to filename start within command line
# On exit: ws_page = file handle, Y = offset past filename
comment(0xBB07, "A=&20: space character", inline=True)
comment(0xBB09, "Print space character", inline=True)

# Restore text pointer and skip past filename in command line
comment(0xBB0C, "Restore byte value from stack", inline=True)

# Scan past filename to find end (space or CR)

# Skip trailing spaces after filename

# Return with Y pointing past filename/spaces
comment(0xBB0D, "Return; Y = offset to next argument", inline=True)

# parse_dump_range: parse hex address from command line
# On entry: Y = offset into command line text
# On exit: buf[0-3] = parsed 32-bit address,
#   C=0 if valid address, C=1 if overflow
#   Y = offset past parsed text
comment(0xBB0E, "Save command line offset to X", inline=True)
comment(0xBB0F, "X tracks current position", inline=True)
comment(0xBB10, "Zero for clearing accumulator", inline=True)
comment(0xBB12, "Y=0 for buffer indexing", inline=True)

# Clear 4-byte accumulator in buffer
comment(0xBB13, "Clear accumulator byte", inline=True)
comment(0xBB15, "Next byte", inline=True)
comment(0xBB16, "All 4 bytes cleared?", inline=True)
comment(0xBB18, "No: clear next", inline=True)

# Main parse loop: get next character
comment(0xBB1A, "Restore pre-increment offset to A", inline=True)
comment(0xBB1B, "Advance X to next char position", inline=True)
comment(0xBB1C, "Y = pre-increment offset for indexing", inline=True)
comment(0xBB1D, "Load character from command line", inline=True)
comment(0xBB1F, "CR: end of input", inline=True)
comment(0xBB21, "Done: skip trailing spaces", inline=True)
comment(0xBB23, "Space: end of this parameter", inline=True)
comment(0xBB25, "Done: skip trailing spaces", inline=True)

# Validate hex digit
comment(0xBB27, "Below '0'?", inline=True)
comment(0xBB29, "Yes: not a hex digit, error", inline=True)
comment(0xBB2B, "Below ':'? (i.e. '0'-'9')", inline=True)
comment(0xBB2D, "Yes: is a decimal digit", inline=True)
comment(0xBB2F, "Force uppercase for A-F", inline=True)
comment(0xBB31, "Map 'A'-'F' → &FA-&FF (C=0 here)", inline=True)
comment(0xBB33, "Carry set: char > 'F', error", inline=True)
comment(0xBB35, "Below &FA? (i.e. was < 'A')", inline=True)
comment(0xBB37, "Yes: gap between '9' and 'A', error", inline=True)

# Extract low nibble as hex value
comment(0xBB39, "Mask to low nibble (0-15)", inline=True)
comment(0xBB3B, "Save hex digit value", inline=True)
comment(0xBB3C, "Save current offset", inline=True)
comment(0xBB3D, "Preserve on stack", inline=True)
comment(0xBB3E, "4 bits to shift in", inline=True)

# Shift 32-bit accumulator left by 4 (one nibble)
comment(0xBB40, "Start from byte 0 (LSB)", inline=True)
comment(0xBB42, "Clear A; C from PHA/PLP below", inline=True)

# Inner loop: rotate one bit through all 4 bytes
comment(0xBB43, "Transfer carry bit to flags via stack", inline=True)
comment(0xBB44, "PLP: C = bit shifted out of prev iter", inline=True)
comment(0xBB45, "Load accumulator byte", inline=True)
comment(0xBB47, "Rotate left through carry", inline=True)
comment(0xBB48, "Store shifted byte", inline=True)
comment(0xBB4A, "Save carry for next byte", inline=True)
comment(0xBB4B, "Transfer to A for PHA/PLP trick", inline=True)
comment(0xBB4C, "Next accumulator byte", inline=True)
comment(0xBB4D, "All 4 bytes rotated?", inline=True)
comment(0xBB4F, "No: rotate next byte", inline=True)

# Check for overflow after shift
comment(0xBB51, "Transfer carry to flags", inline=True)
comment(0xBB52, "C = overflow bit", inline=True)
comment(0xBB53, "Overflow: address too large", inline=True)
comment(0xBB55, "Count bits shifted", inline=True)
comment(0xBB56, "4 bits shifted? No: shift again", inline=True)

# OR new nibble into accumulator byte 0
comment(0xBB58, "Restore command line offset", inline=True)
comment(0xBB59, "Back to X", inline=True)
comment(0xBB5A, "Restore hex digit value", inline=True)
comment(0xBB5B, "Point to LSB of accumulator", inline=True)
comment(0xBB5D, "OR digit into low nibble", inline=True)
comment(0xBB5F, "Store updated LSB", inline=True)
comment(0xBB61, "Parse next character", inline=True)

# Overflow exit: address too large
comment(0xBB64, "Discard saved offset", inline=True)
comment(0xBB65, "Discard saved digit", inline=True)
comment(0xBB66, "C=1: overflow", inline=True)
comment(0xBB67, "Return with C=1", inline=True)

# Bad hex digit: close file and error
comment(0xBB68, "Close open file before error", inline=True)
comment(0xBB6B, "Generate 'Bad hex' error", inline=True)

# Skip trailing spaces after parsed address
comment(0xBB6E, "Advance past space", inline=True)
comment(0xBB6F, "Load next char", inline=True)
comment(0xBB71, "Space?", inline=True)
comment(0xBB73, "Yes: skip it", inline=True)
comment(0xBB75, "C=0: valid parse (no overflow)", inline=True)
comment(0xBB76, "Return; Y past trailing spaces", inline=True)

# init_dump_buffer: set up buffer pointer and parse arguments
# On entry: X = stack pointer (buffer base - 1)
# Buffer becomes page 1 at address X+1
comment(0xBB77, "X+1: first byte of buffer", inline=True)
comment(0xBB78, "Set buffer pointer low byte", inline=True)
comment(0xBB7A, "Buffer is on stack in page 1", inline=True)
comment(0xBB7C, "Set buffer pointer high byte", inline=True)
comment(0xBB7E, "Parse start offset from command line", inline=True)
comment(0xBB81, "Overflow: 'Outside file' error", inline=True)

# Save position, get file length for validation
comment(0xBB83, "A = command line offset after parse", inline=True)
comment(0xBB84, "Save for later (past start addr)", inline=True)
comment(0xBB89, "A=2: read file extent (length)", inline=True)
comment(0xBB8E, "Check from MSB down", inline=True)

# Compare file length with start offset
comment(0xBB90, "Load file length byte", inline=True)
comment(0xBB93, "Compare with start offset byte", inline=True)
comment(0xBB95, "Mismatch: check which is larger", inline=True)
comment(0xBB97, "Next byte down", inline=True)
comment(0xBB98, "More bytes to compare", inline=True)
comment(0xBB9A, "All equal: start = length, within file", inline=True)

# Handle length vs start comparison result
comment(0xBB9C, "Length < start: outside file", inline=True)
comment(0xBB9E, "Y=&FF: length > start, flag for later", inline=True)
comment(0xBBA0, "Continue to copy start address", inline=True)

# Outside file error
comment(0xBBA2, "Close file before error", inline=True)
comment(0xBBA5, "Error number &B7", inline=True)
comment(0xBBA7, "Generate 'Outside file' error", inline=True)

# Copy start offset to osword_flag as file pointer
comment(0xBBB7, "Load start address byte from buffer", inline=True)
comment(0xBBB9, "Store to osword_flag (&AA-&AD)", inline=True)
comment(0xBBBC, "Next byte", inline=True)
comment(0xBBBD, "All 4 bytes copied?", inline=True)
comment(0xBBBF, "No: copy next byte", inline=True)

# Set file pointer to start offset via OSARGS
comment(0xBBC5, "A=1: write file pointer", inline=True)
comment(0xBBC7, "OSARGS: set file pointer", inline=True)

# Restore command line position, check for end parameter
comment(0xBBCA, "Restore saved command line offset", inline=True)
comment(0xBBCB, "Back to Y for command line indexing", inline=True)
comment(0xBBCC, "Load next char from command line", inline=True)
comment(0xBBCE, "End of command? (CR)", inline=True)
comment(0xBBD0, "No: parse display base address", inline=True)

# No explicit display base: use file's load address
comment(0xBBD2, "Copy 2 bytes: os_text_ptr to buffer", inline=True)
comment(0xBBD4, "Load os_text_ptr byte", inline=True)
comment(0xBBD7, "Store as filename pointer in OSFILE CB", inline=True)
comment(0xBBD9, "Next byte", inline=True)
comment(0xBBDA, "Copy both low and high bytes", inline=True)

# OSFILE to read catalogue info (gets load address)
comment(0xBBDC, "Read catalogue information", inline=True)
comment(0xBBDE, "X = control block low", inline=True)
comment(0xBBE0, "Y = control block high", inline=True)
comment(0xBBE2, "OSFILE: read file info", inline=True)

# Copy load address from OSFILE +2..+5 down to buf[0-3]
comment(0xBBE5, "Start at OSFILE +2 (load addr byte 0)", inline=True)
comment(0xBBE7, "Load from OSFILE result offset", inline=True)
comment(0xBBE9, "Y-2: destination is 2 bytes earlier", inline=True)
comment(0xBBEA, "Continue decrement", inline=True)
comment(0xBBEB, "Store to buf[Y-2]", inline=True)
comment(0xBBED, "Y += 3: advance source index", inline=True)
comment(0xBBEE, "(continued)", inline=True)
comment(0xBBEF, "(continued)", inline=True)
comment(0xBBF0, "Copied all 4 load address bytes?", inline=True)
comment(0xBBF2, "No: copy next byte", inline=True)

# Check if load address is &FFFFFFFF (not set)
comment(0xBBF4, "Y=6 after loop exit", inline=True)
comment(0xBBF5, "Y=4: check from buf[4] downward", inline=True)
comment(0xBBF6, "Load address byte", inline=True)
comment(0xBBF8, "Is it &FF?", inline=True)
comment(0xBBFA, "No: valid load address, use it", inline=True)
comment(0xBBFC, "Check next byte down", inline=True)
comment(0xBBFD, "More bytes to check for &FF", inline=True)

# All &FF: clear load address to 0 (default base)
comment(0xBBFF, "Clear all 4 bytes", inline=True)
comment(0xBC01, "Zero value", inline=True)
comment(0xBC03, "Clear byte", inline=True)
comment(0xBC05, "Next byte down", inline=True)
comment(0xBC06, "Loop for all 4 bytes", inline=True)
comment(0xBC08, "Continue to compute display address", inline=True)

# Parse explicit display base address (second parameter)
comment(0xBC0A, "Parse second hex parameter", inline=True)
comment(0xBC0D, "Valid: use as display base", inline=True)
comment(0xBC0F, "Invalid: close file before error", inline=True)
comment(0xBC12, "Error number &FC", inline=True)
comment(0xBC14, "Generate 'Bad address' error", inline=True)

# Compute display start: display_addr = base + start_offset
comment(0xBC1F, "Start from LSB", inline=True)
comment(0xBC21, "4 bytes to add", inline=True)
comment(0xBC23, "Clear carry for addition", inline=True)
comment(0xBC24, "Load display base byte", inline=True)
comment(0xBC26, "Add start offset byte", inline=True)
comment(0xBC29, "Store result in osword_flag", inline=True)
comment(0xBC2C, "Next byte", inline=True)
comment(0xBC2D, "Count down", inline=True)
comment(0xBC2E, "Loop for all 4 bytes", inline=True)

# Store display address into buf[&10-&13]
comment(0xBC30, "Point past end of address area", inline=True)
comment(0xBC32, "Start from MSB (byte 3)", inline=True)
comment(0xBC34, "Pre-decrement Y", inline=True)
comment(0xBC35, "Load computed display address byte", inline=True)
comment(0xBC37, "Store to buf[&10-&13]", inline=True)
comment(0xBC39, "Next byte down", inline=True)
comment(0xBC3A, "Loop for all 4 bytes", inline=True)
comment(0xBC3C, "Return; Y=&10 (address low byte)", inline=True)
comment(0xBC3D, "Load file handle from workspace", inline=True)

comment(0xBC3F, "A=0: close file", inline=True)
# advance_x_by_8/4/inx4: increment X by 8, 4, or 4
comment(0xBC44, "Save caller flags", inline=True)
# Uses chained JSR/fall-through: advance_x_by_8 does 16 INXs
comment(0xBC45, "A=filename offset from Y", inline=True)
comment(0xBC86, "JSR+fall-through: 8+8=16 INXs total", inline=True)
comment(0xBC46, "Clear carry for 16-bit addition", inline=True)
comment(0xBC89, "JSR+fall-through: 4+4=8 INXs", inline=True)
comment(0xBC47, "Add text pointer low byte", inline=True)
comment(0xBC8C, "X += 4", inline=True)
comment(0xBC49, "Save filename address low", inline=True)
comment(0xBC8D, "(continued)", inline=True)
comment(0xBC4A, "X=filename address low (for OSFIND)", inline=True)
comment(0xBC8E, "(continued)", inline=True)
comment(0xBC4B, "A=0: carry propagation only", inline=True)
comment(0xBC8F, "(continued)", inline=True)
comment(0xBC4D, "Add text pointer high byte + carry", inline=True)
comment(0xBC90, "Return", inline=True)
comment(0xBC4F, "Save filename address high", inline=True)
comment(0xBC93, "Padding; next byte is reloc_p5_src", inline=True)
comment(0xBC50, "Y=filename address high (for OSFIND)", inline=True)

comment(0xBC51, "A=&40: open for reading", inline=True)
# ============================================================
comment(0xBC57, "Store file handle in workspace", inline=True)
# cmd_wipe: *Wipe command + channel management utilities
comment(0xBC59, "Non-zero: file opened successfully", inline=True)
# ============================================================
comment(0xBC5B, "Error &D6", inline=True)

comment(0xBC5D, "Raise 'Not found' error", inline=True)
# Entry: parse filename, enumerate directory
comment(0xB359, "Mask owner access flags to 5 bits", inline=True)
comment(0xB35C, "Initialise file index to 0", inline=True)
comment(0xB35E, "Store file counter", inline=True)
comment(0xB360, "Save pointer to command text", inline=True)
comment(0xB363, "Parse wildcard filename argument", inline=True)
comment(0xB366, "Advance past CR terminator", inline=True)
comment(0xB367, "Save end-of-argument buffer position", inline=True)
comment(0xBC6A, "Restore text pointer high from stack", inline=True)

comment(0xBC6B, "Set OS text pointer high", inline=True)
# Main examine loop: request next file from server
comment(0xB369, "Command code 1 = examine directory", inline=True)
comment(0xB36B, "Store command in TX buffer byte 0", inline=True)
comment(0xB36E, "Store flag in TX buffer byte 2", inline=True)
comment(0xB371, "Load current file index", inline=True)
comment(0xB373, "Store file index in TX buffer byte 1", inline=True)
comment(0xB376, "X=3: copy from TX buffer offset 3", inline=True)
comment(0xB378, "Copy filename argument to TX buffer", inline=True)
comment(0xB37B, "Function code 3 = examine", inline=True)
comment(0xB37D, "Flag &80 = escapable", inline=True)
comment(0xB37F, "Mark operation as escapable", inline=True)
comment(0xB381, "Send examine request to file server", inline=True)
comment(0xB384, "Get server response status", inline=True)
comment(0xB387, "Non-zero: file found, process it", inline=True)
comment(0xBC6D, "Restore text pointer low from stack", inline=True)

comment(0xBC6E, "Set OS text pointer low", inline=True)
# No more files: flush keyboard buffers and return
comment(0xB389, "OSBYTE &0F: flush buffer class", inline=True)
comment(0xB38B, "X=1: flush input buffers", inline=True)
comment(0xB38D, "Flush keyboard buffer", inline=True)
comment(0xB390, "OSBYTE &7A: keyboard scan from 16", inline=True)
comment(0xB392, "Scan keyboard to clear state", inline=True)
comment(0xB395, "Y=0: no key pressed", inline=True)
comment(0xB397, "OSBYTE &78: write keys pressed", inline=True)
comment(0xB399, "Clear keyboard state and return", inline=True)
comment(0xBC70, "Y=0: start from beginning", inline=True)

comment(0xBC72, "Advance to next character", inline=True)
# Response processing: filter locked and directory entries
comment(0xB39C, "Load first attribute char of response", inline=True)
comment(0xB39F, "Is file locked?", inline=True)
comment(0xB3A1, "No: check if directory", inline=True)
comment(0xB3A3, "Skip locked file, advance index", inline=True)
comment(0xB3A5, "Request next file from server", inline=True)
comment(0xB3A8, "Is it a directory entry?", inline=True)
comment(0xB3AA, "No: regular file, show prompt", inline=True)
comment(0xB3AC, "Check directory contents flag", inline=True)
comment(0xB3AF, "Non-empty dir: treat as locked, skip", inline=True)
comment(0xBC73, "Load character from command text", inline=True)

comment(0xBC75, "CR (end of line)?", inline=True)
# Print filename and prompt user for Y/N/?
comment(0xB3B1, "X=1: start from response byte 1", inline=True)
comment(0xB3B3, "Y = destination index in delete buffer", inline=True)
comment(0xB3B5, "Load filename char from response", inline=True)
comment(0xB3B8, "Print filename character to screen", inline=True)
comment(0xB3BB, "Store in delete command buffer too", inline=True)
comment(0xB3BE, "Advance destination index", inline=True)
comment(0xB3BF, "Advance source index", inline=True)
comment(0xB3C0, "Copied all 11 filename characters?", inline=True)
comment(0xB3C2, "No: continue copying", inline=True)
comment(0xB3C4, "Print '(Y/N/?) ' prompt", inline=True)
comment(0xB3CA, "Inline string terminator (NOP)", inline=True)
comment(0xB3CB, "Read user response character", inline=True)
comment(0xB3CE, "User pressed '?'?", inline=True)
comment(0xB3D0, "No: check for Y/N response", inline=True)
comment(0xBC77, "Yes: finished parsing filename", inline=True)

comment(0xBC79, "Space (word separator)?", inline=True)
# '?' handler: show full file info then re-prompt
comment(0xB3D2, "Carriage return before full info", inline=True)
comment(0xB3D4, "Print CR", inline=True)
comment(0xB3D7, "X=2: start from response byte 2", inline=True)
comment(0xB3D9, "Load file info character", inline=True)
comment(0xB3DC, "Print file info character", inline=True)
comment(0xB3DF, "Advance to next character", inline=True)
comment(0xB3E0, "Printed all &3C info bytes?", inline=True)
comment(0xB3E2, "No: continue printing", inline=True)
comment(0xB3E4, "Print ' (Y/N) ' prompt (no '?')", inline=True)
comment(0xB3E9, "Padding (string terminator)", inline=True)
comment(0xB3EA, "Read user response (Y/N only)", inline=True)
comment(0xBC7B, "No: still within filename", inline=True)

comment(0xBC7D, "Advance past space", inline=True)
# Check for 'Y' response: build and send delete command
comment(0xB3ED, "Force uppercase", inline=True)
comment(0xB3EF, "User said 'Y' (yes)?", inline=True)
comment(0xB3F1, "No: print newline, skip to next file", inline=True)
comment(0xB3F3, "Echo 'Y' to screen", inline=True)
comment(0xB3F6, "X=0: start of stored filename", inline=True)
comment(0xB3F8, "Check first byte of stored name", inline=True)
comment(0xB3FB, "Is first byte CR (empty first field)?", inline=True)
comment(0xB3FD, "Yes: use second filename field", inline=True)
comment(0xBC7E, "Load next character", inline=True)

comment(0xBC80, "Another space?", inline=True)
# Build delete command from displayed filename
comment(0xBC82, "Yes: skip consecutive spaces", inline=True)
# Replace CR with '.', space terminates with CR
comment(0xB3FF, "Load byte from stored filename", inline=True)
comment(0xB402, "Is it CR (field separator)?", inline=True)
comment(0xB404, "No: check for space", inline=True)
comment(0xB406, "Replace CR with '.' directory sep", inline=True)
comment(0xB408, "Is it a space (name terminator)?", inline=True)
comment(0xB40A, "No: keep character as-is", inline=True)
comment(0xB40C, "Replace space with CR (end of name)", inline=True)
comment(0xB40E, "Store in delete command TX buffer", inline=True)
comment(0xB411, "Advance to next character", inline=True)
comment(0xB412, "Was it the CR terminator?", inline=True)
comment(0xB414, "No: continue building delete command", inline=True)
comment(0xB416, "Function code &14 = delete file", inline=True)
comment(0xB418, "Send delete request to file server", inline=True)
comment(0xB41B, "Adjust file index after deletion", inline=True)
comment(0xBC84, "Restore caller flags", inline=True)

comment(0xBC85, "Return; Y=offset past filename", inline=True)
# Not 'Y': newline and advance to next file
comment(0xB41D, "Print newline after user response", inline=True)
comment(0xB420, "Advance index, process next file", inline=True)

# Second filename field: copy l0e31 to delete buffer
comment(0xB423, "DEX to offset following INX", inline=True)
comment(0xB424, "Advance to next byte", inline=True)
comment(0xB425, "Load byte from second field", inline=True)
comment(0xB428, "Store in delete command TX buffer", inline=True)
comment(0xB42B, "Is it a space (field terminator)?", inline=True)
comment(0xB42D, "No: continue copying second field", inline=True)
comment(0xB42F, "Space found: terminate with CR", inline=True)
comment(0xB431, "Print 'Y/N) ' prompt", inline=True)

# flush_and_read_char: flush input, read one character
comment(0xB7D3, "OSBYTE &0F: flush buffer class", inline=True)
comment(0xB7D5, "X=1: flush input buffers", inline=True)
comment(0xB7D7, "Flush keyboard buffer before read", inline=True)
comment(0xB7DA, "Read character from input stream", inline=True)
comment(0xB7DD, "C clear: character read OK", inline=True)
comment(0xB7DF, "Escape pressed: raise error", inline=True)
comment(0xB7E2, "Return with character in A", inline=True)

# init_channel_table: clear page &10 and set up channels
comment(0xB7E3, "A=0: clear value", inline=True)
comment(0xB7E5, "Y=0: start index", inline=True)
comment(0xB7E6, "Clear channel table entry", inline=True)
comment(0xB7E9, "Next entry", inline=True)
comment(0xB7EA, "Loop until all 256 bytes cleared", inline=True)
comment(0xB7EC, "Offset &0F in receive buffer", inline=True)
comment(0xB7EE, "Get number of available channels", inline=True)
comment(0xB7F0, "Prepare subtraction", inline=True)
comment(0xB7F1, "Subtract 'Z' to get negative count", inline=True)
comment(0xB7F3, "Y = negative channel count (index)", inline=True)
comment(0xB7F4, "Channel marker &40 (available)", inline=True)
comment(0xB7F6, "Mark channel slot as available", inline=True)
comment(0xB7F9, "Previous channel slot", inline=True)
comment(0xB7FA, "Reached start of channel range?", inline=True)
comment(0xB7FC, "No: continue marking channels", inline=True)
comment(0xB7FE, "Point to first channel slot", inline=True)
comment(0xB7FF, "Active channel marker &C0", inline=True)
comment(0xB801, "Mark first channel as active", inline=True)
comment(0xB804, "Return", inline=True)

# attr_to_chan_index: convert attribute byte to channel index
comment(0xB805, "Save flags", inline=True)
comment(0xB806, "Prepare subtraction", inline=True)
comment(0xB807, "Subtract &20 to get table index", inline=True)
comment(0xB809, "Negative: out of valid range", inline=True)
comment(0xB80B, "Above maximum channel index &0F?", inline=True)
comment(0xB80D, "In range: valid index", inline=True)
comment(0xB80F, "Out of range: return &FF (invalid)", inline=True)
comment(0xB811, "Restore flags", inline=True)
comment(0xB812, "X = channel index (or &FF)", inline=True)
comment(0xB813, "Return", inline=True)

# check_chan_char: validate channel character in A
comment(0xB814, "Below space?", inline=True)
comment(0xB816, "Yes: invalid channel character", inline=True)
comment(0xB818, "Below '0'?", inline=True)
comment(0xB81A, "In range &20-&2F: look up channel", inline=True)

# err_net_chan_invalid / err_net_chan_not_found
comment(0xB81C, "Save channel character", inline=True)
comment(0xB81D, "Error code &DE", inline=True)
comment(0xB81F, "Generate 'Net channel' error", inline=True)
comment(0xB82E, "Error string continuation (unreachable)", inline=True)

# lookup_chan_by_char: find channel by character
comment(0xB847, "Save channel character", inline=True)
comment(0xB848, "Prepare subtraction", inline=True)
comment(0xB849, "Convert char to table index", inline=True)
comment(0xB84B, "X = channel table index", inline=True)
comment(0xB84C, "Look up network number for channel", inline=True)
comment(0xB84F, "Zero: channel not found, raise error", inline=True)
comment(0xB851, "Check station/network matches current", inline=True)
comment(0xB854, "No match: build detailed error msg", inline=True)
comment(0xB856, "Discard saved channel character", inline=True)
comment(0xB857, "Load channel status flags", inline=True)
comment(0xB85A, "Return; A = channel flags", inline=True)

# Build custom "Net channel N not on this file server" error
comment(0xB85B, "Error code &DE", inline=True)
comment(0xB85D, "Store error code in error block", inline=True)
comment(0xB860, "BRK opcode", inline=True)
comment(0xB862, "Store BRK at start of error block", inline=True)
comment(0xB865, "X=0: copy index", inline=True)
comment(0xB866, "Advance copy position", inline=True)
comment(0xB867, "Load 'Net channel' string byte", inline=True)
comment(0xB86A, "Copy to error text", inline=True)
comment(0xB86D, "Continue until NUL terminator", inline=True)
comment(0xB86F, "Save end-of-string position", inline=True)
comment(0xB871, "Save for suffix append", inline=True)
comment(0xB873, "Retrieve channel character", inline=True)
comment(0xB874, "Append ' N' (channel number)", inline=True)
comment(0xB877, "Load 'Net channel' end position", inline=True)
comment(0xB879, "Skip past NUL to suffix string", inline=True)
comment(0xB87A, "Advance destination position", inline=True)
comment(0xB87B, "Load ' not on this...' suffix byte", inline=True)
comment(0xB87E, "Append to error message", inline=True)
comment(0xB881, "Continue until NUL", inline=True)
comment(0xB883, "Raise the constructed error", inline=True)

# store_result_check_dir: store channel result, check not dir
comment(0xB886, "Load current channel attribute", inline=True)
comment(0xB889, "Store channel attribute to RX buffer", inline=True)

# check_not_dir: validate channel is not a directory
comment(0xB88C, "Validate and look up channel", inline=True)
comment(0xB88F, "Test directory flag (bit 1)", inline=True)
comment(0xB891, "Not a directory: return OK", inline=True)
comment(0xB893, "Error code &A8", inline=True)
comment(0xB895, "Generate 'Is a dir.' error", inline=True)
# UNMAPPED: comment(0xB508, "Return", inline=True)

# alloc_fcb_slot: find free FCB slot in &20-&2F range
comment(0xB8A8, "Save channel attribute", inline=True)
comment(0xB8A9, "Start scanning from FCB slot &20", inline=True)
comment(0xB8AB, "Load FCB station byte", inline=True)
comment(0xB8AE, "Zero: slot is free, use it", inline=True)
comment(0xB8B0, "Try next slot", inline=True)
comment(0xB8B1, "Past last FCB slot &2F?", inline=True)
comment(0xB8B3, "No: check next slot", inline=True)
comment(0xB8B5, "No free slot: discard saved attribute", inline=True)
comment(0xB8B6, "A=0: return failure (Z set)", inline=True)
comment(0xB8B8, "Return", inline=True)

# Free slot found: initialise FCB entry
comment(0xB8B9, "Restore channel attribute", inline=True)
comment(0xB8BA, "Store attribute in FCB slot", inline=True)
comment(0xB8BD, "A=0: clear value", inline=True)
comment(0xB8BF, "Clear FCB transfer count low", inline=True)
comment(0xB8C2, "Clear FCB transfer count mid", inline=True)
comment(0xB8C5, "Clear FCB transfer count high", inline=True)
comment(0xB8C8, "Load current station number", inline=True)
comment(0xB8CB, "Store station in FCB", inline=True)
comment(0xB8CE, "Load current network number", inline=True)
comment(0xB8D1, "Store network in FCB", inline=True)
comment(0xB8D4, "Get FCB slot index", inline=True)
comment(0xB8D5, "Save slot index", inline=True)
comment(0xB8D6, "Prepare subtraction", inline=True)
comment(0xB8D7, "Convert slot to channel index (0-&0F)", inline=True)
comment(0xB8D9, "X = channel index", inline=True)
comment(0xB8DA, "Restore A = FCB slot index", inline=True)
comment(0xB8DB, "Return; A=slot, X=channel, Z clear", inline=True)

# alloc_fcb_or_error: allocate FCB or raise error
comment(0xB8DC, "Save argument", inline=True)
comment(0xB8DD, "A=0: allocate any available slot", inline=True)
comment(0xB8DF, "Try to allocate an FCB slot", inline=True)
comment(0xB8E2, "Success: slot allocated", inline=True)
comment(0xB8E4, "Error code &C0", inline=True)
comment(0xB8E6, "Generate 'No more FCBs' error", inline=True)
comment(0xB8F6, "Restore argument", inline=True)
comment(0xB8F7, "Return", inline=True)

# close_all_net_chans: close channels for current station
comment(0xB8F8, "C=0: close all matching channels", inline=True)
comment(0xB8F9, "Branch always to scan entry", inline=True)
comment(0xB8F9, "Set V flag via BIT (alternate mode)", inline=True)

# scan_fcb_flags: iterate FCB slots with station matching
comment(0xB8FC, "Start from FCB slot &10", inline=True)
comment(0xB8FE, "Previous FCB slot", inline=True)
comment(0xB8FF, "More slots to check", inline=True)
comment(0xB901, "All FCB slots processed, return", inline=True)
comment(0xB902, "Load channel flags for this slot", inline=True)
comment(0xB905, "Save flags in Y", inline=True)
comment(0xB906, "Test active flag (bit 1)", inline=True)
comment(0xB908, "Not active: check station match", inline=True)
comment(0xB90A, "V clear (close all): next slot", inline=True)
comment(0xB90C, "C clear: check station match", inline=True)
comment(0xB90E, "Restore original flags", inline=True)
comment(0xB90F, "Clear write-pending flag (bit 5)", inline=True)
comment(0xB911, "Update channel flags", inline=True)
comment(0xB914, "Next slot (V always set here)", inline=True)
comment(0xB916, "Check if channel belongs to station", inline=True)
comment(0xB919, "No match: skip to next slot", inline=True)
comment(0xB91B, "A=0: clear channel", inline=True)
comment(0xB91D, "Clear channel flags (close it)", inline=True)
comment(0xB920, "Clear network number", inline=True)
comment(0xB923, "Continue to next slot", inline=True)

# match_station_net: check if FCB X matches current station
comment(0xB925, "Load FCB station number", inline=True)
comment(0xB928, "Compare with current station (EOR)", inline=True)
comment(0xB92B, "Different: Z=0, no match", inline=True)
comment(0xB92D, "Load FCB network number", inline=True)
comment(0xB930, "Compare with current network (EOR)", inline=True)
comment(0xB933, "Return; Z=1 if match, Z=0 if not", inline=True)

# find_open_fcb: find next available FCB slot
# Two-pass scan: first pass skips modified, second accepts
comment(0xB934, "Load current FCB index", inline=True)
comment(0xB937, "Set V flag (first pass marker)", inline=True)
comment(0xB93A, "Next FCB slot", inline=True)
comment(0xB93B, "Past end of table (&10)?", inline=True)
comment(0xB93D, "No: continue checking", inline=True)
comment(0xB93F, "Wrap around to slot 0", inline=True)
comment(0xB941, "Back to starting slot?", inline=True)
comment(0xB944, "No: check this slot", inline=True)
comment(0xB946, "V clear (second pass): scan empties", inline=True)
comment(0xB948, "Clear V for second pass", inline=True)
comment(0xB949, "Continue scanning", inline=True)
comment(0xB94B, "Load FCB status flags", inline=True)
comment(0xB94E, "Shift bit 7 (in-use) into carry", inline=True)
comment(0xB94F, "Not in use: skip", inline=True)
comment(0xB951, "Test bit 2 (modified flag)", inline=True)
comment(0xB953, "Modified: check further conditions", inline=True)

# Found unmodified in-use slot: mark and return
comment(0xB955, "Adjust for following INX", inline=True)
comment(0xB956, "Next FCB slot", inline=True)
comment(0xB957, "Past end of table?", inline=True)
comment(0xB959, "No: continue", inline=True)
comment(0xB95B, "Wrap around to slot 0", inline=True)
comment(0xB95D, "Load FCB status flags", inline=True)
comment(0xB960, "Shift bit 7 into carry", inline=True)
comment(0xB961, "Not in use: continue scanning", inline=True)
comment(0xB963, "Set carry for ROR restore", inline=True)
comment(0xB964, "Restore original flags", inline=True)
comment(0xB965, "Save flags back (mark as found)", inline=True)
comment(0xB968, "Restore original FCB index", inline=True)
comment(0xB96B, "Return with found slot in X", inline=True)
comment(0xB96C, "V set (first pass): skip modified", inline=True)
comment(0xB96E, "Load FCB status flags", inline=True)
comment(0xB971, "Test bit 5 (offset pending)", inline=True)
comment(0xB973, "Bit 5 set: skip this slot", inline=True)
comment(0xB975, "Use this slot", inline=True)

# init_wipe_counters: reset all transfer counters
comment(0xB977, "Initial pass count = 1", inline=True)
comment(0xB979, "Store pass counter", inline=True)
comment(0xB97C, "Y=0", inline=True)
comment(0xB97D, "Clear byte counter low", inline=True)
comment(0xB980, "Clear offset counter", inline=True)
comment(0xB983, "Clear transfer flag", inline=True)
comment(0xB986, "A=0", inline=True)
comment(0xB987, "Clear 3 counter bytes", inline=True)
comment(0xB989, "Clear counter byte", inline=True)
comment(0xB98C, "Next byte", inline=True)
comment(0xB98D, "Loop for indices 2, 1, 0", inline=True)
comment(0xB98F, "Store &FF as sentinel in l10cd", inline=True)
comment(0xB992, "Store &FF as sentinel in l10ce", inline=True)
comment(0xB995, "X=&CA: workspace offset", inline=True)
comment(0xB997, "Y=&10: page &10", inline=True)
comment(0xB999, "Return; X/Y point to &10CA", inline=True)

# start_wipe_pass: flush pending data for one FCB
comment(0xB99A, "Verify workspace checksum integrity", inline=True)
comment(0xB99D, "Save current FCB index", inline=True)
comment(0xB9A0, "Load FCB status flags", inline=True)
comment(0xB9A3, "Shift bit 0 (active) into carry", inline=True)
comment(0xB9A4, "Not active: clear status and return", inline=True)
comment(0xB9A6, "Save current station low to stack", inline=True)
comment(0xB9A9, "Push station low", inline=True)
comment(0xB9AA, "Save current station high", inline=True)
comment(0xB9AD, "Push station high", inline=True)
comment(0xB9AE, "Load FCB station low", inline=True)
comment(0xB9B1, "Set as working station low", inline=True)
comment(0xB9B4, "Load FCB station high", inline=True)
comment(0xB9B7, "Set as working station high", inline=True)
comment(0xB9BA, "Reset transfer counters", inline=True)
comment(0xB9BD, "Set offset to &FF (no data yet)", inline=True)
comment(0xB9C0, "Set pass counter to 0 (flush mode)", inline=True)
comment(0xB9C3, "Reload FCB index", inline=True)
comment(0xB9C6, "Transfer to A", inline=True)
comment(0xB9C7, "Prepare addition", inline=True)
comment(0xB9C8, "Add &11 for buffer page offset", inline=True)
comment(0xB9CA, "Store buffer address high byte", inline=True)
comment(0xB9CD, "Load FCB status flags", inline=True)
comment(0xB9D0, "Test bit 5 (has saved offset)", inline=True)
comment(0xB9D2, "No offset: skip restore", inline=True)
comment(0xB9D4, "Load saved byte offset", inline=True)
comment(0xB9D7, "Restore offset counter", inline=True)
comment(0xB9DA, "Load FCB attribute reference", inline=True)
comment(0xB9DD, "Store as current reference", inline=True)
comment(0xB9E0, "Transfer to X", inline=True)
comment(0xB9E1, "Read saved receive attribute", inline=True)
comment(0xB9E4, "Push to stack", inline=True)
comment(0xB9E5, "Restore attribute to A", inline=True)
comment(0xB9E6, "Set attribute in receive buffer", inline=True)
comment(0xB9E8, "X=&CA: workspace offset", inline=True)
comment(0xB9EA, "Y=&10: page &10", inline=True)
comment(0xB9EC, "A=0: standard transfer mode", inline=True)
comment(0xB9EE, "Send data and receive response", inline=True)
comment(0xB9F1, "Reload FCB index", inline=True)
comment(0xB9F4, "Restore saved receive attribute", inline=True)
comment(0xB9F5, "Restore receive attribute", inline=True)
comment(0xB9F8, "Restore station high", inline=True)
comment(0xB9F9, "Store station high", inline=True)
comment(0xB9FC, "Restore station low", inline=True)
comment(0xB9FD, "Store station low", inline=True)

# Clear active/pending flags and return
comment(0xBA00, "Mask &DC: clear bits 0, 1, 5", inline=True)
comment(0xBA02, "Clear active and offset flags", inline=True)
comment(0xBA05, "Update FCB status", inline=True)
comment(0xBA08, "Return", inline=True)

# save_fcb_context: save TX buffer and workspace, process FCBs
comment(0xBA09, "Copy 13 bytes (indices 0 to &0C)", inline=True)
comment(0xBA0B, "Load TX buffer byte", inline=True)
comment(0xBA0E, "Save to context buffer at &10D9", inline=True)
comment(0xBA11, "Load workspace byte from fs_load_addr", inline=True)
comment(0xBA13, "Save to stack", inline=True)
comment(0xBA14, "Next byte down", inline=True)
comment(0xBA15, "Loop for all 13 bytes", inline=True)
comment(0xBA17, "Y=0? (no FCB to process)", inline=True)
comment(0xBA19, "Non-zero: scan and process FCBs", inline=True)
comment(0xBA1B, "Y=0: skip to restore workspace", inline=True)

# Scan for pending FCBs (bits 7+6 set) and process them
comment(0xBA1E, "Save flags", inline=True)
comment(0xBA1F, "X=&FF: start scanning from -1", inline=True)
comment(0xBA21, "Next FCB slot", inline=True)
comment(0xBA22, "Load FCB status flags", inline=True)
comment(0xBA25, "Bit 7 clear: not pending, skip", inline=True)
comment(0xBA27, "Shift bit 6 to bit 7", inline=True)
comment(0xBA28, "Bit 6 clear: skip", inline=True)
comment(0xBA2A, "Flush this FCB's pending data", inline=True)
comment(0xBA2D, "Pending marker &40", inline=True)
comment(0xBA2F, "Mark FCB as pending-only", inline=True)
comment(0xBA32, "Save flags", inline=True)
comment(0xBA33, "Find next available FCB slot", inline=True)
comment(0xBA36, "Restore flags", inline=True)
comment(0xBA37, "Load current channel attribute", inline=True)
comment(0xBA3A, "Store as current reference", inline=True)
comment(0xBA3D, "Save attribute", inline=True)
comment(0xBA3E, "Prepare attribute-to-channel conversion", inline=True)
comment(0xBA41, "Y = attribute index", inline=True)
comment(0xBA3F, "Convert attribute (&20+) to channel index", inline=True)
comment(0xBA42, "Load station for this attribute", inline=True)
comment(0xBA45, "Store station in TX buffer", inline=True)
comment(0xBA48, "Restore attribute", inline=True)
comment(0xBA49, "Store attribute in FCB slot", inline=True)
comment(0xBA4C, "Load working station low", inline=True)
comment(0xBA4F, "Store in TX buffer", inline=True)
comment(0xBA4F, "Store station low in FCB", inline=True)
comment(0xBA52, "Load working station high", inline=True)
comment(0xBA55, "Store in TX buffer", inline=True)
comment(0xBA55, "Store station high in FCB", inline=True)
comment(0xBA58, "Get FCB slot index", inline=True)
comment(0xBA59, "Prepare addition", inline=True)
comment(0xBA5A, "Add &11 for buffer page offset", inline=True)
comment(0xBA5C, "Store buffer address high byte", inline=True)
comment(0xBA5F, "Restore flags", inline=True)
comment(0xBA60, "V clear: skip directory request", inline=True)

# Send directory listing request for FCB
comment(0xBA62, "Command byte = 0", inline=True)
comment(0xBA6B, "Function code &0D", inline=True)
comment(0xBA62, "Send directory request to server", inline=True)

# Reset counters and send/receive data transfer
comment(0xBA65, "Reset transfer counters", inline=True)
comment(0xBA68, "Read saved receive attribute", inline=True)
comment(0xBA6B, "Push to stack", inline=True)
comment(0xBA6C, "Load current reference", inline=True)
comment(0xBA6F, "Set in receive buffer", inline=True)
comment(0xBA71, "Y=&10: page &10", inline=True)
comment(0xBA73, "A=2: transfer mode 2", inline=True)
comment(0xBA75, "Send and receive data", inline=True)
comment(0xBA78, "Restore receive attribute", inline=True)
comment(0xBA79, "Restore receive attribute", inline=True)
comment(0xBA7C, "Reload FCB index", inline=True)
comment(0xBA7F, "Load pass counter", inline=True)
comment(0xBA82, "Non-zero: data received, calc offset", inline=True)
comment(0xBA84, "Load offset counter", inline=True)
comment(0xBA87, "Zero: no data received at all", inline=True)

# Calculate and store negated offset for buffer positioning
comment(0xBA89, "Load offset counter", inline=True)
comment(0xBA8C, "Negate (ones complement)", inline=True)
comment(0xBA8E, "Clear carry for add", inline=True)
comment(0xBA8F, "Complete twos complement negation", inline=True)
comment(0xBA91, "Store negated offset in FCB", inline=True)
comment(0xBA94, "Set bit 5 (has saved offset)", inline=True)
comment(0xBA96, "Add to FCB flags", inline=True)
comment(0xBA99, "Update FCB status", inline=True)

# Clear buffer from offset to end of page
comment(0xBA9C, "Load buffer address high byte", inline=True)
comment(0xBA9F, "Set pointer high byte", inline=True)
comment(0xBAA1, "A=0: pointer low byte and clear val", inline=True)
comment(0xBAA3, "Set pointer low byte", inline=True)
comment(0xBAA5, "Load negated offset (start of clear)", inline=True)
comment(0xBAA8, "Clear buffer byte", inline=True)
comment(0xBAAA, "Next byte", inline=True)
comment(0xBAAB, "Loop until page boundary", inline=True)

# Mark FCB as active and restore workspace
comment(0xBAAD, "Set bit 1 (active flag)", inline=True)
comment(0xBAAF, "Add active flag to status", inline=True)
comment(0xBAB2, "Update FCB status", inline=True)
comment(0xBAB5, "Y=0: start restoring workspace", inline=True)
comment(0xBAB7, "Restore workspace byte from stack", inline=True)
comment(0xBAB8, "Store to fs_load_addr workspace", inline=True)
comment(0xBABB, "Next byte", inline=True)
comment(0xBABC, "Restored all 13 bytes?", inline=True)
comment(0xBABE, "No: continue restoring", inline=True)

# restore_catalog_entry: restore TX buffer from context
comment(0xBAC0, "Copy 13 bytes (indices 0 to &0C)", inline=True)
comment(0xBAC2, "Load saved catalog byte from &10D9", inline=True)
comment(0xBAC5, "Restore to TX buffer", inline=True)
comment(0xBAC8, "Next byte down", inline=True)
comment(0xBAC9, "Loop for all bytes", inline=True)
comment(0xBACB, "Return", inline=True)

# find_matching_fcb: find FCB matching channel attribute
comment(0xBACC, "Save current context first", inline=True)
comment(0xBACF, "X=&FF: start scanning from -1", inline=True)
comment(0xBAD1, "Load channel attribute to match", inline=True)
comment(0xBAD4, "Next FCB slot", inline=True)
comment(0xBAD5, "Past end of table (&10)?", inline=True)
comment(0xBAD7, "No: check this slot", inline=True)
comment(0xBAD9, "Load channel attribute", inline=True)
comment(0xBADC, "Convert to channel index", inline=True)
comment(0xBADF, "Load station for this channel", inline=True)
comment(0xBAE2, "Store as match target station high", inline=True)
comment(0xBAE5, "Load port for this channel", inline=True)
comment(0xBAE8, "Store as match target station low", inline=True)
comment(0xBAEB, "Save context and rescan from start", inline=True)
comment(0xBAEE, "Load FCB status flags", inline=True)
comment(0xBAF1, "Test active flag (bit 1)", inline=True)
comment(0xBAF3, "Not active: skip to next", inline=True)
comment(0xBAF5, "Get attribute to match", inline=True)
comment(0xBAF6, "Compare with FCB attribute ref", inline=True)
comment(0xBAF9, "No attribute match: skip", inline=True)
comment(0xBAFB, "Save matching FCB index", inline=True)
comment(0xBAFE, "Save flags from attribute compare", inline=True)
comment(0xBAFF, "Prepare subtraction", inline=True)
comment(0xBB00, "Convert attribute to channel index", inline=True)
comment(0xBB02, "Restore flags from attribute compare", inline=True)
comment(0xBB03, "Y = channel index", inline=True)
comment(0xBB04, "Reload FCB index", inline=True)
comment(0xBB07, "Load channel station byte", inline=True)
comment(0xBB0A, "Compare with FCB station", inline=True)
comment(0xBB0D, "Station mismatch: try next", inline=True)
comment(0xBB0F, "Load channel network byte", inline=True)
comment(0xBB12, "Compare with FCB network", inline=True)
comment(0xBB15, "Network mismatch: try next", inline=True)

# FCB matched: clear pending flag if set, check offset
comment(0xBB17, "Load FCB flags", inline=True)
comment(0xBB1A, "Bit 7 clear: no pending flush", inline=True)
comment(0xBB1C, "Clear pending flag (bit 7)", inline=True)
comment(0xBB1E, "Update FCB status", inline=True)
comment(0xBB21, "Find new open FCB slot", inline=True)
comment(0xBB24, "Reload FCB flags", inline=True)
comment(0xBB27, "Test bit 5 (has offset data)", inline=True)
comment(0xBB29, "Return; Z=1 no offset, Z=0 has data", inline=True)

# inc_fcb_byte_count: 3-byte increment
comment(0xBB2A, "Increment byte count low", inline=True)
comment(0xBB2D, "No overflow: done", inline=True)
comment(0xBB2F, "Increment byte count mid", inline=True)
comment(0xBB32, "No overflow: done", inline=True)
comment(0xBB34, "Increment byte count high", inline=True)
comment(0xBB37, "Return", inline=True)

# process_all_fcbs: iterate all FCBs, flush matching ones
# UNMAPPED: comment(0xB799, "Save X", inline=True)
# UNMAPPED: comment(0xB79A, "Push X to stack", inline=True)
# UNMAPPED: comment(0xB79B, "Save Y", inline=True)
# UNMAPPED: comment(0xB79C, "Push Y to stack", inline=True)
comment(0xBB3A, "X=&F7: save 9 workspace bytes (&F7..&FF)", inline=True)
comment(0xBB3F, "Push fs_options", inline=True)
comment(0xBB40, "Next byte", inline=True)
comment(0xBB3C, "Load workspace byte", inline=True)
comment(0xBB43, "Start from FCB slot &0F", inline=True)
comment(0xBB41, "X<0: more bytes to save", inline=True)
comment(0xBB45, "Store as current FCB index", inline=True)
comment(0xBB48, "Load current FCB index", inline=True)
comment(0xBB4B, "Get filter attribute", inline=True)
comment(0xBB4C, "Zero: process all FCBs", inline=True)
comment(0xBB4E, "Compare with FCB attribute ref", inline=True)
comment(0xBB51, "No match: skip this FCB", inline=True)
comment(0xBB53, "Save filter attribute", inline=True)
comment(0xBB54, "Flush pending data for this FCB", inline=True)
# UNMAPPED: comment(0xB7BA, "Restore filter", inline=True)
# UNMAPPED: comment(0xB7BB, "Y = filter attribute", inline=True)
comment(0xBB58, "Previous FCB index", inline=True)
comment(0xBB5B, "More slots: continue loop", inline=True)
comment(0xBB5D, "X=8: restore 9 workspace bytes", inline=True)
comment(0xBB5F, "Restore fs_block_offset", inline=True)
comment(0xBB60, "Restore workspace byte", inline=True)
# UNMAPPED: comment(0xB7C9, "Restore Y", inline=True)
comment(0xBB62, "Next byte down", inline=True)
# UNMAPPED: comment(0xB7CA, "Y restored", inline=True)
comment(0xBB63, "More bytes: continue restoring", inline=True)
# UNMAPPED: comment(0xB7CB, "Restore X", inline=True)
# UNMAPPED: comment(0xB7CC, "X restored", inline=True)
comment(0xBB67, "Return", inline=True)

# OSBGET handler: read byte from buffered file channel
comment(0xBB68, "Save channel attribute", inline=True)
comment(0xBB6B, "Save caller's X", inline=True)
comment(0xBB6C, "Push X", inline=True)
comment(0xBB6D, "Store result and check not directory", inline=True)
comment(0xBB70, "Load channel flags", inline=True)
comment(0xBB73, "Test write-only flag (bit 5)", inline=True)
comment(0xBB75, "Not write-only: proceed with read", inline=True)
comment(0xBB77, "Error code &D4", inline=True)
comment(0xBB79, "Generate 'Write only' error", inline=True)

# Find matching FCB and check for data in buffer
comment(0xBB87, "Clear V (first-pass matching)", inline=True)
comment(0xBB88, "Find FCB matching this channel", inline=True)
comment(0xBB8B, "No offset: read byte from buffer", inline=True)
comment(0xBB8D, "Load byte count for matching FCB", inline=True)
comment(0xBB90, "Compare with buffer offset limit", inline=True)
comment(0xBB93, "Below offset: data available", inline=True)
comment(0xBB95, "Load channel flags for FCB", inline=True)
comment(0xBB98, "Transfer to X for testing", inline=True)
comment(0xBB99, "Test bit 6 (EOF already signalled)", inline=True)
comment(0xBB9B, "EOF already set: raise error", inline=True)
comment(0xBB9D, "Restore flags", inline=True)
comment(0xBB9E, "Set EOF flag (bit 6)", inline=True)
comment(0xBBA0, "Update channel flags with EOF", inline=True)
comment(0xBBA3, "A=0: clear receive attribute", inline=True)
comment(0xBBA5, "Clear receive attribute (A=0)", inline=True)
comment(0xBBA8, "Restore caller's X", inline=True)
comment(0xBBA9, "X restored", inline=True)
comment(0xBBAA, "A=&FE: EOF marker byte", inline=True)
comment(0xBBAC, "Restore channel attribute", inline=True)
comment(0xBBAF, "C=1: end of file", inline=True)
comment(0xBBB0, "Return", inline=True)

# End of file error (already signalled once)
comment(0xBBB1, "Error code &DF", inline=True)
comment(0xBBB3, "Generate 'End of file' error", inline=True)

# Read byte from FCB buffer at current position
comment(0xBBC2, "Load current byte count (= offset)", inline=True)
comment(0xBBC5, "Save byte count", inline=True)
comment(0xBBC6, "Get FCB slot index", inline=True)
comment(0xBBC7, "X = FCB slot for byte count inc", inline=True)
comment(0xBBC8, "A=0: clear receive attribute", inline=True)
comment(0xBBCA, "Clear receive attribute (A=0)", inline=True)
comment(0xBBCD, "Increment byte count for this FCB", inline=True)
comment(0xBBD0, "Restore byte count (= buffer offset)", inline=True)
comment(0xBBD1, "Y = offset into data buffer", inline=True)
comment(0xBBD2, "Load current FCB index", inline=True)
comment(0xBBD5, "Prepare addition", inline=True)
comment(0xBBD6, "Add &11 for buffer page offset", inline=True)
comment(0xBBD8, "Set pointer high byte", inline=True)
comment(0xBBDA, "A=0: pointer low byte", inline=True)
comment(0xBBDC, "Set pointer low byte", inline=True)
comment(0xBBDE, "Restore caller's X", inline=True)
comment(0xBBDF, "X restored", inline=True)
comment(0xBBE0, "Read data byte from buffer", inline=True)
comment(0xBBE2, "Restore channel attribute", inline=True)
comment(0xBBE5, "C=0: byte read successfully", inline=True)
comment(0xBBE6, "Return; A = data byte", inline=True)

# OSBPUT handler: write byte to buffered file channel
comment(0xBBE7, "Save channel attribute", inline=True)
comment(0xBBEA, "Save data byte", inline=True)
comment(0xBBEB, "Y = data byte", inline=True)
comment(0xBBEC, "Save caller's X", inline=True)
comment(0xBBED, "Push X", inline=True)
comment(0xBBEE, "Restore data byte to A", inline=True)
comment(0xBBEF, "Push data byte for later", inline=True)
comment(0xBBF0, "Save data byte in workspace", inline=True)
comment(0xBBF3, "Store result and check not directory", inline=True)
comment(0xBBF6, "Load channel flags", inline=True)
comment(0xBBF9, "Bit 7 set: channel open, proceed", inline=True)
comment(0xBBFB, "Error &C1: Not open for update", inline=True)
comment(0xBBFD, "Raise error with inline string", inline=True)

# Channel open for writing: check write mode
comment(0xBC14, "Test write flag (bit 5)", inline=True)
comment(0xBC16, "Not write-capable: use buffer path", inline=True)
comment(0xBC18, "Load reply port for this channel", inline=True)
comment(0xBC1B, "Restore data byte", inline=True)
comment(0xBC1C, "Send byte directly to server", inline=True)
comment(0xBC1F, "Update byte count and return", inline=True)

# Buffer path: find matching FCB for buffered write
comment(0xBC22, "Set V flag (alternate match mode)", inline=True)
comment(0xBC25, "Find matching FCB for channel", inline=True)
comment(0xBC28, "Load byte count for FCB", inline=True)
comment(0xBC2B, "Buffer full (&FF bytes)?", inline=True)
comment(0xBC2D, "No: store byte in buffer", inline=True)

# Buffer full: flush to server before storing new byte
comment(0xBC2F, "Save X", inline=True)
comment(0xBC32, "Push Y", inline=True)
comment(0xBC37, "Carry set from BCS/BCC above", inline=True)
comment(0xBC2F, "Save context and flush FCB data", inline=True)

# Update buffer offset tracking after write
comment(0xBC32, "Compare count with buffer offset", inline=True)
comment(0xBC35, "Below offset: skip offset update", inline=True)
comment(0xBC37, "Add carry (count + 1)", inline=True)
comment(0xBC39, "Update buffer offset in FCB", inline=True)
comment(0xBC3C, "Non-zero: keep offset flag", inline=True)
comment(0xBC3E, "Mask &DF: clear bit 5", inline=True)
comment(0xBC40, "Clear offset flag", inline=True)
comment(0xBC43, "Update FCB status", inline=True)

# Mark FCB as active, store byte in buffer
comment(0xBC46, "Set bit 0 (dirty/active)", inline=True)
comment(0xBC48, "Add to FCB flags", inline=True)
comment(0xBC4B, "Update FCB status", inline=True)
comment(0xBC4E, "Load byte count (= write position)", inline=True)
comment(0xBC51, "Save count", inline=True)
comment(0xBC52, "Get FCB slot index", inline=True)
comment(0xBC53, "X = FCB slot", inline=True)
comment(0xBC54, "Restore byte count", inline=True)
comment(0xBC55, "Y = buffer write offset", inline=True)
comment(0xBC56, "Load current FCB index", inline=True)
comment(0xBC59, "Prepare addition", inline=True)
comment(0xBC5A, "Add &11 for buffer page offset", inline=True)
comment(0xBC5C, "Set pointer high byte", inline=True)
comment(0xBC5E, "A=0: pointer low byte", inline=True)
comment(0xBC60, "Set pointer low byte", inline=True)
comment(0xBC62, "Restore data byte", inline=True)
comment(0xBC63, "Write data byte to buffer", inline=True)

# Common OSBPUT exit: increment count, restore, return
comment(0xBC65, "Increment byte count for this FCB", inline=True)
comment(0xBC68, "A=0: clear receive attribute", inline=True)
comment(0xBC6A, "Clear receive attribute (A=0)", inline=True)
comment(0xBC6D, "Restore caller's X", inline=True)
comment(0xBC6E, "X restored", inline=True)
comment(0xBC6F, "Discard saved data byte", inline=True)
comment(0xBC70, "Restore channel attribute", inline=True)
comment(0xBC73, "Return", inline=True)
comment(0xBCBB, "Return", inline=True)
comment(0xBC74, "Save A", inline=True)

# UNMAPPED: comment(0xB8DB, "Transfer X to A", inline=True)
# send_wipe_request: send data byte to server via network
# UNMAPPED: comment(0xB8DC, "Save X", inline=True)
comment(0xBCBC, "Store reply port", inline=True)
# UNMAPPED: comment(0xB8DD, "Transfer Y to A", inline=True)
comment(0xBCBF, "Store data byte", inline=True)
# UNMAPPED: comment(0xB8DE, "Save Y (channel index)", inline=True)
comment(0xBCC2, "Save Y", inline=True)
comment(0xBC77, "Load station for this channel", inline=True)
comment(0xBCC3, "Push Y to stack", inline=True)
comment(0xBC7A, "Non-zero: station known, skip init", inline=True)
comment(0xBCC4, "Save X", inline=True)
comment(0xBC7C, "Save A", inline=True)
comment(0xBCC5, "Push X to stack", inline=True)
# UNMAPPED: comment(0xB8E5, "Transfer X to A", inline=True)
comment(0xBCC6, "Function code &90", inline=True)
# UNMAPPED: comment(0xB8E6, "Save X", inline=True)
comment(0xBCC8, "Store in send buffer", inline=True)
# UNMAPPED: comment(0xB8E7, "Transfer Y to A", inline=True)
comment(0xBCCB, "Initialise TX control block", inline=True)
# UNMAPPED: comment(0xB8E8, "Save Y (channel index)", inline=True)
comment(0xBCCE, "TX start address low = &DC", inline=True)
comment(0xBC7F, "Load station for this channel", inline=True)
comment(0xBCD0, "Set TX start in control block", inline=True)
comment(0xBC82, "Save station on stack", inline=True)
comment(0xBCD2, "TX end address low = &E0", inline=True)
comment(0xBC83, "Y=0: reset index", inline=True)
comment(0xBCD4, "Set TX end in control block", inline=True)
comment(0xBC85, "Save current FCB context", inline=True)
comment(0xBCD6, "Expected reply port = 9", inline=True)
comment(0xBC88, "Restore station from stack", inline=True)
comment(0xBCD8, "Store reply port in buffer", inline=True)
comment(0xBC89, "Store station in command buffer", inline=True)
comment(0xBCDB, "TX control = &C0", inline=True)
# UNMAPPED: comment(0xB8F6, "X=station number", inline=True)
comment(0xBCDD, "Y=0: no timeout", inline=True)
# UNMAPPED: comment(0xB8F7, "Restore Y from stack", inline=True)
comment(0xBCDF, "Load reply port for addressing", inline=True)
# UNMAPPED: comment(0xB8F8, "Y=channel index", inline=True)
comment(0xBCE2, "Send packet to server", inline=True)
# UNMAPPED: comment(0xB8F9, "Re-save Y on stack", inline=True)
comment(0xBCE5, "Load reply status", inline=True)
# UNMAPPED: comment(0xB8FA, "A=station number", inline=True)
comment(0xBCE8, "Zero: success", inline=True)
comment(0xBC8E, "Save station for later restore", inline=True)

comment(0xBC8F, "X=0", inline=True)
# Error response: copy error message and raise
comment(0xBC91, "Clear function code", inline=True)
comment(0xBCEA, "Store error code", inline=True)
comment(0xBC94, "Load byte count lo from FCB", inline=True)
comment(0xBCED, "X=0: copy index", inline=True)
comment(0xBC97, "Store as data byte count", inline=True)
comment(0xBCEF, "Load error message byte", inline=True)
comment(0xBC9A, "Load byte count mid from FCB", inline=True)
comment(0xBCF2, "Copy to error block", inline=True)
comment(0xBC9D, "Store as reply command byte", inline=True)
comment(0xBCF5, "Is it CR (end of message)?", inline=True)
comment(0xBCA0, "Load byte count hi from FCB", inline=True)
comment(0xBCF7, "Yes: terminate string", inline=True)
comment(0xBCA3, "Store as load vector field", inline=True)
comment(0xBCF9, "Next byte", inline=True)
comment(0xBCA6, "Y=&0D: TX command byte offset", inline=True)
comment(0xBCFA, "Continue copying error message", inline=True)
comment(0xBCA8, "X=5: send 5 bytes", inline=True)
comment(0xBCFC, "NUL terminator", inline=True)
comment(0xBCAA, "Send flush request to server", inline=True)
comment(0xBCFE, "Terminate error string in block", inline=True)
comment(0xBCAD, "Restore station from stack", inline=True)
comment(0xBD01, "Back up position for error check", inline=True)
comment(0xBCAE, "Y=station for wipe request", inline=True)
comment(0xBD02, "Process and raise network error", inline=True)
comment(0xBCAF, "Load saved data byte", inline=True)

comment(0xBCB2, "Send close/wipe request to server", inline=True)
# Success: toggle station bit and return
comment(0xBCB5, "Restore catalog state after flush", inline=True)
comment(0xBD05, "Load channel attribute index", inline=True)
# UNMAPPED: comment(0xB925, "Restore Y", inline=True)
comment(0xBD08, "Load station number for channel", inline=True)
# UNMAPPED: comment(0xB926, "Y restored", inline=True)
comment(0xBD0B, "Toggle bit 0 (alternate station)", inline=True)
# UNMAPPED: comment(0xB927, "Restore X", inline=True)
comment(0xBD0D, "Update station number", inline=True)
# UNMAPPED: comment(0xB928, "X restored", inline=True)
comment(0xBD10, "Restore X", inline=True)
comment(0xBCBA, "Restore A", inline=True)
comment(0xBD11, "X restored", inline=True)
comment(0xBD12, "Restore Y", inline=True)
comment(0xBD13, "Y restored", inline=True)
comment(0xBD14, "Return", inline=True)

# send_and_receive: set up options and transfer workspace
comment(0xBD15, "Set up FS options pointer", inline=True)
comment(0xBD18, "Set up transfer workspace and return", inline=True)
comment(0xBD1B, "Y=&0A: receive attribute offset", inline=True)

comment(0xBD1D, "Read byte from receive buffer", inline=True)
# error_inline: generate BRK error from inline string (&96BE-&96D9)
comment(0x99C5, "Store return address low", inline=True)
comment(0x99C8, "Store return address high", inline=True)
comment(0x99CA, "X=0: error text index", inline=True)
comment(0x99CF, "Copy error number to A", inline=True)
comment(0x99D0, "Push error number on stack", inline=True)
comment(0x99D1, "Y=0: inline string index", inline=True)
comment(0x99D7, "Advance string index", inline=True)
comment(0x99DA, "Store byte in error block", inline=True)
comment(0xBD1F, "Return", inline=True)

comment(0xBD20, "Y=&0A: receive attribute offset", inline=True)
# check_net_error_code: process network error response (&96DA-&9736)
comment(0x99E2, "Non-zero: network returned an error", inline=True)
comment(0x99E4, "Pop saved error number", inline=True)
comment(0x99E5, "Was it &DE (file server error)?", inline=True)
comment(0x99E7, "Yes: append error number and trigger BRK", inline=True)
comment(0x99E9, "Jump to BRK via error block", inline=True)
comment(0x99EC, "Store error code in workspace", inline=True)
comment(0x99EF, "Push error code", inline=True)
comment(0x99F0, "Save X (error text index)", inline=True)
comment(0x99F1, "Push X", inline=True)
comment(0x99F2, "Read receive attribute byte", inline=True)
comment(0x99F5, "Save to fs_load_addr as spool handle", inline=True)
comment(0x99F7, "A=0: clear error code in RX buffer", inline=True)
comment(0x99F9, "Zero the error code byte in buffer", inline=True)
comment(0x99FB, "A=&C6: OSBYTE read spool handle", inline=True)
comment(0x99FD, "Read current spool file handle", inline=True)
comment(0x9A00, "Compare Y result with saved handle", inline=True)
comment(0x9A02, "Match: close the spool file", inline=True)
comment(0x9A04, "Compare X result with saved handle", inline=True)
comment(0x9A06, "No match: skip spool close", inline=True)
comment(0x9A08, "Push A (preserved)", inline=True)
comment(0x9A09, "A=&C6: disable spool with OSBYTE", inline=True)
comment(0x9A0B, "ALWAYS branch to close spool", inline=True)
# UNMAPPED: comment(0x971E, "Transfer Y to A for stack save", inline=True)
# UNMAPPED: comment(0x971F, "Push A (preserved)", inline=True)
comment(0x9A0E, "A=&C7: disable exec with OSBYTE", inline=True)
comment(0x9A10, "OSBYTE with X=0, Y=0 to close", inline=True)
# UNMAPPED: comment(0x9725, "Pull saved handle", inline=True)
# UNMAPPED: comment(0x9726, "Transfer to Y for OSFIND", inline=True)
comment(0x9A14, "A=0: close file", inline=True)
comment(0x9A16, "Close the spool/exec file", inline=True)
comment(0x9A19, "Pull saved X (error text index)", inline=True)
comment(0x9A1A, "Restore X", inline=True)
comment(0x9A1B, "Y=&0A: lookup index for 'on channel'", inline=True)
comment(0x9A1D, "Load message offset from lookup table", inline=True)
comment(0x9A20, "Transfer offset to Y", inline=True)
comment(0x9A21, "Load error message byte", inline=True)
comment(0x9A24, "Append to error text buffer", inline=True)
comment(0x9A27, "Null terminator: done copying", inline=True)
comment(0x9A29, "Advance error text index", inline=True)
comment(0x9A2A, "Advance message index", inline=True)
comment(0x9A2B, "Loop until full message copied", inline=True)
comment(0x9A2D, "Save error text end position", inline=True)
comment(0x9A2F, "Pull saved error number", inline=True)
comment(0x9A30, "Append ' nnn' error number suffix", inline=True)
comment(0x9A33, "A=0: null terminator", inline=True)
comment(0x9A35, "Terminate error text string", inline=True)
comment(0x9A38, "ALWAYS branch to trigger BRK error", inline=True)
comment(0xBD22, "Store byte to receive buffer", inline=True)

comment(0xBD24, "Return", inline=True)
# append_drv_dot_num: append ' net.station' to error text (&9738-&975B)
comment(0x9A3A, "A=' ': space separator", inline=True)
comment(0x9A3C, "Append space to error text", inline=True)
comment(0x9A3F, "Advance error text index", inline=True)
comment(0x9A40, "Save position for number formatting", inline=True)
comment(0x9A42, "Y=3: offset to network number in TX CB", inline=True)
comment(0x9A44, "Load network number", inline=True)
comment(0x9A46, "Zero: skip network part (local)", inline=True)
comment(0x9A48, "Append network number as decimal", inline=True)
comment(0x9A4B, "Reload error text position", inline=True)
comment(0x9A4D, "A='.': dot separator", inline=True)
comment(0x9A4F, "Append dot to error text", inline=True)
comment(0x9A52, "Advance past dot", inline=True)
comment(0x9A54, "Y=2: offset to station number in TX CB", inline=True)
comment(0x9A56, "Load station number", inline=True)
comment(0x9A58, "Append station number as decimal", inline=True)
comment(0x9A5B, "Reload error text position", inline=True)
comment(0x9A5D, "Return", inline=True)

# append_space_and_num: append ' nnn' to error text (&975C-&9797)
comment(0x9A5E, "Save number in Y", inline=True)
comment(0x9A5F, "A=' ': space prefix", inline=True)
comment(0x9A61, "Load current error text position", inline=True)
comment(0x9A63, "Append space to error text", inline=True)
comment(0x9A66, "Advance position past space", inline=True)
comment(0x9A68, "Restore number to A", inline=True)
comment(0x9A69, "Save number in Y for division", inline=True)
comment(0x9A6A, "Set V: suppress leading zeros", inline=True)
comment(0x9A6D, "A=100: hundreds digit divisor", inline=True)
comment(0x9A6F, "Extract and append hundreds digit", inline=True)
comment(0x9A72, "A=10: tens digit divisor", inline=True)
comment(0x9A74, "Extract and append tens digit", inline=True)
comment(0x9A77, "A=1: units digit (remainder)", inline=True)
comment(0x9A79, "Clear V: always print units digit", inline=True)
comment(0x9A7A, "Store divisor", inline=True)
comment(0x9A7C, "Copy number to A for division", inline=True)
comment(0x9A7D, "X='0'-1: digit counter (ASCII offset)", inline=True)
comment(0x9A7F, "Save V flag (leading zero suppression)", inline=True)
comment(0x9A80, "Set carry for subtraction", inline=True)
comment(0x9A81, "Increment digit counter", inline=True)
comment(0x9A82, "Subtract divisor", inline=True)
comment(0x9A84, "Not negative yet: continue counting", inline=True)
comment(0x9A86, "Add back divisor (restore remainder)", inline=True)
comment(0x9A88, "Restore V flag", inline=True)
comment(0x9A89, "Save remainder back to Y", inline=True)
comment(0x9A8A, "Digit counter to A (ASCII digit)", inline=True)
comment(0x9A8B, "Is digit '0'?", inline=True)
comment(0x9A8D, "Non-zero: always print", inline=True)
comment(0x9A8F, "V set (suppress leading zeros): skip", inline=True)
comment(0x9A91, "Clear V: first non-zero digit seen", inline=True)
comment(0x9A92, "Load current text position", inline=True)
comment(0x9A94, "Store ASCII digit in error text", inline=True)
comment(0x9A97, "Advance text position", inline=True)
comment(0x9A99, "Return", inline=True)

# net_error_lookup_data (&9798) — error class offset table
comment(0x9A9A, "Network error lookup table (12 bytes)\n"
    "\n"
    "Each byte is an offset into error_msg_table.\n"
    "Indices 0-7 are keyed by error class (reply AND 7).\n"
    "Index 8 is used by build_no_reply_error.\n"
    "Indices 9-11 point to suffix strings appended\n"
    "after the station address in compound errors.")
comment(0x9A9A, "Class 0: &A0 \"Line jammed\"", inline=True)
comment(0x9A9B, "Class 1: &A1 \"Net error\"", inline=True)
# UNMAPPED: comment(0x97AF, "Class 2: &A2 \"Station\"", inline=True)
# UNMAPPED: comment(0x97B0, "Class 3: &A3 \"No clock\"", inline=True)
comment(0x9A9E, "Class 4: &11 \"Escape\"", inline=True)
comment(0x9A9F, "Class 5: &11 \"Escape\" (duplicate)", inline=True)
comment(0x9AA0, "Class 6: &11 \"Escape\" (duplicate)", inline=True)
comment(0x9AA1, "Class 7: &CB \"Bad option\"", inline=True)
comment(0x9AA2, "Index 8: &A5 \"No reply from station\"", inline=True)
comment(0x9AA3, "Index 9: \" not listening\" suffix", inline=True)
# UNMAPPED: comment(0x97B7, "Index 10: \" on channel\" suffix", inline=True)
comment(0x9AA5, "Index 11: \" not present\" suffix", inline=True)

# error_msg_table (&97A4) — error number + string entries
# UNMAPPED: comment(0x97B9, "Network error message table\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "Each entry is [error_number][string...][null].\n"
# UNMAPPED:     "The error number is the BRK error code stored in\n"
# UNMAPPED:     "the error block at &0100. Entries 0-6 are complete\n"
# UNMAPPED:     "error messages. The last 3 are suffix strings\n"
# UNMAPPED:     "(no error number) appended to class 2 \"Station\"\n"
# UNMAPPED:     "errors to form compound messages like\n"
# UNMAPPED:     "\"Station 1.254 not listening\".")
# UNMAPPED: comment(0x97B9, "Error &A0: Line jammed", inline=True)
comment(0x9AB2, "Null terminator", inline=True)
comment(0x9AB3, "Error &A1: Net error", inline=True)
# UNMAPPED: comment(0x97D0, "Null terminator", inline=True)
comment(0x9ABE, "Error &A2: Station", inline=True)
# UNMAPPED: comment(0x97D9, "Null terminator", inline=True)
# UNMAPPED: comment(0x97DA, "Error &A3: No clock", inline=True)
comment(0x9AD0, "Null terminator", inline=True)
comment(0x9AD1, "Error &11: Escape", inline=True)
# UNMAPPED: comment(0x97EB, "Null terminator", inline=True)
comment(0x9AD9, "Error &CB: Bad option", inline=True)
# UNMAPPED: comment(0x97F7, "Null terminator", inline=True)
# UNMAPPED: comment(0x97F8, "Error &A5: No reply from station", inline=True)
# UNMAPPED: comment(0x980E, "Null terminator", inline=True)
# UNMAPPED: comment(0x980F, "Suffix: \" not listening\"", inline=True)
comment(0x9B0A, "Null terminator", inline=True)
comment(0x9B0B, "Suffix: \" on channel\"", inline=True)
comment(0x9B16, "Null terminator", inline=True)
comment(0x9B17, "Suffix: \" not present\"", inline=True)
# UNMAPPED: comment(0x9836, "Null terminator", inline=True)

# init_tx_ptr_and_send: init TX pointer and send packet (&9822-&982A)
comment(0x9B24, "X=&C0: TX control block base (low)", inline=True)
comment(0x9B26, "Set TX pointer low", inline=True)
comment(0x9B28, "X=0: TX control block base (high)", inline=True)
comment(0x9B2A, "Set TX pointer high (page 0)", inline=True)

# send_net_packet: send network packet with retry (&982A-&9872)
comment(0x9B2C, "Load retry count from workspace", inline=True)
comment(0x9B2F, "Non-zero: use configured retry count", inline=True)
comment(0x9B31, "A=&FF: default retry count (255)", inline=True)
comment(0x9B33, "Y=&60: timeout value", inline=True)
comment(0x9B35, "Push retry count", inline=True)
comment(0x9B36, "A=&60: copy timeout to A", inline=True)
comment(0x9B37, "Push timeout", inline=True)
comment(0x9B38, "X=0: TX pointer index", inline=True)
comment(0x9B3A, "Load first byte of TX control block", inline=True)
comment(0x9B3C, "Restore control byte (overwritten by result code on retry)", inline=True)
comment(0x9B3E, "Push control byte", inline=True)
comment(0x9B3F, "Poll ADLC until line idle", inline=True)
# TX result code classification:
#   &00 (00000000) = success        -> bit 6 clear -> BPL taken
#   &40 (01000000) = line jammed    -> bit 6 set, bits 5-0 = 0 -> BEQ fatal
#   &41 (01000001) = not listening  -> bit 6 set, bits 5-0 != 0 -> retryable
#   &43 (01000011) = no clock       -> bit 6 set, bits 5-0 != 0 -> retryable
#   &44 (01000100) = bad ctrl byte  -> bit 6 set, bits 5-0 != 0 -> retryable
comment(0x9B42, "ASL: bit 6 (error flag) into N", inline=True)
comment(0x9B43, "N=0 (bit 6 clear): success", inline=True)
comment(0x9B45, "ASL: shift away error flag, keep error type", inline=True)
comment(0x9B46, "Z=1 (no type bits): fatal; Z=0: retryable", inline=True)
comment(0x9B48, "Check for escape condition", inline=True)
comment(0x9B4B, "Pull control byte", inline=True)
comment(0x9B4C, "Restore to X", inline=True)
comment(0x9B4D, "Pull timeout", inline=True)
comment(0x9B4E, "Restore to Y", inline=True)
comment(0x9B4F, "Pull retry count", inline=True)
comment(0x9B50, "Zero retries remaining: try alternate", inline=True)
comment(0x9B52, "Decrement retry counter", inline=True)
comment(0x9B54, "Push updated retry count", inline=True)
comment(0x9B55, "Copy timeout to A", inline=True)
comment(0x9B56, "Push timeout for delay loop", inline=True)
comment(0x9B57, "Copy control byte to A", inline=True)
comment(0x9B58, "Inner delay: decrement X", inline=True)
comment(0x9B59, "Loop until X=0", inline=True)
comment(0x9B5B, "Decrement outer counter Y", inline=True)
comment(0x9B5C, "Loop until Y=0", inline=True)
comment(0x9B5E, "ALWAYS branch: retry transmission", inline=True)
comment(0x9B60, "Compare retry count with alternate", inline=True)
comment(0x9B63, "Different: go to error handling", inline=True)
comment(0x9B65, "A=&80: set escapable flag", inline=True)
comment(0x9B67, "Mark as escapable for second phase", inline=True)
comment(0x9B69, "ALWAYS branch: retry with escapable", inline=True)
comment(0x9B6B, "Result code to X", inline=True)
comment(0x9B6C, "Jump to classify reply and return", inline=True)
comment(0x9B6F, "Pull control byte", inline=True)
comment(0x9B70, "Pull timeout", inline=True)
comment(0x9B71, "Pull retry count", inline=True)
comment(0x9B72, "Clear escapable flag and return", inline=True)

# pass_txbuf_init_table (&9873) — pass-through TXCB template
comment(0x9B75, "Pass-through TX buffer template (12 bytes)\n"
    "\n"
    "Overlaid onto the TX control block by\n"
    "setup_pass_txbuf for pass-through operations.\n"
    "Offsets marked &FD are skipped, preserving the\n"
    "existing destination station and network. Buffer\n"
    "addresses point to &0D3A-&0D3E in NMI workspace.\n"
    "Original TX buffer values are pushed on the stack\n"
    "and restored after transmission.")
comment(0x9B75, "Offset 0: ctrl = &88 (immediate TX)", inline=True)
comment(0x9B76, "Offset 1: port = &00 (immediate op)", inline=True)
comment(0x9B77, "Offset 2: &FD skip (preserve dest stn)", inline=True)
# UNMAPPED: comment(0x988B, "Offset 3: &FD skip (preserve dest net)", inline=True)
# UNMAPPED: comment(0x988C, "Offset 4: buf start lo (&3A)", inline=True)
comment(0x9B7A, "Offset 5: buf start hi (&0D) -> &0D3A", inline=True)
# UNMAPPED: comment(0x988E, "Offset 6: extended addr fill (&FF)", inline=True)
# UNMAPPED: comment(0x988F, "Offset 7: extended addr fill (&FF)", inline=True)
comment(0x9B7D, "Offset 8: buf end lo (&3E)", inline=True)
# UNMAPPED: comment(0x9891, "Offset 9: buf end hi (&0D) -> &0D3E", inline=True)
# UNMAPPED: comment(0x9892, "Offset 10: extended addr fill (&FF)", inline=True)
comment(0x9B80, "Offset 11: extended addr fill (&FF)", inline=True)

# init_tx_ptr_for_pass: set up TX pointer for pass-through (&987F-&9886)
comment(0x9B81, "Y=&C0: TX control block base (low)", inline=True)
comment(0x9B83, "Set TX pointer low byte", inline=True)
comment(0x9B85, "Y=0: TX control block base (high)", inline=True)
comment(0x9B87, "Set TX pointer high byte", inline=True)

# setup_pass_txbuf: init TX buffer from template for pass-through (&9887-&98F2)
comment(0x9B89, "Y=&0B: 12 bytes to process (0-11)", inline=True)
comment(0x9B8B, "Load template byte for this offset", inline=True)
comment(0x9B8E, "Is it &FD (skip marker)?", inline=True)
comment(0x9B90, "Yes: skip this offset, don't modify", inline=True)
comment(0x9B92, "Load existing TX buffer byte", inline=True)
comment(0x9B94, "Save original value on stack", inline=True)
comment(0x9B95, "Copy template value to A", inline=True)
comment(0x9B96, "Store template value to TX buffer", inline=True)
comment(0x9B98, "Next offset (descending)", inline=True)
comment(0x9B99, "Loop until all 12 bytes processed", inline=True)
comment(0x9B9B, "Load pass-through control value", inline=True)
comment(0x9B9E, "Push control value", inline=True)
comment(0x9B9F, "A=&FF (Y is &FF after loop)", inline=True)
comment(0x9BA0, "Push &FF as timeout", inline=True)
comment(0x9BA1, "X=0: TX pointer index", inline=True)
comment(0x9BA3, "Load control byte from TX CB", inline=True)
comment(0x9BA5, "Write control byte to start TX", inline=True)
comment(0x9BA7, "Save control byte on stack", inline=True)
comment(0x9BA8, "Poll ADLC until line idle", inline=True)
comment(0x9BAB, "Shift result: check bit 6 (success)", inline=True)
comment(0x9BAC, "Bit 6 clear: transmission complete", inline=True)
comment(0x9BAE, "Shift result: check bit 5 (fatal)", inline=True)
comment(0x9BAF, "Non-zero (not fatal): retry", inline=True)
comment(0x9BB1, "X=0: clear error status", inline=True)
comment(0x9BB3, "Jump to fix up reply status", inline=True)

# c98b4: poll ADLC status register (&98B4-&98C8)
comment(0x9BB6, "Shift ws_0d60 left to poll ADLC", inline=True)
comment(0x9BB9, "Bit not set: keep polling", inline=True)
comment(0x9BBB, "Copy TX pointer low to NMI TX block", inline=True)
comment(0x9BBD, "Store in NMI TX block low", inline=True)
comment(0x9BBF, "Copy TX pointer high", inline=True)
comment(0x9BC1, "Store in NMI TX block high", inline=True)
comment(0x9BC3, "Begin Econet frame transmission", inline=True)
comment(0x9BC6, "Read TX status byte", inline=True)
comment(0x9BC8, "Bit 7 set: still transmitting", inline=True)
comment(0x9BCA, "Return with result in A", inline=True)

# c98c9: pass-through retry loop (&98C9-&98DC)
comment(0x9BCB, "Pull control byte", inline=True)
comment(0x9BCC, "Restore to X", inline=True)
comment(0x9BCD, "Pull timeout", inline=True)
comment(0x9BCE, "Restore to Y", inline=True)
comment(0x9BCF, "Pull retry count", inline=True)
comment(0x9BD0, "Zero retries: go to error handling", inline=True)
comment(0x9BD2, "Decrement retry counter", inline=True)
comment(0x9BD4, "Push updated retry count", inline=True)
comment(0x9BD5, "Copy timeout to A", inline=True)
comment(0x9BD6, "Push timeout", inline=True)
comment(0x9BD7, "Copy control byte to A", inline=True)
comment(0x9BD8, "Inner delay loop: decrement X", inline=True)
comment(0x9BD9, "Loop until X=0", inline=True)
comment(0x9BDB, "Decrement outer counter Y", inline=True)
comment(0x9BDC, "Loop until Y=0", inline=True)
comment(0x9BDE, "ALWAYS branch: retry transmission", inline=True)

# c98de: pass-through restore TX buffer (&98DE-&98F2)
comment(0x9BE0, "Pull control byte (discard)", inline=True)
comment(0x9BE1, "Pull timeout (discard)", inline=True)
comment(0x9BE2, "Pull retry count (discard)", inline=True)
comment(0x9BE3, "Y=0: start restoring from offset 0", inline=True)
comment(0x9BE5, "Load template byte for this offset", inline=True)
comment(0x9BE8, "Is it &FD (skip marker)?", inline=True)
comment(0x9BEA, "Yes: don't restore this offset", inline=True)
comment(0x9BEC, "Pull original value from stack", inline=True)
comment(0x9BED, "Restore original TX buffer byte", inline=True)
comment(0x9BEF, "Next offset (ascending)", inline=True)
comment(0x9BF0, "Processed all 12 bytes?", inline=True)
comment(0x9BF2, "No: continue restoring", inline=True)
comment(0x9BF4, "Return with TX buffer restored", inline=True)

# load_text_ptr_and_parse: load text pointer from FS options (&98F3-&9920)
comment(0x9BF5, "Y=1: start at second byte of pointer", inline=True)
comment(0x9BF7, "Load pointer byte from FS options", inline=True)
comment(0x9BF9, "Store in OS text pointer", inline=True)
comment(0x9BFC, "Decrement index", inline=True)
comment(0x9BFD, "Loop until both bytes copied", inline=True)
comment(0x9BFF, "Y=0: reset index for string reading", inline=True)

# gsread_to_buf: read string using GSINIT/GSREAD into buffer (&98FF-&9920)
comment(0x9C00, "X=&FF: pre-increment for buffer index", inline=True)
comment(0x9C02, "C=0: initialise for string input", inline=True)
comment(0x9C03, "GSINIT: initialise string reading", inline=True)
comment(0x9C06, "Z set (empty string): store terminator", inline=True)
comment(0x9C08, "GSREAD: read next character", inline=True)
comment(0x9C0B, "C set: end of string reached", inline=True)
comment(0x9C0D, "Advance buffer index", inline=True)
comment(0x9C0E, "Store character in l0e30 buffer", inline=True)
comment(0x9C11, "ALWAYS branch: read next character", inline=True)
comment(0x9C13, "Advance past last character", inline=True)
comment(0x9C14, "A=CR: terminate filename", inline=True)
comment(0x9C16, "Store CR terminator in buffer", inline=True)
comment(0x9C19, "A=&30: low byte of l0e30 buffer", inline=True)
comment(0x9C1B, "Set command text pointer low", inline=True)
comment(0x9C1D, "A=&0E: high byte of l0e30 buffer", inline=True)
comment(0x9C1F, "Set command text pointer high", inline=True)
comment(0x9C21, "Return with buffer filled", inline=True)

# FS command iteration setup (&9921-&9981)
comment(0x9C22, "Set up transfer parameters", inline=True)
comment(0x9C25, "Load text pointer and parse filename", inline=True)
comment(0x9C28, "Set owner-only access mask", inline=True)
comment(0x9C2B, "Parse access prefix from filename", inline=True)
comment(0x9C2E, "Load last byte flag", inline=True)
comment(0x9C30, "Positive (not last): display file info", inline=True)
comment(0x9C32, "Is it &FF (last entry)?", inline=True)
comment(0x9C34, "Yes: copy arg and iterate", inline=True)
comment(0x9C36, "Other value: return with flag", inline=True)
comment(0x9C39, "Copy argument to buffer at X=0", inline=True)
comment(0x9C3C, "Y=2: enumerate directory command", inline=True)

# do_fs_cmd_iteration: send FS command and process response (&993D-&9981)
comment(0x9C3E, "A=&92: FS port number", inline=True)
comment(0x9C40, "Set escapable flag to &92", inline=True)
comment(0x9C42, "Store port number in TX buffer", inline=True)
comment(0x9C45, "Send request to file server", inline=True)
comment(0x9C48, "Y=6: offset to response cycle flag", inline=True)
comment(0x9C4A, "Load cycle flag from FS options", inline=True)
comment(0x9C4C, "Non-zero: already initialised", inline=True)
comment(0x9C4E, "Copy FS options to zero page first", inline=True)
comment(0x9C51, "Then copy workspace to FS options", inline=True)
comment(0x9C54, "Branch to continue (C clear from JSR)", inline=True)
comment(0x9C56, "Copy workspace to FS options first", inline=True)
comment(0x9C59, "Then copy FS options to zero page", inline=True)
comment(0x9C5C, "Y=4: loop counter", inline=True)
comment(0x9C5E, "Load address byte from zero page", inline=True)
comment(0x9C60, "Save to TXCB end pointer", inline=True)
comment(0x9C62, "Add offset from buffer", inline=True)
comment(0x9C65, "Store sum in fs_work area", inline=True)
comment(0x9C67, "Advance to next byte", inline=True)
comment(0x9C68, "Decrement counter", inline=True)
comment(0x9C69, "Loop for all 4 bytes", inline=True)
comment(0x9C6B, "Set carry for subtraction", inline=True)
comment(0x9C6C, "Subtract high offset", inline=True)
comment(0x9C6F, "Store result in fs_work_7", inline=True)
comment(0x9C71, "Format filename for display", inline=True)
comment(0x9C74, "Send TXCB and swap addresses", inline=True)
comment(0x9C77, "X=2: copy 3 offset bytes", inline=True)
comment(0x9C79, "Load offset byte from l0f10", inline=True)
comment(0x9C7C, "Store in l0f05 for next iteration", inline=True)
comment(0x9C7F, "Decrement counter", inline=True)
comment(0x9C80, "Loop until all bytes copied", inline=True)
comment(0x9C82, "Jump to receive and process reply", inline=True)

# send_txcb_swap_addrs: send TX block and swap start/end (&9984-&99AE)
comment(0x9C85, "Compare 5-byte handle with current", inline=True)
comment(0x9C88, "Match: no need to send, return", inline=True)
comment(0x9C8A, "A=&92: FS reply port number", inline=True)
comment(0x9C8C, "Set TXCB port", inline=True)
comment(0x9C8E, "X=3: copy 4 bytes", inline=True)
comment(0x9C90, "Load TXCB end pointer byte", inline=True)
comment(0x9C92, "Store in TXCB start pointer", inline=True)
comment(0x9C94, "Load new end address from fs_work", inline=True)
comment(0x9C96, "Store in TXCB end pointer", inline=True)
comment(0x9C98, "Decrement counter", inline=True)
comment(0x9C99, "Loop for all 4 bytes", inline=True)
comment(0x9C9B, "A=&7F: control byte for data transfer", inline=True)
comment(0x9C9D, "Set TXCB control byte", inline=True)
comment(0x9C9F, "Wait for network TX acknowledgement", inline=True)
comment(0x9CA2, "Y=3: compare 4 bytes", inline=True)
comment(0x9CA4, "Load TXCB end byte", inline=True)
comment(0x9CA7, "Compare with expected end address", inline=True)
comment(0x9CAA, "Mismatch: resend from start", inline=True)
comment(0x9CAC, "Decrement counter", inline=True)
comment(0x9CAD, "Loop until all 4 bytes match", inline=True)
comment(0x9CAF, "Return (all bytes match)", inline=True)

# File info display and directory iteration (&99AF-&9A5D)
comment(0x9CB0, "Z set: directory entry display", inline=True)
comment(0x9CB2, "Non-zero: jump to OSWORD dispatch", inline=True)
comment(0x9CB5, "X=4: loop counter for 4 iterations", inline=True)
comment(0x9CB7, "Y=&0E: FS options offset for addresses", inline=True)
comment(0x9CB9, "Set carry for subtraction", inline=True)
comment(0x9CBA, "Load address byte from FS options", inline=True)
comment(0x9CBC, "Save to workspace (port_ws_offset)", inline=True)
comment(0x9CBF, "Y -= 4 to point to paired offset", inline=True)
comment(0x9CC2, "Subtract paired value", inline=True)
comment(0x9CC4, "Store difference in l0f03 buffer", inline=True)
comment(0x9CC7, "Push difference", inline=True)
comment(0x9CC8, "Load paired value from FS options", inline=True)
comment(0x9CCA, "Save to workspace", inline=True)
comment(0x9CCD, "Pull difference back", inline=True)
comment(0x9CCE, "Store in FS options for display", inline=True)
comment(0x9CD0, "Advance Y by 5 for next field", inline=True)
comment(0x9CD3, "Decrement loop counter", inline=True)
comment(0x9CD4, "Loop for all 4 address pairs", inline=True)
comment(0x9CD6, "Y=9: copy 9 bytes of options data", inline=True)
comment(0x9CD8, "Load FS options byte", inline=True)
comment(0x9CDA, "Store in l0f03 buffer", inline=True)
comment(0x9CDD, "Decrement index", inline=True)
comment(0x9CDE, "Loop until all 9 bytes copied", inline=True)
comment(0x9CE0, "A=&91: FS port for info request", inline=True)
comment(0x9CE2, "Set escapable flag", inline=True)
comment(0x9CE4, "Store port in TX buffer", inline=True)
comment(0x9CE7, "Store in fs_error_ptr", inline=True)
comment(0x9CE9, "X=&0B: copy argument at offset 11", inline=True)
comment(0x9CEB, "Copy argument to TX buffer", inline=True)
comment(0x9CEE, "Y=1: info sub-command", inline=True)
comment(0x9CF0, "Load last byte flag", inline=True)
comment(0x9CF2, "Is it 7 (catalogue info)?", inline=True)
comment(0x9CF4, "Save comparison result", inline=True)
comment(0x9CF5, "Not 7: keep Y=1", inline=True)
comment(0x9CF7, "Y=&1D: extended info command", inline=True)
comment(0x9CF9, "Send request to file server", inline=True)
comment(0x9CFC, "Format filename for display", inline=True)
comment(0x9CFF, "Restore comparison flags", inline=True)
comment(0x9D00, "Not catalogue info: show short format", inline=True)
comment(0x9D02, "X=0: start at first byte", inline=True)
comment(0x9D04, "ALWAYS branch to store and display", inline=True)
comment(0x9D06, "Load file handle from l0f05", inline=True)
comment(0x9D09, "Check and set up TXCB for transfer", inline=True)
comment(0x9D0C, "Receive and process reply", inline=True)
comment(0x9D0F, "Store result byte in l0f08", inline=True)
comment(0x9D12, "Y=&0E: protection bits offset", inline=True)
comment(0x9D14, "Load access byte from l0f05", inline=True)
comment(0x9D17, "Extract protection bit flags", inline=True)
comment(0x9D1A, "Zero: use reply buffer data", inline=True)
comment(0x9D1C, "Load file info byte from l0ef7", inline=True)
comment(0x9D1F, "Store in FS options at offset Y", inline=True)
comment(0x9D21, "Advance to next byte", inline=True)
comment(0x9D22, "Y=&12: end of protection fields?", inline=True)
comment(0x9D24, "No: copy next byte", inline=True)
comment(0x9D26, "Load display flag from l0e06", inline=True)
comment(0x9D29, "Zero: skip display, return", inline=True)
comment(0x9D2B, "Y=&F4: index into l0fff for filename", inline=True)
comment(0x9D2D, "Load filename character from l10f3", inline=True)
comment(0x9D30, "Print character via OSASCI", inline=True)
comment(0x9D33, "Advance to next character", inline=True)
comment(0x9D34, "Printed all 12 characters?", inline=True)
comment(0x9D34, "No: print next character", inline=True)
comment(0x9D36, "Y=5: offset for access string", inline=True)
comment(0x9D38, "Print 5 hex bytes (access info)", inline=True)
comment(0x9D3B, "Print load and exec addresses", inline=True)
comment(0x9D3E, "Print newline", inline=True)
comment(0x9D41, "Jump to return with last flag", inline=True)

# print_load_exec_addrs: print load and exec addresses (&9A45-&9A4E)
comment(0x9D44, "Y=9: offset for exec address", inline=True)
comment(0x9D46, "Print 5 hex bytes (exec address)", inline=True)
comment(0x9D49, "Y=&0C: offset for length (3 bytes)", inline=True)
comment(0x9D4B, "X=3: print 3 bytes only", inline=True)
comment(0x9D4D, "ALWAYS branch to print routine", inline=True)

# print_5_hex_bytes: print hex bytes from FS options (&9A50-&9A5D)
comment(0x9D4F, "X=4: print 5 bytes (4 to 0)", inline=True)
comment(0x9D51, "Load byte from FS options at offset Y", inline=True)
comment(0x9D53, "Print as 2-digit hex", inline=True)
comment(0x9D56, "Decrement byte offset", inline=True)
comment(0x9D57, "Decrement byte count", inline=True)
comment(0x9D58, "Loop until all bytes printed", inline=True)
comment(0x9D5A, "A=' ': space separator", inline=True)
comment(0x9D5C, "Print space via OSASCI and return", inline=True)

# copy_fsopts_to_zp: copy FS options to zero page (&9A60-&9A71)
comment(0x9D5F, "Y=5: copy 4 bytes (offsets 2-5)", inline=True)
comment(0x9D61, "Load byte from FS options", inline=True)
comment(0x9D63, "Store in zero page at l00ae+Y", inline=True)
comment(0x9D66, "Decrement index", inline=True)
comment(0x9D67, "Below offset 2?", inline=True)
comment(0x9D69, "No: copy next byte", inline=True)
comment(0x9D6B, "Y += 5", inline=True)
comment(0x9D6C, "Y += 4", inline=True)
comment(0x9D6D, "(continued)", inline=True)
comment(0x9D6E, "(continued)", inline=True)
comment(0x9D6F, "(continued)", inline=True)
comment(0x9D70, "Return", inline=True)

# copy_workspace_to_fsopts: copy workspace to FS options (&9A72-&9A83)
comment(0x9D71, "Y=&0D: copy bytes from offset &0D down", inline=True)
comment(0x9D73, "Transfer X to A", inline=True)
comment(0x9D74, "Store byte in FS options at offset Y", inline=True)
comment(0x9D76, "Load next workspace byte from l0f02+Y", inline=True)
comment(0x9D79, "Decrement index", inline=True)
comment(0x9D7A, "Below offset 2?", inline=True)
comment(0x9D7C, "No: copy next byte", inline=True)
comment(0x9D7E, "Y -= 4", inline=True)
comment(0x9D7F, "Y -= 3", inline=True)
comment(0x9D80, "(continued)", inline=True)
comment(0x9D81, "(continued)", inline=True)
comment(0x9D82, "Return", inline=True)

# c9a84: discard stacked value and return (&9A84-&9A87)
comment(0x9D83, "Discard stacked value", inline=True)
comment(0x9D84, "Restore Y from fs_block_offset", inline=True)
comment(0x9D86, "Return (handle already matches)", inline=True)

# check_and_setup_txcb: check handle and set up TX control block (&9A88-&9ADB)
comment(0x9D87, "Save port/sub-function on stack", inline=True)
comment(0x9D88, "Compare 5-byte handle with current", inline=True)
comment(0x9D8B, "Match: discard port and return", inline=True)
comment(0x9D8D, "X=0: loop start", inline=True)
comment(0x9D8F, "Y=4: copy 4 bytes", inline=True)
comment(0x9D91, "Clear l0f08 (transfer size low)", inline=True)
comment(0x9D94, "Clear l0f09 (transfer size high)", inline=True)
comment(0x9D97, "Clear carry for addition", inline=True)
comment(0x9D98, "Load address byte from zero page", inline=True)
comment(0x9D9A, "Store in TXCB start pointer", inline=True)
comment(0x9D9C, "Add offset from l0f06", inline=True)
comment(0x9D9F, "Store sum in TXCB end pointer", inline=True)
comment(0x9DA1, "Also update load address", inline=True)
comment(0x9DA3, "Advance to next byte", inline=True)
comment(0x9DA4, "Decrement counter", inline=True)
comment(0x9DA5, "Loop for all 4 bytes", inline=True)
comment(0x9DA7, "Carry set: overflow, use limit", inline=True)
comment(0x9DA9, "Set carry for subtraction", inline=True)
comment(0x9DAA, "Load computed end address", inline=True)
comment(0x9DAD, "Subtract maximum from fs_work_4", inline=True)
comment(0x9DB0, "Advance to next byte", inline=True)
comment(0x9DB1, "Decrement counter", inline=True)
comment(0x9DB2, "Loop for all bytes", inline=True)
comment(0x9DB4, "Below limit: keep computed end", inline=True)
comment(0x9DB6, "X=3: copy 4 bytes of limit", inline=True)
comment(0x9DB8, "Load limit from fs_work_4", inline=True)
comment(0x9DBA, "Store as TXCB end", inline=True)
comment(0x9DBC, "Decrement counter", inline=True)
comment(0x9DBD, "Loop for all 4 bytes", inline=True)
comment(0x9DBF, "Pull port from stack", inline=True)
comment(0x9DC0, "Push back (keep for later)", inline=True)
comment(0x9DC1, "Save flags (carry = overflow state)", inline=True)
comment(0x9DC2, "Set TXCB port number", inline=True)
comment(0x9DC4, "A=&80: control byte for data request", inline=True)
comment(0x9DC6, "Set TXCB control byte", inline=True)
comment(0x9DC8, "Init TX pointer and send packet", inline=True)
comment(0x9DCB, "Load error pointer", inline=True)
comment(0x9DCD, "Init TXCB port from error pointer", inline=True)
comment(0x9DD0, "Restore overflow flags", inline=True)
comment(0x9DD1, "Carry set: discard and return", inline=True)
comment(0x9DD3, "A=&91: FS reply port", inline=True)
comment(0x9DD5, "Set TXCB port for reply", inline=True)
comment(0x9DD7, "Wait for TX acknowledgement", inline=True)
comment(0x9DDA, "Non-zero (not done): retry send", inline=True)

# c9add: OSWORD sub-operation dispatch (&9ADD-&9B85)
comment(0x9DDC, "Store sub-operation code", inline=True)
comment(0x9DDF, "Compare with 7", inline=True)
comment(0x9DE1, "Below 7: handle operations 1-6", inline=True)
comment(0x9DE3, "Above 7: jump to handle via finalise", inline=True)
comment(0x9DE5, "Equal to 7: jump to directory display", inline=True)
comment(0x9DE8, "Compare with 6", inline=True)
comment(0x9DEA, "6: delete file operation", inline=True)
comment(0x9DEC, "Compare with 5", inline=True)
comment(0x9DEE, "5: read catalogue info", inline=True)
comment(0x9DF0, "Compare with 4", inline=True)
comment(0x9DF2, "4: write file attributes", inline=True)
comment(0x9DF4, "Compare with 1", inline=True)
comment(0x9DF6, "1: read file info", inline=True)
comment(0x9DF8, "Shift left twice: A*4", inline=True)
comment(0x9DF9, "A*4", inline=True)
comment(0x9DFA, "Copy to Y as index", inline=True)
comment(0x9DFB, "Y -= 3 to get FS options offset", inline=True)
comment(0x9DFE, "X=3: copy 4 bytes", inline=True)
comment(0x9E00, "Load byte from FS options at offset Y", inline=True)
comment(0x9E02, "Store in l0f06 buffer", inline=True)
comment(0x9E05, "Decrement source offset", inline=True)
comment(0x9E06, "Decrement byte count", inline=True)
comment(0x9E07, "Loop for all 4 bytes", inline=True)
comment(0x9E09, "X=5: copy arg to buffer at offset 5", inline=True)
comment(0x9E0B, "ALWAYS branch to copy and send", inline=True)
comment(0x9E0D, "Get access bits for file", inline=True)
comment(0x9E10, "Store access byte in l0f0e", inline=True)
comment(0x9E13, "Y=9: source offset in FS options", inline=True)
comment(0x9E15, "X=8: copy 8 bytes to buffer", inline=True)
comment(0x9E17, "Load FS options byte", inline=True)
comment(0x9E19, "Store in l0f05 buffer", inline=True)
comment(0x9E1C, "Decrement source offset", inline=True)
comment(0x9E1D, "Decrement byte count", inline=True)
comment(0x9E1E, "Loop for all 8 bytes", inline=True)
comment(0x9E20, "X=&0A: buffer offset for argument", inline=True)
comment(0x9E22, "Copy argument to buffer", inline=True)
comment(0x9E25, "Y=&13: OSWORD &13 (NFS operation)", inline=True)
comment(0x9E27, "ALWAYS branch to send request", inline=True)
comment(0x9E29, "Copy argument to buffer at X=0", inline=True)
comment(0x9E2C, "Y=&14: delete file command", inline=True)
comment(0x9E2E, "Set V flag (no directory check)", inline=True)
comment(0x9E31, "Send request with V set", inline=True)
comment(0x9E34, "Carry set: error, jump to finalise", inline=True)
comment(0x9E36, "No error: return with last flag", inline=True)
comment(0x9E39, "Get access bits for file", inline=True)
comment(0x9E3C, "Store in l0f06", inline=True)
comment(0x9E3F, "X=2: buffer offset", inline=True)
comment(0x9E41, "ALWAYS branch to copy and send", inline=True)
comment(0x9E43, "X=1: buffer offset", inline=True)
comment(0x9E45, "Copy argument to buffer", inline=True)
comment(0x9E48, "Y=&12: open file command", inline=True)
comment(0x9E4A, "Send open file request", inline=True)
comment(0x9E4D, "Load reply handle from l0f11", inline=True)
comment(0x9E50, "Clear l0f11", inline=True)
comment(0x9E53, "Clear l0f14", inline=True)
comment(0x9E56, "Get protection bits", inline=True)
comment(0x9E59, "Load file handle from l0f05", inline=True)
comment(0x9E5C, "Zero: file not found, return", inline=True)
comment(0x9E5E, "Y=&0E: store access bits", inline=True)
comment(0x9E60, "Store access byte in FS options", inline=True)
comment(0x9E62, "Y=&0D", inline=True)
comment(0x9E63, "X=&0C: copy 12 bytes of file info", inline=True)
comment(0x9E65, "Load reply byte from l0f05+X", inline=True)
comment(0x9E68, "Store in FS options at offset Y", inline=True)
comment(0x9E6A, "Decrement destination offset", inline=True)
comment(0x9E6B, "Decrement source counter", inline=True)
comment(0x9E6C, "Loop for all 12 bytes", inline=True)
comment(0x9E6E, "X=1 (INX from 0)", inline=True)
comment(0x9E6F, "X=2", inline=True)
comment(0x9E70, "Y=&11: FS options offset", inline=True)
comment(0x9E72, "Load extended info byte from l0f12", inline=True)
comment(0x9E75, "Store in FS options", inline=True)
comment(0x9E77, "Decrement destination offset", inline=True)
comment(0x9E78, "Decrement source counter", inline=True)
comment(0x9E79, "Loop until all copied", inline=True)
comment(0x9E7B, "Reload file handle", inline=True)
comment(0x9E7E, "Transfer to A", inline=True)
comment(0x9E7F, "Jump to finalise and return", inline=True)
comment(0x9E82, "Unreachable dead code (3 bytes)\n"
    "\n"
    "Duplicate of the JMP at &9B92 immediately above.\n"
    "Unreachable after the unconditional JMP and\n"
    "unreferenced. Likely a development remnant.")
comment(0x9E82, "Dead: duplicate JMP finalise_and_return", inline=True)

# format_filename_field: format filename for display (&9B86-&9BAE)
comment(0x9E82, "Y=0: destination index", inline=True)
comment(0x9E84, "Load source offset from l0f03", inline=True)
comment(0x9E87, "Non-zero: copy from l0f05 buffer", inline=True)
comment(0x9E89, "Load character from command line", inline=True)
comment(0x9E8B, "Below '!' (control/space)?", inline=True)
comment(0x9E8D, "Yes: pad with spaces", inline=True)
comment(0x9E8F, "Store printable character in l10f3", inline=True)
comment(0x9E92, "Advance to next character", inline=True)
comment(0x9E93, "Loop for more characters", inline=True)
comment(0x9E95, "A=' ': space for padding", inline=True)
comment(0x9E97, "Store space in display buffer", inline=True)
comment(0x9E9A, "Advance index", inline=True)
comment(0x9E9B, "Filled all 12 characters?", inline=True)
comment(0x9E9D, "No: pad more spaces", inline=True)
comment(0x9E9F, "Return with field formatted", inline=True)
comment(0x9EA0, "Advance source and destination", inline=True)
comment(0x9EA1, "INY", inline=True)
comment(0x9EA2, "Load byte from l0f05 buffer", inline=True)
comment(0x9EA5, "Store in display buffer l10f3", inline=True)
comment(0x9EA8, "Bit 7 clear: more characters", inline=True)
comment(0x9EAA, "Return (bit 7 set = terminator)", inline=True)

# OSFIND dispatch: open/close file channels (&9BAF-&9CB8)
comment(0x9EAB, "Verify workspace checksum", inline=True)
comment(0x9EAE, "Store result as last byte flag", inline=True)
comment(0x9EB0, "Set FS options pointer", inline=True)
comment(0x9EB3, "OR with 0 to set flags", inline=True)
comment(0x9EB5, "Positive: handle sub-operations", inline=True)
comment(0x9EB7, "Shift left to check bit 6", inline=True)
comment(0x9EB8, "Zero (was &80): close channel", inline=True)
comment(0x9EBA, "Other: process all FCBs first", inline=True)
comment(0x9EBD, "Transfer Y to A", inline=True)
comment(0x9EBE, "Compare with &20 (space)", inline=True)
comment(0x9EC0, "Above &20: check further", inline=True)
comment(0x9EC2, "Below &20: invalid channel char", inline=True)
comment(0x9EC5, "Compare with '0'", inline=True)
comment(0x9EC7, "Above '0': invalid channel char", inline=True)
comment(0x9EC9, "Process all matching FCBs", inline=True)
comment(0x9ECC, "Transfer Y to A (FCB index)", inline=True)
comment(0x9ECD, "Push FCB index", inline=True)
comment(0x9ECE, "Copy to X", inline=True)
comment(0x9ECF, "Y=0: clear counter", inline=True)
comment(0x9ED1, "Clear last byte flag", inline=True)
comment(0x9ED3, "Clear block offset", inline=True)
comment(0x9ED5, "Load channel data from l1010+X", inline=True)
comment(0x9ED8, "Store in FS options at Y", inline=True)
comment(0x9EDA, "Advance X by 8 (next FCB field)", inline=True)
comment(0x9EDD, "Advance destination index", inline=True)
comment(0x9EDE, "Copied all 4 channel fields?", inline=True)
comment(0x9EE0, "No: copy next field", inline=True)
comment(0x9EE2, "Pull saved FCB index", inline=True)
comment(0x9EE3, "Restore to fs_block_offset", inline=True)
comment(0x9EE5, "Compare with 5", inline=True)
comment(0x9EE7, "5 or above: return with last flag", inline=True)
comment(0x9EE9, "Compare Y with 0", inline=True)
comment(0x9EEB, "Non-zero: handle OSFIND with channel", inline=True)
comment(0x9EED, "Y=0 (close): jump to OSFIND open", inline=True)
comment(0x9EF0, "Push sub-function", inline=True)
comment(0x9EF1, "Transfer X to A", inline=True)
comment(0x9EF2, "Push X (FCB slot)", inline=True)
comment(0x9EF3, "Transfer Y to A", inline=True)
comment(0x9EF4, "Push Y (channel char)", inline=True)
comment(0x9EF5, "Check file is not a directory", inline=True)
comment(0x9EF8, "Pull channel char", inline=True)
comment(0x9EF9, "Store channel char as receive attribute", inline=True)
comment(0x9EFC, "Load FCB flag byte from l1030", inline=True)
comment(0x9EFF, "Store in l0f05", inline=True)
comment(0x9F02, "Pull X (FCB slot)", inline=True)
comment(0x9F03, "Restore X", inline=True)
comment(0x9F04, "Pull sub-function", inline=True)
comment(0x9F05, "Shift right: check bit 0", inline=True)
comment(0x9F06, "Zero (OSFIND close): handle close", inline=True)
comment(0x9F08, "Save flags (carry from LSR)", inline=True)
comment(0x9F09, "Push sub-function", inline=True)
comment(0x9F0A, "Load FS options pointer low", inline=True)
comment(0x9F0C, "Load block offset", inline=True)
comment(0x9F0E, "Process all matching FCBs", inline=True)
comment(0x9F11, "Load updated data from l1010", inline=True)
comment(0x9F14, "Store in l0f05", inline=True)
comment(0x9F17, "Pull sub-function", inline=True)
comment(0x9F18, "Store in l0f06", inline=True)
comment(0x9F1B, "Restore flags", inline=True)
comment(0x9F1C, "Transfer Y to A", inline=True)
comment(0x9F1D, "Push Y (offset)", inline=True)
comment(0x9F1E, "Carry clear: read operation", inline=True)
comment(0x9F20, "Y=3: copy 4 bytes", inline=True)
comment(0x9F22, "Load zero page data", inline=True)
comment(0x9F24, "Store in l0f07 buffer", inline=True)
comment(0x9F27, "Decrement source", inline=True)
comment(0x9F28, "Decrement counter", inline=True)
comment(0x9F29, "Loop for all 4 bytes", inline=True)
comment(0x9F2B, "Y=&0D: TX buffer size", inline=True)
comment(0x9F2D, "X=5: argument offset", inline=True)
comment(0x9F2F, "Send TX control block to server", inline=True)
comment(0x9F32, "Store X in last byte flag", inline=True)
comment(0x9F34, "Pull saved offset", inline=True)
comment(0x9F35, "Set connection active flag", inline=True)
comment(0x9F38, "Return with last flag", inline=True)
comment(0x9F3B, "Y=&0C: TX buffer size (smaller)", inline=True)
comment(0x9F3D, "X=2: argument offset", inline=True)
comment(0x9F3F, "Send TX control block", inline=True)
comment(0x9F42, "Store A in last byte flag", inline=True)
comment(0x9F44, "Load FS options pointer low", inline=True)
comment(0x9F46, "Y=2: zero page offset", inline=True)
comment(0x9F48, "Store A in zero page", inline=True)
comment(0x9F4A, "Load buffer byte from l0f05+Y", inline=True)
comment(0x9F4D, "Store in zero page at offset", inline=True)
comment(0x9F4F, "Decrement source X", inline=True)
comment(0x9F50, "Decrement counter Y", inline=True)
comment(0x9F51, "Loop until all bytes copied", inline=True)
comment(0x9F53, "Pull saved offset", inline=True)
comment(0x9F54, "Return with last flag", inline=True)

# c9c5c: OSARGS read/write file pointer (&9C5C-&9CB8)
comment(0x9F57, "Carry set: write file pointer", inline=True)
comment(0x9F59, "Load block offset", inline=True)
comment(0x9F5B, "Convert attribute to channel index", inline=True)
comment(0x9F5E, "Load FS options pointer", inline=True)
comment(0x9F60, "Load FCB low byte from l1000", inline=True)
comment(0x9F63, "Store in zero page pointer low", inline=True)
comment(0x9F66, "Load FCB high byte from l1010", inline=True)
comment(0x9F69, "Store in zero page pointer high", inline=True)
comment(0x9F6C, "Load FCB extent from l1020", inline=True)
comment(0x9F6F, "Store in zero page work area", inline=True)
comment(0x9F72, "A=0: clear high byte", inline=True)
comment(0x9F74, "Store zero in work area high", inline=True)
comment(0x9F77, "ALWAYS branch to return with flag", inline=True)
comment(0x9F79, "Store write value in l0f06", inline=True)
comment(0x9F7C, "Transfer X to A", inline=True)
comment(0x9F7D, "Push X (zero page offset)", inline=True)
comment(0x9F7E, "Y=3: copy 4 bytes", inline=True)
comment(0x9F80, "Load zero page data at offset", inline=True)
comment(0x9F82, "Store in l0f07 buffer", inline=True)
comment(0x9F85, "Decrement source", inline=True)
comment(0x9F86, "Decrement counter", inline=True)
comment(0x9F87, "Loop for all 4 bytes", inline=True)
comment(0x9F89, "Y=&0D: TX buffer size", inline=True)
comment(0x9F8B, "X=5: argument offset", inline=True)
comment(0x9F8D, "Send TX control block", inline=True)
comment(0x9F90, "Store X in last byte flag", inline=True)
comment(0x9F92, "Pull saved zero page offset", inline=True)
comment(0x9F93, "Transfer to Y", inline=True)
comment(0x9F94, "Load block offset (attribute)", inline=True)
comment(0x9F96, "Clear connection active flag", inline=True)
comment(0x9F99, "Convert attribute to channel index", inline=True)
comment(0x9F9C, "Load zero page pointer low", inline=True)
comment(0x9F9F, "Store back to FCB l1000", inline=True)
comment(0x9FA2, "Load zero page pointer high", inline=True)
comment(0x9FA5, "Store back to FCB l1010", inline=True)
comment(0x9FA8, "Load zero page work byte", inline=True)
comment(0x9FAB, "Store back to FCB l1020", inline=True)
comment(0x9FAE, "Return with last flag", inline=True)
comment(0x9FB1, "Process all matching FCBs first", inline=True)

# return_with_last_flag / finalise_and_return (&9CB9-&9CC7)
comment(0x9FB4, "Load last byte flag", inline=True)
comment(0x9FB6, "Push result on stack", inline=True)
comment(0x9FB7, "A=0: clear error flag", inline=True)
comment(0x9FB9, "Clear receive attribute (A=0)", inline=True)
comment(0x9FBC, "Pull result back", inline=True)
comment(0x9FBD, "Restore X from FS options pointer", inline=True)
comment(0x9FBF, "Restore Y from block offset", inline=True)
comment(0x9FC1, "Return to caller", inline=True)

# c9cc8: OSFIND open file dispatch (&9CC8-&9D7D)
comment(0x9FC2, "Compare with 2 (open for output)", inline=True)
comment(0x9FC4, "2 or above: handle file open", inline=True)
comment(0x9FC6, "Transfer to Y (Y=0 or 1)", inline=True)
comment(0x9FC7, "Non-zero (1 = read pointer): copy data", inline=True)
comment(0x9FC9, "A=5: return code for close-all", inline=True)
comment(0x9FCB, "ALWAYS branch to finalise", inline=True)
# UNMAPPED: comment(0x9CE0, "Load reply data byte at Y", inline=True)
# UNMAPPED: comment(0x9CE3, "Store in FS options", inline=True)
# UNMAPPED: comment(0x9CE5, "Decrement index", inline=True)
# UNMAPPED: comment(0x9CE6, "Loop until all bytes copied", inline=True)
# UNMAPPED: comment(0x9CE8, "Clear zero page work low", inline=True)
# UNMAPPED: comment(0x9CEA, "Clear zero page work high", inline=True)
comment(0x9FCD, "Z set: jump to clear A and return", inline=True)
comment(0x9FCF, "A=0: clear result", inline=True)
comment(0x9FD1, "Shift right (always positive)", inline=True)
comment(0x9FD2, "Positive: jump to finalise", inline=True)
comment(0x9FD4, "Mask to 6-bit access value", inline=True)
comment(0x9FD6, "Non-zero: clear A and finalise", inline=True)
comment(0x9FD8, "Transfer X to A (options pointer)", inline=True)
comment(0x9FD9, "Allocate FCB slot or raise error", inline=True)
comment(0x9FDC, "Toggle bit 7", inline=True)
comment(0x9FDE, "Shift left: build open mode", inline=True)
comment(0x9FDF, "Store open mode in l0f05", inline=True)
comment(0x9FE2, "Rotate to complete mode byte", inline=True)
comment(0x9FE3, "Store in l0f06", inline=True)
comment(0x9FE6, "Parse command argument (Y=0)", inline=True)
comment(0x9FE9, "X=2: buffer offset", inline=True)
comment(0x9FEB, "Copy argument to TX buffer", inline=True)
comment(0x9FEE, "Y=6: open file command", inline=True)
comment(0x9FF0, "Set V flag (skip directory check)", inline=True)
comment(0x9FF3, "Set carry", inline=True)
comment(0x9FF4, "Rotate carry into escapable flag bit 7", inline=True)
comment(0x9FF6, "Send open request with V set", inline=True)
comment(0x9FF9, "Carry set (error): jump to finalise", inline=True)
comment(0x9FFB, "A=&FF: mark as newly opened", inline=True)
comment(0x9FFD, "Store &FF as receive attribute", inline=True)
comment(0xA000, "Load handle from l0f05", inline=True)
comment(0xA003, "Push handle", inline=True)
comment(0xA004, "A=4: file info sub-command", inline=True)
comment(0xA006, "Store sub-command", inline=True)
comment(0xA009, "X=1: shift filename", inline=True)
comment(0xA00B, "Load filename byte from l0f06+X", inline=True)
comment(0xA00E, "Shift down to l0f05+X", inline=True)
comment(0xA011, "Advance source index", inline=True)
comment(0xA012, "Is it CR (end of filename)?", inline=True)
comment(0xA014, "No: continue shifting", inline=True)
comment(0xA016, "Y=&12: file info request", inline=True)
comment(0xA018, "Send file info request", inline=True)
comment(0xA01B, "Load last byte flag", inline=True)
comment(0xA01D, "Clear bit 6 (read/write bits)", inline=True)
comment(0xA01F, "OR with reply access byte", inline=True)
comment(0xA022, "Set bit 0 (file is open)", inline=True)
comment(0xA024, "Transfer to Y (access flags)", inline=True)
comment(0xA025, "Check bit 1 (write access)", inline=True)
comment(0xA027, "No write access: check read-only", inline=True)
comment(0xA029, "Pull handle from stack", inline=True)
comment(0xA02A, "Allocate FCB slot for channel", inline=True)
comment(0xA02D, "Non-zero: FCB allocated, store flags", inline=True)
comment(0xA02F, "Verify workspace checksum", inline=True)
comment(0xA032, "Set up transfer parameters", inline=True)
comment(0xA035, "Transfer A to X", inline=True)
comment(0xA036, "Set owner-only access mask", inline=True)
comment(0xA039, "Transfer X back to A", inline=True)
comment(0xA03A, "Zero: close file, process FCBs", inline=True)
comment(0xA03C, "Save text pointer for OS", inline=True)
comment(0xA03F, "Load current directory handle", inline=True)
comment(0xA042, "Zero: allocate new FCB", inline=True)
comment(0xA044, "Transfer Y to A", inline=True)
comment(0xA045, "X=0: clear directory handle", inline=True)
comment(0xA047, "Store zero (clear handle)", inline=True)
comment(0xA04A, "ALWAYS branch to finalise", inline=True)
comment(0xA04C, "Load access/open mode byte", inline=True)
comment(0xA04F, "Rotate right: check bit 0", inline=True)
comment(0xA050, "Carry set (bit 0): check read permission", inline=True)
comment(0xA052, "Rotate right: check bit 1", inline=True)
comment(0xA053, "Carry clear (no write): skip", inline=True)
comment(0xA055, "Test bit 7 of l0f07 (lock flag)", inline=True)
comment(0xA058, "Not locked: skip", inline=True)
comment(0xA05A, "Transfer Y to A (flags)", inline=True)
comment(0xA05B, "Set bit 5 (locked file flag)", inline=True)
comment(0xA05D, "Transfer back to Y", inline=True)
comment(0xA05E, "Pull handle from stack", inline=True)
comment(0xA05F, "Allocate FCB slot for channel", inline=True)
comment(0xA062, "Transfer to X", inline=True)
comment(0xA063, "Transfer Y to A (flags)", inline=True)
comment(0xA064, "Store flags in FCB table l1040", inline=True)
comment(0xA067, "Transfer X back to A (handle)", inline=True)
comment(0xA068, "Jump to finalise and return", inline=True)

# c9d7e: close file and handle spool/exec (&9D7E-&9DBB)
comment(0xA06B, "Process all matching FCBs", inline=True)
comment(0xA06E, "Transfer Y to A", inline=True)
comment(0xA06F, "Non-zero channel: close specific", inline=True)
comment(0xA071, "Load FS options pointer low", inline=True)
comment(0xA073, "Push (save for restore)", inline=True)
comment(0xA074, "A=&77: OSBYTE close spool/exec files", inline=True)
comment(0xA076, "Close any *SPOOL and *EXEC files", inline=True)
comment(0xA079, "Pull saved options pointer", inline=True)
comment(0xA07A, "Restore FS options pointer", inline=True)
comment(0xA07C, "A=0: clear flags", inline=True)
comment(0xA07E, "Clear last byte flag", inline=True)
comment(0xA080, "Clear block offset", inline=True)
comment(0xA082, "ALWAYS branch to send close request", inline=True)
comment(0xA084, "Validate channel character", inline=True)
comment(0xA087, "Load FCB flag byte from l1030", inline=True)
comment(0xA08A, "Store as l0f05 (file handle)", inline=True)
comment(0xA08D, "X=1: argument size", inline=True)
comment(0xA08F, "Y=7: close file command", inline=True)
comment(0xA091, "Send close file request", inline=True)
comment(0xA094, "Load block offset", inline=True)
comment(0xA096, "Non-zero: clear single FCB", inline=True)
comment(0xA098, "Clear V flag", inline=True)
comment(0xA099, "Scan and clear all FCB flags", inline=True)
comment(0xA09C, "Return with last flag", inline=True)
comment(0xA09F, "A=0: clear FCB entry", inline=True)
comment(0xA0A1, "Clear l1010 (FCB high byte)", inline=True)
comment(0xA0A4, "Clear l1040 (FCB flags)", inline=True)
comment(0xA0A7, "ALWAYS branch to return", inline=True)

# OSARGS dispatch: read/write file arguments (&9DBC-&9E02)
comment(0xA0A9, "Z set: handle OSARGS 0", inline=True)
comment(0xA0AB, "Compare X with 4 (number of args)", inline=True)
comment(0xA0AD, "Not 4: check for error", inline=True)
comment(0xA0AF, "Compare Y with 4", inline=True)
comment(0xA0B1, "Below 4: handle special OSARGS", inline=True)
comment(0xA0B3, "Decrement X", inline=True)
comment(0xA0B4, "X was 1: store display flag", inline=True)
comment(0xA0B6, "Store Y in display control flag l0e06", inline=True)
comment(0xA0B9, "Carry clear: return with flag", inline=True)
comment(0xA0BB, "A=7: error code", inline=True)
comment(0xA0BD, "Jump to classify reply error", inline=True)
comment(0xA0C0, "Store Y in l0f05", inline=True)
comment(0xA0C3, "Y=&16: OSARGS save command", inline=True)
comment(0xA0C5, "Send OSARGS request", inline=True)
comment(0xA0C8, "Reload block offset", inline=True)
comment(0xA0CA, "Store in l0e05", inline=True)
comment(0xA0CD, "Positive: return with flag", inline=True)
comment(0xA10B, "Verify workspace checksum", inline=True)
comment(0xA10E, "Push result on stack", inline=True)
comment(0xA10F, "Load block offset", inline=True)
comment(0xA111, "Push block offset", inline=True)
comment(0xA112, "Store X in l10c9", inline=True)
comment(0xA115, "Find matching FCB entry", inline=True)
comment(0xA118, "Zero: no match found", inline=True)
comment(0xA11A, "Load FCB low byte from l1000", inline=True)
comment(0xA11D, "Compare with stored offset l1098", inline=True)
comment(0xA120, "Below stored: no match", inline=True)
comment(0xA122, "X=&FF: mark as found (all bits set)", inline=True)
comment(0xA124, "ALWAYS branch (negative)", inline=True)
comment(0xA126, "X=0: mark as not found", inline=True)
comment(0xA128, "Restore block offset from stack", inline=True)
comment(0xA129, "Transfer to Y", inline=True)
comment(0xA12A, "Restore result from stack", inline=True)
comment(0xA12B, "Return", inline=True)

# update_addr_from_offset9/1 + adjust_fsopts_4bytes (&9E03-&9E22)
comment(0xA12C, "Y=9: FS options offset for high address", inline=True)
comment(0xA12E, "Add workspace values to FS options", inline=True)
comment(0xA131, "Y=1: FS options offset for low address", inline=True)
comment(0xA133, "Clear carry for addition", inline=True)
comment(0xA134, "X=&FC: loop counter (-4 to -1)", inline=True)
comment(0xA136, "Load FS options byte at offset Y", inline=True)
comment(0xA138, "Test fs_load_addr_2 bit 7 (add/subtract)", inline=True)
comment(0xA13A, "Bit 7 set: subtract instead", inline=True)
comment(0xA13C, "Add workspace byte to FS options", inline=True)
comment(0xA13F, "Jump to store result", inline=True)
comment(0xA142, "Subtract workspace byte from FS options", inline=True)
comment(0xA145, "Store result back to FS options", inline=True)
comment(0xA147, "Advance to next byte", inline=True)
comment(0xA148, "Advance counter", inline=True)
comment(0xA149, "Loop until 4 bytes processed", inline=True)
comment(0xA14B, "Return", inline=True)

# OSBGET/OSBPUT dispatch (&9E23-&9E41)
comment(0xA14C, "Verify workspace checksum", inline=True)
comment(0xA14F, "Set up transfer parameters", inline=True)
comment(0xA152, "Push transfer type on stack", inline=True)
comment(0xA153, "Set owner-only access mask", inline=True)
comment(0xA156, "Pull transfer type", inline=True)
comment(0xA157, "Transfer to X", inline=True)
comment(0xA158, "Zero: no valid operation, return", inline=True)
comment(0xA15A, "Decrement (convert 1-based to 0-based)", inline=True)
comment(0xA15B, "Compare with 8 (max operation)", inline=True)
comment(0xA15D, "Below 8: valid operation", inline=True)
comment(0xA15F, "Out of range: return with flag", inline=True)
comment(0xA162, "Transfer operation code to A", inline=True)
comment(0xA163, "Y=0: buffer offset", inline=True)
comment(0xA165, "Push operation code", inline=True)
comment(0xA166, "Compare with 4 (write operations)", inline=True)
comment(0xA168, "Below 4: read operation", inline=True)
comment(0xA16A, "4 or above: write data block", inline=True)

# c9e44: OSBGET read byte from file (&9E44-&9EBD)
comment(0xA16D, "Load channel handle from FS options", inline=True)
comment(0xA16F, "Push handle", inline=True)
comment(0xA170, "Check file is not a directory", inline=True)
comment(0xA173, "Pull handle", inline=True)
comment(0xA174, "Transfer to Y", inline=True)
comment(0xA175, "Process all matching FCBs", inline=True)
comment(0xA178, "Load FCB flag byte from l1030", inline=True)
comment(0xA17B, "Store file handle in l0f05", inline=True)
comment(0xA17E, "A=0: clear direction flag", inline=True)
comment(0xA180, "Store in l0f06", inline=True)
comment(0xA183, "Load FCB low byte (position)", inline=True)
comment(0xA186, "Store in l0f07", inline=True)
comment(0xA189, "Load FCB high byte", inline=True)
comment(0xA18C, "Store in l0f08", inline=True)
comment(0xA18F, "Load FCB extent byte", inline=True)
comment(0xA192, "Store in l0f09", inline=True)
comment(0xA195, "Y=&0D: TX buffer size", inline=True)
comment(0xA197, "X=5: argument count", inline=True)
comment(0xA199, "Send TX control block to server", inline=True)
comment(0xA19C, "Pull operation code", inline=True)
comment(0xA19D, "Set up transfer workspace", inline=True)
comment(0xA1A0, "Save flags (carry from setup)", inline=True)
comment(0xA1A1, "Y=0: index for channel handle", inline=True)
comment(0xA1A3, "Load channel handle from FS options", inline=True)
comment(0xA1A5, "Carry set (write): set active", inline=True)
comment(0xA1A7, "Read: clear connection active", inline=True)
comment(0xA1AA, "Branch to continue (always positive)", inline=True)
comment(0xA1AC, "Write: set connection active", inline=True)
comment(0xA1AF, "Clear l0f06 (Y=0)", inline=True)
comment(0xA1B2, "Look up channel slot data", inline=True)
comment(0xA1B5, "Store flag byte in l0f05", inline=True)
comment(0xA1B8, "Y=&0C: TX buffer size (short)", inline=True)
comment(0xA1BA, "X=2: argument count", inline=True)
comment(0xA1BC, "Send TX control block", inline=True)
comment(0xA1BF, "Look up channel entry at Y=0", inline=True)
comment(0xA1C2, "Y=9: FS options offset for position", inline=True)
comment(0xA1C4, "Load new position low from l0f05", inline=True)
comment(0xA1C7, "Update FCB low byte in l1000", inline=True)
comment(0xA1CA, "Store in FS options at Y=9", inline=True)
comment(0xA1CC, "Y=&0A", inline=True)
comment(0xA1CD, "Load new position high from l0f06", inline=True)
comment(0xA1D0, "Update FCB high byte in l1010", inline=True)
comment(0xA1D3, "Store in FS options at Y=&0A", inline=True)
comment(0xA1D5, "Y=&0B", inline=True)
comment(0xA1D6, "Load new extent from l0f07", inline=True)
comment(0xA1D9, "Update FCB extent in l1020", inline=True)
comment(0xA1DC, "Store in FS options at Y=&0B", inline=True)
comment(0xA1DE, "A=0: clear high byte of extent", inline=True)
comment(0xA1E0, "Y=&0C", inline=True)
comment(0xA1E1, "Store zero in FS options at Y=&0C", inline=True)
comment(0xA1E3, "Restore flags", inline=True)
comment(0xA1E4, "Carry clear: skip last-byte check", inline=True)
comment(0xA1EA, "A=0: success", inline=True)
comment(0xA1E6, "Load last-byte-of-transfer flag", inline=True)
comment(0xA1EC, "Jump to finalise and return", inline=True)
comment(0xA1E8, "Is transfer still pending (flag=3)?", inline=True)

# lookup_cat_entry_0 + lookup_cat_slot_data (&9EC0-&9ECA)
comment(0xA1EF, "Y=0: offset for channel handle", inline=True)
comment(0xA1F1, "Load channel handle from FS options", inline=True)
comment(0xA1F3, "Look up channel by character", inline=True)
comment(0xA1F6, "Load FCB flag byte from l1030", inline=True)
comment(0xA1F9, "Return with flag in A", inline=True)

# setup_transfer_workspace: prepare for data transfer (&9ECB-&9F54)
comment(0xA1FA, "Push operation code on stack", inline=True)
comment(0xA1FB, "Look up channel entry at Y=0", inline=True)
comment(0xA1FE, "Store flag byte in l0f05", inline=True)
comment(0xA201, "Y=&0B: source offset in FS options", inline=True)
comment(0xA203, "X=6: copy 6 bytes", inline=True)
comment(0xA205, "Load FS options byte", inline=True)
comment(0xA207, "Store in l0f06 buffer", inline=True)
comment(0xA20A, "Decrement source index", inline=True)
comment(0xA20B, "Skip offset 8?", inline=True)
comment(0xA20D, "No: continue copy", inline=True)
comment(0xA20F, "Skip offset 8 (hole in structure)", inline=True)
comment(0xA210, "Decrement destination counter", inline=True)
comment(0xA211, "Loop until all 6 bytes copied", inline=True)
comment(0xA213, "Pull operation code", inline=True)
comment(0xA214, "Shift right: check bit 0 (direction)", inline=True)
comment(0xA215, "Push updated code", inline=True)
comment(0xA216, "Carry clear: OSBGET (read)", inline=True)
comment(0xA218, "Carry set: OSBPUT (write), X=1", inline=True)
comment(0xA219, "Store direction flag in l0f06", inline=True)
comment(0xA21C, "Y=&0B: TX buffer size", inline=True)
comment(0xA21E, "X=&91: port for OSBGET", inline=True)
comment(0xA220, "Pull operation code", inline=True)
comment(0xA221, "Push back (keep on stack)", inline=True)
comment(0xA222, "Zero (OSBGET): keep port &91", inline=True)
comment(0xA224, "X=&92: port for OSBPUT", inline=True)
comment(0xA226, "Y=&0A: adjusted buffer size", inline=True)
comment(0xA227, "Store port in l0f02", inline=True)
comment(0xA22A, "Store port in fs_error_ptr", inline=True)
comment(0xA22C, "X=8: argument count", inline=True)
comment(0xA22E, "Load file handle from l0f05", inline=True)
comment(0xA231, "Send request (no write data)", inline=True)
comment(0xA234, "X=0: index", inline=True)
comment(0xA236, "Load channel handle from FS options", inline=True)
comment(0xA238, "Transfer to X as index", inline=True)
comment(0xA239, "Load FCB flags from l1040", inline=True)
comment(0xA23C, "Toggle bit 0 (transfer direction)", inline=True)
comment(0xA23E, "Store updated flags", inline=True)
comment(0xA241, "Clear carry for addition", inline=True)
comment(0xA242, "X=4: process 4 address bytes", inline=True)
comment(0xA244, "Load FS options address byte", inline=True)
comment(0xA246, "Store in zero page address area", inline=True)
comment(0xA249, "Store in TXCB position", inline=True)
comment(0xA24C, "Advance Y by 4", inline=True)
comment(0xA24F, "Add offset from FS options", inline=True)
comment(0xA251, "Store computed end address", inline=True)
comment(0xA254, "Retreat Y by 3 for next pair", inline=True)
comment(0xA257, "Decrement byte counter", inline=True)
comment(0xA258, "Loop for all 4 address bytes", inline=True)
comment(0xA25A, "X=1 (INX from 0)", inline=True)
comment(0xA25B, "Load offset from l0f03", inline=True)
comment(0xA25E, "Copy to l0f06", inline=True)
comment(0xA261, "Decrement counter", inline=True)
comment(0xA262, "Loop until both bytes copied", inline=True)
comment(0xA264, "Pull operation code", inline=True)
comment(0xA265, "Non-zero (OSBPUT): swap addresses", inline=True)
comment(0xA267, "Load port from l0f02", inline=True)
comment(0xA26A, "Check and set up TXCB", inline=True)
comment(0xA26D, "Carry set: skip swap", inline=True)
comment(0xA26F, "Send TXCB and swap start/end addresses", inline=True)
comment(0xA272, "Receive and process reply", inline=True)
comment(0xA275, "Store result in fs_load_addr_2", inline=True)
comment(0xA277, "Update addresses from offset 9", inline=True)
comment(0xA27A, "Decrement fs_load_addr_2", inline=True)
comment(0xA27C, "Set carry for subtraction", inline=True)
comment(0xA27D, "Adjust FS options by 4 bytes", inline=True)
comment(0xA280, "Shift l0f05 left (update status)", inline=True)
comment(0xA283, "Return", inline=True)
comment(0xA289, "Return", inline=True)
comment(0xA284, "Save flags before reply processing", inline=True)

comment(0xA285, "Process server reply", inline=True)
# c9f55: send OSBPUT data to server (&9F55-&9F68)
comment(0xA288, "Restore flags after reply processing", inline=True)
comment(0xA28A, "Y=&15: TX buffer size for OSBPUT data", inline=True)
comment(0xA28C, "Send TX control block", inline=True)
comment(0xA28F, "Load display flag from l0e05", inline=True)
comment(0xA292, "Store in l0f16", inline=True)
comment(0xA295, "Clear fs_load_addr (X=0)", inline=True)
comment(0xA297, "Clear fs_load_addr_hi", inline=True)
comment(0xA299, "A=&12: byte count for data block", inline=True)
comment(0xA29B, "Store in fs_load_addr_2", inline=True)
comment(0xA29D, "ALWAYS branch to write data block", inline=True)

# c9f6a: OSBPUT write byte to file (&9F6A-&9FB6)
comment(0xA29F, "Y=4: offset for station comparison", inline=True)
comment(0xA2A1, "Load stored station from l0d63", inline=True)
comment(0xA2A4, "Zero: skip station check", inline=True)
comment(0xA2A6, "Compare with FS options station", inline=True)
comment(0xA2A8, "Mismatch: skip subtraction", inline=True)
comment(0xA2AA, "Y=3", inline=True)
comment(0xA2AB, "Subtract FS options value", inline=True)
comment(0xA2AD, "Store result in svc_state", inline=True)
comment(0xA2AF, "Load FS options byte at Y", inline=True)
comment(0xA2B1, "Store in workspace at fs_last_byte_flag+Y", inline=True)
comment(0xA2B4, "Decrement index", inline=True)
comment(0xA2B5, "Loop until all bytes copied", inline=True)
comment(0xA2B7, "Pull operation code", inline=True)
comment(0xA2B8, "Mask to 2-bit sub-operation", inline=True)
comment(0xA2BA, "Zero: send OSBPUT data", inline=True)
comment(0xA2BC, "Shift right: check bit 0", inline=True)
comment(0xA2BD, "Zero (bit 0 clear): handle read", inline=True)
comment(0xA2BF, "Carry set: handle catalogue update", inline=True)
comment(0xA2C1, "Transfer to Y (Y=0)", inline=True)
comment(0xA2C2, "Load data byte from l0e03", inline=True)
comment(0xA2C5, "Store in l0f03", inline=True)
comment(0xA2C8, "Load high data byte from l0e04", inline=True)
comment(0xA2CB, "Store in l0f04", inline=True)
comment(0xA2CE, "Load port from l0e02", inline=True)
comment(0xA2D1, "Store in l0f02", inline=True)
comment(0xA2D4, "X=&12: buffer size marker", inline=True)
comment(0xA2D6, "Store in l0f01", inline=True)
comment(0xA2D9, "A=&0D: count value", inline=True)
comment(0xA2DB, "Store in l0f06", inline=True)
comment(0xA2DE, "Store in fs_load_addr_2", inline=True)
comment(0xA2E0, "Shift right (A=6)", inline=True)
comment(0xA2E1, "Store in l0f05", inline=True)
comment(0xA2E4, "Clear carry for addition", inline=True)
comment(0xA2E5, "Prepare and send TX control block", inline=True)
comment(0xA2E8, "Store X in fs_load_addr_hi (X=0)", inline=True)
comment(0xA2EA, "X=1 (INX)", inline=True)
comment(0xA2EB, "Store X in fs_load_addr", inline=True)

# write_data_block: write data to host or tube (&9FB8-&9FF4)
comment(0xA2ED, "Load svc_state (tube flag)", inline=True)
comment(0xA2EF, "Non-zero: write via tube", inline=True)
comment(0xA2F1, "Load source index from fs_load_addr", inline=True)
comment(0xA2F3, "Load destination index from fs_load_addr_hi", inline=True)
comment(0xA2F5, "Load data byte from l0f05 buffer", inline=True)
comment(0xA2F8, "Store to destination via fs_crc pointer", inline=True)
comment(0xA2FA, "Advance source index", inline=True)
comment(0xA2FB, "Advance destination index", inline=True)
comment(0xA2FC, "Decrement byte counter", inline=True)
comment(0xA2FE, "Loop until all bytes transferred", inline=True)
comment(0xA300, "ALWAYS branch to update catalogue", inline=True)
comment(0xA302, "Claim tube with call &C3", inline=True)
comment(0xA305, "A=1: tube transfer type (write)", inline=True)
comment(0xA307, "Load destination low from fs_options", inline=True)
comment(0xA309, "Load destination high from fs_block_offset", inline=True)
comment(0xA30B, "Increment low byte", inline=True)
comment(0xA30C, "No wrap: skip high increment", inline=True)
comment(0xA30E, "Carry: increment high byte", inline=True)
comment(0xA30F, "Set up tube transfer address", inline=True)
comment(0xA312, "Load source index", inline=True)
comment(0xA314, "Load data byte from buffer", inline=True)
comment(0xA317, "Write to tube data register 3", inline=True)
comment(0xA31A, "Advance source index", inline=True)
comment(0xA31B, "Y=6: tube write delay", inline=True)
comment(0xA31D, "Delay loop: decrement Y", inline=True)
comment(0xA31E, "Loop until delay complete", inline=True)
comment(0xA320, "Decrement byte counter", inline=True)
comment(0xA322, "Loop until all bytes written to tube", inline=True)
comment(0xA324, "A=&83: release tube claim", inline=True)
comment(0xA326, "Release tube", inline=True)
comment(0xA329, "Jump to clear A and finalise return", inline=True)

# c9ff7: catalogue update command (&9FF7-&9FFE)
comment(0xA32C, "Y=9: offset for position byte", inline=True)
comment(0xA32E, "Load position from FS options", inline=True)
comment(0xA330, "Store in l0f06", inline=True)
comment(0xA333, "Y=5: offset for extent byte", inline=True)

# c9ff7 continued: catalogue update data transfer (&A000-&A058)
comment(0xA335, "Load extent byte from FS options", inline=True)
comment(0xA337, "Store in l0f07", inline=True)
comment(0xA33A, "X=&0D: byte count", inline=True)
comment(0xA33C, "Store in l0f08", inline=True)
comment(0xA33F, "Y=2: command sub-type", inline=True)
comment(0xA341, "Store in fs_load_addr", inline=True)
comment(0xA343, "Store in l0f05", inline=True)
comment(0xA346, "Y=3: TX buffer command byte", inline=True)
comment(0xA347, "Send TX control block", inline=True)
comment(0xA34A, "Store X (0) in fs_load_addr_hi", inline=True)
comment(0xA34C, "Load data offset from l0f06", inline=True)
comment(0xA34F, "Store as first byte of FS options", inline=True)
comment(0xA351, "Load data count from l0f05", inline=True)
comment(0xA354, "Y=9: position offset in FS options", inline=True)
comment(0xA356, "Add to current position", inline=True)
comment(0xA358, "Store updated position", inline=True)
comment(0xA35A, "Load TXCB end byte", inline=True)
comment(0xA35C, "Subtract 7 (header overhead)", inline=True)
comment(0xA35E, "Store remaining data size", inline=True)
comment(0xA361, "Store in fs_load_addr_2 (byte count)", inline=True)
comment(0xA363, "Zero bytes: skip write", inline=True)
comment(0xA365, "Write data block to host/tube", inline=True)
comment(0xA368, "X=2: clear 3 bytes (indices 0-2)", inline=True)
comment(0xA36A, "Clear l0f07+X", inline=True)
comment(0xA36D, "Decrement index", inline=True)
comment(0xA36E, "Loop until all cleared", inline=True)
comment(0xA370, "Update addresses from offset 1", inline=True)
comment(0xA373, "Set carry for subtraction", inline=True)
comment(0xA374, "Decrement fs_load_addr_2", inline=True)
comment(0xA376, "Load data count from l0f05", inline=True)
comment(0xA379, "Copy to l0f06", inline=True)
comment(0xA37C, "Adjust FS options by 4 bytes (subtract)", inline=True)
comment(0xA37F, "X=3: check 4 bytes", inline=True)
comment(0xA381, "Y=5: starting offset", inline=True)
comment(0xA383, "Set carry for comparison", inline=True)
comment(0xA384, "Load FS options byte", inline=True)
comment(0xA386, "Non-zero: more data remaining", inline=True)
comment(0xA388, "Advance to next byte", inline=True)
comment(0xA389, "Decrement counter", inline=True)
comment(0xA38A, "Loop until all bytes checked", inline=True)
comment(0xA38C, "All zero: clear carry (transfer complete)", inline=True)
comment(0xA38D, "Jump to update catalogue and return", inline=True)

# tube_claim_c3: claim tube with protocol &C3 (&A05B-&A062)
comment(0xA390, "A=&C3: tube claim protocol", inline=True)
comment(0xA392, "Dispatch tube address/data claim", inline=True)
comment(0xA395, "Carry clear: claim failed, retry", inline=True)
comment(0xA397, "Return (tube claimed)", inline=True)

# tube_init_reloc continued: copy relocated blocks (&BE94-&BEC2)
# Copies pages 4/5/6 code and zero-page workspace from ROM to RAM
# UNMAPPED: comment(0xBE94, "Resume normal ROM address space\n"
# UNMAPPED:     "\n"
# UNMAPPED:     "The preceding 512 bytes are the source data for\n"
# UNMAPPED:     "two relocated code blocks (see move() calls):\n"
# UNMAPPED:     "  page 5 source -> &0500-&05FF (Tube host code)\n"
# UNMAPPED:     "  page 6 source -> &0600-&06FF (Econet handlers)\n"
# UNMAPPED:     "py8dis assembles those blocks at their runtime\n"
# UNMAPPED:     "addresses (&0500/&0600) via org directives. This\n"
# UNMAPPED:     "org restores the origin to the actual ROM address\n"
# UNMAPPED:     "for the remaining non-relocated code.")
# UNMAPPED: comment(0xBE94, "Store BRK vector high byte", inline=True)
# UNMAPPED: comment(0xBE97, "A=&8E: Tube control register value", inline=True)
# UNMAPPED: comment(0xBE99, "Write Tube control register", inline=True)
# UNMAPPED: comment(0xBE9C, "Y=0: copy 256 bytes per page", inline=True)
# UNMAPPED: comment(0xBE9E, "Load page 4 source byte", inline=True)
# UNMAPPED: comment(0xBEA1, "Store to page 4 destination", inline=True)
# UNMAPPED: comment(0xBEA4, "Load page 5 source byte", inline=True)
# UNMAPPED: comment(0xBEA7, "Store to page 5 destination", inline=True)
# UNMAPPED: comment(0xBEAA, "Load page 6 source byte", inline=True)
# UNMAPPED: comment(0xBEAD, "Store to page 6 destination", inline=True)
# UNMAPPED: comment(0xBEB0, "Decrement byte counter", inline=True)
# UNMAPPED: comment(0xBEB1, "Non-zero: continue copying", inline=True)
# UNMAPPED: comment(0xBEB3, "Clear tube claim state", inline=True)
# UNMAPPED: comment(0xBEB6, "X=&41: copy 66 bytes of ZP workspace", inline=True)
# UNMAPPED: comment(0xBEB8, "Load ZP source byte from ROM", inline=True)
# UNMAPPED: comment(0xBEBB, "Store to NMI workspace at &16+X", inline=True)
# UNMAPPED: comment(0xBEBD, "Decrement byte counter", inline=True)
# UNMAPPED: comment(0xBEBE, "More bytes: continue copying", inline=True)
# UNMAPPED: comment(0xBEC0, "A=0: return success", inline=True)
# UNMAPPED: comment(0xBEC2, "Return to caller", inline=True)

# ============================================================
# Generate disassembly
# ============================================================

import json
import sys

output = go(print_output=False)

_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "anfs-4.21_variant_1.asm"
output_filepath.write_text(output)
print(f"Wrote {output_filepath}", file=sys.stderr)

structured = get_structured()
json_filepath = _output_dirpath / "anfs-4.21_variant_1.json"
json_filepath.write_text(json.dumps(structured))
print(f"Wrote {json_filepath}", file=sys.stderr)
