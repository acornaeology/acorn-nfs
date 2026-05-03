# 4.21_variant_1 annotation review

Progressive review of every subroutine: leaf routines first, working
up through the call graph. For each routine we check:

- Inline comments correspond to the actual operations and describe
  them one level of abstraction up (semantic, not mechanical).
- Label name is semantic and matches what the routine does.
- Subroutine title and description describe the purpose accurately,
  including how the routine is called.

Status legend:
- `[ ]` pending
- `[x]` reviewed (with brief notes)
- `[s]` skipped (trivial wrapper, no comments to fix)

## Pre-pass: stale-name sweep (done)

Mass-replace 125 stale `lXXXX` auto-name references in inline
comments with the user-given labels at their target addresses
(e.g. `l0f05` -> `fs_cmd_data`, `l1040` -> `fcb_flags`,
`l0f03` -> `fs_cmd_csd`). Commit `48d722b`.

Counts: 464 routines total. Distribution by depth: 0=226, 1=90,
2=34, 3=17, 4=18, 5=30, 6=14, 7=9, 8=5, 9=2, 10=3, 11=10, 12=3, 13=3.

## Depth 0 (226 routines)

- [x] `0x8045` `generate_event` (in=1, out=0) — split out dispatch_svc5 (&8048) and svc_5_unknown_irq (&804F) as their own subroutines; tightened generate_event description
- [x] `0x8070` `init_nmi_workspace` - Inline comments accurate; description matches code.
- [x] `0x809B` `nmi_rx_scout` - Inline comments accurate.
- [x] `0x81B8` `data_rx_setup` - Inline comments accurate.
- [x] `0x81C2` `nmi_data_rx` - Inline comments accurate.
- [x] `0x81D6` `nmi_data_rx_net` - Inline comments accurate.
- [x] `0x81EC` `nmi_data_rx_skip` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x81F7` `install_data_rx_handler` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x8223` `nmi_data_rx_bulk` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x82F8` `ack_tx_write_dest` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x8316` `nmi_ack_tx_src` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x833F` `advance_rx_buffer_ptr` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x83EB` `set_nmi_rx_scout` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x8400` `copy_scout_to_buffer` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x8448` `release_tube` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x848B` `imm_op_dispatch_lo` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x84BC` `rx_imm_machine_type` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x84F9` `imm_op_build_reply` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x852C` `advance_buffer_ptr` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x853B` `tx_done_dispatch_lo` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8540` `tx_done_jsr` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8563` `tx_done_halt` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x857A` `tx_done_continue` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8582` `tx_done_exit` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=3, out=0)
- [x] `0x85F1` `inactive_poll` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x85FC` `intoff_test_inactive` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x862C` `tx_bad_ctrl_error` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x8630` `tx_line_jammed` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x864A` `tx_prepare` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x867E` `tx_ctrl_dispatch_lo` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8686` `tx_ctrl_machine_type` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x868A` `tx_ctrl_peek` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x868E` `tx_ctrl_poke` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8690` `tx_ctrl_store_and_add` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8723` `tx_last_data` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x874B` `nmi_reply_scout` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x875F` `nmi_reply_cont` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8776` `nmi_reply_validate` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x87BE` `nmi_scout_ack_src` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x87CE` `data_tx_begin` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x87E3` `nmi_data_tx` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8886` `handshake_await_ack` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=0)
- [x] `0x8892` `nmi_final_ack` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x88A6` `nmi_final_ack_net` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x88DE` `tx_result_ok` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x88E2` `tx_result_fail` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x88F0` `rom_gap_88f0` - triaged: bounds checked, comments accurate
- [x] `0x898C` `adlc_full_reset` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=3, out=0)
- [x] `0x899B` `adlc_rx_listen` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=2, out=0)
- [x] `0x89A6` `wait_idle_and_reset` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x89D8` `rom_set_nmi_vector` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x89ED` `svc_dispatch_lo` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8A20` `svc_dispatch_hi` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=0, out=0)
- [x] `0x8B00` `scan_remote_keys` - triaged: bounds correct, comments accurate, internal labels are branch-target helpers (in=1, out=1)
- [x] `0x8B18` `save_text_ptr` - triaged: bounds checked, comments accurate
- [x] `0x8B45` `svc_18_fs_select` - triaged: bounds checked, comments accurate
- [x] `0x8B4D` `ensure_fs_selected` - triaged: bounds checked, comments accurate
- [x] `0x8BC0` `help_utils` - triaged: bounds checked, comments accurate
- [x] `0x8BC4` `help_net` - triaged: bounds checked, comments accurate
- [x] `0x8BD5` `print_cmd_table_loop` - triaged: bounds checked, comments accurate
- [x] `0x8C25` `done_print_table` - triaged: bounds checked, comments accurate
- [x] `0x8C29` `help_wrap_if_serial` - triaged: bounds checked, comments accurate
- [x] `0x8CAD` `get_ws_page` - triaged: bounds checked, comments accurate
- [x] `0x8CFD` `notify_new_fs` - triaged: bounds checked, comments accurate
- [x] `0x8CFF` `call_fscv` - triaged: bounds checked, comments accurate
- [x] `0x8D02` `issue_svc_15` - triaged: bounds checked, comments accurate
- [x] `0x8D24` `check_credits_easter_egg` - triaged: bounds checked, comments accurate
- [x] `0x8E5B` `dir_op_dispatch` - triaged: bounds checked, comments accurate
- [x] `0x8E61` `svc_dispatch` - triaged: bounds checked, comments accurate
- [x] `0x8E71` `noop_dey_rts` - triaged: bounds checked, comments accurate
- [x] `0x8E73` `copy_template_to_zp` - triaged: bounds checked, comments accurate
- [x] `0x8E7F` `fs_info_template` - triaged: bounds checked, comments accurate
- [x] `0x8E98` `read_cmos_byte_0` - triaged: bounds checked, comments accurate
- [x] `0x8E9A` `osbyte_a1` - triaged: bounds checked, comments accurate
- [x] `0x8EA7` `fs_vector_table` - triaged: bounds checked, comments accurate
- [x] `0x8EC9` `osbyte_x0` - triaged: bounds checked, comments accurate
- [x] `0x8ECB` `osbyte_yff` - triaged: bounds checked, comments accurate
- [x] `0x8ED2` `osbyte_x0_y0` - triaged: bounds checked, comments accurate
- [x] `0x8EE9` `raise_y_to_c8` - triaged: bounds checked, comments accurate
- [x] `0x8EF0` `store_ws_page_count` - triaged: bounds checked, comments accurate
- [x] `0x904F` `write_vector_entry` - triaged: bounds checked, comments accurate
- [x] `0x9064` `restore_fs_context` - triaged: bounds checked, comments accurate
- [x] `0x909E` `verify_ws_checksum` - triaged: bounds checked, comments accurate
- [x] `0x91F9` `print_newline_no_spool` - triaged: bounds checked, comments accurate
- [x] `0x91FB` `print_char_no_spool` - triaged: bounds checked, comments accurate
- [x] `0x9201` `print_byte_no_spool` - triaged: bounds checked, comments accurate
- [x] `0x923F` `print_hex_nybble` - triaged: bounds checked, comments accurate
- [x] `0x9255` `print_hex_nybble_no_spool` - triaged: bounds checked, comments accurate
- [x] `0x9261` `print_inline` - triaged: bounds checked, comments accurate
- [x] `0x9269` `loop_next_char` - triaged: bounds checked, comments accurate
- [x] `0x939A` `is_decimal_digit` - triaged: bounds checked, comments accurate
- [x] `0x93A2` `is_dec_digit_only` - triaged: bounds checked, comments accurate
- [x] `0x93AB` `get_access_bits` - triaged: bounds checked, comments accurate
- [x] `0x93B5` `get_prot_bits` - triaged: bounds checked, comments accurate
- [x] `0x93C8` `prot_bit_encode_table` - triaged: bounds checked, comments accurate
- [x] `0x93D3` `set_text_and_xfer_ptr` - triaged: bounds checked, comments accurate
- [x] `0x93D7` `set_xfer_params` - triaged: bounds checked, comments accurate
- [x] `0x93DD` `set_options_ptr` - triaged: bounds checked, comments accurate
- [x] `0x93E1` `clear_escapable` - triaged: bounds checked, comments accurate
- [x] `0x93E6` `cmp_5byte_handle` - triaged: bounds checked, comments accurate
- [x] `0x93F2` `fscv_7_read_handles` - triaged: bounds correct (in=0, out=0)
- [x] `0x9446` `check_not_ampersand` - triaged: bounds correct (in=2, out=0)
- [x] `0x9463` `copy_fs_cmd_name` - triaged: bounds correct (in=2, out=0)
- [x] `0x9612` `osbyte_a2` - triaged: bounds correct (in=2, out=1)
- [x] `0x962B` `osbyte_a2_value_tya` - triaged: bounds correct (in=0, out=0)
- [x] `0x973D` `init_txcb_bye` - triaged: bounds correct (in=1, out=0)
- [x] `0x974B` `init_txcb` - triaged: bounds correct (in=4, out=0)
- [x] `0x9763` `txcb_init_template` - triaged: bounds correct (in=0, out=0)
- [x] `0x976F` `send_request_nowrite` - triaged: bounds correct (in=1, out=0)
- [x] `0x9773` `send_request_write` - triaged: bounds correct (in=2, out=0)
- [x] `0x978A` `save_net_tx_cb` - triaged: bounds correct (in=15, out=0)
- [x] `0x978B` `save_net_tx_cb_vset` - triaged: bounds correct (in=2, out=0)
- [x] `0x988F` `check_escape_and_classify` - triaged: bounds correct (in=2, out=0)
- [x] `0x989F` `lang_4_validated` - triaged: bounds correct (in=0, out=0)
- [x] `0x98BE` `wait_net_tx_ack` - triaged: bounds correct (in=6, out=0)
- [x] `0x9930` `fixup_reply_status_a` - triaged: bounds correct (in=1, out=0)
- [x] `0x993B` `load_reply_and_classify` - triaged: bounds correct (in=1, out=0)
- [x] `0x99C3` `error_inline` - triaged: bounds correct (in=4, out=0)
- [x] `0x9A5E` `append_space_and_num` - triaged: bounds correct (in=2, out=0)
- [x] `0x9A7A` `append_decimal_digit` - triaged: bounds correct (in=1, out=0)
- [x] `0x9A9A` `net_error_lookup_data` - triaged: bounds correct (in=0, out=0)
- [x] `0x9AA6` `error_msg_table` - triaged: bounds correct (in=0, out=0)
- [x] `0x9B24` `init_tx_ptr_and_send` - triaged: bounds correct (in=2, out=0)
- [x] `0x9B75` `pass_txbuf_init_table` - triaged: bounds correct (in=0, out=0)
- [x] `0x9B81` `init_tx_ptr_for_pass` - triaged: bounds correct (in=1, out=0)
- [x] `0x9BF5` `load_text_ptr_and_parse` - triaged: bounds checked, comments accurate
- [x] `0x9C00` `gsread_to_buf` - triaged: bounds checked, comments accurate
- [x] `0x9D5F` `copy_fsopts_to_zp` - triaged: bounds checked, comments accurate
- [x] `0x9D6B` `skip_one_and_advance5` - triaged: bounds checked, comments accurate
- [x] `0x9D6C` `advance_y_by_4` - triaged: bounds checked, comments accurate
- [x] `0x9D71` `copy_workspace_to_fsopts` - triaged: bounds checked, comments accurate
- [x] `0x9D7E` `retreat_y_by_4` - triaged: bounds checked, comments accurate
- [x] `0x9D7F` `retreat_y_by_3` - triaged: bounds checked, comments accurate
- [x] `0x9E82` `format_filename_field` - triaged: bounds checked, comments accurate
- [x] `0x9FB4` `return_with_last_flag` - triaged: bounds checked, comments accurate
- [x] `0x9FC2` `osfind_close_or_open` - triaged: bounds checked, comments accurate
- [x] `0xA103` `cmos_opt_mask_table` - triaged: bounds checked, comments accurate
- [x] `0xA131` `update_addr_from_offset1` - triaged: bounds checked, comments accurate
- [x] `0xA133` `add_workspace_to_fsopts` - triaged: bounds checked, comments accurate
- [x] `0xA145` `store_adjusted_byte` - triaged: bounds checked, comments accurate
- [x] `0xA1EF` `lookup_cat_entry_0` - triaged: bounds checked, comments accurate
- [x] `0xA390` `tube_claim_c3` - triaged: bounds checked, comments accurate
- [x] `0xA3E7` `get_pb_ptr_as_index` - triaged: bounds checked, comments accurate
- [x] `0xA3E9` `byte_to_2bit_index` - triaged: bounds checked, comments accurate
- [x] `0xA3FF` `net_1_read_handle` - triaged: bounds checked, comments accurate
- [x] `0xA45B` `match_fs_cmd` - triaged: bounds checked, comments accurate
- [x] `0xA764` `boot_cmd_oscli` - triaged: bounds checked, comments accurate
- [x] `0xA76C` `cmd_table_fs` - triaged: bounds checked, comments accurate
- [x] `0xA864` `osword_setup_handler` - triaged: bounds checked, comments accurate
- [x] `0xA901` `bin_to_bcd` - triaged: bounds checked, comments accurate
- [x] `0xA9A8` `osword_13_dispatch_lo` - triaged: bounds correct (in=0, out=0)
- [x] `0xA9BA` `osword_13_dispatch_hi` - triaged: bounds correct (in=0, out=0)
- [x] `0xAA72` `osword_13_read_csd` - triaged: bounds correct (in=0, out=0)
- [x] `0xAA75` `osword_13_write_csd` - triaged: bounds correct (in=0, out=0)
- [x] `0xAA82` `copy_pb_byte_to_ws` - triaged: bounds correct (in=2, out=0)
- [x] `0xAA91` `osword_13_read_ws_pair` - triaged: bounds correct (in=0, out=0)
- [x] `0xAAB8` `osword_13_write_prot` - Description was stale ('store_prot_mask'); rewrote to reference set_via_shadow_pair fall-through.
- [x] `0xAABB` `set_via_shadow_pair` - triaged: bounds correct (in=2, out=0)
- [x] `0xAB43` `update_fcb_flag_bits` - triaged: bounds correct (in=1, out=0)
- [x] `0xAB71` `osword_13_read_rx_port` - triaged: bounds correct (in=0, out=0)
- [x] `0xAB7F` `osword_13_read_error` - Description referenced &0E09 fs_last_error but code reads hazel_fs_last_error (&C009); fixed.
- [x] `0xAB82` `store_a_to_pb_1` - triaged: bounds correct (in=2, out=0)
- [x] `0xAB86` `osword_13_read_context` - Description completely wrong (claimed tx_retry_count); fixed to reference hazel_fs_error_code.
- [x] `0xAB8B` `osword_13_read_free_bufs` - triaged: bounds correct (in=0, out=0)
- [x] `0xAB93` `osword_13_read_ctx_3` - triaged: bounds correct (in=0, out=0)
- [x] `0xAB9E` `osword_13_write_ctx_3` - triaged: bounds correct (in=0, out=0)
- [x] `0xACAD` `store_ptr_at_ws_y` - triaged: bounds correct (in=1, out=0)
- [x] `0xAD15` `push_osword_handler_addr` - triaged: bounds correct (in=1, out=0)
- [x] `0xAD20` `netv_dispatch_lo` - triaged: bounds correct (in=0, out=0)
- [x] `0xAD29` `netv_dispatch_hi` - triaged: bounds correct (in=0, out=0)
- [x] `0xAD32` `osword_4_handler` - triaged: bounds correct (in=0, out=0)
- [x] `0xADB8` `match_rx_code` - triaged: bounds correct (in=1, out=0)
- [x] `0xADC1` `osword_claim_codes` - triaged: bounds correct (in=0, out=0)
- [x] `0xADFE` `init_ws_copy_wide` - triaged: bounds correct (in=2, out=0)
- [x] `0xAE07` `init_ws_copy_narrow` - triaged: bounds correct (in=1, out=0)
- [x] `0xAE0B` `ws_copy_vclr_entry` - triaged: bounds correct (in=1, out=0)
- [x] `0xAE33` `ws_txcb_template_data` - triaged: bounds correct (in=0, out=0)
- [x] `0xAE5A` `netv_spool_check` - triaged: bounds correct (in=0, out=0)
- [x] `0xAE64` `reset_spool_buf_state` - triaged: bounds correct (in=2, out=0)
- [x] `0xAE94` `append_byte_to_rxbuf` - triaged: bounds correct (in=3, out=0)
- [x] `0xB002` `tx_econet_txcb_template` - triaged: bounds correct (in=0, out=0)
- [x] `0xB05F` `commit_state_byte` - triaged: bounds correct (in=4, out=0)
- [x] `0xB081` `read_osbyte_to_ws_x0` - triaged: bounds correct (in=1, out=0)
- [x] `0xB083` `read_osbyte_to_ws` - triaged: bounds correct (in=0, out=1)
- [x] `0xB0D5` `cdir_alloc_size_table` - triaged: bounds correct (in=0, out=0)
- [x] `0xB0F2` `cmd_lcat` - triaged: bounds correct (in=0, out=0)
- [x] `0xB103` `cmd_ex` - triaged: bounds correct (in=0, out=0)
- [x] `0xB21A` `print_10_chars` - triaged: bounds correct (in=1, out=0)
- [x] `0xB22A` `parse_cmd_arg_y0` - triaged: bounds correct (in=3, out=0)
- [x] `0xB29F` `copy_arg_to_buf_x0` - triaged: bounds correct (in=5, out=0)
- [x] `0xB2A1` `copy_arg_to_buf` - triaged: bounds correct (in=8, out=0)
- [x] `0xB2A3` `copy_arg_validated` - triaged: bounds correct (in=2, out=0)
- [x] `0xB2CF` `mask_owner_access` - triaged: bounds correct (in=12, out=0)
- [x] `0xB327` `print_num_no_leading` - triaged: bounds correct (in=4, out=0)
- [x] `0xB373` `save_ptr_to_os_text` - triaged: bounds correct (in=9, out=0)
- [x] `0xB37F` `skip_to_next_arg` - triaged: bounds correct (in=1, out=0)
- [x] `0xB393` `save_ptr_to_spool_buf` - triaged: bounds correct (in=2, out=0)
- [x] `0xB3D5` `copy_ps_data_y1c` - triaged: bounds correct (in=1, out=0)
- [x] `0xB477` `store_ps_station` - triaged: bounds correct (in=1, out=0)
- [x] `0xB4A8` `load_ps_server_addr` - triaged: bounds correct (in=3, out=0)
- [x] `0xB51C` `write_ps_slot_byte_ff` - triaged: bounds correct (in=1, out=0)
- [x] `0xB523` `write_two_bytes_inc_y` - triaged: bounds correct (in=1, out=0)
- [x] `0xB52B` `reverse_ps_name_to_tx` - triaged: bounds correct (in=2, out=0)
- [x] `0xB575` `ps_slot_txcb_template` - triaged: bounds correct (in=0, out=0)
- [x] `0xB6A6` `init_ps_slot_from_rx` - triaged: bounds correct (in=1, out=0)
- [x] `0xB6BD` `store_char_uppercase` - triaged: bounds correct (in=2, out=0)
- [x] `0xB6D2` `cmd_prot` - triaged: bounds correct (in=0, out=0)
- [x] `0xB7E3` `init_channel_table` - triaged: bounds correct (in=1, out=0)
- [x] `0xB805` `attr_to_chan_index` - triaged: bounds correct (in=4, out=0)
- [x] `0xB814` `check_chan_char` - triaged: bounds correct (in=2, out=0)
- [x] `0xB8A8` `alloc_fcb_slot` - triaged: bounds correct (in=6, out=0)
- [x] `0xB8F8` `close_all_net_chans` - triaged: bounds correct (in=3, out=0)
- [x] `0xB925` `match_station_net` - triaged: bounds correct (in=7, out=0)
- [x] `0xB934` `find_open_fcb` - triaged: bounds correct (in=2, out=0)
- [x] `0xB977` `init_wipe_counters` - triaged: bounds checked, comments accurate
- [x] `0xBAB7` `loop_restore_workspace` - triaged: bounds checked, comments accurate
- [x] `0xBAC0` `restore_catalog_entry` - triaged: bounds checked, comments accurate
- [x] `0xBB2A` `inc_fcb_byte_count` - triaged: bounds checked, comments accurate
- [x] `0xBC74` `flush_fcb_if_station_known` - triaged: bounds checked, comments accurate
- [x] `0xBD1B` `read_rx_attribute` - triaged: bounds checked, comments accurate
- [x] `0xBD20` `store_rx_attribute` - triaged: bounds checked, comments accurate
- [x] `0xBE42` `parse_dump_range` - triaged: bounds checked, comments accurate
- [x] `0xBF71` `close_ws_file` - triaged: bounds checked, comments accurate
- [x] `0xBFC0` `inx4` - triaged: bounds checked, comments accurate
- [x] `0xBFC5` `rom_tail_padding` - triaged: bounds checked, comments accurate
- [x] `0xBFE6` `hazel_idx_bases` - triaged: bounds checked, comments accurate

## Depth 1 (90 routines)

- [x] `0x8028` `svc5_irq_check` - triaged: bounds correct, comments accurate
- [x] `0x8050` `adlc_init` - triaged: bounds correct, comments accurate
- [x] `0x80B8` `nmi_rx_scout_net` - triaged: bounds correct, comments accurate
- [x] `0x81A7` `send_data_rx_ack` - triaged: bounds correct, comments accurate
- [x] `0x8291` `nmi_data_rx_tube` - triaged: bounds correct, comments accurate
- [x] `0x82DF` `ack_tx` - triaged: bounds correct, comments accurate
- [x] `0x8386` `nmi_post_ack_dispatch` - triaged: bounds correct, comments accurate
- [x] `0x83E8` `reset_adlc_rx_listen` - triaged: bounds correct, comments accurate
- [x] `0x83F2` `discard_reset_listen` - triaged: bounds correct, comments accurate
- [x] `0x8549` `tx_done_econet_event` - triaged: bounds correct, comments accurate
- [x] `0x8557` `tx_done_os_proc` - triaged: bounds correct, comments accurate
- [x] `0x8589` `tx_begin` - triaged: bounds correct, comments accurate
- [x] `0x872F` `nmi_tx_complete` - triaged: bounds correct, comments accurate
- [x] `0x8773` `reject_reply` - triaged: bounds correct, comments accurate
- [x] `0x88BA` `nmi_final_ack_validate` - triaged: bounds correct, comments accurate
- [x] `0x8900` `tx_calc_transfer` - triaged: bounds correct, comments accurate
- [x] `0x89B9` `save_econet_state` - triaged: bounds correct, comments accurate
- [x] `0x89CA` `nmi_bootstrap_entry` - triaged: bounds correct, comments accurate
- [x] `0x8A54` `service_handler` - triaged: bounds correct, comments accurate
- [x] `0x8B23` `cmd_net_fs` - triaged: bounds correct, comments accurate
- [x] `0x8BD8` `loop_next_entry` - triaged: bounds correct, comments accurate
- [x] `0x8CBD` `setup_ws_ptr` - triaged: bounds correct, comments accurate
- [x] `0x8D09` `svc_dispatch_idx_2` - triaged: bounds correct, comments accurate
- [x] `0x8DD5` `cmd_pass` - triaged: bounds correct, comments accurate
- [x] `0x8E3C` `send_cmd_and_dispatch` - triaged: bounds correct, comments accurate
- [x] `0x8E8A` `svc_26_close_all_files` - triaged: bounds correct, comments accurate
- [x] `0x8ED8` `svc_7_osbyte` - triaged: bounds correct, comments accurate
- [x] `0x8F10` `svc_2_priv_ws` - triaged: bounds correct, comments accurate
- [x] `0x90C7` `print_station_id` - triaged: bounds correct, comments accurate
- [x] `0x9236` `print_hex_byte` - triaged: bounds correct, comments accurate
- [x] `0x924C` `print_hex_byte_no_spool` - triaged: bounds correct, comments accurate
- [x] `0x928A` `print_inline_no_spool` - triaged: bounds correct, comments accurate
- [x] `0x92B2` `parse_addr_arg` - triaged: bounds correct, comments accurate
- [x] `0x93F7` `set_conn_active` - triaged: bounds correct, comments accurate
- [x] `0x940D` `clear_conn_active` - triaged: bounds correct, comments accurate
- [x] `0x95C1` `print_station_low` - triaged: bounds correct, comments accurate
- [x] `0x95C8` `print_fs_station` - triaged: bounds correct, comments accurate
- [x] `0x95DA` `print_dir_syntax` - triaged: bounds correct, comments accurate
- [x] `0x9619` `cmd_space` - triaged: bounds correct, comments accurate
- [x] `0x9623` `cmd_nospace` - triaged: bounds correct, comments accurate
- [x] `0x965F` `print_ps_address` - triaged: bounds correct, comments accurate
- [x] `0x973F` `init_txcb_port` - triaged: bounds correct, comments accurate
- [x] `0x97B7` `prep_send_tx_cb` - triaged: bounds correct, comments accurate
- [x] `0x9850` `lang_1_remote_boot` - triaged: bounds correct, comments accurate
- [x] `0x98AF` `lang_0_insert_key` - triaged: bounds correct, comments accurate
- [x] `0x99DF` `check_net_error_code` - triaged: bounds correct, comments accurate
- [x] `0x9A69` `append_decimal_num` - triaged: bounds correct, comments accurate
- [x] `0x9FB6` `finalise_and_return` - triaged: bounds correct, comments accurate
- [x] `0xA12C` `update_addr_from_offset9` - triaged: bounds correct, comments accurate
- [x] `0xA134` `adjust_fsopts_4bytes` - triaged: bounds correct, comments accurate
- [x] `0xA28A` `send_osbput_data` - triaged: bounds correct, comments accurate
- [x] `0xA2ED` `write_data_block` - triaged: bounds correct, comments accurate
- [x] `0xA405` `net_2_read_entry` - triaged: bounds correct, comments accurate
- [x] `0xA415` `net_3_close_handle` - triaged: bounds correct, comments accurate
- [x] `0xA42F` `fscv_3_star_cmd` - triaged: bounds correct, comments accurate
- [x] `0xA440` `cmd_fs_reentry` - triaged: bounds correct, comments accurate
- [x] `0xA4E4` `fscv_2_star_run` - triaged: bounds correct, comments accurate
- [x] `0xA644` `find_station_bit2` - triaged: bounds correct, comments accurate
- [x] `0xA66F` `find_station_bit3` - triaged: bounds correct, comments accurate
- [x] `0xA6A6` `flip_set_station_boot` - triaged: bounds correct, comments accurate
- [x] `0xA6D5` `fsreply_1_boot` - triaged: bounds correct, comments accurate
- [x] `0xA83B` `svc_8_osword` - triaged: bounds correct, comments accurate
- [x] `0xA877` `extract_osword_subcode` - triaged: bounds correct, comments accurate
- [x] `0xA985` `osword_12_handler` - triaged: bounds correct, comments accurate
- [x] `0xA9CC` `osword_13_read_station` - triaged: bounds correct, comments accurate
- [x] `0xAAB2` `osword_13_read_prot` - triaged: bounds correct, comments accurate
- [x] `0xAAC2` `osword_13_read_handles` - triaged: bounds correct, comments accurate
- [x] `0xAAD0` `osword_13_set_handles` - triaged: bounds correct, comments accurate
- [x] `0xAB68` `osword_13_read_rx_flag` - triaged: bounds correct, comments accurate
- [x] `0xAC47` `osword_14_handler` - triaged: bounds correct, comments accurate
- [x] `0xACED` `handle_burst_xfer` - triaged: bounds correct, comments accurate
- [x] `0xACFC` `netv_handler` - triaged: bounds correct, comments accurate
- [x] `0xB066` `serialise_palette_entry` - triaged: bounds correct, comments accurate
- [x] `0xB0F8` `cmd_lex` - triaged: bounds correct, comments accurate
- [x] `0xB21C` `print_chars_from_buf` - triaged: bounds correct, comments accurate
- [x] `0xB22C` `parse_filename_arg` - triaged: bounds correct, comments accurate
- [x] `0xB310` `print_decimal_digit_no_spool` - triaged: bounds correct, comments accurate
- [x] `0xB39E` `init_spool_drive` - triaged: bounds correct, comments accurate
- [x] `0xB483` `print_file_server_is` - triaged: bounds correct, comments accurate
- [x] `0xB48D` `print_printer_server_is` - triaged: bounds correct, comments accurate
- [x] `0xB4B4` `pop_requeue_ps_scan` - triaged: bounds correct, comments accurate
- [x] `0xB4D6` `skip_next_ps_slot` - triaged: bounds correct, comments accurate
- [x] `0xB6D6` `cmd_unprot` - triaged: bounds correct, comments accurate
- [x] `0xB847` `lookup_chan_by_char` - triaged: bounds correct, comments accurate
- [x] `0xB886` `store_result_check_dir` - triaged: bounds correct, comments accurate
- [x] `0xB8FC` `scan_fcb_flags` - triaged: bounds correct, comments accurate
- [x] `0xBC65` `done_inc_byte_count` - triaged: bounds correct, comments accurate
- [x] `0xBD25` `abort_if_escape` - triaged: bounds correct, comments accurate
- [x] `0xBF78` `open_file_for_read` - triaged: bounds correct, comments accurate
- [x] `0xBFBD` `advance_x_by_4` - triaged: bounds correct, comments accurate

## Depth 2 (34 routines)

- [ ] `0x80D8` `scout_error` (in=0, out=3)
- [ ] `0x8195` `port_match_found` (in=1, out=2)
- [ ] `0x8268` `data_rx_complete` (in=0, out=1)
- [ ] `0x83E5` `discard_reset_rx` (in=3, out=1)
- [ ] `0x8493` `rx_imm_exec` (in=0, out=1)
- [ ] `0x84CE` `rx_imm_peek` (in=0, out=2)
- [ ] `0x8512` `setup_sr_tx` (in=1, out=1)
- [ ] `0x86A2` `tx_ctrl_proc` (in=0, out=1)
- [ ] `0x8C06` `loop_print_syntax` (in=0, out=4)
- [ ] `0x8C42` `svc_4_star_command` (in=0, out=3)
- [ ] `0x8C93` `print_version_header` (in=2, out=2)
- [ ] `0x903C` `init_adlc_and_vectors` (in=2, out=2)
- [ ] `0x945E` `send_fs_request` (in=1, out=1)
- [ ] `0x9A3A` `append_drv_dot_num` (in=2, out=1)
- [ ] `0x9BB6` `poll_adlc_tx_status` (in=2, out=1)
- [ ] `0x9D4F` `print_5_hex_bytes` (in=2, out=2)
- [ ] `0x9D87` `check_and_setup_txcb` (in=2, out=4)
- [ ] `0xA1F3` `lookup_cat_slot_data` (in=1, out=1)
- [ ] `0xA29F` `write_block_entry` (in=1, out=1)
- [ ] `0xA638` `fsreply_3_set_csd` (in=1, out=2)
- [ ] `0xA63E` `fsreply_5_set_lib` (in=0, out=2)
- [ ] `0xA69A` `cmd_flip` (in=0, out=1)
- [ ] `0xA6E5` `fsreply_2_copy_handles` (in=0, out=7)
- [ ] `0xA910` `osword_10_handler` (in=0, out=3)
- [ ] `0xB01A` `lang_2_save_palette_vdu` (in=0, out=2)
- [ ] `0xB0A1` `cmd_cdir` (in=0, out=7)
- [ ] `0xB2E4` `ex_print_col_sep` (in=1, out=2)
- [ ] `0xB303` `print_decimal_3dig_no_spool` (in=1, out=1)
- [ ] `0xB338` `print_decimal_digit` (in=1, out=6)
- [ ] `0xB6F3` `cmd_wipe` (in=0, out=3)
- [ ] `0xB7CB` `prompt_yn` (in=1, out=1)
- [ ] `0xBD59` `loop_dump_line` (in=1, out=2)
- [ ] `0xBE37` `print_hex_and_space` (in=2, out=2)
- [ ] `0xBFBA` `advance_x_by_8` (in=3, out=1)

## Depth 3 (17 routines)

- [ ] `0x8215` `nmi_error_dispatch` (in=3, out=3)
- [ ] `0x8395` `rx_complete_update_rxcb` (in=1, out=3)
- [ ] `0x84B1` `rx_imm_poke` (in=0, out=1)
- [ ] `0x8845` `nmi_data_tx_tube` (in=0, out=1)
- [ ] `0x88E4` `tx_store_result` (in=1, out=1)
- [ ] `0x8BC6` `print_cmd_table` (in=1, out=2)
- [ ] `0x8C51` `svc_9_help` (in=0, out=3)
- [ ] `0x9900` `cond_save_error_code` (in=4, out=3)
- [ ] `0x9B2C` `send_net_packet` (in=6, out=4)
- [ ] `0x9B89` `setup_pass_txbuf` (in=1, out=2)
- [ ] `0x9CB5` `setup_dir_display` (in=1, out=6)
- [ ] `0x9D44` `print_load_exec_addrs` (in=1, out=1)
- [ ] `0xABE9` `init_bridge_poll` (in=5, out=3)
- [ ] `0xB118` `fscv_5_cat` (in=0, out=14)
- [ ] `0xB32A` `print_decimal_3dig` (in=1, out=1)
- [ ] `0xB703` `request_next_wipe` (in=0, out=8)
- [ ] `0xBE01` `print_dump_header` (in=2, out=2)

## Depth 4 (18 routines)

- [ ] `0x832D` `post_ack_scout` (in=0, out=2)
- [ ] `0x8409` `save_acccon_for_shadow_ram` (in=0, out=2)
- [ ] `0x8454` `immediate_op` (in=1, out=1)
- [ ] `0x86E7` `nmi_tx_data` (in=0, out=1)
- [ ] `0x8BBB` `help_print_nfs_cmds` (in=1, out=1)
- [ ] `0x8E21` `clear_if_station_match` (in=2, out=1)
- [ ] `0x993D` `classify_reply_error` (in=2, out=2)
- [ ] `0x99A7` `error_bad_inline` (in=7, out=1)
- [ ] `0x99C0` `error_inline_log` (in=9, out=1)
- [ ] `0x9DDC` `dispatch_osword_op` (in=1, out=10)
- [ ] `0xA3C4` `parse_fs_ps_args` (in=4, out=2)
- [ ] `0xAA9D` `osword_13_write_ws_pair` (in=0, out=1)
- [ ] `0xABA9` `osword_13_bridge_query` (in=0, out=1)
- [ ] `0xACF8` `enable_irq_and_poll` (in=2, out=1)
- [ ] `0xAD40` `tx_econet_abort` (in=3, out=1)
- [ ] `0xAFA6` `send_disconnect_reply` (in=3, out=3)
- [ ] `0xB556` `print_station_addr` (in=2, out=3)
- [ ] `0xBD79` `loop_pop_stack_buf` (in=1, out=5)

## Depth 5 (30 routines)

- [ ] `0x8112` `scout_complete` (in=0, out=2)
- [ ] `0x8AEA` `cmd_roff` (in=0, out=2)
- [ ] `0x8C64` `svc_return_unclaimed` (in=2, out=3)
- [ ] `0x8DA6` `load_transfer_params` (in=0, out=5)
- [ ] `0x90B5` `error_net_checksum` (in=1, out=1)
- [ ] `0x934A` `err_bad_hex` (in=1, out=1)
- [ ] `0x9437` `error_bad_filename` (in=2, out=1)
- [ ] `0x9483` `parse_quoted_arg` (in=2, out=1)
- [ ] `0x95EE` `set_fs_or_ps_cmos_station` (in=0, out=3)
- [ ] `0x97CD` `recv_and_process_reply` (in=2, out=6)
- [ ] `0x987E` `lang_3_exec_0100` (in=0, out=2)
- [ ] `0x9895` `raise_escape_error` (in=1, out=2)
- [ ] `0x9C85` `send_txcb_swap_addrs` (in=2, out=3)
- [ ] `0xA0A9` `fscv_0_opt_entry` (in=0, out=4)
- [ ] `0xA398` `cmd_fs` (in=0, out=3)
- [ ] `0xA3BB` `print_fs_info_newline` (in=1, out=2)
- [ ] `0xA5A1` `error_bad_command` (in=1, out=1)
- [ ] `0xA5AE` `check_exec_addr` (in=1, out=1)
- [ ] `0xAC67` `store_osword_pb_ptr` (in=0, out=3)
- [ ] `0xACB7` `handle_tx_request` (in=0, out=2)
- [ ] `0xAD64` `netv_claim_release` (in=0, out=2)
- [ ] `0xADD3` `osword_8_handler` (in=0, out=1)
- [ ] `0xAEB8` `process_spool_data` (in=3, out=7)
- [ ] `0xAF80` `err_printer_busy` (in=1, out=1)
- [ ] `0xB81C` `err_net_chan_invalid` (in=1, out=1)
- [ ] `0xB88C` `check_not_dir` (in=2, out=2)
- [ ] `0xB8DC` `alloc_fcb_or_error` (in=2, out=2)
- [ ] `0xBCBC` `send_wipe_request` (in=2, out=3)
- [ ] `0xBDBB` `loop_next_dump_col` (in=0, out=6)
- [ ] `0xBEAB` `init_dump_buffer` (in=1, out=6)

## Depth 6 (14 routines)

- [ ] `0x8B52` `select_fs_via_cmd_net_fs` (in=1, out=9)
- [ ] `0x9670` `print_fs_address` (in=1, out=5)
- [ ] `0x9D0C` `recv_reply` (in=1, out=7)
- [ ] `0x9FCF` `clear_result` (in=1, out=3)
- [ ] `0xA284` `recv_reply_preserve_flags` (in=1, out=1)
- [ ] `0xA4A2` `loop_skip_trail_spaces` (in=0, out=1)
- [ ] `0xAE6F` `netv_print_data` (in=0, out=3)
- [ ] `0xAE9D` `handle_spool_ctrl_byte` (in=1, out=3)
- [ ] `0xB251` `strip_token_prefix` (in=4, out=2)
- [ ] `0xB3AC` `cmd_ps` (in=0, out=7)
- [ ] `0xB3D7` `copy_ps_data` (in=1, out=12)
- [ ] `0xB7D3` `flush_and_read_char` (in=0, out=3)
- [ ] `0xBD41` `cmd_dump` (in=0, out=3)
- [ ] `0xBE4E` `loop_parse_hex_digit` (in=0, out=2)

## Depth 7 (9 routines)

- [ ] `0x8CC7` `svc_3_autoboot` (in=0, out=5)
- [ ] `0x8F38` `nfs_init_body` (in=0, out=13)
- [ ] `0x944E` `read_filename_char` (in=1, out=2)
- [ ] `0x9630` `svc_29_status` (in=0, out=6)
- [ ] `0x9C3E` `do_fs_cmd_iteration` (in=1, out=6)
- [ ] `0xA1FA` `setup_transfer_workspace` (in=2, out=9)
- [ ] `0xA329` `tail_update_catalogue` (in=0, out=5)
- [ ] `0xB22F` `parse_access_prefix` (in=3, out=1)
- [ ] `0xB581` `cmd_pollps` (in=0, out=19)

## Depth 8 (5 routines)

- [ ] `0x9425` `cmd_fs_operation` (in=0, out=4)
- [ ] `0x94C5` `cmd_rename` (in=0, out=7)
- [ ] `0x9C22` `filev_handler` (in=0, out=6)
- [ ] `0xA5C3` `alloc_run_channel` (in=1, out=8)
- [ ] `0xBD15` `send_and_receive` (in=2, out=2)

## Depth 9 (2 routines)

- [ ] `0xA4F1` `cmd_run_via_urd` (in=1, out=10)
- [ ] `0xB99A` `start_wipe_pass` (in=2, out=5)

## Depth 10 (3 routines)

- [ ] `0x8E2D` `check_urd_prefix` (in=1, out=2)
- [ ] `0xBA09` `save_fcb_context` (in=2, out=8)
- [ ] `0xBB38` `process_all_fcbs` (in=8, out=1)

## Depth 11 (10 routines)

- [ ] `0x8D91` `cmd_iam` (in=0, out=2)
- [ ] `0x9071` `fscv_6_shutdown` (in=0, out=2)
- [ ] `0x9512` `cmd_dir` (in=0, out=12)
- [ ] `0x9776` `cmd_bye` (in=0, out=3)
- [ ] `0x9FB1` `close_all_fcbs` (in=1, out=1)
- [ ] `0x9FEE` `send_open_file_request` (in=1, out=14)
- [ ] `0xA14C` `gbpbv_handler` (in=0, out=14)
- [ ] `0xA9DA` `osword_13_set_station` (in=0, out=4)
- [ ] `0xBACC` `loop_save_before_match` (in=1, out=1)
- [ ] `0xBC7C` `flush_fcb_with_init` (in=1, out=4)

## Depth 12 (3 routines)

- [ ] `0x968E` `dispatch_help_command` (in=0, out=7)
- [ ] `0x9EAB` `argsv_handler` (in=0, out=14)
- [ ] `0xBACF` `find_matching_fcb` (in=3, out=3)

## Depth 13 (3 routines)

- [ ] `0xA10B` `fscv_1_eof` (in=0, out=2)
- [ ] `0xBB68` `bgetv_handler` (in=0, out=5)
- [ ] `0xBBE7` `bputv_handler` (in=0, out=6)


## Session 1 progress

Pre-pass + first batch of depth-0 leaves:
- Mass-swept 125 stale lXXXX auto-name references in inline comments.
- generate_event split into 3 subroutines (was masquerading as one
  6-instruction routine but actually 1 + 2 unrelated tenants).
- 5 NMI/RX leaves spot-checked: comments accurate.
- 3 OSWORD &13 sub-handlers had stale labels in their descriptions
  pointing at the wrong addresses; rewrote against the actual code.

- print_station_id had been swallowing two unrelated data tables
  (cmd_syntax_strings and cmd_syntax_table) because their bare
  label() calls didn't break the routine boundary. Promoted both
  to data_banner() declarations; print_station_id's extent shrank
  from &90C7-&91F8 down to &90C7-&90F7.
- Fixed a small wave of pre-HAZEL label refs in subroutine
  descriptions: cond_save_error_code, fscv_2_star_run,
  cmd_run_via_urd, fscv_5_cat, parse_access_prefix,
  mask_owner_access. Each had described pre-HAZEL labels
  (fs_last_error / fs_lib_flags) when the bodies actually access
  the &Cxxx HAZEL versions.
