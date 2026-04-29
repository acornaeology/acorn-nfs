# ANFS 4.21 (variant 1) — Annotation Progress

Tracking review and reannotation of the 4.18-derived baseline against the actual
4.21_v1 ROM. Each chunk should be small enough to commit independently.

## Current state

| Metric | Value |
|---|---|
| Verify | byte-identical (16384 bytes) |
| Lint | clean |
| Active subroutines | 283 |
| Active labels | 1274 |
| Active comments | 6596 |
| UNMAPPED lines | 1933 |
| Opcode similarity vs 4.18 | 85.6% |

UNMAPPED breakdown: 885 comment, 250 label, 56 subroutine, 46 entry, 43 expr,
25 byte, 17 for, 4 rts_code_ptr, 4 move, 3 word.

## Strategy

1. **Inwards from entry points** — service handler, language entry, vector
   handlers, NMI/IRQ. These are the canonical anchors.
2. **Outwards from islands** — subroutines that fell entirely within an
   LCS-equal region carry over reliably; verify their boundaries, then walk
   their callees.
3. **CFG-driven walk** — use `acorn-nfs-disasm-tool cfg <ver> --sub <name>`
   to find callees/callers. Mark each routine reviewed in the table below.
4. **Small chunks, frequent commits.** Stop at natural boundaries.

## Tools

- `extract <ver> <addr> [end]` — assembly listing for a region
- `extract 4.18 <addr>` and `extract 4.21_variant_1 <addr>` — side-by-side
- `cfg <ver> --sub <name>` — caller/callee graph for a routine
- `audit <ver> --sub <addr|name>` — full report on a routine
- `compare 4.18 4.21_variant_1 > /tmp/cmp.txt` — equal/replace/insert regions

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

Used `src/disasm_tools/fingerprint.py` to locate routines that LCS
mapping had abandoned. Each is verified by spot-checking the prologue
opcodes against 4.18.

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

(Add additional findings as they emerge, with an eye to grouping them by
theme for the eventual CHANGES doc.)
