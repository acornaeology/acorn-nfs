# Glossary

Acorn-specific terms used in this project's documentation and annotations.
See the [BBC Micro Advanced User Guide](http://stardot.org.uk/mirrors/www.bbcdocs.com/filebase/essentials/BBC%20Microcomputer%20Advanced%20User%20Guide.pdf)
for full descriptions of the MOS API and vector system.

## MOS vectors

**BRKV** (Break Vector)
: MOS vector at &0202. Called when a BRK instruction is executed.

  NFS installs its own BRK handler to process network errors, replacing
  the default MOS error handler while NFS is the active filing system.

**EVNTV** (Event Vector)
: MOS vector at &0220. Called when an enabled event occurs.

  NFS uses this for Econet event handling, responding to network
  receive-complete and transmit-complete events.

**FSCV** (Filing System Control Vector)
: MOS vector at &021E. Called for filing system control operations
including `*RUN`, `*/`, and unrecognised `*` commands.

  NFS intercepts this to forward commands to the fileserver. FSCV code 3
  passes raw command text; codes 2 and 4 (in 3.35D) parse the filename
  through GSINIT/GSREAD first.

**FILEV** (File Vector)
: MOS vector at &0212. Called for whole-file operations (OSFILE).

  NFS intercepts this to handle remote file loading and saving over
  Econet.

**ARGSV** (Arguments Vector)
: MOS vector at &0214. Called for open-file argument operations (OSARGS).

  NFS intercepts this to query and set attributes on remote file handles.

**BGETV** (Byte Get Vector)
: MOS vector at &0216. Called for single-byte file reads (OSBGET).

  NFS intercepts this to read bytes from remote files over Econet.

**BPUTV** (Byte Put Vector)
: MOS vector at &0218. Called for single-byte file writes (OSBPUT).

  NFS intercepts this to write bytes to remote files over Econet.

**FINDV** (Find Vector)
: MOS vector at &021C. Called for file open/close operations (OSFIND).

  NFS intercepts this to open and close remote file handles on the
  fileserver.

**GBPBV** (Get/Put Byte Vector)
: MOS vector at &021A. Called for multi-byte file transfers (OSGBPB).

  NFS intercepts this to perform block reads and writes on remote files.

**NETV** (Network Vector)
: MOS vector at &0224. Called for Econet network operations.

  Used by the Econet module for low-level network I/O including
  transmit, receive, and broadcast operations.

**RDCHV** (Read Character Vector)
: MOS vector at &0210. Called when OSRDCH reads a character from input.

  NFS intercepts this to support remote input during Tube operations,
  polling the Tube register for characters from the second processor.

**WRCHV** (Write Character Vector)
: MOS vector at &020E. Called when OSWRCH writes a character to output.

  NFS intercepts this to redirect character output to the second
  processor via the Tube during remote operations.

## MOS API calls

**GSINIT** (General String Input Initialise)
: MOS routine at &FFC2. Initialises the string input state for parsing a
command-line argument.

  Used with GSREAD to handle quoted filenames and `|`-escaped special
  characters. NFS 3.35D uses GSINIT/GSREAD for `*/` and `*RUN` filename
  parsing.

**GSREAD** (General String Read)
: MOS routine at &FFC5. Reads the next character from a command-line
argument previously set up by GSINIT.

  Handles `|`-escaped special characters and quoted strings. Each call
  returns one character until the argument is exhausted.

**OSBYTE** (OS Byte)
: MOS routine at &FFF4. Performs miscellaneous OS operations selected by
the accumulator value.

  NFS uses OSBYTE calls for keyboard control (&7C to clear escape),
  handle queries (&C6/&C7 for EXEC/SPOOL handles), and ROM management.

**OSCLI** (OS Command Line Interpreter)
: MOS routine at &FFF7. Executes a `*` command string.

  NFS uses internal OSCLI calls to dispatch the `*NET1`-`*NET4`
  sub-commands, which manage file handles for Econet remote operations.

**OSRDCH** (OS Read Character)
: MOS routine at &FFE0. Reads a single character from the current input
stream.

**OSWRCH** (OS Write Character)
: MOS routine at &FFEE. Writes a single character to the current output
stream.

**OSWORD** (OS Word)
: MOS routine at &FFF1. Performs OS operations using a parameter block.

  NFS uses OSWORD for Econet transmit (&10) and receive (&11)
  operations, passing control blocks that specify station numbers,
  buffer addresses, and byte counts.

## Hardware

**ADLC** (Advanced Data Link Controller)
: The MC6854 ADLC chip at &FEA0-&FEA3. Handles the Econet network
hardware protocol.

  Provides HDLC-framed serial communication over the Econet cable. NFS
  accesses the ADLC's status and control registers directly for
  low-level network operations.

**Econet**
: Acorn's low-cost local area network for BBC Micro and other Acorn
computers.

  Uses a four-wire bus with clock, data, and ground lines, managed by
  the ADLC chip. Each station has a unique station number (and optional
  network number for bridged networks).

**Tube**
: Acorn's second-processor interface, connecting the BBC Micro host to
an external processor via four register pairs (R1-R4) at &FEE0-&FEE7.

  Supported second processors include the 6502, Z80, 80186, and ARM.
  NFS contains relocated host code that manages Tube communication for
  remote filing operations, handling character I/O, data transfers, and
  escape signalling across the register pairs.

**ULA** (Uncommitted Logic Array)
: A semi-custom chip. In the Tube interface, the Tube ULA manages the
register pairs (R1-R4) and the handshaking protocol between host and
second processor.

  R1 handles events and escape signalling (and WRCH in 3.34/3.35D), R2
  handles command bytes, R3 handles multi-byte transfers, and R4 handles
  one-byte transfers. NFS 3.34B temporarily moved WRCH from R1 to R4;
  3.35D reverted this.

## Filing systems

**CFS** (Cassette Filing System)
: The BBC Micro's built-in filing system for cassette tape storage.

**DFS** (Disc Filing System)
: Filing system ROM for floppy disc storage, typically provided by Acorn
or third-party ROMs.

**DNFS** (Disc and Network Filing System)
: A combined ROM containing both DFS and NFS, allowing disc and network
access from a single ROM slot.

**NFS** (Network Filing System)
: The Econet filing system ROM that provides remote file access over the
Econet network.

  This project covers standalone NFS versions 3.34, 3.34B, and 3.35D.
  The related DNFS 3.00/3.60 versions combine NFS with DFS in a single
  ROM.

**RAM** (Random Access Memory)
: Main memory. NFS copies relocated code blocks from ROM into RAM pages
during initialisation for execution at runtime addresses.

**ROM** (Read-Only Memory)
: In Acorn context, typically refers to a sideways ROM — a 16 KB slot in
the BBC Micro's paged ROM bank (&8000-&BFFF).

  NFS occupies one 8 KB sideways ROM slot. Up to 16 sideways ROMs can
  be installed, bank-switched by the MOS.

## Networking

**CR** (Carriage Return)
: ASCII character &0D. Used as the line/command terminator in MOS command
parsing and Econet protocol messages.

**RX** (Receive)
: Refers to data reception over Econet — the receive buffer, receive
control block, or the act of receiving a network packet.

**TX** (Transmit)
: Refers to data transmission over Econet — the transmit buffer, transmit
control block, or the act of sending a network packet.

## Protocol concepts

**MOS** (Machine Operating System)
: The BBC Micro's ROM-based operating system.

  Provides the vector system, API calls (OSBYTE, OSWORD, etc.), service
  call dispatch, sideways ROM management, and the filing system framework
  that NFS plugs into.

**relocated code**
: Code stored in the ROM image that is copied to RAM at a different
address during initialisation.

  NFS relocates blocks to zero page (&0016-&0076), page 4
  (&0400-&04FF), page 5 (&0500-&05FF), and page 6 (&0600-&06FF). The
  BRK handler, Tube host code, and Econet interrupt handlers all run
  from these relocated blocks.

**service call**
: A broadcast mechanism in the MOS where the OS calls each sideways
ROM's service entry point with a service number in the accumulator.

  ROMs inspect the number and either handle the call (claiming it by
  zeroing A) or pass it on. NFS handles service calls for filing system
  selection, command dispatch, and Econet events.

**sideways ROM**
: One of up to 16 ROM slots in the BBC Micro, all mapped to the same
address range (&8000-&BFFF) and bank-switched by the MOS. Only one
sideways ROM is paged in at a time.
