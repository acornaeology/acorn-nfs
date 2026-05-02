# Phase K — Rename auto-generated `l*` / `c*` labels

py8dis emits `lXXXX` for branch targets and `cXXXX` for code/data
references that have no explicit `label()` call in the driver. Each
one is a meaningless hex name. This phase renames every one to a
domain-meaningful semantic label.

**Snapshot** (regen with
`grep -oE '\.(l|c)[0-9a-f]{4}\b' output/anfs-4.21_variant_1.asm | sort -u`):
77 in-ROM auto-labels declared in the asm + 1 HAZEL workspace
external (`lc109` at `&C109`). Total to rename: **78**.

## Method

1. **Examine in context** — `grep -nE '\.[lc][0-9a-f]{4}|<auto-label>'`
   across the ASM output, plus `fantasm asm extract` for full
   surrounding code.
2. **Find 4.18 counterpart where possible** — `fantasm addresses map
   4.21_variant_1 4.18 --addr <hex>`. Only ~14% of these auto-labels
   produced a primary mapping in the LCS pass; for the rest the
   surrounding code differs enough that no direct 4.18 source name
   is available.
3. **Decide the role** — local branch target inside one routine?
   shared dispatch entry? data table base? Pick a name that reads
   well at the use sites.
4. **Add `label(0xXXXX, "name")`** in the driver, near related
   declarations (zero-page block, hardware block, or alongside the
   enclosing subroutine).
5. **Verify + lint** — `uv run fantasm verify 4.21_variant_1` (must
   stay byte-identical) and `uv run fantasm lint 4.21_variant_1
   versions/anfs-4.21_variant_1/disassemble/disasm_anfs_421_variant_1.py`.
6. **Update this file** — strike through the cluster, fill in the
   chosen names.
7. **Commit per cluster** — typically all labels inside one
   subroutine, or one logical group of cross-references.

## Naming conventions

- **Reuse 4.18 names where the code is equivalent.** Most of these
  auto-labels sit inside routines that were carried over from 4.18.
  If the equivalent address in `versions/anfs-4.18` has a semantic
  label, copy that name verbatim. This keeps cross-version diffs
  minimal and lets readers compare directly.
  - Address mapping: `fantasm addresses map 4.21_variant_1 4.18 --addr <hex>`
  - Or `CHANGES-FROM-4.18.md` Section 15 (recovered-routines table)
    for the subset already manually mapped.
- **Only invent new names when there's no 4.18 counterpart** (new
  Master 128 code paths, restructured routines, etc.). Even then,
  match the surrounding routine's vocabulary.
- Local branch targets get short, role-based names:
  `loop`, `next_byte`, `done`, `not_found`, `retry`, `error_exit`.
  Prefix with the routine's vocabulary if there's any chance of
  collision (`copy_loop`, `copy_done`).
- Data-table bases use plural / structural names:
  `osbyte_a1_table`, `error_msg_table`, `dispatch_lo`.
- Mid-routine entry points (called by JSR from elsewhere) get
  full-routine-style names with a brief description in a
  `subroutine()` declaration if the calling convention is clear.
- Match style already used in the driver: `snake_case`, hex-suffix
  only for "this is the same routine but at a different entry"
  (e.g. `print_chars_from_buf` vs `print_10_chars`).

## Status: COMPLETE (2026-05-02)

Three sub-phases:

- **Phase K** — 78 in-ROM auto-labels (`lXXXX`/`cXXXX`)
- **Phase K2** — 31 `sub_cXXXX` / `loop_cXXXX` placeholder routines
- **Phase K3** — 110 workspace external symbols (`lXXXX = &XXXX`) +
  14 indexing-base aliases (`lXXXX = symbol+offset`) + 1 HAZEL
  base (`pydis_end` at `&C000`)

Total: **234 placeholder names eliminated.**

After all three sub-phases:
- `grep -cE '^\.[a-z]+_[a-z]?[0-9a-f]{4}$'` on the asm output returns **0**
  (no hex-tail label declarations anywhere)
- `grep -cE '^l[0-9a-f]{4}\s+= &'` returns **0** (no auto-named externals)
- `grep -cE '^l[0-9a-f]{4}\s+='` returns **0** (no `lXXXX =
  symbol+offset` aliases either)

The visible disassembly is fully semantically named. (Stale
references to old auto-names remain in inline comment text in
some places — those are documentation strings, not labels, and
will be cleaned up by ordinary annotation passes as routines are
revisited.)

Verified byte-identical reassembly, lint clean, comments check
clean.

## Per-routine clusters

Groups labels by enclosing named routine. Status: blank = TODO,
**done** = renamed and committed.

| # | Enclosing routine                | Auto labels                       | Status |
|---|----------------------------------|-----------------------------------|--------|
| 1 | `svc5_irq_check`                 | `c8032`                           | done |
| 2 | `install_tube_rx`                | `c8211`                           | done |
| 3 | `read_second_rx_byte`            | `c8258`                           | done |
| 4 | `check_sr2_loop_again`           | `c8264`                           | done |
| 5 | `scout_copy_done`                | `c842f`, `c8434`                  | done |
| 6 | `scout_page_overflow`            | `c847e`                           | done |
| 7 | `setup_sr_tx`                    | `c8524`                           | done |
| 8 | `write_second_tx_byte`           | `c881b`                           | done |
| 9 | `check_irq_loop`                 | `c8827`                           | done |
| 10 | `tx_calc_transfer`              | `c8922`                           | done |
| 11 | `restore_rom_slot`              | `c8a8d`                           | done |
| 12 | `dispatch_svc_with_state`       | `c8ace`                           | done |
| 13 | `select_fs_via_cmd_net_fs`      | `c8b5a`                           | done |
| 14 | `svc_4_star_command`            | `c8c46`                           | done |
| 15 | `get_ws_page`                   | `c8cbb`                           | done |
| 16 | `return_2`                      | `l8e7f`                           | done |
| 17 | `svc_2_private_workspace_pages` | `c8f1f`                           | done |
| 18 | `nfs_init_body`                 | `c8f4f`                           | done |
| 19 | `loop_copy_init_data`           | `c8fa6`                           | done |
| 20 | `done_alloc_handles`            | `c8fbb`, `c8fc1`, `c8fff`, `c9004` | done |
| 21 | `complete_nfs_init`             | `c9032`                           | done |
| 22 | `print_hex_nybble_no_spool`     | `c925d`                           | done |
| 23 | `loop_c9292`                    | `c9298`, `c92af`                  | done |
| 24 | `clear_conn_active`             | `c9421`                           | done |
| 25 | `parse_filename_validate`       | `c95be`                           | done |
| 26 | `sub_c95c8`                     | `c95cd`                           | done |
| 27 | `sub_c95da`                     | `c95e9`                           | done |
| 28 | `osbyte_a2`                     | `c962b`                           | done |
| 29 | `parse_object_argument`         | `c9653`                           | done |
| 30 | `sub_c9670`                     | `c967f`, `c9689`, `c968c`         | done |
| 31 | `sub_c968e`                     | `l9697`                           | done |
| 32 | `loop_c96a7`                    | `c96b0`, `c96b2`, `c96bc`         | done |
| 33 | `loop_print_help_byte`          | `c971e`, `c9725`                  | done |
| 34 | `loop_scan_channels`            | `c9827`                           | done |
| 35 | `loop_copy_suffix`              | `c9984`                           | done |
| 36 | `handle_net_error`              | `c9a0d`                           | done |
| 37 | `net_error_lookup_data`         | `l9aa6`                           | done |
| 38 | `send_osargs_request`           | `ca0cf`, `ca0db`                  | done |
| 39 | `sub_ca0fe`                     | `la103`                           | done |
| 40 | `skip_if_no_station`            | `ca3e5`                           | done |
| 41 | `sep_table_data`                | `ca4a0`                           | done |
| 42 | `cmd_run_via_urd`               | `ca4fc`                           | done |
| 43 | `library_dir_prefix`            | `ca5df`                           | done |
| 44 | `fsreply_2_copy_handles`        | `la6fe`, `ca70b`, `ca71c`         | done |
| 45 | `boot_load_cmd`                 | `la75b`, `ca75f`                  | done |
| 46 | `loop_ca84a`                    | `ca855`                           | done |
| 47 | `return_from_osword_setup`      | `la871`                           | done |
| 48 | `loop_copy_bcd_to_pb`           | `ca8e7`                           | done |
| 49 | `err_printer_busy`              | `caf92`                           | done |
| 50 | `read_osbyte_to_ws`             | `lb097`, `lb099`                  | done |
| 51 | `cdir_dispatch_col`             | `lb0ee`                           | done |
| 52 | `print_public_label`            | `cb185`                           | done |
| 53 | `option_str_offset_data`        | `lb29c`                           | done |
| 54 | `ex_print_col_sep`              | `cb2f7`, `cb2f9`, `cb2fc`         | done |
| 55 | `print_ps_now`                  | `cb474`                           | done |
| 56 | `skip_if_local_net`             | `cb56f`                           | done |
| 57 | `cmd_unprot`                    | `cb6d8`, `cb6e9`, `cb6eb`         | done |
| 58 | `error_escape_pressed`          | `cbd2d`                           | done |
| 59 | (HAZEL workspace external)      | `lc109`                           | done |

## Applied names

The complete address → name mapping applied in commit (this
phase). Names were proposed by examining each label in context;
they should be reviewed and refined as more context emerges in
future annotation passes.

| Addr | Auto label | New name |
|------|-----------|----------|
| &8032 | `c8032` | `irq_check_dispatch` |
| &8211 | `c8211` | `page_boundary_restore` |
| &8258 | `c8258` | `byte_pair_restore` |
| &8264 | `c8264` | `frame_complete_restore` |
| &842F | `c842f` | `scout_done_restore_x` |
| &8434 | `c8434` | `dispatch_imm_op_fail` |
| &847E | `c847e` | `tube_overflow_restore` |
| &8524 | `c8524` | `enable_irq_pending` |
| &881B | `c881b` | `check_fifo_loop` |
| &8827 | `c8827` | `frame_end_restore` |
| &8922 | `c8922` | `shadow_enable_flag` |
| &8A8D | `c8a8d` | `restore_rom_slot_entry` |
| &8ACE | `c8ace` | `dispatch_svc_state_check` |
| &8B5A | `c8b5a` | `select_fs_cmd_net_fs` |
| &8C46 | `c8c46` | `svc4_dispatch_lookup` |
| &8CBB | `c8cbb` | `get_ws_page_loop` |
| &8E7F | `l8e7f` | `return_2_data_table` |
| &8F1F | `c8f1f` | `private_ws_set_bit` |
| &8F4F | `c8f4f` | `nfs_init_check_fs_flags` |
| &8FA6 | `c8fa6` | `init_copy_skip_cmos` |
| &8FBB | `c8fbb` | `alloc_post_restore_check` |
| &8FC1 | `c8fc1` | `alloc_error_overflow` |
| &8FFF | `c8fff` | `alloc_common_entry` |
| &9004 | `c9004` | `alloc_store_station_id` |
| &9032 | `c9032` | `verify_copy_station_id` |
| &925D | `c925d` | `print_nybble_leading_zero` |
| &9298 | `c9298` | `print_next_string_char` |
| &92AF | `c92af` | `print_char_terminator` |
| &9421 | `c9421` | `clear_channel_flag` |
| &95BE | `c95be` | `parse_filename_padding` |
| &95CD | `c95cd` | `parse_filename_sub_padding` |
| &95E9 | `c95e9` | `parse_filename_sub_exit` |
| &962B | `c962b` | `osbyte_a2_value_tya` |
| &9653 | `c9653` | `parse_object_space_print` |
| &967F | `c967f` | `cmos_read_network_number` |
| &9689 | `c9689` | `cmos_print_value` |
| &968C | `c968c` | `help_dispatch_setup` |
| &9697 | `l9697` | `on_suffix_pattern` |
| &96B0 | `c96b0` | `match_char_loop_cmp` |
| &96B2 | `c96b2` | `match_char_found` |
| &96BC | `c96bc` | `match_char_process` |
| &971E | `c971e` | `help_print_start` |
| &9725 | `c9725` | `help_print_char_check` |
| &9827 | `c9827` | `scan_channel_store_reply` |
| &9984 | `c9984` | `suffix_copy_loop` |
| &9A0D | `c9a0d` | `net_error_close_spool` |
| &9AA6 | `l9aa6` | `error_msg_string_table` |
| &A0CF | `ca0cf` | `osargs_store_ptr_lo` |
| &A0DB | `ca0db` | `osargs_check_length` |
| &A103 | `la103` | `osargs_close_jump` |
| &A3E5 | `ca3e5` | `no_station_loop` |
| &A4A0 | `ca4a0` | `separator_char_table` |
| &A4FC | `ca4fc` | `cmd_run_load_mask` |
| &A5DF | `ca5df` | `library_path_string` |
| &A6FE | `la6fe` | `fsreply_2_skip_handles` |
| &A70B | `ca70b` | `fsreply_2_handle_loop` |
| &A71C | `ca71c` | `fsreply_2_store_handle` |
| &A75B | `la75b` | `boot_prefix_string` |
| &A75F | `ca75f` | `boot_suffix_string` |
| &A855 | `ca855` | `osword_store_svc_state` |
| &A871 | `la871` | `osword_pb_ready` |
| &A8E7 | `ca8e7` | `save_txcb_done` |
| &AF92 | `caf92` | `printer_busy_msg` |
| &B097 | `lb097` | `read_osbyte_return` |
| &B099 | `lb099` | `read_osbyte_table` |
| &B0EE | `lb0ee` | `cdir_size_done` |
| &B185 | `cb185` | `public_label_msg` |
| &B29C | `lb29c` | `option_offset_table` |
| &B2F7 | `cb2f7` | `col_sep_eol_check` |
| &B2F9 | `cb2f9` | `col_sep_print_cr` |
| &B2FC | `cb2fc` | `col_sep_print_char` |
| &B474 | `cb474` | `print_ps_padding` |
| &B56F | `cb56f` | `local_net_prefix` |
| &B6D8 | `cb6d8` | `unprot_clear` |
| &B6E9 | `cb6e9` | `unprot_check` |
| &B6EB | `cb6eb` | `unprot_apply` |
| &BD2D | `cbd2d` | `escape_error_close` |
| &C109 | `lc109` | `hazel_exec_addr` (HAZEL workspace external) |

## Phase K2: rename 31 `sub_`/`loop_` placeholder routines (2026-05-02)

Phase K's original scope was just `l*`/`c*` auto-labels. After
review, 31 routines remained that py8dis had auto-discovered via
code-flow analysis (JSR targets, branch-target entries) but the
driver had never explicitly declared. py8dis fell back to
`sub_cXXXX` / `loop_cXXXX` placeholder names. The earlier audit
phases couldn't see them because the audit checks "subroutines
declared in the driver", not "subroutines visible in the asm
output".

Phase K2 adds explicit `subroutine()` / `label()` declarations
for all 31 with semantic names.

| Addr | Placeholder | Kind | New name | Role |
|------|-------------|------|----------|------|
| &8409 | `sub_c8409` | subroutine | `save_acccon_for_shadow_ram` | Save ACCCON before scout buffer access (shadow RAM gating) |
| &8BEA | `loop_c8bea` | label | `loop_print_cmd_name` | Print command-table entry name characters |
| &8DA6 | `sub_c8da6` | subroutine | `load_transfer_params` | Load and initialize FS transfer parameters |
| &8E75 | `loop_c8e75` | label | `loop_copy_return_template` | Copy 11-byte return-value template to output buffer |
| &9292 | `loop_c9292` | label | `loop_print_inline_string` | Bump pointer and output next inline string char |
| &95C1 | `sub_c95c1` | subroutine | `print_station_low` | Print station low byte with 'P' label via print_inline |
| &95C8 | `sub_c95c8` | subroutine | `print_fs_station` | Print file-server station via print_inline |
| &95DA | `sub_c95da` | subroutine | `print_dir_syntax` | Print *Dir syntax help via print_inline |
| &965F | `sub_c965f` | subroutine | `print_network_from_cmos` | Read CMOS network and print with dot separator |
| &9670 | `sub_c9670` | subroutine | `print_fs_network` | Read CMOS FS network and print with dot separator |
| &968E | `sub_c968e` | subroutine | `dispatch_help_command` | Dispatch help command via parser lookup table |
| &96A7 | `loop_c96a7` | label | `loop_match_on_suffix` | Compare text against ON suffix (case-insensitive) |
| &96BD | `loop_c96bd` | label | `loop_skip_non_spaces` | Skip non-space chars in text |
| &96C8 | `loop_c96c8` | label | `loop_help_skip_spaces` | Skip spaces to next help token |
| &96DB | `loop_c96db` | label | `loop_copy_command_suffix` | Copy template command suffix until '.' |
| &96E7 | `loop_c96e7` | label | `loop_copy_topic_name` | Copy help topic name from buffer |
| &96EB | `loop_c96eb` | label | `loop_store_topic_char` | Store topic char and continue copy loop |
| &9FEE | `sub_c9fee` | subroutine | `send_open_file_request` | Send file open request with V flag (dir check) |
| &A0F2 | `loop_ca0f2` | label | `loop_extract_attribute_bits` | Shift CMOS value, extract attribute bits |
| &A0FE | `sub_ca0fe` | subroutine | `store_carry_to_workspace` | Store carry flag to workspace via OSBYTE A2 |
| &A84A | `loop_ca84a` | label | `loop_save_osword_workspace` | Save and reload OSWORD workspace bytes |
| &A85C | `loop_ca85c` | label | `loop_restore_osword_workspace` | Restore OSWORD workspace bytes from stack |
| &A877 | `sub_ca877` | subroutine | `extract_osword_subcode` | Extract and dispatch OSWORD sub-code |
| &A8EC | `loop_ca8ec` | label | `loop_copy_pbytes_to_workspace` | Copy parameter-block bytes to workspace |
| &B0A0 | `sub_cb0a0` | label | `cmd_cdir_indirect_dispatch` | Dead `JMP (l4898,X)` at cmd_cdir boundary; never executed |
| &B1B4 | `loop_cb1b4` | label | `loop_print_dir_format` | Print directory listing format chars |
| &B2B9 | `loop_cb2b9` | label | `loop_trim_trailing_spaces` | Trim trailing spaces from cmd-arg buffer |
| &B316 | `loop_cb316` | label | `loop_divide_decimal_digit` | Extract one decimal digit by repeated subtraction |
| &BB3C | `loop_cbb3c` | label | `loop_save_fcb_workspace` | Save FCB workspace bytes to stack |
| &BB5F | `loop_cbb5f` | label | `loop_restore_fcb_workspace` | Restore FCB workspace bytes from stack |
| &BE16 | `loop_cbe16` | label | `loop_print_hex_row` | Print 16 hex bytes per row with column numbering |

Note: `loop_help_skip_spaces` (&96C8) was the agent's `loop_skip_spaces`
renamed to avoid collision with an existing `loop_skip_spaces` label
at &948B in a different routine.

## Phase K3: rename 110 workspace external symbols (2026-05-02)

py8dis emits `lXXXX = &XXXX` external declarations for any
address outside the ROM that the code references but the driver
hasn't named. Phase K3 names every one. Distribution:

- 81 HAZEL workspace bytes (`&C001..&C2F3`) — ANFS private FS
  workspace; previously all auto-named
- 14 page-1-3 / MOS-vector addresses — most have direct 4.18
  semantic names that we reused verbatim (`error_block`,
  `stack_page_*`, `vdu_*`, `last_break_type`, `rom_type_table`,
  `nmi_code_base`, etc.)
- 8 misc RAM addresses
- 7 MOS hardware registers (`acccon` at `&FE34`, plus shadow
  registers and Master 128 INTOFF/INTON mirrors)
- 3 zero page

Plus:

- **14 indexing-base aliases** — py8dis emits `lXXXX = symbol+offset`
  for `LDA somelabel,X/Y` patterns where the base lies inside an
  existing routine. Naming the base address explicitly replaces
  the auto-alias with a domain name (`tx_length_table`,
  `cmd_dispatch_lo_table`, `nmi_shim_source`, etc.).
- **1 HAZEL base** at `&C000` — was being addressed via py8dis's
  built-in `pydis_end` symbol (meaning "first address past ROM").
  Renamed to `hazel_fs_station_hi` to make stores there
  self-explanatory.

### Caveats: HAZEL bytes flagged for refinement

Several HAZEL bytes still carry partly-hex-derived names where
the byte's semantic role is not yet fully understood:

- `hazel_ws_spare_0a / 14 / 38 / f7` — single-write/read bytes that
  appear to be ad-hoc scratch slots; full meaning needs the
  surrounding routine annotated.
- `hazel_shadow_10 / 20 / 30 / 40 / 50 / 60 / 70 / 72 / 73 / 74 / 78
  / 88 / 98 / a8 / b8 / c8 / ca / cb / cc / cd / ce / cf / d0 / d1
  / d4 / d5 / d6 / d7 / d9 / f3` — bytes inside the `&C200..&C2F3`
  region (32 entries) named by offset within that "shadow" region.
  These appear to be a per-channel shadow array; identifying the
  field structure needs a focused pass on the routines that touch
  this region (channel-management code).
- `hazel_txcb_spare_116`, `hazel_chan_status` (single-byte placeholder
  for &C1C8 area), `hazel_examine_attr` (best-effort name).

These names are still better than auto-names — they mark the
region and approximate role — but refinement is wanted.

## Findings

- **LCS mapper hit rate is low (~14%) on 4.21_v1 vs 4.18.** Of the
  78 auto-labels, only 11 had primary LCS mappings to a 4.18
  address; for the rest the surrounding code differs enough that
  no direct counterpart exists. This matches the project memory
  note "blockmatch finds 0 supplementary mappings; pairwise ratios
  on unmatched regions max out at 0.31 — Master 128 ANFS genuinely
  rewrote rather than relocated."
- **Names should be considered first-pass.** They were devised by
  examining each label's role in context. As later passes reveal
  more, names may need refinement.
- **The audit gap that hid 31 placeholder routines:** py8dis
  auto-discovers JSR targets and routine-shaped branch entries.
  When the driver doesn't supply an explicit `subroutine()` /
  `label()` call for those addresses, py8dis falls back to
  `sub_cXXXX` / `loop_cXXXX` placeholder names. The fantasm audit
  scans declared subroutines, so these placeholders never showed
  up in the audit report — they were visible in the asm output
  but invisible to the audit. Closed in Phase K2 (above); future
  versions should add a cross-check that scans the asm for
  hex-tail names directly. A `grep -E '^\.[a-z]+_[a-z]?[0-9a-f]{4}$'`
  rule on the asm output catches both `lXXXX/cXXXX` auto-labels
  AND `sub_/loop_` placeholders in one pass.
- **HAZEL workspace external symbols are still auto-named.** A
  separate pool of 110 `lXXXX = &XXXX` declarations names
  workspace addresses outside the ROM (zero page, MOS workspace,
  HAZEL `&C100..&C2FF`, etc.). Only `lc109` at `&C109` was renamed
  in this phase. Renaming the rest is a follow-on Phase K2 if the
  user wants 0 auto-names anywhere in the disassembly. Each
  external benefits from a name that says what the byte holds, not
  just where it lives.
