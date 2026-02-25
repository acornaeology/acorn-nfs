# Changes from NFS 3.35K to NFS 3.40

NFS 3.40 is a substantial revision of Acorn NFS 3.35K for the BBC Micro. The
two 8 KB ROMs are 89.4% identical at the opcode level, with 162 structural
change blocks. Key changes include: restoration of the per-ROM disable flag
(removed in 3.35K) with a new hardware-probing mechanism, reversion from
table-driven to hardcoded vector initialisation (setting only EVNTV and BRKV),
addition of a Tube character transfer loop during Tube init, expansion of the
dispatch table by one entry (service 13: select NFS), a switch from
non-vectored to vectored WRCH in the Tube main loop, reduction of the NMI
workspace by 4 bytes, and relocation of print_hex to the end of ROM. A hidden
developer credits string appears for the first time.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 215 (2.6%)   |
| Byte-level similarity           | 83.4%        |
| Opcode-level similarity         | 89.4%        |
| Full instruction similarity     | 75.3%        |
| Instructions (3.35K / 3.40)     | 4024 / 4043  |
| Structural change blocks        | 162          |

The identical-byte count (2.6%) is extremely low because the extensive code
insertions and deletions shift address operands throughout nearly the entire
ROM. Even where the opcode and logical target are unchanged, the operand bytes
differ. The opcode-level similarity (89.4%) is the best measure of structural
equivalence.

## ROM header

| Field             | 3.35K     | 3.40        |
|-------------------|-----------|-------------|
| Title             | "NET"     | "    NET"   |
| ROM type          | &82       | &82         |
| Binary version    | &03       | &83         |
| Copyright         | "(C)ROFF" | "(C)ROFF"   |
| Language entry    | &80D4     | &80E1       |
| Service entry     | &80EA     | &80F7       |

Three header fields changed. The title gains 4 leading spaces ("NET" →
"    NET"), the binary version changes from &03 to &83 (bit 7 set), and both
entry points shift +&0D bytes due to the expanded title and code insertions.
The copyright offset shifts from &0C to &10 to accommodate the longer title.

## Changes

### 1. Version string: "3.35K" to "3.40"

The ROM identification string printed by `*HELP` (at &81F0 in 3.35K, &8207 in
3.40) changed from `"NFS 3.35K"` to `"NFS 3.40"`. The string is one byte
shorter (8 vs 9 characters), contributing to the address shifts downstream.

### 2. Per-ROM disable flag restored (new mechanism)

3.35K removed the per-ROM disable flag check that 3.35D introduced. 3.40
restores it with a completely different implementation. The service handler
(&80F7) now begins with 9 NOP bytes followed by a new guard sequence:

```assembly
    PHA                         ; save service number
    LDA &0DF0,X                 ; read per-ROM flag (X = ROM bank)
    PHA                         ; save flag value
    BNE c8118                   ; if already initialised, skip probe
    INC &0DF0,X                 ; first call: set flag to 1
    LDA &FE18                   ; read Econet station ID register
    BEQ c8114                   ; if zero (no hardware), disable
    CMP &FE18                   ; read again and compare
    BEQ c8118                   ; if stable, hardware present — OK
.c8114
    SEC
    ROR &0DF0,X                 ; set bit 7 = disable flag
.c8118
    PLA                         ; recover flag
    ASL A                       ; shift bit 7 into carry
    PLA                         ; recover service number
    BMI c811f                   ; if &FE/&FF, always handle
    BCS c818d                   ; if carry set (disabled), skip handler
```

Where 3.35D's version simply checked a software flag, 3.40 actively probes the
Econet station ID register (&FE18) on first call. If the register reads zero or
gives inconsistent values between two reads, the ROM disables itself. This
provides automatic hardware detection: NFS silently disables on machines without
Econet hardware, avoiding wasted service call overhead.

The 9 NOP bytes at &80F7-&80FF likely represent code that was patched out during
development.

### 3. Service &FE (Tube init) handler rewritten

In 3.35K, the service &FE handler saves X and Y to zero page (`zp_temp_10`/
`zp_temp_11`) before calling OSBYTE &14 to explode character definitions, then
restores X and branches to the main service dispatch continuation:

```assembly
    STX zp_temp_11              ; &80F4: save X
    STY zp_temp_10              ; &80F6: save Y
    LDX #6                      ; &80F8
    LDA #osbyte_explode_chars   ; &80FA
    JSR osbyte                  ; &80FC: explode chars (X=6 pages)
    LDX zp_temp_11              ; &80FF: restore X
    BNE c8142                   ; &8101: branch to dispatch continuation
```

In 3.40, the X/Y save is omitted and a new Tube character transfer loop is
added after exploding characters:

```assembly
    LDX #6                      ; &8129
    LDA #osbyte_explode_chars   ; &812B
    JSR osbyte                  ; &812D: explode chars (X=6 pages)
.c8130
    BIT &FEE0                   ; poll Tube R1 status
    BPL c8130                   ; wait until data available
    LDA &FEE1                   ; read Tube R1 data byte
    BEQ c817d                   ; zero byte = end of transfer
    JSR oswrch                  ; output character via WRCH vector
    JMP c8130                   ; loop
```

This reads characters from the Tube co-processor via R1 and outputs them via
OSWRCH until a zero terminator is received — likely printing co-processor
startup or identification messages during Tube initialisation.

### 4. Vector initialisation reverted to hardcoded (2 vectors only)

3.35K uses a table-driven loop that reads 4 triplets from a data table at
`return_2`+1 (&816D) and sets 4 vectors: EVNTV, BRKV, RDCHV, and WRCHV.

3.40 reverts to hardcoded LDA/STA pairs but sets only 2 vectors:

```assembly
.init_vectors_and_copy
    LDA #&AD : STA &0220       ; EVNTV lo → &06AD
    LDA #6   : STA &0221       ; EVNTV hi
    LDA #&16 : STA &0202       ; BRKV lo  → &0016
    LDA #0   : STA &0203       ; BRKV hi
    LDA #&8E                    ; Tube control: enable all registers
    STA &FEE0
    LDY #0                      ; Y=0 for page copy loop
```

RDCHV (&0210) and WRCHV (&020E) are no longer set during NFS initialisation.
The 12-byte vector data table that followed `return_2` in 3.35K is removed.

### 5. Dispatch table expanded: service 13 (select NFS)

The PHA/PHA/RTS dispatch table grows from 36 to 37 entries. A new entry at
index 13 points to `svc_13_select_nfs`, which replaces the direct branch to
`select_nfs` that 3.35K used for service &12 (select FS) with Y=5.

In 3.35K, service &12/Y=5 was handled by special-case code before the dispatch
table:

```assembly
    CMP #&12                    ; &8146
    BNE c814e
    CPY #5
    BEQ select_nfs              ; direct branch
```

In 3.40, the same check remaps A to &0D and falls through to the normal
dispatch mechanism:

```assembly
    CMP #&12                    ; &817F
    BNE c818b
    CPY #5
    BNE c818b
    LDA #&0D                    ; remap to service 13
    BNE c818f                   ; ALWAYS branch to dispatch
```

All base offsets in the dispatch table shift up by 1:

| Caller          | 3.35K base | 3.40 base |
|-----------------|------------|-----------|
| Service calls   | Y=&00      | Y=&00     |
| Language entry  | Y=&0D      | Y=&0E     |
| FSCV            | Y=&12      | Y=&13     |
| FS reply        | Y=&16      | Y=&17     |
| *NET dispatch   | Y=&20      | Y=&21     |

### 6. Service handler epilogue: romsel_copy restored

The service handler epilogue at `svc_star_command` changed:

**3.35K** (&8168):

```assembly
    PLA                         ; restore saved value
    STA rom_svc_num             ; → &CE
    TXA
    RTS
```

**3.40** (&81A5):

```assembly
    PLA                         ; restore saved value
    STA l00a9                   ; → &A9 (see change 7)
    TXA
    LDX romsel_copy             ; restore ROM bank from &F4
    RTS
```

The epilogue now explicitly restores the ROM bank select register from
`romsel_copy` (&F4) before returning. This ensures the correct ROM is paged in
after dispatched service handlers that may have changed the bank.

### 7. Workspace variables: &CD/&CE back to &A8/&A9

3.35K reverted the workspace variables `nfs_temp` and `rom_svc_num` from
3.35D's &A8/&A9 addresses back to their original &CD/&CE locations. 3.40
reverses this change, moving them back to &A8/&A9:

| Variable       | 3.34B | 3.35D | 3.35K | 3.40  |
|----------------|-------|-------|-------|-------|
| `nfs_temp`     | &CD   | &A8   | &CD   | &A8   |
| `rom_svc_num`  | &CE   | &A9   | &CE   | &A9   |

The 3.40 assembly uses `l00a8` and `l00a9` throughout where 3.35K used
`nfs_temp` and `rom_svc_num`. This affects every instruction that accesses
these zero page locations.

### 8. *ROFF/*NET match offsets shifted

The `svc_4_star_command` handler matches star commands by comparing input text
against bytes in the ROM header. The match starting offsets changed because the
title string grew by 4 bytes:

| Command | 3.35K offset | 3.40 offset | Target bytes |
|---------|-------------|-------------|--------------|
| *ROFF   | X=8         | X=&0C       | "ROFF" in copyright string |
| *NET    | X=1         | X=5         | "NET" in title string      |

### 9. Tube main loop: nvwrch to oswrch

The WRCH handler in the Tube main loop (in the BRK handler workspace at runtime
&003B/&003F) changes from non-vectored to vectored character output:

**3.35K** (runtime &003F):

```assembly
    LDA &FEE1                   ; read Tube R1 data byte
    JSR nvwrch                  ; &FFCB: non-vectored write character
```

**3.40** (runtime &003B):

```assembly
    LDA &FEE1                   ; read Tube R1 data byte
    JSR oswrch                  ; &FFEE: vectored write character
```

This routes Tube character output through the standard OS WRCH vector
indirection, allowing other ROMs to intercept WRCH calls from the Tube
co-processor.

### 10. NMI workspace reduced by 4 bytes

The BRK handler / NMI workspace block copied from ROM to zero page shrinks from
69 to 65 bytes:

| Field                | 3.35K    | 3.40     |
|----------------------|----------|----------|
| ROM source           | &9315    | &931C    |
| Runtime range        | &16-&5A  | &16-&56  |
| Size                 | 69 bytes | 65 bytes |
| `tube_dispatch_cmd`  | &0055    | &0051    |
| `tube_transfer_addr` | &0057    | &0053    |
| `zp_63`              | &0063    | &005F    |

The Tube command byte and transfer address variables shift down by 4, matching
the 4-byte reduction. The `tube_main_loop` entry point moves from runtime &003A
to &0036. The workspace also loses the X/Y save at &0036/&0038 that 3.35K had
(see change 3 — those are no longer needed).

### 11. Tube dispatch table: 14 to 12 entries

The Tube command handler address table at &0500 (page 5) shrinks from 14
entries (28 bytes) to 12 entries (24 bytes):

**3.35K** (14 entries at &945A):

```assembly
    equb &5b,5, &c5,5, &26,6, &3b,6, &5d,6, &a3,6, &ef,4
    equb &3d,5, &8c,5, &50,5, &43,5, &69,5, &d8,5,   2,6
```

**3.40** (12 entries at &9456):

```assembly
    equb &37,5, &96,5, &f2,5,   7,6, &27,6, &68,6, &5e,5
    equb &2d,5, &20,5, &42,5, &a9,5, &d1,5
```

Two handler entries were removed. The page 4 relocated code block also shrinks
from 256 to 249 bytes, consistent with handler removal or consolidation.

### 12. Tube post-init: new R4 handshake

In 3.35K, `tube_post_init` (runtime &0414) simply stores &80 to `l0014` and
returns. 3.40 inserts a new subroutine before `tube_post_init` that sends two
bytes to the co-processor via Tube R4:

```assembly
.sub_c0414
    LDA #5                      ; protocol command byte
    JSR tube_send_r4            ; send to co-processor via R4
    LDA l0015                   ; current Tube status byte
    JSR tube_send_r4            ; send status to co-processor
.tube_post_init
    LDA #&80                    ; &041E (was &0414 in 3.35K)
    STA l0014
    RTS
```

This new R4 handshake during initialisation may be a Tube protocol extension
that communicates the host's capabilities or status to the co-processor.

### 13. print_hex relocated to end of ROM

`print_hex` moves from &8D9D (3.35K) to &9FE0 (3.40) — a shift of +&1243
bytes to the very end of the ROM, just before 8 bytes of &FF padding.

The nibble-to-ASCII conversion algorithm also changes:

**3.35K** (&8DA8):

```assembly
    ORA #&30                    ; add ASCII '0'
    CMP #&3A                    ; result >= ':'?
    BCC output                  ; if < ':', it's 0-9
    ADC #6                      ; adjust for A-F
```

**3.40** (&9FE9):

```assembly
    AND #&0F                    ; isolate low nibble
    CMP #&0A                    ; nibble >= 10?
    BCC c9ff1                   ; if < 10, skip
    ADC #6                      ; pre-adjust for A-F
.c9ff1
    ADC #&30                    ; add ASCII '0'
    JSR osasci                  ; output character
    SEC                         ; set carry (return flag)
    RTS
```

The 3.40 version is functionally equivalent but structured differently: it
checks the nibble value before adding the ASCII base, rather than after. It also
makes `print_hex_nibble` self-contained (ending with JSR/SEC/RTS) instead of
falling through to the `print_reply_bytes` loop as in 3.35K. The explicit
`SEC` before `RTS` establishes a documented carry-set return convention.

### 14. boot_cmd_execute extracted as subroutine

Boot command execution logic is extracted into a new standalone subroutine
`boot_cmd_execute` at &8E3A:

```assembly
.boot_cmd_execute
    LDY fs_boot_option          ; &8E3A: read boot option from &0E05
    LDX l8d1c,Y                 ; look up command string offset
    LDY #&8D                    ; high byte of command string page
    JMP oscli                   ; execute via OSCLI
```

In 3.35K this logic was inline within `fsreply_1_copy_handles_boot`.

### 15. Developer credits string

The string `"Brian,Hugo,Jes and Roger"` appears at &9FC8, occupying 24 bytes
of otherwise unused ROM space between the end of the NMI handler code and
`print_hex` at &9FE0. This credits string is not present in any earlier NFS
version. The fragment `"Jes"` visible at &9624 in the page 6 relocated code
area is part of the same ROM bytes, accessed at a different offset when the page
6 block is copied to RAM.

### 16. Shifted address operands

As in previous version transitions, code throughout the ROM has shifted address
operands due to the cumulative effect of insertions and deletions. The shifts
are highly non-uniform — ranging from approximately -51 to +63 bytes depending
on region — reflecting the scattered nature of the code changes across the ROM.
The 162 structural change blocks and only 2.6% byte-level identity confirm that
nearly every instruction's operand bytes are affected.

## Address map

The address mapping between 3.35K and 3.40 is non-linear, with 162 change
blocks. Key entry point mappings:

| Function              | 3.35K   | 3.40    | Offset  |
|-----------------------|---------|---------|---------|
| Language entry        | &80D4   | &80E1   | +&0D    |
| Service entry         | &80EA   | &80F7   | +&0D    |
| Init vectors          | &8103   | &8140   | +&3D    |
| Version string        | &81F0   | &8207   | +&17    |
| Service dispatch      | &8146   | &817F   | +&39    |
| print_hex             | &8D9D   | &9FE0   | +&1243  |

Relocated code block ROM sources:

| Block        | 3.35K  | 3.40   | Runtime       | Size      |
|--------------|--------|--------|---------------|-----------|
| BRK handler  | &9315  | &931C  | &0016-&0056   | 65 bytes  |
| Tube host (pg 4) | &935A  | &935D  | &0400-&04F8   | 249 bytes |
| Tube host (pg 5) | &945A  | &9456  | &0500-&05FF   | 256 bytes |
| Tube host (pg 6) | &955A  | &9556  | &0600-&06FF   | 256 bytes |

The BRK handler block shrinks from 69 to 65 bytes (-4). Page 4 shrinks from
256 to 249 bytes (-7). Pages 5 and 6 remain at 256 bytes each.
