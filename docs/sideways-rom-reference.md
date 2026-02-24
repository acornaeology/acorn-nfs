# BBC Micro Sideways ROM Reference

A summary of the MOS (Machine Operating System) interfaces relevant to
sideways ROMs and filing systems on the BBC Micro. This covers the ROM header
format, language entry, service calls, filing system integration, and FSCV
dispatch — the core APIs that NFS implements.

Based on Sprow's
[Sideways ROM authoring notes](http://www.sprow.co.uk/bbc/library/sidewrom.pdf),
with additional detail from the *Advanced User Guide* and *New Advanced User
Guide*.

---

## ROM Header

Every sideways ROM occupies the address space &8000–&BFFF (16KB) and must
begin with a fixed header structure for the MOS to recognise it.

| Address | Contents |
|---------|----------|
| &8000   | JMP language\_entry (set to 0 if not a language) |
| &8003   | JMP service\_entry (present in all ROMs except 6502 BASIC) |
| &8006   | ROM type byte |
| &8007   | Copyright offset — low byte of the address of the zero byte preceding the copyright string |
| &8008   | Binary version number (informational, not used by MOS) |
| &8009+  | Title string, zero-terminated. Printed by MOS when a language starts. |
| (after title) | Version string, zero-terminated. Optional, e.g. `1.23` or `1.23 (01 Jan 1999)`. If present and the ROM is a language, &FD/&FE points here on entry. |
| (copyright) | Zero byte followed by copyright string, zero-terminated. Must take the form `(C)` followed by date/author. The MOS checks for this to validate the ROM. |
| (after copyright) | Tube relocation address (4 bytes, low byte first). Only required if bit 5 of the ROM type byte is set. |

The copyright string is mandatory — the MOS uses it as one of its checks to
determine whether a valid ROM is present in a given socket.

### ROM Type Byte (&8006)

| Bit | Meaning |
|-----|---------|
| 7   | Service entry present |
| 6   | Language entry present |
| 5   | Tube relocation address present |
| 4   | Electron firmkey support (KEY+FUNC / KEY+CAPS LK) |
| 3–0 | Processor type code |

Processor type codes (bits 3–0):

| Code | Processor |
|------|-----------|
| 0000 | 6502 — the 6502 BASIC ROM specifically |
| 0010 | 6502 — other 6502 code (not BASIC) |
| 0011 | 68000 |
| 1000 | Z80 |
| 1001 | 32016 |
| 1011 | 80186 |
| 1100 | 80286 |
| 1101 | ARM |

A typical NFS ROM has type byte &82 — service entry present (bit 7), 6502
code but not BASIC (bits 3–0 = 0010), no language entry.

---

## Language Entry

A "language" in BBC Micro terminology is any ROM with a language entry point —
not necessarily a programming language (e.g. View is a language ROM). The MOS
enters a language via the JMP at &8000 with a reason code in A.

### Entry Conditions

- Interrupts are disabled — the language must re-enable them (`CLI`).
- The stack pointer is undefined — the language must reset it (`LDX #&FF :
  TXS`).
- The MOS prints the ROM's title string (&8009) before entry.
- &FD/&FE (the error pointer) is set to the version string, or the copyright
  string if no version string is present. This is why `REPORT` in 6502 BASIC
  prints the copyright message when no error has occurred.
- The language should set BRKV to its own error handler.
- Available workspace: zero page &00–&8F, page 4 (&400–&7FF), and OSHWM to
  screen memory.

### Reason Codes (A Register)

| A | Meaning |
|---|---------|
| 0 | No language available — MOS is calling the Tube ROM instead |
| 1 | Normal startup |
| 2 | Request next byte of softkey expansion; Y = byte (Electron MOS only) |
| 3 | Request length of softkey expansion; Y = key number on entry, set Y to length on exit (Electron MOS only) |

A language starts in one of three ways:

1. A star command recognised by the ROM issues `*FX142,<socket>` to select
   itself (enters via service call 4, then language entry).
2. The user types `*FX142,<socket>` directly.
3. The ROM is the configured default language at reset (or the highest-numbered
   socket on machines without NVRAM).

---

## Service Calls

When the MOS needs to notify sideways ROMs of an event, it issues a service
call. ROMs are polled in descending socket order (&F down to &0), giving
higher-numbered sockets priority.

### Entry Conditions

- A = service call number
- X = current ROM socket number
- Y = additional parameter (call-specific)

To **claim** a call: set A to 0 and return (`LDA #0 : RTS`). No further ROMs
will be polled. To **pass on**: return with A, X, and Y preserved.

### Service Call Table

| Call | Hex  | Name | MOS |
|------|------|------|-----|
| 0    | &00  | Already claimed | All |
| 1    | &01  | Claim absolute workspace | All |
| 2    | &02  | Claim private workspace | All |
| 3    | &03  | Auto-boot | All |
| 4    | &04  | Unrecognised star command | All |
| 5    | &05  | Unrecognised interrupt | All |
| 6    | &06  | BRK occurred | All |
| 7    | &07  | Unrecognised OSBYTE | All |
| 8    | &08  | Unrecognised OSWORD | All |
| 9    | &09  | *HELP issued | All |
| 10   | &0A  | Claim static workspace | All |
| 11   | &0B  | NMI release — return NMI workspace to previous owner | All |
| 12   | &0C  | NMI claim — request to take NMI workspace | All |
| 13   | &0D  | ROM filing system initialise | All |
| 14   | &0E  | ROM filing system get byte | All |
| 15   | &0F  | Vectors changed | All |
| 16   | &10  | SPOOL/EXEC closing | All |
| 17   | &11  | Character set explode/implode | All |
| 18   | &12  | Select filing system (Y = FS number) | All |
| 19   | &13  | Character entered RS423 buffer | Electron |
| 20   | &14  | Character entered printer buffer | Electron |
| 21   | &15  | Software polling interrupt | Electron/Master |
| 22   | &16  | BEL request | Electron |
| 23   | &17  | Sound buffer purged | Electron |
| 24   | &18  | Interactive *HELP | Master |
| 33   | &21  | Claim static workspace in hidden RAM | Master |
| 34   | &22  | Claim private workspace in hidden RAM | Master |
| 35   | &23  | Top of static workspace | Master |
| 36   | &24  | Private workspace size in hidden RAM | Master |
| 37   | &25  | Filing system details | Master |
| 38   | &26  | Close all files (*SHUT) | Master |
| 39   | &27  | Reset (Ctrl-Break / power-on / BREAK) | Master |
| 40   | &28  | Unrecognised *CONFIGURE | Master |
| 41   | &29  | Unrecognised *STATUS | Master |
| 42   | &2A  | Language starting up | Master |
| 43   | &2B  | Read memory size | B+ only |
| 254  | &FE  | Pre-Tube initialisation | All |
| 255  | &FF  | Post-Tube initialisation | All |

### Workspace Calls (1, 2, 10)

Three service calls manage workspace allocation at boot:

- **Call 1 — Absolute workspace** (shared, at a fixed address): Y holds the
  current top of absolute workspace on entry. If the ROM needs more, it sets Y
  to the higher value and returns without claiming. All ROMs see this call; the
  MOS uses the final Y value. Filing systems typically claim pages here for NMI
  code, FS state, and command buffers.

- **Call 2 — Private workspace** (per-ROM, at a variable address): Y holds
  the page number assigned to this ROM's private workspace. The ROM should save
  this value for later use. The amount of private workspace is determined by an
  earlier call 1 (the ROM adds to Y to reserve pages above the absolute
  workspace). The MOS calls this after absolute workspace is finalised.

- **Call 10 — Static workspace** (shared, persistent): Similar to absolute
  workspace but survives soft resets. Rarely used by filing systems.

### Star Command (4)

When the MOS cannot match a star command, it issues call 4. On entry, Y
points to the command text (offset from &xx00). The ROM should compare the text
against its own command table and, if matched, execute the command and claim
the call.

### NMI Management (11, 12)

The NMI (Non-Maskable Interrupt) workspace at &D00–&D5F is a shared resource.
Only one ROM can own it at a time. Two protocols exist:

1. **Temporary claim**: Issue OSBYTE &8F with X=12, Y=&FF to claim. Save the
   returned Y. When done, release with OSBYTE &8F, X=11, Y=(saved value).

2. **Persistent claim via service calls**: Claim at filing system init. When
   service call 12 arrives (another ROM wants NMIs), save your NMI state and
   return your filing system ID in Y. When call 11 arrives with your ID in Y,
   reclaim by restoring your NMI state.

Filing systems like NFS use protocol 2, since they need NMIs for network
transfers that can occur at any time.

### Filing System Selection (18)

Issued when the MOS processes `*FX143,<fs>` or a filing system star command
(e.g. `*NET`). Y contains the filing system number. If a ROM owns that filing
system, it should initialise itself and claim the call.

Standard filing system numbers:

| Number | Filing System |
|--------|---------------|
| 0      | None |
| 1      | 1770 DFS |
| 2      | ADFS (Network + ADFS on Master) |
| 3      | RFS (ROM Filing System) |
| 4      | DFS (8271) |
| 5      | NFS (Econet) |
| 6      | TELETEXT |
| 7      | IEEE |
| 8      | ADFS |

### Tube Initialisation (&FE, &FF)

These calls bracket Tube (second processor) setup:

- **&FE — Pre-Tube init**: Issued before the Tube is initialised. ROMs can
  perform host-side setup here. NFS/DNFS uses this to explode character
  definitions.

- **&FF — Post-Tube init**: Issued after the Tube is active. This is where
  NFS installs its vectors and copies relocated code (Tube host code to pages
  &04–&06, workspace initialisation to zero page &16–&76).

---

## Filing System Integration

A filing system ROM integrates with the MOS by installing handlers for the
filing system vectors and managing shared resources (NMI workspace, zero page).

### Filing System Vectors

When selected, a filing system installs handlers into the extended vector table
(at VTABLE + 3 * vector number). Each entry is a 3-byte JMP target: 2-byte
address plus 1-byte ROM socket number. The MOS dispatches calls to the correct
ROM automatically.

| Vector | Name  | Purpose |
|--------|-------|---------|
| FILEV  | File  | Whole-file operations: load, save, read/write catalogue info |
| ARGSV  | Args  | Read/write open file attributes (PTR, EXT, etc.) |
| BGETV  | BGet  | Read single byte from open file |
| BPUTV  | BPut  | Write single byte to open file |
| GBPBV  | GBPB  | Block read/write to open file or directory |
| FINDV  | Find  | Open or close a file (OSFIND) |
| FSCV   | FSC   | Miscellaneous operations: *OPT, EOF, *RUN, *CAT, etc. |

### Zero Page Usage

The MOS reserves zero page regions for the active filing system:

| Range     | Purpose |
|-----------|---------|
| &A0–&A7   | NMI workspace (while NMIs are claimed) |
| &A8–&AF   | Command workspace (during star command processing) |
| &B0–&BF   | Temporary workspace (available if you own absolute workspace) |
| &C0–&CF   | Private workspace (preserved while the filing system is selected) |

### NMI Code Space

The absolute workspace page at &0D00–&0D5F is reserved for NMI handler code.
A filing system that uses NMIs (like NFS for Econet transfers) installs its
handler code here when it claims NMI ownership.

---

## FSCV Function Codes

The MOS calls the FSCV handler with a function code in A. These are the
standard codes:

| A | Function | Description |
|---|----------|-------------|
| 0 | *OPT    | Process `*OPT X,Y` — X in X register, Y in Y register |
| 1 | EOF     | Check for end-of-file — file handle in X, return X=0 (not EOF) or X=&FF (EOF) |
| 2 | */      | Run command — address of filename in X/Y (lo/hi) |
| 3 | Unrecognised command | Forward to filing system — address of command text in X/Y (lo/hi) |
| 4 | *RUN    | Run named file — address of filename in X/Y (lo/hi) |
| 5 | *CAT    | Catalogue current directory — address of parameter in X/Y (lo/hi) |
| 6 | Shutdown | Filing system is being deselected — save state, close SPOOL/EXEC |
| 7 | Read handle range | Return base handle in X, top handle in Y |

Codes 2, 3, and 4 are closely related — a filing system typically routes all
three to the same command parser. Code 6 (sometimes called FSDIE) is issued
when another filing system is about to be selected, giving the current one a
chance to save its state.
