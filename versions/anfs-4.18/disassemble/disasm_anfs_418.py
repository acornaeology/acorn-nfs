import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook, stringz_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'anfs-4.18.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='6502', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.add_move(0x0016, 0xBEC3, 0x42)
d.add_move(0x0400, 0xBF04, 0xFC)
d.add_move(0x0500, 0xBC94, 0x100)
d.add_move(0x0600, 0xBD94, 0x100)

d.label(0xBEC3, 'reloc_zp_src')

d.label(0xBF04, 'reloc_p4_src')

d.label(0xBC94, 'reloc_p5_src')

d.label(0xBD94, 'reloc_p6_src')
d.byte(0xBC93)
d.use_environment('acorn_mos')
d.use_environment('acorn_model_b_hardware')
d.use_environment('acorn_sideways_rom')
d.hook_subroutine(0x9145, 'print_inline', stringhi_hook)
d.hook_subroutine(0x96D4, 'error_inline', stringz_hook)
d.hook_subroutine(0x96D1, 'error_inline_log', stringz_hook)
d.hook_subroutine(0x96B8, 'error_bad_inline', stringz_hook)
d.constant(0xFEA0, 'adlc_cr1')
d.constant(0xFEA1, 'adlc_cr2')
d.constant(0xFEA2, 'adlc_tx')
d.constant(0xFEA3, 'adlc_tx2')
d.constant(0xFE18, 'econet_station_id')
d.constant(0xFE20, 'econet_nmi_enable')
d.constant(0x99, 'port_command')
d.constant(0x90, 'port_reply')
d.constant(0x91, 'port_save_ack')
d.constant(0x92, 'port_load_data')
d.constant(0x93, 'port_remote')
d.constant(0xD1, 'port_printer')
d.constant(0xA0, 'err_line_jammed')
d.constant(0xA1, 'err_net_error')
d.constant(0xA2, 'err_not_listening')
d.constant(0xA3, 'err_no_clock')
d.constant(0xA4, 'err_tx_cb_error')
d.constant(0xA5, 'err_no_reply')
d.constant(0xA8, 'err_fs_cutoff')
d.constant(0x80, 'tx_flag')
d.constant(0x7F, 'rx_ready')
d.constant(0x20, 'handle_base')
d.constant(0xFE, 'cb_stop')
d.constant(0xFD, 'cb_skip')
d.constant(0xFC, 'cb_fill')
d.constant(20, 'osbyte_explode_chars')
d.constant(120, 'osbyte_write_keys_pressed')
d.constant(143, 'osbyte_issue_service_request')
d.constant(168, 'osbyte_read_rom_ptr_table_low')

d.label(0x0097, 'escapable')

d.label(0x0098, 'need_release_tube')

d.label(0x0099, 'prot_flags')

d.label(0x009A, 'net_tx_ptr')

d.label(0x009B, 'net_tx_ptr_hi')

d.label(0x009C, 'net_rx_ptr')

d.label(0x009D, 'net_rx_ptr_hi')

d.label(0x009E, 'nfs_workspace')

d.label(0x009F, 'nfs_workspace_hi')

d.label(0x00A0, 'nmi_tx_block')

d.label(0x00A1, 'nmi_tx_block_hi')

d.label(0x00A2, 'port_buf_len')

d.label(0x00A3, 'port_buf_len_hi')

d.label(0x00A4, 'open_port_buf')

d.label(0x00A5, 'open_port_buf_hi')

d.label(0x00A6, 'port_ws_offset')

d.label(0x00A7, 'rx_buf_offset')

d.label(0x00A8, 'ws_page')

d.label(0x00A9, 'svc_state')

d.label(0x00AA, 'osword_flag')

d.label(0x00AB, 'ws_ptr_lo')

d.label(0x00AC, 'ws_ptr_hi')

d.label(0x00AD, 'table_idx')

d.label(0x00AE, 'work_ae')

d.label(0x00AF, 'addr_work')

d.label(0x00B0, 'fs_load_addr')

d.label(0x00B1, 'fs_load_addr_hi')

d.label(0x00B2, 'fs_load_addr_2')

d.label(0x00B3, 'fs_load_addr_3')

d.label(0x00B4, 'fs_work_4')

d.label(0x00B5, 'fs_work_5')

d.label(0x00B6, 'fs_work_6')

d.label(0x00B7, 'fs_work_7')

d.label(0x00B8, 'fs_error_ptr')

d.label(0x00B9, 'fs_crflag')

d.label(0x00BA, 'fs_spool_handle')

d.label(0x00BB, 'fs_options')

d.label(0x00BC, 'fs_block_offset')

d.label(0x00BD, 'fs_last_byte_flag')

d.label(0x00BE, 'fs_crc_lo')

d.label(0x00BF, 'fs_crc_hi')

d.label(0x00CC, 'fs_ws_ptr')

d.label(0x00C0, 'txcb_ctrl')

d.label(0x00C1, 'txcb_port')

d.label(0x00C2, 'txcb_dest')

d.label(0x00C4, 'txcb_start')

d.label(0x00C7, 'txcb_pos')

d.label(0x00C8, 'txcb_end')

d.label(0x00CD, 'nfs_temp')

d.label(0x00CE, 'rom_svc_num')

d.label(0x00CF, 'fs_spool0')

d.label(0x00D0, 'vdu_status')

d.label(0x0000, 'zp_ptr_lo')

d.label(0x0001, 'zp_ptr_hi')

d.label(0x0002, 'zp_work_2')

d.label(0x0003, 'zp_work_3')

d.label(0x0010, 'zp_temp_10')

d.label(0x0011, 'zp_temp_11')

d.label(0x0012, 'tube_data_ptr')

d.label(0x0013, 'tube_data_ptr_hi')

d.label(0x0014, 'tube_claim_flag')

d.label(0x0015, 'tube_claimed_id')

d.label(0x0016, 'nmi_workspace_start')

d.label(0x0063, 'zp_0063')

d.label(0x0078, 'zp_0078')

d.label(0x00EF, 'osbyte_a_copy')

d.label(0x00F0, 'osword_pb_ptr')

d.label(0x00F1, 'osword_pb_ptr_hi')

d.label(0x00F3, 'os_text_ptr_hi')

d.label(0x00F7, 'osrdsc_ptr_hi')

d.label(0x00FD, 'brk_ptr')

d.label(0x00FF, 'escape_flag')

d.label(0x0100, 'error_block')

d.label(0x0101, 'error_text')

d.label(0x0102, 'stack_page_2')

d.label(0x0103, 'stack_page_3')

d.label(0x0104, 'stack_page_4')

d.label(0x0106, 'stack_page_6')

d.label(0x0128, 'tube_osword_pb')

d.label(0x026A, 'vdu_queue_count')

d.label(0x028D, 'last_break_type')

d.label(0x02A0, 'rom_type_table')

d.label(0x0350, 'vdu_screen_mode')

d.label(0x0351, 'vdu_display_start_hi')

d.label(0x0355, 'vdu_mode')

d.label(0x0700, 'string_buf')

d.label(0x072C, 'tube_vdu_stream_end')

d.label(0x072E, 'tube_vdu_normal_byte')

d.label(0x0CFF, 'nmi_code_base')

d.label(0x0D07, 'nmi_romsel')

d.label(0x0D0C, 'nmi_jmp_lo')

d.label(0x0D0D, 'nmi_jmp_hi')

d.label(0x0D0E, 'set_nmi_vector')

d.label(0x0D11, 'install_nmi_handler')

d.label(0x0D14, 'nmi_rti')

d.label(0x0D1A, 'imm_param_base')

d.label(0x0D1E, 'tx_addr_base')

d.label(0x0D20, 'tx_dst_stn')

d.label(0x0D21, 'tx_dst_net')

d.label(0x0D22, 'tx_src_stn')

d.label(0x0D23, 'tx_src_net')

d.label(0x0D24, 'tx_ctrl_byte')

d.label(0x0D25, 'tx_port')

d.label(0x0D26, 'tx_data_start')

d.label(0x0D2A, 'tx_data_len')

d.label(0x0D2E, 'scout_buf')

d.label(0x0D2F, 'scout_src_net')

d.label(0x0D30, 'scout_ctrl')

d.label(0x0D31, 'scout_port')

d.label(0x0D32, 'scout_data')

d.label(0x0D3D, 'rx_src_stn')

d.label(0x0D3E, 'rx_src_net')

d.label(0x0D3F, 'rx_ctrl')

d.label(0x0D40, 'rx_port')

d.label(0x0D41, 'rx_remote_addr')

d.label(0x0D42, 'rx_extra_byte')

d.label(0x0D43, 'saved_nmi_lo')

d.label(0x0D44, 'saved_nmi_hi')

d.label(0x0D4A, 'tx_flags')

d.label(0x0D4B, 'nmi_next_lo')

d.label(0x0D4C, 'nmi_next_hi')

d.label(0x0D4F, 'tx_index')

d.label(0x0D50, 'tx_length')

d.label(0x0D60, 'tx_complete_flag')

d.label(0x0D61, 'econet_flags')

d.label(0x0D62, 'econet_init_flag')

d.label(0x0D63, 'tube_present')

d.label(0x0D64, 'ws_0d64')

d.label(0x0D65, 'tx_op_type')

d.label(0x0D66, 'exec_addr_lo')

d.label(0x0D67, 'exec_addr_hi')

d.label(0x0D68, 'ws_0d68')

d.label(0x0D69, 'ws_0d69')

d.label(0x0D6A, 'ws_0d6a')

d.label(0x0D6B, 'spool_buf_idx')

d.label(0x0D6C, 'fs_flags')

d.label(0x0D6D, 'tx_retry_count')

d.label(0x0D6E, 'rx_wait_timeout')

d.label(0x0D6F, 'peek_retry_count')

d.label(0x0D72, 'bridge_status')

d.label(0x0DE6, 'txcb_default_base')

d.label(0x0DF0, 'rom_ws_pages')

d.label(0x0DFA, 'fs_context_save')

d.label(0x0DFE, 'osword_ws_base')

d.label(0x0DFF, 'fs_server_base')

d.label(0x0E00, 'fs_server_stn')

d.label(0x0E01, 'fs_server_net')

d.label(0x0E02, 'fs_urd_handle')

d.label(0x0E03, 'fs_csd_handle')

d.label(0x0E04, 'fs_lib_handle')

d.label(0x0E05, 'fs_boot_option')

d.label(0x0E06, 'fs_messages_flag')

d.label(0x0E07, 'fs_eof_flags')

d.label(0x0E09, 'fs_last_error')

d.label(0x0E0A, 'fs_cmd_context')

d.label(0x0E0B, 'fs_context_hi')

d.label(0x0E16, 'fs_work_16')

d.label(0x0E2F, 'fs_filename_buf_m1')

d.label(0x0E30, 'fs_filename_buf')

d.label(0x0E31, 'fs_filename_buf_1')

d.label(0x0E32, 'fs_filename_buf_2')

d.label(0x0E38, 'fs_filename_backup')

d.label(0x0EF7, 'fs_reply_data')

d.label(0x0F00, 'txcb_reply_port')

d.label(0x0F01, 'fs_cmd_y_param')

d.label(0x0F02, 'fs_cmd_urd')

d.label(0x0F03, 'fs_cmd_csd')

d.label(0x0F04, 'fs_cmd_lib')

d.label(0x0F05, 'fs_cmd_data')

d.label(0x0F06, 'fs_func_code')

d.label(0x0F07, 'fs_data_count')

d.label(0x0F08, 'fs_reply_cmd')

d.label(0x0F09, 'fs_load_vector')

d.label(0x0F0A, 'fs_handle_check')

d.label(0x0F0B, 'fs_load_upper')

d.label(0x0F0C, 'fs_addr_check')

d.label(0x0F0D, 'fs_file_len')

d.label(0x0F0E, 'fs_file_attrs')

d.label(0x0F10, 'fs_file_len_3')

d.label(0x0F11, 'fs_obj_type')

d.label(0x0F12, 'fs_access_level')

d.label(0x0F13, 'fs_reply_stn')

d.label(0x0F14, 'fs_len_clear')

d.label(0x0F16, 'fs_boot_data')

d.label(0x0F2F, 'fs_exam_attr_char')

d.label(0x0F30, 'fs_exam_dir_flag')

d.label(0x0FDC, 'fs_putb_buf')

d.label(0x0FDD, 'fs_getb_buf')

d.label(0x0FDE, 'fs_handle_mask')

d.label(0x0FDF, 'fs_error_flags')

d.label(0x0FE0, 'fcb_xfer_count_lo')

d.label(0x0FF0, 'fcb_xfer_count_mid')

d.label(0x1000, 'fcb_count_lo')

d.label(0x1010, 'fcb_attr_or_count_mid')

d.label(0x1020, 'fcb_station_or_count_hi')

d.label(0x1030, 'fcb_net_or_port')

d.label(0x1040, 'fcb_flags')

d.label(0x1050, 'fcb_net_num')

d.label(0x1060, 'chan_status')

d.label(0x1070, 'cur_dir_handle')

d.label(0x1071, 'fs_lib_flags')

d.label(0x1072, 'handle_1_fcb')

d.label(0x1073, 'handle_2_fcb')

d.label(0x1074, 'handle_3_fcb')

d.label(0x1078, 'fcb_stn_lo')

d.label(0x1088, 'fcb_stn_hi')

d.label(0x1098, 'fcb_buf_offset')

d.label(0x10A8, 'fcb_attr_ref')

d.label(0x10B8, 'fcb_status')

d.label(0x10C8, 'cur_fcb_index')

d.label(0x10C9, 'cur_chan_attr')

d.label(0x10CA, 'cur_attr_ref')

d.label(0x10CB, 'xfer_count_lo')

d.label(0x10CC, 'fcb_buf_page')

d.label(0x10CD, 'xfer_sentinel_1')

d.label(0x10CE, 'xfer_sentinel_2')

d.label(0x10CF, 'xfer_offset')

d.label(0x10D0, 'xfer_pass_count')

d.label(0x10D1, 'xfer_counter')

d.label(0x10D4, 'work_stn_lo')

d.label(0x10D5, 'work_stn_hi')

d.label(0x10D6, 'xfer_flag')

d.label(0x10D7, 'osbput_saved_byte')

d.label(0x10D8, 'quote_mode')

d.label(0x10D9, 'fcb_ctx_save')

d.label(0x10F3, 'filename_buf')

d.label(0x6F6E, 'false_ref_6f6e')
d.entry(0x0016)
d.entry(0x0400)
d.entry(0x0403)
d.entry(0x0406)
d.entry(0x0421)
d.entry(0x0500)
d.entry(0x0520)
d.entry(0x0527)
d.entry(0x052D)
d.entry(0x0537)
d.entry(0x053A)
d.entry(0x055E)
d.entry(0x0562)
d.entry(0x0596)
d.entry(0x05A9)
d.entry(0x05D1)
d.entry(0x05F2)
d.entry(0x0600)

d.label(0x0026, 'tube_send_error_num')

d.label(0x0400, 'tube_page4_vectors')

d.label(0x0500, 'tube_r2_dispatch_table')

d.label(0x0600, 'tube_osbyte_reply_block')

d.label(0x06DF, 'loop_poll_r1_vdu')

d.label(0x06EF, 'setup_tube_vectors')

d.label(0x8001, 'rom_header_byte1')

d.label(0x8002, 'rom_header_byte2')

d.label(0x8032, 'save_registers')

d.label(0x805D, 'set_jsr_protection')

d.label(0x8090, 'econet_restore')

d.label(0x80BD, 'adlc_init_done')

d.label(0x83E4, 'loop_count_rxcb_slot')
d.expr_label(0x83FD, 'imm_op_dispatch_lo-&81')

d.label(0x840F, 'return_from_discard_reset')

d.label(0x84AB, 'jmp_send_data_rx_ack')

d.label(0x84BB, 'set_rx_buf_len_hi')

d.label(0x853D, 'return_from_advance_buf')

d.label(0x85FB, 'reload_inactive_mask')

d.label(0x8600, 'intoff_disable_nmi_op')

d.label(0x87C7, 'tx_check_tdra_ready')

d.label(0x87F2, 'check_tdra_status')

d.label(0x8901, 'check_tx_in_progress')

d.label(0x8A33, 'clear_workspace_byte')

d.label(0x8A38, 'restore_rom_slot')

d.label(0x8A3C, 'dispatch_service')

d.label(0x8A53, 'set_adlc_absent')

d.label(0x8A5A, 'check_adlc_flag')

d.label(0x8A62, 'handle_vectors_claimed')

d.label(0x8A6E, 'init_rom_scan')

d.label(0x8A71, 'loop_scan_net_roms')

d.label(0x8A98, 'next_rom_slot')

d.label(0x8AA7, 'dispatch_svc_with_state')

d.label(0x8ABA, 'dispatch_svc_index')

d.label(0x8ACB, 'restore_svc_state')

d.label(0x8AD1, 'restore_romsel_rts')

d.label(0x8AEE, 'loop_scan_key_range')

d.label(0x8AFB, 'clear_svc_and_ws')

d.label(0x8B0C, 'return_from_save_text_ptr')

d.label(0x8B26, 'loop_sum_rom_bytes')

d.label(0x8B34, 'done_rom_checksum')

d.label(0x8B39, 'loop_copy_fs_ctx')

d.label(0x8B4C, 'loop_set_vectors')

d.label(0x8B7A, 'loop_copy_ws_page')

d.label(0x8BA8, 'print_table_newline')

d.label(0x8BAE, 'loop_next_entry')

d.label(0x8BB6, 'print_indent')

d.label(0x8BC0, 'loop_print_name')

d.label(0x8BCA, 'loop_pad_spaces')

d.label(0x8BE0, 'loop_print_syntax')

d.label(0x8BF0, 'print_syntax_char')

d.label(0x8BF6, 'print_shared_prefix')

d.label(0x8C00, 'loop_next_shared')

d.label(0x8C06, 'loop_print_shared')

d.label(0x8C12, 'print_last_char')

d.label(0x8C1F, 'skip_syntax_bytes')

d.label(0x8C24, 'done_shared_cmds')

d.label(0x8C26, 'done_entry_newline')

d.label(0x8C2F, 'done_print_table')

d.label(0x8C45, 'loop_indent_spaces')

d.label(0x8C4D, 'return_from_help_wrap')

d.label(0x8C70, 'svc_return_unclaimed')

d.label(0x8C73, 'check_help_topic')

d.label(0x8C7D, 'match_help_topic')

d.label(0x8C80, 'loop_dispatch_help')

d.label(0x8C98, 'skip_if_no_match')

d.label(0x8CA2, 'version_string_cr')

d.label(0x8CC9, 'return_from_setup_ws_ptr')

d.label(0x8CDA, 'write_key_state')

d.label(0x8CE0, 'select_net_fs')

d.label(0x8D0A, 'issue_svc_osbyte')

d.label(0x8D1B, 'loop_match_credits')

d.label(0x8D26, 'done_credits_check')

d.label(0x8D2C, 'loop_emit_credits')

d.label(0x8D37, 'return_from_credits_check')

d.label(0x8D38, 'credits_keyword_start')

d.label(0x8D61, 'ps_template_base')

d.label(0x8DA7, 'skip_no_fs_addr')

d.label(0x8DAE, 'loop_copy_logon_cmd')

d.label(0x8DBF, 'scan_pass_prompt')

d.label(0x8DC1, 'loop_scan_colon')

d.label(0x8DD2, 'read_pw_char')

d.label(0x8DE4, 'loop_erase_pw')

d.label(0x8DEB, 'check_pw_special')

d.label(0x8DFA, 'send_pass_to_fs')

d.label(0x8E54, 'svc_dispatch_lo_offset')

d.label(0x8E58, 'dispatch_rts')

d.label(0x8E87, 'jmp_osbyte')

d.label(0x8EAB, 'return_from_svc_1_workspace')

d.label(0x8EB3, 'done_cap_ws_count')

d.label(0x8EEE, 'loop_zero_workspace')

d.label(0x8F18, 'loop_copy_init_data')

d.label(0x8F2E, 'loop_alloc_handles')

d.label(0x8F40, 'read_station_id')

d.label(0x8F46, 'error_bad_station')

d.label(0x8F48, 'ws_init_data')
for i in range(3):
    d.byte(0x8F49 + i)

d.label(0x8F4C, 'store_station_id')

d.label(0x8F8E, 'loop_restore_ctx')

d.label(0x8FB0, 'loop_checksum_byte')

d.label(0x8FBA, 'loop_copy_to_ws')

d.label(0x8FBD, 'store_ws_byte')

d.label(0x8FCA, 'return_from_fs_shutdown')

d.label(0x8FD4, 'loop_sum_ws')

d.label(0x901E, 'done_print_newline')

d.label(0x9022, 'cmd_syntax_strings')

d.label(0x9022, 'syn_opt_dir')

d.label(0x902A, 'syn_iam')

d.label(0x9057, 'syn_object')

d.label(0x9060, 'syn_file_offset')

d.label(0x9083, 'syn_dir')

d.label(0x9089, 'syn_dir_num')

d.label(0x909A, 'syn_password')

d.label(0x90BD, 'syn_ps_type')

d.label(0x90D4, 'syn_access')

d.label(0x90F0, 'syn_rename')

d.label(0x910A, 'syn_opt_stn')

d.label(0x9117, 'syn_filename')

d.label(0x9122, 'cmd_syntax_table')
for i in range(13):
    d.byte(0x9122 + i)
d.expr(0x9122, 'syn_iam - cmd_syntax_strings - 2')
d.expr(0x9123, '(syn_opt_dir - cmd_syntax_strings - 1) AND &FF')
d.expr(0x9124, 'syn_iam - cmd_syntax_strings - 1')
d.expr(0x9125, 'syn_object - cmd_syntax_strings - 1')
d.expr(0x9126, 'syn_file_offset - cmd_syntax_strings - 1')
d.expr(0x9127, 'syn_dir - cmd_syntax_strings - 1')
d.expr(0x9128, 'syn_dir_num - cmd_syntax_strings - 1')
d.expr(0x9129, 'syn_password - cmd_syntax_strings - 1')
d.expr(0x912A, 'syn_ps_type - cmd_syntax_strings - 1')
d.expr(0x912B, 'syn_access - cmd_syntax_strings - 1')
d.expr(0x912C, 'syn_rename - cmd_syntax_strings - 1')
d.expr(0x912D, 'syn_opt_stn - cmd_syntax_strings - 1')
d.expr(0x912E, 'syn_filename - cmd_syntax_strings - 1')

d.label(0x9140, 'add_ascii_base')

d.label(0x914D, 'loop_next_char')

d.label(0x9153, 'load_char')

d.label(0x916B, 'resume_caller')

d.label(0x917D, 'next_hex_char')

d.label(0x9188, 'check_digit_range')

d.label(0x9198, 'skip_if_not_hex')

d.label(0x919A, 'extract_digit_value')

d.label(0x91AE, 'next_dec_char')

d.label(0x91DA, 'done_parse_num')

d.label(0x91E3, 'validate_station')

d.label(0x91F9, 'return_parsed')

d.label(0x91FB, 'handle_dot_sep')

d.label(0x9211, 'error_overflow')

d.label(0x9229, 'error_bad_number')

d.label(0x9235, 'error_bad_param')

d.label(0x9244, 'error_bad_net_num')

d.label(0x9266, 'return_from_digit_test')

d.label(0x9267, 'not_a_digit')

d.label(0x9277, 'begin_prot_encode')

d.label(0x927B, 'loop_encode_prot')

d.label(0x9283, 'skip_clear_prot')

d.label(0x9286, 'prot_bit_encode_table')
for i in range(11):
    d.byte(0x9286 + i)

d.label(0x92A6, 'loop_cmp_handle')

d.label(0x92AF, 'return_from_cmp_handle')

d.label(0x92B0, 'fscv_7_read_handles')

d.label(0x92E1, 'done_conn_flag')

d.label(0x9329, 'loop_scan_flag')

d.label(0x9332, 'loop_copy_name')

d.label(0x933E, 'append_space')

d.label(0x9348, 'return_from_copy_cmd_name')

d.label(0x934F, 'loop_skip_spaces')

d.label(0x9358, 'check_open_quote')

d.label(0x9363, 'loop_copy_arg_char')

d.label(0x9371, 'store_arg_char')

d.label(0x939B, 'loop_copy_rename')

d.label(0x93A2, 'error_bad_rename')

d.label(0x93AE, 'store_rename_char')

d.label(0x93BC, 'skip_rename_spaces')

d.label(0x93EE, 'setup_fs_root')

d.label(0x93F0, 'loop_copy_fs_num')

d.label(0x9405, 'check_fs_dot')

d.label(0x940C, 'parse_fs_dot_dir')

d.label(0x943C, 'dir_found_send')

d.label(0x9462, 'dir_pass_simple')

d.label(0x9476, 'loop_init_txcb')

d.label(0x9486, 'skip_txcb_dest')

d.label(0x948B, 'txcb_init_template')
for i in range(12):
    d.byte(0x948B + i)

d.label(0x9491, 'bit_test_ff')

d.label(0x94B4, 'txcb_copy_carry_clr')

d.label(0x94B5, 'txcb_copy_carry_set')

d.label(0x94BB, 'loop_copy_vset_stn')

d.label(0x94D3, 'use_lib_station')

d.label(0x94D9, 'done_vset_station')

d.label(0x94F8, 'loop_next_reply')

d.label(0x9502, 'process_reply_code')

d.label(0x9504, 'return_from_recv_reply')

d.label(0x9505, 'handle_disconnect')

d.label(0x950E, 'store_reply_status')

d.label(0x951B, 'check_data_loss')

d.label(0x9520, 'loop_scan_channels')

d.label(0x9547, 'reload_reply_status')

d.label(0x9551, 'build_error_block')

d.label(0x955B, 'setup_error_copy')

d.label(0x955D, 'loop_copy_error')

d.label(0x9580, 'lang_1_remote_boot')

d.label(0x9586, 'done_commit_state')

d.label(0x9589, 'init_remote_session')

d.label(0x95AE, 'lang_3_execute_at_0100')

d.label(0x95BE, 'lang_4_remote_validated')

d.label(0x95CE, 'lang_0_insert_remote_key')

d.label(0x95EE, 'init_poll_counters')

d.label(0x95F4, 'loop_poll_tx')

d.label(0x9607, 'done_poll_tx')

d.label(0x9619, 'return_from_cond_save_err')

d.label(0x961A, 'build_no_reply_error')

d.label(0x962A, 'loop_copy_no_reply_msg')

d.label(0x9636, 'done_no_reply_msg')

d.label(0x9649, 'skip_if_not_a')

d.label(0x9651, 'mask_error_class')

d.label(0x9668, 'loop_copy_station_msg')

d.label(0x9674, 'done_station_msg')

d.label(0x9686, 'suffix_not_listening')

d.label(0x9688, 'load_suffix_offset')

d.label(0x968C, 'loop_copy_suffix')

d.label(0x9698, 'done_suffix')

d.label(0x969A, 'build_simple_error')

d.label(0x96A9, 'loop_copy_error_msg')

d.label(0x96AF, 'check_msg_terminator')

d.label(0x96C4, 'loop_copy_bad_prefix')

d.label(0x96DD, 'write_error_num_and_str')

d.label(0x96E7, 'loop_copy_inline_str')

d.label(0x96FA, 'trigger_brk')

d.label(0x96FD, 'handle_net_error')

d.label(0x971F, 'close_exec_file')

d.label(0x9722, 'close_spool_exec')

d.label(0x972C, 'done_close_files')

d.label(0x9734, 'loop_copy_channel_msg')

d.label(0x9740, 'append_error_number')

d.label(0x9767, 'append_station_num')

d.label(0x9794, 'loop_count_digit')

d.label(0x97A4, 'store_digit')

d.label(0x97AC, 'return_from_store_digit')

d.label(0x97AD, 'net_error_lookup_data')
for i in range(12):
    d.byte(0x97AD + i)
d.expr(0x97AD, 'error_msg_table - error_msg_table')
d.expr(0x97AE, 'msg_net_error - error_msg_table')
d.expr(0x97AF, 'msg_station - error_msg_table')
d.expr(0x97B0, 'msg_no_clock - error_msg_table')
d.expr(0x97B1, 'msg_escape - error_msg_table')
d.expr(0x97B2, 'msg_escape - error_msg_table')
d.expr(0x97B3, 'msg_escape - error_msg_table')
d.expr(0x97B4, 'msg_bad_option - error_msg_table')
d.expr(0x97B5, 'msg_no_reply - error_msg_table')
d.expr(0x97B6, 'msg_not_listening - error_msg_table')
d.expr(0x97B7, 'msg_on_channel - error_msg_table')
d.expr(0x97B8, 'msg_not_present - error_msg_table')

d.label(0x9846, 'set_timeout')

d.label(0x984F, 'start_tx_attempt')

d.label(0x9865, 'loop_retry_tx')

d.label(0x986B, 'loop_tx_delay')

d.label(0x9873, 'try_alternate_phase')

d.label(0x987E, 'tx_send_error')

d.label(0x9882, 'tx_success')

d.label(0x9888, 'pass_txbuf_init_table')
for i in range(12):
    d.byte(0x9888 + i)

d.label(0x989E, 'loop_copy_template')

d.label(0x98AB, 'skip_template_byte')

d.label(0x98B8, 'start_pass_tx')

d.label(0x98C4, 'done_pass_retries')

d.label(0x98D9, 'loop_poll_pass_tx')

d.label(0x98DE, 'restore_retry_state')

d.label(0x98EB, 'loop_pass_tx_delay')

d.label(0x98F3, 'pass_tx_success')

d.label(0x98F8, 'loop_restore_txbuf')

d.label(0x9902, 'skip_restore_byte')

d.label(0x990A, 'loop_copy_text_ptr')

d.label(0x991B, 'loop_gsread_char')

d.label(0x9926, 'terminate_buf')

d.label(0x994C, 'copy_arg_and_enum')

d.label(0x9969, 'copy_ws_then_fsopts')

d.label(0x996F, 'setup_txcb_addrs')

d.label(0x9971, 'loop_copy_addrs')

d.label(0x998C, 'loop_copy_offsets')

d.label(0x99A1, 'loop_swap_and_send')

d.label(0x99A3, 'loop_copy_start_end')

d.label(0x99B7, 'loop_verify_addrs')

d.label(0x99C2, 'return_from_txcb_swap')

d.label(0x99C3, 'check_display_type')

d.label(0x99C8, 'setup_dir_display')

d.label(0x99CD, 'loop_compute_diffs')

d.label(0x99EB, 'loop_copy_fs_options')

d.label(0x9A0C, 'send_info_request')

d.label(0x9A19, 'setup_txcb_transfer')

d.label(0x9A1F, 'recv_reply')

d.label(0x9A22, 'store_result')

d.label(0x9A2F, 'loop_copy_file_info')

d.label(0x9A32, 'store_prot_byte')

d.label(0x9A40, 'loop_print_filename')

d.label(0x9A64, 'loop_print_hex_byte')

d.label(0x9A74, 'loop_copy_fsopts_byte')

d.label(0x9A83, 'return_from_advance_y')

d.label(0x9A87, 'loop_copy_ws_byte')

d.label(0x9A96, 'discard_handle_match')

d.label(0x9AA0, 'init_transfer_addrs')

d.label(0x9AAB, 'loop_copy_addr_offset')

d.label(0x9ABD, 'loop_check_vs_limit')

d.label(0x9AC9, 'clamp_end_to_limit')

d.label(0x9ACB, 'loop_copy_limit')

d.label(0x9AD2, 'set_port_and_ctrl')

d.label(0x9AEF, 'dispatch_osword_op')

d.label(0x9AFB, 'dispatch_ops_1_to_6')

d.label(0x9B13, 'loop_copy_fsopts_4')

d.label(0x9B20, 'setup_save_access')

d.label(0x9B2A, 'loop_copy_fsopts_8')

d.label(0x9B35, 'send_save_or_access')

d.label(0x9B3C, 'send_delete_request')

d.label(0x9B41, 'send_request_vset')

d.label(0x9B47, 'skip_if_error')

d.label(0x9B4C, 'setup_write_access')

d.label(0x9B56, 'read_cat_info')

d.label(0x9B78, 'loop_copy_cat_info')

d.label(0x9B85, 'loop_copy_ext_info')

d.label(0x9B91, 'return_with_handle')

d.label(0x9B92, 'done_osword_op')

d.label(0x9B9C, 'loop_copy_cmdline_char')

d.label(0x9BA8, 'pad_with_spaces')

d.label(0x9BB3, 'loop_copy_buf_char')

d.label(0x9BB5, 'copy_from_buf_entry')

d.label(0x9BD0, 'validate_chan_close')

d.label(0x9BD5, 'error_invalid_chan')

d.label(0x9BD8, 'check_chan_range')

d.label(0x9BE8, 'loop_copy_fcb_fields')

d.label(0x9BF8, 'dispatch_osfind_op')

d.label(0x9C03, 'osfind_with_channel')

d.label(0x9C35, 'loop_copy_zp_to_buf')

d.label(0x9C4B, 'done_return_flag')

d.label(0x9C4E, 'osargs_read_op')

d.label(0x9C5D, 'loop_copy_reply_to_zp')

d.label(0x9C6A, 'osargs_ptr_dispatch')

d.label(0x9C8C, 'osargs_write_ptr')

d.label(0x9C93, 'loop_copy_ptr_to_buf')

d.label(0x9CC4, 'close_all_fcbs')

d.label(0x9CD5, 'osfind_close_or_open')

d.label(0x9CE0, 'loop_copy_reply_data')

d.label(0x9CEC, 'done_file_open')

d.label(0x9CEE, 'clear_result')

d.label(0x9CF0, 'shift_and_finalise')

d.label(0x9CF3, 'alloc_fcb_for_open')

d.label(0x9D2A, 'loop_shift_filename')

d.label(0x9D6B, 'check_open_mode')

d.label(0x9D7D, 'alloc_fcb_with_flags')

d.label(0x9D81, 'store_fcb_flags')

d.label(0x9D87, 'done_osfind')

d.label(0x9D8A, 'close_all_channels')

d.label(0x9DA3, 'close_specific_chan')

d.label(0x9DA9, 'send_close_request')

d.label(0x9DBB, 'done_close')

d.label(0x9DBE, 'clear_single_fcb')

d.label(0x9DC8, 'fscv_0_opt_entry')

d.label(0x9DD2, 'osargs_dispatch')

d.label(0x9DD5, 'store_display_flag')

d.label(0x9DDA, 'error_osargs')

d.label(0x9DDF, 'send_osargs_request')

d.label(0x9DEE, 'fscv_1_eof')

d.label(0x9E09, 'mark_not_found')

d.label(0x9E0B, 'restore_and_return')

d.label(0x9E19, 'loop_adjust_byte')

d.label(0x9E25, 'subtract_ws_byte')

d.label(0x9E28, 'store_adjusted_byte')

d.label(0x9E42, 'skip_if_out_of_range')

d.label(0x9E45, 'valid_osgbpb_op')

d.label(0x9E50, 'load_chan_handle')

d.label(0x9E8F, 'set_write_active')

d.label(0x9E92, 'setup_gbpb_request')

d.label(0x9EE8, 'loop_copy_opts_to_buf')

d.label(0x9EF3, 'skip_struct_hole')

d.label(0x9EFC, 'store_direction_flag')

d.label(0x9F0A, 'store_port_and_send')

d.label(0x9F27, 'loop_setup_addr_bytes')

d.label(0x9F3E, 'loop_copy_offset')

d.label(0x9F52, 'send_with_swap')

d.label(0x9F55, 'recv_and_update')

d.label(0x9F6D, 'send_osbput_data')

d.label(0x9F82, 'write_block_entry')

d.label(0x9F90, 'store_station_result')

d.label(0x9F92, 'loop_copy_opts_to_ws')

d.label(0x9FA4, 'handle_cat_update')

d.label(0x9FD8, 'loop_copy_to_host')

d.label(0x9FE5, 'tube_write_setup')

d.label(0x9FF2, 'set_tube_addr')

d.label(0x9FF7, 'loop_write_to_tube')

d.label(0xA000, 'loop_tube_delay')

d.label(0xA00F, 'update_cat_position')

d.label(0xA04B, 'clear_buf_after_write')

d.label(0xA04D, 'loop_clear_buf')

d.label(0xA067, 'loop_check_remaining')

d.label(0xA070, 'done_write_block')

d.label(0xA09B, 'print_current_fs')

d.label(0xA0BD, 'store_station_lo')

d.label(0xA0C5, 'skip_if_no_station')

d.label(0xA0C9, 'done_parse_fs_ps')

d.label(0xA0E4, 'net_1_read_handle')

d.label(0xA0EA, 'net_2_read_handle_entry')

d.label(0xA0F5, 'return_zero_uninit')

d.label(0xA0F7, 'store_pb_result')

d.label(0xA0FA, 'net_3_close_handle')

d.label(0xA109, 'mark_ws_uninit')

d.label(0xA133, 'dispatch_fs_cmd')

d.label(0xA142, 'restart_table_scan')

d.label(0xA14A, 'loop_match_char')

d.label(0xA159, 'skip_entry_chars')

d.label(0xA165, 'loop_skip_to_next')

d.label(0xA16A, 'check_separator')

d.label(0xA170, 'loop_check_sep_table')

d.label(0xA17C, 'sep_table_data')
for i in range(9):
    d.byte(0xA17C + i)

d.label(0xA185, 'separator_matched')

d.label(0xA187, 'loop_skip_trail_spaces')

d.label(0xA18D, 'skip_dot_and_spaces')

d.label(0xA191, 'check_cmd_flags')

d.label(0xA1A2, 'clear_v_flag')

d.label(0xA1A3, 'clear_c_flag')

d.label(0xA1A4, 'return_with_result')

d.label(0xA1A8, 'loop_scan_past_word')

d.label(0xA1A9, 'check_char_type')

d.label(0xA1B7, 'skip_sep_spaces')

d.label(0xA1BE, 'set_c_and_return')

d.label(0xA1C1, 'fscv_2_star_run')

d.label(0xA1CA, 'open_file_for_run')

d.label(0xA1E2, 'loop_check_handles')

d.label(0xA1EA, 'alloc_run_fcb')

d.label(0xA206, 'done_run_dispatch')

d.label(0xA209, 'try_library_path')

d.label(0xA21D, 'loop_find_name_end')

d.label(0xA225, 'loop_shift_name_right')

d.label(0xA230, 'loop_copy_lib_prefix')

d.label(0xA241, 'retry_with_library')

d.label(0xA243, 'restore_filename')

d.label(0xA245, 'loop_restore_name')

d.label(0xA25A, 'library_tried')

d.label(0xA26A, 'check_exec_addr')

d.label(0xA26C, 'loop_check_exec_bytes')

d.label(0xA27D, 'alloc_run_channel')

d.label(0xA291, 'library_dir_prefix')

d.label(0xA299, 'setup_oscli_arg')

d.label(0xA2A2, 'loop_read_gs_string')

d.label(0xA2A8, 'loop_skip_trailing')

d.label(0xA2EF, 'dispatch_via_vector')

d.label(0xA2FA, 'fsreply_5_set_lib')

d.label(0xA303, 'loop_search_stn_bit2')

d.label(0xA319, 'done_search_bit2')

d.label(0xA327, 'set_flags_bit2')

d.label(0xA32E, 'loop_search_stn_bit3')

d.label(0xA344, 'done_search_bit3')

d.label(0xA352, 'set_flags_bit3')

d.label(0xA365, 'loop_search_stn_boot')

d.label(0xA37B, 'done_search_boot')

d.label(0xA389, 'set_flags_boot')

d.label(0xA38B, 'store_stn_flags_restore')

d.label(0xA38E, 'jmp_restore_fs_ctx')

d.label(0xA391, 'fsreply_1_copy_handles_boot')

d.label(0xA39B, 'fsreply_2_copy_handles')

d.label(0xA3B4, 'check_auto_boot_flag')

d.label(0xA3DF, 'boot_oscli_lo_table')
for i in range(4):
    d.byte(0xA3DF + i)

d.label(0xA3E3, 'load_boot_type')

d.label(0xA3F1, 'cmd_table_fs_lo')

d.label(0xA3F2, 'cmd_table_fs_hi')

d.label(0xA477, 'cmd_table_nfs_iam')

d.label(0xBBB7, 'loop_copy_osword_data')

d.label(0xA522, 'return_from_osword_setup')
d.comment(0xA523, """OSWORD dispatch table (7 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_8_osword.
Maps OSWORD codes &0E-&14 to handler routines.""")

d.label(0xA523, 'osword_dispatch_lo_table')

d.label(0xA52A, 'osword_dispatch_hi_table')
for i in range(7):
    d.rts_code_ptr(0xA523 + i, 0xA52A + i)
d.comment(0xA523, 'lo-&0E: Read clock', align=Align.INLINE)
d.comment(0xA523, 'lo-&13: Misc operations', align=Align.INLINE)
d.comment(0xA52B, 'hi-&0E: Read clock', align=Align.INLINE)
d.comment(0xA52C, 'hi-&0F: (unimplemented)', align=Align.INLINE)
d.comment(0xA52D, 'hi-&10: Transmit', align=Align.INLINE)
d.comment(0xA52F, 'hi-&12: Read station info', align=Align.INLINE)
d.comment(0xA531, 'hi-&14: Bridge/net config', align=Align.INLINE)

d.label(0xA531, 'osword_0e_handler')

d.label(0xA53E, 'return_from_osword_0e')

d.label(0xA53F, 'save_txcb_and_convert')

d.label(0xA58C, 'loop_copy_bcd_to_pb')

d.label(0xA59C, 'loop_bcd_add')

d.label(0xA5A2, 'done_bcd_convert')

d.label(0xA5A4, 'osword_10_handler')

d.label(0xA5AD, 'setup_ws_rx_ptrs')

d.label(0xA5C1, 'osword_11_handler')

d.label(0xA5D1, 'loop_find_rx_slot')

d.label(0xA5E5, 'store_rx_slot_found')

d.label(0xA5EA, 'use_specified_slot')

d.label(0xA600, 'loop_copy_slot_data')

d.label(0xA601, 'copy_pb_and_mark')

d.label(0xA60E, 'increment_and_retry')

d.label(0xA613, 'store_rx_result')

d.label(0xA615, 'osword_11_done')

d.label(0xA619, 'osword_12_handler')

d.label(0xA62E, 'osword_13_dispatch')

d.label(0xA63B, 'return_from_osword_13')

d.label(0xA63C, 'osword_13_lo_table')

d.label(0xA64E, 'osword_13_hi_table')
for i in range(18):
    d.rts_code_ptr(0xA63C + i, 0xA64E + i)
d.entry(0xA660)
d.entry(0xA673)
d.entry(0xA6E8)
d.entry(0xA6EB)

d.label(0xA665, 'nfs_inactive_exit')

d.label(0xA668, 'read_station_bytes')

d.label(0xA66A, 'loop_copy_station')

d.label(0xA67F, 'loop_store_station')

d.label(0xA68C, 'scan_fcb_entry')

d.label(0xA6B6, 'check_handle_2')

d.label(0xA6CB, 'check_handle_3')

d.label(0xA6E0, 'store_updated_status')

d.label(0xA6E4, 'next_fcb_entry')

d.label(0xA6EC, 'setup_csd_copy')

d.label(0xA6FE, 'copy_ws_byte_to_pb')

d.label(0xA727, 'return_from_write_ws_pair')

d.label(0xA73B, 'loop_copy_handles')

d.label(0xA749, 'return_zero_in_pb')

d.label(0xA74F, 'start_set_handles')

d.label(0xA751, 'validate_handle')

d.label(0xA761, 'handle_invalid')

d.label(0xA768, 'check_handle_alloc')

d.label(0xA78E, 'next_handle_slot')

d.label(0xA795, 'assign_handle_2')

d.label(0xA7AC, 'assign_handle_3')

d.label(0xA7C3, 'loop_scan_fcb_flags')

d.label(0xA7D5, 'no_flag_match')

d.label(0xA7D6, 'clear_flag_bits')

d.label(0xA7DE, 'next_flag_entry')

d.label(0xA7FE, 'store_a_to_pb_1')

d.label(0xA837, 'bridge_found')

d.label(0xA840, 'compare_bridge_status')

d.label(0xA841, 'bridge_ws_init_data')

d.label(0xA847, 'use_default_station')

d.label(0xA84A, 'store_bridge_station')

d.label(0xA84C, 'return_from_bridge_query')

d.label(0xA84D, 'bridge_txcb_init_table')

d.label(0xA859, 'bridge_rxcb_init_data')
for i in range(4):
    d.byte(0xA84D + i)
for i in range(14):
    d.byte(0xA857 + i)

d.label(0xA875, 'loop_copy_bridge_init')

d.label(0xA889, 'loop_wait_ws_status')

d.label(0xA89D, 'loop_wait_tx_done')

d.label(0xA8B5, 'bridge_responded')

d.label(0xA8C4, 'return_from_bridge_poll')

d.label(0xA8C5, 'osword_14_handler')

d.label(0xA8D3, 'loop_copy_txcb_init')

d.label(0xA8DB, 'store_txcb_init_byte')

d.label(0xA903, 'loop_copy_ws_to_pb')

d.label(0xA935, 'handle_tx_request')

d.label(0xA94C, 'loop_send_pb_chars')

d.label(0xA962, 'loop_bridge_tx_delay')

d.label(0xA96B, 'handle_burst_xfer')

d.label(0xA98C, 'restore_regs_return')

d.label(0xA99E, 'osword_handler_lo_table')

d.label(0xA9A7, 'osword_handler_hi_table')
for i in range(9):
    d.rts_code_ptr(0xA99E + i, 0xA9A7 + i)
d.comment(0xA99E, """OSWORD handler dispatch table

9-entry PHA/PHA/RTS table for OSWORD numbers
0-8. push_osword_handler_addr indexes by the
OSWORD number, pushes the handler address-1,
then RTS dispatches to the handler with the
OSWORD number reloaded in A.""")
d.comment(0xA9A7, 'hi OSWORD 0: no-op (RTS)', align=Align.INLINE)
d.comment(0xA9A8, 'hi OSWORD 1: printer spool data', align=Align.INLINE)
d.comment(0xA9A9, 'hi OSWORD 2: printer spool data', align=Align.INLINE)
d.comment(0xA9AA, 'hi OSWORD 3: printer spool data', align=Align.INLINE)
d.comment(0xA9AB, 'hi OSWORD 4: clear carry + abort', align=Align.INLINE)
d.comment(0xA9AC, 'hi OSWORD 5: spool buffer check', align=Align.INLINE)
d.comment(0xA9AD, 'hi OSWORD 6: no-op (RTS)', align=Align.INLINE)
d.comment(0xA9AE, 'hi OSWORD 7: claim/release handler', align=Align.INLINE)
d.comment(0xA9AF, 'hi OSWORD 8: copy PB + abort', align=Align.INLINE)

d.label(0xA9E2, 'netv_claim_release')

d.label(0xA9FB, 'process_match_result')

d.label(0xAA04, 'save_tube_state')

d.label(0xAA06, 'loop_save_tube_bytes')

d.label(0xAA1D, 'loop_poll_ws_status')

d.label(0xAA2A, 'loop_restore_stack')

d.label(0xAA2E, 'store_stack_byte')

d.label(0xAA35, 'return_from_claim_release')

d.label(0xAA3E, 'return_from_match_rx_code')

d.label(0xAA3F, 'osword_claim_codes')
for i in range(18):
    d.byte(0xAA3F + i)

d.label(0xAA5B, 'copy_pb_to_ws')

d.label(0xAA5F, 'loop_copy_pb_to_ws')

d.label(0xAA8A, 'loop_copy_ws_template')

d.label(0xAA9F, 'store_tx_ptr_hi')

d.label(0xAAA1, 'select_store_target')

d.label(0xAAA7, 'store_via_rx_ptr')

d.label(0xAAA9, 'advance_template_idx')

d.label(0xAAAD, 'done_ws_template_copy')

d.label(0xAAB1, 'ws_txcb_template_data')
for i in range(39):
    d.byte(0xAAB1 + i)

d.label(0xAAD8, 'netv_spool_check')

d.label(0xAAEC, 'return_from_spool_reset')

d.label(0xAAED, 'netv_print_data')

d.label(0xAAFC, 'loop_drain_printer_buf')

d.label(0xAB33, 'done_spool_ctrl')

d.label(0xAB75, 'check_spool_state')

d.label(0xAB84, 'start_spool_retry')

d.label(0xAB89, 'loop_copy_spool_tx')

d.label(0xABA8, 'loop_copy_spool_rx')

d.label(0xABB5, 'store_spool_rx_byte')

d.label(0xABB7, 'advance_spool_rx_idx')

d.label(0xABDE, 'spool_tx_succeeded')

d.label(0xABF3, 'spool_tx_retry')

d.label(0xAC10, 'error_printer_jammed')

d.label(0xAC30, 'loop_scan_disconnect')

d.label(0xAC3F, 'verify_stn_match')

d.label(0xAC4A, 'send_disconnect_status')

d.label(0xAC67, 'store_tx_ctrl_byte')

d.label(0xAC6F, 'loop_wait_disc_tx_ack')

d.label(0xAC80, 'tx_econet_txcb_template')
for i in range(12):
    d.byte(0xAC80 + i)

d.label(0xAC8C, 'rx_palette_txcb_template')
for i in range(12):
    d.byte(0xAC8C + i)

d.label(0xAC98, 'lang_2_save_palette_vdu')

d.label(0xACAF, 'loop_read_palette')

d.label(0xAD0D, 'osbyte_mode_read_codes')
for i in range(3):
    d.byte(0xAD0D + i)

d.label(0xAD20, 'parse_cdir_size')

d.label(0xAD29, 'loop_find_alloc_size')

d.label(0xAD2F, 'done_cdir_size')

d.label(0xAD43, 'cdir_alloc_size_table')
for i in range(27):
    d.byte(0xAD44 + i)

d.label(0xAD6F, 'ex_set_lib_flag')

d.label(0xAD80, 'fscv_5_cat')

d.label(0xAD89, 'cat_set_lib_flag')

d.label(0xAD96, 'setup_ex_request')

d.label(0xADB2, 'store_owner_flags')

d.label(0xADE3, 'print_public_label')

d.label(0xADED, 'send_dir_info_req')

d.label(0xAE1C, 'loop_print_option_str')

d.label(0xAE27, 'print_dir_header')

d.label(0xAE4F, 'setup_ex_pagination')

d.label(0xAE6F, 'loop_scan_entry_data')

d.label(0xAE8F, 'jmp_osnewl')

d.label(0xAEBB, 'loop_shift_str_left')

d.label(0xAEC9, 'loop_trim_trailing')

d.label(0xAED8, 'done_strip_prefix')

d.label(0xAEDA, 'return_from_strip_prefix')

d.label(0xAEDB, 'check_hash_prefix')

d.label(0xAEDF, 'error_bad_prefix')

d.label(0xAEE2, 'check_colon_prefix')

d.label(0xAEF1, 'set_fs_select_flag')

d.label(0xAEFB, 'option_str_offset_data')

d.label(0xAEFF, 'roff_off_string')

d.label(0xAF07, 'loop_copy_char')

d.label(0xAF14, 'restore_after_check')

d.label(0xAF16, 'advance_positions')

d.label(0xAF3E, 'fsreply_0_print_dir')

d.label(0xAF40, 'loop_scan_entries')

d.label(0xAF5A, 'print_col_newline')

d.label(0xAF5C, 'print_entry_char')

d.label(0xAF5F, 'next_col_entry')

d.label(0xAF72, 'done_extra_arg_check')

d.label(0xAF9D, 'loop_divide_digit')

d.label(0xAFAD, 'print_nonzero_digit')

d.label(0xAFC0, 'loop_advance_char')

d.label(0xAFCD, 'loop_skip_space_chars')

d.label(0xAFF8, 'done_ps_available')

d.label(0xB01B, 'loop_copy_ps_tmpl')

d.label(0xB025, 'no_ps_name_given')

d.label(0xB028, 'save_ps_cmd_ptr')

d.label(0xB032, 'loop_pad_ps_name')

d.label(0xB04A, 'loop_read_ps_char')

d.label(0xB058, 'done_ps_name_parse')

d.label(0xB06B, 'loop_pop_ps_slot')

d.label(0xB091, 'done_ps_slot_mark')

d.label(0xB099, 'done_ps_scan')

d.label(0xB0AE, 'print_ps_now')

d.label(0xB0B6, 'done_ps_status_msg')

d.label(0xB0B8, 'store_ps_station')

d.label(0xB0DA, 'print_server_is_suffix')

d.label(0xB108, 'loop_scan_ps_slots')

d.label(0xB118, 'skip_next_ps_slot')

d.label(0xB11C, 'reinit_ps_slot')

d.label(0xB13F, 'write_ps_slot_link_addr')

d.label(0xB144, 'done_ps_slot_scan')

d.label(0xB153, 'loop_ps_delay')

d.label(0xB16F, 'loop_push_ps_name')

d.label(0xB179, 'loop_pop_ps_name')

d.label(0xB18B, 'loop_copy_tx_hdr')

d.label(0xB194, 'ps_tx_header_template')
for i in range(4):
    d.byte(0xB194 + i)

d.label(0xB1A8, 'skip_if_local_net')

d.label(0xB1B1, 'print_station_only')

d.label(0xB1B7, 'ps_slot_txcb_template')
for i in range(12):
    d.byte(0xB1B7 + i)

d.label(0xB205, 'no_poll_name_given')

d.label(0xB208, 'skip_if_no_poll_arg')

d.label(0xB210, 'loop_pad_poll_name')

d.label(0xB228, 'loop_read_poll_char')

d.label(0xB236, 'done_poll_name_parse')

d.label(0xB253, 'loop_print_poll_name')

d.label(0xB261, 'done_poll_name_print')

d.label(0xB267, 'loop_pop_poll_slot')

d.label(0xB29C, 'check_poll_jammed')

d.label(0xB2A0, 'print_poll_jammed')

d.label(0xB2AC, 'check_poll_busy')

d.label(0xB2D4, 'done_poll_status_line')

d.label(0xB2D7, 'done_poll_slot_mark')

d.label(0xB2E2, 'loop_copy_slot_tmpl')

d.label(0xB2ED, 'subst_rx_page_byte')

d.label(0xB2EF, 'store_slot_tmpl_byte')

d.label(0xB305, 'done_uppercase_store')

d.label(0xB316, 'parse_prot_keywords')

d.label(0xB31A, 'loop_match_prot_attr')

d.label(0xB32C, 'prot_check_arg_end')

d.label(0xB335, 'done_prot_args')

d.label(0xB336, 'store_prot_mask')

d.label(0xB347, 'loop_match_unprot_attr')

d.label(0xB369, 'request_next_wipe')

d.label(0xB39C, 'check_wipe_attr')

d.label(0xB39F, 'loop_check_if_locked')

d.label(0xB3A3, 'skip_wipe_locked')

d.label(0xB3A8, 'check_wipe_dir')

d.label(0xB3B1, 'show_wipe_prompt')

d.label(0xB3B5, 'loop_copy_wipe_name')

d.label(0xB3D9, 'loop_print_wipe_info')

d.label(0xB3ED, 'check_wipe_response')

d.label(0xB3FF, 'loop_build_wipe_cmd')

d.label(0xB408, 'skip_if_not_space')

d.label(0xB40C, 'set_wipe_cr_end')

d.label(0xB40E, 'store_wipe_tx_char')

d.label(0xB41D, 'skip_wipe_to_next')

d.label(0xB423, 'use_wipe_leaf_name')

d.label(0xB424, 'loop_copy_wipe_leaf')

d.label(0xB44C, 'loop_clear_chan_table')

d.label(0xB45C, 'loop_mark_chan_avail')

d.label(0xB475, 'error_chan_out_of_range')

d.label(0xB477, 'return_chan_index')

d.label(0xB483, 'error_chan_not_found')

d.label(0xB487, 'net_channel_err_string')

d.label(0xB4C1, 'error_chan_not_here')

d.label(0xB4CC, 'loop_copy_chan_err_str')

d.label(0xB4DF, 'loop_append_err_suffix')

d.label(0xB50C, 'loop_scan_fcb_slots')

d.label(0xB51A, 'done_found_free_slot')

d.label(0xB557, 'return_alloc_success')

d.label(0xB55A, 'skip_set_carry')

d.label(0xB55F, 'loop_scan_fcb_down')

d.label(0xB563, 'skip_if_slots_done')

d.label(0xB577, 'done_check_station')

d.label(0xB59B, 'loop_find_fcb')

d.label(0xB5A2, 'skip_if_no_wrap')

d.label(0xB5AC, 'done_check_fcb_status')

d.label(0xB5B6, 'done_select_fcb')

d.label(0xB5B7, 'loop_scan_empty_fcb')

d.label(0xB5BE, 'done_test_empty_slot')

d.label(0xB5CD, 'skip_if_modified_fcb')

d.label(0xB5EA, 'loop_clear_counters')

d.label(0xB63B, 'done_restore_offset')

d.label(0xB661, 'done_clear_fcb_active')

d.label(0xB66C, 'loop_save_tx_context')

d.label(0xB67F, 'done_save_context')

d.label(0xB682, 'loop_find_pending_fcb')

d.label(0xB6C6, 'done_init_wipe')

d.label(0xB6EA, 'done_calc_offset')

d.label(0xB709, 'loop_clear_buffer')

d.label(0xB70E, 'done_set_fcb_active')

d.label(0xB718, 'loop_restore_workspace')

d.label(0xB723, 'loop_restore_tx_buf')

d.label(0xB72D, 'loop_save_before_match')

d.label(0xB732, 'loop_reload_attr')

d.label(0xB735, 'loop_next_fcb_slot')

d.label(0xB74F, 'done_test_fcb_active')

d.label(0xB788, 'return_test_offset')

d.label(0xB7AB, 'loop_process_fcb')

d.label(0xB7B6, 'done_flush_fcb')

d.label(0xB7BC, 'done_advance_fcb')

d.label(0xB7ED, 'done_read_fcb_byte')

d.label(0xB817, 'error_end_of_file')

d.label(0xB828, 'done_load_from_buf')

d.label(0xB87A, 'done_test_write_flag')

d.label(0xB888, 'done_find_write_fcb')

d.label(0xB898, 'done_check_buf_offset')

d.label(0xB8AC, 'done_set_dirty_flag')

d.label(0xB8CB, 'done_inc_byte_count')

d.label(0xB95E, 'loop_copy_wipe_err_msg')

d.label(0xB96B, 'done_terminate_wipe_err')

d.label(0xB974, 'done_toggle_station')

d.label(0xB9A0, 'open_and_read_file')

d.label(0x0406, 'tube_addr_data_dispatch')

d.label(0x0421, 'clear_tube_claim')

d.label(0x83F5, 'discard_reset_rx')

d.label(0x83F8, 'reset_adlc_rx_listen')

d.label(0x83FB, 'set_nmi_rx_scout')

d.label(0x850F, 'setup_sr_tx')

d.label(0x853E, 'tx_done_dispatch_lo')

d.label(0x854C, 'tx_done_econet_event')

d.label(0x8554, 'tx_done_fire_event')

d.label(0x8AEA, 'scan_remote_keys')

d.label(0x8B02, 'save_text_ptr')

d.label(0x8B8D, 'help_print_nfs_cmds')

d.label(0x8B98, 'print_cmd_table')

d.label(0x8BAB, 'print_cmd_table_loop')

d.label(0x8C33, 'help_wrap_if_serial')

d.label(0x8C9F, 'print_version_header')

d.label(0x8CB9, 'get_ws_page')

d.label(0x8CC0, 'setup_ws_ptr')

d.label(0x8CFC, 'notify_new_fs')

d.label(0x8D05, 'call_fscv')

d.label(0x8D08, 'issue_svc_15')

d.label(0x8D17, 'check_credits_easter_egg')

d.label(0x8E09, 'clear_if_station_match')

d.label(0x8E14, 'return_from_station_match')

d.label(0x8E20, 'pass_send_cmd')

d.label(0x8E24, 'send_cmd_and_dispatch')

d.label(0x8E43, 'dir_op_dispatch')

d.label(0x8E52, 'push_dispatch_lo')

d.label(0x8E8C, 'osbyte_x0_y0')

d.label(0x8EAC, 'store_ws_page_count')

d.label(0x8F5D, 'init_adlc_and_vectors')

d.label(0x8F70, 'write_vector_entry')

d.label(0x8F8C, 'restore_fs_context')

d.label(0x8F99, 'fscv_6_shutdown')

d.label(0x8FCB, 'verify_ws_checksum')

d.label(0x8FE4, 'error_net_checksum')

d.label(0x8FF1, 'print_station_id')

d.label(0x912F, 'print_hex_byte')

d.label(0x9138, 'print_hex_nybble')

d.label(0x916E, 'parse_addr_arg')

d.label(0x9208, 'err_bad_hex')

d.label(0x9215, 'err_bad_station_num')

d.label(0x9258, 'is_decimal_digit')

d.label(0x9260, 'is_dec_digit_only')

d.label(0x9269, 'get_access_bits')

d.label(0x9273, 'get_prot_bits')

d.label(0x9291, 'set_text_and_xfer_ptr')

d.label(0x9295, 'set_xfer_params')

d.label(0x929B, 'set_options_ptr')

d.label(0x929F, 'clear_escapable')

d.label(0x92A4, 'cmp_5byte_handle')

d.label(0x92B5, 'set_conn_active')

d.label(0x92CC, 'clear_conn_active')

d.label(0x92FA, 'error_bad_filename')

d.label(0x9309, 'check_not_ampersand')

d.label(0x9311, 'read_filename_char')

d.label(0x9322, 'send_fs_request')

d.label(0x9327, 'copy_fs_cmd_name')

d.label(0x9349, 'parse_quoted_arg')

d.label(0x9465, 'init_txcb_bye')

d.label(0x9467, 'init_txcb_port')

d.label(0x9473, 'init_txcb')

d.label(0x9497, 'send_request_nowrite')

d.label(0x949B, 'send_request_write')

d.label(0x94AD, 'save_net_tx_cb')

d.label(0x94AE, 'save_net_tx_cb_vset')

d.label(0x94DA, 'prep_send_tx_cb')

d.label(0x94F0, 'recv_and_process_reply')

d.label(0x9570, 'check_escape')

d.label(0x9576, 'raise_escape_error')

d.label(0x95DD, 'wait_net_tx_ack')

d.label(0x9611, 'cond_save_error_code')

d.label(0x9641, 'fixup_reply_status_a')

d.label(0x964C, 'load_reply_and_classify')

d.label(0x964E, 'classify_reply_error')

d.label(0x96B3, 'bad_str_anchor')

d.label(0x96F0, 'check_net_error_code')

d.label(0x974D, 'append_drv_dot_num')

d.label(0x9771, 'append_space_and_num')

d.label(0x977C, 'append_decimal_num')

d.label(0x978D, 'append_decimal_digit')

d.label(0x9837, 'init_tx_ptr_and_send')

d.label(0x983F, 'send_net_packet')

d.label(0x9894, 'init_tx_ptr_for_pass')

d.label(0x989C, 'setup_pass_txbuf')

d.label(0x9908, 'load_text_ptr_and_parse')

d.label(0x9913, 'gsread_to_buf')

d.label(0x9951, 'do_fs_cmd_iteration')

d.label(0x9998, 'send_txcb_swap_addrs')

d.label(0x9A57, 'print_load_exec_addrs')

d.label(0x9A62, 'print_5_hex_bytes')

d.label(0x9A72, 'copy_fsopts_to_zp')

d.label(0x9A7E, 'skip_one_and_advance5')

d.label(0x9A7F, 'advance_y_by_4')

d.label(0x9A84, 'copy_workspace_to_fsopts')

d.label(0x9A91, 'retreat_y_by_4')

d.label(0x9A92, 'retreat_y_by_3')

d.label(0x9A9A, 'check_and_setup_txcb')

d.label(0x9B95, 'format_filename_field')

d.label(0x9CC7, 'return_with_last_flag')

d.label(0x9CC9, 'finalise_and_return')

d.label(0x9E0F, 'update_addr_from_offset9')

d.label(0x9E14, 'update_addr_from_offset1')

d.label(0x9E16, 'add_workspace_to_fsopts')

d.label(0x9E17, 'adjust_fsopts_4bytes')

d.label(0x9ED2, 'lookup_cat_entry_0')

d.label(0x9ED6, 'lookup_cat_slot_data')

d.label(0x9EDD, 'setup_transfer_workspace')

d.label(0x9FD0, 'write_data_block')

d.label(0xA00C, 'tail_update_catalogue')

d.label(0xA073, 'tube_claim_c3')

d.label(0xA09E, 'print_fs_info_newline')

d.label(0xA0A7, 'parse_fs_ps_args')

d.label(0xA0CC, 'get_pb_ptr_as_index')

d.label(0xA0CE, 'byte_to_2bit_index')

d.label(0xA0E3, 'return_from_2bit_index')

d.label(0xA114, 'fscv_3_star_cmd')

d.label(0xA125, 'cmd_fs_reentry')

d.label(0xA127, 'error_syntax')

d.label(0xA140, 'match_fs_cmd')

d.label(0xA25D, 'error_bad_command')

d.label(0xA2F4, 'fsreply_3_set_csd')

d.label(0xA300, 'find_station_bit2')

d.label(0xA32B, 'find_station_bit3')

d.label(0xA362, 'flip_set_station_boot')

d.label(0xA3E8, 'boot_cmd_oscli')

d.label(0xA516, 'osword_setup_handler')

d.label(0xA595, 'bin_to_bcd')

d.label(0xA8E5, 'store_osword_pb_ptr')

d.label(0xA92B, 'store_ptr_at_ws_y')

d.label(0xA865, 'init_bridge_poll')

d.label(0xA976, 'enable_irq_and_poll')

d.label(0xA993, 'push_osword_handler_addr')

d.label(0xA9BE, 'tx_econet_abort')

d.label(0xAA7C, 'init_ws_copy_wide')

d.label(0xAA85, 'init_ws_copy_narrow')

d.label(0xAA89, 'ws_copy_vclr_entry')

d.label(0xAAE2, 'reset_spool_buf_state')

d.label(0xAB12, 'append_byte_to_rxbuf')

d.label(0xAB1B, 'handle_spool_ctrl_byte')

d.label(0xABFE, 'err_printer_busy')

d.label(0xAC24, 'send_disconnect_reply')

d.label(0xACDD, 'commit_state_byte')

d.label(0xACE4, 'serialise_palette_entry')

d.label(0xACF7, 'read_osbyte_to_ws_x0')

d.label(0xACF9, 'read_osbyte_to_ws')

d.label(0xAD41, 'cdir_dispatch_col')

d.label(0xAE82, 'print_10_chars')

d.label(0xAE92, 'parse_cmd_arg_y0')

d.label(0xAE94, 'parse_filename_arg')

d.label(0xAE97, 'parse_access_prefix')

d.label(0xAEB7, 'strip_token_prefix')

d.label(0xAF02, 'copy_arg_to_buf_x0')

d.label(0xAF04, 'copy_arg_to_buf')

d.label(0xAF06, 'copy_arg_validated')

d.label(0xAF2D, 'return_from_copy_arg')

d.label(0xAF32, 'mask_owner_access')

d.label(0xAF47, 'ex_print_col_sep')

d.label(0xAF85, 'print_num_no_leading')

d.label(0xAF88, 'print_decimal_3dig')

d.label(0xAF96, 'print_decimal_digit')

d.label(0xAFB4, 'return_from_print_digit')

d.label(0xAFB5, 'save_ptr_to_os_text')

d.label(0xAFC1, 'skip_to_next_arg')

d.label(0xAFD4, 'return_from_skip_arg')

d.label(0xAFD5, 'save_ptr_to_spool_buf')

d.label(0xAFE0, 'init_spool_drive')

d.label(0xB017, 'copy_ps_data_y1c')

d.label(0xB019, 'copy_ps_data')

d.label(0xB0C5, 'print_file_server_is')

d.label(0xB0CF, 'print_printer_server_is')

d.label(0xB0EA, 'load_ps_server_addr')

d.label(0xB0F6, 'pop_requeue_ps_scan')

d.label(0xB13E, 'write_ps_slot_hi_link')

d.label(0xB15E, 'write_ps_slot_byte_ff')

d.label(0xB165, 'write_two_bytes_inc_y')

d.label(0xB16D, 'reverse_ps_name_to_tx')

d.label(0xB198, 'print_station_addr')

d.label(0xB2DF, 'return_from_poll_slots')

d.label(0xB2E0, 'init_ps_slot_from_rx')

d.label(0xB2F7, 'store_char_uppercase')

d.label(0xB439, 'flush_and_read_char')

d.label(0xB449, 'init_channel_table')

d.label(0xB46B, 'attr_to_chan_index')

d.label(0xB47A, 'check_chan_char')

d.label(0xB482, 'err_net_chan_invalid')

d.label(0xB485, 'err_net_chan_not_found')

d.label(0xB4AD, 'lookup_chan_by_char')

d.label(0xB4EC, 'store_result_check_dir')

d.label(0xB4F2, 'check_not_dir')

d.label(0xB508, 'return_from_dir_check')

d.label(0xB509, 'alloc_fcb_slot')

d.label(0xB53D, 'alloc_fcb_or_error')

d.label(0xB559, 'close_all_net_chans')

d.label(0xB55D, 'scan_fcb_flags')

d.label(0xB586, 'match_station_net')

d.label(0xB594, 'return_from_match_stn')

d.label(0xB595, 'find_open_fcb')

d.label(0xB5D8, 'init_wipe_counters')

d.label(0xB5FB, 'start_wipe_pass')

d.label(0xB66A, 'save_fcb_context')

d.label(0xB721, 'restore_catalog_entry')

d.label(0xB730, 'find_matching_fcb')

d.label(0xB78B, 'inc_fcb_byte_count')

d.label(0xB798, 'return_from_inc_fcb_count')

d.label(0xB799, 'process_all_fcbs')

d.label(0xB92B, 'send_wipe_request')

d.label(0xB984, 'send_and_receive')

d.label(0xB9AA, 'loop_read_print_byte')

d.label(0xB9B6, 'done_print_escape')

d.label(0xB9C5, 'done_store_prev_char')

d.label(0xB9C7, 'loop_write_char')

d.label(0xB9CD, 'done_handle_line_end')

d.label(0xB9DA, 'done_normalise_crlf')

d.label(0xB9E7, 'done_write_newline')

d.label(0xB9ED, 'done_check_cr_lf')

d.label(0xB9F4, 'done_check_lf_cr')

d.label(0xB9F9, 'done_consume_pair')

d.label(0xB9FF, 'abort_if_escape')

d.label(0xBA04, 'error_escape_pressed')

d.label(0xBA22, 'loop_push_zero_buf')

d.label(0xBA33, 'loop_dump_line')

d.label(0xBA3A, 'loop_read_dump_byte')

d.label(0xBA4C, 'done_check_dump_eof')

d.label(0xBA53, 'loop_pop_stack_buf')

d.label(0xBA5A, 'done_check_boundary')

d.label(0xBA65, 'done_start_dump_addr')

d.label(0xBA67, 'loop_print_addr_byte')

d.label(0xBA78, 'loop_inc_dump_addr')

d.label(0xBA90, 'loop_print_dump_hex')

d.label(0xBA95, 'loop_next_dump_col')

d.label(0xBAAB, 'done_print_separator')

d.label(0xBAB6, 'loop_print_dump_ascii')

d.label(0xBABE, 'skip_non_printable')

d.label(0xBAC0, 'done_test_del')

d.label(0xBACF, 'done_end_dump_line')

d.label(0xBAD8, 'done_dump_eof')

d.label(0xBADD, 'print_dump_header')

d.label(0xBB03, 'print_hex_and_space')

d.label(0xBC3D, 'close_ws_file')

d.label(0xBC44, 'open_file_for_read')

d.label(0xBB0C, 'done_print_hex_space')

d.label(0xBC72, 'loop_skip_filename')

d.label(0xBC7D, 'loop_skip_fn_spaces')

d.label(0xBB0B, 'osasci_offset')

d.label(0xBB0E, 'parse_dump_range')

d.label(0xBB13, 'loop_clear_hex_accum')

d.label(0xBB1A, 'loop_parse_hex_digit')

d.label(0xBB39, 'done_mask_hex_digit')

d.label(0xBB40, 'loop_shift_nibble')

d.label(0xBB43, 'loop_rotate_hex_accum')

d.label(0xBB64, 'error_hex_overflow')

d.label(0xBB68, 'error_bad_hex_value')

d.label(0xBB6E, 'loop_skip_hex_spaces')

d.label(0xBB6F, 'done_test_hex_space')

d.label(0xBB77, 'init_dump_buffer')

d.label(0xBB90, 'loop_cmp_file_length')

d.label(0xBB9C, 'done_check_outside')

d.label(0xBBA2, 'error_outside_file')

d.label(0xBBB7, 'loop_copy_start_addr')

d.label(0xBBBC, 'done_advance_start')

d.label(0xBBD4, 'loop_copy_osfile_ptr')

d.label(0xBBE7, 'loop_shift_osfile_data')

d.label(0xBBF6, 'loop_check_ff_addr')

d.label(0xBC03, 'loop_zero_load_addr')

d.label(0xBC0A, 'done_parse_disp_base')

d.label(0xBC1F, 'done_add_disp_base')

d.label(0xBC24, 'loop_add_disp_bytes')

d.label(0xBC34, 'loop_store_disp_addr')

d.label(0xBC86, 'advance_x_by_8')

d.label(0xBC89, 'advance_x_by_4')

d.label(0xBC8C, 'inx4')

d.label(0xBE62, 'tube_vdu_dispatch')

d.label(0xBE73, 'loop_poll_r1_vdu_rom')

d.label(0xBE9E, 'loop_copy_reloc_pages')

d.label(0xBEB8, 'loop_copy_zp_workspace')


d.subroutine(0x8028, 'svc5_irq_check', title='Service 5: unrecognised interrupt (SR dispatch)', description="""Tests IFR bit 2 (SR complete) to check for a
shift register transfer complete. If SR is not set,
returns A=5 to pass the service call on. If SR is
set, saves registers, reads the VIA ACR, clears and
restores the SR mode bits from ws_0d64, then dispatches
the TX completion callback via the operation type stored
in tx_op_type. The indexed handler performs the completion
action (e.g. resuming background print spooling) before
returning with A=0 to claim the service call.""", on_entry={'a': '5 (service call number)', 'x': 'ROM slot', 'y': 'parameter'})


d.subroutine(0x805A, 'generate_event', title='Generate event via event vector', description="""Dispatches through the event vector (EVNTV)
to notify event handlers. Called with the event
number in A.""", on_entry={'A': 'event number'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})


d.subroutine(0x8A15, 'service_handler', title='Service call dispatch', description="""Handles service calls 1, 4, 8, 9, 13, 14, and 15.
Service 1: absolute workspace claim.
Service 4: unrecognised star command.
Service 8: unrecognised OSWORD.
Service 9: *HELP.
Service 13: ROM initialisation.
Service 14: ROM initialisation complete.
Service 15: vectors claimed.""", on_entry={'a': 'service call number', 'x': 'ROM slot', 'y': 'parameter'})

d.label(0x0020, 'tube_send_zero_r2')

d.label(0x0029, 'tube_brk_send_loop')

d.label(0x002A, 'tube_send_error_byte')

d.label(0x0032, 'tube_reset_stack')

d.label(0x0036, 'tube_main_loop')

d.label(0x003B, 'tube_handle_wrch')

d.label(0x0041, 'tube_poll_r2')

d.label(0x0050, 'tube_dispatch_cmd')

d.label(0x0051, 'tube_cmd_lo')

d.label(0x0053, 'tube_transfer_addr')

d.label(0x0054, 'tube_xfer_page')

d.label(0x0055, 'tube_xfer_addr_2')

d.label(0x0056, 'tube_xfer_addr_3')

d.label(0x0414, 'tube_release_claim')

d.label(0x0428, 'addr_claim_external')

d.label(0x0432, 'accept_new_claim')

d.label(0x0434, 'return_tube_init')

d.label(0x0435, 'tube_transfer_setup')

d.label(0x0437, 'setup_data_transfer')

d.label(0x0446, 'send_xfer_addr_bytes')

d.label(0x0463, 'skip_r3_flush')

d.label(0x0466, 'poll_r4_copro_ack')

d.label(0x0471, 'tube_sendw_complete')

d.label(0x047A, 'copro_ack_nmi_check')

d.label(0x0482, 'skip_nmi_release')

d.label(0x0483, 'return_tube_xfer')

d.label(0x0484, 'tube_begin')

d.label(0x048C, 'check_break_type')

d.label(0x0491, 'claim_addr_ff')

d.label(0x049D, 'next_rom_page')

d.label(0x04A6, 'send_rom_page_bytes')

d.label(0x04BC, 'skip_addr_carry')

d.label(0x04C7, 'tube_claim_default')

d.label(0x04CE, 'tube_init_reloc')

d.label(0x04E1, 'scan_copyright_end')

d.label(0x04F7, 'store_xfer_end_addr')

d.label(0x0518, 'tube_ctrl_values')

d.label(0x0520, 'tube_osbput')

d.label(0x0527, 'tube_poll_r1_wrch')

d.label(0x052D, 'tube_osbget')

d.label(0x0537, 'tube_osrdch')

d.label(0x053A, 'tube_rdch_reply')

d.label(0x0542, 'tube_osfind')

d.label(0x0552, 'tube_osfind_close')

d.label(0x055E, 'tube_osargs')

d.label(0x0562, 'tube_read_params')

d.label(0x0564, 'read_osargs_params')

d.label(0x0577, 'send_osargs_result')

d.label(0x0582, 'tube_read_string')

d.label(0x0586, 'strnh')

d.label(0x0593, 'string_buf_done')

d.label(0x0596, 'tube_oscli')

d.label(0x059C, 'tube_reply_ack')

d.label(0x059E, 'tube_reply_byte')

d.label(0x05A6, 'mj')

d.label(0x05A9, 'tube_osfile')

d.label(0x05AB, 'argsw')

d.label(0x05C7, 'send_osfile_ctrl_blk')

d.label(0x05D1, 'tube_osgbpb')

d.label(0x05D3, 'read_osgbpb_ctrl_blk')

d.label(0x05E6, 'send_osgbpb_result')

d.label(0x05F2, 'tube_osbyte_2param')

d.label(0x05FC, 'tube_poll_r2_result')

d.label(0x0604, 'bytex')

d.label(0x0607, 'tube_osbyte_long')

d.label(0x061D, 'tube_osbyte_send_y')

d.label(0x0625, 'tube_osbyte_short')

d.label(0x0627, 'tube_osword')

d.label(0x062B, 'tube_osword_read')

d.label(0x0630, 'tube_osbyte_send_x')

d.label(0x0636, 'tube_osword_read_lp')

d.label(0x0645, 'skip_param_read')

d.label(0x064C, 'poll_r2_osword_result')

d.label(0x0657, 'tube_osword_write')

d.label(0x065A, 'tube_osword_write_lp')

d.label(0x0665, 'tube_return_main')

d.label(0x0668, 'tube_osword_rdln')

d.label(0x066A, 'read_rdln_ctrl_block')

d.label(0x0680, 'tube_rdln_send_line')

d.label(0x0687, 'tube_rdln_send_loop')

d.label(0x068A, 'tube_rdln_send_byte')

d.label(0x0695, 'tube_send_r2')

d.label(0x069E, 'tube_send_r4')

d.label(0x06A7, 'tube_escape_check')

d.label(0x06AD, 'tube_event_handler')

d.label(0x06BC, 'tube_send_r1')

d.label(0x06C5, 'tube_read_r2')

d.label(0x06EC, 'svc_11_nmi_claim')

d.label(0x8004, 'service_handler_lo')

d.label(0x801A, 'copyright_string')

d.label(0x806C, 'dispatch_svc5')

d.label(0x8073, 'svc_5_unknown_irq')

d.label(0x8094, 'init_nmi_workspace')

d.label(0x8096, 'copy_nmi_shim')

d.label(0x80D6, 'accept_frame')

d.label(0x80E9, 'scout_reject')

d.label(0x80F1, 'accept_local_net')

d.label(0x80F4, 'accept_scout_net')

d.label(0x810A, 'scout_discard')

d.label(0x8112, 'scout_loop_rda')

d.label(0x8122, 'scout_loop_second')

d.label(0x815D, 'scout_no_match')

d.label(0x8160, 'scout_match_port')

d.label(0x816A, 'scan_port_list')

d.label(0x8173, 'scan_nfs_port_list')

d.label(0x8177, 'check_port_slot')

d.label(0x8179, 'scout_ctrl_check')

d.label(0x818B, 'check_station_filter')

d.label(0x8195, 'scout_port_match')

d.label(0x819F, 'next_port_slot')

d.label(0x81AC, 'discard_no_match')

d.label(0x81AF, 'try_nfs_port_list')

d.label(0x81BA, 'port_match_found')

d.label(0x81CC, 'send_data_rx_ack')

d.label(0x81DD, 'data_rx_setup')

d.label(0x81FB, 'nmi_data_rx_net')

d.label(0x8211, 'nmi_data_rx_skip')

d.label(0x821C, 'install_data_rx_handler')

d.label(0x822F, 'install_tube_rx')

d.label(0x8236, 'nmi_error_dispatch')

d.label(0x823E, 'rx_error_reset')

d.label(0x8249, 'data_rx_loop')

d.label(0x8259, 'read_sr2_between_pairs')

d.label(0x8260, 'read_second_rx_byte')

d.label(0x8270, 'check_sr2_loop_again')

d.label(0x828F, 'read_last_rx_byte')

d.label(0x829E, 'send_ack')

d.label(0x82A1, 'nmi_data_rx_tube')

d.label(0x82A4, 'rx_tube_data')

d.label(0x82C1, 'data_rx_tube_error')

d.label(0x82C4, 'data_rx_tube_complete')

d.label(0x82FA, 'ack_tx_configure')

d.label(0x8308, 'ack_tx_write_dest')

d.label(0x8349, 'start_data_tx')

d.label(0x834C, 'dispatch_nmi_error')

d.label(0x834F, 'advance_rx_buffer_ptr')

d.label(0x835A, 'add_rxcb_ptr')

d.label(0x8388, 'inc_rxcb_ptr')

d.label(0x8393, 'skip_tube_update')

d.label(0x8395, 'return_rx_complete')

d.label(0x83A5, 'rx_complete_update_rxcb')

d.label(0x83AA, 'add_buf_to_base')

d.label(0x83B1, 'inc_rxcb_buf_hi')

d.label(0x83B3, 'store_buf_ptr_lo')

d.label(0x83B5, 'store_rxcb_buf_ptr')

d.label(0x83BA, 'store_rxcb_buf_hi')

d.label(0x83BC, 'skip_buf_ptr_update')

d.label(0x8410, 'copy_scout_to_buffer')

d.label(0x8416, 'copy_scout_select')

d.label(0x841D, 'copy_scout_bytes')

d.label(0x842B, 'next_scout_byte')

d.label(0x8432, 'scout_copy_done')

d.label(0x8437, 'copy_scout_via_tube')

d.label(0x8449, 'release_tube')

d.label(0x8452, 'clear_release_flag')

d.label(0x846C, 'rotate_prot_mask')

d.label(0x8472, 'dispatch_imm_op')

d.label(0x847D, 'scout_page_overflow')

d.label(0x847F, 'check_scout_done')

d.label(0x8485, 'imm_op_out_of_range')

d.label(0x84A2, 'copy_addr_loop')

d.label(0x84AE, 'svc5_dispatch_lo')

d.label(0x84DD, 'set_tx_reply_flag')

d.label(0x84E5, 'rx_imm_halt_cont')

d.label(0x84EA, 'tx_cr2_setup')

d.label(0x84EF, 'tx_nmi_setup')

d.label(0x84F6, 'imm_op_build_reply')

d.label(0x852C, 'imm_op_discard')

d.label(0x8576, 'halt_spin_loop')

d.label(0x8585, 'tx_done_exit')

d.label(0x858C, 'tx_begin')

d.label(0x85A4, 'tx_imm_op_setup')

d.label(0x85B8, 'calc_peek_poke_size')

d.label(0x85CF, 'tx_ctrl_range_check')

d.label(0x85D3, 'check_imm_range')

d.label(0x85D9, 'copy_imm_params')

d.label(0x85E3, 'tx_line_idle_check')

d.label(0x85FD, 'test_inactive_retry')

d.label(0x85FF, 'intoff_test_inactive')

d.label(0x8605, 'test_line_idle')

d.label(0x8619, 'inactive_retry')

d.label(0x862F, 'tx_bad_ctrl_error')

d.label(0x863F, 'tx_no_clock_error')

d.label(0x8641, 'store_tx_error')

d.label(0x869A, 'add_bytes_loop')

d.label(0x8681, 'tx_ctrl_dispatch_lo')

d.label(0x8689, 'tx_ctrl_machine_type')

d.label(0x86AC, 'setup_data_xfer')

d.label(0x86C2, 'copy_bcast_addr')

d.label(0x86CE, 'setup_unicast_xfer')

d.label(0x86D3, 'proc_op_status2')

d.label(0x86D5, 'store_status_copy_ptr')

d.label(0x86D8, 'skip_buf_setup')

d.label(0x86E3, 'tx_ctrl_exit')

d.label(0x86F0, 'tx_fifo_write')

d.label(0x8710, 'tx_error')

d.label(0x8714, 'tx_fifo_not_ready')

d.label(0x871B, 'tx_store_error')

d.label(0x871E, 'delay_nmi_disable')

d.label(0x873F, 'check_handshake_bit')

d.label(0x8749, 'install_reply_scout')

d.label(0x8776, 'reject_reply')

d.label(0x87D1, 'data_tx_begin')

d.label(0x87DF, 'install_imm_data_nmi')

d.label(0x87F5, 'data_tx_check_fifo')

d.label(0x8805, 'write_second_tx_byte')

d.label(0x8815, 'check_irq_loop')

d.label(0x881D, 'data_tx_last')

d.label(0x882E, 'install_saved_handler')

d.label(0x8837, 'nmi_data_tx_tube')

d.label(0x883A, 'tube_tx_fifo_write')

d.label(0x8852, 'write_second_tube_byte')

d.label(0x885C, 'tube_tx_inc_byte2')

d.label(0x8860, 'tube_tx_inc_byte3')

d.label(0x8861, 'tube_tx_inc_operand')

d.label(0x8864, 'tube_tx_inc_byte4')

d.label(0x8868, 'check_tube_irq_loop')

d.label(0x8869, 'tube_tx_sr1_operand')

d.label(0x8870, 'tx_tdra_error')

d.label(0x8898, 'nmi_final_ack_net')

d.label(0x88C9, 'check_fv_final_ack')

d.label(0x88D4, 'tx_result_fail')

d.label(0x8912, 'calc_transfer_size')

d.label(0x8942, 'restore_x_and_return')

d.label(0x8945, 'fallback_calc_transfer')

d.label(0x8968, 'nmi_shim_rom_src')

d.label(0x8983, 'wait_idle_and_reset')

d.label(0x8988, 'poll_nmi_idle')

d.label(0x89A4, 'reset_enter_listen')

d.label(0x89A6, 'listen_jmp_hi')
d.entry(0x0032)
d.entry(0x0036)
d.entry(0x0607)
d.entry(0x0625)
d.entry(0x0627)
d.entry(0x0668)
d.entry(0x06A7)
d.entry(0x06AD)
d.entry(0x06BC)
d.entry(0x06EF)
d.entry(0x8073)
d.entry(0x80BE)
d.entry(0x80DB)
d.entry(0x810D)
d.entry(0x81DD)
d.entry(0x81E7)
d.entry(0x81FB)
d.entry(0x8211)
d.entry(0x8244)
d.entry(0x82A1)
d.entry(0x8326)
d.entry(0x8370)
d.entry(0x8396)
d.entry(0x84F6)
d.entry(0x85F4)
d.entry(0x86EA)
d.entry(0x8710)
d.entry(0x8726)
d.entry(0x8732)
d.entry(0x874E)
d.entry(0x8762)
d.entry(0x8779)
d.entry(0x87C1)
d.entry(0x87E6)
d.entry(0x8837)
d.entry(0x8878)
d.entry(0x8884)
d.entry(0x8898)
d.entry(0x88AC)
d.entry(0x88D0)
d.entry(0x88D6)
d.entry(0x8945)
d.entry(0x89A7)
d.entry(0x89B5)


d.subroutine(0x0406, 'tube_addr_data_dispatch', title='Tube address/data dispatch', description="""Called by 10 sites across the Tube host and Econet
code. Routes requests based on the value of A:
  A < &80: R4 transfer setup at &0435 -- A is the
    transfer type (0-7), used both as the first
    R4 byte and as the index into tube_ctrl_values.
    Types: 0/1 = 1-byte R3 P-to-H/H-to-P,
    2/3 = 2-byte R3 P-to-H/H-to-P,
    4 = execute at address, 5 = release claim,
    6 = event handler, 7 = SENDW transfer+release.
  &80 <= A < &C0: release -- maps A via ORA #&40
    and compares with tube_claimed_id; if we own
    this address, falls through to tube_release_claim
  A >= &C0: external address claim from another host
Falls through to tube_release_claim when releasing our
current claim.""", on_entry={'a': 'request type (<&80 data, &80-&BF release, &C0+ claim)', 'x': 'transfer address low (data transfer only)', 'y': 'transfer address high (data transfer only)'})


d.subroutine(0x0414, 'tube_release_claim', title='Release Tube address claim via R4 command 5', description="""Saves interrupt state (PHP/SEI) to protect the R4
protocol sequence, sends R4 command 5 (release) followed
by the currently-claimed address from tube_claimed_id
(&15), then restores interrupts (PLP). Falls through to
clear_tube_claim to reset the claimed-address state to
the &80 sentinel.""")


d.subroutine(0x0421, 'clear_tube_claim', title='Reset Tube address claim state', description="""Stores &80 into both tube_claimed_id (&15) and
tube_claim_flag (&14). The &80 sentinel indicates no
address is currently claimed and no claim is in
progress. Called after tube_release_claim (via
fall-through) and during initial workspace setup.""")


d.subroutine(0x0435, 'tube_transfer_setup', title='Set up R4 transfer protocol (7-byte sequence)', description="""Initiates a Tube R4 transfer by sending a 7-byte
protocol sequence to R4, each write BVC-polled for
H-to-P space. PHP/SEI at entry and PLP at return
protect the sequence from IRQs.

R4 byte sequence:
  1. Transfer type byte (A on entry, 0-7)
  2. tube_claimed_id (Econet host ownership byte,
     an Econet-specific addition to the standard
     Acorn Tube R4 protocol)
  3-6. 4-byte transfer address, big-endian
     (from (tube_data_ptr),Y=3..0)
  7. Trigger byte (post-LSR remnant of
     tube_ctrl_values[type]); parasite resumes
     after reading this

Between writes 6 and 7, if bit 2 of the ULA ctrl
byte is set (types 0 and 2, both parasite-to-host),
performs two dummy BIT reads of R3 to drain the
2-byte R3 FIFO.

After the final write, polls R4 for the parasite
ack (BVC/BCS at poll_r4_copro_ack). Dispatches on
X (= transfer type):
  X=4: tube_sendw_complete (release, sync via R2,
       reset stack)
  Other: if bit 0 of ctrl byte is set, write &88
         to &FEE0 to release Tube NMI; PLP; RTS""")


d.subroutine(0x0484, 'tube_begin', title='Tube host startup entry (BEGIN)', description="""Entry point via JMP from &0400. Enables interrupts, checks
break type via OSBYTE &FD: soft break re-initialises Tube and
restarts, hard break claims address &FF. Sends ROM contents
to co-processor page by page via SENDW, then claims the final
transfer address.""")


d.subroutine(0x04C7, 'tube_claim_default', title='Claim default Tube transfer address', description="""Sets Y=0, X=&53 (address &0053), then JMP tube_addr_claim
to initiate a Tube address claim for the default transfer
address. Called from the BEGIN startup path and after the
page transfer loop completes.""")


d.subroutine(0x04CE, 'tube_init_reloc', title='Initialise relocation address for ROM transfer', description="""Sets the Tube transfer source page to &8000
(tube_xfer_page = &80) and the page counter to &80.
Checks ROM type bit 5 for a relocation address in the
ROM header. If set, scans past the null-terminated
copyright string and extracts the 4-byte relocation
address into tube_transfer_addr (&53), tube_xfer_page
(&54), tube_xfer_addr_2 (&55), and tube_xfer_addr_3
(&56). If clear, uses the default &8000 start address.
Called twice during tube_begin: once for initial setup
and once after each page transfer completes.""")


d.subroutine(0x0582, 'tube_read_string', title='Read string from Tube R2 into buffer', description="""Loops reading bytes from tube_read_r2 into the
string buffer at &0700, storing at string_buf+Y.
Terminates on CR (&0D) or when Y wraps to zero
(256-byte overflow). Returns with X=0, Y=7 so that
XY = &0700, ready for OSCLI or OSFIND dispatch.
Called by the Tube OSCLI and OSFIND handlers.""", on_exit={'x': '0 (low byte of &0700)', 'y': '7 (high byte of &0700)'})


d.subroutine(0x0695, 'tube_send_r2', title='Send byte to Tube data register R2', description="""Polls Tube status register 2 until bit 6 (TDRA)
is set, then writes A to the data register. Uses a
tight BIT/BVC polling loop. Called by 12 sites
across the Tube host code for all R2 data
transmission: command responses, file data, OSBYTE
results, and control block bytes.""", on_entry={'a': 'byte to send'}, on_exit={'a': 'preserved (value written)'})


d.subroutine(0x069E, 'tube_send_r4', title='Send byte to Tube data register R4', description="""Polls Tube status register 4 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R4 is the command/control
channel used for address claims (ADRR), data transfer
setup (SENDW), and release commands. Called by 7
sites, primarily during tube_release_claim and
tube_transfer_setup sequences.""", on_entry={'a': 'byte to send'}, on_exit={'a': 'preserved (value written)'})


d.subroutine(0x06BC, 'tube_send_r1', title='Send byte to Tube data register R1', description="""Polls Tube status register 1 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R1 is used for asynchronous
event and escape notification to the co-processor.
Called by tube_event_handler to forward event type,
Y, and X parameters, and reached via BMI from
tube_escape_check when the escape flag is set.""", on_entry={'a': 'byte to send'}, on_exit={'a': 'preserved (value written)'})


d.subroutine(0x06C5, 'tube_read_r2', title='Read a byte from Tube data register R2', description="""Polls Tube status register 2 until bit 7 (RDA)
is set, then loads and returns the byte from Tube
data register 2. Uses a BIT/BPL polling loop (testing
the N flag). R2 is the primary data channel from the
co-processor. Called by 14 sites across the Tube host
code for command dispatch, OSFILE/OSGBPB control block
reads, string reads, and OSBYTE parameter reception.""", on_exit={'a': 'byte read from R2'})


d.subroutine(0x805D, 'set_jsr_protection', title='Set JSR protection and dispatch via table', description="""Validates the TX operation type in Y against the
dispatch table range, saves the current JSR protection
mask, sets protection bits 2-4, then dispatches through
the PHA/RTS trampoline using the table at
set_rx_buf_len_hi. If Y >= &86, skips the protection
setup and dispatches directly.""", on_entry={'y': 'TX operation type (dispatch index)'})
d.comment(0x8000, """ANFS ROM 4.08.53 disassembly (Acorn Advanced Network Filing System)
===================================================================""")


d.subroutine(0x0520, 'tube_osbput', title='Tube OSBPUT handler (R2 cmd 8)', description="""Reads file handle and data byte from R2, then
calls OSBPUT (&FFD4) to write the byte. Falls through
to tube_reply_ack to send &7F acknowledgement.""")


d.subroutine(0x052D, 'tube_osbget', title='Tube OSBGET handler (R2 cmd 7)', description="""Reads file handle from R2, calls OSBGET (&FFD7)
to read a byte, then falls through to tube_rdch_reply
which encodes the carry flag (error) into bit 7 and
sends the result byte via R2.""")


d.subroutine(0x0537, 'tube_osrdch', title='Tube OSRDCH handler (R2 cmd 0)', description="""Calls OSRDCH (&FFE0) to read a character from
the current input stream, then falls through to
tube_rdch_reply which encodes the carry flag (error)
into bit 7 and sends the result byte via R2.""")


d.subroutine(0x0542, 'tube_osfind', title='Tube OSFIND handler (R2 cmd 9)', description="""Reads open mode from R2. If zero, reads a file
handle and closes that file. Otherwise saves the mode,
reads a filename string into &0700 via tube_read_string,
then calls OSFIND (&FFCE) to open the file. Sends the
resulting file handle (or &00) via tube_reply_byte.""")


d.subroutine(0x055E, 'tube_osargs', title='Tube OSARGS handler (R2 cmd 6)', description="""Reads file handle from R2 into Y, then reads
a 4-byte argument and reason code into zero page.
Calls OSARGS (&FFDA), sends the result A and 4-byte
return value via R2, then returns to the main loop.""")


d.subroutine(0x0596, 'tube_oscli', title='Tube OSCLI handler (R2 cmd 1)', description="""Reads a command string from R2 into &0700 via
tube_read_string, then calls OSCLI (&FFF7) to execute
it. Falls through to tube_reply_ack to send &7F
acknowledgement.""")


d.subroutine(0x05A9, 'tube_osfile', title='Tube OSFILE handler (R2 cmd 10)', description="""Reads a 16-byte control block into zero page,
a filename string into &0700 via tube_read_string,
and a reason code from R2. Calls OSFILE (&FFDD),
then sends the result A and updated 16-byte control
block back via R2. Returns to the main loop via mj.""")


d.subroutine(0x05D1, 'tube_osgbpb', title='Tube OSGBPB handler (R2 cmd 11)', description="""Reads a 13-byte control block and reason code
from R2 into zero page. Calls OSGBPB (&FFD1), then
sends 12 result bytes and the carry+result byte
(via tube_rdch_reply) back via R2.""")


d.subroutine(0x05F2, 'tube_osbyte_2param', title='Tube OSBYTE 2-param handler (R2 cmd 2)', description="""Reads X and A from R2, calls OSBYTE (&FFF4)
with Y=0, then sends the result X via
tube_reply_byte. Used for OSBYTE calls that take
only A and X parameters.""")


d.subroutine(0x0607, 'tube_osbyte_long', title='Tube OSBYTE 3-param handler (R2 cmd 3)', description="""Reads X, Y, and A from R2, calls OSBYTE
(&FFF4), then sends carry+Y and X as result bytes
via R2. Used for OSBYTE calls needing all three
parameters and returning both X and Y results.""")


d.subroutine(0x0627, 'tube_osword', title='Tube OSWORD handler (R2 cmd 4)', description="""Reads OSWORD number A and in-length from R2,
then reads the parameter block into &0128. Calls
OSWORD (&FFF1), then sends the out-length result
bytes from the parameter block back via R2.
Returns to the main loop via tube_return_main.""")


d.subroutine(0x0668, 'tube_osword_rdln', title='Tube OSWORD 0 handler (R2 cmd 5)', description="""Handles OSWORD 0 (read line) specially. Reads
4 parameter bytes from R2 into &0128 (max length,
min char, max char, flags). Calls OSWORD 0 (&FFF1)
to read a line, then sends &7F+CR or the input line
byte-by-byte via R2, followed by &80 (error/escape)
or &7F (success).""")


d.subroutine(0x8074, 'adlc_init', title='ADLC initialisation', description="""Initialise ADLC hardware and Econet workspace.
Reads station ID via &FE18 (INTOFF side effect),
performs a full ADLC reset (adlc_full_reset), then
checks for Tube co-processor via OSBYTE &EA and
stores the result in l0d63. Issues NMI claim service
request (OSBYTE &8F, X=&0C). Falls through to
init_nmi_workspace to copy the NMI shim to RAM.""")


d.subroutine(0x8094, 'init_nmi_workspace', title='Initialise NMI workspace (skip service request)', description="""Copies 32 bytes of NMI shim code from ROM
(listen_jmp_hi) to &0D00, then patches the current
ROM bank number into the self-modifying code at
&0D07. The shim includes the INTOFF/INTON pair
(BIT &FE18 at entry, BIT &FE20 before RTI) that
toggles the IC97 NMI enable flip-flop to guarantee
edge re-triggering on /NMI. Clears tx_src_net,
need_release_tube, and tx_op_type to zero. Reads
station ID into tx_src_stn (&0D22). Sets
tx_complete_flag and econet_init_flag to &80.
Finally re-enables NMIs via INTON (&FE20 read).""")


d.subroutine(0x80BE, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")


d.subroutine(0x80DB, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &8102.""")


d.subroutine(0x80FD, 'scout_error', title='Scout error/discard handler', description="""Handles scout reception errors and end-of-frame
conditions. Reads SR2 and tests AP|RDA (bits 0|7):
if neither set, the frame ended cleanly and is
simply discarded. If unexpected data is present,
performs a full ADLC reset. Also serves as the
common discard path for address/network mismatches
from nmi_rx_scout and scout_complete -- reached by
5 branch sites across the scout reception chain.""")


d.subroutine(0x8137, 'scout_complete', title='Scout completion handler', description="""Processes a completed scout frame. Writes CR1=&00
and CR2=&84 to disable PSE and suppress FV, then
tests SR2 for FV (frame valid). If FV is set with
RDA, reads the remaining scout data bytes in pairs
into the buffer at &0D3D. Matches the port byte
(&0D40) against open receive control blocks to find
a listener. On match, calculates the transfer size
via tx_calc_transfer, sets up the data RX handler
chain, and sends a scout ACK. On no match or error,
discards the frame via scout_error.""")


d.subroutine(0x81E7, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &81E7 (AP+addr check) -> &81FB (net=0 check) ->
&8211 (skip ctrl+port) -> &8239 (bulk data read) -> &8278 (completion)""")


d.subroutine(0x821C, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects between the normal bulk RX handler (&8239)
and the Tube RX handler based on bit 1 of rx_src_net
(tx_flags). If normal mode, loads the handler address
&8239 and checks SR1 bit 7: if IRQ is already asserted
(more data waiting), jumps directly to nmi_data_rx_bulk
to avoid NMI re-entry overhead. Otherwise installs the
handler via set_nmi_vector and returns via RTI.""")


d.subroutine(0x8236, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")


d.subroutine(0x8244, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &8278.
SR2 = 0 -> RTI, wait for next NMI to continue.""")


d.subroutine(0x8278, 'data_rx_complete', title='Data frame completion', description="""Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&8137): disables PSE (CR2=&84,
CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &82E4.""")


d.subroutine(0x82EF, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&88C6).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")


d.subroutine(0x8326, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Continuation of ACK frame transmission. Reads our
station ID from &FE18 (INTOFF side effect), tests
TDRA via SR1, and writes station + network=0 to the
TX FIFO, completing the 4-byte ACK address header.
Then checks rx_src_net bit 7: if set, branches to
start_data_tx to begin the data phase. Otherwise
writes CR2=&3F (TX_LAST_DATA) and falls through to
post_ack_scout for scout processing.""")


d.subroutine(0x833D, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")


d.subroutine(0x834F, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")


d.subroutine(0x8396, 'nmi_post_ack_dispatch', title='Post-ACK frame-complete NMI handler', description="""Installed by ack_tx_configure via saved_nmi_lo/hi.
Fires as an NMI after the ACK frame (CRC and
closing flag) has been fully transmitted by the
ADLC. Dispatches on scout_port: port != 0 goes
to rx_complete_update_rxcb to finalise the data
transfer and mark the RXCB complete; port = 0
with ctrl &82 (POKE) also goes to
rx_complete_update_rxcb; other port-0 ops go to
imm_op_build_reply.""")


d.subroutine(0x83A5, 'rx_complete_update_rxcb', title='Complete RX and update RXCB', description="""Called from nmi_post_ack_dispatch after the
final ACK has been transmitted. Finalises the
received data transfer: calls advance_rx_buffer_ptr
to update the 4-byte buffer pointer with the
transfer count (and handle Tube re-claim if
needed). Stores the source station, network, and
port into the RXCB, then ORs &80 into the control
byte (bit 7 = complete). This is the NMI-to-
foreground synchronisation point: wait_net_tx_ack
polls this bit to detect that the reply has
arrived. Falls through to discard_reset_rx to
reset the ADLC to idle RX listen mode.""")


d.subroutine(0x8402, 'discard_reset_listen', title='Discard with Tube release', description="""Checks whether a Tube transfer is active by
ANDing bit 1 of l0d63 with rx_src_net (tx_flags).
If a Tube claim is held, calls release_tube to
free it before returning. Used as the clean-up
path after RXCB completion and after ADLC reset
to ensure no stale Tube claims persist.""")

d.label(0x8407, 'imm_op_jump_table')


d.subroutine(0x8410, 'copy_scout_to_buffer', title='Copy scout data to port buffer', description="""Copies scout data bytes (offsets 4-11) from the
RX scout buffer at &0D3D into the open port buffer.
Checks bit 1 of rx_src_net (tx_flags) to select the
write path: direct memory store via (open_port_buf),Y
for normal transfers, or Tube data register 3 write
for Tube transfers. Calls advance_buffer_ptr after
each byte. Falls through to release_tube on
completion. Handles page overflow (Y wrap) by
branching to scout_page_overflow.""")


d.subroutine(0x8449, 'release_tube', title='Release Tube co-processor claim', description="""Tests need_release_tube (&98) bit 7: if set, the
Tube has already been released and the subroutine
just clears the flag. If clear (Tube claim held),
calls tube_addr_data_dispatch with A=&82 to release
the claim, then clears the release flag via LSR
(which shifts bit 7 to 0). Called after completed
RX transfers and during discard paths to ensure no
stale Tube claims persist.""")


d.subroutine(0x8455, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Checks the control byte at l0d30 for immediate
operation codes (&81-&88). Codes below &81 or above
&88 are out of range and discarded. Codes &87-&88
(HALT/CONTINUE) bypass the protection mask check.
For &81-&86, converts to a 0-based index and tests
against the immediate operation mask at &0D61 to
determine if this station accepts the operation.
If accepted, dispatches via the immediate operation
table. Builds the reply by storing data length,
station/network, and control byte into the RX buffer.""")

d.label(0x8488, 'imm_op_dispatch_lo')
for addr in range(0x8488, 0x8490):
    d.byte(addr)
d.expr(0x8488, '<(rx_imm_peek-1)')
d.expr(0x8489, '<(rx_imm_poke-1)')
d.expr(0x848A, '<(rx_imm_exec-1)')
d.expr(0x848B, '<(rx_imm_exec-1)')
d.expr(0x848C, '<(rx_imm_exec-1)')
d.expr(0x848D, '<(rx_imm_halt_cont-1)')
d.expr(0x848E, '<(rx_imm_halt_cont-1)')
d.expr(0x848F, '<(rx_imm_machine_type-1)')


d.subroutine(0x8490, 'rx_imm_exec', title='RX immediate: JSR/UserProc/OSProc setup', description="""Sets up the port buffer to receive remote procedure
data. Copies the 2-byte remote address from &0D32
into the execution address workspace at &0D66, then
jumps to the common receive path at c81c1. Used for
operation types &83 (JSR), &84 (UserProc), and
&85 (OSProc).""")


d.subroutine(0x84AE, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data.
port_ws_offset=&2E, rx_buf_offset=&0D, then jumps to
the common data-receive path at c81af.""")


d.subroutine(0x84B9, 'rx_imm_machine_type', title='RX immediate: machine type query', description="""Sets up a buffer at &88C1 (length #&01FC) for the
machine type query response. Falls through to
set_rx_buf_len_hi to configure buffer dimensions,
then branches to set_tx_reply_flag.""")


d.subroutine(0x84CB, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Writes &0D2E to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send
the PEEK response data back to the requesting station.""")


d.subroutine(0x852F, 'advance_buffer_ptr', title='Increment 4-byte receive buffer pointer', description="""Adds one to the counter at &A2-&A5 (port_buf_len
low/high, open_port_buf low/high), cascading
overflow through all four bytes. Called after each
byte is stored during scout data copy and data
frame reception to track the current write position
in the receive buffer.""")


d.subroutine(0x84F6, 'imm_op_build_reply', title='Build immediate operation reply header', description="""Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")


d.subroutine(0x8543, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes (tx_done_exit - 1) on the stack so RTS returns
to tx_done_exit, then does JMP (l0d66) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")


d.subroutine(0x854C, 'tx_done_econet_event', title='TX done: fire Econet event', description="""Handler for TX operation type &84. Loads the
remote address from l0d66/l0d67 into X/A and
sets Y=8 (Econet event number), then falls
through to tx_done_fire_event to call OSEVEN.""")


d.subroutine(0x855A, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM service entry point with X=l0d66,
Y=l0d67. This invokes an OS-level procedure on
behalf of the remote station, then exits via
tx_done_exit.""")


d.subroutine(0x8566, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of rx_flags (&0D61), enables interrupts,
and spin-waits until bit 2 is cleared (by a CONTINUE
from the remote station). If bit 2 is already set,
skips to exit.""")


d.subroutine(0x857D, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of rx_flags (&0D61), releasing any
station that is halted and spinning in tx_done_halt.""")


d.subroutine(0x858C, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")


d.subroutine(0x85F4, 'inactive_poll', title='INACTIVE polling loop', description="""Entry point for the Econet line idle detection
loop. Saves the TX index in rx_remote_addr, pushes
two timeout counter bytes onto the stack, and loads
Y=&E7 (CR2 value for TX preparation). Loads the
INACTIVE bit mask (&04) into A and falls through to
intoff_test_inactive to begin polling SR2 with
interrupts disabled.""")


d.subroutine(0x85FF, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Disables NMIs via two reads of &FE18 (INTOFF),
then polls SR2 for the INACTIVE bit (bit 2). If
INACTIVE is detected, reads SR1 and writes CR2=&67
to clear status, then tests CTS (SR1 bit 4): if
CTS is present, branches to tx_prepare to begin
transmission. If INACTIVE is not set, re-enables
NMIs via &FE20 (INTON) and decrements the 3-byte
timeout counter on the stack. On timeout, falls
through to tx_line_jammed.""")


d.subroutine(0x8633, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Reached when the INACTIVE polling loop times
out without detecting a quiet line. Writes
CR2=&07 (FC_TDRA|2_1_BYTE|PSE) to abort the TX
attempt, pulls the 3-byte timeout state from the
stack, and stores error code &40 ('Line Jammed')
in the TX control block via store_tx_error.""")


d.subroutine(0x864D, 'tx_prepare', title='TX preparation', description="""Configures the ADLC for frame transmission.
Writes CR2=Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|
2_1_BYTE|PSE) and CR1=&44 (RX_RESET|TIE) to enable
TX with interrupts. Installs the nmi_tx_data handler
at &86E0. Sets need_release_tube flag via SEC/ROR.
Writes the 4-byte destination address (dst_stn,
dst_net, src_stn, src_net=0) to the TX FIFO. For
Tube transfers, claims the Tube address; for direct
transfers, sets up the buffer pointer from the TXCB.""")


d.subroutine(0x8689, 'tx_ctrl_machine_type', title='TX ctrl: machine type query setup', description="""Handler for control byte &88. Sets scout_status=3
and branches to store_status_copy_ptr, skipping
the 4-byte address addition (no address parameters
needed for a machine type query).""")


d.subroutine(0x868D, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets A=3 (scout_status for PEEK) and branches
to tx_ctrl_store_and_add to store the status and
perform the 4-byte transfer address addition.""")


d.subroutine(0x8691, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets A=2 (scout_status for POKE) and falls
through to tx_ctrl_store_and_add to store the
status and perform the 4-byte transfer address
addition.""")


d.subroutine(0x8693, 'tx_ctrl_store_and_add', title='TX ctrl: store status and add transfer address', description="""Shared path for PEEK (A=3) and POKE (A=2).
Stores A as the scout status byte at rx_port
(&0D40), then performs a 4-byte addition with
carry propagation, adding bytes from the TXCB
(nmi_tx_block+&0C to +&0F) into the transfer
address workspace at &0D1E-&0D21. Falls through
to tx_ctrl_proc which checks the loop boundary,
then continues to tx_calc_transfer and
tx_ctrl_exit.""", on_entry={'a': 'scout status (3=PEEK, 2=POKE)'})


d.subroutine(0x86A5, 'tx_ctrl_proc', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer
directly (no 4-byte address addition needed for
procedure calls). Shared by operation types &83-&85.""")


d.subroutine(0x86EA, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")


d.subroutine(0x8726, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &8728 (nmi_tx_complete).
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)
Exits via JMP set_nmi_vector which installs nmi_tx_complete,
then falls through to nmi_rti. The INTON (BIT &FE20) in
nmi_rti creates the /NMI edge for the frame-complete interrupt
-- essential because the ADLC IRQ may transition atomically
from TDRA to frame-complete without de-asserting.""")


d.subroutine(0x8732, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC
and closing flag) has been fully transmitted.
Writes CR1=&82 (TX_RESET|RIE) to clear RX_RESET
and enable RX interrupts -- the TX-to-RX pivot in
the four-way handshake. The scout ACK can only be
received after this point. Full CR1 sequence through
a handshake: &44 (scout TX) -> &82 (await scout ACK)
-> &44 (data TX) -> &82 (await data ACK).
Dispatches on rx_src_net flags: bit6=broadcast
(tx_result_ok), bit0=handshake data pending
(handshake_await_ack), both clear=install
nmi_reply_scout for scout ACK reception.""")


d.subroutine(0x874E, 'nmi_reply_scout', title='RX reply scout handler', description="""Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")


d.subroutine(0x8762, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs nmi_reply_validate
(&8779) for the remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &8767.
If IRQ is still set, falls through directly to &8779 without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")


d.subroutine(0x8779, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &8779 -- must see data available
  2. Read source station at &877E, compare to &0D20 (tx_dst_stn)
  3. Read source network at &877C, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &8786 -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")


d.subroutine(0x87C1, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Continuation of the TX-side scout ACK. Reads our
station ID from &FE18 (INTOFF), tests TDRA via SR1,
and writes station + network=0 to the TX FIFO. Then
checks bit 1 of rx_src_net to select between the
immediate-op data NMI handler and the normal
nmi_data_tx handler at &87EE. Installs the chosen
handler via set_nmi_vector. Shares the tx_check_tdra
entry at &87C7 with ack_tx.""")


d.subroutine(0x87E6, 'nmi_data_tx', title='TX data phase: send payload', description="""Transmits the data payload of a four-way
handshake. Loads bytes from (open_port_buf),Y or
from Tube R3 depending on the transfer mode, writing
pairs to the TX FIFO. After each pair, decrements
the byte count (port_buf_len). If the count reaches
zero, branches to tx_last_data to signal end of
frame. Otherwise tests SR1 bit 7 (IRQ): if still
asserted, writes another pair without returning from
NMI (tight loop optimisation). If IRQ clears, returns
via RTI.""")


d.subroutine(0x8878, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""Called via JMP from nmi_tx_complete when bit 0 of
&0D4A is set (four-way handshake in progress). Writes
CR1=&82 (TX_RESET|RIE) to switch the ADLC from TX
mode to RX mode, listening for the final ACK from the
remote station. Installs the nmi_final_ack handler at
&887A via set_nmi_vector.""")


d.subroutine(0x8884, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&874E-&8779):
  &887A: Check AP, read dest_stn, compare to our station
  &888E: Check RDA, read dest_net, validate = 0
  &88A2: Check RDA, read src_stn/net, compare to TX dest
  &88C1: Check FV for frame completion
On success, stores result=0 at tx_result_ok. On failure, error &41.""")


d.subroutine(0x88AC, 'nmi_final_ack_validate', title='Final ACK validation', description="""Continuation of nmi_final_ack. Tests SR2 for RDA,
then reads the source station and source network
bytes from the RX FIFO, comparing each against the
original TX destination at tx_dst_stn (&0D20) and
tx_dst_net (&0D21). Finally tests SR2 bit 1 (FV)
for frame completion. Any mismatch or missing FV
branches to tx_result_fail. On success, falls
through to tx_result_ok.""")


d.subroutine(0x88D0, 'tx_result_ok', title='TX completion handler', description="""Loads A=0 (success) and branches unconditionally to
tx_store_result (BEQ is always taken since A=0). This
two-instruction entry point exists so that JMP sites
can target the success path without needing to set A.
Called from ack_tx (&82EC) for final-ACK completion
and from nmi_tx_complete (&8732) for immediate-op
completion where no ACK is expected.""")


d.subroutine(0x88D4, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")


d.subroutine(0x88D6, 'tx_store_result', title='TX result store and completion', description="""Stores the TX result code (in A) at offset 0 of
the TX control block via (nmi_tx_block),Y=0. Sets
ws_0d60 to &80 to signal TX completion to the
foreground polling loop. Then jumps to
discard_reset_rx for a full ADLC reset and return
to idle RX listen mode.""", on_entry={'a': 'result code (0=success, &40=jammed, &41=not listening)'})


d.subroutine(0x88F2, 'tx_calc_transfer', title='Calculate transfer size', description="""Computes the data transfer byte count from the
RXCB buffer pointers. Reads the 4-byte buffer end
address from (port_ws_offset) and checks for Tube
addresses (&FExx/&FFxx). For Tube transfers, claims
the Tube address and sets the transfer flag in
rx_src_net. Subtracts the buffer start from the
buffer end to compute the byte count, storing it in
port_buf_len/port_buf_len_hi. Also copies the buffer
start address to open_port_buf for the RX/TX handlers
to use as their working pointer.""")


d.subroutine(0x8969, 'adlc_full_reset', title='ADLC full reset', description="""Performs a full ADLC hardware reset. Writes
CR1=&C1 (TX_RESET|RX_RESET|AC) to put both TX and
RX sections in reset with address control enabled.
Then configures CR4=&1E (8-bit RX word, abort extend,
NRZ encoding) and CR3=&00 (no loopback, no AEX, NRZ,
no DTR). Falls through to adlc_rx_listen to re-enter
RX listen mode.""")


d.subroutine(0x8978, 'adlc_rx_listen', title='Enter RX listen mode', description="""Configures the ADLC for passive RX listen mode.
Writes CR1=&82 (TX_RESET|RIE): TX section held in
reset, RX interrupts enabled. Writes CR2=&67
(CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE) to clear
all pending status and enable prioritised status.
This is the idle state where the ADLC listens for
incoming scout frames via NMI.""")


d.subroutine(0x8983, 'wait_idle_and_reset', title='Wait for idle NMI state and reset Econet', description="""Service 12 handler: NMI release. Checks ws_0d62
to see if Econet has been initialised; if not, skips
straight to adlc_rx_listen. Otherwise spins in a
tight loop comparing the NMI handler vector at
&0D0C/&0D0D against the address of nmi_rx_scout
(&80BE). When the NMI handler returns to idle, falls
through to save_econet_state to clear the initialised
flags and re-enter RX listen mode.""")


d.subroutine(0x8996, 'save_econet_state', title='Reset Econet flags and enter RX listen', description="""Disables NMIs via two reads of &FE18 (INTOFF),
then clears ws_0d60 (TX complete) and ws_0d62
(Econet initialised) by storing the current A value.
Sets Y=5 (service call workspace page) and jumps to
adlc_rx_listen to configure the ADLC for passive
listening. Used during NMI release (service 12) to
safely tear down the Econet state before another
ROM can claim the NMI workspace.""")


d.subroutine(0x89A7, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&80BE). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &80BE.

The BIT &FE18 (INTOFF) at entry and BIT &FE20 (INTON) before RTI
in nmi_rti are essential for edge-triggered NMI re-delivery.
The 6502 /NMI is falling-edge triggered; the Econet NMI enable
flip-flop (IC97) gates the ADLC IRQ onto /NMI. INTOFF clears
the flip-flop, forcing /NMI high; INTON sets it, allowing the
ADLC IRQ through. This creates a guaranteed high-to-low edge on
/NMI even when the ADLC IRQ is continuously asserted (e.g. when
it transitions atomically from TDRA to frame-complete without
de-asserting). Without this mechanism, nmi_tx_complete would
never fire after tx_last_data.""")


d.subroutine(0x89B5, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""ROM-resident version of the NMI exit sequence, also
the source for the initial copy to RAM at &0D0E.
set_nmi_vector (&0D0E): writes both hi and lo bytes
of the JMP target at &0D0C/&0D0D. nmi_rti (&0D14):
restores the original ROM bank, pulls Y and A from
the stack, then BIT &FE20 (INTON) to re-enable the
NMI flip-flop before RTI. The INTON creates a
guaranteed falling edge on /NMI if the ADLC IRQ is
already asserted, ensuring the next handler fires
immediately.""")

d.label(0x8A6F, 'start_rom_scan')


d.subroutine(0x8AEA, 'scan_remote_keys', title='Scan keyboard for remote operation keys', description="""Uses OSBYTE &7A with Y=&7F to check whether
remote operation keys (&CE-&CF) are currently
pressed. If neither key is detected, clears
svc_state and nfs_workspace to zero via the
clear_svc_and_ws entry point, which is also used
directly by cmd_roff. Called by check_escape.""")


d.subroutine(0x8B02, 'save_text_ptr', title='Save OS text pointer for later retrieval', description="""Copies &F2/&F3 into fs_crc_lo/fs_crc_hi. Called by
svc_4_star_command and svc_9_help before attempting
command matches, and by match_fs_cmd during
iterative help topic matching. Preserves A via
PHA/PLA.""", on_exit={'a': 'preserved'})


d.subroutine(0x8B98, 'print_cmd_table', title='Print *HELP command listing with optional header', description="""If V flag is set, saves X/Y, calls
print_version_header to show the ROM version
string and station number, then restores X/Y.
If V flag is clear, outputs a newline only.
Either path then falls through to
print_cmd_table_loop to enumerate commands.""", on_entry={'x': 'offset into cmd_table_fs', 'v': 'set=print version header, clear=newline only'})


d.subroutine(0x8BAB, 'print_cmd_table_loop', title='Enumerate and print command table entries', description="""Walks the ANFS command table from offset X,
printing each command name padded to 9 characters
followed by its syntax description. Entries with
bit 7 set mark end-of-table. The syntax descriptor
byte's low 5 bits index into cmd_syntax_table;
index &0E triggers special handling that lists
shared command names in parentheses. Calls
help_wrap_if_serial to handle line continuation
on serial output streams. Preserves Y.""", on_entry={'x': 'offset into cmd_table_fs'})


d.subroutine(0x8C33, 'help_wrap_if_serial', title='Wrap *HELP syntax lines for serial output', description="""Checks the output destination via &0355. Returns
immediately for VDU (stream 0) or printer
(stream 3) output. For serial streams, outputs a
newline followed by 12 spaces of indentation to
align continuation lines with the syntax
description column.""", on_exit={'y': 'preserved'})


d.subroutine(0x8C9F, 'print_version_header', title='Print ANFS version string and station number', description="""Uses an inline string after JSR print_inline:
CR + "Advanced  4.08.53" + CR. After the inline
string, JMPs to print_station_id to append the
local Econet station number.""")


d.subroutine(0x8CB9, 'get_ws_page', title='Read workspace page number for current ROM slot', description="""Indexes into the MOS per-ROM workspace table at
&0DF0 using romsel_copy (&F4) as the ROM slot.
Returns the allocated page number in both A and Y
for caller convenience.""", on_exit={'a': 'workspace page number', 'y': 'workspace page number (same as A)'})


d.subroutine(0x8CC0, 'setup_ws_ptr', title='Set up zero-page pointer to workspace page', description="""Calls get_ws_page to read the page number, stores
it as the high byte in nfs_temp (&CD), and clears
the low byte at &CC to zero. This gives a
page-aligned pointer used by FS initialisation and
cmd_net_fs to access the private workspace.""", on_exit={'a': '0', 'y': 'workspace page number'})


d.subroutine(0x8CFC, 'notify_new_fs', title='Notify OS of filing system selection', description="""Calls FSCV with A=6 to announce the FS change,
then issues paged ROM service call 10 via OSBYTE
&8F to inform other ROMs. Sets X=&0A and branches
to issue_svc_osbyte which falls through from the
call_fscv subroutine.""")


d.subroutine(0x8D05, 'call_fscv', title='Dispatch to filing system control vector (FSCV)', description="""Indirect JMP through FSCV at &021E, providing
OS-level filing system services such as FS
selection notification (A=6) and *RUN handling.
Also contains issue_svc_15 and issue_svc_osbyte
entry points that issue paged ROM service requests
via OSBYTE &8F.""", on_entry={'a': 'FSCV reason code'})


d.subroutine(0x8D17, 'check_credits_easter_egg', title='Easter egg: match *HELP keyword to author credits', description="""Matches the *HELP argument against a keyword
embedded in the credits data at
credits_keyword_start. Starts matching from offset
5 in the data (X=5) and checks each byte against
the command line text until a mismatch or X reaches
&0D. On a full match, prints the ANFS author
credits string: B Cockburn, J Dunn, B Robertson,
and J Wills, each terminated by CR.""")


d.subroutine(0x8E09, 'clear_if_station_match', title='Clear stored station if parsed argument matches', description="""Parses a station number from the command line via
init_bridge_poll and compares it with the expected
station at &0E01 using EOR. If the parsed value
matches (EOR result is zero), clears &0E01. Called
by cmd_iam when processing a file server address
in the logon command.""", on_exit={'a': '0 if matched, non-zero if different'})

d.label(0x8E15, 'check_urd_prefix')


d.subroutine(0x8E43, 'dir_op_dispatch', title='Dispatch directory operation via PHA/PHA/RTS', description="""Validates X < 5 and sets Y=&0E as the directory
dispatch offset, then falls through to svc_dispatch
for PHA/PHA/RTS table dispatch. Called by
tx_done_os_proc to handle directory operations
(e.g. FILEV, ARGSV) from the remote JSR service.""", on_entry={'x': 'directory operation code (0-4)'})


d.subroutine(0x8E8C, 'osbyte_x0_y0', title='OSBYTE wrapper with X=0, Y=0', description="""Sets X=0 and Y=0 then branches to jmp_osbyte.
Called from the Econet OSBYTE dispatch chain to
handle OSBYTEs that require both X and Y cleared.
The unconditional BEQ (after LDY #0 sets Z)
reaches the JMP osbyte instruction at &8E87.""", on_entry={'a': 'OSBYTE number'}, on_exit={'x': '0', 'y': '0'})


d.subroutine(0x8EAC, 'store_ws_page_count', title='Record workspace page count (capped at &21)', description="""Stores the workspace allocation from service 1
into offset &0B of the receive control block,
capping the value at &21 to prevent overflow into
adjacent workspace areas. Called by
svc_2_private_workspace after issuing the absolute
workspace claim service call.""", on_entry={'y': 'workspace page count from service 1'})

d.label(0x8F3D, 'done_alloc_handles')


d.subroutine(0x8F5D, 'init_adlc_and_vectors', title='Initialise ADLC and install extended vectors', description="""Reads the ROM pointer table via OSBYTE &A8,
writes vector addresses and ROM ID into the
extended vector table for NETV and one additional
vector, then restores any previous FS context.""")


d.subroutine(0x8F70, 'write_vector_entry', title='Install extended vector table entries', description="""Copies vector addresses from the dispatch table at
svc_dispatch_lo_offset+Y into the MOS extended
vector table pointed to by fs_error_ptr. For each
entry, writes address low, high, then the current
ROM ID from romsel_copy (&F4). Loops X times.
After the loop, stores &FF at &0D72 as an
installed flag, calls deselect_fs_if_active and
get_ws_page to restore FS state.""", on_entry={'x': 'number of vectors to install', 'y': 'starting offset in extended vector table'}, on_exit={'y': 'workspace page number + 1'})


d.subroutine(0x8F8C, 'restore_fs_context', title='Restore FS context from saved workspace', description="""Copies 8 bytes (offsets 2 to 9) from the saved
workspace at &0DFA back into the receive control
block via (net_rx_ptr). This restores the station
identity, directory handles, and library path after
a filing system reselection. Called by
svc_2_private_workspace during init,
deselect_fs_if_active during FS teardown, and
flip_set_station_boot.""")


d.subroutine(0x8F99, 'fscv_6_shutdown', title='Deselect filing system and save workspace', description="""If the filing system is currently selected
(bit 7 of &0D6C set), closes all open FCBs,
closes SPOOL/EXEC files via OSBYTE &77,
saves the FS workspace to page &10 shadow
with checksum, and clears the selected flag.""")


d.subroutine(0x8FCB, 'verify_ws_checksum', title='Verify workspace checksum integrity', description="""Sums bytes 0 to &76 of the workspace page via the
zero-page pointer at &CC/&CD and compares with the
stored value at offset &77. On mismatch, raises a
'net sum' error (&AA). The checksummed page holds
open file information (preserved when NFS is not
the current filing system) and the current printer
type. Can only be reset by a control BREAK.
Preserves A, Y, and processor flags using PHP/PHA.
Called by 5 sites across format_filename_field,
adjust_fsopts_4bytes, and start_wipe_pass before
workspace access.""", on_exit={'a': 'preserved', 'y': 'preserved'})


d.subroutine(0x8FF1, 'print_station_id', title='Print Econet station number and clock status', description="""Uses print_inline to output 'Econet Station ',
then reads the station ID from offset 1 of the
receive control block and prints it as a decimal
number via print_num_no_leading. Tests ADLC
status register 2 (&FEA1) to detect the Econet
clock; if absent, appends ' No Clock' via a
second inline string. Finishes with OSNEWL.
Called by print_version_header and svc_3_auto_boot.""")


d.subroutine(0x912F, 'print_hex_byte', title='Print A as two hexadecimal digits', description="""Saves A on the stack, shifts right four times
to isolate the high nybble, calls
print_hex_nybble to print it, then restores
the full byte and falls through to
print_hex_nybble for the low nybble. Called by
print_5_hex_bytes, cmd_ex, cmd_dump, and
print_dump_header.""", on_entry={'a': 'byte to print'}, on_exit={'a': 'original byte value'})


d.subroutine(0x9138, 'print_hex_nybble', title='Print low nybble of A as hex digit', description="""Masks A to the low 4 bits, then converts to
ASCII: adds 7 for letters A-F (via ADC #6 with
carry set from the CMP), then ADC #&30 for the
final '0'-'F' character. Outputs via JMP OSASCI.""", on_entry={'a': 'value (low nybble used)'})


d.subroutine(0x916E, 'parse_addr_arg', title='Parse decimal or hex station address argument', description="""Reads from the command argument at (&BE),Y.
Supports '&' prefix for hex, '.' separator for
net.station addresses, and plain decimal.
Returns result in A. Raises errors for
bad digits, overflow, or zero values.""")


d.subroutine(0x9258, 'is_decimal_digit', title="Test for digit, '&', or '.' separator", description="""Compares A against '&' and '.' first; if
either matches, returns with carry set via the
shared return_12 exit. Otherwise falls through
to is_dec_digit_only for the '0'-'9' range
test. Called by cmd_iam, cmd_ps, and
cmd_pollps when parsing station addresses.""", on_entry={'a': 'character to test'}, on_exit={'c': 'set if digit/&/., clear otherwise'})


d.subroutine(0x9260, 'is_dec_digit_only', title="Test for decimal digit '0'-'9'", description="""Uses two CMPs to bracket-test A against the
range &30-&39. CMP #&3A sets carry if A >= ':'
(above digits), then CMP #&30 sets carry if
A >= '0'. The net effect: carry set only for
'0'-'9'. Called by parse_addr_arg.""", on_entry={'a': 'character to test'}, on_exit={'c': "set if '0'-'9', clear otherwise"})


d.subroutine(0x9269, 'get_access_bits', title='Read and encode directory entry access byte', description="""Loads the access byte from offset &0E of the
directory entry via (fs_options),Y, masks to 6
bits (AND #&3F), then sets X=4 and branches to
begin_prot_encode to map through the protection
bit encode table at &9286. Called by
check_and_setup_txcb for owner and public access.""", on_exit={'a': 'encoded access flags'})


d.subroutine(0x9273, 'get_prot_bits', title='Encode protection bits via lookup table', description="""Masks A to 5 bits (AND #&1F), sets X=&FF to
start at table index 0, then enters the shared
encoding loop at begin_prot_encode. Shifts out
each source bit and ORs in the corresponding
value from prot_bit_encode_table (&9286). Called
by send_txcb_swap_addrs and check_and_setup_txcb.""", on_entry={'a': 'raw protection bits (low 5 used)'}, on_exit={'a': 'encoded protection flags'})


d.subroutine(0x9291, 'set_text_and_xfer_ptr', title='Set OS text pointer then transfer parameters', description="""Stores X/Y into the MOS text pointer at
&F2/&F3, then falls through to set_xfer_params
and set_options_ptr to configure the full FS
transfer context. Called by byte_to_2bit_index.""", on_entry={'x': 'text pointer low byte', 'y': 'text pointer high byte'})


d.subroutine(0x9295, 'set_xfer_params', title='Set FS transfer byte count and source pointer', description="""Stores A into fs_last_byte_flag (&BD) as the
transfer byte count, and X/Y into fs_crc_lo/hi
(&BE/&BF) as the source data pointer. Falls
through to set_options_ptr to complete the
transfer context setup. Called by 5 sites across
cmd_ex, format_filename_field, and gsread_to_buf.""", on_entry={'a': 'transfer byte count', 'x': 'source pointer low', 'y': 'source pointer high'})


d.subroutine(0x929B, 'set_options_ptr', title='Set FS options pointer and clear escape flag', description="""Stores X/Y into fs_options/fs_block_offset
(&BB/&BC) as the options block pointer. Then
enters clear_escapable which uses PHP/LSR/PLP
to clear bit 0 of the escape flag at &97 without
disturbing processor flags. Called by
format_filename_field and send_and_receive.""", on_entry={'x': 'options pointer low', 'y': 'options pointer high'})


d.subroutine(0x92A4, 'cmp_5byte_handle', title='Compare 5-byte handle buffers for equality', description="""Loops X from 4 down to 1, comparing each byte
of l00af+X with fs_load_addr_3+X using EOR.
Returns on the first mismatch (Z=0) or after
all 5 bytes match (Z=1). Called by
send_txcb_swap_addrs and check_and_setup_txcb
to verify station/handle identity.""", on_exit={'z': 'set if all 5 bytes match'})


d.subroutine(0x92B5, 'set_conn_active', title='Set connection-active flag in channel table', description="""Saves registers on the stack, recovers the
original A from the stack via TSX/LDA &0102,X,
then calls attr_to_chan_index to find the channel
slot. ORs bit 6 (&40) into the channel status
byte at &1060+X. Preserves A, X, and processor
flags via PHP/PHA/PLA/PLP. Called by
format_filename_field and adjust_fsopts_4bytes.""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x92CC, 'clear_conn_active', title='Clear connection-active flag in channel table', description="""Mirror of set_conn_active but ANDs the channel
status byte with &BF (bit 6 clear mask) instead
of ORing. Uses the same register-preservation
pattern: PHP/PHA/TSX to recover A, then
attr_to_chan_index to find the slot. Shares the
done_conn_flag exit with set_conn_active.""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x9309, 'check_not_ampersand', title="Reject '&' as filename character", description="""Loads the first character from the parse buffer
at &0E30 and compares with '&' (&26). Branches
to error_bad_filename if matched, otherwise
returns. Also contains read_filename_char which
loops reading characters from the command line
into the TX buffer at &0F05, calling
strip_token_prefix on each byte and terminating
on CR. Used by cmd_fs_operation and cmd_rename.""")


d.subroutine(0x9327, 'copy_fs_cmd_name', title='Copy matched command name to TX buffer', description="""Scans backwards in cmd_table_fs from the
current position to find the bit-7 flag byte
marking the start of the command name. Copies
each character forward into the TX buffer at
&0F05 until the next bit-7 byte (end of name),
then appends a space separator. Called by
cmd_fs_operation and cmd_rename.""", on_exit={'x': 'TX buffer offset past name+space', 'y': 'command line offset (restored)'})


d.subroutine(0x9349, 'parse_quoted_arg', title='Parse possibly-quoted filename argument', description="""Reads from the command line at (&BE),Y. Handles
double-quote delimiters and stores the result
in the parse buffer at &0E30. Raises 'Bad string'
on unbalanced quotes.""")


d.subroutine(0x9465, 'init_txcb_bye', title='Set up open receive for FS reply on port &90', description="""Loads A=&90 (the FS command/reply port) and
falls through to init_txcb_port, which creates
an open receive control block: the template sets
txcb_ctrl to &80, then DEC makes it &7F (bit 7
clear = awaiting reply). The NMI RX handler sets
bit 7 when a reply arrives on this port, which
wait_net_tx_ack polls for.""")


d.subroutine(0x9467, 'init_txcb_port', title='Create open receive control block on specified port', description="""Calls init_txcb to copy the 12-byte template
into the TXCB workspace at &00C0, then stores A
as the port (txcb_port at &C1) and sets
txcb_start to 3. The DEC txcb_ctrl changes the
control byte from &80 to &7F (bit 7 clear),
creating an open receive: the NMI RX handler
will set bit 7 when a reply frame arrives on
this port, which wait_net_tx_ack polls for.""", on_entry={'a': 'port number'})


d.subroutine(0x9473, 'init_txcb', title='Initialise TX control block from ROM template', description="""Copies 12 bytes from txcb_init_template (&948B)
into the TXCB workspace at &00C0. For the first
two bytes (Y=0,1), also copies the destination
station/network from &0E00 into txcb_dest (&C2).
Preserves A via PHA/PLA. Called by 4 sites
including cmd_pass, init_txcb_port,
prep_send_tx_cb, and send_wipe_request.""")


d.subroutine(0x9497, 'send_request_nowrite', title='Send read-only FS request (carry set)', description="""Pushes A and sets carry to indicate no-write
mode, then branches to txcb_copy_carry_set to
enter the common TXCB copy, send, and reply
processing path. The carry flag controls whether
a disconnect is sent on certain reply codes.
Called by setup_transfer_workspace.""")


d.subroutine(0x949B, 'send_request_write', title='Send read-write FS request (V clear)', description="""Clears V flag and branches unconditionally to
txcb_copy_carry_clr (via BVC, always taken after
CLV) to enter the common TXCB copy, send, and
reply processing path with carry clear (write
mode). Called by do_fs_cmd_iteration and
send_txcb_swap_addrs.""")


d.subroutine(0x94AD, 'save_net_tx_cb', title='Save FS state and send command to file server', description="""Copies station address and function code (Y)
to the TX buffer, builds the TXCB, sends the
packet, and waits for the reply. V is clear
for standard mode.""")


d.subroutine(0x94AE, 'save_net_tx_cb_vset', title='Save and send TXCB with V flag set', description="""Variant of save_net_tx_cb for callers that have
already set V. Copies the FS station address
from &0E02 to &0F02, then falls through to
txcb_copy_carry_clr which clears carry and enters
the common TXCB copy, send, and reply path.
Called by check_and_setup_txcb,
format_filename_field, and cmd_remove.""")


d.subroutine(0x94DA, 'prep_send_tx_cb', title='Build TXCB from scratch, send, and receive reply', description="""Full send/receive cycle comprising two separate
Econet transactions. Saves flags, sets reply
port &90, calls init_txcb, computes txcb_end
from X+5. C set dispatches to handle_disconnect;
C clear calls init_tx_ptr_and_send for a
client-initiated four-way handshake (scout, ACK,
data, ACK) to deliver the command. After TX
completes the ADLC returns to idle RX listen.
Then falls through to recv_and_process_reply
which waits for the server to independently
initiate a new four-way handshake with the
reply on port &90. There is no reply data in
the original ACK payload.""")


d.subroutine(0x94F0, 'recv_and_process_reply', title='Receive FS reply and dispatch on status codes', description="""Waits for a server-initiated reply transaction.
After the command TX completes (a separate
client-initiated four-way handshake), calls
init_txcb_bye to set up an open receive on
port &90 (txcb_ctrl = &7F). The server
independently initiates a new four-way handshake
to deliver the reply; the NMI RX handler matches
the incoming scout against this RXCB and sets
bit 7 on completion. wait_net_tx_ack polls for
this. Iterates over reply bytes: zero terminates,
V-set codes are adjusted by +&2B, and non-zero
codes dispatch to store_reply_status. Handles
disconnect requests (C set from prep_send_tx_cb)
and 'Data Lost' warnings when channel status
bits indicate pending writes were interrupted.""")


d.subroutine(0x9570, 'check_escape', title='Check for pending escape condition', description="""ANDs the MOS escape flag (&FF) with the
escapable flag at &97. If bit 7 of the result
is clear (no escape or escape disabled), returns
immediately. Otherwise enters raise_escape_error:
acknowledges the escape via OSBYTE &7E, then
jumps to classify_reply_error with A=6 to raise
the Escape error. Called by cmd_pass and
send_net_packet.""")


d.subroutine(0x95DD, 'wait_net_tx_ack', title='Wait for reply on open receive with timeout', description="""Despite the name, this does not wait for a TX
acknowledgment. It polls an open receive control
block (bit 7 of txcb_ctrl, set to &7F by
init_txcb_port) until the NMI RX handler delivers
a reply frame and sets bit 7. Uses a three-level
nested polling loop: inner and middle counters
start at 0 (wrapping to 256 iterations each),
outer counter from rx_wait_timeout (&0D6E,
default &28 = 40). Total: 256 x 256 x 40 =
2,621,440 poll iterations. At ~17 cycles per
poll on a 2 MHz 6502, the default gives ~22
seconds. On timeout, branches to
build_no_reply_error to raise 'No reply'.
Called by 6 sites across the protocol stack.""")


d.subroutine(0x9611, 'cond_save_error_code', title='Conditionally store error code to workspace', description="""Tests bit 7 of &0D6C (FS selected flag). If
clear, returns immediately. If set, stores A
into &0E09 as the last error code. This guards
against writing error state when no filing system
is active. Called internally by the error
classification chain and by error_inline_log.""", on_entry={'a': 'error code to store'})

d.label(0x971E, 'close_exec_via_y')


d.subroutine(0x974D, 'append_drv_dot_num', title="Append 'net.station' decimal string to error text", description="""Reads network and station numbers from the TX
control block at offsets 3 and 2. Writes a space
separator then the network number (if non-zero),
a dot, and the station number as decimal digits
into the error text buffer at the current position.""", on_entry={'x': 'error text buffer index'}, on_exit={'x': 'updated buffer index past appended text'})


d.subroutine(0x9771, 'append_space_and_num', title='Append space and decimal number to error text', description="""Writes a space character to the error text buffer
at the current position (fs_load_addr_2), then falls
through to append_decimal_num to convert the value
in A to decimal digits with leading zero suppression.""", on_entry={'a': 'number to append (0-255)'})


d.subroutine(0x977C, 'append_decimal_num', title='Convert byte to decimal and append to error text', description="""Extracts hundreds, tens and units digits by three
successive calls to append_decimal_digit. Uses the
V flag to suppress leading zeros — hundreds and tens
are skipped when zero, but the units digit is always
emitted.""", on_entry={'a': 'number to convert (0-255)'})


d.subroutine(0x978D, 'append_decimal_digit', title='Extract and append one decimal digit', description="""Divides Y by A using repeated subtraction to extract
a single decimal digit. Stores the ASCII digit in the
error text buffer at fs_load_addr_2 unless V is set
and the quotient is zero (leading zero suppression).
Returns the remainder in Y for subsequent digit
extraction.""", on_entry={'a': 'divisor (100, 10, or 1)', 'y': 'number to divide', 'v': 'set to suppress leading zero'}, on_exit={'y': 'remainder after division', 'v': 'clear once a non-zero digit is emitted'})


d.subroutine(0x9837, 'init_tx_ptr_and_send', title='Point TX at zero-page TXCB and send', description="""Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the
standard TXCB location in zero page), then falls
through to send_net_packet for transmission with
retry logic.""")


d.subroutine(0x983F, 'send_net_packet', title='Transmit Econet packet with retry', description="""Two-phase transmit with retry. Loads retry count
from tx_retry_count (&0D6D, default &FF = 255;
0 means retry forever). Each failed attempt waits
in a nested delay loop: X = TXCB control byte
(typically &80), Y = &60; total ~61 ms at 2 MHz
(ROM-only fetches, unaffected by video mode).
Phase 1 runs the full count with escape disabled.
Phase 2 only activates when tx_retry_count = 0:
sets need_release_tube to enable escape checking
and retries indefinitely. With default &FF, phase
2 is never entered. Failures go to
load_reply_and_classify (Line jammed, Net error,
etc.), distinct from the 'No reply' timeout in
wait_net_tx_ack.""")


d.subroutine(0x9894, 'init_tx_ptr_for_pass', title='Set up TX pointer and send pass-through packet', description="""Copies the template into the TX buffer (skipping
&FD markers), saves original values on stack,
then polls the ADLC and retries until complete.""")


d.subroutine(0x989C, 'setup_pass_txbuf', title='Initialise TX buffer from pass-through template', description="""Copies 12 bytes from pass_txbuf_init_table into the
TX control block, pushing the original values on the
stack for later restoration. Skips offsets marked &FD
in the template. Starts transmission via
poll_adlc_tx_status and retries on failure, restoring
the original TX buffer contents when done.""")


d.subroutine(0x98C9, 'poll_adlc_tx_status', title='Wait for TX ready, then start new transmission', description="""Polls tx_complete_flag via ASL (testing bit 7)
until set, indicating any previous TX operation
has completed and the ADLC is back in idle RX
listen mode. Then copies the TX control block
pointer from net_tx_ptr to nmi_tx_block and
calls tx_begin, which performs a complete
transmission from scratch: copies destination
from TXCB to scout buffer, polls for INACTIVE,
configures ADLC (CR1=&44 RX_RESET|TIE, CR2=&E7
RTS|CLR), and runs the full four-way handshake
via NMI. After tx_begin returns, polls the TXCB
first byte until bit 7 clears (NMI handler
stores result there). Returns result in A:
&00=success, &40=jammed, &41=not listening,
&43=no clock, &44=bad control byte.""")


d.subroutine(0x9908, 'load_text_ptr_and_parse', title='Copy text pointer from FS options and parse string', description="""Reads a 2-byte address from (fs_options)+0/1 into
os_text_ptr (&00F2), resets Y to zero, then falls
through to gsread_to_buf to parse the string at that
address into the &0E30 buffer.""")


d.subroutine(0x9913, 'gsread_to_buf', title='Parse command line via GSINIT/GSREAD into &0E30', description="""Calls GSINIT to initialise string reading, then
loops calling GSREAD to copy characters into the
l0e30 buffer until end-of-string. Appends a CR
terminator and sets fs_crc_lo/hi to point at &0E30
for subsequent parsing routines.""")


d.subroutine(0x9951, 'do_fs_cmd_iteration', title='Execute one iteration of a multi-step FS command', description="""Called by match_fs_cmd for commands that enumerate
directory entries. Sets port &92, sends the initial
request via send_request_write, then synchronises the
FS options and workspace state (order depends on the
cycle flag at offset 6). Copies 4 address bytes,
formats the filename field, sends via
send_txcb_swap_addrs, and receives the reply.""")


d.subroutine(0x9998, 'send_txcb_swap_addrs', title='Send TXCB and swap start/end addresses', description="""If the 5-byte handle matches, returns
immediately. Otherwise sets port &92, copies
addresses, sends, waits for acknowledgment,
and retries on address mismatch.""")


d.subroutine(0x9A57, 'print_load_exec_addrs', title='Print exec address and file length in hex', description="""Prints the exec address as 5 hex bytes from
(fs_options) offset 9 downwards, then the file
length as 3 hex bytes from offset &0C. Each group
is followed by a space separator via OSASCI.""")


d.subroutine(0x9A62, 'print_5_hex_bytes', title='Print hex byte sequence from FS options', description="""Outputs X+1 bytes from (fs_options) starting at
offset Y, decrementing Y for each byte (big-endian
display order). Each byte is printed as two hex
digits via print_hex_byte. Finishes with a trailing
space via OSASCI. The default entry with X=4 prints
5 bytes (a full 32-bit address plus extent).""", on_entry={'x': 'byte count minus 1 (default 4 for 5 bytes)', 'y': 'starting offset in (fs_options)'})


d.subroutine(0x9A72, 'copy_fsopts_to_zp', title='Copy FS options address bytes to zero page', description="""Copies 4 bytes from (fs_options) at offsets 2-5
into zero page at &00AE+Y. Used by
do_fs_cmd_iteration to preserve the current address
state. Falls through to skip_one_and_advance5 to
advance Y past the copied region.""")


d.subroutine(0x9A7E, 'skip_one_and_advance5', title='Advance Y by 5', description="""Entry point one INY before advance_y_by_4, giving
a total Y increment of 5. Used to skip past a
5-byte address/length structure in the FS options
block.""")


d.subroutine(0x9A7F, 'advance_y_by_4', title='Advance Y by 4', description="""Four consecutive INY instructions. Used as a
subroutine to step Y past a 4-byte address field
in the FS options or workspace structure.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset + 4'})


d.subroutine(0x9A84, 'copy_workspace_to_fsopts', title='Copy workspace reply data to FS options', description="""Copies bytes from the reply buffer at &0F02+Y
into (fs_options) at offsets &0D down to 2. Used
to update the FS options block with data returned
from the file server. Falls through to
retreat_y_by_4.""")


d.subroutine(0x9A91, 'retreat_y_by_4', title='Retreat Y by 4', description="""Four consecutive DEY instructions. Companion to
advance_y_by_4 for reverse traversal of address
structures.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 4'})


d.subroutine(0x9A92, 'retreat_y_by_3', title='Retreat Y by 3', description="""Three consecutive DEY instructions. Used by
setup_transfer_workspace to step back through
interleaved address pairs in the FS options block.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 3'})


d.subroutine(0x9A9A, 'check_and_setup_txcb', title='Set up data transfer TXCB and dispatch reply', description="""Compares the 5-byte handle; if unchanged,
returns. Otherwise computes start/end addresses
with overflow clamping, sets the port and control
byte, sends the packet, and dispatches on the
reply sub-operation code.""")


d.subroutine(0x9B95, 'format_filename_field', title='Format filename into fixed-width display field', description="""Builds a 12-character space-padded filename at
&10F3 for directory listing output. Sources the
name from either the command line or the l0f05
reply buffer depending on the value in l0f03.
Truncates or pads to exactly 12 characters.""")


d.subroutine(0x9E0F, 'update_addr_from_offset9', title='Update both address fields in FS options', description="""Calls add_workspace_to_fsopts for offset 9 (the
high address / exec address field), then falls
through to update_addr_from_offset1 to process
offset 1 (the low address / load address field).""")


d.subroutine(0x9E14, 'update_addr_from_offset1', title='Update low address field in FS options', description="""Sets Y=1 and falls through to
add_workspace_to_fsopts to add the workspace
adjustment bytes to the load address field at
offset 1 in the FS options block.""", on_entry={'c': 'carry state passed to add_workspace_to_fsopts'})


d.subroutine(0x9E16, 'add_workspace_to_fsopts', title='Add workspace bytes to FS options with clear carry', description="""Clears carry and falls through to
adjust_fsopts_4bytes. Provides a convenient entry
point when the caller needs addition without a
preset carry.""", on_entry={'y': 'FS options offset for first byte'})


d.subroutine(0x9E17, 'adjust_fsopts_4bytes', title='Add or subtract 4 workspace bytes from FS options', description="""Processes 4 consecutive bytes at (fs_options)+Y,
adding or subtracting the corresponding workspace
bytes from &0E0A-&0E0D. The direction is controlled
by bit 7 of fs_load_addr_2: set for subtraction,
clear for addition. Carry propagates across all 4
bytes for correct multi-byte arithmetic.""", on_entry={'y': 'FS options offset for first byte', 'c': 'carry input for first byte'})

d.label(0x9ECD, 'return_success')


d.subroutine(0x9ED2, 'lookup_cat_entry_0', title='Look up channel from FS options offset 0', description="""Loads the channel handle from (fs_options) at
offset 0, then falls through to lookup_cat_slot_data
to find the corresponding FCB entry.""", on_exit={'a': 'FCB flag byte from &1030+X', 'x': 'channel slot index'})


d.subroutine(0x9ED6, 'lookup_cat_slot_data', title='Look up channel and return FCB flag byte', description="""Calls lookup_chan_by_char to find the channel
slot for handle A in the channel table, then
loads the FCB flag byte from &1030+X.""", on_entry={'a': 'channel handle'}, on_exit={'a': 'FCB flag byte', 'x': 'channel slot index'})


d.subroutine(0x9EDD, 'setup_transfer_workspace', title='Prepare workspace for OSGBPB data transfer', description="""Orchestrates the setup for OSGBPB (get/put
multiple bytes) operations. Looks up the channel,
copies the 6-byte address structure from FS options
(skipping the hole at offset 8), determines transfer
direction from the operation code (even=read,
odd=write), selects port &91 or &92 accordingly,
and sends the FS request. Then configures the TXCB
address pairs for the actual data transfer phase
and dispatches to the appropriate handler.""")


d.subroutine(0x9F67, 'recv_reply_preserve_flags', title='Receive and process reply, preserving flags', description="""Wrapper around recv_and_process_reply that
saves and restores the processor status register,
so the caller's flag state is not affected by
the reply processing.""")


d.subroutine(0x9FD0, 'write_data_block', title='Write data block to destination or Tube', description="""If no Tube present, copies directly from
the l0f05 buffer via (fs_crc_lo). If Tube
is active, claims the Tube, sets up the
transfer address, and writes via R3.""")


d.subroutine(0xA073, 'tube_claim_c3', title='Claim the Tube via protocol &C3', description="""Loops calling tube_addr_data_dispatch with
protocol byte &C3 until the claim succeeds
(carry set on return). Used before Tube data
transfers to ensure exclusive access to the
Tube co-processor interface.""")


d.subroutine(0xA09E, 'print_fs_info_newline', title='Print station address and newline', description="""Sets V (suppressing leading-zero padding on
the network number) then prints the station
address followed by a newline via OSNEWL.
Used by *FS and *PS output formatting.""")


d.subroutine(0xA0A7, 'parse_fs_ps_args', title='Parse station address from *FS/*PS arguments', description="""Reads a station address in 'net.station' format
from the command line, with the network number
optional (defaults to local network). Calls
init_bridge_poll to ensure the bridge routing
table is populated, then validates the parsed
address against known stations.""")


d.subroutine(0xA0CC, 'get_pb_ptr_as_index', title='Convert parameter block pointer to table index', description="""Reads the first byte from the OSWORD parameter
block pointer and falls through to
byte_to_2bit_index to produce a 12-byte-aligned
table index in Y.""")


d.subroutine(0xA0CE, 'byte_to_2bit_index', title='Convert byte to 12-byte-aligned table index', description="""Computes Y = A * 6 (via A*12/2) for indexing
into the OSWORD handler workspace tables.
Clamps Y to zero if the result exceeds &48,
preventing out-of-bounds access.""", on_entry={'a': 'table entry number'}, on_exit={'y': 'byte offset (0, 6, 12, ... up to &42)'})


d.subroutine(0xA140, 'match_fs_cmd', title='Match command name against FS command table', description="""Case-insensitive compare of the command line
against table entries with bit-7-terminated
names. Returns with the matched entry address
on success.""")


d.subroutine(0xA300, 'find_station_bit2', title='Find printer server station in table (bit 2)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 2 set (printer server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""")


d.subroutine(0xA32B, 'find_station_bit3', title='Find file server station in table (bit 3)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 3 set (file server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""")


d.subroutine(0xA362, 'flip_set_station_boot', title='Set boot option for a station in the table', description="""Scans up to 16 station table entries for one
matching the current address with bit 4 set
(boot-eligible). Stores the requested boot type
in the matching entry and calls
restore_fs_context to re-establish the filing
system state.""")


d.subroutine(0xA516, 'osword_setup_handler', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD dispatch table by X to
push a handler address (hi then lo) onto the
stack. Copies 3 bytes from the osword_flag
workspace into the RX buffer, loads PB byte 0
(the OSWORD sub-code), and clears svc_state.
The subsequent RTS dispatches to the pushed
handler address.""", on_entry={'x': 'OSWORD handler index (0-6)'})


d.subroutine(0xA595, 'bin_to_bcd', title='Convert binary byte to BCD', description="""Uses decimal mode (SED) with a count-up loop:
starts at BCD 0 and adds 1 in decimal mode for
each decrement of the binary input. Saves and
restores the processor flags to avoid leaving
decimal mode active. Called 6 times by
save_txcb_and_convert for clock date/time
conversion.""", on_entry={'a': 'binary value (0-99)'}, on_exit={'a': 'BCD equivalent'})


d.subroutine(0xA8E5, 'store_osword_pb_ptr', title='Store workspace pointer+1 to NFS workspace', description="""Computes ws_ptr_hi + 1 and stores the resulting
16-bit address at workspace offset &1C via
store_ptr_at_ws_y. Then reads PB byte 1 (the
transfer length) and adds ws_ptr_hi to compute
the buffer end pointer, stored at workspace
offset &20.""")


d.subroutine(0xA92B, 'store_ptr_at_ws_y', title='Store 16-bit pointer at workspace offset Y', description="""Writes a 16-bit address to (nfs_workspace)+Y.
The low byte comes from A; the high byte is
computed from table_idx plus carry,
supporting pointer arithmetic across page
boundaries.""", on_entry={'a': 'pointer low byte', 'y': 'workspace offset', 'c': 'carry for high byte addition'})


d.subroutine(0xA6F8, 'copy_pb_byte_to_ws', title='Conditionally copy parameter block byte to workspace', description="""If carry is set, loads a byte from the OSWORD
parameter block at offset Y; if clear, uses
the value already in A. Stores the result to
workspace at the current offset. Decrements X
and loops until the requested byte count is
transferred.""", on_entry={'c': 'set to load from PB, clear to use A', 'x': 'byte count', 'y': 'PB source offset'})


d.subroutine(0xA660, 'osword_13_read_station', title='OSWORD &13 sub 0: read file server station', description="""Returns the current file server station and
network numbers in PB[1..2]. If the NFS is not
active (l0d6c bit 7 clear), returns zero in
PB[0] instead.""")


d.subroutine(0xA673, 'osword_13_set_station', title='OSWORD &13 sub 1: set file server station', description="""Sets the file server station and network
numbers from PB[1..2]. Processes all FCBs,
then scans the 16-entry FCB table to
reassign handles matching the new station.
If the NFS is not active, returns zero.""")


d.subroutine(0xA6E8, 'osword_13_read_csd', title='OSWORD &13 sub 12: read CSD path', description="""Reads 5 current selected directory path bytes
from the RX workspace at offset &17 into
PB[1..5]. Sets carry clear to select the
workspace-to-PB copy direction.""")


d.subroutine(0xA6EB, 'osword_13_write_csd', title='OSWORD &13 sub 13: write CSD path', description="""Writes 5 current selected directory path bytes
from PB[1..5] into the RX workspace at offset
&17. Sets carry to select the PB-to-workspace
copy direction.""")


d.subroutine(0xA707, 'osword_13_read_ws_pair', title='OSWORD &13 sub 2: read workspace byte pair', description="""Reads 2 bytes from the NFS workspace page
starting at offset 1 into PB[1..2]. Uses
nfs_workspace_hi as the page and
copy_pb_byte_to_ws with carry clear for the
workspace-to-PB direction.""")


d.subroutine(0xA713, 'osword_13_write_ws_pair', title='OSWORD &13 sub 3: write workspace byte pair', description="""Writes 2 bytes from PB[1..2] into the NFS
workspace at offsets 2 and 3. Then calls
init_bridge_poll and conditionally clears
the workspace byte if the bridge status
changed.""")


d.subroutine(0xA728, 'osword_13_read_prot', title='OSWORD &13 sub 4: read protection mask', description="""Returns the current protection mask (ws_0d68)
in PB[1].""")


d.subroutine(0xA72E, 'osword_13_write_prot', title='OSWORD &13 sub 5: write protection mask', description="""Sets the protection mask from PB[1] via
store_prot_mask.""")


d.subroutine(0xA734, 'osword_13_read_handles', title='OSWORD &13 sub 6: read FCB handle info', description="""Returns the 3-byte FCB handle/port data from
l1071[1..3] in PB[1..3]. If the NFS is not
active, returns zero in PB[0].""")


d.subroutine(0xA744, 'osword_13_set_handles', title='OSWORD &13 sub 7: set FCB handles', description="""Validates and assigns up to 3 FCB handles
from PB[1..3]. Each handle value (&20-&2F)
indexes the l1010/l1040 tables. For valid
handles with bit 2 set in l1040, stores the
station to l0e01+Y and FCB index to l1071+Y,
then updates flag bits across all FCB entries
via update_fcb_flag_bits.""")


d.subroutine(0xA7BF, 'update_fcb_flag_bits', title='Update FCB flag bits across all entries', description="""Scans all 16 FCB entries in l1060. For each
entry with bit 6 set, tests the Y-specified
bit mask: if matching, ORs bit 5 into the
flags; if not, leaves bit 5 clear. In both
cases, inverts and clears the tested bits.
Preserves X.""", on_entry={'y': 'flag bit mask to test', 'x': 'current FCB index (preserved)'})


d.subroutine(0xA7E4, 'osword_13_read_rx_flag', title='OSWORD &13 sub 8: read RX control block flag', description="""Returns byte 1 of the current RX control
block in PB[1].""")


d.subroutine(0xA7ED, 'osword_13_read_rx_port', title='OSWORD &13 sub 9: read RX port byte', description="""Returns byte &7F of the current RX control
block in PB[1], and stores &80 in PB[2].""")


d.subroutine(0xA7FB, 'osword_13_read_error', title='OSWORD &13 sub 10: read error flag', description='Returns the error flag (l0e09) in PB[1].')


d.subroutine(0xA7FE, 'store_a_to_pb_1', title='Store A to OSWORD parameter block at offset 1', description="""Increments Y to 1 and stores A into the
OSWORD parameter block via (ws_ptr_hi),Y.
Used by OSWORD 13 sub-handlers to return a
single result byte.""", on_entry={'A': 'value to store'}, on_exit={'Y': '1'})


d.subroutine(0xA802, 'osword_13_read_context', title='OSWORD &13 sub 11: read context byte', description='Returns the context byte (l0d6d) in PB[1].')


d.subroutine(0xA807, 'osword_13_read_free_bufs', title='OSWORD &13 sub 14: read printer buffer free space', description="""Returns the number of free bytes remaining in
the printer spool buffer (&6F minus spool_buf_idx)
in PB[1]. The buffer starts at offset &25 and can
hold up to &4A bytes of spool data.""")


d.subroutine(0xA80F, 'osword_13_read_ctx_3', title='OSWORD &13 sub 15: read retry counts', description="""Returns the three retry count values in
PB[1..3]: PB[1] = transmit retry count
(default &FF = 255), PB[2] = receive poll
count (default &28 = 40), PB[3] = machine
peek retry count (default &0A = 10). Setting
transmit retries to 0 means retry forever.""")


d.subroutine(0xA81A, 'osword_13_write_ctx_3', title='OSWORD &13 sub 16: write retry counts', description="""Sets the three retry count values from
PB[1..3]: PB[1] = transmit retry count,
PB[2] = receive poll count, PB[3] = machine
peek retry count.""")


d.subroutine(0xA825, 'osword_13_bridge_query', title='OSWORD &13 sub 17: query bridge status', description="""Calls init_bridge_poll, then returns the
bridge status. If l0d72 is &FF (no bridge),
stores 0 in PB[0]. Otherwise stores l0d72
in PB[1] and conditionally updates PB[3]
based on station comparison.""")


d.subroutine(0xA865, 'init_bridge_poll', title='Initialise Econet bridge routing table', description="""Checks the bridge status byte: if &FF
(uninitialised), broadcasts a bridge query
packet and polls for replies. Each reply
adds a network routing entry to the bridge
table. Skips the broadcast if the table has
already been populated from a previous call.""")


d.subroutine(0xA976, 'enable_irq_and_poll', title='Enable interrupts and send Econet packet', description="""Executes CLI to re-enable interrupts, then
falls through to send_net_packet. Used after
a sequence that ran with interrupts disabled
to ensure the packet is sent with normal
interrupt handling active.""")


d.subroutine(0xA97A, 'netv_handler', title='NETV handler: OSWORD dispatch', description="""Installed as the NETV handler via
write_vector_entry. Saves all registers, reads
the OSWORD number from the stack, and dispatches
OSWORDs 0-8 via push_osword_handler_addr. OSWORDs
>= 9 are ignored (registers restored, RTS returns
to MOS). Address stored at netv_handler_addr
(&8E8A) in the extended vector data area.""")


d.subroutine(0xA993, 'push_osword_handler_addr', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD handler dispatch table
using the current OSWORD number to push the
handler's address (hi/lo) onto the stack.
Reloads the OSWORD number from osbyte_a_copy
so the dispatched handler can identify the
specific call.""")


d.subroutine(0xA9B0, 'osword_4_handler', title='OSWORD 4 handler: clear carry and send abort', description="""Clears the carry flag in the stacked processor
status, stores the original Y to workspace at
offset &DA, and falls through to tx_econet_abort
with A=0. Called via OSWORD handler dispatch
table for OSWORD 4 (write interval timer).""")


d.subroutine(0xA9BE, 'tx_econet_abort', title='Send Econet abort/disconnect packet', description="""Stores the abort code in workspace, configures
the TX control block with control byte &80
(immediate operation flag), and transmits the
abort packet. Used to cleanly disconnect from
a remote station during error recovery.""")


d.subroutine(0xA9E2, 'netv_claim_release', title='OSWORD 7 handler: claim/release network resources', description="""Handles OSWORD 7 (SOUND) intercepted via NETV.
Searches the claim code table in two passes:
first 11 entries (state 2), then all 18 (state
3). On match, saves 3 tube state bytes to
workspace and sends an abort with the state
code. For state 3 matches, also polls workspace
for a response and restores the caller's stack
frame from the saved bytes.""")


d.subroutine(0xAA36, 'match_rx_code', title='Search receive code table for match', description="""Scans a table of receive operation codes
starting at index X, comparing each against A.
Returns with Z set if a match is found, Z clear
if the end-of-table marker is reached.""", on_entry={'a': 'receive code to match', 'x': 'starting table index'}, on_exit={'z': 'set if match found'})


d.subroutine(0xAA51, 'osword_8_handler', title='OSWORD 7/8 handler: copy PB to workspace and abort', description="""Handles OSWORD 7 or 8 by copying 15 bytes from
the parameter block to workspace at offset &DB,
storing the OSWORD number at offset &DA, setting
control value &E9, and sending an abort packet.
Returns via tx_econet_abort. Rejects other
OSWORD numbers by returning immediately.""")


d.subroutine(0xAA7C, 'init_ws_copy_wide', title='Initialise workspace copy in wide mode (14 bytes)', description="""Copies 14 bytes to workspace offset &7C.
Falls through to the template-driven copy
loop which handles &FD (skip), &FE (end),
and &FC (page pointer) markers.""")


d.subroutine(0xAA85, 'init_ws_copy_narrow', title='Initialise workspace copy in narrow mode (27 bytes)', description="""Sets up a 27-byte copy to workspace offset &17,
then falls through to ws_copy_vclr_entry for
the template-driven copy loop. Used for the
compact workspace initialisation variant.""")


d.subroutine(0xAA89, 'ws_copy_vclr_entry', title='Template-driven workspace copy with V clear', description="""Processes a template byte array to initialise
workspace. Special marker bytes: &FE terminates
the copy, &FD skips the current offset, and &FC
substitutes the workspace page pointer. All
other values are stored directly to the
workspace at the current offset.""")


d.subroutine(0xAAD8, 'netv_spool_check', title='OSWORD 5 handler: check spool PB and reset buffer', description="""Handles OSWORD 5 intercepted via NETV. Checks
if X-1 matches osword_pb_ptr and bit 0 of
&00D0 is clear. If both conditions are met,
falls through to reset_spool_buf_state to
reinitialise the spool buffer for new data.""")


d.subroutine(0xAAED, 'netv_print_data', title='OSWORD 1-3 handler: drain printer buffer', description="""Handles OSWORDs 1-3 intercepted via NETV.
When X=1, drains the printer buffer (OSBYTE
&91, buffer 3) into the receive buffer, sending
packets via process_spool_data when the buffer
exceeds &6E bytes. When X>1, routes to
handle_spool_ctrl_byte for spool state control.""")


d.subroutine(0xAAE2, 'reset_spool_buf_state', title='Reset spool buffer to initial state', description="""Sets the spool buffer pointer to &25 (first
available data position) and the control state
byte to &41 (ready for new data). Called after
processing a complete spool data block.""")


d.subroutine(0xAB12, 'append_byte_to_rxbuf', title='Append byte to receive buffer', description="""Stores A in the receive buffer at the current
buffer index (ws_ptr_lo), then increments the
index. Used to accumulate incoming spool data
bytes before processing.""", on_entry={'a': 'byte to append'})


d.subroutine(0xAB1B, 'handle_spool_ctrl_byte', title='Handle spool control byte and flush buffer', description="""Rotates bit 0 of the control byte into carry
for mode selection (print vs spool), appends
the byte to the buffer, calls process_spool_data
to transmit the accumulated data, and resets
the buffer state ready for the next block.""")


d.subroutine(0xAB36, 'process_spool_data', title='Transmit accumulated spool buffer data', description="""Copies the workspace state to the TX control
block, sends a disconnect reply if the previous
transfer requires acknowledgment, then handles
the spool output sequence by setting up and
sending the pass-through TX buffer.""")


d.subroutine(0xAC24, 'send_disconnect_reply', title='Send Econet disconnect reply packet', description="""Sets up the TX pointer, copies station
addresses, matches the station in the table,
and sends the response. Waits for
acknowledgment before returning.""")


d.subroutine(0xACDD, 'commit_state_byte', title='Copy current state byte to committed state', description="""Reads the working state byte from workspace and
stores it to the committed state location. Used
to finalise a state transition after all related
workspace fields have been updated.""")


d.subroutine(0xACE4, 'serialise_palette_entry', title='Serialise palette register to workspace', description="""Reads the current logical colour for a palette
register via OSBYTE &0B and stores both the
palette value and the display mode information
in the workspace block. Used during remote
screen state capture.""")


d.subroutine(0xACF7, 'read_osbyte_to_ws_x0', title='Read OSBYTE with X=0 and store to workspace', description="""Sets X=0 then falls through to read_osbyte_to_ws
to issue the OSBYTE call and store the result.
Used when the OSBYTE parameter X must be zero.""")


d.subroutine(0xACF9, 'read_osbyte_to_ws', title='Issue OSBYTE from table and store result', description="""Loads the OSBYTE function code from the next
entry in the OSBYTE table, issues the call, and
stores the Y result in workspace at the current
offset. Advances the table pointer for the next
call.""")


d.subroutine(0xAE82, 'print_10_chars', title='Print 10 characters from reply buffer', description="""Sets Y=10 and falls through to
print_chars_from_buf. Used by cmd_ex to print
fixed-width directory title, directory name, and
library name fields.""", on_entry={'x': 'buffer offset to start printing from'})


d.subroutine(0xAE84, 'print_chars_from_buf', title='Print Y characters from buffer via OSASCI', description="""Loops Y times, loading each byte from l0f05+X
and printing it via OSASCI. Advances X after
each character, leaving X pointing past the
last printed byte.""", on_entry={'x': 'buffer offset', 'y': 'character count'})


d.subroutine(0xAE92, 'parse_cmd_arg_y0', title='Parse command argument from offset zero', description="""Sets Y=0 and falls through to parse_filename_arg
for GSREAD-based filename parsing with prefix
character handling.""")


d.subroutine(0xAE94, 'parse_filename_arg', title='Parse filename via GSREAD with prefix handling', description="""Calls gsread_to_buf to read the command line
string into the &0E30 buffer, then falls through
to parse_access_prefix to process '&', ':', '.',
and '#' prefix characters.""")


d.subroutine(0xAE97, 'parse_access_prefix', title='Parse access and FS selection prefix characters', description="""Examines the first character(s) of the parsed
buffer at &0E30 for prefix characters: '&' sets
the FS selection flag (bit 6 of l1071) and strips
the prefix, ':' with '.' also triggers FS
selection, '#' is accepted as a channel prefix.
Raises 'Bad file name' for invalid combinations
like '&.' followed by CR.""")


d.subroutine(0xAEB7, 'strip_token_prefix', title='Strip first character from parsed token buffer', description="""Shifts all bytes in the &0E30 buffer left by
one position (removing the first character),
then trims any trailing spaces by replacing
them with CR terminators. Used after consuming
a prefix character like '&' or ':'.""")


d.subroutine(0xAF02, 'copy_arg_to_buf_x0', title='Copy argument to TX buffer from offset zero', description="""Sets X=0 and falls through to copy_arg_to_buf
then copy_arg_validated. Provides the simplest
entry point for copying a single parsed argument
into the TX buffer at position zero.""")


d.subroutine(0xAF04, 'copy_arg_to_buf', title='Copy argument to TX buffer with Y=0', description="""Sets Y=0 and falls through to copy_arg_validated
with carry set, enabling '&' character validation.
X must already contain the destination offset
within the TX buffer.""")


d.subroutine(0xAF06, 'copy_arg_validated', title='Copy command line characters to TX buffer', description="""Copies characters from (fs_crc_lo)+Y to l0f05+X
until a CR terminator is reached. With carry set,
validates each character against '&' — raising
'Bad file name' if found — to prevent FS selector
characters from being embedded in filenames.""", on_entry={'x': 'TX buffer destination offset', 'y': 'command line source offset', 'c': "set to enable '&' validation"})

d.label(0xAF2B, 'done_trim_spaces')


d.subroutine(0xAF32, 'mask_owner_access', title='Clear FS selection flags from options word', description="""ANDs the l1071 flags byte with &1F, clearing
the FS selection flag (bit 6) and other high
bits to retain only the 5-bit owner access
mask. Called before parsing to reset the prefix
state from a previous command.""")


d.subroutine(0xAF47, 'ex_print_col_sep', title='Print column separator or newline for *Ex/*Cat', description="""In *Cat mode, increments a column counter modulo 4
and prints a two-space separator between entries,
with a newline at the end of each row. In *Ex
mode (fs_spool_handle negative), prints a newline
after every entry. Scans the entry data and loops
back to print the next entry's characters.""")


d.subroutine(0xAF85, 'print_num_no_leading', title='Print decimal number with leading zero suppression', description="""Sets V via BIT bit_test_ff to enable leading
zero suppression, then falls through to
print_decimal_3dig. Used by print_station_id
for compact station number display.""", on_entry={'a': 'number to print (0-255)'})


d.subroutine(0xAF88, 'print_decimal_3dig', title='Print byte as 3-digit decimal via OSASCI', description="""Extracts hundreds, tens and units digits by
successive calls to print_decimal_digit. The V
flag controls leading zero suppression: if set,
zero digits are skipped until a non-zero digit
appears. V is always cleared before the units
digit to ensure at least one digit is printed.""", on_entry={'a': 'number to print (0-255)', 'v': 'set to suppress leading zeros'})


d.subroutine(0xAF96, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Initialises X to '0'-1 and loops, incrementing X
while subtracting the divisor from Y. On underflow,
adds back the divisor to get the remainder in Y.
If V is set, suppresses leading zeros by skipping
the OSASCI call when the digit is '0'.""", on_entry={'a': 'divisor', 'y': 'value to divide'}, on_exit={'y': 'remainder after division'})


d.subroutine(0xAFB5, 'save_ptr_to_os_text', title='Copy text pointer to OS text pointer workspace', description="""Saves fs_crc_lo/hi into the MOS text pointer
locations at &00F2/&00F3. Preserves A on the
stack. Called before GSINIT/GSREAD sequences
that need to parse from the current command
line position.""")


d.subroutine(0xAFC1, 'skip_to_next_arg', title='Advance past spaces to the next command argument', description="""Scans (fs_crc_lo)+Y for space characters,
advancing Y past each one. Returns with A
holding the first non-space character, or CR
if the end of line is reached. Used by *CDir
and *Remove to detect extra arguments.""", on_exit={'a': 'first non-space character or CR', 'y': 'offset of that character'})


d.subroutine(0xAFD5, 'save_ptr_to_spool_buf', title='Copy text pointer to spool buffer pointer', description="""Saves fs_crc_lo/hi into fs_options/fs_block_offset
for use as the spool buffer pointer. Preserves A
on the stack. Called by *PS and *PollPS before
parsing their arguments.""")


d.subroutine(0xAFE0, 'init_spool_drive', title='Initialise spool drive page pointers', description="""Calls get_ws_page to read the workspace page
number for the current ROM slot, stores it as
the spool drive page high byte (l00af), and
clears the low byte (l00ae) to zero. Preserves
Y on the stack.""")


d.subroutine(0xB017, 'copy_ps_data_y1c', title='Copy printer server template at offset &18', description="""Sets Y=&18 and falls through to copy_ps_data.
Called during workspace initialisation
(svc_2_private_workspace) to set up the printer
server template at the standard offset.""")


d.subroutine(0xB019, 'copy_ps_data', title='Copy 8-byte printer server template to RX buffer', description="""Copies 8 bytes of default printer server data
into the RX buffer at the current Y offset.
Uses indexed addressing: LDA ps_template_base,X
with X starting at &F8, so the effective read
address is ps_template_base+&F8 = ps_template_data
(&8E59). This 6502 trick reaches data 248 bytes
past the base label using a single instruction.""")

d.label(0xB083, 'read_ps_station_addr')

d.label(0xB0B9, 'store_ps_station_addr')


d.subroutine(0xB0C5, 'print_file_server_is', title="Print 'File server ' prefix", description="""Uses print_inline to output 'File' then falls through
to the shared ' server is ' suffix at
print_printer_server_is.""")


d.subroutine(0xB0CF, 'print_printer_server_is', title="Print 'Printer server is ' prefix", description="""Uses print_inline to output the full label
'Printer server is ' with trailing space.""")


d.subroutine(0xB0EA, 'load_ps_server_addr', title='Load printer server address from workspace', description="""Reads the station and network bytes from workspace
offsets 2 and 3 into the station/network variables.""")


d.subroutine(0xB0F6, 'pop_requeue_ps_scan', title='Pop return address and requeue PS slot scan', description="""Converts the PS slot flags to a workspace index,
writes slot data, and jumps back into the PS scan
loop to continue processing.""")


d.subroutine(0xB15E, 'write_ps_slot_byte_ff', title='Write buffer page byte and two &FF markers', description="""Stores the buffer page byte at the current Y offset
in workspace, followed by two &FF sentinel bytes.
Advances Y after each write.""")


d.subroutine(0xB165, 'write_two_bytes_inc_y', title='Write A to two consecutive workspace bytes', description="""Stores A at the current Y offset via (nfs_workspace),Y
then again at Y+1, advancing Y after each write.""", on_entry={'a': 'byte to store', 'y': 'workspace offset'})


d.subroutine(0xB16D, 'reverse_ps_name_to_tx', title='Reverse-copy printer server name to TX buffer', description="""Copies 8 bytes from the RX buffer (offsets &1C-&23)
to the TX buffer (offsets &13-&1B) in reversed byte
order, pushing onto the stack then popping back.""")


d.subroutine(0xB198, 'print_station_addr', title='Print station address as decimal net.station', description="""If the network number is zero, prints only the
station number. Otherwise prints network.station
separated by a dot. V flag controls padding with
leading spaces for column alignment.""")


d.subroutine(0xB2E0, 'init_ps_slot_from_rx', title='Initialise PS slot buffer from template data', description="""Copies the 12-byte ps_slot_txcb_template (&B1B7)
into workspace at offsets &78-&83 via indexed
addressing from write_ps_slot_link_addr (write_ps_slot_hi_link+1).
Substitutes net_rx_ptr_hi at offsets &7D and &81
(the hi bytes of the two buffer pointers) so they
point into the current RX buffer page.""")


d.subroutine(0xB2F7, 'store_char_uppercase', title='Convert to uppercase and store in RX buffer', description="""If the character in A is lowercase (&61-&7A), converts
to uppercase by clearing bit 5. Stores the result in
the RX buffer at the current position, advances the
buffer pointer, and decrements the character count.""", on_entry={'a': 'character to store'})


d.subroutine(0xB439, 'flush_and_read_char', title='Flush keyboard buffer and read one character', description="""Calls OSBYTE &0F to flush the input buffer, then
OSRDCH to read a single character. Raises an escape
error if escape was pressed (carry set on return).""")


d.subroutine(0xB449, 'init_channel_table', title='Initialise channel allocation table', description="""Clears all 256 bytes of the table, then marks
available channel slots based on the count from
the receive buffer. Sets the first slot to &C0
(active channel marker).""")


d.subroutine(0xB46B, 'attr_to_chan_index', title='Convert channel attribute to table index', description="""Subtracts &20 from the attribute byte and clamps
to the range 0-&0F. Returns &FF if out of range.
Preserves processor flags via PHP/PLP.""", on_entry={'a': 'channel attribute byte'}, on_exit={'a': 'table index (0-&0F) or &FF if invalid'})


d.subroutine(0xB47A, 'check_chan_char', title='Validate channel character and look up entry', description="""Characters below '0' are looked up directly in
the channel table. Characters '0' and above are
converted to a table index via attr_to_chan_index.
Raises 'Net channel' error if invalid.""", on_entry={'a': 'channel character'})


d.subroutine(0xB4AD, 'lookup_chan_by_char', title='Look up channel by character code', description="""Converts the character to a table index via
attr_to_chan_index, checks the station/network
match via match_station_net, and returns the
channel flags in A.""", on_entry={'a': 'channel character'}, on_exit={'a': 'channel flags'})


d.subroutine(0xB4EC, 'store_result_check_dir', title='Store channel attribute and check not directory', description="""Writes the current channel attribute to the receive
buffer, then tests the directory flag (bit 1). Raises
'Is a dir.' error if the attribute refers to a
directory rather than a file.""")


d.subroutine(0xB4F2, 'check_not_dir', title='Validate channel is not a directory', description="""Calls check_chan_char to validate the channel, then
tests the directory flag (bit 1). Raises 'Is a dir.'
error if the channel refers to a directory.""")


d.subroutine(0xB509, 'alloc_fcb_slot', title='Allocate a free file control block slot', description="""Scans FCB slots &20-&2F for an empty entry.
Returns Z=0 with X=slot index on success, or
Z=1 with A=0 if all slots are occupied.""", on_exit={'x': 'slot index (if Z=0)', 'z': '0=success, 1=no free slot'})


d.subroutine(0xB53D, 'alloc_fcb_or_error', title='Allocate FCB slot or raise error', description="""Calls alloc_fcb_slot and raises 'No more FCBs'
if no free slot is available. Preserves the
caller's argument on the stack.""")


d.subroutine(0xB559, 'close_all_net_chans', title='Close all network channels for current station', description="""Scans FCB slots &0F down to 0, closing those
matching the current station. C=0 closes all
matching entries; C=1 closes with write-flush.""", on_entry={'c': '0=close all, 1=close with write-flush'})


d.subroutine(0xB55D, 'scan_fcb_flags', title='Scan FCB slot flags from &10 downward', description="""Iterates through FCB slots starting at &10,
checking each slot's flags byte. Returns when
all slots have been processed.""")


d.subroutine(0xB586, 'match_station_net', title='Check FCB slot matches current station/network', description="""Compares the station and network numbers in the
FCB at slot X against the current values using
EOR. Returns Z=1 if both match, Z=0 if either
differs.""", on_entry={'x': 'FCB slot index'}, on_exit={'z': '1=match, 0=no match'})


d.subroutine(0xB595, 'find_open_fcb', title='Find next open FCB slot for current connection', description="""Scans from the current index, wrapping around at
the end. On the first pass finds active entries
matching the station; on the second pass finds
empty slots for new allocations.""")


d.subroutine(0xB5D8, 'init_wipe_counters', title='Initialise byte counters for wipe/transfer', description="""Clears the pass counter, byte counter, offset
counter, and transfer flag. Stores &FF sentinels
in l10cd/l10ce. Returns with X/Y pointing at
workspace offset &10CA.""", on_exit={'x': '&CA (workspace offset low)', 'y': '&10 (workspace page)'})


d.subroutine(0xB5FB, 'start_wipe_pass', title='Start wipe pass for current FCB', description="""Verifies the workspace checksum, saves the station
context (pushing station low/high), initialises
transfer counters via init_wipe_counters, and sends
the initial request via send_and_receive. Clears the
active and offset flags on completion.""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xB66A, 'save_fcb_context', title='Save FCB context and process pending slots', description="""Copies 13 bytes from the TX buffer (&0F00) and
fs_load_addr workspace to temporary storage at
&10D9. If Y=0, skips to the restore loop. Otherwise
scans for pending FCB slots (bits 7+6 set), flushes
each via start_wipe_pass, allocates new slots via
find_open_fcb, and sends directory requests. Falls
through to restore_catalog_entry.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xB721, 'restore_catalog_entry', title='Restore saved catalog entry to TX buffer', description="""Copies 13 bytes from the context buffer at &10D9
back to the TX buffer at &0F00. Falls through to
find_matching_fcb.""")


d.subroutine(0xB730, 'find_matching_fcb', title='Find FCB slot matching channel attribute', description="""Scans FCB slots 0-&0F for an active entry whose
attribute reference matches l10c9. Converts the
attribute to a channel index, then verifies the
station and network numbers. On the first scan
past slot &0F, saves context via save_fcb_context
and restarts. Returns Z=0 if the FCB has saved
offset data (bit 5 set).""", on_exit={'x': 'matching FCB index', 'z': '0=has offset data, 1=no offset'})


d.subroutine(0xB78B, 'inc_fcb_byte_count', title='Increment 3-byte FCB transfer count', description="""Increments l1000+X (low), cascading overflow to
l1010+X (mid) and l1020+X (high).""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xB799, 'process_all_fcbs', title='Process all active FCB slots', description="""Saves fs_options, fs_block_offset, and X/Y on the
stack, then scans FCB slots &0F down to 0. Calls
start_wipe_pass for each active entry matching the
filter attribute in Y (0=match all). Restores all
saved context on completion. Also contains the
OSBGET/OSBPUT inline logic for reading and writing
bytes through file channels.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xB8DA, 'flush_fcb_if_station_known', title='Flush FCB byte count to server if station is set', description="""Saves all registers, checks if the FCB has a
known station. If yes, sends the accumulated byte
count as a flush request to the file server. If no
station is set, falls through to flush_fcb_with_init
which saves FCB context first.""", on_entry={'Y': 'channel index (FCB slot)'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})


d.subroutine(0xB8E4, 'flush_fcb_with_init', title='Save FCB context and flush byte count to server', description="""Saves all registers and the current FCB context,
copies the FCB byte count into the TX command buffer,
and sends a flush/close request to the file server.
Restores the catalog entry and all registers on return.""", on_entry={'Y': 'channel index (FCB slot)'}, on_exit={'A': 'preserved', 'X': 'preserved', 'Y': 'preserved'})

d.label(0xB8F3, 'store_station_and_flush')


d.subroutine(0xB92B, 'send_wipe_request', title='Send wipe/close request packet', description="""Sets up the TX control block with function code
&90, the reply port from Y, and the data byte from
A. Sends via send_disconnect_reply, then checks the
error code — raises the server error if non-zero.""", on_entry={'a': 'data byte to send', 'y': 'reply port'})


d.subroutine(0xB984, 'send_and_receive', title='Set up FS options and transfer workspace', description="""Calls set_options_ptr to configure the FS options
pointer, then jumps to setup_transfer_workspace to
initialise the transfer and send the request.""", on_entry={'a': 'transfer mode', 'x': 'workspace offset low', 'y': 'workspace page'})


d.subroutine(0xB98A, 'read_rx_attribute', title='Read receive attribute byte from RX buffer', description="""Reads byte at offset &0A in the network receive
control block, used to track which channel owns the
current receive buffer.""", on_entry={}, on_exit={'A': 'receive attribute byte', 'Y': '&0A'})


d.subroutine(0xB98F, 'store_rx_attribute', title='Store receive attribute byte to RX buffer', description="""Writes A to offset &0A in the network receive
control block, marking which channel owns the
current receive buffer.""", on_entry={'A': 'attribute byte to store'}, on_exit={'Y': '&0A'})


d.subroutine(0xB9FF, 'abort_if_escape', title='Test escape flag and abort if pressed', description="""Checks the escape flag byte; returns immediately
if bit 7 is clear. If escape has been pressed,
falls through to the escape abort handler which
acknowledges the escape via OSBYTE &7E.""")


d.subroutine(0xBADD, 'print_dump_header', title='Print hex dump column header line', description="""Outputs the starting address followed by 16 hex
column numbers (00-0F), each separated by a space.
Provides the column alignment header for *Dump
output.""")


d.subroutine(0xBB03, 'print_hex_and_space', title='Print hex byte followed by space', description="""Saves A, prints it as a 2-digit hex value via
print_hex_byte, outputs a space character, then
restores A from the stack. Used by cmd_dump and
print_dump_header for column-aligned hex output.""", on_entry={'a': 'byte value to print'})


d.subroutine(0xBC3D, 'close_ws_file', title='Close file handle stored in workspace', description="""Loads the file handle from ws_page and closes it
via OSFIND with A=0.""")


d.subroutine(0xBC44, 'open_file_for_read', title='Open file for reading via OSFIND', description="""Computes the filename address from the command text
pointer plus the Y offset, calls OSFIND with A=&40
(open for input). Stores the handle in ws_page.
Raises 'Not found' if the returned handle is zero.""")

d.label(0xBC6A, 'restore_text_ptr')

d.label(0xBC84, 'done_skip_filename')


d.subroutine(0xBB0E, 'parse_dump_range', title='Parse hex address for dump range', description="""Reads up to 4 hex digits from the command line
into a 4-byte accumulator, stopping at CR or
space. Each digit shifts the accumulator left
by 4 bits before ORing in the new nybble.""")


d.subroutine(0xBB77, 'init_dump_buffer', title='Initialise dump buffer and parse address range', description="""Parses the start and end addresses from the command
line via parse_dump_range. If no end address is given,
defaults to the file extent. Validates both addresses
against the file size, raising 'Outside file' if either
exceeds the extent.""")


d.subroutine(0xBC86, 'advance_x_by_8', title='Advance X by 8 via nested JSR chain', description="""Calls advance_x_by_4 (which itself JSRs inx4 then
falls through to inx4), then falls through to inx4
for a total of 4+4=8 INX operations.""")


d.subroutine(0xBC89, 'advance_x_by_4', title='Advance X by 4 via JSR and fall-through', description="""JSRs to inx4 for 4 INX operations, then falls
through to inx4 for another 4 — but when called
directly (not from advance_x_by_8), the caller
returns after the first inx4, yielding X+4.""")


d.subroutine(0xBC8C, 'inx4', title='Increment X four times', description="""Four consecutive INX instructions. Used as a
building block by advance_x_by_4 and
advance_x_by_8 via JSR/fall-through chaining.""")

d.label(0x049B, 'send_next_rom_page')
d.comment(0x0016, 'A=&FF: signal error to co-processor via R4', align=Align.INLINE)
d.comment(0x0018, 'Send &FF error signal to Tube R4', align=Align.INLINE)
d.comment(0x001B, 'Flush any pending R2 byte', align=Align.INLINE)
d.comment(0x001E, 'A=0: send zero prefix to R2', align=Align.INLINE)
d.comment(0x0020, 'Send zero prefix byte via R2', align=Align.INLINE)
d.comment(0x0023, 'Y=0: start of error block at (&FD)', align=Align.INLINE)
d.comment(0x0024, 'Load error number from (&FD),0', align=Align.INLINE)
d.comment(0x0026, 'Send error number via R2', align=Align.INLINE)
d.comment(0x0029, 'Advance to next error string byte', align=Align.INLINE)
d.comment(0x002A, 'Load next error string byte', align=Align.INLINE)
d.comment(0x002C, 'Send error string byte via R2', align=Align.INLINE)
d.comment(0x002F, 'Zero byte = end of error string', align=Align.INLINE)
d.comment(0x0030, 'Loop until zero terminator sent', align=Align.INLINE)
d.comment(0x0032, 'Reset stack pointer to top', align=Align.INLINE)
d.comment(0x0034, 'TXS: set stack pointer from X', align=Align.INLINE)
d.comment(0x0035, 'Enable interrupts for main loop', align=Align.INLINE)
d.comment(0x0036, 'BIT R1 status: check WRCH request', align=Align.INLINE)
d.comment(0x0039, 'R1 not ready: check R2 instead', align=Align.INLINE)
d.comment(0x003B, 'Read character from Tube R1 data', align=Align.INLINE)
d.comment(0x0041, 'BIT R2 status: check command byte', align=Align.INLINE)
d.comment(0x0044, 'R2 not ready: loop back to R1 check', align=Align.INLINE)
d.comment(0x0046, 'Re-check R1: WRCH has priority over R2', align=Align.INLINE)
d.comment(0x0049, 'R1 ready: handle WRCH first', align=Align.INLINE)
d.comment(0x004B, 'Read command byte from Tube R2 data', align=Align.INLINE)
d.comment(0x004E, 'Self-modify JMP low byte for dispatch', align=Align.INLINE)
d.comment(0x0050, 'Dispatch to handler via indirect JMP', align=Align.INLINE)
d.comment(0x0053, 'Tube transfer address low byte', align=Align.INLINE)
d.comment(0x0054, 'Tube transfer page (default &80)', align=Align.INLINE)
d.comment(0x0055, 'Tube transfer address byte 2', align=Align.INLINE)
d.comment(0x0056, 'Tube transfer address byte 3', align=Align.INLINE)
d.comment(0x0400, 'JMP to BEGIN startup entry', align=Align.INLINE)
d.comment(0x0403, 'JMP to tube_escape_check (&06A7)', align=Align.INLINE)
d.comment(0x0406, 'A>=&80: address claim; A<&80: data transfer', align=Align.INLINE)
d.comment(0x0408, 'A<&80: data transfer setup (SENDW)', align=Align.INLINE)
d.comment(0x040A, 'A>=&C0: new address claim from another host', align=Align.INLINE)
d.comment(0x040C, 'C=1: external claim, check ownership', align=Align.INLINE)
d.comment(0x040E, 'Map &80-&BF range to &C0-&FF for comparison', align=Align.INLINE)
d.comment(0x0410, 'Is this for our currently-claimed address?', align=Align.INLINE)
d.comment(0x0412, 'Not our address: return', align=Align.INLINE)
d.comment(0x0414, 'PHP: save interrupt state for release', align=Align.INLINE)
d.comment(0x0415, 'SEI: disable interrupts during R4 protocol', align=Align.INLINE)
d.comment(0x0416, 'R4 cmd 5: release our address claim', align=Align.INLINE)
d.comment(0x0418, 'Send release command to co-processor', align=Align.INLINE)
d.comment(0x041B, 'Load our currently-claimed address', align=Align.INLINE)
d.comment(0x041D, 'Send our address as release parameter', align=Align.INLINE)
d.comment(0x0420, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x0421, '&80 sentinel: clear address claim', align=Align.INLINE)
d.comment(0x0423, '&80 sentinel = no address currently claimed', align=Align.INLINE)
d.comment(0x0425, 'Store to claim-in-progress flag', align=Align.INLINE)
d.comment(0x0427, 'Return from tube_post_init', align=Align.INLINE)
d.comment(0x0428, "Another host claiming; check if we're owner", align=Align.INLINE)
d.comment(0x042A, 'C=1: we have an active claim', align=Align.INLINE)
d.comment(0x042C, 'Compare with our claimed address', align=Align.INLINE)
d.comment(0x042E, 'Match: return (we already have it)', align=Align.INLINE)
d.comment(0x0430, "Not ours: CLC = we don't own this address", align=Align.INLINE)
d.comment(0x0431, 'Return with C=0 (claim denied)', align=Align.INLINE)
d.comment(0x0432, 'Accept new claim: update our address', align=Align.INLINE)
d.comment(0x0434, 'Return with address updated', align=Align.INLINE)
d.comment(0x0435, 'PHP: save interrupt state', align=Align.INLINE)
d.comment(0x0436, 'SEI: disable interrupts for R4 protocol', align=Align.INLINE)
d.comment(0x0437, 'Save 16-bit transfer address from (X,Y)', align=Align.INLINE)
d.comment(0x0439, 'Store address pointer low byte', align=Align.INLINE)
d.comment(0x043B, 'R4 byte 1 of 7: transfer type (A on entry)', align=Align.INLINE)
d.comment(0x043E, 'X = transfer type for tube_ctrl_values lookup', align=Align.INLINE)
d.comment(0x043F, 'Y=3: loop counter for 4 address bytes', align=Align.INLINE)
d.comment(0x0441, 'Load tube_claimed_id (Econet host ownership)', align=Align.INLINE)
d.comment(0x0443, 'R4 byte 2 of 7: claimed_id (Econet extension)', align=Align.INLINE)
d.comment(0x0446, 'Load address byte at offset Y (big-endian)', align=Align.INLINE)
d.comment(0x0448, 'R4 bytes 3-6 of 7: address Y=3,2,1,0', align=Align.INLINE)
d.comment(0x044B, 'Y--: next address byte (3->2->1->0)', align=Align.INLINE)
d.comment(0x044C, 'Y>=0: loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x044E, 'Y=&18: enable Tube control register', align=Align.INLINE)
d.comment(0x0450, 'Enable Tube interrupt generation', align=Align.INLINE)
d.comment(0x0453, 'Look up Tube control bits for this xfer type', align=Align.INLINE)
d.comment(0x0456, 'Apply transfer-specific control bits', align=Align.INLINE)
d.comment(0x0459, 'LSR 1: shift ctrl bit 1 into C (discarded)', align=Align.INLINE)
d.comment(0x045A, 'LSR 2: shift ctrl bit 2 into C (flush flag)', align=Align.INLINE)
d.comment(0x045B, 'C=0: not a P-to-H type (only 0/2 flush)', align=Align.INLINE)
d.comment(0x045D, 'Drain R3 FIFO byte 1 (stale data from last xfer)', align=Align.INLINE)
d.comment(0x0460, 'Drain R3 FIFO byte 2 (2-byte FIFO ready for fresh data)', align=Align.INLINE)
d.comment(0x0463, 'R4 byte 7 of 7: trigger/sync (post-LSR ctrl value)', align=Align.INLINE)
d.comment(0x0466, 'Poll R4 status for co-processor response', align=Align.INLINE)
d.comment(0x0469, 'Bit 6 clear: not ready, keep polling', align=Align.INLINE)
d.comment(0x046B, 'R4 bit 7: co-processor acknowledged transfer', align=Align.INLINE)
d.comment(0x046D, 'Type 4 = SENDW (host-to-parasite word xfer)', align=Align.INLINE)
d.comment(0x046F, 'Not SENDW type: skip release path', align=Align.INLINE)
d.comment(0x0471, 'SENDW complete: release, sync, restart', align=Align.INLINE)
d.comment(0x0474, 'Sync via R2 send', align=Align.INLINE)
d.comment(0x0477, 'Restart Tube main loop', align=Align.INLINE)
d.comment(0x047A, 'LSR: check bit 0 (NMI used?)', align=Align.INLINE)
d.comment(0x047B, 'C=0: NMI not used, skip NMI release', align=Align.INLINE)
d.comment(0x047D, 'Release Tube NMI (transfer used interrupts)', align=Align.INLINE)
d.comment(0x047F, 'Write &88 to Tube control to release NMI', align=Align.INLINE)
d.comment(0x0482, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x0483, 'Return from transfer setup', align=Align.INLINE)
d.comment(0x0484, 'BEGIN: enable interrupts for Tube host code', align=Align.INLINE)
d.comment(0x0485, 'C=1: hard break, claim addr &FF', align=Align.INLINE)
d.comment(0x0487, 'C=0, A!=0: re-init path', align=Align.INLINE)
d.comment(0x0489, 'Z=1 from C=0 path: just acknowledge', align=Align.INLINE)
d.comment(0x048C, 'Read last break type from OS workspace', align=Align.INLINE)
d.comment(0x048F, 'Soft break (X=0): re-init Tube and restart', align=Align.INLINE)
d.comment(0x0491, 'Claim address &FF (startup = highest prio)', align=Align.INLINE)
d.comment(0x0493, 'Request address claim from Tube system', align=Align.INLINE)
d.comment(0x0496, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x0498, 'Init reloc pointers from ROM header', align=Align.INLINE)
d.comment(0x049B, 'Save interrupt state', align=Align.INLINE)
d.comment(0x049D, 'R4 cmd 7: SENDW to send ROM to parasite', align=Align.INLINE)
d.comment(0x049C, 'Disable interrupts during ROM transfer', align=Align.INLINE)
d.comment(0x049F, 'Set up Tube for SENDW transfer', align=Align.INLINE)
d.comment(0x04A2, 'Y=0: start at beginning of page', align=Align.INLINE)
d.comment(0x04A4, 'Store to zero page pointer low byte', align=Align.INLINE)
d.comment(0x04A6, 'Send 256-byte page via R3, byte at a time', align=Align.INLINE)
d.comment(0x04A8, 'Write byte to Tube R3 data register', align=Align.INLINE)
d.comment(0x04AB, 'Timing delay: Tube data register needs NOPs', align=Align.INLINE)
d.comment(0x04AC, 'NOP delay (2)', align=Align.INLINE)
d.comment(0x04AD, 'NOP delay (3)', align=Align.INLINE)
d.comment(0x04AE, 'Next byte in page', align=Align.INLINE)
d.comment(0x04AF, 'Loop for all 256 bytes', align=Align.INLINE)
d.comment(0x04B1, 'Restore interrupt state after page sent', align=Align.INLINE)
d.comment(0x04B2, 'Increment 24-bit destination addr', align=Align.INLINE)
d.comment(0x04B4, 'No carry: skip higher bytes', align=Align.INLINE)
d.comment(0x04B6, 'Carry into second byte', align=Align.INLINE)
d.comment(0x04B8, 'No carry: skip third byte', align=Align.INLINE)
d.comment(0x04BA, 'Carry into third byte', align=Align.INLINE)
d.comment(0x04BC, 'Increment page counter', align=Align.INLINE)
d.comment(0x04BE, 'Bit 6 set = all pages transferred', align=Align.INLINE)
d.comment(0x04C0, 'More pages: loop back to SENDW', align=Align.INLINE)
d.comment(0x04C2, 'Re-init reloc pointers for final claim', align=Align.INLINE)
d.comment(0x04C5, 'A=4: transfer type for final address claim', align=Align.INLINE)
d.comment(0x04C7, 'Y=0: transfer address low byte', align=Align.INLINE)
d.comment(0x04C9, 'X=&53: transfer address high byte (&0053)', align=Align.INLINE)
d.comment(0x04CB, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x04CE, 'Init: start sending from &8000', align=Align.INLINE)
d.comment(0x04D0, 'Store &80 as source page high byte', align=Align.INLINE)
d.comment(0x04D2, 'Store &80 as page counter initial value', align=Align.INLINE)
d.comment(0x04D4, 'A=&20: bit 5 mask for ROM type check', align=Align.INLINE)
d.comment(0x04D6, 'ROM type bit 5: reloc address in header?', align=Align.INLINE)
d.comment(0x04D9, 'Y = 0 or &20 (reloc flag)', align=Align.INLINE)
d.comment(0x04DA, 'Store as transfer address selector', align=Align.INLINE)
d.comment(0x04DC, 'No reloc addr: use defaults', align=Align.INLINE)
d.comment(0x04DE, 'Skip past copyright string to find reloc addr', align=Align.INLINE)
d.comment(0x04E1, 'Skip past null-terminated copyright string', align=Align.INLINE)
d.comment(0x04E2, 'Load next byte from ROM header', align=Align.INLINE)
d.comment(0x04E5, 'Loop until null terminator found', align=Align.INLINE)
d.comment(0x04E7, 'Read 4-byte reloc address from ROM header', align=Align.INLINE)
d.comment(0x04EA, 'Store reloc addr byte 1 as transfer addr', align=Align.INLINE)
d.comment(0x04EC, 'Load reloc addr byte 2', align=Align.INLINE)
d.comment(0x04EF, 'Store as source page start', align=Align.INLINE)
d.comment(0x04F1, 'Load reloc addr byte 3', align=Align.INLINE)
d.comment(0x04F4, 'Load reloc addr byte 4 (highest)', align=Align.INLINE)
d.comment(0x04F7, 'Store high byte of end address', align=Align.INLINE)
d.comment(0x04F9, 'Store byte 3 of end address', align=Align.INLINE)
d.comment(0x04FB, 'Return with pointers initialised', align=Align.INLINE)
_tube_r2_entries = [(0x0500, 'tube_osrdch', 'R2 cmd 0: OSRDCH'), (0x0502, 'tube_oscli', 'R2 cmd 1: OSCLI'), (0x0504, 'tube_osbyte_2param', 'R2 cmd 2: OSBYTE (2-param)'), (0x0506, 'tube_osbyte_long', 'R2 cmd 3: OSBYTE (3-param)'), (0x0508, 'tube_osword', 'R2 cmd 4: OSWORD'), (0x050A, 'tube_osword_rdln', 'R2 cmd 5: OSWORD 0 (read line)'), (0x050C, 'tube_osargs', 'R2 cmd 6: OSARGS'), (0x050E, 'tube_osbget', 'R2 cmd 7: OSBGET'), (0x0510, 'tube_osbput', 'R2 cmd 8: OSBPUT'), (0x0512, 'tube_osfind', 'R2 cmd 9: OSFIND'), (0x0514, 'tube_osfile', 'R2 cmd 10: OSFILE'), (0x0516, 'tube_osgbpb', 'R2 cmd 11: OSGBPB')]
for addr, target_label, desc in _tube_r2_entries:
    d.word(addr)
    d.expr(addr, target_label)
    d.comment(addr, desc, align=Align.INLINE)
d.comment(0x0518, """Tube ULA control register values, indexed by transfer
type (0-7). Written to &FEE0 after clearing V+M with
&18. Bit layout: S=set/clear, T=reset regs, P=PRST,
V=2-byte R3, M=PNMI(R3), J=PIRQ(R4), I=PIRQ(R1),
Q=HIRQ(R4). Bits 1-7 select flags; bit 0 (S) is the
value to set or clear.""")
_tube_ctrl_entries = [(0x0518, 'Type 0: set I+J (1-byte R3, parasite to host)'), (0x0519, 'Type 1: set M (1-byte R3, host to parasite)'), (0x051A, 'Type 2: set V+I+J (2-byte R3, parasite to host)'), (0x051B, 'Type 3: set V+M (2-byte R3, host to parasite)'), (0x051C, 'Type 4: clear V+M (execute code at address)'), (0x051D, 'Type 5: clear V+M (release address claim)'), (0x051E, 'Type 6: set I (define event handler)'), (0x051F, 'Type 7: clear V+M (transfer and release)')]
for addr, desc in _tube_ctrl_entries:
    d.byte(addr)
    d.comment(addr, desc, align=Align.INLINE)
d.comment(0x0520, 'Read channel handle from R2 for BPUT', align=Align.INLINE)
d.comment(0x0523, 'Y=channel handle for OSBPUT', align=Align.INLINE)
d.comment(0x0524, 'Read data byte from R2 for OSBPUT', align=Align.INLINE)
d.comment(0x052A, 'Reply with &7F ack after OSBPUT', align=Align.INLINE)
d.comment(0x052D, 'Read channel handle from R2 for BGET', align=Align.INLINE)
d.comment(0x0534, 'Reply with carry+byte via RDCH protocol', align=Align.INLINE)
d.comment(0x053A, 'ROR A: encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x053B, 'Send carry+data byte to Tube R2', align=Align.INLINE)
d.comment(0x053E, 'ROL A: restore carry flag', align=Align.INLINE)
d.comment(0x053F, 'Return via tube_reply_byte', align=Align.INLINE)
d.comment(0x0542, 'Read open mode from R2 for OSFIND', align=Align.INLINE)
d.comment(0x0545, 'Mode=0: close file(s)', align=Align.INLINE)
d.comment(0x0547, 'Save open mode on stack', align=Align.INLINE)
d.comment(0x0548, 'Read filename string from R2', align=Align.INLINE)
d.comment(0x054B, 'Restore open mode', align=Align.INLINE)
d.comment(0x054F, 'Reply with file handle via R2', align=Align.INLINE)
d.comment(0x0552, 'OSFIND close: read handle from R2', align=Align.INLINE)
d.comment(0x0555, 'Transfer handle to Y', align=Align.INLINE)
d.comment(0x0556, 'A=0: close file', align=Align.INLINE)
d.comment(0x055B, 'Reply with acknowledgement via R2', align=Align.INLINE)
d.comment(0x055E, 'Read file handle from R2 for OSARGS', align=Align.INLINE)
d.comment(0x0561, 'Y=file handle for OSARGS', align=Align.INLINE)
d.comment(0x0562, 'Read 4-byte arg + reason from R2 into ZP', align=Align.INLINE)
d.comment(0x0564, 'Read next param byte from R2', align=Align.INLINE)
d.comment(0x0567, 'Store param at ZP+X (escape_flag downward)', align=Align.INLINE)
d.comment(0x0569, 'Decrement index', align=Align.INLINE)
d.comment(0x056A, 'More params: continue reading', align=Align.INLINE)
d.comment(0x056C, 'Read OSARGS reason code from R2', align=Align.INLINE)
d.comment(0x0572, 'Send result A via R2', align=Align.INLINE)
d.comment(0x0575, 'X=3: send 4 result bytes', align=Align.INLINE)
d.comment(0x0577, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x0579, 'Send result byte via R2', align=Align.INLINE)
d.comment(0x057C, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x057D, 'More bytes: continue sending', align=Align.INLINE)
d.comment(0x057F, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x0582, 'X=0: initialise string buffer index', align=Align.INLINE)
d.comment(0x0584, 'Y=0: initialise string offset', align=Align.INLINE)
d.comment(0x0586, 'Read next string byte from R2', align=Align.INLINE)
d.comment(0x0589, 'Store in string buffer at &0700+Y', align=Align.INLINE)
d.comment(0x058C, 'Advance string index', align=Align.INLINE)
d.comment(0x058D, 'Buffer full (256 bytes): done', align=Align.INLINE)
d.comment(0x058F, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x0591, 'Not CR: continue reading', align=Align.INLINE)
d.comment(0x0593, 'Y=7: set XY=&0700 for OSCLI/OSFIND', align=Align.INLINE)
d.comment(0x0595, 'Return with XY pointing to string buffer', align=Align.INLINE)
d.comment(0x0596, 'Read command string from R2 into &0700', align=Align.INLINE)
d.comment(0x0599, 'Execute command string via OSCLI', align=Align.INLINE)
d.comment(0x059C, '&7F = success acknowledgement', align=Align.INLINE)
d.comment(0x059E, 'Poll R2 status until ready', align=Align.INLINE)
d.comment(0x05A1, 'Bit 6 clear: not ready, loop', align=Align.INLINE)
d.comment(0x05A3, 'Write byte to R2 data register', align=Align.INLINE)
d.comment(0x05A6, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x05A9, 'Read 16-byte OSFILE control block from R2', align=Align.INLINE)
d.comment(0x05AB, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05AE, 'Store at ZP+X (control block)', align=Align.INLINE)
d.comment(0x05B0, 'Decrement index', align=Align.INLINE)
d.comment(0x05B1, 'More bytes: continue reading', align=Align.INLINE)
d.comment(0x05B3, 'Read filename string from R2', align=Align.INLINE)
d.comment(0x05B6, 'Set filename ptr low = 0', align=Align.INLINE)
d.comment(0x05B8, 'Set filename ptr high = &07', align=Align.INLINE)
d.comment(0x05BA, 'Y=0: OSFILE reason code index', align=Align.INLINE)
d.comment(0x05BC, 'Read OSFILE reason code from R2', align=Align.INLINE)
d.comment(0x05BF, 'Execute OSFILE', align=Align.INLINE)
d.comment(0x05C2, 'Send result A via R2', align=Align.INLINE)
d.comment(0x05C5, 'X=&10: send 16 result bytes', align=Align.INLINE)
d.comment(0x05C7, 'Load control block byte', align=Align.INLINE)
d.comment(0x05C9, 'Send control block byte via R2', align=Align.INLINE)
d.comment(0x05CC, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05CD, 'More bytes: continue sending', align=Align.INLINE)
d.comment(0x05D1, 'X=&0D: read 13-byte OSGBPB ctrl block', align=Align.INLINE)
d.comment(0x05D3, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05D6, 'Store at ZP+X (escape_flag downward)', align=Align.INLINE)
d.comment(0x05D8, 'Decrement index', align=Align.INLINE)
d.comment(0x05D9, 'More bytes: continue reading', align=Align.INLINE)
d.comment(0x05DB, 'Read OSGBPB reason code from R2', align=Align.INLINE)
d.comment(0x05DE, 'Y=0: OSGBPB direction/count', align=Align.INLINE)
d.comment(0x05E3, 'Save result A on stack', align=Align.INLINE)
d.comment(0x05E4, 'X=&0C: send 12 result bytes', align=Align.INLINE)
d.comment(0x05E6, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x05E8, 'Send result byte via R2', align=Align.INLINE)
d.comment(0x05EB, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05EC, 'More bytes: continue sending', align=Align.INLINE)
d.comment(0x05EE, 'Recover completion status from stack', align=Align.INLINE)
d.comment(0x05EF, 'Reply with RDCH-style result', align=Align.INLINE)
d.comment(0x05F2, 'Read X parameter from R2', align=Align.INLINE)
d.comment(0x05F5, 'Transfer to X register', align=Align.INLINE)
d.comment(0x05F6, 'Read A (OSBYTE function code) from R2', align=Align.INLINE)
d.comment(0x05F9, 'Execute OSBYTE A,X', align=Align.INLINE)
d.comment(0x05FC, 'Poll R2 status for result send', align=Align.INLINE)
d.comment(0x05FF, 'BVC: page 5/6 boundary straddle', align=Align.INLINE)
d.comment(0x0600, 'Send carry+status to co-processor via R2', align=Align.INLINE)
d.comment(0x0601, 'Send X result for 2-param OSBYTE', align=Align.INLINE)
d.comment(0x0604, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0607, 'Read X, Y, A from R2 for 3-param OSBYTE', align=Align.INLINE)
d.comment(0x060A, 'Save in X', align=Align.INLINE)
d.comment(0x060B, 'Read Y parameter from co-processor', align=Align.INLINE)
d.comment(0x060E, 'Save in Y', align=Align.INLINE)
d.comment(0x060F, 'Read A (OSBYTE function code)', align=Align.INLINE)
d.comment(0x0612, 'Execute OSBYTE A,X,Y', align=Align.INLINE)
d.comment(0x0615, 'Test for OSBYTE &9D (fast Tube BPUT)', align=Align.INLINE)
d.comment(0x0617, 'OSBYTE &9D (fast Tube BPUT): no result needed', align=Align.INLINE)
d.comment(0x0619, 'Encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x061A, 'Send carry+status byte via R2', align=Align.INLINE)
d.comment(0x061D, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x0620, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0622, 'Send Y result, then fall through to send X', align=Align.INLINE)
d.comment(0x0625, 'BVS always: jump to send X via R2', align=Align.INLINE)
d.comment(0x0627, 'Overlapping entry: &20 = JSR c06c5 (OSWORD)', align=Align.INLINE)
d.comment(0x062A, 'Save OSWORD number in Y', align=Align.INLINE)
d.comment(0x062B, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x062E, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0630, 'Read param block length from R2', align=Align.INLINE)
d.comment(0x0633, 'DEX: length 0 means no params to read', align=Align.INLINE)
d.comment(0x0634, 'No params (length=0): skip read loop', align=Align.INLINE)
d.comment(0x0636, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x0639, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x063B, 'Read param byte from R2', align=Align.INLINE)
d.comment(0x063E, 'Store param bytes into block at &0128', align=Align.INLINE)
d.comment(0x0641, 'Next param byte (descending)', align=Align.INLINE)
d.comment(0x0642, 'Loop until all params read', align=Align.INLINE)
d.comment(0x0644, 'Restore OSWORD number from Y', align=Align.INLINE)
d.comment(0x0645, 'XY=&0128: param block address for OSWORD', align=Align.INLINE)
d.comment(0x0647, 'Y=&01: param block at &0128', align=Align.INLINE)
d.comment(0x0649, 'Execute OSWORD with XY=&0128', align=Align.INLINE)
d.comment(0x064C, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x064F, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0651, 'Read result block length from R2', align=Align.INLINE)
d.comment(0x0654, 'Decrement result byte counter', align=Align.INLINE)
d.comment(0x0655, 'No results to send: return to main loop', align=Align.INLINE)
d.comment(0x0657, 'Send result block bytes from &0128 via R2', align=Align.INLINE)
d.comment(0x065A, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x065D, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x065F, 'Send result byte via R2', align=Align.INLINE)
d.comment(0x0662, 'Next result byte (descending)', align=Align.INLINE)
d.comment(0x0663, 'Loop until all results sent', align=Align.INLINE)
d.comment(0x0665, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0668, 'Read 5-byte OSWORD 0 control block from R2', align=Align.INLINE)
d.comment(0x066A, 'Read control block byte from R2', align=Align.INLINE)
d.comment(0x066D, 'Store in zero page params', align=Align.INLINE)
d.comment(0x066F, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x0670, 'Loop until all 5 bytes read', align=Align.INLINE)
d.comment(0x0672, 'X=0 after loop, A=0 for OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x0673, 'Y=0 for OSWORD 0', align=Align.INLINE)
d.comment(0x0675, 'A=0: OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x0676, 'Read input line from keyboard', align=Align.INLINE)
d.comment(0x0679, 'C=0: line read OK; C=1: escape pressed', align=Align.INLINE)
d.comment(0x067B, '&FF = escape/error signal to co-processor', align=Align.INLINE)
d.comment(0x067D, 'Escape: send &FF error to co-processor', align=Align.INLINE)
d.comment(0x0680, 'X=0: start of input buffer at &0700', align=Align.INLINE)
d.comment(0x0682, '&7F = line read successfully', align=Align.INLINE)
d.comment(0x0684, 'Send &7F (success) to co-processor', align=Align.INLINE)
d.comment(0x0687, 'Load char from input buffer', align=Align.INLINE)
d.comment(0x068A, 'Send char to co-processor', align=Align.INLINE)
d.comment(0x068D, 'Next character', align=Align.INLINE)
d.comment(0x068E, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x0690, 'Loop until CR terminator sent', align=Align.INLINE)
d.comment(0x0692, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0695, 'Poll R2 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x0698, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x069A, 'Write A to Tube R2 data register', align=Align.INLINE)
d.comment(0x069D, 'Return to caller', align=Align.INLINE)
d.comment(0x069E, 'Poll R4 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06A1, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06A3, 'Write A to Tube R4 data register', align=Align.INLINE)
d.comment(0x06A6, 'Return to caller', align=Align.INLINE)
d.comment(0x06A7, 'Check OS escape flag at &FF', align=Align.INLINE)
d.comment(0x06A9, 'SEC+ROR: put bit 7 of &FF into carry+bit 7', align=Align.INLINE)
d.comment(0x06AA, 'ROR: shift escape bit 7 to carry', align=Align.INLINE)
d.comment(0x06AB, 'Escape set: forward to co-processor via R1', align=Align.INLINE)
d.comment(0x06AD, 'EVNTV: forward event A, Y, X to co-processor', align=Align.INLINE)
d.comment(0x06AE, 'Send &00 prefix (event notification)', align=Align.INLINE)
d.comment(0x06B0, 'Send zero prefix via R1', align=Align.INLINE)
d.comment(0x06B3, 'Y value for event', align=Align.INLINE)
d.comment(0x06B4, 'Send Y via R1', align=Align.INLINE)
d.comment(0x06B7, 'X value for event', align=Align.INLINE)
d.comment(0x06B8, 'Send X via R1', align=Align.INLINE)
d.comment(0x06BB, 'Restore A (event type)', align=Align.INLINE)
d.comment(0x06BC, 'Poll R1 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06BF, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06C1, 'Write A to Tube R1 data register', align=Align.INLINE)
d.comment(0x06C4, 'Return to caller', align=Align.INLINE)
d.comment(0x06C5, 'Poll R2 status (bit 7 = ready)', align=Align.INLINE)
d.comment(0x06C8, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06CA, 'Read data byte from R2', align=Align.INLINE)
d.comment(0x06CD, 'Return with byte in A', align=Align.INLINE)
d.comment(0x06CE, 'Is byte &FE (VDU stream start)?', align=Align.INLINE)
d.comment(0x06D0, 'Below &FE: normal byte', align=Align.INLINE)
d.comment(0x06D2, '&FF: set up event/break vectors', align=Align.INLINE)
d.comment(0x06D4, '&FE: check Y parameter', align=Align.INLINE)
d.comment(0x06D6, 'Y=0: treat as normal byte', align=Align.INLINE)
d.comment(0x06D8, 'X=6: six extra pages', align=Align.INLINE)
d.comment(0x06DA, 'OSBYTE &14: explode char defs', align=Align.INLINE)
d.comment(0x06DF, 'Poll R1 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06E2, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06E4, 'Read byte from Tube R1', align=Align.INLINE)
d.comment(0x06E7, 'Zero: end of VDU stream', align=Align.INLINE)
d.comment(0x06EC, 'Loop back to read next R1 byte', align=Align.INLINE)
d.comment(0x06EF, 'EVNTV low byte (&AD)', align=Align.INLINE)
d.comment(0x06F1, 'Store in EVNTV vector low', align=Align.INLINE)
d.comment(0x06F4, 'EVNTV high byte (page 6)', align=Align.INLINE)
d.comment(0x06F6, 'Store in EVNTV vector high', align=Align.INLINE)
d.comment(0x06F9, 'BRKV low byte (&16)', align=Align.INLINE)
d.comment(0x06FB, 'Store in BRKV vector', align=Align.INLINE)
d.comment(0x06FE, 'A=0', align=Align.INLINE)
d.comment(0x8003, 'JMP service_handler', align=Align.INLINE)
d.comment(0x8006, 'ROM type: service + language', align=Align.INLINE)
d.comment(0x8019, 'Null terminator before copyright', align=Align.INLINE)
d.comment(0x8028, 'A=4: SR bit mask for IFR test', align=Align.INLINE)
d.comment(0x802A, 'Test IFR bit 2: SR complete', align=Align.INLINE)
d.comment(0x802D, 'SR set: shift register complete', align=Align.INLINE)
d.comment(0x802F, 'A=5: not our interrupt, pass on', align=Align.INLINE)
d.comment(0x8031, 'Return service code 5 to MOS', align=Align.INLINE)
d.comment(0x8032, 'Save X on stack', align=Align.INLINE)
d.comment(0x8033, 'Push saved X', align=Align.INLINE)
d.comment(0x8034, 'Save Y on stack', align=Align.INLINE)
d.comment(0x8035, 'Push saved Y', align=Align.INLINE)
d.comment(0x8036, 'Read ACR for shift register restore', align=Align.INLINE)
d.comment(0x8039, 'Clear SR mode bits (2-4)', align=Align.INLINE)
d.comment(0x803B, 'Restore saved SR mode from ws_0d64', align=Align.INLINE)
d.comment(0x803E, 'Write restored ACR to system VIA', align=Align.INLINE)
d.comment(0x8041, 'Read SR to clear shift register IRQ', align=Align.INLINE)
d.comment(0x8044, 'A=4: SR bit mask', align=Align.INLINE)
d.comment(0x8046, 'Clear SR interrupt flag in IFR', align=Align.INLINE)
d.comment(0x8049, 'Disable SR interrupt in IER', align=Align.INLINE)
d.comment(0x804C, 'Load TX operation type for dispatch', align=Align.INLINE)
d.comment(0x804F, 'Copy to A for sign test', align=Align.INLINE)
d.comment(0x8050, 'Bit 7 set: dispatch via table', align=Align.INLINE)
d.comment(0x8052, 'A=&FE: Econet receive event', align=Align.INLINE)
d.comment(0x8057, 'Fire event (enable: *FX52,150)', align=Align.INLINE)
d.comment(0x805A, 'Dispatch through event vector', align=Align.INLINE)
d.comment(0x8054, 'Call event vector handler', align=Align.INLINE)
d.comment(0x805D, 'Y >= &86: above dispatch range', align=Align.INLINE)
d.comment(0x805F, 'Out of range: skip protection', align=Align.INLINE)
d.comment(0x8061, 'Save current JSR protection mask', align=Align.INLINE)
d.comment(0x8064, 'Backup to saved_jsr_mask', align=Align.INLINE)
d.comment(0x8067, 'Set protection bits 2-4', align=Align.INLINE)
d.comment(0x8069, 'Apply protection during dispatch', align=Align.INLINE)
d.comment(0x806C, 'Push return addr high (&85)', align=Align.INLINE)
d.comment(0x806E, 'High byte on stack for RTS', align=Align.INLINE)
d.comment(0x806F, 'Load dispatch target low byte', align=Align.INLINE)
d.comment(0x8072, 'Low byte on stack for RTS', align=Align.INLINE)
d.comment(0x8073, "RTS = dispatch to PHA'd address", align=Align.INLINE)
d.comment(0x8074, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x8077, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x807A, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x807C, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x807E, 'Clear Econet init flag before setup', align=Align.INLINE)
d.comment(0x8087, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8089, 'X=&0C: NMI claim service', align=Align.INLINE)
d.comment(0x8081, 'Check Tube presence via OSBYTE &EA', align=Align.INLINE)
d.comment(0x8084, 'Store Tube presence flag from OSBYTE &EA', align=Align.INLINE)
d.comment(0x808B, 'Issue NMI claim service request', align=Align.INLINE)
d.comment(0x808E, 'Y=5: NMI claim service number', align=Align.INLINE)
d.comment(0x8090, 'Check if NMI service was claimed (Y changed)', align=Align.INLINE)
d.comment(0x8092, 'Service claimed by other ROM: skip init', align=Align.INLINE)
d.comment(0x8094, 'Copy 32 bytes of NMI shim from ROM to &0D00', align=Align.INLINE)
d.comment(0x8096, 'Read byte from NMI shim ROM source', align=Align.INLINE)
d.comment(0x8099, 'Write to NMI shim RAM at &0D00', align=Align.INLINE)
d.comment(0x809C, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x809D, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x809F, 'Patch current ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x80A1, 'Self-modifying code: ROM bank at &0D07', align=Align.INLINE)
d.comment(0x80A4, 'Clear source network (Y=0 from copy loop)', align=Align.INLINE)
d.comment(0x80A7, 'Clear Tube release flag', align=Align.INLINE)
d.comment(0x80A9, 'Clear TX operation type', align=Align.INLINE)
d.comment(0x80AC, 'Read station ID (and disable NMIs)', align=Align.INLINE)
d.comment(0x80AF, 'Set own station as TX source', align=Align.INLINE)
d.comment(0x80B2, '&80 = Econet initialised', align=Align.INLINE)
d.comment(0x80B4, 'Mark TX as complete (ready)', align=Align.INLINE)
d.comment(0x80B7, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x80BA, 'INTON: re-enable NMIs (&FE20 read side effect)', align=Align.INLINE)
d.comment(0x80BD, 'Return', align=Align.INLINE)
d.comment(0x80BE, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x80C0, 'BIT SR2: Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x80C3, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x80C5, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x80C8, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x80CB, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x80CD, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x80CF, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x80D1, 'Flag &40 = broadcast frame', align=Align.INLINE)
d.comment(0x80D3, 'Store broadcast flag in rx_src_net', align=Align.INLINE)
d.comment(0x80D6, 'Install nmi_rx_scout_net NMI handler', align=Align.INLINE)
d.comment(0x80D8, 'Install next handler and RTI', align=Align.INLINE)
d.comment(0x80DB, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x80DE, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x80E0, 'Read destination network byte', align=Align.INLINE)
d.comment(0x80E3, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x80E5, 'EOR &FF: test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x80E7, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x80E9, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x80EB, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x80EE, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x80F1, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x80F4, 'Store Y offset for scout data buffer', align=Align.INLINE)
d.comment(0x80F6, 'Install scout data handler (&8102)', align=Align.INLINE)
d.comment(0x80F8, 'High byte of scout data handler', align=Align.INLINE)
d.comment(0x80FA, 'Install scout data loop and RTI', align=Align.INLINE)
d.comment(0x80FD, 'Read SR2', align=Align.INLINE)
d.comment(0x8100, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x8102, 'Neither set -- clean end, discard frame', align=Align.INLINE)
d.comment(0x8104, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x8107, 'Discard and return to idle', align=Align.INLINE)
d.comment(0x810A, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x810D, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x810F, 'Read SR2', align=Align.INLINE)
d.comment(0x8112, 'No RDA -- error handler', align=Align.INLINE)
d.comment(0x8114, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x8117, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x811A, 'Advance buffer index', align=Align.INLINE)
d.comment(0x811B, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x811E, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x8120, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x8122, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x8125, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x8128, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x8129, 'Copied all 12 scout bytes?', align=Align.INLINE)
d.comment(0x812B, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x812D, 'Save final buffer offset', align=Align.INLINE)
d.comment(0x812F, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x8132, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x8134, 'SR2 = 0 -- RTI, wait for next NMI', align=Align.INLINE)
d.comment(0x8137, 'Save Y for next iteration', align=Align.INLINE)
d.comment(0x8139, 'Write CR1', align=Align.INLINE)
d.comment(0x813C, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x813E, 'Write CR2', align=Align.INLINE)
d.comment(0x8141, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x8143, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x8146, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x8148, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x814A, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x814D, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x8150, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x8152, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x8155, 'Set bit7 of need_release_tube flag', align=Align.INLINE)
d.comment(0x8156, 'Rotate C=1 into bit7: mark Tube release needed', align=Align.INLINE)
d.comment(0x8158, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x815B, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x815D, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x8160, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x8163, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x8165, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x8167, 'Write CR2: broadcast frame prep', align=Align.INLINE)
d.comment(0x816A, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x816D, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x816F, 'Start scanning port list at page &C0', align=Align.INLINE)
d.comment(0x8171, 'Y=0: start offset within each port slot', align=Align.INLINE)
d.comment(0x8173, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x8175, 'Store page high byte for slot scanning', align=Align.INLINE)
d.comment(0x8177, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x8179, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x817B, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x817D, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x817F, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x8181, 'Y=1: advance to port byte in slot', align=Align.INLINE)
d.comment(0x8182, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x8184, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x8186, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x8189, 'Port mismatch -- try next slot', align=Align.INLINE)
d.comment(0x818B, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x818C, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x818E, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x8190, 'Check if source station matches', align=Align.INLINE)
d.comment(0x8193, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x8195, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x8196, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x8198, 'Zero = accept any network', align=Align.INLINE)
d.comment(0x819A, 'Check if source network matches', align=Align.INLINE)
d.comment(0x819D, 'Network matches or zero = accept', align=Align.INLINE)
d.comment(0x819F, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x81A1, 'No NFS workspace -- try fallback path', align=Align.INLINE)
d.comment(0x81A3, 'Load current slot base address', align=Align.INLINE)
d.comment(0x81A5, 'CLC for 12-byte slot advance', align=Align.INLINE)
d.comment(0x81A6, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x81A8, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x81AA, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.comment(0x81AC, 'No match found -- discard frame', align=Align.INLINE)
d.comment(0x81AF, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x81B2, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x81B4, 'NFS workspace starts at offset 0 in page', align=Align.INLINE)
d.comment(0x81B6, 'NFS workspace high byte for port list', align=Align.INLINE)
d.comment(0x81B8, 'Scan NFS workspace port list', align=Align.INLINE)
d.comment(0x81BA, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x81BC, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x81BF, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x81C2, 'C=0: no Tube claimed -- discard', align=Align.INLINE)
d.comment(0x81C4, 'Check broadcast flag for ACK path', align=Align.INLINE)
d.comment(0x81C7, 'Not broadcast -- normal ACK path', align=Align.INLINE)
d.comment(0x81C9, 'Broadcast: different completion path', align=Align.INLINE)
d.comment(0x81CC, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x81CE, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x81D1, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x81D3, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x81D6, 'Install data_rx_setup at &81DD', align=Align.INLINE)
d.comment(0x81D8, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x81DA, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x81DD, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x81DF, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x81E2, 'Install nmi_data_rx at &81E7', align=Align.INLINE)
d.comment(0x81E4, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)
d.comment(0x81E7, 'A=1: AP mask for SR2 bit test', align=Align.INLINE)
d.comment(0x81E9, 'BIT SR2: test AP bit', align=Align.INLINE)
d.comment(0x81EC, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x81EE, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x81F1, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x81F4, 'Not for us: error path', align=Align.INLINE)
d.comment(0x81F6, 'Install net check handler at &81FB', align=Align.INLINE)
d.comment(0x81F8, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x81FB, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x81FE, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x8200, 'Read dest network byte', align=Align.INLINE)
d.comment(0x8203, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x8205, 'Install skip handler at &8211', align=Align.INLINE)
d.comment(0x8207, 'High byte of &8211 handler', align=Align.INLINE)
d.comment(0x8209, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x820C, 'Data ready: skip directly, no RTI', align=Align.INLINE)
d.comment(0x820E, 'Install handler and return via RTI', align=Align.INLINE)
d.comment(0x8211, 'Skip control and port bytes (already known from scout)', align=Align.INLINE)
d.comment(0x8214, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x8216, 'Discard control byte', align=Align.INLINE)
d.comment(0x8219, 'Discard port byte', align=Align.INLINE)
d.comment(0x821C, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x821E, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x8221, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x8223, 'Install bulk read at &8239', align=Align.INLINE)
d.comment(0x8225, 'High byte of &8239 handler', align=Align.INLINE)
d.comment(0x8227, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x822A, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x822C, 'No: install handler and RTI', align=Align.INLINE)
d.comment(0x822F, 'Tube: install Tube RX at &8296', align=Align.INLINE)
d.comment(0x8231, 'High byte of &8296 handler', align=Align.INLINE)
d.comment(0x8233, 'Install Tube handler and RTI', align=Align.INLINE)
d.comment(0x8236, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x8239, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x823B, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x823E, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x8241, 'Discard and return to idle listen', align=Align.INLINE)
d.comment(0x8244, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x8246, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x8249, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x824B, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x824E, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x8250, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8251, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x8253, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x8255, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x8257, 'No pages left: handle as complete', align=Align.INLINE)
d.comment(0x8259, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x825C, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x825E, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)
d.comment(0x8260, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x8263, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x8265, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8266, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8268, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x826A, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x826C, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x826E, 'No pages left: frame complete', align=Align.INLINE)
d.comment(0x8270, 'Read SR2 for next iteration', align=Align.INLINE)
d.comment(0x8273, 'SR2 non-zero: more data, loop back', align=Align.INLINE)
d.comment(0x8275, 'SR2=0: no more data yet, wait for NMI', align=Align.INLINE)
d.comment(0x8278, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x827A, 'Write CR2: disable PSE for bit testing', align=Align.INLINE)
d.comment(0x827D, 'CR2=&84: disable PSE for individual bit testing', align=Align.INLINE)
d.comment(0x827F, 'Write CR1: disable all interrupts', align=Align.INLINE)
d.comment(0x8282, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x8284, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x8286, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x8289, 'No FV -- error', align=Align.INLINE)
d.comment(0x828B, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x828D, 'Check if buffer space remains', align=Align.INLINE)
d.comment(0x828F, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x8291, 'FV+RDA: read and store last data byte', align=Align.INLINE)
d.comment(0x8294, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x8296, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x8298, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x829A, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x829C, 'Page boundary: advance buffer page', align=Align.INLINE)
d.comment(0x829E, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x82A1, 'Read SR2 for Tube data receive path', align=Align.INLINE)
d.comment(0x82A4, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x82A6, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x82A9, 'Check buffer limits and transfer size', align=Align.INLINE)
d.comment(0x82AC, 'Zero: buffer full, handle as error', align=Align.INLINE)
d.comment(0x82AE, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x82B1, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x82B4, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x82B7, 'Check limits after byte pair', align=Align.INLINE)
d.comment(0x82BA, 'Zero: Tube transfer complete', align=Align.INLINE)
d.comment(0x82BC, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x82BF, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x82C1, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x82C4, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x82C6, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x82C9, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x82CB, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x82CE, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x82D0, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x82D3, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x82D5, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x82D7, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x82D9, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x82DB, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x82DD, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x82DF, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x82E1, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x82E4, 'Save extra byte at &0D5D for later use', align=Align.INLINE)
d.comment(0x82E7, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x82E9, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x82EC, 'Store updated flags', align=Align.INLINE)
d.comment(0x82EF, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x82F2, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x82F4, 'Final ACK: call completion handler', align=Align.INLINE)
d.comment(0x82F7, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x82FA, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x82FC, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x82FF, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x8301, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x8304, 'Install saved next handler (&8396 for scout ACK)', align=Align.INLINE)
d.comment(0x8306, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x8308, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x830B, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x830E, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x8311, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x8314, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x8316, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x8319, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x831C, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x831F, 'Install handler at &8326 (write src addr)', align=Align.INLINE)
d.comment(0x8321, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x8323, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)
d.comment(0x8326, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x8329, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x832C, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x832E, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x8331, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x8333, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x8336, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x8339, 'bit7 set: start data TX phase', align=Align.INLINE)
d.comment(0x833B, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x833D, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x8340, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x8343, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x8346, 'Install next NMI handler', align=Align.INLINE)
d.comment(0x8349, 'Jump to start data TX phase', align=Align.INLINE)
d.comment(0x834C, 'Jump to error handler', align=Align.INLINE)
d.comment(0x834F, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x8351, 'BIT tx_flags: check data transfer bit', align=Align.INLINE)
d.comment(0x8354, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x8356, 'CLC: init carry for 4-byte add', align=Align.INLINE)
d.comment(0x8357, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x8358, 'Y=8: RXCB high pointer offset', align=Align.INLINE)
d.comment(0x835A, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x835C, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x835D, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x8360, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x8362, 'Next byte', align=Align.INLINE)
d.comment(0x8363, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x8364, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x8366, 'No: continue adding', align=Align.INLINE)
d.comment(0x8368, 'Discard final carry', align=Align.INLINE)
d.comment(0x8369, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x836B, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x836E, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x8370, 'Save X on stack', align=Align.INLINE)
d.comment(0x8371, 'Push X', align=Align.INLINE)
d.comment(0x8372, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x8374, 'CLC for address calculation', align=Align.INLINE)
d.comment(0x8375, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x8377, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x8378, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x837A, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x837C, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x837F, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x8382, 'Send to Tube via R3', align=Align.INLINE)
d.comment(0x8385, 'SEC: init carry for increment', align=Align.INLINE)
d.comment(0x8386, 'Y=8: start at high pointer', align=Align.INLINE)
d.comment(0x8388, 'A=0: add carry only (increment)', align=Align.INLINE)
d.comment(0x838A, 'Add carry to pointer byte', align=Align.INLINE)
d.comment(0x838C, 'Store back to RXCB', align=Align.INLINE)
d.comment(0x838E, 'Next byte', align=Align.INLINE)
d.comment(0x838F, 'Keep going while carry propagates', align=Align.INLINE)
d.comment(0x8391, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8392, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8393, 'A=&FF: return value (transfer done)', align=Align.INLINE)
d.comment(0x8395, 'Return', align=Align.INLINE)
d.comment(0x8396, 'Load received port byte', align=Align.INLINE)
d.comment(0x8399, 'Port != 0: data transfer frame', align=Align.INLINE)
d.comment(0x839B, 'Port=0: load control byte', align=Align.INLINE)
d.comment(0x839E, 'Ctrl = &82 (POKE)?', align=Align.INLINE)
d.comment(0x83A0, 'Yes: POKE also needs data transfer', align=Align.INLINE)
d.comment(0x83A2, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)
d.comment(0x83A5, 'Update buffer pointer and check for Tube', align=Align.INLINE)
d.comment(0x83A8, 'Transfer not done: skip buffer update', align=Align.INLINE)
d.comment(0x83AA, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x83AC, 'CLC for address add', align=Align.INLINE)
d.comment(0x83AD, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x83AF, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x83B1, 'Carry: increment buffer high byte', align=Align.INLINE)
d.comment(0x83B3, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x83B5, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x83B7, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x83B8, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x83BA, 'Store high byte to RXCB', align=Align.INLINE)
d.comment(0x83BC, 'Check port byte again', align=Align.INLINE)
d.comment(0x83BF, 'Port=0: immediate op, discard+listen', align=Align.INLINE)
d.comment(0x83C1, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x83C4, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x83C6, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x83C8, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x83C9, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x83CC, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x83CE, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x83CF, 'Load port byte', align=Align.INLINE)
d.comment(0x83D2, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x83D4, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x83D5, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x83D8, 'Set bit7: signals wait_net_tx_ack that reply arrived', align=Align.INLINE)
d.comment(0x83DA, 'Store to RXCB byte 0 (bit 7 set = complete)', align=Align.INLINE)
d.comment(0x83DC, 'Load callback event flags', align=Align.INLINE)
d.comment(0x83DF, 'Shift bit 0 into carry', align=Align.INLINE)
d.comment(0x83E0, 'Bit 0 clear: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83E2, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x83E2, 'Load RXCB workspace pointer low byte', align=Align.INLINE)
d.comment(0x83E4, 'Count slots', align=Align.INLINE)
d.comment(0x83E5, 'Subtract 12 bytes per RXCB slot', align=Align.INLINE)
d.comment(0x83E7, 'Loop until pointer exhausted', align=Align.INLINE)
d.comment(0x83E9, 'Adjust for off-by-one', align=Align.INLINE)
d.comment(0x83EA, 'Check slot index >= 3', align=Align.INLINE)
d.comment(0x83EC, 'Slot < 3: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83EE, 'Discard scout and reset listen state', align=Align.INLINE)
d.comment(0x83F1, 'Pass slot index as callback parameter', align=Align.INLINE)
d.comment(0x83F2, 'Jump to TX completion with slot index', align=Align.INLINE)
d.comment(0x83F5, 'Discard scout and reset RX listen', align=Align.INLINE)
d.comment(0x83F8, 'Reset ADLC and return to RX listen', align=Align.INLINE)
d.comment(0x83FB, 'A=&BE: low byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83FD, 'Y=&80: high byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83FF, 'Install nmi_rx_scout as NMI handler', align=Align.INLINE)
d.comment(0x8402, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x8404, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x8407, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x840A, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x840C, 'Release Tube claim before discarding', align=Align.INLINE)
d.comment(0x840F, 'Return', align=Align.INLINE)
d.comment(0x8410, 'Save X on stack', align=Align.INLINE)
d.comment(0x8411, 'Push X', align=Align.INLINE)
d.comment(0x8412, 'X=4: start at scout byte offset 4', align=Align.INLINE)
d.comment(0x8414, 'A=2: Tube transfer check mask', align=Align.INLINE)
d.comment(0x8416, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x8419, 'Tube active: use R3 write path', align=Align.INLINE)
d.comment(0x841B, 'Y = current buffer position', align=Align.INLINE)
d.comment(0x841D, 'Load scout data byte', align=Align.INLINE)
d.comment(0x8420, 'Store to port buffer', align=Align.INLINE)
d.comment(0x8422, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x8423, 'No page crossing', align=Align.INLINE)
d.comment(0x8425, 'Page crossing: inc buffer high byte', align=Align.INLINE)
d.comment(0x8427, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x8429, 'No pages left: overflow', align=Align.INLINE)
d.comment(0x842B, 'Next scout data byte', align=Align.INLINE)
d.comment(0x842C, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x842E, 'Done all scout data? (X reaches &0C)', align=Align.INLINE)
d.comment(0x8430, 'No: continue copying', align=Align.INLINE)
d.comment(0x8432, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8433, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8434, 'Jump to completion handler', align=Align.INLINE)
d.comment(0x8437, 'Tube path: load scout data byte', align=Align.INLINE)
d.comment(0x843A, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x843D, 'Increment buffer position counters', align=Align.INLINE)
d.comment(0x8440, 'Counter overflow: handle end of buffer', align=Align.INLINE)
d.comment(0x8442, 'Next scout data byte', align=Align.INLINE)
d.comment(0x8443, 'Done all scout data?', align=Align.INLINE)
d.comment(0x8445, 'No: continue Tube writes', align=Align.INLINE)
d.comment(0x8449, 'Check if Tube needs releasing', align=Align.INLINE)
d.comment(0x844B, 'Bit7 set: already released', align=Align.INLINE)
d.comment(0x844D, 'A=&82: Tube release claim type', align=Align.INLINE)
d.comment(0x844F, 'Release Tube address claim', align=Align.INLINE)
d.comment(0x8452, 'Clear release flag (LSR clears bit7)', align=Align.INLINE)
d.comment(0x8454, 'Return', align=Align.INLINE)
d.comment(0x8455, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x8458, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x845A, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x845C, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x845E, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x8460, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x8462, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x8464, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x8465, 'SEC for subtract', align=Align.INLINE)
d.comment(0x8466, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x8468, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x8469, 'Load protection mask from LSTAT', align=Align.INLINE)
d.comment(0x846C, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x846D, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x846E, 'Loop until bit aligned', align=Align.INLINE)
d.comment(0x8470, 'Bit set = operation disabled, discard', align=Align.INLINE)
d.comment(0x8472, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x8475, 'Hi byte: all handlers are in page &84', align=Align.INLINE)
d.comment(0x8477, 'Push hi byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8478, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x847B, 'Push handler low byte', align=Align.INLINE)
d.comment(0x847C, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0x847D, 'Increment port buffer length', align=Align.INLINE)
d.comment(0x847F, 'Check if scout data index reached 11', align=Align.INLINE)
d.comment(0x8481, 'Yes: loop back to continue reading', align=Align.INLINE)
d.comment(0x8483, 'Restore A from stack', align=Align.INLINE)
d.comment(0x8484, 'Transfer to X', align=Align.INLINE)
d.comment(0x8485, 'Jump to discard handler', align=Align.INLINE)
d.comment(0x8490, 'A=0: port buffer lo at page boundary', align=Align.INLINE)
d.comment(0x8492, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x8494, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x8496, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x8498, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x849A, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x849C, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x849E, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x84A0, 'Y=1: copy 2 bytes (1 down to 0)', align=Align.INLINE)
d.comment(0x84A2, 'Load remote address byte', align=Align.INLINE)
d.comment(0x84A5, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x84A8, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x84A9, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x84AB, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x84AE, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x84B0, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x84B2, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84B4, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x84B6, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x84B9, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x84BB, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x84BD, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x84BF, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x84C1, 'Buffer start lo = &25', align=Align.INLINE)
d.comment(0x84C3, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x84C5, 'Buffer hi = &7F (below screen)', align=Align.INLINE)
d.comment(0x84C7, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x84CB, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x84CD, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x84CF, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84D1, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x84D3, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x84D5, 'Store scout status', align=Align.INLINE)
d.comment(0x84D8, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x84DB, 'C=0: transfer not set up, discard', align=Align.INLINE)
d.comment(0x84DD, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x84E0, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x84E2, 'Store updated TX flags', align=Align.INLINE)
d.comment(0x84E5, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x84E7, 'Write CR1: enable TX interrupts', align=Align.INLINE)
d.comment(0x84EA, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x84EC, 'Write CR2 for TX setup', align=Align.INLINE)
d.comment(0x84EF, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x84F1, 'Y=&85: NMI handler high byte', align=Align.INLINE)
d.comment(0x84F3, 'Acknowledge and write TX dest', align=Align.INLINE)
d.comment(0x84F6, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x84F8, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x84F9, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x84FB, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x84FD, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x84FF, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x8501, 'Load requesting station number', align=Align.INLINE)
d.comment(0x8504, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x8507, 'Load requesting network number', align=Align.INLINE)
d.comment(0x850A, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x850C, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x850F, 'Save TX operation type for SR dispatch', align=Align.INLINE)
d.comment(0x8512, 'IER bit 2: disable SR interrupt', align=Align.INLINE)
d.comment(0x8514, 'Write IER to disable SR', align=Align.INLINE)
d.comment(0x8517, 'Read ACR for shift register config', align=Align.INLINE)
d.comment(0x851A, 'Isolate shift register mode bits (2-4)', align=Align.INLINE)
d.comment(0x851C, 'Save original SR mode for later restore', align=Align.INLINE)
d.comment(0x851F, 'Reload ACR for modification', align=Align.INLINE)
d.comment(0x8522, 'Clear SR mode bits (keep other bits)', align=Align.INLINE)
d.comment(0x8524, 'SR mode 2: shift in under φ2', align=Align.INLINE)
d.comment(0x8526, 'Apply new shift register mode', align=Align.INLINE)
d.comment(0x8529, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x852C, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x852F, 'Increment buffer length low byte', align=Align.INLINE)
d.comment(0x8531, 'No overflow: done', align=Align.INLINE)
d.comment(0x8533, 'Increment buffer length high byte', align=Align.INLINE)
d.comment(0x8535, 'No overflow: done', align=Align.INLINE)
d.comment(0x8537, 'Increment buffer pointer low byte', align=Align.INLINE)
d.comment(0x8539, 'No overflow: done', align=Align.INLINE)
d.comment(0x853B, 'Increment buffer pointer high byte', align=Align.INLINE)
d.comment(0x853D, 'Return', align=Align.INLINE)
d.comment(0x8543, 'Hi byte of tx_done_exit-1', align=Align.INLINE)
d.comment(0x8545, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x8546, 'Push lo of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x8548, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x8549, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)
d.comment(0x853E, """TX done dispatch table (lo bytes)

Low bytes of PHA/PHA/RTS dispatch targets for TX
operation types &83-&87. Read by the dispatch at
&8064 via LDA set_rx_buf_len_hi,Y (base &84BB
+ Y). High byte is always &85, so targets are
&85xx+1. Entries for Y < &83 read from preceding
code bytes and are not valid operation types.""")
d.comment(0x854C, 'X = remote address lo from l0d66', align=Align.INLINE)
d.comment(0x854F, 'A = remote address hi from l0d67', align=Align.INLINE)
d.comment(0x8552, 'Y = 8: Econet event number', align=Align.INLINE)
d.comment(0x8557, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x855A, 'X = remote address lo', align=Align.INLINE)
d.comment(0x855D, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x8560, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x8563, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x8566, 'A=&04: bit 2 mask for rx_flags', align=Align.INLINE)
d.comment(0x8568, 'Test if already halted', align=Align.INLINE)
d.comment(0x856B, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x856D, 'Set bit 2 in rx_flags', align=Align.INLINE)
d.comment(0x8570, 'Store halt flag', align=Align.INLINE)
d.comment(0x8573, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x8575, 'Enable interrupts during halt wait', align=Align.INLINE)
d.comment(0x8576, 'Test halt flag', align=Align.INLINE)
d.comment(0x8579, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x857D, 'Load current RX flags', align=Align.INLINE)
d.comment(0x8580, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x8582, 'Store updated flags', align=Align.INLINE)
d.comment(0x8585, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8586, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x8587, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8588, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8589, 'A=0: success status', align=Align.INLINE)
d.comment(0x858B, 'Return with A=0 (success)', align=Align.INLINE)
d.comment(0x858C, 'Save X on stack', align=Align.INLINE)
d.comment(0x858D, 'Push X', align=Align.INLINE)
d.comment(0x858E, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x8590, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x8592, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x8596, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x8598, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x859B, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x859D, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x859F, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x85A1, 'Bit7 clear: normal data transfer', align=Align.INLINE)
d.comment(0x85A4, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x85A7, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x85A8, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x85A9, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x85AB, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x85AE, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x85B0, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x85B2, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x85B4, 'SEC: init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x85B5, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x85B6, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)
d.comment(0x85B8, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x85BA, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x85BB, '(continued)', align=Align.INLINE)
d.comment(0x85BC, '(continued)', align=Align.INLINE)
d.comment(0x85BD, '(continued)', align=Align.INLINE)
d.comment(0x85BE, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x85BF, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x85C1, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x85C4, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x85C5, '(continued)', align=Align.INLINE)
d.comment(0x85C6, '(continued)', align=Align.INLINE)
d.comment(0x85C7, '(continued)', align=Align.INLINE)
d.comment(0x85C8, '(continued)', align=Align.INLINE)
d.comment(0x85C9, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x85CA, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x85CC, 'No: next byte pair', align=Align.INLINE)
d.comment(0x85CE, 'Discard final borrow', align=Align.INLINE)
d.comment(0x85CF, 'Ctrl < &81: not an immediate op', align=Align.INLINE)
d.comment(0x85D1, 'Below range: normal data transfer', align=Align.INLINE)
d.comment(0x85D3, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x85D5, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x85D7, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)
d.comment(0x85D9, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x85DB, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x85DE, 'Next byte', align=Align.INLINE)
d.comment(0x85DF, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x85E1, 'No: continue copying', align=Align.INLINE)
d.comment(0x85E3, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x85E5, 'BIT SR2: test if line is idle', align=Align.INLINE)
d.comment(0x85E8, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x85EA, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x85EC, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x85ED, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x85EF, 'Store scout frame length', align=Align.INLINE)
d.comment(0x85F2, 'A=0: init low byte of timeout counter', align=Align.INLINE)
d.comment(0x85F4, 'Save TX index', align=Align.INLINE)
d.comment(0x85F7, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x85F8, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x85F9, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x85FB, 'A=&04: INACTIVE bit mask for SR2 test', align=Align.INLINE)
d.comment(0x85FD, 'Save interrupt state', align=Align.INLINE)
d.comment(0x85FE, 'Disable interrupts for ADLC access', align=Align.INLINE)
d.comment(0x85FF, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x8602, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x8605, 'BIT SR2: Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x8608, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x860A, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x860D, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x860F, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x8612, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x8614, 'BIT SR1: tests CTS present', align=Align.INLINE)
d.comment(0x8617, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x8619, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x861C, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x861D, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x861E, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x8621, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8623, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x8626, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8628, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x862B, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x862F, 'Error &44: control byte out of valid range', align=Align.INLINE)
d.comment(0x8633, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x8635, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x8638, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x8639, 'Pop saved register', align=Align.INLINE)
d.comment(0x863A, 'Pop saved register', align=Align.INLINE)
d.comment(0x863B, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x863D, 'ALWAYS branch to shared error handler', align=Align.INLINE)
d.comment(0x863F, "Error &43 = 'No Clock'", align=Align.INLINE)
d.comment(0x8641, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x8643, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x8645, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x8647, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x864A, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x864B, 'Move to X register', align=Align.INLINE)
d.comment(0x864C, 'Return to TX caller', align=Align.INLINE)
d.comment(0x864D, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x8650, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x8652, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x8655, 'Install NMI handler at &86E0 (TX data handler)', align=Align.INLINE)
d.comment(0x8657, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x8659, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x865C, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x865F, 'Set need_release_tube flag (SEC/ROR = bit7)', align=Align.INLINE)
d.comment(0x8660, 'Rotate carry into bit 7 of flag', align=Align.INLINE)
d.comment(0x8662, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)
d.comment(0x8665, 'Load destination port number', align=Align.INLINE)
d.comment(0x8668, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x866A, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x866D, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x8670, 'Store operation flags', align=Align.INLINE)
d.comment(0x8673, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x8676, 'Store expected transfer length', align=Align.INLINE)
d.comment(0x8679, 'Push high byte of return address (&9C)', align=Align.INLINE)
d.comment(0x867B, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x867C, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x867F, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8680, 'RTS dispatches to control-byte handler', align=Align.INLINE)
d.comment(0x8681, """TX ctrl dispatch table (lo bytes)

Low bytes of PHA/PHA/RTS dispatch targets for TX
control byte types &81-&88. Read by the dispatch
at &867C via LDA intoff_disable_nmi_op,Y (base
intoff_test_inactive+1). High byte is always &86,
so targets are &86xx+1. Last entry dispatches to
tx_ctrl_machine_type at &867F, immediately after
the table.""")
d.comment(0x8689, 'scout_status=3 (machine type query)', align=Align.INLINE)
d.comment(0x868B, 'Skip address addition, store status', align=Align.INLINE)
d.comment(0x868D, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x8691, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)
d.comment(0x8693, 'Store scout status', align=Align.INLINE)
d.comment(0x8696, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x8697, 'Save carry on stack', align=Align.INLINE)
d.comment(0x8698, 'Y=&0C: start at offset 12', align=Align.INLINE)
d.comment(0x869A, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x869D, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x869E, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x86A0, 'Store updated address byte', align=Align.INLINE)
d.comment(0x86A3, 'Next byte', align=Align.INLINE)
d.comment(0x86A4, 'Save carry for next addition', align=Align.INLINE)
d.comment(0x86A5, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x86A7, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x86A9, 'Restore processor flags', align=Align.INLINE)
d.comment(0x86AA, 'Skip buffer setup if transfer size is zero', align=Align.INLINE)
d.comment(0x86AC, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x86AF, 'AND with dest network', align=Align.INLINE)
d.comment(0x86B2, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x86B4, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x86B6, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x86B8, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x86BB, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x86BD, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x86C0, 'Y=4: start of address data in TXCB', align=Align.INLINE)
d.comment(0x86C2, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x86C4, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x86C7, 'Next byte', align=Align.INLINE)
d.comment(0x86C8, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x86CA, 'No: continue copying', align=Align.INLINE)
d.comment(0x86CE, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x86D0, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x86D3, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x86D5, 'Store scout status', align=Align.INLINE)
d.comment(0x86D8, 'Copy TX block pointer to workspace ptr', align=Align.INLINE)
d.comment(0x86DA, 'Store low byte', align=Align.INLINE)
d.comment(0x86DC, 'Copy TX block pointer high byte', align=Align.INLINE)
d.comment(0x86DE, 'Store high byte', align=Align.INLINE)
d.comment(0x86E0, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x86E3, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x86E4, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x86E5, 'Second PLA', align=Align.INLINE)
d.comment(0x86E6, 'Third PLA', align=Align.INLINE)
d.comment(0x86E7, 'Fourth PLA', align=Align.INLINE)
d.comment(0x86E8, 'Restore X from A', align=Align.INLINE)
d.comment(0x86E9, 'Return to caller', align=Align.INLINE)
d.comment(0x86EA, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x86ED, 'BIT SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x86F0, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x86F2, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x86F5, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x86F8, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x86F9, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x86FC, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x86FD, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x8700, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x8703, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x8706, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x8708, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x870B, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x870D, 'RTI -- wait for next NMI', align=Align.INLINE)
d.comment(0x8710, 'Error &42', align=Align.INLINE)
d.comment(0x8714, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x8716, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x8719, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x871B, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x871E, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)
d.comment(0x871F, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x8720, 'Increment delay counter', align=Align.INLINE)
d.comment(0x8721, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x8723, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x8726, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x8728, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x872B, 'Install NMI handler at &8728 (TX completion)', align=Align.INLINE)
d.comment(0x872D, 'High byte of handler address', align=Align.INLINE)
d.comment(0x872F, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x8732, 'Jump to error handler', align=Align.INLINE)
d.comment(0x8734, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x8737, 'Test workspace flags', align=Align.INLINE)
d.comment(0x873A, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x873C, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x873F, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x8741, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x8744, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x8746, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)
d.comment(0x8749, 'Install RX reply handler at &8744', align=Align.INLINE)
d.comment(0x874B, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x874E, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x8750, 'BIT SR2: test AP (Address Present)', align=Align.INLINE)
d.comment(0x8753, 'No AP -- error', align=Align.INLINE)
d.comment(0x8755, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x8758, 'Compare to our station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x875B, 'Not our station -- error/reject', align=Align.INLINE)
d.comment(0x875D, 'Install next handler at &8758 (reply continuation)', align=Align.INLINE)
d.comment(0x875F, 'Install continuation handler', align=Align.INLINE)
d.comment(0x8762, 'Read RX byte (destination station)', align=Align.INLINE)
d.comment(0x8765, 'No RDA -- error', align=Align.INLINE)
d.comment(0x8767, 'Read destination network byte', align=Align.INLINE)
d.comment(0x876A, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x876C, 'Install next handler at &8779 (reply validation)', align=Align.INLINE)
d.comment(0x876E, 'BIT SR1: test IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x8771, 'IRQ set -- fall through to &8779 without RTI', align=Align.INLINE)
d.comment(0x8773, 'IRQ not set -- install handler and RTI', align=Align.INLINE)
d.comment(0x8776, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x8779, 'BIT SR2: test RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x877C, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x877E, 'Read source station', align=Align.INLINE)
d.comment(0x8781, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x8784, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x8786, 'Read source network', align=Align.INLINE)
d.comment(0x8789, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x878C, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x878E, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x8790, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x8793, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x8795, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x8797, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x879A, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x879C, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x879F, 'Install next handler at &8878 (four-way data phase) into &0D43/&0D44', align=Align.INLINE)
d.comment(0x87A1, 'High byte &88 of next handler address', align=Align.INLINE)
d.comment(0x87A3, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x87A6, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x87A9, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x87AC, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87AF, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87B1, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x87B4, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87B7, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87BA, 'Install handler at &87B7 (write src addr for scout ACK)', align=Align.INLINE)
d.comment(0x87BC, 'High byte &87 of handler address', align=Align.INLINE)
d.comment(0x87BE, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x87C1, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x87C4, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x87C7, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87C9, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x87CC, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x87CE, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x87D1, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x87D3, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x87D6, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x87D8, 'Install nmi_data_tx at &87EE', align=Align.INLINE)
d.comment(0x87DA, 'High byte of handler address', align=Align.INLINE)
d.comment(0x87DC, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87DF, 'Install nmi_imm_data at &8837', align=Align.INLINE)
d.comment(0x87E1, 'High byte of handler address', align=Align.INLINE)
d.comment(0x87E3, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87E6, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x87E8, 'No pages left: send final partial page', align=Align.INLINE)
d.comment(0x87EA, 'Load remaining byte count', align=Align.INLINE)
d.comment(0x87EC, 'Zero bytes left: skip to TDRA check', align=Align.INLINE)
d.comment(0x87EE, 'Load remaining byte count (alt entry)', align=Align.INLINE)
d.comment(0x87F0, 'Zero: loop back to top of handler', align=Align.INLINE)
d.comment(0x87F2, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87F5, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87F7, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x87F9, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x87FC, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x87FD, 'No page crossing', align=Align.INLINE)
d.comment(0x87FF, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x8801, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x8803, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x8805, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x8807, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x880A, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x880B, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x880D, 'No page crossing', align=Align.INLINE)
d.comment(0x880F, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x8811, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x8813, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x8815, 'BIT SR1: test IRQ (N=bit7) for tight loop', align=Align.INLINE)
d.comment(0x8818, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x881A, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x881D, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)
d.comment(0x881F, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x8822, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x8825, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x8827, 'Install discard_reset_listen at &83F5', align=Align.INLINE)
d.comment(0x8829, 'High byte of &83F5 handler', align=Align.INLINE)
d.comment(0x882B, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x882E, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x8831, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x8834, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x8837, 'Tube TX: BIT SR1 test TDRA', align=Align.INLINE)
d.comment(0x883A, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x883C, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x883F, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x8842, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x8844, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x8846, 'Carry into second byte', align=Align.INLINE)
d.comment(0x8848, 'No further carry', align=Align.INLINE)
d.comment(0x884A, 'Carry into third byte', align=Align.INLINE)
d.comment(0x884C, 'No further carry', align=Align.INLINE)
d.comment(0x884E, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x8850, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x8852, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x8855, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x8858, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x885A, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x885C, 'Carry into second byte', align=Align.INLINE)
d.comment(0x885E, 'No further carry', align=Align.INLINE)
d.comment(0x8860, 'Carry into third byte', align=Align.INLINE)
d.comment(0x8862, 'No further carry', align=Align.INLINE)
d.comment(0x8864, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x8866, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x8868, 'BIT SR1: test IRQ for tight loop', align=Align.INLINE)
d.comment(0x886B, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x886D, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x8870, 'TX error: check flags for path', align=Align.INLINE)
d.comment(0x8873, 'Bit7 clear: TX result = not listening', align=Align.INLINE)
d.comment(0x8875, 'Bit7 set: discard and return to listen', align=Align.INLINE)
d.comment(0x8878, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)
d.comment(0x887A, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x887D, 'Install nmi_final_ack handler', align=Align.INLINE)
d.comment(0x887F, 'High byte of handler address', align=Align.INLINE)
d.comment(0x8881, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x8884, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x8886, 'BIT SR2: test AP', align=Align.INLINE)
d.comment(0x8889, 'No AP -- error', align=Align.INLINE)
d.comment(0x888B, 'Read dest station', align=Align.INLINE)
d.comment(0x888E, 'Compare to our station (INTOFF side effect)', align=Align.INLINE)
d.comment(0x8891, 'Not our station -- error', align=Align.INLINE)
d.comment(0x8893, 'Install nmi_final_ack_net handler', align=Align.INLINE)
d.comment(0x8895, 'Install continuation handler', align=Align.INLINE)
d.comment(0x8898, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x889B, 'No RDA -- error', align=Align.INLINE)
d.comment(0x889D, 'Read dest network', align=Align.INLINE)
d.comment(0x88A0, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x88A2, 'Install nmi_final_ack_validate handler', align=Align.INLINE)
d.comment(0x88A4, 'BIT SR1: test IRQ -- more data ready?', align=Align.INLINE)
d.comment(0x88A7, 'IRQ set -- fall through to validate', align=Align.INLINE)
d.comment(0x88A9, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x88AC, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x88AF, 'No RDA -- error', align=Align.INLINE)
d.comment(0x88B1, 'Read source station', align=Align.INLINE)
d.comment(0x88B4, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x88B7, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88B9, 'Read source network', align=Align.INLINE)
d.comment(0x88BC, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x88BF, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88C1, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x88C4, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x88C6, 'Install data RX handler', align=Align.INLINE)
d.comment(0x88C9, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x88CB, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x88CE, 'No FV -- error', align=Align.INLINE)
d.comment(0x88D0, 'A=0: success result code', align=Align.INLINE)
d.comment(0x88D2, 'BEQ: always taken (A=0)', align=Align.INLINE)
d.comment(0x88D4, 'A=&41: not listening error code', align=Align.INLINE)
d.comment(0x88D6, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x88D8, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x88DA, '&80: completion flag for &0D3A', align=Align.INLINE)
d.comment(0x88DC, 'Signal TX complete', align=Align.INLINE)
d.comment(0x88DF, 'Full ADLC reset and return to idle listen', align=Align.INLINE)
d.comment(0x88E2, """Unreferenced dead data (16 bytes)

16 bytes between JMP discard_reset_rx (&88DF) and
tx_calc_transfer (&88F2). Unreachable as code (after
an unconditional JMP) and unreferenced as data. No
label, index, or indirect pointer targets any address
in the &88E2-&88F1 range. Likely unused remnant from
development.""")
d.comment(0x88E2, 'Dead data: &0E', align=Align.INLINE)
d.comment(0x88E3, 'Dead data: &0E', align=Align.INLINE)
d.comment(0x88E4, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88E5, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88E6, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88E7, 'Dead data: &06', align=Align.INLINE)
d.comment(0x88E8, 'Dead data: &06', align=Align.INLINE)
d.comment(0x88E9, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88EA, 'Dead data: &81', align=Align.INLINE)
d.comment(0x88EB, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88EC, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88ED, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88EE, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88EF, 'Dead data: &01', align=Align.INLINE)
d.comment(0x88F0, 'Dead data: &01', align=Align.INLINE)
d.comment(0x88F1, 'Dead data: &81', align=Align.INLINE)
d.comment(0x88F2, 'Y=7: offset to RXCB buffer addr byte 3', align=Align.INLINE)
d.comment(0x88F4, 'Read RXCB[7] (buffer addr high byte)', align=Align.INLINE)
d.comment(0x88F6, 'Compare to &FF', align=Align.INLINE)
d.comment(0x88F8, 'Not &FF: normal buffer, skip Tube check', align=Align.INLINE)
d.comment(0x88FB, 'Read RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x88FD, 'Check if addr byte 2 >= &FE (Tube range)', align=Align.INLINE)
d.comment(0x88FF, 'Tube/IO address: use fallback path', align=Align.INLINE)
d.comment(0x8901, 'Transmit in progress?', align=Align.INLINE)
d.comment(0x8904, 'No: fallback path', align=Align.INLINE)
d.comment(0x8906, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x8909, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x890B, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x890E, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x890F, 'Save carry on stack', align=Align.INLINE)
d.comment(0x8910, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x8912, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x8914, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x8915, '(continued)', align=Align.INLINE)
d.comment(0x8916, '(continued)', align=Align.INLINE)
d.comment(0x8917, '(continued)', align=Align.INLINE)
d.comment(0x8918, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x8919, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x891B, 'Store result byte', align=Align.INLINE)
d.comment(0x891E, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x891F, '(continued)', align=Align.INLINE)
d.comment(0x8920, '(continued)', align=Align.INLINE)
d.comment(0x8921, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x8922, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x8924, 'No: next byte pair', align=Align.INLINE)
d.comment(0x8926, 'Discard final borrow', align=Align.INLINE)
d.comment(0x8927, 'Save X', align=Align.INLINE)
d.comment(0x8928, 'Save X', align=Align.INLINE)
d.comment(0x8929, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x892B, 'CLC for base pointer addition', align=Align.INLINE)
d.comment(0x892C, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x892E, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x892F, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x8931, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x8933, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x8936, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x8938, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x893B, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x893E, 'Release Tube claim after reclaim', align=Align.INLINE)
d.comment(0x8941, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x8942, 'Restore X', align=Align.INLINE)
d.comment(0x8943, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8944, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x8945, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x8947, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x8949, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x894B, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x894C, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x894E, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x8950, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x8952, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x8954, 'Propagate borrow only', align=Align.INLINE)
d.comment(0x8956, 'Temp store of adjusted hi byte', align=Align.INLINE)
d.comment(0x8958, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x895A, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x895C, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x895E, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x8960, 'Load RXCB[9]', align=Align.INLINE)
d.comment(0x8962, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x8963, 'Subtract adjusted hi byte', align=Align.INLINE)
d.comment(0x8965, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x8967, 'Return with C=1', align=Align.INLINE)
d.comment(0x8968, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x8969, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x896B, 'Write CR1 to ADLC register 0', align=Align.INLINE)
d.comment(0x896E, 'CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding', align=Align.INLINE)
d.comment(0x8970, 'Write CR4 to ADLC register 3', align=Align.INLINE)
d.comment(0x8973, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)
d.comment(0x8975, 'Write CR3 to ADLC register 1', align=Align.INLINE)
d.comment(0x8978, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x897A, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x897D, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x897F, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x8982, 'Return; ADLC now in RX listen mode', align=Align.INLINE)
d.comment(0x8983, 'Check if Econet has been initialised', align=Align.INLINE)
d.comment(0x8986, 'Not initialised: skip to RX listen', align=Align.INLINE)
d.comment(0x8988, 'Read current NMI handler low byte', align=Align.INLINE)
d.comment(0x898B, 'Expected: &B3 (nmi_rx_scout low)', align=Align.INLINE)
d.comment(0x898D, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x898F, 'Read current NMI handler high byte', align=Align.INLINE)
d.comment(0x8992, 'Test if high byte = &80 (page of nmi_rx_scout)', align=Align.INLINE)
d.comment(0x8994, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x8996, 'INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x8999, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x899C, 'TX not in progress', align=Align.INLINE)
d.comment(0x899F, 'Econet not initialised', align=Align.INLINE)
d.comment(0x89A2, 'Y=5: service call workspace page', align=Align.INLINE)
d.comment(0x89A4, 'Set ADLC to RX listen mode', align=Align.INLINE)
d.comment(0x89A7, 'INTOFF: force /NMI high (IC97 flip-flop clear)', align=Align.INLINE)
d.comment(0x89AA, 'Save A', align=Align.INLINE)
d.comment(0x89AB, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x89AC, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x89AD, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x89AF, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x89B2, 'Jump to scout handler in ROM', align=Align.INLINE)
d.comment(0x89B5, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x89B8, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x89BB, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x89BD, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x89C0, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x89C1, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x89C2, 'Restore A from stack', align=Align.INLINE)
d.comment(0x89C3, 'INTON: guaranteed /NMI edge if ADLC IRQ asserted', align=Align.INLINE)
d.comment(0x89C6, 'Return from interrupt', align=Align.INLINE)
d.comment(0x89C7, """Unreferenced dead data (3 bytes)

3 bytes between the RTI at &89C6 (end of the NMI
shim ROM source) and svc_dispatch_lo at &89CA.
The init copy loop (Y=1..&20) copies &89A7-&89C6
to &0D00-&0D1F; these bytes are outside that range
and unreferenced. Likely unused development remnant.""")
d.comment(0x89C7, 'Dead data: &01', align=Align.INLINE)
d.comment(0x89C8, 'Dead data: &00', align=Align.INLINE)
d.comment(0x8A15, 'Save service call number', align=Align.INLINE)
d.comment(0x8A16, 'Is it service 15 (vectors claimed)?', align=Align.INLINE)
d.comment(0x8A18, 'No: skip vectors-claimed handling', align=Align.INLINE)
d.comment(0x8A1A, 'Save Y parameter', align=Align.INLINE)
d.comment(0x8A1B, 'Save Y on stack', align=Align.INLINE)
d.comment(0x8A1C, 'OSBYTE 0: read OS version', align=Align.INLINE)
d.comment(0x8A1E, 'X=1 to request version number', align=Align.INLINE)
d.comment(0x8A23, 'OS 1.20?', align=Align.INLINE)
d.comment(0x8A25, 'Yes: skip workspace setup', align=Align.INLINE)
d.comment(0x8A27, 'OS 2.00 (BBC B+)?', align=Align.INLINE)
d.comment(0x8A29, 'Yes: skip workspace setup', align=Align.INLINE)
d.comment(0x8A2B, 'Transfer OS version to A', align=Align.INLINE)
d.comment(0x8A2C, 'Save flags (Z set if OS 1.00)', align=Align.INLINE)
d.comment(0x8A2D, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8A2F, 'Restore flags', align=Align.INLINE)
d.comment(0x8A30, 'OS 1.00: skip INX', align=Align.INLINE)
d.comment(0x8A32, 'Adjust index for OS 3+ workspace', align=Align.INLINE)
d.comment(0x8A33, 'A=0', align=Align.INLINE)
d.comment(0x8A35, 'Clear workspace byte for this ROM', align=Align.INLINE)
d.comment(0x8A38, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8A3A, 'Restore Y parameter', align=Align.INLINE)
d.comment(0x8A3B, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8A3C, 'Restore service call number', align=Align.INLINE)
d.comment(0x8A3D, 'Check relocated code service dispatch', align=Align.INLINE)
d.comment(0x8A40, 'Save service call number', align=Align.INLINE)
d.comment(0x8A41, 'Service 1 (workspace claim)?', align=Align.INLINE)
d.comment(0x8A43, 'No: skip ADLC check', align=Align.INLINE)
d.comment(0x8A45, 'Read ADLC status register 1', align=Align.INLINE)
d.comment(0x8A48, 'Mask relevant status bits', align=Align.INLINE)
d.comment(0x8A4A, 'Non-zero: ADLC absent, set flag', align=Align.INLINE)
d.comment(0x8A4C, 'Read ADLC status register 2', align=Align.INLINE)
d.comment(0x8A4F, 'Mask relevant status bits', align=Align.INLINE)
d.comment(0x8A51, 'Zero: ADLC present, skip', align=Align.INLINE)
d.comment(0x8A53, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0x8A56, 'Set carry to mark ADLC absent', align=Align.INLINE)
d.comment(0x8A57, 'Rotate carry into bit 7 of slot flag', align=Align.INLINE)
d.comment(0x8A5A, 'Load ROM slot flag byte', align=Align.INLINE)
d.comment(0x8A5D, 'Shift bit 7 (ADLC absent) into carry', align=Align.INLINE)
d.comment(0x8A5E, 'Restore service call number', align=Align.INLINE)
d.comment(0x8A5F, 'ADLC present: continue dispatch', align=Align.INLINE)
d.comment(0x8A61, 'ADLC absent: decline service, return', align=Align.INLINE)
d.comment(0x8A62, 'Service 15 (vectors claimed)?', align=Align.INLINE)
d.comment(0x8A64, 'No: handle other services', align=Align.INLINE)
d.comment(0x8A66, 'Already initialised?', align=Align.INLINE)
d.comment(0x8A69, 'Yes: skip first-time init', align=Align.INLINE)
d.comment(0x8A6B, 'X=1 (mark as initialised)', align=Align.INLINE)
d.comment(0x8A6C, 'Set ROM present flag', align=Align.INLINE)
d.comment(0x8A6F, 'A=service call number; use as ROM counter', align=Align.INLINE)
d.comment(0x8A71, 'Point to ROM header copyright offset', align=Align.INLINE)
d.comment(0x8A73, 'Set high byte of OSRDSC pointer', align=Align.INLINE)
d.comment(0x8A75, 'Offset &0C: copyright string offset', align=Align.INLINE)
d.comment(0x8A77, 'Set low byte of OSRDSC pointer', align=Align.INLINE)
d.comment(0x8A79, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A7C, "First char 'N'?", align=Align.INLINE)
d.comment(0x8A7E, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A80, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A83, "Second char 'E'?", align=Align.INLINE)
d.comment(0x8A85, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A87, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A8A, "Third char 'T'?", align=Align.INLINE)
d.comment(0x8A8C, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A8E, 'X=ROM slot for indexed store', align=Align.INLINE)
d.comment(0x8A90, 'Load its slot flag byte', align=Align.INLINE)
d.comment(0x8A93, 'Set bit 7 to mark as NET ROM', align=Align.INLINE)
d.comment(0x8A95, 'Store updated flag', align=Align.INLINE)
d.comment(0x8A98, 'Previous ROM slot', align=Align.INLINE)
d.comment(0x8A9A, 'More ROMs to check: loop', align=Align.INLINE)
d.comment(0x8A9C, 'A=&0F: restore service call number', align=Align.INLINE)
d.comment(0x8AA0, 'Advance read pointer to next byte', align=Align.INLINE)
d.comment(0x8AA7, 'Transfer service number to X', align=Align.INLINE)
d.comment(0x8AA8, 'Save current service state', align=Align.INLINE)
d.comment(0x8AAA, 'Push old state', align=Align.INLINE)
d.comment(0x8AAB, 'Restore service number to A', align=Align.INLINE)
d.comment(0x8AAC, 'Store as current service state', align=Align.INLINE)
d.comment(0x8AAE, 'Service < 13?', align=Align.INLINE)
d.comment(0x8AB0, 'Yes: use as dispatch index directly', align=Align.INLINE)
d.comment(0x8AB2, 'Subtract 5 (map 13-17 to 8-12)', align=Align.INLINE)
d.comment(0x8AB4, 'Mapped value = 13? (original was 18)', align=Align.INLINE)
d.comment(0x8AB6, 'Yes: valid service 18 (FS select)', align=Align.INLINE)
d.comment(0x8AB8, 'Unknown service: set index to 0', align=Align.INLINE)
d.comment(0x8ABA, 'Transfer dispatch index to X', align=Align.INLINE)
d.comment(0x8ABB, 'Index 0: unhandled service, skip', align=Align.INLINE)
d.comment(0x8ABD, 'Save current workspace page', align=Align.INLINE)
d.comment(0x8ABF, 'Push old page', align=Align.INLINE)
d.comment(0x8AC0, 'Set workspace page from Y parameter', align=Align.INLINE)
d.comment(0x8AC2, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8AC3, 'Y=0 for dispatch offset', align=Align.INLINE)
d.comment(0x8AC5, 'Dispatch to service handler via table', align=Align.INLINE)
d.comment(0x8AC8, 'Restore old workspace page', align=Align.INLINE)
d.comment(0x8AC9, 'Store it back', align=Align.INLINE)
d.comment(0x8ACB, 'Get service state (return code)', align=Align.INLINE)
d.comment(0x8ACD, 'Restore old service state', align=Align.INLINE)
d.comment(0x8ACE, 'Store it back', align=Align.INLINE)
d.comment(0x8AD0, 'Transfer return code to A', align=Align.INLINE)
d.comment(0x8AD1, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8AD3, 'Return to MOS', align=Align.INLINE)
d.comment(0x8AD4, 'Offset 0 in receive block', align=Align.INLINE)
d.comment(0x8AD6, 'Load remote operation flag', align=Align.INLINE)
d.comment(0x8AD8, 'Zero: already off, skip to cleanup', align=Align.INLINE)
d.comment(0x8ADA, 'A=0', align=Align.INLINE)
d.comment(0x8ADD, 'Clear remote operation flag', align=Align.INLINE)
d.comment(0x8AE0, 'OSBYTE &C9: keyboard disable', align=Align.INLINE)
d.comment(0x8AE5, 'A=&0A: workspace init parameter', align=Align.INLINE)
d.comment(0x8AE7, 'Initialise workspace area', align=Align.INLINE)
d.comment(0x8AEA, 'Save X in workspace', align=Align.INLINE)
d.comment(0x8AEC, 'A=&CE: start of key range', align=Align.INLINE)
d.comment(0x8AEE, 'Restore X from workspace', align=Align.INLINE)
d.comment(0x8AF0, 'Y=&7F: OSBYTE scan parameter', align=Align.INLINE)
d.comment(0x8AF2, 'OSBYTE: scan keyboard', align=Align.INLINE)
d.comment(0x8AF5, 'Advance to next key code', align=Align.INLINE)
d.comment(0x8AF7, 'Reached &D0?', align=Align.INLINE)
d.comment(0x8AF9, 'No: loop back (scan &CE and &CF)', align=Align.INLINE)
d.comment(0x8AFB, 'A=0', align=Align.INLINE)
d.comment(0x8AFD, 'Clear service state', align=Align.INLINE)
d.comment(0x8AFF, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B01, 'Return', align=Align.INLINE)
d.comment(0x8B02, 'Save A', align=Align.INLINE)
d.comment(0x8B03, 'Copy OS text pointer low', align=Align.INLINE)
d.comment(0x8B05, 'to fs_crc_lo', align=Align.INLINE)
d.comment(0x8B07, 'Copy OS text pointer high', align=Align.INLINE)
d.comment(0x8B09, 'to fs_crc_hi', align=Align.INLINE)
d.comment(0x8B0B, 'Restore A', align=Align.INLINE)
d.comment(0x8B0C, 'Return', align=Align.INLINE)
d.comment(0x8B0D, 'Y=5 (Econet filing system)?', align=Align.INLINE)
d.comment(0x8B0F, 'No: not ours, return unclaimed', align=Align.INLINE)
d.comment(0x8B11, 'A=0: clear service state', align=Align.INLINE)
d.comment(0x8B15, 'Already selected?', align=Align.INLINE)
d.comment(0x8B13, 'Reset service processing state', align=Align.INLINE)
d.comment(0x8B18, 'Yes (bit 7 set): return unclaimed', align=Align.INLINE)
d.comment(0x8B1A, 'Get workspace page for this ROM slot', align=Align.INLINE)
d.comment(0x8B1D, 'Store as high byte of load address', align=Align.INLINE)
d.comment(0x8B1F, 'A=0', align=Align.INLINE)
d.comment(0x8B21, 'Clear low byte of load address', align=Align.INLINE)
d.comment(0x8B23, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8B24, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8B26, 'Add byte to running checksum', align=Align.INLINE)
d.comment(0x8B28, 'Decrement index', align=Align.INLINE)
d.comment(0x8B29, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8B2B, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8B2D, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x8B2F, 'Match: checksum valid', align=Align.INLINE)
d.comment(0x8B31, 'Mismatch: raise checksum error', align=Align.INLINE)
d.comment(0x8B34, 'Call FSCV with A=6 (new FS)', align=Align.INLINE)
d.comment(0x8B37, 'Y=9: end of FS context block', align=Align.INLINE)
d.comment(0x8B39, 'Load byte from receive block', align=Align.INLINE)
d.comment(0x8B3B, 'Store into FS workspace', align=Align.INLINE)
d.comment(0x8B3E, 'Decrement index', align=Align.INLINE)
d.comment(0x8B3F, 'Reached offset 1?', align=Align.INLINE)
d.comment(0x8B41, 'No: continue copying', align=Align.INLINE)
d.comment(0x8B43, 'Shift bit 7 of FS flags into carry', align=Align.INLINE)
d.comment(0x8B46, 'Clear carry', align=Align.INLINE)
d.comment(0x8B47, 'Clear bit 7 of FS flags', align=Align.INLINE)
d.comment(0x8B4A, 'Y=&0D: vector table size - 1', align=Align.INLINE)
d.comment(0x8B4C, 'Load FS vector address', align=Align.INLINE)
d.comment(0x8B4F, 'Store into FILEV vector table', align=Align.INLINE)
d.comment(0x8B52, 'Decrement index', align=Align.INLINE)
d.comment(0x8B53, 'Loop until all vectors installed', align=Align.INLINE)
d.comment(0x8B55, 'Initialise ADLC and NMI workspace', align=Align.INLINE)
d.comment(0x8B58, 'Y=&1B: extended vector offset', align=Align.INLINE)
d.comment(0x8B5A, 'X=7: two more vectors to set up', align=Align.INLINE)
d.comment(0x8B5C, 'Set up extended vectors', align=Align.INLINE)
d.comment(0x8B5F, 'A=0', align=Align.INLINE)
d.comment(0x8B61, 'Clear FS state byte', align=Align.INLINE)
d.comment(0x8B64, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B67, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B6A, 'Clear service state', align=Align.INLINE)
d.comment(0x8B6C, 'Clear receive attribute byte', align=Align.INLINE)
d.comment(0x8B6F, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B72, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8B75, 'Initialise FS state', align=Align.INLINE)
d.comment(0x8B78, 'Y=&77: workspace block size - 1', align=Align.INLINE)
d.comment(0x8B7A, 'Load byte from source workspace', align=Align.INLINE)
d.comment(0x8B7C, 'Store to page &10 shadow copy', align=Align.INLINE)
d.comment(0x8B7F, 'Decrement index', align=Align.INLINE)
d.comment(0x8B80, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8B82, 'A=&80: FS selected flag', align=Align.INLINE)
d.comment(0x8B84, 'Set bit 7 of FS flags', align=Align.INLINE)
d.comment(0x8B87, 'Store updated flags', align=Align.INLINE)
d.comment(0x8B8A, 'Issue service 15 (FS initialised)', align=Align.INLINE)
d.comment(0x8B8D, 'X=&4A: NFS command table offset', align=Align.INLINE)
d.comment(0x8B8F, 'Print help for NFS commands', align=Align.INLINE)
d.comment(0x8B92, 'X=0: utility command table offset', align=Align.INLINE)
d.comment(0x8B96, 'X=&4A: NFS command table offset', align=Align.INLINE)
d.comment(0x8B98, 'V clear: need to print header first', align=Align.INLINE)
d.comment(0x8B9A, 'Save X (table offset)', align=Align.INLINE)
d.comment(0x8B9B, 'Push it', align=Align.INLINE)
d.comment(0x8B9C, 'Save Y', align=Align.INLINE)
d.comment(0x8B9D, 'Push it', align=Align.INLINE)
d.comment(0x8B9E, 'Print version string header', align=Align.INLINE)
d.comment(0x8BA1, 'Restore Y', align=Align.INLINE)
d.comment(0x8BA2, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8BA3, 'Restore X', align=Align.INLINE)
d.comment(0x8BA4, 'Transfer to X', align=Align.INLINE)
d.comment(0x8BA5, 'Clear overflow flag', align=Align.INLINE)
d.comment(0x8BAB, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0x8BAC, 'Push it', align=Align.INLINE)
d.comment(0x8BAD, 'Save processor status', align=Align.INLINE)
d.comment(0x8BAE, 'Load byte from command table', align=Align.INLINE)
d.comment(0x8BB1, 'Bit 7 clear: valid entry, continue', align=Align.INLINE)
d.comment(0x8BB3, 'End of table: finish up', align=Align.INLINE)
d.comment(0x8BB6, 'Print two-space indent', align=Align.INLINE)
d.comment(0x8BBB, 'Y=9: max command name length', align=Align.INLINE)
d.comment(0x8BBD, 'Load first byte of command name', align=Align.INLINE)
d.comment(0x8BC3, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8BC4, 'Decrement padding counter', align=Align.INLINE)
d.comment(0x8BC5, 'Load next character', align=Align.INLINE)
d.comment(0x8BC8, 'Bit 7 clear: more chars, continue', align=Align.INLINE)
d.comment(0x8BCA, 'Pad with spaces', align=Align.INLINE)
d.comment(0x8BCF, 'Decrement remaining pad count', align=Align.INLINE)
d.comment(0x8BD0, 'More padding needed: loop', align=Align.INLINE)
d.comment(0x8BD2, 'Load syntax descriptor byte', align=Align.INLINE)
d.comment(0x8BD5, 'Mask to get syntax string index', align=Align.INLINE)
d.comment(0x8BD7, 'Index &0E: shared commands?', align=Align.INLINE)
d.comment(0x8BD9, 'Yes: handle shared commands list', align=Align.INLINE)
d.comment(0x8BDB, 'Use index as Y', align=Align.INLINE)
d.comment(0x8BDC, 'Look up syntax string offset', align=Align.INLINE)
d.comment(0x8BDF, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x8BE0, 'Advance to next character', align=Align.INLINE)
d.comment(0x8BE1, 'Load syntax string character', align=Align.INLINE)
d.comment(0x8BE4, 'Zero terminator: end of syntax', align=Align.INLINE)
d.comment(0x8BE6, 'Carriage return: line continuation', align=Align.INLINE)
d.comment(0x8BE8, 'No: print the character', align=Align.INLINE)
d.comment(0x8BEA, 'Handle line wrap in syntax output', align=Align.INLINE)
d.comment(0x8BED, 'Continue with next character', align=Align.INLINE)
d.comment(0x8BF3, 'Continue with next character', align=Align.INLINE)
d.comment(0x8BF6, 'Save table pointer', align=Align.INLINE)
d.comment(0x8BF7, 'Push it', align=Align.INLINE)
d.comment(0x8BF8, 'Print opening parenthesis', align=Align.INLINE)
d.comment(0x8BFC, 'Y=0: shared command counter', align=Align.INLINE)
d.comment(0x8BFE, 'X=&D3: shared command table start', align=Align.INLINE)
d.comment(0x8C00, 'Load byte from shared command table', align=Align.INLINE)
d.comment(0x8C03, 'Bit 7 set: end of shared commands', align=Align.INLINE)
d.comment(0x8C05, 'Back up one position', align=Align.INLINE)
d.comment(0x8C06, 'Advance to next character', align=Align.INLINE)
d.comment(0x8C07, 'Load command name character', align=Align.INLINE)
d.comment(0x8C0A, 'Bit 7 set: end of this name', align=Align.INLINE)
d.comment(0x8C0F, 'Print more characters of name', align=Align.INLINE)
d.comment(0x8C12, 'Strip bit 7 from final character', align=Align.INLINE)
d.comment(0x8C17, 'Count this shared command', align=Align.INLINE)
d.comment(0x8C18, 'Printed 4 commands?', align=Align.INLINE)
d.comment(0x8C1A, 'No: continue on same line', align=Align.INLINE)
d.comment(0x8C1C, 'Handle line wrap after 4 commands', align=Align.INLINE)
d.comment(0x8C1F, 'X += 3: skip syntax descriptor and address', align=Align.INLINE)
d.comment(0x8C20, '(continued)', align=Align.INLINE)
d.comment(0x8C21, '(continued)', align=Align.INLINE)
d.comment(0x8C22, 'Loop for more shared commands', align=Align.INLINE)
d.comment(0x8C24, 'Restore original table pointer', align=Align.INLINE)
d.comment(0x8C25, 'Transfer to X', align=Align.INLINE)
d.comment(0x8C29, 'X += 3: skip syntax descriptor and address', align=Align.INLINE)
d.comment(0x8C2A, '(continued)', align=Align.INLINE)
d.comment(0x8C2B, '(continued)', align=Align.INLINE)
d.comment(0x8C2C, 'Loop for next command', align=Align.INLINE)
d.comment(0x8C2F, 'Restore processor status', align=Align.INLINE)
d.comment(0x8C30, 'Restore Y', align=Align.INLINE)
d.comment(0x8C31, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8C32, 'Return', align=Align.INLINE)
d.comment(0x8C33, 'Read output stream type', align=Align.INLINE)
d.comment(0x8C36, 'Stream 0 (VDU): no wrapping', align=Align.INLINE)
d.comment(0x8C38, 'Stream 3 (printer)?', align=Align.INLINE)
d.comment(0x8C3A, 'Yes: no wrapping', align=Align.INLINE)
d.comment(0x8C3C, 'Save Y', align=Align.INLINE)
d.comment(0x8C3D, 'Push it', align=Align.INLINE)
d.comment(0x8C41, 'Y=&0B: indent width - 1', align=Align.INLINE)
d.comment(0x8C43, 'Space character', align=Align.INLINE)
d.comment(0x8C48, 'Decrement indent counter', align=Align.INLINE)
d.comment(0x8C49, 'More spaces needed: loop', align=Align.INLINE)
d.comment(0x8C4B, 'Restore Y', align=Align.INLINE)
d.comment(0x8C4C, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8C4D, 'Return', align=Align.INLINE)
d.comment(0x8C4E, 'X=0: start of utility command table', align=Align.INLINE)
d.comment(0x8C50, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C52, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C55, 'Try to match command in table', align=Align.INLINE)
d.comment(0x8C58, 'No match: return to caller', align=Align.INLINE)
d.comment(0x8C5A, 'Match found: execute command', align=Align.INLINE)
d.comment(0x8C5D, 'Check for credits Easter egg', align=Align.INLINE)
d.comment(0x8C60, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C62, 'Load character at offset', align=Align.INLINE)
d.comment(0x8C64, 'Is it CR (bare *HELP)?', align=Align.INLINE)
d.comment(0x8C66, 'No: check for specific topic', align=Align.INLINE)
d.comment(0x8C68, 'Print version string', align=Align.INLINE)
d.comment(0x8C6B, 'X=&C4: start of help command list', align=Align.INLINE)
d.comment(0x8C6D, 'Print command list from table', align=Align.INLINE)
d.comment(0x8C70, 'Restore Y (command line offset)', align=Align.INLINE)
d.comment(0x8C72, 'Return unclaimed', align=Align.INLINE)
d.comment(0x8C73, 'Test for topic match (sets flags)', align=Align.INLINE)
d.comment(0x8C76, "Is first char '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C78, 'No: try topic-specific help', align=Align.INLINE)
d.comment(0x8C7A, "'.' found: show full command list", align=Align.INLINE)
d.comment(0x8C7D, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C80, 'Save flags', align=Align.INLINE)
d.comment(0x8C81, 'X=&C4: help command table start', align=Align.INLINE)
d.comment(0x8C83, 'Try to match help topic in table', align=Align.INLINE)
d.comment(0x8C86, 'No match: try next topic', align=Align.INLINE)
d.comment(0x8C88, 'Restore flags', align=Align.INLINE)
d.comment(0x8C89, 'Push return address high (&8C)', align=Align.INLINE)
d.comment(0x8C8B, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C8C, 'Push return address low (&74)', align=Align.INLINE)
d.comment(0x8C8E, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C8F, 'Load dispatch address high', align=Align.INLINE)
d.comment(0x8C92, 'Push dispatch high for RTS', align=Align.INLINE)
d.comment(0x8C93, 'Load dispatch address low', align=Align.INLINE)
d.comment(0x8C96, 'Push dispatch low for RTS', align=Align.INLINE)
d.comment(0x8C97, 'Dispatch via RTS (returns to &8C80)', align=Align.INLINE)
d.comment(0x8C98, 'Restore flags from before match', align=Align.INLINE)
d.comment(0x8C99, 'End of command line?', align=Align.INLINE)
d.comment(0x8C9B, 'No: try matching next topic', align=Align.INLINE)
d.comment(0x8C9F, 'Print version string via inline', align=Align.INLINE)
d.comment(0x8CB5, 'NOP (string terminator)', align=Align.INLINE)
d.comment(0x8CB6, 'Print station number after version', align=Align.INLINE)
d.comment(0x8CB9, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8CBB, 'Load workspace page for this slot', align=Align.INLINE)
d.comment(0x8CBE, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8CBF, 'Return with page in A and Y', align=Align.INLINE)
d.comment(0x8CC0, 'Get workspace page for ROM slot', align=Align.INLINE)
d.comment(0x8CC3, 'Store page in nfs_temp', align=Align.INLINE)
d.comment(0x8CC5, 'A=0', align=Align.INLINE)
d.comment(0x8CC7, 'Clear low byte of pointer', align=Align.INLINE)
d.comment(0x8CC9, 'Return', align=Align.INLINE)
d.comment(0x8CCA, 'OSBYTE &7A: scan keyboard from key 16', align=Align.INLINE)
d.comment(0x8CD0, 'No key pressed: select Net FS', align=Align.INLINE)
d.comment(0x8CD2, 'Key &19 (N)?', align=Align.INLINE)
d.comment(0x8CD4, 'Yes: write key state and boot', align=Align.INLINE)
d.comment(0x8CD6, "EOR with &55: maps to zero if 'N'", align=Align.INLINE)
d.comment(0x8CD8, 'Not N key: return unclaimed', align=Align.INLINE)
d.comment(0x8CDB, 'OSBYTE &78: write keys pressed', align=Align.INLINE)
d.comment(0x8CE0, 'Select NFS as current filing system', align=Align.INLINE)
d.comment(0x8CE3, 'Print station number', align=Align.INLINE)
d.comment(0x8CE9, 'Get workspace page', align=Align.INLINE)
d.comment(0x8CEB, 'Non-zero: already initialised, return', align=Align.INLINE)
d.comment(0x8CED, 'Load boot flags', align=Align.INLINE)
d.comment(0x8CF0, 'Set bit 2 (auto-boot in progress)', align=Align.INLINE)
d.comment(0x8CF2, 'Store updated boot flags', align=Align.INLINE)
d.comment(0x8CF5, 'X=&0F: boot filename address low', align=Align.INLINE)
d.comment(0x8CF7, 'Y=&8D: boot filename address high', align=Align.INLINE)
d.comment(0x8CF9, 'Execute boot file', align=Align.INLINE)
d.comment(0x8CFC, 'A=6: notify new filing system', align=Align.INLINE)
d.comment(0x8CFE, 'Call FSCV', align=Align.INLINE)
d.comment(0x8D01, 'X=&0A: service 10 parameter', align=Align.INLINE)
d.comment(0x8D05, 'Dispatch via FSCV', align=Align.INLINE)
d.comment(0x8D08, 'X=&0F: service 15 parameter', align=Align.INLINE)
d.comment(0x8D0A, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8D17, 'Get command line offset', align=Align.INLINE)
d.comment(0x8D19, 'X=5: start of credits keyword', align=Align.INLINE)
d.comment(0x8D1B, 'Load character from command line', align=Align.INLINE)
d.comment(0x8D1D, 'Compare with credits keyword', align=Align.INLINE)
d.comment(0x8D20, 'Mismatch: check if keyword complete', align=Align.INLINE)
d.comment(0x8D22, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x8D23, 'Advance keyword pointer', align=Align.INLINE)
d.comment(0x8D24, 'Continue matching', align=Align.INLINE)
d.comment(0x8D26, 'Reached end of keyword (X=&0D)?', align=Align.INLINE)
d.comment(0x8D28, 'No: keyword not fully matched, return', align=Align.INLINE)
d.comment(0x8D2A, 'X=0: start of credits text', align=Align.INLINE)
d.comment(0x8D2C, 'Load character from credits string', align=Align.INLINE)
d.comment(0x8D2F, 'Zero terminator: done printing', align=Align.INLINE)
d.comment(0x8D34, 'Advance string pointer', align=Align.INLINE)
d.comment(0x8D35, 'Continue printing', align=Align.INLINE)
d.comment(0x8D37, 'Return', align=Align.INLINE)
d.comment(0x8D79, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0x8D7A, 'Push it', align=Align.INLINE)
d.comment(0x8D7B, 'OSBYTE &77: close SPOOL/EXEC', align=Align.INLINE)
d.comment(0x8D7D, 'Store as pending operation marker', align=Align.INLINE)
d.comment(0x8D83, 'Y=0', align=Align.INLINE)
d.comment(0x8D85, 'Clear password entry flag', align=Align.INLINE)
d.comment(0x8D87, 'Reset FS connection state', align=Align.INLINE)
d.comment(0x8D8A, 'A=0', align=Align.INLINE)
d.comment(0x8D8C, 'Clear pending operation marker', align=Align.INLINE)
d.comment(0x8D8F, 'Restore command line offset', align=Align.INLINE)
d.comment(0x8D90, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8D91, 'Load first option byte', align=Align.INLINE)
d.comment(0x8D93, 'Parse station number if present', align=Align.INLINE)
d.comment(0x8D96, 'Not a digit: skip to password entry', align=Align.INLINE)
d.comment(0x8D98, 'Parse user ID string', align=Align.INLINE)
d.comment(0x8D9B, 'No user ID: go to password', align=Align.INLINE)
d.comment(0x8DA7, 'No FS address: skip to password', align=Align.INLINE)
d.comment(0x8D9D, 'Store file server station low', align=Align.INLINE)
d.comment(0x8DA0, 'Check and store FS network', align=Align.INLINE)
d.comment(0x8DA3, 'Skip separator', align=Align.INLINE)
d.comment(0x8DA4, 'Parse next argument', align=Align.INLINE)
d.comment(0x8DA9, 'Store file server station high', align=Align.INLINE)
d.comment(0x8DAC, 'X=&FF: pre-decrement for loop', align=Align.INLINE)
d.comment(0x8DAE, 'Advance index', align=Align.INLINE)
d.comment(0x8DAF, 'Load logon command template byte', align=Align.INLINE)
d.comment(0x8DB2, 'Store into transmit buffer', align=Align.INLINE)
d.comment(0x8DB5, 'Bit 7 clear: more bytes, loop', align=Align.INLINE)
d.comment(0x8DB7, 'Send logon with file server lookup', align=Align.INLINE)
d.comment(0x8DBA, 'Success: skip to password entry', align=Align.INLINE)
d.comment(0x8DBC, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8DBF, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x8DC1, 'Advance to next byte', align=Align.INLINE)
d.comment(0x8DC2, 'Load byte from reply buffer', align=Align.INLINE)
d.comment(0x8DC5, 'Is it CR (end of prompt)?', align=Align.INLINE)
d.comment(0x8DC7, 'Yes: no colon found, skip to send', align=Align.INLINE)
d.comment(0x8DC9, "Is it ':' (password prompt)?", align=Align.INLINE)
d.comment(0x8DCB, 'No: keep scanning', align=Align.INLINE)
d.comment(0x8DD0, 'Save position of colon', align=Align.INLINE)
d.comment(0x8DD2, 'A=&FF: mark as escapable', align=Align.INLINE)
d.comment(0x8DD4, 'Set escape flag', align=Align.INLINE)
d.comment(0x8DD6, 'Check for escape condition', align=Align.INLINE)
d.comment(0x8DDE, 'Not NAK (&15): check other chars', align=Align.INLINE)
d.comment(0x8DE0, 'Restore colon position', align=Align.INLINE)
d.comment(0x8DE2, 'Non-zero: restart from colon', align=Align.INLINE)
d.comment(0x8DE4, 'At colon position?', align=Align.INLINE)
d.comment(0x8DE6, 'Yes: restart password input', align=Align.INLINE)
d.comment(0x8DE8, 'Backspace: move back one character', align=Align.INLINE)
d.comment(0x8DE9, 'If not at start: restart input', align=Align.INLINE)
d.comment(0x8DEB, 'Delete key (&7F)?', align=Align.INLINE)
d.comment(0x8DED, 'Yes: handle backspace', align=Align.INLINE)
d.comment(0x8DEF, 'Store character in password buffer', align=Align.INLINE)
d.comment(0x8DF2, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x8DF3, 'Is it CR (end of password)?', align=Align.INLINE)
d.comment(0x8DF5, 'No: read another character', align=Align.INLINE)
d.comment(0x8DFA, 'Transfer string length to A', align=Align.INLINE)
d.comment(0x8DFB, 'Save string length', align=Align.INLINE)
d.comment(0x8DFC, 'Set up transmit control block', align=Align.INLINE)
d.comment(0x8DFF, 'Send to file server and get reply', align=Align.INLINE)
d.comment(0x8E02, 'Restore string length', align=Align.INLINE)
d.comment(0x8E03, 'Transfer to X (byte count)', align=Align.INLINE)
d.comment(0x8E04, 'Include terminator', align=Align.INLINE)
d.comment(0x8E05, 'Y=0', align=Align.INLINE)
d.comment(0x8E09, 'Parse station number from cmd line', align=Align.INLINE)
d.comment(0x8E0C, 'Compare with expected station', align=Align.INLINE)
d.comment(0x8E0F, 'Different: return without clearing', align=Align.INLINE)
d.comment(0x8E11, 'Same: clear station byte', align=Align.INLINE)
d.comment(0x8E14, 'Return', align=Align.INLINE)
d.comment(0x8E15, 'Y=0: first character offset', align=Align.INLINE)
d.comment(0x8E20, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8E17, 'Load first character of command text', align=Align.INLINE)
d.comment(0x8E23, 'Transfer result to Y', align=Align.INLINE)
d.comment(0x8E19, "Is it '&' (URD prefix)?", align=Align.INLINE)
d.comment(0x8E24, 'Set up command and send to FS', align=Align.INLINE)
d.comment(0x8E1B, 'No: send as normal FS command', align=Align.INLINE)
d.comment(0x8E27, 'Load reply function code', align=Align.INLINE)
d.comment(0x8E1D, 'Yes: route via *RUN for URD prefix handling', align=Align.INLINE)
d.comment(0x8E2A, 'Zero: no reply, return', align=Align.INLINE)
d.comment(0x8E2C, 'Load first reply byte', align=Align.INLINE)
d.comment(0x8E2F, 'Y=&17: logon dispatch offset', align=Align.INLINE)
d.comment(0x8E33, 'Parse reply as decimal number', align=Align.INLINE)
d.comment(0x8E36, 'Result >= 8?', align=Align.INLINE)
d.comment(0x8E38, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E3A, 'Transfer handle to X', align=Align.INLINE)
d.comment(0x8E3B, 'Look up in open files table', align=Align.INLINE)
d.comment(0x8E3E, 'Transfer result to A', align=Align.INLINE)
d.comment(0x8E3F, 'Y=&13: handle dispatch offset', align=Align.INLINE)
d.comment(0x8E43, 'Handle >= 5?', align=Align.INLINE)
d.comment(0x8E45, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E47, 'Y=&0E: directory dispatch offset', align=Align.INLINE)
d.comment(0x8E49, 'Advance X to target index', align=Align.INLINE)
d.comment(0x8E4B, 'Y still positive: continue counting', align=Align.INLINE)
d.comment(0x8E4A, 'Decrement Y offset counter', align=Align.INLINE)
d.comment(0x8E4D, 'Y=&FF: will be ignored by caller', align=Align.INLINE)
d.comment(0x8E4E, 'Load dispatch address high byte', align=Align.INLINE)
d.comment(0x8E51, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E52, 'Load dispatch address low byte', align=Align.INLINE)
d.comment(0x8E55, 'Push low byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E56, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x8E58, 'Dispatch via RTS', align=Align.INLINE)
d.comment(0x8E59, """Printer server template (8 bytes)

Default printer server configuration data, read
indirectly by copy_ps_data via LDA ps_template_base,X
with X=&F8..&FF (reaching ps_template_base+&F8 =
&8E59). Contains "PRINT " (6 bytes) as the default
printer server name, followed by &01 and &00 as
default status bytes. Absent from NFS versions;
unique to ANFS.""")
d.comment(0x8E59, 'PS template: default name "PRINT "', align=Align.INLINE)
d.comment(0x8E83, 'X=0', align=Align.INLINE)
d.comment(0x8E85, 'Y=&FF', align=Align.INLINE)
d.comment(0x8E87, 'Execute OSBYTE and return', align=Align.INLINE)
d.comment(0x8E8A, """NETV handler address

2-byte handler address for the NETV extended
vector, read by write_vector_entry at Y=&36
from svc_dispatch_lo_offset. Points to
netv_handler which dispatches OSWORDs
0-8 to Econet handlers. Interleaved with the
OSBYTE wrapper code in the data area.""")
d.comment(0x8E8C, 'X=0', align=Align.INLINE)
d.comment(0x8E8E, 'Y=0', align=Align.INLINE)
d.comment(0x8E92, 'Get original OSBYTE A parameter', align=Align.INLINE)
d.comment(0x8E94, 'Subtract &31 (map &32-&35 to 1-4)', align=Align.INLINE)
d.comment(0x8E96, 'In range 0-3?', align=Align.INLINE)
d.comment(0x8E98, 'No: not ours, return unclaimed', align=Align.INLINE)
d.comment(0x8E9A, 'Transfer to X as dispatch index', align=Align.INLINE)
d.comment(0x8E9B, 'A=0: claim the service call', align=Align.INLINE)
d.comment(0x8E9D, 'Set return value to 0 (claimed)', align=Align.INLINE)
d.comment(0x8E9F, 'Transfer Y to A (OSBYTE Y param)', align=Align.INLINE)
d.comment(0x8EA0, 'Y=&21: OSBYTE dispatch offset', align=Align.INLINE)
d.comment(0x8EA2, 'Dispatch to OSBYTE handler via table', align=Align.INLINE)
d.comment(0x8EA5, 'Need at least &16 pages?', align=Align.INLINE)
d.comment(0x8EA7, 'Already enough: return', align=Align.INLINE)
d.comment(0x8EA9, 'Request &16 pages of workspace', align=Align.INLINE)
d.comment(0x8EAB, 'Return', align=Align.INLINE)
d.comment(0x8EAC, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8EAD, 'Y >= &21?', align=Align.INLINE)
d.comment(0x8EAF, 'No: use Y as-is', align=Align.INLINE)
d.comment(0x8EB1, 'Cap at &21', align=Align.INLINE)
d.comment(0x8EB3, 'Offset &0B in receive block', align=Align.INLINE)
d.comment(0x8EB5, 'Store workspace page count', align=Align.INLINE)
d.comment(0x8EB7, 'Return', align=Align.INLINE)
d.comment(0x8EB8, 'Store Y as receive block page', align=Align.INLINE)
d.comment(0x8EBA, 'Advance to next page', align=Align.INLINE)
d.comment(0x8EBB, 'Store as NFS workspace page', align=Align.INLINE)
d.comment(0x8EBD, 'Advance to next page', align=Align.INLINE)
d.comment(0x8EBE, 'Transfer page to A', align=Align.INLINE)
d.comment(0x8EBF, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8EC1, 'Store workspace page for this slot', align=Align.INLINE)
d.comment(0x8EC4, 'Load break type from hardware register', align=Align.INLINE)
d.comment(0x8EC7, 'A=0', align=Align.INLINE)
d.comment(0x8EC9, 'Clear receive block pointer low', align=Align.INLINE)
d.comment(0x8ECB, 'Clear NFS workspace pointer low', align=Align.INLINE)
d.comment(0x8ECD, 'Clear workspace page counter', align=Align.INLINE)
d.comment(0x8ECF, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8ED2, 'Offset 0 in receive block', align=Align.INLINE)
d.comment(0x8ED4, 'Clear remote operation flag', align=Align.INLINE)
d.comment(0x8ED6, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8ED8, 'X=1: workspace claim service', align=Align.INLINE)
d.comment(0x8EDA, 'Y=&0E: requested pages', align=Align.INLINE)
d.comment(0x8EDF, 'Record final workspace allocation', align=Align.INLINE)
d.comment(0x8EE2, 'Load ROM present flag', align=Align.INLINE)
d.comment(0x8EE5, 'Zero: first ROM init, skip FS setup', align=Align.INLINE)
d.comment(0x8EE7, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8EEA, 'Clear FS flags', align=Align.INLINE)
d.comment(0x8EED, 'A=0, transfer to Y', align=Align.INLINE)
d.comment(0x8EEE, 'Clear byte in FS workspace', align=Align.INLINE)
d.comment(0x8EF0, 'Clear byte in NFS workspace', align=Align.INLINE)
d.comment(0x8EF2, 'Advance index', align=Align.INLINE)
d.comment(0x8EF3, 'Loop until full page zeroed', align=Align.INLINE)
d.comment(0x8EF5, 'Offset 8 in receive block', align=Align.INLINE)
d.comment(0x8EF7, 'Clear protection flags', align=Align.INLINE)
d.comment(0x8EF9, 'Initialise station identity block', align=Align.INLINE)
d.comment(0x8EFC, 'Offset 2 in receive block', align=Align.INLINE)
d.comment(0x8EFE, 'A=&FE: default station ID marker', align=Align.INLINE)
d.comment(0x8F00, 'Store default station low', align=Align.INLINE)
d.comment(0x8F03, 'Store into receive block', align=Align.INLINE)
d.comment(0x8F05, 'A=0', align=Align.INLINE)
d.comment(0x8F07, 'Clear station high byte', align=Align.INLINE)
d.comment(0x8F0B, 'Store into receive block', align=Align.INLINE)
d.comment(0x8F0D, 'Offset 3 in NFS workspace', align=Align.INLINE)
d.comment(0x8F0F, 'Clear NFS workspace byte 3', align=Align.INLINE)
d.comment(0x8F12, 'A=&EB: default listen state', align=Align.INLINE)
d.comment(0x8F14, 'Store at NFS workspace offset 2', align=Align.INLINE)
d.comment(0x8F16, 'X=3: init data byte count', align=Align.INLINE)
d.comment(0x8F18, 'Load initialisation data byte', align=Align.INLINE)
d.comment(0x8F1B, 'Store in workspace', align=Align.INLINE)
d.comment(0x8F1E, 'Decrement counter', align=Align.INLINE)
d.comment(0x8F1F, 'More bytes: loop', align=Align.INLINE)
d.comment(0x8F21, 'Clear workspace flag', align=Align.INLINE)
d.comment(0x8F24, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8F49, """Workspace init data

3 bytes read via LDA ws_init_data,X with X=3
down to 1. ws_init_data at &8F48 overlaps the
high byte of JMP err_bad_station_num; byte at
&8F48 itself (&92) is never read (BNE exits
when X=0). Stores to tx_retry_count (&0D6D),
rx_wait_timeout (&0D6E), peek_retry_count
(&0D6F).""")
d.comment(0x8F49, 'tx_retry_count: init=&FF (255 retries)', align=Align.INLINE)
d.comment(0x8F4A, 'rx_wait_timeout: init=&28 (40, reply wait)', align=Align.INLINE)
d.comment(0x8F4B, 'peek_retry_count: init=&0A (10, peek retries)', align=Align.INLINE)
d.comment(0x8F27, 'Initialise ADLC protection table', align=Align.INLINE)
d.comment(0x8F2A, 'X=&FF (underflow from X=0)', align=Align.INLINE)
d.comment(0x8F2E, 'Get current workspace page', align=Align.INLINE)
d.comment(0x8F2B, 'Initialise workspace flag to &FF', align=Align.INLINE)
d.comment(0x8F30, 'Allocate FS handle page', align=Align.INLINE)
d.comment(0x8F33, 'Allocation failed: finish init', align=Align.INLINE)
d.comment(0x8F35, 'A=&3F: default handle permissions', align=Align.INLINE)
d.comment(0x8F37, 'Store handle permissions', align=Align.INLINE)
d.comment(0x8F39, 'Advance to next page', align=Align.INLINE)
d.comment(0x8F3B, 'Continue allocating: loop', align=Align.INLINE)
d.comment(0x8F3D, 'Restore FS context from saved state', align=Align.INLINE)
d.comment(0x8F40, 'Read station ID from hardware', align=Align.INLINE)
d.comment(0x8F43, 'Transfer to A', align=Align.INLINE)
d.comment(0x8F44, 'Non-zero: station ID valid', align=Align.INLINE)
d.comment(0x8F46, 'Station 0: report error', align=Align.INLINE)
d.comment(0x8F4C, 'Increment station ID', align=Align.INLINE)
d.comment(0x8F4D, 'Overflow to 0: report error', align=Align.INLINE)
d.comment(0x8F4F, 'Offset 1: station ID in recv block', align=Align.INLINE)
d.comment(0x8F51, 'Store station ID', align=Align.INLINE)
d.comment(0x8F53, 'X=&40: Econet flag byte', align=Align.INLINE)
d.comment(0x8F55, 'Store Econet control flag', align=Align.INLINE)
d.comment(0x8F58, 'A=3: protection level', align=Align.INLINE)
d.comment(0x8F5A, 'Set up Econet protection', align=Align.INLINE)
d.comment(0x8F5D, 'Initialise ADLC hardware', align=Align.INLINE)
d.comment(0x8F60, 'OSBYTE &A8: read ROM pointer table', align=Align.INLINE)
d.comment(0x8F62, 'Read ROM pointer table address', align=Align.INLINE)
d.comment(0x8F65, 'Store table pointer low', align=Align.INLINE)
d.comment(0x8F67, 'Store table pointer high', align=Align.INLINE)
d.comment(0x8F69, 'Y=&36: NETV vector offset', align=Align.INLINE)
d.comment(0x8F6B, 'Set NETV address', align=Align.INLINE)
d.comment(0x8F6E, 'X=1: one more vector pair to set', align=Align.INLINE)
d.comment(0x8F70, 'Load vector address low byte', align=Align.INLINE)
d.comment(0x8F73, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x8F75, 'Advance to high byte', align=Align.INLINE)
d.comment(0x8F76, 'Load vector address high byte', align=Align.INLINE)
d.comment(0x8F79, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x8F7B, 'Advance to ROM ID byte', align=Align.INLINE)
d.comment(0x8F7C, 'Load current ROM slot number', align=Align.INLINE)
d.comment(0x8F7E, 'Store ROM ID in extended vector', align=Align.INLINE)
d.comment(0x8F80, 'Advance to next vector entry', align=Align.INLINE)
d.comment(0x8F81, 'Decrement vector counter', align=Align.INLINE)
d.comment(0x8F82, 'More vectors to set: loop', align=Align.INLINE)
d.comment(0x8F84, 'X=&FF', align=Align.INLINE)
d.comment(0x8F84, 'Restore FS state if previously active', align=Align.INLINE)
d.comment(0x8F87, 'Get workspace page for ROM slot', align=Align.INLINE)
d.comment(0x8F8A, 'Advance Y past workspace page', align=Align.INLINE)
d.comment(0x8F8B, 'Return', align=Align.INLINE)
d.comment(0x8F8C, 'Y=9: end of FS context block', align=Align.INLINE)
d.comment(0x8F8E, 'Load FS context byte', align=Align.INLINE)
d.comment(0x8F91, 'Store into receive block', align=Align.INLINE)
d.comment(0x8F93, 'Decrement index', align=Align.INLINE)
d.comment(0x8F94, 'Reached offset 1?', align=Align.INLINE)
d.comment(0x8F96, 'No: continue copying', align=Align.INLINE)
d.comment(0x8F98, 'Return', align=Align.INLINE)
d.comment(0x8F99, 'FS currently selected?', align=Align.INLINE)
d.comment(0x8F9C, 'No (bit 7 clear): return', align=Align.INLINE)
d.comment(0x8F9E, 'Y=0', align=Align.INLINE)
d.comment(0x8FA0, 'Reset FS connection state', align=Align.INLINE)
d.comment(0x8FA3, 'OSBYTE &77: close SPOOL/EXEC', align=Align.INLINE)
d.comment(0x8FA8, 'Restore FS context to receive block', align=Align.INLINE)
d.comment(0x8FAB, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8FAD, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x8FAF, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8FB0, 'Add byte from page &10 shadow', align=Align.INLINE)
d.comment(0x8FB3, 'Decrement index', align=Align.INLINE)
d.comment(0x8FB4, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8FB6, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8FBA, 'Load byte from page &10 shadow', align=Align.INLINE)
d.comment(0x8FBD, 'Copy to FS workspace', align=Align.INLINE)
d.comment(0x8FBF, 'Decrement index', align=Align.INLINE)
d.comment(0x8FC0, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8FC2, 'Load FS flags', align=Align.INLINE)
d.comment(0x8FC5, 'Clear bit 7 (FS no longer selected)', align=Align.INLINE)
d.comment(0x8FC7, 'Store updated flags', align=Align.INLINE)
d.comment(0x8FCA, 'Return', align=Align.INLINE)
d.comment(0x8FCB, 'Save processor status', align=Align.INLINE)
d.comment(0x8FCC, 'Save A', align=Align.INLINE)
d.comment(0x8FCD, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8FCE, 'Save Y', align=Align.INLINE)
d.comment(0x8FCF, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8FD1, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x8FD3, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8FD4, 'Add byte from FS workspace', align=Align.INLINE)
d.comment(0x8FD6, 'Decrement index', align=Align.INLINE)
d.comment(0x8FD7, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8FD9, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8FDB, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x8FDD, 'Mismatch: raise checksum error', align=Align.INLINE)
d.comment(0x8FDF, 'Restore Y', align=Align.INLINE)
d.comment(0x8FE0, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8FE1, 'Restore A', align=Align.INLINE)
d.comment(0x8FE2, 'Restore processor status', align=Align.INLINE)
d.comment(0x8FE3, 'Return (checksum valid)', align=Align.INLINE)
d.comment(0x8FE4, 'Error number &AA', align=Align.INLINE)
d.comment(0x8FE6, "Raise 'net checksum' error", align=Align.INLINE)
d.comment(0x8FF1, "Print 'Econet Station ' prefix", align=Align.INLINE)
d.comment(0x8FF6, "Print 'Econet Station ' via inline", align=Align.INLINE)
d.comment(0x9003, 'Y=1: station number offset in RX block', align=Align.INLINE)
d.comment(0x9005, 'Load station ID from receive block', align=Align.INLINE)
d.comment(0x9007, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x900A, 'Space character', align=Align.INLINE)
d.comment(0x900C, 'Check ADLC status register 2', align=Align.INLINE)
d.comment(0x900F, 'Clock present: skip warning', align=Align.INLINE)
d.comment(0x9011, "Print ' No Clock' via inline", align=Align.INLINE)
d.comment(0x901D, 'NOP (string terminator)', align=Align.INLINE)
d.comment(0x9021, 'Return', align=Align.INLINE)
d.comment(0x9022, """*HELP command syntax strings

13 null-terminated syntax help strings displayed
by *HELP after each command name. Multi-line
entries use &0D as a line break. Indexed by
cmd_syntax_table via the low 5 bits of each
command's syntax descriptor byte.""")
d.comment(0x9022, 'Syn 1: *Dir, *LCat, *LEx, *Wipe', align=Align.INLINE)
d.comment(0x9029, 'Null terminator', align=Align.INLINE)
d.comment(0x902A, 'Syn 2: *I Am (login)', align=Align.INLINE)
d.comment(0x9042, 'Line break', align=Align.INLINE)
d.comment(0x9043, 'Syn 2 continued: password clause', align=Align.INLINE)
d.comment(0x9056, 'Null terminator', align=Align.INLINE)
d.comment(0x9057, 'Syn 3: *Delete, *FS, *Remove', align=Align.INLINE)
d.comment(0x905F, 'Null terminator', align=Align.INLINE)
d.comment(0x9060, 'Syn 4: *Dump', align=Align.INLINE)
d.comment(0x9075, 'Line break', align=Align.INLINE)
d.comment(0x9076, 'Syn 4 continued: address clause', align=Align.INLINE)
d.comment(0x9082, 'Null terminator', align=Align.INLINE)
d.comment(0x9083, 'Syn 5: *Lib', align=Align.INLINE)
d.comment(0x9088, 'Null terminator', align=Align.INLINE)
d.comment(0x9089, 'Syn 6: *CDir', align=Align.INLINE)
d.comment(0x9099, 'Null terminator', align=Align.INLINE)
d.comment(0x909A, 'Syn 7: *Pass', align=Align.INLINE)
d.comment(0x90AD, 'Line break', align=Align.INLINE)
d.comment(0x90AE, 'Syn 7 continued: new password', align=Align.INLINE)
d.comment(0x90BC, 'Null terminator', align=Align.INLINE)
d.comment(0x90BD, 'Syn 8: *PS, *Pollps', align=Align.INLINE)
d.comment(0x90D3, 'Null terminator', align=Align.INLINE)
d.comment(0x90D4, 'Syn 9: *Access', align=Align.INLINE)
d.comment(0x90EF, 'Null terminator', align=Align.INLINE)
d.comment(0x90F0, 'Syn 10: *Rename', align=Align.INLINE)
d.comment(0x9109, 'Null terminator', align=Align.INLINE)
d.comment(0x910A, 'Syn 11: (station id. argument)', align=Align.INLINE)
d.comment(0x9116, 'Null terminator', align=Align.INLINE)
d.comment(0x9117, 'Syn 12: *Print, *Type', align=Align.INLINE)
d.comment(0x9121, 'Null terminator', align=Align.INLINE)
d.comment(0x9122, """Command syntax string offset table

13 offsets into cmd_syntax_strings (&9022).
Indexed by the low 5 bits of each command table
syntax descriptor byte. Index &0E is handled
separately as a shared-commands list. The print
loop at &8BD5 does INY before LDA, so each offset
points to the byte before the first character.""")
d.comment(0x9122, 'Idx 0: (no syntax)', align=Align.INLINE)
d.comment(0x9123, 'Idx 1: "(<dir>)" (Y wraps via &FF)', align=Align.INLINE)
d.comment(0x9124, 'Idx 2: "(<stn.id.>) <user id.>..."', align=Align.INLINE)
d.comment(0x9125, 'Idx 3: "<object>"', align=Align.INLINE)
d.comment(0x9126, 'Idx 4: "<filename> (<offset>...)"', align=Align.INLINE)
d.comment(0x9127, 'Idx 5: "<dir>"', align=Align.INLINE)
d.comment(0x9128, 'Idx 6: "<dir> (<number>)"', align=Align.INLINE)
d.comment(0x9129, 'Idx 7: "(:<CR>) <password>..."', align=Align.INLINE)
d.comment(0x912A, 'Idx 8: "(<stn.id.>|<ps type>)"', align=Align.INLINE)
d.comment(0x912B, 'Idx 9: "<object> (L)(W)(R)..."', align=Align.INLINE)
d.comment(0x912C, 'Idx 10: "<filename> <new filename>"', align=Align.INLINE)
d.comment(0x912D, 'Idx 11: "(<stn. id.>)"', align=Align.INLINE)
d.comment(0x912E, 'Idx 12: "<filename>"', align=Align.INLINE)
d.comment(0x912F, 'Save full byte', align=Align.INLINE)
d.comment(0x9130, 'Shift high nybble to low', align=Align.INLINE)
d.comment(0x9131, 'Continue shifting', align=Align.INLINE)
d.comment(0x9132, 'Continue shifting', align=Align.INLINE)
d.comment(0x9133, 'High nybble now in bits 0-3', align=Align.INLINE)
d.comment(0x9134, 'Print high nybble as hex digit', align=Align.INLINE)
d.comment(0x9137, 'Restore full byte', align=Align.INLINE)
d.comment(0x9138, 'Mask to low nybble', align=Align.INLINE)
d.comment(0x913A, 'Digit >= &0A?', align=Align.INLINE)
d.comment(0x913C, 'No: skip letter adjustment', align=Align.INLINE)
d.comment(0x913E, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.comment(0x9140, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x948B, """TXCB initialisation template (12 bytes)

Copied by init_txcb into the TXCB workspace at
&00C0. For offsets 0-1, the destination station
bytes are also copied from l0e00 into txcb_dest.

The &FF byte at offset 6 (bit_test_ff, &9491)
serves double duty: it is part of this template
AND a BIT target used by 22 callers to set the
V and N flags without clobbering A.""")
d.comment(0x948B, 'Offset 0: txcb_ctrl = &80 (transmit)', align=Align.INLINE)
d.comment(0x948C, 'Offset 1: txcb_port = &99 (FS reply)', align=Align.INLINE)
d.comment(0x948D, 'Offset 2: txcb_dest lo (overwritten)', align=Align.INLINE)
d.comment(0x948E, 'Offset 3: txcb_dest hi (overwritten)', align=Align.INLINE)
d.comment(0x948F, 'Offset 4: txcb_start = 0', align=Align.INLINE)
d.comment(0x9490, 'Offset 5: buffer start hi (page &0F)', align=Align.INLINE)
d.comment(0x9491, 'Offset 6: BIT target / buffer end lo', align=Align.INLINE)
d.comment(0x9492, 'Offset 7: txcb_pos = &FF', align=Align.INLINE)
d.comment(0x9493, 'Offset 8: txcb_end = &FF', align=Align.INLINE)
d.comment(0x9494, 'Offset 9: buffer end hi (page &0F)', align=Align.INLINE)
d.comment(0x9495, 'Offset 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x9496, 'Offset 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x89CA, """Service dispatch table (37 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_dispatch.
Indices 0-14: service calls (index = service + 1).
Indices 15-36: FS command and OSWORD routing.
Indices 1, 7, 11 point to return_4 (no-op RTS).""")

d.label(0x89CA, 'svc_dispatch_lo')

d.label(0x89EF, 'svc_dispatch_hi')
for i in range(1, 37):
    d.rts_code_ptr(0x89CA + i, 0x89EF + i)
svc_dispatch_comments = ['dummy entry (outside ROM range)', 'Svc 0: already claimed (no-op)', 'Svc 1: absolute workspace', 'Svc 2: private workspace', 'Svc 3: auto-boot', 'Svc 4: unrecognised star command', 'Svc 5: unrecognised interrupt', 'Svc 6: BRK (no-op)', 'Svc 7: unrecognised OSBYTE', 'Svc 8: unrecognised OSWORD', 'Svc 9: *HELP', 'Svc 10: static workspace (no-op)', 'Svc 11: NMI release (reclaim NMIs)', 'Svc 12: NMI claim (save NMI state)', 'Svc 18: filing system selection', 'Lang 0: no language / Tube', 'Lang 1: normal startup', 'Lang 2: softkey byte (Electron)', 'Lang 3: softkey length (Electron)', 'Lang 4: remote validated', 'FSCV 0: *OPT', 'FSCV 1: EOF check', 'FSCV 2: */ (run)', 'FSCV 3: unrecognised star command', 'FSCV 4: *RUN', 'FSCV 5: *CAT', 'FSCV 6: shutdown', 'FSCV 7: read handle range', 'FS reply: print directory name', 'FS reply: copy handles + boot', 'FS reply: copy handles', 'FS reply: set CSD handle', 'FS reply: notify + execute', 'FS reply: set library handle', '*NET1: read handle from packet', '*NET2: read handle from workspace', '*NET3: close handle']
for i, body in enumerate(svc_dispatch_comments):
    d.comment(0x89CA + i, f'lo - {body}', align=Align.INLINE)
    d.comment(0x89EF + i, f'hi - {body}', align=Align.INLINE)
d.entry(0x8EA5)
d.entry(0x8EB8)
d.entry(0x8CCA)
d.entry(0x8C4E)
d.entry(0x8E92)
d.entry(0xA4EE)
d.entry(0x8C5D)
d.entry(0x8B0D)

d.label(0x8EA5, 'svc_1_abs_workspace')

d.label(0x8EB8, 'svc_2_private_workspace')

d.label(0x8CCA, 'svc_3_autoboot')

d.label(0x8C4E, 'svc_4_star_command')

d.label(0x8E92, 'svc_7_osbyte')

d.label(0xA4EE, 'svc_8_osword')

d.label(0x8C5D, 'svc_9_help')

d.label(0x8B0D, 'svc_18_fs_select')


d.subroutine(0x8EA5, 'svc_1_abs_workspace', title='Service 1: absolute workspace claim', description="""Ensures the NFS workspace allocation is at least
&16 pages by checking Y on entry. If Y < &16,
sets Y = &16 to claim the required pages;
otherwise returns Y unchanged. This is a passive
claim — NFS only raises the allocation, never
lowers it.""", on_entry={'y': 'current highest workspace page claim'}, on_exit={'y': '>= &16 (NFS minimum requirement)'})


d.subroutine(0x8EB8, 'svc_2_private_workspace', title='Service 2: claim private workspace and initialise NFS', description="""Handles MOS service call 2 (private workspace
claim). Allocates two workspace pages starting
at Y: the receive block page (net_rx_ptr_hi) and
NFS workspace page (nfs_workspace_hi), plus a
per-ROM workspace page stored at &0DF0+ROM slot.
Zeroes all workspace, initialises the station ID
from the Econet hardware register at &FE18,
allocates FS handle pages, copies initial state
to page &10, and falls through to
init_adlc_and_vectors.""", on_entry={'y': 'first available private workspace page'})


d.subroutine(0x8CCA, 'svc_3_autoboot', title='Service 3: auto-boot on reset', description="""Scans the keyboard via OSBYTE &7A for the 'N' key
(&19 or &55 EOR'd with &55). If pressed, records
the key state via OSBYTE &78. Selects the network
filing system by calling cmd_net_fs, prints the
station ID, then checks if this is the first boot
(ws_page = 0). If so, sets the auto-boot flag in
&1071 and JMPs to cmd_fs_entry to execute the boot
file.""")


d.subroutine(0x8C4E, 'svc_4_star_command', title='Service 4: unrecognised star command', description="""Saves the OS text pointer, then calls match_fs_cmd
to search the command table starting at offset 0
(all command sub-tables). If no match is found (carry
set), returns with the service call unclaimed. On
a match, JMPs to cmd_fs_reentry to execute the
matched command handler via the PHA/PHA/RTS
dispatch mechanism.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8E92, 'svc_7_osbyte', title='Service 7: unrecognised OSBYTE', description="""Maps Econet OSBYTE codes &32-&35 to dispatch
indices 0-3 by subtracting &31 (with carry from
a preceding SBC). Returns unclaimed if the OSBYTE
number is outside this range. For valid codes,
claims the service (sets svc_state to 0) and
JMPs to svc_dispatch with Y=&21 to reach the
Econet OSBYTE handler table.""", on_entry={'a': 'OSBYTE number (from osbyte_a_copy at &EF)'})


d.subroutine(0xA4EE, 'svc_8_osword', title='Filing system OSWORD entry', description="""Handles MOS service call 8 (unrecognised OSWORD).
Filters OSWORD codes &0E-&14 by subtracting &0E (via
CLC/SBC &0D) and rejecting values outside 0-6. For
valid codes, calls osword_setup_handler to push the
dispatch address, then copies 3 bytes from the RX
buffer to osword_flag workspace.""")


d.subroutine(0x8C5D, 'svc_9_help', title='Service 9: *HELP', description="""Handles MOS service call 9 (*HELP). First checks
for the credits Easter egg. For bare *HELP (CR
at text pointer), prints the version header and
full command list starting at table offset &C4.
For *HELP with an argument, handles '.' as a
shortcut to list all NFS commands, otherwise
iterates through help topics using PHA/PHA/RTS
dispatch to print matching command groups.
Returns with Y = ws_page (unclaimed).""")


d.subroutine(0x8B0D, 'svc_18_fs_select', title='Service 18: filing system selection request', description="""Checks if Y=5 (Econet filing system number);
returns unclaimed if not. Also returns if bit 7
of &0D6C is already set, indicating the FS is
already selected. Otherwise falls through to
cmd_net_fs to perform the full network filing
system selection sequence.""", on_entry={'y': 'filing system number requested'})
d.entry(0x95CE)
d.entry(0x9580)
d.entry(0xAC98)
d.entry(0x95AE)
d.entry(0x95BE)
d.entry(0x9DC8)
d.entry(0x9B92)
d.entry(0x9DEE)
d.entry(0xA1C1)
d.entry(0xA114)
d.entry(0xAD80)
d.entry(0x8F99)
d.entry(0x92B0)
d.entry(0xAF3E)
d.entry(0xA391)
d.entry(0xA39B)
d.entry(0xA2F4)
d.entry(0xA2FA)
d.entry(0xA0E4)
d.entry(0xA0EA)
d.entry(0xA0FA)
d.comment(0xA3F0, """Star command table (4 interleaved sub-tables).
Each entry: ASCII name + flag byte (&80+) +
dispatch address word (PHA/PHA/RTS, addr-1).
Sub-tables separated by &80 sentinel bytes.
Flag byte: bit 7 = end of name marker,
bit 6 = set V on return if no argument,
bits 0-4 = *HELP syntax string index.
1: Utility cmds  2: NFS commands
3: Help topics  4: Copro/attributes""")

d.label(0xA3F0, 'cmd_table_fs')

d.label(0xA43A, 'cmd_table_nfs')

d.label(0xA4B2, 'cmd_table_help')

d.label(0xA4C3, 'cmd_table_copro')
d.string(0xA3F0, 1)
d.string(0xA3F1, 1)
d.string(0xA41D, 2)
d.byte(0xA41F)
d.string(0xA45F, 2)
d.byte(0xA461)
d.string(0xA46B, 2)
d.byte(0xA46D)
d.entry(0xB994)
d.entry(0xBA1B)
d.entry(0x8B1A)
d.entry(0xB1C3)
d.entry(0xB99D)
d.entry(0xB30C)
d.entry(0xAFEE)
d.entry(0xB99A)
d.entry(0xB33D)
d.entry(0x8AD4)
_cmd_entries = [(0xA3F6, 'cmd_close'), (0xA3FD, 'cmd_dump'), (0xA403, 'cmd_net_fs'), (0xA40C, 'cmd_pollps'), (0xA414, 'cmd_print'), (0xA41B, 'cmd_prot'), (0xA420, 'cmd_ps'), (0xA427, 'cmd_roff'), (0xA42E, 'cmd_type'), (0xA437, 'cmd_unprot'), (0xA441, 'cmd_fs_operation'), (0xA447, 'cmd_bye'), (0xA44E, 'cmd_cdir'), (0xA457, 'cmd_fs_operation'), (0xA45D, 'cmd_dir'), (0xA462, 'cmd_ex'), (0xA469, 'cmd_flip'), (0xA46E, 'cmd_fs'), (0xA475, 'cmd_fs_operation'), (0xA47C, 'cmd_iam'), (0xA483, 'cmd_lcat'), (0xA489, 'cmd_lex'), (0xA48F, 'cmd_fs_operation'), (0xA496, 'cmd_pass'), (0xA49F, 'cmd_remove'), (0xA4A8, 'cmd_rename'), (0xA4AF, 'cmd_wipe'), (0xA4B8, 'help_net'), (0xA4C0, 'help_utils')]
for addr, target_label in _cmd_entries:
    d.word(addr)
    d.expr(addr, target_label + '-1')
d.comment(0xA3F0, '*Close (first char)', align=Align.INLINE)
d.comment(0xA3F1, '*Close cont (dispatch lo base)', align=Align.INLINE)
d.comment(0xA3F2, '*Close cont (dispatch hi base)', align=Align.INLINE)
d.comment(0xA3F5, 'No syntax', align=Align.INLINE)
d.comment(0xA3F8, '*Dump', align=Align.INLINE)
d.comment(0xA3FF, '*Net (select NFS)', align=Align.INLINE)
d.comment(0xA402, 'No syntax', align=Align.INLINE)
d.comment(0xA405, '*Pollps', align=Align.INLINE)
d.comment(0xA40B, 'Syn 8: (<stn. id.>|<ps type>)', align=Align.INLINE)
d.comment(0xA40E, '*Print', align=Align.INLINE)
d.comment(0xA413, 'V no arg; syn 12: <filename>', align=Align.INLINE)
d.comment(0xA416, '*Prot', align=Align.INLINE)
d.comment(0xA41A, 'Syn 14: (attribute keywords)', align=Align.INLINE)
d.comment(0xA41D, '*PS; syn 8: (<stn. id.>|<ps type>)', align=Align.INLINE)
d.comment(0xA422, '*Roff', align=Align.INLINE)
d.comment(0xA426, 'No syntax', align=Align.INLINE)
d.comment(0xA429, '*Type', align=Align.INLINE)
d.comment(0xA42D, 'V no arg; syn 12: <filename>', align=Align.INLINE)
d.comment(0xA430, '*Unprot', align=Align.INLINE)
d.comment(0xA436, 'Syn 14: (attribute keywords)', align=Align.INLINE)
d.comment(0xA439, 'End of utility sub-table', align=Align.INLINE)
d.comment(0xA43A, '*Access', align=Align.INLINE)
d.comment(0xA440, 'V no arg; syn 9: <obj> (L)(W)(R)...', align=Align.INLINE)
d.comment(0xA443, '*Bye', align=Align.INLINE)
d.comment(0xA446, 'No syntax', align=Align.INLINE)
d.comment(0xA449, '*Cdir', align=Align.INLINE)
d.comment(0xA44D, 'V no arg; syn 6: <dir> (<number>)', align=Align.INLINE)
d.comment(0xA450, '*Delete', align=Align.INLINE)
d.comment(0xA456, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA459, '*Dir', align=Align.INLINE)
d.comment(0xA45C, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA45F, '*Ex; syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA464, '*Flip', align=Align.INLINE)
d.comment(0xA468, 'No syntax', align=Align.INLINE)
d.comment(0xA46B, '*FS; syn 11: (<stn. id.>)', align=Align.INLINE)
d.comment(0xA470, '*Info', align=Align.INLINE)
d.comment(0xA474, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA477, '*I am', align=Align.INLINE)
d.comment(0xA47B, 'V no arg; syn 2: (<stn>) <user>...', align=Align.INLINE)
d.comment(0xA47E, '*Lcat', align=Align.INLINE)
d.comment(0xA482, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA485, '*Lex', align=Align.INLINE)
d.comment(0xA488, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA48B, '*Lib', align=Align.INLINE)
d.comment(0xA48E, 'V no arg; syn 5: <dir>', align=Align.INLINE)
d.comment(0xA491, '*Pass', align=Align.INLINE)
d.comment(0xA495, 'V no arg; syn 7: <pass> ...', align=Align.INLINE)
d.comment(0xA498, '*Remove', align=Align.INLINE)
d.comment(0xA4A2, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA4A1, '*Rename', align=Align.INLINE)
d.comment(0xA4A7, 'V no arg; syn 10: <file> <new file>', align=Align.INLINE)
d.comment(0xA4AA, '*Wipe', align=Align.INLINE)
d.comment(0xA4B1, 'End of NFS sub-table', align=Align.INLINE)
d.comment(0xA4B4, '*Net (local)', align=Align.INLINE)
d.comment(0xA4B7, 'No syntax', align=Align.INLINE)
d.comment(0xA4BA, '*Utils', align=Align.INLINE)
d.comment(0xA4BF, 'No syntax', align=Align.INLINE)
d.comment(0xA4C2, 'End of help topic sub-table', align=Align.INLINE)
d.comment(0xA4C3, """Protection attribute keyword table. Each entry:
ASCII name + flag byte (&80+) + OR mask + AND mask.
Used by *Prot (ORA lo byte) and *Unprot (AND hi
byte) to set/clear individual protection bits.
Also listed by *HELP Prot/*HELP Unprot via the
shared commands handler (syntax index 14).
Bits: 0=Peek 1=Poke 2=JSR 3=Proc 4=Utils 5=Halt""")
_attr_entries = [(0xA4C7, 0xA4C8, 0xA4C9), (0xA4CD, 0xA4CE, 0xA4CF), (0xA4D4, 0xA4D5, 0xA4D6), (0xA4DB, 0xA4DC, 0xA4DD), (0xA4E2, 0xA4E3, 0xA4E4), (0xA4EA, 0xA4EB, 0xA4EC)]
for flag_addr, or_addr, and_addr in _attr_entries:
    d.byte(flag_addr)
    d.byte(or_addr)
    d.byte(and_addr)
d.byte(0xA4ED)
d.comment(0xA4C3, 'Halt', align=Align.INLINE)
d.comment(0xA4C7, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4C8, '*Prot OR mask: bit 5', align=Align.INLINE)
d.comment(0xA4C9, '*Unprot AND mask: ~bit 5', align=Align.INLINE)
d.comment(0xA4CA, 'JSR', align=Align.INLINE)
d.comment(0xA4CD, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4CE, '*Prot OR mask: bit 2', align=Align.INLINE)
d.comment(0xA4CF, '*Unprot AND mask: ~bit 2', align=Align.INLINE)
d.comment(0xA4D0, 'Peek', align=Align.INLINE)
d.comment(0xA4D4, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4D5, '*Prot OR mask: bit 0', align=Align.INLINE)
d.comment(0xA4D6, '*Unprot AND mask: ~bit 0', align=Align.INLINE)
d.comment(0xA4D7, 'Poke', align=Align.INLINE)
d.comment(0xA4DB, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4DC, '*Prot OR mask: bit 1', align=Align.INLINE)
d.comment(0xA4DD, '*Unprot AND mask: ~bit 1', align=Align.INLINE)
d.comment(0xA4DE, 'Proc', align=Align.INLINE)
d.comment(0xA4E2, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4E3, '*Prot OR mask: bit 3', align=Align.INLINE)
d.comment(0xA4E4, '*Unprot AND mask: ~bit 3', align=Align.INLINE)
d.comment(0xA4E5, 'Utils', align=Align.INLINE)
d.comment(0xA4EA, 'Flag &A9: syn 9 (unused)', align=Align.INLINE)
d.comment(0xA4EB, '*Prot OR mask: bit 4', align=Align.INLINE)
d.comment(0xA4EC, '*Unprot AND mask: ~bit 4', align=Align.INLINE)
d.comment(0xA4ED, 'End of attribute keyword table', align=Align.INLINE)

d.label(0xB994, 'cmd_close')

d.label(0xBA1B, 'cmd_dump')

d.label(0x8B1A, 'cmd_net_fs')

d.label(0xB1C3, 'cmd_pollps')

d.label(0xB99D, 'cmd_print')

d.label(0xB30C, 'cmd_prot')

d.label(0xAFEE, 'cmd_ps')

d.label(0xB99A, 'cmd_type')

d.label(0xB33D, 'cmd_unprot')

d.label(0x8AD4, 'cmd_roff')


d.subroutine(0xB994, 'cmd_close', title='*Close command handler', description="""Loads A=0 and Y=0, then jumps to OSFIND to close
all open files on the current file server (equivalent
to CLOSE#0). Files open on other file servers are
not affected.""")


d.subroutine(0xBA1B, 'cmd_dump', title='*Dump command handler', description="""Opens the file via open_file_for_read, allocates a
21-byte buffer on the stack, and parses the address
range via init_dump_buffer. Loops reading 16 bytes
per line, printing each as a 4-byte hex address,
16 hex bytes with spaces, and a 16-character ASCII
column (non-printable chars shown as '.'). Prints
a column header at every 256-byte boundary.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8B1A, 'cmd_net_fs', title='Select Econet network filing system', description="""Computes a checksum over the first &77 bytes of
the workspace page and verifies against the stored
value; raises an error on mismatch. On success,
notifies the OS via FSCV reason 6, copies the FS
context block from the receive block to &0DFA,
installs 7 filing system vectors (FILEV etc.)
from fs_vector_table, initialises the ADLC and
extended vectors, sets up the channel table, and
copies the workspace page to &1000 as a shadow.
Sets bit 7 of &0D6C to mark the FS as selected,
then issues service call 15.""")


d.subroutine(0xB1C3, 'cmd_pollps', title='*Pollps command handler', description="""Initialises the spool drive, copies the PS name to
the TX buffer, and parses an optional station number
or PS name argument. Sends a poll request, then
prints the server address and name. Iterates through
PS slots, displaying each station's status as
'ready', 'busy' (with client station), or 'jammed'.
Marks processed slots with &3F.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB99D, 'cmd_print', title='*Print command handler', description="""Sets V flag (distinguishing from *Type which clears V),
then opens the file for reading. Loops reading bytes
via OSBGET, checking for escape between each. In type
mode (V clear), normalises CR/LF pairs to single
newlines by tracking the previous character. In print
mode (V set), outputs all bytes raw via OSWRCH. Closes
the file and prints a final newline on EOF.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB30C, 'cmd_prot', title='*Prot command handler', description="""With no arguments, sets all protection bits (&FF).
Otherwise parses attribute keywords via match_fs_cmd
with table offset &D3, accumulating bits via ORA.
Stores the final protection mask in ws_0d68 and
ws_0d69.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xAFEE, 'cmd_ps', title='*PS command handler', description="""Checks the printer server availability flag; raises
'Printer busy' if unavailable. Initialises the spool
drive and buffer pointer, then dispatches on argument
type: no argument branches to no_ps_name_given, a
leading digit branches to save_ps_cmd_ptr as a station
number, otherwise parses a named PS address via
load_ps_server_addr and parse_fs_ps_args.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB99A, 'cmd_type', title='*Type command handler', description="""Clears V and branches to the shared open_and_read_file
entry in cmd_print. The V-clear state selects line-
ending normalisation mode: CR, LF, CR+LF, and LF+CR
are all treated as a single newline. Designed for
displaying text files.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB33D, 'cmd_unprot', title='*Unprot command handler', description="""With no arguments, clears all protection bits (EOR
yields 0). Otherwise parses attribute keywords, clearing
bits via AND with the complement. Shares the protection
mask storage path with cmd_prot. Falls through to
cmd_wipe.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8AD4, 'cmd_roff', title='*ROFF command handler', description="""Disables remote operation by clearing the flag at
offset 0 in the receive block. If remote operation
was active, re-enables the keyboard via OSBYTE &C9
(with X=0, Y=0) and calls tx_econet_abort with
A=&0A to reinitialise the workspace area. Falls
through to scan_remote_keys which clears svc_state
and nfs_workspace.""")
d.entry(0x92E6)
d.entry(0x949E)
d.entry(0xAD10)
d.entry(0x93DD)
d.entry(0xAD6B)
d.entry(0xA356)
d.entry(0xA07B)
d.entry(0x8D79)
d.entry(0xAD5F)
d.entry(0xAD65)
d.entry(0x8DBC)
d.entry(0xAF66)
d.entry(0x938B)
d.entry(0xB359)

d.label(0x92E6, 'cmd_fs_operation')

d.label(0x949E, 'cmd_bye')

d.label(0xAD10, 'cmd_cdir')

d.label(0x93DD, 'cmd_dir')

d.label(0xAD6B, 'cmd_ex')

d.label(0xA356, 'cmd_flip')

d.label(0xA07B, 'cmd_fs')

d.label(0x8D79, 'cmd_iam')

d.label(0xAD5F, 'cmd_lcat')

d.label(0xAD65, 'cmd_lex')

d.label(0x8DBC, 'cmd_pass')

d.label(0xAF66, 'cmd_remove')

d.label(0x938B, 'cmd_rename')

d.label(0xB359, 'cmd_wipe')


d.subroutine(0x92E6, 'cmd_fs_operation', title='Shared *Access/*Delete/*Info/*Lib command handler', description="""Copies the command name to the TX buffer, parses a
quoted filename argument via parse_quoted_arg, and
checks the access prefix. Validates the filename
does not start with '&', then falls through to
read_filename_char to copy remaining characters and
send the request. Raises 'Bad file name' if a bare
CR is found where a filename was expected.""")


d.subroutine(0x949E, 'cmd_bye', title='*Bye command handler', description="""Closes all open file control blocks via
process_all_fcbs, shuts down any *SPOOL/*EXEC files
with OSBYTE &77, and closes all network channels.
Falls through to save_net_tx_cb with function code
&17 to send the bye request to the file server.""")


d.subroutine(0xAD10, 'cmd_cdir', title='*CDir command handler', description="""Parses an optional allocation size argument: if absent,
defaults to index 2 (standard 19-entry directory, &200
bytes); if present, parses the decimal value and searches
a 26-entry threshold table to find the matching allocation
size index. Parses the directory name via parse_filename_arg,
copies it to the TX buffer, and sends FS command code &1B
to create the directory.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x93DD, 'cmd_dir', title='*Dir command handler', description="""Handles three argument syntaxes: a plain path
(delegates to pass_send_cmd), '&' alone for the root
directory, and '&N.dir' for cross-filesystem directory
changes. The cross-FS form sends a file server
selection command (code &12) to locate the target
server, raising 'Not found' on failure, then sends
the directory change (code 6) and calls
find_fs_and_exit to update the active FS context.""")


d.subroutine(0xAD6B, 'cmd_ex', title='*Ex command handler', description="""Unified handler for *Ex, *LCat, and *LEx. Sets the
library flag from carry (CLC for current, SEC for library).
Configures column format: 1 entry per line for Ex
(command 3), 3 per column for Cat (command &0B). Sends the
examine request (code &12), then prints the directory
header: title, cycle number, Owner/Public label, option
name, Dir. and Lib. paths. Paginates through entries,
printing each via ex_print_col_sep until the server
returns zero entries.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA356, 'cmd_flip', title='*Flip command handler', description="""Exchanges the CSD and CSL (library) handles.
Saves the current CSD handle (&0E03), loads the
library handle (&0E04) into Y, and calls
find_station_bit3 to install it as the new CSD.
Restores the original CSD handle and falls through
to flip_set_station_boot to install it as the new
library. Useful when files to be LOADed are in the
library and *DIR/*LIB would be inconvenient.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA07B, 'cmd_fs', title='*FS command handler', description="""Saves the current file server station address, then
checks for a command-line argument. With no argument,
falls through to print_current_fs to display the active
server. With an argument, parses the station number via
parse_fs_ps_args and issues OSWORD &13 (sub-function 1)
to select the new file server.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8D79, 'cmd_iam', title='*I AM command handler (file server logon)', description="""Closes any *SPOOL/*EXEC files via OSBYTE &77,
resets all file control blocks via
process_all_fcbs, then parses the command line
for an optional station number and file server
address. If a station number is present, stores
it and calls clear_if_station_match to validate.
Copies the logon command template from
cmd_table_nfs_iam into the transmit buffer and
sends via copy_arg_validated. Falls through to
cmd_pass for password entry.""")


d.subroutine(0xAD5F, 'cmd_lcat', title='*LCat command handler', description="""Sets the library flag by rotating SEC into bit 7 of
l1071, then branches to cat_set_lib_flag inside cmd_ex
to catalogue the library directory with three entries
per column.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xAD65, 'cmd_lex', title='*LEx command handler', description="""Sets the library flag by rotating SEC into bit 7 of
l1071, then branches to ex_set_lib_flag inside cmd_ex
to examine the library directory with one entry per line.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8DBC, 'cmd_pass', title='*PASS command handler (change password)', description="""Builds the FS command packet via copy_arg_to_buf_x0,
then scans the reply buffer for a ':' separator
indicating a password prompt. If found, reads
characters from the keyboard without echo, handling
Delete (&7F) for backspace and NAK (&15) to restart
from the colon position. Sends the completed
password to the file server via save_net_tx_cb and
branches to send_cmd_and_dispatch for the reply.""")


d.subroutine(0xAF66, 'cmd_remove', title='*Remove command handler', description="""Like *Delete but suppresses the 'Not found' error,
making it suitable for use in programs where a missing
file should not cause an unexpected error. Validates
that exactly one argument is present — raises 'Syntax'
if extra arguments follow. Parses the filename via
parse_filename_arg, copies it to the TX buffer, and
sends FS command code &14 with the V flag set via BIT
for save_net_tx_cb_vset dispatch.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x938B, 'cmd_rename', title='*Rename command handler', description="""Parses two space-separated filenames from the
command line, each with its own access prefix.
Sets the owner-only access mask before parsing each
name. Validates that both names resolve to the same
file server by comparing the FS options word —
raises 'Bad rename' if they differ. Falls through
to read_filename_char to copy the second filename
into the TX buffer and send the request.""")


d.subroutine(0xB359, 'cmd_wipe', title='*Wipe command handler', description="""Masks owner access, parses a wildcard filename, and
loops sending examine requests to the file server.
Skips locked files and non-empty directories. Shows
each filename with a '(Y/N/?) ' prompt — '?' shows
full file info with a '(Y/N) ' reprompt, 'Y' builds
the delete command in the TX buffer. Falls through to
flush_and_read_char on completion.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB431, 'prompt_yn', title='Print Y/N prompt and read user response', description="""Prints 'Y/N) ' via inline string, flushes
the input buffer, and reads a single character
from the keyboard.""", on_exit={'A': 'character read'})
d.entry(0x8B96)
d.entry(0x8B92)

d.label(0x8B96, 'help_net')

d.label(0x8B92, 'help_utils')


d.subroutine(0x8B96, 'help_net', title='*HELP NET topic handler', description="""Sets X to &4A (the NFS command sub-table offset)
and falls through to print_cmd_table to display
the NFS command list with version header.""")


d.subroutine(0x8B92, 'help_utils', title='*HELP UTILS topic handler', description="""Sets X=0 to select the utility command sub-table
and branches to print_cmd_table to display the
command list. Prints the version header followed
by all utility commands.""")
d.entry(0x8C33)
d.entry(0x92B5)
d.entry(0x9935)
d.entry(0x9BBE)
d.entry(0x9CD5)
d.entry(0x9E2F)
d.entry(0x9F6D)
d.entry(0xA8C5)
d.entry(0xA9E2)
d.entry(0xAAED)
d.entry(0xB7CE)
d.entry(0x854C)
for i in range(5):
    d.byte(0x853E + i)
d.expr(0x853E, '<(tx_done_jsr-1)')
d.expr(0x853F, '<(tx_done_econet_event-1)')
d.expr(0x8540, '<(tx_done_os_proc-1)')
d.expr(0x8541, '<(tx_done_halt-1)')
d.expr(0x8542, '<(tx_done_continue-1)')
d.entry(0x8689)
for i in range(8):
    d.byte(0x8681 + i)
d.expr(0x8681, '<(tx_ctrl_peek-1)')
d.expr(0x8682, '<(tx_ctrl_poke-1)')
d.expr(0x8683, '<(proc_op_status2-1)')
d.expr(0x8684, '<(proc_op_status2-1)')
d.expr(0x8685, '<(proc_op_status2-1)')
d.expr(0x8686, '<(tx_ctrl_exit-1)')
d.expr(0x8687, '<(tx_ctrl_exit-1)')
d.expr(0x8688, '<(tx_ctrl_machine_type-1)')
for i in range(16):
    d.byte(0x88E2 + i)
for i in range(3):
    d.byte(0x89C7 + i)
d.entry(0x84BB)
d.entry(0x84CB)
d.entry(0x88E2)
d.entry(0xA5A4)
d.entry(0xA619)
d.entry(0xA97A)
d.entry(0xB84D)
d.entry(0x0542)
d.entry(0x0564)
d.entry(0x05AB)
d.entry(0x05D3)


d.subroutine(0x8E61, 'fs_vector_table', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by loop_set_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the extended vector table.

Bytes 14-33: handler address pairs read by write_vector_entry.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (write_vector_entry writes the current ROM
bank number instead). The last entry (FSCV) has no padding
byte.""")
for i, name in enumerate(['FILEV', 'ARGSV', 'BGETV', 'BPUTV', 'GBPBV', 'FINDV', 'FSCV']):
    addr = 0x8E61 + i * 2
    d.word(addr)
    d.comment(addr, f'{name} dispatch (&FF{0x1B + i * 3:02X})', align=Align.INLINE)
handler_names = [('FILEV', 0x9935), ('ARGSV', 0x9BBE), ('BGETV', 0xB7CE), ('BPUTV', 0xB84D), ('GBPBV', 0x9E2F), ('FINDV', 0x9D4E), ('FSCV', 0x8E33)]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x8E6F + i * 3
    d.word(base_addr)
    d.comment(base_addr, f'{name} handler (&{handler_addr:04X})', align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, '(ROM bank — not read)', align=Align.INLINE)

d.label(0x8E59, 'ps_template_data')
d.byte(0x8E5F)
d.byte(0x8E60)

d.label(0x8E8A, 'netv_handler_addr')

d.label(0xA97A, 'netv_handler')
d.word(0x8E8A)
d.expr(0x8E8A, 'netv_handler')

d.label(0x9021, 'syntax_strings')

d.label(0x97B9, 'error_msg_table')

d.label(0x97C6, 'msg_net_error')

d.label(0x97D1, 'msg_station')

d.label(0x97DA, 'msg_no_clock')

d.label(0x97E4, 'msg_escape')

d.label(0x97EC, 'msg_bad_option')

d.label(0x97F8, 'msg_no_reply')

d.label(0x980F, 'msg_not_listening')

d.label(0x981E, 'msg_on_channel')

d.label(0x982A, 'msg_not_present')
d.byte(0x97B9)
d.byte(0x97DA)
d.byte(0x97DB)
d.byte(0x97E3)
d.byte(0x97E4)
d.byte(0x97EB)
d.byte(0x97EC)
d.byte(0x97F8)
d.byte(0x97F9)
d.byte(0x980E)
d.byte(0x981D)
d.byte(0x9829)
d.byte(0x9836)

d.label(0x8CA3, 'version_string')

d.label(0x8D39, 'credits_string')
d.byte(0x8D38)
d.comment(0x8D38, 'CR', align=Align.INLINE)
d.byte(0x8D51)
d.comment(0x8D51, 'CR', align=Align.INLINE)
d.byte(0x8D5C)
d.comment(0x8D5C, 'CR', align=Align.INLINE)
d.string(0x8D61, 2)
d.byte(0x8D63)
d.comment(0x8D63, 'CR', align=Align.INLINE)
d.byte(0x8D6F)
d.comment(0x8D6F, 'CR', align=Align.INLINE)
d.byte(0x8D77)
d.comment(0x8D77, 'CR', align=Align.INLINE)
d.byte(0x8D78)
d.comment(0x8D78, 'String terminator', align=Align.INLINE)

d.label(0xA3CE, 'boot_load_cmd')

d.label(0xA3D7, 'boot_exec_cmd')


d.subroutine(0x8E49, 'svc_dispatch', title='PHA/PHA/RTS table dispatch', description="""Computes a target index by incrementing X and
decrementing Y until Y goes negative, effectively
calculating X+Y+1. Pushes the target address
(high then low byte) from svc_dispatch_lo/hi
tables onto the stack, loads fs_options into X,
then returns via RTS to dispatch to the target
subroutine. Used for all service dispatch, FS
command execution, and OSBYTE handler routing.""", on_entry={'x': 'base dispatch index', 'y': 'additional offset'}, on_exit={'x': 'fs_options value'})

d.label(0x8E49, 'svc_dispatch')


d.subroutine(0x8AA0, 'read_paged_rom', title='Read next byte from paged ROM via OSRDSC', description="""Increments the read pointer at osrdsc_ptr (&F6)
first, then calls OSRDSC (&FFB9) with the ROM
number from error_block (&0100) in Y. Called
three times by service_handler during ROM
identification to read the copyright string and
ROM type byte.""", on_exit={'a': 'byte read from ROM'})

d.label(0x8AA0, 'read_paged_rom')


d.subroutine(0x8E83, 'osbyte_x0', title='OSBYTE wrapper with X=0, Y=&FF', description="""Sets X=0 and falls through to osbyte_yff to also
set Y=&FF. Provides a single call to execute
OSBYTE with A as the function code. Used by
adlc_init, init_adlc_and_vectors, and Econet
OSBYTE handling.""", on_entry={'a': 'OSBYTE function code'}, on_exit={'x': '0', 'y': '&FF'})


d.subroutine(0x8E85, 'osbyte_yff', title='OSBYTE wrapper with Y=&FF', description="""Sets Y=&FF and JMPs to the MOS OSBYTE entry
point. X must already be set by the caller. The
osbyte_x0 entry point falls through to here after
setting X=0.""", on_entry={'a': 'OSBYTE function code', 'x': 'OSBYTE X parameter'}, on_exit={'y': '&FF'})

d.label(0x8E83, 'osbyte_x0')

d.label(0x8E85, 'osbyte_yff')


d.subroutine(0x9145, 'print_inline', title='Print inline string, high-bit terminated', description="""Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. Common terminators are
&EA (NOP) for fall-through and &B8 (CLV) followed by BVC for an
unconditional forward branch.""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})
d.comment(0x9145, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x9148, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x914D, 'Advance pointer to next character', align=Align.INLINE)
d.comment(0x9153, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x9155, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x915D, 'Reload character (pointer may have been clobbered)', align=Align.INLINE)
d.comment(0x915F, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x916B, 'Jump to address of high-bit byte (resumes code)', align=Align.INLINE)


d.subroutine(0x96D4, 'error_inline', title='Generate BRK error from inline string', description="""Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""", on_entry={'a': 'error number'})
d.comment(0x96D4, 'Save error number in Y', align=Align.INLINE)
d.comment(0x96D5, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x96D8, 'Pop return address (high)', align=Align.INLINE)


d.subroutine(0x96D1, 'error_inline_log', title='Generate BRK error from inline string (with logging)', description="""Like error_inline, but first conditionally logs the error code to
workspace via sub_c95fb before building the error block.""", on_entry={'a': 'error number'})
d.comment(0x96D1, 'Conditionally log error code to workspace', align=Align.INLINE)


d.subroutine(0x96B8, 'error_bad_inline', title="Generate 'Bad ...' BRK error from inline string", description="""Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""", on_entry={'a': 'error number'})
d.comment(0x96B8, 'Conditionally log error code to workspace', align=Align.INLINE)
d.comment(0x96BB, 'Save error number in Y', align=Align.INLINE)
d.comment(0x96BC, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x96BD, 'Store return address low', align=Align.INLINE)
d.comment(0x96BF, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x96C0, 'Store return address high', align=Align.INLINE)
d.comment(0x96C2, 'X=0: start of prefix string', align=Align.INLINE)
d.comment(0x96C4, "Copy 'Bad ' prefix from lookup table", align=Align.INLINE)
d.comment(0x96C5, 'Get next prefix character', align=Align.INLINE)
d.comment(0x96C8, 'Store in error text buffer', align=Align.INLINE)
d.comment(0x96CB, "Is it space (end of 'Bad ')?", align=Align.INLINE)
d.comment(0x96CD, 'No: copy next prefix character', align=Align.INLINE)
d.comment(0x96DD, 'Store error number in error block', align=Align.INLINE)
d.comment(0x96E4, 'Zero the BRK byte at &0100', align=Align.INLINE)
d.comment(0x96E7, 'Copy inline string into error block', align=Align.INLINE)
d.comment(0x96E9, 'Read next byte from inline string', align=Align.INLINE)
d.comment(0x96EE, 'Loop until null terminator', align=Align.INLINE)
d.comment(0x96F0, 'Read receive attribute byte', align=Align.INLINE)

d.label(0x96B4, 'bad_prefix')
d.comment(0xAD10, 'Save command line offset', align=Align.INLINE)
d.comment(0xAD11, 'Push onto stack', align=Align.INLINE)
d.comment(0xAD12, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xAD15, 'Skip to optional size argument', align=Align.INLINE)
d.comment(0xAD18, 'End of line?', align=Align.INLINE)
d.comment(0xAD1A, 'No: parse size argument', align=Align.INLINE)
d.comment(0xAD1C, 'Default allocation size index = 2', align=Align.INLINE)
d.comment(0xAD20, 'A=&FF: mark as decimal parse', align=Align.INLINE)
d.comment(0xAD22, 'Store decimal parse flag', align=Align.INLINE)
d.comment(0xAD24, 'Parse numeric size argument', align=Align.INLINE)
d.comment(0xAD27, 'X=&1B: top of 26-entry size table', align=Align.INLINE)
d.comment(0xAD29, 'Try next lower index', align=Align.INLINE)
d.comment(0xAD2A, 'Compare size with threshold', align=Align.INLINE)
d.comment(0xAD2D, 'A < threshold: keep searching', align=Align.INLINE)
d.comment(0xAD2F, 'Store allocation size index', align=Align.INLINE)
d.comment(0xAD32, 'Restore command line offset', align=Align.INLINE)
d.comment(0xAD33, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAD34, 'Save text pointer for filename parse', align=Align.INLINE)
d.comment(0xAD37, 'Parse directory name argument', align=Align.INLINE)
d.comment(0xAD3A, 'X=1: one argument to copy', align=Align.INLINE)
d.comment(0xAD3C, 'Copy directory name to TX buffer', align=Align.INLINE)
d.comment(0xAD3F, 'Y=&1B: *CDir FS command code', align=Align.INLINE)
d.comment(0xAD41, 'Send command to file server', align=Align.INLINE)
d.comment(0xAD44, """*CDir allocation size threshold table

26 thresholds dividing 0-255 into size classes.
Table base (cdir_dispatch_col+2) overlaps with
the JMP high byte (entry 0, never reached). Searched
from index 26 down to 0; the result index (1-26)
is stored as the directory allocation size class.
Default when no size argument given: index 2.""")
d.comment(0xAD44, 'Index 1: threshold 0 (catch-all)', align=Align.INLINE)
d.comment(0xAD45, 'Index 2: threshold 10 (default)', align=Align.INLINE)
d.comment(0xAD46, 'Index 3: threshold 20', align=Align.INLINE)
d.comment(0xAD47, 'Index 4: threshold 29', align=Align.INLINE)
d.comment(0xAD48, 'Index 5: threshold 39', align=Align.INLINE)
d.comment(0xAD49, 'Index 6: threshold 49', align=Align.INLINE)
d.comment(0xAD4A, 'Index 7: threshold 59', align=Align.INLINE)
d.comment(0xAD4B, 'Index 8: threshold 69', align=Align.INLINE)
d.comment(0xAD4C, 'Index 9: threshold 79', align=Align.INLINE)
d.comment(0xAD4D, 'Index 10: threshold 88', align=Align.INLINE)
d.comment(0xAD4E, 'Index 11: threshold 98', align=Align.INLINE)
d.comment(0xAD4F, 'Index 12: threshold 108', align=Align.INLINE)
d.comment(0xAD50, 'Index 13: threshold 118', align=Align.INLINE)
d.comment(0xAD51, 'Index 14: threshold 128', align=Align.INLINE)
d.comment(0xAD52, 'Index 15: threshold 138', align=Align.INLINE)
d.comment(0xAD53, 'Index 16: threshold 148', align=Align.INLINE)
d.comment(0xAD54, 'Index 17: threshold 157', align=Align.INLINE)
d.comment(0xAD55, 'Index 18: threshold 167', align=Align.INLINE)
d.comment(0xAD56, 'Index 19: threshold 177', align=Align.INLINE)
d.comment(0xAD57, 'Index 20: threshold 187', align=Align.INLINE)
d.comment(0xAD58, 'Index 21: threshold 197', align=Align.INLINE)
d.comment(0xAD59, 'Index 22: threshold 207', align=Align.INLINE)
d.comment(0xAD5A, 'Index 23: threshold 216', align=Align.INLINE)
d.comment(0xAD5B, 'Index 24: threshold 226', align=Align.INLINE)
d.comment(0xAD5C, 'Index 25: threshold 236', align=Align.INLINE)
d.comment(0xAD5D, 'Index 26: threshold 246', align=Align.INLINE)
d.comment(0xAD5E, 'Unused (index 27, never accessed)', align=Align.INLINE)
d.comment(0xAD5F, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD62, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xAD65, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD68, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xB30C, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB30E, 'Compare with CR (end of line)', align=Align.INLINE)
d.comment(0xB310, 'Not CR: attribute keywords follow', align=Align.INLINE)
d.comment(0xB312, 'A=&FF: protect all attributes', align=Align.INLINE)
d.comment(0xB316, 'Load current protection mask', align=Align.INLINE)
d.comment(0xB319, 'Save as starting value', align=Align.INLINE)
d.comment(0xB31A, 'X=&D3: attribute keyword table offset', align=Align.INLINE)
d.comment(0xB31C, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB31E, 'Save for end-of-args check', align=Align.INLINE)
d.comment(0xB320, 'Match attribute keyword in table', align=Align.INLINE)
d.comment(0xB323, 'No match: check if end of arguments', align=Align.INLINE)
d.comment(0xB325, 'Retrieve accumulated mask', align=Align.INLINE)
d.comment(0xB326, 'OR in attribute bit for keyword', align=Align.INLINE)
d.comment(0xB329, 'Save updated mask', align=Align.INLINE)
d.comment(0xB32A, 'Always non-zero after ORA: loop', align=Align.INLINE)
d.comment(0xB32C, 'Get the unmatched character', align=Align.INLINE)
d.comment(0xB32E, 'Is it CR?', align=Align.INLINE)
d.comment(0xB330, 'Yes: arguments ended correctly', align=Align.INLINE)
d.comment(0xB332, 'No: invalid attribute keyword', align=Align.INLINE)
d.comment(0xB335, 'Retrieve final protection mask', align=Align.INLINE)
d.comment(0xB336, 'Store protection mask', align=Align.INLINE)
d.comment(0xB339, 'Store protection mask copy', align=Align.INLINE)
d.comment(0xB33C, 'Return', align=Align.INLINE)
d.comment(0xB33D, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB33F, 'Compare with CR (end of line)', align=Align.INLINE)
d.comment(0xB341, 'No args: A=0 clears all protection', align=Align.INLINE)
d.comment(0xB343, 'Load current protection mask', align=Align.INLINE)
d.comment(0xB346, 'Save as starting value', align=Align.INLINE)
d.comment(0xB347, 'X=&D3: attribute keyword table offset', align=Align.INLINE)
d.comment(0xB349, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB34B, 'Save for end-of-args check', align=Align.INLINE)
d.comment(0xB34D, 'Match attribute keyword in table', align=Align.INLINE)
d.comment(0xB350, 'No match: check if end of arguments', align=Align.INLINE)
d.comment(0xB352, 'Retrieve accumulated mask', align=Align.INLINE)
d.comment(0xB353, 'AND to clear matched attribute bit', align=Align.INLINE)
d.comment(0xB356, 'Save updated mask', align=Align.INLINE)
d.comment(0x92E6, 'Copy command name to TX buffer', align=Align.INLINE)
d.comment(0x92E9, 'Save buffer position', align=Align.INLINE)
d.comment(0x92EA, 'Push it', align=Align.INLINE)
d.comment(0x92EB, 'Parse filename (handles quoting)', align=Align.INLINE)
d.comment(0x92EE, 'Parse owner/public access prefix', align=Align.INLINE)
d.comment(0x92F1, 'Restore buffer position', align=Align.INLINE)
d.comment(0x92F2, 'Transfer to X', align=Align.INLINE)
d.comment(0x92F3, "Reject '&' character in filename", align=Align.INLINE)
d.comment(0x92F6, 'End of line?', align=Align.INLINE)
d.comment(0x92F8, 'No: copy filename chars to buffer', align=Align.INLINE)
d.comment(0x92FA, 'Error number &CC', align=Align.INLINE)
d.comment(0x92FC, "Raise 'Bad file name' error", align=Align.INLINE)
d.comment(0x9309, 'Load first parsed character', align=Align.INLINE)
d.comment(0x930C, "Is it '&'?", align=Align.INLINE)
d.comment(0x930E, 'Yes: invalid filename', align=Align.INLINE)
d.comment(0x9310, 'Return', align=Align.INLINE)
d.comment(0x9311, "Reject '&' in current char", align=Align.INLINE)
d.comment(0x9314, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x9317, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9318, 'End of line?', align=Align.INLINE)
d.comment(0x931A, 'Yes: send request to file server', align=Align.INLINE)
d.comment(0x931C, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x931F, 'Continue reading filename chars', align=Align.INLINE)
d.comment(0x9322, 'Y=0: no extra dispatch offset', align=Align.INLINE)
d.comment(0x9324, 'Send command and dispatch reply', align=Align.INLINE)
d.comment(0x9327, 'Save command line offset', align=Align.INLINE)
d.comment(0x9328, 'Push it', align=Align.INLINE)
d.comment(0x9329, 'Scan backwards in command table', align=Align.INLINE)
d.comment(0x932A, 'Load table byte', align=Align.INLINE)
d.comment(0x932D, 'Bit 7 clear: keep scanning', align=Align.INLINE)
d.comment(0x932F, 'Point past flag byte to name start', align=Align.INLINE)
d.comment(0x9330, 'Y=0: TX buffer offset', align=Align.INLINE)
d.comment(0x9332, 'Load command name character', align=Align.INLINE)
d.comment(0x9335, 'Bit 7 set: end of name', align=Align.INLINE)
d.comment(0x9337, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x933A, 'Advance table pointer', align=Align.INLINE)
d.comment(0x933B, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x933C, 'Continue copying name', align=Align.INLINE)
d.comment(0x933E, 'Space separator', align=Align.INLINE)
d.comment(0x9340, 'Append space after command name', align=Align.INLINE)
d.comment(0x9343, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9344, 'Transfer length to A', align=Align.INLINE)
d.comment(0x9345, 'And to X (buffer position)', align=Align.INLINE)
d.comment(0x9346, 'Restore command line offset', align=Align.INLINE)
d.comment(0x9347, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9348, 'Return', align=Align.INLINE)
d.comment(0x9349, 'A=0: no quote mode', align=Align.INLINE)
d.comment(0x934C, 'Clear quote tracking flag', align=Align.INLINE)
d.comment(0x934F, 'Load char from command line', align=Align.INLINE)
d.comment(0x9351, 'Space?', align=Align.INLINE)
d.comment(0x9353, 'No: check for opening quote', align=Align.INLINE)
d.comment(0x9355, 'Skip leading space', align=Align.INLINE)
d.comment(0x9356, 'Continue skipping spaces', align=Align.INLINE)
d.comment(0x9358, 'Double-quote character?', align=Align.INLINE)
d.comment(0x935A, 'No: start reading filename', align=Align.INLINE)
d.comment(0x935C, 'Skip opening quote', align=Align.INLINE)
d.comment(0x935D, 'Toggle quote mode flag', align=Align.INLINE)
d.comment(0x9360, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x9363, 'Load char from command line', align=Align.INLINE)
d.comment(0x9365, 'Double-quote?', align=Align.INLINE)
d.comment(0x9367, 'No: store character as-is', align=Align.INLINE)
d.comment(0x9369, 'Toggle quote mode', align=Align.INLINE)
d.comment(0x936C, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x936F, 'Replace closing quote with space', align=Align.INLINE)
d.comment(0x9371, 'Store character in parse buffer', align=Align.INLINE)
d.comment(0x9374, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x9375, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9376, 'End of line?', align=Align.INLINE)
d.comment(0x9378, 'No: continue parsing', align=Align.INLINE)
d.comment(0x937A, 'Check quote balance flag', align=Align.INLINE)
d.comment(0x937D, 'Balanced: return OK', align=Align.INLINE)
d.comment(0x937F, 'Unbalanced: use BRK ptr for error', align=Align.INLINE)
d.comment(0x9381, "Raise 'Bad string' error", align=Align.INLINE)
d.comment(0x938B, "Copy 'Rename ' to TX buffer", align=Align.INLINE)
d.comment(0x938E, 'Save buffer position', align=Align.INLINE)
d.comment(0x938F, 'Push it', align=Align.INLINE)
d.comment(0x9390, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9393, 'Parse first filename (quoted)', align=Align.INLINE)
d.comment(0x9396, 'Parse access prefix', align=Align.INLINE)
d.comment(0x9399, 'Restore buffer position', align=Align.INLINE)
d.comment(0x939A, 'Transfer to X', align=Align.INLINE)
d.comment(0x939B, 'Load next parsed character', align=Align.INLINE)
d.comment(0x939E, 'End of line?', align=Align.INLINE)
d.comment(0x93A0, 'No: store character', align=Align.INLINE)
d.comment(0x93A2, 'Error number &B0', align=Align.INLINE)
d.comment(0x93A4, "Raise 'Bad rename' error", align=Align.INLINE)
d.comment(0x93AE, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x93B1, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x93B2, 'Space (name separator)?', align=Align.INLINE)
d.comment(0x93B4, 'Yes: first name complete', align=Align.INLINE)
d.comment(0x93B6, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x93B9, 'Continue copying first filename', align=Align.INLINE)
d.comment(0x93BC, 'Strip token from next char', align=Align.INLINE)
d.comment(0x93BF, 'Load next parsed character', align=Align.INLINE)
d.comment(0x93C2, 'Still a space?', align=Align.INLINE)
d.comment(0x93C4, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0x93C6, 'Save current FS options', align=Align.INLINE)
d.comment(0x93C9, 'Push them', align=Align.INLINE)
d.comment(0x93CA, 'Reset access mask for second name', align=Align.INLINE)
d.comment(0x93CD, 'Save buffer position', align=Align.INLINE)
d.comment(0x93CE, 'Push it', align=Align.INLINE)
d.comment(0x93CF, 'Parse access prefix for second name', align=Align.INLINE)
d.comment(0x93D2, 'Restore buffer position', align=Align.INLINE)
d.comment(0x93D3, 'Transfer to X', align=Align.INLINE)
d.comment(0x93D4, 'Restore original FS options', align=Align.INLINE)
d.comment(0x93D5, 'Options changed (cross-FS)?', align=Align.INLINE)
d.comment(0x93D8, "Yes: error (can't rename across FS)", align=Align.INLINE)
d.comment(0x93DA, 'Copy second filename and send', align=Align.INLINE)
d.comment(0x93DD, 'Get first char of argument', align=Align.INLINE)
d.comment(0x93DF, "Is it '&' (FS selector prefix)?", align=Align.INLINE)
d.comment(0x93E1, 'No: simple dir change', align=Align.INLINE)
d.comment(0x93E3, "Skip '&'", align=Align.INLINE)
d.comment(0x93E4, "Get char after '&'", align=Align.INLINE)
d.comment(0x93E6, 'End of line?', align=Align.INLINE)
d.comment(0x93E8, "Yes: '&' alone (root directory)", align=Align.INLINE)
d.comment(0x93EA, 'Space?', align=Align.INLINE)
d.comment(0x93EC, "No: check for '.' separator", align=Align.INLINE)
d.comment(0x93EE, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x93F0, 'Advance index', align=Align.INLINE)
d.comment(0x93F1, 'Load char from command line', align=Align.INLINE)
d.comment(0x93F3, 'Copy to TX buffer', align=Align.INLINE)
d.comment(0x93F6, "Is it '&' (end of FS path)?", align=Align.INLINE)
d.comment(0x93F8, 'No: keep copying', align=Align.INLINE)
d.comment(0x93FA, "Replace '&' with CR terminator", align=Align.INLINE)
d.comment(0x93FC, 'Store CR in buffer', align=Align.INLINE)
d.comment(0x93FF, 'Point past CR', align=Align.INLINE)
d.comment(0x9400, 'Transfer length to A', align=Align.INLINE)
d.comment(0x9401, 'And to X (byte count)', align=Align.INLINE)
d.comment(0x9402, 'Send directory request to server', align=Align.INLINE)
d.comment(0x9405, "Is char after '&' a dot?", align=Align.INLINE)
d.comment(0x9407, 'Yes: &FS.dir format', align=Align.INLINE)
d.comment(0x9409, 'No: invalid syntax', align=Align.INLINE)
d.comment(0x940C, "Skip '.'", align=Align.INLINE)
d.comment(0x940D, 'Save dir path start position', align=Align.INLINE)
d.comment(0x940F, 'FS command 4: examine directory', align=Align.INLINE)
d.comment(0x9411, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x9414, 'Load FS flags', align=Align.INLINE)
d.comment(0x9417, 'Set bit 6 (FS selection active)', align=Align.INLINE)
d.comment(0x9419, 'Store updated flags', align=Align.INLINE)
d.comment(0x941C, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x941E, 'Copy FS number to buffer', align=Align.INLINE)
d.comment(0x9421, 'Y=&12: select FS command code', align=Align.INLINE)
d.comment(0x9423, 'Send FS selection command', align=Align.INLINE)
d.comment(0x9426, 'Load reply status', align=Align.INLINE)
d.comment(0x9429, 'Status 2 (found)?', align=Align.INLINE)
d.comment(0x942B, 'Yes: proceed to dir change', align=Align.INLINE)
d.comment(0x942D, 'Error number &D6', align=Align.INLINE)
d.comment(0x942F, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0x943C, 'Load current FS station byte', align=Align.INLINE)
d.comment(0x943F, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x9442, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9444, 'Y=7: change directory command code', align=Align.INLINE)
d.comment(0x9446, 'Send directory change request', align=Align.INLINE)
d.comment(0x9449, 'X=1', align=Align.INLINE)
d.comment(0x944B, 'Store start marker in buffer', align=Align.INLINE)
d.comment(0x944E, 'Store start marker in buffer+1', align=Align.INLINE)
d.comment(0x9452, 'Restore dir path start position', align=Align.INLINE)
d.comment(0x9454, 'Copy directory path to buffer', align=Align.INLINE)
d.comment(0x9457, 'Y=6: set directory command code', align=Align.INLINE)
d.comment(0x9459, 'Send set directory command', align=Align.INLINE)
d.comment(0x945C, 'Load reply handle', align=Align.INLINE)
d.comment(0x945F, 'Select FS and return', align=Align.INLINE)
d.comment(0x9462, 'Simple: pass command to FS', align=Align.INLINE)
d.comment(0x9465, 'A=&90: bye command port', align=Align.INLINE)
d.comment(0x9467, 'Initialise TXCB from template', align=Align.INLINE)
d.comment(0x946A, 'Set transmit port', align=Align.INLINE)
d.comment(0x946C, 'A=3: data start offset', align=Align.INLINE)
d.comment(0x946E, 'Set TXCB start offset', align=Align.INLINE)
d.comment(0x9470, 'Open receive: &80->&7F (bit 7 clear = awaiting reply)', align=Align.INLINE)
d.comment(0x9472, 'Return', align=Align.INLINE)
d.comment(0x9473, 'Save A', align=Align.INLINE)
d.comment(0x9474, 'Y=&0B: template size - 1', align=Align.INLINE)
d.comment(0x9476, 'Load byte from TXCB template', align=Align.INLINE)
d.comment(0x9479, 'Store to TXCB workspace', align=Align.INLINE)
d.comment(0x947C, 'Index >= 2?', align=Align.INLINE)
d.comment(0x947E, 'Yes: skip dest station copy', align=Align.INLINE)
d.comment(0x9480, 'Load dest station byte', align=Align.INLINE)
d.comment(0x9483, 'Store to TXCB destination', align=Align.INLINE)
d.comment(0x9486, 'Decrement index', align=Align.INLINE)
d.comment(0x9487, 'More bytes: continue', align=Align.INLINE)
d.comment(0x9489, 'Restore A', align=Align.INLINE)
d.comment(0x948A, 'Return', align=Align.INLINE)
d.comment(0x9497, 'Save A', align=Align.INLINE)
d.comment(0x9498, 'Set carry (read-only mode)', align=Align.INLINE)
d.comment(0x949B, 'Clear V', align=Align.INLINE)
d.comment(0xA356, 'Load current CSD handle', align=Align.INLINE)
d.comment(0xA359, 'Save CSD handle', align=Align.INLINE)
d.comment(0xA35A, 'Load library handle into Y', align=Align.INLINE)
d.comment(0xA35D, 'Install library as new CSD', align=Align.INLINE)
d.comment(0xA360, 'Restore original CSD handle', align=Align.INLINE)
d.comment(0xA361, 'Y = original CSD (becomes library)', align=Align.INLINE)
d.comment(0xA362, 'X=&10: max 16 station entries', align=Align.INLINE)
d.comment(0xA364, 'Clear V (no match found yet)', align=Align.INLINE)
d.comment(0xA365, 'Decrement station index', align=Align.INLINE)
d.comment(0xA366, 'All searched: exit loop', align=Align.INLINE)
d.comment(0xA368, 'Check if station[X] matches', align=Align.INLINE)
d.comment(0xA36B, 'No match: try next station', align=Align.INLINE)
d.comment(0xA36D, 'Load station flags byte', align=Align.INLINE)
d.comment(0xA370, 'Test bit 4 (active flag)', align=Align.INLINE)
d.comment(0xA372, 'Not active: try next station', align=Align.INLINE)
d.comment(0xA374, 'Transfer boot type to A', align=Align.INLINE)
d.comment(0xA375, 'Store boot setting for station', align=Align.INLINE)
d.comment(0xA378, 'Set V flag (station match found)', align=Align.INLINE)
d.comment(0xA37B, 'Store boot type', align=Align.INLINE)
d.comment(0xA37E, 'V set (matched): skip allocation', align=Align.INLINE)
d.comment(0xA380, 'Boot type to A', align=Align.INLINE)
d.comment(0xA381, 'Allocate FCB slot for new entry', align=Align.INLINE)
d.comment(0xA384, 'Store allocation result', align=Align.INLINE)
d.comment(0xA387, 'Zero: allocation failed, exit', align=Align.INLINE)
d.comment(0xA389, 'A=&32: station flags (active+boot)', align=Align.INLINE)
d.comment(0xA38B, 'Store station flags', align=Align.INLINE)
d.comment(0xA38E, 'Restore FS context and return', align=Align.INLINE)
d.comment(0xA391, 'Close all network channels', align=Align.INLINE)
d.comment(0xA394, 'Set carry flag', align=Align.INLINE)
d.comment(0xA395, 'Load reply boot type', align=Align.INLINE)
d.comment(0xA398, 'Store as current boot type', align=Align.INLINE)
d.comment(0xA39B, 'Save processor status', align=Align.INLINE)
d.comment(0xA39C, 'Load station number from reply', align=Align.INLINE)
d.comment(0xA39F, 'Find station entry with bit 2', align=Align.INLINE)
d.comment(0xA3A2, 'Load network number from reply', align=Align.INLINE)
d.comment(0xA3A5, 'Find station entry with bit 3', align=Align.INLINE)
d.comment(0xA3A8, 'Load boot type from reply', align=Align.INLINE)
d.comment(0xA3AB, 'Set boot config for station', align=Align.INLINE)
d.comment(0xA3AE, 'Restore processor status', align=Align.INLINE)
d.comment(0xA3AF, 'Carry set: proceed with boot', align=Align.INLINE)
d.comment(0xA3B1, 'Return with last flag', align=Align.INLINE)
d.comment(0xA3B4, 'Load config flags', align=Align.INLINE)
d.comment(0xA3B7, 'Save copy in X', align=Align.INLINE)
d.comment(0xA3B8, 'Test bit 2 (auto-boot flag)', align=Align.INLINE)
d.comment(0xA3BA, 'Save bit 2 test result', align=Align.INLINE)
d.comment(0xA3BB, 'Restore full flags', align=Align.INLINE)
d.comment(0xA3BC, 'Clear bit 2 (consume flag)', align=Align.INLINE)
d.comment(0xA3BE, 'Store cleared flags', align=Align.INLINE)
d.comment(0xA3C1, 'Restore bit 2 test result', align=Align.INLINE)
d.comment(0xA3C2, 'Bit 2 was set: skip to boot cmd', align=Align.INLINE)
d.comment(0xA3C4, 'OSBYTE &79: scan keyboard', align=Align.INLINE)
d.comment(0xA3CC, 'CTRL not pressed: proceed to boot', align=Align.INLINE)
d.comment(0xA3CE, 'CTRL pressed: cancel boot, return', align=Align.INLINE)
d.comment(0xA3DF, """Boot option OSCLI address table

Low bytes of boot command string addresses,
all in page &A3. Indexed by boot option 0-3
(option 0 is never reached due to BEQ).
Entry 2 reuses the tail of 'L.!BOOT' to
get '!BOOT' (*RUN equivalent).""")
d.comment(0xA3E3, 'Load boot type', align=Align.INLINE)
d.comment(0xA3E6, 'Type 0: no command, just return', align=Align.INLINE)
d.comment(0xA3E8, 'Look up boot command address low', align=Align.INLINE)
d.comment(0xA3EB, 'Boot command address high (&A3xx)', align=Align.INLINE)
d.comment(0xA3ED, 'Execute boot command via OSCLI', align=Align.INLINE)
d.comment(0xAF66, 'Save command line offset', align=Align.INLINE)
d.comment(0xAF67, 'Push onto stack', align=Align.INLINE)
d.comment(0xAF68, 'Skip to check for extra arguments', align=Align.INLINE)
d.comment(0xAF6B, 'End of line?', align=Align.INLINE)
d.comment(0xAF6D, 'Yes: single arg, proceed', align=Align.INLINE)
d.comment(0xAF6F, 'No: extra args, syntax error', align=Align.INLINE)
d.comment(0xAF72, 'Restore command line offset', align=Align.INLINE)
d.comment(0xAF73, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAF74, 'Save text pointer for parsing', align=Align.INLINE)
d.comment(0xAF77, 'Parse filename argument', align=Align.INLINE)
d.comment(0xAF7A, 'Copy filename to TX buffer', align=Align.INLINE)
d.comment(0xAF7D, 'Y=&14: *Delete FS command code', align=Align.INLINE)
d.comment(0xAF7F, 'Set V flag (via BIT #&FF)', align=Align.INLINE)
d.comment(0xAF82, 'Send to FS with V-flag dispatch', align=Align.INLINE)
d.comment(0xAF85, 'Set V (suppress leading zeros)', align=Align.INLINE)
d.comment(0xAF88, 'Transfer value to Y (remainder)', align=Align.INLINE)
d.comment(0xAF89, 'A=100: hundreds divisor', align=Align.INLINE)
d.comment(0xAF8B, 'Print hundreds digit', align=Align.INLINE)
d.comment(0xAF8E, 'A=10: tens divisor', align=Align.INLINE)
d.comment(0xAF90, 'Print tens digit', align=Align.INLINE)
d.comment(0xAF93, 'Clear V (always print units)', align=Align.INLINE)
d.comment(0xAF94, 'A=1: units divisor', align=Align.INLINE)
d.comment(0xAF96, 'Store divisor', align=Align.INLINE)
d.comment(0xAF98, 'Get remaining value', align=Align.INLINE)
d.comment(0xAF99, "X='0'-1: digit counter", align=Align.INLINE)
d.comment(0xAF9B, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xAF9C, 'Save V flag for leading zero check', align=Align.INLINE)
d.comment(0xAF9D, 'Count quotient digit', align=Align.INLINE)
d.comment(0xAF9E, 'Subtract divisor', align=Align.INLINE)
d.comment(0xAFA0, 'No underflow: continue dividing', align=Align.INLINE)
d.comment(0xAFA2, 'Add back divisor (get remainder)', align=Align.INLINE)
d.comment(0xAFA4, 'Remainder to Y for next digit', align=Align.INLINE)
d.comment(0xAFA5, 'Digit character to A', align=Align.INLINE)
d.comment(0xAFA6, 'Restore V flag', align=Align.INLINE)
d.comment(0xAFA7, 'V clear: always print digit', align=Align.INLINE)
d.comment(0xAFA9, "V set: is digit '0'?", align=Align.INLINE)
d.comment(0xAFAB, 'Yes: suppress leading zero', align=Align.INLINE)
d.comment(0xAFAD, 'Save divisor across OSASCI call', align=Align.INLINE)
d.comment(0xAFB2, 'Restore divisor', align=Align.INLINE)
d.comment(0xAFB4, 'Return', align=Align.INLINE)
d.comment(0xAFB5, 'Save A', align=Align.INLINE)
d.comment(0xAFB6, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xAFB8, 'To OS text pointer low', align=Align.INLINE)
d.comment(0xAFBA, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xAFBC, 'To OS text pointer high', align=Align.INLINE)
d.comment(0xAFBE, 'Restore A', align=Align.INLINE)
d.comment(0xAFBF, 'Return', align=Align.INLINE)
d.comment(0xAFC0, 'Advance past current character', align=Align.INLINE)
d.comment(0xAFC1, 'Load char from command line', align=Align.INLINE)
d.comment(0xAFC3, 'Space?', align=Align.INLINE)
d.comment(0xAFC5, 'Yes: skip trailing spaces', align=Align.INLINE)
d.comment(0xAFC7, 'CR (end of line)?', align=Align.INLINE)
d.comment(0xAFC9, 'Yes: return (at end)', align=Align.INLINE)
d.comment(0xAFCD, 'Advance past space', align=Align.INLINE)
d.comment(0xAFCE, 'Load next character', align=Align.INLINE)
d.comment(0xAFD0, 'Still a space?', align=Align.INLINE)
d.comment(0xAFD2, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0xAFD4, 'Return (at next argument)', align=Align.INLINE)
d.comment(0xAFD5, 'Save A', align=Align.INLINE)
d.comment(0xAFD6, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xAFD8, 'To spool buffer pointer low', align=Align.INLINE)
d.comment(0xAFDA, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xAFDC, 'To spool buffer pointer high', align=Align.INLINE)
d.comment(0xAFDE, 'Restore A', align=Align.INLINE)
d.comment(0xAFDF, 'Return', align=Align.INLINE)
d.comment(0xAFE0, 'Save Y', align=Align.INLINE)
d.comment(0xAFE1, 'Push it', align=Align.INLINE)
d.comment(0xAFE2, 'Get workspace page number', align=Align.INLINE)
d.comment(0xAFE5, 'Store as spool drive page high', align=Align.INLINE)
d.comment(0xAFE7, 'Restore Y', align=Align.INLINE)
d.comment(0xAFE8, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAFE9, 'A=0', align=Align.INLINE)
d.comment(0xAFEB, 'Clear spool drive page low', align=Align.INLINE)
d.comment(0xAFED, 'Return', align=Align.INLINE)
d.comment(0xB994, 'A=0: close all open files', align=Align.INLINE)
d.comment(0xB99A, 'Clear V for unconditional BVC', align=Align.INLINE)
d.comment(0xB99D, 'Set V flag (= print mode)', align=Align.INLINE)
d.comment(0xB9A0, 'Open file for reading', align=Align.INLINE)
d.comment(0xB9A5, 'A = 0', align=Align.INLINE)
d.comment(0xB9A7, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB9A9, 'Save V flag (print/type mode)', align=Align.INLINE)
d.comment(0xB9AD, 'Branch if not end of file', align=Align.INLINE)
d.comment(0xB9AF, 'EOF: restore processor status', align=Align.INLINE)
d.comment(0xB9B0, 'Close the file', align=Align.INLINE)
d.comment(0xB9B6, 'Check for escape key pressed', align=Align.INLINE)
d.comment(0xB9B9, 'Restore V (print/type mode)', align=Align.INLINE)
d.comment(0xB9BA, 'Re-save for next iteration', align=Align.INLINE)
d.comment(0xB9BB, 'Print mode: skip CR/LF handling', align=Align.INLINE)
d.comment(0xB9BD, 'Is it a carriage return?', align=Align.INLINE)
d.comment(0xB9BF, 'Yes: handle line ending', align=Align.INLINE)
d.comment(0xB9C1, 'Is it a line feed?', align=Align.INLINE)
d.comment(0xB9C3, 'Yes: handle line ending', align=Align.INLINE)
d.comment(0xB9C5, 'Save as previous character', align=Align.INLINE)
d.comment(0xB9CA, 'Loop for next byte', align=Align.INLINE)
d.comment(0xB9CD, 'Save the CR or LF character', align=Align.INLINE)
d.comment(0xB9CE, 'Check output destination flag', align=Align.INLINE)
d.comment(0xB9D1, 'Zero: normalise line endings', align=Align.INLINE)
d.comment(0xB9D3, 'Non-zero: output raw', align=Align.INLINE)
d.comment(0xB9D5, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB9D7, 'Retrieve CR/LF', align=Align.INLINE)
d.comment(0xB9D8, 'Output it directly; ALWAYS branch', align=Align.INLINE)
d.comment(0xB9DA, 'Get previous character', align=Align.INLINE)
d.comment(0xB9DC, 'Was previous a CR?', align=Align.INLINE)
d.comment(0xB9DE, 'Yes: check for CR+LF pair', align=Align.INLINE)
d.comment(0xB9E0, 'Was previous a LF?', align=Align.INLINE)
d.comment(0xB9E2, 'Yes: check for LF+CR pair', align=Align.INLINE)
d.comment(0xB9E4, 'Retrieve CR/LF from stack', align=Align.INLINE)
d.comment(0xB9E5, 'Save as previous character', align=Align.INLINE)
d.comment(0xB9EA, 'Loop for next byte', align=Align.INLINE)
d.comment(0xB9ED, 'Retrieve current character', align=Align.INLINE)
d.comment(0xB9EE, 'Is it LF? (CR+LF pair)', align=Align.INLINE)
d.comment(0xB9F0, 'Yes: consume LF, no extra newline', align=Align.INLINE)
d.comment(0xB9F2, 'No: output extra newline', align=Align.INLINE)
d.comment(0xB9F4, 'Retrieve current character', align=Align.INLINE)
d.comment(0xB9F5, 'Is it CR? (LF+CR pair)', align=Align.INLINE)
d.comment(0xB9F7, 'No: output extra newline', align=Align.INLINE)
d.comment(0xB9F9, 'Pair consumed: A = 0', align=Align.INLINE)
d.comment(0xB9FB, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB9FD, 'Loop for next byte; ALWAYS branch', align=Align.INLINE)
d.comment(0xB9FF, 'Test bit 7 of escape flag', align=Align.INLINE)
d.comment(0xBA01, 'Escape pressed: handle abort', align=Align.INLINE)
d.comment(0xBA03, 'No escape: return', align=Align.INLINE)
d.comment(0xBA04, 'Close the open file', align=Align.INLINE)
d.comment(0xBA0A, 'Acknowledge escape condition', align=Align.INLINE)
d.comment(0xBA0F, 'Error number &11', align=Align.INLINE)
d.comment(0xBA11, "Generate 'Escape' BRK error", align=Align.INLINE)
d.comment(0xB1C3, 'Save command line pointer high', align=Align.INLINE)
d.comment(0xB1C5, 'Initialise spool/print drive', align=Align.INLINE)
d.comment(0xB1C8, 'Save spool drive number', align=Align.INLINE)
d.comment(0xB1CA, 'Copy PS name to TX buffer', align=Align.INLINE)
d.comment(0xB1CD, 'Init PS slot from RX data', align=Align.INLINE)
d.comment(0xB1D0, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB1D2, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xB1D5, 'Get first argument character', align=Align.INLINE)
d.comment(0xB1D7, 'End of command line?', align=Align.INLINE)
d.comment(0xB1D9, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xB1DB, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xB1DC, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xB1DF, 'Yes: station number, skip PS name', align=Align.INLINE)
d.comment(0xB1E1, 'PS name follows', align=Align.INLINE)
d.comment(0xB1E2, 'Save Y', align=Align.INLINE)
d.comment(0xB1E3, 'Load PS server address', align=Align.INLINE)
d.comment(0xB1E6, 'Restore Y', align=Align.INLINE)
d.comment(0xB1E7, 'Back to Y register', align=Align.INLINE)
d.comment(0xB1E8, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xB1EB, 'Offset &7A in slot buffer', align=Align.INLINE)
d.comment(0xB1ED, 'Get parsed station low', align=Align.INLINE)
d.comment(0xB1EF, 'Store station number low', align=Align.INLINE)
d.comment(0xB1F2, 'Get parsed network number', align=Align.INLINE)
d.comment(0xB1F4, 'Store station number high', align=Align.INLINE)
d.comment(0xB1F6, 'Offset &14 in TX buffer', align=Align.INLINE)
d.comment(0xB1F8, 'Copy PS data to TX buffer', align=Align.INLINE)
d.comment(0xB1FB, 'Get buffer page high', align=Align.INLINE)
d.comment(0xB1FD, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0xB1FF, 'Offset &78 in buffer', align=Align.INLINE)
d.comment(0xB201, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0xB205, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB208, 'V set (no arg): skip to send', align=Align.INLINE)
d.comment(0xB20A, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB20C, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB20E, 'Space character', align=Align.INLINE)
d.comment(0xB210, 'Fill buffer position with space', align=Align.INLINE)
d.comment(0xB212, 'Next position', align=Align.INLINE)
d.comment(0xB213, 'Count down', align=Align.INLINE)
d.comment(0xB214, 'Loop until 6 spaces filled', align=Align.INLINE)
d.comment(0xB216, 'Save pointer to OS text', align=Align.INLINE)
d.comment(0xB219, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB21B, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB21E, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB220, 'Max 6 characters', align=Align.INLINE)
d.comment(0xB222, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB224, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB226, 'Save buffer position', align=Align.INLINE)
d.comment(0xB228, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB22A, 'Read next char from string', align=Align.INLINE)
d.comment(0xB22D, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB22F, 'End of string: go to send', align=Align.INLINE)
d.comment(0xB231, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB234, 'Loop if more chars to copy', align=Align.INLINE)
d.comment(0xB236, 'Enable escape checking', align=Align.INLINE)
d.comment(0xB238, 'Set escapable flag', align=Align.INLINE)
d.comment(0xB23A, 'Send the poll request packet', align=Align.INLINE)
d.comment(0xB23D, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB240, "Print 'Printer server '", align=Align.INLINE)
d.comment(0xB243, 'Load PS server address', align=Align.INLINE)
d.comment(0xB246, 'Set V and N flags', align=Align.INLINE)
d.comment(0xB249, 'Print station address', align=Align.INLINE)
d.comment(0xB24C, 'Print \' "\'', align=Align.INLINE)
d.comment(0xB251, 'Y=&18: name field offset in RX buffer', align=Align.INLINE)
d.comment(0xB253, 'Get character from name field', align=Align.INLINE)
d.comment(0xB255, 'Is it a space?', align=Align.INLINE)
d.comment(0xB257, 'Yes: end of name', align=Align.INLINE)
d.comment(0xB25C, 'Next character', align=Align.INLINE)
d.comment(0xB25D, 'Past end of name field?', align=Align.INLINE)
d.comment(0xB25F, 'No: continue printing name', align=Align.INLINE)
d.comment(0xB261, 'Print \'"\' + CR', align=Align.INLINE)
d.comment(0xB266, 'Padding byte', align=Align.INLINE)
d.comment(0xB267, 'Get slot offset from stack', align=Align.INLINE)
d.comment(0xB268, 'Zero: all slots done, return', align=Align.INLINE)
d.comment(0xB26A, 'Save slot offset', align=Align.INLINE)
d.comment(0xB26B, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB26C, 'Read slot status byte', align=Align.INLINE)
d.comment(0xB26E, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB270, 'Advance to station number', align=Align.INLINE)
d.comment(0xB271, 'Offset+2 in slot', align=Align.INLINE)
d.comment(0xB272, 'Read station number low', align=Align.INLINE)
d.comment(0xB274, 'Store station low', align=Align.INLINE)
d.comment(0xB276, 'Next byte (offset+3)', align=Align.INLINE)
d.comment(0xB277, 'Read network number', align=Align.INLINE)
d.comment(0xB279, 'Store network number', align=Align.INLINE)
d.comment(0xB27B, 'Next byte (offset+4)', align=Align.INLINE)
d.comment(0xB27C, 'Read status page pointer', align=Align.INLINE)
d.comment(0xB27E, 'Store pointer low', align=Align.INLINE)
d.comment(0xB280, 'Clear V flag', align=Align.INLINE)
d.comment(0xB281, 'Print station address (V=0)', align=Align.INLINE)
d.comment(0xB284, "Print ' is '", align=Align.INLINE)
d.comment(0xB28B, 'X=0 for indirect indexed access', align=Align.INLINE)
d.comment(0xB28D, 'Read printer status byte', align=Align.INLINE)
d.comment(0xB28F, 'Non-zero: not ready', align=Align.INLINE)
d.comment(0xB291, "Print 'ready'", align=Align.INLINE)
d.comment(0xB299, 'Clear V', align=Align.INLINE)
d.comment(0xB29C, 'Status = 2?', align=Align.INLINE)
d.comment(0xB29E, 'No: check for busy', align=Align.INLINE)
d.comment(0xB2A0, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB2A9, 'Clear V', align=Align.INLINE)
d.comment(0xB2AC, 'Status = 1?', align=Align.INLINE)
d.comment(0xB2AE, 'Not 1 or 2: default to jammed', align=Align.INLINE)
d.comment(0xB2B0, "Print 'busy'", align=Align.INLINE)
d.comment(0xB2B7, 'Advance past status byte', align=Align.INLINE)
d.comment(0xB2B9, 'Read client station number', align=Align.INLINE)
d.comment(0xB2BB, 'Store station low', align=Align.INLINE)
d.comment(0xB2BD, 'Zero: no client info, skip', align=Align.INLINE)
d.comment(0xB2BF, "Print ' with station '", align=Align.INLINE)
d.comment(0xB2C8, 'Advance pointer to network byte', align=Align.INLINE)
d.comment(0xB2CC, 'Store network number', align=Align.INLINE)
d.comment(0xB2CA, 'Load client network number', align=Align.INLINE)
d.comment(0xB2CE, 'Set V flag', align=Align.INLINE)
d.comment(0xB2D1, 'Print client station address', align=Align.INLINE)
d.comment(0xB2D7, 'Retrieve slot offset', align=Align.INLINE)
d.comment(0xB2D8, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB2D9, 'Mark slot as processed (&3F)', align=Align.INLINE)
d.comment(0xB2DB, 'Write marker to workspace', align=Align.INLINE)
d.comment(0xB2DF, 'Return', align=Align.INLINE)
d.comment(0xB2E0, 'Start at offset &78', align=Align.INLINE)
d.comment(0xB2E2, 'Load template byte', align=Align.INLINE)
d.comment(0xB2E5, 'At offset &7D?', align=Align.INLINE)
d.comment(0xB2E7, 'Yes: substitute RX page', align=Align.INLINE)
d.comment(0xB2E9, 'At offset &81?', align=Align.INLINE)
d.comment(0xB2EB, 'No: use template byte', align=Align.INLINE)
d.comment(0xB2ED, 'Use RX buffer page instead', align=Align.INLINE)
d.comment(0xB2EF, 'Store byte in slot buffer', align=Align.INLINE)
d.comment(0xB2F1, 'Next offset', align=Align.INLINE)
d.comment(0xB2F2, 'Past end of slot (&84)?', align=Align.INLINE)
d.comment(0xB2F4, 'No: continue copying', align=Align.INLINE)
d.comment(0xB2F6, 'Return', align=Align.INLINE)
d.comment(0xB2F7, 'Y = current buffer position', align=Align.INLINE)
d.comment(0xB2F9, 'Strip high bit', align=Align.INLINE)
d.comment(0xB2FB, "Is it lowercase 'a' or above?", align=Align.INLINE)
d.comment(0xB2FD, "Below 'a': not lowercase", align=Align.INLINE)
d.comment(0xB2FF, "Above 'z'?", align=Align.INLINE)
d.comment(0xB301, 'Yes: not lowercase', align=Align.INLINE)
d.comment(0xB303, 'Convert to uppercase', align=Align.INLINE)
d.comment(0xB305, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB307, 'Next buffer position', align=Align.INLINE)
d.comment(0xB308, 'Update buffer position', align=Align.INLINE)
d.comment(0xB30A, 'Decrement character count', align=Align.INLINE)
d.comment(0xB30B, 'Return (Z set if count=0)', align=Align.INLINE)
d.comment(0xAD6B, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD6E, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xAD6F, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xAD72, 'A=&FF: initial column counter', align=Align.INLINE)
d.comment(0xAD74, 'Store column counter', align=Align.INLINE)
d.comment(0xAD76, 'One entry per line (Ex format)', align=Align.INLINE)
d.comment(0xAD78, 'Store entries per page', align=Align.INLINE)
d.comment(0xAD7A, 'FS command code 3: Examine', align=Align.INLINE)
d.comment(0xAD7C, 'Store command code', align=Align.INLINE)
d.comment(0xAD80, 'Set transfer parameters', align=Align.INLINE)
d.comment(0xAD83, 'Y=0: start from entry 0', align=Align.INLINE)
d.comment(0xAD85, 'Rotate carry into lib flag', align=Align.INLINE)
d.comment(0xAD88, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xAD89, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xAD8C, 'Three entries per column (Cat)', align=Align.INLINE)
d.comment(0xAD8E, 'Store column counter', align=Align.INLINE)
d.comment(0xAD90, 'Store entries per page', align=Align.INLINE)
d.comment(0xAD92, 'FS command code &0B: Catalogue', align=Align.INLINE)
d.comment(0xAD94, 'Store command code', align=Align.INLINE)
d.comment(0xAD96, 'Save text pointer', align=Align.INLINE)
d.comment(0xAD99, 'A=&FF: enable escape checking', align=Align.INLINE)
d.comment(0xAD9B, 'Set escapable flag', align=Align.INLINE)
d.comment(0xAD9D, 'Command code 6', align=Align.INLINE)
d.comment(0xAD9F, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xADA2, 'Parse directory argument', align=Align.INLINE)
d.comment(0xADA5, 'X=1: offset in buffer', align=Align.INLINE)
d.comment(0xADA7, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0xADAA, 'Get library/FS flags', align=Align.INLINE)
d.comment(0xADAD, 'Shift bit 0 to carry', align=Align.INLINE)
d.comment(0xADAE, 'Bit 0 clear: skip', align=Align.INLINE)
d.comment(0xADB0, 'Set bit 6 (owner access flag)', align=Align.INLINE)
d.comment(0xADB2, 'Rotate back', align=Align.INLINE)
d.comment(0xADB3, 'Store modified flags', align=Align.INLINE)
d.comment(0xADB6, 'Y=&12: FS command for examine', align=Align.INLINE)
d.comment(0xADB8, 'Send request to file server', align=Align.INLINE)
d.comment(0xADBB, 'X=3: offset to directory title', align=Align.INLINE)
d.comment(0xADBD, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0xADC0, "Print '('", align=Align.INLINE)
d.comment(0xADB2, 'Get cycle number', align=Align.INLINE)
d.comment(0xADB8, "Print ')     '", align=Align.INLINE)
d.comment(0xADD3, 'Get owner/public flag', align=Align.INLINE)
d.comment(0xADD6, 'Non-zero: public access', align=Align.INLINE)
d.comment(0xADD8, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0xADE1, 'Skip public; ALWAYS branch', align=Align.INLINE)
d.comment(0xADE3, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0xADED, 'Get flags', align=Align.INLINE)
d.comment(0xADF0, 'Save flags', align=Align.INLINE)
d.comment(0xADF1, 'Mask owner access bits', align=Align.INLINE)
d.comment(0xADF4, 'Y=&15: FS command for dir info', align=Align.INLINE)
d.comment(0xADF6, 'Send request to file server', align=Align.INLINE)
d.comment(0xADF9, 'Advance X past header', align=Align.INLINE)
d.comment(0xADFA, 'Y=&10: print 16 chars', align=Align.INLINE)
d.comment(0xADFC, 'Print file entry', align=Align.INLINE)
d.comment(0xADFF, "Print '    Option '", align=Align.INLINE)
d.comment(0xAE0D, 'Get option byte', align=Align.INLINE)
d.comment(0xAE10, 'Transfer to X for table lookup', align=Align.INLINE)
d.comment(0xAE11, 'Print option as hex', align=Align.INLINE)
d.comment(0xAE14, "Print ' ('", align=Align.INLINE)
d.comment(0xAE19, 'Y=string offset for boot option X', align=Align.INLINE)
d.comment(0xAE31, 'Offset &11: directory name', align=Align.INLINE)
d.comment(0xAE33, 'Print directory name (10 chars)', align=Align.INLINE)
d.comment(0xAE1C, 'Load option description character', align=Align.INLINE)
d.comment(0xAE3A, "Print '     Lib. '", align=Align.INLINE)
d.comment(0xAE36, "Print '     Lib. '", align=Align.INLINE)
d.comment(0xAE1F, 'Bit 7 set: end of option string', align=Align.INLINE)
d.comment(0xAE43, 'Offset &1B: library name', align=Align.INLINE)
d.comment(0xAE45, 'Print library name (10 chars)', align=Align.INLINE)
d.comment(0xAE4B, 'Restore flags', align=Align.INLINE)
d.comment(0xAE4C, 'Store restored flags', align=Align.INLINE)
d.comment(0xAE4F, 'Store entry count', align=Align.INLINE)
d.comment(0xAE52, 'Also store in work_4', align=Align.INLINE)
d.comment(0xAE54, 'Get command code', align=Align.INLINE)
d.comment(0xAE56, 'Store in buffer', align=Align.INLINE)
d.comment(0xAE59, 'Get entries per page', align=Align.INLINE)
d.comment(0xAE5B, 'Store in buffer', align=Align.INLINE)
d.comment(0xAE5E, 'X=3: buffer offset', align=Align.INLINE)
d.comment(0xAE60, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xAE63, 'Y=3: FS command for examine/cat', align=Align.INLINE)
d.comment(0xAE65, 'Send request to file server', align=Align.INLINE)
d.comment(0xAE68, 'Advance past header', align=Align.INLINE)
d.comment(0xAE69, 'Get number of entries returned', align=Align.INLINE)
d.comment(0xAE6C, 'Zero: no more entries', align=Align.INLINE)
d.comment(0xAE6E, 'Save entry count', align=Align.INLINE)
d.comment(0xAE6F, 'Advance Y', align=Align.INLINE)
d.comment(0xAE70, 'Get entry data byte', align=Align.INLINE)
d.comment(0xAE73, 'Bit 7 clear: more data', align=Align.INLINE)
d.comment(0xAE75, 'Store terminator byte', align=Align.INLINE)
d.comment(0xAE78, 'Print entry with column separator', align=Align.INLINE)
d.comment(0xAE7B, 'Restore entry count', align=Align.INLINE)
d.comment(0xAE7C, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xAE7D, 'Add entries processed', align=Align.INLINE)
d.comment(0xAE7F, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAE80, 'More entries: loop', align=Align.INLINE)
d.comment(0xAE82, 'Y=10: characters to print', align=Align.INLINE)
d.comment(0xAE84, 'Get character from buffer', align=Align.INLINE)
d.comment(0xAE8A, 'Next buffer position', align=Align.INLINE)
d.comment(0xAE8B, 'Decrement count', align=Align.INLINE)
d.comment(0xAE8C, 'Loop until 10 printed', align=Align.INLINE)
d.comment(0xAE8E, 'Return', align=Align.INLINE)
d.comment(0xAE92, 'Y=0: start of command line', align=Align.INLINE)
d.comment(0xAE94, 'Read string to buffer via GSREAD', align=Align.INLINE)
d.comment(0xAE97, 'Get first parsed character', align=Align.INLINE)
d.comment(0xAE9A, "Is it '&'?", align=Align.INLINE)
d.comment(0xAE9C, "No: check for ':' prefix", align=Align.INLINE)
d.comment(0xAE9E, 'Get flags', align=Align.INLINE)
d.comment(0xAEA1, 'Set FS selection flag (bit 6)', align=Align.INLINE)
d.comment(0xAEA3, 'Store updated flags', align=Align.INLINE)
d.comment(0xAEA6, "Remove '&' prefix character", align=Align.INLINE)
d.comment(0xAEA9, 'Get next character', align=Align.INLINE)
d.comment(0xAEAC, "Is it '.'?", align=Align.INLINE)
d.comment(0xAEAE, "No: check for '#'", align=Align.INLINE)
d.comment(0xAEB0, "Get char after '.'", align=Align.INLINE)
d.comment(0xAEB3, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEB5, "Yes: '&.' + CR only = bad filename", align=Align.INLINE)
d.comment(0xAEB7, 'Save X', align=Align.INLINE)
d.comment(0xAEB8, 'Push X', align=Align.INLINE)
d.comment(0xAEB9, 'X=&FF, will increment to 0', align=Align.INLINE)
d.comment(0xAEBB, 'Increment X', align=Align.INLINE)
d.comment(0xAEBC, 'Get character at offset+1', align=Align.INLINE)
d.comment(0xAEBF, 'Store at offset (shift left)', align=Align.INLINE)
d.comment(0xAEC2, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEC4, 'No: continue shifting', align=Align.INLINE)
d.comment(0xAEC6, 'Get shifted string length', align=Align.INLINE)
d.comment(0xAEC7, 'Zero length: skip trailing trim', align=Align.INLINE)
d.comment(0xAEC9, 'Get character at end of string', align=Align.INLINE)
d.comment(0xAECC, 'Is it a space?', align=Align.INLINE)
d.comment(0xAECE, 'No: done trimming', align=Align.INLINE)
d.comment(0xAED0, 'Replace trailing space with CR', align=Align.INLINE)
d.comment(0xAED2, 'Store CR', align=Align.INLINE)
d.comment(0xAED5, 'Move back', align=Align.INLINE)
d.comment(0xAED6, 'Loop while more trailing spaces', align=Align.INLINE)
d.comment(0xAED8, 'Restore X', align=Align.INLINE)
d.comment(0xAED9, 'Transfer back to X', align=Align.INLINE)
d.comment(0xAEDA, 'Return', align=Align.INLINE)
d.comment(0xAEDB, "Is it '#'?", align=Align.INLINE)
d.comment(0xAEDD, "Yes: '#' prefix accepted", align=Align.INLINE)
d.comment(0xAEDF, 'Bad filename error', align=Align.INLINE)
d.comment(0xAEE2, "Check for ':' prefix", align=Align.INLINE)
d.comment(0xAEE4, "Neither '&' nor ':': no prefix", align=Align.INLINE)
d.comment(0xAEE6, "Get character after ':'", align=Align.INLINE)
d.comment(0xAEE9, "Is it '.'?", align=Align.INLINE)
d.comment(0xAEEB, "Yes: ':.' qualified prefix", align=Align.INLINE)
d.comment(0xAEED, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEEF, 'No: no FS prefix, return', align=Align.INLINE)
d.comment(0xAEF1, 'Get flags', align=Align.INLINE)
d.comment(0xAEF4, 'Set FS selection flag (bit 6)', align=Align.INLINE)
d.comment(0xAEF6, 'Store updated flags', align=Align.INLINE)
d.comment(0xAEFB, 'Data: option string offset table', align=Align.INLINE)
d.comment(0xAF02, 'X=0: start of buffer', align=Align.INLINE)
d.comment(0xAF04, 'Y=0: start of argument', align=Align.INLINE)
d.comment(0xAF06, "Set carry: enable '&' validation", align=Align.INLINE)
d.comment(0xAF07, 'Get character from command line', align=Align.INLINE)
d.comment(0xAF09, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xAF0C, 'Carry clear: skip validation', align=Align.INLINE)
d.comment(0xAF0E, "Is it '!' or above?", align=Align.INLINE)
d.comment(0xAF10, "Is it '&'?", align=Align.INLINE)
d.comment(0xAF12, "Yes: '&' not allowed in filenames", align=Align.INLINE)
d.comment(0xAF14, "'&' in filename: bad filename", align=Align.INLINE)
d.comment(0xAF14, "Restore A (undo '&' EOR)", align=Align.INLINE)
d.comment(0xAF16, 'Advance buffer position', align=Align.INLINE)
d.comment(0xAF17, 'Advance source position', align=Align.INLINE)
d.comment(0xAF18, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAF1A, 'No: continue copying', align=Align.INLINE)
d.comment(0xAF1C, 'Load character from end of buffer', align=Align.INLINE)
d.comment(0xAF2D, 'Return', align=Align.INLINE)
d.comment(0xAF1F, 'Test for space (&20)', align=Align.INLINE)
d.comment(0xAF21, 'Not a space: done trimming', align=Align.INLINE)
d.comment(0xAF23, 'Back up one position', align=Align.INLINE)
d.comment(0xAF32, 'Get flags', align=Align.INLINE)
d.comment(0xAF24, 'CR terminator', align=Align.INLINE)
d.comment(0xAF35, 'Mask to low 5 bits only', align=Align.INLINE)
d.comment(0xAF26, 'Replace trailing space with CR', align=Align.INLINE)
d.comment(0xAF37, 'Store masked flags', align=Align.INLINE)
d.comment(0xAF29, 'ALWAYS: trim next character back', align=Align.INLINE)
d.comment(0xAF3A, 'Return', align=Align.INLINE)
d.comment(0xAF2B, 'A=0: success return code', align=Align.INLINE)
d.comment(0xAF3E, 'X=0: start from first entry', align=Align.INLINE)
d.comment(0xAF40, 'Get entry byte from buffer', align=Align.INLINE)
d.comment(0xAF43, 'High bit set: end of entries', align=Align.INLINE)
d.comment(0xAF45, 'Non-zero: printable character', align=Align.INLINE)
d.comment(0xAF47, 'Get column counter', align=Align.INLINE)
d.comment(0xAF49, 'Negative: newline mode (Ex)', align=Align.INLINE)
d.comment(0xAF4B, 'Increment column counter', align=Align.INLINE)
d.comment(0xAF4C, 'Transfer to A', align=Align.INLINE)
d.comment(0xAF4D, 'Modulo 4 (Cat: 3 per row)', align=Align.INLINE)
d.comment(0xAF4F, 'Store updated counter', align=Align.INLINE)
d.comment(0xAF51, 'Zero: row full, print newline', align=Align.INLINE)
d.comment(0xAF53, "Print '  ' column separator", align=Align.INLINE)
d.comment(0xAF58, 'Skip newline; ALWAYS branch', align=Align.INLINE)
d.comment(0xAF5A, 'CR character for newline', align=Align.INLINE)
d.comment(0xAF5F, 'Advance to next entry', align=Align.INLINE)
d.comment(0xAF60, 'Loop for more entries', align=Align.INLINE)
d.comment(0xAF62, "Embedded string data 'Exec'", align=Align.INLINE)
d.comment(0xAF64, 'Embedded string data (contd)', align=Align.INLINE)
d.comment(0xAFEE, 'A=1: check printer ready', align=Align.INLINE)
d.comment(0xAFF0, 'Test printer server workspace flag', align=Align.INLINE)
d.comment(0xAFF3, 'Non-zero: printer available', align=Align.INLINE)
d.comment(0xAFF5, 'Printer not available: error', align=Align.INLINE)
d.comment(0xAFF8, 'Initialise spool drive', align=Align.INLINE)
d.comment(0xAFFB, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xAFFE, 'Get first argument character', align=Align.INLINE)
d.comment(0xB000, 'End of command line?', align=Align.INLINE)
d.comment(0xB002, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xB004, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xB005, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xB008, 'Yes: station number, skip PS name', align=Align.INLINE)
d.comment(0xB00A, 'PS name follows', align=Align.INLINE)
d.comment(0xB00B, 'Save Y', align=Align.INLINE)
d.comment(0xB00C, 'Load PS server address', align=Align.INLINE)
d.comment(0xB00F, 'Restore Y', align=Align.INLINE)
d.comment(0xB010, 'Back to Y register', align=Align.INLINE)
d.comment(0xB011, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xB014, 'Jump to store station address', align=Align.INLINE)
d.comment(0xB017, 'Start at offset &1C', align=Align.INLINE)
d.comment(0xB019, 'X=&F8: offset into template', align=Align.INLINE)
d.comment(0xB01B, 'Get template byte', align=Align.INLINE)
d.comment(0xB01E, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB020, 'Next destination offset', align=Align.INLINE)
d.comment(0xB021, 'Next source offset', align=Align.INLINE)
d.comment(0xB022, 'Loop until X wraps to 0', align=Align.INLINE)
d.comment(0xB024, 'Return', align=Align.INLINE)
d.comment(0xB025, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB028, 'Save command line pointer', align=Align.INLINE)
d.comment(0xB02A, 'V set: skip PS name parsing', align=Align.INLINE)
d.comment(0xB02C, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB02E, 'Buffer offset &1C for PS name', align=Align.INLINE)
d.comment(0xB030, 'Space character', align=Align.INLINE)
d.comment(0xB032, 'Fill buffer with space', align=Align.INLINE)
d.comment(0xB034, 'Next position', align=Align.INLINE)
d.comment(0xB035, 'Count down', align=Align.INLINE)
d.comment(0xB036, 'Loop until 6 spaces filled', align=Align.INLINE)
d.comment(0xB038, 'Save text pointer', align=Align.INLINE)
d.comment(0xB03B, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB03D, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB040, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB042, 'Max 6 characters', align=Align.INLINE)
d.comment(0xB044, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB046, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB048, 'Save buffer position', align=Align.INLINE)
d.comment(0xB04A, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB04C, 'Read next character', align=Align.INLINE)
d.comment(0xB04F, 'Save updated pointer', align=Align.INLINE)
d.comment(0xB051, 'End of string: go to send', align=Align.INLINE)
d.comment(0xB053, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB056, 'Loop for more characters', align=Align.INLINE)
d.comment(0xB058, 'Copy reversed PS name to TX', align=Align.INLINE)
d.comment(0xB05B, 'Send PS status request', align=Align.INLINE)
d.comment(0xB05E, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB061, 'Load PS server address', align=Align.INLINE)
d.comment(0xB064, 'A=0', align=Align.INLINE)
d.comment(0xB067, 'Offset &24 in buffer', align=Align.INLINE)
d.comment(0xB069, 'Clear PS status byte', align=Align.INLINE)
d.comment(0xB06B, 'Get slot offset from stack', align=Align.INLINE)
d.comment(0xB06C, 'Zero: all slots done', align=Align.INLINE)
d.comment(0xB06E, 'Save slot offset', align=Align.INLINE)
d.comment(0xB06F, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB070, 'Read slot status', align=Align.INLINE)
d.comment(0xB072, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB074, 'Advance Y by 4 (to status page)', align=Align.INLINE)
d.comment(0xB077, 'Read status page pointer', align=Align.INLINE)
d.comment(0xB079, 'Store pointer low', align=Align.INLINE)
d.comment(0xB07B, 'Read printer status byte', align=Align.INLINE)
d.comment(0xB07D, 'Zero (idle): show station info', align=Align.INLINE)
d.comment(0xB081, 'Non-zero (busy): skip', align=Align.INLINE)
d.comment(0xB07F, 'Status 3 (paused)?', align=Align.INLINE)
d.comment(0xB083, 'Back to network number', align=Align.INLINE)
d.comment(0xB084, 'Read network number', align=Align.INLINE)
d.comment(0xB086, 'Store network number', align=Align.INLINE)
d.comment(0xB088, 'Back to station number', align=Align.INLINE)
d.comment(0xB089, 'Read station number', align=Align.INLINE)
d.comment(0xB08B, 'Store station low', align=Align.INLINE)
d.comment(0xB08D, 'Offset &24 in buffer', align=Align.INLINE)
d.comment(0xB08F, 'Store ready station in buffer', align=Align.INLINE)
d.comment(0xB091, 'Retrieve slot offset', align=Align.INLINE)
d.comment(0xB092, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB093, 'Mark slot as processed (&3F)', align=Align.INLINE)
d.comment(0xB095, 'Write marker to workspace', align=Align.INLINE)
d.comment(0xB099, "Print 'Printer server is '", align=Align.INLINE)
d.comment(0xB09C, 'Offset &24: PS station number', align=Align.INLINE)
d.comment(0xB09E, 'Get stored station number', align=Align.INLINE)
d.comment(0xB0A0, 'Non-zero: server changed', align=Align.INLINE)
d.comment(0xB0A2, "Print 'still '", align=Align.INLINE)
d.comment(0xB0AB, 'Clear V', align=Align.INLINE)
d.comment(0xB0AE, "Print 'now '", align=Align.INLINE)
d.comment(0xB0B5, 'Padding', align=Align.INLINE)
d.comment(0xB0B8, 'Workspace offset 2', align=Align.INLINE)
d.comment(0xB0B9, 'Y=2: workspace offset for station', align=Align.INLINE)
d.comment(0xB0BB, 'Get station low', align=Align.INLINE)
d.comment(0xB0BD, 'Store in workspace', align=Align.INLINE)
d.comment(0xB0C0, 'Get network number', align=Align.INLINE)
d.comment(0xB0C2, 'Store in workspace', align=Align.INLINE)
d.comment(0xB0C4, 'Return', align=Align.INLINE)
d.comment(0xB0C5, "Print 'File'", align=Align.INLINE)
d.comment(0xB0CC, 'Clear V', align=Align.INLINE)
d.comment(0xB0CF, "Print 'Printer'", align=Align.INLINE)
d.comment(0xB0D9, 'Padding', align=Align.INLINE)
d.comment(0xB0DA, "Print ' server is '", align=Align.INLINE)
d.comment(0xB0E8, 'Padding', align=Align.INLINE)
d.comment(0xB0E9, 'Return', align=Align.INLINE)
d.comment(0xB0EA, 'Workspace offset 2', align=Align.INLINE)
d.comment(0xB0EC, 'Read station low', align=Align.INLINE)
d.comment(0xB0EE, 'Store station low', align=Align.INLINE)
d.comment(0xB0F1, 'Read network number', align=Align.INLINE)
d.comment(0xB0F3, 'Store network number', align=Align.INLINE)
d.comment(0xB0F5, 'Return', align=Align.INLINE)
d.comment(0xB0F6, 'Pop return address low', align=Align.INLINE)
d.comment(0xB0F7, 'Save return address low', align=Align.INLINE)
d.comment(0xB0F9, 'Pop return address high', align=Align.INLINE)
d.comment(0xB0FA, 'Save return address high', align=Align.INLINE)
d.comment(0xB0FC, 'Push 0 as end-of-list marker', align=Align.INLINE)
d.comment(0xB0FE, 'Push it', align=Align.INLINE)
d.comment(0xB0FF, 'Start scanning from offset &84', align=Align.INLINE)
d.comment(0xB101, 'Store scan position', align=Align.INLINE)
d.comment(0xB103, 'Shift PS slot flags right', align=Align.INLINE)
d.comment(0xB106, 'Counter: 3 PS slots', align=Align.INLINE)
d.comment(0xB108, 'Convert to 2-bit workspace index', align=Align.INLINE)
d.comment(0xB10B, 'Carry set: no more slots', align=Align.INLINE)
d.comment(0xB10D, 'Shift right twice', align=Align.INLINE)
d.comment(0xB10E, 'To get slot offset', align=Align.INLINE)
d.comment(0xB10F, 'Transfer to X', align=Align.INLINE)
d.comment(0xB110, 'Read slot status byte', align=Align.INLINE)
d.comment(0xB112, 'Zero: empty slot, done', align=Align.INLINE)
d.comment(0xB114, 'Is it processed marker (&3F)?', align=Align.INLINE)
d.comment(0xB116, 'Yes: re-initialise this slot', align=Align.INLINE)
d.comment(0xB118, 'Try next slot', align=Align.INLINE)
d.comment(0xB119, 'Transfer slot index to A', align=Align.INLINE)
d.comment(0xB11A, 'Loop for more slots', align=Align.INLINE)
d.comment(0xB11C, 'Y = workspace offset of slot', align=Align.INLINE)
d.comment(0xB11D, 'Push slot offset for scan list', align=Align.INLINE)
d.comment(0xB11E, 'Set active status (&7F)', align=Align.INLINE)
d.comment(0xB120, 'Write status byte', align=Align.INLINE)
d.comment(0xB122, 'Next byte', align=Align.INLINE)
d.comment(0xB123, 'Low byte: workspace page', align=Align.INLINE)
d.comment(0xB125, 'Write workspace pointer low', align=Align.INLINE)
d.comment(0xB127, 'A=0', align=Align.INLINE)
d.comment(0xB129, 'Write two zero bytes + advance Y', align=Align.INLINE)
d.comment(0xB12C, 'Get current scan page', align=Align.INLINE)
d.comment(0xB12E, 'Write RX buffer page low', align=Align.INLINE)
d.comment(0xB130, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xB131, 'Save processor status', align=Align.INLINE)
d.comment(0xB132, 'Advance by 3 pages', align=Align.INLINE)
d.comment(0xB134, 'Restore processor status', align=Align.INLINE)
d.comment(0xB135, 'Update scan position', align=Align.INLINE)
d.comment(0xB137, 'Write buffer page + &FF bytes', align=Align.INLINE)
d.comment(0xB13A, 'Get updated scan position', align=Align.INLINE)
d.comment(0xB13C, 'Write RX buffer page high', align=Align.INLINE)
d.comment(0xB13E, 'Write another page + &FF bytes', align=Align.INLINE)
d.comment(0xB141, 'Continue scanning slots', align=Align.INLINE)
d.comment(0xB144, 'Shift PS slot flags back', align=Align.INLINE)
d.comment(0xB147, 'Restore return address high', align=Align.INLINE)
d.comment(0xB149, 'Push onto stack', align=Align.INLINE)
d.comment(0xB14A, 'Restore return address low', align=Align.INLINE)
d.comment(0xB14C, 'Push onto stack', align=Align.INLINE)
d.comment(0xB14D, 'Delay counter: 10', align=Align.INLINE)
d.comment(0xB151, 'Outer loop counter = 10', align=Align.INLINE)
d.comment(0xB153, 'Decrement Y (inner loop)', align=Align.INLINE)
d.comment(0xB154, 'Inner loop: 10 iterations', align=Align.INLINE)
d.comment(0xB156, 'Decrement X (middle loop)', align=Align.INLINE)
d.comment(0xB157, 'Middle loop: 10 iterations', align=Align.INLINE)
d.comment(0xB159, 'Decrement outer counter', align=Align.INLINE)
d.comment(0xB15B, 'Outer loop: ~1000 delay cycles', align=Align.INLINE)
d.comment(0xB15D, 'Return', align=Align.INLINE)
d.comment(0xB15E, 'Advance Y', align=Align.INLINE)
d.comment(0xB15F, 'Get buffer page', align=Align.INLINE)
d.comment(0xB161, 'Store in workspace', align=Align.INLINE)
d.comment(0xB163, 'A=&FF', align=Align.INLINE)
d.comment(0xB165, 'Advance Y', align=Align.INLINE)
d.comment(0xB166, 'Write byte to workspace', align=Align.INLINE)
d.comment(0xB168, 'Advance Y', align=Align.INLINE)
d.comment(0xB169, 'Write byte to workspace', align=Align.INLINE)
d.comment(0xB16B, 'Advance Y', align=Align.INLINE)
d.comment(0xB16C, 'Return', align=Align.INLINE)
d.comment(0xB16D, 'Start of PS name at offset &1C', align=Align.INLINE)
d.comment(0xB16F, 'Load byte from RX buffer', align=Align.INLINE)
d.comment(0xB171, 'Push to stack (for reversal)', align=Align.INLINE)
d.comment(0xB172, 'Next source byte', align=Align.INLINE)
d.comment(0xB173, 'End of PS name field (&20)?', align=Align.INLINE)
d.comment(0xB175, 'No: continue pushing', align=Align.INLINE)
d.comment(0xB177, 'End of TX name field at &1B', align=Align.INLINE)
d.comment(0xB179, 'Pop byte (reversed order)', align=Align.INLINE)
d.comment(0xB17A, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB17C, 'Previous position', align=Align.INLINE)
d.comment(0xB17D, 'Start of TX field (&0F)?', align=Align.INLINE)
d.comment(0xB17F, 'No: continue popping', align=Align.INLINE)
d.comment(0xB181, 'Copy RX page to TX', align=Align.INLINE)
d.comment(0xB183, 'Set TX pointer high', align=Align.INLINE)
d.comment(0xB185, 'TX offset &10', align=Align.INLINE)
d.comment(0xB187, 'Set TX pointer low', align=Align.INLINE)
d.comment(0xB189, 'Copy 4 header bytes', align=Align.INLINE)
d.comment(0xB18B, 'Get header template byte', align=Align.INLINE)
d.comment(0xB18E, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB190, 'Previous byte', align=Align.INLINE)
d.comment(0xB191, 'Loop until all 4 copied', align=Align.INLINE)
d.comment(0xB193, 'Return', align=Align.INLINE)
d.comment(0xB194, """Printer server TX header template

4-byte header copied to the TX control block by
reverse_ps_name_to_tx. Sets up an immediate
transmit on port &9F (PS port) to any station.""")
d.comment(0xB194, 'Control byte &80 (immediate TX)', align=Align.INLINE)
d.comment(0xB195, 'Port &9F (printer server)', align=Align.INLINE)
d.comment(0xB196, 'Station &FF (any)', align=Align.INLINE)
d.comment(0xB197, 'Network &FF (any)', align=Align.INLINE)
d.comment(0xB198, 'Save V flag (controls padding)', align=Align.INLINE)
d.comment(0xB199, 'Get network number', align=Align.INLINE)
d.comment(0xB19B, 'Zero: no network prefix', align=Align.INLINE)
d.comment(0xB19D, 'Print network as 3 digits', align=Align.INLINE)
d.comment(0xB1A0, "'.' separator", align=Align.INLINE)
d.comment(0xB1A5, 'Set V (suppress station padding)', align=Align.INLINE)
d.comment(0xB1A8, 'V set: skip padding spaces', align=Align.INLINE)
d.comment(0xB1AA, 'Print 4 spaces (padding)', align=Align.INLINE)
d.comment(0xB1B1, 'Get station number', align=Align.INLINE)
d.comment(0xB1B3, 'Restore flags', align=Align.INLINE)
d.comment(0xB1B4, 'Print station as 3 digits', align=Align.INLINE)
d.comment(0xB1B7, """PS slot transmit control block template

12-byte Econet TXCB initialisation template for
printer server slot buffers. Not referenced by
label; accessed indirectly by init_ps_slot_from_rx
via LDA write_ps_slot_link_addr,Y where the base
address write_ps_slot_hi_link+1 plus Y offset &78 computes to &B1B7.

Structure: 4-byte header (control, port, station,
network) followed by two 4-byte buffer descriptors
(lo address, hi page, end lo, end hi). The hi page
bytes at positions 5 and 9 are overwritten with
net_rx_ptr_hi during the copy to point into the
actual RX buffer page. End bytes &FF are
placeholders filled in later by the caller.""")
d.comment(0xB1B7, 'Control byte &80 (immediate TX)', align=Align.INLINE)
d.comment(0xB1B8, 'Port &9F (printer server)', align=Align.INLINE)
d.comment(0xB1B9, 'Station 0 (filled in later)', align=Align.INLINE)
d.comment(0xB1BA, 'Network 0 (filled in later)', align=Align.INLINE)
d.comment(0xB1BC, 'Data buffer start hi (= rx page)', align=Align.INLINE)
d.comment(0xB1BD, 'Data buffer end lo (placeholder)', align=Align.INLINE)
d.comment(0xB1BE, 'Data buffer end hi (placeholder)', align=Align.INLINE)
d.comment(0xB1C0, 'Reply buffer start hi (= rx page)', align=Align.INLINE)
d.comment(0xB1C1, 'Reply buffer end lo (placeholder)', align=Align.INLINE)
d.comment(0xB1C2, 'Reply buffer end hi (placeholder)', align=Align.INLINE)
d.comment(0x949E, 'Y=0: close all files', align=Align.INLINE)
d.comment(0x94A0, 'Process all file control blocks', align=Align.INLINE)
d.comment(0x94A3, 'OSBYTE &77: close spool/exec', align=Align.INLINE)
d.comment(0x94A8, 'Close all network channels', align=Align.INLINE)
d.comment(0x94AB, 'Y=&17: *Bye function code', align=Align.INLINE)
d.comment(0x94AD, 'Clear V (standard mode)', align=Align.INLINE)
d.comment(0x94AE, 'Copy FS station to TX control block', align=Align.INLINE)
d.comment(0x94B1, 'Store in TXCB', align=Align.INLINE)
d.comment(0x94B4, 'Clear carry', align=Align.INLINE)
d.comment(0x94B5, 'Save flags (carry = mode)', align=Align.INLINE)
d.comment(0x94B6, 'Store function code in TXCB', align=Align.INLINE)
d.comment(0x94B9, 'Copy 2 bytes (indices 0-1)', align=Align.INLINE)
d.comment(0x94BB, 'Load source byte', align=Align.INLINE)
d.comment(0x94BE, 'Store to TXCB', align=Align.INLINE)
d.comment(0x94C1, 'Next byte', align=Align.INLINE)
d.comment(0x94C2, 'Loop until all copied', align=Align.INLINE)
d.comment(0x94C4, 'Test library flag bits 6-7', align=Align.INLINE)
d.comment(0x94C7, 'Bit 6 set: use station as port', align=Align.INLINE)
d.comment(0x94C9, 'Bit 7 clear: skip port override', align=Align.INLINE)
d.comment(0x94CB, 'Bit 7 set: load alternative port', align=Align.INLINE)
d.comment(0x94CE, 'Override TXCB port byte', align=Align.INLINE)
d.comment(0x94D3, 'Bit 6: load station byte', align=Align.INLINE)
d.comment(0x94D6, 'Use station as TXCB port', align=Align.INLINE)
d.comment(0x94D9, 'Restore flags (carry = mode)', align=Align.INLINE)
d.comment(0x94DA, 'Save flags', align=Align.INLINE)
d.comment(0x94DB, 'Port &90: FS command port', align=Align.INLINE)
d.comment(0x94DD, 'Set reply port in TXCB', align=Align.INLINE)
d.comment(0x94E0, 'Initialise TXCB workspace', align=Align.INLINE)
d.comment(0x94E3, 'Get TXCB data end offset', align=Align.INLINE)
d.comment(0x94E4, 'Add 5 for header size', align=Align.INLINE)
d.comment(0x94E6, 'Set TXCB end pointer', align=Align.INLINE)
d.comment(0x94E8, 'Restore flags', align=Align.INLINE)
d.comment(0x94E9, 'C set: send disconnect instead', align=Align.INLINE)
d.comment(0x94EB, 'Save flags', align=Align.INLINE)
d.comment(0x94EC, 'Initialise TX pointer and send', align=Align.INLINE)
d.comment(0x94EF, 'Restore flags', align=Align.INLINE)
d.comment(0x94F0, 'Save flags', align=Align.INLINE)
d.comment(0x94F1, 'Set up receive TXCB', align=Align.INLINE)
d.comment(0x94F4, 'Wait for TX acknowledgment', align=Align.INLINE)
d.comment(0x94F7, 'Restore flags', align=Align.INLINE)
d.comment(0x94F8, 'Advance to next reply byte', align=Align.INLINE)
d.comment(0x94F9, 'Load reply byte', align=Align.INLINE)
d.comment(0x94FB, 'Save in X', align=Align.INLINE)
d.comment(0x94FC, 'Zero: no more replies, return', align=Align.INLINE)
d.comment(0x94FE, 'V clear: use code directly', align=Align.INLINE)
d.comment(0x9500, 'V set: adjust reply code (+&2B)', align=Align.INLINE)
d.comment(0x9502, 'Non-zero: process reply', align=Align.INLINE)
d.comment(0x9504, 'Return', align=Align.INLINE)
d.comment(0x9505, 'Discard saved flags', align=Align.INLINE)
d.comment(0x9506, 'X=&C0: disconnect command', align=Align.INLINE)
d.comment(0x9508, 'Advance reply offset', align=Align.INLINE)
d.comment(0x9509, 'Send disconnect reply', align=Align.INLINE)
d.comment(0x950C, 'Successful: process next reply', align=Align.INLINE)
d.comment(0x950E, 'Store reply status code', align=Align.INLINE)
d.comment(0x9511, 'Load pending operation marker', align=Align.INLINE)
d.comment(0x9514, 'Save pending operation flag (Z)', align=Align.INLINE)
d.comment(0x9515, 'Pending: go to data loss check', align=Align.INLINE)
d.comment(0x9517, 'Reply &BF (normal bye response)?', align=Align.INLINE)
d.comment(0x9519, 'No: build error from reply', align=Align.INLINE)
d.comment(0x951B, 'A=&40: initial data-loss flag', align=Align.INLINE)
d.comment(0x951D, 'Push data-loss accumulator', align=Align.INLINE)
d.comment(0x951E, 'Scan 16 channel entries (15 to 0)', align=Align.INLINE)
d.comment(0x9520, 'Pop accumulator', align=Align.INLINE)
d.comment(0x9521, 'OR in channel status bits', align=Align.INLINE)
d.comment(0x9524, 'Push updated accumulator', align=Align.INLINE)
d.comment(0x9525, 'Load channel status', align=Align.INLINE)
d.comment(0x9528, 'Keep only bits 6-7 (close flags)', align=Align.INLINE)
d.comment(0x952A, 'Clear data bits, keep state flags', align=Align.INLINE)
d.comment(0x952D, 'Advance to next channel slot', align=Align.INLINE)
d.comment(0x9533, 'Close all network channels', align=Align.INLINE)
d.comment(0x952E, 'Bit 7 set: more channels to scan', align=Align.INLINE)
d.comment(0x9536, 'Pop data-loss accumulator', align=Align.INLINE)
d.comment(0x9530, 'Store last channel scanned', align=Align.INLINE)
d.comment(0x9537, 'Bit 0 to carry (data lost?)', align=Align.INLINE)
d.comment(0x9538, 'No data lost: skip message', align=Align.INLINE)
d.comment(0x953A, "Print 'Data Lost' + CR", align=Align.INLINE)
d.comment(0x9547, 'Reload reply status code', align=Align.INLINE)
d.comment(0x954A, 'Restore pending operation flag', align=Align.INLINE)
d.comment(0x954D, 'No pending: build error from reply', align=Align.INLINE)
d.comment(0x954B, 'No pending operation: build error', align=Align.INLINE)
d.comment(0x954D, 'Pending: clean up stack (3 bytes)', align=Align.INLINE)
d.comment(0x954E, '(second byte)', align=Align.INLINE)
d.comment(0x954F, '(third byte)', align=Align.INLINE)
d.comment(0x9550, 'Return to pending operation caller', align=Align.INLINE)
d.comment(0x9551, 'Y=1: error code offset in reply', align=Align.INLINE)
d.comment(0x9553, 'Reply code >= &A8?', align=Align.INLINE)
d.comment(0x9555, 'Yes: keep server error code', align=Align.INLINE)
d.comment(0x9557, 'No: use minimum error code &A8', align=Align.INLINE)
d.comment(0x9559, 'Overwrite error code in reply', align=Align.INLINE)
d.comment(0x955B, 'Y=&FF: pre-increment index', align=Align.INLINE)
d.comment(0x955D, 'Advance to next byte', align=Align.INLINE)
d.comment(0x955E, 'Load reply byte', align=Align.INLINE)
d.comment(0x9560, 'Copy to error block', align=Align.INLINE)
d.comment(0x9563, 'Is it CR (end of message)?', align=Align.INLINE)
d.comment(0x9565, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9567, 'Store null terminator (A=0 from EOR)', align=Align.INLINE)
d.comment(0x956A, 'Get message length', align=Align.INLINE)
d.comment(0x956B, 'Transfer to A', align=Align.INLINE)
d.comment(0x956C, 'Length in X', align=Align.INLINE)
d.comment(0x956D, 'Go to error dispatch', align=Align.INLINE)
d.comment(0x9570, 'Load MOS escape flag', align=Align.INLINE)
d.comment(0x9572, 'Mask with escape-enabled flag', align=Align.INLINE)
d.comment(0x9574, 'No escape: return', align=Align.INLINE)
d.comment(0x9576, 'OSBYTE &7E: acknowledge escape', align=Align.INLINE)
d.comment(0x957B, 'Error class 6: Escape', align=Align.INLINE)
d.comment(0x957D, 'Classify as network error', align=Align.INLINE)
d.comment(0x9580, 'Offset 0: remote state byte', align=Align.INLINE)
d.comment(0x9582, 'Load remote state', align=Align.INLINE)
d.comment(0x9584, 'Zero: initialise remote session', align=Align.INLINE)
d.comment(0x9586, 'Non-zero: commit state and return', align=Align.INLINE)
d.comment(0x9589, 'Set bits 0,3: remote active flags', align=Align.INLINE)
d.comment(0x958B, 'Store updated remote state', align=Align.INLINE)
d.comment(0x958D, 'X=&80: flag for vector setup', align=Align.INLINE)
d.comment(0x958F, 'Offset &80 in RX buffer', align=Align.INLINE)
d.comment(0x9591, 'Load remote station low', align=Align.INLINE)
d.comment(0x9593, 'Save on stack', align=Align.INLINE)
d.comment(0x9595, 'Load remote station high', align=Align.INLINE)
d.comment(0x9597, 'Workspace offset &0F', align=Align.INLINE)
d.comment(0x9599, 'Store remote station high', align=Align.INLINE)
d.comment(0x959B, 'Y=&0E', align=Align.INLINE)
d.comment(0x959C, 'Restore remote station low', align=Align.INLINE)
d.comment(0x959D, 'Store remote station low', align=Align.INLINE)
d.comment(0x959F, 'Set up remote keyboard scanning', align=Align.INLINE)
d.comment(0x95A2, 'Initialise workspace copy', align=Align.INLINE)
d.comment(0x95A5, 'X=1: disable keyboard', align=Align.INLINE)
d.comment(0x95A7, 'Y=0', align=Align.INLINE)
d.comment(0x95A9, 'OSBYTE &C9: Econet keyboard disable', align=Align.INLINE)
d.comment(0x95AE, 'Commit state change', align=Align.INLINE)
d.comment(0x95B1, 'Error code 0', align=Align.INLINE)
d.comment(0x95B3, "Generate 'Remoted' error", align=Align.INLINE)
d.comment(0x95BE, 'Offset 0: remote state byte', align=Align.INLINE)
d.comment(0x95C0, 'Load remote state', align=Align.INLINE)
d.comment(0x95C2, 'Zero: reinitialise session', align=Align.INLINE)
d.comment(0x95C4, 'Offset &80: station low', align=Align.INLINE)
d.comment(0x95C6, 'Load station low from RX', align=Align.INLINE)
d.comment(0x95C8, 'Workspace offset &0E', align=Align.INLINE)
d.comment(0x95CA, 'Compare with stored station', align=Align.INLINE)
d.comment(0x95CC, 'Different station: commit state', align=Align.INLINE)
d.comment(0x95CE, 'Offset &82: keypress byte', align=Align.INLINE)
d.comment(0x95D0, 'Load remote keypress', align=Align.INLINE)
d.comment(0x95D2, 'Key code to Y', align=Align.INLINE)
d.comment(0x95D3, 'X=0: keyboard buffer', align=Align.INLINE)
d.comment(0x95D5, 'Commit state change', align=Align.INLINE)
d.comment(0x95D8, 'OSBYTE &99: insert into buffer', align=Align.INLINE)
d.comment(0x95DD, 'Save TX timeout counter', align=Align.INLINE)
d.comment(0x95E0, 'Push (used as outer loop counter)', align=Align.INLINE)
d.comment(0x95E1, 'Save TX control state', align=Align.INLINE)
d.comment(0x95E4, 'Push (preserved during wait)', align=Align.INLINE)
d.comment(0x95E5, 'Check if TX in progress', align=Align.INLINE)
d.comment(0x95E7, 'Non-zero: skip force-wait', align=Align.INLINE)
d.comment(0x95E9, 'Set bit 7 to force wait mode', align=Align.INLINE)
d.comment(0x95EB, 'Store updated control state', align=Align.INLINE)
d.comment(0x95EE, 'A=0: initial counter values', align=Align.INLINE)
d.comment(0x95F0, 'Push inner loop counter', align=Align.INLINE)
d.comment(0x95F1, 'Push middle loop counter', align=Align.INLINE)
d.comment(0x95F3, 'X=SP for stack-relative DECs', align=Align.INLINE)
d.comment(0x95F4, 'Poll TX completion status', align=Align.INLINE)
d.comment(0x95F6, 'Bit 7 set: TX complete', align=Align.INLINE)
d.comment(0x95F8, 'Decrement inner counter', align=Align.INLINE)
d.comment(0x95FB, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x95FD, 'Decrement middle counter', align=Align.INLINE)
d.comment(0x9600, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x9602, 'Decrement outer counter', align=Align.INLINE)
d.comment(0x9605, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x9607, 'Discard inner counter', align=Align.INLINE)
d.comment(0x9608, 'Discard middle counter', align=Align.INLINE)
d.comment(0x9609, 'Restore l0d61 control state', align=Align.INLINE)
d.comment(0x960A, 'Write back TX control state', align=Align.INLINE)
d.comment(0x960D, 'Pop outer counter (0 if timed out)', align=Align.INLINE)
d.comment(0x960E, 'Zero: TX timed out', align=Align.INLINE)
d.comment(0x9610, 'Return (TX acknowledged)', align=Align.INLINE)
d.comment(0x9611, 'Test error logging flag', align=Align.INLINE)
d.comment(0x9614, 'Bit 7 clear: skip save', align=Align.INLINE)
d.comment(0x9616, 'Save error code to workspace', align=Align.INLINE)
d.comment(0x9619, 'Return', align=Align.INLINE)
d.comment(0x961A, "X=8: 'No reply' error index", align=Align.INLINE)
d.comment(0x961C, 'Look up message table offset', align=Align.INLINE)
d.comment(0x961F, 'X=0: error text start', align=Align.INLINE)
d.comment(0x9621, 'Clear BRK byte in error block', align=Align.INLINE)
d.comment(0x9624, 'Load error number from table', align=Align.INLINE)
d.comment(0x9627, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x962A, 'Load message byte', align=Align.INLINE)
d.comment(0x962D, 'Store in error text buffer', align=Align.INLINE)
d.comment(0x9630, 'Null terminator?', align=Align.INLINE)
d.comment(0x9632, 'Advance destination', align=Align.INLINE)
d.comment(0x9633, 'Advance source', align=Align.INLINE)
d.comment(0x9634, 'Loop until end of message', align=Align.INLINE)
d.comment(0x9636, "Append ' net.station' to message", align=Align.INLINE)
d.comment(0x9639, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x963B, 'Terminate error text', align=Align.INLINE)
d.comment(0x963E, 'Check and raise network error', align=Align.INLINE)
d.comment(0x9641, 'Load first reply byte', align=Align.INLINE)
d.comment(0x9643, "Is it 'A' (status &41)?", align=Align.INLINE)
d.comment(0x9645, 'No: keep original', align=Align.INLINE)
d.comment(0x9647, "Yes: change to 'B' (&42)", align=Align.INLINE)
d.comment(0x9649, 'Clear V flag', align=Align.INLINE)
d.comment(0x964C, 'Load first reply byte', align=Align.INLINE)
d.comment(0x964E, 'Set V flag (via BIT &FF)', align=Align.INLINE)
d.comment(0x9651, 'Mask to error class (0-7)', align=Align.INLINE)
d.comment(0x9653, 'Save error class on stack', align=Align.INLINE)
d.comment(0x9654, 'Class 2 (station error)?', align=Align.INLINE)
d.comment(0x9656, 'No: build simple error message', align=Align.INLINE)
d.comment(0x9658, 'Save flags (V state for suffix)', align=Align.INLINE)
d.comment(0x9659, 'Error class to X', align=Align.INLINE)
d.comment(0x965A, 'Look up message table offset', align=Align.INLINE)
d.comment(0x965D, 'Load error number from table', align=Align.INLINE)
d.comment(0x9660, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x9663, 'X=0: error text start', align=Align.INLINE)
d.comment(0x9665, 'Clear BRK byte', align=Align.INLINE)
d.comment(0x9668, 'Load message byte', align=Align.INLINE)
d.comment(0x966B, 'Store in error text', align=Align.INLINE)
d.comment(0x966E, 'Null terminator?', align=Align.INLINE)
d.comment(0x9670, 'Advance source', align=Align.INLINE)
d.comment(0x9671, 'Advance destination', align=Align.INLINE)
d.comment(0x9672, 'Loop until end of message', align=Align.INLINE)
d.comment(0x9674, "Append ' net.station' suffix", align=Align.INLINE)
d.comment(0x9677, 'Restore flags', align=Align.INLINE)
d.comment(0x9678, "V set: append 'not listening'", align=Align.INLINE)
d.comment(0x967A, 'Error code &A4', align=Align.INLINE)
d.comment(0x967C, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x967F, 'Replace error number in block', align=Align.INLINE)
d.comment(0x9682, "Y=&0B: 'not present' suffix index", align=Align.INLINE)
d.comment(0x9686, "Y=9: 'not listening' suffix index", align=Align.INLINE)
d.comment(0x9688, 'Look up suffix table offset', align=Align.INLINE)
d.comment(0x968B, 'Offset to Y for indexing', align=Align.INLINE)
d.comment(0x968C, 'Load suffix byte', align=Align.INLINE)
d.comment(0x968F, 'Append to error text', align=Align.INLINE)
d.comment(0x9692, 'Null terminator?', align=Align.INLINE)
d.comment(0x9694, 'Advance source', align=Align.INLINE)
d.comment(0x9695, 'Advance destination', align=Align.INLINE)
d.comment(0x9696, 'Loop until end of suffix', align=Align.INLINE)
d.comment(0x9698, 'ALWAYS branch to error dispatch', align=Align.INLINE)
d.comment(0x969A, 'Error class to X', align=Align.INLINE)
d.comment(0x969B, 'Look up message table offset', align=Align.INLINE)
d.comment(0x969E, 'X=0: error text start', align=Align.INLINE)
d.comment(0x96A0, 'Clear BRK byte', align=Align.INLINE)
d.comment(0x96A3, 'Load error number from table', align=Align.INLINE)
d.comment(0x96A6, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x96A9, 'Load message byte', align=Align.INLINE)
d.comment(0x96AC, 'Store in error text', align=Align.INLINE)
d.comment(0x96AF, 'Null terminator? Go to error', align=Align.INLINE)
d.comment(0x96B1, 'Advance source', align=Align.INLINE)
d.comment(0x96B2, 'Advance destination', align=Align.INLINE)
d.comment(0x96B3, 'Loop until end of message', align=Align.INLINE)
d.comment(0xA07B, 'Load current FS station high', align=Align.INLINE)
d.comment(0xA07E, 'Save to fs_work_5', align=Align.INLINE)
d.comment(0xA080, 'Load current FS station low', align=Align.INLINE)
d.comment(0xA083, 'Save to l00b6', align=Align.INLINE)
d.comment(0xA085, 'Get first character of argument', align=Align.INLINE)
d.comment(0xA087, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0xA089, 'No arg: print current FS info', align=Align.INLINE)
d.comment(0xA08B, 'Parse FS/PS station arguments', align=Align.INLINE)
d.comment(0xA08E, 'A=1: write NFS info', align=Align.INLINE)
d.comment(0xA090, 'Store OSWORD sub-function', align=Align.INLINE)
d.comment(0xA092, 'OSWORD &13: NFS information', align=Align.INLINE)
d.comment(0xA094, 'Parameter block low', align=Align.INLINE)
d.comment(0xA096, 'Parameter block high', align=Align.INLINE)
d.comment(0xA09B, "Print 'File server '", align=Align.INLINE)
d.comment(0xA09E, 'Set V (suppress padding)', align=Align.INLINE)
d.comment(0xA0A1, 'Print station address', align=Align.INLINE)
d.comment(0xA0A7, 'Save X on stack', align=Align.INLINE)
d.comment(0xA0A8, 'Push X', align=Align.INLINE)
d.comment(0xA0A9, 'A=0: initialise dot-seen flag', align=Align.INLINE)
d.comment(0xA0AB, 'Clear dot-seen flag', align=Align.INLINE)
d.comment(0xA0AD, 'Parse first number (network)', align=Align.INLINE)
d.comment(0xA0B0, 'C set: number found, check for dot', align=Align.INLINE)
d.comment(0xA0B2, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0xA0B3, 'Push Y', align=Align.INLINE)
d.comment(0xA0B4, 'Initialise bridge polling', align=Align.INLINE)
d.comment(0xA0B7, 'Compare bridge result with parsed value', align=Align.INLINE)
d.comment(0xA0B9, 'Same: keep bridge result', align=Align.INLINE)
d.comment(0xA0BB, 'Different: use parsed value', align=Align.INLINE)
d.comment(0xA0BD, 'Store station low byte', align=Align.INLINE)
d.comment(0xA0BF, 'Restore Y', align=Align.INLINE)
d.comment(0xA0C0, 'Transfer back to Y', align=Align.INLINE)
d.comment(0xA0C1, 'Skip dot separator', align=Align.INLINE)
d.comment(0xA0C2, 'Parse second number (station)', align=Align.INLINE)
d.comment(0xA0C5, 'Zero result: skip store', align=Align.INLINE)
d.comment(0xA0C7, 'Store station high byte', align=Align.INLINE)
d.comment(0xA0C9, 'Restore X', align=Align.INLINE)
d.comment(0xA0CA, 'Transfer back to X', align=Align.INLINE)
d.comment(0xA0CB, 'Return', align=Align.INLINE)
d.comment(0xA0CC, 'Load parameter block pointer', align=Align.INLINE)
d.comment(0xA0CE, 'Shift left (A * 2)', align=Align.INLINE)
d.comment(0xA0CF, 'Shift left (A * 4)', align=Align.INLINE)
d.comment(0xA0D0, 'Save A * 4 on stack', align=Align.INLINE)
d.comment(0xA0D1, 'Shift left (A * 8)', align=Align.INLINE)
d.comment(0xA0D2, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA0D3, 'Save flags (carry from shift)', align=Align.INLINE)
d.comment(0xA0D4, 'A*8 + A*4 (from stack) = A*12', align=Align.INLINE)
d.comment(0xA0D7, 'Divide by 2 with carry', align=Align.INLINE)
d.comment(0xA0D8, 'Restore original flags', align=Align.INLINE)
d.comment(0xA0D9, 'Shift left again', align=Align.INLINE)
d.comment(0xA0DA, 'Result to Y as index', align=Align.INLINE)
d.comment(0xA0DB, 'Pop saved A * 4', align=Align.INLINE)
d.comment(0xA0DC, 'A * 4 >= &48 (out of range)?', align=Align.INLINE)
d.comment(0xA0DE, 'In range: return', align=Align.INLINE)
d.comment(0xA0E0, 'Out of range: Y=0', align=Align.INLINE)
d.comment(0xA0E2, 'A=&00', align=Align.INLINE)
d.comment(0xA0E3, 'Return with A=index, Y=index', align=Align.INLINE)
d.comment(0xA0E4, 'Y=&6F: source offset', align=Align.INLINE)
d.comment(0xA0E6, 'Load byte from RX buffer', align=Align.INLINE)
d.comment(0xA0E8, 'C clear: store directly', align=Align.INLINE)
d.comment(0xA0EA, 'Get index from PB pointer', align=Align.INLINE)
d.comment(0xA0ED, 'C set (out of range): clear value', align=Align.INLINE)
d.comment(0xA0EF, 'Load workspace byte at index', align=Align.INLINE)
d.comment(0xA0F1, "Is it '?' (uninitialised)?", align=Align.INLINE)
d.comment(0xA0F3, 'No: use value from RX buffer', align=Align.INLINE)
d.comment(0xA0F5, 'A=0: return zero for uninitialised', align=Align.INLINE)
d.comment(0xA0F7, 'Store result to PB pointer', align=Align.INLINE)
d.comment(0xA0F9, 'Return', align=Align.INLINE)
d.comment(0xA0FA, 'Get index from PB pointer', align=Align.INLINE)
d.comment(0xA0FD, 'C clear: store to workspace', align=Align.INLINE)
d.comment(0xA0FF, 'Save carry to l0d6c bit 7', align=Align.INLINE)
d.comment(0xA102, 'Load PB pointer value', align=Align.INLINE)
d.comment(0xA104, 'Shift carry back in', align=Align.INLINE)
d.comment(0xA105, 'Restore l0d6c bit 7', align=Align.INLINE)
d.comment(0xA108, 'Return', align=Align.INLINE)
d.comment(0xA109, 'Save carry to l0d61 bit 7', align=Align.INLINE)
d.comment(0xA10C, "A='?': mark as uninitialised", align=Align.INLINE)
d.comment(0xA10E, "Store '?' to workspace", align=Align.INLINE)
d.comment(0xA110, 'Restore l0d61 bit 7', align=Align.INLINE)
d.comment(0xA113, 'Return', align=Align.INLINE)
d.comment(0xA114, 'Set text and transfer pointers', align=Align.INLINE)
d.comment(0xA117, 'Y=&FF: prepare for INY to 0', align=Align.INLINE)
d.comment(0xA119, 'Clear spool handle (no spool active)', align=Align.INLINE)
d.comment(0xA11B, 'Set escapable flag (&FF)', align=Align.INLINE)
d.comment(0xA11E, 'X=&4A: FS command table offset', align=Align.INLINE)
d.comment(0xA120, 'Match command in FS table', align=Align.INLINE)
d.comment(0xA123, 'C set: command found', align=Align.INLINE)
d.comment(0xA125, 'V clear: syntax error', align=Align.INLINE)
d.comment(0xA127, 'Error code &DC', align=Align.INLINE)
d.comment(0xA129, "Generate 'Syntax' error", align=Align.INLINE)
d.comment(0xA133, 'A=0: clear service state', align=Align.INLINE)
d.comment(0xA135, 'Store cleared service state', align=Align.INLINE)
d.comment(0xA137, 'Load command handler address high', align=Align.INLINE)
d.comment(0xA13A, 'Push high byte', align=Align.INLINE)
d.comment(0xA13B, 'Load command handler address low', align=Align.INLINE)
d.comment(0xA13E, 'Push low byte', align=Align.INLINE)
d.comment(0xA13F, 'RTS dispatches to command handler', align=Align.INLINE)
d.comment(0xA140, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0xA141, 'Push on stack', align=Align.INLINE)
d.comment(0xA142, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA143, 'Push back (keep on stack)', align=Align.INLINE)
d.comment(0xA144, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA145, 'Load table entry byte', align=Align.INLINE)
d.comment(0xA148, 'Bit 7 set: end of table names', align=Align.INLINE)
d.comment(0xA14A, 'Load table byte', align=Align.INLINE)
d.comment(0xA14D, 'Bit 7 set: end of this name', align=Align.INLINE)
d.comment(0xA14F, 'Compare with command line char', align=Align.INLINE)
d.comment(0xA151, 'Case-insensitive compare', align=Align.INLINE)
d.comment(0xA153, 'Mismatch: skip to next entry', align=Align.INLINE)
d.comment(0xA155, 'Match: advance command line', align=Align.INLINE)
d.comment(0xA156, 'Advance table pointer', align=Align.INLINE)
d.comment(0xA157, 'Loop for next character', align=Align.INLINE)
d.comment(0xA159, 'Advance past remaining table chars', align=Align.INLINE)
d.comment(0xA15A, 'Load next table byte', align=Align.INLINE)
d.comment(0xA15D, 'Bit 7 clear: more chars to skip', align=Align.INLINE)
d.comment(0xA15F, 'Check command line terminator', align=Align.INLINE)
d.comment(0xA161, "Is it '.' (abbreviation)?", align=Align.INLINE)
d.comment(0xA163, 'Yes: skip spaces after dot', align=Align.INLINE)
d.comment(0xA165, 'X += 3: skip flags and address bytes', align=Align.INLINE)
d.comment(0xA166, '(continued)', align=Align.INLINE)
d.comment(0xA167, '(continued)', align=Align.INLINE)
d.comment(0xA168, 'Try next table entry', align=Align.INLINE)
d.comment(0xA16A, 'Save Y (end of matched name)', align=Align.INLINE)
d.comment(0xA16B, 'Push position', align=Align.INLINE)
d.comment(0xA16C, 'Load char after matched portion', align=Align.INLINE)
d.comment(0xA16E, 'Y=9: check 10 separator chars', align=Align.INLINE)
d.comment(0xA170, 'Compare with separator table', align=Align.INLINE)
d.comment(0xA173, 'Match: valid command separator', align=Align.INLINE)
d.comment(0xA175, 'Try next separator', align=Align.INLINE)
d.comment(0xA176, 'Loop through separator list', align=Align.INLINE)
d.comment(0xA178, 'No separator match: restore Y', align=Align.INLINE)
d.comment(0xA179, 'Transfer back to Y', align=Align.INLINE)
d.comment(0xA17A, 'Try next table entry', align=Align.INLINE)
d.comment(0xA17C, """Command separator table (9 bytes)

Characters that terminate a command name in the
star command parser. loop_check_sep_table scans
Y down from 8 to 0, comparing each input char
against this table.""")
d.comment(0xA17C, 'Space', align=Align.INLINE)
d.comment(0xA17D, '\'"\' double quote', align=Align.INLINE)
d.comment(0xA17E, "'#' hash", align=Align.INLINE)
d.comment(0xA17F, "'$' dollar", align=Align.INLINE)
d.comment(0xA180, "'&' ampersand", align=Align.INLINE)
d.comment(0xA181, "'*' asterisk", align=Align.INLINE)
d.comment(0xA182, "':' colon", align=Align.INLINE)
d.comment(0xA183, "'@' at-sign", align=Align.INLINE)
d.comment(0xA184, 'CR (carriage return)', align=Align.INLINE)
d.comment(0xA185, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA186, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA187, 'Load next char', align=Align.INLINE)
d.comment(0xA189, 'Is it space?', align=Align.INLINE)
d.comment(0xA18B, 'No: done skipping', align=Align.INLINE)
d.comment(0xA18D, 'Advance past space', align=Align.INLINE)
d.comment(0xA18E, 'Loop for more spaces', align=Align.INLINE)
d.comment(0xA191, 'Load command flags byte', align=Align.INLINE)
d.comment(0xA194, "Shift: check 'no-arg' bit", align=Align.INLINE)
d.comment(0xA195, 'Bit clear: allow arguments', align=Align.INLINE)
d.comment(0xA197, 'Check if line ends here', align=Align.INLINE)
d.comment(0xA199, 'Is it CR?', align=Align.INLINE)
d.comment(0xA19B, 'No: argument present, V clear', align=Align.INLINE)
d.comment(0xA19D, 'CR found: set V (no argument)', align=Align.INLINE)
d.comment(0xA1A0, 'V set: command is valid', align=Align.INLINE)
d.comment(0xA1A2, 'Clear V (argument present)', align=Align.INLINE)
d.comment(0xA1A3, 'C=0: command not found', align=Align.INLINE)
d.comment(0xA1A4, 'Pop saved Y from stack', align=Align.INLINE)
d.comment(0xA1A5, 'Load command line char at Y', align=Align.INLINE)
d.comment(0xA1A7, 'Return (C and V set per result)', align=Align.INLINE)
d.comment(0xA1A8, 'Advance past character', align=Align.INLINE)
d.comment(0xA1A9, 'Load current char', align=Align.INLINE)
d.comment(0xA1AB, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xA1AD, 'Yes: end of input', align=Align.INLINE)
d.comment(0xA1AF, "Is it '.' (abbreviation dot)?", align=Align.INLINE)
d.comment(0xA1B1, 'Yes: skip to next word', align=Align.INLINE)
d.comment(0xA1B3, 'Is it space?', align=Align.INLINE)
d.comment(0xA1B5, 'No: keep scanning', align=Align.INLINE)
d.comment(0xA1B7, 'Skip past separator', align=Align.INLINE)
d.comment(0xA1B8, 'Load next char', align=Align.INLINE)
d.comment(0xA1BA, 'Is it space?', align=Align.INLINE)
d.comment(0xA1BC, 'Yes: skip consecutive spaces', align=Align.INLINE)
d.comment(0xA1BE, 'C=1: have more text to match', align=Align.INLINE)
d.comment(0xA1C1, 'Save text pointer', align=Align.INLINE)
d.comment(0xA1C4, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA1C7, 'Parse command argument (Y=0)', align=Align.INLINE)
d.comment(0xA1CA, 'X=1: buffer index', align=Align.INLINE)
d.comment(0xA1CC, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xA1CF, 'A=2: open for update', align=Align.INLINE)
d.comment(0xA1D1, 'Store open mode', align=Align.INLINE)
d.comment(0xA1D4, 'Y=&12: open file command', align=Align.INLINE)
d.comment(0xA1D6, 'Send open request to server', align=Align.INLINE)
d.comment(0xA1D9, 'Load reply status', align=Align.INLINE)
d.comment(0xA1DC, 'Status 1 (success)?', align=Align.INLINE)
d.comment(0xA1DE, 'No: file not found, try library', align=Align.INLINE)
d.comment(0xA1E0, 'X=3: check 4 handle bytes', align=Align.INLINE)
d.comment(0xA1E2, 'Increment handle byte', align=Align.INLINE)
d.comment(0xA1E5, 'Was &FF (overflow to 0): try next', align=Align.INLINE)
d.comment(0xA1E7, 'Non-zero: handle valid, execute', align=Align.INLINE)
d.comment(0xA1EA, 'Try next handle byte', align=Align.INLINE)
d.comment(0xA1EB, 'Loop until all checked', align=Align.INLINE)
d.comment(0xA1ED, 'Allocate new FCB or raise error', align=Align.INLINE)
d.comment(0xA1F0, 'X=1: open mode index', align=Align.INLINE)
d.comment(0xA1F2, 'Store in l0f05', align=Align.INLINE)
d.comment(0xA1F5, 'Store in l0f06', align=Align.INLINE)
d.comment(0xA1F8, 'X=2', align=Align.INLINE)
d.comment(0xA1F9, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xA1FC, 'Y=6: re-open command', align=Align.INLINE)
d.comment(0xA1FE, 'Send re-open request', align=Align.INLINE)
d.comment(0xA201, 'C set: error on re-open', align=Align.INLINE)
d.comment(0xA203, 'C clear: finalise file opening', align=Align.INLINE)
d.comment(0xA206, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0xA209, 'Load first char of filename', align=Align.INLINE)
d.comment(0xA20C, "Is it '$' (root dir)?", align=Align.INLINE)
d.comment(0xA20E, 'Yes: no library search, error', align=Align.INLINE)
d.comment(0xA210, 'Load library flag byte', align=Align.INLINE)
d.comment(0xA213, 'Bit 7 set: library already tried', align=Align.INLINE)
d.comment(0xA215, 'Rotate bits to check library state', align=Align.INLINE)
d.comment(0xA216, 'Rotate again', align=Align.INLINE)
d.comment(0xA217, 'Bit 7 set: restore from backup', align=Align.INLINE)
d.comment(0xA219, 'Carry set: bad command', align=Align.INLINE)
d.comment(0xA21B, 'X=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0xA21D, 'Find end of filename', align=Align.INLINE)
d.comment(0xA21E, 'Load filename byte', align=Align.INLINE)
d.comment(0xA221, 'Is it CR (end)?', align=Align.INLINE)
d.comment(0xA223, 'No: continue scanning', align=Align.INLINE)
d.comment(0xA225, 'Shift filename right by 8 bytes', align=Align.INLINE)
d.comment(0xA228, 'Store shifted byte', align=Align.INLINE)
d.comment(0xA22B, 'Previous byte', align=Align.INLINE)
d.comment(0xA22C, 'Loop until all shifted', align=Align.INLINE)
d.comment(0xA22E, "X=7: 'Library.' is 8 bytes", align=Align.INLINE)
d.comment(0xA230, "Copy 'Library.' prefix", align=Align.INLINE)
d.comment(0xA233, 'Store prefix byte', align=Align.INLINE)
d.comment(0xA236, 'Previous byte', align=Align.INLINE)
d.comment(0xA237, 'Loop until prefix copied', align=Align.INLINE)
d.comment(0xA239, 'Load library flag', align=Align.INLINE)
d.comment(0xA23C, 'Set bits 5-6: library path active', align=Align.INLINE)
d.comment(0xA23E, 'Store updated flag', align=Align.INLINE)
d.comment(0xA241, 'Retry file open with library path', align=Align.INLINE)
d.comment(0xA243, 'X=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0xA245, 'Restore original filename', align=Align.INLINE)
d.comment(0xA246, 'Load backup byte', align=Align.INLINE)
d.comment(0xA249, 'Store to filename buffer', align=Align.INLINE)
d.comment(0xA24C, 'Is it CR (end)?', align=Align.INLINE)
d.comment(0xA24E, 'No: continue restoring', align=Align.INLINE)
d.comment(0xA250, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA253, 'Set bit 7: library tried', align=Align.INLINE)
d.comment(0xA255, 'Store updated flag', align=Align.INLINE)
d.comment(0xA25A, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA25D, 'Error code &FE', align=Align.INLINE)
d.comment(0xA25F, "Generate 'Bad command' error", align=Align.INLINE)
d.comment(0xA26A, 'X=3: check 4 execution bytes', align=Align.INLINE)
d.comment(0xA26C, 'Increment execution address byte', align=Align.INLINE)
d.comment(0xA26F, 'Non-zero: valid, go to OSCLI', align=Align.INLINE)
d.comment(0xA271, 'Try next byte', align=Align.INLINE)
d.comment(0xA272, 'Loop until all checked', align=Align.INLINE)
d.comment(0xA274, 'Error code &93', align=Align.INLINE)
d.comment(0xA276, "Generate 'No!' error", align=Align.INLINE)
d.comment(0xA27D, 'Load open mode result', align=Align.INLINE)
d.comment(0xA280, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA283, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA284, 'A=0: clear channel status', align=Align.INLINE)
d.comment(0xA286, 'Clear status in channel table', align=Align.INLINE)
d.comment(0xA289, 'Store handle in l1070', align=Align.INLINE)
d.comment(0xA28C, 'Y=3: OSCLI execution', align=Align.INLINE)
d.comment(0xA28E, 'Execute via boot/OSCLI path', align=Align.INLINE)
d.comment(0xA299, 'Copy command argument to buffer', align=Align.INLINE)
d.comment(0xA29C, 'Y=0', align=Align.INLINE)
d.comment(0xA29E, 'C=0 for GSINIT', align=Align.INLINE)
d.comment(0xA29F, 'Initialise GS string read', align=Align.INLINE)
d.comment(0xA2A2, 'Read next GS character', align=Align.INLINE)
d.comment(0xA2A5, 'C clear: more chars', align=Align.INLINE)
d.comment(0xA2A7, 'Back up one position', align=Align.INLINE)
d.comment(0xA2A8, 'Skip trailing spaces', align=Align.INLINE)
d.comment(0xA2A9, 'Load next char', align=Align.INLINE)
d.comment(0xA2AB, 'Is it space?', align=Align.INLINE)
d.comment(0xA2AD, 'Yes: skip it', align=Align.INLINE)
d.comment(0xA2AF, 'Check for CR (end of line)', align=Align.INLINE)
d.comment(0xA2B1, 'C=0 for addition', align=Align.INLINE)
d.comment(0xA2B2, 'Transfer Y offset to A', align=Align.INLINE)
d.comment(0xA2B3, 'Add to text pointer low', align=Align.INLINE)
d.comment(0xA2B5, 'Store as command tail pointer low', align=Align.INLINE)
d.comment(0xA2B8, 'Load text pointer high', align=Align.INLINE)
d.comment(0xA2BA, 'Add carry', align=Align.INLINE)
d.comment(0xA2BC, 'Store as command tail pointer high', align=Align.INLINE)
d.comment(0xA2BF, 'Save text pointer for later', align=Align.INLINE)
d.comment(0xA2C2, 'X=&0E: OSWORD parameter offset', align=Align.INLINE)
d.comment(0xA2C4, 'Store as block offset high', align=Align.INLINE)
d.comment(0xA2C6, 'A=&0E: OSWORD parameter size', align=Align.INLINE)
d.comment(0xA2C8, 'Store as options pointer', align=Align.INLINE)
d.comment(0xA2CA, 'Store to l0e16', align=Align.INLINE)
d.comment(0xA2CD, 'X=&4A: FS command table offset', align=Align.INLINE)
d.comment(0xA2CF, 'Y=5', align=Align.INLINE)
d.comment(0xA2D1, 'Execute FS command iteration', align=Align.INLINE)
d.comment(0xA2D4, 'Load tube flag', align=Align.INLINE)
d.comment(0xA2D7, 'Zero: no tube transfer needed', align=Align.INLINE)
d.comment(0xA2D9, 'AND with l0f0b', align=Align.INLINE)
d.comment(0xA2DC, 'AND with l0f0c', align=Align.INLINE)
d.comment(0xA2DF, 'All &FF?', align=Align.INLINE)
d.comment(0xA2E1, 'Yes: no tube transfer needed', align=Align.INLINE)
d.comment(0xA2E3, 'Claim tube for data transfer', align=Align.INLINE)
d.comment(0xA2E6, 'X=9: parameter count', align=Align.INLINE)
d.comment(0xA2E8, 'Y=&0F: parameter offset', align=Align.INLINE)
d.comment(0xA2EA, 'A=4: tube transfer type', align=Align.INLINE)
d.comment(0xA2EC, 'Dispatch tube address/data', align=Align.INLINE)
d.comment(0xA2EF, 'A=1', align=Align.INLINE)
d.comment(0xA2F1, 'Dispatch via indirect vector', align=Align.INLINE)
d.comment(0xA2F4, 'Find station with bit 3 set', align=Align.INLINE)
d.comment(0xA2F7, 'Return with last flag state', align=Align.INLINE)
d.comment(0xA2FA, 'Flip/set station boot config', align=Align.INLINE)
d.comment(0xA2FD, 'Return with last flag state', align=Align.INLINE)
d.comment(0xA300, 'X=&10: scan 16 slots (15 to 0)', align=Align.INLINE)
d.comment(0xA302, 'Clear V', align=Align.INLINE)
d.comment(0xA303, 'Try next slot', align=Align.INLINE)
d.comment(0xA304, 'All slots checked: not found', align=Align.INLINE)
d.comment(0xA306, 'Compare station/network', align=Align.INLINE)
d.comment(0xA309, 'No match: try next', align=Align.INLINE)
d.comment(0xA30B, 'Load slot status byte', align=Align.INLINE)
d.comment(0xA30E, 'Test bit 2 (PS active flag)?', align=Align.INLINE)
d.comment(0xA310, 'Not set: try next', align=Align.INLINE)
d.comment(0xA312, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA313, 'Store Y in slot data', align=Align.INLINE)
d.comment(0xA316, 'Set V (found match)', align=Align.INLINE)
d.comment(0xA319, 'Store Y to l0e02', align=Align.INLINE)
d.comment(0xA31C, 'V set: found, skip allocation', align=Align.INLINE)
d.comment(0xA31E, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA31F, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA322, 'Store allocation result', align=Align.INLINE)
d.comment(0xA325, 'Zero: failed, restore context', align=Align.INLINE)
d.comment(0xA327, 'A=&26: station flags value', align=Align.INLINE)
d.comment(0xA32B, 'X=&10: scan 16 slots (15 to 0)', align=Align.INLINE)
d.comment(0xA32D, 'Clear V', align=Align.INLINE)
d.comment(0xA32E, 'Try next slot', align=Align.INLINE)
d.comment(0xA32F, 'All slots checked: not found', align=Align.INLINE)
d.comment(0xA331, 'Compare station/network', align=Align.INLINE)
d.comment(0xA334, 'No match: try next', align=Align.INLINE)
d.comment(0xA336, 'Load slot status byte', align=Align.INLINE)
d.comment(0xA339, 'Test bit 3 (FS active flag)?', align=Align.INLINE)
d.comment(0xA33B, 'Not set: try next', align=Align.INLINE)
d.comment(0xA33D, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA33E, 'Store Y in slot data', align=Align.INLINE)
d.comment(0xA341, 'Set V (found match)', align=Align.INLINE)
d.comment(0xA344, 'Store Y to l0e03', align=Align.INLINE)
d.comment(0xA347, 'V set: found, skip allocation', align=Align.INLINE)
d.comment(0xA349, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA34A, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA34D, 'Store allocation result', align=Align.INLINE)
d.comment(0xA350, 'Zero: failed, restore context', align=Align.INLINE)
d.comment(0xA352, 'A=&2A: station flags value', align=Align.INLINE)
d.comment(0x9146, 'Store as string pointer low', align=Align.INLINE)
d.comment(0x9149, 'Store as string pointer high', align=Align.INLINE)
d.comment(0x914B, 'Y=0: index for indirect loads', align=Align.INLINE)
d.comment(0x914F, 'No page crossing', align=Align.INLINE)
d.comment(0x9151, 'Carry into high byte', align=Align.INLINE)
d.comment(0x9157, 'Save string pointer on stack', align=Align.INLINE)
d.comment(0x9159, '(push low byte)', align=Align.INLINE)
d.comment(0x915A, 'Save pointer high byte', align=Align.INLINE)
d.comment(0x915C, '(push high byte)', align=Align.INLINE)
d.comment(0x9162, 'Restore string pointer high', align=Align.INLINE)
d.comment(0x9163, 'Store pointer high', align=Align.INLINE)
d.comment(0x9165, 'Restore string pointer low', align=Align.INLINE)
d.comment(0x9166, 'Store pointer low', align=Align.INLINE)
d.comment(0x9168, 'Loop for next character', align=Align.INLINE)
d.comment(0x916E, 'Clear accumulator', align=Align.INLINE)
d.comment(0x9170, 'Initialise result to zero', align=Align.INLINE)
d.comment(0x9172, 'Get first character of argument', align=Align.INLINE)
d.comment(0x9174, "Is it '&' (hex prefix)?", align=Align.INLINE)
d.comment(0x9176, 'No: try decimal path', align=Align.INLINE)
d.comment(0x9178, "Skip '&' prefix", align=Align.INLINE)
d.comment(0x9179, 'Get first hex digit', align=Align.INLINE)
d.comment(0x917B, 'C always set from CMP: validate digit', align=Align.INLINE)
d.comment(0x917D, 'Advance to next character', align=Align.INLINE)
d.comment(0x917E, 'Get next character', align=Align.INLINE)
d.comment(0x9180, "Is it '.' (net.station separator)?", align=Align.INLINE)
d.comment(0x9182, 'Yes: handle dot separator', align=Align.INLINE)
d.comment(0x9184, "Below '!' (space/control)?", align=Align.INLINE)
d.comment(0x9186, 'Yes: end of number', align=Align.INLINE)
d.comment(0x9188, "Below '0'?", align=Align.INLINE)
d.comment(0x918A, 'Not a digit: bad hex', align=Align.INLINE)
d.comment(0x918C, "Above '9'?", align=Align.INLINE)
d.comment(0x918E, 'Decimal digit: extract value', align=Align.INLINE)
d.comment(0x9190, 'Force uppercase', align=Align.INLINE)
d.comment(0x9192, "Map 'A'-'F' to &FA-&FF", align=Align.INLINE)
d.comment(0x9194, 'Overflow: not A-F', align=Align.INLINE)
d.comment(0x9196, 'Valid hex letter (A-F)?', align=Align.INLINE)
d.comment(0x9198, 'Below A: bad hex', align=Align.INLINE)
d.comment(0x919A, 'Extract digit value (0-15)', align=Align.INLINE)
d.comment(0x919C, 'Save current digit', align=Align.INLINE)
d.comment(0x919E, 'Load running result', align=Align.INLINE)
d.comment(0x91A0, 'Would shift overflow a byte?', align=Align.INLINE)
d.comment(0x91A2, 'Yes: overflow error', align=Align.INLINE)
d.comment(0x91A4, 'Shift result left 4 (x16)', align=Align.INLINE)
d.comment(0x91A5, '(shift 2)', align=Align.INLINE)
d.comment(0x91A6, '(shift 3)', align=Align.INLINE)
d.comment(0x91A7, '(shift 4)', align=Align.INLINE)
d.comment(0x91A8, 'Add new hex digit', align=Align.INLINE)
d.comment(0x91AA, 'Store updated result', align=Align.INLINE)
d.comment(0x91AC, 'Loop for next hex digit', align=Align.INLINE)
d.comment(0x91AE, 'Get current character', align=Align.INLINE)
d.comment(0x91B0, "Is it '.' (net.station separator)?", align=Align.INLINE)
d.comment(0x91B2, 'Yes: handle dot separator', align=Align.INLINE)
d.comment(0x91B4, "Below '!' (space/control)?", align=Align.INLINE)
d.comment(0x91B6, 'Yes: end of number', align=Align.INLINE)
d.comment(0x91B8, 'Is it a decimal digit?', align=Align.INLINE)
d.comment(0x91BB, "No: 'Bad number' error", align=Align.INLINE)
d.comment(0x91BD, 'Extract digit value (0-9)', align=Align.INLINE)
d.comment(0x91BF, 'Save current digit', align=Align.INLINE)
d.comment(0x91C1, 'result * 2', align=Align.INLINE)
d.comment(0x91C3, 'Overflow', align=Align.INLINE)
d.comment(0x91C5, 'Load result * 2', align=Align.INLINE)
d.comment(0x91C7, 'result * 4', align=Align.INLINE)
d.comment(0x91C8, 'Overflow', align=Align.INLINE)
d.comment(0x91CA, 'result * 8', align=Align.INLINE)
d.comment(0x91CB, 'Overflow', align=Align.INLINE)
d.comment(0x91CD, '* 8 + * 2 = result * 10', align=Align.INLINE)
d.comment(0x91CF, 'Overflow', align=Align.INLINE)
d.comment(0x91D1, 'result * 10 + new digit', align=Align.INLINE)
d.comment(0x91D3, 'Overflow', align=Align.INLINE)
d.comment(0x91D5, 'Store updated result', align=Align.INLINE)
d.comment(0x91D7, 'Advance to next character', align=Align.INLINE)
d.comment(0x91D8, 'Loop (always branches)', align=Align.INLINE)
d.comment(0x91DA, 'Check parsing mode', align=Align.INLINE)
d.comment(0x91DC, 'Bit 7 clear: net.station mode', align=Align.INLINE)
d.comment(0x91DE, 'Decimal-only mode: get result', align=Align.INLINE)
d.comment(0x91E0, "Zero: 'Bad parameter'", align=Align.INLINE)
d.comment(0x91E2, 'Return with result in A', align=Align.INLINE)
d.comment(0x91E3, 'Get parsed station number', align=Align.INLINE)
d.comment(0x91E5, 'Station 255 is reserved', align=Align.INLINE)
d.comment(0x91E7, "255: 'Bad station number'", align=Align.INLINE)
d.comment(0x91E9, 'Reload result', align=Align.INLINE)
d.comment(0x91EB, 'Non-zero: valid station', align=Align.INLINE)
d.comment(0x91ED, 'Zero result: check if dot was seen', align=Align.INLINE)
d.comment(0x91EF, "No dot and zero: 'Bad station number'", align=Align.INLINE)
d.comment(0x91F1, 'Check character before current pos', align=Align.INLINE)
d.comment(0x91F2, 'Load previous character', align=Align.INLINE)
d.comment(0x91F4, 'Restore Y', align=Align.INLINE)
d.comment(0x91F5, "Was previous char '.'?", align=Align.INLINE)
d.comment(0x91F7, "No: 'Bad station number'", align=Align.INLINE)
d.comment(0x91F9, 'C=1: number was parsed', align=Align.INLINE)
d.comment(0x91FA, 'Return (result in fs_load_addr_2)', align=Align.INLINE)
d.comment(0x91FB, 'Check if dot already seen', align=Align.INLINE)
d.comment(0x91FD, "Already seen: 'Bad number'", align=Align.INLINE)
d.comment(0x91FF, 'Set dot-seen flag', align=Align.INLINE)
d.comment(0x9201, 'Get network number (before dot)', align=Align.INLINE)
d.comment(0x9203, 'Network 255 is reserved', align=Align.INLINE)
d.comment(0x9205, "255: 'Bad network number'", align=Align.INLINE)
d.comment(0x9207, 'Return to caller with network part', align=Align.INLINE)
d.comment(0x9208, 'Error code &F1', align=Align.INLINE)
d.comment(0x920A, "Generate 'Bad hex' error", align=Align.INLINE)
d.comment(0x9211, 'Test parsing mode', align=Align.INLINE)
d.comment(0x9213, "Decimal mode: 'Bad parameter'", align=Align.INLINE)
d.comment(0x9215, 'Error code &D0', align=Align.INLINE)
d.comment(0x9217, "Generate 'Bad station number' error", align=Align.INLINE)
d.comment(0x9229, 'Error code &F0', align=Align.INLINE)
d.comment(0x922B, "Generate 'Bad number' error", align=Align.INLINE)
d.comment(0x9235, 'Error code &94', align=Align.INLINE)
d.comment(0x9237, "Generate 'Bad parameter' error", align=Align.INLINE)
d.comment(0x9244, 'Error code &D1', align=Align.INLINE)
d.comment(0x9246, "Generate 'Bad network number' error", align=Align.INLINE)
d.comment(0x9258, "Is it '&' (hex prefix)?", align=Align.INLINE)
d.comment(0x925A, 'Yes: return C set (not decimal)', align=Align.INLINE)
d.comment(0x925C, "Is it '.' (separator)?", align=Align.INLINE)
d.comment(0x925E, 'Yes: return C set (not decimal)', align=Align.INLINE)
d.comment(0x9260, "Above '9'?", align=Align.INLINE)
d.comment(0x9262, 'Yes: not a digit', align=Align.INLINE)
d.comment(0x9264, "Below '0'? C clear if so", align=Align.INLINE)
d.comment(0x9266, "Return: C set if '0'-'9'", align=Align.INLINE)
d.comment(0x9267, 'C=0: not a digit', align=Align.INLINE)
d.comment(0x9268, 'Return', align=Align.INLINE)
d.comment(0x9269, 'Offset &0E in directory entry', align=Align.INLINE)
d.comment(0x926B, 'Load raw access byte', align=Align.INLINE)
d.comment(0x926D, 'Mask to 6 access bits', align=Align.INLINE)
d.comment(0x926F, 'X=4: start encoding at bit 4', align=Align.INLINE)
d.comment(0x9271, 'ALWAYS branch to encoder', align=Align.INLINE)
d.comment(0x9273, 'Mask to 5 protection bits', align=Align.INLINE)
d.comment(0x9275, 'X=&FF: start encoding at bit 0', align=Align.INLINE)
d.comment(0x9277, 'Save remaining bits', align=Align.INLINE)
d.comment(0x9279, 'Clear encoded result', align=Align.INLINE)
d.comment(0x927B, 'Advance to next table position', align=Align.INLINE)
d.comment(0x927C, 'Shift out lowest source bit', align=Align.INLINE)
d.comment(0x927E, 'Bit clear: skip this position', align=Align.INLINE)
d.comment(0x9280, 'Bit set: OR in encoded value', align=Align.INLINE)
d.comment(0x9283, 'More bits to process', align=Align.INLINE)
d.comment(0x9285, 'Return encoded access in A', align=Align.INLINE)
d.comment(0x9286, """Protection/access bit encode table

11-entry lookup table used by get_prot_bits and
get_access_bits to remap attribute bits between
the file server protocol format and the local
representation. The encoding loop shifts out each
source bit; for each set bit, the corresponding
table entry is ORed into the result.

Indices 0-4: used by get_prot_bits (5-bit input).
Some entries set multiple output bits (expansion).

Indices 5-10: used by get_access_bits (6-bit input
from directory entry offset &0E). Each entry sets
exactly one output bit (pure permutation).""")
d.comment(0x9286, 'Bit 0: &50 = %01010000 (bits 4,6)', align=Align.INLINE)
d.comment(0x9287, 'Bit 1: &20 = %00100000 (bit 5)', align=Align.INLINE)
d.comment(0x9288, 'Bit 2: &05 = %00000101 (bits 0,2)', align=Align.INLINE)
d.comment(0x9289, 'Bit 3: &02 = %00000010 (bit 1)', align=Align.INLINE)
d.comment(0x928A, 'Bit 4: &88 = %10001000 (bits 3,7)', align=Align.INLINE)
d.comment(0x928B, 'Bit 0: &04 = %00000100 (bit 2)', align=Align.INLINE)
d.comment(0x928C, 'Bit 1: &08 = %00001000 (bit 3)', align=Align.INLINE)
d.comment(0x928D, 'Bit 2: &80 = %10000000 (bit 7)', align=Align.INLINE)
d.comment(0x928E, 'Bit 3: &10 = %00010000 (bit 4)', align=Align.INLINE)
d.comment(0x928F, 'Bit 4: &01 = %00000001 (bit 0)', align=Align.INLINE)
d.comment(0x9290, 'Bit 5: &02 = %00000010 (bit 1)', align=Align.INLINE)
d.comment(0x9291, 'Set text pointer low', align=Align.INLINE)
d.comment(0x9293, 'Set text pointer high', align=Align.INLINE)
d.comment(0x9295, 'Store transfer byte count', align=Align.INLINE)
d.comment(0x9297, 'Store source pointer low', align=Align.INLINE)
d.comment(0x9299, 'Store source pointer high', align=Align.INLINE)
d.comment(0x929B, 'Store options pointer low', align=Align.INLINE)
d.comment(0x929D, 'Store options pointer high', align=Align.INLINE)
d.comment(0x929F, 'Save processor flags', align=Align.INLINE)
d.comment(0x92A0, 'Clear bit 0 of escape flag', align=Align.INLINE)
d.comment(0x92A2, 'Restore processor flags', align=Align.INLINE)
d.comment(0x92A3, 'Return', align=Align.INLINE)
d.comment(0x92A4, 'Compare 5 bytes (indices 4 down to 1)', align=Align.INLINE)
d.comment(0x92A6, 'Load byte from handle buffer', align=Align.INLINE)
d.comment(0x92A8, 'Compare with channel handle', align=Align.INLINE)
d.comment(0x92AA, 'Mismatch: return Z=0', align=Align.INLINE)
d.comment(0x92AC, 'Next byte', align=Align.INLINE)
d.comment(0x92AD, 'Loop until all compared', align=Align.INLINE)
d.comment(0x92AF, 'Return: Z=1 if all 5 matched', align=Align.INLINE)
d.comment(0x92B0, 'Unreachable code', align=Align.INLINE)
d.comment(0x92B2, '(dead)', align=Align.INLINE)
d.comment(0x92B4, '(dead)', align=Align.INLINE)
d.comment(0x92B5, 'Save processor flags', align=Align.INLINE)
d.comment(0x92B6, 'Save A', align=Align.INLINE)
d.comment(0x92B7, 'Transfer X to A', align=Align.INLINE)
d.comment(0x92B8, 'Save original X', align=Align.INLINE)
d.comment(0x92B9, 'Get stack pointer', align=Align.INLINE)
d.comment(0x92BA, 'Read original A from stack', align=Align.INLINE)
d.comment(0x92BD, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92C0, 'No channel found: skip', align=Align.INLINE)
d.comment(0x92C2, 'Bit 6: connection active flag', align=Align.INLINE)
d.comment(0x92C4, 'Set active flag in channel table', align=Align.INLINE)
d.comment(0x92C7, 'Store updated status', align=Align.INLINE)
d.comment(0x92CA, 'ALWAYS branch to exit', align=Align.INLINE)
d.comment(0x92CC, 'Save processor flags', align=Align.INLINE)
d.comment(0x92CD, 'Save A', align=Align.INLINE)
d.comment(0x92CE, 'Transfer X to A', align=Align.INLINE)
d.comment(0x92CF, 'Save original X', align=Align.INLINE)
d.comment(0x92D0, 'Get stack pointer', align=Align.INLINE)
d.comment(0x92D1, 'Read original A from stack', align=Align.INLINE)
d.comment(0x92D4, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92D7, 'No channel found: skip', align=Align.INLINE)
d.comment(0x92D9, 'Bit 6 clear mask (&BF = ~&40)', align=Align.INLINE)
d.comment(0x92DB, 'Clear active flag in channel table', align=Align.INLINE)
d.comment(0x92DE, 'Store updated status', align=Align.INLINE)
d.comment(0x92E1, 'Restore X', align=Align.INLINE)
d.comment(0x92E2, 'Transfer back to X', align=Align.INLINE)
d.comment(0x92E3, 'Restore A', align=Align.INLINE)
d.comment(0x92E4, 'Restore processor flags', align=Align.INLINE)
d.comment(0x92E5, 'Return', align=Align.INLINE)
d.comment(0xA4EE, 'CLC so SBC subtracts value+1', align=Align.INLINE)
d.comment(0xA4EF, 'A = OSWORD number', align=Align.INLINE)
d.comment(0xA4F1, 'A = OSWORD - &0E (CLC+SBC = -&0E)', align=Align.INLINE)
d.comment(0xA4F3, 'Below &0E: not ours, return', align=Align.INLINE)
d.comment(0xA4F5, 'Index >= 7? (OSWORD > &14)', align=Align.INLINE)
d.comment(0xA4F7, 'Above &14: not ours, return', align=Align.INLINE)
d.comment(0xA4F9, 'X=OSWORD handler index (0-6)', align=Align.INLINE)
d.comment(0xA509, 'Set up dispatch and save state', align=Align.INLINE)
d.comment(0xA4FA, 'Y=6: save 6 workspace bytes', align=Align.INLINE)
d.comment(0xA4FC, 'Load current workspace byte', align=Align.INLINE)
d.comment(0xA4FF, 'Save on stack', align=Align.INLINE)
d.comment(0xA50C, 'Y=&FA: restore 6 workspace bytes', align=Align.INLINE)
d.comment(0xA50E, 'Restore saved workspace byte', align=Align.INLINE)
d.comment(0xA500, 'Load OSWORD parameter byte', align=Align.INLINE)
d.comment(0xA50F, 'Store to osword_flag workspace', align=Align.INLINE)
d.comment(0xA512, 'Next byte', align=Align.INLINE)
d.comment(0xA503, 'Copy parameter to workspace', align=Align.INLINE)
d.comment(0xA515, 'Return from svc_8_osword', align=Align.INLINE)
d.comment(0xA513, 'Loop until all 6 restored', align=Align.INLINE)
d.comment(0xA506, 'Next byte down', align=Align.INLINE)
d.comment(0xA507, 'Loop for all 6 bytes', align=Align.INLINE)
d.comment(0xA516, 'X = OSWORD index (0-6)', align=Align.INLINE)
d.comment(0xA516, 'Load handler address high byte', align=Align.INLINE)
d.comment(0xA519, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0xA51A, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA51D, 'Push low byte for RTS dispatch', align=Align.INLINE)
d.comment(0xA51E, 'Copy 3 bytes (Y=2,1,0)', align=Align.INLINE)
d.comment(0xA520, 'Load from osword_flag workspace', align=Align.INLINE)
d.comment(0xA523, 'Store to RX buffer', align=Align.INLINE)
d.comment(0xA51E, 'Load PB byte 0 (OSWORD sub-code)', align=Align.INLINE)
d.comment(0xA520, 'Clear service state', align=Align.INLINE)
d.comment(0xA522, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0xA531, 'Test station active flag', align=Align.INLINE)
d.comment(0xA534, 'Not active: just return', align=Align.INLINE)
d.comment(0xA536, 'Restore A (OSWORD sub-code)', align=Align.INLINE)
d.comment(0xA536, 'Sub-code = 4? (read clock)', align=Align.INLINE)
d.comment(0xA538, 'Yes: handle clock read', align=Align.INLINE)
d.comment(0xA53A, 'Other sub-codes: set state = 8', align=Align.INLINE)
d.comment(0xA53C, 'Store service state', align=Align.INLINE)
d.comment(0xA53E, 'Return', align=Align.INLINE)
d.comment(0xA53F, 'X=0: start of TX control block', align=Align.INLINE)
d.comment(0xA541, 'Y=&10: length of TXCB to save', align=Align.INLINE)
d.comment(0xA543, 'Save current TX control block', align=Align.INLINE)
d.comment(0xA546, 'Load seconds from clock workspace', align=Align.INLINE)
d.comment(0xA549, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA54C, 'Store BCD seconds', align=Align.INLINE)
d.comment(0xA54F, 'Load minutes from clock workspace', align=Align.INLINE)
d.comment(0xA552, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA555, 'Store BCD minutes', align=Align.INLINE)
d.comment(0xA558, 'Load hours from clock workspace', align=Align.INLINE)
d.comment(0xA55B, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA55E, 'Store BCD hours', align=Align.INLINE)
d.comment(0xA561, 'Clear hours high position', align=Align.INLINE)
d.comment(0xA563, 'Store zero', align=Align.INLINE)
d.comment(0xA566, 'Load day+month byte', align=Align.INLINE)
d.comment(0xA569, 'Save for later high nibble extract', align=Align.INLINE)
d.comment(0xA56A, 'Load day value', align=Align.INLINE)
d.comment(0xA56D, 'Convert day to BCD', align=Align.INLINE)
d.comment(0xA570, 'Store BCD day', align=Align.INLINE)
d.comment(0xA573, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA574, 'Save again for month extract', align=Align.INLINE)
d.comment(0xA575, 'Mask low nibble (month low bits)', align=Align.INLINE)
d.comment(0xA577, 'Convert to BCD', align=Align.INLINE)
d.comment(0xA57A, 'Store BCD month', align=Align.INLINE)
d.comment(0xA57D, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA57E, 'Shift high nibble down', align=Align.INLINE)
d.comment(0xA57F, 'Continue shifting', align=Align.INLINE)
d.comment(0xA580, 'Continue shifting', align=Align.INLINE)
d.comment(0xA581, '4th shift: isolate high nibble', align=Align.INLINE)
d.comment(0xA582, 'Add &51 for year offset + carry', align=Align.INLINE)
d.comment(0xA584, 'Convert year to BCD', align=Align.INLINE)
d.comment(0xA587, 'Store BCD year', align=Align.INLINE)
d.comment(0xA58A, 'Copy 7 bytes (Y=6 down to 0)', align=Align.INLINE)
d.comment(0xA58C, 'Load BCD byte from workspace', align=Align.INLINE)
d.comment(0xA58F, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA591, 'Next byte down', align=Align.INLINE)
d.comment(0xA592, 'Loop for all 7 bytes', align=Align.INLINE)
d.comment(0xA594, 'Return', align=Align.INLINE)
d.comment(0xA595, 'Save processor flags (decimal mode)', align=Align.INLINE)
d.comment(0xA596, 'X = binary count', align=Align.INLINE)
d.comment(0xA597, 'Zero: result is 0, skip loop', align=Align.INLINE)
d.comment(0xA599, 'Set decimal mode for BCD add', align=Align.INLINE)
d.comment(0xA59A, 'Start BCD result at 0', align=Align.INLINE)
d.comment(0xA59C, 'Clear carry for BCD add', align=Align.INLINE)
d.comment(0xA59D, 'Add 1 in decimal mode', align=Align.INLINE)
d.comment(0xA59F, 'Count down binary value', align=Align.INLINE)
d.comment(0xA5A0, 'Loop until zero', align=Align.INLINE)
d.comment(0xA5A2, 'Restore flags (clears decimal mode)', align=Align.INLINE)
d.comment(0xA5A3, 'Return with BCD result in A', align=Align.INLINE)
d.comment(0xA5A4, 'Shift ws_0d60 left (status flag)', align=Align.INLINE)
d.comment(0xA5A7, 'A = Y (saved index)', align=Align.INLINE)
d.comment(0xA5A8, 'C=1: transmit active path', align=Align.INLINE)
d.comment(0xA5AA, 'C=0: store Y to parameter block', align=Align.INLINE)
d.comment(0xA5AC, 'Return (transmit not active)', align=Align.INLINE)
d.comment(0xA5AD, 'Set workspace high byte', align=Align.INLINE)
d.comment(0xA5AF, 'Copy to ws_ptr_lo', align=Align.INLINE)
d.comment(0xA5B1, 'Also set as NMI TX block high', align=Align.INLINE)
d.comment(0xA5B3, 'Low byte = &6F', align=Align.INLINE)
d.comment(0xA5B5, 'Set osword_flag', align=Align.INLINE)
d.comment(0xA5B7, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xA5B9, 'X=&0F: byte count for copy', align=Align.INLINE)
d.comment(0xA5BB, 'Copy data and begin transmission', align=Align.INLINE)
d.comment(0xA5BE, 'Jump to begin Econet transmission', align=Align.INLINE)
d.comment(0xA5C1, 'Load NFS workspace page high byte', align=Align.INLINE)
d.comment(0xA5C3, 'Set workspace pointer high', align=Align.INLINE)
d.comment(0xA5C5, 'Set workspace pointer low from Y', align=Align.INLINE)
d.comment(0xA5C7, 'Rotate Econet flags (save interrupt state)', align=Align.INLINE)
d.comment(0xA5CA, 'Y=OSWORD flag (slot specifier)', align=Align.INLINE)
d.comment(0xA5CB, 'Store OSWORD flag', align=Align.INLINE)
d.comment(0xA5CD, 'Non-zero: use specified slot', align=Align.INLINE)
d.comment(0xA5CF, 'A=3: start searching from slot 3', align=Align.INLINE)
d.comment(0xA5D1, 'Convert slot to 2-bit workspace index', align=Align.INLINE)
d.comment(0xA5D4, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5D6, 'Shift index right (divide by 4)', align=Align.INLINE)
d.comment(0xA5D7, 'Continue shift', align=Align.INLINE)
d.comment(0xA5D8, 'Transfer to X as workspace offset', align=Align.INLINE)
d.comment(0xA5D9, 'Load workspace byte at offset', align=Align.INLINE)
d.comment(0xA5DB, 'Zero: slot empty, store result', align=Align.INLINE)
d.comment(0xA5DD, "Compare with &3F ('?' marker)", align=Align.INLINE)
d.comment(0xA5DF, 'Match: slot found for receive', align=Align.INLINE)
d.comment(0xA5E1, 'Try next slot index', align=Align.INLINE)
d.comment(0xA5E2, 'Transfer back to A', align=Align.INLINE)
d.comment(0xA5E3, 'Loop back (A != 0)', align=Align.INLINE)
d.comment(0xA5E5, 'Transfer found slot to A', align=Align.INLINE)
d.comment(0xA5E6, 'X=0: index for indirect store', align=Align.INLINE)
d.comment(0xA5E8, 'Store slot number to PB byte 0', align=Align.INLINE)
d.comment(0xA5EA, 'Convert specified slot to workspace index', align=Align.INLINE)
d.comment(0xA5ED, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5EF, 'Y=Y-1: adjust workspace offset', align=Align.INLINE)
d.comment(0xA5F0, 'Update workspace pointer low', align=Align.INLINE)
d.comment(0xA5F2, 'A=&C0: slot active marker', align=Align.INLINE)
d.comment(0xA5F4, 'Y=1: workspace byte offset', align=Align.INLINE)
d.comment(0xA5F6, 'X=&0B: byte count for PB copy', align=Align.INLINE)
d.comment(0xA5F8, 'Compare Y with OSWORD flag', align=Align.INLINE)
d.comment(0xA5FA, 'Add workspace byte (check slot state)', align=Align.INLINE)
d.comment(0xA5FC, 'Zero: slot ready, copy PB and mark', align=Align.INLINE)
d.comment(0xA5FE, 'Negative: slot busy, increment and retry', align=Align.INLINE)
d.comment(0xA600, 'Clear carry for PB copy', align=Align.INLINE)
d.comment(0xA601, 'Copy PB byte to workspace slot', align=Align.INLINE)
d.comment(0xA604, 'C set: copy done, finish', align=Align.INLINE)
d.comment(0xA606, "A=&3F: mark slot as pending ('?')", align=Align.INLINE)
d.comment(0xA608, 'Y=1: workspace flag offset', align=Align.INLINE)
d.comment(0xA60A, 'Store pending marker to workspace', align=Align.INLINE)
d.comment(0xA60E, 'Increment retry counter', align=Align.INLINE)
d.comment(0xA610, 'Non-zero: retry copy loop', align=Align.INLINE)
d.comment(0xA612, 'Decrement Y (adjust offset)', align=Align.INLINE)
d.comment(0xA613, 'Store result A to PB via Y', align=Align.INLINE)
d.comment(0xA615, 'Rotate Econet flags back (restore state)', align=Align.INLINE)
d.comment(0xA618, 'Return from OSWORD 11 handler', align=Align.INLINE)
d.comment(0xA619, 'Set workspace from RX ptr high', align=Align.INLINE)
d.comment(0xA61B, 'Store to ws_ptr_lo', align=Align.INLINE)
d.comment(0xA61D, 'Y=&7F: last byte of RX buffer', align=Align.INLINE)
d.comment(0xA61F, 'Load port/count from RX buffer', align=Align.INLINE)
d.comment(0xA621, 'Y=&80: set workspace pointer', align=Align.INLINE)
d.comment(0xA622, 'Store as osword_flag', align=Align.INLINE)
d.comment(0xA624, 'X = port/count value', align=Align.INLINE)
d.comment(0xA625, 'X-1: adjust count', align=Align.INLINE)
d.comment(0xA626, 'Y=0 for copy', align=Align.INLINE)
d.comment(0xA628, 'Copy workspace data', align=Align.INLINE)
d.comment(0xA62B, 'Update state and return', align=Align.INLINE)
d.comment(0xA62E, 'X = sub-code', align=Align.INLINE)
d.comment(0xA62F, 'Sub-code < &13?', align=Align.INLINE)
d.comment(0xA631, 'Out of range: return', align=Align.INLINE)
d.comment(0xA633, 'Load handler address high byte', align=Align.INLINE)
d.comment(0xA636, 'Push high byte', align=Align.INLINE)
d.comment(0xA637, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA63A, 'Push low byte', align=Align.INLINE)
d.comment(0xA63B, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0xA64E, 'hi-sub 0: read FS station', align=Align.INLINE)
d.comment(0xA64F, 'hi-sub 1: set FS station', align=Align.INLINE)
d.comment(0xA650, 'hi-sub 2: read workspace pair', align=Align.INLINE)
d.comment(0xA651, 'hi-sub 3: write workspace pair', align=Align.INLINE)
d.comment(0xA652, 'hi-sub 4: read protection mask', align=Align.INLINE)
d.comment(0xA653, 'hi-sub 5: write protection mask', align=Align.INLINE)
d.comment(0xA654, 'hi-sub 6: read FCB handles', align=Align.INLINE)
d.comment(0xA655, 'hi-sub 7: set FCB handles', align=Align.INLINE)
d.comment(0xA656, 'hi-sub 8: read RX flag', align=Align.INLINE)
d.comment(0xA657, 'hi-sub 9: read RX port', align=Align.INLINE)
d.comment(0xA658, 'hi-sub 10: read error flag', align=Align.INLINE)
d.comment(0xA659, 'hi-sub 11: read context byte', align=Align.INLINE)
d.comment(0xA65A, 'hi-sub 12: read CSD path', align=Align.INLINE)
d.comment(0xA65B, 'hi-sub 13: write CSD path', align=Align.INLINE)
d.comment(0xA65C, 'hi-sub 14: read free buffers', align=Align.INLINE)
d.comment(0xA65D, 'hi-sub 15: read 3 context bytes', align=Align.INLINE)
d.comment(0xA65E, 'hi-sub 16: write 3 context bytes', align=Align.INLINE)
d.comment(0xA65F, 'hi-sub 17: query bridge status', align=Align.INLINE)
d.comment(0xA6F8, 'C=0: skip PB-to-WS copy', align=Align.INLINE)
d.comment(0xA6FA, 'C=1: load from parameter block', align=Align.INLINE)
d.comment(0xA6FC, 'Store to workspace', align=Align.INLINE)
d.comment(0xA6FE, 'Load from workspace', align=Align.INLINE)
d.comment(0xA700, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA702, 'Next byte', align=Align.INLINE)
d.comment(0xA703, 'Count down', align=Align.INLINE)
d.comment(0xA704, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xA706, 'Return', align=Align.INLINE)
d.comment(0xA660, 'NFS active?', align=Align.INLINE)
d.comment(0xA663, 'Yes: read station data', align=Align.INLINE)
d.comment(0xA665, 'No: return zero', align=Align.INLINE)
d.comment(0xA668, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA66A, 'Load station byte', align=Align.INLINE)
d.comment(0xA66D, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA66F, 'Previous byte', align=Align.INLINE)
d.comment(0xA670, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA672, 'Return', align=Align.INLINE)
d.comment(0xA673, 'NFS active?', align=Align.INLINE)
d.comment(0xA676, 'No: return zero', align=Align.INLINE)
d.comment(0xA678, 'Y=0 for process_all_fcbs', align=Align.INLINE)
d.comment(0xA67A, 'Close all open FCBs', align=Align.INLINE)
d.comment(0xA67D, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA67F, 'Load new station byte from PB', align=Align.INLINE)
d.comment(0xA681, 'Store to l0dff', align=Align.INLINE)
d.comment(0xA684, 'Previous byte', align=Align.INLINE)
d.comment(0xA685, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA687, 'Clear handles if station matches', align=Align.INLINE)
d.comment(0xA68A, 'X=&0F: scan 16 FCB entries', align=Align.INLINE)
d.comment(0xA68C, 'Load FCB flags', align=Align.INLINE)
d.comment(0xA68F, 'Save flags in Y', align=Align.INLINE)
d.comment(0xA690, 'Test bit 1 (FCB allocated?)', align=Align.INLINE)
d.comment(0xA692, 'No: skip to next entry', align=Align.INLINE)
d.comment(0xA694, 'Restore flags', align=Align.INLINE)
d.comment(0xA695, 'Clear bit 5 (pending update)', align=Align.INLINE)
d.comment(0xA697, 'Store updated flags', align=Align.INLINE)
d.comment(0xA69A, 'Save in Y', align=Align.INLINE)
d.comment(0xA69B, 'Does FCB match new station?', align=Align.INLINE)
d.comment(0xA69E, 'No match: skip to next', align=Align.INLINE)
d.comment(0xA6A0, 'Clear carry for ADC', align=Align.INLINE)
d.comment(0xA6A1, 'Restore flags', align=Align.INLINE)
d.comment(0xA6A2, 'Test bit 2 (handle 1 active?)', align=Align.INLINE)
d.comment(0xA6A4, 'No: check handle 2', align=Align.INLINE)
d.comment(0xA6A6, 'Restore flags', align=Align.INLINE)
d.comment(0xA6A7, 'Set bit 5 (handle reassigned)', align=Align.INLINE)
d.comment(0xA6A9, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6AA, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6AD, 'Store as handle 1 station', align=Align.INLINE)
d.comment(0xA6B0, 'FCB index', align=Align.INLINE)
d.comment(0xA6B1, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6B3, 'Store as handle 1 FCB index', align=Align.INLINE)
d.comment(0xA6B6, 'Restore flags', align=Align.INLINE)
d.comment(0xA6B7, 'Test bit 3 (handle 2 active?)', align=Align.INLINE)
d.comment(0xA6B9, 'No: check handle 3', align=Align.INLINE)
d.comment(0xA6BB, 'Restore flags', align=Align.INLINE)
d.comment(0xA6BC, 'Set bit 5', align=Align.INLINE)
d.comment(0xA6BE, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6BF, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6C2, 'Store as handle 2 station', align=Align.INLINE)
d.comment(0xA6C5, 'FCB index', align=Align.INLINE)
d.comment(0xA6C6, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6C8, 'Store as handle 2 FCB index', align=Align.INLINE)
d.comment(0xA6CB, 'Restore flags', align=Align.INLINE)
d.comment(0xA6CC, 'Test bit 4 (handle 3 active?)', align=Align.INLINE)
d.comment(0xA6CE, 'No: store final flags', align=Align.INLINE)
d.comment(0xA6D0, 'Restore flags', align=Align.INLINE)
d.comment(0xA6D1, 'Set bit 5', align=Align.INLINE)
d.comment(0xA6D3, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6D4, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6D7, 'Store as handle 3 station', align=Align.INLINE)
d.comment(0xA6DA, 'FCB index', align=Align.INLINE)
d.comment(0xA6DB, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6DD, 'Store as handle 3 FCB index', align=Align.INLINE)
d.comment(0xA6E0, 'Store final flags for this FCB', align=Align.INLINE)
d.comment(0xA6E1, 'Update l1060[X]', align=Align.INLINE)
d.comment(0xA6E4, 'Next FCB entry', align=Align.INLINE)
d.comment(0xA6E5, 'Loop for all 16 entries', align=Align.INLINE)
d.comment(0xA6E7, 'Return', align=Align.INLINE)
d.comment(0xA6E8, 'C=0: workspace-to-PB direction', align=Align.INLINE)
d.comment(0xA6E9, 'Skip SEC', align=Align.INLINE)
d.comment(0xA6EB, 'C=1: PB-to-workspace direction', align=Align.INLINE)
d.comment(0xA6EC, 'Workspace offset &17', align=Align.INLINE)
d.comment(0xA6EE, 'Set ws_ptr_lo', align=Align.INLINE)
d.comment(0xA6F0, 'Page from RX pointer high byte', align=Align.INLINE)
d.comment(0xA6F2, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xA6F4, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xA6F6, 'X=5: copy 5 bytes', align=Align.INLINE)
d.comment(0xA707, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0xA709, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xA70B, 'Y=1', align=Align.INLINE)
d.comment(0xA70C, 'A=1', align=Align.INLINE)
d.comment(0xA70D, 'Set ws_ptr_lo = 1', align=Align.INLINE)
d.comment(0xA70F, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0xA710, 'C=0: workspace-to-PB direction', align=Align.INLINE)
d.comment(0xA711, 'Copy via copy_pb_byte_to_ws', align=Align.INLINE)
d.comment(0xA713, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xA714, 'Load PB[1]', align=Align.INLINE)
d.comment(0xA716, 'Y=2', align=Align.INLINE)
d.comment(0xA717, 'Store to (nfs_workspace)+2', align=Align.INLINE)
d.comment(0xA719, 'Load PB[2]', align=Align.INLINE)
d.comment(0xA71B, 'Y=3', align=Align.INLINE)
d.comment(0xA71C, 'Store to (nfs_workspace)+3', align=Align.INLINE)
d.comment(0xA71E, 'Reinitialise bridge routing', align=Align.INLINE)
d.comment(0xA721, 'Compare result with workspace', align=Align.INLINE)
d.comment(0xA723, 'Different: leave unchanged', align=Align.INLINE)
d.comment(0xA725, 'Same: clear workspace byte', align=Align.INLINE)
d.comment(0xA727, 'Return', align=Align.INLINE)
d.comment(0xA728, 'Load protection mask', align=Align.INLINE)
d.comment(0xA72B, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA72E, 'Y=1: PB data offset', align=Align.INLINE)
d.comment(0xA72F, 'Load new mask from PB[1]', align=Align.INLINE)
d.comment(0xA731, 'Store via store_prot_mask', align=Align.INLINE)
d.comment(0xA734, 'NFS active?', align=Align.INLINE)
d.comment(0xA737, 'No: return zero', align=Align.INLINE)
d.comment(0xA739, 'Y=3: copy 3 bytes', align=Align.INLINE)
d.comment(0xA73B, 'Load handle byte', align=Align.INLINE)
d.comment(0xA73E, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA740, 'Previous byte', align=Align.INLINE)
d.comment(0xA741, 'Loop for bytes 3..1', align=Align.INLINE)
d.comment(0xA743, 'Return', align=Align.INLINE)
d.comment(0xA749, 'A=0', align=Align.INLINE)
d.comment(0xA74C, 'Store 0 to PB[0]', align=Align.INLINE)
d.comment(0xA74E, 'Return', align=Align.INLINE)
d.comment(0xA744, 'NFS active?', align=Align.INLINE)
d.comment(0xA747, 'Yes: process handles', align=Align.INLINE)
d.comment(0xA74F, 'Y=1: first handle in PB', align=Align.INLINE)
d.comment(0xA751, 'Load handle value from PB[Y]', align=Align.INLINE)
d.comment(0xA753, 'Must be >= &20', align=Align.INLINE)
d.comment(0xA755, 'Below range: invalid', align=Align.INLINE)
d.comment(0xA757, 'Must be < &30', align=Align.INLINE)
d.comment(0xA759, 'Above range: invalid', align=Align.INLINE)
d.comment(0xA75B, 'X = handle value', align=Align.INLINE)
d.comment(0xA75C, 'Load l1010[handle]', align=Align.INLINE)
d.comment(0xA75F, 'Non-zero: FCB exists', align=Align.INLINE)
d.comment(0xA761, 'Invalid: store 0 to PB[0]', align=Align.INLINE)
d.comment(0xA764, 'Clear PB[0] status', align=Align.INLINE)
d.comment(0xA766, 'Skip to next handle', align=Align.INLINE)
d.comment(0xA768, 'Load l1040[handle] flags', align=Align.INLINE)
d.comment(0xA76B, 'Test bit 1 (allocated?)', align=Align.INLINE)
d.comment(0xA76D, 'Not allocated: invalid', align=Align.INLINE)
d.comment(0xA76F, 'X = handle value', align=Align.INLINE)
d.comment(0xA770, 'Store handle to l1071+Y', align=Align.INLINE)
d.comment(0xA773, 'Load station from l1010', align=Align.INLINE)
d.comment(0xA776, 'Store station to l0e01+Y', align=Align.INLINE)
d.comment(0xA779, 'Is this handle 1 (Y=1)?', align=Align.INLINE)
d.comment(0xA77B, 'No: check handle 2', align=Align.INLINE)
d.comment(0xA77D, 'Save Y', align=Align.INLINE)
d.comment(0xA77E, 'Push Y', align=Align.INLINE)
d.comment(0xA77F, 'Bit mask &04 for handle 1', align=Align.INLINE)
d.comment(0xA781, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA784, 'Restore Y', align=Align.INLINE)
d.comment(0xA785, 'Back to Y', align=Align.INLINE)
d.comment(0xA786, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA789, 'Set bits 2+5 (active+updated)', align=Align.INLINE)
d.comment(0xA78B, 'Store updated flags', align=Align.INLINE)
d.comment(0xA78E, 'Next handle slot', align=Align.INLINE)
d.comment(0xA78F, 'Done all 3 handles?', align=Align.INLINE)
d.comment(0xA791, 'No: process next handle', align=Align.INLINE)
d.comment(0xA793, 'Y=3 for return', align=Align.INLINE)
d.comment(0xA794, 'Return', align=Align.INLINE)
d.comment(0xA795, 'Is this handle 2 (Y=2)?', align=Align.INLINE)
d.comment(0xA797, 'No: must be handle 3', align=Align.INLINE)
d.comment(0xA799, 'Save Y', align=Align.INLINE)
d.comment(0xA79A, 'Push Y', align=Align.INLINE)
d.comment(0xA79B, 'Bit mask &08 for handle 2', align=Align.INLINE)
d.comment(0xA79D, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA7A0, 'Restore Y', align=Align.INLINE)
d.comment(0xA7A1, 'Back to Y', align=Align.INLINE)
d.comment(0xA7A2, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA7A5, 'Set bits 3+5 (active+updated)', align=Align.INLINE)
d.comment(0xA7A7, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7AA, 'Next handle slot', align=Align.INLINE)
d.comment(0xA7AC, 'Handle 3: save Y', align=Align.INLINE)
d.comment(0xA7AD, 'Push Y', align=Align.INLINE)
d.comment(0xA7AE, 'Bit mask &10 for handle 3', align=Align.INLINE)
d.comment(0xA7B0, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA7B3, 'Restore Y', align=Align.INLINE)
d.comment(0xA7B4, 'Back to Y', align=Align.INLINE)
d.comment(0xA7B5, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA7B8, 'Set bits 4+5 (active+updated)', align=Align.INLINE)
d.comment(0xA7BA, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7BD, 'Next handle slot', align=Align.INLINE)
d.comment(0xA7BF, 'Save X (current FCB index)', align=Align.INLINE)
d.comment(0xA7C0, 'Push X', align=Align.INLINE)
d.comment(0xA7C1, 'X=&0F: scan 16 FCB entries', align=Align.INLINE)
d.comment(0xA7C3, 'Load FCB flags', align=Align.INLINE)
d.comment(0xA7C6, 'Shift bits 6-7 into bits 7-0', align=Align.INLINE)
d.comment(0xA7C7, 'Bit 6 now in bit 7 (N flag)', align=Align.INLINE)
d.comment(0xA7C8, 'Bit 6 clear: skip entry', align=Align.INLINE)
d.comment(0xA7CA, 'Restore Y (bit mask)', align=Align.INLINE)
d.comment(0xA7CB, 'Test mask bits against flags', align=Align.INLINE)
d.comment(0xA7CE, 'Zero: no matching bits', align=Align.INLINE)
d.comment(0xA7D0, 'Matching: restore Y', align=Align.INLINE)
d.comment(0xA7D1, 'Set bit 5 (updated)', align=Align.INLINE)
d.comment(0xA7D3, 'Skip clear path', align=Align.INLINE)
d.comment(0xA7D5, 'No match: restore Y', align=Align.INLINE)
d.comment(0xA7D6, 'Invert all bits', align=Align.INLINE)
d.comment(0xA7D8, 'Clear tested bits in flags', align=Align.INLINE)
d.comment(0xA7DB, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7DE, 'Next FCB entry', align=Align.INLINE)
d.comment(0xA7DF, 'Loop for all 16 entries', align=Align.INLINE)
d.comment(0xA7E1, 'Restore original X', align=Align.INLINE)
d.comment(0xA7E2, 'Back to X', align=Align.INLINE)
d.comment(0xA7E3, 'Return', align=Align.INLINE)
d.comment(0xA7E4, 'Y=1: RX control block offset', align=Align.INLINE)
d.comment(0xA7E6, 'Load (net_rx_ptr)+1', align=Align.INLINE)
d.comment(0xA7E8, 'Y=0', align=Align.INLINE)
d.comment(0xA7EA, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA7ED, 'Y=&7F: port byte offset', align=Align.INLINE)
d.comment(0xA7EF, 'Load (net_rx_ptr)+&7F', align=Align.INLINE)
d.comment(0xA7F1, 'Y=1', align=Align.INLINE)
d.comment(0xA7F3, 'Store to PB[1]', align=Align.INLINE)
d.comment(0xA7F6, 'A=&80', align=Align.INLINE)
d.comment(0xA7F8, 'Store &80 to PB[2]', align=Align.INLINE)
d.comment(0xA7FA, 'Return', align=Align.INLINE)
d.comment(0xA7FB, 'Load error flag', align=Align.INLINE)
d.comment(0xA7FE, 'Y=1: parameter block offset 1', align=Align.INLINE)
d.comment(0xA7FF, 'Store result to PB[1]', align=Align.INLINE)
d.comment(0xA801, 'Return', align=Align.INLINE)
d.comment(0xA802, 'Load context byte', align=Align.INLINE)
d.comment(0xA805, 'Bit 7 clear: store context to PB', align=Align.INLINE)
d.comment(0xA807, 'Total buffers = &6F', align=Align.INLINE)
d.comment(0xA809, 'Subtract used count', align=Align.INLINE)
d.comment(0xA80A, 'Free = &6F - l0d6b', align=Align.INLINE)
d.comment(0xA80D, 'Non-negative: store free count to PB', align=Align.INLINE)
d.comment(0xA810, 'Return', align=Align.INLINE)
d.comment(0xA80F, 'Next byte offset', align=Align.INLINE)
d.comment(0xA810, 'Load l0d6d[Y]', align=Align.INLINE)
d.comment(0xA813, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA815, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xA817, 'No: loop', align=Align.INLINE)
d.comment(0xA819, 'Return', align=Align.INLINE)
d.comment(0xA81A, 'Next byte offset', align=Align.INLINE)
d.comment(0xA81B, 'Load PB[Y]', align=Align.INLINE)
d.comment(0xA81D, 'Store to l0d6d[Y]', align=Align.INLINE)
d.comment(0xA820, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xA822, 'No: loop', align=Align.INLINE)
d.comment(0xA824, 'Return', align=Align.INLINE)
d.comment(0xA825, 'Poll for bridge', align=Align.INLINE)
d.comment(0xA828, 'Y=0', align=Align.INLINE)
d.comment(0xA82A, 'Load bridge status', align=Align.INLINE)
d.comment(0xA82D, 'Is it &FF (no bridge)?', align=Align.INLINE)
d.comment(0xA82F, 'No: bridge found', align=Align.INLINE)
d.comment(0xA832, 'PB[0] = 0 (no bridge)', align=Align.INLINE)
d.comment(0xA837, 'Y=1', align=Align.INLINE)
d.comment(0xA838, 'PB[1] = bridge status', align=Align.INLINE)
d.comment(0xA83A, 'Y=2', align=Align.INLINE)
d.comment(0xA83B, 'Y=3', align=Align.INLINE)
d.comment(0xA83C, 'Load PB[3] (caller value)', align=Align.INLINE)
d.comment(0xA83E, 'Zero: use default station', align=Align.INLINE)
d.comment(0xA840, 'Compare with bridge status', align=Align.INLINE)
d.comment(0xA843, 'Different: return unchanged', align=Align.INLINE)
d.comment(0xA845, 'Same: confirm station', align=Align.INLINE)
d.comment(0xA847, 'Load default from l0e01', align=Align.INLINE)
d.comment(0xA84A, 'Store to PB[3]', align=Align.INLINE)
d.comment(0xA84C, 'Return', align=Align.INLINE)
d.comment(0xA84D, """Bridge discovery init data (24 bytes)

Two 12-byte templates copied simultaneously by
loop_copy_bridge_init. X counts down &0B to 0,
copying the TXCB template into &C0. Y counts up
&18 to &23, copying the RXCB data into workspace
via bridge_ws_init_data (compare_bridge_status+1)
+ Y to reach the RXCB data area.

The TX broadcasts "BRIDGE" as immediate data on
port &9C to all stations (FF.FF). The RX listens
on the same port for a reply into the bridge
status bytes at &0D72.""")
d.comment(0xA84D, 'TX 0: ctrl = &82 (immediate mode)', align=Align.INLINE)
d.comment(0xA84E, 'TX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xA84F, 'TX 2: dest station = &FF (broadcast)', align=Align.INLINE)
d.comment(0xA850, 'TX 3: dest network = &FF (all nets)', align=Align.INLINE)
d.comment(0xA851, 'TX 4-9: immediate data payload', align=Align.INLINE)
d.comment(0xA857, 'TX 10: &9C (port echo)', align=Align.INLINE)
d.comment(0xA858, 'TX 11: &00 (terminator)', align=Align.INLINE)
d.comment(0xA859, 'RX 0: ctrl = &7F (receive)', align=Align.INLINE)
d.comment(0xA85A, 'RX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xA85B, 'RX 2: station = &00 (any)', align=Align.INLINE)
d.comment(0xA85C, 'RX 3: network = &00 (any)', align=Align.INLINE)
d.comment(0xA85E, 'RX 5: buf start hi (&0D) -> &0D72', align=Align.INLINE)
d.comment(0xA85F, 'RX 6: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA860, 'RX 7: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA862, 'RX 9: buf end hi (&0D) -> &0D74', align=Align.INLINE)
d.comment(0xA863, 'RX 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA864, 'RX 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA865, 'Check bridge status', align=Align.INLINE)
d.comment(0xA868, 'Is it &FF (uninitialised)?', align=Align.INLINE)
d.comment(0xA86A, 'No: bridge already active, return', align=Align.INLINE)
d.comment(0xA86C, 'Save Y', align=Align.INLINE)
d.comment(0xA86D, 'Preserve Y on stack', align=Align.INLINE)
d.comment(0xA86E, 'Y=&18: workspace offset for init', align=Align.INLINE)
d.comment(0xA870, 'X=&0B: 12 bytes to copy', align=Align.INLINE)
d.comment(0xA872, 'Rotate l0d61 right (save flag)', align=Align.INLINE)
d.comment(0xA875, 'Load init data byte', align=Align.INLINE)
d.comment(0xA878, 'Store to workspace', align=Align.INLINE)
d.comment(0xA87A, 'Load TXCB template byte', align=Align.INLINE)
d.comment(0xA87D, 'Store to TX control block', align=Align.INLINE)
d.comment(0xA87F, 'Next workspace byte', align=Align.INLINE)
d.comment(0xA880, 'Next template byte', align=Align.INLINE)
d.comment(0xA881, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0xA883, 'Store X (-1) as bridge counter', align=Align.INLINE)
d.comment(0xA886, 'Restore l0d61 flag', align=Align.INLINE)
d.comment(0xA889, 'Shift ws_0d60 left (check status)', align=Align.INLINE)
d.comment(0xA88C, 'C=0: status clear, retry', align=Align.INLINE)
d.comment(0xA88E, 'Control byte &82 for TX', align=Align.INLINE)
d.comment(0xA890, 'Set in TX control block', align=Align.INLINE)
d.comment(0xA892, 'Data block at &00C0', align=Align.INLINE)
d.comment(0xA894, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xA896, 'High byte = 0 (page 0)', align=Align.INLINE)
d.comment(0xA898, 'Set NMI TX block high', align=Align.INLINE)
d.comment(0xA89A, 'Begin Econet transmission', align=Align.INLINE)
d.comment(0xA89D, 'Test TX control block bit 7', align=Align.INLINE)
d.comment(0xA89F, 'Negative: TX still in progress', align=Align.INLINE)
d.comment(0xA8A1, 'Transfer TX completion status to A', align=Align.INLINE)
d.comment(0xA8A2, 'Save TX status', align=Align.INLINE)
d.comment(0xA8A3, 'OSBYTE &13: wait for VSYNC', align=Align.INLINE)
d.comment(0xA8A5, 'Wait for vertical sync', align=Align.INLINE)
d.comment(0xA8A8, 'Restore TX status', align=Align.INLINE)
d.comment(0xA8A9, 'Back to X', align=Align.INLINE)
d.comment(0xA8AA, 'Y=&18: check workspace response', align=Align.INLINE)
d.comment(0xA8AC, 'Load bridge response', align=Align.INLINE)
d.comment(0xA8AE, 'Negative: bridge responded', align=Align.INLINE)
d.comment(0xA8B0, 'Advance retry counter by 8', align=Align.INLINE)
d.comment(0xA8B3, 'Positive: retry poll loop', align=Align.INLINE)
d.comment(0xA8B5, 'Set response to &3F (OK)', align=Align.INLINE)
d.comment(0xA8B7, 'Store to workspace', align=Align.INLINE)
d.comment(0xA8B9, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA8BA, 'Back to Y', align=Align.INLINE)
d.comment(0xA8BB, 'Load bridge status', align=Align.INLINE)
d.comment(0xA8BE, 'X = bridge status', align=Align.INLINE)
d.comment(0xA8BF, 'Complement status', align=Align.INLINE)
d.comment(0xA8C1, 'Status was &FF: return (no bridge)', align=Align.INLINE)
d.comment(0xA8C3, 'Return bridge station in A', align=Align.INLINE)
d.comment(0xA8C4, 'Return', align=Align.INLINE)
d.comment(0xA8C5, 'Compare sub-code with 1', align=Align.INLINE)
d.comment(0xA8C7, 'Sub-code >= 1: handle TX request', align=Align.INLINE)
d.comment(0xA8C9, 'Test station active flag', align=Align.INLINE)
d.comment(0xA8CC, 'Not active: return', align=Align.INLINE)
d.comment(0xA8CE, 'Y=&23: workspace offset for params', align=Align.INLINE)
d.comment(0xA8D0, 'Set owner access mask', align=Align.INLINE)
d.comment(0xA8D3, 'Load TXCB init byte', align=Align.INLINE)
d.comment(0xA8D6, 'Non-zero: use template value', align=Align.INLINE)
d.comment(0xA8D8, 'Zero: use workspace default value', align=Align.INLINE)
d.comment(0xA8DB, 'Store to workspace', align=Align.INLINE)
d.comment(0xA8DD, 'Next byte down', align=Align.INLINE)
d.comment(0xA8DE, 'Until Y reaches &17', align=Align.INLINE)
d.comment(0xA8E0, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xA8E2, 'Y=&18 (INY from &17)', align=Align.INLINE)
d.comment(0xA8E3, 'Set net_tx_ptr low byte', align=Align.INLINE)
d.comment(0xA8E5, 'Y=&1C: workspace offset for PB pointer', align=Align.INLINE)
d.comment(0xA8F6, 'Store PB pointer to workspace', align=Align.INLINE)
d.comment(0xA8E7, 'Load PB page number', align=Align.INLINE)
d.comment(0xA8F9, 'Y=2: parameter offset', align=Align.INLINE)
d.comment(0xA8E9, 'PB starts at next page boundary (+1)', align=Align.INLINE)
d.comment(0xA8FB, 'Control byte &90', align=Align.INLINE)
d.comment(0xA8EB, 'Store PB start pointer at ws[&1C]', align=Align.INLINE)
d.comment(0xA8FD, 'Set escapable flag', align=Align.INLINE)
d.comment(0xA8EE, 'Y=1: PB byte 1 (transfer length)', align=Align.INLINE)
d.comment(0xA8FF, 'Store control byte to PB', align=Align.INLINE)
d.comment(0xA8F0, 'Load transfer length from PB', align=Align.INLINE)
d.comment(0xA903, 'Load workspace data', align=Align.INLINE)
d.comment(0xA8F2, 'Y=&20: workspace offset for buffer end', align=Align.INLINE)
d.comment(0xA906, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA8F4, 'Add PB base for buffer end address', align=Align.INLINE)
d.comment(0xA908, 'Next byte', align=Align.INLINE)
d.comment(0xA909, 'Until Y reaches 7', align=Align.INLINE)
d.comment(0xA90B, 'Loop for 3 bytes (Y=4,5,6)', align=Align.INLINE)
d.comment(0xA90D, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0xA90F, 'Store to net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xA911, 'Enable interrupts', align=Align.INLINE)
d.comment(0xA911, 'Send the network packet', align=Align.INLINE)
d.comment(0xA914, 'Y=&20: workspace offset', align=Align.INLINE)
d.comment(0xA916, 'Set to &FF (pending)', align=Align.INLINE)
d.comment(0xA918, 'Mark send pending in workspace', align=Align.INLINE)
d.comment(0xA91B, 'Also mark offset &21', align=Align.INLINE)
d.comment(0xA91D, 'Y=&19: control offset', align=Align.INLINE)
d.comment(0xA91F, 'Control byte &90', align=Align.INLINE)
d.comment(0xA921, 'Store to workspace', align=Align.INLINE)
d.comment(0xA923, 'Y=&18: RX control offset', align=Align.INLINE)
d.comment(0xA924, 'Control byte &7F', align=Align.INLINE)
d.comment(0xA926, 'Store RX control', align=Align.INLINE)
d.comment(0xA928, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xA92B, 'Store address low byte at ws[Y]', align=Align.INLINE)
d.comment(0xA92D, 'Advance to high byte offset', align=Align.INLINE)
d.comment(0xA92E, 'Load high byte base (table_idx)', align=Align.INLINE)
d.comment(0xA935, 'Save processor flags', align=Align.INLINE)
d.comment(0xA930, 'Add carry for page crossing', align=Align.INLINE)
d.comment(0xA936, 'Y=1: PB offset for station', align=Align.INLINE)
d.comment(0xA932, 'Store address high byte at ws[Y+1]', align=Align.INLINE)
d.comment(0xA938, 'Load station number from PB', align=Align.INLINE)
d.comment(0xA934, 'Return', align=Align.INLINE)
d.comment(0xA93A, 'X = station number', align=Align.INLINE)
d.comment(0xA93C, 'Load network number from PB', align=Align.INLINE)
d.comment(0xA93E, 'Y=3: workspace start offset', align=Align.INLINE)
d.comment(0xA93F, 'Store Y as ws_ptr_lo', align=Align.INLINE)
d.comment(0xA941, 'Y=&72: workspace offset for dest', align=Align.INLINE)
d.comment(0xA943, 'Store network to workspace', align=Align.INLINE)
d.comment(0xA945, 'Y=&71', align=Align.INLINE)
d.comment(0xA946, 'A = station (from X)', align=Align.INLINE)
d.comment(0xA947, 'Store station to workspace', align=Align.INLINE)
d.comment(0xA949, 'Restore flags from PHP', align=Align.INLINE)
d.comment(0xA94A, 'Non-zero sub-code: handle burst', align=Align.INLINE)
d.comment(0xA94C, 'Load current offset', align=Align.INLINE)
d.comment(0xA94E, 'Advance offset for next byte', align=Align.INLINE)
d.comment(0xA950, 'Load next char from PB', align=Align.INLINE)
d.comment(0xA952, 'Zero: end of data, return', align=Align.INLINE)
d.comment(0xA954, 'Y=&7D: workspace char offset', align=Align.INLINE)
d.comment(0xA956, 'Store char to RX buffer', align=Align.INLINE)
d.comment(0xA958, 'Save char for later test', align=Align.INLINE)
d.comment(0xA959, 'Init workspace copy for wide xfer', align=Align.INLINE)
d.comment(0xA95C, 'Set carry for flag set', align=Align.INLINE)
d.comment(0xA95F, 'Enable IRQ and send packet', align=Align.INLINE)
d.comment(0xA95D, 'Set bit 7: Tube needs release', align=Align.INLINE)
d.comment(0xA962, 'Delay countdown', align=Align.INLINE)
d.comment(0xA963, 'Loop for short delay', align=Align.INLINE)
d.comment(0xA965, 'Restore char', align=Align.INLINE)
d.comment(0xA966, 'Test if char was CR (&0D)', align=Align.INLINE)
d.comment(0xA968, 'Not CR: send next char', align=Align.INLINE)
d.comment(0xA96A, 'CR sent: return', align=Align.INLINE)
d.comment(0xA96B, 'Init workspace for wide copy', align=Align.INLINE)
d.comment(0xA96E, 'Y=&7B: workspace offset', align=Align.INLINE)
d.comment(0xA970, 'Load buffer size', align=Align.INLINE)
d.comment(0xA972, 'Add 3 for header', align=Align.INLINE)
d.comment(0xA974, 'Store adjusted size', align=Align.INLINE)
d.comment(0xA976, 'Enable interrupts', align=Align.INLINE)
d.comment(0xA977, 'Send packet and return', align=Align.INLINE)
d.comment(0xA97A, 'Save processor flags', align=Align.INLINE)
d.comment(0xA97B, 'Save A', align=Align.INLINE)
d.comment(0xA97C, 'Save X', align=Align.INLINE)
d.comment(0xA97D, 'Push X', align=Align.INLINE)
d.comment(0xA97E, 'Save Y', align=Align.INLINE)
d.comment(0xA97F, 'Push Y', align=Align.INLINE)
d.comment(0xA980, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA981, 'Read OSWORD number from stack', align=Align.INLINE)
d.comment(0xA984, 'OSWORD >= 9?', align=Align.INLINE)
d.comment(0xA986, 'Yes: out of range, restore + return', align=Align.INLINE)
d.comment(0xA988, 'X = OSWORD number', align=Align.INLINE)
d.comment(0xA989, 'Push handler address for dispatch', align=Align.INLINE)
d.comment(0xA98C, 'Restore Y', align=Align.INLINE)
d.comment(0xA98D, 'Back to Y', align=Align.INLINE)
d.comment(0xA98E, 'Restore X', align=Align.INLINE)
d.comment(0xA98F, 'Back to X', align=Align.INLINE)
d.comment(0xA990, 'Restore A', align=Align.INLINE)
d.comment(0xA991, 'Restore processor flags', align=Align.INLINE)
d.comment(0xA992, 'RTS dispatches via pushed address', align=Align.INLINE)
d.comment(0xA993, 'Load handler high byte from table', align=Align.INLINE)
d.comment(0xA996, 'Push for RTS dispatch', align=Align.INLINE)
d.comment(0xA997, 'Load handler low byte from table', align=Align.INLINE)
d.comment(0xA99A, 'Push for RTS dispatch', align=Align.INLINE)
d.comment(0xA99B, 'Reload OSWORD number for handler', align=Align.INLINE)
d.comment(0xA99D, 'RTS will dispatch to handler', align=Align.INLINE)
d.comment(0xA9BE, 'Y=&D9: workspace abort offset', align=Align.INLINE)
d.comment(0xA9C0, 'Store abort code to workspace', align=Align.INLINE)
d.comment(0xA9C2, 'Control byte &80 (abort)', align=Align.INLINE)
d.comment(0xA9C4, 'Y=&0C: control offset', align=Align.INLINE)
d.comment(0xA9C6, 'Store control byte', align=Align.INLINE)
d.comment(0xA9C8, 'Save current TX ptr low', align=Align.INLINE)
d.comment(0xA9CA, 'Push on stack', align=Align.INLINE)
d.comment(0xA9CB, 'Save current TX ptr high', align=Align.INLINE)
d.comment(0xA9CD, 'Push on stack', align=Align.INLINE)
d.comment(0xA9CE, 'Set TX ptr to workspace offset', align=Align.INLINE)
d.comment(0xA9D0, 'Load workspace high byte', align=Align.INLINE)
d.comment(0xA9D2, 'Set TX ptr high', align=Align.INLINE)
d.comment(0xA9D4, 'Send the abort packet', align=Align.INLINE)
d.comment(0xA9D7, 'Set status to &3F (complete)', align=Align.INLINE)
d.comment(0xA9D9, 'Store at TX ptr offset 0', align=Align.INLINE)
d.comment(0xA9DB, 'Restore TX ptr high', align=Align.INLINE)
d.comment(0xA9DC, 'Back to net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xA9DE, 'Restore TX ptr low', align=Align.INLINE)
d.comment(0xA9DF, 'Back to net_tx_ptr', align=Align.INLINE)
d.comment(0xA9E1, 'Return', align=Align.INLINE)
d.comment(0xA9E2, 'Load PB pointer high', align=Align.INLINE)
d.comment(0xA9E4, 'Compare with &81 (special case)', align=Align.INLINE)
d.comment(0xA9E6, 'Match: skip to processing', align=Align.INLINE)
d.comment(0xA9E8, 'Y=1: first claim code position', align=Align.INLINE)
d.comment(0xA9EA, 'X=&0A: 11 codes to check', align=Align.INLINE)
d.comment(0xA9EC, 'Search claim code table', align=Align.INLINE)
d.comment(0xA9EF, 'Found: skip to processing', align=Align.INLINE)
d.comment(0xA9F1, 'Try second table range', align=Align.INLINE)
d.comment(0xA9F2, 'Y=-1: flag second range', align=Align.INLINE)
d.comment(0xA9F3, 'X=&11: 18 codes to check', align=Align.INLINE)
d.comment(0xA9F5, 'Search claim code table', align=Align.INLINE)
d.comment(0xA9F8, 'Found: skip to processing', align=Align.INLINE)
d.comment(0xA9FA, 'Not found: increment Y', align=Align.INLINE)
d.comment(0xA9FB, 'X=2: default state', align=Align.INLINE)
d.comment(0xA9FD, 'A = Y (search result)', align=Align.INLINE)
d.comment(0xA9FE, 'Zero: not found, return', align=Align.INLINE)
d.comment(0xAA00, 'Save result flags', align=Align.INLINE)
d.comment(0xAA01, 'Positive: use state X=2', align=Align.INLINE)
d.comment(0xAA04, 'Y=&DC: workspace offset for save', align=Align.INLINE)
d.comment(0xAA06, 'Load tube claim ID byte', align=Align.INLINE)
d.comment(0xAA09, 'Store to workspace', align=Align.INLINE)
d.comment(0xAA0B, 'Next byte down', align=Align.INLINE)
d.comment(0xAA0C, 'Until Y reaches &DA', align=Align.INLINE)
d.comment(0xAA0E, 'Loop for 3 bytes', align=Align.INLINE)
d.comment(0xAA10, 'A = state (2 or 3)', align=Align.INLINE)
d.comment(0xAA11, 'Send abort with state code', align=Align.INLINE)
d.comment(0xAA14, 'Restore flags', align=Align.INLINE)
d.comment(0xAA15, 'Positive: return without poll', align=Align.INLINE)
d.comment(0xAA17, 'Set control to &7F', align=Align.INLINE)
d.comment(0xAA19, 'Y=&0C: control offset', align=Align.INLINE)
d.comment(0xAA1B, 'Store control byte', align=Align.INLINE)
d.comment(0xAA1D, 'Load status from workspace', align=Align.INLINE)
d.comment(0xAA1F, 'Positive: keep waiting', align=Align.INLINE)
d.comment(0xAA21, 'Get stack pointer', align=Align.INLINE)
d.comment(0xAA22, 'Y=&DD: workspace result offset', align=Align.INLINE)
d.comment(0xAA24, 'Load result byte', align=Align.INLINE)
d.comment(0xAA26, 'Set bit 6 and bit 2', align=Align.INLINE)
d.comment(0xAA28, 'Always branch (NZ from ORA)', align=Align.INLINE)
d.comment(0xAA2A, 'Previous workspace byte', align=Align.INLINE)
d.comment(0xAA2B, 'Previous stack position', align=Align.INLINE)
d.comment(0xAA2C, 'Load workspace byte', align=Align.INLINE)
d.comment(0xAA2E, "Store to caller's stack frame", align=Align.INLINE)
d.comment(0xAA31, 'Reached start of save area?', align=Align.INLINE)
d.comment(0xAA33, 'No: copy next byte', align=Align.INLINE)
d.comment(0xAA35, 'Return', align=Align.INLINE)
d.comment(0xAA36, 'Compare A with code at index X', align=Align.INLINE)
d.comment(0xAA39, 'Match: return with Z set', align=Align.INLINE)
d.comment(0xAA3B, 'Try next code', align=Align.INLINE)
d.comment(0xAA3C, 'More codes: continue search', align=Align.INLINE)
d.comment(0xAA3E, 'Return (Z clear = not found)', align=Align.INLINE)
d.comment(0xAA3F, """OSWORD claim code table

Table of OSWORD numbers that trigger NMI
claim processing. Searched in two passes by
the OSWORD 7 handler: first the 11-entry
range (indices 0-&0A), then the full 18-entry
range (indices 0-&11). A match in the first
range sets state 2 (standard claim); a match
only in the extended range sets state 3.""")
d.comment(0xAA3F, 'Range 1+2: OSWORD &04', align=Align.INLINE)
d.comment(0xAA40, 'Range 1+2: OSWORD &09', align=Align.INLINE)
d.comment(0xAA41, 'Range 1+2: OSWORD &0A', align=Align.INLINE)
d.comment(0xAA42, 'Range 1+2: OSWORD &14', align=Align.INLINE)
d.comment(0xAA43, 'Range 1+2: OSWORD &15', align=Align.INLINE)
d.comment(0xAA44, 'Range 1+2: OSWORD &9A', align=Align.INLINE)
d.comment(0xAA45, 'Range 1+2: OSWORD &9B', align=Align.INLINE)
d.comment(0xAA46, 'Range 1+2: OSWORD &E1', align=Align.INLINE)
d.comment(0xAA47, 'Range 1+2: OSWORD &E2', align=Align.INLINE)
d.comment(0xAA48, 'Range 1+2: OSWORD &E3', align=Align.INLINE)
d.comment(0xAA49, 'Range 1+2: OSWORD &E4', align=Align.INLINE)
d.comment(0xAA4A, 'Range 2 only: OSWORD &0B', align=Align.INLINE)
d.comment(0xAA4B, 'Range 2 only: OSWORD &0C', align=Align.INLINE)
d.comment(0xAA4C, 'Range 2 only: OSWORD &0F', align=Align.INLINE)
d.comment(0xAA4D, 'Range 2 only: OSWORD &79', align=Align.INLINE)
d.comment(0xAA4E, 'Range 2 only: OSWORD &7A', align=Align.INLINE)
d.comment(0xAA4F, 'Range 2 only: OSWORD &86', align=Align.INLINE)
d.comment(0xAA50, 'Range 2 only: OSWORD &87', align=Align.INLINE)
d.comment(0xAA51, 'Y=&0E: copy 15 bytes (0-14)', align=Align.INLINE)
d.comment(0xAA53, 'OSWORD 7?', align=Align.INLINE)
d.comment(0xAA55, 'Yes: handle', align=Align.INLINE)
d.comment(0xAA57, 'OSWORD 8?', align=Align.INLINE)
d.comment(0xAA59, 'No: return', align=Align.INLINE)
d.comment(0xAA5B, 'Workspace low = &DB', align=Align.INLINE)
d.comment(0xAA5D, 'Set nfs_workspace low byte', align=Align.INLINE)
d.comment(0xAA5F, 'Load PB[Y]', align=Align.INLINE)
d.comment(0xAA61, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0xAA63, 'Next byte down', align=Align.INLINE)
d.comment(0xAA64, 'Loop for 15 bytes', align=Align.INLINE)
d.comment(0xAA66, 'Y=0', align=Align.INLINE)
d.comment(0xAA67, 'Workspace low = &DA', align=Align.INLINE)
d.comment(0xAA69, 'Load OSWORD number', align=Align.INLINE)
d.comment(0xAA6B, 'Store at workspace+0 (= &DA)', align=Align.INLINE)
d.comment(0xAA6D, 'Workspace low = 0 (restore)', align=Align.INLINE)
d.comment(0xAA6F, 'Y=&14: control offset', align=Align.INLINE)
d.comment(0xAA71, 'Control value &E9', align=Align.INLINE)
d.comment(0xAA73, 'Store to workspace+&14', align=Align.INLINE)
d.comment(0xAA75, 'Abort code = 1', align=Align.INLINE)
d.comment(0xAA77, 'Send abort packet', align=Align.INLINE)
d.comment(0xAA7A, 'Restore nfs_workspace low', align=Align.INLINE)
d.comment(0xA9B0, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA9B1, 'Clear bit 0 of stacked P (carry)', align=Align.INLINE)
d.comment(0xA9B4, 'Shift back (clears carry flag)', align=Align.INLINE)
d.comment(0xA9B7, 'A = original Y', align=Align.INLINE)
d.comment(0xA9B8, 'Y=&DA: workspace offset', align=Align.INLINE)
d.comment(0xA9BA, 'Store Y to workspace', align=Align.INLINE)
d.comment(0xA9BC, 'Abort code = 0', align=Align.INLINE)
d.comment(0xAA7C, 'X=&0D: 14 bytes to copy', align=Align.INLINE)
d.comment(0xAA7E, 'Y=&7C: workspace destination offset', align=Align.INLINE)
d.comment(0xAA80, 'Test bit 6 via BIT (V flag check)', align=Align.INLINE)
d.comment(0xAA83, 'V=1: skip to wide mode copy', align=Align.INLINE)
d.comment(0xAA85, 'Y=&17: narrow mode dest offset', align=Align.INLINE)
d.comment(0xAA87, 'X=&1A: 27 bytes to copy', align=Align.INLINE)
d.comment(0xAA89, 'Clear V flag for narrow mode', align=Align.INLINE)
d.comment(0xAA8A, 'Load template byte', align=Align.INLINE)
d.comment(0xAA8D, 'Is it &FE? (end marker)', align=Align.INLINE)
d.comment(0xAA8F, 'Yes: finished, set TX ptr', align=Align.INLINE)
d.comment(0xAA91, 'Is it &FD? (skip marker)', align=Align.INLINE)
d.comment(0xAA93, 'Yes: skip store, just advance', align=Align.INLINE)
d.comment(0xAA95, 'Is it &FC? (page ptr marker)', align=Align.INLINE)
d.comment(0xAA97, 'No: use literal value', align=Align.INLINE)
d.comment(0xAA99, '&FC: load RX buffer page', align=Align.INLINE)
d.comment(0xAA9B, 'V=1: use net_rx_ptr_hi', align=Align.INLINE)
d.comment(0xAA9D, 'V=0: use nfs_workspace_hi', align=Align.INLINE)
d.comment(0xAA9F, 'Store as TX ptr high', align=Align.INLINE)
d.comment(0xAAA1, 'V=1: store to net_rx_ptr target', align=Align.INLINE)
d.comment(0xAAA3, 'V=0: store to nfs_workspace', align=Align.INLINE)
d.comment(0xAAA5, 'Continue to next byte', align=Align.INLINE)
d.comment(0xAAA7, 'V=1: store to net_rx_ptr', align=Align.INLINE)
d.comment(0xAAA9, 'Advance workspace offset down', align=Align.INLINE)
d.comment(0xAAAA, 'Advance template index', align=Align.INLINE)
d.comment(0xAAAB, 'More bytes: continue copy', align=Align.INLINE)
d.comment(0xAAAD, 'Adjust Y for start of TX data', align=Align.INLINE)
d.comment(0xAAAE, 'Set net_tx_ptr from Y', align=Align.INLINE)
d.comment(0xAAB0, 'Return', align=Align.INLINE)
d.comment(0xAAB1, """Workspace TXCB init template

39-byte template with three overlapping
regions, each a TXCB/RXCB structure:
  Wide  [0..13]:  ws+&6F..&7C via net_rx_ptr
  Narrow [14..26]: ws+&0C..&17 via workspace
  Spool [27..38]:  ws+&01..&0B via workspace
Markers: &FE=end, &FD=skip, &FC=page ptr.""")
d.comment(0xAAB1, 'Wide &6F: ctrl=&85', align=Align.INLINE)
d.comment(0xAAB2, 'Wide &70: port=&00', align=Align.INLINE)
d.comment(0xAAB3, 'Wide &71: skip (dest station)', align=Align.INLINE)
d.comment(0xAAB4, 'Wide &72: skip (dest network)', align=Align.INLINE)
d.comment(0xAAB5, 'Wide &73: buf start lo=&7D', align=Align.INLINE)
d.comment(0xAAB6, 'Wide &74: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAAB7, 'Wide &75: buf start ext lo', align=Align.INLINE)
d.comment(0xAAB8, 'Wide &76: buf start ext hi', align=Align.INLINE)
d.comment(0xAAB9, 'Wide &77: buf end lo=&7E', align=Align.INLINE)
d.comment(0xAABA, 'Wide &78: buf end hi=page ptr', align=Align.INLINE)
d.comment(0xAABB, 'Wide &79: buf end ext lo', align=Align.INLINE)
d.comment(0xAABC, 'Wide &7A: buf end ext hi', align=Align.INLINE)
d.comment(0xAABD, 'Wide &7B: zero', align=Align.INLINE)
d.comment(0xAABE, 'Wide &7C: zero', align=Align.INLINE)
d.comment(0xAABF, 'Narrow stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAAC0, 'Narrow &0C: ctrl=&80 (standard)', align=Align.INLINE)
d.comment(0xAAC1, 'Narrow &0D: port=&93', align=Align.INLINE)
d.comment(0xAAC2, 'Narrow &0E: skip (dest station)', align=Align.INLINE)
d.comment(0xAAC3, 'Narrow &0F: skip (dest network)', align=Align.INLINE)
d.comment(0xAAC4, 'Narrow &10: buf start lo=&D9', align=Align.INLINE)
d.comment(0xAAC5, 'Narrow &11: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAAC6, 'Narrow &12: buf start ext lo', align=Align.INLINE)
d.comment(0xAAC7, 'Narrow &13: buf start ext hi', align=Align.INLINE)
d.comment(0xAAC8, 'Narrow &14: buf end lo=&DE', align=Align.INLINE)
d.comment(0xAAC9, 'Narrow &15: buf end hi=page ptr', align=Align.INLINE)
d.comment(0xAACA, 'Narrow &16: buf end ext lo', align=Align.INLINE)
d.comment(0xAACB, 'Narrow &17: buf end ext hi', align=Align.INLINE)
d.comment(0xAACC, 'Spool stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAACD, 'Spool &01: port=&D1', align=Align.INLINE)
d.comment(0xAACF, 'Spool &03: skip (dest network)', align=Align.INLINE)
d.comment(0xAAD1, 'Spool &05: skip (buf start hi)', align=Align.INLINE)
d.comment(0xAAD2, 'Spool &06: buf start ext lo', align=Align.INLINE)
d.comment(0xAAD3, 'Spool &07: buf start ext hi', align=Align.INLINE)
d.comment(0xAAD4, 'Spool &08: skip (buf end lo)', align=Align.INLINE)
d.comment(0xAAD5, 'Spool &09: skip (buf end hi)', align=Align.INLINE)
d.comment(0xAAD6, 'Spool &0A: buf end ext lo', align=Align.INLINE)
d.comment(0xAAD7, 'Spool &0B: buf end ext hi', align=Align.INLINE)
d.comment(0xAAD8, 'X = X - 1', align=Align.INLINE)
d.comment(0xAAD9, 'Match osword_pb_ptr?', align=Align.INLINE)
d.comment(0xAADB, 'No: return (not our PB)', align=Align.INLINE)
d.comment(0xAADD, 'Load spool state byte', align=Align.INLINE)
d.comment(0xAADF, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAAE0, 'C=1: already active, return', align=Align.INLINE)
d.comment(0xAAE2, 'Buffer start at &25', align=Align.INLINE)
d.comment(0xAAE4, 'Store as buffer pointer', align=Align.INLINE)
d.comment(0xAAE7, 'Control state &41', align=Align.INLINE)
d.comment(0xAAE9, 'Store as spool control state', align=Align.INLINE)
d.comment(0xAAEC, 'Return', align=Align.INLINE)
d.comment(0xAAED, 'Check Y == 4', align=Align.INLINE)
d.comment(0xAAEF, 'No: return', align=Align.INLINE)
d.comment(0xAAF1, 'A = X (control byte)', align=Align.INLINE)
d.comment(0xAAF2, 'Decrement X', align=Align.INLINE)
d.comment(0xAAF3, 'Non-zero: handle spool ctrl byte', align=Align.INLINE)
d.comment(0xAAF5, 'Get stack pointer', align=Align.INLINE)
d.comment(0xAAF6, 'OR with stack value', align=Align.INLINE)
d.comment(0xAAF9, 'Store back to stack', align=Align.INLINE)
d.comment(0xAAFC, 'OSBYTE &91: read buffer', align=Align.INLINE)
d.comment(0xAAFE, 'X=3: printer buffer', align=Align.INLINE)
d.comment(0xAB00, 'Read character from buffer', align=Align.INLINE)
d.comment(0xAB03, 'C=1: buffer empty, return', align=Align.INLINE)
d.comment(0xAB05, 'A = extracted character', align=Align.INLINE)
d.comment(0xAB06, 'Add byte to RX buffer', align=Align.INLINE)
d.comment(0xAB09, 'Buffer past &6E limit?', align=Align.INLINE)
d.comment(0xAB0B, 'No: read more from buffer', align=Align.INLINE)
d.comment(0xAB0D, 'Buffer full: send packet', align=Align.INLINE)
d.comment(0xAB10, 'More room: continue reading', align=Align.INLINE)
d.comment(0xAB12, 'Load current buffer index', align=Align.INLINE)
d.comment(0xAB15, 'Store byte at buffer position', align=Align.INLINE)
d.comment(0xAB17, 'Advance buffer index', align=Align.INLINE)
d.comment(0xAB1A, 'Return', align=Align.INLINE)
d.comment(0xAB1B, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAB1C, 'Bit 0 clear: not active path', align=Align.INLINE)
d.comment(0xAB1E, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB21, 'Save for bit test', align=Align.INLINE)
d.comment(0xAB22, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAB23, 'Restore state', align=Align.INLINE)
d.comment(0xAB24, 'C=1: already started, reset', align=Align.INLINE)
d.comment(0xAB26, 'Set bits 0-1 (active + pending)', align=Align.INLINE)
d.comment(0xAB28, 'Store updated state', align=Align.INLINE)
d.comment(0xAB2B, 'Control byte 3 for header', align=Align.INLINE)
d.comment(0xAB2D, 'Add to RX buffer', align=Align.INLINE)
d.comment(0xAB30, 'Send current buffer', align=Align.INLINE)
d.comment(0xAB33, 'Reset spool buffer state', align=Align.INLINE)
d.comment(0xAB36, 'Y=8: workspace offset for length', align=Align.INLINE)
d.comment(0xAB38, 'Load buffer index (=length)', align=Align.INLINE)
d.comment(0xAB3B, 'Store length to workspace', align=Align.INLINE)
d.comment(0xAB3D, 'Set data page high byte', align=Align.INLINE)
d.comment(0xAB40, 'Store to workspace+9', align=Align.INLINE)
d.comment(0xAB42, 'Y=5: workspace offset', align=Align.INLINE)
d.comment(0xAB44, 'Store page to workspace+5', align=Align.INLINE)
d.comment(0xAB46, 'Y=&0B: template start offset', align=Align.INLINE)
d.comment(0xAB48, 'X=&26: template index', align=Align.INLINE)
d.comment(0xAB4A, 'Copy template to workspace', align=Align.INLINE)
d.comment(0xAB4D, 'Adjust Y down', align=Align.INLINE)
d.comment(0xAB4E, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB51, 'Save state', align=Align.INLINE)
d.comment(0xAB52, 'Rotate to get carry (bit 7)', align=Align.INLINE)
d.comment(0xAB53, 'Restore state', align=Align.INLINE)
d.comment(0xAB54, 'Toggle bit 7', align=Align.INLINE)
d.comment(0xAB56, 'Store updated state', align=Align.INLINE)
d.comment(0xAB59, 'Shift to get both flag bits', align=Align.INLINE)
d.comment(0xAB5A, 'Store flags to workspace', align=Align.INLINE)
d.comment(0xAB5C, 'Save l00d0 (exec flag)', align=Align.INLINE)
d.comment(0xAB5E, 'Push for later restore', align=Align.INLINE)
d.comment(0xAB5F, 'Clear bit 0 of exec flag', align=Align.INLINE)
d.comment(0xAB61, 'Store modified exec flag', align=Align.INLINE)
d.comment(0xAB63, 'Reset buffer start to &25', align=Align.INLINE)
d.comment(0xAB65, 'Store reset buffer index', align=Align.INLINE)
d.comment(0xAB68, 'A=0 for disconnect reply', align=Align.INLINE)
d.comment(0xAB6A, 'X=0', align=Align.INLINE)
d.comment(0xAB6B, 'Y = workspace page', align=Align.INLINE)
d.comment(0xAB6D, 'Enable interrupts', align=Align.INLINE)
d.comment(0xAB6E, 'Send disconnect reply packet', align=Align.INLINE)
d.comment(0xAB71, 'Restore exec flag', align=Align.INLINE)
d.comment(0xAB72, 'Store original exec flag', align=Align.INLINE)
d.comment(0xAB74, 'Return', align=Align.INLINE)
d.comment(0xAB75, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB78, 'Rotate bit 0 to carry', align=Align.INLINE)
d.comment(0xAB79, 'C=0: send current buffer', align=Align.INLINE)
d.comment(0xAB7B, 'Save exec flag', align=Align.INLINE)
d.comment(0xAB7D, 'Push for restore', align=Align.INLINE)
d.comment(0xAB7E, 'Clear bit 0', align=Align.INLINE)
d.comment(0xAB80, 'Store modified flag', align=Align.INLINE)
d.comment(0xAB82, 'Control byte &14 (repeat count)', align=Align.INLINE)
d.comment(0xAB84, 'Save retry count', align=Align.INLINE)
d.comment(0xAB85, 'X=&0B: 12 bytes of template', align=Align.INLINE)
d.comment(0xAB87, 'Y=&2C: workspace offset for TXCB', align=Align.INLINE)
d.comment(0xAB89, 'Load template byte', align=Align.INLINE)
d.comment(0xAB8C, 'Store to workspace', align=Align.INLINE)
d.comment(0xAB8E, 'Next byte down', align=Align.INLINE)
d.comment(0xAB8F, 'Next template byte', align=Align.INLINE)
d.comment(0xAB90, 'Loop for 12 bytes', align=Align.INLINE)
d.comment(0xAB92, 'X=-1: disable escape checking', align=Align.INLINE)
d.comment(0xAB94, 'Y=2: workspace offset for station', align=Align.INLINE)
d.comment(0xAB96, 'Load station number', align=Align.INLINE)
d.comment(0xAB98, 'Save station', align=Align.INLINE)
d.comment(0xAB9A, 'Load network number', align=Align.INLINE)
d.comment(0xAB9C, 'Y=&24: TXCB dest network offset', align=Align.INLINE)
d.comment(0xAB9E, 'Store network to TXCB', align=Align.INLINE)
d.comment(0xABA0, 'Y=&23', align=Align.INLINE)
d.comment(0xABA1, 'Restore station', align=Align.INLINE)
d.comment(0xABA2, 'Store station to TXCB', align=Align.INLINE)
d.comment(0xABA4, 'X=&0B: 12 bytes of RX template', align=Align.INLINE)
d.comment(0xABA6, 'Y=&0B: workspace RX offset', align=Align.INLINE)
d.comment(0xABA8, 'Load RX template byte', align=Align.INLINE)
d.comment(0xABAB, 'Is it &FD? (skip marker)', align=Align.INLINE)
d.comment(0xABAD, 'Yes: skip store', align=Align.INLINE)
d.comment(0xABAF, 'Is it &FC? (page ptr marker)', align=Align.INLINE)
d.comment(0xABB1, 'No: use literal value', align=Align.INLINE)
d.comment(0xABB3, '&FC: substitute RX buffer page', align=Align.INLINE)
d.comment(0xABB5, 'Store to workspace', align=Align.INLINE)
d.comment(0xABB7, 'Next byte down', align=Align.INLINE)
d.comment(0xABB8, 'Next template byte', align=Align.INLINE)
d.comment(0xABB9, 'Loop for 12 bytes', align=Align.INLINE)
d.comment(0xABBB, 'TX data start at &25', align=Align.INLINE)
d.comment(0xABBD, 'Set net_tx_ptr low', align=Align.INLINE)
d.comment(0xABBF, 'Set data page high byte', align=Align.INLINE)
d.comment(0xABC1, 'Set net_tx_ptr high', align=Align.INLINE)
d.comment(0xABC3, 'Set up password in TX buffer', align=Align.INLINE)
d.comment(0xABC6, 'Send the packet', align=Align.INLINE)
d.comment(0xABC9, 'Clear net_tx_ptr low (page base)', align=Align.INLINE)
d.comment(0xABCB, 'Store zero', align=Align.INLINE)
d.comment(0xABCD, 'Set TX high to workspace page', align=Align.INLINE)
d.comment(0xABCF, 'Store workspace high byte', align=Align.INLINE)
d.comment(0xABD1, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xABD4, 'Y=&2D: reply status offset', align=Align.INLINE)
d.comment(0xABD6, 'Load reply byte', align=Align.INLINE)
d.comment(0xABD8, 'Zero: success', align=Align.INLINE)
d.comment(0xABDA, 'Status = 3? (busy, can retry)', align=Align.INLINE)
d.comment(0xABDC, 'Other error: handle failure', align=Align.INLINE)
d.comment(0xABDE, 'Discard retry count', align=Align.INLINE)
d.comment(0xABDF, 'Discard saved exec flag', align=Align.INLINE)
d.comment(0xABE0, 'Restore l00d0', align=Align.INLINE)
d.comment(0xABE2, 'A=0: null terminator', align=Align.INLINE)
d.comment(0xABE4, 'Add zero to RX buffer (end marker)', align=Align.INLINE)
d.comment(0xABE7, 'Send final buffer', align=Align.INLINE)
d.comment(0xABEA, 'Load spool state', align=Align.INLINE)
d.comment(0xABED, 'Clear low nibble', align=Align.INLINE)
d.comment(0xABEF, 'Store cleaned state', align=Align.INLINE)
d.comment(0xABF2, 'Return', align=Align.INLINE)
d.comment(0xABF3, 'X = error code', align=Align.INLINE)
d.comment(0xABF4, 'Restore retry count', align=Align.INLINE)
d.comment(0xABF5, 'Set carry for subtract', align=Align.INLINE)
d.comment(0xABF6, 'Decrement retry count', align=Align.INLINE)
d.comment(0xABF8, 'Non-zero: retry send', align=Align.INLINE)
d.comment(0xABFA, 'Error code = 1? (busy)', align=Align.INLINE)
d.comment(0xABFC, 'No: printer jammed error', align=Align.INLINE)
d.comment(0xABFE, 'A=&A6: printer busy error number', align=Align.INLINE)
d.comment(0xAC00, "Generate 'Printer busy' error", align=Align.INLINE)
d.comment(0xAC10, 'A=&A7: printer jammed error number', align=Align.INLINE)
d.comment(0xAC12, "Generate 'Printer jammed' error", align=Align.INLINE)
d.comment(0xAC24, 'Set TX ptr low byte', align=Align.INLINE)
d.comment(0xAC26, 'Set TX ptr high byte', align=Align.INLINE)
d.comment(0xAC28, 'Save disconnect code', align=Align.INLINE)
d.comment(0xAC29, 'Test if zero', align=Align.INLINE)
d.comment(0xAC2B, 'Zero: skip station search', align=Align.INLINE)
d.comment(0xAC2D, 'X=&FF: start search from -1', align=Align.INLINE)
d.comment(0xAC2F, 'Y = disconnect code', align=Align.INLINE)
d.comment(0xAC30, 'A = disconnect code', align=Align.INLINE)
d.comment(0xAC31, 'Next station index', align=Align.INLINE)
d.comment(0xAC32, 'Compare with station table entry', align=Align.INLINE)
d.comment(0xAC35, 'Match: verify station/network', align=Align.INLINE)
d.comment(0xAC37, 'Past last station?', align=Align.INLINE)
d.comment(0xAC39, 'No: try next', align=Align.INLINE)
d.comment(0xAC3B, 'Not found: A=0', align=Align.INLINE)
d.comment(0xAC3D, 'Skip to status update', align=Align.INLINE)
d.comment(0xAC3F, 'Y = disconnect code for compare', align=Align.INLINE)
d.comment(0xAC40, 'Check station and network match', align=Align.INLINE)
d.comment(0xAC43, 'No match: try next station', align=Align.INLINE)
d.comment(0xAC45, 'Load station status flags', align=Align.INLINE)
d.comment(0xAC48, 'Isolate bit 0 (active flag)', align=Align.INLINE)
d.comment(0xAC4A, 'Y=0: TX buffer status offset', align=Align.INLINE)
d.comment(0xAC4C, 'OR with existing status byte', align=Align.INLINE)
d.comment(0xAC4E, 'Save combined status', align=Align.INLINE)
d.comment(0xAC4F, 'Store to TX buffer', align=Align.INLINE)
d.comment(0xAC51, 'Send the packet', align=Align.INLINE)
d.comment(0xAC54, 'Set end markers to &FF', align=Align.INLINE)
d.comment(0xAC56, 'Y=8: first end marker offset', align=Align.INLINE)
d.comment(0xAC58, 'Store &FF', align=Align.INLINE)
d.comment(0xAC5B, 'Store &FF at offset 9 too', align=Align.INLINE)
d.comment(0xAC5D, 'Restore disconnect code', align=Align.INLINE)
d.comment(0xAC5E, 'X = status for control byte', align=Align.INLINE)
d.comment(0xAC5F, 'Y=&D1: default control', align=Align.INLINE)
d.comment(0xAC61, 'Check original disconnect code', align=Align.INLINE)
d.comment(0xAC62, 'Peek but keep on stack', align=Align.INLINE)
d.comment(0xAC63, 'Zero: use &D1 control', align=Align.INLINE)
d.comment(0xAC65, 'Non-zero: use &90 control', align=Align.INLINE)
d.comment(0xAC67, 'A = control byte (Y)', align=Align.INLINE)
d.comment(0xAC68, 'Y=1: control byte offset', align=Align.INLINE)
d.comment(0xAC6A, 'Store control byte', align=Align.INLINE)
d.comment(0xAC6C, 'A = X (status)', align=Align.INLINE)
d.comment(0xAC6D, 'Y=0', align=Align.INLINE)
d.comment(0xAC6E, 'Save status on stack', align=Align.INLINE)
d.comment(0xAC6F, 'Set status to &7F (waiting)', align=Align.INLINE)
d.comment(0xAC71, 'Store at TX buffer offset 0', align=Align.INLINE)
d.comment(0xAC73, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xAC76, 'Restore status', align=Align.INLINE)
d.comment(0xAC77, 'Keep on stack for next check', align=Align.INLINE)
d.comment(0xAC78, 'Compare with current TX buffer', align=Align.INLINE)
d.comment(0xAC7A, 'Rotate result bit 0 to carry', align=Align.INLINE)
d.comment(0xAC7B, 'C=1: status changed, retry', align=Align.INLINE)
d.comment(0xAC7D, 'Done: discard status', align=Align.INLINE)
d.comment(0xAC7E, 'Discard disconnect code', align=Align.INLINE)
d.comment(0xAC7F, 'Return', align=Align.INLINE)
d.comment(0xAC80, """Spool TX control block template

12-byte TXCB template copied directly (no
marker processing) to workspace at offset
&21..&2C. Destination station and network
(&23/&24) are filled in from (nfs_workspace)
after the copy.""")
d.comment(0xAC80, 'ctrl=&80 (standard TX)', align=Align.INLINE)
d.comment(0xAC81, 'port=&9F', align=Align.INLINE)
d.comment(0xAC82, 'dest station=&00 (filled later)', align=Align.INLINE)
d.comment(0xAC83, 'dest network=&00 (filled later)', align=Align.INLINE)
d.comment(0xAC85, 'buf start hi=&8E', align=Align.INLINE)
d.comment(0xAC86, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xAC87, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xAC89, 'buf end hi=&8E', align=Align.INLINE)
d.comment(0xAC8A, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xAC8B, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xAC8C, """Spool RX control block template

12-byte RXCB template with marker processing:
&FD skips the offset (preserves existing value)
and &FC substitutes net_rx_ptr_hi. Copied to
workspace at offset &00..&0B. Sets up a 3-byte
receive buffer at &xx31..&xx34.""")
d.comment(0xAC8C, 'ctrl=&7F (RX listen)', align=Align.INLINE)
d.comment(0xAC8D, 'port=&9E', align=Align.INLINE)
d.comment(0xAC8E, 'skip: preserve dest station', align=Align.INLINE)
d.comment(0xAC91, 'buf start hi=page ptr (&FC)', align=Align.INLINE)
d.comment(0xAC92, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xAC93, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xAC95, 'buf end hi=page ptr (&FC)', align=Align.INLINE)
d.comment(0xAC96, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xAC97, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xAC98, 'Save l00ad counter', align=Align.INLINE)
d.comment(0xAC9A, 'Push for later restore', align=Align.INLINE)
d.comment(0xAC9B, 'Set workspace low to &E9', align=Align.INLINE)
d.comment(0xAC9D, 'Store to nfs_workspace low', align=Align.INLINE)
d.comment(0xAC9F, 'Y=0: initial palette index', align=Align.INLINE)
d.comment(0xACA1, 'Clear palette counter', align=Align.INLINE)
d.comment(0xACA3, 'Load current screen mode', align=Align.INLINE)
d.comment(0xACA6, 'Store mode to workspace', align=Align.INLINE)
d.comment(0xACA8, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACAA, 'Load video ULA copy', align=Align.INLINE)
d.comment(0xACAD, 'Save for later restore', align=Align.INLINE)
d.comment(0xACAE, 'A=0 for first palette entry', align=Align.INLINE)
d.comment(0xACAF, 'Store logical colour to workspace', align=Align.INLINE)
d.comment(0xACB1, 'X = workspace ptr low', align=Align.INLINE)
d.comment(0xACB3, 'Y = workspace ptr high', align=Align.INLINE)
d.comment(0xACB5, 'OSWORD &0B: read palette', align=Align.INLINE)
d.comment(0xACB7, 'Read palette entry', align=Align.INLINE)
d.comment(0xACBA, 'Restore previous ULA value', align=Align.INLINE)
d.comment(0xACBB, 'Y=0: reset index', align=Align.INLINE)
d.comment(0xACBD, 'Store ULA value to workspace', align=Align.INLINE)
d.comment(0xACBF, 'Y=1: physical colour offset', align=Align.INLINE)
d.comment(0xACC0, 'Load physical colour', align=Align.INLINE)
d.comment(0xACC2, 'Save for next iteration', align=Align.INLINE)
d.comment(0xACC3, 'X = workspace ptr', align=Align.INLINE)
d.comment(0xACC5, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACC7, 'Advance palette counter', align=Align.INLINE)
d.comment(0xACC9, 'Y=0', align=Align.INLINE)
d.comment(0xACCA, 'Load counter', align=Align.INLINE)
d.comment(0xACCC, 'Reached &F9 workspace limit?', align=Align.INLINE)
d.comment(0xACCE, 'No: read next palette entry', align=Align.INLINE)
d.comment(0xACD0, 'Discard last ULA value', align=Align.INLINE)
d.comment(0xACD1, 'Clear counter', align=Align.INLINE)
d.comment(0xACD3, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACD5, 'Store extra palette info', align=Align.INLINE)
d.comment(0xACD8, 'Advance workspace ptr again', align=Align.INLINE)
d.comment(0xACDA, 'Restore original l00ad', align=Align.INLINE)
d.comment(0xACDB, 'Store restored counter', align=Align.INLINE)
d.comment(0xACDD, 'Load current state', align=Align.INLINE)
d.comment(0xACE0, 'Store as committed state', align=Align.INLINE)
d.comment(0xACE3, 'Return', align=Align.INLINE)
d.comment(0xACE4, 'Load palette register value', align=Align.INLINE)
d.comment(0xACE7, 'Store to workspace', align=Align.INLINE)
d.comment(0xACE9, 'X = palette register', align=Align.INLINE)
d.comment(0xACEC, 'Read OSBYTE for this mode', align=Align.INLINE)
d.comment(0xACEF, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACF1, 'A=0', align=Align.INLINE)
d.comment(0xACF2, 'Store zero to workspace', align=Align.INLINE)
d.comment(0xACF4, 'Read OSBYTE with X=0', align=Align.INLINE)
d.comment(0xACF7, 'X=0: read mode info', align=Align.INLINE)
d.comment(0xACF9, 'Load OSBYTE code index', align=Align.INLINE)
d.comment(0xACFB, 'Advance index counter', align=Align.INLINE)
d.comment(0xACFD, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACFF, 'Load OSBYTE number from table', align=Align.INLINE)
d.comment(0xAD02, 'Y=&FF: read current value', align=Align.INLINE)
d.comment(0xAD04, 'Call OSBYTE to read value', align=Align.INLINE)
d.comment(0xAD07, 'A = result (from X)', align=Align.INLINE)
d.comment(0xAD08, 'X=0 for indexed store', align=Align.INLINE)
d.comment(0xAD0A, 'Store result to workspace', align=Align.INLINE)
d.comment(0xAD0C, 'Return', align=Align.INLINE)
d.comment(0xAD0D, """OSBYTE mode read codes

Three OSBYTE numbers used by read_osbyte_to_ws
to save display mode state to workspace before
a language 2 file transfer.""")
d.comment(0xAD0E, 'OSBYTE &C2: read video ULA ctrl', align=Align.INLINE)
d.comment(0xAD0F, 'OSBYTE &C3: read video ULA palette', align=Align.INLINE)
d.comment(0xBA1B, 'Open file for reading, set ws_page', align=Align.INLINE)
d.comment(0xBA1E, '21 bytes to push (0-&14)', align=Align.INLINE)
d.comment(0xBA20, 'Zero fill value', align=Align.INLINE)
d.comment(0xBA22, 'Push zero onto stack', align=Align.INLINE)
d.comment(0xBA23, 'Count down', align=Align.INLINE)
d.comment(0xBA24, 'Loop until all 21 bytes pushed', align=Align.INLINE)
d.comment(0xBA26, 'X = stack pointer (buffer base - 1)', align=Align.INLINE)
d.comment(0xBA27, 'Set up buffer pointer and parse args', align=Align.INLINE)
d.comment(0xBA2A, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBA2C, 'Test high nibble', align=Align.INLINE)
d.comment(0xBA2E, 'Skip header if 16-byte aligned', align=Align.INLINE)
d.comment(0xBA30, 'Print column header for offset start', align=Align.INLINE)
d.comment(0xBA33, 'Check for Escape key', align=Align.INLINE)
d.comment(0xBA36, 'Start byte counter at -1', align=Align.INLINE)
d.comment(0xBA38, 'Reset counter', align=Align.INLINE)
d.comment(0xBA3F, 'C=1 from OSBGET: end of file', align=Align.INLINE)
d.comment(0xBA41, 'Increment byte counter (0-15)', align=Align.INLINE)
d.comment(0xBA43, 'Use counter as buffer index', align=Align.INLINE)
d.comment(0xBA45, 'Store byte in data buffer', align=Align.INLINE)
d.comment(0xBA47, 'Read 16 bytes? (index 0-15)', align=Align.INLINE)
d.comment(0xBA49, 'No: read next byte', align=Align.INLINE)
d.comment(0xBA4B, 'C=0: not EOF, full line read', align=Align.INLINE)
d.comment(0xBA4C, 'Save C: EOF status', align=Align.INLINE)
d.comment(0xBA4D, 'Check byte counter', align=Align.INLINE)
d.comment(0xBA4F, 'Counter >= 0: have data to display', align=Align.INLINE)
d.comment(0xBA51, '22 bytes to pop (21 buffer + PHP)', align=Align.INLINE)
d.comment(0xBA53, 'Pop one byte from stack', align=Align.INLINE)
d.comment(0xBA54, 'Count down', align=Align.INLINE)
d.comment(0xBA55, 'Loop until stack cleaned up', align=Align.INLINE)
d.comment(0xBA57, 'Close file and return', align=Align.INLINE)
d.comment(0xBA5A, 'Point to display address low byte', align=Align.INLINE)
d.comment(0xBA5C, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBA5E, 'Test high nibble', align=Align.INLINE)
d.comment(0xBA60, 'Non-zero: header already current', align=Align.INLINE)
d.comment(0xBA62, 'Crossed 256-byte boundary: new header', align=Align.INLINE)
d.comment(0xBA65, 'Start from highest address byte', align=Align.INLINE)
d.comment(0xBA67, 'Load address byte', align=Align.INLINE)
d.comment(0xBA69, 'Save for address increment later', align=Align.INLINE)
d.comment(0xBA6A, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBA6D, 'Restore address byte', align=Align.INLINE)
d.comment(0xBA6E, 'Next byte down', align=Align.INLINE)
d.comment(0xBA6F, 'Printed all 4 address bytes?', align=Align.INLINE)
d.comment(0xBA71, 'No: print next address byte', align=Align.INLINE)
d.comment(0xBA73, 'Y=&10: point to address byte 0', align=Align.INLINE)
d.comment(0xBA74, 'Prepare for 16-byte add', align=Align.INLINE)
d.comment(0xBA75, 'Add 16 to lowest address byte', align=Align.INLINE)
d.comment(0xBA77, 'Save carry for propagation', align=Align.INLINE)
d.comment(0xBA78, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0xBA79, 'Store updated address byte', align=Align.INLINE)
d.comment(0xBA7B, 'Next address byte up', align=Align.INLINE)
d.comment(0xBA7C, 'Load next address byte', align=Align.INLINE)
d.comment(0xBA7E, 'Add carry', align=Align.INLINE)
d.comment(0xBA80, 'Save carry for next byte', align=Align.INLINE)
d.comment(0xBA81, 'Past all 4 address bytes?', align=Align.INLINE)
d.comment(0xBA83, 'No: continue propagation', align=Align.INLINE)
d.comment(0xBA85, 'Discard final carry', align=Align.INLINE)
d.comment(0xBA86, 'Print address/data separator', align=Align.INLINE)
d.comment(0xBA8C, 'Start from first data byte', align=Align.INLINE)
d.comment(0xBA8E, 'X = bytes read (counter for display)', align=Align.INLINE)
d.comment(0xBA90, 'Load data byte from buffer', align=Align.INLINE)
d.comment(0xBA92, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBA95, 'Space separator', align=Align.INLINE)
d.comment(0xBA95, 'Next column', align=Align.INLINE)
d.comment(0xBA96, 'All 16 columns done?', align=Align.INLINE)
d.comment(0xBA98, 'Yes: go to ASCII separator', align=Align.INLINE)
d.comment(0xBA9A, 'Decrement remaining data bytes', align=Align.INLINE)
d.comment(0xBA9B, 'More data: print next hex byte', align=Align.INLINE)
d.comment(0xBA9D, 'Save column position', align=Align.INLINE)
d.comment(0xBA9E, 'Preserve Y across print', align=Align.INLINE)
d.comment(0xBA9F, 'Print 3-space padding', align=Align.INLINE)
d.comment(0xBAA5, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xBAA6, 'Restore column position', align=Align.INLINE)
d.comment(0xBAA7, 'Back to Y', align=Align.INLINE)
d.comment(0xBAA8, 'Check next column', align=Align.INLINE)
d.comment(0xBAAB, 'Adjust X for advance_x_by_8', align=Align.INLINE)
d.comment(0xBAAC, 'Print hex/ASCII separator', align=Align.INLINE)
d.comment(0xBAB1, 'Y=0: start ASCII section from byte 0', align=Align.INLINE)
d.comment(0xBAB3, 'Advance X to ASCII display column', align=Align.INLINE)
d.comment(0xBAB6, 'Load data byte', align=Align.INLINE)
d.comment(0xBAB8, 'Strip high bit', align=Align.INLINE)
d.comment(0xBABA, 'Printable? (>= space)', align=Align.INLINE)
d.comment(0xBABC, 'Yes: check for DEL', align=Align.INLINE)
d.comment(0xBABE, "Non-printable: substitute '.'", align=Align.INLINE)
d.comment(0xBAC0, 'Is it DEL (&7F)?', align=Align.INLINE)
d.comment(0xBAC2, "Yes: substitute '.'", align=Align.INLINE)
d.comment(0xBAC4, 'Print ASCII character', align=Align.INLINE)
d.comment(0xBAC7, 'Next column', align=Align.INLINE)
d.comment(0xBAC8, 'All 16 columns done?', align=Align.INLINE)
d.comment(0xBACA, 'Yes: end of line', align=Align.INLINE)
d.comment(0xBACC, 'Decrement remaining data bytes', align=Align.INLINE)
d.comment(0xBACD, 'More data: print next ASCII char', align=Align.INLINE)
d.comment(0xBACF, 'Print newline', align=Align.INLINE)
d.comment(0xBAD2, 'Restore EOF status from &BA4C', align=Align.INLINE)
d.comment(0xBAD3, 'C=1: EOF reached, clean up', align=Align.INLINE)
d.comment(0xBAD5, 'Not EOF: continue with next line', align=Align.INLINE)
d.comment(0xBAD8, '21 bytes to pop (buffer only, PHP done)', align=Align.INLINE)
d.comment(0xBADA, 'Reuse stack cleanup loop', align=Align.INLINE)
d.comment(0xBADD, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBADF, 'Save as starting column number', align=Align.INLINE)
d.comment(0xBAE0, 'Print header label with leading CR', align=Align.INLINE)
d.comment(0xBAEF, 'X=&0F: 16 column numbers to print', align=Align.INLINE)
d.comment(0xBAF1, 'Restore starting column number', align=Align.INLINE)
d.comment(0xBAF2, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBAF5, 'Space separator', align=Align.INLINE)
d.comment(0xBAFA, 'Restore column number', align=Align.INLINE)
d.comment(0xBAF5, 'SEC for +1 via ADC', align=Align.INLINE)
d.comment(0xBAF6, 'Increment column number (SEC+ADC 0=+1)', align=Align.INLINE)
d.comment(0xBAF8, 'Wrap to low nibble (0-F)', align=Align.INLINE)
d.comment(0xBAFA, 'Count down', align=Align.INLINE)
d.comment(0xBAFB, 'Loop for all 16 columns', align=Align.INLINE)
d.comment(0xBAFD, 'Print trailer with ASCII label', align=Align.INLINE)
d.comment(0xBB03, 'Save byte value on stack', align=Align.INLINE)
d.comment(0xBB07, 'A=&20: space character', align=Align.INLINE)
d.comment(0xBB09, 'Print space character', align=Align.INLINE)
d.comment(0xBB0C, 'Restore byte value from stack', align=Align.INLINE)
d.comment(0xBB0D, 'Return; Y = offset to next argument', align=Align.INLINE)
d.comment(0xBB0E, 'Save command line offset to X', align=Align.INLINE)
d.comment(0xBB0F, 'X tracks current position', align=Align.INLINE)
d.comment(0xBB10, 'Zero for clearing accumulator', align=Align.INLINE)
d.comment(0xBB12, 'Y=0 for buffer indexing', align=Align.INLINE)
d.comment(0xBB13, 'Clear accumulator byte', align=Align.INLINE)
d.comment(0xBB15, 'Next byte', align=Align.INLINE)
d.comment(0xBB16, 'All 4 bytes cleared?', align=Align.INLINE)
d.comment(0xBB18, 'No: clear next', align=Align.INLINE)
d.comment(0xBB1A, 'Restore pre-increment offset to A', align=Align.INLINE)
d.comment(0xBB1B, 'Advance X to next char position', align=Align.INLINE)
d.comment(0xBB1C, 'Y = pre-increment offset for indexing', align=Align.INLINE)
d.comment(0xBB1D, 'Load character from command line', align=Align.INLINE)
d.comment(0xBB1F, 'CR: end of input', align=Align.INLINE)
d.comment(0xBB21, 'Done: skip trailing spaces', align=Align.INLINE)
d.comment(0xBB23, 'Space: end of this parameter', align=Align.INLINE)
d.comment(0xBB25, 'Done: skip trailing spaces', align=Align.INLINE)
d.comment(0xBB27, "Below '0'?", align=Align.INLINE)
d.comment(0xBB29, 'Yes: not a hex digit, error', align=Align.INLINE)
d.comment(0xBB2B, "Below ':'? (i.e. '0'-'9')", align=Align.INLINE)
d.comment(0xBB2D, 'Yes: is a decimal digit', align=Align.INLINE)
d.comment(0xBB2F, 'Force uppercase for A-F', align=Align.INLINE)
d.comment(0xBB31, "Map 'A'-'F' → &FA-&FF (C=0 here)", align=Align.INLINE)
d.comment(0xBB33, "Carry set: char > 'F', error", align=Align.INLINE)
d.comment(0xBB35, "Below &FA? (i.e. was < 'A')", align=Align.INLINE)
d.comment(0xBB37, "Yes: gap between '9' and 'A', error", align=Align.INLINE)
d.comment(0xBB39, 'Mask to low nibble (0-15)', align=Align.INLINE)
d.comment(0xBB3B, 'Save hex digit value', align=Align.INLINE)
d.comment(0xBB3C, 'Save current offset', align=Align.INLINE)
d.comment(0xBB3D, 'Preserve on stack', align=Align.INLINE)
d.comment(0xBB3E, '4 bits to shift in', align=Align.INLINE)
d.comment(0xBB40, 'Start from byte 0 (LSB)', align=Align.INLINE)
d.comment(0xBB42, 'Clear A; C from PHA/PLP below', align=Align.INLINE)
d.comment(0xBB43, 'Transfer carry bit to flags via stack', align=Align.INLINE)
d.comment(0xBB44, 'PLP: C = bit shifted out of prev iter', align=Align.INLINE)
d.comment(0xBB45, 'Load accumulator byte', align=Align.INLINE)
d.comment(0xBB47, 'Rotate left through carry', align=Align.INLINE)
d.comment(0xBB48, 'Store shifted byte', align=Align.INLINE)
d.comment(0xBB4A, 'Save carry for next byte', align=Align.INLINE)
d.comment(0xBB4B, 'Transfer to A for PHA/PLP trick', align=Align.INLINE)
d.comment(0xBB4C, 'Next accumulator byte', align=Align.INLINE)
d.comment(0xBB4D, 'All 4 bytes rotated?', align=Align.INLINE)
d.comment(0xBB4F, 'No: rotate next byte', align=Align.INLINE)
d.comment(0xBB51, 'Transfer carry to flags', align=Align.INLINE)
d.comment(0xBB52, 'C = overflow bit', align=Align.INLINE)
d.comment(0xBB53, 'Overflow: address too large', align=Align.INLINE)
d.comment(0xBB55, 'Count bits shifted', align=Align.INLINE)
d.comment(0xBB56, '4 bits shifted? No: shift again', align=Align.INLINE)
d.comment(0xBB58, 'Restore command line offset', align=Align.INLINE)
d.comment(0xBB59, 'Back to X', align=Align.INLINE)
d.comment(0xBB5A, 'Restore hex digit value', align=Align.INLINE)
d.comment(0xBB5B, 'Point to LSB of accumulator', align=Align.INLINE)
d.comment(0xBB5D, 'OR digit into low nibble', align=Align.INLINE)
d.comment(0xBB5F, 'Store updated LSB', align=Align.INLINE)
d.comment(0xBB61, 'Parse next character', align=Align.INLINE)
d.comment(0xBB64, 'Discard saved offset', align=Align.INLINE)
d.comment(0xBB65, 'Discard saved digit', align=Align.INLINE)
d.comment(0xBB66, 'C=1: overflow', align=Align.INLINE)
d.comment(0xBB67, 'Return with C=1', align=Align.INLINE)
d.comment(0xBB68, 'Close open file before error', align=Align.INLINE)
d.comment(0xBB6B, "Generate 'Bad hex' error", align=Align.INLINE)
d.comment(0xBB6E, 'Advance past space', align=Align.INLINE)
d.comment(0xBB6F, 'Load next char', align=Align.INLINE)
d.comment(0xBB71, 'Space?', align=Align.INLINE)
d.comment(0xBB73, 'Yes: skip it', align=Align.INLINE)
d.comment(0xBB75, 'C=0: valid parse (no overflow)', align=Align.INLINE)
d.comment(0xBB76, 'Return; Y past trailing spaces', align=Align.INLINE)
d.comment(0xBB77, 'X+1: first byte of buffer', align=Align.INLINE)
d.comment(0xBB78, 'Set buffer pointer low byte', align=Align.INLINE)
d.comment(0xBB7A, 'Buffer is on stack in page 1', align=Align.INLINE)
d.comment(0xBB7C, 'Set buffer pointer high byte', align=Align.INLINE)
d.comment(0xBB7E, 'Parse start offset from command line', align=Align.INLINE)
d.comment(0xBB81, "Overflow: 'Outside file' error", align=Align.INLINE)
d.comment(0xBB83, 'A = command line offset after parse', align=Align.INLINE)
d.comment(0xBB84, 'Save for later (past start addr)', align=Align.INLINE)
d.comment(0xBB89, 'A=2: read file extent (length)', align=Align.INLINE)
d.comment(0xBB8E, 'Check from MSB down', align=Align.INLINE)
d.comment(0xBB90, 'Load file length byte', align=Align.INLINE)
d.comment(0xBB93, 'Compare with start offset byte', align=Align.INLINE)
d.comment(0xBB95, 'Mismatch: check which is larger', align=Align.INLINE)
d.comment(0xBB97, 'Next byte down', align=Align.INLINE)
d.comment(0xBB98, 'More bytes to compare', align=Align.INLINE)
d.comment(0xBB9A, 'All equal: start = length, within file', align=Align.INLINE)
d.comment(0xBB9C, 'Length < start: outside file', align=Align.INLINE)
d.comment(0xBB9E, 'Y=&FF: length > start, flag for later', align=Align.INLINE)
d.comment(0xBBA0, 'Continue to copy start address', align=Align.INLINE)
d.comment(0xBBA2, 'Close file before error', align=Align.INLINE)
d.comment(0xBBA5, 'Error number &B7', align=Align.INLINE)
d.comment(0xBBA7, "Generate 'Outside file' error", align=Align.INLINE)
d.comment(0xBBB7, 'Load start address byte from buffer', align=Align.INLINE)
d.comment(0xBBB9, 'Store to osword_flag (&AA-&AD)', align=Align.INLINE)
d.comment(0xBBBC, 'Next byte', align=Align.INLINE)
d.comment(0xBBBD, 'All 4 bytes copied?', align=Align.INLINE)
d.comment(0xBBBF, 'No: copy next byte', align=Align.INLINE)
d.comment(0xBBC5, 'A=1: write file pointer', align=Align.INLINE)
d.comment(0xBBC7, 'OSARGS: set file pointer', align=Align.INLINE)
d.comment(0xBBCA, 'Restore saved command line offset', align=Align.INLINE)
d.comment(0xBBCB, 'Back to Y for command line indexing', align=Align.INLINE)
d.comment(0xBBCC, 'Load next char from command line', align=Align.INLINE)
d.comment(0xBBCE, 'End of command? (CR)', align=Align.INLINE)
d.comment(0xBBD0, 'No: parse display base address', align=Align.INLINE)
d.comment(0xBBD2, 'Copy 2 bytes: os_text_ptr to buffer', align=Align.INLINE)
d.comment(0xBBD4, 'Load os_text_ptr byte', align=Align.INLINE)
d.comment(0xBBD7, 'Store as filename pointer in OSFILE CB', align=Align.INLINE)
d.comment(0xBBD9, 'Next byte', align=Align.INLINE)
d.comment(0xBBDA, 'Copy both low and high bytes', align=Align.INLINE)
d.comment(0xBBDC, 'Read catalogue information', align=Align.INLINE)
d.comment(0xBBDE, 'X = control block low', align=Align.INLINE)
d.comment(0xBBE0, 'Y = control block high', align=Align.INLINE)
d.comment(0xBBE2, 'OSFILE: read file info', align=Align.INLINE)
d.comment(0xBBE5, 'Start at OSFILE +2 (load addr byte 0)', align=Align.INLINE)
d.comment(0xBBE7, 'Load from OSFILE result offset', align=Align.INLINE)
d.comment(0xBBE9, 'Y-2: destination is 2 bytes earlier', align=Align.INLINE)
d.comment(0xBBEA, 'Continue decrement', align=Align.INLINE)
d.comment(0xBBEB, 'Store to buf[Y-2]', align=Align.INLINE)
d.comment(0xBBED, 'Y += 3: advance source index', align=Align.INLINE)
d.comment(0xBBEE, '(continued)', align=Align.INLINE)
d.comment(0xBBEF, '(continued)', align=Align.INLINE)
d.comment(0xBBF0, 'Copied all 4 load address bytes?', align=Align.INLINE)
d.comment(0xBBF2, 'No: copy next byte', align=Align.INLINE)
d.comment(0xBBF4, 'Y=6 after loop exit', align=Align.INLINE)
d.comment(0xBBF5, 'Y=4: check from buf[4] downward', align=Align.INLINE)
d.comment(0xBBF6, 'Load address byte', align=Align.INLINE)
d.comment(0xBBF8, 'Is it &FF?', align=Align.INLINE)
d.comment(0xBBFA, 'No: valid load address, use it', align=Align.INLINE)
d.comment(0xBBFC, 'Check next byte down', align=Align.INLINE)
d.comment(0xBBFD, 'More bytes to check for &FF', align=Align.INLINE)
d.comment(0xBBFF, 'Clear all 4 bytes', align=Align.INLINE)
d.comment(0xBC01, 'Zero value', align=Align.INLINE)
d.comment(0xBC03, 'Clear byte', align=Align.INLINE)
d.comment(0xBC05, 'Next byte down', align=Align.INLINE)
d.comment(0xBC06, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC08, 'Continue to compute display address', align=Align.INLINE)
d.comment(0xBC0A, 'Parse second hex parameter', align=Align.INLINE)
d.comment(0xBC0D, 'Valid: use as display base', align=Align.INLINE)
d.comment(0xBC0F, 'Invalid: close file before error', align=Align.INLINE)
d.comment(0xBC12, 'Error number &FC', align=Align.INLINE)
d.comment(0xBC14, "Generate 'Bad address' error", align=Align.INLINE)
d.comment(0xBC1F, 'Start from LSB', align=Align.INLINE)
d.comment(0xBC21, '4 bytes to add', align=Align.INLINE)
d.comment(0xBC23, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xBC24, 'Load display base byte', align=Align.INLINE)
d.comment(0xBC26, 'Add start offset byte', align=Align.INLINE)
d.comment(0xBC29, 'Store result in osword_flag', align=Align.INLINE)
d.comment(0xBC2C, 'Next byte', align=Align.INLINE)
d.comment(0xBC2D, 'Count down', align=Align.INLINE)
d.comment(0xBC2E, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC30, 'Point past end of address area', align=Align.INLINE)
d.comment(0xBC32, 'Start from MSB (byte 3)', align=Align.INLINE)
d.comment(0xBC34, 'Pre-decrement Y', align=Align.INLINE)
d.comment(0xBC35, 'Load computed display address byte', align=Align.INLINE)
d.comment(0xBC37, 'Store to buf[&10-&13]', align=Align.INLINE)
d.comment(0xBC39, 'Next byte down', align=Align.INLINE)
d.comment(0xBC3A, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC3C, 'Return; Y=&10 (address low byte)', align=Align.INLINE)
d.comment(0xBC3D, 'Load file handle from workspace', align=Align.INLINE)
d.comment(0xBC3F, 'A=0: close file', align=Align.INLINE)
d.comment(0xBC44, 'Save caller flags', align=Align.INLINE)
d.comment(0xBC45, 'A=filename offset from Y', align=Align.INLINE)
d.comment(0xBC86, 'JSR+fall-through: 8+8=16 INXs total', align=Align.INLINE)
d.comment(0xBC46, 'Clear carry for 16-bit addition', align=Align.INLINE)
d.comment(0xBC89, 'JSR+fall-through: 4+4=8 INXs', align=Align.INLINE)
d.comment(0xBC47, 'Add text pointer low byte', align=Align.INLINE)
d.comment(0xBC8C, 'X += 4', align=Align.INLINE)
d.comment(0xBC49, 'Save filename address low', align=Align.INLINE)
d.comment(0xBC8D, '(continued)', align=Align.INLINE)
d.comment(0xBC4A, 'X=filename address low (for OSFIND)', align=Align.INLINE)
d.comment(0xBC8E, '(continued)', align=Align.INLINE)
d.comment(0xBC4B, 'A=0: carry propagation only', align=Align.INLINE)
d.comment(0xBC8F, '(continued)', align=Align.INLINE)
d.comment(0xBC4D, 'Add text pointer high byte + carry', align=Align.INLINE)
d.comment(0xBC90, 'Return', align=Align.INLINE)
d.comment(0xBC4F, 'Save filename address high', align=Align.INLINE)
d.comment(0xBC93, 'Padding; next byte is reloc_p5_src', align=Align.INLINE)
d.comment(0xBC50, 'Y=filename address high (for OSFIND)', align=Align.INLINE)
d.comment(0xBC51, 'A=&40: open for reading', align=Align.INLINE)
d.comment(0xBC57, 'Store file handle in workspace', align=Align.INLINE)
d.comment(0xBC59, 'Non-zero: file opened successfully', align=Align.INLINE)
d.comment(0xBC5B, 'Error &D6', align=Align.INLINE)
d.comment(0xBC5D, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0xB359, 'Mask owner access flags to 5 bits', align=Align.INLINE)
d.comment(0xB35C, 'Initialise file index to 0', align=Align.INLINE)
d.comment(0xB35E, 'Store file counter', align=Align.INLINE)
d.comment(0xB360, 'Save pointer to command text', align=Align.INLINE)
d.comment(0xB363, 'Parse wildcard filename argument', align=Align.INLINE)
d.comment(0xB366, 'Advance past CR terminator', align=Align.INLINE)
d.comment(0xB367, 'Save end-of-argument buffer position', align=Align.INLINE)
d.comment(0xBC6A, 'Restore text pointer high from stack', align=Align.INLINE)
d.comment(0xBC6B, 'Set OS text pointer high', align=Align.INLINE)
d.comment(0xB369, 'Command code 1 = examine directory', align=Align.INLINE)
d.comment(0xB36B, 'Store command in TX buffer byte 0', align=Align.INLINE)
d.comment(0xB36E, 'Store flag in TX buffer byte 2', align=Align.INLINE)
d.comment(0xB371, 'Load current file index', align=Align.INLINE)
d.comment(0xB373, 'Store file index in TX buffer byte 1', align=Align.INLINE)
d.comment(0xB376, 'X=3: copy from TX buffer offset 3', align=Align.INLINE)
d.comment(0xB378, 'Copy filename argument to TX buffer', align=Align.INLINE)
d.comment(0xB37B, 'Function code 3 = examine', align=Align.INLINE)
d.comment(0xB37D, 'Flag &80 = escapable', align=Align.INLINE)
d.comment(0xB37F, 'Mark operation as escapable', align=Align.INLINE)
d.comment(0xB381, 'Send examine request to file server', align=Align.INLINE)
d.comment(0xB384, 'Get server response status', align=Align.INLINE)
d.comment(0xB387, 'Non-zero: file found, process it', align=Align.INLINE)
d.comment(0xBC6D, 'Restore text pointer low from stack', align=Align.INLINE)
d.comment(0xBC6E, 'Set OS text pointer low', align=Align.INLINE)
d.comment(0xB389, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0xB38B, 'X=1: flush input buffers', align=Align.INLINE)
d.comment(0xB38D, 'Flush keyboard buffer', align=Align.INLINE)
d.comment(0xB390, 'OSBYTE &7A: keyboard scan from 16', align=Align.INLINE)
d.comment(0xB392, 'Scan keyboard to clear state', align=Align.INLINE)
d.comment(0xB395, 'Y=0: no key pressed', align=Align.INLINE)
d.comment(0xB397, 'OSBYTE &78: write keys pressed', align=Align.INLINE)
d.comment(0xB399, 'Clear keyboard state and return', align=Align.INLINE)
d.comment(0xBC70, 'Y=0: start from beginning', align=Align.INLINE)
d.comment(0xBC72, 'Advance to next character', align=Align.INLINE)
d.comment(0xB39C, 'Load first attribute char of response', align=Align.INLINE)
d.comment(0xB39F, 'Is file locked?', align=Align.INLINE)
d.comment(0xB3A1, 'No: check if directory', align=Align.INLINE)
d.comment(0xB3A3, 'Skip locked file, advance index', align=Align.INLINE)
d.comment(0xB3A5, 'Request next file from server', align=Align.INLINE)
d.comment(0xB3A8, 'Is it a directory entry?', align=Align.INLINE)
d.comment(0xB3AA, 'No: regular file, show prompt', align=Align.INLINE)
d.comment(0xB3AC, 'Check directory contents flag', align=Align.INLINE)
d.comment(0xB3AF, 'Non-empty dir: treat as locked, skip', align=Align.INLINE)
d.comment(0xBC73, 'Load character from command text', align=Align.INLINE)
d.comment(0xBC75, 'CR (end of line)?', align=Align.INLINE)
d.comment(0xB3B1, 'X=1: start from response byte 1', align=Align.INLINE)
d.comment(0xB3B3, 'Y = destination index in delete buffer', align=Align.INLINE)
d.comment(0xB3B5, 'Load filename char from response', align=Align.INLINE)
d.comment(0xB3B8, 'Print filename character to screen', align=Align.INLINE)
d.comment(0xB3BB, 'Store in delete command buffer too', align=Align.INLINE)
d.comment(0xB3BE, 'Advance destination index', align=Align.INLINE)
d.comment(0xB3BF, 'Advance source index', align=Align.INLINE)
d.comment(0xB3C0, 'Copied all 11 filename characters?', align=Align.INLINE)
d.comment(0xB3C2, 'No: continue copying', align=Align.INLINE)
d.comment(0xB3C4, "Print '(Y/N/?) ' prompt", align=Align.INLINE)
d.comment(0xB3CA, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xB3CB, 'Read user response character', align=Align.INLINE)
d.comment(0xB3CE, "User pressed '?'?", align=Align.INLINE)
d.comment(0xB3D0, 'No: check for Y/N response', align=Align.INLINE)
d.comment(0xBC77, 'Yes: finished parsing filename', align=Align.INLINE)
d.comment(0xBC79, 'Space (word separator)?', align=Align.INLINE)
d.comment(0xB3D2, 'Carriage return before full info', align=Align.INLINE)
d.comment(0xB3D4, 'Print CR', align=Align.INLINE)
d.comment(0xB3D7, 'X=2: start from response byte 2', align=Align.INLINE)
d.comment(0xB3D9, 'Load file info character', align=Align.INLINE)
d.comment(0xB3DC, 'Print file info character', align=Align.INLINE)
d.comment(0xB3DF, 'Advance to next character', align=Align.INLINE)
d.comment(0xB3E0, 'Printed all &3C info bytes?', align=Align.INLINE)
d.comment(0xB3E2, 'No: continue printing', align=Align.INLINE)
d.comment(0xB3E4, "Print ' (Y/N) ' prompt (no '?')", align=Align.INLINE)
d.comment(0xB3E9, 'Padding (string terminator)', align=Align.INLINE)
d.comment(0xB3EA, 'Read user response (Y/N only)', align=Align.INLINE)
d.comment(0xBC7B, 'No: still within filename', align=Align.INLINE)
d.comment(0xBC7D, 'Advance past space', align=Align.INLINE)
d.comment(0xB3ED, 'Force uppercase', align=Align.INLINE)
d.comment(0xB3EF, "User said 'Y' (yes)?", align=Align.INLINE)
d.comment(0xB3F1, 'No: print newline, skip to next file', align=Align.INLINE)
d.comment(0xB3F3, "Echo 'Y' to screen", align=Align.INLINE)
d.comment(0xB3F6, 'X=0: start of stored filename', align=Align.INLINE)
d.comment(0xB3F8, 'Check first byte of stored name', align=Align.INLINE)
d.comment(0xB3FB, 'Is first byte CR (empty first field)?', align=Align.INLINE)
d.comment(0xB3FD, 'Yes: use second filename field', align=Align.INLINE)
d.comment(0xBC7E, 'Load next character', align=Align.INLINE)
d.comment(0xBC80, 'Another space?', align=Align.INLINE)
d.comment(0xBC82, 'Yes: skip consecutive spaces', align=Align.INLINE)
d.comment(0xB3FF, 'Load byte from stored filename', align=Align.INLINE)
d.comment(0xB402, 'Is it CR (field separator)?', align=Align.INLINE)
d.comment(0xB404, 'No: check for space', align=Align.INLINE)
d.comment(0xB406, "Replace CR with '.' directory sep", align=Align.INLINE)
d.comment(0xB408, 'Is it a space (name terminator)?', align=Align.INLINE)
d.comment(0xB40A, 'No: keep character as-is', align=Align.INLINE)
d.comment(0xB40C, 'Replace space with CR (end of name)', align=Align.INLINE)
d.comment(0xB40E, 'Store in delete command TX buffer', align=Align.INLINE)
d.comment(0xB411, 'Advance to next character', align=Align.INLINE)
d.comment(0xB412, 'Was it the CR terminator?', align=Align.INLINE)
d.comment(0xB414, 'No: continue building delete command', align=Align.INLINE)
d.comment(0xB416, 'Function code &14 = delete file', align=Align.INLINE)
d.comment(0xB418, 'Send delete request to file server', align=Align.INLINE)
d.comment(0xB41B, 'Adjust file index after deletion', align=Align.INLINE)
d.comment(0xBC84, 'Restore caller flags', align=Align.INLINE)
d.comment(0xBC85, 'Return; Y=offset past filename', align=Align.INLINE)
d.comment(0xB41D, 'Print newline after user response', align=Align.INLINE)
d.comment(0xB420, 'Advance index, process next file', align=Align.INLINE)
d.comment(0xB423, 'DEX to offset following INX', align=Align.INLINE)
d.comment(0xB424, 'Advance to next byte', align=Align.INLINE)
d.comment(0xB425, 'Load byte from second field', align=Align.INLINE)
d.comment(0xB428, 'Store in delete command TX buffer', align=Align.INLINE)
d.comment(0xB42B, 'Is it a space (field terminator)?', align=Align.INLINE)
d.comment(0xB42D, 'No: continue copying second field', align=Align.INLINE)
d.comment(0xB42F, 'Space found: terminate with CR', align=Align.INLINE)
d.comment(0xB431, "Print 'Y/N) ' prompt", align=Align.INLINE)
d.comment(0xB439, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0xB43B, 'X=1: flush input buffers', align=Align.INLINE)
d.comment(0xB43D, 'Flush keyboard buffer before read', align=Align.INLINE)
d.comment(0xB440, 'Read character from input stream', align=Align.INLINE)
d.comment(0xB443, 'C clear: character read OK', align=Align.INLINE)
d.comment(0xB445, 'Escape pressed: raise error', align=Align.INLINE)
d.comment(0xB448, 'Return with character in A', align=Align.INLINE)
d.comment(0xB449, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB44B, 'Y=0: start index', align=Align.INLINE)
d.comment(0xB44C, 'Clear channel table entry', align=Align.INLINE)
d.comment(0xB44F, 'Next entry', align=Align.INLINE)
d.comment(0xB450, 'Loop until all 256 bytes cleared', align=Align.INLINE)
d.comment(0xB452, 'Offset &0F in receive buffer', align=Align.INLINE)
d.comment(0xB454, 'Get number of available channels', align=Align.INLINE)
d.comment(0xB456, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB457, "Subtract 'Z' to get negative count", align=Align.INLINE)
d.comment(0xB459, 'Y = negative channel count (index)', align=Align.INLINE)
d.comment(0xB45A, 'Channel marker &40 (available)', align=Align.INLINE)
d.comment(0xB45C, 'Mark channel slot as available', align=Align.INLINE)
d.comment(0xB45F, 'Previous channel slot', align=Align.INLINE)
d.comment(0xB460, 'Reached start of channel range?', align=Align.INLINE)
d.comment(0xB462, 'No: continue marking channels', align=Align.INLINE)
d.comment(0xB464, 'Point to first channel slot', align=Align.INLINE)
d.comment(0xB465, 'Active channel marker &C0', align=Align.INLINE)
d.comment(0xB467, 'Mark first channel as active', align=Align.INLINE)
d.comment(0xB46A, 'Return', align=Align.INLINE)
d.comment(0xB46B, 'Save flags', align=Align.INLINE)
d.comment(0xB46C, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB46D, 'Subtract &20 to get table index', align=Align.INLINE)
d.comment(0xB46F, 'Negative: out of valid range', align=Align.INLINE)
d.comment(0xB471, 'Above maximum channel index &0F?', align=Align.INLINE)
d.comment(0xB473, 'In range: valid index', align=Align.INLINE)
d.comment(0xB475, 'Out of range: return &FF (invalid)', align=Align.INLINE)
d.comment(0xB477, 'Restore flags', align=Align.INLINE)
d.comment(0xB478, 'X = channel index (or &FF)', align=Align.INLINE)
d.comment(0xB479, 'Return', align=Align.INLINE)
d.comment(0xB47A, 'Below space?', align=Align.INLINE)
d.comment(0xB47C, 'Yes: invalid channel character', align=Align.INLINE)
d.comment(0xB47E, "Below '0'?", align=Align.INLINE)
d.comment(0xB480, 'In range &20-&2F: look up channel', align=Align.INLINE)
d.comment(0xB482, 'Save channel character', align=Align.INLINE)
d.comment(0xB483, 'Error code &DE', align=Align.INLINE)
d.comment(0xB485, "Generate 'Net channel' error", align=Align.INLINE)
d.comment(0xB494, 'Error string continuation (unreachable)', align=Align.INLINE)
d.comment(0xB4AD, 'Save channel character', align=Align.INLINE)
d.comment(0xB4AE, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB4AF, 'Convert char to table index', align=Align.INLINE)
d.comment(0xB4B1, 'X = channel table index', align=Align.INLINE)
d.comment(0xB4B2, 'Look up network number for channel', align=Align.INLINE)
d.comment(0xB4B5, 'Zero: channel not found, raise error', align=Align.INLINE)
d.comment(0xB4B7, 'Check station/network matches current', align=Align.INLINE)
d.comment(0xB4BA, 'No match: build detailed error msg', align=Align.INLINE)
d.comment(0xB4BC, 'Discard saved channel character', align=Align.INLINE)
d.comment(0xB4BD, 'Load channel status flags', align=Align.INLINE)
d.comment(0xB4C0, 'Return; A = channel flags', align=Align.INLINE)
d.comment(0xB4C1, 'Error code &DE', align=Align.INLINE)
d.comment(0xB4C3, 'Store error code in error block', align=Align.INLINE)
d.comment(0xB4C6, 'BRK opcode', align=Align.INLINE)
d.comment(0xB4C8, 'Store BRK at start of error block', align=Align.INLINE)
d.comment(0xB4CB, 'X=0: copy index', align=Align.INLINE)
d.comment(0xB4CC, 'Advance copy position', align=Align.INLINE)
d.comment(0xB4CD, "Load 'Net channel' string byte", align=Align.INLINE)
d.comment(0xB4D0, 'Copy to error text', align=Align.INLINE)
d.comment(0xB4D3, 'Continue until NUL terminator', align=Align.INLINE)
d.comment(0xB4D5, 'Save end-of-string position', align=Align.INLINE)
d.comment(0xB4D7, 'Save for suffix append', align=Align.INLINE)
d.comment(0xB4D9, 'Retrieve channel character', align=Align.INLINE)
d.comment(0xB4DA, "Append ' N' (channel number)", align=Align.INLINE)
d.comment(0xB4DD, "Load 'Net channel' end position", align=Align.INLINE)
d.comment(0xB4DF, 'Skip past NUL to suffix string', align=Align.INLINE)
d.comment(0xB4E0, 'Advance destination position', align=Align.INLINE)
d.comment(0xB4E1, "Load ' not on this...' suffix byte", align=Align.INLINE)
d.comment(0xB4E4, 'Append to error message', align=Align.INLINE)
d.comment(0xB4E7, 'Continue until NUL', align=Align.INLINE)
d.comment(0xB4E9, 'Raise the constructed error', align=Align.INLINE)
d.comment(0xB4EC, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xB4EF, 'Store channel attribute to RX buffer', align=Align.INLINE)
d.comment(0xB4F2, 'Validate and look up channel', align=Align.INLINE)
d.comment(0xB4F5, 'Test directory flag (bit 1)', align=Align.INLINE)
d.comment(0xB4F7, 'Not a directory: return OK', align=Align.INLINE)
d.comment(0xB4F9, 'Error code &A8', align=Align.INLINE)
d.comment(0xB4FB, "Generate 'Is a dir.' error", align=Align.INLINE)
d.comment(0xB508, 'Return', align=Align.INLINE)
d.comment(0xB509, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB50A, 'Start scanning from FCB slot &20', align=Align.INLINE)
d.comment(0xB50C, 'Load FCB station byte', align=Align.INLINE)
d.comment(0xB50F, 'Zero: slot is free, use it', align=Align.INLINE)
d.comment(0xB511, 'Try next slot', align=Align.INLINE)
d.comment(0xB512, 'Past last FCB slot &2F?', align=Align.INLINE)
d.comment(0xB514, 'No: check next slot', align=Align.INLINE)
d.comment(0xB516, 'No free slot: discard saved attribute', align=Align.INLINE)
d.comment(0xB517, 'A=0: return failure (Z set)', align=Align.INLINE)
d.comment(0xB519, 'Return', align=Align.INLINE)
d.comment(0xB51A, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB51B, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xB51E, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB520, 'Clear FCB transfer count low', align=Align.INLINE)
d.comment(0xB523, 'Clear FCB transfer count mid', align=Align.INLINE)
d.comment(0xB526, 'Clear FCB transfer count high', align=Align.INLINE)
d.comment(0xB529, 'Load current station number', align=Align.INLINE)
d.comment(0xB52C, 'Store station in FCB', align=Align.INLINE)
d.comment(0xB52F, 'Load current network number', align=Align.INLINE)
d.comment(0xB532, 'Store network in FCB', align=Align.INLINE)
d.comment(0xB535, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB536, 'Save slot index', align=Align.INLINE)
d.comment(0xB537, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB538, 'Convert slot to channel index (0-&0F)', align=Align.INLINE)
d.comment(0xB53A, 'X = channel index', align=Align.INLINE)
d.comment(0xB53B, 'Restore A = FCB slot index', align=Align.INLINE)
d.comment(0xB53C, 'Return; A=slot, X=channel, Z clear', align=Align.INLINE)
d.comment(0xB53D, 'Save argument', align=Align.INLINE)
d.comment(0xB53E, 'A=0: allocate any available slot', align=Align.INLINE)
d.comment(0xB540, 'Try to allocate an FCB slot', align=Align.INLINE)
d.comment(0xB543, 'Success: slot allocated', align=Align.INLINE)
d.comment(0xB545, 'Error code &C0', align=Align.INLINE)
d.comment(0xB547, "Generate 'No more FCBs' error", align=Align.INLINE)
d.comment(0xB557, 'Restore argument', align=Align.INLINE)
d.comment(0xB558, 'Return', align=Align.INLINE)
d.comment(0xB559, 'C=0: close all matching channels', align=Align.INLINE)
d.comment(0xB55A, 'Branch always to scan entry', align=Align.INLINE)
d.comment(0xB55A, 'Set V flag via BIT (alternate mode)', align=Align.INLINE)
d.comment(0xB55D, 'Start from FCB slot &10', align=Align.INLINE)
d.comment(0xB55F, 'Previous FCB slot', align=Align.INLINE)
d.comment(0xB560, 'More slots to check', align=Align.INLINE)
d.comment(0xB562, 'All FCB slots processed, return', align=Align.INLINE)
d.comment(0xB563, 'Load channel flags for this slot', align=Align.INLINE)
d.comment(0xB566, 'Save flags in Y', align=Align.INLINE)
d.comment(0xB567, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xB569, 'Not active: check station match', align=Align.INLINE)
d.comment(0xB56B, 'V clear (close all): next slot', align=Align.INLINE)
d.comment(0xB56D, 'C clear: check station match', align=Align.INLINE)
d.comment(0xB56F, 'Restore original flags', align=Align.INLINE)
d.comment(0xB570, 'Clear write-pending flag (bit 5)', align=Align.INLINE)
d.comment(0xB572, 'Update channel flags', align=Align.INLINE)
d.comment(0xB575, 'Next slot (V always set here)', align=Align.INLINE)
d.comment(0xB577, 'Check if channel belongs to station', align=Align.INLINE)
d.comment(0xB57A, 'No match: skip to next slot', align=Align.INLINE)
d.comment(0xB57C, 'A=0: clear channel', align=Align.INLINE)
d.comment(0xB57E, 'Clear channel flags (close it)', align=Align.INLINE)
d.comment(0xB581, 'Clear network number', align=Align.INLINE)
d.comment(0xB584, 'Continue to next slot', align=Align.INLINE)
d.comment(0xB586, 'Load FCB station number', align=Align.INLINE)
d.comment(0xB589, 'Compare with current station (EOR)', align=Align.INLINE)
d.comment(0xB58C, 'Different: Z=0, no match', align=Align.INLINE)
d.comment(0xB58E, 'Load FCB network number', align=Align.INLINE)
d.comment(0xB591, 'Compare with current network (EOR)', align=Align.INLINE)
d.comment(0xB594, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)
d.comment(0xB595, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB598, 'Set V flag (first pass marker)', align=Align.INLINE)
d.comment(0xB59B, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB59C, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xB59E, 'No: continue checking', align=Align.INLINE)
d.comment(0xB5A0, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB5A2, 'Back to starting slot?', align=Align.INLINE)
d.comment(0xB5A5, 'No: check this slot', align=Align.INLINE)
d.comment(0xB5A7, 'V clear (second pass): scan empties', align=Align.INLINE)
d.comment(0xB5A9, 'Clear V for second pass', align=Align.INLINE)
d.comment(0xB5AA, 'Continue scanning', align=Align.INLINE)
d.comment(0xB5AC, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5AF, 'Shift bit 7 (in-use) into carry', align=Align.INLINE)
d.comment(0xB5B0, 'Not in use: skip', align=Align.INLINE)
d.comment(0xB5B2, 'Test bit 2 (modified flag)', align=Align.INLINE)
d.comment(0xB5B4, 'Modified: check further conditions', align=Align.INLINE)
d.comment(0xB5B6, 'Adjust for following INX', align=Align.INLINE)
d.comment(0xB5B7, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB5B8, 'Past end of table?', align=Align.INLINE)
d.comment(0xB5BA, 'No: continue', align=Align.INLINE)
d.comment(0xB5BC, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB5BE, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5C1, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0xB5C2, 'Not in use: continue scanning', align=Align.INLINE)
d.comment(0xB5C4, 'Set carry for ROR restore', align=Align.INLINE)
d.comment(0xB5C5, 'Restore original flags', align=Align.INLINE)
d.comment(0xB5C6, 'Save flags back (mark as found)', align=Align.INLINE)
d.comment(0xB5C9, 'Restore original FCB index', align=Align.INLINE)
d.comment(0xB5CC, 'Return with found slot in X', align=Align.INLINE)
d.comment(0xB5CD, 'V set (first pass): skip modified', align=Align.INLINE)
d.comment(0xB5CF, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5D2, 'Test bit 5 (offset pending)', align=Align.INLINE)
d.comment(0xB5D4, 'Bit 5 set: skip this slot', align=Align.INLINE)
d.comment(0xB5D6, 'Use this slot', align=Align.INLINE)
d.comment(0xB5D8, 'Initial pass count = 1', align=Align.INLINE)
d.comment(0xB5DA, 'Store pass counter', align=Align.INLINE)
d.comment(0xB5DD, 'Y=0', align=Align.INLINE)
d.comment(0xB5DE, 'Clear byte counter low', align=Align.INLINE)
d.comment(0xB5E1, 'Clear offset counter', align=Align.INLINE)
d.comment(0xB5E4, 'Clear transfer flag', align=Align.INLINE)
d.comment(0xB5E7, 'A=0', align=Align.INLINE)
d.comment(0xB5E8, 'Clear 3 counter bytes', align=Align.INLINE)
d.comment(0xB5EA, 'Clear counter byte', align=Align.INLINE)
d.comment(0xB5ED, 'Next byte', align=Align.INLINE)
d.comment(0xB5EE, 'Loop for indices 2, 1, 0', align=Align.INLINE)
d.comment(0xB5F0, 'Store &FF as sentinel in l10cd', align=Align.INLINE)
d.comment(0xB5F3, 'Store &FF as sentinel in l10ce', align=Align.INLINE)
d.comment(0xB5F6, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB5F8, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB5FA, 'Return; X/Y point to &10CA', align=Align.INLINE)
d.comment(0xB5FB, 'Verify workspace checksum integrity', align=Align.INLINE)
d.comment(0xB5FE, 'Save current FCB index', align=Align.INLINE)
d.comment(0xB601, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB604, 'Shift bit 0 (active) into carry', align=Align.INLINE)
d.comment(0xB605, 'Not active: clear status and return', align=Align.INLINE)
d.comment(0xB607, 'Save current station low to stack', align=Align.INLINE)
d.comment(0xB60A, 'Push station low', align=Align.INLINE)
d.comment(0xB60B, 'Save current station high', align=Align.INLINE)
d.comment(0xB60E, 'Push station high', align=Align.INLINE)
d.comment(0xB60F, 'Load FCB station low', align=Align.INLINE)
d.comment(0xB612, 'Set as working station low', align=Align.INLINE)
d.comment(0xB615, 'Load FCB station high', align=Align.INLINE)
d.comment(0xB618, 'Set as working station high', align=Align.INLINE)
d.comment(0xB61B, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xB61E, 'Set offset to &FF (no data yet)', align=Align.INLINE)
d.comment(0xB621, 'Set pass counter to 0 (flush mode)', align=Align.INLINE)
d.comment(0xB624, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB627, 'Transfer to A', align=Align.INLINE)
d.comment(0xB628, 'Prepare addition', align=Align.INLINE)
d.comment(0xB629, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB62B, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xB62E, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB631, 'Test bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xB633, 'No offset: skip restore', align=Align.INLINE)
d.comment(0xB635, 'Load saved byte offset', align=Align.INLINE)
d.comment(0xB638, 'Restore offset counter', align=Align.INLINE)
d.comment(0xB63B, 'Load FCB attribute reference', align=Align.INLINE)
d.comment(0xB63E, 'Store as current reference', align=Align.INLINE)
d.comment(0xB641, 'Transfer to X', align=Align.INLINE)
d.comment(0xB642, 'Read saved receive attribute', align=Align.INLINE)
d.comment(0xB645, 'Push to stack', align=Align.INLINE)
d.comment(0xB646, 'Restore attribute to A', align=Align.INLINE)
d.comment(0xB647, 'Set attribute in receive buffer', align=Align.INLINE)
d.comment(0xB649, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB64B, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB64D, 'A=0: standard transfer mode', align=Align.INLINE)
d.comment(0xB64F, 'Send data and receive response', align=Align.INLINE)
d.comment(0xB652, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB655, 'Restore saved receive attribute', align=Align.INLINE)
d.comment(0xB656, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB659, 'Restore station high', align=Align.INLINE)
d.comment(0xB65A, 'Store station high', align=Align.INLINE)
d.comment(0xB65D, 'Restore station low', align=Align.INLINE)
d.comment(0xB65E, 'Store station low', align=Align.INLINE)
d.comment(0xB661, 'Mask &DC: clear bits 0, 1, 5', align=Align.INLINE)
d.comment(0xB663, 'Clear active and offset flags', align=Align.INLINE)
d.comment(0xB666, 'Update FCB status', align=Align.INLINE)
d.comment(0xB669, 'Return', align=Align.INLINE)
d.comment(0xB66A, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xB66C, 'Load TX buffer byte', align=Align.INLINE)
d.comment(0xB66F, 'Save to context buffer at &10D9', align=Align.INLINE)
d.comment(0xB672, 'Load workspace byte from fs_load_addr', align=Align.INLINE)
d.comment(0xB674, 'Save to stack', align=Align.INLINE)
d.comment(0xB675, 'Next byte down', align=Align.INLINE)
d.comment(0xB676, 'Loop for all 13 bytes', align=Align.INLINE)
d.comment(0xB678, 'Y=0? (no FCB to process)', align=Align.INLINE)
d.comment(0xB67A, 'Non-zero: scan and process FCBs', align=Align.INLINE)
d.comment(0xB67C, 'Y=0: skip to restore workspace', align=Align.INLINE)
d.comment(0xB67F, 'Save flags', align=Align.INLINE)
d.comment(0xB680, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xB682, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB683, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB686, 'Bit 7 clear: not pending, skip', align=Align.INLINE)
d.comment(0xB688, 'Shift bit 6 to bit 7', align=Align.INLINE)
d.comment(0xB689, 'Bit 6 clear: skip', align=Align.INLINE)
d.comment(0xB68B, "Flush this FCB's pending data", align=Align.INLINE)
d.comment(0xB68E, 'Pending marker &40', align=Align.INLINE)
d.comment(0xB690, 'Mark FCB as pending-only', align=Align.INLINE)
d.comment(0xB693, 'Save flags', align=Align.INLINE)
d.comment(0xB694, 'Find next available FCB slot', align=Align.INLINE)
d.comment(0xB697, 'Restore flags', align=Align.INLINE)
d.comment(0xB698, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xB69B, 'Store as current reference', align=Align.INLINE)
d.comment(0xB69E, 'Save attribute', align=Align.INLINE)
d.comment(0xB69F, 'Prepare attribute-to-channel conversion', align=Align.INLINE)
d.comment(0xB6A2, 'Y = attribute index', align=Align.INLINE)
d.comment(0xB6A0, 'Convert attribute (&20+) to channel index', align=Align.INLINE)
d.comment(0xB6A3, 'Load station for this attribute', align=Align.INLINE)
d.comment(0xB6A6, 'Store station in TX buffer', align=Align.INLINE)
d.comment(0xB6A9, 'Restore attribute', align=Align.INLINE)
d.comment(0xB6AA, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xB6AD, 'Load working station low', align=Align.INLINE)
d.comment(0xB6B0, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6B0, 'Store station low in FCB', align=Align.INLINE)
d.comment(0xB6B3, 'Load working station high', align=Align.INLINE)
d.comment(0xB6B6, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6B6, 'Store station high in FCB', align=Align.INLINE)
d.comment(0xB6B9, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB6BA, 'Prepare addition', align=Align.INLINE)
d.comment(0xB6BB, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB6BD, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xB6C0, 'Restore flags', align=Align.INLINE)
d.comment(0xB6C1, 'V clear: skip directory request', align=Align.INLINE)
d.comment(0xB6C3, 'Command byte = 0', align=Align.INLINE)
d.comment(0xB6CC, 'Function code &0D', align=Align.INLINE)
d.comment(0xB6C3, 'Send directory request to server', align=Align.INLINE)
d.comment(0xB6C6, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xB6C9, 'Read saved receive attribute', align=Align.INLINE)
d.comment(0xB6CC, 'Push to stack', align=Align.INLINE)
d.comment(0xB6CD, 'Load current reference', align=Align.INLINE)
d.comment(0xB6D0, 'Set in receive buffer', align=Align.INLINE)
d.comment(0xB6D2, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB6D4, 'A=2: transfer mode 2', align=Align.INLINE)
d.comment(0xB6D6, 'Send and receive data', align=Align.INLINE)
d.comment(0xB6D9, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB6DA, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB6DD, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB6E0, 'Load pass counter', align=Align.INLINE)
d.comment(0xB6E3, 'Non-zero: data received, calc offset', align=Align.INLINE)
d.comment(0xB6E5, 'Load offset counter', align=Align.INLINE)
d.comment(0xB6E8, 'Zero: no data received at all', align=Align.INLINE)
d.comment(0xB6EA, 'Load offset counter', align=Align.INLINE)
d.comment(0xB6ED, 'Negate (ones complement)', align=Align.INLINE)
d.comment(0xB6EF, 'Clear carry for add', align=Align.INLINE)
d.comment(0xB6F0, 'Complete twos complement negation', align=Align.INLINE)
d.comment(0xB6F2, 'Store negated offset in FCB', align=Align.INLINE)
d.comment(0xB6F5, 'Set bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xB6F7, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xB6FA, 'Update FCB status', align=Align.INLINE)
d.comment(0xB6FD, 'Load buffer address high byte', align=Align.INLINE)
d.comment(0xB700, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB702, 'A=0: pointer low byte and clear val', align=Align.INLINE)
d.comment(0xB704, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB706, 'Load negated offset (start of clear)', align=Align.INLINE)
d.comment(0xB709, 'Clear buffer byte', align=Align.INLINE)
d.comment(0xB70B, 'Next byte', align=Align.INLINE)
d.comment(0xB70C, 'Loop until page boundary', align=Align.INLINE)
d.comment(0xB70E, 'Set bit 1 (active flag)', align=Align.INLINE)
d.comment(0xB710, 'Add active flag to status', align=Align.INLINE)
d.comment(0xB713, 'Update FCB status', align=Align.INLINE)
d.comment(0xB716, 'Y=0: start restoring workspace', align=Align.INLINE)
d.comment(0xB718, 'Restore workspace byte from stack', align=Align.INLINE)
d.comment(0xB719, 'Store to fs_load_addr workspace', align=Align.INLINE)
d.comment(0xB71C, 'Next byte', align=Align.INLINE)
d.comment(0xB71D, 'Restored all 13 bytes?', align=Align.INLINE)
d.comment(0xB71F, 'No: continue restoring', align=Align.INLINE)
d.comment(0xB721, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xB723, 'Load saved catalog byte from &10D9', align=Align.INLINE)
d.comment(0xB726, 'Restore to TX buffer', align=Align.INLINE)
d.comment(0xB729, 'Next byte down', align=Align.INLINE)
d.comment(0xB72A, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xB72C, 'Return', align=Align.INLINE)
d.comment(0xB72D, 'Save current context first', align=Align.INLINE)
d.comment(0xB730, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xB732, 'Load channel attribute to match', align=Align.INLINE)
d.comment(0xB735, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB736, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xB738, 'No: check this slot', align=Align.INLINE)
d.comment(0xB73A, 'Load channel attribute', align=Align.INLINE)
d.comment(0xB73D, 'Convert to channel index', align=Align.INLINE)
d.comment(0xB740, 'Load station for this channel', align=Align.INLINE)
d.comment(0xB743, 'Store as match target station high', align=Align.INLINE)
d.comment(0xB746, 'Load port for this channel', align=Align.INLINE)
d.comment(0xB749, 'Store as match target station low', align=Align.INLINE)
d.comment(0xB74C, 'Save context and rescan from start', align=Align.INLINE)
d.comment(0xB74F, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB752, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xB754, 'Not active: skip to next', align=Align.INLINE)
d.comment(0xB756, 'Get attribute to match', align=Align.INLINE)
d.comment(0xB757, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xB75A, 'No attribute match: skip', align=Align.INLINE)
d.comment(0xB75C, 'Save matching FCB index', align=Align.INLINE)
d.comment(0xB75F, 'Save flags from attribute compare', align=Align.INLINE)
d.comment(0xB760, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB761, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0xB763, 'Restore flags from attribute compare', align=Align.INLINE)
d.comment(0xB764, 'Y = channel index', align=Align.INLINE)
d.comment(0xB765, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB768, 'Load channel station byte', align=Align.INLINE)
d.comment(0xB76B, 'Compare with FCB station', align=Align.INLINE)
d.comment(0xB76E, 'Station mismatch: try next', align=Align.INLINE)
d.comment(0xB770, 'Load channel network byte', align=Align.INLINE)
d.comment(0xB773, 'Compare with FCB network', align=Align.INLINE)
d.comment(0xB776, 'Network mismatch: try next', align=Align.INLINE)
d.comment(0xB778, 'Load FCB flags', align=Align.INLINE)
d.comment(0xB77B, 'Bit 7 clear: no pending flush', align=Align.INLINE)
d.comment(0xB77D, 'Clear pending flag (bit 7)', align=Align.INLINE)
d.comment(0xB77F, 'Update FCB status', align=Align.INLINE)
d.comment(0xB782, 'Find new open FCB slot', align=Align.INLINE)
d.comment(0xB785, 'Reload FCB flags', align=Align.INLINE)
d.comment(0xB788, 'Test bit 5 (has offset data)', align=Align.INLINE)
d.comment(0xB78A, 'Return; Z=1 no offset, Z=0 has data', align=Align.INLINE)
d.comment(0xB78B, 'Increment byte count low', align=Align.INLINE)
d.comment(0xB78E, 'No overflow: done', align=Align.INLINE)
d.comment(0xB790, 'Increment byte count mid', align=Align.INLINE)
d.comment(0xB793, 'No overflow: done', align=Align.INLINE)
d.comment(0xB795, 'Increment byte count high', align=Align.INLINE)
d.comment(0xB798, 'Return', align=Align.INLINE)
d.comment(0xB799, 'Save X', align=Align.INLINE)
d.comment(0xB79A, 'Push X to stack', align=Align.INLINE)
d.comment(0xB79B, 'Save Y', align=Align.INLINE)
d.comment(0xB79C, 'Push Y to stack', align=Align.INLINE)
d.comment(0xB79D, 'X=&F7: save 9 workspace bytes (&F7..&FF)', align=Align.INLINE)
d.comment(0xB7A2, 'Push fs_options', align=Align.INLINE)
d.comment(0xB7A3, 'Next byte', align=Align.INLINE)
d.comment(0xB79F, 'Load workspace byte', align=Align.INLINE)
d.comment(0xB7A6, 'Start from FCB slot &0F', align=Align.INLINE)
d.comment(0xB7A4, 'X<0: more bytes to save', align=Align.INLINE)
d.comment(0xB7A8, 'Store as current FCB index', align=Align.INLINE)
d.comment(0xB7AB, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB7AE, 'Get filter attribute', align=Align.INLINE)
d.comment(0xB7AF, 'Zero: process all FCBs', align=Align.INLINE)
d.comment(0xB7B1, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xB7B4, 'No match: skip this FCB', align=Align.INLINE)
d.comment(0xB7B6, 'Save filter attribute', align=Align.INLINE)
d.comment(0xB7B7, 'Flush pending data for this FCB', align=Align.INLINE)
d.comment(0xB7BA, 'Restore filter', align=Align.INLINE)
d.comment(0xB7BB, 'Y = filter attribute', align=Align.INLINE)
d.comment(0xB7BC, 'Previous FCB index', align=Align.INLINE)
d.comment(0xB7BF, 'More slots: continue loop', align=Align.INLINE)
d.comment(0xB7C1, 'X=8: restore 9 workspace bytes', align=Align.INLINE)
d.comment(0xB7C3, 'Restore fs_block_offset', align=Align.INLINE)
d.comment(0xB7C4, 'Restore workspace byte', align=Align.INLINE)
d.comment(0xB7C9, 'Restore Y', align=Align.INLINE)
d.comment(0xB7C6, 'Next byte down', align=Align.INLINE)
d.comment(0xB7CA, 'Y restored', align=Align.INLINE)
d.comment(0xB7C7, 'More bytes: continue restoring', align=Align.INLINE)
d.comment(0xB7CB, 'Restore X', align=Align.INLINE)
d.comment(0xB7CC, 'X restored', align=Align.INLINE)
d.comment(0xB7CD, 'Return', align=Align.INLINE)
d.comment(0xB7CE, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB7D1, "Save caller's X", align=Align.INLINE)
d.comment(0xB7D2, 'Push X', align=Align.INLINE)
d.comment(0xB7D3, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xB7D6, 'Load channel flags', align=Align.INLINE)
d.comment(0xB7D9, 'Test write-only flag (bit 5)', align=Align.INLINE)
d.comment(0xB7DB, 'Not write-only: proceed with read', align=Align.INLINE)
d.comment(0xB7DD, 'Error code &D4', align=Align.INLINE)
d.comment(0xB7DF, "Generate 'Write only' error", align=Align.INLINE)
d.comment(0xB7ED, 'Clear V (first-pass matching)', align=Align.INLINE)
d.comment(0xB7EE, 'Find FCB matching this channel', align=Align.INLINE)
d.comment(0xB7F1, 'No offset: read byte from buffer', align=Align.INLINE)
d.comment(0xB7F3, 'Load byte count for matching FCB', align=Align.INLINE)
d.comment(0xB7F6, 'Compare with buffer offset limit', align=Align.INLINE)
d.comment(0xB7F9, 'Below offset: data available', align=Align.INLINE)
d.comment(0xB7FB, 'Load channel flags for FCB', align=Align.INLINE)
d.comment(0xB7FE, 'Transfer to X for testing', align=Align.INLINE)
d.comment(0xB7FF, 'Test bit 6 (EOF already signalled)', align=Align.INLINE)
d.comment(0xB801, 'EOF already set: raise error', align=Align.INLINE)
d.comment(0xB803, 'Restore flags', align=Align.INLINE)
d.comment(0xB804, 'Set EOF flag (bit 6)', align=Align.INLINE)
d.comment(0xB806, 'Update channel flags with EOF', align=Align.INLINE)
d.comment(0xB809, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB80B, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xB80E, "Restore caller's X", align=Align.INLINE)
d.comment(0xB80F, 'X restored', align=Align.INLINE)
d.comment(0xB810, 'A=&FE: EOF marker byte', align=Align.INLINE)
d.comment(0xB812, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB815, 'C=1: end of file', align=Align.INLINE)
d.comment(0xB816, 'Return', align=Align.INLINE)
d.comment(0xB817, 'Error code &DF', align=Align.INLINE)
d.comment(0xB819, "Generate 'End of file' error", align=Align.INLINE)
d.comment(0xB828, 'Load current byte count (= offset)', align=Align.INLINE)
d.comment(0xB82B, 'Save byte count', align=Align.INLINE)
d.comment(0xB82C, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB82D, 'X = FCB slot for byte count inc', align=Align.INLINE)
d.comment(0xB82E, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB830, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xB833, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xB836, 'Restore byte count (= buffer offset)', align=Align.INLINE)
d.comment(0xB837, 'Y = offset into data buffer', align=Align.INLINE)
d.comment(0xB838, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB83B, 'Prepare addition', align=Align.INLINE)
d.comment(0xB83C, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB83E, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB840, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xB842, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB844, "Restore caller's X", align=Align.INLINE)
d.comment(0xB845, 'X restored', align=Align.INLINE)
d.comment(0xB846, 'Read data byte from buffer', align=Align.INLINE)
d.comment(0xB848, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB84B, 'C=0: byte read successfully', align=Align.INLINE)
d.comment(0xB84C, 'Return; A = data byte', align=Align.INLINE)
d.comment(0xB84D, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB850, 'Save data byte', align=Align.INLINE)
d.comment(0xB851, 'Y = data byte', align=Align.INLINE)
d.comment(0xB852, "Save caller's X", align=Align.INLINE)
d.comment(0xB853, 'Push X', align=Align.INLINE)
d.comment(0xB854, 'Restore data byte to A', align=Align.INLINE)
d.comment(0xB855, 'Push data byte for later', align=Align.INLINE)
d.comment(0xB856, 'Save data byte in workspace', align=Align.INLINE)
d.comment(0xB859, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xB85C, 'Load channel flags', align=Align.INLINE)
d.comment(0xB85F, 'Bit 7 set: channel open, proceed', align=Align.INLINE)
d.comment(0xB861, 'Error &C1: Not open for update', align=Align.INLINE)
d.comment(0xB863, 'Raise error with inline string', align=Align.INLINE)
d.comment(0xB87A, 'Test write flag (bit 5)', align=Align.INLINE)
d.comment(0xB87C, 'Not write-capable: use buffer path', align=Align.INLINE)
d.comment(0xB87E, 'Load reply port for this channel', align=Align.INLINE)
d.comment(0xB881, 'Restore data byte', align=Align.INLINE)
d.comment(0xB882, 'Send byte directly to server', align=Align.INLINE)
d.comment(0xB885, 'Update byte count and return', align=Align.INLINE)
d.comment(0xB888, 'Set V flag (alternate match mode)', align=Align.INLINE)
d.comment(0xB88B, 'Find matching FCB for channel', align=Align.INLINE)
d.comment(0xB88E, 'Load byte count for FCB', align=Align.INLINE)
d.comment(0xB891, 'Buffer full (&FF bytes)?', align=Align.INLINE)
d.comment(0xB893, 'No: store byte in buffer', align=Align.INLINE)
d.comment(0xB895, 'Save X', align=Align.INLINE)
d.comment(0xB898, 'Push Y', align=Align.INLINE)
d.comment(0xB89D, 'Carry set from BCS/BCC above', align=Align.INLINE)
d.comment(0xB895, 'Save context and flush FCB data', align=Align.INLINE)
d.comment(0xB898, 'Compare count with buffer offset', align=Align.INLINE)
d.comment(0xB89B, 'Below offset: skip offset update', align=Align.INLINE)
d.comment(0xB89D, 'Add carry (count + 1)', align=Align.INLINE)
d.comment(0xB89F, 'Update buffer offset in FCB', align=Align.INLINE)
d.comment(0xB8A2, 'Non-zero: keep offset flag', align=Align.INLINE)
d.comment(0xB8A4, 'Mask &DF: clear bit 5', align=Align.INLINE)
d.comment(0xB8A6, 'Clear offset flag', align=Align.INLINE)
d.comment(0xB8A9, 'Update FCB status', align=Align.INLINE)
d.comment(0xB8AC, 'Set bit 0 (dirty/active)', align=Align.INLINE)
d.comment(0xB8AE, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xB8B1, 'Update FCB status', align=Align.INLINE)
d.comment(0xB8B4, 'Load byte count (= write position)', align=Align.INLINE)
d.comment(0xB8B7, 'Save count', align=Align.INLINE)
d.comment(0xB8B8, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB8B9, 'X = FCB slot', align=Align.INLINE)
d.comment(0xB8BA, 'Restore byte count', align=Align.INLINE)
d.comment(0xB8BB, 'Y = buffer write offset', align=Align.INLINE)
d.comment(0xB8BC, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB8BF, 'Prepare addition', align=Align.INLINE)
d.comment(0xB8C0, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB8C2, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB8C4, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xB8C6, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB8C8, 'Restore data byte', align=Align.INLINE)
d.comment(0xB8C9, 'Write data byte to buffer', align=Align.INLINE)
d.comment(0xB8CB, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xB8CE, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB8D0, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0xB8D3, "Restore caller's X", align=Align.INLINE)
d.comment(0xB8D4, 'X restored', align=Align.INLINE)
d.comment(0xB8D5, 'Discard saved data byte', align=Align.INLINE)
d.comment(0xB8D6, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB8D9, 'Return', align=Align.INLINE)
d.comment(0xB92A, 'Return', align=Align.INLINE)
d.comment(0xB8DA, 'Save A', align=Align.INLINE)
d.comment(0xB8DB, 'Transfer X to A', align=Align.INLINE)
d.comment(0xB8DC, 'Save X', align=Align.INLINE)
d.comment(0xB92B, 'Store reply port', align=Align.INLINE)
d.comment(0xB8DD, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xB92E, 'Store data byte', align=Align.INLINE)
d.comment(0xB8DE, 'Save Y (channel index)', align=Align.INLINE)
d.comment(0xB931, 'Save Y', align=Align.INLINE)
d.comment(0xB8DF, 'Load station for this channel', align=Align.INLINE)
d.comment(0xB932, 'Push Y to stack', align=Align.INLINE)
d.comment(0xB8E2, 'Non-zero: station known, skip init', align=Align.INLINE)
d.comment(0xB933, 'Save X', align=Align.INLINE)
d.comment(0xB8E4, 'Save A', align=Align.INLINE)
d.comment(0xB934, 'Push X to stack', align=Align.INLINE)
d.comment(0xB8E5, 'Transfer X to A', align=Align.INLINE)
d.comment(0xB935, 'Function code &90', align=Align.INLINE)
d.comment(0xB8E6, 'Save X', align=Align.INLINE)
d.comment(0xB937, 'Store in send buffer', align=Align.INLINE)
d.comment(0xB8E7, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xB93A, 'Initialise TX control block', align=Align.INLINE)
d.comment(0xB8E8, 'Save Y (channel index)', align=Align.INLINE)
d.comment(0xB93D, 'TX start address low = &DC', align=Align.INLINE)
d.comment(0xB8E9, 'Load station for this channel', align=Align.INLINE)
d.comment(0xB93F, 'Set TX start in control block', align=Align.INLINE)
d.comment(0xB8EC, 'Save station on stack', align=Align.INLINE)
d.comment(0xB941, 'TX end address low = &E0', align=Align.INLINE)
d.comment(0xB8ED, 'Y=0: reset index', align=Align.INLINE)
d.comment(0xB943, 'Set TX end in control block', align=Align.INLINE)
d.comment(0xB8EF, 'Save current FCB context', align=Align.INLINE)
d.comment(0xB945, 'Expected reply port = 9', align=Align.INLINE)
d.comment(0xB8F2, 'Restore station from stack', align=Align.INLINE)
d.comment(0xB947, 'Store reply port in buffer', align=Align.INLINE)
d.comment(0xB8F3, 'Store station in command buffer', align=Align.INLINE)
d.comment(0xB94A, 'TX control = &C0', align=Align.INLINE)
d.comment(0xB8F6, 'X=station number', align=Align.INLINE)
d.comment(0xB94C, 'Y=0: no timeout', align=Align.INLINE)
d.comment(0xB8F7, 'Restore Y from stack', align=Align.INLINE)
d.comment(0xB94E, 'Load reply port for addressing', align=Align.INLINE)
d.comment(0xB8F8, 'Y=channel index', align=Align.INLINE)
d.comment(0xB951, 'Send packet to server', align=Align.INLINE)
d.comment(0xB8F9, 'Re-save Y on stack', align=Align.INLINE)
d.comment(0xB954, 'Load reply status', align=Align.INLINE)
d.comment(0xB8FA, 'A=station number', align=Align.INLINE)
d.comment(0xB957, 'Zero: success', align=Align.INLINE)
d.comment(0xB8FB, 'Save station for later restore', align=Align.INLINE)
d.comment(0xB8FC, 'X=0', align=Align.INLINE)
d.comment(0xB8FE, 'Clear function code', align=Align.INLINE)
d.comment(0xB959, 'Store error code', align=Align.INLINE)
d.comment(0xB901, 'Load byte count lo from FCB', align=Align.INLINE)
d.comment(0xB95C, 'X=0: copy index', align=Align.INLINE)
d.comment(0xB904, 'Store as data byte count', align=Align.INLINE)
d.comment(0xB95E, 'Load error message byte', align=Align.INLINE)
d.comment(0xB907, 'Load byte count mid from FCB', align=Align.INLINE)
d.comment(0xB961, 'Copy to error block', align=Align.INLINE)
d.comment(0xB90A, 'Store as reply command byte', align=Align.INLINE)
d.comment(0xB964, 'Is it CR (end of message)?', align=Align.INLINE)
d.comment(0xB90D, 'Load byte count hi from FCB', align=Align.INLINE)
d.comment(0xB966, 'Yes: terminate string', align=Align.INLINE)
d.comment(0xB910, 'Store as load vector field', align=Align.INLINE)
d.comment(0xB968, 'Next byte', align=Align.INLINE)
d.comment(0xB913, 'Y=&0D: TX command byte offset', align=Align.INLINE)
d.comment(0xB969, 'Continue copying error message', align=Align.INLINE)
d.comment(0xB915, 'X=5: send 5 bytes', align=Align.INLINE)
d.comment(0xB96B, 'NUL terminator', align=Align.INLINE)
d.comment(0xB917, 'Send flush request to server', align=Align.INLINE)
d.comment(0xB96D, 'Terminate error string in block', align=Align.INLINE)
d.comment(0xB91A, 'Restore station from stack', align=Align.INLINE)
d.comment(0xB970, 'Back up position for error check', align=Align.INLINE)
d.comment(0xB91B, 'Y=station for wipe request', align=Align.INLINE)
d.comment(0xB971, 'Process and raise network error', align=Align.INLINE)
d.comment(0xB91C, 'Load saved data byte', align=Align.INLINE)
d.comment(0xB91F, 'Send close/wipe request to server', align=Align.INLINE)
d.comment(0xB922, 'Restore catalog state after flush', align=Align.INLINE)
d.comment(0xB974, 'Load channel attribute index', align=Align.INLINE)
d.comment(0xB925, 'Restore Y', align=Align.INLINE)
d.comment(0xB977, 'Load station number for channel', align=Align.INLINE)
d.comment(0xB926, 'Y restored', align=Align.INLINE)
d.comment(0xB97A, 'Toggle bit 0 (alternate station)', align=Align.INLINE)
d.comment(0xB927, 'Restore X', align=Align.INLINE)
d.comment(0xB97C, 'Update station number', align=Align.INLINE)
d.comment(0xB928, 'X restored', align=Align.INLINE)
d.comment(0xB97F, 'Restore X', align=Align.INLINE)
d.comment(0xB929, 'Restore A', align=Align.INLINE)
d.comment(0xB980, 'X restored', align=Align.INLINE)
d.comment(0xB981, 'Restore Y', align=Align.INLINE)
d.comment(0xB982, 'Y restored', align=Align.INLINE)
d.comment(0xB983, 'Return', align=Align.INLINE)
d.comment(0xB984, 'Set up FS options pointer', align=Align.INLINE)
d.comment(0xB987, 'Set up transfer workspace and return', align=Align.INLINE)
d.comment(0xB98A, 'Y=&0A: receive attribute offset', align=Align.INLINE)
d.comment(0xB98C, 'Read byte from receive buffer', align=Align.INLINE)
d.comment(0x96D6, 'Store return address low', align=Align.INLINE)
d.comment(0x96D9, 'Store return address high', align=Align.INLINE)
d.comment(0x96DB, 'X=0: error text index', align=Align.INLINE)
d.comment(0x96E0, 'Copy error number to A', align=Align.INLINE)
d.comment(0x96E1, 'Push error number on stack', align=Align.INLINE)
d.comment(0x96E2, 'Y=0: inline string index', align=Align.INLINE)
d.comment(0x96E8, 'Advance string index', align=Align.INLINE)
d.comment(0x96EB, 'Store byte in error block', align=Align.INLINE)
d.comment(0xB98E, 'Return', align=Align.INLINE)
d.comment(0xB98F, 'Y=&0A: receive attribute offset', align=Align.INLINE)
d.comment(0x96F3, 'Non-zero: network returned an error', align=Align.INLINE)
d.comment(0x96F5, 'Pop saved error number', align=Align.INLINE)
d.comment(0x96F6, 'Was it &DE (file server error)?', align=Align.INLINE)
d.comment(0x96F8, 'Yes: append error number and trigger BRK', align=Align.INLINE)
d.comment(0x96FA, 'Jump to BRK via error block', align=Align.INLINE)
d.comment(0x96FD, 'Store error code in workspace', align=Align.INLINE)
d.comment(0x9700, 'Push error code', align=Align.INLINE)
d.comment(0x9701, 'Save X (error text index)', align=Align.INLINE)
d.comment(0x9702, 'Push X', align=Align.INLINE)
d.comment(0x9703, 'Read receive attribute byte', align=Align.INLINE)
d.comment(0x9706, 'Save to fs_load_addr as spool handle', align=Align.INLINE)
d.comment(0x9708, 'A=0: clear error code in RX buffer', align=Align.INLINE)
d.comment(0x970A, 'Zero the error code byte in buffer', align=Align.INLINE)
d.comment(0x970C, 'A=&C6: OSBYTE read spool handle', align=Align.INLINE)
d.comment(0x970E, 'Read current spool file handle', align=Align.INLINE)
d.comment(0x9711, 'Compare Y result with saved handle', align=Align.INLINE)
d.comment(0x9713, 'Match: close the spool file', align=Align.INLINE)
d.comment(0x9715, 'Compare X result with saved handle', align=Align.INLINE)
d.comment(0x9717, 'No match: skip spool close', align=Align.INLINE)
d.comment(0x9719, 'Push A (preserved)', align=Align.INLINE)
d.comment(0x971A, 'A=&C6: disable spool with OSBYTE', align=Align.INLINE)
d.comment(0x971C, 'ALWAYS branch to close spool', align=Align.INLINE)
d.comment(0x971E, 'Transfer Y to A for stack save', align=Align.INLINE)
d.comment(0x971F, 'Push A (preserved)', align=Align.INLINE)
d.comment(0x9720, 'A=&C7: disable exec with OSBYTE', align=Align.INLINE)
d.comment(0x9722, 'OSBYTE with X=0, Y=0 to close', align=Align.INLINE)
d.comment(0x9725, 'Pull saved handle', align=Align.INLINE)
d.comment(0x9726, 'Transfer to Y for OSFIND', align=Align.INLINE)
d.comment(0x9727, 'A=0: close file', align=Align.INLINE)
d.comment(0x9729, 'Close the spool/exec file', align=Align.INLINE)
d.comment(0x972C, 'Pull saved X (error text index)', align=Align.INLINE)
d.comment(0x972D, 'Restore X', align=Align.INLINE)
d.comment(0x972E, "Y=&0A: lookup index for 'on channel'", align=Align.INLINE)
d.comment(0x9730, 'Load message offset from lookup table', align=Align.INLINE)
d.comment(0x9733, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x9734, 'Load error message byte', align=Align.INLINE)
d.comment(0x9737, 'Append to error text buffer', align=Align.INLINE)
d.comment(0x973A, 'Null terminator: done copying', align=Align.INLINE)
d.comment(0x973C, 'Advance error text index', align=Align.INLINE)
d.comment(0x973D, 'Advance message index', align=Align.INLINE)
d.comment(0x973E, 'Loop until full message copied', align=Align.INLINE)
d.comment(0x9740, 'Save error text end position', align=Align.INLINE)
d.comment(0x9742, 'Pull saved error number', align=Align.INLINE)
d.comment(0x9743, "Append ' nnn' error number suffix", align=Align.INLINE)
d.comment(0x9746, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x9748, 'Terminate error text string', align=Align.INLINE)
d.comment(0x974B, 'ALWAYS branch to trigger BRK error', align=Align.INLINE)
d.comment(0xB991, 'Store byte to receive buffer', align=Align.INLINE)
d.comment(0xB993, 'Return', align=Align.INLINE)
d.comment(0x974D, "A=' ': space separator", align=Align.INLINE)
d.comment(0x974F, 'Append space to error text', align=Align.INLINE)
d.comment(0x9752, 'Advance error text index', align=Align.INLINE)
d.comment(0x9753, 'Save position for number formatting', align=Align.INLINE)
d.comment(0x9755, 'Y=3: offset to network number in TX CB', align=Align.INLINE)
d.comment(0x9757, 'Load network number', align=Align.INLINE)
d.comment(0x9759, 'Zero: skip network part (local)', align=Align.INLINE)
d.comment(0x975B, 'Append network number as decimal', align=Align.INLINE)
d.comment(0x975E, 'Reload error text position', align=Align.INLINE)
d.comment(0x9760, "A='.': dot separator", align=Align.INLINE)
d.comment(0x9762, 'Append dot to error text', align=Align.INLINE)
d.comment(0x9765, 'Advance past dot', align=Align.INLINE)
d.comment(0x9767, 'Y=2: offset to station number in TX CB', align=Align.INLINE)
d.comment(0x9769, 'Load station number', align=Align.INLINE)
d.comment(0x976B, 'Append station number as decimal', align=Align.INLINE)
d.comment(0x976E, 'Reload error text position', align=Align.INLINE)
d.comment(0x9770, 'Return', align=Align.INLINE)
d.comment(0x9771, 'Save number in Y', align=Align.INLINE)
d.comment(0x9772, "A=' ': space prefix", align=Align.INLINE)
d.comment(0x9774, 'Load current error text position', align=Align.INLINE)
d.comment(0x9776, 'Append space to error text', align=Align.INLINE)
d.comment(0x9779, 'Advance position past space', align=Align.INLINE)
d.comment(0x977B, 'Restore number to A', align=Align.INLINE)
d.comment(0x977C, 'Save number in Y for division', align=Align.INLINE)
d.comment(0x977D, 'Set V: suppress leading zeros', align=Align.INLINE)
d.comment(0x9780, 'A=100: hundreds digit divisor', align=Align.INLINE)
d.comment(0x9782, 'Extract and append hundreds digit', align=Align.INLINE)
d.comment(0x9785, 'A=10: tens digit divisor', align=Align.INLINE)
d.comment(0x9787, 'Extract and append tens digit', align=Align.INLINE)
d.comment(0x978A, 'A=1: units digit (remainder)', align=Align.INLINE)
d.comment(0x978C, 'Clear V: always print units digit', align=Align.INLINE)
d.comment(0x978D, 'Store divisor', align=Align.INLINE)
d.comment(0x978F, 'Copy number to A for division', align=Align.INLINE)
d.comment(0x9790, "X='0'-1: digit counter (ASCII offset)", align=Align.INLINE)
d.comment(0x9792, 'Save V flag (leading zero suppression)', align=Align.INLINE)
d.comment(0x9793, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9794, 'Increment digit counter', align=Align.INLINE)
d.comment(0x9795, 'Subtract divisor', align=Align.INLINE)
d.comment(0x9797, 'Not negative yet: continue counting', align=Align.INLINE)
d.comment(0x9799, 'Add back divisor (restore remainder)', align=Align.INLINE)
d.comment(0x979B, 'Restore V flag', align=Align.INLINE)
d.comment(0x979C, 'Save remainder back to Y', align=Align.INLINE)
d.comment(0x979D, 'Digit counter to A (ASCII digit)', align=Align.INLINE)
d.comment(0x979E, "Is digit '0'?", align=Align.INLINE)
d.comment(0x97A0, 'Non-zero: always print', align=Align.INLINE)
d.comment(0x97A2, 'V set (suppress leading zeros): skip', align=Align.INLINE)
d.comment(0x97A4, 'Clear V: first non-zero digit seen', align=Align.INLINE)
d.comment(0x97A5, 'Load current text position', align=Align.INLINE)
d.comment(0x97A7, 'Store ASCII digit in error text', align=Align.INLINE)
d.comment(0x97AA, 'Advance text position', align=Align.INLINE)
d.comment(0x97AC, 'Return', align=Align.INLINE)
d.comment(0x97AD, """Network error lookup table (12 bytes)

Each byte is an offset into error_msg_table.
Indices 0-7 are keyed by error class (reply AND 7).
Index 8 is used by build_no_reply_error.
Indices 9-11 point to suffix strings appended
after the station address in compound errors.""")
d.comment(0x97AD, 'Class 0: &A0 "Line jammed"', align=Align.INLINE)
d.comment(0x97AE, 'Class 1: &A1 "Net error"', align=Align.INLINE)
d.comment(0x97AF, 'Class 2: &A2 "Station"', align=Align.INLINE)
d.comment(0x97B0, 'Class 3: &A3 "No clock"', align=Align.INLINE)
d.comment(0x97B1, 'Class 4: &11 "Escape"', align=Align.INLINE)
d.comment(0x97B2, 'Class 5: &11 "Escape" (duplicate)', align=Align.INLINE)
d.comment(0x97B3, 'Class 6: &11 "Escape" (duplicate)', align=Align.INLINE)
d.comment(0x97B4, 'Class 7: &CB "Bad option"', align=Align.INLINE)
d.comment(0x97B5, 'Index 8: &A5 "No reply from station"', align=Align.INLINE)
d.comment(0x97B6, 'Index 9: " not listening" suffix', align=Align.INLINE)
d.comment(0x97B7, 'Index 10: " on channel" suffix', align=Align.INLINE)
d.comment(0x97B8, 'Index 11: " not present" suffix', align=Align.INLINE)
d.comment(0x97B9, """Network error message table

Each entry is [error_number][string...][null].
The error number is the BRK error code stored in
the error block at &0100. Entries 0-6 are complete
error messages. The last 3 are suffix strings
(no error number) appended to class 2 "Station"
errors to form compound messages like
"Station 1.254 not listening".""")
d.comment(0x97B9, 'Error &A0: Line jammed', align=Align.INLINE)
d.comment(0x97C5, 'Null terminator', align=Align.INLINE)
d.comment(0x97C6, 'Error &A1: Net error', align=Align.INLINE)
d.comment(0x97D0, 'Null terminator', align=Align.INLINE)
d.comment(0x97D1, 'Error &A2: Station', align=Align.INLINE)
d.comment(0x97D9, 'Null terminator', align=Align.INLINE)
d.comment(0x97DA, 'Error &A3: No clock', align=Align.INLINE)
d.comment(0x97E3, 'Null terminator', align=Align.INLINE)
d.comment(0x97E4, 'Error &11: Escape', align=Align.INLINE)
d.comment(0x97EB, 'Null terminator', align=Align.INLINE)
d.comment(0x97EC, 'Error &CB: Bad option', align=Align.INLINE)
d.comment(0x97F7, 'Null terminator', align=Align.INLINE)
d.comment(0x97F8, 'Error &A5: No reply from station', align=Align.INLINE)
d.comment(0x980E, 'Null terminator', align=Align.INLINE)
d.comment(0x980F, 'Suffix: " not listening"', align=Align.INLINE)
d.comment(0x981D, 'Null terminator', align=Align.INLINE)
d.comment(0x981E, 'Suffix: " on channel"', align=Align.INLINE)
d.comment(0x9829, 'Null terminator', align=Align.INLINE)
d.comment(0x982A, 'Suffix: " not present"', align=Align.INLINE)
d.comment(0x9836, 'Null terminator', align=Align.INLINE)
d.comment(0x9837, 'X=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9839, 'Set TX pointer low', align=Align.INLINE)
d.comment(0x983B, 'X=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x983D, 'Set TX pointer high (page 0)', align=Align.INLINE)
d.comment(0x983F, 'Load retry count from workspace', align=Align.INLINE)
d.comment(0x9842, 'Non-zero: use configured retry count', align=Align.INLINE)
d.comment(0x9844, 'A=&FF: default retry count (255)', align=Align.INLINE)
d.comment(0x9846, 'Y=&60: timeout value', align=Align.INLINE)
d.comment(0x9848, 'Push retry count', align=Align.INLINE)
d.comment(0x9849, 'A=&60: copy timeout to A', align=Align.INLINE)
d.comment(0x984A, 'Push timeout', align=Align.INLINE)
d.comment(0x984B, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x984D, 'Load first byte of TX control block', align=Align.INLINE)
d.comment(0x984F, 'Restore control byte (overwritten by result code on retry)', align=Align.INLINE)
d.comment(0x9851, 'Push control byte', align=Align.INLINE)
d.comment(0x9852, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x9855, 'ASL: bit 6 (error flag) into N', align=Align.INLINE)
d.comment(0x9856, 'N=0 (bit 6 clear): success', align=Align.INLINE)
d.comment(0x9858, 'ASL: shift away error flag, keep error type', align=Align.INLINE)
d.comment(0x9859, 'Z=1 (no type bits): fatal; Z=0: retryable', align=Align.INLINE)
d.comment(0x985B, 'Check for escape condition', align=Align.INLINE)
d.comment(0x985E, 'Pull control byte', align=Align.INLINE)
d.comment(0x985F, 'Restore to X', align=Align.INLINE)
d.comment(0x9860, 'Pull timeout', align=Align.INLINE)
d.comment(0x9861, 'Restore to Y', align=Align.INLINE)
d.comment(0x9862, 'Pull retry count', align=Align.INLINE)
d.comment(0x9863, 'Zero retries remaining: try alternate', align=Align.INLINE)
d.comment(0x9865, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x9867, 'Push updated retry count', align=Align.INLINE)
d.comment(0x9868, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x9869, 'Push timeout for delay loop', align=Align.INLINE)
d.comment(0x986A, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x986B, 'Inner delay: decrement X', align=Align.INLINE)
d.comment(0x986C, 'Loop until X=0', align=Align.INLINE)
d.comment(0x986E, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x986F, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x9871, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x9873, 'Compare retry count with alternate', align=Align.INLINE)
d.comment(0x9876, 'Different: go to error handling', align=Align.INLINE)
d.comment(0x9878, 'A=&80: set escapable flag', align=Align.INLINE)
d.comment(0x987A, 'Mark as escapable for second phase', align=Align.INLINE)
d.comment(0x987C, 'ALWAYS branch: retry with escapable', align=Align.INLINE)
d.comment(0x987E, 'Result code to X', align=Align.INLINE)
d.comment(0x987F, 'Jump to classify reply and return', align=Align.INLINE)
d.comment(0x9882, 'Pull control byte', align=Align.INLINE)
d.comment(0x9883, 'Pull timeout', align=Align.INLINE)
d.comment(0x9884, 'Pull retry count', align=Align.INLINE)
d.comment(0x9885, 'Clear escapable flag and return', align=Align.INLINE)
d.comment(0x9888, """Pass-through TX buffer template (12 bytes)

Overlaid onto the TX control block by
setup_pass_txbuf for pass-through operations.
Offsets marked &FD are skipped, preserving the
existing destination station and network. Buffer
addresses point to &0D3A-&0D3E in NMI workspace.
Original TX buffer values are pushed on the stack
and restored after transmission.""")
d.comment(0x9888, 'Offset 0: ctrl = &88 (immediate TX)', align=Align.INLINE)
d.comment(0x9889, 'Offset 1: port = &00 (immediate op)', align=Align.INLINE)
d.comment(0x988A, 'Offset 2: &FD skip (preserve dest stn)', align=Align.INLINE)
d.comment(0x988B, 'Offset 3: &FD skip (preserve dest net)', align=Align.INLINE)
d.comment(0x988C, 'Offset 4: buf start lo (&3A)', align=Align.INLINE)
d.comment(0x988D, 'Offset 5: buf start hi (&0D) -> &0D3A', align=Align.INLINE)
d.comment(0x988E, 'Offset 6: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x988F, 'Offset 7: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x9890, 'Offset 8: buf end lo (&3E)', align=Align.INLINE)
d.comment(0x9891, 'Offset 9: buf end hi (&0D) -> &0D3E', align=Align.INLINE)
d.comment(0x9892, 'Offset 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x9893, 'Offset 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x9894, 'Y=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9896, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0x9898, 'Y=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x989A, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0x989C, 'Y=&0B: 12 bytes to process (0-11)', align=Align.INLINE)
d.comment(0x989E, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x98A1, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x98A3, "Yes: skip this offset, don't modify", align=Align.INLINE)
d.comment(0x98A5, 'Load existing TX buffer byte', align=Align.INLINE)
d.comment(0x98A7, 'Save original value on stack', align=Align.INLINE)
d.comment(0x98A8, 'Copy template value to A', align=Align.INLINE)
d.comment(0x98A9, 'Store template value to TX buffer', align=Align.INLINE)
d.comment(0x98AB, 'Next offset (descending)', align=Align.INLINE)
d.comment(0x98AC, 'Loop until all 12 bytes processed', align=Align.INLINE)
d.comment(0x98AE, 'Load pass-through control value', align=Align.INLINE)
d.comment(0x98B1, 'Push control value', align=Align.INLINE)
d.comment(0x98B2, 'A=&FF (Y is &FF after loop)', align=Align.INLINE)
d.comment(0x98B3, 'Push &FF as timeout', align=Align.INLINE)
d.comment(0x98B4, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x98B6, 'Load control byte from TX CB', align=Align.INLINE)
d.comment(0x98B8, 'Write control byte to start TX', align=Align.INLINE)
d.comment(0x98BA, 'Save control byte on stack', align=Align.INLINE)
d.comment(0x98BB, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x98BE, 'Shift result: check bit 6 (success)', align=Align.INLINE)
d.comment(0x98BF, 'Bit 6 clear: transmission complete', align=Align.INLINE)
d.comment(0x98C1, 'Shift result: check bit 5 (fatal)', align=Align.INLINE)
d.comment(0x98C2, 'Non-zero (not fatal): retry', align=Align.INLINE)
d.comment(0x98C4, 'X=0: clear error status', align=Align.INLINE)
d.comment(0x98C6, 'Jump to fix up reply status', align=Align.INLINE)
d.comment(0x98C9, 'Shift ws_0d60 left to poll ADLC', align=Align.INLINE)
d.comment(0x98CC, 'Bit not set: keep polling', align=Align.INLINE)
d.comment(0x98CE, 'Copy TX pointer low to NMI TX block', align=Align.INLINE)
d.comment(0x98D0, 'Store in NMI TX block low', align=Align.INLINE)
d.comment(0x98D2, 'Copy TX pointer high', align=Align.INLINE)
d.comment(0x98D4, 'Store in NMI TX block high', align=Align.INLINE)
d.comment(0x98D6, 'Begin Econet frame transmission', align=Align.INLINE)
d.comment(0x98D9, 'Read TX status byte', align=Align.INLINE)
d.comment(0x98DB, 'Bit 7 set: still transmitting', align=Align.INLINE)
d.comment(0x98DD, 'Return with result in A', align=Align.INLINE)
d.comment(0x98DE, 'Pull control byte', align=Align.INLINE)
d.comment(0x98DF, 'Restore to X', align=Align.INLINE)
d.comment(0x98E0, 'Pull timeout', align=Align.INLINE)
d.comment(0x98E1, 'Restore to Y', align=Align.INLINE)
d.comment(0x98E2, 'Pull retry count', align=Align.INLINE)
d.comment(0x98E3, 'Zero retries: go to error handling', align=Align.INLINE)
d.comment(0x98E5, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x98E7, 'Push updated retry count', align=Align.INLINE)
d.comment(0x98E8, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x98E9, 'Push timeout', align=Align.INLINE)
d.comment(0x98EA, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x98EB, 'Inner delay loop: decrement X', align=Align.INLINE)
d.comment(0x98EC, 'Loop until X=0', align=Align.INLINE)
d.comment(0x98EE, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x98EF, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x98F1, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x98F3, 'Pull control byte (discard)', align=Align.INLINE)
d.comment(0x98F4, 'Pull timeout (discard)', align=Align.INLINE)
d.comment(0x98F5, 'Pull retry count (discard)', align=Align.INLINE)
d.comment(0x98F6, 'Y=0: start restoring from offset 0', align=Align.INLINE)
d.comment(0x98F8, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x98FB, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x98FD, "Yes: don't restore this offset", align=Align.INLINE)
d.comment(0x98FF, 'Pull original value from stack', align=Align.INLINE)
d.comment(0x9900, 'Restore original TX buffer byte', align=Align.INLINE)
d.comment(0x9902, 'Next offset (ascending)', align=Align.INLINE)
d.comment(0x9903, 'Processed all 12 bytes?', align=Align.INLINE)
d.comment(0x9905, 'No: continue restoring', align=Align.INLINE)
d.comment(0x9907, 'Return with TX buffer restored', align=Align.INLINE)
d.comment(0x9908, 'Y=1: start at second byte of pointer', align=Align.INLINE)
d.comment(0x990A, 'Load pointer byte from FS options', align=Align.INLINE)
d.comment(0x990C, 'Store in OS text pointer', align=Align.INLINE)
d.comment(0x990F, 'Decrement index', align=Align.INLINE)
d.comment(0x9910, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0x9912, 'Y=0: reset index for string reading', align=Align.INLINE)
d.comment(0x9913, 'X=&FF: pre-increment for buffer index', align=Align.INLINE)
d.comment(0x9915, 'C=0: initialise for string input', align=Align.INLINE)
d.comment(0x9916, 'GSINIT: initialise string reading', align=Align.INLINE)
d.comment(0x9919, 'Z set (empty string): store terminator', align=Align.INLINE)
d.comment(0x991B, 'GSREAD: read next character', align=Align.INLINE)
d.comment(0x991E, 'C set: end of string reached', align=Align.INLINE)
d.comment(0x9920, 'Advance buffer index', align=Align.INLINE)
d.comment(0x9921, 'Store character in l0e30 buffer', align=Align.INLINE)
d.comment(0x9924, 'ALWAYS branch: read next character', align=Align.INLINE)
d.comment(0x9926, 'Advance past last character', align=Align.INLINE)
d.comment(0x9927, 'A=CR: terminate filename', align=Align.INLINE)
d.comment(0x9929, 'Store CR terminator in buffer', align=Align.INLINE)
d.comment(0x992C, 'A=&30: low byte of l0e30 buffer', align=Align.INLINE)
d.comment(0x992E, 'Set command text pointer low', align=Align.INLINE)
d.comment(0x9930, 'A=&0E: high byte of l0e30 buffer', align=Align.INLINE)
d.comment(0x9932, 'Set command text pointer high', align=Align.INLINE)
d.comment(0x9934, 'Return with buffer filled', align=Align.INLINE)
d.comment(0x9935, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9938, 'Load text pointer and parse filename', align=Align.INLINE)
d.comment(0x993B, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x993E, 'Parse access prefix from filename', align=Align.INLINE)
d.comment(0x9941, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9943, 'Positive (not last): display file info', align=Align.INLINE)
d.comment(0x9945, 'Is it &FF (last entry)?', align=Align.INLINE)
d.comment(0x9947, 'Yes: copy arg and iterate', align=Align.INLINE)
d.comment(0x9949, 'Other value: return with flag', align=Align.INLINE)
d.comment(0x994C, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x994F, 'Y=2: enumerate directory command', align=Align.INLINE)
d.comment(0x9951, 'A=&92: FS port number', align=Align.INLINE)
d.comment(0x9953, 'Set escapable flag to &92', align=Align.INLINE)
d.comment(0x9955, 'Store port number in TX buffer', align=Align.INLINE)
d.comment(0x9958, 'Send request to file server', align=Align.INLINE)
d.comment(0x995B, 'Y=6: offset to response cycle flag', align=Align.INLINE)
d.comment(0x995D, 'Load cycle flag from FS options', align=Align.INLINE)
d.comment(0x995F, 'Non-zero: already initialised', align=Align.INLINE)
d.comment(0x9961, 'Copy FS options to zero page first', align=Align.INLINE)
d.comment(0x9964, 'Then copy workspace to FS options', align=Align.INLINE)
d.comment(0x9967, 'Branch to continue (C clear from JSR)', align=Align.INLINE)
d.comment(0x9969, 'Copy workspace to FS options first', align=Align.INLINE)
d.comment(0x996C, 'Then copy FS options to zero page', align=Align.INLINE)
d.comment(0x996F, 'Y=4: loop counter', align=Align.INLINE)
d.comment(0x9971, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x9973, 'Save to TXCB end pointer', align=Align.INLINE)
d.comment(0x9975, 'Add offset from buffer', align=Align.INLINE)
d.comment(0x9978, 'Store sum in fs_work area', align=Align.INLINE)
d.comment(0x997A, 'Advance to next byte', align=Align.INLINE)
d.comment(0x997B, 'Decrement counter', align=Align.INLINE)
d.comment(0x997C, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x997E, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x997F, 'Subtract high offset', align=Align.INLINE)
d.comment(0x9982, 'Store result in fs_work_7', align=Align.INLINE)
d.comment(0x9984, 'Format filename for display', align=Align.INLINE)
d.comment(0x9987, 'Send TXCB and swap addresses', align=Align.INLINE)
d.comment(0x998A, 'X=2: copy 3 offset bytes', align=Align.INLINE)
d.comment(0x998C, 'Load offset byte from l0f10', align=Align.INLINE)
d.comment(0x998F, 'Store in l0f05 for next iteration', align=Align.INLINE)
d.comment(0x9992, 'Decrement counter', align=Align.INLINE)
d.comment(0x9993, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9995, 'Jump to receive and process reply', align=Align.INLINE)
d.comment(0x9998, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x999B, 'Match: no need to send, return', align=Align.INLINE)
d.comment(0x999D, 'A=&92: FS reply port number', align=Align.INLINE)
d.comment(0x999F, 'Set TXCB port', align=Align.INLINE)
d.comment(0x99A1, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x99A3, 'Load TXCB end pointer byte', align=Align.INLINE)
d.comment(0x99A5, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x99A7, 'Load new end address from fs_work', align=Align.INLINE)
d.comment(0x99A9, 'Store in TXCB end pointer', align=Align.INLINE)
d.comment(0x99AB, 'Decrement counter', align=Align.INLINE)
d.comment(0x99AC, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x99AE, 'A=&7F: control byte for data transfer', align=Align.INLINE)
d.comment(0x99B0, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x99B2, 'Wait for network TX acknowledgement', align=Align.INLINE)
d.comment(0x99B5, 'Y=3: compare 4 bytes', align=Align.INLINE)
d.comment(0x99B7, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0x99BA, 'Compare with expected end address', align=Align.INLINE)
d.comment(0x99BD, 'Mismatch: resend from start', align=Align.INLINE)
d.comment(0x99BF, 'Decrement counter', align=Align.INLINE)
d.comment(0x99C0, 'Loop until all 4 bytes match', align=Align.INLINE)
d.comment(0x99C2, 'Return (all bytes match)', align=Align.INLINE)
d.comment(0x99C3, 'Z set: directory entry display', align=Align.INLINE)
d.comment(0x99C5, 'Non-zero: jump to OSWORD dispatch', align=Align.INLINE)
d.comment(0x99C8, 'X=4: loop counter for 4 iterations', align=Align.INLINE)
d.comment(0x99CA, 'Y=&0E: FS options offset for addresses', align=Align.INLINE)
d.comment(0x99CC, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x99CD, 'Load address byte from FS options', align=Align.INLINE)
d.comment(0x99CF, 'Save to workspace (port_ws_offset)', align=Align.INLINE)
d.comment(0x99D2, 'Y -= 4 to point to paired offset', align=Align.INLINE)
d.comment(0x99D5, 'Subtract paired value', align=Align.INLINE)
d.comment(0x99D7, 'Store difference in l0f03 buffer', align=Align.INLINE)
d.comment(0x99DA, 'Push difference', align=Align.INLINE)
d.comment(0x99DB, 'Load paired value from FS options', align=Align.INLINE)
d.comment(0x99DD, 'Save to workspace', align=Align.INLINE)
d.comment(0x99E0, 'Pull difference back', align=Align.INLINE)
d.comment(0x99E1, 'Store in FS options for display', align=Align.INLINE)
d.comment(0x99E3, 'Advance Y by 5 for next field', align=Align.INLINE)
d.comment(0x99E6, 'Decrement loop counter', align=Align.INLINE)
d.comment(0x99E7, 'Loop for all 4 address pairs', align=Align.INLINE)
d.comment(0x99E9, 'Y=9: copy 9 bytes of options data', align=Align.INLINE)
d.comment(0x99EB, 'Load FS options byte', align=Align.INLINE)
d.comment(0x99ED, 'Store in l0f03 buffer', align=Align.INLINE)
d.comment(0x99F0, 'Decrement index', align=Align.INLINE)
d.comment(0x99F1, 'Loop until all 9 bytes copied', align=Align.INLINE)
d.comment(0x99F3, 'A=&91: FS port for info request', align=Align.INLINE)
d.comment(0x99F5, 'Set escapable flag', align=Align.INLINE)
d.comment(0x99F7, 'Store port in TX buffer', align=Align.INLINE)
d.comment(0x99FA, 'Store in fs_error_ptr', align=Align.INLINE)
d.comment(0x99FC, 'X=&0B: copy argument at offset 11', align=Align.INLINE)
d.comment(0x99FE, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x9A01, 'Y=1: info sub-command', align=Align.INLINE)
d.comment(0x9A03, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9A05, 'Is it 7 (catalogue info)?', align=Align.INLINE)
d.comment(0x9A07, 'Save comparison result', align=Align.INLINE)
d.comment(0x9A08, 'Not 7: keep Y=1', align=Align.INLINE)
d.comment(0x9A0A, 'Y=&1D: extended info command', align=Align.INLINE)
d.comment(0x9A0C, 'Send request to file server', align=Align.INLINE)
d.comment(0x9A0F, 'Format filename for display', align=Align.INLINE)
d.comment(0x9A12, 'Restore comparison flags', align=Align.INLINE)
d.comment(0x9A13, 'Not catalogue info: show short format', align=Align.INLINE)
d.comment(0x9A15, 'X=0: start at first byte', align=Align.INLINE)
d.comment(0x9A17, 'ALWAYS branch to store and display', align=Align.INLINE)
d.comment(0x9A19, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9A1C, 'Check and set up TXCB for transfer', align=Align.INLINE)
d.comment(0x9A1F, 'Receive and process reply', align=Align.INLINE)
d.comment(0x9A22, 'Store result byte in l0f08', align=Align.INLINE)
d.comment(0x9A25, 'Y=&0E: protection bits offset', align=Align.INLINE)
d.comment(0x9A27, 'Load access byte from l0f05', align=Align.INLINE)
d.comment(0x9A2A, 'Extract protection bit flags', align=Align.INLINE)
d.comment(0x9A2D, 'Zero: use reply buffer data', align=Align.INLINE)
d.comment(0x9A2F, 'Load file info byte from l0ef7', align=Align.INLINE)
d.comment(0x9A32, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9A34, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9A35, 'Y=&12: end of protection fields?', align=Align.INLINE)
d.comment(0x9A37, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A39, 'Load display flag from l0e06', align=Align.INLINE)
d.comment(0x9A3C, 'Zero: skip display, return', align=Align.INLINE)
d.comment(0x9A3E, 'Y=&F4: index into l0fff for filename', align=Align.INLINE)
d.comment(0x9A40, 'Load filename character from l10f3', align=Align.INLINE)
d.comment(0x9A43, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x9A46, 'Advance to next character', align=Align.INLINE)
d.comment(0x9A47, 'Printed all 12 characters?', align=Align.INLINE)
d.comment(0x9A47, 'No: print next character', align=Align.INLINE)
d.comment(0x9A49, 'Y=5: offset for access string', align=Align.INLINE)
d.comment(0x9A4B, 'Print 5 hex bytes (access info)', align=Align.INLINE)
d.comment(0x9A4E, 'Print load and exec addresses', align=Align.INLINE)
d.comment(0x9A51, 'Print newline', align=Align.INLINE)
d.comment(0x9A54, 'Jump to return with last flag', align=Align.INLINE)
d.comment(0x9A57, 'Y=9: offset for exec address', align=Align.INLINE)
d.comment(0x9A59, 'Print 5 hex bytes (exec address)', align=Align.INLINE)
d.comment(0x9A5C, 'Y=&0C: offset for length (3 bytes)', align=Align.INLINE)
d.comment(0x9A5E, 'X=3: print 3 bytes only', align=Align.INLINE)
d.comment(0x9A60, 'ALWAYS branch to print routine', align=Align.INLINE)
d.comment(0x9A62, 'X=4: print 5 bytes (4 to 0)', align=Align.INLINE)
d.comment(0x9A64, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9A66, 'Print as 2-digit hex', align=Align.INLINE)
d.comment(0x9A69, 'Decrement byte offset', align=Align.INLINE)
d.comment(0x9A6A, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9A6B, 'Loop until all bytes printed', align=Align.INLINE)
d.comment(0x9A6D, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9A6F, 'Print space via OSASCI and return', align=Align.INLINE)
d.comment(0x9A72, 'Y=5: copy 4 bytes (offsets 2-5)', align=Align.INLINE)
d.comment(0x9A74, 'Load byte from FS options', align=Align.INLINE)
d.comment(0x9A76, 'Store in zero page at l00ae+Y', align=Align.INLINE)
d.comment(0x9A79, 'Decrement index', align=Align.INLINE)
d.comment(0x9A7A, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9A7C, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A7E, 'Y += 5', align=Align.INLINE)
d.comment(0x9A7F, 'Y += 4', align=Align.INLINE)
d.comment(0x9A80, '(continued)', align=Align.INLINE)
d.comment(0x9A81, '(continued)', align=Align.INLINE)
d.comment(0x9A82, '(continued)', align=Align.INLINE)
d.comment(0x9A83, 'Return', align=Align.INLINE)
d.comment(0x9A84, 'Y=&0D: copy bytes from offset &0D down', align=Align.INLINE)
d.comment(0x9A86, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9A87, 'Store byte in FS options at offset Y', align=Align.INLINE)
d.comment(0x9A89, 'Load next workspace byte from l0f02+Y', align=Align.INLINE)
d.comment(0x9A8C, 'Decrement index', align=Align.INLINE)
d.comment(0x9A8D, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9A8F, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A91, 'Y -= 4', align=Align.INLINE)
d.comment(0x9A92, 'Y -= 3', align=Align.INLINE)
d.comment(0x9A93, '(continued)', align=Align.INLINE)
d.comment(0x9A94, '(continued)', align=Align.INLINE)
d.comment(0x9A95, 'Return', align=Align.INLINE)
d.comment(0x9A96, 'Discard stacked value', align=Align.INLINE)
d.comment(0x9A97, 'Restore Y from fs_block_offset', align=Align.INLINE)
d.comment(0x9A99, 'Return (handle already matches)', align=Align.INLINE)
d.comment(0x9A9A, 'Save port/sub-function on stack', align=Align.INLINE)
d.comment(0x9A9B, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x9A9E, 'Match: discard port and return', align=Align.INLINE)
d.comment(0x9AA0, 'X=0: loop start', align=Align.INLINE)
d.comment(0x9AA2, 'Y=4: copy 4 bytes', align=Align.INLINE)
d.comment(0x9AA4, 'Clear l0f08 (transfer size low)', align=Align.INLINE)
d.comment(0x9AA7, 'Clear l0f09 (transfer size high)', align=Align.INLINE)
d.comment(0x9AAA, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9AAB, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x9AAD, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x9AAF, 'Add offset from l0f06', align=Align.INLINE)
d.comment(0x9AB2, 'Store sum in TXCB end pointer', align=Align.INLINE)
d.comment(0x9AB4, 'Also update load address', align=Align.INLINE)
d.comment(0x9AB6, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9AB7, 'Decrement counter', align=Align.INLINE)
d.comment(0x9AB8, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9ABA, 'Carry set: overflow, use limit', align=Align.INLINE)
d.comment(0x9ABC, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9ABD, 'Load computed end address', align=Align.INLINE)
d.comment(0x9AC0, 'Subtract maximum from fs_work_4', align=Align.INLINE)
d.comment(0x9AC3, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9AC4, 'Decrement counter', align=Align.INLINE)
d.comment(0x9AC5, 'Loop for all bytes', align=Align.INLINE)
d.comment(0x9AC7, 'Below limit: keep computed end', align=Align.INLINE)
d.comment(0x9AC9, 'X=3: copy 4 bytes of limit', align=Align.INLINE)
d.comment(0x9ACB, 'Load limit from fs_work_4', align=Align.INLINE)
d.comment(0x9ACD, 'Store as TXCB end', align=Align.INLINE)
d.comment(0x9ACF, 'Decrement counter', align=Align.INLINE)
d.comment(0x9AD0, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9AD2, 'Pull port from stack', align=Align.INLINE)
d.comment(0x9AD3, 'Push back (keep for later)', align=Align.INLINE)
d.comment(0x9AD4, 'Save flags (carry = overflow state)', align=Align.INLINE)
d.comment(0x9AD5, 'Set TXCB port number', align=Align.INLINE)
d.comment(0x9AD7, 'A=&80: control byte for data request', align=Align.INLINE)
d.comment(0x9AD9, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x9ADB, 'Init TX pointer and send packet', align=Align.INLINE)
d.comment(0x9ADE, 'Load error pointer', align=Align.INLINE)
d.comment(0x9AE0, 'Init TXCB port from error pointer', align=Align.INLINE)
d.comment(0x9AE3, 'Restore overflow flags', align=Align.INLINE)
d.comment(0x9AE4, 'Carry set: discard and return', align=Align.INLINE)
d.comment(0x9AE6, 'A=&91: FS reply port', align=Align.INLINE)
d.comment(0x9AE8, 'Set TXCB port for reply', align=Align.INLINE)
d.comment(0x9AEA, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0x9AED, 'Non-zero (not done): retry send', align=Align.INLINE)
d.comment(0x9AEF, 'Store sub-operation code', align=Align.INLINE)
d.comment(0x9AF2, 'Compare with 7', align=Align.INLINE)
d.comment(0x9AF4, 'Below 7: handle operations 1-6', align=Align.INLINE)
d.comment(0x9AF6, 'Above 7: jump to handle via finalise', align=Align.INLINE)
d.comment(0x9AF8, 'Equal to 7: jump to directory display', align=Align.INLINE)
d.comment(0x9AFB, 'Compare with 6', align=Align.INLINE)
d.comment(0x9AFD, '6: delete file operation', align=Align.INLINE)
d.comment(0x9AFF, 'Compare with 5', align=Align.INLINE)
d.comment(0x9B01, '5: read catalogue info', align=Align.INLINE)
d.comment(0x9B03, 'Compare with 4', align=Align.INLINE)
d.comment(0x9B05, '4: write file attributes', align=Align.INLINE)
d.comment(0x9B07, 'Compare with 1', align=Align.INLINE)
d.comment(0x9B09, '1: read file info', align=Align.INLINE)
d.comment(0x9B0B, 'Shift left twice: A*4', align=Align.INLINE)
d.comment(0x9B0C, 'A*4', align=Align.INLINE)
d.comment(0x9B0D, 'Copy to Y as index', align=Align.INLINE)
d.comment(0x9B0E, 'Y -= 3 to get FS options offset', align=Align.INLINE)
d.comment(0x9B11, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9B13, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9B15, 'Store in l0f06 buffer', align=Align.INLINE)
d.comment(0x9B18, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9B19, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9B1A, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9B1C, 'X=5: copy arg to buffer at offset 5', align=Align.INLINE)
d.comment(0x9B1E, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9B20, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9B23, 'Store access byte in l0f0e', align=Align.INLINE)
d.comment(0x9B26, 'Y=9: source offset in FS options', align=Align.INLINE)
d.comment(0x9B28, 'X=8: copy 8 bytes to buffer', align=Align.INLINE)
d.comment(0x9B2A, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9B2C, 'Store in l0f05 buffer', align=Align.INLINE)
d.comment(0x9B2F, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9B30, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9B31, 'Loop for all 8 bytes', align=Align.INLINE)
d.comment(0x9B33, 'X=&0A: buffer offset for argument', align=Align.INLINE)
d.comment(0x9B35, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9B38, 'Y=&13: OSWORD &13 (NFS operation)', align=Align.INLINE)
d.comment(0x9B3A, 'ALWAYS branch to send request', align=Align.INLINE)
d.comment(0x9B3C, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x9B3F, 'Y=&14: delete file command', align=Align.INLINE)
d.comment(0x9B41, 'Set V flag (no directory check)', align=Align.INLINE)
d.comment(0x9B44, 'Send request with V set', align=Align.INLINE)
d.comment(0x9B47, 'Carry set: error, jump to finalise', align=Align.INLINE)
d.comment(0x9B49, 'No error: return with last flag', align=Align.INLINE)
d.comment(0x9B4C, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9B4F, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9B52, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9B54, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9B56, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9B58, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9B5B, 'Y=&12: open file command', align=Align.INLINE)
d.comment(0x9B5D, 'Send open file request', align=Align.INLINE)
d.comment(0x9B60, 'Load reply handle from l0f11', align=Align.INLINE)
d.comment(0x9B63, 'Clear l0f11', align=Align.INLINE)
d.comment(0x9B66, 'Clear l0f14', align=Align.INLINE)
d.comment(0x9B69, 'Get protection bits', align=Align.INLINE)
d.comment(0x9B6C, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9B6F, 'Zero: file not found, return', align=Align.INLINE)
d.comment(0x9B71, 'Y=&0E: store access bits', align=Align.INLINE)
d.comment(0x9B73, 'Store access byte in FS options', align=Align.INLINE)
d.comment(0x9B75, 'Y=&0D', align=Align.INLINE)
d.comment(0x9B76, 'X=&0C: copy 12 bytes of file info', align=Align.INLINE)
d.comment(0x9B78, 'Load reply byte from l0f05+X', align=Align.INLINE)
d.comment(0x9B7B, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9B7D, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9B7E, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9B7F, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0x9B81, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0x9B82, 'X=2', align=Align.INLINE)
d.comment(0x9B83, 'Y=&11: FS options offset', align=Align.INLINE)
d.comment(0x9B85, 'Load extended info byte from l0f12', align=Align.INLINE)
d.comment(0x9B88, 'Store in FS options', align=Align.INLINE)
d.comment(0x9B8A, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9B8B, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9B8C, 'Loop until all copied', align=Align.INLINE)
d.comment(0x9B8E, 'Reload file handle', align=Align.INLINE)
d.comment(0x9B91, 'Transfer to A', align=Align.INLINE)
d.comment(0x9B92, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9B95, """Unreachable dead code (3 bytes)

Duplicate of the JMP at &9B92 immediately above.
Unreachable after the unconditional JMP and
unreferenced. Likely a development remnant.""")
d.comment(0x9B95, 'Dead: duplicate JMP finalise_and_return', align=Align.INLINE)
d.comment(0x9B95, 'Y=0: destination index', align=Align.INLINE)
d.comment(0x9B97, 'Load source offset from l0f03', align=Align.INLINE)
d.comment(0x9B9A, 'Non-zero: copy from l0f05 buffer', align=Align.INLINE)
d.comment(0x9B9C, 'Load character from command line', align=Align.INLINE)
d.comment(0x9B9E, "Below '!' (control/space)?", align=Align.INLINE)
d.comment(0x9BA0, 'Yes: pad with spaces', align=Align.INLINE)
d.comment(0x9BA2, 'Store printable character in l10f3', align=Align.INLINE)
d.comment(0x9BA5, 'Advance to next character', align=Align.INLINE)
d.comment(0x9BA6, 'Loop for more characters', align=Align.INLINE)
d.comment(0x9BA8, "A=' ': space for padding", align=Align.INLINE)
d.comment(0x9BAA, 'Store space in display buffer', align=Align.INLINE)
d.comment(0x9BAD, 'Advance index', align=Align.INLINE)
d.comment(0x9BAE, 'Filled all 12 characters?', align=Align.INLINE)
d.comment(0x9BB0, 'No: pad more spaces', align=Align.INLINE)
d.comment(0x9BB2, 'Return with field formatted', align=Align.INLINE)
d.comment(0x9BB3, 'Advance source and destination', align=Align.INLINE)
d.comment(0x9BB4, 'INY', align=Align.INLINE)
d.comment(0x9BB5, 'Load byte from l0f05 buffer', align=Align.INLINE)
d.comment(0x9BB8, 'Store in display buffer l10f3', align=Align.INLINE)
d.comment(0x9BBB, 'Bit 7 clear: more characters', align=Align.INLINE)
d.comment(0x9BBD, 'Return (bit 7 set = terminator)', align=Align.INLINE)
d.comment(0x9BBE, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9BC1, 'Store result as last byte flag', align=Align.INLINE)
d.comment(0x9BC3, 'Set FS options pointer', align=Align.INLINE)
d.comment(0x9BC6, 'OR with 0 to set flags', align=Align.INLINE)
d.comment(0x9BC8, 'Positive: handle sub-operations', align=Align.INLINE)
d.comment(0x9BCA, 'Shift left to check bit 6', align=Align.INLINE)
d.comment(0x9BCB, 'Zero (was &80): close channel', align=Align.INLINE)
d.comment(0x9BCD, 'Other: process all FCBs first', align=Align.INLINE)
d.comment(0x9BD0, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9BD1, 'Compare with &20 (space)', align=Align.INLINE)
d.comment(0x9BD3, 'Above &20: check further', align=Align.INLINE)
d.comment(0x9BD5, 'Below &20: invalid channel char', align=Align.INLINE)
d.comment(0x9BD8, "Compare with '0'", align=Align.INLINE)
d.comment(0x9BDA, "Above '0': invalid channel char", align=Align.INLINE)
d.comment(0x9BDC, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9BDF, 'Transfer Y to A (FCB index)', align=Align.INLINE)
d.comment(0x9BE0, 'Push FCB index', align=Align.INLINE)
d.comment(0x9BE1, 'Copy to X', align=Align.INLINE)
d.comment(0x9BE2, 'Y=0: clear counter', align=Align.INLINE)
d.comment(0x9BE4, 'Clear last byte flag', align=Align.INLINE)
d.comment(0x9BE6, 'Clear block offset', align=Align.INLINE)
d.comment(0x9BE8, 'Load channel data from l1010+X', align=Align.INLINE)
d.comment(0x9BEB, 'Store in FS options at Y', align=Align.INLINE)
d.comment(0x9BED, 'Advance X by 8 (next FCB field)', align=Align.INLINE)
d.comment(0x9BF0, 'Advance destination index', align=Align.INLINE)
d.comment(0x9BF1, 'Copied all 4 channel fields?', align=Align.INLINE)
d.comment(0x9BF3, 'No: copy next field', align=Align.INLINE)
d.comment(0x9BF5, 'Pull saved FCB index', align=Align.INLINE)
d.comment(0x9BF6, 'Restore to fs_block_offset', align=Align.INLINE)
d.comment(0x9BF8, 'Compare with 5', align=Align.INLINE)
d.comment(0x9BFA, '5 or above: return with last flag', align=Align.INLINE)
d.comment(0x9BFC, 'Compare Y with 0', align=Align.INLINE)
d.comment(0x9BFE, 'Non-zero: handle OSFIND with channel', align=Align.INLINE)
d.comment(0x9C00, 'Y=0 (close): jump to OSFIND open', align=Align.INLINE)
d.comment(0x9C03, 'Push sub-function', align=Align.INLINE)
d.comment(0x9C04, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9C05, 'Push X (FCB slot)', align=Align.INLINE)
d.comment(0x9C06, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9C07, 'Push Y (channel char)', align=Align.INLINE)
d.comment(0x9C08, 'Check file is not a directory', align=Align.INLINE)
d.comment(0x9C0B, 'Pull channel char', align=Align.INLINE)
d.comment(0x9C0C, 'Store channel char as receive attribute', align=Align.INLINE)
d.comment(0x9C0F, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9C12, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9C15, 'Pull X (FCB slot)', align=Align.INLINE)
d.comment(0x9C16, 'Restore X', align=Align.INLINE)
d.comment(0x9C17, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9C18, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0x9C19, 'Zero (OSFIND close): handle close', align=Align.INLINE)
d.comment(0x9C1B, 'Save flags (carry from LSR)', align=Align.INLINE)
d.comment(0x9C1C, 'Push sub-function', align=Align.INLINE)
d.comment(0x9C1D, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9C1F, 'Load block offset', align=Align.INLINE)
d.comment(0x9C21, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9C24, 'Load updated data from l1010', align=Align.INLINE)
d.comment(0x9C27, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9C2A, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9C2B, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9C2E, 'Restore flags', align=Align.INLINE)
d.comment(0x9C2F, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9C30, 'Push Y (offset)', align=Align.INLINE)
d.comment(0x9C31, 'Carry clear: read operation', align=Align.INLINE)
d.comment(0x9C33, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9C35, 'Load zero page data', align=Align.INLINE)
d.comment(0x9C37, 'Store in l0f07 buffer', align=Align.INLINE)
d.comment(0x9C3A, 'Decrement source', align=Align.INLINE)
d.comment(0x9C3B, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C3C, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C3E, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9C40, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9C42, 'Send TX control block to server', align=Align.INLINE)
d.comment(0x9C45, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9C47, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9C48, 'Set connection active flag', align=Align.INLINE)
d.comment(0x9C4B, 'Return with last flag', align=Align.INLINE)
d.comment(0x9C4E, 'Y=&0C: TX buffer size (smaller)', align=Align.INLINE)
d.comment(0x9C50, 'X=2: argument offset', align=Align.INLINE)
d.comment(0x9C52, 'Send TX control block', align=Align.INLINE)
d.comment(0x9C55, 'Store A in last byte flag', align=Align.INLINE)
d.comment(0x9C57, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9C59, 'Y=2: zero page offset', align=Align.INLINE)
d.comment(0x9C5B, 'Store A in zero page', align=Align.INLINE)
d.comment(0x9C5D, 'Load buffer byte from l0f05+Y', align=Align.INLINE)
d.comment(0x9C60, 'Store in zero page at offset', align=Align.INLINE)
d.comment(0x9C62, 'Decrement source X', align=Align.INLINE)
d.comment(0x9C63, 'Decrement counter Y', align=Align.INLINE)
d.comment(0x9C64, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9C66, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9C67, 'Return with last flag', align=Align.INLINE)
d.comment(0x9C6A, 'Carry set: write file pointer', align=Align.INLINE)
d.comment(0x9C6C, 'Load block offset', align=Align.INLINE)
d.comment(0x9C6E, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9C71, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x9C73, 'Load FCB low byte from l1000', align=Align.INLINE)
d.comment(0x9C76, 'Store in zero page pointer low', align=Align.INLINE)
d.comment(0x9C79, 'Load FCB high byte from l1010', align=Align.INLINE)
d.comment(0x9C7C, 'Store in zero page pointer high', align=Align.INLINE)
d.comment(0x9C7F, 'Load FCB extent from l1020', align=Align.INLINE)
d.comment(0x9C82, 'Store in zero page work area', align=Align.INLINE)
d.comment(0x9C85, 'A=0: clear high byte', align=Align.INLINE)
d.comment(0x9C87, 'Store zero in work area high', align=Align.INLINE)
d.comment(0x9C8A, 'ALWAYS branch to return with flag', align=Align.INLINE)
d.comment(0x9C8C, 'Store write value in l0f06', align=Align.INLINE)
d.comment(0x9C8F, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9C90, 'Push X (zero page offset)', align=Align.INLINE)
d.comment(0x9C91, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9C93, 'Load zero page data at offset', align=Align.INLINE)
d.comment(0x9C95, 'Store in l0f07 buffer', align=Align.INLINE)
d.comment(0x9C98, 'Decrement source', align=Align.INLINE)
d.comment(0x9C99, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C9A, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C9C, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9C9E, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9CA0, 'Send TX control block', align=Align.INLINE)
d.comment(0x9CA3, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9CA5, 'Pull saved zero page offset', align=Align.INLINE)
d.comment(0x9CA6, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9CA7, 'Load block offset (attribute)', align=Align.INLINE)
d.comment(0x9CA9, 'Clear connection active flag', align=Align.INLINE)
d.comment(0x9CAC, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9CAF, 'Load zero page pointer low', align=Align.INLINE)
d.comment(0x9CB2, 'Store back to FCB l1000', align=Align.INLINE)
d.comment(0x9CB5, 'Load zero page pointer high', align=Align.INLINE)
d.comment(0x9CB8, 'Store back to FCB l1010', align=Align.INLINE)
d.comment(0x9CBB, 'Load zero page work byte', align=Align.INLINE)
d.comment(0x9CBE, 'Store back to FCB l1020', align=Align.INLINE)
d.comment(0x9CC1, 'Return with last flag', align=Align.INLINE)
d.comment(0x9CC4, 'Process all matching FCBs first', align=Align.INLINE)
d.comment(0x9CC7, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9CC9, 'Push result on stack', align=Align.INLINE)
d.comment(0x9CCA, 'A=0: clear error flag', align=Align.INLINE)
d.comment(0x9CCC, 'Clear receive attribute (A=0)', align=Align.INLINE)
d.comment(0x9CCF, 'Pull result back', align=Align.INLINE)
d.comment(0x9CD0, 'Restore X from FS options pointer', align=Align.INLINE)
d.comment(0x9CD2, 'Restore Y from block offset', align=Align.INLINE)
d.comment(0x9CD4, 'Return to caller', align=Align.INLINE)
d.comment(0x9CD5, 'Compare with 2 (open for output)', align=Align.INLINE)
d.comment(0x9CD7, '2 or above: handle file open', align=Align.INLINE)
d.comment(0x9CD9, 'Transfer to Y (Y=0 or 1)', align=Align.INLINE)
d.comment(0x9CDA, 'Non-zero (1 = read pointer): copy data', align=Align.INLINE)
d.comment(0x9CDC, 'A=5: return code for close-all', align=Align.INLINE)
d.comment(0x9CDE, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0x9CE0, 'Load reply data byte at Y', align=Align.INLINE)
d.comment(0x9CE3, 'Store in FS options', align=Align.INLINE)
d.comment(0x9CE5, 'Decrement index', align=Align.INLINE)
d.comment(0x9CE6, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9CE8, 'Clear zero page work low', align=Align.INLINE)
d.comment(0x9CEA, 'Clear zero page work high', align=Align.INLINE)
d.comment(0x9CEC, 'Z set: jump to clear A and return', align=Align.INLINE)
d.comment(0x9CEE, 'A=0: clear result', align=Align.INLINE)
d.comment(0x9CF0, 'Shift right (always positive)', align=Align.INLINE)
d.comment(0x9CF1, 'Positive: jump to finalise', align=Align.INLINE)
d.comment(0x9CF3, 'Mask to 6-bit access value', align=Align.INLINE)
d.comment(0x9CF5, 'Non-zero: clear A and finalise', align=Align.INLINE)
d.comment(0x9CF7, 'Transfer X to A (options pointer)', align=Align.INLINE)
d.comment(0x9CF8, 'Allocate FCB slot or raise error', align=Align.INLINE)
d.comment(0x9CFB, 'Toggle bit 7', align=Align.INLINE)
d.comment(0x9CFD, 'Shift left: build open mode', align=Align.INLINE)
d.comment(0x9CFE, 'Store open mode in l0f05', align=Align.INLINE)
d.comment(0x9D01, 'Rotate to complete mode byte', align=Align.INLINE)
d.comment(0x9D02, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9D05, 'Parse command argument (Y=0)', align=Align.INLINE)
d.comment(0x9D08, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9D0A, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x9D0D, 'Y=6: open file command', align=Align.INLINE)
d.comment(0x9D0F, 'Set V flag (skip directory check)', align=Align.INLINE)
d.comment(0x9D12, 'Set carry', align=Align.INLINE)
d.comment(0x9D13, 'Rotate carry into escapable flag bit 7', align=Align.INLINE)
d.comment(0x9D15, 'Send open request with V set', align=Align.INLINE)
d.comment(0x9D18, 'Carry set (error): jump to finalise', align=Align.INLINE)
d.comment(0x9D1A, 'A=&FF: mark as newly opened', align=Align.INLINE)
d.comment(0x9D1C, 'Store &FF as receive attribute', align=Align.INLINE)
d.comment(0x9D1F, 'Load handle from l0f05', align=Align.INLINE)
d.comment(0x9D22, 'Push handle', align=Align.INLINE)
d.comment(0x9D23, 'A=4: file info sub-command', align=Align.INLINE)
d.comment(0x9D25, 'Store sub-command', align=Align.INLINE)
d.comment(0x9D28, 'X=1: shift filename', align=Align.INLINE)
d.comment(0x9D2A, 'Load filename byte from l0f06+X', align=Align.INLINE)
d.comment(0x9D2D, 'Shift down to l0f05+X', align=Align.INLINE)
d.comment(0x9D30, 'Advance source index', align=Align.INLINE)
d.comment(0x9D31, 'Is it CR (end of filename)?', align=Align.INLINE)
d.comment(0x9D33, 'No: continue shifting', align=Align.INLINE)
d.comment(0x9D35, 'Y=&12: file info request', align=Align.INLINE)
d.comment(0x9D37, 'Send file info request', align=Align.INLINE)
d.comment(0x9D3A, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9D3C, 'Clear bit 6 (read/write bits)', align=Align.INLINE)
d.comment(0x9D3E, 'OR with reply access byte', align=Align.INLINE)
d.comment(0x9D41, 'Set bit 0 (file is open)', align=Align.INLINE)
d.comment(0x9D43, 'Transfer to Y (access flags)', align=Align.INLINE)
d.comment(0x9D44, 'Check bit 1 (write access)', align=Align.INLINE)
d.comment(0x9D46, 'No write access: check read-only', align=Align.INLINE)
d.comment(0x9D48, 'Pull handle from stack', align=Align.INLINE)
d.comment(0x9D49, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0x9D4C, 'Non-zero: FCB allocated, store flags', align=Align.INLINE)
d.comment(0x9D4E, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9D51, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9D54, 'Transfer A to X', align=Align.INLINE)
d.comment(0x9D55, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9D58, 'Transfer X back to A', align=Align.INLINE)
d.comment(0x9D59, 'Zero: close file, process FCBs', align=Align.INLINE)
d.comment(0x9D5B, 'Save text pointer for OS', align=Align.INLINE)
d.comment(0x9D5E, 'Load current directory handle', align=Align.INLINE)
d.comment(0x9D61, 'Zero: allocate new FCB', align=Align.INLINE)
d.comment(0x9D63, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9D64, 'X=0: clear directory handle', align=Align.INLINE)
d.comment(0x9D66, 'Store zero (clear handle)', align=Align.INLINE)
d.comment(0x9D69, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0x9D6B, 'Load access/open mode byte', align=Align.INLINE)
d.comment(0x9D6E, 'Rotate right: check bit 0', align=Align.INLINE)
d.comment(0x9D6F, 'Carry set (bit 0): check read permission', align=Align.INLINE)
d.comment(0x9D71, 'Rotate right: check bit 1', align=Align.INLINE)
d.comment(0x9D72, 'Carry clear (no write): skip', align=Align.INLINE)
d.comment(0x9D74, 'Test bit 7 of l0f07 (lock flag)', align=Align.INLINE)
d.comment(0x9D77, 'Not locked: skip', align=Align.INLINE)
d.comment(0x9D79, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0x9D7A, 'Set bit 5 (locked file flag)', align=Align.INLINE)
d.comment(0x9D7C, 'Transfer back to Y', align=Align.INLINE)
d.comment(0x9D7D, 'Pull handle from stack', align=Align.INLINE)
d.comment(0x9D7E, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0x9D81, 'Transfer to X', align=Align.INLINE)
d.comment(0x9D82, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0x9D83, 'Store flags in FCB table l1040', align=Align.INLINE)
d.comment(0x9D86, 'Transfer X back to A (handle)', align=Align.INLINE)
d.comment(0x9D87, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9D8A, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9D8D, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9D8E, 'Non-zero channel: close specific', align=Align.INLINE)
d.comment(0x9D90, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9D92, 'Push (save for restore)', align=Align.INLINE)
d.comment(0x9D93, 'A=&77: OSBYTE close spool/exec files', align=Align.INLINE)
d.comment(0x9D95, 'Close any *SPOOL and *EXEC files', align=Align.INLINE)
d.comment(0x9D98, 'Pull saved options pointer', align=Align.INLINE)
d.comment(0x9D99, 'Restore FS options pointer', align=Align.INLINE)
d.comment(0x9D9B, 'A=0: clear flags', align=Align.INLINE)
d.comment(0x9D9D, 'Clear last byte flag', align=Align.INLINE)
d.comment(0x9D9F, 'Clear block offset', align=Align.INLINE)
d.comment(0x9DA1, 'ALWAYS branch to send close request', align=Align.INLINE)
d.comment(0x9DA3, 'Validate channel character', align=Align.INLINE)
d.comment(0x9DA6, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9DA9, 'Store as l0f05 (file handle)', align=Align.INLINE)
d.comment(0x9DAC, 'X=1: argument size', align=Align.INLINE)
d.comment(0x9DAE, 'Y=7: close file command', align=Align.INLINE)
d.comment(0x9DB0, 'Send close file request', align=Align.INLINE)
d.comment(0x9DB3, 'Load block offset', align=Align.INLINE)
d.comment(0x9DB5, 'Non-zero: clear single FCB', align=Align.INLINE)
d.comment(0x9DB7, 'Clear V flag', align=Align.INLINE)
d.comment(0x9DB8, 'Scan and clear all FCB flags', align=Align.INLINE)
d.comment(0x9DBB, 'Return with last flag', align=Align.INLINE)
d.comment(0x9DBE, 'A=0: clear FCB entry', align=Align.INLINE)
d.comment(0x9DC0, 'Clear l1010 (FCB high byte)', align=Align.INLINE)
d.comment(0x9DC3, 'Clear l1040 (FCB flags)', align=Align.INLINE)
d.comment(0x9DC6, 'ALWAYS branch to return', align=Align.INLINE)
d.comment(0x9DC8, 'Z set: handle OSARGS 0', align=Align.INLINE)
d.comment(0x9DCA, 'Compare X with 4 (number of args)', align=Align.INLINE)
d.comment(0x9DCC, 'Not 4: check for error', align=Align.INLINE)
d.comment(0x9DCE, 'Compare Y with 4', align=Align.INLINE)
d.comment(0x9DD0, 'Below 4: handle special OSARGS', align=Align.INLINE)
d.comment(0x9DD2, 'Decrement X', align=Align.INLINE)
d.comment(0x9DD3, 'X was 1: store display flag', align=Align.INLINE)
d.comment(0x9DD5, 'Store Y in display control flag l0e06', align=Align.INLINE)
d.comment(0x9DD8, 'Carry clear: return with flag', align=Align.INLINE)
d.comment(0x9DDA, 'A=7: error code', align=Align.INLINE)
d.comment(0x9DDC, 'Jump to classify reply error', align=Align.INLINE)
d.comment(0x9DDF, 'Store Y in l0f05', align=Align.INLINE)
d.comment(0x9DE2, 'Y=&16: OSARGS save command', align=Align.INLINE)
d.comment(0x9DE4, 'Send OSARGS request', align=Align.INLINE)
d.comment(0x9DE7, 'Reload block offset', align=Align.INLINE)
d.comment(0x9DE9, 'Store in l0e05', align=Align.INLINE)
d.comment(0x9DEC, 'Positive: return with flag', align=Align.INLINE)
d.comment(0x9DEE, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9DF1, 'Push result on stack', align=Align.INLINE)
d.comment(0x9DF2, 'Load block offset', align=Align.INLINE)
d.comment(0x9DF4, 'Push block offset', align=Align.INLINE)
d.comment(0x9DF5, 'Store X in l10c9', align=Align.INLINE)
d.comment(0x9DF8, 'Find matching FCB entry', align=Align.INLINE)
d.comment(0x9DFB, 'Zero: no match found', align=Align.INLINE)
d.comment(0x9DFD, 'Load FCB low byte from l1000', align=Align.INLINE)
d.comment(0x9E00, 'Compare with stored offset l1098', align=Align.INLINE)
d.comment(0x9E03, 'Below stored: no match', align=Align.INLINE)
d.comment(0x9E05, 'X=&FF: mark as found (all bits set)', align=Align.INLINE)
d.comment(0x9E07, 'ALWAYS branch (negative)', align=Align.INLINE)
d.comment(0x9E09, 'X=0: mark as not found', align=Align.INLINE)
d.comment(0x9E0B, 'Restore block offset from stack', align=Align.INLINE)
d.comment(0x9E0C, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9E0D, 'Restore result from stack', align=Align.INLINE)
d.comment(0x9E0E, 'Return', align=Align.INLINE)
d.comment(0x9E0F, 'Y=9: FS options offset for high address', align=Align.INLINE)
d.comment(0x9E11, 'Add workspace values to FS options', align=Align.INLINE)
d.comment(0x9E14, 'Y=1: FS options offset for low address', align=Align.INLINE)
d.comment(0x9E16, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9E17, 'X=&FC: loop counter (-4 to -1)', align=Align.INLINE)
d.comment(0x9E19, 'Load FS options byte at offset Y', align=Align.INLINE)
d.comment(0x9E1B, 'Test fs_load_addr_2 bit 7 (add/subtract)', align=Align.INLINE)
d.comment(0x9E1D, 'Bit 7 set: subtract instead', align=Align.INLINE)
d.comment(0x9E1F, 'Add workspace byte to FS options', align=Align.INLINE)
d.comment(0x9E22, 'Jump to store result', align=Align.INLINE)
d.comment(0x9E25, 'Subtract workspace byte from FS options', align=Align.INLINE)
d.comment(0x9E28, 'Store result back to FS options', align=Align.INLINE)
d.comment(0x9E2A, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9E2B, 'Advance counter', align=Align.INLINE)
d.comment(0x9E2C, 'Loop until 4 bytes processed', align=Align.INLINE)
d.comment(0x9E2E, 'Return', align=Align.INLINE)
d.comment(0x9E2F, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9E32, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9E35, 'Push transfer type on stack', align=Align.INLINE)
d.comment(0x9E36, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9E39, 'Pull transfer type', align=Align.INLINE)
d.comment(0x9E3A, 'Transfer to X', align=Align.INLINE)
d.comment(0x9E3B, 'Zero: no valid operation, return', align=Align.INLINE)
d.comment(0x9E3D, 'Decrement (convert 1-based to 0-based)', align=Align.INLINE)
d.comment(0x9E3E, 'Compare with 8 (max operation)', align=Align.INLINE)
d.comment(0x9E40, 'Below 8: valid operation', align=Align.INLINE)
d.comment(0x9E42, 'Out of range: return with flag', align=Align.INLINE)
d.comment(0x9E45, 'Transfer operation code to A', align=Align.INLINE)
d.comment(0x9E46, 'Y=0: buffer offset', align=Align.INLINE)
d.comment(0x9E48, 'Push operation code', align=Align.INLINE)
d.comment(0x9E49, 'Compare with 4 (write operations)', align=Align.INLINE)
d.comment(0x9E4B, 'Below 4: read operation', align=Align.INLINE)
d.comment(0x9E4D, '4 or above: write data block', align=Align.INLINE)
d.comment(0x9E50, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9E52, 'Push handle', align=Align.INLINE)
d.comment(0x9E53, 'Check file is not a directory', align=Align.INLINE)
d.comment(0x9E56, 'Pull handle', align=Align.INLINE)
d.comment(0x9E57, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9E58, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9E5B, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9E5E, 'Store file handle in l0f05', align=Align.INLINE)
d.comment(0x9E61, 'A=0: clear direction flag', align=Align.INLINE)
d.comment(0x9E63, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9E66, 'Load FCB low byte (position)', align=Align.INLINE)
d.comment(0x9E69, 'Store in l0f07', align=Align.INLINE)
d.comment(0x9E6C, 'Load FCB high byte', align=Align.INLINE)
d.comment(0x9E6F, 'Store in l0f08', align=Align.INLINE)
d.comment(0x9E72, 'Load FCB extent byte', align=Align.INLINE)
d.comment(0x9E75, 'Store in l0f09', align=Align.INLINE)
d.comment(0x9E78, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9E7A, 'X=5: argument count', align=Align.INLINE)
d.comment(0x9E7C, 'Send TX control block to server', align=Align.INLINE)
d.comment(0x9E7F, 'Pull operation code', align=Align.INLINE)
d.comment(0x9E80, 'Set up transfer workspace', align=Align.INLINE)
d.comment(0x9E83, 'Save flags (carry from setup)', align=Align.INLINE)
d.comment(0x9E84, 'Y=0: index for channel handle', align=Align.INLINE)
d.comment(0x9E86, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9E88, 'Carry set (write): set active', align=Align.INLINE)
d.comment(0x9E8A, 'Read: clear connection active', align=Align.INLINE)
d.comment(0x9E8D, 'Branch to continue (always positive)', align=Align.INLINE)
d.comment(0x9E8F, 'Write: set connection active', align=Align.INLINE)
d.comment(0x9E92, 'Clear l0f06 (Y=0)', align=Align.INLINE)
d.comment(0x9E95, 'Look up channel slot data', align=Align.INLINE)
d.comment(0x9E98, 'Store flag byte in l0f05', align=Align.INLINE)
d.comment(0x9E9B, 'Y=&0C: TX buffer size (short)', align=Align.INLINE)
d.comment(0x9E9D, 'X=2: argument count', align=Align.INLINE)
d.comment(0x9E9F, 'Send TX control block', align=Align.INLINE)
d.comment(0x9EA2, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0x9EA5, 'Y=9: FS options offset for position', align=Align.INLINE)
d.comment(0x9EA7, 'Load new position low from l0f05', align=Align.INLINE)
d.comment(0x9EAA, 'Update FCB low byte in l1000', align=Align.INLINE)
d.comment(0x9EAD, 'Store in FS options at Y=9', align=Align.INLINE)
d.comment(0x9EAF, 'Y=&0A', align=Align.INLINE)
d.comment(0x9EB0, 'Load new position high from l0f06', align=Align.INLINE)
d.comment(0x9EB3, 'Update FCB high byte in l1010', align=Align.INLINE)
d.comment(0x9EB6, 'Store in FS options at Y=&0A', align=Align.INLINE)
d.comment(0x9EB8, 'Y=&0B', align=Align.INLINE)
d.comment(0x9EB9, 'Load new extent from l0f07', align=Align.INLINE)
d.comment(0x9EBC, 'Update FCB extent in l1020', align=Align.INLINE)
d.comment(0x9EBF, 'Store in FS options at Y=&0B', align=Align.INLINE)
d.comment(0x9EC1, 'A=0: clear high byte of extent', align=Align.INLINE)
d.comment(0x9EC3, 'Y=&0C', align=Align.INLINE)
d.comment(0x9EC4, 'Store zero in FS options at Y=&0C', align=Align.INLINE)
d.comment(0x9EC6, 'Restore flags', align=Align.INLINE)
d.comment(0x9EC7, 'Carry clear: skip last-byte check', align=Align.INLINE)
d.comment(0x9ECD, 'A=0: success', align=Align.INLINE)
d.comment(0x9EC9, 'Load last-byte-of-transfer flag', align=Align.INLINE)
d.comment(0x9ECF, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9ECB, 'Is transfer still pending (flag=3)?', align=Align.INLINE)
d.comment(0x9ED2, 'Y=0: offset for channel handle', align=Align.INLINE)
d.comment(0x9ED4, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9ED6, 'Look up channel by character', align=Align.INLINE)
d.comment(0x9ED9, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9EDC, 'Return with flag in A', align=Align.INLINE)
d.comment(0x9EDD, 'Push operation code on stack', align=Align.INLINE)
d.comment(0x9EDE, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0x9EE1, 'Store flag byte in l0f05', align=Align.INLINE)
d.comment(0x9EE4, 'Y=&0B: source offset in FS options', align=Align.INLINE)
d.comment(0x9EE6, 'X=6: copy 6 bytes', align=Align.INLINE)
d.comment(0x9EE8, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9EEA, 'Store in l0f06 buffer', align=Align.INLINE)
d.comment(0x9EED, 'Decrement source index', align=Align.INLINE)
d.comment(0x9EEE, 'Skip offset 8?', align=Align.INLINE)
d.comment(0x9EF0, 'No: continue copy', align=Align.INLINE)
d.comment(0x9EF2, 'Skip offset 8 (hole in structure)', align=Align.INLINE)
d.comment(0x9EF3, 'Decrement destination counter', align=Align.INLINE)
d.comment(0x9EF4, 'Loop until all 6 bytes copied', align=Align.INLINE)
d.comment(0x9EF6, 'Pull operation code', align=Align.INLINE)
d.comment(0x9EF7, 'Shift right: check bit 0 (direction)', align=Align.INLINE)
d.comment(0x9EF8, 'Push updated code', align=Align.INLINE)
d.comment(0x9EF9, 'Carry clear: OSBGET (read)', align=Align.INLINE)
d.comment(0x9EFB, 'Carry set: OSBPUT (write), X=1', align=Align.INLINE)
d.comment(0x9EFC, 'Store direction flag in l0f06', align=Align.INLINE)
d.comment(0x9EFF, 'Y=&0B: TX buffer size', align=Align.INLINE)
d.comment(0x9F01, 'X=&91: port for OSBGET', align=Align.INLINE)
d.comment(0x9F03, 'Pull operation code', align=Align.INLINE)
d.comment(0x9F04, 'Push back (keep on stack)', align=Align.INLINE)
d.comment(0x9F05, 'Zero (OSBGET): keep port &91', align=Align.INLINE)
d.comment(0x9F07, 'X=&92: port for OSBPUT', align=Align.INLINE)
d.comment(0x9F09, 'Y=&0A: adjusted buffer size', align=Align.INLINE)
d.comment(0x9F0A, 'Store port in l0f02', align=Align.INLINE)
d.comment(0x9F0D, 'Store port in fs_error_ptr', align=Align.INLINE)
d.comment(0x9F0F, 'X=8: argument count', align=Align.INLINE)
d.comment(0x9F11, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9F14, 'Send request (no write data)', align=Align.INLINE)
d.comment(0x9F17, 'X=0: index', align=Align.INLINE)
d.comment(0x9F19, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9F1B, 'Transfer to X as index', align=Align.INLINE)
d.comment(0x9F1C, 'Load FCB flags from l1040', align=Align.INLINE)
d.comment(0x9F1F, 'Toggle bit 0 (transfer direction)', align=Align.INLINE)
d.comment(0x9F21, 'Store updated flags', align=Align.INLINE)
d.comment(0x9F24, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9F25, 'X=4: process 4 address bytes', align=Align.INLINE)
d.comment(0x9F27, 'Load FS options address byte', align=Align.INLINE)
d.comment(0x9F29, 'Store in zero page address area', align=Align.INLINE)
d.comment(0x9F2C, 'Store in TXCB position', align=Align.INLINE)
d.comment(0x9F2F, 'Advance Y by 4', align=Align.INLINE)
d.comment(0x9F32, 'Add offset from FS options', align=Align.INLINE)
d.comment(0x9F34, 'Store computed end address', align=Align.INLINE)
d.comment(0x9F37, 'Retreat Y by 3 for next pair', align=Align.INLINE)
d.comment(0x9F3A, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9F3B, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x9F3D, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0x9F3E, 'Load offset from l0f03', align=Align.INLINE)
d.comment(0x9F41, 'Copy to l0f06', align=Align.INLINE)
d.comment(0x9F44, 'Decrement counter', align=Align.INLINE)
d.comment(0x9F45, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0x9F47, 'Pull operation code', align=Align.INLINE)
d.comment(0x9F48, 'Non-zero (OSBPUT): swap addresses', align=Align.INLINE)
d.comment(0x9F4A, 'Load port from l0f02', align=Align.INLINE)
d.comment(0x9F4D, 'Check and set up TXCB', align=Align.INLINE)
d.comment(0x9F50, 'Carry set: skip swap', align=Align.INLINE)
d.comment(0x9F52, 'Send TXCB and swap start/end addresses', align=Align.INLINE)
d.comment(0x9F55, 'Receive and process reply', align=Align.INLINE)
d.comment(0x9F58, 'Store result in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F5A, 'Update addresses from offset 9', align=Align.INLINE)
d.comment(0x9F5D, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F5F, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9F60, 'Adjust FS options by 4 bytes', align=Align.INLINE)
d.comment(0x9F63, 'Shift l0f05 left (update status)', align=Align.INLINE)
d.comment(0x9F66, 'Return', align=Align.INLINE)
d.comment(0x9F6C, 'Return', align=Align.INLINE)
d.comment(0x9F67, 'Save flags before reply processing', align=Align.INLINE)
d.comment(0x9F68, 'Process server reply', align=Align.INLINE)
d.comment(0x9F6B, 'Restore flags after reply processing', align=Align.INLINE)
d.comment(0x9F6D, 'Y=&15: TX buffer size for OSBPUT data', align=Align.INLINE)
d.comment(0x9F6F, 'Send TX control block', align=Align.INLINE)
d.comment(0x9F72, 'Load display flag from l0e05', align=Align.INLINE)
d.comment(0x9F75, 'Store in l0f16', align=Align.INLINE)
d.comment(0x9F78, 'Clear fs_load_addr (X=0)', align=Align.INLINE)
d.comment(0x9F7A, 'Clear fs_load_addr_hi', align=Align.INLINE)
d.comment(0x9F7C, 'A=&12: byte count for data block', align=Align.INLINE)
d.comment(0x9F7E, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F80, 'ALWAYS branch to write data block', align=Align.INLINE)
d.comment(0x9F82, 'Y=4: offset for station comparison', align=Align.INLINE)
d.comment(0x9F84, 'Load stored station from l0d63', align=Align.INLINE)
d.comment(0x9F87, 'Zero: skip station check', align=Align.INLINE)
d.comment(0x9F89, 'Compare with FS options station', align=Align.INLINE)
d.comment(0x9F8B, 'Mismatch: skip subtraction', align=Align.INLINE)
d.comment(0x9F8D, 'Y=3', align=Align.INLINE)
d.comment(0x9F8E, 'Subtract FS options value', align=Align.INLINE)
d.comment(0x9F90, 'Store result in svc_state', align=Align.INLINE)
d.comment(0x9F92, 'Load FS options byte at Y', align=Align.INLINE)
d.comment(0x9F94, 'Store in workspace at fs_last_byte_flag+Y', align=Align.INLINE)
d.comment(0x9F97, 'Decrement index', align=Align.INLINE)
d.comment(0x9F98, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9F9A, 'Pull operation code', align=Align.INLINE)
d.comment(0x9F9B, 'Mask to 2-bit sub-operation', align=Align.INLINE)
d.comment(0x9F9D, 'Zero: send OSBPUT data', align=Align.INLINE)
d.comment(0x9F9F, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0x9FA0, 'Zero (bit 0 clear): handle read', align=Align.INLINE)
d.comment(0x9FA2, 'Carry set: handle catalogue update', align=Align.INLINE)
d.comment(0x9FA4, 'Transfer to Y (Y=0)', align=Align.INLINE)
d.comment(0x9FA5, 'Load data byte from l0e03', align=Align.INLINE)
d.comment(0x9FA8, 'Store in l0f03', align=Align.INLINE)
d.comment(0x9FAB, 'Load high data byte from l0e04', align=Align.INLINE)
d.comment(0x9FAE, 'Store in l0f04', align=Align.INLINE)
d.comment(0x9FB1, 'Load port from l0e02', align=Align.INLINE)
d.comment(0x9FB4, 'Store in l0f02', align=Align.INLINE)
d.comment(0x9FB7, 'X=&12: buffer size marker', align=Align.INLINE)
d.comment(0x9FB9, 'Store in l0f01', align=Align.INLINE)
d.comment(0x9FBC, 'A=&0D: count value', align=Align.INLINE)
d.comment(0x9FBE, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9FC1, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9FC3, 'Shift right (A=6)', align=Align.INLINE)
d.comment(0x9FC4, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9FC7, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9FC8, 'Prepare and send TX control block', align=Align.INLINE)
d.comment(0x9FCB, 'Store X in fs_load_addr_hi (X=0)', align=Align.INLINE)
d.comment(0x9FCD, 'X=1 (INX)', align=Align.INLINE)
d.comment(0x9FCE, 'Store X in fs_load_addr', align=Align.INLINE)
d.comment(0x9FD0, 'Load svc_state (tube flag)', align=Align.INLINE)
d.comment(0x9FD2, 'Non-zero: write via tube', align=Align.INLINE)
d.comment(0x9FD4, 'Load source index from fs_load_addr', align=Align.INLINE)
d.comment(0x9FD6, 'Load destination index from fs_load_addr_hi', align=Align.INLINE)
d.comment(0x9FD8, 'Load data byte from l0f05 buffer', align=Align.INLINE)
d.comment(0x9FDB, 'Store to destination via fs_crc pointer', align=Align.INLINE)
d.comment(0x9FDD, 'Advance source index', align=Align.INLINE)
d.comment(0x9FDE, 'Advance destination index', align=Align.INLINE)
d.comment(0x9FDF, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9FE1, 'Loop until all bytes transferred', align=Align.INLINE)
d.comment(0x9FE3, 'ALWAYS branch to update catalogue', align=Align.INLINE)
d.comment(0x9FE5, 'Claim tube with call &C3', align=Align.INLINE)
d.comment(0x9FE8, 'A=1: tube transfer type (write)', align=Align.INLINE)
d.comment(0x9FEA, 'Load destination low from fs_options', align=Align.INLINE)
d.comment(0x9FEC, 'Load destination high from fs_block_offset', align=Align.INLINE)
d.comment(0x9FEE, 'Increment low byte', align=Align.INLINE)
d.comment(0x9FEF, 'No wrap: skip high increment', align=Align.INLINE)
d.comment(0x9FF1, 'Carry: increment high byte', align=Align.INLINE)
d.comment(0x9FF2, 'Set up tube transfer address', align=Align.INLINE)
d.comment(0x9FF5, 'Load source index', align=Align.INLINE)
d.comment(0x9FF7, 'Load data byte from buffer', align=Align.INLINE)
d.comment(0x9FFA, 'Write to tube data register 3', align=Align.INLINE)
d.comment(0x9FFD, 'Advance source index', align=Align.INLINE)
d.comment(0x9FFE, 'Y=6: tube write delay', align=Align.INLINE)
d.comment(0xA000, 'Delay loop: decrement Y', align=Align.INLINE)
d.comment(0xA001, 'Loop until delay complete', align=Align.INLINE)
d.comment(0xA003, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xA005, 'Loop until all bytes written to tube', align=Align.INLINE)
d.comment(0xA007, 'A=&83: release tube claim', align=Align.INLINE)
d.comment(0xA009, 'Release tube', align=Align.INLINE)
d.comment(0xA00C, 'Jump to clear A and finalise return', align=Align.INLINE)
d.comment(0xA00F, 'Y=9: offset for position byte', align=Align.INLINE)
d.comment(0xA011, 'Load position from FS options', align=Align.INLINE)
d.comment(0xA013, 'Store in l0f06', align=Align.INLINE)
d.comment(0xA016, 'Y=5: offset for extent byte', align=Align.INLINE)
d.comment(0xA018, 'Load extent byte from FS options', align=Align.INLINE)
d.comment(0xA01A, 'Store in l0f07', align=Align.INLINE)
d.comment(0xA01D, 'X=&0D: byte count', align=Align.INLINE)
d.comment(0xA01F, 'Store in l0f08', align=Align.INLINE)
d.comment(0xA022, 'Y=2: command sub-type', align=Align.INLINE)
d.comment(0xA024, 'Store in fs_load_addr', align=Align.INLINE)
d.comment(0xA026, 'Store in l0f05', align=Align.INLINE)
d.comment(0xA029, 'Y=3: TX buffer command byte', align=Align.INLINE)
d.comment(0xA02A, 'Send TX control block', align=Align.INLINE)
d.comment(0xA02D, 'Store X (0) in fs_load_addr_hi', align=Align.INLINE)
d.comment(0xA02F, 'Load data offset from l0f06', align=Align.INLINE)
d.comment(0xA032, 'Store as first byte of FS options', align=Align.INLINE)
d.comment(0xA034, 'Load data count from l0f05', align=Align.INLINE)
d.comment(0xA037, 'Y=9: position offset in FS options', align=Align.INLINE)
d.comment(0xA039, 'Add to current position', align=Align.INLINE)
d.comment(0xA03B, 'Store updated position', align=Align.INLINE)
d.comment(0xA03D, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0xA03F, 'Subtract 7 (header overhead)', align=Align.INLINE)
d.comment(0xA041, 'Store remaining data size', align=Align.INLINE)
d.comment(0xA044, 'Store in fs_load_addr_2 (byte count)', align=Align.INLINE)
d.comment(0xA046, 'Zero bytes: skip write', align=Align.INLINE)
d.comment(0xA048, 'Write data block to host/tube', align=Align.INLINE)
d.comment(0xA04B, 'X=2: clear 3 bytes (indices 0-2)', align=Align.INLINE)
d.comment(0xA04D, 'Clear l0f07+X', align=Align.INLINE)
d.comment(0xA050, 'Decrement index', align=Align.INLINE)
d.comment(0xA051, 'Loop until all cleared', align=Align.INLINE)
d.comment(0xA053, 'Update addresses from offset 1', align=Align.INLINE)
d.comment(0xA056, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xA057, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0xA059, 'Load data count from l0f05', align=Align.INLINE)
d.comment(0xA05C, 'Copy to l0f06', align=Align.INLINE)
d.comment(0xA05F, 'Adjust FS options by 4 bytes (subtract)', align=Align.INLINE)
d.comment(0xA062, 'X=3: check 4 bytes', align=Align.INLINE)
d.comment(0xA064, 'Y=5: starting offset', align=Align.INLINE)
d.comment(0xA066, 'Set carry for comparison', align=Align.INLINE)
d.comment(0xA067, 'Load FS options byte', align=Align.INLINE)
d.comment(0xA069, 'Non-zero: more data remaining', align=Align.INLINE)
d.comment(0xA06B, 'Advance to next byte', align=Align.INLINE)
d.comment(0xA06C, 'Decrement counter', align=Align.INLINE)
d.comment(0xA06D, 'Loop until all bytes checked', align=Align.INLINE)
d.comment(0xA06F, 'All zero: clear carry (transfer complete)', align=Align.INLINE)
d.comment(0xA070, 'Jump to update catalogue and return', align=Align.INLINE)
d.comment(0xA073, 'A=&C3: tube claim protocol', align=Align.INLINE)
d.comment(0xA075, 'Dispatch tube address/data claim', align=Align.INLINE)
d.comment(0xA078, 'Carry clear: claim failed, retry', align=Align.INLINE)
d.comment(0xA07A, 'Return (tube claimed)', align=Align.INLINE)
d.comment(0xBE94, """Resume normal ROM address space

The preceding 512 bytes are the source data for
two relocated code blocks (see move() calls):
  page 5 source -> &0500-&05FF (Tube host code)
  page 6 source -> &0600-&06FF (Econet handlers)
py8dis assembles those blocks at their runtime
addresses (&0500/&0600) via org directives. This
org restores the origin to the actual ROM address
for the remaining non-relocated code.""")
d.comment(0xBE94, 'Store BRK vector high byte', align=Align.INLINE)
d.comment(0xBE97, 'A=&8E: Tube control register value', align=Align.INLINE)
d.comment(0xBE99, 'Write Tube control register', align=Align.INLINE)
d.comment(0xBE9C, 'Y=0: copy 256 bytes per page', align=Align.INLINE)
d.comment(0xBE9E, 'Load page 4 source byte', align=Align.INLINE)
d.comment(0xBEA1, 'Store to page 4 destination', align=Align.INLINE)
d.comment(0xBEA4, 'Load page 5 source byte', align=Align.INLINE)
d.comment(0xBEA7, 'Store to page 5 destination', align=Align.INLINE)
d.comment(0xBEAA, 'Load page 6 source byte', align=Align.INLINE)
d.comment(0xBEAD, 'Store to page 6 destination', align=Align.INLINE)
d.comment(0xBEB0, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xBEB1, 'Non-zero: continue copying', align=Align.INLINE)
d.comment(0xBEB3, 'Clear tube claim state', align=Align.INLINE)
d.comment(0xBEB6, 'X=&41: copy 66 bytes of ZP workspace', align=Align.INLINE)
d.comment(0xBEB8, 'Load ZP source byte from ROM', align=Align.INLINE)
d.comment(0xBEBB, 'Store to NMI workspace at &16+X', align=Align.INLINE)
d.comment(0xBEBD, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xBEBE, 'More bytes: continue copying', align=Align.INLINE)
d.comment(0xBEC0, 'A=0: return success', align=Align.INLINE)
d.comment(0xBEC2, 'Return to caller', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'anfs-4.18.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'anfs-4.18.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
