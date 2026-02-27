# Changes from NFS 3.40 to NFS 3.60

NFS 3.60 is a substantial revision of Acorn NFS 3.40 for the BBC Micro. The two
8 KB ROMs are 89.9% identical at the opcode level, with 118 structural change
blocks. Key changes include: a rewritten ADLC-based hardware detection mechanism
(replacing the station ID probe), a new escapable flag system for interruptible
network operations, relocation of `tx_poll_core` and `print_file_info` into the
FS vector handler region, extraction of `clear_escapable` and
`save_fscv_args_with_ptrs` as separate subroutines, factoring out
`inc_buf_counter_32` and `release_tube` from inline code, relocation of
`adlc_full_reset` / `adlc_rx_listen` / `wait_idle_and_reset` to end of ROM, a
new `svc5_dispatch` trampoline for page 6 relocated code, NMI interrupt
protection via PHP/SEI/PLP around the scout handler, a new BGETV entry point
via `clear_escapable`, and the `prot_flags` variable moved from absolute to zero
page. The developer credits string is removed and the free space at end of ROM
increases from 8 to 75 bytes.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 8192 bytes   |
| Identical bytes at same offset  | 398 (4.9%)   |
| Byte-level similarity           | 85.7%        |
| Opcode-level similarity         | 89.9%        |
| Full instruction similarity     | 61.2%        |
| Instructions (3.40 / 3.60)      | 4043 / 4073  |
| Structural change blocks        | 118          |

The identical-byte count (4.9%) is extremely low because the extensive code
insertions and deletions shift address operands throughout nearly the entire
ROM. Even where the opcode and logical target are unchanged, the operand bytes
differ. The opcode-level similarity (89.9%) is the best measure of structural
equivalence.

## ROM header

| Field             | 3.40      | 3.60        |
|-------------------|-----------|-------------|
| Title             | "    NET" | "    NET"   |
| ROM type          | &82       | &82         |
| Binary version    | &83       | &83         |
| Copyright         | "(C)ROFF" | "(C)ROFF"   |
| Language entry    | &80E1     | &80E1       |
| Service entry     | &80F7     | &80F7       |

All header fields are unchanged. The language and service entry points remain
at the same ROM offsets despite the code changes — the net effect of insertions
and deletions leaves the entry points at &80E1 and &80F7.

## Changes

### 1. Version string: "3.40" to "3.60"

The ROM identification string printed by `*HELP` (at &8207 in 3.40, &820B in
3.60) changed from `"NFS 3.40"` to `"NFS 3.60"`. The string length is the same
(8 characters). The 4-byte address shift is caused by upstream code insertions.

### 2. Per-ROM hardware detection rewritten (ADLC probe)

Both versions disable NFS when Econet hardware is absent, but the detection
mechanism is completely different.

**3.40** (&8100): probes the station ID register at &FE18 on first call:

```assembly
    PHA                         ; save service number
    LDA &0DF0,X                 ; read per-ROM workspace flag
    PHA                         ; save flag value
    BNE adlc_detect_done        ; if already tested, skip probe
    INC &0DF0,X                 ; first call: mark ROM as present
    LDA &FE18                   ; read Econet station ID
    BEQ no_adlc_found           ; zero: no hardware
    CMP &FE18                   ; read again: bus stability check
    BEQ adlc_detect_done        ; stable: hardware present
.no_adlc_found
    SEC
    ROR &0DF0,X                 ; set bit 7 = disable flag
.adlc_detect_done
    PLA                         ; recover flag
    ASL A                       ; shift bit 7 into carry
    PLA                         ; recover service number
```

**3.60** (&8100): probes ADLC status registers on service 1 only:

```assembly
    PHA                         ; save service number
    CMP #1                      ; only probe on service 1
    BNE check_disable_flag      ; not service 1: skip probe
    LDA &FEA0                   ; probe ADLC SR1
    AND #&ED                    ; mask status bits (ignore bits 4,1)
    BNE set_adlc_disable        ; non-zero: ADLC active, set flag
    LDA &FEA1                   ; probe ADLC SR2
    AND #&DB                    ; mask status bits (ignore bits 5,2)
    BEQ check_disable_flag      ; both zero: no ADLC present
.set_adlc_disable
    ROL &0DF0,X                 ; shift current bits left
    SEC
    ROR &0DF0,X                 ; rotate carry into bit 7
.check_disable_flag
    LDA &0DF0,X                 ; read back flag
    ASL A                       ; bit 7 into carry
    PLA                         ; recover service number
```

The key differences:

- **3.40** reads the station ID register (&FE18) twice and compares for bus
  stability. This probe runs on every service call until the workspace flag is
  set, regardless of service number.
- **3.60** reads the ADLC status registers SR1 (&FEA0) and SR2 (&FEA1),
  masking out reserved/uninteresting bits. The probe only runs on service 1
  (workspace claim), avoiding unnecessary hardware access on other service
  calls. If another NFS ROM has already initialised the ADLC, SR1/SR2 will
  contain non-zero status bits, marking this ROM as a duplicate.
- **3.40** uses INC followed by SEC/ROR to set the flag. **3.60** uses
  ROL/SEC/ROR, which preserves any existing low bits in the workspace byte.

The 3.60 approach is more robust: it detects whether the ADLC hardware has
actually been initialised by another ROM (via its status registers) rather than
just testing whether the station ID register responds. This correctly handles
the case where Econet hardware is present but another ROM's NFS has already
claimed it.

### 3. check_escape_handler replaced by escapable flag system

3.40 has a single `check_escape_handler` subroutine at &854D that
unconditionally tests the MOS escape flag and aborts if escape is pending:

```assembly
.check_escape_handler
    BIT &FF                     ; test escape flag
    BPL return_4                ; no escape: return
    LDA #&7E                    ; OSBYTE &7E: acknowledge escape
    JSR osbyte
    LSR A                       ; store escape result
    STA (net_tx_ptr),Y
    ASL A
    BNE nlisne                  ; report 'Not listening'
```

3.60 replaces this with a two-part system:

1. An `escapable` flag at zero page &97 that gates escape checking
2. A new `check_escape` routine at &84A1 that tests both the MOS escape flag
   AND the escapable flag:

```assembly
.check_escape
    LDA &FF                     ; read escape flag
    AND escapable               ; mask with escapable flag
    BPL return                  ; both bits 7 must be set
    LDA #&7E                    ; OSBYTE &7E: acknowledge escape
    JSR osbyte
    JMP nlisne                  ; report escape error
```

The `escapable` flag is managed via `clear_escapable` at &8657 (PHP/LSR
&97/PLP: clears bit 7 while preserving processor flags). Multiple call sites
explicitly set `escapable` before escapable operations:

- `STA escapable` with A=&92 before `filev_load_data` (&8724)
- `STA escapable` with A=&91 before `filev_save` (&87C1)
- `STX escapable` with X=non-zero before `*EX` (&8C22)
- `STY escapable` with Y=&FF before `*INFO` (&8C6D)
- `STA escapable` with A=non-zero before OSWORD Econet operations (&900F)

This allows NFS to selectively enable escape checking only during long-running
operations (file transfers, catalogue listings, network transmit), preventing
spurious escape interrupts during short internal operations.

### 4. BGETV entry point: clear_escapable added

3.40 has `bgetv_handler` at &855C as a simple SEC/JSR sequence:

```assembly
.bgetv_handler
    SEC                         ; C=1: BGET mode
    JSR handle_bput_bget        ; handle via FS command
```

3.60 inserts a new `bgetv_entry` at &8414 that clears the escapable flag
before falling through to `handle_bput_bget`:

```assembly
.bgetv_entry
    JSR clear_escapable         ; clear escapable flag
; falls through to handle_bput_bget
.handle_bput_bget
    ...
```

The BGETV caller at &8564 now calls `bgetv_entry` instead of `bgetv_handler`.
The `bputv_handler` at &8413 (CLC) falls through directly to
`handle_bput_bget`, so BPUT operations also benefit from the cleared
escapable flag via the shared code path.

### 5. tx_poll_core relocated and restructured

`tx_poll_core` — the core transmit polling loop with retry and timeout
logic — moves from &8693 (3.40) to &8603 (3.60), a shift of -&90 bytes.
This brings it closer to its callers in the FS vector handler region.

The 3.60 version has two functional changes:

1. **ADLC TX setup**: 3.40 calls `trampoline_tx_setup` (JMP via page 6 to the
   full `start_adlc_tx` routine). 3.60 calls `start_adlc_tx` directly,
   bypassing the page 6 trampoline — possible because the ADLC setup code
   has been relocated into the main ROM (see change 12).

2. **Success epilogue**: 3.40 ends with a plain PLA/PLA/PLA/RTS. 3.60 ends
   with PLA/PLA/PLA followed by `JMP clear_escapable`, which clears the
   escapable flag via PHP/LSR/PLP before returning. This ensures escape
   checking is disabled after a successful transmit.

### 6. save_fscv_args_with_ptrs extracted (store_fs_ptrs removed)

3.40 has `save_fscv_args_with_ptrs` at &85C8, a standalone subroutine called
from the language entry point that stores X/Y into multiple locations:

```assembly
.sub_c85c8
    STX &F2                     ; os_text_ptr lo
    STY &F3                     ; os_text_ptr hi
    STX &0E10                   ; fs_cmd_ptr lo
    STY &0E11                   ; fs_cmd_ptr hi
    STA &BD                     ; fs_last_byte_flag
    STX &BB                     ; fs_options
    STY &BC                     ; fs_block_offset
    STX &BE                     ; fs_crc_lo
    STY &BF                     ; fs_crc_hi
    RTS
```

3.60 replaces this with two smaller, composable subroutines:

```assembly
.save_fscv_args_with_ptrs       ; &8649
    STX &F2                     ; os_text_ptr lo
    STY &F3                     ; os_text_ptr hi
; falls through to save_fscv_args
.save_fscv_args                 ; &864D
    STA &BD                     ; fs_last_byte_flag
    STX &BB                     ; fs_options
    STY &BC                     ; fs_block_offset
    STX &BE                     ; fs_crc_lo
    STY &BF                     ; fs_crc_hi
; falls through to clear_escapable
.clear_escapable                ; &8657
    PHP
    LSR escapable               ; clear bit 7
    PLP
    RTS
```

The `STX &0E10` / `STY &0E11` stores are removed — `fs_cmd_ptr` is no
longer set during this entry path. And `clear_escapable` is appended as a
fall-through from `save_fscv_args`, so every FS vector entry now
automatically clears the escapable flag.

### 7. print_file_info relocated to filev_save

`print_file_info` (the routine that displays filename, load/exec addresses,
and file length during `*LOAD`, `*SAVE`, and `*EX`) moves from &8D24 (3.40) to
the `filev_save` handler area in 3.60. In 3.40, `print_file_info` is called
via JSR from `filev_load_data` (&874C) and `filev_save` (&87CA):

```assembly
    JSR print_file_info         ; 3.40: &874C / &87CA
```

In 3.60, the `print_file_info` logic is inlined within the `filev_save`
handler's `save_csd_display` code (&87D8). The standalone `print_file_info`
subroutine at &8D24 no longer exists; its functionality is split between the
inline code at &87E5-&8810 and the remaining `print_hex_bytes` / `num01`
routines.

The display format also changes slightly: 3.40 terminates filenames on CR
(&0D) or space (&20); 3.60 terminates on characters below &21 (i.e. any
control character or space). The padding space printing uses `print_space`
at &8D7B (3.60) vs &8D6E (3.40).

### 8. inc_buf_counter_32 extracted as subroutine

The 4-byte increment sequence `INC &A2 / BNE + / INC &A3 / BNE + / INC &A4 /
BNE + / INC &A5` appears inline twice in 3.40 (at &98E5 and &98FE in the NMI
data receive handler). 3.60 extracts this into a standalone subroutine
`inc_buf_counter_32` at &9A37:

```assembly
.inc_buf_counter_32
    INC port_buf_len            ; &A2
    BNE done
    INC port_buf_len_hi         ; &A3
    BNE done
    INC open_port_buf           ; &A4
    BNE done
    INC open_port_buf_hi        ; &A5
.done
    RTS
```

The two inline occurrences are replaced with `JSR inc_buf_counter_32`, saving
approximately 10 bytes of ROM. The subroutine returns Z=1 if the counter wraps
to zero, which the callers test to detect buffer overflow.

A third call site at &9A1F (in the Tube scout copy path) also uses this
routine.

### 9. release_tube extracted as subroutine

In 3.40, the Tube release sequence — test `need_release_tube`, call
`tube_addr_claim` with A=&82, then clear the flag — appears inline at &9A38
(in the TX acknowledgement path). 3.60 extracts it as `release_tube` at &9A2B:

```assembly
.release_tube
    BIT need_release_tube       ; &98
    BMI clear_release_flag      ; bit 7 set: already released
    LDA #&82                    ; Tube release claim type
    JSR tube_addr_claim
.clear_release_flag
    LSR need_release_tube       ; LSR clears bit 7
    RTS
```

This subroutine is called from two sites: the TX acknowledgement path (&99E5)
and `tx_calc_transfer` (&9F12). In 3.40, the `tx_calc_transfer` path did not
call `release_tube` — the JSR at &9F12 is a new call site in 3.60.

### 10. adlc_full_reset and adlc_rx_listen relocated to end of ROM

In 3.40, `adlc_full_reset` (&96D8) and `adlc_rx_listen` (&96E7) sit within the
ADLC initialisation region. 3.60 moves both to near the end of ROM:

| Routine          | 3.40   | 3.60   |
|------------------|--------|--------|
| adlc_full_reset  | &96D8  | &9F3D  |
| adlc_rx_listen   | &96E7  | &9F4C  |

The code is functionally identical:

```assembly
.adlc_full_reset
    LDA #&C1                    ; CR1: TX+RX reset, AC set
    STA &FEA0
    LDA #&1E                    ; CR4: 8-bit, abort extend, NRZ
    STA &FEA3
    LDA #0                      ; CR3: no loopback/AEX/DTR
    STA &FEA1
.adlc_rx_listen
    LDA #&82                    ; CR1: TX reset, RX interrupts on
    STA &FEA0
    LDA #&67                    ; CR2: clear status, PSE, 2/1 byte
    STA &FEA1
    RTS
```

The relocation frees space in the ADLC init region for the new
`svc5_dispatch` and `start_adlc_tx` code (see changes 12-13).

### 11. wait_idle_and_reset relocated to end of ROM

`wait_idle_and_reset` (the routine that waits for the NMI handler to become
idle before resetting Econet state) moves from &96B2 (3.40) to &9F57 (3.60).
The code is functionally identical except for the NMI handler target address it
polls — 3.40 polls for &96F2 while 3.60 polls for &96BF (`nmi_rx_scout`),
reflecting the shifted handler address.

### 12. svc5_dispatch moved from adlc_init to page 6

In 3.40, the page 6 relocated code ends with `trampoline_tx_setup` (a
`JMP start_adlc_tx`) and includes a large block of code at &9B35-&9B73 for
VIA interrupt handling and service 5 dispatch, followed by &FF padding.

3.60 reorganises this area significantly:

- The VIA interrupt handler (`handle_cb1_intr`) and `svc5_dispatch` are moved
  into the page 6 relocated code block, executing at runtime &06DA-&06FF.
- `start_adlc_tx` (formerly reached via a JMP trampoline in page 6) is
  relocated into the main ROM area at &9630 and called directly.
- The `trampoline_tx_setup` in page 6 still exists as a JMP at runtime &06CE,
  but `tx_poll_core` now calls `start_adlc_tx` directly rather than via the
  trampoline.

This reorganisation eliminates approximately 60 bytes of code from the
&9B35-&9B7E region, which in 3.40 was occupied by the VIA handler, dispatch
table indexing, and associated data.

### 13. NMI scout handler: interrupt protection added

The NMI scout receive handler (`nmi_scout_rx`) gains PHP/SEI/PLP protection
around critical sections. In 3.40, the handler calls `tube_post_init` (at
runtime &0414) without masking interrupts. In 3.60, PHP/SEI wraps the Tube R4
protocol sequence:

```assembly
    PHP                         ; save interrupt state
    SEI                         ; disable IRQs during R4 handshake
    ...                         ; Tube R4 protocol operations
    PLP                         ; restore interrupt state
```

This appears at two sites: the R4 send at &9377 and the R4 read at &9398.
Additionally, at &9382 a PLP is inserted after the Tube register access,
ensuring interrupts are re-enabled promptly.

The protection prevents IRQs from firing during the Tube R4 handshake, which
requires strict byte-level timing between the host and co-processor. Without
SEI, a VIA timer or keyboard IRQ could delay the handshake long enough for the
Tube ULA to timeout or the co-processor to misinterpret the protocol state.

### 14. prot_flags variable moved from &0D60 to zero page &99

The protection status variable used during Econet operations moves from
absolute address &0D60 (3.40) to zero page &99 (3.60, labelled `prot_flags`).
All references change from 3-byte absolute addressing (LDA &0D60 / STA &0D60 /
EOR &0D60) to 2-byte zero page addressing (LDA &99 / STA &99 / EOR &99).

This saves 1 byte per access (6 references, saving approximately 6 bytes of
ROM) and reduces the access time from 4 cycles to 3 cycles per instruction.

### 15. need_release_tube initialised during adlc_init

3.60 adds `STY need_release_tube` (with Y=0) at &96B9 during ADLC
initialisation, within `adlc_init_workspace`. This ensures the Tube release
flag at &98 is cleared to a known state during startup. 3.40 does not
explicitly initialise this location during ADLC init — it relies on the
zero-page workspace being cleared by the MOS during reset.

### 16. NMI workspace pointer: LDY #&98 removed

Three occurrences of `LDY #&98` in 3.40 (at &970C, &981C, &9832) that reload
the NMI workspace page pointer are removed in 3.60. The Y register already
holds the correct value at these points, making the explicit loads redundant.
This saves 6 bytes.

### 17. scout_complete: Y register initialised

At &9772 in 3.60, `LDY #0` is inserted in `scout_complete` before code that
uses Y as an index. In 3.40, Y was assumed to be zero but could potentially
hold a stale value from earlier code paths.

### 18. nmi_reply_validate restructured

The reply validation path in the NMI handler (`nmi_reply_validate`) is
restructured. In 3.40, the Tube transfer path branches forward to a separate
code block at &9A47 and contains an inline 3-byte JMP at &97F4. In 3.60, the
code is reorganised to use backward branches, reducing the JMP count:

**3.40** (&97E5-&97F4):
```assembly
    LDA &9F                     ; load workspace page
    STA &A7                     ; store for RXCB access
    LDY #0
    STY &A6
    BEQ &97AF                   ; branch to receive loop
    BIT &0D4A                   ; test TX flags
    BVC &97F7                   ; no Tube: skip
    JMP &9A47                   ; Tube: forward to handler
```

**3.60** (&97B3-&97C6):
```assembly
    LDA #0                      ; A=0
    LDY &9F                     ; load workspace page
    BNE &9774                   ; branch back to receive loop
    ...
    BCC &9835                   ; skip forward
    BIT &0D4A                   ; test TX flags
    BVC &97CB                   ; no Tube: skip
```

The forward JMP to &9A47 is eliminated; instead the Tube path falls through
to code at &97C8 in 3.60.

### 19. rx_data_store: BCS range extended

In the NMI data reception handler, a `BCS` at &9E70 (3.40) — which had
limited branch range — is replaced with a 3-instruction sequence in 3.60
(&9E48):

**3.40** (&9E70):
```assembly
    BPL &9E75                   ; skip to tx_poll jump
    JMP &9A2E                   ; Tube: forward to handler
    JMP &9F1A                   ; non-Tube: continue
    LDA &0D4B                   ; fall through
```

**3.60** (&9E48):
```assembly
    LDA &0D4A                   ; load TX flags
    BPL &9EAC                   ; bit 7 clear: skip forward
    JMP &99DB                   ; bit 7 set: handle Tube
```

This improves the branch structure and resolves a potential out-of-range
branch that would have occurred due to code insertions elsewhere.

### 20. nmi_scout_rx polling: BNE replaces JMP

At two sites in the NMI handler, 3-byte JMP instructions are replaced with
2-byte BNE/BEQ branches that are always taken (the preceding code guarantees
the branch condition), saving 1 byte each:

- &9ACE (3.40 `JMP &9AE3`) → &9ABA (3.60 `BNE &9ACE`)
- &9C68 (3.40 `JMP &9C6F`) → &9C0F (3.60 `BEQ &9C15`)
- &9CEC (3.40 `JMP &9D1B`) → &9C8C (3.60 `BNE &9CBA`)

### 21. Developer credits string removed

The 24-byte string `"Brian,Hugo,Jes and Roger"` at &9FC8 (3.40) is removed in
3.60. The space is absorbed into the &FF padding at end of ROM. 3.60 has 75
bytes of &FF padding (&9FB5-&9FFF) compared to 8 bytes (&9FF8-&9FFF) in 3.40.
The additional free space comes from the credits removal plus various code
size reductions throughout the ROM.

### 22. Shifted address operands

As in previous version transitions, code throughout the ROM has shifted address
operands due to the cumulative effect of insertions and deletions. The shifts
are highly non-uniform — ranging from approximately -&90 to +&65 bytes
depending on region — reflecting the scattered nature of the code changes
across the ROM. The 118 structural change blocks and only 4.9% byte-level
identity confirm that nearly every instruction's operand bytes are affected.

## Address map

The address mapping between 3.40 and 3.60 is non-linear, with 118 change
blocks. Key entry point mappings:

| Function              | 3.40    | 3.60    | Offset  |
|-----------------------|---------|---------|---------|
| Language entry        | &80E1   | &80E1   | +0      |
| Service entry         | &80F7   | &80F7   | +0      |
| Init vectors          | &8140   | &8144   | +4      |
| Version string        | &8207   | &820B   | +4      |
| Service dispatch      | &817F   | &8183   | +4      |
| check_escape          | &854D   | &84A1   | -&AC    |
| tx_poll_core          | &8693   | &8603   | -&90    |
| print_file_info       | &8D24   | (inline)| —       |
| print_hex             | &9FE0   | &9F9D   | -&43    |
| adlc_full_reset       | &96D8   | &9F3D   | +&865   |
| adlc_rx_listen        | &96E7   | &9F4C   | +&865   |

Key new subroutines in 3.60:

| Subroutine              | Address |
|-------------------------|---------|
| bgetv_entry             | &8414   |
| check_escape            | &84A1   |
| save_fscv_args_with_ptrs| &8649   |
| save_fscv_args          | &864D   |
| clear_escapable         | &8657   |
| release_tube            | &9A2B   |
| inc_buf_counter_32      | &9A37   |

Relocated code block ROM sources:

| Block        | 3.40   | 3.60   | Runtime       | Size      |
|--------------|--------|--------|---------------|-----------|
| BRK handler  | &931C  | &9321  | &0016-&0076   | 97 bytes  |
| Tube host (pg 4) | &935D  | &9362  | &0400-&04FF   | 254 bytes |
| Tube host (pg 5) | &9456  | &9462  | &0500-&05FF   | 256 bytes |
| Tube host (pg 6) | &9556  | &9562  | &0600-&06FF   | 256 bytes |

The BRK handler block remains at 97 bytes. Page 4 grows from 249 to 254 bytes
(+5), reflecting the new PHP/SEI/PLP interrupt protection sequences. Pages 5
and 6 remain at 256 bytes each, though the page 6 content changes
significantly due to the `svc5_dispatch` relocation (change 12).
