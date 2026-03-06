# Changes from NFS 3.65 to ANFS 4.08.53

ANFS 4.08.53 (Advanced Network Filing System) is the successor to NFS 3.65, the
final release of Acorn's original NFS. The ROM doubles from 8 KB (&8000-&9FFF) to
16 KB (&8000-&BFFF), adding extensive new functionality including a full filing
system client, multi-platform OS support, and a vastly expanded star command set.
This document does not catalogue every new feature; instead it focuses on changes
to the Econet protocol stack and other code inherited from NFS 3.65 — bug fixes,
robustness improvements, and architectural refinements.

The Econet protocol stack (NFS &965E-&9FD1 → ANFS &8025-&89BC) is the dominant
shared region, containing approximately 2,300 bytes of opcode-matched code across
48 blocks. The Tube host pages 4 and 5 are byte-identical; page 6 is 74% matched;
the zero-page BRK handler block is 70% matched.

## Summary statistics

| Metric                     | Value                                     |
|----------------------------|-------------------------------------------|
| NFS 3.65 ROM size          | 8192 bytes                                |
| ANFS 4.08.53 ROM size      | 16384 bytes                               |
| Main ROM opcode match      | 26.8% (1087 of 4053 NFS opcodes, 48 blocks) |
| Page 4 match               | 100% (124 opcodes)                        |
| Page 5 match               | 100% (118 opcodes)                        |
| Page 6 match               | 74.2% (98 of 132 opcodes, 3 blocks)       |
| Zero-page block match      | 69.6% (32 of 46 opcodes)                  |

## ROM header

| Field             | NFS 3.65       | ANFS 4.08.53      |
|-------------------|----------------|-------------------|
| Language entry    | &80DD (JMP)    | Data bytes        |
| Service entry     | &80F3          | &8A0B             |
| ROM type          | &82            | &82               |
| Binary version    | &03            | &04               |
| Title             | "NET"          | "Acorn ANFS"      |
| Copyright         | "(C)ROFF"      | "(C)1985 Acorn"   |

ANFS is a pure service ROM with no language entry point. NFS 3.65 had both a
language JMP at &8000 and a service entry at &80F3, allowing it to be entered
as a language ROM during network boot.

## Changes

### 1. Error messages: station addresses in network errors

The most user-visible improvement. NFS 3.65 reports network errors as bare
strings — "Not listening", "No reply" — with no indication of which station
was involved. ANFS builds compound error messages that include the destination
station address as a decimal "net.station" suffix.

NFS 3.65 error messages:

| Code | Message         |
|------|-----------------|
| &A0  | "Line Jammed"   |
| &A1  | "Net Error"     |
| &A2  | "Not listening"  |
| &A3  | "No Clock"      |
| &11  | "Escape"        |
| &CB  | "Bad Option"    |
| &A5  | "No reply"      |

ANFS 4.08.53 error messages:

| Code | Message                            |
|------|------------------------------------|
| &A0  | "Line jammed"                      |
| &A1  | "Net error"                        |
| &A2  | "Station N.S not listening"        |
| &A2  | "Station N.S not present"          |
| &A3  | "No clock"                         |
| &11  | "Escape"                           |
| &CB  | "Bad option"                       |
| &A5  | "No reply from station N.S"        |

The new `classify_reply_error` subroutine at &9638 handles this. For error
class 2 (station errors), it copies the base "Station" string, appends the
decimal station address via `append_drv_dot_num`, then selects a suffix
based on the processor V flag:

```
.classify_reply_error
    bit bit_test_ff          ; Set V flag
.mask_error_class
    and #7                   ; Mask to error class (0-7)
    pha                      ; Save error class
    cmp #2                   ; Class 2 (station error)?
    bne build_simple_error   ; No: simple error path
    ...
    jsr append_drv_dot_num   ; Append ' net.station'
    plp                      ; Restore V flag
    bvs suffix_not_listening ; V set: ' not listening'
    ...                      ; V clear: ' not present'
```

The V flag distinguishes the error source: V is set on entry to
`classify_reply_error` (from the TX layer, where the remote station actively
refused), selecting "not listening". When the error comes via `mask_error_class`
with V explicitly cleared (from the reply handler, where no response was
received), "not present" is selected instead.

The `append_drv_dot_num` subroutine (&9738) formats station addresses as
decimal strings with leading-zero suppression. For local-network stations,
only the station number is shown; for inter-network addresses, the network
number and a dot separator are prepended.

The "No reply" message similarly gains a station suffix, becoming
"No reply from station N.S" via `build_no_reply_error` at &9604.

### 2. Error message capitalisation

All error strings are normalised to sentence case:

| NFS 3.65         | ANFS 4.08.53       |
|------------------|--------------------|
| "Line Jammed"    | "Line jammed"      |
| "Net Error"      | "Net error"        |
| "Not listening"  | (see above)        |
| "No Clock"       | "No clock"         |
| "Bad Option"     | "Bad option"       |
| "No reply"       | "No reply from..." |

This aligns with Acorn's standard MOS error message style.

### 3. check_escape: explicit error class

NFS 3.65's `check_escape` acknowledges the escape condition via OSBYTE &7E,
then jumps to `nlisne` which masks the low 3 bits of A to select the error
message. This works because OSBYTE &7E returns A=&7E, and &7E AND &07 = 6,
which indexes the "Escape" entry. But the error class is an implicit side
effect of the OSBYTE return value — a fragile dependency.

NFS 3.65 (&848F):
```
.check_escape
    lda escape_flag          ; Read escape flag
    and escapable            ; Mask with escapable flag
    bpl return_remote_cmd    ; No escape: return
    lda #&7E                 ; OSBYTE &7E: acknowledge escape
    jsr osbyte
    jmp nlisne               ; A=&7E from OSBYTE, AND #7 = 6 = Escape
```

ANFS 4.08.53 (&955A):
```
.check_escape
    lda escape_flag          ; Read escape flag
    and escapable            ; Mask with escapable flag
    bpl return_from_recv_reply
.raise_escape_error
    lda #&7E                 ; OSBYTE &7E: acknowledge escape
    jsr osbyte
    lda #6                   ; Error class 6: Escape (explicit)
    jmp classify_reply_error
```

ANFS loads A=6 explicitly before calling the error classifier, removing the
dependency on the OSBYTE return value.

### 4. Conditional error code logging

NFS 3.65 stores every network error code unconditionally into the FS workspace.
ANFS adds a guard: `cond_save_error_code` (&95FB) tests bit 7 of `fs_flags`
(&0D6C) and only writes to `fs_last_error` (&0E09) when the filing system is
actually selected:

```
.cond_save_error_code
    bit fs_flags             ; Test FS selected flag
    bpl return               ; Bit 7 clear: skip save
    sta fs_last_error        ; Save error code
    rts
```

This prevents network errors from corrupting FS error state when ANFS is not
the active filing system — relevant in multi-ROM configurations where Econet
may be handling traffic for other services.

### 5. Spool/exec closure on network errors

NFS 3.65 closes spool and exec files on errors only in the BGET/BPUT path.
ANFS centralises this in `handle_net_error` (&96E8), which is called from
the shared error dispatch path `check_net_error_code` (&96DA). When a network
error occurs, it checks whether the error code matches the current spool
(OSBYTE &C6) or exec (OSBYTE &C7) file handle, and closes the matching file:

```
.handle_net_error
    sta net_context          ; Save error code
    ...
    lda #&c6                 ; OSBYTE &C6: read spool handle
    jsr osbyte_x0
    cpy fs_load_addr         ; Compare with error handle
    beq close_exec_file      ; Match: close exec
    cpx fs_load_addr         ; Compare X result
    bne done_close_files     ; No match: skip
```

This ensures that spool/exec files are properly closed for any network error,
not just those occurring during explicit BGET/BPUT calls.

### 6. NMI claim guard in adlc_init

NFS 3.65's `adlc_init` issues OSBYTE &8F with X=&0C (NMI claim service
request) and unconditionally falls through to initialise the NMI workspace,
regardless of whether another ROM has claimed the NMI.

NFS 3.65 (&96AF-&96B8):
```
    lda #&8f                 ; OSBYTE &8F: issue service request
    ldx #&0c                 ; X=&0C: NMI claim service
    ldy #&ff
.adlc_init_workspace
    jsr osbyte               ; Issue service call
.init_nmi_workspace          ; Falls through unconditionally
    ldy #&20                 ; Copy NMI shim...
```

ANFS 4.08.53 (&807C-&8089):
```
    lda #&8f                 ; OSBYTE &8F: issue service request
    ldx #&0c                 ; X=&0C: NMI claim service
    jsr osbyte_yff
    ldy #5                   ; Y=5: NMI claim service number
.econet_restore
    cpy #5                   ; Was Y changed by another ROM?
    bne adlc_init_done       ; Yes: another ROM claimed NMI, skip init
.init_nmi_workspace
    ldy #&20                 ; Copy NMI shim...
```

After the service call returns, ANFS checks whether Y was modified (indicating
another ROM claimed the NMI). If so, it skips the NMI workspace initialisation
entirely. This prevents ANFS from overwriting another ROM's NMI handler — a
correctness issue on machines with multiple Econet-aware ROMs.

### 7. Self-modifying NMI shim removed

The most architecturally significant change to the protocol stack. NFS 3.65
introduced a self-modifying NMI disable mechanism (in `CHANGES-FROM-3.62.md`,
section "Self-modifying INTOFF mechanism"): a byte at &0D1C within the NMI
dispatch shim at &0D00 is toggled between `BIT` (&2C, NMI enabled) and `RTI`
(&40, NMI disabled) opcodes. Writing &40 causes the NMI handler to return
immediately; writing &2C allows it to proceed.

NFS 3.65 `test_inactive_retry` (&9BFF):
```
.test_inactive_retry
    php                      ; Save interrupt state
    sei                      ; Disable interrupts
    lda #&40                 ; A=&40: RTI opcode (disable NMI)
    sta l0d1c                ; Self-modify NMI shim: disable
.intoff_test_inactive
    bit &FE18                ; INTOFF
    ...
    lda #&2c                 ; A=&2C: BIT opcode (re-enable NMI)
    sta l0d1c                ; Self-modify NMI shim: enable
.inactive_retry
    bit &FE20                ; INTON
```

ANFS replaces all self-modifying writes with a double INTOFF — two consecutive
`BIT &FE18` reads:

ANFS 4.08.53 `test_inactive_retry` (&85F3):
```
.test_inactive_retry
    php                      ; Save interrupt state
    sei                      ; Disable interrupts
.intoff_test_inactive
    bit &FE18                ; INTOFF: disable NMIs
    bit &FE18                ; INTOFF again (belt-and-braces)
.test_line_idle
    bit &FEA1                ; Test SR2 for INACTIVE
    beq inactive_retry       ; Not idle: re-enable and retry
    ...
.inactive_retry
    bit &FE20                ; INTON: re-enable NMIs
```

The double INTOFF eliminates a potential race condition: if an NMI fires
between the `STA l0d1c` write and the `BIT &FE18` read, the self-modifying
code approach could leave the NMI shim in an inconsistent state. The hardware
INTOFF is atomic — each `BIT &FE18` read clears the NMI enable latch in the
Econet hardware. Two reads ensure the latch is cleared even if the first read
coincides with an incoming NMI edge.

This pattern is applied consistently across all locations where NFS 3.65 used
self-modification:
- `test_inactive_retry` / `inactive_retry` (INACTIVE polling loop)
- `tx_prepare` (NMI re-enable after TX setup)
- `wait_idle_and_reset` → `save_econet_state` (NMI release)

The `l0d1c` workspace byte and all `STA l0d1c` / `LDA #&2C` / `LDA #&40`
sequences are absent from ANFS.

### 8. tx_calc_transfer: Tube/IO address detection widened

NFS 3.65's `tx_calc_transfer` checks whether the buffer address is in Tube
space by ANDing bytes 6 and 7 of the RXCB and comparing the result to &FF.
This only detects addresses where both bytes are &FF — i.e. the &FFFFxxxx
range.

NFS 3.65 (&9EFD):
```
.tx_calc_transfer
    ldy #6                   ; RXCB[6]
    lda (port_ws_offset),y
    iny                      ; RXCB[7]
    and (port_ws_offset),y   ; AND bytes 6 and 7
    cmp #&ff                 ; Both &FF?
    beq fallback_calc_transfer
```

ANFS 4.08.53 (&88E8):
```
.tx_calc_transfer
    ldy #7                   ; RXCB[7] (high byte first)
    lda (port_ws_offset),y
    cmp #&ff                 ; High byte = &FF?
    bne check_tx_in_progress ; No: normal buffer
    dey                      ; RXCB[6]
    lda (port_ws_offset),y
    cmp #&fe                 ; Byte 6 >= &FE?
    bcs fallback_calc_transfer ; Yes: I/O or Tube address
```

The ANFS version checks RXCB[7] for &FF first, then tests whether RXCB[6]
is &FE or above. This correctly identifies both &FExxxxxx (BBC I/O space,
including the Tube registers at &FEE0-&FEE7 and memory-mapped I/O) and
&FFxxxxxx (Tube host address space). The NFS 3.65 AND-based test would miss
&FExx addresses entirely, potentially causing incorrect transfer size
calculations for I/O-page operations.

### 9. tx_op_type initialised during workspace init

NFS 3.65's `init_nmi_workspace` does not initialise the `tx_op_type` byte
at &0D65, leaving it with whatever value was in RAM. ANFS explicitly clears
it:

ANFS `init_nmi_workspace` (&8089):
```
    ...
    sty tx_src_net           ; Clear source network (Y=0)
    sty need_release_tube    ; Clear Tube release flag
    sty tx_op_type           ; Clear TX operation type (Y=0)
    ...
```

The Y register is zero after the NMI shim copy loop, so this costs only two
bytes (STY absolute). Without this initialisation, stale values in `tx_op_type`
could affect the first TX operation after Econet initialisation.

### 10. OS version detection in service handler

ANFS adds OS version detection via OSBYTE 0, adjusting its workspace addressing
for different BBC Micro variants. NFS 3.65 assumes a single machine type
(BBC Model B) throughout. The ANFS service 15 handler reads the OS version and
stores it for later use, enabling ANFS to run correctly on:

- BBC Model B (OS 1.x) — original hardware
- BBC B+ (OS 2.x) — different memory layout
- Master 128 (OS 3.x) — shadow RAM, different paging
- Master Compact (OS 5.x) — further paging changes

This cross-platform support is new to ANFS; NFS was exclusively a BBC Model B
ROM.

### 11. Page 6 relocated code: VDU stream relay replaces trampolines

NFS 3.65's page 6 tail (&06CE-&06FF) contains 29 bytes of &FF padding
followed by four JMP trampolines that dispatch to the main ROM code:

```
; NFS 3.65 page 6 (&06CE-&06FF)
    EQUB &FF, &FF, ...      ; 29 bytes &FF padding
.trampoline_tx_setup
    JMP tx_begin             ; &06EB
.trampoline_adlc_init
    JMP adlc_init            ; &06EE
.svc_12_nmi_release
    JMP wait_idle_and_reset  ; &06F1
.svc_11_nmi_claim
    JMP init_nmi_workspace   ; &06F4
    LDA #4                   ; SR interrupt test
    BIT &FE4D
```

ANFS replaces this entirely with `tube_vdu_dispatch` — a VDU stream relay
handler for the Tube co-processor. This code handles service call &FE (Tube
initialisation) from the relocated page, including character definition
explosion (OSBYTE &14), an R1 data stream read loop, and EVNTV/BRKV vector
setup:

```
; ANFS 4.08.53 page 6 (&06CE-&06FF)
    CMP #&FE                 ; VDU stream start?
    BCC tube_vdu_normal_byte ; Below &FE: normal byte
    BNE setup_tube_vectors   ; &FF: set up vectors
    CPY #0                   ; &FE: check Y parameter
    BEQ tube_vdu_normal_byte
    LDX #6                   ; Explode 6 extra pages
    LDA #&14                 ; OSBYTE &14: explode chars
    JSR osbyte
.loop_poll_r1_vdu
    BIT &FEE0                ; Poll R1 status
    BPL loop_poll_r1_vdu     ; Not ready: keep polling
    LDA &FEE1                ; Read byte from R1
    BEQ tube_vdu_stream_end  ; Zero: end of stream
    JSR oswrch               ; Write character
    JMP loop_poll_r1_vdu     ; Next byte
.setup_tube_vectors
    LDA #&AD                 ; Set EVNTV to &06AD
    STA &0220
    ...
```

The NFS trampolines are no longer needed because ANFS calls the main ROM
subroutines directly from its service handler dispatch table.

### 12. Zero-page relocated block reduced

The zero-page relocated block (BRK handler and workspace) shrinks from 97
bytes (&0016-&0076) in NFS 3.65 to 66 bytes (&0016-&0057) in ANFS. The
content within the shared address range is byte-identical. The reduction
reflects removal of some workspace variables that ANFS handles differently.

### 13. Workspace layout reorganisation

Several workspace bytes in the &0D60-&0D6F range are repurposed:

| Address | NFS 3.65           | ANFS 4.08.53       |
|---------|--------------------|---------------------|
| &0D60   | (not named)        | ws_0d60 (TX done)   |
| &0D62   | tx_clear_flag      | ws_0d62 (Econet init)|
| &0D63   | (not used)         | tube_present        |
| &0D64   | rx_flags           | (not used)          |
| &0D65   | (not named)        | tx_op_type          |
| &0D66   | econet_init_flag   | (not used)          |
| &0D67   | tube_flag          | (not used)          |
| &0D6C   | (not used)         | fs_flags            |
| &0D6D   | (not used)         | net_context         |

ANFS also introduces new workspace variables for bridge status, TX retry
counts, TX timeout values, and filing system context save areas that have no
NFS equivalents.

### 14. Protection system removed

NFS 3.65 implements a per-station access control system for immediate
operations (PEEK, POKE, HALT, JSR, OSProc) via `prot_flags` and
`saved_jsr_mask`. The `clear_jsr_protection` subroutine manages this state.
ANFS removes the protection system entirely — the `clear_jsr_protection`
subroutine is absent, `prot_flags` is not used, and the protection mask
checking code in the immediate operation handlers is removed. ANFS still
handles PEEK, POKE, HALT and other immediate operations, but without the
per-station access control layer.

### 15. Double INTOFF in save_econet_state

NFS 3.65's NMI release path uses the self-modifying shim to disable NMIs
before clearing state:

NFS 3.65 `wait_idle_and_reset` (&9F9D):
```
    lda #&40                 ; RTI opcode
    sta l0d1c                ; Disable NMI via self-mod
.save_econet_state
    bit &FE18                ; INTOFF
    lda #0
    sta tx_clear_flag
    sta econet_init_flag
```

ANFS replaces this with two hardware INTOFF reads, consistent with the
self-modifying code removal throughout the protocol stack:

ANFS 4.08.53 `save_econet_state` (&898C):
```
.save_econet_state
    bit &FE18                ; INTOFF: disable NMIs
    bit &FE18                ; INTOFF again (belt-and-braces)
    sta ws_0d60              ; TX not in progress
    sta ws_0d62              ; Econet not initialised
    ldy #5
    jmp adlc_rx_listen       ; Enter RX listen mode
```

## Matched subroutine address map

Key subroutines matched by opcode-level comparison, grouped by functional
area. Addresses are in the main ROM unless noted.

### ADLC init/reset

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &969A    | &8069        | adlc_init                       |
| &96B8    | &8089        | init_nmi_workspace              |
| &9F70    | &895F        | adlc_full_reset                 |
| &9F7F    | &896E        | adlc_rx_listen                  |

### NMI scout handling

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &96DF    | &80B3        | nmi_rx_scout                    |
| &96FC    | &80D0        | RX scout second byte handler    |
| &971E    | &80F2        | Scout error/discard handler     |
| &972E    | &8102        | Scout data reading loop         |
| &9758    | &812C        | Scout completion handler        |

### Data RX

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &9808    | &81DC        | Data frame RX handler           |
| &983D    | &8211        | Install data RX bulk handler    |
| &9865    | &8239        | Data frame bulk read loop       |
| &9899    | &826D        | Data frame completion           |

### TX system

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &9B90    | &8582        | tx_begin                        |
| &9BF8    | &85EA        | inactive_poll                   |
| &9C5D    | &8643        | tx_prepare                      |
| &9CFF    | &86E0        | nmi_tx_data                     |
| &9D3B    | &871C        | TX_LAST_DATA and frame complete |
| &9EFD    | &88E8        | tx_calc_transfer                |

### Reply/handshake

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &9D63    | &8744        | RX reply scout handler          |
| &9DD6    | &87B7        | TX scout ACK                    |
| &9E83    | &886E        | Four-way handshake RX switch    |
| &9E8F    | &887A        | RX final ACK handler            |

### Utility

| NFS 3.65 | ANFS 4.08.53 | Subroutine                      |
|----------|--------------|---------------------------------|
| &9F8A    | &8979        | wait_idle_and_reset             |
| &9FA2    | &898C        | save_econet_state               |
| &9FB2    | &899D        | nmi_bootstrap_entry             |
| &9FC0    | &89AB        | rom_set_nmi_vector              |

### Relocated code (unchanged)

| NFS 3.65 | ANFS 4.08.53 | Subroutine (runtime address)    |
|----------|--------------|---------------------------------|
| &0016    | &0016        | Tube BRK handler [zp]           |
| &0400    | &0400        | Tube host page 4 entry          |
| &0500    | &0500        | Tube host page 5 entry          |
| &06C5    | &06C5        | Read byte from Tube R2 [p6]     |

## Relocated code blocks

| Block    | NFS 3.65 source | ANFS source | Runtime | Size (NFS / ANFS) |
|----------|-----------------|-------------|---------|-------------------|
| ZP/BRK   | &9324           | &BEBF       | &0016   | 97 / 66 bytes     |
| Page 4   | &9365           | &BF00       | &0400   | 256 / 256 bytes   |
| Page 5   | &9465           | &BC90       | &0500   | 256 / 256 bytes   |
| Page 6   | &9565           | &BD90       | &0600   | 256 / 256 bytes   |

The ANFS ROM source addresses for the relocated blocks are non-contiguous
(&BEBF, &BF00, &BC90, &BD90), unlike NFS 3.65 where they are packed
sequentially from &9324. Pages 4 and 5 are byte-identical between versions.
