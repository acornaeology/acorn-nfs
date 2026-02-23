# Glossary

Acorn-specific terms used in this project's documentation and annotations.
See the [BBC Micro Advanced User Guide](http://stardot.org.uk/mirrors/www.bbcdocs.com/filebase/essentials/BBC%20Microcomputer%20Advanced%20User%20Guide.pdf)
for full descriptions of the MOS API and vector system.

## MOS vectors

**BRKV** (Break Vector)
: MOS vector at &0202. Called when a BRK instruction is executed, typically
for error handling. NFS installs its own BRK handler to process network errors.

**EVNTV** (Event Vector)
: MOS vector at &0220. Called when an enabled event occurs. NFS uses this for
Econet event handling.

**FSCV** (Filing System Control Vector)
: MOS vector at &021E. Called for filing system control operations including
`*RUN`, `*/`, and unrecognised `*` commands. NFS intercepts this to forward
commands to the fileserver.

**FILEV** (File Vector)
: MOS vector at &0212. Called for whole-file operations (OSFILE). NFS
intercepts this to handle remote file loading and saving.

**ARGSV** (Arguments Vector)
: MOS vector at &0214. Called for open-file argument operations (OSARGS). NFS
intercepts this for remote file handles.

**BGETV** (Byte Get Vector)
: MOS vector at &0216. Called for single-byte file reads (OSBGET). NFS
intercepts this for remote file reading.

**BPUTV** (Byte Put Vector)
: MOS vector at &0218. Called for single-byte file writes (OSBPUT). NFS
intercepts this for remote file writing.

**FINDV** (Find Vector)
: MOS vector at &021C. Called for file open/close operations (OSFIND). NFS
intercepts this for remote file handle management.

**GBPBV** (Get/Put Byte Vector)
: MOS vector at &021A. Called for multi-byte file transfers (OSGBPB). NFS
intercepts this for remote block transfers.

**NETV** (Network Vector)
: MOS vector at &0224. Called for Econet network operations. Used by the
Econet module for low-level network I/O.

**RDCHV** (Read Character Vector)
: MOS vector at &0210. Called when OSRDCH reads a character from input. NFS
intercepts this to support remote input during Tube operations.

**WRCHV** (Write Character Vector)
: MOS vector at &020E. Called when OSWRCH writes a character to output. NFS
intercepts this to redirect character output during Tube operations.

## MOS API calls

**GSINIT** (General String Input Initialise)
: MOS routine at &FFC2. Initialises the string input state for parsing a
command-line argument. Used with GSREAD to handle quoted strings and escape
characters.

**GSREAD** (General String Read)
: MOS routine at &FFC5. Reads the next character from a command-line argument
previously set up by GSINIT. Handles `|`-escaped special characters and
quoted strings.

**OSBYTE** (OS Byte)
: MOS routine at &FFF4. Performs miscellaneous OS operations selected by the
accumulator value. NFS uses OSBYTE calls for keyboard control, handle
queries, and ROM management.

**OSCLI** (OS Command Line Interpreter)
: MOS routine at &FFF7. Executes a `*` command string. NFS uses internal
OSCLI calls to dispatch the `*NET1`-`*NET4` sub-commands.

**OSRDCH** (OS Read Character)
: MOS routine at &FFE0. Reads a single character from the current input
stream. Used by NFS 3.35D for interactive colon-command input.

**OSWRCH** (OS Write Character)
: MOS routine at &FFEE. Writes a single character to the current output
stream.

**OSWORD** (OS Word)
: MOS routine at &FFF1. Performs OS operations using a parameter block. NFS
uses OSWORD for Econet transmit/receive operations and filing system calls.

## Hardware

**ADLC** (Advanced Data Link Controller)
: The MC6854 ADLC chip at &FEA0-&FEA3 that handles the Econet network
hardware protocol, providing HDLC-framed serial communication over the
Econet cable.

**Econet**
: Acorn's low-cost local area network for BBC Micro and other Acorn
computers. Uses a four-wire bus with clock, data, and ground lines, managed
by the ADLC chip.

**Tube**
: Acorn's second-processor interface. A memory-mapped I/O bus connecting the
BBC Micro host to an external processor (Z80, 6502, 80186, or ARM) via four
register pairs (R1-R4) at &FEE0-&FEE7.

**ULA** (Uncommitted Logic Array)
: A semi-custom chip. In the Tube interface, the Tube ULA manages the four
register pairs (R1-R4) and the handshaking protocol between the host and
second processor.

## Filing systems

**CFS** (Cassette Filing System)
: The BBC Micro's built-in filing system for cassette tape storage.

**DFS** (Disc Filing System)
: Filing system ROM for floppy disc storage, typically provided by Acorn or
third-party ROMs.

**DNFS** (Disc and Network Filing System)
: A combined ROM containing both DFS and NFS, allowing disc and network
access from a single ROM slot.

**NFS** (Network Filing System)
: The Econet filing system ROM that provides remote file access over the
Econet network. This project covers standalone NFS versions 3.34, 3.34B,
and 3.35D.

**RAM** (Random Access Memory)
: Main memory. NFS copies relocated code blocks from ROM into RAM pages
during initialisation for execution at runtime addresses.

**ROM** (Read-Only Memory)
: In Acorn context, typically refers to a sideways ROM — a 16 KB slot in the
BBC Micro's paged ROM bank (&8000-&BFFF). NFS occupies one 8 KB sideways
ROM slot.

## Networking

**CR** (Carriage Return)
: ASCII character &0D. Used as the line/command terminator in MOS command
parsing and Econet protocol messages.

**RX** (Receive)
: Refers to data reception over Econet — the receive buffer, receive control
block, or the act of receiving a network packet.

**TX** (Transmit)
: Refers to data transmission over Econet — the transmit buffer, transmit
control block, or the act of sending a network packet.

## Protocol concepts

**MOS** (Machine Operating System)
: The BBC Micro's ROM-based operating system. Provides the vector system,
API calls (OSBYTE, OSWORD, etc.), service call dispatch, sideways ROM
management, and the filing system framework that NFS plugs into.

**relocated code**
: Code stored in the ROM image that is copied to RAM at a different address
during initialisation. NFS relocates blocks to zero page (&0016-&0076),
page 4 (&0400-&04FF), page 5 (&0500-&05FF), and page 6 (&0600-&06FF).

**service call**
: A broadcast mechanism in the MOS where the OS calls each sideways ROM's
service entry point with a service number in the accumulator. ROMs inspect
the number and either handle the call (claiming it by zeroing A) or pass it
on. NFS handles service calls for filing system selection, command dispatch,
and Econet events.

**sideways ROM**
: One of up to 16 ROM slots in the BBC Micro, all mapped to the same address
range (&8000-&BFFF) and bank-switched by the MOS. Only one sideways ROM is
paged in at a time.
