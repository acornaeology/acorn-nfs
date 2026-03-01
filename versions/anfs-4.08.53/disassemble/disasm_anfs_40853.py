import os
from pathlib import Path

from py8dis.commands import *
import py8dis.acorn as acorn
import py8dis.trace as trace

init(assembler_name="beebasm", lower_case=True)

# ============================================================
# ANFS 4.08.53 — Acorn Advanced Network Filing System
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
    str(_version_dirpath / "rom" / "anfs-4.08.53.rom"),
)
_output_dirpath = Path(os.environ.get(
    "ACORN_NFS_OUTPUT",
    str(_version_dirpath / "output"),
))

load(0x8000, _rom_filepath, "6502")
trace.cpu.default_subroutine_hook = None

# ============================================================
# Relocated code blocks
# ============================================================
# The ANFS ROM copies code from ROM into RAM at initialisation.
# These blocks execute at different addresses than their storage locations.
# move(dest, src, length) tells py8dis the runtime address for each block.
#
# The page copy loop (&BE9A) copies all 256 bytes of pages 4, 5, 6
# using DEY/BNE wrapping through &FF..&01.
#
# The workspace init (&BEB4) copies X=&41 downto 0 (BPL) = 66 bytes.

# BRK handler + NMI workspace init code (&BEBF -> &0016-&0057)
move(0x0016, 0xBEBF, 0x42)

# NMI handler / page 4-6 relocated code
move(0x0400, 0xBF00, 0x100)    # Page 4: NMI dispatch + TX/RX
move(0x0500, 0xBC90, 0x100)    # Page 5: Tube host code
move(0x0600, 0xBD90, 0x100)    # Page 6: Econet protocol handlers

# ROM-address labels for move() block origins (referenced by copy routines)
label(0xBEBF, "reloc_zp_src")        # ROM source of zero-page relocated code
label(0xBF00, "reloc_p4_src")        # ROM source of page 4 code
label(0xBC90, "reloc_p5_src")        # ROM source of page 5 code
label(0xBD90, "reloc_p6_src")        # ROM source of page 6 code

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
hook_subroutine(0x9131, "print_inline", stringhi_hook)

# error_inline (&96BE) builds a BRK error block from a null-terminated inline
# string following the JSR. The error number is passed in A. Never returns.
hook_subroutine(0x96BE, "error_inline", stringz_hook)

# error_inline_log (&96BB) is identical to error_inline but first logs the
# error code via sub_c95fb. Never returns.
hook_subroutine(0x96BB, "error_inline_log", stringz_hook)

# error_bad_inline (&96A2) prepends "Bad " to the inline string before
# building the BRK error block. The error number is passed in A. Never returns.
hook_subroutine(0x96A2, "error_bad_inline", stringz_hook)


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
constant(0x20, "handle_base")         # HAND: base value for file handles

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

# ============================================================
# Zero page — Filing system workspace (&B0-&CF)
# ============================================================

label(0x00B0, "fs_load_addr")        # WORK: load/start address (4 bytes)
label(0x00B1, "fs_load_addr_hi")
label(0x00B2, "fs_load_addr_2")
label(0x00B3, "fs_load_addr_3")
label(0x00B4, "fs_work_4")
label(0x00B5, "fs_work_5")
label(0x00B7, "fs_work_7")
label(0x00B8, "fs_error_ptr")
label(0x00B9, "fs_crflag")
label(0x00BA, "fs_spool_handle")
label(0x00BB, "fs_options")
label(0x00BC, "fs_block_offset")
label(0x00BD, "fs_last_byte_flag")
label(0x00BE, "fs_crc_lo")
label(0x00BF, "fs_crc_hi")
label(0x00C0, "txcb_ctrl")
label(0x00C1, "txcb_port")
label(0x00C2, "txcb_dest")
label(0x00C4, "txcb_start")
label(0x00C7, "txcb_pos")
label(0x00C8, "txcb_end")
label(0x00CD, "nfs_temp")
label(0x00CE, "rom_svc_num")
label(0x00CF, "fs_spool0")

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
label(0x0016, "nmi_workspace_start")

# Zero page — MOS locations (&EF-&FF)
label(0x00EF, "osbyte_a_copy")
label(0x00F0, "osword_pb_ptr")
label(0x00F1, "osword_pb_ptr_hi")
label(0x00F3, "os_text_ptr_hi")
label(0x00F7, "osrdsc_ptr_hi")
label(0x00FD, "brk_ptr")
label(0x00FF, "escape_flag")

# Page 1 — Stack page
label(0x0100, "error_block")
label(0x0101, "error_text")

# Page 3 — VDU variables
label(0x0350, "vdu_screen_mode")

# Page 7 — String buffer
label(0x0700, "string_buf")

# Page &0C — NMI shim write base
label(0x0CFF, "nmi_code_base")

# ============================================================
# Page &0D — NMI handler workspace (&0D00-&0DFF)
# ============================================================

label(0x0D0C, "nmi_jmp_lo")
label(0x0D0D, "nmi_jmp_hi")
label(0x0D0E, "set_nmi_vector")
label(0x0D11, "install_nmi_handler")
label(0x0D14, "nmi_rti")

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

# Received scout
label(0x0D3D, "rx_src_stn")
label(0x0D3E, "rx_src_net")
label(0x0D3F, "rx_ctrl")
label(0x0D40, "rx_port")
label(0x0D41, "rx_remote_addr")

# TX state
label(0x0D4A, "tx_flags")
label(0x0D4B, "nmi_next_lo")
label(0x0D4C, "nmi_next_hi")
label(0x0D4F, "tx_index")
label(0x0D50, "tx_length")

# ANFS-specific workspace (identified from references in ROM)
label(0x0D60, "ws_0d60")
label(0x0D62, "ws_0d62")
label(0x0D64, "ws_0d64")
label(0x0D65, "tx_op_type")
label(0x0D68, "ws_0d68")
label(0x0D69, "ws_0d69")
label(0x0D6A, "ws_0d6a")

# ============================================================
# Entry points for relocated code
# ============================================================

# Zero-page relocated code entry points
entry(0x0016)

# Page 4 entry points
entry(0x0400)
entry(0x0403)
entry(0x0406)
entry(0x0421)

# Page 5 entry points
entry(0x0500)
entry(0x0520)   # tube_osbput
entry(0x0527)   # tube_poll_r1_wrch
entry(0x052D)   # tube_osbget
entry(0x0537)   # tube_osrdch
entry(0x053A)   # tube_rdch_reply
entry(0x055E)   # tube_osargs
entry(0x0562)   # tube_read_params
entry(0x0596)   # tube_oscli
entry(0x05A9)   # tube_osfile
entry(0x05D1)   # tube_osgbpb
entry(0x05F2)   # tube_osbyte_2param

# Page 6 entry points
entry(0x0600)


# ============================================================
# Code label renames (Phase 3)
# ============================================================

# Data and shared-tail label renames (Phase 3b)
label(0x0026, "tube_send_error_num")
label(0x0400, "tube_page4_vectors")
label(0x0500, "tube_r2_dispatch_table")
label(0x0600, "tube_osbyte_reply_block")
label(0x06DF, "loop_poll_r1_vdu")
label(0x06EF, "setup_tube_vectors")
label(0x8001, "rom_header_byte1")
label(0x8002, "rom_header_byte2")
label(0x802D, "save_registers")
label(0x8052, "set_jsr_protection")
label(0x8085, "econet_restore")
label(0x83DA, "loop_count_rxcb_slot")
expr_label(0x83FD, "imm_op_dispatch_lo-&81")  # = &847E - &81
label(0x84B1, "set_rx_buf_len_hi")
label(0x85F1, "reload_inactive_mask")
label(0x85F6, "intoff_disable_nmi_op")
label(0x87BD, "tx_check_tdra_ready")
label(0x87E8, "check_tdra_status")
label(0x88F7, "check_tx_in_progress")
label(0x8A29, "clear_workspace_byte")
label(0x8A2E, "restore_rom_slot")
label(0x8A32, "dispatch_service")
label(0x8A49, "set_adlc_present")
label(0x8A50, "check_adlc_flag")
label(0x8A58, "handle_vectors_claimed")
label(0x8A65, "init_rom_scan")
label(0x8A68, "loop_scan_net_roms")
label(0x8A90, "next_rom_slot")
label(0x8A9F, "dispatch_svc_with_state")
label(0x8AB2, "dispatch_svc_index")
label(0x8AC3, "restore_svc_state")
label(0x8AC9, "restore_romsel_rts")
label(0x8AE6, "loop_scan_key_range")
label(0x8AF3, "clear_svc_and_ws")
label(0x8B1A, "loop_sum_rom_bytes")
label(0x8B28, "done_rom_checksum")
label(0x8B2D, "loop_copy_fs_ctx")
label(0x8B40, "loop_set_vectors")
label(0x8B6F, "loop_copy_ws_page")
label(0x8B9D, "print_table_newline")
label(0x8BA3, "loop_next_entry")
label(0x8BAB, "print_indent")
label(0x8BB5, "loop_print_name")
label(0x8BBF, "loop_pad_spaces")
label(0x8BD5, "loop_print_syntax")
label(0x8BE5, "print_syntax_char")
label(0x8BEB, "print_shared_prefix")
label(0x8BF5, "loop_next_shared")
label(0x8BFB, "loop_print_shared")
label(0x8C07, "print_last_char")
label(0x8C14, "skip_syntax_bytes")
label(0x8C19, "done_shared_cmds")
label(0x8C1B, "done_entry_newline")
label(0x8C24, "done_print_table")
label(0x8C3A, "loop_indent_spaces")
label(0x8C65, "svc_return_unclaimed")
label(0x8C68, "check_help_topic")
label(0x8C72, "match_help_topic")
label(0x8C75, "loop_dispatch_help")
label(0x8C8D, "skip_if_no_match")
label(0x8C97, "version_string_cr")
label(0x8CCF, "write_key_state")
label(0x8CD5, "select_net_fs")
label(0x8CFF, "issue_svc_osbyte")
label(0x8D10, "loop_match_credits")
label(0x8D1B, "done_credits_check")
label(0x8D21, "loop_emit_credits")
label(0x8D2D, "credits_keyword_start")
label(0x8D4B, "credits_string_mid")
label(0x8D9C, "skip_no_fs_addr")
label(0x8DA3, "loop_copy_logon_cmd")
label(0x8DB4, "scan_pass_prompt")
label(0x8DB6, "loop_scan_colon")
label(0x8DC7, "read_pw_char")
label(0x8DD9, "loop_erase_pw")
label(0x8DE0, "check_pw_special")
label(0x8DEF, "send_pass_to_fs")
label(0x8E3E, "svc_dispatch_lo_offset")
label(0x8E71, "jmp_osbyte")
label(0x8E9D, "done_cap_ws_count")
label(0x8ED5, "loop_zero_workspace")
label(0x8EFF, "loop_copy_init_data")
label(0x8F11, "loop_alloc_handles")
label(0x8F23, "read_station_id")
label(0x8F29, "error_bad_station")
label(0x8F2B, "ws_init_data")
label(0x8F2F, "store_station_id")
label(0x8F75, "loop_restore_ctx")
label(0x8F97, "loop_checksum_byte")
label(0x8FA1, "loop_copy_to_ws")
label(0x8FA4, "store_ws_byte")
label(0x8FBB, "loop_sum_ws")
label(0x900A, "done_print_newline")
label(0x900E, "cmd_syntax_strings")
label(0x910E, "cmd_syntax_table")
label(0x912C, "add_ascii_base")
label(0x9139, "loop_next_char")
label(0x913F, "load_char")
label(0x9157, "resume_caller")
label(0x9169, "next_hex_char")
label(0x9174, "check_digit_range")
label(0x9184, "skip_if_not_hex")
label(0x9186, "extract_digit_value")
label(0x919A, "next_dec_char")
label(0x91C6, "done_parse_num")
label(0x91CF, "validate_station")
label(0x91E5, "return_parsed")
label(0x91E7, "handle_dot_sep")
label(0x91FD, "error_overflow")
label(0x9215, "error_bad_number")
label(0x9221, "error_bad_param")
label(0x9230, "error_bad_net_num")
label(0x9253, "not_a_digit")
label(0x9263, "begin_prot_encode")
label(0x9267, "loop_encode_prot")
label(0x926F, "skip_clear_prot")
label(0x9272, "prot_bit_encode_table")
label(0x9292, "loop_cmp_handle")
label(0x929C, "fscv_7_read_handles")
label(0x92CD, "done_conn_flag")
label(0x9315, "loop_scan_flag")
label(0x931E, "loop_copy_name")
label(0x932A, "append_space")
label(0x933B, "loop_skip_spaces")
label(0x9344, "check_open_quote")
label(0x934F, "loop_copy_arg_char")
label(0x935D, "store_arg_char")
label(0x9387, "loop_copy_rename")
label(0x938E, "error_bad_rename")
label(0x939A, "store_rename_char")
label(0x93A8, "skip_rename_spaces")
label(0x93DA, "setup_fs_root")
label(0x93DC, "loop_copy_fs_num")
label(0x93F1, "check_fs_dot")
label(0x93F8, "parse_fs_dot_dir")
label(0x9428, "dir_found_send")
label(0x944E, "dir_pass_simple")
label(0x9462, "loop_init_txcb")
label(0x9472, "skip_txcb_dest")
label(0x9477, "txcb_init_template")
label(0x947D, "bit_test_ff_pad")
label(0x94A0, "txcb_copy_carry_clr")
label(0x94A1, "txcb_copy_carry_set")
label(0x94A7, "loop_copy_vset_stn")
label(0x94BF, "use_lib_station")
label(0x94C5, "done_vset_station")
label(0x94E4, "loop_next_reply")
label(0x94EE, "process_reply_code")
label(0x94F1, "handle_disconnect")
label(0x94FA, "store_reply_status")
label(0x9506, "check_data_loss")
label(0x950B, "loop_scan_channels")
label(0x952F, "reload_reply_status")
label(0x953B, "build_error_block")
label(0x9545, "setup_error_copy")
label(0x9547, "loop_copy_error")
label(0x956A, "lang_1_remote_boot")
label(0x9570, "done_commit_state")
label(0x9573, "init_remote_session")
label(0x9598, "lang_3_execute_at_0100")
label(0x95A8, "lang_4_remote_validated")
label(0x95B8, "lang_0_insert_remote_key")
label(0x95D8, "init_poll_counters")
label(0x95DE, "loop_poll_tx")
label(0x95F1, "done_poll_tx")
label(0x9604, "build_no_reply_error")
label(0x9614, "loop_copy_no_reply_msg")
label(0x9620, "done_no_reply_msg")
label(0x9633, "skip_if_not_a")
label(0x963B, "mask_error_class")
label(0x9652, "loop_copy_station_msg")
label(0x965E, "done_station_msg")
label(0x9670, "suffix_not_listening")
label(0x9672, "load_suffix_offset")
label(0x9676, "loop_copy_suffix")
label(0x9682, "done_suffix")
label(0x9684, "build_simple_error")
label(0x9693, "loop_copy_error_msg")
label(0x9699, "check_msg_terminator")
label(0x96AE, "loop_copy_bad_prefix")
label(0x96C7, "write_error_num_and_str")
label(0x96D1, "loop_copy_inline_str")
label(0x96E5, "trigger_brk")
label(0x96E8, "handle_net_error")
label(0x970A, "close_exec_file")
label(0x970D, "close_spool_exec")
label(0x9717, "done_close_files")
label(0x971F, "loop_copy_channel_msg")
label(0x972B, "append_error_number")
label(0x9752, "append_station_num")
label(0x977F, "loop_count_digit")
label(0x978F, "store_digit")
label(0x9798, "net_error_lookup_data")
label(0x9831, "set_timeout")
label(0x983A, "start_tx_attempt")
label(0x9850, "loop_retry_tx")
label(0x9856, "loop_tx_delay")
label(0x985E, "try_alternate_phase")
label(0x9869, "tx_send_error")
label(0x986D, "tx_success")
label(0x9873, "pass_txbuf_init_table")
label(0x9889, "loop_copy_template")
label(0x9896, "skip_template_byte")
label(0x98A3, "start_pass_tx")
label(0x98AF, "done_pass_retries")
label(0x98C4, "loop_poll_pass_tx")
label(0x98C9, "restore_retry_state")
label(0x98D6, "loop_pass_tx_delay")
label(0x98DE, "pass_tx_success")
label(0x98E3, "loop_restore_txbuf")
label(0x98ED, "skip_restore_byte")
label(0x98F5, "loop_copy_text_ptr")
label(0x9907, "loop_gsread_char")
label(0x9912, "terminate_buf")
label(0x9938, "copy_arg_and_enum")
label(0x9955, "copy_ws_then_fsopts")
label(0x995B, "setup_txcb_addrs")
label(0x995D, "loop_copy_addrs")
label(0x9978, "loop_copy_offsets")
label(0x998D, "loop_swap_and_send")
label(0x998F, "loop_copy_start_end")
label(0x99A3, "loop_verify_addrs")
label(0x99AF, "check_display_type")
label(0x99B4, "setup_dir_display")
label(0x99B9, "loop_compute_diffs")
label(0x99D7, "loop_copy_fs_options")
label(0x99F8, "send_info_request")
label(0x9A05, "setup_txcb_transfer")
label(0x9A0B, "recv_reply")
label(0x9A0E, "store_result")
label(0x9A1B, "loop_copy_file_info")
label(0x9A1E, "store_prot_byte")
label(0x9A2C, "loop_print_filename")
label(0x9A52, "loop_print_hex_byte")
label(0x9A62, "loop_copy_fsopts_byte")
label(0x9A75, "loop_copy_ws_byte")
label(0x9A84, "discard_handle_match")
label(0x9A8E, "init_transfer_addrs")
label(0x9A99, "loop_copy_addr_offset")
label(0x9AAB, "loop_check_vs_limit")
label(0x9AB7, "clamp_end_to_limit")
label(0x9AB9, "loop_copy_limit")
label(0x9AC0, "set_port_and_ctrl")
label(0x9ADD, "dispatch_osword_op")
label(0x9AE9, "dispatch_ops_1_to_6")
label(0x9B01, "loop_copy_fsopts_4")
label(0x9B0E, "setup_save_access")
label(0x9B18, "loop_copy_fsopts_8")
label(0x9B23, "send_save_or_access")
label(0x9B2A, "send_delete_request")
label(0x9B2F, "send_request_vset")
label(0x9B35, "skip_if_error")
label(0x9B3A, "setup_write_access")
label(0x9B44, "read_cat_info")
label(0x9B66, "loop_copy_cat_info")
label(0x9B73, "loop_copy_ext_info")
label(0x9B7F, "return_with_handle")
label(0x9B80, "done_osword_op")
label(0x9B8D, "loop_copy_cmdline_char")
label(0x9B99, "pad_with_spaces")
label(0x9BA4, "loop_copy_buf_char")
label(0x9BA6, "copy_from_buf_entry")
label(0x9BC1, "validate_chan_close")
label(0x9BC6, "error_invalid_chan")
label(0x9BC9, "check_chan_range")
label(0x9BD9, "loop_copy_fcb_fields")
label(0x9BE9, "dispatch_osfind_op")
label(0x9BF4, "osfind_with_channel")
label(0x9C27, "loop_copy_zp_to_buf")
label(0x9C3D, "done_return_flag")
label(0x9C40, "osargs_read_op")
label(0x9C4F, "loop_copy_reply_to_zp")
label(0x9C5C, "osargs_ptr_dispatch")
label(0x9C7E, "osargs_write_ptr")
label(0x9C85, "loop_copy_ptr_to_buf")
label(0x9CB6, "close_all_fcbs")
label(0x9CC8, "osfind_close_or_open")
label(0x9CD3, "loop_copy_reply_data")
label(0x9CDF, "done_file_open")
label(0x9CE1, "clear_result")
label(0x9CE3, "shift_and_finalise")
label(0x9CE6, "alloc_fcb_for_open")
label(0x9D1E, "loop_shift_filename")
label(0x9D5F, "check_open_mode")
label(0x9D71, "alloc_fcb_with_flags")
label(0x9D75, "store_fcb_flags")
label(0x9D7B, "done_osfind")
label(0x9D7E, "close_all_channels")
label(0x9D97, "close_specific_chan")
label(0x9D9D, "send_close_request")
label(0x9DAF, "done_close")
label(0x9DB2, "clear_single_fcb")
label(0x9DBC, "fscv_0_opt_entry")
label(0x9DC6, "osargs_dispatch")
label(0x9DC9, "store_display_flag")
label(0x9DCE, "error_osargs")
label(0x9DD3, "send_osargs_request")
label(0x9DE2, "fscv_1_eof")
label(0x9DFD, "mark_not_found")
label(0x9DFF, "restore_and_return")
label(0x9E0D, "loop_adjust_byte")
label(0x9E19, "subtract_ws_byte")
label(0x9E1C, "store_adjusted_byte")
label(0x9E36, "skip_if_out_of_range")
label(0x9E39, "valid_osgbpb_op")
label(0x9E44, "load_chan_handle")
label(0x9E83, "set_write_active")
label(0x9E86, "setup_gbpb_request")
label(0x9ED6, "loop_copy_opts_to_buf")
label(0x9EE1, "skip_struct_hole")
label(0x9EEA, "store_direction_flag")
label(0x9EF8, "store_port_and_send")
label(0x9F15, "loop_setup_addr_bytes")
label(0x9F2C, "loop_copy_offset")
label(0x9F40, "send_with_swap")
label(0x9F43, "recv_and_update")
label(0x9F55, "send_osbput_data")
label(0x9F6A, "write_block_entry")
label(0x9F78, "store_station_result")
label(0x9F7A, "loop_copy_opts_to_ws")
label(0x9F8C, "handle_cat_update")
label(0x9FC0, "loop_copy_to_host")
label(0x9FCD, "tube_write_setup")
label(0x9FDA, "set_tube_addr")
label(0x9FDF, "loop_write_to_tube")
label(0x9FE8, "loop_tube_delay")
label(0x9FF7, "update_cat_position")
label(0xA033, "clear_buf_after_write")
label(0xA035, "loop_clear_buf")
label(0xA04F, "loop_check_remaining")
label(0xA058, "done_write_block")
label(0xA083, "print_current_fs")
label(0xA0A5, "store_station_lo")
label(0xA0AD, "skip_if_no_station")
label(0xA0B1, "done_parse_fs_ps")
label(0xA0CC, "net_1_read_handle")
label(0xA0D2, "net_2_read_handle_entry")
label(0xA0DD, "return_zero_uninit")
label(0xA0DF, "store_pb_result")
label(0xA0E2, "net_3_close_handle")
label(0xA0F1, "mark_ws_uninit")
label(0xA11B, "dispatch_fs_cmd")
label(0xA12A, "restart_table_scan")
label(0xA132, "loop_match_char")
label(0xA141, "skip_entry_chars")
label(0xA14D, "loop_skip_to_next")
label(0xA152, "check_separator")
label(0xA158, "loop_check_sep_table")
label(0xA164, "sep_table_data")
label(0xA16D, "separator_matched")
label(0xA16F, "loop_skip_trail_spaces")
label(0xA175, "skip_dot_and_spaces")
label(0xA179, "check_cmd_flags")
label(0xA18A, "clear_v_flag")
label(0xA18B, "clear_c_flag")
label(0xA18C, "return_with_result")
label(0xA190, "loop_scan_past_word")
label(0xA191, "check_char_type")
label(0xA19F, "skip_sep_spaces")
label(0xA1A6, "set_c_and_return")
label(0xA1A9, "fscv_2_star_run")
label(0xA1B2, "open_file_for_run")
label(0xA1CA, "loop_check_handles")
label(0xA1D2, "alloc_run_fcb")
label(0xA1EE, "done_run_dispatch")
label(0xA1F1, "try_library_path")
label(0xA205, "loop_find_name_end")
label(0xA20D, "loop_shift_name_right")
label(0xA218, "loop_copy_lib_prefix")
label(0xA229, "retry_with_library")
label(0xA22B, "restore_filename")
label(0xA22D, "loop_restore_name")
label(0xA242, "library_tried")
label(0xA252, "check_exec_addr")
label(0xA254, "loop_check_exec_bytes")
label(0xA265, "alloc_run_channel")
label(0xA279, "library_dir_prefix")
label(0xA281, "setup_oscli_arg")
label(0xA28A, "loop_read_gs_string")
label(0xA290, "loop_skip_trailing")
label(0xA2D7, "dispatch_via_vector")
label(0xA2E2, "fsreply_5_set_lib")
label(0xA2EB, "loop_search_stn_bit2")
label(0xA301, "done_search_bit2")
label(0xA30F, "set_flags_bit2")
label(0xA316, "loop_search_stn_bit3")
label(0xA32C, "done_search_bit3")
label(0xA33A, "set_flags_bit3")
label(0xA34D, "loop_search_stn_boot")
label(0xA363, "done_search_boot")
label(0xA371, "set_flags_boot")
label(0xA373, "store_stn_flags_restore")
label(0xA376, "jmp_restore_fs_ctx")
label(0xA379, "fsreply_1_copy_handles_boot")
label(0xA383, "fsreply_2_copy_handles")
label(0xA39C, "check_auto_boot_flag")
label(0xA3C7, "boot_oscli_lo_table")
label(0xA3CB, "load_boot_type")
label(0xA3D9, "cmd_table_fs_lo")
label(0xA3DA, "cmd_table_fs_hi")
label(0xA45F, "cmd_table_nfs_iam")
label(0xA4E6, "loop_copy_osword_data")
label(0xA4FA, "loop_copy_osword_flag")
comment(0xA508, """\
OSWORD dispatch table (7 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_8_osword.
Maps OSWORD codes &0E-&14 to handler routines.""")

label(0xA508, "osword_dispatch_lo_table")
label(0xA50F, "osword_dispatch_hi_table")

# Mark OSWORD dispatch table entries as symbolic address pairs.
for i in range(7):
    rts_code_ptr(0xA508 + i, 0xA50F + i)
label(0xA516, "osword_0e_handler")
label(0xA526, "save_txcb_and_convert")
label(0xA573, "loop_copy_bcd_to_pb")
label(0xA583, "loop_bcd_add")
label(0xA589, "done_bcd_convert")
label(0xA58B, "osword_10_handler")
label(0xA594, "setup_ws_rx_ptrs")
label(0xA5A8, "osword_11_handler")
label(0xA61C, "osword_12_handler")
label(0xA631, "osword_13_dispatch")
label(0xA701, "copy_ws_byte_to_pb")
label(0xA844, "bridge_ws_init_data")
label(0xA850, "bridge_txcb_init_table")
label(0xA878, "loop_copy_bridge_init")
label(0xA88C, "loop_wait_ws_status")
label(0xA8A0, "loop_wait_tx_done")
label(0xA8C0, "bridge_responded")
label(0xA8D0, "osword_14_handler")
label(0xA8DE, "loop_copy_txcb_init")
label(0xA8E6, "store_txcb_init_byte")
label(0xA8FD, "loop_copy_ws_to_pb")
label(0xA926, "handle_tx_request")
label(0xA93D, "loop_send_pb_chars")
label(0xA950, "loop_bridge_tx_delay")
label(0xA959, "handle_burst_xfer")
label(0xA97A, "restore_regs_return")
label(0xA98C, "osword_handler_lo_table")
label(0xA995, "osword_handler_hi_table")
label(0xA9E9, "process_match_result")
label(0xA9F2, "save_tube_state")
label(0xA9F4, "loop_save_tube_bytes")
label(0xAA0B, "loop_poll_ws_status")
label(0xAA18, "loop_restore_stack")
label(0xAA1C, "store_stack_byte")
label(0xAA2D, "osword_claim_codes")
label(0xAA78, "loop_copy_ws_template")
label(0xAA8D, "store_tx_ptr_hi")
label(0xAA8F, "select_store_target")
label(0xAA95, "store_via_rx_ptr")
label(0xAA97, "advance_template_idx")
label(0xAA9B, "done_ws_template_copy")
label(0xAA9F, "ws_txcb_template_data")
label(0xAAEA, "loop_drain_printer_buf")
label(0xAB21, "done_spool_ctrl")
label(0xAB63, "check_spool_state")
label(0xAB72, "start_spool_retry")
label(0xAB77, "loop_copy_spool_tx")
label(0xAB96, "loop_copy_spool_rx")
label(0xABA3, "store_spool_rx_byte")
label(0xABA5, "advance_spool_rx_idx")
label(0xABCC, "spool_tx_succeeded")
label(0xABE1, "spool_tx_retry")
label(0xABFE, "error_printer_jammed")
label(0xAC1E, "loop_scan_disconnect")
label(0xAC2D, "verify_stn_match")
label(0xAC38, "send_disconnect_status")
label(0xAC55, "store_tx_ctrl_byte")
label(0xAC5D, "loop_wait_disc_tx_ack")
label(0xAC6E, "tx_econet_txcb_template")
label(0xAC7A, "rx_palette_txcb_template")
label(0xAC86, "lang_2_save_palette_vdu")
label(0xAC9D, "loop_read_palette")
label(0xACFB, "osbyte_mode_read_codes")
label(0xAD0E, "parse_cdir_size")
label(0xAD17, "loop_find_alloc_size")
label(0xAD1D, "done_cdir_size")
label(0xAD31, "cdir_alloc_size_table")
label(0xAD5D, "ex_set_lib_flag")
label(0xAD6E, "fscv_5_cat")
label(0xAD77, "cat_set_lib_flag")
label(0xAD84, "setup_ex_request")
label(0xADA0, "store_owner_flags")
label(0xADD1, "print_public_label")
label(0xADDB, "send_dir_info_req")
label(0xAE0A, "loop_print_option_str")
label(0xAE15, "print_dir_header")
label(0xAE3D, "setup_ex_pagination")
label(0xAE5D, "loop_scan_entry_data")
label(0xAE7D, "jmp_osnewl")
label(0xAEA9, "loop_shift_str_left")
label(0xAEB7, "loop_trim_trailing")
label(0xAEC6, "done_strip_prefix")
label(0xAEC9, "check_hash_prefix")
label(0xAECD, "error_bad_prefix")
label(0xAED0, "check_colon_prefix")
label(0xAEDF, "set_fs_select_flag")
label(0xAEE9, "option_str_offset_data")
label(0xAEED, "roff_off_string")
label(0xAEF5, "loop_copy_char")
label(0xAF05, "restore_after_check")
label(0xAF07, "advance_positions")
label(0xAF1E, "fsreply_0_print_dir")
label(0xAF20, "loop_scan_entries")
label(0xAF3A, "print_col_newline")
label(0xAF3C, "print_entry_char")
label(0xAF3F, "next_col_entry")
label(0xAF52, "done_extra_arg_check")
label(0xAF7D, "loop_divide_digit")
label(0xAF8D, "print_nonzero_digit")
label(0xAFA0, "loop_advance_char")
label(0xAFAD, "loop_skip_space_chars")
label(0xAFD8, "done_ps_available")
label(0xAFFB, "loop_copy_ps_tmpl")
label(0xB005, "no_ps_name_given")
label(0xB008, "save_ps_cmd_ptr")
label(0xB012, "loop_pad_ps_name")
label(0xB02A, "loop_read_ps_char")
label(0xB038, "done_ps_name_parse")
label(0xB04B, "loop_pop_ps_slot")
label(0xB06D, "done_ps_slot_mark")
label(0xB075, "done_ps_scan")
label(0xB08A, "print_ps_now")
label(0xB092, "done_ps_status_msg")
label(0xB095, "store_ps_station")
label(0xB0B6, "print_server_is_suffix")
label(0xB0E4, "loop_scan_ps_slots")
label(0xB0F4, "skip_next_ps_slot")
label(0xB0F8, "reinit_ps_slot")
label(0xB11B, "write_ps_slot_link_addr")
label(0xB120, "done_ps_slot_scan")
label(0xB12F, "loop_ps_delay")
label(0xB14B, "loop_push_ps_name")
label(0xB155, "loop_pop_ps_name")
label(0xB167, "loop_copy_tx_hdr")
label(0xB170, "ps_tx_header_template")
label(0xB184, "skip_if_local_net")
label(0xB18D, "print_station_only")
label(0xB1E1, "no_poll_name_given")
label(0xB1E4, "skip_if_no_poll_arg")
label(0xB1EC, "loop_pad_poll_name")
label(0xB204, "loop_read_poll_char")
label(0xB212, "done_poll_name_parse")
label(0xB22F, "loop_print_poll_name")
label(0xB23D, "done_poll_name_print")
label(0xB243, "loop_pop_poll_slot")
label(0xB278, "check_poll_jammed")
label(0xB27C, "print_poll_jammed")
label(0xB288, "check_poll_busy")
label(0xB2B8, "done_poll_status_line")
label(0xB2BB, "done_poll_slot_mark")
label(0xB2C6, "loop_copy_slot_tmpl")
label(0xB2D1, "subst_rx_page_byte")
label(0xB2D3, "store_slot_tmpl_byte")
label(0xB2E9, "done_uppercase_store")
label(0xB2FA, "parse_prot_keywords")
label(0xB2FE, "loop_match_prot_attr")
label(0xB310, "prot_check_arg_end")
label(0xB319, "done_prot_args")
label(0xB31A, "store_prot_mask")
label(0xB32B, "loop_match_unprot_attr")
label(0xB34D, "request_next_wipe")
label(0xB380, "check_wipe_attr")
label(0xB383, "loop_check_if_locked")
label(0xB387, "skip_wipe_locked")
label(0xB38C, "check_wipe_dir")
label(0xB395, "show_wipe_prompt")
label(0xB399, "loop_copy_wipe_name")
label(0xB3C2, "loop_print_wipe_info")
label(0xB3DB, "check_wipe_response")
label(0xB3ED, "loop_build_wipe_cmd")
label(0xB3F6, "skip_if_not_space")
label(0xB3FA, "set_wipe_cr_end")
label(0xB3FC, "store_wipe_tx_char")
label(0xB40B, "skip_wipe_to_next")
label(0xB411, "use_wipe_leaf_name")
label(0xB412, "loop_copy_wipe_leaf")
label(0xB43C, "loop_clear_chan_table")
label(0xB44C, "loop_mark_chan_avail")
label(0xB465, "error_chan_out_of_range")
label(0xB467, "return_chan_index")
label(0xB473, "error_chan_not_found")
label(0xB477, "net_channel_err_string")
label(0xB4B1, "error_chan_not_here")
label(0xB4BC, "loop_copy_chan_err_str")
label(0xB4CF, "loop_append_err_suffix")
label(0xB4FD, "loop_scan_fcb_slots")
label(0xB50B, "done_found_free_slot")
label(0xB548, "return_alloc_success")
label(0xB54E, "skip_set_carry")
label(0xB553, "loop_scan_fcb_down")
label(0xB557, "skip_if_slots_done")
label(0xB56B, "done_check_station")
label(0xB58F, "loop_find_fcb")
label(0xB596, "skip_if_no_wrap")
label(0xB5A0, "done_check_fcb_status")
label(0xB5AA, "done_select_fcb")
label(0xB5AB, "loop_scan_empty_fcb")
label(0xB5B2, "done_test_empty_slot")
label(0xB5C1, "skip_if_modified_fcb")
label(0xB5DE, "loop_clear_counters")
label(0xB62F, "done_restore_offset")
label(0xB657, "done_clear_fcb_active")
label(0xB662, "loop_save_tx_context")
label(0xB675, "done_save_context")
label(0xB678, "loop_find_pending_fcb")
label(0xB6CC, "done_init_wipe")
label(0xB6F2, "done_calc_offset")
label(0xB711, "loop_clear_buffer")
label(0xB716, "done_set_fcb_active")
label(0xB720, "loop_restore_workspace")
label(0xB72B, "loop_restore_tx_buf")
label(0xB735, "loop_save_before_match")
label(0xB73A, "loop_reload_attr")
label(0xB73D, "loop_next_fcb_slot")
label(0xB757, "done_test_fcb_active")
label(0xB78E, "return_test_offset")
label(0xB7AE, "loop_process_fcb")
label(0xB7B9, "done_flush_fcb")
label(0xB7BF, "done_advance_fcb")
label(0xB7EE, "done_read_fcb_byte")
label(0xB819, "error_end_of_file")
label(0xB82A, "done_load_from_buf")
label(0xB87D, "done_test_write_flag")
label(0xB88B, "done_find_write_fcb")
label(0xB8DD, "done_check_buf_offset")
label(0xB8F1, "done_set_dirty_flag")
label(0xB910, "done_inc_byte_count")
label(0xB953, "loop_copy_wipe_err_msg")
label(0xB960, "done_terminate_wipe_err")
label(0xB969, "done_toggle_station")
label(0xB98B, "open_and_read_file")


label(0x0406, "tube_addr_data_dispatch")
label(0x0421, "clear_tube_claim")
label(0x83EB, "discard_reset_rx")
label(0x83EE, "reset_adlc_rx_listen")
label(0x83F1, "set_nmi_rx_scout")
label(0x8505, "setup_cb1_sr_tx")
label(0x854A, "tx_done_fire_event")
label(0x8AE2, "scan_remote_keys")
label(0x8AFA, "save_text_ptr")
label(0x8B82, "help_print_nfs_cmds")
label(0x8B8D, "print_cmd_table")
label(0x8BA0, "print_cmd_table_loop")
label(0x8C28, "help_wrap_if_serial")
label(0x8C94, "print_version_header")
label(0x8CAE, "get_ws_page")
label(0x8CB5, "setup_ws_ptr")
label(0x8CF1, "notify_new_fs")
label(0x8CFA, "call_fscv")
label(0x8CFD, "issue_svc_15")
label(0x8D0C, "check_credits_easter_egg")
label(0x8DFE, "clear_if_station_match")
label(0x8E0A, "pass_send_cmd")
label(0x8E0E, "send_cmd_and_dispatch")
label(0x8E3C, "push_dispatch_lo")
label(0x8E76, "osbyte_x0_y0")
label(0x8E96, "store_ws_page_count")
label(0x8F40, "init_adlc_and_vectors")
label(0x8F53, "write_vector_entry")
label(0x8F73, "restore_fs_context")
label(0x8F80, "fscv_6_shutdown")
label(0x8FB2, "verify_ws_checksum")
label(0x8FCB, "error_net_checksum")
label(0x8FDD, "print_station_id")
label(0x911B, "print_hex_byte")
label(0x9124, "print_hex_nybble")
label(0x915A, "parse_addr_arg")
label(0x91F4, "err_bad_hex")
label(0x9201, "err_bad_station_num")
label(0x9244, "is_decimal_digit")
label(0x924C, "is_dec_digit_only")
label(0x9255, "get_access_bits")
label(0x925F, "get_prot_bits")
label(0x927D, "set_text_and_xfer_ptr")
label(0x9281, "set_xfer_params")
label(0x9287, "set_options_ptr")
label(0x928B, "clear_escapable")
label(0x9290, "cmp_5byte_handle")
label(0x92A1, "set_conn_active")
label(0x92B8, "clear_conn_active")
label(0x92E6, "error_bad_filename")
label(0x92F5, "check_not_ampersand")
label(0x92FD, "read_filename_char")
label(0x930E, "send_fs_request")
label(0x9313, "copy_fs_cmd_name")
label(0x9335, "parse_quoted_arg")
label(0x9451, "init_txcb_bye")
label(0x9453, "init_txcb_port")
label(0x945F, "init_txcb")
label(0x9483, "send_request_nowrite")
label(0x9487, "send_request_write")
label(0x9499, "save_net_tx_cb")
label(0x949A, "save_net_tx_cb_vset")
label(0x94C6, "prep_send_tx_cb")
label(0x94DC, "recv_and_process_reply")
label(0x955A, "check_escape")
label(0x9560, "raise_escape_error")
label(0x95C7, "wait_net_tx_ack")
label(0x95FB, "cond_save_error_code")
label(0x962B, "fixup_reply_status_a")
label(0x9636, "load_reply_and_classify")
label(0x9638, "classify_reply_error")
label(0x969D, "bad_str_anchor")
label(0x96DA, "check_net_error_code")
label(0x9738, "append_drv_dot_num")
label(0x975C, "append_space_and_num")
label(0x9767, "append_decimal_num")
label(0x9778, "append_decimal_digit")
label(0x9822, "init_tx_ptr_and_send")
label(0x982A, "send_net_packet")
label(0x987F, "init_tx_ptr_for_pass")
label(0x9887, "setup_pass_txbuf")
label(0x98F3, "load_text_ptr_and_parse")
label(0x98FF, "gsread_to_buf")
label(0x993D, "do_fs_cmd_iteration")
label(0x9984, "send_txcb_swap_addrs")
label(0x9A45, "print_load_exec_addrs")
label(0x9A50, "print_5_hex_bytes")
label(0x9A60, "copy_fsopts_to_zp")
label(0x9A6C, "skip_one_and_advance5")
label(0x9A6D, "advance_y_by_4")
label(0x9A72, "copy_workspace_to_fsopts")
label(0x9A7F, "retreat_y_by_4")
label(0x9A80, "retreat_y_by_3")
label(0x9A88, "check_and_setup_txcb")
label(0x9B86, "format_filename_field")
label(0x9CB9, "return_with_last_flag")
label(0x9CBB, "finalise_and_return")
label(0x9E03, "update_addr_from_offset9")
label(0x9E08, "update_addr_from_offset1")
label(0x9E0A, "add_workspace_to_fsopts")
label(0x9E0B, "adjust_fsopts_4bytes")
label(0x9EC0, "lookup_cat_entry_0")
label(0x9EC4, "lookup_cat_slot_data")
label(0x9ECB, "setup_transfer_workspace")
label(0x9FB8, "write_data_block")
label(0x9FF4, "tail_update_catalogue")
label(0xA05B, "tube_claim_c3")
label(0xA086, "print_fs_info_newline")
label(0xA08F, "parse_fs_ps_args")
label(0xA0B4, "get_pb_ptr_as_index")
label(0xA0B6, "byte_to_2bit_index")
label(0xA0FC, "fscv_3_star_cmd")
label(0xA10D, "cmd_fs_reentry")
label(0xA10F, "error_syntax")
label(0xA128, "match_fs_cmd")
label(0xA245, "error_bad_command")
label(0xA2DC, "fsreply_3_set_csd")
label(0xA2E8, "find_station_bit2")
label(0xA313, "find_station_bit3")
label(0xA34A, "flip_set_station_boot")
label(0xA3D0, "boot_cmd_oscli")
label(0xA4EF, "osword_setup_handler")
label(0xA57C, "bin_to_bcd")
label(0xA601, "store_osword_pb_ptr")
label(0xA612, "store_ptr_at_ws_y")
label(0xA868, "init_bridge_poll")
label(0xA964, "enable_irq_and_poll")
label(0xA981, "push_osword_handler_addr")
label(0xA9AC, "tx_econet_abort")
label(0xAA6A, "init_ws_copy_wide")
label(0xAA73, "init_ws_copy_narrow")
label(0xAA77, "ws_copy_vclr_entry")
label(0xAAD0, "reset_spool_buf_state")
label(0xAB00, "append_byte_to_rxbuf")
label(0xAB09, "handle_spool_ctrl_byte")
label(0xABEC, "err_printer_busy")
label(0xAC12, "send_disconnect_reply")
label(0xACCB, "commit_state_byte")
label(0xACD2, "serialise_palette_entry")
label(0xACE5, "read_osbyte_to_ws_x0")
label(0xACE7, "read_osbyte_to_ws")
label(0xAD2F, "cdir_dispatch_col")
label(0xAE70, "print_10_chars")
label(0xAE80, "parse_cmd_arg_y0")
label(0xAE82, "parse_filename_arg")
label(0xAE85, "parse_access_prefix")
label(0xAEA5, "strip_token_prefix")
label(0xAEF0, "copy_arg_to_buf_x0")
label(0xAEF2, "copy_arg_to_buf")
label(0xAEF4, "copy_arg_validated")
label(0xAF12, "mask_owner_access")
label(0xAF27, "ex_print_col_sep")
label(0xAF65, "print_num_no_leading")
label(0xAF68, "print_decimal_3dig")
label(0xAF76, "print_decimal_digit")
label(0xAF95, "save_ptr_to_os_text")
label(0xAFA1, "skip_to_next_arg")
label(0xAFB5, "save_ptr_to_spool_buf")
label(0xAFC0, "init_spool_drive")
label(0xAFF7, "copy_ps_data_y1c")
label(0xAFF9, "copy_ps_data")
label(0xB0A1, "print_file_server_is")
label(0xB0AB, "print_printer_server_is")
label(0xB0C6, "load_ps_server_addr")
label(0xB0D2, "pop_requeue_ps_scan")
label(0xB11A, "write_ps_slot_hi_link")
label(0xB13A, "write_ps_slot_byte_ff")
label(0xB141, "write_two_bytes_inc_y")
label(0xB149, "reverse_ps_name_to_tx")
label(0xB174, "print_station_addr")
label(0xB2C4, "init_ps_slot_from_rx")
label(0xB2DB, "store_char_uppercase")
label(0xB41F, "flush_and_read_char")
label(0xB439, "init_channel_table")
label(0xB45B, "attr_to_chan_index")
label(0xB46A, "check_chan_char")
label(0xB472, "err_net_chan_invalid")
label(0xB475, "err_net_chan_not_found")
label(0xB49D, "lookup_chan_by_char")
label(0xB4DC, "store_result_check_dir")
label(0xB4E3, "check_not_dir")
label(0xB4FA, "alloc_fcb_slot")
label(0xB52E, "alloc_fcb_or_error")
label(0xB54A, "close_all_net_chans")
label(0xB551, "scan_fcb_flags")
label(0xB57A, "match_station_net")
label(0xB589, "find_open_fcb")
label(0xB5CC, "init_wipe_counters")
label(0xB5EF, "start_wipe_pass")
label(0xB660, "save_fcb_context")
label(0xB729, "restore_catalog_entry")
label(0xB738, "find_matching_fcb")
label(0xB791, "inc_fcb_byte_count")
label(0xB79F, "process_all_fcbs")
label(0xB920, "send_wipe_request")
label(0xB979, "send_and_receive")
label(0xB995, "loop_read_print_byte")
label(0xB9A1, "done_print_escape")
label(0xB9B0, "done_store_prev_char")
label(0xB9B2, "loop_write_char")
label(0xB9B8, "done_handle_line_end")
label(0xB9C5, "done_normalise_crlf")
label(0xB9D2, "done_write_newline")
label(0xB9D8, "done_check_cr_lf")
label(0xB9DF, "done_check_lf_cr")
label(0xB9E4, "done_consume_pair")
label(0xB9EA, "abort_if_escape")
label(0xB9EF, "error_escape_pressed")
label(0xBA0D, "loop_push_zero_buf")
label(0xBA1E, "loop_dump_line")
label(0xBA25, "loop_read_dump_byte")
label(0xBA37, "done_check_dump_eof")
label(0xBA3E, "loop_pop_stack_buf")
label(0xBA45, "done_check_boundary")
label(0xBA50, "done_start_dump_addr")
label(0xBA52, "loop_print_addr_byte")
label(0xBA63, "loop_inc_dump_addr")
label(0xBA7B, "loop_print_dump_hex")
label(0xBA85, "loop_next_dump_col")
label(0xBA9B, "done_print_separator")
label(0xBAA7, "loop_print_dump_ascii")
label(0xBAAF, "skip_non_printable")
label(0xBAB1, "done_test_del")
label(0xBAC0, "done_end_dump_line")
label(0xBAC9, "done_dump_eof")
label(0xBACE, "print_dump_header")
label(0xBAE4, "loop_print_col_num")
label(0xBB0C, "close_ws_file")
label(0xBB13, "open_file_for_read")
label(0xBB39, "done_restore_text_ptr")
label(0xBB41, "loop_skip_filename")
label(0xBB4C, "loop_skip_fn_spaces")
label(0xBB53, "return_with_fn_offset")
label(0xBB55, "parse_dump_range")
label(0xBB5A, "loop_clear_hex_accum")
label(0xBB61, "loop_parse_hex_digit")
label(0xBB80, "done_mask_hex_digit")
label(0xBB87, "loop_shift_nibble")
label(0xBB8A, "loop_rotate_hex_accum")
label(0xBBAB, "error_hex_overflow")
label(0xBBAF, "error_bad_hex_value")
label(0xBBB5, "loop_skip_hex_spaces")
label(0xBBB6, "done_test_hex_space")
label(0xBBBE, "init_dump_buffer")
label(0xBBD7, "loop_cmp_file_length")
label(0xBBE3, "done_check_outside")
label(0xBBE9, "error_outside_file")
label(0xBBFE, "loop_copy_start_addr")
label(0xBC03, "done_advance_start")
label(0xBC1B, "loop_copy_osfile_ptr")
label(0xBC2E, "loop_shift_osfile_data")
label(0xBC3D, "loop_check_ff_addr")
label(0xBC4A, "loop_zero_load_addr")
label(0xBC51, "done_parse_disp_base")
label(0xBC66, "done_add_disp_base")
label(0xBC6B, "loop_add_disp_bytes")
label(0xBC7B, "loop_store_disp_addr")
label(0xBC84, "advance_x_by_8")
label(0xBC87, "advance_x_by_4")
label(0xBC8A, "inx4")
label(0xBE9A, "loop_copy_reloc_pages")
label(0xBEB4, "loop_copy_zp_workspace")

# ============================================================
# ROM entry points and subroutines
# ============================================================

subroutine(0x8023, "svc5_irq_check",
    title="Service 5: unrecognised interrupt (CB1 dispatch)",
    description="Tests IFR bit 2 (CB1 active edge) to check for a\n"
    "shift register transfer complete. If CB1 is not set,\n"
    "returns A=5 to pass the service call on. If CB1 is\n"
    "set, saves registers, reads the VIA ACR, clears and\n"
    "restores the SR mode bits from ws_0d64, then dispatches\n"
    "the TX completion callback via the operation type stored\n"
    "in tx_op_type. The indexed handler performs the completion\n"
    "action (e.g. resuming background print spooling) before\n"
    "returning with A=0 to claim the service call.",
    on_entry={"a": "5 (service call number)",
              "x": "ROM slot",
              "y": "parameter"})

subroutine(0x8A0B, "service_handler",
    title="Service call dispatch",
    description="Handles service calls 1, 4, 8, 9, 13, 14, and 15.\n"
    "Service 1: absolute workspace claim.\n"
    "Service 4: unrecognised star command.\n"
    "Service 8: unrecognised OSWORD.\n"
    "Service 9: *HELP.\n"
    "Service 13: ROM initialisation.\n"
    "Service 14: ROM initialisation complete.\n"
    "Service 15: vectors claimed.",
    on_entry={"a": "service call number", "x": "ROM slot", "y": "parameter"})


# ============================================================
# Relocated code labels (from NFS 3.65 correspondence)
# ============================================================
# Pages 4-5 are 100% opcode-identical to NFS 3.65.
# Page 6 is 74% matching. Zero page block is 70% matching.

label(0x0020, "tube_send_zero_r2")
label(0x0029, "tube_brk_send_loop")
label(0x002A, "tube_send_error_byte")
label(0x0032, "tube_reset_stack")
label(0x0036, "tube_main_loop")
label(0x003B, "tube_handle_wrch")
label(0x0041, "tube_poll_r2")
label(0x0050, "tube_dispatch_cmd")
label(0x0051, "tube_cmd_lo")
label(0x0053, "tube_transfer_addr")
label(0x0054, "tube_xfer_page")
label(0x0055, "tube_xfer_addr_2")
label(0x0056, "tube_xfer_addr_3")
label(0x0414, "tube_release_claim")
label(0x0428, "addr_claim_external")
label(0x0432, "accept_new_claim")
label(0x0434, "return_tube_init")
label(0x0435, "tube_transfer_setup")
label(0x0437, "setup_data_transfer")
label(0x0446, "send_xfer_addr_bytes")
label(0x0463, "skip_r3_flush")
label(0x0466, "poll_r4_copro_ack")
label(0x0471, "tube_sendw_complete")
label(0x047A, "copro_ack_nmi_check")
label(0x0482, "skip_nmi_release")
label(0x0483, "return_tube_xfer")
label(0x0484, "tube_begin")
label(0x048C, "check_break_type")
label(0x0498, "claim_addr_ff")
label(0x04A2, "next_rom_page")
label(0x04AB, "send_rom_page_bytes")
label(0x04C0, "skip_addr_carry")
label(0x04CB, "tube_claim_default")
label(0x04D2, "tube_init_reloc")
label(0x04E5, "scan_copyright_end")
label(0x04FB, "store_xfer_end_addr")
label(0x0518, "tube_ctrl_values")
label(0x0520, "tube_osbput")
label(0x0527, "tube_poll_r1_wrch")
label(0x052D, "tube_osbget")
label(0x0537, "tube_osrdch")
label(0x053A, "tube_rdch_reply")
label(0x0542, "tube_osfind")
label(0x0552, "tube_osfind_close")
label(0x055E, "tube_osargs")
label(0x0562, "tube_read_params")
label(0x0564, "read_osargs_params")
label(0x0577, "send_osargs_result")
label(0x0582, "tube_read_string")
label(0x0586, "strnh")
label(0x0593, "string_buf_done")
label(0x0596, "tube_oscli")
label(0x059C, "tube_reply_ack")
label(0x059E, "tube_reply_byte")
label(0x05A6, "mj")
label(0x05A9, "tube_osfile")
label(0x05AB, "argsw")
label(0x05C7, "send_osfile_ctrl_blk")
label(0x05D1, "tube_osgbpb")
label(0x05D3, "read_osgbpb_ctrl_blk")
label(0x05E6, "send_osgbpb_result")
label(0x05F2, "tube_osbyte_2param")
label(0x05FC, "tube_poll_r2_result")
label(0x0604, "bytex")
label(0x0607, "tube_osbyte_long")
label(0x061D, "tube_osbyte_send_y")
label(0x0625, "tube_osbyte_short")
label(0x0627, "tube_osword")
label(0x062B, "tube_osword_read")
label(0x0630, "tube_osbyte_send_x")
label(0x0636, "tube_osword_read_lp")
label(0x0645, "skip_param_read")
label(0x064C, "poll_r2_osword_result")
label(0x0657, "tube_osword_write")
label(0x065A, "tube_osword_write_lp")
label(0x0665, "tube_return_main")
label(0x0668, "tube_osword_rdln")
label(0x066A, "read_rdln_ctrl_block")
label(0x0680, "tube_rdln_send_line")
label(0x0687, "tube_rdln_send_loop")
label(0x068A, "tube_rdln_send_byte")
label(0x0695, "tube_send_r2")
label(0x069E, "tube_send_r4")
label(0x06A7, "tube_escape_check")
label(0x06AD, "tube_event_handler")
label(0x06BC, "tube_send_r1")
label(0x06C5, "tube_read_r2")
label(0x06EC, "svc_11_nmi_claim")

# ============================================================
# ROM code labels (from NFS 3.65 correspondence)
# ============================================================
# About 27% of NFS 3.65 main ROM opcodes match in ANFS.

label(0x8004, "service_handler_lo")
label(0x8015, "copyright_string")
label(0x8061, "dispatch_svc5")
label(0x8068, "svc_5_unknown_irq")
label(0x8089, "init_nmi_workspace")
label(0x808B, "copy_nmi_shim")
label(0x80CB, "accept_frame")
label(0x80DE, "scout_reject")
label(0x80E6, "accept_local_net")
label(0x80E9, "accept_scout_net")
label(0x80FF, "scout_discard")
label(0x8107, "scout_loop_rda")
label(0x8117, "scout_loop_second")
label(0x8152, "scout_no_match")
label(0x8155, "scout_match_port")
label(0x815F, "scan_port_list")
label(0x8168, "scan_nfs_port_list")
label(0x816C, "check_port_slot")
label(0x816E, "scout_ctrl_check")
label(0x8180, "check_station_filter")
label(0x818A, "scout_port_match")
label(0x8194, "next_port_slot")
label(0x81A1, "discard_no_match")
label(0x81A4, "try_nfs_port_list")
label(0x81AF, "port_match_found")
label(0x81C1, "send_data_rx_ack")
label(0x81D2, "data_rx_setup")
label(0x81F0, "nmi_data_rx_net")
label(0x8206, "nmi_data_rx_skip")
label(0x8211, "install_data_rx_handler")
label(0x8224, "install_tube_rx")
label(0x822B, "nmi_error_dispatch")
label(0x8233, "rx_error_reset")
label(0x823E, "data_rx_loop")
label(0x824E, "read_sr2_between_pairs")
label(0x8255, "read_second_rx_byte")
label(0x8265, "check_sr2_loop_again")
label(0x8284, "read_last_rx_byte")
label(0x8293, "send_ack")
label(0x8296, "nmi_data_rx_tube")
label(0x8299, "rx_tube_data")
label(0x82B6, "data_rx_tube_error")
label(0x82B9, "data_rx_tube_complete")
label(0x82EF, "ack_tx_configure")
label(0x82FD, "ack_tx_write_dest")
label(0x833E, "start_data_tx")
label(0x8341, "dispatch_nmi_error")
label(0x8344, "advance_rx_buffer_ptr")
label(0x834F, "add_rxcb_ptr")
label(0x837D, "inc_rxcb_ptr")
label(0x8388, "skip_tube_update")
label(0x838A, "return_rx_complete")
label(0x839A, "rx_complete_update_rxcb")
label(0x839F, "add_buf_to_base")
label(0x83A6, "inc_rxcb_buf_hi")
label(0x83A8, "store_buf_ptr_lo")
label(0x83AA, "store_rxcb_buf_ptr")
label(0x83AF, "store_rxcb_buf_hi")
label(0x83B1, "skip_buf_ptr_update")
label(0x8406, "copy_scout_to_buffer")
label(0x840C, "copy_scout_select")
label(0x8413, "copy_scout_bytes")
label(0x8421, "next_scout_byte")
label(0x8428, "scout_copy_done")
label(0x842D, "copy_scout_via_tube")
label(0x843F, "release_tube")
label(0x8448, "clear_release_flag")
label(0x8462, "rotate_prot_mask")
label(0x8468, "dispatch_imm_op")
label(0x8473, "scout_page_overflow")
label(0x8475, "check_scout_done")
label(0x847B, "imm_op_out_of_range")
label(0x8498, "copy_addr_loop")
label(0x84A2, "svc5_dispatch_lo")
label(0x84D3, "set_tx_reply_flag")
label(0x84DB, "rx_imm_halt_cont")
label(0x84E0, "tx_cr2_setup")
label(0x84E5, "tx_nmi_setup")
label(0x84EC, "imm_op_build_reply")
label(0x8522, "imm_op_discard")
label(0x856C, "halt_spin_loop")
label(0x857B, "tx_done_exit")
label(0x8582, "tx_begin")
label(0x859A, "tx_imm_op_setup")
label(0x85AE, "calc_peek_poke_size")
label(0x85C5, "tx_ctrl_range_check")
label(0x85C9, "check_imm_range")
label(0x85CF, "copy_imm_params")
label(0x85D9, "tx_line_idle_check")
label(0x85F3, "test_inactive_retry")
label(0x85F5, "intoff_test_inactive")
label(0x85FB, "test_line_idle")
label(0x860F, "inactive_retry")
label(0x8625, "tx_active_start")
label(0x8635, "tx_no_clock_error")
label(0x8637, "store_tx_error")
label(0x8689, "store_status_add4")
label(0x8690, "add_bytes_loop")
label(0x86A2, "setup_data_xfer")
label(0x86B8, "copy_bcast_addr")
label(0x86C4, "setup_unicast_xfer")
label(0x86C9, "proc_op_status2")
label(0x86CB, "store_status_copy_ptr")
label(0x86CE, "skip_buf_setup")
label(0x86D9, "tx_ctrl_exit")
label(0x86E6, "tx_fifo_write")
label(0x8706, "tx_error")
label(0x870A, "tx_fifo_not_ready")
label(0x8711, "tx_store_error")
label(0x8714, "delay_nmi_disable")
label(0x8735, "check_handshake_bit")
label(0x873F, "install_reply_scout")
label(0x876C, "reject_reply")
label(0x87C7, "data_tx_begin")
label(0x87D5, "install_imm_data_nmi")
label(0x87EB, "data_tx_check_fifo")
label(0x87FB, "write_second_tx_byte")
label(0x880B, "check_irq_loop")
label(0x8813, "data_tx_last")
label(0x8824, "install_saved_handler")
label(0x882D, "nmi_data_tx_tube")
label(0x8830, "tube_tx_fifo_write")
label(0x8848, "write_second_tube_byte")
label(0x8852, "tube_tx_inc_byte2")
label(0x8856, "tube_tx_inc_byte3")
label(0x8857, "tube_tx_inc_operand")
label(0x885A, "tube_tx_inc_byte4")
label(0x885E, "check_tube_irq_loop")
label(0x885F, "tube_tx_sr1_operand")
label(0x8866, "tx_tdra_error")
label(0x888E, "nmi_final_ack_net")
label(0x88BF, "check_fv_final_ack")
label(0x88CA, "tx_result_fail")
label(0x8908, "calc_transfer_size")
label(0x8938, "restore_x_and_return")
label(0x893B, "fallback_calc_transfer")
label(0x895E, "nmi_shim_rom_src")
label(0x8979, "wait_idle_and_reset")
label(0x897E, "poll_nmi_idle")
label(0x899A, "reset_enter_listen")
label(0x899C, "listen_jmp_hi")

# Entry points from NFS 3.65 correspondence
entry(0x0032)
entry(0x0036)
entry(0x0607)
entry(0x0625)
entry(0x0627)
entry(0x0668)
entry(0x06A7)
entry(0x06AD)
entry(0x06BC)
entry(0x06EF)
entry(0x8068)
entry(0x80B3)
entry(0x80D0)
entry(0x8102)
entry(0x81D2)
entry(0x81DC)
entry(0x81F0)
entry(0x8206)
entry(0x8239)
entry(0x8296)
entry(0x831B)
entry(0x8365)
entry(0x838B)
entry(0x84EC)
entry(0x85EA)
entry(0x86E0)
entry(0x8706)
entry(0x871C)
entry(0x8728)
entry(0x8744)
entry(0x8758)
entry(0x876F)
entry(0x87B7)
entry(0x87DC)
entry(0x882D)
entry(0x886E)
entry(0x887A)
entry(0x888E)
entry(0x88A2)
entry(0x88C6)
entry(0x88CC)
entry(0x893B)
entry(0x899D)
entry(0x89AB)

# ============================================================
# Subroutines (from NFS 3.65 correspondence)
# ============================================================

subroutine(0x0406, "tube_addr_data_dispatch",
    title="Tube address/data dispatch",
    description="Called by 10 sites across the Tube host and Econet\n"
    "code. Routes requests based on the value of A:\n"
    "  A < &80: data transfer setup (SENDW) at &0435\n"
    "  &80 <= A < &C0: release -- maps A via ORA #&40\n"
    "    and compares with tube_claimed_id; if we own\n"
    "    this address, falls through to tube_release_claim\n"
    "  A >= &C0: external address claim from another host\n"
    "Falls through to tube_release_claim when releasing our\n"
    "current claim.",
    on_entry={"a": "request type (<&80 data, &80-&BF release, &C0+ claim)",
              "x": "transfer address low (data transfer only)",
              "y": "transfer address high (data transfer only)"})
subroutine(0x0414, "tube_release_claim",
    title="Release Tube address claim via R4 command 5",
    description="Saves interrupt state (PHP/SEI) to protect the R4\n"
    "protocol sequence, sends R4 command 5 (release) followed\n"
    "by the currently-claimed address from tube_claimed_id\n"
    "(&15), then restores interrupts (PLP). Falls through to\n"
    "clear_tube_claim to reset the claimed-address state to\n"
    "the &80 sentinel.")
subroutine(0x0421, "clear_tube_claim",
    title="Reset Tube address claim state",
    description="Stores &80 into both tube_claimed_id (&15) and\n"
    "tube_claim_flag (&14). The &80 sentinel indicates no\n"
    "address is currently claimed and no claim is in\n"
    "progress. Called after tube_release_claim (via\n"
    "fall-through) and during initial workspace setup.")
subroutine(0x0484, "tube_begin",
    title="Tube host startup entry (BEGIN)",
    description="Entry point via JMP from &0400. Enables interrupts, checks\n"
    "break type via OSBYTE &FD: soft break re-initialises Tube and\n"
    "restarts, hard break claims address &FF. Sends ROM contents\n"
    "to co-processor page by page via SENDW, then claims the final\n"
    "transfer address.")
subroutine(0x04CB, "tube_claim_default",
    title="Claim default Tube transfer address",
    description="Sets Y=0, X=&53 (address &0053), then JMP tube_addr_claim\n"
    "to initiate a Tube address claim for the default transfer\n"
    "address. Called from the BEGIN startup path and after the\n"
    "page transfer loop completes.")
subroutine(0x04D2, "tube_init_reloc",
    title="Initialise relocation address for ROM transfer",
    description="Sets the Tube transfer source page to &8000\n"
    "(tube_xfer_page = &80) and the page counter to &80.\n"
    "Checks ROM type bit 5 for a relocation address in the\n"
    "ROM header. If set, scans past the null-terminated\n"
    "copyright string and extracts the 4-byte relocation\n"
    "address into tube_transfer_addr (&53), tube_xfer_page\n"
    "(&54), tube_xfer_addr_2 (&55), and tube_xfer_addr_3\n"
    "(&56). If clear, uses the default &8000 start address.\n"
    "Called twice during tube_begin: once for initial setup\n"
    "and once after each page transfer completes.")
subroutine(0x0582, "tube_read_string",
    title="Read string from Tube R2 into buffer",
    description="Loops reading bytes from tube_read_r2 into the\n"
    "string buffer at &0700, storing at string_buf+Y.\n"
    "Terminates on CR (&0D) or when Y wraps to zero\n"
    "(256-byte overflow). Returns with X=0, Y=7 so that\n"
    "XY = &0700, ready for OSCLI or OSFIND dispatch.\n"
    "Called by the Tube OSCLI and OSFIND handlers.",
    on_exit={"x": "0 (low byte of &0700)",
             "y": "7 (high byte of &0700)"})
subroutine(0x0695, "tube_send_r2",
    title="Send byte to Tube data register R2",
    description="Polls Tube status register 2 until bit 6 (TDRA)\n"
    "is set, then writes A to the data register. Uses a\n"
    "tight BIT/BVC polling loop. Called by 12 sites\n"
    "across the Tube host code for all R2 data\n"
    "transmission: command responses, file data, OSBYTE\n"
    "results, and control block bytes.",
    on_entry={"a": "byte to send"},
    on_exit={"a": "preserved (value written)"})
subroutine(0x069E, "tube_send_r4",
    title="Send byte to Tube data register R4",
    description="Polls Tube status register 4 until bit 6 is set,\n"
    "then writes A to the data register. Uses a tight\n"
    "BIT/BVC polling loop. R4 is the command/control\n"
    "channel used for address claims (ADRR), data transfer\n"
    "setup (SENDW), and release commands. Called by 7\n"
    "sites, primarily during tube_release_claim and\n"
    "tube_transfer_setup sequences.",
    on_entry={"a": "byte to send"},
    on_exit={"a": "preserved (value written)"})
subroutine(0x06BC, "tube_send_r1",
    title="Send byte to Tube data register R1",
    description="Polls Tube status register 1 until bit 6 is set,\n"
    "then writes A to the data register. Uses a tight\n"
    "BIT/BVC polling loop. R1 is used for asynchronous\n"
    "event and escape notification to the co-processor.\n"
    "Called by tube_event_handler to forward event type,\n"
    "Y, and X parameters, and reached via BMI from\n"
    "tube_escape_check when the escape flag is set.",
    on_entry={"a": "byte to send"},
    on_exit={"a": "preserved (value written)"})
subroutine(0x06C5, "tube_read_r2",
    title="Read a byte from Tube data register R2",
    description="Polls Tube status register 2 until bit 7 (RDA)\n"
    "is set, then loads and returns the byte from Tube\n"
    "data register 2. Uses a BIT/BPL polling loop (testing\n"
    "the N flag). R2 is the primary data channel from the\n"
    "co-processor. Called by 14 sites across the Tube host\n"
    "code for command dispatch, OSFILE/OSGBPB control block\n"
    "reads, string reads, and OSBYTE parameter reception.",
    on_exit={"a": "byte read from R2"})
subroutine(0x0520, "tube_osbput",
    title="Tube OSBPUT handler (R2 cmd 8)",
    description="Reads file handle and data byte from R2, then\n"
    "calls OSBPUT (&FFD4) to write the byte. Falls through\n"
    "to tube_reply_ack to send &7F acknowledgement.")
subroutine(0x052D, "tube_osbget",
    title="Tube OSBGET handler (R2 cmd 7)",
    description="Reads file handle from R2, calls OSBGET (&FFD7)\n"
    "to read a byte, then falls through to tube_rdch_reply\n"
    "which encodes the carry flag (error) into bit 7 and\n"
    "sends the result byte via R2.")
subroutine(0x0537, "tube_osrdch",
    title="Tube OSRDCH handler (R2 cmd 0)",
    description="Calls OSRDCH (&FFE0) to read a character from\n"
    "the current input stream, then falls through to\n"
    "tube_rdch_reply which encodes the carry flag (error)\n"
    "into bit 7 and sends the result byte via R2.")
subroutine(0x0542, "tube_osfind",
    title="Tube OSFIND handler (R2 cmd 9)",
    description="Reads open mode from R2. If zero, reads a file\n"
    "handle and closes that file. Otherwise saves the mode,\n"
    "reads a filename string into &0700 via tube_read_string,\n"
    "then calls OSFIND (&FFCE) to open the file. Sends the\n"
    "resulting file handle (or &00) via tube_reply_byte.")
subroutine(0x055E, "tube_osargs",
    title="Tube OSARGS handler (R2 cmd 6)",
    description="Reads file handle from R2 into Y, then reads\n"
    "a 4-byte argument and reason code into zero page.\n"
    "Calls OSARGS (&FFDA), sends the result A and 4-byte\n"
    "return value via R2, then returns to the main loop.")
subroutine(0x0596, "tube_oscli",
    title="Tube OSCLI handler (R2 cmd 1)",
    description="Reads a command string from R2 into &0700 via\n"
    "tube_read_string, then calls OSCLI (&FFF7) to execute\n"
    "it. Falls through to tube_reply_ack to send &7F\n"
    "acknowledgement.")
subroutine(0x05A9, "tube_osfile",
    title="Tube OSFILE handler (R2 cmd 10)",
    description="Reads a 16-byte control block into zero page,\n"
    "a filename string into &0700 via tube_read_string,\n"
    "and a reason code from R2. Calls OSFILE (&FFDD),\n"
    "then sends the result A and updated 16-byte control\n"
    "block back via R2. Returns to the main loop via mj.")
subroutine(0x05D1, "tube_osgbpb",
    title="Tube OSGBPB handler (R2 cmd 11)",
    description="Reads a 13-byte control block and reason code\n"
    "from R2 into zero page. Calls OSGBPB (&FFD1), then\n"
    "sends 12 result bytes and the carry+result byte\n"
    "(via tube_rdch_reply) back via R2.")
subroutine(0x05F2, "tube_osbyte_2param",
    title="Tube OSBYTE 2-param handler (R2 cmd 2)",
    description="Reads X and A from R2, calls OSBYTE (&FFF4)\n"
    "with Y=0, then sends the result X via\n"
    "tube_reply_byte. Used for OSBYTE calls that take\n"
    "only A and X parameters.")
subroutine(0x0607, "tube_osbyte_long",
    title="Tube OSBYTE 3-param handler (R2 cmd 3)",
    description="Reads X, Y, and A from R2, calls OSBYTE\n"
    "(&FFF4), then sends carry+Y and X as result bytes\n"
    "via R2. Used for OSBYTE calls needing all three\n"
    "parameters and returning both X and Y results.")
subroutine(0x0627, "tube_osword",
    title="Tube OSWORD handler (R2 cmd 4)",
    description="Reads OSWORD number A and in-length from R2,\n"
    "then reads the parameter block into &0128. Calls\n"
    "OSWORD (&FFF1), then sends the out-length result\n"
    "bytes from the parameter block back via R2.\n"
    "Returns to the main loop via tube_return_main.")
subroutine(0x0668, "tube_osword_rdln",
    title="Tube OSWORD 0 handler (R2 cmd 5)",
    description="Handles OSWORD 0 (read line) specially. Reads\n"
    "4 parameter bytes from R2 into &0128 (max length,\n"
    "min char, max char, flags). Calls OSWORD 0 (&FFF1)\n"
    "to read a line, then sends &7F+CR or the input line\n"
    "byte-by-byte via R2, followed by &80 (error/escape)\n"
    "or &7F (success).")
subroutine(0x8069, "adlc_init",
    title="ADLC initialisation",
    description="Initialise ADLC hardware and Econet workspace.\n"
    "Reads station ID via &FE18 (INTOFF side effect),\n"
    "performs a full ADLC reset (adlc_full_reset), then\n"
    "checks for Tube co-processor via OSBYTE &EA and\n"
    "stores the result in l0d63. Issues NMI claim service\n"
    "request (OSBYTE &8F, X=&0C). Falls through to\n"
    "init_nmi_workspace to copy the NMI shim to RAM.")
subroutine(0x8089, "init_nmi_workspace",
    title="Initialise NMI workspace (skip service request)",
    description="Copies 32 bytes of NMI shim code from ROM\n"
    "(listen_jmp_hi) to &0D00, then patches the current\n"
    "ROM bank number into the self-modifying code at\n"
    "&0D07. Clears tx_src_net, need_release_tube, and\n"
    "tx_op_type to zero. Reads station ID into tx_src_stn\n"
    "(&0D22). Sets ws_0d60 and ws_0d62 to &80 to mark\n"
    "TX complete and Econet initialised. Finally re-enables\n"
    "NMIs via INTON (&FE20 read).")
subroutine(0x80B3, "nmi_rx_scout",
    title="NMI RX scout handler (initial byte)",
    description="Default NMI handler for incoming scout frames. Checks if the frame\n"
    "is addressed to us or is a broadcast. Installed as the NMI target\n"
    "during idle RX listen mode.\n"
    "Tests SR2 bit0 (AP = Address Present) to detect incoming data.\n"
    "Reads the first byte (destination station) from the RX FIFO and\n"
    "compares against our station ID. Reading &FE18 also disables NMIs\n"
    "(INTOFF side effect).")
subroutine(0x80D0, "nmi_rx_scout_net",
    title="RX scout second byte handler",
    description="Reads the second byte of an incoming scout (destination network).\n"
    "Checks for network match: 0 = local network (accept), &FF = broadcast\n"
    "(accept and flag), anything else = reject.\n"
    "Installs the scout data reading loop handler at &970E.")
subroutine(0x80F2, "scout_error",
    title="Scout error/discard handler",
    description="Handles scout reception errors and end-of-frame\n"
    "conditions. Reads SR2 and tests AP|RDA (bits 0|7):\n"
    "if neither set, the frame ended cleanly and is\n"
    "simply discarded. If unexpected data is present,\n"
    "performs a full ADLC reset. Also serves as the\n"
    "common discard path for address/network mismatches\n"
    "from nmi_rx_scout and scout_complete -- reached by\n"
    "5 branch sites across the scout reception chain.")
subroutine(0x812C, "scout_complete",
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
subroutine(0x81DC, "nmi_data_rx",
    title="Data frame RX handler (four-way handshake)",
    description="Receives the data frame after the scout ACK has been sent.\n"
    "First checks AP (Address Present) for the start of the data frame.\n"
    "Reads and validates the first two address bytes (dest_stn, dest_net)\n"
    "against our station address, then installs continuation handlers\n"
    "to read the remaining data payload into the open port buffer.\n"
    "\n"
    "Handler chain: &97E6 (AP+addr check) -> &97FA (net=0 check) ->\n"
    "&9810 (skip ctrl+port) -> &9843 (bulk data read) -> &9877 (completion)")
subroutine(0x8211, "install_data_rx_handler",
    title="Install data RX bulk or Tube handler",
    description="Selects between the normal bulk RX handler (&8239)\n"
    "and the Tube RX handler based on bit 1 of rx_src_net\n"
    "(tx_flags). If normal mode, loads the handler address\n"
    "&8239 and checks SR1 bit 7: if IRQ is already asserted\n"
    "(more data waiting), jumps directly to nmi_data_rx_bulk\n"
    "to avoid NMI re-entry overhead. Otherwise installs the\n"
    "handler via set_nmi_vector and returns via RTI.")
subroutine(0x822B, "nmi_error_dispatch",
    title="NMI error handler dispatch",
    description="Common error/abort entry used by 12 call sites. Checks\n"
    "tx_flags bit 7: if clear, does a full ADLC reset and returns\n"
    "to idle listen (RX error path); if set, jumps to tx_result_fail\n"
    "(TX not-listening path).")
subroutine(0x8239, "nmi_data_rx_bulk",
    title="Data frame bulk read loop",
    description="Reads data payload bytes from the RX FIFO and stores them into\n"
    "the open port buffer at (open_port_buf),Y. Reads bytes in pairs\n"
    "(like the scout data loop), checking SR2 between each pair.\n"
    "SR2 non-zero (FV or other) -> frame completion at &9877.\n"
    "SR2 = 0 -> RTI, wait for next NMI to continue.")
subroutine(0x826D, "data_rx_complete",
    title="Data frame completion",
    description="Reached when SR2 non-zero during data RX (FV detected).\n"
    "Same pattern as scout completion (&9738): disables PSE (CR2=&84,\n"
    "CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.\n"
    "If extra data available and buffer space remains, stores it.\n"
    "Proceeds to send the final ACK via &98EE.")
subroutine(0x82E4, "ack_tx",
    title="ACK transmission",
    description="Sends a scout ACK or final ACK frame as part of the four-way handshake.\n"
    "If bit7 of &0D4A is set, this is a final ACK -> completion (&9EA8).\n"
    "Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK\n"
    "frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).\n"
    "The ACK frame has no data payload -- just address bytes.\n"
    "\n"
    "After writing the address bytes to the TX FIFO, installs the next\n"
    "NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)\n"
    "and sends TX_LAST_DATA (CR2=&3F) to close the frame.")
subroutine(0x831B, "nmi_ack_tx_src",
    title="ACK TX continuation",
    description="Continuation of ACK frame transmission. Reads our\n"
    "station ID from &FE18 (INTOFF side effect), tests\n"
    "TDRA via SR1, and writes station + network=0 to the\n"
    "TX FIFO, completing the 4-byte ACK address header.\n"
    "Then checks rx_src_net bit 7: if set, branches to\n"
    "start_data_tx to begin the data phase. Otherwise\n"
    "writes CR2=&3F (TX_LAST_DATA) and falls through to\n"
    "post_ack_scout for scout processing.")
subroutine(0x8332, "post_ack_scout",
    title="Post-ACK scout processing",
    description="Called after the scout ACK has been transmitted. Processes the\n"
    "received scout data stored in the buffer at &0D3D-&0D48.\n"
    "Checks the port byte (&0D40) against open receive blocks to\n"
    "find a matching listener. If a match is found, sets up the\n"
    "data RX handler chain for the four-way handshake data phase.\n"
    "If no match, discards the frame.")
subroutine(0x8344, "advance_rx_buffer_ptr",
    title="Advance RX buffer pointer after transfer",
    description="Adds the transfer count to the RXCB buffer pointer (4-byte\n"
    "addition). If a Tube transfer is active, re-claims the Tube\n"
    "address and sends the extra RX byte via R3, incrementing the\n"
    "Tube pointer by 1.")
subroutine(0x839A, "rx_complete_update_rxcb",
    title="Complete RX and update RXCB",
    description="Finalises a received data transfer. Calls\n"
    "advance_rx_buffer_ptr to update the 4-byte buffer\n"
    "pointer with the transfer count (and handle Tube\n"
    "re-claim if needed). Adds the buffer bytes remaining\n"
    "to the base address, then subtracts 8 from the RXCB\n"
    "buffer length to account for the scout overhead.\n"
    "Clears the RXCB flag byte and sends the final ACK\n"
    "via ack_tx. On Tube transfers, releases the Tube\n"
    "claim before resetting to idle listen.")
subroutine(0x83F8, "discard_reset_listen",
    title="Discard with Tube release",
    description="Checks whether a Tube transfer is active by\n"
    "ANDing bit 1 of l0d63 with rx_src_net (tx_flags).\n"
    "If a Tube claim is held, calls release_tube to\n"
    "free it before returning. Used as the clean-up\n"
    "path after RXCB completion and after ADLC reset\n"
    "to ensure no stale Tube claims persist.")
subroutine(0x8406, "copy_scout_to_buffer",
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
subroutine(0x843F, "release_tube",
    title="Release Tube co-processor claim",
    description="Tests need_release_tube (&98) bit 7: if set, the\n"
    "Tube has already been released and the subroutine\n"
    "just clears the flag. If clear (Tube claim held),\n"
    "calls tube_addr_data_dispatch with A=&82 to release\n"
    "the claim, then clears the release flag via LSR\n"
    "(which shifts bit 7 to 0). Called after completed\n"
    "RX transfers and during discard paths to ensure no\n"
    "stale Tube claims persist.")
subroutine(0x844B, "immediate_op",
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

label(0x847E, "imm_op_dispatch_lo")  # Immediate op dispatch lo-byte table

# Immediate operation dispatch lo-byte table (&847E-&8485)
# Indexed by ctrl byte Y=&81-&88 via LDA imm_op_dispatch_lo-&81,Y
for addr in range(0x847E, 0x8486):
    byte(addr)
expr(0x847E, "<(rx_imm_peek-1)")
expr(0x847F, "<(rx_imm_poke-1)")
expr(0x8480, "<(rx_imm_exec-1)")
expr(0x8481, "<(rx_imm_exec-1)")
expr(0x8482, "<(rx_imm_exec-1)")
expr(0x8483, "<(rx_imm_halt_cont-1)")
expr(0x8484, "<(rx_imm_halt_cont-1)")
expr(0x8485, "<(rx_imm_machine_type-1)")
comment(0x847E, "Ctrl &81: PEEK", inline=True)
comment(0x847F, "Ctrl &82: POKE", inline=True)
comment(0x8480, "Ctrl &83: JSR", inline=True)
comment(0x8481, "Ctrl &84: UserProc", inline=True)
comment(0x8482, "Ctrl &85: OSProc", inline=True)
comment(0x8483, "Ctrl &86: HALT", inline=True)
comment(0x8484, "Ctrl &87: CONTINUE", inline=True)
comment(0x8485, "Ctrl &88: machine type query", inline=True)

subroutine(0x8486, "rx_imm_exec",
    title="RX immediate: JSR/UserProc/OSProc setup",
    description="Sets up the port buffer to receive remote procedure\n"
    "data. Copies the 2-byte remote address from &0D32\n"
    "into the execution address workspace at &0D66, then\n"
    "jumps to the common receive path at c81c1. Used for\n"
    "operation types &83 (JSR), &84 (UserProc), and\n"
    "&85 (OSProc).")
subroutine(0x84A4, "rx_imm_poke",
    title="RX immediate: POKE setup",
    description="Sets up workspace offsets for receiving POKE data.\n"
    "port_ws_offset=&2E, rx_buf_offset=&0D, then jumps to\n"
    "the common data-receive path at c81af.")
subroutine(0x84AF, "rx_imm_machine_type",
    title="RX immediate: machine type query",
    description="Sets up a buffer at &88C1 (length #&01FC) for the\n"
    "machine type query response. Falls through to\n"
    "set_rx_buf_len_hi to configure buffer dimensions,\n"
    "then branches to set_tx_reply_flag.")
subroutine(0x84C1, "rx_imm_peek",
    title="RX immediate: PEEK setup",
    description="Writes &0D2E to port_ws_offset/rx_buf_offset, sets\n"
    "scout_status=2, then calls tx_calc_transfer to send\n"
    "the PEEK response data back to the requesting station.")
subroutine(0x8525, "advance_buffer_ptr",
    title="Increment 4-byte receive buffer pointer",
    description="Adds one to the counter at &A2-&A5 (port_buf_len\n"
    "low/high, open_port_buf low/high), cascading\n"
    "overflow through all four bytes. Called after each\n"
    "byte is stored during scout data copy and data\n"
    "frame reception to track the current write position\n"
    "in the receive buffer.")
subroutine(0x84EC, "imm_op_build_reply",
    title="Build immediate operation reply header",
    description="Stores data length, source station/network, and control byte\n"
    "into the RX buffer header area for port-0 immediate operations.\n"
    "Then disables CB1 interrupts and configures the VIA shift\n"
    "register for outgoing shift-out mode before returning to\n"
    "idle listen.")
subroutine(0x8539, "tx_done_jsr",
    title="TX done: remote JSR execution",
    description="Pushes address &857A on the stack (so RTS returns to\n"
    "tx_done_exit), then does JMP (l0d66) to call the remote\n"
    "JSR target routine. When that routine returns via RTS,\n"
    "control resumes at tx_done_exit.")
subroutine(0x8550, "tx_done_os_proc",
    title="TX done: OSProc call",
    description="Calls the ROM service entry point with X=l0d66,\n"
    "Y=l0d67. This invokes an OS-level procedure on\n"
    "behalf of the remote station, then exits via\n"
    "tx_done_exit.")
subroutine(0x855C, "tx_done_halt",
    title="TX done: HALT",
    description="Sets bit 2 of rx_flags (&0D61), enables interrupts,\n"
    "and spin-waits until bit 2 is cleared (by a CONTINUE\n"
    "from the remote station). If bit 2 is already set,\n"
    "skips to exit.")
subroutine(0x8573, "tx_done_continue",
    title="TX done: CONTINUE",
    description="Clears bit 2 of rx_flags (&0D61), releasing any\n"
    "station that is halted and spinning in tx_done_halt.")
subroutine(0x8582, "tx_begin",
    title="Begin TX operation",
    description="Main TX initiation entry point (called via trampoline at &06CE).\n"
    "Copies dest station/network from the TXCB to the scout buffer,\n"
    "dispatches to immediate op setup (ctrl >= &81) or normal data\n"
    "transfer, calculates transfer sizes, copies extra parameters,\n"
    "then enters the INACTIVE polling loop.")
subroutine(0x85EA, "inactive_poll",
    title="INACTIVE polling loop",
    description="Entry point for the Econet line idle detection\n"
    "loop. Saves the TX index in rx_remote_addr, pushes\n"
    "two timeout counter bytes onto the stack, and loads\n"
    "Y=&E7 (CR2 value for TX preparation). Loads the\n"
    "INACTIVE bit mask (&04) into A and falls through to\n"
    "intoff_test_inactive to begin polling SR2 with\n"
    "interrupts disabled.")
subroutine(0x85F5, "intoff_test_inactive",
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
subroutine(0x8629, "tx_line_jammed",
    title="TX timeout error handler (Line Jammed)",
    description="Reached when the INACTIVE polling loop times\n"
    "out without detecting a quiet line. Writes\n"
    "CR2=&07 (FC_TDRA|2_1_BYTE|PSE) to abort the TX\n"
    "attempt, pulls the 3-byte timeout state from the\n"
    "stack, and stores error code &40 ('Line Jammed')\n"
    "in the TX control block via store_tx_error.")
subroutine(0x8643, "tx_prepare",
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
subroutine(0x8683, "tx_ctrl_peek",
    title="TX ctrl: PEEK transfer setup",
    description="Sets scout_status=3, then performs a 4-byte addition\n"
    "of bytes from the TX block into the transfer parameter\n"
    "workspace at &0D1E-&0D21 (with carry propagation).\n"
    "Calls tx_calc_transfer to finalise, then exits via\n"
    "tx_ctrl_exit.")
subroutine(0x8687, "tx_ctrl_poke",
    title="TX ctrl: POKE transfer setup",
    description="Sets scout_status=2 and shares the 4-byte addition\n"
    "and transfer calculation path with tx_ctrl_peek.")
subroutine(0x869B, "tx_ctrl_proc",
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="Sets scout_status=2 and calls tx_calc_transfer\n"
    "directly (no 4-byte address addition needed for\n"
    "procedure calls). Shared by operation types &83-&85.")
subroutine(0x86E0, "nmi_tx_data",
    title="NMI TX data handler",
    description="Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the\n"
    "BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).\n"
    "After writing 2 bytes, checks if the frame is complete. If more data,\n"
    "tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes\n"
    "without returning from NMI (tight loop). Otherwise returns via RTI.")
subroutine(0x871C, "tx_last_data",
    title="TX_LAST_DATA and frame completion",
    description="Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs\n"
    "the TX completion NMI handler at &9D14 (nmi_tx_complete).\n"
    "CR2=&3F = 0011_1111:\n"
    "  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)\n"
    "  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte\n"
    "  bit3: FLAG_IDLE -- send flags/idle after frame\n"
    "  bit2: FC_TDRA -- force clear TDRA\n"
    "  bit1: 2_1_BYTE -- two-byte transfer mode\n"
    "  bit0: PSE -- prioritised status enable\n"
    "Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)")
subroutine(0x8728, "nmi_tx_complete",
    title="TX completion: switch to RX mode",
    description="Called via NMI after the frame (including CRC and closing flag) has been\n"
    "fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.\n"
    "CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).\n"
    "Checks workspace flags to decide next action:\n"
    "  - bit6 set at &0D4A -> tx_result_ok at &9EA8\n"
    "  - bit0 set at &0D4A -> handshake_await_ack at &9E50\n"
    "  - Otherwise -> install nmi_reply_scout at &9D30")
subroutine(0x8744, "nmi_reply_scout",
    title="RX reply scout handler",
    description="Handles reception of the reply scout frame after transmission.\n"
    "Checks SR2 bit0 (AP) for incoming data, reads the first byte\n"
    "(destination station) and compares to our station ID via &FE18\n"
    "(which also disables NMIs as a side effect).")
subroutine(0x8758, "nmi_reply_cont",
    title="RX reply continuation handler",
    description="Reads the second byte of the reply scout (destination network) and\n"
    "validates it is zero (local network). Installs nmi_reply_validate\n"
    "(&9D5B) for the remaining two bytes (source station and network).\n"
    "Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9D53.\n"
    "If IRQ is still set, falls through directly to &9D5B without an RTI,\n"
    "avoiding NMI re-entry overhead for short frames where all bytes arrive\n"
    "in quick succession.")
subroutine(0x876F, "nmi_reply_validate",
    title="RX reply validation (Path 2 for FV/PSE interaction)",
    description="Reads the source station and source network from the reply scout and\n"
    "validates them against the original TX destination (&0D20/&0D21).\n"
    "Sequence:\n"
    "  1. Check SR2 bit7 (RDA) at &9D5B -- must see data available\n"
    "  2. Read source station at &9D60, compare to &0D20 (tx_dst_stn)\n"
    "  3. Read source network at &9D68, compare to &0D21 (tx_dst_net)\n"
    "  4. Check SR2 bit1 (FV) at &9D72 -- must see frame complete\n"
    "If all checks pass, the reply scout is valid and the ROM proceeds\n"
    "to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).")
subroutine(0x87B7, "nmi_scout_ack_src",
    title="TX scout ACK: write source address",
    description="Continuation of the TX-side scout ACK. Reads our\n"
    "station ID from &FE18 (INTOFF), tests TDRA via SR1,\n"
    "and writes station + network=0 to the TX FIFO. Then\n"
    "checks bit 1 of rx_src_net to select between the\n"
    "immediate-op data NMI handler and the normal\n"
    "nmi_data_tx handler at &87E4. Installs the chosen\n"
    "handler via set_nmi_vector. Shares the tx_check_tdra\n"
    "entry at &87BD with ack_tx.")
subroutine(0x87DC, "nmi_data_tx",
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
subroutine(0x886E, "handshake_await_ack",
    title="Four-way handshake: switch to RX for final ACK",
    description="Called via JMP from nmi_tx_complete when bit 0 of\n"
    "&0D4A is set (four-way handshake in progress). Writes\n"
    "CR1=&82 (TX_RESET|RIE) to switch the ADLC from TX\n"
    "mode to RX mode, listening for the final ACK from the\n"
    "remote station. Installs the nmi_final_ack handler at\n"
    "&887A via set_nmi_vector.")
subroutine(0x887A, "nmi_final_ack",
    title="RX final ACK handler",
    description="Receives the final ACK in a four-way handshake. Same validation\n"
    "pattern as the reply scout handler (&9D30-&9D5B):\n"
    "  &9E5C: Check AP, read dest_stn, compare to our station\n"
    "  &9E70: Check RDA, read dest_net, validate = 0\n"
    "  &9E84: Check RDA, read src_stn/net, compare to TX dest\n"
    "  &9EA3: Check FV for frame completion\n"
    "On success, stores result=0 at tx_result_ok. On failure, error &41.")
subroutine(0x88A2, "nmi_final_ack_validate",
    title="Final ACK validation",
    description="Continuation of nmi_final_ack. Tests SR2 for RDA,\n"
    "then reads the source station and source network\n"
    "bytes from the RX FIFO, comparing each against the\n"
    "original TX destination at tx_dst_stn (&0D20) and\n"
    "tx_dst_net (&0D21). Finally tests SR2 bit 1 (FV)\n"
    "for frame completion. Any mismatch or missing FV\n"
    "branches to tx_result_fail. On success, falls\n"
    "through to tx_result_ok.")
subroutine(0x88C6, "tx_result_ok",
    title="TX completion handler",
    description="Loads A=0 (success) and branches unconditionally to\n"
    "tx_store_result (BEQ is always taken since A=0). This\n"
    "two-instruction entry point exists so that JMP sites\n"
    "can target the success path without needing to set A.\n"
    "Called from ack_tx (&82EC) for final-ACK completion\n"
    "and from nmi_tx_complete (&8732) for immediate-op\n"
    "completion where no ACK is expected.")
subroutine(0x88CA, "tx_result_fail",
    title="TX failure: not listening",
    description="Loads error code &41 (not listening) and falls through to\n"
    "tx_store_result. The most common TX error path — reached from\n"
    "11 sites across the final-ACK validation chain when the remote\n"
    "station doesn't respond or the frame is malformed.")
subroutine(0x88CC, "tx_store_result",
    title="TX result store and completion",
    description="Stores the TX result code (in A) at offset 0 of\n"
    "the TX control block via (nmi_tx_block),Y=0. Sets\n"
    "ws_0d60 to &80 to signal TX completion to the\n"
    "foreground polling loop. Then jumps to\n"
    "discard_reset_rx for a full ADLC reset and return\n"
    "to idle RX listen mode.",
    on_entry={"a": "result code (0=success, &40=jammed, &41=not listening)"})
subroutine(0x88E8, "tx_calc_transfer",
    title="Calculate transfer size",
    description="Computes the data transfer byte count from the\n"
    "RXCB buffer pointers. Reads the 4-byte buffer end\n"
    "address from (port_ws_offset) and checks for Tube\n"
    "addresses (&FExx/&FFxx). For Tube transfers, claims\n"
    "the Tube address and sets the transfer flag in\n"
    "rx_src_net. Subtracts the buffer start from the\n"
    "buffer end to compute the byte count, storing it in\n"
    "port_buf_len/port_buf_len_hi. Also copies the buffer\n"
    "start address to open_port_buf for the RX/TX handlers\n"
    "to use as their working pointer.")
subroutine(0x895F, "adlc_full_reset",
    title="ADLC full reset",
    description="Performs a full ADLC hardware reset. Writes\n"
    "CR1=&C1 (TX_RESET|RX_RESET|AC) to put both TX and\n"
    "RX sections in reset with address control enabled.\n"
    "Then configures CR4=&1E (8-bit RX word, abort extend,\n"
    "NRZ encoding) and CR3=&00 (no loopback, no AEX, NRZ,\n"
    "no DTR). Falls through to adlc_rx_listen to re-enter\n"
    "RX listen mode.")
subroutine(0x896E, "adlc_rx_listen",
    title="Enter RX listen mode",
    description="Configures the ADLC for passive RX listen mode.\n"
    "Writes CR1=&82 (TX_RESET|RIE): TX section held in\n"
    "reset, RX interrupts enabled. Writes CR2=&67\n"
    "(CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE) to clear\n"
    "all pending status and enable prioritised status.\n"
    "This is the idle state where the ADLC listens for\n"
    "incoming scout frames via NMI.")
subroutine(0x8979, "wait_idle_and_reset",
    title="Wait for idle NMI state and reset Econet",
    description="Service 12 handler: NMI release. Checks ws_0d62\n"
    "to see if Econet has been initialised; if not, skips\n"
    "straight to adlc_rx_listen. Otherwise spins in a\n"
    "tight loop comparing the NMI handler vector at\n"
    "&0D0C/&0D0D against the address of nmi_rx_scout\n"
    "(&80B3). When the NMI handler returns to idle, falls\n"
    "through to save_econet_state to clear the initialised\n"
    "flags and re-enter RX listen mode.")
subroutine(0x898C, "save_econet_state",
    title="Reset Econet flags and enter RX listen",
    description="Disables NMIs via two reads of &FE18 (INTOFF),\n"
    "then clears ws_0d60 (TX complete) and ws_0d62\n"
    "(Econet initialised) by storing the current A value.\n"
    "Sets Y=5 (service call workspace page) and jumps to\n"
    "adlc_rx_listen to configure the ADLC for passive\n"
    "listening. Used during NMI release (service 12) to\n"
    "safely tear down the Econet state before another\n"
    "ROM can claim the NMI workspace.")
subroutine(0x899D, "nmi_bootstrap_entry",
    title="Bootstrap NMI entry point (in ROM)",
    description="An alternate NMI handler that lives in the ROM itself rather than\n"
    "in the RAM workspace at &0D00. Unlike the RAM shim (which uses a\n"
    "self-modifying JMP to dispatch to different handlers), this one\n"
    "hardcodes JMP nmi_rx_scout (&96BF). Used as the initial NMI handler\n"
    "before the workspace has been properly set up during initialisation.\n"
    "Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,\n"
    "LDA romsel, STA &FE30, JMP &96BF.")
subroutine(0x89AB, "rom_set_nmi_vector",
    title="ROM copy of set_nmi_vector + nmi_rti",
    description="A version of the NMI vector-setting subroutine and RTI sequence\n"
    "that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the\n"
    "one normally used at runtime; this ROM copy is used during early\n"
    "initialisation before the RAM workspace has been set up, and as\n"
    "the source for the initial copy to RAM.")
subroutine(0x8AE2, "scan_remote_keys",
    title="Scan keyboard for remote operation keys",
    description="Uses OSBYTE &7A with Y=&7F to check whether\n"
    "remote operation keys (&CE-&CF) are currently\n"
    "pressed. If neither key is detected, clears\n"
    "svc_state and nfs_workspace to zero via the\n"
    "clear_svc_and_ws entry point, which is also used\n"
    "directly by cmd_roff. Called by check_escape.")
subroutine(0x8AFA, "save_text_ptr",
    title="Save OS text pointer for later retrieval",
    description="Copies &F2/&F3 into fs_crc_lo/fs_crc_hi. Called by\n"
    "svc_4_star_command and svc_9_help before attempting\n"
    "command matches, and by match_fs_cmd during\n"
    "iterative help topic matching. Preserves A via\n"
    "PHA/PLA.",
    on_exit={"a": "preserved"})
subroutine(0x8B8D, "print_cmd_table",
    title="Print *HELP command listing with optional header",
    description="If V flag is set, saves X/Y, calls\n"
    "print_version_header to show the ROM version\n"
    "string and station number, then restores X/Y.\n"
    "If V flag is clear, outputs a newline only.\n"
    "Either path then falls through to\n"
    "print_cmd_table_loop to enumerate commands.",
    on_entry={"x": "offset into cmd_table_fs",
              "v": "set=print version header, clear=newline only"})
subroutine(0x8BA0, "print_cmd_table_loop",
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
subroutine(0x8C28, "help_wrap_if_serial",
    title="Wrap *HELP syntax lines for serial output",
    description="Checks the output destination via &0355. Returns\n"
    "immediately for VDU (stream 0) or printer\n"
    "(stream 3) output. For serial streams, outputs a\n"
    "newline followed by 12 spaces of indentation to\n"
    "align continuation lines with the syntax\n"
    "description column.",
    on_exit={"y": "preserved"})
subroutine(0x8C94, "print_version_header",
    title="Print ANFS version string and station number",
    description="Uses an inline string after JSR print_inline:\n"
    "CR + \"Advanced  4.08.53\" + CR. After the inline\n"
    "string, JMPs to print_station_id to append the\n"
    "local Econet station number.")
subroutine(0x8CAE, "get_ws_page",
    title="Read workspace page number for current ROM slot",
    description="Indexes into the MOS per-ROM workspace table at\n"
    "&0DF0 using romsel_copy (&F4) as the ROM slot.\n"
    "Returns the allocated page number in both A and Y\n"
    "for caller convenience.",
    on_exit={"a": "workspace page number",
             "y": "workspace page number (same as A)"})
subroutine(0x8CB5, "setup_ws_ptr",
    title="Set up zero-page pointer to workspace page",
    description="Calls get_ws_page to read the page number, stores\n"
    "it as the high byte in nfs_temp (&CD), and clears\n"
    "the low byte at &CC to zero. This gives a\n"
    "page-aligned pointer used by FS initialisation and\n"
    "cmd_net_fs to access the private workspace.",
    on_exit={"a": "0", "y": "workspace page number"})
subroutine(0x8CF1, "notify_new_fs",
    title="Notify OS of filing system selection",
    description="Calls FSCV with A=6 to announce the FS change,\n"
    "then issues paged ROM service call 10 via OSBYTE\n"
    "&8F to inform other ROMs. Sets X=&0A and branches\n"
    "to issue_svc_osbyte which falls through from the\n"
    "call_fscv subroutine.")
subroutine(0x8CFA, "call_fscv",
    title="Dispatch to filing system control vector (FSCV)",
    description="Indirect JMP through FSCV at &021E, providing\n"
    "OS-level filing system services such as FS\n"
    "selection notification (A=6) and *RUN handling.\n"
    "Also contains issue_svc_15 and issue_svc_osbyte\n"
    "entry points that issue paged ROM service requests\n"
    "via OSBYTE &8F.",
    on_entry={"a": "FSCV reason code"})
subroutine(0x8D0C, "check_credits_easter_egg",
    title="Easter egg: match *HELP keyword to author credits",
    description="Matches the *HELP argument against a keyword\n"
    "embedded in the credits data at\n"
    "credits_keyword_start. Starts matching from offset\n"
    "5 in the data (X=5) and checks each byte against\n"
    "the command line text until a mismatch or X reaches\n"
    "&0D. On a full match, prints the ANFS author\n"
    "credits string: B Cockburn, J Dunn, B Robertson,\n"
    "and J Wills, each terminated by CR.")
subroutine(0x8DFE, "clear_if_station_match",
    title="Clear stored station if parsed argument matches",
    description="Parses a station number from the command line via\n"
    "init_bridge_poll and compares it with the expected\n"
    "station at &0E01 using EOR. If the parsed value\n"
    "matches (EOR result is zero), clears &0E01. Called\n"
    "by cmd_iam when processing a file server address\n"
    "in the logon command.",
    on_exit={"a": "0 if matched, non-zero if different"})
subroutine(0x8E76, "osbyte_x0_y0",
    title="OSBYTE wrapper with X=0, Y=0",
    description="Sets X=0 and Y=0 then branches to jmp_osbyte.\n"
    "Called from the Econet OSBYTE dispatch chain to\n"
    "handle OSBYTEs that require both X and Y cleared.\n"
    "The unconditional BEQ (after LDY #0 sets Z)\n"
    "reaches the JMP osbyte instruction at &8E71.",
    on_entry={"a": "OSBYTE number"},
    on_exit={"x": "0", "y": "0"})
subroutine(0x8E96, "store_ws_page_count",
    title="Record workspace page count (capped at &21)",
    description="Stores the workspace allocation from service 1\n"
    "into offset &0F of the receive control block,\n"
    "capping the value at &21 to prevent overflow into\n"
    "adjacent workspace areas. Called by\n"
    "svc_2_private_workspace after issuing the absolute\n"
    "workspace claim service call.",
    on_entry={"y": "workspace page count from service 1"})
subroutine(0x8F40, "init_adlc_and_vectors",
    title="Initialise ADLC and install extended vectors",
    description="Reads the ROM pointer table via OSBYTE &A8,\n"
    "writes vector addresses and ROM ID into the\n"
    "extended vector table for NETV and one additional\n"
    "vector, then restores any previous FS context.")
subroutine(0x8F53, "write_vector_entry",
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
subroutine(0x8F73, "restore_fs_context",
    title="Restore FS context from saved workspace",
    description="Copies 8 bytes (offsets 6 to &0D) from the saved\n"
    "workspace at &0DFA back into the receive control\n"
    "block via (net_rx_ptr). This restores the station\n"
    "identity, directory handles, and library path after\n"
    "a filing system reselection. Called by\n"
    "svc_2_private_workspace during init,\n"
    "deselect_fs_if_active during FS teardown, and\n"
    "flip_set_station_boot.")
subroutine(0x8F80, "fscv_6_shutdown",
    title="Deselect filing system and save workspace",
    description="If the filing system is currently selected\n"
    "(bit 7 of &0D6C set), closes all open FCBs,\n"
    "closes SPOOL/EXEC files via OSBYTE &77,\n"
    "saves the FS workspace to page &10 shadow\n"
    "with checksum, and clears the selected flag.")
subroutine(0x8FB2, "verify_ws_checksum",
    title="Verify workspace checksum integrity",
    description="Sums bytes 0 to &76 of the workspace page via the\n"
    "zero-page pointer at &CC/&CD and compares with the\n"
    "stored value at offset &77. On mismatch, raises a\n"
    "'net checksum' error via error_bad_inline.\n"
    "Preserves A, Y, and processor flags using PHP/PHA.\n"
    "Called by 5 sites across format_filename_field,\n"
    "adjust_fsopts_4bytes, and start_wipe_pass before\n"
    "workspace access.",
    on_exit={"a": "preserved", "y": "preserved"})
subroutine(0x8FDD, "print_station_id",
    title="Print Econet station number and clock status",
    description="Uses print_inline to output 'Econet Station ',\n"
    "then reads the station ID from offset 5 of the\n"
    "receive control block and prints it as a decimal\n"
    "number via print_num_no_leading. Tests ADLC\n"
    "status register 2 (&FEA1) to detect the Econet\n"
    "clock; if absent, appends ' No Clock' via a\n"
    "second inline string. Finishes with OSNEWL.\n"
    "Called by print_version_header and svc_3_auto_boot.")
subroutine(0x911B, "print_hex_byte",
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
subroutine(0x9124, "print_hex_nybble",
    title="Print low nybble of A as hex digit",
    description="Masks A to the low 4 bits, then converts to\n"
    "ASCII: adds 7 for letters A-F (via ADC #6 with\n"
    "carry set from the CMP), then ADC #&30 for the\n"
    "final '0'-'F' character. Outputs via JMP OSASCI.",
    on_entry={"a": "value (low nybble used)"})
subroutine(0x915A, "parse_addr_arg",
    title="Parse decimal or hex station address argument",
    description="Reads from the command argument at (&BE),Y.\n"
    "Supports '&' prefix for hex, '.' separator for\n"
    "net.station addresses, and plain decimal.\n"
    "Returns result in A. Raises errors for\n"
    "bad digits, overflow, or zero values.")
subroutine(0x9244, "is_decimal_digit",
    title="Test for digit, '&', or '.' separator",
    description="Compares A against '&' and '.' first; if\n"
    "either matches, returns with carry set via the\n"
    "shared return_12 exit. Otherwise falls through\n"
    "to is_dec_digit_only for the '0'-'9' range\n"
    "test. Called by cmd_iam, cmd_ps, and\n"
    "cmd_pollps when parsing station addresses.",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if digit/&/., clear otherwise"})
subroutine(0x924C, "is_dec_digit_only",
    title="Test for decimal digit '0'-'9'",
    description="Uses two CMPs to bracket-test A against the\n"
    "range &30-&39. CMP #&3A sets carry if A >= ':'\n"
    "(above digits), then CMP #&30 sets carry if\n"
    "A >= '0'. The net effect: carry set only for\n"
    "'0'-'9'. Called by parse_addr_arg.",
    on_entry={"a": "character to test"},
    on_exit={"c": "set if '0'-'9', clear otherwise"})
subroutine(0x9255, "get_access_bits",
    title="Read and encode directory entry access byte",
    description="Loads the access byte from offset &0E of the\n"
    "directory entry via (fs_options),Y, masks to 6\n"
    "bits (AND #&3F), then sets X=4 and branches to\n"
    "begin_prot_encode to map through the protection\n"
    "bit encode table at &9272. Called by\n"
    "check_and_setup_txcb for owner and public access.",
    on_exit={"a": "encoded access flags"})
subroutine(0x925F, "get_prot_bits",
    title="Encode protection bits via lookup table",
    description="Masks A to 5 bits (AND #&1F), sets X=&FF to\n"
    "start at table index 0, then enters the shared\n"
    "encoding loop at begin_prot_encode. Shifts out\n"
    "each source bit and ORs in the corresponding\n"
    "value from prot_bit_encode_table (&9272). Called\n"
    "by send_txcb_swap_addrs and check_and_setup_txcb.",
    on_entry={"a": "raw protection bits (low 5 used)"},
    on_exit={"a": "encoded protection flags"})
subroutine(0x927D, "set_text_and_xfer_ptr",
    title="Set OS text pointer then transfer parameters",
    description="Stores X/Y into the MOS text pointer at\n"
    "&F2/&F3, then falls through to set_xfer_params\n"
    "and set_options_ptr to configure the full FS\n"
    "transfer context. Called by byte_to_2bit_index.",
    on_entry={"x": "text pointer low byte",
              "y": "text pointer high byte"})
subroutine(0x9281, "set_xfer_params",
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
subroutine(0x9287, "set_options_ptr",
    title="Set FS options pointer and clear escape flag",
    description="Stores X/Y into fs_options/fs_block_offset\n"
    "(&BB/&BC) as the options block pointer. Then\n"
    "enters clear_escapable which uses PHP/LSR/PLP\n"
    "to clear bit 0 of the escape flag at &97 without\n"
    "disturbing processor flags. Called by\n"
    "format_filename_field and send_and_receive.",
    on_entry={"x": "options pointer low",
              "y": "options pointer high"})
subroutine(0x9290, "cmp_5byte_handle",
    title="Compare 5-byte handle buffers for equality",
    description="Loops X from 4 down to 1, comparing each byte\n"
    "of l00af+X with fs_load_addr_3+X using EOR.\n"
    "Returns on the first mismatch (Z=0) or after\n"
    "all 5 bytes match (Z=1). Called by\n"
    "send_txcb_swap_addrs and check_and_setup_txcb\n"
    "to verify station/handle identity.",
    on_exit={"z": "set if all 5 bytes match"})
subroutine(0x92A1, "set_conn_active",
    title="Set connection-active flag in channel table",
    description="Saves registers on the stack, recovers the\n"
    "original A from the stack via TSX/LDA &0102,X,\n"
    "then calls attr_to_chan_index to find the channel\n"
    "slot. ORs bit 6 (&40) into the channel status\n"
    "byte at &1060+X. Preserves A, X, and processor\n"
    "flags via PHP/PHA/PLA/PLP. Called by\n"
    "format_filename_field and adjust_fsopts_4bytes.",
    on_entry={"a": "channel attribute byte"})
subroutine(0x92B8, "clear_conn_active",
    title="Clear connection-active flag in channel table",
    description="Mirror of set_conn_active but ANDs the channel\n"
    "status byte with &BF (bit 6 clear mask) instead\n"
    "of ORing. Uses the same register-preservation\n"
    "pattern: PHP/PHA/TSX to recover A, then\n"
    "attr_to_chan_index to find the slot. Shares the\n"
    "done_conn_flag exit with set_conn_active.",
    on_entry={"a": "channel attribute byte"})
subroutine(0x92F5, "check_not_ampersand",
    title="Reject '&' as filename character",
    description="Loads the first character from the parse buffer\n"
    "at &0E30 and compares with '&' (&26). Branches\n"
    "to error_bad_filename if matched, otherwise\n"
    "returns. Also contains read_filename_char which\n"
    "loops reading characters from the command line\n"
    "into the TX buffer at &0F05, calling\n"
    "strip_token_prefix on each byte and terminating\n"
    "on CR. Used by cmd_fs_operation and cmd_rename.")
subroutine(0x9313, "copy_fs_cmd_name",
    title="Copy matched command name to TX buffer",
    description="Scans backwards in cmd_table_fs from the\n"
    "current position to find the bit-7 flag byte\n"
    "marking the start of the command name. Copies\n"
    "each character forward into the TX buffer at\n"
    "&0F05 until the next bit-7 byte (end of name),\n"
    "then appends a space separator. Called by\n"
    "cmd_fs_operation and cmd_rename.",
    on_exit={"x": "TX buffer offset past name+space",
             "y": "command line offset (restored)"})
subroutine(0x9335, "parse_quoted_arg",
    title="Parse possibly-quoted filename argument",
    description="Reads from the command line at (&BE),Y. Handles\n"
    "double-quote delimiters and stores the result\n"
    "in the parse buffer at &0E30. Raises 'Bad string'\n"
    "on unbalanced quotes.")
subroutine(0x9451, "init_txcb_bye",
    title="Initialise TXCB for bye/receive on port &90",
    description="Loads A=&90 (the FS command port) and falls\n"
    "through to init_txcb_port, which initialises\n"
    "the TXCB from the template, sets the port,\n"
    "data start offset to 3, and decrements the\n"
    "control byte. Called by recv_and_process_reply.")
subroutine(0x9453, "init_txcb_port",
    title="Initialise TXCB with specified port number",
    description="Calls init_txcb to copy the 12-byte template\n"
    "into the TXCB workspace at &00C0, then stores A\n"
    "as the transmit port (txcb_port at &C1), sets\n"
    "txcb_start to 3 (data begins at offset 3 in the\n"
    "packet), and decrements txcb_ctrl. Called by\n"
    "check_and_setup_txcb.",
    on_entry={"a": "port number"})
subroutine(0x945F, "init_txcb",
    title="Initialise TX control block from ROM template",
    description="Copies 12 bytes from txcb_init_template (&9477)\n"
    "into the TXCB workspace at &00C0. For the first\n"
    "two bytes (Y=0,1), also copies the destination\n"
    "station/network from &0E00 into txcb_dest (&C2).\n"
    "Preserves A via PHA/PLA. Called by 4 sites\n"
    "including cmd_pass, init_txcb_port,\n"
    "prep_send_tx_cb, and send_wipe_request.")
subroutine(0x9483, "send_request_nowrite",
    title="Send read-only FS request (carry set)",
    description="Pushes A and sets carry to indicate no-write\n"
    "mode, then branches to txcb_copy_carry_set to\n"
    "enter the common TXCB copy, send, and reply\n"
    "processing path. The carry flag controls whether\n"
    "a disconnect is sent on certain reply codes.\n"
    "Called by setup_transfer_workspace.")
subroutine(0x9487, "send_request_write",
    title="Send read-write FS request (V clear)",
    description="Clears V flag and branches unconditionally to\n"
    "txcb_copy_carry_clr (via BVC, always taken after\n"
    "CLV) to enter the common TXCB copy, send, and\n"
    "reply processing path with carry clear (write\n"
    "mode). Called by do_fs_cmd_iteration and\n"
    "send_txcb_swap_addrs.")
subroutine(0x9499, "save_net_tx_cb",
    title="Save FS state and send command to file server",
    description="Copies station address and function code (Y)\n"
    "to the TX buffer, builds the TXCB, sends the\n"
    "packet, and waits for the reply. V is clear\n"
    "for standard mode.")
subroutine(0x949A, "save_net_tx_cb_vset",
    title="Save and send TXCB with V flag set",
    description="Variant of save_net_tx_cb for callers that have\n"
    "already set V. Copies the FS station address\n"
    "from &0E02 to &0F02, then falls through to\n"
    "txcb_copy_carry_clr which clears carry and enters\n"
    "the common TXCB copy, send, and reply path.\n"
    "Called by check_and_setup_txcb,\n"
    "format_filename_field, and cmd_remove.")
subroutine(0x94C6, "prep_send_tx_cb",
    title="Build TXCB from scratch, send, and receive reply",
    description="Full send/receive cycle: saves flags, sets\n"
    "reply port &90, calls init_txcb to load the\n"
    "template, computes txcb_end from X+5, then\n"
    "dispatches based on carry: C set sends a\n"
    "disconnect via handle_disconnect, C clear calls\n"
    "init_tx_ptr_and_send and falls through to\n"
    "recv_and_process_reply. Called by\n"
    "setup_transfer_workspace.")
subroutine(0x94DC, "recv_and_process_reply",
    title="Receive FS reply and dispatch on status codes",
    description="Calls init_txcb_bye to set up a receive TXCB\n"
    "on port &90, then wait_net_tx_ack to wait for\n"
    "the acknowledgment. Iterates over reply bytes:\n"
    "zero terminates, V-set codes are adjusted by\n"
    "+&2B, and non-zero codes dispatch to\n"
    "store_reply_status. Handles disconnect requests\n"
    "(C set from prep_send_tx_cb) and 'Data Lost'\n"
    "warnings when channel status bits indicate\n"
    "pending writes were interrupted.")
subroutine(0x955A, "check_escape",
    title="Check for pending escape condition",
    description="ANDs the MOS escape flag (&FF) with the\n"
    "escapable flag at &97. If bit 7 of the result\n"
    "is clear (no escape or escape disabled), returns\n"
    "immediately. Otherwise enters raise_escape_error:\n"
    "acknowledges the escape via OSBYTE &7E, then\n"
    "jumps to classify_reply_error with A=6 to raise\n"
    "the Escape error. Called by cmd_pass and\n"
    "send_net_packet.")
subroutine(0x95C7, "wait_net_tx_ack",
    title="Wait for Econet TX completion with timeout",
    description="Saves the timeout counter from &0D6F and the\n"
    "TX control state from &0D61, then polls\n"
    "net_tx_ptr_hi (&9B) for completion. Uses a\n"
    "three-level nested loop: the outer counter\n"
    "comes from the configured timeout at &0D6F.\n"
    "On completion, restores both saved values.\n"
    "On timeout (all loops exhausted), branches to\n"
    "build_no_reply_error to raise 'No reply'.\n"
    "Called by 6 sites across the protocol stack.")
subroutine(0x95FB, "cond_save_error_code",
    title="Conditionally store error code to workspace",
    description="Tests bit 7 of &0D6C (FS selected flag). If\n"
    "clear, returns immediately. If set, stores A\n"
    "into &0E09 as the last error code. This guards\n"
    "against writing error state when no filing system\n"
    "is active. Called internally by the error\n"
    "classification chain and by error_inline_log.",
    on_entry={"a": "error code to store"})
subroutine(0x9738, "append_drv_dot_num",
    title="Append 'net.station' decimal string to error text",
    description="Reads network and station numbers from the TX\n"
    "control block at offsets 3 and 2. Writes a space\n"
    "separator then the network number (if non-zero),\n"
    "a dot, and the station number as decimal digits\n"
    "into the error text buffer at the current position.",
    on_entry={"x": "error text buffer index"},
    on_exit={"x": "updated buffer index past appended text"})
subroutine(0x975C, "append_space_and_num",
    title="Append space and decimal number to error text",
    description="Writes a space character to the error text buffer\n"
    "at the current position (fs_load_addr_2), then falls\n"
    "through to append_decimal_num to convert the value\n"
    "in A to decimal digits with leading zero suppression.",
    on_entry={"a": "number to append (0-255)"})
subroutine(0x9767, "append_decimal_num",
    title="Convert byte to decimal and append to error text",
    description="Extracts hundreds, tens and units digits by three\n"
    "successive calls to append_decimal_digit. Uses the\n"
    "V flag to suppress leading zeros — hundreds and tens\n"
    "are skipped when zero, but the units digit is always\n"
    "emitted.",
    on_entry={"a": "number to convert (0-255)"})
subroutine(0x9778, "append_decimal_digit",
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
subroutine(0x9822, "init_tx_ptr_and_send",
    title="Point TX at zero-page TXCB and send",
    description="Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the\n"
    "standard TXCB location in zero page), then falls\n"
    "through to send_net_packet for transmission with\n"
    "retry logic.")
subroutine(0x982A, "send_net_packet",
    title="Transmit Econet packet with retry",
    description="Polls for line idle, starts transmission via\n"
    "the ADLC, and retries on failure with a\n"
    "configurable count and delay. Enables escape\n"
    "handling after the first retry phase exhausts\n"
    "its count.")
subroutine(0x987F, "init_tx_ptr_for_pass",
    title="Set up TX pointer and send pass-through packet",
    description="Copies the template into the TX buffer (skipping\n"
    "&FD markers), saves original values on stack,\n"
    "then polls the ADLC and retries until complete.")
subroutine(0x9887, "setup_pass_txbuf",
    title="Initialise TX buffer from pass-through template",
    description="Copies 12 bytes from pass_txbuf_init_table into the\n"
    "TX control block, pushing the original values on the\n"
    "stack for later restoration. Skips offsets marked &FD\n"
    "in the template. Starts transmission via\n"
    "poll_adlc_tx_status and retries on failure, restoring\n"
    "the original TX buffer contents when done.")
subroutine(0x98B4, "poll_adlc_tx_status",
    title="Poll ADLC and start frame transmission",
    description="Shifts the workspace status byte left in a\n"
    "loop, then copies the TX pointer into the NMI\n"
    "TX block and calls tx_begin to start frame\n"
    "transmission. Returns the TX completion status\n"
    "in A.")
subroutine(0x98F3, "load_text_ptr_and_parse",
    title="Copy text pointer from FS options and parse string",
    description="Reads a 2-byte address from (fs_options)+0/1 into\n"
    "os_text_ptr (&00F2), resets Y to zero, then falls\n"
    "through to gsread_to_buf to parse the string at that\n"
    "address into the &0E30 buffer.")
subroutine(0x98FF, "gsread_to_buf",
    title="Parse command line via GSINIT/GSREAD into &0E30",
    description="Calls GSINIT to initialise string reading, then\n"
    "loops calling GSREAD to copy characters into the\n"
    "l0e30 buffer until end-of-string. Appends a CR\n"
    "terminator and sets fs_crc_lo/hi to point at &0E30\n"
    "for subsequent parsing routines.")
subroutine(0x993D, "do_fs_cmd_iteration",
    title="Execute one iteration of a multi-step FS command",
    description="Called by match_fs_cmd for commands that enumerate\n"
    "directory entries. Sets port &92, sends the initial\n"
    "request via send_request_write, then synchronises the\n"
    "FS options and workspace state (order depends on the\n"
    "cycle flag at offset 6). Copies 4 address bytes,\n"
    "formats the filename field, sends via\n"
    "send_txcb_swap_addrs, and receives the reply.")
subroutine(0x9984, "send_txcb_swap_addrs",
    title="Send TXCB and swap start/end addresses",
    description="If the 5-byte handle matches, returns\n"
    "immediately. Otherwise sets port &92, copies\n"
    "addresses, sends, waits for acknowledgment,\n"
    "and retries on address mismatch.")
subroutine(0x9A45, "print_load_exec_addrs",
    title="Print exec address and file length in hex",
    description="Prints the exec address as 5 hex bytes from\n"
    "(fs_options) offset 9 downwards, then the file\n"
    "length as 3 hex bytes from offset &0C. Each group\n"
    "is followed by a space separator via OSASCI.")
subroutine(0x9A50, "print_5_hex_bytes",
    title="Print hex byte sequence from FS options",
    description="Outputs X+1 bytes from (fs_options) starting at\n"
    "offset Y, decrementing Y for each byte (big-endian\n"
    "display order). Each byte is printed as two hex\n"
    "digits via print_hex_byte. Finishes with a trailing\n"
    "space via OSASCI. The default entry with X=4 prints\n"
    "5 bytes (a full 32-bit address plus extent).",
    on_entry={"x": "byte count minus 1 (default 4 for 5 bytes)",
              "y": "starting offset in (fs_options)"})
subroutine(0x9A60, "copy_fsopts_to_zp",
    title="Copy FS options address bytes to zero page",
    description="Copies 4 bytes from (fs_options) at offsets 2-5\n"
    "into zero page at &00AE+Y. Used by\n"
    "do_fs_cmd_iteration to preserve the current address\n"
    "state. Falls through to skip_one_and_advance5 to\n"
    "advance Y past the copied region.")
subroutine(0x9A6C, "skip_one_and_advance5",
    title="Advance Y by 5",
    description="Entry point one INY before advance_y_by_4, giving\n"
    "a total Y increment of 5. Used to skip past a\n"
    "5-byte address/length structure in the FS options\n"
    "block.")
subroutine(0x9A6D, "advance_y_by_4",
    title="Advance Y by 4",
    description="Four consecutive INY instructions. Used as a\n"
    "subroutine to step Y past a 4-byte address field\n"
    "in the FS options or workspace structure.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset + 4"})
subroutine(0x9A72, "copy_workspace_to_fsopts",
    title="Copy workspace reply data to FS options",
    description="Copies bytes from the reply buffer at &0F02+Y\n"
    "into (fs_options) at offsets &0D down to 2. Used\n"
    "to update the FS options block with data returned\n"
    "from the file server. Falls through to\n"
    "retreat_y_by_4.")
subroutine(0x9A7F, "retreat_y_by_4",
    title="Retreat Y by 4",
    description="Four consecutive DEY instructions. Companion to\n"
    "advance_y_by_4 for reverse traversal of address\n"
    "structures.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 4"})
subroutine(0x9A80, "retreat_y_by_3",
    title="Retreat Y by 3",
    description="Three consecutive DEY instructions. Used by\n"
    "setup_transfer_workspace to step back through\n"
    "interleaved address pairs in the FS options block.",
    on_entry={"y": "current offset"},
    on_exit={"y": "offset - 3"})
subroutine(0x9A88, "check_and_setup_txcb",
    title="Set up data transfer TXCB and dispatch reply",
    description="Compares the 5-byte handle; if unchanged,\n"
    "returns. Otherwise computes start/end addresses\n"
    "with overflow clamping, sets the port and control\n"
    "byte, sends the packet, and dispatches on the\n"
    "reply sub-operation code.")
subroutine(0x9B86, "format_filename_field",
    title="Format filename into fixed-width display field",
    description="Builds a 12-character space-padded filename at\n"
    "&10F3 for directory listing output. Sources the\n"
    "name from either the command line or the l0f05\n"
    "reply buffer depending on the value in l0f03.\n"
    "Truncates or pads to exactly 12 characters.")
subroutine(0x9E03, "update_addr_from_offset9",
    title="Update both address fields in FS options",
    description="Calls add_workspace_to_fsopts for offset 9 (the\n"
    "high address / exec address field), then falls\n"
    "through to update_addr_from_offset1 to process\n"
    "offset 1 (the low address / load address field).")
subroutine(0x9E08, "update_addr_from_offset1",
    title="Update low address field in FS options",
    description="Sets Y=1 and falls through to\n"
    "add_workspace_to_fsopts to add the workspace\n"
    "adjustment bytes to the load address field at\n"
    "offset 1 in the FS options block.",
    on_entry={"c": "carry state passed to add_workspace_to_fsopts"})
subroutine(0x9E0A, "add_workspace_to_fsopts",
    title="Add workspace bytes to FS options with clear carry",
    description="Clears carry and falls through to\n"
    "adjust_fsopts_4bytes. Provides a convenient entry\n"
    "point when the caller needs addition without a\n"
    "preset carry.",
    on_entry={"y": "FS options offset for first byte"})
subroutine(0x9E0B, "adjust_fsopts_4bytes",
    title="Add or subtract 4 workspace bytes from FS options",
    description="Processes 4 consecutive bytes at (fs_options)+Y,\n"
    "adding or subtracting the corresponding workspace\n"
    "bytes from &0E0A-&0E0D. The direction is controlled\n"
    "by bit 7 of fs_load_addr_2: set for subtraction,\n"
    "clear for addition. Carry propagates across all 4\n"
    "bytes for correct multi-byte arithmetic.",
    on_entry={"y": "FS options offset for first byte",
              "c": "carry input for first byte"})
subroutine(0x9EC0, "lookup_cat_entry_0",
    title="Look up channel from FS options offset 0",
    description="Loads the channel handle from (fs_options) at\n"
    "offset 0, then falls through to lookup_cat_slot_data\n"
    "to find the corresponding FCB entry.",
    on_exit={"a": "FCB flag byte from &1030+X",
             "x": "channel slot index"})
subroutine(0x9EC4, "lookup_cat_slot_data",
    title="Look up channel and return FCB flag byte",
    description="Calls lookup_chan_by_char to find the channel\n"
    "slot for handle A in the channel table, then\n"
    "loads the FCB flag byte from &1030+X.",
    on_entry={"a": "channel handle"},
    on_exit={"a": "FCB flag byte",
             "x": "channel slot index"})
subroutine(0x9ECB, "setup_transfer_workspace",
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
subroutine(0x9FB8, "write_data_block",
    title="Write data block to destination or Tube",
    description="If no Tube present, copies directly from\n"
    "the l0f05 buffer via (fs_crc_lo). If Tube\n"
    "is active, claims the Tube, sets up the\n"
    "transfer address, and writes via R3.")
subroutine(0xA05B, "tube_claim_c3",
    title="Claim the Tube via protocol &C3",
    description="Loops calling tube_addr_data_dispatch with\n"
    "protocol byte &C3 until the claim succeeds\n"
    "(carry set on return). Used before Tube data\n"
    "transfers to ensure exclusive access to the\n"
    "Tube co-processor interface.")
subroutine(0xA086, "print_fs_info_newline",
    title="Print station address and newline",
    description="Sets V (suppressing leading-zero padding on\n"
    "the network number) then prints the station\n"
    "address followed by a newline via OSNEWL.\n"
    "Used by *FS and *PS output formatting.")
subroutine(0xA08F, "parse_fs_ps_args",
    title="Parse station address from *FS/*PS arguments",
    description="Reads a station address in 'net.station' format\n"
    "from the command line, with the network number\n"
    "optional (defaults to local network). Calls\n"
    "init_bridge_poll to ensure the bridge routing\n"
    "table is populated, then validates the parsed\n"
    "address against known stations.")
subroutine(0xA0B4, "get_pb_ptr_as_index",
    title="Convert parameter block pointer to table index",
    description="Reads the first byte from the OSWORD parameter\n"
    "block pointer and falls through to\n"
    "byte_to_2bit_index to produce a 12-byte-aligned\n"
    "table index in Y.")
subroutine(0xA0B6, "byte_to_2bit_index",
    title="Convert byte to 12-byte-aligned table index",
    description="Computes Y = A * 6 (via A*12/2) for indexing\n"
    "into the OSWORD handler workspace tables.\n"
    "Clamps Y to zero if the result exceeds &48,\n"
    "preventing out-of-bounds access.",
    on_entry={"a": "table entry number"},
    on_exit={"y": "byte offset (0, 6, 12, ... up to &42)"})
subroutine(0xA128, "match_fs_cmd",
    title="Match command name against FS command table",
    description="Case-insensitive compare of the command line\n"
    "against table entries with bit-7-terminated\n"
    "names. Returns with the matched entry address\n"
    "on success.")
subroutine(0xA2E8, "find_station_bit2",
    title="Find printer server station in table (bit 2)",
    description="Scans the 16-entry station table for a slot\n"
    "matching the current station/network address\n"
    "with bit 2 set (printer server active). Sets V\n"
    "if found, clears V if not. Falls through to\n"
    "allocate or update the matching slot with the\n"
    "new station address and status flags.")
subroutine(0xA313, "find_station_bit3",
    title="Find file server station in table (bit 3)",
    description="Scans the 16-entry station table for a slot\n"
    "matching the current station/network address\n"
    "with bit 3 set (file server active). Sets V\n"
    "if found, clears V if not. Falls through to\n"
    "allocate or update the matching slot with the\n"
    "new station address and status flags.")
subroutine(0xA34A, "flip_set_station_boot",
    title="Set boot option for a station in the table",
    description="Scans up to 16 station table entries for one\n"
    "matching the current address with bit 4 set\n"
    "(boot-eligible). Stores the requested boot type\n"
    "in the matching entry and calls\n"
    "restore_fs_context to re-establish the filing\n"
    "system state.")
subroutine(0xA4EF, "osword_setup_handler",
    title="Push OSWORD handler address for RTS dispatch",
    description="Indexes the OSWORD dispatch table by X to\n"
    "push a handler address (hi then lo) onto the\n"
    "stack. Copies 3 bytes from the osword_flag\n"
    "workspace into the RX buffer, loads PB byte 0\n"
    "(the OSWORD sub-code), and clears svc_state.\n"
    "The subsequent RTS dispatches to the pushed\n"
    "handler address.",
    on_entry={"x": "OSWORD handler index (0-6)"})
subroutine(0xA57C, "bin_to_bcd",
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
subroutine(0xA601, "store_osword_pb_ptr",
    title="Store OSWORD parameter block pointer+1 to workspace",
    description="Computes PB pointer + 1 and stores the resulting\n"
    "16-bit address at workspace offset &1C via\n"
    "store_ptr_at_ws_y. Then reads PB byte 1 (the\n"
    "transfer length) and adds the PB low byte to\n"
    "compute the buffer end pointer, stored at\n"
    "workspace offset &20.")
subroutine(0xA612, "store_ptr_at_ws_y",
    title="Store 16-bit pointer at workspace offset Y",
    description="Writes a 16-bit address to (nfs_workspace)+Y.\n"
    "The low byte comes from A; the high byte is\n"
    "computed from osword_pb_ptr_hi plus carry,\n"
    "supporting pointer arithmetic across page\n"
    "boundaries.",
    on_entry={"a": "pointer low byte",
              "y": "workspace offset",
              "c": "carry for high byte addition"})
subroutine(0xA6FB, "copy_pb_byte_to_ws",
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
subroutine(0xA868, "init_bridge_poll",
    title="Initialise Econet bridge routing table",
    description="Checks the bridge status byte: if &FF\n"
    "(uninitialised), broadcasts a bridge query\n"
    "packet and polls for replies. Each reply\n"
    "adds a network routing entry to the bridge\n"
    "table. Skips the broadcast if the table has\n"
    "already been populated from a previous call.")
subroutine(0xA964, "enable_irq_and_poll",
    title="Enable interrupts and send Econet packet",
    description="Executes CLI to re-enable interrupts, then\n"
    "falls through to send_net_packet. Used after\n"
    "a sequence that ran with interrupts disabled\n"
    "to ensure the packet is sent with normal\n"
    "interrupt handling active.")
subroutine(0xA981, "push_osword_handler_addr",
    title="Push OSWORD handler address for RTS dispatch",
    description="Indexes the OSWORD handler dispatch table\n"
    "using the current OSWORD number to push the\n"
    "handler's address (hi/lo) onto the stack.\n"
    "Reloads the OSWORD number from osbyte_a_copy\n"
    "so the dispatched handler can identify the\n"
    "specific call.")
subroutine(0xA9AC, "tx_econet_abort",
    title="Send Econet abort/disconnect packet",
    description="Stores the abort code in workspace, configures\n"
    "the TX control block with control byte &80\n"
    "(immediate operation flag), and transmits the\n"
    "abort packet. Used to cleanly disconnect from\n"
    "a remote station during error recovery.")
subroutine(0xAA24, "match_rx_code",
    title="Search receive code table for match",
    description="Scans a table of receive operation codes\n"
    "starting at index X, comparing each against A.\n"
    "Returns with Z set if a match is found, Z clear\n"
    "if the end-of-table marker is reached.",
    on_entry={"a": "receive code to match",
              "x": "starting table index"},
    on_exit={"z": "set if match found"})
subroutine(0xAA6A, "init_ws_copy_wide",
    title="Initialise workspace copy in wide mode (14 bytes)",
    description="Copies 14 bytes to workspace offset &7C.\n"
    "Falls through to the template-driven copy\n"
    "loop which handles &FD (skip), &FE (end),\n"
    "and &FC (page pointer) markers.")
subroutine(0xAA73, "init_ws_copy_narrow",
    title="Initialise workspace copy in narrow mode (27 bytes)",
    description="Sets up a 27-byte copy to workspace offset &17,\n"
    "then falls through to ws_copy_vclr_entry for\n"
    "the template-driven copy loop. Used for the\n"
    "compact workspace initialisation variant.")
subroutine(0xAA77, "ws_copy_vclr_entry",
    title="Template-driven workspace copy with V clear",
    description="Processes a template byte array to initialise\n"
    "workspace. Special marker bytes: &FE terminates\n"
    "the copy, &FD skips the current offset, and &FC\n"
    "substitutes the workspace page pointer. All\n"
    "other values are stored directly to the\n"
    "workspace at the current offset.")
subroutine(0xAAD0, "reset_spool_buf_state",
    title="Reset spool buffer to initial state",
    description="Sets the spool buffer pointer to &25 (first\n"
    "available data position) and the control state\n"
    "byte to &41 (ready for new data). Called after\n"
    "processing a complete spool data block.")
subroutine(0xAB00, "append_byte_to_rxbuf",
    title="Append byte to receive buffer",
    description="Stores A in the receive buffer at the current\n"
    "buffer index (ws_ptr_lo), then increments the\n"
    "index. Used to accumulate incoming spool data\n"
    "bytes before processing.",
    on_entry={"a": "byte to append"})
subroutine(0xAB09, "handle_spool_ctrl_byte",
    title="Handle spool control byte and flush buffer",
    description="Rotates bit 0 of the control byte into carry\n"
    "for mode selection (print vs spool), appends\n"
    "the byte to the buffer, calls process_spool_data\n"
    "to transmit the accumulated data, and resets\n"
    "the buffer state ready for the next block.")
subroutine(0xAB24, "process_spool_data",
    title="Transmit accumulated spool buffer data",
    description="Copies the workspace state to the TX control\n"
    "block, sends a disconnect reply if the previous\n"
    "transfer requires acknowledgment, then handles\n"
    "the spool output sequence by setting up and\n"
    "sending the pass-through TX buffer.")
subroutine(0xAC12, "send_disconnect_reply",
    title="Send Econet disconnect reply packet",
    description="Sets up the TX pointer, copies station\n"
    "addresses, matches the station in the table,\n"
    "and sends the response. Waits for\n"
    "acknowledgment before returning.")
subroutine(0xACCB, "commit_state_byte",
    title="Copy current state byte to committed state",
    description="Reads the working state byte from workspace and\n"
    "stores it to the committed state location. Used\n"
    "to finalise a state transition after all related\n"
    "workspace fields have been updated.")
subroutine(0xACD2, "serialise_palette_entry",
    title="Serialise palette register to workspace",
    description="Reads the current logical colour for a palette\n"
    "register via OSBYTE &0B and stores both the\n"
    "palette value and the display mode information\n"
    "in the workspace block. Used during remote\n"
    "screen state capture.")
subroutine(0xACE5, "read_osbyte_to_ws_x0",
    title="Read OSBYTE with X=0 and store to workspace",
    description="Sets X=0 then falls through to read_osbyte_to_ws\n"
    "to issue the OSBYTE call and store the result.\n"
    "Used when the OSBYTE parameter X must be zero.")
subroutine(0xACE7, "read_osbyte_to_ws",
    title="Issue OSBYTE from table and store result",
    description="Loads the OSBYTE function code from the next\n"
    "entry in the OSBYTE table, issues the call, and\n"
    "stores the Y result in workspace at the current\n"
    "offset. Advances the table pointer for the next\n"
    "call.")

# --- cmd_ex subroutines ---

subroutine(0xAE70, "print_10_chars",
    title="Print 10 characters from reply buffer",
    description="Sets Y=10 and falls through to\n"
    "print_chars_from_buf. Used by cmd_ex to print\n"
    "fixed-width directory title, directory name, and\n"
    "library name fields.",
    on_entry={"x": "buffer offset to start printing from"})
subroutine(0xAE72, "print_chars_from_buf",
    title="Print Y characters from buffer via OSASCI",
    description="Loops Y times, loading each byte from l0f05+X\n"
    "and printing it via OSASCI. Advances X after\n"
    "each character, leaving X pointing past the\n"
    "last printed byte.",
    on_entry={"x": "buffer offset", "y": "character count"})
subroutine(0xAE80, "parse_cmd_arg_y0",
    title="Parse command argument from offset zero",
    description="Sets Y=0 and falls through to parse_filename_arg\n"
    "for GSREAD-based filename parsing with prefix\n"
    "character handling.")
subroutine(0xAE82, "parse_filename_arg",
    title="Parse filename via GSREAD with prefix handling",
    description="Calls gsread_to_buf to read the command line\n"
    "string into the &0E30 buffer, then falls through\n"
    "to parse_access_prefix to process '&', ':', '.',\n"
    "and '#' prefix characters.")
subroutine(0xAE85, "parse_access_prefix",
    title="Parse access and FS selection prefix characters",
    description="Examines the first character(s) of the parsed\n"
    "buffer at &0E30 for prefix characters: '&' sets\n"
    "the FS selection flag (bit 6 of l1071) and strips\n"
    "the prefix, ':' with '.' also triggers FS\n"
    "selection, '#' is accepted as a channel prefix.\n"
    "Raises 'Bad file name' for invalid combinations\n"
    "like '&.' followed by CR.")
subroutine(0xAEA5, "strip_token_prefix",
    title="Strip first character from parsed token buffer",
    description="Shifts all bytes in the &0E30 buffer left by\n"
    "one position (removing the first character),\n"
    "then trims any trailing spaces by replacing\n"
    "them with CR terminators. Used after consuming\n"
    "a prefix character like '&' or ':'.")
subroutine(0xAEF0, "copy_arg_to_buf_x0",
    title="Copy argument to TX buffer from offset zero",
    description="Sets X=0 and falls through to copy_arg_to_buf\n"
    "then copy_arg_validated. Provides the simplest\n"
    "entry point for copying a single parsed argument\n"
    "into the TX buffer at position zero.")
subroutine(0xAEF2, "copy_arg_to_buf",
    title="Copy argument to TX buffer with Y=0",
    description="Sets Y=0 and falls through to copy_arg_validated\n"
    "with carry set, enabling '&' character validation.\n"
    "X must already contain the destination offset\n"
    "within the TX buffer.")
subroutine(0xAEF4, "copy_arg_validated",
    title="Copy command line characters to TX buffer",
    description="Copies characters from (fs_crc_lo)+Y to l0f05+X\n"
    "until a CR terminator is reached. With carry set,\n"
    "validates each character against '&' — raising\n"
    "'Bad file name' if found — to prevent FS selector\n"
    "characters from being embedded in filenames.",
    on_entry={"x": "TX buffer destination offset",
              "y": "command line source offset",
              "c": "set to enable '&' validation"})
subroutine(0xAF12, "mask_owner_access",
    title="Clear FS selection flags from options word",
    description="ANDs the l1071 flags byte with &1F, clearing\n"
    "the FS selection flag (bit 6) and other high\n"
    "bits to retain only the 5-bit owner access\n"
    "mask. Called before parsing to reset the prefix\n"
    "state from a previous command.")
subroutine(0xAF27, "ex_print_col_sep",
    title="Print column separator or newline for *Ex/*Cat",
    description="In *Cat mode, increments a column counter modulo 4\n"
    "and prints a two-space separator between entries,\n"
    "with a newline at the end of each row. In *Ex\n"
    "mode (fs_spool_handle negative), prints a newline\n"
    "after every entry. Scans the entry data and loops\n"
    "back to print the next entry's characters.")

# --- cmd_remove subroutines ---

subroutine(0xAF65, "print_num_no_leading",
    title="Print decimal number with leading zero suppression",
    description="Sets V via BIT bit_test_ff_pad to enable leading\n"
    "zero suppression, then falls through to\n"
    "print_decimal_3dig. Used by print_station_id\n"
    "for compact station number display.",
    on_entry={"a": "number to print (0-255)"})
subroutine(0xAF68, "print_decimal_3dig",
    title="Print byte as 3-digit decimal via OSASCI",
    description="Extracts hundreds, tens and units digits by\n"
    "successive calls to print_decimal_digit. The V\n"
    "flag controls leading zero suppression: if set,\n"
    "zero digits are skipped until a non-zero digit\n"
    "appears. V is always cleared before the units\n"
    "digit to ensure at least one digit is printed.",
    on_entry={"a": "number to print (0-255)",
              "v": "set to suppress leading zeros"})
subroutine(0xAF76, "print_decimal_digit",
    title="Print one decimal digit by repeated subtraction",
    description="Initialises X to '0'-1 and loops, incrementing X\n"
    "while subtracting the divisor from Y. On underflow,\n"
    "adds back the divisor to get the remainder in Y.\n"
    "If V is set, suppresses leading zeros by skipping\n"
    "the OSASCI call when the digit is '0'.",
    on_entry={"a": "divisor", "y": "value to divide"},
    on_exit={"y": "remainder after division"})
subroutine(0xAF95, "save_ptr_to_os_text",
    title="Copy text pointer to OS text pointer workspace",
    description="Saves fs_crc_lo/hi into the MOS text pointer\n"
    "locations at &00F2/&00F3. Preserves A on the\n"
    "stack. Called before GSINIT/GSREAD sequences\n"
    "that need to parse from the current command\n"
    "line position.")
subroutine(0xAFA1, "skip_to_next_arg",
    title="Advance past spaces to the next command argument",
    description="Scans (fs_crc_lo)+Y for space characters,\n"
    "advancing Y past each one. Returns with A\n"
    "holding the first non-space character, or CR\n"
    "if the end of line is reached. Used by *CDir\n"
    "and *Remove to detect extra arguments.",
    on_exit={"a": "first non-space character or CR",
             "y": "offset of that character"})
subroutine(0xAFB5, "save_ptr_to_spool_buf",
    title="Copy text pointer to spool buffer pointer",
    description="Saves fs_crc_lo/hi into fs_options/fs_block_offset\n"
    "for use as the spool buffer pointer. Preserves A\n"
    "on the stack. Called by *PS and *PollPS before\n"
    "parsing their arguments.")
subroutine(0xAFC0, "init_spool_drive",
    title="Initialise spool drive page pointers",
    description="Calls get_ws_page to read the workspace page\n"
    "number for the current ROM slot, stores it as\n"
    "the spool drive page high byte (l00af), and\n"
    "clears the low byte (l00ae) to zero. Preserves\n"
    "Y on the stack.")

# --- cmd_ps subroutines ---

subroutine(0xAFF7, "copy_ps_data_y1c",
    title="Copy printer server template at offset &1C",
    description="Sets Y=&1C and falls through to copy_ps_data.\n"
    "Called during workspace initialisation\n"
    "(svc_2_private_workspace) to set up the printer\n"
    "server template at the standard offset.")
subroutine(0xAFF9, "copy_ps_data",
    title="Copy 8-byte printer server template to RX buffer",
    description="Copies 8 bytes from the credits_string_mid area\n"
    "(using X starting at &F8, wrapping to 0) into\n"
    "the RX buffer at the current Y offset. The\n"
    "template contains default printer server\n"
    "configuration data used when initialising a new\n"
    "printer server slot.")
subroutine(0xB0A1, "print_file_server_is",
    title="Print 'File server ' prefix",
    description="Uses print_inline to output 'File' then falls through\n"
    "to the shared ' server is ' suffix at\n"
    "print_printer_server_is.")
subroutine(0xB0AB, "print_printer_server_is",
    title="Print 'Printer server is ' prefix",
    description="Uses print_inline to output the full label\n"
    "'Printer server is ' with trailing space.")
subroutine(0xB0C6, "load_ps_server_addr",
    title="Load printer server address from workspace",
    description="Reads the station and network bytes from workspace\n"
    "offsets 2 and 3 into the station/network variables.")
subroutine(0xB0D2, "pop_requeue_ps_scan",
    title="Pop return address and requeue PS slot scan",
    description="Converts the PS slot flags to a workspace index,\n"
    "writes slot data, and jumps back into the PS scan\n"
    "loop to continue processing.")
subroutine(0xB13A, "write_ps_slot_byte_ff",
    title="Write buffer page byte and two &FF markers",
    description="Stores the buffer page byte at the current Y offset\n"
    "in workspace, followed by two &FF sentinel bytes.\n"
    "Advances Y after each write.")
subroutine(0xB141, "write_two_bytes_inc_y",
    title="Write A to two consecutive workspace bytes",
    description="Stores A at the current Y offset via (nfs_workspace),Y\n"
    "then again at Y+1, advancing Y after each write.",
    on_entry={"a": "byte to store", "y": "workspace offset"})
subroutine(0xB149, "reverse_ps_name_to_tx",
    title="Reverse-copy printer server name to TX buffer",
    description="Copies 8 bytes from the RX buffer (offsets &1C-&23)\n"
    "to the TX buffer (offsets &13-&1B) in reversed byte\n"
    "order, pushing onto the stack then popping back.")
subroutine(0xB174, "print_station_addr",
    title="Print station address as decimal net.station",
    description="If the network number is zero, prints only the\n"
    "station number. Otherwise prints network.station\n"
    "separated by a dot. V flag controls padding with\n"
    "leading spaces for column alignment.")

# --- cmd_pollps subroutines ---

subroutine(0xB2C4, "init_ps_slot_from_rx",
    title="Initialise PS slot buffer from template data",
    description="Copies 12 bytes from the template at offsets &78-&83\n"
    "into workspace, substituting the RX buffer page at\n"
    "offsets &7D and &81.")
subroutine(0xB2DB, "store_char_uppercase",
    title="Convert to uppercase and store in RX buffer",
    description="If the character in A is lowercase (&61-&7A), converts\n"
    "to uppercase by clearing bit 5. Stores the result in\n"
    "the RX buffer at the current position, advances the\n"
    "buffer pointer, and decrements the character count.",
    on_entry={"a": "character to store"})

# --- cmd_wipe subroutines ---

subroutine(0xB41F, "flush_and_read_char",
    title="Flush keyboard buffer and read one character",
    description="Calls OSBYTE &0F to flush the input buffer, then\n"
    "OSRDCH to read a single character. Raises an escape\n"
    "error if escape was pressed (carry set on return).")
subroutine(0xB439, "init_channel_table",
    title="Initialise channel allocation table",
    description="Clears all 256 bytes of the table, then marks\n"
    "available channel slots based on the count from\n"
    "the receive buffer. Sets the first slot to &C0\n"
    "(active channel marker).")
subroutine(0xB45B, "attr_to_chan_index",
    title="Convert channel attribute to table index",
    description="Subtracts &20 from the attribute byte and clamps\n"
    "to the range 0-&0F. Returns &FF if out of range.\n"
    "Preserves processor flags via PHP/PLP.",
    on_entry={"a": "channel attribute byte"},
    on_exit={"a": "table index (0-&0F) or &FF if invalid"})
subroutine(0xB46A, "check_chan_char",
    title="Validate channel character and look up entry",
    description="Characters below '0' are looked up directly in\n"
    "the channel table. Characters '0' and above are\n"
    "converted to a table index via attr_to_chan_index.\n"
    "Raises 'Net channel' error if invalid.",
    on_entry={"a": "channel character"})
subroutine(0xB49D, "lookup_chan_by_char",
    title="Look up channel by character code",
    description="Converts the character to a table index via\n"
    "attr_to_chan_index, checks the station/network\n"
    "match via match_station_net, and returns the\n"
    "channel flags in A.",
    on_entry={"a": "channel character"},
    on_exit={"a": "channel flags"})
subroutine(0xB4DC, "store_result_check_dir",
    title="Store channel attribute and check not directory",
    description="Writes the current channel attribute to the receive\n"
    "buffer, then tests the directory flag (bit 1). Raises\n"
    "'Is a dir.' error if the attribute refers to a\n"
    "directory rather than a file.")
subroutine(0xB4E3, "check_not_dir",
    title="Validate channel is not a directory",
    description="Calls check_chan_char to validate the channel, then\n"
    "tests the directory flag (bit 1). Raises 'Is a dir.'\n"
    "error if the channel refers to a directory.")
subroutine(0xB4FA, "alloc_fcb_slot",
    title="Allocate a free file control block slot",
    description="Scans FCB slots &20-&2F for an empty entry.\n"
    "Returns Z=0 with X=slot index on success, or\n"
    "Z=1 with A=0 if all slots are occupied.",
    on_exit={"x": "slot index (if Z=0)", "z": "0=success, 1=no free slot"})
subroutine(0xB52E, "alloc_fcb_or_error",
    title="Allocate FCB slot or raise error",
    description="Calls alloc_fcb_slot and raises 'No more FCBs'\n"
    "if no free slot is available. Preserves the\n"
    "caller's argument on the stack.")
subroutine(0xB54A, "close_all_net_chans",
    title="Close all network channels for current station",
    description="Scans FCB slots &0F down to 0, closing those\n"
    "matching the current station. C=0 closes all\n"
    "matching entries; C=1 closes with write-flush.",
    on_entry={"c": "0=close all, 1=close with write-flush"})
subroutine(0xB551, "scan_fcb_flags",
    title="Scan FCB slot flags from &10 downward",
    description="Iterates through FCB slots starting at &10,\n"
    "checking each slot's flags byte. Returns when\n"
    "all slots have been processed.")
subroutine(0xB57A, "match_station_net",
    title="Check FCB slot matches current station/network",
    description="Compares the station and network numbers in the\n"
    "FCB at slot X against the current values using\n"
    "EOR. Returns Z=1 if both match, Z=0 if either\n"
    "differs.",
    on_entry={"x": "FCB slot index"},
    on_exit={"z": "1=match, 0=no match"})
subroutine(0xB589, "find_open_fcb",
    title="Find next open FCB slot for current connection",
    description="Scans from the current index, wrapping around at\n"
    "the end. On the first pass finds active entries\n"
    "matching the station; on the second pass finds\n"
    "empty slots for new allocations.")
subroutine(0xB5CC, "init_wipe_counters",
    title="Initialise byte counters for wipe/transfer",
    description="Clears the pass counter, byte counter, offset\n"
    "counter, and transfer flag. Stores &FF sentinels\n"
    "in l10cd/l10ce. Returns with X/Y pointing at\n"
    "workspace offset &10CA.",
    on_exit={"x": "&CA (workspace offset low)", "y": "&10 (workspace page)"})
subroutine(0xB5EF, "start_wipe_pass",
    title="Start wipe pass for current FCB",
    description="Verifies the workspace checksum, saves the station\n"
    "context (pushing station low/high), initialises\n"
    "transfer counters via init_wipe_counters, and sends\n"
    "the initial request via send_and_receive. Clears the\n"
    "active and offset flags on completion.",
    on_entry={"x": "FCB slot index"})
subroutine(0xB660, "save_fcb_context",
    title="Save FCB context and process pending slots",
    description="Copies 13 bytes from the TX buffer (&0F00) and\n"
    "fs_load_addr workspace to temporary storage at\n"
    "&10D9. If Y=0, skips to the restore loop. Otherwise\n"
    "scans for pending FCB slots (bits 7+6 set), flushes\n"
    "each via start_wipe_pass, allocates new slots via\n"
    "find_open_fcb, and sends directory requests. Falls\n"
    "through to restore_catalog_entry.",
    on_entry={"y": "filter attribute (0=process all)"})
subroutine(0xB729, "restore_catalog_entry",
    title="Restore saved catalog entry to TX buffer",
    description="Copies 13 bytes from the context buffer at &10D9\n"
    "back to the TX buffer at &0F00. Falls through to\n"
    "find_matching_fcb.")
subroutine(0xB738, "find_matching_fcb",
    title="Find FCB slot matching channel attribute",
    description="Scans FCB slots 0-&0F for an active entry whose\n"
    "attribute reference matches l10c9. Converts the\n"
    "attribute to a channel index, then verifies the\n"
    "station and network numbers. On the first scan\n"
    "past slot &0F, saves context via save_fcb_context\n"
    "and restarts. Returns Z=0 if the FCB has saved\n"
    "offset data (bit 5 set).",
    on_exit={"x": "matching FCB index", "z": "0=has offset data, 1=no offset"})
subroutine(0xB791, "inc_fcb_byte_count",
    title="Increment 3-byte FCB transfer count",
    description="Increments l1000+X (low), cascading overflow to\n"
    "l1010+X (mid) and l1020+X (high).",
    on_entry={"x": "FCB slot index"})
subroutine(0xB79F, "process_all_fcbs",
    title="Process all active FCB slots",
    description="Saves fs_options, fs_block_offset, and X/Y on the\n"
    "stack, then scans FCB slots &0F down to 0. Calls\n"
    "start_wipe_pass for each active entry matching the\n"
    "filter attribute in Y (0=match all). Restores all\n"
    "saved context on completion. Also contains the\n"
    "OSBGET/OSBPUT inline logic for reading and writing\n"
    "bytes through file channels.",
    on_entry={"y": "filter attribute (0=process all)"})
subroutine(0xB920, "send_wipe_request",
    title="Send wipe/close request packet",
    description="Sets up the TX control block with function code\n"
    "&90, the reply port from Y, and the data byte from\n"
    "A. Sends via send_disconnect_reply, then checks the\n"
    "error code — raises the server error if non-zero.",
    on_entry={"a": "data byte to send", "y": "reply port"})
subroutine(0xB979, "send_and_receive",
    title="Set up FS options and transfer workspace",
    description="Calls set_options_ptr to configure the FS options\n"
    "pointer, then jumps to setup_transfer_workspace to\n"
    "initialise the transfer and send the request.",
    on_entry={"a": "transfer mode", "x": "workspace offset low", "y": "workspace page"})

# --- cmd_print subroutines ---

subroutine(0xB9EA, "abort_if_escape",
    title="Test escape flag and abort if pressed",
    description="Checks the escape flag byte; returns immediately\n"
    "if bit 7 is clear. If escape has been pressed,\n"
    "falls through to the escape abort handler which\n"
    "acknowledges the escape via OSBYTE &7E.")

# --- cmd_dump subroutines ---

subroutine(0xBACE, "print_dump_header",
    title="Print hex dump column header line",
    description="Outputs the starting address followed by 16 hex\n"
    "column numbers (00-0F), each separated by a space.\n"
    "Provides the column alignment header for *Dump\n"
    "output.")
subroutine(0xBB0C, "close_ws_file",
    title="Close file handle stored in workspace",
    description="Loads the file handle from ws_page and closes it\n"
    "via OSFIND with A=0.")
subroutine(0xBB13, "open_file_for_read",
    title="Open file for reading via OSFIND",
    description="Computes the filename address from the command text\n"
    "pointer plus the Y offset, calls OSFIND with A=&40\n"
    "(open for input). Stores the handle in ws_page.\n"
    "Raises 'Not found' if the returned handle is zero.")
subroutine(0xBB55, "parse_dump_range",
    title="Parse hex address for dump range",
    description="Reads up to 4 hex digits from the command line\n"
    "into a 4-byte accumulator, stopping at CR or\n"
    "space. Each digit shifts the accumulator left\n"
    "by 4 bits before ORing in the new nybble.")
subroutine(0xBBBE, "init_dump_buffer",
    title="Initialise dump buffer and parse address range",
    description="Parses the start and end addresses from the command\n"
    "line via parse_dump_range. If no end address is given,\n"
    "defaults to the file extent. Validates both addresses\n"
    "against the file size, raising 'Outside file' if either\n"
    "exceeds the extent.")
subroutine(0xBC84, "advance_x_by_8",
    title="Advance X by 8 via nested JSR chain",
    description="Calls advance_x_by_4 (which itself JSRs inx4 then\n"
    "falls through to inx4), then falls through to inx4\n"
    "for a total of 4+4=8 INX operations.")
subroutine(0xBC87, "advance_x_by_4",
    title="Advance X by 4 via JSR and fall-through",
    description="JSRs to inx4 for 4 INX operations, then falls\n"
    "through to inx4 for another 4 — but when called\n"
    "directly (not from advance_x_by_8), the caller\n"
    "returns after the first inx4, yielding X+4.")
subroutine(0xBC8A, "inx4",
    title="Increment X four times",
    description="Four consecutive INX instructions. Used as a\n"
    "building block by advance_x_by_4 and\n"
    "advance_x_by_8 via JSR/fall-through chaining.")

# ============================================================
# Inline comments (from NFS 3.65 correspondence)
# ============================================================

comment(0x0016, "A=&FF: signal error to co-processor via R4", inline=True)
comment(0x0018, "Send &FF error signal to Tube R4", inline=True)
comment(0x001B, "Flush any pending R2 byte", inline=True)
comment(0x001E, "A=0: send zero prefix to R2", inline=True)
comment(0x0020, "Send zero prefix byte via R2", inline=True)
comment(0x0023, "Y=0: start of error block at (&FD)", inline=True)
comment(0x0024, "Load error number from (&FD),0", inline=True)
comment(0x0026, "Send error number via R2", inline=True)
comment(0x0029, "Advance to next error string byte", inline=True)
comment(0x002A, "Load next error string byte", inline=True)
comment(0x002C, "Send error string byte via R2", inline=True)
comment(0x002F, "Zero byte = end of error string", inline=True)
comment(0x0030, "Loop until zero terminator sent", inline=True)
comment(0x0032, "Reset stack pointer to top", inline=True)
comment(0x0034, "TXS: set stack pointer from X", inline=True)
comment(0x0035, "Enable interrupts for main loop", inline=True)
comment(0x0036, "BIT R1 status: check WRCH request", inline=True)
comment(0x0039, "R1 not ready: check R2 instead", inline=True)
comment(0x003B, "Read character from Tube R1 data", inline=True)
comment(0x0041, "BIT R2 status: check command byte", inline=True)
comment(0x0044, "R2 not ready: loop back to R1 check", inline=True)
comment(0x0046, "Re-check R1: WRCH has priority over R2", inline=True)
comment(0x0049, "R1 ready: handle WRCH first", inline=True)
comment(0x004B, "Read command byte from Tube R2 data", inline=True)
comment(0x004E, "Self-modify JMP low byte for dispatch", inline=True)
comment(0x0050, "Dispatch to handler via indirect JMP", inline=True)
comment(0x0053, "Tube transfer address low byte", inline=True)
comment(0x0054, "Tube transfer page (default &80)", inline=True)
comment(0x0055, "Tube transfer address byte 2", inline=True)
comment(0x0056, "Tube transfer address byte 3", inline=True)
comment(0x0400, "JMP to BEGIN startup entry", inline=True)
comment(0x0403, "JMP to tube_escape_check (&06A7)", inline=True)
comment(0x0406, "A>=&80: address claim; A<&80: data transfer", inline=True)
comment(0x0408, "A<&80: data transfer setup (SENDW)", inline=True)
comment(0x040A, "A>=&C0: new address claim from another host", inline=True)
comment(0x040C, "C=1: external claim, check ownership", inline=True)
comment(0x040E, "Map &80-&BF range to &C0-&FF for comparison", inline=True)
comment(0x0410, "Is this for our currently-claimed address?", inline=True)
comment(0x0412, "Match: we own it, return (no release)", inline=True)
comment(0x0414, "PHP: save interrupt state for release", inline=True)
comment(0x0415, "SEI: disable interrupts during R4 protocol", inline=True)
comment(0x0416, "R4 cmd 5: release our address claim", inline=True)
comment(0x0418, "Send release command to co-processor", inline=True)
comment(0x041B, "Load our currently-claimed address", inline=True)
comment(0x041D, "Send our address as release parameter", inline=True)
comment(0x0420, "Restore interrupt state", inline=True)
comment(0x0421, "&80 sentinel: clear address claim", inline=True)
comment(0x0423, "&80 sentinel = no address currently claimed", inline=True)
comment(0x0425, "Store to claim-in-progress flag", inline=True)
comment(0x0427, "Return from tube_post_init", inline=True)
comment(0x0428, "Another host claiming; check if we're owner", inline=True)
comment(0x042A, "C=1: we have an active claim", inline=True)
comment(0x042C, "Compare with our claimed address", inline=True)
comment(0x042E, "Match: return (we already have it)", inline=True)
comment(0x0430, "Not ours: CLC = we don't own this address", inline=True)
comment(0x0431, "Return with C=0 (claim denied)", inline=True)
comment(0x0432, "Accept new claim: update our address", inline=True)
comment(0x0434, "Return with address updated", inline=True)
comment(0x0435, "PHP: save interrupt state", inline=True)
comment(0x0436, "SEI: disable interrupts for R4 protocol", inline=True)
comment(0x0437, "Save 16-bit transfer address from (X,Y)", inline=True)
comment(0x0439, "Store address pointer low byte", inline=True)
comment(0x043B, "Send transfer type byte to co-processor", inline=True)
comment(0x043E, "X = transfer type for table lookup", inline=True)
comment(0x043F, "Y=3: send 4 bytes (address + claimed addr)", inline=True)
comment(0x0441, "Send our claimed address + 4-byte xfer addr", inline=True)
comment(0x0443, "Send transfer address byte", inline=True)
comment(0x0446, "Load transfer address byte from (X,Y)", inline=True)
comment(0x0448, "Send address byte to co-processor via R4", inline=True)
comment(0x044B, "Previous byte (big-endian: 3,2,1,0)", inline=True)
comment(0x044C, "Loop for all 4 address bytes", inline=True)
comment(0x044E, "Y=&18: enable Tube control register", inline=True)
comment(0x0450, "Enable Tube interrupt generation", inline=True)
comment(0x0453, "Look up Tube control bits for this xfer type", inline=True)
comment(0x0456, "Apply transfer-specific control bits", inline=True)
comment(0x0459, "LSR: check bit 2 (2-byte flush needed?)", inline=True)
comment(0x045A, "LSR: shift bit 2 to carry", inline=True)
comment(0x045B, "C=0: no flush needed, skip R3 reads", inline=True)
comment(0x045D, "Dummy R3 reads: flush for 2-byte transfers", inline=True)
comment(0x0460, "Second dummy read to flush R3 FIFO", inline=True)
comment(0x0463, "Trigger co-processor ack via R4", inline=True)
comment(0x0466, "Poll R4 status for co-processor response", inline=True)
comment(0x0469, "Bit 6 clear: not ready, keep polling", inline=True)
comment(0x046B, "R4 bit 7: co-processor acknowledged transfer", inline=True)
comment(0x046D, "Type 4 = SENDW (host-to-parasite word xfer)", inline=True)
comment(0x046F, "Not SENDW type: skip release path", inline=True)
comment(0x0471, "SENDW complete: release, sync, restart", inline=True)
comment(0x0474, "Sync via R2 send", inline=True)
comment(0x0477, "Restart Tube main loop", inline=True)
comment(0x047A, "LSR: check bit 0 (NMI used?)", inline=True)
comment(0x047B, "C=0: NMI not used, skip NMI release", inline=True)
comment(0x047D, "Release Tube NMI (transfer used interrupts)", inline=True)
comment(0x047F, "Write &88 to Tube control to release NMI", inline=True)
comment(0x0482, "Restore interrupt state", inline=True)
comment(0x0483, "Return from transfer setup", inline=True)
comment(0x0484, "BEGIN: enable interrupts for Tube host code", inline=True)
comment(0x0485, "C=1: hard break, claim addr &FF", inline=True)
comment(0x0487, "C=0, A!=0: re-init path", inline=True)
comment(0x0489, "Z=1 from C=0 path: just acknowledge", inline=True)
comment(0x048C, "X=0 for OSBYTE", inline=True)
comment(0x048E, "Y=&FF for OSBYTE", inline=True)
comment(0x0490, "OSBYTE &FD: what type of reset was this?", inline=True)
comment(0x0496, "Soft break (X=0): re-init Tube and restart", inline=True)
comment(0x0498, "Claim address &FF (startup = highest prio)", inline=True)
comment(0x049A, "Request address claim from Tube system", inline=True)
comment(0x049D, "C=0: claim failed, retry", inline=True)
comment(0x049F, "Init reloc pointers from ROM header", inline=True)
comment(0x04A2, "R4 cmd 7: SENDW to send ROM to parasite", inline=True)
comment(0x04A4, "Set up Tube for SENDW transfer", inline=True)
comment(0x04A7, "Y=0: start at beginning of page", inline=True)
comment(0x04A9, "Store to zero page pointer low byte", inline=True)
comment(0x04AB, "Send 256-byte page via R3, byte at a time", inline=True)
comment(0x04AD, "Write byte to Tube R3 data register", inline=True)
comment(0x04B0, "Timing delay: Tube data register needs NOPs", inline=True)
comment(0x04B1, "NOP delay (2)", inline=True)
comment(0x04B2, "NOP delay (3)", inline=True)
comment(0x04B3, "Next byte in page", inline=True)
comment(0x04B4, "Loop for all 256 bytes", inline=True)
comment(0x04B6, "Increment 24-bit destination addr", inline=True)
comment(0x04B8, "No carry: skip higher bytes", inline=True)
comment(0x04BA, "Carry into second byte", inline=True)
comment(0x04BC, "No carry: skip third byte", inline=True)
comment(0x04BE, "Carry into third byte", inline=True)
comment(0x04C0, "Increment page counter", inline=True)
comment(0x04C2, "Bit 6 set = all pages transferred", inline=True)
comment(0x04C4, "More pages: loop back to SENDW", inline=True)
comment(0x04C6, "Re-init reloc pointers for final claim", inline=True)
comment(0x04C9, "A=4: transfer type for final address claim", inline=True)
comment(0x04CB, "Y=0: transfer address low byte", inline=True)
comment(0x04CD, "X=&53: transfer address high byte (&0053)", inline=True)
comment(0x04CF, "Claim Tube address for transfer", inline=True)
comment(0x04D2, "Init: start sending from &8000", inline=True)
comment(0x04D4, "Store &80 as source page high byte", inline=True)
comment(0x04D6, "Store &80 as page counter initial value", inline=True)
comment(0x04D8, "A=&20: bit 5 mask for ROM type check", inline=True)
comment(0x04DA, "ROM type bit 5: reloc address in header?", inline=True)
comment(0x04DD, "Y = 0 or &20 (reloc flag)", inline=True)
comment(0x04DE, "Store as transfer address selector", inline=True)
comment(0x04E0, "No reloc addr: use defaults", inline=True)
comment(0x04E2, "Skip past copyright string to find reloc addr", inline=True)
comment(0x04E5, "Skip past null-terminated copyright string", inline=True)
comment(0x04E6, "Load next byte from ROM header", inline=True)
comment(0x04E9, "Loop until null terminator found", inline=True)
comment(0x04EB, "Read 4-byte reloc address from ROM header", inline=True)
comment(0x04EE, "Store reloc addr byte 1 as transfer addr", inline=True)
comment(0x04F0, "Load reloc addr byte 2", inline=True)
comment(0x04F3, "Store as source page start", inline=True)
comment(0x04F5, "Load reloc addr byte 3", inline=True)
comment(0x04F8, "Load reloc addr byte 4 (highest)", inline=True)
comment(0x04FB, "Store high byte of end address", inline=True)
comment(0x04FD, "Store byte 3 of end address", inline=True)
comment(0x04FF, "Return with pointers initialised", inline=True)
# Tube R2 command dispatch table: 12 entries mapping R2 command
# codes 0-11 to handler addresses in pages 5-6.
_tube_r2_entries = [
    (0x0500, "tube_osrdch",        "R2 cmd 0: OSRDCH"),
    (0x0502, "tube_oscli",         "R2 cmd 1: OSCLI"),
    (0x0504, "tube_osbyte_2param", "R2 cmd 2: OSBYTE (2-param)"),
    (0x0506, "tube_osbyte_long",   "R2 cmd 3: OSBYTE (3-param)"),
    (0x0508, "tube_osword",        "R2 cmd 4: OSWORD"),
    (0x050A, "tube_osword_rdln",   "R2 cmd 5: OSWORD 0 (read line)"),
    (0x050C, "tube_osargs",        "R2 cmd 6: OSARGS"),
    (0x050E, "tube_osbget",        "R2 cmd 7: OSBGET"),
    (0x0510, "tube_osbput",        "R2 cmd 8: OSBPUT"),
    (0x0512, "tube_osfind",        "R2 cmd 9: OSFIND"),
    (0x0514, "tube_osfile",        "R2 cmd 10: OSFILE"),
    (0x0516, "tube_osgbpb",        "R2 cmd 11: OSGBPB"),
]
for addr, target_label, desc in _tube_r2_entries:
    word(addr)
    expr(addr, target_label)
    comment(addr, desc, inline=True)
comment(0x0518, """\
Tube ULA control register values, indexed by transfer
type (0-7). Written to &FEE0 after clearing V+M with
&18. Bit layout: S=set/clear, T=reset regs, P=PRST,
V=2-byte R3, M=PNMI(R3), J=PIRQ(R4), I=PIRQ(R1),
Q=HIRQ(R4). Bits 1-7 select flags; bit 0 (S) is the
value to set or clear.""")
_tube_ctrl_entries = [
    (0x0518, "Type 0: set I+J (1-byte R3, parasite to host)"),
    (0x0519, "Type 1: set M (1-byte R3, host to parasite)"),
    (0x051A, "Type 2: set V+I+J (2-byte R3, parasite to host)"),
    (0x051B, "Type 3: set V+M (2-byte R3, host to parasite)"),
    (0x051C, "Type 4: clear V+M (execute code at address)"),
    (0x051D, "Type 5: clear V+M (release address claim)"),
    (0x051E, "Type 6: set I (define event handler)"),
    (0x051F, "Type 7: clear V+M (transfer and release)"),
]
for addr, desc in _tube_ctrl_entries:
    byte(addr)
    comment(addr, desc, inline=True)
comment(0x0520, "Read channel handle from R2 for BPUT", inline=True)
comment(0x052D, "Read channel handle from R2 for BGET", inline=True)
comment(0x053A, "ROR A: encode carry (error flag) into bit 7", inline=True)
comment(0x053B, "Send carry+data byte to Tube R2", inline=True)
comment(0x053E, "ROL A: restore carry flag", inline=True)
comment(0x0542, "Read open mode from R2 for OSFIND", inline=True)
comment(0x0545, "Mode=0: close file(s)", inline=True)
comment(0x0547, "Save open mode on stack", inline=True)
comment(0x0548, "Read filename string from R2", inline=True)
comment(0x054B, "Restore open mode", inline=True)
comment(0x054F, "Reply with file handle via R2", inline=True)
comment(0x0552, "OSFIND close: read handle from R2", inline=True)
comment(0x0555, "Transfer handle to Y", inline=True)
comment(0x0556, "A=0: close file", inline=True)
comment(0x055B, "Reply with acknowledgement via R2", inline=True)
comment(0x055E, "Read file handle from R2 for OSARGS", inline=True)
comment(0x0562, "Read 4-byte arg + reason from R2 into ZP", inline=True)
comment(0x0564, "Read next param byte from R2", inline=True)
comment(0x0567, "Store param at ZP+X (escape_flag downward)", inline=True)
comment(0x0569, "Decrement index", inline=True)
comment(0x056A, "More params: continue reading", inline=True)
comment(0x0572, "Send result A via R2", inline=True)
comment(0x0575, "X=3: send 4 result bytes", inline=True)
comment(0x0577, "Load result byte from zero page", inline=True)
comment(0x0579, "Send result byte via R2", inline=True)
comment(0x057C, "Decrement byte counter", inline=True)
comment(0x057D, "More bytes: continue sending", inline=True)
comment(0x057F, "Return to Tube main loop", inline=True)
comment(0x0582, "X=0: initialise string buffer index", inline=True)
comment(0x0584, "Y=0: initialise string offset", inline=True)
comment(0x0586, "Read next string byte from R2", inline=True)
comment(0x0589, "Store in string buffer at &0700+Y", inline=True)
comment(0x058C, "Advance string index", inline=True)
comment(0x058D, "Buffer full (256 bytes): done", inline=True)
comment(0x058F, "Check for CR terminator", inline=True)
comment(0x0591, "Not CR: continue reading", inline=True)
comment(0x0593, "Y=7: set XY=&0700 for OSCLI/OSFIND", inline=True)
comment(0x0595, "Return with XY pointing to string buffer", inline=True)
comment(0x0596, "Read command string from R2 into &0700", inline=True)
comment(0x059C, "&7F = success acknowledgement", inline=True)
comment(0x059E, "Poll R2 status until ready", inline=True)
comment(0x05A1, "Bit 6 clear: not ready, loop", inline=True)
comment(0x05A3, "Write byte to R2 data register", inline=True)
comment(0x05A6, "Return to Tube main loop", inline=True)
comment(0x05A9, "Read 16-byte OSFILE control block from R2", inline=True)
comment(0x05AB, "Read next control block byte from R2", inline=True)
comment(0x05AE, "Store at ZP+X (control block)", inline=True)
comment(0x05B0, "Decrement index", inline=True)
comment(0x05B1, "More bytes: continue reading", inline=True)
comment(0x05B3, "Read filename string from R2", inline=True)
comment(0x05B6, "Set filename ptr low = 0", inline=True)
comment(0x05B8, "Set filename ptr high = &07", inline=True)
comment(0x05BA, "Y=0: OSFILE reason code index", inline=True)
comment(0x05BF, "Execute OSFILE", inline=True)
comment(0x05C2, "Send result A via R2", inline=True)
comment(0x05C5, "X=&10: send 16 result bytes", inline=True)
comment(0x05C7, "Load control block byte", inline=True)
comment(0x05C9, "Send control block byte via R2", inline=True)
comment(0x05CC, "Decrement byte counter", inline=True)
comment(0x05CD, "More bytes: continue sending", inline=True)
comment(0x05D1, "X=&0D: read 13-byte OSGBPB ctrl block", inline=True)
comment(0x05D3, "Read next control block byte from R2", inline=True)
comment(0x05D6, "Store at ZP+X (escape_flag downward)", inline=True)
comment(0x05D8, "Decrement index", inline=True)
comment(0x05D9, "More bytes: continue reading", inline=True)
comment(0x05DE, "Y=0: OSGBPB direction/count", inline=True)
comment(0x05E3, "Save result A on stack", inline=True)
comment(0x05E4, "X=&0C: send 12 result bytes", inline=True)
comment(0x05E6, "Load result byte from zero page", inline=True)
comment(0x05E8, "Send result byte via R2", inline=True)
comment(0x05EB, "Decrement byte counter", inline=True)
comment(0x05EC, "More bytes: continue sending", inline=True)
comment(0x05EE, "Recover completion status from stack", inline=True)
comment(0x05EF, "Reply with RDCH-style result", inline=True)
comment(0x05FC, "Poll R2 status for result send", inline=True)
comment(0x05FF, "BVC: page 5/6 boundary straddle", inline=True)
comment(0x0600, "Send carry+status to co-processor via R2", inline=True)
comment(0x0601, "Send X result for 2-param OSBYTE", inline=True)
comment(0x0604, "Return to main event loop", inline=True)
comment(0x0607, "Read X, Y, A from R2 for 3-param OSBYTE", inline=True)
comment(0x060A, "Save in X", inline=True)
comment(0x060B, "Read Y parameter from co-processor", inline=True)
comment(0x060E, "Save in Y", inline=True)
comment(0x060F, "Read A (OSBYTE function code)", inline=True)
comment(0x0612, "Execute OSBYTE A,X,Y", inline=True)
comment(0x0615, "Send carry result to co-processor", inline=True)
comment(0x0617, "OSBYTE &9D (fast Tube BPUT): no result needed", inline=True)
comment(0x0619, "Encode carry (error flag) into bit 7", inline=True)
comment(0x061A, "Send carry+status byte via R2", inline=True)
comment(0x061D, "Poll R2 status for ready", inline=True)
comment(0x0620, "Not ready: keep polling", inline=True)
comment(0x0622, "Send Y result, then fall through to send X", inline=True)
comment(0x0625, "BVS always: jump to send X via R2", inline=True)
comment(0x0627, "Overlapping entry: &20 = JSR c06c5 (OSWORD)", inline=True)
comment(0x062A, "Save OSWORD number in Y", inline=True)
comment(0x062B, "Poll R2 status for data ready", inline=True)
comment(0x062E, "Not ready: keep polling", inline=True)
comment(0x0630, "Read param block length from R2", inline=True)
comment(0x0633, "DEX: length 0 means no params to read", inline=True)
comment(0x0634, "No params (length=0): skip read loop", inline=True)
comment(0x0636, "Poll R2 status for data ready", inline=True)
comment(0x0639, "Not ready: keep polling", inline=True)
comment(0x063B, "Read param byte from R2", inline=True)
comment(0x063E, "Store param bytes into block at &0128", inline=True)
comment(0x0641, "Next param byte (descending)", inline=True)
comment(0x0642, "Loop until all params read", inline=True)
comment(0x0644, "Restore OSWORD number from Y", inline=True)
comment(0x0645, "XY=&0128: param block address for OSWORD", inline=True)
comment(0x0647, "Y=&01: param block at &0128", inline=True)
comment(0x0649, "Send result marker via R2", inline=True)
comment(0x064C, "Poll R2 status for ready", inline=True)
comment(0x064F, "Not ready: keep polling", inline=True)
comment(0x0651, "Read result block length from R2", inline=True)
comment(0x0654, "Decrement result byte counter", inline=True)
comment(0x0655, "No results to send: return to main loop", inline=True)
comment(0x0657, "Send result block bytes from &0128 via R2", inline=True)
comment(0x065A, "Poll R2 status for ready", inline=True)
comment(0x065D, "Not ready: keep polling", inline=True)
comment(0x065F, "Send result byte via R2", inline=True)
comment(0x0662, "Next result byte (descending)", inline=True)
comment(0x0663, "Loop until all results sent", inline=True)
comment(0x0665, "Return to main event loop", inline=True)
comment(0x0668, "Read 5-byte OSWORD 0 control block from R2", inline=True)
comment(0x066A, "Read control block byte from R2", inline=True)
comment(0x066D, "Store in zero page params", inline=True)
comment(0x066F, "Next byte (descending)", inline=True)
comment(0x0670, "Loop until all 5 bytes read", inline=True)
comment(0x0672, "X=0 after loop, A=0 for OSWORD 0 (read line)", inline=True)
comment(0x0673, "Y=0 for OSWORD 0", inline=True)
comment(0x0675, "A=0: OSWORD 0 (read line)", inline=True)
comment(0x0676, "Read input line from keyboard", inline=True)
comment(0x0679, "C=0: line read OK; C=1: escape pressed", inline=True)
comment(0x067B, "&FF = escape/error signal to co-processor", inline=True)
comment(0x067D, "Escape: send &FF error to co-processor", inline=True)
comment(0x0680, "X=0: start of input buffer at &0700", inline=True)
comment(0x0682, "&7F = line read successfully", inline=True)
comment(0x0684, "Send &7F (success) to co-processor", inline=True)
comment(0x0687, "Load char from input buffer", inline=True)
comment(0x068A, "Send char to co-processor", inline=True)
comment(0x068D, "Next character", inline=True)
comment(0x068E, "Loop until CR terminator sent", inline=True)
comment(0x0690, "Loop until CR terminator sent", inline=True)
comment(0x0692, "Return to main event loop", inline=True)
comment(0x0695, "Poll R2 status (bit 6 = ready)", inline=True)
comment(0x0698, "Not ready: keep polling", inline=True)
comment(0x069A, "Write A to Tube R2 data register", inline=True)
comment(0x069D, "Return to caller", inline=True)
comment(0x069E, "Poll R4 status (bit 6 = ready)", inline=True)
comment(0x06A1, "Not ready: keep polling", inline=True)
comment(0x06A3, "Write A to Tube R4 data register", inline=True)
comment(0x06A6, "Return to caller", inline=True)
comment(0x06A7, "Check OS escape flag at &FF", inline=True)
comment(0x06A9, "SEC+ROR: put bit 7 of &FF into carry+bit 7", inline=True)
comment(0x06AA, "ROR: shift escape bit 7 to carry", inline=True)
comment(0x06AB, "Escape set: forward to co-processor via R1", inline=True)
comment(0x06AD, "EVNTV: forward event A, Y, X to co-processor", inline=True)
comment(0x06AE, "Send &00 prefix (event notification)", inline=True)
comment(0x06B0, "Send event number via R1", inline=True)
comment(0x06B3, "Y value for event", inline=True)
comment(0x06B4, "Send Y via R1", inline=True)
comment(0x06B7, "X value for event", inline=True)
comment(0x06B8, "Send X via R1", inline=True)
comment(0x06BB, "Restore A (event type)", inline=True)
comment(0x06BC, "Poll R1 status (bit 6 = ready)", inline=True)
comment(0x06BF, "Not ready: keep polling", inline=True)
comment(0x06C1, "Write A to Tube R1 data register", inline=True)
comment(0x06C4, "Return to caller", inline=True)
comment(0x06C5, "Poll R2 status (bit 7 = ready)", inline=True)
comment(0x06C8, "Not ready: keep polling", inline=True)
comment(0x06CA, "Read data byte from R2", inline=True)
comment(0x06CD, "Return with byte in A", inline=True)
comment(0x06CE, "Is byte &FE (VDU stream start)?", inline=True)
comment(0x06D0, "Below &FE: normal byte", inline=True)
comment(0x06D2, "&FF: set up event/break vectors", inline=True)
comment(0x06D4, "&FE: check Y parameter", inline=True)
comment(0x06D6, "Y=0: treat as normal byte", inline=True)
comment(0x06D8, "X=6: six extra pages", inline=True)
comment(0x06DA, "OSBYTE &14: explode char defs", inline=True)
comment(0x06DF, "Poll R1 status (bit 6 = ready)", inline=True)
comment(0x06E2, "Not ready: keep polling", inline=True)
comment(0x06E4, "Read byte from Tube R1", inline=True)
comment(0x06E7, "Zero: end of VDU stream", inline=True)
comment(0x06EC, "Loop back to read next R1 byte", inline=True)
comment(0x06EF, "EVNTV low byte (&AD)", inline=True)
comment(0x06F1, "Store in EVNTV vector low", inline=True)
comment(0x06F4, "EVNTV high byte (page 6)", inline=True)
comment(0x06F6, "Store in EVNTV vector high", inline=True)
comment(0x06F9, "BRKV low byte (&16)", inline=True)
comment(0x06FB, "Store in BRKV vector", inline=True)
comment(0x06FE, "A=0", inline=True)
comment(0x8003, "JMP service_handler", inline=True)
comment(0x8006, "ROM type: service + language", inline=True)
comment(0x8014, "Null terminator before copyright", inline=True)
comment(0x8023, "A=4: CB1 bit mask for IFR test", inline=True)
comment(0x8025, "Test IFR bit 2: CB1 active edge", inline=True)
comment(0x8028, "CB1 set: shift register complete", inline=True)
comment(0x802A, "A=5: not our interrupt, pass on", inline=True)
comment(0x802C, "Return service code 5 to MOS", inline=True)
comment(0x802D, "Save X on stack", inline=True)
comment(0x802E, "Push saved X", inline=True)
comment(0x802F, "Save Y on stack", inline=True)
comment(0x8030, "Push saved Y", inline=True)
comment(0x8031, "Read ACR for shift register restore", inline=True)
comment(0x8034, "Clear SR mode bits (2-4)", inline=True)
comment(0x8036, "Restore saved SR mode from ws_0d64", inline=True)
comment(0x8039, "Write restored ACR to system VIA", inline=True)
comment(0x803C, "Read SR to clear shift register IRQ", inline=True)
comment(0x803F, "A=4: CB1 bit mask", inline=True)
comment(0x8041, "Clear CB1 interrupt flag in IFR", inline=True)
comment(0x8044, "Disable CB1 interrupt in IER", inline=True)
comment(0x8047, "Load TX operation type for dispatch", inline=True)
comment(0x804A, "Copy to A for sign test", inline=True)
comment(0x804B, "Bit 7 set: dispatch via table", inline=True)
comment(0x804D, "Y=&FE: Econet event number", inline=True)
comment(0x804F, "Generate event and exit", inline=True)
comment(0x8052, "Y >= &86: above dispatch range", inline=True)
comment(0x8054, "Out of range: skip protection", inline=True)
comment(0x8056, "Save current JSR protection mask", inline=True)
comment(0x8059, "Backup to saved_jsr_mask", inline=True)
comment(0x805C, "Set protection bits 2-4", inline=True)
comment(0x805E, "Apply protection during dispatch", inline=True)
comment(0x8061, "Push return addr high (&85)", inline=True)
comment(0x8063, "High byte on stack for RTS", inline=True)
comment(0x8064, "Load dispatch target low byte", inline=True)
comment(0x8067, "Low byte on stack for RTS", inline=True)
comment(0x8068, "RTS = dispatch to PHA'd address", inline=True)
comment(0x8069, "INTOFF: read station ID, disable NMIs", inline=True)
comment(0x806C, "Full ADLC hardware reset", inline=True)
comment(0x806F, "OSBYTE &EA: check Tube co-processor", inline=True)
comment(0x8071, "X=0 for OSBYTE", inline=True)
comment(0x8073, "Clear Econet init flag before setup", inline=True)
comment(0x807C, "OSBYTE &8F: issue service request", inline=True)
comment(0x807E, "X=&0C: NMI claim service", inline=True)
comment(0x8079, "Store Tube presence flag from OSBYTE &EA", inline=True)
comment(0x8083, "Y=5: NMI claim service number", inline=True)
comment(0x8085, "Check if NMI service was claimed (Y changed)", inline=True)
comment(0x8087, "Service claimed by other ROM: skip init", inline=True)
comment(0x8089, "Copy 32 bytes of NMI shim from ROM to &0D00", inline=True)
comment(0x808B, "Read byte from NMI shim ROM source", inline=True)
comment(0x808E, "Write to NMI shim RAM at &0D00", inline=True)
comment(0x8091, "Next byte (descending)", inline=True)
comment(0x8092, "Loop until all 32 bytes copied", inline=True)
comment(0x8094, "Patch current ROM bank into NMI shim", inline=True)
comment(0x8096, "Self-modifying code: ROM bank at &0D07", inline=True)
comment(0x8099, "Clear source network (Y=0 from copy loop)", inline=True)
comment(0x809C, "Clear Tube release flag", inline=True)
comment(0x809E, "Clear TX operation type", inline=True)
comment(0x80A1, "Read station ID (and disable NMIs)", inline=True)
comment(0x80A4, "Set own station as TX source", inline=True)
comment(0x80A7, "&80 = Econet initialised", inline=True)
comment(0x80A9, "Mark TX as complete (ready)", inline=True)
comment(0x80AC, "Mark Econet as initialised", inline=True)
comment(0x80AF, "INTON: re-enable NMIs (&FE20 read side effect)", inline=True)
comment(0x80B2, "Return", inline=True)
comment(0x80B3, "A=&01: mask for SR2 bit0 (AP = Address Present)", inline=True)
comment(0x80B5, "BIT SR2: Z = A AND SR2 -- tests if AP is set", inline=True)
comment(0x80B8, "AP not set, no incoming data -- check for errors", inline=True)
comment(0x80BA, "Read first RX byte (destination station address)", inline=True)
comment(0x80BD, "Compare to our station ID (&FE18 read = INTOFF, disables NMIs)", inline=True)
comment(0x80C0, "Match -- accept frame", inline=True)
comment(0x80C2, "Check for broadcast address (&FF)", inline=True)
comment(0x80C4, "Neither our address nor broadcast -- reject frame", inline=True)
comment(0x80C6, "Flag &40 = broadcast frame", inline=True)
comment(0x80C8, "Clear TX flags for new reception", inline=True)
comment(0x80CB, "Install nmi_rx_scout_net NMI handler", inline=True)
comment(0x80CD, "Install next handler and RTI", inline=True)
comment(0x80D0, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x80D3, "No RDA -- check errors", inline=True)
comment(0x80D5, "Read destination network byte", inline=True)
comment(0x80D8, "Network = 0 -- local network, accept", inline=True)
comment(0x80DA, "EOR &FF: test if network = &FF (broadcast)", inline=True)
comment(0x80DC, "Broadcast network -- accept", inline=True)
comment(0x80DE, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", inline=True)
comment(0x80E0, "Write CR1 to discontinue RX", inline=True)
comment(0x80E3, "Return to idle scout listening", inline=True)
comment(0x80E6, "Network = &FF broadcast: clear &0D4A", inline=True)
comment(0x80E9, "Store Y offset for scout data buffer", inline=True)
comment(0x80EB, "Install scout data handler (&8102)", inline=True)
comment(0x80ED, "High byte of scout data handler", inline=True)
comment(0x80EF, "Install scout data loop and RTI", inline=True)
comment(0x80F2, "Read SR2", inline=True)
comment(0x80F5, "Test AP (b0) | RDA (b7)", inline=True)
comment(0x80F7, "Neither set -- clean end, discard frame", inline=True)
comment(0x80F9, "Unexpected data/status: full ADLC reset", inline=True)
comment(0x80FC, "Discard and return to idle", inline=True)
comment(0x80FF, "Gentle discard: RX_DISCONTINUE", inline=True)
comment(0x8102, "Y = buffer offset", inline=True)
comment(0x8104, "Read SR2", inline=True)
comment(0x8107, "No RDA -- error handler", inline=True)
comment(0x8109, "Read data byte from RX FIFO", inline=True)
comment(0x810C, "Store at &0D3D+Y (scout buffer)", inline=True)
comment(0x810F, "Advance buffer index", inline=True)
comment(0x8110, "Read SR2 again (FV detection point)", inline=True)
comment(0x8113, "RDA set -- more data, read second byte", inline=True)
comment(0x8115, "SR2 non-zero (FV or other) -- scout completion", inline=True)
comment(0x8117, "Read second byte of pair", inline=True)
comment(0x811A, "Store at &0D3D+Y", inline=True)
comment(0x811D, "Advance and check buffer limit", inline=True)
comment(0x811E, "Copied all 12 scout bytes?", inline=True)
comment(0x8120, "Buffer full (Y=12) -- force completion", inline=True)
comment(0x8122, "Save final buffer offset", inline=True)
comment(0x8124, "Read SR2 for next pair", inline=True)
comment(0x8127, "SR2 non-zero -- loop back for more bytes", inline=True)
comment(0x8129, "SR2 = 0 -- RTI, wait for next NMI", inline=True)
comment(0x812C, "Save Y for next iteration", inline=True)
comment(0x812E, "Write CR1", inline=True)
comment(0x8131, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", inline=True)
comment(0x8133, "Write CR2", inline=True)
comment(0x8136, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x8138, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x813B, "No FV -- not a valid frame end, error", inline=True)
comment(0x813D, "FV set but no RDA -- missing last byte, error", inline=True)
comment(0x813F, "Read last byte from RX FIFO", inline=True)
comment(0x8142, "Store last byte at &0D3D+Y", inline=True)
comment(0x8145, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", inline=True)
comment(0x8147, "Write CR1: switch to TX mode", inline=True)
comment(0x814A, "Set bit7 of need_release_tube flag", inline=True)
comment(0x814B, "Rotate C=1 into bit7: mark Tube release needed", inline=True)
comment(0x814D, "Check port byte: 0 = immediate op, non-zero = data transfer", inline=True)
comment(0x8150, "Port non-zero -- look for matching receive block", inline=True)
comment(0x8152, "Port = 0 -- immediate operation handler", inline=True)
comment(0x8155, "Check if broadcast (bit6 of tx_flags)", inline=True)
comment(0x8158, "Not broadcast -- skip CR2 setup", inline=True)
comment(0x815A, "CR2=&07: broadcast prep", inline=True)
comment(0x815C, "Write CR2: broadcast frame prep", inline=True)
comment(0x815F, "Check if RX port list active (bit7)", inline=True)
comment(0x8162, "No active ports -- try NFS workspace", inline=True)
comment(0x8164, "Start scanning port list at page &C0", inline=True)
comment(0x8166, "Y=0: start offset within each port slot", inline=True)
comment(0x8168, "Store page to workspace pointer low", inline=True)
comment(0x816A, "Store page high byte for slot scanning", inline=True)
comment(0x816C, "Y=0: read control byte from start of slot", inline=True)
comment(0x816E, "Read port control byte from slot", inline=True)
comment(0x8170, "Zero = end of port list, no match", inline=True)
comment(0x8172, "&7F = any-port wildcard", inline=True)
comment(0x8174, "Not wildcard -- check specific port match", inline=True)
comment(0x8176, "Y=1: advance to port byte in slot", inline=True)
comment(0x8177, "Read port number from slot (offset 1)", inline=True)
comment(0x8179, "Zero port in slot = match any port", inline=True)
comment(0x817B, "Check if port matches this slot", inline=True)
comment(0x817E, "Port mismatch -- try next slot", inline=True)
comment(0x8180, "Y=2: advance to station byte", inline=True)
comment(0x8181, "Read station filter from slot (offset 2)", inline=True)
comment(0x8183, "Zero station = match any station, accept", inline=True)
comment(0x8185, "Check if source station matches", inline=True)
comment(0x8188, "Station mismatch -- try next slot", inline=True)
comment(0x818A, "Y=3: advance to network byte", inline=True)
comment(0x818B, "Read network filter from slot (offset 3)", inline=True)
comment(0x818D, "Zero = accept any network", inline=True)
comment(0x818F, "Check if source network matches", inline=True)
comment(0x8192, "Network matches or zero = accept", inline=True)
comment(0x8194, "Check if NFS workspace search pending", inline=True)
comment(0x8196, "No NFS workspace -- try fallback path", inline=True)
comment(0x8198, "Load current slot base address", inline=True)
comment(0x819A, "CLC for 12-byte slot advance", inline=True)
comment(0x819B, "Advance to next 12-byte port slot", inline=True)
comment(0x819D, "Update workspace pointer to next slot", inline=True)
comment(0x819F, "Always branches (page &C0 won't overflow)", inline=True)
comment(0x81A1, "No match found -- discard frame", inline=True)
comment(0x81A4, "Try NFS workspace if paged list exhausted", inline=True)
comment(0x81A7, "No NFS workspace RX (bit6 clear) -- discard", inline=True)
comment(0x81A9, "NFS workspace starts at offset 0 in page", inline=True)
comment(0x81AB, "NFS workspace high byte for port list", inline=True)
comment(0x81AD, "Scan NFS workspace port list", inline=True)
comment(0x81AF, "Match found: set scout_status = 3", inline=True)
comment(0x81B1, "Record match for completion handler", inline=True)
comment(0x81B4, "Calculate transfer parameters", inline=True)
comment(0x81B7, "C=0: no Tube claimed -- discard", inline=True)
comment(0x81B9, "Check broadcast flag for ACK path", inline=True)
comment(0x81BC, "Not broadcast -- normal ACK path", inline=True)
comment(0x81BE, "Broadcast: different completion path", inline=True)
comment(0x81C1, "CR1=&44: RX_RESET | TIE", inline=True)
comment(0x81C3, "Write CR1: TX mode for ACK", inline=True)
comment(0x81C6, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", inline=True)
comment(0x81C8, "Write CR2: enable TX with PSE", inline=True)
comment(0x81CB, "Install data_rx_setup at &81D2", inline=True)
comment(0x81CD, "High byte of data_rx_setup handler", inline=True)
comment(0x81CF, "Send ACK with data_rx_setup as next NMI", inline=True)
comment(0x81D2, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", inline=True)
comment(0x81D4, "Write CR1: switch to RX for data frame", inline=True)
comment(0x81D7, "Install nmi_data_rx at &81DC", inline=True)
comment(0x81D9, "Install nmi_data_rx and return from NMI", inline=True)
comment(0x81DC, "Read SR2 for AP check", inline=True)
comment(0x81DE, "BIT SR2: test AP bit", inline=True)
comment(0x81E1, "No AP: wrong frame or error", inline=True)
comment(0x81E3, "Read first byte (dest station)", inline=True)
comment(0x81E6, "Compare to our station ID (INTOFF)", inline=True)
comment(0x81E9, "Not for us: error path", inline=True)
comment(0x81EB, "Install net check handler at &81F0", inline=True)
comment(0x81ED, "Set NMI vector via RAM shim", inline=True)
comment(0x81F0, "Validate source network = 0", inline=True)
comment(0x81F3, "SR2 bit7 clear: no data ready -- error", inline=True)
comment(0x81F5, "Read dest network byte", inline=True)
comment(0x81F8, "Network != 0: wrong network -- error", inline=True)
comment(0x81FA, "Install skip handler at &8206", inline=True)
comment(0x81FC, "High byte of &8206 handler", inline=True)
comment(0x81FE, "SR1 bit7: IRQ, data already waiting", inline=True)
comment(0x8201, "Data ready: skip directly, no RTI", inline=True)
comment(0x8203, "Install handler and return via RTI", inline=True)
comment(0x8206, "Skip control and port bytes (already known from scout)", inline=True)
comment(0x8209, "SR2 bit7 clear: error", inline=True)
comment(0x820B, "Discard control byte", inline=True)
comment(0x820E, "Discard port byte", inline=True)
comment(0x8211, "A=2: Tube transfer flag mask", inline=True)
comment(0x8213, "Check if Tube transfer active", inline=True)
comment(0x8216, "Tube active: use Tube RX path", inline=True)
comment(0x8218, "Install bulk read at &8239", inline=True)
comment(0x821A, "High byte of &8239 handler", inline=True)
comment(0x821C, "SR1 bit7: more data already waiting?", inline=True)
comment(0x821F, "Yes: enter bulk read directly", inline=True)
comment(0x8221, "No: install handler and RTI", inline=True)
comment(0x8224, "Tube: install Tube RX at &8296", inline=True)
comment(0x8226, "High byte of &8296 handler", inline=True)
comment(0x8228, "Install Tube handler and RTI", inline=True)
comment(0x822B, "Check tx_flags for error path", inline=True)
comment(0x822E, "Bit7 clear: RX error path", inline=True)
comment(0x8230, "Bit7 set: TX result = not listening", inline=True)
comment(0x8233, "Full ADLC reset on RX error", inline=True)
comment(0x8236, "Discard and return to idle listen", inline=True)
comment(0x8239, "Y = buffer offset, resume from last position", inline=True)
comment(0x823B, "Read SR2 for next pair", inline=True)
comment(0x823E, "SR2 bit7 clear: frame complete (FV)", inline=True)
comment(0x8240, "Read first byte of pair from RX FIFO", inline=True)
comment(0x8243, "Store byte to buffer", inline=True)
comment(0x8245, "Advance buffer offset", inline=True)
comment(0x8246, "Y != 0: no page boundary crossing", inline=True)
comment(0x8248, "Crossed page: increment buffer high byte", inline=True)
comment(0x824A, "Decrement remaining page count", inline=True)
comment(0x824C, "No pages left: handle as complete", inline=True)
comment(0x824E, "Read SR2 between byte pairs", inline=True)
comment(0x8251, "SR2 bit7 set: more data available", inline=True)
comment(0x8253, "SR2 non-zero, bit7 clear: frame done", inline=True)
comment(0x8255, "Read second byte of pair from RX FIFO", inline=True)
comment(0x8258, "Store byte to buffer", inline=True)
comment(0x825A, "Advance buffer offset", inline=True)
comment(0x825B, "Save updated buffer position", inline=True)
comment(0x825D, "Y != 0: no page boundary crossing", inline=True)
comment(0x825F, "Crossed page: increment buffer high byte", inline=True)
comment(0x8261, "Decrement remaining page count", inline=True)
comment(0x8263, "No pages left: frame complete", inline=True)
comment(0x8265, "Read SR2 for next iteration", inline=True)
comment(0x8268, "SR2 non-zero: more data, loop back", inline=True)
comment(0x826A, "SR2=0: no more data yet, wait for NMI", inline=True)
comment(0x826D, "CR1=&00: disable all interrupts", inline=True)
comment(0x826F, "Write CR2: disable PSE for bit testing", inline=True)
comment(0x8272, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x8274, "Write CR1: disable all interrupts", inline=True)
comment(0x8277, "Save Y (byte count from data RX loop)", inline=True)
comment(0x8279, "A=&02: FV mask", inline=True)
comment(0x827B, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x827E, "No FV -- error", inline=True)
comment(0x8280, "FV set, no RDA -- proceed to ACK", inline=True)
comment(0x8282, "Check if buffer space remains", inline=True)
comment(0x8284, "No buffer space: error/discard frame", inline=True)
comment(0x8286, "FV+RDA: read and store last data byte", inline=True)
comment(0x8289, "Y = current buffer write offset", inline=True)
comment(0x828B, "Store last byte in port receive buffer", inline=True)
comment(0x828D, "Advance buffer write offset", inline=True)
comment(0x828F, "No page wrap: proceed to send ACK", inline=True)
comment(0x8291, "Page boundary: advance buffer page", inline=True)
comment(0x8293, "Send ACK frame to complete handshake", inline=True)
comment(0x8296, "Read SR2 for Tube data receive path", inline=True)
comment(0x8299, "RDA clear: no more data, frame complete", inline=True)
comment(0x829B, "Read data byte from ADLC RX FIFO", inline=True)
comment(0x829E, "Check buffer limits and transfer size", inline=True)
comment(0x82A1, "Zero: buffer full, handle as error", inline=True)
comment(0x82A3, "Send byte to Tube data register 3", inline=True)
comment(0x82A6, "Read second data byte (paired transfer)", inline=True)
comment(0x82A9, "Send second byte to Tube", inline=True)
comment(0x82AC, "Check limits after byte pair", inline=True)
comment(0x82AF, "Zero: Tube transfer complete", inline=True)
comment(0x82B1, "Re-read SR2 for next byte pair", inline=True)
comment(0x82B4, "More data available: continue loop", inline=True)
comment(0x82B6, "Unexpected end: return from NMI", inline=True)
comment(0x82B9, "CR1=&00: disable all interrupts", inline=True)
comment(0x82BB, "Write CR1 for individual bit testing", inline=True)
comment(0x82BE, "CR2=&84: disable PSE", inline=True)
comment(0x82C0, "Write CR2: same pattern as main path", inline=True)
comment(0x82C3, "A=&02: FV mask for Tube completion", inline=True)
comment(0x82C5, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x82C8, "No FV: incomplete frame, error", inline=True)
comment(0x82CA, "FV set, no RDA: proceed to ACK", inline=True)
comment(0x82CC, "Check if any buffer was allocated", inline=True)
comment(0x82CE, "OR all 4 buffer pointer bytes together", inline=True)
comment(0x82D0, "Check buffer low byte", inline=True)
comment(0x82D2, "Check buffer high byte", inline=True)
comment(0x82D4, "All zero (null buffer): error", inline=True)
comment(0x82D6, "Read extra trailing byte from FIFO", inline=True)
comment(0x82D9, "Save extra byte at &0D5D for later use", inline=True)
comment(0x82DC, "Bit5 = extra data byte available flag", inline=True)
comment(0x82DE, "Set extra byte flag in tx_flags", inline=True)
comment(0x82E1, "Store updated flags", inline=True)
comment(0x82E4, "Load TX flags to check ACK type", inline=True)
comment(0x82E7, "Bit7 clear: normal scout ACK", inline=True)
comment(0x82E9, "Final ACK: call completion handler", inline=True)
comment(0x82EC, "Jump to TX success result", inline=True)
comment(0x82EF, "CR1=&44: RX_RESET | TIE (switch to TX mode)", inline=True)
comment(0x82F1, "Write CR1: switch to TX mode", inline=True)
comment(0x82F4, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x82F6, "Write CR2: enable TX with status clear", inline=True)
comment(0x82F9, "Install saved next handler (&838B for scout ACK)", inline=True)
comment(0x82FB, "High byte of post-ACK handler", inline=True)
comment(0x82FD, "Store next handler low byte", inline=True)
comment(0x8300, "Store next handler high byte", inline=True)
comment(0x8303, "Load dest station from RX scout buffer", inline=True)
comment(0x8306, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x8309, "TDRA not ready -- error", inline=True)
comment(0x830B, "Write dest station to TX FIFO", inline=True)
comment(0x830E, "Write dest network to TX FIFO", inline=True)
comment(0x8311, "Write dest net byte to FIFO", inline=True)
comment(0x8314, "Install handler at &831B (write src addr)", inline=True)
comment(0x8316, "High byte of nmi_ack_tx_src", inline=True)
comment(0x8318, "Set NMI vector to ack_tx_src handler", inline=True)
comment(0x831B, "Load our station ID (also INTOFF)", inline=True)
comment(0x831E, "BIT SR1: test TDRA", inline=True)
comment(0x8321, "TDRA not ready -- error", inline=True)
comment(0x8323, "Write our station to TX FIFO", inline=True)
comment(0x8326, "Write network=0 to TX FIFO", inline=True)
comment(0x8328, "Write network=0 (local) to TX FIFO", inline=True)
comment(0x832B, "Check tx_flags for data phase", inline=True)
comment(0x832E, "bit7 set: start data TX phase", inline=True)
comment(0x8330, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x8332, "Write CR2 to clear status after ACK TX", inline=True)
comment(0x8335, "Install saved handler from &0D4B/&0D4C", inline=True)
comment(0x8338, "Load saved next handler high byte", inline=True)
comment(0x833B, "Install next NMI handler", inline=True)
comment(0x833E, "Jump to start data TX phase", inline=True)
comment(0x8341, "Jump to error handler", inline=True)
comment(0x8344, "A=2: test bit1 of tx_flags", inline=True)
comment(0x8346, "BIT tx_flags: check data transfer bit", inline=True)
comment(0x8349, "Bit1 clear: no transfer -- return", inline=True)
comment(0x834B, "CLC: init carry for 4-byte add", inline=True)
comment(0x834C, "Save carry on stack for loop", inline=True)
comment(0x834D, "Y=8: RXCB high pointer offset", inline=True)
comment(0x834F, "Load RXCB[Y] (buffer pointer byte)", inline=True)
comment(0x8351, "Restore carry from stack", inline=True)
comment(0x8352, "Add transfer count byte", inline=True)
comment(0x8355, "Store updated pointer back to RXCB", inline=True)
comment(0x8357, "Next byte", inline=True)
comment(0x8358, "Save carry for next iteration", inline=True)
comment(0x8359, "Done 4 bytes? (Y reaches &0C)", inline=True)
comment(0x835B, "No: continue adding", inline=True)
comment(0x835D, "Discard final carry", inline=True)
comment(0x835E, "A=&20: test bit5 of tx_flags", inline=True)
comment(0x8360, "BIT tx_flags: check Tube bit", inline=True)
comment(0x8363, "No Tube: skip Tube update", inline=True)
comment(0x8365, "Save X on stack", inline=True)
comment(0x8366, "Push X", inline=True)
comment(0x8367, "A=8: offset for Tube address", inline=True)
comment(0x8369, "CLC for address calculation", inline=True)
comment(0x836A, "Add workspace base offset", inline=True)
comment(0x836C, "X = address low for Tube claim", inline=True)
comment(0x836D, "Y = address high for Tube claim", inline=True)
comment(0x836F, "A=1: Tube claim type (read)", inline=True)
comment(0x8371, "Claim Tube address for transfer", inline=True)
comment(0x8374, "Load extra RX data byte", inline=True)
comment(0x8377, "Send to Tube via R3", inline=True)
comment(0x837A, "SEC: init carry for increment", inline=True)
comment(0x837B, "Y=8: start at high pointer", inline=True)
comment(0x837D, "A=0: add carry only (increment)", inline=True)
comment(0x837F, "Add carry to pointer byte", inline=True)
comment(0x8381, "Store back to RXCB", inline=True)
comment(0x8383, "Next byte", inline=True)
comment(0x8384, "Keep going while carry propagates", inline=True)
comment(0x8386, "Restore X from stack", inline=True)
comment(0x8387, "Transfer to X register", inline=True)
comment(0x8388, "A=&FF: return value (transfer done)", inline=True)
comment(0x838A, "Return", inline=True)
comment(0x838B, "Load received port byte", inline=True)
comment(0x838E, "Port != 0: data transfer frame", inline=True)
comment(0x8390, "Port=0: load control byte", inline=True)
comment(0x8393, "Ctrl = &82 (POKE)?", inline=True)
comment(0x8395, "Yes: POKE also needs data transfer", inline=True)
comment(0x8397, "Other port-0 ops: immediate dispatch", inline=True)
comment(0x839A, "Update buffer pointer and check for Tube", inline=True)
comment(0x839D, "Transfer not done: skip buffer update", inline=True)
comment(0x839F, "Load buffer bytes remaining", inline=True)
comment(0x83A1, "CLC for address add", inline=True)
comment(0x83A2, "Add to buffer base address", inline=True)
comment(0x83A4, "No carry: skip high byte increment", inline=True)
comment(0x83A6, "Carry: increment buffer high byte", inline=True)
comment(0x83A8, "Y=8: store updated buffer position", inline=True)
comment(0x83AA, "Store updated low byte to RXCB", inline=True)
comment(0x83AC, "Y=9: buffer high byte offset", inline=True)
comment(0x83AD, "Load updated buffer high byte", inline=True)
comment(0x83AF, "Store high byte to RXCB", inline=True)
comment(0x83B1, "Check port byte again", inline=True)
comment(0x83B4, "Port=0: immediate op, discard+listen", inline=True)
comment(0x83B6, "Load source network from scout buffer", inline=True)
comment(0x83B9, "Y=3: RXCB source network offset", inline=True)
comment(0x83BB, "Store source network to RXCB", inline=True)
comment(0x83BD, "Y=2: source station offset", inline=True)
comment(0x83BE, "Load source station from scout buffer", inline=True)
comment(0x83C1, "Store source station to RXCB", inline=True)
comment(0x83C3, "Y=1: port byte offset", inline=True)
comment(0x83C4, "Load port byte", inline=True)
comment(0x83C7, "Store port to RXCB", inline=True)
comment(0x83C9, "Y=0: control/flag byte offset", inline=True)
comment(0x83CA, "Load control byte from scout", inline=True)
comment(0x83CD, "Set bit7 = reception complete flag", inline=True)
comment(0x83CF, "Store to RXCB (marks CB as complete)", inline=True)
comment(0x83D1, "Load callback event flags", inline=True)
comment(0x83D4, "Shift bit 0 into carry", inline=True)
comment(0x83D5, "Bit 0 clear: no callback, skip to reset", inline=True)
comment(0x83D7, "Set carry for subtraction", inline=True)
comment(0x83D8, "Load RXCB workspace pointer low byte", inline=True)
comment(0x83DA, "Count slots", inline=True)
comment(0x83DB, "Subtract 12 bytes per RXCB slot", inline=True)
comment(0x83DD, "Loop until pointer exhausted", inline=True)
comment(0x83DF, "Adjust for off-by-one", inline=True)
comment(0x83E0, "Check slot index >= 3", inline=True)
comment(0x83E2, "Slot < 3: no callback, skip to reset", inline=True)
comment(0x83E7, "Pass slot index as callback parameter", inline=True)
comment(0x83E8, "Jump to TX completion with slot index", inline=True)
comment(0x83F1, "A=&B3: low byte of nmi_rx_scout", inline=True)
comment(0x83F3, "Y=&80: high byte of nmi_rx_scout", inline=True)
comment(0x83F5, "Install nmi_rx_scout as NMI handler", inline=True)
comment(0x83F8, "Tube flag bit 1 AND tx_flags bit 1", inline=True)
comment(0x83FA, "Check if Tube transfer active", inline=True)
comment(0x83FD, "Test tx_flags for Tube transfer", inline=True)
comment(0x8400, "No Tube transfer active -- skip release", inline=True)
comment(0x8402, "Release Tube claim before discarding", inline=True)
comment(0x8405, "Return", inline=True)
comment(0x8406, "Save X on stack", inline=True)
comment(0x8407, "Push X", inline=True)
comment(0x8408, "X=4: start at scout byte offset 4", inline=True)
comment(0x840A, "A=2: Tube transfer check mask", inline=True)
comment(0x840C, "BIT tx_flags: check Tube bit", inline=True)
comment(0x840F, "Tube active: use R3 write path", inline=True)
comment(0x8411, "Y = current buffer position", inline=True)
comment(0x8413, "Load scout data byte", inline=True)
comment(0x8416, "Store to port buffer", inline=True)
comment(0x8418, "Advance buffer pointer", inline=True)
comment(0x8419, "No page crossing", inline=True)
comment(0x841B, "Page crossing: inc buffer high byte", inline=True)
comment(0x841D, "Decrement remaining page count", inline=True)
comment(0x841F, "No pages left: overflow", inline=True)
comment(0x8421, "Next scout data byte", inline=True)
comment(0x8422, "Save updated buffer position", inline=True)
comment(0x8424, "Done all scout data? (X reaches &0C)", inline=True)
comment(0x8426, "No: continue copying", inline=True)
comment(0x8428, "Restore X from stack", inline=True)
comment(0x8429, "Transfer to X register", inline=True)
comment(0x842A, "Jump to completion handler", inline=True)
comment(0x842D, "Tube path: load scout data byte", inline=True)
comment(0x8430, "Send byte to Tube via R3", inline=True)
comment(0x8433, "Increment buffer position counters", inline=True)
comment(0x8436, "Counter overflow: handle end of buffer", inline=True)
comment(0x8438, "Next scout data byte", inline=True)
comment(0x8439, "Done all scout data?", inline=True)
comment(0x843B, "No: continue Tube writes", inline=True)
comment(0x843F, "Check if Tube needs releasing", inline=True)
comment(0x8441, "Bit7 set: already released", inline=True)
comment(0x8443, "A=&82: Tube release claim type", inline=True)
comment(0x8445, "Release Tube address claim", inline=True)
comment(0x8448, "Clear release flag (LSR clears bit7)", inline=True)
comment(0x844A, "Return", inline=True)
comment(0x844B, "Control byte &81-&88 range check", inline=True)
comment(0x844E, "Below &81: not an immediate op", inline=True)
comment(0x8450, "Out of range low: jump to discard", inline=True)
comment(0x8452, "Above &88: not an immediate op", inline=True)
comment(0x8454, "Out of range high: jump to discard", inline=True)
comment(0x8456, "HALT(&87)/CONTINUE(&88) skip protection", inline=True)
comment(0x8458, "Ctrl >= &87: dispatch without mask check", inline=True)
comment(0x845A, "Convert ctrl byte to 0-based index for mask", inline=True)
comment(0x845B, "SEC for subtract", inline=True)
comment(0x845C, "A = ctrl - &81 (0-based operation index)", inline=True)
comment(0x845E, "Y = index for mask rotation count", inline=True)
comment(0x845F, "Load protection mask from LSTAT", inline=True)
comment(0x8462, "Rotate mask right by control byte index", inline=True)
comment(0x8463, "Decrement rotation counter", inline=True)
comment(0x8464, "Loop until bit aligned", inline=True)
comment(0x8466, "Bit set = operation disabled, discard", inline=True)
comment(0x8468, "Reload ctrl byte for dispatch table", inline=True)
comment(0x846B, "Hi byte: all handlers are in page &84", inline=True)
comment(0x846D, "Push hi byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x846E, "Load handler low byte from jump table", inline=True)
comment(0x8471, "Push handler low byte", inline=True)
comment(0x8472, "RTS dispatches to handler", inline=True)
comment(0x8473, "Increment port buffer length", inline=True)
comment(0x8475, "Check if scout data index reached 11", inline=True)
comment(0x8477, "Yes: loop back to continue reading", inline=True)
comment(0x8479, "Restore A from stack", inline=True)
comment(0x847A, "Transfer to X", inline=True)
comment(0x847B, "Jump to discard handler", inline=True)
comment(0x8488, "Set port buffer lo", inline=True)
comment(0x848A, "Buffer length lo = &82", inline=True)
comment(0x848C, "Set buffer length lo", inline=True)
comment(0x848E, "Buffer length hi = 1", inline=True)
comment(0x8490, "Set buffer length hi", inline=True)
comment(0x8492, "Load RX page hi for buffer", inline=True)
comment(0x8494, "Set port buffer hi", inline=True)
comment(0x8496, "Y=3: copy 4 bytes (3 down to 0)", inline=True)
comment(0x8498, "Load remote address byte", inline=True)
comment(0x849B, "Store to exec address workspace", inline=True)
comment(0x849E, "Next byte (descending)", inline=True)
comment(0x849F, "Loop until all 4 bytes copied", inline=True)
comment(0x84A1, "Enter common data-receive path", inline=True)
comment(0x84A2, "Svc 5 dispatch table low bytes", inline=True)
comment(0x84A4, "Port workspace offset = &3D", inline=True)
comment(0x84A6, "Store workspace offset lo", inline=True)
comment(0x84A8, "RX buffer page = &0D", inline=True)
comment(0x84AA, "Store workspace offset hi", inline=True)
comment(0x84AC, "Enter POKE data-receive path", inline=True)
comment(0x84AF, "Buffer length hi = 1", inline=True)
comment(0x84B1, "Set buffer length hi", inline=True)
comment(0x84B3, "Buffer length lo = &FC", inline=True)
comment(0x84B5, "Set buffer length lo", inline=True)
comment(0x84B7, "Buffer start lo = &25", inline=True)
comment(0x84B9, "Set port buffer lo", inline=True)
comment(0x84BB, "Buffer hi = &7F (below screen)", inline=True)
comment(0x84BD, "Set port buffer hi", inline=True)
comment(0x84C1, "Port workspace offset = &3D", inline=True)
comment(0x84C3, "Store workspace offset lo", inline=True)
comment(0x84C5, "RX buffer page = &0D", inline=True)
comment(0x84C7, "Store workspace offset hi", inline=True)
comment(0x84C9, "Scout status = 2 (PEEK response)", inline=True)
comment(0x84CB, "Store scout status", inline=True)
comment(0x84CE, "Calculate transfer size for response", inline=True)
comment(0x84D1, "C=0: transfer not set up, discard", inline=True)
comment(0x84D3, "Mark TX flags bit 7 (reply pending)", inline=True)
comment(0x84D6, "Set reply pending flag", inline=True)
comment(0x84D8, "Store updated TX flags", inline=True)
comment(0x84DB, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
comment(0x84DD, "Write CR1: enable TX interrupts", inline=True)
comment(0x84E0, "NMI handler hi byte (self-modifying)", inline=True)
comment(0x84E2, "Write CR2 for TX setup", inline=True)
comment(0x84E5, "NMI handler lo byte (self-modifying)", inline=True)
comment(0x84E7, "Y=&9B: dispatch table page", inline=True)
comment(0x84E9, "Acknowledge and write TX dest", inline=True)
comment(0x84EC, "Get buffer position for reply header", inline=True)
comment(0x84EE, "Clear carry for offset addition", inline=True)
comment(0x84EF, "Data offset = buf_len + &80 (past header)", inline=True)
comment(0x84F1, "Y=&7F: reply data length slot", inline=True)
comment(0x84F3, "Store reply data length in RX buffer", inline=True)
comment(0x84F5, "Y=&80: source station slot", inline=True)
comment(0x84F7, "Load requesting station number", inline=True)
comment(0x84FA, "Store source station in reply header", inline=True)
comment(0x84FD, "Load requesting network number", inline=True)
comment(0x8500, "Store source network in reply header", inline=True)
comment(0x8502, "Load control byte from received frame", inline=True)
comment(0x8505, "Save TX operation type for CB1 dispatch", inline=True)
comment(0x8508, "IER bit 2: disable CB1 interrupt", inline=True)
comment(0x850A, "Write IER to disable CB1", inline=True)
comment(0x850D, "Read ACR for shift register config", inline=True)
comment(0x8510, "Isolate shift register mode bits (2-4)", inline=True)
comment(0x8512, "Save original SR mode for later restore", inline=True)
comment(0x8515, "Reload ACR for modification", inline=True)
comment(0x8518, "Clear SR mode bits (keep other bits)", inline=True)
comment(0x851A, "SR mode 4: shift out under CB1 control", inline=True)
comment(0x851C, "Apply new shift register mode", inline=True)
comment(0x851F, "Read SR to clear pending interrupt", inline=True)
comment(0x8522, "Return to idle listen mode", inline=True)
comment(0x8525, "Increment buffer length low byte", inline=True)
comment(0x8527, "No overflow: done", inline=True)
comment(0x8529, "Increment buffer length high byte", inline=True)
comment(0x852B, "No overflow: done", inline=True)
comment(0x852D, "Increment buffer pointer low byte", inline=True)
comment(0x852F, "No overflow: done", inline=True)
comment(0x8531, "Increment buffer pointer high byte", inline=True)
comment(0x8533, "Return", inline=True)
comment(0x853B, "Push hi byte on stack", inline=True)
comment(0x853C, "Push lo of (tx_done_exit-1)", inline=True)
comment(0x853E, "Push lo byte on stack", inline=True)
comment(0x853F, "Call remote JSR; RTS to tx_done_exit", inline=True)
comment(0x8541, "ORA opcode (dead code / data overlap)", inline=True)
comment(0x8542, "X = remote address lo", inline=True)
comment(0x8545, "A = remote address hi", inline=True)
comment(0x854D, "Exit TX done handler", inline=True)
comment(0x8550, "X = remote address lo", inline=True)
comment(0x8553, "Y = remote address hi", inline=True)
comment(0x8556, "Call ROM entry point at &8000", inline=True)
comment(0x8559, "Exit TX done handler", inline=True)
comment(0x855C, "A=&04: bit 2 mask for rx_flags", inline=True)
comment(0x855E, "Test if already halted", inline=True)
comment(0x8561, "Already halted: skip to exit", inline=True)
comment(0x8563, "Set bit 2 in rx_flags", inline=True)
comment(0x8566, "Store halt flag", inline=True)
comment(0x8569, "A=4: re-load halt bit mask", inline=True)
comment(0x856B, "Enable interrupts during halt wait", inline=True)
comment(0x856C, "Test halt flag", inline=True)
comment(0x856F, "Still halted: keep spinning", inline=True)
comment(0x8573, "Load current RX flags", inline=True)
comment(0x8576, "Clear bit 2: release halted station", inline=True)
comment(0x8578, "Store updated flags", inline=True)
comment(0x857B, "Restore Y from stack", inline=True)
comment(0x857C, "Transfer to Y register", inline=True)
comment(0x857D, "Restore X from stack", inline=True)
comment(0x857E, "Transfer to X register", inline=True)
comment(0x857F, "A=0: success status", inline=True)
comment(0x8581, "Return with A=0 (success)", inline=True)
comment(0x8582, "Save X on stack", inline=True)
comment(0x8583, "Push X", inline=True)
comment(0x8584, "Y=2: TXCB offset for dest station", inline=True)
comment(0x8586, "Load dest station from TX control block", inline=True)
comment(0x8588, "Store to TX scout buffer", inline=True)
comment(0x858C, "Load dest network from TX control block", inline=True)
comment(0x858E, "Store to TX scout buffer", inline=True)
comment(0x8591, "Y=0: first byte of TX control block", inline=True)
comment(0x8593, "Load control/flag byte", inline=True)
comment(0x8595, "Bit7 set: immediate operation ctrl byte", inline=True)
comment(0x8597, "Bit7 clear: normal data transfer", inline=True)
comment(0x859A, "Store control byte to TX scout buffer", inline=True)
comment(0x859D, "X = control byte for range checks", inline=True)
comment(0x859E, "Y=1: port byte offset", inline=True)
comment(0x859F, "Load port byte from TX control block", inline=True)
comment(0x85A1, "Store port byte to TX scout buffer", inline=True)
comment(0x85A4, "Port != 0: skip immediate op setup", inline=True)
comment(0x85A6, "Ctrl < &83: PEEK/POKE need address calc", inline=True)
comment(0x85A8, "Ctrl >= &83: skip to range check", inline=True)
comment(0x85AA, "SEC: init borrow for 4-byte subtract", inline=True)
comment(0x85AB, "Save carry on stack for loop", inline=True)
comment(0x85AC, "Y=8: high pointer offset in TXCB", inline=True)
comment(0x85AE, "Load TXCB[Y] (end addr byte)", inline=True)
comment(0x85B0, "Y -= 4: back to start addr offset", inline=True)
comment(0x85B1, "(Y -= 4: reach start addr offset)", inline=True)
comment(0x85B2, "(continued)", inline=True)
comment(0x85B3, "(continued)", inline=True)
comment(0x85B4, "Restore borrow from stack", inline=True)
comment(0x85B5, "end - start = transfer size byte", inline=True)
comment(0x85B7, "Store result to tx_data_start", inline=True)
comment(0x85BA, "(Y += 5: advance to next end byte)", inline=True)
comment(0x85BB, "(continued)", inline=True)
comment(0x85BC, "(continued)", inline=True)
comment(0x85BD, "(continued)", inline=True)
comment(0x85BE, "(continued)", inline=True)
comment(0x85BF, "Save borrow for next byte", inline=True)
comment(0x85C0, "Done all 4 bytes? (Y reaches &0C)", inline=True)
comment(0x85C2, "No: next byte pair", inline=True)
comment(0x85C4, "Discard final borrow", inline=True)
comment(0x85C5, "Ctrl < &81: not an immediate op", inline=True)
comment(0x85C7, "Below range: normal data transfer", inline=True)
comment(0x85C9, "Ctrl >= &89: out of immediate range", inline=True)
comment(0x85CB, "Above range: normal data transfer", inline=True)
comment(0x85CD, "Y=&0C: start of extra data in TXCB", inline=True)
comment(0x85CF, "Load extra parameter byte from TXCB", inline=True)
comment(0x85D1, "Copy to NMI shim workspace at &0D1A+Y", inline=True)
comment(0x85D4, "Next byte", inline=True)
comment(0x85D5, "Done 4 bytes? (Y reaches &10)", inline=True)
comment(0x85D7, "No: continue copying", inline=True)
comment(0x85D9, "A=&20: mask for SR2 INACTIVE bit", inline=True)
comment(0x85DB, "BIT SR2: test if line is idle", inline=True)
comment(0x85DE, "Line not idle: handle as line jammed", inline=True)
comment(0x85E0, "A=&FD: high byte of timeout counter", inline=True)
comment(0x85E2, "Push timeout high byte to stack", inline=True)
comment(0x85E3, "Scout frame = 6 address+ctrl bytes", inline=True)
comment(0x85E5, "Store scout frame length", inline=True)
comment(0x85E8, "A=0: init low byte of timeout counter", inline=True)
comment(0x85EA, "Save TX index", inline=True)
comment(0x85ED, "Push timeout byte 1 on stack", inline=True)
comment(0x85EE, "Push timeout byte 2 on stack", inline=True)
comment(0x85EF, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x85F1, "A=&04: INACTIVE bit mask for SR2 test", inline=True)
comment(0x85F3, "Save interrupt state", inline=True)
comment(0x85F4, "Disable interrupts for ADLC access", inline=True)
comment(0x85F5, "INTOFF -- disable NMIs", inline=True)
comment(0x85F8, "INTOFF again (belt-and-braces)", inline=True)
comment(0x85FB, "BIT SR2: Z = &04 AND SR2 -- tests INACTIVE", inline=True)
comment(0x85FE, "INACTIVE not set -- re-enable NMIs and loop", inline=True)
comment(0x8600, "Read SR1 (acknowledge pending interrupt)", inline=True)
comment(0x8603, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x8605, "Write CR2: clear status, prepare TX", inline=True)
comment(0x8608, "A=&10: CTS mask for SR1 bit4", inline=True)
comment(0x860A, "BIT SR1: tests CTS present", inline=True)
comment(0x860D, "CTS set -- clock hardware detected, start TX", inline=True)
comment(0x860F, "INTON -- re-enable NMIs (&FE20 read)", inline=True)
comment(0x8612, "Restore interrupt state", inline=True)
comment(0x8613, "3-byte timeout counter on stack", inline=True)
comment(0x8614, "Increment timeout counter byte 1", inline=True)
comment(0x8617, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x8619, "Increment timeout counter byte 2", inline=True)
comment(0x861C, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x861E, "Increment timeout counter byte 3", inline=True)
comment(0x8621, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x8625, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
comment(0x8629, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", inline=True)
comment(0x862B, "Write CR2 to abort TX", inline=True)
comment(0x862E, "Clean 3 bytes of timeout loop state", inline=True)
comment(0x862F, "Pop saved register", inline=True)
comment(0x8630, "Pop saved register", inline=True)
comment(0x8631, "Error &40 = 'Line Jammed'", inline=True)
comment(0x8633, "ALWAYS branch to shared error handler", inline=True)
comment(0x8635, "Error &43 = 'No Clock'", inline=True)
comment(0x8637, "Offset 0 = error byte in TX control block", inline=True)
comment(0x8639, "Store error code in TX CB byte 0", inline=True)
comment(0x863B, "&80 = TX complete flag", inline=True)
comment(0x863D, "Signal TX operation complete", inline=True)
comment(0x8640, "Restore X saved by caller", inline=True)
comment(0x8641, "Move to X register", inline=True)
comment(0x8642, "Return to TX caller", inline=True)
comment(0x8643, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x8646, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", inline=True)
comment(0x8648, "Write to ADLC CR1", inline=True)
comment(0x864B, "Install NMI handler at &86E0 (TX data handler)", inline=True)
comment(0x864D, "High byte of NMI handler address", inline=True)
comment(0x864F, "Write NMI vector low byte directly", inline=True)
comment(0x8652, "Write NMI vector high byte directly", inline=True)
comment(0x8655, "Set need_release_tube flag (SEC/ROR = bit7)", inline=True)
comment(0x8656, "Rotate carry into bit 7 of flag", inline=True)
comment(0x8658, "INTON -- NMIs now fire for TDRA (&FE20 read)", inline=True)
comment(0x865B, "Load destination port number", inline=True)
comment(0x865E, "Port != 0: standard data transfer", inline=True)
comment(0x8660, "Port 0: load control byte for table lookup", inline=True)
comment(0x8663, "Look up tx_flags from table", inline=True)
comment(0x8666, "Store operation flags", inline=True)
comment(0x8669, "Look up tx_length from table", inline=True)
comment(0x866C, "Store expected transfer length", inline=True)
comment(0x866F, "Push high byte of return address (&9C)", inline=True)
comment(0x8671, "Push high byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x8672, "Look up handler address low from table", inline=True)
comment(0x8675, "Push low byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x8676, "RTS dispatches to control-byte handler", inline=True)
comment(0x8683, "A=3: scout_status for PEEK op", inline=True)
comment(0x8687, "Scout status = 2 (POKE transfer)", inline=True)
comment(0x8689, "Store scout status", inline=True)
comment(0x868C, "Clear carry for 4-byte addition", inline=True)
comment(0x868D, "Save carry on stack", inline=True)
comment(0x868E, "Y=&0C: start at offset 12", inline=True)
comment(0x8690, "Load workspace address byte", inline=True)
comment(0x8693, "Restore carry from previous byte", inline=True)
comment(0x8694, "Add TXCB address byte", inline=True)
comment(0x8696, "Store updated address byte", inline=True)
comment(0x8699, "Next byte", inline=True)
comment(0x869A, "Save carry for next addition", inline=True)
comment(0x869B, "Compare Y with 16-byte boundary", inline=True)
comment(0x869D, "Below boundary: continue addition", inline=True)
comment(0x869F, "Restore processor flags", inline=True)
comment(0x86A2, "Load dest station for broadcast check", inline=True)
comment(0x86A5, "AND with dest network", inline=True)
comment(0x86A8, "Both &FF = broadcast address?", inline=True)
comment(0x86AA, "Not broadcast: unicast path", inline=True)
comment(0x86AC, "Broadcast scout: 14 bytes total", inline=True)
comment(0x86AE, "Store broadcast scout length", inline=True)
comment(0x86B1, "A=&40: broadcast flag", inline=True)
comment(0x86B3, "Set broadcast flag in tx_flags", inline=True)
comment(0x86B6, "Y=4: start of address data in TXCB", inline=True)
comment(0x86B8, "Copy TXCB address bytes to scout buffer", inline=True)
comment(0x86BA, "Store to TX source/data area", inline=True)
comment(0x86BD, "Next byte", inline=True)
comment(0x86BE, "Done 8 bytes? (Y reaches &0C)", inline=True)
comment(0x86C0, "No: continue copying", inline=True)
comment(0x86C4, "A=0: clear flags for unicast", inline=True)
comment(0x86C6, "Clear tx_flags", inline=True)
comment(0x86C9, "scout_status=2: data transfer pending", inline=True)
comment(0x86CB, "Store scout status", inline=True)
comment(0x86CE, "Copy TX block pointer to workspace ptr", inline=True)
comment(0x86D0, "Store low byte", inline=True)
comment(0x86D2, "Copy TX block pointer high byte", inline=True)
comment(0x86D4, "Store high byte", inline=True)
comment(0x86D6, "Calculate transfer size from RXCB", inline=True)
comment(0x86D9, "Restore processor status from stack", inline=True)
comment(0x86DA, "Restore stacked registers (4 PLAs)", inline=True)
comment(0x86DB, "Second PLA", inline=True)
comment(0x86DC, "Third PLA", inline=True)
comment(0x86DD, "Fourth PLA", inline=True)
comment(0x86DE, "Restore X from A", inline=True)
comment(0x86DF, "Return to caller", inline=True)
comment(0x86E0, "Load TX buffer index", inline=True)
comment(0x86E3, "BIT SR1: V=bit6(TDRA), N=bit7(IRQ)", inline=True)
comment(0x86E6, "TDRA not set -- TX error", inline=True)
comment(0x86E8, "Load byte from TX buffer", inline=True)
comment(0x86EB, "Write to TX_DATA (continue frame)", inline=True)
comment(0x86EE, "Next TX buffer byte", inline=True)
comment(0x86EF, "Load second byte from TX buffer", inline=True)
comment(0x86F2, "Advance TX index past second byte", inline=True)
comment(0x86F3, "Save updated TX buffer index", inline=True)
comment(0x86F6, "Write second byte to TX_DATA", inline=True)
comment(0x86F9, "Compare index to TX length", inline=True)
comment(0x86FC, "Frame complete -- go to TX_LAST_DATA", inline=True)
comment(0x86FE, "Check if we can send another pair", inline=True)
comment(0x8701, "IRQ set -- send 2 more bytes (tight loop)", inline=True)
comment(0x8703, "RTI -- wait for next NMI", inline=True)
comment(0x8706, "Error &42", inline=True)
comment(0x870A, "CR2=&67: clear status, return to listen", inline=True)
comment(0x870C, "Write CR2: clear status, idle listen", inline=True)
comment(0x870F, "Error &41 (TDRA not ready)", inline=True)
comment(0x8711, "INTOFF (also loads station ID)", inline=True)
comment(0x8714, "PHA/PLA delay loop (256 iterations for NMI disable)", inline=True)
comment(0x8715, "PHA/PLA delay (~7 cycles each)", inline=True)
comment(0x8716, "Increment delay counter", inline=True)
comment(0x8717, "Loop 256 times for NMI disable", inline=True)
comment(0x8719, "Store error and return to idle", inline=True)
comment(0x871C, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x871E, "Write to ADLC CR2", inline=True)
comment(0x8721, "Install NMI handler at &8728 (TX completion)", inline=True)
comment(0x8723, "High byte of handler address", inline=True)
comment(0x8725, "Install and return via set_nmi_vector", inline=True)
comment(0x8728, "Jump to error handler", inline=True)
comment(0x872A, "Write CR1 to switch from TX to RX", inline=True)
comment(0x872D, "Test workspace flags", inline=True)
comment(0x8730, "bit6 not set -- check bit0", inline=True)
comment(0x8732, "bit6 set -- TX completion", inline=True)
comment(0x8735, "A=1: mask for bit0 test", inline=True)
comment(0x8737, "Test tx_flags bit0 (handshake)", inline=True)
comment(0x873A, "bit0 clear: install reply handler", inline=True)
comment(0x873C, "bit0 set -- four-way handshake data phase", inline=True)
comment(0x873F, "Install RX reply handler at &8744", inline=True)
comment(0x8741, "Install handler and RTI", inline=True)
comment(0x8744, "A=&01: AP mask for SR2", inline=True)
comment(0x8746, "BIT SR2: test AP (Address Present)", inline=True)
comment(0x8749, "No AP -- error", inline=True)
comment(0x874B, "Read first RX byte (destination station)", inline=True)
comment(0x874E, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x8751, "Not our station -- error/reject", inline=True)
comment(0x8753, "Install next handler at &8758 (reply continuation)", inline=True)
comment(0x8755, "Install continuation handler", inline=True)
comment(0x8758, "Read RX byte (destination station)", inline=True)
comment(0x875B, "No RDA -- error", inline=True)
comment(0x875D, "Read destination network byte", inline=True)
comment(0x8760, "Non-zero -- network mismatch, error", inline=True)
comment(0x8762, "Install next handler at &876F (reply validation)", inline=True)
comment(0x8764, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
comment(0x8767, "IRQ set -- fall through to &876F without RTI", inline=True)
comment(0x8769, "IRQ not set -- install handler and RTI", inline=True)
comment(0x876C, "Store error and return to idle", inline=True)
comment(0x876F, "BIT SR2: test RDA (bit7). Must be set for valid reply.", inline=True)
comment(0x8772, "No RDA -- error (FV masking RDA via PSE would cause this)", inline=True)
comment(0x8774, "Read source station", inline=True)
comment(0x8777, "Compare to original TX destination station (&0D20)", inline=True)
comment(0x877A, "Mismatch -- not the expected reply, error", inline=True)
comment(0x877C, "Read source network", inline=True)
comment(0x877F, "Compare to original TX destination network (&0D21)", inline=True)
comment(0x8782, "Mismatch -- error", inline=True)
comment(0x8784, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x8786, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x8789, "No FV -- incomplete frame, error", inline=True)
comment(0x878B, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", inline=True)
comment(0x878D, "Write CR2: enable RTS for TX handshake", inline=True)
comment(0x8790, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", inline=True)
comment(0x8792, "Write CR1: reset RX, enable TX interrupt", inline=True)
comment(0x8795, "Install next handler at &886E (four-way data phase) into &0D43/&0D44", inline=True)
comment(0x8797, "High byte &88 of next handler address", inline=True)
comment(0x8799, "Store low byte to nmi_next_lo", inline=True)
comment(0x879C, "Store high byte to nmi_next_hi", inline=True)
comment(0x879F, "Load dest station for scout ACK TX", inline=True)
comment(0x87A2, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x87A5, "TDRA not ready -- error", inline=True)
comment(0x87A7, "Write dest station to TX FIFO", inline=True)
comment(0x87AA, "Write dest network to TX FIFO", inline=True)
comment(0x87AD, "Write dest network to TX FIFO", inline=True)
comment(0x87B0, "Install handler at &87B7 (write src addr for scout ACK)", inline=True)
comment(0x87B2, "High byte &87 of handler address", inline=True)
comment(0x87B4, "Set NMI vector and return", inline=True)
comment(0x87B7, "Load our station ID (also INTOFF)", inline=True)
comment(0x87BA, "BIT SR1: test TDRA", inline=True)
comment(0x87BD, "TDRA not ready -- error", inline=True)
comment(0x87BF, "Write our station to TX FIFO", inline=True)
comment(0x87C2, "Write network=0 to TX FIFO", inline=True)
comment(0x87C4, "Write network byte to TX FIFO", inline=True)
comment(0x87C7, "Test bit 1 of tx_flags", inline=True)
comment(0x87C9, "Check if immediate-op or data-transfer", inline=True)
comment(0x87CC, "Bit 1 set: immediate op, use alt handler", inline=True)
comment(0x87CE, "Install nmi_data_tx at &87E4", inline=True)
comment(0x87D0, "High byte of handler address", inline=True)
comment(0x87D2, "Install and return via set_nmi_vector", inline=True)
comment(0x87D5, "Install nmi_imm_data at &882D", inline=True)
comment(0x87D7, "High byte of handler address", inline=True)
comment(0x87D9, "Install and return via set_nmi_vector", inline=True)
comment(0x87DC, "Y = buffer offset, resume from last position", inline=True)
comment(0x87DE, "No pages left: send final partial page", inline=True)
comment(0x87E0, "Load remaining byte count", inline=True)
comment(0x87E2, "Zero bytes left: skip to TDRA check", inline=True)
comment(0x87E4, "Load remaining byte count (alt entry)", inline=True)
comment(0x87E6, "Zero: loop back to top of handler", inline=True)
comment(0x87E8, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x87EB, "TDRA not ready -- error", inline=True)
comment(0x87ED, "Write data byte to TX FIFO", inline=True)
comment(0x87EF, "Write first byte of pair to FIFO", inline=True)
comment(0x87F2, "Advance buffer offset", inline=True)
comment(0x87F3, "No page crossing", inline=True)
comment(0x87F5, "Page crossing: decrement page count", inline=True)
comment(0x87F7, "No pages left: send last data", inline=True)
comment(0x87F9, "Increment buffer high byte", inline=True)
comment(0x87FB, "Load second byte of pair", inline=True)
comment(0x87FD, "Write second byte to FIFO", inline=True)
comment(0x8800, "Advance buffer offset", inline=True)
comment(0x8801, "Save updated buffer position", inline=True)
comment(0x8803, "No page crossing", inline=True)
comment(0x8805, "Page crossing: decrement page count", inline=True)
comment(0x8807, "No pages left: send last data", inline=True)
comment(0x8809, "Increment buffer high byte", inline=True)
comment(0x880B, "BIT SR1: test IRQ (N=bit7) for tight loop", inline=True)
comment(0x880E, "IRQ still set: write 2 more bytes", inline=True)
comment(0x8810, "No IRQ: return, wait for next NMI", inline=True)
comment(0x8813, "CR2=&3F: TX_LAST_DATA (close data frame)", inline=True)
comment(0x8815, "Write CR2 to close frame", inline=True)
comment(0x8818, "Check tx_flags for next action", inline=True)
comment(0x881B, "Bit7 clear: error, install saved handler", inline=True)
comment(0x881D, "Install discard_reset_listen at &83EB", inline=True)
comment(0x881F, "High byte of &83EB handler", inline=True)
comment(0x8821, "Set NMI vector and return", inline=True)
comment(0x8824, "Load saved next handler low byte", inline=True)
comment(0x8827, "Load saved next handler high byte", inline=True)
comment(0x882A, "Install saved handler and return", inline=True)
comment(0x882D, "Tube TX: BIT SR1 test TDRA", inline=True)
comment(0x8830, "TDRA not ready -- error", inline=True)
comment(0x8832, "Read byte from Tube R3", inline=True)
comment(0x8835, "Write to TX FIFO", inline=True)
comment(0x8838, "Increment 4-byte buffer counter", inline=True)
comment(0x883A, "Low byte didn't wrap", inline=True)
comment(0x883C, "Carry into second byte", inline=True)
comment(0x883E, "No further carry", inline=True)
comment(0x8840, "Carry into third byte", inline=True)
comment(0x8842, "No further carry", inline=True)
comment(0x8844, "Carry into fourth byte", inline=True)
comment(0x8846, "Counter wrapped to zero: last data", inline=True)
comment(0x8848, "Read second Tube byte from R3", inline=True)
comment(0x884B, "Write second byte to TX FIFO", inline=True)
comment(0x884E, "Increment 4-byte counter (second byte)", inline=True)
comment(0x8850, "Low byte didn't wrap", inline=True)
comment(0x8852, "Carry into second byte", inline=True)
comment(0x8854, "No further carry", inline=True)
comment(0x8856, "Carry into third byte", inline=True)
comment(0x8858, "No further carry", inline=True)
comment(0x885A, "Carry into fourth byte", inline=True)
comment(0x885C, "Counter wrapped to zero: last data", inline=True)
comment(0x885E, "BIT SR1: test IRQ for tight loop", inline=True)
comment(0x8861, "IRQ still set: write 2 more bytes", inline=True)
comment(0x8863, "No IRQ: return, wait for next NMI", inline=True)
comment(0x8866, "TX error: check flags for path", inline=True)
comment(0x8869, "Bit7 clear: TX result = not listening", inline=True)
comment(0x886B, "Bit7 set: discard and return to listen", inline=True)
comment(0x886E, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", inline=True)
comment(0x8870, "Write to ADLC CR1", inline=True)
comment(0x8873, "Install nmi_final_ack handler", inline=True)
comment(0x8875, "High byte of handler address", inline=True)
comment(0x8877, "Install and return via set_nmi_vector", inline=True)
comment(0x887A, "A=&01: AP mask", inline=True)
comment(0x887C, "BIT SR2: test AP", inline=True)
comment(0x887F, "No AP -- error", inline=True)
comment(0x8881, "Read dest station", inline=True)
comment(0x8884, "Compare to our station (INTOFF side effect)", inline=True)
comment(0x8887, "Not our station -- error", inline=True)
comment(0x8889, "Install nmi_final_ack_net handler", inline=True)
comment(0x888B, "Install continuation handler", inline=True)
comment(0x888E, "BIT SR2: test RDA", inline=True)
comment(0x8891, "No RDA -- error", inline=True)
comment(0x8893, "Read dest network", inline=True)
comment(0x8896, "Non-zero -- network mismatch, error", inline=True)
comment(0x8898, "Install nmi_final_ack_validate handler", inline=True)
comment(0x889A, "BIT SR1: test IRQ -- more data ready?", inline=True)
comment(0x889D, "IRQ set -- fall through to validate", inline=True)
comment(0x889F, "Install handler and RTI", inline=True)
comment(0x88A2, "BIT SR2: test RDA", inline=True)
comment(0x88A5, "No RDA -- error", inline=True)
comment(0x88A7, "Read source station", inline=True)
comment(0x88AA, "Compare to TX dest station (&0D20)", inline=True)
comment(0x88AD, "Mismatch -- error", inline=True)
comment(0x88AF, "Read source network", inline=True)
comment(0x88B2, "Compare to TX dest network (&0D21)", inline=True)
comment(0x88B5, "Mismatch -- error", inline=True)
comment(0x88B7, "Load TX flags for next action", inline=True)
comment(0x88BA, "bit7 clear: no data phase", inline=True)
comment(0x88BC, "Install data RX handler", inline=True)
comment(0x88BF, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x88C1, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x88C4, "No FV -- error", inline=True)
comment(0x88C6, "A=0: success result code", inline=True)
comment(0x88C8, "BEQ: always taken (A=0)", inline=True)
comment(0x88CA, "A=&41: not listening error code", inline=True)
comment(0x88CC, "Y=0: index into TX control block", inline=True)
comment(0x88CE, "Store result/error code at (nmi_tx_block),0", inline=True)
comment(0x88D0, "&80: completion flag for &0D3A", inline=True)
comment(0x88D2, "Signal TX complete", inline=True)
comment(0x88D5, "Full ADLC reset and return to idle listen", inline=True)
comment(0x88D8, "Unreferenced data block (purpose unknown)", inline=True)
comment(0x88DB, "Unreachable: data decoded as ASL A", inline=True)
comment(0x88DC, "Unreachable: data decoded as ASL A", inline=True)
comment(0x88DD, "Unreachable: data decoded as ASL &06", inline=True)
comment(0x88DF, "Unreachable: data decoded as ASL A", inline=True)
comment(0x88E0, "Unreachable: data decoded as STA (&00,X)", inline=True)
comment(0x88E2, "Unreachable: data decoded as BRK", inline=True)
comment(0x88E8, "Y=7: offset to RXCB buffer addr byte 3", inline=True)
comment(0x88EA, "Read RXCB[7] (buffer addr high byte)", inline=True)
comment(0x88EC, "Compare to &FF", inline=True)
comment(0x88EE, "Not &FF: normal buffer, skip Tube check", inline=True)
comment(0x88F1, "Read RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x88F3, "Check if addr byte 2 >= &FE (Tube range)", inline=True)
comment(0x88F5, "Tube/IO address: use fallback path", inline=True)
comment(0x88F7, "Transmit in progress?", inline=True)
comment(0x88FA, "No: fallback path", inline=True)
comment(0x88FC, "Load TX flags for transfer setup", inline=True)
comment(0x88FF, "Set bit 1 (transfer complete)", inline=True)
comment(0x8901, "Store with bit 1 set (Tube xfer)", inline=True)
comment(0x8904, "Init borrow for 4-byte subtract", inline=True)
comment(0x8905, "Save carry on stack", inline=True)
comment(0x8906, "Y=4: start at RXCB offset 4", inline=True)
comment(0x8908, "Load RXCB[Y] (current ptr byte)", inline=True)
comment(0x890A, "Y += 4: advance to RXCB[Y+4]", inline=True)
comment(0x890B, "Y += 4: advance to high ptr offset", inline=True)
comment(0x890C, "(continued)", inline=True)
comment(0x890D, "(continued)", inline=True)
comment(0x890E, "Restore borrow from previous byte", inline=True)
comment(0x890F, "Subtract RXCB[Y+4] (start ptr byte)", inline=True)
comment(0x8911, "Store result byte", inline=True)
comment(0x8914, "Y -= 3: next source byte", inline=True)
comment(0x8915, "Y -= 3: back to next low ptr byte", inline=True)
comment(0x8916, "(continued)", inline=True)
comment(0x8917, "Save borrow for next byte", inline=True)
comment(0x8918, "Done all 4 bytes?", inline=True)
comment(0x891A, "No: next byte pair", inline=True)
comment(0x891C, "Discard final borrow", inline=True)
comment(0x891D, "Save X", inline=True)
comment(0x891E, "Save X", inline=True)
comment(0x891F, "Compute address of RXCB+4", inline=True)
comment(0x8921, "CLC for base pointer addition", inline=True)
comment(0x8922, "Add RXCB base to get RXCB+4 addr", inline=True)
comment(0x8924, "X = low byte of RXCB+4", inline=True)
comment(0x8925, "Y = high byte of RXCB ptr", inline=True)
comment(0x8927, "Tube claim type &C2", inline=True)
comment(0x8929, "Claim Tube transfer address", inline=True)
comment(0x892C, "No Tube: skip reclaim", inline=True)
comment(0x892E, "Tube: reclaim with scout status", inline=True)
comment(0x8931, "Reclaim with scout status type", inline=True)
comment(0x8934, "Release Tube claim after reclaim", inline=True)
comment(0x8937, "C=1: Tube address claimed", inline=True)
comment(0x8938, "Restore X", inline=True)
comment(0x8939, "Restore X from stack", inline=True)
comment(0x893A, "Return with C = transfer status", inline=True)
comment(0x893B, "Y=4: RXCB current pointer offset", inline=True)
comment(0x893D, "Load RXCB[4] (current ptr lo)", inline=True)
comment(0x893F, "Y=8: RXCB start address offset", inline=True)
comment(0x8941, "Set carry for subtraction", inline=True)
comment(0x8942, "Subtract RXCB[8] (start ptr lo)", inline=True)
comment(0x8944, "Store transfer size lo", inline=True)
comment(0x8946, "Y=5: current ptr hi offset", inline=True)
comment(0x8948, "Load RXCB[5] (current ptr hi)", inline=True)
comment(0x894A, "Propagate borrow only", inline=True)
comment(0x894C, "Temp store of adjusted hi byte", inline=True)
comment(0x894E, "Y=8: start address lo offset", inline=True)
comment(0x8950, "Copy RXCB[8] to open port buffer lo", inline=True)
comment(0x8952, "Store to scratch (side effect)", inline=True)
comment(0x8954, "Y=9: start address hi offset", inline=True)
comment(0x8956, "Load RXCB[9]", inline=True)
comment(0x8958, "Set carry for subtraction", inline=True)
comment(0x8959, "Subtract adjusted hi byte", inline=True)
comment(0x895B, "Store transfer size hi", inline=True)
comment(0x895D, "Return with C=1", inline=True)
comment(0x895E, "Return with C=1 (success)", inline=True)
comment(0x895F, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", inline=True)
comment(0x8961, "Write CR1 to ADLC register 0", inline=True)
comment(0x8964, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", inline=True)
comment(0x8966, "Write CR4 to ADLC register 3", inline=True)
comment(0x8969, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", inline=True)
comment(0x896B, "Write CR3 to ADLC register 1", inline=True)
comment(0x896E, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", inline=True)
comment(0x8970, "Write to ADLC CR1", inline=True)
comment(0x8973, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x8975, "Write to ADLC CR2", inline=True)
comment(0x8978, "Return; ADLC now in RX listen mode", inline=True)
comment(0x8979, "Check if Econet has been initialised", inline=True)
comment(0x897C, "Not initialised: skip to RX listen", inline=True)
comment(0x897E, "Read current NMI handler low byte", inline=True)
comment(0x8981, "Expected: &B3 (nmi_rx_scout low)", inline=True)
comment(0x8983, "Not idle: spin and wait", inline=True)
comment(0x8985, "Read current NMI handler high byte", inline=True)
comment(0x8988, "Test if high byte = &80 (page of nmi_rx_scout)", inline=True)
comment(0x898A, "Not idle: spin and wait", inline=True)
comment(0x898C, "INTOFF: disable NMIs", inline=True)
comment(0x898F, "INTOFF again (belt-and-braces)", inline=True)
comment(0x8992, "TX not in progress", inline=True)
comment(0x8995, "Econet not initialised", inline=True)
comment(0x8998, "Y=5: service call workspace page", inline=True)
comment(0x899A, "Set ADLC to RX listen mode", inline=True)
comment(0x899D, "INTOFF: disable NMIs while switching ROM", inline=True)
comment(0x89A0, "Save A", inline=True)
comment(0x89A1, "Transfer Y to A", inline=True)
comment(0x89A2, "Save Y (via A)", inline=True)
comment(0x89A3, "ROM bank 0 (patched during init for actual bank)", inline=True)
comment(0x89A5, "Select Econet ROM bank via ROMSEL", inline=True)
comment(0x89A8, "Jump to scout handler in ROM", inline=True)
comment(0x89AB, "Store handler high byte at &0D0D", inline=True)
comment(0x89AE, "Store handler low byte at &0D0C", inline=True)
comment(0x89B1, "Restore NFS ROM bank", inline=True)
comment(0x89B3, "Page in via hardware latch", inline=True)
comment(0x89B6, "Restore Y from stack", inline=True)
comment(0x89B7, "Transfer ROM bank to Y", inline=True)
comment(0x89B8, "Restore A from stack", inline=True)
comment(0x89B9, "INTON: re-enable NMIs", inline=True)
comment(0x89BC, "Return from interrupt", inline=True)

# Inline comments: service/infrastructure layer (&8A0B-&9130)
comment(0x8A0B, "Save service call number", inline=True)
comment(0x8A0C, "Is it service 15 (vectors claimed)?", inline=True)
comment(0x8A0E, "No: skip vectors-claimed handling", inline=True)
comment(0x8A10, "Save Y parameter", inline=True)
comment(0x8A11, "Save Y on stack", inline=True)
comment(0x8A12, "OSBYTE 0: read OS version", inline=True)
comment(0x8A14, "X=1 to request version number", inline=True)
comment(0x8A19, "OS 1.20?", inline=True)
comment(0x8A1B, "Yes: skip workspace setup", inline=True)
comment(0x8A1D, "OS 2.00 (BBC B+)?", inline=True)
comment(0x8A1F, "Yes: skip workspace setup", inline=True)
comment(0x8A21, "Transfer OS version to A", inline=True)
comment(0x8A22, "Save flags (Z set if OS 1.00)", inline=True)
comment(0x8A23, "Get current ROM slot number", inline=True)
comment(0x8A25, "Restore flags", inline=True)
comment(0x8A26, "OS 1.00: skip INX", inline=True)
comment(0x8A28, "Adjust index for OS 3+ workspace", inline=True)
comment(0x8A29, "A=0", inline=True)
comment(0x8A2B, "Clear workspace byte for this ROM", inline=True)
comment(0x8A2E, "Restore ROM slot to X", inline=True)
comment(0x8A30, "Restore Y parameter", inline=True)
comment(0x8A31, "Transfer to Y", inline=True)
comment(0x8A32, "Restore service call number", inline=True)
comment(0x8A33, "Check relocated code service dispatch", inline=True)
comment(0x8A36, "Save service call number", inline=True)
comment(0x8A37, "Service 1 (workspace claim)?", inline=True)
comment(0x8A39, "No: skip ADLC check", inline=True)
comment(0x8A3B, "Read ADLC status register 1", inline=True)
comment(0x8A3E, "Mask relevant status bits", inline=True)
comment(0x8A40, "Non-zero: ADLC present, set flag", inline=True)
comment(0x8A42, "Read ADLC status register 2", inline=True)
comment(0x8A45, "Mask relevant status bits", inline=True)
comment(0x8A47, "Zero: no ADLC detected, skip", inline=True)
comment(0x8A49, "Shift bit 7 into carry", inline=True)
comment(0x8A4C, "Set carry to mark ADLC present", inline=True)
comment(0x8A4D, "Rotate carry into bit 7 of slot flag", inline=True)
comment(0x8A50, "Load ROM slot flag byte", inline=True)
comment(0x8A53, "Shift bit 7 (ADLC present) into carry", inline=True)
comment(0x8A54, "Restore service call number", inline=True)
comment(0x8A55, "ADLC not present: continue dispatch", inline=True)
comment(0x8A57, "ADLC present: claim service, return", inline=True)
comment(0x8A58, "Service 15 (vectors claimed)?", inline=True)
comment(0x8A5A, "No: handle other services", inline=True)
comment(0x8A5C, "Already initialised?", inline=True)
comment(0x8A5F, "Yes: skip first-time init", inline=True)
comment(0x8A61, "X=1 (mark as initialised)", inline=True)
comment(0x8A62, "Set ROM present flag", inline=True)
comment(0x8A65, "Store service number as ROM counter", inline=True)
comment(0x8A68, "Point to ROM header copyright offset", inline=True)
comment(0x8A6A, "Set high byte of OSRDSC pointer", inline=True)
comment(0x8A6C, "Offset &0C: copyright string offset", inline=True)
comment(0x8A6E, "Set low byte of OSRDSC pointer", inline=True)
comment(0x8A73, "First char 'N'?", inline=True)
comment(0x8A75, "No: not a NET ROM, try next", inline=True)
comment(0x8A7A, "Second char 'E'?", inline=True)
comment(0x8A7C, "No: not a NET ROM, try next", inline=True)
comment(0x8A81, "Third char 'T'?", inline=True)
comment(0x8A83, "No: not a NET ROM, try next", inline=True)
comment(0x8A85, "Get ROM slot being checked", inline=True)
comment(0x8A88, "Load its slot flag byte", inline=True)
comment(0x8A8B, "Set bit 7 to mark as NET ROM", inline=True)
comment(0x8A8D, "Store updated flag", inline=True)
comment(0x8A90, "Decrement ROM counter", inline=True)
comment(0x8A93, "More ROMs to check: loop", inline=True)
comment(0x8A97, "Advance read pointer to next byte", inline=True)
comment(0x8A9F, "Transfer service number to X", inline=True)
comment(0x8AA0, "Save current service state", inline=True)
comment(0x8AA2, "Push old state", inline=True)
comment(0x8AA3, "Restore service number to A", inline=True)
comment(0x8AA4, "Store as current service state", inline=True)
comment(0x8AA6, "Service < 13?", inline=True)
comment(0x8AA8, "Yes: use as dispatch index directly", inline=True)
comment(0x8AAA, "Subtract 5 (map 13-17 to 8-12)", inline=True)
comment(0x8AAC, "Mapped value = 13? (original was 18)", inline=True)
comment(0x8AAE, "Yes: valid service 18 (FS select)", inline=True)
comment(0x8AB0, "Unknown service: set index to 0", inline=True)
comment(0x8AB2, "Transfer dispatch index to X", inline=True)
comment(0x8AB3, "Index 0: unhandled service, skip", inline=True)
comment(0x8AB5, "Save current workspace page", inline=True)
comment(0x8AB7, "Push old page", inline=True)
comment(0x8AB8, "Set workspace page from Y parameter", inline=True)
comment(0x8ABA, "Transfer Y to A", inline=True)
comment(0x8ABB, "Y=0 for dispatch offset", inline=True)
comment(0x8AC0, "Restore old workspace page", inline=True)
comment(0x8AC1, "Store it back", inline=True)
comment(0x8AC3, "Get service state (return code)", inline=True)
comment(0x8AC5, "Restore old service state", inline=True)
comment(0x8AC6, "Store it back", inline=True)
comment(0x8AC8, "Transfer return code to A", inline=True)
comment(0x8AC9, "Restore ROM slot to X", inline=True)
comment(0x8ACB, "Return to MOS", inline=True)
comment(0x8ACC, "Offset 4 in receive block", inline=True)
comment(0x8ACE, "Load remote operation flag", inline=True)
comment(0x8AD0, "Zero: already off, skip to cleanup", inline=True)
comment(0x8AD2, "A=0", inline=True)
comment(0x8AD5, "Clear remote operation flag", inline=True)
comment(0x8AD8, "OSBYTE &C9: keyboard disable", inline=True)
comment(0x8ADD, "A=&0A: workspace init parameter", inline=True)
comment(0x8ADF, "Initialise workspace area", inline=True)
comment(0x8AE2, "Save X in workspace", inline=True)
comment(0x8AE4, "A=&CE: start of key range", inline=True)
comment(0x8AE6, "Restore X from workspace", inline=True)
comment(0x8AE8, "Y=&7F: OSBYTE scan parameter", inline=True)
comment(0x8AEA, "OSBYTE: scan keyboard", inline=True)
comment(0x8AED, "Advance to next key code", inline=True)
comment(0x8AEF, "Reached &D0?", inline=True)
comment(0x8AF1, "No: loop back (scan &CE and &CF)", inline=True)
comment(0x8AF3, "A=0", inline=True)
comment(0x8AF5, "Clear service state", inline=True)
comment(0x8AF7, "Clear workspace byte", inline=True)
comment(0x8AF9, "Return", inline=True)
comment(0x8AFA, "Save A", inline=True)
comment(0x8AFB, "Copy OS text pointer low", inline=True)
comment(0x8AFD, "to fs_crc_lo", inline=True)
comment(0x8AFF, "Copy OS text pointer high", inline=True)
comment(0x8B01, "to fs_crc_hi", inline=True)
comment(0x8B03, "Restore A", inline=True)
comment(0x8B04, "Return", inline=True)
comment(0x8B05, "Y=5 (Econet filing system)?", inline=True)
comment(0x8B07, "No: not ours, return unclaimed", inline=True)
comment(0x8B09, "Already selected?", inline=True)
comment(0x8B0C, "Yes (bit 7 set): return unclaimed", inline=True)
comment(0x8B0E, "Get workspace page for this ROM slot", inline=True)
comment(0x8B11, "Store as high byte of load address", inline=True)
comment(0x8B13, "A=0", inline=True)
comment(0x8B15, "Clear low byte of load address", inline=True)
comment(0x8B17, "Clear carry for addition", inline=True)
comment(0x8B18, "Y=&76: checksum range end", inline=True)
comment(0x8B1A, "Add byte to running checksum", inline=True)
comment(0x8B1C, "Decrement index", inline=True)
comment(0x8B1D, "Loop until all bytes summed", inline=True)
comment(0x8B1F, "Y=&77: checksum storage offset", inline=True)
comment(0x8B21, "Compare with stored checksum", inline=True)
comment(0x8B23, "Match: checksum valid", inline=True)
comment(0x8B25, "Mismatch: raise checksum error", inline=True)
comment(0x8B28, "Call FSCV with A=6 (new FS)", inline=True)
comment(0x8B2B, "Y=&0D: end of FS context block", inline=True)
comment(0x8B2D, "Load byte from receive block", inline=True)
comment(0x8B2F, "Store into FS workspace", inline=True)
comment(0x8B32, "Decrement index", inline=True)
comment(0x8B33, "Reached offset 5?", inline=True)
comment(0x8B35, "No: continue copying", inline=True)
comment(0x8B37, "Shift bit 7 of FS flags into carry", inline=True)
comment(0x8B3A, "Clear carry", inline=True)
comment(0x8B3B, "Clear bit 7 of FS flags", inline=True)
comment(0x8B3E, "Y=&0D: vector table size - 1", inline=True)
comment(0x8B40, "Load FS vector address", inline=True)
comment(0x8B43, "Store into FILEV vector table", inline=True)
comment(0x8B46, "Decrement index", inline=True)
comment(0x8B47, "Loop until all vectors installed", inline=True)
comment(0x8B49, "Initialise ADLC and NMI workspace", inline=True)
comment(0x8B4C, "Y=&1B: extended vector offset", inline=True)
comment(0x8B4E, "X=7: two more vectors to set up", inline=True)
comment(0x8B50, "Set up extended vectors", inline=True)
comment(0x8B53, "A=0", inline=True)
comment(0x8B55, "Clear FS state byte", inline=True)
comment(0x8B58, "Clear workspace byte", inline=True)
comment(0x8B5B, "Clear workspace byte", inline=True)
comment(0x8B5E, "Clear service state", inline=True)
comment(0x8B60, "Offset &0E in receive block", inline=True)
comment(0x8B62, "Clear receive block flag", inline=True)
comment(0x8B64, "Clear workspace byte", inline=True)
comment(0x8B67, "Set up workspace pointers", inline=True)
comment(0x8B6A, "Initialise FS state", inline=True)
comment(0x8B6D, "Y=&77: workspace block size - 1", inline=True)
comment(0x8B6F, "Load byte from source workspace", inline=True)
comment(0x8B71, "Store to page &10 shadow copy", inline=True)
comment(0x8B74, "Decrement index", inline=True)
comment(0x8B75, "Loop until all bytes copied", inline=True)
comment(0x8B77, "A=&80: FS selected flag", inline=True)
comment(0x8B79, "Set bit 7 of FS flags", inline=True)
comment(0x8B7C, "Store updated flags", inline=True)
comment(0x8B7F, "Issue service 15 (FS initialised)", inline=True)
comment(0x8B82, "X=&4A: NFS command table offset", inline=True)
comment(0x8B84, "Print help for NFS commands", inline=True)
comment(0x8B87, "X=0: FS command table offset", inline=True)
comment(0x8B8B, "X=&4A: NFS command table offset", inline=True)
comment(0x8B8D, "V clear: need to print header first", inline=True)
comment(0x8B8F, "Save X (table offset)", inline=True)
comment(0x8B90, "Push it", inline=True)
comment(0x8B91, "Save Y", inline=True)
comment(0x8B92, "Push it", inline=True)
comment(0x8B93, "Print version string header", inline=True)
comment(0x8B96, "Restore Y", inline=True)
comment(0x8B97, "Transfer to Y", inline=True)
comment(0x8B98, "Restore X", inline=True)
comment(0x8B99, "Transfer to X", inline=True)
comment(0x8B9A, "Clear overflow flag", inline=True)
comment(0x8BA0, "Save Y (command line offset)", inline=True)
comment(0x8BA1, "Push it", inline=True)
comment(0x8BA2, "Save processor status", inline=True)
comment(0x8BA3, "Load byte from command table", inline=True)
comment(0x8BA6, "Bit 7 clear: valid entry, continue", inline=True)
comment(0x8BA8, "End of table: finish up", inline=True)
comment(0x8BAB, "Print two-space indent", inline=True)
comment(0x8BB0, "Y=9: max command name length", inline=True)
comment(0x8BB2, "Load first char of command name", inline=True)
comment(0x8BB8, "Advance table pointer", inline=True)
comment(0x8BB9, "Decrement padding counter", inline=True)
comment(0x8BBA, "Load next character", inline=True)
comment(0x8BBD, "Bit 7 clear: more chars, continue", inline=True)
comment(0x8BBF, "Pad with spaces", inline=True)
comment(0x8BC4, "Decrement remaining pad count", inline=True)
comment(0x8BC5, "More padding needed: loop", inline=True)
comment(0x8BC7, "Load syntax descriptor byte", inline=True)
comment(0x8BCA, "Mask to get syntax string index", inline=True)
comment(0x8BCC, "Index &0E: shared commands?", inline=True)
comment(0x8BCE, "Yes: handle shared commands list", inline=True)
comment(0x8BD0, "Use index as Y", inline=True)
comment(0x8BD1, "Look up syntax string offset", inline=True)
comment(0x8BD4, "Transfer offset to Y", inline=True)
comment(0x8BD5, "Advance to next character", inline=True)
comment(0x8BD6, "Load syntax string character", inline=True)
comment(0x8BD9, "Zero terminator: end of syntax", inline=True)
comment(0x8BDB, "Carriage return: line continuation", inline=True)
comment(0x8BDD, "No: print the character", inline=True)
comment(0x8BDF, "Handle line wrap in syntax output", inline=True)
comment(0x8BE2, "Continue with next character", inline=True)
comment(0x8BE8, "Continue with next character", inline=True)
comment(0x8BEB, "Save table pointer", inline=True)
comment(0x8BEC, "Push it", inline=True)
comment(0x8BED, "Print opening parenthesis", inline=True)
comment(0x8BF1, "Y=0: shared command counter", inline=True)
comment(0x8BF3, "X=&D3: shared command table start", inline=True)
comment(0x8BF5, "Load byte from shared command table", inline=True)
comment(0x8BF8, "Bit 7 set: end of shared commands", inline=True)
comment(0x8BFA, "Back up one position", inline=True)
comment(0x8BFB, "Advance to next character", inline=True)
comment(0x8BFC, "Load command name character", inline=True)
comment(0x8BFF, "Bit 7 set: end of this name", inline=True)
comment(0x8C04, "Print more characters of name", inline=True)
comment(0x8C07, "Strip bit 7 from final character", inline=True)
comment(0x8C0C, "Count this shared command", inline=True)
comment(0x8C0D, "Printed 4 commands?", inline=True)
comment(0x8C0F, "No: continue on same line", inline=True)
comment(0x8C11, "Handle line wrap after 4 commands", inline=True)
comment(0x8C14, "Skip 3 bytes (syntax descriptor)", inline=True)
comment(0x8C15, "to advance to next command", inline=True)
comment(0x8C16, "in the table", inline=True)
comment(0x8C17, "Loop for more shared commands", inline=True)
comment(0x8C19, "Restore original table pointer", inline=True)
comment(0x8C1A, "Transfer to X", inline=True)
comment(0x8C1E, "Skip 3 bytes to next table entry", inline=True)
comment(0x8C1F, "(syntax descriptor byte,", inline=True)
comment(0x8C20, "dispatch address low and high)", inline=True)
comment(0x8C21, "Loop for next command", inline=True)
comment(0x8C24, "Restore processor status", inline=True)
comment(0x8C25, "Restore Y", inline=True)
comment(0x8C26, "Transfer to Y", inline=True)
comment(0x8C27, "Return", inline=True)
comment(0x8C28, "Read output stream type", inline=True)
comment(0x8C2B, "Stream 0 (VDU): no wrapping", inline=True)
comment(0x8C2D, "Stream 3 (printer)?", inline=True)
comment(0x8C2F, "Yes: no wrapping", inline=True)
comment(0x8C31, "Save Y", inline=True)
comment(0x8C32, "Push it", inline=True)
comment(0x8C36, "Y=&0B: indent width - 1", inline=True)
comment(0x8C38, "Space character", inline=True)
comment(0x8C3D, "Decrement indent counter", inline=True)
comment(0x8C3E, "More spaces needed: loop", inline=True)
comment(0x8C40, "Restore Y", inline=True)
comment(0x8C41, "Transfer to Y", inline=True)
comment(0x8C42, "Return", inline=True)
comment(0x8C43, "X=0: start of FS command table", inline=True)
comment(0x8C45, "Get command line offset", inline=True)
comment(0x8C47, "Save text pointer to fs_crc", inline=True)
comment(0x8C4A, "Try to match command in table", inline=True)
comment(0x8C4D, "No match: return to caller", inline=True)
comment(0x8C4F, "Match found: execute command", inline=True)
comment(0x8C52, "Check for credits Easter egg", inline=True)
comment(0x8C55, "Get command line offset", inline=True)
comment(0x8C57, "Load character at offset", inline=True)
comment(0x8C59, "Is it CR (bare *HELP)?", inline=True)
comment(0x8C5B, "No: check for specific topic", inline=True)
comment(0x8C5D, "Print version string", inline=True)
comment(0x8C60, "X=&C4: start of help command list", inline=True)
comment(0x8C62, "Print command list from table", inline=True)
comment(0x8C65, "Restore Y (command line offset)", inline=True)
comment(0x8C67, "Return unclaimed", inline=True)
comment(0x8C68, "Test for topic match (sets flags)", inline=True)
comment(0x8C6B, "Is first char '.' (abbreviation)?", inline=True)
comment(0x8C6D, "No: try topic-specific help", inline=True)
comment(0x8C6F, "'.' found: show full command list", inline=True)
comment(0x8C72, "Save text pointer to fs_crc", inline=True)
comment(0x8C75, "Save flags", inline=True)
comment(0x8C76, "X=&C4: help command table start", inline=True)
comment(0x8C78, "Try to match help topic in table", inline=True)
comment(0x8C7B, "No match: try next topic", inline=True)
comment(0x8C7D, "Restore flags", inline=True)
comment(0x8C7E, "Push return address high (&8C)", inline=True)
comment(0x8C80, "Push it for RTS dispatch", inline=True)
comment(0x8C81, "Push return address low (&74)", inline=True)
comment(0x8C83, "Push it for RTS dispatch", inline=True)
comment(0x8C84, "Load dispatch address high", inline=True)
comment(0x8C87, "Push dispatch high for RTS", inline=True)
comment(0x8C88, "Load dispatch address low", inline=True)
comment(0x8C8B, "Push dispatch low for RTS", inline=True)
comment(0x8C8C, "Dispatch via RTS (returns to &8C75)", inline=True)
comment(0x8C8D, "Restore flags from before match", inline=True)
comment(0x8C8E, "End of command line?", inline=True)
comment(0x8C90, "No: try matching next topic", inline=True)
comment(0x8C94, "Print version string via inline", inline=True)
comment(0x8CAA, "NOP (string terminator)", inline=True)
comment(0x8CAB, "Print station number", inline=True)
comment(0x8CAE, "Get current ROM slot number", inline=True)
comment(0x8CB0, "Load workspace page for this slot", inline=True)
comment(0x8CB3, "Transfer to Y", inline=True)
comment(0x8CB4, "Return with page in A and Y", inline=True)
comment(0x8CB5, "Get workspace page for ROM slot", inline=True)
comment(0x8CB8, "Store page in nfs_temp", inline=True)
comment(0x8CBA, "A=0", inline=True)
comment(0x8CBC, "Clear low byte of pointer", inline=True)
comment(0x8CBE, "Return", inline=True)
comment(0x8CBF, "OSBYTE &7A: scan keyboard from key 16", inline=True)
comment(0x8CC5, "No key pressed: select Net FS", inline=True)
comment(0x8CC7, "Key &19 (N)?", inline=True)
comment(0x8CC9, "Yes: write key state and boot", inline=True)
comment(0x8CCB, "EOR with &55: maps to zero if 'N'", inline=True)
comment(0x8CCD, "Not N key: return unclaimed", inline=True)
comment(0x8CD0, "OSBYTE &78: write keys pressed", inline=True)
comment(0x8CD8, "Print station number", inline=True)
comment(0x8CDE, "Get workspace page", inline=True)
comment(0x8CE0, "Non-zero: already initialised, return", inline=True)
comment(0x8CE2, "Load boot flags", inline=True)
comment(0x8CE5, "Set bit 2 (auto-boot in progress)", inline=True)
comment(0x8CE7, "Store updated boot flags", inline=True)
comment(0x8CEA, "X=4: boot filename parameter", inline=True)
comment(0x8CEC, "Y=&8D: boot filename address high", inline=True)
comment(0x8CEE, "Execute boot file", inline=True)
comment(0x8CF1, "A=6: notify new filing system", inline=True)
comment(0x8CF3, "Call FSCV", inline=True)
comment(0x8CF6, "X=&0A: service 10 parameter", inline=True)
comment(0x8CFA, "Dispatch via FSCV", inline=True)
comment(0x8CFD, "X=&0F: service 15 parameter", inline=True)
comment(0x8CFF, "OSBYTE &8F: issue service request", inline=True)
comment(0x8D0C, "Get command line offset", inline=True)
comment(0x8D0E, "X=5: start of credits keyword", inline=True)
comment(0x8D10, "Load character from command line", inline=True)
comment(0x8D12, "Compare with credits keyword", inline=True)
comment(0x8D15, "Mismatch: check if keyword complete", inline=True)
comment(0x8D17, "Advance command line pointer", inline=True)
comment(0x8D18, "Advance keyword pointer", inline=True)
comment(0x8D19, "Continue matching", inline=True)
comment(0x8D1B, "Reached end of keyword (X=&0D)?", inline=True)
comment(0x8D1D, "No: keyword not fully matched, return", inline=True)
comment(0x8D1F, "X=0: start of credits text", inline=True)
comment(0x8D21, "Load character from credits string", inline=True)
comment(0x8D24, "Zero terminator: done printing", inline=True)
comment(0x8D29, "Advance string pointer", inline=True)
comment(0x8D2A, "Continue printing", inline=True)
comment(0x8D2C, "Return", inline=True)
comment(0x8D6E, "Save Y (command line offset)", inline=True)
comment(0x8D6F, "Push it", inline=True)
comment(0x8D70, "OSBYTE &77: close SPOOL/EXEC", inline=True)
comment(0x8D72, "Store as pending operation marker", inline=True)
comment(0x8D78, "Y=0", inline=True)
comment(0x8D7A, "Clear password entry flag", inline=True)
comment(0x8D7C, "Reset FS connection state", inline=True)
comment(0x8D7F, "A=0", inline=True)
comment(0x8D81, "Clear pending operation marker", inline=True)
comment(0x8D84, "Restore command line offset", inline=True)
comment(0x8D85, "Transfer to Y", inline=True)
comment(0x8D86, "Load first option byte", inline=True)
comment(0x8D88, "Parse station number if present", inline=True)
comment(0x8D8D, "Parse user ID string", inline=True)
comment(0x8D90, "No user ID: go to password", inline=True)
comment(0x8D92, "Store file server station low", inline=True)
comment(0x8D95, "Check and store FS network", inline=True)
comment(0x8D98, "Skip separator", inline=True)
comment(0x8D99, "Parse next argument", inline=True)
comment(0x8D9E, "Store file server station high", inline=True)
comment(0x8DA1, "X=&FF: pre-decrement for loop", inline=True)
comment(0x8DA3, "Advance index", inline=True)
comment(0x8DA4, "Load logon command template byte", inline=True)
comment(0x8DA7, "Store into transmit buffer", inline=True)
comment(0x8DAA, "Bit 7 clear: more bytes, loop", inline=True)
comment(0x8DAC, "Send logon with file server lookup", inline=True)
comment(0x8DAF, "Success: skip to password entry", inline=True)
comment(0x8DB1, "Build FS command packet", inline=True)
comment(0x8DB4, "Y=&FF: pre-increment for loop", inline=True)
comment(0x8DB6, "Advance to next byte", inline=True)
comment(0x8DB7, "Load byte from reply buffer", inline=True)
comment(0x8DBA, "Is it CR (end of prompt)?", inline=True)
comment(0x8DBC, "Yes: no colon found, skip to send", inline=True)
comment(0x8DBE, "Is it ':' (password prompt)?", inline=True)
comment(0x8DC0, "No: keep scanning", inline=True)
comment(0x8DC5, "Save position of colon", inline=True)
comment(0x8DC7, "A=&FF: mark as escapable", inline=True)
comment(0x8DC9, "Set escape flag", inline=True)
comment(0x8DCB, "Check for escape condition", inline=True)
comment(0x8DD3, "Not NAK (&15): check other chars", inline=True)
comment(0x8DD5, "Restore colon position", inline=True)
comment(0x8DD7, "Non-zero: restart from colon", inline=True)
comment(0x8DD9, "At colon position?", inline=True)
comment(0x8DDB, "Yes: restart password input", inline=True)
comment(0x8DDD, "Backspace: move back one character", inline=True)
comment(0x8DDE, "If not at start: restart input", inline=True)
comment(0x8DE0, "Delete key (&7F)?", inline=True)
comment(0x8DE2, "Yes: handle backspace", inline=True)
comment(0x8DE4, "Store character in password buffer", inline=True)
comment(0x8DE7, "Advance buffer pointer", inline=True)
comment(0x8DE8, "Is it CR (end of password)?", inline=True)
comment(0x8DEA, "No: read another character", inline=True)
comment(0x8DEF, "Transfer string length to A", inline=True)
comment(0x8DF0, "Save string length", inline=True)
comment(0x8DF1, "Set up transmit control block", inline=True)
comment(0x8DF4, "Send to file server and get reply", inline=True)
comment(0x8DF7, "Restore string length", inline=True)
comment(0x8DF8, "Transfer to X (byte count)", inline=True)
comment(0x8DF9, "Include terminator", inline=True)
comment(0x8DFA, "Y=0", inline=True)
comment(0x8DFE, "Parse station number from cmd line", inline=True)
comment(0x8E01, "Compare with expected station", inline=True)
comment(0x8E04, "Different: return without clearing", inline=True)
comment(0x8E06, "Same: clear station byte", inline=True)
comment(0x8E09, "Return", inline=True)
comment(0x8E0A, "Build FS command packet", inline=True)
comment(0x8E0D, "Transfer result to Y", inline=True)
comment(0x8E0E, "Set up command and send to FS", inline=True)
comment(0x8E11, "Load reply function code", inline=True)
comment(0x8E14, "Zero: no reply, return", inline=True)
comment(0x8E16, "Load first reply byte", inline=True)
comment(0x8E19, "Y=&17: logon dispatch offset", inline=True)
comment(0x8E1D, "Parse reply as decimal number", inline=True)
comment(0x8E20, "Result >= 8?", inline=True)
comment(0x8E22, "Yes: out of range, return", inline=True)
comment(0x8E24, "Transfer handle to X", inline=True)
comment(0x8E25, "Look up in open files table", inline=True)
comment(0x8E28, "Transfer result to A", inline=True)
comment(0x8E29, "Y=&13: handle dispatch offset", inline=True)
comment(0x8E2D, "Handle >= 5?", inline=True)
comment(0x8E2F, "Yes: out of range, return", inline=True)
comment(0x8E31, "Y=&0E: directory dispatch offset", inline=True)
comment(0x8E33, "Advance X to target index", inline=True)
comment(0x8E34, "Decrement Y offset counter", inline=True)
comment(0x8E37, "Y=&FF: will be ignored by caller", inline=True)
comment(0x8E38, "Load dispatch address high byte", inline=True)
comment(0x8E3B, "Push high byte for RTS dispatch", inline=True)
comment(0x8E3C, "Load dispatch address low byte", inline=True)
comment(0x8E3F, "Push low byte for RTS dispatch", inline=True)
comment(0x8E40, "Load FS options pointer", inline=True)
comment(0x8E42, "Dispatch via RTS", inline=True)
comment(0x8E6D, "X=0", inline=True)
comment(0x8E6F, "Y=&FF", inline=True)
comment(0x8E71, "Execute OSBYTE and return", inline=True)
comment(0x8E76, "X=0", inline=True)
comment(0x8E78, "Y=0", inline=True)
comment(0x8E7C, "Get original OSBYTE A parameter", inline=True)
comment(0x8E7E, "Subtract &31 (map &32-&35 to 1-4)", inline=True)
comment(0x8E80, "In range 0-3?", inline=True)
comment(0x8E82, "No: not ours, return unclaimed", inline=True)
comment(0x8E84, "Transfer to X as dispatch index", inline=True)
comment(0x8E85, "A=0: claim the service call", inline=True)
comment(0x8E87, "Set return value to 0 (claimed)", inline=True)
comment(0x8E89, "Transfer Y to A (OSBYTE Y param)", inline=True)
comment(0x8E8A, "Y=&21: OSBYTE dispatch offset", inline=True)
comment(0x8E8F, "Need at least &16 pages?", inline=True)
comment(0x8E91, "Already enough: return", inline=True)
comment(0x8E93, "Request &16 pages of workspace", inline=True)
comment(0x8E95, "Return", inline=True)
comment(0x8E96, "Transfer Y to A", inline=True)
comment(0x8E97, "Y >= &21?", inline=True)
comment(0x8E99, "No: use Y as-is", inline=True)
comment(0x8E9B, "Cap at &21", inline=True)
comment(0x8E9D, "Offset &0F in receive block", inline=True)
comment(0x8E9F, "Store workspace page count", inline=True)
comment(0x8EA1, "Return", inline=True)
comment(0x8EA2, "Store Y as receive block page", inline=True)
comment(0x8EA4, "Advance to next page", inline=True)
comment(0x8EA5, "Store as NFS workspace page", inline=True)
comment(0x8EA7, "Advance to next page", inline=True)
comment(0x8EA8, "Transfer page to A", inline=True)
comment(0x8EA9, "Get current ROM slot number", inline=True)
comment(0x8EAB, "Store workspace page for this slot", inline=True)
comment(0x8EAE, "A=0", inline=True)
comment(0x8EB0, "Clear receive block pointer low", inline=True)
comment(0x8EB2, "Clear NFS workspace pointer low", inline=True)
comment(0x8EB4, "Clear workspace page counter", inline=True)
comment(0x8EB6, "Clear workspace byte", inline=True)
comment(0x8EB9, "Offset 4 in receive block", inline=True)
comment(0x8EBB, "Clear remote operation flag", inline=True)
comment(0x8EBD, "OSBYTE &8F: issue service request", inline=True)
comment(0x8EBF, "X=1: workspace claim service", inline=True)
comment(0x8EC1, "Y=&0E: requested pages", inline=True)
comment(0x8EC6, "Record final workspace allocation", inline=True)
comment(0x8EC9, "Load ROM present flag", inline=True)
comment(0x8ECC, "Zero: first ROM init, skip FS setup", inline=True)
comment(0x8ECE, "Set up workspace pointers", inline=True)
comment(0x8ED1, "Clear FS flags", inline=True)
comment(0x8ED4, "A=0, transfer to Y", inline=True)
comment(0x8ED5, "Clear byte in FS workspace", inline=True)
comment(0x8ED7, "Clear byte in NFS workspace", inline=True)
comment(0x8ED9, "Advance index", inline=True)
comment(0x8EDA, "Loop until full page zeroed", inline=True)
comment(0x8EDC, "Offset &0C in receive block", inline=True)
comment(0x8EDE, "Clear protection flags", inline=True)
comment(0x8EE0, "Initialise station identity block", inline=True)
comment(0x8EE3, "Offset 6 in receive block", inline=True)
comment(0x8EE5, "A=&FE: default station ID marker", inline=True)
comment(0x8EE7, "Store default station low", inline=True)
comment(0x8EEA, "Store into receive block", inline=True)
comment(0x8EEC, "A=0", inline=True)
comment(0x8EEE, "Clear station high byte", inline=True)
comment(0x8EF2, "Store into receive block", inline=True)
comment(0x8EF4, "Offset 3 in NFS workspace", inline=True)
comment(0x8EF6, "Clear NFS workspace byte 3", inline=True)
comment(0x8EF9, "A=&EB: default listen state", inline=True)
comment(0x8EFB, "Store at NFS workspace offset 2", inline=True)
comment(0x8EFD, "X=3: init data byte count", inline=True)
comment(0x8EFF, "Load initialisation data byte", inline=True)
comment(0x8F02, "Store in workspace", inline=True)
comment(0x8F05, "Decrement counter", inline=True)
comment(0x8F06, "More bytes: loop", inline=True)
comment(0x8F08, "Clear workspace flag", inline=True)
comment(0x8F0B, "Clear workspace byte", inline=True)
comment(0x8F0E, "Initialise ADLC protection table", inline=True)
comment(0x8F11, "Get current workspace page", inline=True)
comment(0x8F13, "Allocate FS handle page", inline=True)
comment(0x8F16, "Allocation failed: finish init", inline=True)
comment(0x8F18, "A=&3F: default handle permissions", inline=True)
comment(0x8F1A, "Store handle permissions", inline=True)
comment(0x8F1C, "Advance to next page", inline=True)
comment(0x8F1E, "Continue allocating: loop", inline=True)
comment(0x8F20, "Restore FS context from saved state", inline=True)
comment(0x8F23, "Read station ID from hardware", inline=True)
comment(0x8F26, "Transfer to A", inline=True)
comment(0x8F27, "Non-zero: station ID valid", inline=True)
comment(0x8F29, "Station 0: report error", inline=True)
comment(0x8F2F, "Increment station ID", inline=True)
comment(0x8F30, "Overflow to 0: report error", inline=True)
comment(0x8F32, "Offset 5: station ID in recv block", inline=True)
comment(0x8F34, "Store station ID", inline=True)
comment(0x8F36, "X=&40: Econet flag byte", inline=True)
comment(0x8F38, "Store Econet control flag", inline=True)
comment(0x8F3B, "A=3: protection level", inline=True)
comment(0x8F3D, "Set up Econet protection", inline=True)
comment(0x8F43, "OSBYTE &A8: read ROM pointer table", inline=True)
comment(0x8F48, "Store table pointer low", inline=True)
comment(0x8F4A, "Store table pointer high", inline=True)
comment(0x8F4C, "Y=&36: NETV vector offset", inline=True)
comment(0x8F4E, "Set NETV address", inline=True)
comment(0x8F51, "X=1: one more vector pair to set", inline=True)
comment(0x8F53, "Load vector address low byte", inline=True)
comment(0x8F56, "Store into extended vector table", inline=True)
comment(0x8F58, "Advance to high byte", inline=True)
comment(0x8F59, "Load vector address high byte", inline=True)
comment(0x8F5C, "Store into extended vector table", inline=True)
comment(0x8F5E, "Advance to ROM ID byte", inline=True)
comment(0x8F5F, "Load current ROM slot number", inline=True)
comment(0x8F61, "Store ROM ID in extended vector", inline=True)
comment(0x8F63, "Advance to next vector entry", inline=True)
comment(0x8F64, "Decrement vector counter", inline=True)
comment(0x8F65, "More vectors to set: loop", inline=True)
comment(0x8F67, "X=&FF", inline=True)
comment(0x8F68, "Store &FF in workspace flag", inline=True)
comment(0x8F6B, "Restore FS state if previously active", inline=True)
comment(0x8F6E, "Get workspace page for ROM slot", inline=True)
comment(0x8F71, "Advance Y past workspace page", inline=True)
comment(0x8F72, "Return", inline=True)
comment(0x8F73, "Y=&0D: end of FS context block", inline=True)
comment(0x8F75, "Load FS context byte", inline=True)
comment(0x8F78, "Store into receive block", inline=True)
comment(0x8F7A, "Decrement index", inline=True)
comment(0x8F7B, "Reached offset 5?", inline=True)
comment(0x8F7D, "No: continue copying", inline=True)
comment(0x8F7F, "Return", inline=True)
comment(0x8F80, "FS currently selected?", inline=True)
comment(0x8F83, "No (bit 7 clear): return", inline=True)
comment(0x8F85, "Y=0", inline=True)
comment(0x8F87, "Reset FS connection state", inline=True)
comment(0x8F8A, "OSBYTE &77: close SPOOL/EXEC", inline=True)
comment(0x8F8F, "Restore FS context to receive block", inline=True)
comment(0x8F92, "Y=&76: checksum range end", inline=True)
comment(0x8F94, "A=0: checksum accumulator", inline=True)
comment(0x8F96, "Clear carry for addition", inline=True)
comment(0x8F97, "Add byte from page &10 shadow", inline=True)
comment(0x8F9A, "Decrement index", inline=True)
comment(0x8F9B, "Loop until all bytes summed", inline=True)
comment(0x8F9D, "Y=&77: checksum storage offset", inline=True)
comment(0x8FA1, "Load byte from page &10 shadow", inline=True)
comment(0x8FA4, "Copy to FS workspace", inline=True)
comment(0x8FA6, "Decrement index", inline=True)
comment(0x8FA7, "Loop until all bytes copied", inline=True)
comment(0x8FA9, "Load FS flags", inline=True)
comment(0x8FAC, "Clear bit 7 (FS no longer selected)", inline=True)
comment(0x8FAE, "Store updated flags", inline=True)
comment(0x8FB1, "Return", inline=True)
comment(0x8FB2, "Save processor status", inline=True)
comment(0x8FB3, "Save A", inline=True)
comment(0x8FB4, "Transfer Y to A", inline=True)
comment(0x8FB5, "Save Y", inline=True)
comment(0x8FB6, "Y=&76: checksum range end", inline=True)
comment(0x8FB8, "A=0: checksum accumulator", inline=True)
comment(0x8FBA, "Clear carry for addition", inline=True)
comment(0x8FBB, "Add byte from FS workspace", inline=True)
comment(0x8FBD, "Decrement index", inline=True)
comment(0x8FBE, "Loop until all bytes summed", inline=True)
comment(0x8FC0, "Y=&77: checksum storage offset", inline=True)
comment(0x8FC2, "Compare with stored checksum", inline=True)
comment(0x8FC4, "Mismatch: raise checksum error", inline=True)
comment(0x8FC6, "Restore Y", inline=True)
comment(0x8FC7, "Transfer to Y", inline=True)
comment(0x8FC8, "Restore A", inline=True)
comment(0x8FC9, "Restore processor status", inline=True)
comment(0x8FCA, "Return (checksum valid)", inline=True)
comment(0x8FCB, "Error number &AA", inline=True)
comment(0x8FCD, "Raise 'net checksum' error", inline=True)
comment(0x8FDD, "Print 'Econet Station ' via inline", inline=True)
comment(0x8FEF, "Offset 5: station ID", inline=True)
comment(0x8FF1, "Load station ID from receive block", inline=True)
comment(0x8FF3, "Print station number as decimal", inline=True)
comment(0x8FF6, "Space character", inline=True)
comment(0x8FF8, "Check ADLC status register 2", inline=True)
comment(0x8FFB, "Clock present: skip warning", inline=True)
comment(0x8FFD, "Print ' No Clock' via inline", inline=True)
comment(0x9009, "NOP (string terminator)", inline=True)
comment(0x900D, "Return", inline=True)
comment(0x911B, "Save full byte", inline=True)
comment(0x911C, "Shift high nybble to low", inline=True)
comment(0x911D, "Continue shifting", inline=True)
comment(0x911E, "Continue shifting", inline=True)
comment(0x911F, "High nybble now in bits 0-3", inline=True)
comment(0x9120, "Print high nybble as hex digit", inline=True)
comment(0x9123, "Restore full byte", inline=True)
comment(0x9124, "Mask to low nybble", inline=True)
comment(0x9126, "Digit >= &0A?", inline=True)
comment(0x9128, "No: skip letter adjustment", inline=True)
comment(0x912A, "Add 7 to get 'A'-'F' (6 + carry)", inline=True)
comment(0x912C, "Add &30 for ASCII '0'-'9' or 'A'-'F'", inline=True)
comment(0x947D, "&FF padding (unused ROM space)", inline=True)


# ============================================================
# Service dispatch table (&89C0/&89E5)
# ============================================================
# 37-entry PHA/PHA/RTS dispatch table used by svc_dispatch.
# Indices 0-14: service dispatch (index = mapped service code + 1).
# Indices 15-36: extended dispatch for FS commands and OSWORD routing.
# Service codes 1-12 map directly; 18 maps to index 14 via SBC #5.
# Indices 1, 7, 11 point to &8E42 (RTS = no-op).

comment(0x89C0, """\
Service dispatch table (37 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_dispatch.
Indices 0-14: service calls (index = service + 1).
Indices 15-36: FS command and OSWORD routing.
Indices 1, 7, 11 point to return_4 (no-op RTS).""")

label(0x89C0, "svc_dispatch_lo")
label(0x89E5, "svc_dispatch_hi")

# Mark dispatch table entries as symbolic address pairs.
# Skip index 0 (&CB05 — outside ROM range, unused dispatch slot).
for i in range(1, 37):
    rts_code_ptr(0x89C0 + i, 0x89E5 + i)

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
for i, body in enumerate(svc_dispatch_comments):
    comment(0x89C0 + i, f"lo - {body}", inline=True)
    comment(0x89E5 + i, f"hi - {body}", inline=True)

# Service dispatch targets — already labelled
# Index 6 (svc 5): &8023 = svc5_irq_check (unrecognised interrupt)
# Index 12 (svc 11): &8085 = svc_11_nmi_claim (NMI claim)
# Index 13 (svc 12): &8979 = wait_idle_and_reset (NMI release)

# Service dispatch targets — new entry points
entry(0x8E8F)   # Index 2 (svc 1): absolute workspace claim
entry(0x8EA2)   # Index 3 (svc 2): private workspace
entry(0x8CBF)   # Index 4 (svc 3): auto-boot
entry(0x8C43)   # Index 5 (svc 4): unrecognised star command
entry(0x8E7C)   # Index 8 (svc 7): unrecognised OSBYTE
entry(0xA4D6)   # Index 9 (svc 8): unrecognised OSWORD
entry(0x8C52)   # Index 10 (svc 9): *HELP
entry(0x8B05)   # Index 14 (svc 18): filing system selection

label(0x8E8F, "svc_1_abs_workspace")
label(0x8EA2, "svc_2_private_workspace")
label(0x8CBF, "svc_3_autoboot")
label(0x8C43, "svc_4_star_command")
label(0x8E7C, "svc_7_osbyte")
label(0xA4D6, "svc_8_osword")
label(0x8C52, "svc_9_help")
label(0x8B05, "svc_18_fs_select")

subroutine(0x8E8F, "svc_1_abs_workspace",
    title="Service 1: absolute workspace claim",
    description="Ensures the NFS workspace allocation is at least\n"
    "&16 pages by checking Y on entry. If Y < &16,\n"
    "sets Y = &16 to claim the required pages;\n"
    "otherwise returns Y unchanged. This is a passive\n"
    "claim — NFS only raises the allocation, never\n"
    "lowers it.",
    on_entry={"y": "current highest workspace page claim"},
    on_exit={"y": ">= &16 (NFS minimum requirement)"})
subroutine(0x8EA2, "svc_2_private_workspace",
    title="Service 2: claim private workspace and initialise NFS",
    description="Handles MOS service call 2 (private workspace\n"
    "claim). Allocates two workspace pages starting\n"
    "at Y: the receive block page (net_rx_ptr_hi) and\n"
    "NFS workspace page (nfs_workspace_hi), plus a\n"
    "per-ROM workspace page stored at &0DF0+ROM slot.\n"
    "Zeroes all workspace, initialises the station ID\n"
    "from the Econet hardware register at &FE18,\n"
    "allocates FS handle pages, copies initial state\n"
    "to page &10, and falls through to\n"
    "init_adlc_and_vectors.",
    on_entry={"y": "first available private workspace page"})
subroutine(0x8CBF, "svc_3_autoboot",
    title="Service 3: auto-boot on reset",
    description="Scans the keyboard via OSBYTE &7A for the 'N' key\n"
    "(&19 or &55 EOR'd with &55). If pressed, records\n"
    "the key state via OSBYTE &78. Selects the network\n"
    "filing system by calling cmd_net_fs, prints the\n"
    "station ID, then checks if this is the first boot\n"
    "(ws_page = 0). If so, sets the auto-boot flag in\n"
    "&1071 and JMPs to cmd_fs_entry to execute the boot\n"
    "file.")
subroutine(0x8C43, "svc_4_star_command",
    title="Service 4: unrecognised star command",
    description="Saves the OS text pointer, then calls match_fs_cmd\n"
    "to search the command table starting at offset 0\n"
    "(all FS commands). If no match is found (carry\n"
    "set), returns with the service call unclaimed. On\n"
    "a match, JMPs to cmd_fs_reentry to execute the\n"
    "matched command handler via the PHA/PHA/RTS\n"
    "dispatch mechanism.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8E7C, "svc_7_osbyte",
    title="Service 7: unrecognised OSBYTE",
    description="Maps Econet OSBYTE codes &32-&35 to dispatch\n"
    "indices 0-3 by subtracting &31 (with carry from\n"
    "a preceding SBC). Returns unclaimed if the OSBYTE\n"
    "number is outside this range. For valid codes,\n"
    "claims the service (sets svc_state to 0) and\n"
    "JMPs to svc_dispatch with Y=&21 to reach the\n"
    "Econet OSBYTE handler table.",
    on_entry={"a": "OSBYTE number (from osbyte_a_copy at &EF)"})
subroutine(0xA4D6, "svc_8_osword",
    title="Filing system OSWORD entry",
    description="Handles MOS service call 8 (unrecognised OSWORD).\n"
    "Filters OSWORD codes &0E-&14 by subtracting &0E (via\n"
    "CLC/SBC &0D) and rejecting values outside 0-6. For\n"
    "valid codes, calls osword_setup_handler to push the\n"
    "dispatch address, then copies 3 bytes from the RX\n"
    "buffer to osword_flag workspace.")
subroutine(0x8C52, "svc_9_help",
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
subroutine(0x8B05, "svc_18_fs_select",
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
entry(0x95B8)
entry(0x956A)
entry(0xAC86)
entry(0x9598)
entry(0x95A8)
entry(0x9DBC)
entry(0x9DE2)
entry(0xA1A9)
entry(0xA0FC)
entry(0xAD6E)
entry(0x8F80)
entry(0x929C)
entry(0xAF1E)
entry(0xA379)
entry(0xA383)
entry(0xA2DC)
entry(0xA2E2)
entry(0xA0CC)
entry(0xA0D2)
entry(0xA0E2)


# ============================================================
# Star command table (&A3D8-&A4D5)
# ============================================================
# Four sub-tables of star command entries. Each entry:
# ASCII command name + flag byte (>= &80) + lo byte + hi byte.
# Tables separated by &80 sentinel bytes.

comment(0xA3D8, """\
Star command table (4 interleaved sub-tables).
Each entry: ASCII name + flag byte (&80+) +
lo/hi dispatch address (PHA/PHA/RTS, address-1).
Sub-tables separated by &80 sentinel bytes.
1: FS commands  2: NFS commands
3: Net/Utils    4: Copro commands""")

label(0xA3D8, "cmd_table_fs")
label(0xA422, "cmd_table_nfs")
label(0xA49A, "cmd_table_net")
label(0xA4AB, "cmd_table_copro")

# Sub-table 1: file server commands
# Table stores address-1 for PHA/PHA/RTS dispatch; actual targets are +1.
entry(0xB97F)   # *Close
entry(0xBA06)   # *Dump
entry(0x8B0E)   # *Net (file server)
entry(0xB19F)   # *Pollps
entry(0xB988)   # *Print
entry(0xB2F0)   # *Prot
entry(0xAFCE)   # *PS
entry(0xB985)   # *Type
entry(0xB321)   # *Unprot
entry(0x8ACC)   # *Roff

# Mark lo/hi dispatch bytes as symbolic label expressions.
# Each entry: (lo_addr, hi_addr, target_label).
_cmd_entries = [
    # Sub-table 1: FS commands
    (0xA3DE, 0xA3DF, "cmd_close"),
    (0xA3E5, 0xA3E6, "cmd_dump"),
    (0xA3EB, 0xA3EC, "cmd_net_fs"),
    (0xA3F4, 0xA3F5, "cmd_pollps"),
    (0xA3FC, 0xA3FD, "cmd_print"),
    (0xA403, 0xA404, "cmd_prot"),
    (0xA408, 0xA409, "cmd_ps"),
    (0xA40F, 0xA410, "cmd_roff"),
    (0xA416, 0xA417, "cmd_type"),
    (0xA41F, 0xA420, "cmd_unprot"),
    # Sub-table 2: NFS commands
    (0xA429, 0xA42A, "cmd_fs_operation"),   # *Access
    (0xA42F, 0xA430, "cmd_bye"),
    (0xA436, 0xA437, "cmd_cdir"),
    (0xA43F, 0xA440, "cmd_fs_operation"),   # *Delete
    (0xA445, 0xA446, "cmd_dir"),
    (0xA44A, 0xA44B, "cmd_ex"),
    (0xA451, 0xA452, "cmd_flip"),
    (0xA456, 0xA457, "cmd_fs"),
    (0xA45D, 0xA45E, "cmd_fs_operation"),   # *Info
    (0xA464, 0xA465, "cmd_iam"),
    (0xA46B, 0xA46C, "cmd_lcat"),
    (0xA471, 0xA472, "cmd_lex"),
    (0xA477, 0xA478, "cmd_fs_operation"),   # *Lib
    (0xA47E, 0xA47F, "cmd_pass"),
    (0xA487, 0xA488, "cmd_remove"),
    (0xA490, 0xA491, "cmd_rename"),
    (0xA497, 0xA498, "cmd_wipe"),
    # Sub-table 3: Net/Utils commands
    (0xA4A0, 0xA4A1, "cmd_net_local"),
    (0xA4A8, 0xA4A9, "cmd_utils"),
    # Sub-table 4 (copro) skipped — targets outside ROM range
]
for lo_addr, hi_addr, target_label in _cmd_entries:
    byte(lo_addr)
    expr(lo_addr, make_lo(target_label + "-1"))
    byte(hi_addr)
    expr(hi_addr, make_hi(target_label + "-1"))

label(0xB97F, "cmd_close")
label(0xBA06, "cmd_dump")
label(0x8B0E, "cmd_net_fs")
label(0xB19F, "cmd_pollps")
label(0xB988, "cmd_print")
label(0xB2F0, "cmd_prot")
label(0xAFCE, "cmd_ps")
label(0xB985, "cmd_type")
label(0xB321, "cmd_unprot")
label(0x8ACC, "cmd_roff")

subroutine(0xB97F, "cmd_close",
    title="*Close command handler",
    description="Loads A=0 and Y=0, then jumps to OSFIND to close\n"
    "all open files. Just 3 instructions.")
subroutine(0xBA06, "cmd_dump",
    title="*Dump command handler",
    description="Opens the file via open_file_for_read, allocates a\n"
    "21-byte buffer on the stack, and parses the address\n"
    "range via init_dump_buffer. Loops reading 16 bytes\n"
    "per line, printing each as a 4-byte hex address,\n"
    "16 hex bytes with spaces, and a 16-character ASCII\n"
    "column (non-printable chars shown as '.'). Prints\n"
    "a column header at every 256-byte boundary.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8B0E, "cmd_net_fs",
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
    "then issues service call 15.")
subroutine(0xB19F, "cmd_pollps",
    title="*Pollps command handler",
    description="Initialises the spool drive, copies the PS name to\n"
    "the TX buffer, and parses an optional station number\n"
    "or PS name argument. Sends a poll request, then\n"
    "prints the server address and name. Iterates through\n"
    "PS slots, displaying each station's status as\n"
    "'ready', 'busy' (with client station), or 'jammed'.\n"
    "Marks processed slots with &3F.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB988, "cmd_print",
    title="*Print command handler",
    description="Sets V flag (distinguishing from *Type which clears V),\n"
    "then opens the file for reading. Loops reading bytes\n"
    "via OSBGET, checking for escape between each. In type\n"
    "mode (V clear), normalises CR/LF pairs to single\n"
    "newlines by tracking the previous character. In print\n"
    "mode (V set), outputs all bytes raw via OSWRCH. Closes\n"
    "the file and prints a final newline on EOF.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB2F0, "cmd_prot",
    title="*Prot command handler",
    description="With no arguments, sets all protection bits (&FF).\n"
    "Otherwise parses attribute keywords via match_fs_cmd\n"
    "with table offset &D3, accumulating bits via ORA.\n"
    "Stores the final protection mask in ws_0d68 and\n"
    "ws_0d69.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xAFCE, "cmd_ps",
    title="*PS command handler",
    description="Checks the printer server availability flag; raises\n"
    "'Printer busy' if unavailable. Initialises the spool\n"
    "drive and buffer pointer, then dispatches on argument\n"
    "type: no argument branches to no_ps_name_given, a\n"
    "leading digit branches to save_ps_cmd_ptr as a station\n"
    "number, otherwise parses a named PS address via\n"
    "load_ps_server_addr and parse_fs_ps_args.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB985, "cmd_type",
    title="*Type command handler",
    description="Clears V and branches to the shared open_and_read_file\n"
    "entry in cmd_print. The V-clear state selects line-\n"
    "ending normalisation mode, converting CR/LF or LF/CR\n"
    "pairs to single newlines.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xB321, "cmd_unprot",
    title="*Unprot command handler",
    description="With no arguments, clears all protection bits (EOR\n"
    "yields 0). Otherwise parses attribute keywords, clearing\n"
    "bits via AND with the complement. Shares the protection\n"
    "mask storage path with cmd_prot. Falls through to\n"
    "cmd_wipe.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8ACC, "cmd_roff",
    title="*ROFF command handler",
    description="Disables remote operation by clearing the flag at\n"
    "offset 4 in the receive block. If remote operation\n"
    "was active, re-enables the keyboard via OSBYTE &C9\n"
    "(with X=0, Y=0) and calls tx_econet_abort with\n"
    "A=&0A to reinitialise the workspace area. Falls\n"
    "through to scan_remote_keys which clears svc_state\n"
    "and nfs_workspace.")

# Sub-table 2: NFS commands
entry(0x92D2)   # *Access, *Delete, *Info, *Lib (shared entry)
entry(0x948A)   # *Bye
entry(0xACFE)   # *Cdir
entry(0x93C9)   # *Dir
entry(0xAD59)   # *Ex
entry(0xA33E)   # *Flip
entry(0xA063)   # *FS
entry(0x8D6E)   # *I am
entry(0xAD4D)   # *Lcat
entry(0xAD53)   # *Lex
entry(0x8DB1)   # *Pass
entry(0xAF46)   # *Remove
entry(0x9377)   # *Rename
entry(0xB33D)   # *Wipe

label(0x92D2, "cmd_fs_operation")
label(0x948A, "cmd_bye")
label(0xACFE, "cmd_cdir")
label(0x93C9, "cmd_dir")
label(0xAD59, "cmd_ex")
label(0xA33E, "cmd_flip")
label(0xA063, "cmd_fs")
label(0x8D6E, "cmd_iam")
label(0xAD4D, "cmd_lcat")
label(0xAD53, "cmd_lex")
label(0x8DB1, "cmd_pass")
label(0xAF46, "cmd_remove")
label(0x9377, "cmd_rename")
label(0xB33D, "cmd_wipe")

subroutine(0x92D2, "cmd_fs_operation",
    title="Shared *Access/*Delete/*Info/*Lib command handler",
    description="Copies the command name to the TX buffer, parses a\n"
    "quoted filename argument via parse_quoted_arg, and\n"
    "checks the access prefix. Validates the filename\n"
    "does not start with '&', then falls through to\n"
    "read_filename_char to copy remaining characters and\n"
    "send the request. Raises 'Bad file name' if a bare\n"
    "CR is found where a filename was expected.")
subroutine(0x948A, "cmd_bye",
    title="*Bye command handler",
    description="Closes all open file control blocks via\n"
    "process_all_fcbs, shuts down any *SPOOL/*EXEC files\n"
    "with OSBYTE &77, and closes all network channels.\n"
    "Falls through to save_net_tx_cb with function code\n"
    "&17 to send the bye request to the file server.")
subroutine(0xACFE, "cmd_cdir",
    title="*CDir command handler",
    description="Parses an optional allocation size argument: if absent,\n"
    "defaults to index 2; if present, parses the decimal value\n"
    "and searches a 27-entry threshold table to find the\n"
    "matching allocation size index. Parses the directory name\n"
    "via parse_filename_arg, copies it to the TX buffer, and\n"
    "sends FS command code &1B to create the directory.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x93C9, "cmd_dir",
    title="*Dir command handler",
    description="Handles three argument syntaxes: a plain path\n"
    "(delegates to pass_send_cmd), '&' alone for the root\n"
    "directory, and '&N.dir' for cross-filesystem directory\n"
    "changes. The cross-FS form sends a file server\n"
    "selection command (code &12) to locate the target\n"
    "server, raising 'Not found' on failure, then sends\n"
    "the directory change (code 6) and calls\n"
    "find_fs_and_exit to update the active FS context.")
subroutine(0xAD59, "cmd_ex",
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
subroutine(0xA33E, "cmd_flip",
    title="*Flip command handler",
    description="Saves the file server station byte (&0E03), loads the\n"
    "boot type flag from &0E04, and calls find_station_bit3\n"
    "to locate the station table entry. Restores the station\n"
    "byte to Y and falls through to flip_set_station_boot\n"
    "to toggle the auto-boot setting.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xA063, "cmd_fs",
    title="*FS command handler",
    description="Saves the current file server station address, then\n"
    "checks for a command-line argument. With no argument,\n"
    "falls through to print_current_fs to display the active\n"
    "server. With an argument, parses the station number via\n"
    "parse_fs_ps_args and issues OSWORD &13 (sub-function 1)\n"
    "to select the new file server.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8D6E, "cmd_iam",
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
    "cmd_pass for password entry.")
subroutine(0xAD4D, "cmd_lcat",
    title="*LCat command handler",
    description="Sets the library flag by rotating SEC into bit 7 of\n"
    "l1071, then branches to cat_set_lib_flag inside cmd_ex\n"
    "to catalogue the library directory with three entries\n"
    "per column.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0xAD53, "cmd_lex",
    title="*LEx command handler",
    description="Sets the library flag by rotating SEC into bit 7 of\n"
    "l1071, then branches to ex_set_lib_flag inside cmd_ex\n"
    "to examine the library directory with one entry per line.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x8DB1, "cmd_pass",
    title="*PASS command handler (change password)",
    description="Builds the FS command packet via copy_arg_to_buf_x0,\n"
    "then scans the reply buffer for a ':' separator\n"
    "indicating a password prompt. If found, reads\n"
    "characters from the keyboard without echo, handling\n"
    "Delete (&7F) for backspace and NAK (&15) to restart\n"
    "from the colon position. Sends the completed\n"
    "password to the file server via save_net_tx_cb and\n"
    "branches to send_cmd_and_dispatch for the reply.")
subroutine(0xAF46, "cmd_remove",
    title="*Remove command handler",
    description="Validates that exactly one argument is present — raises\n"
    "'Syntax' if extra arguments follow. Parses the filename\n"
    "via parse_filename_arg, copies it to the TX buffer, and\n"
    "sends FS command code &14 (*Delete) with the V flag set\n"
    "via BIT for save_net_tx_cb_vset dispatch.",
    on_entry={"y": "command line offset in text pointer"})
subroutine(0x9377, "cmd_rename",
    title="*Rename command handler",
    description="Parses two space-separated filenames from the\n"
    "command line, each with its own access prefix.\n"
    "Sets the owner-only access mask before parsing each\n"
    "name. Validates that both names resolve to the same\n"
    "file server by comparing the FS options word —\n"
    "raises 'Bad rename' if they differ. Falls through\n"
    "to read_filename_char to copy the second filename\n"
    "into the TX buffer and send the request.")
subroutine(0xB33D, "cmd_wipe",
    title="*Wipe command handler",
    description="Masks owner access, parses a wildcard filename, and\n"
    "loops sending examine requests to the file server.\n"
    "Skips locked files and non-empty directories. Shows\n"
    "each filename with a '(Y/N/?) ' prompt — '?' shows\n"
    "full file info with a '(Y/N) ' reprompt, 'Y' builds\n"
    "the delete command in the TX buffer. Falls through to\n"
    "flush_and_read_char on completion.",
    on_entry={"y": "command line offset in text pointer"})

# Sub-table 3: Net/Utils commands
entry(0x8B8B)   # *Net (second variant)
entry(0x8B87)   # *Utils

label(0x8B8B, "cmd_net_local")
label(0x8B87, "cmd_utils")

subroutine(0x8B8B, "cmd_net_local",
    title="*Net command (local variant)",
    description="Sets X to &4A (the NFS command sub-table offset)\n"
    "and falls through to print_cmd_table to display\n"
    "the NFS command list with version header.")
subroutine(0x8B87, "cmd_utils",
    title="*Utils command handler",
    description="Sets X=0 to select the first (FS) command\n"
    "sub-table and branches to print_cmd_table to\n"
    "display the command list. Prints the version\n"
    "header followed by all FS utility commands.")


# ============================================================
# Additional code entry points (undecoded blocks)
# ============================================================
# These blocks follow decoded code (usually after an RTS or inline
# data) and start with valid 6502 opcodes. Adding entry points
# causes py8dis to trace execution from these addresses.

entry(0x8C28)   # After svc_9_help return
entry(0x92A1)   # After cmd_fs_operation utility code
entry(0x9921)   # Referenced from FS option handler table
entry(0x9BAF)   # Large undecoded block (266 bytes)
entry(0x9CC8)   # After &9CB8 block
entry(0x9E23)   # Large undecoded block (157 bytes)
entry(0x9F55)   # Large undecoded block (203 bytes)
entry(0xA8D0)   # Large undecoded block (220 bytes)
entry(0xA9D0)   # After &A9CF code
entry(0xAADB)   # After &AACF data table
entry(0xB7CF)   # File operation handler
entry(0xB865)   # File operation handler

# Smaller undecoded blocks with valid first opcodes
entry(0x84B1)   # After dispatch table data
entry(0x84C1)   # After &84B1 block
entry(0x88D8)   # 16 bytes after NMI code
entry(0xA58B)   # 118-byte undecoded block
entry(0xA61C)   # 552-byte undecoded block (largest remaining)
entry(0xA968)   # 68-byte undecoded block
entry(0xAA9F)   # 49-byte undecoded block
entry(0xB850)   # 21-byte file handler block

# Page 5 relocated code — ANFS-specific entry points
# Runtime addresses for undecoded blocks in page 5 source (&BC90)
entry(0x0542)   # tube_osfind (ANFS variant)
entry(0x0564)   # read_osargs_params (ANFS variant)
entry(0x05AB)   # argsw (ANFS variant)
entry(0x05D3)   # read_osgbpb_ctrl_blk (ANFS variant)


# ============================================================
# Data tables in main ROM
# ============================================================

# ============================================================
# FS vector dispatch and handler addresses (&8E4B)
# ============================================================
subroutine(0x8E4B, "fs_vector_table",
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
for i, name in enumerate(["FILEV", "ARGSV", "BGETV", "BPUTV",
                           "GBPBV", "FINDV", "FSCV"]):
    addr = 0x8E4B + i * 2
    word(addr)
    comment(addr, f"{name} dispatch (&FF{0x1B + i * 3:02X})", inline=True)

# Part 2: handler address entries (7 x {lo, hi, pad})
# write_vector_entry reads lo/hi from svc_dispatch_lo_offset+Y.
# With Y=&1B, that's &8E3E+&1B = &8E59.
handler_names = [
    ("FILEV",  0x9921),
    ("ARGSV",  0x9BAF),
    ("BGETV",  0xB7CF),
    ("BPUTV",  0xB850),
    ("GBPBV",  0x9E23),
    ("FINDV",  0x9D42),
    ("FSCV",   0x8E1D),
]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x8E59 + i * 3
    word(base_addr)
    comment(base_addr, f"{name} handler (&{handler_addr:04X})", inline=True)
    if i < 6:  # pad byte for all but last entry
        byte(base_addr + 2, 1)
        comment(base_addr + 2, "(ROM bank — not read)", inline=True)

# "PRINT " string at &8E43
label(0x8E43, "print_string")

# Command syntax help strings (&900D-&910C)
label(0x900D, "syntax_strings")

# Error message table (&97A4)
label(0x97A4, "error_msg_table")

# Credits string
label(0x8C98, "version_string")
label(0x8D2E, "credits_string")

# Boot command strings
label(0xA3B6, "boot_load_cmd")
label(0xA3BF, "boot_exec_cmd")


# ============================================================
# Additional ROM subroutines (from code analysis)
# ============================================================

# Subroutine at &8E33: PHA/PHA/RTS dispatch via svc_dispatch tables.
# On entry: X=base index, Y=offset. Dispatches to table[X+Y+1].
subroutine(0x8E33, "svc_dispatch",
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
label(0x8E33, "svc_dispatch")

# sub_c8a97: read byte from paged ROM via OSRDSC
subroutine(0x8A97, "read_paged_rom",
    title="Read next byte from paged ROM via OSRDSC",
    description="Increments the read pointer at osrdsc_ptr (&F6)\n"
    "first, then calls OSRDSC (&FFB9) with the ROM\n"
    "number from error_block (&0100) in Y. Called\n"
    "three times by service_handler during ROM\n"
    "identification to read the copyright string and\n"
    "ROM type byte.",
    on_exit={"a": "byte read from ROM"})
label(0x8A97, "read_paged_rom")

# sub_c8e6d / sub_c8e6f: OSBYTE with X=0 / OSBYTE with Y=&FF
subroutine(0x8E6D, "osbyte_x0",
    title="OSBYTE wrapper with X=0, Y=&FF",
    description="Sets X=0 and falls through to osbyte_yff to also\n"
    "set Y=&FF. Provides a single call to execute\n"
    "OSBYTE with A as the function code. Used by\n"
    "adlc_init, init_adlc_and_vectors, and Econet\n"
    "OSBYTE handling.",
    on_entry={"a": "OSBYTE function code"},
    on_exit={"x": "0", "y": "&FF"})
subroutine(0x8E6F, "osbyte_yff",
    title="OSBYTE wrapper with Y=&FF",
    description="Sets Y=&FF and JMPs to the MOS OSBYTE entry\n"
    "point. X must already be set by the caller. The\n"
    "osbyte_x0 entry point falls through to here after\n"
    "setting X=0.",
    on_entry={"a": "OSBYTE function code",
              "x": "OSBYTE X parameter"},
    on_exit={"y": "&FF"})
label(0x8E6D, "osbyte_x0")
label(0x8E6F, "osbyte_yff")


# ============================================================
# Inline string subroutines — descriptions and comments
# ============================================================
# Label and code-tracing hooks created by hook_subroutine() above.

subroutine(0x9131,
    title="Print inline string, high-bit terminated",
    description="""\
Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. Common terminators are
&EA (NOP) for fall-through and &B8 (CLV) followed by BVC for an
unconditional forward branch.""",
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)",
             "x": "corrupted (by OSASCI)",
             "y": "0"})

comment(0x9131, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x9134, "Pop return address (high)", inline=True)
comment(0x9139, "Advance pointer to next character", inline=True)
comment(0x913F, "Load next byte from inline string", inline=True)
comment(0x9141, "Bit 7 set? Done — this byte is the next opcode", inline=True)
comment(0x9149, "Reload character (pointer may have been clobbered)", inline=True)
comment(0x914B, "Print character via OSASCI", inline=True)
comment(0x9157, "Jump to address of high-bit byte (resumes code)", inline=True)

subroutine(0x96BE,
    title="Generate BRK error from inline string",
    description="""\
Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""",
    on_entry={"a": "error number"})

comment(0x96BE, "Save error number in Y", inline=True)
comment(0x96BF, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x96C2, "Pop return address (high)", inline=True)

subroutine(0x96BB,
    title="Generate BRK error from inline string (with logging)",
    description="""\
Like error_inline, but first conditionally logs the error code to
workspace via sub_c95fb before building the error block.""",
    on_entry={"a": "error number"})

comment(0x96BB, "Conditionally log error code to workspace", inline=True)

subroutine(0x96A2,
    title="Generate 'Bad ...' BRK error from inline string",
    description="""\
Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""",
    on_entry={"a": "error number"})

comment(0x96A2, "Conditionally log error code to workspace", inline=True)
comment(0x96A5, "Save error number in Y", inline=True)
comment(0x96A6, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x96A7, "Store return address low", inline=True)
comment(0x96A9, "Pop return address (high)", inline=True)
comment(0x96AA, "Store return address high", inline=True)
comment(0x96AC, "X=0: start of prefix string", inline=True)
comment(0x96AE, "Copy 'Bad ' prefix from lookup table", inline=True)
comment(0x96AF, "Get next prefix character", inline=True)
comment(0x96B2, "Store in error text buffer", inline=True)
comment(0x96B5, "Is it space (end of 'Bad ')?", inline=True)
comment(0x96B7, "No: copy next prefix character", inline=True)
comment(0x96C7, "Store error number in error block", inline=True)
comment(0x96CE, "Zero the BRK byte at &0100", inline=True)
comment(0x96D1, "Copy inline string into error block", inline=True)
comment(0x96D3, "Read next byte from inline string", inline=True)
comment(0x96D8, "Loop until null terminator", inline=True)

# "Bad " prefix table
label(0x969E, "bad_prefix")


# ============================================================
# FS command inline comments (Phase 4)
# ============================================================

# cmd_cdir (&ACFE) — *CDir: create directory
comment(0xACFE, "Save command line offset", inline=True)
comment(0xACFF, "Push onto stack", inline=True)
comment(0xAD00, "Set owner-only access mask", inline=True)
comment(0xAD03, "Skip to optional size argument", inline=True)
comment(0xAD06, "End of line?", inline=True)
comment(0xAD08, "No: parse size argument", inline=True)
comment(0xAD0A, "Default allocation size index = 2", inline=True)
comment(0xAD0E, "A=&FF: mark as decimal parse", inline=True)
comment(0xAD10, "Store decimal parse flag", inline=True)
comment(0xAD12, "Parse numeric size argument", inline=True)
comment(0xAD15, "X=&1B: top of 27-entry size table", inline=True)
comment(0xAD17, "Try next lower index", inline=True)
comment(0xAD18, "Compare size with threshold", inline=True)
comment(0xAD1B, "A < threshold: keep searching", inline=True)
comment(0xAD1D, "Store allocation size index", inline=True)
comment(0xAD20, "Restore command line offset", inline=True)
comment(0xAD21, "Transfer to Y", inline=True)
comment(0xAD22, "Save text pointer for filename parse", inline=True)
comment(0xAD25, "Parse directory name argument", inline=True)
comment(0xAD28, "X=1: one argument to copy", inline=True)
comment(0xAD2A, "Copy directory name to TX buffer", inline=True)
comment(0xAD2D, "Y=&1B: *CDir FS command code", inline=True)
comment(0xAD2F, "Send command to file server", inline=True)

# cmd_lcat (&AD4D) — *LCat: library catalogue
comment(0xAD4D, "Rotate carry into lib flag bit 7", inline=True)
comment(0xAD50, "Set carry (= library directory)", inline=True)

# cmd_lex (&AD53) — *LEx: library examine
comment(0xAD53, "Rotate carry into lib flag bit 7", inline=True)
comment(0xAD56, "Set carry (= library directory)", inline=True)

# cmd_prot (&B2F0) — *Prot: set file protection
comment(0xB2F0, "Get next char from command line", inline=True)
comment(0xB2F2, "Compare with CR (end of line)", inline=True)
comment(0xB2F4, "Not CR: attribute keywords follow", inline=True)
comment(0xB2F6, "A=&FF: protect all attributes", inline=True)
comment(0xB2FA, "Load current protection mask", inline=True)
comment(0xB2FD, "Save as starting value", inline=True)
comment(0xB2FE, "X=&D3: attribute keyword table offset", inline=True)
comment(0xB300, "Get next char from command line", inline=True)
comment(0xB302, "Save for end-of-args check", inline=True)
comment(0xB304, "Match attribute keyword in table", inline=True)
comment(0xB307, "No match: check if end of arguments", inline=True)
comment(0xB309, "Retrieve accumulated mask", inline=True)
comment(0xB30A, "OR in attribute bit for keyword", inline=True)
comment(0xB30D, "Save updated mask", inline=True)
comment(0xB30E, "Always non-zero after ORA: loop", inline=True)
comment(0xB310, "Get the unmatched character", inline=True)
comment(0xB312, "Is it CR?", inline=True)
comment(0xB314, "Yes: arguments ended correctly", inline=True)
comment(0xB316, "No: invalid attribute keyword", inline=True)
comment(0xB319, "Retrieve final protection mask", inline=True)
comment(0xB31A, "Store protection mask", inline=True)
comment(0xB31D, "Store protection mask copy", inline=True)
comment(0xB320, "Return", inline=True)

# cmd_unprot (&B321) — *Unprot: remove file protection
comment(0xB321, "Get next char from command line", inline=True)
comment(0xB323, "Compare with CR (end of line)", inline=True)
comment(0xB325, "No args: A=0 clears all protection", inline=True)
comment(0xB327, "Load current protection mask", inline=True)
comment(0xB32A, "Save as starting value", inline=True)
comment(0xB32B, "X=&D3: attribute keyword table offset", inline=True)
comment(0xB32D, "Get next char from command line", inline=True)
comment(0xB32F, "Save for end-of-args check", inline=True)
comment(0xB331, "Match attribute keyword in table", inline=True)
comment(0xB334, "No match: check if end of arguments", inline=True)
comment(0xB336, "Retrieve accumulated mask", inline=True)
comment(0xB337, "AND to clear matched attribute bit", inline=True)
comment(0xB33A, "Save updated mask", inline=True)

# cmd_fs_operation (&92D2) — shared handler for *Access, *Delete, *Info, *Lib
comment(0x92D2, "Copy command name to TX buffer", inline=True)
comment(0x92D5, "Save buffer position", inline=True)
comment(0x92D6, "Push it", inline=True)
comment(0x92D7, "Parse filename (handles quoting)", inline=True)
comment(0x92DA, "Parse owner/public access prefix", inline=True)
comment(0x92DD, "Restore buffer position", inline=True)
comment(0x92DE, "Transfer to X", inline=True)
comment(0x92DF, "Reject '&' character in filename", inline=True)
comment(0x92E2, "End of line?", inline=True)
comment(0x92E4, "No: copy filename chars to buffer", inline=True)
comment(0x92E6, "Error number &CC", inline=True)
comment(0x92E8, "Raise 'Bad file name' error", inline=True)
comment(0x92F5, "Load first parsed character", inline=True)
comment(0x92F8, "Is it '&'?", inline=True)
comment(0x92FA, "Yes: invalid filename", inline=True)
comment(0x92FC, "Return", inline=True)
comment(0x92FD, "Reject '&' in current char", inline=True)
comment(0x9300, "Store character in TX buffer", inline=True)
comment(0x9303, "Advance buffer pointer", inline=True)
comment(0x9304, "End of line?", inline=True)
comment(0x9306, "Yes: send request to file server", inline=True)
comment(0x9308, "Strip BASIC token prefix byte", inline=True)
comment(0x930B, "Continue reading filename chars", inline=True)
comment(0x930E, "Y=0: no extra dispatch offset", inline=True)
comment(0x9310, "Send command and dispatch reply", inline=True)
comment(0x9313, "Save command line offset", inline=True)
comment(0x9314, "Push it", inline=True)
comment(0x9315, "Scan backwards in command table", inline=True)
comment(0x9316, "Load table byte", inline=True)
comment(0x9319, "Bit 7 clear: keep scanning", inline=True)
comment(0x931B, "Point past flag byte to name start", inline=True)
comment(0x931C, "Y=0: TX buffer offset", inline=True)
comment(0x931E, "Load command name character", inline=True)
comment(0x9321, "Bit 7 set: end of name", inline=True)
comment(0x9323, "Store character in TX buffer", inline=True)
comment(0x9326, "Advance table pointer", inline=True)
comment(0x9327, "Advance buffer pointer", inline=True)
comment(0x9328, "Continue copying name", inline=True)
comment(0x932A, "Space separator", inline=True)
comment(0x932C, "Append space after command name", inline=True)
comment(0x932F, "Advance buffer pointer", inline=True)
comment(0x9330, "Transfer length to A", inline=True)
comment(0x9331, "And to X (buffer position)", inline=True)
comment(0x9332, "Restore command line offset", inline=True)
comment(0x9333, "Transfer to Y", inline=True)
comment(0x9334, "Return", inline=True)
comment(0x9335, "A=0: no quote mode", inline=True)
comment(0x9338, "Clear quote tracking flag", inline=True)
comment(0x933B, "Load char from command line", inline=True)
comment(0x933D, "Space?", inline=True)
comment(0x933F, "No: check for opening quote", inline=True)
comment(0x9341, "Skip leading space", inline=True)
comment(0x9342, "Continue skipping spaces", inline=True)
comment(0x9344, "Double-quote character?", inline=True)
comment(0x9346, "No: start reading filename", inline=True)
comment(0x9348, "Skip opening quote", inline=True)
comment(0x9349, "Toggle quote mode flag", inline=True)
comment(0x934C, "Store updated quote mode", inline=True)
comment(0x934F, "Load char from command line", inline=True)
comment(0x9351, "Double-quote?", inline=True)
comment(0x9353, "No: store character as-is", inline=True)
comment(0x9355, "Toggle quote mode", inline=True)
comment(0x9358, "Store updated quote mode", inline=True)
comment(0x935B, "Replace closing quote with space", inline=True)
comment(0x935D, "Store character in parse buffer", inline=True)
comment(0x9360, "Advance command line pointer", inline=True)
comment(0x9361, "Advance buffer pointer", inline=True)
comment(0x9362, "End of line?", inline=True)
comment(0x9364, "No: continue parsing", inline=True)
comment(0x9366, "Check quote balance flag", inline=True)
comment(0x9369, "Balanced: return OK", inline=True)
comment(0x936B, "Unbalanced: use BRK ptr for error", inline=True)
comment(0x936D, "Raise 'Bad string' error", inline=True)

# cmd_rename (&9377) — *Rename: rename file on server
comment(0x9377, "Copy 'Rename ' to TX buffer", inline=True)
comment(0x937A, "Save buffer position", inline=True)
comment(0x937B, "Push it", inline=True)
comment(0x937C, "Set owner-only access mask", inline=True)
comment(0x937F, "Parse first filename (quoted)", inline=True)
comment(0x9382, "Parse access prefix", inline=True)
comment(0x9385, "Restore buffer position", inline=True)
comment(0x9386, "Transfer to X", inline=True)
comment(0x9387, "Load next parsed character", inline=True)
comment(0x938A, "End of line?", inline=True)
comment(0x938C, "No: store character", inline=True)
comment(0x938E, "Error number &B0", inline=True)
comment(0x9390, "Raise 'Bad rename' error", inline=True)
comment(0x939A, "Store character in TX buffer", inline=True)
comment(0x939D, "Advance buffer pointer", inline=True)
comment(0x939E, "Space (name separator)?", inline=True)
comment(0x93A0, "Yes: first name complete", inline=True)
comment(0x93A2, "Strip BASIC token prefix byte", inline=True)
comment(0x93A5, "Continue copying first filename", inline=True)
comment(0x93A8, "Strip token from next char", inline=True)
comment(0x93AB, "Load next parsed character", inline=True)
comment(0x93AE, "Still a space?", inline=True)
comment(0x93B0, "Yes: skip multiple spaces", inline=True)
comment(0x93B2, "Save current FS options", inline=True)
comment(0x93B5, "Push them", inline=True)
comment(0x93B6, "Reset access mask for second name", inline=True)
comment(0x93B9, "Save buffer position", inline=True)
comment(0x93BA, "Push it", inline=True)
comment(0x93BB, "Parse access prefix for second name", inline=True)
comment(0x93BE, "Restore buffer position", inline=True)
comment(0x93BF, "Transfer to X", inline=True)
comment(0x93C0, "Restore original FS options", inline=True)
comment(0x93C1, "Options changed (cross-FS)?", inline=True)
comment(0x93C4, "Yes: error (can't rename across FS)", inline=True)
comment(0x93C6, "Copy second filename and send", inline=True)

# cmd_dir (&93C9) — *Dir: set current directory
comment(0x93C9, "Get first char of argument", inline=True)
comment(0x93CB, "Is it '&' (FS selector prefix)?", inline=True)
comment(0x93CD, "No: simple dir change", inline=True)
comment(0x93CF, "Skip '&'", inline=True)
comment(0x93D0, "Get char after '&'", inline=True)
comment(0x93D2, "End of line?", inline=True)
comment(0x93D4, "Yes: '&' alone (root directory)", inline=True)
comment(0x93D6, "Space?", inline=True)
comment(0x93D8, "No: check for '.' separator", inline=True)
comment(0x93DA, "Y=&FF: pre-increment for loop", inline=True)
comment(0x93DC, "Advance index", inline=True)
comment(0x93DD, "Load char from command line", inline=True)
comment(0x93DF, "Copy to TX buffer", inline=True)
comment(0x93E2, "Is it '&' (end of FS path)?", inline=True)
comment(0x93E4, "No: keep copying", inline=True)
comment(0x93E6, "Replace '&' with CR terminator", inline=True)
comment(0x93E8, "Store CR in buffer", inline=True)
comment(0x93EB, "Point past CR", inline=True)
comment(0x93EC, "Transfer length to A", inline=True)
comment(0x93ED, "And to X (byte count)", inline=True)
comment(0x93EE, "Send directory request to server", inline=True)
comment(0x93F1, "Is char after '&' a dot?", inline=True)
comment(0x93F3, "Yes: &FS.dir format", inline=True)
comment(0x93F5, "No: invalid syntax", inline=True)
comment(0x93F8, "Skip '.'", inline=True)
comment(0x93F9, "Save dir path start position", inline=True)
comment(0x93FB, "FS command 4: examine directory", inline=True)
comment(0x93FD, "Store in TX buffer", inline=True)
comment(0x9400, "Load FS flags", inline=True)
comment(0x9403, "Set bit 6 (FS selection active)", inline=True)
comment(0x9405, "Store updated flags", inline=True)
comment(0x9408, "X=1: buffer offset", inline=True)
comment(0x940A, "Copy FS number to buffer", inline=True)
comment(0x940D, "Y=&12: select FS command code", inline=True)
comment(0x940F, "Send FS selection command", inline=True)
comment(0x9412, "Load reply status", inline=True)
comment(0x9415, "Status 2 (found)?", inline=True)
comment(0x9417, "Yes: proceed to dir change", inline=True)
comment(0x9419, "Error number &D6", inline=True)
comment(0x941B, "Raise 'Not found' error", inline=True)
comment(0x9428, "Load current FS station byte", inline=True)
comment(0x942B, "Store in TX buffer", inline=True)
comment(0x942E, "X=1: buffer offset", inline=True)
comment(0x9430, "Y=7: change directory command code", inline=True)
comment(0x9432, "Send directory change request", inline=True)
comment(0x9435, "X=1", inline=True)
comment(0x9437, "Store start marker in buffer", inline=True)
comment(0x943A, "Store start marker in buffer+1", inline=True)
comment(0x943E, "Restore dir path start position", inline=True)
comment(0x9440, "Copy directory path to buffer", inline=True)
comment(0x9443, "Y=6: set directory command code", inline=True)
comment(0x9445, "Send set directory command", inline=True)
comment(0x9448, "Load reply handle", inline=True)
comment(0x944B, "Select FS and return", inline=True)
comment(0x944E, "Simple: pass command to FS", inline=True)

# init_txcb_bye / init_txcb_port / init_txcb (&9451-&9476)
comment(0x9451, "A=&90: bye command port", inline=True)
comment(0x9453, "Initialise TXCB from template", inline=True)
comment(0x9456, "Set transmit port", inline=True)
comment(0x9458, "A=3: data start offset", inline=True)
comment(0x945A, "Set TXCB start offset", inline=True)
comment(0x945C, "Decrement control byte", inline=True)
comment(0x945E, "Return", inline=True)
comment(0x945F, "Save A", inline=True)
comment(0x9460, "Y=&0B: template size - 1", inline=True)
comment(0x9462, "Load byte from TXCB template", inline=True)
comment(0x9465, "Store to TXCB workspace", inline=True)
comment(0x9468, "Index >= 2?", inline=True)
comment(0x946A, "Yes: skip dest station copy", inline=True)
comment(0x946C, "Load dest station byte", inline=True)
comment(0x946F, "Store to TXCB destination", inline=True)
comment(0x9472, "Decrement index", inline=True)
comment(0x9473, "More bytes: continue", inline=True)
comment(0x9475, "Restore A", inline=True)
comment(0x9476, "Return", inline=True)

# send_request_nowrite / send_request_write (&9483-&9488)
comment(0x9483, "Save A", inline=True)
comment(0x9484, "Set carry (read-only mode)", inline=True)
comment(0x9487, "Clear V", inline=True)

# cmd_flip (&A33E) — *Flip: toggle auto-boot configuration
comment(0xA33E, "Load FS station byte", inline=True)
comment(0xA341, "Save it", inline=True)
comment(0xA342, "Load boot type flag", inline=True)
comment(0xA345, "Find station entry with bit 3 set", inline=True)
comment(0xA348, "Restore FS station", inline=True)
comment(0xA349, "Transfer to Y (boot type)", inline=True)
comment(0xA34A, "X=&10: max 16 station entries", inline=True)
comment(0xA34C, "Clear V (no match found yet)", inline=True)
comment(0xA34D, "Decrement station index", inline=True)
comment(0xA34E, "All searched: exit loop", inline=True)
comment(0xA350, "Check if station[X] matches", inline=True)
comment(0xA353, "No match: try next station", inline=True)
comment(0xA355, "Load station flags byte", inline=True)
comment(0xA358, "Test bit 4 (active flag)", inline=True)
comment(0xA35A, "Not active: try next station", inline=True)
comment(0xA35C, "Transfer boot type to A", inline=True)
comment(0xA35D, "Store boot setting for station", inline=True)
comment(0xA360, "Set V flag (station match found)", inline=True)
comment(0xA363, "Store boot type", inline=True)
comment(0xA366, "V set (matched): skip allocation", inline=True)
comment(0xA368, "Boot type to A", inline=True)
comment(0xA369, "Allocate FCB slot for new entry", inline=True)
comment(0xA36C, "Store allocation result", inline=True)
comment(0xA36F, "Zero: allocation failed, exit", inline=True)
comment(0xA371, "A=&32: station flags (active+boot)", inline=True)
comment(0xA373, "Store station flags", inline=True)
comment(0xA376, "Restore FS context and return", inline=True)
comment(0xA379, "Close all network channels", inline=True)
comment(0xA37C, "Set carry flag", inline=True)
comment(0xA37D, "Load reply boot type", inline=True)
comment(0xA380, "Store as current boot type", inline=True)
comment(0xA383, "Save processor status", inline=True)
comment(0xA384, "Load station number from reply", inline=True)
comment(0xA387, "Find station entry with bit 2", inline=True)
comment(0xA38A, "Load network number from reply", inline=True)
comment(0xA38D, "Find station entry with bit 3", inline=True)
comment(0xA390, "Load boot type from reply", inline=True)
comment(0xA393, "Set boot config for station", inline=True)
comment(0xA396, "Restore processor status", inline=True)
comment(0xA397, "Carry set: proceed with boot", inline=True)
comment(0xA399, "Return with last flag", inline=True)
comment(0xA39C, "Load config flags", inline=True)
comment(0xA39F, "Save copy in X", inline=True)
comment(0xA3A0, "Test bit 2 (auto-boot flag)", inline=True)
comment(0xA3A2, "Save bit 2 test result", inline=True)
comment(0xA3A3, "Restore full flags", inline=True)
comment(0xA3A4, "Clear bit 2 (consume flag)", inline=True)
comment(0xA3A6, "Store cleared flags", inline=True)
comment(0xA3A9, "Restore bit 2 test result", inline=True)
comment(0xA3AA, "Bit 2 was set: skip to boot cmd", inline=True)
comment(0xA3AC, "OSBYTE &79: scan keyboard", inline=True)
comment(0xA3B4, "CTRL not pressed: proceed to boot", inline=True)
comment(0xA3B6, "CTRL pressed: cancel boot, return", inline=True)
comment(0xA3CB, "Load boot type", inline=True)
comment(0xA3CE, "Type 0: no command, just return", inline=True)
comment(0xA3D0, "Look up boot command address low", inline=True)
comment(0xA3D3, "Boot command address high (&A3xx)", inline=True)
comment(0xA3D5, "Execute boot command via OSCLI", inline=True)

# cmd_remove (&AF46) — *Remove: delete file from server
comment(0xAF46, "Save command line offset", inline=True)
comment(0xAF47, "Push onto stack", inline=True)
comment(0xAF48, "Skip to check for extra arguments", inline=True)
comment(0xAF4B, "End of line?", inline=True)
comment(0xAF4D, "Yes: single arg, proceed", inline=True)
comment(0xAF4F, "No: extra args, syntax error", inline=True)
comment(0xAF52, "Restore command line offset", inline=True)
comment(0xAF53, "Transfer to Y", inline=True)
comment(0xAF54, "Save text pointer for parsing", inline=True)
comment(0xAF57, "Parse filename argument", inline=True)
comment(0xAF5A, "Copy filename to TX buffer", inline=True)
comment(0xAF5D, "Y=&14: *Delete FS command code", inline=True)
comment(0xAF5F, "Set V flag (via BIT #&FF)", inline=True)
comment(0xAF62, "Send to FS with V-flag dispatch", inline=True)

# print_num_no_leading / print_decimal_3dig / print_decimal_digit
# Decimal number printing utility (&AF65-&AF94)
comment(0xAF65, "Set V (suppress leading zeros)", inline=True)
comment(0xAF68, "Transfer value to Y (remainder)", inline=True)
comment(0xAF69, "A=100: hundreds divisor", inline=True)
comment(0xAF6B, "Print hundreds digit", inline=True)
comment(0xAF6E, "A=10: tens divisor", inline=True)
comment(0xAF70, "Print tens digit", inline=True)
comment(0xAF73, "Clear V (always print units)", inline=True)
comment(0xAF74, "A=1: units divisor", inline=True)
comment(0xAF76, "Store divisor", inline=True)
comment(0xAF78, "Get remaining value", inline=True)
comment(0xAF79, "X='0'-1: digit counter", inline=True)
comment(0xAF7B, "Set carry for subtraction", inline=True)
comment(0xAF7C, "Save V flag for leading zero check", inline=True)
comment(0xAF7D, "Count quotient digit", inline=True)
comment(0xAF7E, "Subtract divisor", inline=True)
comment(0xAF80, "No underflow: continue dividing", inline=True)
comment(0xAF82, "Add back divisor (get remainder)", inline=True)
comment(0xAF84, "Remainder to Y for next digit", inline=True)
comment(0xAF85, "Digit character to A", inline=True)
comment(0xAF86, "Restore V flag", inline=True)
comment(0xAF87, "V clear: always print digit", inline=True)
comment(0xAF89, "V set: is digit '0'?", inline=True)
comment(0xAF8B, "Yes: suppress leading zero", inline=True)
comment(0xAF8D, "Save divisor across OSASCI call", inline=True)
comment(0xAF92, "Restore divisor", inline=True)
comment(0xAF94, "Return", inline=True)

# save_ptr_to_os_text (&AF95-&AF9F)
comment(0xAF95, "Save A", inline=True)
comment(0xAF96, "Copy text pointer low byte", inline=True)
comment(0xAF98, "To OS text pointer low", inline=True)
comment(0xAF9A, "Copy text pointer high byte", inline=True)
comment(0xAF9C, "To OS text pointer high", inline=True)
comment(0xAF9E, "Restore A", inline=True)
comment(0xAF9F, "Return", inline=True)

# skip_to_next_arg (&AFA0-&AFB4)
comment(0xAFA0, "Advance past current character", inline=True)
comment(0xAFA1, "Load char from command line", inline=True)
comment(0xAFA3, "Space?", inline=True)
comment(0xAFA5, "Yes: skip trailing spaces", inline=True)
comment(0xAFA7, "CR (end of line)?", inline=True)
comment(0xAFA9, "Yes: return (at end)", inline=True)
comment(0xAFAD, "Advance past space", inline=True)
comment(0xAFAE, "Load next character", inline=True)
comment(0xAFB0, "Still a space?", inline=True)
comment(0xAFB2, "Yes: skip multiple spaces", inline=True)
comment(0xAFB4, "Return (at next argument)", inline=True)

# save_ptr_to_spool_buf (&AFB5-&AFBF)
comment(0xAFB5, "Save A", inline=True)
comment(0xAFB6, "Copy text pointer low byte", inline=True)
comment(0xAFB8, "To spool buffer pointer low", inline=True)
comment(0xAFBA, "Copy text pointer high byte", inline=True)
comment(0xAFBC, "To spool buffer pointer high", inline=True)
comment(0xAFBE, "Restore A", inline=True)
comment(0xAFBF, "Return", inline=True)

# init_spool_drive (&AFC0-&AFCD)
comment(0xAFC0, "Save Y", inline=True)
comment(0xAFC1, "Push it", inline=True)
comment(0xAFC2, "Get workspace page number", inline=True)
comment(0xAFC5, "Store as spool drive page high", inline=True)
comment(0xAFC7, "Restore Y", inline=True)
comment(0xAFC8, "Transfer to Y", inline=True)
comment(0xAFC9, "A=0", inline=True)
comment(0xAFCB, "Clear spool drive page low", inline=True)
comment(0xAFCD, "Return", inline=True)

# cmd_close (&B97F) — *Close: close all files
comment(0xB97F, "A=0: close all open files", inline=True)

# cmd_type (&B985) — *Type: display file contents
comment(0xB985, "Clear V for unconditional BVC", inline=True)

# cmd_print (&B988) — *Print: send file to printer
comment(0xB988, "Set V flag (= print mode)", inline=True)

# open_and_read_file (&B98B) — shared entry for Print/Type
comment(0xB98B, "Open file for reading", inline=True)
comment(0xB990, "A = 0", inline=True)
comment(0xB992, "Clear previous-character tracker", inline=True)
comment(0xB994, "Save V flag (print/type mode)", inline=True)
comment(0xB998, "Branch if not end of file", inline=True)
comment(0xB99A, "EOF: restore processor status", inline=True)
comment(0xB99B, "Close the file", inline=True)

# Process character
comment(0xB9A1, "Check for escape key pressed", inline=True)
comment(0xB9A4, "Restore V (print/type mode)", inline=True)
comment(0xB9A5, "Re-save for next iteration", inline=True)
comment(0xB9A6, "Print mode: skip CR/LF handling", inline=True)
comment(0xB9A8, "Is it a carriage return?", inline=True)
comment(0xB9AA, "Yes: handle line ending", inline=True)
comment(0xB9AC, "Is it a line feed?", inline=True)
comment(0xB9AE, "Yes: handle line ending", inline=True)

# Output character
comment(0xB9B0, "Save as previous character", inline=True)
comment(0xB9B5, "Loop for next byte", inline=True)

# CR/LF handling in type mode
comment(0xB9B8, "Save the CR or LF character", inline=True)
comment(0xB9B9, "Check output destination flag", inline=True)
comment(0xB9BC, "Zero: normalise line endings", inline=True)
comment(0xB9BE, "Non-zero: output raw", inline=True)
comment(0xB9C0, "Clear previous-character tracker", inline=True)
comment(0xB9C2, "Retrieve CR/LF", inline=True)
comment(0xB9C3, "Output it directly; ALWAYS branch", inline=True)

# Line ending normalisation (l00ad tracks previous char)
comment(0xB9C5, "Get previous character", inline=True)
comment(0xB9C7, "Was previous a CR?", inline=True)
comment(0xB9C9, "Yes: check for CR+LF pair", inline=True)
comment(0xB9CB, "Was previous a LF?", inline=True)
comment(0xB9CD, "Yes: check for LF+CR pair", inline=True)
comment(0xB9CF, "Retrieve CR/LF from stack", inline=True)
comment(0xB9D0, "Save as previous character", inline=True)
comment(0xB9D5, "Loop for next byte", inline=True)

# Previous was CR — check for CR+LF pair
comment(0xB9D8, "Retrieve current character", inline=True)
comment(0xB9D9, "Is it LF? (CR+LF pair)", inline=True)
comment(0xB9DB, "Yes: consume LF, no extra newline", inline=True)
comment(0xB9DD, "No: output extra newline", inline=True)

# Previous was LF — check for LF+CR pair
comment(0xB9DF, "Retrieve current character", inline=True)
comment(0xB9E0, "Is it CR? (LF+CR pair)", inline=True)
comment(0xB9E2, "No: output extra newline", inline=True)

# Consume paired character
comment(0xB9E4, "Pair consumed: A = 0", inline=True)
comment(0xB9E6, "Clear previous-character tracker", inline=True)
comment(0xB9E8, "Loop for next byte; ALWAYS branch", inline=True)

# abort_if_escape (&B9EA) — abort file read on Escape
comment(0xB9EA, "Test bit 7 of escape flag", inline=True)
comment(0xB9EC, "Escape pressed: handle abort", inline=True)
comment(0xB9EE, "No escape: return", inline=True)
comment(0xB9EF, "Close the open file", inline=True)
comment(0xB9F5, "Acknowledge escape condition", inline=True)
comment(0xB9FA, "Error number &11", inline=True)
comment(0xB9FC, "Generate 'Escape' BRK error", inline=True)

# cmd_pollps (&B19F) — *PollPS: poll printer server status
# Entry and setup
comment(0xB19F, "Save command line pointer high", inline=True)
comment(0xB1A1, "Initialise spool/print drive", inline=True)
comment(0xB1A4, "Save spool drive number", inline=True)
comment(0xB1A6, "Copy PS name to TX buffer", inline=True)
comment(0xB1A9, "Init PS slot from RX data", inline=True)
comment(0xB1AC, "Restore command line pointer", inline=True)
comment(0xB1AE, "Save pointer to spool buffer", inline=True)
comment(0xB1B1, "Get first argument character", inline=True)
comment(0xB1B3, "End of command line?", inline=True)
comment(0xB1B5, "Yes: no argument given", inline=True)

# Argument parsing: check if PS name or station number
comment(0xB1B7, "Clear V (= explicit PS name given)", inline=True)
comment(0xB1B8, "Is first char a decimal digit?", inline=True)
comment(0xB1BB, "Yes: station number, skip PS name", inline=True)
comment(0xB1BD, "PS name follows", inline=True)
comment(0xB1BE, "Save Y", inline=True)
comment(0xB1BF, "Load PS server address", inline=True)
comment(0xB1C2, "Restore Y", inline=True)
comment(0xB1C3, "Back to Y register", inline=True)
comment(0xB1C4, "Parse FS/PS arguments", inline=True)
comment(0xB1C7, "Offset &7A in slot buffer", inline=True)
comment(0xB1C9, "Get parsed station low", inline=True)
comment(0xB1CB, "Store station number low", inline=True)
comment(0xB1CE, "Get parsed network number", inline=True)
comment(0xB1D0, "Store station number high", inline=True)
comment(0xB1D2, "Offset &14 in TX buffer", inline=True)
comment(0xB1D4, "Copy PS data to TX buffer", inline=True)
comment(0xB1D7, "Get buffer page high", inline=True)
comment(0xB1D9, "Set TX pointer high byte", inline=True)
comment(0xB1DB, "Offset &78 in buffer", inline=True)
comment(0xB1DD, "Set TX pointer low byte", inline=True)

# No argument path: set V flag
comment(0xB1E1, "Set V (= no explicit PS name)", inline=True)

# Station number path: fill PS name buffer
comment(0xB1E4, "V set (no arg): skip to send", inline=True)
comment(0xB1E6, "Max 6 characters for PS name", inline=True)
comment(0xB1E8, "Buffer offset for PS name", inline=True)
comment(0xB1EA, "Space character", inline=True)
comment(0xB1EC, "Fill buffer position with space", inline=True)
comment(0xB1EE, "Next position", inline=True)
comment(0xB1EF, "Count down", inline=True)
comment(0xB1F0, "Loop until 6 spaces filled", inline=True)
comment(0xB1F2, "Save pointer to OS text", inline=True)
comment(0xB1F5, "Restore command line pointer", inline=True)
comment(0xB1F7, "Initialise string reading", inline=True)
comment(0xB1FA, "Empty string: skip to send", inline=True)
comment(0xB1FC, "Max 6 characters", inline=True)
comment(0xB1FE, "Save updated string pointer", inline=True)
comment(0xB200, "Buffer offset for PS name", inline=True)
comment(0xB202, "Save buffer position", inline=True)

# Copy PS name from command line, uppercased
comment(0xB204, "Restore string pointer", inline=True)
comment(0xB206, "Read next char from string", inline=True)
comment(0xB209, "Save updated string pointer", inline=True)
comment(0xB20B, "End of string: go to send", inline=True)
comment(0xB20D, "Store char uppercased in buffer", inline=True)
comment(0xB210, "Loop if more chars to copy", inline=True)

# Send poll request and display header
comment(0xB212, "Enable escape checking", inline=True)
comment(0xB214, "Set escapable flag", inline=True)
comment(0xB216, "Send the poll request packet", inline=True)
comment(0xB219, "Pop and requeue PS scan", inline=True)
comment(0xB21C, "Print 'Printer server '", inline=True)
comment(0xB21F, "Load PS server address", inline=True)
comment(0xB222, "Set V and N flags", inline=True)
comment(0xB225, "Print station address", inline=True)
comment(0xB228, "Print ' \"'", inline=True)

# Display PS name from RX buffer
comment(0xB22D, "Start of PS name in buffer", inline=True)
comment(0xB22F, "Get character from name field", inline=True)
comment(0xB231, "Is it a space?", inline=True)
comment(0xB233, "Yes: end of name", inline=True)
comment(0xB238, "Next character", inline=True)
comment(0xB239, "Past end of name field?", inline=True)
comment(0xB23B, "No: continue printing name", inline=True)
comment(0xB23D, "Print '\"' + CR", inline=True)
comment(0xB242, "Padding byte", inline=True)

# Poll each printer slot
comment(0xB243, "Get slot offset from stack", inline=True)
comment(0xB244, "Zero: all slots done, return", inline=True)
comment(0xB246, "Save slot offset", inline=True)
comment(0xB247, "Transfer to Y", inline=True)
comment(0xB248, "Read slot status byte", inline=True)
comment(0xB24A, "Bit 7 clear: slot inactive", inline=True)
comment(0xB24C, "Advance to station number", inline=True)
comment(0xB24D, "Offset+2 in slot", inline=True)
comment(0xB24E, "Read station number low", inline=True)
comment(0xB250, "Store station low", inline=True)
comment(0xB252, "Next byte (offset+3)", inline=True)
comment(0xB253, "Read network number", inline=True)
comment(0xB255, "Store network number", inline=True)
comment(0xB257, "Next byte (offset+4)", inline=True)
comment(0xB258, "Read status page pointer", inline=True)
comment(0xB25A, "Store pointer low", inline=True)
comment(0xB25C, "Clear V flag", inline=True)
comment(0xB25D, "Print station address (V=0)", inline=True)
comment(0xB260, "Print ' is '", inline=True)

# Display printer status
comment(0xB267, "X=0 for indirect indexed access", inline=True)
comment(0xB269, "Read printer status byte", inline=True)
comment(0xB26B, "Non-zero: not ready", inline=True)
comment(0xB26D, "Print 'ready'", inline=True)
comment(0xB275, "Clear V", inline=True)
comment(0xB278, "Status = 2?", inline=True)
comment(0xB27A, "No: check for busy", inline=True)
comment(0xB27C, "Print 'jammed'", inline=True)
comment(0xB285, "Clear V", inline=True)
comment(0xB288, "Status = 1?", inline=True)
comment(0xB28A, "Not 1 or 2: default to jammed", inline=True)
comment(0xB28C, "Print 'busy'", inline=True)

# Display client station for busy printer
comment(0xB293, "Advance past status byte", inline=True)
comment(0xB295, "Read client station number", inline=True)
comment(0xB297, "Store station low", inline=True)
comment(0xB299, "Zero: no client info, skip", inline=True)
comment(0xB29B, "Print ' with station '", inline=True)
comment(0xB2AC, "Advance past station low", inline=True)
comment(0xB2AE, "Read client network number", inline=True)
comment(0xB2B0, "Store network number", inline=True)
comment(0xB2B2, "Set V flag", inline=True)
comment(0xB2B5, "Print client station address", inline=True)

# Advance to next slot
comment(0xB2BB, "Retrieve slot offset", inline=True)
comment(0xB2BC, "Transfer to Y", inline=True)
comment(0xB2BD, "Mark slot as processed (&3F)", inline=True)
comment(0xB2BF, "Write marker to workspace", inline=True)
comment(0xB2C3, "Return", inline=True)

# init_ps_slot_from_rx (&B2C4) — initialise PS slot from RX data
comment(0xB2C4, "Start at offset &78", inline=True)
comment(0xB2C6, "Load template byte", inline=True)
comment(0xB2C9, "At offset &7D?", inline=True)
comment(0xB2CB, "Yes: substitute RX page", inline=True)
comment(0xB2CD, "At offset &81?", inline=True)
comment(0xB2CF, "No: use template byte", inline=True)
comment(0xB2D1, "Use RX buffer page instead", inline=True)
comment(0xB2D3, "Store byte in slot buffer", inline=True)
comment(0xB2D5, "Next offset", inline=True)
comment(0xB2D6, "Past end of slot (&84)?", inline=True)
comment(0xB2D8, "No: continue copying", inline=True)
comment(0xB2DA, "Return", inline=True)

# store_char_uppercase (&B2DB) — store char to buffer, uppercased
comment(0xB2DB, "Y = current buffer position", inline=True)
comment(0xB2DD, "Strip high bit", inline=True)
comment(0xB2DF, "Is it lowercase 'a' or above?", inline=True)
comment(0xB2E1, "Below 'a': not lowercase", inline=True)
comment(0xB2E3, "Above 'z'?", inline=True)
comment(0xB2E5, "Yes: not lowercase", inline=True)
comment(0xB2E7, "Convert to uppercase", inline=True)
comment(0xB2E9, "Store in RX buffer", inline=True)
comment(0xB2EB, "Next buffer position", inline=True)
comment(0xB2EC, "Update buffer position", inline=True)
comment(0xB2EE, "Decrement character count", inline=True)
comment(0xB2EF, "Return (Z set if count=0)", inline=True)

# cmd_ex (&AD59) — *Ex: examine directory listing
# Entry: set up for Ex mode (1 entry per line, FS code 3)
comment(0xAD59, "Rotate carry into lib flag bit 7", inline=True)
comment(0xAD5C, "Clear carry (= current directory)", inline=True)
comment(0xAD5D, "Rotate carry back, clearing bit 7", inline=True)
comment(0xAD60, "A=&FF: initial column counter", inline=True)
comment(0xAD62, "Store column counter", inline=True)
comment(0xAD64, "One entry per line (Ex format)", inline=True)
comment(0xAD66, "Store entries per page", inline=True)
comment(0xAD68, "FS command code 3: Examine", inline=True)
comment(0xAD6A, "Store command code", inline=True)

# Cat entry (&AD6E) — *Cat: catalogue directory
comment(0xAD6E, "Set transfer parameters", inline=True)
comment(0xAD71, "Y=0: start from entry 0", inline=True)
comment(0xAD73, "Rotate carry into lib flag", inline=True)
comment(0xAD76, "Clear carry (= current directory)", inline=True)
comment(0xAD77, "Rotate carry back, clearing bit 7", inline=True)
comment(0xAD7A, "Three entries per column (Cat)", inline=True)
comment(0xAD7C, "Store column counter", inline=True)
comment(0xAD7E, "Store entries per page", inline=True)
comment(0xAD80, "FS command code &0B: Catalogue", inline=True)
comment(0xAD82, "Store command code", inline=True)

# Shared Ex/Cat setup
comment(0xAD84, "Save text pointer", inline=True)
comment(0xAD87, "A=&FF: enable escape checking", inline=True)
comment(0xAD89, "Set escapable flag", inline=True)
comment(0xAD8B, "Command code 6", inline=True)
comment(0xAD8D, "Store in TX buffer", inline=True)
comment(0xAD90, "Parse directory argument", inline=True)
comment(0xAD93, "X=1: offset in buffer", inline=True)
comment(0xAD95, "Copy argument to TX buffer", inline=True)
comment(0xAD98, "Get library/FS flags", inline=True)
comment(0xAD9B, "Shift bit 0 to carry", inline=True)
comment(0xAD9C, "Bit 0 clear: skip", inline=True)
comment(0xAD9E, "Set bit 6 (owner access flag)", inline=True)
comment(0xADA0, "Rotate back", inline=True)
comment(0xADA1, "Store modified flags", inline=True)
comment(0xADA4, "Y=&12: FS command for examine", inline=True)
comment(0xADA6, "Send request to file server", inline=True)
comment(0xADA9, "X=3: offset to directory title", inline=True)
comment(0xADAB, "Print directory title (10 chars)", inline=True)
comment(0xADAE, "Print '('", inline=True)

# Directory header: cycle number and access
comment(0xADB2, "Get cycle number", inline=True)
comment(0xADB5, "Print as 3-digit decimal", inline=True)
comment(0xADB8, "Print ')     '", inline=True)
comment(0xADC1, "Get owner/public flag", inline=True)
comment(0xADC4, "Non-zero: public access", inline=True)
comment(0xADC6, "Print 'Owner' + CR", inline=True)
comment(0xADCF, "Skip public; ALWAYS branch", inline=True)
comment(0xADD1, "Print 'Public' + CR", inline=True)

# Directory info: option, dir name, lib name
comment(0xADDB, "Get flags", inline=True)
comment(0xADDE, "Save flags", inline=True)
comment(0xADDF, "Mask owner access bits", inline=True)
comment(0xADE2, "Y=&15: FS command for dir info", inline=True)
comment(0xADE4, "Send request to file server", inline=True)
comment(0xADE7, "Advance X past header", inline=True)
comment(0xADE8, "Y=&10: print 16 chars", inline=True)
comment(0xADEA, "Print file entry", inline=True)
comment(0xADED, "Print '    Option '", inline=True)
comment(0xADFB, "Get option byte", inline=True)
comment(0xADFE, "Transfer to X for table lookup", inline=True)
comment(0xADFF, "Print option as hex", inline=True)
comment(0xAE02, "Print ' ('", inline=True)
comment(0xAE07, "Index into option string table", inline=True)
comment(0xAE0A, "Get option name character", inline=True)
comment(0xAE0D, "High bit set: end of string", inline=True)
comment(0xAE12, "Next character", inline=True)
comment(0xAE13, "Loop; ALWAYS branch", inline=True)
comment(0xAE15, "Print ')' + CR + 'Dir. '", inline=True)
comment(0xAE1F, "Offset &11: directory name", inline=True)
comment(0xAE21, "Print directory name (10 chars)", inline=True)
comment(0xAE24, "Print '     Lib. '", inline=True)
comment(0xAE31, "Offset &1B: library name", inline=True)
comment(0xAE33, "Print library name (10 chars)", inline=True)
comment(0xAE39, "Restore flags", inline=True)
comment(0xAE3A, "Store restored flags", inline=True)

# Entry listing loop
comment(0xAE3D, "Store entry count", inline=True)
comment(0xAE40, "Also store in work_4", inline=True)
comment(0xAE42, "Get command code", inline=True)
comment(0xAE44, "Store in buffer", inline=True)
comment(0xAE47, "Get entries per page", inline=True)
comment(0xAE49, "Store in buffer", inline=True)
comment(0xAE4C, "X=3: buffer offset", inline=True)
comment(0xAE4E, "Copy argument to buffer", inline=True)
comment(0xAE51, "Y=3: FS command for examine/cat", inline=True)
comment(0xAE53, "Send request to file server", inline=True)
comment(0xAE56, "Advance past header", inline=True)
comment(0xAE57, "Get number of entries returned", inline=True)
comment(0xAE5A, "Zero: no more entries", inline=True)
comment(0xAE5C, "Save entry count", inline=True)

# Scan for end-of-entry marker
comment(0xAE5D, "Advance Y", inline=True)
comment(0xAE5E, "Get entry data byte", inline=True)
comment(0xAE61, "Bit 7 clear: more data", inline=True)
comment(0xAE63, "Store terminator byte", inline=True)
comment(0xAE66, "Print entry with column separator", inline=True)
comment(0xAE69, "Restore entry count", inline=True)
comment(0xAE6A, "Clear carry for addition", inline=True)
comment(0xAE6B, "Add entries processed", inline=True)
comment(0xAE6D, "Transfer to Y", inline=True)
comment(0xAE6E, "More entries: loop", inline=True)

# print_10_chars (&AE70) — print 10 chars from buffer at X
comment(0xAE70, "Y=10: characters to print", inline=True)
comment(0xAE72, "Get character from buffer", inline=True)
comment(0xAE78, "Next buffer position", inline=True)
comment(0xAE79, "Decrement count", inline=True)
comment(0xAE7A, "Loop until 10 printed", inline=True)
comment(0xAE7C, "Return", inline=True)

# parse_cmd_arg_y0 (&AE80)
comment(0xAE80, "Y=0: start of command line", inline=True)

# parse_filename_arg (&AE82)
comment(0xAE82, "Read string to buffer via GSREAD", inline=True)

# parse_access_prefix (&AE85) — parse '&' or ':' FS prefix
comment(0xAE85, "Get first parsed character", inline=True)
comment(0xAE88, "Is it '&'?", inline=True)
comment(0xAE8A, "No: check for ':' prefix", inline=True)
comment(0xAE8C, "Get flags", inline=True)
comment(0xAE8F, "Set FS selection flag (bit 6)", inline=True)
comment(0xAE91, "Store updated flags", inline=True)
comment(0xAE94, "Remove '&' prefix character", inline=True)
comment(0xAE97, "Get next character", inline=True)
comment(0xAE9A, "Is it '.'?", inline=True)
comment(0xAE9C, "No: check for '#'", inline=True)
comment(0xAE9E, "Get char after '.'", inline=True)
comment(0xAEA1, "Is it CR (end of line)?", inline=True)
comment(0xAEA3, "Yes: '&.' + CR only = bad filename", inline=True)

# strip_token_prefix (&AEA5) — shift buffer left by 1 char
comment(0xAEA5, "Save X", inline=True)
comment(0xAEA6, "Push X", inline=True)
comment(0xAEA7, "X=&FF, will increment to 0", inline=True)
comment(0xAEA9, "Increment X", inline=True)
comment(0xAEAA, "Get character at offset+1", inline=True)
comment(0xAEAD, "Store at offset (shift left)", inline=True)
comment(0xAEB0, "Is it CR (end of line)?", inline=True)
comment(0xAEB2, "No: continue shifting", inline=True)
comment(0xAEB4, "Get shifted string length", inline=True)
comment(0xAEB5, "Zero length: skip trailing trim", inline=True)
comment(0xAEB7, "Get character at end of string", inline=True)
comment(0xAEBA, "Is it a space?", inline=True)
comment(0xAEBC, "No: done trimming", inline=True)
comment(0xAEBE, "Replace trailing space with CR", inline=True)
comment(0xAEC0, "Store CR", inline=True)
comment(0xAEC3, "Move back", inline=True)
comment(0xAEC4, "Loop while more trailing spaces", inline=True)
comment(0xAEC6, "Restore X", inline=True)
comment(0xAEC7, "Transfer back to X", inline=True)
comment(0xAEC8, "Return", inline=True)

# Error paths for parse_access_prefix
comment(0xAEC9, "Is it '#'?", inline=True)
comment(0xAECB, "Yes: '#' prefix accepted", inline=True)
comment(0xAECD, "Bad filename error", inline=True)

# Alternative ':' prefix path
comment(0xAED0, "Check for ':' prefix", inline=True)
comment(0xAED2, "Neither '&' nor ':': no prefix", inline=True)
comment(0xAED4, "Get character after ':'", inline=True)
comment(0xAED7, "Is it '.'?", inline=True)
comment(0xAED9, "Yes: ':.' qualified prefix", inline=True)
comment(0xAEDB, "Is it CR (end of line)?", inline=True)
comment(0xAEDD, "No: no FS prefix, return", inline=True)
comment(0xAEDF, "Get flags", inline=True)
comment(0xAEE2, "Set FS selection flag (bit 6)", inline=True)
comment(0xAEE4, "Store updated flags", inline=True)
comment(0xAEE9, "Data: option string offset table", inline=True)

# copy_arg_to_buf_x0 (&AEF0) — copy argument to buffer
comment(0xAEF0, "X=0: start of buffer", inline=True)
comment(0xAEF2, "Y=0: start of argument", inline=True)
comment(0xAEF4, "Set carry: enable '&' validation", inline=True)
comment(0xAEF5, "Get character from command line", inline=True)
comment(0xAEF7, "Store in TX buffer", inline=True)
comment(0xAEFA, "Carry clear: skip validation", inline=True)
comment(0xAEFC, "Is it '!' or above?", inline=True)
comment(0xAEFE, "Is it '&'?", inline=True)
comment(0xAF00, "No: continue copying", inline=True)
comment(0xAF02, "'&' in filename: bad filename", inline=True)
comment(0xAF05, "Restore A (undo '&' EOR)", inline=True)
comment(0xAF07, "Advance buffer position", inline=True)
comment(0xAF08, "Advance source position", inline=True)
comment(0xAF09, "Is it CR (end of line)?", inline=True)
comment(0xAF0B, "No: continue copying", inline=True)
comment(0xAF0D, "Return", inline=True)

# mask_owner_access (&AF12) — clear owner/FS bits from flags
comment(0xAF12, "Get flags", inline=True)
comment(0xAF15, "Mask to low 5 bits only", inline=True)
comment(0xAF17, "Store masked flags", inline=True)
comment(0xAF1A, "Return", inline=True)

# ex_print_col_sep (&AF27) — print column separator or newline
comment(0xAF1E, "X=0: start from first entry", inline=True)
comment(0xAF20, "Get entry byte from buffer", inline=True)
comment(0xAF23, "High bit set: end of entries", inline=True)
comment(0xAF25, "Non-zero: printable character", inline=True)
comment(0xAF27, "Get column counter", inline=True)
comment(0xAF29, "Negative: newline mode (Ex)", inline=True)
comment(0xAF2B, "Increment column counter", inline=True)
comment(0xAF2C, "Transfer to A", inline=True)
comment(0xAF2D, "Modulo 4 (Cat: 3 per row)", inline=True)
comment(0xAF2F, "Store updated counter", inline=True)
comment(0xAF31, "Zero: row full, print newline", inline=True)
comment(0xAF33, "Print '  ' column separator", inline=True)
comment(0xAF38, "Skip newline; ALWAYS branch", inline=True)
comment(0xAF3A, "CR character for newline", inline=True)
comment(0xAF3F, "Advance to next entry", inline=True)
comment(0xAF40, "Loop for more entries", inline=True)
comment(0xAF42, "Embedded string data 'Exec'", inline=True)
comment(0xAF44, "Embedded string data (contd)", inline=True)

# cmd_ps (&AFCE) — *PS: list printer server status
# Entry: check printer available
comment(0xAFCE, "A=1: check printer ready", inline=True)
comment(0xAFD0, "Test printer server workspace flag", inline=True)
comment(0xAFD3, "Non-zero: printer available", inline=True)
comment(0xAFD5, "Printer not available: error", inline=True)

# Initialise and parse argument
comment(0xAFD8, "Initialise spool drive", inline=True)
comment(0xAFDB, "Save pointer to spool buffer", inline=True)
comment(0xAFDE, "Get first argument character", inline=True)
comment(0xAFE0, "End of command line?", inline=True)
comment(0xAFE2, "Yes: no argument given", inline=True)
comment(0xAFE4, "Clear V (= explicit PS name given)", inline=True)
comment(0xAFE5, "Is first char a decimal digit?", inline=True)
comment(0xAFE8, "Yes: station number, skip PS name", inline=True)
comment(0xAFEA, "PS name follows", inline=True)
comment(0xAFEB, "Save Y", inline=True)
comment(0xAFEC, "Load PS server address", inline=True)
comment(0xAFEF, "Restore Y", inline=True)
comment(0xAFF0, "Back to Y register", inline=True)
comment(0xAFF1, "Parse FS/PS arguments", inline=True)
comment(0xAFF4, "Jump to store station address", inline=True)

# copy_ps_data (&AFF7) — copy PS data from template
comment(0xAFF7, "Start at offset &1C", inline=True)
comment(0xAFF9, "X=&F8: offset into template", inline=True)
comment(0xAFFB, "Get template byte", inline=True)
comment(0xAFFE, "Store in RX buffer", inline=True)
comment(0xB000, "Next destination offset", inline=True)
comment(0xB001, "Next source offset", inline=True)
comment(0xB002, "Loop until X wraps to 0", inline=True)
comment(0xB004, "Return", inline=True)

# No argument: set V and skip PS name
comment(0xB005, "Set V (= no explicit PS name)", inline=True)

# Station number path: fill PS name buffer
comment(0xB008, "Save command line pointer", inline=True)
comment(0xB00A, "V set: skip PS name parsing", inline=True)
comment(0xB00C, "Max 6 characters for PS name", inline=True)
comment(0xB00E, "Buffer offset &1C for PS name", inline=True)
comment(0xB010, "Space character", inline=True)
comment(0xB012, "Fill buffer with space", inline=True)
comment(0xB014, "Next position", inline=True)
comment(0xB015, "Count down", inline=True)
comment(0xB016, "Loop until 6 spaces filled", inline=True)
comment(0xB018, "Save text pointer", inline=True)
comment(0xB01B, "Restore command line pointer", inline=True)
comment(0xB01D, "Initialise string reading", inline=True)
comment(0xB020, "Empty string: skip to send", inline=True)
comment(0xB022, "Max 6 characters", inline=True)
comment(0xB024, "Save updated string pointer", inline=True)
comment(0xB026, "Buffer offset for PS name", inline=True)
comment(0xB028, "Save buffer position", inline=True)

# Copy PS name from command line
comment(0xB02A, "Restore string pointer", inline=True)
comment(0xB02C, "Read next character", inline=True)
comment(0xB02F, "Save updated pointer", inline=True)
comment(0xB031, "End of string: go to send", inline=True)
comment(0xB033, "Store char uppercased in buffer", inline=True)
comment(0xB036, "Loop for more characters", inline=True)

# Send PS status request
comment(0xB038, "Copy reversed PS name to TX", inline=True)
comment(0xB03B, "Send PS status request", inline=True)
comment(0xB03E, "Pop and requeue PS scan", inline=True)
comment(0xB041, "Load PS server address", inline=True)
comment(0xB044, "A=0", inline=True)
comment(0xB047, "Offset &24 in buffer", inline=True)
comment(0xB049, "Clear PS status byte", inline=True)

# Scan PS slots for ready printer
comment(0xB04B, "Get slot offset from stack", inline=True)
comment(0xB04C, "Zero: all slots done", inline=True)
comment(0xB04E, "Save slot offset", inline=True)
comment(0xB04F, "Transfer to Y", inline=True)
comment(0xB050, "Read slot status", inline=True)
comment(0xB052, "Bit 7 clear: slot inactive", inline=True)
comment(0xB054, "Advance Y by 4 (to status page)", inline=True)
comment(0xB057, "Read status page pointer", inline=True)
comment(0xB059, "Store pointer low", inline=True)
comment(0xB05B, "Read printer status byte", inline=True)
comment(0xB05D, "Non-zero (busy): skip", inline=True)
comment(0xB05F, "Back to network number", inline=True)
comment(0xB060, "Read network number", inline=True)
comment(0xB062, "Store network number", inline=True)
comment(0xB064, "Back to station number", inline=True)
comment(0xB065, "Read station number", inline=True)
comment(0xB067, "Store station low", inline=True)
comment(0xB069, "Offset &24 in buffer", inline=True)
comment(0xB06B, "Store ready station in buffer", inline=True)

# Mark slot and advance
comment(0xB06D, "Retrieve slot offset", inline=True)
comment(0xB06E, "Transfer to Y", inline=True)
comment(0xB06F, "Mark slot as processed (&3F)", inline=True)
comment(0xB071, "Write marker to workspace", inline=True)

# Display PS status
comment(0xB075, "Print 'Printer server is '", inline=True)
comment(0xB078, "Offset &24: PS station number", inline=True)
comment(0xB07A, "Get stored station number", inline=True)
comment(0xB07C, "Non-zero: server changed", inline=True)
comment(0xB07E, "Print 'still '", inline=True)
comment(0xB087, "Clear V", inline=True)
comment(0xB08A, "Print 'now '", inline=True)
comment(0xB091, "Padding", inline=True)
comment(0xB092, "Print FS info and newline", inline=True)

# Store new PS address in workspace
comment(0xB095, "Workspace offset 2", inline=True)
comment(0xB097, "Get station low", inline=True)
comment(0xB099, "Store in workspace", inline=True)
comment(0xB09C, "Get network number", inline=True)
comment(0xB09E, "Store in workspace", inline=True)
comment(0xB0A0, "Return", inline=True)

# print_file_server_is (&B0A1)
comment(0xB0A1, "Print 'File'", inline=True)
comment(0xB0A8, "Clear V", inline=True)

# print_printer_server_is (&B0AB)
comment(0xB0AB, "Print 'Printer'", inline=True)
comment(0xB0B5, "Padding", inline=True)
comment(0xB0B6, "Print ' server is '", inline=True)
comment(0xB0C4, "Padding", inline=True)
comment(0xB0C5, "Return", inline=True)

# load_ps_server_addr (&B0C6) — load PS address from workspace
comment(0xB0C6, "Workspace offset 2", inline=True)
comment(0xB0C8, "Read station low", inline=True)
comment(0xB0CA, "Store station low", inline=True)
comment(0xB0CD, "Read network number", inline=True)
comment(0xB0CF, "Store network number", inline=True)
comment(0xB0D1, "Return", inline=True)

# pop_requeue_ps_scan (&B0D2) — requeue print server scan
comment(0xB0D2, "Pop return address low", inline=True)
comment(0xB0D3, "Save return address low", inline=True)
comment(0xB0D5, "Pop return address high", inline=True)
comment(0xB0D6, "Save return address high", inline=True)
comment(0xB0D8, "Push 0 as end-of-list marker", inline=True)
comment(0xB0DA, "Push it", inline=True)
comment(0xB0DB, "Start scanning from offset &84", inline=True)
comment(0xB0DD, "Store scan position", inline=True)
comment(0xB0DF, "Shift PS slot flags right", inline=True)
comment(0xB0E2, "Counter: 3 PS slots", inline=True)

# Slot scanning loop
comment(0xB0E4, "Convert to 2-bit workspace index", inline=True)
comment(0xB0E7, "Carry set: no more slots", inline=True)
comment(0xB0E9, "Shift right twice", inline=True)
comment(0xB0EA, "To get slot offset", inline=True)
comment(0xB0EB, "Transfer to X", inline=True)
comment(0xB0EC, "Read slot status byte", inline=True)
comment(0xB0EE, "Zero: empty slot, done", inline=True)
comment(0xB0F0, "Is it processed marker (&3F)?", inline=True)
comment(0xB0F2, "Yes: re-initialise this slot", inline=True)
comment(0xB0F4, "Try next slot", inline=True)
comment(0xB0F5, "Transfer slot index to A", inline=True)
comment(0xB0F6, "Loop for more slots", inline=True)

# Re-initialise PS slot
comment(0xB0F8, "Y = workspace offset of slot", inline=True)
comment(0xB0F9, "Push slot offset for scan list", inline=True)
comment(0xB0FA, "Set active status (&7F)", inline=True)
comment(0xB0FC, "Write status byte", inline=True)
comment(0xB0FE, "Next byte", inline=True)
comment(0xB0FF, "Low byte: workspace page", inline=True)
comment(0xB101, "Write workspace pointer low", inline=True)
comment(0xB103, "A=0", inline=True)
comment(0xB105, "Write two zero bytes + advance Y", inline=True)
comment(0xB108, "Get current scan page", inline=True)
comment(0xB10A, "Write RX buffer page low", inline=True)
comment(0xB10C, "Clear carry for addition", inline=True)
comment(0xB10D, "Save processor status", inline=True)
comment(0xB10E, "Advance by 3 pages", inline=True)
comment(0xB110, "Restore processor status", inline=True)
comment(0xB111, "Update scan position", inline=True)
comment(0xB113, "Write buffer page + &FF bytes", inline=True)
comment(0xB116, "Get updated scan position", inline=True)
comment(0xB118, "Write RX buffer page high", inline=True)
comment(0xB11A, "Write another page + &FF bytes", inline=True)
comment(0xB11D, "Continue scanning slots", inline=True)

# Done scanning: restore return addr and delay
comment(0xB120, "Shift PS slot flags back", inline=True)
comment(0xB123, "Restore return address high", inline=True)
comment(0xB125, "Push onto stack", inline=True)
comment(0xB126, "Restore return address low", inline=True)
comment(0xB128, "Push onto stack", inline=True)
comment(0xB129, "Delay counter: 10", inline=True)
comment(0xB12D, "Outer loop counter = 10", inline=True)
comment(0xB12F, "Decrement Y (inner loop)", inline=True)
comment(0xB130, "Inner loop: 10 iterations", inline=True)
comment(0xB132, "Decrement X (middle loop)", inline=True)
comment(0xB133, "Middle loop: 10 iterations", inline=True)
comment(0xB135, "Decrement outer counter", inline=True)
comment(0xB137, "Outer loop: ~1000 delay cycles", inline=True)
comment(0xB139, "Return", inline=True)

# write_ps_slot_byte_ff (&B13A) — write page + two &FF bytes
comment(0xB13A, "Advance Y", inline=True)
comment(0xB13B, "Get buffer page", inline=True)
comment(0xB13D, "Store in workspace", inline=True)
comment(0xB13F, "A=&FF", inline=True)
comment(0xB141, "Advance Y", inline=True)
comment(0xB142, "Write byte to workspace", inline=True)
comment(0xB144, "Advance Y", inline=True)
comment(0xB145, "Write byte to workspace", inline=True)
comment(0xB147, "Advance Y", inline=True)
comment(0xB148, "Return", inline=True)

# reverse_ps_name_to_tx (&B149) — reverse PS name for TX buffer
comment(0xB149, "Start of PS name at offset &1C", inline=True)
comment(0xB14B, "Load byte from RX buffer", inline=True)
comment(0xB14D, "Push to stack (for reversal)", inline=True)
comment(0xB14E, "Next source byte", inline=True)
comment(0xB14F, "End of PS name field (&24)?", inline=True)
comment(0xB151, "No: continue pushing", inline=True)
comment(0xB153, "End of TX name field at &1B", inline=True)
comment(0xB155, "Pop byte (reversed order)", inline=True)
comment(0xB156, "Store in RX buffer", inline=True)
comment(0xB158, "Previous position", inline=True)
comment(0xB159, "Start of TX field (&13)?", inline=True)
comment(0xB15B, "No: continue popping", inline=True)
comment(0xB15D, "Copy RX page to TX", inline=True)
comment(0xB15F, "Set TX pointer high", inline=True)
comment(0xB161, "TX offset &10", inline=True)
comment(0xB163, "Set TX pointer low", inline=True)
comment(0xB165, "Copy 4 header bytes", inline=True)
comment(0xB167, "Get header template byte", inline=True)
comment(0xB16A, "Store in TX buffer", inline=True)
comment(0xB16C, "Previous byte", inline=True)
comment(0xB16D, "Loop until all 4 copied", inline=True)
comment(0xB16F, "Return", inline=True)

# print_station_addr (&B174) — print net.station address
comment(0xB174, "Save V flag (controls padding)", inline=True)
comment(0xB175, "Get network number", inline=True)
comment(0xB177, "Zero: no network prefix", inline=True)
comment(0xB179, "Print network as 3 digits", inline=True)
comment(0xB17C, "'.' separator", inline=True)
comment(0xB181, "Set V (suppress station padding)", inline=True)
comment(0xB184, "V set: skip padding spaces", inline=True)
comment(0xB186, "Print 4 spaces (padding)", inline=True)
comment(0xB18D, "Get station number", inline=True)
comment(0xB18F, "Restore flags", inline=True)
comment(0xB190, "Print station as 3 digits", inline=True)

# cmd_bye (&948A) — *Bye: logoff from file server
comment(0x948A, "Y=0: close all files", inline=True)
comment(0x948C, "Process all file control blocks", inline=True)
comment(0x948F, "OSBYTE &77: close spool/exec", inline=True)
comment(0x9494, "Close all network channels", inline=True)
comment(0x9497, "Y=&17: *Bye function code", inline=True)

# save_net_tx_cb (&9499) — save state and build TX control block
comment(0x9499, "Clear V (standard mode)", inline=True)
comment(0x949A, "Copy FS station to TX control block", inline=True)
comment(0x949D, "Store in TXCB", inline=True)
comment(0x94A0, "Clear carry", inline=True)
comment(0x94A1, "Save flags (carry = mode)", inline=True)
comment(0x94A2, "Store function code in TXCB", inline=True)
comment(0x94A5, "Copy 2 bytes (indices 0-1)", inline=True)
comment(0x94A7, "Load source byte", inline=True)
comment(0x94AA, "Store to TXCB", inline=True)
comment(0x94AD, "Next byte", inline=True)
comment(0x94AE, "Loop until all copied", inline=True)
comment(0x94B0, "Test library flag bits 6-7", inline=True)
comment(0x94B3, "Bit 6 set: use station as port", inline=True)
comment(0x94B5, "Bit 7 clear: skip port override", inline=True)
comment(0x94B7, "Bit 7 set: load alternative port", inline=True)
comment(0x94BA, "Override TXCB port byte", inline=True)
comment(0x94BF, "Bit 6: load station byte", inline=True)
comment(0x94C2, "Use station as TXCB port", inline=True)
comment(0x94C5, "Restore flags (carry = mode)", inline=True)

# prep_send_tx_cb (&94C6) — prepare TXCB and send
comment(0x94C6, "Save flags", inline=True)
comment(0x94C7, "Port &90: FS command port", inline=True)
comment(0x94C9, "Set reply port in TXCB", inline=True)
comment(0x94CC, "Initialise TXCB workspace", inline=True)
comment(0x94CF, "Get TXCB data end offset", inline=True)
comment(0x94D0, "Add 5 for header size", inline=True)
comment(0x94D2, "Set TXCB end pointer", inline=True)
comment(0x94D4, "Restore flags", inline=True)
comment(0x94D5, "C set: send disconnect instead", inline=True)
comment(0x94D7, "Save flags", inline=True)
comment(0x94D8, "Initialise TX pointer and send", inline=True)
comment(0x94DB, "Restore flags", inline=True)

# recv_and_process_reply (&94DC) — wait for reply and dispatch
comment(0x94DC, "Save flags", inline=True)
comment(0x94DD, "Set up receive TXCB", inline=True)
comment(0x94E0, "Wait for TX acknowledgment", inline=True)
comment(0x94E3, "Restore flags", inline=True)
comment(0x94E4, "Advance to next reply byte", inline=True)
comment(0x94E5, "Load reply byte", inline=True)
comment(0x94E7, "Save in X", inline=True)
comment(0x94E8, "Zero: no more replies, return", inline=True)
comment(0x94EA, "V clear: use code directly", inline=True)
comment(0x94EC, "V set: adjust reply code (+&2B)", inline=True)
comment(0x94EE, "Non-zero: process reply", inline=True)
comment(0x94F0, "Return", inline=True)

# Disconnect path — send disconnect if carry was set
comment(0x94F1, "Discard saved flags", inline=True)
comment(0x94F2, "X=&C0: disconnect command", inline=True)
comment(0x94F4, "Advance reply offset", inline=True)
comment(0x94F5, "Send disconnect reply", inline=True)
comment(0x94F8, "Successful: process next reply", inline=True)

# Process reply status — handle reply code and data loss
comment(0x94FA, "Store reply status code", inline=True)
comment(0x94FD, "Load pending operation marker", inline=True)
comment(0x9500, "Pending: go to data loss check", inline=True)
comment(0x9502, "Reply &BF (normal bye response)?", inline=True)
comment(0x9504, "No: build error from reply", inline=True)
comment(0x9506, "A=&40: initial data-loss flag", inline=True)
comment(0x9508, "Push data-loss accumulator", inline=True)
comment(0x9509, "Scan 16 channel entries (15 to 0)", inline=True)
comment(0x950B, "Pop accumulator", inline=True)
comment(0x950C, "OR in channel status bits", inline=True)
comment(0x950F, "Push updated accumulator", inline=True)
comment(0x9510, "Load channel status", inline=True)
comment(0x9513, "Keep only bits 6-7 (close flags)", inline=True)
comment(0x9515, "Clear data bits, keep state flags", inline=True)
comment(0x9518, "Next channel", inline=True)
comment(0x9519, "Loop all 16 channels", inline=True)
comment(0x951B, "Close all network channels", inline=True)
comment(0x951E, "Pop data-loss accumulator", inline=True)
comment(0x951F, "Bit 0 to carry (data lost?)", inline=True)
comment(0x9520, "No data lost: skip message", inline=True)
comment(0x9522, "Print 'Data Lost' + CR", inline=True)
comment(0x952F, "Reload reply status code", inline=True)
comment(0x9532, "Check pending operation", inline=True)
comment(0x9535, "No pending: build error from reply", inline=True)
comment(0x9537, "Pending: clean up stack (3 bytes)", inline=True)
comment(0x9538, "(second byte)", inline=True)
comment(0x9539, "(third byte)", inline=True)
comment(0x953A, "Return to pending operation caller", inline=True)

# Build server error — copy error from server reply
comment(0x953B, "Y=1: error code offset in reply", inline=True)
comment(0x953D, "Reply code >= &A8?", inline=True)
comment(0x953F, "Yes: keep server error code", inline=True)
comment(0x9541, "No: use minimum error code &A8", inline=True)
comment(0x9543, "Overwrite error code in reply", inline=True)
comment(0x9545, "Y=&FF: pre-increment index", inline=True)
comment(0x9547, "Advance to next byte", inline=True)
comment(0x9548, "Load reply byte", inline=True)
comment(0x954A, "Copy to error block", inline=True)
comment(0x954D, "Is it CR (end of message)?", inline=True)
comment(0x954F, "No: copy next byte", inline=True)
comment(0x9551, "Store null terminator (A=0 from EOR)", inline=True)
comment(0x9554, "Get message length", inline=True)
comment(0x9555, "Transfer to A", inline=True)
comment(0x9556, "Length in X", inline=True)
comment(0x9557, "Go to error dispatch", inline=True)

# check_escape (&955A) — test for escape condition
comment(0x955A, "Load MOS escape flag", inline=True)
comment(0x955C, "Mask with escape-enabled flag", inline=True)
comment(0x955E, "No escape: return", inline=True)

# raise_escape_error (&9560) — acknowledge and raise escape error
comment(0x9560, "OSBYTE &7E: acknowledge escape", inline=True)
comment(0x9565, "Error class 6: Escape", inline=True)
comment(0x9567, "Classify as network error", inline=True)

# Remote station handler (&956A) — handle Econet remote control
comment(0x956A, "Offset 4: remote state byte", inline=True)
comment(0x956C, "Load remote state", inline=True)
comment(0x956E, "Zero: initialise remote session", inline=True)
comment(0x9570, "Non-zero: commit state and return", inline=True)
comment(0x9573, "Set bits 0,3: remote active flags", inline=True)
comment(0x9575, "Store updated remote state", inline=True)
comment(0x9577, "X=&80: flag for vector setup", inline=True)
comment(0x9579, "Offset &80 in RX buffer", inline=True)
comment(0x957B, "Load remote station low", inline=True)
comment(0x957D, "Save on stack", inline=True)
comment(0x957F, "Load remote station high", inline=True)
comment(0x9581, "Workspace offset &0F", inline=True)
comment(0x9583, "Store remote station high", inline=True)
comment(0x9585, "Y=&0E", inline=True)
comment(0x9586, "Restore remote station low", inline=True)
comment(0x9587, "Store remote station low", inline=True)
comment(0x9589, "Set up remote keyboard scanning", inline=True)
comment(0x958C, "Initialise workspace copy", inline=True)
comment(0x958F, "X=1: disable keyboard", inline=True)
comment(0x9591, "Y=0", inline=True)
comment(0x9593, "OSBYTE &C9: Econet keyboard disable", inline=True)
comment(0x9598, "Commit state change", inline=True)
comment(0x959B, "Error code 0", inline=True)
comment(0x959D, "Generate 'Remoted' error", inline=True)

# Remote key injection (&95A8)
comment(0x95A8, "Offset 4: remote state byte", inline=True)
comment(0x95AA, "Load remote state", inline=True)
comment(0x95AC, "Zero: reinitialise session", inline=True)
comment(0x95AE, "Offset &80: station low", inline=True)
comment(0x95B0, "Load station low from RX", inline=True)
comment(0x95B2, "Workspace offset &0E", inline=True)
comment(0x95B4, "Compare with stored station", inline=True)
comment(0x95B6, "Different station: commit state", inline=True)
comment(0x95B8, "Offset &82: keypress byte", inline=True)
comment(0x95BA, "Load remote keypress", inline=True)
comment(0x95BC, "Key code to Y", inline=True)
comment(0x95BD, "X=0: keyboard buffer", inline=True)
comment(0x95BF, "Commit state change", inline=True)
comment(0x95C2, "OSBYTE &99: insert into buffer", inline=True)

# wait_net_tx_ack (&95C7) — poll TX status with 3-level timeout
comment(0x95C7, "Save TX timeout counter", inline=True)
comment(0x95CA, "Push (used as outer loop counter)", inline=True)
comment(0x95CB, "Save TX control state", inline=True)
comment(0x95CE, "Push (preserved during wait)", inline=True)
comment(0x95CF, "Check if TX in progress", inline=True)
comment(0x95D1, "Non-zero: skip force-wait", inline=True)
comment(0x95D3, "Set bit 7 to force wait mode", inline=True)
comment(0x95D5, "Store updated control state", inline=True)
comment(0x95D8, "A=0: initial counter values", inline=True)
comment(0x95DA, "Push inner loop counter", inline=True)
comment(0x95DB, "Push middle loop counter", inline=True)
comment(0x95DD, "X=SP for stack-relative DECs", inline=True)
comment(0x95DE, "Poll TX completion status", inline=True)
comment(0x95E0, "Bit 7 set: TX complete", inline=True)
comment(0x95E2, "Decrement inner counter", inline=True)
comment(0x95E5, "Not zero: keep polling", inline=True)
comment(0x95E7, "Decrement middle counter", inline=True)
comment(0x95EA, "Not zero: keep polling", inline=True)
comment(0x95EC, "Decrement outer counter", inline=True)
comment(0x95EF, "Not zero: keep polling", inline=True)
comment(0x95F1, "Discard inner counter", inline=True)
comment(0x95F2, "Discard middle counter", inline=True)
comment(0x95F3, "Restore l0d61 control state", inline=True)
comment(0x95F4, "Write back TX control state", inline=True)
comment(0x95F7, "Pop outer counter (0 if timed out)", inline=True)
comment(0x95F8, "Zero: TX timed out", inline=True)
comment(0x95FA, "Return (TX acknowledged)", inline=True)

# cond_save_error_code (&95FB) — conditionally store error code
comment(0x95FB, "Test error logging flag", inline=True)
comment(0x95FE, "Bit 7 clear: skip save", inline=True)
comment(0x9600, "Save error code to workspace", inline=True)
comment(0x9603, "Return", inline=True)

# TX timeout error builder (&9604) — build 'No reply' error
comment(0x9604, "X=8: 'No reply' error index", inline=True)
comment(0x9606, "Look up message table offset", inline=True)
comment(0x9609, "X=0: error text start", inline=True)
comment(0x960B, "Clear BRK byte in error block", inline=True)
comment(0x960E, "Load error number from table", inline=True)
comment(0x9611, "Conditionally save error code", inline=True)
comment(0x9614, "Load message byte", inline=True)
comment(0x9617, "Store in error text buffer", inline=True)
comment(0x961A, "Null terminator?", inline=True)
comment(0x961C, "Advance destination", inline=True)
comment(0x961D, "Advance source", inline=True)
comment(0x961E, "Loop until end of message", inline=True)
comment(0x9620, "Append ' net.station' to message", inline=True)
comment(0x9623, "A=0: null terminator", inline=True)
comment(0x9625, "Terminate error text", inline=True)
comment(0x9628, "Check and raise network error", inline=True)

# fixup_reply_status_a (&962B) — remap status 'A' to 'B'
comment(0x962B, "Load first reply byte", inline=True)
comment(0x962D, "Is it 'A' (status &41)?", inline=True)
comment(0x962F, "No: keep original", inline=True)
comment(0x9631, "Yes: change to 'B' (&42)", inline=True)
comment(0x9633, "Clear V flag", inline=True)

# load_reply_and_classify (&9636) — load reply and classify error
comment(0x9636, "Load first reply byte", inline=True)
# classify_reply_error (&9638) — main error classification
comment(0x9638, "Set V flag (via BIT &FF)", inline=True)
comment(0x963B, "Mask to error class (0-7)", inline=True)
comment(0x963D, "Save error class on stack", inline=True)
comment(0x963E, "Class 2 (station error)?", inline=True)
comment(0x9640, "No: build simple error message", inline=True)
comment(0x9642, "Save flags (V state for suffix)", inline=True)
comment(0x9643, "Error class to X", inline=True)
comment(0x9644, "Look up message table offset", inline=True)
comment(0x9647, "Load error number from table", inline=True)
comment(0x964A, "Conditionally save error code", inline=True)
comment(0x964D, "X=0: error text start", inline=True)
comment(0x964F, "Clear BRK byte", inline=True)
comment(0x9652, "Load message byte", inline=True)
comment(0x9655, "Store in error text", inline=True)
comment(0x9658, "Null terminator?", inline=True)
comment(0x965A, "Advance source", inline=True)
comment(0x965B, "Advance destination", inline=True)
comment(0x965C, "Loop until end of message", inline=True)
comment(0x965E, "Append ' net.station' suffix", inline=True)
comment(0x9661, "Restore flags", inline=True)
comment(0x9662, "V set: append 'not listening'", inline=True)
comment(0x9664, "Error code &A4", inline=True)
comment(0x9666, "Conditionally save error code", inline=True)
comment(0x9669, "Replace error number in block", inline=True)
comment(0x966C, "Y=&0B: 'not present' suffix index", inline=True)
comment(0x9670, "Y=9: 'not listening' suffix index", inline=True)
comment(0x9672, "Look up suffix table offset", inline=True)
comment(0x9675, "Offset to Y for indexing", inline=True)
comment(0x9676, "Load suffix byte", inline=True)
comment(0x9679, "Append to error text", inline=True)
comment(0x967C, "Null terminator?", inline=True)
comment(0x967E, "Advance source", inline=True)
comment(0x967F, "Advance destination", inline=True)
comment(0x9680, "Loop until end of suffix", inline=True)
comment(0x9682, "ALWAYS branch to error dispatch", inline=True)

# Simple error path — build error from class lookup
comment(0x9684, "Error class to X", inline=True)
comment(0x9685, "Look up message table offset", inline=True)
comment(0x9688, "X=0: error text start", inline=True)
comment(0x968A, "Clear BRK byte", inline=True)
comment(0x968D, "Load error number from table", inline=True)
comment(0x9690, "Conditionally save error code", inline=True)
comment(0x9693, "Load message byte", inline=True)
comment(0x9696, "Store in error text", inline=True)
comment(0x9699, "Null terminator? Go to error", inline=True)
comment(0x969B, "Advance source", inline=True)
comment(0x969C, "Advance destination", inline=True)
comment(0x969D, "Loop until end of message", inline=True)

# cmd_fs (&A063) — *FS: select file server by number
comment(0xA063, "Load current FS station high", inline=True)
comment(0xA066, "Save to fs_work_5", inline=True)
comment(0xA068, "Load current FS station low", inline=True)
comment(0xA06B, "Save to l00b6", inline=True)
comment(0xA06D, "Get first character of argument", inline=True)
comment(0xA06F, "Is it CR (no argument)?", inline=True)
comment(0xA071, "No arg: print current FS info", inline=True)
comment(0xA073, "Parse FS/PS station arguments", inline=True)
comment(0xA076, "A=1: write NFS info", inline=True)
comment(0xA078, "Store OSWORD sub-function", inline=True)
comment(0xA07A, "OSWORD &13: NFS information", inline=True)
comment(0xA07C, "Parameter block low", inline=True)
comment(0xA07E, "Parameter block high", inline=True)

# Print current FS info
comment(0xA083, "Print 'File server '", inline=True)
comment(0xA086, "Set V (suppress padding)", inline=True)
comment(0xA089, "Print station address", inline=True)

# parse_fs_ps_args (&A08F) — parse net.station arguments for FS/PS
comment(0xA08F, "Save X on stack", inline=True)
comment(0xA090, "Push X", inline=True)
comment(0xA091, "A=0: initialise dot-seen flag", inline=True)
comment(0xA093, "Clear dot-seen flag", inline=True)
comment(0xA095, "Parse first number (network)", inline=True)
comment(0xA098, "C set: number found, check for dot", inline=True)
comment(0xA09A, "Save Y (command line offset)", inline=True)
comment(0xA09B, "Push Y", inline=True)
comment(0xA09C, "Initialise bridge polling", inline=True)
comment(0xA09F, "Compare bridge result with parsed value", inline=True)
comment(0xA0A1, "Same: keep bridge result", inline=True)
comment(0xA0A3, "Different: use parsed value", inline=True)
comment(0xA0A5, "Store station low byte", inline=True)
comment(0xA0A7, "Restore Y", inline=True)
comment(0xA0A8, "Transfer back to Y", inline=True)
comment(0xA0A9, "Skip dot separator", inline=True)
comment(0xA0AA, "Parse second number (station)", inline=True)
comment(0xA0AD, "Zero result: skip store", inline=True)
comment(0xA0AF, "Store station high byte", inline=True)
comment(0xA0B1, "Restore X", inline=True)
comment(0xA0B2, "Transfer back to X", inline=True)
comment(0xA0B3, "Return", inline=True)

# get_pb_ptr_as_index (&A0B4) — convert PB pointer to 2-bit index
comment(0xA0B4, "Load parameter block pointer", inline=True)
# byte_to_2bit_index (&A0B6) — map byte to 2-bit index in Y
comment(0xA0B6, "Shift left (A * 2)", inline=True)
comment(0xA0B7, "Shift left (A * 4)", inline=True)
comment(0xA0B8, "Save A * 4 on stack", inline=True)
comment(0xA0B9, "Shift left (A * 8)", inline=True)
comment(0xA0BA, "Get stack pointer", inline=True)
comment(0xA0BB, "Save flags (carry from shift)", inline=True)
comment(0xA0BC, "A*8 + A*4 (from stack) = A*12", inline=True)
comment(0xA0BF, "Divide by 2 with carry", inline=True)
comment(0xA0C0, "Restore original flags", inline=True)
comment(0xA0C1, "Shift left again", inline=True)
comment(0xA0C2, "Result to Y as index", inline=True)
comment(0xA0C3, "Pop saved A * 4", inline=True)
comment(0xA0C4, "A * 4 >= &48 (out of range)?", inline=True)
comment(0xA0C6, "In range: return", inline=True)
comment(0xA0C8, "Out of range: Y=0", inline=True)
comment(0xA0CA, "A=&00", inline=True)
comment(0xA0CB, "Return with A=index, Y=index", inline=True)

# OSWORD read handler (&A0CC)
comment(0xA0CC, "Y=&6F: source offset", inline=True)
comment(0xA0CE, "Load byte from RX buffer", inline=True)
comment(0xA0D0, "C clear: store directly", inline=True)
comment(0xA0D2, "Get index from PB pointer", inline=True)
comment(0xA0D5, "C set (out of range): clear value", inline=True)
comment(0xA0D7, "Load workspace byte at index", inline=True)
comment(0xA0D9, "Is it '?' (uninitialised)?", inline=True)
comment(0xA0DB, "No: use value from RX buffer", inline=True)
comment(0xA0DD, "A=0: return zero for uninitialised", inline=True)
comment(0xA0DF, "Store result to PB pointer", inline=True)
comment(0xA0E1, "Return", inline=True)

# OSWORD write handler (&A0E2)
comment(0xA0E2, "Get index from PB pointer", inline=True)
comment(0xA0E5, "C clear: store to workspace", inline=True)
comment(0xA0E7, "Save carry to l0d6c bit 7", inline=True)
comment(0xA0EA, "Load PB pointer value", inline=True)
comment(0xA0EC, "Shift carry back in", inline=True)
comment(0xA0ED, "Restore l0d6c bit 7", inline=True)
comment(0xA0F0, "Return", inline=True)
comment(0xA0F1, "Save carry to l0d61 bit 7", inline=True)
comment(0xA0F4, "A='?': mark as uninitialised", inline=True)
comment(0xA0F6, "Store '?' to workspace", inline=True)
comment(0xA0F8, "Restore l0d61 bit 7", inline=True)
comment(0xA0FB, "Return", inline=True)

# cmd_fs_entry (&A0FC) — FS command dispatch entry
comment(0xA0FC, "Set text and transfer pointers", inline=True)
comment(0xA0FF, "Y=&FF: prepare for INY to 0", inline=True)
comment(0xA101, "Clear spool handle (no spool active)", inline=True)
comment(0xA103, "Set escapable flag (&FF)", inline=True)
comment(0xA106, "X=&4A: FS command table offset", inline=True)
comment(0xA108, "Match command in FS table", inline=True)
comment(0xA10B, "C set: command found", inline=True)

# cmd_fs_reentry (&A10D)
comment(0xA10D, "V clear: syntax error", inline=True)
# error_syntax (&A10F)
comment(0xA10F, "Error code &DC", inline=True)
comment(0xA111, "Generate 'Syntax' error", inline=True)

# Dispatch matched command (&A11B)
comment(0xA11B, "A=0: clear service state", inline=True)
comment(0xA11D, "Store cleared service state", inline=True)
comment(0xA11F, "Load command handler address high", inline=True)
comment(0xA122, "Push high byte", inline=True)
comment(0xA123, "Load command handler address low", inline=True)
comment(0xA126, "Push low byte", inline=True)
comment(0xA127, "RTS dispatches to command handler", inline=True)

# match_fs_cmd (&A128) — match command name in table
comment(0xA128, "Save Y (command line offset)", inline=True)
comment(0xA129, "Push on stack", inline=True)
comment(0xA12A, "Restore saved Y", inline=True)
comment(0xA12B, "Push back (keep on stack)", inline=True)
comment(0xA12C, "Transfer to Y", inline=True)
comment(0xA12D, "Load table entry byte", inline=True)
comment(0xA130, "Bit 7 set: end of table names", inline=True)

# Command name comparison loop
comment(0xA132, "Load table byte", inline=True)
comment(0xA135, "Bit 7 set: end of this name", inline=True)
comment(0xA137, "Compare with command line char", inline=True)
comment(0xA139, "Case-insensitive compare", inline=True)
comment(0xA13B, "Mismatch: skip to next entry", inline=True)
comment(0xA13D, "Match: advance command line", inline=True)
comment(0xA13E, "Advance table pointer", inline=True)
comment(0xA13F, "Loop for next character", inline=True)

# Skip to next table entry on mismatch
comment(0xA141, "Advance past remaining table chars", inline=True)
comment(0xA142, "Load next table byte", inline=True)
comment(0xA145, "Bit 7 clear: more chars to skip", inline=True)
comment(0xA147, "Check command line terminator", inline=True)
comment(0xA149, "Is it '.' (abbreviation)?", inline=True)
comment(0xA14B, "Yes: skip spaces after dot", inline=True)

# Try next table entry
comment(0xA14D, "Skip 3 bytes (flags + address)", inline=True)
comment(0xA14E, "(skip 2)", inline=True)
comment(0xA14F, "(skip 3)", inline=True)
comment(0xA150, "Try next table entry", inline=True)

# End of table names — check separators
comment(0xA152, "Save Y (end of matched name)", inline=True)
comment(0xA153, "Push position", inline=True)
comment(0xA154, "Load char after matched portion", inline=True)
comment(0xA156, "Y=9: check 10 separator chars", inline=True)
comment(0xA158, "Compare with separator table", inline=True)
comment(0xA15B, "Match: valid command separator", inline=True)
comment(0xA15D, "Try next separator", inline=True)
comment(0xA15E, "Loop through separator list", inline=True)
comment(0xA160, "No separator match: restore Y", inline=True)
comment(0xA161, "Transfer back to Y", inline=True)
comment(0xA162, "Try next table entry", inline=True)
comment(0xA164, "Data: command separator table (space/quotes)", inline=True)
comment(0xA167, "Data: separator chars &24, &26", inline=True)
comment(0xA169, "Data: separator char &2A (asterisk)", inline=True)

# Valid separator found
comment(0xA16D, "Restore saved Y", inline=True)
comment(0xA16E, "Transfer to Y", inline=True)

# Skip spaces after command name
comment(0xA16F, "Load next char", inline=True)
comment(0xA171, "Is it space?", inline=True)
comment(0xA173, "No: done skipping", inline=True)
comment(0xA175, "Advance past space", inline=True)
comment(0xA176, "Loop for more spaces", inline=True)

# Check command flags
comment(0xA179, "Load command flags byte", inline=True)
comment(0xA17C, "Shift: check 'no-arg' bit", inline=True)
comment(0xA17D, "Bit clear: allow arguments", inline=True)
comment(0xA17F, "Check if line ends here", inline=True)
comment(0xA181, "Is it CR?", inline=True)
comment(0xA183, "No: argument present, V clear", inline=True)
comment(0xA185, "CR found: set V (no argument)", inline=True)
comment(0xA188, "V set: command is valid", inline=True)
comment(0xA18A, "Clear V (argument present)", inline=True)
comment(0xA18B, "C=0: command not found", inline=True)
comment(0xA18C, "Pop saved Y from stack", inline=True)
comment(0xA18D, "Load command line char at Y", inline=True)
comment(0xA18F, "Return (C and V set per result)", inline=True)

# No match in table — scan to next command word
comment(0xA190, "Advance past character", inline=True)
comment(0xA191, "Load current char", inline=True)
comment(0xA193, "Is it CR (end of line)?", inline=True)
comment(0xA195, "Yes: end of input", inline=True)
comment(0xA197, "Is it '.' (abbreviation dot)?", inline=True)
comment(0xA199, "Yes: skip to next word", inline=True)
comment(0xA19B, "Is it space?", inline=True)
comment(0xA19D, "No: keep scanning", inline=True)
comment(0xA19F, "Skip past separator", inline=True)
comment(0xA1A0, "Load next char", inline=True)
comment(0xA1A2, "Is it space?", inline=True)
comment(0xA1A4, "Yes: skip consecutive spaces", inline=True)
comment(0xA1A6, "C=1: have more text to match", inline=True)

# FS command: save pointer and parse filename
comment(0xA1A9, "Save text pointer", inline=True)
comment(0xA1AC, "Set owner-only access mask", inline=True)
comment(0xA1AF, "Parse command argument (Y=0)", inline=True)

# Open file for command (&A1B2)
comment(0xA1B2, "X=1: buffer index", inline=True)
comment(0xA1B4, "Copy argument to buffer", inline=True)
comment(0xA1B7, "A=2: open for update", inline=True)
comment(0xA1B9, "Store open mode", inline=True)
comment(0xA1BC, "Y=&12: open file command", inline=True)
comment(0xA1BE, "Send open request to server", inline=True)
comment(0xA1C1, "Load reply status", inline=True)
comment(0xA1C4, "Status 1 (success)?", inline=True)
comment(0xA1C6, "No: file not found, try library", inline=True)

# Check if file handle is available
comment(0xA1C8, "X=3: check 4 handle bytes", inline=True)
comment(0xA1CA, "Increment handle byte", inline=True)
comment(0xA1CD, "Was &FF (overflow to 0): try next", inline=True)
comment(0xA1CF, "Non-zero: handle valid, execute", inline=True)
comment(0xA1D2, "Try next handle byte", inline=True)
comment(0xA1D3, "Loop until all checked", inline=True)
comment(0xA1D5, "Allocate new FCB or raise error", inline=True)
comment(0xA1D8, "X=1: open mode index", inline=True)
comment(0xA1DA, "Store in l0f05", inline=True)
comment(0xA1DD, "Store in l0f06", inline=True)
comment(0xA1E0, "X=2", inline=True)
comment(0xA1E1, "Copy argument to buffer", inline=True)
comment(0xA1E4, "Y=6: re-open command", inline=True)
comment(0xA1E6, "Send re-open request", inline=True)
comment(0xA1E9, "C set: error on re-open", inline=True)
comment(0xA1EB, "C clear: finalise file opening", inline=True)
comment(0xA1EE, "Jump to finalise and return", inline=True)

# File not found — try library path (&A1F1)
comment(0xA1F1, "Load first char of filename", inline=True)
comment(0xA1F4, "Is it '$' (root dir)?", inline=True)
comment(0xA1F6, "Yes: no library search, error", inline=True)
comment(0xA1F8, "Load library flag byte", inline=True)
comment(0xA1FB, "Bit 7 set: library already tried", inline=True)
comment(0xA1FD, "Rotate bits to check library state", inline=True)
comment(0xA1FE, "Rotate again", inline=True)
comment(0xA1FF, "Bit 7 set: restore from backup", inline=True)
comment(0xA201, "Carry set: bad command", inline=True)

# Shift filename right to prepend "Library."
comment(0xA203, "X=&FF: pre-increment for loop", inline=True)
comment(0xA205, "Find end of filename", inline=True)
comment(0xA206, "Load filename byte", inline=True)
comment(0xA209, "Is it CR (end)?", inline=True)
comment(0xA20B, "No: continue scanning", inline=True)
comment(0xA20D, "Shift filename right by 8 bytes", inline=True)
comment(0xA210, "Store shifted byte", inline=True)
comment(0xA213, "Previous byte", inline=True)
comment(0xA214, "Loop until all shifted", inline=True)
comment(0xA216, "X=7: 'Library.' is 8 bytes", inline=True)
comment(0xA218, "Copy 'Library.' prefix", inline=True)
comment(0xA21B, "Store prefix byte", inline=True)
comment(0xA21E, "Previous byte", inline=True)
comment(0xA21F, "Loop until prefix copied", inline=True)
comment(0xA221, "Load library flag", inline=True)
comment(0xA224, "Set bits 5-6: library path active", inline=True)
comment(0xA226, "Store updated flag", inline=True)
comment(0xA229, "Retry file open with library path", inline=True)

# Restore original filename after library attempt
comment(0xA22B, "X=&FF: pre-increment for loop", inline=True)
comment(0xA22D, "Restore original filename", inline=True)
comment(0xA22E, "Load backup byte", inline=True)
comment(0xA231, "Store to filename buffer", inline=True)
comment(0xA234, "Is it CR (end)?", inline=True)
comment(0xA236, "No: continue restoring", inline=True)
comment(0xA238, "Set owner-only access mask", inline=True)
comment(0xA23B, "Set bit 7: library tried", inline=True)
comment(0xA23D, "Store updated flag", inline=True)

# error_bad_command
comment(0xA242, "Set owner-only access mask", inline=True)
comment(0xA245, "Error code &FE", inline=True)
comment(0xA247, "Generate 'Bad command' error", inline=True)

# Execute file with handle (&A252)
comment(0xA252, "X=3: check 4 execution bytes", inline=True)
comment(0xA254, "Increment execution address byte", inline=True)
comment(0xA257, "Non-zero: valid, go to OSCLI", inline=True)
comment(0xA259, "Try next byte", inline=True)
comment(0xA25A, "Loop until all checked", inline=True)
comment(0xA25C, "Error code &93", inline=True)
comment(0xA25E, "Generate 'No!' error", inline=True)

# Finalise file opening (&A265)
comment(0xA265, "Load open mode result", inline=True)
comment(0xA268, "Allocate FCB slot", inline=True)
comment(0xA26B, "Transfer to Y", inline=True)
comment(0xA26C, "A=0: clear channel status", inline=True)
comment(0xA26E, "Clear status in channel table", inline=True)
comment(0xA271, "Store handle in l1070", inline=True)
comment(0xA274, "Y=3: OSCLI execution", inline=True)
comment(0xA276, "Execute via boot/OSCLI path", inline=True)

# OSCLI argument parsing (&A281)
comment(0xA281, "Copy argument to buffer (X=0)", inline=True)
comment(0xA284, "Y=0", inline=True)
comment(0xA286, "C=0 for GSINIT", inline=True)
comment(0xA287, "Initialise GS string read", inline=True)
comment(0xA28A, "Read next GS character", inline=True)
comment(0xA28D, "C clear: more chars", inline=True)
comment(0xA28F, "Back up one position", inline=True)
comment(0xA290, "Skip trailing spaces", inline=True)
comment(0xA291, "Load next char", inline=True)
comment(0xA293, "Is it space?", inline=True)
comment(0xA295, "Yes: skip it", inline=True)
comment(0xA297, "Check for CR (end of line)", inline=True)
comment(0xA299, "C=0 for addition", inline=True)
comment(0xA29A, "Transfer Y offset to A", inline=True)
comment(0xA29B, "Add to text pointer low", inline=True)
comment(0xA29D, "Store as command tail pointer low", inline=True)
comment(0xA2A0, "Load text pointer high", inline=True)
comment(0xA2A2, "Add carry", inline=True)
comment(0xA2A4, "Store as command tail pointer high", inline=True)
comment(0xA2A7, "Save text pointer for later", inline=True)
comment(0xA2AA, "X=&0E: OSWORD parameter offset", inline=True)
comment(0xA2AC, "Store as block offset high", inline=True)
comment(0xA2AE, "A=&10: OSWORD parameter size", inline=True)
comment(0xA2B0, "Store as options pointer", inline=True)
comment(0xA2B2, "Store to l0e16", inline=True)
comment(0xA2B5, "X=&4A: FS command table offset", inline=True)
comment(0xA2B7, "Y=5", inline=True)
comment(0xA2B9, "Execute FS command iteration", inline=True)
comment(0xA2BC, "Load tube flag", inline=True)
comment(0xA2BF, "Zero: no tube transfer needed", inline=True)
comment(0xA2C1, "AND with l0f0b", inline=True)
comment(0xA2C4, "AND with l0f0c", inline=True)
comment(0xA2C7, "All &FF?", inline=True)
comment(0xA2C9, "Yes: no tube transfer needed", inline=True)
comment(0xA2CB, "Claim tube for data transfer", inline=True)
comment(0xA2CE, "X=9: parameter count", inline=True)
comment(0xA2D0, "Y=&0F: parameter offset", inline=True)
comment(0xA2D2, "A=4: tube transfer type", inline=True)
comment(0xA2D4, "Dispatch tube address/data", inline=True)
comment(0xA2D7, "A=1", inline=True)
comment(0xA2D9, "Dispatch via indirect vector", inline=True)

# find_fs_and_exit (&A2DC)
comment(0xA2DC, "Find station with bit 3 set", inline=True)
comment(0xA2DF, "Return with last flag state", inline=True)

# Unnamed: flip/set station boot (&A2E2)
comment(0xA2E2, "Flip/set station boot config", inline=True)
comment(0xA2E5, "Return with last flag state", inline=True)

# find_station_bit2 (&A2E8) — find station with bit 2 set
comment(0xA2E8, "X=&10: scan 16 slots (15 to 0)", inline=True)
comment(0xA2EA, "Clear V", inline=True)
comment(0xA2EB, "Try next slot", inline=True)
comment(0xA2EC, "All slots checked: not found", inline=True)
comment(0xA2EE, "Compare station/network", inline=True)
comment(0xA2F1, "No match: try next", inline=True)
comment(0xA2F3, "Load slot status byte", inline=True)
comment(0xA2F6, "Test bit 2 (PS active flag)?", inline=True)
comment(0xA2F8, "Not set: try next", inline=True)
comment(0xA2FA, "Transfer Y to A", inline=True)
comment(0xA2FB, "Store Y in slot data", inline=True)
comment(0xA2FE, "Set V (found match)", inline=True)
comment(0xA301, "Store Y to l0e02", inline=True)
comment(0xA304, "V set: found, skip allocation", inline=True)
comment(0xA306, "Transfer Y to A", inline=True)
comment(0xA307, "Allocate FCB slot", inline=True)
comment(0xA30A, "Store allocation result", inline=True)
comment(0xA30D, "Zero: failed, restore context", inline=True)
comment(0xA30F, "A=&26: station flags value", inline=True)

# find_station_bit3 (&A313) — find station with bit 3 set
comment(0xA313, "X=&10: scan 16 slots (15 to 0)", inline=True)
comment(0xA315, "Clear V", inline=True)
comment(0xA316, "Try next slot", inline=True)
comment(0xA317, "All slots checked: not found", inline=True)
comment(0xA319, "Compare station/network", inline=True)
comment(0xA31C, "No match: try next", inline=True)
comment(0xA31E, "Load slot status byte", inline=True)
comment(0xA321, "Test bit 3 (FS active flag)?", inline=True)
comment(0xA323, "Not set: try next", inline=True)
comment(0xA325, "Transfer Y to A", inline=True)
comment(0xA326, "Store Y in slot data", inline=True)
comment(0xA329, "Set V (found match)", inline=True)
comment(0xA32C, "Store Y to l0e03", inline=True)
comment(0xA32F, "V set: found, skip allocation", inline=True)
comment(0xA331, "Transfer Y to A", inline=True)
comment(0xA332, "Allocate FCB slot", inline=True)
comment(0xA335, "Store allocation result", inline=True)
comment(0xA338, "Zero: failed, restore context", inline=True)
comment(0xA33A, "A=&2A: station flags value", inline=True)

# print_inline gaps (&9132-&9154) — fill remaining items
comment(0x9132, "Store as string pointer low", inline=True)
comment(0x9135, "Store as string pointer high", inline=True)
comment(0x9137, "Y=0: index for indirect loads", inline=True)
comment(0x913B, "No page crossing", inline=True)
comment(0x913D, "Carry into high byte", inline=True)
comment(0x9143, "Save string pointer on stack", inline=True)
comment(0x9145, "(push low byte)", inline=True)
comment(0x9146, "Save pointer high byte", inline=True)
comment(0x9148, "(push high byte)", inline=True)
comment(0x914E, "Restore string pointer high", inline=True)
comment(0x914F, "Store pointer high", inline=True)
comment(0x9151, "Restore string pointer low", inline=True)
comment(0x9152, "Store pointer low", inline=True)
comment(0x9154, "Loop for next character", inline=True)

# parse_addr_arg (&915A) — parse hex (&nn) or decimal number
# fs_work_4 controls mode: 0=net.station, &FF=decimal-only
comment(0x915A, "Clear accumulator", inline=True)
comment(0x915C, "Initialise result to zero", inline=True)
comment(0x915E, "Get first character of argument", inline=True)
comment(0x9160, "Is it '&' (hex prefix)?", inline=True)
comment(0x9162, "No: try decimal path", inline=True)
comment(0x9164, "Skip '&' prefix", inline=True)
comment(0x9165, "Get first hex digit", inline=True)
comment(0x9167, "C always set from CMP: validate digit", inline=True)

# Hex digit loop — reads chars, checks for '.'/terminator
comment(0x9169, "Advance to next character", inline=True)
comment(0x916A, "Get next character", inline=True)
comment(0x916C, "Is it '.' (net.station separator)?", inline=True)
comment(0x916E, "Yes: handle dot separator", inline=True)
comment(0x9170, "Below '!' (space/control)?", inline=True)
comment(0x9172, "Yes: end of number", inline=True)

# Hex digit validation — '0'-'9' or case-insensitive 'A'-'F'
comment(0x9174, "Below '0'?", inline=True)
comment(0x9176, "Not a digit: bad hex", inline=True)
comment(0x9178, "Above '9'?", inline=True)
comment(0x917A, "Decimal digit: extract value", inline=True)
comment(0x917C, "Force uppercase", inline=True)
comment(0x917E, "Map 'A'-'F' to &FA-&FF", inline=True)
comment(0x9180, "Overflow: not A-F", inline=True)
comment(0x9182, "Valid hex letter (A-F)?", inline=True)
comment(0x9184, "Below A: bad hex", inline=True)

# Accumulate hex digit — shift result left 4, add digit
comment(0x9186, "Extract digit value (0-15)", inline=True)
comment(0x9188, "Save current digit", inline=True)
comment(0x918A, "Load running result", inline=True)
comment(0x918C, "Would shift overflow a byte?", inline=True)
comment(0x918E, "Yes: overflow error", inline=True)
comment(0x9190, "Shift result left 4 (x16)", inline=True)
comment(0x9191, "(shift 2)", inline=True)
comment(0x9192, "(shift 3)", inline=True)
comment(0x9193, "(shift 4)", inline=True)
comment(0x9194, "Add new hex digit", inline=True)
comment(0x9196, "Store updated result", inline=True)
comment(0x9198, "Loop for next hex digit", inline=True)

# Decimal path — parse digits with multiply-by-10
comment(0x919A, "Get current character", inline=True)
comment(0x919C, "Is it '.' (net.station separator)?", inline=True)
comment(0x919E, "Yes: handle dot separator", inline=True)
comment(0x91A0, "Below '!' (space/control)?", inline=True)
comment(0x91A2, "Yes: end of number", inline=True)
comment(0x91A4, "Is it a decimal digit?", inline=True)
comment(0x91A7, "No: 'Bad number' error", inline=True)
comment(0x91A9, "Extract digit value (0-9)", inline=True)
comment(0x91AB, "Save current digit", inline=True)
comment(0x91AD, "result * 2", inline=True)
comment(0x91AF, "Overflow", inline=True)
comment(0x91B1, "Load result * 2", inline=True)
comment(0x91B3, "result * 4", inline=True)
comment(0x91B4, "Overflow", inline=True)
comment(0x91B6, "result * 8", inline=True)
comment(0x91B7, "Overflow", inline=True)
comment(0x91B9, "* 8 + * 2 = result * 10", inline=True)
comment(0x91BB, "Overflow", inline=True)
comment(0x91BD, "result * 10 + new digit", inline=True)
comment(0x91BF, "Overflow", inline=True)
comment(0x91C1, "Store updated result", inline=True)
comment(0x91C3, "Advance to next character", inline=True)
comment(0x91C4, "Loop (always branches)", inline=True)

# End-of-number validation
comment(0x91C6, "Check parsing mode", inline=True)
comment(0x91C8, "Bit 7 clear: net.station mode", inline=True)
comment(0x91CA, "Decimal-only mode: get result", inline=True)
comment(0x91CC, "Zero: 'Bad parameter'", inline=True)
comment(0x91CE, "Return with result in A", inline=True)

# Station number validation
comment(0x91CF, "Get parsed station number", inline=True)
comment(0x91D1, "Station 255 is reserved", inline=True)
comment(0x91D3, "255: 'Bad station number'", inline=True)
comment(0x91D5, "Reload result", inline=True)
comment(0x91D7, "Non-zero: valid station", inline=True)
comment(0x91D9, "Zero result: check if dot was seen", inline=True)
comment(0x91DB, "No dot and zero: 'Bad station number'", inline=True)
comment(0x91DD, "Check character before current pos", inline=True)
comment(0x91DE, "Load previous character", inline=True)
comment(0x91E0, "Restore Y", inline=True)
comment(0x91E1, "Was previous char '.'?", inline=True)
comment(0x91E3, "No: 'Bad station number'", inline=True)

# Valid station: return with C set
comment(0x91E5, "C=1: number was parsed", inline=True)
comment(0x91E6, "Return (result in fs_load_addr_2)", inline=True)

# Dot separator — store network part, set dot-seen flag
comment(0x91E7, "Check if dot already seen", inline=True)
comment(0x91E9, "Already seen: 'Bad number'", inline=True)
comment(0x91EB, "Set dot-seen flag", inline=True)
comment(0x91ED, "Get network number (before dot)", inline=True)
comment(0x91EF, "Network 255 is reserved", inline=True)
comment(0x91F1, "255: 'Bad network number'", inline=True)
comment(0x91F3, "Return to caller with network part", inline=True)

# Error handlers for parse_addr_arg
comment(0x91F4, "Error code &F1", inline=True)
comment(0x91F6, "Generate 'Bad hex' error", inline=True)
comment(0x91FD, "Test parsing mode", inline=True)
comment(0x91FF, "Decimal mode: 'Bad parameter'", inline=True)
comment(0x9201, "Error code &D0", inline=True)
comment(0x9203, "Generate 'Bad station number' error", inline=True)
comment(0x9215, "Error code &F0", inline=True)
comment(0x9217, "Generate 'Bad number' error", inline=True)
comment(0x9221, "Error code &94", inline=True)
comment(0x9223, "Generate 'Bad parameter' error", inline=True)
comment(0x9230, "Error code &D1", inline=True)
comment(0x9232, "Generate 'Bad network number' error", inline=True)

# is_decimal_digit (&9244) — test if char is decimal digit
# Also rejects '&' and '.' as non-decimal
comment(0x9244, "Is it '&' (hex prefix)?", inline=True)
comment(0x9246, "Yes: return C set (not decimal)", inline=True)
comment(0x9248, "Is it '.' (separator)?", inline=True)
comment(0x924A, "Yes: return C set (not decimal)", inline=True)
# is_dec_digit_only entry — pure digit test
comment(0x924C, "Above '9'?", inline=True)
comment(0x924E, "Yes: not a digit", inline=True)
comment(0x9250, "Below '0'? C clear if so", inline=True)
comment(0x9252, "Return: C set if '0'-'9'", inline=True)
comment(0x9253, "C=0: not a digit", inline=True)
comment(0x9254, "Return", inline=True)

# get_access_bits (&9255) — encode directory access byte
comment(0x9255, "Offset &0E in directory entry", inline=True)
comment(0x9257, "Load raw access byte", inline=True)
comment(0x9259, "Mask to 6 access bits", inline=True)
comment(0x925B, "X=4: start encoding at bit 4", inline=True)
comment(0x925D, "ALWAYS branch to encoder", inline=True)

# get_prot_bits (&925F) — encode protection attribute
comment(0x925F, "Mask to 5 protection bits", inline=True)
comment(0x9261, "X=&FF: start encoding at bit 0", inline=True)

# Shared encoder loop — maps source bits via lookup table
comment(0x9263, "Save remaining bits", inline=True)
comment(0x9265, "Clear encoded result", inline=True)
comment(0x9267, "Advance to next table position", inline=True)
comment(0x9268, "Shift out lowest source bit", inline=True)
comment(0x926A, "Bit clear: skip this position", inline=True)
comment(0x926C, "Bit set: OR in encoded value", inline=True)
comment(0x926F, "More bits to process", inline=True)
comment(0x9271, "Return encoded access in A", inline=True)

# set_text_and_xfer_ptr (&927D) — set OSWORD text and transfer pointers
comment(0x927D, "Set text pointer low", inline=True)
comment(0x927F, "Set text pointer high", inline=True)

# set_xfer_params (&9281) — set transfer parameters
comment(0x9281, "Store transfer byte count", inline=True)
comment(0x9283, "Store source pointer low", inline=True)
comment(0x9285, "Store source pointer high", inline=True)

# set_options_ptr (&9287) — set options block pointer
comment(0x9287, "Store options pointer low", inline=True)
comment(0x9289, "Store options pointer high", inline=True)

# clear_escapable (&928B) — clear escape-sensitive flag
comment(0x928B, "Save processor flags", inline=True)
comment(0x928C, "Clear bit 0 of escape flag", inline=True)
comment(0x928E, "Restore processor flags", inline=True)
comment(0x928F, "Return", inline=True)

# cmp_5byte_handle (&9290) — compare 5-byte channel handle
comment(0x9290, "Compare 5 bytes (indices 4 down to 1)", inline=True)
comment(0x9292, "Load byte from handle buffer", inline=True)
comment(0x9294, "Compare with channel handle", inline=True)
comment(0x9296, "Mismatch: return Z=0", inline=True)
comment(0x9298, "Next byte", inline=True)
comment(0x9299, "Loop until all compared", inline=True)
comment(0x929B, "Return: Z=1 if all 5 matched", inline=True)

# Dead code (&929C-&92A0) — unreachable
comment(0x929C, "Unreachable code", inline=True)
comment(0x929E, "(dead)", inline=True)
comment(0x92A0, "(dead)", inline=True)

# set_conn_active (&92A1) — set channel connection active flag
comment(0x92A1, "Save processor flags", inline=True)
comment(0x92A2, "Save A", inline=True)
comment(0x92A3, "Transfer X to A", inline=True)
comment(0x92A4, "Save original X", inline=True)
comment(0x92A5, "Get stack pointer", inline=True)
comment(0x92A6, "Read original A from stack", inline=True)
comment(0x92A9, "Convert to channel index", inline=True)
comment(0x92AC, "No channel found: skip", inline=True)
comment(0x92AE, "Bit 6: connection active flag", inline=True)
comment(0x92B0, "Set active flag in channel table", inline=True)
comment(0x92B3, "Store updated status", inline=True)
comment(0x92B6, "ALWAYS branch to exit", inline=True)

# clear_conn_active (&92B8) — clear channel connection active flag
comment(0x92B8, "Save processor flags", inline=True)
comment(0x92B9, "Save A", inline=True)
comment(0x92BA, "Transfer X to A", inline=True)
comment(0x92BB, "Save original X", inline=True)
comment(0x92BC, "Get stack pointer", inline=True)
comment(0x92BD, "Read original A from stack", inline=True)
comment(0x92C0, "Convert to channel index", inline=True)
comment(0x92C3, "No channel found: skip", inline=True)
comment(0x92C5, "Bit 6 clear mask (&BF = ~&40)", inline=True)
comment(0x92C7, "Clear active flag in channel table", inline=True)
comment(0x92CA, "Store updated status", inline=True)

# Shared exit for set/clear_conn_active
comment(0x92CD, "Restore X", inline=True)
comment(0x92CE, "Transfer back to X", inline=True)
comment(0x92CF, "Restore A", inline=True)
comment(0x92D0, "Restore processor flags", inline=True)
comment(0x92D1, "Return", inline=True)

# svc_8_osword (&A4D6): Service 8 — OSWORD dispatch
# Handles OSWORD &0E-&14: clock read, transmit, receive, etc.
# Primary dispatch via PHA/PHA/RTS from tables at &A508/&A50F

# Entry: validate OSWORD number and dispatch
comment(0xA4D6, "CLC so SBC subtracts value+1", inline=True)
comment(0xA4D7, "A = OSWORD number", inline=True)
comment(0xA4D9, "A = OSWORD - &0E (CLC+SBC = -&0E)", inline=True)
comment(0xA4DB, "Below &0E: not ours, return", inline=True)
comment(0xA4DD, "Index >= 7? (OSWORD > &14)", inline=True)
comment(0xA4DF, "Above &14: not ours, return", inline=True)
comment(0xA4E1, "Set up dispatch and save state", inline=True)

# Copy osword_flag to parameter block on return
comment(0xA4E4, "Copy 3 bytes (Y=2,1,0)", inline=True)
comment(0xA4E6, "Load from RX buffer", inline=True)
comment(0xA4E8, "Store to osword_flag workspace", inline=True)
comment(0xA4EB, "Next byte down", inline=True)
comment(0xA4EC, "Loop for all 3 bytes", inline=True)
comment(0xA4EE, "Return from svc_8_osword", inline=True)

# osword_setup_handler: push handler address and save state
comment(0xA4EF, "X = OSWORD index (0-6)", inline=True)
comment(0xA4F0, "Load handler address high byte", inline=True)
comment(0xA4F3, "Push high byte for RTS dispatch", inline=True)
comment(0xA4F4, "Load handler address low byte", inline=True)
comment(0xA4F7, "Push low byte for RTS dispatch", inline=True)
comment(0xA4F8, "Copy 3 bytes (Y=2,1,0)", inline=True)

# Save osword_flag to RX buffer (reverse of return copy)
comment(0xA4FA, "Load from osword_flag workspace", inline=True)
comment(0xA4FD, "Store to RX buffer", inline=True)
comment(0xA4FF, "Next byte down", inline=True)
comment(0xA500, "Loop for all 3 bytes", inline=True)
comment(0xA502, "Y=0 (INY from -1)", inline=True)
comment(0xA503, "Load PB byte 0 (OSWORD sub-code)", inline=True)
comment(0xA505, "Clear service state", inline=True)
comment(0xA507, "RTS dispatches to pushed handler", inline=True)

# Dispatch tables at &A508 (lo) and &A50F (hi) are handled by
# rts_code_ptr() calls which produce symbolic label expressions.

# OSWORD &0E handler (&A516): read clock
# Copies clock data and converts binary to BCD
comment(0xA516, "Save A for later test", inline=True)
comment(0xA517, "Test station active flag", inline=True)
comment(0xA51A, "Not active: just return", inline=True)
comment(0xA51C, "Restore A (OSWORD sub-code)", inline=True)
comment(0xA51D, "Sub-code = 4? (read clock)", inline=True)
comment(0xA51F, "Yes: handle clock read", inline=True)
comment(0xA521, "Other sub-codes: set state = 8", inline=True)
comment(0xA523, "Store service state", inline=True)
comment(0xA525, "Return", inline=True)

# Clock read handler (&A526): read time from workspace, convert to BCD
comment(0xA526, "X=0: start of TX control block", inline=True)
comment(0xA528, "Y=&10: length of TXCB to save", inline=True)
comment(0xA52A, "Save current TX control block", inline=True)
comment(0xA52D, "Load seconds from clock workspace", inline=True)
comment(0xA530, "Convert binary to BCD", inline=True)
comment(0xA533, "Store BCD seconds", inline=True)
comment(0xA536, "Load minutes from clock workspace", inline=True)
comment(0xA539, "Convert binary to BCD", inline=True)
comment(0xA53C, "Store BCD minutes", inline=True)
comment(0xA53F, "Load hours from clock workspace", inline=True)
comment(0xA542, "Convert binary to BCD", inline=True)
comment(0xA545, "Store BCD hours", inline=True)
comment(0xA548, "Clear hours high position", inline=True)
comment(0xA54A, "Store zero", inline=True)
comment(0xA54D, "Load day+month byte", inline=True)
comment(0xA550, "Save for later high nibble extract", inline=True)
comment(0xA551, "Load day value", inline=True)
comment(0xA554, "Convert day to BCD", inline=True)
comment(0xA557, "Store BCD day", inline=True)
comment(0xA55A, "Restore day+month byte", inline=True)
comment(0xA55B, "Save again for month extract", inline=True)
comment(0xA55C, "Mask low nibble (month low bits)", inline=True)
comment(0xA55E, "Convert to BCD", inline=True)
comment(0xA561, "Store BCD month", inline=True)
comment(0xA564, "Restore day+month byte", inline=True)
comment(0xA565, "Shift high nibble down", inline=True)
comment(0xA566, "Continue shifting", inline=True)
comment(0xA567, "Continue shifting", inline=True)
comment(0xA568, "4th shift: isolate high nibble", inline=True)
comment(0xA569, "Add &51 for year offset + carry", inline=True)
comment(0xA56B, "Convert year to BCD", inline=True)
comment(0xA56E, "Store BCD year", inline=True)
comment(0xA571, "Copy 7 bytes (Y=6 down to 0)", inline=True)

# Copy BCD result to OSWORD parameter block
comment(0xA573, "Load BCD byte from workspace", inline=True)
comment(0xA576, "Store to parameter block", inline=True)
comment(0xA578, "Next byte down", inline=True)
comment(0xA579, "Loop for all 7 bytes", inline=True)
comment(0xA57B, "Return", inline=True)

# bin_to_bcd: convert binary value in A to BCD
comment(0xA57C, "Save processor flags (decimal mode)", inline=True)
comment(0xA57D, "X = binary count", inline=True)
comment(0xA57E, "Zero: result is 0, skip loop", inline=True)
comment(0xA580, "Set decimal mode for BCD add", inline=True)
comment(0xA581, "Start BCD result at 0", inline=True)
comment(0xA583, "Clear carry for BCD add", inline=True)
comment(0xA584, "Add 1 in decimal mode", inline=True)
comment(0xA586, "Count down binary value", inline=True)
comment(0xA587, "Loop until zero", inline=True)
comment(0xA589, "Restore flags (clears decimal mode)", inline=True)
comment(0xA58A, "Return with BCD result in A", inline=True)

# OSWORD &10 handler (&A58B): transmit
comment(0xA58B, "Shift ws_0d60 left (status flag)", inline=True)
comment(0xA58E, "A = Y (saved index)", inline=True)
comment(0xA58F, "C=1: transmit active path", inline=True)
comment(0xA591, "C=0: store Y to parameter block", inline=True)
comment(0xA593, "Return (transmit not active)", inline=True)

# Transmit active: set up and begin
comment(0xA594, "Set workspace high byte", inline=True)
comment(0xA596, "Copy to ws_ptr_hi", inline=True)
comment(0xA598, "Also set as NMI TX block high", inline=True)
comment(0xA59A, "Low byte = &6F", inline=True)
comment(0xA59C, "Set ws_ptr_lo", inline=True)
comment(0xA59E, "Set NMI TX block low", inline=True)
comment(0xA5A0, "X=&0F: byte count for copy", inline=True)
comment(0xA5A2, "Copy data and begin transmission", inline=True)
comment(0xA5A5, "Jump to begin Econet transmission", inline=True)

# store_osword_pb_ptr: store parameter block pointers to workspace
comment(0xA601, "Y=&1C: workspace offset", inline=True)
comment(0xA603, "Load PB pointer low byte", inline=True)
comment(0xA605, "Add 1 (C from earlier operation)", inline=True)
comment(0xA607, "Store ptr at workspace+Y", inline=True)
comment(0xA60A, "Y=1: read PB byte 1", inline=True)
comment(0xA60C, "Load transfer length from PB", inline=True)
comment(0xA60E, "Y=&20: second workspace offset", inline=True)
comment(0xA610, "Add PB low byte to get end ptr", inline=True)

# store_ptr_at_ws_y: store 16-bit pointer to workspace
comment(0xA612, "Store low byte to workspace+Y", inline=True)
comment(0xA614, "Next byte", inline=True)
comment(0xA615, "Load PB pointer high byte", inline=True)
comment(0xA617, "Add carry", inline=True)
comment(0xA619, "Store high byte to workspace+Y+1", inline=True)
comment(0xA61B, "Return", inline=True)

# OSWORD &12 handler (&A61C): receive setup
comment(0xA61C, "Set workspace from RX ptr high", inline=True)
comment(0xA61E, "Store to ws_ptr_hi", inline=True)
comment(0xA620, "Y=&7F: last byte of RX buffer", inline=True)
comment(0xA622, "Load port/count from RX buffer", inline=True)
comment(0xA624, "Y=&80: set workspace pointer", inline=True)
comment(0xA625, "Store as ws_ptr_lo", inline=True)
comment(0xA627, "X = port/count value", inline=True)
comment(0xA628, "X-1: adjust count", inline=True)
comment(0xA629, "Y=0 for copy", inline=True)
comment(0xA62B, "Copy workspace data", inline=True)
comment(0xA62E, "Update state and return", inline=True)

# ca6fb: copy between workspace and parameter block
comment(0xA6FB, "C=0: skip PB-to-WS copy", inline=True)
comment(0xA6FD, "C=1: load from parameter block", inline=True)
comment(0xA6FF, "Store to workspace", inline=True)
comment(0xA701, "Load from workspace", inline=True)
comment(0xA703, "Store to parameter block", inline=True)
comment(0xA705, "Next byte", inline=True)
comment(0xA706, "Count down", inline=True)
comment(0xA707, "Loop for all bytes", inline=True)
comment(0xA709, "Return", inline=True)

# init_bridge_poll (&A868): initialise bridge polling
comment(0xA868, "Check bridge status", inline=True)
comment(0xA86B, "Is it &FF (uninitialised)?", inline=True)
comment(0xA86D, "No: bridge already active, return", inline=True)
comment(0xA86F, "Save Y", inline=True)
comment(0xA870, "Preserve Y on stack", inline=True)
comment(0xA871, "Y=&18: workspace offset for init", inline=True)
comment(0xA873, "X=&0B: 12 bytes to copy", inline=True)
comment(0xA875, "Rotate l0d61 right (save flag)", inline=True)

# Copy bridge init data to workspace and TXCB
comment(0xA878, "Load init data byte", inline=True)
comment(0xA87B, "Store to workspace", inline=True)
comment(0xA87D, "Load TXCB template byte", inline=True)
comment(0xA880, "Store to TX control block", inline=True)
comment(0xA882, "Next workspace byte", inline=True)
comment(0xA883, "Next template byte", inline=True)
comment(0xA884, "Loop for all 12 bytes", inline=True)
comment(0xA886, "Store X (-1) as bridge counter", inline=True)
comment(0xA889, "Restore l0d61 flag", inline=True)

# Poll loop: wait for line idle, transmit, check response
comment(0xA88C, "Shift ws_0d60 left (check status)", inline=True)
comment(0xA88F, "C=0: status clear, retry", inline=True)
comment(0xA891, "Control byte &82 for TX", inline=True)
comment(0xA893, "Set in TX control block", inline=True)
comment(0xA895, "Data block at &00C0", inline=True)
comment(0xA897, "Set NMI TX block low", inline=True)
comment(0xA899, "High byte = 0 (page 0)", inline=True)
comment(0xA89B, "Set NMI TX block high", inline=True)
comment(0xA89D, "Begin Econet transmission", inline=True)

# Wait for TX complete
comment(0xA8A0, "Test TX control block bit 7", inline=True)
comment(0xA8A2, "Negative: TX still in progress", inline=True)
comment(0xA8A4, "X = result status", inline=True)
comment(0xA8A5, "Save TX status", inline=True)
comment(0xA8A6, "Save PB pointer high", inline=True)
comment(0xA8A8, "Push for later restore", inline=True)
comment(0xA8A9, "X = PB pointer low", inline=True)
comment(0xA8AB, "OSBYTE &13: wait for VSYNC", inline=True)
comment(0xA8AD, "Wait for vertical sync", inline=True)
comment(0xA8B0, "Restore PB pointer high", inline=True)
comment(0xA8B1, "Restore to osword_pb_ptr_hi", inline=True)
comment(0xA8B3, "Restore TX status", inline=True)
comment(0xA8B4, "Back to X", inline=True)
comment(0xA8B5, "Y=&18: check workspace response", inline=True)
comment(0xA8B7, "Load bridge response", inline=True)
comment(0xA8B9, "Negative: bridge responded", inline=True)
comment(0xA8BB, "Advance retry counter by 8", inline=True)
comment(0xA8BE, "Positive: retry poll loop", inline=True)

# Bridge response received
comment(0xA8C0, "Set response to &3F (OK)", inline=True)
comment(0xA8C2, "Store to workspace", inline=True)
comment(0xA8C4, "Restore saved Y", inline=True)
comment(0xA8C5, "Back to Y", inline=True)
comment(0xA8C6, "Load bridge status", inline=True)
comment(0xA8C9, "X = bridge status", inline=True)
comment(0xA8CA, "Complement status", inline=True)
comment(0xA8CC, "Status was &FF: return (no bridge)", inline=True)
comment(0xA8CE, "Return bridge station in A", inline=True)
comment(0xA8CF, "Return", inline=True)

# OSWORD &14 handler (&A8D0): network file operation
comment(0xA8D0, "Compare sub-code with 1", inline=True)
comment(0xA8D2, "Sub-code >= 1: handle TX request", inline=True)
comment(0xA8D4, "Test station active flag", inline=True)
comment(0xA8D7, "Not active: return", inline=True)
comment(0xA8D9, "Y=&23: workspace offset for params", inline=True)
comment(0xA8DB, "Set owner access mask", inline=True)

# Copy init_txcb template to workspace
comment(0xA8DE, "Load TXCB init byte", inline=True)
comment(0xA8E1, "Non-zero: use template value", inline=True)
comment(0xA8E3, "Zero: use workspace default value", inline=True)
comment(0xA8E6, "Store to workspace", inline=True)
comment(0xA8E8, "Next byte down", inline=True)
comment(0xA8E9, "Until Y reaches &17", inline=True)
comment(0xA8EB, "Loop for all bytes", inline=True)
comment(0xA8ED, "Y=&18 (INY from &17)", inline=True)
comment(0xA8EE, "Set net_tx_ptr low byte", inline=True)
comment(0xA8F0, "Store PB pointer to workspace", inline=True)
comment(0xA8F3, "Y=2: parameter offset", inline=True)
comment(0xA8F5, "Control byte &90", inline=True)
comment(0xA8F7, "Set escapable flag", inline=True)
comment(0xA8F9, "Store control byte to PB", inline=True)
comment(0xA8FD, "Load workspace data", inline=True)
comment(0xA900, "Store to parameter block", inline=True)
comment(0xA902, "Next byte", inline=True)
comment(0xA903, "Until Y reaches 7", inline=True)
comment(0xA905, "Loop for 3 bytes (Y=4,5,6)", inline=True)
comment(0xA907, "Set TX pointer high byte", inline=True)
comment(0xA909, "Store to net_tx_ptr_hi", inline=True)
comment(0xA90B, "Enable interrupts", inline=True)
comment(0xA90C, "Send the network packet", inline=True)
comment(0xA90F, "Y=&20: workspace offset", inline=True)
comment(0xA911, "Set to &FF (pending)", inline=True)
comment(0xA913, "Mark send pending in workspace", inline=True)
comment(0xA916, "Also mark offset &21", inline=True)
comment(0xA918, "Y=&19: control offset", inline=True)
comment(0xA91A, "Control byte &90", inline=True)
comment(0xA91C, "Store to workspace", inline=True)
comment(0xA91E, "Y=&18: RX control offset", inline=True)
comment(0xA91F, "Control byte &7F", inline=True)
comment(0xA921, "Store RX control", inline=True)
comment(0xA923, "Wait for TX acknowledgement", inline=True)

# TX request handler (&A926)
comment(0xA926, "Save processor flags", inline=True)
comment(0xA927, "Y=1: PB offset for station", inline=True)
comment(0xA929, "Load station number from PB", inline=True)
comment(0xA92B, "X = station number", inline=True)
comment(0xA92D, "Load network number from PB", inline=True)
comment(0xA92F, "Y=3: workspace start offset", inline=True)
comment(0xA930, "Store Y as ws_ptr_lo", inline=True)
comment(0xA932, "Y=&72: workspace offset for dest", inline=True)
comment(0xA934, "Store network to workspace", inline=True)
comment(0xA936, "Y=&71", inline=True)
comment(0xA937, "A = station (from X)", inline=True)
comment(0xA938, "Store station to workspace", inline=True)
comment(0xA93A, "Restore flags from PHP", inline=True)
comment(0xA93B, "Non-zero sub-code: handle burst", inline=True)

# Sub-code 0: character-by-character send loop
comment(0xA93D, "Load current offset", inline=True)
comment(0xA93F, "Advance offset for next byte", inline=True)
comment(0xA941, "Load next char from PB", inline=True)
comment(0xA943, "Zero: end of data, return", inline=True)
comment(0xA945, "Y=&7D: workspace char offset", inline=True)
comment(0xA947, "Store char to RX buffer", inline=True)
comment(0xA949, "Save char for later test", inline=True)
comment(0xA94A, "Init workspace copy for wide xfer", inline=True)
comment(0xA94D, "Enable IRQ and send packet", inline=True)

# Short delay loop
comment(0xA950, "Delay countdown", inline=True)
comment(0xA951, "Loop for short delay", inline=True)
comment(0xA953, "Restore char", inline=True)
comment(0xA954, "Test if char was CR (&0D)", inline=True)
comment(0xA956, "Not CR: send next char", inline=True)
comment(0xA958, "CR sent: return", inline=True)

# Sub-code != 0: burst transmit (&A959)
comment(0xA959, "Init workspace for wide copy", inline=True)
comment(0xA95C, "Y=&7B: workspace offset", inline=True)
comment(0xA95E, "Load buffer size", inline=True)
comment(0xA960, "Add 3 for header", inline=True)
comment(0xA962, "Store adjusted size", inline=True)

# enable_irq_and_poll
comment(0xA964, "Enable interrupts", inline=True)
comment(0xA965, "Send packet and return", inline=True)

# Dispatch interceptor (&A968): hook into OSWORD processing
comment(0xA968, "Save processor flags", inline=True)
comment(0xA969, "Save A", inline=True)
comment(0xA96A, "Save X", inline=True)
comment(0xA96B, "Push X", inline=True)
comment(0xA96C, "Save Y", inline=True)
comment(0xA96D, "Push Y", inline=True)
comment(0xA96E, "Get stack pointer", inline=True)
comment(0xA96F, "Read OSWORD number from stack", inline=True)
comment(0xA972, "OSWORD >= 9?", inline=True)
comment(0xA974, "Yes: out of range, restore + return", inline=True)
comment(0xA976, "X = OSWORD number", inline=True)
comment(0xA977, "Push handler address for dispatch", inline=True)

# Restore registers and return
comment(0xA97A, "Restore Y", inline=True)
comment(0xA97B, "Back to Y", inline=True)
comment(0xA97C, "Restore X", inline=True)
comment(0xA97D, "Back to X", inline=True)
comment(0xA97E, "Restore A", inline=True)
comment(0xA97F, "Restore processor flags", inline=True)
comment(0xA980, "RTS dispatches via pushed address", inline=True)

# push_osword_handler_addr
comment(0xA981, "Load handler high byte from table", inline=True)
comment(0xA984, "Push for RTS dispatch", inline=True)
comment(0xA985, "Load handler low byte from table", inline=True)
comment(0xA988, "Push for RTS dispatch", inline=True)
comment(0xA989, "Reload OSWORD number for handler", inline=True)
comment(0xA98B, "RTS will dispatch to handler", inline=True)

# tx_econet_abort: send abort to remote station
comment(0xA9AC, "Y=&D9: workspace abort offset", inline=True)
comment(0xA9AE, "Store abort code to workspace", inline=True)
comment(0xA9B0, "Control byte &80 (abort)", inline=True)
comment(0xA9B2, "Y=&0C: control offset", inline=True)
comment(0xA9B4, "Store control byte", inline=True)
comment(0xA9B6, "Save current TX ptr low", inline=True)
comment(0xA9B8, "Push on stack", inline=True)
comment(0xA9B9, "Save current TX ptr high", inline=True)
comment(0xA9BB, "Push on stack", inline=True)
comment(0xA9BC, "Set TX ptr to workspace offset", inline=True)
comment(0xA9BE, "Load workspace high byte", inline=True)
comment(0xA9C0, "Set TX ptr high", inline=True)
comment(0xA9C2, "Send the abort packet", inline=True)
comment(0xA9C5, "Set status to &3F (complete)", inline=True)
comment(0xA9C7, "Store at TX ptr offset 0", inline=True)
comment(0xA9C9, "Restore TX ptr high", inline=True)
comment(0xA9CA, "Back to net_tx_ptr_hi", inline=True)
comment(0xA9CC, "Restore TX ptr low", inline=True)
comment(0xA9CD, "Back to net_tx_ptr", inline=True)
comment(0xA9CF, "Return", inline=True)

# OSWORD handler (&A9D0): handle claim/release
comment(0xA9D0, "Load PB pointer high", inline=True)
comment(0xA9D2, "Compare with &81 (special case)", inline=True)
comment(0xA9D4, "Match: skip to processing", inline=True)
comment(0xA9D6, "Y=1: first claim code position", inline=True)
comment(0xA9D8, "X=&0A: 11 codes to check", inline=True)
comment(0xA9DA, "Search claim code table", inline=True)
comment(0xA9DD, "Found: skip to processing", inline=True)
comment(0xA9DF, "Try second table range", inline=True)
comment(0xA9E0, "Y=-1: flag second range", inline=True)
comment(0xA9E1, "X=&11: 18 codes to check", inline=True)
comment(0xA9E3, "Search claim code table", inline=True)
comment(0xA9E6, "Found: skip to processing", inline=True)
comment(0xA9E8, "Not found: increment Y", inline=True)

# Process claim result
comment(0xA9E9, "X=2: default state", inline=True)
comment(0xA9EB, "A = Y (search result)", inline=True)
comment(0xA9EC, "Zero: not found, return", inline=True)
comment(0xA9EE, "Save result flags", inline=True)
comment(0xA9EF, "Positive: use state X=2", inline=True)
comment(0xA9F2, "Y=&DC: workspace offset for save", inline=True)

# Save tube claim data to workspace
comment(0xA9F4, "Load tube claim ID byte", inline=True)
comment(0xA9F7, "Store to workspace", inline=True)
comment(0xA9F9, "Next byte down", inline=True)
comment(0xA9FA, "Until Y reaches &DA", inline=True)
comment(0xA9FC, "Loop for 3 bytes", inline=True)
comment(0xA9FE, "A = state (2 or 3)", inline=True)
comment(0xA9FF, "Send abort with state code", inline=True)
comment(0xAA02, "Restore flags", inline=True)
comment(0xAA03, "Positive: return without poll", inline=True)
comment(0xAA05, "Set control to &7F", inline=True)
comment(0xAA07, "Y=&0C: control offset", inline=True)
comment(0xAA09, "Store control byte", inline=True)

# Wait for response
comment(0xAA0B, "Load status from workspace", inline=True)
comment(0xAA0D, "Positive: keep waiting", inline=True)
comment(0xAA0F, "Get stack pointer", inline=True)
comment(0xAA10, "Y=&DD: workspace result offset", inline=True)
comment(0xAA12, "Load result byte", inline=True)
comment(0xAA14, "Set bit 6 and bit 2", inline=True)
comment(0xAA16, "Always branch (NZ from ORA)", inline=True)

# Copy result back to caller's stack
comment(0xAA18, "Previous workspace byte", inline=True)
comment(0xAA19, "Previous stack position", inline=True)
comment(0xAA1A, "Load workspace byte", inline=True)
comment(0xAA1C, "Store to caller's stack frame", inline=True)
comment(0xAA1F, "Reached start of save area?", inline=True)
comment(0xAA21, "No: copy next byte", inline=True)
comment(0xAA23, "Return", inline=True)

# caa24: search claim code table
comment(0xAA24, "Compare A with code at index X", inline=True)
comment(0xAA27, "Match: return with Z set", inline=True)
comment(0xAA29, "Try next code", inline=True)
comment(0xAA2A, "More codes: continue search", inline=True)
comment(0xAA2C, "Return (Z clear = not found)", inline=True)

# init_ws_copy_wide: copy template to workspace (wide mode)
comment(0xAA6A, "X=&0D: 14 bytes to copy", inline=True)
comment(0xAA6C, "Y=&7C: workspace destination offset", inline=True)
comment(0xAA6E, "Test bit 6 via BIT (V flag check)", inline=True)
comment(0xAA71, "V=1: skip to wide mode copy", inline=True)

# init_ws_copy_narrow: copy template to workspace (narrow mode)
comment(0xAA73, "Y=&17: narrow mode dest offset", inline=True)
comment(0xAA75, "X=&1A: 27 bytes to copy", inline=True)
comment(0xAA77, "Clear V flag for narrow mode", inline=True)

# Template copy loop with special marker handling
comment(0xAA78, "Load template byte", inline=True)
comment(0xAA7B, "Is it &FE? (end marker)", inline=True)
comment(0xAA7D, "Yes: finished, set TX ptr", inline=True)
comment(0xAA7F, "Is it &FD? (skip marker)", inline=True)
comment(0xAA81, "Yes: skip store, just advance", inline=True)
comment(0xAA83, "Is it &FC? (page ptr marker)", inline=True)
comment(0xAA85, "No: use literal value", inline=True)
comment(0xAA87, "&FC: load RX buffer page", inline=True)
comment(0xAA89, "V=1: use net_rx_ptr_hi", inline=True)
comment(0xAA8B, "V=0: use nfs_workspace_hi", inline=True)
comment(0xAA8D, "Store as TX ptr high", inline=True)
comment(0xAA8F, "V=1: store to net_rx_ptr target", inline=True)
comment(0xAA91, "V=0: store to nfs_workspace", inline=True)
comment(0xAA93, "Continue to next byte", inline=True)
comment(0xAA95, "V=1: store to net_rx_ptr", inline=True)
comment(0xAA97, "Advance workspace offset down", inline=True)
comment(0xAA98, "Advance template index", inline=True)
comment(0xAA99, "More bytes: continue copy", inline=True)

# End: set TX pointer
comment(0xAA9B, "Adjust Y for start of TX data", inline=True)
comment(0xAA9C, "Set net_tx_ptr from Y", inline=True)
comment(0xAA9E, "Return", inline=True)
comment(0xAA9F, "Data: TXCB template (decoded as STA &00)", inline=True)
comment(0xAAA1, "Data: template continuation bytes", inline=True)

# reset_spool_buf_state: reset printer spool buffer
comment(0xAAD0, "Buffer start at &25", inline=True)
comment(0xAAD2, "Store as buffer pointer", inline=True)
comment(0xAAD5, "Control state &41", inline=True)
comment(0xAAD7, "Store as spool control state", inline=True)
comment(0xAADA, "Return", inline=True)

# Spool printer handler (&AADB)
comment(0xAADB, "Check Y == 4", inline=True)
comment(0xAADD, "No: return", inline=True)
comment(0xAADF, "A = X (control byte)", inline=True)
comment(0xAAE0, "Decrement X", inline=True)
comment(0xAAE1, "Non-zero: handle spool ctrl byte", inline=True)
comment(0xAAE3, "Get stack pointer", inline=True)
comment(0xAAE4, "OR with stack value", inline=True)
comment(0xAAE7, "Store back to stack", inline=True)

# Read printer buffer loop
comment(0xAAEA, "OSBYTE &91: read buffer", inline=True)
comment(0xAAEC, "X=3: printer buffer", inline=True)
comment(0xAAEE, "Read character from buffer", inline=True)
comment(0xAAF1, "C=1: buffer empty, return", inline=True)
comment(0xAAF3, "A = extracted character", inline=True)
comment(0xAAF4, "Add byte to RX buffer", inline=True)
comment(0xAAF7, "Buffer past &6E limit?", inline=True)
comment(0xAAF9, "No: read more from buffer", inline=True)
comment(0xAAFB, "Buffer full: send packet", inline=True)
comment(0xAAFE, "More room: continue reading", inline=True)

# append_byte_to_rxbuf: add byte to receive buffer
comment(0xAB00, "Load current buffer index", inline=True)
comment(0xAB03, "Store byte at buffer position", inline=True)
comment(0xAB05, "Advance buffer index", inline=True)
comment(0xAB08, "Return", inline=True)

# handle_spool_ctrl_byte: process spool control byte
comment(0xAB09, "Rotate bit 0 into carry", inline=True)
comment(0xAB0A, "Bit 0 clear: not active path", inline=True)
comment(0xAB0C, "Load spool control state", inline=True)
comment(0xAB0F, "Save for bit test", inline=True)
comment(0xAB10, "Rotate bit 0 into carry", inline=True)
comment(0xAB11, "Restore state", inline=True)
comment(0xAB12, "C=1: already started, reset", inline=True)
comment(0xAB14, "Set bits 0-1 (active + pending)", inline=True)
comment(0xAB16, "Store updated state", inline=True)
comment(0xAB19, "Control byte 3 for header", inline=True)
comment(0xAB1B, "Add to RX buffer", inline=True)
comment(0xAB1E, "Send current buffer", inline=True)
comment(0xAB21, "Reset spool buffer state", inline=True)

# cab24: prepare and send spool buffer packet
comment(0xAB24, "Y=8: workspace offset for length", inline=True)
comment(0xAB26, "Load buffer index (=length)", inline=True)
comment(0xAB29, "Store length to workspace", inline=True)
comment(0xAB2B, "Set data page high byte", inline=True)
comment(0xAB2E, "Store to workspace+9", inline=True)
comment(0xAB30, "Y=5: workspace offset", inline=True)
comment(0xAB32, "Store page to workspace+5", inline=True)
comment(0xAB34, "Y=&0B: template start offset", inline=True)
comment(0xAB36, "X=&26: template index", inline=True)
comment(0xAB38, "Copy template to workspace", inline=True)
comment(0xAB3B, "Adjust Y down", inline=True)
comment(0xAB3C, "Load spool control state", inline=True)
comment(0xAB3F, "Save state", inline=True)
comment(0xAB40, "Rotate to get carry (bit 7)", inline=True)
comment(0xAB41, "Restore state", inline=True)
comment(0xAB42, "Toggle bit 7", inline=True)
comment(0xAB44, "Store updated state", inline=True)
comment(0xAB47, "Shift to get both flag bits", inline=True)
comment(0xAB48, "Store flags to workspace", inline=True)
comment(0xAB4A, "Save l00d0 (exec flag)", inline=True)
comment(0xAB4C, "Push for later restore", inline=True)
comment(0xAB4D, "Clear bit 0 of exec flag", inline=True)
comment(0xAB4F, "Store modified exec flag", inline=True)
comment(0xAB51, "Reset buffer start to &25", inline=True)
comment(0xAB53, "Store reset buffer index", inline=True)
comment(0xAB56, "A=0 for disconnect reply", inline=True)
comment(0xAB58, "X=0", inline=True)
comment(0xAB59, "Y = workspace page", inline=True)
comment(0xAB5B, "Enable interrupts", inline=True)
comment(0xAB5C, "Send disconnect reply packet", inline=True)
comment(0xAB5F, "Restore exec flag", inline=True)
comment(0xAB60, "Store original exec flag", inline=True)
comment(0xAB62, "Return", inline=True)

# cab63: spool not-active path
comment(0xAB63, "Load spool control state", inline=True)
comment(0xAB66, "Rotate bit 0 to carry", inline=True)
comment(0xAB67, "C=0: send current buffer", inline=True)
comment(0xAB69, "Save exec flag", inline=True)
comment(0xAB6B, "Push for restore", inline=True)
comment(0xAB6C, "Clear bit 0", inline=True)
comment(0xAB6E, "Store modified flag", inline=True)
comment(0xAB70, "Control byte &14 (repeat count)", inline=True)

# cab72: transmit spool data with retry
comment(0xAB72, "Save retry count", inline=True)
comment(0xAB73, "X=&0B: 12 bytes of template", inline=True)
comment(0xAB75, "Y=&30: workspace offset for TXCB", inline=True)

# Copy TX template to workspace
comment(0xAB77, "Load template byte", inline=True)
comment(0xAB7A, "Store to workspace", inline=True)
comment(0xAB7C, "Next byte down", inline=True)
comment(0xAB7D, "Next template byte", inline=True)
comment(0xAB7E, "Loop for 12 bytes", inline=True)
comment(0xAB80, "X=-1: disable escape checking", inline=True)
comment(0xAB82, "Y=2: workspace offset for station", inline=True)
comment(0xAB84, "Load station number", inline=True)
comment(0xAB86, "Save station", inline=True)
comment(0xAB88, "Load network number", inline=True)
comment(0xAB8A, "Y=&28: TXCB dest network offset", inline=True)
comment(0xAB8C, "Store network to TXCB", inline=True)
comment(0xAB8E, "Y=&27", inline=True)
comment(0xAB8F, "Restore station", inline=True)
comment(0xAB90, "Store station to TXCB", inline=True)
comment(0xAB92, "X=&0B: 12 bytes of RX template", inline=True)
comment(0xAB94, "Y=&0B: workspace RX offset", inline=True)

# Copy RX palette template with marker substitution
comment(0xAB96, "Load RX template byte", inline=True)
comment(0xAB99, "Is it &FD? (skip marker)", inline=True)
comment(0xAB9B, "Yes: skip store", inline=True)
comment(0xAB9D, "Is it &FC? (page ptr marker)", inline=True)
comment(0xAB9F, "No: use literal value", inline=True)
comment(0xABA1, "&FC: substitute RX buffer page", inline=True)
comment(0xABA3, "Store to workspace", inline=True)
comment(0xABA5, "Next byte down", inline=True)
comment(0xABA6, "Next template byte", inline=True)
comment(0xABA7, "Loop for 12 bytes", inline=True)

# Set up pointers and send packet
comment(0xABA9, "TX data start at &25", inline=True)
comment(0xABAB, "Set net_tx_ptr low", inline=True)
comment(0xABAD, "Set data page high byte", inline=True)
comment(0xABAF, "Set net_tx_ptr high", inline=True)
comment(0xABB1, "Set up password in TX buffer", inline=True)
comment(0xABB4, "Send the packet", inline=True)
comment(0xABB7, "Clear net_tx_ptr low (page base)", inline=True)
comment(0xABB9, "Store zero", inline=True)
comment(0xABBB, "Set TX high to workspace page", inline=True)
comment(0xABBD, "Store workspace high byte", inline=True)
comment(0xABBF, "Wait for TX acknowledgement", inline=True)
comment(0xABC2, "Y=&31: check reply status", inline=True)
comment(0xABC4, "Load reply byte", inline=True)
comment(0xABC6, "Zero: success", inline=True)
comment(0xABC8, "Status = 3? (busy, can retry)", inline=True)
comment(0xABCA, "Other error: handle failure", inline=True)

# Success: clean up and return
comment(0xABCC, "Discard retry count", inline=True)
comment(0xABCD, "Discard saved exec flag", inline=True)
comment(0xABCE, "Restore l00d0", inline=True)
comment(0xABD0, "A=0: null terminator", inline=True)
comment(0xABD2, "Add zero to RX buffer (end marker)", inline=True)
comment(0xABD5, "Send final buffer", inline=True)
comment(0xABD8, "Load spool state", inline=True)
comment(0xABDB, "Clear low nibble", inline=True)
comment(0xABDD, "Store cleaned state", inline=True)
comment(0xABE0, "Return", inline=True)

# Error: retry or report
comment(0xABE1, "X = error code", inline=True)
comment(0xABE2, "Restore retry count", inline=True)
comment(0xABE3, "Set carry for subtract", inline=True)
comment(0xABE4, "Decrement retry count", inline=True)
comment(0xABE6, "Non-zero: retry send", inline=True)
comment(0xABE8, "Error code = 1? (busy)", inline=True)
comment(0xABEA, "No: printer jammed error", inline=True)
comment(0xABEC, "A=&A6: printer busy error number", inline=True)
comment(0xABEE, "Generate 'Printer busy' error", inline=True)
comment(0xABFE, "A=&A7: printer jammed error number", inline=True)
comment(0xAC00, "Generate 'Printer jammed' error", inline=True)

# send_disconnect_reply: send disconnect/status reply
comment(0xAC12, "Set TX ptr low byte", inline=True)
comment(0xAC14, "Set TX ptr high byte", inline=True)
comment(0xAC16, "Save disconnect code", inline=True)
comment(0xAC17, "Test if zero", inline=True)
comment(0xAC19, "Zero: skip station search", inline=True)
comment(0xAC1B, "X=&FF: start search from -1", inline=True)
comment(0xAC1D, "Y = disconnect code", inline=True)

# Search station table for matching station
comment(0xAC1E, "A = disconnect code", inline=True)
comment(0xAC1F, "Next station index", inline=True)
comment(0xAC20, "Compare with station table entry", inline=True)
comment(0xAC23, "Match: verify station/network", inline=True)
comment(0xAC25, "Past last station?", inline=True)
comment(0xAC27, "No: try next", inline=True)
comment(0xAC29, "Not found: A=0", inline=True)
comment(0xAC2B, "Skip to status update", inline=True)

# Verify matching station
comment(0xAC2D, "Y = disconnect code for compare", inline=True)
comment(0xAC2E, "Check station and network match", inline=True)
comment(0xAC31, "No match: try next station", inline=True)
comment(0xAC33, "Load station status flags", inline=True)
comment(0xAC36, "Isolate bit 0 (active flag)", inline=True)

# Update TX buffer and send status
comment(0xAC38, "Y=0: TX buffer status offset", inline=True)
comment(0xAC3A, "OR with existing status byte", inline=True)
comment(0xAC3C, "Save combined status", inline=True)
comment(0xAC3D, "Store to TX buffer", inline=True)
comment(0xAC3F, "Send the packet", inline=True)
comment(0xAC42, "Set end markers to &FF", inline=True)
comment(0xAC44, "Y=8: first end marker offset", inline=True)
comment(0xAC46, "Store &FF", inline=True)
comment(0xAC49, "Store &FF at offset 9 too", inline=True)
comment(0xAC4B, "Restore disconnect code", inline=True)
comment(0xAC4C, "X = status for control byte", inline=True)
comment(0xAC4D, "Y=&D1: default control", inline=True)
comment(0xAC4F, "Check original disconnect code", inline=True)
comment(0xAC50, "Peek but keep on stack", inline=True)
comment(0xAC51, "Zero: use &D1 control", inline=True)
comment(0xAC53, "Non-zero: use &90 control", inline=True)

# Store control byte and set up wait loop
comment(0xAC55, "A = control byte (Y)", inline=True)
comment(0xAC56, "Y=1: control byte offset", inline=True)
comment(0xAC58, "Store control byte", inline=True)
comment(0xAC5A, "A = X (status)", inline=True)
comment(0xAC5B, "Y=0", inline=True)
comment(0xAC5C, "Save status on stack", inline=True)

# Wait for acknowledgement with retry
comment(0xAC5D, "Set status to &7F (waiting)", inline=True)
comment(0xAC5F, "Store at TX buffer offset 0", inline=True)
comment(0xAC61, "Wait for TX acknowledgement", inline=True)
comment(0xAC64, "Restore status", inline=True)
comment(0xAC65, "Keep on stack for next check", inline=True)
comment(0xAC66, "Compare with current TX buffer", inline=True)
comment(0xAC68, "Rotate result bit 0 to carry", inline=True)
comment(0xAC69, "C=1: status changed, retry", inline=True)
comment(0xAC6B, "Done: discard status", inline=True)
comment(0xAC6C, "Discard disconnect code", inline=True)
comment(0xAC6D, "Return", inline=True)

# Palette read handler (&AC86)
comment(0xAC86, "Save l00ad counter", inline=True)
comment(0xAC88, "Push for later restore", inline=True)
comment(0xAC89, "Set workspace low to &E9", inline=True)
comment(0xAC8B, "Store to nfs_workspace low", inline=True)
comment(0xAC8D, "Y=0: initial palette index", inline=True)
comment(0xAC8F, "Clear palette counter", inline=True)
comment(0xAC91, "Load current screen mode", inline=True)
comment(0xAC94, "Store mode to workspace", inline=True)
comment(0xAC96, "Advance workspace ptr", inline=True)
comment(0xAC98, "Load video ULA copy", inline=True)
comment(0xAC9B, "Save for later restore", inline=True)
comment(0xAC9C, "A=0 for first palette entry", inline=True)

# Palette read loop
comment(0xAC9D, "Store logical colour to workspace", inline=True)
comment(0xAC9F, "X = workspace ptr low", inline=True)
comment(0xACA1, "Y = workspace ptr high", inline=True)
comment(0xACA3, "OSWORD &0B: read palette", inline=True)
comment(0xACA5, "Read palette entry", inline=True)
comment(0xACA8, "Restore previous ULA value", inline=True)
comment(0xACA9, "Y=0: reset index", inline=True)
comment(0xACAB, "Store ULA value to workspace", inline=True)
comment(0xACAD, "Y=1: physical colour offset", inline=True)
comment(0xACAE, "Load physical colour", inline=True)
comment(0xACB0, "Save for next iteration", inline=True)
comment(0xACB1, "X = workspace ptr", inline=True)
comment(0xACB3, "Advance workspace ptr", inline=True)
comment(0xACB5, "Advance palette counter", inline=True)
comment(0xACB7, "Y=0", inline=True)
comment(0xACB8, "Load counter", inline=True)
comment(0xACBA, "Reached &F9 workspace limit?", inline=True)
comment(0xACBC, "No: read next palette entry", inline=True)
comment(0xACBE, "Discard last ULA value", inline=True)
comment(0xACBF, "Clear counter", inline=True)
comment(0xACC1, "Advance workspace ptr", inline=True)
comment(0xACC3, "Store extra palette info", inline=True)
comment(0xACC6, "Advance workspace ptr again", inline=True)
comment(0xACC8, "Restore original l00ad", inline=True)
comment(0xACC9, "Store restored counter", inline=True)

# commit_state_byte: copy state to committed state
comment(0xACCB, "Load current state", inline=True)
comment(0xACCE, "Store as committed state", inline=True)
comment(0xACD1, "Return", inline=True)

# serialise_palette_entry
comment(0xACD2, "Load palette register value", inline=True)
comment(0xACD5, "Store to workspace", inline=True)
comment(0xACD7, "X = palette register", inline=True)
comment(0xACDA, "Read OSBYTE for this mode", inline=True)
comment(0xACDD, "Advance workspace ptr", inline=True)
comment(0xACDF, "A=0", inline=True)
comment(0xACE0, "Store zero to workspace", inline=True)
comment(0xACE2, "Read OSBYTE with X=0", inline=True)

# read_osbyte_to_ws_x0
comment(0xACE5, "X=0: read mode info", inline=True)

# read_osbyte_to_ws
comment(0xACE7, "Load OSBYTE code index", inline=True)
comment(0xACE9, "Advance index counter", inline=True)
comment(0xACEB, "Advance workspace ptr", inline=True)
comment(0xACED, "Load OSBYTE number from table", inline=True)
comment(0xACF0, "Y=&FF: read current value", inline=True)
comment(0xACF2, "Call OSBYTE to read value", inline=True)
comment(0xACF5, "A = result (from X)", inline=True)
comment(0xACF6, "X=0 for indexed store", inline=True)
comment(0xACF8, "Store result to workspace", inline=True)
comment(0xACFA, "Return", inline=True)

# cmd_dump (&BA06): *DUMP command — hex/ASCII file dump
# Buffer layout: 21 bytes on stack (page 1), pointed to by l00ae/l00af
#   buf[&00-&0F]: 16 data bytes read from file
#   buf[&10-&13]: 4-byte display address (little-endian)
#   buf[&14]:     flags/counter byte (high nibble for header control)
# osword_flag (&AA) reused as byte counter during dump loop (-1 to 15)

# Entry: open file and allocate stack buffer
comment(0xBA06, "Open file for reading, set ws_page", inline=True)
comment(0xBA09, "21 bytes to push (0-&14)", inline=True)
comment(0xBA0B, "Zero fill value", inline=True)
comment(0xBA0D, "Push zero onto stack", inline=True)
comment(0xBA0E, "Count down", inline=True)
comment(0xBA0F, "Loop until all 21 bytes pushed", inline=True)
comment(0xBA11, "X = stack pointer (buffer base - 1)", inline=True)
comment(0xBA12, "Set up buffer pointer and parse args", inline=True)

# Check start alignment and maybe print header
comment(0xBA15, "Load display address low byte", inline=True)
comment(0xBA17, "Test high nibble", inline=True)
comment(0xBA19, "Skip header if 16-byte aligned", inline=True)
comment(0xBA1B, "Print column header for offset start", inline=True)

# Main line loop: read up to 16 bytes per line
comment(0xBA1E, "Check for Escape key", inline=True)
comment(0xBA21, "Start byte counter at -1", inline=True)
comment(0xBA23, "Reset counter", inline=True)

# OSBGET read loop: fill buffer with up to 16 bytes
comment(0xBA2A, "C=1 from OSBGET: end of file", inline=True)
comment(0xBA2C, "Increment byte counter (0-15)", inline=True)
comment(0xBA2E, "Use counter as buffer index", inline=True)
comment(0xBA30, "Store byte in data buffer", inline=True)
comment(0xBA32, "Read 16 bytes? (index 0-15)", inline=True)
comment(0xBA34, "No: read next byte", inline=True)
comment(0xBA36, "C=0: not EOF, full line read", inline=True)

# EOF/empty check
comment(0xBA37, "Save C: EOF status", inline=True)
comment(0xBA38, "Check byte counter", inline=True)
comment(0xBA3A, "Counter >= 0: have data to display", inline=True)
comment(0xBA3C, "22 bytes to pop (21 buffer + PHP)", inline=True)

# Stack cleanup loop (shared by EOF-no-data and last-line)
comment(0xBA3E, "Pop one byte from stack", inline=True)
comment(0xBA3F, "Count down", inline=True)
comment(0xBA40, "Loop until stack cleaned up", inline=True)
comment(0xBA42, "Close file and return", inline=True)

# Check if header needed at 256-byte boundary
comment(0xBA45, "Point to display address low byte", inline=True)
comment(0xBA47, "Load display address low byte", inline=True)
comment(0xBA49, "Test high nibble", inline=True)
comment(0xBA4B, "Non-zero: header already current", inline=True)
comment(0xBA4D, "Crossed 256-byte boundary: new header", inline=True)

# Print 4-byte address big-endian
comment(0xBA50, "Start from highest address byte", inline=True)
comment(0xBA52, "Load address byte", inline=True)
comment(0xBA54, "Save for address increment later", inline=True)
comment(0xBA55, "Print as two hex digits", inline=True)
comment(0xBA58, "Restore address byte", inline=True)
comment(0xBA59, "Next byte down", inline=True)
comment(0xBA5A, "Printed all 4 address bytes?", inline=True)
comment(0xBA5C, "No: print next address byte", inline=True)

# Advance display address by 16 for next line
comment(0xBA5E, "Y=&10: point to address byte 0", inline=True)
comment(0xBA5F, "Prepare for 16-byte add", inline=True)
comment(0xBA60, "Add 16 to lowest address byte", inline=True)
comment(0xBA62, "Save carry for propagation", inline=True)

# 4-byte address increment loop (carry propagation)
comment(0xBA63, "Restore carry from previous byte", inline=True)
comment(0xBA64, "Store updated address byte", inline=True)
comment(0xBA66, "Next address byte up", inline=True)
comment(0xBA67, "Load next address byte", inline=True)
comment(0xBA69, "Add carry", inline=True)
comment(0xBA6B, "Save carry for next byte", inline=True)
comment(0xBA6C, "Past all 4 address bytes?", inline=True)
comment(0xBA6E, "No: continue propagation", inline=True)
comment(0xBA70, "Discard final carry", inline=True)
comment(0xBA71, "Print address/data separator", inline=True)

# Hex byte display: print each data byte as hex
comment(0xBA77, "Start from first data byte", inline=True)
comment(0xBA79, "X = bytes read (counter for display)", inline=True)
comment(0xBA7B, "Load data byte from buffer", inline=True)
comment(0xBA7D, "Print as two hex digits", inline=True)
comment(0xBA80, "Space separator", inline=True)
comment(0xBA82, "Print space between hex bytes", inline=True)

# Advance to next column position
comment(0xBA85, "Next column", inline=True)
comment(0xBA86, "All 16 columns done?", inline=True)
comment(0xBA88, "Yes: go to ASCII separator", inline=True)
comment(0xBA8A, "Decrement remaining data bytes", inline=True)
comment(0xBA8B, "More data: print next hex byte", inline=True)

# Pad missing hex columns with spaces
comment(0xBA8D, "Save column position", inline=True)
comment(0xBA8E, "Preserve Y across print", inline=True)
comment(0xBA8F, "Print 3-space padding", inline=True)
comment(0xBA95, "Inline string terminator (NOP)", inline=True)
comment(0xBA96, "Restore column position", inline=True)
comment(0xBA97, "Back to Y", inline=True)
comment(0xBA98, "Check next column", inline=True)

# ASCII section separator
comment(0xBA9B, "Adjust X for advance_x_by_8", inline=True)
comment(0xBA9C, "Print hex/ASCII separator", inline=True)
comment(0xBAA1, "Inline string terminator (NOP)", inline=True)
comment(0xBAA2, "X += 16: restore byte count for ASCII", inline=True)
comment(0xBAA5, "Start from first data byte", inline=True)

# ASCII display: print printable chars, '.' for others
comment(0xBAA7, "Load data byte", inline=True)
comment(0xBAA9, "Strip high bit", inline=True)
comment(0xBAAB, "Printable? (>= space)", inline=True)
comment(0xBAAD, "Yes: check for DEL", inline=True)
comment(0xBAAF, "Non-printable: substitute '.'", inline=True)
comment(0xBAB1, "Is it DEL (&7F)?", inline=True)
comment(0xBAB3, "Yes: substitute '.'", inline=True)
comment(0xBAB5, "Print ASCII character", inline=True)
comment(0xBAB8, "Next column", inline=True)
comment(0xBAB9, "All 16 columns done?", inline=True)
comment(0xBABB, "Yes: end of line", inline=True)
comment(0xBABD, "Decrement remaining data bytes", inline=True)
comment(0xBABE, "More data: print next ASCII char", inline=True)

# End of line: check for EOF
comment(0xBAC0, "Print newline", inline=True)
comment(0xBAC3, "Restore EOF status from &BA37", inline=True)
comment(0xBAC4, "C=1: EOF reached, clean up", inline=True)
comment(0xBAC6, "Not EOF: continue with next line", inline=True)

# EOF on last partial line: clean up stack
comment(0xBAC9, "21 bytes to pop (buffer only, PHP done)", inline=True)
comment(0xBACB, "Reuse stack cleanup loop", inline=True)

# print_dump_header: print column offset header
comment(0xBACE, "Load display address low byte", inline=True)
comment(0xBAD0, "Save as starting column number", inline=True)
comment(0xBAD1, "Print header label with leading CR", inline=True)
comment(0xBAE0, "Inline string terminator (NOP)", inline=True)
comment(0xBAE1, "Restore starting column number", inline=True)
comment(0xBAE2, "16 column headers to print", inline=True)

# Column header print loop
comment(0xBAE4, "Save current column number", inline=True)
comment(0xBAE5, "Print as two hex digits", inline=True)
comment(0xBAE8, "Space separator", inline=True)
comment(0xBAEA, "Print space after column number", inline=True)
comment(0xBAED, "Restore column number", inline=True)
comment(0xBAEE, "SEC for +1 via ADC", inline=True)
comment(0xBAEF, "Increment column number (SEC+ADC 0=+1)", inline=True)
comment(0xBAF1, "Wrap to low nibble (0-F)", inline=True)
comment(0xBAF3, "Count down", inline=True)
comment(0xBAF4, "Loop for all 16 columns", inline=True)
comment(0xBAF6, "Print trailer with ASCII label", inline=True)
comment(0xBB0A, "Inline string terminator (NOP)", inline=True)
comment(0xBB0B, "Return", inline=True)

# close_ws_file: close file handle stored in ws_page
comment(0xBB0C, "Y = file handle from ws_page", inline=True)
comment(0xBB0E, "A=0: close file", inline=True)
comment(0xBB10, "Close file and return", inline=True)

# open_file_for_read: open file, advance past filename
# On entry: Y = offset to filename start within command line
# On exit: ws_page = file handle, Y = offset past filename
comment(0xBB13, "Save processor flags", inline=True)
comment(0xBB14, "A = filename offset", inline=True)
comment(0xBB15, "Add to command text pointer", inline=True)
comment(0xBB16, "Low byte of filename address", inline=True)
comment(0xBB18, "Save on stack for later restore", inline=True)
comment(0xBB19, "X = filename address low", inline=True)
comment(0xBB1A, "Carry into high byte", inline=True)
comment(0xBB1C, "High byte of filename address", inline=True)
comment(0xBB1E, "Save on stack for later restore", inline=True)
comment(0xBB1F, "Y = filename address high", inline=True)
comment(0xBB20, "Open for input", inline=True)
comment(0xBB22, "OSFIND: open file", inline=True)
comment(0xBB26, "Store file handle", inline=True)
comment(0xBB28, "Non-zero: file opened OK", inline=True)
comment(0xBB2A, "Error number &D6", inline=True)
comment(0xBB2C, "Generate 'Not found' error", inline=True)

# Restore text pointer and skip past filename in command line
comment(0xBB39, "Restore saved text pointer high", inline=True)
comment(0xBB3A, "Restore os_text_ptr high byte", inline=True)
comment(0xBB3C, "Restore saved text pointer low", inline=True)
comment(0xBB3D, "Restore os_text_ptr low byte", inline=True)
comment(0xBB3F, "Start scanning from offset 0", inline=True)

# Scan past filename to find end (space or CR)
comment(0xBB41, "Advance past current char", inline=True)
comment(0xBB42, "Load next char from command line", inline=True)
comment(0xBB44, "CR: end of command line", inline=True)
comment(0xBB46, "Yes: done scanning", inline=True)
comment(0xBB48, "Space: end of filename", inline=True)
comment(0xBB4A, "No: keep scanning filename", inline=True)

# Skip trailing spaces after filename
comment(0xBB4C, "Advance past space", inline=True)
comment(0xBB4D, "Load next char", inline=True)
comment(0xBB4F, "Still a space?", inline=True)
comment(0xBB51, "Yes: skip it", inline=True)

# Return with Y pointing past filename/spaces
comment(0xBB53, "Restore processor flags", inline=True)
comment(0xBB54, "Return; Y = offset to next argument", inline=True)

# parse_dump_range: parse hex address from command line
# On entry: Y = offset into command line text
# On exit: buf[0-3] = parsed 32-bit address,
#   C=0 if valid address, C=1 if overflow
#   Y = offset past parsed text
comment(0xBB55, "Save command line offset to X", inline=True)
comment(0xBB56, "X tracks current position", inline=True)
comment(0xBB57, "Zero for clearing accumulator", inline=True)
comment(0xBB59, "Y=0 for buffer indexing", inline=True)

# Clear 4-byte accumulator in buffer
comment(0xBB5A, "Clear accumulator byte", inline=True)
comment(0xBB5C, "Next byte", inline=True)
comment(0xBB5D, "All 4 bytes cleared?", inline=True)
comment(0xBB5F, "No: clear next", inline=True)

# Main parse loop: get next character
comment(0xBB61, "Restore pre-increment offset to A", inline=True)
comment(0xBB62, "Advance X to next char position", inline=True)
comment(0xBB63, "Y = pre-increment offset for indexing", inline=True)
comment(0xBB64, "Load character from command line", inline=True)
comment(0xBB66, "CR: end of input", inline=True)
comment(0xBB68, "Done: skip trailing spaces", inline=True)
comment(0xBB6A, "Space: end of this parameter", inline=True)
comment(0xBB6C, "Done: skip trailing spaces", inline=True)

# Validate hex digit
comment(0xBB6E, "Below '0'?", inline=True)
comment(0xBB70, "Yes: not a hex digit, error", inline=True)
comment(0xBB72, "Below ':'? (i.e. '0'-'9')", inline=True)
comment(0xBB74, "Yes: is a decimal digit", inline=True)
comment(0xBB76, "Force uppercase for A-F", inline=True)
comment(0xBB78, "Map 'A'-'F' → &FA-&FF (C=0 here)", inline=True)
comment(0xBB7A, "Carry set: char > 'F', error", inline=True)
comment(0xBB7C, "Below &FA? (i.e. was < 'A')", inline=True)
comment(0xBB7E, "Yes: gap between '9' and 'A', error", inline=True)

# Extract low nibble as hex value
comment(0xBB80, "Mask to low nibble (0-15)", inline=True)
comment(0xBB82, "Save hex digit value", inline=True)
comment(0xBB83, "Save current offset", inline=True)
comment(0xBB84, "Preserve on stack", inline=True)
comment(0xBB85, "4 bits to shift in", inline=True)

# Shift 32-bit accumulator left by 4 (one nibble)
comment(0xBB87, "Start from byte 0 (LSB)", inline=True)
comment(0xBB89, "Clear A; C from PHA/PLP below", inline=True)

# Inner loop: rotate one bit through all 4 bytes
comment(0xBB8A, "Transfer carry bit to flags via stack", inline=True)
comment(0xBB8B, "PLP: C = bit shifted out of prev iter", inline=True)
comment(0xBB8C, "Load accumulator byte", inline=True)
comment(0xBB8E, "Rotate left through carry", inline=True)
comment(0xBB8F, "Store shifted byte", inline=True)
comment(0xBB91, "Save carry for next byte", inline=True)
comment(0xBB92, "Transfer to A for PHA/PLP trick", inline=True)
comment(0xBB93, "Next accumulator byte", inline=True)
comment(0xBB94, "All 4 bytes rotated?", inline=True)
comment(0xBB96, "No: rotate next byte", inline=True)

# Check for overflow after shift
comment(0xBB98, "Transfer carry to flags", inline=True)
comment(0xBB99, "C = overflow bit", inline=True)
comment(0xBB9A, "Overflow: address too large", inline=True)
comment(0xBB9C, "Count bits shifted", inline=True)
comment(0xBB9D, "4 bits shifted? No: shift again", inline=True)

# OR new nibble into accumulator byte 0
comment(0xBB9F, "Restore command line offset", inline=True)
comment(0xBBA0, "Back to X", inline=True)
comment(0xBBA1, "Restore hex digit value", inline=True)
comment(0xBBA2, "Point to LSB of accumulator", inline=True)
comment(0xBBA4, "OR digit into low nibble", inline=True)
comment(0xBBA6, "Store updated LSB", inline=True)
comment(0xBBA8, "Parse next character", inline=True)

# Overflow exit: address too large
comment(0xBBAB, "Discard saved offset", inline=True)
comment(0xBBAC, "Discard saved digit", inline=True)
comment(0xBBAD, "C=1: overflow", inline=True)
comment(0xBBAE, "Return with C=1", inline=True)

# Bad hex digit: close file and error
comment(0xBBAF, "Close open file before error", inline=True)
comment(0xBBB2, "Generate 'Bad hex' error", inline=True)

# Skip trailing spaces after parsed address
comment(0xBBB5, "Advance past space", inline=True)
comment(0xBBB6, "Load next char", inline=True)
comment(0xBBB8, "Space?", inline=True)
comment(0xBBBA, "Yes: skip it", inline=True)
comment(0xBBBC, "C=0: valid parse (no overflow)", inline=True)
comment(0xBBBD, "Return; Y past trailing spaces", inline=True)

# init_dump_buffer: set up buffer pointer and parse arguments
# On entry: X = stack pointer (buffer base - 1)
# Buffer becomes page 1 at address X+1
comment(0xBBBE, "X+1: first byte of buffer", inline=True)
comment(0xBBBF, "Set buffer pointer low byte", inline=True)
comment(0xBBC1, "Buffer is on stack in page 1", inline=True)
comment(0xBBC3, "Set buffer pointer high byte", inline=True)
comment(0xBBC5, "Parse start offset from command line", inline=True)
comment(0xBBC8, "Overflow: 'Outside file' error", inline=True)

# Save position, get file length for validation
comment(0xBBCA, "A = command line offset after parse", inline=True)
comment(0xBBCB, "Save for later (past start addr)", inline=True)
comment(0xBBD0, "A=2: read file extent (length)", inline=True)
comment(0xBBD5, "Check from MSB down", inline=True)

# Compare file length with start offset
comment(0xBBD7, "Load file length byte", inline=True)
comment(0xBBDA, "Compare with start offset byte", inline=True)
comment(0xBBDC, "Mismatch: check which is larger", inline=True)
comment(0xBBDE, "Next byte down", inline=True)
comment(0xBBDF, "More bytes to compare", inline=True)
comment(0xBBE1, "All equal: start = length, within file", inline=True)

# Handle length vs start comparison result
comment(0xBBE3, "Length < start: outside file", inline=True)
comment(0xBBE5, "Y=&FF: length > start, flag for later", inline=True)
comment(0xBBE7, "Continue to copy start address", inline=True)

# Outside file error
comment(0xBBE9, "Close file before error", inline=True)
comment(0xBBEC, "Error number &B7", inline=True)
comment(0xBBEE, "Generate 'Outside file' error", inline=True)

# Copy start offset to osword_flag as file pointer
comment(0xBBFE, "Load start address byte from buffer", inline=True)
comment(0xBC00, "Store to osword_flag (&AA-&AD)", inline=True)
comment(0xBC03, "Next byte", inline=True)
comment(0xBC04, "All 4 bytes copied?", inline=True)
comment(0xBC06, "No: copy next byte", inline=True)

# Set file pointer to start offset via OSARGS
comment(0xBC0C, "A=1: write file pointer", inline=True)
comment(0xBC0E, "OSARGS: set file pointer", inline=True)

# Restore command line position, check for end parameter
comment(0xBC11, "Restore saved command line offset", inline=True)
comment(0xBC12, "Back to Y for command line indexing", inline=True)
comment(0xBC13, "Load next char from command line", inline=True)
comment(0xBC15, "End of command? (CR)", inline=True)
comment(0xBC17, "No: parse display base address", inline=True)

# No explicit display base: use file's load address
comment(0xBC19, "Copy 2 bytes: os_text_ptr to buffer", inline=True)
comment(0xBC1B, "Load os_text_ptr byte", inline=True)
comment(0xBC1E, "Store as filename pointer in OSFILE CB", inline=True)
comment(0xBC20, "Next byte", inline=True)
comment(0xBC21, "Copy both low and high bytes", inline=True)

# OSFILE to read catalogue info (gets load address)
comment(0xBC23, "Read catalogue information", inline=True)
comment(0xBC25, "X = control block low", inline=True)
comment(0xBC27, "Y = control block high", inline=True)
comment(0xBC29, "OSFILE: read file info", inline=True)

# Copy load address from OSFILE +2..+5 down to buf[0-3]
comment(0xBC2C, "Start at OSFILE +2 (load addr byte 0)", inline=True)
comment(0xBC2E, "Load from OSFILE result offset", inline=True)
comment(0xBC30, "Y-2: destination is 2 bytes earlier", inline=True)
comment(0xBC31, "Continue decrement", inline=True)
comment(0xBC32, "Store to buf[Y-2]", inline=True)
comment(0xBC34, "Advance source index by 3", inline=True)
comment(0xBC35, "(net +1 per iteration)", inline=True)
comment(0xBC36, "Continue increment", inline=True)
comment(0xBC37, "Copied all 4 load address bytes?", inline=True)
comment(0xBC39, "No: copy next byte", inline=True)

# Check if load address is &FFFFFFFF (not set)
comment(0xBC3B, "Y=6 after loop exit", inline=True)
comment(0xBC3C, "Y=4: check from buf[4] downward", inline=True)
comment(0xBC3D, "Load address byte", inline=True)
comment(0xBC3F, "Is it &FF?", inline=True)
comment(0xBC41, "No: valid load address, use it", inline=True)
comment(0xBC43, "Check next byte down", inline=True)
comment(0xBC44, "More bytes to check", inline=True)

# All &FF: clear load address to 0 (default base)
comment(0xBC46, "Clear all 4 bytes", inline=True)
comment(0xBC48, "Zero value", inline=True)
comment(0xBC4A, "Clear byte", inline=True)
comment(0xBC4C, "Next byte down", inline=True)
comment(0xBC4D, "Loop for all 4 bytes", inline=True)
comment(0xBC4F, "Continue to compute display address", inline=True)

# Parse explicit display base address (second parameter)
comment(0xBC51, "Parse second hex parameter", inline=True)
comment(0xBC54, "Valid: use as display base", inline=True)
comment(0xBC56, "Invalid: close file before error", inline=True)
comment(0xBC59, "Error number &FC", inline=True)
comment(0xBC5B, "Generate 'Bad address' error", inline=True)

# Compute display start: display_addr = base + start_offset
comment(0xBC66, "Start from LSB", inline=True)
comment(0xBC68, "4 bytes to add", inline=True)
comment(0xBC6A, "Clear carry for addition", inline=True)
comment(0xBC6B, "Load display base byte", inline=True)
comment(0xBC6D, "Add start offset byte", inline=True)
comment(0xBC70, "Store result in osword_flag", inline=True)
comment(0xBC73, "Next byte", inline=True)
comment(0xBC74, "Count down", inline=True)
comment(0xBC75, "Loop for all 4 bytes", inline=True)

# Store display address into buf[&10-&13]
comment(0xBC77, "Point past end of address area", inline=True)
comment(0xBC79, "Start from MSB (byte 3)", inline=True)
comment(0xBC7B, "Pre-decrement Y", inline=True)
comment(0xBC7C, "Load computed display address byte", inline=True)
comment(0xBC7E, "Store to buf[&10-&13]", inline=True)
comment(0xBC80, "Next byte down", inline=True)
comment(0xBC81, "Loop for all 4 bytes", inline=True)
comment(0xBC83, "Return; Y=&10 (address low byte)", inline=True)

# advance_x_by_8/4/inx4: increment X by 8, 4, or 4
# Uses chained JSR/fall-through: advance_x_by_8 does 16 INXs
comment(0xBC84, "JSR+fall-through: 8+8=16 INXs total", inline=True)
comment(0xBC87, "JSR+fall-through: 4+4=8 INXs", inline=True)
comment(0xBC8A, "X += 1", inline=True)
comment(0xBC8B, "X += 2", inline=True)
comment(0xBC8C, "X += 3", inline=True)
comment(0xBC8D, "X += 4", inline=True)
comment(0xBC8E, "Return", inline=True)


# ============================================================
# cmd_wipe: *Wipe command + channel management utilities
# ============================================================

# Entry: parse filename, enumerate directory
comment(0xB33D, "Mask owner access flags to 5 bits", inline=True)
comment(0xB340, "Initialise file index to 0", inline=True)
comment(0xB342, "Store file counter", inline=True)
comment(0xB344, "Save pointer to command text", inline=True)
comment(0xB347, "Parse wildcard filename argument", inline=True)
comment(0xB34A, "Advance past CR terminator", inline=True)
comment(0xB34B, "Save end-of-argument buffer position", inline=True)

# Main examine loop: request next file from server
comment(0xB34D, "Command code 1 = examine directory", inline=True)
comment(0xB34F, "Store command in TX buffer byte 0", inline=True)
comment(0xB352, "Store flag in TX buffer byte 2", inline=True)
comment(0xB355, "Load current file index", inline=True)
comment(0xB357, "Store file index in TX buffer byte 1", inline=True)
comment(0xB35A, "X=3: copy from TX buffer offset 3", inline=True)
comment(0xB35C, "Copy filename argument to TX buffer", inline=True)
comment(0xB35F, "Function code 3 = examine", inline=True)
comment(0xB361, "Flag &80 = escapable", inline=True)
comment(0xB363, "Mark operation as escapable", inline=True)
comment(0xB365, "Send examine request to file server", inline=True)
comment(0xB368, "Get server response status", inline=True)
comment(0xB36B, "Non-zero: file found, process it", inline=True)

# No more files: flush keyboard buffers and return
comment(0xB36D, "OSBYTE &0F: flush buffer class", inline=True)
comment(0xB36F, "X=1: flush input buffers", inline=True)
comment(0xB371, "Flush keyboard buffer", inline=True)
comment(0xB374, "OSBYTE &7A: keyboard scan from 16", inline=True)
comment(0xB376, "Scan keyboard to clear state", inline=True)
comment(0xB379, "Y=0: no key pressed", inline=True)
comment(0xB37B, "OSBYTE &78: write keys pressed", inline=True)
comment(0xB37D, "Clear keyboard state and return", inline=True)

# Response processing: filter locked and directory entries
comment(0xB380, "Load first attribute char of response", inline=True)
comment(0xB383, "Is file locked?", inline=True)
comment(0xB385, "No: check if directory", inline=True)
comment(0xB387, "Skip locked file, advance index", inline=True)
comment(0xB389, "Request next file from server", inline=True)
comment(0xB38C, "Is it a directory entry?", inline=True)
comment(0xB38E, "No: regular file, show prompt", inline=True)
comment(0xB390, "Check directory contents flag", inline=True)
comment(0xB393, "Non-empty dir: treat as locked, skip", inline=True)

# Print filename and prompt user for Y/N/?
comment(0xB395, "X=1: start from response byte 1", inline=True)
comment(0xB397, "Y = destination index in delete buffer", inline=True)
comment(0xB399, "Load filename char from response", inline=True)
comment(0xB39C, "Print filename character to screen", inline=True)
comment(0xB39F, "Store in delete command buffer too", inline=True)
comment(0xB3A2, "Advance destination index", inline=True)
comment(0xB3A3, "Advance source index", inline=True)
comment(0xB3A4, "Copied all 11 filename characters?", inline=True)
comment(0xB3A6, "No: continue copying", inline=True)
comment(0xB3A8, "Print '(Y/N/?) ' prompt", inline=True)
comment(0xB3B3, "Inline string terminator (NOP)", inline=True)
comment(0xB3B4, "Read user response character", inline=True)
comment(0xB3B7, "User pressed '?'?", inline=True)
comment(0xB3B9, "No: check for Y/N response", inline=True)

# '?' handler: show full file info then re-prompt
comment(0xB3BB, "Carriage return before full info", inline=True)
comment(0xB3BD, "Print CR", inline=True)
comment(0xB3C0, "X=2: start from response byte 2", inline=True)
comment(0xB3C2, "Load file info character", inline=True)
comment(0xB3C5, "Print file info character", inline=True)
comment(0xB3C8, "Advance to next character", inline=True)
comment(0xB3C9, "Printed all &3C info bytes?", inline=True)
comment(0xB3CB, "No: continue printing", inline=True)
comment(0xB3CD, "Print ' (Y/N) ' prompt (no '?')", inline=True)
comment(0xB3D7, "Inline string terminator (NOP)", inline=True)
comment(0xB3D8, "Read user response (Y/N only)", inline=True)

# Check for 'Y' response: build and send delete command
comment(0xB3DB, "Force uppercase", inline=True)
comment(0xB3DD, "User said 'Y' (yes)?", inline=True)
comment(0xB3DF, "No: print newline, skip to next file", inline=True)
comment(0xB3E1, "Echo 'Y' to screen", inline=True)
comment(0xB3E4, "X=0: start of stored filename", inline=True)
comment(0xB3E6, "Check first byte of stored name", inline=True)
comment(0xB3E9, "Is first byte CR (empty first field)?", inline=True)
comment(0xB3EB, "Yes: use second filename field", inline=True)

# Build delete command from displayed filename
# Replace CR with '.', space terminates with CR
comment(0xB3ED, "Load byte from stored filename", inline=True)
comment(0xB3F0, "Is it CR (field separator)?", inline=True)
comment(0xB3F2, "No: check for space", inline=True)
comment(0xB3F4, "Replace CR with '.' directory sep", inline=True)
comment(0xB3F6, "Is it a space (name terminator)?", inline=True)
comment(0xB3F8, "No: keep character as-is", inline=True)
comment(0xB3FA, "Replace space with CR (end of name)", inline=True)
comment(0xB3FC, "Store in delete command TX buffer", inline=True)
comment(0xB3FF, "Advance to next character", inline=True)
comment(0xB400, "Was it the CR terminator?", inline=True)
comment(0xB402, "No: continue building delete command", inline=True)
comment(0xB404, "Function code &14 = delete file", inline=True)
comment(0xB406, "Send delete request to file server", inline=True)
comment(0xB409, "Adjust file index after deletion", inline=True)

# Not 'Y': newline and advance to next file
comment(0xB40B, "Print newline after user response", inline=True)
comment(0xB40E, "Advance index, process next file", inline=True)

# Second filename field: copy l0e31 to delete buffer
comment(0xB411, "DEX to offset following INX", inline=True)
comment(0xB412, "Advance to next byte", inline=True)
comment(0xB413, "Load byte from second field", inline=True)
comment(0xB416, "Store in delete command TX buffer", inline=True)
comment(0xB419, "Is it a space (field terminator)?", inline=True)
comment(0xB41B, "No: continue copying second field", inline=True)
comment(0xB41D, "Space found: terminate with CR", inline=True)

# flush_and_read_char: flush input, read one character
comment(0xB41F, "OSBYTE &0F: flush buffer class", inline=True)
comment(0xB421, "X=1: flush input buffers", inline=True)
comment(0xB423, "Flush keyboard buffer before read", inline=True)
comment(0xB426, "Read character from input stream", inline=True)
comment(0xB429, "C clear: character read OK", inline=True)
comment(0xB42B, "Escape pressed: raise error", inline=True)
comment(0xB42E, "Return with character in A", inline=True)

# init_channel_table: clear page &10 and set up channels
comment(0xB439, "A=0: clear value", inline=True)
comment(0xB43B, "Y=0: start index", inline=True)
comment(0xB43C, "Clear channel table entry", inline=True)
comment(0xB43F, "Next entry", inline=True)
comment(0xB440, "Loop until all 256 bytes cleared", inline=True)
comment(0xB442, "Offset &0F in receive buffer", inline=True)
comment(0xB444, "Get number of available channels", inline=True)
comment(0xB446, "Prepare subtraction", inline=True)
comment(0xB447, "Subtract 'Z' to get negative count", inline=True)
comment(0xB449, "Y = negative channel count (index)", inline=True)
comment(0xB44A, "Channel marker &40 (available)", inline=True)
comment(0xB44C, "Mark channel slot as available", inline=True)
comment(0xB44F, "Previous channel slot", inline=True)
comment(0xB450, "Reached start of channel range?", inline=True)
comment(0xB452, "No: continue marking channels", inline=True)
comment(0xB454, "Point to first channel slot", inline=True)
comment(0xB455, "Active channel marker &C0", inline=True)
comment(0xB457, "Mark first channel as active", inline=True)
comment(0xB45A, "Return", inline=True)

# attr_to_chan_index: convert attribute byte to channel index
comment(0xB45B, "Save flags", inline=True)
comment(0xB45C, "Prepare subtraction", inline=True)
comment(0xB45D, "Subtract &20 to get table index", inline=True)
comment(0xB45F, "Negative: out of valid range", inline=True)
comment(0xB461, "Above maximum channel index &0F?", inline=True)
comment(0xB463, "In range: valid index", inline=True)
comment(0xB465, "Out of range: return &FF (invalid)", inline=True)
comment(0xB467, "Restore flags", inline=True)
comment(0xB468, "X = channel index (or &FF)", inline=True)
comment(0xB469, "Return", inline=True)

# check_chan_char: validate channel character in A
comment(0xB46A, "Below space?", inline=True)
comment(0xB46C, "Yes: invalid channel character", inline=True)
comment(0xB46E, "Below '0'?", inline=True)
comment(0xB470, "In range &20-&2F: look up channel", inline=True)

# err_net_chan_invalid / err_net_chan_not_found
comment(0xB472, "Save channel character", inline=True)
comment(0xB473, "Error code &DE", inline=True)
comment(0xB475, "Generate 'Net channel' error", inline=True)
comment(0xB484, "Error string continuation (unreachable)", inline=True)

# lookup_chan_by_char: find channel by character
comment(0xB49D, "Save channel character", inline=True)
comment(0xB49E, "Prepare subtraction", inline=True)
comment(0xB49F, "Convert char to table index", inline=True)
comment(0xB4A1, "X = channel table index", inline=True)
comment(0xB4A2, "Look up network number for channel", inline=True)
comment(0xB4A5, "Zero: channel not found, raise error", inline=True)
comment(0xB4A7, "Check station/network matches current", inline=True)
comment(0xB4AA, "No match: build detailed error msg", inline=True)
comment(0xB4AC, "Discard saved channel character", inline=True)
comment(0xB4AD, "Load channel status flags", inline=True)
comment(0xB4B0, "Return; A = channel flags", inline=True)

# Build custom "Net channel N not on this file server" error
comment(0xB4B1, "Error code &DE", inline=True)
comment(0xB4B3, "Store error code in error block", inline=True)
comment(0xB4B6, "BRK opcode", inline=True)
comment(0xB4B8, "Store BRK at start of error block", inline=True)
comment(0xB4BB, "X=0: copy index", inline=True)
comment(0xB4BC, "Advance copy position", inline=True)
comment(0xB4BD, "Load 'Net channel' string byte", inline=True)
comment(0xB4C0, "Copy to error text", inline=True)
comment(0xB4C3, "Continue until NUL terminator", inline=True)
comment(0xB4C5, "Save end-of-string position", inline=True)
comment(0xB4C7, "Save for suffix append", inline=True)
comment(0xB4C9, "Retrieve channel character", inline=True)
comment(0xB4CA, "Append ' N' (channel number)", inline=True)
comment(0xB4CD, "Load 'Net channel' end position", inline=True)
comment(0xB4CF, "Skip past NUL to suffix string", inline=True)
comment(0xB4D0, "Advance destination position", inline=True)
comment(0xB4D1, "Load ' not on this...' suffix byte", inline=True)
comment(0xB4D4, "Append to error message", inline=True)
comment(0xB4D7, "Continue until NUL", inline=True)
comment(0xB4D9, "Raise the constructed error", inline=True)

# store_result_check_dir: store channel result, check not dir
comment(0xB4DC, "Load current channel attribute", inline=True)
comment(0xB4DF, "Offset &0E in receive buffer", inline=True)
comment(0xB4E1, "Store attribute in receive buffer", inline=True)

# check_not_dir: validate channel is not a directory
comment(0xB4E3, "Validate and look up channel", inline=True)
comment(0xB4E6, "Test directory flag (bit 1)", inline=True)
comment(0xB4E8, "Not a directory: return OK", inline=True)
comment(0xB4EA, "Error code &A8", inline=True)
comment(0xB4EC, "Generate 'Is a dir.' error", inline=True)
comment(0xB4F9, "Return", inline=True)

# alloc_fcb_slot: find free FCB slot in &20-&2F range
comment(0xB4FA, "Save channel attribute", inline=True)
comment(0xB4FB, "Start scanning from FCB slot &20", inline=True)
comment(0xB4FD, "Load FCB station byte", inline=True)
comment(0xB500, "Zero: slot is free, use it", inline=True)
comment(0xB502, "Try next slot", inline=True)
comment(0xB503, "Past last FCB slot &2F?", inline=True)
comment(0xB505, "No: check next slot", inline=True)
comment(0xB507, "No free slot: discard saved attribute", inline=True)
comment(0xB508, "A=0: return failure (Z set)", inline=True)
comment(0xB50A, "Return", inline=True)

# Free slot found: initialise FCB entry
comment(0xB50B, "Restore channel attribute", inline=True)
comment(0xB50C, "Store attribute in FCB slot", inline=True)
comment(0xB50F, "A=0: clear value", inline=True)
comment(0xB511, "Clear FCB transfer count low", inline=True)
comment(0xB514, "Clear FCB transfer count mid", inline=True)
comment(0xB517, "Clear FCB transfer count high", inline=True)
comment(0xB51A, "Load current station number", inline=True)
comment(0xB51D, "Store station in FCB", inline=True)
comment(0xB520, "Load current network number", inline=True)
comment(0xB523, "Store network in FCB", inline=True)
comment(0xB526, "Get FCB slot index", inline=True)
comment(0xB527, "Save slot index", inline=True)
comment(0xB528, "Prepare subtraction", inline=True)
comment(0xB529, "Convert slot to channel index (0-&0F)", inline=True)
comment(0xB52B, "X = channel index", inline=True)
comment(0xB52C, "Restore A = FCB slot index", inline=True)
comment(0xB52D, "Return; A=slot, X=channel, Z clear", inline=True)

# alloc_fcb_or_error: allocate FCB or raise error
comment(0xB52E, "Save argument", inline=True)
comment(0xB52F, "A=0: allocate any available slot", inline=True)
comment(0xB531, "Try to allocate an FCB slot", inline=True)
comment(0xB534, "Success: slot allocated", inline=True)
comment(0xB536, "Error code &C0", inline=True)
comment(0xB538, "Generate 'No more FCBs' error", inline=True)
comment(0xB548, "Restore argument", inline=True)
comment(0xB549, "Return", inline=True)

# close_all_net_chans: close channels for current station
comment(0xB54A, "C=0: close all matching channels", inline=True)
comment(0xB54B, "Branch always to scan entry", inline=True)
comment(0xB54D, "C=1: close with write-flush", inline=True)
comment(0xB54E, "Set V flag via BIT (alternate mode)", inline=True)

# scan_fcb_flags: iterate FCB slots with station matching
comment(0xB551, "Start from FCB slot &10", inline=True)
comment(0xB553, "Previous FCB slot", inline=True)
comment(0xB554, "More slots to check", inline=True)
comment(0xB556, "All FCB slots processed, return", inline=True)
comment(0xB557, "Load channel flags for this slot", inline=True)
comment(0xB55A, "Save flags in Y", inline=True)
comment(0xB55B, "Test active flag (bit 1)", inline=True)
comment(0xB55D, "Not active: check station match", inline=True)
comment(0xB55F, "V clear (close all): next slot", inline=True)
comment(0xB561, "C clear: check station match", inline=True)
comment(0xB563, "Restore original flags", inline=True)
comment(0xB564, "Clear write-pending flag (bit 5)", inline=True)
comment(0xB566, "Update channel flags", inline=True)
comment(0xB569, "Next slot (V always set here)", inline=True)
comment(0xB56B, "Check if channel belongs to station", inline=True)
comment(0xB56E, "No match: skip to next slot", inline=True)
comment(0xB570, "A=0: clear channel", inline=True)
comment(0xB572, "Clear channel flags (close it)", inline=True)
comment(0xB575, "Clear network number", inline=True)
comment(0xB578, "Continue to next slot", inline=True)

# match_station_net: check if FCB X matches current station
comment(0xB57A, "Load FCB station number", inline=True)
comment(0xB57D, "Compare with current station (EOR)", inline=True)
comment(0xB580, "Different: Z=0, no match", inline=True)
comment(0xB582, "Load FCB network number", inline=True)
comment(0xB585, "Compare with current network (EOR)", inline=True)
comment(0xB588, "Return; Z=1 if match, Z=0 if not", inline=True)

# find_open_fcb: find next available FCB slot
# Two-pass scan: first pass skips modified, second accepts
comment(0xB589, "Load current FCB index", inline=True)
comment(0xB58C, "Set V flag (first pass marker)", inline=True)
comment(0xB58F, "Next FCB slot", inline=True)
comment(0xB590, "Past end of table (&10)?", inline=True)
comment(0xB592, "No: continue checking", inline=True)
comment(0xB594, "Wrap around to slot 0", inline=True)
comment(0xB596, "Back to starting slot?", inline=True)
comment(0xB599, "No: check this slot", inline=True)
comment(0xB59B, "V clear (second pass): scan empties", inline=True)
comment(0xB59D, "Clear V for second pass", inline=True)
comment(0xB59E, "Continue scanning", inline=True)
comment(0xB5A0, "Load FCB status flags", inline=True)
comment(0xB5A3, "Shift bit 7 (in-use) into carry", inline=True)
comment(0xB5A4, "Not in use: skip", inline=True)
comment(0xB5A6, "Test bit 2 (modified flag)", inline=True)
comment(0xB5A8, "Modified: check further conditions", inline=True)

# Found unmodified in-use slot: mark and return
comment(0xB5AA, "Adjust for following INX", inline=True)
comment(0xB5AB, "Next FCB slot", inline=True)
comment(0xB5AC, "Past end of table?", inline=True)
comment(0xB5AE, "No: continue", inline=True)
comment(0xB5B0, "Wrap around to slot 0", inline=True)
comment(0xB5B2, "Load FCB status flags", inline=True)
comment(0xB5B5, "Shift bit 7 into carry", inline=True)
comment(0xB5B6, "Not in use: continue scanning", inline=True)
comment(0xB5B8, "Set carry for ROR restore", inline=True)
comment(0xB5B9, "Restore original flags", inline=True)
comment(0xB5BA, "Save flags back (mark as found)", inline=True)
comment(0xB5BD, "Restore original FCB index", inline=True)
comment(0xB5C0, "Return with found slot in X", inline=True)
comment(0xB5C1, "V set (first pass): skip modified", inline=True)
comment(0xB5C3, "Load FCB status flags", inline=True)
comment(0xB5C6, "Test bit 5 (offset pending)", inline=True)
comment(0xB5C8, "Bit 5 set: skip this slot", inline=True)
comment(0xB5CA, "Use this slot", inline=True)

# init_wipe_counters: reset all transfer counters
comment(0xB5CC, "Initial pass count = 1", inline=True)
comment(0xB5CE, "Store pass counter", inline=True)
comment(0xB5D1, "Y=0", inline=True)
comment(0xB5D2, "Clear byte counter low", inline=True)
comment(0xB5D5, "Clear offset counter", inline=True)
comment(0xB5D8, "Clear transfer flag", inline=True)
comment(0xB5DB, "A=0", inline=True)
comment(0xB5DC, "Clear 3 counter bytes", inline=True)
comment(0xB5DE, "Clear counter byte", inline=True)
comment(0xB5E1, "Next byte", inline=True)
comment(0xB5E2, "Loop for indices 2, 1, 0", inline=True)
comment(0xB5E4, "Store &FF as sentinel in l10cd", inline=True)
comment(0xB5E7, "Store &FF as sentinel in l10ce", inline=True)
comment(0xB5EA, "X=&CA: workspace offset", inline=True)
comment(0xB5EC, "Y=&10: page &10", inline=True)
comment(0xB5EE, "Return; X/Y point to &10CA", inline=True)

# start_wipe_pass: flush pending data for one FCB
comment(0xB5EF, "Verify workspace checksum integrity", inline=True)
comment(0xB5F2, "Save current FCB index", inline=True)
comment(0xB5F5, "Load FCB status flags", inline=True)
comment(0xB5F8, "Shift bit 0 (active) into carry", inline=True)
comment(0xB5F9, "Not active: clear status and return", inline=True)
comment(0xB5FB, "Save current station low to stack", inline=True)
comment(0xB5FE, "Push station low", inline=True)
comment(0xB5FF, "Save current station high", inline=True)
comment(0xB602, "Push station high", inline=True)
comment(0xB603, "Load FCB station low", inline=True)
comment(0xB606, "Set as working station low", inline=True)
comment(0xB609, "Load FCB station high", inline=True)
comment(0xB60C, "Set as working station high", inline=True)
comment(0xB60F, "Reset transfer counters", inline=True)
comment(0xB612, "Set offset to &FF (no data yet)", inline=True)
comment(0xB615, "Set pass counter to 0 (flush mode)", inline=True)
comment(0xB618, "Reload FCB index", inline=True)
comment(0xB61B, "Transfer to A", inline=True)
comment(0xB61C, "Prepare addition", inline=True)
comment(0xB61D, "Add &11 for buffer page offset", inline=True)
comment(0xB61F, "Store buffer address high byte", inline=True)
comment(0xB622, "Load FCB status flags", inline=True)
comment(0xB625, "Test bit 5 (has saved offset)", inline=True)
comment(0xB627, "No offset: skip restore", inline=True)
comment(0xB629, "Load saved byte offset", inline=True)
comment(0xB62C, "Restore offset counter", inline=True)
comment(0xB62F, "Load FCB attribute reference", inline=True)
comment(0xB632, "Store as current reference", inline=True)
comment(0xB635, "Transfer to X", inline=True)
comment(0xB636, "Offset &0E in receive buffer", inline=True)
comment(0xB638, "Save current receive attribute", inline=True)
comment(0xB63A, "Push to stack", inline=True)
comment(0xB63B, "Restore attribute to A", inline=True)
comment(0xB63C, "Set attribute in receive buffer", inline=True)
comment(0xB63E, "X=&CA: workspace offset", inline=True)
comment(0xB640, "Y=&10: page &10", inline=True)
comment(0xB642, "A=0: standard transfer mode", inline=True)
comment(0xB644, "Send data and receive response", inline=True)
comment(0xB647, "Reload FCB index", inline=True)
comment(0xB64A, "Restore saved receive attribute", inline=True)
comment(0xB64B, "Offset &0E", inline=True)
comment(0xB64D, "Restore receive attribute", inline=True)
comment(0xB64F, "Restore station high", inline=True)
comment(0xB650, "Store station high", inline=True)
comment(0xB653, "Restore station low", inline=True)
comment(0xB654, "Store station low", inline=True)

# Clear active/pending flags and return
comment(0xB657, "Mask &DC: clear bits 0, 1, 5", inline=True)
comment(0xB659, "Clear active and offset flags", inline=True)
comment(0xB65C, "Update FCB status", inline=True)
comment(0xB65F, "Return", inline=True)

# save_fcb_context: save TX buffer and workspace, process FCBs
comment(0xB660, "Copy 13 bytes (indices 0 to &0C)", inline=True)
comment(0xB662, "Load TX buffer byte", inline=True)
comment(0xB665, "Save to context buffer at &10D9", inline=True)
comment(0xB668, "Load workspace byte from fs_load_addr", inline=True)
comment(0xB66A, "Save to stack", inline=True)
comment(0xB66B, "Next byte down", inline=True)
comment(0xB66C, "Loop for all 13 bytes", inline=True)
comment(0xB66E, "Y=0? (no FCB to process)", inline=True)
comment(0xB670, "Non-zero: scan and process FCBs", inline=True)
comment(0xB672, "Y=0: skip to restore workspace", inline=True)

# Scan for pending FCBs (bits 7+6 set) and process them
comment(0xB675, "Save flags", inline=True)
comment(0xB676, "X=&FF: start scanning from -1", inline=True)
comment(0xB678, "Next FCB slot", inline=True)
comment(0xB679, "Load FCB status flags", inline=True)
comment(0xB67C, "Bit 7 clear: not pending, skip", inline=True)
comment(0xB67E, "Shift bit 6 to bit 7", inline=True)
comment(0xB67F, "Bit 6 clear: skip", inline=True)
comment(0xB681, "Flush this FCB's pending data", inline=True)
comment(0xB684, "Pending marker &40", inline=True)
comment(0xB686, "Mark FCB as pending-only", inline=True)
comment(0xB689, "Save flags", inline=True)
comment(0xB68A, "Find next available FCB slot", inline=True)
comment(0xB68D, "Restore flags", inline=True)
comment(0xB68E, "Load current channel attribute", inline=True)
comment(0xB691, "Store as current reference", inline=True)
comment(0xB694, "Save attribute", inline=True)
comment(0xB695, "Y = attribute index", inline=True)
comment(0xB696, "Load station for this attribute", inline=True)
comment(0xB699, "Store station in TX buffer", inline=True)
comment(0xB69C, "Restore attribute", inline=True)
comment(0xB69D, "Store attribute in FCB slot", inline=True)
comment(0xB6A0, "Load working station low", inline=True)
comment(0xB6A3, "Store in TX buffer", inline=True)
comment(0xB6A6, "Store station low in FCB", inline=True)
comment(0xB6A9, "Load working station high", inline=True)
comment(0xB6AC, "Store in TX buffer", inline=True)
comment(0xB6AF, "Store station high in FCB", inline=True)
comment(0xB6B2, "Get FCB slot index", inline=True)
comment(0xB6B3, "Prepare addition", inline=True)
comment(0xB6B4, "Add &11 for buffer page offset", inline=True)
comment(0xB6B6, "Store buffer address high byte", inline=True)
comment(0xB6B9, "Restore flags", inline=True)
comment(0xB6BA, "V clear: skip directory request", inline=True)

# Send directory listing request for FCB
comment(0xB6BC, "Command byte = 0", inline=True)
comment(0xB6BE, "Store in TX buffer", inline=True)
comment(0xB6C1, "X=1: flag byte", inline=True)
comment(0xB6C2, "Store in TX buffer", inline=True)
comment(0xB6C5, "Function code &0D", inline=True)
comment(0xB6C7, "X=5: copy 5 bytes to TX", inline=True)
comment(0xB6C9, "Send directory request to server", inline=True)

# Reset counters and send/receive data transfer
comment(0xB6CC, "Reset transfer counters", inline=True)
comment(0xB6CF, "Offset &0E", inline=True)
comment(0xB6D1, "Save current receive attribute", inline=True)
comment(0xB6D3, "Push to stack", inline=True)
comment(0xB6D4, "Load current reference", inline=True)
comment(0xB6D7, "Set in receive buffer", inline=True)
comment(0xB6D9, "Y=&10: page &10", inline=True)
comment(0xB6DB, "A=2: transfer mode 2", inline=True)
comment(0xB6DD, "Send and receive data", inline=True)
comment(0xB6E0, "Restore receive attribute", inline=True)
comment(0xB6E1, "Offset &0E", inline=True)
comment(0xB6E3, "Restore receive attribute", inline=True)
comment(0xB6E5, "Reload FCB index", inline=True)
comment(0xB6E8, "Load pass counter", inline=True)
comment(0xB6EB, "Non-zero: data received, calc offset", inline=True)
comment(0xB6ED, "Load offset counter", inline=True)
comment(0xB6F0, "Zero: no data received at all", inline=True)

# Calculate and store negated offset for buffer positioning
comment(0xB6F2, "Load offset counter", inline=True)
comment(0xB6F5, "Negate (ones complement)", inline=True)
comment(0xB6F7, "Clear carry for add", inline=True)
comment(0xB6F8, "Complete twos complement negation", inline=True)
comment(0xB6FA, "Store negated offset in FCB", inline=True)
comment(0xB6FD, "Set bit 5 (has saved offset)", inline=True)
comment(0xB6FF, "Add to FCB flags", inline=True)
comment(0xB702, "Update FCB status", inline=True)

# Clear buffer from offset to end of page
comment(0xB705, "Load buffer address high byte", inline=True)
comment(0xB708, "Set pointer high byte", inline=True)
comment(0xB70A, "A=0: pointer low byte and clear val", inline=True)
comment(0xB70C, "Set pointer low byte", inline=True)
comment(0xB70E, "Load negated offset (start of clear)", inline=True)
comment(0xB711, "Clear buffer byte", inline=True)
comment(0xB713, "Next byte", inline=True)
comment(0xB714, "Loop until page boundary", inline=True)

# Mark FCB as active and restore workspace
comment(0xB716, "Set bit 1 (active flag)", inline=True)
comment(0xB718, "Add active flag to status", inline=True)
comment(0xB71B, "Update FCB status", inline=True)
comment(0xB71E, "Y=0: start restoring workspace", inline=True)
comment(0xB720, "Restore workspace byte from stack", inline=True)
comment(0xB721, "Store to fs_load_addr workspace", inline=True)
comment(0xB724, "Next byte", inline=True)
comment(0xB725, "Restored all 13 bytes?", inline=True)
comment(0xB727, "No: continue restoring", inline=True)

# restore_catalog_entry: restore TX buffer from context
comment(0xB729, "Copy 13 bytes (indices 0 to &0C)", inline=True)
comment(0xB72B, "Load saved catalog byte from &10D9", inline=True)
comment(0xB72E, "Restore to TX buffer", inline=True)
comment(0xB731, "Next byte down", inline=True)
comment(0xB732, "Loop for all bytes", inline=True)
comment(0xB734, "Return", inline=True)

# find_matching_fcb: find FCB matching channel attribute
comment(0xB735, "Save current context first", inline=True)
comment(0xB738, "X=&FF: start scanning from -1", inline=True)
comment(0xB73A, "Load channel attribute to match", inline=True)
comment(0xB73D, "Next FCB slot", inline=True)
comment(0xB73E, "Past end of table (&10)?", inline=True)
comment(0xB740, "No: check this slot", inline=True)
comment(0xB742, "Load channel attribute", inline=True)
comment(0xB745, "Convert to channel index", inline=True)
comment(0xB748, "Load station for this channel", inline=True)
comment(0xB74B, "Store as match target station high", inline=True)
comment(0xB74E, "Load port for this channel", inline=True)
comment(0xB751, "Store as match target station low", inline=True)
comment(0xB754, "Save context and rescan from start", inline=True)
comment(0xB757, "Load FCB status flags", inline=True)
comment(0xB75A, "Test active flag (bit 1)", inline=True)
comment(0xB75C, "Not active: skip to next", inline=True)
comment(0xB75E, "Get attribute to match", inline=True)
comment(0xB75F, "Compare with FCB attribute ref", inline=True)
comment(0xB762, "No attribute match: skip", inline=True)
comment(0xB764, "Save matching FCB index", inline=True)
comment(0xB767, "Prepare subtraction", inline=True)
comment(0xB768, "Convert attribute to channel index", inline=True)
comment(0xB76A, "Y = channel index", inline=True)
comment(0xB76B, "Reload FCB index", inline=True)
comment(0xB76E, "Load channel station byte", inline=True)
comment(0xB771, "Compare with FCB station", inline=True)
comment(0xB774, "Station mismatch: try next", inline=True)
comment(0xB776, "Load channel network byte", inline=True)
comment(0xB779, "Compare with FCB network", inline=True)
comment(0xB77C, "Network mismatch: try next", inline=True)

# FCB matched: clear pending flag if set, check offset
comment(0xB77E, "Load FCB flags", inline=True)
comment(0xB781, "Bit 7 clear: no pending flush", inline=True)
comment(0xB783, "Clear pending flag (bit 7)", inline=True)
comment(0xB785, "Update FCB status", inline=True)
comment(0xB788, "Find new open FCB slot", inline=True)
comment(0xB78B, "Reload FCB flags", inline=True)
comment(0xB78E, "Test bit 5 (has offset data)", inline=True)
comment(0xB790, "Return; Z=1 no offset, Z=0 has data", inline=True)

# inc_fcb_byte_count: 3-byte increment
comment(0xB791, "Increment byte count low", inline=True)
comment(0xB794, "No overflow: done", inline=True)
comment(0xB796, "Increment byte count mid", inline=True)
comment(0xB799, "No overflow: done", inline=True)
comment(0xB79B, "Increment byte count high", inline=True)
comment(0xB79E, "Return", inline=True)

# process_all_fcbs: iterate all FCBs, flush matching ones
comment(0xB79F, "Save X", inline=True)
comment(0xB7A0, "Push X to stack", inline=True)
comment(0xB7A1, "Save Y", inline=True)
comment(0xB7A2, "Push Y to stack", inline=True)
comment(0xB7A3, "Save fs_options", inline=True)
comment(0xB7A5, "Push fs_options", inline=True)
comment(0xB7A6, "Save fs_block_offset", inline=True)
comment(0xB7A8, "Push fs_block_offset", inline=True)
comment(0xB7A9, "Start from FCB slot &0F", inline=True)
comment(0xB7AB, "Store as current FCB index", inline=True)
comment(0xB7AE, "Load current FCB index", inline=True)
comment(0xB7B1, "Get filter attribute", inline=True)
comment(0xB7B2, "Zero: process all FCBs", inline=True)
comment(0xB7B4, "Compare with FCB attribute ref", inline=True)
comment(0xB7B7, "No match: skip this FCB", inline=True)
comment(0xB7B9, "Save filter attribute", inline=True)
comment(0xB7BA, "Flush pending data for this FCB", inline=True)
comment(0xB7BD, "Restore filter", inline=True)
comment(0xB7BE, "Y = filter attribute", inline=True)
comment(0xB7BF, "Previous FCB index", inline=True)
comment(0xB7C2, "More slots: continue loop", inline=True)
comment(0xB7C4, "Restore fs_block_offset", inline=True)
comment(0xB7C5, "Store fs_block_offset", inline=True)
comment(0xB7C7, "Restore fs_options", inline=True)
comment(0xB7C8, "Store fs_options", inline=True)
comment(0xB7CA, "Restore Y", inline=True)
comment(0xB7CB, "Y restored", inline=True)
comment(0xB7CC, "Restore X", inline=True)
comment(0xB7CD, "X restored", inline=True)
comment(0xB7CE, "Return", inline=True)

# OSBGET handler: read byte from buffered file channel
comment(0xB7CF, "Save channel attribute", inline=True)
comment(0xB7D2, "Save caller's X", inline=True)
comment(0xB7D3, "Push X", inline=True)
comment(0xB7D4, "Store result and check not directory", inline=True)
comment(0xB7D7, "Load channel flags", inline=True)
comment(0xB7DA, "Test write-only flag (bit 5)", inline=True)
comment(0xB7DC, "Not write-only: proceed with read", inline=True)
comment(0xB7DE, "Error code &D4", inline=True)
comment(0xB7E0, "Generate 'Write only' error", inline=True)

# Find matching FCB and check for data in buffer
comment(0xB7EE, "Clear V (first-pass matching)", inline=True)
comment(0xB7EF, "Find FCB matching this channel", inline=True)
comment(0xB7F2, "No offset: read byte from buffer", inline=True)
comment(0xB7F4, "Load byte count for matching FCB", inline=True)
comment(0xB7F7, "Compare with buffer offset limit", inline=True)
comment(0xB7FA, "Below offset: data available", inline=True)
comment(0xB7FC, "Load channel flags for FCB", inline=True)
comment(0xB7FF, "Transfer to X for testing", inline=True)
comment(0xB800, "Test bit 6 (EOF already signalled)", inline=True)
comment(0xB802, "EOF already set: raise error", inline=True)
comment(0xB804, "Restore flags", inline=True)
comment(0xB805, "Set EOF flag (bit 6)", inline=True)
comment(0xB807, "Update channel flags with EOF", inline=True)
comment(0xB80A, "A=0: clear receive attribute", inline=True)
comment(0xB80C, "Offset &0E", inline=True)
comment(0xB80E, "Clear attribute in receive buffer", inline=True)
comment(0xB810, "Restore caller's X", inline=True)
comment(0xB811, "X restored", inline=True)
comment(0xB812, "A=&FE: EOF marker byte", inline=True)
comment(0xB814, "Restore channel attribute", inline=True)
comment(0xB817, "C=1: end of file", inline=True)
comment(0xB818, "Return", inline=True)

# End of file error (already signalled once)
comment(0xB819, "Error code &DF", inline=True)
comment(0xB81B, "Generate 'End of file' error", inline=True)

# Read byte from FCB buffer at current position
comment(0xB82A, "Load current byte count (= offset)", inline=True)
comment(0xB82D, "Save byte count", inline=True)
comment(0xB82E, "Get FCB slot index", inline=True)
comment(0xB82F, "X = FCB slot for byte count inc", inline=True)
comment(0xB830, "A=0: clear receive attribute", inline=True)
comment(0xB832, "Offset &0E", inline=True)
comment(0xB834, "Clear attribute in receive buffer", inline=True)
comment(0xB836, "Increment byte count for this FCB", inline=True)
comment(0xB839, "Restore byte count (= buffer offset)", inline=True)
comment(0xB83A, "Y = offset into data buffer", inline=True)
comment(0xB83B, "Load current FCB index", inline=True)
comment(0xB83E, "Prepare addition", inline=True)
comment(0xB83F, "Add &11 for buffer page offset", inline=True)
comment(0xB841, "Set pointer high byte", inline=True)
comment(0xB843, "A=0: pointer low byte", inline=True)
comment(0xB845, "Set pointer low byte", inline=True)
comment(0xB847, "Restore caller's X", inline=True)
comment(0xB848, "X restored", inline=True)
comment(0xB849, "Read data byte from buffer", inline=True)
comment(0xB84B, "Restore channel attribute", inline=True)
comment(0xB84E, "C=0: byte read successfully", inline=True)
comment(0xB84F, "Return; A = data byte", inline=True)

# OSBPUT handler: write byte to buffered file channel
comment(0xB850, "Save channel attribute", inline=True)
comment(0xB853, "Save data byte", inline=True)
comment(0xB854, "Y = data byte", inline=True)
comment(0xB855, "Save caller's X", inline=True)
comment(0xB856, "Push X", inline=True)
comment(0xB857, "Restore data byte to A", inline=True)
comment(0xB858, "Push data byte for later", inline=True)
comment(0xB859, "Save data byte in workspace", inline=True)
comment(0xB85C, "Store result and check not directory", inline=True)
comment(0xB85F, "Load channel flags", inline=True)
comment(0xB862, "Bit 7 set: channel open, proceed", inline=True)
comment(0xB865, "Misdecoded error path (equb data)", inline=True)

# Channel open for writing: check write mode
comment(0xB87D, "Test write flag (bit 5)", inline=True)
comment(0xB87F, "Not write-capable: use buffer path", inline=True)
comment(0xB881, "Load reply port for this channel", inline=True)
comment(0xB884, "Restore data byte", inline=True)
comment(0xB885, "Send byte directly to server", inline=True)
comment(0xB888, "Update byte count and return", inline=True)

# Buffer path: find matching FCB for buffered write
comment(0xB88B, "Set V flag (alternate match mode)", inline=True)
comment(0xB88E, "Find matching FCB for channel", inline=True)
comment(0xB891, "Load byte count for FCB", inline=True)
comment(0xB894, "Buffer full (&FF bytes)?", inline=True)
comment(0xB896, "No: store byte in buffer", inline=True)

# Buffer full: flush to server before storing new byte
comment(0xB898, "Save X", inline=True)
comment(0xB899, "Push X", inline=True)
comment(0xB89A, "Save Y (FCB slot)", inline=True)
comment(0xB89B, "Push Y", inline=True)
comment(0xB89C, "Load reply port for FCB", inline=True)
comment(0xB89F, "Save reply port", inline=True)
comment(0xB8A0, "Y=0: no nested context", inline=True)
comment(0xB8A2, "Save context and flush FCB data", inline=True)
comment(0xB8A5, "Restore reply port", inline=True)
comment(0xB8A6, "Store reply port in TX buffer", inline=True)
comment(0xB8A9, "X = reply port", inline=True)
comment(0xB8AA, "Restore Y (FCB slot)", inline=True)
comment(0xB8AB, "Y restored", inline=True)
comment(0xB8AC, "Save Y again for later restore", inline=True)
comment(0xB8AD, "A = reply port", inline=True)
comment(0xB8AE, "Save reply port for send", inline=True)
comment(0xB8AF, "Command byte = 0", inline=True)
comment(0xB8B1, "Store in TX buffer", inline=True)
comment(0xB8B4, "X=&FF: flag byte", inline=True)
comment(0xB8B5, "Store &FF in TX buffer", inline=True)
comment(0xB8B8, "Load station for FCB", inline=True)
comment(0xB8BB, "Store in TX buffer", inline=True)
comment(0xB8BE, "Load network for FCB", inline=True)
comment(0xB8C1, "Store in TX buffer", inline=True)
comment(0xB8C4, "Function code &0D", inline=True)
comment(0xB8C6, "X=5: copy 5 bytes to TX", inline=True)
comment(0xB8C8, "Send flush request to server", inline=True)
comment(0xB8CB, "Restore reply port", inline=True)
comment(0xB8CC, "Y = reply port", inline=True)
comment(0xB8CD, "Load saved data byte", inline=True)
comment(0xB8D0, "Send data byte to server", inline=True)
comment(0xB8D3, "Restore TX buffer from saved context", inline=True)
comment(0xB8D6, "Restore Y (FCB slot)", inline=True)
comment(0xB8D7, "Y restored", inline=True)
comment(0xB8D8, "Restore X", inline=True)
comment(0xB8D9, "X restored", inline=True)
comment(0xB8DA, "Reload byte count after flush", inline=True)

# Update buffer offset tracking after write
comment(0xB8DD, "Compare count with buffer offset", inline=True)
comment(0xB8E0, "Below offset: skip offset update", inline=True)
comment(0xB8E2, "Add carry (count + 1)", inline=True)
comment(0xB8E4, "Update buffer offset in FCB", inline=True)
comment(0xB8E7, "Non-zero: keep offset flag", inline=True)
comment(0xB8E9, "Mask &DF: clear bit 5", inline=True)
comment(0xB8EB, "Clear offset flag", inline=True)
comment(0xB8EE, "Update FCB status", inline=True)

# Mark FCB as active, store byte in buffer
comment(0xB8F1, "Set bit 0 (dirty/active)", inline=True)
comment(0xB8F3, "Add to FCB flags", inline=True)
comment(0xB8F6, "Update FCB status", inline=True)
comment(0xB8F9, "Load byte count (= write position)", inline=True)
comment(0xB8FC, "Save count", inline=True)
comment(0xB8FD, "Get FCB slot index", inline=True)
comment(0xB8FE, "X = FCB slot", inline=True)
comment(0xB8FF, "Restore byte count", inline=True)
comment(0xB900, "Y = buffer write offset", inline=True)
comment(0xB901, "Load current FCB index", inline=True)
comment(0xB904, "Prepare addition", inline=True)
comment(0xB905, "Add &11 for buffer page offset", inline=True)
comment(0xB907, "Set pointer high byte", inline=True)
comment(0xB909, "A=0: pointer low byte", inline=True)
comment(0xB90B, "Set pointer low byte", inline=True)
comment(0xB90D, "Restore data byte", inline=True)
comment(0xB90E, "Write data byte to buffer", inline=True)

# Common OSBPUT exit: increment count, restore, return
comment(0xB910, "Increment byte count for this FCB", inline=True)
comment(0xB913, "A=0: clear receive attribute", inline=True)
comment(0xB915, "Offset &0E", inline=True)
comment(0xB917, "Clear attribute in receive buffer", inline=True)
comment(0xB919, "Restore caller's X", inline=True)
comment(0xB91A, "X restored", inline=True)
comment(0xB91B, "Discard saved data byte", inline=True)
comment(0xB91C, "Restore channel attribute", inline=True)
comment(0xB91F, "Return", inline=True)

# send_wipe_request: send data byte to server via network
comment(0xB920, "Store reply port", inline=True)
comment(0xB923, "Store data byte", inline=True)
comment(0xB926, "Save Y", inline=True)
comment(0xB927, "Push Y to stack", inline=True)
comment(0xB928, "Save X", inline=True)
comment(0xB929, "Push X to stack", inline=True)
comment(0xB92A, "Function code &90", inline=True)
comment(0xB92C, "Store in send buffer", inline=True)
comment(0xB92F, "Initialise TX control block", inline=True)
comment(0xB932, "TX start address low = &DC", inline=True)
comment(0xB934, "Set TX start in control block", inline=True)
comment(0xB936, "TX end address low = &E0", inline=True)
comment(0xB938, "Set TX end in control block", inline=True)
comment(0xB93A, "Expected reply port = 9", inline=True)
comment(0xB93C, "Store reply port in buffer", inline=True)
comment(0xB93F, "TX control = &C0", inline=True)
comment(0xB941, "Y=0: no timeout", inline=True)
comment(0xB943, "Load reply port for addressing", inline=True)
comment(0xB946, "Send packet to server", inline=True)
comment(0xB949, "Load reply status", inline=True)
comment(0xB94C, "Zero: success", inline=True)

# Error response: copy error message and raise
comment(0xB94E, "Store error code", inline=True)
comment(0xB951, "X=0: copy index", inline=True)
comment(0xB953, "Load error message byte", inline=True)
comment(0xB956, "Copy to error block", inline=True)
comment(0xB959, "Is it CR (end of message)?", inline=True)
comment(0xB95B, "Yes: terminate string", inline=True)
comment(0xB95D, "Next byte", inline=True)
comment(0xB95E, "Continue copying error message", inline=True)
comment(0xB960, "NUL terminator", inline=True)
comment(0xB962, "Terminate error string in block", inline=True)
comment(0xB965, "Back up position for error check", inline=True)
comment(0xB966, "Process and raise network error", inline=True)

# Success: toggle station bit and return
comment(0xB969, "Load channel attribute index", inline=True)
comment(0xB96C, "Load station number for channel", inline=True)
comment(0xB96F, "Toggle bit 0 (alternate station)", inline=True)
comment(0xB971, "Update station number", inline=True)
comment(0xB974, "Restore X", inline=True)
comment(0xB975, "X restored", inline=True)
comment(0xB976, "Restore Y", inline=True)
comment(0xB977, "Y restored", inline=True)
comment(0xB978, "Return", inline=True)

# send_and_receive: set up options and transfer workspace
comment(0xB979, "Set up FS options pointer", inline=True)
comment(0xB97C, "Set up transfer workspace and return", inline=True)

# error_inline: generate BRK error from inline string (&96BE-&96D9)
comment(0x96C0, "Store return address low", inline=True)
comment(0x96C3, "Store return address high", inline=True)
comment(0x96C5, "X=0: error text index", inline=True)
comment(0x96CA, "Copy error number to A", inline=True)
comment(0x96CB, "Push error number on stack", inline=True)
comment(0x96CC, "Y=0: inline string index", inline=True)
comment(0x96D2, "Advance string index", inline=True)
comment(0x96D5, "Store byte in error block", inline=True)

# check_net_error_code: process network error response (&96DA-&9736)
comment(0x96DA, "Y=&0E: offset to error code in RX buffer", inline=True)
comment(0x96DC, "Load network error code from reply", inline=True)
comment(0x96DE, "Non-zero: network returned an error", inline=True)
comment(0x96E0, "Pop saved error number", inline=True)
comment(0x96E1, "Was it &DE (file server error)?", inline=True)
comment(0x96E3, "Yes: append error number and trigger BRK", inline=True)
comment(0x96E5, "Jump to BRK via error block", inline=True)
comment(0x96E8, "Store error code in workspace", inline=True)
comment(0x96EB, "Push error code", inline=True)
comment(0x96EC, "Save X (error text index)", inline=True)
comment(0x96ED, "Push X", inline=True)
comment(0x96EE, "Y=&0E: error code offset", inline=True)
comment(0x96F0, "Load error code from RX buffer", inline=True)
comment(0x96F2, "Save to fs_load_addr as spool handle", inline=True)
comment(0x96F4, "A=0: clear error code in RX buffer", inline=True)
comment(0x96F6, "Zero the error code byte in buffer", inline=True)
comment(0x96F8, "A=&C6: OSBYTE read spool handle", inline=True)
comment(0x96FA, "Read current spool file handle", inline=True)
comment(0x96FD, "Compare Y result with saved handle", inline=True)
comment(0x96FF, "Match: close the spool file", inline=True)
comment(0x9701, "Compare X result with saved handle", inline=True)
comment(0x9703, "No match: skip spool close", inline=True)
comment(0x9705, "Push A (preserved)", inline=True)
comment(0x9706, "A=&C6: disable spool with OSBYTE", inline=True)
comment(0x9708, "ALWAYS branch to close spool", inline=True)
comment(0x970A, "Push A (preserved)", inline=True)
comment(0x970B, "A=&C7: disable exec with OSBYTE", inline=True)
comment(0x970D, "OSBYTE with X=0, Y=0 to close", inline=True)
comment(0x9710, "Pull saved handle", inline=True)
comment(0x9711, "Transfer to Y for OSFIND", inline=True)
comment(0x9712, "A=0: close file", inline=True)
comment(0x9714, "Close the spool/exec file", inline=True)
comment(0x9717, "Pull saved X (error text index)", inline=True)
comment(0x9718, "Restore X", inline=True)
comment(0x9719, "Y=&0A: lookup index for 'on channel'", inline=True)
comment(0x971B, "Load message offset from lookup table", inline=True)
comment(0x971E, "Transfer offset to Y", inline=True)
comment(0x971F, "Load error message byte", inline=True)
comment(0x9722, "Append to error text buffer", inline=True)
comment(0x9725, "Null terminator: done copying", inline=True)
comment(0x9727, "Advance error text index", inline=True)
comment(0x9728, "Advance message index", inline=True)
comment(0x9729, "Loop until full message copied", inline=True)
comment(0x972B, "Save error text end position", inline=True)
comment(0x972D, "Pull saved error number", inline=True)
comment(0x972E, "Append ' nnn' error number suffix", inline=True)
comment(0x9731, "A=0: null terminator", inline=True)
comment(0x9733, "Terminate error text string", inline=True)
comment(0x9736, "ALWAYS branch to trigger BRK error", inline=True)

# append_drv_dot_num: append ' net.station' to error text (&9738-&975B)
comment(0x9738, "A=' ': space separator", inline=True)
comment(0x973A, "Append space to error text", inline=True)
comment(0x973D, "Advance error text index", inline=True)
comment(0x973E, "Save position for number formatting", inline=True)
comment(0x9740, "Y=3: offset to network number in TX CB", inline=True)
comment(0x9742, "Load network number", inline=True)
comment(0x9744, "Zero: skip network part (local)", inline=True)
comment(0x9746, "Append network number as decimal", inline=True)
comment(0x9749, "Reload error text position", inline=True)
comment(0x974B, "A='.': dot separator", inline=True)
comment(0x974D, "Append dot to error text", inline=True)
comment(0x9750, "Advance past dot", inline=True)
comment(0x9752, "Y=2: offset to station number in TX CB", inline=True)
comment(0x9754, "Load station number", inline=True)
comment(0x9756, "Append station number as decimal", inline=True)
comment(0x9759, "Reload error text position", inline=True)
comment(0x975B, "Return", inline=True)

# append_space_and_num: append ' nnn' to error text (&975C-&9797)
comment(0x975C, "Save number in Y", inline=True)
comment(0x975D, "A=' ': space prefix", inline=True)
comment(0x975F, "Load current error text position", inline=True)
comment(0x9761, "Append space to error text", inline=True)
comment(0x9764, "Advance position past space", inline=True)
comment(0x9766, "Restore number to A", inline=True)
comment(0x9767, "Save number in Y for division", inline=True)
comment(0x9768, "Set V: suppress leading zeros", inline=True)
comment(0x976B, "A=100: hundreds digit divisor", inline=True)
comment(0x976D, "Extract and append hundreds digit", inline=True)
comment(0x9770, "A=10: tens digit divisor", inline=True)
comment(0x9772, "Extract and append tens digit", inline=True)
comment(0x9775, "A=1: units digit (remainder)", inline=True)
comment(0x9777, "Clear V: always print units digit", inline=True)
comment(0x9778, "Store divisor", inline=True)
comment(0x977A, "Copy number to A for division", inline=True)
comment(0x977B, "X='0'-1: digit counter (ASCII offset)", inline=True)
comment(0x977D, "Save V flag (leading zero suppression)", inline=True)
comment(0x977E, "Set carry for subtraction", inline=True)
comment(0x977F, "Increment digit counter", inline=True)
comment(0x9780, "Subtract divisor", inline=True)
comment(0x9782, "Not negative yet: continue counting", inline=True)
comment(0x9784, "Add back divisor (restore remainder)", inline=True)
comment(0x9786, "Restore V flag", inline=True)
comment(0x9787, "Save remainder back to Y", inline=True)
comment(0x9788, "Digit counter to A (ASCII digit)", inline=True)
comment(0x9789, "Is digit '0'?", inline=True)
comment(0x978B, "Non-zero: always print", inline=True)
comment(0x978D, "V set (suppress leading zeros): skip", inline=True)
comment(0x978F, "Clear V: first non-zero digit seen", inline=True)
comment(0x9790, "Load current text position", inline=True)
comment(0x9792, "Store ASCII digit in error text", inline=True)
comment(0x9795, "Advance text position", inline=True)
comment(0x9797, "Return", inline=True)

# init_tx_ptr_and_send: init TX pointer and send packet (&9822-&982A)
comment(0x9822, "X=&C0: TX control block base (low)", inline=True)
comment(0x9824, "Set TX pointer low", inline=True)
comment(0x9826, "X=0: TX control block base (high)", inline=True)
comment(0x9828, "Set TX pointer high (page 0)", inline=True)

# send_net_packet: send network packet with retry (&982A-&9872)
comment(0x982A, "Load retry count from workspace", inline=True)
comment(0x982D, "Non-zero: use configured retry count", inline=True)
comment(0x982F, "A=&FF: default retry count (255)", inline=True)
comment(0x9831, "Y=&60: timeout value", inline=True)
comment(0x9833, "Push retry count", inline=True)
comment(0x9834, "A=&60: copy timeout to A", inline=True)
comment(0x9835, "Push timeout", inline=True)
comment(0x9836, "X=0: TX pointer index", inline=True)
comment(0x9838, "Load first byte of TX control block", inline=True)
comment(0x983A, "Write control byte back to CB", inline=True)
comment(0x983C, "Push control byte", inline=True)
comment(0x983D, "Poll ADLC until line idle", inline=True)
comment(0x9840, "Shift left: check bit 6 (success)", inline=True)
comment(0x9841, "Bit 6 clear: transmission complete", inline=True)
comment(0x9843, "Shift left: check bit 5 (fatal)", inline=True)
comment(0x9844, "Zero (bit 5 clear): fatal error", inline=True)
comment(0x9846, "Check for escape condition", inline=True)
comment(0x9849, "Pull control byte", inline=True)
comment(0x984A, "Restore to X", inline=True)
comment(0x984B, "Pull timeout", inline=True)
comment(0x984C, "Restore to Y", inline=True)
comment(0x984D, "Pull retry count", inline=True)
comment(0x984E, "Zero retries remaining: try alternate", inline=True)
comment(0x9850, "Decrement retry counter", inline=True)
comment(0x9852, "Push updated retry count", inline=True)
comment(0x9853, "Copy timeout to A", inline=True)
comment(0x9854, "Push timeout for delay loop", inline=True)
comment(0x9855, "Copy control byte to A", inline=True)
comment(0x9856, "Inner delay: decrement X", inline=True)
comment(0x9857, "Loop until X=0", inline=True)
comment(0x9859, "Decrement outer counter Y", inline=True)
comment(0x985A, "Loop until Y=0", inline=True)
comment(0x985C, "ALWAYS branch: retry transmission", inline=True)
comment(0x985E, "Compare retry count with alternate", inline=True)
comment(0x9861, "Different: go to error handling", inline=True)
comment(0x9863, "A=&80: set escapable flag", inline=True)
comment(0x9865, "Mark as escapable for second phase", inline=True)
comment(0x9867, "ALWAYS branch: retry with escapable", inline=True)
comment(0x9869, "Result code to X", inline=True)
comment(0x986A, "Jump to classify reply and return", inline=True)
comment(0x986D, "Pull control byte", inline=True)
comment(0x986E, "Pull timeout", inline=True)
comment(0x986F, "Pull retry count", inline=True)
comment(0x9870, "Clear escapable flag and return", inline=True)

# init_tx_ptr_for_pass: set up TX pointer for pass-through (&987F-&9886)
comment(0x987F, "Y=&C0: TX control block base (low)", inline=True)
comment(0x9881, "Set TX pointer low byte", inline=True)
comment(0x9883, "Y=0: TX control block base (high)", inline=True)
comment(0x9885, "Set TX pointer high byte", inline=True)

# setup_pass_txbuf: init TX buffer from template for pass-through (&9887-&98F2)
comment(0x9887, "Y=&0B: 12 bytes to process (0-11)", inline=True)
comment(0x9889, "Load template byte for this offset", inline=True)
comment(0x988C, "Is it &FD (skip marker)?", inline=True)
comment(0x988E, "Yes: skip this offset, don't modify", inline=True)
comment(0x9890, "Load existing TX buffer byte", inline=True)
comment(0x9892, "Save original value on stack", inline=True)
comment(0x9893, "Copy template value to A", inline=True)
comment(0x9894, "Store template value to TX buffer", inline=True)
comment(0x9896, "Next offset (descending)", inline=True)
comment(0x9897, "Loop until all 12 bytes processed", inline=True)
comment(0x9899, "Load pass-through control value", inline=True)
comment(0x989C, "Push control value", inline=True)
comment(0x989D, "A=&FF (Y is &FF after loop)", inline=True)
comment(0x989E, "Push &FF as timeout", inline=True)
comment(0x989F, "X=0: TX pointer index", inline=True)
comment(0x98A1, "Load control byte from TX CB", inline=True)
comment(0x98A3, "Write control byte to start TX", inline=True)
comment(0x98A5, "Save control byte on stack", inline=True)
comment(0x98A6, "Poll ADLC until line idle", inline=True)
comment(0x98A9, "Shift result: check bit 6 (success)", inline=True)
comment(0x98AA, "Bit 6 clear: transmission complete", inline=True)
comment(0x98AC, "Shift result: check bit 5 (fatal)", inline=True)
comment(0x98AD, "Non-zero (not fatal): retry", inline=True)
comment(0x98AF, "X=0: clear error status", inline=True)
comment(0x98B1, "Jump to fix up reply status", inline=True)

# c98b4: poll ADLC status register (&98B4-&98C8)
comment(0x98B4, "Shift ws_0d60 left to poll ADLC", inline=True)
comment(0x98B7, "Bit not set: keep polling", inline=True)
comment(0x98B9, "Copy TX pointer low to NMI TX block", inline=True)
comment(0x98BB, "Store in NMI TX block low", inline=True)
comment(0x98BD, "Copy TX pointer high", inline=True)
comment(0x98BF, "Store in NMI TX block high", inline=True)
comment(0x98C1, "Begin Econet frame transmission", inline=True)
comment(0x98C4, "Read TX status byte", inline=True)
comment(0x98C6, "Bit 7 set: still transmitting", inline=True)
comment(0x98C8, "Return with result in A", inline=True)

# c98c9: pass-through retry loop (&98C9-&98DC)
comment(0x98C9, "Pull control byte", inline=True)
comment(0x98CA, "Restore to X", inline=True)
comment(0x98CB, "Pull timeout", inline=True)
comment(0x98CC, "Restore to Y", inline=True)
comment(0x98CD, "Pull retry count", inline=True)
comment(0x98CE, "Zero retries: go to error handling", inline=True)
comment(0x98D0, "Decrement retry counter", inline=True)
comment(0x98D2, "Push updated retry count", inline=True)
comment(0x98D3, "Copy timeout to A", inline=True)
comment(0x98D4, "Push timeout", inline=True)
comment(0x98D5, "Copy control byte to A", inline=True)
comment(0x98D6, "Inner delay loop: decrement X", inline=True)
comment(0x98D7, "Loop until X=0", inline=True)
comment(0x98D9, "Decrement outer counter Y", inline=True)
comment(0x98DA, "Loop until Y=0", inline=True)
comment(0x98DC, "ALWAYS branch: retry transmission", inline=True)

# c98de: pass-through restore TX buffer (&98DE-&98F2)
comment(0x98DE, "Pull control byte (discard)", inline=True)
comment(0x98DF, "Pull timeout (discard)", inline=True)
comment(0x98E0, "Pull retry count (discard)", inline=True)
comment(0x98E1, "Y=0: start restoring from offset 0", inline=True)
comment(0x98E3, "Load template byte for this offset", inline=True)
comment(0x98E6, "Is it &FD (skip marker)?", inline=True)
comment(0x98E8, "Yes: don't restore this offset", inline=True)
comment(0x98EA, "Pull original value from stack", inline=True)
comment(0x98EB, "Restore original TX buffer byte", inline=True)
comment(0x98ED, "Next offset (ascending)", inline=True)
comment(0x98EE, "Processed all 12 bytes?", inline=True)
comment(0x98F0, "No: continue restoring", inline=True)
comment(0x98F2, "Return with TX buffer restored", inline=True)

# load_text_ptr_and_parse: load text pointer from FS options (&98F3-&9920)
comment(0x98F3, "Y=1: start at second byte of pointer", inline=True)
comment(0x98F5, "Load pointer byte from FS options", inline=True)
comment(0x98F7, "Store in OS text pointer", inline=True)
comment(0x98FA, "Decrement index", inline=True)
comment(0x98FB, "Loop until both bytes copied", inline=True)
comment(0x98FD, "Y=0: reset command line offset", inline=True)

# gsread_to_buf: read string using GSINIT/GSREAD into buffer (&98FF-&9920)
comment(0x98FF, "X=&FF: pre-increment for buffer index", inline=True)
comment(0x9901, "C=0: initialise for string input", inline=True)
comment(0x9902, "GSINIT: initialise string reading", inline=True)
comment(0x9905, "Z set (empty string): store terminator", inline=True)
comment(0x9907, "GSREAD: read next character", inline=True)
comment(0x990A, "C set: end of string reached", inline=True)
comment(0x990C, "Advance buffer index", inline=True)
comment(0x990D, "Store character in l0e30 buffer", inline=True)
comment(0x9910, "ALWAYS branch: read next character", inline=True)
comment(0x9912, "Advance past last character", inline=True)
comment(0x9913, "A=CR: terminate filename", inline=True)
comment(0x9915, "Store CR terminator in buffer", inline=True)
comment(0x9918, "A=&30: low byte of l0e30 buffer", inline=True)
comment(0x991A, "Set command text pointer low", inline=True)
comment(0x991C, "A=&0E: high byte of l0e30 buffer", inline=True)
comment(0x991E, "Set command text pointer high", inline=True)
comment(0x9920, "Return with buffer filled", inline=True)

# FS command iteration setup (&9921-&9981)
comment(0x9921, "Set up transfer parameters", inline=True)
comment(0x9924, "Load text pointer and parse filename", inline=True)
comment(0x9927, "Set owner-only access mask", inline=True)
comment(0x992A, "Parse access prefix from filename", inline=True)
comment(0x992D, "Load last byte flag", inline=True)
comment(0x992F, "Positive (not last): display file info", inline=True)
comment(0x9931, "Is it &FF (last entry)?", inline=True)
comment(0x9933, "Yes: copy arg and iterate", inline=True)
comment(0x9935, "Other value: return with flag", inline=True)
comment(0x9938, "Copy argument to buffer at X=0", inline=True)
comment(0x993B, "Y=2: enumerate directory command", inline=True)

# do_fs_cmd_iteration: send FS command and process response (&993D-&9981)
comment(0x993D, "A=&92: FS port number", inline=True)
comment(0x993F, "Set escapable flag to &92", inline=True)
comment(0x9941, "Store port number in TX buffer", inline=True)
comment(0x9944, "Send request to file server", inline=True)
comment(0x9947, "Y=6: offset to response cycle flag", inline=True)
comment(0x9949, "Load cycle flag from FS options", inline=True)
comment(0x994B, "Non-zero: already initialised", inline=True)
comment(0x994D, "Copy FS options to zero page first", inline=True)
comment(0x9950, "Then copy workspace to FS options", inline=True)
comment(0x9953, "Branch to continue (C clear from JSR)", inline=True)
comment(0x9955, "Copy workspace to FS options first", inline=True)
comment(0x9958, "Then copy FS options to zero page", inline=True)
comment(0x995B, "Y=4: loop counter", inline=True)
comment(0x995D, "Load address byte from zero page", inline=True)
comment(0x995F, "Save to TXCB end pointer", inline=True)
comment(0x9961, "Add offset from buffer", inline=True)
comment(0x9964, "Store sum in fs_work area", inline=True)
comment(0x9966, "Advance to next byte", inline=True)
comment(0x9967, "Decrement counter", inline=True)
comment(0x9968, "Loop for all 4 bytes", inline=True)
comment(0x996A, "Set carry for subtraction", inline=True)
comment(0x996B, "Subtract high offset", inline=True)
comment(0x996E, "Store result in fs_work_7", inline=True)
comment(0x9970, "Format filename for display", inline=True)
comment(0x9973, "Send TXCB and swap addresses", inline=True)
comment(0x9976, "X=2: copy 3 offset bytes", inline=True)
comment(0x9978, "Load offset byte from l0f10", inline=True)
comment(0x997B, "Store in l0f05 for next iteration", inline=True)
comment(0x997E, "Decrement counter", inline=True)
comment(0x997F, "Loop until all bytes copied", inline=True)
comment(0x9981, "Jump to receive and process reply", inline=True)

# send_txcb_swap_addrs: send TX block and swap start/end (&9984-&99AE)
comment(0x9984, "Compare 5-byte handle with current", inline=True)
comment(0x9987, "Match: no need to send, return", inline=True)
comment(0x9989, "A=&92: FS reply port number", inline=True)
comment(0x998B, "Set TXCB port", inline=True)
comment(0x998D, "X=3: copy 4 bytes", inline=True)
comment(0x998F, "Load TXCB end pointer byte", inline=True)
comment(0x9991, "Store in TXCB start pointer", inline=True)
comment(0x9993, "Load new end address from fs_work", inline=True)
comment(0x9995, "Store in TXCB end pointer", inline=True)
comment(0x9997, "Decrement counter", inline=True)
comment(0x9998, "Loop for all 4 bytes", inline=True)
comment(0x999A, "A=&7F: control byte for data transfer", inline=True)
comment(0x999C, "Set TXCB control byte", inline=True)
comment(0x999E, "Wait for network TX acknowledgement", inline=True)
comment(0x99A1, "Y=3: compare 4 bytes", inline=True)
comment(0x99A3, "Load TXCB end byte", inline=True)
comment(0x99A6, "Compare with expected end address", inline=True)
comment(0x99A9, "Mismatch: resend from start", inline=True)
comment(0x99AB, "Decrement counter", inline=True)
comment(0x99AC, "Loop until all 4 bytes match", inline=True)
comment(0x99AE, "Return (all bytes match)", inline=True)

# File info display and directory iteration (&99AF-&9A5D)
comment(0x99AF, "Z set: directory entry display", inline=True)
comment(0x99B1, "Non-zero: jump to OSWORD dispatch", inline=True)
comment(0x99B4, "X=4: loop counter for 4 iterations", inline=True)
comment(0x99B6, "Y=&0E: FS options offset for addresses", inline=True)
comment(0x99B8, "Set carry for subtraction", inline=True)
comment(0x99B9, "Load address byte from FS options", inline=True)
comment(0x99BB, "Save to workspace (port_ws_offset)", inline=True)
comment(0x99BE, "Y -= 4 to point to paired offset", inline=True)
comment(0x99C1, "Subtract paired value", inline=True)
comment(0x99C3, "Store difference in l0f03 buffer", inline=True)
comment(0x99C6, "Push difference", inline=True)
comment(0x99C7, "Load paired value from FS options", inline=True)
comment(0x99C9, "Save to workspace", inline=True)
comment(0x99CC, "Pull difference back", inline=True)
comment(0x99CD, "Store in FS options for display", inline=True)
comment(0x99CF, "Advance Y by 5 for next field", inline=True)
comment(0x99D2, "Decrement loop counter", inline=True)
comment(0x99D3, "Loop for all 4 address pairs", inline=True)
comment(0x99D5, "Y=9: copy 9 bytes of options data", inline=True)
comment(0x99D7, "Load FS options byte", inline=True)
comment(0x99D9, "Store in l0f03 buffer", inline=True)
comment(0x99DC, "Decrement index", inline=True)
comment(0x99DD, "Loop until all 9 bytes copied", inline=True)
comment(0x99DF, "A=&91: FS port for info request", inline=True)
comment(0x99E1, "Set escapable flag", inline=True)
comment(0x99E3, "Store port in TX buffer", inline=True)
comment(0x99E6, "Store in fs_error_ptr", inline=True)
comment(0x99E8, "X=&0B: copy argument at offset 11", inline=True)
comment(0x99EA, "Copy argument to TX buffer", inline=True)
comment(0x99ED, "Y=1: info sub-command", inline=True)
comment(0x99EF, "Load last byte flag", inline=True)
comment(0x99F1, "Is it 7 (catalogue info)?", inline=True)
comment(0x99F3, "Save comparison result", inline=True)
comment(0x99F4, "Not 7: keep Y=1", inline=True)
comment(0x99F6, "Y=&1D: extended info command", inline=True)
comment(0x99F8, "Send request to file server", inline=True)
comment(0x99FB, "Format filename for display", inline=True)
comment(0x99FE, "Restore comparison flags", inline=True)
comment(0x99FF, "Not catalogue info: show short format", inline=True)
comment(0x9A01, "X=0: start at first byte", inline=True)
comment(0x9A03, "ALWAYS branch to store and display", inline=True)
comment(0x9A05, "Load file handle from l0f05", inline=True)
comment(0x9A08, "Check and set up TXCB for transfer", inline=True)
comment(0x9A0B, "Receive and process reply", inline=True)
comment(0x9A0E, "Store result byte in l0f08", inline=True)
comment(0x9A11, "Y=&0E: protection bits offset", inline=True)
comment(0x9A13, "Load access byte from l0f05", inline=True)
comment(0x9A16, "Extract protection bit flags", inline=True)
comment(0x9A19, "Zero: use reply buffer data", inline=True)
comment(0x9A1B, "Load file info byte from l0ef7", inline=True)
comment(0x9A1E, "Store in FS options at offset Y", inline=True)
comment(0x9A20, "Advance to next byte", inline=True)
comment(0x9A21, "Y=&12: end of protection fields?", inline=True)
comment(0x9A23, "No: copy next byte", inline=True)
comment(0x9A25, "Load display flag from l0e06", inline=True)
comment(0x9A28, "Zero: skip display, return", inline=True)
comment(0x9A2A, "Y=0: filename character index", inline=True)
comment(0x9A2C, "Load filename character from l10f3", inline=True)
comment(0x9A2F, "Print character via OSASCI", inline=True)
comment(0x9A32, "Advance to next character", inline=True)
comment(0x9A33, "Printed all 12 characters?", inline=True)
comment(0x9A35, "No: print next character", inline=True)
comment(0x9A37, "Y=5: offset for access string", inline=True)
comment(0x9A39, "Print 5 hex bytes (access info)", inline=True)
comment(0x9A3C, "Print load and exec addresses", inline=True)
comment(0x9A3F, "Print newline", inline=True)
comment(0x9A42, "Jump to return with last flag", inline=True)

# print_load_exec_addrs: print load and exec addresses (&9A45-&9A4E)
comment(0x9A45, "Y=9: offset for exec address", inline=True)
comment(0x9A47, "Print 5 hex bytes (exec address)", inline=True)
comment(0x9A4A, "Y=&0C: offset for length (3 bytes)", inline=True)
comment(0x9A4C, "X=3: print 3 bytes only", inline=True)
comment(0x9A4E, "ALWAYS branch to print routine", inline=True)

# print_5_hex_bytes: print hex bytes from FS options (&9A50-&9A5D)
comment(0x9A50, "X=4: print 5 bytes (4 to 0)", inline=True)
comment(0x9A52, "Load byte from FS options at offset Y", inline=True)
comment(0x9A54, "Print as 2-digit hex", inline=True)
comment(0x9A57, "Decrement byte offset", inline=True)
comment(0x9A58, "Decrement byte count", inline=True)
comment(0x9A59, "Loop until all bytes printed", inline=True)
comment(0x9A5B, "A=' ': space separator", inline=True)
comment(0x9A5D, "Print space via OSASCI and return", inline=True)

# copy_fsopts_to_zp: copy FS options to zero page (&9A60-&9A71)
comment(0x9A60, "Y=5: copy 4 bytes (offsets 2-5)", inline=True)
comment(0x9A62, "Load byte from FS options", inline=True)
comment(0x9A64, "Store in zero page at l00ae+Y", inline=True)
comment(0x9A67, "Decrement index", inline=True)
comment(0x9A68, "Below offset 2?", inline=True)
comment(0x9A6A, "No: copy next byte", inline=True)
comment(0x9A6C, "Skip one (INY for skip_one_and_advance5)", inline=True)
comment(0x9A6D, "INY (advance_y_by_4 entry)", inline=True)
comment(0x9A6E, "INY", inline=True)
comment(0x9A6F, "INY", inline=True)
comment(0x9A70, "INY", inline=True)
comment(0x9A71, "Return", inline=True)

# copy_workspace_to_fsopts: copy workspace to FS options (&9A72-&9A83)
comment(0x9A72, "Y=&0D: copy bytes from offset &0D down", inline=True)
comment(0x9A74, "Transfer X to A", inline=True)
comment(0x9A75, "Store byte in FS options at offset Y", inline=True)
comment(0x9A77, "Load next workspace byte from l0f02+Y", inline=True)
comment(0x9A7A, "Decrement index", inline=True)
comment(0x9A7B, "Below offset 2?", inline=True)
comment(0x9A7D, "No: copy next byte", inline=True)
comment(0x9A7F, "DEY (retreat_y_by_4 entry)", inline=True)
comment(0x9A80, "DEY (retreat_y_by_3 entry)", inline=True)
comment(0x9A81, "DEY", inline=True)
comment(0x9A82, "DEY", inline=True)
comment(0x9A83, "Return", inline=True)

# c9a84: discard stacked value and return (&9A84-&9A87)
comment(0x9A84, "Discard stacked value", inline=True)
comment(0x9A85, "Restore Y from fs_block_offset", inline=True)
comment(0x9A87, "Return (handle already matches)", inline=True)

# check_and_setup_txcb: check handle and set up TX control block (&9A88-&9ADB)
comment(0x9A88, "Save port/sub-function on stack", inline=True)
comment(0x9A89, "Compare 5-byte handle with current", inline=True)
comment(0x9A8C, "Match: discard port and return", inline=True)
comment(0x9A8E, "X=0: loop start", inline=True)
comment(0x9A90, "Y=4: copy 4 bytes", inline=True)
comment(0x9A92, "Clear l0f08 (transfer size low)", inline=True)
comment(0x9A95, "Clear l0f09 (transfer size high)", inline=True)
comment(0x9A98, "Clear carry for addition", inline=True)
comment(0x9A99, "Load address byte from zero page", inline=True)
comment(0x9A9B, "Store in TXCB start pointer", inline=True)
comment(0x9A9D, "Add offset from l0f06", inline=True)
comment(0x9AA0, "Store sum in TXCB end pointer", inline=True)
comment(0x9AA2, "Also update load address", inline=True)
comment(0x9AA4, "Advance to next byte", inline=True)
comment(0x9AA5, "Decrement counter", inline=True)
comment(0x9AA6, "Loop for all 4 bytes", inline=True)
comment(0x9AA8, "Carry set: overflow, use limit", inline=True)
comment(0x9AAA, "Set carry for subtraction", inline=True)
comment(0x9AAB, "Load computed end address", inline=True)
comment(0x9AAE, "Subtract maximum from fs_work_4", inline=True)
comment(0x9AB1, "Advance to next byte", inline=True)
comment(0x9AB2, "Decrement counter", inline=True)
comment(0x9AB3, "Loop for all bytes", inline=True)
comment(0x9AB5, "Below limit: keep computed end", inline=True)
comment(0x9AB7, "X=3: copy 4 bytes of limit", inline=True)
comment(0x9AB9, "Load limit from fs_work_4", inline=True)
comment(0x9ABB, "Store as TXCB end", inline=True)
comment(0x9ABD, "Decrement counter", inline=True)
comment(0x9ABE, "Loop for all 4 bytes", inline=True)
comment(0x9AC0, "Pull port from stack", inline=True)
comment(0x9AC1, "Push back (keep for later)", inline=True)
comment(0x9AC2, "Save flags (carry = overflow state)", inline=True)
comment(0x9AC3, "Set TXCB port number", inline=True)
comment(0x9AC5, "A=&80: control byte for data request", inline=True)
comment(0x9AC7, "Set TXCB control byte", inline=True)
comment(0x9AC9, "Init TX pointer and send packet", inline=True)
comment(0x9ACC, "Load error pointer", inline=True)
comment(0x9ACE, "Init TXCB port from error pointer", inline=True)
comment(0x9AD1, "Restore overflow flags", inline=True)
comment(0x9AD2, "Carry set: discard and return", inline=True)
comment(0x9AD4, "A=&91: FS reply port", inline=True)
comment(0x9AD6, "Set TXCB port for reply", inline=True)
comment(0x9AD8, "Wait for TX acknowledgement", inline=True)
comment(0x9ADB, "Non-zero (not done): retry send", inline=True)

# c9add: OSWORD sub-operation dispatch (&9ADD-&9B85)
comment(0x9ADD, "Store sub-operation code", inline=True)
comment(0x9AE0, "Compare with 7", inline=True)
comment(0x9AE2, "Below 7: handle operations 1-6", inline=True)
comment(0x9AE4, "Above 7: jump to handle via finalise", inline=True)
comment(0x9AE6, "Equal to 7: jump to directory display", inline=True)
comment(0x9AE9, "Compare with 6", inline=True)
comment(0x9AEB, "6: delete file operation", inline=True)
comment(0x9AED, "Compare with 5", inline=True)
comment(0x9AEF, "5: read catalogue info", inline=True)
comment(0x9AF1, "Compare with 4", inline=True)
comment(0x9AF3, "4: write file attributes", inline=True)
comment(0x9AF5, "Compare with 1", inline=True)
comment(0x9AF7, "1: read file info", inline=True)
comment(0x9AF9, "Shift left twice: A*4", inline=True)
comment(0x9AFA, "A*4", inline=True)
comment(0x9AFB, "Copy to Y as index", inline=True)
comment(0x9AFC, "Y -= 3 to get FS options offset", inline=True)
comment(0x9AFF, "X=3: copy 4 bytes", inline=True)
comment(0x9B01, "Load byte from FS options at offset Y", inline=True)
comment(0x9B03, "Store in l0f06 buffer", inline=True)
comment(0x9B06, "Decrement source offset", inline=True)
comment(0x9B07, "Decrement byte count", inline=True)
comment(0x9B08, "Loop for all 4 bytes", inline=True)
comment(0x9B0A, "X=5: copy arg to buffer at offset 5", inline=True)
comment(0x9B0C, "ALWAYS branch to copy and send", inline=True)
comment(0x9B0E, "Get access bits for file", inline=True)
comment(0x9B11, "Store access byte in l0f0e", inline=True)
comment(0x9B14, "Y=9: source offset in FS options", inline=True)
comment(0x9B16, "X=8: copy 8 bytes to buffer", inline=True)
comment(0x9B18, "Load FS options byte", inline=True)
comment(0x9B1A, "Store in l0f05 buffer", inline=True)
comment(0x9B1D, "Decrement source offset", inline=True)
comment(0x9B1E, "Decrement byte count", inline=True)
comment(0x9B1F, "Loop for all 8 bytes", inline=True)
comment(0x9B21, "X=&0A: buffer offset for argument", inline=True)
comment(0x9B23, "Copy argument to buffer", inline=True)
comment(0x9B26, "Y=&13: OSWORD &13 (NFS operation)", inline=True)
comment(0x9B28, "ALWAYS branch to send request", inline=True)
comment(0x9B2A, "Copy argument to buffer at X=0", inline=True)
comment(0x9B2D, "Y=&14: delete file command", inline=True)
comment(0x9B2F, "Set V flag (no directory check)", inline=True)
comment(0x9B32, "Send request with V set", inline=True)
comment(0x9B35, "Carry set: error, jump to finalise", inline=True)
comment(0x9B37, "No error: return with last flag", inline=True)
comment(0x9B3A, "Get access bits for file", inline=True)
comment(0x9B3D, "Store in l0f06", inline=True)
comment(0x9B40, "X=2: buffer offset", inline=True)
comment(0x9B42, "ALWAYS branch to copy and send", inline=True)
comment(0x9B44, "X=1: buffer offset", inline=True)
comment(0x9B46, "Copy argument to buffer", inline=True)
comment(0x9B49, "Y=&12: open file command", inline=True)
comment(0x9B4B, "Send open file request", inline=True)
comment(0x9B4E, "Load reply handle from l0f11", inline=True)
comment(0x9B51, "Clear l0f11", inline=True)
comment(0x9B54, "Clear l0f14", inline=True)
comment(0x9B57, "Get protection bits", inline=True)
comment(0x9B5A, "Load file handle from l0f05", inline=True)
comment(0x9B5D, "Zero: file not found, return", inline=True)
comment(0x9B5F, "Y=&0E: store access bits", inline=True)
comment(0x9B61, "Store access byte in FS options", inline=True)
comment(0x9B63, "Y=&0D", inline=True)
comment(0x9B64, "X=&0C: copy 12 bytes of file info", inline=True)
comment(0x9B66, "Load reply byte from l0f05+X", inline=True)
comment(0x9B69, "Store in FS options at offset Y", inline=True)
comment(0x9B6B, "Decrement destination offset", inline=True)
comment(0x9B6C, "Decrement source counter", inline=True)
comment(0x9B6D, "Loop for all 12 bytes", inline=True)
comment(0x9B6F, "X=1 (INX from 0)", inline=True)
comment(0x9B70, "X=2", inline=True)
comment(0x9B71, "Y=&11: FS options offset", inline=True)
comment(0x9B73, "Load extended info byte from l0f12", inline=True)
comment(0x9B76, "Store in FS options", inline=True)
comment(0x9B78, "Decrement destination offset", inline=True)
comment(0x9B79, "Decrement source counter", inline=True)
comment(0x9B7A, "Loop until all copied", inline=True)
comment(0x9B7C, "Reload file handle", inline=True)
comment(0x9B7F, "Transfer to A", inline=True)
comment(0x9B80, "Jump to finalise and return", inline=True)

# format_filename_field: format filename for display (&9B86-&9BAE)
comment(0x9B86, "Y=0: destination index", inline=True)
comment(0x9B88, "Load source offset from l0f03", inline=True)
comment(0x9B8B, "Non-zero: copy from l0f05 buffer", inline=True)
comment(0x9B8D, "Load character from command line", inline=True)
comment(0x9B8F, "Below '!' (control/space)?", inline=True)
comment(0x9B91, "Yes: pad with spaces", inline=True)
comment(0x9B93, "Store printable character in l10f3", inline=True)
comment(0x9B96, "Advance to next character", inline=True)
comment(0x9B97, "Loop for more characters", inline=True)
comment(0x9B99, "A=' ': space for padding", inline=True)
comment(0x9B9B, "Store space in display buffer", inline=True)
comment(0x9B9E, "Advance index", inline=True)
comment(0x9B9F, "Filled all 12 characters?", inline=True)
comment(0x9BA1, "No: pad more spaces", inline=True)
comment(0x9BA3, "Return with field formatted", inline=True)
comment(0x9BA4, "Advance source and destination", inline=True)
comment(0x9BA5, "INY", inline=True)
comment(0x9BA6, "Load byte from l0f05 buffer", inline=True)
comment(0x9BA9, "Store in display buffer l10f3", inline=True)
comment(0x9BAC, "Bit 7 clear: more characters", inline=True)
comment(0x9BAE, "Return (bit 7 set = terminator)", inline=True)

# OSFIND dispatch: open/close file channels (&9BAF-&9CB8)
comment(0x9BAF, "Verify workspace checksum", inline=True)
comment(0x9BB2, "Store result as last byte flag", inline=True)
comment(0x9BB4, "Set FS options pointer", inline=True)
comment(0x9BB7, "OR with 0 to set flags", inline=True)
comment(0x9BB9, "Positive: handle sub-operations", inline=True)
comment(0x9BBB, "Shift left to check bit 6", inline=True)
comment(0x9BBC, "Zero (was &80): close channel", inline=True)
comment(0x9BBE, "Other: process all FCBs first", inline=True)
comment(0x9BC1, "Transfer Y to A", inline=True)
comment(0x9BC2, "Compare with &20 (space)", inline=True)
comment(0x9BC4, "Above &20: check further", inline=True)
comment(0x9BC6, "Below &20: invalid channel char", inline=True)
comment(0x9BC9, "Compare with '0'", inline=True)
comment(0x9BCB, "Above '0': invalid channel char", inline=True)
comment(0x9BCD, "Process all matching FCBs", inline=True)
comment(0x9BD0, "Transfer Y to A (FCB index)", inline=True)
comment(0x9BD1, "Push FCB index", inline=True)
comment(0x9BD2, "Copy to X", inline=True)
comment(0x9BD3, "Y=0: clear counter", inline=True)
comment(0x9BD5, "Clear last byte flag", inline=True)
comment(0x9BD7, "Clear block offset", inline=True)
comment(0x9BD9, "Load channel data from l1010+X", inline=True)
comment(0x9BDC, "Store in FS options at Y", inline=True)
comment(0x9BDE, "Advance X by 8 (next FCB field)", inline=True)
comment(0x9BE1, "Advance destination index", inline=True)
comment(0x9BE2, "Copied all 4 channel fields?", inline=True)
comment(0x9BE4, "No: copy next field", inline=True)
comment(0x9BE6, "Pull saved FCB index", inline=True)
comment(0x9BE7, "Restore to fs_block_offset", inline=True)
comment(0x9BE9, "Compare with 5", inline=True)
comment(0x9BEB, "5 or above: return with last flag", inline=True)
comment(0x9BED, "Compare Y with 0", inline=True)
comment(0x9BEF, "Non-zero: handle OSFIND with channel", inline=True)
comment(0x9BF1, "Y=0 (close): jump to OSFIND open", inline=True)
comment(0x9BF4, "Push sub-function", inline=True)
comment(0x9BF5, "Transfer X to A", inline=True)
comment(0x9BF6, "Push X (FCB slot)", inline=True)
comment(0x9BF7, "Transfer Y to A", inline=True)
comment(0x9BF8, "Push Y (channel char)", inline=True)
comment(0x9BF9, "Check file is not a directory", inline=True)
comment(0x9BFC, "Pull channel char", inline=True)
comment(0x9BFD, "Y=&0E: error code offset", inline=True)
comment(0x9BFF, "Store channel char in RX buffer", inline=True)
comment(0x9C01, "Load FCB flag byte from l1030", inline=True)
comment(0x9C04, "Store in l0f05", inline=True)
comment(0x9C07, "Pull X (FCB slot)", inline=True)
comment(0x9C08, "Restore X", inline=True)
comment(0x9C09, "Pull sub-function", inline=True)
comment(0x9C0A, "Shift right: check bit 0", inline=True)
comment(0x9C0B, "Zero (OSFIND close): handle close", inline=True)
comment(0x9C0D, "Save flags (carry from LSR)", inline=True)
comment(0x9C0E, "Push sub-function", inline=True)
comment(0x9C0F, "Load FS options pointer low", inline=True)
comment(0x9C11, "Load block offset", inline=True)
comment(0x9C13, "Process all matching FCBs", inline=True)
comment(0x9C16, "Load updated data from l1010", inline=True)
comment(0x9C19, "Store in l0f05", inline=True)
comment(0x9C1C, "Pull sub-function", inline=True)
comment(0x9C1D, "Store in l0f06", inline=True)
comment(0x9C20, "Restore flags", inline=True)
comment(0x9C21, "Transfer Y to A", inline=True)
comment(0x9C22, "Push Y (offset)", inline=True)
comment(0x9C23, "Carry clear: read operation", inline=True)
comment(0x9C25, "Y=3: copy 4 bytes", inline=True)
comment(0x9C27, "Load zero page data", inline=True)
comment(0x9C29, "Store in l0f07 buffer", inline=True)
comment(0x9C2C, "Decrement source", inline=True)
comment(0x9C2D, "Decrement counter", inline=True)
comment(0x9C2E, "Loop for all 4 bytes", inline=True)
comment(0x9C30, "Y=&0D: TX buffer size", inline=True)
comment(0x9C32, "X=5: argument offset", inline=True)
comment(0x9C34, "Send TX control block to server", inline=True)
comment(0x9C37, "Store X in last byte flag", inline=True)
comment(0x9C39, "Pull saved offset", inline=True)
comment(0x9C3A, "Set connection active flag", inline=True)
comment(0x9C3D, "Return with last flag", inline=True)
comment(0x9C40, "Y=&0C: TX buffer size (smaller)", inline=True)
comment(0x9C42, "X=2: argument offset", inline=True)
comment(0x9C44, "Send TX control block", inline=True)
comment(0x9C47, "Store A in last byte flag", inline=True)
comment(0x9C49, "Load FS options pointer low", inline=True)
comment(0x9C4B, "Y=2: zero page offset", inline=True)
comment(0x9C4D, "Store A in zero page", inline=True)
comment(0x9C4F, "Load buffer byte from l0f05+Y", inline=True)
comment(0x9C52, "Store in zero page at offset", inline=True)
comment(0x9C54, "Decrement source X", inline=True)
comment(0x9C55, "Decrement counter Y", inline=True)
comment(0x9C56, "Loop until all bytes copied", inline=True)
comment(0x9C58, "Pull saved offset", inline=True)
comment(0x9C59, "Return with last flag", inline=True)

# c9c5c: OSARGS read/write file pointer (&9C5C-&9CB8)
comment(0x9C5C, "Carry set: write file pointer", inline=True)
comment(0x9C5E, "Load block offset", inline=True)
comment(0x9C60, "Convert attribute to channel index", inline=True)
comment(0x9C63, "Load FS options pointer", inline=True)
comment(0x9C65, "Load FCB low byte from l1000", inline=True)
comment(0x9C68, "Store in zero page pointer low", inline=True)
comment(0x9C6B, "Load FCB high byte from l1010", inline=True)
comment(0x9C6E, "Store in zero page pointer high", inline=True)
comment(0x9C71, "Load FCB extent from l1020", inline=True)
comment(0x9C74, "Store in zero page work area", inline=True)
comment(0x9C77, "A=0: clear high byte", inline=True)
comment(0x9C79, "Store zero in work area high", inline=True)
comment(0x9C7C, "ALWAYS branch to return with flag", inline=True)
comment(0x9C7E, "Store write value in l0f06", inline=True)
comment(0x9C81, "Transfer X to A", inline=True)
comment(0x9C82, "Push X (zero page offset)", inline=True)
comment(0x9C83, "Y=3: copy 4 bytes", inline=True)
comment(0x9C85, "Load zero page data at offset", inline=True)
comment(0x9C87, "Store in l0f07 buffer", inline=True)
comment(0x9C8A, "Decrement source", inline=True)
comment(0x9C8B, "Decrement counter", inline=True)
comment(0x9C8C, "Loop for all 4 bytes", inline=True)
comment(0x9C8E, "Y=&0D: TX buffer size", inline=True)
comment(0x9C90, "X=5: argument offset", inline=True)
comment(0x9C92, "Send TX control block", inline=True)
comment(0x9C95, "Store X in last byte flag", inline=True)
comment(0x9C97, "Pull saved zero page offset", inline=True)
comment(0x9C98, "Transfer to Y", inline=True)
comment(0x9C99, "Load block offset (attribute)", inline=True)
comment(0x9C9B, "Clear connection active flag", inline=True)
comment(0x9C9E, "Convert attribute to channel index", inline=True)
comment(0x9CA1, "Load zero page pointer low", inline=True)
comment(0x9CA4, "Store back to FCB l1000", inline=True)
comment(0x9CA7, "Load zero page pointer high", inline=True)
comment(0x9CAA, "Store back to FCB l1010", inline=True)
comment(0x9CAD, "Load zero page work byte", inline=True)
comment(0x9CB0, "Store back to FCB l1020", inline=True)
comment(0x9CB3, "Return with last flag", inline=True)
comment(0x9CB6, "Process all matching FCBs first", inline=True)

# return_with_last_flag / finalise_and_return (&9CB9-&9CC7)
comment(0x9CB9, "Load last byte flag", inline=True)
comment(0x9CBB, "Push result on stack", inline=True)
comment(0x9CBC, "A=0: clear error flag", inline=True)
comment(0x9CBE, "Y=&0E: error code offset", inline=True)
comment(0x9CC0, "Clear error code in RX buffer", inline=True)
comment(0x9CC2, "Pull result back", inline=True)
comment(0x9CC3, "Restore X from FS options pointer", inline=True)
comment(0x9CC5, "Restore Y from block offset", inline=True)
comment(0x9CC7, "Return to caller", inline=True)

# c9cc8: OSFIND open file dispatch (&9CC8-&9D7D)
comment(0x9CC8, "Compare with 2 (open for output)", inline=True)
comment(0x9CCA, "2 or above: handle file open", inline=True)
comment(0x9CCC, "Transfer to Y (Y=0 or 1)", inline=True)
comment(0x9CCD, "Non-zero (1 = read pointer): copy data", inline=True)
comment(0x9CCF, "A=5: return code for close-all", inline=True)
comment(0x9CD1, "ALWAYS branch to finalise", inline=True)
comment(0x9CD3, "Load reply data byte at Y", inline=True)
comment(0x9CD6, "Store in FS options", inline=True)
comment(0x9CD8, "Decrement index", inline=True)
comment(0x9CD9, "Loop until all bytes copied", inline=True)
comment(0x9CDB, "Clear zero page work low", inline=True)
comment(0x9CDD, "Clear zero page work high", inline=True)
comment(0x9CDF, "Z set: jump to clear A and return", inline=True)
comment(0x9CE1, "A=0: clear result", inline=True)
comment(0x9CE3, "Shift right (always positive)", inline=True)
comment(0x9CE4, "Positive: jump to finalise", inline=True)
comment(0x9CE6, "Mask to 6-bit access value", inline=True)
comment(0x9CE8, "Non-zero: clear A and finalise", inline=True)
comment(0x9CEA, "Transfer X to A (options pointer)", inline=True)
comment(0x9CEB, "Allocate FCB slot or raise error", inline=True)
comment(0x9CEE, "Toggle bit 7", inline=True)
comment(0x9CF0, "Shift left: build open mode", inline=True)
comment(0x9CF1, "Store open mode in l0f05", inline=True)
comment(0x9CF4, "Rotate to complete mode byte", inline=True)
comment(0x9CF5, "Store in l0f06", inline=True)
comment(0x9CF8, "Parse command argument (Y=0)", inline=True)
comment(0x9CFB, "X=2: buffer offset", inline=True)
comment(0x9CFD, "Copy argument to TX buffer", inline=True)
comment(0x9D00, "Y=6: open file command", inline=True)
comment(0x9D02, "Set V flag (skip directory check)", inline=True)
comment(0x9D05, "Set carry", inline=True)
comment(0x9D06, "Rotate carry into escapable flag bit 7", inline=True)
comment(0x9D08, "Send open request with V set", inline=True)
comment(0x9D0B, "Carry set (error): jump to finalise", inline=True)
comment(0x9D0D, "A=&FF: mark as newly opened", inline=True)
comment(0x9D0F, "Y=&0E: error code offset", inline=True)
comment(0x9D11, "Store &FF as error flag in RX buffer", inline=True)
comment(0x9D13, "Load handle from l0f05", inline=True)
comment(0x9D16, "Push handle", inline=True)
comment(0x9D17, "A=4: file info sub-command", inline=True)
comment(0x9D19, "Store sub-command", inline=True)
comment(0x9D1C, "X=1: shift filename", inline=True)
comment(0x9D1E, "Load filename byte from l0f06+X", inline=True)
comment(0x9D21, "Shift down to l0f05+X", inline=True)
comment(0x9D24, "Advance source index", inline=True)
comment(0x9D25, "Is it CR (end of filename)?", inline=True)
comment(0x9D27, "No: continue shifting", inline=True)
comment(0x9D29, "Y=&12: file info request", inline=True)
comment(0x9D2B, "Send file info request", inline=True)
comment(0x9D2E, "Load last byte flag", inline=True)
comment(0x9D30, "Clear bit 6 (read/write bits)", inline=True)
comment(0x9D32, "OR with reply access byte", inline=True)
comment(0x9D35, "Set bit 0 (file is open)", inline=True)
comment(0x9D37, "Transfer to Y (access flags)", inline=True)
comment(0x9D38, "Check bit 1 (write access)", inline=True)
comment(0x9D3A, "No write access: check read-only", inline=True)
comment(0x9D3C, "Pull handle from stack", inline=True)
comment(0x9D3D, "Allocate FCB slot for channel", inline=True)
comment(0x9D40, "Non-zero: FCB allocated, store flags", inline=True)
comment(0x9D42, "Verify workspace checksum", inline=True)
comment(0x9D45, "Set up transfer parameters", inline=True)
comment(0x9D48, "Transfer A to X", inline=True)
comment(0x9D49, "Set owner-only access mask", inline=True)
comment(0x9D4C, "Transfer X back to A", inline=True)
comment(0x9D4D, "Zero: close file, process FCBs", inline=True)
comment(0x9D4F, "Save text pointer for OS", inline=True)
comment(0x9D52, "Load current directory handle", inline=True)
comment(0x9D55, "Zero: allocate new FCB", inline=True)
comment(0x9D57, "Transfer Y to A", inline=True)
comment(0x9D58, "X=0: clear directory handle", inline=True)
comment(0x9D5A, "Store zero (clear handle)", inline=True)
comment(0x9D5D, "ALWAYS branch to finalise", inline=True)
comment(0x9D5F, "Load access/open mode byte", inline=True)
comment(0x9D62, "Rotate right: check bit 0", inline=True)
comment(0x9D63, "Carry set (bit 0): check read permission", inline=True)
comment(0x9D65, "Rotate right: check bit 1", inline=True)
comment(0x9D66, "Carry clear (no write): skip", inline=True)
comment(0x9D68, "Test bit 7 of l0f07 (lock flag)", inline=True)
comment(0x9D6B, "Not locked: skip", inline=True)
comment(0x9D6D, "Transfer Y to A (flags)", inline=True)
comment(0x9D6E, "Set bit 5 (locked file flag)", inline=True)
comment(0x9D70, "Transfer back to Y", inline=True)
comment(0x9D71, "Pull handle from stack", inline=True)
comment(0x9D72, "Allocate FCB slot for channel", inline=True)
comment(0x9D75, "Transfer to X", inline=True)
comment(0x9D76, "Transfer Y to A (flags)", inline=True)
comment(0x9D77, "Store flags in FCB table l1040", inline=True)
comment(0x9D7A, "Transfer X back to A (handle)", inline=True)
comment(0x9D7B, "Jump to finalise and return", inline=True)

# c9d7e: close file and handle spool/exec (&9D7E-&9DBB)
comment(0x9D7E, "Process all matching FCBs", inline=True)
comment(0x9D81, "Transfer Y to A", inline=True)
comment(0x9D82, "Non-zero channel: close specific", inline=True)
comment(0x9D84, "Load FS options pointer low", inline=True)
comment(0x9D86, "Push (save for restore)", inline=True)
comment(0x9D87, "A=&77: OSBYTE close spool/exec files", inline=True)
comment(0x9D89, "Close any *SPOOL and *EXEC files", inline=True)
comment(0x9D8C, "Pull saved options pointer", inline=True)
comment(0x9D8D, "Restore FS options pointer", inline=True)
comment(0x9D8F, "A=0: clear flags", inline=True)
comment(0x9D91, "Clear last byte flag", inline=True)
comment(0x9D93, "Clear block offset", inline=True)
comment(0x9D95, "ALWAYS branch to send close request", inline=True)
comment(0x9D97, "Validate channel character", inline=True)
comment(0x9D9A, "Load FCB flag byte from l1030", inline=True)
comment(0x9D9D, "Store as l0f05 (file handle)", inline=True)
comment(0x9DA0, "X=1: argument size", inline=True)
comment(0x9DA2, "Y=7: close file command", inline=True)
comment(0x9DA4, "Send close file request", inline=True)
comment(0x9DA7, "Load block offset", inline=True)
comment(0x9DA9, "Non-zero: clear single FCB", inline=True)
comment(0x9DAB, "Clear V flag", inline=True)
comment(0x9DAC, "Scan and clear all FCB flags", inline=True)
comment(0x9DAF, "Return with last flag", inline=True)
comment(0x9DB2, "A=0: clear FCB entry", inline=True)
comment(0x9DB4, "Clear l1010 (FCB high byte)", inline=True)
comment(0x9DB7, "Clear l1040 (FCB flags)", inline=True)
comment(0x9DBA, "ALWAYS branch to return", inline=True)

# OSARGS dispatch: read/write file arguments (&9DBC-&9E02)
comment(0x9DBC, "Z set: handle OSARGS 0", inline=True)
comment(0x9DBE, "Compare X with 4 (number of args)", inline=True)
comment(0x9DC0, "Not 4: check for error", inline=True)
comment(0x9DC2, "Compare Y with 4", inline=True)
comment(0x9DC4, "Below 4: handle special OSARGS", inline=True)
comment(0x9DC6, "Decrement X", inline=True)
comment(0x9DC7, "X was 1: store display flag", inline=True)
comment(0x9DC9, "Store Y in display control flag l0e06", inline=True)
comment(0x9DCC, "Carry clear: return with flag", inline=True)
comment(0x9DCE, "A=7: error code", inline=True)
comment(0x9DD0, "Jump to classify reply error", inline=True)
comment(0x9DD3, "Store Y in l0f05", inline=True)
comment(0x9DD6, "Y=&16: OSARGS save command", inline=True)
comment(0x9DD8, "Send OSARGS request", inline=True)
comment(0x9DDB, "Reload block offset", inline=True)
comment(0x9DDD, "Store in l0e05", inline=True)
comment(0x9DE0, "Positive: return with flag", inline=True)
comment(0x9DE2, "Verify workspace checksum", inline=True)
comment(0x9DE5, "Push result on stack", inline=True)
comment(0x9DE6, "Load block offset", inline=True)
comment(0x9DE8, "Push block offset", inline=True)
comment(0x9DE9, "Store X in l10c9", inline=True)
comment(0x9DEC, "Find matching FCB entry", inline=True)
comment(0x9DEF, "Zero: no match found", inline=True)
comment(0x9DF1, "Load FCB low byte from l1000", inline=True)
comment(0x9DF4, "Compare with stored offset l1098", inline=True)
comment(0x9DF7, "Below stored: no match", inline=True)
comment(0x9DF9, "X=&FF: mark as found (all bits set)", inline=True)
comment(0x9DFB, "ALWAYS branch (negative)", inline=True)
comment(0x9DFD, "X=0: mark as not found", inline=True)
comment(0x9DFF, "Restore block offset from stack", inline=True)
comment(0x9E00, "Transfer to Y", inline=True)
comment(0x9E01, "Restore result from stack", inline=True)
comment(0x9E02, "Return", inline=True)

# update_addr_from_offset9/1 + adjust_fsopts_4bytes (&9E03-&9E22)
comment(0x9E03, "Y=9: FS options offset for high address", inline=True)
comment(0x9E05, "Add workspace values to FS options", inline=True)
comment(0x9E08, "Y=1: FS options offset for low address", inline=True)
comment(0x9E0A, "Clear carry for addition", inline=True)
comment(0x9E0B, "X=&FC: loop counter (-4 to -1)", inline=True)
comment(0x9E0D, "Load FS options byte at offset Y", inline=True)
comment(0x9E0F, "Test fs_load_addr_2 bit 7 (add/subtract)", inline=True)
comment(0x9E11, "Bit 7 set: subtract instead", inline=True)
comment(0x9E13, "Add workspace byte to FS options", inline=True)
comment(0x9E16, "Jump to store result", inline=True)
comment(0x9E19, "Subtract workspace byte from FS options", inline=True)
comment(0x9E1C, "Store result back to FS options", inline=True)
comment(0x9E1E, "Advance to next byte", inline=True)
comment(0x9E1F, "Advance counter", inline=True)
comment(0x9E20, "Loop until 4 bytes processed", inline=True)
comment(0x9E22, "Return", inline=True)

# OSBGET/OSBPUT dispatch (&9E23-&9E41)
comment(0x9E23, "Verify workspace checksum", inline=True)
comment(0x9E26, "Set up transfer parameters", inline=True)
comment(0x9E29, "Push transfer type on stack", inline=True)
comment(0x9E2A, "Set owner-only access mask", inline=True)
comment(0x9E2D, "Pull transfer type", inline=True)
comment(0x9E2E, "Transfer to X", inline=True)
comment(0x9E2F, "Zero: no valid operation, return", inline=True)
comment(0x9E31, "Decrement (convert 1-based to 0-based)", inline=True)
comment(0x9E32, "Compare with 8 (max operation)", inline=True)
comment(0x9E34, "Below 8: valid operation", inline=True)
comment(0x9E36, "Out of range: return with flag", inline=True)
comment(0x9E39, "Transfer operation code to A", inline=True)
comment(0x9E3A, "Y=0: buffer offset", inline=True)
comment(0x9E3C, "Push operation code", inline=True)
comment(0x9E3D, "Compare with 4 (write operations)", inline=True)
comment(0x9E3F, "Below 4: read operation", inline=True)
comment(0x9E41, "4 or above: write data block", inline=True)

# c9e44: OSBGET read byte from file (&9E44-&9EBD)
comment(0x9E44, "Load channel handle from FS options", inline=True)
comment(0x9E46, "Push handle", inline=True)
comment(0x9E47, "Check file is not a directory", inline=True)
comment(0x9E4A, "Pull handle", inline=True)
comment(0x9E4B, "Transfer to Y", inline=True)
comment(0x9E4C, "Process all matching FCBs", inline=True)
comment(0x9E4F, "Load FCB flag byte from l1030", inline=True)
comment(0x9E52, "Store file handle in l0f05", inline=True)
comment(0x9E55, "A=0: clear direction flag", inline=True)
comment(0x9E57, "Store in l0f06", inline=True)
comment(0x9E5A, "Load FCB low byte (position)", inline=True)
comment(0x9E5D, "Store in l0f07", inline=True)
comment(0x9E60, "Load FCB high byte", inline=True)
comment(0x9E63, "Store in l0f08", inline=True)
comment(0x9E66, "Load FCB extent byte", inline=True)
comment(0x9E69, "Store in l0f09", inline=True)
comment(0x9E6C, "Y=&0D: TX buffer size", inline=True)
comment(0x9E6E, "X=5: argument count", inline=True)
comment(0x9E70, "Send TX control block to server", inline=True)
comment(0x9E73, "Pull operation code", inline=True)
comment(0x9E74, "Set up transfer workspace", inline=True)
comment(0x9E77, "Save flags (carry from setup)", inline=True)
comment(0x9E78, "Y=0: index for channel handle", inline=True)
comment(0x9E7A, "Load channel handle from FS options", inline=True)
comment(0x9E7C, "Carry set (write): set active", inline=True)
comment(0x9E7E, "Read: clear connection active", inline=True)
comment(0x9E81, "Branch to continue (always positive)", inline=True)
comment(0x9E83, "Write: set connection active", inline=True)
comment(0x9E86, "Clear l0f06 (Y=0)", inline=True)
comment(0x9E89, "Look up channel slot data", inline=True)
comment(0x9E8C, "Store flag byte in l0f05", inline=True)
comment(0x9E8F, "Y=&0C: TX buffer size (short)", inline=True)
comment(0x9E91, "X=2: argument count", inline=True)
comment(0x9E93, "Send TX control block", inline=True)
comment(0x9E96, "Look up channel entry at Y=0", inline=True)
comment(0x9E99, "Y=9: FS options offset for position", inline=True)
comment(0x9E9B, "Load new position low from l0f05", inline=True)
comment(0x9E9E, "Update FCB low byte in l1000", inline=True)
comment(0x9EA1, "Store in FS options at Y=9", inline=True)
comment(0x9EA3, "Y=&0A", inline=True)
comment(0x9EA4, "Load new position high from l0f06", inline=True)
comment(0x9EA7, "Update FCB high byte in l1010", inline=True)
comment(0x9EAA, "Store in FS options at Y=&0A", inline=True)
comment(0x9EAC, "Y=&0B", inline=True)
comment(0x9EAD, "Load new extent from l0f07", inline=True)
comment(0x9EB0, "Update FCB extent in l1020", inline=True)
comment(0x9EB3, "Store in FS options at Y=&0B", inline=True)
comment(0x9EB5, "A=0: clear high byte of extent", inline=True)
comment(0x9EB7, "Y=&0C", inline=True)
comment(0x9EB8, "Store zero in FS options at Y=&0C", inline=True)
comment(0x9EBA, "Restore flags", inline=True)
comment(0x9EBB, "A=0: success", inline=True)
comment(0x9EBD, "Jump to finalise and return", inline=True)

# lookup_cat_entry_0 + lookup_cat_slot_data (&9EC0-&9ECA)
comment(0x9EC0, "Y=0: offset for channel handle", inline=True)
comment(0x9EC2, "Load channel handle from FS options", inline=True)
comment(0x9EC4, "Look up channel by character", inline=True)
comment(0x9EC7, "Load FCB flag byte from l1030", inline=True)
comment(0x9ECA, "Return with flag in A", inline=True)

# setup_transfer_workspace: prepare for data transfer (&9ECB-&9F54)
comment(0x9ECB, "Push operation code on stack", inline=True)
comment(0x9ECC, "Look up channel entry at Y=0", inline=True)
comment(0x9ECF, "Store flag byte in l0f05", inline=True)
comment(0x9ED2, "Y=&0B: source offset in FS options", inline=True)
comment(0x9ED4, "X=6: copy 6 bytes", inline=True)
comment(0x9ED6, "Load FS options byte", inline=True)
comment(0x9ED8, "Store in l0f06 buffer", inline=True)
comment(0x9EDB, "Decrement source index", inline=True)
comment(0x9EDC, "Skip offset 8?", inline=True)
comment(0x9EDE, "No: continue copy", inline=True)
comment(0x9EE0, "Skip offset 8 (hole in structure)", inline=True)
comment(0x9EE1, "Decrement destination counter", inline=True)
comment(0x9EE2, "Loop until all 6 bytes copied", inline=True)
comment(0x9EE4, "Pull operation code", inline=True)
comment(0x9EE5, "Shift right: check bit 0 (direction)", inline=True)
comment(0x9EE6, "Push updated code", inline=True)
comment(0x9EE7, "Carry clear: OSBGET (read)", inline=True)
comment(0x9EE9, "Carry set: OSBPUT (write), X=1", inline=True)
comment(0x9EEA, "Store direction flag in l0f06", inline=True)
comment(0x9EED, "Y=&0B: TX buffer size", inline=True)
comment(0x9EEF, "X=&91: port for OSBGET", inline=True)
comment(0x9EF1, "Pull operation code", inline=True)
comment(0x9EF2, "Push back (keep on stack)", inline=True)
comment(0x9EF3, "Zero (OSBGET): keep port &91", inline=True)
comment(0x9EF5, "X=&92: port for OSBPUT", inline=True)
comment(0x9EF7, "Y=&0A: adjusted buffer size", inline=True)
comment(0x9EF8, "Store port in l0f02", inline=True)
comment(0x9EFB, "Store port in fs_error_ptr", inline=True)
comment(0x9EFD, "X=8: argument count", inline=True)
comment(0x9EFF, "Load file handle from l0f05", inline=True)
comment(0x9F02, "Send request (no write data)", inline=True)
comment(0x9F05, "X=0: index", inline=True)
comment(0x9F07, "Load channel handle from FS options", inline=True)
comment(0x9F09, "Transfer to X as index", inline=True)
comment(0x9F0A, "Load FCB flags from l1040", inline=True)
comment(0x9F0D, "Toggle bit 0 (transfer direction)", inline=True)
comment(0x9F0F, "Store updated flags", inline=True)
comment(0x9F12, "Clear carry for addition", inline=True)
comment(0x9F13, "X=4: process 4 address bytes", inline=True)
comment(0x9F15, "Load FS options address byte", inline=True)
comment(0x9F17, "Store in zero page address area", inline=True)
comment(0x9F1A, "Store in TXCB position", inline=True)
comment(0x9F1D, "Advance Y by 4", inline=True)
comment(0x9F20, "Add offset from FS options", inline=True)
comment(0x9F22, "Store computed end address", inline=True)
comment(0x9F25, "Retreat Y by 3 for next pair", inline=True)
comment(0x9F28, "Decrement byte counter", inline=True)
comment(0x9F29, "Loop for all 4 address bytes", inline=True)
comment(0x9F2B, "X=1 (INX from 0)", inline=True)
comment(0x9F2C, "Load offset from l0f03", inline=True)
comment(0x9F2F, "Copy to l0f06", inline=True)
comment(0x9F32, "Decrement counter", inline=True)
comment(0x9F33, "Loop until both bytes copied", inline=True)
comment(0x9F35, "Pull operation code", inline=True)
comment(0x9F36, "Non-zero (OSBPUT): swap addresses", inline=True)
comment(0x9F38, "Load port from l0f02", inline=True)
comment(0x9F3B, "Check and set up TXCB", inline=True)
comment(0x9F3E, "Carry set: skip swap", inline=True)
comment(0x9F40, "Send TXCB and swap start/end addresses", inline=True)
comment(0x9F43, "Receive and process reply", inline=True)
comment(0x9F46, "Store result in fs_load_addr_2", inline=True)
comment(0x9F48, "Update addresses from offset 9", inline=True)
comment(0x9F4B, "Decrement fs_load_addr_2", inline=True)
comment(0x9F4D, "Set carry for subtraction", inline=True)
comment(0x9F4E, "Adjust FS options by 4 bytes", inline=True)
comment(0x9F51, "Shift l0f05 left (update status)", inline=True)
comment(0x9F54, "Return", inline=True)

# c9f55: send OSBPUT data to server (&9F55-&9F68)
comment(0x9F55, "Y=&15: TX buffer size for OSBPUT data", inline=True)
comment(0x9F57, "Send TX control block", inline=True)
comment(0x9F5A, "Load display flag from l0e05", inline=True)
comment(0x9F5D, "Store in l0f16", inline=True)
comment(0x9F60, "Clear fs_load_addr (X=0)", inline=True)
comment(0x9F62, "Clear fs_load_addr_hi", inline=True)
comment(0x9F64, "A=&12: byte count for data block", inline=True)
comment(0x9F66, "Store in fs_load_addr_2", inline=True)
comment(0x9F68, "ALWAYS branch to write data block", inline=True)

# c9f6a: OSBPUT write byte to file (&9F6A-&9FB6)
comment(0x9F6A, "Y=4: offset for station comparison", inline=True)
comment(0x9F6C, "Load stored station from l0d63", inline=True)
comment(0x9F6F, "Zero: skip station check", inline=True)
comment(0x9F71, "Compare with FS options station", inline=True)
comment(0x9F73, "Mismatch: skip subtraction", inline=True)
comment(0x9F75, "Y=3", inline=True)
comment(0x9F76, "Subtract FS options value", inline=True)
comment(0x9F78, "Store result in svc_state", inline=True)
comment(0x9F7A, "Load FS options byte at Y", inline=True)
comment(0x9F7C, "Store in workspace at fs_last_byte_flag+Y", inline=True)
comment(0x9F7F, "Decrement index", inline=True)
comment(0x9F80, "Loop until all bytes copied", inline=True)
comment(0x9F82, "Pull operation code", inline=True)
comment(0x9F83, "Mask to 2-bit sub-operation", inline=True)
comment(0x9F85, "Zero: send OSBPUT data", inline=True)
comment(0x9F87, "Shift right: check bit 0", inline=True)
comment(0x9F88, "Zero (bit 0 clear): handle read", inline=True)
comment(0x9F8A, "Carry set: handle catalogue update", inline=True)
comment(0x9F8C, "Transfer to Y (Y=0)", inline=True)
comment(0x9F8D, "Load data byte from l0e03", inline=True)
comment(0x9F90, "Store in l0f03", inline=True)
comment(0x9F93, "Load high data byte from l0e04", inline=True)
comment(0x9F96, "Store in l0f04", inline=True)
comment(0x9F99, "Load port from l0e02", inline=True)
comment(0x9F9C, "Store in l0f02", inline=True)
comment(0x9F9F, "X=&12: buffer size marker", inline=True)
comment(0x9FA1, "Store in l0f01", inline=True)
comment(0x9FA4, "A=&0D: count value", inline=True)
comment(0x9FA6, "Store in l0f06", inline=True)
comment(0x9FA9, "Store in fs_load_addr_2", inline=True)
comment(0x9FAB, "Shift right (A=6)", inline=True)
comment(0x9FAC, "Store in l0f05", inline=True)
comment(0x9FAF, "Clear carry for addition", inline=True)
comment(0x9FB0, "Prepare and send TX control block", inline=True)
comment(0x9FB3, "Store X in fs_load_addr_hi (X=0)", inline=True)
comment(0x9FB5, "X=1 (INX)", inline=True)
comment(0x9FB6, "Store X in fs_load_addr", inline=True)

# write_data_block: write data to host or tube (&9FB8-&9FF4)
comment(0x9FB8, "Load svc_state (tube flag)", inline=True)
comment(0x9FBA, "Non-zero: write via tube", inline=True)
comment(0x9FBC, "Load source index from fs_load_addr", inline=True)
comment(0x9FBE, "Load destination index from fs_load_addr_hi", inline=True)
comment(0x9FC0, "Load data byte from l0f05 buffer", inline=True)
comment(0x9FC3, "Store to destination via fs_crc pointer", inline=True)
comment(0x9FC5, "Advance source index", inline=True)
comment(0x9FC6, "Advance destination index", inline=True)
comment(0x9FC7, "Decrement byte counter", inline=True)
comment(0x9FC9, "Loop until all bytes transferred", inline=True)
comment(0x9FCB, "ALWAYS branch to update catalogue", inline=True)
comment(0x9FCD, "Claim tube with call &C3", inline=True)
comment(0x9FD0, "A=1: tube transfer type (write)", inline=True)
comment(0x9FD2, "Load destination low from fs_options", inline=True)
comment(0x9FD4, "Load destination high from fs_block_offset", inline=True)
comment(0x9FD6, "Increment low byte", inline=True)
comment(0x9FD7, "No wrap: skip high increment", inline=True)
comment(0x9FD9, "Carry: increment high byte", inline=True)
comment(0x9FDA, "Set up tube transfer address", inline=True)
comment(0x9FDD, "Load source index", inline=True)
comment(0x9FDF, "Load data byte from buffer", inline=True)
comment(0x9FE2, "Write to tube data register 3", inline=True)
comment(0x9FE5, "Advance source index", inline=True)
comment(0x9FE6, "Y=6: tube write delay", inline=True)
comment(0x9FE8, "Delay loop: decrement Y", inline=True)
comment(0x9FE9, "Loop until delay complete", inline=True)
comment(0x9FEB, "Decrement byte counter", inline=True)
comment(0x9FED, "Loop until all bytes written to tube", inline=True)
comment(0x9FEF, "A=&83: release tube claim", inline=True)
comment(0x9FF1, "Release tube", inline=True)
comment(0x9FF4, "Jump to clear A and finalise return", inline=True)

# c9ff7: catalogue update command (&9FF7-&9FFE)
comment(0x9FF7, "Y=9: offset for position byte", inline=True)
comment(0x9FF9, "Load position from FS options", inline=True)
comment(0x9FFB, "Store in l0f06", inline=True)
comment(0x9FFE, "Y=5: offset for extent byte", inline=True)

# c9ff7 continued: catalogue update data transfer (&A000-&A058)
comment(0xA000, "Load extent byte from FS options", inline=True)
comment(0xA002, "Store in l0f07", inline=True)
comment(0xA005, "X=&0D: byte count", inline=True)
comment(0xA007, "Store in l0f08", inline=True)
comment(0xA00A, "Y=2: command sub-type", inline=True)
comment(0xA00C, "Store in fs_load_addr", inline=True)
comment(0xA00E, "Store in l0f05", inline=True)
comment(0xA011, "Y=3: TX buffer command byte", inline=True)
comment(0xA012, "Send TX control block", inline=True)
comment(0xA015, "Store X (0) in fs_load_addr_hi", inline=True)
comment(0xA017, "Load data offset from l0f06", inline=True)
comment(0xA01A, "Store as first byte of FS options", inline=True)
comment(0xA01C, "Load data count from l0f05", inline=True)
comment(0xA01F, "Y=9: position offset in FS options", inline=True)
comment(0xA021, "Add to current position", inline=True)
comment(0xA023, "Store updated position", inline=True)
comment(0xA025, "Load TXCB end byte", inline=True)
comment(0xA027, "Subtract 7 (header overhead)", inline=True)
comment(0xA029, "Store remaining data size", inline=True)
comment(0xA02C, "Store in fs_load_addr_2 (byte count)", inline=True)
comment(0xA02E, "Zero bytes: skip write", inline=True)
comment(0xA030, "Write data block to host/tube", inline=True)
comment(0xA033, "X=2: clear 3 bytes (indices 0-2)", inline=True)
comment(0xA035, "Clear l0f07+X", inline=True)
comment(0xA038, "Decrement index", inline=True)
comment(0xA039, "Loop until all cleared", inline=True)
comment(0xA03B, "Update addresses from offset 1", inline=True)
comment(0xA03E, "Set carry for subtraction", inline=True)
comment(0xA03F, "Decrement fs_load_addr_2", inline=True)
comment(0xA041, "Load data count from l0f05", inline=True)
comment(0xA044, "Copy to l0f06", inline=True)
comment(0xA047, "Adjust FS options by 4 bytes (subtract)", inline=True)
comment(0xA04A, "X=3: check 4 bytes", inline=True)
comment(0xA04C, "Y=5: starting offset", inline=True)
comment(0xA04E, "Set carry for comparison", inline=True)
comment(0xA04F, "Load FS options byte", inline=True)
comment(0xA051, "Non-zero: more data remaining", inline=True)
comment(0xA053, "Advance to next byte", inline=True)
comment(0xA054, "Decrement counter", inline=True)
comment(0xA055, "Loop until all bytes checked", inline=True)
comment(0xA057, "All zero: clear carry (transfer complete)", inline=True)
comment(0xA058, "Jump to update catalogue and return", inline=True)

# tube_claim_c3: claim tube with protocol &C3 (&A05B-&A062)
comment(0xA05B, "A=&C3: tube claim protocol", inline=True)
comment(0xA05D, "Dispatch tube address/data claim", inline=True)
comment(0xA060, "Carry clear: claim failed, retry", inline=True)
comment(0xA062, "Return (tube claimed)", inline=True)

# tube_init_reloc continued: copy relocated blocks (&BE90-&BEBE)
# Copies pages 4/5/6 code and zero-page workspace from ROM to RAM
comment(0xBE90, "Store BRK vector high byte", inline=True)
comment(0xBE93, "A=&8E: Tube control register value", inline=True)
comment(0xBE95, "Write Tube control register", inline=True)
comment(0xBE98, "Y=0: copy 256 bytes per page", inline=True)
comment(0xBE9A, "Load page 4 source byte", inline=True)
comment(0xBE9D, "Store to page 4 destination", inline=True)
comment(0xBEA0, "Load page 5 source byte", inline=True)
comment(0xBEA3, "Store to page 5 destination", inline=True)
comment(0xBEA6, "Load page 6 source byte", inline=True)
comment(0xBEA9, "Store to page 6 destination", inline=True)
comment(0xBEAC, "Decrement byte counter", inline=True)
comment(0xBEAD, "Non-zero: continue copying", inline=True)
comment(0xBEAF, "Clear tube claim state", inline=True)
comment(0xBEB2, "X=&41: copy 66 bytes of ZP workspace", inline=True)
comment(0xBEB4, "Load ZP source byte from ROM", inline=True)
comment(0xBEB7, "Store to NMI workspace at &16+X", inline=True)
comment(0xBEB9, "Decrement byte counter", inline=True)
comment(0xBEBA, "More bytes: continue copying", inline=True)
comment(0xBEBC, "A=0: return success", inline=True)
comment(0xBEBE, "Return to caller", inline=True)

# ============================================================
# Generate disassembly
# ============================================================

import json
import sys

output = go(print_output=False)

_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "anfs-4.08.53.asm"
output_filepath.write_text(output)
print(f"Wrote {output_filepath}", file=sys.stderr)

structured = get_structured()
json_filepath = _output_dirpath / "anfs-4.08.53.json"
json_filepath.write_text(json.dumps(structured))
print(f"Wrote {json_filepath}", file=sys.stderr)
