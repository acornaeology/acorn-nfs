# ANFS 4.26 annotation progress

4.26 is built on 4.25 — both Master 128, 65C02, HAZEL workspace, no relocated
blocks. **99.0 % identical at the same byte offset** (no meaningful address
shift; the service entry is unchanged). The driver
(`disassemble/disasm_anfs_426.py`) was bootstrapped by `generate_426.py`
(opcode-map of the 4.25 driver + byte-verified interpolation) and then
hand-finished for the small delta. 4.25 is the pristine parent (0 auto-labels,
comments-check clean), so almost every annotation transferred unchanged.

## Status (current)

| Gate | State |
|---|---|
| `fantasm verify` | PASSED — byte-identical 16384 bytes |
| `fantasm lint` | clean (driver + `CHANGES-FROM-4.25.md` links) |
| `fantasm comments check` | 0 HIGH, 0 MEDIUM |
| `fantasm audit undeclared` | 0 |
| Inline-comment density | **100.0 %** |
| Auto-labels | 0 |
| Structural parity with 4.25 | matches (equw `handler - 1` 26, byte-exprs 188, char_literals 99); the only named-def differences are inside the rewritten OSWORD &0E routine |

## The 4.26 delta (what was hand-finished)

Almost everything transferred from 4.25. The genuine changes:

1. **Reworked OSWORD &0E (14) real-time-clock routine.** The dispatcher
   `osword_0e_dispatch` (`&A89A`), the reader/formatter `save_txcb_and_convert`
   (entry `&A8B1`), the write-back `save_txcb_done` (`&A903`) and the `bin_to_bcd`
   helper (`&A924`). In 4.25 this region was rendered as data with per-byte
   comments (reached only via PHA/PHA/RTS dispatch, so untraceable); 4.26's
   rewrite is re-annotated here as explicit **code** (`d.entry` + `d.subroutine`),
   which decodes cleanly. The *meaning* of the changes — the NetFS filing-system
   guard (`fs_num_via_osargs`), the 20xx-century year math (with the 2100-2107
   limitation), and the corrected `Bad string` error at `&94C0` — was
   cross-checked against **J.G. Harston's "ANFS 4.26 updated OSWORD 14 RTC
   routine"** (linked and credited in `rom.json` and `CHANGES-FROM-4.25.md`);
   each point was confirmed against the actual (byte-identical) 4.26 disassembly.
   Note: the same code-rendering fix was propagated upstream so the routine is
   code in 4.24/4.25 too.
2. **New routine** `fs_num_via_osargs` at `&BFF7`, in the former `&FF` ROM-tail
   padding. Its last bytes anchor the restored `hazel_minus_1`/`hazel_minus_2`
   indexing bases (moved off the padding onto the new code, `fs_num_check`
   anchoring the mid-instruction base).
3. Small edits: the `&94C0` bad-inline error path (immediate error number), and
   the credits punctuation.

## Tooling notes

- dasmos 4.1.0 / fantasm 0.18.0. `generate_426.py` is a one-shot bootstrap; the
  driver is the source of truth — do not regenerate.
- ROM source: 4.26 is **not** in the BBC Micro ROM Library, so `rom.json` links
  J.G. Harston's site (<https://mdfs.net/System/ROMs/Filing/Network/Acorn/>)
  instead of the `?md5=` library link.
