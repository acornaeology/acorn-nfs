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

All 78 in-ROM auto-labels have been renamed. `grep -cE '\.l[0-9a-f]{4}\b|\.c[0-9a-f]{4}\b'`
on the regenerated ASM output now returns **0** in-ROM declarations
(the only remaining matches are `lc106..lc109` mentioned in
description text — see Findings).

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

## Findings

- **LCS mapper hit rate is low (~14%) on 4.21_v1 vs 4.18.** Of the
  78 auto-labels, only 11 had primary LCS mappings to a 4.18
  address; for the rest the surrounding code differs enough that
  no direct counterpart exists. This matches the project memory
  note "blockmatch finds 0 supplementary mappings; pairwise ratios
  on unmatched regions max out at 0.31 — Master 128 ANFS genuinely
  rewrote rather than relocated."
- **Names should be considered first-pass.** They were devised by
  examining each label's role in context; some sit in routines
  that haven't yet had Phase A/B annotation, so the name reflects
  immediate role rather than full semantic understanding. As later
  passes reveal more, names may need refinement.
- **HAZEL workspace external symbols are still auto-named.** A
  separate pool of 110 `lXXXX = &XXXX` declarations names
  workspace addresses outside the ROM (zero page, MOS workspace,
  HAZEL `&C100..&C2FF`, etc.). Only `lc109` at `&C109` was renamed
  in this phase. Renaming the rest is a follow-on Phase K2 if the
  user wants 0 auto-names anywhere in the disassembly. Each
  external benefits from a name that says what the byte holds, not
  just where it lives.
