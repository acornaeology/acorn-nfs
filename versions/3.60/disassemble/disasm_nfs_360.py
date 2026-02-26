import os
from pathlib import Path

from py8dis.commands import *
import py8dis.acorn as acorn

init(assembler_name="beebasm", lower_case=True)

# ============================================================
# Address map: NFS 3.40 → NFS 3.60
# ============================================================
# This driver was derived from the NFS 3.40 disassembly driver.
# The two ROMs are 89.9% identical at the opcode level.
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
    str(_version_dirpath / "rom" / "nfs-3.60.rom"),
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
# Vectors set up during init (rewritten in 3.40 — only 2 vectors,
# RDCHV and WRCHV are no longer claimed):
#   BRKV  = &0016 (in workspace block — BRK/error handler)
#   EVNTV = &06AD (in page 6 — event handler)

# BRK handler + NMI workspace init code (&9321 → &0016-&0076)
move(0x0016, 0x9321, 0x61)

# NMI handler / CLI command code (&9362/&9462/&9562 → pages &04/&05/&06)
move(0x0400, 0x9362, 0x100)
move(0x0500, 0x9462, 0x100)
move(0x0600, 0x9562, 0x100)

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
hook_subroutine(0x865C, "print_inline", stringhi_hook)

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
comment(0x0016, "A=&FF: signal error to co-processor via R4", inline=True)
comment(0x001B, "Flush any pending R2 byte", inline=True)
comment(0x0023, "Y=0: start of error block at (&FD)", inline=True)
comment(0x002F, "Zero byte = end of error string", inline=True)
comment(0x0046, "Re-check R1: WRCH has priority over R2", inline=True)
comment(0x004E, "Self-modify JMP low byte for dispatch", inline=True)

# Relocated code — page 4 (Tube address claim, RDCH, data transfer)
# Reference: NFS12 (BEGIN, ADRR, SENDW, TADDR, SETADR)
label(0x0403, "tube_escape_entry")   # JMP to tube_escape_check (&06E2)
label(0x0406, "tube_addr_claim")     # Tube address claim protocol (ADRR in reference)
label(0x0421, "tube_post_init")      # Called after ROM→RAM copy; initial Tube setup
label(0x0434, "return_tube_init")    # Return from tube_post_init path
label(0x0483, "return_tube_xfer")   # Return from tube transfer/setup
# 3.35K label tube_setup_transfer ($04E0) — Tube code rewritten in 3.40
# 3.34 label tube_rdch_handler ($04E7) — Tube code rewritten in 3.40; address
# now falls inside sub_c04d2 relocation address extraction. RDCHV no longer claimed.
# 3.35K labels tube_restore_regs ($04EF), tube_read_r2 ($04F7) — also rewritten.
entry(0x0400)
entry(0x0403)
entry(0x0406)
entry(0x0421)
# tube_addr_claim: A>=&80 is address (re)claim, A<&80 is data transfer
comment(0x0406, "A>=&80: address claim; A<&80: data transfer", inline=True)
comment(0x040A, "A>=&C0: new address claim from another host", inline=True)
comment(0x040E, "Map &80-&BF range to &C0-&FF for comparison", inline=True)
comment(0x0410, "Is this for our currently-claimed address?", inline=True)
comment(0x0416, "R4 cmd 5: release our address claim", inline=True)
comment(0x0423, "&80 sentinel = no address currently claimed", inline=True)
comment(0x0428, "Another host claiming; check if we're owner", inline=True)
comment(0x0430, "Not ours: CLC = we don't own this address", inline=True)
comment(0x0432, "Accept new claim: update our address", inline=True)
# c0435: data transfer setup for A<&80 (SENDW protocol)
comment(0x0437, "Save 16-bit transfer address from (X,Y)", inline=True)
comment(0x043B, "Send transfer type byte to co-processor", inline=True)
comment(0x0441, "Send our claimed address + 4-byte xfer addr", inline=True)
comment(0x0450, "Enable Tube interrupt generation", inline=True)
comment(0x0453, "Look up Tube control bits for this xfer type", inline=True)
comment(0x045D, "Dummy R3 reads: flush for 2-byte transfers", inline=True)
comment(0x0463, "Trigger co-processor ack via R4", inline=True)
comment(0x046B, "R4 bit 7: co-processor acknowledged transfer", inline=True)
comment(0x046D, "Type 4 = SENDW (host-to-parasite word xfer)", inline=True)
comment(0x0471, "SENDW complete: release, sync, restart", inline=True)
comment(0x047D, "Release Tube NMI (transfer used interrupts)", inline=True)
# c0484: BEGIN — startup entry
comment(0x0484, "BEGIN: enable interrupts for Tube host code", inline=True)
comment(0x0489, "Z=1 from C=0 path: just acknowledge", inline=True)
comment(0x0490, "OSBYTE &FD: what type of reset was this?", inline=True)
comment(0x0496, "Soft break (X=0): re-init Tube and restart", inline=True)
comment(0x0498, "Claim address &FF (startup = highest prio)", inline=True)
# SENDW transfer loop: send ROM contents to co-processor page by page
comment(0x04A2, "R4 cmd 7: SENDW to send ROM to parasite", inline=True)
comment(0x04AB, "Send 256-byte page via R3, byte at a time", inline=True)
comment(0x04B0, "Timing delay: Tube data register needs NOPs", inline=True)
comment(0x04B6, "Increment 24-bit destination addr", inline=True)
comment(0x04C2, "Bit 6 set = all pages transferred", inline=True)
# sub_c04d2: initialise transfer pointers
comment(0x04D2, "Init: start sending from &8000", inline=True)
comment(0x04DA, "ROM type bit 5: reloc address in header?", inline=True)
comment(0x04E2, "Skip past copyright string to find reloc addr", inline=True)
comment(0x04EB, "Read 4-byte reloc address from ROM header", inline=True)

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
#   &04      2   &05F2  tube_osbyte_short (2-param, X result)
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
label(0x053D, "tube_release_return")  # Dead code (unreferenced)
label(0x0520, "tube_osbput")          # OSBPUT: read channel+byte from R2, call &FFD4
label(0x052D, "tube_osbget")          # OSBGET: read channel from R2, call &FFD7
label(0x0537, "tube_osrdch")          # OSRDCH: call &FFC8, send carry+byte reply
label(0x053A, "tube_rdch_reply")      # Send carry in bit 7 + data byte as reply
comment(0x053B, """\
Overlapping code: bytes &053B-&053D (20 95 06) are
JSR tube_send_r2 when falling through from ROR A
above. tube_release_return at &053D is dead code
so tube_release_return is now dead code.""")
comment(0x053B, "= JSR tube_send_r2 (overlaps &053D entry)", inline=True)
label(0x0542, "tube_osfind")          # OSFIND open: read arg+filename, call &FFCE
label(0x0552, "tube_osfind_close")    # OSFIND close: read handle, call &FFCE with A=0
label(0x055E, "tube_osargs")          # OSARGS: read handle+4 bytes+reason, call &FFDA
label(0x0562, "tube_read_params")     # Read parameter bytes from R2 into zero page
label(0x0582, "tube_read_string")     # Read CR-terminated string from R2 into &0700
label(0x0596, "tube_oscli")           # OSCLI: read command string, call &FFF7
label(0x059C, "tube_reply_ack")       # Send &7F acknowledge, return to main loop
label(0x059E, "tube_reply_byte")      # Poll R2, send byte in A, return to main loop
label(0x05A9, "tube_osfile")          # OSFILE: read 16 params+filename+reason, call &FFDD
# Dispatch table entry points (12 entries in 3.60, see table above)
for addr in [0x0537, 0x0596, 0x05F2, 0x0607, 0x0627, 0x0668,
             0x055E, 0x052D, 0x0520, 0x0542, 0x05A9, 0x05D1]:
    entry(addr)
# Additional entry points within page 5 (not dispatch entries)
entry(0x053D)  # tube_release_return (dead code, but structurally present)
# Page 5 inline comments
comment(0x0523, "Y=channel handle from R2", inline=True)
comment(0x0530, "Y=channel handle for OSBGET", inline=True)
comment(0x053A, "ROR A: encode carry (error flag) into bit 7", inline=True)
comment(0x0545, "A=0: close file, else open with filename", inline=True)
comment(0x0547, "Save open mode while reading filename", inline=True)
comment(0x0555, "Y=handle to close", inline=True)
comment(0x0561, "Y=file handle for OSARGS", inline=True)
comment(0x0562, "Read 4-byte arg + reason from R2 into ZP", inline=True)
comment(0x0567, "Params stored at &00-&03 (little-endian)", inline=True)
comment(0x0572, "Send result A back to co-processor", inline=True)
comment(0x0575, "Return 4-byte result from ZP &00-&03", inline=True)
comment(0x0584, "X=0, Y=0: buffer at &0700, offset 0", inline=True)
comment(0x058D, "Y overflow: string too long, truncate", inline=True)
comment(0x0593, "Y=7: set XY=&0700 for OSCLI/OSFIND", inline=True)
comment(0x059C, "&7F = success acknowledgement", inline=True)
comment(0x05A9, "Read 16-byte OSFILE control block from R2", inline=True)
comment(0x05B6, "XY=&0700: filename pointer for OSFILE", inline=True)
comment(0x05C2, "Send result A (object type) to co-processor", inline=True)
comment(0x05C5, "Return 16-byte control block to co-processor", inline=True)
comment(0x05D1, "Read 13-byte OSGBPB control block from R2", inline=True)
comment(0x05E3, "Save A (completion status) for later", inline=True)
comment(0x05E4, "Return 13-byte result block to co-processor", inline=True)

# Relocated code — page 6 (OSGBPB, OSBYTE, OSWORD, RDLN, event handler)
# Reference: NFS13 (GBPB, SBYTE, BYTE, WORD, RDLN, RDCHA, WRIFOR, ESCAPE, EVENT, ESCA)
# 3.35K label tube_osgbpb ($0602) — Tube code rewritten
# After JSR osgbpb, ROR A encodes carry into bit 7
# and sends it via tube_send_r2 BEFORE the 13 parameter bytes.
comment(0x0615, "Send carry result to co-processor", inline=True)
comment(0x0601, "Send X result for 2-param OSBYTE", inline=True)
comment(0x0607, "Read X, Y, A from R2 for 3-param OSBYTE", inline=True)
comment(0x0617, "OSBYTE &9D (fast Tube BPUT): no result needed", inline=True)
comment(0x0619, "Encode carry (error flag) into bit 7", inline=True)
comment(0x0622, "Send Y result, then fall through to send X", inline=True)
comment(0x0625, "BVS &05FC: overlapping code — loops back to"
        " page 5 R2 poll to send X after Y", inline=True)
comment(0x0627, "Overlapping entry: &20 = JSR c06c5 (OSWORD)", inline=True)
comment(0x0630, "Read param block length from R2", inline=True)
comment(0x0633, "DEX: length 0 means no params to read", inline=True)
comment(0x063E, "Store param bytes into block at &0128", inline=True)
comment(0x0644, "Restore OSWORD number from Y", inline=True)
comment(0x0645, "XY=&0128: param block address for OSWORD", inline=True)
comment(0x0651, "Read result block length from R2", inline=True)
comment(0x0655, "No results to send: return to main loop", inline=True)
comment(0x0657, "Send result block bytes from &0128 via R2", inline=True)
comment(0x0668, "Read 5-byte OSWORD 0 control block from R2", inline=True)
comment(0x0672, "X=0 after loop, A=0 for OSWORD 0 (read line)", inline=True)
comment(0x0679, "C=0: line read OK; C=1: escape pressed", inline=True)
comment(0x067B, "&FF = escape/error signal to co-processor", inline=True)
comment(0x0682, "&7F = line read successfully", inline=True)
comment(0x068E, "Loop until CR terminator sent", inline=True)
comment(0x06A7, "Check OS escape flag at &FF", inline=True)
comment(0x06A9, "SEC+ROR: put bit 7 of &FF into carry+bit 7", inline=True)
comment(0x06AB, "Escape set: forward to co-processor via R1", inline=True)
comment(0x06AD, "EVNTV: forward event A, Y, X to co-processor", inline=True)
comment(0x06AE, "Send &00 prefix (event notification)", inline=True)
label(0x0625, "tube_osbyte_short")    # OSBYTE 2-param: read X+A, call &FFF4, return X
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
entry(0x0625)
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
label(0x8EA7, "fs_osword_tbl_lo")      # Low bytes of FS OSWORD handler table
label(0x8EBD, "fs_osword_tbl_hi")      # High bytes of FS OSWORD handler table

# FS OSWORD handler routines
# osword_0f_handler label created by subroutine() call below.
label(0x8EF1, "read_args_size")        # READRB: get args buffer size from RX block offset &7F
# osword_10_handler label created by subroutine() call below.

# Econet TX/RX handler and OSWORD dispatch
label(0x8FE6, "store_16bit_at_y")     # Store 16-bit value at (nfs_workspace)+Y
# osword_dispatch label created by subroutine() call below.
label(0x9099, "osword_trampoline")     # PHA/PHA/RTS trampoline
label(0x90A4, "osword_tbl_lo")         # Dispatch table low bytes
label(0x90AD, "osword_tbl_hi")         # Dispatch table high bytes
# net_write_char label created by subroutine() call below.

# Remote operation function handlers (dispatched via osword_tbl)
# (net_write_char subroutine defined above)
label(0x913C, "match_osbyte_code")   # NCALLP: compare A against OSBYTE function table; Z=1 on match
label(0x9144, "return_match_osbyte") # Return from match_osbyte_code
label(0x84A0, "return_remote_cmd")   # Return from remote command data handler
label(0x84B5, "rchex")                # Clear JSR protection after remote command exec

# Control block setup
label(0x918C, "ctrl_block_setup_clv") # CLV entry: same setup but clears V flag

# Remote printer and display handlers (fn 1/2/3/5)

# Network transmit

# JSR buffer protection
label(0x92F0, "clear_jsr_protection") # CLRJSR: reset JSR buffer protection bits (4 refs)

# Palette/VDU state save
label(0x9308, "read_vdu_osbyte_x0")  # Read next VDU OSBYTE with X=0 parameter
label(0x930A, "read_vdu_osbyte")     # Read next OSBYTE from table, store result in workspace

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
label(0x81AF, "return_2")
label(0x82C2, "return_3")
label(0x857F, "return_4")
label(0x8D91, "return_5")
label(0x8E66, "return_6")
label(0x8EB7, "return_7")
label(0x9070, "return_8")
label(0x8D53, "return_9")
label(0x9994, "return_10")

# --- Service call handlers ---

label(0x81B5, "svc_4_star_command")     # Svc 4 dispatch entry (mid-routine in svc_star_command)

# --- Trampoline JMPs in page 6 relocated code (&06CE-&06D7) ---
# In 3.40 these were in main ROM at &9660; in 3.60 they fell inside the
# page 6 relocated block (source &9630, runtime &06CE).
label(0x06CE, "trampoline_tx_setup")    # JMP TX control block setup
label(0x06D1, "trampoline_adlc_init")   # JMP adlc_init
label(0x06D4, "svc_12_nmi_release")     # Svc 12: JMP save_econet_state
label(0x06D7, "svc_11_nmi_claim")       # Svc 11: JMP restore_econet_state
label(0x9679, "svc_5_unknown_irq")        # Svc 5: JMP unknown interrupt handler
entry(0x06CE)
entry(0x06D1)

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
#   *NET1 → index 33 → net_1_read_handle (&8E67)
#   *NET2 → index 34 → net_2_read_handle_entry (&8E6D)
#   *NET3 → index 35 → net_3_close_handle (&8E7D)
#   *NET4 → index 36 → net_4_resume_remote (&81BC)
# --- Filing system vector entry points ---
# Extended vector table entries set up at init (&8325):
#   FILEV → &870C    ARGSV → &8968    BGETV → &8563
#   BPUTV → &8413    GBPBV → &8A72    FINDV → &89D8
#   FSCV  → &80D4
# Labels and entry points for FSCV, FILEV, ARGSV, FINDV, GBPBV
# are created by subroutine() calls below in the comment sections.
label(0x8563, "bgetv_handler")          # BGETV entry: SEC then JSR handle_bput_bget
label(0x8413, "bputv_handler")          # BPUTV entry: CLC then fall into handle_bput_bget
entry(0x8563)
entry(0x8413)
entry(0x86DE)                            # Param block copy, falls through to parse_filename_gs
entry(0x870C)                            # Actual FILEV entry point (ROM pointer table target)

# --- Helper routines in header/init section ---
label(0x81E1, "cmd_name_matched")       # MATCH2: full name matched, check terminator byte
# 3.35K label skip_cmd_spaces ($81E4) — mapped to skpspi ($81E3) in 3.40
label(0x8339, "store_rom_ptr_pair")     # Write 2-byte address + ROM bank to ROM pointer table

# --- TX control block and FS command setup ---
label(0x83C8, "init_tx_ctrl_data")      # Init TX control block for data port (&90)
label(0x8389, "init_tx_ctrl_port")      # Init TX control block with port in A (2 JSR refs)
label(0x83B9, "prepare_cmd_with_flag")  # Prepare FS command with '*' flag and carry set
label(0x83BD, "prepare_cmd_clv")        # Prepare FS command with V cleared
# prepare_fs_cmd and build_send_fs_cmd labels created by subroutine() calls below.
label(0x83C8, "prepare_fs_cmd_v")       # Prepare FS command, V flag preserved
label(0x83F3, "send_fs_reply_cmd")      # Send FS command with reply processing

# --- Byte I/O and escape ---
# handle_bput_bget label created by subroutine() call below.
label(0x8441, "store_retry_count")      # RAND1: store retry count to &0FDD, initiate TX
label(0x8498, "update_sequence_return") # RAND3: update sequence numbers and pull A/Y/X/return
label(0x8514, "set_listen_offset")      # NLISN2: use reply code as table offset for listen
label(0x8533, "send_to_fs_star")        # Send '*' command to fileserver
label(0x8559, "fs_wait_cleanup")        # WAITEX: tidy stack, restore rx_status_flags

# --- Pointer arithmetic helpers ---
label(0x883B, "add_5_to_y")             # INY * 5; RTS
label(0x883C, "add_4_to_y")             # INY * 4; RTS
label(0x884E, "sub_4_from_y")           # DEY * 4; RTS
label(0x884F, "sub_3_from_y")           # DEY * 3; RTS

# --- Error messages and data tables ---
label(0x81D2, "clear_osbyte_ce_cf")     # Reset OSBYTE &CE/&CF intercept masks to &7F (restore MOS vectors)

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
label(0x85EC, "access_bit_table")       # Lookup table for attribute bit mapping (11 bytes)

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
label(0x86CA, "return_compare")          # Return from compare_addresses (not equal)

# --- FSCV 7: read FS handles ---
label(0x86CB, "fscv_7_read_handles")      # Return X=&20 (base handle), Y=&27 (top handle)
label(0x86CF, "return_fscv_handles")    # Return from fscv_7_read_handles

# --- FS flags manipulation ---
label(0x86DA, "store_fs_flag")           # Shared STA fs_eof_flags / RTS for set/clear_fs_flag

# --- File info display (hex print helpers moved to &8Dxx) ---
# pad_filename_spaces and print_exec_and_len deleted in 3.60;
# catalogue display restructured to use server-formatted strings.
label(0x8D70, "print_hex_bytes")        # Print X bytes from (fs_options)+Y as hex (high->low)
label(0x8D7B, "print_space")            # Print a space character via OSASCI

# --- TX control and transmission ---
label(0x8601, "tx_poll_timeout")        # Transmit with Y=&60 (specified timeout)
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
label(0x88FB, "get_file_protection")  # CHA1: decode attribute byte for protection status
label(0x8910, "copy_filename_to_cmd") # CHASK2: copy filename string into FS command buffer
label(0x894D, "copy_fs_reply_to_cb")  # COPYFS: copy FS reply buffer data to control block

# --- Common return point (&8952) ---
label(0x8999, "save_args_handle")      # SETARG: save handle for OSARGS operation

# --- FSCV 0: *OPT handler (&89CA) ---
label(0x8A1A, "close_single_handle")   # CLOSE1: send close command for specific handle to FS

# --- Address adjustment helpers (&89EE-&8A0E) ---
label(0x8A52, "adjust_addrs_9")        # Adjust 4-byte addresses at param block offset 9
label(0x8A57, "adjust_addrs_1")        # Adjust 4-byte addresses at param block offset 1
label(0x8A59, "adjust_addrs_clc")      # CLC entry: clear carry before address adjustment
label(0x8B7F, "copy_reply_to_caller") # Copy FS reply data to caller buffer (direct or via Tube)
label(0x8C13, "tube_claim_loop")      # TCLAIM: claim Tube with &C3, retry until acquired

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
label(0x8D47, "print_reply_bytes")
label(0x8D49, "print_reply_counted")
label(0x8D86, "copy_string_from_offset") # COPLP1: sub-entry of copy_string_to_cmd with caller-supplied Y offset

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
label(0x96EA, "scout_reject")          # Reject: wrong network (RX_DISCONTINUE)
label(0x970B, "scout_discard")         # Clean discard via &99E8
label(0x9713, "scout_loop_rda")        # Scout data loop: check RDA
label(0x9723, "scout_loop_second")     # Scout data loop: read second byte of pair
label(0x975E, "scout_no_match")        # Scout port/station mismatch (3 refs)
label(0x9761, "scout_match_port")      # Port non-zero: look for matching RX block

# --- Data frame RX (inbound four-way handshake) ---
label(0x97DC, "data_rx_setup")         # Switch to RX mode, install data RX handler
label(0x97FA, "nmi_data_rx_net")       # Data frame: validate dest_net = 0
label(0x9810, "nmi_data_rx_skip")      # Data frame: skip ctrl/port (already from scout)
label(0x983D, "rx_error")              # RX error dispatcher (13 refs -- most referenced!)
label(0x983D, "rx_error_reset")        # Full reset and discard
label(0x98A0, "nmi_data_rx_tube")      # Data frame: Tube co-processor variant

# --- Data frame completion and FV validation ---
label(0x98C3, "data_rx_tube_complete") # Tube data frame completion
label(0x98C0, "data_rx_tube_error")    # Tube data frame error (3 refs)

# --- ACK transmission ---
label(0x98F9, "ack_tx_configure")      # Configure CR1/CR2 for TX
label(0x9907, "ack_tx_write_dest")     # Write dest addr to TX FIFO

# --- Discard and idle ---

# --- TX path ---
label(0x9C11, "tx_active_start")       # Begin TX (CR1=&44)
label(0x9CF2, "tx_error")              # TX error path

# --- RX reply scout (outbound handshake) ---
# 3.35K label reply_error ($9DED) — mapped to tx_result_fail ($9F1A) in 3.40

# --- TX scout ACK + data phase ---
label(0x9DB3, "data_tx_begin")         # Begin data frame TX
label(0x9DF5, "data_tx_last")          # TX_LAST_DATA for data frame (5 refs)
label(0x9E06, "data_tx_error")         # Data TX error (5 refs)
label(0x9E06, "install_saved_handler") # Install handler from &0D4B/&0D4C
label(0x9E0F, "nmi_data_tx_tube")      # NMI: send data from Tube

# --- Four-way handshake: RX final ACK ---
label(0x9E70, "nmi_final_ack_net")     # Read dest_net, validate

# --- Completion and error ---
label(0x9EAC, "tx_result_fail")        # Store result=&41 (not listening) (9 refs)

# --- NMI shim at end of ROM ---
label(0x9F3C, "nmi_shim_rom_src")      # Source for 32-byte copy to &0D00
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
label(0x815F, "cloop")                # NFS01: copy loop (page copy)
label(0x81FC, "initl")                # NFS01: init loop
label(0x81E7, "skpspi")               # NFS01: skip SPI

# --- FS command dispatch (&82xx-&83xx) ---
label(0x8250, "dofsl1")               # NFS03: do FS loop 1
label(0x8353, "fsdiel")               # NFS01: FS die loop
label(0x8398, "fstxl1")               # NFS03: FS TX loop 1
label(0x83A8, "fstxl2")               # NFS03: FS TX loop 2
label(0x83FB, "dofsl7")               # NFS03: do FS loop 7
label(0x8407, "return_dofsl7")        # NFS03: return from FS loop 7
label(0x8408, "dofsl5")               # NFS03: do FS loop 5
label(0x8452, "error1")               # NFS03: error handler 1

# --- Net list / pointer arithmetic (&84xx-&85xx) ---
label(0x8510, "nlistn")               # NFS03: net list entry
label(0x8512, "nlisne")               # NFS03: net list next entry
label(0x8546, "incpx")                # NFS04: increment pointer X
label(0x86A4, "y2fsl5")               # NFS04: Y-to-FS loop 5
label(0x86AA, "y2fsl2")               # NFS04: Y-to-FS loop 2
label(0x86B9, "fs2al1")               # NFS04: FS-to-A loop 1

# --- Number formatting and file info (&86xx) ---
label(0x8D72, "num01")                # NFS07: number print entry
label(0x861D, "l4")                   # NFS03: net TX polling loop
label(0x86E0, "file1")                # NFS05: FILEV entry 1
label(0x86F2, "quote1")               # NFS05: filename quote loop
label(0x871D, "loadop")               # NFS05: load operation
label(0x873A, "lodfil")               # NFS05: load file

# --- FILEV, load/save size (&87xx) ---
label(0x875A, "floop")                # NFS01: FS loop
label(0x8784, "lodchk")               # NFS05: load check
label(0x878F, "return_lodchk")        # NFS05: return from load check
label(0x8790, "saveop")               # NFS05: save operation
label(0x8799, "savsiz")               # NFS05: save size handling
label(0x8831, "lodrl1")               # NFS05: load reply loop 1
label(0x8844, "lodrl2")               # NFS05: load reply loop 2
label(0x8879, "savchk")               # NFS05: save check

# --- Channel/attribute handling (&88xx-&89xx) ---
label(0x88EE, "chalp1")               # NFS05: channel loop 1
label(0x8905, "chalp2")               # NFS05: channel loop 2
label(0x8917, "cha6")                  # NFS05: channel handler 6
label(0x8926, "cha4")                  # NFS05: channel handler 4
label(0x8930, "cha5")                  # NFS05: channel handler 5
label(0x895A, "cha5lp")               # NFS05: channel 5 loop
label(0x89C8, "osarg1")               # NFS05: OSARGS handler 1
label(0x8A3E, "opter1")               # NFS05: *OPT error 1
label(0x8A43, "optl1")                # NFS05: *OPT loop 1

# --- GBPB handler (&89xx-&8Axx) ---
label(0x8A6B, "gbpbx")                # NFS05: GBPB dispatch
label(0x8AA2, "gbpbx0")               # NFS05: GBPB dispatch 0
label(0x8A80, "gbpbx1")               # NFS05: GBPB dispatch 1
label(0x8A8B, "gbpbe1")               # NFS05: GBPB EOF 1
label(0x8A97, "gbpbf1")               # NFS05: GBPB forward 1
label(0x8AA2, "gbpbf2")               # NFS05: GBPB forward 2
label(0x8AAB, "gbpbl1")               # NFS05: GBPB loop 1
label(0x8ACD, "gbpbl3")               # NFS05: GBPB loop 3
label(0x8AE4, "gbpbf3")               # NFS05: GBPB forward 3

# --- *INFO and decimal print (&8Axx-&8Bxx) ---
label(0x8B41, "info2")                # NFS06: *INFO loop 2
label(0x8BA6, "tbcop1")               # NFS06: Tube copy loop 1
label(0x8C26, "decfir")               # NFS07: decimal first digit
label(0x8C28, "decmor")               # NFS07: decimal more digits
label(0x8C34, "decmin")               # NFS07: decimal minimum

# --- Logon and *NET (&8Dxx) ---
label(0x8E3D, "logon2")               # NFS07: logon handler 2
label(0x8F2A, "logon3")               # NFS07: logon handler 3
label(0x8D98, "print_dir_from_offset") # INFOLP: sub-entry of fsreply_0_print_dir with caller-supplied X offset
label(0x8D82, "infol2")               # NFS07: info loop 2

# --- File I/O: save, read, open (&8Dxx-&8Fxx) ---
label(0x8E78, "rxpol2")               # NFS08: RX poll loop 2
label(0x8EAA, "save1")                # NFS08: save handler 1
# copyl3 label deleted in 3.60; dispatch table restructured.
label(0x8EFC, "readry")               # NFS08: read ready
label(0x8F2B, "rssl1")                # NFS08: read size/status loop 1
label(0x8F36, "rssl2")                # NFS08: read size/status loop 2
label(0x8F46, "rsl1")                 # NFS08: read status loop 1
label(0x8F70, "readc1")               # NFS08: read char 1
label(0x8F8D, "scan0")                # NFS08: scan entry 0
label(0x8FA1, "scan1")                # NFS08: scan entry 1
label(0x8FBD, "openl6")               # NFS08: open loop 6
label(0x8FCA, "openl7")               # NFS08: open loop 7
label(0x8FCF, "openl4")               # NFS08: open loop 4
# 3.35K label rest1 ($8FC1) — data block removed in 3.40
label(0x8FF6, "dofs01")               # NFS08: do FS 01
label(0x9071, "dofs2")                # NFS08: do FS 2

# --- OSWORD and remote ops (&90xx-&91xx) ---
label(0x9092, "entry1")               # NFS09: OSWORD entry 1
label(0x910A, "nbyte6")               # NFS09: net byte handler 6
label(0x910C, "nbyte1")               # NFS09: net byte handler 1
label(0x9130, "nbyte4")               # NFS09: net byte handler 4
label(0x9134, "nbyte5")               # NFS09: net byte handler 5
label(0x913B, "return_nbyte")         # NFS09: return from net byte handler
label(0x84B8, "remot1")               # NFS03: remote handler 1
label(0x918D, "cbset2")               # NFS09: control block set 2
label(0x91A4, "cbset3")               # NFS09: control block set 3
label(0x91AA, "cbset4")               # NFS09: control block set 4
label(0x91E7, "setup1")               # NFS09: setup 1
label(0x91E9, "return_printer_select") # NFS09: return from printer_select_handler
label(0x91F9, "prlp1")                # NFS09: printer loop 1

# --- Broadcast/station search (&92xx) ---
label(0x9272, "bsxl1")                # NFS09: broadcast search loop 1
label(0x928F, "bspsx")                # NFS09: broadcast search parse exit
label(0x9297, "bsxl0")                # NFS09: broadcast search loop 0
label(0x92AA, "return_bspsx")         # NFS09: return from broadcast search area

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
  &96BF: RX scout (idle listen, default handler)
  &9BD6: INACTIVE polling (pre-TX, waits for idle line)
  &9CCC: TX data (2 bytes per NMI, tight loop if IRQ persists)
  &9D08: TX_LAST_DATA (close frame)
  &9D14: TX completion (switch to RX: CR1=&82)
  &9D30: RX reply scout (check AP, read dest_stn)
  &9D44: RX reply continuation (read dest_net, validate)
  &9D5B: RX reply validation (read src_stn/net, check FV)
  &9DA3: TX scout ACK (write dest/src addr, TX_LAST_DATA)
  &9E50: Four-way handshake data phase

NMI handler chain for inbound reception (scout -> data):
  &96BF: RX scout (idle listen)
  &96DC: RX scout second byte (dest_net, install &970E)
  &970E: Scout data loop (read body in pairs, detect FV)
  &9738: Scout completion (disable PSE, read last byte)
  &98EE: TX scout ACK
  &97E6: RX data frame (AP check, validate dest_stn/net)
  &9843: RX data bulk read (read payload into buffer)
  &9877: RX data completion (disable PSE, check FV, read last)
  &98EE: TX final ACK

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
    rts_code_ptr(0x8EB8 + i, 0x8EBD + i)

# ============================================================
# NMI handler chain entry points
# ============================================================
# These are installed via self-modifying JMP at &0D0C/&0D0D,
# so py8dis cannot trace them automatically.

# --- ADLC init and idle listen ---
entry(0x96B9)   # ADLC init / reset entry
entry(0x96BF)   # RX scout (idle listen) - default NMI handler

# --- TX path: polling, data, completion ---
entry(0x9BD6)   # INACTIVE polling loop (pre-TX)
entry(0x9CCC)   # NMI TX data handler (2 bytes per NMI)
entry(0x9CF2)   # TX error path
entry(0x9D08)   # TX_LAST_DATA and frame completion
entry(0x9D14)   # TX completion: switch to RX mode

# --- RX reply handlers ---
entry(0x9D30)   # RX reply scout handler
entry(0x9D44)   # RX reply continuation handler
entry(0x9D5B)   # RX reply next handler

# --- Four-way handshake (outbound data phase) ---
entry(0x9E50)   # Four-way handshake: switch to RX for final ACK
entry(0x9E5C)   # Four-way handshake: RX final ACK (check AP, dest_stn)
entry(0x9E70)   # Four-way handshake: RX final ACK continuation (dest_net=0)

# --- Completion / error ---
entry(0x9EA8)   # Completion handler (store result=0 to tx_block)
entry(0x9EAE)   # Error handler (store error code to tx_block)
entry(0x9E84)   # Four-way handshake: validate final ACK src addr

# --- Discovered via JMP &0D0E scan (NMI handler installations) ---
entry(0x96DC)   # RX scout second byte handler (dest network)
entry(0x970E)   # Scout data reading loop (reads body in pairs)
entry(0x97E6)   # Data frame RX handler (four-way handshake)
entry(0x97FA)   # Data frame: validate source network = 0
entry(0x9810)   # Data frame: skip ctrl/port bytes
entry(0x9843)   # Data frame: bulk data read loop
entry(0x98A0)   # Data frame: Tube co-processor RX handler
entry(0x9925)   # ACK TX continuation (write src addr, TX_LAST_DATA)

# --- NMI shim at end of ROM (&9FD9-&9FFF) ---
# Bootstrap NMI handler and ROM copies of workspace routines.
# &9FD9 is the source for the 32-byte copy to &0D00 by install_nmi_shim.
entry(0x9F7D)   # Bootstrap NMI entry (hardcoded JMP nmi_rx_scout, no self-mod)
entry(0x9F8B)   # ROM copy of set_nmi_vector + nmi_rti
# entry(0x9FFA) — removed: code at $9FFA runs off ROM end ($9FFF STA truncated)

# --- Data RX NMI handlers (four-way handshake data phase) ---
entry(0x9DA3)   # Data phase RX first byte
entry(0x9DC8)   # Data phase RX continuation
entry(0x9E0F)   # Data phase RX bulk transfer

# ============================================================
# Additional known entry points
# ============================================================
entry(0x822C)
entry(0x824B)
entry(0x824D)
entry(0x81B0)   # Auto-boot/service handler (NOP pad + LDX #&0C; JSR)
entry(0x8284)   # Issue vectors claimed handler (JSR osbyte)
entry(0x8371)   # TX control block string copy loop tail
entry(0x86CB)   # FSCV read handles (LDX #&20; LDY #&27; RTS)
entry(0x8D40)   # Boot option dispatch (PLA; CLC; ADC zp)
entry(0x8DDC)   # fscv_2_star_run: FSCV 2/4 handler (JSR parse_filename_gs)
entry(0x8E67)   # Read handle entry (LDY #&6F; LDA (nfs_workspace),Y)
entry(0x91A8)   # Control block setup loop tail
entry(0x9315)   # Read VDU OSBYTE (JSR osbyte; TXA; LDX #0)
entry(0x9639)   # NMI claim trampolines (JMP; JMP)
entry(0x9679)   # svc_5_unknown_irq: JMP to IRQ service
entry(0x9995)   # Econet RX immediate-operation handler
entry(0x9AE7)   # ACK/reply handler: store source station, configure VIA
entry(0x06DA)   # IRQ service: check CB1, dispatch TX done handlers

# ============================================================
# Code regions identified by manual inspection of equb data
# ============================================================
# These are preceded by RTS and start with valid opcodes, but
# are not reachable via JSR/JMP from already-traced code (their
# callers are themselves in equb regions -- cascading resolution).

entry(0x883B)   # INY*5; RTS (pointer arithmetic helper)
entry(0x884E)   # DEY*4; RTS (pointer arithmetic helper)
entry(0x8853)   # PHA; JSR ... (called from &878A and &8A6C)
entry(0x88D1)   # STA abs; CMP#; ... (called from &8744)
entry(0x89C0)   # TAY; BNE; ... (preceded by RTS, standalone entry)
entry(0x8A72)   # JSR &85A6; ... (preceded by RTS, standalone entry)
# entry(0x8E34) created by subroutine() call below
entry(0x90E8)   # LDY zp; CMP#; ... (preceded by RTS, standalone entry)
entry(0x996F)   # Post-ACK: process received scout (check port, match RX block)

# --- Econet TX/RX handler and OSWORD dispatch (&8FE5-&90B8) ---
# &8FE5: Main transmit/receive handler entry (A=0: set up and send, A>=1: handle result)
# &9074: OSWORD-style dispatch handler (function codes 0-8, PHA/PHA/RTS)
entry(0x8FF0)   # Econet TX/RX handler (CMP #1; BCS)
# entry(0x9008) and entry(0x903E) created by subroutine() calls below
entry(0x9099)   # Dispatch trampoline (PHA/PHA/RTS into table at &90A4/&90AD)

# Dispatch table at &90A4 (low bytes) / &90AD (high bytes)
# 9 entries for function codes 0-8, used via PHA/PHA/RTS at &9099.
for i in range(9):
    rts_code_ptr(0x90A4 + i, 0x90AD + i)

# ============================================================
# Immediate operation dispatch table at &9A04/&9A0C
# ============================================================
# Used by the PHA/PHA/RTS dispatch at &9A66 (immediate_op handler).
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
# Y-indexed dispatch table deleted in 3.60; replaced by
# single-table pattern (constant hi byte + lo table).

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
# Y-indexed dispatch table deleted in 3.60; replaced by
# single-table pattern (constant hi byte + lo table).

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
# Y-indexed dispatch table deleted in 3.60; replaced by
# single-table pattern (constant hi byte + lo table).

# ============================================================
# Immediate operation RX handler labels (&9AB5-&9AF1)
# ============================================================
# Targets of dispatch table 1 at &9A24/&9A2C.
# These handle incoming immediate operations (PEEK, POKE, JSR,
# UserProc, OSProc, machine type query) received from the network.

label(0x9A45, "return_inc_port_buf")

label(0x9A80, "rx_imm_exec")
subroutine(0x9A80, hook=None,
    title="RX immediate: JSR/UserProc/OSProc setup",
    description="""\
Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace at &0D58, then jumps to
the common receive path at c9826. Used for operation types
&83 (JSR), &84 (UserProc), and &85 (OSProc).""")

label(0x9A9F, "rx_imm_poke")
subroutine(0x9A9F, hook=None,
    title="RX immediate: POKE setup",
    description="""\
Sets up workspace offsets for receiving POKE data.
port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
the common data-receive path at c9805.""")

label(0x9AAA, "rx_imm_machine_type")
subroutine(0x9AAA, hook=None,
    title="RX immediate: machine type query",
    description="""\
Sets up a buffer at &7F21 (length #&01FC) for the machine
type query response, then jumps to the query handler at
c9b0f. Returns system identification data to the remote
station.""")

label(0x9ABC, "rx_imm_peek")
subroutine(0x9ABC, hook=None,
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

label(0x9B25, "tx_done_jsr")
subroutine(0x9B25, hook=None,
    title="TX done: remote JSR execution",
    description="""\
Pushes address &9BEB on the stack (so RTS returns to
tx_done_exit), then does JMP (l0d58) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")

label(0x9B2E, "tx_done_user_proc")
subroutine(0x9B2E, hook=None,
    title="TX done: UserProc event",
    description="""\
Generates a network event (event 8) via OSEVEN with
X=l0d58, A=l0d59 (the remote address). This notifies
the user program that a UserProc operation has completed.""")

label(0x9B3C, "tx_done_os_proc")
subroutine(0x9B3C, hook=None,
    title="TX done: OSProc call",
    description="""\
Calls the ROM entry point at &8000 (rom_header) with
X=l0d58, Y=l0d59. This invokes an OS-level procedure
on behalf of the remote station.""")

label(0x9B48, "tx_done_halt")
subroutine(0x9B48, hook=None,
    title="TX done: HALT",
    description="""\
Sets bit 2 of rx_flags (&0D64), enables interrupts, and
spin-waits until bit 2 is cleared (by a CONTINUE from the
remote station). If bit 2 is already set, skips to exit.""")

label(0x9B5F, "tx_done_continue")
subroutine(0x9B5F, hook=None,
    title="TX done: CONTINUE",
    description="""\
Clears bit 2 of rx_flags (&0D64), releasing any station
that is halted and spinning in tx_done_halt.""")

label(0x9B67, "tx_done_exit")

# ============================================================
# TX ctrl byte handler labels (&9CF7-&9D54)
# ============================================================
# Targets of dispatch table 3 at &9C62/&9C6A.
# Called to set up the scout control byte and transfer
# parameters for outbound immediate operations.

label(0x9C6F, "tx_ctrl_peek")
subroutine(0x9C6F, hook=None,
    title="TX ctrl: PEEK transfer setup",
    description="""\
Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace at &0D1E-&0D21 (with carry propagation).
Calls tx_calc_transfer to finalise, then exits via
tx_ctrl_exit.""")

label(0x9C73, "tx_ctrl_poke")
subroutine(0x9C73, hook=None,
    title="TX ctrl: POKE transfer setup",
    description="""\
Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")

label(0x9C87, "tx_ctrl_proc")
subroutine(0x9C87, hook=None,
    title="TX ctrl: JSR/UserProc/OSProc setup",
    description="""\
Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

label(0x9CC5, "tx_ctrl_exit")

# Alternate entry into ctrl_block_setup (&9171)
entry(0x917F)   # ADLC setup: LDX #&0D; LDY #&7C; BIT &833B; BVS c9167

# Dispatch targets found in equb data regions
# These are the bodies of the econet function dispatch handlers.
# Functions 1-3 share a handler (&91D4) — possibly different
# sub-operations that share setup logic. Function 5 (&91C4) and
# function 8 (&9142) are distinct. The exact purpose of each
# function code hasn't been fully determined yet.
entry(0x91EA)   # Function 1/2/3 handler (shared)
entry(0x915C)   # Function 8 handler (remote_cmd_data)

# --- Code found in third-pass remaining equb regions ---
entry(0x8790)   # BEQ +3; JMP &8870 (called from &8744 region)
entry(0x8FD5)   # LDY #&28; ... (preceded by RTS, standalone entry)
entry(0x97DC)   # LDA #&82; STA &FEA0; installs NMI handler &97E6

# ============================================================
# Inline comments for key instructions
# ============================================================
# Note: acorn.bbc()'s hooks auto-annotate OSBYTE/OSWORD calls, so
# we only add comments where the auto-annotations don't reach.

# ============================================================
# Save FSCV arguments (&859C)
# ============================================================
entry(0x8649)
subroutine(0x8649, "save_fscv_args_with_ptrs", hook=None,
    title="Save FSCV arguments with text pointers",
    description="""\
Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
falls through to save_fscv_args to store A/X/Y in the FS
workspace.""")
comment(0x8649, "Set os_text_ptr low = X", inline=True)
comment(0x864B, "Set os_text_ptr high = Y", inline=True)

subroutine(0x864D, "save_fscv_args", hook=None,
    title="Save FSCV/vector arguments",
    description="""\
Stores A, X, Y into the filing system workspace. Called at the
start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
  &BD (fs_last_byte_flag) = A (function code / command)
  &BB (fs_options)        = X (control block ptr low)
  &BC (fs_block_offset)   = Y (control block ptr high)
  &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)""")
comment(0x8657, "Clear escapable flag, preserving processor flags", inline=True)

# ============================================================
# Attribute decoding (&85B1 / &85BB)
# ============================================================
subroutine(0x85CF, "decode_attribs_6bit", hook=None,
    title="Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)",
    description="""\
Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&85EC. The two formats use different bit layouts for file
protection attributes.""")
comment(0x85D5, "X=4: skip first 4 table entries (BBC→FS half)", inline=True)

subroutine(0x85D9, "decode_attribs_5bit", hook=None,
    title="Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)",
    description="""\
Masks A to 5 bits and builds an access bitmask via the
lookup table at &85EC. Each input bit position maps to a
different output bit via the table. The conversion is done
by iterating through the source bits and OR-ing in the
corresponding destination bits from the table, translating
between BBC (8-bit) and fileserver (5-bit) protection formats.""")
comment(0x85DB, "X=&FF: INX makes 0; start from table index 0", inline=True)
comment(0x85DD, "Temp storage for source bitmask to shift out", inline=True)
comment(0x85E2, "Shift out source bits one at a time", inline=True)
comment(0x85E6, "OR in destination bit from lookup table", inline=True)


# ============================================================
# Decimal number parser (&8620)
# ============================================================
subroutine(0x8677, "parse_decimal",
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
comment(0x8677, "Zero accumulator", inline=True)
comment(0x867B, "Load next char from buffer", inline=True)
comment(0x867D, "Dot separator?", inline=True)
comment(0x867F, "Yes: exit with C=1 (dot found)", inline=True)
comment(0x8681, "Control char or space: done", inline=True)
comment(0x8683, "Mask ASCII digit to 0-9", inline=True)
comment(0x8685, "Save new digit", inline=True)
comment(0x8687, "Running total * 2", inline=True)
comment(0x8689, "A = running total * 2", inline=True)
comment(0x868B, "A = running total * 4", inline=True)
comment(0x868C, "A = running total * 8", inline=True)
comment(0x868D, "+ total*2 = total * 10", inline=True)
comment(0x868F, "+ digit = total*10 + digit", inline=True)
comment(0x8691, "Store new running total", inline=True)
comment(0x8693, "Advance to next char", inline=True)
comment(0x8694, "Loop (always: Y won't wrap to 0)", inline=True)
comment(0x8696, "No dot found: C=0", inline=True)
comment(0x8697, "Return result in A", inline=True)

# ============================================================
# File handle conversion (&8643-&8645)
# ============================================================
subroutine(0x869A, "handle_to_mask_a", hook=None,
    title="Convert handle in A to bitmask",
    description="""\
Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""")
comment(0x869A, "Handle number to Y for conversion", inline=True)

subroutine(0x869B, "handle_to_mask_clc", hook=None,
    title="Convert handle to bitmask (carry cleared)",
    description="""\
Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""")

subroutine(0x869C, "handle_to_mask",
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
comment(0x869C, "Save A (will be restored on exit)", inline=True)
comment(0x869D, "Save X (will be restored on exit)", inline=True)
comment(0x869E, "  (second half of X save)", inline=True)
comment(0x869F, "A = handle from Y", inline=True)
comment(0x86A0, "C=0: always convert", inline=True)
comment(0x86A2, "C=1 and Y=0: skip (handle 0 = none)", inline=True)
comment(0x86A4, "C=1 and Y!=0: convert", inline=True)
comment(0x86A5, "A = handle - &1F (1-based bit position)", inline=True)
comment(0x86A7, "X = shift count", inline=True)
comment(0x86A8, "Start with bit 0 set", inline=True)
comment(0x86AA, "Shift bit left", inline=True)
comment(0x86AB, "Count down", inline=True)
comment(0x86AC, "Loop until correct position", inline=True)
comment(0x86AE, "Undo final extra shift", inline=True)
comment(0x86AF, "Y = resulting bitmask", inline=True)
comment(0x86B0, "Non-zero: valid mask, skip to exit", inline=True)
comment(0x86B2, "Zero: invalid handle, set Y=&FF", inline=True)
comment(0x86B3, "Restore X", inline=True)
comment(0x86B5, "Restore A", inline=True)

# ============================================================
# Mask to handle (&8638)
# ============================================================
subroutine(0x86B7, "mask_to_handle",
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
comment(0x86B7, "X = &1F (handle base - 1)", inline=True)
comment(0x86B9, "Count this bit position", inline=True)
comment(0x86BA, "Shift mask right; C=0 when done", inline=True)
comment(0x86BB, "Loop until all bits shifted out", inline=True)
comment(0x86BD, "A = X = &1F + bit position = handle", inline=True)

# ============================================================
# Print decimal number (&8D7E)
# ============================================================
subroutine(0x8DBD, "print_decimal", hook=None,
    title="Print byte as 3-digit decimal number",
    description="""\
Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""",
    on_entry={"a": "byte value to print"},
    on_exit={"a": "last digit character",
             "x": "corrupted",
             "y": "0 (remainder after last division)"})

subroutine(0x8DCA, "print_decimal_digit", hook=None,
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
subroutine(0x86BF, "compare_addresses",
    title="Compare two 4-byte addresses",
    description="""\
Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
Used by the OSFILE save handler to compare the current
transfer address (&C8-&CB, copied to &B0) against the end
address (&B4-&B7) during multi-block file data transfers.""",
    on_exit={"a": "corrupted (EOR result)",
             "x": "corrupted",
             "y": "preserved"})
comment(0x86BF, "Compare 4 bytes (index 4,3,2,1)", inline=True)
comment(0x86C1, "Load byte from first address", inline=True)
comment(0x86C3, "XOR with corresponding byte", inline=True)
comment(0x86C5, "Mismatch: Z=0, return unequal", inline=True)
comment(0x86C8, "Continue comparing", inline=True)
comment(0x86CB, "X=first handle (&20)", inline=True)
comment(0x86CD, "Y=last handle (&27)", inline=True)

# ============================================================
# FS flags (&8651 / &8659)
# ============================================================
subroutine(0x86D0, "set_fs_flag", hook=None,
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
comment(0x86D0, "Merge new bits into flags", inline=True)
comment(0x86D3, "Store updated flags (always taken)", inline=True)

subroutine(0x86D5, "clear_fs_flag", hook=None,
    title="Clear bit(s) in FS flags (&0E07)",
    description="""\
Inverts A (EOR #&FF), then ANDs the result into fs_eof_flags
to clear the specified bits.""")
comment(0x86D5, "Invert mask: set bits become clear bits", inline=True)
comment(0x86D7, "Clear specified bits in flags", inline=True)
comment(0x86DA, "Write back updated flags", inline=True)

# ============================================================
# Print file info — deleted in 3.60
# ============================================================
# print_file_info, pad_filename_spaces, and print_exec_and_len
# were deleted; catalogue display restructured to use
# server-formatted strings (new-format FS only).

# ============================================================
# Hex printing (&9FE0 / &9FE9)
# ============================================================
# Moved to end of ROM and rewritten in 3.40 (was at &8D9D in
# 3.35K). The new routine uses CMP #&0A / ADC #6 / ADC #&30
# instead of ORA #&30 / CMP #&3A / ADC #6, and explicitly
# calls OSASCI before returning (self-contained, no fall-through).
label(0x9F9D, "print_hex")
subroutine(0x9F9D, hook=None,
    title="Print byte as two hex digits",
    description="""\
Prints the high nibble first (via 4x LSR), then the low
nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
and output via OSASCI. Returns with carry set.""")

label(0x9FA6, "print_hex_nibble")
subroutine(0x9FA6, hook=None,
    title="Print single hex nibble",
    description="""\
Converts the low nibble of A to ASCII hex ('0'-'9' or 'A'-'F')
and prints via OSASCI. Returns with carry set.""")
comment(0x9FAC, "A-F: ADC #6 + ADC #&30 + C = &41-&46", inline=True)
comment(0x9FB0, "Write character", inline=True)
comment(0x9FB3, "C=1: callers use SEC as sentinel", inline=True)

# ============================================================
# TX control (&8660-&866C)
# ============================================================
subroutine(0x85F7, "setup_tx_ptr_c0", hook=None,
    title="Set up TX pointer to control block at &00C0",
    description="""\
Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""")
comment(0x85F7, "TX control block low byte", inline=True)
comment(0x85F9, "Set net_tx_ptr = &00C0", inline=True)
comment(0x85FB, "TX control block high byte", inline=True)
comment(0x85FD, "Set net_tx_ptr+1 = &00", inline=True)

subroutine(0x85FF, "tx_poll_ff", hook=None,
    title="Transmit and poll for result (full retry)",
    description="""\
Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""")

subroutine(0x8603, "tx_poll_core",
    title="Core transmit and poll routine (XMIT)",
    description="""\
Claims the TX semaphore (tx_clear_flag) via ASL -- a busy-wait
spinlock where carry=0 means the semaphore is held by another
operation. Only after claiming the semaphore is the TX pointer
copied to nmi_tx_block, ensuring the low-level transmit code
sees a consistent pointer. Then calls the ADLC TX setup routine
and polls the control byte for completion:
  bit 7 set = still busy (loop)
  bit 6 set = error (check escape or report)
  bit 6 clear = success (clean return)
On error, checks for escape condition and handles retries.
Two entry points: setup_tx_ptr_c0 (&85F7) always uses the
standard TXCB; tx_poll_core (&8603) is general-purpose.""",
    on_entry={"a": "retry count (&FF = full retry)",
              "y": "timeout parameter (&60 = standard)"},
    on_exit={"a": "entry A (retry count, restored from stack)",
             "x": "0",
             "y": "0"})
comment(0x8603, "Save retry count and timeout on stack", inline=True)
comment(0x8608, "Read control byte from TX block", inline=True)
comment(0x860A, "Write back control byte (re-arm for TX)", inline=True)
comment(0x860D, "Spin until TX semaphore is free (C=1)", inline=True)
comment(0x8612, "Copy TX pointer to NMI block while locked", inline=True)
comment(0x861A, "Initiate ADLC transmission", inline=True)
comment(0x861D, "Poll: wait for bit 7 to clear (TX done)", inline=True)
comment(0x8621, "Bit 6 into sign: 0=success, 1=error", inline=True)
comment(0x8622, "Success: clean up stack and exit", inline=True)
comment(0x8624, "Bit 5: escape condition?", inline=True)
comment(0x8625, "Yes (Z=1): abort via nlistn", inline=True)
comment(0x8627, "Check for escape key pressed", inline=True)
comment(0x862A, "Recover saved control byte", inline=True)
comment(0x862C, "Recover timeout parameter", inline=True)
comment(0x862E, "Recover retry count", inline=True)
comment(0x862F, "Retries exhausted: abort via nlistn", inline=True)
comment(0x8631, "Decrement retry count (C=1 from CMP)", inline=True)
comment(0x8633, "Re-push retry count and timeout for retry", inline=True)
comment(0x8637, "Delay loop: X*Y iterations before retry", inline=True)
comment(0x863D, "ALWAYS branch", inline=True)
comment(0x8643, "Success: discard 3 saved bytes from stack", inline=True)

# ============================================================
# print_inline subroutine (&85D9)
# ============================================================
# Label and code-tracing hook created by hook_subroutine() above.
subroutine(0x865C, hook=None,
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

comment(0x865C, "Pop return address (low) — points to last byte of JSR", inline=True)
comment(0x865F, "Pop return address (high)", inline=True)
comment(0x8664, "Advance pointer past return address / to next char", inline=True)
comment(0x866A, "Load next byte from inline string", inline=True)
comment(0x866C, "Bit 7 set? Done — this byte is the next opcode", inline=True)
comment(0x8674, "Jump to address of high-bit byte (resumes code after string)", inline=True)

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
# Service handler preamble: ADLC probe for duplicate ROM detection
comment(0x80F7, "9 NOPs: bus settling time for ADLC probe", inline=True)
comment(0x8101, "Only probe ADLC on service 1 (workspace claim)", inline=True)
comment(0x8105, "Probe ADLC SR1: non-zero = already initialised", inline=True)
comment(0x810C, "Probe ADLC SR2 if SR1 was all zeros", inline=True)
comment(0x8113, "Set bit 7 of per-ROM workspace = disable flag", inline=True)
comment(0x811A, "Read back flag; ASL puts bit 7 into carry", inline=True)
comment(0x811F, "Service >= &80: always handle (Tube/init)", inline=True)
comment(0x8121, "C=1 (ADLC active): duplicate ROM, skip", inline=True)
subroutine(0x8123, hook=None,
    title="Service handler entry",
    description="""\
Preamble at &80F7 (9 NOPs + ADLC probe): on service 1 only,
probes ADLC status registers &FEA0/&FEA1 to detect whether
Econet hardware has already been initialised by another ROM.
If active ADLC bits found, sets bit 7 of per-ROM workspace
as a disable flag. For services < &80, the flag causes an
early return (disabling this ROM as a duplicate). Services
>= &80 (&FE, &FF) are always handled regardless of flag.

Intercepts three service calls before normal dispatch:
  &FE: Tube init — explode character definitions
  &FF: Full init — vector setup, copy code to RAM, select NFS
  &12 (Y=5): Select NFS as active filing system
All other service calls < &0D dispatch via c8146.

Probes ADLC status registers SR1 (&FEA0) and SR2 (&FEA1)
to detect whether Econet hardware is present. Sets bit 7 of
per-ROM workspace as a disable flag if not found. The 9 NOPs
at &80F7 provide bus settling time after register access.""")

# ============================================================
# Init: set up vectors and copy code (&8140)
# ============================================================
label(0x8144, "init_vectors_and_copy")

# ============================================================
# Select NFS as active filing system (&81B5)
# ============================================================
subroutine(0x81F1, "svc_13_select_nfs", hook=None,
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
subroutine(0x8228, "check_boot_key", hook=None,
    title="Check boot key",
    description="""\
Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")

# ============================================================
# Print station identification (&822E)
# ============================================================
subroutine(0x8232, "print_station_info", hook=None,
    title="Print station identification",
    description="""\
Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")

comment(0x824B, "BIT trick: bit 5 of SR2 = clock present", inline=True)

# ============================================================
# Initialise filing system vectors (&8260)
# ============================================================
subroutine(0x8264, "init_fs_vectors", hook=None,
    title="Initialise filing system vectors",
    description="""\
Copies 14 bytes from l829a (&829A) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from svc_13_select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")

comment(0x8264, "Copy 14 bytes: FS vector addresses to FILEV-FSCV", inline=True)
comment(0x8272, "Install 7 handler entries in ROM ptr table", inline=True)
comment(0x8279, "X=0 after loop; store as workspace offset", inline=True)

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
subroutine(0x8298, "fs_vector_addrs", hook=None,
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

# Bytes &8296-&8299 overlap: tail of auto-boot string "OOT\r"
# and the first 4 bytes of fs_vector_addrs. Not copied by the
# dispatch loop (which starts at l829a = &829A).
byte(0x8296, 2)
comment(0x8296, "Auto-boot string tail / NETV handler data", inline=True)
byte(0x8298, 2)
comment(0x8298, "Auto-boot string tail / NETV handler data", inline=True)

# Part 1: extended vector dispatch addresses (7 x 2 bytes)
# The copy loop reads from l829a (Y=0..&0D), so the dispatch table
# starts at &829A, not at fs_vector_addrs (&8298).
for i, name in enumerate(["FILEV", "ARGSV", "BGETV", "BPUTV",
                           "GBPBV", "FINDV", "FSCV"]):
    addr = 0x829A + i * 2
    byte(addr, 2)
    comment(addr, f"{name} dispatch (&FF{0x1B + i * 3:02X})", inline=True)

# Part 2: handler address entries (7 x {lo, hi, pad})
# store_rom_ptr_pair reads lo/hi from run_fscv_cmd+Y. With Y=&1B,
# that's &828D+&1B = &82A8, so the handler table starts at &82A8.
handler_names = [
    ("FILEV",  0x870C),
    ("ARGSV",  0x8968),
    ("BGETV",  0x8563),
    ("BPUTV",  0x8413),
    ("GBPBV",  0x8A72),
    ("FINDV",  0x89D8),
    ("FSCV",   0x80D4),
]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x82A8 + i * 3
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
subroutine(0x82BC, "svc_1_abs_workspace", hook=None,
    title="Service 1: claim absolute workspace",
    description="""\
Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""")
comment(0x82BC, "Already at page &10 or above?", inline=True)
comment(0x82BE, "Yes: nothing to claim", inline=True)
comment(0x82C0, "Claim pages &0D-&0F (3 pages)", inline=True)

# ============================================================
# Service 2: claim private workspace (&82AB)
# ============================================================
subroutine(0x82C5, "svc_2_private_workspace", hook=None,
    title="Service 2: claim private workspace and initialise NFS",
    description="""\
Y = next available workspace page on entry.
Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
On soft break (OSBYTE &FD returns 0): skips FS state init,
preserving existing login state, file server selection, and
control block configuration — this is why pressing BREAK
keeps the user logged in.
On power-up/CTRL-BREAK (result non-zero):
  - Sets FS server station to &FE (no server selected)
  - Sets printer server station to &FE (no server selected)
  - Clears FS handles, OPT byte, message flag, SEQNOS
  - Initialises all RXCBs with &3F flag (available)
In both cases: reads station ID from &FE18 (only valid during
reset), calls adlc_init, enables user-level RX (LFLAG=&40).""")

comment(0x82CE, "Clear status byte in net receive buffer", inline=True)
comment(0x82DC, "OSBYTE &FD: read type of last reset", inline=True)
comment(0x82E2, "Soft break (X=0): skip FS init", inline=True)
comment(0x82E8, "Station &FE = no server selected", inline=True)
comment(0x82FE, "Init printer server: station &FE, net 0", inline=True)
comment(0x830E, "Mark RXCB as available", inline=True)
comment(0x8316, "Read station ID (also INTOFF)", inline=True)
comment(0x831D, "Initialise ADLC hardware", inline=True)
comment(0x8320, "Enable user-level RX (LFLAG=&40)", inline=True)

# ============================================================
# Service 3: auto-boot (&8203)
# ============================================================
subroutine(0x821D, "svc_3_autoboot", hook=None,
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
subroutine(0x81A9, "svc_star_command", hook=None,
    title="Service 4: unrecognised * command",
    description="""\
The first 5 bytes (&81A9-&81AF) are the service handler epilogue:
PLA/STA restores &A9, TXA/LDX retrieves romsel_copy, then RTS.
This is the common return path reached after any dispatched
service handler completes.

The service 4 handler entry at &81B5 (after 5 NOPs of padding)
makes two match_rom_string calls against the ROM header, reusing
header bytes as command strings:

  X=&0C: matches "ROFF" at &8014 — the suffix of the
         copyright string "(C)ROFF" — *ROFF (Remote Off,
         end remote session) — falls through to net_4_resume_remote

  X=5: matches "NET" at &800D — the ROM title suffix
       — *NET (select NFS) — falls through to svc_13_select_nfs

If neither matches, returns with the service call
unclaimed.""")
comment(0x81A9, "Restore saved A from service dispatch", inline=True)
comment(0x81AA, "Save to workspace &A9", inline=True)
comment(0x81AC, "Return ROM number in A", inline=True)
comment(0x81AD, "Restore X from MOS ROM select copy", inline=True)
comment(0x81B0, "Padding: dispatch targets &81B5", inline=True)
comment(0x81B5, "ROM offset for \"ROFF\" (copyright suffix)", inline=True)
comment(0x81B7, "Try matching *ROFF command", inline=True)
comment(0x81BA, "No match: try *NET", inline=True)

# ============================================================
# Service 9: *HELP (&81ED)
# ============================================================
subroutine(0x8208, "svc_9_help", hook=None,
    title="Service 9: *HELP",
    description="""\
Prints the ROM identification string using print_inline.""")

# ============================================================
# Match ROM string (&835E)
# ============================================================
label(0x8362, "match_rom_string")
comment(0x8362, "Y = saved text pointer offset", inline=True)
comment(0x8364, "Load next input character", inline=True)
comment(0x8366, "Is it a '.' (abbreviation)?", inline=True)
comment(0x8368, "Yes: skip to space skipper (match)", inline=True)
comment(0x836A, "Force uppercase (clear bit 5)", inline=True)
comment(0x836C, "Input char is NUL/space: check ROM byte", inline=True)
comment(0x836E, "Compare with ROM string byte", inline=True)
comment(0x8371, "Mismatch: check if ROM string ended", inline=True)
comment(0x8373, "Advance input pointer", inline=True)
comment(0x8374, "Advance ROM string pointer", inline=True)
comment(0x8375, "Continue matching (always taken)", inline=True)
comment(0x8377, "Load ROM string byte at match point", inline=True)
comment(0x837A, "Zero = end of ROM string = full match", inline=True)
comment(0x837C, "Non-zero = partial/no match; Z=0", inline=True)
comment(0x837D, "Skip this space", inline=True)
comment(0x837E, "Load next input character", inline=True)
comment(0x8380, "Is it a space?", inline=True)
comment(0x8382, "Yes: keep skipping", inline=True)
comment(0x8384, "XOR with CR: Z=1 if end of line", inline=True)

# ============================================================
# Call FSCV shutdown (&81FE)
# ============================================================
subroutine(0x8218, "call_fscv_shutdown", hook=None,
    title="Notify filing system of shutdown",
    description="""\
Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")
comment(0x8218, "FSCV reason 6 = FS shutdown", inline=True)
comment(0x821A, "Tail-call via filing system control vector", inline=True)

# ============================================================
# Issue service: vectors claimed (&8261)
# ============================================================
subroutine(0x827B, "issue_vectors_claimed", hook=None,
    title="Issue 'vectors claimed' service and optionally auto-boot",
    description="""\
Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If l00a8 is zero (soft break — RXCBs already
initialised), sets up the command string "I .BOOT" at &828E
and jumps to the FSCV 3 unrecognised-command handler (which
matches against the command table at &8C4B). The "I." prefix
triggers the catch-all entry which forwards the command to
the fileserver. Falls through to run_fscv_cmd.""")

comment(0x8284, "Issue service &0A", inline=True)
comment(0x8287, "Non-zero after hard reset: skip auto-boot", inline=True)
comment(0x828B, "X = lo byte of auto-boot string at &8292", inline=True)

# ============================================================
# Run FSCV command from ROM (&8289)
# ============================================================
subroutine(0x828D, "run_fscv_cmd", hook=None,
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
subroutine(0x8325, "setup_rom_ptrs_netv", hook=None,
    title="Set up ROM pointer table and NETV",
    description="""\
Reads the ROM pointer table base address via OSBYTE &A8, stores
it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
one 3-byte extended vector entry (addr=&9080, rom=current) into
the ROM pointer table at offset &36, installing osword_dispatch
as the NETV handler.""")

comment(0x8332, "NETV extended vector offset in ROM ptr table", inline=True)
comment(0x8337, "Install 1 entry (NETV) in ROM ptr table", inline=True)
comment(0x8345, "Write current ROM bank number", inline=True)
comment(0x834D, "Y = next workspace page for MOS", inline=True)

# ============================================================
# FSCV shutdown: save FS state (&8337)
# ============================================================
subroutine(0x8351, "fscv_6_shutdown", hook=None,
    title="FSCV 6: Filing system shutdown / save state (FSDIE)",
    description="""\
Called when another filing system (e.g. DFS) is selected. Saves
the current NFS context (FSLOCN station number, URD/CSD/LIB
handles, OPT byte, etc.) from page &0E into the dynamic workspace
backup area. This allows the state to be restored when *NET is
re-issued later, without losing the login session. Finally calls
OSBYTE &77 (FXSPEX: close SPOOL and EXEC files) to avoid leaving
dangling file handles across the FS switch.""")

comment(0x8351, "Copy 10 bytes: FS state to workspace backup", inline=True)
comment(0x8359, "Offsets &15-&1D: server, handles, OPT, etc.", inline=True)

# ============================================================
# Init TX control block (&8356)
# ============================================================
subroutine(0x8395, "init_tx_ctrl_block", hook=None,
    title="Initialise TX control block at &00C0 from template",
    description="""\
Copies 12 bytes from tx_ctrl_template (&83AD) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""")

comment(0x839E, "Y < 2: also copy FS server station/network", inline=True)

subroutine(0x83AD, "tx_ctrl_template", hook=None,
    title="TX control block template (TXTAB, 12 bytes)",
    description="""\
12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")
# &836D-&8379 is code (string
# comparison loop tail: BNE/INY/INX/BNE + LDA abs,X/BEQ/RTS/INY).
# The TX control block template is at different addresses in 3.40.

# ============================================================
# Prepare FS command (&838A)
# ============================================================
subroutine(0x83C7, "prepare_fs_cmd",
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

comment(0x83C7, "V=0: standard FS command path", inline=True)
comment(0x83D4, "Copy CSD and LIB handles to command buffer", inline=True)

# ============================================================
# Build and send FS command (&83A4)
# ============================================================
subroutine(0x83DD, "build_send_fs_cmd",
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
              "c": "0 for standard FS path, 1 for byte-stream (BSXMIT)"},
    on_exit={"a": "0 on success",
             "x": "0 on success, &D6 on not-found",
             "y": "1 (offset past command code in reply)"})

comment(0x83DE, "Reply port &90 (PREPLY)", inline=True)
comment(0x83E7, "HPTR = header (5) + data (X) bytes to send", inline=True)
comment(0x83EC, "C=1: byte-stream path (BSXMIT)", inline=True)

# ============================================================
# FS error handler (&8443)
# ============================================================
subroutine(0x847A, "store_fs_error", hook=None,
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
comment(0x847F, "Clamp FS errors below &A8 to standard &A8", inline=True)
comment(0x848A, "Copy reply buffer to &0100 for BRK execution", inline=True)
comment(0x848F, "Scan for CR terminator (&0D)", inline=True)
comment(0x8493, "Replace CR with zero = BRK error block end", inline=True)
comment(0x8496, "Execute as BRK error block at &0100", inline=True)

# ============================================================
# Handle BPUT/BGET (&83DD)
# ============================================================
subroutine(0x8417, "handle_bput_bget",
    title="Handle BPUT/BGET file byte I/O",
    description="""\
BPUTV enters at &8413 (CLC; fall through) and BGETV enters
at &8563 (SEC; JSR here). The carry flag is preserved via
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
comment(0x8420, "Save handle for SPOOL/EXEC comparison later", inline=True)
comment(0x842A, "&90 = data port (PREPLY)", inline=True)
comment(0x8432, "CB reply buffer at &0FDC", inline=True)
comment(0x8436, "Error buffer at &0FE0", inline=True)
comment(0x843D, "Restore C: selects BPUT (0) vs BGET (1)", inline=True)
comment(0x844E, "Zero reply = success, skip error handling", inline=True)
comment(0x8450, "Copy 32-byte reply to error buffer at &0FE0", inline=True)
comment(0x845C, "Returns X=EXEC handle, Y=SPOOL handle", inline=True)
comment(0x8461, "')': offset into \"SP.\" string at &8529", inline=True)
comment(0x8463, "Y=value of *SPOOL file handle", inline=True)
comment(0x8467, "'-': offset into \"E.\" string at &852D", inline=True)
comment(0x8469, "X=value of *EXEC file handle", inline=True)
comment(0x846E, "Y=&85: high byte of OSCLI string in ROM", inline=True)
comment(0x8470, "Close SPOOL/EXEC via \"*SP.\" or \"*E.\"", inline=True)
comment(0x8473, "Reset CB pointer to error buffer at &0FE0", inline=True)

# ============================================================
# Send command to fileserver (&84ED)
# ============================================================
subroutine(0x8532, "send_to_fs", hook=None,
    title="Send command to fileserver and handle reply (WAITFS)",
    description="""\
Performs a complete FS transaction: transmit then wait for reply.
Sets bit 7 of rx_flags (mark FS transaction in progress),
builds a TX frame from the data at (net_tx_ptr), and transmits
it. The system RX flag (LFLAG bit 7) is only set when receiving
into the page-zero control block — if RXCBP's high byte is
non-zero, setting the system flag would interfere with other RX
operations. The timeout counter uses the stack (indexed via TSX)
rather than memory to avoid bus conflicts with Econet hardware
during the tight polling loop. Handles multi-block replies and
checks for escape conditions between blocks.""")
comment(0x8537, "Only flag rx_flags if using page-zero CB", inline=True)
comment(0x8540, "Push two zero bytes as timeout counters", inline=True)
comment(0x8545, "TSX: index stack-based timeout via X", inline=True)
comment(0x8548, "Bit 7 set = reply received", inline=True)
comment(0x854A, "Three-stage nested timeout: inner loop", inline=True)
comment(0x854F, "Middle timeout loop", inline=True)
comment(0x8554, "Outer timeout loop (slowest)", inline=True)
comment(0x855C, "Restore saved rx_flags from stack", inline=True)
comment(0x8560, "A=saved func code; zero would mean no reply", inline=True)

# The RTS at &8562 is the tail of send_to_fs / fs_wait_cleanup.

# ============================================================
# Error message table (&854D)
# ============================================================
# N.B. This is data, not code — we use label() not subroutine()
# to avoid entry() tracing from &854D, where the &A0 error code
# byte would be misinterpreted as LDY #imm.
label(0x8580, "error_msg_table")
comment(0x8580, """\
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
Indexed via c850c/nlistn/nlisne at &850C-&8514.""")

# Mark each error table entry as data: error code byte + NUL-terminated string.
# Without this, the first entry's &A0 byte is traced as code (LDY #imm).
addr = 0x8579
for _ in range(7):
    byte(addr, 1)           # error number byte
    addr = stringz(addr + 1)  # NUL-terminated message string

# ============================================================
# Resume after remote operation (&8180)
# ============================================================
subroutine(0x81BC, "net_4_resume_remote", hook=None,
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
# GSINIT/GSREAD filename parser (&86E8)
# ============================================================
subroutine(0x86E8, "parse_filename_gs", hook=None,
    title="Parse filename using GSINIT/GSREAD into &0E30",
    description="""\
Uses the MOS GSINIT/GSREAD API to parse a filename string from
(os_text_ptr),Y, handling quoted strings and |-escaped characters.
Stores the parsed result CR-terminated at &0E30 and sets up
fs_crc_lo/hi to point to that buffer. Sub-entry at &86EA allows
a non-zero starting Y offset.""",
    on_entry={"y": "offset into (os_text_ptr) buffer (0 at &86E8)"},
    on_exit={"x": "length of parsed string",
             "y": "preserved"})
comment(0x86EA, "X=&FF: INX will make X=0 (first char index)", inline=True)
comment(0x86EC, "C=0 for GSINIT: parse from current position", inline=True)
comment(0x86F0, "Empty string: skip to CR terminator", inline=True)
comment(0x86F5, "C=1 from GSREAD: end of string reached", inline=True)
comment(0x86FD, "Terminate parsed string with CR", inline=True)
comment(0x8703, "Point fs_crc_lo/hi at &0E30 parse buffer", inline=True)

# ============================================================
# FILEV handler (&870C)
# ============================================================
subroutine(0x870C, "filev_handler",
    title="FILEV handler (OSFILE entry point)",
    description="""\
Calls save_fscv_args (&864D) to preserve A/X/Y, then JSR &86DE
to copy the 2-byte filename pointer from the parameter block to
os_text_ptr and fall through to parse_filename_gs (&86E8) which
parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &8722)
  A=&00: save file (filev_save at &8795)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &88D1)
  Other: restore_args_return (unsupported, no-op)""",
    on_entry={"a": "function code (&FF=load, &00=save, &01-&06=attrs)",
              "x": "parameter block address low byte",
              "y": "parameter block address high byte"},
    on_exit={"a": "restored",
             "x": "restored",
             "y": "restored"})
comment(0x870F, "Copy filename ptr from param block to os_text_ptr", inline=True)
comment(0x8712, "Recover function code from saved A", inline=True)
comment(0x8714, "A >= 0: save (&00) or attribs (&01-&06)", inline=True)
comment(0x8716, "A=&FF? Only &FF is valid for load", inline=True)
comment(0x871A, "Unknown negative code: no-op return", inline=True)

subroutine(0x8722, "send_fs_examine", hook=None,
    title="Send FS examine command",
    description="""\
Sends an FS examine/load command to the fileserver. The function
code in Y is set by the caller (Y=2 for load, Y=5 for examine).
Overwrites fs_cmd_urd (&0F02) with &92 (PLDATA port number) to
repurpose the URD header field for the data transfer port. Sets
escapable to &92 so escape checking is active during the transfer.
Calls prepare_cmd_clv to build the FS header (which skips the
normal URD copy, preserving &92). The FS reply contains load/exec
addresses and file length used to set up the data transfer.
Byte 6 of the parameter block selects load address handling:
non-zero uses the address from the FS reply (load to file's own
address); zero uses the caller-supplied address.""")
comment(0x8722, "Port &92 = PLDATA (data transfer port)", inline=True)
comment(0x8724, "Mark transfer as escapable", inline=True)
comment(0x8726, "Overwrite URD field with data port number", inline=True)
comment(0x872E, "Byte 6: use file's own load address?", inline=True)
comment(0x8730, "Non-zero: use FS reply address (lodfil)", inline=True)
comment(0x8732, "Zero: copy caller's load addr first", inline=True)
comment(0x8738, "Carry clear from prepare_cmd_clv: skip lodfil", inline=True)
comment(0x8740, "Compute end address = load + file length", inline=True)
comment(0x874F, "Adjust high byte for 3-byte length overflow", inline=True)
comment(0x8755, "Transfer file data in &80-byte blocks", inline=True)
comment(0x8758, "Copy 3-byte file length to FS reply cmd buffer", inline=True)
comment(0x8763, "ALWAYS branch", inline=True)

subroutine(0x8765, "send_data_blocks", hook=None,
    title="Send file data in multi-block chunks",
    description="""\
Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")
comment(0x8768, "Addresses match: transfer complete", inline=True)
comment(0x876A, "Port &92 for data block transfer", inline=True)
comment(0x876E, "Set up next &80-byte block for transfer", inline=True)
comment(0x8770, "Swap: current addr -> source, end -> current", inline=True)
comment(0x877B, "Command &7F = data block transfer", inline=True)
comment(0x877F, "Send this block to the fileserver", inline=True)
comment(0x8784, "Compare current vs end address (4 bytes)", inline=True)
comment(0x878A, "Not equal: more blocks to send", inline=True)

subroutine(0x8795, "filev_save", hook=None,
    title="OSFILE save handler (A=&00)",
    description="""\
Copies 4-byte load/exec/length addresses from the parameter block
to the FS command buffer, along with the filename. The savsiz loop
computes data-end minus data-start for each address byte to derive
the transfer length, saving both the original address and the
difference. Sends FS command with port &91, function code Y=1,
and the filename via copy_string_to_cmd. After transfer_file_blocks
sends the data, calls send_fs_reply_cmd for the final handshake.
If fs_messages_flag is set, prints the catalogue line inline:
filename (padded to 12 chars), load address, exec address, and
file length. Finally decodes the FS attributes and copies the
reply data back into the caller's parameter block.""")
comment(0x8795, "Process 4 address bytes (load/exec/start/end)", inline=True)
comment(0x8797, "Y=&0E: start from end-address in param block", inline=True)
comment(0x8799, "Read end-address byte from param block", inline=True)
comment(0x879B, "Save to port workspace for transfer setup", inline=True)
comment(0x87A1, "end - start = transfer length byte", inline=True)
comment(0x87A3, "Store length byte in FS command buffer", inline=True)
comment(0x87A7, "Read corresponding start-address byte", inline=True)
comment(0x87A9, "Save to port workspace", inline=True)
comment(0x87AD, "Replace param block entry with length", inline=True)
comment(0x87B5, "Copy load/exec addresses to FS command buffer", inline=True)
comment(0x87BF, "Port &91 for save command", inline=True)
comment(0x87C1, "Mark as escapable during save", inline=True)
comment(0x87C3, "Overwrite URD field with port number", inline=True)
comment(0x87C8, "Append filename at offset &0B in cmd buffer", inline=True)
comment(0x87CD, "Y=1: function code for save", inline=True)
comment(0x87D2, "Read FS reply command code for transfer type", inline=True)
comment(0x87D5, "Send file data blocks to server", inline=True)
comment(0x87D8, "Save CSD from reply for catalogue display", inline=True)
comment(0x87DC, "Send final reply acknowledgement", inline=True)
comment(0x87E0, "Check if file info messages enabled", inline=True)
comment(0x87E3, "Messages off: skip catalogue display", inline=True)

subroutine(0x882F, "copy_load_addr_from_params", hook=None,
    title="Copy load address from parameter block",
    description="""\
Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""")
comment(0x882F, "Start at offset 5 (top of 4-byte addr)", inline=True)
comment(0x8831, "Read from parameter block", inline=True)
comment(0x8833, "Store to local workspace", inline=True)
comment(0x8837, "Copy offsets 5,4,3,2 (4 bytes)", inline=True)
comment(0x883B, "Y=3 after loop; add 5 to get Y=8", inline=True)

subroutine(0x8841, "copy_reply_to_params", hook=None,
    title="Copy FS reply data to parameter block",
    description="""\
Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""")
comment(0x8841, "Start at offset &0D (top of range)", inline=True)
comment(0x8843, "First store uses X (attrib byte)", inline=True)
comment(0x8844, "Write to parameter block", inline=True)
comment(0x8846, "Read next byte from reply buffer", inline=True)
comment(0x884A, "Copy offsets &0D down to 2", inline=True)
comment(0x884E, "Y=1 after loop; sub 4 to get Y=&FD", inline=True)

subroutine(0x8853, "transfer_file_blocks", hook=None,
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
comment(0x8857, "Addresses equal: nothing to transfer", inline=True)
comment(0x885B, "Push 4-byte block size: 0, 0, hi, lo", inline=True)
comment(0x8869, "Source = current position", inline=True)
comment(0x886E, "Dest = current pos + block size", inline=True)
comment(0x8872, "Advance current position", inline=True)
comment(0x8879, "Check if new pos overshot end addr", inline=True)
comment(0x8885, "Overshot: clamp dest to end address", inline=True)
comment(0x888E, "Recover original FS command byte", inline=True)
comment(0x8893, "128-byte block size for data transfer", inline=True)
comment(0x889A, "ACK port for flow control", inline=True)
comment(0x88A2, "Command &91 = data block transfer", inline=True)
comment(0x88A6, "Skip command code byte in TX buffer", inline=True)
comment(0x88AB, "More blocks? Loop back", inline=True)

subroutine(0x88AD, "fscv_1_eof", hook=None,
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
comment(0x88B3, "Local hint: is EOF possible for this handle?", inline=True)
comment(0x88B7, "Hint clear: definitely not at EOF", inline=True)
comment(0x88C5, "FS reply: non-zero = at EOF", inline=True)
comment(0x88CA, "Not at EOF: clear the hint bit", inline=True)

subroutine(0x88D1, "filev_attrib_dispatch", hook=None,
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
comment(0x88D8, "A>=7: unsupported, fall through to return", inline=True)
comment(0x88E6, "A=2 or 3: convert to param block offset", inline=True)
comment(0x88E9, "Y = A*4 - 3 (load addr offset for A=2)", inline=True)
comment(0x88FB, "A=1: encode protection from param block", inline=True)
comment(0x893A, "Save object type from FS reply", inline=True)
comment(0x8943, "Decode 5-bit access byte from FS reply", inline=True)
comment(0x8948, "Store decoded attrs at param block +&0E", inline=True)
comment(0x8963, "Return object type in A", inline=True)

subroutine(0x89B3, "restore_args_return", hook=None,
    title="Restore arguments and return",
    description="""\
Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""")

label(0x8A2C, "fscv_0_opt_entry")       # FSCV 0 dispatch entry (BEQ guard before fscv_0_opt)

subroutine(0x8A2E, "fscv_0_opt", hook=None,
    title="FSCV 0: *OPT handler (OPTION)",
    description="""\
Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""")
comment(0x8A36, "Not *OPT 4: check for *OPT 1", inline=True)
comment(0x8A39, "Set local messages flag (*OPT 1,Y)", inline=True)
comment(0x8A4D, "Cache boot option locally", inline=True)

subroutine(0x8A5A, "adjust_addrs", hook=None,
    title="Bidirectional 4-byte address adjustment",
    description="""\
Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""")
comment(0x8A5A, "X=&FC: index into &0E06 area (wraps to 0)", inline=True)
comment(0x8A5C, "Load byte from param block", inline=True)
comment(0x8A5E, "Test sign of adjustment direction", inline=True)
comment(0x8A60, "Negative: subtract instead", inline=True)
comment(0x8A62, "Add adjustment value", inline=True)
comment(0x8A65, "Skip to store result", inline=True)
comment(0x8A68, "Subtract adjustment value", inline=True)
comment(0x8A6B, "Store adjusted byte back", inline=True)
comment(0x8A6D, "Next param block byte", inline=True)
comment(0x8A6E, "Next adjustment byte (X wraps &FC->&00)", inline=True)
comment(0x8A6F, "Loop 4 times (X=&FC,&FD,&FE,&FF,done)", inline=True)

# ============================================================
# ARGSV handler (&8968)
# ============================================================
subroutine(0x8968, "argsv_handler",
    title="ARGSV handler (OSARGS entry point)",
    description="""\
  A=0, Y=0: return filing system number (5 = network FS)
  A=0, Y>0: read file pointer via FS command &0C (FCRDSE)
  A=1, Y>0: write file pointer via FS command &0D (FCWRSE)
  A=2, Y=0: return &01 (command-line tail supported)
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
comment(0x896D, "A>=3 (ensure/flush): no-op for NFS", inline=True)
comment(0x8979, "LSR splits A: C=1 means write (A=1)", inline=True)
comment(0x897D, "C=1: write path, copy ptr from caller", inline=True)
comment(0x898C, "Zero high byte of 3-byte pointer", inline=True)
comment(0x89BA, "Y=0: FS-level queries (no file handle)", inline=True)
comment(0x89C3, "FS number 5 (loaded as &0A, LSR'd)", inline=True)
comment(0x89C5, "Shared: A=0->&05, A=2->&01", inline=True)
comment(0x89C8, "Copy command context to caller's block", inline=True)

# ============================================================
# FINDV handler (&89D8)
# ============================================================
subroutine(0x89D8, "findv_handler",
    title="FINDV handler (OSFIND entry point)",
    description="""\
  A=0: close file -- delegates to close_handle (&8A10)
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
comment(0x89DB, "SEC distinguishes open (A>0) from close", inline=True)
comment(0x89E2, "Valid open modes: &40, &80, &C0 only", inline=True)
comment(0x89E7, "Convert MOS mode to FS protocol flags", inline=True)
comment(0x89EA, "Flag 1: read/write direction", inline=True)
comment(0x89EE, "Flag 2: create vs existing file", inline=True)

# 3.35K: sequence number initialisation for newly opened handles
comment(0x8A0A, """\
OR handle bit into fs_sequence_nos
(&0E08). Without this, a newly opened file could
inherit a stale sequence number from a previous
file using the same handle, causing byte-stream
protocol errors.""")

# ============================================================
# CLOSE handler (&8A10)
# ============================================================
subroutine(0x8A10, "close_handle", hook=None,
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
# GBPBV handler (&8A72)
# ============================================================
subroutine(0x8A72, "gbpbv_handler",
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
comment(0x8A78, "Convert to 0-based (A=0..7)", inline=True)
comment(0x8A84, "A>=4: info queries, dispatch separately", inline=True)
comment(0x8A8B, "Get file handle from param block byte 0", inline=True)
comment(0x8A9D, "Skip param block offset 8 (the handle)", inline=True)
comment(0x8AA6, "LSR: odd=read (C=1), even=write (C=0)", inline=True)
comment(0x8AAB, "Store FS direction flag", inline=True)
comment(0x8AB0, "Command &91=put, &92=get", inline=True)
comment(0x8AB8, "Read: one fewer data byte in command", inline=True)
comment(0x8AC6, "Save seq# for byte-stream flow control", inline=True)
comment(0x8ACD, "Set up source/dest from param block", inline=True)
comment(0x8AD5, "Skip 4 bytes to reach transfer length", inline=True)
comment(0x8AD8, "Dest = source + length", inline=True)
comment(0x8AED, "Odd (read): send data to FS first", inline=True)
comment(0x8AF3, "Transfer data blocks to fileserver", inline=True)
comment(0x8B00, "Check FS reply: bit 7 = not at EOF", inline=True)
comment(0x8B05, "At EOF: clear EOF hint for this handle", inline=True)
comment(0x8B0B, "Direction=0: forward adjustment", inline=True)
comment(0x8B10, "Direction=&FF: reverse adjustment", inline=True)
comment(0x8B16, "Shift bit 7 into C for return flag", inline=True)

# ============================================================
# OSGBPB info handler (&8B31)
# ============================================================
subroutine(0x8B31, "osgbpb_info", hook=None,
    title="OSGBPB 5-8 info handler (OSINFO)",
    description="""\
Handles the "messy interface tacked onto OSGBPB" (original source).
Checks whether the destination address is in Tube space by comparing
the high bytes against TBFLAG. If in Tube space, data must be
copied via the Tube FIFO registers (with delays to accommodate the
slow 16032 co-processor) instead of direct memory access.""")
comment(0x8B33, "Check if destination is in Tube space", inline=True)
comment(0x8B3F, "Non-zero = Tube transfer required", inline=True)
comment(0x8B41, "Copy param block bytes 1-4 to workspace", inline=True)
comment(0x8B49, "Sub-function: AND #3 of (original A - 4)", inline=True)
comment(0x8B4C, "A=0 (OSGBPB 5): read disc title", inline=True)
comment(0x8B54, "Get CSD/LIB/URD handles for FS command", inline=True)
comment(0x8B6B, "&0D = 13 bytes of reply data expected", inline=True)
comment(0x8B7F, "Copy FS reply to caller's buffer", inline=True)
comment(0x8B81, "Non-zero: use Tube transfer path", inline=True)
comment(0x8BAD, "Delay loop for slow Tube co-processor", inline=True)
comment(0x8BB6, "Release Tube after transfer complete", inline=True)
comment(0x8BBE, "OSGBPB 8: read filenames from dir", inline=True)
comment(0x8BEE, "Subtract header (7 bytes) from reply len", inline=True)
comment(0x8C02, "Adjust pointer by +1 (one filename read)", inline=True)
comment(0x8C06, "Reverse adjustment for updated counter", inline=True)

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
and catch-all entries in the command match table at &8C4B, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")

# ============================================================
# *BYE handler (&8383)
# ============================================================
subroutine(0x83C0, "bye_handler", hook=None,
    title="*BYE handler (logoff)",
    description="""\
Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8C4B for "BYE".""")

# ============================================================
# FSCV unrecognised * handler (&8BB6)
# ============================================================
subroutine(0x8C1B, "fscv_3_star_cmd", hook=None,
    title="FSCV 2/3/4: unrecognised * command handler (DECODE)",
    description="""\
CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8C4B using case-insensitive comparison with abbreviation
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

subroutine(0x8C4B, "fs_cmd_match_table", hook=None,
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
  "EX"     → &8C61 (ex_handler: embedded in table tail)
  "BYE"\\r  → &83C0 (bye_handler: logoff)
  <catch-all> → &80C1 (forward anything else to FS)""")

# ============================================================
# *EX and *CAT handlers (&8C61 / &8C67)
# ============================================================
# ex_handler code is embedded in the tail of fs_cmd_match_table
# at &8C61 — the bytes A2 01 A9 03 D0 0B serve as both table
# data and executable code (LDX #1 / LDA #3 / BNE fscv_5_cat+9).
# Dispatched via PHA/PHA/RTS from the "EX" entry in the match
# table.
entry(0x8C61)
label(0x8C61, "ex_handler")

subroutine(0x8C67, "fscv_5_cat", hook=None,
    title="*CAT handler (directory catalogue)",
    description="""\
Initialises &B5=&0B (examine arg count) and &B7=&03 (column
count). The catalogue protocol is multi-step: first sends
FCREAD (&12: examine) to get the directory header, then sends
FCUSER (&15: read user environment) to get CSD, disc, and
library names, then sends FC &03 (examine entries) repeatedly
to fetch entries in batches until zero are returned (end of dir).
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
  - Directory entries: CRFLAG (&B9) cycles 0-3 for multi-column
    layout; at count 0 a newline is printed, others get spaces.
    *EX sets CRFLAG=&FF to force one entry per line.""")
comment(0x8C69, "CRFLAG=3: first entry will trigger newline", inline=True)
comment(0x8CA0, "Access level byte: 0=Owner, non-zero=Public", inline=True)
comment(0x8D2E, "Zero entries returned = end of directory", inline=True)

# ============================================================
# Boot command strings (&8CE7)
# ============================================================
subroutine(0x8D5B, "boot_cmd_strings", hook=None,
    title="Boot command strings for auto-boot",
    description="""\
The four boot options use OSCLI strings at offsets within page &8D.
The offset table at boot_option_offsets+1 (&8D68) is indexed by
the boot option value (0-3); each byte is the low byte of the
string address, with the page high byte &8D loaded separately:
  Option 0 (Off):  offset &67 → &8D67 = bare CR (empty command)
  Option 1 (Load): offset &58 → &8D58 = "L.!BOOT" (the bytes
      &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D5F)
  Option 2 (Run):  offset &5A → &8D5A = "!BOOT" (bare filename = *RUN)
  Option 3 (Exec): offset &60 → &8D60 = "E.!BOOT"

This is a classic BBC ROM space optimisation: the string data
overlaps with other byte sequences to save space. The &0D byte
at &8D67 terminates "E.!BOOT" AND doubles as the bare-CR
command for boot option 0.""")

# ============================================================
# Boot option table and "I AM" handler (&8CF4-&8E20)
# ============================================================
subroutine(0x8D67, "boot_option_offsets", hook=None,
    title="Boot option → OSCLI string offset table",
    description="""\
Five bytes: the first byte (&0D) is the bare-CR target for boot
option 0; bytes 1-4 are the offset table indexed by boot option
(0-3). Each offset is the low byte of a pointer into page &8D.
The code reads from boot_option_offsets+1 (&8D68) via
LDX l8d68,Y with Y=boot_option, then LDY #&8D, JMP oscli.
See boot_cmd_strings for the target strings.""")
for i in range(5):
    byte(0x8D67 + i)
comment(0x8D68, "Opt 0 (Off): bare CR at &8D67", inline=True)
comment(0x8D69, "Opt 1 (Load): L.!BOOT at &8D58", inline=True)
comment(0x8D6A, "Opt 2 (Run): !BOOT at &8D5A", inline=True)
comment(0x8D6B, "Opt 3 (Exec): E.!BOOT at &8D60", inline=True)
comment(0x8D53, """\
Option name encoding: the boot option names ("Off", "Load",
"Run", "Exec") are scattered through the code rather than
stored as a contiguous table. They are addressed via base+offset
from l8d54 (&8D54), whose four bytes are offsets into page &8D:
  &2B→&8D7F "Off", &3E→&8D92 "Load",
  &66→&8DBA "Run", &18→&8D6C "Exec"
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
comment(0x8088, "Colon = interactive remote command prefix", inline=True)
comment(0x808F, "C=1: dot found, first number was network", inline=True)
comment(0x8091, "Store network number (n.s = network.station)", inline=True)
comment(0x8098, "Z=1: no station parsed (empty or non-numeric)", inline=True)
comment(0x80A0, "Scan backward for ':' (interactive prefix)", inline=True)
comment(0x80AA, "Echo colon, then read user input from keyboard", inline=True)
comment(0x80B3, "Append typed character to command buffer", inline=True)

# ============================================================
# Handle workspace management (&8E15-&8E1A)
# ============================================================
subroutine(0x8E2D, "fsreply_5_set_lib", hook=None,
    title="Set library handle",
    description="""\
Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to JMP restore_args_return if Y is non-zero.""")

subroutine(0x8E32, "fsreply_3_set_csd", hook=None,
    title="Set CSD handle",
    description="""\
Stores Y into &0E03 (current selected directory handle).
Falls through to JMP restore_args_return.""")

# ============================================================
# Copy handles and boot (&8E20 / &8E21)
# ============================================================
subroutine(0x8E38, "fsreply_1_copy_handles_boot", hook=None,
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

subroutine(0x8E39, "fsreply_2_copy_handles", hook=None,
    title="Copy FS reply handles to workspace (no boot)",
    description="""\
CLC entry (SDISC): copies handles only, then jumps to
restore_args_return via c8e27. Called when the FS reply contains
updated handle values but no boot action is needed.""")
comment(0x8E39, "Copy 4 bytes: boot option + 3 handles", inline=True)
comment(0x8E3B, "SDISC: skip boot option, copy handles only", inline=True)
comment(0x8E3D, "Load from FS reply (&0F05+X)", inline=True)
comment(0x8E40, "Store to handle workspace (&0E02+X)", inline=True)
comment(0x8E43, "Next handle (descending)", inline=True)
comment(0x8E44, "Loop while X >= 0", inline=True)
comment(0x8E46, "SDISC: done, restore args and return", inline=True)

# ============================================================
# Filename copy helpers (&8D43-&8D51)
# ============================================================
subroutine(0x8D82, "copy_filename", hook=None,
    title="Copy filename to FS command buffer",
    description="""\
Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""")
comment(0x8D82, "Start writing at &0F05 (after cmd header)", inline=True)

subroutine(0x8D84, "copy_string_to_cmd", hook=None,
    title="Copy string to FS command buffer",
    description="""\
Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""")
comment(0x8D8D, "XOR with CR: result=0 if byte was CR", inline=True)

# ============================================================
# Print directory name (&8D57)
# ============================================================
subroutine(0x8D96, "fsreply_0_print_dir", hook=None,
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
subroutine(0x8DDC, "fscv_2_star_run", hook=None,
    title="FSCV 2/4: */ (run) and *RUN handler",
    description="""\
Parses the filename via parse_filename_gs and calls infol2,
then falls through to fsreply_4_notify_exec to set up and
send the FS load-as-command request.""")

# ============================================================
# FS reply 4: notify and execute (&8DD5)
# ============================================================
subroutine(0x8DE2, "fsreply_4_notify_exec", hook=None,
    title="FS reply 4: send FS load-as-command and execute response",
    description="""\
Initialises a GS reader to skip past the filename and
calculate the command context address, then sets up an FS
command with function code &05 (FCCMND: load as command)
using send_fs_examine. If a Tube co-processor is present
(tube_flag != 0), transfers the response data to the Tube
via tube_addr_claim. Otherwise jumps via the indirect
pointer at (&0F09) to execute at the load address.""")
comment(0x8DE5, "GSINIT/GSREAD: skip past the filename", inline=True)
comment(0x8DF0, "Calculate context addr = text ptr + Y", inline=True)
comment(0x8E10, "Check for Tube co-processor", inline=True)

# ============================================================
# *NET sub-command handlers (&8E3B-&8E75)
# ============================================================
subroutine(0x8E48, "boot_cmd_execute", hook=None,
    title="Execute boot command via OSCLI",
    description="""\
Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")

# The actual *NET1 handler is at &8E67 (dispatched via table to &8E67).
# The code at &8E3A was incorrectly labeled net_1_read_handle by the
# auto-generator — the address shifted due to the ROM header change.
entry(0x8E67)
label(0x8E67, "net_1_read_handle")
comment(0x8E67, """\
*NET1: read file handle from received packet.
Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
and falls through to net_2_read_handle_entry's common path.""")

subroutine(0x8E55, "calc_handle_offset", hook=None,
    title="Calculate handle workspace offset",
    description="""\
Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""")
comment(0x8E55, "A = handle * 2", inline=True)
comment(0x8E56, "A = handle * 4", inline=True)
comment(0x8E57, "Push handle*4 onto stack", inline=True)
comment(0x8E58, "A = handle * 8", inline=True)
comment(0x8E5A, "A = handle*8 + handle*4 = handle*12", inline=True)
comment(0x8E5D, "Y = offset into handle workspace", inline=True)
comment(0x8E5E, "Clean up stack (discard handle*4)", inline=True)
comment(0x8E5F, "Offset >= &48? (6 handles max)", inline=True)
comment(0x8E61, "Valid: return with C clear", inline=True)
comment(0x8E65, "A=0, C set = error indicator", inline=True)

label(0x8E66, "return_calc_handle")      # Return from calc_handle_offset (invalid)

entry(0x8E6D)
subroutine(0x8E6D, "net_2_read_handle_entry", hook=None,
    title="*NET2: read handle entry from workspace",
    description="""\
Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""")

entry(0x8E7D)
subroutine(0x8E7D, "net_3_close_handle", hook=None,
    title="*NET3: close handle (mark as unused)",
    description="""\
Looks up the handle in &F0 via calc_handle_offset. Writes
&3F ('?') to mark the handle slot as closed in the NFS
workspace. Returns via RTS (earlier versions preserved the
carry flag across the write using ROL/ROR on rx_flags, but
3.60 simplified this).""")

# NMI handler init — ROM code copies to page &04/&05/&06
# ============================================================
# Filing system OSWORD dispatch (&8E76 / &8E80)
# ============================================================
subroutine(0x8E87, "svc_8_osword", hook=None,
    title="Filing system OSWORD entry",
    description="""\
Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the range
check and dispatch at osword_12_handler (&8E8D).""")

comment(0x8E87, "Command code from &EF", inline=True)
comment(0x8E89, "Subtract &0F: OSWORD &0F-&13 become indices 0-4", inline=True)

subroutine(0x8E9F, "fs_osword_dispatch", hook=None,
    title="PHA/PHA/RTS dispatch for filing system OSWORDs",
    description="""\
Saves the param block pointer (&AA-&AC) to (net_rx_ptr) and
reads the sub-function code from (&F0)+1, then dispatches via
the 5-entry table at &8EB8 (low) / &8EBD (high) using
PHA/PHA/RTS. The RTS at the end of the dispatched handler
returns here, after which the caller restores &AA-&AC.""")

comment(0x8EA7, "Dispatch table: low bytes for OSWORD &0F-&13 handlers", inline=True)
comment(0x8EBD, "Dispatch table: high bytes for OSWORD &0F-&13 handlers", inline=True)

comment(0x815F, "Copy NMI handler code from ROM to RAM pages &04-&06")
comment(0x8179, "Copy NMI workspace initialiser from ROM to &0016-&0076")

# ============================================================
# Econet TX/RX handler (&8FE5)
# ============================================================
subroutine(0x8FF0, "econet_tx_rx", hook=None,
    title="Econet transmit/receive handler",
    description="""\
A=0: Initialise TX control block from ROM template at &8395
     (init_tx_ctrl_block+Y, zero entries substituted from NMI
     workspace &0DE6), transmit it, set up RX control block,
     and receive reply.
A>=1: Handle transmit result (branch to cleanup at &903E).""")

comment(0x8FF0, "A=0: set up and transmit; A>=1: handle result", inline=True)
comment(0x8FF9, "Non-zero = use ROM template byte as-is", inline=True)
comment(0x8FFB, "Zero = substitute from NMI workspace", inline=True)
comment(0x9023, "Enable interrupts before transmit", inline=True)
comment(0x9029, "Set RX end address to &FFFF (accept any length)", inline=True)
comment(0x906C, "Test for end-of-data marker (&0D)", inline=True)

# ============================================================
# OSWORD-style function dispatch (&9074)
# ============================================================
subroutine(0x9080, "osword_dispatch",
    title="NETVEC dispatch handler (ENTRY)",
    description="""\
Indirected from NETVEC at &0224. Saves all registers and flags,
retrieves the reason code from the stacked A, and dispatches to
one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
&9099. Reason codes >= 9 are ignored.

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

comment(0x9087, "Retrieve original A (reason code) from stack", inline=True)
comment(0x9099, "PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it", inline=True)

# ============================================================
# FS response data relay (&9043)
# ============================================================
subroutine(0x9043, "net_write_char",
    title="FS response data relay (DOFS)",
    description="""\
Entered from the econet_tx_rx response handler at &903E after
loading the first data byte from the RX buffer. Saves the
command byte and station address from the received packet into
(net_rx_ptr)+&71/&72, then iterates through remaining data
bytes. Each byte is stored at (net_rx_ptr)+&7D, the control
block is set up via ctrl_block_setup_alt, and the packet is
transmitted. Loops until a &0D terminator or &00 null is found.
The branch at &9053 (BNE dofs2) handles the first-packet case
where the data length field at (net_rx_ptr)+&7B is adjusted.""")

comment(0x904A, "Store station addr hi at (net_rx_ptr)+&72", inline=True)
comment(0x9050, "Store station addr lo at (net_rx_ptr)+&71", inline=True)
comment(0x905F, "Store data byte at (net_rx_ptr)+&7D for TX", inline=True)
comment(0x9078, "Adjust data length by 3 for header bytes", inline=True)

# sub_c90b6 is the actual NWRCH dispatch handler (code 4).
comment(0x90B7, "ROR/ASL on stacked P: zeros carry to signal success", inline=True)
comment(0x90BE, "Store character at workspace offset &DA", inline=True)

# ============================================================
# Setup TX and send (&90B8)
# ============================================================
subroutine(0x90C4, "setup_tx_and_send", hook=None,
    title="Set up TX control block and send",
    description="""\
Stores A at workspace offset &D9 (command type), then sets byte
&0C to &80 (TX active flag). Saves the current net_tx_ptr,
temporarily redirects it to (nfs_workspace)+&0C so tx_poll_ff
transmits from the workspace TX control block. After transmission
completes, writes &3F (TX deleted) at (net_tx_ptr)+&00 to mark
the control block as free, then restores net_tx_ptr to its
original value.""")

comment(0x90C8, "Mark TX control block as active (&80)", inline=True)
comment(0x90CE, "Save net_tx_ptr; redirect to workspace TXCB", inline=True)
comment(0x90DD, "Mark TXCB as deleted (&3F) after transmit", inline=True)

# ============================================================
# Control block setup routine (&9168 / &9171)
# ============================================================
subroutine(0x917F, "ctrl_block_setup_alt", hook=None,
    title="Alternate entry into control block setup",
    description="""\
Sets X=&0D, Y=&7C. Tests bit 6 of &83B3 to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")

subroutine(0x9188, "ctrl_block_setup", hook=None,
    title="Control block setup — main entry",
    description="""\
Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &91B4 indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")

comment(0x918D, "Load template byte from ctrl_block_template[X]", inline=True)

subroutine(0x91B4, "ctrl_block_template", hook=None,
    title="Control block initialisation template",
    description="""\
Read by the loop at &918D, indexed by X from a starting value
down to 0. Values are stored into either (nfs_workspace) or
(net_rx_ptr) at offset Y, depending on the V flag.

Two entry paths read different slices of this table:
  ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
  ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &83B3

Sentinel values:
  &FE = stop processing
  &FD = skip this offset (decrement Y but don't store)
  &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)""")
byte(0x919D, 1)
comment(0x91B4, "Alt-path only → Y=&6F", inline=True)
byte(0x919E, 1)
comment(0x91AA, "Alt-path only → Y=&70", inline=True)
byte(0x919F, 1)
comment(0x91B6, "SKIP", inline=True)
byte(0x91A0, 1)
comment(0x91AC, "SKIP", inline=True)
byte(0x91A1, 1)
comment(0x91AD, "→ Y=&01 / Y=&73", inline=True)
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
comment(0x91B3, "→ Y=&07 / Y=&79", inline=True)
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
subroutine(0x8F24, "copy_param_block", hook=None,
    title="Bidirectional block copy between OSWORD param block and workspace.",
    description="""\
C=1: copy X+1 bytes from (&F0),Y to (&AB),Y (param to workspace)
C=0: copy X+1 bytes from (&AB),Y to (&F0),Y (workspace to param)""")
comment(0x8F1C, "C=0: skip param-to-workspace copy", inline=True)
comment(0x8F24, "Store to param block (no-op if C=1)", inline=True)

# ============================================================
# OSWORD handler block comments
# ============================================================
label(0x8F2A, "return_copy_param")       # Return from copy_param_block

subroutine(0x8EC2, "osword_0f_handler",
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
comment(0x8EC2, "ASL TXCLR: C=1 means TX free to claim", inline=True)
comment(0x8EC6, "C=0: TX busy, return error status", inline=True)

subroutine(0x8EDC, "osword_11_handler", hook=None,
    title="OSWORD &11 handler: read JSR arguments (READRA)",
    description="""\
Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8EE7) to return just the buffer size and args size
without copying the data.""")
comment(0x8EE0, "JSRSIZ at workspace offset &7F", inline=True)
comment(0x8EE4, "Y=&80: start of JSR argument data", inline=True)

subroutine(0x8E8D, "osword_12_handler", hook=None,
    title="OSWORD range check, dispatch, and register restore",
    description="""\
Reached by fall-through from svc_8_osword with A = OSWORD
number minus &0F. Rejects indices >= 5 (only OSWORDs &0F-&13
are handled). Dispatches to the appropriate handler via
fs_osword_dispatch, then on return copies 3 bytes from
(net_rx_ptr)+0..2 back to &AA-&AC (restoring the param block
pointer that was saved by fs_osword_dispatch before dispatch).

The actual OSWORD &12 sub-function dispatch (read/set station,
protection, handles etc.) lives in sub_c8f01.""")

subroutine(0x8F7C, "osword_10_handler",
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
comment(0x8F82, "Disable user RX during CB operation", inline=True)
comment(0x8F8B, "Start scan from RXCB #3 (0-2 reserved)", inline=True)
comment(0x8F99, "&3F = deleted slot, free for reuse", inline=True)
comment(0x8FC2, "Mark CB as consumed (consume-once)", inline=True)
comment(0x8FD1, "Re-enable user RX", inline=True)

# ============================================================
# Remote operation handlers (&846A-&84D1)
# ============================================================
subroutine(0x84AF, "lang_1_remote_boot", hook=None,
    title="Remote boot/execute handler",
    description="""\
Checks byte 4 of the RX control block (remote status flag).
If zero (not currently remoted), falls through to remot1 to
set up a new remote session. If non-zero (already remoted),
jumps to clear_jsr_protection and returns.""")
comment(0x84B8, "Set remote status: bits 0+3 (ORA #9)", inline=True)
comment(0x84C0, "Read source station lo from RX data at &80", inline=True)
comment(0x84C4, "Read source station hi from RX data at &81", inline=True)
comment(0x84C6, "Save controlling station to workspace &0E/&0F", inline=True)
comment(0x84D8, "Disable keyboard for remote session", inline=True)

subroutine(0x84DD, "lang_3_execute_at_0100", hook=None,
    title="Execute code at &0100",
    description="""\
Clears JSR protection, zeroes &0100-&0102 (creating a BRK
instruction at &0100 as a safe default), then JMP &0100 to
execute code received over the network. If no code was loaded,
the BRK triggers an error handler.""")
comment(0x84DD, "Allow JSR to page 1 (stack page)", inline=True)
comment(0x84E0, "Zero bytes &0100-&0102", inline=True)
comment(0x84E4, "BRK at &0100 as safe default", inline=True)
comment(0x84EA, "Execute downloaded code", inline=True)

subroutine(0x84ED, "lang_4_remote_validated", hook=None,
    title="Remote operation with source validation",
    description="""\
Validates that the source station in the received packet matches
the controlling station stored in the NFS workspace. If byte 4 of
the RX control block is zero (not currently remoted), allows the
new remote session via remot1. If non-zero, compares the source
station at RX offset &80 against workspace offset &0E -- rejects
mismatched stations via clear_jsr_protection, accepts matching
stations by falling through to lang_0_insert_remote_key.""")
comment(0x84F3, "Read source station from RX data at &80", inline=True)
comment(0x84F7, "Compare against controlling station at &0E", inline=True)
comment(0x84FB, "Reject: source != controlling station", inline=True)

subroutine(0x84FD, "lang_0_insert_remote_key", hook=None,
    title="Insert remote keypress",
    description="""\
Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")
comment(0x84FD, "Read keypress from RX data at &82", inline=True)
comment(0x8504, "Release JSR protection before inserting key", inline=True)

# ============================================================
# Remote operation support routines (&8FCA-&92FE)
# ============================================================
subroutine(0x8FD5, "setup_rx_buffer_ptrs", hook=None,
    title="Set up RX buffer pointers in NFS workspace",
    description="""\
Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &1C. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &20.""")

subroutine(0x90E8, "remote_cmd_dispatch", hook=None,
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

comment(0x90E8, "Load original Y (OSBYTE secondary param)", inline=True)
comment(0x90EA, "OSBYTE &81 (INKEY): always forward to terminal", inline=True)
comment(0x90EE, "Y=1: search NCTBPL table (execute on both)", inline=True)
comment(0x90F7, "Y=-1: search NCTBMI table (terminal only)", inline=True)
comment(0x9100, "Y=0: OSBYTE not recognised, ignore", inline=True)
comment(0x9101, "X=2 bytes to copy (default for RBYTE)", inline=True)
comment(0x9106, "Y>0 (NCTBPL): send only, no result expected", inline=True)
comment(0x9109, "Y<0 (NCTBMI): X=3 bytes (result + P flags)", inline=True)
comment(0x910C, "Copy OSBYTE args from stack frame to workspace", inline=True)
comment(0x911D, "Set up RX control block to wait for reply", inline=True)
comment(0x9123, "Poll for TX completion (wait for bit 7 set)", inline=True)
comment(0x912C, "Force V=1 (claimed) and I=1 (no IRQ) in saved P", inline=True)
comment(0x912E, "ALWAYS branch (ORA #&44 never zero)", inline=True)
comment(0x9134, "Write result bytes to stacked registers", inline=True)

subroutine(0x915C, "remote_cmd_data", hook=None,
    title="Fn 8: remote OSWORD handler (NWORD)",
    description="""\
Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget -- no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")

comment(0x9154, "Y=&0E: max 14 parameter bytes for OSWORD", inline=True)
comment(0x9156, "OSWORD 7 = make a sound", inline=True)
comment(0x915A, "OSWORD 8 = define an envelope", inline=True)
comment(0x915C, "Not OSWORD 7 or 8: ignore (BNE exits)", inline=True)
comment(0x915E, "Point workspace to offset &DB for params", inline=True)
comment(0x9162, "Copy parameter bytes from RX buffer", inline=True)
comment(0x916C, "Store original OSBYTE code at workspace+0", inline=True)
comment(0x9174, "Tag as RWORD (port &E9)", inline=True)

subroutine(0x91DB, "printer_select_handler", hook=None,
    title="Fn 5: printer selection changed (SELECT)",
    description="""\
Called when the printer selection changes. Compares X against
the network printer buffer number (&F0). If it matches,
initialises the printer buffer pointer (&0D61 = &1F) and
sets the initial flag byte (&0D60 = &41). Otherwise falls
through to return.""")

subroutine(0x91EA, "remote_print_handler", hook=None,
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

comment(0x91EA, "Only handle buffer 4 (network printer)", inline=True)
comment(0x91F3, "Force I flag in stacked P to block IRQs", inline=True)
comment(0x91F9, "OSBYTE &91: extract char from MOS buffer", inline=True)
comment(0x9206, "Buffer nearly full? (&6E = threshold)", inline=True)
comment(0x921A, "EOR #1: toggle print-active flag (bit 0)", inline=True)
comment(0x9221, "Test if sequence changed (bit 7 mismatch)", inline=True)
comment(0x922C, "Extract upper nibble of PFLAGS", inline=True)
comment(0x9231, "Merge print-active bit from original A", inline=True)
comment(0x9233, "Recombine into new PFLAGS value", inline=True)

subroutine(0x920F, "store_output_byte", hook=None,
    title="Store output byte to network buffer",
    description="""\
Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""")

subroutine(0x9237, "flush_output_block", hook=None,
    title="Flush output block",
    description="""\
Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")

comment(0x9237, "Store buffer length at workspace offset &08", inline=True)
comment(0x923E, "Store page high byte at offset &09", inline=True)
comment(0x9249, "X=&26: start from template entry &26", inline=True)
comment(0x924B, "Reuse ctrl_block_setup with CLV entry", inline=True)
comment(0x9254, "Toggle sequence number (bit 7 of PFLAGS)", inline=True)
comment(0x925D, "Reset printer buffer to start (&1F)", inline=True)

subroutine(0x92F7, "save_vdu_state", hook=None,
    title="Save VDU workspace state",
    description="""\
Stores the cursor position value from &0355 into NFS workspace,
then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
each result into consecutive workspace bytes. The JSR to
read_vdu_osbyte_x0 is a self-calling trick: it executes
read_vdu_osbyte twice (once for &C2, once for &C3) because the
RTS returns to the instruction at read_vdu_osbyte_x0 itself.""")
comment(0x92F7, "Read cursor editing state", inline=True)
comment(0x92FA, "Store to workspace[Y]", inline=True)
comment(0x92FC, "Preserve in X for OSBYTE", inline=True)
comment(0x92FD, "OSBYTE &85: read cursor position", inline=True)
comment(0x9300, "Advance workspace pointer", inline=True)
comment(0x9302, "Y result from OSBYTE &85", inline=True)
comment(0x9303, "Store Y pos to workspace (X=0)", inline=True)
comment(0x9305, "Self-call trick: executes twice", inline=True)
comment(0x9308, "X=0 for (zp,X) addressing", inline=True)
comment(0x930A, "Index into OSBYTE number table", inline=True)
comment(0x930C, "Next table entry next time", inline=True)
comment(0x930E, "Advance workspace pointer", inline=True)
comment(0x9310, "Read OSBYTE number from table", inline=True)
comment(0x9313, "Y=&FF: read current value", inline=True)
comment(0x9315, "Call OSBYTE", inline=True)
comment(0x9318, "Result in X to A", inline=True)
comment(0x9319, "X=0 for indexed indirect store", inline=True)
comment(0x931B, "Store result to workspace", inline=True)

comment(0x92AE, "Point workspace to palette save area (&E9)", inline=True)
comment(0x92B6, "Save current screen MODE to workspace", inline=True)
comment(0x92C8, "OSWORD &0B: read palette for logical colour", inline=True)
comment(0x92DF, "Loop until workspace wraps past &F9", inline=True)
comment(0x92E8, "Save cursor pos and OSBYTE state values", inline=True)
comment(0x92F0, "Restore LSTAT from saved OLDJSR value", inline=True)

# ============================================================
# ADLC initialisation (&967A)
# ============================================================
subroutine(0x967A, "adlc_init", hook=None,
    title="ADLC initialisation",
    description="""\
Reads station ID (INTOFF side effect), performs full ADLC reset,
checks for Tube presence (OSBYTE &EA), then falls through to
adlc_init_workspace.""")

subroutine(0x9695, "adlc_init_workspace", hook=None,
    title="Initialise NMI workspace",
    description="""\
Issues OSBYTE &8F with X=&0C (NMI claim service request) before
copying the NMI shim. Sub-entry at &9698 skips the service
request for quick re-init. Then copies 32 bytes of
NMI shim from ROM (&9F7D) to RAM (&0D00), patches the current
ROM bank number into the shim's self-modifying code at &0D07,
sets TX clear flag and econet_init_flag to &80, reads station ID
from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
and re-enables NMIs by reading &FE20 (INTON side effect).""")

comment(0x9698, "Copy 32 bytes of NMI shim from ROM to &0D00", inline=True)
comment(0x96A3, "Patch current ROM bank into NMI shim", inline=True)
comment(0x96A8, "&80 = Econet initialised", inline=True)
comment(0x96B0, "Read station ID (&FE18 = INTOFF side effect)", inline=True)
comment(0x96B6, "Y=0 after copy loop: net = local", inline=True)
comment(0x96B9, "Clear Tube release flag", inline=True)
comment(0x96BB, "INTON: re-enable NMIs (&FE20 read side effect)", inline=True)

# c9f57: service 12 entry -- spin-wait for idle NMI handler
# before releasing Econet. Checks that nmi_jmp points to
# nmi_rx_scout (&96BF), confirming no transfer is in progress.
comment(0x9F57, "Econet not initialised -- skip to adlc_rx_listen", inline=True)
comment(0x9F5C, "Spin until NMI handler = &96BF (nmi_rx_scout)", inline=True)
comment(0x9F6A, "INTOFF before clearing state", inline=True)

subroutine(0x9F6D, "save_econet_state", hook=None,
    title="Reset Econet flags and enter RX listen",
    description="""\
Disables NMIs via INTOFF (BIT &FE18), clears tx_clear_flag and
econet_init_flag to zero, then falls through to adlc_rx_listen
with Y=5.""")

# Initialisation sequence at &9698 issues OSBYTE &8F
# service request before copying the NMI shim from &9F7D to &0D00.

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
12-entry table at &0500). The R2 command byte is stored at &51
(self-modifying the JMP indirect low byte) before dispatch.""")

subroutine(0x0400, "tube_code_page4", hook=None,
    title="Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)",
    description="""\
Copied from ROM at &9362 during init. The first 28 bytes (&0400-&041B)
overlap with the end of the ZP block (the same ROM bytes serve both
the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
  &0400: JMP &0484 (BEGIN — startup/CLI entry, break type check)
  &0403: JMP &06E2 (tube_escape_check)
  &0406: tube_addr_claim — Tube address claim (ADRR protocol)
  &0414: sub_c0414 — release address claim via R4 command 5
  &0421: tube_post_init — reset claimed-address state to &80
  &0435: data transfer setup (SENDW protocol) — &0435-&0483
  &0484: BEGIN — startup entry, sends ROM contents to Tube
  &04D2: sub_c04d2 — extract relocation address from ROM table""")

subroutine(0x0500, "tube_dispatch_table", hook=None,
    title="Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)",
    description="""\
Copied from ROM at &9462 during init. Contains:
  &0500: 12-entry dispatch table (&0500-&0517)
  &0518: 8-byte Tube control register value table
  &0520: tube_osbput — write byte to file
  &052D: tube_osbget — read byte from file
  &0537: tube_osrdch — read character
  &053A: tube_rdch_reply — send carry+data as reply
  &0542: tube_osfind — open/close file
  &055E: tube_osargs — file argument read/write
  &0582: tube_read_string — read string from R2 into &0700
  &0596: tube_oscli — execute * command
  &059C: tube_reply_ack — send &7F acknowledge
  &05A9: tube_osfile — whole file operation
  &05D1: tube_osgbpb — multi-byte file read/write
Code continues seamlessly into page 6 (tube_osbyte_short at &05F2
straddles the page boundary with a BVC at &05FF/&0600).""")

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
# &9310-&9315 is code
# (read_vdu_osbyte: JSR osbyte; TXA; LDX #0).
# The osbyte_vdu_table is at different addresses in 3.40.

# ============================================================
# Relocated code block sources (&9321, &9362, &9462, &9562)
# ============================================================
# These labels mark the ROM storage addresses. The code is
# disassembled at its runtime addresses via move() declarations
# near the top of this file. See the preamble for addresses.

# ============================================================
# Byte-stream transmit (&9266)
# ============================================================
subroutine(0x9266, "econet_tx_retry", hook=None,
    title="Byte-stream transmit (BSXMIT/BSPSX)",
    description="""\
Transmits a data packet over econet with sequence number tracking.
Sets up the TX control block pointer from X/Y, computes the
sequence bit from A AND fs_sequence_nos (handle-based tracking),
merges it into the flag byte at (net_tx_ptr)+0, then initiates
transmit via tx_poll_ff. Sets end addresses (offsets 8/9) to
&FF to allow unlimited data. Selects port byte &D1 (print) or
&90 (FS) based on the original A value. Polls the TX result in
a loop via BRIANX (c8530), retrying while the result bit
differs from the expected sequence. On success, toggles the
sequence tracking bit in fs_sequence_nos.""")

comment(0x926B, "Compute sequence bit from handle", inline=True)
comment(0x9274, "Merge sequence into existing flag byte", inline=True)
comment(0x927C, "End address &FFFF = unlimited data length", inline=True)
comment(0x928B, "A=0: port &D1 (print); A!=0: port &90 (FS)", inline=True)
comment(0x92A0, "Check if TX result matches expected sequence", inline=True)
comment(0x92A7, "Toggle sequence bit on success", inline=True)

# ============================================================
# Save palette and VDU state (&929F)
# ============================================================
subroutine(0x92AB, "lang_2_save_palette_vdu", hook=None,
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
(OSBYTE &C3) using the 3-entry table at &931E.
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")

# ============================================================
# Post-ACK scout processing (&99C5)
# ============================================================
subroutine(0x993C, "post_ack_scout", hook=None,
    title="Post-ACK scout processing",
    description="""\
Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")

# ============================================================
# Immediate operation handler (&9A46)
# ============================================================
subroutine(0x9A46, "immediate_op", hook=None,
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
# Discard paths (&99DB / &99E8 / &9A46)
# ============================================================
subroutine(0x99DB, "discard_reset_listen", hook=None,
    title="Discard with Tube release",
    description="""\
Conditionally releases the Tube co-processor before discarding.
If tx_flags bit 1 is set (Tube transfer was active), calls
sub_c9a2b to release the Tube claim, then falls through to
discard_listen. The main teardown path for RX operations that
used the Tube.""")
comment(0x99DB, "Tube flag bit 1 AND tx_flags bit 1", inline=True)
comment(0x99E3, "No Tube transfer active -- skip release", inline=True)
comment(0x99E5, "Release Tube claim before discarding", inline=True)

subroutine(0x99E8, "discard_listen", hook=None,
    title="Discard frame and return to idle listen",
    description="""\
Calls adlc_rx_listen to re-enter idle RX mode (CR1=&82, CR2=&67),
then installs nmi_rx_scout (&96BF) as the NMI handler via
set_nmi_vector. Returns to the caller's NMI context. Used as
the common discard tail for both gentle rejection (wrong
station/network) and error recovery paths.""")
comment(0x99EB, "Install nmi_rx_scout (&96BF) as NMI handler", inline=True)

subroutine(0x9A46, "discard_after_reset", hook=None,
    title="Discard with immediate operation dispatch",
    description="""\
Co-located with immediate_op. After the scout ACK is sent for a
port-0 frame, this entry dispatches on the control byte via the
jump table at c99f8. Also reached as a discard path when the
immediate operation is not permitted by the protection mask.""")
comment(0x9A46, "Control byte &81-&88 range check", inline=True)
comment(0x9A55, "Convert ctrl byte to 0-based index for mask", inline=True)
comment(0x9A5A, "Load protection mask from LSTAT", inline=True)
comment(0x9A5D, "Rotate mask right by control byte index", inline=True)
comment(0x9A61, "Bit set = operation disabled, discard", inline=True)
comment(0x9A66, "PHA hi byte / PHA lo byte / RTS dispatch", inline=True)

# ============================================================
# Unreferenced data block (&9EBA-&9EC9)
# ============================================================
# 16 bytes of unreferenced data between tx_store_result and
# tx_calc_transfer. No code in any NFS version references this
# block. The byte pattern suggests two 8-entry lookup tables
# (possibly ADLC control register values), but their original
# purpose is unknown.
comment(0x9EBA, "Unreferenced data block (purpose unknown)")
byte(0x9F28, 16)

# ============================================================
# Transfer size calculation (&9ECA)
# ============================================================
subroutine(0x9ECA, "tx_calc_transfer", hook=None,
    title="Calculate transfer size",
    description="""\
Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")
comment(0x9ECA, "Load RXCB[6] (buffer addr byte 2)", inline=True)
comment(0x9ECF, "AND with RXCB[7] (byte 3)", inline=True)
comment(0x9ED1, "Both &FF = no buffer?", inline=True)
comment(0x9ED3, "Yes: fallback path", inline=True)
comment(0x9ED5, "Tube transfer in progress?", inline=True)
comment(0x9ED8, "No: fallback path", inline=True)
comment(0x9EDD, "Set bit 1 (transfer complete)", inline=True)
comment(0x9EE2, "Init borrow for 4-byte subtract", inline=True)
comment(0x9EE3, "Save carry on stack", inline=True)
comment(0x9EE4, "Y=4: start at RXCB offset 4", inline=True)
comment(0x9EE6, "Load RXCB[Y] (current ptr byte)", inline=True)
comment(0x9EE8, "Y += 4: advance to RXCB[Y+4]", inline=True)
comment(0x9EEC, "Restore borrow from previous byte", inline=True)
comment(0x9EED, "Subtract RXCB[Y+4] (start ptr byte)", inline=True)
comment(0x9EEF, "Store result byte", inline=True)
comment(0x9EF2, "Y -= 3: next source byte", inline=True)
comment(0x9EF5, "Save borrow for next byte", inline=True)
comment(0x9EF6, "Done all 4 bytes?", inline=True)
comment(0x9EF8, "No: next byte pair", inline=True)
comment(0x9EFA, "Discard final borrow", inline=True)
comment(0x9EFB, "A = saved X", inline=True)
comment(0x9EFC, "Save X", inline=True)
comment(0x9EFD, "Compute address of RXCB+4", inline=True)
comment(0x9F02, "X = low byte of RXCB+4", inline=True)
comment(0x9F03, "Y = high byte of RXCB ptr", inline=True)
comment(0x9F05, "Tube claim type &C2", inline=True)
comment(0x9F0A, "No Tube: skip reclaim", inline=True)
comment(0x9F0C, "Tube: reclaim with scout status", inline=True)
comment(0x9F15, "C=1: Tube address claimed", inline=True)
comment(0x9F16, "Restore X", inline=True)
comment(0x9F1B, "Load RXCB[4] (current ptr lo)", inline=True)
comment(0x9F20, "Subtract RXCB[8] (start ptr lo)", inline=True)
comment(0x9F22, "Store transfer size lo", inline=True)
comment(0x9F26, "Load RXCB[5] (current ptr hi)", inline=True)
comment(0x9F28, "Propagate borrow only", inline=True)
# Inline comments removed — &9F28-&9F37 is data in 3.60, not code
comment(0x9F39, "Store transfer size hi", inline=True)
comment(0x9F3B, "Return with C=1", inline=True)

# ============================================================
# NMI shim at end of ROM (&9F7D-&9F9C)
# ============================================================
subroutine(0x9F7D, "nmi_bootstrap_entry", hook=None,
    title="Bootstrap NMI entry point (in ROM)",
    description="""\
An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&96BF). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &96BF.""")
comment(0x9F83, "ROM bank 0 (patched during init for actual bank)", inline=True)

subroutine(0x9F8B, "rom_set_nmi_vector", hook=None,
    title="ROM copy of set_nmi_vector + nmi_rti",
    description="""\
A version of the NMI vector-setting subroutine and RTI sequence
that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
one normally used at runtime; this ROM copy is used during early
initialisation before the RAM workspace has been set up, and as
the source for the initial copy to RAM.""")
comment(0x9F8B, "Store handler high byte at &0D0D", inline=True)
comment(0x9F8E, "Store handler low byte at &0D0C", inline=True)
# nmi_rti sequence: restore ROM bank, registers, re-enable NMIs
comment(0x9F91, "Restore NFS ROM bank", inline=True)
comment(0x9F93, "Page in via hardware latch", inline=True)
comment(0x9F96, "Restore Y from stack", inline=True)
comment(0x9F98, "Restore A from stack", inline=True)
comment(0x9F99, "INTON: re-enable NMIs", inline=True)
comment(0x9F9C, "Return from interrupt", inline=True)

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
# ADLC full reset (&9F3D)
# ============================================================
# In 3.60, adlc_full_reset and adlc_rx_listen relocated to
# end-of-ROM (&9F3D / &9F4C).
subroutine(0x9F3D, "adlc_full_reset", hook=None,
    title="ADLC full reset",
    description="""\
Aborts all activity and returns to idle RX listen mode.""")

comment(0x9F3D, "CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)", inline=True)
comment(0x9F42, "CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding", inline=True)
comment(0x9F47, "CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR", inline=True)

# ============================================================
# Enter RX listen mode (&9F4C)
# ============================================================
subroutine(0x9F4C, "adlc_rx_listen", hook=None,
    title="Enter RX listen mode",
    description="""\
TX held in reset, RX active with interrupts. Clears all status.""")

comment(0x9F4C, "CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)", inline=True)
comment(0x9F51, "CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE", inline=True)

# ============================================================
# NMI RX scout handler (&96BF) — idle listen
# ============================================================
subroutine(0x96BF, "nmi_rx_scout", hook=None,
    title="NMI RX scout handler (initial byte)",
    description="""\
Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")

comment(0x96BF, "A=&01: mask for SR2 bit0 (AP = Address Present)", inline=True)
comment(0x96C1, "BIT SR2: Z = A AND SR2 -- tests if AP is set", inline=True)
comment(0x96C4, "AP not set, no incoming data -- check for errors", inline=True)
comment(0x96C6, "Read first RX byte (destination station address)", inline=True)
comment(0x96C9, "Compare to our station ID (&FE18 read = INTOFF, disables NMIs)", inline=True)
comment(0x96CC, "Match -- accept frame", inline=True)
comment(0x96CE, "Check for broadcast address (&FF)", inline=True)
comment(0x96D0, "Neither our address nor broadcast -- reject frame", inline=True)
comment(0x96D2, "Flag &40 = broadcast frame", inline=True)
comment(0x96D7, "Install next NMI handler at &96DC (RX scout net byte)", inline=True)

# ============================================================
# RX scout second byte handler (&96DC)
# ============================================================
subroutine(0x96DC, "nmi_rx_scout_net", hook=None,
    title="RX scout second byte handler",
    description="""\
Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &970E.""")

comment(0x96DC, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x96DF, "No RDA -- check errors", inline=True)
comment(0x96E1, "Read destination network byte", inline=True)
comment(0x96E4, "Network = 0 -- local network, accept", inline=True)
comment(0x96E6, "EOR &FF: test if network = &FF (broadcast)", inline=True)
comment(0x96E8, "Broadcast network -- accept", inline=True)
comment(0x96EA, "Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE", inline=True)

comment(0x96F2, "Network = 0 (local): clear tx_flags", inline=True)
comment(0x96F5, "Store Y offset for scout data buffer", inline=True)
comment(0x96F7, "Install scout data reading loop at &970E", inline=True)

# ============================================================
# Error/discard path (&96FE)
# ============================================================
subroutine(0x96FE, "scout_error", hook=None,
    title="Scout error/discard handler",
    description="""\
Reached when the scout data loop sees no RDA (BPL at &9713) or
when scout completion finds unexpected SR2 state.
If SR2 & &81 is non-zero (AP or RDA still active), performs full
ADLC reset and discards. If zero (clean end), discards via &99E8.
This path is a common landing for any unexpected ADLC state during
scout reception.""")

comment(0x96FE, "Read SR2", inline=True)
comment(0x9701, "Test AP (b0) | RDA (b7)", inline=True)
comment(0x9703, "Neither set -- clean end, discard via &99E8", inline=True)
comment(0x9705, "Unexpected data/status: full ADLC reset", inline=True)
comment(0x9708, "Discard and return to idle", inline=True)

# ============================================================
# Scout data reading loop (&970E-&9735)
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
subroutine(0x970E, hook=None,
    title="Scout data reading loop",
    description="""\
Reads the body of a scout frame, two bytes per iteration. Stores
bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
Between each pair it checks SR2:
  - At entry (&9710): SR2 read, BPL tests RDA (bit7)
    - No RDA (BPL) -> error (&96FE)
    - RDA set (BMI) -> read byte
  - After first byte (&971C): full SR2 tested
    - SR2 non-zero (BNE) -> scout completion (&9738)
      This is the FV detection point: when FV is set (by inline refill
      of the last byte during the preceding RX FIFO read), SR2 is
      non-zero and the branch is taken.
    - SR2 = 0 -> read second byte and loop
  - After second byte (&9730): re-test full SR2
    - SR2 non-zero (BNE) -> loop back to &9713
    - SR2 = 0 -> RTI, wait for next NMI
The loop ends at Y=&0C (12 bytes max in scout buffer).""")

comment(0x970E, "Y = buffer offset", inline=True)
comment(0x9710, "Read SR2", inline=True)
comment(0x9713, "No RDA -- error handler &96FE", inline=True)
comment(0x9715, "Read data byte from RX FIFO", inline=True)
comment(0x9718, "Store at &0D3D+Y (scout buffer)", inline=True)
comment(0x971B, "Advance buffer index", inline=True)
comment(0x971C, "Read SR2 again (FV detection point)", inline=True)
comment(0x971F, "RDA set -- more data, read second byte", inline=True)
comment(0x9721, "SR2 non-zero (FV or other) -- scout completion", inline=True)
comment(0x9723, "Read second byte of pair", inline=True)
comment(0x9726, "Store at &0D3D+Y", inline=True)
comment(0x9729, "Advance and check buffer limit", inline=True)
comment(0x972C, "Buffer full (Y=12) -- force completion", inline=True)
comment(0x9730, "Read SR2 for next pair", inline=True)
comment(0x9733, "SR2 non-zero -- loop back for more bytes", inline=True)
comment(0x9735, "SR2 = 0 -- RTI, wait for next NMI", inline=True)

# ============================================================
# Scout completion (&9738-&975E)
# ============================================================
subroutine(0x9738, "scout_complete", hook=None,
    title="Scout completion handler",
    description="""\
Reached from the scout data loop when SR2 is non-zero (FV detected).
Disables PSE to allow individual SR2 bit testing:
  CR1=&00 (clear all enables)
  CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
Then checks FV (bit1) and RDA (bit7):
  - No FV (BEQ) -> error &96FE (not a valid frame end)
  - FV set, no RDA (BPL) -> error &96FE (missing last byte)
  - FV set, RDA set -> read last byte, process scout
After reading the last byte, the complete scout buffer (&0D3D-&0D48)
contains: src_stn, src_net, ctrl, port [, extra_data...].
The port byte at &0D40 determines further processing:
  - Port = 0 -> immediate operation (&9A46)
  - Port non-zero -> check if it matches an open receive block""")

comment(0x9738, "CR1=&00: disable all interrupts", inline=True)
comment(0x973D, "CR2=&84: disable PSE, enable RDA_SUPPRESS_FV", inline=True)
comment(0x9742, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9744, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x9747, "No FV -- not a valid frame end, error", inline=True)
comment(0x9749, "FV set but no RDA -- missing last byte, error", inline=True)
comment(0x974B, "Read last byte from RX FIFO", inline=True)
comment(0x974E, "Store last byte at &0D3D+Y", inline=True)
comment(0x9751, "CR1=&44: RX_RESET | TIE (switch to TX for ACK)", inline=True)
comment(0x9759, "Check port byte: 0 = immediate op, non-zero = data transfer", inline=True)
comment(0x975C, "Port non-zero -- look for matching receive block", inline=True)
comment(0x975E, "Port = 0 -- immediate operation handler", inline=True)
comment(0x9756, "Set bit7 of need_release_tube flag", inline=True)
comment(0x9761, "Check if broadcast (bit6 of tx_flags)", inline=True)
comment(0x9766, "CR2=&07: broadcast prep", inline=True)
comment(0x976B, "Check if RX port list active (bit7)", inline=True)
comment(0x976E, "No active ports -- try NFS workspace", inline=True)
comment(0x9770, "Start scanning port list at page &C0", inline=True)
comment(0x977A, "Read port control byte from slot", inline=True)
comment(0x977C, "Zero = end of port list, no match", inline=True)
comment(0x977E, "&7F = any-port wildcard", inline=True)
comment(0x9787, "Check if port matches this slot", inline=True)
comment(0x9791, "Check if source station matches", inline=True)
comment(0x9799, "Check if source network matches", inline=True)
comment(0x97A5, "Advance to next 12-byte port slot", inline=True)
comment(0x97AE, "Try NFS workspace if paged list exhausted", inline=True)
comment(0x97B5, "NFS workspace high byte for port list", inline=True)
comment(0x97B9, "Match found: set scout_status = 3", inline=True)
comment(0x97BE, "Calculate transfer parameters", inline=True)
comment(0x97CB, "CR1=&44: RX_RESET | TIE", inline=True)
comment(0x97D0, "CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE", inline=True)
comment(0x97D5, "Install data_rx_setup at &97DC", inline=True)

# ============================================================
# Data RX handler (&97E6-&9840)
# ============================================================
# This handler chain receives the data frame in a four-way handshake.
# After sending the scout ACK, the ROM installs &97E6 to receive
# the incoming data frame.
subroutine(0x97E6, "nmi_data_rx", hook=None,
    title="Data frame RX handler (four-way handshake)",
    description="""\
Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &97E6 (AP+addr check) -> &97FA (net=0 check) ->
&9810 (skip ctrl+port) -> &9843 (bulk data read) -> &9877 (completion)""")

comment(0x97DC, "CR1=&82: TX_RESET | RIE (switch to RX for data frame)", inline=True)
comment(0x97E1, "Install nmi_data_rx at &97E6", inline=True)
comment(0x97E6, "A=&01: mask for AP (Address Present)", inline=True)
comment(0x97F5, "Install net check handler at &97FA", inline=True)
comment(0x97FA, "Validate source network = 0", inline=True)
comment(0x9804, "Install skip handler at &9810", inline=True)
comment(0x9808, "SR1 bit7: IRQ, data already waiting", inline=True)
comment(0x9810, "Skip control and port bytes (already known from scout)", inline=True)
comment(0x9815, "Discard control byte", inline=True)
comment(0x9818, "Discard port byte", inline=True)

# ============================================================
# Data frame bulk read (&9843-&9874)
# ============================================================
subroutine(0x9843, "nmi_data_rx_bulk", hook=None,
    title="Data frame bulk read loop",
    description="""\
Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &9877.
SR2 = 0 -> RTI, wait for next NMI to continue.""")

comment(0x9843, "Y = buffer offset, resume from last position", inline=True)
comment(0x9845, "Read SR2 for next pair", inline=True)

# ============================================================
# Data frame completion (&9877-&989D)
# ============================================================
subroutine(0x9877, "data_rx_complete", hook=None,
    title="Data frame completion",
    description="""\
Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&9738): disables PSE (CR2=&84,
CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &98EE.""")

comment(0x9877, "CR2=&84: disable PSE for individual bit testing", inline=True)
comment(0x987C, "CR1=&00: disable all interrupts", inline=True)
comment(0x9883, "A=&02: FV mask", inline=True)
comment(0x9885, "BIT SR2: test FV (Z) and RDA (N)", inline=True)
comment(0x9888, "No FV -- error", inline=True)
comment(0x988A, "FV set, no RDA -- proceed to ACK", inline=True)
comment(0x9890, "FV+RDA: read and store last data byte", inline=True)

# ============================================================
# Scout ACK / Final ACK TX (&98EE-&9922)
# ============================================================
subroutine(0x98EE, "ack_tx", hook=None,
    title="ACK transmission",
    description="""\
Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&9EA8).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")

comment(0x98F9, "CR1=&44: RX_RESET | TIE (switch to TX mode)", inline=True)
comment(0x98FE, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x9903, "Save &9995 (post-ACK port check) in &0D4B/&0D4C", inline=True)
comment(0x990D, "Load dest station from RX scout buffer", inline=True)
comment(0x9910, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9913, "TDRA not ready -- error", inline=True)
comment(0x9915, "Write dest station to TX FIFO", inline=True)
comment(0x9918, "Write dest network to TX FIFO", inline=True)
comment(0x991E, "Install nmi_ack_tx_src at &9925", inline=True)

subroutine(0x9925, "nmi_ack_tx_src", hook=None,
    title="ACK TX continuation",
    description="""\
Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
comment(0x9925, "Load our station ID (also INTOFF)", inline=True)
comment(0x9928, "BIT SR1: test TDRA", inline=True)
comment(0x992B, "TDRA not ready -- error", inline=True)
comment(0x992D, "Write our station to TX FIFO", inline=True)
comment(0x9930, "Write network=0 to TX FIFO", inline=True)
comment(0x993A, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | PSE", inline=True)
comment(0x993F, "Install saved handler from &0D4B/&0D4C", inline=True)

# ============================================================
# INACTIVE polling loop (&9BD6)
# ============================================================
subroutine(0x9BD6, "inactive_poll", hook=None,
    title="INACTIVE polling loop",
    description="""\
Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9BF4-&9BF9 works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")

comment(0x9BDB, "Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9BDD, "A=&04: INACTIVE mask for SR2 bit2", inline=True)
comment(0x9BE1, "INTOFF -- disable NMIs", inline=True)
comment(0x9BE4, "INTOFF again (belt-and-braces)", inline=True)
comment(0x9BE7, "BIT SR2: Z = &04 AND SR2 -- tests INACTIVE", inline=True)
comment(0x9BEA, "INACTIVE not set -- re-enable NMIs and loop", inline=True)
comment(0x9BEC, "Read SR1 (acknowledge pending interrupt)", inline=True)
comment(0x9BEF, "CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE", inline=True)
comment(0x9BF4, "A=&10: CTS mask for SR1 bit4", inline=True)
comment(0x9BF6, "BIT SR1: tests CTS present", inline=True)
comment(0x9BF9, "CTS set -- clock hardware detected, start TX", inline=True)
comment(0x9BFB, "INTON -- re-enable NMIs (&FE20 read)", inline=True)
comment(0x9BFF, "3-byte timeout counter on stack", inline=True)

# ============================================================
# Timeout error (&9C15) and TX setup (&9C2F)
# ============================================================
comment(0x9C11, "TX_ACTIVE branch (A=&44 = CR1 value for TX active)")
subroutine(0x9C15, "tx_line_jammed", hook=None,
    title="TX timeout error handler (Line Jammed)",
    description="""\
Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")

comment(0x9C15, "CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)", inline=True)
comment(0x9C1D, "Error &40 = 'Line Jammed'", inline=True)

# ============================================================
# TX preparation (&9C2F)
# ============================================================
subroutine(0x9C2F, "tx_prepare", hook=None,
    title="TX preparation",
    description="""\
Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9CCC (nmi_tx_data), and re-enables NMIs.
For port-0 (immediate) operations, dispatches via a lookup table indexed
by control byte to set tx_flags, tx_length, and a per-operation handler.
For port non-zero, branches to c9c8e for standard data transfer setup.""")

comment(0x9C2F, "Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)", inline=True)
comment(0x9C32, "CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)", inline=True)
comment(0x9C37, "Install NMI handler at &9CCC (nmi_tx_data)", inline=True)
comment(0x9C41, "Set need_release_tube flag (SEC/ROR = bit7)", inline=True)
comment(0x9C44, "INTON -- NMIs now fire for TDRA (&FE20 read)", inline=True)

# ============================================================
# NMI TX data handler (&9CCC)
# ============================================================
subroutine(0x9CCC, "nmi_tx_data", hook=None,
    title="NMI TX data handler",
    description="""\
Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")

comment(0x9CCC, "Load TX buffer index", inline=True)
comment(0x9CCF, "BIT SR1: V=bit6(TDRA), N=bit7(IRQ)", inline=True)
comment(0x9CD2, "TDRA not set -- TX error", inline=True)
comment(0x9CD4, "Load byte from TX buffer", inline=True)
comment(0x9CD7, "Write to TX_DATA (continue frame)", inline=True)
comment(0x9CE2, "Write second byte to TX_DATA", inline=True)
comment(0x9CE5, "Compare index to TX length", inline=True)
comment(0x9CE8, "Frame complete -- go to TX_LAST_DATA", inline=True)
comment(0x9CEA, "Check if we can send another pair", inline=True)
comment(0x9CED, "IRQ set -- send 2 more bytes (tight loop)", inline=True)
comment(0x9CEF, "RTI -- wait for next NMI", inline=True)

# TX error path (&9CF2-&9D05)
comment(0x9CF2, "TX error path")
comment(0x9CF2, "Error &42", inline=True)
comment(0x9CF6, "CR2=&67: clear status, return to listen", inline=True)
comment(0x9CFB, "Error &41 (TDRA not ready)", inline=True)
comment(0x9CFD, "INTOFF (also loads station ID)", inline=True)
comment(0x9D00, "PHA/PLA delay loop (256 iterations for NMI disable)", inline=True)

# ============================================================
# TX_LAST_DATA and frame completion (&9D08)
# ============================================================
subroutine(0x9D08, "tx_last_data", hook=None,
    title="TX_LAST_DATA and frame completion",
    description="""\
Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &9D14 (nmi_tx_complete).
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)""")

comment(0x9D08, "CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE", inline=True)
comment(0x9D0D, "Install NMI handler at &9D14 (nmi_tx_complete)", inline=True)

# ============================================================
# TX completion: switch to RX mode (&9D14)
# ============================================================
subroutine(0x9D14, "nmi_tx_complete", hook=None,
    title="TX completion: switch to RX mode",
    description="""\
Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> tx_result_ok at &9EA8
  - bit0 set at &0D4A -> handshake_await_ack at &9E50
  - Otherwise -> install nmi_reply_scout at &9D30""")

comment(0x9D14, "CR1=&82: TX_RESET | RIE (now in RX mode)", inline=True)
comment(0x9D19, "Test workspace flags", inline=True)
comment(0x9D1C, "bit6 not set -- check bit0", inline=True)
comment(0x9D1E, "bit6 set -- TX completion", inline=True)
comment(0x9D28, "bit0 set -- four-way handshake data phase", inline=True)
comment(0x9D2B, "Install nmi_reply_scout at &9D30", inline=True)

# ============================================================
# RX reply scout handler (&9D30)
# ============================================================
subroutine(0x9D30, "nmi_reply_scout", hook=None,
    title="RX reply scout handler",
    description="""\
Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")

comment(0x9D30, "A=&01: AP mask for SR2", inline=True)
comment(0x9D32, "BIT SR2: test AP (Address Present)", inline=True)
comment(0x9D35, "No AP -- error", inline=True)
comment(0x9D37, "Read first RX byte (destination station)", inline=True)
comment(0x9D3A, "Compare to our station ID (INTOFF side effect)", inline=True)
comment(0x9D3D, "Not our station -- error/reject", inline=True)
comment(0x9D3F, "Install nmi_reply_cont at &9D44", inline=True)

# ============================================================
# RX reply continuation handler (&9D44)
# ============================================================
subroutine(0x9D44, "nmi_reply_cont", hook=None,
    title="RX reply continuation handler",
    description="""\
Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs nmi_reply_validate
(&9D5B) for the remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9D53.
If IRQ is still set, falls through directly to &9D5B without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")

comment(0x9D44, "BIT SR2: test for RDA (bit7 = data available)", inline=True)
comment(0x9D47, "No RDA -- error", inline=True)
comment(0x9D49, "Read destination network byte", inline=True)
comment(0x9D4C, "Non-zero -- network mismatch, error", inline=True)
comment(0x9D4E, "Install nmi_reply_validate at &9D5B", inline=True)
comment(0x9D50, "BIT SR1: test IRQ (N=bit7) -- more data ready?", inline=True)
comment(0x9D53, "IRQ set -- fall through to &9D5B without RTI", inline=True)
comment(0x9D55, "IRQ not set -- install handler and RTI", inline=True)

# ============================================================
# RX reply validation handler (&9D5B)
# ============================================================
# This is the critical Path 2 code for ADLC FV/PSE interaction.
# The handler reads two bytes (source station and network) and
# then checks for FV. The key requirement is that RDA must be
# visible at &9D5B even if FV has been latched.
#
# With Beebium's inline refill model, this works because the
# inline refill chain feeds bytes in rapid succession: each FIFO
# read refills the next byte. For a 4-byte reply scout:
#   Read byte 0 at &9D37 -> refills byte 1 (RDA visible at &9D44)
#   Read byte 1 at &9D49 -> refills byte 2 (RDA visible at &9D5B)
#   Read byte 2 at &9D60 -> refills byte 3/LAST (FV set)
#   Read byte 3 at &9D68 -> FIFO empty
#   Check FV at &9D72 -> FV is set
subroutine(0x9D5B, "nmi_reply_validate", hook=None,
    title="RX reply validation (Path 2 for FV/PSE interaction)",
    description="""\
Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &9D5B -- must see data available
  2. Read source station at &9D60, compare to &0D20 (tx_dst_stn)
  3. Read source network at &9D68, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &9D72 -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")

comment(0x9D5B, "BIT SR2: test RDA (bit7). Must be set for valid reply.", inline=True)
comment(0x9D5E, "No RDA -- error (FV masking RDA via PSE would cause this)", inline=True)
comment(0x9D60, "Read source station", inline=True)
comment(0x9D63, "Compare to original TX destination station (&0D20)", inline=True)
comment(0x9D66, "Mismatch -- not the expected reply, error", inline=True)
comment(0x9D68, "Read source network", inline=True)
comment(0x9D6B, "Compare to original TX destination network (&0D21)", inline=True)
comment(0x9D6E, "Mismatch -- error", inline=True)
comment(0x9D70, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9D72, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9D75, "No FV -- incomplete frame, error", inline=True)
comment(0x9D77, "CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)", inline=True)
comment(0x9D7C, "CR1=&44: RX_RESET | TIE (TX active for scout ACK)", inline=True)
comment(0x9D81, "Save handshake_await_ack (&9E50) in &0D4B/&0D4C", inline=True)
comment(0x9D8B, "Load dest station for scout ACK TX", inline=True)
comment(0x9D8E, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9D91, "TDRA not ready -- error", inline=True)
comment(0x9D93, "Write dest station to TX FIFO", inline=True)
comment(0x9D96, "Write dest network to TX FIFO", inline=True)
comment(0x9D9C, "Install nmi_scout_ack_src at &9DA3", inline=True)

# ============================================================
# TX data phase: write src address (&9DA3)
# ============================================================
subroutine(0x9DA3, "nmi_scout_ack_src", hook=None,
    title="TX scout ACK: write source address",
    description="""\
Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
comment(0x9DA3, "Load our station ID (also INTOFF)", inline=True)
comment(0x9DA6, "BIT SR1: test TDRA", inline=True)
comment(0x9DA9, "TDRA not ready -- error", inline=True)
comment(0x9DAB, "Write our station to TX FIFO", inline=True)
comment(0x9DAE, "Write network=0 to TX FIFO", inline=True)

# ============================================================
# TX data phase: send data payload (&9DC8)
# ============================================================
subroutine(0x9DC8, "nmi_data_tx", hook=None,
    title="TX data phase: send payload",
    description="""\
Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9CCC but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
comment(0x9DC8, "Y = buffer offset, resume from last position", inline=True)
comment(0x9DCA, "BIT SR1: test TDRA (V=bit6)", inline=True)
comment(0x9DCD, "TDRA not ready -- error", inline=True)
comment(0x9DCF, "Write data byte to TX FIFO", inline=True)
comment(0x9DF5, "CR2=&3F: TX_LAST_DATA (close data frame)", inline=True)

# ============================================================
# Four-way handshake: switch to RX for final ACK (&9E50)
# ============================================================
subroutine(0x9E50, "handshake_await_ack", hook=None,
    title="Four-way handshake: switch to RX for final ACK",
    description="""\
After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9EF8 to receive the final ACK from the remote station.""")
comment(0x9E50, "CR1=&82: TX_RESET | RIE (switch to RX for final ACK)", inline=True)
comment(0x9E55, "Install nmi_final_ack at &9E5C", inline=True)

# ============================================================
# Four-way handshake: RX final ACK (&9E5C-&9EA6)
# ============================================================
# Same pattern as &9D30/&9D44/&9D5B but for the final ACK.
# Validates that the final ACK is from the expected station.
subroutine(0x9E5C, "nmi_final_ack", hook=None,
    title="RX final ACK handler",
    description="""\
Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9D30-&9D5B):
  &9E5C: Check AP, read dest_stn, compare to our station
  &9E70: Check RDA, read dest_net, validate = 0
  &9E84: Check RDA, read src_stn/net, compare to TX dest
  &9EA3: Check FV for frame completion
On success, stores result=0 at tx_result_ok. On failure, error &41.""")

comment(0x9E5C, "A=&01: AP mask", inline=True)
comment(0x9E5E, "BIT SR2: test AP", inline=True)
comment(0x9E61, "No AP -- error", inline=True)
comment(0x9E63, "Read dest station", inline=True)
comment(0x9E66, "Compare to our station (INTOFF side effect)", inline=True)
comment(0x9E69, "Not our station -- error", inline=True)
comment(0x9E6B, "Install nmi_final_ack_net at &9E70", inline=True)

comment(0x9E70, "BIT SR2: test RDA", inline=True)
comment(0x9E73, "No RDA -- error", inline=True)
comment(0x9E75, "Read dest network", inline=True)
comment(0x9E78, "Non-zero -- network mismatch, error", inline=True)
comment(0x9E7A, "Install nmi_final_ack_validate at &9E84", inline=True)
comment(0x9E7C, "BIT SR1: test IRQ -- more data ready?", inline=True)
comment(0x9E7F, "IRQ set -- fall through to &9E84 without RTI", inline=True)

subroutine(0x9E84, "nmi_final_ack_validate", hook=None,
    title="Final ACK validation",
    description="""\
Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
comment(0x9E84, "BIT SR2: test RDA", inline=True)
comment(0x9E87, "No RDA -- error", inline=True)
comment(0x9E89, "Read source station", inline=True)
comment(0x9E8C, "Compare to TX dest station (&0D20)", inline=True)
comment(0x9E8F, "Mismatch -- error", inline=True)
comment(0x9E91, "Read source network", inline=True)
comment(0x9E94, "Compare to TX dest network (&0D21)", inline=True)
comment(0x9E97, "Mismatch -- error", inline=True)
comment(0x9EA1, "A=&02: FV mask for SR2 bit1", inline=True)
comment(0x9EA3, "BIT SR2: test FV -- frame must be complete", inline=True)
comment(0x9EA6, "No FV -- error", inline=True)

# ============================================================
# Completion and error handlers (&9EA8-&9EB7)
# ============================================================
subroutine(0x9EA8, "tx_result_ok", hook=None,
    title="TX completion handler",
    description="""\
Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls discard_reset_listen to return to idle.""")
comment(0x9EA8, "A=0: success result code", inline=True)
comment(0x9EAA, "BEQ: always taken (A=0)", inline=True)

subroutine(0x9EAE, "tx_store_result", hook=None,
    title="TX error handler",
    description="""\
Stores error code (A) into the TX control block, sets &0D3A bit7
for completion, and returns to idle via discard_reset_listen.
Error codes: &00=success, &40=line jammed, &41=not listening,
&42=net error.""")
comment(0x9EAE, "Y=0: index into TX control block", inline=True)
comment(0x9EB0, "Store result/error code at (nmi_tx_block),0", inline=True)
comment(0x9EB2, "&80: completion flag for &0D3A", inline=True)
comment(0x9EB4, "Signal TX complete", inline=True)
comment(0x9EB7, "Full ADLC reset and return to idle listen", inline=True)

# ============================================================
# Generate disassembly
# ============================================================

import json
import sys

output = go(print_output=False)

_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / "nfs-3.60.asm"
output_filepath.write_text(output)
print(f"Wrote {output_filepath}", file=sys.stderr)

structured = get_structured()
json_filepath = _output_dirpath / "nfs-3.60.json"
json_filepath.write_text(json.dumps(structured))
print(f"Wrote {json_filepath}", file=sys.stderr)
