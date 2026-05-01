# ANFS 4.21 (variant 1) — Annotation Progress

Tracking review and reannotation of the 4.18-derived baseline against the actual
4.21_v1 ROM. Each chunk should be small enough to commit independently.

## Current state

| Metric | Value (initial) | Value (now) |
|---|---|---|
| Verify | byte-identical | byte-identical |
| Lint | clean | clean |
| Active subroutines | 283 | 304 |
| Active labels | 1274 | 1281 |
| Active comments | 6596 | 6539 |
| UNMAPPED subs | 56 | 39 |
| Opcode similarity vs 4.18 | 85.6% | (unchanged) |

Net: 21 routines named, ~57 stale carry-over comments removed, 7
labels added.

## Strategy

1. **Inwards from entry points** — service handler, language entry, vector
   handlers, NMI/IRQ. These are the canonical anchors.
2. **Outwards from islands** — subroutines that fell entirely within an
   LCS-equal region carry over reliably; verify their boundaries, then walk
   their callees.
3. **CFG-driven walk** — use `fantasm cfg sub <ver> <name>`
   to find callees/callers. Mark each routine reviewed in the table below.
4. **Small chunks, frequent commits.** Stop at natural boundaries.

## Tools

- `fantasm asm extract <ver> <addr> [end]` — assembly listing for a region
- `fantasm asm extract 4.18 <addr>` and `fantasm asm extract 4.21_variant_1 <addr>` — side-by-side
- `fantasm cfg sub <ver> <name>` — caller/callee graph for a routine
- `fantasm audit detail <ver> <addr|name>` — full report on a routine
- `fantasm compare 4.18 4.21_variant_1 > /tmp/cmp.txt` — equal/replace/insert regions

## Review log

Status legend: ✅ verified accurate, 🔧 fixed, ⚠️ partial, ❌ replaced/gone.

### Entry points

| Addr | Name | Status | Notes |
|------|------|--------|-------|
| &8003 | service_entry (JMP) | | trampoline only |
| &8A54 | service_handler | 🔧 | done; description rewritten for Master-only Bad ROM rejection; 8 inline comments updated, 4 added |
| &4342 | language_entry | | check ROM header |

### Print helpers

| Addr | Name | Status | Notes |
|------|------|--------|-------|
| &91F9 | print_newline_no_spool | 🔧 | renamed from auto `l91f9`; OSBYTE 199 closes/restores spool around CR via OSASCI |
| &91FB | print_char_no_spool    | 🔧 | renamed from auto `c91fb`; A->OSASCI, BIT &9769 forces V=1 |
| &9201 | print_byte_no_spool    | 🔧 | renamed from auto `sub_c9201`; A->OSWRCH (raw), CLV forces V=0 |
| &9769 | always_set_v_byte      | 🔧 | named the &FF byte used by 21 BIT-test callers to set V |
| &9203 | save_regs_for_print_no_spool | 🔧 | shared body label |
| &921D | do_print_no_spool      | 🔧 | OSASCI/OSWRCH branch point |
| &9227 | print_via_oswrch       | 🔧 | OSWRCH branch label |
| &922A | restore_spool_and_return | 🔧 | epilogue label |

### Vector handlers (filing-system)

Master 128 mechanism: ANFS installs &FF1B/&FF1E/.../&FF2D in the
&0212-&021F vector slots (table at &8EA7), then plants its real
handlers in the per-ROM extended vector table at &0D9F+ via
write_vector_entry, reading from the lo/hi/pad table at &8EB5.

| Vector | 4.18 addr | 4.21_v1 addr | Status | Notes |
|--------|-----------|--------------|--------|-------|
| FILEV  | &9935 | &9C22 | | LCS-mapped; carry-over comments to verify |
| ARGSV  | &9BBE | &9EAB | | LCS-mapped |
| BGETV  | &B7CE | &BB68 | | LCS-mapped |
| BPUTV  | &B84D | &BBE7 | | LCS-mapped |
| GBPBV  | &9E2F | &A14C | | LCS-mapped |
| FINDV  | &9D4E | &A02F | | LCS-mapped |
| FSCV   | &8E33 | &8E4B | | LCS-mapped |
| (table) | &8E61/&8E6F | &8EA7/&8EB5 | 🔧 | dispatch+handler tables fully annotated |

### Island boundaries (subroutines spanning change blocks)

To populate. Start by intersecting subroutine extents with the compare-tool's
opcode-level change blocks.

## Open follow-ups

- ~~`l91f9`~~ DONE — see Print helpers table above.
- ~~`parse_addr_arg` location~~ DONE — relocated to &92B2.
- ~~filing-system vector handlers~~ DONE — table at &8EA7/&8EB5.
- **`l976A` / `bit_test_ff` overlap** — &9769 and &976A are both &FF and
  both used as `BIT $abs` "set V" targets. They live inside
  `txcb_init_template`. Worth checking which callers prefer which (might
  indicate a subtle distinction, or just historical accident).

## Recovered subroutines (so far)

Used `fantasm.api.fingerprint` to locate routines that LCS mapping had
abandoned. Each is verified by spot-checking the prologue opcodes
against 4.18.

| 4.18 addr | 4.21_v1 addr | Name | Notes |
|-----------|--------------|------|-------|
| &8B0D | &8B45 | svc_18_fs_select | ratio 1.00, exact match |
| &A4EE | &A83B | svc_8_osword | ratio 0.95; replaced stale `byte()` |
| &8D17 | &8D24 | check_credits_easter_egg | shifted by 3 bytes |
| &A673 | &A9DD | osword_13_set_station | BIT/BPL prologue removed |
| &B799 | &BB38 | process_all_fcbs | 9-byte workspace save (CHANGES §5) |
| &8D79 | &8D91 | cmd_iam | TYA/PHA prologue removed |
| &9327 | &9463 | copy_fs_cmd_name | uses 65C12 PHY |
| &AD10 | &B0A0 | cmd_cdir | shifted by 1 (RTS terminator) |
| &916E | &92B2 | parse_addr_arg | direct manual fingerprint |
| &AF32 | &B2CF | mask_owner_access | workspace moved &1071->&C271 |
| &8E8C | &8ED2 | osbyte_x0_y0 | LDX #0 / LDY #0 / BEQ |
| &8E83 | &8EC9 | osbyte_x0 | LDX #0 then falls into osbyte_yff |
| &8CB9 | &8CAD | get_ws_page | found via JSR-following from caller |
| &8FF1 | &90C7 | print_station_id | found via 'Econet Station' string |
| &A0A7 | &A3C4 | parse_fs_ps_args | uses 65C12 PHX/PHY |
| &A660 | &A9CC | osword_13_read_station | OSWORD &13 sub 0 |
| &A734 | &AAC2 | osword_13_read_handles | OSWORD &13 sub 6 |
| &A744 | &AAD0 | osword_13_set_handles | OSWORD &13 sub 7 |

## Deferred candidates (false positives or harder)

| 4.18 addr | Tried | Issue |
|-----------|-------|-------|
| &A744 osword_13_set_handles | &AAC7 | prologue diverged; entry may be earlier |
| &88F2 tx_calc_transfer | &8910 | code rewritten, body opcodes differ |
| &A9B0 osword_4_handler | &AD30 | first opcode differs (LDA vs TSX) |
| &9570 check_escape | &984D | completely different code |
| &8AA0 read_paged_rom | &8AB4 | completely different code |
| &8FF1 print_station_id | &908D | different code (no inline string) |
| &8028 svc5_irq_check | &BBD6 | low ratio (0.43) |
| Various cmd_* | various | low confidence |

## Related analysis

- `docs/analysis/anfs-421-variant-naming.md` — why this ROM is named
  "variant 1" (host-OS gate at &8A61 rejects OS 5.0 / Master Compact;
  the natural sibling would be a Compact build).

## Findings — to fold into CHANGES-FROM-4.18.md eventually

### service_handler (&8A54) — Master-only Bad ROM check
- 4.18: skips workspace setup for OS 1.20 (X=1) or OS 2.00 (X=2).
- 4.21_v1: skips workspace setup for OS 3.2/3.5 (X=3) or OS 4.0 (X=4) i.e.
  Master 128 / Master Econet Terminal. On any other OS it prints
  `"Bad ROM "<rom-number>` and clears the workspace byte at &02A0+slot,
  rejecting the ROM. Even OS 5.0 (Master Compact) is rejected — likely why
  this is "variant 1" (presumably another variant supports Compact).
- 4.21_v1 uses 65C12 `phy / ply` in place of 4.18's `tya / pha / pla / tay`.

### OSWORD &13: auto-select FS instead of abort
- 4.18: each OSWORD &13 sub-handler (read_station / set_station /
  read_handles / set_handles) inlined a `BIT &0D6C / BPL <return>`
  check at the prologue. If ANFS was NOT the active FS (bit 7 clear),
  the handler aborted by returning zero in PB[0] without touching FS
  state.
- 4.21_v1: the check is factored into `ensure_fs_selected` at &8B4D
  with INVERTED behaviour: `BIT fs_flags / BMI return / fall through
  to JSR cmd_net_fs / BEQ ok / JMP error_net_checksum`. If the FS is
  not active, it AUTO-SELECTS by calling cmd_net_fs and raises a
  'net checksum' error on selection failure — instead of silently
  aborting.
- This is an observable behaviour change for software using OSWORD
  &13: a previously safe "query if FS is active" call now triggers
  a selection attempt.

### Master 128 workspace migration
- ANFS 4.18 used MOS RAM pages &0Dxx-&10xx for filing-system state.
- ANFS 4.21_v1 moves the same data into the Master 128 sideways-RAM
  workspace at &C000-&C2FF. Visible in many recovered routines:
  - `mask_owner_access`: writes &C271 instead of &1071
  - `parse_fs_ps_args`: stores result in &B7 instead of &B6
  - `copy_fs_cmd_name`: writes TX buffer at &C105 instead of &0F05

### 65C12 instruction adoption
- Several recovered routines use 65C12 (Master CMOS) instructions
  in place of NMOS 6502 idioms:
  - `print_no_spool` family: PHY/PLY/PHX/PLX, BRA, STZ, BIT abs,X
  - `parse_addr_arg` and `parse_fs_ps_args`: PHX/PHY in place of
    TXA/PHA, TYA/PHA
  - `copy_fs_cmd_name`: PHY in place of TYA/PHA
  - `service_handler`: PHY/PLY in place of TYA/PHA, PLA/TAY
- Net effect: tighter prologues, freeing space for the new code.

(Add additional findings as they emerge, with an eye to grouping them by
theme for the eventual CHANGES doc.)
