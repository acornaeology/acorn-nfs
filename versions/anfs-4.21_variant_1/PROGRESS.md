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

| Vector | Addr | Status | Notes |
|--------|------|--------|-------|
| FILEV  | &9C22 (4.18) | | reverify in 4.21 |
| ARGSV  | &9EAB (4.18) | | reverify in 4.21 |
| BGETV  | &BB68 (4.18) | | reverify in 4.21 |
| BPUTV  | &BBE7 (4.18) | | reverify in 4.21 |
| GBPBV  | &A14C (4.18) | | reverify in 4.21 |
| FINDV  | &A02F (4.18) | | reverify in 4.21 |
| FSCV   | &8E4B (4.18) | | reverify in 4.21 |

### Island boundaries (subroutines spanning change blocks)

To populate. Start by intersecting subroutine extents with the compare-tool's
opcode-level change blocks.

## Open follow-ups

- ~~`l91f9`~~ DONE — see Print helpers table above. Resolved by recognising
  that the cmd_syntax_table at &91ED is 12 entries in 4.21_v1 (4.18 had 13).
  The ROM-overlapping byte at &91F9 is the entry point of the print-no-spool
  helper, not a table value.
- **`parse_addr_arg` location in 4.21_v1** — the 4.18 routine at &916E is
  UNMAPPED. It may have been moved or restructured. Find it via opcode
  fingerprinting on the multiply-by-10 / hex-prefix logic.
- **`l976A` / `bit_test_ff` overlap** — &9769 and &976A are both &FF and
  both used as `BIT $abs` "set V" targets. They live inside
  `txcb_init_template`. Worth checking which callers prefer which (might
  indicate a subtle distinction, or just historical accident).

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
