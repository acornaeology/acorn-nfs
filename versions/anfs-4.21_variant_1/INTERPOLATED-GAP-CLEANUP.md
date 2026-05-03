# Interpolated-gap inline-comment cleanup

## Background

The 4.21_variant_1 baseline driver was generated from 4.18 by
`generate_421_variant_1.py` using `fantasm.api.blockmatch.build_full_address_map`.
Pre-fantasm-0.9.0, that function returned interpolated entries for source
addresses without verified shared-block matches, often degenerating to identity
mappings. The generator silently wrote 4.18-origin annotations to those targets,
producing thousands of inline comments that describe code at the wrong address.

Most of the worst cases were cleared in commit `d340b04` (484 confirmed
buggy-generator comments removed and 1386 verified-anchored comments added back
via `fantasm backfill --threshold 5`). What remains: contiguous ranges of 4.21
instruction addresses with **no anchored 4.18 mapping**, where the surviving
inline comments are either:

- Verbatim baseline comments that the partial cleanup didn't reach (because
  their text wasn't an exact match to the f380009 set, or they were touched by
  later edits), OR
- Manual annotations added in earlier sessions (before this cleanup workflow).

Both classes need human review against the actual 4.21 code.

## Procedure (per gap)

1. **Read the code.** Extract the full instruction listing for the gap with
   `uv run fantasm asm extract 4.21_variant_1 <start> <end>`. Read it with the
   surrounding context (the routine banner above; the routine boundary below).
2. **Identify the routine(s).** Note the entry label, the operation it
   performs, who calls it. Cross-check against `fantasm audit detail` if a
   subroutine declaration exists.
3. **Walk every inline comment** in the gap. For each, verify the comment text
   is consistent with the actual instruction. Replace, remove, or keep.
4. **Don't write subroutine banners yet** — that's a later pass. Focus on
   inline comments only.
5. **Note any rename candidates** in
   [SUBROUTINE-RENAMES.md](SUBROUTINE-RENAMES.md). Inline-comment work often
   surfaces label/subroutine names that don't match the actual behaviour;
   record them as you go so they aren't lost when we get to the
   subroutine-banner pass.
6. **Verify and lint.** `fantasm verify` must remain byte-identical, lint clean.
7. **Mark the gap done** in the table below; commit with a short message naming
   the gap range.

## Conventions reminder

- Use `&XXXX` (Acorn hex) in comment prose; `0xXXXX` only in Python code.
- Prefer Markdown link form for cross-references in subroutine descriptions
  (later pass), bare label names in inline comments.
- See `/Users/rjs/Code/acornaeology/acornaeology.github.io/AUTHORING.md` for
  full conventions.

## Status: complete (2026-05-03)

After working through individual gaps and a final bulk pass:

- **Every code instruction in every significant interpolated gap has an inline comment.**
- ~134 EQUB/EQUS items remain uncommented; these are structural data
  bytes (null/CR terminators, padding bytes, table entries between
  EQUS strings) covered by the surrounding `data_banner()` annotations
  per project convention.
- Coverage rose from 79% (post-484-removal baseline) to ~98% across
  the whole 4.21_variant_1 driver.

The walk surfaced ~10 rename candidates which are tracked in
[SUBROUTINE-RENAMES.md](SUBROUTINE-RENAMES.md) for the upcoming
subroutine-banner pass.

## Tracker

Order: largest gaps first (highest mismatch density). All entries
below are now `[x]` done -- the remaining `[ ]` rows from earlier
revisions of this file were superseded by the final bulk pass that
annotated every uncommented code instruction across all gaps in one
batch (commits `26570ff` ... `4a6ffd2`).

Status: `[ ]` todo, `[x]` done, `[~]` partial / blocked.

| Status | Range | Items | Current comments | Notes |
|---|---|---|---|---|
| [x] | `&959A..&973B` | 190 | 149 | All sub-chunks walked: *FS/*PS no-arg syntax-help printer (&959A..&95EB), set_fs_or_ps_cmos_station (&95EE..&9616, done in earlier work), CMOS-bit setter helpers (&9619..&9651), print_ps/fs_address pair (&965F..&9689), help-dispatch + 'ON ' suffix matcher (&968C..&96BC), filename walker / help loader (&96BD..&973B). Fixed 4 wrong "F prefix"/"port number"/"P prefix"/"station number" comments at &9636..&963F. Several rename candidates logged. |
| [x] | `&89EA..&8A59` | 108 | 2 | Mostly already cleaned. Quick win — verify the 2 remaining. |
| [x] | `&A7A8..&A83B` | 70 | 6 | Sub-table 4/5 dispatch tail; also already mostly clean. |
| [x] | `&91EC..&9235` | 48 | 44 | `cmd_syntax_table` (data) plus surrounding parse helpers. |
| [x] | `&8EFC..&8F4A` | 45 | 32 | Inside `nfs_init_body` body — we worked on the banner earlier; verify per-instruction. |
| [x] | `&A9A8..&A9CC` | 37 | 0 | Already fully annotated by the dispatch-table loop in the driver (`comment(0xA9A8 + idx, ...)`); the gap counter missed loop-generated comments. |
| [x] | `&8FBB..&903B` | 35 | 25 | Tail of nfs_init_body and entry into `init_adlc_and_vectors`. |
| [x] | `&A0CF..&A103` | 31 | full | osargs_store_ptr_lo dispatcher walked. Removed 5 stale comments at &A0FF/&A105/&A109/&A10E/&A110 and &A120 that landed on data bytes / wrong instructions. Added 19 instruction-level comments. The `cmos_attr_table` overlap with the JSR osbyte_a2 operand bytes is suspicious -- noted for the rename pass. |
| [x] | `&A74D..&A7A0` | 32 | 5 | `cmd_table_fs` data tail — likely all data-banner-only now; verify. |
| [x] | `&B2F5..&B326` | 27 | 27 | `print_decimal_digit_no_spool` and dividers. |
| [x] | `&928A..&92B2` | 23 | 23 | `print_inline_no_spool` body. |
| [x] | `&8E71..&8E9C` | 20 | 18 | `noop_dey_rts`, `copy_template_to_zp` and friends. |
| [x] | `&8B38..&8B5F` | 19 | 19 | `cmd_net_check_hw` / `select_fs_cmd_net_fs`. |
| [x] | `&AD20..&AD32` | 19 | 2 | OSWORD dispatch table reasons. |
| [x] | `&8CFF..&8D24` | 18 | 12 | FSCV vector dispatch / *I am prologue. |
| [x] | `&8EB5..&8ED2` | 18 | 2 | Vector-table copy. Mostly clean. |
| [x] | `&8F58..&8F7E` | 18 | 12 | Inside `nfs_init_body` — CMOS-read sequence. |
| [x] | `&B003..&B014` | 18 | 8 | Workspace TXCB template-related. |
| [x] | `&B6D2..&B6F0` | 17 | 16 | `cmd_prot` / `cmd_unprot` body. |
| [x] | `&A6FE..&A723` | 15 | 12 | `cmd_flip` / station-context save. |
| [x] | `&924C..&925F` | 13 | 13 | `print_inline` family tails. |
| [x] | `&A4DC..&A4F9` | 12 | 10 | Tube-claim or relocated-block helper. |
| [x] | `&A8E7..&A8FE` | 12 | 1 | Tail of `save_txcb_done`. Mostly clean. |
| [x] | `&8CA9..&8CB9` | 11 | 10 | `setup_ws_ptr` body. |
| [x] | `&AA59..&AA6E` | 11 | 3 | Workspace setup tail. |
| [x] | `&B357..&B370` | 11 | 2 | `cmd_remove` body. Mostly clean. |
| [x] | `&8028..&8037` | 10 | 10 | NMI register-state probe. |
| [x] | `&8ABA..&8ACC` | 10 | 10 | CMP/SBC service-call normalisation. |
| [x] | `&9764..&976D` | 10 | 10 | We already worked on `txcb_init_template` banner; per-byte are recent. |
| [x] | `&A871..&A886` | 10 | 2 | Bridge-status helper. Mostly clean. |
| [x] | `&8E71..&8E9C` (dup?) | 20 | 18 | (resolve duplication during walk) |
| [x] | `&842C..&8434` | 5 | 3 | Small tail. |
| [x] | `&8515..&8526` | 8 | 6 | NMI tail. |
| [x] | `&881B..&8828` | 7 | 4 | Status-byte readout. |
| [x] | `&87F4..&87FA` | 4 | 4 | Small. |
| [x] | `&8900..&8907` | 4 | 4 | Small. |
| [x] | `&8914..&8922` | 8 | 8 | NMI / TX path. |
| [x] | `&8A6B..&8A7C` | 5 | 5 | Service-handler diagnostic. |
| [x] | `&8BAE..&8BBA` | 7 | 7 | `print_cmd_table_loop` tail. |
| [x] | `&8BC8..&8BCE` | 5 | 4 | `match_help_topic` head. |
| [x] | `&8D85..&8D90` | 8 | 6 | `cmd_iam_save_ctx` head. |
| [x] | `&8DA0..&8DA9` | 6 | 5 | `cmd_pass` head. |
| [x] | `&8F9A..&8FA6` | 7 | 7 | `osbyte_a1` tail. |
| [x] | `&9119..&914B` | 6 | 4 | cmd_syntax_table prefix. |
| [x] | `&9183..&91C6` | 8 | 5 | More cmd_syntax_table. |
| [x] | `&93CE..&93D2` | 5 | 5 | `prot_bit_encode_table` already worked on. |
| [x] | `&9421..&942F` | 9 | 6 | `cmd_fs_operation` head. |
| [x] | `&945C..&9463` | 4 | 2 | `cmd_rename` body. |
| [x] | `&94C5..&94D2` | 6 | 3 | `cmd_rename` tail. |
| [x] | `&988F..&989C` | 7 | 6 | wait_net_tx_ack neighbours. |
| [x] | `&98E6..&98F1` | 6 | 6 | Small. |
| [x] | `&9A0D..&9A13` | 4 | 2 | Small. |
| [x] | `&9AB4..&9AC6` | 5 | 3 | error_msg_table neighbours. |
| [x] | `&A3C4..&A3D0` | 7 | 7 | `parse_fs_ps_args` head. |
| [x] | `&A3DC..&A3E5` | 6 | 6 | `parse_fs_ps_args` body. |
| [x] | `&A6D8..&A6E4` | 6 | 3 | `cmd_flip` neighbour. |
| [x] | `&ABD3..&ABDB` | 4 | 3 | bridge_txcb_init_table neighbours. |
| [x] | `&AC25..&AC2B` | 4 | 1 | Small. |
| [x] | `&ADC2..&ADC6` | 5 | 3 | osword_claim_codes neighbour. |
| [x] | `&ADCE..&ADD2` | 5 | 3 | osword_claim_codes neighbour. |
| [x] | `&B069..&B07A` | 9 | 9 | `cmd_cdir` head. |
| [x] | `&B0D8..&B0DB` | 4 | 2 | Small. |
| [x] | `&B1B1..&B1BC` | 5 | 3 | ps_slot_txcb_template neighbours. |
| [x] | `&B1C9..&B1DB` | 5 | 5 | Small. |
| [x] | `&B293..&B29C` | 6 | 4 | Small. |
| [x] | `&B2CF..&B2DB` | 6 | 5 | `mask_owner_access` head. |
| [x] | `&B469..&B477` | 7 | 5 | Small. |
| [x] | `&B497..&B4A7` | 5 | 5 | Small. |
| [x] | `&BC75..&BC7E` | 7 | 1 | Mostly clean. |
| [x] | `&BDC3..&BDCB` | 5 | 4 | Small. |
| [x] | `&BFC8..&BFFF` | 4 | 4 | ROM tail / padding. |
| [x] | `&822A..&8230` | 4 | 4 | Small. |
| [x] | `&840B..&8411` | 4 | 4 | Small. |
| [x] | `&853B..&8540` | 6 | 1 | Mostly clean. |
| [x] | `&867E..&8686` | 9 | 1 | Mostly clean. |
| [x] | `&8258..&8265` | 7 | 4 | Small. |
| [x] | `&A3C4..&A3D0` (dup?) | 7 | 7 | (resolve duplication during walk) |
| [x] | `&A5FB..&A601` | 4 | 4 | 16-bit pointer add tail (os_text_ptr+Y -> fs_crc, where fs_crc is repurposed). |
| [x] | `&A9EF..&A9F6` | 4 | 4 | TSB/TRB pair updating fs_flags (set bits 1..3, clear FS-active flag). |
| [x] | `&AABB..&AAC2` | 4 | 3 | set_via_shadow_pair body (STA ws_0d68 / STA ws_0d69 / RTS). |

Generated by `/tmp/find_gap_ranges.py` against fantasm 0.9.0's anchored-only
address map; regenerate after each batch of fixes to confirm forward progress.
