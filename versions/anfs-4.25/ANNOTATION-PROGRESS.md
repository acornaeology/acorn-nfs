# ANFS 4.25 annotation progress

4.25 is built on 4.24 — both Master 128, 65C02, HAZEL workspace, no
relocated blocks. **98.2 %** opcode-similar. The driver
(`disassemble/disasm_anfs_425.py`) was bootstrapped by `generate_425.py`
(opcode-map of the 4.24 driver + byte-verified interpolation) and then
hand-corrected. Because 4.25 differs from 4.24 by a single inserted
instruction (`STA svc_state` at `&85AC`) plus the resulting uniform `+2`
shift, almost every 4.24 annotation transfers unchanged; the work was
transfer + shift, with fresh annotation only for the one delta.

## Status (current)

| Gate | State |
|---|---|
| `fantasm verify` | PASSED — byte-identical 16384 bytes |
| `fantasm lint` | clean (driver + `CHANGES-FROM-4.24.md` links) |
| `fantasm comments check` | 0 HIGH, 1 benign MEDIUM (range-end `&0D2D`) |
| `fantasm audit undeclared` | 0 |
| Inline-comment density | **100.0 %** (6961 code items) |
| Subroutines | 464 |
| Auto-labels / placeholders | 17 (the same data-adjacent artifacts 4.24 leaves, shifted `+2`) |

## Structural parity with 4.24 (verified)

Every structural annotation type matches 4.24 exactly, by shift-invariant
signature:

| Element | 4.24 | 4.25 |
|---|---|---|
| Named label / sub / index_base defs | 1423 | 1423 |
| `equw <handler> - 1` dispatch/command words | 26 | 26 |
| `<(..)` / `>(..)` byte expressions | 188 | 188 |
| `char_literal` sites | 99 | 99 |
| `entry()` points | 131 | 131 |
| `equs` strings | 147 | 147 |

Zero 4.24 semantic label, subroutine, dispatch/command-table entry or
byte-expression is missing from 4.25.

## Done

- Version scaffold, `rom.json` (with `memory_map_groups` legend),
  `fantasm.toml` + `acornaeology.json` registration, CI matrix entry.
- `generate_425.py` bootstrap + byte-verified interpolation (no stale
  comment can smear onto an operand-changed instruction).
- The one functional delta annotated: the inserted `STA svc_state` on the
  transmit-done exit path (`&85AC`).
- 51 uniform-shift prose addresses remapped `+2` (`remap_stale_prose_425.py`,
  ROM-space only — workspace addresses left fixed); the one genuine
  operand-value change (boot-filename pointer `#&3E`→`#&40`) corrected.
- 13 change-boundary comments recovered from their 4.24 counterparts.
- 9 semantic labels dropped by the bootstrap (dispatch-table halves,
  `hazel_minus_1/2`, relocated helpers) restored at their true `+2`
  addresses.
- Three PHA/PHA/RTS dispatch loops (svc `&8A25/&8A58`, OSWORD-13
  `&A9CA/&A9DC`, NETV `&AD42/&AD4B`) and the command table + extended-vector
  table (`&8ECF`) restored to structured `equw handler - 1` rendering with
  per-entry comments (`restore_cmd_table_425.py`).
- 11 self-modifying NMI-handler address `d.expr` writes restored.
- All JSR targets declared; 100 % inline-comment coverage.
- `CHANGES-FROM-4.24.md` written and link-validated.

## Corrections found and backported

While transferring annotations, several "resolves-but-wrong" prose
addresses (valid item, wrong instruction — invisible to `comments check`)
surfaced and were fixed in 4.25 **and** backported as far as they occur:

- `print_newline_no_spool` service-handler caller, `set_fs_or_ps_cmos_station`
  record slots, `cmd_nospace` BRA shortcut, `osbyte_a2` end/byte-count,
  `rx_imm_poke`/`rx_imm_exec` data-receive targets — fixed in 4.24 and, where
  they originated, in 4.21 (variant 1).

## Remaining (minor)

1. **17 residual auto-labels** — the same intentional data-adjacent
   artifacts 4.24 leaves (imm-op dispatch operand overlap, tube-address
   index bases, command-name data bytes, ROM-tail `&FF` padding), shifted
   `+2`. All are banner/alias covered.
2. **Inherited 4.24 backlog** — a handful of labels (e.g. `match_on_suffix`,
   the interactive-`*HELP` matcher) are UNMAPPED in 4.24 too; 4.25 holds them
   at parity rather than getting ahead of the sibling.

## Tooling notes

- dasmos 4.1.0 / fantasm 0.18.0. Operand overrides use the `dasmos.expr`
  DSL (`sym`/`lo`/`hi`); every mapped memory-map entry carries a `group=`
  and `rom.json` a `memory_map_groups` legend (dasmos#43). Doc/comment
  links use the `address:` / `label:` / `glossary:` schemes.
- `generate_425.py`, `remap_stale_prose_425.py` and `restore_cmd_table_425.py`
  are one-shot bootstrap tools; the driver is now the source of truth — do
  not regenerate (it would drop the hand corrections above).
