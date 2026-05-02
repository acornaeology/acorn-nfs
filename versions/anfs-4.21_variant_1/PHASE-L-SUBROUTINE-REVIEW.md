# Phase L — systematic subroutine comment review + Markdown rewrite

For each of 452 subroutines:

1. Extract the assembly via `uv run fantasm asm extract 4.21_variant_1 <addr>`.
2. Compare the existing `subroutine()` description against what the
   code actually does. Correct any inaccuracies.
3. Rewrite the description using the Markdown features documented
   in `acornaeology.github.io/AUTHORING.md`:
   - GFM tables for bit decompositions, register I/O summaries,
     dispatch tables, multi-byte field layouts.
   - `[label](address:HEX?hex)` for first-mention cross-references
     (use `?hex` to render label + clickable hex).
   - Inline backticks for register names, hex literals, mnemonics.
   - **Bold** / *emphasis* for key facts.
   - En-dashes (` – `) for parenthetical breaks.
4. Verify byte-identical reassembly + lint clean per cluster
   (~10–20 subs).
5. Commit per cluster.
6. Update this file: mark each row `done` / `skipped` (with reason).

## Phase L0 — memory-map metadata enrichment (done 2026-05-02)

Before resuming Phase L proper, took a detour to add memory-map
metadata to the most-referenced workspace and MMIO addresses.
Per AUTHORING.md §3.1, a `label()` with `description=` /
`length=` / `group=` / `access=` kwargs becomes a memory-map
entry that links cleanly when subroutine descriptions reference
it via `[name](address:HEX?hex)`. Without metadata, such links
warn at site build and render as broken `<a href="address:XXXX">`.

71 enriched labels in 3 groups:

- **`io` (11):** ADLC registers `&FEA0..&FEA3`; Econet ULA
  `&FE18` / `&FE20`; Master 128 ROMSEL/break-type/ACCCON/INTOFF/
  INTON shadows `&FE28` / `&FE2B` / `&FE34` / `&FE38` / `&FE3C`.
  ACCCON gets a full bit-by-bit table.
- **`mmio` (10):** MOS extended-vector dispatchers `&FF1B..&FF2D`;
  MOS internal workspace `&FFB7`; the two MOS-area indexing-base
  aliases `&FFB0` / `&FFBD`.
- **`ram_workspace` (50):** page-2 OS vector slots `&0212..&021E`;
  NMI shim `&0D07..&0D14`; scout/ACK packet buffer `&0D20..&0D26`;
  received-scout fields `&0D3D..&0D44`; TX state `&0D4A..&0D50`;
  ANFS workspace `&0D60..&0D72`.

Result: site build now reports **0 warnings** (was 11
pre-Phase-L0). All `[name](address:HEX?hex)` links from
subroutine descriptions resolve to the memory-map page with
proper tooltips (`&XXXX – first sentence of description`).

Phase L proper can now use the full linking syntax for these
addresses across all 431 remaining routines.

## Conventions

- **Title** (`title=` kwarg): one-line banner, ≤ 60 chars.
  Doubles as tooltip text when readers hover JSR/JMP/BXX
  operands targeting the routine.
- **Description**: full Markdown. First sentence (or first line
  before `\n` inside the first paragraph) is the tooltip brief
  for memory-map references; first paragraph + extended
  paragraphs render in full on the listing page.
- For workspace addresses with no memory-map metadata
  (`&0Dxx`, etc.), use bare backticked text rather than
  `address:` links — the link will warn at site build because
  the target has no map entry. Adding memory-map metadata to
  commonly-referenced workspace bytes is a separate Phase L2
  candidate.

## Progress

452 routines total. Processing address-ordered, in clusters of
~10–20 per commit.

| # | Addr | Name | Status | Notes |
|---|------|------|--------|-------|
| 1 | &8028 | `svc5_irq_check` | done | dispatch decision rendered as table |
| 2 | &8045 | `generate_event` | kept | already terse + accurate |
| 3 | &8050 | `adlc_init` | done | added [adlc_full_reset]/[init_nmi_workspace] links |
| 4 | &8070 | `init_nmi_workspace` | done | added workspace-fields table |
| 5 | &809B | `nmi_rx_scout` | done | inline-code formatting; econet_station_id ref |
| 6 | &80B8 | `nmi_rx_scout_net` | done | network-match dispatch table; ?hex on copy_scout_to_buffer |
| 7 | &80D8 | `scout_error` | done | bullet-list dispatch; nmi_rx_scout/scout_complete links |
| 8 | &8112 | `scout_complete` | done | bullet-list match/no-match; tx_calc_transfer/scout_error links |
| 9 | &8195 | `port_match_found` | done | C/V triage table; 4 cross-refs added |
| 10 | &81A7 | `send_data_rx_ack` | done | data_rx_setup/ack_tx_write_dest links + inline code |
| 11 | &81B8 | `data_rx_setup` | done | added ?hex on first-mention links |
| 12 | &81C2 | `nmi_data_rx` | done | added ?hex on chain links |
| 13 | &81D6 | `nmi_data_rx_net` | done | added ?hex on first-mention links |
| 14 | &81EC | `nmi_data_rx_skip` | done | added ?hex on first-mention links |
| 15 | &81F7 | `install_data_rx_handler` | done | bit-1 dispatch table; nmi_data_rx_bulk link |
| 16 | &8215 | `nmi_error_dispatch` | done | tx_flags bit-7 dispatch table; tx_result_fail link |
| 17 | &8223 | `nmi_data_rx_bulk` | done | already has bullet list; refined inline code |
| 18 | &8268 | `data_rx_complete` | done | inline code refinement; ?hex on ack_tx |
| 19 | &8291 | `nmi_data_rx_tube` | kept | already has accurate inline-code description |
| 20 | &82DF | `ack_tx` | kept | already has links + inline code; description complete |
| 21 | &82F8 | `ack_tx_write_dest` | done | added ?hex on send_data_rx_ack/imm_op_build_reply |
| 22 | &8316 | `nmi_ack_tx_src` | done | rx_src_net dispatch table; econet_station_id + post_ack_scout links |
| 23 | &832D | `post_ack_scout` | done | bullet-list match/no-match; rx_src_stn + rx_port links |
| 24 | &833F | `advance_rx_buffer_ptr` | done | bullet-listed reads; tx_flags link |
| 25 | &8386 | `nmi_post_ack_dispatch` | done | 3-row scout_port/control dispatch table; saved_nmi_lo/hi + rx_complete_update_rxcb links |
| 26 | &8395 | `rx_complete_update_rxcb` | done | 3-step numbered list; bold sync-point note; advance_rx_buffer_ptr + discard_reset_rx links |
| 27 | &83E5 | `discard_reset_rx` | done | 3-stage numbered chain; all 3 stage links + nmi_rx_scout + set_nmi_vector |
| 28 | &83E8 | `reset_adlc_rx_listen` | done | discard_reset_rx + set_nmi_rx_scout links |
| 29 | &83EB | `set_nmi_rx_scout` | done | nmi_rx_scout + set_nmi_vector + chain links |
| 30 | &83F2 | `discard_reset_listen` | done | tube_present + rx_src_net + release_tube links |
| 31 | &8400 | `copy_scout_to_buffer` | done | bit-1 write-path table; rx_src_stn + rx_src_net + release_tube links |
| 32 | &8409 | `save_acccon_for_shadow_ram` | done | full title + description; acccon link |
| 33 | &8448 | `release_tube` | done | bit-7 dispatch table; bold idempotent note |
| 34 | &8454 | `immediate_op` | done | 3-row range table; scout_ctrl/econet_flags/imm_op_dispatch_lo links |
| 35 | &848B | `imm_op_dispatch_lo` | kept | already has accurate description with per-entry expr |
| 36 | &8493 | `rx_imm_exec` | done | scout_data + exec_addr_lo/hi links |
| 37 | &84B1 | `rx_imm_poke` | done | inline-code refinement |
| 38 | &84BC | `rx_imm_machine_type` | done | ?hex on set_rx_buf_len_hi |
| 39 | &84CE | `rx_imm_peek` | done | tx_calc_transfer link |
| 40 | &84F9 | `imm_op_build_reply` | done | inline-code refinement |
| 41 | &8512 | `setup_sr_tx` | done | op-code dispatch table; tx_op_type/ws_0d68/ws_0d69/scout_complete links |
| 42 | &852C | `advance_buffer_ptr` | done | inline-code refinement |
| 43 | &853B | `tx_done_dispatch_lo` | kept | already accurate; per-entry expr declarations |
| 44 | &8540 | `tx_done_jsr` | done | exec_addr_lo + tx_done_exit links |
| 45 | &8549 | `tx_done_econet_event` | done | exec_addr_lo/hi + tx_done_dispatch + tx_done_exit links |
| 46 | &8557 | `tx_done_os_proc` | done | exec_addr_lo/hi + tx_done_dispatch + tx_done_exit links |
| 47 | &8563 | `tx_done_halt` | done | econet_flags + tx_done_continue/exit links |
| 48 | &857A | `tx_done_continue` | done | econet_flags + tx_done_halt/dispatch/exit links |
| 49 | &8582 | `tx_done_exit` | done | tx_done_dispatch_lo + svc5_irq_check links |
| 50 | &8589 | `tx_begin` | done | numbered 4-step list; tx_calc_transfer + inactive_poll links |
| 51 | &85F1 | `inactive_poll` | done | numbered 5-step list; rx_remote_addr + intoff_test_inactive links |
| 52 | &85FC | `intoff_test_inactive` | done | INACTIVE dispatch table; econet_station_id + econet_nmi_enable + tx_prepare + tx_line_jammed links |
| 53 | &862C | `tx_bad_ctrl_error` | done | tx_begin link |
| 54 | &8630 | `tx_line_jammed` | done | inactive_poll/intoff_test_inactive links + numbered breakdown |
| 55 | &864A | `tx_prepare` | done | 4-step list + Tube/Direct dispatch table; nmi_tx_data + tx_dst_stn/net/src_stn links |
| 56 | &867E | `tx_ctrl_dispatch_lo` | kept | already accurate dispatch table |
| 57 | &8686 | `tx_ctrl_machine_type` | done | tx_ctrl_dispatch_lo link |
| 58 | &868A | `tx_ctrl_peek` | done | tx_ctrl_store_and_add link |
| 59 | &868E | `tx_ctrl_poke` | done | tx_ctrl_store_and_add link |
| 60 | &8690 | `tx_ctrl_store_and_add` | done | numbered list; rx_port + tx_ctrl_proc + tx_calc_transfer links |
| 61 | &86A2 | `tx_ctrl_proc` | done | tx_calc_transfer link |
| 62 | &86E7 | `nmi_tx_data` | done | SR1 IRQ dispatch table; adlc_tx + adlc_cr1 links |
| 63 | &8723 | `tx_last_data` | done | bit-decomposition table; corrected &8728 → &872F; refreshed set_nmi_vector/nmi_rti/econet_nmi_enable links (post-L0) |
| 64 | &872F | `nmi_tx_complete` | done | CR1 sequence table + rx_src_net flags table; tx_result_ok/handshake_await_ack/nmi_reply_scout links |
| 65 | &874B | `nmi_reply_scout` | done | econet_station_id link; inline-code refinement |
| 66 | &875F | `nmi_reply_cont` | done | nmi_reply_validate link; bold optimisation note |
| 67 | &8773 | `reject_reply` | done | tx_result_fail + nmi_reply_scout/validate/scout_ack_src links |
| 68 | &8776 | `nmi_reply_validate` | kept | already has accurate numbered list + tx_dst_stn/net links |
| 69 | &87BE | `nmi_scout_ack_src` | done | rx_src_net dispatch table; econet_station_id link |
| 70 | &87CE | `data_tx_begin` | done | bit-1 dispatch table; nmi_data_tx + ack_tx links |
| 71 | &87E3 | `nmi_data_tx` | done | 3-row count/IRQ dispatch table; tx_last_data link |
| 72 | &8845 | `nmi_data_tx_tube` | kept | already has accurate description with tx_prepare link |
| 73 | &8886 | `handshake_await_ack` | kept | already has accurate description with all relevant links |
| 74 | &8892 | `nmi_final_ack` | kept | already has accurate numbered list + tx_result_ok/nmi_reply_validate links |
| 75 | &88A6 | `nmi_final_ack_net` | kept | already has accurate description with tx_result_fail/nmi_final_ack_validate links |
| 76 | &88BA | `nmi_final_ack_validate` | done | nmi_final_ack + tx_dst_stn/net + tx_result_fail/ok links |
| 77 | &88DE | `tx_result_ok` | kept | already has accurate description with tx_store_result/ack_tx/nmi_tx_complete links |
| 78 | &88E2 | `tx_result_fail` | done | tx_store_result link |
| 79 | &88E4 | `tx_store_result` | done | tx_complete_flag + discard_reset_rx links |
| 80 | &88F0 | `rom_gap_88f0` | | |
| 81 | &8900 | `tx_calc_transfer` | | |
| 82 | &898C | `adlc_full_reset` | | |
| 83 | &899B | `adlc_rx_listen` | | |
| 84 | &89A6 | `wait_idle_and_reset` | | |
| 85 | &89B9 | `save_econet_state` | | |
| 86 | &89CA | `nmi_bootstrap_entry` | | |
| 87 | &89D8 | `rom_set_nmi_vector` | | |
| 88 | &89ED | `svc_dispatch_lo` | | |
| 89 | &8A20 | `svc_dispatch_hi` | | |
| 90 | &8A54 | `service_handler` | | |
| 91 | &8AEA | `cmd_roff` | | |
| 92 | &8B00 | `scan_remote_keys` | | |
| 93 | &8B18 | `save_text_ptr` | | |
| 94 | &8B23 | `cmd_net_fs` | | |
| 95 | &8B45 | `svc_18_fs_select` | | |
| 96 | &8B4D | `ensure_fs_selected` | | |
| 97 | &8B52 | `select_fs_via_cmd_net_fs` | | |
| 98 | &8BBB | `help_print_nfs_cmds` | | |
| 99 | &8BC0 | `help_utils` | | |
| 100 | &8BC4 | `help_net` | | |
| 101 | &8BC6 | `print_cmd_table` | | |
| 102 | &8BD5 | `print_cmd_table_loop` | | |
| 103 | &8BD8 | `loop_next_entry` | | |
| 104 | &8C06 | `loop_print_syntax` | | |
| 105 | &8C25 | `done_print_table` | | |
| 106 | &8C29 | `help_wrap_if_serial` | | |
| 107 | &8C42 | `svc_4_star_command` | | |
| 108 | &8C51 | `svc_9_help` | | |
| 109 | &8C64 | `svc_return_unclaimed` | | |
| 110 | &8C93 | `print_version_header` | | |
| 111 | &8CAD | `get_ws_page` | | |
| 112 | &8CBD | `setup_ws_ptr` | | |
| 113 | &8CC7 | `svc_3_autoboot` | | |
| 114 | &8CFD | `notify_new_fs` | | |
| 115 | &8CFF | `call_fscv` | | |
| 116 | &8D02 | `issue_svc_15` | | |
| 117 | &8D09 | `svc_dispatch_idx_2` | | |
| 118 | &8D24 | `check_credits_easter_egg` | | |
| 119 | &8D91 | `cmd_iam` | | |
| 120 | &8DA6 | `load_transfer_params` | | |
| 121 | &8DD5 | `cmd_pass` | | |
| 122 | &8E21 | `clear_if_station_match` | | |
| 123 | &8E2D | `check_urd_prefix` | | |
| 124 | &8E3C | `send_cmd_and_dispatch` | | |
| 125 | &8E5B | `dir_op_dispatch` | | |
| 126 | &8E61 | `svc_dispatch` | | |
| 127 | &8E98 | `read_cmos_byte_0` | | |
| 128 | &8E9A | `osbyte_a1` | | |
| 129 | &8EA7 | `fs_vector_table` | | |
| 130 | &8EC9 | `osbyte_x0` | | |
| 131 | &8ECB | `osbyte_yff` | | |
| 132 | &8ED2 | `osbyte_x0_y0` | | |
| 133 | &8ED8 | `svc_7_osbyte` | | |
| 134 | &8EE9 | `raise_y_to_c8` | | |
| 135 | &8EF0 | `store_ws_page_count` | | |
| 136 | &8F10 | `svc_2_private_workspace_pages` | | |
| 137 | &8F38 | `nfs_init_body` | | |
| 138 | &903C | `init_adlc_and_vectors` | | |
| 139 | &904F | `write_vector_entry` | | |
| 140 | &9064 | `restore_fs_context` | | |
| 141 | &9071 | `fscv_6_shutdown` | | |
| 142 | &909E | `verify_ws_checksum` | | |
| 143 | &90B5 | `error_net_checksum` | | |
| 144 | &90C7 | `print_station_id` | | |
| 145 | &91F9 | `print_newline_no_spool` | | |
| 146 | &91FB | `print_char_no_spool` | | |
| 147 | &9201 | `print_byte_no_spool` | | |
| 148 | &9236 | `print_hex_byte` | | |
| 149 | &923F | `print_hex_nybble` | | |
| 150 | &924C | `print_hex_byte_no_spool` | | |
| 151 | &9255 | `print_hex_nybble_no_spool` | | |
| 152 | &9261 | `print_inline` | | |
| 153 | &9269 | `loop_next_char` | | |
| 154 | &928A | `print_inline_no_spool` | | |
| 155 | &92B2 | `parse_addr_arg` | | |
| 156 | &934A | `err_bad_hex` | | |
| 157 | &939A | `is_decimal_digit` | | |
| 158 | &93A2 | `is_dec_digit_only` | | |
| 159 | &93AB | `get_access_bits` | | |
| 160 | &93B5 | `get_prot_bits` | | |
| 161 | &93C8 | `prot_bit_encode_table` | | |
| 162 | &93D3 | `set_text_and_xfer_ptr` | | |
| 163 | &93D7 | `set_xfer_params` | | |
| 164 | &93DD | `set_options_ptr` | | |
| 165 | &93E1 | `clear_escapable` | | |
| 166 | &93E6 | `cmp_5byte_handle` | | |
| 167 | &93F2 | `fscv_7_read_handles` | | |
| 168 | &93F7 | `set_conn_active` | | |
| 169 | &940D | `clear_conn_active` | | |
| 170 | &9425 | `cmd_fs_operation` | | |
| 171 | &9437 | `error_bad_filename` | | |
| 172 | &9446 | `check_not_ampersand` | | |
| 173 | &944E | `read_filename_char` | | |
| 174 | &945E | `send_fs_request` | | |
| 175 | &9463 | `copy_fs_cmd_name` | | |
| 176 | &9483 | `parse_quoted_arg` | | |
| 177 | &94C5 | `cmd_rename` | | |
| 178 | &9512 | `cmd_dir` | | |
| 179 | &95C1 | `print_station_low` | | |
| 180 | &95C8 | `print_fs_station` | | |
| 181 | &95DA | `print_dir_syntax` | | |
| 182 | &9612 | `osbyte_a2` | | |
| 183 | &965F | `print_network_from_cmos` | | |
| 184 | &9670 | `print_fs_network` | | |
| 185 | &968E | `dispatch_help_command` | | |
| 186 | &973D | `init_txcb_bye` | | |
| 187 | &973F | `init_txcb_port` | | |
| 188 | &974B | `init_txcb` | | |
| 189 | &9763 | `txcb_init_template` | | |
| 190 | &976F | `send_request_nowrite` | | |
| 191 | &9773 | `send_request_write` | | |
| 192 | &9776 | `cmd_bye` | | |
| 193 | &978A | `save_net_tx_cb` | | |
| 194 | &978B | `save_net_tx_cb_vset` | | |
| 195 | &97B7 | `prep_send_tx_cb` | | |
| 196 | &97CD | `recv_and_process_reply` | | |
| 197 | &9850 | `lang_1_remote_boot` | | |
| 198 | &987E | `lang_3_execute_at_0100` | | |
| 199 | &988F | `check_escape_and_classify` | | |
| 200 | &9895 | `raise_escape_error` | | |
| 201 | &989F | `lang_4_remote_validated` | | |
| 202 | &98AF | `lang_0_insert_remote_key` | | |
| 203 | &98BE | `wait_net_tx_ack` | | |
| 204 | &9900 | `cond_save_error_code` | | |
| 205 | &9930 | `fixup_reply_status_a` | | |
| 206 | &993B | `load_reply_and_classify` | | |
| 207 | &993D | `classify_reply_error` | | |
| 208 | &99A7 | `error_bad_inline` | | |
| 209 | &99C0 | `error_inline_log` | | |
| 210 | &99C3 | `error_inline` | | |
| 211 | &99DF | `check_net_error_code` | | |
| 212 | &9A3A | `append_drv_dot_num` | | |
| 213 | &9A5E | `append_space_and_num` | | |
| 214 | &9A69 | `append_decimal_num` | | |
| 215 | &9A7A | `append_decimal_digit` | | |
| 216 | &9A9A | `net_error_lookup_data` | | |
| 217 | &9B24 | `init_tx_ptr_and_send` | | |
| 218 | &9B2C | `send_net_packet` | | |
| 219 | &9B75 | `pass_txbuf_init_table` | | |
| 220 | &9B81 | `init_tx_ptr_for_pass` | | |
| 221 | &9B89 | `setup_pass_txbuf` | | |
| 222 | &9BB6 | `poll_adlc_tx_status` | | |
| 223 | &9BF5 | `load_text_ptr_and_parse` | | |
| 224 | &9C00 | `gsread_to_buf` | | |
| 225 | &9C22 | `filev_handler` | | |
| 226 | &9C3E | `do_fs_cmd_iteration` | | |
| 227 | &9C85 | `send_txcb_swap_addrs` | | |
| 228 | &9CB5 | `setup_dir_display` | | |
| 229 | &9D0C | `recv_reply` | | |
| 230 | &9D44 | `print_load_exec_addrs` | | |
| 231 | &9D4F | `print_5_hex_bytes` | | |
| 232 | &9D5F | `copy_fsopts_to_zp` | | |
| 233 | &9D6B | `skip_one_and_advance5` | | |
| 234 | &9D6C | `advance_y_by_4` | | |
| 235 | &9D71 | `copy_workspace_to_fsopts` | | |
| 236 | &9D7E | `retreat_y_by_4` | | |
| 237 | &9D7F | `retreat_y_by_3` | | |
| 238 | &9D87 | `check_and_setup_txcb` | | |
| 239 | &9DDC | `dispatch_osword_op` | | |
| 240 | &9E82 | `format_filename_field` | | |
| 241 | &9EAB | `argsv_handler` | | |
| 242 | &9FB1 | `close_all_fcbs` | | |
| 243 | &9FB4 | `return_with_last_flag` | | |
| 244 | &9FB6 | `finalise_and_return` | | |
| 245 | &9FC2 | `osfind_close_or_open` | | |
| 246 | &9FCF | `clear_result` | | |
| 247 | &9FEE | `send_open_file_request` | | |
| 248 | &A0A9 | `fscv_0_opt_entry` | | |
| 249 | &A0FE | `store_carry_to_workspace` | | |
| 250 | &A10B | `fscv_1_eof` | | |
| 251 | &A12C | `update_addr_from_offset9` | | |
| 252 | &A131 | `update_addr_from_offset1` | | |
| 253 | &A133 | `add_workspace_to_fsopts` | | |
| 254 | &A134 | `adjust_fsopts_4bytes` | | |
| 255 | &A145 | `store_adjusted_byte` | | |
| 256 | &A14C | `gbpbv_handler` | | |
| 257 | &A1EF | `lookup_cat_entry_0` | | |
| 258 | &A1F3 | `lookup_cat_slot_data` | | |
| 259 | &A1FA | `setup_transfer_workspace` | | |
| 260 | &A284 | `recv_reply_preserve_flags` | | |
| 261 | &A28A | `send_osbput_data` | | |
| 262 | &A29F | `write_block_entry` | | |
| 263 | &A2ED | `write_data_block` | | |
| 264 | &A329 | `tail_update_catalogue` | | |
| 265 | &A390 | `tube_claim_c3` | | |
| 266 | &A398 | `cmd_fs` | | |
| 267 | &A3BB | `print_fs_info_newline` | | |
| 268 | &A3C4 | `parse_fs_ps_args` | | |
| 269 | &A3E7 | `get_pb_ptr_as_index` | | |
| 270 | &A3E9 | `byte_to_2bit_index` | | |
| 271 | &A3FF | `net_1_read_handle` | | |
| 272 | &A405 | `net_2_read_handle_entry` | | |
| 273 | &A415 | `net_3_close_handle` | | |
| 274 | &A42F | `fscv_3_star_cmd` | | |
| 275 | &A440 | `cmd_fs_reentry` | | |
| 276 | &A45B | `match_fs_cmd` | | |
| 277 | &A4A2 | `loop_skip_trail_spaces` | | |
| 278 | &A4E4 | `fscv_2_star_run` | | |
| 279 | &A4F1 | `cmd_run_via_urd` | | |
| 280 | &A5A1 | `error_bad_command` | | |
| 281 | &A5AE | `check_exec_addr` | | |
| 282 | &A5C3 | `alloc_run_channel` | | |
| 283 | &A638 | `fsreply_3_set_csd` | | |
| 284 | &A63E | `fsreply_5_set_lib` | | |
| 285 | &A644 | `find_station_bit2` | | |
| 286 | &A66F | `find_station_bit3` | | |
| 287 | &A69A | `cmd_flip` | | |
| 288 | &A6A6 | `flip_set_station_boot` | | |
| 289 | &A6D5 | `fsreply_1_copy_handles_boot` | | |
| 290 | &A6E5 | `fsreply_2_copy_handles` | | |
| 291 | &A764 | `boot_cmd_oscli` | | |
| 292 | &A76C | `cmd_table_fs` | | |
| 293 | &A83B | `svc_8_osword` | | |
| 294 | &A864 | `osword_setup_handler` | | |
| 295 | &A877 | `extract_osword_subcode` | | |
| 296 | &A901 | `bin_to_bcd` | | |
| 297 | &A910 | `osword_10_handler` | | |
| 298 | &A985 | `osword_12_handler` | | |
| 299 | &A9A8 | `osword_13_dispatch_lo` | | |
| 300 | &A9BA | `osword_13_dispatch_hi` | | |
| 301 | &A9CC | `osword_13_read_station` | | |
| 302 | &A9DA | `osword_13_set_station` | | |
| 303 | &AA72 | `osword_13_read_csd` | | |
| 304 | &AA75 | `osword_13_write_csd` | | |
| 305 | &AA82 | `copy_pb_byte_to_ws` | | |
| 306 | &AA91 | `osword_13_read_ws_pair` | | |
| 307 | &AA9D | `osword_13_write_ws_pair` | | |
| 308 | &AAB2 | `osword_13_read_prot` | | |
| 309 | &AAB8 | `osword_13_write_prot` | | |
| 310 | &AABB | `set_via_shadow_pair` | | |
| 311 | &AAC2 | `osword_13_read_handles` | | |
| 312 | &AAD0 | `osword_13_set_handles` | | |
| 313 | &AB43 | `update_fcb_flag_bits` | | |
| 314 | &AB68 | `osword_13_read_rx_flag` | | |
| 315 | &AB71 | `osword_13_read_rx_port` | | |
| 316 | &AB7F | `osword_13_read_error` | | |
| 317 | &AB82 | `store_a_to_pb_1` | | |
| 318 | &AB86 | `osword_13_read_context` | | |
| 319 | &AB8B | `osword_13_read_free_bufs` | | |
| 320 | &AB93 | `osword_13_read_ctx_3` | | |
| 321 | &AB9E | `osword_13_write_ctx_3` | | |
| 322 | &ABA9 | `osword_13_bridge_query` | | |
| 323 | &ABE9 | `init_bridge_poll` | | |
| 324 | &AC47 | `osword_14_handler` | | |
| 325 | &AC67 | `store_osword_pb_ptr` | | |
| 326 | &ACAD | `store_ptr_at_ws_y` | | |
| 327 | &ACF8 | `enable_irq_and_poll` | | |
| 328 | &ACFC | `netv_handler` | | |
| 329 | &AD15 | `push_osword_handler_addr` | | |
| 330 | &AD20 | `netv_dispatch_lo` | | |
| 331 | &AD29 | `netv_dispatch_hi` | | |
| 332 | &AD32 | `osword_4_handler` | | |
| 333 | &AD40 | `tx_econet_abort` | | |
| 334 | &AD64 | `netv_claim_release` | | |
| 335 | &ADB8 | `match_rx_code` | | |
| 336 | &ADC1 | `osword_claim_codes` | | |
| 337 | &ADD3 | `osword_8_handler` | | |
| 338 | &ADFE | `init_ws_copy_wide` | | |
| 339 | &AE07 | `init_ws_copy_narrow` | | |
| 340 | &AE0B | `ws_copy_vclr_entry` | | |
| 341 | &AE33 | `ws_txcb_template_data` | | |
| 342 | &AE5A | `netv_spool_check` | | |
| 343 | &AE64 | `reset_spool_buf_state` | | |
| 344 | &AE6F | `netv_print_data` | | |
| 345 | &AE94 | `append_byte_to_rxbuf` | | |
| 346 | &AE9D | `handle_spool_ctrl_byte` | | |
| 347 | &AEB8 | `process_spool_data` | | |
| 348 | &AF80 | `err_printer_busy` | | |
| 349 | &AFA6 | `send_disconnect_reply` | | |
| 350 | &B002 | `tx_econet_txcb_template` | | |
| 351 | &B01A | `lang_2_save_palette_vdu` | | |
| 352 | &B05F | `commit_state_byte` | | |
| 353 | &B066 | `serialise_palette_entry` | | |
| 354 | &B081 | `read_osbyte_to_ws_x0` | | |
| 355 | &B083 | `read_osbyte_to_ws` | | |
| 356 | &B0A1 | `cmd_cdir` | | |
| 357 | &B0D5 | `cdir_alloc_size_table` | | |
| 358 | &B0F2 | `cmd_lcat` | | |
| 359 | &B0F8 | `cmd_lex` | | |
| 360 | &B103 | `cmd_ex` | | |
| 361 | &B118 | `fscv_5_cat` | | |
| 362 | &B21A | `print_10_chars` | | |
| 363 | &B21C | `print_chars_from_buf` | | |
| 364 | &B22A | `parse_cmd_arg_y0` | | |
| 365 | &B22C | `parse_filename_arg` | | |
| 366 | &B22F | `parse_access_prefix` | | |
| 367 | &B251 | `strip_token_prefix` | | |
| 368 | &B29F | `copy_arg_to_buf_x0` | | |
| 369 | &B2A1 | `copy_arg_to_buf` | | |
| 370 | &B2A3 | `copy_arg_validated` | | |
| 371 | &B2CF | `mask_owner_access` | | |
| 372 | &B2E4 | `ex_print_col_sep` | | |
| 373 | &B303 | `print_decimal_3dig_no_spool` | | |
| 374 | &B310 | `print_decimal_digit_no_spool` | | |
| 375 | &B327 | `print_num_no_leading` | | |
| 376 | &B32A | `print_decimal_3dig` | | |
| 377 | &B338 | `print_decimal_digit` | | |
| 378 | &B373 | `save_ptr_to_os_text` | | |
| 379 | &B37F | `skip_to_next_arg` | | |
| 380 | &B393 | `save_ptr_to_spool_buf` | | |
| 381 | &B39E | `init_spool_drive` | | |
| 382 | &B3AC | `cmd_ps` | | |
| 383 | &B3D5 | `copy_ps_data_y1c` | | |
| 384 | &B3D7 | `copy_ps_data` | | |
| 385 | &B477 | `store_ps_station` | | |
| 386 | &B483 | `print_file_server_is` | | |
| 387 | &B48D | `print_printer_server_is` | | |
| 388 | &B4A8 | `load_ps_server_addr` | | |
| 389 | &B4B4 | `pop_requeue_ps_scan` | | |
| 390 | &B4D6 | `skip_next_ps_slot` | | |
| 391 | &B51C | `write_ps_slot_byte_ff` | | |
| 392 | &B523 | `write_two_bytes_inc_y` | | |
| 393 | &B52B | `reverse_ps_name_to_tx` | | |
| 394 | &B556 | `print_station_addr` | | |
| 395 | &B575 | `ps_slot_txcb_template` | | |
| 396 | &B581 | `cmd_pollps` | | |
| 397 | &B6A6 | `init_ps_slot_from_rx` | | |
| 398 | &B6BD | `store_char_uppercase` | | |
| 399 | &B6D2 | `cmd_prot` | | |
| 400 | &B6D6 | `cmd_unprot` | | |
| 401 | &B6F3 | `cmd_wipe` | | |
| 402 | &B703 | `request_next_wipe` | | |
| 403 | &B7CB | `prompt_yn` | | |
| 404 | &B7D3 | `flush_and_read_char` | | |
| 405 | &B7E3 | `init_channel_table` | | |
| 406 | &B805 | `attr_to_chan_index` | | |
| 407 | &B814 | `check_chan_char` | | |
| 408 | &B81C | `err_net_chan_invalid` | | |
| 409 | &B847 | `lookup_chan_by_char` | | |
| 410 | &B886 | `store_result_check_dir` | | |
| 411 | &B88C | `check_not_dir` | | |
| 412 | &B8A8 | `alloc_fcb_slot` | | |
| 413 | &B8DC | `alloc_fcb_or_error` | | |
| 414 | &B8F8 | `close_all_net_chans` | | |
| 415 | &B8FC | `scan_fcb_flags` | | |
| 416 | &B925 | `match_station_net` | | |
| 417 | &B934 | `find_open_fcb` | | |
| 418 | &B977 | `init_wipe_counters` | | |
| 419 | &B99A | `start_wipe_pass` | | |
| 420 | &BA09 | `save_fcb_context` | | |
| 421 | &BAB7 | `loop_restore_workspace` | | |
| 422 | &BAC0 | `restore_catalog_entry` | | |
| 423 | &BACC | `loop_save_before_match` | | |
| 424 | &BACF | `find_matching_fcb` | | |
| 425 | &BB2A | `inc_fcb_byte_count` | | |
| 426 | &BB38 | `process_all_fcbs` | | |
| 427 | &BB68 | `bgetv_handler` | | |
| 428 | &BBE7 | `bputv_handler` | | |
| 429 | &BC65 | `done_inc_byte_count` | | |
| 430 | &BC74 | `flush_fcb_if_station_known` | | |
| 431 | &BC7C | `flush_fcb_with_init` | | |
| 432 | &BCBC | `send_wipe_request` | | |
| 433 | &BD15 | `send_and_receive` | | |
| 434 | &BD1B | `read_rx_attribute` | | |
| 435 | &BD20 | `store_rx_attribute` | | |
| 436 | &BD25 | `abort_if_escape` | | |
| 437 | &BD41 | `cmd_dump` | | |
| 438 | &BD59 | `loop_dump_line` | | |
| 439 | &BD79 | `loop_pop_stack_buf` | | |
| 440 | &BDBB | `loop_next_dump_col` | | |
| 441 | &BE01 | `print_dump_header` | | |
| 442 | &BE37 | `print_hex_and_space` | | |
| 443 | &BE42 | `parse_dump_range` | | |
| 444 | &BE4E | `loop_parse_hex_digit` | | |
| 445 | &BEAB | `init_dump_buffer` | | |
| 446 | &BF71 | `close_ws_file` | | |
| 447 | &BF78 | `open_file_for_read` | | |
| 448 | &BFBA | `advance_x_by_8` | | |
| 449 | &BFBD | `advance_x_by_4` | | |
| 450 | &BFC0 | `inx4` | | |
| 451 | &BFC5 | `rom_tail_padding` | | |
| 452 | &BFE6 | `hazel_idx_bases` | | |
