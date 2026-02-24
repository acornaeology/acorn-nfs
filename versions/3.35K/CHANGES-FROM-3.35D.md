# Changes from NFS 3.35D to NFS 3.35K

NFS 3.35K is a bug-fix release of Acorn NFS 3.35D for the BBC Micro. The two
8 KB ROMs are 97.8% identical at the opcode level, with 44 structural change
blocks. The changes fix several significant bugs — most notably in the BGETV
EOF hint logic, Tube OSGBPB result handling, and FINDV sequence number
initialisation — while removing the per-ROM disable feature introduced in
3.35D and reverting workspace variables to their 3.34B locations.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 2784 (34.0%) |
| Byte-level similarity           | 94.5%        |
| Opcode-level similarity         | 97.8%        |
| Full instruction similarity     | 89.6%        |
| Instructions (3.35D / 3.35K)    | 4019 / 4024  |
| Structural change blocks        | 44           |

The identical-byte count (34.0%) is low relative to the opcode similarity
(97.8%) because address operands shift throughout the ROM as a cumulative
effect of code insertions and deletions. The full instruction similarity
(89.6%) captures these operand changes.

## ROM header

| Field             | 3.35D     | 3.35K     |
|-------------------|-----------|-----------|
| Title             | "NET"     | "NET"     |
| ROM type          | &82       | &82       |
| Binary version    | &03       | &03       |
| Copyright         | "(C)ROFF" | "(C)ROFF" |
| Language entry    | &80D4     | &80D4     |
| Service entry     | &80EA     | &80EA     |

All header fields are unchanged. The language and service entry points remain
at the same ROM offsets despite the code changes — the net effect of
insertions and deletions leaves the entry points at &80D4 and &80EA.

## Changes

### 1. Version string: "3.35d" to "3.35K"

The ROM identification string printed by `*HELP` (at &81FA in 3.35D, &81F0 in
3.35K) changed from `"NFS 3.35d"` to `"NFS 3.35K"`. The revision letter
reverts from lowercase to the conventional uppercase used in earlier versions.

### 2. Per-ROM disable flag removed

The service handler guard introduced in 3.35D (6 bytes at &80EA-&80F3) is
removed entirely:

| Runtime addr | 3.35D instruction      | Purpose                           |
|--------------|------------------------|-----------------------------------|
| &80EA        | PHA                    | Save service number               |
| &80EB        | LDA &0DF0,X           | Read per-ROM disable flag         |
| &80EE        | ASL A                  | Shift bit 7 into carry            |
| &80EF        | PLA                    | Restore service number            |
| &80F0        | BMI &80F4              | If &FE/&FF, skip disable check    |
| &80F2        | BCS return_1           | If carry set, ROM is disabled     |

In 3.35D, if bit 7 of `&0DF0+X` (where X is the ROM bank number) was set, NFS
ignored all service calls except &FE (Tube init) and &FF (full reset). This
provided a software mechanism to disable NFS without removing the ROM.

In 3.35K, the service handler dispatches all service calls unconditionally.
The workspace at &0DF0+X is freed.

### 3. Workspace variables reverted: &A8/&A9 back to &CD/&CE

3.35D relocated two zero page workspace variables from their 3.34B locations:

| Variable       | 3.34B | 3.35D | 3.35K |
|----------------|-------|-------|-------|
| `nfs_temp`     | &CD   | &A8   | &CD   |
| `rom_svc_num`  | &CE   | &A9   | &CE   |

3.35K reverts both to their original &CD/&CE addresses. In 3.35K the labels
are `fs_temp_cd` and `fs_temp_ce`. Addresses &A8/&A9 are in the MOS
general-purpose scratch area, shared with other ROMs; &CD/&CE are in the
filing system workspace area reserved for the active filing system. The
reversion may resolve a conflict where &A8/&A9 were being overwritten by
other ROMs or the MOS.

### 4. BGETV EOF hint logic fixed

The most significant bug fix. In the BGETV handler, the EOF hint flag is
maintained per open file handle to avoid unnecessary network round-trips when
checking for end-of-file.

**3.35D** (at &8545-&8551):
```
    CLC
    PHP              ; save processor status
    LDA &CF          ; load handle mask
    PLP              ; restore N flag from BIT
    BMI &854F        ; if N set (at EOF), skip clear
    JSR clear_fs_flag ; clear EOF hint
.c854f
    JSR set_fs_flag  ; set EOF hint (ALWAYS)
```

**3.35K** (at &853A-&8548):
```
    CLC
    BMI &8544        ; if N set (at EOF), skip to set-only
    LDA &CF          ; load handle mask
    JSR clear_fs_flag ; clear EOF hint
    BCC &8549        ; branch always (CLC above)
.c8544
    LDA &CF          ; load handle mask
    JSR set_fs_flag  ; set EOF hint
.c8549
```

In 3.35D, `clear_fs_flag` and `set_fs_flag` are called sequentially when N is
clear. The clear is immediately undone by the set, so the EOF hint bit is
always SET regardless of the actual file position. This renders the EOF hint
cache useless — every BGET would mark the file as "possibly at EOF", forcing
an unnecessary network round-trip on the next EOF check even when the file
pointer is nowhere near the end.

In 3.35K, the two operations are mutually exclusive: only `clear_fs_flag` is
called when not at EOF, and only `set_fs_flag` when at EOF.

### 5. BGETV escape handler: Y register initialised

A single instruction (`LDY #0`) is inserted at &8526 in 3.35K before a
`STA (net_tx_ptr),Y` in the escape handling path of BGETV:

**3.35D** (at &8533):
```
    LSR A
    STA (net_tx_ptr),Y   ; Y is uninitialised
```

**3.35K** (at &8526):
```
    LDY #0               ; initialise Y
    LSR A
    STA (net_tx_ptr),Y   ; Y is now 0
```

In 3.35D, Y could hold any value at this point (it was last set during the
`handle_bput_bget` common path but may have been modified by the OSBYTE escape
acknowledge call), causing the store to write to an incorrect offset within
the transmit buffer.

### 6. Tube OSGBPB: carry result now sent to co-processor

The Tube host code for OSGBPB (in the page 5 relocated block, runtime &0612)
had a bug where the OSGBPB completion status was lost:

**3.35D** (ROM &9574, runtime &0615):
```
    JSR osgbpb         ; &0612
    PHA                ; &0615: save A (never sent or popped!)
    LDX #&0C           ; &0616: 13 parameter bytes
    ...send loop...
    JMP &055F           ; &0620: return via intermediate handler
```

**3.35K** (ROM &956F, runtime &0615):
```
    JSR osgbpb         ; &0612
    ROR A              ; &0615: encode carry into bit 7
    JSR tube_send_r2   ; &0616: send carry+result byte first
    LDX #&0C           ; &0619: 13 parameter bytes
    ...send loop...
    JMP tube_main_loop ; &0623: return to Tube command dispatcher
```

In 3.35D, after calling OSGBPB, the accumulator (containing the result and
carry indicating whether the transfer completed) is pushed to the stack but
never transmitted to the co-processor and never popped. The co-processor has
no way to determine whether the OSGBPB operation completed or was truncated.

In 3.35K, A is rotated right (ROR encodes carry into bit 7) and sent via
`tube_send_r2` before the 13 control block bytes, allowing the co-processor
to decode the completion status. The return target also changes from an
intermediate handler (&055F) to `tube_main_loop` (&003A), the standard Tube
command dispatch loop used by other Tube handlers.

### 7. FINDV: sequence number initialisation added

When a file is opened via FINDV, 3.35K adds initialisation of the sequence
number tracking byte (`fs_sequence_nos` at &0E08):

**3.35K** inserts at &89A1 (3 instructions):
```
    TXA                    ; restore handle bitmask
    ORA fs_sequence_nos    ; OR handle bit into &0E08
    STA fs_sequence_nos    ; store updated sequence numbers
```

In 3.35D, opening a file OR's the handle bit into the EOF hint flags
(`fs_eof_flags` at &0E07) but NOT into the sequence number byte. Without
this initialisation, a newly opened file could start with a stale sequence
number from a previous file that used the same handle, potentially causing
byte-stream protocol errors (duplicate or out-of-order data frames).

### 8. Error handler: SPOOL/EXEC handle closing restructured

The error handler code that closes any SPOOL or EXEC file matching the
errored handle was restructured.

**3.35D** (at &8437-&8449):
```
    LDA #&F1           ; default: "SP.\r" string
    CPY &BA            ; SPOOL handle matches?
    BEQ &8443          ; yes: close SPOOL
    LDA #&F5           ; "E.\r" string
    CPX &BA            ; EXEC handle matches?
    BNE &8449          ; no: skip OSCLI entirely
.c8443
    TAX / LDY #&84 / JSR OSCLI
```

**3.35K** (at &8428-&8439):
```
    LDA #&EA           ; default: ".\r" (harmless)
    CPY &BA            ; SPOOL handle matches?
    BNE &8430          ; no: skip to EXEC check
    LDA #&E4           ; yes: "SP.\r" string
.c8430
    CPX &BA            ; EXEC handle matches?
    BNE &8436          ; no: skip
    LDA #&E8           ; yes: "E.\r" string
.c8436
    TAX / LDY #&84 / JSR OSCLI   ; always called
```

In 3.35D, the BEQ at the SPOOL check means that if SPOOL matches, the code
jumps directly to OSCLI without ever checking the EXEC handle — so if both
SPOOL and EXEC use the same handle, only the SPOOL close runs.

In 3.35K, both checks always execute: SPOOL is checked first, then EXEC. If
EXEC matches, its command string overrides the SPOOL one. If neither matches,
the default `".\r"` is passed to OSCLI, which is effectively a no-op.

### 9. Error handler: retry count read from &0FDE instead of &CF

At &841A (3.35D) / &840A (3.35K), the error handler reads the retry count
from a different location:

| Version | Instruction     | Address |
|---------|-----------------|---------|
| 3.35D   | LDA &CF         | Zero page |
| 3.35K   | LDA &0FDE       | Absolute workspace |

This change is connected to the workspace variable reversion (change 3): &CF
is now used by `fs_temp_cd`, so the retry count is read from its absolute
workspace copy at &0FDE instead.

### 10. *EX file info printing: CSD check removed

The `print_file_info` routine (3.35D: &8CFA, 3.35K: &8CFC) had a conditional
check that is removed in 3.35K:

**3.35D** (at &8D01-&8D09):
```
    LDX fs_cmd_csd     ; &8D01: load CSD handle from &0F03
    BEQ &8D0B          ; if zero, skip to print filename
    JSR &8D61          ; check fs_cmd_data[X] bit 7
    BMI &8D23          ; if set, skip filename — show hex only
```

In 3.35K, these 4 instructions (7 bytes) are removed. The filename is always
printed in `*EX` output regardless of the CSD handle state.

### 11. OSARGS dispatch simplified

The OSARGS handler dispatch for Y=0 (filing system query) was reorganised.
Both versions return the same results:

| A value | Result | 3.35D method            | 3.35K method    |
|---------|--------|-------------------------|-----------------|
| 0       | 5      | LDA #&0A; LSR A         | LDA #5          |
| 1       | copy   | TAY; BNE osarg1         | LSR A (→0); BNE |
| 2       | 1      | CMP #2; BEQ; LSR A      | LSR A (→1); BNE |
| ≥3      | 0      | BCS (already rejected)  | BCS (rejected)  |

The result for A=0 (filing system number 5) is computed identically by
different methods. The overall logic is functionally equivalent but 3 bytes
shorter.

### 12. set_fs_flag / clear_fs_flag reordered

The pair of routines for setting and clearing per-handle EOF hint bits in
`fs_eof_flags` (&0E07) were reordered. In 3.35D, `set_fs_flag` comes first
and falls through to the shared `STA fs_eof_flags`; `clear_fs_flag` follows
and also falls through. In 3.35K, `clear_fs_flag` comes first (with a JMP
to the shared store), and `set_fs_flag` follows. The result is functionally
equivalent but saves 1 byte by using overlapping instruction encoding.

### 13. JMP replaced with BNE

At &85F7 (3.35D) / &85EE (3.35K), a 3-byte `JMP` is replaced with a 2-byte
`BNE` which is always taken (the preceding code guarantees Z=0). Saves 1 byte.

### 14. sub_c83c6 inlined at call sites

3.35D has a small wrapper subroutine at &83C4-&83C8 that loads `#&2A` ('*')
into `fs_error_ptr` (&B8) before falling through to `send_fs_reply_cmd`. In
3.35K, this wrapper is eliminated. The two call sites inline the `LDA #&2A`
/ `STA &B8` sequence before calling `send_fs_reply_cmd` directly (at &87B0
and &8A97).

### 15. EVNTV target shifted +3

The EVNTV handler address set during initialisation changed from &06E5
(3.35D) to &06E8 (3.35K), tracking the shifted position of
`tube_event_handler` within the page 6 relocated code. The entry point
difference reflects a 3-byte code change earlier in page 6. All other vector
targets (BRKV, WRCHV, RDCHV) are unchanged.

### 16. Shifted address operands

All code throughout the ROM has shifted address operands due to the cumulative
effect of insertions and deletions. The shifts are non-uniform, varying by
region. Approximately 150 instructions have different operand values while
retaining the same opcode and logical target.

## Address map

The address mapping between 3.35D and 3.35K is non-linear, with 44 change
blocks. Key entry point mappings:

| Function              | 3.35D   | 3.35K   | Offset  |
|-----------------------|---------|---------|---------|
| Language entry        | &80D4   | &80D4   | +0      |
| Service entry         | &80EA   | &80EA   | +0      |
| Init vectors          | &810D   | &8103   | -&0A    |
| Version string        | &81FA   | &81F0   | -&0A    |
| Service dispatch      | &8150   | &8146   | -&0A    |

Relocated code block ROM sources (all -5 bytes):

| Block        | 3.35D  | 3.35K  | Runtime       | Size      |
|--------------|--------|--------|---------------|-----------|
| BRK handler  | &931A  | &9315  | &0016-&0076   | 97 bytes  |
| Page 4       | &935F  | &935A  | &0400-&04FF   | 256 bytes |
| Page 5       | &945F  | &945A  | &0500-&05FF   | 256 bytes |
| Page 6       | &955F  | &955A  | &0600-&06FF   | 256 bytes |
