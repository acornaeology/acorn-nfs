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

- **`l91f9` (&91F9)** — JSR'd from `service_handler` (&8A7C) and 2 other
  callers (&8E10, &9D3E). py8dis has classified it as `equb &a9 / equb &0d`
  (i.e. data) but it's clearly an entry point. The 2 raw bytes are
  `LDA #&0D` (load CR), then control falls into `c91fb` which is a number
  parser — that doesn't fit calling it as "print newline". Needs proper
  classification with `entry()` and a name. Investigate at next chunk.

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
