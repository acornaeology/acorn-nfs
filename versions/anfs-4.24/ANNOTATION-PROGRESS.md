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
| Inline-comment density | 96.2 % |

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

## Remaining (future passes, in priority order)

1. **Coverage gaps (~270 code items, → 100 %).** `fantasm context
   uncommented 4.24 --threshold-pct 100 --min-items 1` lists the
   subroutines with gaps. These are inline comments missing in the
   changed regions; ~640 `# UNMAPPED:` lines in the driver mark most of
   them — for each, read the 4.24 instruction and either re-map the
   4.21 comment (if the instruction is unchanged) or write a fresh one.
   Exact-match relocations were already auto-recovered; what remains is
   genuinely-changed code.
2. **36 auto-labels / placeholders.** 29 `l####`/`c####` auto-labels,
   5 `sub_c####`, 2 `loop_c####`. Several are data-adjacent artifacts of
   the restructured dispatch tables (e.g. `sub_c8492`/`l8494` in the
   immediate-op dispatch, `sub_c8a1d`/`l8a23` by the service table) and
   need care; the loop bodies (`loop_cb1e7`, `loop_cb637`) are quick
   semantic renames. Cross-check with `grep -E '^\.[a-z]+_?[a-z]?[0-9a-f]{4}$'`
   on the `.asm` (audit only sees declared subs).
3. **New `*HELP` sub-table entry (~`&A80F`).** The one net-new code
   path; dispatch through `&8E45`. Decode and annotate the entry and its
   handler.
4. **Description/calling-convention review.** Sweep `on_entry`/`on_exit`
   coverage and Markdown/address-link quality (as 4.21 Phases A/L did).

## Tooling notes

- dasmos pinned at 2.0.1; dasmos 4.0.0 exists but fantasm (0.18.0) still
  targets schema v2 — the dasmos-4 migration is deferred repo-wide.
- `generate_424.py` and the interpolation are a one-shot bootstrap; the
  driver is now the source of truth (do not regenerate — it would drop
  the hand corrections above).
