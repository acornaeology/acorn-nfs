# Changes from ANFS 4.08.53 to ANFS 4.18

ANFS 4.18 is the last version of Acorn's Advanced Network Filing System for the
BBC Model B and B+ series; subsequent ANFS releases target the Master series.
The two 16 KB ROMs are 95.6% identical at the opcode level, with 148 structural
change blocks. The changes include several bug fixes to Tube co-processor
support and filing system workspace handling, a restructured network receive
control block, and small optimisations throughout.

## Summary statistics

| Metric                          | Value        |
|---------------------------------|--------------|
| ROM size                        | 16384 bytes  |
| Identical bytes at same offset  | 577 (3.5%)   |
| Byte-level similarity           | 90.1%        |
| Opcode-level similarity         | 95.6%        |
| Full instruction similarity     | 83.6%        |
| Instructions (4.08.53 / 4.18)   | 8190 / 8189  |
| Structural change blocks        | 148          |
| Subroutines (4.08.53 / 4.18)    | 274 / 283    |

The low identical-byte count (3.5%) is misleading: the 5-byte longer ROM title
shifts all subsequent addresses, causing operand differences throughout even
where the opcodes are unchanged. The opcode-level similarity (95.6%) is the
meaningful measure.

## ROM header

| Field             | 4.08.53          | 4.18                |
|-------------------|------------------|---------------------|
| Service entry     | &8A0B            | &8A15               |
| ROM type          | &82              | &82                 |
| Copyright offset  | &14              | &19                 |
| Binary version    | &04              | &04                 |
| Title             | "Acorn ANFS"     | "Acorn ANFS 4.18"   |
| Copyright         | "(C)1985 Acorn"  | "(C)1985 Acorn"     |

The title grew from 10 to 15 characters, adding the version number. This is
the root cause of the +5 address shift that propagates through the ROM.

## Changes

### 1. Tube ROM transfer: interrupts disabled during page sends

The most significant bug fix. During Tube co-processor startup, the host
copies the ROM image to the parasite one page at a time via the R3 data
register. The byte transfer loop is timing-sensitive — three NOP instructions
provide the minimum delay between consecutive writes to &FEE5.

4.08.53 (`next_rom_page`, runtime &04A2):
```
.next_rom_page
    LDA #7                ; R4 cmd 7: SENDW
    JSR tube_claim_default
    LDY #0
.send_rom_page_bytes
    LDA (zp_ptr_lo),Y
    STA tube_data_register_3
    NOP / NOP / NOP       ; Timing delay
    INY
    BNE send_rom_page_bytes
    INC tube_xfer_page    ; Next page
```

4.18 (`next_rom_page`, runtime &049D):
```
    PHP                   ; Save interrupt state
    SEI                   ; Disable interrupts
.next_rom_page
    LDA #7                ; R4 cmd 7: SENDW
    JSR tube_claim_default
    LDY #0
.send_rom_page_bytes
    LDA (zp_ptr_lo),Y
    STA tube_data_register_3
    NOP / NOP / NOP       ; Timing delay
    INY
    BNE send_rom_page_bytes
    PLP                   ; Restore interrupts between pages
    INC tube_xfer_page    ; Next page
```

In 4.08.53, an interrupt firing during the 256-byte transfer could disrupt
the NOP timing or clobber the Tube data register state, potentially corrupting
the co-processor ROM image. 4.18 wraps each page transfer in a PHP/SEI...PLP
bracket. Interrupts are briefly re-enabled between pages (PLP restores the
original state), so the system remains responsive during multi-page transfers
while each individual page copy is atomic.

### 2. OSBYTE &FD replaced by direct LDX &028D

The Tube startup path reads the last break type to distinguish soft breaks
(re-initialise) from hard breaks (full ROM transfer).

4.08.53 (`check_break_type`, runtime &048C):
```
    LDX #0
    LDY #&FF
    LDA #&FD              ; OSBYTE &FD: read last break type
    JSR OSBYTE
    TXA                   ; Result in X
    BEQ tube_sendw_complete
```

4.18 (`check_break_type`, runtime &048C):
```
    LDX last_break_type   ; Direct read from &028D
    BEQ tube_sendw_complete
```

The OS stores the last break type at &028D. Reading it directly saves 3 bytes
and ~50 cycles (the OSBYTE dispatch overhead), recovering space in the
tight 256-byte page 4 relocated block. The page 4 block shrinks from 256 to
252 bytes as a result of this and other savings.

### 3. Event dispatch via EVNTV vector

4.08.53 fires the Econet receive event by loading the event number in Y and
jumping to `tx_done_fire_event`, which calls OSEVEN (&FFBF).

4.08.53 (`svc5_irq_check`, &804D):
```
    LDY #&FE              ; Y=&FE: Econet receive event
    JMP tx_done_fire_event
```

4.18 (`svc5_irq_check`, &8052):
```
    LDA #&FE              ; A=&FE: Econet receive event
    JSR generate_event    ; JMP (EVNTV)
    JMP tx_done_exit
```

The new `generate_event` subroutine at &805A is a single `JMP (EVNTV)`,
dispatching the event directly through the event vector at &0220 rather
than via the OS entry point. The event number moves from Y to A, matching
the EVNTV calling convention. This allows third-party software that hooks
EVNTV to intercept Econet events without also intercepting the OS dispatch
layer.

### 4. OSWORD workspace preservation

4.08.53's `svc_8_osword` handler copies OSWORD parameters from the MOS
parameter block at &00ED directly into the NFS workspace at `svc_state`
(&00A9) without saving the original contents. If an OSWORD arrived during
an in-progress filing system operation, the workspace was silently corrupted.

4.18 (`svc_8_osword`, &A4EE):
```
    LDY #6
.loop_save
    LDA svc_state,Y       ; Save current workspace byte
    PHA
    LDA l00ED,Y           ; Copy OSWORD parameter
    STA svc_state,Y
    DEY
    BNE loop_save
    JSR osword_setup_handler
    LDY #&FA              ; Restore 6 workspace bytes
.loop_restore
    PLA
    STA lFFB0,Y
    INY
    BNE loop_restore
```

The 4.18 version saves 6 bytes of workspace on the stack before overwriting
them with OSWORD parameters, and restores them after the handler returns.
This prevents re-entrant OSWORD processing from corrupting filing system
state during multi-block file transfers.

### 5. process_all_fcbs: extended workspace preservation

4.08.53's `process_all_fcbs` saves only `fs_options` and `fs_block_offset`
(2 workspace bytes) before scanning all 16 FCB slots and calling
`start_wipe_pass` for each:

```
    LDA fs_options        ; Save 2 bytes
    PHA
    LDA fs_block_offset
    PHA
```

4.18 saves 9 contiguous workspace bytes (&FFB4-&FFBC) via a loop:

```
    LDX #&F7              ; Save 9 workspace bytes
.loop
    LDA lFFBD,X
    PHA
    INX
    BMI loop
```

If `start_wipe_pass` modified workspace variables beyond `fs_options` and
`fs_block_offset` — such as `fs_crc_lo`, `fs_load_addr`, or `fs_cmd_csd` —
those changes would leak into subsequent FCB iterations. The 4.18 version
preserves all 9 bytes, preventing cross-FCB workspace corruption during
batch operations like `*BYE`.

### 6. Receive control block layout restructured

The network receive control block (RXCB) layout changed. Several offsets
used to access fields within the RXCB shifted:

| Field                  | 4.08.53 offset | 4.18 offset |
|------------------------|----------------|-------------|
| Channel attribute      | &0E            | &0A         |
| Workspace page count   | &0F            | &0B         |
| RX flag                | &05            | &01         |
| Remote flag (*ROFF)    | &04            | &00         |

In 4.08.53, the channel attribute field at offset &0E is accessed inline
(`LDY #&0E / LDA (net_rx_ptr),Y`) at 14 locations across the ROM. In 4.18,
these are factored into two helper subroutines:

- `read_rx_attribute` (&B98A): `LDY #&0A / LDA (net_rx_ptr),Y / RTS`
- `store_rx_attribute` (&B98F): `LDY #&0A / STA (net_rx_ptr),Y / RTS`

The helpers are called 4 times (read) and 10 times (store), saving ~20 bytes
overall compared to inline access, and centralising the offset value so that
future layout changes require only two edits.

### 7. OSWORD parameter block pointer: &F0/&F1 to &AC/&AD

The zero page pointer used by OSWORD 13 sub-handlers to access the parameter
block changed from &F0/&F1 (`osword_pb_ptr`) to &AC/&AD (`ws_ptr_hi`). This
affects 28 of 31 parameter block references across the OSWORD handlers.

Zero page locations &F0/&F1 are used by the MOS for OSWORD parameter passing.
Modifying them during OSWORD processing risks conflicts with the MOS or other
ROMs that use &F0/&F1 during interrupts. By using &AC/&AD, which is in the
filing system's own workspace range, 4.18 avoids potential pointer corruption
in nested or re-entrant scenarios.

### 8. Receive reply flag preservation

In the multi-block file transfer routine `recv_and_update`, 4.08.53 calls
`recv_and_process_reply` directly. The reply processing can modify the
processor flags, but the subsequent `SEC / JSR adjust_fsopts_4bytes` depends
on the carry flag being set for correct subtraction.

4.18 interposes a new wrapper, `recv_reply_preserve_flags` (&9F67):
```
.recv_reply_preserve_flags
    PHP                   ; Save flags before reply processing
    JSR recv_and_process_reply
    PLP                   ; Restore flags after reply processing
    RTS
```

This ensures the caller's carry flag survives across the reply handler,
preventing incorrect address adjustment calculations during multi-block
LOAD/SAVE operations.

### 9. Filename trailing space trimming

4.08.53's `copy_arg_validated` copies command line characters verbatim until
it hits a CR terminator. If the user types `*DIR mydir ` (with trailing
spaces), the spaces are sent to the file server as part of the directory name.

4.18 adds a trimming loop after the copy:
```
.loop_trim
    LDA fs_cmd_csd,X      ; Load end of buffer
    EOR #&20              ; Test for space
    BNE done_trim         ; Not a space: done
    DEX                   ; Back up
    LDA #&0D              ; CR terminator
    STA fs_cmd_lib,X      ; Replace trailing space with CR
    BNE loop_trim         ; Trim next character back
```

This strips trailing spaces from filenames before they are sent to the
file server, fixing commands with accidental trailing whitespace.

### 10. '&' prefix handled on unrecognised star commands

In ANFS, the `&` prefix on filenames means "resolve relative to the User Root
Directory (URD) rather than the Current Selected Directory (CSD)". When
`parse_access_prefix` encounters a leading `&`, it strips the character
and sets bit 6 of `fs_lib_flags`. Later, when `save_net_tx_cb` builds the
packet for the file server, it checks bit 6 and substitutes the URD handle
into the CSD handle slot of the command header. The file server then resolves
the path relative to the user's root directory.

Commands like `*RUN` already handle the `&` prefix via `parse_access_prefix`.
However, in 4.08.53, unrecognised star commands (FSCV code 3) are forwarded
to the file server without prefix parsing. If a user types `*&myfile`
(intending to run `myfile` from the user root directory), the raw `&myfile`
string is sent to the file server, which does not understand the `&` prefix
and returns an error.

4.18 adds a check on this path:

```
.check_urd_prefix
    LDY #0
    LDA (fs_crc_lo),Y     ; Load first character of command
    CMP #&26              ; Is it '&'?
    BNE pass_send_cmd     ; No: forward to file server
    JMP fscv_2_star_run   ; Yes: divert to *RUN handler
```

Commands beginning with `&` are diverted to `fscv_2_star_run`, which calls
`parse_access_prefix` to strip the prefix and set the URD flag before
opening and running the file.

### 11. FCB flush factored and optimised

4.08.53 contains ~80 bytes of inline code in `done_find_write_fcb` to save
context, flush the FCB byte count to the file server, and restore context.
4.18 extracts this into two subroutines:

- `flush_fcb_with_init` (&B8E4): full context save, flush, and restore
- `flush_fcb_if_station_known` (&B8DA): wrapper that checks if the FCB
  already has a known station, skipping the context save when it does

The factoring saves ~70 bytes in `done_find_write_fcb` (replaced by a single
`JSR flush_fcb_with_init`) and the station-known shortcut avoids an
unnecessary context save/restore cycle during heavy file I/O, where the
station number is typically cached after the first write.

### 12. Redundant SEC removed

In the callback event handler, 4.08.53 has an explicit `SEC` before a
subtraction loop that counts RXCB slots:

```
    ROR A                 ; Shift bit 0 into carry
    BCC discard_reset_rx  ; Bit 0 clear: skip
    SEC                   ; Set carry for subtraction
    LDA port_ws_offset
.loop_count_rxcb_slot
    INY
    SBC #&0C
    BCS loop_count_rxcb_slot
```

The SEC is redundant: if `BCC` was not taken, carry is already set. 4.18
removes it, saving 1 byte.

### 13. check_data_loss: scanning direction and pending flag preservation

4.08.53 scans FCB status bytes from slot &0F downward using `DEX / BPL`.
4.18 reverses the direction, scanning from negative offset &F0 upward:

```
    PHP                   ; Save pending operation flag
    BNE check_data_loss
    ...
.check_data_loss
    LDX #&F0              ; Start from negative offset
.loop_scan_channels
    ORA l0FC8,X           ; Address &0FC8+&F0 = &10B8
    INX
    BMI loop_scan_channels
    STX fs_eof_flags      ; Clear pending marker
```

The `PHP` before the branch preserves the pending operation flag (Z status)
across the data loss check. In 4.08.53, the `LDA fs_eof_flags` result was
consumed by the `BNE` without being preserved, and the value could be
overwritten by the channel scan. After the scan, `STX fs_eof_flags` clears
the pending marker, preventing the data loss check from retriggering on the
next bye attempt.

### 14. Dead code removed

The unreferenced subroutine `unused_clear_ws_78` (&B42F in 4.08.53), a
10-byte routine that cleared 120 bytes of workspace, is removed. It had
been superseded by `loop_zero_workspace` which clears a full 256-byte page.

### 15. Small refactorings

Three small subroutines were extracted from inline code to save space:

- `prompt_yn` (&B431): prints "Y/N) " via inline string, called from
  `cmd_wipe` (2 sites)
- `print_hex_and_space` (&BB03): prints a hex byte followed by a space,
  called from `cmd_dump` and `print_dump_header` (2 sites)
- `dir_op_dispatch` (&8E43): validates directory operation index and sets
  Y=&0E before falling through to `svc_dispatch`, called from
  `clear_if_station_match` (1 site)
- `store_a_to_pb_1` (&A7FE): stores A to offset 1 of the OSWORD parameter
  block, called from `osword_13_read_prot` and `osword_13_read_rx_flag`

## Relocated code blocks

| Block    | 4.08.53 source | 4.18 source | Runtime | Size (4.08.53 / 4.18) |
|----------|----------------|-------------|---------|----------------------|
| ZP/BRK   | &BEBF          | &BEC3       | &0016   | 66 / 66 bytes        |
| Page 4   | &BF00          | &BF04       | &0400   | 256 / 252 bytes      |
| Page 5   | &BC90          | &BC94       | &0500   | 256 / 256 bytes      |
| Page 6   | &BD90          | &BD94       | &0600   | 256 / 256 bytes      |

All source addresses shift +4 bytes. The zero-page BRK handler block,
page 5 (Tube host code), and page 6 (Econet protocol handlers) are
byte-identical between versions. Page 4 shrinks by 4 bytes due to the
OSBYTE &FD optimisation (change 2); the final 4 runtime bytes &04FC-&04FF
are not initialised by the ROM copy loop.

## Shifted address operands

All code throughout the ROM has shifted address operands due to the 5-byte
title string insertion and cumulative effect of code insertions and
deletions. The shifts are non-uniform, varying by region.
