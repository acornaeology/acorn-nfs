# ANFS 4.24 annotation progress

4.24 is built on 4.21 (variant 1) — both Master 128, 65C02, HAZEL
workspace, no relocated blocks. 93.9 % opcode-similar. The driver
(`disassemble/disasm_anfs_424.py`) was bootstrapped by `generate_424.py`
(opcode-map of the 4.21 driver + byte-verified interpolation) and then
hand-corrected.

## Status (current)

| Gate | State |
|---|---|
| `fantasm verify` | PASSED — byte-identical 16384 bytes |
| `fantasm lint` | clean |
| `fantasm comments check` | 0 HIGH, 1 benign MEDIUM (range-end `&0D2D`) |
| `fantasm audit undeclared` | 0 |
| Inline-comment density | **100.0 %** (6960 code items) |
| Meaningful-bare data bytes | 40 (vs 48 in 4.21 — ahead of the sibling) |
| Auto-labels / placeholders | 6 residual (index-base overlaps, command-name bytes, ROM-tail &FF padding — all banner-covered) |

## Done

- Version scaffold, `rom.json`, `fantasm.toml` + `acornaeology.json`
  registration, CI matrix entry.
- Generator + byte-verified interpolation (no stale comment can smear
  onto an operand-changed instruction).
- Four PHA/PHA/RTS dispatch tables re-based from each dispatcher's
  operand (service `&8A23/&8A56`, OSWORD-13 `&A9C8/&A9DA`, NETV
  `&AD40/&AD49`, extended-vector table `&8ECD`).
- Command table (`_cmd_table_fs_entries`) re-mapped across the `+&14 /
  +&19` split around the new `*HELP` sub-table entry.
- Restructured regions re-annotated: credits easter-egg (now
  `jsr print_inline`), `print_fs_address`/`print_ps_address` shared
  tail, immediate-op handlers, the CLD guards, the ACCCON buffer-store
  guard, `tx_calc_transfer` (relocated `&8900`→`&85AD`, + shadow branch).
- 24 stale operand comments and 100 stale address references fixed
  (all `comments check` HIGH findings resolved).
- All JSR targets declared.
- `CHANGES-FROM-4.21.md` written.

## Done (this session, continued)

1. **100 % inline-comment coverage.** All 6960 code items commented — the
   ~270 changed-region gaps were annotated (argsv pointer/extent compare,
   cmd_pollps status display, help-table walker, PS/workspace flags, boot
   library lookup, register/branch gaps). 38 comments carried verbatim
   from 4.21 by structural (mnemonic+mode) alignment; the rest written
   from the 4.24 code.
2. **Jump tables + EQUBs.** All PHA/PHA/RTS dispatch tables named and
   banner'd (incl. the previously auto-labelled svc/OSWORD-13/NETV LO-HI
   bases). cdir threshold table, OSWORD claim-code table and net-error
   codes completed; the new `*HELP` `On` matcher entry (`&A80E`,
   dispatch `&8E45`) explained. Remaining bare data (40 bytes) is at/below
   4.21's own bar — the same field-continuation bytes 4.21 leaves bare.
3. **Structural labels.** 30 of 36 auto-labels/placeholders named
   (dispatch bases, poll-status labels, OSARGS compare labels, TX
   interrupt gates, printer/spool error paths, `nmi_return_inton`).

## Remaining (minor)

1. **6 residual auto-labels** — `sub_c8492`/`l8494` (imm-op dispatch
   operand-overlap), `c85b9`/`sub_c85c0` (tube-address index bases),
   `la76f`/`la88a` (command-name data bytes), `sub_cbff8` (ROM-tail &FF
   padding). All are intentional data-adjacent artifacts covered by
   banners/aliases; forcing names would misrepresent them.
2. **Description/calling-convention review.** Optional deeper sweep of
   `on_entry`/`on_exit` on the newly-declared subs (as 4.21 Phases A/L
   did) — not required for parity.

## Tooling notes

- dasmos 4.0.0 / fantasm 0.18.0 repo-wide. Operand overrides use the
  `dasmos.expr` DSL (`sym`/`lo`/`hi`); every memory-map entry carries a
  `group=` and each rom.json a `memory_map_groups` legend (dasmos#43).
- `generate_424.py` and the interpolation are a one-shot bootstrap; the
  driver is now the source of truth (do not regenerate — it would drop
  the hand corrections above).
