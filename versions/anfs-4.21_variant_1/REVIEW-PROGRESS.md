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

- [x] `0x8045` `generate_event` - description compared against body, accurate
- [x] `0x8070` `init_nmi_workspace` - description compared against body, accurate
- [x] `0x809B` `nmi_rx_scout` - description compared against body, accurate
- [x] `0x81B8` `data_rx_setup` - description compared against body, accurate
- [x] `0x81C2` `nmi_data_rx` - description compared against body, accurate
- [x] `0x81D6` `nmi_data_rx_net` - description compared against body, accurate
- [x] `0x81EC` `nmi_data_rx_skip` - description matches body; refined inline comment at &81EC (was 'Skip control and port bytes' but BIT actually tests SR2 RDA)
- [x] `0x81F7` `install_data_rx_handler` - description claimed handlers at &8239/&8296 but bytes load &8223/&8291; rewrote desc and 4 inline comments
- [x] `0x8223` `nmi_data_rx_bulk` - description matches body; inline comments accurate
- [x] `0x82F8` `ack_tx_write_dest` - description was incomplete (stopped at TDRA error path); rewrote to cover success path; fixed inline comment claiming &8326 when target is &8316
- [x] `0x8316` `nmi_ack_tx_src` - description claimed reads econet_station_id with INTOFF but body reads tx_src_stn workspace copy; corrected
- [ ] `0x833F` `advance_rx_buffer_ptr`
- [ ] `0x83EB` `set_nmi_rx_scout`
- [ ] `0x8400` `copy_scout_to_buffer`
- [ ] `0x8448` `release_tube`
- [ ] `0x848B` `imm_op_dispatch_lo`
- [ ] `0x84BC` `rx_imm_machine_type`
- [ ] `0x84F9` `imm_op_build_reply`
- [ ] `0x852C` `advance_buffer_ptr`
- [ ] `0x853B` `tx_done_dispatch_lo`
- [ ] `0x8540` `tx_done_jsr`
- [ ] `0x8563` `tx_done_halt`
- [ ] `0x857A` `tx_done_continue`
- [ ] `0x8582` `tx_done_exit`
- [ ] `0x85F1` `inactive_poll`
- [ ] `0x85FC` `intoff_test_inactive`
- [ ] `0x862C` `tx_bad_ctrl_error`
- [ ] `0x8630` `tx_line_jammed`
- [ ] `0x864A` `tx_prepare`
- [ ] `0x867E` `tx_ctrl_dispatch_lo`
- [ ] `0x8686` `tx_ctrl_machine_type`
- [ ] `0x868A` `tx_ctrl_peek`
- [ ] `0x868E` `tx_ctrl_poke`
- [ ] `0x8690` `tx_ctrl_store_and_add`
- [ ] `0x8723` `tx_last_data`
- [ ] `0x874B` `nmi_reply_scout`
- [ ] `0x875F` `nmi_reply_cont`
- [ ] `0x8776` `nmi_reply_validate`
- [ ] `0x87BE` `nmi_scout_ack_src`
- [ ] `0x87CE` `data_tx_begin`
- [ ] `0x87E3` `nmi_data_tx`
- [ ] `0x8886` `handshake_await_ack`
- [ ] `0x8892` `nmi_final_ack`
- [ ] `0x88A6` `nmi_final_ack_net`
- [ ] `0x88DE` `tx_result_ok`
- [ ] `0x88E2` `tx_result_fail`
- [ ] `0x88F0` `rom_gap_88f0`
- [ ] `0x898C` `adlc_full_reset`
- [ ] `0x899B` `adlc_rx_listen`
- [ ] `0x89A6` `wait_idle_and_reset`
- [ ] `0x89D8` `rom_set_nmi_vector`
- [ ] `0x89ED` `svc_dispatch_lo`
- [ ] `0x8A20` `svc_dispatch_hi`
- [ ] `0x8B00` `scan_remote_keys`
- [ ] `0x8B18` `save_text_ptr`
- [ ] `0x8B45` `svc_18_fs_select`
- [ ] `0x8B4D` `ensure_fs_selected`
- [ ] `0x8BC0` `help_utils`
- [ ] `0x8BC4` `help_net`
- [ ] `0x8BD5` `print_cmd_table_loop`
- [ ] `0x8C25` `done_print_table`
- [ ] `0x8C29` `help_wrap_if_serial`
- [ ] `0x8CAD` `get_ws_page`
- [ ] `0x8CFD` `notify_new_fs`
- [ ] `0x8CFF` `call_fscv`
- [ ] `0x8D02` `issue_svc_15`
- [ ] `0x8D24` `check_credits_easter_egg`
- [ ] `0x8E5B` `dir_op_dispatch`
- [x] `0x8E61` `svc_dispatch` - description compared against body, accurate
- [x] `0x8E71` `noop_dey_rts` - description compared against body, accurate
- [x] `0x8E73` `copy_template_to_zp` - description compared against body, accurate
- [x] `0x8E7F` `fs_info_template` - description compared against body, accurate
- [ ] `0x8E98` `read_cmos_byte_0`
- [ ] `0x8E9A` `osbyte_a1`
- [ ] `0x8EA7` `fs_vector_table`
- [ ] `0x8EC9` `osbyte_x0`
- [ ] `0x8ECB` `osbyte_yff`
- [ ] `0x8ED2` `osbyte_x0_y0`
- [ ] `0x8EE9` `raise_y_to_c8`
- [ ] `0x8EF0` `store_ws_page_count`
- [ ] `0x904F` `write_vector_entry`
- [ ] `0x9064` `restore_fs_context`
- [ ] `0x909E` `verify_ws_checksum`
- [ ] `0x91F9` `print_newline_no_spool`
- [ ] `0x91FB` `print_char_no_spool`
- [ ] `0x9201` `print_byte_no_spool`
- [ ] `0x923F` `print_hex_nybble`
- [ ] `0x9255` `print_hex_nybble_no_spool`
- [ ] `0x9261` `print_inline`
- [ ] `0x9269` `loop_next_char`
- [ ] `0x939A` `is_decimal_digit`
- [ ] `0x93A2` `is_dec_digit_only`
- [ ] `0x93AB` `get_access_bits`
- [ ] `0x93B5` `get_prot_bits`
- [ ] `0x93C8` `prot_bit_encode_table`
- [ ] `0x93D3` `set_text_and_xfer_ptr`
- [ ] `0x93D7` `set_xfer_params`
- [ ] `0x93DD` `set_options_ptr`
- [ ] `0x93E1` `clear_escapable`
- [ ] `0x93E6` `cmp_5byte_handle`
- [ ] `0x93F2` `fscv_7_read_handles`
- [ ] `0x9446` `check_not_ampersand`
- [ ] `0x9463` `copy_fs_cmd_name`
- [x] `0x9612` `osbyte_a2` - description compared against body, accurate
- [x] `0x962B` `osbyte_a2_value_tya` - description compared against body, accurate
- [ ] `0x973D` `init_txcb_bye`
- [ ] `0x974B` `init_txcb`
- [ ] `0x9763` `txcb_init_template`
- [ ] `0x976F` `send_request_nowrite`
- [ ] `0x9773` `send_request_write`
- [ ] `0x978A` `save_net_tx_cb`
- [ ] `0x978B` `save_net_tx_cb_vset`
- [ ] `0x988F` `check_escape_and_classify`
- [ ] `0x989F` `lang_4_validated`
- [ ] `0x98BE` `wait_net_tx_ack`
- [ ] `0x9930` `fixup_reply_status_a`
- [ ] `0x993B` `load_reply_and_classify`
- [ ] `0x99C3` `error_inline`
- [ ] `0x9A5E` `append_space_and_num`
- [ ] `0x9A7A` `append_decimal_digit`
- [ ] `0x9A9A` `net_error_lookup_data`
- [ ] `0x9AA6` `error_msg_table`
- [ ] `0x9B24` `init_tx_ptr_and_send`
- [ ] `0x9B75` `pass_txbuf_init_table`
- [ ] `0x9B81` `init_tx_ptr_for_pass`
- [ ] `0x9BF5` `load_text_ptr_and_parse`
- [ ] `0x9C00` `gsread_to_buf`
- [ ] `0x9D5F` `copy_fsopts_to_zp`
- [ ] `0x9D6B` `skip_one_and_advance5`
- [ ] `0x9D6C` `advance_y_by_4`
- [ ] `0x9D71` `copy_workspace_to_fsopts`
- [ ] `0x9D7E` `retreat_y_by_4`
- [ ] `0x9D7F` `retreat_y_by_3`
- [ ] `0x9E82` `format_filename_field`
- [ ] `0x9FB4` `return_with_last_flag`
- [ ] `0x9FC2` `osfind_close_or_open`
- [x] `0xA103` `cmos_opt_mask_table` - description compared against body, accurate
- [ ] `0xA131` `update_addr_from_offset1`
- [ ] `0xA133` `add_workspace_to_fsopts`
- [ ] `0xA145` `store_adjusted_byte`
- [ ] `0xA1EF` `lookup_cat_entry_0`
- [ ] `0xA390` `tube_claim_c3`
- [ ] `0xA3E7` `get_pb_ptr_as_index`
- [ ] `0xA3E9` `byte_to_2bit_index`
- [ ] `0xA3FF` `net_1_read_handle`
- [ ] `0xA45B` `match_fs_cmd`
- [ ] `0xA764` `boot_cmd_oscli`
- [ ] `0xA76C` `cmd_table_fs`
- [ ] `0xA864` `osword_setup_handler`
- [ ] `0xA901` `bin_to_bcd`
- [ ] `0xA9A8` `osword_13_dispatch_lo`
- [ ] `0xA9BA` `osword_13_dispatch_hi`
- [ ] `0xAA72` `osword_13_read_csd`
- [ ] `0xAA75` `osword_13_write_csd`
- [ ] `0xAA82` `copy_pb_byte_to_ws`
- [ ] `0xAA91` `osword_13_read_ws_pair`
- [x] `0xAAB8` `osword_13_write_prot` - description compared against body, accurate
- [ ] `0xAABB` `set_via_shadow_pair`
- [ ] `0xAB43` `update_fcb_flag_bits`
- [ ] `0xAB71` `osword_13_read_rx_port`
- [x] `0xAB7F` `osword_13_read_error` - description compared against body, accurate
- [ ] `0xAB82` `store_a_to_pb_1`
- [x] `0xAB86` `osword_13_read_context` - description compared against body, accurate
- [ ] `0xAB8B` `osword_13_read_free_bufs`
- [ ] `0xAB93` `osword_13_read_ctx_3`
- [ ] `0xAB9E` `osword_13_write_ctx_3`
- [ ] `0xACAD` `store_ptr_at_ws_y`
- [ ] `0xAD15` `push_osword_handler_addr`
- [ ] `0xAD20` `netv_dispatch_lo`
- [ ] `0xAD29` `netv_dispatch_hi`
- [ ] `0xAD32` `osword_4_handler`
- [ ] `0xADB8` `match_rx_code`
- [ ] `0xADC1` `osword_claim_codes`
- [ ] `0xADFE` `init_ws_copy_wide`
- [ ] `0xAE07` `init_ws_copy_narrow`
- [ ] `0xAE0B` `ws_copy_vclr_entry`
- [ ] `0xAE33` `ws_txcb_template_data`
- [ ] `0xAE5A` `netv_spool_check`
- [ ] `0xAE64` `reset_spool_buf_state`
- [ ] `0xAE94` `append_byte_to_rxbuf`
- [ ] `0xB002` `tx_econet_txcb_template`
- [ ] `0xB05F` `commit_state_byte`
- [ ] `0xB081` `read_osbyte_to_ws_x0`
- [ ] `0xB083` `read_osbyte_to_ws`
- [ ] `0xB0D5` `cdir_alloc_size_table`
- [ ] `0xB0F2` `cmd_lcat`
- [ ] `0xB103` `cmd_ex`
- [ ] `0xB21A` `print_10_chars`
- [ ] `0xB22A` `parse_cmd_arg_y0`
- [ ] `0xB29F` `copy_arg_to_buf_x0`
- [ ] `0xB2A1` `copy_arg_to_buf`
- [ ] `0xB2A3` `copy_arg_validated`
- [x] `0xB2CF` `mask_owner_access` - description compared against body, accurate
- [ ] `0xB327` `print_num_no_leading`
- [ ] `0xB373` `save_ptr_to_os_text`
- [ ] `0xB37F` `skip_to_next_arg`
- [ ] `0xB393` `save_ptr_to_spool_buf`
- [ ] `0xB3D5` `copy_ps_data_y1c`
- [ ] `0xB477` `store_ps_station`
- [ ] `0xB4A8` `load_ps_server_addr`
- [ ] `0xB51C` `write_ps_slot_byte_ff`
- [ ] `0xB523` `write_two_bytes_inc_y`
- [ ] `0xB52B` `reverse_ps_name_to_tx`
- [ ] `0xB575` `ps_slot_txcb_template`
- [ ] `0xB6A6` `init_ps_slot_from_rx`
- [ ] `0xB6BD` `store_char_uppercase`
- [ ] `0xB6D2` `cmd_prot`
- [ ] `0xB7E3` `init_channel_table`
- [ ] `0xB805` `attr_to_chan_index`
- [ ] `0xB814` `check_chan_char`
- [ ] `0xB8A8` `alloc_fcb_slot`
- [ ] `0xB8F8` `close_all_net_chans`
- [ ] `0xB925` `match_station_net`
- [ ] `0xB934` `find_open_fcb`
- [ ] `0xB977` `init_wipe_counters`
- [ ] `0xBAB7` `loop_restore_workspace`
- [ ] `0xBAC0` `restore_catalog_entry`
- [ ] `0xBB2A` `inc_fcb_byte_count`
- [ ] `0xBC74` `flush_fcb_if_station_known`
- [ ] `0xBD1B` `read_rx_attribute`
- [ ] `0xBD20` `store_rx_attribute`
- [ ] `0xBE42` `parse_dump_range`
- [ ] `0xBF71` `close_ws_file`
- [ ] `0xBFC0` `inx4`
- [ ] `0xBFC5` `rom_tail_padding`
- [ ] `0xBFE6` `hazel_idx_bases`

## Depth 1 (90 routines)

- [ ] `0x8028` `svc5_irq_check`
- [ ] `0x8050` `adlc_init`
- [ ] `0x80B8` `nmi_rx_scout_net`
- [ ] `0x81A7` `send_data_rx_ack`
- [ ] `0x8291` `nmi_data_rx_tube`
- [ ] `0x82DF` `ack_tx`
- [ ] `0x8386` `nmi_post_ack_dispatch`
- [ ] `0x83E8` `reset_adlc_rx_listen`
- [ ] `0x83F2` `discard_reset_listen`
- [ ] `0x8549` `tx_done_econet_event`
- [ ] `0x8557` `tx_done_os_proc`
- [ ] `0x8589` `tx_begin`
- [ ] `0x872F` `nmi_tx_complete`
- [ ] `0x8773` `reject_reply`
- [ ] `0x88BA` `nmi_final_ack_validate`
- [ ] `0x8900` `tx_calc_transfer`
- [ ] `0x89B9` `save_econet_state`
- [ ] `0x89CA` `nmi_bootstrap_entry`
- [x] `0x8A54` `service_handler` - description compared against body, accurate
- [ ] `0x8B23` `cmd_net_fs`
- [ ] `0x8BD8` `loop_next_entry`
- [ ] `0x8CBD` `setup_ws_ptr`
- [ ] `0x8D09` `svc_dispatch_idx_2`
- [ ] `0x8DD5` `cmd_pass`
- [ ] `0x8E3C` `send_cmd_and_dispatch`
- [x] `0x8E8A` `svc_26_close_all_files` - description compared against body, accurate
- [ ] `0x8ED8` `svc_7_osbyte`
- [ ] `0x8F10` `svc_2_priv_ws`
- [x] `0x90C7` `print_station_id` - description compared against body, accurate
- [ ] `0x9236` `print_hex_byte`
- [ ] `0x924C` `print_hex_byte_no_spool`
- [ ] `0x928A` `print_inline_no_spool`
- [ ] `0x92B2` `parse_addr_arg`
- [ ] `0x93F7` `set_conn_active`
- [ ] `0x940D` `clear_conn_active`
- [ ] `0x95C1` `print_station_low`
- [ ] `0x95C8` `print_fs_station`
- [ ] `0x95DA` `print_dir_syntax`
- [x] `0x9619` `cmd_space` - description compared against body, accurate
- [x] `0x9623` `cmd_nospace` - description compared against body, accurate
- [ ] `0x965F` `print_ps_address`
- [ ] `0x973F` `init_txcb_port`
- [ ] `0x97B7` `prep_send_tx_cb`
- [ ] `0x9850` `lang_1_remote_boot`
- [ ] `0x98AF` `lang_0_insert_key`
- [ ] `0x99DF` `check_net_error_code`
- [ ] `0x9A69` `append_decimal_num`
- [ ] `0x9FB6` `finalise_and_return`
- [ ] `0xA12C` `update_addr_from_offset9`
- [ ] `0xA134` `adjust_fsopts_4bytes`
- [ ] `0xA28A` `send_osbput_data`
- [ ] `0xA2ED` `write_data_block`
- [ ] `0xA405` `net_2_read_entry`
- [ ] `0xA415` `net_3_close_handle`
- [ ] `0xA42F` `fscv_3_star_cmd`
- [ ] `0xA440` `cmd_fs_reentry`
- [x] `0xA4E4` `fscv_2_star_run` - description compared against body, accurate
- [ ] `0xA644` `find_station_bit2`
- [ ] `0xA66F` `find_station_bit3`
- [ ] `0xA6A6` `flip_set_station_boot`
- [ ] `0xA6D5` `fsreply_1_boot`
- [ ] `0xA83B` `svc_8_osword`
- [ ] `0xA877` `extract_osword_subcode`
- [ ] `0xA985` `osword_12_handler`
- [ ] `0xA9CC` `osword_13_read_station`
- [ ] `0xAAB2` `osword_13_read_prot`
- [ ] `0xAAC2` `osword_13_read_handles`
- [ ] `0xAAD0` `osword_13_set_handles`
- [ ] `0xAB68` `osword_13_read_rx_flag`
- [ ] `0xAC47` `osword_14_handler`
- [ ] `0xACED` `handle_burst_xfer`
- [ ] `0xACFC` `netv_handler`
- [ ] `0xB066` `serialise_palette_entry`
- [ ] `0xB0F8` `cmd_lex`
- [ ] `0xB21C` `print_chars_from_buf`
- [ ] `0xB22C` `parse_filename_arg`
- [ ] `0xB310` `print_decimal_digit_no_spool`
- [ ] `0xB39E` `init_spool_drive`
- [ ] `0xB483` `print_file_server_is`
- [ ] `0xB48D` `print_printer_server_is`
- [ ] `0xB4B4` `pop_requeue_ps_scan`
- [ ] `0xB4D6` `skip_next_ps_slot`
- [ ] `0xB6D6` `cmd_unprot`
- [ ] `0xB847` `lookup_chan_by_char`
- [ ] `0xB886` `store_result_check_dir`
- [ ] `0xB8FC` `scan_fcb_flags`
- [ ] `0xBC65` `done_inc_byte_count`
- [ ] `0xBD25` `abort_if_escape`
- [ ] `0xBF78` `open_file_for_read`
- [ ] `0xBFBD` `advance_x_by_4`

## Depth 2 (34 routines)

- [ ] `0x80D8` `scout_error`
- [ ] `0x8195` `port_match_found`
- [ ] `0x8268` `data_rx_complete`
- [ ] `0x83E5` `discard_reset_rx`
- [ ] `0x8493` `rx_imm_exec`
- [ ] `0x84CE` `rx_imm_peek`
- [ ] `0x8512` `setup_sr_tx`
- [ ] `0x86A2` `tx_ctrl_proc`
- [ ] `0x8C06` `loop_print_syntax`
- [ ] `0x8C42` `svc_4_star_command`
- [ ] `0x8C93` `print_version_header`
- [ ] `0x903C` `init_adlc_and_vectors`
- [ ] `0x945E` `send_fs_request`
- [ ] `0x9A3A` `append_drv_dot_num`
- [ ] `0x9BB6` `poll_adlc_tx_status`
- [ ] `0x9D4F` `print_5_hex_bytes`
- [ ] `0x9D87` `check_and_setup_txcb`
- [ ] `0xA1F3` `lookup_cat_slot_data`
- [ ] `0xA29F` `write_block_entry`
- [ ] `0xA638` `fsreply_3_set_csd`
- [ ] `0xA63E` `fsreply_5_set_lib`
- [ ] `0xA69A` `cmd_flip`
- [ ] `0xA6E5` `fsreply_2_copy_handles`
- [ ] `0xA910` `osword_10_handler`
- [ ] `0xB01A` `lang_2_save_palette_vdu`
- [ ] `0xB0A1` `cmd_cdir`
- [ ] `0xB2E4` `ex_print_col_sep`
- [ ] `0xB303` `print_decimal_3dig_no_spool`
- [ ] `0xB338` `print_decimal_digit`
- [ ] `0xB6F3` `cmd_wipe`
- [ ] `0xB7CB` `prompt_yn`
- [ ] `0xBD59` `loop_dump_line`
- [ ] `0xBE37` `print_hex_and_space`
- [ ] `0xBFBA` `advance_x_by_8`

## Depth 3 (17 routines)

- [ ] `0x8215` `nmi_error_dispatch`
- [ ] `0x8395` `rx_complete_update_rxcb`
- [ ] `0x84B1` `rx_imm_poke`
- [ ] `0x8845` `nmi_data_tx_tube`
- [ ] `0x88E4` `tx_store_result`
- [ ] `0x8BC6` `print_cmd_table`
- [ ] `0x8C51` `svc_9_help`
- [x] `0x9900` `cond_save_error_code` - description compared against body, accurate
- [ ] `0x9B2C` `send_net_packet`
- [ ] `0x9B89` `setup_pass_txbuf`
- [ ] `0x9CB5` `setup_dir_display`
- [ ] `0x9D44` `print_load_exec_addrs`
- [ ] `0xABE9` `init_bridge_poll`
- [x] `0xB118` `fscv_5_cat` - description compared against body, accurate
- [ ] `0xB32A` `print_decimal_3dig`
- [ ] `0xB703` `request_next_wipe`
- [ ] `0xBE01` `print_dump_header`

## Depth 4 (18 routines)

- [ ] `0x832D` `post_ack_scout`
- [ ] `0x8409` `save_acccon_for_shadow_ram`
- [ ] `0x8454` `immediate_op`
- [ ] `0x86E7` `nmi_tx_data`
- [ ] `0x8BBB` `help_print_nfs_cmds`
- [ ] `0x8E21` `clear_if_station_match`
- [ ] `0x993D` `classify_reply_error`
- [ ] `0x99A7` `error_bad_inline`
- [ ] `0x99C0` `error_inline_log`
- [ ] `0x9DDC` `dispatch_osword_op`
- [ ] `0xA3C4` `parse_fs_ps_args`
- [ ] `0xAA9D` `osword_13_write_ws_pair`
- [ ] `0xABA9` `osword_13_bridge_query`
- [ ] `0xACF8` `enable_irq_and_poll`
- [ ] `0xAD40` `tx_econet_abort`
- [ ] `0xAFA6` `send_disconnect_reply`
- [ ] `0xB556` `print_station_addr`
- [ ] `0xBD79` `loop_pop_stack_buf`

## Depth 5 (30 routines)

- [ ] `0x8112` `scout_complete`
- [ ] `0x8AEA` `cmd_roff`
- [ ] `0x8C64` `svc_return_unclaimed`
- [ ] `0x8DA6` `load_transfer_params`
- [ ] `0x90B5` `error_net_checksum`
- [ ] `0x934A` `err_bad_hex`
- [ ] `0x9437` `error_bad_filename`
- [ ] `0x9483` `parse_quoted_arg`
- [ ] `0x95EE` `set_fs_or_ps_cmos_station`
- [ ] `0x97CD` `recv_and_process_reply`
- [ ] `0x987E` `lang_3_exec_0100`
- [ ] `0x9895` `raise_escape_error`
- [ ] `0x9C85` `send_txcb_swap_addrs`
- [x] `0xA0A9` `fscv_0_opt_entry` - description compared against body, accurate
- [ ] `0xA398` `cmd_fs`
- [ ] `0xA3BB` `print_fs_info_newline`
- [ ] `0xA5A1` `error_bad_command`
- [ ] `0xA5AE` `check_exec_addr`
- [ ] `0xAC67` `store_osword_pb_ptr`
- [ ] `0xACB7` `handle_tx_request`
- [ ] `0xAD64` `netv_claim_release`
- [ ] `0xADD3` `osword_8_handler`
- [ ] `0xAEB8` `process_spool_data`
- [ ] `0xAF80` `err_printer_busy`
- [ ] `0xB81C` `err_net_chan_invalid`
- [ ] `0xB88C` `check_not_dir`
- [ ] `0xB8DC` `alloc_fcb_or_error`
- [ ] `0xBCBC` `send_wipe_request`
- [ ] `0xBDBB` `loop_next_dump_col`
- [ ] `0xBEAB` `init_dump_buffer`

## Depth 6 (14 routines)

- [ ] `0x8B52` `select_fs_via_cmd_net_fs`
- [ ] `0x9670` `print_fs_address`
- [ ] `0x9D0C` `recv_reply`
- [ ] `0x9FCF` `clear_result`
- [ ] `0xA284` `recv_reply_preserve_flags`
- [ ] `0xA4A2` `loop_skip_trail_spaces`
- [ ] `0xAE6F` `netv_print_data`
- [ ] `0xAE9D` `handle_spool_ctrl_byte`
- [ ] `0xB251` `strip_token_prefix`
- [ ] `0xB3AC` `cmd_ps`
- [ ] `0xB3D7` `copy_ps_data`
- [ ] `0xB7D3` `flush_and_read_char`
- [ ] `0xBD41` `cmd_dump`
- [ ] `0xBE4E` `loop_parse_hex_digit`

## Depth 7 (9 routines)

- [ ] `0x8CC7` `svc_3_autoboot`
- [ ] `0x8F38` `nfs_init_body`
- [ ] `0x944E` `read_filename_char`
- [x] `0x9630` `svc_29_status` - description compared against body, accurate
- [ ] `0x9C3E` `do_fs_cmd_iteration`
- [ ] `0xA1FA` `setup_transfer_workspace`
- [ ] `0xA329` `tail_update_catalogue`
- [x] `0xB22F` `parse_access_prefix` - description compared against body, accurate
- [ ] `0xB581` `cmd_pollps`

## Depth 8 (5 routines)

- [ ] `0x9425` `cmd_fs_operation`
- [ ] `0x94C5` `cmd_rename`
- [ ] `0x9C22` `filev_handler`
- [ ] `0xA5C3` `alloc_run_channel`
- [ ] `0xBD15` `send_and_receive`

## Depth 9 (2 routines)

- [x] `0xA4F1` `cmd_run_via_urd` - description compared against body, accurate
- [ ] `0xB99A` `start_wipe_pass`

## Depth 10 (3 routines)

- [ ] `0x8E2D` `check_urd_prefix`
- [ ] `0xBA09` `save_fcb_context`
- [ ] `0xBB38` `process_all_fcbs`

## Depth 11 (10 routines)

- [ ] `0x8D91` `cmd_iam`
- [ ] `0x9071` `fscv_6_shutdown`
- [ ] `0x9512` `cmd_dir`
- [ ] `0x9776` `cmd_bye`
- [ ] `0x9FB1` `close_all_fcbs`
- [ ] `0x9FEE` `send_open_file_request`
- [ ] `0xA14C` `gbpbv_handler`
- [ ] `0xA9DA` `osword_13_set_station`
- [ ] `0xBACC` `loop_save_before_match`
- [ ] `0xBC7C` `flush_fcb_with_init`

## Depth 12 (3 routines)

- [ ] `0x968E` `dispatch_help_command`
- [ ] `0x9EAB` `argsv_handler`
- [ ] `0xBACF` `find_matching_fcb`

## Depth 13 (3 routines)

- [ ] `0xA10B` `fscv_1_eof`
- [ ] `0xBB68` `bgetv_handler`
- [ ] `0xBBE7` `bputv_handler`



## Session 1 honest summary

Genuinely description-reviewed (body compared against description and
inline comments examined): ~35 routines. The remainder of the depth-0/1
'triage' was bounds-only: it confirmed each routine's start/end address
and that internal labels were branch-target helpers, but it did NOT
verify that each subroutine() description matches what the body does.

Resuming with proper discipline from session 2: leaf-first, one
routine at a time, body-vs-description for every entry.
