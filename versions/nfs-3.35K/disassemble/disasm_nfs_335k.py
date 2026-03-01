import os
from pathlib import Path

from py8dis.commands import *
import py8dis.acorn as acorn

init(assembler_name="beebasm", lower_case=True)

# ============================================================
# Address map: NFS 3.35D → NFS 3.35K
# ============================================================
# This driver was derived from the NFS 3.35D disassembly driver.
# The two ROMs are 97.8% identical at the opcode level.
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
    str(_version_dirpath / "rom" / "nfs-3.35K.rom"),
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
move(0x0016, 0x9315, 0x61)

# NMI handler / CLI command code (&934D/&944D/&954D → pages &04/&05/&06)
move(0x0400, 0x935A, 0x100)
move(0x0500, 0x945A, 0x100)
move(0x0600, 0x955A, 0x100)

# acorn.bbc() provides: os_text_ptr (&F2), romsel_copy (&F4), osrdsc_ptr (&F6),
# all OS vectors (brkv, wrchv, ..., netv), all OS entry points (osasci, osbyte, ...),
# plus hooks for automatic OSBYTE/OSWORD annotation.
# acorn.is_sideways_rom() provides: rom_header, language_entry, service_entry,
# rom_type, copyright_offset, binary_version, title, language_handler, service_handler.
acorn.bbc()
acorn.is_sideways_rom()

# Split the copyright string classification so the null terminator
# at &8014 becomes a separate item.  This lets error_offsets have its
# own label line rather than being expressed as copyright_string+7.
from py8dis import classification as _cls, disassembly as _disasm
from py8dis.memorymanager import RuntimeAddr as _RuntimeAddr
from py8dis.movemanager import r2b as _r2b
_copyright_bin = _r2b(_RuntimeAddr(0x800D))[0]
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
hook_subroutine(0x85D9, "print_inline", stringhi_hook)

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
label(0x0063, "zp_63")               # Used by NFS

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
label(0x003A, "tube_main_loop")      # Poll R1 (WRCH) and R2 (commands), dispatch via table
label(0x003F, "tube_handle_wrch")    # R1 data ready: read byte, call OSWRITCH (&FFCB)
label(0x0045, "tube_poll_r2")        # Poll R2 status; if ready, read command and dispatch
label(0x0054, "tube_dispatch_cmd")   # JMP (&0500) — dispatch to handler via table
label(0x0057, "tube_transfer_addr")  # 4-byte transfer start address (written by address claim)
entry(0x0016)
entry(0x0032)
entry(0x003A)

# Relocated code — page 4 (Tube address claim, RDCH, data transfer)
# Reference: NFS12 (BEGIN, ADRR, SENDW, TADDR, SETADR)
label(0x0403, "tube_escape_entry")   # JMP to tube_escape_check (&06E2)
label(0x0406, "tube_addr_claim")     # Tube address claim protocol (ADRR in reference)
label(0x0414, "tube_post_init")      # Called after ROM→RAM copy; initial Tube setup
label(0x0425, "return_tube_init")    # Return from tube_post_init path
label(0x046A, "return_tube_xfer")   # Return from tube transfer/setup
label(0x04E0, "tube_setup_transfer")  # Set Y=0, X=&57 (tube_transfer_addr), JMP tube_addr_claim
label(0x04E7, "tube_rdch_handler")   # RDCHV target — send &01 via R2, enter main loop
label(0x04EF, "tube_restore_regs")   # Restore X,Y from &10/&11 (dispatch entry 6)
label(0x04F7, "tube_read_r2")        # Wait for R2 data ready, read byte to A
entry(0x0400)
entry(0x0403)
entry(0x0406)
entry(0x0414)
entry(0x04E0)
entry(0x04E7)
entry(0x04EF)
entry(0x04F7)

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
label(0x051C, "tube_wrch_handler")    # WRCHV target -- write character via Tube
label(0x051F, "tube_send_and_poll")   # Send byte via R2, poll R2/R1 for reply
label(0x0527, "tube_poll_r1_wrch")    # Service R1 WRCH requests while waiting for R2
label(0x0532, "tube_resume_poll")     # JMP back to R2 poll loop after servicing R1
label(0x053D, "tube_release_return")  # Restore X,Y from &10/&11, PLA, RTS
label(0x0543, "tube_osbput")          # OSBPUT: read channel+byte from R2, call &FFD4
label(0x0550, "tube_osbget")          # OSBGET: read channel from R2, call &FFD7
label(0x055B, "tube_osrdch")          # OSRDCH: call &FFC8, send carry+byte reply
label(0x0561, "tube_rdch_reply")      # Send carry in bit 7 + data byte as reply
label(0x0569, "tube_osfind")          # OSFIND open: read arg+filename, call &FFCE
label(0x0580, "tube_osfind_close")    # OSFIND close: read handle, call &FFCE with A=0
label(0x058C, "tube_osargs")          # OSARGS: read handle+4 bytes+reason, call &FFDA
label(0x0590, "tube_read_params")     # Read parameter bytes from R2 into zero page
label(0x05B1, "tube_read_string")     # Read CR-terminated string from R2 into &0700
label(0x05C5, "tube_oscli")           # OSCLI: read command string, call &FFF7
label(0x05CB, "tube_reply_ack")       # Send &7F acknowledge, return to main loop
label(0x05CD, "tube_reply_byte")      # Poll R2, send byte in A, return to main loop
label(0x05D8, "tube_osfile")          # OSFILE: read 16 params+filename+reason, call &FFDD
entry(0x051C)
# Dispatch table entry points
for addr in [0x055B, 0x05C5, 0x0626, 0x063B, 0x065D, 0x06A3,
             0x04EF, 0x053D, 0x058C, 0x0550, 0x0543, 0x0569,
             0x05D8, 0x0602]:
    entry(addr)

# Tube R2 command dispatch table: 14 entries mapping Tube command
# codes 0-13 to handler addresses in pages 4-6.
_tube_r2_entries = [
    (0x0500, "tube_osrdch",        "cmd 0: OSRDCH"),
    (0x0502, "tube_oscli",         "cmd 1: OSCLI"),
    (0x0504, "tube_osbyte_short",  "cmd 2: OSBYTE (2-param)"),
    (0x0506, "tube_osbyte_long",   "cmd 3: OSBYTE (3-param)"),
    (0x0508, "tube_osword",        "cmd 4: OSWORD"),
    (0x050A, "tube_osword_rdln",   "cmd 5: OSWORD 0 (read line)"),
    (0x050C, "tube_restore_regs",  "cmd 6: release/restore regs"),
    (0x050E, "tube_release_return", "cmd 7: restore regs, RTS"),
    (0x0510, "tube_osargs",        "cmd 8: OSARGS"),
    (0x0512, "tube_osbget",        "cmd 9: OSBGET"),
    (0x0514, "tube_osbput",        "cmd 10: OSBPUT"),
    (0x0516, "tube_osfind",        "cmd 11: OSFIND"),
    (0x0518, "tube_osfile",        "cmd 12: OSFILE"),
    (0x051A, "tube_osgbpb",        "cmd 13: OSGBPB"),
]
for addr, target_label, desc in _tube_r2_entries:
    word(addr)
    expr(addr, target_label)
    comment(addr, desc, inline=True)

# Relocated code — page 6 (OSGBPB, OSBYTE, OSWORD, RDLN, event handler)
# Reference: NFS13 (GBPB, SBYTE, BYTE, WORD, RDLN, RDCHA, WRIFOR, ESCAPE, EVENT, ESCA)
label(0x0602, "tube_osgbpb")          # OSGBPB: read 13 params+reason, call &FFD1
# 3.35K fix: after JSR osgbpb, ROR A encodes carry into bit 7
# and sends it via tube_send_r2 BEFORE the 13 parameter bytes.
# In 3.35D, PHA saved A but never sent or popped it — the
# co-processor had no way to determine completion status.
comment(0x0615, """\
3.35K fix: send carry result to co-processor.
3.35D had PHA here (never sent, never popped).""", inline=True)
label(0x0626, "tube_osbyte_short")    # OSBYTE 2-param: read X+A, call &FFF4, return X
label(0x0630, "tube_osbyte_send_x")   # Poll R2, send X result
label(0x063B, "tube_osbyte_long")     # OSBYTE 3-param: read X+Y+A, call &FFF4, return carry+Y+X
label(0x0653, "tube_osbyte_send_y")   # Poll R2, send Y result, then fall through to send X
label(0x065D, "tube_osword")          # OSWORD variable-length: read A+params, call &FFF1
label(0x0661, "tube_osword_read")     # Poll R2 for param block length, read params
label(0x066C, "tube_osword_read_lp")  # Read param block bytes from R2 into &0130
label(0x0692, "tube_osword_write")    # Write param block bytes from &0130 back to R2
label(0x0695, "tube_osword_write_lp") # Poll R2, send param block byte
label(0x06A0, "tube_return_main")     # JMP tube_main_loop
label(0x06A3, "tube_osword_rdln")     # OSWORD 0 (read line): read 5 params, call &FFF1
label(0x06BB, "tube_rdln_send_line")  # Send input line bytes from &0700 back to Tube
label(0x06C2, "tube_rdln_send_loop")  # Load byte from &0700+X
label(0x06C5, "tube_rdln_send_byte")  # Send byte via R2, loop until CR
label(0x06E2, "tube_escape_check")    # Check &FF escape flag, forward to Tube via R1
label(0x06E8, "tube_event_handler")   # EVNTV target: forward event (A,X,Y) to Tube via R1
label(0x06F7, "tube_send_r1")         # Poll R1 status, write A to R1 data (ESCA in reference)
entry(0x0600)
entry(0x0602)
entry(0x0626)
entry(0x063B)
entry(0x065D)
entry(0x06A3)
entry(0x06E2)
entry(0x06E8)
entry(0x06F7)
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
comment(0x800D, """\
The 'ROFF' suffix at &8010 is reused by the *ROFF
command matcher (svc_star_command) — a space-saving
trick that shares ROM bytes between the copyright
string and the star command table.""")

# ROM header: copyright string and error offset table
label(0x800D, "copyright_string")
label(0x8014, "error_offsets")

# Error message offset table (9 entries, indices 0-8).
# The copyright null terminator doubles as entry 0.
# Indexed by TXCB status: AND #7 for codes 0-7, or hardcoded 8.
# Each value is a Y offset into error_msg_table; the code loads
# error_msg_table,Y to copy the selected error string.
comment(0x8014, """\
Error message offset table (9 entries).
Each byte is a Y offset into error_msg_table.
Entry 0 (Y=0, "Line Jammed") doubles as the
copyright string null terminator.
Indexed by TXCB status (AND #7), or hardcoded 8.""")
comment(0x8014, '"Line Jammed"', inline=True)
for addr in range(0x8015, 0x801D):
    byte(addr)
comment(0x8015, '"Net Error"', inline=True)
comment(0x8016, '"Not listening"', inline=True)
comment(0x8017, '"No Clock"', inline=True)
comment(0x8018, '"Escape"', inline=True)
comment(0x8019, '"Escape"', inline=True)
comment(0x801A, '"Escape"', inline=True)
comment(0x801B, '"Bad Option"', inline=True)
comment(0x801C, '"No reply"', inline=True)

# Unreferenced padding between error offsets and dispatch table
comment(0x801D, "Four bytes with unknown purpose.")
for addr in range(0x801D, 0x8021):
    byte(addr)
comment(0x801D, "Purpose unknown", inline=True)
comment(0x801E, "Purpose unknown", inline=True)
comment(0x801F, "Purpose unknown", inline=True)
comment(0x8020, "Purpose unknown", inline=True)

# Dispatch tables: split low/high byte address tables
label(0x8021, "dispatch_0_lo")          # First low byte entry (Svc 0)
label(0x8045, "dispatch_0_hi")          # First high byte entry (Svc 0)
expr_label(0x8020, "dispatch_0_lo-1")   # Code operand expression
expr_label(0x8044, "dispatch_0_hi-1")   # Code operand expression

# Dispatcher and dispatch callers
# Note: &80D4 is already labelled "language_handler" by acorn.is_sideways_rom()

# Filing system OSWORD dispatch (&8EB8-&8E3E)
label(0x8E9F, "fs_osword_tbl_lo")      # Low bytes of FS OSWORD handler table
label(0x8EA4, "fs_osword_tbl_hi")      # High bytes of FS OSWORD handler table

# FS OSWORD handler routines
# osword_0f_handler label created by subroutine() call below.
label(0x8EE7, "read_args_size")        # READRB: get args buffer size from RX block offset &7F
# osword_10_handler label created by subroutine() call below.

# Econet TX/RX handler and OSWORD dispatch
label(0x8FDB, "store_16bit_at_y")     # Store 16-bit value at (nfs_workspace)+Y
# osword_dispatch label created by subroutine() call below.
label(0x908D, "osword_trampoline")     # PHA/PHA/RTS trampoline
label(0x9098, "osword_tbl_lo")         # Dispatch table low bytes
label(0x90A1, "osword_tbl_hi")         # Dispatch table high bytes
# net_write_char label created by subroutine() call below.

# Remote operation function handlers (dispatched via osword_tbl)
# (net_write_char subroutine defined above)
label(0x912A, "return_match_osbyte") # Return from match_osbyte_code
label(0x8469, "return_remote_cmd")   # Return from remote command data handler
label(0x8470, "rchex")                # Clear JSR protection after remote command exec

# Control block setup
label(0x9175, "ctrl_block_setup_clv") # CLV entry: same setup but clears V flag

# Remote printer and display handlers (fn 1/2/3/5)

# Network transmit

# JSR buffer protection
label(0x92E4, "clear_jsr_protection") # CLRJSR: reset JSR buffer protection bits (4 refs)

# Palette/VDU state save
label(0x92FC, "read_vdu_osbyte_x0")  # Read next VDU OSBYTE with X=0 parameter
label(0x92FE, "read_vdu_osbyte")     # Read next OSBYTE from table, store result in workspace

# ADLC initialisation and state management

# Tube co-processor I/O subroutines (in relocated page 6)
# Reference: RDCHA (R2 write), WRIFOR (R4 write), ESCA (R1 write)
label(0x06D0, "tube_send_r2")       # Poll R2 status, write A to R2 data (RDCHA in reference)
label(0x06D9, "tube_send_r4")       # Poll R4 status, write A to R4 data (WRIFOR in reference)

# ============================================================
# Service call handler labels (&8000-&8500)
# ============================================================
# Service call numbers and their dispatch table indices:
#   svc 0  → index 1  → return_2 (no-op)
#   svc 1  → index 2  → svc_1_abs_workspace (&82A2)
#   svc 2  → index 3  → svc_2_private_workspace (&82AB)
#   svc 3  → index 4  → svc_3_autoboot (&8203)
#   svc 4  → index 5  → svc_4_star_command (&8179)
#   svc 5  → index 6  → svc_5_unknown_irq (&966C) → JMP c9b52
#   svc 6  → index 7  → return_2 (BRK — no action)
#   svc 7  → index 8  → dispatch_net_cmd (&8069) (unrecognised OSBYTE)
#   svc 8  → index 9  → svc_8_osword (&8E76) (unrecognised OSWORD)
#   svc 9  → index 10 → svc_9_help (&81ED)
#   svc 10 → index 11 → return_2 (no action)
#   svc 11 → index 12 → svc_11_nmi_claim (&9669) → JMP restore_econet_state
#   svc 12 → index 13 → svc_12_nmi_release (&9666) → JMP save_econet_state
#
# Special service handling (outside dispatch table):
#   svc &12 (18) with Y=5 → select_nfs (&81B5)
#   svc &FE → Tube init (explode character definitions)
#   svc &FF → init_vectors_and_copy (&8103)

label(0x80E9, "return_1")
label(0x816C, "return_2")
label(0x82A8, "return_3")
label(0x854C, "return_4")
label(0x8D52, "return_5")
label(0x8E55, "return_6")
label(0x8EB7, "return_7")
label(0x9064, "return_8")
label(0x8CE0, "return_9")

# --- Service call handlers ---

label(0x8179, "svc_4_star_command")     # Svc 4 dispatch entry (mid-routine in svc_star_command)

# --- Trampoline JMPs near ADLC init (&9660-&966C) ---
label(0x9660, "trampoline_tx_setup")    # JMP c9be4 (TX control block setup)
label(0x9663, "trampoline_adlc_init")   # JMP adlc_init (&966F)
label(0x9666, "svc_12_nmi_release")        # Svc 12: JMP save_econet_state (&96CF)
label(0x9669, "svc_11_nmi_claim")          # Svc 11: JMP restore_econet_state (&96B4)
label(0x966C, "svc_5_unknown_irq")        # Svc 5: JMP c9b52 (unknown interrupt handler)
entry(0x9660)
entry(0x9663)

# --- Init and vector setup ---
label(0x8280, "fs_vector_addrs")        # FS vector dispatch and handler addresses (34 bytes)

# --- FSCV handler and dispatch ---
# FSCV (&80C7) dispatches via secondary indices 19-26:
#   FSCV 0 (*OPT)               → index 19 → fscv_0_opt (&89CA)
#   FSCV 1 (EOF)                → index 20 → fscv_1_eof (&884C)
#   FSCV 2 (*/ run)             → index 21 → fscv_2_star_run (&8DBF)
#   FSCV 3 (unrecognised *)     → index 22 → fscv_3_star_cmd (match known FS commands)
#   FSCV 4 (*RUN)               → index 23 → fscv_2_star_run (&8DBF)
#   FSCV 5 (*CAT)               → index 24 → fscv_5_cat (&8C02)
#   FSCV 6 (shut down)          → index 25 → fscv_6_shutdown (&8337)
#   FSCV 7 (read handles/info)  → index 26 → fscv_7_read_handles (&864C)
#
# Extended dispatch table entries (indices 27-36):
# These appear to be used by FS reply processing and *NET sub-commands.
#   index 27 → fsreply_0_print_dir (&8D57)        (print directory path)
#   index 28 → fsreply_1_copy_handles_boot (&8E20) (copy handles + run boot command)
#   index 29 → fsreply_2_copy_handles (&8E21)          (copy handles only)
#   index 30 → fsreply_3_set_csd (&8E1A)        (update CSD handle)
#   index 31 → fsreply_4_notify_exec (&8DC5)       (send FS notify, execute response)
#   index 32 → fsreply_5_set_lib (&8E15)        (update library handle)
#
# *NET sub-commands (base Y=&20, indices 33-36):
#   *NET1 → index 33 → net_1_read_handle (&8E3B)
#   *NET2 → index 34 → net_2_read_handle_entry (&8E56)
#   *NET3 → index 35 → net_3_close_handle (&8E66)
#   *NET4 → index 36 → net_4_resume_remote (&8180)
# --- Filing system vector entry points ---
# Extended vector table entries set up at init (&831F):
#   FILEV → &86DE    ARGSV → &8907    BGETV → &852E
#   BPUTV → &83DC    GBPBV → &8A0E    FINDV → &896F
#   FSCV  → &80C7
# Labels and entry points for FSCV, FILEV, ARGSV, FINDV, GBPBV
# are created by subroutine() calls below in the comment sections.
label(0x852E, "bgetv_handler")          # BGETV entry: SEC then JSR handle_bput_bget
label(0x83DC, "bputv_handler")          # BPUTV entry: CLC then fall into handle_bput_bget
entry(0x852E)
entry(0x83DC)
entry(0x86B0)                            # Param block copy, falls through to parse_filename_gs
entry(0x86DE)                            # Actual FILEV entry point (ROM pointer table target)

# --- Helper routines in header/init section ---
label(0x81DD, "cmd_name_matched")       # MATCH2: full name matched, check terminator byte
label(0x81E4, "skip_cmd_spaces")         # SKPSP: skip spaces in command text; Z=1 if CR follows
label(0x831F, "store_rom_ptr_pair")     # Write 2-byte address + ROM bank to ROM pointer table

# --- TX control block and FS command setup ---
label(0x838B, "init_tx_ctrl_data")      # Init TX control block for data port (&90)
label(0x834A, "init_tx_ctrl_port")      # Init TX control block with port in A (2 JSR refs)
label(0x837A, "prepare_cmd_with_flag")  # Prepare FS command with '*' flag and carry set
label(0x8380, "prepare_cmd_clv")        # Prepare FS command with V cleared
# prepare_fs_cmd and build_send_fs_cmd labels created by subroutine() calls below.
label(0x838B, "prepare_fs_cmd_v")       # Prepare FS command, V flag preserved
label(0x83BA, "send_fs_reply_cmd")      # Send FS command with reply processing

# --- Byte I/O and escape ---
# handle_bput_bget label created by subroutine() call below.
label(0x8407, "store_retry_count")      # RAND1: store retry count to &0FDD, initiate TX
label(0x8461, "update_sequence_return") # RAND3: update sequence numbers and pull A/Y/X/return
label(0x84CF, "set_listen_offset")      # NLISN2: use reply code as table offset for listen
label(0x84EB, "send_to_fs_star")        # Send '*' command to fileserver
label(0x8513, "fs_wait_cleanup")        # WAITEX: tidy stack, restore rx_status_flags

# --- Pointer arithmetic helpers ---
label(0x87DD, "add_5_to_y")             # INY * 5; RTS
label(0x87DE, "add_4_to_y")             # INY * 4; RTS
label(0x87F0, "sub_4_from_y")           # DEY * 4; RTS
label(0x87F1, "sub_3_from_y")           # DEY * 3; RTS

# --- Error messages and data tables ---
label(0x8196, "clear_osbyte_ce_cf")     # Reset OSBYTE &CE/&CF intercept masks to &7F (restore MOS vectors)

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
label(0x85CE, "access_bit_table")       # Lookup table for attribute bit mapping (11 bytes)

# --- Decimal number parser (&85F3-&861B) ---
# parse_decimal label created by subroutine() call below.

# --- File handle ↔ bitmask conversion ---
# handle_to_mask_a, handle_to_mask_clc, handle_to_mask and mask_to_handle
# labels created by subroutine() calls below.

# --- Number and hex printing ---
label(0x8D9D, "print_hex")              # Print A as two hex digits
label(0x8DA8, "print_hex_nibble")       # Print low nibble of A as hex digit

# --- Address comparison ---
# compare_addresses label created by subroutine() call below.
label(0x864B, "return_compare")          # Return from compare_addresses (not equal)

# --- FSCV 7: read FS handles ---
label(0x864C, "fscv_7_read_handles")      # Return X=&20 (base handle), Y=&27 (top handle)
label(0x8650, "return_fscv_handles")    # Return from fscv_7_read_handles

# --- FS flags manipulation ---
label(0x865C, "store_fs_flag")           # Shared STA fs_eof_flags / RTS for set/clear_fs_flag

# --- File info display (hex print helpers moved to &8Dxx) ---
label(0x8D13, "pad_filename_spaces")    # Pad filename display to 12 chars with spaces
label(0x8D26, "print_exec_and_len")     # Print exec address (4 bytes) and file length (3 bytes)
label(0x8D31, "print_hex_bytes")        # Print X bytes from (fs_options)+Y as hex (high->low)
label(0x8D3C, "print_space")            # Print a space character via OSASCI

# --- TX control and transmission ---
label(0x866A, "tx_poll_timeout")        # Transmit with Y=&60 (specified timeout)
# tx_poll_core label created by subroutine() call below.


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
label(0x889A, "get_file_protection")  # CHA1: decode attribute byte for protection status
label(0x88AF, "copy_filename_to_cmd") # CHASK2: copy filename string into FS command buffer
label(0x88EC, "copy_fs_reply_to_cb")  # COPYFS: copy FS reply buffer data to control block

# --- Common return point (&8952) ---
label(0x8938, "save_args_handle")      # SETARG: save handle for OSARGS operation

# --- FSCV 0: *OPT handler (&89CA) ---
label(0x89B8, "close_single_handle")   # CLOSE1: send close command for specific handle to FS

# --- Address adjustment helpers (&89EE-&8A0E) ---
label(0x89EE, "adjust_addrs_9")        # Adjust 4-byte addresses at param block offset 9
label(0x89F3, "adjust_addrs_1")        # Adjust 4-byte addresses at param block offset 1
label(0x89F5, "adjust_addrs_clc")      # CLC entry: clear carry before address adjustment
label(0x8B1F, "copy_reply_to_caller") # Copy FS reply data to caller buffer (direct or via Tube)
label(0x8BAE, "tube_claim_loop")      # TCLAIM: claim Tube with &C3, retry until acquired

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
label(0x8DB4, "print_reply_counted")   # STRIN1: sub-entry of print_reply_bytes with caller-supplied Y count
label(0x8D47, "copy_string_from_offset") # COPLP1: sub-entry of copy_string_to_cmd with caller-supplied Y offset

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
label(0x972D, "scout_reject")          # Reject: wrong network (RX_DISCONTINUE)
label(0x974E, "scout_discard")         # Clean discard via &9A56
label(0x9756, "scout_loop_rda")        # Scout data loop: check RDA
label(0x9766, "scout_loop_second")     # Scout data loop: read second byte of pair
label(0x97A1, "scout_no_match")        # Scout port/station mismatch (3 refs)
label(0x97A4, "scout_match_port")      # Port non-zero: look for matching RX block

# --- Data frame RX (inbound four-way handshake) ---
label(0x9837, "data_rx_setup")         # Switch to RX mode, install data RX handler
label(0x9859, "nmi_data_rx_net")       # Data frame: validate dest_net = 0
label(0x986F, "nmi_data_rx_skip")      # Data frame: skip ctrl/port (already from scout)
label(0x989E, "rx_error")              # RX error dispatcher (13 refs -- most referenced!)
label(0x989E, "rx_error_reset")        # Full reset and discard
label(0x9901, "nmi_data_rx_tube")      # Data frame: Tube co-processor variant

# --- Data frame completion and FV validation ---
label(0x993D, "data_rx_tube_complete") # Tube data frame completion
label(0x993A, "data_rx_tube_error")    # Tube data frame error (3 refs)

# --- ACK transmission ---
label(0x9970, "ack_tx_configure")      # Configure CR1/CR2 for TX
label(0x997E, "ack_tx_write_dest")     # Write dest addr to TX FIFO

# --- Discard and idle ---

# --- TX path ---
label(0x9C93, "tx_active_start")       # Begin TX (CR1=&44)
label(0x9D81, "tx_error")              # TX error path

# --- RX reply scout (outbound handshake) ---
label(0x9DED, "reply_error")           # Reply error: store &41 (8 refs)

# --- TX scout ACK + data phase ---
label(0x9E4A, "data_tx_begin")         # Begin data frame TX
label(0x9E8C, "data_tx_last")          # TX_LAST_DATA for data frame (5 refs)
label(0x9E9D, "data_tx_error")         # Data TX error (5 refs)
label(0x9EAA, "install_saved_handler") # Install handler from &0D4B/&0D4C
label(0x9EB3, "nmi_data_tx_tube")      # NMI: send data from Tube

# --- Four-way handshake: RX final ACK ---
label(0x9F0E, "nmi_final_ack_net")     # Read dest_net, validate

# --- Completion and error ---

# --- NMI shim at end of ROM ---
label(0x9FD9, "nmi_shim_rom_src")      # Source for 32-byte copy to &0D00
# label(0x9FFA, "rom_nmi_tail") — removed: truncated code at ROM end

# ============================================================
# Labels from DNFS 3.60 source correspondence
# ============================================================
# These labels were identified by opcode fingerprint matching between
# the NFS 3.34 ROM and the original Acorn DNFS 3.60 source code
# (NFS00-NFS13). Each replaces a py8dis auto-generated label with
# the name used in the Acorn reference source.

# --- Relocated Tube code (pages 4-6) ---
label(0x04AE, "begink")               # NFS12: Tube begin
label(0x04BA, "beginr")               # NFS12: Tube begin return
label(0x05B5, "strnh")                # NFS13: string handling
label(0x05D5, "mj")                   # NFS13: conditional jump
label(0x05DA, "argsw")                # NFS13: OSARGS workspace
label(0x0638, "bytex")                # NFS13: byte transfer

# --- Service call init (&80xx) ---
label(0x8120, "cloop")                # NFS01: copy loop (page copy)
label(0x81C0, "initl")                # NFS01: init loop
label(0x81E3, "skpspi")               # NFS01: skip SPI

# --- FS command dispatch (&82xx-&83xx) ---
label(0x824C, "dofsl1")               # NFS03: do FS loop 1
label(0x8339, "fsdiel")               # NFS01: FS die loop
label(0x8359, "fstxl1")               # NFS03: FS TX loop 1
label(0x8369, "fstxl2")               # NFS03: FS TX loop 2
label(0x83C4, "dofsl7")               # NFS03: do FS loop 7
label(0x83D0, "return_dofsl7")        # NFS03: return from FS loop 7
label(0x83D1, "dofsl5")               # NFS03: do FS loop 5
label(0x8419, "error1")               # NFS03: error handler 1

# --- Net list / pointer arithmetic (&84xx-&85xx) ---
label(0x84CB, "nlistn")               # NFS03: net list entry
label(0x84CD, "nlisne")               # NFS03: net list next entry
label(0x8500, "incpx")                # NFS04: increment pointer X
label(0x8625, "y2fsl5")               # NFS04: Y-to-FS loop 5
label(0x862B, "y2fsl2")               # NFS04: Y-to-FS loop 2
label(0x863A, "fs2al1")               # NFS04: FS-to-A loop 1

# --- Number formatting and file info (&86xx) ---
label(0x8D33, "num01")                # NFS07: number print entry
label(0x8686, "poll_txcb_status")      # Poll TXCB for TX completion
label(0x86B2, "file1")                # NFS05: FILEV entry 1
label(0x86C4, "quote1")               # NFS05: filename quote loop
label(0x86EF, "loadop")               # NFS05: load operation
label(0x870C, "lodfil")               # NFS05: load file

# --- FILEV, load/save size (&87xx) ---
label(0x872F, "floop")                # NFS01: FS loop
label(0x8759, "lodchk")               # NFS05: load check
label(0x8764, "return_lodchk")        # NFS05: return from load check
label(0x8765, "saveop")               # NFS05: save operation
label(0x876E, "savsiz")               # NFS05: save size handling
label(0x87D3, "lodrl1")               # NFS05: load reply loop 1
label(0x87E6, "lodrl2")               # NFS05: load reply loop 2
label(0x8818, "savchk")               # NFS05: save check

# --- Channel/attribute handling (&88xx-&89xx) ---
label(0x888D, "chalp1")               # NFS05: channel loop 1
label(0x88A4, "chalp2")               # NFS05: channel loop 2
label(0x88B6, "cha6")                  # NFS05: channel handler 6
label(0x88C5, "cha4")                  # NFS05: channel handler 4
label(0x88CF, "cha5")                  # NFS05: channel handler 5
label(0x88F9, "cha5lp")               # NFS05: channel 5 loop
label(0x8963, "osarg1")               # NFS05: OSARGS handler 1
label(0x89DA, "opter1")               # NFS05: *OPT error 1
label(0x89DF, "optl1")                # NFS05: *OPT loop 1

# --- GBPB handler (&89xx-&8Axx) ---
label(0x8A07, "gbpbx")                # NFS05: GBPB dispatch
label(0x8A3E, "gbpbx0")               # NFS05: GBPB dispatch 0
label(0x8A1C, "gbpbx1")               # NFS05: GBPB dispatch 1
label(0x8A27, "gbpbe1")               # NFS05: GBPB EOF 1
label(0x8A33, "gbpbf1")               # NFS05: GBPB forward 1
label(0x8A3E, "gbpbf2")               # NFS05: GBPB forward 2
label(0x8A47, "gbpbl1")               # NFS05: GBPB loop 1
label(0x8A69, "gbpbl3")               # NFS05: GBPB loop 3
label(0x8A80, "gbpbf3")               # NFS05: GBPB forward 3

# --- *INFO and decimal print (&8Axx-&8Bxx) ---
label(0x8AE1, "info2")                # NFS06: *INFO loop 2
label(0x8B46, "tbcop1")               # NFS06: Tube copy loop 1
label(0x8BBF, "decfir")               # NFS07: decimal first digit
label(0x8BC1, "decmor")               # NFS07: decimal more digits
label(0x8BCD, "decmin")               # NFS07: decimal minimum

# --- Logon and *NET (&8Dxx) ---
label(0x8E25, "logon2")               # NFS07: logon handler 2
label(0x8EB7, "logon3")               # NFS07: logon handler 3
label(0x8D59, "print_dir_from_offset") # INFOLP: sub-entry of fsreply_0_print_dir with caller-supplied X offset
label(0x8D75, "infol2")               # NFS07: info loop 2

# --- File I/O: save, read, open (&8Dxx-&8Fxx) ---
label(0x8E61, "rxpol2")               # NFS08: RX poll loop 2
label(0x8E91, "save1")                # NFS08: save handler 1
label(0x8EB3, "copyl3")               # NFS08: copy loop 3
label(0x8EF2, "readry")               # NFS08: read ready
label(0x8F15, "rssl1")                # NFS08: read size/status loop 1
label(0x8F20, "rssl2")                # NFS08: read size/status loop 2
label(0x8F30, "rsl1")                 # NFS08: read status loop 1
label(0x8F5A, "readc1")               # NFS08: read char 1
label(0x8F77, "scan0")                # NFS08: scan entry 0
label(0x8F8B, "scan1")                # NFS08: scan entry 1
label(0x8FA7, "openl6")               # NFS08: open loop 6
label(0x8FB4, "openl7")               # NFS08: open loop 7
label(0x8FB9, "openl4")               # NFS08: open loop 4
label(0x8FC1, "rest1")                # NFS08: restore 1
label(0x8FEB, "dofs01")               # NFS08: do FS 01
label(0x9065, "dofs2")                # NFS08: do FS 2

# --- OSWORD and remote ops (&90xx-&91xx) ---
label(0x9086, "entry1")               # NFS09: OSWORD entry 1
label(0x90F2, "nbyte6")               # NFS09: net byte handler 6
label(0x90F4, "nbyte1")               # NFS09: net byte handler 1
label(0x9116, "nbyte4")               # NFS09: net byte handler 4
label(0x911A, "nbyte5")               # NFS09: net byte handler 5
label(0x9121, "return_nbyte")         # NFS09: return from net byte handler
label(0x8473, "remot1")               # NFS03: remote handler 1
label(0x9176, "cbset2")               # NFS09: control block set 2
label(0x918D, "cbset3")               # NFS09: control block set 3
label(0x9193, "cbset4")               # NFS09: control block set 4
label(0x91D0, "setup1")               # NFS09: setup 1
label(0x91D3, "return_printer_select") # NFS09: return from printer_select_handler
label(0x91E3, "prlp1")                # NFS09: printer loop 1

# --- Broadcast/station search (&92xx) ---
label(0x9262, "bsxl1")                # NFS09: broadcast search loop 1
label(0x927F, "bspsx")                # NFS09: broadcast search parse exit
label(0x9287, "bsxl0")                # NFS09: broadcast search loop 0
label(0x929E, "return_bspsx")         # NFS09: return from broadcast search area

# ============================================================
# File header / overview comment (placed at &8000, first in code)
# ============================================================
comment(0x8000, """\
NFS ROM 3.35K disassembly (Acorn Econet filing system)
=====================================================""")

# ============================================================
# Dispatch table at &8020 (low bytes) / &8044 (high bytes)
# ============================================================
# Used via the PHA/PHA/RTS dispatch trick at &80DA-&80E9.
#
# This is a standard 6502 computed-jump technique. The table stores
# handler addresses minus 1, split into separate low-byte and high-byte
# arrays. The dispatcher at &80DA pushes the high byte then the low
# byte onto the stack. When RTS executes, it pops the address and adds
# 1, jumping to the handler.
#
# Multiple callers share this single table using different base offsets
# in Y. The dispatcher loop at &80DA adds Y to X (the command index),
# so each caller maps its index into a different region of the table:
#
#   Caller              Y (base)  X (index)         Table indices
#   ─────────────────   ────────  ────────────────  ─────────────
#   Service calls        &00      svc_num            1-13
#   Language entry       &0D      reason             14-18
#   FSCV                 &12      fscv_code          19-26
#   FS reply             &16      reply_code         27-32
#   *NET1-4 commands     &20      char-'1'           33-36
#
# Index 0 and unused indices point to an RTS (null handler), so
# unrecognised service calls or out-of-range values fall through
# harmlessly.
#
# rts_code_ptr(lo_addr, hi_addr) decodes the address and adds entry().

# Service call handlers (indices 1-13)
for i in range(1, 14):
    rts_code_ptr(0x8020 + i, 0x8044 + i)

# Language entry handlers (indices 14-18)
for i in range(14, 19):
    rts_code_ptr(0x8020 + i, 0x8044 + i)

# FSCV handlers (indices 19-26, codes 0-7, base Y=&12)
for i in range(19, 27):
    rts_code_ptr(0x8020 + i, 0x8044 + i)

# FS reply handlers (indices 27-32)
# Dispatched by forward_star_cmd with base Y=&16 using the
# fileserver's reply code as the index.
for i in range(27, 33):
    rts_code_ptr(0x8020 + i, 0x8044 + i)

# *NET command handlers (indices 33-36)
# Index 36 overlaps: low byte at &8044 (= high table[0])
for i in range(33, 37):
    rts_code_ptr(0x8020 + i, 0x8044 + i)

# ============================================================
# Filing system OSWORD dispatch table at &8E9F/&8EA4
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &8E80 (entered from svc_8_osword).
# svc_8_osword subtracts &0F from the command code in &EF, giving a
# 0-4 index for OSWORD calls &0F-&13 (15-19).
#
# Index  OSWORD  Target   Purpose
# ─────  ──────  ───────  ────────────────────────────
#   0      &0F   &8EB8    Protection/status control
#   1      &10   &8F66    RX block read/setup
#   2      &11   &8ED2    Data block copy
#   3      &12   &908F    FS server station lookup
#   4      &13   &0490    Econet TX/RX handler (page 4)
for i in range(5):
    rts_code_ptr(0x8E9F + i, 0x8EA4 + i)

# ============================================================
# NMI handler chain entry points
# ============================================================
# These are installed via self-modifying JMP at &0D0C/&0D0D,
# so py8dis cannot trace them automatically.

# --- ADLC init and idle listen ---
entry(0x96FA)   # ADLC init / reset entry
entry(0x9700)   # RX scout (idle listen) - default NMI handler

# --- TX path: polling, data, completion ---
entry(0x9C57)   # INACTIVE polling loop (pre-TX)
entry(0x9D5B)   # NMI TX data handler (2 bytes per NMI)
entry(0x9D81)   # TX error path
entry(0x9D97)   # TX_LAST_DATA and frame completion
entry(0x9DA3)   # TX completion: switch to RX mode

# --- RX reply handlers ---
entry(0x9DC1)   # RX reply scout handler
entry(0x9DD7)   # RX reply continuation handler
entry(0x9DF2)   # RX reply next handler

# --- Four-way handshake (outbound data phase) ---
entry(0x9EEC)   # Four-way handshake: switch to RX for final ACK
entry(0x9EF8)   # Four-way handshake: RX final ACK (check AP, dest_stn)
entry(0x9F0E)   # Four-way handshake: RX final ACK continuation (dest_net=0)

# --- Completion / error ---
entry(0x9F48)   # Completion handler (store result=0 to tx_block)
entry(0x9F4E)   # Error handler (store error code to tx_block)
entry(0x9F24)   # Four-way handshake: validate final ACK src addr

# --- Discovered via JMP &0D0E scan (NMI handler installations) ---
entry(0x971F)   # RX scout second byte handler (dest network)
entry(0x9751)   # Scout data reading loop (reads body in pairs)
entry(0x9843)   # Data frame RX handler (four-way handshake)
entry(0x9859)   # Data frame: validate source network = 0
entry(0x986F)   # Data frame: skip ctrl/port bytes
entry(0x98A4)   # Data frame: bulk data read loop
entry(0x9901)   # Data frame: Tube co-processor RX handler
entry(0x999C)   # ACK TX continuation (write src addr, TX_LAST_DATA)

# --- NMI shim at end of ROM (&9FD9-&9FFF) ---
# Bootstrap NMI handler and ROM copies of workspace routines.
# &9FD9 is the source for the 32-byte copy to &0D00 by install_nmi_shim.
entry(0x9FDA)   # Bootstrap NMI entry (hardcoded JMP nmi_rx_scout, no self-mod)
entry(0x9FE8)   # ROM copy of set_nmi_vector + nmi_rti
# entry(0x9FFA) — removed: code at $9FFA runs off ROM end ($9FFF STA truncated)

# --- Data RX NMI handlers (four-way handshake data phase) ---
entry(0x9E3A)   # Data phase RX first byte
entry(0x9E5F)   # Data phase RX continuation
entry(0x9EB3)   # Data phase RX bulk transfer

# ============================================================
# Additional known entry points
# ============================================================
entry(0x8212)
entry(0x8231)
entry(0x8233)

# ============================================================
# Code regions identified by manual inspection of equb data
# ============================================================
# These are preceded by RTS and start with valid opcodes, but
# are not reachable via JSR/JMP from already-traced code (their
# callers are themselves in equb regions -- cascading resolution).

entry(0x87DD)   # INY*5; RTS (pointer arithmetic helper)
entry(0x87F0)   # DEY*4; RTS (pointer arithmetic helper)
entry(0x87F5)   # PHA; JSR ... (called from &878A and &8A6C)
entry(0x8870)   # STA abs; CMP#; ... (called from &8744)
entry(0x8959)   # TAY; BNE; ... (preceded by RTS, standalone entry)
entry(0x8A0E)   # JSR &85A6; ... (preceded by RTS, standalone entry)
# entry(0x8E34) created by subroutine() call below
entry(0x90D0)   # LDY zp; CMP#; ... (preceded by RTS, standalone entry)
entry(0x99C5)   # Post-ACK: process received scout (check port, match RX block)

# --- Econet TX/RX handler and OSWORD dispatch (&8FE5-&90B8) ---
# &8FE5: Main transmit/receive handler entry (A=0: set up and send, A>=1: handle result)
# &9074: OSWORD-style dispatch handler (function codes 0-8, PHA/PHA/RTS)
entry(0x8FE5)   # Econet TX/RX handler (CMP #1; BCS)
# entry(0x9008) and entry(0x903E) created by subroutine() calls below
entry(0x908D)   # Dispatch trampoline (PHA/PHA/RTS into table at &9098/&90A1)

# Dispatch table at &9098 (low bytes) / &90A1 (high bytes)
# 9 entries for function codes 0-8, used via PHA/PHA/RTS at &908D.
for i in range(9):
    rts_code_ptr(0x9098 + i, 0x90A1 + i)

# ============================================================
# Immediate operation dispatch table at &9A24/&9A2C
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9A96 (immediate_op handler).
# Y = rx_ctrl (&81-&88), so table entries are at base+&81..base+&88.
# The control byte determines the remote operation type:
#
# Y   Operation   Target
# ──   ─────────   ──────
# &81  PEEK        &9AF1
# &82  POKE        &9AD3
# &83  JSR         &9AB5
# &84  UserProc    &9AB5
# &85  OSProc      &9AB5
# &86  HALT        &9B17
# &87  CONTINUE    &9B17
# &88  (machine type query)  &9ADE
for y in range(0x81, 0x89):
    rts_code_ptr(0x9A24 + y, 0x9A2C + y)

# ============================================================
# TX completion dispatch table at &9B1D/&9B22
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9B97.
# Y = tx_work_57 (the Econet operation type being sent).
# The dispatch is reached both by Y >= &86 (via BCS at &9B8A)
# and by Y < &86 (falls through from &9B94 after saving
# prot_status). Table entries for Y=&81/&82 overlap with the
# PHA/RTS code itself and are not valid — those operation types
# (PEEK/POKE) are response-only and never initiated via TX.
#
# Y   Operation   Target
# ──   ─────────   ──────
# &83  JSR         &9BAA  (remote JSR initiation)
# &84  UserProc    &9BB3  (user procedure initiation)
# &85  OSProc      &9BC1  (OS procedure initiation)
# &86  HALT        &9BCD  (HALT completion)
# &87  CONTINUE    &9BE4  (CONTINUE completion)
for y in range(0x83, 0x88):
    rts_code_ptr(0x9B1D + y, 0x9B22 + y)

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
    rts_code_ptr(0x9C62 + y, 0x9C6A + y)

# ============================================================
# Immediate operation RX handler labels (&9AB5-&9AF1)
# ============================================================
# Targets of dispatch table 1 at &9A24/&9A2C.
# These handle incoming immediate operations (PEEK, POKE, JSR,
# UserProc, OSProc, machine type query) received from the network.

label(0x9AB5, "rx_imm_exec")
subroutine(0x9AB5, hook=None,
    title="RX immediate: JSR/UserProc/OSProc setup",
    description="""\
Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace at &0D58, then jumps to
the common receive path at c9826. Used for operation types
&83 (JSR), &84 (UserProc), and &85 (OSProc).""")

label(0x9AD3, "rx_imm_poke")
subroutine(0x9AD3, hook=None,
    title="RX immediate: POKE setup",
    description="""\
Sets up workspace offsets for receiving POKE data.
port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
the common data-receive path at c9805.""")

label(0x9ADE, "rx_imm_machine_type")
subroutine(0x9ADE, hook=None,
    title="RX immediate: machine type query",
    description="""\
Sets up a buffer at &7F21 (length #&01FC) for the machine
type query response, then jumps to the query handler at
c9b0f. Returns system identification data to the remote
station.""")

label(0x9AF1, "rx_imm_peek")
subroutine(0x9AF1, hook=None,
    title="RX immediate: PEEK setup",
    description="""\
Saves the current TX block pointer, replaces it with a
pointer to &0D3D, and prepares to send the PEEK response
data back to the requesting station.""")

# ============================================================
# TX completion handler labels (&9BAA-&9BEC)
# ============================================================
# Targets of dispatch table 2 at &9B1D/&9B22.
# Called when an outbound immediate operation TX completes.

label(0x9BAA, "tx_done_jsr")
subroutine(0x9BAA, hook=None,
    title="TX done: remote JSR execution",
    description="""\
Pushes address &9BEB on the stack (so RTS returns to
tx_done_exit), then does JMP (l0d58) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")

label(0x9BB3, "tx_done_user_proc")
subroutine(0x9BB3, hook=None,
    title="TX done: UserProc event",
    description="""\
Generates a network event (event 8) via OSEVEN with
X=l0d58, A=l0d59 (the remote address). This notifies
the user program that a UserProc operation has completed.""")

label(0x9BC1, "tx_done_os_proc")
subroutine(0x9BC1, hook=None,
    title="TX done: OSProc call",
    description="""\
Calls the ROM entry point at &8000 (rom_header) with
X=l0d58, Y=l0d59. This invokes an OS-level procedure
on behalf of the remote station.""")

label(0x9BCD, "tx_done_halt")
subroutine(0x9BCD, hook=None,
    title="TX done: HALT",
    description="""\
Sets bit 2 of rx_flags (&0D64), enables interrupts, and
spin-waits until bit 2 is cleared (by a CONTINUE from the
remote station). If bit 2 is already set, skips to exit.""")

label(0x9BE4, "tx_done_continue")
subroutine(0x9BE4, hook=None,
    title="TX done: CONTINUE",
    description="""\
Clears bit 2 of rx_flags (&0D64), releasing any station
that is halted and spinning in tx_done_halt.""")

label(0x9BEC, "tx_done_exit")

# ============================================================
# TX ctrl byte handler labels (&9CF7-&9D54)
# ============================================================
# Targets of dispatch table 3 at &9C62/&9C6A.
# Called to set up the scout control byte and transfer
# parameters for outbound immediate operations.

label(0x9CF7, "tx_ctrl_peek")
subroutine(0x9CF7, hook=None,
    title="TX ctrl: PEEK transfer setup",
    description="""\
Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace at &0D1E-&0D21 (with carry propagation).
Calls tx_calc_transfer to finalise, then exits via
tx_ctrl_exit.""")

label(0x9CFB, "tx_ctrl_poke")
subroutine(0x9CFB, hook=None,
    title="TX ctrl: POKE transfer setup",
    description="""\
Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")

label(0x9D1A, "tx_ctrl_proc")
subroutine(0x9D1A, hook=None,
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="""\
Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

label(0x9D54, "tx_ctrl_exit")

# Alternate entry into ctrl_block_setup (&9171)
entry(0x9168)   # ADLC setup: LDX #&0D; LDY #&7C; BIT &833B; BVS c9167

# Dispatch targets found in equb data regions
# These are the bodies of the econet function dispatch handlers.
# Functions 1-3 share a handler (&91D4) — possibly different
# sub-operations that share setup logic. Function 5 (&91C4) and
# function 8 (&9142) are distinct. The exact purpose of each
# function code hasn't been fully determined yet.
entry(0x91D4)   # Function 1/2/3 handler (shared)
entry(0x9142)   # Function 8 handler (remote_cmd_data)

# --- Code found in third-pass remaining equb regions ---
entry(0x8765)   # BEQ +3; JMP &8870 (called from &8744 region)
entry(0x8FCA)   # LDY #&28; ... (preceded by RTS, standalone entry)
entry(0x9837)   # LDA #&82; STA &FEA0; installs NMI handler &9843

# ============================================================
# Inline comments for key instructions
# ============================================================
# Note: acorn.bbc()'s hooks auto-annotate OSBYTE/OSWORD calls, so
# we only add comments where the auto-annotations don't reach.

# ============================================================
# Save FSCV arguments (&859C)
# ============================================================
entry(0x859C)
subroutine(0x859C, "save_fscv_args_with_ptrs", hook=None,
    title="Save FSCV arguments with text pointers",
    description="""\
Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
falls through to save_fscv_args to store A/X/Y in the FS
workspace.""")

subroutine(0x85A6, "save_fscv_args", hook=None,
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
subroutine(0x85B1, "decode_attribs_6bit", hook=None,
    title="Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)",
    description="""\
Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&85CE. The two formats use different bit layouts for file
protection attributes.""")

subroutine(0x85BB, "decode_attribs_5bit", hook=None,
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
subroutine(0x85F3, "parse_decimal",
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
             "x": "initial A value (saved by TAX)",
             "y": "offset past last digit parsed"})
comment(0x85F3, "Save A in X for caller", inline=True)
comment(0x85F4, "Zero accumulator", inline=True)
comment(0x85F8, "Load next char from buffer", inline=True)
comment(0x85FA, "Letter or above?", inline=True)
comment(0x85FC, "Yes: not a digit, done", inline=True)
comment(0x85FE, "Dot separator?", inline=True)
comment(0x8600, "Yes: exit with C=1 (dot found)", inline=True)
comment(0x8602, "Control char or space: done", inline=True)
comment(0x8604, "Mask ASCII digit to 0-9", inline=True)
comment(0x8606, "Save new digit", inline=True)
comment(0x8608, "Running total * 2", inline=True)
comment(0x860A, "A = running total * 2", inline=True)
comment(0x860C, "A = running total * 4", inline=True)
comment(0x860D, "A = running total * 8", inline=True)
comment(0x860E, "+ total*2 = total * 10", inline=True)
comment(0x8610, "+ digit = total*10 + digit", inline=True)
comment(0x8612, "Store new running total", inline=True)
comment(0x8614, "Advance to next char", inline=True)
comment(0x8615, "Loop (always: Y won't wrap to 0)", inline=True)
comment(0x8617, "No dot found: C=0", inline=True)
comment(0x8618, "Return result in A", inline=True)

# ============================================================
# File handle conversion (&861B-&861D)
# ============================================================
subroutine(0x861B, "handle_to_mask_a", hook=None,
    title="Convert handle in A to bitmask",
    description="""\
Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""")

subroutine(0x861C, "handle_to_mask_clc", hook=None,
    title="Convert handle to bitmask (carry cleared)",
    description="""\
Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""")

subroutine(0x861D, "handle_to_mask",
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
Callers needing to move the handle from A use handle_to_mask_a;
callers needing carry cleared use handle_to_mask_clc.""",
    on_entry={"y": "handle number",
              "c": "0: convert, 1 with Y=0: skip, 1 with Y!=0: convert"},
    on_exit={"a": "preserved",
             "x": "preserved",
             "y": "bitmask (single bit set) or &FF if handle invalid"})
comment(0x861D, "Save A (will be restored on exit)", inline=True)
comment(0x861E, "Save X (will be restored on exit)", inline=True)
comment(0x861F, "  (second half of X save)", inline=True)
comment(0x8620, "A = handle from Y", inline=True)
comment(0x8621, "C=0: always convert", inline=True)
comment(0x8623, "C=1 and Y=0: skip (handle 0 = none)", inline=True)
comment(0x8625, "C=1 and Y!=0: convert", inline=True)
comment(0x8626, "A = handle - &1F (1-based bit position)", inline=True)
comment(0x8628, "X = shift count", inline=True)
comment(0x8629, "Start with bit 0 set", inline=True)
comment(0x862B, "Shift bit left", inline=True)
comment(0x862C, "Count down", inline=True)
comment(0x862D, "Loop until correct position", inline=True)
comment(0x862F, "Undo final extra shift", inline=True)
comment(0x8630, "Y = resulting bitmask", inline=True)
comment(0x8631, "Non-zero: valid mask, skip to exit", inline=True)
comment(0x8633, "Zero: invalid handle, set Y=&FF", inline=True)
comment(0x8634, "Restore X", inline=True)
comment(0x8636, "Restore A", inline=True)

# ============================================================
# Mask to handle (&8638)
# ============================================================
subroutine(0x8638, "mask_to_handle",
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
comment(0x8638, "X = &1F (handle base - 1)", inline=True)
comment(0x863A, "Count this bit position", inline=True)
comment(0x863B, "Shift mask right; C=0 when done", inline=True)
comment(0x863C, "Loop until all bits shifted out", inline=True)
comment(0x863E, "A = X = &1F + bit position = handle", inline=True)

# ============================================================
# Print decimal number (&8D7E)
# ============================================================
subroutine(0x8D7E, "print_decimal", hook=None,
    title="Print byte as 3-digit decimal number",
    description="""\
Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""",
    on_entry={"a": "byte value to print"},
    on_exit={"a": "last digit character",
             "x": "corrupted",
             "y": "0 (remainder after last division)"})

subroutine(0x8D8B, "print_decimal_digit", hook=None,
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
subroutine(0x8640, "compare_addresses",
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
subroutine(0x8651, "clear_fs_flag", hook=None,
    title="Clear bit(s) in FS flags (&0E07)",
    description="""\
Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
the specified bits. JMPs to the shared STA at &865C, skipping
the ORA in set_fs_flag.""")

entry(0x8659)
subroutine(0x8659, "set_fs_flag", hook=None,
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
subroutine(0x8CFC, "print_file_info", hook=None,
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
# Hex printing (&8D9D / &8DA8)
# ============================================================
subroutine(0x8D9D, hook=None,
    title="Print byte as two hex digits",
    description="""\
Prints the high nibble first (via 4× LSR), then the low
nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
and output via OSASCI.""")

# ============================================================
# TX control (&8660-&866C)
# ============================================================
subroutine(0x8660, "setup_tx_ptr_c0", hook=None,
    title="Set up TX pointer to control block at &00C0",
    description="""\
Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""")

subroutine(0x8668, "tx_poll_ff", hook=None,
    title="Transmit and poll for result (full retry)",
    description="""\
Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""")

subroutine(0x866C, "tx_poll_core",
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
Two entry points: setup_tx_ptr_c0 (&8660) always uses the
standard TXCB; tx_poll_core (&866C) is general-purpose.""",
    on_entry={"a": "retry count (&FF = full retry)",
              "y": "timeout parameter (&60 = standard)"},
    on_exit={"a": "entry A (retry count, restored from stack)",
             "x": "0",
             "y": "0"})

# ============================================================
# print_inline subroutine (&85D9)
# ============================================================
# Label and code-tracing hook created by hook_subroutine() above.
subroutine(0x85D9, hook=None,
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

comment(0x85D9, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x85DC, "Pop return address (high)", inline=True)
comment(0x85E1, "Advance pointer past return address / to next char", inline=True)
comment(0x85E7, "Load next byte from inline string", inline=True)
comment(0x85E9, "Bit 7 set? Done — this byte is the next opcode", inline=True)
comment(0x85F0, "Jump to address of high-bit byte (resumes code after string)", inline=True)

# ============================================================
# Dispatch table comments (&8021-&8068)
# ============================================================
comment(0x8021, """\
Dispatch table: low bytes of (handler_address - 1)
Each entry stores the low byte of a handler address minus 1,
for use with the PHA/PHA/RTS dispatch trick at &80DA.
See dispatch_0_hi (&8045) for the corresponding high bytes.

Five callers share this table via different Y base offsets:
  Y=&00  Service calls 0-12       (indices 1-13)
  Y=&0D  Language entry reasons    (indices 14-18)
  Y=&12  FSCV codes 0-7           (indices 19-26)
  Y=&16  FS reply handlers        (indices 27-32)
  Y=&20  *NET1-4 sub-commands     (indices 33-36)""")

comment(0x8045, """\
Dispatch table: high bytes of (handler_address - 1)
Paired with dispatch_0_lo (&8021). Together they form a table
of 37 handler addresses, used via the PHA/PHA/RTS trick at
&80DA.""")

# Dispatch table inline comments (lo and hi bytes).
# The comment bodies are defined once and emitted for both halves so
# they stay in sync.
dispatch_comments = [
    # Service call handlers (Y=&00, indices 1-13)
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
    # Language entry handlers (Y=&0D, indices 14-18)
    "Lang 0: no language / Tube",
    "Lang 1: normal startup",
    "Lang 2: softkey byte (Electron)",
    "Lang 3: softkey length (Electron)",
    "Lang 4: remote validated",
    # FSCV handlers (Y=&12, indices 19-26)
    "FSCV 0: *OPT",
    "FSCV 1: EOF check",
    "FSCV 2: */ (run)",
    "FSCV 3: unrecognised star command",
    "FSCV 4: *RUN",
    "FSCV 5: *CAT",
    "FSCV 6: shutdown",
    "FSCV 7: read handle range",
    # FS reply handlers (Y=&16, indices 27-32)
    "FS reply: print directory name",
    "FS reply: copy handles + boot",
    "FS reply: copy handles",
    "FS reply: set CSD handle",
    "FS reply: notify + execute",
    "FS reply: set library handle",
    # *NET sub-command handlers (Y=&20, indices 33-36)
    "*NET1: read handle from packet",
    "*NET2: read handle from workspace",
    "*NET3: close handle",
    "*NET4: resume remote",
]
for i, body in enumerate(dispatch_comments):
    comment(0x8021 + i, f"lo - {body}", inline=True)
    comment(0x8045 + i, f"hi - {body}", inline=True)

# ============================================================
# *NET command dispatch (&8069)
# ============================================================
subroutine(0x8069, "dispatch_net_cmd", hook=None,
    title="*NET command dispatcher",
    description="""\
Parses the character after *NET as '1'-'4', maps to table
indices 33-36 via base offset Y=&20, and dispatches via &80DA.
Characters outside '1'-'4' fall through to return_1 (RTS).

These are internal sub-commands used only by the ROM itself,
not user-accessible star commands. The MOS command parser
requires a space or terminator after 'NET', so *NET1 typed
at the command line does not match; these are reached only
via OSCLI calls within the ROM.

*NET1 (&8E3B): read file handle from received
packet (net_1_read_handle)

*NET2 (&8E56): read handle entry from workspace
(net_2_read_handle_entry)

*NET3 (&8E66): close handle / mark as unused
(net_3_close_handle)

*NET4 (&8180): resume after remote operation
(net_4_resume_remote)""")

comment(0x8069, "Read command character following *NET", inline=True)
comment(0x806B, "Subtract ASCII '1' to get 0-based command index", inline=True)
comment(0x8079, "Y=&20: base offset for *NET commands (index 33+)", inline=True)

# ============================================================
# PHA/PHA/RTS dispatcher (&80DA)
# ============================================================
subroutine(0x80DA, "dispatch", hook=None,
    title="PHA/PHA/RTS computed dispatch",
    description="""\
X = command index within caller's group (e.g. service number)
Y = base offset into dispatch table (0, &0D, &20, etc.)
The loop adds Y+1 to X, so final X = command index + base + 1.
Then high and low bytes of (handler-1) are pushed onto the stack,
and RTS pops them and jumps to handler_address.

This is a standard 6502 trick: RTS increments the popped address
by 1 before jumping, so the table stores (address - 1) to
compensate. Multiple callers share one table via different Y
base offsets.""")

comment(0x80DA, "Add base offset Y to index X (loop: X += Y+1)", inline=True)
comment(0x80DF, "Load high byte of (handler - 1) from table", inline=True)
comment(0x80E2, "Push high byte onto stack", inline=True)
comment(0x80E3, "Load low byte of (handler - 1) from table", inline=True)
comment(0x80E6, "Push low byte onto stack", inline=True)
comment(0x80E7, "Restore X (fileserver options) for use by handler", inline=True)
comment(0x80E9, "RTS pops address, adds 1, jumps to handler", inline=True)

# ============================================================
# Language entry dispatch (&80D4)
# ============================================================
subroutine(0x80D4, hook=None,
    title="Language entry dispatcher",
    description="""\
Called when the NFS ROM is entered as a language. Although rom_type
(&82) does not set the language bit, the MOS enters this point
after NFS claims service &FE (Tube post-init). X = reason code
(0-4). Dispatches via table indices 14-18 (base offset Y=&0D).""")

comment(0x80D8, "Y=&0D: base offset for language handlers (index 14+)", inline=True)

# ============================================================
# Service handler entry (&80EA)
# ============================================================
subroutine(0x80EA, hook=None,
    title="Service handler entry",
    description="""\
Intercepts three service calls before normal dispatch:
  &FE: Tube init -- explode character definitions
  &FF: Full init -- vector setup, copy code to RAM, select NFS
  &12 (Y=5): Select NFS as active filing system
All other service calls < &0D dispatch via c8146.
3.35K removes the per-ROM disable flag check that 3.35D has.""")

# ============================================================
# Init: set up vectors and copy code (&8103)
# ============================================================
subroutine(0x8103, "init_vectors_and_copy", hook=None,
    title="NFS initialisation (service &FF: full reset)",
    description="""\
New in 3.35D: table-driven vector initialisation replaces
the hardcoded LDA/STA pairs of 3.34B. Reads 4 triplets from
the data table at &816D (low byte, high byte, vector offset)
and stores each 16-bit value at &0200+offset:
  EVNTV (&0220) = &06E8   BRKV  (&0202) = &0016
  RDCHV (&0210) = &04E7   WRCHV (&020E) = &051C
Then writes &8E to Tube control register (&FEE0) and copies
3 pages of Tube host code from ROM (&935A/&945A/&955A)
to RAM (&0400/&0500/&0600), calls tube_post_init (&0414),
and copies 97 bytes of workspace init from ROM (&9315) to
&0016-&0076.""")

# ============================================================
# Select NFS as active filing system (&81B5)
# ============================================================
subroutine(0x81B5, "select_nfs", hook=None,
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
# Check boot key (&820E)
# ============================================================
subroutine(0x820E, "check_boot_key", hook=None,
    title="Check boot key",
    description="""\
Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")

# ============================================================
# Print station identification (&8218)
# ============================================================
subroutine(0x8218, "print_station_info", hook=None,
    title="Print station identification",
    description="""\
Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")

# ============================================================
# Initialise filing system vectors (&824A)
# ============================================================
subroutine(0x824A, "init_fs_vectors", hook=None,
    title="Initialise filing system vectors",
    description="""\
Copies 14 bytes from fs_vector_addrs (&8280) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")

comment(0x824A, "Copy 14 bytes: FS vector addresses → FILEV-FSCV", inline=True)

# ============================================================
# FS vector dispatch and handler addresses (&8280)
# ============================================================
subroutine(0x8280, "fs_vector_addrs", hook=None,
    title="FS vector dispatch and handler addresses (34 bytes)",
    description="""\
Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by init_fs_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the ROM pointer table.

Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (store_rom_ptr_pair writes the current ROM
bank number without reading). The last entry (FSCV) has no
padding byte.""")

# Part 1: extended vector dispatch addresses (7 x 2 bytes)
byte(0x8280, 1)
comment(0x8280, "FILEV dispatch lo", inline=True)
byte(0x8281, 1)
comment(0x8281, "FILEV dispatch hi", inline=True)
byte(0x8282, 1)
comment(0x8282, "ARGSV dispatch lo", inline=True)
byte(0x8283, 1)
comment(0x8283, "ARGSV dispatch hi", inline=True)
byte(0x8284, 1)
comment(0x8284, "BGETV dispatch lo", inline=True)
byte(0x8285, 1)
comment(0x8285, "BGETV dispatch hi", inline=True)
byte(0x8286, 1)
comment(0x8286, "BPUTV dispatch lo", inline=True)
byte(0x8287, 1)
comment(0x8287, "BPUTV dispatch hi", inline=True)
byte(0x8288, 1)
comment(0x8288, "GBPBV dispatch lo", inline=True)
byte(0x8289, 1)
comment(0x8289, "GBPBV dispatch hi", inline=True)
byte(0x828A, 1)
comment(0x828A, "FINDV dispatch lo", inline=True)
byte(0x828B, 1)
comment(0x828B, "FINDV dispatch hi", inline=True)
byte(0x828C, 1)
comment(0x828C, "FSCV dispatch lo", inline=True)
byte(0x828D, 1)
comment(0x828D, "FSCV dispatch hi", inline=True)

# Part 2: handler address entries (7 x {lo, hi, pad})
byte(0x828E, 1)
comment(0x828E, "FILEV handler lo (&86DE)", inline=True)
byte(0x828F, 1)
comment(0x828F, "FILEV handler hi", inline=True)
byte(0x8290, 1)
comment(0x8290, "(ROM bank — not read)", inline=True)
byte(0x8291, 1)
comment(0x8291, "ARGSV handler lo (&8907)", inline=True)
byte(0x8292, 1)
comment(0x8292, "ARGSV handler hi", inline=True)
byte(0x8293, 1)
comment(0x8293, "(ROM bank — not read)", inline=True)
byte(0x8294, 1)
comment(0x8294, "BGETV handler lo (&852E)", inline=True)
byte(0x8295, 1)
comment(0x8295, "BGETV handler hi", inline=True)
byte(0x8296, 1)
comment(0x8296, "(ROM bank — not read)", inline=True)
byte(0x8297, 1)
comment(0x8297, "BPUTV handler lo (&83DC)", inline=True)
byte(0x8298, 1)
comment(0x8298, "BPUTV handler hi", inline=True)
byte(0x8299, 1)
comment(0x8299, "(ROM bank — not read)", inline=True)
byte(0x829A, 1)
comment(0x829A, "GBPBV handler lo (&8A0E)", inline=True)
byte(0x829B, 1)
comment(0x829B, "GBPBV handler hi", inline=True)
byte(0x829C, 1)
comment(0x829C, "(ROM bank — not read)", inline=True)
byte(0x829D, 1)
comment(0x829D, "FINDV handler lo (&896F)", inline=True)
byte(0x829E, 1)
comment(0x829E, "FINDV handler hi", inline=True)
byte(0x829F, 1)
comment(0x829F, "(ROM bank — not read)", inline=True)
byte(0x82A0, 1)
comment(0x82A0, "FSCV handler lo (&80C7)", inline=True)
byte(0x82A1, 1)
comment(0x82A1, "FSCV handler hi", inline=True)

# ============================================================
# Service 1: claim absolute workspace (&82A2)
# ============================================================
subroutine(0x82A2, "svc_1_abs_workspace", hook=None,
    title="Service 1: claim absolute workspace",
    description="""\
Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""")

# ============================================================
# Service 2: claim private workspace (&82AB)
# ============================================================
subroutine(0x82AB, "svc_2_private_workspace", hook=None,
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

comment(0x82C2, "OSBYTE &FD: read type of last reset", inline=True)
comment(0x82C8, "Soft break (X=0): skip FS init", inline=True)
comment(0x82CE, "Station &FE = no server selected", inline=True)
comment(0x82FC, "Read station ID (also INTOFF)", inline=True)
comment(0x8303, "Initialise ADLC hardware", inline=True)

# ============================================================
# Service 3: auto-boot (&8203)
# ============================================================
subroutine(0x8203, "svc_3_autoboot", hook=None,
    title="Service 3: auto-boot",
    description="""\
Notifies current FS of shutdown via FSCV A=6. Scans keyboard
(OSBYTE &7A): if no key is pressed, auto-boot proceeds directly
via print_station_info. If a key is pressed, falls through to
check_boot_key: the 'N' key (matrix address &55) proceeds with
auto-boot, any other key causes the auto-boot to be declined.""")

# ============================================================
# Service 4: unrecognised * command (&8168)
# ============================================================
subroutine(0x8168, "svc_star_command", hook=None,
    title="Service 4: unrecognised * command",
    description="""\
Matches the command text against ROM string table entries.
Both entries reuse bytes from the ROM header to save space:

  X=8: matches "ROFF" at &8010 — the suffix of the
       copyright string "(C)ROFF" → *ROFF (Remote Off,
       end remote session) — jumps to net_4_resume_remote

  X=1: matches "NET" at &8009 — the ROM title string
       → *NET (select NFS) — falls through to select_nfs

If neither matches, returns with the service call
unclaimed.""")

# ============================================================
# Service 9: *HELP (&81ED)
# ============================================================
subroutine(0x81ED, "svc_9_help", hook=None,
    title="Service 9: *HELP",
    description="""\
Prints the ROM identification string using print_inline.""")

# ============================================================
# Match ROM string (&81CC)
# ============================================================
subroutine(0x81CC, "match_rom_string", hook=None,
    title="Match command text against ROM string table",
    description="""\
Compares characters from (os_text_ptr)+Y against bytes starting
at binary_version+X (&8008+X). Input is uppercased via AND &DF.
Returns with Z=1 if the ROM string's NUL terminator was reached
(match), or Z=0 if a mismatch was found. On match, Y points
past the matched text; on return, skips trailing spaces.""")
comment(0x81CC, "Y = saved text pointer offset", inline=True)
comment(0x81CE, "Load next input character", inline=True)
comment(0x81D0, "Force uppercase (clear bit 5)", inline=True)
comment(0x81D2, "Input char is NUL/space: check ROM byte", inline=True)
comment(0x81D4, "Compare with ROM string byte", inline=True)
comment(0x81D7, "Mismatch: check if ROM string ended", inline=True)
comment(0x81D9, "Advance input pointer", inline=True)
comment(0x81DA, "Advance ROM string pointer", inline=True)
comment(0x81DB, "Continue matching (always taken)", inline=True)
comment(0x81DD, "Load ROM string byte at match point", inline=True)
comment(0x81E0, "Zero = end of ROM string = full match", inline=True)
comment(0x81E2, "Non-zero = partial/no match; Z=0", inline=True)
comment(0x81E3, "Skip this space", inline=True)
comment(0x81E4, "Load next input character", inline=True)
comment(0x81E6, "Is it a space?", inline=True)
comment(0x81E8, "Yes: keep skipping", inline=True)
comment(0x81EA, "XOR with CR: Z=1 if end of line", inline=True)

# ============================================================
# Call FSCV shutdown (&81FE)
# ============================================================
subroutine(0x81FE, "call_fscv_shutdown", hook=None,
    title="Notify filing system of shutdown",
    description="""\
Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")

# ============================================================
# Issue service: vectors claimed (&8261)
# ============================================================
subroutine(0x8261, "issue_vectors_claimed", hook=None,
    title="Issue 'vectors claimed' service and optionally auto-boot",
    description="""\
Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If nfs_temp is zero (auto-boot not inhibited),
sets up the command string "I .BOOT" at &8246 and jumps to
the FSCV 3 unrecognised-command handler (which matches against
the command table at &8BE4). The "I." prefix triggers the
catch-all entry which forwards the command to the fileserver.
Falls through to run_fscv_cmd.""")

# ============================================================
# Run FSCV command from ROM (&8273)
# ============================================================
subroutine(0x8273, "run_fscv_cmd", hook=None,
    title="Run FSCV command from ROM",
    description="""\
Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
to execute the command string at (X, Y). X is pre-loaded by the
caller with the low byte of the string address. Also used as a
data base address by store_rom_ptr_pair for Y-indexed access to
the handler address table.""")

# ============================================================
# Auto-boot command string (&8278)
# ============================================================
string(0x8278, 8)
comment(0x8278, """\
Synthetic auto-boot command string. "I " does not match any
entry in NFS's local command table — "I." requires a dot, and
"I AM" requires 'A' after the space — so fscv_3_star_cmd
forwards the entire string to the fileserver, which executes
the .BOOT file.""")

# ============================================================
# Set up ROM pointer table and NETV (&830B)
# ============================================================
subroutine(0x830B, "setup_rom_ptrs_netv", hook=None,
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
subroutine(0x8337, "fscv_6_shutdown", hook=None,
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
subroutine(0x8356, "init_tx_ctrl_block", hook=None,
    title="Initialise TX control block at &00C0 from template",
    description="""\
Copies 12 bytes from tx_ctrl_template (&836E) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""")

subroutine(0x836E, "tx_ctrl_template", hook=None,
    title="TX control block template (TXTAB, 12 bytes)",
    description="""\
12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")
byte(0x836E, 1)
comment(0x836E, "Control flag", inline=True)
byte(0x836F, 1)
comment(0x836F, "Port (FS command = &99)", inline=True)
byte(0x8370, 1)
comment(0x8370, "Station (filled at runtime)", inline=True)
byte(0x8371, 1)
comment(0x8371, "Network (filled at runtime)", inline=True)
byte(0x8372, 1)
comment(0x8372, "Buffer start low", inline=True)
byte(0x8373, 1)
comment(0x8373, "Buffer start high (page &0F)", inline=True)
byte(0x8374, 1)
comment(0x8374, "Buffer start pad (4-byte Econet addr)", inline=True)
byte(0x8375, 1)
comment(0x8375, "Buffer start pad", inline=True)
byte(0x8376, 1)
comment(0x8376, "Buffer end low", inline=True)
byte(0x8377, 1)
comment(0x8377, "Buffer end high (page &0F)", inline=True)
byte(0x8378, 1)
comment(0x8378, "Buffer end pad", inline=True)
byte(0x8379, 1)
comment(0x8379, "Buffer end pad", inline=True)

subroutine(0x837A, "prepare_cmd_with_flag", hook=None,
    title="Prepare FS command with carry set",
    description="""\
Alternate entry to prepare_fs_cmd that pushes A, loads &2A
into fs_error_ptr, and enters with carry set (SEC). The carry
flag is later tested by build_send_fs_cmd to select the
byte-stream (BSXMIT) transmission path.""")

# ============================================================
# Prepare FS command (&838A)
# ============================================================
subroutine(0x838A, "prepare_fs_cmd",
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
subroutine(0x83A4, "build_send_fs_cmd",
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
subroutine(0x8443, "store_fs_error", hook=None,
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
subroutine(0x83DD, "handle_bput_bget",
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
subroutine(0x84ED, "send_to_fs", hook=None,
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
subroutine(0x851D, "check_escape", hook=None,
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

# 3.35K: Y register initialised before STA (net_tx_ptr),Y
comment(0x8526, """\
3.35K fix: initialise Y=0 before the indexed store.
In 3.35D, Y could hold any value here after the
OSBYTE escape acknowledge call.""")

# 3.35K: BGETV EOF hint logic corrected
comment(0x853A, """\
3.35K fix: EOF hint clear/set are now mutually
exclusive. In 3.35D, both clear_fs_flag and
set_fs_flag were called when N=0, with the clear
immediately undone by the set — making the EOF
hint always set regardless of file position.""")

# ============================================================
# Error message table (&854D)
# ============================================================
# N.B. This is data, not code — we use label() not subroutine()
# to avoid entry() tracing from &854D, where the &A0 error code
# byte would be misinterpreted as LDY #imm.
label(0x854D, "error_msg_table")
comment(0x854D, """\
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
addr = 0x854D
for _ in range(7):
    byte(addr, 1)           # error number byte
    addr = stringz(addr + 1)  # NUL-terminated message string

# ============================================================
# Resume after remote operation (&8180)
# ============================================================
subroutine(0x8180, "net_4_resume_remote", hook=None,
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
subroutine(0x80C7, "fscv_handler",
    title="FSCV dispatch entry",
    description="""\
Entered via the extended vector table when the MOS calls FSCV.
Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
and dispatches codes 0-7 via the shared dispatch table at &8020
with base offset Y=&12 (table indices 19-26).
Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.""",
    on_entry={"a": "function code (0-7)",
              "x": "depends on function",
              "y": "depends on function"},
    on_exit={"a": "depends on handler (preserved if A >= 8)",
             "x": "depends on handler (preserved if A >= 8)",
             "y": "depends on handler (preserved if A >= 8)"})

comment(0x80C7, "Store A/X/Y in FS workspace", inline=True)
comment(0x80CC, "Function code >= 8? Return (unsupported)", inline=True)
comment(0x80D0, "Y=&12: base offset for FSCV dispatch (indices 19+)", inline=True)

# ============================================================
# GSINIT/GSREAD filename parser (&86BA)
# ============================================================
subroutine(0x86BA, "parse_filename_gs", hook=None,
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
subroutine(0x86DE, "filev_handler",
    title="FILEV handler (OSFILE entry point)",
    description="""\
Calls save_fscv_args (&85A6) to preserve A/X/Y, then JSR &86B0
to copy the 2-byte filename pointer from the parameter block to
os_text_ptr and fall through to parse_filename_gs (&86BA) which
parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &86F4)
  A=&00: save file (filev_save at &876A)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &8870)
  Other: restore_args_return (unsupported, no-op)""",
    on_entry={"a": "function code (&FF=load, &00=save, &01-&06=attrs)",
              "x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "restored",
             "x": "restored",
             "y": "restored"})

subroutine(0x86F4, "send_fs_examine", hook=None,
    title="Send FS examine command",
    description="""\
Sends FS command &03 (FCEXAM: examine file) to the fileserver.
Sets &0F02=&03 and error pointer to '*'. Called for OSFILE &FF
(load file) with the filename already in the command buffer.
The FS reply contains load/exec addresses and file length which
are used to set up the data transfer. The header URD field
is repurposed to carry the Econet data port number (PLDATA=&92)
for the subsequent block data transfer.""")

subroutine(0x873A, "send_data_blocks", hook=None,
    title="Send file data in multi-block chunks",
    description="""\
Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")

subroutine(0x876A, "filev_save", hook=None,
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

subroutine(0x87D1, "copy_load_addr_from_params", hook=None,
    title="Copy load address from parameter block",
    description="""\
Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""")

subroutine(0x87E3, "copy_reply_to_params", hook=None,
    title="Copy FS reply data to parameter block",
    description="""\
Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""")

subroutine(0x87F5, "transfer_file_blocks", hook=None,
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

subroutine(0x884C, "fscv_1_eof", hook=None,
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

subroutine(0x8870, "filev_attrib_dispatch", hook=None,
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

subroutine(0x8952, "restore_args_return", hook=None,
    title="Restore arguments and return",
    description="""\
Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""")

subroutine(0x89CA, "fscv_0_opt", hook=None,
    title="FSCV 0: *OPT handler (OPTION)",
    description="""\
Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""")

subroutine(0x89F6, "adjust_addrs", hook=None,
    title="Bidirectional 4-byte address adjustment",
    description="""\
Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""")
comment(0x89F6, "X=&FC: index into &0E06 area (wraps to 0)", inline=True)
comment(0x89F8, "Load byte from param block", inline=True)
comment(0x89FA, "Test sign of adjustment direction", inline=True)
comment(0x89FC, "Negative: subtract instead", inline=True)
comment(0x89FE, "Add adjustment value", inline=True)
comment(0x8A01, "Skip to store result", inline=True)
comment(0x8A04, "Subtract adjustment value", inline=True)
comment(0x8A07, "Store adjusted byte back", inline=True)
comment(0x8A09, "Next param block byte", inline=True)
comment(0x8A0A, "Next adjustment byte (X wraps &FC->&00)", inline=True)
comment(0x8A0B, "Loop 4 times (X=&FC,&FD,&FE,&FF,done)", inline=True)

# ============================================================
# ARGSV handler (&8907)
# ============================================================
subroutine(0x8907, "argsv_handler",
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
subroutine(0x896F, "findv_handler",
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
comment(0x89A1, """\
3.35K fix: OR handle bit into fs_sequence_nos
(&0E08). Without this, a newly opened file could
inherit a stale sequence number from a previous
file using the same handle, causing byte-stream
protocol errors.""")

# ============================================================
# CLOSE handler (&89AE)
# ============================================================
subroutine(0x89AE, "close_handle", hook=None,
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
subroutine(0x8A0E, "gbpbv_handler",
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
subroutine(0x8AD1, "osgbpb_info", hook=None,
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
subroutine(0x80B4, "forward_star_cmd", hook=None,
    title="Forward unrecognised * command to fileserver (COMERR)",
    description="""\
Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
prepares an FS command with function code 0, and sends it to the
fileserver to request decoding. The server returns a command code
indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
5=load-as-command). This mechanism allows the fileserver to extend
the client's command set without ROM updates. Called from the "I."
and catch-all entries in the command match table at &8BE4, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")

# ============================================================
# *BYE handler (&8383)
# ============================================================
subroutine(0x8383, "bye_handler", hook=None,
    title="*BYE handler (logoff)",
    description="""\
Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8BE4 for "BYE".""")

# ============================================================
# FSCV unrecognised * handler (&8BB6)
# ============================================================
subroutine(0x8BB6, "fscv_3_star_cmd", hook=None,
    title="FSCV 2/3/4: unrecognised * command handler (DECODE)",
    description="""\
CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8BE4 using case-insensitive comparison with abbreviation
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

subroutine(0x8BE4, "fs_cmd_match_table", hook=None,
    title="FS command match table (COMTAB)",
    description="""\
Format: command letters (bit 7 clear), then dispatch address
as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
adds 1 to the stored (address-1). Matching is case-insensitive
(AND &DF) and supports '.' abbreviation (standard Acorn pattern).

Entries:
  "I."     → &80B4 (forward_star_cmd) — placed first as a fudge
             to catch *I. abbreviation before matching *I AM
  "I AM"   → &807E (i_am_handler: parse station.net, logon)
  "EX"     → &8BFA (ex_handler: extended catalogue)
  "BYE"\\r  → &8383 (bye_handler: logoff)
  <catch-all> → &80B4 (forward anything else to FS)""")

# ============================================================
# *EX and *CAT handlers (&8BFA / &8C02)
# ============================================================
subroutine(0x8BFA, "ex_handler", hook=None,
    title="*EX handler (extended catalogue)",
    description="""\
Sets &B7=&01 and &B5=&03, then branches into fscv_5_cat at
&8C0A, bypassing fscv_5_cat's default column setup. &B7=1
gives one entry per line with full details (vs &B7=3 for *CAT
which gives multiple files per line).""")

subroutine(0x8C02, "fscv_5_cat", hook=None,
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
subroutine(0x8CE7, "boot_cmd_strings", hook=None,
    title="Boot command strings for auto-boot",
    description="""\
The four boot options use OSCLI strings at offsets within page &8C:
  Option 0 (Off):  offset &F3 → &8CF3 = bare CR (empty command)
  Option 1 (Load): offset &E4 → &8CE4 = "L.!BOOT" (dual-purpose:
      the bytes &4C='L', &2E='.', &21='!' at &8CE4 are followed
      by "BOOT" at &8CE7, forming the OSCLI string "L.!BOOT")
  Option 2 (Run):  offset &E6 → &8CE6 = "!BOOT" (bare filename = *RUN)
  Option 3 (Exec): offset &EC → &8CEC = "E.!BOOT"

This is a classic BBC ROM space optimisation: the string data
overlaps with other byte sequences to save space.""")

# ============================================================
# Boot option table and "I AM" handler (&8CF4-&8E20)
# ============================================================
subroutine(0x8CF4, "boot_option_offsets", hook=None,
    title="Boot option → OSCLI string offset table",
    description="""\
Four bytes indexed by the boot option value (0-3). Each byte
is the low byte of a pointer into page &8C, where the OSCLI
command string for that boot option lives. See boot_cmd_strings.
Referenced by fsreply_1_copy_handles_boot via LDX boot_option_offsets,Y.""")
byte(0x8CF4, 1)
comment(0x8CF4, "Opt 0 (Off): bare CR", inline=True)
byte(0x8CF5, 1)
comment(0x8CF5, "Opt 1 (Load): L.!BOOT", inline=True)
byte(0x8CF6, 1)
comment(0x8CF6, "Opt 2 (Run): !BOOT", inline=True)
byte(0x8CF7, 1)
comment(0x8CF7, "Opt 3 (Exec): E.!BOOT", inline=True)
string(0x8CF8, 4)
comment(0x8CE0, """\
Option name encoding: in 3.35, the boot option names ("Off",
"Load", "Run", "Exec") are scattered through the code rather
than stored as a contiguous table. They are addressed via
base+offset from return_9 (&8CE0), whose first four bytes
(starting with the RTS opcode &60) double as the offset table:
  &60→&8D40 "Off", &73→&8D53 "Load",
  &9B→&8D7B "Run", &18→&8CF8 "Exec"
Each string is terminated by the next instruction's opcode
having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).""")

subroutine(0x807E, "i_am_handler", hook=None,
    title="\"I AM\" command handler",
    description="""\
Dispatched from the command match table when the user types
"*I AM <station>" or "*I AM <network>.<station>". Also used as
the station number parser for "*NET <network>.<station>".
Skips leading spaces, then calls parse_decimal twice if a dot
separator is present. The first number becomes the network
(&0E01, via TAX pass-through in parse_decimal) and the second
becomes the station (&0E00). With a single number, it is stored
as the station and the network defaults to 0 (local). If a colon
follows, reads interactive input via OSRDCH and appends it to
the command buffer. Finally jumps to forward_star_cmd.""")

# ============================================================
# Handle workspace management (&8E15-&8E1A)
# ============================================================
subroutine(0x8E15, "fsreply_5_set_lib", hook=None,
    title="Set library handle",
    description="""\
Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to JMP restore_args_return if Y is non-zero.""")

subroutine(0x8E1A, "fsreply_3_set_csd", hook=None,
    title="Set CSD handle",
    description="""\
Stores Y into &0E03 (current selected directory handle).
Falls through to JMP restore_args_return.""")

# ============================================================
# Copy handles and boot (&8E20 / &8E21)
# ============================================================
subroutine(0x8E20, "fsreply_1_copy_handles_boot", hook=None,
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

subroutine(0x8E21, "fsreply_2_copy_handles", hook=None,
    title="Copy FS reply handles to workspace (no boot)",
    description="""\
CLC entry (SDISC): copies handles only, then jumps to c8cff.
Called when the FS reply contains updated handle values
but no boot action is needed.""")

# ============================================================
# Filename copy helpers (&8D43-&8D51)
# ============================================================
subroutine(0x8D43, "copy_filename", hook=None,
    title="Copy filename to FS command buffer",
    description="""\
Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""")

subroutine(0x8D45, "copy_string_to_cmd", hook=None,
    title="Copy string to FS command buffer",
    description="""\
Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""")
comment(0x8D45, "Start copying from offset 0", inline=True)
comment(0x8D47, "Load next byte from source string", inline=True)
comment(0x8D49, "Store to command buffer", inline=True)
comment(0x8D4C, "Advance write position", inline=True)
comment(0x8D4D, "Advance read position", inline=True)
comment(0x8D4E, "XOR with CR: result=0 if byte was CR", inline=True)
comment(0x8D50, "Loop until CR copied", inline=True)

# ============================================================
# Print directory name (&8D57)
# ============================================================
subroutine(0x8D57, "fsreply_0_print_dir", hook=None,
    title="Print directory name from reply buffer",
    description="""\
Prints characters from the FS reply buffer (&0F05+X onwards).
Null bytes (&00) are replaced with CR (&0D) for display.
Stops when a byte with bit 7 set is encountered (high-bit
terminator). Used by fscv_5_cat to display Dir. and Lib. paths.""")

# ============================================================
# Print reply buffer bytes (&8DB2)
# ============================================================
subroutine(0x8DB2, "print_reply_bytes", hook=None,
    title="Print reply buffer bytes",
    description="""\
Prints Y characters from the FS reply buffer (&0F05+X) to
the screen via OSASCI. X = starting offset, Y = count.
Used by fscv_5_cat to display directory and library names.""")

# ============================================================
# FSCV 2/4: */ and *RUN handler (&8DBF)
# ============================================================
subroutine(0x8DBF, "fscv_2_star_run", hook=None,
    title="FSCV 2/4: */ (run) and *RUN handler",
    description="""\
Parses the filename via parse_filename_gs and copies it into
the command buffer, then falls through to fsreply_4_notify_exec
to send the FS load-as-command request.""")

# ============================================================
# FS reply 4: notify and execute (&8DC5)
# ============================================================
subroutine(0x8DC5, "fsreply_4_notify_exec", hook=None,
    title="Send FS load-as-command and execute response",
    description="""\
Sets up an FS command with function code &05 (FCCMND: load as
command) using send_fs_examine. If a Tube co-processor is
present (tx_in_progress != 0), transfers the response data
to the Tube via tube_addr_claim. Otherwise jumps via the
indirect pointer at (&0F09) to execute at the load address.""")

# ============================================================
# *NET sub-command handlers (&8E3B-&8E75)
# ============================================================
subroutine(0x8E3B, "net_1_read_handle", hook=None,
    title="*NET1: read file handle from received packet",
    description="""\
Reads a file handle byte from offset &6F in the RX buffer
(net_rx_ptr), stores it in &F0, then falls through to the
common handle workspace cleanup at c8dda (clear rom_svc_num).""")

subroutine(0x8E44, "calc_handle_offset", hook=None,
    title="Calculate handle workspace offset",
    description="""\
Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""")
comment(0x8E44, "A = handle * 2", inline=True)
comment(0x8E45, "A = handle * 4", inline=True)
comment(0x8E46, "Push handle*4 onto stack", inline=True)
comment(0x8E47, "A = handle * 8", inline=True)
comment(0x8E48, "X = stack pointer", inline=True)
comment(0x8E49, "A = handle*8 + handle*4 = handle*12", inline=True)
comment(0x8E4C, "Y = offset into handle workspace", inline=True)
comment(0x8E4D, "Clean up stack (discard handle*4)", inline=True)
comment(0x8E4E, "Offset >= &48? (6 handles max)", inline=True)
comment(0x8E50, "Valid: return with C clear", inline=True)
comment(0x8E52, "Invalid: Y = 0", inline=True)
comment(0x8E54, "A = 0, C set (error)", inline=True)

label(0x8E55, "return_calc_handle")      # Return from calc_handle_offset (invalid)

entry(0x8E56)
subroutine(0x8E56, "net_2_read_handle_entry", hook=None,
    title="*NET2: read handle entry from workspace",
    description="""\
Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""")

entry(0x8E66)
subroutine(0x8E66, "net_3_close_handle", hook=None,
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
subroutine(0x8E76, "svc_8_osword", hook=None,
    title="Filing system OSWORD entry",
    description="""\
Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the
PHA/PHA/RTS dispatch at &8E80.""")

comment(0x8E76, "Command code from &EF", inline=True)
comment(0x8E78, "Subtract &0F: OSWORD &0F-&13 become indices 0-4", inline=True)

subroutine(0x8E80, "fs_osword_dispatch", hook=None,
    title="PHA/PHA/RTS dispatch for filing system OSWORDs",
    description="""\
X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
at &8E9F (low) / &8EA4 (high).""")

comment(0x8E9F, "Dispatch table: low bytes for OSWORD &0F-&13 handlers", inline=True)
comment(0x8EA4, "Dispatch table: high bytes for OSWORD &0F-&13 handlers", inline=True)

comment(0x8120, "Copy NMI handler code from ROM to RAM pages &04-&06")
comment(0x813A, "Copy NMI workspace initialiser from ROM to &0016-&0076")

# ============================================================
# Econet TX/RX handler (&8FE5)
# ============================================================
subroutine(0x8FE5, "econet_tx_rx", hook=None,
    title="Econet transmit/receive handler",
    description="""\
A=0: Initialise TX control block from ROM template at &834A
     (zero entries substituted from NMI workspace &0DDA), transmit
     it, set up RX control block, and receive reply.
A>=1: Handle transmit result (branch to cleanup at &8F49).""")

comment(0x8FE5, "A=0: set up and transmit; A>=1: handle result", inline=True)
comment(0x8F71, "Load from ROM template (zero = use NMI workspace value)", inline=True)
comment(0x8F9C, "Enable interrupts before transmit", inline=True)
comment(0x8FA2, "Dest station = &FFFF (accept reply from any station)", inline=True)
comment(0x8FB4, "Initiate receive with timeout", inline=True)
# 3.34B had BNE (error/timeout branch) at &8FBF; in 3.35D this was
# restructured into a JMP tail call at &9036, so the comment is removed.

# Data transfer loop (&8FD8-&8FF4)
comment(0x8FD0, "Receive data blocks until command byte = &00 or &0D", inline=True)
comment(0x9060, "Test for end-of-data marker (&0D)", inline=True)

# ============================================================
# OSWORD-style function dispatch (&9074)
# ============================================================
subroutine(0x9074, "osword_dispatch",
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

comment(0x9007, "Retrieve original A (function code) from stack", inline=True)
comment(0x908D, "PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it", inline=True)

# ============================================================
# NWRCH: net write character (&9036)
# ============================================================
subroutine(0x9036, "net_write_char",
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

comment(0x9037, "ROR/ASL on stacked P: zeros carry to signal success", inline=True)

# ============================================================
# Setup TX and send (&90B8)
# ============================================================
subroutine(0x90B8, "setup_tx_and_send", hook=None,
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
subroutine(0x9168, "ctrl_block_setup_alt", hook=None,
    title="Alternate entry into control block setup",
    description="""\
Sets X=&0D, Y=&7C. Tests bit 6 of &8374 to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")

subroutine(0x9171, "ctrl_block_setup", hook=None,
    title="Control block setup — main entry",
    description="""\
Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &919D indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")

comment(0x9160, "Load template byte from ctrl_block_template[X]", inline=True)

subroutine(0x919D, "ctrl_block_template", hook=None,
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
comment(0x919D, "Alt-path only → Y=&6F", inline=True)
byte(0x919E, 1)
comment(0x919E, "Alt-path only → Y=&70", inline=True)
byte(0x919F, 1)
comment(0x919F, "SKIP", inline=True)
byte(0x91A0, 1)
comment(0x91A0, "SKIP", inline=True)
byte(0x91A1, 1)
comment(0x91A1, "→ Y=&01 / Y=&73", inline=True)
byte(0x91A2, 1)
comment(0x91A2, "PAGE byte → Y=&02 / Y=&74", inline=True)
byte(0x91A3, 1)
comment(0x91A3, "→ Y=&03 / Y=&75", inline=True)
byte(0x91A4, 1)
comment(0x91A4, "→ Y=&04 / Y=&76", inline=True)
byte(0x91A5, 1)
comment(0x91A5, "→ Y=&05 / Y=&77", inline=True)
byte(0x91A6, 1)
comment(0x91A6, "PAGE byte → Y=&06 / Y=&78", inline=True)
byte(0x91A7, 1)
comment(0x91A7, "→ Y=&07 / Y=&79", inline=True)
byte(0x91A8, 1)
comment(0x91A8, "→ Y=&08 / Y=&7A", inline=True)
byte(0x91A9, 1)
comment(0x91A9, "→ Y=&09 / Y=&7B", inline=True)
byte(0x91AA, 1)
comment(0x91AA, "→ Y=&0A / Y=&7C", inline=True)
byte(0x91AB, 1)
comment(0x91AB, "STOP — main-path boundary", inline=True)
byte(0x91AC, 1)
comment(0x91AC, "→ Y=&0C (main only)", inline=True)
byte(0x91AD, 1)
comment(0x91AD, "→ Y=&0D (main only)", inline=True)
byte(0x91AE, 1)
comment(0x91AE, "SKIP (main only)", inline=True)
byte(0x91AF, 1)
comment(0x91AF, "SKIP (main only)", inline=True)
byte(0x91B0, 1)
comment(0x91B0, "→ Y=&10 (main only)", inline=True)
byte(0x91B1, 1)
comment(0x91B1, "PAGE byte → Y=&11 (main only)", inline=True)
byte(0x91B2, 1)
comment(0x91B2, "→ Y=&12 (main only)", inline=True)
byte(0x91B3, 1)
comment(0x91B3, "→ Y=&13 (main only)", inline=True)
byte(0x91B4, 1)
comment(0x91B4, "→ Y=&14 (main only)", inline=True)
byte(0x91B5, 1)
comment(0x91B5, "PAGE byte → Y=&15 (main only)", inline=True)
byte(0x91B6, 1)
comment(0x91B6, "→ Y=&16 (main only)", inline=True)
byte(0x91B7, 1)
comment(0x91B7, "→ Y=&17 (main only)", inline=True)

# ============================================================
# Bidirectional block copy (&8EB1)
# ============================================================
subroutine(0x8EB1, "copy_param_block", hook=None,
    title="Bidirectional block copy between OSWORD param block and workspace.",
    description="""\
C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)""")
comment(0x8EA9, "C=0: skip param-to-workspace copy", inline=True)
comment(0x8EAB, "Load byte from param block", inline=True)
comment(0x8EAD, "Store to workspace", inline=True)
comment(0x8EAF, "Load byte from workspace", inline=True)
comment(0x8EB1, "Store to param block (no-op if C=1)", inline=True)
comment(0x8EB3, "Advance to next byte", inline=True)
comment(0x8EB4, "Decrement byte counter", inline=True)
comment(0x8EB5, "Loop while X >= 0", inline=True)

# ============================================================
# OSWORD handler block comments
# ============================================================
label(0x8EB7, "return_copy_param")       # Return from copy_param_block

subroutine(0x8EB8, "osword_0f_handler",
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

subroutine(0x8ED2, "osword_11_handler", hook=None,
    title="OSWORD &11 handler: read JSR arguments (READRA)",
    description="""\
Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8EE7) to return just the buffer size and args size
without copying the data.""")

subroutine(0x8E7C, "osword_12_handler", hook=None,
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

subroutine(0x8F66, "osword_10_handler",
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
subroutine(0x846A, "lang_1_remote_boot", hook=None,
    title="Remote boot/execute handler",
    description="""\
Checks byte 4 of the RX control block (remote status flag).
If zero (not currently remoted), falls through to remot1 to
set up a new remote session. If non-zero (already remoted),
jumps to clear_jsr_protection and returns.""")

subroutine(0x8498, "lang_3_execute_at_0100", hook=None,
    title="Execute code at &0100",
    description="""\
Clears JSR protection, zeroes &0100-&0102 (creating a BRK
instruction at &0100 as a safe default), then JMP &0100 to
execute code received over the network. If no code was loaded,
the BRK triggers an error handler.""")

subroutine(0x84A8, "lang_4_remote_validated", hook=None,
    title="Remote operation with source validation",
    description="""\
Validates that the source station in the received packet matches
the controlling station stored in the NFS workspace. If byte 4 of
the RX control block is zero (not currently remoted), allows the
new remote session via remot1. If non-zero, compares the source
station at RX offset &80 against workspace offset &0E -- rejects
mismatched stations via clear_jsr_protection, accepts matching
stations by falling through to lang_0_insert_remote_key.""")

subroutine(0x84B8, "lang_0_insert_remote_key", hook=None,
    title="Insert remote keypress",
    description="""\
Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")

# ============================================================
# Remote operation support routines (&8FCA-&92FE)
# ============================================================
subroutine(0x8FCA, "setup_rx_buffer_ptrs", hook=None,
    title="Set up RX buffer pointers in NFS workspace",
    description="""\
Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &28. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &2C.""")

subroutine(0x90D0, "remote_cmd_dispatch", hook=None,
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

subroutine(0x9122, "match_osbyte_code", hook=None,
    title="Search remote OSBYTE table for match (NCALLP)",
    description="""\
Searches remote_osbyte_table for OSBYTE code A. X indexes the
last entry to check (table is scanned X..0). Returns Z=1 if
found. Called twice by remote_cmd_dispatch:

  X=9  -> first 10 entries (NCTBPL: execute on both machines)
  X=14 -> all 15 entries (NCTBMI: execute on terminal only)

The last 5 entries (&0F, &79, &7A, &E3, &E4) are terminal-only
because they affect the local keyboard, buffers, or function keys.

On entry: A = OSBYTE code, X = table size - 1
On exit:  Z=1 if match found, Z=0 if not""")

subroutine(0x9142, "remote_cmd_data", hook=None,
    title="Fn 8: remote OSWORD handler (NWORD)",
    description="""\
Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget -- no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")

subroutine(0x91C4, "printer_select_handler", hook=None,
    title="Fn 5: printer selection changed (SELECT)",
    description="""\
Called when the printer selection changes. Compares X against
the network printer buffer number (&F0). If it matches,
initialises the printer buffer pointer (&0D61 = &1F) and
sets the initial flag byte (&0D60 = &41). Otherwise falls
through to return.""")

subroutine(0x91D4, "remote_print_handler", hook=None,
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

subroutine(0x91F9, "store_output_byte", hook=None,
    title="Store output byte to network buffer",
    description="""\
Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""")

subroutine(0x9225, "flush_output_block", hook=None,
    title="Flush output block",
    description="""\
Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")

subroutine(0x92EB, "save_vdu_state", hook=None,
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

subroutine(0x9687, "adlc_init_workspace", hook=None,
    title="Initialise NMI workspace",
    description="""\
New in 3.35D: issues OSBYTE &8F with X=&0C (NMI claim service
request) before copying the NMI shim. Sub-entry at &968A skips
the service request for quick re-init. Then copies 32 bytes of
NMI shim from ROM (&9FE8) to RAM (&0D00), patches the current
ROM bank number into the shim's self-modifying code at &0D07,
sets TX clear flag and econet_init_flag to &80, reads station ID
from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
and re-enables NMIs by reading &FE20 (INTON side effect).""")

subroutine(0x96CF, "save_econet_state", hook=None,
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

subroutine(0x0600, "tube_code_page6", hook=None,
    title="Tube host code page 6 — reference: NFS13 (GBPB-ESCA)",
    description="""\
Copied from ROM at &954D during init. &0600-&0601 is the tail
of tube_osfile (BEQ to tube_reply_byte when done). Contains:
  &0602: tube_osgbpb — multi-byte file I/O
  &0626: tube_osbyte_short — 2-param OSBYTE (returns X)
  &063B: tube_osbyte_long — 3-param OSBYTE (returns carry+Y+X)
  &065D: tube_osword — variable-length OSWORD (buffer at &0130)
  &06A3: tube_osword_rdln — OSWORD 0 (read line, 5-byte params)
  &06BB: tube_rdln_send_line — send input line from &0700
  &06D0: tube_send_r2 — poll R2 status, write A to R2 data
  &06D9: tube_send_r4 — poll R4 status, write A to R4 data
  &06E2: tube_escape_check — check &FF, forward escape to R1
  &06E8: tube_event_handler — EVNTV: forward event (A,X,Y) via R1
  &06F7: tube_send_r1 — poll R1 status, write A to R1 data""")

# ============================================================
# OSBYTE code table for VDU state save (&9312)
# ============================================================
label(0x9312, "osbyte_vdu_table")
comment(0x9312, "3-entry OSBYTE table for lang_2_save_palette_vdu (&929F)")
byte(0x9312, 1)
comment(0x9312, "OSBYTE &85: read cursor position", inline=True)
byte(0x9313, 1)
comment(0x9313, "OSBYTE &C2: read shadow RAM allocation", inline=True)
byte(0x9314, 1)
comment(0x9314, "OSBYTE &C3: read screen start address", inline=True)

# ============================================================
# Relocated code block sources (&9308, &934D, &944D, &954D)
# ============================================================
# These labels mark the ROM storage addresses. The code is
# disassembled at its runtime addresses via move() declarations
# near the top of this file. See the preamble for addresses.

# ============================================================
# Econet TX retry (&9256)
# ============================================================
subroutine(0x9256, "econet_tx_retry", hook=None,
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
subroutine(0x929F, "lang_2_save_palette_vdu", hook=None,
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
(OSBYTE &C3) using the 3-entry table at &9312 (osbyte_vdu_table).
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")

# ============================================================
# Post-ACK scout processing (&99C5)
# ============================================================
subroutine(0x99C5, "post_ack_scout", hook=None,
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
subroutine(0x9A6F, "immediate_op", hook=None,
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
# Discard paths (&9A4A / &9A56)
# ============================================================
subroutine(0x9A4A, "discard_reset_listen", hook=None,
    title="Discard with full ADLC reset",
    description="""\
Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
then falls through to install_rx_scout_handler. Used when the ADLC is
in an unexpected state and needs a hard reset before returning
to idle listen mode. 5 references — the main error recovery path.""")

subroutine(0x9A56, "discard_listen", hook=None,
    title="Discard frame (gentle)",
    description="""\
Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
current frame reception without a full reset, then falls through
to install_rx_scout_handler. Used for clean rejection of frames
that are correctly formatted but not for us (wrong station/network).""")

# ============================================================
# Unreferenced data block (&9F5A-&9F69)
# ============================================================
# 16 bytes of unreferenced data between tx_store_result and
# tx_calc_transfer. No code in any NFS version references this
# block. The byte pattern suggests two 8-entry lookup tables
# (possibly ADLC control register values), but their original
# purpose is unknown.
comment(0x9F5A, "Unreferenced data block (purpose unknown)")
byte(0x9F5A, 16)

# ============================================================
# Transfer size calculation (&9F6A)
# ============================================================
subroutine(0x9F6A, "tx_calc_transfer", hook=None,
    title="Calculate transfer size",
    description="""\
Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")
comment(0x9F6A, "Load RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x9F6F, "AND with RXCB[7] (byte 3)", inline=True)
comment(0x9F71, "Both &FF = no buffer?", inline=True)
comment(0x9F73, "Yes: fallback path", inline=True)
comment(0x9F75, "Transmit in progress?", inline=True)
comment(0x9F78, "No: fallback path", inline=True)
comment(0x9F7D, "Set bit 1 (transfer complete)", inline=True)
comment(0x9F82, "Init borrow for 4-byte subtract", inline=True)
comment(0x9F83, "Save carry on stack", inline=True)
comment(0x9F84, "Y=4: start at RXCB offset 4", inline=True)
comment(0x9F86, "Load RXCB[Y] (current ptr byte)", inline=True)
comment(0x9F88, "Y += 4: advance to RXCB[Y+4]", inline=True)
comment(0x9F8C, "Restore borrow from previous byte", inline=True)
comment(0x9F8D, "Subtract RXCB[Y+4] (start ptr byte)", inline=True)
comment(0x9F8F, "Store result byte", inline=True)
comment(0x9F92, "Y -= 3: next source byte", inline=True)
comment(0x9F95, "Save borrow for next byte", inline=True)
comment(0x9F96, "Done all 4 bytes?", inline=True)
comment(0x9F98, "No: next byte pair", inline=True)
comment(0x9F9A, "Discard final borrow", inline=True)
comment(0x9F9B, "Save X", inline=True)
comment(0x9F9D, "Compute address of RXCB+4", inline=True)
comment(0x9FA2, "X = low byte of RXCB+4", inline=True)
comment(0x9FA3, "Y = high byte of RXCB ptr", inline=True)
comment(0x9FA5, "Tube claim type &C2", inline=True)
comment(0x9FAA, "No Tube: skip reclaim", inline=True)
comment(0x9FAC, "Tube: reclaim with scout status", inline=True)
comment(0x9FB2, "C=1: Tube address claimed", inline=True)
comment(0x9FB3, "Restore X", inline=True)
comment(0x9FB8, "Load RXCB[4] (current ptr lo)", inline=True)
comment(0x9FBD, "Subtract RXCB[8] (start ptr lo)", inline=True)
comment(0x9FBF, "Store transfer size lo", inline=True)
comment(0x9FC3, "Load RXCB[5] (current ptr hi)", inline=True)
comment(0x9FC5, "Propagate borrow only", inline=True)
comment(0x9FC7, "Temp store of adjusted hi byte", inline=True)
comment(0x9FCB, "Copy RXCB[8] to open port buffer lo", inline=True)
comment(0x9FD1, "Load RXCB[9]", inline=True)
comment(0x9FD4, "Subtract adjusted hi byte", inline=True)
comment(0x9FD6, "Store transfer size hi", inline=True)
comment(0x9FD8, "Return with C=1", inline=True)

# ============================================================
# NMI shim at end of ROM (&9FD9-&9FFF)
# ============================================================
subroutine(0x9FDA, "nmi_bootstrap_entry", hook=None,
    title="Bootstrap NMI entry point (in ROM)",
    description="""\
An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&9700). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &9700.""")

subroutine(0x9FE8, "rom_set_nmi_vector", hook=None,
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
subroutine(0x96E6, "adlc_full_reset", hook=None,
    title="ADLC full reset",
    description="""\
Aborts all activity and returns to idle RX listen mode.""")

comment(0x96E6, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", inline=True)
comment(0x96F5, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", inline=True)
comment(0x96F0, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", inline=True)

# ============================================================
# Enter RX listen mode (&96F5)
# ============================================================
subroutine(0x96F5, "adlc_rx_listen", hook=None,
    title="Enter RX listen mode",
    description="""\
TX held in reset, RX active with interrupts. Clears all status.""")

comment(0x96F5, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", inline=True)
comment(0x96FA, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", inline=True)

# ============================================================
# NMI RX scout handler (&9700) — idle listen
# ============================================================
subroutine(0x9700, "nmi_rx_scout", hook=None,
    title="NMI RX scout handler (initial byte)",
    description="""\
Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")

comment(0x9700, "A=&01: mask for SR2 bit0 (AP = Address Present)", inline=True)
comment(0x9702, "BIT SR2: Z = A AND SR2 -- tests if AP is set", inline=True)
comment(0x9705, "AP not set, no incoming data -- check for errors", inline=True)
comment(0x9707, "Read first RX byte (destination station address)", inline=True)
comment(0x970A, "Compare to our station ID (&FE18 read = INTOFF, disables NMIs)", inline=True)
comment(0x970D, "Match -- accept frame", inline=True)
comment(0x970F, "Check for broadcast address (&FF)", inline=True)
comment(0x9711, "Neither our address nor broadcast -- reject frame", inline=True)
comment(0x9713, "Flag &40 = broadcast frame", inline=True)
comment(0x9718, "Install next NMI handler at &9715 (RX scout second byte)", inline=True)

# ============================================================
# RX scout second byte handler (&971F)
# ============================================================
subroutine(0x971F, "nmi_rx_scout_net", hook=None,
    title="RX scout second byte handler",
    description="""\
Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &9747.""")

comment(0x971F, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x9722, "No RDA -- check errors", inline=True)
comment(0x9724, "Read destination network byte", inline=True)
comment(0x9727, "Network = 0 -- local network, accept", inline=True)
comment(0x9729, "EOR &FF: test if network = &FF (broadcast)", inline=True)
comment(0x972B, "Broadcast network -- accept", inline=True)
comment(0x972D, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", inline=True)

comment(0x9735, "Network = &FF broadcast: clear &0D4A", inline=True)
comment(0x9738, "Store Y offset for scout data buffer", inline=True)
comment(0x973A, "Install scout data reading loop at &9747", inline=True)

# ============================================================
# Error/discard path (&9741)
# ============================================================
subroutine(0x9741, "scout_error", hook=None,
    title="Scout error/discard handler",
    description="""\
Reached when the scout data loop sees no RDA (BPL at &9756) or
when scout completion finds unexpected SR2 state.
If SR2 & &81 is non-zero (AP or RDA still active), performs full
ADLC reset and discards. If zero (clean end), discards via &9A56.
This path is a common landing for any unexpected ADLC state during
scout reception.""")

comment(0x9741, "Read SR2", inline=True)
comment(0x9744, "Test AP (b0) | RDA (b7)", inline=True)
comment(0x9746, "Neither set -- clean end, discard via &9A40", inline=True)
comment(0x9748, "Unexpected data/status: full ADLC reset", inline=True)
comment(0x974B, "Discard and return to idle", inline=True)

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
subroutine(0x9751, hook=None,
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

comment(0x9751, "Y = buffer offset", inline=True)
comment(0x9753, "Read SR2", inline=True)
comment(0x9756, "No RDA -- error handler &9737", inline=True)
comment(0x9758, "Read data byte from RX FIFO", inline=True)
comment(0x975B, "Store at &0D3D+Y (scout buffer)", inline=True)
comment(0x975E, "Advance buffer index", inline=True)
comment(0x975F, "Read SR2 again (FV detection point)", inline=True)
comment(0x9762, "RDA set -- more data, read second byte", inline=True)
comment(0x9764, "SR2 non-zero (FV or other) -- scout completion", inline=True)
comment(0x9766, "Read second byte of pair", inline=True)
comment(0x9769, "Store at &0D3D+Y", inline=True)
comment(0x976C, "Advance and check buffer limit", inline=True)
comment(0x976F, "Buffer full (Y=12) -- force completion", inline=True)
comment(0x977B, "Save Y for next iteration", inline=True)
comment(0x9773, "Read SR2 for next pair", inline=True)
comment(0x9776, "SR2 non-zero -- loop back for more bytes", inline=True)
comment(0x9778, "SR2 = 0 -- RTI, wait for next NMI", inline=True)

# ============================================================
# Scout completion (&977B-&978F)
# ============================================================
subroutine(0x977B, "scout_complete", hook=None,
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

comment(0x977B, "CR1=&00: disable all interrupts", inline=True)
comment(0x9780, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", inline=True)
comment(0x9785, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9787, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x978A, "No FV -- not a valid frame end, error", inline=True)
comment(0x978C, "FV set but no RDA -- missing last byte, error", inline=True)
comment(0x978E, "Read last byte from RX FIFO", inline=True)
comment(0x9791, "Store last byte at &0D3D+Y", inline=True)
comment(0x9794, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", inline=True)
comment(0x9799, "Check port byte: 0 = immediate op, non-zero = data transfer", inline=True)
comment(0x979C, "Port non-zero -- look for matching receive block", inline=True)
comment(0x979E, "Port = 0 -- immediate operation handler", inline=True)

# ============================================================
# Data RX handler (&9843-&98D8)
# ============================================================
# This handler chain receives the data frame in a four-way handshake.
# After sending the scout ACK, the ROM installs &9843 to receive
# the incoming data frame.
subroutine(0x9843, "nmi_data_rx", hook=None,
    title="Data frame RX handler (four-way handshake)",
    description="""\
Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &9843 (AP+addr check) -> &9859 (net=0 check) ->
&986F (skip ctrl+port) -> &98A4 (bulk data read) -> &98D8 (completion)""")

comment(0x9837, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", inline=True)
comment(0x9843, "Read SR2 for AP check", inline=True)
comment(0x9859, "Validate source network = 0", inline=True)
comment(0x986F, "Skip control and port bytes (already known from scout)", inline=True)
comment(0x9874, "Discard control byte", inline=True)
comment(0x9877, "Discard port byte", inline=True)

# ============================================================
# Data frame bulk read (&98A4-&98D8)
# ============================================================
subroutine(0x98A4, "nmi_data_rx_bulk", hook=None,
    title="Data frame bulk read loop",
    description="""\
Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &98D8.
SR2 = 0 -> RTI, wait for next NMI to continue.""")

comment(0x98A4, "Y = buffer offset, resume from last position", inline=True)
comment(0x98A6, "Read SR2 for next pair", inline=True)

# ============================================================
# Data frame completion (&98D8-&98F4)
# ============================================================
subroutine(0x98D8, "data_rx_complete", hook=None,
    title="Data frame completion",
    description="""\
Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&977B): disables PSE (CR1=&00,
CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &9968.""")

comment(0x98D8, "CR1=&00: disable all interrupts", inline=True)
comment(0x98DD, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x98E4, "A=&02: FV mask", inline=True)
comment(0x98E6, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x98E9, "No FV -- error", inline=True)
comment(0x98EB, "FV set, no RDA -- proceed to ACK", inline=True)
comment(0x98F1, "FV+RDA: read and store last data byte", inline=True)

# ============================================================
# Scout ACK / Final ACK TX (&9968-&99B5)
# ============================================================
subroutine(0x9968, "ack_tx", hook=None,
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

comment(0x9970, "CR1=&44: RX_RESET | TIE (switch to TX mode)", inline=True)
comment(0x9975, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x997A, "Install saved next handler (&99BB for scout ACK)", inline=True)
comment(0x9984, "Load dest station from RX scout buffer", inline=True)
comment(0x9987, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x998A, "TDRA not ready -- error", inline=True)
comment(0x998C, "Write dest station to TX FIFO", inline=True)
comment(0x998F, "Write dest network to TX FIFO", inline=True)
comment(0x9995, "Install handler at &9992 (write src addr)", inline=True)

subroutine(0x999C, "nmi_ack_tx_src", hook=None,
    title="ACK TX continuation",
    description="""\
Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
comment(0x999C, "Load our station ID (also INTOFF)", inline=True)
comment(0x999F, "BIT SR1: test TDRA", inline=True)
comment(0x99A2, "TDRA not ready -- error", inline=True)
comment(0x99A4, "Write our station to TX FIFO", inline=True)
comment(0x99A7, "Write network=0 to TX FIFO", inline=True)
comment(0x99B1, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x99B6, "Install saved handler from &0D4B/&0D4C", inline=True)

# ============================================================
# INACTIVE polling loop (&9C57)
# ============================================================
subroutine(0x9C57, "inactive_poll", hook=None,
    title="INACTIVE polling loop",
    description="""\
Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9C66-&9C6B works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")

comment(0x9C5C, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9C5E, "A=&04: INACTIVE mask for SR2 bit2", inline=True)
comment(0x9C62, "INTOFF -- disable NMIs", inline=True)
comment(0x9C65, "INTOFF again (belt-and-braces)", inline=True)
comment(0x9C68, "BIT SR2: Z = &04 AND SR2 -- tests INACTIVE", inline=True)
comment(0x9C6B, "INACTIVE not set -- re-enable NMIs and loop", inline=True)
comment(0x9C6D, "Read SR1 (acknowledge pending interrupt)", inline=True)
comment(0x9C70, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x9C75, "A=&10: CTS mask for SR1 bit4", inline=True)
comment(0x9C77, "BIT SR1: tests CTS present", inline=True)
comment(0x9C7A, "CTS set -- clock hardware detected, start TX", inline=True)
comment(0x9C7C, "INTON -- re-enable NMIs (&FE20 read)", inline=True)
comment(0x9C80, "3-byte timeout counter on stack", inline=True)

# ============================================================
# Timeout error (&9C97) and TX setup (&9C93)
# ============================================================
comment(0x9C93, "TX_ACTIVE branch (A=&44 = CR1 value for TX active)")
subroutine(0x9C97, "tx_line_jammed", hook=None,
    title="TX timeout error handler (Line Jammed)",
    description="""\
Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")

comment(0x9C97, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", inline=True)
comment(0x9C9F, "Error &40 = 'Line Jammed'", inline=True)

# ============================================================
# TX preparation (&9CB1)
# ============================================================
subroutine(0x9CB1, "tx_prepare", hook=None,
    title="TX preparation",
    description="""\
Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9D5B, and re-enables NMIs.""")

comment(0x9CB1, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9CB4, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", inline=True)
comment(0x9CB9, "Install NMI handler at &9D4C (TX data handler)", inline=True)
comment(0x9CC3, "INTON -- NMIs now fire for TDRA (&FE20 read)", inline=True)

# ============================================================
# NMI TX data handler (&9D5B)
# ============================================================
subroutine(0x9D5B, "nmi_tx_data", hook=None,
    title="NMI TX data handler",
    description="""\
Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")

comment(0x9D5B, "Load TX buffer index", inline=True)
comment(0x9D5E, "BIT SR1: V=bit6(TDRA), N=bit7(IRQ)", inline=True)
comment(0x9D61, "TDRA not set -- TX error", inline=True)
comment(0x9D63, "Load byte from TX buffer", inline=True)
comment(0x9D66, "Write to TX_DATA (continue frame)", inline=True)
comment(0x9D71, "Write second byte to TX_DATA", inline=True)
comment(0x9D74, "Compare index to TX length", inline=True)
comment(0x9D77, "Frame complete -- go to TX_LAST_DATA", inline=True)
comment(0x9D79, "Check if we can send another pair", inline=True)
comment(0x9D7C, "IRQ set -- send 2 more bytes (tight loop)", inline=True)
comment(0x9D7E, "RTI -- wait for next NMI", inline=True)

# TX error path (&9D81-&9D85)
comment(0x9D81, "TX error path")
comment(0x9D81, "Error &42", inline=True)
comment(0x9D85, "CR2=&67: clear status, return to listen", inline=True)
comment(0x9D8A, "Error &41 (TDRA not ready)", inline=True)
comment(0x9D8C, "INTOFF (also loads station ID)", inline=True)
comment(0x9D8F, "PHA/PLA delay loop (256 iterations for NMI disable)", inline=True)
comment(0x9DA3, "Jump to error handler", inline=True)

# ============================================================
# TX_LAST_DATA and frame completion (&9D97)
# ============================================================
subroutine(0x9D97, "tx_last_data", hook=None,
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

comment(0x9D97, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x9D9C, "Install NMI handler at &9D94 (TX completion)", inline=True)

# ============================================================
# TX completion: switch to RX mode (&9DA3)
# ============================================================
subroutine(0x9DA3, "nmi_tx_complete", hook=None,
    title="TX completion: switch to RX mode",
    description="""\
Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> completion at &9F48
  - bit0 set at &0D4A -> four-way handshake data phase at &9EEC
  - Otherwise -> install RX reply handler at &9DC1""")

comment(0x9DA3, "CR1=&82: TX_RESET | RIE (now in RX mode)", inline=True)
comment(0x9DA8, "Test workspace flags", inline=True)
comment(0x9DAB, "bit6 not set -- check bit0", inline=True)
comment(0x9DAD, "bit6 set -- TX completion", inline=True)
comment(0x9DB7, "bit0 set -- four-way handshake data phase", inline=True)
comment(0x9DBA, "Install RX reply handler at &9DB2", inline=True)

# ============================================================
# RX reply scout handler (&9DC1)
# ============================================================
subroutine(0x9DC1, "nmi_reply_scout", hook=None,
    title="RX reply scout handler",
    description="""\
Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")

comment(0x9DC1, "A=&01: AP mask for SR2", inline=True)
comment(0x9DC3, "BIT SR2: test AP (Address Present)", inline=True)
comment(0x9DC6, "No AP -- error", inline=True)
comment(0x9DD7, "Read RX byte (destination station)", inline=True)
comment(0x9DCB, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x9DCE, "Not our station -- error/reject", inline=True)
comment(0x9DD0, "Install next handler at &9DC8 (reply continuation)", inline=True)

# ============================================================
# RX reply continuation handler (&9DD7)
# ============================================================
subroutine(0x9DD7, "nmi_reply_cont", hook=None,
    title="RX reply continuation handler",
    description="""\
Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs &9DF2 for the
remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DD9.
If IRQ is still set, falls through directly to &9DF2 without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")

comment(0x9DD7, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x9DDA, "No RDA -- error", inline=True)
comment(0x9DDC, "Read destination network byte", inline=True)
comment(0x9DDF, "Non-zero -- network mismatch, error", inline=True)
comment(0x9DE1, "Install next handler at &9DE3 (reply validation)", inline=True)
comment(0x9DE5, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
comment(0x9DE8, "IRQ set -- fall through to &9DE3 without RTI", inline=True)
comment(0x9DEA, "IRQ not set -- install handler and RTI", inline=True)

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
subroutine(0x9DF2, "nmi_reply_validate", hook=None,
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

comment(0x9DF2, "BIT SR2: test RDA (bit7). Must be set for valid reply.", inline=True)
comment(0x9DF5, "No RDA -- error (FV masking RDA via PSE would cause this)", inline=True)
comment(0x9DF7, "Read source station", inline=True)
comment(0x9DFA, "Compare to original TX destination station (&0D20)", inline=True)
comment(0x9DFD, "Mismatch -- not the expected reply, error", inline=True)
comment(0x9DFF, "Read source network", inline=True)
comment(0x9E02, "Compare to original TX destination network (&0D21)", inline=True)
comment(0x9E05, "Mismatch -- error", inline=True)
comment(0x9E07, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9E09, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9E0C, "No FV -- incomplete frame, error", inline=True)
comment(0x9E0E, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", inline=True)
comment(0x9E13, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", inline=True)
comment(0x9E18, "Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C", inline=True)
comment(0x9E22, "Load dest station for scout ACK TX", inline=True)
comment(0x9E25, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9E28, "TDRA not ready -- error", inline=True)
comment(0x9E2A, "Write dest station to TX FIFO", inline=True)
comment(0x9E2D, "Write dest network to TX FIFO", inline=True)
comment(0x9E33, "Install handler at &9E2B (write src addr for scout ACK)", inline=True)

# ============================================================
# TX data phase: write src address (&9E3A)
# ============================================================
subroutine(0x9E3A, "nmi_scout_ack_src", hook=None,
    title="TX scout ACK: write source address",
    description="""\
Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
comment(0x9E3A, "Load our station ID (also INTOFF)", inline=True)
comment(0x9E3D, "BIT SR1: test TDRA", inline=True)
comment(0x9E40, "TDRA not ready -- error", inline=True)
comment(0x9E42, "Write our station to TX FIFO", inline=True)
comment(0x9E45, "Write network=0 to TX FIFO", inline=True)

# ============================================================
# TX data phase: send data payload (&9E5F)
# ============================================================
subroutine(0x9E5F, "nmi_data_tx", hook=None,
    title="TX data phase: send payload",
    description="""\
Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9D5B but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
comment(0x9E5F, "Y = buffer offset, resume from last position", inline=True)
comment(0x9E61, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9E64, "TDRA not ready -- error", inline=True)
comment(0x9E66, "Write data byte to TX FIFO", inline=True)
comment(0x9E8C, "CR2=&3F: TX_LAST_DATA (close data frame)", inline=True)

# ============================================================
# Four-way handshake: switch to RX for final ACK (&9EEC)
# ============================================================
subroutine(0x9EEC, "handshake_await_ack", hook=None,
    title="Four-way handshake: switch to RX for final ACK",
    description="""\
After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9EF8 to receive the final ACK from the remote station.""")
comment(0x9EEC, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", inline=True)
comment(0x9EF1, "Install handler at &9EE9 (RX final ACK)", inline=True)

# ============================================================
# Four-way handshake: RX final ACK (&9EF8-&9F4C)
# ============================================================
# Same pattern as &9DC1/&9DD7/&9DF2 but for the final ACK.
# Validates that the final ACK is from the expected station.
subroutine(0x9EF8, "nmi_final_ack", hook=None,
    title="RX final ACK handler",
    description="""\
Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9DC1-&9DF2):
  &9EF8: Check AP, read dest_stn, compare to our station
  &9F0E: Check RDA, read dest_net, validate = 0
  &9F24: Check RDA, read src_stn/net, compare to TX dest
  &9F32: Check FV for frame completion
On success, stores result=0 at &9F48. On any failure, error &41.""")

comment(0x9EF8, "A=&01: AP mask", inline=True)
comment(0x9EFA, "BIT SR2: test AP", inline=True)
comment(0x9EFD, "No AP -- error", inline=True)
comment(0x9EFF, "Read dest station", inline=True)
comment(0x9F02, "Compare to our station (INTOFF side effect)", inline=True)
comment(0x9F05, "Not our station -- error", inline=True)
comment(0x9F07, "Install handler at &9EFF (final ACK continuation)", inline=True)

comment(0x9F0E, "BIT SR2: test RDA", inline=True)
comment(0x9F11, "No RDA -- error", inline=True)
comment(0x9F13, "Read dest network", inline=True)
comment(0x9F16, "Non-zero -- network mismatch, error", inline=True)
comment(0x9F18, "Install handler at &9F15 (final ACK validation)", inline=True)
comment(0x9F1C, "BIT SR1: test IRQ -- more data ready?", inline=True)
comment(0x9F1F, "IRQ set -- fall through to &9F15 without RTI", inline=True)

subroutine(0x9F24, "nmi_final_ack_validate", hook=None,
    title="Final ACK validation",
    description="""\
Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
comment(0x9F24, "BIT SR2: test RDA", inline=True)
comment(0x9F27, "No RDA -- error", inline=True)
comment(0x9F29, "Read source station", inline=True)
comment(0x9F2C, "Compare to TX dest station (&0D20)", inline=True)
comment(0x9F2F, "Mismatch -- error", inline=True)
comment(0x9F31, "Read source network", inline=True)
comment(0x9F34, "Compare to TX dest network (&0D21)", inline=True)
comment(0x9F37, "Mismatch -- error", inline=True)
comment(0x9F41, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9F43, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9F46, "No FV -- error", inline=True)

# ============================================================
# Completion and error handlers (&9F48-&9F48)
# ============================================================
subroutine(0x9F48, "tx_result_ok", hook=None,
    title="TX completion handler",
    description="""\
Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls full ADLC reset + idle listen via &9A4A.""")
comment(0x9F48, "A=0: success result code", inline=True)
comment(0x9F4A, "BEQ: always taken (A=0)", inline=True)

subroutine(0x9F4E, "tx_store_result", hook=None,
    title="TX error handler",
    description="""\
Stores error code (A) into the TX control block, sets &0D3A bit7
for completion, and returns to idle via &9A4A.
Error codes: &00=success, &40=line jammed, &41=not listening,
&42=net error.""")
comment(0x9F4E, "Y=0: index into TX control block", inline=True)
comment(0x9F50, "Store result/error code at (nmi_tx_block),0", inline=True)
comment(0x9F52, "&80: completion flag for &0D3A", inline=True)
comment(0x9F54, "Signal TX complete", inline=True)
comment(0x9F57, "Full ADLC reset and return to idle listen", inline=True)


# ============================================================
# Annotations back-propagated from NFS 3.60
# ============================================================
label(0x0000, "zp_ptr_lo")           # General-purpose ZP indirect pointer (lo) / indexed base
label(0x0001, "zp_ptr_hi")           # General-purpose ZP pointer (hi) / page counter
label(0x0002, "zp_work_2")           # Indexed scratch (control block access via X)
label(0x0003, "zp_work_3")           # Indexed scratch (control block access via X)
label(0x0012, "tube_data_ptr")       # Tube host: indirect pointer to transfer data (lo)
label(0x0013, "tube_data_ptr_hi")    # Tube host: indirect pointer to transfer data (hi)
label(0x0014, "tube_claim_flag")     # Tube host: address claim in progress flag
label(0x0015, "tube_claimed_id")     # Tube host: currently-claimed address (&80=none)
comment(0x0016, "A=&FF: signal error to co-processor via R4", inline=True)
comment(0x0018, "Send &FF error signal to Tube R4", inline=True)
comment(0x001B, "Flush any pending R2 byte", inline=True)
comment(0x001E, "A=0: send zero prefix to R2", inline=True)
comment(0x0020, "Send zero prefix byte via R2", inline=True)
comment(0x0023, "Y=0: start of error block at (&FD)", inline=True)
comment(0x0024, "Load error number from (&FD),0", inline=True)
comment(0x0026, "Send error number via R2", inline=True)
comment(0x0029, "Advance to next error string byte", inline=True)
label(0x002A, "tube_send_error_byte") # Load next error byte and send via R2 (alt entry)
comment(0x002A, "Load next error string byte", inline=True)
comment(0x002C, "Send error string byte via R2", inline=True)
comment(0x002F, "Zero byte = end of error string", inline=True)
comment(0x0030, "Loop until zero terminator sent", inline=True)
comment(0x0032, "Reset stack pointer to top", inline=True)
comment(0x0034, "TXS: set stack pointer from X", inline=True)
comment(0x0035, "Enable interrupts for main loop", inline=True)
comment(0x003A, "BIT R1 status: check WRCH request", inline=True)
comment(0x003D, "R1 not ready: check R2 instead", inline=True)
comment(0x003F, "Read character from Tube R1 data", inline=True)
comment(0x0045, "BIT R2 status: check command byte", inline=True)
comment(0x0048, "R2 not ready: loop back to R1 check", inline=True)
comment(0x004A, "Re-check R1: WRCH has priority over R2", inline=True)
comment(0x004D, "R1 ready: handle WRCH first", inline=True)
comment(0x004F, "Read command byte from Tube R2 data", inline=True)
comment(0x0052, "Self-modify JMP low byte for dispatch", inline=True)
comment(0x0054, "Dispatch to handler via indirect JMP", inline=True)
label(0x0058, "tube_xfer_page")      # Transfer source page high byte (&80 default)
label(0x0059, "tube_xfer_addr_2")    # Transfer address byte 2
label(0x005A, "tube_xfer_addr_3")    # Transfer address byte 3
label(0x0099, "prot_flags")          # PFLAGS: printer/protocol status flags
label(0x00A8, "ws_page")             # Multi-purpose: workspace page / RXCB counter / loop counter
label(0x00A9, "svc_state")           # Multi-purpose: service state / Tube flag / workspace offset
label(0x00AA, "osword_flag")         # OSWORD param byte / open-vs-read flag
label(0x00AB, "ws_ptr_lo")           # Workspace indirect pointer (lo)
label(0x00AC, "ws_ptr_hi")           # Workspace indirect pointer (hi)
label(0x00AD, "table_idx")           # OSBYTE/palette table index counter
label(0x00AE, "work_ae")             # Indexed workspace (single-use scratch)
label(0x00AF, "addr_work")           # Address work byte for comparison (indexed)
label(0x00B3, "fs_load_addr_3")     # WORK+3: load address byte 3
label(0x00B4, "fs_work_4")          # WORK+4: end address / compare target (lo)
label(0x00B5, "fs_work_5")          # WORK+5: examine arg count / end address (hi)
label(0x00B7, "fs_work_7")          # WORK+7: column count / end address byte 3
label(0x00B9, "fs_crflag")          # CRFLAG: carriage return / column flag
label(0x00BA, "fs_spool_handle")    # SPOOL1: saved spool file handle for comparison
label(0x00C0, "txcb_ctrl")          # TXCB control byte
label(0x00C1, "txcb_port")          # TXCB command/port byte
label(0x00C2, "txcb_dest")          # TXCB destination station (Y-indexed)
label(0x00C4, "txcb_start")         # TXCB data start address (lo) / reply buffer ptr
label(0x00C7, "txcb_pos")           # TXCB current transfer position (indexed)
label(0x00C8, "txcb_end")           # TXCB data end address (lo) / dest address
label(0x00CF, "fs_spool0")          # SPOOL0: handle bitmask / BGET result byte
label(0x00EF, "osbyte_a_copy")       # MOS copy of OSBYTE A parameter / command code
label(0x00F0, "osword_pb_ptr")       # OSBYTE/OSWORD parameter block pointer (lo)
label(0x00F1, "osword_pb_ptr_hi")    # OSBYTE/OSWORD parameter block pointer (hi)
label(0x00F3, "os_text_ptr_hi")      # GS text pointer (hi), paired with os_text_ptr at &F2
label(0x00F7, "osrdsc_ptr_hi")       # OSRDSC pointer (hi), paired with osrdsc_ptr at &F6
label(0x00FD, "brk_ptr")             # MOS BRK error pointer (lo), set after BRK instruction
label(0x00FF, "escape_flag")         # MOS escape flag: b7=escape condition active
comment(0x0400, "JMP to BEGIN startup entry", inline=True)
comment(0x0403, "JMP to tube_escape_check (&06A7)", inline=True)
comment(0x0406, "A>=&80: address claim; A<&80: data transfer", inline=True)
comment(0x0408, "A<&80: data transfer setup (SENDW)", inline=True)
comment(0x040A, "A>=&C0: new address claim from another host", inline=True)
comment(0x040C, "C=1: external claim, check ownership", inline=True)
comment(0x040E, "Map &80-&BF range to &C0-&FF for comparison", inline=True)
comment(0x0410, "Is this for our currently-claimed address?", inline=True)
comment(0x0412, "Match: we own it, return (no release)", inline=True)
comment(0x0416, "Store to claim-in-progress flag", inline=True)
comment(0x0418, "Return from tube_post_init", inline=True)
label(0x0419, "addr_claim_external")  # External address claim check (another host)
comment(0x0419, "Another host claiming; check if we're owner", inline=True)
comment(0x041B, "C=1: we have an active claim", inline=True)
comment(0x041D, "Compare with our claimed address", inline=True)
comment(0x041F, "Match: return (we already have it)", inline=True)
comment(0x0421, "Not ours: CLC = we don't own this address", inline=True)
comment(0x0422, "Return with C=0 (claim denied)", inline=True)
label(0x0423, "accept_new_claim")    # BCS: active claim exists, store incoming address
comment(0x0423, "Accept new claim: update our address", inline=True)
comment(0x0425, "Return with address updated", inline=True)
comment(0x0426, "Save 16-bit transfer address from (X,Y)", inline=True)
comment(0x0428, "Store address pointer low byte", inline=True)
comment(0x042A, "Send transfer type byte to co-processor", inline=True)
comment(0x042D, "X = transfer type for table lookup", inline=True)
comment(0x042E, "Y=3: send 4 bytes (address + claimed addr)", inline=True)
label(0x0430, "send_xfer_addr_bytes") # Send 4-byte transfer address to co-processor via R4
comment(0x0430, "Load transfer address byte from (X,Y)", inline=True)
comment(0x0432, "Send address byte to co-processor via R4", inline=True)
comment(0x0435, "Previous byte (big-endian: 3,2,1,0)", inline=True)
comment(0x0436, "Loop for all 4 address bytes", inline=True)
comment(0x043B, "Y=&18: enable Tube control register", inline=True)
comment(0x043D, "Enable Tube interrupt generation", inline=True)
comment(0x0440, "Look up Tube control bits for this xfer type", inline=True)
comment(0x0443, "Apply transfer-specific control bits", inline=True)
comment(0x0446, "LSR: check bit 2 (2-byte flush needed?)", inline=True)
comment(0x0447, "LSR: shift bit 2 to carry", inline=True)
label(0x0448, "poll_r4_copro_ack")   # Poll R4 status waiting for co-processor acknowledgement
comment(0x0448, "Poll R4 status for co-processor response", inline=True)
comment(0x044B, "Bit 6 clear: not ready, keep polling", inline=True)
comment(0x044D, "R4 bit 7: co-processor acknowledged transfer", inline=True)
comment(0x044F, "Type 4 = SENDW (host-to-parasite word xfer)", inline=True)
comment(0x0451, "Not SENDW type: skip release path", inline=True)
comment(0x0459, "Restart Tube main loop", inline=True)
label(0x0462, "copro_ack_nmi_check") # BCS: co-processor acknowledged, test NMI release
comment(0x0462, "LSR: check bit 0 (NMI used?)", inline=True)
comment(0x0463, "C=0: NMI not used, skip NMI release", inline=True)
comment(0x0465, "Release Tube NMI (transfer used interrupts)", inline=True)
comment(0x0467, "Write &88 to Tube control to release NMI", inline=True)
comment(0x047A, "Init: start sending from &8000", inline=True)
comment(0x047C, "Store &80 as source page high byte", inline=True)
comment(0x047E, "Store &80 as page counter initial value", inline=True)
comment(0x0480, "A=&20: bit 5 mask for ROM type check", inline=True)
comment(0x0482, "ROM type bit 5: reloc address in header?", inline=True)
comment(0x0485, "No reloc addr: use defaults", inline=True)
comment(0x0487, "Skip past copyright string to find reloc addr", inline=True)
label(0x048A, "scan_copyright_end")  # Scan past null-terminated copyright string in ROM header
comment(0x048A, "Skip past null-terminated copyright string", inline=True)
comment(0x048B, "Load next byte from ROM header", inline=True)
comment(0x048E, "Loop until null terminator found", inline=True)
comment(0x0490, "Read 4-byte reloc address from ROM header", inline=True)
comment(0x0493, "Store reloc addr byte 1 as transfer addr", inline=True)
comment(0x0495, "Load reloc addr byte 2", inline=True)
comment(0x0498, "Store as source page start", inline=True)
comment(0x049A, "Load reloc addr byte 3", inline=True)
comment(0x049D, "Load reloc addr byte 4 (highest)", inline=True)
label(0x04A0, "store_xfer_end_addr") # BEQ: no reloc flag, store default end address
comment(0x04A0, "Store high byte of end address", inline=True)
comment(0x04A2, "Store byte 3 of end address", inline=True)
comment(0x0546, "Y=channel handle from R2", inline=True)
comment(0x0547, "Read data byte from R2 for BPUT", inline=True)
comment(0x054D, "BPUT done: send acknowledge, return", inline=True)
comment(0x0553, "Y=channel handle for OSBGET", inline=True)
comment(0x0566, "JMP tube_reply_byte (dead code path)", inline=True)
comment(0x056C, "A=0: close file, else open with filename", inline=True)
comment(0x056E, "Save open mode while reading filename", inline=True)
comment(0x056F, "Read filename string from R2 into &0700", inline=True)
comment(0x0572, "Recover open mode from stack", inline=True)
comment(0x057D, "Send file handle result to co-processor", inline=True)
comment(0x0580, "OSFIND close: read handle from R2", inline=True)
comment(0x0583, "Y=handle to close", inline=True)
comment(0x0584, "A=0: close command for OSFIND", inline=True)
comment(0x0589, "Close done: send acknowledge, return", inline=True)
comment(0x058F, "Y=file handle for OSARGS", inline=True)
comment(0x0590, "Read 4-byte arg + reason from R2 into ZP", inline=True)
label(0x0592, "read_osargs_params")  # Read 4 OSARGS parameter bytes from R2 into zero page
comment(0x0592, "Read next param byte from R2", inline=True)
comment(0x0595, "Params stored at &00-&03 (little-endian)", inline=True)
comment(0x0597, "Decrement byte counter", inline=True)
comment(0x059B, "Read OSARGS reason code from R2", inline=True)
comment(0x05A1, "Send result A back to co-processor", inline=True)
comment(0x05A4, "Return 4-byte result from ZP &00-&03", inline=True)
label(0x05A6, "send_osargs_result")  # Send 4 OSARGS result bytes back to co-processor via R2
comment(0x05A6, "Load result byte from zero page", inline=True)
comment(0x05A8, "Send byte to co-processor via R2", inline=True)
comment(0x05AB, "Previous byte (count down)", inline=True)
comment(0x05AC, "Loop for all 4 bytes", inline=True)
comment(0x05AE, "Return to Tube main loop", inline=True)
comment(0x05B1, "X=0: initialise string buffer index", inline=True)
comment(0x05B3, "X=0, Y=0: buffer at &0700, offset 0", inline=True)
comment(0x05B5, "Read next string byte from R2", inline=True)
comment(0x05B8, "Store byte in string buffer at &0700+Y", inline=True)
comment(0x05BB, "Next buffer position", inline=True)
comment(0x05BC, "Y overflow: string too long, truncate", inline=True)
comment(0x05BE, "Check for CR terminator", inline=True)
comment(0x05C0, "Not CR: continue reading string", inline=True)
label(0x05C2, "string_buf_done")     # BEQ: overflow or CR found, set XY=&0700/RTS
comment(0x05C2, "Y=7: set XY=&0700 for OSCLI/OSFIND", inline=True)
comment(0x05C4, "Return with XY pointing to &0700", inline=True)
comment(0x05C8, "Execute * command via OSCLI", inline=True)
comment(0x05CB, "&7F = success acknowledgement", inline=True)
comment(0x05CD, "Poll R2 status until ready", inline=True)
comment(0x05D0, "Bit 6 clear: not ready, loop", inline=True)
comment(0x05D2, "Write byte to R2 data register", inline=True)
comment(0x05D5, "Return to Tube main loop", inline=True)
comment(0x05DA, "Read next control block byte from R2", inline=True)
comment(0x05DD, "Store at &01+X (descending)", inline=True)
comment(0x05DF, "Decrement byte counter", inline=True)
comment(0x05E0, "Loop for all 16 bytes", inline=True)
comment(0x05E2, "Read filename string from R2 into &0700", inline=True)
comment(0x05E5, "XY=&0700: filename pointer for OSFILE", inline=True)
comment(0x05E7, "Store Y=7 as pointer high byte", inline=True)
comment(0x05E9, "Y=0 for OSFILE control block offset", inline=True)
comment(0x05EB, "Read OSFILE reason code from R2", inline=True)
comment(0x05EE, "Execute OSFILE operation", inline=True)
comment(0x05F3, "Send result A (object type) to co-processor", inline=True)
comment(0x05F6, "Return 16-byte control block to co-processor", inline=True)
label(0x05F8, "send_osfile_ctrl_blk") # Send 16-byte OSFILE control block to co-processor via R2
comment(0x05F8, "Load control block byte", inline=True)
comment(0x05FA, "Send byte to co-processor via R2", inline=True)
comment(0x05FD, "Decrement byte counter", inline=True)
comment(0x05FE, "Loop for all 16 bytes", inline=True)
comment(0x0635, "Send X result for 2-param OSBYTE", inline=True)
comment(0x0649, "Send carry result to co-processor", inline=True)
comment(0x064B, "OSBYTE &9D (fast Tube BPUT): no result needed", inline=True)
comment(0x064F, "Encode carry (error flag) into bit 7", inline=True)
comment(0x0658, "Send Y result, then fall through to send X", inline=True)
comment(0x0666, "Read param block length from R2", inline=True)
comment(0x0669, "DEX: length 0 means no params to read", inline=True)
comment(0x0674, "Store param bytes into block at &0128", inline=True)
comment(0x067A, "Restore OSWORD number from Y", inline=True)
label(0x067B, "skip_param_read")     # BMI: zero-length params, skip R2 read loop
comment(0x067B, "XY=&0128: param block address for OSWORD", inline=True)
label(0x0687, "poll_r2_osword_result") # Poll R2 status waiting for OSWORD result data
comment(0x068C, "Read result block length from R2", inline=True)
comment(0x0690, "No results to send: return to main loop", inline=True)
comment(0x0692, "Send result block bytes from &0128 via R2", inline=True)
label(0x06A5, "read_rdln_ctrl_block") # Read 5-byte OSWORD 0 control block from R2
comment(0x06AD, "X=0 after loop, A=0 for OSWORD 0 (read line)", inline=True)
comment(0x06B4, "C=0: line read OK; C=1: escape pressed", inline=True)
comment(0x06B6, "&FF = escape/error signal to co-processor", inline=True)
comment(0x06BD, "&7F = line read successfully", inline=True)
comment(0x06C9, "Loop until CR terminator sent", inline=True)
comment(0x06E2, "Check OS escape flag at &FF", inline=True)
comment(0x06E4, "SEC+ROR: put bit 7 of &FF into carry+bit 7", inline=True)
comment(0x06E6, "Escape set: forward to co-processor via R1", inline=True)
comment(0x06E8, "EVNTV: forward event A, Y, X to co-processor", inline=True)
comment(0x06E9, "Send &00 prefix (event notification)", inline=True)
label(0x0D11, "install_nmi_handler") # Entry: A=handler offset, installs NMI vector
label(0x0DE6, "nmi_sub_table")      # NMI substitution data (Y-indexed lookup)
label(0x0DF0, "rom_ws_table")       # ROM workspace pointer table (16 bytes, X=ROM#)
label(0x0DFE, "fs_context_base")    # Base for Y-indexed access to FS context at &0E00+
label(0x0E0B, "fs_context_hi")      # Command context high byte
label(0x0E16, "fs_work_16")         # FS workspace byte at offset &16
label(0x0E30, "fs_filename_buf")    # Parsed filename buffer
label(0x0EF7, "fs_reply_data")      # FS reply data area
label(0x0F06, "fs_func_code")           # Data byte 1: function code / direction flag / reply count
label(0x0F07, "fs_data_count")          # Data byte 2: block size (hi) / entry count
label(0x0F08, "fs_reply_cmd")           # Data byte 3: reply command / extent
label(0x0F09, "fs_load_vector")         # Data byte 4: indirect JMP target (load address lo)
label(0x0F0B, "fs_load_upper")          # Data byte 6: load address upper byte check
label(0x0F0C, "fs_addr_check")          # Data byte 7: address range validation byte
label(0x0F0D, "fs_file_len")            # Data byte 8: file length byte (indexed)
label(0x0F0E, "fs_file_attrs")          # Data byte 9: encoded file attributes
label(0x0F10, "fs_file_len_3")          # Data byte &0B: file length byte 3
label(0x0F11, "fs_obj_type")            # Data byte &0C: object type from FS reply
label(0x0F12, "fs_access_level")        # Data byte &0D: access level / length high
label(0x0F13, "fs_reply_stn")           # Data byte &0E: station number from FS reply
label(0x0F14, "fs_len_clear")           # Data byte &0F: length high (cleared on success)
label(0x0F16, "fs_boot_data")           # Data byte &11: boot option in reply area
label(0x0FDE, "fs_handle_mask")         # Handle bitmask for sequence tracking
label(0x0FDF, "fs_error_flags")         # BSXMIT error/status flags
label(0x0FE0, "fs_error_buf")           # Error buffer at end of FS page
comment(0x806F, "Command index >= 4: invalid *NET sub-command", inline=True)
comment(0x8071, "Out of range: return via c80e3/RTS", inline=True)
comment(0x8073, "X = command index (0-3)", inline=True)
comment(0x8074, "Clear &A9 (used by dispatch)", inline=True)
comment(0x8076, "Store zero to &A9", inline=True)
comment(0x8078, "Preserve A before dispatch", inline=True)
comment(0x8079, "Y=&21: base offset for *NET commands (index 33+)", inline=True)
comment(0x807B, "ALWAYS branch to dispatch", inline=True)
comment(0x807E, "Load next char from command line", inline=True)
comment(0x8080, "Skip spaces", inline=True)
comment(0x8082, "Loop back to skip leading spaces", inline=True)
comment(0x8084, "Colon = interactive remote command prefix", inline=True)
comment(0x8086, "Char >= ':': skip number parsing", inline=True)
label(0x80B8, "prepare_cmd_dispatch")   # Prepare FS command and dispatch recognised *command
comment(0x80D0, "Y=&13: base offset for FSCV dispatch (indices 20+)", inline=True)
comment(0x80D4, "X >= 5: invalid reason code, return", inline=True)
label(0x80D6, "svc_dispatch_range")     # Service dispatch range check (out of range: return)
comment(0x80D6, "Out of range: return via RTS", inline=True)
comment(0x80D8, "Y=&0E: base offset for language handlers (index 15+)", inline=True)
comment(0x80DB, "Decrement base offset counter", inline=True)
comment(0x80DC, "Loop until Y exhausted", inline=True)
comment(0x80DE, "Y=&FF (no further use)", inline=True)
label(0x80EA, "check_svc_high")         # Test service >= &FE (high-priority dispatch)
comment(0x80EA, "Service >= &FE?", inline=True)
comment(0x80EC, "Service < &FE: skip to &12/dispatch check", inline=True)
comment(0x80EE, "Service &FF: full init (vectors + RAM copy)", inline=True)
comment(0x80F0, "Service &FE: Y=0?", inline=True)
comment(0x80F2, "Y=0: no Tube data, skip to &12 check", inline=True)
comment(0x8120, "Load ROM byte from page &93", inline=True)
comment(0x8123, "Store to page &04 (Tube code)", inline=True)
comment(0x8126, "Load ROM byte from page &94", inline=True)
comment(0x8129, "Store to page &05 (dispatch table)", inline=True)
comment(0x812C, "Load ROM byte from page &95", inline=True)
comment(0x812F, "Store to page &06", inline=True)
comment(0x8132, "DEY wraps 0 -> &FF on first iteration", inline=True)
comment(0x8133, "Loop until 256 bytes copied per page", inline=True)
comment(0x8135, "Run post-init routine in copied code", inline=True)
comment(0x8138, "X=&60: copy 97 bytes (&60..&00)", inline=True)
label(0x813A, "copy_nmi_workspace")  # Copy 97 bytes of NMI workspace init data from ROM
comment(0x813A, "Load NMI workspace init byte from ROM", inline=True)
comment(0x813D, "Store to zero page &16+X", inline=True)
comment(0x813F, "Next byte", inline=True)
comment(0x8140, "Loop until all workspace bytes copied", inline=True)
label(0x814E, "not_svc_12_nfs")        # BNE: not service &12 or not NFS (Y!=5)
comment(0x814E, "Service >= &0D?", inline=True)
label(0x8150, "svc_unhandled_return")   # Unhandled service (>= &0D): return unclaimed
comment(0x8150, "Service >= &0D: not handled, return", inline=True)
label(0x8152, "do_svc_dispatch")        # BNE: entry to TAX/workspace save/dispatch
comment(0x8152, "X = service number (dispatch index)", inline=True)
comment(0x8153, "Save &A9 (current service state)", inline=True)
comment(0x8155, "Push saved &A9", inline=True)
comment(0x8156, "Save &A8 (workspace page number)", inline=True)
comment(0x8158, "Push saved &A8", inline=True)
comment(0x8159, "Store service number to &A9", inline=True)
comment(0x815B, "Store Y (page number) to &A8", inline=True)
comment(0x815D, "A = Y for dispatch table offset", inline=True)
comment(0x815E, "Y=0: base offset for service dispatch", inline=True)
comment(0x8160, "Dispatch to service handler", inline=True)
comment(0x8163, "Recover service claim status from &A9", inline=True)
comment(0x8165, "Restore saved &A8 from stack", inline=True)
comment(0x8166, "Write back &A8", inline=True)
comment(0x8168, "Restore saved A from service dispatch", inline=True)
comment(0x8169, "Save to workspace &A9", inline=True)
comment(0x816B, "Return ROM number in A", inline=True)
comment(0x8179, "ROM offset for \"ROFF\" (copyright suffix)", inline=True)
comment(0x817B, "Try matching *ROFF command", inline=True)
comment(0x817E, "No match: try *NET", inline=True)
comment(0x8180, "Y=4: offset of keyboard disable flag", inline=True)
comment(0x8182, "Read flag from RX buffer", inline=True)
comment(0x8184, "Zero: keyboard not disabled, skip", inline=True)
comment(0x8186, "A=0: value to clear flag and re-enable", inline=True)
comment(0x8189, "Clear keyboard disable flag in buffer", inline=True)
comment(0x818C, "OSBYTE &C9: Econet keyboard disable", inline=True)
comment(0x818E, "Re-enable keyboard (X=0, Y=0)", inline=True)
comment(0x8191, "Function &0A: remote operation complete", inline=True)
comment(0x8193, "Send notification to controlling station", inline=True)
comment(0x8196, "Save X (return value from TX)", inline=True)
comment(0x8198, "OSBYTE &CE: first system mask to reset", inline=True)
label(0x819A, "clear_osbyte_masks")   # Loop clearing OSBYTE mask bytes with AND &7F
comment(0x819A, "Restore X for OSBYTE call", inline=True)
comment(0x819C, "Y=&7F: AND mask (clear bit 7)", inline=True)
comment(0x819E, "Reset system mask byte", inline=True)
comment(0x81A1, "Advance to next OSBYTE (&CE -> &CF)", inline=True)
comment(0x81A3, "Reached &D0? (past &CF)", inline=True)
comment(0x81A5, "No: reset &CF too", inline=True)
label(0x81A7, "skip_kbd_reenable")      # BEQ: keyboard not disabled, skip re-enable
comment(0x81A7, "A=0: clear remote state", inline=True)
comment(0x81A9, "Clear &A9 (service dispatch state)", inline=True)
comment(0x81AB, "Clear workspace byte", inline=True)
comment(0x81AD, "Return", inline=True)
label(0x81AE, "match_net_cmd")          # Try matching *NET command text
comment(0x81AE, "X=5: ROM offset for \"NET\" match", inline=True)
comment(0x81B0, "Try matching *NET command", inline=True)
comment(0x81B3, "No match: return unclaimed", inline=True)
comment(0x81B5, "Notify current FS of shutdown (FSCV A=6)", inline=True)
comment(0x81B8, "C=1 for ROR", inline=True)
comment(0x81B9, "Set bit 7 of l00a8 (inhibit auto-boot)", inline=True)
comment(0x81BB, "Claim OS vectors, issue service &0F", inline=True)
comment(0x81BE, "Y=&1D: top of FS state range", inline=True)
comment(0x81C0, "Copy FS state from RX buffer...", inline=True)
comment(0x81C2, "...to workspace (offsets &15-&1D)", inline=True)
comment(0x81C5, "Next byte (descending)", inline=True)
comment(0x81C6, "Loop until offset &14 done", inline=True)
comment(0x81C8, "Continue loop", inline=True)
comment(0x81CA, "ALWAYS branch to init_fs_vectors", inline=True)
comment(0x81FD, "Return (service not claimed)", inline=True)
comment(0x81FE, "FSCV reason 6 = FS shutdown", inline=True)
comment(0x8200, "Tail-call via filing system control vector", inline=True)
comment(0x8203, "Notify current FS of shutdown", inline=True)
comment(0x8206, "OSBYTE &7A: scan keyboard", inline=True)
comment(0x820C, "No key pressed: proceed with auto-boot", inline=True)
comment(0x820E, "XOR with &55: result=0 if key is 'N'", inline=True)
comment(0x8210, "Not 'N': return without claiming", inline=True)
comment(0x8213, "OSBYTE &78: clear key-pressed state", inline=True)
comment(0x8218, "Print 'Econet Station ' banner", inline=True)
comment(0x822C, "Load station number", inline=True)
comment(0x822E, "Print as 3-digit decimal", inline=True)
comment(0x8231, "BIT trick: bit 5 of SR2 = clock present", inline=True)
comment(0x8233, "Test DCD: clock present if bit 5 clear", inline=True)
comment(0x8236, "Clock present: skip warning", inline=True)
comment(0x8238, "Print ' No Clock' warning", inline=True)
comment(0x8244, "NOP (padding after inline string)", inline=True)
label(0x8245, "skip_no_clock_msg")     # BEQ: clock present, skip "No Clock" message
comment(0x8245, "Print two CRs (blank line)", inline=True)
comment(0x824F, "Write to FILEV-FSCV vector table", inline=True)
comment(0x8252, "Next byte (descending)", inline=True)
comment(0x8253, "Loop until all 14 bytes copied", inline=True)
comment(0x8255, "Read ROM ptr table addr, install NETV", inline=True)
comment(0x8258, "Install 7 handler entries in ROM ptr table", inline=True)
comment(0x825A, "7 FS vectors to install", inline=True)
comment(0x825C, "Install each 3-byte vector entry", inline=True)
comment(0x825F, "X=0 after loop; store as workspace offset", inline=True)
comment(0x826A, "Issue service &0A", inline=True)
comment(0x826D, "Non-zero after hard reset: skip auto-boot", inline=True)
comment(0x8271, "X = lo byte of auto-boot string at &8292", inline=True)
comment(0x827E, "Auto-boot string tail / NETV handler data", inline=True)
comment(0x82A2, "Already at page &10 or above?", inline=True)
comment(0x82A4, "Yes: nothing to claim", inline=True)
comment(0x82A6, "Claim pages &0D-&0F (3 pages)", inline=True)
comment(0x82B0, "A=0 for clearing workspace", inline=True)
comment(0x82B2, "Y=4: remote status offset", inline=True)
comment(0x82B4, "Clear status byte in net receive buffer", inline=True)
comment(0x82B6, "Y=&FF: used for later iteration", inline=True)
comment(0x82B8, "Clear RX ptr low byte", inline=True)
comment(0x82BA, "Clear workspace ptr low byte", inline=True)
comment(0x82BC, "Clear RXCB iteration counter", inline=True)
comment(0x82BE, "Clear TX semaphore (no TX in progress)", inline=True)
comment(0x82C1, "X=0 for OSBYTE", inline=True)
comment(0x82C7, "X = break type from OSBYTE result", inline=True)
comment(0x82CA, "Y=&15: printer station offset in RX buffer", inline=True)
comment(0x82CC, "&FE = no server selected", inline=True)
comment(0x82D1, "Store &FE at printer station offset", inline=True)
comment(0x82D3, "A=0 for clearing workspace fields", inline=True)
comment(0x82D5, "Clear network number", inline=True)
comment(0x82D8, "Clear protection status", inline=True)
comment(0x82DB, "Clear message flag", inline=True)
comment(0x82DE, "Clear boot option", inline=True)
comment(0x82E1, "Y=&16", inline=True)
comment(0x82E2, "Clear net number at RX buffer offset &16", inline=True)
comment(0x82E4, "Init printer server: station &FE, net 0", inline=True)
comment(0x82E6, "Store net 0 at workspace offset 3", inline=True)
comment(0x82E8, "Y=2: printer station offset", inline=True)
comment(0x82E9, "&FE = no printer server", inline=True)
comment(0x82EB, "Store &FE at printer station in workspace", inline=True)
label(0x82ED, "init_rxcb_entries")   # Mark all RXCBs as available (&3F) in NFS workspace
comment(0x82ED, "Load RXCB counter", inline=True)
comment(0x82EF, "Convert to workspace byte offset", inline=True)
comment(0x82F2, "C=1: past max handles, done", inline=True)
comment(0x82F4, "Mark RXCB as available", inline=True)
comment(0x82F6, "Write &3F flag to workspace", inline=True)
comment(0x82F8, "Next RXCB number", inline=True)
comment(0x82FA, "Loop for all RXCBs", inline=True)
label(0x82FC, "read_station_id")       # BEQ/BCS: soft break or RXCBs done, read &FE18
comment(0x82FF, "Y=&14: station ID offset in RX buffer", inline=True)
comment(0x8301, "Store our station number", inline=True)
comment(0x8306, "Enable user-level RX (LFLAG=&40)", inline=True)
comment(0x8308, "Store to rx_flags", inline=True)
comment(0x830B, "OSBYTE &A8: read ROM pointer table address", inline=True)
comment(0x830D, "X=0: read low byte", inline=True)
comment(0x830F, "Y=&FF: read high byte", inline=True)
comment(0x8311, "Returns table address in X (lo) Y (hi)", inline=True)
comment(0x8314, "Store table base address low byte", inline=True)
comment(0x8316, "Store table base address high byte", inline=True)
comment(0x8318, "NETV extended vector offset in ROM ptr table", inline=True)
comment(0x831A, "Set NETV low byte = &36 (vector dispatch)", inline=True)
comment(0x831D, "Install 1 entry (NETV) in ROM ptr table", inline=True)
comment(0x831F, "Load handler address low byte from table", inline=True)
comment(0x8322, "Store to ROM pointer table", inline=True)
comment(0x8324, "Next byte", inline=True)
comment(0x8325, "Load handler address high byte from table", inline=True)
comment(0x8328, "Store to ROM pointer table", inline=True)
comment(0x832A, "Next byte", inline=True)
comment(0x832B, "Write current ROM bank number", inline=True)
comment(0x832D, "Store ROM number to ROM pointer table", inline=True)
comment(0x832F, "Advance to next entry position", inline=True)
comment(0x8330, "Count down entries", inline=True)
comment(0x8331, "Loop until all entries installed", inline=True)
comment(0x8333, "Y = workspace high byte + 1 = next free page", inline=True)
comment(0x8333, "Y = next workspace page for MOS", inline=True)
comment(0x8335, "Advance past workspace page", inline=True)
comment(0x8336, "Return; Y = page after NFS workspace", inline=True)
comment(0x8337, "Copy 10 bytes: FS state to workspace backup", inline=True)
comment(0x833F, "Offsets &15-&1D: server, handles, OPT, etc.", inline=True)
comment(0x8348, "A=&90: FS reply port (PREPLY)", inline=True)
comment(0x834A, "Init TXCB from template", inline=True)
comment(0x834D, "Store port number in TXCB", inline=True)
comment(0x834F, "Control byte: 3 = transmit", inline=True)
comment(0x8351, "Store control byte in TXCB", inline=True)
comment(0x8353, "Decrement TXCB flag to arm TX", inline=True)
comment(0x8356, "Preserve A across call", inline=True)
comment(0x8357, "Copy 12 bytes (Y=11..0)", inline=True)
comment(0x8359, "Load template byte", inline=True)
comment(0x835C, "Store to TX control block at &00C0", inline=True)
comment(0x835F, "Y < 2: also copy FS server station/network", inline=True)
comment(0x8361, "Skip station/network copy for Y >= 2", inline=True)
comment(0x8363, "Load FS server station (Y=0) or network (Y=1)", inline=True)
comment(0x8366, "Store to dest station/network at &00C2", inline=True)
comment(0x8369, "Next byte (descending)", inline=True)
comment(0x836A, "Loop until all 12 bytes copied", inline=True)
comment(0x836C, "Restore A", inline=True)
comment(0x836D, "Return", inline=True)
label(0x8374, "tx_ctrl_upper")       # TX control template upper half (high bytes/masks)
comment(0x837A, "Save flag byte for command", inline=True)
comment(0x837D, "C=1: include flag in FS command", inline=True)
comment(0x837E, "ALWAYS branch to prepare_fs_cmd", inline=True)
comment(0x8380, "V=0: command has no flag byte", inline=True)
comment(0x8381, "ALWAYS branch to prepare_fs_cmd", inline=True)
comment(0x838A, "V=0: standard FS command path", inline=True)
comment(0x838B, "Copy URD handle from workspace to buffer", inline=True)
comment(0x838E, "Store URD at &0F02", inline=True)
comment(0x8399, "Y=1: copy CSD (offset 1) then LIB (offset 0)", inline=True)
label(0x839B, "copy_dir_handles")       # Copy CSD and LIB handles into FS command header
comment(0x839B, "Copy CSD and LIB handles to command buffer", inline=True)
comment(0x839E, "Store at &0F03 (CSD) and &0F04 (LIB)", inline=True)
comment(0x83A1, "Y=function code", inline=True)
comment(0x83A2, "Loop for both handles", inline=True)
comment(0x83A4, "Save carry (FS path vs byte-stream)", inline=True)
comment(0x83A5, "Reply port &90 (PREPLY)", inline=True)
comment(0x83A7, "Store at &0F00 (HDRREP)", inline=True)
comment(0x83AA, "Copy TX template to &00C0", inline=True)
comment(0x83AD, "A = X (buffer extent)", inline=True)
comment(0x83AE, "HPTR = header (5) + data (X) bytes to send", inline=True)
comment(0x83B0, "Store to TXCB end-pointer low", inline=True)
comment(0x83B2, "Restore carry flag", inline=True)
comment(0x83B3, "C=1: byte-stream path (BSXMIT)", inline=True)
comment(0x83B5, "Save flags for send_fs_reply_cmd", inline=True)
comment(0x83B6, "Point net_tx_ptr to &00C0; transmit", inline=True)
comment(0x83B9, "Restore flags", inline=True)
comment(0x83BA, "Save flags (V flag state)", inline=True)
comment(0x83BB, "Set up RX wait for FS reply", inline=True)
comment(0x83C0, "Transmit and wait (BRIANX)", inline=True)
comment(0x83C3, "Restore flags", inline=True)
comment(0x83C4, "Y=1: skip past command code byte", inline=True)
comment(0x83C5, "Load return code from FS reply", inline=True)
comment(0x83C7, "X = return code", inline=True)
comment(0x83C8, "Zero: success, return", inline=True)
comment(0x83CA, "V=0: standard path, error is fatal", inline=True)
comment(0x83CC, "ADC #&2A: test for &D6 (not found)", inline=True)
label(0x83CE, "check_fs_error")        # BVC: standard path, BNE to store_fs_error
comment(0x83CE, "Non-zero: hard error, go to FSERR", inline=True)
comment(0x83D0, "Return (success or soft &D6 error)", inline=True)
comment(0x83D1, "Discard saved flags from stack", inline=True)
comment(0x83D2, "X=&C0: TXCB address for byte-stream TX", inline=True)
comment(0x83D4, "Y++ past command code", inline=True)
comment(0x83D5, "Byte-stream transmit with retry", inline=True)
comment(0x83D8, "Store result to &B3", inline=True)
comment(0x83DA, "C=0: success, check reply code", inline=True)
comment(0x83DD, "Save A (BPUT byte) on stack", inline=True)
comment(0x83DE, "Also save byte at &0FDF for BSXMIT", inline=True)
comment(0x83E1, "Transfer X for stack save", inline=True)
comment(0x83E2, "Save X on stack", inline=True)
comment(0x83E3, "Transfer Y (handle) for stack save", inline=True)
comment(0x83E4, "Save Y (handle) on stack", inline=True)
comment(0x83E5, "Save P (C = BPUT/BGET selector) on stack", inline=True)
comment(0x83E6, "Save handle for SPOOL/EXEC comparison later", inline=True)
comment(0x83E8, "Convert handle Y to single-bit mask", inline=True)
comment(0x83EB, "Store handle bitmask at &0FDE", inline=True)
comment(0x83EE, "Store handle bitmask for sequence tracking", inline=True)
comment(0x83F0, "&90 = data port (PREPLY)", inline=True)
comment(0x83F2, "Store reply port in command buffer", inline=True)
comment(0x83F5, "Set up 12-byte TXCB from template", inline=True)
comment(0x83F8, "CB reply buffer at &0FDC", inline=True)
comment(0x83FA, "Store reply buffer ptr low in TXCB", inline=True)
comment(0x83FC, "Error buffer at &0FE0", inline=True)
comment(0x83FE, "Store error buffer ptr low in TXCB", inline=True)
comment(0x8400, "Y=1 (from init_tx_ctrl_block exit)", inline=True)
comment(0x8401, "X=9: BPUT function code", inline=True)
comment(0x8403, "Restore C: selects BPUT (0) vs BGET (1)", inline=True)
comment(0x8404, "C=0 (BPUT): keep X=9", inline=True)
comment(0x8407, "Store function code at &0FDD", inline=True)
comment(0x840D, "X=&C0: TXCB address for econet_tx_retry", inline=True)
comment(0x840F, "Transmit via byte-stream protocol", inline=True)
comment(0x8412, "Load reply byte from buffer", inline=True)
comment(0x8415, "Zero reply = success, skip error handling", inline=True)
comment(0x8417, "Copy 32-byte reply to error buffer at &0FE0", inline=True)
comment(0x8419, "Load reply byte at offset Y", inline=True)
comment(0x841C, "Store to error buffer at &0FE0+Y", inline=True)
comment(0x841F, "Next byte (descending)", inline=True)
comment(0x8420, "Loop until all 32 bytes copied", inline=True)
comment(0x8423, "Returns X=EXEC handle, Y=SPOOL handle", inline=True)
comment(0x8428, "')': offset into \"SP.\" string at &8529", inline=True)
comment(0x842A, "Y=value of *SPOOL file handle", inline=True)
label(0x8436, "close_spool_exec")       # BEQ: SPOOL handle matched, OSCLI close
comment(0x8436, "X = string offset for OSCLI close", inline=True)
comment(0x8437, "Y=&85: high byte of OSCLI string in ROM", inline=True)
comment(0x8439, "Close SPOOL/EXEC via \"*SP.\" or \"*E.\"", inline=True)
label(0x843C, "dispatch_fs_error")     # BNE: no handle match, reset ptr for FSERR
comment(0x843C, "Reset CB pointer to error buffer at &0FE0", inline=True)
comment(0x843E, "Reset reply ptr to error buffer", inline=True)
comment(0x8440, "Reload reply byte for error dispatch", inline=True)
comment(0x8443, "Remember raw FS error code", inline=True)
comment(0x8446, "Y=1: point to error number byte in reply", inline=True)
comment(0x8448, "Clamp FS errors below &A8 to standard &A8", inline=True)
comment(0x844A, "Error >= &A8: keep original value", inline=True)
comment(0x844C, "Error < &A8: override with standard &A8", inline=True)
comment(0x844E, "Write clamped error number to reply buffer", inline=True)
label(0x8450, "error_code_clamped")    # BCS: error >= &A8, skip clamp, start scan
comment(0x8450, "Start scanning from offset &FF (will INY to 0)", inline=True)
label(0x8452, "copy_error_to_brk")      # Copy FS error reply to &0100 as BRK error block
comment(0x8452, "Next byte in reply buffer", inline=True)
comment(0x8453, "Copy reply buffer to &0100 for BRK execution", inline=True)
comment(0x8455, "Build BRK error block at &0100", inline=True)
comment(0x8458, "Scan for CR terminator (&0D)", inline=True)
comment(0x845A, "Continue until CR found", inline=True)
comment(0x845C, "Replace CR with zero = BRK error block end", inline=True)
comment(0x845F, "Execute as BRK error block at &0100; ALWAYS", inline=True)
comment(0x8461, "Save updated sequence number", inline=True)
comment(0x8464, "Restore Y from stack", inline=True)
comment(0x8466, "Restore X from stack", inline=True)
comment(0x8468, "Restore A from stack", inline=True)
comment(0x8469, "Return to caller", inline=True)
comment(0x846A, "Y=4: remote status flag offset", inline=True)
comment(0x846C, "Read remote status from RX CB", inline=True)
comment(0x846E, "Zero: not remoted, set up session", inline=True)
comment(0x8470, "Already remoted: clear and return", inline=True)
comment(0x8473, "Set remote status: bits 0+3 (ORA #9)", inline=True)
comment(0x8475, "Store updated remote status", inline=True)
comment(0x8477, "X=&80: RX data area offset", inline=True)
comment(0x8479, "Y=&80: read source station low", inline=True)
comment(0x847B, "Read source station lo from RX data at &80", inline=True)
comment(0x847D, "Save source station low byte", inline=True)
comment(0x847E, "Y=&81", inline=True)
comment(0x847F, "Read source station hi from RX data at &81", inline=True)
comment(0x8481, "Save controlling station to workspace &0E/&0F", inline=True)
comment(0x8483, "Store station high to ws+&0F", inline=True)
comment(0x8485, "Y=&0E", inline=True)
comment(0x8486, "Restore source station low", inline=True)
comment(0x8487, "Store station low to ws+&0E", inline=True)
comment(0x8489, "Clear OSBYTE &CE/&CF flags", inline=True)
comment(0x848C, "Set up TX control block", inline=True)
comment(0x848F, "X=1: disable keyboard", inline=True)
comment(0x8491, "Y=0 for OSBYTE", inline=True)
comment(0x8493, "Disable keyboard for remote session", inline=True)
comment(0x8498, "Allow JSR to page 1 (stack page)", inline=True)
comment(0x849B, "Zero bytes &0100-&0102", inline=True)
label(0x849F, "zero_exec_header")      # Zero bytes &0100-&0102 before executing downloaded code
comment(0x849F, "BRK at &0100 as safe default", inline=True)
label(0x84A5, "execute_downloaded")      # JMP &0100: execute downloaded code at stack page
comment(0x84A5, "Execute downloaded code", inline=True)
comment(0x84A8, "Y=4: RX control block byte 4 (remote status)", inline=True)
comment(0x84AA, "Read remote status flag", inline=True)
comment(0x84AC, "Zero = not remoted; allow new session", inline=True)
comment(0x84AE, "Read source station from RX data at &80", inline=True)
comment(0x84B0, "A = source station number", inline=True)
comment(0x84B2, "Compare against controlling station at &0E", inline=True)
comment(0x84B4, "Check if source matches controller", inline=True)
comment(0x84B6, "Reject: source != controlling station", inline=True)
comment(0x84B8, "Read keypress from RX data at &82", inline=True)
comment(0x84BA, "Load character byte", inline=True)
comment(0x84BC, "Y = character to insert", inline=True)
comment(0x84BD, "X = buffer 0 (keyboard input)", inline=True)
comment(0x84BF, "Release JSR protection before inserting key", inline=True)
comment(0x84C2, "OSBYTE &99: insert char into input buffer", inline=True)
comment(0x84C4, "Tail call: insert character Y into buffer X", inline=True)
label(0x84C7, "error_not_listening")     # Error code 8: "Not listening"
comment(0x84C7, "Error code 8: \"Not listening\" error", inline=True)
comment(0x84C9, "ALWAYS branch to set_listen_offset", inline=True)
comment(0x84CB, "Load TX status byte for error lookup", inline=True)
comment(0x84CD, "Mask to 3-bit error code (0-7)", inline=True)
comment(0x84CF, "X = error code index", inline=True)
comment(0x84D0, "Look up error message offset from table", inline=True)
comment(0x84D3, "X=0: start writing at &0101", inline=True)
comment(0x84D5, "Store BRK opcode at &0100", inline=True)
label(0x84D8, "copy_error_message")     # Copy Econet error message string into BRK block
comment(0x84D8, "Load error message byte", inline=True)
comment(0x84DB, "Build error message at &0101+", inline=True)
comment(0x84DE, "Zero byte = end of message; go execute BRK", inline=True)
comment(0x84E2, "Continue copying message", inline=True)
comment(0x84ED, "Save function code on stack", inline=True)
comment(0x84EE, "Load current rx_flags", inline=True)
comment(0x84F1, "Save rx_flags on stack for restore", inline=True)
comment(0x84F2, "Set bit7: FS transaction in progress", inline=True)
comment(0x84F4, "Write back updated rx_flags", inline=True)
label(0x84F7, "skip_rx_flag_set")       # BNE: non-zero TX hi byte, skip bit-7 set
comment(0x84F7, "Push two zero bytes as timeout counters", inline=True)
comment(0x84F9, "First zero for timeout", inline=True)
comment(0x84FA, "Second zero for timeout", inline=True)
comment(0x84FB, "Y=0: index for flag byte check", inline=True)
comment(0x84FC, "TSX: index stack-based timeout via X", inline=True)
comment(0x8500, "Read flag byte from TX control block", inline=True)
comment(0x8502, "Bit 7 set = reply received", inline=True)
comment(0x8504, "Three-stage nested timeout: inner loop", inline=True)
comment(0x8507, "Inner not expired: keep polling", inline=True)
comment(0x8509, "Middle timeout loop", inline=True)
comment(0x850C, "Middle not expired: keep polling", inline=True)
comment(0x850E, "Outer timeout loop (slowest)", inline=True)
comment(0x8511, "Outer not expired: keep polling", inline=True)
comment(0x8513, "Pop first timeout byte", inline=True)
comment(0x8514, "Pop second timeout byte", inline=True)
comment(0x8515, "Pop saved rx_flags into A", inline=True)
comment(0x8516, "Restore saved rx_flags from stack", inline=True)
comment(0x8519, "Pop saved function code", inline=True)
comment(0x851A, "A=saved func code; zero would mean no reply", inline=True)
comment(0x851C, "Return to caller", inline=True)
comment(0x852E, "C=1: flag for BGET mode", inline=True)
comment(0x852F, "Handle BGET via FS command", inline=True)
comment(0x8532, "SEC: set carry for error check", inline=True)
comment(0x8533, "A=&FE: mask for EOF check", inline=True)
comment(0x8535, "BIT l0fdf: test error flags", inline=True)
comment(0x8538, "V=1: error, return early", inline=True)
comment(0x853A, "CLC: no error", inline=True)
label(0x8546, "bgetv_shared_jsr")      # Embedded JSR opcode: code-sharing with error table
comment(0x85B1, "Y=&0E: attribute byte offset in param block", inline=True)
comment(0x85B3, "Load FS attribute byte", inline=True)
comment(0x85B5, "Mask to 6 bits (FS → BBC direction)", inline=True)
comment(0x85B7, "X=4: skip first 4 table entries (BBC→FS half)", inline=True)
comment(0x85B9, "ALWAYS branch to shared bitmask builder", inline=True)
comment(0x85BB, "Mask to 5 bits (BBC → FS direction)", inline=True)
comment(0x85BD, "X=&FF: INX makes 0; start from table index 0", inline=True)
label(0x85BF, "attrib_shift_bits")      # Attribute bitmask conversion (shared tail)
comment(0x85BF, "Temp storage for source bitmask to shift out", inline=True)
comment(0x85C1, "A=0: accumulate destination bits here", inline=True)
label(0x85C3, "map_attrib_bits")         # Map source attribute bits via access_bit_table lookup
comment(0x85C3, "Next table entry", inline=True)
comment(0x85C4, "Shift out source bits one at a time", inline=True)
comment(0x85C6, "Bit was 0: skip this destination bit", inline=True)
comment(0x85C8, "OR in destination bit from lookup table", inline=True)
label(0x85CB, "skip_set_attrib_bit")   # BCC: source bit was 0, don't OR destination
comment(0x85CB, "Loop while source bits remain (A != 0)", inline=True)
comment(0x85CD, "Return; A = converted attribute bitmask", inline=True)
label(0x85E1, "print_inline_char")     # Print inline string bytes via OSASCI until bit-7 terminator
label(0x85E7, "print_next_char")      # INC lo-byte of pointer, load and print next char
label(0x8617, "no_dot_exit")          # BCC: char < '.', CLC then RTS (no dot found)
label(0x8618, "parse_decimal_rts")    # BEQ: char = '.', LDA result/RTS
comment(0x861B, "Handle number to Y for conversion", inline=True)
comment(0x861C, "Force unconditional conversion", inline=True)
label(0x8634, "handle_mask_exit")     # BEQ/BNE: PLA/TAX/PLA/RTS exit restoring X and A
comment(0x8640, "Compare 4 bytes (index 4,3,2,1)", inline=True)
label(0x8642, "compare_addr_byte")     # EOR bytes of two 4-byte addresses checking for mismatch
comment(0x8642, "Load byte from first address", inline=True)
comment(0x8644, "XOR with corresponding byte", inline=True)
comment(0x8646, "Mismatch: Z=0, return unequal", inline=True)
comment(0x8649, "Continue comparing", inline=True)
comment(0x864C, "X=first handle (&20)", inline=True)
comment(0x864E, "Y=last handle (&27)", inline=True)
comment(0x865C, "Write back updated flags", inline=True)
comment(0x865F, "Return", inline=True)
comment(0x86B0, "Y=1: copy 2 bytes (high then low)", inline=True)
comment(0x86B2, "Load filename ptr from control block", inline=True)
comment(0x86B4, "Store to MOS text pointer (&F2/&F3)", inline=True)
comment(0x86B7, "Next byte (descending)", inline=True)
comment(0x86B8, "Loop for both bytes", inline=True)
comment(0x86BA, "Start from beginning of string", inline=True)
comment(0x86BC, "X=&FF: INX will make X=0 (first char index)", inline=True)
comment(0x86BE, "C=0 for GSINIT: parse from current position", inline=True)
comment(0x86BF, "Initialise GS string parser", inline=True)
comment(0x86C2, "Empty string: skip to CR terminator", inline=True)
comment(0x86C4, "Read next character via GSREAD", inline=True)
comment(0x86C7, "C=1 from GSREAD: end of string reached", inline=True)
comment(0x86C9, "Advance buffer index", inline=True)
comment(0x86CA, "Store parsed character to &0E30+X", inline=True)
comment(0x86CD, "ALWAYS loop (GSREAD clears C on success)", inline=True)
label(0x86CF, "terminate_filename")   # BEQ/BCS: empty or end-of-GSREAD, append CR
comment(0x86CF, "Terminate parsed string with CR", inline=True)
comment(0x86D0, "CR = &0D", inline=True)
comment(0x86D2, "Store CR terminator at end of string", inline=True)
comment(0x86D5, "Point fs_crc_lo/hi at &0E30 parse buffer", inline=True)
comment(0x86D7, "fs_crc_lo = &30", inline=True)
comment(0x86D9, "fs_crc_hi = &0E → buffer at &0E30", inline=True)
comment(0x86DB, "Store high byte", inline=True)
comment(0x86DD, "Return; X = string length", inline=True)
comment(0x86E1, "Copy filename ptr from param block to os_text_ptr", inline=True)
comment(0x86E4, "Recover function code from saved A", inline=True)
comment(0x86E6, "A >= 0: save (&00) or attribs (&01-&06)", inline=True)
comment(0x86E8, "A=&FF? Only &FF is valid for load", inline=True)
comment(0x86EC, "Unknown negative code: no-op return", inline=True)
comment(0x86F4, "Port &92 = PLDATA (data transfer port)", inline=True)
comment(0x86F6, "Overwrite URD field with data port number", inline=True)
comment(0x86FB, "Build FS header (V=1: CLV path)", inline=True)
comment(0x86FE, "Y=6: param block byte 6", inline=True)
comment(0x8700, "Byte 6: use file's own load address?", inline=True)
comment(0x8702, "Non-zero: use FS reply address (lodfil)", inline=True)
comment(0x8704, "Zero: copy caller's load addr first", inline=True)
comment(0x8707, "Then copy FS reply to param block", inline=True)
comment(0x870A, "Carry clear from prepare_cmd_clv: skip lodfil", inline=True)
comment(0x870C, "Copy FS reply addresses to param block", inline=True)
comment(0x870F, "Then copy load addr from param block", inline=True)
label(0x8712, "skip_lodfil")           # BCC: skip lodfil block, proceed to compute end addr
comment(0x8712, "Compute end address = load + file length", inline=True)
label(0x8714, "copy_load_end_addr")    # Copy 4 load-address bytes and compute end address
comment(0x8714, "Load address byte", inline=True)
comment(0x8716, "Store as current transfer position", inline=True)
comment(0x8718, "Add file length byte", inline=True)
comment(0x871B, "Store as end position", inline=True)
comment(0x871D, "Next address byte", inline=True)
comment(0x871E, "Decrement byte counter", inline=True)
comment(0x871F, "Loop for all 4 address bytes", inline=True)
comment(0x8721, "Adjust high byte for 3-byte length overflow", inline=True)
comment(0x8722, "Subtract 4th length byte from end addr", inline=True)
comment(0x8725, "Store adjusted end address high byte", inline=True)
comment(0x872A, "Transfer file data in &80-byte blocks", inline=True)
comment(0x872D, "Copy 3-byte file length to FS reply cmd buffer", inline=True)
comment(0x872F, "Load file length byte", inline=True)
comment(0x8732, "Store in FS command data buffer", inline=True)
comment(0x8735, "Next byte (count down)", inline=True)
comment(0x8736, "Loop for 3 bytes (X=2,1,0)", inline=True)
comment(0x8738, "ALWAYS branch", inline=True)
comment(0x873D, "Addresses match: transfer complete", inline=True)
comment(0x873F, "Port &92 for data block transfer", inline=True)
comment(0x8741, "Store port to TXCB command byte", inline=True)
label(0x8743, "send_block_loop")       # Outer loop: set up and send each 128-byte block
comment(0x8743, "Set up next &80-byte block for transfer", inline=True)
label(0x8745, "copy_block_addrs")      # Inner loop: swap 4-byte current/end addresses
comment(0x8745, "Swap: current addr -> source, end -> current", inline=True)
comment(0x8747, "Source addr = current position", inline=True)
comment(0x8749, "Load end address byte", inline=True)
comment(0x874B, "Dest = end address (will be clamped)", inline=True)
comment(0x874D, "Next address byte", inline=True)
comment(0x874E, "Loop for all 4 bytes", inline=True)
comment(0x8750, "Command &7F = data block transfer", inline=True)
comment(0x8752, "Store to TXCB control byte", inline=True)
comment(0x8754, "Send this block to the fileserver", inline=True)
comment(0x8757, "Y=3: compare 4 bytes (3..0)", inline=True)
comment(0x8759, "Compare current vs end address (4 bytes)", inline=True)
comment(0x875C, "XOR with end address byte", inline=True)
comment(0x875F, "Not equal: more blocks to send", inline=True)
comment(0x8761, "Next byte", inline=True)
comment(0x8762, "Loop for all 4 address bytes", inline=True)
comment(0x8764, "All equal: transfer complete", inline=True)
comment(0x8765, "A=0: SAVE handler", inline=True)
comment(0x8767, "A!=0: attribute dispatch (A=1-6)", inline=True)
comment(0x876A, "Process 4 address bytes (load/exec/start/end)", inline=True)
comment(0x876C, "Y=&0E: start from end-address in param block", inline=True)
comment(0x876E, "Read end-address byte from param block", inline=True)
comment(0x8770, "Save to port workspace for transfer setup", inline=True)
comment(0x8773, "Y = Y-4: point to start-address byte", inline=True)
comment(0x8776, "end - start = transfer length byte", inline=True)
comment(0x8778, "Store length byte in FS command buffer", inline=True)
comment(0x877B, "Save length byte for param block restore", inline=True)
comment(0x877C, "Read corresponding start-address byte", inline=True)
comment(0x877E, "Save to port workspace", inline=True)
comment(0x8781, "Restore length byte from stack", inline=True)
comment(0x8782, "Replace param block entry with length", inline=True)
comment(0x8784, "Y = Y+5: advance to next address group", inline=True)
comment(0x8787, "Decrement address byte counter", inline=True)
comment(0x8788, "Loop for all 4 address bytes", inline=True)
comment(0x878A, "Copy load/exec addresses to FS command buffer", inline=True)
label(0x878C, "copy_save_params")      # Copy 9 bytes of load/exec address into FS command buffer
comment(0x878C, "Read load/exec address byte from params", inline=True)
comment(0x878E, "Copy to FS command buffer", inline=True)
comment(0x8791, "Next byte (descending)", inline=True)
comment(0x8792, "Loop for bytes 9..1", inline=True)
comment(0x8794, "Port &91 for save command", inline=True)
comment(0x8796, "Overwrite URD field with port number", inline=True)
comment(0x8799, "Save port &91 for flow control ACK", inline=True)
comment(0x879B, "Append filename at offset &0B in cmd buffer", inline=True)
comment(0x879D, "Append filename to cmd buffer at offset X", inline=True)
comment(0x87A0, "Y=1: function code for save", inline=True)
label(0x87B7, "skip_catalogue_msg")   # BEQ: messages flag=0, skip display
comment(0x87B7, "Store reply command for attr decode", inline=True)
comment(0x87BA, "Y=&0E: access byte offset in param block", inline=True)
comment(0x87BC, "Load access byte from FS reply", inline=True)
comment(0x87BF, "Convert FS access to BBC attribute format", inline=True)
comment(0x87CA, "Copied all 4 bytes? (Y=&0E..&11)", inline=True)
comment(0x87CC, "Loop for 4 attribute bytes", inline=True)
comment(0x87CE, "Restore A/X/Y and return to caller", inline=True)
comment(0x87D1, "Start at offset 5 (top of 4-byte addr)", inline=True)
comment(0x87D3, "Read from parameter block", inline=True)
comment(0x87D5, "Store to local workspace", inline=True)
comment(0x87D8, "Next byte (descending)", inline=True)
comment(0x87D9, "Copy offsets 5,4,3,2 (4 bytes)", inline=True)
comment(0x87DB, "Loop while Y >= 2", inline=True)
comment(0x87DD, "Y=3 after loop; add 5 to get Y=8", inline=True)
comment(0x87DE, "INY * 4 = add 4 to Y", inline=True)
comment(0x87E2, "Return", inline=True)
comment(0x87E3, "Start at offset &0D (top of range)", inline=True)
comment(0x87E5, "First store uses X (attrib byte)", inline=True)
comment(0x87E6, "Write to parameter block", inline=True)
comment(0x87E8, "Read next byte from reply buffer", inline=True)
comment(0x87EC, "Copy offsets &0D down to 2", inline=True)
comment(0x87F0, "Y=1 after loop; sub 4 to get Y=&FD", inline=True)
comment(0x87F5, "Save FS command byte on stack", inline=True)
comment(0x87F9, "Addresses equal: nothing to transfer", inline=True)
comment(0x880D, "Store dest address byte", inline=True)
comment(0x880F, "Advance current position", inline=True)
comment(0x8811, "Next address byte", inline=True)
comment(0x8812, "Decrement byte counter", inline=True)
comment(0x8813, "Loop for all 4 bytes", inline=True)
comment(0x8817, "SEC for SBC in overshoot check", inline=True)
comment(0x8818, "Check if new pos overshot end addr", inline=True)
comment(0x881B, "Subtract end address byte", inline=True)
comment(0x881E, "Next byte", inline=True)
comment(0x881F, "Decrement counter", inline=True)
comment(0x8820, "Loop for 4-byte comparison", inline=True)
comment(0x8822, "C=0: no overshoot, proceed", inline=True)
comment(0x8824, "Overshot: clamp dest to end address", inline=True)
label(0x8826, "clamp_dest_addr")       # Clamp dest addr when block overshoots transfer end
comment(0x8826, "Load end address byte", inline=True)
comment(0x8828, "Replace dest with end address", inline=True)
comment(0x882A, "Next byte", inline=True)
comment(0x882B, "Loop for all 4 bytes", inline=True)
label(0x882D, "send_block")           # BCC: no overshoot, skip clamp, send block
comment(0x882D, "Recover original FS command byte", inline=True)
comment(0x882E, "Re-push for next iteration", inline=True)
comment(0x882F, "Save processor flags (C from cmp)", inline=True)
comment(0x8830, "Store command byte in TXCB", inline=True)
comment(0x8832, "128-byte block size for data transfer", inline=True)
comment(0x8834, "Store size in TXCB control byte", inline=True)
comment(0x8836, "Point TX ptr to &00C0; transmit", inline=True)
comment(0x8839, "ACK port for flow control", inline=True)
comment(0x883B, "Set reply port for ACK receive", inline=True)
comment(0x883E, "Restore flags (C=overshoot status)", inline=True)
comment(0x883F, "C=1: all data sent (overshot), done", inline=True)
comment(0x8841, "Command &91 = data block transfer", inline=True)
comment(0x8843, "Store command &91 in TXCB", inline=True)
comment(0x8847, "Transmit block and wait (BRIANX)", inline=True)
comment(0x884A, "More blocks? Loop back", inline=True)
comment(0x884C, "Save A (function code)", inline=True)
comment(0x884D, "X = file handle to check", inline=True)
comment(0x884E, "Convert handle to bitmask in A", inline=True)
comment(0x8851, "Y = handle bitmask from conversion", inline=True)
comment(0x8852, "Local hint: is EOF possible for this handle?", inline=True)
comment(0x8855, "X = result of AND (0 = not at EOF)", inline=True)
comment(0x8856, "Hint clear: definitely not at EOF", inline=True)
comment(0x8858, "Save bitmask for clear_fs_flag", inline=True)
comment(0x8859, "Handle byte in FS command buffer", inline=True)
comment(0x885C, "Y=&11: FS function code FCEOF", inline=True)
comment(0x8863, "Restore bitmask", inline=True)
comment(0x8864, "FS reply: non-zero = at EOF", inline=True)
comment(0x8867, "At EOF: skip flag clear", inline=True)
comment(0x8869, "Not at EOF: clear the hint bit", inline=True)
label(0x886C, "restore_ay_return")      # Restore A and Y registers, return
comment(0x886C, "Restore A", inline=True)
comment(0x886D, "Restore Y", inline=True)
comment(0x886F, "Return; X=0 (not EOF) or X=&FF (EOF)", inline=True)
comment(0x8870, "Store function code in FS cmd buffer", inline=True)
comment(0x8873, "A=6? (delete)", inline=True)
comment(0x8875, "Yes: jump to delete handler", inline=True)
comment(0x8877, "A>=7: unsupported, fall through to return", inline=True)
comment(0x8879, "A=5? (read catalogue info)", inline=True)
comment(0x887B, "Yes: jump to read info handler", inline=True)
comment(0x887D, "A=4? (write attributes only)", inline=True)
comment(0x887F, "Yes: jump to write attrs handler", inline=True)
comment(0x8881, "A=1? (write all catalogue info)", inline=True)
comment(0x8883, "Yes: jump to write-all handler", inline=True)
comment(0x8885, "A=2 or 3: convert to param block offset", inline=True)
comment(0x8886, "A*4: 2->8, 3->12", inline=True)
comment(0x8887, "Y = A*4", inline=True)
comment(0x8888, "Y = A*4 - 3 (load addr offset for A=2)", inline=True)
comment(0x888B, "X=3: copy 4 bytes", inline=True)
comment(0x888D, "Load address byte from param block", inline=True)
comment(0x888F, "Store to FS cmd data area", inline=True)
comment(0x8892, "Next source byte (descending)", inline=True)
comment(0x8893, "Next dest byte", inline=True)
comment(0x8894, "Loop for 4 bytes", inline=True)
comment(0x8896, "X=5: data extent for filename copy", inline=True)
comment(0x889A, "A=1: encode protection from param block", inline=True)
comment(0x889D, "Store encoded attrs at &0F0E", inline=True)
comment(0x88A0, "Y=9: source offset in param block", inline=True)
comment(0x88A2, "X=8: dest offset in cmd buffer", inline=True)
comment(0x88A4, "Load byte from param block", inline=True)
comment(0x88A6, "Store to FS cmd buffer", inline=True)
comment(0x88A9, "Next source byte (descending)", inline=True)
comment(0x88AA, "Next dest byte", inline=True)
comment(0x88AB, "Loop until X=0 (8 bytes copied)", inline=True)
comment(0x88AD, "X=&0A: data extent past attrs+addrs", inline=True)
comment(0x88AF, "Append filename to cmd buffer", inline=True)
comment(0x88B2, "Y=&13: fn code for FCSAVE (write attrs)", inline=True)
comment(0x88B4, "ALWAYS branch to send command", inline=True)
comment(0x88B6, "A=6: copy filename (delete)", inline=True)
comment(0x88B9, "Y=&14: fn code for FCDEL (delete)", inline=True)
label(0x88BB, "send_fs_cmd_v1")       # BNE: after copy_filename, BIT tx_ctrl_upper
comment(0x88BB, "Set V=1 (BIT trick: &B3 has bit 6 set)", inline=True)
comment(0x88BE, "Send via prepare_fs_cmd_v (V=1 path)", inline=True)
label(0x88C1, "check_attrib_result")  # BCS: A>=7 unsupported, dispatch to error/return
comment(0x88C1, "C=1: &D6 not-found, skip to return", inline=True)
comment(0x88C3, "C=0: success, copy reply to param block", inline=True)
comment(0x88C5, "A=4: encode attrs from param block", inline=True)
comment(0x88C8, "Store encoded attrs at &0F06", inline=True)
comment(0x88CB, "X=2: data extent (1 attr byte + fn)", inline=True)
comment(0x88CD, "ALWAYS branch to append filename", inline=True)
comment(0x88CF, "A=5: X=1 (filename only, no data)", inline=True)
comment(0x88D1, "Copy filename to cmd buffer", inline=True)
comment(0x88D4, "Y=&12: fn code for FCEXAM (read info)", inline=True)
comment(0x88D9, "Save object type from FS reply", inline=True)
comment(0x88DC, "Clear reply byte (X=0 on success)", inline=True)
comment(0x88DF, "Clear length high byte in reply", inline=True)
comment(0x88E2, "Decode 5-bit access byte from FS reply", inline=True)
comment(0x88E5, "Y=&0E: attrs offset in param block", inline=True)
comment(0x88E7, "Store decoded attrs at param block +&0E", inline=True)
comment(0x88E9, "Y=&0D: start copy below attrs", inline=True)
comment(0x88EA, "X=&0C: copy from reply offset &0C down", inline=True)
comment(0x88EC, "Load reply byte (load/exec/length)", inline=True)
comment(0x88EF, "Store to param block", inline=True)
comment(0x88F1, "Next dest byte (descending)", inline=True)
comment(0x88F2, "Next source byte", inline=True)
comment(0x88F3, "Loop until X=0 (12 bytes copied)", inline=True)
comment(0x88F5, "X=0 -> X=2 for length high copy", inline=True)
comment(0x88F6, "INX again: X=2", inline=True)
comment(0x88F7, "Y=&11: length high dest in param block", inline=True)
comment(0x88F9, "Load length high byte from reply", inline=True)
comment(0x88FC, "Store to param block", inline=True)
comment(0x88FE, "Next dest byte (descending)", inline=True)
comment(0x88FF, "Next source byte", inline=True)
comment(0x8900, "Loop for 3 length-high bytes", inline=True)
comment(0x8902, "Return object type in A", inline=True)
label(0x8905, "attrib_error_exit")    # BCS: not-found/error, BPL restore_xy_return
comment(0x8905, "A>=0: branch to restore_args_return", inline=True)
comment(0x8907, "Save A/X/Y registers for later restore", inline=True)
comment(0x890A, "Function >= 3?", inline=True)
comment(0x890C, "A>=3 (ensure/flush): no-op for NFS", inline=True)
comment(0x890E, "Test file handle", inline=True)
comment(0x8910, "Y=0: FS-level query, not per-file", inline=True)
comment(0x8912, "Convert handle to bitmask", inline=True)
comment(0x8915, "Store bitmask as first cmd data byte", inline=True)
comment(0x8918, "LSR splits A: C=1 means write (A=1)", inline=True)
comment(0x8919, "Store function code to cmd data byte 2", inline=True)
comment(0x891C, "C=1: write path, copy ptr from caller", inline=True)
comment(0x891E, "Y=&0C: FCRDSE (read sequential pointer)", inline=True)
comment(0x8920, "X=2: 3 data bytes in command", inline=True)
comment(0x8922, "Build and send FS command", inline=True)
comment(0x8925, "Clear last-byte flag on success", inline=True)
comment(0x8927, "X = saved control block ptr low", inline=True)
comment(0x8929, "Y=2: copy 3 bytes of file pointer", inline=True)
comment(0x892B, "Zero high byte of 3-byte pointer", inline=True)
label(0x892D, "copy_fileptr_reply")    # Copy 3-byte file pointer from FS reply data
comment(0x892D, "Read reply byte from FS cmd data", inline=True)
comment(0x8930, "Store to caller's control block", inline=True)
comment(0x8932, "Next byte (descending)", inline=True)
comment(0x8933, "Next source byte", inline=True)
comment(0x8934, "Loop for all 3 bytes", inline=True)
label(0x8936, "argsv_check_return")    # Conditional return after ARGSV file pointer op
comment(0x8936, "C=0 (read): return to caller", inline=True)
comment(0x8938, "Save bitmask for set_fs_flag later", inline=True)
comment(0x8939, "Push bitmask", inline=True)
comment(0x893A, "Y=3: copy 4 bytes of file pointer", inline=True)
label(0x893C, "copy_fileptr_to_cmd")  # Copy 4-byte file pointer into FS command area
comment(0x893C, "Read caller's pointer byte", inline=True)
comment(0x893E, "Store to FS command data area", inline=True)
comment(0x8941, "Next source byte", inline=True)
comment(0x8942, "Next destination byte", inline=True)
comment(0x8943, "Loop for all 4 bytes", inline=True)
comment(0x8945, "Y=&0D: FCWRSE (write sequential pointer)", inline=True)
comment(0x8947, "X=5: 6 data bytes in command", inline=True)
comment(0x8949, "Build and send FS command", inline=True)
comment(0x894C, "Save not-found status from X", inline=True)
comment(0x894E, "Recover bitmask for EOF hint update", inline=True)
comment(0x894F, "Set EOF hint bit for this handle", inline=True)
comment(0x8952, "A = saved function code / command", inline=True)
label(0x8954, "restore_xy_return")     # Restore X and Y from workspace, return
comment(0x8954, "X = saved control block ptr low", inline=True)
comment(0x8956, "Y = saved control block ptr high", inline=True)
comment(0x8958, "Return to MOS with registers restored", inline=True)
label(0x8960, "halve_args_a")         # BEQ: A=2, LSR A then dispatch
comment(0x8960, "Shared: halve A (A=0 or A=2 paths)", inline=True)
comment(0x8960, "Shared: A=0->&05, A=2->&01", inline=True)
comment(0x8961, "Return with A = FS number or 1", inline=True)
comment(0x8963, "Read FS command context byte", inline=True)
comment(0x8963, "Copy command context to caller's block", inline=True)
comment(0x8966, "Store to caller's parameter block", inline=True)
comment(0x8968, "Next byte (descending)", inline=True)
comment(0x8969, "Loop until all bytes copied", inline=True)
comment(0x896F, "Save A/X/Y and set up pointers", inline=True)
comment(0x8972, "SEC distinguishes open (A>0) from close", inline=True)
comment(0x8977, "A=0: close file(s)", inline=True)
comment(0x8979, "Valid open modes: &40, &80, &C0 only", inline=True)
comment(0x897B, "Invalid mode bits: return", inline=True)
comment(0x897D, "A = original mode byte", inline=True)
comment(0x897E, "Convert MOS mode to FS protocol flags", inline=True)
comment(0x8980, "ASL: shift mode bits left", inline=True)
comment(0x8981, "Flag 1: read/write direction", inline=True)
comment(0x8984, "ROL: Flag 2 into bit 0", inline=True)
comment(0x8985, "Flag 2: create vs existing file", inline=True)
comment(0x8988, "Parse filename from command line", inline=True)
comment(0x898B, "X=2: copy after 2-byte flags", inline=True)
comment(0x898D, "Copy filename to FS command buffer", inline=True)
comment(0x8990, "Y=6: FS function code FCOPEN", inline=True)
comment(0x8992, "Set V flag from l83b3 bit 6", inline=True)
comment(0x8995, "Build and send FS open command", inline=True)
comment(0x8998, "Error: restore and return", inline=True)
comment(0x899A, "Load reply handle from FS", inline=True)
comment(0x899D, "X = new file handle", inline=True)
comment(0x899E, "Set EOF hint + sequence bits", inline=True)
comment(0x89AC, "ALWAYS branch to restore and return", inline=True)
comment(0x89AE, "A = handle (Y preserved in A)", inline=True)
comment(0x89AF, "Y>0: close single file", inline=True)
comment(0x89B1, "Close SPOOL/EXEC before FS close-all", inline=True)
comment(0x89B6, "Y=0: close all handles on server", inline=True)
comment(0x89B8, "Handle byte in FS command buffer", inline=True)
comment(0x89C2, "Reply handle for flag update", inline=True)
comment(0x89C5, "Update EOF/sequence tracking bits", inline=True)
label(0x89C8, "close_opt_return")      # Conditional return after close/opt handler
comment(0x89C8, "C=0: restore A/X/Y and return", inline=True)
comment(0x89CA, "Is it *OPT 4,Y?", inline=True)
comment(0x89CC, "No: check for *OPT 1", inline=True)
comment(0x89CE, "Y must be 0-3 for boot option", inline=True)
comment(0x89D0, "Y < 4: valid boot option", inline=True)
label(0x89D2, "check_opt1")           # BNE: X!=4, DEX/BNE to check for *OPT 1
comment(0x89D2, "Not *OPT 4: check for *OPT 1", inline=True)
comment(0x89D3, "Not *OPT 1 either: bad option", inline=True)
label(0x89D5, "set_messages_flag")     # Set *OPT 1 local messages flag from Y
comment(0x89D5, "Set local messages flag (*OPT 1,Y)", inline=True)
comment(0x89D8, "Return via restore_args_return", inline=True)
comment(0x89DA, "Error index 7 (Bad option)", inline=True)
comment(0x89DC, "Generate BRK error", inline=True)
comment(0x89DF, "Boot option value in FS command", inline=True)
comment(0x89E2, "Y=&16: FS function code FCOPT", inline=True)
comment(0x89E7, "Restore Y from saved value", inline=True)
comment(0x89E9, "Cache boot option locally", inline=True)
label(0x89EC, "opt_return")           # BCC: *OPT 1 done, to close_opt_return
comment(0x89EC, "Return via restore_args_return", inline=True)
comment(0x89EE, "Y=9: adjust 9 address bytes", inline=True)
comment(0x89F0, "Adjust with carry clear", inline=True)
comment(0x89F3, "Y=1: adjust 1 address byte", inline=True)
comment(0x89F5, "C=0 for address adjustment", inline=True)
label(0x89F8, "adjust_addr_byte")      # Add or subtract one adjustment byte per iteration (4 total)
label(0x8A04, "subtract_adjust")      # BMI: fs_load_addr_2 negative, SBC instead of ADC
comment(0x8A0E, "Save A/X/Y to FS workspace", inline=True)
comment(0x8A11, "X = call number for range check", inline=True)
comment(0x8A12, "A=0: invalid, restore and return", inline=True)
comment(0x8A14, "Convert to 0-based (A=0..7)", inline=True)
comment(0x8A15, "Range check: must be 0-7", inline=True)
comment(0x8A17, "In range: continue to handler", inline=True)
label(0x8A19, "gbpb_invalid_exit")    # BEQ/fall: A=0 or X>=8 out of range, JMP restore_args
comment(0x8A19, "Out of range: restore args and return", inline=True)
comment(0x8A1C, "Recover 0-based function code", inline=True)
comment(0x8A1D, "Y=0: param block byte 0 (file handle)", inline=True)
comment(0x8A1F, "Save function code on stack", inline=True)
comment(0x8A20, "A>=4: info queries, dispatch separately", inline=True)
comment(0x8A22, "A<4: file read/write operations", inline=True)
comment(0x8A24, "Dispatch to OSGBPB 5-8 info handler", inline=True)
comment(0x8A27, "Get file handle from param block byte 0", inline=True)
comment(0x8A29, "Convert handle to bitmask for EOF flags", inline=True)
comment(0x8A2C, "Store handle in FS command data", inline=True)
comment(0x8A2F, "Y=&0B: start at param block byte 11", inline=True)
comment(0x8A31, "X=6: copy 6 bytes of transfer params", inline=True)
comment(0x8A33, "Load param block byte", inline=True)
comment(0x8A35, "Store to FS command buffer at &0F06+X", inline=True)
comment(0x8A38, "Previous param block byte", inline=True)
comment(0x8A39, "Skip param block offset 8 (the handle)", inline=True)
comment(0x8A3B, "Not at handle offset: continue", inline=True)
comment(0x8A3D, "Extra DEY to skip handle byte", inline=True)
comment(0x8A3E, "Decrement copy counter", inline=True)
comment(0x8A3F, "Loop for all 6 bytes", inline=True)
comment(0x8A41, "Recover function code from stack", inline=True)
comment(0x8A42, "LSR: odd=read (C=1), even=write (C=0)", inline=True)
comment(0x8A43, "Save function code again (need C later)", inline=True)
comment(0x8A44, "Even (write): X stays 0", inline=True)
comment(0x8A46, "Odd (read): X=1", inline=True)
comment(0x8A47, "Store FS direction flag", inline=True)
comment(0x8A4A, "Y=&0B: command data extent", inline=True)
comment(0x8A4C, "Command &91=put, &92=get", inline=True)
comment(0x8A4E, "Recover function code", inline=True)
comment(0x8A4F, "Save again for later direction check", inline=True)
comment(0x8A50, "Even (write): keep &91 and Y=&0B", inline=True)
comment(0x8A52, "Odd (read): use &92 (get) instead", inline=True)
comment(0x8A54, "Read: one fewer data byte in command", inline=True)
label(0x8A55, "gbpb_write_path")      # BEQ: A=0 write, keeps X=&91/Y=&0B
comment(0x8A55, "Store port to FS command URD field", inline=True)
comment(0x8A58, "Save port for error recovery", inline=True)
comment(0x8A5A, "X=8: command data bytes", inline=True)
comment(0x8A5C, "Load handle from FS command data", inline=True)
comment(0x8A5F, "Build FS command with handle+flag", inline=True)
comment(0x8A62, "Save seq# for byte-stream flow control", inline=True)
comment(0x8A64, "Store to FS sequence number workspace", inline=True)
comment(0x8A67, "X=4: copy 4 address bytes", inline=True)
comment(0x8A69, "Set up source/dest from param block", inline=True)
comment(0x8A6B, "Store as source address", inline=True)
comment(0x8A6E, "Store as current transfer position", inline=True)
comment(0x8A71, "Skip 4 bytes to reach transfer length", inline=True)
comment(0x8A74, "Dest = source + length", inline=True)
comment(0x8A76, "Store as end address", inline=True)
comment(0x8A79, "Back 3 to align for next iteration", inline=True)
comment(0x8A7C, "Decrement byte counter", inline=True)
comment(0x8A7D, "Loop for all 4 address bytes", inline=True)
comment(0x8A7F, "X=1 after loop", inline=True)
comment(0x8A80, "Copy CSD data to command buffer", inline=True)
comment(0x8A83, "Store at &0F06+X", inline=True)
comment(0x8A86, "Decrement counter", inline=True)
comment(0x8A87, "Loop for X=1,0", inline=True)
comment(0x8A89, "Odd (read): send data to FS first", inline=True)
comment(0x8A8A, "Non-zero: skip write path", inline=True)
comment(0x8A8C, "Load port for transfer setup", inline=True)
comment(0x8A8F, "Transfer data blocks to fileserver", inline=True)
label(0x8A9B, "wait_fs_reply")        # BCS/fall: post-transfer, JSR send_fs_reply_cmd
comment(0x8A9B, "Wait for FS reply command", inline=True)
comment(0x8A9E, "Load handle mask for EOF flag update", inline=True)
comment(0x8AA0, "Check FS reply: bit 7 = not at EOF", inline=True)
comment(0x8AA3, "Bit 7 set: not EOF, skip clear", inline=True)
comment(0x8AA5, "At EOF: clear EOF hint for this handle", inline=True)
label(0x8AA8, "skip_clear_flag")      # BMI: reply bit 7 set (not EOF), skip clear_fs_flag
comment(0x8AA8, "Set EOF hint flag (may be at EOF)", inline=True)
comment(0x8AAB, "Direction=0: forward adjustment", inline=True)
comment(0x8AAD, "Adjust param block addrs by +9 bytes", inline=True)
comment(0x8AB0, "Direction=&FF: reverse adjustment", inline=True)
comment(0x8AB2, "SEC for reverse subtraction", inline=True)
comment(0x8AB3, "Adjust param block addrs (reverse)", inline=True)
comment(0x8AB6, "Shift bit 7 into C for return flag", inline=True)
comment(0x8AB9, "Return via restore_args path", inline=True)
label(0x8ABC, "get_disc_title")        # Request disc title via FS function code &15
comment(0x8ABC, "Y=&15: function code for disc title", inline=True)
comment(0x8ABE, "Build and send FS command", inline=True)
comment(0x8AC1, "Load boot option from FS workspace", inline=True)
comment(0x8AC4, "Store boot option in reply area", inline=True)
comment(0x8AC7, "X=0: reply data start offset", inline=True)
comment(0x8AC9, "Clear reply buffer high byte", inline=True)
comment(0x8ACB, "A=&12: 18 bytes of reply data", inline=True)
comment(0x8ACD, "Store as byte count for copy", inline=True)
comment(0x8ACF, "ALWAYS branch to copy_reply_to_caller", inline=True)
comment(0x8AD1, "Y=4: check param block byte 4", inline=True)
comment(0x8AD3, "Check if destination is in Tube space", inline=True)
comment(0x8AD6, "No Tube: skip Tube address check", inline=True)
comment(0x8AD8, "Compare Tube flag with addr byte 4", inline=True)
comment(0x8ADA, "Mismatch: not Tube space", inline=True)
comment(0x8ADD, "Y=3: subtract addr byte 3 from flag", inline=True)
label(0x8ADF, "store_tube_flag")      # BEQ/BNE: store Tube-transfer flag to l00a9
comment(0x8ADF, "Non-zero = Tube transfer required", inline=True)
comment(0x8AE1, "Copy param block bytes 1-4 to workspace", inline=True)
comment(0x8AE3, "Store to &BD+Y workspace area", inline=True)
comment(0x8AE6, "Previous byte", inline=True)
comment(0x8AE7, "Loop for bytes 3,2,1", inline=True)
comment(0x8AE9, "Sub-function: AND #3 of (original A - 4)", inline=True)
comment(0x8AEA, "Mask to 0-3 (OSGBPB 5-8 → 0-3)", inline=True)
comment(0x8AEC, "A=0 (OSGBPB 5): read disc title", inline=True)
comment(0x8AEE, "LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)", inline=True)
comment(0x8AEF, "A=0 (OSGBPB 6): read CSD/LIB name", inline=True)
comment(0x8AF1, "C=1 (OSGBPB 8): read filenames from dir", inline=True)
label(0x8AF3, "gbpb6_read_name")      # BEQ: A=0 OSGBPB 6, load CSD/LIB/URD handle
comment(0x8AF3, "Y=0 for CSD or carry for fn code select", inline=True)
comment(0x8AF4, "Get CSD/LIB/URD handles for FS command", inline=True)
comment(0x8AF7, "Store CSD handle in command buffer", inline=True)
comment(0x8AFA, "Load LIB handle from workspace", inline=True)
comment(0x8AFD, "Store LIB handle in command buffer", inline=True)
comment(0x8B00, "Load URD handle from workspace", inline=True)
comment(0x8B03, "Store URD handle in command buffer", inline=True)
comment(0x8B06, "X=&12: buffer extent for command data", inline=True)
comment(0x8B08, "Store X as function code in header", inline=True)
comment(0x8B0B, "&0D = 13 bytes of reply data expected", inline=True)
comment(0x8B0D, "Store reply length in command buffer", inline=True)
comment(0x8B10, "Store as byte count for copy loop", inline=True)
comment(0x8B12, "LSR: &0D >> 1 = 6", inline=True)
comment(0x8B13, "Store as command data byte", inline=True)
comment(0x8B16, "CLC for standard FS path", inline=True)
comment(0x8B1C, "INX: X=1 after build_send_fs_cmd", inline=True)
comment(0x8B1D, "Store X as reply start offset", inline=True)
comment(0x8B1F, "Copy FS reply to caller's buffer", inline=True)
comment(0x8B21, "Non-zero: use Tube transfer path", inline=True)
comment(0x8B23, "X = reply start offset", inline=True)
comment(0x8B25, "Y = reply buffer high byte", inline=True)
label(0x8B27, "copy_reply_bytes")     # Copy N bytes of FS reply data to caller buffer
comment(0x8B27, "Load reply data byte", inline=True)
comment(0x8B2A, "Store to caller's buffer", inline=True)
comment(0x8B2C, "Next source byte", inline=True)
comment(0x8B2D, "Next destination byte", inline=True)
comment(0x8B2E, "Decrement remaining bytes", inline=True)
comment(0x8B30, "Loop until all bytes copied", inline=True)
comment(0x8B32, "ALWAYS branch to exit", inline=True)
label(0x8B34, "tube_transfer")        # BNE: l00a9 non-zero, claim Tube and send via R3
comment(0x8B34, "Claim Tube transfer channel", inline=True)
comment(0x8B37, "A=1: Tube claim type 1 (write)", inline=True)
comment(0x8B39, "X = param block address low", inline=True)
comment(0x8B3B, "Y = param block address high", inline=True)
comment(0x8B3D, "INX: advance past byte 0", inline=True)
comment(0x8B3E, "No page wrap: keep Y", inline=True)
comment(0x8B40, "Page wrap: increment high byte", inline=True)
label(0x8B41, "no_page_wrap")         # BNE: no page boundary crossed in copy
comment(0x8B41, "Claim Tube address for transfer", inline=True)
comment(0x8B44, "X = reply data start offset", inline=True)
comment(0x8B46, "Load reply data byte", inline=True)
comment(0x8B49, "Send byte to Tube via R3", inline=True)
comment(0x8B4C, "Next source byte", inline=True)
comment(0x8B4D, "Decrement remaining bytes", inline=True)
comment(0x8B4F, "Loop until all bytes sent to Tube", inline=True)
comment(0x8B51, "Release Tube after transfer complete", inline=True)
comment(0x8B53, "Release Tube address claim", inline=True)
label(0x8B56, "gbpb_done")            # BEQ: copy/adjust done, JMP return_a_zero
comment(0x8B56, "Return via restore_args path", inline=True)
label(0x8B59, "gbpb8_read_dir")       # BCS: C=1 OSGBPB 8, read dir entries
comment(0x8B59, "OSGBPB 8: read filenames from dir", inline=True)
comment(0x8B5B, "Byte 9: number of entries to read", inline=True)
comment(0x8B5D, "Store as reply count in command buffer", inline=True)
comment(0x8B60, "Y=5: byte 5 = starting entry number", inline=True)
comment(0x8B62, "Load starting entry number", inline=True)
comment(0x8B64, "Store in command buffer", inline=True)
comment(0x8B67, "X=&0D: command data extent", inline=True)
comment(0x8B69, "Store extent in command buffer", inline=True)
comment(0x8B6C, "Y=2: function code for dir read", inline=True)
comment(0x8B6E, "Store 2 as reply data start offset", inline=True)
comment(0x8B70, "Store 2 as command data byte", inline=True)
comment(0x8B73, "Y=3: function code for header read", inline=True)
comment(0x8B77, "X=0 after FS command completes", inline=True)
comment(0x8B79, "Load reply entry count", inline=True)
comment(0x8B7C, "Store at param block byte 0 (X=0)", inline=True)
comment(0x8B7E, "Load entries-read count from reply", inline=True)
comment(0x8B81, "Y=9: param block byte 9", inline=True)
comment(0x8B83, "Add to starting entry number", inline=True)
comment(0x8B85, "Update param block with new position", inline=True)
comment(0x8B87, "Load total reply length", inline=True)
comment(0x8B89, "Subtract header (7 bytes) from reply len", inline=True)
comment(0x8B8B, "Store adjusted length in command buffer", inline=True)
comment(0x8B8E, "Store as byte count for copy loop", inline=True)
comment(0x8B90, "Zero bytes: skip copy", inline=True)
comment(0x8B92, "Copy reply data to caller's buffer", inline=True)
label(0x8B95, "skip_copy_reply")      # BEQ: zero byte count, skip copy_reply_to_caller
comment(0x8B95, "X=2: clear 3 bytes", inline=True)
label(0x8B97, "zero_cmd_bytes")       # Zero 3 bytes of &0F07 area before address adjustment
comment(0x8B97, "Zero out &0F07+X area", inline=True)
comment(0x8B9A, "Next byte", inline=True)
comment(0x8B9B, "Loop for X=2,1,0", inline=True)
comment(0x8B9D, "Adjust pointer by +1 (one filename read)", inline=True)
comment(0x8BA0, "SEC for reverse adjustment", inline=True)
comment(0x8BA1, "Reverse adjustment for updated counter", inline=True)
comment(0x8BA3, "Load entries-read count", inline=True)
comment(0x8BA6, "Store in command buffer", inline=True)
comment(0x8BA9, "Adjust param block addresses", inline=True)
comment(0x8BAC, "Z=1: all done, exit", inline=True)
comment(0x8BAE, "A=&C3: Tube claim with retry", inline=True)
comment(0x8BB0, "Request Tube address claim", inline=True)
comment(0x8BB3, "C=0: claim failed, retry", inline=True)
comment(0x8BB5, "Tube claimed successfully", inline=True)
comment(0x8BB6, "Save A/X/Y and set up command ptr", inline=True)
comment(0x8BB9, "X=&FF: table index (pre-incremented)", inline=True)
comment(0x8BBB, "Disable column formatting", inline=True)
label(0x8BBD, "scan_cmd_table")        # Outer command-table search loop for * command match
comment(0x8BBD, "Y=&FF: input index (pre-incremented)", inline=True)
comment(0x8BBF, "Advance input pointer", inline=True)
comment(0x8BC0, "Advance table pointer", inline=True)
comment(0x8BC1, "Load table character", inline=True)
comment(0x8BC4, "Bit 7: end of name, dispatch", inline=True)
comment(0x8BC6, "XOR input char with table char", inline=True)
comment(0x8BC8, "Case-insensitive (clear bit 5)", inline=True)
comment(0x8BCA, "Match: continue comparing", inline=True)
comment(0x8BCC, "Mismatch: back up table pointer", inline=True)
comment(0x8BCD, "Skip to end of table entry", inline=True)
comment(0x8BCE, "Load table byte", inline=True)
comment(0x8BD1, "Loop until bit 7 set (end marker)", inline=True)
comment(0x8BD3, "Check input for '.' abbreviation", inline=True)
comment(0x8BD5, "Skip past handler high byte", inline=True)
comment(0x8BD6, "Is input '.' (abbreviation)?", inline=True)
comment(0x8BD8, "No: try next table entry", inline=True)
comment(0x8BDA, "Yes: skip '.' in input", inline=True)
comment(0x8BDB, "Back to handler high byte", inline=True)
comment(0x8BDC, "ALWAYS branch; dispatch via BMI", inline=True)
label(0x8BDE, "dispatch_cmd")         # BMI: end-of-name marker, push handler addr/dispatch
comment(0x8BDE, "Push handler address high byte", inline=True)
comment(0x8BDF, "Load handler address low byte", inline=True)
comment(0x8BE2, "Push handler address low byte", inline=True)
comment(0x8BE3, "Dispatch via RTS (addr-1 on stack)", inline=True)
comment(0x8BE4, "Match last char against '.' for *I. abbreviation", inline=True)
comment(0x8C0E, "A=6: examine format type in command", inline=True)
comment(0x8C10, "Store format type at &0F05", inline=True)
comment(0x8C13, "Set up command parameter pointers", inline=True)
comment(0x8C16, "X=1: copy dir name at cmd offset 1", inline=True)
comment(0x8C18, "Copy directory name to command buffer", inline=True)
comment(0x8C20, "X=3: start printing from reply offset 3", inline=True)
comment(0x8C22, "Print directory title (10 chars)", inline=True)
comment(0x8C25, "Print '('", inline=True)
comment(0x8C29, "Load station number from FS reply", inline=True)
comment(0x8C2C, "Print station number as decimal", inline=True)
comment(0x8C2F, "Print ')     '", inline=True)
comment(0x8C3B, "Non-zero: Public access", inline=True)
comment(0x8C3D, "Print 'Owner' + CR", inline=True)
label(0x8C48, "print_public")          # BNE: access non-zero (public), print "Public"+CR
comment(0x8C48, "Print 'Public' + CR", inline=True)
comment(0x8C57, "X=1: past command code byte", inline=True)
comment(0x8C58, "Y=&10: print 16 characters", inline=True)
comment(0x8C5A, "Print disc/CSD name from reply", inline=True)
comment(0x8C5D, "Print '    Option '", inline=True)
comment(0x8C6E, "X = boot option for name table lookup", inline=True)
comment(0x8C6F, "Print boot option as hex digit", inline=True)
comment(0x8C72, "Print ' ('", inline=True)
comment(0x8C82, "Next character", inline=True)
comment(0x8C83, "Continue printing option name", inline=True)
label(0x8C85, "done_option_name")      # BMI: bit 7 set, option name printing complete
comment(0x8C85, "Print ')' + CR + 'Dir. '", inline=True)
comment(0x8CA3, "Print library name", inline=True)
comment(0x8CAE, "Save start offset in zero page for loop", inline=True)
comment(0x8CB0, "Load examine arg count for batch size", inline=True)
comment(0x8CB2, "Store as request count at &0F07", inline=True)
comment(0x8CB5, "Load column count for display format", inline=True)
comment(0x8CB7, "Store column count in command data", inline=True)
comment(0x8CBA, "X=3: copy directory name at offset 3", inline=True)
comment(0x8CBC, "Append directory name to examine command", inline=True)
comment(0x8D31, "X=4: print 4 hex bytes", inline=True)
comment(0x8D33, "Load byte from parameter block", inline=True)
comment(0x8D35, "Print as two hex digits", inline=True)
comment(0x8D38, "Next byte (descending)", inline=True)
comment(0x8D39, "Count down", inline=True)
comment(0x8D3A, "Loop until 4 bytes printed", inline=True)
comment(0x8D3C, "A=space character", inline=True)
comment(0x8D43, "Start writing at &0F05 (after cmd header)", inline=True)
comment(0x8D45, "Start source offset at 0", inline=True)
comment(0x8D47, "Load byte from source string", inline=True)
comment(0x8D49, "Store to FS command buffer (&0F05+X)", inline=True)
comment(0x8D4C, "Advance dest pointer", inline=True)
comment(0x8D4D, "Advance source pointer", inline=True)
comment(0x8D52, "Return; X = next free position in buffer", inline=True)
comment(0x8D57, "X=0: start from first reply byte", inline=True)
comment(0x8D59, "Load byte from FS reply buffer", inline=True)
comment(0x8D5C, "Bit 7 set: end of string, return", inline=True)
comment(0x8D5E, "Non-zero: print character", inline=True)
comment(0x8D60, "Null byte: check column counter", inline=True)
comment(0x8D62, "Negative: print CR (no columns)", inline=True)
comment(0x8D64, "Advance column counter", inline=True)
comment(0x8D65, "Transfer to A for modulo", inline=True)
comment(0x8D66, "Modulo 4 columns", inline=True)
comment(0x8D68, "Update column counter", inline=True)
comment(0x8D6A, "Column 0: start new line", inline=True)
comment(0x8D6C, "Print 2-space column separator", inline=True)
label(0x8D78, "next_dir_entry")        # Always-branch: advance X, loop for next entry
comment(0x8D78, "Next byte in reply buffer", inline=True)
comment(0x8D79, "Loop until end of buffer", inline=True)
comment(0x8D7E, "Y = value to print", inline=True)
comment(0x8D7F, "Divisor = 100 (hundreds digit)", inline=True)
comment(0x8D81, "Print hundreds digit", inline=True)
comment(0x8D84, "Divisor = 10 (tens digit)", inline=True)
comment(0x8D86, "Print tens digit", inline=True)
comment(0x8D89, "Divisor = 1; fall through to units", inline=True)
comment(0x8D8B, "Save divisor to workspace", inline=True)
comment(0x8D8D, "A = dividend (from Y)", inline=True)
comment(0x8D8E, "X = &2F = ASCII '0' - 1", inline=True)
comment(0x8D90, "Prepare for subtraction", inline=True)
label(0x8D91, "divide_subtract")        # Repeated-subtraction division for decimal print
comment(0x8D91, "Count one subtraction (next digit value)", inline=True)
comment(0x8D92, "A = A - divisor", inline=True)
comment(0x8D94, "Loop while A >= 0 (borrow clear)", inline=True)
comment(0x8D96, "Undo last subtraction: A = remainder", inline=True)
comment(0x8D98, "Y = remainder for caller", inline=True)
comment(0x8D99, "A = X = ASCII digit character", inline=True)
label(0x8D9A, "print_digit")            # Print decimal digit via JMP OSASCI
comment(0x8DC5, "X=&0E: FS command buffer offset", inline=True)
comment(0x8DC7, "Store block offset for FS command", inline=True)
comment(0x8DC9, "A=&10: 16 bytes of command data", inline=True)
comment(0x8DCB, "Store options byte", inline=True)
comment(0x8DCD, "Store to FS workspace", inline=True)
comment(0x8DD0, "X=&4A: TXCB size for load command", inline=True)
comment(0x8DD2, "Y=5: FCCMND (load as command)", inline=True)
comment(0x8DD4, "Send FS examine/load command", inline=True)
comment(0x8DF9, "Check for Tube co-processor", inline=True)
comment(0x8DFC, "No Tube: execute locally", inline=True)
comment(0x8DFE, "Check load address upper bytes", inline=True)
comment(0x8E01, "Continue address range check", inline=True)
comment(0x8E04, "Carry set: not Tube space, exec locally", inline=True)
comment(0x8E06, "Claim Tube transfer channel", inline=True)
comment(0x8E09, "X=9: source offset in FS reply", inline=True)
comment(0x8E0B, "Y=&0F: page &0F (FS command buffer)", inline=True)
comment(0x8E0D, "A=4: Tube transfer type 4 (256-byte)", inline=True)
comment(0x8E0F, "Transfer data to Tube co-processor", inline=True)
comment(0x8E12, "Execute at load address via indirect JMP", inline=True)
comment(0x8E15, "Save library handle from FS reply", inline=True)
comment(0x8E1A, "Store CSD handle from FS reply", inline=True)
label(0x8E1D, "jmp_restore_args")      # JMP restore_args_return (common FS reply exit)
comment(0x8E1D, "Restore A/X/Y and return to caller", inline=True)
comment(0x8E20, "Set carry: LOGIN path (copy + boot)", inline=True)
comment(0x8E21, "Copy 4 bytes: boot option + 3 handles", inline=True)
comment(0x8E23, "SDISC: skip boot option, copy handles only", inline=True)
comment(0x8E25, "Load from FS reply (&0F05+X)", inline=True)
comment(0x8E28, "Store to handle workspace (&0E02+X)", inline=True)
label(0x8E2B, "copy_handles_loop")    # SDISC entry: skip boot option byte, X=3 descending
comment(0x8E2B, "Next handle (descending)", inline=True)
comment(0x8E2C, "Loop while X >= 0", inline=True)
comment(0x8E2E, "SDISC: done, restore args and return", inline=True)
subroutine(0x8E30, "boot_cmd_execute", hook=None,
    title="Execute boot command via OSCLI",
    description="""\
Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")
comment(0x8E30, "Y = boot option from FS workspace", inline=True)
comment(0x8E33, "X = command string offset from table", inline=True)
comment(0x8E36, "Y = &8D (high byte of command address)", inline=True)
comment(0x8E38, "Execute boot command string via OSCLI", inline=True)
comment(0x8E42, "Load handle from &F0", inline=True)
comment(0x8E54, "A=0, C set = error indicator", inline=True)
comment(0x8E56, "Look up handle &F0 in workspace", inline=True)
comment(0x8E59, "Invalid handle: return 0", inline=True)
comment(0x8E5B, "Load stored handle value", inline=True)
comment(0x8E5D, "&3F = unused/closed slot marker", inline=True)
comment(0x8E5F, "Slot in use: return actual value", inline=True)
comment(0x8E61, "Return 0 for closed/invalid handle", inline=True)
label(0x8E63, "store_handle_return")   # Store handle result to &F0, return
comment(0x8E63, "Store result back to &F0", inline=True)
comment(0x8E65, "Return", inline=True)
comment(0x8E66, "Look up handle &F0 in workspace", inline=True)
comment(0x8E69, "Invalid handle: return 0", inline=True)
comment(0x8E75, "Return", inline=True)
comment(0x8E7C, "Only OSWORDs &0F-&13 (index 0-4)", inline=True)
comment(0x8E7E, "Index >= 5: not ours, return", inline=True)
comment(0x8E87, "Load handler address high byte from table", inline=True)
comment(0x8E8A, "Push high byte for RTS dispatch", inline=True)
comment(0x8E8B, "Load handler address low byte from table", inline=True)
comment(0x8E8E, "Dispatch table: low bytes for OSWORD &0F-&13 handlers", inline=True)
comment(0x8E8F, "Y=2: save 3 bytes (&AA-&AC)", inline=True)
comment(0x8E91, "Load param block pointer byte", inline=True)
comment(0x8E94, "Save to NFS workspace via (net_rx_ptr)", inline=True)
comment(0x8E96, "Next byte (descending)", inline=True)
comment(0x8E97, "Loop for all 3 bytes", inline=True)
comment(0x8E99, "Y=0 after BPL exit; INY makes Y=1", inline=True)
comment(0x8E9A, "Read sub-function code from (&F0)+1", inline=True)
comment(0x8E9C, "Store Y=1 to &A9", inline=True)
comment(0x8E9E, "RTS dispatches to pushed handler address", inline=True)
comment(0x8EBE, "User TX CB in workspace page (high byte)", inline=True)
comment(0x8EC0, "Set param block high byte", inline=True)
comment(0x8EC2, "Set LTXCBP high byte for low-level TX", inline=True)
comment(0x8EC4, "&6F: offset into workspace for user TXCB", inline=True)
comment(0x8EC6, "Set param block low byte", inline=True)
comment(0x8EC8, "Set LTXCBP low byte for low-level TX", inline=True)
comment(0x8ECA, "X=15: copy 16 bytes (OSWORD param block)", inline=True)
comment(0x8ECC, "Copy param block to user TX control block", inline=True)
comment(0x8ECF, "Start user transmit via BRIANX", inline=True)
comment(0x8ED2, "Set source high byte from workspace page", inline=True)
comment(0x8ED4, "Store as copy source high byte in &AC", inline=True)
comment(0x8ED6, "JSRSIZ at workspace offset &7F", inline=True)
comment(0x8ED8, "Load buffer size from workspace", inline=True)
comment(0x8EDA, "Y=&80: start of JSR argument data", inline=True)
comment(0x8EDB, "Store &80 as copy source low byte", inline=True)
comment(0x8EDD, "X = buffer size (loop counter)", inline=True)
comment(0x8EDE, "X = size-1 (0-based count for copy)", inline=True)
comment(0x8EDF, "Y=0: start of destination param block", inline=True)
comment(0x8EE1, "Copy X+1 bytes from workspace to param", inline=True)
comment(0x8EE4, "Clear JSR protection status (CLRJSR)", inline=True)
comment(0x8EE7, "Y=&7F: JSRSIZ offset (READRB entry)", inline=True)
comment(0x8EE9, "Load buffer size from workspace", inline=True)
comment(0x8EEB, "Y=1: param block offset for size byte", inline=True)
comment(0x8EED, "Store buffer size to (&F0)+1", inline=True)
comment(0x8EEF, "Y=2: param block offset for args size", inline=True)
comment(0x8EF0, "A=&80: argument data starts at offset &80", inline=True)
comment(0x8EF2, "Store args start offset to (&F0)+2", inline=True)
comment(0x8EF4, "Return", inline=True)
label(0x8EF5, "osword_12_offsets")   # OSWORD &12 sub-function offset table
comment(0x8EFD, "Sub-function 4 or 5: read/set station", inline=True)
comment(0x8EFF, "LSR: 0->0, 1->0, 2->1, 3->1", inline=True)
comment(0x8F00, "X=&0D: default to static workspace page", inline=True)
comment(0x8F02, "Transfer LSR result to Y for indexing", inline=True)
comment(0x8F03, "Y=0 (sub 0-1): use page &0D", inline=True)
comment(0x8F05, "Y=1 (sub 2-3): use dynamic workspace", inline=True)
label(0x8F07, "set_workspace_page")   # Sub-fn 0-1: use static page &0D, store to &AC
comment(0x8F07, "Store workspace page in &AC (hi byte)", inline=True)
comment(0x8F09, "Load offset: &FF (sub 0-1) or &01 (sub 2-3)", inline=True)
comment(0x8F0C, "Store offset in &AB (lo byte)", inline=True)
comment(0x8F0E, "X=1: copy 2 bytes", inline=True)
comment(0x8F10, "Y=1: start at param block offset 1", inline=True)
comment(0x8F15, "LSR A: test bit 0 of sub-function", inline=True)
comment(0x8F16, "Y=1: offset for protection byte", inline=True)
comment(0x8F17, "Load protection byte from param block", inline=True)
comment(0x8F19, "C=1 (odd sub): set protection", inline=True)
comment(0x8F1B, "C=0 (even sub): read current status", inline=True)
comment(0x8F1E, "Return current value to param block", inline=True)
comment(0x8F20, "Update protection status", inline=True)
comment(0x8F23, "Also save as JSR mask backup", inline=True)
comment(0x8F26, "Return", inline=True)
label(0x8F27, "read_fs_handle")       # Read one FS handle from RX data at offset &14
comment(0x8F27, "Y=&14: RX buffer offset for FS handle", inline=True)
comment(0x8F29, "Read FS reply handle from RX data", inline=True)
comment(0x8F2B, "Y=1: param block byte 1", inline=True)
comment(0x8F2D, "Return handle to caller's param block", inline=True)
comment(0x8F2F, "Return", inline=True)
comment(0x8F30, "Sub-function 8: read FS handle", inline=True)
comment(0x8F32, "Match: read handle from RX buffer", inline=True)
comment(0x8F34, "Sub-function 9: read args size", inline=True)
comment(0x8F36, "Match: read ARGS buffer info", inline=True)
comment(0x8F38, "Sub >= 10 (bit 7 clear): read error", inline=True)
comment(0x8F3A, "Y=3: start from handle 3 (descending)", inline=True)
comment(0x8F3C, "LSR: test read/write bit", inline=True)
comment(0x8F3D, "C=0: read handles from workspace", inline=True)
comment(0x8F3F, "Init loop counter at Y=3", inline=True)
label(0x8F41, "copy_handles_to_ws")   # Convert handles to bitmasks and store to workspace
comment(0x8F41, "Reload loop counter", inline=True)
comment(0x8F43, "Read handle from caller's param block", inline=True)
comment(0x8F45, "Convert handle number to bitmask", inline=True)
comment(0x8F48, "TYA: get bitmask result", inline=True)
comment(0x8F49, "Reload loop counter", inline=True)
comment(0x8F4B, "Store bitmask to FS server table", inline=True)
comment(0x8F4E, "Next handle (descending)", inline=True)
comment(0x8F50, "Loop for handles 3,2,1", inline=True)
comment(0x8F52, "Return", inline=True)
label(0x8F53, "return_last_error")    # Sub-fn >= 10, bit 7 clear: return last FS error
comment(0x8F53, "Y=1 (post-INY): param block byte 1", inline=True)
comment(0x8F54, "Read last FS error code", inline=True)
comment(0x8F57, "Return error to caller's param block", inline=True)
comment(0x8F59, "Return", inline=True)
comment(0x8F62, "Next handle (descending)", inline=True)
comment(0x8F63, "Loop for handles 3,2,1", inline=True)
comment(0x8F65, "Return", inline=True)
comment(0x8F66, "Workspace page high byte", inline=True)
comment(0x8F68, "Set up pointer high byte in &AC", inline=True)
comment(0x8F6A, "Save param block high byte in &AB", inline=True)
comment(0x8F6C, "Disable user RX during CB operation", inline=True)
comment(0x8F6F, "Read first byte of param block", inline=True)
comment(0x8F71, "Save: 0=open new, non-zero=read RXCB", inline=True)
comment(0x8F73, "Non-zero: read specified RXCB", inline=True)
comment(0x8F75, "Start scan from RXCB #3 (0-2 reserved)", inline=True)
comment(0x8F77, "Convert RXCB number to workspace offset", inline=True)
comment(0x8F7A, "Invalid RXCB: return zero", inline=True)
comment(0x8F7C, "LSR twice: byte offset / 4", inline=True)
comment(0x8F7D, "Yields RXCB number from offset", inline=True)
comment(0x8F7E, "X = RXCB number for iteration", inline=True)
comment(0x8F7F, "Read flag byte from RXCB workspace", inline=True)
comment(0x8F81, "Zero = end of CB list", inline=True)
comment(0x8F83, "&3F = deleted slot, free for reuse", inline=True)
comment(0x8F85, "Found free slot", inline=True)
comment(0x8F87, "Try next RXCB", inline=True)
comment(0x8F88, "A = next RXCB number", inline=True)
comment(0x8F89, "Continue scan (always branches)", inline=True)
comment(0x8F8B, "A = free RXCB number", inline=True)
comment(0x8F8C, "X=0 for indexed indirect store", inline=True)
comment(0x8F8E, "Return RXCB number to caller's byte 0", inline=True)
label(0x8F90, "read_rxcb")            # BNE: non-zero RXCB param, skip free-slot scan
comment(0x8F90, "Convert RXCB number to workspace offset", inline=True)
comment(0x8F93, "Invalid: write zero to param block", inline=True)
comment(0x8F95, "Y = offset-1: points to flag byte", inline=True)
comment(0x8F96, "Set &AB = workspace ptr low byte", inline=True)
comment(0x8F98, "&C0: test mask for flag byte", inline=True)
comment(0x8F9A, "Y=1: flag byte offset in RXCB", inline=True)
comment(0x8F9C, "X=11: copy 12 bytes from RXCB", inline=True)
comment(0x8F9E, "Compare Y(1) with saved byte (open/read)", inline=True)
comment(0x8FA0, "ADC flag: test if slot is in use", inline=True)
comment(0x8FA2, "Zero: slot open, do copy", inline=True)
comment(0x8FA4, "Negative: slot has received data", inline=True)
label(0x8FA6, "copy_rxcb_to_param")   # Copy RXCB data from workspace to param block
comment(0x8FA6, "C=0: workspace-to-param direction", inline=True)
comment(0x8FA7, "Copy RXCB data to param block", inline=True)
comment(0x8FAA, "Done: skip deletion on error", inline=True)
comment(0x8FAC, "Mark CB as consumed (consume-once)", inline=True)
comment(0x8FAE, "Y=1: flag byte offset", inline=True)
comment(0x8FB0, "Write &3F to mark slot deleted", inline=True)
comment(0x8FB2, "Branch to exit (always taken)", inline=True)
comment(0x8FB4, "Advance through multi-byte field", inline=True)
comment(0x8FB6, "Loop until all bytes processed", inline=True)
comment(0x8FB8, "Y=-1 → Y=0 after STA below", inline=True)
comment(0x8FB9, "Return zero (no free RXCB found)", inline=True)
label(0x8FBB, "reenable_rx")          # Common exit: ROL rx_flags, RTS
comment(0x8FBB, "Re-enable user RX", inline=True)
comment(0x8FBE, "Return", inline=True)
comment(0x8FBF, "Workspace offset &1C = RX data start", inline=True)
comment(0x8FCC, "A = base address low byte", inline=True)
comment(0x8FCE, "A = base + 1 (skip length byte)", inline=True)
comment(0x8FD0, "Store 16-bit start addr at ws+&1C/&1D", inline=True)
comment(0x8FD3, "Read data length from (&F0)+1", inline=True)
comment(0x8FD5, "A = data length byte", inline=True)
comment(0x8FD7, "Workspace offset &20 = RX data end", inline=True)
comment(0x8FD9, "A = base + length = end address low", inline=True)
comment(0x8FDB, "Store low byte of 16-bit address", inline=True)
comment(0x8FDD, "Advance to high byte offset", inline=True)
comment(0x8FDE, "A = high byte of base address", inline=True)
comment(0x8FE0, "Add carry for 16-bit addition", inline=True)
comment(0x8FE2, "Store high byte", inline=True)
comment(0x8FE4, "Return", inline=True)
comment(0x8FE7, "A >= 1: handle TX result", inline=True)
comment(0x8FE9, "Y=&23: start of template (descending)", inline=True)
comment(0x8FEB, "Load ROM template byte", inline=True)
comment(0x8FEE, "Non-zero = use ROM template byte as-is", inline=True)
comment(0x8FF0, "Zero = substitute from NMI workspace", inline=True)
label(0x8FF3, "store_txcb_byte")      # BNE: non-zero template byte, skip substitution
comment(0x8FF3, "Store to dynamic workspace", inline=True)
comment(0x8FF5, "Descend through template", inline=True)
comment(0x8FF6, "Stop at offset &17", inline=True)
comment(0x8FF8, "Loop until all bytes copied", inline=True)
comment(0x8FFA, "Y=&18: TX block starts here", inline=True)
comment(0x8FFB, "Point net_tx_ptr at workspace+&18", inline=True)
comment(0x8FFD, "Set up RX buffer start/end pointers", inline=True)
comment(0x9000, "Y=2: port byte offset in RXCB", inline=True)
comment(0x9002, "A=&90: FS reply port", inline=True)
comment(0x9004, "Store port &90 at (&F0)+2", inline=True)
label(0x9008, "copy_fs_addr")          # Copy 3-byte FS station address into RX param block
comment(0x9008, "Copy FS station addr from workspace", inline=True)
comment(0x900B, "Store to RX param block", inline=True)
comment(0x900D, "Next byte", inline=True)
comment(0x900E, "Done 3 bytes (Y=4,5,6)?", inline=True)
comment(0x9010, "No: continue copying", inline=True)
comment(0x9012, "High byte of workspace for TX ptr", inline=True)
comment(0x9014, "Store as TX pointer high byte", inline=True)
comment(0x9016, "Enable interrupts before transmit", inline=True)
comment(0x9017, "Transmit with full retry", inline=True)
comment(0x901A, "Y=&20: RX end address offset", inline=True)
comment(0x901C, "Set RX end address to &FFFF (accept any length)", inline=True)
comment(0x901E, "Store end address low byte (&FF)", inline=True)
comment(0x9021, "Store end address high byte (&FF)", inline=True)
comment(0x9023, "Y=&19: port byte in workspace RXCB", inline=True)
comment(0x9025, "A=&90: FS reply port", inline=True)
comment(0x9027, "Store port to workspace RXCB", inline=True)
comment(0x902A, "A=&7F: flag byte = waiting for reply", inline=True)
comment(0x902C, "Store flag byte to workspace RXCB", inline=True)
comment(0x902E, "Jump to RX poll (BRIANX)", inline=True)
label(0x9031, "handle_tx_result")     # BCS: A>=1, save flags and load RX result
comment(0x9031, "Save processor flags", inline=True)
comment(0x9032, "Y=1: first data byte offset", inline=True)
comment(0x9034, "Load first data byte from RX buffer", inline=True)
comment(0x9036, "X = first data byte (command code)", inline=True)
comment(0x9037, "Advance to next data byte", inline=True)
comment(0x9038, "Load station address high byte", inline=True)
comment(0x903A, "Advance past station addr", inline=True)
comment(0x903B, "Save Y as data index", inline=True)
comment(0x903D, "Store station addr hi at (net_rx_ptr)+&72", inline=True)
comment(0x903F, "Store to workspace", inline=True)
comment(0x9042, "A = command code (from X)", inline=True)
comment(0x9043, "Store station addr lo at (net_rx_ptr)+&71", inline=True)
comment(0x9045, "Restore flags from earlier PHP", inline=True)
comment(0x9046, "First call: adjust data length", inline=True)
label(0x9048, "send_data_bytes")       # Outer loop: fetch and TX successive data bytes
comment(0x9048, "Reload data index", inline=True)
comment(0x904A, "Advance data index for next iteration", inline=True)
comment(0x904C, "Load next data byte", inline=True)
comment(0x9062, "Not &0D: continue with next byte", inline=True)
comment(0x9064, "Return (data complete)", inline=True)
comment(0x9065, "First-packet: set up control block", inline=True)
comment(0x9068, "Y=&7B: data length offset", inline=True)
comment(0x906A, "Load current data length", inline=True)
comment(0x906C, "Add 3 for header bytes", inline=True)
comment(0x906C, "Adjust data length by 3 for header bytes", inline=True)
comment(0x906E, "Store adjusted length", inline=True)
comment(0x9070, "Enable interrupts", inline=True)
comment(0x9071, "Transmit via tx_poll_ff", inline=True)
comment(0x9074, "Save processor status", inline=True)
comment(0x9075, "Save A (reason code)", inline=True)
comment(0x9076, "Save X", inline=True)
comment(0x9077, "Push X to stack", inline=True)
comment(0x9078, "Save Y", inline=True)
comment(0x9079, "Push Y to stack", inline=True)
comment(0x907A, "Get stack pointer for indexed access", inline=True)
comment(0x907B, "Retrieve original A (reason code) from stack", inline=True)
comment(0x907E, "Reason codes 0-8 only", inline=True)
comment(0x9080, "Code >= 9: skip dispatch, restore regs", inline=True)
comment(0x9082, "X = reason code for table lookup", inline=True)
comment(0x9083, "Dispatch to handler via trampoline", inline=True)
comment(0x9086, "Restore Y", inline=True)
comment(0x9087, "Transfer to Y register", inline=True)
comment(0x9088, "Restore X", inline=True)
comment(0x9089, "Transfer to X register", inline=True)
comment(0x908A, "Restore A", inline=True)
comment(0x908B, "Restore processor status flags", inline=True)
comment(0x908C, "Return with all registers preserved", inline=True)
comment(0x9090, "Push high byte of handler address", inline=True)
comment(0x9091, "Load handler low byte from table", inline=True)
comment(0x9094, "Push low byte of handler address", inline=True)
comment(0x9095, "Load workspace byte &EF for handler", inline=True)
comment(0x9097, "RTS dispatches to pushed handler", inline=True)
comment(0x90AB, "ROR/ASL on stacked P: zeros carry to signal success", inline=True)
comment(0x90AE, "ASL: restore P after ROR zeroed carry", inline=True)
comment(0x90B1, "Y = character to write", inline=True)
comment(0x90B2, "Store character at workspace offset &DA", inline=True)
comment(0x90B4, "Store char at workspace offset &DA", inline=True)
comment(0x90B6, "A=0: command type for net write char", inline=True)
comment(0x90B8, "Y=&D9: command type offset", inline=True)
comment(0x90BA, "Store command type at ws+&D9", inline=True)
comment(0x90BC, "Mark TX control block as active (&80)", inline=True)
comment(0x90BE, "Y=&0C: TXCB start offset", inline=True)
comment(0x90C0, "Set TX active flag at ws+&0C", inline=True)
comment(0x90C2, "Redirect net_tx_ptr low to workspace", inline=True)
comment(0x90C4, "Load workspace page high byte", inline=True)
comment(0x90C6, "Complete ptr redirect", inline=True)
comment(0x90C8, "Transmit with full retry", inline=True)
comment(0x90CB, "Mark TXCB as deleted (&3F) after transmit", inline=True)
comment(0x90CD, "Write &3F to TXCB byte 0", inline=True)
comment(0x90CF, "Return", inline=True)
comment(0x90D0, "Load original Y (OSBYTE secondary param)", inline=True)
comment(0x90D2, "OSBYTE &81 (INKEY): always forward to terminal", inline=True)
comment(0x90D4, "Forward &81 to terminal for keyboard read", inline=True)
comment(0x90D6, "Y=1: search NCTBPL table (execute on both)", inline=True)
comment(0x90D8, "X=9: 10-entry NCTBPL table size", inline=True)
comment(0x90DA, "Search for OSBYTE code in NCTBPL table", inline=True)
comment(0x90DD, "Match found: dispatch with Y=1 (both)", inline=True)
comment(0x90DF, "Y=-1: search NCTBMI table (terminal only)", inline=True)
comment(0x90E0, "Second DEY: Y=&FF (from 1 via 0)", inline=True)
comment(0x90E1, "X=&0E: 15-entry NCTBMI table size", inline=True)
comment(0x90E3, "Search for OSBYTE code in NCTBMI table", inline=True)
comment(0x90E6, "Match found: dispatch with Y=&FF (terminal)", inline=True)
comment(0x90E8, "Y=0: OSBYTE not recognised, ignore", inline=True)
label(0x90E9, "dispatch_remote_osbyte") # Common target for OSBYTE dispatch setup
comment(0x90E9, "X=2 bytes to copy (default for RBYTE)", inline=True)
comment(0x90EB, "A=Y: check table match result", inline=True)
comment(0x90EC, "Y=0: not recognised, return unhandled", inline=True)
comment(0x90EE, "Y>0 (NCTBPL): send only, no result expected", inline=True)
comment(0x90EF, "Y>0 (NCTBPL): no result expected, skip RX", inline=True)
comment(0x90F1, "Y<0 (NCTBMI): X=3 bytes (result + P flags)", inline=True)
comment(0x90F2, "Y=&DC: top of 3-byte stack frame region", inline=True)
comment(0x90F4, "Copy OSBYTE args from stack frame to workspace", inline=True)
comment(0x90F7, "Store to NFS workspace for transmission", inline=True)
comment(0x90F9, "Next byte (descending)", inline=True)
comment(0x90FA, "Copied all 3 bytes? (&DC, &DB, &DA)", inline=True)
comment(0x90FC, "Loop for remaining bytes", inline=True)
comment(0x90FE, "A = byte count for setup_tx_and_send", inline=True)
comment(0x90FF, "Build TXCB and transmit to terminal", inline=True)
comment(0x9102, "Restore N flag from table match type", inline=True)
comment(0x9103, "Y was positive (NCTBPL): done, no result", inline=True)
comment(0x9105, "Set up RX control block to wait for reply", inline=True)
comment(0x910B, "Bit7 clear: still waiting, poll again", inline=True)
comment(0x910D, "X = stack pointer for register restoration", inline=True)
comment(0x910E, "Y=&DD: saved P byte offset in workspace", inline=True)
comment(0x9110, "Load remote processor status from reply", inline=True)
comment(0x9112, "Force V=1 (claimed) and I=1 (no IRQ) in saved P", inline=True)
comment(0x9114, "ALWAYS branch (ORA #&44 never zero)", inline=True)
comment(0x9116, "Previous workspace offset", inline=True)
comment(0x9117, "Previous stack register slot", inline=True)
comment(0x9118, "Load next result byte (X, then Y)", inline=True)
comment(0x911A, "Write result bytes to stacked registers", inline=True)
comment(0x911D, "Copied all result bytes? (P at &DA)", inline=True)
comment(0x911F, "Loop for remaining result bytes", inline=True)
comment(0x9121, "Return to OSBYTE dispatcher", inline=True)
comment(0x9122, "Compare OSBYTE code with table entry", inline=True)
comment(0x9125, "Match found: return with Z=1", inline=True)
comment(0x9127, "Next table entry (descending)", inline=True)
comment(0x9128, "Loop for remaining entries", inline=True)
comment(0x912A, "Return; Z=1 if match, Z=0 if not", inline=True)
label(0x912B, "remote_osbyte_table") # OSBYTE codes accepted for remote execution
for addr in range(0x912B, 0x913A):
    byte(addr)
comment(0x912B, "OSBYTE &04: cursor key status", inline=True)
comment(0x912C, "OSBYTE &09: flash duration (1st colour)", inline=True)
comment(0x912D, "OSBYTE &0A: flash duration (2nd colour)", inline=True)
comment(0x912E, "OSBYTE &14: explode soft character RAM", inline=True)
comment(0x912F, "OSBYTE &9A: video ULA control register", inline=True)
comment(0x9130, "OSBYTE &9B: video ULA palette", inline=True)
comment(0x9131, "OSBYTE &9C: ACIA control register", inline=True)
comment(0x9132, "OSBYTE &E2: function key &D0-&DF", inline=True)
comment(0x9133, "OSBYTE &0B: auto-repeat delay", inline=True)
comment(0x9134, "OSBYTE &0C: auto-repeat rate", inline=True)
comment(0x9135, "OSBYTE &0F: flush buffer class", inline=True)
comment(0x9136, "OSBYTE &79: keyboard scan from X", inline=True)
comment(0x9137, "OSBYTE &7A: keyboard scan from &10", inline=True)
comment(0x9138, "OSBYTE &E3: function key &E0-&EF", inline=True)
comment(0x9139, "OSBYTE &E4: function key &F0-&FF", inline=True)
comment(0x913E, "OSWORD 7 (sound): handle via common path", inline=True)
comment(0x9140, "OSWORD 8 = define an envelope", inline=True)
comment(0x9142, "Not OSWORD 7 or 8: ignore (BNE exits)", inline=True)
label(0x9144, "copy_params_rword")     # Copy param bytes and tag as RWORD message
comment(0x9144, "Point workspace to offset &DB for params", inline=True)
comment(0x9146, "Store workspace ptr offset &DB", inline=True)
label(0x9148, "copy_osword_params")    # Copy OSWORD parameter bytes from RX buffer to workspace
comment(0x9148, "Copy parameter bytes from RX buffer", inline=True)
comment(0x914A, "Write param byte to workspace", inline=True)
comment(0x914C, "Next byte (descending)", inline=True)
comment(0x914D, "Loop for all parameter bytes", inline=True)
comment(0x914F, "Y=0 after loop", inline=True)
comment(0x9150, "Point workspace to offset &DA", inline=True)
comment(0x9152, "Store original OSBYTE code at workspace+0", inline=True)
comment(0x9154, "Store OSBYTE code at ws+0", inline=True)
comment(0x9156, "Reset workspace ptr to base", inline=True)
comment(0x9158, "Y=&14: command type offset", inline=True)
comment(0x915A, "Tag as RWORD (port &E9)", inline=True)
comment(0x915C, "Store port tag at ws+&14", inline=True)
comment(0x915E, "A=1: single-byte TX", inline=True)
comment(0x9160, "Transmit via workspace TXCB", inline=True)
comment(0x9163, "Restore workspace ptr", inline=True)
comment(0x9168, "X=&0D: template offset for alt entry", inline=True)
comment(0x916A, "Y=&7C: target workspace offset for alt entry", inline=True)
comment(0x916C, "BIT test: V flag = bit 6 of &83B3", inline=True)
comment(0x916F, "V=1: store to (net_rx_ptr) instead", inline=True)
comment(0x9171, "Y=&17: workspace target offset (main entry)", inline=True)
comment(0x9173, "X=&1A: template table index (main entry)", inline=True)
comment(0x9175, "V=0: target is (nfs_workspace)", inline=True)
comment(0x9176, "Load template byte from ctrl_block_template[X]", inline=True)
comment(0x9179, "&FE = stop sentinel", inline=True)
comment(0x917B, "End of template: jump to exit", inline=True)
comment(0x917D, "&FD = skip sentinel", inline=True)
comment(0x917F, "Skip: don't store, just decrement Y", inline=True)
comment(0x9181, "&FC = page byte sentinel", inline=True)
comment(0x9183, "Not sentinel: store template value directly", inline=True)
comment(0x918B, "PAGE byte → Y=&02 / Y=&74", inline=True)
comment(0x918D, "→ Y=&04 / Y=&76", inline=True)
comment(0x918F, "PAGE byte → Y=&06 / Y=&78", inline=True)
comment(0x9191, "→ Y=&08 / Y=&7A", inline=True)
comment(0x9193, "Alt-path only → Y=&70", inline=True)
comment(0x9193, "→ Y=&0A / Y=&7C", inline=True)
label(0x9195, "cb_template_main_start") # Control block template: main-path section
comment(0x9195, "SKIP", inline=True)
comment(0x9195, "→ Y=&0C (main only)", inline=True)
comment(0x9196, "→ Y=&01 / Y=&73", inline=True)
comment(0x9196, "→ Y=&0D (main only)", inline=True)
label(0x9199, "cb_template_tail")    # Control block template: tail section
comment(0x9199, "→ Y=&10 (main only)", inline=True)
comment(0x919C, "→ Y=&07 / Y=&79", inline=True)
comment(0x91C4, "X-1: convert 1-based buffer to 0-based", inline=True)
comment(0x91C5, "Is this the network printer buffer?", inline=True)
comment(0x91C7, "No: skip printer init", inline=True)
comment(0x91C9, "&1F = initial buffer pointer offset", inline=True)
comment(0x91CB, "Reset printer buffer write position", inline=True)
comment(0x91CE, "&41 = initial PFLAGS (bit 6 set, bit 0 set)", inline=True)
comment(0x91D3, "Return", inline=True)
comment(0x91D4, "Only handle buffer 4 (network printer)", inline=True)
comment(0x91D6, "Not buffer 4: ignore", inline=True)
comment(0x91D8, "A = reason code", inline=True)
comment(0x91D9, "Reason 1? (DEX: 1->0)", inline=True)
comment(0x91DA, "Not reason 1: handle Ctrl-B/C", inline=True)
comment(0x91DC, "Get stack pointer for P register", inline=True)
comment(0x91DD, "Force I flag in stacked P to block IRQs", inline=True)
comment(0x91E0, "Write back modified P register", inline=True)
comment(0x91E3, "OSBYTE &91: extract char from MOS buffer", inline=True)
comment(0x91E5, "X=3: printer buffer number", inline=True)
comment(0x91EA, "Buffer empty: return", inline=True)
comment(0x91EC, "Y = extracted character", inline=True)
comment(0x91ED, "Store char in output buffer", inline=True)
comment(0x91F0, "Buffer nearly full? (&6E = threshold)", inline=True)
comment(0x91F2, "Not full: get next char", inline=True)
comment(0x91F4, "Buffer full: flush to network", inline=True)
comment(0x91F7, "Continue after flush", inline=True)
comment(0x91F9, "Load current buffer offset", inline=True)
comment(0x91FC, "Store byte at current position", inline=True)
comment(0x91FE, "Advance buffer pointer", inline=True)
comment(0x9201, "Return; Y = buffer offset", inline=True)
label(0x9202, "toggle_print_flag")    # Toggle print-active flag and update PFLAGS
comment(0x9202, "Save reason code", inline=True)
comment(0x9203, "A = reason code", inline=True)
comment(0x9204, "EOR #1: toggle print-active flag (bit 0)", inline=True)
comment(0x9206, "Store toggled flag as output byte", inline=True)
comment(0x9219, "Extract upper nibble of PFLAGS", inline=True)
comment(0x921B, "Shift for bit extraction", inline=True)
comment(0x921C, "Save in X", inline=True)
comment(0x921D, "Restore original reason code", inline=True)
comment(0x921E, "Merge print-active bit from original A", inline=True)
comment(0x921F, "Retrieve shifted PFLAGS", inline=True)
comment(0x9220, "Recombine into new PFLAGS value", inline=True)
comment(0x9224, "Return", inline=True)
comment(0x9225, "Store buffer length at workspace offset &08", inline=True)
comment(0x9227, "Current buffer fill position", inline=True)
comment(0x922A, "Write to workspace offset &08", inline=True)
comment(0x922C, "Store page high byte at offset &09", inline=True)
comment(0x922E, "Y=&09", inline=True)
comment(0x922F, "Write page high byte at offset &09", inline=True)
comment(0x9231, "Also store at offset &05", inline=True)
comment(0x9233, "(end address high byte)", inline=True)
comment(0x9235, "Y=&0B: flag byte offset", inline=True)
comment(0x9237, "X=&26: start from template entry &26", inline=True)
comment(0x9239, "Reuse ctrl_block_setup with CLV entry", inline=True)
comment(0x923C, "Y=&0A: sequence flag byte offset", inline=True)
comment(0x9248, "Old sequence bit into bit 0", inline=True)
comment(0x9249, "Store sequence flag at offset &0A", inline=True)
comment(0x924B, "Y=&1F: buffer start offset", inline=True)
comment(0x924D, "Reset printer buffer to start (&1F)", inline=True)
comment(0x9250, "A=0: printer output flag", inline=True)
comment(0x9252, "X=0: workspace low byte", inline=True)
comment(0x9253, "Y = workspace page high byte", inline=True)
comment(0x9255, "Enable interrupts before TX", inline=True)
comment(0x9256, "Set TX control block ptr low byte", inline=True)
comment(0x9258, "Set TX control block ptr high byte", inline=True)
comment(0x925A, "Save A (handle bitmask) for later", inline=True)
comment(0x925B, "Compute sequence bit from handle", inline=True)
comment(0x925E, "Zero: no sequence bit set", inline=True)
comment(0x9260, "Non-zero: normalise to bit 0", inline=True)
comment(0x9262, "Y=0: flag byte offset in TXCB", inline=True)
comment(0x9264, "Merge sequence into existing flag byte", inline=True)
comment(0x9266, "Save merged flag byte", inline=True)
comment(0x9267, "Write flag+sequence to TXCB byte 0", inline=True)
comment(0x9269, "Transmit with full retry", inline=True)
comment(0x926C, "End address &FFFF = unlimited data length", inline=True)
comment(0x926E, "Y=8: end address low offset in TXCB", inline=True)
comment(0x9270, "Store &FF to end addr low", inline=True)
comment(0x9273, "Store &FF to end addr high (Y=9)", inline=True)
comment(0x9275, "Recover merged flag byte", inline=True)
comment(0x9276, "Save in X for sequence compare", inline=True)
comment(0x9277, "Y=&D1: printer port number", inline=True)
comment(0x9279, "Recover saved handle bitmask", inline=True)
comment(0x927A, "Re-save for later consumption", inline=True)
comment(0x927B, "A=0: port &D1 (print); A!=0: port &90 (FS)", inline=True)
comment(0x927D, "Y=&90: FS data port", inline=True)
comment(0x927F, "A = selected port number", inline=True)
comment(0x9280, "Y=1: port byte offset in TXCB", inline=True)
comment(0x9282, "Write port to TXCB byte 1", inline=True)
comment(0x9284, "A = saved flag byte (expected sequence)", inline=True)
comment(0x9286, "Push expected sequence for retry loop", inline=True)
comment(0x9287, "Flag byte &7F = waiting for reply", inline=True)
comment(0x9289, "Write to TXCB flag byte (Y=0)", inline=True)
comment(0x928B, "Transmit and wait for reply (BRIANX)", inline=True)
comment(0x928E, "Recover expected sequence", inline=True)
comment(0x928F, "Keep on stack for next iteration", inline=True)
comment(0x9290, "Check if TX result matches expected sequence", inline=True)
comment(0x9292, "Bit 0 to carry (sequence mismatch?)", inline=True)
comment(0x9293, "C=1: mismatch, retry transmit", inline=True)
comment(0x9295, "Clean up: discard expected sequence", inline=True)
comment(0x9296, "Discard saved handle bitmask", inline=True)
comment(0x929B, "Toggle sequence bit on success", inline=True)
comment(0x929E, "Return", inline=True)
comment(0x929F, "Save current table index", inline=True)
comment(0x92A1, "Push for later restore", inline=True)
comment(0x92A2, "Point workspace to palette save area (&E9)", inline=True)
comment(0x92A4, "Set workspace low byte", inline=True)
comment(0x92A6, "Y=0: first palette entry", inline=True)
comment(0x92A8, "Clear table index counter", inline=True)
comment(0x92AA, "Save current screen MODE to workspace", inline=True)
comment(0x92AD, "Store MODE at workspace[0]", inline=True)
comment(0x92AF, "Advance workspace pointer past MODE byte", inline=True)
comment(0x92B1, "Read colour count (from &0351)", inline=True)
comment(0x92B4, "Push for iteration count tracking", inline=True)
comment(0x92B5, "A=0: logical colour number for OSWORD", inline=True)
label(0x92B6, "save_palette_entry")    # Per-entry OSWORD &0B palette read and workspace store
comment(0x92B6, "Store logical colour at workspace[0]", inline=True)
comment(0x92B8, "X = workspace ptr low (param block addr)", inline=True)
comment(0x92BA, "Y = workspace ptr high", inline=True)
comment(0x92BC, "OSWORD &0B: read palette for logical colour", inline=True)
comment(0x92C1, "Recover colour count", inline=True)
comment(0x92C2, "Y=0: access workspace[0]", inline=True)
comment(0x92C4, "Write colour count back to workspace[0]", inline=True)
comment(0x92C6, "Y=1: access workspace[1] (palette result)", inline=True)
comment(0x92C7, "Read palette value returned by OSWORD", inline=True)
comment(0x92C9, "Push palette value for next iteration", inline=True)
comment(0x92CA, "X = current workspace ptr low", inline=True)
comment(0x92CC, "Advance workspace pointer", inline=True)
comment(0x92CE, "Increment table index", inline=True)
comment(0x92D0, "Y=0 for next store", inline=True)
comment(0x92D1, "Load table index as logical colour", inline=True)
comment(0x92D3, "Loop until workspace wraps past &F9", inline=True)
comment(0x92D5, "Continue for all 16 palette entries", inline=True)
comment(0x92D7, "Discard last palette value from stack", inline=True)
comment(0x92D8, "Reset table index to 0", inline=True)
comment(0x92DA, "Advance workspace past palette data", inline=True)
comment(0x92DC, "Save cursor pos and OSBYTE state values", inline=True)
comment(0x92DF, "Advance workspace past VDU state data", inline=True)
comment(0x92E1, "Recover saved table index", inline=True)
comment(0x92E2, "Restore table index", inline=True)
comment(0x92E4, "Restore LSTAT from saved OLDJSR value", inline=True)
comment(0x92E7, "Write to protection status", inline=True)
comment(0x92EA, "Return", inline=True)
comment(0x92EB, "Read cursor editing state", inline=True)
comment(0x92EE, "Store to workspace[Y]", inline=True)
comment(0x92F0, "Preserve in X for OSBYTE", inline=True)
comment(0x92F1, "OSBYTE &85: read cursor position", inline=True)
comment(0x92F4, "Advance workspace pointer", inline=True)
comment(0x92F6, "Y result from OSBYTE &85", inline=True)
comment(0x92F7, "Store Y pos to workspace (X=0)", inline=True)
comment(0x92F9, "Self-call trick: executes twice", inline=True)
comment(0x92FC, "X=0 for (zp,X) addressing", inline=True)
comment(0x92FE, "Index into OSBYTE number table", inline=True)
comment(0x9300, "Next table entry next time", inline=True)
comment(0x9302, "Advance workspace pointer", inline=True)
comment(0x9304, "Read OSBYTE number from table", inline=True)
comment(0x9307, "Y=&FF: read current value", inline=True)
comment(0x9309, "Call OSBYTE", inline=True)
comment(0x930C, "Result in X to A", inline=True)
comment(0x930D, "X=0 for indexed indirect store", inline=True)
comment(0x930F, "Store result to workspace", inline=True)
label(0x9315, "reloc_zp_src")        # ROM source of zero-page relocated code
label(0x935A, "reloc_p4_src")        # ROM source of Tube host page 4 code
comment(0x966F, "INTOFF: read station ID, disable NMIs", inline=True)
comment(0x9672, "Full ADLC hardware reset", inline=True)
comment(0x9675, "OSBYTE &EA: check Tube co-processor", inline=True)
comment(0x9677, "X=0 for OSBYTE", inline=True)
comment(0x9679, "Y=&FF for OSBYTE", inline=True)
comment(0x9681, "OSBYTE &8F: issue service request", inline=True)
comment(0x9683, "X=&0C: NMI claim service", inline=True)
comment(0x9685, "Y=&FF: pass to adlc_init_workspace", inline=True)
comment(0x968A, "Copy 32 bytes of NMI shim from ROM to &0D00", inline=True)
label(0x968C, "copy_nmi_shim")        # Copy 32 bytes of NMI shim code from ROM to &0D00
comment(0x968C, "Read byte from NMI shim ROM source", inline=True)
comment(0x968F, "Write to NMI shim RAM at &0D00", inline=True)
comment(0x9692, "Next byte (descending)", inline=True)
comment(0x9693, "Loop until all 32 bytes copied", inline=True)
comment(0x9695, "Patch current ROM bank into NMI shim", inline=True)
comment(0x9697, "Self-modifying code: ROM bank at &0D07", inline=True)
comment(0x969A, "&80 = Econet initialised", inline=True)
comment(0x969C, "Mark TX as complete (ready)", inline=True)
comment(0x969F, "Mark Econet as initialised", inline=True)
comment(0x96A2, "Read station ID (&FE18 = INTOFF side effect)", inline=True)
comment(0x96A5, "Store our station ID in TX scout", inline=True)
comment(0x96FF, "Return", inline=True)
label(0x9718, "accept_frame")         # Station ID matched, install next NMI handler
comment(0x9718, "Install next NMI handler at &96DC (RX scout net byte)", inline=True)
label(0x9735, "accept_local_net")     # Network=0: clear broadcast marker
comment(0x9735, "Network = 0 (local): clear tx_flags", inline=True)
label(0x9738, "accept_scout_net")     # Common accept for local/broadcast frames
comment(0x973A, "Install scout data reading loop at &970E", inline=True)
comment(0x9746, "Neither set -- clean end, discard via &99E8", inline=True)
comment(0x9756, "No RDA -- error handler &96FE", inline=True)
comment(0x977D, "Write CR1", inline=True)
comment(0x9782, "Write CR2", inline=True)
comment(0x9796, "Write CR1: switch to TX mode", inline=True)
comment(0x97A1, "Port = 0 -- immediate operation handler", inline=True)
comment(0x97A4, "Check if broadcast (bit6 of tx_flags)", inline=True)
comment(0x97A7, "Not broadcast -- skip CR2 setup", inline=True)
comment(0x97A9, "CR2=&07: broadcast prep", inline=True)
comment(0x97AB, "Write CR2: broadcast frame prep", inline=True)
label(0x97AE, "scan_port_list")        # Non-broadcast: skip CR2 setup, begin port scan
comment(0x97AE, "Check if RX port list active (bit7)", inline=True)
comment(0x97B1, "No active ports -- try NFS workspace", inline=True)
comment(0x97B3, "Start scanning port list at page &C0", inline=True)
label(0x97BB, "check_port_slot")      # Loop: read port control byte, zero=end
comment(0x97BB, "Y=0: read control byte from start of slot", inline=True)
comment(0x97BD, "Read port control byte from slot", inline=True)
comment(0x97BF, "Zero = end of port list, no match", inline=True)
comment(0x97C1, "&7F = any-port wildcard", inline=True)
comment(0x97C3, "Not wildcard -- check specific port match", inline=True)
comment(0x97C6, "Read port number from slot (offset 1)", inline=True)
comment(0x97C8, "Zero port in slot = match any port", inline=True)
comment(0x97CA, "Check if port matches this slot", inline=True)
comment(0x97CD, "Port mismatch -- try next slot", inline=True)
label(0x97CF, "check_station_filter") # Port matched: advance to station filter check
comment(0x97CF, "Y=2: advance to station byte", inline=True)
comment(0x97D0, "Read station filter from slot (offset 2)", inline=True)
comment(0x97D2, "Zero station = match any station, accept", inline=True)
comment(0x97D4, "Check if source station matches", inline=True)
comment(0x97D7, "Station mismatch -- try next slot", inline=True)
comment(0x97D9, "Y=3: advance to network byte", inline=True)
comment(0x97DA, "Read network filter from slot (offset 3)", inline=True)
comment(0x97DC, "Check if source network matches", inline=True)
comment(0x97DF, "Network matches or zero = accept", inline=True)
label(0x97E1, "next_port_slot")        # Mismatch: advance pointer by 12 for next slot
comment(0x97E1, "Check if NFS workspace search pending", inline=True)
comment(0x9823, "Broadcast: different completion path", inline=True)
label(0x9826, "send_data_rx_ack")     # Non-broadcast: set up CR1/CR2 for TX ACK
comment(0x9826, "CR1=&44: RX_RESET | TIE", inline=True)
comment(0x9828, "Write CR1: TX mode for ACK", inline=True)
comment(0x982B, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", inline=True)
comment(0x982D, "Write CR2: enable TX with PSE", inline=True)
comment(0x9830, "Install data_rx_setup at &97DC", inline=True)
comment(0x9832, "High byte of data_rx_setup handler", inline=True)
comment(0x9834, "Send ACK with data_rx_setup as next NMI", inline=True)
comment(0x9839, "Write CR1: switch to RX for data frame", inline=True)
comment(0x983C, "Install nmi_data_rx at &97E6", inline=True)
comment(0x9840, "Install nmi_data_rx and return from NMI", inline=True)
comment(0x9843, "A=&01: mask for AP (Address Present)", inline=True)
comment(0x9845, "BIT SR2: test AP bit", inline=True)
comment(0x9848, "No AP: wrong frame or error", inline=True)
comment(0x984A, "Read first byte (dest station)", inline=True)
comment(0x984D, "Compare to our station ID (INTOFF)", inline=True)
comment(0x9850, "Not for us: error path", inline=True)
comment(0x9852, "Install net check handler at &97FA", inline=True)
comment(0x9856, "Set NMI vector via RAM shim", inline=True)
comment(0x985C, "SR2 bit7 clear: no data ready -- error", inline=True)
comment(0x985E, "Read dest network byte", inline=True)
comment(0x9861, "Network != 0: wrong network -- error", inline=True)
comment(0x9863, "Install skip handler at &9810", inline=True)
comment(0x9865, "High byte of &9810 handler", inline=True)
comment(0x9867, "SR1 bit7: IRQ, data already waiting", inline=True)
comment(0x986A, "Data ready: skip directly, no RTI", inline=True)
comment(0x986C, "Install handler and return via RTI", inline=True)
comment(0x9872, "SR2 bit7 clear: error", inline=True)
comment(0x987A, "A=2: Tube transfer flag mask", inline=True)
comment(0x987C, "Check if Tube transfer active", inline=True)
comment(0x987F, "Tube active: use Tube RX path", inline=True)
comment(0x9881, "Install bulk read at &9843", inline=True)
comment(0x9883, "High byte of &9843 handler", inline=True)
comment(0x9885, "SR1 bit7: more data already waiting?", inline=True)
comment(0x9888, "Yes: enter bulk read directly", inline=True)
comment(0x988A, "No: install handler and RTI", inline=True)
label(0x988D, "install_tube_rx")      # BNE: Tube active, install Tube RX handler
comment(0x988D, "Tube: install Tube RX at &98A0", inline=True)
comment(0x988F, "High byte of &98A0 handler", inline=True)
comment(0x9891, "Install Tube handler and RTI", inline=True)
comment(0x9894, "Check tx_flags for error path", inline=True)
comment(0x9897, "Bit7 clear: RX error path", inline=True)
comment(0x989B, "Bit7 set: TX result = not listening", inline=True)
comment(0x989E, "Full ADLC reset on RX error", inline=True)
comment(0x98A1, "Discard and return to idle listen", inline=True)
label(0x98A9, "data_rx_loop")          # Loop: check SR2, if RDA continue reading byte pairs
comment(0x98A9, "SR2 bit7 clear: frame complete (FV)", inline=True)
comment(0x98AB, "Read first byte of pair from RX FIFO", inline=True)
comment(0x98AE, "Store byte to buffer", inline=True)
comment(0x98B0, "Advance buffer offset", inline=True)
comment(0x98B1, "Y != 0: no page boundary crossing", inline=True)
comment(0x98B3, "Crossed page: increment buffer high byte", inline=True)
comment(0x98B5, "Decrement remaining page count", inline=True)
comment(0x98B7, "No pages left: handle as complete", inline=True)
label(0x98B9, "read_sr2_between_pairs") # After page boundary, read SR2 before second byte
comment(0x98B9, "Read SR2 between byte pairs", inline=True)
comment(0x98BC, "SR2 bit7 set: more data available", inline=True)
comment(0x98BE, "SR2 non-zero, bit7 clear: frame done", inline=True)
label(0x98C0, "read_second_rx_byte")  # BMI: SR2 bit7 set, read second byte from FIFO
comment(0x98C0, "Read second byte of pair from RX FIFO", inline=True)
comment(0x98C3, "Store byte to buffer", inline=True)
comment(0x98C5, "Advance buffer offset", inline=True)
comment(0x98C6, "Save updated buffer position", inline=True)
comment(0x98C8, "Y != 0: no page boundary crossing", inline=True)
comment(0x98CA, "Crossed page: increment buffer high byte", inline=True)
comment(0x98CC, "Decrement remaining page count", inline=True)
comment(0x98CE, "No pages left: frame complete", inline=True)
label(0x98D0, "check_sr2_loop_again") # After page boundary on second byte, check SR2
comment(0x98D0, "Read SR2 for next iteration", inline=True)
comment(0x98D3, "SR2 non-zero: more data, loop back", inline=True)
comment(0x98D5, "SR2=0: no more data yet, wait for NMI", inline=True)
comment(0x98D8, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x98DA, "Write CR2: disable PSE for bit testing", inline=True)
comment(0x98DD, "CR1=&00: disable all interrupts", inline=True)
comment(0x98DF, "Write CR1: disable all interrupts", inline=True)
comment(0x98E2, "Save Y (byte count from data RX loop)", inline=True)
comment(0x98ED, "Check if buffer space remains", inline=True)
label(0x98EF, "read_last_rx_byte")    # Multi-source: check buffer then read trailing byte
comment(0x98EF, "No buffer space: error/discard frame", inline=True)
comment(0x98F4, "Y = current buffer write offset", inline=True)
comment(0x98F6, "Store last byte in port receive buffer", inline=True)
comment(0x98F8, "Advance buffer write offset", inline=True)
comment(0x98FA, "No page wrap: proceed to send ACK", inline=True)
comment(0x98FC, "Page boundary: advance buffer page", inline=True)
label(0x98FE, "send_ack")             # No more data: unconditional JMP ack_tx
comment(0x98FE, "Send ACK frame to complete handshake", inline=True)
comment(0x9901, "Read SR2 for Tube data receive path", inline=True)
label(0x9904, "rx_tube_data")         # Poll SR2 RDA and forward byte pairs to Tube R3
comment(0x9904, "RDA clear: no more data, frame complete", inline=True)
comment(0x9906, "Read data byte from ADLC RX FIFO", inline=True)
comment(0x993A, "Unexpected end: return from NMI", inline=True)
comment(0x993D, "CR1=&00: disable all interrupts", inline=True)
comment(0x993F, "Write CR1 for individual bit testing", inline=True)
comment(0x9942, "CR2=&84: disable PSE", inline=True)
comment(0x9944, "Write CR2: same pattern as main path", inline=True)
comment(0x9947, "A=&02: FV mask for Tube completion", inline=True)
comment(0x9949, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x994C, "No FV: incomplete frame, error", inline=True)
comment(0x994E, "FV set, no RDA: proceed to ACK", inline=True)
comment(0x9950, "Check if any buffer was allocated", inline=True)
comment(0x9952, "OR all 4 buffer pointer bytes together", inline=True)
comment(0x9954, "Check buffer low byte", inline=True)
comment(0x9956, "Check buffer high byte", inline=True)
comment(0x9958, "All zero (null buffer): error", inline=True)
comment(0x995A, "Read extra trailing byte from FIFO", inline=True)
comment(0x995D, "Save extra byte at &0D5D for later use", inline=True)
comment(0x9960, "Bit5 = extra data byte available flag", inline=True)
comment(0x9962, "Set extra byte flag in tx_flags", inline=True)
comment(0x9965, "Store updated flags", inline=True)
comment(0x9968, "Load TX flags to check ACK type", inline=True)
comment(0x996B, "Bit7 clear: normal scout ACK", inline=True)
comment(0x996D, "Jump to TX success result", inline=True)
comment(0x9972, "Write CR1: switch to TX mode", inline=True)
comment(0x9977, "Write CR2: enable TX with status clear", inline=True)
comment(0x997A, "Save &9995 (post-ACK port check) in &0D4B/&0D4C", inline=True)
comment(0x997C, "High byte of post-ACK handler", inline=True)
comment(0x997E, "Store next handler low byte", inline=True)
comment(0x9981, "Store next handler high byte", inline=True)
comment(0x9992, "Write dest net byte to FIFO", inline=True)
comment(0x9995, "Install nmi_ack_tx_src at &9925", inline=True)
comment(0x9997, "High byte of nmi_ack_tx_src", inline=True)
comment(0x9999, "Set NMI vector to ack_tx_src handler", inline=True)
comment(0x99B1, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | PSE", inline=True)
comment(0x99B3, "Write CR2 to clear status after ACK TX", inline=True)
comment(0x99B6, "Load saved next handler low byte", inline=True)
comment(0x99B9, "Load saved next handler high byte", inline=True)
comment(0x99BC, "Install next NMI handler", inline=True)
label(0x99BF, "start_data_tx")          # Start data TX phase of four-way handshake
comment(0x99BF, "Jump to start data TX phase", inline=True)
label(0x99D1, "dispatch_nmi_error")    # JMP nmi_error_dispatch for TX failures
comment(0x99D1, "Jump to error handler", inline=True)
comment(0x99D4, "A=2: test bit1 of tx_flags", inline=True)
comment(0x99D6, "BIT tx_flags: check data transfer bit", inline=True)
comment(0x99D9, "Bit1 clear: no transfer -- return", inline=True)
comment(0x99DB, "CLC: init carry for 4-byte add", inline=True)
comment(0x99DC, "Save carry on stack for loop", inline=True)
comment(0x99DD, "Y=8: RXCB high pointer offset", inline=True)
label(0x99DF, "add_rxcb_ptr")         # 4-byte multi-precision add to RXCB buffer pointer
comment(0x99DF, "Load RXCB[Y] (buffer pointer byte)", inline=True)
comment(0x99E1, "Restore carry from stack", inline=True)
comment(0x99E2, "Add transfer count byte", inline=True)
comment(0x99E5, "Store updated pointer back to RXCB", inline=True)
comment(0x99E7, "Next byte", inline=True)
comment(0x99E8, "Save carry for next iteration", inline=True)
comment(0x99E9, "Done 4 bytes? (Y reaches &0C)", inline=True)
comment(0x99EB, "No: continue adding", inline=True)
comment(0x99ED, "Discard final carry", inline=True)
comment(0x99EE, "A=&20: test bit5 of tx_flags", inline=True)
comment(0x99F0, "BIT tx_flags: check Tube bit", inline=True)
comment(0x99F3, "No Tube: skip Tube update", inline=True)
comment(0x99F5, "Save X on stack", inline=True)
comment(0x99F6, "Push X", inline=True)
comment(0x99F7, "A=8: offset for Tube address", inline=True)
comment(0x99F9, "CLC for address calculation", inline=True)
comment(0x99FA, "Add workspace base offset", inline=True)
comment(0x99FC, "X = address low for Tube claim", inline=True)
comment(0x99FD, "Y = address high for Tube claim", inline=True)
comment(0x99FF, "A=1: Tube claim type (read)", inline=True)
comment(0x9A01, "Claim Tube address for transfer", inline=True)
comment(0x9A04, "Load extra RX data byte", inline=True)
comment(0x9A07, "Send to Tube via R3", inline=True)
comment(0x9A18, "Load buffer bytes remaining", inline=True)
comment(0x9A1A, "CLC for address add", inline=True)
comment(0x9A1B, "Add to buffer base address", inline=True)
comment(0x9A1D, "No carry: skip high byte increment", inline=True)
comment(0x9A1F, "Carry: increment buffer high byte", inline=True)
label(0x9A21, "store_buf_ptr_lo")     # BCC: no carry, store updated buffer low byte
comment(0x9A21, "Y=8: store updated buffer position", inline=True)
comment(0x9A23, "Store updated low byte to RXCB", inline=True)
comment(0x9A25, "Y=9: buffer high byte offset", inline=True)
comment(0x9A26, "Load updated buffer high byte", inline=True)
comment(0x9A28, "Store high byte to RXCB", inline=True)
label(0x9A2A, "skip_buf_ptr_update")  # BNE: transfer not done, skip buffer ptr write
comment(0x9A2A, "Check port byte again", inline=True)
comment(0x9A2D, "Port=0: immediate op, discard+listen", inline=True)
comment(0x9A2F, "Load source network from scout buffer", inline=True)
comment(0x9A32, "Y=3: RXCB source network offset", inline=True)
comment(0x9A34, "Store source network to RXCB", inline=True)
comment(0x9A36, "Y=2: source station offset", inline=True)
comment(0x9A37, "Load source station from scout buffer", inline=True)
comment(0x9A3A, "Store source station to RXCB", inline=True)
comment(0x9A3C, "Y=1: port byte offset", inline=True)
comment(0x9A3D, "Load port byte", inline=True)
comment(0x9A40, "Store port to RXCB", inline=True)
comment(0x9A42, "Y=0: control/flag byte offset", inline=True)
comment(0x9A43, "Load control byte from scout", inline=True)
comment(0x9A46, "Set bit7 = reception complete flag", inline=True)
comment(0x9A48, "Store to RXCB (marks CB as complete)", inline=True)
comment(0x9A4A, "Tube flag bit 1 AND tx_flags bit 1", inline=True)
comment(0x9A4F, "No Tube transfer active -- skip release", inline=True)
comment(0x9A53, "Release Tube claim before discarding", inline=True)
comment(0x9A56, "Re-enter idle RX listen mode", inline=True)
comment(0x9A59, "Install nmi_rx_scout (&96BF) as NMI handler", inline=True)
comment(0x9A5B, "High byte of nmi_rx_scout", inline=True)
comment(0x9A5D, "Set NMI vector and return", inline=True)
comment(0x9A6F, "Control byte &81-&88 range check", inline=True)
comment(0x9A72, "Below &81: not an immediate op", inline=True)
comment(0x9A74, "Out of range low: jump to discard", inline=True)
comment(0x9A76, "Above &88: not an immediate op", inline=True)
comment(0x9A78, "Out of range high: jump to discard", inline=True)
comment(0x9A7A, "HALT(&87)/CONTINUE(&88) skip protection", inline=True)
comment(0x9A7C, "Ctrl >= &87: dispatch without mask check", inline=True)
comment(0x9A85, "Convert ctrl byte to 0-based index for mask", inline=True)
comment(0x9A86, "SEC for subtract", inline=True)
comment(0x9A87, "A = ctrl - &81 (0-based operation index)", inline=True)
comment(0x9A89, "Y = index for mask rotation count", inline=True)
comment(0x9A8A, "Load protection mask from LSTAT", inline=True)
label(0x9A8D, "rotate_prot_mask")      # Rotate protection mask right to align permission bit
comment(0x9A8D, "Rotate mask right by control byte index", inline=True)
comment(0x9A8E, "Decrement rotation counter", inline=True)
comment(0x9A8F, "Loop until bit aligned", inline=True)
subroutine(0x9AF7, hook=None,
    title="RX immediate: PEEK setup",
    description="""\
Writes &0D3D to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send the
PEEK response data back to the requesting station.
Uses workspace offsets (&A6/&A7) for nmi_tx_block.""")
comment(0x9B28, "Get buffer position for reply header", inline=True)
comment(0x9B2A, "Clear carry for offset addition", inline=True)
comment(0x9B2B, "Data offset = buf_len + &80 (past header)", inline=True)
comment(0x9B2D, "Y=&7F: reply data length slot", inline=True)
comment(0x9B2F, "Store reply data length in RX buffer", inline=True)
comment(0x9B31, "Y=&80: source station slot", inline=True)
comment(0x9B33, "Load requesting station number", inline=True)
comment(0x9B36, "Store source station in reply header", inline=True)
comment(0x9B39, "Load requesting network number", inline=True)
comment(0x9B3C, "Store source network in reply header", inline=True)
comment(0x9B3E, "Load control byte from received frame", inline=True)
comment(0x9B41, "Save ctrl byte for TX response", inline=True)
comment(0x9B44, "IER bit 2: disable CB1 interrupt", inline=True)
comment(0x9B46, "Write IER to disable CB1", inline=True)
comment(0x9B49, "Read ACR for shift register config", inline=True)
comment(0x9B4C, "Isolate shift register mode bits (2-4)", inline=True)
comment(0x9B4E, "Save original SR mode for later restore", inline=True)
comment(0x9B51, "Reload ACR for modification", inline=True)
comment(0x9B54, "Clear SR mode bits (keep other bits)", inline=True)
comment(0x9B56, "SR mode 4: shift out under CB1 control", inline=True)
comment(0x9B58, "Apply new shift register mode", inline=True)
comment(0x9B5B, "Read SR to clear pending interrupt", inline=True)
comment(0x9B5E, "Return to idle listen mode", inline=True)
comment(0x9BF3, "Save X on stack", inline=True)
comment(0x9BF4, "Push X", inline=True)
comment(0x9BF5, "Y=2: TXCB offset for dest station", inline=True)
comment(0x9BF7, "Load dest station from TX control block", inline=True)
comment(0x9BF9, "Store to TX scout buffer", inline=True)
comment(0x9BFD, "Load dest network from TX control block", inline=True)
comment(0x9BFF, "Store to TX scout buffer", inline=True)
comment(0x9C02, "Y=0: first byte of TX control block", inline=True)
comment(0x9C04, "Load control/flag byte", inline=True)
comment(0x9C06, "Bit7 set: immediate operation ctrl byte", inline=True)
comment(0x9C08, "Bit7 clear: normal data transfer", inline=True)
label(0x9C0B, "tx_imm_op_setup")       # BMI: TXCB bit7 set, store ctrl byte for imm op
comment(0x9C0B, "Store control byte to TX scout buffer", inline=True)
comment(0x9C0E, "X = control byte for range checks", inline=True)
comment(0x9C0F, "Y=1: port byte offset", inline=True)
comment(0x9C10, "Load port byte from TX control block", inline=True)
comment(0x9C12, "Store port byte to TX scout buffer", inline=True)
comment(0x9C15, "Port != 0: skip immediate op setup", inline=True)
comment(0x9C17, "Ctrl < &83: PEEK/POKE need address calc", inline=True)
comment(0x9C19, "Ctrl >= &83: skip to range check", inline=True)
comment(0x9C1B, "SEC: init borrow for 4-byte subtract", inline=True)
comment(0x9C1C, "Save carry on stack for loop", inline=True)
comment(0x9C1D, "Y=8: high pointer offset in TXCB", inline=True)
label(0x9C1F, "calc_peek_poke_size")   # 4-byte subtraction for PEEK/POKE transfer size
comment(0x9C1F, "Load TXCB[Y] (end addr byte)", inline=True)
comment(0x9C21, "Y -= 4: back to start addr offset", inline=True)
comment(0x9C25, "Restore borrow from stack", inline=True)
comment(0x9C26, "end - start = transfer size byte", inline=True)
comment(0x9C28, "Store result to tx_data_start", inline=True)
comment(0x9C30, "Save borrow for next byte", inline=True)
comment(0x9C31, "Done all 4 bytes? (Y reaches &0C)", inline=True)
comment(0x9C33, "No: next byte pair", inline=True)
comment(0x9C35, "Discard final borrow", inline=True)
comment(0x9C36, "Ctrl >= &89: out of immediate range", inline=True)
comment(0x9C38, "Above range: normal data transfer", inline=True)
comment(0x9C3A, "Y=&0C: start of extra data in TXCB", inline=True)
label(0x9C3C, "copy_imm_params")      # Copy 4 extra parameter bytes from TXCB to NMI workspace
comment(0x9C3C, "Load extra parameter byte from TXCB", inline=True)
comment(0x9C3E, "Copy to NMI shim workspace at &0D1A+Y", inline=True)
comment(0x9C41, "Next byte", inline=True)
comment(0x9C42, "Done 4 bytes? (Y reaches &10)", inline=True)
comment(0x9C44, "No: continue copying", inline=True)
label(0x9C46, "tx_line_idle_check")   # BNE: port != 0, test SR2 INACTIVE before polling
comment(0x9C46, "A=&20: mask for SR2 INACTIVE bit", inline=True)
comment(0x9C48, "BIT SR2: test if line is idle", inline=True)
comment(0x9C4B, "Line not idle: handle as line jammed", inline=True)
comment(0x9C4D, "A=&FD: high byte of timeout counter", inline=True)
comment(0x9C4F, "Push timeout high byte to stack", inline=True)
comment(0x9C50, "Scout frame = 6 address+ctrl bytes", inline=True)
comment(0x9C52, "Store scout frame length", inline=True)
comment(0x9C55, "A=0: init low byte of timeout counter", inline=True)
label(0x9C5E, "test_inactive_retry")   # Reload INACTIVE mask and retry polling
label(0x9C7C, "inactive_retry")       # BEQ: INACTIVE not set, re-enable NMIs/retry
comment(0x9C99, "Write CR2 to abort TX", inline=True)
comment(0x9C9C, "Clean 3 bytes of timeout loop state", inline=True)
comment(0x9CA1, "ALWAYS branch to shared error handler", inline=True)
label(0x9CA3, "tx_no_clock_error")   # Error code &43: "No Clock"
comment(0x9CA3, "Error &43 = 'No Clock'", inline=True)
label(0x9CA5, "store_tx_error")      # Store error code to TX control block
comment(0x9CA5, "Offset 0 = error byte in TX control block", inline=True)
comment(0x9CA7, "Store error code in TX CB byte 0", inline=True)
comment(0x9CA9, "&80 = TX complete flag", inline=True)
comment(0x9CAB, "Signal TX operation complete", inline=True)
comment(0x9CAE, "Restore X saved by caller", inline=True)
comment(0x9CAF, "Move to X register", inline=True)
comment(0x9CB0, "Return to TX caller", inline=True)
comment(0x9CB6, "Write to ADLC CR1", inline=True)
comment(0x9CB9, "Install NMI handler at &9CCC (nmi_tx_data)", inline=True)
comment(0x9CBB, "High byte of NMI handler address", inline=True)
comment(0x9CBD, "Write NMI vector low byte directly", inline=True)
comment(0x9CC0, "Write NMI vector high byte directly", inline=True)
comment(0x9CC6, "Load destination port number", inline=True)
comment(0x9CC9, "Port != 0: standard data transfer", inline=True)
comment(0x9CCB, "Port 0: load control byte for table lookup", inline=True)
comment(0x9CCE, "Look up tx_flags from table", inline=True)
comment(0x9CD1, "Store operation flags", inline=True)
comment(0x9CD4, "Look up tx_length from table", inline=True)
comment(0x9CD7, "Store expected transfer length", inline=True)
subroutine(0x9D0F, hook=None,
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="""\
Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")
label(0x9D25, "setup_data_xfer")       # Configure scout length and flags for data transfer
comment(0x9D25, "Load dest station for broadcast check", inline=True)
comment(0x9D28, "AND with dest network", inline=True)
comment(0x9D2B, "Both &FF = broadcast address?", inline=True)
comment(0x9D2D, "Not broadcast: unicast path", inline=True)
comment(0x9D2F, "Broadcast scout: 14 bytes total", inline=True)
comment(0x9D31, "Store broadcast scout length", inline=True)
comment(0x9D34, "A=&40: broadcast flag", inline=True)
comment(0x9D36, "Set broadcast flag in tx_flags", inline=True)
comment(0x9D39, "Y=4: start of address data in TXCB", inline=True)
label(0x9D3B, "copy_bcast_addr")      # Copy 8-byte broadcast address data into TX scout buffer
comment(0x9D3B, "Copy TXCB address bytes to scout buffer", inline=True)
comment(0x9D3D, "Store to TX source/data area", inline=True)
comment(0x9D40, "Next byte", inline=True)
comment(0x9D41, "Done 8 bytes? (Y reaches &0C)", inline=True)
comment(0x9D43, "No: continue copying", inline=True)
label(0x9D47, "setup_unicast_xfer")   # BNE: not broadcast, clear flags/scout_status=2
comment(0x9D47, "A=0: clear flags for unicast", inline=True)
comment(0x9D49, "Clear tx_flags", inline=True)
comment(0x9D4C, "scout_status=2: data transfer pending", inline=True)
comment(0x9D4E, "Store scout status", inline=True)
comment(0x9D51, "Calculate transfer size from RXCB", inline=True)
comment(0x9D54, "Restore processor status from stack", inline=True)
comment(0x9D55, "Restore stacked registers (4 PLAs)", inline=True)
comment(0x9D56, "Second PLA", inline=True)
comment(0x9D57, "Third PLA", inline=True)
comment(0x9D58, "Fourth PLA", inline=True)
comment(0x9D59, "Restore X from A", inline=True)
comment(0x9D5A, "Return to caller", inline=True)
label(0x9D61, "tx_fifo_write")        # NMI TX loop: write 2 bytes per iteration to ADLC FIFO
label(0x9D85, "tx_fifo_not_ready")    # BVC: TDRA clear, write CR2=&67, error &41
label(0x9D8C, "tx_store_error")       # BNE: error &42 path, merge with &9CF6
label(0x9D8F, "delay_nmi_disable")    # PHA/PLA delay loop after INTOFF before storing TX result
comment(0x9D99, "Write to ADLC CR2", inline=True)
comment(0x9D9C, "Install NMI handler at &9D14 (nmi_tx_complete)", inline=True)
comment(0x9D9E, "High byte of handler address", inline=True)
comment(0x9DA0, "Install and return via set_nmi_vector", inline=True)
label(0x9DB0, "check_handshake_bit")  # BVC: tx_flags bit6 clear, check bit0
label(0x9DBA, "install_reply_scout")  # BEQ: handshake bit0 clear, install nmi_reply_scout
comment(0x9DBA, "Install nmi_reply_scout at &9D30", inline=True)
comment(0x9DC8, "Read first RX byte (destination station)", inline=True)
comment(0x9DD0, "Install nmi_reply_cont at &9D44", inline=True)
comment(0x9DE1, "Install nmi_reply_validate at &9D5B", inline=True)
comment(0x9DE8, "IRQ set -- fall through to &9D5B without RTI", inline=True)
label(0x9DEF, "reject_reply")          # Reject invalid reply scout frame
comment(0x9E10, "Write CR2: enable RTS for TX handshake", inline=True)
comment(0x9E15, "Write CR1: reset RX, enable TX interrupt", inline=True)
comment(0x9E18, "Save handshake_await_ack (&9E50) in &0D4B/&0D4C", inline=True)
comment(0x9E1A, "High byte &9E of next handler address", inline=True)
comment(0x9E1C, "Store low byte to nmi_next_lo", inline=True)
comment(0x9E1F, "Store high byte to nmi_next_hi", inline=True)
comment(0x9E2D, "Load dest network for scout ACK TX", inline=True)
comment(0x9E30, "Write dest network to TX FIFO", inline=True)
comment(0x9E33, "Install nmi_scout_ack_src at &9DA3", inline=True)
comment(0x9E35, "High byte &9D of handler address", inline=True)
comment(0x9E37, "Set NMI vector and return", inline=True)
comment(0x9E3A, "Read our station ID (also INTOFF)", inline=True)
comment(0x9E3D, "BIT SR1: check TDRA before writing", inline=True)
comment(0x9E40, "TDRA not ready: TX error", inline=True)
comment(0x9E45, "Network = 0 (local network)", inline=True)
comment(0x9E47, "Write network byte to TX FIFO", inline=True)
comment(0x9E4A, "Test bit 1 of tx_flags", inline=True)
comment(0x9E4C, "Check if immediate-op or data-transfer", inline=True)
comment(0x9E4F, "Bit 1 set: immediate op, use alt handler", inline=True)
comment(0x9E51, "Install nmi_data_tx at &9DC8", inline=True)
comment(0x9E53, "High byte of handler address", inline=True)
comment(0x9E55, "Install and return via set_nmi_vector", inline=True)
label(0x9E58, "install_imm_data_nmi")  # BNE: tx_flags bit1 set, install nmi_imm_data
comment(0x9E58, "Install nmi_imm_data at &9E0F", inline=True)
comment(0x9E5A, "High byte of handler address", inline=True)
comment(0x9E5C, "Install and return via set_nmi_vector", inline=True)
label(0x9E64, "data_tx_check_fifo")   # Test TDRA and write data byte pair to FIFO
comment(0x9E68, "Write first byte of pair to FIFO", inline=True)
comment(0x9E6B, "Advance buffer offset", inline=True)
comment(0x9E6C, "No page crossing", inline=True)
comment(0x9E6E, "Page crossing: decrement page count", inline=True)
comment(0x9E70, "No pages left: send last data", inline=True)
comment(0x9E72, "Increment buffer high byte", inline=True)
label(0x9E74, "write_second_tx_byte") # BNE: skip page check, write second FIFO byte
comment(0x9E74, "Load second byte of pair", inline=True)
comment(0x9E76, "Write second byte to FIFO", inline=True)
comment(0x9E79, "Advance buffer offset", inline=True)
comment(0x9E7A, "Save updated buffer position", inline=True)
comment(0x9E7C, "No page crossing", inline=True)
comment(0x9E7E, "Page crossing: decrement page count", inline=True)
comment(0x9E80, "No pages left: send last data", inline=True)
comment(0x9E82, "Increment buffer high byte", inline=True)
label(0x9E84, "check_irq_loop")       # BNE: skip page check, test SR1 IRQ for loop
comment(0x9E84, "BIT SR1: test IRQ (N=bit7) for tight loop", inline=True)
comment(0x9E87, "IRQ still set: write 2 more bytes", inline=True)
comment(0x9E89, "No IRQ: return, wait for next NMI", inline=True)
comment(0x9E8E, "Write CR2 to close frame", inline=True)
comment(0x9E91, "Check tx_flags for next action", inline=True)
comment(0x9E94, "Bit7 clear: error, install saved handler", inline=True)
comment(0x9E96, "Install discard_reset_listen at &99DB", inline=True)
comment(0x9E98, "High byte of &99DB handler", inline=True)
comment(0x9E9A, "Set NMI vector and return", inline=True)
comment(0x9E9D, "Load saved next handler low byte", inline=True)
comment(0x9EAD, "Load saved next handler high byte", inline=True)
comment(0x9EB0, "Install saved handler and return", inline=True)
comment(0x9EB3, "Tube TX: BIT SR1 test TDRA", inline=True)
label(0x9EB6, "tube_tx_fifo_write")    # BMI: IRQ set, Tube TX FIFO write entry point
comment(0x9EB6, "TDRA not ready -- error", inline=True)
comment(0x9EB8, "Read byte from Tube R3", inline=True)
comment(0x9EBB, "Write to TX FIFO", inline=True)
comment(0x9EBE, "Increment 4-byte buffer counter", inline=True)
comment(0x9EC0, "Low byte didn't wrap", inline=True)
comment(0x9EC2, "Carry into second byte", inline=True)
comment(0x9EC4, "No further carry", inline=True)
comment(0x9EC6, "Carry into third byte", inline=True)
comment(0x9EC8, "No further carry", inline=True)
comment(0x9ECA, "Carry into fourth byte", inline=True)
comment(0x9ECC, "Counter wrapped to zero: last data", inline=True)
label(0x9ECE, "write_second_tube_byte") # BNE: skip carry, read/write second Tube byte
comment(0x9ECE, "Read second Tube byte from R3", inline=True)
comment(0x9ED1, "Write second byte to TX FIFO", inline=True)
comment(0x9ED4, "Increment 4-byte counter (second byte)", inline=True)
comment(0x9ED6, "Low byte didn't wrap", inline=True)
comment(0x9ED8, "Carry into second byte", inline=True)
comment(0x9EDA, "No further carry", inline=True)
label(0x9EDC, "tube_tx_inc_byte3")    # Tube TX buffer counter byte 3 increment
comment(0x9EDC, "Carry into third byte", inline=True)
comment(0x9EDE, "No further carry", inline=True)
comment(0x9EE0, "Carry into fourth byte", inline=True)
comment(0x9EE2, "Counter wrapped to zero: last data", inline=True)
label(0x9EE4, "check_tube_irq_loop")  # BNE: skip carry, test SR1 IRQ for loop
comment(0x9EE4, "BIT SR1: test IRQ for tight loop", inline=True)
comment(0x9EE7, "IRQ still set: write 2 more bytes", inline=True)
comment(0x9EE9, "No IRQ: return, wait for next NMI", inline=True)
comment(0x9EEE, "Write to ADLC CR1", inline=True)
comment(0x9EF1, "Install nmi_final_ack at &9E5C", inline=True)
comment(0x9EF3, "High byte of handler address", inline=True)
comment(0x9EF5, "Install and return via set_nmi_vector", inline=True)
comment(0x9F07, "Install nmi_final_ack_net at &9E70", inline=True)
comment(0x9F18, "Install nmi_final_ack_validate at &9E84", inline=True)
comment(0x9F1F, "IRQ set -- fall through to &9E84 without RTI", inline=True)
label(0x9F41, "check_fv_final_ack")    # BPL: tx_flags bit7 clear, test FV for frame end
subroutine(0x9F4C, "tx_result_fail", hook=None,
    title="TX failure: not listening",
    description="""\
Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")
comment(0x9F4C, "A=&41: not listening error code", inline=True)
comment(0x9F75, "Tube transfer in progress?", inline=True)
label(0x9F86, "calc_transfer_size")    # 4-byte subtraction to calculate actual bytes received
comment(0x9F9B, "A = saved X", inline=True)
comment(0x9F9C, "Save X", inline=True)
label(0x9FB3, "restore_x_and_return") # BCC: Tube not claimed, restore X/RTS
label(0x9FB6, "fallback_calc_transfer") # BEQ: no buffer/Tube, simple 2-byte subtract
comment(0x9FB6, "Y=4: RXCB current pointer offset", inline=True)
comment(0x9FBA, "Y=8: RXCB start address offset", inline=True)
comment(0x9FBC, "Set carry for subtraction", inline=True)
comment(0x9FC1, "Y=5: current ptr hi offset", inline=True)
comment(0x9FC5, "Propagate borrow from lo subtraction", inline=True)
comment(0x9FC7, "Temp store adjusted current ptr hi", inline=True)
comment(0x9FC9, "Y=8: start address lo offset", inline=True)
comment(0x9FCB, "Load RXCB[8] (start ptr lo)", inline=True)
comment(0x9FCD, "Store to scratch (side effect)", inline=True)
comment(0x9FCF, "Y=9: start address hi offset", inline=True)
comment(0x9FD1, "Load RXCB[9] (start ptr hi)", inline=True)
comment(0x9FD3, "Set carry for subtraction", inline=True)
comment(0x9FD4, "start_hi - adjusted current_hi", inline=True)
comment(0x9FDA, "INTOFF: disable NMIs while switching ROM", inline=True)
comment(0x9FDD, "Save A", inline=True)
comment(0x9FDE, "Transfer Y to A", inline=True)
comment(0x9FDF, "Save Y (via A)", inline=True)
comment(0x9FE0, "ROM bank 0 (patched during init for actual bank)", inline=True)
comment(0x9FE2, "Select Econet ROM bank via ROMSEL", inline=True)
comment(0x9FE5, "Jump to scout handler in ROM", inline=True)
comment(0x9FE8, "Store handler high byte at &0D0D", inline=True)
comment(0x9FEB, "Store handler low byte at &0D0C", inline=True)
comment(0x9FEE, "Restore NFS ROM bank", inline=True)
comment(0x9FF0, "Page in via hardware latch", inline=True)
comment(0x9FF3, "Restore Y from stack", inline=True)
comment(0x9FF5, "Restore A from stack", inline=True)
comment(0x9FF6, "INTON: re-enable NMIs", inline=True)
comment(0x9FF9, "Return from interrupt", inline=True)
# ============================================================

# ============================================================
# Annotations back-propagated from NFS 3.40
# ============================================================
label(0x0020, "tube_send_zero_r2")    # Sends zero prefix via R2 to Tube
label(0x045C, "flush_r3_nmi_check")   # BIT R3 twice to flush, check NMI
comment(0x8273, "Y=&82: ROM page high byte", inline=True)
comment(0x8275, "Execute command string at (X, Y)", inline=True)
label(0x84FD, "fs_reply_poll")        # Poll for FS reply with timeout/escape
comment(0x859C, "X to os_text_ptr (text ptr lo)", inline=True)
comment(0x859E, "Y to os_text_ptr hi", inline=True)
comment(0x85A0, "X to FS command ptr lo", inline=True)
comment(0x85A3, "Y to FS command ptr hi", inline=True)
comment(0x85A6, "A = function code / command", inline=True)
comment(0x85A8, "X = control block ptr lo", inline=True)
comment(0x85AA, "Y = control block ptr hi", inline=True)
comment(0x85AC, "X dup for indexed access via (fs_crc)", inline=True)
comment(0x85AE, "Y dup for indexed access", inline=True)
comment(0x85B0, "Return", inline=True)
comment(0x8660, "X=&C0: TX control block at &00C0", inline=True)
comment(0x8662, "Set TX pointer lo", inline=True)
comment(0x8664, "X=0: page zero", inline=True)
comment(0x8666, "Set TX pointer hi", inline=True)
comment(0x866C, "Save retry count on stack", inline=True)
comment(0x866D, "Transfer timeout to A", inline=True)
comment(0x866E, "Save timeout on stack", inline=True)
comment(0x866F, "X=0 for (net_tx_ptr,X) indirect", inline=True)
comment(0x8671, "Load TXCB byte 0 (control/status)", inline=True)
label(0x8673, "tx_retry")             # Retry TX after error
comment(0x8673, "Write control byte to start TX", inline=True)
comment(0x8675, "Save control byte for retry", inline=True)
label(0x8676, "tx_semaphore_spin")    # TX semaphore spinlock
comment(0x8676, "Test TX semaphore (C=1 when free)", inline=True)
comment(0x8679, "Spin until semaphore released", inline=True)
comment(0x867B, "Copy TX ptr lo to NMI block", inline=True)
comment(0x867D, "Store for NMI handler access", inline=True)
comment(0x867F, "Copy TX ptr hi to NMI block", inline=True)
comment(0x8681, "Store for NMI handler access", inline=True)
comment(0x8683, "Initiate ADLC TX via trampoline", inline=True)
comment(0x8686, "Poll TXCB byte 0 for completion", inline=True)
comment(0x8688, "Bit 7 set: still busy, keep polling", inline=True)
comment(0x868A, "Shift bit 6 into bit 7 (error flag)", inline=True)
comment(0x868B, "Bit 6 clear: success, clean return", inline=True)
comment(0x868D, "Shift bit 5 into carry", inline=True)
comment(0x868E, "Zero: fatal error, no escape", inline=True)
comment(0x8690, "Check for user escape condition", inline=True)
comment(0x8693, "Discard saved control byte", inline=True)
comment(0x8694, "Save to X for retry delay", inline=True)
comment(0x8695, "Restore timeout parameter", inline=True)
comment(0x8696, "Back to Y", inline=True)
comment(0x8697, "Restore retry count", inline=True)
comment(0x8698, "No retries left: report error", inline=True)
comment(0x869A, "Decrement retry count", inline=True)
comment(0x869C, "Save updated retry count", inline=True)
comment(0x869D, "Timeout to A for delay", inline=True)
comment(0x869E, "Save timeout parameter", inline=True)
comment(0x869F, "Control byte for delay duration", inline=True)
label(0x86A0, "msdely")               # DNFS: MSDELY — delay loop
comment(0x86A0, "Inner delay loop", inline=True)
comment(0x86A1, "Spin until X=0", inline=True)
comment(0x86A3, "Outer delay loop", inline=True)
comment(0x86A4, "Continue delay", inline=True)
label(0x86A8, "tx_not_listening")     # Fatal TX error: "Not listening"
comment(0x86A8, "Save error code in X", inline=True)
comment(0x86A9, "Report 'Not listening' error", inline=True)
label(0x86AC, "tx_success")           # TX success: clean return
comment(0x86AC, "Discard saved control byte", inline=True)
comment(0x86AD, "Discard timeout parameter", inline=True)
comment(0x86AE, "Discard retry count", inline=True)
comment(0x86AF, "Return (success)", inline=True)
label(0x87B4, "send_fs_reply")        # Sends FS reply command after transfer
label(0x87C4, "copy_attr_loop")       # Copy 4 attribute bytes loop
label(0x87C7, "direct_attr_copy")     # Skip attr decode, direct copy
label(0x87FB, "next_block")           # Reinit for next transfer block
label(0x8806, "block_addr_loop")      # Multi-byte address addition loop
label(0x8824, "clamp_dest_setup")     # Set up 4-byte dest clamping
label(0x8D03, "next_filename_char")   # Load and print next filename char
comment(0x8D03, "Load next filename character", inline=True)
comment(0x8D05, "CR: end of filename", inline=True)
comment(0x8D07, "CR found: pad remaining with spaces", inline=True)
comment(0x8D09, "Space: end of name field", inline=True)
comment(0x8D0B, "Space found: pad with spaces", inline=True)
comment(0x8D10, "Advance to next character", inline=True)
comment(0x8D11, "Continue printing filename", inline=True)
comment(0x8D13, "Print space for padding", inline=True)
comment(0x8D16, "Advance column counter", inline=True)
comment(0x8D17, "Reached 12 columns?", inline=True)
comment(0x8D19, "No: continue padding", inline=True)
label(0x8D1B, "print_hex_fields")     # Print load/exec/length fields
comment(0x8D1B, "Y=5: load address offset (4 bytes)", inline=True)
comment(0x8D1D, "Print load address", inline=True)
comment(0x8D20, "Print exec address and file length", inline=True)
label(0x8D23, "print_newline")        # JMP OSNEWL after catalogue line
comment(0x8D26, "Y=9: exec address offset (4 bytes)", inline=True)
comment(0x8D28, "Print exec address", inline=True)
comment(0x8D2B, "Y=&0C: file length offset", inline=True)
comment(0x8D2D, "X=3: print 3 bytes (24-bit length)", inline=True)
label(0x8E12, "exec_at_load_addr")    # JMP (fs_load_vector) — execute locally
label(0x9109, "poll_rxcb_loop")       # Poll RXCB for OSBYTE reply
label(0x918B, "rxcb_matched")         # Scout frame matched RXCB
label(0x9216, "pril1")                # DNFS: PRIL1 — print/store loop
label(0x96BE, "nmi_vec_lo_match")     # NMI vector low byte matches
comment(0x96CF, "INTOFF: disable NMIs", inline=True)
label(0x96E3, "enter_rx_listen")      # JMP adlc_rx_listen (idle RX mode)
comment(0x96E3, "Re-enter idle RX listen mode", inline=True)
comment(0x96E8, "Write CR1: full reset", inline=True)
comment(0x96EB, "CR4=&1E: 8-bit word, abort ext, NRZ", inline=True)
comment(0x96ED, "Write CR4 via ADLC reg 3 (AC=1)", inline=True)
comment(0x96F2, "Write CR3=0: clear loop-back/AEX/DTR", inline=True)
label(0x97BD, "scout_ctrl_check")     # Check scout control byte
label(0x97D9, "scout_port_match")     # Check scout port number
label(0x97EA, "scout_station_check")  # Check scout station number
label(0x97EE, "scout_network_match")  # Check scout network number
label(0x97FD, "scout_accept")         # Scout accepted: all checks passed
label(0x9805, "ack_scout_match")      # Sets scout_status=3, initiates ACK
label(0x991C, "rx_update_buf")        # Update buffer pointer after RX
label(0x9932, "rx_check_error")       # Check error status after data RX
label(0x9A1F, "inc_rxcb_buf_hi")      # Increments RXCB buffer high byte
label(0x9A28, "store_rxcb_buf_hi")    # Stores buffer hi byte to RXCB offset 9
label(0x9A60, "copy_scout_fields")    # Copies scout fields to port workspace
comment(0x9A60, "Y=4: start at RX CB offset 4", inline=True)
label(0x9A62, "copy_scout_loop")      # Copy 8 scout fields to workspace
comment(0x9A62, "Load scout field (stn/net/ctrl/port)", inline=True)
comment(0x9A65, "Store to port workspace buffer", inline=True)
comment(0x9A67, "Next field", inline=True)
comment(0x9A68, "All 8 fields copied?", inline=True)
comment(0x9A6A, "No: continue copy loop", inline=True)
comment(0x9A6C, "Skip buffer pointer update", inline=True)
label(0x9A96, "imm_op_dispatch")      # PHA/PHA/RTS dispatch for immediate ops
label(0x9AA2, "imm_op_out_of_range")  # JMP nmi_error_dispatch
comment(0x9AB5, "Buffer start lo = &00", inline=True)
comment(0x9AB7, "Set port buffer lo", inline=True)
comment(0x9AB9, "Buffer length lo = &82", inline=True)
comment(0x9ABB, "Set buffer length lo", inline=True)
comment(0x9ABD, "Buffer length hi = 1", inline=True)
comment(0x9ABF, "Set buffer length hi", inline=True)
comment(0x9AC1, "Load RX page hi for buffer", inline=True)
comment(0x9AC3, "Set port buffer hi", inline=True)
comment(0x9AC5, "Y=3: copy 4 bytes (3 down to 0)", inline=True)
label(0x9AC7, "copy_addr_loop")       # Copy 4-byte remote address loop
comment(0x9AC7, "Load remote address byte", inline=True)
comment(0x9ACA, "Store to exec address workspace", inline=True)
comment(0x9ACD, "Next byte (descending)", inline=True)
comment(0x9ACE, "Loop until all 4 bytes copied", inline=True)
comment(0x9AD0, "Enter common data-receive path", inline=True)
comment(0x9AD3, "Port workspace offset = &3D", inline=True)
comment(0x9AD5, "Store workspace offset lo", inline=True)
comment(0x9AD7, "RX buffer page = &0D", inline=True)
comment(0x9AD9, "Store workspace offset hi", inline=True)
comment(0x9ADB, "Enter POKE data-receive path", inline=True)
comment(0x9ADE, "Buffer length hi = 1", inline=True)
comment(0x9AE0, "Set buffer length hi", inline=True)
comment(0x9AE2, "Buffer length lo = &FC", inline=True)
comment(0x9AE4, "Set buffer length lo", inline=True)
comment(0x9AE6, "Buffer start lo = &25", inline=True)
comment(0x9AE8, "Set port buffer lo", inline=True)
comment(0x9AEA, "Buffer hi = &7F (below screen)", inline=True)
comment(0x9AEC, "Set port buffer hi", inline=True)
comment(0x9AEE, "Enter reply build path", inline=True)
comment(0x9AF7, "Port workspace offset = &3D", inline=True)
comment(0x9AF9, "Store workspace offset lo", inline=True)
comment(0x9AFB, "RX buffer page = &0D", inline=True)
comment(0x9AFD, "Store workspace offset hi", inline=True)
comment(0x9AFF, "Scout status = 2 (PEEK response)", inline=True)
comment(0x9B01, "Store scout status", inline=True)
comment(0x9B04, "Calculate transfer size for response", inline=True)
comment(0x9B0D, "C=0: transfer not set up, discard", inline=True)
label(0x9B0F, "set_tx_reply_flag")    # Sets TX reply-pending flag (bit7)
comment(0x9B0F, "Mark TX flags bit 7 (reply pending)", inline=True)
comment(0x9B12, "Set reply pending flag", inline=True)
comment(0x9B14, "Store updated TX flags", inline=True)
label(0x9B17, "rx_imm_halt_cont")     # Handler for HALT/CONTINUE immediate ops
comment(0x9B17, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
comment(0x9B19, "Write CR1: enable TX interrupts", inline=True)
label(0x9B1C, "tx_cr2_setup")         # Self-modifying CR2 configuration
comment(0x9B1C, "NMI handler hi byte (self-modifying)", inline=True)
comment(0x9B1E, "Write CR2 for TX setup", inline=True)
label(0x9B21, "tx_nmi_setup")         # Self-modifying NMI handler lo byte
comment(0x9B21, "NMI handler lo byte (self-modifying)", inline=True)
comment(0x9B23, "Y=&9B: dispatch table page", inline=True)
comment(0x9B25, "Acknowledge and write TX dest", inline=True)
label(0x9B5E, "imm_op_discard")       # Error path: JMP discard_listen
label(0x9B61, "check_cb1_irq")        # Tests CB1 interrupt pending via IFR
comment(0x9B61, "A=&04: IFR bit 2 (CB1) mask", inline=True)
comment(0x9B63, "Test CB1 interrupt pending", inline=True)
comment(0x9B66, "CB1 fired: handle TX completion", inline=True)
comment(0x9B68, "A=5: no CB1, return status 5", inline=True)
comment(0x9B6A, "Return (no CB1 interrupt)", inline=True)
label(0x9B6B, "tx_done_error")        # TX error code check
comment(0x9B6B, "Save X", inline=True)
comment(0x9B6C, "Push X", inline=True)
comment(0x9B6D, "Save Y", inline=True)
comment(0x9B6E, "Push Y", inline=True)
comment(0x9B6F, "Read ACR for shift register mode", inline=True)
comment(0x9B72, "Clear SR mode bits (2-4)", inline=True)
comment(0x9B74, "Restore original SR mode", inline=True)
comment(0x9B77, "Write updated ACR", inline=True)
comment(0x9B7A, "Read SR to clear pending interrupt", inline=True)
comment(0x9B7D, "A=&04: CB1 bit mask", inline=True)
comment(0x9B7F, "Clear CB1 in IFR", inline=True)
comment(0x9B82, "Disable CB1 in IER", inline=True)
comment(0x9B85, "Load ctrl byte for dispatch", inline=True)
comment(0x9B88, "Ctrl >= &86? (HALT/CONTINUE)", inline=True)
comment(0x9B8A, "Yes: skip protection mask save", inline=True)
comment(0x9B8C, "Load current protection mask", inline=True)
comment(0x9B8F, "Save mask before JSR modification", inline=True)
comment(0x9B92, "Enable bits 2-4 (allow JSR ops)", inline=True)
comment(0x9B94, "Store modified protection mask", inline=True)
label(0x9B97, "tx_done_classify")     # TX operation type classification
comment(0x9B97, "Load handler addr hi from table", inline=True)
comment(0x9B9A, "Push handler hi", inline=True)
comment(0x9B9B, "Load handler addr lo from table", inline=True)
comment(0x9B9E, "Push handler lo", inline=True)
comment(0x9B9F, "Dispatch via RTS (addr-1 on stack)", inline=True)
comment(0x9BAA, "Push hi of (tx_done_exit-1)", inline=True)
comment(0x9BAC, "Push hi byte on stack", inline=True)
comment(0x9BAD, "Push lo of (tx_done_exit-1)", inline=True)
comment(0x9BAF, "Push lo byte on stack", inline=True)
comment(0x9BB0, "Call remote JSR; RTS to tx_done_exit", inline=True)
comment(0x9BB3, "Y=8: network event type", inline=True)
comment(0x9BB5, "X = remote address lo", inline=True)
comment(0x9BB8, "A = remote address hi", inline=True)
comment(0x9BBE, "Exit TX done handler", inline=True)
comment(0x9BC1, "X = remote address lo", inline=True)
comment(0x9BC4, "Y = remote address hi", inline=True)
comment(0x9BC7, "Call ROM entry point at &8000", inline=True)
comment(0x9BCA, "Exit TX done handler", inline=True)
comment(0x9BCD, "A=&04: bit 2 mask for rx_flags", inline=True)
comment(0x9BCF, "Test if already halted", inline=True)
comment(0x9BD2, "Already halted: skip to exit", inline=True)
comment(0x9BD4, "Set bit 2 in rx_flags", inline=True)
comment(0x9BD7, "Store halt flag", inline=True)
comment(0x9BDA, "A=4: re-load halt bit mask", inline=True)
comment(0x9BDC, "Enable interrupts during halt wait", inline=True)
label(0x9BDD, "halt_spin_loop")       # Spin-wait during system halt state
comment(0x9BDD, "Test halt flag", inline=True)
comment(0x9BE0, "Still halted: keep spinning", inline=True)
comment(0x9C57, "Save TX index", inline=True)
comment(0x9C5A, "Push timeout byte 1 on stack", inline=True)
comment(0x9C5B, "Push timeout byte 2 on stack", inline=True)
comment(0x9C60, "Save interrupt state", inline=True)
comment(0x9C61, "Disable interrupts for ADLC access", inline=True)
label(0x9C68, "test_line_idle")       # Tests SR2 INACTIVE bit for line idle
comment(0x9C72, "Write CR2: clear status, prepare TX", inline=True)
comment(0x9C7F, "Restore interrupt state", inline=True)
comment(0x9C81, "Increment timeout counter byte 1", inline=True)
comment(0x9C84, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C86, "Increment timeout counter byte 2", inline=True)
comment(0x9C89, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C8B, "Increment timeout counter byte 3", inline=True)
comment(0x9C8E, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C90, "All 3 bytes overflowed: line jammed", inline=True)
comment(0x9C93, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
label(0x9CF3, "imm_op_status3")       # Loads scout_status=3 for immediate ops
comment(0x9CFB, "Scout status = 2 (POKE transfer)", inline=True)
label(0x9CFD, "store_status_add4")    # Stores scout status + 4-byte addition
comment(0x9CFD, "Store scout status", inline=True)
comment(0x9D00, "Clear carry for 4-byte addition", inline=True)
comment(0x9D01, "Save carry on stack", inline=True)
comment(0x9D02, "Y=&0C: start at offset 12", inline=True)
label(0x9D04, "add_bytes_loop")       # 4-byte address addition loop
comment(0x9D04, "Load workspace address byte", inline=True)
comment(0x9D07, "Restore carry from previous byte", inline=True)
comment(0x9D08, "Add TXCB address byte", inline=True)
comment(0x9D0A, "Store updated address byte", inline=True)
comment(0x9D0D, "Next byte", inline=True)
comment(0x9D0E, "Save carry for next addition", inline=True)
label(0x9D4C, "proc_op_status2")      # Loads scout_status=2 for proc calls
label(0x9D4E, "store_status_copy_ptr")  # Stores status + copies TX block ptr
label(0x9EA7, "jmp_tx_result_fail")   # JMP tx_result_fail
label(0x9ED8, "tube_tx_inc_byte2")    # Increment byte 2 of 4-byte counter
label(0x9EE0, "tube_tx_inc_byte4")    # Increment byte 4 of 4-byte counter

# ============================================================
# Label renames and subroutine promotions: 3.35K-specific
# ============================================================

# --- Subroutine promotions (8) ---

label(0x0036, "tube_enter_main_loop")
subroutine(0x0036, hook=None,
    title="Save registers and enter Tube polling loop",
    description="""\
Saves X and Y to zp_temp_11/zp_temp_10, then falls through
to tube_main_loop which polls Tube R1 (WRCH) and R2 (command)
registers in an infinite loop. Called from tube_init_reloc
after ROM relocation and from tube_dispatch_table handlers
that need to restart the main loop.""")

label(0x8EA9, "copy_param_byte")
subroutine(0x8EA9, hook=None,
    title="Copy one byte between OSWORD param block and workspace",
    description="""\
If C=1, copies one byte from (osword_pb_ptr),Y to
(fs_crc_lo),Y (param to workspace). Always loads the
workspace byte into A. Used as the inner body of
copy_param_block's bidirectional copy loop, and called
directly by OSWORD &0F/&10/&11 handlers to set up or
retrieve workspace data.""")

label(0x8EF7, "osword_12_dispatch")
subroutine(0x8EF7, hook=None,
    title="OSWORD &12 sub-function dispatch",
    description="""\
Dispatches OSWORD &12 sub-functions 0-9. Sub-functions 0-3
read or write workspace paths (static page &0D or dynamic
workspace). Sub-functions 4/5 read/set the JSR protection
status byte. Sub-function 8 reads the FS handle from the
RX buffer. Sub-function 9 reads ARGS buffer size info.
Sub-functions >= 6 and unrecognised codes are handled
via the shared rsl1 error path.""")

label(0x90AA, "nwrch_handler")
subroutine(0x90AA, hook=None,
    title="NETVEC reason 4: write character to network (NWRCH)",
    description="""\
Handles remote character output over the network. Clears
carry in the stacked processor status (via ROR/ASL on the
stack frame) to signal success to the MOS dispatcher.
Stores the character from Y into workspace offset &DA,
then falls through to setup_tx_and_send with A=0 to
transmit the character to the remote terminal.""")

label(0x913A, "remote_osword_handler")
subroutine(0x913A, hook=None,
    title="NETVEC reason 8: remote OSWORD handler (NWORD)",
    description="""\
Handles OSWORD 7 (sound) and OSWORD 8 (define envelope)
across the network. Copies up to 14 parameter bytes from
the RX buffer to workspace, tags the message as RWORD,
and transmits. Fire-and-forget: no return value is sent
back. Other OSWORD numbers are ignored.""")

label(0x96B1, "wait_nmi_ready")
subroutine(0x96B1, hook=None,
    title="Wait for NMI subsystem ready and save Econet state",
    description="""\
Clears the TX complete flag, then polls econet_init_flag
until the NMI subsystem reports initialised. Validates the
NMI jump vector points to the expected handler (&9700) by
polling nmi_jmp_lo/hi in a tight loop. Once validated,
disables NMIs via INTOFF and falls through to
save_econet_state. Called from save_vdu_state during
VDU state preservation.""")

label(0x96DC, "restore_econet_state")
subroutine(0x96DC, hook=None,
    title="Restore Econet TX state and re-enter RX listen",
    description="""\
Loads the saved tx_in_progress flag from RXCB offset 8
(previously stored by save_econet_state) and restores it.
Then jumps to init_nmi_workspace to re-initialise the NMI
handler and return to idle RX listen mode. Called from
save_vdu_state during VDU state restoration.""")

label(0x9A23, "store_rxcb_buf_ptr")  # Store updated buffer pointer pair to RXCB

# --- Shared tail renames (9) ---

label(0x0455, "release_claim_restart")  # Release Tube claim flag and restart main loop
label(0x8142, "restore_y_check_svc")   # Restore Y from temp, continue service dispatch
label(0x81FB, "restore_y_return")      # Restore Y from nfs_temp and return (unclaimed)
label(0x87B0, "setup_fs_reply_attrs")  # Set error ptr, send FS reply, decode attributes
label(0x8959, "argsv_dispatch_a")      # TAY then dispatch: A=0 returns FS#, A!=0 copies context
label(0x8DB0, "print_char_always")     # BNE print_digit (always taken)
label(0x96D9, "jmp_rx_listen")         # JMP adlc_rx_listen (tail-call to RX listen)
label(0x99C2, "tdra_error")            # JMP nmi_error_dispatch (TDRA not ready)
label(0x9D1C, "store_status_calc_xfer")  # Store scout_status, calculate transfer, exit

# --- Internal conditional renames (18) ---

# tube_code_page4 / tube_init_reloc / tube_dispatch_table
label(0x0426, "setup_data_transfer")   # Save (X,Y) as transfer addr, send type via R4
label(0x04CC, "send_rom_byte")         # Read byte from (zp_ptr),Y and send to Tube R3
label(0x0522, "poll_r2_reply")         # Poll Tube R2 status for co-processor reply
label(0x0535, "wrch_echo_reply")       # R2 ready: recover char, echo back, re-enter loop
label(0x055F, "send_reply_ok")         # Set no-error bit, encode carry, send reply via R2

# i_am_handler
label(0x8093, "store_station_net")     # Store parsed station (A) and network (X)
label(0x8099, "scan_for_colon")        # Scan command line for colon or CR terminator

# handle_bput_bget
label(0x8430, "check_exec_handle")     # Test if *EXEC handle matches error file

# check_escape_handler (BGETV EOF handling)
label(0x8544, "set_eof_flag")          # Load handle mask and set EOF hint flag
label(0x8549, "load_handle_mask")      # Load handle bitmask for return

# gbpbv_handler
label(0x8A97, "set_gbpb_error_ptr")    # Set error pointer (&2A) for GBPB retry

# fscv_5_cat
label(0x8C52, "cat_print_header")      # Display catalogue header (disc name, option, dirs)
label(0x8CB5, "cat_examine_loop")      # Send examine request and display entries

# cat_column_separator
label(0x8D73, "print_cr_separator")    # Print CR for column/line break

# copy_param_byte
label(0x8EAF, "load_workspace_byte")   # Load byte from workspace (C=0 skip-copy path)

# advance_rx_buffer_ptr
label(0x9A18, "add_buf_to_base")       # Add buffer length to base address (no Tube)

# tx_begin
label(0x9C36, "check_imm_range")       # Check if ctrl byte is in immediate op range

# nmi_data_tx
label(0x9EA5, "nmi_tx_not_listening")  # Store "not listening" error and exit

# Internal loop label renames (by parent subroutine)
# tube_init_reloc
label(0x04D1, "poll_r3_ready")         # Poll Tube R3 status until ready

# tube_code_page6 (tube_osgbpb)
label(0x0604, "read_gbpb_params")      # Read 13 OSGBPB param bytes from R2
label(0x061B, "send_gbpb_params")      # Send 13 updated OSGBPB params via R2

# i_am_handler
label(0x807D, "skip_iam_spaces")       # Skip leading spaces before station number

# init_vectors_and_copy
label(0x8107, "init_vector_loop")      # Read triplets from vector init table

# match_rom_string
label(0x81CE, "match_next_char")       # Compare next char against ROM string byte

# fscv_5_cat
label(0x8C7A, "print_option_char")     # Print next char of boot option name

# fsreply_4_notify_exec
label(0x8DDD, "gsread_scan_loop")      # Scan command string via GSREAD
label(0x8DE3, "skip_filename_spaces")  # Skip leading spaces in filename

# Data label renames (by parent subroutine/location)
# ROM header byte aliases (used by tube_init_reloc for indexed access)
label(0x8001, "lang_entry_lo")         # ROM language entry address low byte
label(0x8002, "lang_entry_hi")         # ROM language entry address high byte
label(0x8004, "svc_entry_lo")          # ROM service entry address low byte

# tube_enter_main_loop (tube_dispatch_cmd operand)
label(0x0055, "tube_dispatch_ptr_lo")  # JMP indirect low byte (self-modified)

# tube_code_page4 (transfer control bits table)
label(0x046B, "tube_xfer_ctrl_bits")   # Tube control register values per xfer type

# fs_cmd_match_table (second byte of table)
label(0x8BE5, "cmd_table_entry_1")     # Second byte of command match table

# advance_rx_buffer_ptr (store instruction operand)
label(0x9A24, "store_rxcb_byte")       # Operand of STA (port_ws_offset),Y
label(0x9A2C, "rx_port_operand")       # Operand of LDA rx_port in skip_buf_ptr

# NMI TX setup (self-modifying code operands)
label(0x9B1D, "tx_cr2_operand")        # CR2 value operand (self-modified)
label(0x9B22, "tx_nmi_lo_operand")     # NMI handler lo byte operand (self-modified)

# intoff_test_inactive (SR2 test operand)
label(0x9C6A, "sr2_test_operand")      # Operand of BIT SR2 in INACTIVE test

# nmi_data_tx (Tube TX counter increment targets)
label(0x9ED9, "tube_tx_byte2_operand")  # Operand of INC port_buf_len_hi
label(0x9EE1, "tube_tx_byte4_operand")  # Operand of INC open_port_buf_hi

# ============================================================
# Inline comments: gap-filling for 3.35K-specific code
# ============================================================

# --- tube_code_page4 (&0400): Tube host code page 4 ---
comment(0x0438, "Send claimed address via R4", inline=True)
comment(0x0453, "Discard return address (high byte)", inline=True)
comment(0x0454, "Discard return address (low byte)", inline=True)
comment(0x0455, "A=&80: reset claim flag sentinel", inline=True)
comment(0x0457, "Clear claim-in-progress flag", inline=True)
comment(0x045C, "Flush R3 data (first byte)", inline=True)
comment(0x045F, "Flush R3 data (second byte)", inline=True)
comment(0x0474, "Save processor status", inline=True)
comment(0x0475, "Save A on stack", inline=True)

# --- tube_init_reloc (&047A): Tube init relocated code ---
comment(0x04A4, "Restore A from stack", inline=True)
comment(0x04A5, "Restore processor status", inline=True)
comment(0x04A6, "Carry set: language entry (claim Tube)", inline=True)
comment(0x04A8, "X = A (preserved from entry)", inline=True)
comment(0x04A9, "Non-zero: check break type", inline=True)
comment(0x04AB, "A=0: acknowledge and return", inline=True)
comment(0x04AE, "X=0 for OSBYTE read", inline=True)
comment(0x04B0, "Y=&FF for OSBYTE read", inline=True)
comment(0x04B2, "OSBYTE &FD: read last break type", inline=True)
comment(0x04B8, "Soft break (0): skip ROM transfer", inline=True)
comment(0x04BA, "A=&FF: claim Tube for all operations", inline=True)
comment(0x04BC, "Claim Tube address via R4", inline=True)
comment(0x04BF, "Not claimed: retry until claimed", inline=True)
comment(0x04C1, "Transfer type 1 (parasite to host)", inline=True)
comment(0x04C3, "Set up Tube transfer parameters", inline=True)
comment(0x04C6, "Y=0: start at page boundary", inline=True)
comment(0x04C8, "Source ptr low = 0", inline=True)
comment(0x04CA, "X=&40: 64 pages (16KB) to transfer", inline=True)
comment(0x04CC, "Read byte from source address", inline=True)
comment(0x04CE, "Send byte to Tube via R3", inline=True)
comment(0x04D1, "Check R3 status", inline=True)
comment(0x04D4, "Not ready: wait for Tube", inline=True)
comment(0x04D6, "Next byte in page", inline=True)
comment(0x04D7, "More bytes in page: continue", inline=True)
comment(0x04D9, "Next source page", inline=True)
comment(0x04DB, "Decrement page counter", inline=True)
comment(0x04DC, "More pages: continue transfer", inline=True)
comment(0x04DE, "Transfer type 4 (host to parasite burst)", inline=True)
comment(0x04E0, "Y=0: low byte of param block ptr", inline=True)
comment(0x04E2, "X=&57: param block at &0057", inline=True)
comment(0x04E4, "Claim Tube and start transfer", inline=True)
comment(0x04E7, "R2 command: OSRDCH request", inline=True)
comment(0x04E9, "Send OSRDCH request to host", inline=True)
comment(0x04EC, "Jump to RDCH completion handler", inline=True)
comment(0x04EF, "Restore Y from saved value", inline=True)
comment(0x04F1, "Restore X from saved value", inline=True)
comment(0x04F3, "Read result byte from R2", inline=True)
comment(0x04F6, "Shift carry into C flag", inline=True)
comment(0x04F7, "Poll R2 status register", inline=True)
comment(0x04FA, "Bit 7 clear: R2 not ready, wait", inline=True)
comment(0x04FC, "Read byte from R2 data register", inline=True)
comment(0x04FF, "Return with byte in A", inline=True)

# --- fscv_6_shutdown (&8337): FS shutdown ---
comment(0x8339, "Load FS state byte at offset Y", inline=True)
comment(0x833C, "Store to workspace backup area", inline=True)
comment(0x833E, "Next byte down", inline=True)
comment(0x8341, "Loop for offsets &1D..&15", inline=True)
comment(0x8343, "A=&7B: printer driver going dormant", inline=True)

# --- scout_complete (&977B): Scout frame processing ---
comment(0x97B7, "A=0: no NFS workspace offset yet", inline=True)
comment(0x97B9, "Clear NFS workspace search flag", inline=True)
comment(0x97C5, "Y=1: advance to port byte in slot", inline=True)
comment(0x97EA, "Check if NFS workspace already searched", inline=True)
comment(0x97EC, "Already searched: no match found", inline=True)
comment(0x97F3, "Get NFS workspace page number", inline=True)
comment(0x97F5, "Mark NFS workspace as search target", inline=True)
comment(0x97F7, "Y=0: start at offset 0 in workspace", inline=True)
comment(0x97F9, "Reset slot pointer to start", inline=True)
comment(0x97FD, "Check broadcast flag (bit 6)", inline=True)
comment(0x9800, "Not broadcast: ACK and set up RX", inline=True)
comment(0x9802, "Broadcast: copy scout fields directly", inline=True)
comment(0x980A, "Save current TX block ptr (low)", inline=True)
comment(0x980C, "Push TX block low on stack", inline=True)
comment(0x980D, "Save current TX block ptr (high)", inline=True)
comment(0x980F, "Push TX block high on stack", inline=True)
comment(0x9810, "Use port slot as temp RXCB ptr (lo)", inline=True)
comment(0x9812, "Set RXCB low for tx_calc_transfer", inline=True)
comment(0x9814, "Use workspace page as temp RXCB (hi)", inline=True)
comment(0x9816, "Set RXCB high for tx_calc_transfer", inline=True)
comment(0x981B, "Restore original TX block (high)", inline=True)
comment(0x981C, "Restore TX block ptr (high)", inline=True)
comment(0x981E, "Restore original TX block (low)", inline=True)
comment(0x981F, "Restore TX block ptr (low)", inline=True)
comment(0x9821, "Transfer OK: send data ACK", inline=True)
comment(0x983E, "High byte of nmi_data_rx handler", inline=True)

# --- fscv_5_cat (&8C02): Catalogue display ---
comment(0x8C08, "Clear CRFLAG column counter", inline=True)
comment(0x8C38, "Load access level from FS reply", inline=True)
comment(0x8C46, "Skip past 'Owner' string", inline=True)
comment(0x8C6B, "Load boot option from FS workspace", inline=True)
comment(0x8C77, "Y = option name offset from table", inline=True)
comment(0x8C7A, "Load next char of option name", inline=True)
comment(0x8C7D, "Bit 7 set: end of name string", inline=True)
comment(0x8C8F, "X=&11: CSD name offset in reply", inline=True)
comment(0x8C91, "Print CSD name from reply buffer", inline=True)
comment(0x8C94, "Print '     Lib. ' header", inline=True)
comment(0x8CA1, "X=&1B: library name offset in reply", inline=True)
comment(0x8CA6, "Print two CRs (blank line)", inline=True)
comment(0x8CAB, "Init examine start offset to 0", inline=True)
comment(0x8CC7, "Zero entries returned: catalogue done", inline=True)
comment(0x8CC9, "X=2: first entry offset in reply", inline=True)
comment(0x8CCF, "Load current examine start offset", inline=True)
comment(0x8CD1, "Add entries returned this batch", inline=True)
comment(0x8CD4, "Update next examine start offset", inline=True)
comment(0x8CD7, "Save updated start offset", inline=True)
comment(0x8CD9, "Reload batch size for next request", inline=True)
comment(0x8CDB, "Store batch size in command buffer", inline=True)
comment(0x8CE0, "RTS doubles as offset table byte", inline=True)

# --- fsreply_4_notify_exec (&8DC5): Load-as-command ---
comment(0x8DD7, "Y=0: init GSINIT string offset", inline=True)
comment(0x8DD9, "CLC: no flags for GSINIT", inline=True)
comment(0x8DDA, "Init string scanning state", inline=True)
comment(0x8DDD, "Read next char via GSREAD", inline=True)
comment(0x8DE0, "More chars: continue scanning", inline=True)
comment(0x8DE2, "Back up Y to last valid char", inline=True)
comment(0x8DE3, "Advance past current position", inline=True)
comment(0x8DE4, "Read char from command line", inline=True)
comment(0x8DE6, "Is it a space?", inline=True)
comment(0x8DE8, "Skip leading spaces in filename", inline=True)
comment(0x8DEA, "CLC for pointer addition", inline=True)
comment(0x8DEB, "A = Y (offset past spaces)", inline=True)
comment(0x8DEC, "Add base pointer to get abs addr", inline=True)
comment(0x8DEE, "Store filename pointer (low)", inline=True)
comment(0x8DF1, "Load text pointer high byte", inline=True)
comment(0x8DF3, "Add carry from low byte addition", inline=True)
comment(0x8DF5, "Store filename pointer (high)", inline=True)
comment(0x8DF8, "SEC for address range test", inline=True)

# --- data_rx_complete (&98D8): Tube data RX path ---
# 4-byte Tube transfer counter increment (first byte)
comment(0x9909, "Advance Tube transfer byte count", inline=True)
comment(0x990E, "No overflow: read second byte", inline=True)
comment(0x9910, "Carry to transfer count byte 2", inline=True)
comment(0x9912, "No overflow: read second byte", inline=True)
comment(0x9914, "Carry to transfer count byte 3", inline=True)
comment(0x9916, "No overflow: read second byte", inline=True)
comment(0x9918, "Carry to transfer count byte 4", inline=True)
comment(0x991A, "All bytes zero: overflow error", inline=True)
# 4-byte Tube transfer counter increment (second byte)
comment(0x9922, "Advance count after second byte", inline=True)
comment(0x9924, "No overflow: check for more data", inline=True)
comment(0x9926, "Carry to count byte 2", inline=True)
comment(0x9928, "No overflow: check for more data", inline=True)
comment(0x992A, "Carry to count byte 3", inline=True)
comment(0x992C, "No overflow: check for more data", inline=True)
comment(0x992E, "Carry to count byte 4", inline=True)
comment(0x9937, "Return from NMI, wait for data", inline=True)

# --- tx_calc_transfer (&9F6A): Calculate transfer size ---
comment(0x9F6C, "Load RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x9F7A, "Load TX flags for transfer setup", inline=True)
comment(0x9F7F, "Store with bit 1 set (Tube xfer)", inline=True)
comment(0x9F89, "Y += 4: advance to high ptr offset", inline=True)
comment(0x9F8A, "(continued)", inline=True)
comment(0x9F8B, "(continued)", inline=True)
comment(0x9F93, "Y -= 3: back to next low ptr byte", inline=True)
comment(0x9F94, "(continued)", inline=True)
comment(0x9F9F, "CLC for base pointer addition", inline=True)
comment(0x9FA0, "Add RXCB base to get RXCB+4 addr", inline=True)
comment(0x9FA7, "Claim Tube transfer address", inline=True)
comment(0x9FAF, "Reclaim with scout status type", inline=True)
comment(0x9FB4, "Restore X from stack", inline=True)
comment(0x9FB5, "Return with C = transfer status", inline=True)
comment(0x9FD9, "Return with C=1 (success)", inline=True)

# --- init_vectors_and_copy (&8103): NFS init ---
comment(0x8103, "Save Y (ROM number) for later", inline=True)
comment(0x8105, "Y=12: 4 triplets x 3 bytes each", inline=True)
comment(0x8107, "Load vector offset from table", inline=True)
comment(0x810A, "Previous table byte", inline=True)
comment(0x810B, "Load vector high byte from table", inline=True)
comment(0x810E, "Store high byte at &0201+X", inline=True)
comment(0x8111, "Previous table byte", inline=True)
comment(0x8112, "Load vector low byte from table", inline=True)
comment(0x8115, "Store low byte at &0200+X", inline=True)
comment(0x8118, "Previous table byte", inline=True)
comment(0x8119, "Loop for all 4 vector pairs", inline=True)
comment(0x8142, "Restore Y (ROM number)", inline=True)
comment(0x814C, "Y=5: select NFS", inline=True)

# --- nmi_tx_data (&9D5B): NMI TX data handler ---
comment(0x9D69, "Next TX buffer byte", inline=True)
comment(0x9D6A, "Load second byte from TX buffer", inline=True)
comment(0x9D6D, "Advance TX index past second byte", inline=True)
comment(0x9D6E, "Save updated TX buffer index", inline=True)
comment(0x9D87, "Write CR2: clear status, idle listen", inline=True)
comment(0x9D90, "PHA/PLA delay (~7 cycles each)", inline=True)
comment(0x9D91, "Increment delay counter", inline=True)
comment(0x9D92, "Loop 256 times for NMI disable", inline=True)
comment(0x9D94, "Store error and return to idle", inline=True)

# --- tx_begin (&9BF3): Begin TX operation ---
comment(0x9C22, "(Y -= 4: reach start addr offset)", inline=True)
comment(0x9C23, "(continued)", inline=True)
comment(0x9C24, "(continued)", inline=True)
comment(0x9C2B, "(Y += 5: advance to next end byte)", inline=True)
comment(0x9C2C, "(continued)", inline=True)
comment(0x9C2D, "(continued)", inline=True)
comment(0x9C2E, "(continued)", inline=True)
comment(0x9C2F, "(continued)", inline=True)

# --- &9BE4: TX done CONTINUE ---
comment(0x9BE4, "Load current RX flags", inline=True)
comment(0x9BE7, "Clear bit 2: release halted station", inline=True)
comment(0x9BE9, "Store updated flags", inline=True)
comment(0x9BEC, "Restore Y from stack", inline=True)
comment(0x9BED, "Transfer to Y register", inline=True)
comment(0x9BEE, "Restore X from stack", inline=True)
comment(0x9BEF, "Transfer to X register", inline=True)
comment(0x9BF0, "A=0: success status", inline=True)
comment(0x9BF2, "Return with A=0 (success)", inline=True)

# --- post_ack_scout (&99C5): Post-ACK scout processing ---
comment(0x99C5, "Check port byte from scout", inline=True)
comment(0x99C8, "Non-zero port: advance RX buffer", inline=True)
comment(0x99CA, "Load control byte from scout", inline=True)
comment(0x99CD, "Is ctrl &82 (immediate peek)?", inline=True)
comment(0x99CF, "Yes: advance RX buffer for peek", inline=True)

# --- tube_dispatch_table (&0500): Tube host code page 5 ---
# tube_wrch_handler (&051C)
comment(0x051C, "Save character for WRCH output", inline=True)
comment(0x051D, "A=0: send null prefix via R2", inline=True)
comment(0x051F, "Send prefix byte to co-processor", inline=True)
comment(0x0522, "Poll R2 for co-processor reply", inline=True)
comment(0x0525, "R2 ready: go process reply", inline=True)
comment(0x0527, "Check R1 for pending WRCH request", inline=True)
comment(0x052A, "No R1 data: back to polling R2", inline=True)
comment(0x052C, "Read WRCH character from R1", inline=True)
comment(0x0532, "Resume R2 polling after servicing", inline=True)
# c0535: R2 reply received
comment(0x0535, "Recover original character", inline=True)
comment(0x0536, "Echo character back via R2", inline=True)
comment(0x0539, "Push for dispatch loop re-entry", inline=True)
comment(0x053A, "Enter main dispatch loop", inline=True)
# tube_release_return (&053D)
comment(0x053D, "Restore saved X", inline=True)
comment(0x053F, "Restore saved Y", inline=True)
comment(0x0541, "Restore saved A", inline=True)
comment(0x0542, "Return to caller", inline=True)
# tube_osbput (&0543)
comment(0x0543, "Read channel handle from R2", inline=True)
# tube_osbget (&0550)
comment(0x0550, "Read channel handle from R2", inline=True)
comment(0x0557, "Save byte read from file", inline=True)
# c055f: OSRDCH/OSBGET carry+byte reply
comment(0x055F, "Set bit 7 (no-error flag)", inline=True)
comment(0x0565, "Restore read character/byte", inline=True)
# tube_osfind (&0569)
comment(0x0569, "Read OSFIND open mode from R2", inline=True)
comment(0x0576, "Save file handle result", inline=True)
comment(0x0577, "A=&FF: success marker", inline=True)
comment(0x0579, "Send success marker via R2", inline=True)
comment(0x057C, "Restore file handle", inline=True)
# tube_osargs (&058C)
comment(0x058C, "Read file handle from R2", inline=True)
comment(0x0598, "Loop until all 4 bytes read", inline=True)
comment(0x059A, "X=0: reset index after loop", inline=True)
# tube_oscli (&05C5)
comment(0x05C5, "Read * command string from R2", inline=True)
# tube_osfile (&05D8)
comment(0x05D8, "X=&10: read 16-byte ctrl block", inline=True)
comment(0x05F1, "Set bit 7: mark result as present", inline=True)

# --- tube_code_page6 (&0600): Tube host code page 6 ---
comment(0x0600, "OSGBPB done: return to main loop", inline=True)
comment(0x0602, "X=12: read 13 OSGBPB param bytes", inline=True)
comment(0x0604, "Read param byte from Tube R2", inline=True)
comment(0x0607, "Store in zero page param block", inline=True)
comment(0x0609, "Next byte (descending)", inline=True)
comment(0x060A, "Loop until all 13 bytes read", inline=True)
comment(0x060C, "Read A (OSGBPB function code)", inline=True)
comment(0x060F, "X=0 after loop", inline=True)
comment(0x0610, "Y=0 for OSGBPB call", inline=True)
comment(0x0616, "Send OSGBPB carry result via R2", inline=True)
comment(0x0619, "X=12: send 13 updated param bytes", inline=True)
comment(0x061B, "Load updated param byte", inline=True)
comment(0x061D, "Send param byte via R2", inline=True)
comment(0x0620, "Next byte (descending)", inline=True)
comment(0x0621, "Loop until all 13 bytes sent", inline=True)
comment(0x0623, "Return to main event loop", inline=True)
comment(0x0626, "Read X parameter from co-processor", inline=True)
comment(0x0629, "Save in X", inline=True)
comment(0x062A, "Read A (OSBYTE function code)", inline=True)
comment(0x062D, "Execute OSBYTE A,X", inline=True)
comment(0x0630, "Poll R2 status (bit 6 = ready)", inline=True)
comment(0x0633, "Not ready: keep polling", inline=True)
comment(0x0638, "Return to main event loop", inline=True)
comment(0x063B, "Read X parameter from co-processor", inline=True)
comment(0x063E, "Save in X", inline=True)
comment(0x063F, "Read Y parameter from co-processor", inline=True)
comment(0x0642, "Save in Y", inline=True)
comment(0x0643, "Read A (OSBYTE function code)", inline=True)
comment(0x0646, "Execute OSBYTE A,X,Y", inline=True)
comment(0x064D, "A=&40: high bit will hold carry", inline=True)
comment(0x0650, "Send carry+status byte via R2", inline=True)
comment(0x0653, "Poll R2 status for ready", inline=True)
comment(0x0656, "Not ready: keep polling", inline=True)
comment(0x065D, "Read OSWORD number from co-processor", inline=True)
comment(0x0660, "Save OSWORD number in Y", inline=True)
comment(0x0661, "Poll R2 status for data ready", inline=True)
comment(0x0664, "Not ready: keep polling", inline=True)
comment(0x066A, "No params (length=0): skip read loop", inline=True)
comment(0x066C, "Poll R2 status for data ready", inline=True)
comment(0x066F, "Not ready: keep polling", inline=True)
comment(0x0671, "Read param byte from R2", inline=True)
comment(0x0677, "Next param byte (descending)", inline=True)
comment(0x0678, "Loop until all params read", inline=True)
comment(0x067D, "Y=&01: param block at &0128", inline=True)
comment(0x067F, "Execute OSWORD with XY=&0128", inline=True)
comment(0x0682, "A=&FF: result marker for co-processor", inline=True)
comment(0x0684, "Send result marker via R2", inline=True)
comment(0x0687, "Poll R2 status for ready", inline=True)
comment(0x068A, "Not ready: keep polling", inline=True)
comment(0x068F, "Decrement result byte counter", inline=True)
comment(0x0695, "Poll R2 status for ready", inline=True)
comment(0x0698, "Not ready: keep polling", inline=True)
comment(0x069A, "Send result byte via R2", inline=True)
comment(0x069D, "Next result byte (descending)", inline=True)
comment(0x069E, "Loop until all results sent", inline=True)
comment(0x06A0, "Return to main event loop", inline=True)
comment(0x06A3, "X=4: read 5-byte RDLN control block", inline=True)
comment(0x06A5, "Read control block byte from R2", inline=True)
comment(0x06A8, "Store in zero page params", inline=True)
comment(0x06AA, "Next byte (descending)", inline=True)
comment(0x06AB, "Loop until all 5 bytes read", inline=True)
comment(0x06AE, "Y=0 for OSWORD 0", inline=True)
comment(0x06B0, "A=0: OSWORD 0 (read line)", inline=True)
comment(0x06B1, "Read input line from keyboard", inline=True)
comment(0x06B8, "Escape: send &FF error to co-processor", inline=True)
comment(0x06BB, "X=0: start of input buffer at &0700", inline=True)
comment(0x06BF, "Send &7F (success) to co-processor", inline=True)
comment(0x06C2, "Load char from input buffer", inline=True)
comment(0x06C5, "Send char to co-processor", inline=True)
comment(0x06C8, "Next character", inline=True)
comment(0x06CB, "Loop until CR terminator sent", inline=True)
comment(0x06CD, "Return to main event loop", inline=True)
comment(0x06D0, "Poll R2 status (bit 6 = ready)", inline=True)
comment(0x06D3, "Not ready: keep polling", inline=True)
comment(0x06D5, "Write A to Tube R2 data register", inline=True)
comment(0x06D8, "Return to caller", inline=True)
comment(0x06D9, "Poll R4 status (bit 6 = ready)", inline=True)
comment(0x06DC, "Not ready: keep polling", inline=True)
comment(0x06DE, "Write A to Tube R4 data register", inline=True)
comment(0x06E1, "Return to caller", inline=True)
comment(0x06E5, "ROR: shift escape bit 7 to carry", inline=True)
comment(0x06EB, "Send event number via R1", inline=True)
comment(0x06EE, "Y value for event", inline=True)
comment(0x06EF, "Send Y via R1", inline=True)
comment(0x06F2, "X value for event", inline=True)
comment(0x06F3, "Send X via R1", inline=True)
comment(0x06F6, "Restore A (event type)", inline=True)
comment(0x06F7, "Poll R1 status (bit 6 = ready)", inline=True)
comment(0x06FA, "Not ready: keep polling", inline=True)
comment(0x06FC, "Write A to Tube R1 data register", inline=True)
comment(0x06FF, "Return to caller", inline=True)

# --- clear_fs_flag (&8651) ---
comment(0x8651, "Invert A to create clear mask", inline=True)
comment(0x8653, "AND into FS flags to clear bits", inline=True)
comment(0x8656, "Jump to shared store handler", inline=True)

# --- ex_handler (&8BFA) ---
comment(0x8BFA, "X=1: single-entry-per-line mode", inline=True)
comment(0x8BFC, "Store column format selector", inline=True)
comment(0x8BFE, "A=3: FS function code for EX", inline=True)

# --- print_hex (&8D9D) ---
comment(0x8D9D, "Save byte for low nibble", inline=True)
comment(0x8D9E, "Shift high nibble to low position", inline=True)
comment(0x8D9F, "Shift high nibble to low position", inline=True)
comment(0x8DA0, "Shift high nibble to low position", inline=True)
comment(0x8DA1, "Shift high nibble to low position", inline=True)
comment(0x8DA2, "Print high nibble as hex digit", inline=True)
comment(0x8DA5, "Restore original byte", inline=True)
comment(0x8DA6, "Mask to low nibble", inline=True)
comment(0x8DA8, "Convert to ASCII '0' base", inline=True)
comment(0x8DAA, "Above '9'?", inline=True)
comment(0x8DAC, "No: digit 0-9, skip adjustment", inline=True)
comment(0x8DAE, "Add 7 (6+C) for 'A'-'F'", inline=True)
comment(0x8DB0, "ALWAYS branch to print character", inline=True)

# --- print_reply_bytes (&8DB2) ---
comment(0x8DB2, "Y=10: character count", inline=True)
comment(0x8DB4, "Load byte from FS reply buffer", inline=True)
comment(0x8DBA, "Next buffer offset", inline=True)
comment(0x8DBB, "Decrement character counter", inline=True)
comment(0x8DBC, "Loop until all chars printed", inline=True)
comment(0x8DBE, "Return to caller", inline=True)

# --- net_1_read_handle (&8E3B) ---
comment(0x8E3B, "Y=&6F: offset to handle byte in RX buf", inline=True)
comment(0x8E3D, "Load file handle from RX buffer", inline=True)
comment(0x8E3F, "Store in parameter block pointer (&F0)", inline=True)
comment(0x8E41, "Return to caller", inline=True)

# --- net_3_close_handle (&8E66) ---
comment(0x8E6B, "Preserve carry via ROL", inline=True)
comment(0x8E6E, "A=&3F: close marker byte", inline=True)
comment(0x8E70, "Mark handle as closed in workspace", inline=True)
comment(0x8E72, "Restore carry via ROR", inline=True)

# --- adlc_init_workspace (&9687) ---
comment(0x96A8, "A=0: clear source network", inline=True)
comment(0x96AA, "Clear TX source network byte", inline=True)
comment(0x96AD, "BIT INTON: re-enable NMIs", inline=True)
comment(0x96B0, "Return to caller", inline=True)
comment(0x96B1, "A=0: clear TX complete flag", inline=True)
comment(0x96B3, "Clear TX complete flag", inline=True)
comment(0x96B6, "Poll Econet init status", inline=True)
comment(0x96B9, "Not initialised: skip to RX listen", inline=True)
comment(0x96BB, "Clear Econet init flag", inline=True)
comment(0x96BE, "Load NMI vector low byte", inline=True)
comment(0x96C1, "Check if low byte is expected value", inline=True)
comment(0x96C3, "Mismatch: keep polling", inline=True)
comment(0x96C5, "Load NMI vector high byte", inline=True)
comment(0x96C8, "Check if high byte is &97", inline=True)
comment(0x96CA, "Mismatch: keep polling", inline=True)
comment(0x96CC, "BIT INTOFF: disable NMIs", inline=True)

# --- rx_imm_peek (&9AF1) ---
comment(0x9AF1, "Save current TX block low byte", inline=True)
comment(0x9AF3, "Push to stack", inline=True)
comment(0x9AF4, "Save current TX block high byte", inline=True)
comment(0x9AF6, "Push to stack", inline=True)

# --- svc_9_help (&81ED) ---
comment(0x81ED, "Print inline ROM identification string", inline=True)
comment(0x81FB, "Load preserved Y from temp storage", inline=True)

# --- fscv_2_star_run (&8DBF) ---
comment(0x8DBF, "Parse filename using GSINIT/GSREAD", inline=True)
comment(0x8DC2, "Copy filename to FS command buffer", inline=True)

# --- save_econet_state (&96CF) ---
comment(0x96D2, "Y=8: RXCB offset for TX status", inline=True)
comment(0x96D4, "Load current TX status flag", inline=True)
comment(0x96D7, "Save TX status in RXCB", inline=True)
comment(0x96D9, "Enter RX listen mode", inline=True)
comment(0x96DC, "Y=8: RXCB offset for TX status", inline=True)
comment(0x96DE, "Load saved TX status from RXCB", inline=True)
comment(0x96E0, "Restore TX status flag", inline=True)

# --- tx_ctrl_proc (&9D0F) ---
comment(0x9D0F, "Compare Y with 16-byte boundary", inline=True)
comment(0x9D11, "Below boundary: continue addition", inline=True)
comment(0x9D13, "Restore processor flags", inline=True)
comment(0x9D14, "Calculate transfer byte count", inline=True)
comment(0x9D17, "Jump to TX control exit", inline=True)

# --- check_escape (&851D) ---
comment(0x851D, "A=&7E: OSBYTE acknowledge escape", inline=True)
comment(0x851F, "Test escape flag (bit 7)", inline=True)
comment(0x8521, "Bit 7 clear: no escape, return", inline=True)
comment(0x8526, "Y=0 for indexed store", inline=True)
comment(0x8528, "LSR: get escape result bit", inline=True)
comment(0x8529, "Store escape result to TXCB", inline=True)
comment(0x852B, "Restore A", inline=True)
comment(0x852C, "Non-zero: report 'Not listening'", inline=True)
comment(0x853B, "N=1: at/past EOF, set EOF flag", inline=True)
comment(0x853D, "Load SPOOL handle mask", inline=True)
comment(0x853F, "Clear EOF flag for this handle", inline=True)
comment(0x8542, "C=0: skip to handle mask load", inline=True)
comment(0x8544, "Load SPOOL handle mask", inline=True)
comment(0x8546, "Set EOF flag for this handle", inline=True)
comment(0x8549, "Load handle bitmask for caller", inline=True)
comment(0x854C, "Return with handle mask in A", inline=True)


# ============================================================
# Annotations back-propagated from NFS 3.60
# ============================================================
comment(0x0476, "Y=0: start at beginning of page", inline=True)
comment(0x0478, "Store to zero page pointer low byte", inline=True)
subroutine(0x047A, "tube_init_reloc", hook=None,
    title="Initialise relocation address for ROM transfer",
    description="""\
Sets source page to &8000 and page counter to &80. Checks
ROM type bit 5 for a relocation address in the ROM header;
if present, extracts the 4-byte address from after the
copyright string. Otherwise uses default &8000 start.""")
comment(0x0558, "Send carry+byte reply (BGET result)", inline=True)
comment(0x0561, "ROR A: encode carry (error flag) into bit 7", inline=True)
comment(0x0562, "= JSR tube_send_r2 (overlaps &053D entry)", inline=True)
comment(0x808D, "C=1: dot found, first number was network", inline=True)
comment(0x80A0, "Test for colon separator", inline=True)
comment(0x80A2, "Not colon: keep scanning backward", inline=True)
comment(0x80A4, "Echo colon, then read user input from keyboard", inline=True)
label(0x80A7, "read_remote_cmd_line")   # Read characters from keyboard into FS command buffer
comment(0x80A7, "Check for escape condition", inline=True)
comment(0x80AD, "Test for CR (end of line)", inline=True)
comment(0x80AF, "Not CR: continue reading input", inline=True)
comment(0x80F8, "X=6 extra pages for char definitions", inline=True)
comment(0x80FA, "OSBYTE &14: explode character RAM", inline=True)
label(0x811B, "init_tube_and_workspace")
comment(0x811B, "EVNTV low = &AD (event handler address)", inline=True)
comment(0x811D, "Set EVNTV low byte at &0220", inline=True)
label(0x8144, "tube_chars_done")       # BEQ: zero byte received, transfer complete
comment(0x8144, "A=0: fall through to service &12 check", inline=True)
label(0x8146, "check_svc_12")          # Convergence before CMP #&12 test
comment(0x8146, "Is this service &12 (select FS)?", inline=True)
comment(0x8148, "No: check if service < &0D", inline=True)
comment(0x814A, "Service &12: Y=5 (NFS)?", inline=True)
comment(0x81ED, "Print ROM identification string", inline=True)
subroutine(0x8348, "init_tx_reply_port", hook=None,
    title="Initialise TX control block for FS reply on port &90",
    description="""\
Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
up the TX control block, stores the port and control bytes, then
decrements the control flag. Used by send_fs_reply_cmd to prepare
for receiving the fileserver's reply.""")
label(0x8393, "store_fs_hdr_clc")       # CLC entry: clear carry then store function code
comment(0x8393, "CLC: no byte-stream path", inline=True)
label(0x8394, "store_fs_hdr_fn")       # Store function code and CSD/LIB handles
comment(0x8394, "Store function code at &0F01", inline=True)
comment(0x842E, "'-': offset into \"E.\" string at &852D", inline=True)
comment(0x8430, "X=value of *EXEC file handle", inline=True)
comment(0x8432, "No EXEC match -- skip close", inline=True)
label(0x85F8, "scan_decimal_digit")    # Read ASCII digits and accumulate decimal value
comment(0x85FA, "Dot separator?", inline=True)
comment(0x8651, "Invert mask: set bits become clear bits", inline=True)
comment(0x8653, "Clear specified bits in flags", inline=True)
subroutine(0x86B0, "copy_filename_ptr", hook=None,
    title="Copy filename pointer to os_text_ptr and parse",
    description="""\
Copies the 2-byte filename pointer from (fs_options),Y into
os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
to parse the filename via GSINIT/GSREAD into the &0E30 buffer.""")
subroutine(0x86BC, "parse_filename_gs_y", hook=None,
    title="Parse filename via GSINIT/GSREAD from offset Y",
    description="""\
Sub-entry of parse_filename_gs that accepts a non-zero Y offset
into the (os_text_ptr) string. Initialises GSINIT, reads chars
via GSREAD into &0E30, CR-terminates the result, and sets up
fs_crc_lo/hi to point at the buffer.""")
comment(0x87A4, "Build header and send FS save command", inline=True)
comment(0x87A7, "Send file data blocks to server", inline=True)
label(0x87AA, "save_csd_display")       # Save CSD from reply and display file info
comment(0x87AA, "Save CSD from reply for catalogue display", inline=True)
comment(0x87AD, "Print file length in hex", inline=True)
comment(0x87C7, "Store decoded access in param block", inline=True)
comment(0x87C9, "Next attribute byte", inline=True)
comment(0x8805, "CLC for ADC in loop", inline=True)
comment(0x8806, "Source = current position", inline=True)
comment(0x8808, "Store source address byte", inline=True)
comment(0x8959, "Y = A = byte count for copy loop", inline=True)
comment(0x895A, "A!=0: copy command context block", inline=True)
comment(0x895C, "&0A >> 1 = 5 = NFS filing system number", inline=True)
comment(0x895C, "FS number 5 (loaded as &0A, LSR'd)", inline=True)
subroutine(0x896B, "return_a_zero", hook=None,
    title="Return with A=0 via register restore",
    description="""\
Loads A=0 and branches (always taken) to the common register
restore exit at restore_args_return. Used as a shared exit
point by ARGSV, FINDV, and GBPBV when an operation is
unsupported or should return zero.""")
comment(0x8C02, "X=3: column count for multi-column layout", inline=True)
comment(0x8C04, "CRFLAG=3: first entry will trigger newline", inline=True)
comment(0x8C06, "Y=&FF: mark as escapable", inline=True)
comment(0x8C0A, "A=&0B: examine argument count", inline=True)
label(0x8C0C, "init_cat_params")       # Store examine arg count, init catalogue display
comment(0x8C0C, "Store examine argument count", inline=True)
comment(0x8CC4, "Load entry count from reply", inline=True)
comment(0x8CDE, "Loop for remaining characters", inline=True)
subroutine(0x8D60, "cat_column_separator", hook=None,
    title="Print catalogue column separator or newline",
    description="""\
Handles column formatting for *CAT display. On a null byte
separator, advances the column counter modulo 4: prints a
2-space separator between columns, or a CR at column 0.
Called from fsreply_0_print_dir.""")
comment(0x8DBF, "Parse filename from command line", inline=True)
subroutine(0x8E42, "load_handle_calc_offset", hook=None,
    title="Load handle from &F0 and calculate workspace offset",
    description="""\
Loads the file handle byte from &F0, then falls through to
calc_handle_offset which converts handle * 12 to a workspace
byte offset. Validates offset < &48.""")
comment(0x8E6E, "&3F = '?' marks slot as unused", inline=True)
comment(0x8E70, "Write close marker to workspace slot", inline=True)
comment(0x904E, "Y=&7D: store byte for TX at offset &7D", inline=True)
comment(0x9050, "Store data byte at (net_rx_ptr)+&7D for TX", inline=True)
comment(0x9050, "Store data byte at (net_rx_ptr)+&7D for TX", inline=True)
comment(0x9052, "Save data byte for &0D check after TX", inline=True)
comment(0x9053, "Set up TX control block", inline=True)
comment(0x9057, "Enable IRQs and transmit", inline=True)
label(0x905A, "delay_between_tx")      # Spin-delay between consecutive TX packets
comment(0x905A, "Short delay loop between TX packets", inline=True)
comment(0x905B, "Spin until X reaches 0", inline=True)
comment(0x905D, "Restore data byte for terminator check", inline=True)
subroutine(0x9070, "enable_irq_and_tx", hook=None,
    title="Enable interrupts and transmit via tx_poll_ff",
    description="""\
CLI to enable interrupts, then JMP tx_poll_ff. A short
tail-call wrapper used after building the TX control block.""")
comment(0x920C, "Test if sequence changed (bit 7 mismatch)", inline=True)
comment(0x920D, "Sequence unchanged: skip flush", inline=True)
comment(0x920F, "Undo ROR", inline=True)
comment(0x9240, "Save current PFLAGS", inline=True)
comment(0x9241, "Carry = current sequence (bit 7)", inline=True)
comment(0x9242, "Restore original PFLAGS", inline=True)
comment(0x9243, "Toggle sequence number (bit 7 of PFLAGS)", inline=True)
subroutine(0x968A, "init_nmi_workspace", hook=None,
    title="Initialise NMI workspace (skip service request)",
    description="""\
Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
service request. Copies 32 bytes of NMI shim from ROM to
&0D00, patches the ROM bank number, sets init flags, reads
station ID, and re-enables NMIs.""")
comment(0x97E3, "CLC for 12-byte slot advance", inline=True)
comment(0x97E4, "Advance to next 12-byte port slot", inline=True)
comment(0x97E6, "Update workspace pointer to next slot", inline=True)
comment(0x97E8, "Always branches (page &C0 won't overflow)", inline=True)
comment(0x97EE, "Try NFS workspace if paged list exhausted", inline=True)
comment(0x97F1, "No NFS workspace RX (bit6 clear) -- discard", inline=True)
comment(0x9805, "Match found: set scout_status = 3", inline=True)
comment(0x9807, "Record match for completion handler", inline=True)
subroutine(0x987A, "install_data_rx_handler", hook=None,
    title="Install data RX bulk or Tube handler",
    description="""\
Selects either the normal bulk RX handler (&9843) or the Tube
RX handler (&98A0) based on the Tube transfer flag in tx_flags,
and installs the appropriate NMI handler.""")
subroutine(0x9894, "nmi_error_dispatch", hook=None,
    title="NMI error handler dispatch",
    description="""\
Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")
comment(0x991C, "Read second data byte (paired transfer)", inline=True)
comment(0x991F, "Send second byte to Tube", inline=True)
comment(0x9930, "Zero: Tube transfer complete", inline=True)
comment(0x9932, "Re-read SR2 for next byte pair", inline=True)
comment(0x9935, "More data available: continue loop", inline=True)
subroutine(0x99D4, "advance_rx_buffer_ptr", hook=None,
    title="Advance RX buffer pointer after transfer",
    description="""\
Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")
comment(0x9A0A, "Restore X from stack", inline=True)
comment(0x9A0B, "Transfer to X register", inline=True)
subroutine(0x9A59, "install_rx_scout_handler", hook=None,
    title="Install RX scout NMI handler",
    description="""\
Installs nmi_rx_scout (&96BF) as the NMI handler via
set_nmi_vector, without first calling adlc_rx_listen.
Used when the ADLC is already in the correct RX mode.""")
comment(0x9A65, "Store to port buffer", inline=True)
comment(0x9A67, "Advance buffer pointer", inline=True)
comment(0x9A9C, "Push &9A as dispatch high byte", inline=True)
comment(0x9A9D, "Load handler low byte from jump table", inline=True)
comment(0x9AA0, "Push handler low byte", inline=True)
comment(0x9AA1, "RTS dispatches to handler", inline=True)
subroutine(0x9B28, "imm_op_build_reply", hook=None,
    title="Build immediate operation reply header",
    description="""\
Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables CB1 interrupts and configures the VIA shift
register for outgoing shift-out mode before returning to
idle listen.""")
subroutine(0x9BF3, "tx_begin", hook=None,
    title="Begin TX operation",
    description="""\
Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")
subroutine(0x9C62, "intoff_test_inactive", hook=None,
    title="Disable NMIs and test INACTIVE",
    description="""\
Mid-instruction label within the INACTIVE polling loop. The
address &9BE2 is referenced as a constant for self-modifying
code. Disables NMIs twice (belt-and-braces) then tests SR2
for INACTIVE before proceeding with TX.""")
comment(0x9CDD, "Push high byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x9CDE, "Look up handler address low from table", inline=True)
comment(0x9CE1, "Push low byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x9CE2, "RTS dispatches to control-byte handler", inline=True)
label(0x9F4C, "tx_result_fail")        # Store result=&41 (not listening) (9 refs)
# ============================================================

# ============================================================
# Annotations back-propagated from NFS 3.40
# ============================================================
label(0x047A, "tube_init_reloc")     # Init relocation address for ROM→Tube transfer
label(0x8348, "init_tx_reply_port")     # Init TX control block for FS reply on port &90
subroutine(0x851F, "check_escape_handler", hook=None,
    title="Test MOS escape flag and abort if pending",
    description="""\
Tests MOS escape flag (&FF bit 7). If escape is pending:
acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
the control block via (net_tx_ptr),Y, and branches to the
NLISTN error path. If no escape, returns immediately.""")
label(0x86B0, "copy_filename_ptr")       # Copy filename pointer to os_text_ptr and parse
label(0x86BC, "parse_filename_gs_y")     # Parse filename via GS from offset Y
label(0x896B, "return_a_zero")          # Return with A=0 via register restore
comment(0x8CFA, "Data bytes: boot_cmd_strings 'ec'", inline=True)
comment(0x8CFC, "Check if messages enabled", inline=True)
comment(0x8CFF, "Zero: no info to display, return", inline=True)
comment(0x8D01, "Y=0: start of filename", inline=True)
label(0x8D60, "cat_column_separator")    # Print catalogue column separator or newline
label(0x8E42, "load_handle_calc_offset") # Load handle from &F0 and calc workspace offset
comment(0x8E6E, "A=&3F: handle closed/unused marker", inline=True)
comment(0x8E70, "Write marker to handle slot", inline=True)
label(0x9070, "enable_irq_and_tx")     # CLI then JMP tx_poll_ff
label(0x968A, "init_nmi_workspace")     # Init NMI workspace (skip service request)
label(0x96B6, "poll_nmi_ready")       # Polls NMI vector for shim installation
label(0x987A, "install_data_rx_handler") # Select bulk or Tube RX handler
label(0x9894, "nmi_error_dispatch")    # NMI error handler dispatch (12 refs)
label(0x99D4, "advance_rx_buffer_ptr") # Advance RX buffer pointer after transfer
label(0x9A59, "install_rx_scout_handler") # Install RX scout NMI handler
label(0x9B28, "imm_op_build_reply")    # Build immediate operation reply header
label(0x9BF3, "tx_begin")              # Begin TX operation
label(0x9C62, "intoff_test_inactive")  # Disable NMIs and test INACTIVE
# Generate disassembly

# ============================================================
# Annotations back-propagated from NFS 3.40
# ============================================================
comment(0x96D2, "Y=5: status flags offset", inline=True)

# ============================================================
# Annotations back-propagated from NFS 3.60
# ============================================================
comment(0x0414, "&80 sentinel: clear address claim", inline=True)
comment(0x046A, "Return from transfer setup", inline=True)
label(0x0473, "tube_begin")          # BEGIN: startup entry for Tube host code
comment(0x0473, "BEGIN: enable interrupts for Tube host code", inline=True)
comment(0x04FF, "Return with pointers initialised", inline=True)
comment(0x809E, "Y=0: no colon found, send command", inline=True)
comment(0x80AC, "Advance write pointer", inline=True)
comment(0x84E0, "Next dest byte", inline=True)
comment(0x853B, "Bit7 set: skip FS flag clear", inline=True)
comment(0x853F, "Clear FS flag for handle", inline=True)
label(0x85F0, "jump_via_addr")        # BMI: bit 7 terminator, JMP (fs_load_addr)
comment(0x87FD, "Y=4: process 4 address bytes", inline=True)
label(0x8A94, "gbpb_read_path")      # BNE: non-zero read, skip write transfer
comment(0x8A94, "Read path: receive data blocks from FS", inline=True)
comment(0x8CCB, "Print/format this directory entry", inline=True)
comment(0x8CCE, "CLC for addition", inline=True)
comment(0x8E80, "X = sub-function code for table lookup", inline=True)
comment(0x9213, "Flush current output block", inline=True)
comment(0x96AD, "INTON: re-enable NMIs (&FE20 read side effect)", inline=True)
label(0x97B5, "scan_nfs_port_list")   # NFS workspace port list scan entry
comment(0x97B5, "Store page to workspace pointer low", inline=True)
comment(0x9818, "Calculate transfer parameters", inline=True)
comment(0x990B, "Send byte to Tube data register 3", inline=True)
comment(0x9A15, "Other port-0 ops: immediate dispatch", inline=True)
comment(0x9A6A, "No page crossing", inline=True)
comment(0x9A6C, "Jump to completion handler", inline=True)
comment(0x9A96, "Reload ctrl byte for dispatch table", inline=True)
comment(0x9AA2, "Jump to discard handler", inline=True)

# --- service_handler (&80EA): service call dispatch ---
comment(0x80F4, "Save ROM number across OSBYTE", inline=True)
comment(0x80F6, "Save Tube address across OSBYTE", inline=True)
comment(0x80FF, "Restore ROM number", inline=True)
comment(0x8101, "Continue to vector setup", inline=True)

# --- print_inline (&85D9): inline string printing ---
comment(0x85DA, "Store return addr low as string ptr", inline=True)
comment(0x85DD, "Store return addr high as string ptr", inline=True)
comment(0x85DF, "Y=0: offset for indirect load", inline=True)
comment(0x85E3, "No page wrap: skip high byte inc", inline=True)
comment(0x85E5, "Handle page crossing in pointer", inline=True)
comment(0x85EE, "OSASCI preserves NZ; loop always", inline=True)

# --- nmi_tx_complete (&9DA3): TX done, switch to RX ---
comment(0x9DA5, "Write CR1 to switch from TX to RX", inline=True)
comment(0x9DB0, "A=1: mask for bit0 test", inline=True)
comment(0x9DB2, "Test tx_flags bit0 (handshake)", inline=True)
comment(0x9DB5, "bit0 clear: install reply handler", inline=True)
comment(0x9DBC, "High byte of nmi_reply_scout addr", inline=True)
comment(0x9DBE, "Install handler and RTI", inline=True)

# --- immediate_op (&9A6F): immediate op dispatch ---
comment(0x9A7E, "Load source station number", inline=True)
comment(0x9A81, "Station >= &F0? (privileged)", inline=True)
comment(0x9A83, "Privileged: skip protection check", inline=True)
comment(0x9A91, "Carry clear: operation permitted", inline=True)
comment(0x9A93, "Operation blocked by LSTAT mask", inline=True)
comment(0x9A99, "Look up handler address high byte", inline=True)
comment(0x9A9C, "Push handler address high", inline=True)
comment(0x9A9D, "Look up handler address low byte", inline=True)
comment(0x9AA0, "Push handler address low", inline=True)
comment(0x9AA1, "RTS dispatch to handler", inline=True)

# --- save_vdu_state (&92EB): trampoline block ---
comment(0x9311, "Return after storing result", inline=True)
comment(0x9660, "Trampoline: forward to tx_begin", inline=True)
comment(0x9663, "Trampoline: forward to adlc_init", inline=True)
comment(0x9666, "Trampoline: forward to NMI release", inline=True)
comment(0x9669, "Trampoline: forward to NMI claim", inline=True)
comment(0x966C, "Trampoline: forward to IRQ handler", inline=True)

# --- filev_handler (&86DE): OSFILE dispatch ---
comment(0x86DE, "Save A/X/Y in FS workspace", inline=True)
comment(0x86EA, "A=&FF: branch to load path", inline=True)
comment(0x86EF, "Copy parsed filename to cmd buffer", inline=True)
comment(0x86F2, "Y=2: FS function code offset", inline=True)

# --- nmi_ack_tx_src (&999C): ACK frame completion ---
comment(0x99A9, "Write network=0 (local) to TX FIFO", inline=True)
comment(0x99AC, "Check tx_flags for data phase", inline=True)
comment(0x99AF, "bit7 set: start data TX phase", inline=True)
comment(0x99C2, "TDRA error: jump to error handler", inline=True)

# --- nmi_rx_scout_net (&971F): scout net byte ---
comment(0x972F, "Write CR1 to discontinue RX", inline=True)
comment(0x9732, "Return to idle scout listening", inline=True)
comment(0x973C, "High byte of scout data handler", inline=True)
comment(0x973E, "Install scout data loop and RTI", inline=True)

# --- nmi_reply_cont (&9DD7): reply scout byte 2 ---
comment(0x9DE3, "High byte of nmi_reply_validate", inline=True)
comment(0x9DED, "A=&41: 'not listening' error code", inline=True)
comment(0x9DEF, "Store error and return to idle", inline=True)

# --- tx_ctrl_peek (&9CF7): PEEK setup ---
comment(0x9CF7, "A=3: scout_status for PEEK op", inline=True)

# --- copy_reply_to_params (&87E3): copy FS reply data ---
comment(0x87EB, "Next byte (descending)", inline=True)
comment(0x87EE, "Loop until offset 2 reached", inline=True)
comment(0x87F1, "Subtract 1 (of 3) from Y", inline=True)
comment(0x87F2, "Subtract 2 (of 3) from Y", inline=True)
comment(0x87F3, "Subtract 3 (of 3) from Y", inline=True)
comment(0x87F4, "Return to caller", inline=True)

# --- transfer_file_blocks (&87F5): multi-block xfer ---
comment(0x87FB, "X=0: clear hi bytes of block size", inline=True)
comment(0x87FF, "Clear block size hi byte 1", inline=True)
comment(0x8802, "Clear block size hi byte 2", inline=True)
comment(0x880A, "Add block size to current position", inline=True)
comment(0x8815, "Carry: address overflowed, clamp", inline=True)
comment(0x8845, "A=&2A: error ptr for retry", inline=True)

# --- filev_save (&876A): OSFILE save ---
comment(0x87A2, "A=&14: FS function code for SAVE", inline=True)
comment(0x87B0, "A=&2A: error ptr for retry", inline=True)
comment(0x87B2, "Store error pointer for TX poll", inline=True)
comment(0x87B4, "Send FS reply acknowledgement", inline=True)
comment(0x87C2, "Z=1: first byte, use A directly", inline=True)
comment(0x87C4, "Load attribute byte from FS reply", inline=True)

# --- nmi_data_tx (&9E5F): TX data payload ---
comment(0x9EA0, "bit7 clear: error path", inline=True)
comment(0x9EA2, "ADLC reset and return to idle", inline=True)
comment(0x9EA5, "A=&41: 'not listening' error", inline=True)
comment(0x9EA7, "Store result and return to idle", inline=True)
comment(0x9EAA, "Load saved handler low byte", inline=True)

# --- advance_rx_buffer_ptr (&99D4): Tube update ---
comment(0x9A0C, "Y=8: RXCB buffer ptr offset", inline=True)
comment(0x9A0E, "Load current RXCB buffer ptr lo", inline=True)
comment(0x9A10, "SEC for ADC #0 = add carry", inline=True)
comment(0x9A11, "Increment by 1 (Tube extra byte)", inline=True)
comment(0x9A13, "Store updated ptr back to RXCB", inline=True)

# --- ctrl_block_setup (&9171): template init ---
comment(0x9185, "V=1: use (net_rx_ptr) page", inline=True)
comment(0x9187, "V=1: skip to net_rx_ptr page", inline=True)
comment(0x9189, "V=0: use (nfs_workspace) page", inline=True)
comment(0x9197, "Loop until all template bytes done", inline=True)
comment(0x919A, "Store final offset as net_tx_ptr", inline=True)

# --- nmi_final_ack (&9EF8): final ACK validation ---
comment(0x9F09, "High byte of handler address", inline=True)
comment(0x9F0B, "Install continuation handler", inline=True)
comment(0x9F1A, "High byte of handler address", inline=True)
comment(0x9F21, "Install handler and RTI", inline=True)

# --- tx_ctrl_proc (&9D1A): JSR/UserProc/OSProc ---
comment(0x9D1A, "A=2: scout_status for procedure ops", inline=True)
comment(0x9D1C, "Store scout status", inline=True)
comment(0x9D1F, "Calculate transfer parameters", inline=True)
comment(0x9D22, "Exit TX ctrl setup", inline=True)

# --- rx_imm_peek (&9AF7): PEEK response setup ---
comment(0x9B07, "Restore saved nmi_tx_block_hi", inline=True)
comment(0x9B08, "Restore workspace ptr hi byte", inline=True)
comment(0x9B0A, "Restore saved nmi_tx_block", inline=True)
comment(0x9B0B, "Restore workspace ptr lo byte", inline=True)

# --- store_output_byte (&91F9): printer output ---
comment(0x9209, "XOR with current PFLAGS", inline=True)
comment(0x9210, "Store toggled PFLAGS", inline=True)
comment(0x9216, "Reload current PFLAGS", inline=True)
comment(0x9221, "Store recombined PFLAGS value", inline=True)

# --- remote_cmd_dispatch (&90D0): remote OSBYTE ---
comment(0x9107, "Write &7F to RXCB (wait for reply)", inline=True)
comment(0x9109, "Poll RXCB for completion (bit7)", inline=True)
comment(0x913A, "Y=&0E: 14 bytes for OSWORD 8", inline=True)
comment(0x913C, "OSWORD 7 (sound)?", inline=True)

# --- i_am_handler (&807E): station number parse ---
comment(0x8088, "A=0: default network number", inline=True)
comment(0x8099, "Skip past current character", inline=True)
comment(0x809A, "Load next character from cmd line", inline=True)
comment(0x809C, "CR: end of command string?", inline=True)

# --- issue_vectors_claimed (&8261): init services ---
comment(0x8261, "A=&8F: issue service request", inline=True)
comment(0x8263, "X=&0F: 'vectors claimed' service", inline=True)
comment(0x8268, "X=&0A: service &0A", inline=True)
comment(0x826F, "Non-zero: skip auto-boot", inline=True)

# --- fs_osword_dispatch (&8E80): PHA/PHA/RTS ---
comment(0x8E81, "Push return addr high (restore_args)", inline=True)
comment(0x8E83, "Push return addr high byte", inline=True)
comment(0x8E84, "Push return addr low (restore_args)", inline=True)
comment(0x8E86, "Push return addr low byte", inline=True)

# --- osword_11_handler (&8ED2): sub-dispatch ---
comment(0x8EF7, "Sub-function >= 6?", inline=True)
comment(0x8EF9, "Yes: out of range, error", inline=True)
comment(0x8EFB, "Sub-function 4 or 5?", inline=True)
comment(0x8F12, "Jump to read/write workspace path", inline=True)

# --- tube_brk_handler (&0016): relocated Tube BRK ---
comment(0x0036, "More pages: continue transfer", inline=True)
comment(0x0038, "A=4: host-to-parasite burst", inline=True)

# --- dispatch_net_cmd (&8069) ---
comment(0x806D, "Negative: not a net command, exit", inline=True)
comment(0x807D, "Advance past matched command text", inline=True)

# --- forward_star_cmd (&80B4) ---
comment(0x80B4, "Copy command text to FS buffer", inline=True)
comment(0x80BE, "CSD handle zero: not logged in", inline=True)

# --- fscv_handler (&80C7) ---
comment(0x80CA, "FSCV function >= 8?", inline=True)
comment(0x80CE, "X = function code for dispatch", inline=True)
comment(0x80CF, "Save Y (command text ptr hi)", inline=True)

# --- svc_star_command (&8168) ---
comment(0x816C, "Return (not our command)", inline=True)

# --- svc_9_help (&81ED) ---
comment(0x81EC, "Return (not our service call)", inline=True)

# --- print_station_info (&8218) ---
comment(0x822A, "Y=&14: OSBYTE for version number", inline=True)

# --- init_fs_vectors (&824A) ---
comment(0x824C, "Load vector address from table", inline=True)

# --- svc_1_abs_workspace (&82A2) ---
comment(0x82A8, "Return (workspace claim done)", inline=True)

# --- svc_2_private_workspace (&82AB) ---
comment(0x82AB, "Store RX buffer page high byte", inline=True)
comment(0x82AD, "Next page for NFS workspace", inline=True)
comment(0x82AE, "Store workspace page high byte", inline=True)

# --- init_tx_reply_port (&8348) ---
comment(0x8355, "Return after port setup", inline=True)

# --- prepare_cmd_with_flag (&837A) ---
comment(0x837B, "A=&2A: error ptr for retry", inline=True)

# --- bye_handler (&8383) ---
comment(0x8383, "A=&77: OSBYTE close spool/exec", inline=True)

# --- prepare_fs_cmd (&838A) ---
comment(0x8391, "A=&2A: error ptr for retry", inline=True)
comment(0x8397, "Store error ptr for TX poll", inline=True)

# --- build_send_fs_cmd (&83A4) ---
comment(0x83BE, "Load error ptr for TX retry", inline=True)
comment(0x83DC, "CLC for address addition", inline=True)

# --- handle_bput_bget (&83DD) ---
comment(0x840A, "Load handle mask for seq tracking", inline=True)
comment(0x842C, "Non-zero reply: error or done", inline=True)
comment(0x8434, "A=&E8: Tube OSWORD for BPUT", inline=True)

# --- store_fs_error (&8443) ---
comment(0x8465, "Transfer A to Y for indexing", inline=True)
comment(0x8467, "Transfer to X for return", inline=True)

# --- lang_3_execute_at_0100 (&8498) ---
comment(0x849D, "A=0: zero execution header bytes", inline=True)
comment(0x84A2, "Next byte", inline=True)
comment(0x84A3, "Loop until all zeroed", inline=True)

# --- send_to_fs (&84ED) ---
comment(0x84E1, "Advance past saved flags", inline=True)
comment(0x84EB, "A=&2A: error ptr for retry", inline=True)
comment(0x84FD, "Check for user escape condition", inline=True)

# --- check_escape_handler (&851F) ---
comment(0x8523, "Acknowledge escape via OSBYTE &7E", inline=True)

# --- parse_decimal (&85F3) ---
comment(0x85F6, "Clear accumulator workspace", inline=True)
comment(0x861A, "Return with result in A", inline=True)

# --- handle_to_mask (&861D) ---
comment(0x8635, "Transfer mask to X for return", inline=True)
comment(0x8637, "Return with mask in X", inline=True)
comment(0x863F, "Return (identity: no conversion)", inline=True)

# --- compare_addresses (&8640) ---
comment(0x8648, "Next byte", inline=True)
comment(0x864B, "Return with Z flag result", inline=True)
comment(0x8650, "Return (FSCV 7 read handles)", inline=True)

# --- set_fs_flag (&8659) ---
comment(0x8659, "OR into FS flags to set bits", inline=True)

# --- tx_poll_ff (&8668) ---
comment(0x8668, "A=&FF: full retry count", inline=True)

# --- send_fs_examine (&86F4) ---
comment(0x86F9, "A=&2A: error ptr for retry", inline=True)
comment(0x8727, "Display file info after FS reply", inline=True)

# --- copy_load_addr_from_params (&87D1) ---
comment(0x87DF, "Add 1 (of 5) to Y", inline=True)
comment(0x87E0, "Add 2 (of 5) to Y", inline=True)
comment(0x87E1, "Add 3 (of 5) to Y", inline=True)

# --- findv_handler (&896F) ---
comment(0x89A1, "A=handle bitmask for new file", inline=True)
comment(0x89A2, "OR new handle into seq tracker", inline=True)
comment(0x89A5, "Store updated sequence byte", inline=True)

# --- gbpbv_handler (&8A0E) ---
comment(0x8A0D, "Return (unsupported function)", inline=True)
comment(0x8A92, "Non-zero: branch past error ptr", inline=True)
comment(0x8A97, "A=&2A: error ptr for retry", inline=True)
comment(0x8A99, "Store error ptr for TX poll", inline=True)

# --- cat_column_separator (&8D60) ---
comment(0x8D71, "Not last column: skip CR", inline=True)
comment(0x8D73, "A=&0D: CR for column separator", inline=True)

# --- fsreply_5_set_lib (&8E15) ---
comment(0x8E18, "Non-zero: jump to restore exit", inline=True)

# --- calc_handle_offset (&8E44) ---
comment(0x8E55, "Return after calculation", inline=True)

# --- svc_8_osword (&8E76) ---
comment(0x8E7A, "Outside our OSWORD range, exit", inline=True)

# --- copy_param_block (&8EB1) ---
comment(0x8EB7, "Return after copy", inline=True)

# --- osword_0f_handler (&8EB8) ---
comment(0x8EB8, "ASL: set C if TX in progress", inline=True)
comment(0x8EBB, "Y = sub-function number", inline=True)
comment(0x8EBC, "C=0: read path", inline=True)

# --- setup_rx_buffer_ptrs (&8FCA) ---
comment(0x8FCA, "Y=&1C: RXCB template offset", inline=True)

# --- net_write_char (&9036) ---
comment(0x9056, "Enable interrupts for TX", inline=True)
comment(0x905E, "Z=1: not intercepted, pass through", inline=True)

# --- osword_dispatch (&9074) ---
comment(0x90AA, "TSX: index stack for register fix", inline=True)

# --- remote_cmd_data (&9142) ---
comment(0x9165, "Set up alt control block", inline=True)

# --- printer_select_handler (&91C4) ---
comment(0x91D0, "Store initial PFLAGS value", inline=True)

# --- flush_output_block (&9225) ---
comment(0x923D, "Load current PFLAGS", inline=True)
comment(0x9245, "Store toggled sequence number", inline=True)

# --- econet_tx_retry (&9256) ---
comment(0x9297, "Transfer count to X", inline=True)
comment(0x9298, "Test for retry exhaustion", inline=True)
comment(0x9299, "X wrapped to 0: retries exhausted", inline=True)

# --- adlc_rx_listen (&96F5) ---
comment(0x96F7, "Write CR1: RIE | TX_RESET", inline=True)
comment(0x96FC, "Write CR2: listen mode config", inline=True)

# --- nmi_rx_scout (&9700) ---
comment(0x9715, "Clear TX flags for new reception", inline=True)
comment(0x971A, "High byte of scout net handler", inline=True)
comment(0x971C, "Install next handler and RTI", inline=True)

# --- scout_error (&9741) ---
comment(0x974E, "Gentle discard: RX_DISCONTINUE", inline=True)

# --- &9751: scout data loop ---
comment(0x976D, "Copied all 12 scout bytes?", inline=True)
comment(0x9771, "Save final buffer offset", inline=True)

# --- nmi_data_rx (&9843) ---
comment(0x9854, "High byte of nmi_data_rx handler", inline=True)

# --- nmi_error_dispatch (&9894) ---
comment(0x9899, "A=&41: 'not listening' error", inline=True)

# --- discard_reset_listen (&9A4A) ---
comment(0x9A4C, "Test tx_flags for Tube transfer", inline=True)
comment(0x9A51, "A=&82: Tube release claim type", inline=True)

# --- tx_line_jammed (&9C97) ---
comment(0x9C9D, "Pop saved register", inline=True)
comment(0x9C9E, "Pop saved register", inline=True)

# --- tx_prepare (&9CB1) ---
comment(0x9CDA, "Load handler from dispatch table", inline=True)
comment(0x9CF3, "A=3: scout_status for POKE", inline=True)

# --- nmi_reply_scout (&9DC1) ---
comment(0x9DD2, "High byte of nmi_reply_cont", inline=True)
comment(0x9DD4, "Install continuation handler", inline=True)

# --- nmi_final_ack_validate (&9F24) ---
comment(0x9F39, "Load TX flags for next action", inline=True)
comment(0x9F3C, "bit7 clear: no data phase", inline=True)
comment(0x9F3E, "Install data RX handler", inline=True)

# --- rom_set_nmi_vector (&9FE8) ---
comment(0x9FF4, "Transfer ROM bank to Y", inline=True)

# ============================================================

import json
import sys

output = go(print_output=False)

_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "nfs-3.35K.asm"
output_filepath.write_text(output)
print(f"Wrote {output_filepath}", file=sys.stderr)

structured = get_structured()
json_filepath = _output_dirpath / "nfs-3.35K.json"
json_filepath.write_text(json.dumps(structured))
print(f"Wrote {json_filepath}", file=sys.stderr)
