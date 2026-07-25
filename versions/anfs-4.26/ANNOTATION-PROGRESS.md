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

1. **Rewritten OSWORD &0E clock reply routine** at `&A8B2`
   (`save_txcb_and_convert`) and its `bin_to_bcd` helper at `&A924`. In 4.25
   this region was rendered as data with per-byte comments (reached only via
   PHA/PHA/RTS dispatch, so untraceable). Because 4.26 rewrote the bytes, the
   4.25 comments were correctly dropped by the byte-verified interpolation. It
   is re-annotated here as explicit **code** (`d.entry` + `d.subroutine`), which
   decodes cleanly with resolved label references (`save_net_tx_cb`,
   `hazel_txcb_flag`, the reply-buffer store) — higher quality than the 4.25
   data rendering.
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
