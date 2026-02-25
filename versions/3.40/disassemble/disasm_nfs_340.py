import os
from pathlib import Path

from py8dis.commands import *
import py8dis.acorn as acorn

init(assembler_name="beebasm", lower_case=True)

# ============================================================
# Address map: NFS 3.35K → NFS 3.40
# ============================================================
# This driver was derived from the NFS 3.35K disassembly driver.
# The two ROMs are 89.4% identical at the opcode level.
# with operands). There are 161 change blocks across the ROM.
#
# Major changes vs 3.34B:
# - Language entry shifted $8099 → $80D4, service entry $80AF → $80EA
# - New station number parser for *I AM / login commands
# - Table-driven vector initialisation replaces hardcoded stores
# - GSINIT/GSREAD filename parsing for *LOAD/*SAVE
# - Per-ROM disable flag in service handler filtering
# - Tube WRCH handling moved back to R1 ($FEE0/$FEE1),
#   reversing the 3.34B change that moved it to R4
# - Relocated blocks shifted +$12 in ROM (BRK $931A, P4 $935F,
#   P5 $945F, P6 $955F)
# - Table-driven Tube transfer init replaces conditional branching
# - Print/display routines relocated from $85xx to $8Dxx area

# Paths are resolved relative to this script's location in the repo
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get(
    "ACORN_NFS_ROM",
    str(_version_dirpath / "rom" / "nfs-3.40.rom"),
)
_output_dirpath = Path(os.environ.get(
    "ACORN_NFS_OUTPUT",
    str(_version_dirpath / "output"),
))

load(0x8000, _rom_filepath, "6502")

# ============================================================
# Relocated code blocks
# ============================================================
# The NFS ROM copies code from ROM into RAM at initialisation (&8103-&8140).
# These blocks execute at different addresses than their storage locations.
# move(dest, src, length) tells py8dis the runtime address for each block.
#
# The page copy loop (&8120) starts with Y=0, DEY/BNE wraps through
# &FF..&01 — all 256 bytes of each page are copied.
#
# The workspace init (&813A) copies X=&60 downto 0 (BPL) = 97 bytes.
#
# Vectors set up during init:
#   BRKV  = &0016 (in workspace block — BRK/error handler)
#   RDCHV = &04E7 (in page 4 — RDCH handler)
#   WRCHV = &051C (in page 5 — WRCH handler)
#   EVNTV = &06E8 (in page 6 — event handler)

# BRK handler + NMI workspace init code (&9308 → &0016-&0076)
move(0x0016, 0x931C, 0x61)

# NMI handler / CLI command code (&934D/&944D/&954D → pages &04/&05/&06)
move(0x0400, 0x935D, 0x100)
move(0x0500, 0x9456, 0x100)
move(0x0600, 0x9556, 0x100)

# acorn.bbc() provides: os_text_ptr (&F2), romsel_copy (&F4), osrdsc_ptr (&F6),
# all OS vectors (brkv, wrchv, ..., netv), all OS entry points (osasci, osbyte, ...),
# plus hooks for automatic OSBYTE/OSWORD annotation.
# acorn.is_sideways_rom() provides: rom_header, language_entry, service_entry,
# rom_type, copyright_offset, binary_version, title, language_handler, service_handler.
acorn.bbc()
acorn.is_sideways_rom()

# Split the copyright string classification so the null terminator
# at &8018 becomes a separate item.  This lets error_offsets have its
# own label line rather than being expressed as copyright_string+7.
from py8dis import classification as _cls, disassembly as _disasm
from py8dis.memorymanager import RuntimeAddr as _RuntimeAddr
from py8dis.movemanager import r2b as _r2b
_copyright_bin = _r2b(_RuntimeAddr(0x8011))[0]
_disasm.classifications[_copyright_bin] = _cls.String(7)       # "(C)ROFF"
_disasm.classifications[_copyright_bin + 7] = _cls.Byte(1)     # null terminator

# ============================================================
# Hardware registers
# ============================================================

# MC6854 ADLC registers (active at &FEA0-&FEA3 when active Econet station)
constant(0xFEA0, "adlc_cr1")   # Write: CR1 (or CR3 if AC=1). Read: SR1
constant(0xFEA1, "adlc_cr2")   # Write: CR2 (or CR4 if AC=1). Read: SR2
constant(0xFEA2, "adlc_tx")    # Write: TX FIFO (continue frame). Read: RX FIFO
constant(0xFEA3, "adlc_tx2")   # Write: TX FIFO (last byte, terminates frame). Read: RX FIFO

# Econet hardware on the 1MHz bus
constant(0xFE18, "econet_station_id")  # Read: station DIP switches AND INTOFF (disable NMIs)
constant(0xFE20, "econet_nmi_enable")  # Read: INTON (re-enable NMIs). Any read &FE20-&FE23.

# Tube ULA registers (&FEE0-&FEE7) — named by acorn.bbc()
# R1 (&FEE0/&FEE1): events and escape signalling (host↔parasite)
# R2 (&FEE2/&FEE3): command bytes and general data transfer
# R4 (&FEE6/&FEE7): one-byte transfers (error codes, BRK signalling)

# Key ADLC register values (from original disassembly annotations):
#   CR1=&C1: full reset (TX_RESET|RX_RESET|AC)
#   CR1=&82: RX listen (TX_RESET|RIE)
#   CR1=&44: TX active (RX_RESET|TIE)
#   CR2=&67: clear all status (CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
#   CR2=&E7: TX prepare (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)
#   CR2=&3F: TX last data (CLR_RX_ST|TX_LAST_DATA|FLAG_IDLE|FC_TDRA|2_1_BYTE|PSE)
#   CR2=&A7: TX in handshake (RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE)

# ============================================================
# Protocol constants from DNFS 3.60 reference (NFS00)
# ============================================================

# Econet port numbers (FS protocol version 2)
# Ports are allocated above &B0 to leave &01-&AA free for user applications.
# The low 3 bits of the TXCB flag byte encode error reasons and index into
# the error message table (ERRTAB) at &854D.
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
constant(0xA4, "err_tx_cb_error")     # TXCBER: TX control block error
constant(0xA5, "err_no_reply")        # NOREPE: no reply from server
constant(0xA8, "err_fs_cutoff")       # ERRCUT: FS errors >= this are FS-specific

# Protocol flags
constant(0x80, "tx_flag")             # TXFLAG: OR with flag byte before transmit
constant(0x7F, "rx_ready")            # RXRDY: flag byte value for reception ready

# FS handle base and retry count
constant(0x20, "handle_base")         # HAND: base value for file handles (&20-&27)

# Control block template markers
constant(0xFE, "cb_stop")             # CBSTOP: stop copying in ctrl_block_setup
constant(0xFD, "cb_skip")             # CBSKIP: skip this byte (leave unchanged)
constant(0xFC, "cb_fill")             # CBFILL: substitute page byte of pointer

# ============================================================
# Inline string subroutine hook
# ============================================================
# print_inline (&85D9) prints an inline string following the JSR, terminated by a
# byte with bit 7 set. The high-bit byte is the opcode of the next
# instruction — the routine jumps there via JMP (fs_load_addr).
hook_subroutine(0x8605, "print_inline", stringhi_hook)

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
# From J.G. Harston's NFSWorkSp and mdfs.net/Docs/Comp/BBC/AllMem

label(0x0097, "escapable")           # b7=respond to Escape flag
label(0x0098, "need_release_tube")   # b7=need to release Tube
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
# nfs_temp and rom_svc_num were at &A8/&A9 in 3.35D; reverted to &CD/&CE in 3.35K

# ============================================================
# Zero page — Filing system workspace (&B0-&CF)
# ============================================================
# NFS zero-page layout from DNFS 3.60 source (NFS00):
#   &B0-&B3  WORK    4-byte variable workspace (load/exec/size)
#   &B4-&B7  (WORK+4) additional workspace (address compare target)
#   &B8      JWORK   3 bytes for timing (also CRFLAG at &B9, SPOOL1 at &BA)
#   &BB      TEMPX   register save: X (also used as options pointer low)
#   &BC      TEMPY   register save: Y (also options pointer high)
#   &BD      TEMPA   register save: A (also last-byte flag)
#   &BE-&BF  POINTR  generic 2-byte pointer (filename, workspace)
#   &C0-&CE  TXCB/RXCB overlapping TX/RX control blocks (15 bytes)
#   &CF      SPOOL0  spool file handle
# NB: &CD-&CE noted as "two bytes free" in original source.

label(0x00B0, "fs_load_addr")        # WORK: load/start address (4 bytes)
label(0x00B1, "fs_load_addr_hi")
label(0x00B2, "fs_load_addr_2")
label(0x00B8, "fs_error_ptr")        # JWORK: error pointer / timing workspace
label(0x00BB, "fs_options")          # TEMPX: options/control block pointer (low)
label(0x00BC, "fs_block_offset")     # TEMPY: block offset / control block pointer (high)
label(0x00BD, "fs_last_byte_flag")   # TEMPA: b7=last byte from block / saved A
label(0x00BE, "fs_crc_lo")           # POINTR: generic pointer (low)
label(0x00BF, "fs_crc_hi")           # POINTR+1: generic pointer (high)
label(0x00CD, "nfs_temp")            # General-purpose NFS temporary (at &A8 in 3.35D)
label(0x00CE, "rom_svc_num")        # ROM service number, 7=osbyte, 8=osword (at &A9 in 3.35D)

# Zero page — Additional OS locations
label(0x0010, "zp_temp_10")          # Temporary storage (Y save during service calls)
label(0x0011, "zp_temp_11")          # Temporary storage (X save during service calls)
label(0x0016, "nmi_workspace_start") # Start of NMI workspace area (&0016-&0076)
label(0x005F, "zp_63")               # Used by NFS

# ============================================================
# Page &0D — NMI handler workspace (&0D00-&0D67)
# ============================================================
# The NMI shim code occupies &0D00-&0D1F. Workspace follows at &0D20.
# From J.G. Harston's PageD (mdfs.net/Misc/Source/Acorn/NFS/PageD)

# NMI shim internal addresses (label not constant — these are memory refs)
label(0x0D0C, "nmi_jmp_lo")         # JMP target low byte (self-modifying)
label(0x0D0D, "nmi_jmp_hi")         # JMP target high byte (self-modifying)
label(0x0D0E, "set_nmi_vector")     # Subroutine: set NMI handler (A=low, Y=high)
label(0x0D14, "nmi_rti")            # NMI return: restore ROM bank, PLA, BIT INTON, RTI
label(0x0D1A, "nmi_shim_1a")        # Referenced by NMI workspace init

# Scout/acknowledge packet buffer (&0D20-&0D25)
label(0x0D20, "tx_dst_stn")         # TX: Destination station
label(0x0D21, "tx_dst_net")         # TX: Destination network
label(0x0D22, "tx_src_stn")         # TX: Source station
label(0x0D23, "tx_src_net")         # TX: Source network
label(0x0D24, "tx_ctrl_byte")       # TX: Control byte
label(0x0D25, "tx_port")            # TX: Port number
label(0x0D26, "tx_data_start")      # TX: Start of data area

# TX control
label(0x0D2A, "tx_data_len")        # Length of data in open port block
label(0x0D3A, "tx_ctrl_status")     # TX control/status byte (shifted by ASL at &8EB8)

# Received scout (&0D3D-&0D48)
# &0D3D is also the base of the scout buffer for indexed access (STA &0D3D,Y)
label(0x0D3D, "rx_src_stn")         # RX: Source station (scout buffer base)
label(0x0D3E, "rx_src_net")         # RX: Source network
label(0x0D3F, "rx_ctrl")            # RX: Control byte
label(0x0D40, "rx_port")            # RX: Port number
label(0x0D41, "rx_remote_addr")     # RX: Remote address (4 bytes) / broadcast data (8 bytes)

# TX state
label(0x0D4A, "tx_flags")           # TX workspace flags (b0=four-way, b6=completion)
label(0x0D4B, "nmi_next_lo")        # Next NMI handler address (low)
label(0x0D4C, "nmi_next_hi")        # Next NMI handler address (high)
label(0x0D4F, "tx_index")           # Current TX buffer index
label(0x0D50, "tx_length")          # TX frame length
label(0x0D51, "tx_work_51")         # TX workspace (possibly retry count or flags)
label(0x0D57, "tx_work_57")         # TX workspace (possibly timeout or state)

# RX/status
label(0x0D07, "nmi_shim_07")        # NMI shim workspace
label(0x0D38, "rx_status_flags")    # RX status/mode flags
label(0x0D3B, "rx_ctrl_copy")       # Copy of received control byte
label(0x0D52, "tx_in_progress")     # Referenced by NMI handlers
label(0x0D5C, "scout_status")       # Scout/packet status indicator
label(0x0D5D, "rx_extra_byte")      # Extra byte read after data frame completion

# Econet state (&0D60-&0D67) — reference: NFS00 PBUFFP-TBFLAG
label(0x0D61, "printer_buf_ptr")    # PBUFFP: printer buffer pointer
label(0x0D62, "tx_clear_flag")      # TXCLR: b7=Transmission in progress
label(0x0D63, "prot_status")        # LSTAT: protection mask — b0=PEEK, b1=POKE, b2=HALT, b3=JSR, b4=PROC
label(0x0D64, "rx_flags")           # LFLAG: b7=system Rx (into page-zero CB), b6=user Rx, b2=Halted
label(0x0D65, "saved_jsr_mask")     # OLDJSR: old copy of JSR buffer protection bits
label(0x0D66, "econet_init_flag")   # b7=Econet using NMI code (&00=no, &80=yes)
label(0x0D67, "tube_flag")          # TBFLAG: b7=Tube present (&00=no, &FF=yes)

# ============================================================
# Page &0E — Filing system context (reference: NFS00 FSLOCN-CMNDP)
# ============================================================
# Layout from the original source (NFS00):
#   &0E00  FSLOCN   File server station (2 bytes: station + network)
#   &0E02  URD      User root directory handle
#   &0E03  CSD      Current selected directory handle
#   &0E04  LIB      Library directory handle
#   &0E05  OPT      AUTOBOOT option number (*OPT 4,n)
#   &0E06  MESS     Messages on/off flag
#   &0E07  EOF      End-of-file flags
#   &0E08  SEQNOS   Byte stream sequence numbers
#   &0E09  ERROR    Slot for last unknown error code
#   &0E0A  SPARE    (also JCMNDP)
#   &0E0D  RSTAT    Status byte
#   &0E0E  TARGET   Target station (2 bytes)
#   &0E10  CMNDP    Pointer to rest of command line
label(0x0E00, "fs_server_stn")      # FSLOCN: file server station number
label(0x0E01, "fs_server_net")      # FSLOCN+1: file server network number
label(0x0E02, "fs_urd_handle")      # URD: user root directory handle
label(0x0E03, "fs_csd_handle")      # CSD: current selected directory handle
label(0x0E04, "fs_lib_handle")      # LIB: library directory handle
label(0x0E05, "fs_boot_option")     # OPT: AUTOBOOT option number
label(0x0E06, "fs_messages_flag")   # MESS: messages on/off flag
label(0x0E07, "fs_eof_flags")       # EOF: end-of-file flags
label(0x0E08, "fs_sequence_nos")    # SEQNOS: byte stream sequence numbers
label(0x0E09, "fs_last_error")      # ERROR: slot for last unknown error code
label(0x0E0A, "fs_cmd_context")     # SPARE/JCMNDP: command context
label(0x0E0D, "fs_reply_status")    # RSTAT: b0=remote ok, b1=view ok, b2=notify ok, b3=remoted, b7=FS selected
label(0x0E0E, "fs_target_stn")      # TARGET: target station for remote ops (2 bytes)
label(0x0E10, "fs_cmd_ptr")         # CMNDP: pointer to rest of command line

# Other workspace used by NFS
# Relocated code — Tube host zero-page code (BRKV = &0016)
# Reference: NFS11 (NEWBR, TSTART, MAIN)
label(0x0029, "tube_brk_send_loop")  # Loop: send error message bytes via R2 until zero terminator
label(0x0032, "tube_reset_stack")    # Reset SP=&FF, CLI, fall through to main loop
label(0x0036, "tube_main_loop")      # Poll R1 (WRCH) and R2 (commands), dispatch via table
label(0x003B, "tube_handle_wrch")    # R1 data ready: read byte, call OSWRITCH (&FFCB)
label(0x0041, "tube_poll_r2")        # Poll R2 status; if ready, read command and dispatch
label(0x0050, "tube_dispatch_cmd")   # JMP (&0500) — dispatch to handler via table
label(0x0053, "tube_transfer_addr")  # 4-byte transfer start address (written by address claim)
entry(0x0016)
entry(0x0032)
entry(0x0036)

# Relocated code — page 4 (Tube address claim, RDCH, data transfer)
# Reference: NFS12 (BEGIN, ADRR, SENDW, TADDR, SETADR)
label(0x0403, "tube_escape_entry")   # JMP to tube_escape_check (&06E2)
label(0x0406, "tube_addr_claim")     # Tube address claim protocol (ADRR in reference)
label(0x041E, "tube_post_init")      # Called after ROM→RAM copy; initial Tube setup
label(0x042F, "return_tube_init")    # Return from tube_post_init path
label(0x047C, "return_tube_xfer")   # Return from tube transfer/setup
# 3.35K label tube_setup_transfer ($04E0) — Tube code rewritten in 3.40
label(0x04E7, "tube_rdch_handler")   # RDCHV target — send &01 via R2, enter main loop
# 3.35K labels tube_restore_regs ($04EF), tube_read_r2 ($04F7) — Tube code rewritten
entry(0x0400)
entry(0x0403)
entry(0x0406)
entry(0x041E)
entry(0x04E7)

# Relocated code — page 5 (Tube dispatch table, WRCH, file I/O handlers)
# Reference: NFS13 (TASKS table, BPUT, BGET, RDCHZ, FIND, ARGS, STRNG, CLI, FILE)
#
# &0500-&051B: 14-entry dispatch table of word addresses.
# JMP (&0500) at &0054 dispatches Tube commands; the address claim
# protocol at &0406 patches &0500-&0501 with the target handler address.
#
# Tube cmd  Entry  Addr   Handler
# ────────  ─────  ─────  ─────────────────────────────
#   &00       0    &055B  tube_osrdch (OSRDCH)
#   &01       1    &05C5  tube_oscli (OSCLI)
#   &02       2    &0626  tube_osbyte_short (2-param, X result)
#   &03       3    &063B  tube_osbyte_long (3-param, X+Y results)
#   &04       4    &065D  tube_osword (variable-length)
#   &05       5    &06A3  tube_osword_rdln (OSWORD 0, read line)
#   &06       6    &04EF  tube_restore_regs (release/no-op)
#   &07       7    &053D  tube_release_return (restore regs, RTS)
#   &08       8    &058C  tube_osargs (OSARGS)
#   &09       9    &0550  tube_osbget (OSBGET)
#   &0A      10    &0543  tube_osbput (OSBPUT)
#   &0B      11    &0569  tube_osfind (OSFIND open)
#   &0C      12    &05D8  tube_osfile (OSFILE)
#   &0D      13    &0602  tube_osgbpb (OSGBPB)
# 3.35K labels tube_wrch_handler ($051C), tube_send_and_poll ($051F) — Tube code rewritten
label(0x0527, "tube_poll_r1_wrch")    # Service R1 WRCH requests while waiting for R2
# 3.35K label tube_resume_poll ($0532) — Tube code rewritten
label(0x053D, "tube_release_return")  # Restore X,Y from &10/&11, PLA, RTS
label(0x0520, "tube_osbput")          # OSBPUT: read channel+byte from R2, call &FFD4
label(0x052D, "tube_osbget")          # OSBGET: read channel from R2, call &FFD7
label(0x0537, "tube_osrdch")          # OSRDCH: call &FFC8, send carry+byte reply
label(0x053A, "tube_rdch_reply")      # Send carry in bit 7 + data byte as reply
label(0x0542, "tube_osfind")          # OSFIND open: read arg+filename, call &FFCE
label(0x0552, "tube_osfind_close")    # OSFIND close: read handle, call &FFCE with A=0
label(0x055E, "tube_osargs")          # OSARGS: read handle+4 bytes+reason, call &FFDA
label(0x0562, "tube_read_params")     # Read parameter bytes from R2 into zero page
label(0x0582, "tube_read_string")     # Read CR-terminated string from R2 into &0700
label(0x0596, "tube_oscli")           # OSCLI: read command string, call &FFF7
label(0x059C, "tube_reply_ack")       # Send &7F acknowledge, return to main loop
label(0x059E, "tube_reply_byte")      # Poll R2, send byte in A, return to main loop
label(0x05A9, "tube_osfile")          # OSFILE: read 16 params+filename+reason, call &FFDD
# Dispatch table entry points (3.40 addresses)
for addr in [0x0537, 0x0596, 0x0626, 0x0607, 0x0627, 0x0668,
             0x04EF, 0x053D, 0x0602,
             0x0520, 0x052D, 0x0542, 0x055E, 0x05A9, 0x05F2]:
    entry(addr)

# Relocated code — page 6 (OSGBPB, OSBYTE, OSWORD, RDLN, event handler)
# Reference: NFS13 (GBPB, SBYTE, BYTE, WORD, RDLN, RDCHA, WRIFOR, ESCAPE, EVENT, ESCA)
# 3.35K label tube_osgbpb ($0602) — Tube code rewritten
# 3.35K fix: after JSR osgbpb, ROR A encodes carry into bit 7
# and sends it via tube_send_r2 BEFORE the 13 parameter bytes.
# In 3.35D, PHA saved A but never sent or popped it — the
# co-processor had no way to determine completion status.
comment(0x0615, """\
3.35K fix: send carry result to co-processor.
3.35D had PHA here (never sent, never popped).""", inline=True)
label(0x0626, "tube_osbyte_short")    # OSBYTE 2-param: read X+A, call &FFF4, return X
label(0x0630, "tube_osbyte_send_x")   # Poll R2, send X result
label(0x0607, "tube_osbyte_long")     # OSBYTE 3-param: read X+Y+A, call &FFF4, return carry+Y+X
label(0x061D, "tube_osbyte_send_y")   # Poll R2, send Y result, then fall through to send X
# 3.35K label tube_osword ($0627) — Tube code rewritten
label(0x062B, "tube_osword_read")     # Poll R2 for param block length, read params
label(0x0636, "tube_osword_read_lp")  # Read param block bytes from R2 into &0130
label(0x0657, "tube_osword_write")    # Write param block bytes from &0130 back to R2
label(0x065A, "tube_osword_write_lp") # Poll R2, send param block byte
label(0x0665, "tube_return_main")     # JMP tube_main_loop
label(0x0668, "tube_osword_rdln")     # OSWORD 0 (read line): read 5 params, call &FFF1
label(0x0680, "tube_rdln_send_line")  # Send input line bytes from &0700 back to Tube
label(0x0687, "tube_rdln_send_loop")  # Load byte from &0700+X
label(0x068A, "tube_rdln_send_byte")  # Send byte via R2, loop until CR
label(0x06A7, "tube_escape_check")    # Check &FF escape flag, forward to Tube via R1
label(0x06AD, "tube_event_handler")   # EVNTV target: forward event (A,X,Y) to Tube via R1
label(0x06BC, "tube_send_r1")         # Poll R1 status, write A to R1 data (ESCA in reference)
entry(0x0600)
entry(0x0626)
entry(0x0607)
entry(0x0627)
entry(0x0668)
entry(0x06A7)
entry(0x06AD)
entry(0x06BC)
label(0x0DEB, "fs_state_deb")        # Filing system state

# ============================================================
# Named labels for dispatch table and key routines
# ============================================================

# ROM header: copyright string doubles as *ROFF command text
# The copyright string "(C)ROFF" serves double duty: the MOS requires
# a valid (C) marker for ROM recognition, and the "ROFF" suffix is
# reused by the star command matcher (svc_star_command) as the command
# text for *ROFF (Remote Off). This saves 4 bytes by avoiding a
# separate "ROFF" entry in the command table.
comment(0x8011, """\
The 'ROFF' suffix at &8014 is reused by the *ROFF
command matcher (svc_star_command) — a space-saving
trick that shares ROM bytes between the copyright
string and the star command table.""")

# ROM header: copyright string and error offset table
label(0x8011, "copyright_string")
label(0x8018, "error_offsets")

# Dispatch tables: split low/high byte address tables.
# In 3.40 the ROM title is 4 bytes longer ("    NET" vs "NET"),
# so ROM header data extends to &8023, and the dispatch tables
# start at &8024/&8049 rather than &8020/&8044.
label(0x8024, "dispatch_lo")            # Low bytes of (handler_addr - 1)
label(0x8049, "dispatch_hi")            # High bytes of (handler_addr - 1)

# Dispatcher and dispatch callers
# Note: &80D4 is already labelled "language_handler" by acorn.is_sideways_rom()

# Filing system OSWORD dispatch (&8EB8-&8E3E)
label(0x8E9F, "fs_osword_tbl_lo")      # Low bytes of FS OSWORD handler table
label(0x8EB5, "fs_osword_tbl_hi")      # High bytes of FS OSWORD handler table

# FS OSWORD handler routines
# osword_0f_handler label created by subroutine() call below.
label(0x8EE9, "read_args_size")        # READRB: get args buffer size from RX block offset &7F
# osword_10_handler label created by subroutine() call below.

# Econet TX/RX handler and OSWORD dispatch
label(0x8FDE, "store_16bit_at_y")     # Store 16-bit value at (nfs_workspace)+Y
# osword_dispatch label created by subroutine() call below.
label(0x908F, "osword_trampoline")     # PHA/PHA/RTS trampoline
label(0x909A, "osword_tbl_lo")         # Dispatch table low bytes
label(0x90A1, "osword_tbl_hi")         # Dispatch table high bytes
# net_write_char label created by subroutine() call below.

# Remote operation function handlers (dispatched via osword_tbl)
# (net_write_char subroutine defined above)
label(0x9130, "match_osbyte_code")   # NCALLP: compare A against OSBYTE function table; Z=1 on match
label(0x9138, "return_match_osbyte") # Return from match_osbyte_code
label(0x8499, "return_remote_cmd")   # Return from remote command data handler
label(0x84A0, "rchex")                # Clear JSR protection after remote command exec

# Control block setup
label(0x9180, "ctrl_block_setup_clv") # CLV entry: same setup but clears V flag

# Remote printer and display handlers (fn 1/2/3/5)

# Network transmit

# JSR buffer protection
label(0x92EB, "clear_jsr_protection") # CLRJSR: reset JSR buffer protection bits (4 refs)

# Palette/VDU state save
label(0x9303, "read_vdu_osbyte_x0")  # Read next VDU OSBYTE with X=0 parameter
label(0x9305, "read_vdu_osbyte")     # Read next OSBYTE from table, store result in workspace

# ADLC initialisation and state management

# Tube co-processor I/O subroutines (in relocated page 6)
# Reference: RDCHA (R2 write), WRIFOR (R4 write), ESCA (R1 write)
label(0x0695, "tube_send_r2")       # Poll R2 status, write A to R2 data (RDCHA in reference)
label(0x069E, "tube_send_r4")       # Poll R4 status, write A to R4 data (WRIFOR in reference)

# ============================================================
# Service call handler labels (&8000-&8500)
# ============================================================
# Service call numbers and their dispatch table indices:
#   svc 0  → index 1  → return_2 (no-op)
#   svc 1  → index 2  → svc_1_abs_workspace (&82A2)
#   svc 2  → index 3  → svc_2_private_workspace (&82AB)
#   svc 3  → index 4  → svc_3_autoboot (&8203)
#   svc 4  → index 5  → svc_4_star_command (&81B1)
#   svc 5  → index 6  → svc_5_unknown_irq (&966C) → JMP c9b52
#   svc 6  → index 7  → return_2 (BRK — no action)
#   svc 7  → index 8  → dispatch_net_cmd (&806F) (unrecognised OSBYTE)
#   svc 8  → index 9  → svc_8_osword (&8E7F) (unrecognised OSWORD)
#   svc 9  → index 10 → svc_9_help (&81ED)
#   svc 10 → index 11 → return_2 (no action)
#   svc 11 → index 12 → svc_11_nmi_claim (&9669) → JMP restore_econet_state
#   svc 12 → index 13 → svc_12_nmi_release (&9666) → JMP save_econet_state
#
# Special service handling (outside dispatch table):
#   svc &12 (18) with Y=5 → svc_13_select_nfs (&81B5)
#   svc &FE → Tube init (explode character definitions)
#   svc &FF → init_vectors_and_copy (&8103)

label(0x80F6, "return_1")
label(0x81AB, "return_2")
label(0x82BE, "return_3")
label(0x8578, "return_4")
label(0x8D84, "return_5")
label(0x8E58, "return_6")
label(0x8EAF, "return_7")
label(0x9066, "return_8")
label(0x8D07, "return_9")
label(0x99E7, "return_10")

# --- Service call handlers ---

label(0x81B1, "svc_4_star_command")     # Svc 4 dispatch entry (mid-routine in svc_star_command)

# --- Trampoline JMPs near ADLC init (&9660-&966C) ---
label(0x9660, "trampoline_tx_setup")    # JMP c9be4 (TX control block setup)
label(0x9663, "trampoline_adlc_init")   # JMP adlc_init (&966F)
label(0x9666, "svc_12_nmi_release")        # Svc 12: JMP save_econet_state (&96CF)
label(0x9669, "svc_11_nmi_claim")          # Svc 11: JMP restore_econet_state (&96B4)
label(0x966C, "svc_5_unknown_irq")        # Svc 5: JMP c9b52 (unknown interrupt handler)
entry(0x9660)
entry(0x9663)

# --- Init and vector setup ---
# label at $8280 removed — fs_vector_addrs mapped to $8294 in 3.40

# --- FSCV handler and dispatch ---
# FSCV dispatches via table indices 20-27 (base Y=&13):
#   FSCV 0 (*OPT)               → index 20 → fscv_0_opt_entry (&89E8)
#   FSCV 1 (EOF)                → index 21 → fscv_1_eof
#   FSCV 2 (*/ run)             → index 22 → fscv_2_star_run (&8DCF)
#   FSCV 3 (unrecognised *)     → index 23 → fscv_3_star_cmd
#   FSCV 4 (*RUN)               → index 24 → fscv_2_star_run (&8DCF)
#   FSCV 5 (*CAT)               → index 25 → fscv_5_cat
#   FSCV 6 (shut down)          → index 26 → fscv_6_shutdown
#   FSCV 7 (read handles/info)  → index 27 → fscv_7_read_handles
#
# Extended dispatch table entries (indices 27-36):
# These appear to be used by FS reply processing and *NET sub-commands.
#   index 27 → fsreply_0_print_dir (&8D57)        (print directory path)
#   index 28 → fsreply_1_copy_handles_boot (&8E20) (copy handles + run boot command)
#   index 29 → fsreply_2_copy_handles (&8E21)          (copy handles only)
#   index 30 → fsreply_3_set_csd (&8E1A)        (update CSD handle)
#   index 31 → fsreply_4_notify_exec (&8DD5)       (send FS notify, execute response)
#   index 32 → fsreply_5_set_lib (&8E15)        (update library handle)
#
# *NET sub-commands (base Y=&21, indices 33-36):
#   *NET1 → index 33 → net_1_read_handle (&8E59)
#   *NET2 → index 34 → net_2_read_handle_entry (&8E5F)
#   *NET3 → index 35 → net_3_close_handle (&8E6F)
#   *NET4 → index 36 → net_4_resume_remote (&81B8)
# --- Filing system vector entry points ---
# Extended vector table entries set up at init (&831F):
#   FILEV → &86DE    ARGSV → &8907    BGETV → &852E
#   BPUTV → &83DC    GBPBV → &8A0E    FINDV → &896F
#   FSCV  → &80C7
# Labels and entry points for FSCV, FILEV, ARGSV, FINDV, GBPBV
# are created by subroutine() calls below in the comment sections.
label(0x855C, "bgetv_handler")          # BGETV entry: SEC then JSR handle_bput_bget
label(0x840F, "bputv_handler")          # BPUTV entry: CLC then fall into handle_bput_bget
entry(0x855C)
entry(0x840F)
entry(0x86D7)                            # Param block copy, falls through to parse_filename_gs
entry(0x8705)                            # Actual FILEV entry point (ROM pointer table target)

# --- Helper routines in header/init section ---
label(0x81DD, "cmd_name_matched")       # MATCH2: full name matched, check terminator byte
# 3.35K label skip_cmd_spaces ($81E4) — mapped to skpspi ($81E3) in 3.40
label(0x8335, "store_rom_ptr_pair")     # Write 2-byte address + ROM bank to ROM pointer table

# --- TX control block and FS command setup ---
label(0x83C4, "init_tx_ctrl_data")      # Init TX control block for data port (&90)
label(0x8385, "init_tx_ctrl_port")      # Init TX control block with port in A (2 JSR refs)
label(0x83B5, "prepare_cmd_with_flag")  # Prepare FS command with '*' flag and carry set
label(0x83B9, "prepare_cmd_clv")        # Prepare FS command with V cleared
# prepare_fs_cmd and build_send_fs_cmd labels created by subroutine() calls below.
label(0x83C4, "prepare_fs_cmd_v")       # Prepare FS command, V flag preserved
label(0x83EF, "send_fs_reply_cmd")      # Send FS command with reply processing

# --- Byte I/O and escape ---
# handle_bput_bget label created by subroutine() call below.
label(0x843A, "store_retry_count")      # RAND1: store retry count to &0FDD, initiate TX
label(0x8491, "update_sequence_return") # RAND3: update sequence numbers and pull A/Y/X/return
label(0x84FF, "set_listen_offset")      # NLISN2: use reply code as table offset for listen
label(0x851B, "send_to_fs_star")        # Send '*' command to fileserver
label(0x8543, "fs_wait_cleanup")        # WAITEX: tidy stack, restore rx_status_flags

# --- Pointer arithmetic helpers ---
label(0x87FC, "add_5_to_y")             # INY * 5; RTS
label(0x87FD, "add_4_to_y")             # INY * 4; RTS
label(0x880F, "sub_4_from_y")           # DEY * 4; RTS
label(0x8810, "sub_3_from_y")           # DEY * 3; RTS

# --- Error messages and data tables ---
label(0x81CE, "clear_osbyte_ce_cf")     # Reset OSBYTE &CE/&CF intercept masks to &7F (restore MOS vectors)

# --- * command forwarding and BYE ---

# --- Page &0F workspace (FS command buffer) ---
# NFS00 layout: BIGBUF=&0F00, TXBUF/RXBUF=&0F05, RXBUFE=&0FFF
#   &0F00 HDRREP: reply header / command type
#   &0F01 HDRFN:  function code
#   &0F02 HDRURD: URD handle slot
#   &0F03 HDRCSD/RXCC: CSD slot / RX control code
#   &0F04 HDRLIB/RXRC: LIB slot / RX return code
#   &0F05 TXBUF/RXBUF: start of TX/RX data area
#   &0FDC PUTB/PUTB1: single-byte random access buffer (4 bytes)
#   &0FDD PUTB2/GETB2: shared GET/PUT byte workspace
label(0x0F00, "fs_cmd_type")            # HDRREP: reply header / command type
label(0x0F01, "fs_cmd_y_param")         # HDRFN: function code
label(0x0F02, "fs_cmd_urd")             # HDRURD: URD handle slot
label(0x0F03, "fs_cmd_csd")             # HDRCSD: CSD handle / RX control code
label(0x0F04, "fs_cmd_lib")             # HDRLIB/RXRC: LIB slot / RX return code
label(0x0F05, "fs_cmd_data")            # TXBUF/RXBUF: start of TX/RX data area
label(0x0FDC, "fs_putb_buf")            # PUTB: single-byte random access buffer (4 bytes)
label(0x0FDD, "fs_getb_buf")            # PUTB2/GETB2: shared GET/PUT byte workspace

# ============================================================
# Filing system protocol client (&8501-&8700)
# ============================================================
# Core routines shared by all FS commands: argument saving,
# file handle conversion, number parsing/printing, TX/RX,
# file info display, and attribute decoding.

# --- Argument save and file handle conversion ---
label(0x85FA, "access_bit_table")       # Lookup table for attribute bit mapping (11 bytes)

# --- Decimal number parser (&85F3-&861B) ---
# parse_decimal label created by subroutine() call below.

# --- File handle ↔ bitmask conversion ---
label(0x8643, "handle_to_mask_a")       # TAY; CLC; fall into handle_to_mask
label(0x8644, "handle_to_mask_clc")     # CLC; fall into handle_to_mask (always convert)
# handle_to_mask and mask_to_handle labels created by subroutine() calls below.

# --- Number and hex printing ---
# 3.35K print_hex ($8D9D) and print_hex_nibble ($8DA8) — replaced by
# new routines at $9FE0/$9FE9 in 3.40

# --- Address comparison ---
# compare_addresses label created by subroutine() call below.
label(0x8673, "return_compare")          # Return from compare_addresses (not equal)

# --- FSCV 7: read FS handles ---
label(0x8674, "fscv_7_read_handles")      # Return X=&20 (base handle), Y=&27 (top handle)
label(0x8678, "return_fscv_handles")    # Return from fscv_7_read_handles

# --- FS flags manipulation ---
label(0x8683, "store_fs_flag")           # Shared STA fs_eof_flags / RTS for set/clear_fs_flag

# --- File info display (hex print helpers moved to &8Dxx) ---
label(0x8D45, "pad_filename_spaces")    # Pad filename display to 12 chars with spaces
label(0x8D58, "print_exec_and_len")     # Print exec address (4 bytes) and file length (3 bytes)
label(0x8D63, "print_hex_bytes")        # Print X bytes from (fs_options)+Y as hex (high->low)
label(0x8D6E, "print_space")            # Print a space character via OSASCI

# --- TX control and transmission ---
label(0x8691, "tx_poll_timeout")        # Transmit with Y=&60 (specified timeout)
# tx_poll_core label created by subroutine() call below.
label(0x86EB, "delay_1ms")              # MSDELY: 1ms delay loop (nested DEX/DEY)

# ============================================================
# File operations: FILEV, ARGSV, FINDV, GBPBV (&86B0-&8BB6)
# ============================================================
# The FS vector handlers for file I/O. Each handler saves
# args via save_fscv_args, processes the request by building
# FS commands and sending them to the fileserver, then restores
# args and returns via restore_args_return (&8952).

# --- FILEV handler (&86DE) and helpers ---

# --- FSCV 1: EOF handler (&884C) ---

# --- FILEV attribute dispatch (&8870) ---
label(0x88B7, "get_file_protection")  # CHA1: decode attribute byte for protection status
label(0x88CC, "copy_filename_to_cmd") # CHASK2: copy filename string into FS command buffer
label(0x8909, "copy_fs_reply_to_cb")  # COPYFS: copy FS reply buffer data to control block

# --- Common return point (&8952) ---
label(0x8955, "save_args_handle")      # SETARG: save handle for OSARGS operation

# --- FSCV 0: *OPT handler (&89CA) ---
label(0x89D6, "close_single_handle")   # CLOSE1: send close command for specific handle to FS

# --- Address adjustment helpers (&89EE-&8A0E) ---
label(0x8A0E, "adjust_addrs_9")        # Adjust 4-byte addresses at param block offset 9
label(0x8A13, "adjust_addrs_1")        # Adjust 4-byte addresses at param block offset 1
label(0x8A15, "adjust_addrs_clc")      # CLC entry: clear carry before address adjustment
label(0x8B3B, "copy_reply_to_caller") # Copy FS reply data to caller buffer (direct or via Tube)
label(0x8BCF, "tube_claim_loop")      # TCLAIM: claim Tube with &C3, retry until acquired

# ============================================================
# *-Command handlers and FSCV dispatch (&8BB6-&8E00)
# ============================================================
# FSCV 2/3/4 (unrecognised *) routes through fscv_3_star_cmd
# which matches against known FS commands before forwarding.
# The *CAT/*EX handlers display directory listings.
# *NET1-4 sub-commands manage file handles in local workspace.

# --- FSCV unrecognised * and command matching ---

# --- *EX and *CAT handlers ---

# --- Boot command strings and option tables ---
label(0x8CFB, "print_reply_bytes")
label(0x8CFD, "print_reply_counted")
label(0x8D79, "copy_string_from_offset") # COPLP1: sub-entry of copy_string_to_cmd with caller-supplied Y offset

# --- *NET sub-command handlers ---

# ============================================================
# Named labels for ADLC NMI handler routines
# ============================================================
# These replace auto-generated c/sub_ prefixed labels with
# descriptive names based on analysis of the NFS ROM's ADLC
# interaction and four-way handshake state machine.

# --- ADLC control (BRIAN entry points: NFS02) ---
# BRIANX=+&0000 (transmit), BRIANP=+&0003 (power up),
# BRIANC=+&0006 (relinquish NMI), BRIANQ=+&0009 (reclaim NMI),
# BRIANI=+&000C (unknown interrupt handler)

# --- RX scout reception (inbound) ---
label(0x971F, "scout_reject")          # Reject: wrong network (RX_DISCONTINUE)
label(0x9740, "scout_discard")         # Clean discard via &9A56
label(0x9748, "scout_loop_rda")        # Scout data loop: check RDA
label(0x9758, "scout_loop_second")     # Scout data loop: read second byte of pair
label(0x9793, "scout_no_match")        # Scout port/station mismatch (3 refs)
label(0x9796, "scout_match_port")      # Port non-zero: look for matching RX block

# --- Data frame RX (inbound four-way handshake) ---
label(0x9815, "data_rx_setup")         # Switch to RX mode, install data RX handler
label(0x9837, "nmi_data_rx_net")       # Data frame: validate dest_net = 0
label(0x984D, "nmi_data_rx_skip")      # Data frame: skip ctrl/port (already from scout)
label(0x987A, "rx_error")              # RX error dispatcher (13 refs -- most referenced!)
label(0x987A, "rx_error_reset")        # Full reset and discard
label(0x98DD, "nmi_data_rx_tube")      # Data frame: Tube co-processor variant

# --- Data frame completion and FV validation ---
label(0x9919, "data_rx_tube_complete") # Tube data frame completion
label(0x9916, "data_rx_tube_error")    # Tube data frame error (3 refs)

# --- ACK transmission ---
label(0x994F, "ack_tx_configure")      # Configure CR1/CR2 for TX
label(0x995D, "ack_tx_write_dest")     # Write dest addr to TX FIFO

# --- Discard and idle ---

# --- TX path ---
label(0x9C6B, "tx_active_start")       # Begin TX (CR1=&44)
label(0x9D53, "tx_error")              # TX error path

# --- RX reply scout (outbound handshake) ---
# 3.35K label reply_error ($9DED) — mapped to tx_result_fail ($9F1A) in 3.40

# --- TX scout ACK + data phase ---
label(0x9E1A, "data_tx_begin")         # Begin data frame TX
label(0x9E5C, "data_tx_last")          # TX_LAST_DATA for data frame (5 refs)
label(0x9E6D, "data_tx_error")         # Data TX error (5 refs)
label(0x9E78, "install_saved_handler") # Install handler from &0D4B/&0D4C
label(0x9E81, "nmi_data_tx_tube")      # NMI: send data from Tube

# --- Four-way handshake: RX final ACK ---
label(0x9EDC, "nmi_final_ack_net")     # Read dest_net, validate

# --- Completion and error ---
label(0x9F1A, "tx_result_fail")        # Store result=&41 (not listening) (9 refs)

# --- NMI shim at end of ROM ---
label(0x9FA7, "nmi_shim_rom_src")      # Source for 32-byte copy to &0D00
# label(0x9FFA, "rom_nmi_tail") — removed: truncated code at ROM end

# ============================================================
# Labels from DNFS 3.60 source correspondence
# ============================================================
# These labels were identified by opcode fingerprint matching between
# the NFS 3.34 ROM and the original Acorn DNFS 3.60 source code
# (NFS00-NFS13). Each replaces a py8dis auto-generated label with
# the name used in the Acorn reference source.

# --- Relocated Tube code (pages 4-6) ---
# 3.35K labels begink ($04AE), beginr ($04BA) — Tube code rewritten
label(0x0586, "strnh")                # NFS13: string handling
label(0x05A6, "mj")                   # NFS13: conditional jump
label(0x05AB, "argsw")                # NFS13: OSARGS workspace
label(0x0604, "bytex")                # NFS13: byte transfer

# --- Service call init (&80xx) ---
label(0x815B, "cloop")                # NFS01: copy loop (page copy)
label(0x81F8, "initl")                # NFS01: init loop
label(0x81E3, "skpspi")               # NFS01: skip SPI

# --- FS command dispatch (&82xx-&83xx) ---
label(0x824C, "dofsl1")               # NFS03: do FS loop 1
label(0x834F, "fsdiel")               # NFS01: FS die loop
label(0x8394, "fstxl1")               # NFS03: FS TX loop 1
label(0x83A4, "fstxl2")               # NFS03: FS TX loop 2
label(0x83F7, "dofsl7")               # NFS03: do FS loop 7
label(0x8403, "return_dofsl7")        # NFS03: return from FS loop 7
label(0x8404, "dofsl5")               # NFS03: do FS loop 5
label(0x844B, "error1")               # NFS03: error handler 1

# --- Net list / pointer arithmetic (&84xx-&85xx) ---
label(0x84FB, "nlistn")               # NFS03: net list entry
label(0x84FD, "nlisne")               # NFS03: net list next entry
label(0x8530, "incpx")                # NFS04: increment pointer X
label(0x864D, "y2fsl5")               # NFS04: Y-to-FS loop 5
label(0x8653, "y2fsl2")               # NFS04: Y-to-FS loop 2
label(0x8662, "fs2al1")               # NFS04: FS-to-A loop 1

# --- Number formatting and file info (&86xx) ---
label(0x8D65, "num01")                # NFS07: number print entry
label(0x86AD, "l4")                   # NFS03: net TX polling loop
label(0x86D9, "file1")                # NFS05: FILEV entry 1
label(0x86EB, "quote1")               # NFS05: filename quote loop
label(0x8716, "loadop")               # NFS05: load operation
label(0x8731, "lodfil")               # NFS05: load file

# --- FILEV, load/save size (&87xx) ---
label(0x8754, "floop")                # NFS01: FS loop
label(0x877E, "lodchk")               # NFS05: load check
label(0x8789, "return_lodchk")        # NFS05: return from load check
label(0x878A, "saveop")               # NFS05: save operation
label(0x8793, "savsiz")               # NFS05: save size handling
label(0x87F2, "lodrl1")               # NFS05: load reply loop 1
label(0x8805, "lodrl2")               # NFS05: load reply loop 2
label(0x8837, "savchk")               # NFS05: save check

# --- Channel/attribute handling (&88xx-&89xx) ---
label(0x88AA, "chalp1")               # NFS05: channel loop 1
label(0x88C1, "chalp2")               # NFS05: channel loop 2
label(0x88D3, "cha6")                  # NFS05: channel handler 6
label(0x88E2, "cha4")                  # NFS05: channel handler 4
label(0x88EC, "cha5")                  # NFS05: channel handler 5
label(0x8916, "cha5lp")               # NFS05: channel 5 loop
label(0x8984, "osarg1")               # NFS05: OSARGS handler 1
label(0x89FA, "opter1")               # NFS05: *OPT error 1
label(0x89FF, "optl1")                # NFS05: *OPT loop 1

# --- GBPB handler (&89xx-&8Axx) ---
label(0x8A27, "gbpbx")                # NFS05: GBPB dispatch
label(0x8A5E, "gbpbx0")               # NFS05: GBPB dispatch 0
label(0x8A3C, "gbpbx1")               # NFS05: GBPB dispatch 1
label(0x8A47, "gbpbe1")               # NFS05: GBPB EOF 1
label(0x8A53, "gbpbf1")               # NFS05: GBPB forward 1
label(0x8A5E, "gbpbf2")               # NFS05: GBPB forward 2
label(0x8A67, "gbpbl1")               # NFS05: GBPB loop 1
label(0x8A89, "gbpbl3")               # NFS05: GBPB loop 3
label(0x8AA0, "gbpbf3")               # NFS05: GBPB forward 3

# --- *INFO and decimal print (&8Axx-&8Bxx) ---
label(0x8AFD, "info2")                # NFS06: *INFO loop 2
label(0x8B62, "tbcop1")               # NFS06: Tube copy loop 1
label(0x8BE0, "decfir")               # NFS07: decimal first digit
label(0x8BE2, "decmor")               # NFS07: decimal more digits
label(0x8BEE, "decmin")               # NFS07: decimal minimum

# --- Logon and *NET (&8Dxx) ---
label(0x8E2F, "logon2")               # NFS07: logon handler 2
label(0x8EB7, "logon3")               # NFS07: logon handler 3
label(0x8D8B, "print_dir_from_offset") # INFOLP: sub-entry of fsreply_0_print_dir with caller-supplied X offset
label(0x8D75, "infol2")               # NFS07: info loop 2

# --- File I/O: save, read, open (&8Dxx-&8Fxx) ---
label(0x8E6A, "rxpol2")               # NFS08: RX poll loop 2
label(0x8EA2, "save1")                # NFS08: save handler 1
label(0x8EB3, "copyl3")               # NFS08: copy loop 3
label(0x8EF4, "readry")               # NFS08: read ready
label(0x8F23, "rssl1")                # NFS08: read size/status loop 1
label(0x8F2E, "rssl2")                # NFS08: read size/status loop 2
label(0x8F3E, "rsl1")                 # NFS08: read status loop 1
label(0x8F68, "readc1")               # NFS08: read char 1
label(0x8F85, "scan0")                # NFS08: scan entry 0
label(0x8F99, "scan1")                # NFS08: scan entry 1
label(0x8FB5, "openl6")               # NFS08: open loop 6
label(0x8FC2, "openl7")               # NFS08: open loop 7
label(0x8FC7, "openl4")               # NFS08: open loop 4
# 3.35K label rest1 ($8FC1) — data block removed in 3.40
label(0x8FEE, "dofs01")               # NFS08: do FS 01
label(0x9067, "dofs2")                # NFS08: do FS 2

# --- OSWORD and remote ops (&90xx-&91xx) ---
label(0x9088, "entry1")               # NFS09: OSWORD entry 1
label(0x9100, "nbyte6")               # NFS09: net byte handler 6
label(0x9102, "nbyte1")               # NFS09: net byte handler 1
label(0x9124, "nbyte4")               # NFS09: net byte handler 4
label(0x9128, "nbyte5")               # NFS09: net byte handler 5
label(0x912F, "return_nbyte")         # NFS09: return from net byte handler
label(0x84A3, "remot1")               # NFS03: remote handler 1
label(0x9181, "cbset2")               # NFS09: control block set 2
label(0x9198, "cbset3")               # NFS09: control block set 3
label(0x919E, "cbset4")               # NFS09: control block set 4
label(0x91DB, "setup1")               # NFS09: setup 1
label(0x91DE, "return_printer_select") # NFS09: return from printer_select_handler
label(0x91EE, "prlp1")                # NFS09: printer loop 1

# --- Broadcast/station search (&92xx) ---
label(0x926D, "bsxl1")                # NFS09: broadcast search loop 1
label(0x928A, "bspsx")                # NFS09: broadcast search parse exit
label(0x9292, "bsxl0")                # NFS09: broadcast search loop 0
label(0x92A5, "return_bspsx")         # NFS09: return from broadcast search area

# ============================================================
# File header / overview comment (placed at &8000, first in code)
# ============================================================
comment(0x8000, """\
NFS ROM 3.34B disassembly (Acorn Econet filing system)

NMI handler architecture
========================
The NFS ROM uses self-modifying code to implement a state
machine for ADLC communication. An NMI workspace shim is
copied to &0D00 at init.

NMI entry (&0D00):
  BIT &FE18       ; INTOFF -- immediately disable further NMIs
  PHA / TYA / PHA ; save A, Y
  LDA #$nn        ; page in NFS ROM bank (self-modified)
  STA &FE30
  JMP $xxxx       ; self-modifying target at &0D0C/&0D0D

set_nmi_vector (&0D0E): stores A->&0D0C (low), Y->&0D0D (high)
  Falls through to nmi_rti.

nmi_rti (&0D14):
  LDA &F4         ; restore original ROM bank
  STA &FE30
  PLA / TAY / PLA ; restore Y, A
  BIT &FE20       ; INTON -- re-enable NMIs
  RTI

NMI handler chain for outbound TX (four-way handshake):
  &9700: RX scout (idle listen, default handler)
  &9C57: INACTIVE polling (pre-TX, waits for idle line)
  &9D5B: TX data (2 bytes per NMI, tight loop if IRQ persists)
  &9D97: TX_LAST_DATA (close frame)
  &9DA3: TX completion (switch to RX: CR1=&82)
  &9DC1: RX reply scout (check AP, read dest_stn)
  &9DD7: RX reply continuation (read dest_net, validate)
  &9DF2: RX reply validation (read src_stn/net, check FV)
  &9E24: TX scout ACK (write dest/src addr, TX_LAST_DATA)
  &9EEC: Four-way handshake data phase

NMI handler chain for inbound reception (scout -> data):
  &9700: RX scout (idle listen)
  &971F: RX scout second byte (dest_net, install &9747)
  &9747: Scout data loop (read body in pairs, detect FV)
  &977B: Scout completion (disable PSE, read last byte)
  &9968: TX scout ACK
  &9843: RX data frame (AP check, validate dest_stn/net)
  &9859: RX data frame (validate src_net=0)
  &986F: RX data frame (skip ctrl/port bytes)
  &98A4: RX data bulk read (read payload into buffer)
  &98D8: RX data completion (disable PSE, check FV, read last)
  &9968: TX final ACK

Key ADLC register values:
  CR1=&C1: full reset (TX_RESET|RX_RESET|AC)
  CR1=&82: RX listen (TX_RESET|RIE)
  CR1=&44: TX active (RX_RESET|TIE)

  CR2 values (all set FC_TDRA|2_1_BYTE|PSE):
  &67: clear status  CLR_TX_ST|CLR_RX_ST
  &E7: TX prepare    RTS|CLR_TX_ST|CLR_RX_ST
  &3F: TX last data  CLR_RX_ST|TX_LAST_DATA|FLAG_IDLE
  &A7: TX handshake  RTS|CLR_TX_ST""")

# ============================================================
# Dispatch table at &8020 (low bytes) / &8044 (high bytes)
# ============================================================
# Used via the PHA/PHA/RTS dispatch trick at &80E7.
#
# This is a standard 6502 computed-jump technique. The table stores
# handler addresses minus 1, split into separate low-byte and high-byte
# arrays. The dispatcher pushes the high byte then the low byte onto
# the stack; RTS pops them and jumps to (address + 1).
#
# Multiple callers share this single table using different base offsets
# in Y. The dispatch loop at &80E7 adds Y+1 to X (the command index),
# so each caller maps its index into a different region of the table:
#
#   Caller              Y (base)  X (index)         Table indices
#   ─────────────────   ────────  ────────────────  ─────────────
#   Service calls        &00      svc_num            0-13
#   Language entry       &0E      reason             14-18
#   FSCV                 &13      fscv_code          19-26
#   FS reply             &17      reply_code         27-32
#   *NET1-4 commands     &21      char-'1'           33-36
#
# The dispatch code at &80EC/&80F0 reads via LDA dispatch_hi,X and
# LDA dispatch_lo,X. After the loop adds Y+1 to X, the final byte
# addresses for logical entry i are:
#   lo = &8024 + (i+1) = &8025 + i
#   hi = &8049 + (i+1) = &804A + i
#
# In older NFS versions (3.34-3.35K), the tables start at &8020/&8044
# so rts_code_ptr(0x8020+i, 0x8044+i) works directly. In 3.40 the
# ROM title is 4 bytes longer ("    NET" vs "NET"), so ROM header
# data extends to &8023 and the tables start at &8024/&8049.
#
# The lo and hi sub-tables overlap: lo bytes for the last 6
# entries (i=31-36) fall at &8044-&8049 (the start of the hi area),
# and hi bytes for i=31-36 are at &8069-&806E (between the main
# dispatch_hi table and dispatch_net_cmd at &806F).
#
# Index 0 and unused indices point to an RTS (null handler), so
# unrecognised service calls or out-of-range values fall through
# harmlessly.

# Error message offset table (9 entries, indices 0-8).
# The copyright null terminator doubles as entry 0.
# Indexed by TXCB status: AND #7 for codes 0-7, or hardcoded 8.
# Each value is a Y offset into error_msg_table; the code loads
# error_msg_table,Y to copy the selected error string.
comment(0x8018, """\
Error message offset table (9 entries).
Each byte is a Y offset into error_msg_table.
Entry 0 (Y=0, "Line Jammed") doubles as the
copyright string null terminator.
Indexed by TXCB status (AND #7), or hardcoded 8.""")
comment(0x8018, '"Line Jammed"', inline=True)
for addr in range(0x8019, 0x8021):
    byte(addr)
comment(0x8019, '"Net Error"', inline=True)
comment(0x801A, '"Not listening"', inline=True)
comment(0x801B, '"No Clock"', inline=True)
comment(0x801C, '"Escape"', inline=True)
comment(0x801D, '"Escape"', inline=True)
comment(0x801E, '"Escape"', inline=True)
comment(0x801F, '"Bad Option"', inline=True)
comment(0x8020, '"No reply"', inline=True)

# Unreferenced padding between error offsets and dispatch table.
# &8024 is the dispatch_lo pad byte — the dispatcher adds Y+1
# to X before indexing, so entry 0 at &8025 is the first handler.
for addr in range(0x8021, 0x8025):
    byte(addr)
comment(0x8021, "Purpose unknown", inline=True)
comment(0x8022, "Purpose unknown", inline=True)
comment(0x8023, "Purpose unknown", inline=True)
comment(0x8024, "Purpose unknown; ignored by dispatcher", inline=True)

# Null handler and service call handlers (indices 0-13)
for i in range(0, 14):
    rts_code_ptr(0x8025 + i, 0x804A + i)

# Language entry handlers (indices 14-18, base Y=&0E)
for i in range(14, 19):
    rts_code_ptr(0x8025 + i, 0x804A + i)

# FSCV handlers (indices 19-26, codes 0-7, base Y=&13)
for i in range(19, 27):
    rts_code_ptr(0x8025 + i, 0x804A + i)

# FS reply handlers (indices 27-30)
# Dispatched by forward_star_cmd with base Y=&17 using the
# fileserver's reply code as the index.
for i in range(27, 31):
    rts_code_ptr(0x8025 + i, 0x804A + i)

# Entries 31-36: overlap zone. Lo bytes are at &8044-&8049 (start
# of dispatch_hi area), hi bytes are at &8069-&806E (between the
# main dispatch_hi table and dispatch_net_cmd at &806F).
for i in range(31, 37):
    rts_code_ptr(0x8025 + i, 0x804A + i)
comment(0x8044, "FS reply: notify + execute", inline=True)
comment(0x8045, "FS reply: set library handle", inline=True)
comment(0x8046, "*NET1: read handle from packet", inline=True)
comment(0x8047, "*NET2: read handle from workspace", inline=True)
comment(0x8048, "*NET3: close handle", inline=True)
comment(0x8049, "*NET4: resume remote", inline=True)

# ============================================================
# Filing system OSWORD dispatch table at &8EB0/&8EB5
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &8E80 (entered from svc_8_osword).
# svc_8_osword subtracts &0F from the command code in &EF, giving a
# 0-4 index for OSWORD calls &0F-&13 (15-19).
#
# Index  OSWORD  Target   Purpose
# ─────  ──────  ───────  ────────────────────────────
#   0      &0F   &8EBA    Protection/status control
#   1      &10   &8F74    RX block read/setup
#   2      &11   &8ED4    Data block copy
#   3      &12   &8EF9    FS server station lookup
#   4      &13   &8FE8    Econet TX/RX handler
for i in range(5):
    rts_code_ptr(0x8EB0 + i, 0x8EB5 + i)

# ============================================================
# NMI handler chain entry points
# ============================================================
# These are installed via self-modifying JMP at &0D0C/&0D0D,
# so py8dis cannot trace them automatically.

# --- ADLC init and idle listen ---
entry(0x96EC)   # ADLC init / reset entry
entry(0x96F2)   # RX scout (idle listen) - default NMI handler

# --- TX path: polling, data, completion ---
entry(0x9C2F)   # INACTIVE polling loop (pre-TX)
entry(0x9D2D)   # NMI TX data handler (2 bytes per NMI)
entry(0x9D53)   # TX error path
entry(0x9D69)   # TX_LAST_DATA and frame completion
entry(0x9D75)   # TX completion: switch to RX mode

# --- RX reply handlers ---
entry(0x9D93)   # RX reply scout handler
entry(0x9DA9)   # RX reply continuation handler
entry(0x9DC2)   # RX reply next handler

# --- Four-way handshake (outbound data phase) ---
entry(0x9EBA)   # Four-way handshake: switch to RX for final ACK
entry(0x9EC6)   # Four-way handshake: RX final ACK (check AP, dest_stn)
entry(0x9EDC)   # Four-way handshake: RX final ACK continuation (dest_net=0)

# --- Completion / error ---
entry(0x9F16)   # Completion handler (store result=0 to tx_block)
entry(0x9F1C)   # Error handler (store error code to tx_block)
entry(0x9EF2)   # Four-way handshake: validate final ACK src addr

# --- Discovered via JMP &0D0E scan (NMI handler installations) ---
entry(0x9711)   # RX scout second byte handler (dest network)
entry(0x9743)   # Scout data reading loop (reads body in pairs)
entry(0x9821)   # Data frame RX handler (four-way handshake)
entry(0x9837)   # Data frame: validate source network = 0
entry(0x984D)   # Data frame: skip ctrl/port bytes
entry(0x9880)   # Data frame: bulk data read loop
entry(0x98DD)   # Data frame: Tube co-processor RX handler
entry(0x997B)   # ACK TX continuation (write src addr, TX_LAST_DATA)

# --- NMI shim at end of ROM (&9FD9-&9FFF) ---
# Bootstrap NMI handler and ROM copies of workspace routines.
# &9FD9 is the source for the 32-byte copy to &0D00 by install_nmi_shim.
entry(0x9FA8)   # Bootstrap NMI entry (hardcoded JMP nmi_rx_scout, no self-mod)
entry(0x9FB6)   # ROM copy of set_nmi_vector + nmi_rti
# entry(0x9FFA) — removed: code at $9FFA runs off ROM end ($9FFF STA truncated)

# --- Data RX NMI handlers (four-way handshake data phase) ---
entry(0x9E0A)   # Data phase RX first byte
entry(0x9E2F)   # Data phase RX continuation
entry(0x9E81)   # Data phase RX bulk transfer

# ============================================================
# Additional known entry points
# ============================================================
entry(0x8228)
entry(0x8247)
entry(0x8249)
entry(0x81AC)   # Auto-boot/service handler (NOP pad + LDX #&0C; JSR)
entry(0x8280)   # Issue vectors claimed handler (JSR osbyte)
entry(0x836D)   # TX control block string copy loop tail
entry(0x8674)   # FSCV read handles (LDX #&20; LDY #&27; RTS)
entry(0x8CF4)   # Boot option dispatch (PLA; CLC; ADC zp)
entry(0x8DCF)   # fscv_2_star_run: FSCV 2/4 handler (JSR parse_filename_gs)
entry(0x8E59)   # Read handle entry (LDY #&6F; LDA (nfs_workspace),Y)
entry(0x919C)   # Control block setup loop tail
entry(0x9310)   # Read VDU OSBYTE (JSR osbyte; TXA; LDX #0)
entry(0x9669)   # NMI claim trampolines (JMP; JMP)
entry(0x966C)   # svc_5_unknown_irq: JMP to IRQ service
entry(0x99E8)   # Econet RX immediate-operation handler
entry(0x9AFC)   # ACK/reply handler: store source station, configure VIA
entry(0x9B35)   # IRQ service: check CB1, dispatch TX done handlers

# ============================================================
# Code regions identified by manual inspection of equb data
# ============================================================
# These are preceded by RTS and start with valid opcodes, but
# are not reachable via JSR/JMP from already-traced code (their
# callers are themselves in equb regions -- cascading resolution).

entry(0x87FC)   # INY*5; RTS (pointer arithmetic helper)
entry(0x880F)   # DEY*4; RTS (pointer arithmetic helper)
entry(0x8814)   # PHA; JSR ... (called from &878A and &8A6C)
entry(0x888D)   # STA abs; CMP#; ... (called from &8744)
entry(0x897C)   # TAY; BNE; ... (preceded by RTS, standalone entry)
entry(0x8A2E)   # JSR &85A6; ... (preceded by RTS, standalone entry)
# entry(0x8E34) created by subroutine() call below
entry(0x90DE)   # LDY zp; CMP#; ... (preceded by RTS, standalone entry)
entry(0x99C5)   # Post-ACK: process received scout (check port, match RX block)

# --- Econet TX/RX handler and OSWORD dispatch (&8FE5-&90B8) ---
# &8FE5: Main transmit/receive handler entry (A=0: set up and send, A>=1: handle result)
# &9074: OSWORD-style dispatch handler (function codes 0-8, PHA/PHA/RTS)
entry(0x8FE8)   # Econet TX/RX handler (CMP #1; BCS)
# entry(0x9008) and entry(0x903E) created by subroutine() calls below
entry(0x908F)   # Dispatch trampoline (PHA/PHA/RTS into table at &9098/&90A1)

# Dispatch table at &909A (low bytes) / &90A3 (high bytes)
# 9 entries for function codes 0-8, used via PHA/PHA/RTS at &908F.
for i in range(9):
    rts_code_ptr(0x909A + i, 0x90A3 + i)

# ============================================================
# Immediate operation dispatch table at &9A04/&9A0C
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9A56 (immediate_op handler).
# Y = rx_ctrl (&81-&88), so table entries are at base+&81..base+&88.
# The control byte determines the remote operation type:
#
# Y   Operation   Target
# ──   ─────────   ──────
# &81  PEEK        &9AD1
# &82  POKE        &9AB3
# &83  JSR         &9A95
# &84  UserProc    &9A95
# &85  OSProc      &9A95
# &86  HALT        &9AEB
# &87  CONTINUE    &9AEB
# &88  (machine type query)  &9ABE
for y in range(0x81, 0x89):
    rts_code_ptr(0x9A04 + y, 0x9A0C + y)

# ============================================================
# TX completion dispatch table at &9AF1/&9AF6
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9B6B.
# Y = tx_work_57 (the Econet operation type being sent).
# The dispatch is reached both by Y >= &86 (via BCS at &9B5E)
# and by Y < &86 (falls through from &9B68 after saving
# prot_status). Table entries for Y=&81/&82 overlap with the
# PHA/RTS code itself and are not valid — those operation types
# (PEEK/POKE) are response-only and never initiated via TX.
#
# Y   Operation   Target
# ──   ─────────   ──────
# &83  JSR         &9B7E  (remote JSR initiation)
# &84  UserProc    &9B87  (user procedure initiation)
# &85  OSProc      &9B95  (OS procedure initiation)
# &86  HALT        &9BA1  (HALT completion)
# &87  CONTINUE    &9BB8  (CONTINUE completion)
for y in range(0x83, 0x88):
    rts_code_ptr(0x9AF1 + y, 0x9AF6 + y)

# ============================================================
# TX ctrl byte dispatch table at &9C62/&9C6A
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9CCB.
# Y = tx_ctrl_byte (&81-&88), selects the transmit handler for
# each Econet operation type.
#
# Y   Target
# ──   ──────
# &81  &9CF7
# &82  &9CFB
# &83  &9D1A  (JSR/UserProc/OSProc share handler)
# &84  &9D1A
# &85  &9D1A
# &86  &9D54  (HALT/CONTINUE share handler)
# &87  &9D54
# &88  &9CF3
for y in range(0x81, 0x89):
    rts_code_ptr(0x9C3A + y, 0x9C42 + y)

# ============================================================
# Immediate operation RX handler labels (&9AB5-&9AF1)
# ============================================================
# Targets of dispatch table 1 at &9A24/&9A2C.
# These handle incoming immediate operations (PEEK, POKE, JSR,
# UserProc, OSProc, machine type query) received from the network.

label(0x9A95, "rx_imm_exec")
subroutine(0x9A95, hook=None,
    title="RX immediate: JSR/UserProc/OSProc setup",
    description="""\
Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace at &0D58, then jumps to
the common receive path at c9826. Used for operation types
&83 (JSR), &84 (UserProc), and &85 (OSProc).""")

label(0x9AB3, "rx_imm_poke")
subroutine(0x9AB3, hook=None,
    title="RX immediate: POKE setup",
    description="""\
Sets up workspace offsets for receiving POKE data.
port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
the common data-receive path at c9805.""")

label(0x9ABE, "rx_imm_machine_type")
subroutine(0x9ABE, hook=None,
    title="RX immediate: machine type query",
    description="""\
Sets up a buffer at &7F21 (length #&01FC) for the machine
type query response, then jumps to the query handler at
c9b0f. Returns system identification data to the remote
station.""")

label(0x9AD1, "rx_imm_peek")
subroutine(0x9AD1, hook=None,
    title="RX immediate: PEEK setup",
    description="""\
Writes &0D3D to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send the
PEEK response data back to the requesting station.
Rewritten in 3.40 to use workspace offsets (&A6/&A7)
instead of saving/restoring nmi_tx_block (&A0/&A1).""")

# ============================================================
# TX completion handler labels (&9BAA-&9BEC)
# ============================================================
# Targets of dispatch table 2 at &9B1D/&9B22.
# Called when an outbound immediate operation TX completes.

label(0x9B7E, "tx_done_jsr")
subroutine(0x9B7E, hook=None,
    title="TX done: remote JSR execution",
    description="""\
Pushes address &9BEB on the stack (so RTS returns to
tx_done_exit), then does JMP (l0d58) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")

label(0x9B87, "tx_done_user_proc")
subroutine(0x9B87, hook=None,
    title="TX done: UserProc event",
    description="""\
Generates a network event (event 8) via OSEVEN with
X=l0d58, A=l0d59 (the remote address). This notifies
the user program that a UserProc operation has completed.""")

label(0x9B95, "tx_done_os_proc")
subroutine(0x9B95, hook=None,
    title="TX done: OSProc call",
    description="""\
Calls the ROM entry point at &8000 (rom_header) with
X=l0d58, Y=l0d59. This invokes an OS-level procedure
on behalf of the remote station.""")

label(0x9BA1, "tx_done_halt")
subroutine(0x9BA1, hook=None,
    title="TX done: HALT",
    description="""\
Sets bit 2 of rx_flags (&0D64), enables interrupts, and
spin-waits until bit 2 is cleared (by a CONTINUE from the
remote station). If bit 2 is already set, skips to exit.""")

label(0x9BB8, "tx_done_continue")
subroutine(0x9BB8, hook=None,
    title="TX done: CONTINUE",
    description="""\
Clears bit 2 of rx_flags (&0D64), releasing any station
that is halted and spinning in tx_done_halt.""")

label(0x9BC0, "tx_done_exit")

# ============================================================
# TX ctrl byte handler labels (&9CF7-&9D54)
# ============================================================
# Targets of dispatch table 3 at &9C62/&9C6A.
# Called to set up the scout control byte and transfer
# parameters for outbound immediate operations.

label(0x9CCF, "tx_ctrl_peek")
subroutine(0x9CCF, hook=None,
    title="TX ctrl: PEEK transfer setup",
    description="""\
Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace at &0D1E-&0D21 (with carry propagation).
Calls tx_calc_transfer to finalise, then exits via
tx_ctrl_exit.""")

label(0x9CD3, "tx_ctrl_poke")
subroutine(0x9CD3, hook=None,
    title="TX ctrl: POKE transfer setup",
    description="""\
Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")

label(0x9CE7, "tx_ctrl_proc")
subroutine(0x9CE7, hook=None,
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="""\
Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

label(0x9D26, "tx_ctrl_exit")

# Alternate entry into ctrl_block_setup (&9171)
entry(0x9173)   # ADLC setup: LDX #&0D; LDY #&7C; BIT &833B; BVS c9167

# Dispatch targets found in equb data regions
# These are the bodies of the econet function dispatch handlers.
# Functions 1-3 share a handler (&91D4) — possibly different
# sub-operations that share setup logic. Function 5 (&91C4) and
# function 8 (&9142) are distinct. The exact purpose of each
# function code hasn't been fully determined yet.
entry(0x91DF)   # Function 1/2/3 handler (shared)
entry(0x9150)   # Function 8 handler (remote_cmd_data)

# --- Code found in third-pass remaining equb regions ---
entry(0x878A)   # BEQ +3; JMP &8870 (called from &8744 region)
entry(0x8FCD)   # LDY #&28; ... (preceded by RTS, standalone entry)
entry(0x9815)   # LDA #&82; STA &FEA0; installs NMI handler &9843

# ============================================================
# Inline comments for key instructions
# ============================================================
# Note: acorn.bbc()'s hooks auto-annotate OSBYTE/OSWORD calls, so
# we only add comments where the auto-annotations don't reach.

# ============================================================
# Save FSCV arguments (&859C)
# ============================================================
entry(0x85C8)
subroutine(0x85C8, "save_fscv_args_with_ptrs", hook=None,
    title="Save FSCV arguments with text pointers",
    description="""\
Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
falls through to save_fscv_args to store A/X/Y in the FS
workspace.""")

subroutine(0x85D2, "save_fscv_args", hook=None,
    title="Save FSCV/vector arguments",
    description="""\
Stores A, X, Y into the filing system workspace. Called at the
start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
  &BD (fs_last_byte_flag) = A (function code / command)
  &BB (fs_options)        = X (control block ptr low)
  &BC (fs_block_offset)   = Y (control block ptr high)
  &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)""")

# ============================================================
# Attribute decoding (&85B1 / &85BB)
# ============================================================
subroutine(0x85DD, "decode_attribs_6bit", hook=None,
    title="Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)",
    description="""\
Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&85CE. The two formats use different bit layouts for file
protection attributes.""")

subroutine(0x85E7, "decode_attribs_5bit", hook=None,
    title="Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)",
    description="""\
Masks A to 5 bits and builds an access bitmask via the
lookup table at &85CE. Each input bit position maps to a
different output bit via the table. The conversion is done
by iterating through the source bits and OR-ing in the
corresponding destination bits from the table, translating
between BBC (8-bit) and fileserver (5-bit) protection formats.""")

# skip_spaces (&854D in 3.34B) was removed in 3.35D; its functionality
# was integrated into the new inline station number parser at &807D.

# ============================================================
# Decimal number parser (&85F3)
# ============================================================
subroutine(0x861D, "parse_decimal",
    title="Parse decimal number from (fs_options),Y (DECIN)",
    description="""\
Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
then ADC &B2 gives x10.
Terminates on "." (pathname separator), control chars, or space.
The delimiter handling was revised to support dot-separated path
components (e.g. "1.$.PROG") -- originally stopped on any char
>= &40 (any letter), but the revision allows numbers followed
by dots.""",
    on_entry={"y": "offset into (fs_options) buffer"},
    on_exit={"a": "parsed value (accumulated in &B2)",
             "x": "corrupted",
             "y": "offset past last digit parsed"})

# ============================================================
# File handle conversion (&861B-&861D)
# ============================================================
subroutine(0x8645, "handle_to_mask",
    title="Convert file handle to bitmask (Y2FS)",
    description="""\
Converts fileserver handles to single-bit masks segregated inside
the BBC. NFS handles occupy the &20-&27 range (base HAND=&20),
which cannot collide with local filing system or cassette handles
-- the MOS routes OSFIND/OSBGET/OSBPUT to the correct filing
system based on the handle value alone. The power-of-two encoding
allows the EOF hint byte to track up to 8 files simultaneously
with one bit per file, and enables fast set operations (ORA to
add, EOR to toggle, AND to test) without loops. Handle 0 passes
through unchanged (means "no file"). The bit-shift conversion loop
has a built-in validity check: if the handle is out of range, the
repeated ASL shifts all bits out, leaving A=0, which is converted
to Y=&FF as a sentinel -- bad handles fail gracefully rather than
indexing into garbage.
Three entry points: &861D (direct), &861C (CLC first), &861B (TAY first).""",
    on_entry={"y": "handle number",
              "c": "0: convert, 1 with Y=0: skip, 1 with Y!=0: convert"},
    on_exit={"a": "preserved",
             "x": "preserved",
             "y": "bitmask (single bit set) or &FF if handle invalid"})

# ============================================================
# Mask to handle (&8638)
# ============================================================
subroutine(0x8660, "mask_to_handle",
    title="Convert bitmask to handle number (FS2A)",
    description="""\
Inverse of Y2FS. Converts from the power-of-two FS format
back to a sequential handle number by counting right shifts
until A=0. Adds &1E to convert the 1-based bit position to
a handle number (handles start at &1F+1 = &20). Used when
receiving handle values from the fileserver in reply packets.""",
    on_entry={"a": "single-bit bitmask"},
    on_exit={"a": "handle number (&20-&27)",
             "x": "corrupted",
             "y": "preserved"})

# ============================================================
# Print decimal number (&8D7E)
# ============================================================
subroutine(0x8DB0, "print_decimal", hook=None,
    title="Print byte as 3-digit decimal number",
    description="""\
Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""",
    on_entry={"a": "byte value to print"},
    on_exit={"a": "last digit character",
             "x": "corrupted",
             "y": "0 (remainder after last division)"})

subroutine(0x8DBD, "print_decimal_digit", hook=None,
    title="Print one decimal digit by repeated subtraction",
    description="""\
Divides Y by A using repeated subtraction. Prints the
quotient as an ASCII digit ('0'-'9') via OSASCI. Returns
with the remainder in Y. X starts at &2F ('0'-1) and
increments once per subtraction, giving the ASCII digit
directly.""",
    on_entry={"a": "divisor (stored to &B8)",
              "y": "dividend"},
    on_exit={"y": "remainder"})

# ============================================================
# Address comparison (&8640)
# ============================================================
subroutine(0x8668, "compare_addresses",
    title="Compare two 4-byte addresses",
    description="""\
Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
Used by the OSFILE save handler to compare the current
transfer address (&C8-&CB, copied to &B0) against the end
address (&B4-&B7) during multi-block file data transfers.""",
    on_exit={"a": "corrupted (EOR result)",
             "x": "corrupted",
             "y": "preserved"})

# ============================================================
# FS flags (&8651 / &8659)
# ============================================================
subroutine(0x867E, "clear_fs_flag", hook=None,
    title="Clear bit(s) in FS flags (&0E07)",
    description="""\
Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
the specified bits. JMPs to the shared STA at &865C, skipping
the ORA in set_fs_flag.""")

entry(0x8680)
subroutine(0x8680, "set_fs_flag", hook=None,
    title="Set bit(s) in FS flags (&0E07)",
    description="""\
ORs A into fs_work_0e07 (EOF hint byte), then falls through
to STA fs_eof_flags at &865C (shared with clear_fs_flag).
Each bit represents one of up to 8 open file handles. When
clear, the file is definitely NOT at EOF. When set, the
fileserver must be queried to confirm EOF status. This
negative-cache optimisation avoids expensive network
round-trips for the common case. The hint is cleared when
the file pointer is updated (since seeking away from EOF
invalidates the hint) and set after BGET/OPEN/EOF operations
that might have reached the end.""")

# ============================================================
# Print file info (&8CFC)
# ============================================================
subroutine(0x8D24, "print_file_info", hook=None,
    title="Print file catalogue line",
    description="""\
Displays a formatted catalogue entry: filename (padded to 12
chars with spaces), load address (4 hex bytes at offset 5-2),
exec address (4 hex bytes at offset 9-6), and file length
(3 hex bytes at offset &0C-&0A), followed by a newline.
Data is read from (fs_crc_lo) for the filename and from
(fs_options) for the numeric fields. Returns immediately
if fs_messages_flag is zero (no info available).""")

# ============================================================
# Hex printing (&9FE0 / &9FE9)
# ============================================================
# Moved to end of ROM and rewritten in 3.40 (was at &8D9D in
# 3.35K). The new routine uses CMP #&0A / ADC #6 / ADC #&30
# instead of ORA #&30 / CMP #&3A / ADC #6, and explicitly
# calls OSASCI before returning (self-contained, no fall-through).
label(0x9FE0, "print_hex")
subroutine(0x9FE0, hook=None,
    title="Print byte as two hex digits",
    description="""\
Prints the high nibble first (via 4x LSR), then the low
nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
and output via OSASCI. Returns with carry set.""")

label(0x9FE9, "print_hex_nibble")
subroutine(0x9FE9, hook=None,
    title="Print single hex nibble",
    description="""\
Converts the low nibble of A to ASCII hex ('0'-'9' or 'A'-'F')
and prints via OSASCI. Returns with carry set.""")

# ============================================================
# TX control (&8660-&866C)
# ============================================================
subroutine(0x8687, "setup_tx_ptr_c0", hook=None,
    title="Set up TX pointer to control block at &00C0",
    description="""\
Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""")

subroutine(0x868F, "tx_poll_ff", hook=None,
    title="Transmit and poll for result (full retry)",
    description="""\
Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""")

subroutine(0x8693, "tx_poll_core",
    title="Core transmit and poll routine (XMIT)",
    description="""\
Claims the TX semaphore (tx_ctrl_status) via ASL -- a busy-wait
spinlock where carry=0 means the semaphore is held by another
operation. Only after claiming the semaphore is the TX pointer
copied to nmi_tx_block, ensuring the low-level transmit code
sees a consistent pointer. Then calls the ADLC TX setup routine
and polls the control byte for completion:
  bit 7 set = still busy (loop)
  bit 6 set = error (check escape or report)
  bit 6 clear = success (clean return)
On error, checks for escape condition and handles retries.
Two entry points: setup_tx_ptr_c0 (&8687) always uses the
standard TXCB; tx_poll_core (&8693) is general-purpose.""",
    on_entry={"a": "retry count (&FF = full retry)",
              "y": "timeout parameter (&60 = standard)"},
    on_exit={"a": "entry A (retry count, restored from stack)",
             "x": "0",
             "y": "0"})

# ============================================================
# print_inline subroutine (&85D9)
# ============================================================
# Label and code-tracing hook created by hook_subroutine() above.
subroutine(0x8605, hook=None,
    title="Print inline string, high-bit terminated (VSTRNG)",
    description="""\
Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. N.B. Cannot be used for
BRK error messages -- the stack manipulation means a BRK in the
inline data would corrupt the stack rather than invoke the error
handler.""",
    on_exit={"a": "terminator byte (bit 7 set, also next opcode)",
             "x": "corrupted (by OSASCI)",
             "y": "0"})

comment(0x8605, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x8608, "Pop return address (high)", inline=True)
comment(0x860D, "Advance pointer past return address / to next char", inline=True)
comment(0x8613, "Load next byte from inline string", inline=True)
comment(0x8615, "Bit 7 set? Done — this byte is the next opcode", inline=True)
comment(0x861D, "Jump to address of high-bit byte (resumes code after string)", inline=True)

# ============================================================
# Dispatch table comments (&8024-&8068)
# ============================================================
comment(0x8024, """\
Dispatch table: low bytes of (handler_address - 1)
Each entry stores the low byte of a handler address minus 1,
for use with the PHA/PHA/RTS dispatch trick at &80E7.
See dispatch_hi (&8049) for the corresponding high bytes.

Five callers share this table via different Y base offsets:
  Y=&00  Service calls 0-12       (indices 0-13)
  Y=&0E  Language entry reasons    (indices 14-18)
  Y=&13  FSCV codes 0-7           (indices 19-26)
  Y=&17  FS reply handlers        (indices 27-32)
  Y=&21  *NET1-4 sub-commands     (indices 33-36)

Lo bytes for the last 6 entries (indices 31-36) occupy &8044-&8049,
immediately before the hi bytes. Their hi bytes are at
&8069-&806E, after the main dispatch_hi table.""")

comment(0x8049, """\
Dispatch table: high bytes of (handler_address - 1)
Paired with dispatch_lo (&8024). Together they form a table of
37 handler addresses, used via the PHA/PHA/RTS trick at &80E7.""")

# Inline comments on each low-byte dispatch table entry.
# Service call handlers (Y=&00, indices 0-13)
comment(0x8025, "Svc 0: already claimed (no-op)", inline=True)
comment(0x8026, "Svc 1: absolute workspace", inline=True)
comment(0x8027, "Svc 2: private workspace", inline=True)
comment(0x8028, "Svc 3: auto-boot", inline=True)
comment(0x8029, "Svc 4: unrecognised star command", inline=True)
comment(0x802A, "Svc 5: unrecognised interrupt", inline=True)
comment(0x802B, "Svc 6: BRK (no-op)", inline=True)
comment(0x802C, "Svc 7: unrecognised OSBYTE", inline=True)
comment(0x802D, "Svc 8: unrecognised OSWORD", inline=True)
comment(0x802E, "Svc 9: *HELP", inline=True)
comment(0x802F, "Svc 10: static workspace (no-op)", inline=True)
comment(0x8030, "Svc 11: NMI release (reclaim NMIs)", inline=True)
comment(0x8031, "Svc 12: NMI claim (save NMI state)", inline=True)
comment(0x8032, "Svc 13: select NFS (intercepted before dispatch)", inline=True)

# Language entry handlers (Y=&0E, indices 14-18)
comment(0x8033, "Lang 0: no language / Tube", inline=True)
comment(0x8034, "Lang 1: normal startup", inline=True)
comment(0x8035, "Lang 2: softkey byte (Electron)", inline=True)
comment(0x8036, "Lang 3: softkey length (Electron)", inline=True)
comment(0x8037, "Lang 4: remote validated", inline=True)

# FSCV handlers (Y=&13, indices 19-26)
comment(0x8038, "FSCV 0: *OPT", inline=True)
comment(0x8039, "FSCV 1: EOF check", inline=True)
comment(0x803A, "FSCV 2: */ (run)", inline=True)
comment(0x803B, "FSCV 3: unrecognised star command", inline=True)
comment(0x803C, "FSCV 4: *RUN", inline=True)
comment(0x803D, "FSCV 5: *CAT", inline=True)
comment(0x803E, "FSCV 6: shutdown", inline=True)
comment(0x803F, "FSCV 7: read handle range", inline=True)

# FS reply handlers (Y=&17, indices 27-32)
comment(0x8040, "FS reply: print directory name", inline=True)
comment(0x8041, "FS reply: copy handles + boot", inline=True)
comment(0x8042, "FS reply: copy handles", inline=True)
comment(0x8043, "FS reply: set CSD handle", inline=True)

# ============================================================
# *NET command dispatch (&806F)
# ============================================================
subroutine(0x806F, "dispatch_net_cmd", hook=None,
    title="*NET command dispatcher",
    description="""\
Parses the character after *NET as '1'-'4', maps to table
indices 33-36 via base offset Y=&21, and dispatches via &80E7.
Characters outside '1'-'4' fall through to return_1 (RTS).

These are internal sub-commands used only by the ROM itself,
not user-accessible star commands. The MOS command parser
requires a space or terminator after 'NET', so *NET1 typed
at the command line does not match; these are reached only
via OSCLI calls within the ROM.

*NET1 (&8E59): read file handle from received
packet (net_1_read_handle)

*NET2 (&8E5F): read handle entry from workspace
(net_2_read_handle_entry)

*NET3 (&8E6F): close handle / mark as unused
(net_3_close_handle)

*NET4 (&81B8): resume after remote operation
(net_4_resume_remote)""")

comment(0x806F, "Read command character following *NET", inline=True)
comment(0x8071, "Subtract ASCII '1' to get 0-based command index", inline=True)
comment(0x807D, "Y=&21: base offset for *NET commands (index 33+)", inline=True)

# ============================================================
# PHA/PHA/RTS dispatcher (&80DA)
# ============================================================
subroutine(0x80E7, "dispatch", hook=None,
    title="PHA/PHA/RTS computed dispatch",
    description="""\
X = command index within caller's group (e.g. service number)
Y = base offset into dispatch table (0, &0E, &13, &21, etc.)
The loop adds Y+1 to X, so final X = command index + base + 1.
Then high and low bytes of (handler-1) are pushed onto the stack,
and RTS pops them and jumps to handler_address.

This is a standard 6502 trick: RTS increments the popped address
by 1 before jumping, so the table stores (address - 1) to
compensate. Multiple callers share one table via different Y
base offsets.""")

comment(0x80E7, "Add base offset Y to index X (loop: X += Y+1)", inline=True)
comment(0x80EC, "Load high byte of (handler - 1) from table", inline=True)
comment(0x80EF, "Push high byte onto stack", inline=True)
comment(0x80F0, "Load low byte of (handler - 1) from table", inline=True)
comment(0x80F3, "Push low byte onto stack", inline=True)
comment(0x80F4, "Restore X (fileserver options) for use by handler", inline=True)
comment(0x80F6, "RTS pops address, adds 1, jumps to handler", inline=True)

# ============================================================
# Language entry dispatch (&80D4)
# ============================================================
subroutine(0x80E1, hook=None,
    title="Language entry dispatcher",
    description="""\
Called when the NFS ROM is entered as a language. X = reason code
(0-4). Dispatches via table indices 15-19 (base offset Y=&0E).""")

comment(0x80E5, "Y=&0E: base offset for language handlers (index 15+)", inline=True)

# ============================================================
# Service handler entry (&80EA)
# ============================================================
subroutine(0x811F, hook=None,
    title="Service handler entry",
    description="""\
Intercepts three service calls before normal dispatch:
  &FE: Tube init -- explode character definitions
  &FF: Full init -- vector setup, copy code to RAM, select NFS
  &12 (Y=5): Select NFS as active filing system
All other service calls < &0D dispatch via c8146.
3.35K removes the per-ROM disable flag check that 3.35D has.""")

# ============================================================
# Init: set up vectors and copy code (&8140)
# ============================================================
# Rewritten in 3.40: reverts from table-driven vector init
# (3.35D/3.35K) to hardcoded LDA/STA pairs, and only sets
# 2 vectors (EVNTV and BRKV) instead of 4. RDCHV and WRCHV
# are no longer initialised during full reset.
label(0x8140, "init_vectors_and_copy")

# ============================================================
# Select NFS as active filing system (&81B5)
# ============================================================
subroutine(0x81ED, "svc_13_select_nfs", hook=None,
    title="Select NFS as active filing system (INIT)",
    description="""\
Reached from service &12 (select FS) with Y=5, or when *NET command
selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
this triggers the outgoing FS to save its context back to its
workspace page, allowing restoration if re-selected later (the
FSDIE handoff mechanism). Then sets up the standard OS vector
indirections (FILEV through FSCV) to NFS entry points, claims the
extended vector table entries, and issues service &0F (vectors
claimed) to notify other ROMs. If nfs_temp is zero (auto-boot
not inhibited), injects the synthetic command "I .BOOT" through
the command decoder to trigger auto-boot login.""")

# ============================================================
# Set up filing system vectors (&820E)
# ============================================================
subroutine(0x8224, "setup_fs_vectors", hook=None,
    title="Set up filing system vectors",
    description="""\
Entered from svc_3_autoboot: first checks the pressed key (EOR #&55),
prints "Econet Station <n>" via print_inline/print_decimal, and checks
ADLC SR2 for network clock — prints "No Clock" if absent.

Then copies 14 bytes from fs_vector_addrs (&8296) into FILEV-FSCV
(&0212), setting all 7 filing system vectors to the extended vector
dispatch addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install
the ROM pointer table entries with the actual NFS handler addresses.
The vector copy loop at &8260 is also reached directly from svc_13_select_nfs
via BEQ, bypassing the station/clock display.""")

comment(0x8260, "Copy 14 bytes: FS vector addresses → FILEV-FSCV", inline=True)

# ============================================================
# Auto-boot command string (&828E)
# ============================================================
# In 3.35K, &828E was inside the vector dispatch table. In 3.40, the
# code shifted: issue_vectors_claimed now loads X/Y pointing to &828E
# as the "I .BOOT\r" command string passed to fscv_3_star_cmd.
string(0x828E, 8)
comment(0x828E, "Auto-boot command string for fscv_3_star_cmd", inline=True)

# ============================================================
# FS vector dispatch and handler addresses (&8296)
# ============================================================
subroutine(0x8296, "fs_vector_addrs", hook=None,
    title="FS vector dispatch and handler addresses (34 bytes)",
    description="""\
Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by setup_fs_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the ROM pointer table.

Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (store_rom_ptr_pair writes the current ROM
bank number without reading). The last entry (FSCV) has no
padding byte.""")

# Part 1: extended vector dispatch addresses (7 x 2 bytes)
for i, name in enumerate(["FILEV", "ARGSV", "BGETV", "BPUTV",
                           "GBPBV", "FINDV", "FSCV"]):
    addr = 0x8296 + i * 2
    byte(addr, 2)
    comment(addr, f"{name} dispatch (&FF{0x1B + i * 3:02X})", inline=True)

# Part 2: handler address entries (7 x {lo, hi, pad})
# store_rom_ptr_pair reads lo/hi from ROM and writes ROM bank as pad.
handler_names = [
    ("FILEV",  0x8705),
    ("ARGSV",  0x8924),
    ("BGETV",  0x855C),
    ("BPUTV",  0x840F),
    ("GBPBV",  0x8A2E),
    ("FINDV",  0x8994),
    ("FSCV",   0x80D4),
]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x82A4 + i * 3
    byte(base_addr, 1)
    comment(base_addr, f"{name} handler lo (&{handler_addr:04X})", inline=True)
    byte(base_addr + 1, 1)
    comment(base_addr + 1, f"{name} handler hi", inline=True)
    if i < 6:  # pad byte for all but last entry
        byte(base_addr + 2, 1)
        comment(base_addr + 2, "(ROM bank — not read)", inline=True)

# ============================================================
# Service 1: claim absolute workspace (&82A2)
# ============================================================
subroutine(0x82B8, "svc_1_abs_workspace", hook=None,
    title="Service 1: claim absolute workspace",
    description="""\
Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""")

# ============================================================
# Service 2: claim private workspace (&82AB)
# ============================================================
subroutine(0x82C1, "svc_2_private_workspace", hook=None,
    title="Service 2: claim private workspace and initialise NFS",
    description="""\
Y = next available workspace page on entry.
Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
On soft break (OSBYTE &FD returns 0): skips FS state init,
preserving existing login state, file server selection, and
control block configuration — this is why pressing BREAK
keeps the user logged in.
On power-up/CTRL-BREAK (result non-zero):
  - Sets FS server station to &FE (FS, the default; no server)
  - Sets printer server to &EB (PS, the default)
  - Clears FS handles, OPT byte, message flag, SEQNOS
  - Initialises all RXCBs with &3F flag (available)
In both cases: reads station ID from &FE18 (only valid during
reset), calls adlc_init, enables user-level RX (LFLAG=&40).""")

comment(0x82D8, "OSBYTE &FD: read type of last reset", inline=True)
comment(0x82DE, "Soft break (X=0): skip FS init", inline=True)
comment(0x82E4, "Station &FE = no server selected", inline=True)
comment(0x8312, "Read station ID (also INTOFF)", inline=True)
comment(0x8319, "Initialise ADLC hardware", inline=True)

# ============================================================
# Service 3: auto-boot (&8203)
# ============================================================
subroutine(0x8219, "svc_3_autoboot", hook=None,
    title="Service 3: auto-boot",
    description="""\
Notifies current FS of shutdown via FSCV A=6. Scans keyboard
(OSBYTE &7A): if no key is pressed, auto-boot proceeds; if the
'N' key is pressed (matrix address &55), the boot is declined
and the key is forgotten via OSBYTE &78. Any other key also
declines. Prints "Econet Station <n>" and checks the ADLC SR2
for the network clock signal — prints "No Clock" if absent (no
network communication possible without it). Then falls through
to set up NFS vectors (selecting NFS as the filing system).""")

# ============================================================
# Service 4: unrecognised * command (&8168)
# ============================================================
subroutine(0x81A5, "svc_star_command", hook=None,
    title="Service 4: unrecognised * command",
    description="""\
The first 7 bytes (&81A5-&81AB) are the service handler epilogue:
PLA/STA restores &A9, TXA/LDX retrieves romsel_copy, then RTS.
This is the return path reached after any dispatched service
handler completes.

The service 4 handler itself is dispatched via the table to
&81B1 (after 5 NOPs of padding). It makes two match_rom_string
calls against the ROM header, reusing header bytes as command
strings:

  X=&0C: matches "ROFF" at &8014 — the suffix of the
         copyright string "(C)ROFF" → *ROFF (Remote Off,
         end remote session) — falls through to net_4_resume_remote

  X=5: matches "NET" at &800D — the ROM title suffix
       → *NET (select NFS) — falls through to svc_13_select_nfs

If neither matches, returns with the service call
unclaimed.""")

# ============================================================
# Service 9: *HELP (&81ED)
# ============================================================
subroutine(0x8204, "svc_9_help", hook=None,
    title="Service 9: *HELP",
    description="""\
Prints the ROM identification string using print_inline.""")

# ============================================================
# Match ROM string (&835E)
# ============================================================
# Rewritten in 3.40 with '.' abbreviation support (CMP #&2E
# at &8362). In 3.35K this was at &81CC without dot support.
label(0x835E, "match_rom_string")

# ============================================================
# Call FSCV shutdown (&81FE)
# ============================================================
subroutine(0x8214, "call_fscv_shutdown", hook=None,
    title="Notify filing system of shutdown",
    description="""\
Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")

# ============================================================
# Issue service: vectors claimed (&8261)
# ============================================================
subroutine(0x8277, "issue_vectors_claimed", hook=None,
    title="Issue 'vectors claimed' service and optionally auto-boot",
    description="""\
Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If nfs_temp is zero (auto-boot not inhibited),
sets up the command string "I .BOOT" at &828E and jumps to
the FSCV 3 unrecognised-command handler (which matches against
the command table at &8C05). The "I." prefix triggers the
catch-all entry which forwards the command to the fileserver.""")

# ============================================================
# Set up ROM pointer table and NETV (&830B)
# ============================================================
subroutine(0x8321, "setup_rom_ptrs_netv", hook=None,
    title="Set up ROM pointer table and NETV",
    description="""\
Reads the ROM pointer table base address via OSBYTE &A8, stores
it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
one 3-byte extended vector entry (addr=&9074, rom=current) into
the ROM pointer table at offset &36, installing osword_dispatch
as the NETV handler.""")

# ============================================================
# FSCV shutdown: save FS state (&8337)
# ============================================================
subroutine(0x834D, "fscv_6_shutdown", hook=None,
    title="FSCV 6: Filing system shutdown / save state (FSDIE)",
    description="""\
Called when another filing system (e.g. DFS) is selected. Saves
the current NFS context (FSLOCN station number, URD/CSD/LIB
handles, OPT byte, etc.) from page &0E into the dynamic workspace
backup area. This allows the state to be restored when *NET is
re-issued later, without losing the login session. Finally calls
OSBYTE &77 (FXSPEX: close SPOOL and EXEC files) to avoid leaving
dangling file handles across the FS switch.""")

# ============================================================
# Init TX control block (&8356)
# ============================================================
subroutine(0x8391, "init_tx_ctrl_block", hook=None,
    title="Initialise TX control block at &00C0 from template",
    description="""\
Copies 12 bytes from tx_ctrl_template (&83A9) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""")

subroutine(0x83A9, "tx_ctrl_template", hook=None,
    title="TX control block template (TXTAB, 12 bytes)",
    description="""\
12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")
# In 3.35K, &836E-&837A was the TX control block template data.
# In 3.40, the code shifted so &836D-&8379 is now code (string
# comparison loop tail: BNE/INY/INX/BNE + LDA abs,X/BEQ/RTS/INY).
# The TX control block template is at different addresses in 3.40.

# ============================================================
# Prepare FS command (&838A)
# ============================================================
subroutine(0x83C3, "prepare_fs_cmd",
    title="Prepare FS command buffer (12 references)",
    description="""\
Builds the 5-byte FS protocol header at &0F00:
  &0F00 HDRREP = reply port (set downstream, typically &90/PREPLY)
  &0F01 HDRFN  = Y parameter (function code)
  &0F02 HDRURD = URD handle (from &0E02)
  &0F03 HDRCSD = CSD handle (from &0E03)
  &0F04 HDRLIB = LIB handle (from &0E04)
Command-specific data follows at &0F05 (TXBUF). Also clears V flag.
Called before building specific FS commands for transmission.""",
    on_entry={"y": "function code for HDRFN",
              "x": "preserved through header build"},
    on_exit={"a": "0 on success (from build_send_fs_cmd)",
             "x": "0 on success, &D6 on not-found",
             "y": "1 (offset past command code in reply)"})

# ============================================================
# Build and send FS command (&83A4)
# ============================================================
subroutine(0x83D9, "build_send_fs_cmd",
    title="Build and send FS command (DOFSOP)",
    description="""\
Sets reply port to &90 (PREPLY) at &0F00, initialises the TX
control block, then adjusts TXCB's high pointer (HPTR) to X+5
-- the 5-byte FS header (reply port, function code, URD, CSD,
LIB) plus the command data -- so only meaningful bytes are
transmitted, conserving Econet bandwidth. If carry is set on
entry (DOFSBX byte-stream path), takes the alternate path
through econet_tx_retry for direct BSXMIT transmission.
Otherwise sets up the TX pointer via setup_tx_ptr_c0 and falls
through to send_fs_reply_cmd for reply handling. The carry flag
is the sole discriminator between byte-stream and standard FS
protocol paths -- set by SEC at the BPUTV/BGETV entry points.
On return from WAITFS/BSXMIT, Y=0; INY advances past the
command code to read the return code. Error &D6 ("not found")
is detected via ADC #(&100-&D6) with C=0 -- if the return code
was exactly &D6, the result wraps to zero (Z=1). This is a
branchless comparison returning C=1, A=0 as a soft error that
callers can handle, vs hard errors which go through FSERR.""",
    on_entry={"x": "buffer extent (command-specific data bytes)",
              "y": "function code",
              "a": "timeout period for FS reply",
              "c": "0 for standard FS path, 1 for byte-stream (BSXMIT)"},
    on_exit={"a": "0 on success",
             "x": "0 on success, &D6 on not-found",
             "y": "1 (offset past command code in reply)"})

# ============================================================
# FS error handler (&8443)
# ============================================================
subroutine(0x8473, "store_fs_error", hook=None,
    title="Handle fileserver error replies (FSERR)",
    description="""\
The fileserver returns errors as: zero command code + error number +
CR-terminated message string. This routine converts the reply buffer
in-place to a standard MOS BRK error packet by:
  1. Storing the error code at fs_last_error (&0E09)
  2. Normalizing error codes below &A8 to &A8 (the standard FS error
     number), since the MOS error space below &A8 has other meanings
  3. Scanning for the CR terminator and replacing it with &00
  4. JMPing indirect through (l00c4) to execute the buffer as a BRK
     instruction — the zero command code serves as the BRK opcode
N.B. This relies on the fileserver always returning a zero command
code in position 0 of the reply buffer.""")

# ============================================================
# Handle BPUT/BGET (&83DD)
# ============================================================
subroutine(0x8410, "handle_bput_bget",
    title="Handle BPUT/BGET file byte I/O",
    description="""\
BPUTV enters at &83DC (CLC; fall through) and BGETV enters
at &852E (SEC; JSR here). The carry flag is preserved via
PHP/PLP through the call chain and tested later (BCS) to
select byte-stream transmission (BSXMIT) vs normal FS
transmission (FSXMIT) -- a control-flow encoding using
processor flags to avoid an extra flag variable.

BSXMIT uses handle=0 for print stream transactions (which
sidestep the SEQNOS sequence number manipulation) and non-zero
handles for file operations. After transmission, the high
pointer bytes of the CB are reset to &FF -- "The BGET/PUT byte
fix" which prevents stale buffer pointers corrupting subsequent
byte-level operations.""",
    on_entry={"c": "0 for BPUT (write byte), 1 for BGET (read byte)",
              "a": "byte to write (BPUT only)",
              "y": "file handle"},
    on_exit={"a": "preserved",
             "x": "preserved",
             "y": "preserved"})

# ============================================================
# Send command to fileserver (&84ED)
# ============================================================
subroutine(0x851D, "send_to_fs", hook=None,
    title="Send command to fileserver and handle reply (WAITFS)",
    description="""\
Performs a complete FS transaction: transmit then wait for reply.
Sets bit 7 of rx_status_flags (mark FS transaction in progress),
builds a TX frame from the data at (net_tx_ptr), and transmits
it. The system RX flag (LFLAG bit 7) is only set when receiving
into the page-zero control block — if RXCBP's high byte is
non-zero, setting the system flag would interfere with other RX
operations. The timeout counter uses the stack (indexed via TSX)
rather than memory to avoid bus conflicts with Econet hardware
during the tight polling loop. Handles multi-block replies and
checks for escape conditions between blocks.""")

# ============================================================
# Check escape (&851D)
# ============================================================
subroutine(0x854C, "check_escape", hook=None,
    title="Check and handle escape condition (ESC)",
    description="""\
Two-level escape gating: the MOS escape flag (&FF bit 7) is ANDed
with the software enable flag ESCAP. Both must have bit 7 set for
escape to fire. ESCAP is set non-zero during data port operations
(LOADOP stores the data port &90, serving double duty as both the
port number and the escape-enable flag). ESCAP is disabled via LSR
in the ENTER routine, which clears bit 7 — PHP/PLP around the LSR
preserves the carry flag since ENTER is called from contexts where
carry has semantic meaning (e.g., PUTBYT vs BGET distinction).
This architecture allows escape between retransmission attempts
but prevents interruption during critical FS transactions. If
escape fires: acknowledges via OSBYTE &7E, then checks whether
the failing handle is the current SPOOL or EXEC handle (OSBYTE
&C6/&C7); if so, issues "*SP." or "*E." via OSCLI to gracefully
close the channel before raising the error — preventing the system
from continuing to spool output to a broken file handle.

3.35K restructures the SPOOL/EXEC close logic: both handles
are always checked (3.35D skipped EXEC if SPOOL matched),
and OSCLI is always called (with a harmless "." default if
neither matched).""")

# 3.35K fix comments at $8526/$8568 — addresses shifted in 3.40;
# these fixes originated in 3.35K and are present in 3.40 but at
# different addresses (will be confirmed after code tracing).

# ============================================================
# Error message table (&854D)
# ============================================================
# N.B. This is data, not code — we use label() not subroutine()
# to avoid entry() tracing from &854D, where the &A0 error code
# byte would be misinterpreted as LDY #imm.
label(0x8579, "error_msg_table")
comment(0x8579, """\
Econet error message table (ERRTAB, 7 entries).
Each entry: error number byte followed by NUL-terminated string.
  &A0: "Line Jammed"     &A1: "Net Error"
  &A2: "Not listening"   &A3: "No Clock"
  &11: "Escape"           &CB: "Bad Option"
  &A5: "No reply"
Indexed by the low 3 bits of the TXCB flag byte (AND #&07),
which encode the specific Econet failure reason. The NREPLY
and NLISTN routines build a MOS BRK error block at &100 on the
stack page: NREPLY fires when the fileserver does not respond
within the timeout period; NLISTN fires when the destination
station actively refused the connection.
Indexed via the error dispatch at c8424/c842c.""")

# Mark each error table entry as data: error code byte + NUL-terminated string.
# Without this, the first entry's &A0 byte is traced as code (LDY #imm).
addr = 0x8579
for _ in range(7):
    byte(addr, 1)           # error number byte
    addr = stringz(addr + 1)  # NUL-terminated message string

# ============================================================
# Resume after remote operation (&8180)
# ============================================================
subroutine(0x81B8, "net_4_resume_remote", hook=None,
    title="Resume after remote operation / *ROFF handler (NROFF)",
    description="""\
Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
disabled during a remote operation (peek/poke/boot). Clears
the flag, re-enables the keyboard via OSBYTE &C9, and sends
function &0A to notify completion. Also handles *ROFF and the
triple-plus escape sequence (+++), which resets system masks
via OSBYTE &CE and returns control to the MOS, providing an
escape route when a remote session becomes unresponsive.""")

# ============================================================
# FSCV handler (&80C7)
# ============================================================
subroutine(0x80D4, "fscv_handler",
    title="FSCV dispatch entry",
    description="""\
Entered via the extended vector table when the MOS calls FSCV.
Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
and dispatches codes 0-7 via the shared dispatch table at &8024
with base offset Y=&13 (table indices 20-27).
Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.""",
    on_entry={"a": "function code (0-7)",
              "x": "depends on function",
              "y": "depends on function"},
    on_exit={"a": "depends on handler (preserved if A >= 8)",
             "x": "depends on handler (preserved if A >= 8)",
             "y": "depends on handler (preserved if A >= 8)"})

comment(0x80D4, "Store A/X/Y in FS workspace", inline=True)
comment(0x80D9, "Function code >= 8? Return (unsupported)", inline=True)
comment(0x80DD, "Y=&13: base offset for FSCV dispatch (indices 20+)", inline=True)

# ============================================================
# GSINIT/GSREAD filename parser (&86BA)
# ============================================================
subroutine(0x86E1, "parse_filename_gs", hook=None,
    title="Parse filename using GSINIT/GSREAD into &0E30",
    description="""\
Uses the MOS GSINIT/GSREAD API to parse a filename string from
(os_text_ptr),Y, handling quoted strings and |-escaped characters.
Stores the parsed result CR-terminated at &0E30 and sets up
fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
a non-zero starting Y offset.""",
    on_entry={"y": "offset into (os_text_ptr) buffer (0 at &86C3)"},
    on_exit={"x": "length of parsed string",
             "y": "preserved"})

# ============================================================
# FILEV handler (&86DE)
# ============================================================
subroutine(0x8705, "filev_handler",
    title="FILEV handler (OSFILE entry point)",
    description="""\
Calls save_fscv_args (&85D2) to preserve A/X/Y, then JSR &86D7
to copy the 2-byte filename pointer from the parameter block to
os_text_ptr and fall through to parse_filename_gs (&86E1) which
parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &871B)
  A=&00: save file (filev_save at &878F)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &888D)
  Other: restore_args_return (unsupported, no-op)""",
    on_entry={"a": "function code (&FF=load, &00=save, &01-&06=attrs)",
              "x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "restored",
             "x": "restored",
             "y": "restored"})

subroutine(0x871B, "send_fs_examine", hook=None,
    title="Send FS examine command",
    description="""\
Sends FS command &03 (FCEXAM: examine file) to the fileserver.
Sets &0F02=&03 and error pointer to '*'. Called for OSFILE &FF
(load file) with the filename already in the command buffer.
The FS reply contains load/exec addresses and file length which
are used to set up the data transfer. The header URD field
is repurposed to carry the Econet data port number (PLDATA=&92)
for the subsequent block data transfer.""")

subroutine(0x875F, "send_data_blocks", hook=None,
    title="Send file data in multi-block chunks",
    description="""\
Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")

subroutine(0x878F, "filev_save", hook=None,
    title="OSFILE save handler (A=&00)",
    description="""\
Copies 4-byte load/exec/length addresses from the parameter block
to the FS command buffer, along with the filename. Sends FS
command &91 with function &14 to initiate the save, then
calls print_file_info to display the filename being saved.
Handles both host and Tube-based data sources.
When receiving the save acknowledgement, the RX low pointer is
incremented by 1 to skip the command code (CC) byte, which
indicates the FS type and must be preserved. N.B. this assumes
the RX buffer does not cross a page boundary.""")

subroutine(0x87F0, "copy_load_addr_from_params", hook=None,
    title="Copy load address from parameter block",
    description="""\
Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""")

subroutine(0x8802, "copy_reply_to_params", hook=None,
    title="Copy FS reply data to parameter block",
    description="""\
Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""")

subroutine(0x8814, "transfer_file_blocks", hook=None,
    title="Multi-block file data transfer",
    description="""\
Manages the transfer of file data in chunks between the local
machine and the fileserver. Entry conditions: WORK (&B0-&B3) and
WORK+4 (&B4-&B7) hold the low and high addresses of the data
being sent/received. Sets up source (&C4-&C7) and destination
(&C8-&CB) from the FS reply, sends &80-byte (128-byte) blocks
with command &91, and continues until all data has been
transferred. Handles address overflow and Tube co-processor
transfers. For SAVE, WORK+8 holds the port on which to receive
byte-level ACKs for each data block (flow control).""")

subroutine(0x8869, "fscv_1_eof", hook=None,
    title="FSCV 1: EOF handler",
    description="""\
Checks whether a file handle has reached end-of-file. Converts
the handle via handle_to_mask_clc, tests the result against the
EOF hint byte (&0E07). If the hint bit is clear, returns X=0
immediately (definitely not at EOF — no network call needed).
If the hint bit is set, sends FS command &11 (FCEOF) to query
the fileserver for definitive EOF status. Returns X=&FF if at
EOF, X=&00 if not. This two-level check avoids an expensive
network round-trip when the file is known to not be at EOF.""")

subroutine(0x888D, "filev_attrib_dispatch", hook=None,
    title="FILEV attribute dispatch (A=1-6)",
    description="""\
Dispatches OSFILE operations by function code:
  A=1: write catalogue info (load/exec/length/attrs) — FS &14
  A=2: write load address only
  A=3: write exec address only
  A=4: write file attributes
  A=5: read catalogue info, returns type in A — FS &12
  A=6: delete named object — FS &14 (FCDEL)
  A>=7: falls through to restore_args_return (no-op)
Each handler builds the appropriate FS command, sends it to
the fileserver, and copies the reply into the parameter block.
The control block layout uses dual-purpose fields: the 'data
start' field doubles as 'length' and 'data end' doubles as
'protection' depending on whether reading or writing attrs.""")

subroutine(0x896F, "restore_args_return", hook=None,
    title="Restore arguments and return",
    description="""\
Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""")

label(0x89E8, "fscv_0_opt_entry")       # FSCV 0 dispatch entry (BEQ guard before fscv_0_opt)

subroutine(0x89EA, "fscv_0_opt", hook=None,
    title="FSCV 0: *OPT handler (OPTION)",
    description="""\
Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""")

subroutine(0x8A16, "adjust_addrs", hook=None,
    title="Bidirectional 4-byte address adjustment",
    description="""\
Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""")

# ============================================================
# ARGSV handler (&8907)
# ============================================================
subroutine(0x8924, "argsv_handler",
    title="ARGSV handler (OSARGS entry point)",
    description="""\
  A=0, Y=0: return filing system number (10 = network FS)
  A=0, Y>0: read file pointer via FS command &0A (FCRDSE)
  A=1, Y>0: write file pointer via FS command &14 (FCWRSE)
  A>=3 (ensure): silently returns -- NFS has no local write buffer
     to flush, since all data is sent to the fileserver immediately
The handle in Y is converted via handle_to_mask_clc. For writes
(A=1), the carry flag from the mask conversion is used to branch
to save_args_handle, which records the handle for later use.""",
    on_entry={"a": "function code (0=query, 1=write ptr, >=3=ensure)",
              "y": "file handle (0=FS-level query, >0=per-file)"},
    on_exit={"a": "filing system number if A=0/Y=0 query, else restored",
             "x": "restored",
             "y": "restored"})

# ============================================================
# FINDV handler (&896F)
# ============================================================
subroutine(0x8994, "findv_handler",
    title="FINDV handler (OSFIND entry point)",
    description="""\
  A=0: close file -- delegates to close_handle (&89AE)
  A>0: open file -- modes &40=read, &80=write/update, &C0=read/write
For open: the mode byte is converted to the fileserver's two-flag
format by flipping bit 7 (EOR #&80) and shifting. This produces
Flag 1 (read/write direction) and Flag 2 (create/existing),
matching the fileserver protocol. After a successful open, the
new handle's bit is OR'd into the EOF hint byte (marks it as
"might be at EOF, query the server"), and into the sequence
number tracking byte for the byte-stream protocol.""",
    on_entry={"a": "operation (0=close, &40=read, &80=write, &C0=R/W)",
              "x": "filename pointer low (open)",
              "y": "file handle (close) or filename pointer high (open)"},
    on_exit={"a": "handle on open, 0 on close-all, restored on close-one",
             "x": "restored",
             "y": "restored"})

# 3.35K: sequence number initialisation for newly opened handles
comment(0x89C6, """\
3.35K fix: OR handle bit into fs_sequence_nos
(&0E08). Without this, a newly opened file could
inherit a stale sequence number from a previous
file using the same handle, causing byte-stream
protocol errors.""")

# ============================================================
# CLOSE handler (&89AE)
# ============================================================
subroutine(0x89CC, "close_handle", hook=None,
    title="Close file handle(s) (CLOSE)",
    description="""\
  Y=0: close all files — first calls OSBYTE &77 (close SPOOL and
       EXEC files) to coordinate with the MOS before sending the
       close-all command to the fileserver. This ensures locally-
       managed file handles are released before the server-side
       handles are invalidated, preventing the MOS from writing to
       a closed spool file.
  Y>0: close single handle — sends FS close command and clears
       the handle's bit in both the EOF hint byte and the sequence
       number tracking byte.""")

# ============================================================
# GBPBV handler (&8A0E)
# ============================================================
subroutine(0x8A2E, "gbpbv_handler",
    title="GBPBV handler (OSGBPB entry point)",
    description="""\
  A=1-4: file read/write operations (handle-based)
  A=5-8: info queries (disc title, current dir, lib, filenames)
Calls 1-4 are standard file data transfers via the fileserver.
Calls 5-8 were a late addition to the MOS spec and are the only
NFS operations requiring Tube data transfer -- described in the
original source as "untidy but useful in theory." The data format
uses length-prefixed strings (<name length><object name>) rather
than the CR-terminated strings used elsewhere in the FS.""",
    on_entry={"a": "call number (1-8)",
              "x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "0 after FS operation, else restored",
             "x": "restored",
             "y": "restored"})

# ============================================================
# OSGBPB info handler (&8AD1)
# ============================================================
subroutine(0x8AED, "osgbpb_info", hook=None,
    title="OSGBPB 5-8 info handler (OSINFO)",
    description="""\
Handles the "messy interface tacked onto OSGBPB" (original source).
Checks whether the destination address is in Tube space by comparing
the high bytes against TBFLAG. If in Tube space, data must be
copied via the Tube FIFO registers (with delays to accommodate the
slow 16032 co-processor) instead of direct memory access.""")

# ============================================================
# Forward unrecognised * command to fileserver (&80B4)
# ============================================================
subroutine(0x80C1, "forward_star_cmd", hook=None,
    title="Forward unrecognised * command to fileserver (COMERR)",
    description="""\
Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
prepares an FS command with function code 0, and sends it to the
fileserver to request decoding. The server returns a command code
indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
5=load-as-command). This mechanism allows the fileserver to extend
the client's command set without ROM updates. Called from the "I."
and catch-all entries in the command match table at &8C05, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")

# ============================================================
# *BYE handler (&8383)
# ============================================================
subroutine(0x83BC, "bye_handler", hook=None,
    title="*BYE handler (logoff)",
    description="""\
Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8C05 for "BYE".""")

# ============================================================
# FSCV unrecognised * handler (&8BB6)
# ============================================================
subroutine(0x8BD7, "fscv_3_star_cmd", hook=None,
    title="FSCV 2/3/4: unrecognised * command handler (DECODE)",
    description="""\
CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8C05 using case-insensitive comparison with abbreviation
support — commands can be shortened with '.' (e.g. "I." for
"INFO"). The "I." entry is a special fudge placed first in the
table: since "I." could match multiple commands, it jumps to
forward_star_cmd to let the fileserver resolve the ambiguity.

The matching loop compares input characters against table
entries. On mismatch, it skips to the next entry. On match
of all table characters, or when '.' abbreviation is found,
it dispatches via PHA/PHA/RTS to the entry's handler address.

After matching, adjusts fs_crc_lo/fs_crc_hi to point past
the matched command text.""")

subroutine(0x8C05, "fs_cmd_match_table", hook=None,
    title="FS command match table (COMTAB)",
    description="""\
Format: command letters (bit 7 clear), then dispatch address
as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
adds 1 to the stored (address-1). Matching is case-insensitive
(AND &DF) and supports '.' abbreviation (standard Acorn pattern).

Entries:
  "I."     → &80C1 (forward_star_cmd) — placed first as a fudge
             to catch *I. abbreviation before matching *I AM
  "I AM"   → &8082 (i_am_handler: parse station.net, logon)
  "EX"     → &8C1B (ex_handler: embedded in table tail)
  "BYE"\\r  → &83BC (bye_handler: logoff)
  <catch-all> → &80C1 (forward anything else to FS)""")

# ============================================================
# *EX and *CAT handlers (&8C1B / &8C21)
# ============================================================
# In 3.40, ex_handler code is embedded in the tail of
# fs_cmd_match_table at &8C1B — the bytes A2 01 A9 03 D0 08
# serve as both table data and executable code (LDX #1 / LDA #3
# / BNE fscv_5_cat+8). Dispatched via PHA/PHA/RTS from the
# "EX" entry in the match table.
entry(0x8C1B)
label(0x8C1B, "ex_handler")

subroutine(0x8C21, "fscv_5_cat", hook=None,
    title="*CAT handler (directory catalogue)",
    description="""\
Sets column width &B6=&14 (20 columns, four files per 80-column
line) and &B7=&03. The catalogue protocol is multi-step: first
sends FCUSER (&15: read user environment) to get CSD, disc, and
library names, then sends FCREAD (&12: examine) repeatedly to
fetch entries in batches until zero are returned (end of dir).
The receive buffer abuts the examine request buffer and ends at
RXBUFE, allowing seamless data handling across request cycles.

The command code byte in the fileserver reply indicates FS type:
zero means an old-format FS (client must format data locally),
non-zero means new-format (server returns pre-formatted strings).
This enables backward compatibility with older Acorn fileservers.

Display format:
  - Station number in parentheses
  - "Owner" or "Public" access level
  - Boot option with name (Off/Load/Run/Exec)
  - Current directory and library paths
  - Directory entries: CRFLAG (&CF) cycles 0-3 for multi-column
    layout; at count 0 a newline is printed, others get spaces.
    *EX sets CRFLAG=&FF to force one entry per line.""")

# ============================================================
# Boot command strings (&8CE7)
# ============================================================
subroutine(0x8D0F, "boot_cmd_strings", hook=None,
    title="Boot command strings for auto-boot",
    description="""\
The four boot options use OSCLI strings at offsets within page &8D.
The offset table at boot_option_offsets+1 (&8D1C) is indexed by
the boot option value (0-3); each byte is the low byte of the
string address, with the page high byte &8D loaded separately:
  Option 0 (Off):  offset &1B → &8D1B = bare CR (empty command)
  Option 1 (Load): offset &0C → &8D0C = "L.!BOOT" (the bytes
      &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D0F)
  Option 2 (Run):  offset &0E → &8D0E = "!BOOT" (bare filename = *RUN)
  Option 3 (Exec): offset &14 → &8D14 = "E.!BOOT"

This is a classic BBC ROM space optimisation: the string data
overlaps with other byte sequences to save space. The &0D byte
at &8D1B terminates "E.!BOOT" AND doubles as the bare-CR
command for boot option 0.""")

# ============================================================
# Boot option table and "I AM" handler (&8CF4-&8E20)
# ============================================================
subroutine(0x8D1B, "boot_option_offsets", hook=None,
    title="Boot option → OSCLI string offset table",
    description="""\
Five bytes: the first byte (&0D) is the bare-CR target for boot
option 0; bytes 1-4 are the offset table indexed by boot option
(0-3). Each offset is the low byte of a pointer into page &8D.
The code reads from boot_option_offsets+1 (&8D1C) via
LDX l8d1c,Y with Y=boot_option, then LDY #&8D, JMP oscli.
See boot_cmd_strings for the target strings.""")
for i in range(5):
    byte(0x8D1B + i)
# In 3.40, $8CF4-$8CFC is code (PLA/CLC/ADC $B4/TAY/BNE/LDY #$0A)
# that forms the print_reply_bytes entry chain. The byte values also
# serve as boot command string offsets in earlier versions, but in
# 3.40 the boot option offset table is at boot_option_offsets ($8D1B).
comment(0x8D07, """\
Option name encoding: in 3.35, the boot option names ("Off",
"Load", "Run", "Exec") are scattered through the code rather
than stored as a contiguous table. They are addressed via
base+offset from return_9 (&8CE0), whose first four bytes
(starting with the RTS opcode &60) double as the offset table:
  &60→&8D40 "Off", &73→&8D53 "Load",
  &9B→&8D7B "Run", &18→&8CF8 "Exec"
Each string is terminated by the next instruction's opcode
having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).""")

subroutine(0x8082, "i_am_handler", hook=None,
    title="\"I AM\" command handler",
    description="""\
Dispatched from the command match table when the user types
"*I AM <station>" or "*I AM <station>.<network>". Also used as
the station number parser for "*NET <station>[.<network>]".
Skips leading spaces, then parses a decimal station number (and
optional network number after '.') via parse_decimal. Stores
the results in &0E00 (station) and &0E01 (network). If a colon
follows, reads interactive input via OSRDCH and appends it to
the command buffer. Finally jumps to forward_star_cmd.""")

# ============================================================
# Handle workspace management (&8E15-&8E1A)
# ============================================================
subroutine(0x8E1F, "fsreply_5_set_lib", hook=None,
    title="Set library handle",
    description="""\
Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to JMP restore_args_return if Y is non-zero.""")

subroutine(0x8E24, "fsreply_3_set_csd", hook=None,
    title="Set CSD handle",
    description="""\
Stores Y into &0E03 (current selected directory handle).
Falls through to JMP restore_args_return.""")

# ============================================================
# Copy handles and boot (&8E20 / &8E21)
# ============================================================
subroutine(0x8E2A, "fsreply_1_copy_handles_boot", hook=None,
    title="Copy FS reply handles to workspace and execute boot command",
    description="""\
SEC entry (LOGIN): copies 4 bytes from &0F05-&0F08 (FS reply) to
&0E02-&0E05 (URD, CSD, LIB handles and boot option), then
looks up the boot option in boot_option_offsets to get the
OSCLI command string and executes it via JMP oscli.
The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
share the handle-copying code, but only LOGIN executes the boot
command. This use of the carry flag to select behaviour between
two callers avoids duplicating the handle-copy loop.""")

subroutine(0x8E2B, "fsreply_2_copy_handles", hook=None,
    title="Copy FS reply handles to workspace (no boot)",
    description="""\
CLC entry (SDISC): copies handles only, then jumps to
restore_args_return via c8e27. Called when the FS reply contains
updated handle values but no boot action is needed.""")

# ============================================================
# Filename copy helpers (&8D43-&8D51)
# ============================================================
subroutine(0x8D75, "copy_filename", hook=None,
    title="Copy filename to FS command buffer",
    description="""\
Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""")

subroutine(0x8D77, "copy_string_to_cmd", hook=None,
    title="Copy string to FS command buffer",
    description="""\
Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""")

# ============================================================
# Print directory name (&8D57)
# ============================================================
subroutine(0x8D89, "fsreply_0_print_dir", hook=None,
    title="Print directory name from reply buffer",
    description="""\
Prints characters from the FS reply buffer (&0F05+X onwards).
Null bytes (&00) are replaced with CR (&0D) for display.
Stops when a byte with bit 7 set is encountered (high-bit
terminator). Used by fscv_5_cat to display Dir. and Lib. paths.""")

# ============================================================
# Print reply buffer bytes (&8CFB / &8CFD)
# ============================================================
# Rewritten in 3.40 and relocated from &8DB2 to &8CFB.
# Entry at &8CFB: sets Y=10 and falls into the loop.
# Entry at &8CFD: caller-supplied Y count.
# Entry at &8CF4: PLA/CLC/ADC $B4/TAY/BNE to compute count
# from stacked value, then enters loop via branch.

# ============================================================
# FSCV 2/4: */ and *RUN handler (&8DCF)
# ============================================================
subroutine(0x8DCF, "fscv_2_star_run", hook=None,
    title="FSCV 2/4: */ (run) and *RUN handler",
    description="""\
Parses the filename via parse_filename_gs and calls infol2,
then falls through to fsreply_4_notify_exec to set up and
send the FS load-as-command request.""")

# ============================================================
# FS reply 4: notify and execute (&8DD5)
# ============================================================
subroutine(0x8DD5, "fsreply_4_notify_exec", hook=None,
    title="FS reply 4: send FS load-as-command and execute response",
    description="""\
Initialises a GS reader to skip past the filename and
calculate the command context address, then sets up an FS
command with function code &05 (FCCMND: load as command)
using send_fs_examine. If a Tube co-processor is present
(tx_in_progress != 0), transfers the response data to the
Tube via tube_addr_claim. Otherwise jumps via the indirect
pointer at (&0F09) to execute at the load address.""")

# ============================================================
# *NET sub-command handlers (&8E3B-&8E75)
# ============================================================
subroutine(0x8E3A, "boot_cmd_execute", hook=None,
    title="Execute boot command via OSCLI",
    description="""\
Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")

# The actual *NET1 handler is at &8E59 (dispatched via table to &8E59).
# The code at &8E3A was incorrectly labeled net_1_read_handle by the
# auto-generator — the address shifted due to the ROM header change.
entry(0x8E59)
label(0x8E59, "net_1_read_handle")
comment(0x8E59, """\
*NET1: read file handle from received packet.
Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
and falls through to net_2_read_handle_entry's common path.""")

subroutine(0x8E47, "calc_handle_offset", hook=None,
    title="Calculate handle workspace offset",
    description="""\
Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""")

label(0x8E58, "return_calc_handle")      # Return from calc_handle_offset (invalid)

entry(0x8E5F)
subroutine(0x8E5F, "net_2_read_handle_entry", hook=None,
    title="*NET2: read handle entry from workspace",
    description="""\
Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""")

entry(0x8E6F)
subroutine(0x8E6F, "net_3_close_handle", hook=None,
    title="*NET3: close handle (mark as unused)",
    description="""\
Looks up the handle in &F0 via calc_handle_offset. Writes
&3F ('?') to mark the handle slot as closed in the NFS
workspace. Preserves the carry flag state across the write
using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.""")

# NMI handler init — ROM code copies to page &04/&05/&06
# ============================================================
# Filing system OSWORD dispatch (&8E76 / &8E80)
# ============================================================
subroutine(0x8E7F, "svc_8_osword", hook=None,
    title="Filing system OSWORD entry",
    description="""\
Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the
PHA/PHA/RTS dispatch at &8E80.""")

comment(0x8E7F, "Command code from &EF", inline=True)
comment(0x8E81, "Subtract &0F: OSWORD &0F-&13 become indices 0-4", inline=True)

subroutine(0x8E97, "fs_osword_dispatch", hook=None,
    title="PHA/PHA/RTS dispatch for filing system OSWORDs",
    description="""\
X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
at &8EB0 (low) / &8EB5 (high).""")

comment(0x8E9F, "Dispatch table: low bytes for OSWORD &0F-&13 handlers", inline=True)
comment(0x8EB5, "Dispatch table: high bytes for OSWORD &0F-&13 handlers", inline=True)

comment(0x815B, "Copy NMI handler code from ROM to RAM pages &04-&06")
comment(0x8175, "Copy NMI workspace initialiser from ROM to &0016-&0076")

# ============================================================
# Econet TX/RX handler (&8FE5)
# ============================================================
subroutine(0x8FE8, "econet_tx_rx", hook=None,
    title="Econet transmit/receive handler",
    description="""\
A=0: Initialise TX control block from ROM template at &8391
     (zero entries substituted from NMI workspace &0DDA), transmit
     it, set up RX control block, and receive reply.
A>=1: Handle transmit result (branch to cleanup at &9034).""")

comment(0x8FE8, "A=0: set up and transmit; A>=1: handle result", inline=True)
comment(0x8F7F, "Load from ROM template (zero = use NMI workspace value)", inline=True)
comment(0x8FAA, "Enable interrupts before transmit", inline=True)
comment(0x8FB0, "Dest station = &FFFF (accept reply from any station)", inline=True)
comment(0x8FC2, "Initiate receive with timeout", inline=True)
# 3.34B had BNE (error/timeout branch) at &8FBF; in 3.35D this was
# restructured into a JMP tail call at &9036, so the comment is removed.

# Data transfer loop (&8FD8-&8FF4)
comment(0x8FD3, "Receive data blocks until command byte = &00 or &0D", inline=True)
comment(0x9062, "Test for end-of-data marker (&0D)", inline=True)

# ============================================================
# OSWORD-style function dispatch (&9074)
# ============================================================
subroutine(0x9076, "osword_dispatch",
    title="NETVEC dispatch handler (ENTRY)",
    description="""\
Indirected from NETVEC at &0224. Saves all registers and flags,
retrieves the reason code from the stacked A, and dispatches to
one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
&908D. Reason codes >= 9 are ignored.

Dispatch targets (from NFS09):
  0:   no-op (RTS)
  1-3: PRINT -- chars in printer buffer / Ctrl-B / Ctrl-C
  4:   NWRCH -- write character to screen (net write char)
  5:   SELECT -- printer selection changed
  6:   no-op (net read char -- not implemented)
  7:   NBYTE -- remote OSBYTE call
  8:   NWORD -- remote OSWORD call""",
    on_entry={"a": "reason code (0-8)"},
    on_exit={"a": "preserved",
             "x": "preserved",
             "y": "preserved"})

comment(0x900A, "Retrieve original A (function code) from stack", inline=True)
comment(0x908F, "PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it", inline=True)

# ============================================================
# NWRCH: net write character (&9036)
# ============================================================
subroutine(0x9039, "net_write_char",
    title="Fn 4: net write character (NWRCH)",
    description="""\
Writes a character (passed in Y) to the screen via OSWRITCH.
Before the write, uses TSX to reach into the stack and zero the
carry flag in the caller's saved processor status byte -- ROR
followed by ASL on the stacked P byte (&0106,X) shifts carry
out and back in as zero. This ensures the calling code's PLP
restores carry=0, signalling "character accepted" without needing
a separate CLC/PHP sequence. A classic 6502 trick for modifying
return flags without touching the actual processor status.""",
    on_entry={"y": "character to write"},
    on_exit={"a": "&3F",
             "x": "0",
             "y": "0"})

comment(0x903A, "ROR/ASL on stacked P: zeros carry to signal success", inline=True)

# ============================================================
# Setup TX and send (&90B8)
# ============================================================
subroutine(0x90BA, "setup_tx_and_send", hook=None,
    title="Set up TX control block and send",
    description="""\
Builds a TX control block at (nfs_workspace)+&0C from the current
workspace state, then initiates transmission via the ADLC TX path.
This is the common send routine used after command data has been
prepared. The exact control block layout and field mapping need
further analysis.""")

# ============================================================
# Control block setup routine (&9168 / &9171)
# ============================================================
subroutine(0x9173, "ctrl_block_setup_alt", hook=None,
    title="Alternate entry into control block setup",
    description="""\
Sets X=&0D, Y=&7C. Tests bit 6 of &83AF to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")

subroutine(0x917C, "ctrl_block_setup", hook=None,
    title="Control block setup — main entry",
    description="""\
Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &91A8 indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")

comment(0x916E, "Load template byte from ctrl_block_template[X]", inline=True)

subroutine(0x91A8, "ctrl_block_template", hook=None,
    title="Control block initialisation template",
    description="""\
Read by the loop at &9176, indexed by X from a starting value
down to 0. Values are stored into either (nfs_workspace) or
(net_rx_ptr) at offset Y, depending on the V flag.

Two entry paths read different slices of this table:
  ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
  ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &8374

Sentinel values:
  &FE = stop processing
  &FD = skip this offset (decrement Y but don't store)
  &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)""")
byte(0x919D, 1)
comment(0x91A8, "Alt-path only → Y=&6F", inline=True)
byte(0x919E, 1)
comment(0x919E, "Alt-path only → Y=&70", inline=True)
byte(0x919F, 1)
comment(0x91AA, "SKIP", inline=True)
byte(0x91A0, 1)
comment(0x91A0, "SKIP", inline=True)
byte(0x91A1, 1)
comment(0x91A1, "→ Y=&01 / Y=&73", inline=True)
byte(0x91A2, 1)
comment(0x91AD, "PAGE byte → Y=&02 / Y=&74", inline=True)
byte(0x91A3, 1)
comment(0x91AE, "→ Y=&03 / Y=&75", inline=True)
byte(0x91A4, 1)
comment(0x91AF, "→ Y=&04 / Y=&76", inline=True)
byte(0x91A5, 1)
comment(0x91B0, "→ Y=&05 / Y=&77", inline=True)
byte(0x91A6, 1)
comment(0x91A6, "PAGE byte → Y=&06 / Y=&78", inline=True)
byte(0x91A7, 1)
comment(0x91A7, "→ Y=&07 / Y=&79", inline=True)
byte(0x91A8, 1)
comment(0x91B3, "→ Y=&08 / Y=&7A", inline=True)
byte(0x91A9, 1)
comment(0x91B4, "→ Y=&09 / Y=&7B", inline=True)
byte(0x91AA, 1)
comment(0x91B5, "→ Y=&0A / Y=&7C", inline=True)
byte(0x91AB, 1)
comment(0x91B6, "STOP — main-path boundary", inline=True)
byte(0x91AC, 1)
comment(0x91AC, "→ Y=&0C (main only)", inline=True)
byte(0x91AD, 1)
comment(0x91AD, "→ Y=&0D (main only)", inline=True)
byte(0x91AE, 1)
byte(0x91AF, 1)
comment(0x91AF, "SKIP (main only)", inline=True)
byte(0x91B0, 1)
comment(0x91B0, "→ Y=&10 (main only)", inline=True)
byte(0x91B1, 1)
byte(0x91B2, 1)
byte(0x91B3, 1)
byte(0x91B4, 1)
byte(0x91B5, 1)
comment(0x91B5, "PAGE byte → Y=&15 (main only)", inline=True)
byte(0x91B6, 1)
comment(0x91B6, "→ Y=&16 (main only)", inline=True)
byte(0x91B7, 1)

# ============================================================
# Bidirectional block copy (&8EB1)
# ============================================================
subroutine(0x8F1C, "copy_param_block", hook=None,
    title="Bidirectional block copy between OSWORD param block and workspace.",
    description="""\
C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)""")

# ============================================================
# OSWORD handler block comments
# ============================================================
label(0x8EB7, "return_copy_param")       # Return from copy_param_block

subroutine(0x8EBA, "osword_0f_handler",
    title="OSWORD &0F handler: initiate transmit (CALLTX)",
    description="""\
Checks the TX semaphore (TXCLR at &0D62) via ASL -- if carry is
clear, a TX is already in progress and the call returns an error,
preventing user code from corrupting a system transmit. Otherwise
copies 16 bytes from the caller's OSWORD parameter block into the
user TX control block (UTXCB) in static workspace. The TXCB
pointer is copied to LTXCBP only after the semaphore is claimed,
ensuring the low-level transmit code (BRIANX) sees a consistent
pointer -- if copied before claiming, another transmitter could
modify TXCBP between the copy and the claim.""",
    on_entry={"x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "corrupted",
             "x": "corrupted",
             "y": "&FF"})

subroutine(0x8ED4, "osword_11_handler", hook=None,
    title="OSWORD &11 handler: read JSR arguments (READRA)",
    description="""\
Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8EE7) to return just the buffer size and args size
without copying the data.""")

subroutine(0x8E85, "osword_12_handler", hook=None,
    title="OSWORD &12 handler: read/set state information (RS)",
    description="""\
Dispatches on the sub-function code (0-9):
  0: read FS station (FSLOCN at &0E00)
  1: set FS station
  2: read printer server station (PSLOCN)
  3: set printer server station
  4: read protection masks (LSTAT at &D63)
  5: set protection masks
  6: read context handles (URD/CSD/LIB, converted from
     internal single-bit form back to handle numbers)
  7: set context handles (converted to internal form)
  8: read local station number
  9: read JSR arguments buffer size
Even-numbered sub-functions read; odd-numbered ones write.
Uses the bidirectional copy at &8EB1 for station read/set.""")

subroutine(0x8F74, "osword_10_handler",
    title="OSWORD &10 handler: open/read RX control block (OPENRX)",
    description="""\
If the first byte of the caller's parameter block is zero, scans
for a free RXCB (flag byte = &3F = deleted) starting from RXCB #3
(RXCBs 0-2 are dedicated: printer, remote, FS). Returns the RXCB
number in the first byte, or zero if none free. If the first byte
is non-zero, reads the specified RXCB's data back into the caller's
parameter block (12 bytes) and then deletes the RXCB by setting
its flag byte to &3F -- a consume-once semantic so user code reads
received data and frees the CB in a single atomic operation,
preventing double-reads. The low-level user RX flag (LFLAG) is
temporarily disabled via ROR/ROL during the operation to prevent
the interrupt-driven receive code from modifying a CB that is
being read or opened.""",
    on_entry={"x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "corrupted",
             "x": "corrupted",
             "y": "&FF"})

# ============================================================
# Remote operation handlers (&846A-&84D1)
# ============================================================
subroutine(0x849A, "lang_1_remote_boot", hook=None,
    title="Remote boot/execute handler",
    description="""\
Checks byte 4 of the RX control block (remote status flag).
If zero (not currently remoted), falls through to remot1 to
set up a new remote session. If non-zero (already remoted),
jumps to clear_jsr_protection and returns.""")

subroutine(0x84C8, "lang_3_execute_at_0100", hook=None,
    title="Execute code at &0100",
    description="""\
Clears JSR protection, zeroes &0100-&0102 (creating a BRK
instruction at &0100 as a safe default), then JMP &0100 to
execute code received over the network. If no code was loaded,
the BRK triggers an error handler.""")

subroutine(0x84D8, "lang_4_remote_validated", hook=None,
    title="Remote operation with source validation",
    description="""\
Validates that the source station in the received packet matches
the controlling station stored in the NFS workspace. If byte 4 of
the RX control block is zero (not currently remoted), allows the
new remote session via remot1. If non-zero, compares the source
station at RX offset &80 against workspace offset &0E -- rejects
mismatched stations via clear_jsr_protection, accepts matching
stations by falling through to lang_0_insert_remote_key.""")

subroutine(0x84E8, "lang_0_insert_remote_key", hook=None,
    title="Insert remote keypress",
    description="""\
Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")

# ============================================================
# Remote operation support routines (&8FCA-&92FE)
# ============================================================
subroutine(0x8FCD, "setup_rx_buffer_ptrs", hook=None,
    title="Set up RX buffer pointers in NFS workspace",
    description="""\
Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &28. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &2C.""")

subroutine(0x90DE, "remote_cmd_dispatch", hook=None,
    title="Fn 7: remote OSBYTE handler (NBYTE)",
    description="""\
Full RPC mechanism for OSBYTE calls across the network. When a
machine is remoted, OSBYTE/OSWORD calls that affect terminal-side
hardware (keyboard scanning, flash rates, etc.) must be indirected
across the net. OSBYTE calls are classified into three categories:
  Y>0 (NCTBPL table): executed on BOTH machines (flash rates etc.)
  Y<0 (NCTBMI table): executed on terminal only, result sent back
  Y=0: not recognised, passed through unhandled
Results returned via stack manipulation: the saved processor status
byte at &0106 has V-flag (bit 6) forced on to tell the MOS the
call was claimed (preventing dispatch to other ROMs), and the I-bit
(bit 2) forced on to disable interrupts during register restoration,
preventing race conditions. The carry flag in the saved P is also
manipulated via ROR/ASL to zero it, signaling success to the caller.
OSBYTE &81 (INKEY) gets special handling as it must read the
terminal's keyboard.""")

subroutine(0x9150, "remote_cmd_data", hook=None,
    title="Fn 8: remote OSWORD handler (NWORD)",
    description="""\
Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget -- no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")

subroutine(0x91CF, "printer_select_handler", hook=None,
    title="Fn 5: printer selection changed (SELECT)",
    description="""\
Called when the printer selection changes. Compares X against
the network printer buffer number (&F0). If it matches,
initialises the printer buffer pointer (&0D61 = &1F) and
sets the initial flag byte (&0D60 = &41). Otherwise falls
through to return.""")

subroutine(0x91DF, "remote_print_handler", hook=None,
    title="Fn 1/2/3: network printer handler (PRINT)",
    description="""\
Handles network printer output. Reason 1 = chars in buffer (extract
from MOS buffer 3 and accumulate), reason 2 = Ctrl-B (start print),
reason 3 = Ctrl-C (end print). The printer status byte PFLAGS uses:
  bit 7 = sequence number (toggles per packet for dup detection)
  bit 6 = always 1 (validity marker)
  bit 0 = 0 when print active
Print streams reuse the BSXMIT (byte-stream transmit) code with
handle=0, which causes the AND SEQNOS to produce zero and sidestep
per-file sequence tracking. After transmission, TXCB pointer bytes
are filled with &FF to prevent stale values corrupting subsequent
BGET/BPUT operations (a historically significant bug fix).
N.B. The printer and REMOTE facility share the same dynamically
allocated static workspace page via WORKP1 (&9E,&9F) — care must
be taken to never leave the pointer corrupted, as corruption would
cause one subsystem to overwrite the other's data.
Only handles buffer 4 (network printer); others are ignored.""")

subroutine(0x9204, "store_output_byte", hook=None,
    title="Store output byte to network buffer",
    description="""\
Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""")

subroutine(0x9230, "flush_output_block", hook=None,
    title="Flush output block",
    description="""\
Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")

subroutine(0x92F2, "save_vdu_state", hook=None,
    title="Save VDU workspace state",
    description="""\
Stores the cursor position value from &0355 into NFS workspace,
then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
each result into consecutive workspace bytes.""")

# ============================================================
# ADLC initialisation (&966F)
# ============================================================
subroutine(0x966F, "adlc_init", hook=None,
    title="ADLC initialisation",
    description="""\
Reads station ID (INTOFF side effect), performs full ADLC reset,
checks for Tube presence (OSBYTE &EA), then falls through to
adlc_init_workspace.""")

subroutine(0x968A, "adlc_init_workspace", hook=None,
    title="Initialise NMI workspace",
    description="""\
New in 3.35D: issues OSBYTE &8F with X=&0C (NMI claim service
request) before copying the NMI shim. Sub-entry at &968A skips
the service request for quick re-init. Then copies 32 bytes of
NMI shim from ROM (&9FA8) to RAM (&0D00), patches the current
ROM bank number into the shim's self-modifying code at &0D07,
sets TX clear flag and econet_init_flag to &80, reads station ID
from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
and re-enables NMIs by reading &FE20 (INTON side effect).""")

subroutine(0x96C8, "save_econet_state", hook=None,
    title="Save Econet state to RX control block",
    description="""\
Stores rx_status_flags, protection_mask, and tx_in_progress
to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.""")

# restore_econet_state and install_nmi_shim were restructured in 3.35D
# into a new initialisation sequence at &968A that issues OSBYTE &8F
# service request before copying the NMI shim from &9FE8 to &0D00.

# ============================================================
# Relocated code block comments
# ============================================================
subroutine(0x0016, "tube_brk_handler", hook=None,
    title="Tube BRK handler (BRKV target) — reference: NFS11 NEWBR",
    description="""\
Sends error information to the Tube co-processor via R2 and R4:
  1. Sends &FF to R4 (WRIFOR) to signal error
  2. Reads R2 data (flush any pending byte)
  3. Sends &00 via R2, then error number from (&FD),0
  4. Loops sending error string bytes via R2 until zero terminator
  5. Falls through to tube_reset_stack → tube_main_loop
The main loop continuously polls R1 for WRCH requests (forwarded
to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
14-entry table at &0500). The R2 command byte is stored at &55
before dispatch via JMP (&0500).""")

subroutine(0x0400, "tube_code_page4", hook=None,
    title="Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)",
    description="""\
Copied from ROM at &934D during init. The first 28 bytes (&0400-&041B)
overlap with the end of the ZP block (the same ROM bytes serve both
the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
  &0400: JMP &0473 (BEGIN — CLI parser / startup entry)
  &0403: JMP &06E2 (tube_escape_check)
  &0406: tube_addr_claim — Tube address claim protocol (ADRR)
  &0414: tube_post_init — called after ROM→RAM copy
  &0473: BEGIN — startup/CLI entry, break type check
  &04E7: tube_rdch_handler — RDCHV target
  &04EF: tube_restore_regs — restore X,Y, dispatch entry 6
  &04F7: tube_read_r2 — poll R2 status, read data byte to A""")

subroutine(0x0500, "tube_dispatch_table", hook=None,
    title="Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)",
    description="""\
Copied from ROM at &944D during init. Contains:
  &0500: tube_dispatch_table — 14-entry handler address table
  &051C: tube_wrch_handler — WRCHV target
  &051F: tube_send_and_poll — send byte via R2, poll for reply
  &0527: tube_poll_r1_wrch — service R1 WRCH while waiting for R2
  &053D: tube_release_return — restore regs and RTS
  &0543: tube_osbput — write byte to file
  &0550: tube_osbget — read byte from file
  &055B: tube_osrdch — read character
  &0569: tube_osfind — open file
  &0580: tube_osfind_close — close file (A=0)
  &058C: tube_osargs — file argument read/write
  &05B1: tube_read_string — read CR-terminated string into &0700
  &05C5: tube_oscli — execute * command
  &05CB: tube_reply_ack — send &7F acknowledge
  &05CD: tube_reply_byte — send byte and return to main loop
  &05D8: tube_osfile — whole file operation""")

# No tube_code_page6 subroutine in 3.40 — the page 5/6 boundary
# at &05FF/&0600 splits a BVC instruction (opcode $50 at &05FF,
# operand $FB at &0600). Page 6 is a seamless continuation of
# page 5 code, not a separate entry point.
#
# The Tube client code was completely rewritten in 3.40. Page 6
# contains (runtime addresses):
#   &0601: OSBYTE result — write X to R2, return to main loop
#   &0607: tube_osbyte_long — 3-param OSBYTE via R2
#   &062B: tube_osword_read — read OSWORD params from R2
#   &0645: tube_osword_dispatch — call OSWORD, send results
#   &0668: tube_osword_param_read — read OSWORD param block
#   &0680: tube_rdln_send_line — RDLN response via R2
#   &0695: tube_send_r2 — poll R2 status, write A to R2
#   &069E: tube_send_r4 — poll R4 status, write A to R4
#   &06A7: tube_escape_check — check &FF, forward via R1
#   &06AD: tube_event_handler — EVNTV handler, send via R1
#   &06BC: tube_send_r1 — poll R1 status, write A to R1
#   &06C5: tube_read_r2 — poll R2, read byte from R2

# ============================================================
# OSBYTE code table for VDU state save (&9312)
# ============================================================
# In 3.35K, &9312-&9314 was the osbyte_vdu_table (3 data bytes).
# In 3.40, the code shifted so &9310-&9315 is now code
# (read_vdu_osbyte: JSR osbyte; TXA; LDX #0).
# The osbyte_vdu_table is at different addresses in 3.40.

# ============================================================
# Relocated code block sources (&9308, &934D, &944D, &954D)
# ============================================================
# These labels mark the ROM storage addresses. The code is
# disassembled at its runtime addresses via move() declarations
# near the top of this file. See the preamble for addresses.

# ============================================================
# Econet TX retry (&9256)
# ============================================================
subroutine(0x9261, "econet_tx_retry", hook=None,
    title="Transmit with retry loop (XMITFS/XMITFY)",
    description="""\
Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
retries and FSDELY (&60 = 96) ms delay between attempts. On each
iteration, checks the result code: zero means success, non-zero
means retry. After all retries exhausted, reports a 'Net error'.
Entry point XMITFY allows a custom delay in Y.""")

# ============================================================
# Save palette and VDU state (&929F)
# ============================================================
subroutine(0x92A6, "lang_2_save_palette_vdu", hook=None,
    title="Save palette and VDU state (CVIEW)",
    description="""\
Part of the VIEW facility (second iteration, started 27/7/82).
Uses dynamically allocated buffer store. The WORKP1 pointer
(&9E,&9F) serves double duty: non-zero indicates data ready AND
provides the buffer address — an efficient use of scarce zero-
page space. This code must be user-transparent as the NFS may not
be the dominant filing system.
Reads all 16 palette entries using OSWORD &0B (read palette) and
stores the results. Then reads cursor position (OSBYTE &85),
shadow RAM allocation (OSBYTE &C2), and screen start address
(OSBYTE &C3) using the 3-entry table at &9319.
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")

# ============================================================
# Post-ACK scout processing (&99C5)
# ============================================================
subroutine(0x9992, "post_ack_scout", hook=None,
    title="Post-ACK scout processing",
    description="""\
Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")

# ============================================================
# Immediate operation handler (&9A6F)
# ============================================================
subroutine(0x9A56, "immediate_op", hook=None,
    title="Immediate operation handler (port = 0)",
    description="""\
Handles immediate (non-data-transfer) operations received via
scout frames with port byte = 0. The control byte (&0D3F)
determines the operation type:
  &81 = PEEK (read memory)
  &82 = POKE (write memory)
  &83 = JSR (remote procedure call)
  &84 = user procedure
  &85 = OS procedure
  &86 = HALT
  &87 = CONTINUE
The protection mask (LSTAT at &D63) controls which operations
are permitted — each bit enables or disables an operation type.
If the operation is not permitted by the mask, it is silently
ignored. LSTAT can be read/set via OSWORD &12 sub-functions 4/5.""")

# ============================================================
# Discard paths (&9A4A / &9A56 / &9A6F)
# ============================================================
subroutine(0x9A2E, "discard_reset_listen", hook=None,
    title="Discard with full ADLC reset",
    description="""\
Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
then falls through to discard_after_reset. Used when the ADLC is
in an unexpected state and needs a hard reset before returning
to idle listen mode. 5 references — the main error recovery path.""")

subroutine(0x9A3D, "discard_listen", hook=None,
    title="Discard frame (gentle)",
    description="""\
Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
current frame reception without a full reset, then falls through
to discard_after_reset. Used for clean rejection of frames that
are correctly formatted but not for us (wrong station/network).""")

subroutine(0x9A56, "discard_after_reset", hook=None,
    title="Return to idle listen after reset/discard",
    description="""\
Just calls adlc_rx_listen (CR1=&82, CR2=&67) to re-enter idle
RX mode, then RTI. The simplest of the three discard paths —
used as the tail of both discard_reset_listen and discard_listen.""")

# ============================================================
# Unreferenced data block (&9F5A-&9F69)
# ============================================================
# 16 bytes of unreferenced data between tx_store_result and
# tx_calc_transfer. No code in any NFS version references this
# block. The byte pattern suggests two 8-entry lookup tables
# (possibly ADLC control register values), but their original
# purpose is unknown.
comment(0x9F28, "Unreferenced data block (purpose unknown)")
byte(0x9F5A, 16)

# ============================================================
# Transfer size calculation (&9F6A)
# ============================================================
subroutine(0x9F38, "tx_calc_transfer", hook=None,
    title="Calculate transfer size",
    description="""\
Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")

# ============================================================
# NMI shim at end of ROM (&9FD9-&9FFF)
# ============================================================
subroutine(0x9FA8, "nmi_bootstrap_entry", hook=None,
    title="Bootstrap NMI entry point (in ROM)",
    description="""\
An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&9700). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &9700.""")

subroutine(0x9FB6, "rom_set_nmi_vector", hook=None,
    title="ROM copy of set_nmi_vector + nmi_rti",
    description="""\
A version of the NMI vector-setting subroutine and RTI sequence
that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
one normally used at runtime; this ROM copy is used during early
initialisation before the RAM workspace has been set up, and as
the source for the initial copy to RAM.""")

# ============================================================
# Secondary dispatch entries (indices 19-32)
# ============================================================
# These are accessed via callers at &80B4 and &80C7 which set
# different Y base offsets. They handle *-command parsing and
# filing system operations. The exact mapping of indices to
# handlers hasn't been fully traced yet.

# ============================================================
# OSWORD &12 handler detail
# ============================================================
# OSWORD &12 (RS) dispatches on sub-function codes 0-9:
# read/set FS station, printer station, protection masks,
# context handles (URD/CSD/LIB), local station, JSR buffer size.
# Uses the bidirectional copy at &8EB1 to transfer data between
# the OSWORD parameter block and the FS workspace.

# ============================================================
# ADLC full reset (&96E6)
# ============================================================
subroutine(0x96D8, "adlc_full_reset", hook=None,
    title="ADLC full reset",
    description="""\
Aborts all activity and returns to idle RX listen mode.""")

comment(0x96D8, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", inline=True)
comment(0x96E7, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", inline=True)
comment(0x96E2, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", inline=True)

# ============================================================
# Enter RX listen mode (&96F5)
# ============================================================
subroutine(0x96E7, "adlc_rx_listen", hook=None,
    title="Enter RX listen mode",
    description="""\
TX held in reset, RX active with interrupts. Clears all status.""")

comment(0x96E7, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", inline=True)
comment(0x96EC, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", inline=True)

# ============================================================
# NMI RX scout handler (&9700) — idle listen
# ============================================================
subroutine(0x96F2, "nmi_rx_scout", hook=None,
    title="NMI RX scout handler (initial byte)",
    description="""\
Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")

comment(0x96F2, "A=&01: mask for SR2 bit0 (AP = Address Present)", inline=True)
comment(0x96F4, "BIT SR2: Z = A AND SR2 -- tests if AP is set", inline=True)
comment(0x96F7, "AP not set, no incoming data -- check for errors", inline=True)
comment(0x96F9, "Read first RX byte (destination station address)", inline=True)
comment(0x96FC, "Compare to our station ID (&FE18 read = INTOFF, disables NMIs)", inline=True)
comment(0x96FF, "Match -- accept frame", inline=True)
comment(0x9701, "Check for broadcast address (&FF)", inline=True)
comment(0x9703, "Neither our address nor broadcast -- reject frame", inline=True)
comment(0x9705, "Flag &40 = broadcast frame", inline=True)
comment(0x970A, "Install next NMI handler at &9715 (RX scout second byte)", inline=True)

# ============================================================
# RX scout second byte handler (&971F)
# ============================================================
subroutine(0x9711, "nmi_rx_scout_net", hook=None,
    title="RX scout second byte handler",
    description="""\
Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &9747.""")

comment(0x9711, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x9714, "No RDA -- check errors", inline=True)
comment(0x9716, "Read destination network byte", inline=True)
comment(0x9719, "Network = 0 -- local network, accept", inline=True)
comment(0x971B, "EOR &FF: test if network = &FF (broadcast)", inline=True)
comment(0x971D, "Broadcast network -- accept", inline=True)
comment(0x971F, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", inline=True)

comment(0x9727, "Network = &FF broadcast: clear &0D4A", inline=True)
comment(0x972A, "Store Y offset for scout data buffer", inline=True)
comment(0x972C, "Install scout data reading loop at &9747", inline=True)

# ============================================================
# Error/discard path (&9741)
# ============================================================
subroutine(0x9733, "scout_error", hook=None,
    title="Scout error/discard handler",
    description="""\
Reached when the scout data loop sees no RDA (BPL at &9756) or
when scout completion finds unexpected SR2 state.
If SR2 & &81 is non-zero (AP or RDA still active), performs full
ADLC reset and discards. If zero (clean end), discards via &9A56.
This path is a common landing for any unexpected ADLC state during
scout reception.""")

comment(0x9733, "Read SR2", inline=True)
comment(0x9736, "Test AP (b0) | RDA (b7)", inline=True)
comment(0x9738, "Neither set -- clean end, discard via &9A40", inline=True)
comment(0x973A, "Unexpected data/status: full ADLC reset", inline=True)
comment(0x973D, "Discard and return to idle", inline=True)

# ============================================================
# Scout data reading loop (&9747-&976E)
# ============================================================
# This is the critical Path 1 code for ADLC FV/PSE interaction.
# The loop reads scout body bytes two at a time, storing them at
# &0D3D+Y. Between each pair, it checks SR2 to detect frame
# completion (FV set) or errors.
#
# ADLC timing requirement: after the CPU reads the penultimate byte,
# FV must be visible in SR2 before the next SR2 check. Beebium's
# inline refill + byte timer reset ensures this: reading the
# penultimate byte triggers inline refill of the last byte, which
# sets FV immediately (push-time FV). The byte timer reset prevents
# the timer from firing mid-loop.
subroutine(0x9743, hook=None,
    title="Scout data reading loop",
    description="""\
Reads the body of a scout frame, two bytes per iteration. Stores
bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
Between each pair it checks SR2:
  - SR2 & &81 tested at entry (&974A): AP|RDA bits
    - Neither set (BEQ) -> discard (&974E -> &9A56)
    - AP without RDA (BPL) -> error (&9741)
    - RDA set (BMI) -> read byte
  - After first byte (&9755): full SR2 tested
    - SR2 non-zero (BNE) -> scout completion (&977B)
      This is the FV detection point: when FV is set (by inline refill
      of the last byte during the preceding RX FIFO read), SR2 is
      non-zero and the branch is taken.
    - SR2 = 0 -> read second byte and loop
  - After second byte (&9769): re-test SR2 & &81 for next pair
    - RDA set (BMI) -> loop back to &974E
    - Neither set -> RTI, wait for next NMI
The loop ends at Y=&0C (12 bytes max in scout buffer).""")

comment(0x9743, "Y = buffer offset", inline=True)
comment(0x9745, "Read SR2", inline=True)
comment(0x9748, "No RDA -- error handler &9737", inline=True)
comment(0x974A, "Read data byte from RX FIFO", inline=True)
comment(0x974D, "Store at &0D3D+Y (scout buffer)", inline=True)
comment(0x9750, "Advance buffer index", inline=True)
comment(0x9751, "Read SR2 again (FV detection point)", inline=True)
comment(0x9754, "RDA set -- more data, read second byte", inline=True)
comment(0x9756, "SR2 non-zero (FV or other) -- scout completion", inline=True)
comment(0x9758, "Read second byte of pair", inline=True)
comment(0x975B, "Store at &0D3D+Y", inline=True)
comment(0x975E, "Advance and check buffer limit", inline=True)
comment(0x9761, "Buffer full (Y=12) -- force completion", inline=True)
comment(0x976D, "Save Y for next iteration", inline=True)
comment(0x9765, "Read SR2 for next pair", inline=True)
comment(0x9768, "SR2 non-zero -- loop back for more bytes", inline=True)
comment(0x976A, "SR2 = 0 -- RTI, wait for next NMI", inline=True)

# ============================================================
# Scout completion (&977B-&978F)
# ============================================================
subroutine(0x976D, "scout_complete", hook=None,
    title="Scout completion handler",
    description="""\
Reached from the scout data loop when SR2 is non-zero (FV detected).
Disables PSE to allow individual SR2 bit testing:
  CR1=&00 (clear all enables)
  CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
Then checks FV (bit1) and RDA (bit7):
  - No FV (BEQ) -> error &9741 (not a valid frame end)
  - FV set, no RDA (BPL) -> error &9741 (missing last byte)
  - FV set, RDA set -> read last byte, process scout
After reading the last byte, the complete scout buffer (&0D3D-&0D48)
contains: src_stn, src_net, ctrl, port [, extra_data...].
The port byte at &0D40 determines further processing:
  - Port = 0 -> immediate operation (&9A6F)
  - Port non-zero -> check if it matches an open receive block""")

comment(0x976D, "CR1=&00: disable all interrupts", inline=True)
comment(0x9772, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", inline=True)
comment(0x9777, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9779, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x977C, "No FV -- not a valid frame end, error", inline=True)
comment(0x977E, "FV set but no RDA -- missing last byte, error", inline=True)
comment(0x9780, "Read last byte from RX FIFO", inline=True)
comment(0x9783, "Store last byte at &0D3D+Y", inline=True)
comment(0x9786, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", inline=True)
comment(0x978B, "Check port byte: 0 = immediate op, non-zero = data transfer", inline=True)
comment(0x978E, "Port non-zero -- look for matching receive block", inline=True)
comment(0x9790, "Port = 0 -- immediate operation handler", inline=True)

# ============================================================
# Data RX handler (&9843-&98D8)
# ============================================================
# This handler chain receives the data frame in a four-way handshake.
# After sending the scout ACK, the ROM installs &9843 to receive
# the incoming data frame.
subroutine(0x9821, "nmi_data_rx", hook=None,
    title="Data frame RX handler (four-way handshake)",
    description="""\
Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &9843 (AP+addr check) -> &9859 (net=0 check) ->
&986F (skip ctrl+port) -> &98A4 (bulk data read) -> &98D8 (completion)""")

comment(0x9815, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", inline=True)
comment(0x9821, "Read SR2 for AP check", inline=True)
comment(0x9837, "Validate source network = 0", inline=True)
comment(0x984D, "Skip control and port bytes (already known from scout)", inline=True)
comment(0x9852, "Discard control byte", inline=True)
comment(0x9855, "Discard port byte", inline=True)

# ============================================================
# Data frame bulk read (&98A4-&98D8)
# ============================================================
subroutine(0x9880, "nmi_data_rx_bulk", hook=None,
    title="Data frame bulk read loop",
    description="""\
Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &98D8.
SR2 = 0 -> RTI, wait for next NMI to continue.""")

comment(0x9880, "Y = buffer offset, resume from last position", inline=True)
comment(0x9882, "Read SR2 for next pair", inline=True)

# ============================================================
# Data frame completion (&98D8-&98F4)
# ============================================================
subroutine(0x98B4, "data_rx_complete", hook=None,
    title="Data frame completion",
    description="""\
Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&977B): disables PSE (CR1=&00,
CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &9968.""")

comment(0x98B4, "CR1=&00: disable all interrupts", inline=True)
comment(0x98B9, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x98C0, "A=&02: FV mask", inline=True)
comment(0x98C2, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x98C5, "No FV -- error", inline=True)
comment(0x98C7, "FV set, no RDA -- proceed to ACK", inline=True)
comment(0x98CD, "FV+RDA: read and store last data byte", inline=True)

# ============================================================
# Scout ACK / Final ACK TX (&9968-&99B5)
# ============================================================
subroutine(0x9944, "ack_tx", hook=None,
    title="ACK transmission",
    description="""\
Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&9F48).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")

comment(0x994F, "CR1=&44: RX_RESET | TIE (switch to TX mode)", inline=True)
comment(0x9954, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x9959, "Install saved next handler (&99BB for scout ACK)", inline=True)
comment(0x9963, "Load dest station from RX scout buffer", inline=True)
comment(0x9966, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9969, "TDRA not ready -- error", inline=True)
comment(0x996B, "Write dest station to TX FIFO", inline=True)
comment(0x996E, "Write dest network to TX FIFO", inline=True)
comment(0x9974, "Install handler at &9992 (write src addr)", inline=True)

subroutine(0x997B, "nmi_ack_tx_src", hook=None,
    title="ACK TX continuation",
    description="""\
Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
comment(0x997B, "Load our station ID (also INTOFF)", inline=True)
comment(0x997E, "BIT SR1: test TDRA", inline=True)
comment(0x9981, "TDRA not ready -- error", inline=True)
comment(0x9983, "Write our station to TX FIFO", inline=True)
comment(0x9986, "Write network=0 to TX FIFO", inline=True)
comment(0x9990, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x9995, "Install saved handler from &0D4B/&0D4C", inline=True)

# ============================================================
# INACTIVE polling loop (&9C57)
# ============================================================
subroutine(0x9C2F, "inactive_poll", hook=None,
    title="INACTIVE polling loop",
    description="""\
Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9C66-&9C6B works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")

comment(0x9C34, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9C36, "A=&04: INACTIVE mask for SR2 bit2", inline=True)
comment(0x9C3A, "INTOFF -- disable NMIs", inline=True)
comment(0x9C3D, "INTOFF again (belt-and-braces)", inline=True)
comment(0x9C40, "BIT SR2: Z = &04 AND SR2 -- tests INACTIVE", inline=True)
comment(0x9C43, "INACTIVE not set -- re-enable NMIs and loop", inline=True)
comment(0x9C45, "Read SR1 (acknowledge pending interrupt)", inline=True)
comment(0x9C48, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x9C4D, "A=&10: CTS mask for SR1 bit4", inline=True)
comment(0x9C4F, "BIT SR1: tests CTS present", inline=True)
comment(0x9C52, "CTS set -- clock hardware detected, start TX", inline=True)
comment(0x9C54, "INTON -- re-enable NMIs (&FE20 read)", inline=True)
comment(0x9C58, "3-byte timeout counter on stack", inline=True)

# ============================================================
# Timeout error (&9C97) and TX setup (&9C93)
# ============================================================
comment(0x9C6B, "TX_ACTIVE branch (A=&44 = CR1 value for TX active)")
subroutine(0x9C6F, "tx_line_jammed", hook=None,
    title="TX timeout error handler (Line Jammed)",
    description="""\
Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")

comment(0x9C6F, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", inline=True)
comment(0x9C77, "Error &40 = 'Line Jammed'", inline=True)

# ============================================================
# TX preparation (&9CB1)
# ============================================================
subroutine(0x9C89, "tx_prepare", hook=None,
    title="TX preparation",
    description="""\
Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9D5B, and re-enables NMIs.""")

comment(0x9C89, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9C8C, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", inline=True)
comment(0x9C91, "Install NMI handler at &9D4C (TX data handler)", inline=True)
comment(0x9C9B, "INTON -- NMIs now fire for TDRA (&FE20 read)", inline=True)

# ============================================================
# NMI TX data handler (&9D5B)
# ============================================================
subroutine(0x9D2D, "nmi_tx_data", hook=None,
    title="NMI TX data handler",
    description="""\
Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")

comment(0x9D2D, "Load TX buffer index", inline=True)
comment(0x9D30, "BIT SR1: V=bit6(TDRA), N=bit7(IRQ)", inline=True)
comment(0x9D33, "TDRA not set -- TX error", inline=True)
comment(0x9D35, "Load byte from TX buffer", inline=True)
comment(0x9D38, "Write to TX_DATA (continue frame)", inline=True)
comment(0x9D43, "Write second byte to TX_DATA", inline=True)
comment(0x9D46, "Compare index to TX length", inline=True)
comment(0x9D49, "Frame complete -- go to TX_LAST_DATA", inline=True)
comment(0x9D4B, "Check if we can send another pair", inline=True)
comment(0x9D4E, "IRQ set -- send 2 more bytes (tight loop)", inline=True)
comment(0x9D50, "RTI -- wait for next NMI", inline=True)

# TX error path (&9D81-&9D85)
comment(0x9D53, "TX error path")
comment(0x9D53, "Error &42", inline=True)
comment(0x9D57, "CR2=&67: clear status, return to listen", inline=True)
comment(0x9D5C, "Error &41 (TDRA not ready)", inline=True)
comment(0x9D5E, "INTOFF (also loads station ID)", inline=True)
comment(0x9D61, "PHA/PLA delay loop (256 iterations for NMI disable)", inline=True)
comment(0x9D75, "Jump to error handler", inline=True)

# ============================================================
# TX_LAST_DATA and frame completion (&9D97)
# ============================================================
subroutine(0x9D69, "tx_last_data", hook=None,
    title="TX_LAST_DATA and frame completion",
    description="""\
Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &9DA3 which switches to RX mode.
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)""")

comment(0x9D69, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x9D6E, "Install NMI handler at &9D94 (TX completion)", inline=True)

# ============================================================
# TX completion: switch to RX mode (&9DA3)
# ============================================================
subroutine(0x9D75, "nmi_tx_complete", hook=None,
    title="TX completion: switch to RX mode",
    description="""\
Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> completion at &9F48
  - bit0 set at &0D4A -> four-way handshake data phase at &9EEC
  - Otherwise -> install RX reply handler at &9DC1""")

comment(0x9D75, "CR1=&82: TX_RESET | RIE (now in RX mode)", inline=True)
comment(0x9D7A, "Test workspace flags", inline=True)
comment(0x9D7D, "bit6 not set -- check bit0", inline=True)
comment(0x9D7F, "bit6 set -- TX completion", inline=True)
comment(0x9D89, "bit0 set -- four-way handshake data phase", inline=True)
comment(0x9D8C, "Install RX reply handler at &9DB2", inline=True)

# ============================================================
# RX reply scout handler (&9DC1)
# ============================================================
subroutine(0x9D93, "nmi_reply_scout", hook=None,
    title="RX reply scout handler",
    description="""\
Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")

comment(0x9D93, "A=&01: AP mask for SR2", inline=True)
comment(0x9D95, "BIT SR2: test AP (Address Present)", inline=True)
comment(0x9D98, "No AP -- error", inline=True)
comment(0x9DA9, "Read RX byte (destination station)", inline=True)
comment(0x9D9D, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x9DA0, "Not our station -- error/reject", inline=True)
comment(0x9DA2, "Install next handler at &9DC8 (reply continuation)", inline=True)

# ============================================================
# RX reply continuation handler (&9DD7)
# ============================================================
subroutine(0x9DA9, "nmi_reply_cont", hook=None,
    title="RX reply continuation handler",
    description="""\
Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs &9DF2 for the
remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DD9.
If IRQ is still set, falls through directly to &9DF2 without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")

comment(0x9DA9, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x9DAC, "No RDA -- error", inline=True)
comment(0x9DAE, "Read destination network byte", inline=True)
comment(0x9DB1, "Non-zero -- network mismatch, error", inline=True)
comment(0x9DB3, "Install next handler at &9DE3 (reply validation)", inline=True)
comment(0x9DB7, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
comment(0x9DBA, "IRQ set -- fall through to &9DE3 without RTI", inline=True)
comment(0x9DBC, "IRQ not set -- install handler and RTI", inline=True)

# ============================================================
# RX reply validation handler (&9DF2)
# ============================================================
# This is the critical Path 2 code for ADLC FV/PSE interaction.
# The handler reads two bytes (source station and network) and
# then checks for FV. The key requirement is that RDA must be
# visible at &9DF2 even if FV has been latched.
#
# With Beebium's inline refill model, this works because the
# inline refill chain feeds bytes in rapid succession: each FIFO
# read refills the next byte. For a 4-byte reply scout:
#   Read byte 0 at &9DB9 -> refills byte 1 (RDA visible at &9DD7)
#   Read byte 1 at &9DCD -> refills byte 2 (RDA visible at &9DF2)
#   Read byte 2 at &9DE8 -> refills byte 3/LAST (FV set)
#   Read byte 3 at &9DF1 -> FIFO empty
#   Check FV at &9DFA -> FV is set
subroutine(0x9DC2, "nmi_reply_validate", hook=None,
    title="RX reply validation (Path 2 for FV/PSE interaction)",
    description="""\
Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &9DF2 -- must see data available
  2. Read source station at &9DE8, compare to &0D20 (tx_dst_stn)
  3. Read source network at &9DF0, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &9DFA -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")

comment(0x9DC2, "BIT SR2: test RDA (bit7). Must be set for valid reply.", inline=True)
comment(0x9DC5, "No RDA -- error (FV masking RDA via PSE would cause this)", inline=True)
comment(0x9DC7, "Read source station", inline=True)
comment(0x9DCA, "Compare to original TX destination station (&0D20)", inline=True)
comment(0x9DCD, "Mismatch -- not the expected reply, error", inline=True)
comment(0x9DCF, "Read source network", inline=True)
comment(0x9DD2, "Compare to original TX destination network (&0D21)", inline=True)
comment(0x9DD5, "Mismatch -- error", inline=True)
comment(0x9DD7, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9DD9, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9DDC, "No FV -- incomplete frame, error", inline=True)
comment(0x9DDE, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", inline=True)
comment(0x9DE3, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", inline=True)
comment(0x9DE8, "Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C", inline=True)
comment(0x9DF2, "Load dest station for scout ACK TX", inline=True)
comment(0x9DF5, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9DF8, "TDRA not ready -- error", inline=True)
comment(0x9DFA, "Write dest station to TX FIFO", inline=True)
comment(0x9DFD, "Write dest network to TX FIFO", inline=True)
comment(0x9E03, "Install handler at &9E2B (write src addr for scout ACK)", inline=True)

# ============================================================
# TX data phase: write src address (&9E3A)
# ============================================================
subroutine(0x9E0A, "nmi_scout_ack_src", hook=None,
    title="TX scout ACK: write source address",
    description="""\
Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
comment(0x9E0A, "Load our station ID (also INTOFF)", inline=True)
comment(0x9E0D, "BIT SR1: test TDRA", inline=True)
comment(0x9E10, "TDRA not ready -- error", inline=True)
comment(0x9E12, "Write our station to TX FIFO", inline=True)
comment(0x9E15, "Write network=0 to TX FIFO", inline=True)

# ============================================================
# TX data phase: send data payload (&9E5F)
# ============================================================
subroutine(0x9E2F, "nmi_data_tx", hook=None,
    title="TX data phase: send payload",
    description="""\
Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9D5B but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
comment(0x9E2F, "Y = buffer offset, resume from last position", inline=True)
comment(0x9E31, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9E34, "TDRA not ready -- error", inline=True)
comment(0x9E36, "Write data byte to TX FIFO", inline=True)
comment(0x9E5C, "CR2=&3F: TX_LAST_DATA (close data frame)", inline=True)

# ============================================================
# Four-way handshake: switch to RX for final ACK (&9EEC)
# ============================================================
subroutine(0x9EBA, "handshake_await_ack", hook=None,
    title="Four-way handshake: switch to RX for final ACK",
    description="""\
After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9EF8 to receive the final ACK from the remote station.""")
comment(0x9EBA, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", inline=True)
comment(0x9EBF, "Install handler at &9EE9 (RX final ACK)", inline=True)

# ============================================================
# Four-way handshake: RX final ACK (&9EF8-&9F4C)
# ============================================================
# Same pattern as &9DC1/&9DD7/&9DF2 but for the final ACK.
# Validates that the final ACK is from the expected station.
subroutine(0x9EC6, "nmi_final_ack", hook=None,
    title="RX final ACK handler",
    description="""\
Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9DC1-&9DF2):
  &9EF8: Check AP, read dest_stn, compare to our station
  &9F0E: Check RDA, read dest_net, validate = 0
  &9F24: Check RDA, read src_stn/net, compare to TX dest
  &9F32: Check FV for frame completion
On success, stores result=0 at &9F48. On any failure, error &41.""")

comment(0x9EC6, "A=&01: AP mask", inline=True)
comment(0x9EC8, "BIT SR2: test AP", inline=True)
comment(0x9ECB, "No AP -- error", inline=True)
comment(0x9ECD, "Read dest station", inline=True)
comment(0x9ED0, "Compare to our station (INTOFF side effect)", inline=True)
comment(0x9ED3, "Not our station -- error", inline=True)
comment(0x9ED5, "Install handler at &9EFF (final ACK continuation)", inline=True)

comment(0x9EDC, "BIT SR2: test RDA", inline=True)
comment(0x9EDF, "No RDA -- error", inline=True)
comment(0x9EE1, "Read dest network", inline=True)
comment(0x9EE4, "Non-zero -- network mismatch, error", inline=True)
comment(0x9EE6, "Install handler at &9F15 (final ACK validation)", inline=True)
comment(0x9EEA, "BIT SR1: test IRQ -- more data ready?", inline=True)
comment(0x9EED, "IRQ set -- fall through to &9F15 without RTI", inline=True)

subroutine(0x9EF2, "nmi_final_ack_validate", hook=None,
    title="Final ACK validation",
    description="""\
Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
comment(0x9EF2, "BIT SR2: test RDA", inline=True)
comment(0x9EF5, "No RDA -- error", inline=True)
comment(0x9EF7, "Read source station", inline=True)
comment(0x9EFA, "Compare to TX dest station (&0D20)", inline=True)
comment(0x9EFD, "Mismatch -- error", inline=True)
comment(0x9EFF, "Read source network", inline=True)
comment(0x9F02, "Compare to TX dest network (&0D21)", inline=True)
comment(0x9F05, "Mismatch -- error", inline=True)
comment(0x9F0F, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9F11, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9F14, "No FV -- error", inline=True)

# ============================================================
# Completion and error handlers (&9F48-&9F48)
# ============================================================
subroutine(0x9F16, "tx_result_ok", hook=None,
    title="TX completion handler",
    description="""\
Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls full ADLC reset + idle listen via &9A4A.""")
comment(0x9F16, "A=0: success result code", inline=True)
comment(0x9F18, "BEQ: always taken (A=0)", inline=True)

subroutine(0x9F1C, "tx_store_result", hook=None,
    title="TX error handler",
    description="""\
Stores error code (A) into the TX control block, sets &0D3A bit7
for completion, and returns to idle via &9A4A.
Error codes: &00=success, &40=line jammed, &41=not listening,
&42=net error.""")
comment(0x9F1C, "Y=0: index into TX control block", inline=True)
comment(0x9F1E, "Store result/error code at (nmi_tx_block),0", inline=True)
comment(0x9F20, "&80: completion flag for &0D3A", inline=True)
comment(0x9F22, "Signal TX complete", inline=True)
comment(0x9F25, "Full ADLC reset and return to idle listen", inline=True)

# ============================================================
# Generate disassembly
# ============================================================

import json
import sys

output = go(print_output=False)

_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "nfs-3.40.asm"
output_filepath.write_text(output)
print(f"Wrote {output_filepath}", file=sys.stderr)

structured = get_structured()
json_filepath = _output_dirpath / "nfs-3.40.json"
json_filepath.write_text(json.dumps(structured))
print(f"Wrote {json_filepath}", file=sys.stderr)
