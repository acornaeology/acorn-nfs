# Changes from ANFS 4.18 to ANFS 4.21 (variant 1)

ANFS 4.21 (variant 1) is the first ANFS for Acorn's BBC Master 128
series. The two 16 KB sideways ROMs share 86.7 % of their opcode
structure but the 4.21 variant 1 build is 65C02-aware, drops the
page 4-6 relocated workspace in favour of HAZEL hidden RAM at &C000-&C2FF, and gates
the service-call handler with a Master-only OS-version check.

The "variant 1" suffix reflects that this build refuses to install on
anything other than a Master 128 (or Master Econet Terminal): a later
variant 2 build, byte-identical except for an extra OS-version branch
in the gate, exists for the Compact.

## Summary statistics

| Metric                          | Value         |
|---------------------------------|---------------|
| ROM size                        | 16384 bytes   |
| Identical bytes at same offset  | 285 (1.7 %)   |
| Byte-level similarity           | 75.8 %        |
| Opcode-level similarity         | 86.7 %        |
| Full instruction similarity     | 69.0 %        |
| Instructions (4.18 / 4.21)      | 8189 / 8270   |
| Structural change blocks        | 234           |
| Subroutines (4.18 / 4.21)       | 326 / 454     |

The low identical-byte count (1.7 %) reflects the +5-byte ROM-title
shift cascading through almost every opcode operand, plus the
relocation of every workspace access from `&0Dxx-&10xx` (4.18) to
`&C0xx-&C2xx` (4.21). The opcode-level similarity (86.7 %) is the
meaningful structural measure: roughly one instruction in seven has
been substantively changed.

## ROM header

| Field             | 4.18                | 4.21 variant 1      |
|-------------------|---------------------|---------------------|
| Service entry     | &8A15               | &8A54               |
| ROM type          | &82                 | &82                 |
| Copyright offset  | &19                 | &19                 |
| Binary version    | &04                 | &04                 |
| Title             | "Acorn ANFS 4.18"   | "Acorn ANFS 4.21"   |
| Copyright         | "(C)1985 Acorn"     | "(C)1986 Acorn"     |

## Changes

### 1. Master 128 Bad-ROM gate at the service handler

The most visible structural change. The service handler at &8A54 (was
&8A15 in 4.18) now begins with an OSBYTE 0 OS-version check:

| OS version returned          | Action                          |
|------------------------------|---------------------------------|
| 3.x (Master 128 MOS)         | proceed with service dispatch   |
| 4.0 (Master Econet Terminal) | proceed                         |
| anything else                | silently return unclaimed       |

The gate explicitly rejects OS 1.00, 1.20, 2.00 (BBC B / B+) and OS
5.0 (Master Compact). Pre-Master OSes lack the CMOS RAM that 4.21
uses to store station and protection state, so a "soft" failure is
preferable to running and corrupting workspace.

4.18 had no equivalent gate -- its service handler dispatched
directly. The "variant 1" naming captures that this build is not
universal across the Master series.

### 2. CPU upgrade to 65C02 with R65C02 extensions

The Master 128 ships with Rockwell's R65C02 (the GTE65SC02 silicon
variant on later units behaves identically for the opcodes ANFS uses).
The driver loads with `load(addr, file, "65c02")`; beebasm assembles
under `CPU 1`.

65C12 / R65C02 instructions adopted throughout:

- `PHX` / `PHY` / `PLX` / `PLY` (replacing `TXA` / `PHA` / `TYA` /
  `PHA` push/pop sequences). Saves 2 cycles per push/pop pair.
- `BRA` for unconditional branches inside routines (saves 1 byte vs
  `JMP abs`).
- `STZ abs` / `STZ zp` for clearing single bytes (replaces `LDA #0` /
  `STA <addr>`).
- `BIT abs,X` for indexed BIT tests in dispatch tails.
- `TSB` / `TRB` for atomic bit-set / bit-reset operations on memory
  -- used in the Master shadow-VIA path (see change 6).

Routines visibly rewritten with 65C12 prologues include
`copy_fs_cmd_name` (&9463), `parse_fs_ps_args` (&A3C4), and
`help_wrap_if_serial` (around &8C29).

### 3. Workspace migration from MOS RAM to HAZEL hidden RAM

4.18 used MOS RAM pages &0E.. &10 for its filing-system workspace
(parse buffer, TX buffer base, FS lib flags, FCB attributes, saved
catalogue buffer). 4.21 moves the entire workspace to HAZEL -- the
Master 128's 8 KB hidden-RAM region at `&C000-&DFFF`, paged over
the MOS VDU drivers when ACCCON bit Y is set. ANFS occupies the
first 768 bytes of HAZEL (`&C000-&C2FF`); HAZEL's documented
upper limit for filing-system static workspace is `page &DB`, so
the choice of `&C8` as ANFS's claim base leaves room for other
filing-system claimants.

| Workspace data         | 4.18    | 4.21 variant 1 |
|------------------------|---------|----------------|
| Parse buffer           | `&0E30` | `&C030`        |
| TX buffer base         | `&0F00` | `&C100`        |
| FS lib flags           | `&1071` | `&C271`        |
| FCB attributes         | `&10C9` | `&C2C9`        |
| Saved catalogue buffer | `&10D9` | `&C2D9`        |

The +&B200 offset is uniform: 4.18's `&0Dxx-&10xx` range maps to
4.21's `&BFxx-&C2xx`. The migration removes the entire page-copy
loop that 4.18 used to set up the relocated blocks (formerly around
&BE94); 4.21 has no equivalent code in that region.

### 4. svc5_irq_check rewritten around the Master deferred-work flag

`svc5_irq_check` lives at the same address `&8028` in both ROMs but
the body is completely different.

4.18 (`svc5_irq_check`, runtime &8028):

```
    LDA &FE4D            ; VIA IFR
    AND #&02             ; Bit 1: shift register IRQ
    BEQ no_sr_irq        ; Not us
    ...                  ; Service the SR completion
```

4.21 (`svc5_irq_check`, runtime &8028):

```
    LDY &0D65            ; Master deferred-work flag
    BEQ no_deferred      ; Nothing pending
    TRB ACCCON           ; Clear bit 7 of &FE34 (shadow-RAM enable)
    STZ &0D65            ; Consume the deferred flag
    BMI dispatch_svc5    ; Y had bit 7 set on entry: PHA/PHA/RTS dispatch
    LDA #&FE             ; Otherwise fire Econet RX event &FE
    JSR generate_event
    JMP tx_done_exit
```

The 4.18 SR-IRQ handling is gone; the new mechanism uses a Master-
specific workspace flag at `&0D65` set by IRQ and NMI paths and
consumed here during deferred service. As a side effect, the 4.18
`set_jsr_protection` prologue at &805D (which protected the SVC5
dispatch via shadow-VIA state) is gone too -- no JMP-protection
mechanism is needed in the new design. The shared `&0D68 / &0D69`
shadow-pair body that fed JSR-protection now lives at `setup_sr_tx`
(&8512) for an unrelated TX-prep purpose.

The `&27` Master service call ("Reset has occurred") that runs
`nfs_init_body` after a hard reset uses this same flag-passing
discipline: ANFS uses the post-reset call specifically to claim
NMIs for Econet receive handling, since the Master MOS no longer
offers workspace on a soft BREAK.

### 5. OSWORD &13 sub-handlers auto-select the FS

4.21's OSWORD &13 sub-handlers all begin with a `JSR ensure_fs_selected`
(&8B4D) prologue. `ensure_fs_selected` tests bit 7 of `fs_flags`
(`&0D6C`); if clear, it calls `cmd_net_fs` to AUTO-SELECT ANFS as the
active filing system. On selection failure it raises a 'net checksum'
error (`&AA`).

4.18's equivalent handlers inlined `BIT &0D6C / BPL <return>` and
returned a zero in `PB[0]` if the FS was inactive -- a quiet failure.
4.21's behaviour is louder but more robust: client code that uses
OSWORD &13 will reliably get either real data or a clean error,
not silent zeroes.

### 6. setup_sr_tx via shadow VIA pair

Master MOS owns the System VIA's auxiliary control register and shift
register; ANFS can't touch them directly without fighting MOS. 4.21
introduces a shadow pair at workspace bytes `&0D68` (mirror of ACR)
and `&0D69` (mirror of SR), updated by `setup_sr_tx` (&8512). The
shadow is flushed into the live VIA inside the Master's IRQ dispatch
path. 4.18 wrote `system_via_acr` / `system_via_sr` directly.

### 7. Protection state moved to CMOS RAM

4.18's `cmd_prot` / `cmd_unprot` (4.18 &B30C / &B33D) parsed attribute
keywords (`L`, `W`, `R`, etc.) and accumulated the protection bits
into a workspace mask at `ws_0d68 / ws_0d69`.

4.21's `cmd_prot` (&B6D2) and `cmd_unprot` (&B6D6) take **no
arguments**. They just toggle bit 6 of CMOS RAM byte `&11` (the
Econet station-flags byte) via OSBYTE `&A1` (read CMOS) and OSBYTE
`&A2` (write CMOS), mirroring the new value into the shadow ACR/IER
pair through `set_via_shadow_pair`.

Because the state lives in CMOS, protection now survives BREAK and
power-cycle without ANFS having to manage persistence. The keyword
parser and the per-keyword bit-encoding table that fed it in 4.18 are
gone.

### 8. Star commands removed in 4.21

The Master MOS handles `*CLOSE`, `*PRINT`, and `*TYPE` natively, so
the ANFS ROM no longer wraps them. Removed entries:

- `cmd_close` (4.18 wrapper for OSFIND close)
- `cmd_print` (4.18 wrapper)
- `cmd_type` (4.18 wrapper)

The strings "Close", "Print", "Type" do not appear anywhere in the
4.21 ROM.

`cmd_table_nfs` shrinks correspondingly. The 4.21 utility sub-table
also drops `*Close`-adjacent entries; the freed bytes contribute to
the space budget for the new Bad-ROM gate and CMOS handlers.

### 9. *RUN argument with `&` prefix is URD-relative

The 4.21 cmd_run handler splits into two entries:

- `check_urd_prefix` at &8E2D -- tests first arg char for `&`
- `cmd_run_via_urd` at &8E35 / &A4F1 -- the URD-prefixed entry

If the first arg char is `&`, control JMPs to `cmd_run_via_urd`,
which clears `fs_lib_flags` bit 1 before parsing the rest (so the
file is looked up relative to the user's URD, not the current LIB).
Otherwise control falls through to `pass_send_cmd` for normal
FS-command dispatch.

4.18's `check_escape` (&9570) bundled its escape-flag BIT-test prologue
and the escape-acknowledge action; 4.21 splits them apart. Each call
site now does its own BIT-test against the FS-options / escapable
flag, then JSRs `raise_escape_error` (&9895) on hit. The action half
emits OSBYTE &7E and tail-jumps to `classify_reply_error` with `A=6`.

### 10. svc_2_private_workspace split

4.18's `svc_2_private_workspace` (around &8EB8) bundled the
workspace-allocation prologue and the ANFS bring-up sequence in a
single body. 4.21 splits them:

- `svc_2_private_workspace_pages` (&8F10) -- pages allocation
- `nfs_init_body` (&8F38) -- bring-up

The latter is reachable in 4.21 only via PHA/PHA/RTS dispatch (as
table[22] in `svc_dispatch_lo / svc_dispatch_hi`); no static call
exists.

### 11. svc_dispatch table relocated and re-keyed

The PHA/PHA/RTS service dispatch table moved:

- Lo half: `&89CA` (4.18) -> `&89ED` (4.21)
- Hi half: `&89EF` (4.18) -> `&8A20` (4.21)

The +&23/&31 shift comes from the longer ROM title plus the inserted
Bad-ROM gate code. The table content also gained six new dispatch
slots for OSWORD-style sub-handlers, language reply 2 (palette/VDU
state), and the help-suffix matcher; see the 4.21 `svc_dispatch_lo`
declaration in the driver for the full mapping.

`fs_vector_table` similarly shifts from 4.18's `&8E6F` to 4.21's
`&8EB5` (`&8E9A + &1B`, the offset that the dispatcher's
`svc_dispatch_lo_offset+&1B` indexed-access uses).

### 12. Other dispatch-table layout shifts

| Table                     | 4.18    | 4.21    | Notes                |
|---------------------------|---------|---------|----------------------|
| `imm_op_dispatch_lo`      | &8488   | &848B   | +3-byte shift        |
| `tx_done_dispatch_lo`     | &853E   | &853B   | -3-byte shift        |
| `tx_ctrl_dispatch_lo`     | &8681   | &867E   | -3-byte shift        |
| `tx_ctrl_machine_type`    | &8689   | &8686   | -3-byte shift        |

For each, the dispatcher operand uses an `expr_label` of the form
`<table_label>-<base_offset>` so renames flow through cleanly.

### 13. dir_op_dispatch Y value

`dir_op_dispatch` at &8E5B sets `Y=&18` (was `&0E` in 4.18). The
indices reachable through this dispatch path therefore shift from
the old 15..19 range to the new 25..29 range (language replies 0-4).

### 14. read_paged_rom uses LDX &028D directly

4.21 reads the current ROM number at `&028D` inline rather than via
OSBYTE `&FD`. Same optimisation 4.18 made vs 4.08.53 for the break-
type read; here applied to the ROM-number read in a couple more sites.

The 4.18 `read_paged_rom` helper (4.18 &8AA0) is removed entirely --
no `JMP &FFB9` (osrdsc) instruction appears anywhere in the 4.21 ROM.

### 15. Address-mapping table (recovered routines)

| Routine                       | 4.18         | 4.21 variant 1 | Notes                              |
|-------------------------------|--------------|----------------|------------------------------------|
| `svc5_irq_check`              | &8028        | &8028          | rewritten body (see #4)            |
| `tx_done_jsr`                 | &8543        | &8540          | -3 byte shift                      |
| `tx_calc_transfer`            | &88F2        | &8900          |                                    |
| `get_ws_page`                 | &8CB9        | &8CAD          | body extends with ROL/PHP/ROR/PLP  |
| `issue_svc_15`                | &8D17        | &8D24          |                                    |
| `osbyte_x0_y0`                | &8E8C        | &8ED2          | same body                          |
| `osbyte_x0`                   | &8E83        | &8EC9          | same body                          |
| `svc_2_private_workspace_pages` | &8EB8 (part) | &8F10        | split (see #10)                    |
| `nfs_init_body`               | &8EB8 (part) | &8F38          | split (see #10)                    |
| `print_station_id`            | &8FF1        | &90C7          |                                    |
| `copy_fs_cmd_name`            | &9327        | &9463          | 65C12 PHY                          |
| `read_filename_char` (TX buf) | &0F05        | &C105          | workspace migrated (see #3)        |
| `parse_fs_ps_args`            | &A0A7        | &A3C4          | 65C12 PHX/PHY                      |
| `osword_13_read_station`      | &A660        | &A9CC          |                                    |
| `osword_13_set_station`       | &A673        | &A9DA          | FS-active gate factored out (#5)   |
| `osword_13_read_handles`      | &A734        | &AAC2          |                                    |
| `osword_13_set_handles`       | &A744        | &AAD0          |                                    |
| `svc_8_osword`                | &A4EE        | &A83B          |                                    |
| `ensure_fs_selected`          | &8B0D        | &8B45          |                                    |
| `mask_owner_access`           | &AF32        | &B2CF          | `fs_lib_flags` migrated (see #3)   |
| `process_all_fcbs`            | &B799        | &BB38          | rewritten -- uses `fs_options` + `fs_block_offset` |
| `svc_18_fs_select` related    | &AD10        | &B0A0          |                                    |
| `cmd_prot`                    | &B30C        | &B6D2          | reduced to CMOS toggle (see #7)    |
| `cmd_unprot`                  | &B33D        | &B6D6          | reduced to CMOS toggle (see #7)    |

### 16. ROM-tail workspace shift

In 4.18 the relocated blocks for pages 4 / 5 / 6 lived at:

- `&BF00` (page 4)
- `&BC90` (page 5)
- `&BD90` (page 6)

4.21 has none of these. The bytes at the end of the 4.21 ROM
(`&BFC0..&BFFF`) are a small stub plus 33 bytes of `&FF` padding
plus three labels (`hazel_minus_1a` at `&BFE6`, `hazel_minus_2`
at `&BFFE`, `hazel_minus_1` at `&BFFF`) used as **indexing
bases for accesses into HAZEL**. The trick: HAZEL begins at
`&C000`, so an indexed instruction like `STA hazel_minus_2,Y`
with Y ≥ 2 lands at `&BFFE + Y ≥ &C000` -- inside HAZEL.
Routines like `loop_copy_fs_ctx` (9 bytes at `&C000..&C007`),
`osword_13_set_station` (2 bytes at `&C000..&C001`), and
`loop_copy_ws_to_pb` (3 bytes at `&C002..&C004`) all use this
pattern to copy small blocks between HAZEL and other buffers
without burning a separate zero-page pointer for the HAZEL base
address. Each loop's `CPY`/`BNE` guard stops Y before it would
land inside the ROM tail. See the `rom_tail_padding` and
`hazel_idx_bases` banners in the 4.21 driver for the full
mapping.

## Annotation / structural notes

### svc_dispatch / fs_vector_table converted to symbolic equb pairs

The 4.21 disassembly emits the lo/hi halves of the service-call
dispatch table as `equb <(target-1)` / `equb >(target-1)` rather than
raw bytes, and `fs_vector_table` as `equw label` rather than raw
addresses. All target labels appear inline in the per-entry comments;
renames flow through cleanly.

### `osbyte_a1` is dual-use code + table base

The 5 bytes at `&8E9A` (`A9 A1 4C F4 FF` = `LDA #&A1 / JMP OSBYTE`)
are the routine's body AND the leading slot of a vector-dispatch
read accessed via `LDA c8e9a,Y`. The driver expresses this with
`expr_label` so the code, the table, and `osbyte_a1`'s callers all
stay consistent under renaming.

### print_inline_no_spool needed a stringhi_hook

The *SPOOL-bypassing variant of `print_inline` at `&928A` follows the
same inline-string + high-bit-terminator + resume-on-terminator
contract as `print_inline` (`&9261`) but lacked the
`hook_subroutine(0x928A, "print_inline_no_spool", stringhi_hook)`
declaration in the early 4.21 driver. Without it, py8dis stopped
tracing past every `JSR &928A` site, leaving the resume code
byte-classified across roughly two dozen sites. Adding the hook
recovered ~96 code items in a single change.

## Open issues

- **O-1**: the dispatch path that reaches `nfs_init_body` (`&8F38`)
  is verified at the table level (svc_dispatch_lo[22] / hi[22] both
  decode to that address) but no static `JSR` / `JMP` / branch to
  `&8F38` exists in the disassembled code. The dispatch is
  presumably triggered by an OS-event-driven `JMP svc_dispatch` with
  the right `Y`, but the trigger site has not been identified.

- **O-2..O-4**: minor stale-label survivals in the dispatch area
  (the 'Service 1' inline at `&8A8F`, `dir_op_dispatch`'s `Y=&0E`
  vs `&18` description). Tracked in `OPEN-ISSUES.md`.
