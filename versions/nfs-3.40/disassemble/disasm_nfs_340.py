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
label(0x00CD, "nfs_temp")            # General-purpose NFS temporary
label(0x00CE, "rom_svc_num")        # ROM service number, 7=osbyte, 8=osword

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
# 3.35K labels tube_setup_transfer ($04E0), tube_rdch_handler ($04E7),
# tube_restore_regs ($04EF), tube_read_r2 ($04F7) — Tube code rewritten in 3.40.
# RDCHV is no longer claimed; &04E7 is now mid-flow in address extraction.
entry(0x0400)
entry(0x0403)
entry(0x0406)
entry(0x041E)

# Relocated code — page 5 (Tube dispatch table, WRCH, file I/O handlers)
# Reference: NFS13 (TASKS table, BPUT, BGET, RDCHZ, FIND, ARGS, STRNG, CLI, FILE)
#
# &0500-&0517: 12-entry dispatch table of word addresses.
# The R2 command byte is stored directly as the JMP (&0050) operand low byte,
# so even-numbered R2 commands index pairs of bytes in this table.
#
# R2 cmd  Entry  Addr   Handler
# ──────  ─────  ─────  ─────────────────────────────
#   &00      0   &0537  tube_osrdch (OSRDCH)
#   &02      1   &0596  tube_oscli (OSCLI)
#   &04      2   &05F2  tube_osbyte_2param (2-param, X result)
#   &06      3   &0607  tube_osbyte_long (3-param, X+Y results)
#   &08      4   &0627  tube_osword (overlapping code entry)
#   &0A      5   &0668  tube_osword_rdln (OSWORD 0, read line)
#   &0C      6   &055E  tube_osargs (OSARGS)
#   &0E      7   &052D  tube_osbget (OSBGET)
#   &10      8   &0520  tube_osbput (OSBPUT)
#   &12      9   &0542  tube_osfind (OSFIND)
#   &14     10   &05A9  tube_osfile (OSFILE)
#   &16     11   &05D1  tube_osgbpb (OSGBPB)
# 3.35K labels tube_wrch_handler ($051C), tube_send_and_poll ($051F) — Tube code rewritten
label(0x0527, "tube_poll_r1_wrch")    # Service R1 WRCH requests while waiting for R2
# 3.35K label tube_resume_poll ($0532) — Tube code rewritten
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
label(0x05D1, "tube_osgbpb")          # OSGBPB: read 13 params+reason, call &FFD1
label(0x05F2, "tube_osbyte_2param")   # OSBYTE 2-param: read X+A from R2, call &FFF4
# Dispatch table entry points (3.40 addresses)
for addr in [0x0537, 0x0596, 0x0626, 0x0607, 0x0627, 0x0668,
             0x04EF, 0x0602,
             0x0520, 0x052D, 0x0542, 0x055E, 0x05A9, 0x05F2]:
    entry(addr)

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

# Relocated code — page 6 (OSGBPB, OSBYTE, OSWORD, RDLN, event handler)
# Reference: NFS13 (GBPB, SBYTE, BYTE, WORD, RDLN, RDCHA, WRIFOR, ESCAPE, EVENT, ESCA)
# 3.35K label tube_osgbpb ($0602) — Tube code rewritten
# After JSR osgbpb, ROR A encodes carry into bit 7
# and sends it via tube_send_r2 BEFORE the 13 parameter bytes.
comment(0x0615, "Test for OSBYTE &9D (fast Tube BPUT)", inline=True)
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
label(0x8025, "dispatch_0_lo")          # First low byte entry (Svc 0)
label(0x804A, "dispatch_0_hi")          # First high byte entry (Svc 0)
expr_label(0x8024, "dispatch_0_lo-1")   # Code operand expression
expr_label(0x8049, "dispatch_0_hi-1")   # Code operand expression

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

subroutine(0x0520, "tube_osbput", hook=None,
    title="Tube OSBPUT handler (R2 cmd 8)",
    description="""\
Reads file handle and data byte from R2, then
calls OSBPUT (&FFD4) to write the byte. Falls through
to tube_reply_ack to send &7F acknowledgement.""")
subroutine(0x052D, "tube_osbget", hook=None,
    title="Tube OSBGET handler (R2 cmd 7)",
    description="""\
Reads file handle from R2, calls OSBGET (&FFD7)
to read a byte, then falls through to tube_rdch_reply
which encodes the carry flag (error) into bit 7 and
sends the result byte via R2.""")
subroutine(0x0537, "tube_osrdch", hook=None,
    title="Tube OSRDCH handler (R2 cmd 0)",
    description="""\
Calls OSRDCH (&FFE0) to read a character from
the current input stream, then falls through to
tube_rdch_reply which encodes the carry flag (error)
into bit 7 and sends the result byte via R2.""")
subroutine(0x0542, "tube_osfind", hook=None,
    title="Tube OSFIND handler (R2 cmd 9)",
    description="""\
Reads open mode from R2. If zero, reads a file
handle and closes that file. Otherwise saves the mode,
reads a filename string into &0700 via tube_read_string,
then calls OSFIND (&FFCE) to open the file. Sends the
resulting file handle (or &00) via tube_reply_byte.""")
subroutine(0x055E, "tube_osargs", hook=None,
    title="Tube OSARGS handler (R2 cmd 6)",
    description="""\
Reads file handle from R2 into Y, then reads
a 4-byte argument and reason code into zero page.
Calls OSARGS (&FFDA), sends the result A and 4-byte
return value via R2, then returns to the main loop.""")
subroutine(0x0582, "tube_read_string", hook=None,
    title="Read string from Tube R2 into buffer",
    description="""\
Loops reading bytes from tube_read_r2 into the
string buffer at &0700, storing at string_buf+Y.
Terminates on CR (&0D) or when Y wraps to zero
(256-byte overflow). Returns with X=0, Y=7 so that
XY = &0700, ready for OSCLI or OSFIND dispatch.
Called by the Tube OSCLI and OSFIND handlers.""")
subroutine(0x0596, "tube_oscli", hook=None,
    title="Tube OSCLI handler (R2 cmd 1)",
    description="""\
Reads a command string from R2 into &0700 via
tube_read_string, then calls OSCLI (&FFF7) to execute
it. Falls through to tube_reply_ack to send &7F
acknowledgement.""")
subroutine(0x05A9, "tube_osfile", hook=None,
    title="Tube OSFILE handler (R2 cmd 10)",
    description="""\
Reads a 16-byte control block into zero page,
a filename string into &0700 via tube_read_string,
and a reason code from R2. Calls OSFILE (&FFDD),
then sends the result A and updated 16-byte control
block back via R2. Returns to the main loop via mj.""")
subroutine(0x05D1, "tube_osgbpb", hook=None,
    title="Tube OSGBPB handler (R2 cmd 11)",
    description="""\
Reads a 13-byte control block and reason code
from R2 into zero page. Calls OSGBPB (&FFD1), then
sends 12 result bytes and the carry+result byte
(via tube_rdch_reply) back via R2.""")
subroutine(0x05F2, "tube_osbyte_2param", hook=None,
    title="Tube OSBYTE 2-param handler (R2 cmd 2)",
    description="""\
Reads X and A from R2, calls OSBYTE (&FFF4)
with Y=0, then sends the result X via
tube_reply_byte. Used for OSBYTE calls that take
only A and X parameters.""")
subroutine(0x0607, "tube_osbyte_long", hook=None,
    title="Tube OSBYTE 3-param handler (R2 cmd 3)",
    description="""\
Reads X, Y, and A from R2, calls OSBYTE
(&FFF4), then sends carry+Y and X as result bytes
via R2. Used for OSBYTE calls needing all three
parameters and returning both X and Y results.""")
subroutine(0x0627, "tube_osword", hook=None,
    title="Tube OSWORD handler (R2 cmd 4)",
    description="""\
Reads OSWORD number A and in-length from R2,
then reads the parameter block into &0128. Calls
OSWORD (&FFF1), then sends the out-length result
bytes from the parameter block back via R2.
Returns to the main loop via tube_return_main.""")
subroutine(0x0668, "tube_osword_rdln", hook=None,
    title="Tube OSWORD 0 handler (R2 cmd 5)",
    description="""\
Handles OSWORD 0 (read line) specially. Reads
4 parameter bytes from R2 into &0128 (max length,
min char, max char, flags). Calls OSWORD 0 (&FFF1)
to read a line, then sends &7F+CR or the input line
byte-by-byte via R2, followed by &80 (error/escape)
or &7F (success).""")
subroutine(0x0695, "tube_send_r2", hook=None,
    title="Send byte to Tube data register R2",
    description="""\
Polls Tube status register 2 until bit 6 (TDRA)
is set, then writes A to the data register. Uses a
tight BIT/BVC polling loop. Called by 12 sites
across the Tube host code for all R2 data
transmission: command responses, file data, OSBYTE
results, and control block bytes.""")
subroutine(0x069E, "tube_send_r4", hook=None,
    title="Send byte to Tube data register R4",
    description="""\
Polls Tube status register 4 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R4 is the command/control
channel used for address claims (ADRR), data transfer
setup (SENDW), and release commands. Called by 7
sites, primarily during tube_release_claim and
tube_transfer_setup sequences.""")
subroutine(0x06BC, "tube_send_r1", hook=None,
    title="Send byte to Tube data register R1",
    description="""\
Polls Tube status register 1 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R1 is used for asynchronous
event and escape notification to the co-processor.
Called by tube_event_handler to forward event type,
Y, and X parameters, and reached via BMI from
tube_escape_check when the escape flag is set.""")
subroutine(0x06C5, "tube_read_r2", hook=None,
    title="Read a byte from Tube data register R2",
    description="""\
Polls Tube status register 2 until data is available
(bit 7 set), then loads A from Tube data register 2.
Called by all Tube dispatch handlers that receive data
or parameters from the co-processor.""")

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

# --- Decimal number parser (&8620-&8642) ---
# parse_decimal label created by subroutine() call below.

# --- File handle ↔ bitmask conversion ---
# handle_to_mask_a, handle_to_mask_clc, handle_to_mask and mask_to_handle
# labels created by subroutine() calls below.

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
label(0x8F22, "logon3")               # NFS07: logon handler 3
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
NFS ROM 3.40 disassembly (Acorn Econet filing system)
====================================================""")

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
# The dispatch code at &80EC/&80F0 reads via LDA dispatch_0_hi-1,X
# and LDA dispatch_0_lo-1,X. After the loop adds Y+1 to X,
# the final byte addresses for logical entry i are:
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
# dispatch_0_hi table and dispatch_net_cmd at &806F).
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
# &8024 is the dispatch table pad byte — the dispatcher adds Y+1
# to X before indexing, so entry 0 at &8025 is the first handler.
comment(0x8021, "Four bytes with unknown purpose.")
for addr in range(0x8021, 0x8025):
    byte(addr)
comment(0x8021, "Purpose unknown", inline=True)
comment(0x8022, "Purpose unknown", inline=True)
comment(0x8023, "Purpose unknown", inline=True)
comment(0x8024, "Purpose unknown", inline=True)

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
# of dispatch_0_hi area), hi bytes are at &8069-&806E (between the
# main dispatch_0_hi table and dispatch_net_cmd at &806F).
for i in range(31, 37):
    rts_code_ptr(0x8025 + i, 0x804A + i)

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
entry(0x9B35)   # IRQ service: check SR, dispatch TX done handlers

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
Uses workspace offsets (&A6/&A7) for nmi_tx_block.""")

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


# ============================================================
# Decimal number parser (&8620)
# ============================================================
subroutine(0x8620, "parse_decimal",
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
             "x": "preserved",
             "y": "offset past last digit parsed"})
comment(0x8620, "Zero accumulator", inline=True)
comment(0x8624, "Load next char from buffer", inline=True)
comment(0x8626, "Dot separator?", inline=True)
comment(0x8628, "Yes: exit with C=1 (dot found)", inline=True)
comment(0x862A, "Control char or space: done", inline=True)
comment(0x862C, "Mask ASCII digit to 0-9", inline=True)
comment(0x862E, "Save new digit", inline=True)
comment(0x8630, "Running total * 2", inline=True)
comment(0x8632, "A = running total * 2", inline=True)
comment(0x8634, "A = running total * 4", inline=True)
comment(0x8635, "A = running total * 8", inline=True)
comment(0x8636, "+ total*2 = total * 10", inline=True)
comment(0x8638, "+ digit = total*10 + digit", inline=True)
comment(0x863A, "Store new running total", inline=True)
comment(0x863C, "Advance to next char", inline=True)
comment(0x863D, "Loop (always: Y won't wrap to 0)", inline=True)
comment(0x863F, "No dot found: C=0", inline=True)
comment(0x8640, "Return result in A", inline=True)

# ============================================================
# File handle conversion (&8643-&8645)
# ============================================================
subroutine(0x8643, "handle_to_mask_a", hook=None,
    title="Convert handle in A to bitmask",
    description="""\
Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""")

subroutine(0x8644, "handle_to_mask_clc", hook=None,
    title="Convert handle to bitmask (carry cleared)",
    description="""\
Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""")

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
Callers needing to move the handle from A use handle_to_mask_a;
callers needing carry cleared use handle_to_mask_clc.""",
    on_entry={"y": "handle number",
              "c": "0: convert, 1 with Y=0: skip, 1 with Y!=0: convert"},
    on_exit={"a": "preserved",
             "x": "preserved",
             "y": "bitmask (single bit set) or &FF if handle invalid"})
comment(0x8645, "Save A (will be restored on exit)", inline=True)
comment(0x8646, "Save X (will be restored on exit)", inline=True)
comment(0x8647, "  (second half of X save)", inline=True)
comment(0x8648, "A = handle from Y", inline=True)
comment(0x8649, "C=0: always convert", inline=True)
comment(0x864B, "C=1 and Y=0: skip (handle 0 = none)", inline=True)
comment(0x864D, "C=1 and Y!=0: convert", inline=True)
comment(0x864E, "A = handle - &1F (1-based bit position)", inline=True)
comment(0x8650, "X = shift count", inline=True)
comment(0x8651, "Start with bit 0 set", inline=True)
comment(0x8653, "Shift bit left", inline=True)
comment(0x8654, "Count down", inline=True)
comment(0x8655, "Loop until correct position", inline=True)
comment(0x8657, "Undo final extra shift", inline=True)
comment(0x8658, "Y = resulting bitmask", inline=True)
comment(0x8659, "Non-zero: valid mask, skip to exit", inline=True)
comment(0x865B, "Zero: invalid handle, set Y=&FF", inline=True)
comment(0x865C, "Restore X", inline=True)
comment(0x865E, "Restore A", inline=True)

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
comment(0x8660, "X = &1F (handle base - 1)", inline=True)
comment(0x8662, "Count this bit position", inline=True)
comment(0x8663, "Shift mask right; C=0 when done", inline=True)
comment(0x8664, "Loop until all bits shifted out", inline=True)
comment(0x8666, "A = X = &1F + bit position = handle", inline=True)

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
subroutine(0x8679, "set_fs_flag", hook=None,
    title="Set bit(s) in EOF hint flags (&0E07)",
    description="""\
ORs A into fs_eof_flags then stores the result via
store_fs_flag. Each bit represents one of up to 8 open file
handles. When clear, the file is definitely NOT at EOF. When
set, the fileserver must be queried to confirm EOF status.
This negative-cache optimisation avoids expensive network
round-trips for the common case. The hint is cleared when
the file pointer is updated (since seeking away from EOF
invalidates the hint) and set after BGET/OPEN/EOF operations
that might have reached the end.""")

subroutine(0x867E, "clear_fs_flag", hook=None,
    title="Clear bit(s) in FS flags (&0E07)",
    description="""\
Inverts A (EOR #&FF), then ANDs the result into fs_eof_flags
to clear the specified bits.""")

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
# Dispatch table comments (&8025-&8068)
# ============================================================
comment(0x8025, """\
Dispatch table: low bytes of (handler_address - 1)
Each entry stores the low byte of a handler address minus 1,
for use with the PHA/PHA/RTS dispatch trick at &80E7.
See dispatch_0_hi (&804A) for the corresponding high bytes.

Five callers share this table via different Y base offsets:
  Y=&00  Service calls 0-12       (indices 0-13)
  Y=&0E  Language entry reasons    (indices 14-18)
  Y=&13  FSCV codes 0-7           (indices 19-26)
  Y=&17  FS reply handlers        (indices 27-32)
  Y=&21  *NET1-4 sub-commands     (indices 33-36)

Lo bytes for the last 6 entries (indices 31-36) occupy
&8044-&8049, immediately before the hi bytes. Their hi
bytes are at &8069-&806E, after dispatch_0_hi.""")

comment(0x804A, """\
Dispatch table: high bytes of (handler_address - 1)
Paired with dispatch_0_lo (&8025). Together they form a table
of 37 handler addresses, used via the PHA/PHA/RTS trick at
&80E7.""")

# Dispatch table inline comments (lo and hi bytes).
# The comment bodies are defined once and emitted for both halves so
# they stay in sync.
dispatch_comments = [
    # Service call handlers (Y=&00, indices 0-13)
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
    "Svc 13: select NFS (intercepted before dispatch)",
    # Language entry handlers (Y=&0E, indices 14-18)
    "Lang 0: no language / Tube",
    "Lang 1: normal startup",
    "Lang 2: softkey byte (Electron)",
    "Lang 3: softkey length (Electron)",
    "Lang 4: remote validated",
    # FSCV handlers (Y=&13, indices 19-26)
    "FSCV 0: *OPT",
    "FSCV 1: EOF check",
    "FSCV 2: */ (run)",
    "FSCV 3: unrecognised star command",
    "FSCV 4: *RUN",
    "FSCV 5: *CAT",
    "FSCV 6: shutdown",
    "FSCV 7: read handle range",
    # FS reply handlers (Y=&17, indices 27-32)
    "FS reply: print directory name",
    "FS reply: copy handles + boot",
    "FS reply: copy handles",
    "FS reply: set CSD handle",
    "FS reply: notify + execute",
    "FS reply: set library handle",
    # *NET sub-command handlers (Y=&21, indices 33-36)
    "*NET1: read handle from packet",
    "*NET2: read handle from workspace",
    "*NET3: close handle",
    "*NET4: resume remote",
]
for i, body in enumerate(dispatch_comments):
    comment(0x8025 + i, f"lo - {body}", inline=True)
    comment(0x804A + i, f"hi - {body}", inline=True)

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
Called when the NFS ROM is entered as a language. Although rom_type
(&82) does not set the language bit, the MOS enters this point
after NFS claims service &FE (Tube post-init). X = reason code
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
All other service calls < &0D dispatch via c8146.""")

# ============================================================
# Init: set up vectors and copy code (&8140)
# ============================================================
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
# Check boot key (&8224)
# ============================================================
subroutine(0x8224, "check_boot_key", hook=None,
    title="Check boot key",
    description="""\
Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")

# ============================================================
# Print station identification (&822E)
# ============================================================
subroutine(0x822E, "print_station_info", hook=None,
    title="Print station identification",
    description="""\
Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")

# ============================================================
# Initialise filing system vectors (&8260)
# ============================================================
subroutine(0x8260, "init_fs_vectors", hook=None,
    title="Initialise filing system vectors",
    description="""\
Copies 14 bytes from fs_vector_addrs (&8296) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from svc_13_select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")

comment(0x8260, "Copy 14 bytes: FS vector addresses → FILEV-FSCV", inline=True)

# ============================================================
# Auto-boot command string (&828E)
# ============================================================
string(0x828E, 8)
comment(0x828E, """\
Synthetic auto-boot command string. "I " does not match any
entry in NFS's local command table — "I." requires a dot, and
"I AM" requires 'A' after the space — so fscv_3_star_cmd
forwards the entire string to the fileserver, which executes
the .BOOT file.""")

# ============================================================
# FS vector dispatch and handler addresses (&8296)
# ============================================================
subroutine(0x8296, "fs_vector_addrs", hook=None,
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
for i, name in enumerate(["FILEV", "ARGSV", "BGETV", "BPUTV",
                           "GBPBV", "FINDV", "FSCV"]):
    addr = 0x8296 + i * 2
    word(addr)
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
    word(base_addr)
    comment(base_addr, f"{name} handler (&{handler_addr:04X})", inline=True)
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
(OSBYTE &7A): if no key is pressed, auto-boot proceeds directly
via print_station_info. If a key is pressed, falls through to
check_boot_key: the 'N' key (matrix address &55) proceeds with
auto-boot, any other key causes the auto-boot to be declined.""")

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
label(0x835E, "match_rom_string")
comment(0x835E, "Y = saved text pointer offset", inline=True)
comment(0x8360, "Load next input character", inline=True)
comment(0x8362, "Is it a '.' (abbreviation)?", inline=True)
comment(0x8364, "Yes: skip to space skipper (match)", inline=True)
comment(0x8366, "Force uppercase (clear bit 5)", inline=True)
comment(0x8368, "Input char is NUL/space: check ROM byte", inline=True)
comment(0x836A, "Compare with ROM string byte", inline=True)
comment(0x836D, "Mismatch: check if ROM string ended", inline=True)
comment(0x836F, "Advance input pointer", inline=True)
comment(0x8370, "Advance ROM string pointer", inline=True)
comment(0x8371, "Continue matching (always taken)", inline=True)
comment(0x8373, "Load ROM string byte at match point", inline=True)
comment(0x8376, "Zero = end of ROM string = full match", inline=True)
comment(0x8378, "Non-zero = partial/no match; Z=0", inline=True)
comment(0x8379, "Skip this space", inline=True)
comment(0x837A, "Load next input character", inline=True)
comment(0x837C, "Is it a space?", inline=True)
comment(0x837E, "Yes: keep skipping", inline=True)
comment(0x8380, "XOR with CR: Z=1 if end of line", inline=True)

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
catch-all entry which forwards the command to the fileserver.
Falls through to run_fscv_cmd.""")

# ============================================================
# Run FSCV command from ROM (&8289)
# ============================================================
subroutine(0x8289, "run_fscv_cmd", hook=None,
    title="Run FSCV command from ROM",
    description="""\
Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
to execute the command string at (X, Y). X is pre-loaded by the
caller with the low byte of the string address. Also used as a
data base address by store_rom_ptr_pair for Y-indexed access to
the handler address table.""")

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
OSBYTE &77 (close SPOOL/EXEC files) to release the
Econet network printer on FS switch.""")

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
# Check escape handler (&854D)
# ============================================================
subroutine(0x854D, "check_escape_handler", hook=None,
    title="Test MOS escape flag and abort if pending",
    description="""\
Tests MOS escape flag (&FF bit 7). If escape is pending:
acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
the control block via (net_tx_ptr),Y, and branches to the
NLISTN error path. If no escape, returns immediately.""")

# ============================================================
# Error message table (&8579)
# ============================================================
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
comment(0x8A16, "X=&FC: index into &0E06 area (wraps to 0)", inline=True)
comment(0x8A18, "Load byte from param block", inline=True)
comment(0x8A1A, "Test sign of adjustment direction", inline=True)
comment(0x8A1C, "Negative: subtract instead", inline=True)
comment(0x8A1E, "Add adjustment value", inline=True)
comment(0x8A21, "Skip to store result", inline=True)
comment(0x8A24, "Subtract adjustment value", inline=True)
comment(0x8A27, "Store adjusted byte back", inline=True)
comment(0x8A29, "Next param block byte", inline=True)
comment(0x8A2A, "Next adjustment byte (X wraps &FC->&00)", inline=True)
comment(0x8A2B, "Loop 4 times (X=&FC,&FD,&FE,&FF,done)", inline=True)

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

comment(0x89C6, """\
OR handle bit into fs_sequence_nos (&0E08) to prevent
a newly opened file inheriting a stale sequence number
from a previous file using the same handle.""")

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
Option name encoding: the boot option names ("Off",
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
"*I AM <station>" or "*I AM <network>.<station>". Also used as
the station number parser for "*NET <network>.<station>".
Skips leading spaces, then calls parse_decimal for the first
number. If a dot separator was found (carry set), it stores the
result directly as the network (&0E01) and calls parse_decimal
again for the station (&0E00). With a single number, it is stored
as the station and the network defaults to 0 (local). If a colon
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
comment(0x8D77, "Start copying from offset 0", inline=True)
comment(0x8D79, "Load next byte from source string", inline=True)
comment(0x8D7E, "Advance write position", inline=True)
comment(0x8D80, "XOR with CR: result=0 if byte was CR", inline=True)
comment(0x8D82, "Loop until CR copied", inline=True)

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
comment(0x8E47, "A = handle * 2", inline=True)
comment(0x8E48, "A = handle * 4", inline=True)
comment(0x8E49, "Push handle*4 onto stack", inline=True)
comment(0x8E4A, "A = handle * 8", inline=True)
comment(0x8E4B, "X = stack pointer", inline=True)
comment(0x8E4C, "A = handle*8 + handle*4 = handle*12", inline=True)
comment(0x8E4F, "Y = offset into handle workspace", inline=True)
comment(0x8E50, "Clean up stack (discard handle*4)", inline=True)
comment(0x8E51, "Offset >= &48? (6 handles max)", inline=True)
comment(0x8E53, "Valid: return with C clear", inline=True)
comment(0x8E55, "Invalid: Y = 0", inline=True)
comment(0x8E57, "A = 0, C set (error)", inline=True)

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
comment(0x8FAA, "Enable interrupts before transmit", inline=True)
comment(0x8FB0, "Dest station = &FFFF (accept reply from any station)", inline=True)

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

comment(0x900A, "Y=&04: advance to station address", inline=True)
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
byte(0x91A3, 1)
comment(0x91AE, "→ Y=&03 / Y=&75", inline=True)
byte(0x91A4, 1)
byte(0x91A5, 1)
byte(0x91A6, 1)
comment(0x91A6, "PAGE byte → Y=&06 / Y=&78", inline=True)
byte(0x91A7, 1)
comment(0x91A7, "→ Y=&07 / Y=&79", inline=True)
byte(0x91A8, 1)
comment(0x91B3, "→ Y=&08 / Y=&7A", inline=True)
byte(0x91A9, 1)
comment(0x91B4, "→ Y=&09 / Y=&7B", inline=True)
byte(0x91AA, 1)
byte(0x91AB, 1)
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
# Bidirectional block copy (&8F14)
# ============================================================
subroutine(0x8F1C, "copy_param_block", hook=None,
    title="Bidirectional block copy between OSWORD param block and workspace.",
    description="""\
C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)""")
comment(0x8F14, "C=0: skip param-to-workspace copy", inline=True)
comment(0x8F1A, "Load byte from workspace", inline=True)
comment(0x8F1C, "Store to param block (no-op if C=1)", inline=True)
comment(0x8F1E, "Advance to next byte", inline=True)

# ============================================================
# OSWORD handler block comments
# ============================================================
label(0x8F22, "return_copy_param")       # Return from copy_param_block

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
Issues OSBYTE &8F with X=&0C (NMI claim service request) before
copying the NMI shim. Sub-entry at &968A skips the service
request for quick re-init. Then copies 32 bytes of
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
12-entry table at &0500). The R2 command byte is stored at &55
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
  &04D2: sub_c04d2 — extract relocation address from ROM table""")

subroutine(0x0500, "tube_dispatch_table", hook=None,
    title="Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)",
    description="""\
Copied from ROM at &944D during init. Contains:
  &0500: tube_dispatch_table — 12-entry handler address table
  &0518: R2 command byte table — 8 even command bytes (&00-&0E)
  &0520: tube_osbput — write byte to file
  &052D: tube_osbget — read byte from file
  &0537: tube_osrdch — read character
  &053A: tube_rdch_reply — ROR carry into byte, send via R2
  &053D: tube_release_return — dead code (unreferenced)
  &0542: tube_osfind — open file
  &0552: tube_osfind_close — close file (A=0)
  &055E: tube_osargs — file argument read/write
  &0582: tube_read_string — read CR-terminated string into &0700
  &0596: tube_oscli — execute * command
  &059C: tube_reply_ack — send &7F acknowledge
  &059E: tube_reply_byte — send byte and return to main loop
  &05A9: tube_osfile — whole file operation""")

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
# Discard paths (&9A2E / &9A3D)
# ============================================================
subroutine(0x9A2E, "discard_reset_listen", hook=None,
    title="Discard with full ADLC reset",
    description="""\
Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
then falls through to install_rx_scout_handler. Used when the ADLC is
in an unexpected state and needs a hard reset before returning
to idle listen mode. 5 references — the main error recovery path.""")

subroutine(0x9A3D, "discard_listen", hook=None,
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
comment(0x9F28, "Unreferenced data block (purpose unknown)")
byte(0x9F28, 16)

# ============================================================
# Transfer size calculation (&9F38)
# ============================================================
subroutine(0x9F38, "tx_calc_transfer", hook=None,
    title="Calculate transfer size",
    description="""\
Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")
comment(0x9F38, "Load RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x9F3D, "AND with TX block[7] (byte 3)", inline=True)
comment(0x9F3F, "Both &FF = no buffer?", inline=True)
comment(0x9F41, "Yes: fallback path", inline=True)
comment(0x9F43, "Tube transfer in progress?", inline=True)
comment(0x9F46, "No: fallback path", inline=True)
comment(0x9F4B, "Set bit 1 (transfer complete)", inline=True)
comment(0x9F50, "Init borrow for 4-byte subtract", inline=True)
comment(0x9F51, "Save carry on stack", inline=True)
comment(0x9F52, "Y=4: start at RXCB offset 4", inline=True)
comment(0x9F54, "Load RXCB[Y] (current ptr byte)", inline=True)
comment(0x9F56, "Y += 4: advance to RXCB[Y+4]", inline=True)
comment(0x9F5A, "Restore borrow from previous byte", inline=True)
comment(0x9F5B, "Subtract RXCB[Y+4] (start ptr byte)", inline=True)
comment(0x9F5D, "Store result byte", inline=True)
comment(0x9F60, "Y -= 3: next source byte", inline=True)
comment(0x9F63, "Save borrow for next byte", inline=True)
comment(0x9F64, "Done all 4 bytes?", inline=True)
comment(0x9F66, "No: next byte pair", inline=True)
comment(0x9F68, "Discard final borrow", inline=True)
comment(0x9F69, "A = saved X", inline=True)
comment(0x9F6A, "Save X", inline=True)
comment(0x9F6B, "Compute address of RXCB+4", inline=True)
comment(0x9F70, "X = low byte of RXCB+4", inline=True)
comment(0x9F71, "Y = high byte of RXCB ptr", inline=True)
comment(0x9F73, "Tube claim type &C2", inline=True)
comment(0x9F78, "No Tube: skip reclaim", inline=True)
comment(0x9F7A, "Tube: reclaim with scout status", inline=True)
comment(0x9F80, "C=1: Tube address claimed", inline=True)
comment(0x9F81, "Restore X", inline=True)
comment(0x9F86, "Load RXCB[4] (current ptr lo)", inline=True)
comment(0x9F8B, "Subtract RXCB[8] (start ptr lo)", inline=True)
comment(0x9F8D, "Store transfer size lo", inline=True)
comment(0x9F91, "Load RXCB[5] (current ptr hi)", inline=True)
comment(0x9F99, "Copy RXCB[8] to open port buffer lo", inline=True)
comment(0x9FA4, "Store transfer size hi", inline=True)
comment(0x9FA6, "Return with C=1", inline=True)

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

comment(0x9727, "Network = 0 (local): clear tx_flags", inline=True)
comment(0x972A, "Store Y offset for scout data buffer", inline=True)

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
comment(0x9D9D, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x9DA0, "Not our station -- error/reject", inline=True)

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
comment(0x9DB7, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
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
comment(0x9DE8, "Install next handler at &9EBA into &0D4B/&0D4C", inline=True)
comment(0x9DF2, "Load dest station for scout ACK TX", inline=True)
comment(0x9DF5, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9DF8, "TDRA not ready -- error", inline=True)
comment(0x9DFA, "Write dest station to TX FIFO", inline=True)

# ============================================================
# TX data phase: write src address (&9E3A)
# ============================================================
subroutine(0x9E0A, "nmi_scout_ack_src", hook=None,
    title="TX scout ACK: write source address",
    description="""\
Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
comment(0x9E12, "Write our station to TX FIFO", inline=True)

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

comment(0x9EDC, "BIT SR2: test RDA", inline=True)
comment(0x9EDF, "No RDA -- error", inline=True)
comment(0x9EE1, "Read dest network", inline=True)
comment(0x9EE4, "Non-zero -- network mismatch, error", inline=True)
comment(0x9EEA, "BIT SR1: test IRQ -- more data ready?", inline=True)

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
label(0x0054, "tube_xfer_page")      # Transfer source page high byte (&80 default)
label(0x0055, "tube_xfer_addr_2")    # Transfer address byte 2
label(0x0056, "tube_xfer_addr_3")    # Transfer address byte 3
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
comment(0x0412, "Not our address: return", inline=True)
comment(0x0420, "Store to claim-in-progress flag", inline=True)
comment(0x0422, "Return from tube_post_init", inline=True)
label(0x0423, "addr_claim_external")  # External address claim check (another host)
comment(0x0423, "Another host claiming; check if we're owner", inline=True)
comment(0x0425, "C=1: we have an active claim", inline=True)
comment(0x0427, "Compare with our claimed address", inline=True)
comment(0x0429, "Match: return (we already have it)", inline=True)
comment(0x042B, "Not ours: CLC = we don't own this address", inline=True)
comment(0x042C, "Return with C=0 (claim denied)", inline=True)
label(0x042D, "accept_new_claim")    # BCS: active claim exists, store incoming address
comment(0x042D, "Accept new claim: update our address", inline=True)
comment(0x042F, "Return with address updated", inline=True)
label(0x0430, "tube_transfer_setup")  # Data transfer setup (SENDW protocol)
comment(0x0430, "PHP: save interrupt state", inline=True)
comment(0x0431, "SEI: disable interrupts for R4 protocol", inline=True)
comment(0x0432, "Save 16-bit transfer address from (X,Y)", inline=True)
comment(0x0434, "Store address pointer low byte", inline=True)
comment(0x0436, "Send transfer type byte to co-processor", inline=True)
comment(0x0439, "X = transfer type for table lookup", inline=True)
comment(0x043A, "Y=3: send 4 bytes (address + claimed addr)", inline=True)
comment(0x043C, "Send our claimed address + 4-byte xfer addr", inline=True)
label(0x0441, "send_xfer_addr_bytes") # Send 4-byte transfer address to co-processor via R4
comment(0x0441, "Load transfer address byte from (X,Y)", inline=True)
comment(0x0443, "Send address byte to co-processor via R4", inline=True)
comment(0x0446, "Previous byte (big-endian: 3,2,1,0)", inline=True)
comment(0x0447, "Loop for all 4 address bytes", inline=True)
comment(0x044C, "Y=&18: enable Tube control register", inline=True)
comment(0x044E, "Enable Tube interrupt generation", inline=True)
comment(0x0451, "Look up Tube control bits for this xfer type", inline=True)
comment(0x0454, "Apply transfer-specific control bits", inline=True)
comment(0x0457, "LSR: check bit 2 (2-byte flush needed?)", inline=True)
comment(0x0458, "LSR: shift bit 2 to carry", inline=True)
label(0x0459, "poll_r4_copro_ack")   # Poll R4 status waiting for co-processor acknowledgement
comment(0x0459, "Poll R4 status for co-processor response", inline=True)
comment(0x045C, "Bit 6 clear: not ready, keep polling", inline=True)
comment(0x045E, "R4 bit 7: co-processor acknowledged transfer", inline=True)
comment(0x0460, "Type 4 = SENDW (host-to-parasite word xfer)", inline=True)
comment(0x0462, "Not SENDW type: skip release path", inline=True)
label(0x0464, "tube_sendw_complete") # SENDW done: release claim, sync R2, restart
comment(0x0464, "SENDW complete: release, sync, restart", inline=True)
comment(0x0467, "Sync via R2 send", inline=True)
comment(0x046A, "Restart Tube main loop", inline=True)
label(0x0473, "copro_ack_nmi_check") # BCS: co-processor acknowledged, test NMI release
comment(0x0473, "LSR: check bit 0 (NMI used?)", inline=True)
comment(0x0474, "C=0: NMI not used, skip NMI release", inline=True)
comment(0x0476, "Release Tube NMI (transfer used interrupts)", inline=True)
comment(0x0478, "Write &88 to Tube control to release NMI", inline=True)
label(0x047B, "skip_nmi_release")    # BNE/BCC: skip NMI release, PLP/RTS
comment(0x047B, "Restore interrupt state", inline=True)
comment(0x047C, "Return from transfer setup", inline=True)
label(0x047D, "tube_begin")          # BEGIN: startup entry for Tube host code
comment(0x047D, "BEGIN: enable interrupts for Tube host code", inline=True)
comment(0x047E, "C=1: hard break, claim addr &FF", inline=True)
comment(0x0480, "C=0, A!=0: re-init path", inline=True)
comment(0x0482, "Z=1 from C=0 path: just acknowledge", inline=True)
label(0x0485, "check_break_type")    # BNE: not soft break, query OSBYTE &FD reset type
comment(0x0485, "X=0 for OSBYTE", inline=True)
comment(0x0487, "Y=&FF for OSBYTE", inline=True)
comment(0x0489, "OSBYTE &FD: what type of reset was this?", inline=True)
comment(0x048F, "Soft break (X=0): re-init Tube and restart", inline=True)
label(0x0491, "claim_addr_ff")       # Hard break or retry: claim address &FF
comment(0x0491, "Claim address &FF (startup = highest prio)", inline=True)
comment(0x0493, "Request address claim from Tube system", inline=True)
comment(0x0496, "C=0: claim failed, retry", inline=True)
comment(0x0498, "Init reloc pointers from ROM header", inline=True)
label(0x049B, "next_rom_page")       # BVC: more pages to send, loop SENDW
comment(0x049B, "R4 cmd 7: SENDW to send ROM to parasite", inline=True)
comment(0x049D, "Set up Tube for SENDW transfer", inline=True)
comment(0x04A0, "Y=0: start at beginning of page", inline=True)
comment(0x04A2, "Store to zero page pointer low byte", inline=True)
label(0x04A4, "send_rom_page_bytes") # Send 256 bytes of one ROM page to co-processor via R3
comment(0x04A4, "Send 256-byte page via R3, byte at a time", inline=True)
comment(0x04A6, "Write byte to Tube R3 data register", inline=True)
comment(0x04AC, "Next byte in page", inline=True)
comment(0x04AD, "Loop for all 256 bytes", inline=True)
comment(0x04AF, "Increment 24-bit destination addr", inline=True)
comment(0x04B1, "No carry: skip higher bytes", inline=True)
comment(0x04B3, "Carry into second byte", inline=True)
comment(0x04B5, "No carry: skip third byte", inline=True)
comment(0x04B7, "Carry into third byte", inline=True)
label(0x04B9, "skip_addr_carry")     # BNE: skip 24-bit destination address carry
comment(0x04B9, "Increment page counter", inline=True)
comment(0x04BB, "Bit 6 set = all pages transferred", inline=True)
comment(0x04BD, "More pages: loop back to SENDW", inline=True)
comment(0x04BF, "Re-init reloc pointers for final claim", inline=True)
comment(0x04C2, "A=4: transfer type for final address claim", inline=True)
label(0x04C4, "tube_claim_default")  # Claim default Tube transfer address (&0053)
comment(0x04C4, "Y=0: transfer address low byte", inline=True)
comment(0x04C6, "X=&53: transfer address high byte (&0053)", inline=True)
comment(0x04C8, "Claim Tube address for transfer", inline=True)
comment(0x04CB, "Init: start sending from &8000", inline=True)
comment(0x04CD, "Store &80 as source page high byte", inline=True)
comment(0x04CF, "Store &80 as page counter initial value", inline=True)
comment(0x04D1, "A=&20: bit 5 mask for ROM type check", inline=True)
comment(0x04D3, "ROM type bit 5: reloc address in header?", inline=True)
comment(0x04D6, "Y = 0 or &20 (reloc flag)", inline=True)
comment(0x04D7, "Store as transfer address selector", inline=True)
comment(0x04D9, "No reloc addr: use defaults", inline=True)
comment(0x04DB, "Skip past copyright string to find reloc addr", inline=True)
label(0x04DE, "scan_copyright_end")  # Scan past null-terminated copyright string in ROM header
comment(0x04DE, "Skip past null-terminated copyright string", inline=True)
comment(0x04DF, "Load next byte from ROM header", inline=True)
comment(0x04E2, "Loop until null terminator found", inline=True)
comment(0x04E4, "Read 4-byte reloc address from ROM header", inline=True)
comment(0x04E7, "Store reloc addr byte 1 as transfer addr", inline=True)
comment(0x04E9, "Load reloc addr byte 2", inline=True)
comment(0x04EC, "Store as source page start", inline=True)
comment(0x04EE, "Load reloc addr byte 3", inline=True)
comment(0x04F1, "Load reloc addr byte 4 (highest)", inline=True)
label(0x04F4, "store_xfer_end_addr") # BEQ: no reloc flag, store default end address
comment(0x04F4, "Store high byte of end address", inline=True)
comment(0x04F6, "Store byte 3 of end address", inline=True)
comment(0x04F8, "Return with pointers initialised", inline=True)
comment(0x0523, "Y=channel handle from R2", inline=True)
comment(0x0524, "Read data byte from R2 for BPUT", inline=True)
comment(0x052A, "BPUT done: send acknowledge, return", inline=True)
comment(0x0530, "Y=channel handle for OSBGET", inline=True)
comment(0x0534, "Send carry+byte reply (BGET result)", inline=True)
comment(0x053A, "ROR A: encode carry (error flag) into bit 7", inline=True)
comment(0x053F, "Return to Tube main loop", inline=True)
comment(0x0545, "A=0: close file, else open with filename", inline=True)
comment(0x0547, "Save open mode while reading filename", inline=True)
comment(0x0548, "Read filename string from R2 into &0700", inline=True)
comment(0x054B, "Recover open mode from stack", inline=True)
comment(0x054F, "Send file handle result to co-processor", inline=True)
comment(0x0552, "OSFIND close: read handle from R2", inline=True)
comment(0x0555, "Y=handle to close", inline=True)
comment(0x0556, "A=0: close command for OSFIND", inline=True)
comment(0x055B, "Close done: send acknowledge, return", inline=True)
comment(0x0561, "Y=file handle for OSARGS", inline=True)
comment(0x0562, "Read 4-byte arg + reason from R2 into ZP", inline=True)
label(0x0564, "read_osargs_params")  # Read 4 OSARGS parameter bytes from R2 into zero page
comment(0x0564, "Read next param byte from R2", inline=True)
comment(0x0567, "Params stored at &00-&03 (little-endian)", inline=True)
comment(0x0569, "Decrement byte counter", inline=True)
comment(0x056A, "Loop for 4 bytes", inline=True)
comment(0x056C, "Read OSARGS reason code from R2", inline=True)
comment(0x0572, "Send result A back to co-processor", inline=True)
comment(0x0575, "Return 4-byte result from ZP &00-&03", inline=True)
label(0x0577, "send_osargs_result")  # Send 4 OSARGS result bytes back to co-processor via R2
comment(0x0577, "Load result byte from zero page", inline=True)
comment(0x0579, "Send byte to co-processor via R2", inline=True)
comment(0x057C, "Previous byte (count down)", inline=True)
comment(0x057D, "Loop for all 4 bytes", inline=True)
comment(0x057F, "Return to Tube main loop", inline=True)
comment(0x0582, "X=0: initialise string buffer index", inline=True)
comment(0x0584, "X=0, Y=0: buffer at &0700, offset 0", inline=True)
comment(0x0586, "Read next string byte from R2", inline=True)
comment(0x0589, "Store byte in string buffer at &0700+Y", inline=True)
comment(0x058C, "Next buffer position", inline=True)
comment(0x058D, "Y overflow: string too long, truncate", inline=True)
comment(0x058F, "Check for CR terminator", inline=True)
comment(0x0591, "Not CR: continue reading string", inline=True)
label(0x0593, "string_buf_done")     # BEQ: overflow or CR found, set XY=&0700/RTS
comment(0x0593, "Y=7: set XY=&0700 for OSCLI/OSFIND", inline=True)
comment(0x0595, "Return with XY pointing to &0700", inline=True)
comment(0x0599, "Execute * command via OSCLI", inline=True)
comment(0x059C, "&7F = success acknowledgement", inline=True)
comment(0x059E, "Poll R2 status until ready", inline=True)
comment(0x05A1, "Bit 6 clear: not ready, loop", inline=True)
comment(0x05A3, "Write byte to R2 data register", inline=True)
comment(0x05A6, "Return to Tube main loop", inline=True)
comment(0x05AB, "Read next control block byte from R2", inline=True)
comment(0x05AE, "Store at &01+X (descending)", inline=True)
comment(0x05B0, "Decrement byte counter", inline=True)
comment(0x05B1, "Loop for all 16 bytes", inline=True)
comment(0x05B3, "Read filename string from R2 into &0700", inline=True)
comment(0x05B6, "XY=&0700: filename pointer for OSFILE", inline=True)
comment(0x05B8, "Store Y=7 as pointer high byte", inline=True)
comment(0x05BA, "Y=0 for OSFILE control block offset", inline=True)
comment(0x05BC, "Read OSFILE reason code from R2", inline=True)
comment(0x05BF, "Execute OSFILE operation", inline=True)
comment(0x05C2, "Send result A (object type) to co-processor", inline=True)
comment(0x05C5, "Return 16-byte control block to co-processor", inline=True)
label(0x05C7, "send_osfile_ctrl_blk") # Send 16-byte OSFILE control block to co-processor via R2
comment(0x05C7, "Load control block byte", inline=True)
comment(0x05C9, "Send byte to co-processor via R2", inline=True)
comment(0x05CC, "Decrement byte counter", inline=True)
comment(0x05CD, "Loop for all 16 bytes", inline=True)
comment(0x05CF, "ALWAYS branch to main loop", inline=True)
comment(0x05D1, "Read 13-byte OSGBPB control block from R2", inline=True)
label(0x05D3, "read_osgbpb_ctrl_blk") # Read 13-byte OSGBPB control block from R2
comment(0x05D3, "Read next control block byte from R2", inline=True)
comment(0x05D6, "Store at &FF+X (descending into &00-&0C)", inline=True)
comment(0x05D8, "Decrement byte counter", inline=True)
comment(0x05D9, "Loop for all 13 bytes", inline=True)
comment(0x05DB, "Read OSGBPB reason code from R2", inline=True)
comment(0x05DE, "Y=0 for OSGBPB control block", inline=True)
comment(0x05E3, "Save A (completion status) for later", inline=True)
comment(0x05E4, "Return 13-byte result block to co-processor", inline=True)
label(0x05E6, "send_osgbpb_result")  # Send 13-byte OSGBPB result block to co-processor via R2
comment(0x05E6, "Load result byte from zero page", inline=True)
comment(0x05E8, "Send byte to co-processor via R2", inline=True)
comment(0x05EB, "Decrement byte counter", inline=True)
comment(0x05EC, "Loop for 13 bytes (X=12..0)", inline=True)
comment(0x05EE, "Recover completion status from stack", inline=True)
comment(0x05EF, "Send carry+status as RDCH-style reply", inline=True)
comment(0x05F5, "X = first parameter", inline=True)
comment(0x05F6, "Read A (OSBYTE number) from R2", inline=True)
comment(0x05F9, "Execute OSBYTE call", inline=True)
label(0x05FC, "tube_poll_r2_result")  # Poll R2 status before sending result
comment(0x05FC, "Poll R2 status for result send", inline=True)
label(0x0600, "tube_page6_start")    # First byte of page 6 relocated Tube code
comment(0x0601, "Send X result for 2-param OSBYTE", inline=True)
comment(0x0617, "OSBYTE &9D (fast Tube BPUT): no result needed", inline=True)
comment(0x0619, "Encode carry (error flag) into bit 7", inline=True)
comment(0x0622, "Send Y result, then fall through to send X", inline=True)
comment(0x0630, "Read param block length from R2", inline=True)
comment(0x0633, "DEX: length 0 means no params to read", inline=True)
comment(0x063E, "Store param bytes into block at &0128", inline=True)
comment(0x0644, "Restore OSWORD number from Y", inline=True)
label(0x0645, "skip_param_read")     # BMI: zero-length params, skip R2 read loop
comment(0x0645, "XY=&0128: param block address for OSWORD", inline=True)
label(0x064C, "poll_r2_osword_result") # Poll R2 status waiting for OSWORD result data
comment(0x0651, "Read result block length from R2", inline=True)
comment(0x0655, "No results to send: return to main loop", inline=True)
comment(0x0657, "Send result block bytes from &0128 via R2", inline=True)
label(0x066A, "read_rdln_ctrl_block") # Read 5-byte OSWORD 0 control block from R2
comment(0x0672, "X=0 after loop, A=0 for OSWORD 0 (read line)", inline=True)
comment(0x0679, "C=0: line read OK; C=1: escape pressed", inline=True)
comment(0x067B, "&FF = escape/error signal to co-processor", inline=True)
comment(0x0682, "&7F = line read successfully", inline=True)
comment(0x068E, "Check for CR terminator", inline=True)
comment(0x06A7, "Check OS escape flag at &FF", inline=True)
comment(0x06A9, "SEC+ROR: put bit 7 of &FF into carry+bit 7", inline=True)
comment(0x06AB, "Escape set: forward to co-processor via R1", inline=True)
comment(0x06AD, "EVNTV: forward event A, Y, X to co-processor", inline=True)
comment(0x06AE, "Send &00 prefix (event notification)", inline=True)
label(0x06C5, "tube_read_r2")         # Poll R2 status, read R2 data into A
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
comment(0x8073, "Command index >= 4: invalid *NET sub-command", inline=True)
comment(0x8075, "Out of range: return via c80e3/RTS", inline=True)
comment(0x8077, "X = command index (0-3)", inline=True)
comment(0x8078, "Clear &A9 (used by dispatch)", inline=True)
comment(0x807A, "Store zero to &A9", inline=True)
comment(0x807C, "Preserve A before dispatch", inline=True)
comment(0x807F, "ALWAYS branch to dispatch", inline=True)
label(0x8081, "skip_cmd_spaces")        # Skip leading spaces in command line before parsing
comment(0x8082, "Load next char from command line", inline=True)
comment(0x8084, "Skip spaces", inline=True)
comment(0x8086, "Loop back to skip leading spaces", inline=True)
comment(0x8088, "Colon = interactive remote command prefix", inline=True)
comment(0x808A, "Char >= ':': skip number parsing", inline=True)
comment(0x808F, "C=1: dot found, first number was network", inline=True)
comment(0x8091, "Store network number (n.s = network.station)", inline=True)
label(0x8098, "got_station_num")       # BCC: no dot, parsed value is bare station number
comment(0x8098, "Z=1: no station parsed (empty or non-numeric)", inline=True)
label(0x809D, "skip_stn_parse")        # BCS/BEQ: bypass station parsing, copy cmd text
comment(0x809D, "Copy command text to FS buffer", inline=True)
label(0x80A0, "scan_for_colon")        # Loop: scan backward through cmd buffer for ':'
comment(0x80A0, "Scan backward for ':' (interactive prefix)", inline=True)
comment(0x80A1, "Y=0: no colon found, send command", inline=True)
comment(0x80A3, "Read char from FS command buffer", inline=True)
comment(0x80A6, "Test for colon separator", inline=True)
comment(0x80A8, "Not colon: keep scanning backward", inline=True)
comment(0x80AA, "Echo colon, then read user input from keyboard", inline=True)
label(0x80AD, "read_remote_cmd_line")   # Read characters from keyboard into FS command buffer
comment(0x80AD, "Check for escape condition", inline=True)
comment(0x80B3, "Append typed character to command buffer", inline=True)
comment(0x80B6, "Advance write pointer", inline=True)
comment(0x80B7, "Increment character count", inline=True)
comment(0x80B8, "Test for CR (end of line)", inline=True)
comment(0x80BA, "Not CR: continue reading input", inline=True)
comment(0x80BF, "After OSNEWL: loop back to scan for colon", inline=True)
label(0x80C5, "prepare_cmd_dispatch")   # Prepare FS command and dispatch recognised *command
comment(0x80E1, "X >= 5: invalid reason code, return", inline=True)
label(0x80E3, "svc_dispatch_range")     # Service dispatch range check (out of range: return)
comment(0x80E3, "Out of range: return via RTS", inline=True)
comment(0x80E8, "Decrement base offset counter", inline=True)
comment(0x80E9, "Loop until Y exhausted", inline=True)
comment(0x80EB, "Y=&FF (no further use)", inline=True)
comment(0x80F7, "9 NOPs: bus settling time for ADLC probe", inline=True)
comment(0x8100, "Save service call number", inline=True)
comment(0x8119, "C into bit 7 of A", inline=True)
comment(0x811A, "Restore service call number", inline=True)
comment(0x811B, "Service >= &80: always handle (Tube/init)", inline=True)
comment(0x811D, "C=1 (no ADLC): disable ROM, skip", inline=True)
label(0x811F, "check_svc_high")         # Test service >= &FE (high-priority dispatch)
comment(0x811F, "Service >= &FE?", inline=True)
comment(0x8121, "Service < &FE: skip to &12/dispatch check", inline=True)
comment(0x8123, "Service &FF: full init (vectors + RAM copy)", inline=True)
comment(0x8125, "Service &FE: Y=0?", inline=True)
comment(0x8127, "Y=0: no Tube data, skip to &12 check", inline=True)
comment(0x8129, "X=6 extra pages for char definitions", inline=True)
comment(0x812B, "OSBYTE &14: explode character RAM", inline=True)
label(0x8130, "poll_tube_ready")       # Top of Tube status polling loop
comment(0x8130, "Poll Tube status register 1", inline=True)
comment(0x8133, "Loop until Tube ready (bit 7 set)", inline=True)
comment(0x8135, "Read byte from Tube data register 1", inline=True)
comment(0x8138, "Zero byte: Tube transfer complete", inline=True)
comment(0x813A, "Send Tube char to screen via OSWRCH", inline=True)
comment(0x813D, "Loop for next Tube byte", inline=True)
comment(0x8140, "EVNTV low = &AD (event handler address)", inline=True)
comment(0x8142, "Set EVNTV low byte at &0220", inline=True)
comment(0x8145, "EVNTV high = &06 (page 6)", inline=True)
comment(0x8147, "Set EVNTV high byte at &0221", inline=True)
comment(0x814A, "BRKV low = &16 (NMI workspace)", inline=True)
comment(0x814C, "Set BRKV low byte at &0202", inline=True)
comment(0x814F, "BRKV high = &00 (zero page)", inline=True)
comment(0x8151, "Set BRKV high byte at &0203", inline=True)
comment(0x8154, "Tube control register init value &8E", inline=True)
comment(0x8156, "Write to Tube control register", inline=True)
comment(0x8159, "Y=0: copy 256 bytes per page", inline=True)
comment(0x815B, "Load ROM byte from page &93", inline=True)
comment(0x815E, "Store to page &04 (Tube code)", inline=True)
comment(0x8161, "Load ROM byte from page &94", inline=True)
comment(0x8164, "Store to page &05 (dispatch table)", inline=True)
comment(0x8167, "Load ROM byte from page &95", inline=True)
comment(0x816A, "Store to page &06", inline=True)
comment(0x816D, "DEY wraps 0 -> &FF on first iteration", inline=True)
comment(0x816E, "Loop until 256 bytes copied per page", inline=True)
comment(0x8170, "Run post-init routine in copied code", inline=True)
comment(0x8173, "X=&60: copy 97 bytes (&60..&00)", inline=True)
label(0x8175, "copy_nmi_workspace")  # Copy 97 bytes of NMI workspace init data from ROM
comment(0x8175, "Load NMI workspace init byte from ROM", inline=True)
comment(0x8178, "Store to zero page &16+X", inline=True)
comment(0x817A, "Next byte", inline=True)
comment(0x817B, "Loop until all workspace bytes copied", inline=True)
label(0x817D, "tube_chars_done")       # BEQ: zero byte received, transfer complete
comment(0x817D, "A=0: fall through to service &12 check", inline=True)
label(0x817F, "check_svc_12")          # Convergence before CMP #&12 test
comment(0x817F, "Is this service &12 (select FS)?", inline=True)
comment(0x8181, "No: check if service < &0D", inline=True)
comment(0x8183, "Service &12: Y=5 (NFS)?", inline=True)
comment(0x8185, "Not NFS: check if service < &0D", inline=True)
comment(0x8187, "A=&0D: dispatch index for svc_13_select_nfs", inline=True)
comment(0x8189, "ALWAYS branch to dispatch", inline=True)
label(0x818B, "not_svc_12_nfs")        # BNE: not service &12 or not NFS (Y!=5)
comment(0x818B, "Service >= &0D?", inline=True)
label(0x818D, "svc_unhandled_return")   # Unhandled service (>= &0D): return unclaimed
comment(0x818D, "Service >= &0D: not handled, return", inline=True)
label(0x818F, "do_svc_dispatch")        # BNE: entry to TAX/workspace save/dispatch
comment(0x818F, "X = service number (dispatch index)", inline=True)
comment(0x8190, "Save &A9 (current service state)", inline=True)
comment(0x8192, "Push saved &A9", inline=True)
comment(0x8193, "Save &A8 (workspace page number)", inline=True)
comment(0x8195, "Push saved &A8", inline=True)
comment(0x8196, "Store service number to &A9", inline=True)
comment(0x8198, "Store Y (page number) to &A8", inline=True)
comment(0x819A, "A = Y for dispatch table offset", inline=True)
comment(0x819B, "Y=0: base offset for service dispatch", inline=True)
comment(0x819D, "Dispatch to service handler", inline=True)
comment(0x81A0, "Recover service claim status from &A9", inline=True)
comment(0x81A2, "Restore saved &A8 from stack", inline=True)
comment(0x81A3, "Write back &A8", inline=True)
comment(0x81A5, "Restore saved A from service dispatch", inline=True)
comment(0x81A6, "Save to workspace &A9", inline=True)
comment(0x81A8, "Return ROM number in A", inline=True)
comment(0x81A9, "Restore X from MOS ROM select copy", inline=True)
comment(0x81AC, "Padding: dispatch targets &81B1", inline=True)
comment(0x81B1, "ROM offset for \"ROFF\" (copyright suffix)", inline=True)
comment(0x81B3, "Try matching *ROFF command", inline=True)
comment(0x81B6, "No match: try *NET", inline=True)
comment(0x81B8, "Y=4: offset of keyboard disable flag", inline=True)
comment(0x81BA, "Read flag from RX buffer", inline=True)
comment(0x81BC, "Zero: keyboard not disabled, skip", inline=True)
comment(0x81BE, "A=0: value to clear flag and re-enable", inline=True)
comment(0x81C1, "Clear keyboard disable flag in buffer", inline=True)
comment(0x81C4, "OSBYTE &C9: Econet keyboard disable", inline=True)
comment(0x81C6, "Re-enable keyboard (X=0, Y=0)", inline=True)
comment(0x81C9, "Function &0A: remote operation complete", inline=True)
comment(0x81CB, "Send notification to controlling station", inline=True)
comment(0x81CE, "Save X (return value from TX)", inline=True)
comment(0x81D0, "OSBYTE &CE: first system mask to reset", inline=True)
label(0x81D2, "clear_osbyte_masks")   # Loop clearing OSBYTE mask bytes with AND &7F
comment(0x81D2, "Restore X for OSBYTE call", inline=True)
comment(0x81D4, "Y=&7F: AND mask (clear bit 7)", inline=True)
comment(0x81D6, "Reset system mask byte", inline=True)
comment(0x81D9, "Advance to next OSBYTE (&CE -> &CF)", inline=True)
comment(0x81DB, "Reached &D0? (past &CF)", inline=True)
comment(0x81DD, "No: reset &CF too", inline=True)
label(0x81DF, "skip_kbd_reenable")      # BEQ: keyboard not disabled, skip re-enable
comment(0x81DF, "A=0: clear remote state", inline=True)
comment(0x81E1, "Clear &A9 (service dispatch state)", inline=True)
comment(0x81E3, "Clear workspace byte", inline=True)
comment(0x81E5, "Return", inline=True)
label(0x81E6, "match_net_cmd")          # Try matching *NET command text
comment(0x81E6, "X=5: ROM offset for \"NET\" match", inline=True)
comment(0x81E8, "Try matching *NET command", inline=True)
comment(0x81EB, "No match: return unclaimed", inline=True)
comment(0x81ED, "Notify current FS of shutdown (FSCV A=6)", inline=True)
comment(0x81F0, "C=1 for ROR", inline=True)
comment(0x81F1, "Set bit 7 of l00a8 (inhibit auto-boot)", inline=True)
comment(0x81F3, "Claim OS vectors, issue service &0F", inline=True)
comment(0x81F6, "Y=&1D: top of FS state range", inline=True)
comment(0x81F8, "Copy FS state from RX buffer...", inline=True)
comment(0x81FA, "...to workspace (offsets &15-&1D)", inline=True)
comment(0x81FD, "Next byte (descending)", inline=True)
comment(0x81FE, "Loop until offset &14 done", inline=True)
comment(0x8200, "Continue loop", inline=True)
comment(0x8202, "ALWAYS branch to init_fs_vectors", inline=True)
comment(0x8204, "Print ROM identification string", inline=True)
comment(0x8213, "Return (service not claimed)", inline=True)
comment(0x8214, "FSCV reason 6 = FS shutdown", inline=True)
comment(0x8216, "Tail-call via filing system control vector", inline=True)
comment(0x8219, "Notify current FS of shutdown", inline=True)
comment(0x821C, "OSBYTE &7A: scan keyboard", inline=True)
comment(0x8222, "No key pressed: proceed with auto-boot", inline=True)
comment(0x8224, "XOR with &55: result=0 if key is 'N'", inline=True)
comment(0x8226, "Not 'N': return without claiming", inline=True)
comment(0x8229, "OSBYTE &78: clear key-pressed state", inline=True)
comment(0x822E, "Print 'Econet Station ' banner", inline=True)
comment(0x8242, "Load station number", inline=True)
comment(0x8244, "Print as 3-digit decimal", inline=True)
comment(0x8247, "BIT trick: bit 5 of SR2 = clock present", inline=True)
comment(0x8249, "Test DCD: clock present if bit 5 clear", inline=True)
comment(0x824C, "Clock present: skip warning", inline=True)
comment(0x824E, "Print ' No Clock' warning", inline=True)
comment(0x825A, "NOP (padding after inline string)", inline=True)
label(0x825B, "skip_no_clock_msg")     # BEQ: clock present, skip "No Clock" message
comment(0x825B, "Print two CRs (blank line)", inline=True)
comment(0x8265, "Write to FILEV-FSCV vector table", inline=True)
comment(0x8268, "Next byte (descending)", inline=True)
comment(0x8269, "Loop until all 14 bytes copied", inline=True)
comment(0x826B, "Read ROM ptr table addr, install NETV", inline=True)
comment(0x826E, "Install 7 handler entries in ROM ptr table", inline=True)
comment(0x8270, "7 FS vectors to install", inline=True)
comment(0x8272, "Install each 3-byte vector entry", inline=True)
comment(0x8275, "X=0 after loop; store as workspace offset", inline=True)
comment(0x8280, "Issue service &0A", inline=True)
comment(0x8283, "Non-zero after hard reset: skip auto-boot", inline=True)
comment(0x8287, "X = lo byte of auto-boot string at &828E", inline=True)
comment(0x8294, "Auto-boot string tail / NETV handler data", inline=True)
comment(0x82B8, "Already at page &10 or above?", inline=True)
comment(0x82BA, "Yes: nothing to claim", inline=True)
comment(0x82BC, "Claim pages &0D-&0F (3 pages)", inline=True)
comment(0x82C6, "A=0 for clearing workspace", inline=True)
comment(0x82C8, "Y=4: remote status offset", inline=True)
comment(0x82CA, "Clear status byte in net receive buffer", inline=True)
comment(0x82CC, "Y=&FF: used for later iteration", inline=True)
comment(0x82CE, "Clear RX ptr low byte", inline=True)
comment(0x82D0, "Clear workspace ptr low byte", inline=True)
comment(0x82D2, "Clear RXCB iteration counter", inline=True)
comment(0x82D4, "Clear TX semaphore (no TX in progress)", inline=True)
comment(0x82D7, "X=0 for OSBYTE", inline=True)
comment(0x82DD, "X = break type from OSBYTE result", inline=True)
comment(0x82E0, "Y=&15: printer station offset in RX buffer", inline=True)
comment(0x82E2, "&FE = no server selected", inline=True)
comment(0x82E7, "Store &FE at printer station offset", inline=True)
comment(0x82E9, "A=0 for clearing workspace fields", inline=True)
comment(0x82EB, "Clear network number", inline=True)
comment(0x82EE, "Clear protection status", inline=True)
comment(0x82F1, "Clear message flag", inline=True)
comment(0x82F4, "Clear boot option", inline=True)
comment(0x82F7, "Y=&16", inline=True)
comment(0x82F8, "Clear net number at RX buffer offset &16", inline=True)
comment(0x82FA, "Init printer server: station &FE, net 0", inline=True)
comment(0x82FC, "Store net 0 at workspace offset 3", inline=True)
comment(0x82FE, "Y=2: printer station offset", inline=True)
comment(0x82FF, "&FE = no printer server", inline=True)
comment(0x8301, "Store &FE at printer station in workspace", inline=True)
label(0x8303, "init_rxcb_entries")   # Mark all RXCBs as available (&3F) in NFS workspace
comment(0x8303, "Load RXCB counter", inline=True)
comment(0x8305, "Convert to workspace byte offset", inline=True)
comment(0x8308, "C=1: past max handles, done", inline=True)
comment(0x830A, "Mark RXCB as available", inline=True)
comment(0x830C, "Write &3F flag to workspace", inline=True)
comment(0x830E, "Next RXCB number", inline=True)
comment(0x8310, "Loop for all RXCBs", inline=True)
label(0x8312, "read_station_id")       # BEQ/BCS: soft break or RXCBs done, read &FE18
comment(0x8315, "Y=&14: station ID offset in RX buffer", inline=True)
comment(0x8317, "Store our station number", inline=True)
comment(0x831C, "Enable user-level RX (LFLAG=&40)", inline=True)
comment(0x831E, "Store to rx_flags", inline=True)
comment(0x8321, "OSBYTE &A8: read ROM pointer table address", inline=True)
comment(0x8323, "X=0: read low byte", inline=True)
comment(0x8325, "Y=&FF: read high byte", inline=True)
comment(0x8327, "Returns table address in X (lo) Y (hi)", inline=True)
comment(0x832A, "Store table base address low byte", inline=True)
comment(0x832C, "Store table base address high byte", inline=True)
comment(0x832E, "NETV extended vector offset in ROM ptr table", inline=True)
comment(0x8330, "Set NETV low byte = &36 (vector dispatch)", inline=True)
comment(0x8333, "Install 1 entry (NETV) in ROM ptr table", inline=True)
comment(0x8335, "Load handler address low byte from table", inline=True)
comment(0x8338, "Store to ROM pointer table", inline=True)
comment(0x833A, "Next byte", inline=True)
comment(0x833B, "Load handler address high byte from table", inline=True)
comment(0x833E, "Store to ROM pointer table", inline=True)
comment(0x8340, "Next byte", inline=True)
comment(0x8341, "Write current ROM bank number", inline=True)
comment(0x8343, "Store ROM number to ROM pointer table", inline=True)
comment(0x8345, "Advance to next entry position", inline=True)
comment(0x8346, "Count down entries", inline=True)
comment(0x8347, "Loop until all entries installed", inline=True)
comment(0x8349, "Y = workspace high byte + 1 = next free page", inline=True)
comment(0x834B, "Advance past workspace page", inline=True)
comment(0x834C, "Return; Y = page after NFS workspace", inline=True)
comment(0x834D, "Copy 10 bytes: FS state to workspace backup", inline=True)
comment(0x8355, "Offsets &15-&1D: server, handles, OPT, etc.", inline=True)
label(0x8360, "match_cmd_chars")       # Match input chars against ROM string byte-by-byte
label(0x8373, "check_rom_end")        # BEQ/BNE: mismatch or space, test ROM string end
label(0x8379, "skip_space_next")         # INY then fall into skip_spaces
label(0x837A, "skip_spaces")            # Skip spaces and test for end of line (CR)
comment(0x8383, "A=&90: FS reply port (PREPLY)", inline=True)
comment(0x8385, "Init TXCB from template", inline=True)
comment(0x8388, "Store port number in TXCB", inline=True)
comment(0x838A, "Control byte: 3 = transmit", inline=True)
comment(0x838C, "Store control byte in TXCB", inline=True)
comment(0x838E, "Decrement TXCB flag to arm TX", inline=True)
comment(0x8391, "Preserve A across call", inline=True)
comment(0x8392, "Copy 12 bytes (Y=11..0)", inline=True)
comment(0x8394, "Load template byte", inline=True)
comment(0x8397, "Store to TX control block at &00C0", inline=True)
comment(0x839A, "Y < 2: also copy FS server station/network", inline=True)
comment(0x839C, "Skip station/network copy for Y >= 2", inline=True)
comment(0x839E, "Load FS server station (Y=0) or network (Y=1)", inline=True)
comment(0x83A1, "Store to dest station/network at &00C2", inline=True)
comment(0x83A4, "Next byte (descending)", inline=True)
comment(0x83A5, "Loop until all 12 bytes copied", inline=True)
comment(0x83A7, "Restore A", inline=True)
comment(0x83A8, "Return", inline=True)
label(0x83AF, "tx_ctrl_upper")       # TX control template upper half (high bytes/masks)
comment(0x83B5, "Save flag byte for command", inline=True)
comment(0x83B6, "C=1: include flag in FS command", inline=True)
comment(0x83B7, "ALWAYS branch to prepare_fs_cmd", inline=True)
comment(0x83B9, "V=0: command has no flag byte", inline=True)
comment(0x83BA, "ALWAYS branch to prepare_fs_cmd", inline=True)
comment(0x83C3, "V=0: standard FS command path", inline=True)
comment(0x83C4, "Copy URD handle from workspace to buffer", inline=True)
comment(0x83C7, "Store URD at &0F02", inline=True)
label(0x83CA, "store_fs_hdr_clc")       # CLC entry: clear carry then store function code
comment(0x83CA, "CLC: no byte-stream path", inline=True)
label(0x83CB, "store_fs_hdr_fn")       # Store function code and CSD/LIB handles
comment(0x83CB, "Store function code at &0F01", inline=True)
comment(0x83CE, "Y=1: copy CSD (offset 1) then LIB (offset 0)", inline=True)
label(0x83D0, "copy_dir_handles")       # Copy CSD and LIB handles into FS command header
comment(0x83D0, "Copy CSD and LIB handles to command buffer", inline=True)
comment(0x83D3, "Store at &0F03 (CSD) and &0F04 (LIB)", inline=True)
comment(0x83D6, "Y=function code", inline=True)
comment(0x83D7, "Loop for both handles", inline=True)
comment(0x83D9, "Save carry (FS path vs byte-stream)", inline=True)
comment(0x83DA, "Reply port &90 (PREPLY)", inline=True)
comment(0x83DC, "Store at &0F00 (HDRREP)", inline=True)
comment(0x83DF, "Copy TX template to &00C0", inline=True)
comment(0x83E2, "A = X (buffer extent)", inline=True)
comment(0x83E3, "HPTR = header (5) + data (X) bytes to send", inline=True)
comment(0x83E5, "Store to TXCB end-pointer low", inline=True)
comment(0x83E7, "Restore carry flag", inline=True)
comment(0x83E8, "C=1: byte-stream path (BSXMIT)", inline=True)
comment(0x83EA, "Save flags for send_fs_reply_cmd", inline=True)
comment(0x83EB, "Point net_tx_ptr to &00C0; transmit", inline=True)
comment(0x83EE, "Restore flags", inline=True)
comment(0x83EF, "Save flags (V flag state)", inline=True)
comment(0x83F0, "Set up RX wait for FS reply", inline=True)
comment(0x83F3, "Transmit and wait (BRIANX)", inline=True)
comment(0x83F6, "Restore flags", inline=True)
comment(0x83F7, "Y=1: skip past command code byte", inline=True)
comment(0x83F8, "Load return code from FS reply", inline=True)
comment(0x83FA, "X = return code", inline=True)
comment(0x83FB, "Zero: success, return", inline=True)
comment(0x83FD, "V=0: standard path, error is fatal", inline=True)
comment(0x83FF, "ADC #&2A: test for &D6 (not found)", inline=True)
label(0x8401, "check_fs_error")        # BVC: standard path, BNE to store_fs_error
comment(0x8401, "Non-zero: hard error, go to FSERR", inline=True)
comment(0x8403, "Return (success or soft &D6 error)", inline=True)
comment(0x8404, "Discard saved flags from stack", inline=True)
comment(0x8405, "X=&C0: TXCB address for byte-stream TX", inline=True)
comment(0x8407, "Y++ past command code", inline=True)
comment(0x8408, "Byte-stream transmit with retry", inline=True)
comment(0x840B, "Store result to &B3", inline=True)
comment(0x840D, "C=0: success, check reply code", inline=True)
comment(0x8410, "Save A (BPUT byte) on stack", inline=True)
comment(0x8411, "Also save byte at &0FDF for BSXMIT", inline=True)
comment(0x8414, "Transfer X for stack save", inline=True)
comment(0x8415, "Save X on stack", inline=True)
comment(0x8416, "Transfer Y (handle) for stack save", inline=True)
comment(0x8417, "Save Y (handle) on stack", inline=True)
comment(0x8418, "Save P (C = BPUT/BGET selector) on stack", inline=True)
comment(0x8419, "Save handle for SPOOL/EXEC comparison later", inline=True)
comment(0x841B, "Convert handle Y to single-bit mask", inline=True)
comment(0x841E, "Store handle bitmask at &0FDE", inline=True)
comment(0x8421, "Store handle bitmask for sequence tracking", inline=True)
comment(0x8423, "&90 = data port (PREPLY)", inline=True)
comment(0x8425, "Store reply port in command buffer", inline=True)
comment(0x8428, "Set up 12-byte TXCB from template", inline=True)
comment(0x842B, "CB reply buffer at &0FDC", inline=True)
comment(0x842D, "Store reply buffer ptr low in TXCB", inline=True)
comment(0x842F, "Error buffer at &0FE0", inline=True)
comment(0x8431, "Store error buffer ptr low in TXCB", inline=True)
comment(0x8433, "Y=1 (from init_tx_ctrl_block exit)", inline=True)
comment(0x8434, "X=9: BPUT function code", inline=True)
comment(0x8436, "Restore C: selects BPUT (0) vs BGET (1)", inline=True)
comment(0x8437, "C=0 (BPUT): keep X=9", inline=True)
comment(0x843A, "Store function code at &0FDD", inline=True)
comment(0x843D, "Load handle bitmask for BSXMIT", inline=True)
comment(0x843F, "X=&C0: TXCB address for econet_tx_retry", inline=True)
comment(0x8441, "Transmit via byte-stream protocol", inline=True)
comment(0x8444, "Load reply byte from buffer", inline=True)
comment(0x8447, "Zero reply = success, skip error handling", inline=True)
comment(0x8449, "Copy 32-byte reply to error buffer at &0FE0", inline=True)
comment(0x844B, "Load reply byte at offset Y", inline=True)
comment(0x844E, "Store to error buffer at &0FE0+Y", inline=True)
comment(0x8451, "Next byte (descending)", inline=True)
comment(0x8452, "Loop until all 32 bytes copied", inline=True)
comment(0x8455, "A=&C6: read *EXEC file handle", inline=True)
comment(0x845A, "')': offset into \"SP.\" string at &8529", inline=True)
comment(0x845C, "Y=value of *SPOOL file handle", inline=True)
comment(0x845E, "Handle matches SPOOL -- close it", inline=True)
comment(0x8460, "'-': offset into \"E.\" string at &852D", inline=True)
comment(0x8462, "X=value of *EXEC file handle", inline=True)
comment(0x8464, "No EXEC match -- skip close", inline=True)
label(0x8466, "close_spool_exec")       # BEQ: SPOOL handle matched, OSCLI close
comment(0x8466, "X = string offset for OSCLI close", inline=True)
comment(0x8467, "Y=&85: high byte of OSCLI string in ROM", inline=True)
comment(0x8469, "Close SPOOL/EXEC via \"*SP.\" or \"*E.\"", inline=True)
label(0x846C, "dispatch_fs_error")     # BNE: no handle match, reset ptr for FSERR
comment(0x846C, "Reset CB pointer to error buffer at &0FE0", inline=True)
comment(0x846E, "Reset reply ptr to error buffer", inline=True)
comment(0x8470, "Reload reply byte for error dispatch", inline=True)
comment(0x8473, "Remember raw FS error code", inline=True)
comment(0x8476, "Y=1: point to error number byte in reply", inline=True)
comment(0x8478, "Clamp FS errors below &A8 to standard &A8", inline=True)
comment(0x847A, "Error >= &A8: keep original value", inline=True)
comment(0x847C, "Error < &A8: override with standard &A8", inline=True)
comment(0x847E, "Write clamped error number to reply buffer", inline=True)
label(0x8480, "error_code_clamped")    # BCS: error >= &A8, skip clamp, start scan
comment(0x8480, "Start scanning from offset &FF (will INY to 0)", inline=True)
label(0x8482, "copy_error_to_brk")      # Copy FS error reply to &0100 as BRK error block
comment(0x8482, "Next byte in reply buffer", inline=True)
comment(0x8483, "Copy reply buffer to &0100 for BRK execution", inline=True)
comment(0x8485, "Build BRK error block at &0100", inline=True)
comment(0x8488, "Scan for CR terminator (&0D)", inline=True)
comment(0x848A, "Continue until CR found", inline=True)
comment(0x848C, "Replace CR with zero = BRK error block end", inline=True)
comment(0x848F, "Execute as BRK error block at &0100; ALWAYS", inline=True)
comment(0x8491, "Save updated sequence number", inline=True)
comment(0x8494, "Restore Y from stack", inline=True)
comment(0x8496, "Restore X from stack", inline=True)
comment(0x8498, "Restore A from stack", inline=True)
comment(0x8499, "Return to caller", inline=True)
comment(0x849A, "Y=4: remote status flag offset", inline=True)
comment(0x849C, "Read remote status from RX CB", inline=True)
comment(0x849E, "Zero: not remoted, set up session", inline=True)
comment(0x84A0, "Already remoted: clear and return", inline=True)
comment(0x84A3, "Set remote status: bits 0+3 (ORA #9)", inline=True)
comment(0x84A5, "Store updated remote status", inline=True)
comment(0x84A7, "X=&80: RX data area offset", inline=True)
comment(0x84A9, "Y=&80: read source station low", inline=True)
comment(0x84AB, "Read source station lo from RX data at &80", inline=True)
comment(0x84AD, "Save source station low byte", inline=True)
comment(0x84AE, "Y=&81", inline=True)
comment(0x84AF, "Read source station hi from RX data at &81", inline=True)
comment(0x84B1, "Save controlling station to workspace &0E/&0F", inline=True)
comment(0x84B3, "Store station high to ws+&0F", inline=True)
comment(0x84B5, "Y=&0E", inline=True)
comment(0x84B6, "Restore source station low", inline=True)
comment(0x84B7, "Store station low to ws+&0E", inline=True)
comment(0x84B9, "Clear OSBYTE &CE/&CF flags", inline=True)
comment(0x84BC, "Set up TX control block", inline=True)
comment(0x84BF, "X=1: disable keyboard", inline=True)
comment(0x84C1, "Y=0 for OSBYTE", inline=True)
comment(0x84C3, "Disable keyboard for remote session", inline=True)
comment(0x84C8, "Allow JSR to page 1 (stack page)", inline=True)
comment(0x84CB, "Zero bytes &0100-&0102", inline=True)
label(0x84CF, "zero_exec_header")      # Zero bytes &0100-&0102 before executing downloaded code
comment(0x84CF, "BRK at &0100 as safe default", inline=True)
label(0x84D5, "execute_downloaded")      # JMP &0100: execute downloaded code at stack page
comment(0x84D5, "Execute downloaded code", inline=True)
comment(0x84D8, "Y=4: RX control block byte 4 (remote status)", inline=True)
comment(0x84DA, "Read remote status flag", inline=True)
comment(0x84DC, "Zero = not remoted; allow new session", inline=True)
comment(0x84DE, "Read source station from RX data at &80", inline=True)
comment(0x84E0, "A = source station number", inline=True)
comment(0x84E2, "Compare against controlling station at &0E", inline=True)
comment(0x84E4, "Check if source matches controller", inline=True)
comment(0x84E6, "Reject: source != controlling station", inline=True)
comment(0x84E8, "Read keypress from RX data at &82", inline=True)
comment(0x84EA, "Load character byte", inline=True)
comment(0x84EC, "Y = character to insert", inline=True)
comment(0x84ED, "X = buffer 0 (keyboard input)", inline=True)
comment(0x84EF, "Release JSR protection before inserting key", inline=True)
comment(0x84F2, "OSBYTE &99: insert char into input buffer", inline=True)
comment(0x84F4, "Tail call: insert character Y into buffer X", inline=True)
label(0x84F7, "error_not_listening")     # Error code 8: "Not listening"
comment(0x84F7, "Error code 8: \"Not listening\" error", inline=True)
comment(0x84F9, "ALWAYS branch to set_listen_offset", inline=True)
comment(0x84FB, "Load TX status byte for error lookup", inline=True)
comment(0x84FD, "Mask to 3-bit error code (0-7)", inline=True)
comment(0x84FF, "X = error code index", inline=True)
comment(0x8500, "Look up error message offset from table", inline=True)
comment(0x8503, "X=0: start writing at &0101", inline=True)
comment(0x8505, "Store BRK opcode at &0100", inline=True)
label(0x8508, "copy_error_message")     # Copy Econet error message string into BRK block
comment(0x8508, "Load error message byte", inline=True)
comment(0x850B, "Build error message at &0101+", inline=True)
comment(0x850E, "Zero byte = end of message; go execute BRK", inline=True)
comment(0x8510, "Next source byte", inline=True)
comment(0x8511, "Next dest byte", inline=True)
comment(0x8512, "Continue copying message", inline=True)
comment(0x851D, "Save function code on stack", inline=True)
comment(0x851E, "Load current rx_flags", inline=True)
comment(0x8521, "Save rx_flags on stack for restore", inline=True)
comment(0x8522, "Set bit7: FS transaction in progress", inline=True)
comment(0x8524, "Write back updated rx_flags", inline=True)
label(0x8527, "skip_rx_flag_set")       # BNE: non-zero TX hi byte, skip bit-7 set
comment(0x8527, "Push two zero bytes as timeout counters", inline=True)
comment(0x8529, "First zero for timeout", inline=True)
comment(0x852A, "Second zero for timeout", inline=True)
comment(0x852B, "Y=0: index for flag byte check", inline=True)
comment(0x852C, "TSX: index stack-based timeout via X", inline=True)
comment(0x8530, "Read flag byte from TX control block", inline=True)
comment(0x8532, "Bit 7 set = reply received", inline=True)
comment(0x8534, "Three-stage nested timeout: inner loop", inline=True)
comment(0x8537, "Inner not expired: keep polling", inline=True)
comment(0x8539, "Middle timeout loop", inline=True)
comment(0x853C, "Middle not expired: keep polling", inline=True)
comment(0x853E, "Outer timeout loop (slowest)", inline=True)
comment(0x8541, "Outer not expired: keep polling", inline=True)
comment(0x8543, "Pop first timeout byte", inline=True)
comment(0x8544, "Pop second timeout byte", inline=True)
comment(0x8545, "Pop saved rx_flags into A", inline=True)
comment(0x8546, "Restore saved rx_flags from stack", inline=True)
comment(0x8549, "Pop saved function code", inline=True)
comment(0x854A, "A=saved func code; zero would mean no reply", inline=True)
comment(0x854C, "Return to caller", inline=True)
comment(0x855C, "C=1: flag for BGET mode", inline=True)
comment(0x855D, "Handle BGET via FS command", inline=True)
comment(0x8560, "SEC: set carry for error check", inline=True)
comment(0x8561, "A=&FE: mask for EOF check", inline=True)
comment(0x8563, "BIT l0fdf: test error flags", inline=True)
comment(0x8566, "V=1: error, return early", inline=True)
comment(0x8568, "CLC: no error", inline=True)
comment(0x8569, "Save flags for EOF check", inline=True)
comment(0x856A, "Load BGET result byte", inline=True)
comment(0x856C, "Restore flags", inline=True)
comment(0x856D, "Bit7 set: skip FS flag clear", inline=True)
comment(0x856F, "Clear FS flag for handle", inline=True)
label(0x8572, "bgetv_shared_jsr")      # Embedded JSR opcode: code-sharing with error table
comment(0x85DD, "Y=&0E: attribute byte offset in param block", inline=True)
comment(0x85DF, "Load FS attribute byte", inline=True)
comment(0x85E1, "Mask to 6 bits (FS → BBC direction)", inline=True)
comment(0x85E3, "X=4: skip first 4 table entries (BBC→FS half)", inline=True)
comment(0x85E5, "ALWAYS branch to shared bitmask builder", inline=True)
comment(0x85E7, "Mask to 5 bits (BBC → FS direction)", inline=True)
comment(0x85E9, "X=&FF: INX makes 0; start from table index 0", inline=True)
label(0x85EB, "attrib_shift_bits")      # Attribute bitmask conversion (shared tail)
comment(0x85EB, "Temp storage for source bitmask to shift out", inline=True)
comment(0x85ED, "A=0: accumulate destination bits here", inline=True)
label(0x85EF, "map_attrib_bits")         # Map source attribute bits via access_bit_table lookup
comment(0x85EF, "Next table entry", inline=True)
comment(0x85F0, "Shift out source bits one at a time", inline=True)
comment(0x85F2, "Bit was 0: skip this destination bit", inline=True)
comment(0x85F4, "OR in destination bit from lookup table", inline=True)
label(0x85F7, "skip_set_attrib_bit")   # BCC: source bit was 0, don't OR destination
comment(0x85F7, "Loop while source bits remain (A != 0)", inline=True)
comment(0x85F9, "Return; A = converted attribute bitmask", inline=True)
label(0x860D, "print_inline_char")     # Print inline string bytes via OSASCI until bit-7 terminator
label(0x8613, "print_next_char")      # INC lo-byte of pointer, load and print next char
label(0x861D, "jump_via_addr")        # BMI: bit 7 terminator, JMP (fs_load_addr)
label(0x8624, "scan_decimal_digit")    # Read ASCII digits and accumulate decimal value
label(0x863F, "no_dot_exit")          # BCC: char < '.', CLC then RTS (no dot found)
label(0x8640, "parse_decimal_rts")    # BEQ: char = '.', LDA result/RTS
comment(0x8643, "Handle number to Y for conversion", inline=True)
comment(0x8644, "Force unconditional conversion", inline=True)
label(0x865C, "handle_mask_exit")     # BEQ/BNE: PLA/TAX/PLA/RTS exit restoring X and A
comment(0x8668, "Compare 4 bytes (index 4,3,2,1)", inline=True)
label(0x866A, "compare_addr_byte")     # EOR bytes of two 4-byte addresses checking for mismatch
comment(0x866A, "Load byte from first address", inline=True)
comment(0x866C, "XOR with corresponding byte", inline=True)
comment(0x866E, "Mismatch: Z=0, return unequal", inline=True)
comment(0x8671, "Continue comparing", inline=True)
comment(0x8674, "X=first handle (&20)", inline=True)
comment(0x8676, "Y=last handle (&27)", inline=True)
comment(0x8679, "Merge new bits into flags", inline=True)
comment(0x867C, "Store updated flags (always taken)", inline=True)
comment(0x867E, "Invert mask: set bits become clear bits", inline=True)
comment(0x8680, "Clear specified bits in flags", inline=True)
comment(0x8683, "Write back updated flags", inline=True)
comment(0x8686, "Return", inline=True)
comment(0x86D7, "Y=1: copy 2 bytes (high then low)", inline=True)
comment(0x86D9, "Load filename ptr from control block", inline=True)
comment(0x86DB, "Store to MOS text pointer (&F2/&F3)", inline=True)
comment(0x86DE, "Next byte (descending)", inline=True)
comment(0x86DF, "Loop for both bytes", inline=True)
comment(0x86E1, "Start from beginning of string", inline=True)
comment(0x86E3, "X=&FF: INX will make X=0 (first char index)", inline=True)
comment(0x86E5, "C=0 for GSINIT: parse from current position", inline=True)
comment(0x86E6, "Initialise GS string parser", inline=True)
comment(0x86E9, "Empty string: skip to CR terminator", inline=True)
comment(0x86EB, "Read next character via GSREAD", inline=True)
comment(0x86EE, "C=1 from GSREAD: end of string reached", inline=True)
comment(0x86F0, "Advance buffer index", inline=True)
comment(0x86F1, "Store parsed character to &0E30+X", inline=True)
comment(0x86F4, "ALWAYS loop (GSREAD clears C on success)", inline=True)
label(0x86F6, "terminate_filename")   # BEQ/BCS: empty or end-of-GSREAD, append CR
comment(0x86F6, "Terminate parsed string with CR", inline=True)
comment(0x86F7, "CR = &0D", inline=True)
comment(0x86F9, "Store CR terminator at end of string", inline=True)
comment(0x86FC, "Point fs_crc_lo/hi at &0E30 parse buffer", inline=True)
comment(0x86FE, "fs_crc_lo = &30", inline=True)
comment(0x8700, "fs_crc_hi = &0E → buffer at &0E30", inline=True)
comment(0x8702, "Store high byte", inline=True)
comment(0x8704, "Return; X = string length", inline=True)
comment(0x8708, "Copy filename ptr from param block to os_text_ptr", inline=True)
comment(0x870B, "Recover function code from saved A", inline=True)
comment(0x870D, "A >= 0: save (&00) or attribs (&01-&06)", inline=True)
comment(0x870F, "A=&FF? Only &FF is valid for load", inline=True)
comment(0x8713, "Unknown negative code: no-op return", inline=True)
comment(0x871B, "Port &92 = PLDATA (data transfer port)", inline=True)
comment(0x871D, "Overwrite URD field with data port number", inline=True)
comment(0x8720, "Build FS header (V=1: CLV path)", inline=True)
comment(0x8723, "Y=6: param block byte 6", inline=True)
comment(0x8725, "Byte 6: use file's own load address?", inline=True)
comment(0x8727, "Non-zero: use FS reply address (lodfil)", inline=True)
comment(0x8729, "Zero: copy caller's load addr first", inline=True)
comment(0x872C, "Then copy FS reply to param block", inline=True)
comment(0x872F, "Carry clear from prepare_cmd_clv: skip lodfil", inline=True)
comment(0x8731, "Copy FS reply addresses to param block", inline=True)
comment(0x8734, "Then copy load addr from param block", inline=True)
label(0x8737, "skip_lodfil")           # BCC: skip lodfil block, proceed to compute end addr
comment(0x8737, "Compute end address = load + file length", inline=True)
label(0x8739, "copy_load_end_addr")    # Copy 4 load-address bytes and compute end address
comment(0x8739, "Load address byte", inline=True)
comment(0x873B, "Store as current transfer position", inline=True)
comment(0x873D, "Add file length byte", inline=True)
comment(0x8740, "Store as end position", inline=True)
comment(0x8742, "Next address byte", inline=True)
comment(0x8743, "Decrement byte counter", inline=True)
comment(0x8744, "Loop for all 4 address bytes", inline=True)
comment(0x8746, "Adjust high byte for 3-byte length overflow", inline=True)
comment(0x8747, "Subtract 4th length byte from end addr", inline=True)
comment(0x874A, "Store adjusted end address high byte", inline=True)
comment(0x874F, "Transfer file data in &80-byte blocks", inline=True)
comment(0x8752, "Copy 3-byte file length to FS reply cmd buffer", inline=True)
comment(0x8754, "Load file length byte", inline=True)
comment(0x8757, "Store in FS command data buffer", inline=True)
comment(0x875A, "Next byte (count down)", inline=True)
comment(0x875B, "Loop for 3 bytes (X=2,1,0)", inline=True)
comment(0x875D, "ALWAYS branch", inline=True)
comment(0x8762, "Addresses match: transfer complete", inline=True)
comment(0x8764, "Port &92 for data block transfer", inline=True)
comment(0x8766, "Store port to TXCB command byte", inline=True)
label(0x8768, "send_block_loop")       # Outer loop: set up and send each 128-byte block
comment(0x8768, "Set up next &80-byte block for transfer", inline=True)
label(0x876A, "copy_block_addrs")      # Inner loop: swap 4-byte current/end addresses
comment(0x876A, "Swap: current addr -> source, end -> current", inline=True)
comment(0x876C, "Source addr = current position", inline=True)
comment(0x876E, "Load end address byte", inline=True)
comment(0x8770, "Dest = end address (will be clamped)", inline=True)
comment(0x8772, "Next address byte", inline=True)
comment(0x8773, "Loop for all 4 bytes", inline=True)
comment(0x8775, "Command &7F = data block transfer", inline=True)
comment(0x8777, "Store to TXCB control byte", inline=True)
comment(0x8779, "Send this block to the fileserver", inline=True)
comment(0x877C, "Y=3: compare 4 bytes (3..0)", inline=True)
comment(0x877E, "Compare current vs end address (4 bytes)", inline=True)
comment(0x8781, "XOR with end address byte", inline=True)
comment(0x8784, "Not equal: more blocks to send", inline=True)
comment(0x8786, "Next byte", inline=True)
comment(0x8787, "Loop for all 4 address bytes", inline=True)
comment(0x8789, "All equal: transfer complete", inline=True)
comment(0x878A, "A=0: SAVE handler", inline=True)
comment(0x878C, "A!=0: attribute dispatch (A=1-6)", inline=True)
comment(0x878F, "Process 4 address bytes (load/exec/start/end)", inline=True)
comment(0x8791, "Y=&0E: start from end-address in param block", inline=True)
comment(0x8793, "Read end-address byte from param block", inline=True)
comment(0x8795, "Save to port workspace for transfer setup", inline=True)
comment(0x8798, "Y = Y-4: point to start-address byte", inline=True)
comment(0x879B, "end - start = transfer length byte", inline=True)
comment(0x879D, "Store length byte in FS command buffer", inline=True)
comment(0x87A0, "Save length byte for param block restore", inline=True)
comment(0x87A1, "Read corresponding start-address byte", inline=True)
comment(0x87A3, "Save to port workspace", inline=True)
comment(0x87A6, "Restore length byte from stack", inline=True)
comment(0x87A7, "Replace param block entry with length", inline=True)
comment(0x87A9, "Y = Y+5: advance to next address group", inline=True)
comment(0x87AC, "Decrement address byte counter", inline=True)
comment(0x87AD, "Loop for all 4 address bytes", inline=True)
comment(0x87AF, "Copy load/exec addresses to FS command buffer", inline=True)
label(0x87B1, "copy_save_params")      # Copy 9 bytes of load/exec address into FS command buffer
comment(0x87B1, "Read load/exec address byte from params", inline=True)
comment(0x87B3, "Copy to FS command buffer", inline=True)
comment(0x87B6, "Next byte (descending)", inline=True)
comment(0x87B7, "Loop for bytes 9..1", inline=True)
comment(0x87B9, "Port &91 for save command", inline=True)
comment(0x87BB, "Overwrite URD field with port number", inline=True)
comment(0x87BE, "Save port &91 for flow control ACK", inline=True)
comment(0x87C0, "Append filename at offset &0B in cmd buffer", inline=True)
comment(0x87C2, "Append filename to cmd buffer at offset X", inline=True)
comment(0x87C5, "Y=1: function code for save", inline=True)
comment(0x87C7, "Build header and send FS save command", inline=True)
comment(0x87D0, "Print file length in hex", inline=True)
label(0x87D6, "skip_catalogue_msg")   # BEQ: messages flag=0, skip display
comment(0x87D6, "Store reply command for attr decode", inline=True)
comment(0x87D9, "Y=&0E: access byte offset in param block", inline=True)
comment(0x87DB, "Load access byte from FS reply", inline=True)
comment(0x87DE, "Convert FS access to BBC attribute format", inline=True)
comment(0x87E9, "Copied all 4 bytes? (Y=&0E..&11)", inline=True)
comment(0x87EB, "Loop for 4 attribute bytes", inline=True)
comment(0x87ED, "Restore A/X/Y and return to caller", inline=True)
comment(0x87F0, "Start at offset 5 (top of 4-byte addr)", inline=True)
comment(0x87F2, "Read from parameter block", inline=True)
comment(0x87F4, "Store to local workspace", inline=True)
comment(0x87F7, "Next byte (descending)", inline=True)
comment(0x87F8, "Copy offsets 5,4,3,2 (4 bytes)", inline=True)
comment(0x87FA, "Loop while Y >= 2", inline=True)
comment(0x87FC, "Y=3 after loop; add 5 to get Y=8", inline=True)
comment(0x87FD, "INY * 4 = add 4 to Y", inline=True)
comment(0x8801, "Return", inline=True)
comment(0x8802, "Start at offset &0D (top of range)", inline=True)
comment(0x8804, "First store uses X (attrib byte)", inline=True)
comment(0x8805, "Write to parameter block", inline=True)
comment(0x8807, "Read next byte from reply buffer", inline=True)
comment(0x880B, "Copy offsets &0D down to 2", inline=True)
comment(0x880F, "Y=1 after loop; sub 4 to get Y=&FD", inline=True)
comment(0x8814, "Save FS command byte on stack", inline=True)
comment(0x8818, "Addresses equal: nothing to transfer", inline=True)
comment(0x882C, "Store dest address byte", inline=True)
comment(0x882E, "Advance current position", inline=True)
comment(0x8830, "Next address byte", inline=True)
comment(0x8831, "Decrement byte counter", inline=True)
comment(0x8832, "Loop for all 4 bytes", inline=True)
comment(0x8836, "SEC for SBC in overshoot check", inline=True)
comment(0x8837, "Check if new pos overshot end addr", inline=True)
comment(0x883A, "Subtract end address byte", inline=True)
comment(0x883D, "Next byte", inline=True)
comment(0x883E, "Decrement counter", inline=True)
comment(0x883F, "Loop for 4-byte comparison", inline=True)
comment(0x8841, "C=0: no overshoot, proceed", inline=True)
comment(0x8843, "Overshot: clamp dest to end address", inline=True)
label(0x8845, "clamp_dest_addr")       # Clamp dest addr when block overshoots transfer end
comment(0x8845, "Load end address byte", inline=True)
comment(0x8847, "Replace dest with end address", inline=True)
comment(0x8849, "Next byte", inline=True)
comment(0x884A, "Loop for all 4 bytes", inline=True)
label(0x884C, "send_block")           # BCC: no overshoot, skip clamp, send block
comment(0x884C, "Recover original FS command byte", inline=True)
comment(0x884D, "Re-push for next iteration", inline=True)
comment(0x884E, "Save processor flags (C from cmp)", inline=True)
comment(0x884F, "Store command byte in TXCB", inline=True)
comment(0x8851, "128-byte block size for data transfer", inline=True)
comment(0x8853, "Store size in TXCB control byte", inline=True)
comment(0x8855, "Point TX ptr to &00C0; transmit", inline=True)
comment(0x8858, "ACK port for flow control", inline=True)
comment(0x885A, "Set reply port for ACK receive", inline=True)
comment(0x885D, "Restore flags (C=overshoot status)", inline=True)
comment(0x885E, "C=1: all data sent (overshot), done", inline=True)
comment(0x8860, "Command &91 = data block transfer", inline=True)
comment(0x8862, "Store command &91 in TXCB", inline=True)
comment(0x8864, "Transmit block and wait (BRIANX)", inline=True)
comment(0x8867, "More blocks? Loop back", inline=True)
comment(0x8869, "Save A (function code)", inline=True)
comment(0x886A, "X = file handle to check", inline=True)
comment(0x886B, "Convert handle to bitmask in A", inline=True)
comment(0x886E, "Y = handle bitmask from conversion", inline=True)
comment(0x886F, "Local hint: is EOF possible for this handle?", inline=True)
comment(0x8872, "X = result of AND (0 = not at EOF)", inline=True)
comment(0x8873, "Hint clear: definitely not at EOF", inline=True)
comment(0x8875, "Save bitmask for clear_fs_flag", inline=True)
comment(0x8876, "Handle byte in FS command buffer", inline=True)
comment(0x8879, "Y=&11: FS function code FCEOF", inline=True)
comment(0x8880, "Restore bitmask", inline=True)
comment(0x8881, "FS reply: non-zero = at EOF", inline=True)
comment(0x8884, "At EOF: skip flag clear", inline=True)
comment(0x8886, "Not at EOF: clear the hint bit", inline=True)
label(0x8889, "restore_ay_return")      # Restore A and Y registers, return
comment(0x8889, "Restore A", inline=True)
comment(0x888A, "Restore Y", inline=True)
comment(0x888C, "Return; X=0 (not EOF) or X=&FF (EOF)", inline=True)
comment(0x888D, "Store function code in FS cmd buffer", inline=True)
comment(0x8890, "A=6? (delete)", inline=True)
comment(0x8892, "Yes: jump to delete handler", inline=True)
comment(0x8894, "A>=7: unsupported, fall through to return", inline=True)
comment(0x8896, "A=5? (read catalogue info)", inline=True)
comment(0x8898, "Yes: jump to read info handler", inline=True)
comment(0x889A, "A=4? (write attributes only)", inline=True)
comment(0x889C, "Yes: jump to write attrs handler", inline=True)
comment(0x889E, "A=1? (write all catalogue info)", inline=True)
comment(0x88A0, "Yes: jump to write-all handler", inline=True)
comment(0x88A2, "A=2 or 3: convert to param block offset", inline=True)
comment(0x88A3, "A*4: 2->8, 3->12", inline=True)
comment(0x88A4, "Y = A*4", inline=True)
comment(0x88A5, "Y = A*4 - 3 (load addr offset for A=2)", inline=True)
comment(0x88A8, "X=3: copy 4 bytes", inline=True)
comment(0x88AA, "Load address byte from param block", inline=True)
comment(0x88AC, "Store to FS cmd data area", inline=True)
comment(0x88AF, "Next source byte (descending)", inline=True)
comment(0x88B0, "Next dest byte", inline=True)
comment(0x88B1, "Loop for 4 bytes", inline=True)
comment(0x88B3, "X=5: data extent for filename copy", inline=True)
comment(0x88B7, "A=1: encode protection from param block", inline=True)
comment(0x88BA, "Store encoded attrs at &0F0E", inline=True)
comment(0x88BD, "Y=9: source offset in param block", inline=True)
comment(0x88BF, "X=8: dest offset in cmd buffer", inline=True)
comment(0x88C1, "Load byte from param block", inline=True)
comment(0x88C3, "Store to FS cmd buffer", inline=True)
comment(0x88C6, "Next source byte (descending)", inline=True)
comment(0x88C7, "Next dest byte", inline=True)
comment(0x88C8, "Loop until X=0 (8 bytes copied)", inline=True)
comment(0x88CA, "X=&0A: data extent past attrs+addrs", inline=True)
comment(0x88CC, "Append filename to cmd buffer", inline=True)
comment(0x88CF, "Y=&13: fn code for FCSAVE (write attrs)", inline=True)
comment(0x88D1, "ALWAYS branch to send command", inline=True)
comment(0x88D3, "A=6: copy filename (delete)", inline=True)
comment(0x88D6, "Y=&14: fn code for FCDEL (delete)", inline=True)
label(0x88D8, "send_fs_cmd_v1")       # BNE: after copy_filename, BIT tx_ctrl_upper
comment(0x88D8, "Set V=1 (BIT trick: &B3 has bit 6 set)", inline=True)
comment(0x88DB, "Send via prepare_fs_cmd_v (V=1 path)", inline=True)
label(0x88DE, "check_attrib_result")  # BCS: A>=7 unsupported, dispatch to error/return
comment(0x88DE, "C=1: &D6 not-found, skip to return", inline=True)
comment(0x88E0, "C=0: success, copy reply to param block", inline=True)
comment(0x88E2, "A=4: encode attrs from param block", inline=True)
comment(0x88E5, "Store encoded attrs at &0F06", inline=True)
comment(0x88E8, "X=2: data extent (1 attr byte + fn)", inline=True)
comment(0x88EA, "ALWAYS branch to append filename", inline=True)
comment(0x88EC, "A=5: X=1 (filename only, no data)", inline=True)
comment(0x88EE, "Copy filename to cmd buffer", inline=True)
comment(0x88F1, "Y=&12: fn code for FCEXAM (read info)", inline=True)
comment(0x88F6, "Save object type from FS reply", inline=True)
comment(0x88F9, "Clear reply byte (X=0 on success)", inline=True)
comment(0x88FC, "Clear length high byte in reply", inline=True)
comment(0x88FF, "Decode 5-bit access byte from FS reply", inline=True)
comment(0x8902, "Y=&0E: attrs offset in param block", inline=True)
comment(0x8904, "Store decoded attrs at param block +&0E", inline=True)
comment(0x8906, "Y=&0D: start copy below attrs", inline=True)
comment(0x8907, "X=&0C: copy from reply offset &0C down", inline=True)
comment(0x8909, "Load reply byte (load/exec/length)", inline=True)
comment(0x890C, "Store to param block", inline=True)
comment(0x890E, "Next dest byte (descending)", inline=True)
comment(0x890F, "Next source byte", inline=True)
comment(0x8910, "Loop until X=0 (12 bytes copied)", inline=True)
comment(0x8912, "X=0 -> X=2 for length high copy", inline=True)
comment(0x8913, "INX again: X=2", inline=True)
comment(0x8914, "Y=&11: length high dest in param block", inline=True)
comment(0x8916, "Load length high byte from reply", inline=True)
comment(0x8919, "Store to param block", inline=True)
comment(0x891B, "Next dest byte (descending)", inline=True)
comment(0x891C, "Next source byte", inline=True)
comment(0x891D, "Loop for 3 length-high bytes", inline=True)
comment(0x891F, "Return object type in A", inline=True)
label(0x8922, "attrib_error_exit")    # BCS: not-found/error, BPL restore_xy_return
comment(0x8922, "A>=0: branch to restore_args_return", inline=True)
comment(0x8924, "Save A/X/Y registers for later restore", inline=True)
comment(0x8927, "Function >= 3?", inline=True)
comment(0x8929, "A>=3 (ensure/flush): no-op for NFS", inline=True)
comment(0x892B, "Test file handle", inline=True)
comment(0x892D, "Y=0: FS-level query, not per-file", inline=True)
comment(0x892F, "Convert handle to bitmask", inline=True)
comment(0x8932, "Store bitmask as first cmd data byte", inline=True)
comment(0x8935, "LSR splits A: C=1 means write (A=1)", inline=True)
comment(0x8936, "Store function code to cmd data byte 2", inline=True)
comment(0x8939, "C=1: write path, copy ptr from caller", inline=True)
comment(0x893B, "Y=&0C: FCRDSE (read sequential pointer)", inline=True)
comment(0x893D, "X=2: 3 data bytes in command", inline=True)
comment(0x893F, "Build and send FS command", inline=True)
comment(0x8942, "Clear last-byte flag on success", inline=True)
comment(0x8944, "X = saved control block ptr low", inline=True)
comment(0x8946, "Y=2: copy 3 bytes of file pointer", inline=True)
comment(0x8948, "Zero high byte of 3-byte pointer", inline=True)
label(0x894A, "copy_fileptr_reply")    # Copy 3-byte file pointer from FS reply data
comment(0x894A, "Read reply byte from FS cmd data", inline=True)
comment(0x894D, "Store to caller's control block", inline=True)
comment(0x894F, "Next byte (descending)", inline=True)
comment(0x8950, "Next source byte", inline=True)
comment(0x8951, "Loop for all 3 bytes", inline=True)
label(0x8953, "argsv_check_return")    # Conditional return after ARGSV file pointer op
comment(0x8953, "C=0 (read): return to caller", inline=True)
comment(0x8955, "Save bitmask for set_fs_flag later", inline=True)
comment(0x8956, "Push bitmask", inline=True)
comment(0x8957, "Y=3: copy 4 bytes of file pointer", inline=True)
label(0x8959, "copy_fileptr_to_cmd")  # Copy 4-byte file pointer into FS command area
comment(0x8959, "Read caller's pointer byte", inline=True)
comment(0x895B, "Store to FS command data area", inline=True)
comment(0x895E, "Next source byte", inline=True)
comment(0x895F, "Next destination byte", inline=True)
comment(0x8960, "Loop for all 4 bytes", inline=True)
comment(0x8962, "Y=&0D: FCWRSE (write sequential pointer)", inline=True)
comment(0x8964, "X=5: 6 data bytes in command", inline=True)
comment(0x8966, "Build and send FS command", inline=True)
comment(0x8969, "Save not-found status from X", inline=True)
comment(0x896B, "Recover bitmask for EOF hint update", inline=True)
comment(0x896C, "Set EOF hint bit for this handle", inline=True)
comment(0x896F, "A = saved function code / command", inline=True)
label(0x8971, "restore_xy_return")     # Restore X and Y from workspace, return
comment(0x8971, "X = saved control block ptr low", inline=True)
comment(0x8973, "Y = saved control block ptr high", inline=True)
comment(0x8975, "Return to MOS with registers restored", inline=True)
label(0x8976, "argsv_fs_query")        # FS-level ARGSV query (A=0/1/2 dispatch)
comment(0x8976, "Y=0: FS-level queries (no file handle)", inline=True)
comment(0x8978, "A=2: FS-level ensure (write extent)", inline=True)
comment(0x897A, "A>=3: FS command (ARGSV write)", inline=True)
comment(0x897C, "Y = A = byte count for copy loop", inline=True)
comment(0x897D, "A!=0: copy command context block", inline=True)
comment(0x897F, "FS number 5 (loaded as &0A, LSR'd)", inline=True)
label(0x8981, "halve_args_a")         # BEQ: A=2, LSR A then dispatch
comment(0x8981, "Shared: halve A (A=0 or A=2 paths)", inline=True)
comment(0x8982, "Return with A = FS number or 1", inline=True)
comment(0x8984, "Copy command context to caller's block", inline=True)
comment(0x8987, "Store to caller's parameter block", inline=True)
comment(0x8989, "Next byte (descending)", inline=True)
comment(0x898A, "Loop until all bytes copied", inline=True)
comment(0x898C, "Y=&FF after loop; fill high bytes", inline=True)
comment(0x898E, "Set 32-bit result bytes 2-3 to &FF", inline=True)
comment(0x8994, "Save A/X/Y and set up pointers", inline=True)
comment(0x8997, "SEC distinguishes open (A>0) from close", inline=True)
comment(0x899C, "A=0: close file(s)", inline=True)
comment(0x899E, "Valid open modes: &40, &80, &C0 only", inline=True)
comment(0x89A0, "Invalid mode bits: return", inline=True)
comment(0x89A2, "A = original mode byte", inline=True)
comment(0x89A3, "Convert MOS mode to FS protocol flags", inline=True)
comment(0x89A5, "ASL: shift mode bits left", inline=True)
comment(0x89A6, "Flag 1: read/write direction", inline=True)
comment(0x89A9, "ROL: Flag 2 into bit 0", inline=True)
comment(0x89AA, "Flag 2: create vs existing file", inline=True)
comment(0x89AD, "Parse filename from command line", inline=True)
comment(0x89B0, "X=2: copy after 2-byte flags", inline=True)
comment(0x89B2, "Copy filename to FS command buffer", inline=True)
comment(0x89B5, "Y=6: FS function code FCOPEN", inline=True)
comment(0x89B7, "Set V flag from l83b3 bit 6", inline=True)
comment(0x89BA, "Build and send FS open command", inline=True)
comment(0x89BD, "Error: restore and return", inline=True)
comment(0x89BF, "Load reply handle from FS", inline=True)
comment(0x89C2, "X = new file handle", inline=True)
comment(0x89C3, "Set EOF hint + sequence bits", inline=True)
comment(0x89CA, "ALWAYS branch to restore and return", inline=True)
comment(0x89CC, "A = handle (Y preserved in A)", inline=True)
comment(0x89CD, "Y>0: close single file", inline=True)
comment(0x89CF, "Close SPOOL/EXEC before FS close-all", inline=True)
comment(0x89D4, "Y=0: close all handles on server", inline=True)
comment(0x89D6, "Handle byte in FS command buffer", inline=True)
comment(0x89E0, "Reply handle for flag update", inline=True)
comment(0x89E3, "Update EOF/sequence tracking bits", inline=True)
label(0x89E6, "close_opt_return")      # Conditional return after close/opt handler
comment(0x89E6, "C=0: restore A/X/Y and return", inline=True)
comment(0x89E8, "Entry from fscv_0_opt (close-all path)", inline=True)
comment(0x89EA, "Is it *OPT 4,Y?", inline=True)
comment(0x89EC, "No: check for *OPT 1", inline=True)
comment(0x89EE, "Y must be 0-3 for boot option", inline=True)
comment(0x89F0, "Y < 4: valid boot option", inline=True)
label(0x89F2, "check_opt1")           # BNE: X!=4, DEX/BNE to check for *OPT 1
comment(0x89F2, "Not *OPT 4: check for *OPT 1", inline=True)
comment(0x89F3, "Not *OPT 1 either: bad option", inline=True)
label(0x89F5, "set_messages_flag")     # Set *OPT 1 local messages flag from Y
comment(0x89F5, "Set local messages flag (*OPT 1,Y)", inline=True)
comment(0x89F8, "Return via restore_args_return", inline=True)
comment(0x89FA, "Error index 7 (Bad option)", inline=True)
comment(0x89FC, "Generate BRK error", inline=True)
comment(0x89FF, "Boot option value in FS command", inline=True)
comment(0x8A02, "Y=&16: FS function code FCOPT", inline=True)
comment(0x8A07, "Restore Y from saved value", inline=True)
comment(0x8A09, "Cache boot option locally", inline=True)
label(0x8A0C, "opt_return")           # BCC: *OPT 1 done, to close_opt_return
comment(0x8A0C, "Return via restore_args_return", inline=True)
comment(0x8A0E, "Y=9: adjust 9 address bytes", inline=True)
comment(0x8A10, "Adjust with carry clear", inline=True)
comment(0x8A13, "Y=1: adjust 1 address byte", inline=True)
comment(0x8A15, "C=0 for address adjustment", inline=True)
label(0x8A18, "adjust_addr_byte")      # Add or subtract one adjustment byte per iteration (4 total)
label(0x8A24, "subtract_adjust")      # BMI: fs_load_addr_2 negative, SBC instead of ADC
comment(0x8A2E, "Save A/X/Y to FS workspace", inline=True)
comment(0x8A31, "X = call number for range check", inline=True)
comment(0x8A32, "A=0: invalid, restore and return", inline=True)
comment(0x8A34, "Convert to 0-based (A=0..7)", inline=True)
comment(0x8A35, "Range check: must be 0-7", inline=True)
comment(0x8A37, "In range: continue to handler", inline=True)
label(0x8A39, "gbpb_invalid_exit")    # BEQ/fall: A=0 or X>=8 out of range, JMP restore_args
comment(0x8A39, "Out of range: restore args and return", inline=True)
comment(0x8A3C, "Recover 0-based function code", inline=True)
comment(0x8A3D, "Y=0: param block byte 0 (file handle)", inline=True)
comment(0x8A3F, "Save function code on stack", inline=True)
comment(0x8A40, "A>=4: info queries, dispatch separately", inline=True)
comment(0x8A42, "A<4: file read/write operations", inline=True)
comment(0x8A44, "Dispatch to OSGBPB 5-8 info handler", inline=True)
comment(0x8A47, "Get file handle from param block byte 0", inline=True)
comment(0x8A49, "Convert handle to bitmask for EOF flags", inline=True)
comment(0x8A4C, "Store handle in FS command data", inline=True)
comment(0x8A4F, "Y=&0B: start at param block byte 11", inline=True)
comment(0x8A51, "X=6: copy 6 bytes of transfer params", inline=True)
comment(0x8A53, "Load param block byte", inline=True)
comment(0x8A55, "Store to FS command buffer at &0F06+X", inline=True)
comment(0x8A58, "Previous param block byte", inline=True)
comment(0x8A59, "Skip param block offset 8 (the handle)", inline=True)
comment(0x8A5B, "Not at handle offset: continue", inline=True)
comment(0x8A5D, "Extra DEY to skip handle byte", inline=True)
comment(0x8A5E, "Decrement copy counter", inline=True)
comment(0x8A5F, "Loop for all 6 bytes", inline=True)
comment(0x8A61, "Recover function code from stack", inline=True)
comment(0x8A62, "LSR: odd=read (C=1), even=write (C=0)", inline=True)
comment(0x8A63, "Save function code again (need C later)", inline=True)
comment(0x8A64, "Even (write): X stays 0", inline=True)
comment(0x8A66, "Odd (read): X=1", inline=True)
comment(0x8A67, "Store FS direction flag", inline=True)
comment(0x8A6A, "Y=&0B: command data extent", inline=True)
comment(0x8A6C, "Command &91=put, &92=get", inline=True)
comment(0x8A6E, "Recover function code", inline=True)
comment(0x8A6F, "Save again for later direction check", inline=True)
comment(0x8A70, "Even (write): keep &91 and Y=&0B", inline=True)
comment(0x8A72, "Odd (read): use &92 (get) instead", inline=True)
comment(0x8A74, "Read: one fewer data byte in command", inline=True)
label(0x8A75, "gbpb_write_path")      # BEQ: A=0 write, keeps X=&91/Y=&0B
comment(0x8A75, "Store port to FS command URD field", inline=True)
comment(0x8A78, "Save port for error recovery", inline=True)
comment(0x8A7A, "X=8: command data bytes", inline=True)
comment(0x8A7C, "Load handle from FS command data", inline=True)
comment(0x8A7F, "Build FS command with handle+flag", inline=True)
comment(0x8A82, "Save seq# for byte-stream flow control", inline=True)
comment(0x8A84, "Store to FS sequence number workspace", inline=True)
comment(0x8A87, "X=4: copy 4 address bytes", inline=True)
comment(0x8A89, "Set up source/dest from param block", inline=True)
comment(0x8A8B, "Store as source address", inline=True)
comment(0x8A8E, "Store as current transfer position", inline=True)
comment(0x8A91, "Skip 4 bytes to reach transfer length", inline=True)
comment(0x8A94, "Dest = source + length", inline=True)
comment(0x8A96, "Store as end address", inline=True)
comment(0x8A99, "Back 3 to align for next iteration", inline=True)
comment(0x8A9C, "Decrement byte counter", inline=True)
comment(0x8A9D, "Loop for all 4 address bytes", inline=True)
comment(0x8A9F, "X=1 after loop", inline=True)
comment(0x8AA0, "Copy CSD data to command buffer", inline=True)
comment(0x8AA3, "Store at &0F06+X", inline=True)
comment(0x8AA6, "Decrement counter", inline=True)
comment(0x8AA7, "Loop for X=1,0", inline=True)
comment(0x8AA9, "Odd (read): send data to FS first", inline=True)
comment(0x8AAA, "Non-zero: skip write path", inline=True)
comment(0x8AAC, "Load port for transfer setup", inline=True)
comment(0x8AAF, "Transfer data blocks to fileserver", inline=True)
comment(0x8AB2, "Carry set: transfer error", inline=True)
label(0x8AB4, "gbpb_read_path")      # BNE: non-zero read, skip write transfer
comment(0x8AB4, "Read path: receive data blocks from FS", inline=True)
label(0x8AB7, "wait_fs_reply")        # BCS/fall: post-transfer, JSR send_fs_reply_cmd
comment(0x8AB7, "Wait for FS reply command", inline=True)
comment(0x8ABA, "Load handle mask for EOF flag update", inline=True)
comment(0x8ABC, "Check FS reply: bit 7 = not at EOF", inline=True)
comment(0x8ABF, "Bit 7 set: not EOF, skip clear", inline=True)
comment(0x8AC1, "At EOF: clear EOF hint for this handle", inline=True)
label(0x8AC4, "skip_clear_flag")      # BMI: reply bit 7 set (not EOF), skip clear_fs_flag
comment(0x8AC4, "Set EOF hint flag (may be at EOF)", inline=True)
comment(0x8AC7, "Direction=0: forward adjustment", inline=True)
comment(0x8AC9, "Adjust param block addrs by +9 bytes", inline=True)
comment(0x8ACC, "Direction=&FF: reverse adjustment", inline=True)
comment(0x8ACE, "SEC for reverse subtraction", inline=True)
comment(0x8ACF, "Adjust param block addrs (reverse)", inline=True)
comment(0x8AD2, "Shift bit 7 into C for return flag", inline=True)
comment(0x8AD5, "Return via restore_args path", inline=True)
label(0x8AD8, "get_disc_title")        # Request disc title via FS function code &15
comment(0x8AD8, "Y=&15: function code for disc title", inline=True)
comment(0x8ADA, "Build and send FS command", inline=True)
comment(0x8ADD, "Load boot option from FS workspace", inline=True)
comment(0x8AE0, "Store boot option in reply area", inline=True)
comment(0x8AE3, "X=0: reply data start offset", inline=True)
comment(0x8AE5, "Clear reply buffer high byte", inline=True)
comment(0x8AE7, "A=&12: 18 bytes of reply data", inline=True)
comment(0x8AE9, "Store as byte count for copy", inline=True)
comment(0x8AEB, "ALWAYS branch to copy_reply_to_caller", inline=True)
comment(0x8AED, "Y=4: check param block byte 4", inline=True)
comment(0x8AEF, "Check if destination is in Tube space", inline=True)
comment(0x8AF2, "No Tube: skip Tube address check", inline=True)
comment(0x8AF4, "Compare Tube flag with addr byte 4", inline=True)
comment(0x8AF6, "Mismatch: not Tube space", inline=True)
comment(0x8AF9, "Y=3: subtract addr byte 3 from flag", inline=True)
label(0x8AFB, "store_tube_flag")      # BEQ/BNE: store Tube-transfer flag to l00a9
comment(0x8AFB, "Non-zero = Tube transfer required", inline=True)
comment(0x8AFD, "Copy param block bytes 1-4 to workspace", inline=True)
comment(0x8AFF, "Store to &BD+Y workspace area", inline=True)
comment(0x8B02, "Previous byte", inline=True)
comment(0x8B03, "Loop for bytes 3,2,1", inline=True)
comment(0x8B05, "Sub-function: AND #3 of (original A - 4)", inline=True)
comment(0x8B06, "Mask to 0-3 (OSGBPB 5-8 → 0-3)", inline=True)
comment(0x8B08, "A=0 (OSGBPB 5): read disc title", inline=True)
comment(0x8B0A, "LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)", inline=True)
comment(0x8B0B, "A=0 (OSGBPB 6): read CSD/LIB name", inline=True)
comment(0x8B0D, "C=1 (OSGBPB 8): read filenames from dir", inline=True)
label(0x8B0F, "gbpb6_read_name")      # BEQ: A=0 OSGBPB 6, load CSD/LIB/URD handle
comment(0x8B0F, "Y=0 for CSD or carry for fn code select", inline=True)
comment(0x8B10, "Get CSD/LIB/URD handles for FS command", inline=True)
comment(0x8B13, "Store CSD handle in command buffer", inline=True)
comment(0x8B16, "Load LIB handle from workspace", inline=True)
comment(0x8B19, "Store LIB handle in command buffer", inline=True)
comment(0x8B1C, "Load URD handle from workspace", inline=True)
comment(0x8B1F, "Store URD handle in command buffer", inline=True)
comment(0x8B22, "X=&12: buffer extent for command data", inline=True)
comment(0x8B24, "Store X as function code in header", inline=True)
comment(0x8B27, "&0D = 13 bytes of reply data expected", inline=True)
comment(0x8B29, "Store reply length in command buffer", inline=True)
comment(0x8B2C, "Store as byte count for copy loop", inline=True)
comment(0x8B2E, "LSR: &0D >> 1 = 6", inline=True)
comment(0x8B2F, "Store as command data byte", inline=True)
comment(0x8B32, "CLC for standard FS path", inline=True)
comment(0x8B38, "INX: X=1 after build_send_fs_cmd", inline=True)
comment(0x8B39, "Store X as reply start offset", inline=True)
comment(0x8B3B, "Copy FS reply to caller's buffer", inline=True)
comment(0x8B3D, "Non-zero: use Tube transfer path", inline=True)
comment(0x8B3F, "X = reply start offset", inline=True)
comment(0x8B41, "Y = reply buffer high byte", inline=True)
label(0x8B43, "copy_reply_bytes")     # Copy N bytes of FS reply data to caller buffer
comment(0x8B43, "Load reply data byte", inline=True)
comment(0x8B46, "Store to caller's buffer", inline=True)
comment(0x8B48, "Next source byte", inline=True)
comment(0x8B49, "Next destination byte", inline=True)
comment(0x8B4A, "Decrement remaining bytes", inline=True)
comment(0x8B4C, "Loop until all bytes copied", inline=True)
comment(0x8B4E, "ALWAYS branch to exit", inline=True)
label(0x8B50, "tube_transfer")        # BNE: l00a9 non-zero, claim Tube and send via R3
comment(0x8B50, "Claim Tube transfer channel", inline=True)
comment(0x8B53, "A=1: Tube claim type 1 (write)", inline=True)
comment(0x8B55, "X = param block address low", inline=True)
comment(0x8B57, "Y = param block address high", inline=True)
comment(0x8B59, "INX: advance past byte 0", inline=True)
comment(0x8B5A, "No page wrap: keep Y", inline=True)
comment(0x8B5C, "Page wrap: increment high byte", inline=True)
label(0x8B5D, "no_page_wrap")         # BNE: no page boundary crossed in copy
comment(0x8B5D, "Claim Tube address for transfer", inline=True)
comment(0x8B60, "X = reply data start offset", inline=True)
comment(0x8B62, "Load reply data byte", inline=True)
comment(0x8B65, "Send byte to Tube via R3", inline=True)
comment(0x8B68, "Next source byte", inline=True)
comment(0x8B69, "Delay loop for slow Tube co-processor", inline=True)
label(0x8B6B, "wait_tube_delay")      # 6-cycle delay loop between Tube R3 writes
comment(0x8B6B, "Decrement delay counter", inline=True)
comment(0x8B6C, "Loop until delay complete", inline=True)
comment(0x8B6E, "Decrement remaining bytes", inline=True)
comment(0x8B70, "Loop until all bytes sent to Tube", inline=True)
comment(0x8B72, "Release Tube after transfer complete", inline=True)
comment(0x8B74, "Release Tube address claim", inline=True)
label(0x8B77, "gbpb_done")            # BEQ: copy/adjust done, JMP return_a_zero
comment(0x8B77, "Return via restore_args path", inline=True)
label(0x8B7A, "gbpb8_read_dir")       # BCS: C=1 OSGBPB 8, read dir entries
comment(0x8B7A, "OSGBPB 8: read filenames from dir", inline=True)
comment(0x8B7C, "Byte 9: number of entries to read", inline=True)
comment(0x8B7E, "Store as reply count in command buffer", inline=True)
comment(0x8B81, "Y=5: byte 5 = starting entry number", inline=True)
comment(0x8B83, "Load starting entry number", inline=True)
comment(0x8B85, "Store in command buffer", inline=True)
comment(0x8B88, "X=&0D: command data extent", inline=True)
comment(0x8B8A, "Store extent in command buffer", inline=True)
comment(0x8B8D, "Y=2: function code for dir read", inline=True)
comment(0x8B8F, "Store 2 as reply data start offset", inline=True)
comment(0x8B91, "Store 2 as command data byte", inline=True)
comment(0x8B94, "Y=3: function code for header read", inline=True)
comment(0x8B98, "X=0 after FS command completes", inline=True)
comment(0x8B9A, "Load reply entry count", inline=True)
comment(0x8B9D, "Store at param block byte 0 (X=0)", inline=True)
comment(0x8B9F, "Load entries-read count from reply", inline=True)
comment(0x8BA2, "Y=9: param block byte 9", inline=True)
comment(0x8BA4, "Add to starting entry number", inline=True)
comment(0x8BA6, "Update param block with new position", inline=True)
comment(0x8BA8, "Load total reply length", inline=True)
comment(0x8BAA, "Subtract header (7 bytes) from reply len", inline=True)
comment(0x8BAC, "Store adjusted length in command buffer", inline=True)
comment(0x8BAF, "Store as byte count for copy loop", inline=True)
comment(0x8BB1, "Zero bytes: skip copy", inline=True)
comment(0x8BB3, "Copy reply data to caller's buffer", inline=True)
label(0x8BB6, "skip_copy_reply")      # BEQ: zero byte count, skip copy_reply_to_caller
comment(0x8BB6, "X=2: clear 3 bytes", inline=True)
label(0x8BB8, "zero_cmd_bytes")       # Zero 3 bytes of &0F07 area before address adjustment
comment(0x8BB8, "Zero out &0F07+X area", inline=True)
comment(0x8BBB, "Next byte", inline=True)
comment(0x8BBC, "Loop for X=2,1,0", inline=True)
comment(0x8BBE, "Adjust pointer by +1 (one filename read)", inline=True)
comment(0x8BC1, "SEC for reverse adjustment", inline=True)
comment(0x8BC2, "Reverse adjustment for updated counter", inline=True)
comment(0x8BC4, "Load entries-read count", inline=True)
comment(0x8BC7, "Store in command buffer", inline=True)
comment(0x8BCA, "Adjust param block addresses", inline=True)
comment(0x8BCD, "Z=1: all done, exit", inline=True)
comment(0x8BCF, "A=&C3: Tube claim with retry", inline=True)
comment(0x8BD1, "Request Tube address claim", inline=True)
comment(0x8BD4, "C=0: claim failed, retry", inline=True)
comment(0x8BD6, "Tube claimed successfully", inline=True)
comment(0x8BD7, "Save A/X/Y and set up command ptr", inline=True)
comment(0x8BDA, "X=&FF: table index (pre-incremented)", inline=True)
comment(0x8BDC, "Disable column formatting", inline=True)
label(0x8BDE, "scan_cmd_table")        # Outer command-table search loop for * command match
comment(0x8BDE, "Y=&FF: input index (pre-incremented)", inline=True)
comment(0x8BE0, "Advance input pointer", inline=True)
comment(0x8BE1, "Advance table pointer", inline=True)
comment(0x8BE2, "Load table character", inline=True)
comment(0x8BE5, "Bit 7: end of name, dispatch", inline=True)
comment(0x8BE7, "XOR input char with table char", inline=True)
comment(0x8BE9, "Case-insensitive (clear bit 5)", inline=True)
comment(0x8BEB, "Match: continue comparing", inline=True)
comment(0x8BED, "Mismatch: back up table pointer", inline=True)
comment(0x8BEE, "Skip to end of table entry", inline=True)
comment(0x8BEF, "Load table byte", inline=True)
comment(0x8BF2, "Loop until bit 7 set (end marker)", inline=True)
comment(0x8BF4, "Check input for '.' abbreviation", inline=True)
comment(0x8BF6, "Skip past handler high byte", inline=True)
comment(0x8BF7, "Is input '.' (abbreviation)?", inline=True)
comment(0x8BF9, "No: try next table entry", inline=True)
comment(0x8BFB, "Yes: skip '.' in input", inline=True)
comment(0x8BFC, "Back to handler high byte", inline=True)
comment(0x8BFD, "ALWAYS branch; dispatch via BMI", inline=True)
label(0x8BFF, "dispatch_cmd")         # BMI: end-of-name marker, push handler addr/dispatch
comment(0x8BFF, "Push handler address high byte", inline=True)
comment(0x8C00, "Load handler address low byte", inline=True)
comment(0x8C03, "Push handler address low byte", inline=True)
comment(0x8C04, "Dispatch via RTS (addr-1 on stack)", inline=True)
comment(0x8C05, "Match last char against '.' for *I. abbreviation", inline=True)
comment(0x8C21, "X=3: column count for multi-column layout", inline=True)
comment(0x8C23, "CRFLAG=3: first entry will trigger newline", inline=True)
comment(0x8C25, "Y=0: initialise column counter", inline=True)
comment(0x8C27, "A=&0B: examine argument count", inline=True)
label(0x8C29, "init_cat_params")       # Store examine arg count, init catalogue display
comment(0x8C29, "Store examine argument count", inline=True)
comment(0x8C2B, "Store column count", inline=True)
comment(0x8C2D, "A=6: examine format type in command", inline=True)
comment(0x8C2F, "Store format type at &0F05", inline=True)
comment(0x8C32, "Set up command parameter pointers", inline=True)
comment(0x8C35, "X=1: copy dir name at cmd offset 1", inline=True)
comment(0x8C37, "Copy directory name to command buffer", inline=True)
comment(0x8C3F, "X=3: start printing from reply offset 3", inline=True)
comment(0x8C41, "Print directory title (10 chars)", inline=True)
comment(0x8C44, "Print '('", inline=True)
comment(0x8C48, "Load station number from FS reply", inline=True)
comment(0x8C4B, "Print station number as decimal", inline=True)
comment(0x8C4E, "Print ')     '", inline=True)
comment(0x8C5A, "Non-zero: Public access", inline=True)
comment(0x8C5C, "Print 'Owner' + CR", inline=True)
label(0x8C67, "print_public")          # BNE: access non-zero (public), print "Public"+CR
comment(0x8C67, "Print 'Public' + CR", inline=True)
comment(0x8C76, "X=1: past command code byte", inline=True)
comment(0x8C77, "Y=&10: print 16 characters", inline=True)
comment(0x8C79, "Print disc/CSD name from reply", inline=True)
comment(0x8C7C, "Print '    Option '", inline=True)
comment(0x8C8D, "X = boot option for name table lookup", inline=True)
comment(0x8C8E, "Print boot option as hex digit", inline=True)
comment(0x8C91, "Print ' ('", inline=True)
comment(0x8CA1, "Next character", inline=True)
comment(0x8CA2, "Continue printing option name", inline=True)
label(0x8CA4, "done_option_name")      # BMI: bit 7 set, option name printing complete
comment(0x8CA4, "Print ')' + CR + 'Dir. '", inline=True)
comment(0x8CC2, "Print library name", inline=True)
label(0x8CC8, "fetch_dir_batch")       # Loop: store entry offset, issue next examine batch
comment(0x8CC8, "Store entry start offset for request", inline=True)
comment(0x8CCB, "Save start offset in zero page for loop", inline=True)
comment(0x8CCD, "Load examine arg count for batch size", inline=True)
comment(0x8CCF, "Store as request count at &0F07", inline=True)
comment(0x8CD2, "Load column count for display format", inline=True)
comment(0x8CD4, "Store column count in command data", inline=True)
comment(0x8CD7, "X=3: copy directory name at offset 3", inline=True)
comment(0x8CD9, "Append directory name to examine command", inline=True)
comment(0x8CE1, "X past command code byte in reply", inline=True)
comment(0x8CE2, "Load entry count from reply", inline=True)
label(0x8CE7, "process_entries")      # BNE: non-zero entry count, save and process batch
comment(0x8CE7, "Save entry count for batch processing", inline=True)
label(0x8CE8, "scan_entry_terminator") # Advance through catalogue entry to bit-7 terminator
comment(0x8CE8, "Advance Y past entry data bytes", inline=True)
comment(0x8CE9, "Read entry byte from reply buffer", inline=True)
comment(0x8CEC, "Loop until high-bit terminator found", inline=True)
comment(0x8CEE, "Store terminator as print boundary", inline=True)
comment(0x8CF1, "Print/format this directory entry", inline=True)
comment(0x8CF4, "Restore entry count from stack", inline=True)
comment(0x8CF5, "CLC for addition", inline=True)
comment(0x8CF6, "Advance start offset by entry count", inline=True)
comment(0x8CF8, "Y = new entry start offset", inline=True)
comment(0x8CF9, "More entries: fetch next batch", inline=True)
comment(0x8CFB, "Y=&0A: default print 10 characters", inline=True)
comment(0x8CFD, "Load reply byte at offset X", inline=True)
comment(0x8D03, "Next reply byte", inline=True)
comment(0x8D04, "Decrement character count", inline=True)
comment(0x8D05, "Loop for remaining characters", inline=True)
comment(0x8D63, "X=4: print 4 hex bytes", inline=True)
comment(0x8D65, "Load byte from parameter block", inline=True)
comment(0x8D67, "Print as two hex digits", inline=True)
comment(0x8D6A, "Next byte (descending)", inline=True)
comment(0x8D6B, "Count down", inline=True)
comment(0x8D6C, "Loop until 4 bytes printed", inline=True)
comment(0x8D6E, "A=space character", inline=True)
comment(0x8D75, "Start writing at &0F05 (after cmd header)", inline=True)
comment(0x8D7B, "Store to FS command buffer (&0F05+X)", inline=True)
comment(0x8D7F, "Advance source pointer", inline=True)
comment(0x8D84, "Return; X = next free position in buffer", inline=True)
comment(0x8D89, "X=0: start from first reply byte", inline=True)
comment(0x8D8B, "Load byte from FS reply buffer", inline=True)
comment(0x8D8E, "Bit 7 set: end of string, return", inline=True)
comment(0x8D90, "Non-zero: print character", inline=True)
comment(0x8D92, "Null byte: check column counter", inline=True)
comment(0x8D94, "Negative: print CR (no columns)", inline=True)
comment(0x8D96, "Advance column counter", inline=True)
comment(0x8D97, "Transfer to A for modulo", inline=True)
comment(0x8D98, "Modulo 4 columns", inline=True)
comment(0x8D9A, "Update column counter", inline=True)
comment(0x8D9C, "Column 0: start new line", inline=True)
comment(0x8D9E, "Print 2-space column separator", inline=True)
label(0x8DAA, "next_dir_entry")        # Always-branch: advance X, loop for next entry
comment(0x8DAA, "Next byte in reply buffer", inline=True)
comment(0x8DAB, "Loop until end of buffer", inline=True)
comment(0x8DB0, "Y = value to print", inline=True)
comment(0x8DB1, "Divisor = 100 (hundreds digit)", inline=True)
comment(0x8DB3, "Print hundreds digit", inline=True)
comment(0x8DB6, "Divisor = 10 (tens digit)", inline=True)
comment(0x8DB8, "Print tens digit", inline=True)
comment(0x8DBB, "Divisor = 1; fall through to units", inline=True)
comment(0x8DBD, "Save divisor to workspace", inline=True)
comment(0x8DBF, "A = dividend (from Y)", inline=True)
comment(0x8DC0, "X = &2F = ASCII '0' - 1", inline=True)
comment(0x8DC2, "Prepare for subtraction", inline=True)
label(0x8DC3, "divide_subtract")        # Repeated-subtraction division for decimal print
comment(0x8DC3, "Count one subtraction (next digit value)", inline=True)
comment(0x8DC4, "A = A - divisor", inline=True)
comment(0x8DC6, "Loop while A >= 0 (borrow clear)", inline=True)
comment(0x8DC8, "Undo last subtraction: A = remainder", inline=True)
comment(0x8DCA, "Y = remainder for caller", inline=True)
comment(0x8DCB, "A = X = ASCII digit character", inline=True)
label(0x8DCC, "print_digit")            # Print decimal digit via JMP OSASCI
comment(0x8DCF, "Parse filename from command line", inline=True)
comment(0x8DD2, "Copy filename to FS command buffer", inline=True)
comment(0x8DD5, "Y=0: start of text for GSINIT", inline=True)
comment(0x8DD7, "CLC before GSINIT call", inline=True)
comment(0x8DD8, "GSINIT/GSREAD: skip past the filename", inline=True)
label(0x8DDB, "skip_gs_filename")      # Call GSREAD repeatedly to skip past GS filename string
comment(0x8DDB, "Read next filename character", inline=True)
comment(0x8DDE, "C=0: more characters, keep reading", inline=True)
comment(0x8DE0, "Skip spaces after filename", inline=True)
comment(0x8DE3, "Calculate context addr = text ptr + Y", inline=True)
comment(0x8DE4, "Y = offset past filename end", inline=True)
comment(0x8DE5, "Add text pointer low byte", inline=True)
comment(0x8DE7, "Store context address low byte", inline=True)
comment(0x8DEA, "Load text pointer high byte", inline=True)
comment(0x8DEC, "Add carry from low byte addition", inline=True)
comment(0x8DEE, "Store context address high byte", inline=True)
comment(0x8DF1, "X=&0E: FS command buffer offset", inline=True)
comment(0x8DF3, "Store block offset for FS command", inline=True)
comment(0x8DF5, "A=&10: 16 bytes of command data", inline=True)
comment(0x8DF7, "Store options byte", inline=True)
comment(0x8DF9, "Store to FS workspace", inline=True)
comment(0x8DFC, "X=&4A: TXCB size for load command", inline=True)
comment(0x8DFE, "Y=5: FCCMND (load as command)", inline=True)
comment(0x8E00, "Send FS examine/load command", inline=True)
comment(0x8E03, "Check for Tube co-processor", inline=True)
comment(0x8E06, "No Tube: execute locally", inline=True)
comment(0x8E08, "Check load address upper bytes", inline=True)
comment(0x8E0B, "Continue address range check", inline=True)
comment(0x8E0E, "Carry set: not Tube space, exec locally", inline=True)
comment(0x8E10, "Claim Tube transfer channel", inline=True)
comment(0x8E13, "X=9: source offset in FS reply", inline=True)
comment(0x8E15, "Y=&0F: page &0F (FS command buffer)", inline=True)
comment(0x8E17, "A=4: Tube transfer type 4 (256-byte)", inline=True)
comment(0x8E19, "Transfer data to Tube co-processor", inline=True)
comment(0x8E1C, "Execute at load address via indirect JMP", inline=True)
comment(0x8E1F, "Save library handle from FS reply", inline=True)
comment(0x8E22, "SDISC path: skip CSD, jump to return", inline=True)
comment(0x8E24, "Store CSD handle from FS reply", inline=True)
label(0x8E27, "jmp_restore_args")      # JMP restore_args_return (common FS reply exit)
comment(0x8E27, "Restore A/X/Y and return to caller", inline=True)
comment(0x8E2A, "Set carry: LOGIN path (copy + boot)", inline=True)
comment(0x8E2B, "Copy 4 bytes: boot option + 3 handles", inline=True)
comment(0x8E2D, "SDISC: skip boot option, copy handles only", inline=True)
comment(0x8E2F, "Load from FS reply (&0F05+X)", inline=True)
comment(0x8E32, "Store to handle workspace (&0E02+X)", inline=True)
label(0x8E35, "copy_handles_loop")    # SDISC entry: skip boot option byte, X=3 descending
comment(0x8E35, "Next handle (descending)", inline=True)
comment(0x8E36, "Loop while X >= 0", inline=True)
comment(0x8E38, "SDISC: done, restore args and return", inline=True)
comment(0x8E3A, "Y = boot option from FS workspace", inline=True)
comment(0x8E3D, "X = command string offset from table", inline=True)
comment(0x8E40, "Y = &8D (high byte of command address)", inline=True)
comment(0x8E42, "Execute boot command string via OSCLI", inline=True)
comment(0x8E45, "Load handle from &F0", inline=True)
comment(0x8E5F, "Look up handle &F0 in workspace", inline=True)
comment(0x8E62, "Invalid handle: return 0", inline=True)
comment(0x8E64, "Load stored handle value", inline=True)
comment(0x8E66, "&3F = unused/closed slot marker", inline=True)
comment(0x8E68, "Slot in use: return actual value", inline=True)
comment(0x8E6A, "Return 0 for closed/invalid handle", inline=True)
label(0x8E6C, "store_handle_return")   # Store handle result to &F0, return
comment(0x8E6C, "Store result back to &F0", inline=True)
comment(0x8E6E, "Return", inline=True)
comment(0x8E6F, "Look up handle &F0 in workspace", inline=True)
comment(0x8E72, "Invalid handle: return 0", inline=True)
comment(0x8E7E, "Return", inline=True)
comment(0x8E85, "Only OSWORDs &0F-&13 (index 0-4)", inline=True)
comment(0x8E87, "Index >= 5: not ours, return", inline=True)
comment(0x8E89, "Dispatch via PHA/PHA/RTS table", inline=True)
comment(0x8E8C, "Y=2: restore 3 bytes (&AA-&AC)", inline=True)
label(0x8E8E, "copy_param_ptr")       # Restore 3-byte param block pointer from (net_rx_ptr)
comment(0x8E8E, "Load saved param block byte", inline=True)
comment(0x8E90, "Restore to &AA-&AC", inline=True)
comment(0x8E93, "Next byte (descending)", inline=True)
comment(0x8E94, "Loop for all 3 bytes", inline=True)
comment(0x8E96, "Return to service handler", inline=True)
comment(0x8E97, "X = sub-function code for table lookup", inline=True)
comment(0x8E98, "Load handler address high byte from table", inline=True)
comment(0x8E9B, "Push high byte for RTS dispatch", inline=True)
comment(0x8E9C, "Load handler address low byte from table", inline=True)
comment(0x8EA0, "Y=2: save 3 bytes (&AA-&AC)", inline=True)
comment(0x8EA2, "Load param block pointer byte", inline=True)
comment(0x8EA5, "Save to NFS workspace via (net_rx_ptr)", inline=True)
comment(0x8EA7, "Next byte (descending)", inline=True)
comment(0x8EA8, "Loop for all 3 bytes", inline=True)
comment(0x8EAA, "Y=0 after BPL exit; INY makes Y=1", inline=True)
comment(0x8EAB, "Read sub-function code from (&F0)+1", inline=True)
comment(0x8EAD, "Store Y=1 to &A9", inline=True)
comment(0x8EAF, "RTS dispatches to pushed handler address", inline=True)
comment(0x8EC0, "User TX CB in workspace page (high byte)", inline=True)
comment(0x8EC2, "Set param block high byte", inline=True)
comment(0x8EC4, "Set LTXCBP high byte for low-level TX", inline=True)
comment(0x8EC6, "&6F: offset into workspace for user TXCB", inline=True)
comment(0x8EC8, "Set param block low byte", inline=True)
comment(0x8ECA, "Set LTXCBP low byte for low-level TX", inline=True)
comment(0x8ECC, "X=15: copy 16 bytes (OSWORD param block)", inline=True)
comment(0x8ECE, "Copy param block to user TX control block", inline=True)
comment(0x8ED1, "Start user transmit via BRIANX", inline=True)
comment(0x8ED4, "Set source high byte from workspace page", inline=True)
comment(0x8ED6, "Store as copy source high byte in &AC", inline=True)
comment(0x8ED8, "JSRSIZ at workspace offset &7F", inline=True)
comment(0x8EDA, "Load buffer size from workspace", inline=True)
comment(0x8EDC, "Y=&80: start of JSR argument data", inline=True)
comment(0x8EDD, "Store &80 as copy source low byte", inline=True)
comment(0x8EDF, "X = buffer size (loop counter)", inline=True)
comment(0x8EE0, "X = size-1 (0-based count for copy)", inline=True)
comment(0x8EE1, "Y=0: start of destination param block", inline=True)
comment(0x8EE3, "Copy X+1 bytes from workspace to param", inline=True)
comment(0x8EE6, "Clear JSR protection status (CLRJSR)", inline=True)
comment(0x8EE9, "Y=&7F: JSRSIZ offset (READRB entry)", inline=True)
comment(0x8EEB, "Load buffer size from workspace", inline=True)
comment(0x8EED, "Y=1: param block offset for size byte", inline=True)
comment(0x8EEF, "Store buffer size to (&F0)+1", inline=True)
comment(0x8EF1, "Y=2: param block offset for args size", inline=True)
comment(0x8EF2, "A=&80: argument data starts at offset &80", inline=True)
comment(0x8EF4, "Store args start offset to (&F0)+2", inline=True)
comment(0x8EF6, "Return", inline=True)
label(0x8EF7, "osword_12_offsets")   # OSWORD &12 sub-function offset table
comment(0x8EFF, "Sub-function 4 or 5: read/set protection", inline=True)
comment(0x8F01, "LSR: 0->0, 1->0, 2->1, 3->1", inline=True)
comment(0x8F02, "X=&0D: default to static workspace page", inline=True)
comment(0x8F04, "Transfer LSR result to Y for indexing", inline=True)
comment(0x8F05, "Y=0 (sub 0-1): use page &0D", inline=True)
comment(0x8F07, "Y=1 (sub 2-3): use dynamic workspace", inline=True)
label(0x8F09, "set_workspace_page")   # Sub-fn 0-1: use static page &0D, store to &AC
comment(0x8F09, "Store workspace page in &AC (hi byte)", inline=True)
comment(0x8F0B, "Load offset: &FF (sub 0-1) or &01 (sub 2-3)", inline=True)
comment(0x8F0E, "Store offset in &AB (lo byte)", inline=True)
comment(0x8F10, "X=1: copy 2 bytes", inline=True)
comment(0x8F12, "Y=1: start at param block offset 1", inline=True)
label(0x8F14, "copy_param_workspace")  # Bidirectional copy between param block and workspace
comment(0x8F16, "C=1: copy from param to workspace", inline=True)
comment(0x8F18, "Store param byte to workspace", inline=True)
label(0x8F1A, "skip_param_write")     # C=0: skip writing param to workspace
comment(0x8F1F, "Decrement remaining count", inline=True)
comment(0x8F20, "Loop while bytes remain", inline=True)
comment(0x8F22, "Return", inline=True)
comment(0x8F23, "LSR A: test bit 0 of sub-function", inline=True)
comment(0x8F24, "Y=1: offset for protection byte", inline=True)
comment(0x8F25, "Load protection byte from param block", inline=True)
comment(0x8F27, "C=1 (odd sub): set protection", inline=True)
comment(0x8F29, "C=0 (even sub): read current status", inline=True)
comment(0x8F2C, "Return current value to param block", inline=True)
comment(0x8F2E, "Update protection status", inline=True)
comment(0x8F31, "Also save as JSR mask backup", inline=True)
comment(0x8F34, "Return", inline=True)
label(0x8F35, "read_fs_handle")       # Read one FS handle from RX data at offset &14
comment(0x8F35, "Y=&14: RX buffer offset for FS handle", inline=True)
comment(0x8F37, "Read FS reply handle from RX data", inline=True)
comment(0x8F39, "Y=1: param block byte 1", inline=True)
comment(0x8F3B, "Return handle to caller's param block", inline=True)
comment(0x8F3D, "Return", inline=True)
comment(0x8F3E, "Sub-function 8: read FS handle", inline=True)
comment(0x8F40, "Match: read handle from RX buffer", inline=True)
comment(0x8F42, "Sub-function 9: read args size", inline=True)
comment(0x8F44, "Match: read ARGS buffer info", inline=True)
comment(0x8F46, "Sub >= 10 (bit 7 clear): read error", inline=True)
comment(0x8F48, "Y=3: start from handle 3 (descending)", inline=True)
comment(0x8F4A, "LSR: test read/write bit", inline=True)
comment(0x8F4B, "C=0: read handles from workspace", inline=True)
comment(0x8F4D, "Init loop counter at Y=3", inline=True)
label(0x8F4F, "copy_handles_to_ws")   # Convert handles to bitmasks and store to workspace
comment(0x8F4F, "Reload loop counter", inline=True)
comment(0x8F51, "Read handle from caller's param block", inline=True)
comment(0x8F53, "Convert handle number to bitmask", inline=True)
comment(0x8F56, "TYA: get bitmask result", inline=True)
comment(0x8F57, "Reload loop counter", inline=True)
comment(0x8F59, "Store bitmask to FS server table", inline=True)
comment(0x8F5C, "Next handle (descending)", inline=True)
comment(0x8F5E, "Loop for handles 3,2,1", inline=True)
comment(0x8F60, "Return", inline=True)
label(0x8F61, "return_last_error")    # Sub-fn >= 10, bit 7 clear: return last FS error
comment(0x8F61, "Y=1 (post-INY): param block byte 1", inline=True)
comment(0x8F62, "Read last FS error code", inline=True)
comment(0x8F65, "Return error to caller's param block", inline=True)
comment(0x8F67, "Return", inline=True)
comment(0x8F70, "Next handle (descending)", inline=True)
comment(0x8F71, "Loop for handles 3,2,1", inline=True)
comment(0x8F73, "Return", inline=True)
comment(0x8F74, "Workspace page high byte", inline=True)
comment(0x8F76, "Set up pointer high byte in &AC", inline=True)
comment(0x8F78, "Save param block high byte in &AB", inline=True)
comment(0x8F7A, "Disable user RX during CB operation", inline=True)
comment(0x8F7D, "Read first byte of param block", inline=True)
comment(0x8F7F, "Save: 0=open new, non-zero=read RXCB", inline=True)
comment(0x8F81, "Non-zero: read specified RXCB", inline=True)
comment(0x8F83, "Start scan from RXCB #3 (0-2 reserved)", inline=True)
comment(0x8F85, "Convert RXCB number to workspace offset", inline=True)
comment(0x8F88, "Invalid RXCB: return zero", inline=True)
comment(0x8F8A, "LSR twice: byte offset / 4", inline=True)
comment(0x8F8B, "Yields RXCB number from offset", inline=True)
comment(0x8F8C, "X = RXCB number for iteration", inline=True)
comment(0x8F8D, "Read flag byte from RXCB workspace", inline=True)
comment(0x8F8F, "Zero = end of CB list", inline=True)
comment(0x8F91, "&3F = deleted slot, free for reuse", inline=True)
comment(0x8F93, "Found free slot", inline=True)
comment(0x8F95, "Try next RXCB", inline=True)
comment(0x8F96, "A = next RXCB number", inline=True)
comment(0x8F97, "Continue scan (always branches)", inline=True)
comment(0x8F99, "A = free RXCB number", inline=True)
comment(0x8F9A, "X=0 for indexed indirect store", inline=True)
comment(0x8F9C, "Return RXCB number to caller's byte 0", inline=True)
label(0x8F9E, "read_rxcb")            # BNE: non-zero RXCB param, skip free-slot scan
comment(0x8F9E, "Convert RXCB number to workspace offset", inline=True)
comment(0x8FA1, "Invalid: write zero to param block", inline=True)
comment(0x8FA3, "Y = offset-1: points to flag byte", inline=True)
comment(0x8FA4, "Set &AB = workspace ptr low byte", inline=True)
comment(0x8FA6, "&C0: test mask for flag byte", inline=True)
comment(0x8FA8, "Y=1: flag byte offset in RXCB", inline=True)
comment(0x8FAC, "Compare Y(1) with saved byte (open/read)", inline=True)
comment(0x8FAE, "ADC flag: test if slot is in use", inline=True)
comment(0x8FB2, "Negative: slot has received data", inline=True)
label(0x8FB4, "copy_rxcb_to_param")   # Copy RXCB data from workspace to param block
comment(0x8FB4, "C=0: workspace-to-param direction", inline=True)
comment(0x8FB5, "Copy RXCB data to param block", inline=True)
comment(0x8FB8, "Done: skip deletion on error", inline=True)
comment(0x8FBA, "Mark CB as consumed (consume-once)", inline=True)
comment(0x8FBC, "Y=1: flag byte offset", inline=True)
comment(0x8FBE, "Write &3F to mark slot deleted", inline=True)
comment(0x8FC0, "Branch to exit (always taken)", inline=True)
comment(0x8FC2, "Advance through multi-byte field", inline=True)
comment(0x8FC4, "Loop until all bytes processed", inline=True)
comment(0x8FC6, "Y=-1 → Y=0 after STA below", inline=True)
comment(0x8FC7, "Return zero (no free RXCB found)", inline=True)
label(0x8FC9, "reenable_rx")          # Common exit: ROL rx_flags, RTS
comment(0x8FC9, "Re-enable user RX", inline=True)
comment(0x8FCC, "Return", inline=True)
comment(0x8FCD, "Y=&1C: workspace offset for RX data start", inline=True)
comment(0x8FCF, "A = base address low byte", inline=True)
comment(0x8FD1, "A = base + 1 (skip length byte)", inline=True)
comment(0x8FD6, "Read data length from (&F0)+1", inline=True)
comment(0x8FD8, "A = data length byte", inline=True)
comment(0x8FDA, "Workspace offset &20 = RX data end", inline=True)
comment(0x8FDC, "A = base + length = end address low", inline=True)
comment(0x8FDE, "Store low byte of 16-bit address", inline=True)
comment(0x8FE0, "Advance to high byte offset", inline=True)
comment(0x8FE1, "A = high byte of base address", inline=True)
comment(0x8FE3, "Add carry for 16-bit addition", inline=True)
comment(0x8FE5, "Store high byte", inline=True)
comment(0x8FE7, "Return", inline=True)
comment(0x8FEA, "A >= 1: handle TX result", inline=True)
comment(0x8FEC, "Y=&23: start of template (descending)", inline=True)
comment(0x8FEE, "Load ROM template byte", inline=True)
comment(0x8FF1, "Non-zero = use ROM template byte as-is", inline=True)
comment(0x8FF3, "Zero = substitute from NMI workspace", inline=True)
label(0x8FF6, "store_txcb_byte")      # BNE: non-zero template byte, skip substitution
comment(0x8FF6, "Store to dynamic workspace", inline=True)
comment(0x8FF8, "Descend through template", inline=True)
comment(0x8FF9, "Stop at offset &17", inline=True)
comment(0x8FFB, "Loop until all bytes copied", inline=True)
comment(0x8FFD, "Y=&18: TX block starts here", inline=True)
comment(0x8FFE, "Point net_tx_ptr at workspace+&18", inline=True)
comment(0x9000, "Set up RX buffer start/end pointers", inline=True)
comment(0x9003, "Y=2: port byte offset in RXCB", inline=True)
comment(0x9005, "A=&90: FS reply port", inline=True)
comment(0x9007, "Store port &90 at (&F0)+2", inline=True)
label(0x900B, "copy_fs_addr")          # Copy 3-byte FS station address into RX param block
comment(0x900B, "Copy FS station addr from workspace", inline=True)
comment(0x900E, "Store to RX param block", inline=True)
comment(0x9010, "Next byte", inline=True)
comment(0x9011, "Done 3 bytes (Y=4,5,6)?", inline=True)
comment(0x9013, "No: continue copying", inline=True)
comment(0x9015, "High byte of workspace for TX ptr", inline=True)
comment(0x9017, "Store as TX pointer high byte", inline=True)
comment(0x9019, "Enable interrupts before transmit", inline=True)
comment(0x901A, "Transmit with full retry", inline=True)
comment(0x901D, "Y=&20: RX end address offset", inline=True)
comment(0x901F, "Set RX end address to &FFFF (accept any length)", inline=True)
comment(0x9021, "Store end address low byte (&FF)", inline=True)
comment(0x9024, "Store end address high byte (&FF)", inline=True)
comment(0x9026, "Y=&19: port byte in workspace RXCB", inline=True)
comment(0x9028, "A=&90: FS reply port", inline=True)
comment(0x902A, "Store port to workspace RXCB", inline=True)
comment(0x902D, "A=&7F: flag byte = waiting for reply", inline=True)
comment(0x902F, "Store flag byte to workspace RXCB", inline=True)
comment(0x9031, "Jump to RX poll (BRIANX)", inline=True)
label(0x9034, "handle_tx_result")     # BCS: A>=1, save flags and load RX result
comment(0x9034, "Save processor flags", inline=True)
comment(0x9035, "Y=1: first data byte offset", inline=True)
comment(0x9037, "Load first data byte from RX buffer", inline=True)
comment(0x9039, "X = first data byte (command code)", inline=True)
comment(0x903A, "Advance to next data byte", inline=True)
comment(0x903B, "Load station address high byte", inline=True)
comment(0x903D, "Advance past station addr", inline=True)
comment(0x903E, "Save Y as data index", inline=True)
comment(0x9040, "Store station addr hi at (net_rx_ptr)+&72", inline=True)
comment(0x9042, "Store to workspace", inline=True)
comment(0x9045, "A = command code (from X)", inline=True)
comment(0x9046, "Store station addr lo at (net_rx_ptr)+&71", inline=True)
comment(0x9048, "Restore flags from earlier PHP", inline=True)
comment(0x9049, "First call: adjust data length", inline=True)
label(0x904B, "send_data_bytes")       # Outer loop: fetch and TX successive data bytes
comment(0x904B, "Reload data index", inline=True)
comment(0x904D, "Advance data index for next iteration", inline=True)
comment(0x904F, "Load next data byte", inline=True)
comment(0x9051, "Zero byte: end of data, return", inline=True)
comment(0x9053, "Y=&7D: store byte for TX at offset &7D", inline=True)
comment(0x9055, "Store data byte at (net_rx_ptr)+&7D for TX", inline=True)
comment(0x9057, "Save data byte for &0D check after TX", inline=True)
comment(0x9058, "Set up TX control block", inline=True)
comment(0x905B, "Enable IRQs and transmit", inline=True)
label(0x905E, "delay_between_tx")      # Spin-delay between consecutive TX packets
comment(0x905E, "Short delay loop between TX packets", inline=True)
comment(0x905F, "Spin until X reaches 0", inline=True)
comment(0x9061, "Restore data byte for terminator check", inline=True)
comment(0x9064, "Not &0D: continue with next byte", inline=True)
comment(0x9066, "Return (data complete)", inline=True)
comment(0x9067, "First-packet: set up control block", inline=True)
comment(0x906A, "Y=&7B: data length offset", inline=True)
comment(0x906C, "Load current data length", inline=True)
comment(0x906E, "Adjust data length by 3 for header bytes", inline=True)
comment(0x9070, "Store adjusted length", inline=True)
comment(0x9072, "Enable interrupts", inline=True)
comment(0x9073, "Transmit via tx_poll_ff", inline=True)
comment(0x9076, "Save processor status", inline=True)
comment(0x9077, "Save A (reason code)", inline=True)
comment(0x9078, "Save X", inline=True)
comment(0x9079, "Push X to stack", inline=True)
comment(0x907A, "Save Y", inline=True)
comment(0x907B, "Push Y to stack", inline=True)
comment(0x907C, "Get stack pointer for indexed access", inline=True)
comment(0x907D, "Retrieve original A (reason code) from stack", inline=True)
comment(0x9080, "Reason codes 0-8 only", inline=True)
comment(0x9082, "Code >= 9: skip dispatch, restore regs", inline=True)
comment(0x9084, "X = reason code for table lookup", inline=True)
comment(0x9085, "Dispatch to handler via trampoline", inline=True)
comment(0x9088, "Restore Y", inline=True)
comment(0x9089, "Transfer to Y register", inline=True)
comment(0x908A, "Restore X", inline=True)
comment(0x908B, "Transfer to X register", inline=True)
comment(0x908C, "Restore A", inline=True)
comment(0x908D, "Restore processor status flags", inline=True)
comment(0x908E, "Return with all registers preserved", inline=True)
comment(0x9092, "Push high byte of handler address", inline=True)
comment(0x9093, "Load handler low byte from table", inline=True)
comment(0x9096, "Push low byte of handler address", inline=True)
comment(0x9097, "Load workspace byte &EF for handler", inline=True)
comment(0x9099, "RTS dispatches to pushed handler", inline=True)
label(0x90AC, "net_write_char_handler") # NETVEC fn 4: net write character (NWRCH)
comment(0x90AC, "Get stack pointer for P register access", inline=True)
comment(0x90AD, "ROR/ASL on stacked P: zeros carry to signal success", inline=True)
comment(0x90B0, "ASL: restore P after ROR zeroed carry", inline=True)
comment(0x90B3, "Y = character to write", inline=True)
comment(0x90B4, "Store character at workspace offset &DA", inline=True)
comment(0x90B6, "Store char at workspace offset &DA", inline=True)
comment(0x90B8, "A=0: command type for net write char", inline=True)
comment(0x90BA, "Y=&D9: command type offset", inline=True)
comment(0x90BC, "Store command type at ws+&D9", inline=True)
comment(0x90BE, "Mark TX control block as active (&80)", inline=True)
comment(0x90C0, "Y=&0C: TXCB start offset", inline=True)
comment(0x90C2, "Set TX active flag at ws+&0C", inline=True)
comment(0x90C4, "Save net_tx_ptr; redirect to workspace TXCB", inline=True)
comment(0x90C6, "Save net_tx_ptr low", inline=True)
comment(0x90C7, "Load net_tx_ptr high", inline=True)
comment(0x90C9, "Save net_tx_ptr high", inline=True)
comment(0x90CA, "Redirect net_tx_ptr low to workspace", inline=True)
comment(0x90CC, "Load workspace page high byte", inline=True)
comment(0x90CE, "Complete ptr redirect", inline=True)
comment(0x90D0, "Transmit with full retry", inline=True)
comment(0x90D3, "Mark TXCB as deleted (&3F) after transmit", inline=True)
comment(0x90D5, "Write &3F to TXCB byte 0", inline=True)
comment(0x90D7, "Restore net_tx_ptr high", inline=True)
comment(0x90D8, "Write back", inline=True)
comment(0x90DA, "Restore net_tx_ptr low", inline=True)
comment(0x90DB, "Write back", inline=True)
comment(0x90DD, "Return", inline=True)
comment(0x90DE, "Load original Y (OSBYTE secondary param)", inline=True)
comment(0x90E0, "OSBYTE &81 (INKEY): always forward to terminal", inline=True)
comment(0x90E2, "Forward &81 to terminal for keyboard read", inline=True)
comment(0x90E4, "Y=1: search NCTBPL table (execute on both)", inline=True)
comment(0x90E6, "X=7: 8-entry NCTBPL table size", inline=True)
comment(0x90E8, "Search for OSBYTE code in NCTBPL table", inline=True)
comment(0x90EB, "Match found: dispatch with Y=1 (both)", inline=True)
comment(0x90ED, "Y=-1: search NCTBMI table (terminal only)", inline=True)
comment(0x90EE, "Second DEY: Y=&FF (from 1 via 0)", inline=True)
comment(0x90EF, "X=&0E: 15-entry NCTBMI table size", inline=True)
comment(0x90F1, "Search for OSBYTE code in NCTBMI table", inline=True)
comment(0x90F4, "Match found: dispatch with Y=&FF (terminal)", inline=True)
comment(0x90F6, "Y=0: OSBYTE not recognised, ignore", inline=True)
label(0x90F7, "dispatch_remote_osbyte") # Common target for OSBYTE dispatch setup
comment(0x90F7, "X=2 bytes to copy (default for RBYTE)", inline=True)
comment(0x90F9, "A=Y: check table match result", inline=True)
comment(0x90FA, "Y=0: not recognised, return unhandled", inline=True)
comment(0x90FC, "Y>0 (NCTBPL): send only, no result expected", inline=True)
comment(0x90FD, "Y>0 (NCTBPL): no result expected, skip RX", inline=True)
comment(0x90FF, "Y<0 (NCTBMI): X=3 bytes (result + P flags)", inline=True)
comment(0x9100, "Y=&DC: top of 3-byte stack frame region", inline=True)
comment(0x9102, "Copy OSBYTE args from stack frame to workspace", inline=True)
comment(0x9105, "Store to NFS workspace for transmission", inline=True)
comment(0x9107, "Next byte (descending)", inline=True)
comment(0x9108, "Copied all 3 bytes? (&DC, &DB, &DA)", inline=True)
comment(0x910A, "Loop for remaining bytes", inline=True)
comment(0x910C, "A = byte count for setup_tx_and_send", inline=True)
comment(0x910D, "Build TXCB and transmit to terminal", inline=True)
comment(0x9110, "Restore N flag from table match type", inline=True)
comment(0x9111, "Y was positive (NCTBPL): done, no result", inline=True)
comment(0x9113, "Set up RX control block to wait for reply", inline=True)
comment(0x9119, "Bit7 clear: still waiting, poll again", inline=True)
comment(0x911B, "X = stack pointer for register restoration", inline=True)
comment(0x911C, "Y=&DD: saved P byte offset in workspace", inline=True)
comment(0x911E, "Load remote processor status from reply", inline=True)
comment(0x9120, "Force V=1 (claimed) and I=1 (no IRQ) in saved P", inline=True)
comment(0x9122, "ALWAYS branch (ORA #&44 never zero)", inline=True)
comment(0x9124, "Previous workspace offset", inline=True)
comment(0x9125, "Previous stack register slot", inline=True)
comment(0x9126, "Load next result byte (X, then Y)", inline=True)
comment(0x9128, "Write result bytes to stacked registers", inline=True)
comment(0x912B, "Copied all result bytes? (P at &DA)", inline=True)
comment(0x912D, "Loop for remaining result bytes", inline=True)
comment(0x912F, "Return to OSBYTE dispatcher", inline=True)
comment(0x9130, "Compare OSBYTE code with table entry", inline=True)
comment(0x9133, "Match found: return with Z=1", inline=True)
comment(0x9135, "Next table entry (descending)", inline=True)
comment(0x9136, "Loop for remaining entries", inline=True)
comment(0x9138, "Return; Z=1 if match, Z=0 if not", inline=True)
label(0x9139, "remote_osbyte_table") # OSBYTE codes accepted for remote execution
comment(0x914C, "OSWORD 7 (sound): handle via common path", inline=True)
comment(0x914E, "OSWORD 8 = define an envelope", inline=True)
comment(0x9150, "Not OSWORD 7 or 8: ignore (BNE exits)", inline=True)
label(0x9152, "copy_params_rword")     # Copy param bytes and tag as RWORD message
comment(0x9152, "Point workspace to offset &DB for params", inline=True)
comment(0x9154, "Store workspace ptr offset &DB", inline=True)
label(0x9156, "copy_osword_params")    # Copy OSWORD parameter bytes from RX buffer to workspace
comment(0x9156, "Load param byte from OSWORD param block", inline=True)
comment(0x9158, "Write param byte to workspace", inline=True)
comment(0x915A, "Next byte (descending)", inline=True)
comment(0x915B, "Loop for all parameter bytes", inline=True)
comment(0x915D, "Y=0 after loop", inline=True)
comment(0x915E, "Point workspace to offset &DA", inline=True)
comment(0x9160, "Load original OSWORD code", inline=True)
comment(0x9162, "Store OSWORD code at ws+0", inline=True)
comment(0x9164, "Reset workspace ptr to base", inline=True)
comment(0x9166, "Y=&14: command type offset", inline=True)
comment(0x9168, "Tag as RWORD (port &E9)", inline=True)
comment(0x916A, "Store port tag at ws+&14", inline=True)
comment(0x916C, "A=1: single-byte TX", inline=True)
comment(0x9171, "Restore workspace ptr", inline=True)
comment(0x9173, "X=&0D: template offset for alt entry", inline=True)
comment(0x9175, "Y=&7C: target workspace offset for alt entry", inline=True)
comment(0x9177, "BIT test: V flag = bit 6 of &83AF", inline=True)
comment(0x917A, "V=1: store to (net_rx_ptr) instead", inline=True)
comment(0x917C, "Y=&17: workspace target offset (main entry)", inline=True)
comment(0x917E, "X=&1A: template table index (main entry)", inline=True)
comment(0x9180, "V=0: target is (nfs_workspace)", inline=True)
comment(0x9181, "Load template byte from ctrl_block_template[X]", inline=True)
comment(0x9184, "&FE = stop sentinel", inline=True)
comment(0x9186, "End of template: jump to exit", inline=True)
comment(0x9188, "&FD = skip sentinel", inline=True)
comment(0x918A, "Skip: don't store, just decrement Y", inline=True)
comment(0x918C, "&FC = page byte sentinel", inline=True)
comment(0x918E, "Not sentinel: store template value directly", inline=True)
comment(0x9196, "PAGE byte → Y=&02 / Y=&74", inline=True)
comment(0x9198, "→ Y=&04 / Y=&76", inline=True)
comment(0x919A, "PAGE byte → Y=&06 / Y=&78", inline=True)
comment(0x919C, "→ Y=&08 / Y=&7A", inline=True)
label(0x91A0, "cb_template_main_start") # Control block template: main-path section
label(0x91A4, "cb_template_tail")    # Control block template: tail section
comment(0x91CF, "X-1: convert 1-based buffer to 0-based", inline=True)
comment(0x91D0, "Is this the network printer buffer?", inline=True)
comment(0x91D2, "No: skip printer init", inline=True)
comment(0x91D4, "&1F = initial buffer pointer offset", inline=True)
comment(0x91D6, "Reset printer buffer write position", inline=True)
comment(0x91D9, "&41 = initial PFLAGS (bit 6 set, bit 0 set)", inline=True)
comment(0x91DE, "Return", inline=True)
comment(0x91DF, "Only handle buffer 4 (network printer)", inline=True)
comment(0x91E1, "Not buffer 4: ignore", inline=True)
comment(0x91E3, "A = reason code", inline=True)
comment(0x91E4, "Reason 1? (DEX: 1->0)", inline=True)
comment(0x91E5, "Not reason 1: handle Ctrl-B/C", inline=True)
comment(0x91E7, "Get stack pointer for P register", inline=True)
comment(0x91E8, "Force I flag in stacked P to block IRQs", inline=True)
comment(0x91EB, "Write back modified P register", inline=True)
comment(0x91EE, "OSBYTE &91: extract char from MOS buffer", inline=True)
comment(0x91F0, "X=3: printer buffer number", inline=True)
comment(0x91F5, "Buffer empty: return", inline=True)
comment(0x91F7, "Y = extracted character", inline=True)
comment(0x91F8, "Store char in output buffer", inline=True)
comment(0x91FB, "Buffer nearly full? (&6E = threshold)", inline=True)
comment(0x91FD, "Not full: get next char", inline=True)
comment(0x91FF, "Buffer full: flush to network", inline=True)
comment(0x9202, "Continue after flush", inline=True)
comment(0x9204, "Load current buffer offset", inline=True)
comment(0x9207, "Store byte at current position", inline=True)
comment(0x9209, "Advance buffer pointer", inline=True)
comment(0x920C, "Return; Y = buffer offset", inline=True)
label(0x920D, "toggle_print_flag")    # Toggle print-active flag and update PFLAGS
comment(0x920D, "Save reason code", inline=True)
comment(0x920E, "A = reason code", inline=True)
comment(0x920F, "EOR #1: toggle print-active flag (bit 0)", inline=True)
comment(0x9211, "Store toggled flag as output byte", inline=True)
comment(0x9224, "Extract upper nibble of PFLAGS", inline=True)
comment(0x9226, "Shift for bit extraction", inline=True)
comment(0x9227, "Save in X", inline=True)
comment(0x9228, "Restore original reason code", inline=True)
comment(0x9229, "Merge print-active bit from original A", inline=True)
comment(0x922A, "Retrieve shifted PFLAGS", inline=True)
comment(0x922B, "Recombine into new PFLAGS value", inline=True)
comment(0x922F, "Return", inline=True)
comment(0x9230, "Store buffer length at workspace offset &08", inline=True)
comment(0x9232, "Current buffer fill position", inline=True)
comment(0x9235, "Write to workspace offset &08", inline=True)
comment(0x9237, "Store page high byte at offset &09", inline=True)
comment(0x9239, "Y=&09", inline=True)
comment(0x923A, "Write page high byte at offset &09", inline=True)
comment(0x923C, "Also store at offset &05", inline=True)
comment(0x923E, "(end address high byte)", inline=True)
comment(0x9240, "Y=&0B: flag byte offset", inline=True)
comment(0x9242, "X=&26: start from template entry &26", inline=True)
comment(0x9244, "Reuse ctrl_block_setup with CLV entry", inline=True)
comment(0x9247, "Y=&0A: sequence flag byte offset", inline=True)
comment(0x9253, "Old sequence bit into bit 0", inline=True)
comment(0x9254, "Store sequence flag at offset &0A", inline=True)
comment(0x9256, "Y=&1F: buffer start offset", inline=True)
comment(0x9258, "Reset printer buffer to start (&1F)", inline=True)
comment(0x925B, "A=0: printer output flag", inline=True)
comment(0x925D, "X=0: workspace low byte", inline=True)
comment(0x925E, "Y = workspace page high byte", inline=True)
comment(0x9260, "Enable interrupts before TX", inline=True)
comment(0x9261, "Set TX control block ptr low byte", inline=True)
comment(0x9263, "Set TX control block ptr high byte", inline=True)
comment(0x9265, "Save A (handle bitmask) for later", inline=True)
comment(0x9266, "Compute sequence bit from handle", inline=True)
comment(0x9269, "Zero: no sequence bit set", inline=True)
comment(0x926B, "Non-zero: normalise to bit 0", inline=True)
comment(0x926D, "Y=0: flag byte offset in TXCB", inline=True)
comment(0x926F, "Merge sequence into existing flag byte", inline=True)
comment(0x9271, "Save merged flag byte", inline=True)
comment(0x9272, "Write flag+sequence to TXCB byte 0", inline=True)
comment(0x9274, "Transmit with full retry", inline=True)
comment(0x9277, "End address &FFFF = unlimited data length", inline=True)
comment(0x9279, "Y=8: end address low offset in TXCB", inline=True)
comment(0x927B, "Store &FF to end addr low", inline=True)
comment(0x927E, "Store &FF to end addr high (Y=9)", inline=True)
comment(0x9280, "Recover merged flag byte", inline=True)
comment(0x9281, "Save in X for sequence compare", inline=True)
comment(0x9282, "Y=&D1: printer port number", inline=True)
comment(0x9284, "Recover saved handle bitmask", inline=True)
comment(0x9285, "Re-save for later consumption", inline=True)
comment(0x9286, "A=0: port &D1 (print); A!=0: port &90 (FS)", inline=True)
comment(0x9288, "Y=&90: FS data port", inline=True)
comment(0x928A, "A = selected port number", inline=True)
comment(0x928B, "Y=1: port byte offset in TXCB", inline=True)
comment(0x928D, "Write port to TXCB byte 1", inline=True)
comment(0x928F, "A = saved flag byte (expected sequence)", inline=True)
comment(0x9291, "Push expected sequence for retry loop", inline=True)
comment(0x9292, "Flag byte &7F = waiting for reply", inline=True)
comment(0x9294, "Write to TXCB flag byte (Y=0)", inline=True)
comment(0x9296, "Transmit and wait for reply (BRIANX)", inline=True)
comment(0x9299, "Recover expected sequence", inline=True)
comment(0x929A, "Keep on stack for next iteration", inline=True)
comment(0x929B, "Check if TX result matches expected sequence", inline=True)
comment(0x929D, "Bit 0 to carry (sequence mismatch?)", inline=True)
comment(0x929E, "C=1: mismatch, retry transmit", inline=True)
comment(0x92A0, "Clean up: discard expected sequence", inline=True)
comment(0x92A1, "Discard saved handle bitmask", inline=True)
comment(0x92A2, "Toggle sequence bit on success", inline=True)
comment(0x92A5, "Return", inline=True)
comment(0x92A6, "Save current table index", inline=True)
comment(0x92A8, "Push for later restore", inline=True)
comment(0x92A9, "Point workspace to palette save area (&E9)", inline=True)
comment(0x92AB, "Set workspace low byte", inline=True)
comment(0x92AD, "Y=0: first palette entry", inline=True)
comment(0x92AF, "Clear table index counter", inline=True)
comment(0x92B1, "Save current screen MODE to workspace", inline=True)
comment(0x92B4, "Store MODE at workspace[0]", inline=True)
comment(0x92B6, "Advance workspace pointer past MODE byte", inline=True)
comment(0x92B8, "Read colour count (from &0351)", inline=True)
comment(0x92BB, "Push for iteration count tracking", inline=True)
comment(0x92BC, "A=0: logical colour number for OSWORD", inline=True)
label(0x92BD, "save_palette_entry")    # Per-entry OSWORD &0B palette read and workspace store
comment(0x92BD, "Store logical colour at workspace[0]", inline=True)
comment(0x92BF, "X = workspace ptr low (param block addr)", inline=True)
comment(0x92C1, "Y = workspace ptr high", inline=True)
comment(0x92C3, "OSWORD &0B: read palette for logical colour", inline=True)
comment(0x92C8, "Recover colour count", inline=True)
comment(0x92C9, "Y=0: access workspace[0]", inline=True)
comment(0x92CB, "Write colour count back to workspace[0]", inline=True)
comment(0x92CD, "Y=1: access workspace[1] (palette result)", inline=True)
comment(0x92CE, "Read palette value returned by OSWORD", inline=True)
comment(0x92D0, "Push palette value for next iteration", inline=True)
comment(0x92D1, "X = current workspace ptr low", inline=True)
comment(0x92D3, "Advance workspace pointer", inline=True)
comment(0x92D5, "Increment table index", inline=True)
comment(0x92D7, "Y=0 for next store", inline=True)
comment(0x92D8, "Load table index as logical colour", inline=True)
comment(0x92DA, "Loop until workspace wraps past &F9", inline=True)
comment(0x92DC, "Continue for all 16 palette entries", inline=True)
comment(0x92DE, "Discard last palette value from stack", inline=True)
comment(0x92DF, "Reset table index to 0", inline=True)
comment(0x92E1, "Advance workspace past palette data", inline=True)
comment(0x92E3, "Save cursor pos and OSBYTE state values", inline=True)
comment(0x92E6, "Advance workspace past VDU state data", inline=True)
comment(0x92E8, "Recover saved table index", inline=True)
comment(0x92E9, "Restore table index", inline=True)
comment(0x92EB, "Restore LSTAT from saved OLDJSR value", inline=True)
comment(0x92EE, "Write to protection status", inline=True)
comment(0x92F1, "Return", inline=True)
comment(0x92F2, "Read cursor editing state", inline=True)
comment(0x92F5, "Store to workspace[Y]", inline=True)
comment(0x92F7, "Preserve in X for OSBYTE", inline=True)
comment(0x92F8, "OSBYTE &85: read cursor position", inline=True)
comment(0x92FB, "Advance workspace pointer", inline=True)
comment(0x92FD, "Y result from OSBYTE &85", inline=True)
comment(0x92FE, "Store Y pos to workspace (X=0)", inline=True)
comment(0x9300, "Self-call trick: executes twice", inline=True)
comment(0x9303, "X=0 for (zp,X) addressing", inline=True)
comment(0x9305, "Index into OSBYTE number table", inline=True)
comment(0x9307, "Next table entry next time", inline=True)
comment(0x9309, "Advance workspace pointer", inline=True)
comment(0x930B, "Read OSBYTE number from table", inline=True)
comment(0x930E, "Y=&FF: read current value", inline=True)
comment(0x9310, "Call OSBYTE", inline=True)
comment(0x9313, "Result in X to A", inline=True)
comment(0x9314, "X=0 for indexed indirect store", inline=True)
comment(0x9316, "Store result to workspace", inline=True)
label(0x9319, "vdu_osbyte_table")   # OSBYTE numbers for VDU state save (&85, &C2, &C3)
label(0x931C, "reloc_zp_src")        # ROM source of zero-page relocated code
label(0x935D, "reloc_p4_src")        # ROM source of Tube host page 4 code
label(0x9456, "reloc_p5_src")        # ROM source of Tube host page 5 code
comment(0x966F, "INTOFF: read station ID, disable NMIs", inline=True)
comment(0x9672, "Full ADLC hardware reset", inline=True)
comment(0x9675, "OSBYTE &EA: check Tube co-processor", inline=True)
comment(0x9677, "X=0 for OSBYTE", inline=True)
comment(0x9679, "Clear Econet init flag before setup", inline=True)
comment(0x967C, "Y=&FF for OSBYTE", inline=True)
comment(0x9684, "OSBYTE &8F: issue service request", inline=True)
comment(0x9686, "X=&0C: NMI claim service", inline=True)
comment(0x9688, "Y=&FF: pass to adlc_init_workspace", inline=True)
comment(0x968D, "Copy 32 bytes of NMI shim from ROM to &0D00", inline=True)
label(0x968F, "copy_nmi_shim")        # Copy 32 bytes of NMI shim code from ROM to &0D00
comment(0x968F, "Read byte from NMI shim ROM source", inline=True)
comment(0x9692, "Write to NMI shim RAM at &0D00", inline=True)
comment(0x9695, "Next byte (descending)", inline=True)
comment(0x9696, "Loop until all 32 bytes copied", inline=True)
comment(0x9698, "Patch current ROM bank into NMI shim", inline=True)
comment(0x969A, "Self-modifying code: ROM bank at &0D07", inline=True)
comment(0x969D, "&80 = Econet initialised", inline=True)
comment(0x969F, "Mark TX as complete (ready)", inline=True)
comment(0x96A2, "Mark Econet as initialised", inline=True)
comment(0x96A5, "Read station ID (&FE18 = INTOFF side effect)", inline=True)
comment(0x96A8, "Store our station ID in TX scout", inline=True)
comment(0x96AB, "Y=0 after copy loop: net = local", inline=True)
comment(0x96F1, "Return", inline=True)
label(0x970A, "accept_frame")         # Station ID matched, install next NMI handler
comment(0x970A, "Install next NMI handler at &9711 (RX scout net byte)", inline=True)
label(0x9727, "accept_local_net")     # Network=0: clear broadcast marker
label(0x972A, "accept_scout_net")     # Common accept for local/broadcast frames
comment(0x972C, "Install scout data reading loop at &970E", inline=True)
comment(0x9738, "Neither set -- clean end, discard via &9740", inline=True)
comment(0x9748, "No RDA -- error handler &9733", inline=True)
comment(0x976F, "Write CR1", inline=True)
comment(0x9774, "Write CR2", inline=True)
comment(0x9788, "Write CR1: switch to TX mode", inline=True)
comment(0x9793, "Port = 0 -- immediate operation handler", inline=True)
comment(0x9796, "Check if broadcast (bit6 of tx_flags)", inline=True)
comment(0x9799, "Not broadcast -- skip CR2 setup", inline=True)
comment(0x979B, "CR2=&07: broadcast prep", inline=True)
comment(0x979D, "Write CR2: broadcast frame prep", inline=True)
label(0x97A0, "scan_port_list")        # Non-broadcast: skip CR2 setup, begin port scan
comment(0x97A0, "Check if RX port list active (bit7)", inline=True)
comment(0x97A3, "No active ports -- try NFS workspace", inline=True)
comment(0x97A5, "Start scanning port list at page &C0", inline=True)
label(0x97AD, "check_port_slot")      # Loop: read port control byte, zero=end
comment(0x97AD, "Y=0: read control byte from start of slot", inline=True)
comment(0x97AF, "Read port control byte from slot", inline=True)
comment(0x97B1, "Zero = end of port list, no match", inline=True)
comment(0x97B3, "&7F = any-port wildcard", inline=True)
comment(0x97B5, "Not wildcard -- check specific port match", inline=True)
comment(0x97B8, "Read port number from slot (offset 1)", inline=True)
comment(0x97BA, "Zero port in slot = match any port", inline=True)
comment(0x97BC, "Check if port matches this slot", inline=True)
comment(0x97BF, "Port mismatch -- try next slot", inline=True)
label(0x97C1, "check_station_filter") # Port matched: advance to station filter check
comment(0x97C1, "Y=2: advance to station byte", inline=True)
comment(0x97C2, "Read station filter from slot (offset 2)", inline=True)
comment(0x97C4, "Zero station = match any station, accept", inline=True)
comment(0x97C6, "Check if source station matches", inline=True)
comment(0x97C9, "Station mismatch -- try next slot", inline=True)
comment(0x97CB, "Y=3: advance to network byte", inline=True)
comment(0x97CC, "Read network filter from slot (offset 3)", inline=True)
comment(0x97CE, "Check if source network matches", inline=True)
comment(0x97D1, "Network matches or zero = accept", inline=True)
label(0x97D3, "next_port_slot")        # Mismatch: advance pointer by 12 for next slot
comment(0x97D3, "Check if NFS workspace search pending", inline=True)
comment(0x9801, "Broadcast: different completion path", inline=True)
label(0x9804, "send_data_rx_ack")     # Non-broadcast: set up CR1/CR2 for TX ACK
comment(0x9804, "CR1=&44: RX_RESET | TIE", inline=True)
comment(0x9806, "Write CR1: TX mode for ACK", inline=True)
comment(0x9809, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", inline=True)
comment(0x980B, "Write CR2: enable TX with PSE", inline=True)
comment(0x980E, "Install data_rx_setup at &97DC", inline=True)
comment(0x9810, "High byte of data_rx_setup handler", inline=True)
comment(0x9812, "Send ACK with data_rx_setup as next NMI", inline=True)
comment(0x9817, "Write CR1: switch to RX for data frame", inline=True)
comment(0x981A, "Install nmi_data_rx at &9821", inline=True)
comment(0x981E, "Install nmi_data_rx and return from NMI", inline=True)
comment(0x9821, "A=&01: mask for AP (Address Present)", inline=True)
comment(0x9823, "BIT SR2: test AP bit", inline=True)
comment(0x9826, "No AP: wrong frame or error", inline=True)
comment(0x9828, "Read first byte (dest station)", inline=True)
comment(0x982B, "Compare to our station ID (INTOFF)", inline=True)
comment(0x982E, "Not for us: error path", inline=True)
comment(0x9830, "Install net check handler at &9837", inline=True)
comment(0x9834, "Set NMI vector via RAM shim", inline=True)
comment(0x983A, "SR2 bit7 clear: no data ready -- error", inline=True)
comment(0x983C, "Read dest network byte", inline=True)
comment(0x983F, "Network != 0: wrong network -- error", inline=True)
comment(0x9841, "Install skip handler at &9810", inline=True)
comment(0x9843, "High byte of &9810 handler", inline=True)
comment(0x9845, "SR1 bit7: IRQ, data already waiting", inline=True)
comment(0x9848, "Data ready: skip directly, no RTI", inline=True)
comment(0x984A, "Install handler and return via RTI", inline=True)
comment(0x9850, "SR2 bit7 clear: error", inline=True)
comment(0x9858, "A=2: Tube transfer flag mask", inline=True)
comment(0x985A, "Check if Tube transfer active", inline=True)
comment(0x985D, "Tube active: use Tube RX path", inline=True)
comment(0x985F, "Install bulk read at &9843", inline=True)
comment(0x9861, "High byte of &9843 handler", inline=True)
comment(0x9863, "SR1 bit7: more data already waiting?", inline=True)
comment(0x9866, "Yes: enter bulk read directly", inline=True)
comment(0x9868, "No: install handler and RTI", inline=True)
label(0x986B, "install_tube_rx")      # BNE: Tube active, install Tube RX handler
comment(0x986B, "Tube: install Tube RX at &98DD", inline=True)
comment(0x986D, "High byte of &98DD handler", inline=True)
comment(0x986F, "Install Tube handler and RTI", inline=True)
comment(0x9872, "Check tx_flags for error path", inline=True)
comment(0x9875, "Bit7 clear: RX error path", inline=True)
comment(0x9877, "Bit7 set: TX result = not listening", inline=True)
comment(0x987A, "Full ADLC reset on RX error", inline=True)
comment(0x987D, "Discard and return to idle listen", inline=True)
label(0x9885, "data_rx_loop")          # Loop: check SR2, if RDA continue reading byte pairs
comment(0x9885, "SR2 bit7 clear: frame complete (FV)", inline=True)
comment(0x9887, "Read first byte of pair from RX FIFO", inline=True)
comment(0x988A, "Store byte to buffer", inline=True)
comment(0x988C, "Advance buffer offset", inline=True)
comment(0x988D, "Y != 0: no page boundary crossing", inline=True)
comment(0x988F, "Crossed page: increment buffer high byte", inline=True)
comment(0x9891, "Decrement remaining page count", inline=True)
comment(0x9893, "No pages left: handle as complete", inline=True)
label(0x9895, "read_sr2_between_pairs") # After page boundary, read SR2 before second byte
comment(0x9895, "Read SR2 between byte pairs", inline=True)
comment(0x9898, "SR2 bit7 set: more data available", inline=True)
comment(0x989A, "SR2 non-zero, bit7 clear: frame done", inline=True)
label(0x989C, "read_second_rx_byte")  # BMI: SR2 bit7 set, read second byte from FIFO
comment(0x989C, "Read second byte of pair from RX FIFO", inline=True)
comment(0x989F, "Store byte to buffer", inline=True)
comment(0x98A1, "Advance buffer offset", inline=True)
comment(0x98A2, "Save updated buffer position", inline=True)
comment(0x98A4, "Y != 0: no page boundary crossing", inline=True)
comment(0x98A6, "Crossed page: increment buffer high byte", inline=True)
comment(0x98A8, "Decrement remaining page count", inline=True)
comment(0x98AA, "No pages left: frame complete", inline=True)
label(0x98AC, "check_sr2_loop_again") # After page boundary on second byte, check SR2
comment(0x98AC, "Read SR2 for next iteration", inline=True)
comment(0x98AF, "SR2 non-zero: more data, loop back", inline=True)
comment(0x98B1, "SR2=0: no more data yet, wait for NMI", inline=True)
comment(0x98B6, "Write CR1", inline=True)
comment(0x98BB, "Write CR2", inline=True)
comment(0x98BE, "Save Y (byte count from data RX loop)", inline=True)
comment(0x98C9, "Check if buffer space remains", inline=True)
label(0x98CB, "read_last_rx_byte")    # Multi-source: check buffer then read trailing byte
comment(0x98CB, "No buffer space: error/discard frame", inline=True)
comment(0x98D0, "Y = current buffer write offset", inline=True)
comment(0x98D2, "Store last byte in port receive buffer", inline=True)
comment(0x98D4, "Advance buffer write offset", inline=True)
comment(0x98D6, "No page wrap: proceed to send ACK", inline=True)
comment(0x98D8, "Page boundary: advance buffer page", inline=True)
label(0x98DA, "send_ack")             # No more data: unconditional JMP ack_tx
comment(0x98DA, "Send ACK frame to complete handshake", inline=True)
comment(0x98DD, "Read SR2 for Tube data receive path", inline=True)
label(0x98E0, "rx_tube_data")         # Poll SR2 RDA and forward byte pairs to Tube R3
comment(0x98E0, "RDA clear: no more data, frame complete", inline=True)
comment(0x98E2, "Read data byte from ADLC RX FIFO", inline=True)
comment(0x9916, "Unexpected end: return from NMI", inline=True)
comment(0x9919, "CR1=&00: disable all interrupts", inline=True)
comment(0x991B, "Write CR1 for individual bit testing", inline=True)
comment(0x991E, "CR2=&84: disable PSE", inline=True)
comment(0x9920, "Write CR2: same pattern as main path", inline=True)
comment(0x9923, "A=&02: FV mask for Tube completion", inline=True)
comment(0x9925, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x9928, "No FV: incomplete frame, error", inline=True)
comment(0x992A, "FV set, no RDA: proceed to ACK", inline=True)
comment(0x992C, "Check if any buffer was allocated", inline=True)
comment(0x992E, "OR all 4 buffer pointer bytes together", inline=True)
comment(0x9930, "Check buffer low byte", inline=True)
comment(0x9932, "Check buffer high byte", inline=True)
comment(0x9934, "All zero (null buffer): error", inline=True)
comment(0x9936, "Read extra trailing byte from FIFO", inline=True)
comment(0x9939, "Save extra byte at &0D5D for later use", inline=True)
comment(0x993C, "Bit5 = extra data byte available flag", inline=True)
comment(0x993E, "Set extra byte flag in tx_flags", inline=True)
comment(0x9941, "Store updated flags", inline=True)
comment(0x9944, "Load TX flags to check ACK type", inline=True)
comment(0x9947, "Bit7 clear: normal scout ACK", inline=True)
comment(0x9949, "Final ACK: call completion handler", inline=True)
comment(0x994C, "Jump to TX success result", inline=True)
comment(0x9951, "Write CR1: switch to TX mode", inline=True)
comment(0x9956, "Write CR2: enable TX with status clear", inline=True)
comment(0x995B, "High byte of post-ACK handler", inline=True)
comment(0x995D, "Store next handler low byte", inline=True)
comment(0x9960, "Store next handler high byte", inline=True)
comment(0x9971, "Write dest net byte to FIFO", inline=True)
comment(0x9974, "Install nmi_ack_tx_src at &9925", inline=True)
comment(0x9976, "High byte of nmi_ack_tx_src", inline=True)
comment(0x9978, "Set NMI vector to ack_tx_src handler", inline=True)
comment(0x9992, "Write CR2 to clear status after ACK TX", inline=True)
comment(0x9998, "Load saved next handler high byte", inline=True)
comment(0x999B, "Install next NMI handler", inline=True)
label(0x999E, "start_data_tx")          # Start data TX phase of four-way handshake
comment(0x999E, "Jump to start data TX phase", inline=True)
label(0x99A1, "dispatch_nmi_error")    # JMP nmi_error_dispatch for TX failures
comment(0x99A1, "Jump to error handler", inline=True)
comment(0x99A4, "A=2: test bit1 of tx_flags", inline=True)
comment(0x99A6, "BIT tx_flags: check data transfer bit", inline=True)
comment(0x99A9, "Bit1 clear: no transfer -- return", inline=True)
comment(0x99AB, "CLC: init carry for 4-byte add", inline=True)
comment(0x99AC, "Save carry on stack for loop", inline=True)
comment(0x99AD, "Y=8: RXCB high pointer offset", inline=True)
label(0x99AF, "add_rxcb_ptr")         # 4-byte multi-precision add to RXCB buffer pointer
comment(0x99AF, "Load RXCB[Y] (buffer pointer byte)", inline=True)
comment(0x99B1, "Restore carry from stack", inline=True)
comment(0x99B2, "Add transfer count byte", inline=True)
comment(0x99B5, "Store updated pointer back to RXCB", inline=True)
comment(0x99B7, "Next byte", inline=True)
comment(0x99B8, "Save carry for next iteration", inline=True)
comment(0x99B9, "Done 4 bytes? (Y reaches &0C)", inline=True)
comment(0x99BB, "No: continue adding", inline=True)
comment(0x99BD, "Discard final carry", inline=True)
comment(0x99BE, "A=&20: test bit5 of tx_flags", inline=True)
comment(0x99C0, "BIT tx_flags: check Tube bit", inline=True)
comment(0x99C3, "No Tube: skip Tube update", inline=True)
comment(0x99C5, "Save X on stack", inline=True)
comment(0x99C6, "Push X", inline=True)
comment(0x99C7, "A=8: offset for Tube address", inline=True)
comment(0x99C9, "CLC for address calculation", inline=True)
comment(0x99CA, "Add workspace base offset", inline=True)
comment(0x99CC, "X = address low for Tube claim", inline=True)
comment(0x99CD, "Y = address high for Tube claim", inline=True)
comment(0x99CF, "A=1: Tube claim type (read)", inline=True)
comment(0x99D1, "Claim Tube address for transfer", inline=True)
comment(0x99D4, "Load extra RX data byte", inline=True)
comment(0x99D7, "Send to Tube via R3", inline=True)
label(0x99E5, "skip_tube_update")     # BEQ: Tube flag clear, skip Tube pointer update
comment(0x99E5, "A=&FF: return value (transfer done)", inline=True)
comment(0x99E7, "Return", inline=True)
comment(0x99E8, "Load received port byte", inline=True)
comment(0x99EB, "Port != 0: data transfer frame", inline=True)
comment(0x99ED, "Port=0: load control byte", inline=True)
comment(0x99F0, "Ctrl = &82 (POKE)?", inline=True)
comment(0x99F2, "Yes: POKE also needs data transfer", inline=True)
comment(0x99F4, "Other port-0 ops: immediate dispatch", inline=True)
label(0x99F7, "rx_complete_update_rxcb") # Complete RX and update RXCB
comment(0x99F7, "Update buffer pointer and check for Tube", inline=True)
comment(0x99FA, "Transfer not done: skip buffer update", inline=True)
comment(0x99FC, "Load buffer bytes remaining", inline=True)
comment(0x99FE, "CLC for address add", inline=True)
comment(0x99FF, "Add to buffer base address", inline=True)
comment(0x9A01, "No carry: skip high byte increment", inline=True)
comment(0x9A03, "Carry: increment buffer high byte", inline=True)
label(0x9A05, "store_buf_ptr_lo")     # BCC: no carry, store updated buffer low byte
comment(0x9A05, "Y=8: store updated buffer position", inline=True)
comment(0x9A07, "Store updated low byte to RXCB", inline=True)
comment(0x9A09, "Y=9: buffer high byte offset", inline=True)
comment(0x9A0A, "Load updated buffer high byte", inline=True)
comment(0x9A0C, "Store high byte to RXCB", inline=True)
label(0x9A0E, "skip_buf_ptr_update")  # BNE: transfer not done, skip buffer ptr write
comment(0x9A0E, "Check port byte again", inline=True)
comment(0x9A11, "Port=0: immediate op, discard+listen", inline=True)
comment(0x9A13, "Load source network from scout buffer", inline=True)
comment(0x9A16, "Y=3: RXCB source network offset", inline=True)
comment(0x9A18, "Store source network to RXCB", inline=True)
comment(0x9A1A, "Y=2: source station offset", inline=True)
comment(0x9A1B, "Load source station from scout buffer", inline=True)
comment(0x9A1E, "Store source station to RXCB", inline=True)
comment(0x9A20, "Y=1: port byte offset", inline=True)
comment(0x9A21, "Load port byte", inline=True)
comment(0x9A24, "Store port to RXCB", inline=True)
comment(0x9A26, "Y=0: control/flag byte offset", inline=True)
comment(0x9A27, "Load control byte from scout", inline=True)
comment(0x9A2A, "Set bit7 = reception complete flag", inline=True)
comment(0x9A2C, "Store to RXCB (marks CB as complete)", inline=True)
comment(0x9A2E, "Tube flag bit 1 AND tx_flags bit 1", inline=True)
comment(0x9A36, "No Tube transfer active -- skip release", inline=True)
comment(0x9A3A, "Release Tube claim before discarding", inline=True)
comment(0x9A3D, "Re-enter idle RX listen mode", inline=True)
comment(0x9A40, "Install nmi_rx_scout (&96F2) as NMI handler", inline=True)
comment(0x9A42, "High byte of nmi_rx_scout", inline=True)
comment(0x9A44, "Set NMI vector and return", inline=True)
comment(0x9A56, "Control byte &81-&88 range check", inline=True)
comment(0x9A59, "Below &81: not an immediate op", inline=True)
comment(0x9A5B, "Out of range low: jump to discard", inline=True)
comment(0x9A5D, "Above &88: not an immediate op", inline=True)
comment(0x9A5F, "Out of range high: jump to discard", inline=True)
comment(0x9A61, "HALT(&87)/CONTINUE(&88) skip protection", inline=True)
comment(0x9A63, "Ctrl >= &87: dispatch without mask check", inline=True)
comment(0x9A65, "Convert ctrl byte to 0-based index for mask", inline=True)
comment(0x9A66, "SEC for subtract", inline=True)
comment(0x9A67, "A = ctrl - &81 (0-based operation index)", inline=True)
comment(0x9A69, "Y = index for mask rotation count", inline=True)
comment(0x9A6A, "Load protection mask from LSTAT", inline=True)
label(0x9A6D, "rotate_prot_mask")      # Rotate protection mask right to align permission bit
comment(0x9A6D, "Rotate mask right by control byte index", inline=True)
comment(0x9A6E, "Decrement rotation counter", inline=True)
comment(0x9A6F, "Loop until bit aligned", inline=True)
comment(0x9AFC, "Get buffer position for reply header", inline=True)
comment(0x9AFE, "Clear carry for offset addition", inline=True)
comment(0x9AFF, "Data offset = buf_len + &80 (past header)", inline=True)
comment(0x9B01, "Y=&7F: reply data length slot", inline=True)
comment(0x9B03, "Store reply data length in RX buffer", inline=True)
comment(0x9B05, "Y=&80: source station slot", inline=True)
comment(0x9B07, "Load requesting station number", inline=True)
comment(0x9B0A, "Store source station in reply header", inline=True)
comment(0x9B0D, "Load requesting network number", inline=True)
comment(0x9B10, "Store source network in reply header", inline=True)
comment(0x9B12, "Load control byte from received frame", inline=True)
comment(0x9B15, "Save ctrl byte for TX response", inline=True)
comment(0x9B18, "IER bit 2: disable SR interrupt", inline=True)
comment(0x9B1A, "Write IER to disable SR", inline=True)
comment(0x9B1D, "Read ACR for shift register config", inline=True)
comment(0x9B20, "Isolate shift register mode bits (2-4)", inline=True)
comment(0x9B22, "Save original SR mode for later restore", inline=True)
comment(0x9B25, "Reload ACR for modification", inline=True)
comment(0x9B28, "Clear SR mode bits (keep other bits)", inline=True)
comment(0x9B2A, "SR mode 2: shift in under φ2", inline=True)
comment(0x9B2C, "Apply new shift register mode", inline=True)
comment(0x9B2F, "Read SR to clear pending interrupt", inline=True)
comment(0x9B32, "Return to idle listen mode", inline=True)
comment(0x9BC7, "Save X on stack", inline=True)
comment(0x9BC8, "Push X", inline=True)
comment(0x9BC9, "Y=2: TXCB offset for dest station", inline=True)
comment(0x9BCB, "Load dest station from TX control block", inline=True)
comment(0x9BCD, "Store to TX scout buffer", inline=True)
comment(0x9BD1, "Load dest network from TX control block", inline=True)
comment(0x9BD3, "Store to TX scout buffer", inline=True)
comment(0x9BD6, "Y=0: first byte of TX control block", inline=True)
comment(0x9BD8, "Load control/flag byte", inline=True)
comment(0x9BDA, "Bit7 set: immediate operation ctrl byte", inline=True)
comment(0x9BDC, "Bit7 clear: normal data transfer", inline=True)
label(0x9BDF, "tx_imm_op_setup")       # BMI: TXCB bit7 set, store ctrl byte for imm op
comment(0x9BDF, "Store control byte to TX scout buffer", inline=True)
comment(0x9BE2, "X = control byte for range checks", inline=True)
comment(0x9BE3, "Y=1: port byte offset", inline=True)
comment(0x9BE4, "Load port byte from TX control block", inline=True)
comment(0x9BE6, "Store port byte to TX scout buffer", inline=True)
comment(0x9BE9, "Port != 0: skip immediate op setup", inline=True)
comment(0x9BEB, "Ctrl < &83: PEEK/POKE need address calc", inline=True)
comment(0x9BED, "Ctrl >= &83: skip to range check", inline=True)
comment(0x9BEF, "SEC: init borrow for 4-byte subtract", inline=True)
comment(0x9BF0, "Save carry on stack for loop", inline=True)
comment(0x9BF1, "Y=8: high pointer offset in TXCB", inline=True)
label(0x9BF3, "calc_peek_poke_size")   # 4-byte subtraction for PEEK/POKE transfer size
comment(0x9BF3, "Load TXCB[Y] (end addr byte)", inline=True)
comment(0x9BF5, "Y -= 4: back to start addr offset", inline=True)
comment(0x9BF9, "Restore borrow from stack", inline=True)
comment(0x9BFA, "end - start = transfer size byte", inline=True)
comment(0x9BFC, "Store result to tx_data_start", inline=True)
comment(0x9C04, "Save borrow for next byte", inline=True)
comment(0x9C05, "Done all 4 bytes? (Y reaches &0C)", inline=True)
comment(0x9C07, "No: next byte pair", inline=True)
comment(0x9C09, "Discard final borrow", inline=True)
label(0x9C0A, "tx_ctrl_range_check")  # BCS: ctrl >= &83, validate &81-&88 range
comment(0x9C0A, "Ctrl < &81: not an immediate op", inline=True)
comment(0x9C0C, "Below range: normal data transfer", inline=True)
comment(0x9C0E, "Ctrl >= &89: out of immediate range", inline=True)
comment(0x9C10, "Above range: normal data transfer", inline=True)
comment(0x9C12, "Y=&0C: start of extra data in TXCB", inline=True)
label(0x9C14, "copy_imm_params")      # Copy 4 extra parameter bytes from TXCB to NMI workspace
comment(0x9C14, "Load extra parameter byte from TXCB", inline=True)
comment(0x9C16, "Copy to NMI shim workspace at &0D1A+Y", inline=True)
comment(0x9C19, "Next byte", inline=True)
comment(0x9C1A, "Done 4 bytes? (Y reaches &10)", inline=True)
comment(0x9C1C, "No: continue copying", inline=True)
label(0x9C1E, "tx_line_idle_check")   # BNE: port != 0, test SR2 INACTIVE before polling
comment(0x9C1E, "A=&20: mask for SR2 INACTIVE bit", inline=True)
comment(0x9C20, "BIT SR2: test if line is idle", inline=True)
comment(0x9C23, "Line not idle: handle as line jammed", inline=True)
comment(0x9C25, "A=&FD: high byte of timeout counter", inline=True)
comment(0x9C27, "Push timeout high byte to stack", inline=True)
comment(0x9C28, "Scout frame = 6 address+ctrl bytes", inline=True)
comment(0x9C2A, "Store scout frame length", inline=True)
comment(0x9C2D, "A=0: init low byte of timeout counter", inline=True)
label(0x9C36, "test_inactive_retry")   # Reload INACTIVE mask and retry polling
label(0x9C54, "inactive_retry")       # BEQ: INACTIVE not set, re-enable NMIs/retry
comment(0x9C71, "Write CR2 to abort TX", inline=True)
comment(0x9C74, "Clean 3 bytes of timeout loop state", inline=True)
comment(0x9C79, "ALWAYS branch to shared error handler", inline=True)
label(0x9C7B, "tx_no_clock_error")   # Error code &43: "No Clock"
comment(0x9C7B, "Error &43 = 'No Clock'", inline=True)
label(0x9C7D, "store_tx_error")      # Store error code to TX control block
comment(0x9C7D, "Offset 0 = error byte in TX control block", inline=True)
comment(0x9C7F, "Store error code in TX CB byte 0", inline=True)
comment(0x9C81, "&80 = TX complete flag", inline=True)
comment(0x9C83, "Signal TX operation complete", inline=True)
comment(0x9C86, "Restore X saved by caller", inline=True)
comment(0x9C87, "Move to X register", inline=True)
comment(0x9C88, "Return to TX caller", inline=True)
comment(0x9C8E, "Write to ADLC CR1", inline=True)
comment(0x9C91, "Install NMI handler at &9D2D (nmi_tx_data)", inline=True)
comment(0x9C93, "High byte of NMI handler address", inline=True)
comment(0x9C95, "Write NMI vector low byte directly", inline=True)
comment(0x9C98, "Write NMI vector high byte directly", inline=True)
comment(0x9C9E, "Load destination port number", inline=True)
comment(0x9CA1, "Port != 0: standard data transfer", inline=True)
comment(0x9CA3, "Port 0: load control byte for table lookup", inline=True)
comment(0x9CA6, "Look up tx_flags from table", inline=True)
comment(0x9CA9, "Store operation flags", inline=True)
comment(0x9CAC, "Look up tx_length from table", inline=True)
comment(0x9CAF, "Store expected transfer length", inline=True)
label(0x9CEF, "setup_data_xfer")       # Configure scout length and flags for data transfer
comment(0x9CEF, "Load dest station for broadcast check", inline=True)
comment(0x9CF2, "AND with dest network", inline=True)
comment(0x9CF5, "Both &FF = broadcast address?", inline=True)
comment(0x9CF7, "Not broadcast: unicast path", inline=True)
comment(0x9CF9, "Broadcast scout: 14 bytes total", inline=True)
comment(0x9CFB, "Store broadcast scout length", inline=True)
comment(0x9CFE, "A=&40: broadcast flag", inline=True)
comment(0x9D00, "Set broadcast flag in tx_flags", inline=True)
comment(0x9D03, "Y=4: start of address data in TXCB", inline=True)
label(0x9D05, "copy_bcast_addr")      # Copy 8-byte broadcast address data into TX scout buffer
comment(0x9D05, "Copy TXCB address bytes to scout buffer", inline=True)
comment(0x9D07, "Store to TX source/data area", inline=True)
comment(0x9D0A, "Next byte", inline=True)
comment(0x9D0B, "Done 8 bytes? (Y reaches &0C)", inline=True)
comment(0x9D0D, "No: continue copying", inline=True)
label(0x9D11, "setup_unicast_xfer")   # BNE: not broadcast, clear flags/scout_status=2
comment(0x9D11, "A=0: clear flags for unicast", inline=True)
comment(0x9D13, "Clear tx_flags", inline=True)
comment(0x9D16, "scout_status=2: data transfer pending", inline=True)
comment(0x9D18, "Store scout status", inline=True)
comment(0x9D1B, "Copy TX block pointer to workspace ptr", inline=True)
comment(0x9D1D, "Store low byte", inline=True)
comment(0x9D1F, "Copy TX block pointer high byte", inline=True)
comment(0x9D21, "Store high byte", inline=True)
comment(0x9D23, "Calculate transfer size from RXCB", inline=True)
comment(0x9D26, "Restore processor status from stack", inline=True)
comment(0x9D27, "Restore stacked registers (4 PLAs)", inline=True)
comment(0x9D28, "Second PLA", inline=True)
comment(0x9D29, "Third PLA", inline=True)
comment(0x9D2A, "Fourth PLA", inline=True)
comment(0x9D2B, "Restore X from A", inline=True)
comment(0x9D2C, "Return to caller", inline=True)
label(0x9D33, "tx_fifo_write")        # NMI TX loop: write 2 bytes per iteration to ADLC FIFO
label(0x9D57, "tx_fifo_not_ready")    # BVC: TDRA clear, write CR2=&67, error &41
label(0x9D5E, "tx_store_error")       # BNE: error &42 path, merge with &9CF6
label(0x9D61, "delay_nmi_disable")    # PHA/PLA delay loop after INTOFF before storing TX result
comment(0x9D6B, "Write to ADLC CR2", inline=True)
comment(0x9D6E, "Install NMI handler at &9D75 (nmi_tx_complete)", inline=True)
comment(0x9D70, "High byte of handler address", inline=True)
comment(0x9D72, "Install and return via set_nmi_vector", inline=True)
label(0x9D82, "check_handshake_bit")  # BVC: tx_flags bit6 clear, check bit0
label(0x9D8C, "install_reply_scout")  # BEQ: handshake bit0 clear, install nmi_reply_scout
comment(0x9D8C, "Install nmi_reply_scout at &9D30", inline=True)
comment(0x9D9A, "Read first RX byte (destination station)", inline=True)
comment(0x9DA2, "Install nmi_reply_cont at &9DA9", inline=True)
comment(0x9DB3, "Install nmi_reply_validate at &9DC2", inline=True)
comment(0x9DBA, "IRQ set -- fall through to &9DC2 without RTI", inline=True)
label(0x9DBF, "reject_reply")          # Reject invalid reply scout frame
comment(0x9DE0, "Write CR2: enable RTS for TX handshake", inline=True)
comment(0x9DE5, "Write CR1: reset RX, enable TX interrupt", inline=True)
comment(0x9DEA, "High byte &9E of next handler address", inline=True)
comment(0x9DEC, "Store low byte to nmi_next_lo", inline=True)
comment(0x9DEF, "Store high byte to nmi_next_hi", inline=True)
comment(0x9DFD, "Load dest network for scout ACK TX", inline=True)
comment(0x9E00, "Write dest network to TX FIFO", inline=True)
comment(0x9E03, "Install nmi_scout_ack_src at &9E0A", inline=True)
comment(0x9E05, "High byte &9D of handler address", inline=True)
comment(0x9E07, "Set NMI vector and return", inline=True)
comment(0x9E0A, "Read our station ID (also INTOFF)", inline=True)
comment(0x9E0D, "BIT SR1: check TDRA before writing", inline=True)
comment(0x9E10, "TDRA not ready: TX error", inline=True)
comment(0x9E15, "Network = 0 (local network)", inline=True)
comment(0x9E17, "Write network byte to TX FIFO", inline=True)
comment(0x9E1A, "Test bit 1 of tx_flags", inline=True)
comment(0x9E1C, "Check if immediate-op or data-transfer", inline=True)
comment(0x9E1F, "Bit 1 set: immediate op, use alt handler", inline=True)
comment(0x9E21, "Install nmi_data_tx at &9E2F", inline=True)
comment(0x9E23, "High byte of handler address", inline=True)
comment(0x9E25, "Install and return via set_nmi_vector", inline=True)
label(0x9E28, "install_imm_data_nmi")  # BNE: tx_flags bit1 set, install nmi_imm_data
comment(0x9E28, "Install nmi_data_tx_tube at &9E81", inline=True)
comment(0x9E2A, "High byte of handler address", inline=True)
comment(0x9E2C, "Install and return via set_nmi_vector", inline=True)
label(0x9E34, "data_tx_check_fifo")   # Test TDRA and write data byte pair to FIFO
comment(0x9E38, "Write first byte of pair to FIFO", inline=True)
comment(0x9E3B, "Advance buffer offset", inline=True)
comment(0x9E3C, "No page crossing", inline=True)
comment(0x9E3E, "Page crossing: decrement page count", inline=True)
comment(0x9E40, "No pages left: send last data", inline=True)
comment(0x9E42, "Increment buffer high byte", inline=True)
label(0x9E44, "write_second_tx_byte") # BNE: skip page check, write second FIFO byte
comment(0x9E44, "Load second byte of pair", inline=True)
comment(0x9E46, "Write second byte to FIFO", inline=True)
comment(0x9E49, "Advance buffer offset", inline=True)
comment(0x9E4A, "Save updated buffer position", inline=True)
comment(0x9E4C, "No page crossing", inline=True)
comment(0x9E4E, "Page crossing: decrement page count", inline=True)
comment(0x9E50, "No pages left: send last data", inline=True)
comment(0x9E52, "Increment buffer high byte", inline=True)
label(0x9E54, "check_irq_loop")       # BNE: skip page check, test SR1 IRQ for loop
comment(0x9E54, "BIT SR1: test IRQ (N=bit7) for tight loop", inline=True)
comment(0x9E57, "IRQ still set: write 2 more bytes", inline=True)
comment(0x9E59, "No IRQ: return, wait for next NMI", inline=True)
comment(0x9E5E, "Write CR2 to close frame", inline=True)
comment(0x9E61, "Check tx_flags for next action", inline=True)
comment(0x9E64, "Bit7 clear: error, install saved handler", inline=True)
comment(0x9E66, "Install discard_reset_listen at &99DB", inline=True)
comment(0x9E68, "High byte of &99DB handler", inline=True)
comment(0x9E6A, "Set NMI vector and return", inline=True)
comment(0x9E6D, "Load saved next handler low byte", inline=True)
comment(0x9E7B, "Load saved next handler high byte", inline=True)
comment(0x9E7E, "Install saved handler and return", inline=True)
comment(0x9E81, "Tube TX: BIT SR1 test TDRA", inline=True)
label(0x9E84, "tube_tx_fifo_write")    # BMI: IRQ set, Tube TX FIFO write entry point
comment(0x9E84, "TDRA not ready -- error", inline=True)
comment(0x9E86, "Read byte from Tube R3", inline=True)
comment(0x9E89, "Write to TX FIFO", inline=True)
comment(0x9E8C, "Increment 4-byte buffer counter", inline=True)
comment(0x9E8E, "Low byte didn't wrap", inline=True)
comment(0x9E90, "Carry into second byte", inline=True)
comment(0x9E92, "No further carry", inline=True)
comment(0x9E94, "Carry into third byte", inline=True)
comment(0x9E96, "No further carry", inline=True)
comment(0x9E98, "Carry into fourth byte", inline=True)
comment(0x9E9A, "Counter wrapped to zero: last data", inline=True)
label(0x9E9C, "write_second_tube_byte") # BNE: skip carry, read/write second Tube byte
comment(0x9E9C, "Read second Tube byte from R3", inline=True)
comment(0x9E9F, "Write second byte to TX FIFO", inline=True)
comment(0x9EA2, "Increment 4-byte counter (second byte)", inline=True)
comment(0x9EA4, "Low byte didn't wrap", inline=True)
comment(0x9EA6, "Carry into second byte", inline=True)
comment(0x9EA8, "No further carry", inline=True)
label(0x9EAA, "tube_tx_inc_byte3")    # Tube TX buffer counter byte 3 increment
comment(0x9EAA, "Carry into third byte", inline=True)
comment(0x9EAC, "No further carry", inline=True)
comment(0x9EAE, "Carry into fourth byte", inline=True)
comment(0x9EB0, "Counter wrapped to zero: last data", inline=True)
label(0x9EB2, "check_tube_irq_loop")  # BNE: skip carry, test SR1 IRQ for loop
comment(0x9EB2, "BIT SR1: test IRQ for tight loop", inline=True)
comment(0x9EB5, "IRQ still set: write 2 more bytes", inline=True)
comment(0x9EB7, "No IRQ: return, wait for next NMI", inline=True)
comment(0x9EBC, "Write to ADLC CR1", inline=True)
comment(0x9EBF, "Install nmi_final_ack at &9E5C", inline=True)
comment(0x9EC1, "High byte of handler address", inline=True)
comment(0x9EC3, "Install and return via set_nmi_vector", inline=True)
comment(0x9ED5, "Install nmi_final_ack_net at &9E70", inline=True)
comment(0x9EE6, "Install nmi_final_ack_validate at &9E84", inline=True)
comment(0x9EED, "IRQ set -- fall through to &9E84 without RTI", inline=True)
label(0x9F0F, "check_fv_final_ack")    # BPL: tx_flags bit7 clear, test FV for frame end
subroutine(0x9F1A, "tx_result_fail", hook=None,
    title="TX failure: not listening",
    description="""\
Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")
comment(0x9F1A, "A=&41: not listening error code", inline=True)
label(0x9F54, "calc_transfer_size")    # 4-byte subtraction to calculate actual bytes received
label(0x9F81, "restore_x_and_return") # BCC: Tube not claimed, restore X/RTS
label(0x9F84, "fallback_calc_transfer") # BEQ: no buffer/Tube, simple 2-byte subtract
comment(0x9F84, "Y=4: RXCB current pointer offset", inline=True)
comment(0x9F88, "Y=8: RXCB start address offset", inline=True)
comment(0x9F8A, "Set carry for subtraction", inline=True)
comment(0x9F8F, "Y=5: current ptr hi offset", inline=True)
comment(0x9F93, "Propagate borrow from lo subtraction", inline=True)
comment(0x9F95, "Temp store adjusted current ptr hi", inline=True)
comment(0x9F97, "Y=8: start address lo offset", inline=True)
comment(0x9F9B, "Store to scratch (side effect)", inline=True)
comment(0x9F9D, "Y=9: start address hi offset", inline=True)
comment(0x9F9F, "Load RXCB[9] (start ptr hi)", inline=True)
comment(0x9FA1, "Set carry for subtraction", inline=True)
comment(0x9FA2, "start_hi - adjusted current_hi", inline=True)
comment(0x9FA8, "INTOFF: disable NMIs while switching ROM", inline=True)
comment(0x9FAB, "Save A", inline=True)
comment(0x9FAC, "Transfer Y to A", inline=True)
comment(0x9FAD, "Save Y (via A)", inline=True)
comment(0x9FAE, "ROM bank 0 (patched during init for actual bank)", inline=True)
comment(0x9FB0, "Select Econet ROM bank via ROMSEL", inline=True)
comment(0x9FB3, "Jump to scout handler in ROM", inline=True)
comment(0x9FB6, "Store handler high byte at &0D0D", inline=True)
comment(0x9FB9, "Store handler low byte at &0D0C", inline=True)
comment(0x9FBC, "Restore NFS ROM bank", inline=True)
comment(0x9FBE, "Page in via hardware latch", inline=True)
comment(0x9FC1, "Restore Y from stack", inline=True)
comment(0x9FC3, "Restore A from stack", inline=True)
comment(0x9FC4, "INTON: re-enable NMIs", inline=True)
comment(0x9FC7, "Return from interrupt", inline=True)
comment(0x9FE0, "Save original byte for low nibble", inline=True)
comment(0x9FE1, "Shift high nibble right (4x LSR)", inline=True)
comment(0x9FE5, "Print high nibble as hex", inline=True)
comment(0x9FE8, "Restore byte; fall through for low nibble", inline=True)
comment(0x9FE9, "Mask to low nibble (0-F)", inline=True)
comment(0x9FEB, "Digit A-F?", inline=True)
comment(0x9FED, "No: skip letter offset", inline=True)
comment(0x9FEF, "A-F: ADC #6 + ADC #&30 + C = &41-&46", inline=True)
label(0x9FF1, "add_ascii_base")        # BCC: nibble 0-9, ADC #&30 converts to ASCII
comment(0x9FF1, "Add ASCII '0' base (with carry)", inline=True)
comment(0x9FF3, "Write character", inline=True)
comment(0x9FF6, "C=1: callers use SEC as sentinel", inline=True)
comment(0x9FF7, "Return", inline=True)

# ============================================================
# Inline comments: gap-filling for 3.40-specific code
# ============================================================
# These instructions were not mapped from 3.60 (either in
# opcode-change blocks or version-specific subroutines).

# service_handler: ADLC detection probe (&80F7-&8118)
comment(0x80F8, "(bus settling continued)", inline=True)
comment(0x80F9, "(bus settling continued)", inline=True)
comment(0x80FA, "(bus settling continued)", inline=True)
comment(0x80FB, "(bus settling continued)", inline=True)
comment(0x80FC, "(bus settling continued)", inline=True)
comment(0x80FD, "(bus settling continued)", inline=True)
comment(0x80FE, "(bus settling continued)", inline=True)
comment(0x80FF, "(bus settling continued)", inline=True)
comment(0x8101, "Load workspace byte for this ROM slot", inline=True)
comment(0x8104, "Push detection flag", inline=True)
comment(0x8105, "Non-zero: ROM already detected, skip probe", inline=True)
comment(0x8107, "First call: mark ROM as present", inline=True)
comment(0x810A, "Read station ID (INTOFF side effect)", inline=True)
comment(0x810D, "Zero: no ADLC hardware, skip", inline=True)
comment(0x810F, "Second read: bus stability check", inline=True)
comment(0x8112, "Same value: ADLC present, continue", inline=True)
comment(0x8114, "C=1: prepare to set disable flag", inline=True)
comment(0x8115, "Bit 7 into workspace: disable this ROM", inline=True)
comment(0x8118, "Restore detection flag", inline=True)

# run_fscv_cmd (&8289)
comment(0x8289, "Y=&82: ROM page high byte", inline=True)
comment(0x828B, "Execute command string at (X, Y)", inline=True)

# save_fscv_args_with_ptrs (&85C8)
comment(0x85C8, "X to os_text_ptr (text ptr lo)", inline=True)
comment(0x85CA, "Y to os_text_ptr hi", inline=True)
comment(0x85CC, "X to FS command ptr lo", inline=True)
comment(0x85CF, "Y to FS command ptr hi", inline=True)

# save_fscv_args (&85D2)
comment(0x85D2, "A = function code / command", inline=True)
comment(0x85D4, "X = control block ptr lo", inline=True)
comment(0x85D6, "Y = control block ptr hi", inline=True)
comment(0x85D8, "X dup for indexed access via (fs_crc)", inline=True)
comment(0x85DA, "Y dup for indexed access", inline=True)
comment(0x85DC, "Return", inline=True)

# setup_tx_ptr_c0 (&8687)
comment(0x8687, "X=&C0: TX control block at &00C0", inline=True)
comment(0x8689, "Set TX pointer lo", inline=True)
comment(0x868B, "X=0: page zero", inline=True)
comment(0x868D, "Set TX pointer hi", inline=True)

# tx_poll_core (&8693)
comment(0x8693, "Save retry count on stack", inline=True)
comment(0x8694, "Transfer timeout to A", inline=True)
comment(0x8695, "Save timeout on stack", inline=True)
comment(0x8696, "X=0 for (net_tx_ptr,X) indirect", inline=True)
comment(0x8698, "Load TXCB byte 0 (control/status)", inline=True)
comment(0x869A, "Write control byte to start TX", inline=True)
comment(0x869C, "Save control byte for retry", inline=True)
comment(0x869D, "Test TX semaphore (C=1 when free)", inline=True)
comment(0x86A0, "Spin until semaphore released", inline=True)
comment(0x86A2, "Copy TX ptr lo to NMI block", inline=True)
comment(0x86A4, "Store for NMI handler access", inline=True)
comment(0x86A6, "Copy TX ptr hi to NMI block", inline=True)
comment(0x86A8, "Store for NMI handler access", inline=True)
comment(0x86AA, "Initiate ADLC TX via trampoline", inline=True)
comment(0x86AD, "Poll TXCB byte 0 for completion", inline=True)
comment(0x86AF, "Bit 7 set: still busy, keep polling", inline=True)
comment(0x86B1, "Shift bit 6 into bit 7 (error flag)", inline=True)
comment(0x86B2, "Bit 6 clear: success, clean return", inline=True)
comment(0x86B4, "Shift bit 5 into carry", inline=True)
comment(0x86B5, "Zero: fatal error, no escape", inline=True)
comment(0x86B7, "Check for user escape condition", inline=True)
comment(0x86BA, "Discard saved control byte", inline=True)
comment(0x86BB, "Save to X for retry delay", inline=True)
comment(0x86BC, "Restore timeout parameter", inline=True)
comment(0x86BD, "Back to Y", inline=True)
comment(0x86BE, "Restore retry count", inline=True)
comment(0x86BF, "No retries left: report error", inline=True)
comment(0x86C1, "Decrement retry count", inline=True)
comment(0x86C3, "Save updated retry count", inline=True)
comment(0x86C4, "Timeout to A for delay", inline=True)
comment(0x86C5, "Save timeout parameter", inline=True)
comment(0x86C6, "Control byte for delay duration", inline=True)
comment(0x86C7, "Inner delay loop", inline=True)
comment(0x86C8, "Spin until X=0", inline=True)
comment(0x86CA, "Outer delay loop", inline=True)
comment(0x86CB, "Continue delay", inline=True)
comment(0x86CF, "Save error code in X", inline=True)
comment(0x86D0, "Report 'Not listening' error", inline=True)
comment(0x86D3, "Discard saved control byte", inline=True)
comment(0x86D4, "Discard timeout parameter", inline=True)
comment(0x86D5, "Discard retry count", inline=True)
comment(0x86D6, "Return (success)", inline=True)

# boot_option_offsets (&8D1B): data bytes misclassified as code
comment(0x8D21, "Data byte: boot_cmd_strings 'x'", inline=True)
comment(0x8D22, "Data bytes: boot_cmd_strings 'ec'", inline=True)

# print_file_info (&8D24)
comment(0x8D24, "Check if messages enabled", inline=True)
comment(0x8D27, "Zero: no info to display, return", inline=True)
comment(0x8D29, "Y=0: start of filename", inline=True)
comment(0x8D2B, "Load current directory prefix flag", inline=True)
comment(0x8D2E, "No prefix: skip directory display", inline=True)
comment(0x8D30, "Print directory name prefix", inline=True)
comment(0x8D33, "N=1: skip to hex fields after dir", inline=True)
comment(0x8D35, "Load next filename character", inline=True)
comment(0x8D37, "CR: end of filename", inline=True)
comment(0x8D39, "CR found: pad remaining with spaces", inline=True)
comment(0x8D3B, "Space: end of name field", inline=True)
comment(0x8D3D, "Space found: pad with spaces", inline=True)
comment(0x8D42, "Advance to next character", inline=True)
comment(0x8D43, "Continue printing filename", inline=True)
comment(0x8D45, "Print space for padding", inline=True)
comment(0x8D48, "Advance column counter", inline=True)
comment(0x8D49, "Reached 12 columns?", inline=True)
comment(0x8D4B, "No: continue padding", inline=True)
comment(0x8D4D, "Y=5: load address offset (4 bytes)", inline=True)
comment(0x8D4F, "Print load address", inline=True)
comment(0x8D52, "Print exec address and file length", inline=True)
comment(0x8D58, "Y=9: exec address offset (4 bytes)", inline=True)
comment(0x8D5A, "Print exec address", inline=True)
comment(0x8D5D, "Y=&0C: file length offset", inline=True)
comment(0x8D5F, "X=3: print 3 bytes (24-bit length)", inline=True)

# net_3_close_handle (&8E6F)
comment(0x8E74, "Save carry via rotate", inline=True)
comment(0x8E77, "A=&3F: handle closed/unused marker", inline=True)
comment(0x8E79, "Write marker to handle slot", inline=True)
comment(0x8E7B, "Restore carry from rotate", inline=True)

# save_econet_state (&96C8)
comment(0x96C8, "INTOFF: disable NMIs", inline=True)
comment(0x96CB, "A=0: clear TX and init flags", inline=True)
comment(0x96CD, "Clear TX semaphore (allow new TX)", inline=True)
comment(0x96D0, "Clear Econet init flag", inline=True)
comment(0x96D3, "Y=5: status flags offset", inline=True)
comment(0x96D5, "Re-enter idle RX listen mode", inline=True)

# adlc_full_reset (&96D8)
comment(0x96DA, "Write CR1: full reset", inline=True)
comment(0x96DD, "CR4=&1E: 8-bit word, abort ext, NRZ", inline=True)
comment(0x96DF, "Write CR4 via ADLC reg 3 (AC=1)", inline=True)
comment(0x96E4, "Write CR3=0: clear loop-back/AEX/DTR", inline=True)

# discard_listen gap: c9a47 scout field copy
comment(0x9A47, "Y=4: start at RX CB offset 4", inline=True)
comment(0x9A49, "Load scout field (stn/net/ctrl/port)", inline=True)
comment(0x9A4C, "Store to port workspace buffer", inline=True)
comment(0x9A4F, "All 8 fields copied?", inline=True)
comment(0x9A51, "No: continue copy loop", inline=True)

# rx_imm_exec (&9A95): JSR/UserProc/OSProc setup
comment(0x9A95, "Buffer start lo = &00", inline=True)
comment(0x9A97, "Set port buffer lo", inline=True)
comment(0x9A99, "Buffer length lo = &82", inline=True)
comment(0x9A9B, "Set buffer length lo", inline=True)
comment(0x9A9D, "Buffer length hi = 1", inline=True)
comment(0x9A9F, "Set buffer length hi", inline=True)
comment(0x9AA1, "Load RX page hi for buffer", inline=True)
comment(0x9AA3, "Set port buffer hi", inline=True)
comment(0x9AA5, "Y=3: copy 4 bytes (3 down to 0)", inline=True)
comment(0x9AA7, "Load remote address byte", inline=True)
comment(0x9AAA, "Store to exec address workspace", inline=True)
comment(0x9AAD, "Next byte (descending)", inline=True)
comment(0x9AAE, "Loop until all 4 bytes copied", inline=True)
comment(0x9AB0, "Enter common data-receive path", inline=True)

# rx_imm_poke (&9AB3)
comment(0x9AB3, "Port workspace offset = &3D", inline=True)
comment(0x9AB5, "Store workspace offset lo", inline=True)
comment(0x9AB7, "RX buffer page = &0D", inline=True)
comment(0x9AB9, "Store workspace offset hi", inline=True)
comment(0x9ABB, "Enter POKE data-receive path", inline=True)

# rx_imm_machine_type (&9ABE)
comment(0x9ABE, "Buffer length hi = 1", inline=True)
comment(0x9AC0, "Set buffer length hi", inline=True)
comment(0x9AC2, "Buffer length lo = &FC", inline=True)
comment(0x9AC4, "Set buffer length lo", inline=True)
comment(0x9AC6, "Buffer start lo = &25", inline=True)
comment(0x9AC8, "Set port buffer lo", inline=True)
comment(0x9ACA, "Buffer hi = &7F (below screen)", inline=True)
comment(0x9ACC, "Set port buffer hi", inline=True)
comment(0x9ACE, "Enter reply build path", inline=True)

# rx_imm_peek (&9AD1)
comment(0x9AD1, "Port workspace offset = &3D", inline=True)
comment(0x9AD3, "Store workspace offset lo", inline=True)
comment(0x9AD5, "RX buffer page = &0D", inline=True)
comment(0x9AD7, "Store workspace offset hi", inline=True)
comment(0x9AD9, "Scout status = 2 (PEEK response)", inline=True)
comment(0x9ADB, "Store scout status", inline=True)
comment(0x9ADE, "Calculate transfer size for response", inline=True)
comment(0x9AE1, "C=0: transfer not set up, discard", inline=True)
comment(0x9AE3, "Mark TX flags bit 7 (reply pending)", inline=True)
comment(0x9AE6, "Set reply pending flag", inline=True)
comment(0x9AE8, "Store updated TX flags", inline=True)
comment(0x9AEB, "CR1=&44: TIE | TX_LAST_DATA", inline=True)
comment(0x9AED, "Write CR1: enable TX interrupts", inline=True)
comment(0x9AF0, "CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE", inline=True)
comment(0x9AF2, "Write CR2 for TX setup", inline=True)
comment(0x9AF5, "NMI handler lo byte (self-modifying)", inline=True)
comment(0x9AF7, "Y=&9B: dispatch table page", inline=True)
comment(0x9AF9, "Acknowledge and write TX dest", inline=True)

# c9b35: TX done SR check and dispatch
comment(0x9B35, "A=&04: IFR bit 2 (SR) mask", inline=True)
comment(0x9B37, "Test SR interrupt pending", inline=True)
comment(0x9B3A, "SR fired: handle TX completion", inline=True)
comment(0x9B3C, "A=5: no SR, return status 5", inline=True)
comment(0x9B3E, "Return (no SR interrupt)", inline=True)
comment(0x9B3F, "Save X", inline=True)
comment(0x9B40, "Push X", inline=True)
comment(0x9B41, "Save Y", inline=True)
comment(0x9B42, "Push Y", inline=True)
comment(0x9B43, "Read ACR for shift register mode", inline=True)
comment(0x9B46, "Clear SR mode bits (2-4)", inline=True)
comment(0x9B48, "Restore original SR mode", inline=True)
comment(0x9B4B, "Write updated ACR", inline=True)
comment(0x9B4E, "Read SR to clear pending interrupt", inline=True)
comment(0x9B51, "A=&04: SR bit mask", inline=True)
comment(0x9B53, "Clear SR in IFR", inline=True)
comment(0x9B56, "Disable SR in IER", inline=True)
comment(0x9B59, "Load ctrl byte for dispatch", inline=True)
comment(0x9B5C, "Ctrl >= &86? (HALT/CONTINUE)", inline=True)
comment(0x9B5E, "Yes: skip protection mask save", inline=True)
comment(0x9B60, "Load current protection mask", inline=True)
comment(0x9B63, "Save mask before JSR modification", inline=True)
comment(0x9B66, "Enable bits 2-4 (allow JSR ops)", inline=True)
comment(0x9B68, "Store modified protection mask", inline=True)
comment(0x9B6B, "Load handler addr hi from table", inline=True)
comment(0x9B6E, "Push handler hi", inline=True)
comment(0x9B6F, "Load handler addr lo from table", inline=True)
comment(0x9B72, "Push handler lo", inline=True)
comment(0x9B73, "Dispatch via RTS (addr-1 on stack)", inline=True)

# tx_done_jsr (&9B7E)
comment(0x9B7E, "Push hi of (tx_done_exit-1)", inline=True)
comment(0x9B80, "Push hi byte on stack", inline=True)
comment(0x9B81, "Push lo of (tx_done_exit-1)", inline=True)
comment(0x9B83, "Push lo byte on stack", inline=True)
comment(0x9B84, "Call remote JSR; RTS to tx_done_exit", inline=True)

# tx_done_user_proc (&9B87)
comment(0x9B87, "Y=8: network event type", inline=True)
comment(0x9B89, "X = remote address lo", inline=True)
comment(0x9B8C, "A = remote address hi", inline=True)
comment(0x9B92, "Exit TX done handler", inline=True)

# tx_done_os_proc (&9B95)
comment(0x9B95, "X = remote address lo", inline=True)
comment(0x9B98, "Y = remote address hi", inline=True)
comment(0x9B9B, "Call ROM entry point at &8000", inline=True)
comment(0x9B9E, "Exit TX done handler", inline=True)

# tx_done_halt (&9BA1)
comment(0x9BA1, "A=&04: bit 2 mask for rx_flags", inline=True)
comment(0x9BA3, "Test if already halted", inline=True)
comment(0x9BA6, "Already halted: skip to exit", inline=True)
comment(0x9BA8, "Set bit 2 in rx_flags", inline=True)
comment(0x9BAB, "Store halt flag", inline=True)
comment(0x9BAE, "A=4: re-load halt bit mask", inline=True)
comment(0x9BB0, "Enable interrupts during halt wait", inline=True)
comment(0x9BB1, "Test halt flag", inline=True)
comment(0x9BB4, "Still halted: keep spinning", inline=True)

# inactive_poll (&9C2F)
comment(0x9C2F, "Save TX index", inline=True)
comment(0x9C32, "Push timeout byte 1 on stack", inline=True)
comment(0x9C33, "Push timeout byte 2 on stack", inline=True)
comment(0x9C38, "Save interrupt state", inline=True)
comment(0x9C39, "Disable interrupts for ADLC access", inline=True)
comment(0x9C4A, "Write CR2: clear status, prepare TX", inline=True)
comment(0x9C57, "Restore interrupt state", inline=True)
comment(0x9C59, "Increment timeout counter byte 1", inline=True)
comment(0x9C5C, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C5E, "Increment timeout counter byte 2", inline=True)
comment(0x9C61, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C63, "Increment timeout counter byte 3", inline=True)
comment(0x9C66, "Not overflowed: retry INACTIVE test", inline=True)
comment(0x9C68, "All 3 bytes overflowed: line jammed", inline=True)
comment(0x9C6B, "CR1=&44: TIE | TX_LAST_DATA", inline=True)

# tx_ctrl_poke (&9CD3)
comment(0x9CD3, "Scout status = 2 (POKE transfer)", inline=True)
comment(0x9CD5, "Store scout status", inline=True)
comment(0x9CD8, "Clear carry for 4-byte addition", inline=True)
comment(0x9CD9, "Save carry on stack", inline=True)
comment(0x9CDA, "Y=&0C: start at offset 12", inline=True)
comment(0x9CDC, "Load workspace address byte", inline=True)
comment(0x9CDF, "Restore carry from previous byte", inline=True)
comment(0x9CE0, "Add TXCB address byte", inline=True)
comment(0x9CE2, "Store updated address byte", inline=True)
comment(0x9CE5, "Next byte", inline=True)
comment(0x9CE6, "Save carry for next addition", inline=True)

# ============================================================
# Label renaming: auto-generated labels in 3.40
# ============================================================
# Names derived from context analysis and DNFS 3.60 reference source
# (label_correspondence.py). DNFS matches noted where applicable.

# --- Subroutine-category labels (18) ---
label(0x0414, "tube_send_release")    # Sends release (5) + claimed ID via R4
label(0x8EF9, "rs")                   # DNFS: RS — OSWORD 11 sub-function router
label(0x9148, "nword")                # DNFS: NWORD — OSWORD 7/8 fire-and-forget
label(0x96B2, "poll_nmi_ready")       # Polls NMI vector for shim installation
label(0x97F7, "ack_scout_match")      # Sets scout_status=3, initiates ACK
label(0x9A03, "inc_rxcb_buf_hi")      # Increments RXCB buffer high byte
label(0x9A47, "copy_scout_fields")    # Copies scout fields to port workspace
label(0x9AE3, "set_tx_reply_flag")    # Sets TX reply-pending flag (bit7)
label(0x9AEB, "rx_imm_halt_cont")     # Handler for HALT/CONTINUE immediate ops
label(0x9AF0, "tx_cr2_setup")         # Self-modifying CR2 configuration
label(0x9AF5, "tx_nmi_setup")         # Self-modifying NMI handler lo byte
label(0x9B32, "imm_op_discard")       # Error path: JMP discard_listen
label(0x9B35, "check_sr_irq")         # Tests SR interrupt pending via IFR
label(0x9C40, "test_line_idle")       # Tests SR2 INACTIVE bit for line idle
label(0x9CCB, "imm_op_status3")       # Loads scout_status=3 for immediate ops
label(0x9D16, "proc_op_status2")      # Loads scout_status=2 for proc calls
label(0x9EA6, "tube_tx_inc_byte2")    # Increment byte 2 of 4-byte counter
label(0x9EAE, "tube_tx_inc_byte4")    # Increment byte 4 of 4-byte counter

# --- Shared-tail labels (8) ---
label(0x0020, "tube_send_zero_r2")    # Sends zero prefix via R2 to Tube
label(0x8211, "return_service")       # LDY ws_page, RTS (service unclaimed)
label(0x87D3, "send_fs_reply")        # Sends FS reply command after transfer
label(0x8D55, "print_newline")        # JMP OSNEWL after catalogue line
label(0x96D5, "enter_rx_listen")      # JMP adlc_rx_listen (idle RX mode)
label(0x9A0C, "store_rxcb_buf_hi")    # Stores buffer hi byte to RXCB offset 9
label(0x9CD5, "store_status_add4")    # Stores scout status + 4-byte addition
label(0x9D18, "store_status_copy_ptr")  # Stores status + copies TX block ptr

# --- Data labels (17) ---
label(0x8001, "lang_entry_lo")        # ROM language entry address low byte
label(0x8002, "lang_entry_hi")        # ROM language entry address high byte
label(0x8004, "svc_entry_lo")         # ROM service entry address low byte
label(0x0051, "tube_jmp_target")      # Self-modifying JMP operand
label(0x0518, "tube_ctrl_values")     # Tube ULA control register lookup table
label(0x86AD, "tx_poll_status")       # BIT target for poll loop (bit7 busy)
label(0x8C06, "fs_cmd_dispatch_hi")   # FS command dispatch address high byte
label(0x8D08, "boot_option_text")     # Boot option name/offset table
label(0x8D1C, "boot_oscli_offset")    # Boot option OSCLI string offset table
label(0x8EB0, "osword_handler_lo")    # OSWORD handler address lo table
label(0x90A3, "netvec_handler_hi")    # NETVEC handler address hi table
label(0x9A04, "imm_dispatch_lo")      # Immediate op handler addr lo base
label(0x9AF1, "tx_done_handler_lo")   # TX done handler address lo table
label(0x9AF6, "tx_done_handler_hi")   # TX done handler address hi table
label(0x9C42, "sr2_idle_status")      # BIT operand for SR2 INACTIVE test
label(0x9EA7, "tube_tx_count_2")      # 4-byte counter byte 2 operand
label(0x9EAF, "tube_tx_count_4")      # 4-byte counter byte 4 operand

# --- Internal loop labels (10) ---
label(0x8262, "copy_vectors_loop")    # FS vector copy loop (cf. DOFSL1)
label(0x869D, "tx_semaphore_spin")    # TX semaphore spinlock
label(0x87E3, "copy_attr_loop")       # Copy 4 attribute bytes loop
label(0x8825, "block_addr_loop")      # Multi-byte address addition loop
label(0x8C99, "cattxt")               # DNFS: CATTXT — catalogue text print loop
label(0x9117, "poll_rxcb_loop")       # Poll RXCB for OSBYTE reply
label(0x9A49, "copy_scout_loop")      # Copy 8 scout fields to workspace
label(0x9AA7, "copy_addr_loop")       # Copy 4-byte remote address loop
label(0x9BB1, "halt_spin_loop")       # Spin-wait during system halt state
label(0x9CDC, "add_bytes_loop")       # 4-byte address addition loop

# --- Internal conditional labels (33) ---
label(0x046D, "flush_r3_nmi_check")   # BIT R3 twice to flush, check NMI
comment(0x046D, "Flush R3 data (first byte)", inline=True)
label(0x8114, "no_adlc_found")        # No ADLC: zero station ID, set flag
label(0x8118, "adlc_detect_done")     # ADLC detection complete
label(0x852D, "fs_reply_poll")        # Poll for FS reply with timeout/escape
label(0x869A, "tx_retry")             # Retry TX after error
label(0x86C7, "msdely")               # DNFS: MSDELY — delay loop
label(0x86CF, "tx_not_listening")     # Fatal TX error: "Not listening"
label(0x86D3, "tx_success")           # TX success: clean return
label(0x87E6, "direct_attr_copy")     # Skip attr decode, direct copy
label(0x881A, "next_block")           # Reinit for next transfer block
label(0x8843, "clamp_dest_setup")     # Set up 4-byte dest clamping
label(0x8C71, "cat_check_access")     # Branch on access level
label(0x8D35, "next_filename_char")   # Load and print next filename char
label(0x8D4D, "print_hex_fields")     # Print load/exec/length fields
label(0x8DA5, "dir_column_check")     # Check column position for formatting
label(0x8DA7, "dir_print_char")       # Column character output (cf. INFOL2)
label(0x8E1C, "exec_at_load_addr")    # JMP (fs_load_vector) — execute locally
label(0x9196, "rxcb_matched")         # Scout frame matched RXCB
label(0x9221, "pril1")                # DNFS: PRIL1 — print/store loop
label(0x96B7, "nmi_vec_lo_match")     # NMI vector low byte matches
label(0x97AF, "scout_ctrl_check")     # Check scout control byte
label(0x97CB, "scout_port_match")     # Check scout port number
label(0x97DC, "scout_station_check")  # Check scout station number
label(0x97E0, "scout_network_match")  # Check scout network number
label(0x97EF, "scout_accept")         # Scout accepted: all checks passed
label(0x98F8, "rx_update_buf")        # Update buffer pointer after RX
label(0x990E, "rx_check_error")       # Check error status after data RX
label(0x9A76, "imm_op_dispatch")      # PHA/PHA/RTS dispatch for immediate ops
label(0x9A82, "imm_op_out_of_range")  # JMP nmi_error_dispatch
label(0x9B3F, "tx_done_error")        # TX error code check
label(0x9B6B, "tx_done_classify")     # TX operation type classification
label(0x9D1B, "skip_buf_setup")       # Transfer size check: skip buffer
label(0x9E75, "jmp_tx_result_fail")   # JMP tx_result_fail


# ============================================================
# Annotations back-propagated from NFS 3.35K
# ============================================================
comment(0x041E, "&80 sentinel: clear address claim", inline=True)
label(0x0432, "setup_data_transfer")   # Save (X,Y) as transfer addr, send type via R4
comment(0x0449, "Send claimed address via R4", inline=True)

comment(0x0470, "Flush R3 data (second byte)", inline=True)
subroutine(0x04CB, "tube_init_reloc", hook=None,
    title="Initialise relocation address for ROM transfer",
    description="""\
Sets source page to &8000 and page counter to &80. Checks
ROM type bit 5 for a relocation address in the ROM header;
if present, extracts the 4-byte address from after the
copyright string. Otherwise uses default &8000 start.""")
comment(0x0604, "Return to main event loop", inline=True)
comment(0x060A, "Save in X", inline=True)
comment(0x060B, "Read Y parameter from co-processor", inline=True)
comment(0x060E, "Save in Y", inline=True)
comment(0x060F, "Read A (OSBYTE function code)", inline=True)
comment(0x0612, "Execute OSBYTE A,X,Y", inline=True)
comment(0x061A, "Send carry+status byte via R2", inline=True)
comment(0x061D, "Poll R2 status for ready", inline=True)
comment(0x0620, "Not ready: keep polling", inline=True)
label(0x0627, "tube_osword")          # OSWORD variable-length: read A+params, call &FFF1
comment(0x062A, "Save OSWORD number in Y", inline=True)
comment(0x062B, "Poll R2 status for data ready", inline=True)
comment(0x062E, "Not ready: keep polling", inline=True)
comment(0x0634, "No params (length=0): skip read loop", inline=True)
comment(0x0636, "Poll R2 status for data ready", inline=True)
comment(0x0639, "Not ready: keep polling", inline=True)
comment(0x063B, "Read param byte from R2", inline=True)
comment(0x0641, "Next param byte (descending)", inline=True)
comment(0x0642, "Loop until all params read", inline=True)
comment(0x0647, "Y=&01: param block at &0128", inline=True)
comment(0x0649, "Execute OSWORD with XY=&0128", inline=True)
comment(0x064C, "Poll R2 status for ready", inline=True)
comment(0x064F, "Not ready: keep polling", inline=True)
comment(0x0654, "Decrement result byte counter", inline=True)
comment(0x065A, "Poll R2 status for ready", inline=True)
comment(0x065D, "Not ready: keep polling", inline=True)
comment(0x065F, "Send result byte via R2", inline=True)
comment(0x0662, "Next result byte (descending)", inline=True)
comment(0x0663, "Loop until all results sent", inline=True)
comment(0x0665, "Return to main event loop", inline=True)
comment(0x066A, "Read control block byte from R2", inline=True)
comment(0x066D, "Store in zero page params", inline=True)
comment(0x066F, "Next byte (descending)", inline=True)
comment(0x0670, "Loop until all 5 bytes read", inline=True)
comment(0x0673, "Y=0 for OSWORD 0", inline=True)
comment(0x0675, "A=0: OSWORD 0 (read line)", inline=True)
comment(0x0676, "Read input line from keyboard", inline=True)
comment(0x067D, "Escape: send &FF error to co-processor", inline=True)
comment(0x0680, "X=0: start of input buffer at &0700", inline=True)
comment(0x0684, "Send &7F (success) to co-processor", inline=True)
comment(0x0687, "Load char from input buffer", inline=True)
comment(0x068A, "Send char to co-processor", inline=True)
comment(0x068D, "Next character", inline=True)
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
comment(0x06AA, "ROR: shift escape bit 7 to carry", inline=True)
comment(0x06B0, "Send zero prefix via R1", inline=True)
comment(0x06B3, "Y value for event", inline=True)
comment(0x06B4, "Send Y via R1", inline=True)
comment(0x06B7, "X value for event", inline=True)
comment(0x06B8, "Send X via R1", inline=True)
comment(0x06BB, "Restore A (event type)", inline=True)
comment(0x06BC, "Poll R1 status (bit 6 = ready)", inline=True)
comment(0x06BF, "Not ready: keep polling", inline=True)
comment(0x06C1, "Write A to Tube R1 data register", inline=True)
comment(0x06C4, "Return to caller", inline=True)
comment(0x8081, "Advance past matched command text", inline=True)
comment(0x80C1, "Copy command text to FS buffer", inline=True)
comment(0x80CB, "CSD handle zero: not logged in", inline=True)
comment(0x80D7, "FSCV function >= 8?", inline=True)
comment(0x80DB, "X = function code for dispatch", inline=True)
comment(0x80DC, "Save Y (command text ptr hi)", inline=True)
comment(0x8277, "A=&8F: issue service request", inline=True)
comment(0x8279, "X=&0F: 'vectors claimed' service", inline=True)
comment(0x827E, "X=&0A: service &0A", inline=True)
comment(0x8285, "Non-zero: skip auto-boot", inline=True)
comment(0x8298, "ARGSV dispatch lo", inline=True)
comment(0x829B, "BGETV dispatch hi", inline=True)
comment(0x829C, "BPUTV dispatch lo", inline=True)
comment(0x829E, "GBPBV dispatch lo", inline=True)
comment(0x829F, "GBPBV dispatch hi", inline=True)
comment(0x82A0, "FINDV dispatch lo", inline=True)
comment(0x82A1, "FINDV dispatch hi", inline=True)
comment(0x82A2, "FSCV dispatch lo", inline=True)
comment(0x82B7, "FSCV handler hi", inline=True)
comment(0x82BE, "Return (workspace claim done)", inline=True)
comment(0x834F, "Load FS state byte at offset Y", inline=True)
comment(0x8352, "Store to workspace backup area", inline=True)
comment(0x8354, "Next byte down", inline=True)
comment(0x8357, "Loop for offsets &1D..&15", inline=True)
comment(0x8359, "A=&77: OSBYTE close spool/exec", inline=True)
subroutine(0x8383, "init_tx_reply_port", hook=None,
    title="Initialise TX control block for FS reply on port &90",
    description="""\
Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
up the TX control block, stores the port and control bytes, then
decrements the control flag. Used by send_fs_reply_cmd to prepare
for receiving the fileserver's reply.""")
comment(0x8390, "Return after port setup", inline=True)
comment(0x83A9, "Control flag", inline=True)
comment(0x83AA, "Port (FS command = &99)", inline=True)
comment(0x83AD, "Buffer start low", inline=True)
comment(0x83AE, "Buffer start high (page &0F)", inline=True)
comment(0x83AF, "Buffer start pad (4-byte Econet addr)", inline=True)
comment(0x83B0, "Buffer start pad", inline=True)
comment(0x83B1, "Buffer end low", inline=True)
comment(0x83B2, "Buffer end high (page &0F)", inline=True)
comment(0x83B3, "Buffer end pad", inline=True)
comment(0x83B4, "Buffer end pad", inline=True)
subroutine(0x83B5, "prepare_cmd_with_flag", hook=None,
    title="Prepare FS command with carry set",
    description="""\
Alternate entry to prepare_fs_cmd that pushes A, loads &2A
into fs_error_ptr, and enters with carry set (SEC). The carry
flag is later tested by build_send_fs_cmd to select the
byte-stream (BSXMIT) transmission path.""")
comment(0x83BC, "A=&77: OSBYTE close spool/exec", inline=True)
comment(0x840F, "CLC for address addition", inline=True)
comment(0x8495, "Transfer A to Y for indexing", inline=True)
comment(0x8497, "Transfer to X for return", inline=True)
comment(0x84CD, "A=0: zero execution header bytes", inline=True)
comment(0x84D2, "Next byte", inline=True)
comment(0x84D3, "Loop until all zeroed", inline=True)
comment(0x852D, "Check for user escape condition", inline=True)
comment(0x8556, "LSR: get escape result bit", inline=True)
comment(0x8557, "Store escape result to TXCB", inline=True)
comment(0x8559, "Restore A", inline=True)
comment(0x855A, "Non-zero: report 'Not listening'", inline=True)
comment(0x8572, "Set EOF flag for this handle", inline=True)
label(0x8575, "load_handle_mask")      # Load handle bitmask for return
comment(0x8575, "Load handle bitmask for caller", inline=True)
comment(0x8578, "Return with handle mask in A", inline=True)
comment(0x8606, "Store return addr low as string ptr", inline=True)
comment(0x8609, "Store return addr high as string ptr", inline=True)
comment(0x860B, "Y=0: offset for indirect load", inline=True)
comment(0x860F, "No page wrap: skip high byte inc", inline=True)
comment(0x8611, "Handle page crossing in pointer", inline=True)
comment(0x8642, "Return with result in A", inline=True)
comment(0x865D, "Restore X from stack", inline=True)
comment(0x865F, "Return with mask in X", inline=True)
comment(0x8667, "Return with handle in A", inline=True)
comment(0x8670, "Next byte", inline=True)
comment(0x8673, "Return with Z flag result", inline=True)
comment(0x8678, "Return (FSCV 7 read handles)", inline=True)
comment(0x868F, "A=&FF: full retry count", inline=True)
subroutine(0x86D7, "copy_filename_ptr", hook=None,
    title="Copy filename pointer to os_text_ptr and parse",
    description="""\
Copies the 2-byte filename pointer from (fs_options),Y into
os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
to parse the filename via GSINIT/GSREAD into the &0E30 buffer.""")
subroutine(0x86E3, "parse_filename_gs_y", hook=None,
    title="Parse filename via GSINIT/GSREAD from offset Y",
    description="""\
Sub-entry of parse_filename_gs that accepts a non-zero Y offset
into the (os_text_ptr) string. Initialises GSINIT, reads chars
via GSREAD into &0E30, CR-terminates the result, and sets up
fs_crc_lo/hi to point at the buffer.""")
comment(0x8705, "Save A/X/Y in FS workspace", inline=True)
comment(0x8711, "A=&FF: branch to load path", inline=True)
comment(0x8716, "Copy parsed filename to cmd buffer", inline=True)
comment(0x8719, "Y=2: FS function code offset", inline=True)
comment(0x874C, "Display file info after FS reply", inline=True)
comment(0x87D3, "Send FS reply acknowledgement", inline=True)
comment(0x87E1, "Z=1: first byte, use A directly", inline=True)
comment(0x87E3, "Load attribute byte from FS reply", inline=True)
comment(0x87E6, "Store decoded access in param block", inline=True)
comment(0x87E8, "Next attribute byte", inline=True)
comment(0x87FE, "Add 1 (of 5) to Y", inline=True)
comment(0x87FF, "Add 2 (of 5) to Y", inline=True)
comment(0x8800, "Add 3 (of 5) to Y", inline=True)
comment(0x880A, "Next byte (descending)", inline=True)
comment(0x880D, "Loop until offset 2 reached", inline=True)
comment(0x8810, "Subtract 1 (of 3) from Y", inline=True)
comment(0x8811, "Subtract 2 (of 3) from Y", inline=True)
comment(0x8812, "Subtract 3 (of 3) from Y", inline=True)
comment(0x8813, "Return to caller", inline=True)
comment(0x881A, "X=0: clear hi bytes of block size", inline=True)
comment(0x881C, "Y=4: process 4 address bytes", inline=True)
comment(0x881E, "Clear block size hi byte 1", inline=True)
comment(0x8821, "Clear block size hi byte 2", inline=True)
comment(0x8824, "CLC for ADC in loop", inline=True)
comment(0x8825, "Source = current position", inline=True)
comment(0x8827, "Store source address byte", inline=True)
comment(0x8829, "Add block size to current position", inline=True)
comment(0x8834, "Carry: address overflowed, clamp", inline=True)
subroutine(0x8990, "return_a_zero", hook=None,
    title="Return with A=0 via register restore",
    description="""\
Loads A=0 and branches (always taken) to the common register
restore exit at restore_args_return. Used as a shared exit
point by ARGSV, FINDV, and GBPBV when an operation is
unsupported or should return zero.""")
comment(0x89C6, "A=handle bitmask for new file", inline=True)
comment(0x8A2D, "Return (unsupported function)", inline=True)
comment(0x8CC5, "Print two CRs (blank line)", inline=True)
label(0x8CD2, "cat_examine_loop")      # Send examine request and display entries
subroutine(0x8D92, "cat_column_separator", hook=None,
    title="Print catalogue column separator or newline",
    description="""\
Handles column formatting for *CAT display. On a null byte
separator, advances the column counter modulo 4: prints a
2-space separator between columns, or a CR at column 0.
Called from fsreply_0_print_dir.""")
subroutine(0x8E45, "load_handle_calc_offset", hook=None,
    title="Load handle from &F0 and calculate workspace offset",
    description="""\
Loads the file handle byte from &F0, then falls through to
calc_handle_offset which converts handle * 12 to a workspace
byte offset. Validates offset < &48.""")
comment(0x8E58, "Return after calculation", inline=True)
comment(0x8E83, "Outside our OSWORD range, exit", inline=True)
subroutine(0x9072, "enable_irq_and_tx", hook=None,
    title="Enable interrupts and transmit via tx_poll_ff",
    description="""\
CLI to enable interrupts, then JMP tx_poll_ff. A short
tail-call wrapper used after building the TX control block.""")
comment(0x9115, "Write &7F to RXCB (wait for reply)", inline=True)
comment(0x9117, "Poll RXCB for completion (bit7)", inline=True)
comment(0x9190, "V=1: use (net_rx_ptr) page", inline=True)
comment(0x9192, "V=1: skip to net_rx_ptr page", inline=True)
comment(0x9194, "V=0: use (nfs_workspace) page", inline=True)
comment(0x91B9, "SKIP (main only)", inline=True)
comment(0x91BC, "PAGE byte → Y=&11 (main only)", inline=True)
comment(0x91BD, "→ Y=&12 (main only)", inline=True)
comment(0x91BE, "→ Y=&13 (main only)", inline=True)
comment(0x91BF, "→ Y=&14 (main only)", inline=True)
comment(0x91C2, "→ Y=&17 (main only)", inline=True)
comment(0x91DB, "Store initial PFLAGS value", inline=True)
comment(0x9214, "XOR with current PFLAGS", inline=True)
comment(0x9217, "Test if sequence changed (bit 7 mismatch)", inline=True)
comment(0x9218, "Sequence unchanged: skip flush", inline=True)
comment(0x921A, "Undo ROR", inline=True)
comment(0x921B, "Store toggled PFLAGS", inline=True)
comment(0x921E, "Flush current output block", inline=True)
comment(0x9221, "Reload current PFLAGS", inline=True)
comment(0x922C, "Store recombined PFLAGS value", inline=True)
comment(0x9248, "Load current PFLAGS", inline=True)
comment(0x924B, "Save current PFLAGS", inline=True)
comment(0x924C, "Carry = current sequence (bit 7)", inline=True)
comment(0x924D, "Restore original PFLAGS", inline=True)
comment(0x924E, "Toggle sequence number (bit 7 of PFLAGS)", inline=True)
comment(0x9250, "Store toggled sequence number", inline=True)
comment(0x9318, "Return after storing result", inline=True)
comment(0x9319, "OSBYTE &85: read cursor position", inline=True)
comment(0x931B, "OSBYTE &C3: read screen start address", inline=True)
comment(0x9660, "Trampoline: forward to tx_begin", inline=True)
comment(0x9663, "Trampoline: forward to adlc_init", inline=True)
comment(0x9666, "Trampoline: forward to NMI release", inline=True)
comment(0x9669, "Trampoline: forward to NMI claim", inline=True)
comment(0x966C, "Trampoline: forward to IRQ handler", inline=True)
subroutine(0x968D, "init_nmi_workspace", hook=None,
    title="Initialise NMI workspace (skip service request)",
    description="""\
Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
service request. Copies 32 bytes of NMI shim from ROM to
&0D00, patches the ROM bank number, sets init flags, reads
station ID, and re-enables NMIs.""")
comment(0x96B7, "Load NMI vector low byte", inline=True)
comment(0x96BA, "Check if low byte is expected value", inline=True)
comment(0x96BC, "Mismatch: keep polling", inline=True)
comment(0x96BE, "Load NMI vector high byte", inline=True)
comment(0x96C1, "Check if high byte is &96", inline=True)
comment(0x96C3, "Mismatch: keep polling", inline=True)
comment(0x96C5, "BIT INTOFF: disable NMIs", inline=True)
comment(0x96E9, "Write CR1: RIE | TX_RESET", inline=True)
comment(0x96EE, "Write CR2: listen mode config", inline=True)
comment(0x9707, "Store broadcast flag in TX flags", inline=True)
comment(0x970C, "High byte of scout net handler", inline=True)
comment(0x970E, "Install next handler and RTI", inline=True)
comment(0x9721, "Write CR1 to discontinue RX", inline=True)
comment(0x9724, "Return to idle scout listening", inline=True)
comment(0x972E, "High byte of scout data handler", inline=True)
comment(0x9730, "Install scout data loop and RTI", inline=True)
comment(0x9740, "Gentle discard: RX_DISCONTINUE", inline=True)
comment(0x975F, "Copied all 12 scout bytes?", inline=True)
comment(0x9763, "Save final buffer offset", inline=True)
label(0x97A7, "scan_nfs_port_list")   # NFS workspace port list scan entry
comment(0x97A7, "Store page to workspace pointer low", inline=True)
comment(0x97A9, "A=0: no NFS workspace offset yet", inline=True)
comment(0x97AB, "Clear NFS workspace search flag", inline=True)
comment(0x97B7, "Y=1: advance to port byte in slot", inline=True)
comment(0x97D5, "CLC for 12-byte slot advance", inline=True)
comment(0x97D6, "Advance to next 12-byte port slot", inline=True)
comment(0x97D8, "Update workspace pointer to next slot", inline=True)
comment(0x97DA, "Always branches (page &C0 won't overflow)", inline=True)
comment(0x97DC, "Check if NFS workspace already searched", inline=True)
comment(0x97DE, "Already searched: no match found", inline=True)
comment(0x97E0, "Try NFS workspace if paged list exhausted", inline=True)
comment(0x97E3, "No NFS workspace RX (bit6 clear) -- discard", inline=True)
comment(0x97E5, "Get NFS workspace page number", inline=True)
comment(0x97E7, "Mark NFS workspace as search target", inline=True)
comment(0x97E9, "Y=0: start at offset 0 in workspace", inline=True)
comment(0x97EB, "Reset slot pointer to start", inline=True)
comment(0x97EF, "Check broadcast flag (bit 6)", inline=True)
comment(0x97F2, "Not broadcast: ACK and set up RX", inline=True)
comment(0x97F4, "Broadcast: copy scout fields directly", inline=True)
comment(0x97F7, "Match found: set scout_status = 3", inline=True)
comment(0x97F9, "Record match for completion handler", inline=True)
comment(0x97FF, "Transfer OK: send data ACK", inline=True)
comment(0x981C, "High byte of nmi_data_rx handler", inline=True)
comment(0x9832, "High byte of nmi_data_rx handler", inline=True)
subroutine(0x9858, "install_data_rx_handler", hook=None,
    title="Install data RX bulk or Tube handler",
    description="""\
Selects either the normal bulk RX handler (&9843) or the Tube
RX handler (&98A0) based on the Tube transfer flag in tx_flags,
and installs the appropriate NMI handler.""")
subroutine(0x9872, "nmi_error_dispatch", hook=None,
    title="NMI error handler dispatch",
    description="""\
Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")
comment(0x98E5, "Advance Tube transfer byte count", inline=True)
comment(0x98E7, "Send byte to Tube data register 3", inline=True)
comment(0x98EA, "No overflow: read second byte", inline=True)
comment(0x98EC, "Carry to transfer count byte 2", inline=True)
comment(0x98EE, "No overflow: read second byte", inline=True)
comment(0x98F0, "Carry to transfer count byte 3", inline=True)
comment(0x98F2, "No overflow: read second byte", inline=True)
comment(0x98F4, "Carry to transfer count byte 4", inline=True)
comment(0x98F6, "All bytes zero: overflow error", inline=True)
comment(0x98F8, "Read second data byte (paired transfer)", inline=True)
comment(0x98FB, "Send second byte to Tube", inline=True)
comment(0x98FE, "Advance count after second byte", inline=True)
comment(0x9900, "No overflow: check for more data", inline=True)
comment(0x9902, "Carry to count byte 2", inline=True)
comment(0x9904, "No overflow: check for more data", inline=True)
comment(0x9906, "Carry to count byte 3", inline=True)
comment(0x9908, "No overflow: check for more data", inline=True)
comment(0x990A, "Carry to count byte 4", inline=True)
comment(0x990C, "Zero: Tube transfer complete", inline=True)
comment(0x990E, "Re-read SR2 for next byte pair", inline=True)
comment(0x9911, "More data available: continue loop", inline=True)
comment(0x9913, "Return from NMI, wait for data", inline=True)
comment(0x9988, "Write network=0 (local) to TX FIFO", inline=True)
comment(0x998B, "Check tx_flags for data phase", inline=True)
comment(0x998E, "bit7 set: start data TX phase", inline=True)
subroutine(0x99A4, "advance_rx_buffer_ptr", hook=None,
    title="Advance RX buffer pointer after transfer",
    description="""\
Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")
comment(0x99DA, "Restore X from stack", inline=True)
comment(0x99DB, "Transfer to X register", inline=True)
comment(0x99DC, "Y=8: RXCB buffer ptr offset", inline=True)
comment(0x99DE, "Load current RXCB buffer ptr lo", inline=True)
comment(0x99E0, "SEC for ADC #0 = add carry", inline=True)
comment(0x99E1, "Increment by 1 (Tube extra byte)", inline=True)
comment(0x99E3, "Store updated ptr back to RXCB", inline=True)
label(0x99FC, "add_buf_to_base")       # Add buffer length to base address (no Tube)
label(0x9A07, "store_rxcb_buf_ptr")  # Store updated buffer pointer pair to RXCB
comment(0x9A33, "Test tx_flags for Tube transfer", inline=True)
comment(0x9A38, "A=&82: Tube release claim type", inline=True)
subroutine(0x9A40, "install_rx_scout_handler", hook=None,
    title="Install RX scout NMI handler",
    description="""\
Installs nmi_rx_scout (&96BF) as the NMI handler via
set_nmi_vector, without first calling adlc_rx_listen.
Used when the ADLC is already in the correct RX mode.""")
comment(0x9A4E, "Advance buffer pointer", inline=True)
comment(0x9A53, "Jump to completion handler", inline=True)
comment(0x9A71, "Carry clear: operation permitted", inline=True)
comment(0x9A73, "Operation blocked by LSTAT mask", inline=True)
comment(0x9A76, "Reload ctrl byte for dispatch table", inline=True)
comment(0x9A79, "Look up handler address high byte", inline=True)
comment(0x9A7C, "Push handler address high", inline=True)
comment(0x9A7D, "Load handler low byte from jump table", inline=True)
comment(0x9A80, "Push handler address low", inline=True)
comment(0x9A81, "RTS dispatches to handler", inline=True)
comment(0x9A82, "Jump to discard handler", inline=True)
subroutine(0x9AFC, "imm_op_build_reply", hook=None,
    title="Build immediate operation reply header",
    description="""\
Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")
comment(0x9BB8, "Load current RX flags", inline=True)
comment(0x9BBB, "Clear bit 2: release halted station", inline=True)
comment(0x9BBD, "Store updated flags", inline=True)
comment(0x9BC0, "Restore Y from stack", inline=True)
comment(0x9BC1, "Transfer to Y register", inline=True)
comment(0x9BC2, "Restore X from stack", inline=True)
comment(0x9BC3, "Transfer to X register", inline=True)
comment(0x9BC4, "A=0: success status", inline=True)
comment(0x9BC6, "Return with A=0 (success)", inline=True)
subroutine(0x9BC7, "tx_begin", hook=None,
    title="Begin TX operation",
    description="""\
Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")
comment(0x9BF6, "(Y -= 4: reach start addr offset)", inline=True)
comment(0x9BF7, "(continued)", inline=True)
comment(0x9BF8, "(continued)", inline=True)
comment(0x9BFF, "(Y += 5: advance to next end byte)", inline=True)
comment(0x9C00, "(continued)", inline=True)
comment(0x9C01, "(continued)", inline=True)
comment(0x9C02, "(continued)", inline=True)
comment(0x9C03, "(continued)", inline=True)
label(0x9C0E, "check_imm_range")       # Check if ctrl byte is in immediate op range
subroutine(0x9C3A, "intoff_test_inactive", hook=None,
    title="Disable NMIs and test INACTIVE",
    description="""\
Mid-instruction label within the INACTIVE polling loop. The
address &9BE2 is referenced as a constant for self-modifying
code. Disables NMIs twice (belt-and-braces) then tests SR2
for INACTIVE before proceeding with TX.""")
comment(0x9C75, "Pop saved register", inline=True)
comment(0x9C76, "Pop saved register", inline=True)
comment(0x9CB2, "Load handler from dispatch table", inline=True)
comment(0x9CB5, "Push high byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x9CB6, "Look up handler address low from table", inline=True)
comment(0x9CB9, "Push low byte for PHA/PHA/RTS dispatch", inline=True)
comment(0x9CBA, "RTS dispatches to control-byte handler", inline=True)
comment(0x9CCB, "A=3: scout_status for PEEK", inline=True)
comment(0x9CCF, "A=3: scout_status for PEEK op", inline=True)
comment(0x9CE7, "Compare Y with 16-byte boundary", inline=True)
comment(0x9CE9, "Below boundary: continue addition", inline=True)
comment(0x9CEB, "Restore processor flags", inline=True)
comment(0x9CEC, "Exit TX ctrl setup", inline=True)
comment(0x9D3B, "Next TX buffer byte", inline=True)
comment(0x9D3C, "Load second byte from TX buffer", inline=True)
comment(0x9D3F, "Advance TX index past second byte", inline=True)
comment(0x9D40, "Save updated TX buffer index", inline=True)
comment(0x9D59, "Write CR2: clear status, idle listen", inline=True)
comment(0x9D62, "PHA/PLA delay (~7 cycles each)", inline=True)
comment(0x9D63, "Increment delay counter", inline=True)
comment(0x9D64, "Loop 256 times for NMI disable", inline=True)
comment(0x9D66, "Store error and return to idle", inline=True)
comment(0x9D77, "Write CR1 to switch from TX to RX", inline=True)
comment(0x9D82, "A=1: mask for bit0 test", inline=True)
comment(0x9D84, "Test tx_flags bit0 (handshake)", inline=True)
comment(0x9D87, "bit0 clear: install reply handler", inline=True)
comment(0x9D8E, "High byte of nmi_reply_scout addr", inline=True)
comment(0x9D90, "Install handler and RTI", inline=True)
comment(0x9DA4, "High byte of nmi_reply_cont", inline=True)
comment(0x9DA6, "Install continuation handler", inline=True)
comment(0x9DB5, "High byte of nmi_reply_validate", inline=True)
comment(0x9DBF, "Store error and return to idle", inline=True)
comment(0x9E70, "bit7 clear: error path", inline=True)
comment(0x9E72, "ADLC reset and return to idle", inline=True)
comment(0x9E75, "Store result and return to idle", inline=True)
comment(0x9E78, "Load saved handler low byte", inline=True)
comment(0x9ED7, "High byte of handler address", inline=True)
comment(0x9ED9, "Install continuation handler", inline=True)
comment(0x9EE8, "High byte of handler address", inline=True)
comment(0x9EEF, "Install handler and RTI", inline=True)
comment(0x9F07, "Load TX flags for next action", inline=True)
comment(0x9F0A, "bit7 clear: no data phase", inline=True)
comment(0x9F0C, "Install data RX handler", inline=True)
label(0x9F1A, "tx_result_fail")        # Store result=&41 (not listening) (9 refs)
comment(0x9F48, "Load TX flags for transfer setup", inline=True)
comment(0x9F4D, "Store with bit 1 set (Tube xfer)", inline=True)
comment(0x9F57, "Y += 4: advance to high ptr offset", inline=True)
comment(0x9F58, "(continued)", inline=True)
comment(0x9F59, "(continued)", inline=True)
comment(0x9F61, "Y -= 3: back to next low ptr byte", inline=True)
comment(0x9F62, "(continued)", inline=True)
comment(0x9F6D, "CLC for base pointer addition", inline=True)
comment(0x9F6E, "Add RXCB base to get RXCB+4 addr", inline=True)
comment(0x9F75, "Claim Tube transfer address", inline=True)
comment(0x9F7D, "Reclaim with scout status type", inline=True)
comment(0x9F82, "Restore X from stack", inline=True)
comment(0x9F83, "Return with C = transfer status", inline=True)
comment(0x9FA7, "Return with C=1 (success)", inline=True)
comment(0x9FC2, "Transfer ROM bank to Y", inline=True)

# ============================================================
# Inline comments for 3.40 change-block gaps
# ============================================================

# i_am_handler (&8082)
comment(0x80B0, "Test escape flag before FS reply", inline=True)

# svc_star_command (&81A5)
comment(0x81AB, "Return to MOS service handler", inline=True)
comment(0x81AD, "NOP padding for command table", inline=True)
comment(0x81AE, "NOP padding", inline=True)
comment(0x81AF, "NOP padding", inline=True)
comment(0x81B0, "NOP padding", inline=True)

# svc_9_help (&8204)
comment(0x8211, "Load workspace page for printing", inline=True)

# print_station_info (&822E)
comment(0x8240, "Y=&14: offset for station number", inline=True)

# init_fs_vectors (&8260)
comment(0x8262, "Load vector address from table", inline=True)

# svc_2_private_workspace (&82C1)
comment(0x82C1, "Store page as RX buffer high byte", inline=True)
comment(0x82C3, "Next page for NFS workspace", inline=True)
comment(0x82C4, "Store page as NFS workspace high", inline=True)

# fscv_6_shutdown (&834D)
comment(0x8382, "Return with Z flag result", inline=True)

# check_escape_handler (&854D)
comment(0x854D, "Test escape flag (bit 7)", inline=True)
comment(0x854F, "Bit 7 clear: no escape, return", inline=True)
comment(0x8551, "A=&7E: acknowledge escape OSBYTE", inline=True)

# lang_0_insert_remote_key (&84E8)
comment(0x851B, "A=&2A: error ptr for FS send", inline=True)

# &8605 (print_inline)
comment(0x861A, "Continue printing next character", inline=True)

# parse_decimal (&8620)
comment(0x8622, "Initialise accumulator to zero", inline=True)

# filev_save (&878F)
comment(0x87CA, "Display save info (addr/len)", inline=True)
comment(0x87CD, "Load reply byte for transfer", inline=True)

# fs_cmd_match_table (&8C05)
comment(0x8C1B, "X=1: *EX single-entry examine", inline=True)
comment(0x8C1D, "A=3: column count for *EX mode", inline=True)

# fscv_5_cat (&8C21)
comment(0x8C57, "Load access level from reply", inline=True)
comment(0x8C65, "ALWAYS branch past 'Owner'", inline=True)
comment(0x8C8A, "Load boot option from reply", inline=True)
comment(0x8C96, "Y=string offset for this option", inline=True)
comment(0x8C99, "Load next char of option name", inline=True)
comment(0x8C9C, "Bit 7 set: end of option name", inline=True)
comment(0x8CAE, "X=&11: Dir. name offset in reply", inline=True)
comment(0x8CB0, "Print directory name (10 chars)", inline=True)
comment(0x8CB3, "Print '     Lib. ' header", inline=True)
comment(0x8CC0, "X=&1B: Lib. name offset in reply", inline=True)
comment(0x8CE5, "Zero entries: catalogue complete", inline=True)
comment(0x8D07, "Return from column separator", inline=True)

# cat_column_separator (&8D92)
comment(0x8DA3, "More entries: skip final newline", inline=True)
comment(0x8DA5, "A=CR: print newline separator", inline=True)

# calc_handle_offset (&8E47)
comment(0x8E59, "Y=&6F: RX buffer handle offset", inline=True)
comment(0x8E5B, "Read handle from RX packet", inline=True)
comment(0x8E5D, "Valid handle: store and return", inline=True)

# osword_0f_handler (&8EBA)
comment(0x8EBA, "Test TX semaphore (bit 7 to C)", inline=True)
comment(0x8EBD, "Save Y for return value", inline=True)
comment(0x8EBE, "C=0: TX busy, return error", inline=True)

# osword_11_handler (&8ED4)
comment(0x8EF9, "Sub-function >= 6?", inline=True)
comment(0x8EFB, "Yes: jump to sub 6-9 handler", inline=True)
comment(0x8EFD, "Sub-function >= 4?", inline=True)

# remote_cmd_dispatch (&90DE)
comment(0x9148, "Y=14: max OSWORD parameter bytes", inline=True)
comment(0x914A, "OSWORD 7 = make a sound", inline=True)

# init_nmi_workspace (&968D)
comment(0x96AE, "BIT VULA: enable NMIs via latch", inline=True)
comment(0x96B1, "Return from NMI workspace init", inline=True)
comment(0x96B2, "Test Econet init complete flag", inline=True)
comment(0x96B5, "Init done: enter RX listen mode", inline=True)

# scout_complete (&976D)
comment(0x97FC, "Calculate transfer parameters", inline=True)

# discard_reset_listen (&9A2E)
comment(0x9A30, "Check if Tube transfer active", inline=True)

# tx_calc_transfer (&9F38)
comment(0x9F3A, "Load workspace byte at offset Y", inline=True)

# &9FE0 (print_hex)
comment(0x9FE2, "Shift high nibble to low", inline=True)
comment(0x9FE3, "Shift high nibble to low", inline=True)
comment(0x9FE4, "Shift high nibble to low", inline=True)

# tube_code_page4 (&0400)
comment(0x0414, "A=5: Tube release request code", inline=True)
comment(0x0416, "Send release code via R4", inline=True)
comment(0x0419, "Load current Tube claim ID", inline=True)
comment(0x041B, "Send claim ID via R4", inline=True)
comment(0x043E, "Send transfer address byte", inline=True)
comment(0x04A9, "Load ROM header byte for TX", inline=True)

# tube_dispatch_table (&0500)
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
comment(0x0520, "Read channel handle from R2", inline=True)
comment(0x052D, "Read channel handle from R2", inline=True)
comment(0x053B, "Send carry+data byte to Tube R2", inline=True)
comment(0x053E, "ROL A: restore carry flag", inline=True)
comment(0x0542, "Read open mode from R2", inline=True)
comment(0x055E, "Read file handle from R2", inline=True)
comment(0x0596, "Read command string from R2", inline=True)
comment(0x05A9, "X=&10: 16 bytes for OSFILE CB", inline=True)
comment(0x05F2, "Read OSWORD number from R2", inline=True)

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
