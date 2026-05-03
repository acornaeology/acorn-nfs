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

**OSARGS** (OS Arguments)
: MOS routine at &FFDA. Reads or writes attributes of an open file handle,
selected by the accumulator value, with the file handle in Y and a parameter
block address in X.

  NFS intercepts OSARGS via the ARGSV vector to handle remote file handle
  queries over Econet. A=0 with Y=0 returns the filing system number (5 for
  NFS).

**OSCLI** (OS Command Line Interpreter)
: MOS routine at &FFF7. Executes a `*` command string.

  NFS uses internal OSCLI calls to dispatch the `*NET1`-`*NET4`
  sub-commands, which manage file handles for Econet remote operations.

**OSFILE** (OS File)
: MOS routine at &FFDD. Performs whole-file operations (load, save,
read/write attributes) using a parameter block pointed to by X and Y.

  NFS intercepts OSFILE via the FILEV vector to load and save files over
  Econet. The parameter block format differs between host and fileserver:
  NFS translates between the MOS 4-byte attribute format and the fileserver's
  2-byte format using a lookup table.

**OSFIND** (OS Find)
: MOS routine at &FFCE. Opens or closes a file, returning a file handle in A.
A=0 closes the handle in Y; non-zero A values open the file named at X,Y.

  NFS intercepts OSFIND via the FINDV vector to manage remote file handles
  on the fileserver. 3.35K adds initialisation of the sequence number
  tracking byte when opening a file, fixing a potential protocol error.

**OSGBPB** (OS Get Bytes/Put Bytes)
: MOS routine at &FFD1. Performs multi-byte file read or write operations
using a 13-byte parameter block.

  NFS intercepts OSGBPB via the GBPBV vector. The Tube host code for OSGBPB
  had a bug in 3.35D where the carry result was not sent to the co-processor,
  fixed in 3.35K.

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

**65C02**
: The CMOS variant of the 6502 fitted to the Master 128. Adds a
dozen new instructions over the original NMOS 6502 and fixes
several long-standing edge cases.

  Acorn used the Rockwell R65C02 (later units: GTE65SC02), a
  superset of the standard 65C02 that adds bit-test instructions
  (BBR / BBS / RMB / SMB). ANFS 4.21 doesn't use the bit-test
  extensions but takes routine advantage of the core 65C02
  additions: PHX / PHY / PLX / PLY (push/pull X / Y), BRA
  (unconditional branch), STZ (store zero, no register needed),
  TSB / TRB (test-and-set / test-and-reset bits in memory), and
  BIT abs,X. All save bytes, cycles, or both over the equivalent
  6502 sequences. Because the host-OS gate at the start of the
  service handler refuses to install on a Model B / B+, the
  assembler can rely on the 65C02 throughout.

**ACCCON** (Access Control register)
: The Master 128 access-control register at &FE34. Each bit gates a
specific shadow- or hidden-RAM paging mode.

  Bits of interest to ANFS:
  D toggles whether the CRT controller displays the LYNNE shadow-RAM
  region or main memory; E enables LYNNE for opcode-driven access in
  the &3000-&7FFF range; X forces region (a) accesses to redirect into
  LYNNE regardless of opcode address; Y pages the HAZEL hidden RAM
  over the MOS VDU drivers at &C000-&DFFF (this is what ANFS uses to
  reach its filing-system workspace); ITU selects the internal vs
  external Tube; IRR drives an open-drain pull on /IRQ. Code that
  sets bit Y is responsible for clearing it -- there is no hardware
  fallback, so missing the clear leaves MOS VDU calls broken.

**ADLC** (Advanced Data Link Controller)
: The MC6854 ADLC chip at &FEA0-&FEA3. Handles the Econet network
hardware protocol.

  Provides HDLC-framed serial communication over the Econet cable. NFS
  accesses the ADLC's status and control registers directly for
  low-level network operations.

**CR1** (Control Register 1)
: ADLC control register at &FEA0 (active when AC=0). Configures receiver
and transmitter operating modes.

  Key bits: b0=RIE (RX interrupt enable), b1=TIE (TX interrupt enable),
  b2=RX_DISCONTINUE (abort receive), b3=RX_RESET, b4=TX_RESET,
  b6=RIE complement, b7=AC (address control — selects CR1 vs CR3).

**CR2** (Control Register 2)
: ADLC control register at &FEA1 (active when AC=0). Controls frame
transmission and prioritised status bits.

  Key bits: b0=PSE (prioritised status enable), b1=2/1 byte mode,
  b2=flag/mark idle, b3=FC_TDRA (TDRA select: FIFO available vs any
  byte), b4=CLR_TX_ST (clear TX status), b5=RTS (request to send),
  b6-b7=not used. Typical values: &1E (RX idle), &82 (flag idle wait),
  &A7 (TX handshake with RTS+PSE).

**CMOS** (CMOS RAM)
: 50 bytes of battery-backed RAM in the Master 128, accessed
through OSBYTE &A1 (read) and OSBYTE &A2 (write).

  Holds settings that need to survive BREAK and power-cycle:
  keyboard layout, default filing system, configured Econet
  station number, screen mode, and so on. ANFS 4.21 stores its
  protection state in CMOS byte &11 bit 6 – a single bit that
  cmd_prot / cmd_unprot toggle. Persistence is automatic: the
  state is in CMOS, not in volatile RAM, so it survives across
  resets and power-off. ANFS 4.18 had no equivalent; its
  protection mask was kept in workspace and lost on BREAK.

**CTS** (Clear To Send)
: ADLC status register 1 bit 4. Indicates that the Econet clock
hardware is present and the network is physically connected.

  NFS tests CTS in SR1 during the INACTIVE polling loop after
  detecting a quiet line. If CTS is not set, the station has no
  clock signal and cannot transmit. The "No Clock" error is generated
  when CTS is absent.

**Econet**
: Acorn's low-cost local area network for BBC Micro and other Acorn
computers.

  Uses a four-wire bus with clock, data, and ground lines, managed by
  the ADLC chip. Each station has a unique station number (and optional
  network number for bridged networks).

**FIFO** (First In, First Out)
: A hardware buffer in the MC6854 ADLC that queues bytes for transmission or
reception. The ADLC has separate TX and RX FIFOs (3 bytes each).

  NFS interrupt handlers feed outbound bytes into the TX FIFO and drain
  inbound bytes from the RX FIFO during Econet frame transmission and
  reception. FIFO status bits in the ADLC status registers drive the NMI
  handler's decision to read or write data.

**FV** (Frame Valid)
: ADLC status register 2 bit 1. Set when a complete, error-free frame
has been received (valid CRC, no overrun, no abort).

  NFS NMI handlers test FV to confirm a received scout or data frame is
  complete before processing its contents. FV interacts with PSE: when
  PSE is enabled, FV masks RDA in the prioritised status.

**HAZEL**
: An 8 KB Master 128 hidden-RAM region at &C000-&DFFF that ACCCON's
Y bit pages over the MOS VDU drivers.

  Designated by Acorn as filing-system workspace; the documented
  upper limit for static workspace claims is page &DB. ANFS 4.21
  variant 1 occupies the first 768 bytes (&C000-&C2FF) for its parse
  buffer, TX buffer, FS lib flags, FCB attributes, and saved-catalogue
  buffer (the same data that 4.18 kept in MOS RAM pages &0Dxx-&10xx).
  Code that pages HAZEL in via ACCCON.Y must page it back out before
  any MOS VDU call.

**INACTIVE**
: ADLC status register 2 bit 2. Set when the Econet line is idle —
no carrier is detected and no frame transmission or reception is in
progress.

  NFS polls INACTIVE before attempting to transmit, spinning in a
  tight loop with a three-byte timeout counter. If INACTIVE is never
  detected, the "Line Jammed" error is generated. The line must be
  idle before a station can assert RTS and begin sending a scout frame.

**INTOFF**
: Disable Econet NMIs by reading the station ID register at &FE18. The
read has the side effect of clearing the NMI enable latch in the Econet
hardware, preventing further NMIs until INTON is performed.

  NFS 3.65 uses INTOFF in combination with a self-modifying NMI shim.
  ANFS replaces the self-modifying approach with double INTOFF (two
  consecutive reads of &FE18) for robustness.

**INTON**
: Re-enable Econet NMIs by reading the video ULA control register at
&FE20. The read has the side effect of setting the NMI enable latch,
allowing the ADLC to trigger NMIs again.

  Always paired with a preceding INTOFF. The NMI-disabled window
  between INTOFF and INTON protects critical ADLC register accesses
  from being interrupted by incoming network traffic.

**IRQ** (Interrupt Request)
: A maskable hardware interrupt on the 6502 processor, triggered by
peripheral devices pulling the IRQ line low.

  In the BBC Micro, IRQs handle keyboard, timer, and VIA events. NFS's
  Econet interrupt handling uses NMIs rather than IRQs for time-critical
  network operations, since NMIs cannot be masked.

**LYNNE**
: A 20 KB shadow-RAM region in the Master 128, addressable in the
&3000-&7FFF window when ACCCON's E bit (or X bit) is set.

  Holds the screen bit-map. With ACCCON.D set the CRT controller
  displays LYNNE; with E set, opcode-driven loads/stores in
  &3000-&7FFF transparently access LYNNE; with X set, all accesses
  to that region redirect into LYNNE regardless of the opcode
  source. ANFS doesn't store its own data in LYNNE but does
  cooperate with the shadow-RAM rules: NMI data-copy paths
  bracket their work with ACCCON save/restore so the in-flight
  byte transfer reaches the correct memory.

**Master 128**
: Acorn's 1986 successor to the BBC Model B. Same desktop
form-factor, but adds a Rockwell R65C02 CPU, 128 KB of RAM
(32 K main + 20 K LYNNE shadow + 8 K HAZEL hidden + 64 K paged
ROM banks), and 50 bytes of CMOS-backed configuration store.

  ANFS 4.21 (variant 1) is the first ANFS for the Master family.
  Its host-OS gate accepts MOS 3.x (Master 128) and MOS 4.0
  (Master Econet Terminal); it explicitly rejects MOS 5.0
  (Master Compact). The Master's expanded memory map – HAZEL
  for filing-system workspace, LYNNE for shadow display, CMOS
  for persistent settings – drives major structural changes
  through ANFS that have nothing to do with the network protocol
  itself.

**PSE** (Prioritised Status Enable)
: ADLC control register 2 bit 0. When set, enables prioritised status
reporting in status register 2: FV, RX abort, and error conditions
take priority over RDA.

  NFS enables PSE during receive to detect frame-complete and error
  conditions via SR2. The interaction between PSE, FV, and RDA is
  central to the NMI handler's frame reception logic.

**NMI** (Non-Maskable Interrupt)
: A hardware interrupt on the 6502 that cannot be disabled. Triggered by
the ADLC when Econet network activity requires immediate attention.

  NFS installs an NMI handler (via the NMI workspace at &0D00) that manages
  the ADLC during frame transmission and reception. The handler reads ADLC
  status registers to determine the interrupt cause and processes TX/RX data
  accordingly. The NMI shim at &0D00 dispatches to version-specific handlers
  in pages 4-6.

**RDA** (Receive Data Available)
: ADLC status register 2 bit 7. Set when data is available to read
from the RX FIFO.

  NFS NMI handlers test RDA (via BIT SR2, checking the sign flag) to
  determine whether to read the next received byte from the ADLC data
  register. When PSE is enabled, FV can mask RDA.

**RAM** (Random Access Memory)
: Main memory. NFS copies relocated code blocks from ROM into RAM pages
during initialisation for execution at runtime addresses.

**ROM** (Read-Only Memory)
: In Acorn context, typically refers to a sideways ROM — a 16 KB slot in
the BBC Micro's paged ROM bank (&8000-&BFFF).

  NFS occupies one 8 KB sideways ROM slot. Up to 16 sideways ROMs can
  be installed, bank-switched by the MOS.

**RTS** (Request To Send)
: ADLC control register 2 bit 5. When set, asserts the RTS line to
signal readiness to transmit on the Econet bus.

  NFS sets RTS in CR2 when beginning a transmission (scout or data
  frame). The typical TX setup value &A7 includes RTS along with
  CLR_TX_ST, FC_TDRA, and PSE.

**shadow RAM**
: A bank of RAM that mirrors part of the main address space and is
paged into the same address window under software control.

  The Master 128 has two shadow regions: LYNNE (20 KB at
  &3000-&7FFF, used for the display bitmap when shadow-screen
  modes are selected) and HAZEL (8 KB at &C000-&DFFF, used by
  filing systems as workspace). Both are paged via bits of the
  ACCCON register; routines that page shadow RAM in are
  responsible for paging it back out before any code that
  expects to see main RAM at the same address.

**sideways ROM**
: One of up to 16 ROM slots in the BBC Micro, all mapped to the same
address range (&8000-&BFFF) and bank-switched by the MOS. Only one
sideways ROM is paged in at a time.

**SR1** (Status Register 1)
: ADLC status register at &FEA0 (read when AC=0). Reports transmitter
and receiver status.

  Key bits: b0=RDA (via 2/1 byte mode), b1=S2RQ (SR2 request),
  b2=loop/FD, b3=DCD, b4=CTS, b5=TXU (underrun), b6=TDRA,
  b7=IRQ. NFS reads SR1 to check CTS (clock present) and TDRA
  (TX FIFO ready), and to acknowledge pending interrupts.

**SR2** (Status Register 2)
: ADLC status register at &FEA1 (read when AC=0). Reports frame-level
receive status and error conditions.

  Key bits: b0=AP (address present), b1=FV (frame valid),
  b2=INACTIVE (idle line), b3=abort, b4=FCS error, b5=DCD,
  b6=RX overrun, b7=RDA. When PSE is enabled, FV and error bits
  take priority over RDA. NFS NMI handlers use BIT SR2 to test
  AP, INACTIVE, FV, and RDA during frame reception.

**TDRA** (Transmit Data Register Available)
: ADLC status register 1 bit 6. Set when the TX FIFO has space for
at least one more byte.

  NFS NMI handlers test TDRA (via BIT SR1, checking the overflow flag)
  before writing each byte to the ADLC data register. If TDRA is not
  set, the handler branches to an error or retry path.

**TIE** (Transmit Interrupt Enable)
: ADLC control register 1 bit 1. When set, enables NMI generation when
TDRA becomes set (TX FIFO ready for data).

  NFS enables TIE in CR1 when switching from receive to transmit mode,
  so the NMI handler is called each time the ADLC is ready to accept
  the next TX byte. Typical CR1 value &44 sets TIE with RX_RESET.

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

**VIA** (Versatile Interface Adapter)
: A 6522 chip providing parallel I/O ports, two timers, and a shift
register. The BBC Micro and Master 128 both have two: the System
VIA at &FE40-&FE4F and the User VIA at &FE60-&FE6F.

  ANFS interacts mostly with the System VIA, whose shift register
  (SR) and auxiliary control register (ACR) are involved in
  Econet TX setup. On the Model B, ANFS 4.18 wrote the System
  VIA directly. On the Master 128, MOS owns the System VIA – it
  uses the shift register for sound and keyboard polling – so
  ANFS 4.21 maintains a shadow ACR/SR pair in workspace
  (&0D68 / &0D69) that the Master's IRQ dispatch path reconciles
  with the live VIA.

## Filing systems

**CFS** (Cassette Filing System)
: The BBC Micro's built-in filing system for cassette tape storage.

**CSD** (Current Selected Directory)
: The currently active directory on the fileserver for file operations.
Stored at &0F03 in the NFS workspace.

  The CSD handle determines which directory is used for relative filename
  lookups. In 3.35D, `*EX` conditionally skips filenames based on the CSD
  handle state; this check was removed in 3.35K.

**DFS** (Disc Filing System)
: Filing system ROM for floppy disc storage, typically provided by Acorn
or third-party ROMs.

**DNFS** (Disc and Network Filing System)
: A combined ROM containing both DFS and NFS, allowing disc and network
access from a single ROM slot.

**EOF** (End Of File)
: Indicates that all data in a file has been read. NFS maintains per-handle
EOF hint flags at &0E07 to avoid unnecessary network round-trips when
checking file position.

  The EOF hint cache was broken in 3.35D: a bug in the BGETV handler always
  set the hint flag regardless of file position, forcing a network round-trip
  on every EOF check. Fixed in 3.35K.

**NFS** (Network Filing System)
: The Econet filing system ROM that provides remote file access over the
Econet network.

  This project covers standalone NFS versions 3.34, 3.34B, 3.35D, and 3.35K.
  The related DNFS 3.00/3.60 versions combine NFS with DFS in a single
  ROM.

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

**four-way handshake**
: The Econet reliable delivery protocol for data transfers between
stations. Consists of four sequential frames: scout, scout ACK, data,
and final ACK.

  The transmitting station sends a scout frame containing the
  destination address and control byte. If the destination is
  listening, it replies with a scout ACK. The transmitter then sends
  the data frame, and the receiver confirms with a final ACK. Any
  failure at any stage causes a retry or error. NFS implements the
  full four-way handshake in its NMI handler chain.

**scout**
: The initial short frame in an Econet four-way handshake. Contains the
destination station address, source station address, and a control byte
identifying the operation type (port number and function code).

  The scout tests whether the remote station is listening before
  committing to a potentially large data transfer. The NMI handler
  `nmi_rx_scout` processes incoming scouts by checking the destination
  address against the local station ID. If the scout is for us (or a
  broadcast), the handler sets up to receive the data frame.

**RXCB** (Receive Control Block)
: The 12-byte parameter block for OSWORD &11 (Econet receive). Specifies
the port number, station filter, buffer address, and buffer size for an
incoming data transfer.

  NFS maintains an RXCB in its workspace for each active receive
  operation. The buffer address bytes at offsets 4-7 determine whether
  the transfer targets main memory or Tube address space.

**TXCB** (Transmit Control Block)
: The 12-byte parameter block for OSWORD &10 (Econet transmit). Specifies
the destination port, station address, control byte, buffer address, and
byte count for an outgoing data transfer.

  The low 3 bits of the TXCB status byte encode the error class when
  a transmission fails (0=Line Jammed, 2=Not listening, 3=No Clock,
  etc.). NFS masks these bits to select the appropriate error message.

## Miscellaneous

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
