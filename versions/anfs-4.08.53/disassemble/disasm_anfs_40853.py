import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook, stringz_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'anfs-4.08.53.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='6502', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.add_move(0x0016, 0xBEBF, 0x42)
d.add_move(0x0400, 0xBF00, 0x100)
d.add_move(0x0500, 0xBC90, 0x100)
d.add_move(0x0600, 0xBD90, 0x100)

d.label(0xBEBF, 'reloc_zp_src')

d.label(0xBF00, 'reloc_p4_src')

d.label(0xBC90, 'reloc_p5_src')

d.label(0xBD90, 'reloc_p6_src')
d.byte(0xBC8F)
d.use_environment('acorn_mos')
d.use_environment('acorn_model_b_hardware')
d.use_environment('acorn_sideways_rom')
d.hook_subroutine(0x9131, 'print_inline', stringhi_hook)
d.hook_subroutine(0x96BE, 'error_inline', stringz_hook)
d.hook_subroutine(0x96BB, 'error_inline_log', stringz_hook)
d.hook_subroutine(0x96A2, 'error_bad_inline', stringz_hook)
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

d.label(0x0D6D, 'net_context')

d.label(0x0D6E, 'tx_retry_count')

d.label(0x0D6F, 'rx_poll_count')

d.label(0x0D70, 'peek_retry_count')

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

d.label(0x802D, 'save_registers')

d.label(0x8052, 'set_jsr_protection')

d.label(0x8085, 'econet_restore')

d.label(0x80B2, 'adlc_init_done')

d.label(0x83DA, 'loop_count_rxcb_slot')
d.expr_label(0x83FD, 'imm_op_dispatch_lo-&81')

d.label(0x8405, 'return_from_discard_reset')

d.label(0x84A1, 'jmp_send_data_rx_ack')

d.label(0x84B1, 'set_rx_buf_len_hi')

d.label(0x8533, 'return_from_advance_buf')

d.label(0x85F1, 'reload_inactive_mask')

d.label(0x85F6, 'intoff_disable_nmi_op')

d.label(0x87BD, 'tx_check_tdra_ready')

d.label(0x87E8, 'check_tdra_status')

d.label(0x88F7, 'check_tx_in_progress')

d.label(0x8A29, 'clear_workspace_byte')

d.label(0x8A2E, 'restore_rom_slot')

d.label(0x8A32, 'dispatch_service')

d.label(0x8A49, 'set_adlc_absent')

d.label(0x8A50, 'check_adlc_flag')

d.label(0x8A58, 'handle_vectors_claimed')

d.label(0x8A65, 'init_rom_scan')

d.label(0x8A68, 'loop_scan_net_roms')

d.label(0x8A90, 'next_rom_slot')

d.label(0x8A9F, 'dispatch_svc_with_state')

d.label(0x8AB2, 'dispatch_svc_index')

d.label(0x8AC3, 'restore_svc_state')

d.label(0x8AC9, 'restore_romsel_rts')

d.label(0x8AE6, 'loop_scan_key_range')

d.label(0x8AF3, 'clear_svc_and_ws')

d.label(0x8B04, 'return_from_save_text_ptr')

d.label(0x8B1A, 'loop_sum_rom_bytes')

d.label(0x8B28, 'done_rom_checksum')

d.label(0x8B2D, 'loop_copy_fs_ctx')

d.label(0x8B40, 'loop_set_vectors')

d.label(0x8B6F, 'loop_copy_ws_page')

d.label(0x8B9D, 'print_table_newline')

d.label(0x8BA3, 'loop_next_entry')

d.label(0x8BAB, 'print_indent')

d.label(0x8BB5, 'loop_print_name')

d.label(0x8BBF, 'loop_pad_spaces')

d.label(0x8BD5, 'loop_print_syntax')

d.label(0x8BE5, 'print_syntax_char')

d.label(0x8BEB, 'print_shared_prefix')

d.label(0x8BF5, 'loop_next_shared')

d.label(0x8BFB, 'loop_print_shared')

d.label(0x8C07, 'print_last_char')

d.label(0x8C14, 'skip_syntax_bytes')

d.label(0x8C19, 'done_shared_cmds')

d.label(0x8C1B, 'done_entry_newline')

d.label(0x8C24, 'done_print_table')

d.label(0x8C3A, 'loop_indent_spaces')

d.label(0x8C42, 'return_from_help_wrap')

d.label(0x8C65, 'svc_return_unclaimed')

d.label(0x8C68, 'check_help_topic')

d.label(0x8C72, 'match_help_topic')

d.label(0x8C75, 'loop_dispatch_help')

d.label(0x8C8D, 'skip_if_no_match')

d.label(0x8C97, 'version_string_cr')

d.label(0x8CBE, 'return_from_setup_ws_ptr')

d.label(0x8CCF, 'write_key_state')

d.label(0x8CD5, 'select_net_fs')

d.label(0x8CFF, 'issue_svc_osbyte')

d.label(0x8D10, 'loop_match_credits')

d.label(0x8D1B, 'done_credits_check')

d.label(0x8D21, 'loop_emit_credits')

d.label(0x8D2C, 'return_from_credits_check')

d.label(0x8D2D, 'credits_keyword_start')

d.label(0x8D4B, 'ps_template_base')

d.label(0x8D9C, 'skip_no_fs_addr')

d.label(0x8DA3, 'loop_copy_logon_cmd')

d.label(0x8DB4, 'scan_pass_prompt')

d.label(0x8DB6, 'loop_scan_colon')

d.label(0x8DC7, 'read_pw_char')

d.label(0x8DD9, 'loop_erase_pw')

d.label(0x8DE0, 'check_pw_special')

d.label(0x8DEF, 'send_pass_to_fs')

d.label(0x8E3E, 'svc_dispatch_lo_offset')

d.label(0x8E42, 'dispatch_rts')

d.label(0x8E71, 'jmp_osbyte')

d.label(0x8E95, 'return_from_svc_1_workspace')

d.label(0x8E9D, 'done_cap_ws_count')

d.label(0x8ED5, 'loop_zero_workspace')

d.label(0x8EFF, 'loop_copy_init_data')

d.label(0x8F11, 'loop_alloc_handles')

d.label(0x8F23, 'read_station_id')

d.label(0x8F29, 'error_bad_station')

d.label(0x8F2B, 'ws_init_data')
for i in range(3):
    d.byte(0x8F2C + i)

d.label(0x8F2F, 'store_station_id')

d.label(0x8F75, 'loop_restore_ctx')

d.label(0x8F97, 'loop_checksum_byte')

d.label(0x8FA1, 'loop_copy_to_ws')

d.label(0x8FA4, 'store_ws_byte')

d.label(0x8FB1, 'return_from_fs_shutdown')

d.label(0x8FBB, 'loop_sum_ws')

d.label(0x900A, 'done_print_newline')

d.label(0x900E, 'cmd_syntax_strings')

d.label(0x900E, 'syn_opt_dir')

d.label(0x9016, 'syn_iam')

d.label(0x9043, 'syn_object')

d.label(0x904C, 'syn_file_offset')

d.label(0x906F, 'syn_dir')

d.label(0x9075, 'syn_dir_num')

d.label(0x9086, 'syn_password')

d.label(0x90A9, 'syn_ps_type')

d.label(0x90C0, 'syn_access')

d.label(0x90DC, 'syn_rename')

d.label(0x90F6, 'syn_opt_stn')

d.label(0x9103, 'syn_filename')

d.label(0x910E, 'cmd_syntax_table')
for i in range(13):
    d.byte(0x910E + i)
d.expr(0x910E, 'syn_iam - cmd_syntax_strings - 2')
d.expr(0x910F, '(syn_opt_dir - cmd_syntax_strings - 1) AND &FF')
d.expr(0x9110, 'syn_iam - cmd_syntax_strings - 1')
d.expr(0x9111, 'syn_object - cmd_syntax_strings - 1')
d.expr(0x9112, 'syn_file_offset - cmd_syntax_strings - 1')
d.expr(0x9113, 'syn_dir - cmd_syntax_strings - 1')
d.expr(0x9114, 'syn_dir_num - cmd_syntax_strings - 1')
d.expr(0x9115, 'syn_password - cmd_syntax_strings - 1')
d.expr(0x9116, 'syn_ps_type - cmd_syntax_strings - 1')
d.expr(0x9117, 'syn_access - cmd_syntax_strings - 1')
d.expr(0x9118, 'syn_rename - cmd_syntax_strings - 1')
d.expr(0x9119, 'syn_opt_stn - cmd_syntax_strings - 1')
d.expr(0x911A, 'syn_filename - cmd_syntax_strings - 1')

d.label(0x912C, 'add_ascii_base')

d.label(0x9139, 'loop_next_char')

d.label(0x913F, 'load_char')

d.label(0x9157, 'resume_caller')

d.label(0x9169, 'next_hex_char')

d.label(0x9174, 'check_digit_range')

d.label(0x9184, 'skip_if_not_hex')

d.label(0x9186, 'extract_digit_value')

d.label(0x919A, 'next_dec_char')

d.label(0x91C6, 'done_parse_num')

d.label(0x91CF, 'validate_station')

d.label(0x91E5, 'return_parsed')

d.label(0x91E7, 'handle_dot_sep')

d.label(0x91FD, 'error_overflow')

d.label(0x9215, 'error_bad_number')

d.label(0x9221, 'error_bad_param')

d.label(0x9230, 'error_bad_net_num')

d.label(0x9252, 'return_from_digit_test')

d.label(0x9253, 'not_a_digit')

d.label(0x9263, 'begin_prot_encode')

d.label(0x9267, 'loop_encode_prot')

d.label(0x926F, 'skip_clear_prot')

d.label(0x9272, 'prot_bit_encode_table')
for i in range(11):
    d.byte(0x9272 + i)

d.label(0x9292, 'loop_cmp_handle')

d.label(0x929B, 'return_from_cmp_handle')

d.label(0x929C, 'fscv_7_read_handles')

d.label(0x92CD, 'done_conn_flag')

d.label(0x9315, 'loop_scan_flag')

d.label(0x931E, 'loop_copy_name')

d.label(0x932A, 'append_space')

d.label(0x9334, 'return_from_copy_cmd_name')

d.label(0x933B, 'loop_skip_spaces')

d.label(0x9344, 'check_open_quote')

d.label(0x934F, 'loop_copy_arg_char')

d.label(0x935D, 'store_arg_char')

d.label(0x9387, 'loop_copy_rename')

d.label(0x938E, 'error_bad_rename')

d.label(0x939A, 'store_rename_char')

d.label(0x93A8, 'skip_rename_spaces')

d.label(0x93DA, 'setup_fs_root')

d.label(0x93DC, 'loop_copy_fs_num')

d.label(0x93F1, 'check_fs_dot')

d.label(0x93F8, 'parse_fs_dot_dir')

d.label(0x9428, 'dir_found_send')

d.label(0x944E, 'dir_pass_simple')

d.label(0x9462, 'loop_init_txcb')

d.label(0x9472, 'skip_txcb_dest')

d.label(0x9477, 'txcb_init_template')
for i in range(12):
    d.byte(0x9477 + i)

d.label(0x947D, 'bit_test_ff')

d.label(0x94A0, 'txcb_copy_carry_clr')

d.label(0x94A1, 'txcb_copy_carry_set')

d.label(0x94A7, 'loop_copy_vset_stn')

d.label(0x94BF, 'use_lib_station')

d.label(0x94C5, 'done_vset_station')

d.label(0x94E4, 'loop_next_reply')

d.label(0x94EE, 'process_reply_code')

d.label(0x94F0, 'return_from_recv_reply')

d.label(0x94F1, 'handle_disconnect')

d.label(0x94FA, 'store_reply_status')

d.label(0x9506, 'check_data_loss')

d.label(0x950B, 'loop_scan_channels')

d.label(0x952F, 'reload_reply_status')

d.label(0x953B, 'build_error_block')

d.label(0x9545, 'setup_error_copy')

d.label(0x9547, 'loop_copy_error')

d.label(0x956A, 'lang_1_remote_boot')

d.label(0x9570, 'done_commit_state')

d.label(0x9573, 'init_remote_session')

d.label(0x9598, 'lang_3_execute_at_0100')

d.label(0x95A8, 'lang_4_remote_validated')

d.label(0x95B8, 'lang_0_insert_remote_key')

d.label(0x95D8, 'init_poll_counters')

d.label(0x95DE, 'loop_poll_tx')

d.label(0x95F1, 'done_poll_tx')

d.label(0x9603, 'return_from_cond_save_err')

d.label(0x9604, 'build_no_reply_error')

d.label(0x9614, 'loop_copy_no_reply_msg')

d.label(0x9620, 'done_no_reply_msg')

d.label(0x9633, 'skip_if_not_a')

d.label(0x963B, 'mask_error_class')

d.label(0x9652, 'loop_copy_station_msg')

d.label(0x965E, 'done_station_msg')

d.label(0x9670, 'suffix_not_listening')

d.label(0x9672, 'load_suffix_offset')

d.label(0x9676, 'loop_copy_suffix')

d.label(0x9682, 'done_suffix')

d.label(0x9684, 'build_simple_error')

d.label(0x9693, 'loop_copy_error_msg')

d.label(0x9699, 'check_msg_terminator')

d.label(0x96AE, 'loop_copy_bad_prefix')

d.label(0x96C7, 'write_error_num_and_str')

d.label(0x96D1, 'loop_copy_inline_str')

d.label(0x96E5, 'trigger_brk')

d.label(0x96E8, 'handle_net_error')

d.label(0x970A, 'close_exec_file')

d.label(0x970D, 'close_spool_exec')

d.label(0x9717, 'done_close_files')

d.label(0x971F, 'loop_copy_channel_msg')

d.label(0x972B, 'append_error_number')

d.label(0x9752, 'append_station_num')

d.label(0x977F, 'loop_count_digit')

d.label(0x978F, 'store_digit')

d.label(0x9797, 'return_from_store_digit')

d.label(0x9798, 'net_error_lookup_data')
for i in range(12):
    d.byte(0x9798 + i)
d.expr(0x9798, 'error_msg_table - error_msg_table')
d.expr(0x9799, 'msg_net_error - error_msg_table')
d.expr(0x979A, 'msg_station - error_msg_table')
d.expr(0x979B, 'msg_no_clock - error_msg_table')
d.expr(0x979C, 'msg_escape - error_msg_table')
d.expr(0x979D, 'msg_escape - error_msg_table')
d.expr(0x979E, 'msg_escape - error_msg_table')
d.expr(0x979F, 'msg_bad_option - error_msg_table')
d.expr(0x97A0, 'msg_no_reply - error_msg_table')
d.expr(0x97A1, 'msg_not_listening - error_msg_table')
d.expr(0x97A2, 'msg_on_channel - error_msg_table')
d.expr(0x97A3, 'msg_not_present - error_msg_table')

d.label(0x9831, 'set_timeout')

d.label(0x983A, 'start_tx_attempt')

d.label(0x9850, 'loop_retry_tx')

d.label(0x9856, 'loop_tx_delay')

d.label(0x985E, 'try_alternate_phase')

d.label(0x9869, 'tx_send_error')

d.label(0x986D, 'tx_success')

d.label(0x9873, 'pass_txbuf_init_table')
for i in range(12):
    d.byte(0x9873 + i)

d.label(0x9889, 'loop_copy_template')

d.label(0x9896, 'skip_template_byte')

d.label(0x98A3, 'start_pass_tx')

d.label(0x98AF, 'done_pass_retries')

d.label(0x98C4, 'loop_poll_pass_tx')

d.label(0x98C9, 'restore_retry_state')

d.label(0x98D6, 'loop_pass_tx_delay')

d.label(0x98DE, 'pass_tx_success')

d.label(0x98E3, 'loop_restore_txbuf')

d.label(0x98ED, 'skip_restore_byte')

d.label(0x98F5, 'loop_copy_text_ptr')

d.label(0x9907, 'loop_gsread_char')

d.label(0x9912, 'terminate_buf')

d.label(0x9938, 'copy_arg_and_enum')

d.label(0x9955, 'copy_ws_then_fsopts')

d.label(0x995B, 'setup_txcb_addrs')

d.label(0x995D, 'loop_copy_addrs')

d.label(0x9978, 'loop_copy_offsets')

d.label(0x998D, 'loop_swap_and_send')

d.label(0x998F, 'loop_copy_start_end')

d.label(0x99A3, 'loop_verify_addrs')

d.label(0x99AE, 'return_from_txcb_swap')

d.label(0x99AF, 'check_display_type')

d.label(0x99B4, 'setup_dir_display')

d.label(0x99B9, 'loop_compute_diffs')

d.label(0x99D7, 'loop_copy_fs_options')

d.label(0x99F8, 'send_info_request')

d.label(0x9A05, 'setup_txcb_transfer')

d.label(0x9A0B, 'recv_reply')

d.label(0x9A0E, 'store_result')

d.label(0x9A1B, 'loop_copy_file_info')

d.label(0x9A1E, 'store_prot_byte')

d.label(0x9A2C, 'loop_print_filename')

d.label(0x9A52, 'loop_print_hex_byte')

d.label(0x9A62, 'loop_copy_fsopts_byte')

d.label(0x9A71, 'return_from_advance_y')

d.label(0x9A75, 'loop_copy_ws_byte')

d.label(0x9A84, 'discard_handle_match')

d.label(0x9A8E, 'init_transfer_addrs')

d.label(0x9A99, 'loop_copy_addr_offset')

d.label(0x9AAB, 'loop_check_vs_limit')

d.label(0x9AB7, 'clamp_end_to_limit')

d.label(0x9AB9, 'loop_copy_limit')

d.label(0x9AC0, 'set_port_and_ctrl')

d.label(0x9ADD, 'dispatch_osword_op')

d.label(0x9AE9, 'dispatch_ops_1_to_6')

d.label(0x9B01, 'loop_copy_fsopts_4')

d.label(0x9B0E, 'setup_save_access')

d.label(0x9B18, 'loop_copy_fsopts_8')

d.label(0x9B23, 'send_save_or_access')

d.label(0x9B2A, 'send_delete_request')

d.label(0x9B2F, 'send_request_vset')

d.label(0x9B35, 'skip_if_error')

d.label(0x9B3A, 'setup_write_access')

d.label(0x9B44, 'read_cat_info')

d.label(0x9B66, 'loop_copy_cat_info')

d.label(0x9B73, 'loop_copy_ext_info')

d.label(0x9B7F, 'return_with_handle')

d.label(0x9B80, 'done_osword_op')

d.label(0x9B8D, 'loop_copy_cmdline_char')

d.label(0x9B99, 'pad_with_spaces')

d.label(0x9BA4, 'loop_copy_buf_char')

d.label(0x9BA6, 'copy_from_buf_entry')

d.label(0x9BC1, 'validate_chan_close')

d.label(0x9BC6, 'error_invalid_chan')

d.label(0x9BC9, 'check_chan_range')

d.label(0x9BD9, 'loop_copy_fcb_fields')

d.label(0x9BE9, 'dispatch_osfind_op')

d.label(0x9BF4, 'osfind_with_channel')

d.label(0x9C27, 'loop_copy_zp_to_buf')

d.label(0x9C3D, 'done_return_flag')

d.label(0x9C40, 'osargs_read_op')

d.label(0x9C4F, 'loop_copy_reply_to_zp')

d.label(0x9C5C, 'osargs_ptr_dispatch')

d.label(0x9C7E, 'osargs_write_ptr')

d.label(0x9C85, 'loop_copy_ptr_to_buf')

d.label(0x9CB6, 'close_all_fcbs')

d.label(0x9CC8, 'osfind_close_or_open')

d.label(0x9CD3, 'loop_copy_reply_data')

d.label(0x9CDF, 'done_file_open')

d.label(0x9CE1, 'clear_result')

d.label(0x9CE3, 'shift_and_finalise')

d.label(0x9CE6, 'alloc_fcb_for_open')

d.label(0x9D1E, 'loop_shift_filename')

d.label(0x9D5F, 'check_open_mode')

d.label(0x9D71, 'alloc_fcb_with_flags')

d.label(0x9D75, 'store_fcb_flags')

d.label(0x9D7B, 'done_osfind')

d.label(0x9D7E, 'close_all_channels')

d.label(0x9D97, 'close_specific_chan')

d.label(0x9D9D, 'send_close_request')

d.label(0x9DAF, 'done_close')

d.label(0x9DB2, 'clear_single_fcb')

d.label(0x9DBC, 'fscv_0_opt_entry')

d.label(0x9DC6, 'osargs_dispatch')

d.label(0x9DC9, 'store_display_flag')

d.label(0x9DCE, 'error_osargs')

d.label(0x9DD3, 'send_osargs_request')

d.label(0x9DE2, 'fscv_1_eof')

d.label(0x9DFD, 'mark_not_found')

d.label(0x9DFF, 'restore_and_return')

d.label(0x9E0D, 'loop_adjust_byte')

d.label(0x9E19, 'subtract_ws_byte')

d.label(0x9E1C, 'store_adjusted_byte')

d.label(0x9E36, 'skip_if_out_of_range')

d.label(0x9E39, 'valid_osgbpb_op')

d.label(0x9E44, 'load_chan_handle')

d.label(0x9E83, 'set_write_active')

d.label(0x9E86, 'setup_gbpb_request')

d.label(0x9ED6, 'loop_copy_opts_to_buf')

d.label(0x9EE1, 'skip_struct_hole')

d.label(0x9EEA, 'store_direction_flag')

d.label(0x9EF8, 'store_port_and_send')

d.label(0x9F15, 'loop_setup_addr_bytes')

d.label(0x9F2C, 'loop_copy_offset')

d.label(0x9F40, 'send_with_swap')

d.label(0x9F43, 'recv_and_update')

d.label(0x9F55, 'send_osbput_data')

d.label(0x9F6A, 'write_block_entry')

d.label(0x9F78, 'store_station_result')

d.label(0x9F7A, 'loop_copy_opts_to_ws')

d.label(0x9F8C, 'handle_cat_update')

d.label(0x9FC0, 'loop_copy_to_host')

d.label(0x9FCD, 'tube_write_setup')

d.label(0x9FDA, 'set_tube_addr')

d.label(0x9FDF, 'loop_write_to_tube')

d.label(0x9FE8, 'loop_tube_delay')

d.label(0x9FF7, 'update_cat_position')

d.label(0xA033, 'clear_buf_after_write')

d.label(0xA035, 'loop_clear_buf')

d.label(0xA04F, 'loop_check_remaining')

d.label(0xA058, 'done_write_block')

d.label(0xA083, 'print_current_fs')

d.label(0xA0A5, 'store_station_lo')

d.label(0xA0AD, 'skip_if_no_station')

d.label(0xA0B1, 'done_parse_fs_ps')

d.label(0xA0CC, 'net_1_read_handle')

d.label(0xA0D2, 'net_2_read_handle_entry')

d.label(0xA0DD, 'return_zero_uninit')

d.label(0xA0DF, 'store_pb_result')

d.label(0xA0E2, 'net_3_close_handle')

d.label(0xA0F1, 'mark_ws_uninit')

d.label(0xA11B, 'dispatch_fs_cmd')

d.label(0xA12A, 'restart_table_scan')

d.label(0xA132, 'loop_match_char')

d.label(0xA141, 'skip_entry_chars')

d.label(0xA14D, 'loop_skip_to_next')

d.label(0xA152, 'check_separator')

d.label(0xA158, 'loop_check_sep_table')

d.label(0xA164, 'sep_table_data')
for i in range(9):
    d.byte(0xA164 + i)

d.label(0xA16D, 'separator_matched')

d.label(0xA16F, 'loop_skip_trail_spaces')

d.label(0xA175, 'skip_dot_and_spaces')

d.label(0xA179, 'check_cmd_flags')

d.label(0xA18A, 'clear_v_flag')

d.label(0xA18B, 'clear_c_flag')

d.label(0xA18C, 'return_with_result')

d.label(0xA190, 'loop_scan_past_word')

d.label(0xA191, 'check_char_type')

d.label(0xA19F, 'skip_sep_spaces')

d.label(0xA1A6, 'set_c_and_return')

d.label(0xA1A9, 'fscv_2_star_run')

d.label(0xA1B2, 'open_file_for_run')

d.label(0xA1CA, 'loop_check_handles')

d.label(0xA1D2, 'alloc_run_fcb')

d.label(0xA1EE, 'done_run_dispatch')

d.label(0xA1F1, 'try_library_path')

d.label(0xA205, 'loop_find_name_end')

d.label(0xA20D, 'loop_shift_name_right')

d.label(0xA218, 'loop_copy_lib_prefix')

d.label(0xA229, 'retry_with_library')

d.label(0xA22B, 'restore_filename')

d.label(0xA22D, 'loop_restore_name')

d.label(0xA242, 'library_tried')

d.label(0xA252, 'check_exec_addr')

d.label(0xA254, 'loop_check_exec_bytes')

d.label(0xA265, 'alloc_run_channel')

d.label(0xA279, 'library_dir_prefix')

d.label(0xA281, 'setup_oscli_arg')

d.label(0xA28A, 'loop_read_gs_string')

d.label(0xA290, 'loop_skip_trailing')

d.label(0xA2D7, 'dispatch_via_vector')

d.label(0xA2E2, 'fsreply_5_set_lib')

d.label(0xA2EB, 'loop_search_stn_bit2')

d.label(0xA301, 'done_search_bit2')

d.label(0xA30F, 'set_flags_bit2')

d.label(0xA316, 'loop_search_stn_bit3')

d.label(0xA32C, 'done_search_bit3')

d.label(0xA33A, 'set_flags_bit3')

d.label(0xA34D, 'loop_search_stn_boot')

d.label(0xA363, 'done_search_boot')

d.label(0xA371, 'set_flags_boot')

d.label(0xA373, 'store_stn_flags_restore')

d.label(0xA376, 'jmp_restore_fs_ctx')

d.label(0xA379, 'fsreply_1_copy_handles_boot')

d.label(0xA383, 'fsreply_2_copy_handles')

d.label(0xA39C, 'check_auto_boot_flag')

d.label(0xA3C7, 'boot_oscli_lo_table')
for i in range(4):
    d.byte(0xA3C7 + i)

d.label(0xA3CB, 'load_boot_type')

d.label(0xA3D9, 'cmd_table_fs_lo')

d.label(0xA3DA, 'cmd_table_fs_hi')

d.label(0xA45F, 'cmd_table_nfs_iam')

d.label(0xA4E6, 'loop_copy_osword_data')

d.label(0xA4FA, 'loop_copy_osword_flag')

d.label(0xA507, 'return_from_osword_setup')
d.comment(0xA508, """OSWORD dispatch table (7 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_8_osword.
Maps OSWORD codes &0E-&14 to handler routines.""")

d.label(0xA508, 'osword_dispatch_lo_table')

d.label(0xA50F, 'osword_dispatch_hi_table')
for i in range(7):
    d.rts_code_ptr(0xA508 + i, 0xA50F + i)
d.comment(0xA508, 'lo-&0E: Read clock', align=Align.INLINE)
d.comment(0xA509, 'lo-&0F: (unimplemented)', align=Align.INLINE)
d.comment(0xA50A, 'lo-&10: Transmit', align=Align.INLINE)
d.comment(0xA50B, 'lo-&11: Receive', align=Align.INLINE)
d.comment(0xA50C, 'lo-&12: Read station info', align=Align.INLINE)
d.comment(0xA50D, 'lo-&13: Misc operations', align=Align.INLINE)
d.comment(0xA50E, 'lo-&14: Bridge/net config', align=Align.INLINE)
d.comment(0xA50F, 'hi-&0E: Read clock', align=Align.INLINE)
d.comment(0xA510, 'hi-&0F: (unimplemented)', align=Align.INLINE)
d.comment(0xA511, 'hi-&10: Transmit', align=Align.INLINE)
d.comment(0xA512, 'hi-&11: Receive', align=Align.INLINE)
d.comment(0xA513, 'hi-&12: Read station info', align=Align.INLINE)
d.comment(0xA514, 'hi-&13: Misc operations', align=Align.INLINE)
d.comment(0xA515, 'hi-&14: Bridge/net config', align=Align.INLINE)

d.label(0xA516, 'osword_0e_handler')

d.label(0xA525, 'return_from_osword_0e')

d.label(0xA526, 'save_txcb_and_convert')

d.label(0xA573, 'loop_copy_bcd_to_pb')

d.label(0xA583, 'loop_bcd_add')

d.label(0xA589, 'done_bcd_convert')

d.label(0xA58B, 'osword_10_handler')

d.label(0xA594, 'setup_ws_rx_ptrs')

d.label(0xA5A8, 'osword_11_handler')

d.label(0xA5B9, 'loop_find_rx_slot')

d.label(0xA5CD, 'store_rx_slot_found')

d.label(0xA5D2, 'use_specified_slot')

d.label(0xA5E8, 'loop_copy_slot_data')

d.label(0xA5E9, 'copy_pb_and_mark')

d.label(0xA5F6, 'increment_and_retry')

d.label(0xA5FB, 'store_rx_result')

d.label(0xA5FD, 'osword_11_done')

d.label(0xA61C, 'osword_12_handler')

d.label(0xA631, 'osword_13_dispatch')

d.label(0xA63E, 'return_from_osword_13')

d.label(0xA63F, 'osword_13_lo_table')

d.label(0xA651, 'osword_13_hi_table')
for i in range(18):
    d.rts_code_ptr(0xA63F + i, 0xA651 + i)
d.entry(0xA663)
d.entry(0xA676)
d.entry(0xA6EB)
d.entry(0xA6EE)

d.label(0xA668, 'nfs_inactive_exit')

d.label(0xA66B, 'read_station_bytes')

d.label(0xA66D, 'loop_copy_station')

d.label(0xA682, 'loop_store_station')

d.label(0xA68F, 'scan_fcb_entry')

d.label(0xA6B9, 'check_handle_2')

d.label(0xA6CE, 'check_handle_3')

d.label(0xA6E3, 'store_updated_status')

d.label(0xA6E7, 'next_fcb_entry')

d.label(0xA6EF, 'setup_csd_copy')

d.label(0xA701, 'copy_ws_byte_to_pb')

d.label(0xA72A, 'return_from_write_ws_pair')

d.label(0xA73E, 'loop_copy_handles')

d.label(0xA74C, 'return_zero_in_pb')

d.label(0xA752, 'start_set_handles')

d.label(0xA754, 'validate_handle')

d.label(0xA764, 'handle_invalid')

d.label(0xA76B, 'check_handle_alloc')

d.label(0xA791, 'next_handle_slot')

d.label(0xA798, 'assign_handle_2')

d.label(0xA7AF, 'assign_handle_3')

d.label(0xA7C6, 'loop_scan_fcb_flags')

d.label(0xA7D8, 'no_flag_match')

d.label(0xA7D9, 'clear_flag_bits')

d.label(0xA7E1, 'next_flag_entry')

d.label(0xA810, 'store_a_to_pb_1')

d.label(0xA83A, 'bridge_found')

d.label(0xA843, 'compare_bridge_status')

d.label(0xA844, 'bridge_ws_init_data')

d.label(0xA84A, 'use_default_station')

d.label(0xA84D, 'store_bridge_station')

d.label(0xA84F, 'return_from_bridge_query')

d.label(0xA850, 'bridge_txcb_init_table')

d.label(0xA85C, 'bridge_rxcb_init_data')
for i in range(4):
    d.byte(0xA850 + i)
for i in range(14):
    d.byte(0xA85A + i)

d.label(0xA878, 'loop_copy_bridge_init')

d.label(0xA88C, 'loop_wait_ws_status')

d.label(0xA8A0, 'loop_wait_tx_done')

d.label(0xA8C0, 'bridge_responded')

d.label(0xA8CF, 'return_from_bridge_poll')

d.label(0xA8D0, 'osword_14_handler')

d.label(0xA8DE, 'loop_copy_txcb_init')

d.label(0xA8E6, 'store_txcb_init_byte')

d.label(0xA8FD, 'loop_copy_ws_to_pb')

d.label(0xA926, 'handle_tx_request')

d.label(0xA93D, 'loop_send_pb_chars')

d.label(0xA950, 'loop_bridge_tx_delay')

d.label(0xA959, 'handle_burst_xfer')

d.label(0xA97A, 'restore_regs_return')

d.label(0xA98C, 'osword_handler_lo_table')

d.label(0xA995, 'osword_handler_hi_table')
for i in range(9):
    d.rts_code_ptr(0xA98C + i, 0xA995 + i)
d.comment(0xA98C, """OSWORD handler dispatch table

9-entry PHA/PHA/RTS table for OSWORD numbers
0-8. push_osword_handler_addr indexes by the
OSWORD number, pushes the handler address-1,
then RTS dispatches to the handler with the
OSWORD number reloaded in A.""")
d.comment(0xA98C, 'lo OSWORD 0: no-op (RTS)', align=Align.INLINE)
d.comment(0xA98D, 'lo OSWORD 1: printer spool data', align=Align.INLINE)
d.comment(0xA98E, 'lo OSWORD 2: printer spool data', align=Align.INLINE)
d.comment(0xA98F, 'lo OSWORD 3: printer spool data', align=Align.INLINE)
d.comment(0xA990, 'lo OSWORD 4: clear carry + abort', align=Align.INLINE)
d.comment(0xA991, 'lo OSWORD 5: spool buffer check', align=Align.INLINE)
d.comment(0xA992, 'lo OSWORD 6: no-op (RTS)', align=Align.INLINE)
d.comment(0xA993, 'lo OSWORD 7: claim/release handler', align=Align.INLINE)
d.comment(0xA994, 'lo OSWORD 8: copy PB + abort', align=Align.INLINE)
d.comment(0xA995, 'hi OSWORD 0: no-op (RTS)', align=Align.INLINE)
d.comment(0xA996, 'hi OSWORD 1: printer spool data', align=Align.INLINE)
d.comment(0xA997, 'hi OSWORD 2: printer spool data', align=Align.INLINE)
d.comment(0xA998, 'hi OSWORD 3: printer spool data', align=Align.INLINE)
d.comment(0xA999, 'hi OSWORD 4: clear carry + abort', align=Align.INLINE)
d.comment(0xA99A, 'hi OSWORD 5: spool buffer check', align=Align.INLINE)
d.comment(0xA99B, 'hi OSWORD 6: no-op (RTS)', align=Align.INLINE)
d.comment(0xA99C, 'hi OSWORD 7: claim/release handler', align=Align.INLINE)
d.comment(0xA99D, 'hi OSWORD 8: copy PB + abort', align=Align.INLINE)

d.label(0xA9D0, 'netv_claim_release')

d.label(0xA9E9, 'process_match_result')

d.label(0xA9F2, 'save_tube_state')

d.label(0xA9F4, 'loop_save_tube_bytes')

d.label(0xAA0B, 'loop_poll_ws_status')

d.label(0xAA18, 'loop_restore_stack')

d.label(0xAA1C, 'store_stack_byte')

d.label(0xAA23, 'return_from_claim_release')

d.label(0xAA2C, 'return_from_match_rx_code')

d.label(0xAA2D, 'osword_claim_codes')
for i in range(18):
    d.byte(0xAA2D + i)

d.label(0xAA49, 'copy_pb_to_ws')

d.label(0xAA4D, 'loop_copy_pb_to_ws')

d.label(0xAA78, 'loop_copy_ws_template')

d.label(0xAA8D, 'store_tx_ptr_hi')

d.label(0xAA8F, 'select_store_target')

d.label(0xAA95, 'store_via_rx_ptr')

d.label(0xAA97, 'advance_template_idx')

d.label(0xAA9B, 'done_ws_template_copy')

d.label(0xAA9F, 'ws_txcb_template_data')
for i in range(39):
    d.byte(0xAA9F + i)

d.label(0xAAC6, 'netv_spool_check')

d.label(0xAADA, 'return_from_spool_reset')

d.label(0xAADB, 'netv_print_data')

d.label(0xAAEA, 'loop_drain_printer_buf')

d.label(0xAB21, 'done_spool_ctrl')

d.label(0xAB63, 'check_spool_state')

d.label(0xAB72, 'start_spool_retry')

d.label(0xAB77, 'loop_copy_spool_tx')

d.label(0xAB96, 'loop_copy_spool_rx')

d.label(0xABA3, 'store_spool_rx_byte')

d.label(0xABA5, 'advance_spool_rx_idx')

d.label(0xABCC, 'spool_tx_succeeded')

d.label(0xABE1, 'spool_tx_retry')

d.label(0xABFE, 'error_printer_jammed')

d.label(0xAC1E, 'loop_scan_disconnect')

d.label(0xAC2D, 'verify_stn_match')

d.label(0xAC38, 'send_disconnect_status')

d.label(0xAC55, 'store_tx_ctrl_byte')

d.label(0xAC5D, 'loop_wait_disc_tx_ack')

d.label(0xAC6E, 'tx_econet_txcb_template')
for i in range(12):
    d.byte(0xAC6E + i)

d.label(0xAC7A, 'rx_palette_txcb_template')
for i in range(12):
    d.byte(0xAC7A + i)

d.label(0xAC86, 'lang_2_save_palette_vdu')

d.label(0xAC9D, 'loop_read_palette')

d.label(0xACFB, 'osbyte_mode_read_codes')
for i in range(3):
    d.byte(0xACFB + i)

d.label(0xAD0E, 'parse_cdir_size')

d.label(0xAD17, 'loop_find_alloc_size')

d.label(0xAD1D, 'done_cdir_size')

d.label(0xAD31, 'cdir_alloc_size_table')
for i in range(27):
    d.byte(0xAD32 + i)

d.label(0xAD5D, 'ex_set_lib_flag')

d.label(0xAD6E, 'fscv_5_cat')

d.label(0xAD77, 'cat_set_lib_flag')

d.label(0xAD84, 'setup_ex_request')

d.label(0xADA0, 'store_owner_flags')

d.label(0xADD1, 'print_public_label')

d.label(0xADDB, 'send_dir_info_req')

d.label(0xAE0A, 'loop_print_option_str')

d.label(0xAE15, 'print_dir_header')

d.label(0xAE3D, 'setup_ex_pagination')

d.label(0xAE5D, 'loop_scan_entry_data')

d.label(0xAE7D, 'jmp_osnewl')

d.label(0xAEA9, 'loop_shift_str_left')

d.label(0xAEB7, 'loop_trim_trailing')

d.label(0xAEC6, 'done_strip_prefix')

d.label(0xAEC8, 'return_from_strip_prefix')

d.label(0xAEC9, 'check_hash_prefix')

d.label(0xAECD, 'error_bad_prefix')

d.label(0xAED0, 'check_colon_prefix')

d.label(0xAEDF, 'set_fs_select_flag')

d.label(0xAEE9, 'option_str_offset_data')

d.label(0xAEED, 'roff_off_string')

d.label(0xAEF5, 'loop_copy_char')

d.label(0xAF05, 'restore_after_check')

d.label(0xAF07, 'advance_positions')

d.label(0xAF1E, 'fsreply_0_print_dir')

d.label(0xAF20, 'loop_scan_entries')

d.label(0xAF3A, 'print_col_newline')

d.label(0xAF3C, 'print_entry_char')

d.label(0xAF3F, 'next_col_entry')

d.label(0xAF52, 'done_extra_arg_check')

d.label(0xAF7D, 'loop_divide_digit')

d.label(0xAF8D, 'print_nonzero_digit')

d.label(0xAFA0, 'loop_advance_char')

d.label(0xAFAD, 'loop_skip_space_chars')

d.label(0xAFD8, 'done_ps_available')

d.label(0xAFFB, 'loop_copy_ps_tmpl')

d.label(0xB005, 'no_ps_name_given')

d.label(0xB008, 'save_ps_cmd_ptr')

d.label(0xB012, 'loop_pad_ps_name')

d.label(0xB02A, 'loop_read_ps_char')

d.label(0xB038, 'done_ps_name_parse')

d.label(0xB04B, 'loop_pop_ps_slot')

d.label(0xB06D, 'done_ps_slot_mark')

d.label(0xB075, 'done_ps_scan')

d.label(0xB08A, 'print_ps_now')

d.label(0xB092, 'done_ps_status_msg')

d.label(0xB095, 'store_ps_station')

d.label(0xB0B6, 'print_server_is_suffix')

d.label(0xB0E4, 'loop_scan_ps_slots')

d.label(0xB0F4, 'skip_next_ps_slot')

d.label(0xB0F8, 'reinit_ps_slot')

d.label(0xB11B, 'write_ps_slot_link_addr')

d.label(0xB120, 'done_ps_slot_scan')

d.label(0xB12F, 'loop_ps_delay')

d.label(0xB14B, 'loop_push_ps_name')

d.label(0xB155, 'loop_pop_ps_name')

d.label(0xB167, 'loop_copy_tx_hdr')

d.label(0xB170, 'ps_tx_header_template')
for i in range(4):
    d.byte(0xB170 + i)

d.label(0xB184, 'skip_if_local_net')

d.label(0xB18D, 'print_station_only')

d.label(0xB193, 'ps_slot_txcb_template')
for i in range(12):
    d.byte(0xB193 + i)

d.label(0xB1E1, 'no_poll_name_given')

d.label(0xB1E4, 'skip_if_no_poll_arg')

d.label(0xB1EC, 'loop_pad_poll_name')

d.label(0xB204, 'loop_read_poll_char')

d.label(0xB212, 'done_poll_name_parse')

d.label(0xB22F, 'loop_print_poll_name')

d.label(0xB23D, 'done_poll_name_print')

d.label(0xB243, 'loop_pop_poll_slot')

d.label(0xB278, 'check_poll_jammed')

d.label(0xB27C, 'print_poll_jammed')

d.label(0xB288, 'check_poll_busy')

d.label(0xB2B8, 'done_poll_status_line')

d.label(0xB2BB, 'done_poll_slot_mark')

d.label(0xB2C6, 'loop_copy_slot_tmpl')

d.label(0xB2D1, 'subst_rx_page_byte')

d.label(0xB2D3, 'store_slot_tmpl_byte')

d.label(0xB2E9, 'done_uppercase_store')

d.label(0xB2FA, 'parse_prot_keywords')

d.label(0xB2FE, 'loop_match_prot_attr')

d.label(0xB310, 'prot_check_arg_end')

d.label(0xB319, 'done_prot_args')

d.label(0xB31A, 'store_prot_mask')

d.label(0xB32B, 'loop_match_unprot_attr')

d.label(0xB34D, 'request_next_wipe')

d.label(0xB380, 'check_wipe_attr')

d.label(0xB383, 'loop_check_if_locked')

d.label(0xB387, 'skip_wipe_locked')

d.label(0xB38C, 'check_wipe_dir')

d.label(0xB395, 'show_wipe_prompt')

d.label(0xB399, 'loop_copy_wipe_name')

d.label(0xB3C2, 'loop_print_wipe_info')

d.label(0xB3DB, 'check_wipe_response')

d.label(0xB3ED, 'loop_build_wipe_cmd')

d.label(0xB3F6, 'skip_if_not_space')

d.label(0xB3FA, 'set_wipe_cr_end')

d.label(0xB3FC, 'store_wipe_tx_char')

d.label(0xB40B, 'skip_wipe_to_next')

d.label(0xB411, 'use_wipe_leaf_name')

d.label(0xB412, 'loop_copy_wipe_leaf')

d.label(0xB43C, 'loop_clear_chan_table')

d.label(0xB44C, 'loop_mark_chan_avail')

d.label(0xB465, 'error_chan_out_of_range')

d.label(0xB467, 'return_chan_index')

d.label(0xB473, 'error_chan_not_found')

d.label(0xB477, 'net_channel_err_string')

d.label(0xB4B1, 'error_chan_not_here')

d.label(0xB4BC, 'loop_copy_chan_err_str')

d.label(0xB4CF, 'loop_append_err_suffix')

d.label(0xB4FD, 'loop_scan_fcb_slots')

d.label(0xB50B, 'done_found_free_slot')

d.label(0xB548, 'return_alloc_success')

d.label(0xB54E, 'skip_set_carry')

d.label(0xB553, 'loop_scan_fcb_down')

d.label(0xB557, 'skip_if_slots_done')

d.label(0xB56B, 'done_check_station')

d.label(0xB58F, 'loop_find_fcb')

d.label(0xB596, 'skip_if_no_wrap')

d.label(0xB5A0, 'done_check_fcb_status')

d.label(0xB5AA, 'done_select_fcb')

d.label(0xB5AB, 'loop_scan_empty_fcb')

d.label(0xB5B2, 'done_test_empty_slot')

d.label(0xB5C1, 'skip_if_modified_fcb')

d.label(0xB5DE, 'loop_clear_counters')

d.label(0xB62F, 'done_restore_offset')

d.label(0xB657, 'done_clear_fcb_active')

d.label(0xB662, 'loop_save_tx_context')

d.label(0xB675, 'done_save_context')

d.label(0xB678, 'loop_find_pending_fcb')

d.label(0xB6CC, 'done_init_wipe')

d.label(0xB6F2, 'done_calc_offset')

d.label(0xB711, 'loop_clear_buffer')

d.label(0xB716, 'done_set_fcb_active')

d.label(0xB720, 'loop_restore_workspace')

d.label(0xB72B, 'loop_restore_tx_buf')

d.label(0xB735, 'loop_save_before_match')

d.label(0xB73A, 'loop_reload_attr')

d.label(0xB73D, 'loop_next_fcb_slot')

d.label(0xB757, 'done_test_fcb_active')

d.label(0xB78E, 'return_test_offset')

d.label(0xB7AE, 'loop_process_fcb')

d.label(0xB7B9, 'done_flush_fcb')

d.label(0xB7BF, 'done_advance_fcb')

d.label(0xB7EE, 'done_read_fcb_byte')

d.label(0xB819, 'error_end_of_file')

d.label(0xB82A, 'done_load_from_buf')

d.label(0xB87D, 'done_test_write_flag')

d.label(0xB88B, 'done_find_write_fcb')

d.label(0xB8DD, 'done_check_buf_offset')

d.label(0xB8F1, 'done_set_dirty_flag')

d.label(0xB910, 'done_inc_byte_count')

d.label(0xB953, 'loop_copy_wipe_err_msg')

d.label(0xB960, 'done_terminate_wipe_err')

d.label(0xB969, 'done_toggle_station')

d.label(0xB98B, 'open_and_read_file')

d.label(0x0406, 'tube_addr_data_dispatch')

d.label(0x0421, 'clear_tube_claim')

d.label(0x83EB, 'discard_reset_rx')

d.label(0x83EE, 'reset_adlc_rx_listen')

d.label(0x83F1, 'set_nmi_rx_scout')

d.label(0x8505, 'setup_sr_tx')

d.label(0x8534, 'tx_done_dispatch_lo')

d.label(0x8542, 'tx_done_econet_event')

d.label(0x854A, 'tx_done_fire_event')

d.label(0x8AE2, 'scan_remote_keys')

d.label(0x8AFA, 'save_text_ptr')

d.label(0x8B82, 'help_print_nfs_cmds')

d.label(0x8B8D, 'print_cmd_table')

d.label(0x8BA0, 'print_cmd_table_loop')

d.label(0x8C28, 'help_wrap_if_serial')

d.label(0x8C94, 'print_version_header')

d.label(0x8CAE, 'get_ws_page')

d.label(0x8CB5, 'setup_ws_ptr')

d.label(0x8CF1, 'notify_new_fs')

d.label(0x8CFA, 'call_fscv')

d.label(0x8CFD, 'issue_svc_15')

d.label(0x8D0C, 'check_credits_easter_egg')

d.label(0x8DFE, 'clear_if_station_match')

d.label(0x8E09, 'return_from_station_match')

d.label(0x8E0A, 'pass_send_cmd')

d.label(0x8E0E, 'send_cmd_and_dispatch')

d.label(0x8E2D, 'dir_op_dispatch')

d.label(0x8E3C, 'push_dispatch_lo')

d.label(0x8E76, 'osbyte_x0_y0')

d.label(0x8E96, 'store_ws_page_count')

d.label(0x8F40, 'init_adlc_and_vectors')

d.label(0x8F53, 'write_vector_entry')

d.label(0x8F73, 'restore_fs_context')

d.label(0x8F80, 'fscv_6_shutdown')

d.label(0x8FB2, 'verify_ws_checksum')

d.label(0x8FCB, 'error_net_checksum')

d.label(0x8FDD, 'print_station_id')

d.label(0x911B, 'print_hex_byte')

d.label(0x9124, 'print_hex_nybble')

d.label(0x915A, 'parse_addr_arg')

d.label(0x91F4, 'err_bad_hex')

d.label(0x9201, 'err_bad_station_num')

d.label(0x9244, 'is_decimal_digit')

d.label(0x924C, 'is_dec_digit_only')

d.label(0x9255, 'get_access_bits')

d.label(0x925F, 'get_prot_bits')

d.label(0x927D, 'set_text_and_xfer_ptr')

d.label(0x9281, 'set_xfer_params')

d.label(0x9287, 'set_options_ptr')

d.label(0x928B, 'clear_escapable')

d.label(0x9290, 'cmp_5byte_handle')

d.label(0x92A1, 'set_conn_active')

d.label(0x92B8, 'clear_conn_active')

d.label(0x92E6, 'error_bad_filename')

d.label(0x92F5, 'check_not_ampersand')

d.label(0x92FD, 'read_filename_char')

d.label(0x930E, 'send_fs_request')

d.label(0x9313, 'copy_fs_cmd_name')

d.label(0x9335, 'parse_quoted_arg')

d.label(0x9451, 'init_txcb_bye')

d.label(0x9453, 'init_txcb_port')

d.label(0x945F, 'init_txcb')

d.label(0x9483, 'send_request_nowrite')

d.label(0x9487, 'send_request_write')

d.label(0x9499, 'save_net_tx_cb')

d.label(0x949A, 'save_net_tx_cb_vset')

d.label(0x94C6, 'prep_send_tx_cb')

d.label(0x94DC, 'recv_and_process_reply')

d.label(0x955A, 'check_escape')

d.label(0x9560, 'raise_escape_error')

d.label(0x95C7, 'wait_net_tx_ack')

d.label(0x95FB, 'cond_save_error_code')

d.label(0x962B, 'fixup_reply_status_a')

d.label(0x9636, 'load_reply_and_classify')

d.label(0x9638, 'classify_reply_error')

d.label(0x969D, 'bad_str_anchor')

d.label(0x96DA, 'check_net_error_code')

d.label(0x9738, 'append_drv_dot_num')

d.label(0x975C, 'append_space_and_num')

d.label(0x9767, 'append_decimal_num')

d.label(0x9778, 'append_decimal_digit')

d.label(0x9822, 'init_tx_ptr_and_send')

d.label(0x982A, 'send_net_packet')

d.label(0x987F, 'init_tx_ptr_for_pass')

d.label(0x9887, 'setup_pass_txbuf')

d.label(0x98F3, 'load_text_ptr_and_parse')

d.label(0x98FF, 'gsread_to_buf')

d.label(0x993D, 'do_fs_cmd_iteration')

d.label(0x9984, 'send_txcb_swap_addrs')

d.label(0x9A45, 'print_load_exec_addrs')

d.label(0x9A50, 'print_5_hex_bytes')

d.label(0x9A60, 'copy_fsopts_to_zp')

d.label(0x9A6C, 'skip_one_and_advance5')

d.label(0x9A6D, 'advance_y_by_4')

d.label(0x9A72, 'copy_workspace_to_fsopts')

d.label(0x9A7F, 'retreat_y_by_4')

d.label(0x9A80, 'retreat_y_by_3')

d.label(0x9A88, 'check_and_setup_txcb')

d.label(0x9B86, 'format_filename_field')

d.label(0x9CB9, 'return_with_last_flag')

d.label(0x9CBB, 'finalise_and_return')

d.label(0x9E03, 'update_addr_from_offset9')

d.label(0x9E08, 'update_addr_from_offset1')

d.label(0x9E0A, 'add_workspace_to_fsopts')

d.label(0x9E0B, 'adjust_fsopts_4bytes')

d.label(0x9EC0, 'lookup_cat_entry_0')

d.label(0x9EC4, 'lookup_cat_slot_data')

d.label(0x9ECB, 'setup_transfer_workspace')

d.label(0x9FB8, 'write_data_block')

d.label(0x9FF4, 'tail_update_catalogue')

d.label(0xA05B, 'tube_claim_c3')

d.label(0xA086, 'print_fs_info_newline')

d.label(0xA08F, 'parse_fs_ps_args')

d.label(0xA0B4, 'get_pb_ptr_as_index')

d.label(0xA0B6, 'byte_to_2bit_index')

d.label(0xA0CB, 'return_from_2bit_index')

d.label(0xA0FC, 'fscv_3_star_cmd')

d.label(0xA10D, 'cmd_fs_reentry')

d.label(0xA10F, 'error_syntax')

d.label(0xA128, 'match_fs_cmd')

d.label(0xA245, 'error_bad_command')

d.label(0xA2DC, 'fsreply_3_set_csd')

d.label(0xA2E8, 'find_station_bit2')

d.label(0xA313, 'find_station_bit3')

d.label(0xA34A, 'flip_set_station_boot')

d.label(0xA3D0, 'boot_cmd_oscli')

d.label(0xA4EF, 'osword_setup_handler')

d.label(0xA57C, 'bin_to_bcd')

d.label(0xA601, 'store_osword_pb_ptr')

d.label(0xA612, 'store_ptr_at_ws_y')

d.label(0xA868, 'init_bridge_poll')

d.label(0xA964, 'enable_irq_and_poll')

d.label(0xA981, 'push_osword_handler_addr')

d.label(0xA9AC, 'tx_econet_abort')

d.label(0xAA6A, 'init_ws_copy_wide')

d.label(0xAA73, 'init_ws_copy_narrow')

d.label(0xAA77, 'ws_copy_vclr_entry')

d.label(0xAAD0, 'reset_spool_buf_state')

d.label(0xAB00, 'append_byte_to_rxbuf')

d.label(0xAB09, 'handle_spool_ctrl_byte')

d.label(0xABEC, 'err_printer_busy')

d.label(0xAC12, 'send_disconnect_reply')

d.label(0xACCB, 'commit_state_byte')

d.label(0xACD2, 'serialise_palette_entry')

d.label(0xACE5, 'read_osbyte_to_ws_x0')

d.label(0xACE7, 'read_osbyte_to_ws')

d.label(0xAD2F, 'cdir_dispatch_col')

d.label(0xAE70, 'print_10_chars')

d.label(0xAE80, 'parse_cmd_arg_y0')

d.label(0xAE82, 'parse_filename_arg')

d.label(0xAE85, 'parse_access_prefix')

d.label(0xAEA5, 'strip_token_prefix')

d.label(0xAEF0, 'copy_arg_to_buf_x0')

d.label(0xAEF2, 'copy_arg_to_buf')

d.label(0xAEF4, 'copy_arg_validated')

d.label(0xAF0D, 'return_from_copy_arg')

d.label(0xAF12, 'mask_owner_access')

d.label(0xAF27, 'ex_print_col_sep')

d.label(0xAF65, 'print_num_no_leading')

d.label(0xAF68, 'print_decimal_3dig')

d.label(0xAF76, 'print_decimal_digit')

d.label(0xAF94, 'return_from_print_digit')

d.label(0xAF95, 'save_ptr_to_os_text')

d.label(0xAFA1, 'skip_to_next_arg')

d.label(0xAFB4, 'return_from_skip_arg')

d.label(0xAFB5, 'save_ptr_to_spool_buf')

d.label(0xAFC0, 'init_spool_drive')

d.label(0xAFF7, 'copy_ps_data_y1c')

d.label(0xAFF9, 'copy_ps_data')

d.label(0xB0A1, 'print_file_server_is')

d.label(0xB0AB, 'print_printer_server_is')

d.label(0xB0C6, 'load_ps_server_addr')

d.label(0xB0D2, 'pop_requeue_ps_scan')

d.label(0xB11A, 'write_ps_slot_hi_link')

d.label(0xB13A, 'write_ps_slot_byte_ff')

d.label(0xB141, 'write_two_bytes_inc_y')

d.label(0xB149, 'reverse_ps_name_to_tx')

d.label(0xB174, 'print_station_addr')

d.label(0xB2C3, 'return_from_poll_slots')

d.label(0xB2C4, 'init_ps_slot_from_rx')

d.label(0xB2DB, 'store_char_uppercase')

d.label(0xB41F, 'flush_and_read_char')

d.label(0xB42E, 'return_from_flush_read')

d.label(0xB42F, 'unused_clear_ws_78')

d.label(0xB433, 'loop_clear_ws_78')

d.label(0xB439, 'init_channel_table')

d.label(0xB45B, 'attr_to_chan_index')

d.label(0xB46A, 'check_chan_char')

d.label(0xB472, 'err_net_chan_invalid')

d.label(0xB475, 'err_net_chan_not_found')

d.label(0xB49D, 'lookup_chan_by_char')

d.label(0xB4DC, 'store_result_check_dir')

d.label(0xB4E3, 'check_not_dir')

d.label(0xB4F9, 'return_from_dir_check')

d.label(0xB4FA, 'alloc_fcb_slot')

d.label(0xB52E, 'alloc_fcb_or_error')

d.label(0xB54A, 'close_all_net_chans')

d.label(0xB551, 'scan_fcb_flags')

d.label(0xB57A, 'match_station_net')

d.label(0xB588, 'return_from_match_stn')

d.label(0xB589, 'find_open_fcb')

d.label(0xB5CC, 'init_wipe_counters')

d.label(0xB5EF, 'start_wipe_pass')

d.label(0xB660, 'save_fcb_context')

d.label(0xB729, 'restore_catalog_entry')

d.label(0xB738, 'find_matching_fcb')

d.label(0xB791, 'inc_fcb_byte_count')

d.label(0xB79E, 'return_from_inc_fcb_count')

d.label(0xB79F, 'process_all_fcbs')

d.label(0xB920, 'send_wipe_request')

d.label(0xB979, 'send_and_receive')

d.label(0xB995, 'loop_read_print_byte')

d.label(0xB9A1, 'done_print_escape')

d.label(0xB9B0, 'done_store_prev_char')

d.label(0xB9B2, 'loop_write_char')

d.label(0xB9B8, 'done_handle_line_end')

d.label(0xB9C5, 'done_normalise_crlf')

d.label(0xB9D2, 'done_write_newline')

d.label(0xB9D8, 'done_check_cr_lf')

d.label(0xB9DF, 'done_check_lf_cr')

d.label(0xB9E4, 'done_consume_pair')

d.label(0xB9EA, 'abort_if_escape')

d.label(0xB9EF, 'error_escape_pressed')

d.label(0xBA0D, 'loop_push_zero_buf')

d.label(0xBA1E, 'loop_dump_line')

d.label(0xBA25, 'loop_read_dump_byte')

d.label(0xBA37, 'done_check_dump_eof')

d.label(0xBA3E, 'loop_pop_stack_buf')

d.label(0xBA45, 'done_check_boundary')

d.label(0xBA50, 'done_start_dump_addr')

d.label(0xBA52, 'loop_print_addr_byte')

d.label(0xBA63, 'loop_inc_dump_addr')

d.label(0xBA7B, 'loop_print_dump_hex')

d.label(0xBA85, 'loop_next_dump_col')

d.label(0xBA9B, 'done_print_separator')

d.label(0xBAA7, 'loop_print_dump_ascii')

d.label(0xBAAF, 'skip_non_printable')

d.label(0xBAB1, 'done_test_del')

d.label(0xBAC0, 'done_end_dump_line')

d.label(0xBAC9, 'done_dump_eof')

d.label(0xBACE, 'print_dump_header')

d.label(0xBAE4, 'loop_print_col_num')

d.label(0xBB0C, 'close_ws_file')

d.label(0xBB13, 'open_file_for_read')

d.label(0xBB39, 'done_restore_text_ptr')

d.label(0xBB41, 'loop_skip_filename')

d.label(0xBB4C, 'loop_skip_fn_spaces')

d.label(0xBB53, 'return_with_fn_offset')

d.label(0xBB55, 'parse_dump_range')

d.label(0xBB5A, 'loop_clear_hex_accum')

d.label(0xBB61, 'loop_parse_hex_digit')

d.label(0xBB80, 'done_mask_hex_digit')

d.label(0xBB87, 'loop_shift_nibble')

d.label(0xBB8A, 'loop_rotate_hex_accum')

d.label(0xBBAB, 'error_hex_overflow')

d.label(0xBBAF, 'error_bad_hex_value')

d.label(0xBBB5, 'loop_skip_hex_spaces')

d.label(0xBBB6, 'done_test_hex_space')

d.label(0xBBBE, 'init_dump_buffer')

d.label(0xBBD7, 'loop_cmp_file_length')

d.label(0xBBE3, 'done_check_outside')

d.label(0xBBE9, 'error_outside_file')

d.label(0xBBFE, 'loop_copy_start_addr')

d.label(0xBC03, 'done_advance_start')

d.label(0xBC1B, 'loop_copy_osfile_ptr')

d.label(0xBC2E, 'loop_shift_osfile_data')

d.label(0xBC3D, 'loop_check_ff_addr')

d.label(0xBC4A, 'loop_zero_load_addr')

d.label(0xBC51, 'done_parse_disp_base')

d.label(0xBC66, 'done_add_disp_base')

d.label(0xBC6B, 'loop_add_disp_bytes')

d.label(0xBC7B, 'loop_store_disp_addr')

d.label(0xBC84, 'advance_x_by_8')

d.label(0xBC87, 'advance_x_by_4')

d.label(0xBC8A, 'inx4')

d.label(0xBE5E, 'tube_vdu_dispatch')

d.label(0xBE6F, 'loop_poll_r1_vdu_rom')

d.label(0xBE9A, 'loop_copy_reloc_pages')

d.label(0xBEB4, 'loop_copy_zp_workspace')


d.subroutine(0x8023, 'svc5_irq_check', title='Service 5: unrecognised interrupt (SR dispatch)', description="""Tests IFR bit 2 (SR complete) to check for a
shift register transfer complete. If SR is not set,
returns A=5 to pass the service call on. If SR is
set, saves registers, reads the VIA ACR, clears and
restores the SR mode bits from ws_0d64, then dispatches
the TX completion callback via the operation type stored
in tx_op_type. The indexed handler performs the completion
action (e.g. resuming background print spooling) before
returning with A=0 to claim the service call.""", on_entry={'a': '5 (service call number)', 'x': 'ROM slot', 'y': 'parameter'})


d.subroutine(0x8A0B, 'service_handler', title='Service call dispatch', description="""Handles service calls 1, 4, 8, 9, 13, 14, and 15.
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

d.label(0x0498, 'claim_addr_ff')

d.label(0x04A2, 'next_rom_page')

d.label(0x04AB, 'send_rom_page_bytes')

d.label(0x04C0, 'skip_addr_carry')

d.label(0x04CB, 'tube_claim_default')

d.label(0x04D2, 'tube_init_reloc')

d.label(0x04E5, 'scan_copyright_end')

d.label(0x04FB, 'store_xfer_end_addr')

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

d.label(0x8015, 'copyright_string')

d.label(0x8061, 'dispatch_svc5')

d.label(0x8068, 'svc_5_unknown_irq')

d.label(0x8089, 'init_nmi_workspace')

d.label(0x808B, 'copy_nmi_shim')

d.label(0x80CB, 'accept_frame')

d.label(0x80DE, 'scout_reject')

d.label(0x80E6, 'accept_local_net')

d.label(0x80E9, 'accept_scout_net')

d.label(0x80FF, 'scout_discard')

d.label(0x8107, 'scout_loop_rda')

d.label(0x8117, 'scout_loop_second')

d.label(0x8152, 'scout_no_match')

d.label(0x8155, 'scout_match_port')

d.label(0x815F, 'scan_port_list')

d.label(0x8168, 'scan_nfs_port_list')

d.label(0x816C, 'check_port_slot')

d.label(0x816E, 'scout_ctrl_check')

d.label(0x8180, 'check_station_filter')

d.label(0x818A, 'scout_port_match')

d.label(0x8194, 'next_port_slot')

d.label(0x81A1, 'discard_no_match')

d.label(0x81A4, 'try_nfs_port_list')

d.label(0x81AF, 'port_match_found')

d.label(0x81C1, 'send_data_rx_ack')

d.label(0x81D2, 'data_rx_setup')

d.label(0x81F0, 'nmi_data_rx_net')

d.label(0x8206, 'nmi_data_rx_skip')

d.label(0x8211, 'install_data_rx_handler')

d.label(0x8224, 'install_tube_rx')

d.label(0x822B, 'nmi_error_dispatch')

d.label(0x8233, 'rx_error_reset')

d.label(0x823E, 'data_rx_loop')

d.label(0x824E, 'read_sr2_between_pairs')

d.label(0x8255, 'read_second_rx_byte')

d.label(0x8265, 'check_sr2_loop_again')

d.label(0x8284, 'read_last_rx_byte')

d.label(0x8293, 'send_ack')

d.label(0x8296, 'nmi_data_rx_tube')

d.label(0x8299, 'rx_tube_data')

d.label(0x82B6, 'data_rx_tube_error')

d.label(0x82B9, 'data_rx_tube_complete')

d.label(0x82EF, 'ack_tx_configure')

d.label(0x82FD, 'ack_tx_write_dest')

d.label(0x833E, 'start_data_tx')

d.label(0x8341, 'dispatch_nmi_error')

d.label(0x8344, 'advance_rx_buffer_ptr')

d.label(0x834F, 'add_rxcb_ptr')

d.label(0x837D, 'inc_rxcb_ptr')

d.label(0x8388, 'skip_tube_update')

d.label(0x838A, 'return_rx_complete')

d.label(0x839A, 'rx_complete_update_rxcb')

d.label(0x839F, 'add_buf_to_base')

d.label(0x83A6, 'inc_rxcb_buf_hi')

d.label(0x83A8, 'store_buf_ptr_lo')

d.label(0x83AA, 'store_rxcb_buf_ptr')

d.label(0x83AF, 'store_rxcb_buf_hi')

d.label(0x83B1, 'skip_buf_ptr_update')

d.label(0x8406, 'copy_scout_to_buffer')

d.label(0x840C, 'copy_scout_select')

d.label(0x8413, 'copy_scout_bytes')

d.label(0x8421, 'next_scout_byte')

d.label(0x8428, 'scout_copy_done')

d.label(0x842D, 'copy_scout_via_tube')

d.label(0x843F, 'release_tube')

d.label(0x8448, 'clear_release_flag')

d.label(0x8462, 'rotate_prot_mask')

d.label(0x8468, 'dispatch_imm_op')

d.label(0x8473, 'scout_page_overflow')

d.label(0x8475, 'check_scout_done')

d.label(0x847B, 'imm_op_out_of_range')

d.label(0x8498, 'copy_addr_loop')

d.label(0x84A2, 'svc5_dispatch_lo')

d.label(0x84D3, 'set_tx_reply_flag')

d.label(0x84DB, 'rx_imm_halt_cont')

d.label(0x84E0, 'tx_cr2_setup')

d.label(0x84E5, 'tx_nmi_setup')

d.label(0x84EC, 'imm_op_build_reply')

d.label(0x8522, 'imm_op_discard')

d.label(0x856C, 'halt_spin_loop')

d.label(0x857B, 'tx_done_exit')

d.label(0x8582, 'tx_begin')

d.label(0x859A, 'tx_imm_op_setup')

d.label(0x85AE, 'calc_peek_poke_size')

d.label(0x85C5, 'tx_ctrl_range_check')

d.label(0x85C9, 'check_imm_range')

d.label(0x85CF, 'copy_imm_params')

d.label(0x85D9, 'tx_line_idle_check')

d.label(0x85F3, 'test_inactive_retry')

d.label(0x85F5, 'intoff_test_inactive')

d.label(0x85FB, 'test_line_idle')

d.label(0x860F, 'inactive_retry')

d.label(0x8625, 'tx_bad_ctrl_error')

d.label(0x8635, 'tx_no_clock_error')

d.label(0x8637, 'store_tx_error')

d.label(0x8690, 'add_bytes_loop')

d.label(0x8677, 'tx_ctrl_dispatch_lo')

d.label(0x867F, 'tx_ctrl_machine_type')

d.label(0x86A2, 'setup_data_xfer')

d.label(0x86B8, 'copy_bcast_addr')

d.label(0x86C4, 'setup_unicast_xfer')

d.label(0x86C9, 'proc_op_status2')

d.label(0x86CB, 'store_status_copy_ptr')

d.label(0x86CE, 'skip_buf_setup')

d.label(0x86D9, 'tx_ctrl_exit')

d.label(0x86E6, 'tx_fifo_write')

d.label(0x8706, 'tx_error')

d.label(0x870A, 'tx_fifo_not_ready')

d.label(0x8711, 'tx_store_error')

d.label(0x8714, 'delay_nmi_disable')

d.label(0x8735, 'check_handshake_bit')

d.label(0x873F, 'install_reply_scout')

d.label(0x876C, 'reject_reply')

d.label(0x87C7, 'data_tx_begin')

d.label(0x87D5, 'install_imm_data_nmi')

d.label(0x87EB, 'data_tx_check_fifo')

d.label(0x87FB, 'write_second_tx_byte')

d.label(0x880B, 'check_irq_loop')

d.label(0x8813, 'data_tx_last')

d.label(0x8824, 'install_saved_handler')

d.label(0x882D, 'nmi_data_tx_tube')

d.label(0x8830, 'tube_tx_fifo_write')

d.label(0x8848, 'write_second_tube_byte')

d.label(0x8852, 'tube_tx_inc_byte2')

d.label(0x8856, 'tube_tx_inc_byte3')

d.label(0x8857, 'tube_tx_inc_operand')

d.label(0x885A, 'tube_tx_inc_byte4')

d.label(0x885E, 'check_tube_irq_loop')

d.label(0x885F, 'tube_tx_sr1_operand')

d.label(0x8866, 'tx_tdra_error')

d.label(0x888E, 'nmi_final_ack_net')

d.label(0x88BF, 'check_fv_final_ack')

d.label(0x88CA, 'tx_result_fail')

d.label(0x8908, 'calc_transfer_size')

d.label(0x8938, 'restore_x_and_return')

d.label(0x893B, 'fallback_calc_transfer')

d.label(0x895E, 'nmi_shim_rom_src')

d.label(0x8979, 'wait_idle_and_reset')

d.label(0x897E, 'poll_nmi_idle')

d.label(0x899A, 'reset_enter_listen')

d.label(0x899C, 'listen_jmp_hi')
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
d.entry(0x8068)
d.entry(0x80B3)
d.entry(0x80D0)
d.entry(0x8102)
d.entry(0x81D2)
d.entry(0x81DC)
d.entry(0x81F0)
d.entry(0x8206)
d.entry(0x8239)
d.entry(0x8296)
d.entry(0x831B)
d.entry(0x8365)
d.entry(0x838B)
d.entry(0x84EC)
d.entry(0x85EA)
d.entry(0x86E0)
d.entry(0x8706)
d.entry(0x871C)
d.entry(0x8728)
d.entry(0x8744)
d.entry(0x8758)
d.entry(0x876F)
d.entry(0x87B7)
d.entry(0x87DC)
d.entry(0x882D)
d.entry(0x886E)
d.entry(0x887A)
d.entry(0x888E)
d.entry(0x88A2)
d.entry(0x88C6)
d.entry(0x88CC)
d.entry(0x893B)
d.entry(0x899D)
d.entry(0x89AB)


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


d.subroutine(0x04CB, 'tube_claim_default', title='Claim default Tube transfer address', description="""Sets Y=0, X=&53 (address &0053), then JMP tube_addr_claim
to initiate a Tube address claim for the default transfer
address. Called from the BEGIN startup path and after the
page transfer loop completes.""")


d.subroutine(0x04D2, 'tube_init_reloc', title='Initialise relocation address for ROM transfer', description="""Sets the Tube transfer source page to &8000
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


d.subroutine(0x8052, 'set_jsr_protection', title='Set JSR protection and dispatch via table', description="""Validates the TX operation type in Y against the
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


d.subroutine(0x8069, 'adlc_init', title='ADLC initialisation', description="""Initialise ADLC hardware and Econet workspace.
Reads station ID via &FE18 (INTOFF side effect),
performs a full ADLC reset (adlc_full_reset), then
checks for Tube co-processor via OSBYTE &EA and
stores the result in l0d63. Issues NMI claim service
request (OSBYTE &8F, X=&0C). Falls through to
init_nmi_workspace to copy the NMI shim to RAM.""")


d.subroutine(0x8089, 'init_nmi_workspace', title='Initialise NMI workspace (skip service request)', description="""Copies 32 bytes of NMI shim code from ROM
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


d.subroutine(0x80B3, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")


d.subroutine(0x80D0, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &8102.""")


d.subroutine(0x80F2, 'scout_error', title='Scout error/discard handler', description="""Handles scout reception errors and end-of-frame
conditions. Reads SR2 and tests AP|RDA (bits 0|7):
if neither set, the frame ended cleanly and is
simply discarded. If unexpected data is present,
performs a full ADLC reset. Also serves as the
common discard path for address/network mismatches
from nmi_rx_scout and scout_complete -- reached by
5 branch sites across the scout reception chain.""")


d.subroutine(0x812C, 'scout_complete', title='Scout completion handler', description="""Processes a completed scout frame. Writes CR1=&00
and CR2=&84 to disable PSE and suppress FV, then
tests SR2 for FV (frame valid). If FV is set with
RDA, reads the remaining scout data bytes in pairs
into the buffer at &0D3D. Matches the port byte
(&0D40) against open receive control blocks to find
a listener. On match, calculates the transfer size
via tx_calc_transfer, sets up the data RX handler
chain, and sends a scout ACK. On no match or error,
discards the frame via scout_error.""")


d.subroutine(0x81DC, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &81DC (AP+addr check) -> &81F0 (net=0 check) ->
&8206 (skip ctrl+port) -> &8239 (bulk data read) -> &826D (completion)""")


d.subroutine(0x8211, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects between the normal bulk RX handler (&8239)
and the Tube RX handler based on bit 1 of rx_src_net
(tx_flags). If normal mode, loads the handler address
&8239 and checks SR1 bit 7: if IRQ is already asserted
(more data waiting), jumps directly to nmi_data_rx_bulk
to avoid NMI re-entry overhead. Otherwise installs the
handler via set_nmi_vector and returns via RTI.""")


d.subroutine(0x822B, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")


d.subroutine(0x8239, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &826D.
SR2 = 0 -> RTI, wait for next NMI to continue.""")


d.subroutine(0x826D, 'data_rx_complete', title='Data frame completion', description="""Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&812C): disables PSE (CR2=&84,
CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &82E4.""")


d.subroutine(0x82E4, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&88C6).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")


d.subroutine(0x831B, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Continuation of ACK frame transmission. Reads our
station ID from &FE18 (INTOFF side effect), tests
TDRA via SR1, and writes station + network=0 to the
TX FIFO, completing the 4-byte ACK address header.
Then checks rx_src_net bit 7: if set, branches to
start_data_tx to begin the data phase. Otherwise
writes CR2=&3F (TX_LAST_DATA) and falls through to
post_ack_scout for scout processing.""")


d.subroutine(0x8332, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")


d.subroutine(0x8344, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")


d.subroutine(0x838B, 'nmi_post_ack_dispatch', title='Post-ACK frame-complete NMI handler', description="""Installed by ack_tx_configure via saved_nmi_lo/hi.
Fires as an NMI after the ACK frame (CRC and
closing flag) has been fully transmitted by the
ADLC. Dispatches on scout_port: port != 0 goes
to rx_complete_update_rxcb to finalise the data
transfer and mark the RXCB complete; port = 0
with ctrl &82 (POKE) also goes to
rx_complete_update_rxcb; other port-0 ops go to
imm_op_build_reply.""")


d.subroutine(0x839A, 'rx_complete_update_rxcb', title='Complete RX and update RXCB', description="""Called from nmi_post_ack_dispatch after the
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


d.subroutine(0x83F8, 'discard_reset_listen', title='Discard with Tube release', description="""Checks whether a Tube transfer is active by
ANDing bit 1 of l0d63 with rx_src_net (tx_flags).
If a Tube claim is held, calls release_tube to
free it before returning. Used as the clean-up
path after RXCB completion and after ADLC reset
to ensure no stale Tube claims persist.""")


d.subroutine(0x8406, 'copy_scout_to_buffer', title='Copy scout data to port buffer', description="""Copies scout data bytes (offsets 4-11) from the
RX scout buffer at &0D3D into the open port buffer.
Checks bit 1 of rx_src_net (tx_flags) to select the
write path: direct memory store via (open_port_buf),Y
for normal transfers, or Tube data register 3 write
for Tube transfers. Calls advance_buffer_ptr after
each byte. Falls through to release_tube on
completion. Handles page overflow (Y wrap) by
branching to scout_page_overflow.""")


d.subroutine(0x843F, 'release_tube', title='Release Tube co-processor claim', description="""Tests need_release_tube (&98) bit 7: if set, the
Tube has already been released and the subroutine
just clears the flag. If clear (Tube claim held),
calls tube_addr_data_dispatch with A=&82 to release
the claim, then clears the release flag via LSR
(which shifts bit 7 to 0). Called after completed
RX transfers and during discard paths to ensure no
stale Tube claims persist.""")


d.subroutine(0x844B, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Checks the control byte at l0d30 for immediate
operation codes (&81-&88). Codes below &81 or above
&88 are out of range and discarded. Codes &87-&88
(HALT/CONTINUE) bypass the protection mask check.
For &81-&86, converts to a 0-based index and tests
against the immediate operation mask at &0D61 to
determine if this station accepts the operation.
If accepted, dispatches via the immediate operation
table. Builds the reply by storing data length,
station/network, and control byte into the RX buffer.""")

d.label(0x847E, 'imm_op_dispatch_lo')
for addr in range(0x847E, 0x8486):
    d.byte(addr)
d.expr(0x847E, '<(rx_imm_peek-1)')
d.expr(0x847F, '<(rx_imm_poke-1)')
d.expr(0x8480, '<(rx_imm_exec-1)')
d.expr(0x8481, '<(rx_imm_exec-1)')
d.expr(0x8482, '<(rx_imm_exec-1)')
d.expr(0x8483, '<(rx_imm_halt_cont-1)')
d.expr(0x8484, '<(rx_imm_halt_cont-1)')
d.expr(0x8485, '<(rx_imm_machine_type-1)')
d.comment(0x847E, 'Ctrl &81: PEEK', align=Align.INLINE)
d.comment(0x847F, 'Ctrl &82: POKE', align=Align.INLINE)
d.comment(0x8480, 'Ctrl &83: JSR', align=Align.INLINE)
d.comment(0x8481, 'Ctrl &84: UserProc', align=Align.INLINE)
d.comment(0x8482, 'Ctrl &85: OSProc', align=Align.INLINE)
d.comment(0x8483, 'Ctrl &86: HALT', align=Align.INLINE)
d.comment(0x8484, 'Ctrl &87: CONTINUE', align=Align.INLINE)
d.comment(0x8485, 'Ctrl &88: machine type query', align=Align.INLINE)


d.subroutine(0x8486, 'rx_imm_exec', title='RX immediate: JSR/UserProc/OSProc setup', description="""Sets up the port buffer to receive remote procedure
data. Copies the 2-byte remote address from &0D32
into the execution address workspace at &0D66, then
jumps to the common receive path at c81c1. Used for
operation types &83 (JSR), &84 (UserProc), and
&85 (OSProc).""")


d.subroutine(0x84A4, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data.
port_ws_offset=&2E, rx_buf_offset=&0D, then jumps to
the common data-receive path at c81af.""")


d.subroutine(0x84AF, 'rx_imm_machine_type', title='RX immediate: machine type query', description="""Sets up a buffer at &88C1 (length #&01FC) for the
machine type query response. Falls through to
set_rx_buf_len_hi to configure buffer dimensions,
then branches to set_tx_reply_flag.""")


d.subroutine(0x84C1, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Writes &0D2E to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send
the PEEK response data back to the requesting station.""")


d.subroutine(0x8525, 'advance_buffer_ptr', title='Increment 4-byte receive buffer pointer', description="""Adds one to the counter at &A2-&A5 (port_buf_len
low/high, open_port_buf low/high), cascading
overflow through all four bytes. Called after each
byte is stored during scout data copy and data
frame reception to track the current write position
in the receive buffer.""")


d.subroutine(0x84EC, 'imm_op_build_reply', title='Build immediate operation reply header', description="""Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")


d.subroutine(0x8539, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes (tx_done_exit - 1) on the stack so RTS returns
to tx_done_exit, then does JMP (l0d66) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")


d.subroutine(0x8542, 'tx_done_econet_event', title='TX done: fire Econet event', description="""Handler for TX operation type &84. Loads the
remote address from l0d66/l0d67 into X/A and
sets Y=8 (Econet event number), then falls
through to tx_done_fire_event to call OSEVEN.""")


d.subroutine(0x8550, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM service entry point with X=l0d66,
Y=l0d67. This invokes an OS-level procedure on
behalf of the remote station, then exits via
tx_done_exit.""")


d.subroutine(0x855C, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of rx_flags (&0D61), enables interrupts,
and spin-waits until bit 2 is cleared (by a CONTINUE
from the remote station). If bit 2 is already set,
skips to exit.""")


d.subroutine(0x8573, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of rx_flags (&0D61), releasing any
station that is halted and spinning in tx_done_halt.""")


d.subroutine(0x8582, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")


d.subroutine(0x85EA, 'inactive_poll', title='INACTIVE polling loop', description="""Entry point for the Econet line idle detection
loop. Saves the TX index in rx_remote_addr, pushes
two timeout counter bytes onto the stack, and loads
Y=&E7 (CR2 value for TX preparation). Loads the
INACTIVE bit mask (&04) into A and falls through to
intoff_test_inactive to begin polling SR2 with
interrupts disabled.""")


d.subroutine(0x85F5, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Disables NMIs via two reads of &FE18 (INTOFF),
then polls SR2 for the INACTIVE bit (bit 2). If
INACTIVE is detected, reads SR1 and writes CR2=&67
to clear status, then tests CTS (SR1 bit 4): if
CTS is present, branches to tx_prepare to begin
transmission. If INACTIVE is not set, re-enables
NMIs via &FE20 (INTON) and decrements the 3-byte
timeout counter on the stack. On timeout, falls
through to tx_line_jammed.""")


d.subroutine(0x8629, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Reached when the INACTIVE polling loop times
out without detecting a quiet line. Writes
CR2=&07 (FC_TDRA|2_1_BYTE|PSE) to abort the TX
attempt, pulls the 3-byte timeout state from the
stack, and stores error code &40 ('Line Jammed')
in the TX control block via store_tx_error.""")


d.subroutine(0x8643, 'tx_prepare', title='TX preparation', description="""Configures the ADLC for frame transmission.
Writes CR2=Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|
2_1_BYTE|PSE) and CR1=&44 (RX_RESET|TIE) to enable
TX with interrupts. Installs the nmi_tx_data handler
at &86E0. Sets need_release_tube flag via SEC/ROR.
Writes the 4-byte destination address (dst_stn,
dst_net, src_stn, src_net=0) to the TX FIFO. For
Tube transfers, claims the Tube address; for direct
transfers, sets up the buffer pointer from the TXCB.""")


d.subroutine(0x867F, 'tx_ctrl_machine_type', title='TX ctrl: machine type query setup', description="""Handler for control byte &88. Sets scout_status=3
and branches to store_status_copy_ptr, skipping
the 4-byte address addition (no address parameters
needed for a machine type query).""")


d.subroutine(0x8683, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets A=3 (scout_status for PEEK) and branches
to tx_ctrl_store_and_add to store the status and
perform the 4-byte transfer address addition.""")


d.subroutine(0x8687, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets A=2 (scout_status for POKE) and falls
through to tx_ctrl_store_and_add to store the
status and perform the 4-byte transfer address
addition.""")


d.subroutine(0x8689, 'tx_ctrl_store_and_add', title='TX ctrl: store status and add transfer address', description="""Shared path for PEEK (A=3) and POKE (A=2).
Stores A as the scout status byte at rx_port
(&0D40), then performs a 4-byte addition with
carry propagation, adding bytes from the TXCB
(nmi_tx_block+&0C to +&0F) into the transfer
address workspace at &0D1E-&0D21. Falls through
to tx_ctrl_proc which checks the loop boundary,
then continues to tx_calc_transfer and
tx_ctrl_exit.""", on_entry={'a': 'scout status (3=PEEK, 2=POKE)'})


d.subroutine(0x869B, 'tx_ctrl_proc', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer
directly (no 4-byte address addition needed for
procedure calls). Shared by operation types &83-&85.""")


d.subroutine(0x86E0, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")


d.subroutine(0x871C, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
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


d.subroutine(0x8728, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC
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


d.subroutine(0x8744, 'nmi_reply_scout', title='RX reply scout handler', description="""Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")


d.subroutine(0x8758, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs nmi_reply_validate
(&876F) for the remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &8767.
If IRQ is still set, falls through directly to &876F without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")


d.subroutine(0x876F, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &876F -- must see data available
  2. Read source station at &8774, compare to &0D20 (tx_dst_stn)
  3. Read source network at &877C, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &8786 -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")


d.subroutine(0x87B7, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Continuation of the TX-side scout ACK. Reads our
station ID from &FE18 (INTOFF), tests TDRA via SR1,
and writes station + network=0 to the TX FIFO. Then
checks bit 1 of rx_src_net to select between the
immediate-op data NMI handler and the normal
nmi_data_tx handler at &87E4. Installs the chosen
handler via set_nmi_vector. Shares the tx_check_tdra
entry at &87BD with ack_tx.""")


d.subroutine(0x87DC, 'nmi_data_tx', title='TX data phase: send payload', description="""Transmits the data payload of a four-way
handshake. Loads bytes from (open_port_buf),Y or
from Tube R3 depending on the transfer mode, writing
pairs to the TX FIFO. After each pair, decrements
the byte count (port_buf_len). If the count reaches
zero, branches to tx_last_data to signal end of
frame. Otherwise tests SR1 bit 7 (IRQ): if still
asserted, writes another pair without returning from
NMI (tight loop optimisation). If IRQ clears, returns
via RTI.""")


d.subroutine(0x886E, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""Called via JMP from nmi_tx_complete when bit 0 of
&0D4A is set (four-way handshake in progress). Writes
CR1=&82 (TX_RESET|RIE) to switch the ADLC from TX
mode to RX mode, listening for the final ACK from the
remote station. Installs the nmi_final_ack handler at
&887A via set_nmi_vector.""")


d.subroutine(0x887A, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&8744-&876F):
  &887A: Check AP, read dest_stn, compare to our station
  &888E: Check RDA, read dest_net, validate = 0
  &88A2: Check RDA, read src_stn/net, compare to TX dest
  &88C1: Check FV for frame completion
On success, stores result=0 at tx_result_ok. On failure, error &41.""")


d.subroutine(0x88A2, 'nmi_final_ack_validate', title='Final ACK validation', description="""Continuation of nmi_final_ack. Tests SR2 for RDA,
then reads the source station and source network
bytes from the RX FIFO, comparing each against the
original TX destination at tx_dst_stn (&0D20) and
tx_dst_net (&0D21). Finally tests SR2 bit 1 (FV)
for frame completion. Any mismatch or missing FV
branches to tx_result_fail. On success, falls
through to tx_result_ok.""")


d.subroutine(0x88C6, 'tx_result_ok', title='TX completion handler', description="""Loads A=0 (success) and branches unconditionally to
tx_store_result (BEQ is always taken since A=0). This
two-instruction entry point exists so that JMP sites
can target the success path without needing to set A.
Called from ack_tx (&82EC) for final-ACK completion
and from nmi_tx_complete (&8732) for immediate-op
completion where no ACK is expected.""")


d.subroutine(0x88CA, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")


d.subroutine(0x88CC, 'tx_store_result', title='TX result store and completion', description="""Stores the TX result code (in A) at offset 0 of
the TX control block via (nmi_tx_block),Y=0. Sets
ws_0d60 to &80 to signal TX completion to the
foreground polling loop. Then jumps to
discard_reset_rx for a full ADLC reset and return
to idle RX listen mode.""", on_entry={'a': 'result code (0=success, &40=jammed, &41=not listening)'})


d.subroutine(0x88E8, 'tx_calc_transfer', title='Calculate transfer size', description="""Computes the data transfer byte count from the
RXCB buffer pointers. Reads the 4-byte buffer end
address from (port_ws_offset) and checks for Tube
addresses (&FExx/&FFxx). For Tube transfers, claims
the Tube address and sets the transfer flag in
rx_src_net. Subtracts the buffer start from the
buffer end to compute the byte count, storing it in
port_buf_len/port_buf_len_hi. Also copies the buffer
start address to open_port_buf for the RX/TX handlers
to use as their working pointer.""")


d.subroutine(0x895F, 'adlc_full_reset', title='ADLC full reset', description="""Performs a full ADLC hardware reset. Writes
CR1=&C1 (TX_RESET|RX_RESET|AC) to put both TX and
RX sections in reset with address control enabled.
Then configures CR4=&1E (8-bit RX word, abort extend,
NRZ encoding) and CR3=&00 (no loopback, no AEX, NRZ,
no DTR). Falls through to adlc_rx_listen to re-enter
RX listen mode.""")


d.subroutine(0x896E, 'adlc_rx_listen', title='Enter RX listen mode', description="""Configures the ADLC for passive RX listen mode.
Writes CR1=&82 (TX_RESET|RIE): TX section held in
reset, RX interrupts enabled. Writes CR2=&67
(CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE) to clear
all pending status and enable prioritised status.
This is the idle state where the ADLC listens for
incoming scout frames via NMI.""")


d.subroutine(0x8979, 'wait_idle_and_reset', title='Wait for idle NMI state and reset Econet', description="""Service 12 handler: NMI release. Checks ws_0d62
to see if Econet has been initialised; if not, skips
straight to adlc_rx_listen. Otherwise spins in a
tight loop comparing the NMI handler vector at
&0D0C/&0D0D against the address of nmi_rx_scout
(&80B3). When the NMI handler returns to idle, falls
through to save_econet_state to clear the initialised
flags and re-enter RX listen mode.""")


d.subroutine(0x898C, 'save_econet_state', title='Reset Econet flags and enter RX listen', description="""Disables NMIs via two reads of &FE18 (INTOFF),
then clears ws_0d60 (TX complete) and ws_0d62
(Econet initialised) by storing the current A value.
Sets Y=5 (service call workspace page) and jumps to
adlc_rx_listen to configure the ADLC for passive
listening. Used during NMI release (service 12) to
safely tear down the Econet state before another
ROM can claim the NMI workspace.""")


d.subroutine(0x899D, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&80B3). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &80B3.

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


d.subroutine(0x89AB, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""ROM-resident version of the NMI exit sequence, also
the source for the initial copy to RAM at &0D0E.
set_nmi_vector (&0D0E): writes both hi and lo bytes
of the JMP target at &0D0C/&0D0D. nmi_rti (&0D14):
restores the original ROM bank, pulls Y and A from
the stack, then BIT &FE20 (INTON) to re-enable the
NMI flip-flop before RTI. The INTON creates a
guaranteed falling edge on /NMI if the ADLC IRQ is
already asserted, ensuring the next handler fires
immediately.""")


d.subroutine(0x8AE2, 'scan_remote_keys', title='Scan keyboard for remote operation keys', description="""Uses OSBYTE &7A with Y=&7F to check whether
remote operation keys (&CE-&CF) are currently
pressed. If neither key is detected, clears
svc_state and nfs_workspace to zero via the
clear_svc_and_ws entry point, which is also used
directly by cmd_roff. Called by check_escape.""")


d.subroutine(0x8AFA, 'save_text_ptr', title='Save OS text pointer for later retrieval', description="""Copies &F2/&F3 into fs_crc_lo/fs_crc_hi. Called by
svc_4_star_command and svc_9_help before attempting
command matches, and by match_fs_cmd during
iterative help topic matching. Preserves A via
PHA/PLA.""", on_exit={'a': 'preserved'})


d.subroutine(0x8B8D, 'print_cmd_table', title='Print *HELP command listing with optional header', description="""If V flag is set, saves X/Y, calls
print_version_header to show the ROM version
string and station number, then restores X/Y.
If V flag is clear, outputs a newline only.
Either path then falls through to
print_cmd_table_loop to enumerate commands.""", on_entry={'x': 'offset into cmd_table_fs', 'v': 'set=print version header, clear=newline only'})


d.subroutine(0x8BA0, 'print_cmd_table_loop', title='Enumerate and print command table entries', description="""Walks the ANFS command table from offset X,
printing each command name padded to 9 characters
followed by its syntax description. Entries with
bit 7 set mark end-of-table. The syntax descriptor
byte's low 5 bits index into cmd_syntax_table;
index &0E triggers special handling that lists
shared command names in parentheses. Calls
help_wrap_if_serial to handle line continuation
on serial output streams. Preserves Y.""", on_entry={'x': 'offset into cmd_table_fs'})


d.subroutine(0x8C28, 'help_wrap_if_serial', title='Wrap *HELP syntax lines for serial output', description="""Checks the output destination via &0355. Returns
immediately for VDU (stream 0) or printer
(stream 3) output. For serial streams, outputs a
newline followed by 12 spaces of indentation to
align continuation lines with the syntax
description column.""", on_exit={'y': 'preserved'})


d.subroutine(0x8C94, 'print_version_header', title='Print ANFS version string and station number', description="""Uses an inline string after JSR print_inline:
CR + "Advanced  4.08.53" + CR. After the inline
string, JMPs to print_station_id to append the
local Econet station number.""")


d.subroutine(0x8CAE, 'get_ws_page', title='Read workspace page number for current ROM slot', description="""Indexes into the MOS per-ROM workspace table at
&0DF0 using romsel_copy (&F4) as the ROM slot.
Returns the allocated page number in both A and Y
for caller convenience.""", on_exit={'a': 'workspace page number', 'y': 'workspace page number (same as A)'})


d.subroutine(0x8CB5, 'setup_ws_ptr', title='Set up zero-page pointer to workspace page', description="""Calls get_ws_page to read the page number, stores
it as the high byte in nfs_temp (&CD), and clears
the low byte at &CC to zero. This gives a
page-aligned pointer used by FS initialisation and
cmd_net_fs to access the private workspace.""", on_exit={'a': '0', 'y': 'workspace page number'})


d.subroutine(0x8CF1, 'notify_new_fs', title='Notify OS of filing system selection', description="""Calls FSCV with A=6 to announce the FS change,
then issues paged ROM service call 10 via OSBYTE
&8F to inform other ROMs. Sets X=&0A and branches
to issue_svc_osbyte which falls through from the
call_fscv subroutine.""")


d.subroutine(0x8CFA, 'call_fscv', title='Dispatch to filing system control vector (FSCV)', description="""Indirect JMP through FSCV at &021E, providing
OS-level filing system services such as FS
selection notification (A=6) and *RUN handling.
Also contains issue_svc_15 and issue_svc_osbyte
entry points that issue paged ROM service requests
via OSBYTE &8F.""", on_entry={'a': 'FSCV reason code'})


d.subroutine(0x8D0C, 'check_credits_easter_egg', title='Easter egg: match *HELP keyword to author credits', description="""Matches the *HELP argument against a keyword
embedded in the credits data at
credits_keyword_start. Starts matching from offset
5 in the data (X=5) and checks each byte against
the command line text until a mismatch or X reaches
&0D. On a full match, prints the ANFS author
credits string: B Cockburn, J Dunn, B Robertson,
and J Wills, each terminated by CR.""")


d.subroutine(0x8DFE, 'clear_if_station_match', title='Clear stored station if parsed argument matches', description="""Parses a station number from the command line via
init_bridge_poll and compares it with the expected
station at &0E01 using EOR. If the parsed value
matches (EOR result is zero), clears &0E01. Called
by cmd_iam when processing a file server address
in the logon command.""", on_exit={'a': '0 if matched, non-zero if different'})


d.subroutine(0x8E76, 'osbyte_x0_y0', title='OSBYTE wrapper with X=0, Y=0', description="""Sets X=0 and Y=0 then branches to jmp_osbyte.
Called from the Econet OSBYTE dispatch chain to
handle OSBYTEs that require both X and Y cleared.
The unconditional BEQ (after LDY #0 sets Z)
reaches the JMP osbyte instruction at &8E71.""", on_entry={'a': 'OSBYTE number'}, on_exit={'x': '0', 'y': '0'})


d.subroutine(0x8E96, 'store_ws_page_count', title='Record workspace page count (capped at &21)', description="""Stores the workspace allocation from service 1
into offset &0F of the receive control block,
capping the value at &21 to prevent overflow into
adjacent workspace areas. Called by
svc_2_private_workspace after issuing the absolute
workspace claim service call.""", on_entry={'y': 'workspace page count from service 1'})


d.subroutine(0x8F40, 'init_adlc_and_vectors', title='Initialise ADLC and install extended vectors', description="""Reads the ROM pointer table via OSBYTE &A8,
writes vector addresses and ROM ID into the
extended vector table for NETV and one additional
vector, then restores any previous FS context.""")


d.subroutine(0x8F53, 'write_vector_entry', title='Install extended vector table entries', description="""Copies vector addresses from the dispatch table at
svc_dispatch_lo_offset+Y into the MOS extended
vector table pointed to by fs_error_ptr. For each
entry, writes address low, high, then the current
ROM ID from romsel_copy (&F4). Loops X times.
After the loop, stores &FF at &0D72 as an
installed flag, calls deselect_fs_if_active and
get_ws_page to restore FS state.""", on_entry={'x': 'number of vectors to install', 'y': 'starting offset in extended vector table'}, on_exit={'y': 'workspace page number + 1'})


d.subroutine(0x8F73, 'restore_fs_context', title='Restore FS context from saved workspace', description="""Copies 8 bytes (offsets 6 to &0D) from the saved
workspace at &0DFA back into the receive control
block via (net_rx_ptr). This restores the station
identity, directory handles, and library path after
a filing system reselection. Called by
svc_2_private_workspace during init,
deselect_fs_if_active during FS teardown, and
flip_set_station_boot.""")


d.subroutine(0x8F80, 'fscv_6_shutdown', title='Deselect filing system and save workspace', description="""If the filing system is currently selected
(bit 7 of &0D6C set), closes all open FCBs,
closes SPOOL/EXEC files via OSBYTE &77,
saves the FS workspace to page &10 shadow
with checksum, and clears the selected flag.""")


d.subroutine(0x8FB2, 'verify_ws_checksum', title='Verify workspace checksum integrity', description="""Sums bytes 0 to &76 of the workspace page via the
zero-page pointer at &CC/&CD and compares with the
stored value at offset &77. On mismatch, raises a
'net checksum' error (&AA). The checksummed page
holds open file information (preserved when NFS is
not the current filing system) and the current
printer type. Can only be reset by a control BREAK.
Preserves A, Y, and processor flags using PHP/PHA.
Called by 5 sites across format_filename_field,
adjust_fsopts_4bytes, and start_wipe_pass before
workspace access.""", on_exit={'a': 'preserved', 'y': 'preserved'})


d.subroutine(0x8FDD, 'print_station_id', title='Print Econet station number and clock status', description="""Uses print_inline to output 'Econet Station ',
then reads the station ID from offset 5 of the
receive control block and prints it as a decimal
number via print_num_no_leading. Tests ADLC
status register 2 (&FEA1) to detect the Econet
clock; if absent, appends ' No Clock' via a
second inline string. Finishes with OSNEWL.
Called by print_version_header and svc_3_auto_boot.""")


d.subroutine(0x911B, 'print_hex_byte', title='Print A as two hexadecimal digits', description="""Saves A on the stack, shifts right four times
to isolate the high nybble, calls
print_hex_nybble to print it, then restores
the full byte and falls through to
print_hex_nybble for the low nybble. Called by
print_5_hex_bytes, cmd_ex, cmd_dump, and
print_dump_header.""", on_entry={'a': 'byte to print'}, on_exit={'a': 'original byte value'})


d.subroutine(0x9124, 'print_hex_nybble', title='Print low nybble of A as hex digit', description="""Masks A to the low 4 bits, then converts to
ASCII: adds 7 for letters A-F (via ADC #6 with
carry set from the CMP), then ADC #&30 for the
final '0'-'F' character. Outputs via JMP OSASCI.""", on_entry={'a': 'value (low nybble used)'})


d.subroutine(0x915A, 'parse_addr_arg', title='Parse decimal or hex station address argument', description="""Reads from the command argument at (&BE),Y.
Supports '&' prefix for hex, '.' separator for
net.station addresses, and plain decimal.
Returns result in A. Raises errors for
bad digits, overflow, or zero values.""")


d.subroutine(0x9244, 'is_decimal_digit', title="Test for digit, '&', or '.' separator", description="""Compares A against '&' and '.' first; if
either matches, returns with carry set via the
shared return_12 exit. Otherwise falls through
to is_dec_digit_only for the '0'-'9' range
test. Called by cmd_iam, cmd_ps, and
cmd_pollps when parsing station addresses.""", on_entry={'a': 'character to test'}, on_exit={'c': 'set if digit/&/., clear otherwise'})


d.subroutine(0x924C, 'is_dec_digit_only', title="Test for decimal digit '0'-'9'", description="""Uses two CMPs to bracket-test A against the
range &30-&39. CMP #&3A sets carry if A >= ':'
(above digits), then CMP #&30 sets carry if
A >= '0'. The net effect: carry set only for
'0'-'9'. Called by parse_addr_arg.""", on_entry={'a': 'character to test'}, on_exit={'c': "set if '0'-'9', clear otherwise"})


d.subroutine(0x9255, 'get_access_bits', title='Read and encode directory entry access byte', description="""Loads the access byte from offset &0E of the
directory entry via (fs_options),Y, masks to 6
bits (AND #&3F), then sets X=4 and branches to
begin_prot_encode to map through the protection
bit encode table at &9272. Called by
check_and_setup_txcb for owner and public access.""", on_exit={'a': 'encoded access flags'})


d.subroutine(0x925F, 'get_prot_bits', title='Encode protection bits via lookup table', description="""Masks A to 5 bits (AND #&1F), sets X=&FF to
start at table index 0, then enters the shared
encoding loop at begin_prot_encode. Shifts out
each source bit and ORs in the corresponding
value from prot_bit_encode_table (&9272). Called
by send_txcb_swap_addrs and check_and_setup_txcb.""", on_entry={'a': 'raw protection bits (low 5 used)'}, on_exit={'a': 'encoded protection flags'})


d.subroutine(0x927D, 'set_text_and_xfer_ptr', title='Set OS text pointer then transfer parameters', description="""Stores X/Y into the MOS text pointer at
&F2/&F3, then falls through to set_xfer_params
and set_options_ptr to configure the full FS
transfer context. Called by byte_to_2bit_index.""", on_entry={'x': 'text pointer low byte', 'y': 'text pointer high byte'})


d.subroutine(0x9281, 'set_xfer_params', title='Set FS transfer byte count and source pointer', description="""Stores A into fs_last_byte_flag (&BD) as the
transfer byte count, and X/Y into fs_crc_lo/hi
(&BE/&BF) as the source data pointer. Falls
through to set_options_ptr to complete the
transfer context setup. Called by 5 sites across
cmd_ex, format_filename_field, and gsread_to_buf.""", on_entry={'a': 'transfer byte count', 'x': 'source pointer low', 'y': 'source pointer high'})


d.subroutine(0x9287, 'set_options_ptr', title='Set FS options pointer and clear escape flag', description="""Stores X/Y into fs_options/fs_block_offset
(&BB/&BC) as the options block pointer. Then
enters clear_escapable which uses PHP/LSR/PLP
to clear bit 0 of the escape flag at &97 without
disturbing processor flags. Called by
format_filename_field and send_and_receive.""", on_entry={'x': 'options pointer low', 'y': 'options pointer high'})


d.subroutine(0x9290, 'cmp_5byte_handle', title='Compare 5-byte handle buffers for equality', description="""Loops X from 4 down to 1, comparing each byte
of l00af+X with fs_load_addr_3+X using EOR.
Returns on the first mismatch (Z=0) or after
all 5 bytes match (Z=1). Called by
send_txcb_swap_addrs and check_and_setup_txcb
to verify station/handle identity.""", on_exit={'z': 'set if all 5 bytes match'})


d.subroutine(0x92A1, 'set_conn_active', title='Set connection-active flag in channel table', description="""Saves registers on the stack, recovers the
original A from the stack via TSX/LDA &0102,X,
then calls attr_to_chan_index to find the channel
slot. ORs bit 6 (&40) into the channel status
byte at &1060+X. Preserves A, X, and processor
flags via PHP/PHA/PLA/PLP. Called by
format_filename_field and adjust_fsopts_4bytes.""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x92B8, 'clear_conn_active', title='Clear connection-active flag in channel table', description="""Mirror of set_conn_active but ANDs the channel
status byte with &BF (bit 6 clear mask) instead
of ORing. Uses the same register-preservation
pattern: PHP/PHA/TSX to recover A, then
attr_to_chan_index to find the slot. Shares the
done_conn_flag exit with set_conn_active.""", on_entry={'a': 'channel attribute byte'})


d.subroutine(0x92F5, 'check_not_ampersand', title="Reject '&' as filename character", description="""Loads the first character from the parse buffer
at &0E30 and compares with '&' (&26). Branches
to error_bad_filename if matched, otherwise
returns. Also contains read_filename_char which
loops reading characters from the command line
into the TX buffer at &0F05, calling
strip_token_prefix on each byte and terminating
on CR. Used by cmd_fs_operation and cmd_rename.""")


d.subroutine(0x9313, 'copy_fs_cmd_name', title='Copy matched command name to TX buffer', description="""Scans backwards in cmd_table_fs from the
current position to find the bit-7 flag byte
marking the start of the command name. Copies
each character forward into the TX buffer at
&0F05 until the next bit-7 byte (end of name),
then appends a space separator. Called by
cmd_fs_operation and cmd_rename.""", on_exit={'x': 'TX buffer offset past name+space', 'y': 'command line offset (restored)'})


d.subroutine(0x9335, 'parse_quoted_arg', title='Parse possibly-quoted filename argument', description="""Reads from the command line at (&BE),Y. Handles
double-quote delimiters and stores the result
in the parse buffer at &0E30. Raises 'Bad string'
on unbalanced quotes.""")


d.subroutine(0x9451, 'init_txcb_bye', title='Set up open receive for FS reply on port &90', description="""Loads A=&90 (the FS command/reply port) and
falls through to init_txcb_port, which creates
an open receive control block: the template sets
txcb_ctrl to &80, then DEC makes it &7F (bit 7
clear = awaiting reply). The NMI RX handler sets
bit 7 when a reply arrives on this port, which
wait_net_tx_ack polls for.""")


d.subroutine(0x9453, 'init_txcb_port', title='Create open receive control block on specified port', description="""Calls init_txcb to copy the 12-byte template
into the TXCB workspace at &00C0, then stores A
as the port (txcb_port at &C1) and sets
txcb_start to 3. The DEC txcb_ctrl changes the
control byte from &80 to &7F (bit 7 clear),
creating an open receive: the NMI RX handler
will set bit 7 when a reply frame arrives on
this port, which wait_net_tx_ack polls for.""", on_entry={'a': 'port number'})


d.subroutine(0x945F, 'init_txcb', title='Initialise TX control block from ROM template', description="""Copies 12 bytes from txcb_init_template (&9477)
into the TXCB workspace at &00C0. For the first
two bytes (Y=0,1), also copies the destination
station/network from &0E00 into txcb_dest (&C2).
Preserves A via PHA/PLA. Called by 4 sites
including cmd_pass, init_txcb_port,
prep_send_tx_cb, and send_wipe_request.""")


d.subroutine(0x9483, 'send_request_nowrite', title='Send read-only FS request (carry set)', description="""Pushes A and sets carry to indicate no-write
mode, then branches to txcb_copy_carry_set to
enter the common TXCB copy, send, and reply
processing path. The carry flag controls whether
a disconnect is sent on certain reply codes.
Called by setup_transfer_workspace.""")


d.subroutine(0x9487, 'send_request_write', title='Send read-write FS request (V clear)', description="""Clears V flag and branches unconditionally to
txcb_copy_carry_clr (via BVC, always taken after
CLV) to enter the common TXCB copy, send, and
reply processing path with carry clear (write
mode). Called by do_fs_cmd_iteration and
send_txcb_swap_addrs.""")


d.subroutine(0x9499, 'save_net_tx_cb', title='Save FS state and send command to file server', description="""Copies station address and function code (Y)
to the TX buffer, builds the TXCB, sends the
packet, and waits for the reply. V is clear
for standard mode.""")


d.subroutine(0x949A, 'save_net_tx_cb_vset', title='Save and send TXCB with V flag set', description="""Variant of save_net_tx_cb for callers that have
already set V. Copies the FS station address
from &0E02 to &0F02, then falls through to
txcb_copy_carry_clr which clears carry and enters
the common TXCB copy, send, and reply path.
Called by check_and_setup_txcb,
format_filename_field, and cmd_remove.""")


d.subroutine(0x94C6, 'prep_send_tx_cb', title='Build TXCB from scratch, send, and receive reply', description="""Full send/receive cycle comprising two separate
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


d.subroutine(0x94DC, 'recv_and_process_reply', title='Receive FS reply and dispatch on status codes', description="""Waits for a server-initiated reply transaction.
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


d.subroutine(0x955A, 'check_escape', title='Check for pending escape condition', description="""ANDs the MOS escape flag (&FF) with the
escapable flag at &97. If bit 7 of the result
is clear (no escape or escape disabled), returns
immediately. Otherwise enters raise_escape_error:
acknowledges the escape via OSBYTE &7E, then
jumps to classify_reply_error with A=6 to raise
the Escape error. Called by cmd_pass and
send_net_packet.""")


d.subroutine(0x95C7, 'wait_net_tx_ack', title='Wait for reply on open receive with timeout', description="""Despite the name, this does not wait for a TX
acknowledgment. It polls an open receive control
block (bit 7 of txcb_ctrl, set to &7F by
init_txcb_port) until the NMI RX handler delivers
a reply frame and sets bit 7. Uses a three-level
nested polling loop: inner and middle counters
start at 0 (wrapping to 256 iterations each),
outer counter from rx_poll_count (&0D6F,
default &28 = 40). Total: 256 x 256 x 40 =
2,621,440 poll iterations. At ~17 cycles per
poll on a 2 MHz 6502, the default gives ~22
seconds. On timeout, branches to
build_no_reply_error to raise 'No reply'.
Called by 6 sites across the protocol stack.""")


d.subroutine(0x95FB, 'cond_save_error_code', title='Conditionally store error code to workspace', description="""Tests bit 7 of &0D6C (FS selected flag). If
clear, returns immediately. If set, stores A
into &0E09 as the last error code. This guards
against writing error state when no filing system
is active. Called internally by the error
classification chain and by error_inline_log.""", on_entry={'a': 'error code to store'})


d.subroutine(0x9738, 'append_drv_dot_num', title="Append 'net.station' decimal string to error text", description="""Reads network and station numbers from the TX
control block at offsets 3 and 2. Writes a space
separator then the network number (if non-zero),
a dot, and the station number as decimal digits
into the error text buffer at the current position.""", on_entry={'x': 'error text buffer index'}, on_exit={'x': 'updated buffer index past appended text'})


d.subroutine(0x975C, 'append_space_and_num', title='Append space and decimal number to error text', description="""Writes a space character to the error text buffer
at the current position (fs_load_addr_2), then falls
through to append_decimal_num to convert the value
in A to decimal digits with leading zero suppression.""", on_entry={'a': 'number to append (0-255)'})


d.subroutine(0x9767, 'append_decimal_num', title='Convert byte to decimal and append to error text', description="""Extracts hundreds, tens and units digits by three
successive calls to append_decimal_digit. Uses the
V flag to suppress leading zeros — hundreds and tens
are skipped when zero, but the units digit is always
emitted.""", on_entry={'a': 'number to convert (0-255)'})


d.subroutine(0x9778, 'append_decimal_digit', title='Extract and append one decimal digit', description="""Divides Y by A using repeated subtraction to extract
a single decimal digit. Stores the ASCII digit in the
error text buffer at fs_load_addr_2 unless V is set
and the quotient is zero (leading zero suppression).
Returns the remainder in Y for subsequent digit
extraction.""", on_entry={'a': 'divisor (100, 10, or 1)', 'y': 'number to divide', 'v': 'set to suppress leading zero'}, on_exit={'y': 'remainder after division', 'v': 'clear once a non-zero digit is emitted'})


d.subroutine(0x9822, 'init_tx_ptr_and_send', title='Point TX at zero-page TXCB and send', description="""Sets net_tx_ptr/net_tx_ptr_hi to &00C0 (the
standard TXCB location in zero page), then falls
through to send_net_packet for transmission with
retry logic.""")


d.subroutine(0x982A, 'send_net_packet', title='Transmit Econet packet with retry', description="""Two-phase transmit with retry. Loads retry count
from tx_retry_count (&0D6E, default &FF = 255;
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


d.subroutine(0x987F, 'init_tx_ptr_for_pass', title='Set up TX pointer and send pass-through packet', description="""Copies the template into the TX buffer (skipping
&FD markers), saves original values on stack,
then polls the ADLC and retries until complete.""")


d.subroutine(0x9887, 'setup_pass_txbuf', title='Initialise TX buffer from pass-through template', description="""Copies 12 bytes from pass_txbuf_init_table into the
TX control block, pushing the original values on the
stack for later restoration. Skips offsets marked &FD
in the template. Starts transmission via
poll_adlc_tx_status and retries on failure, restoring
the original TX buffer contents when done.""")


d.subroutine(0x98B4, 'poll_adlc_tx_status', title='Wait for TX ready, then start new transmission', description="""Polls tx_complete_flag via ASL (testing bit 7)
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


d.subroutine(0x98F3, 'load_text_ptr_and_parse', title='Copy text pointer from FS options and parse string', description="""Reads a 2-byte address from (fs_options)+0/1 into
os_text_ptr (&00F2), resets Y to zero, then falls
through to gsread_to_buf to parse the string at that
address into the &0E30 buffer.""")


d.subroutine(0x98FF, 'gsread_to_buf', title='Parse command line via GSINIT/GSREAD into &0E30', description="""Calls GSINIT to initialise string reading, then
loops calling GSREAD to copy characters into the
l0e30 buffer until end-of-string. Appends a CR
terminator and sets fs_crc_lo/hi to point at &0E30
for subsequent parsing routines.""")


d.subroutine(0x993D, 'do_fs_cmd_iteration', title='Execute one iteration of a multi-step FS command', description="""Called by match_fs_cmd for commands that enumerate
directory entries. Sets port &92, sends the initial
request via send_request_write, then synchronises the
FS options and workspace state (order depends on the
cycle flag at offset 6). Copies 4 address bytes,
formats the filename field, sends via
send_txcb_swap_addrs, and receives the reply.""")


d.subroutine(0x9984, 'send_txcb_swap_addrs', title='Send TXCB and swap start/end addresses', description="""If the 5-byte handle matches, returns
immediately. Otherwise sets port &92, copies
addresses, sends, waits for acknowledgment,
and retries on address mismatch.""")


d.subroutine(0x9A45, 'print_load_exec_addrs', title='Print exec address and file length in hex', description="""Prints the exec address as 5 hex bytes from
(fs_options) offset 9 downwards, then the file
length as 3 hex bytes from offset &0C. Each group
is followed by a space separator via OSASCI.""")


d.subroutine(0x9A50, 'print_5_hex_bytes', title='Print hex byte sequence from FS options', description="""Outputs X+1 bytes from (fs_options) starting at
offset Y, decrementing Y for each byte (big-endian
display order). Each byte is printed as two hex
digits via print_hex_byte. Finishes with a trailing
space via OSASCI. The default entry with X=4 prints
5 bytes (a full 32-bit address plus extent).""", on_entry={'x': 'byte count minus 1 (default 4 for 5 bytes)', 'y': 'starting offset in (fs_options)'})


d.subroutine(0x9A60, 'copy_fsopts_to_zp', title='Copy FS options address bytes to zero page', description="""Copies 4 bytes from (fs_options) at offsets 2-5
into zero page at &00AE+Y. Used by
do_fs_cmd_iteration to preserve the current address
state. Falls through to skip_one_and_advance5 to
advance Y past the copied region.""")


d.subroutine(0x9A6C, 'skip_one_and_advance5', title='Advance Y by 5', description="""Entry point one INY before advance_y_by_4, giving
a total Y increment of 5. Used to skip past a
5-byte address/length structure in the FS options
block.""")


d.subroutine(0x9A6D, 'advance_y_by_4', title='Advance Y by 4', description="""Four consecutive INY instructions. Used as a
subroutine to step Y past a 4-byte address field
in the FS options or workspace structure.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset + 4'})


d.subroutine(0x9A72, 'copy_workspace_to_fsopts', title='Copy workspace reply data to FS options', description="""Copies bytes from the reply buffer at &0F02+Y
into (fs_options) at offsets &0D down to 2. Used
to update the FS options block with data returned
from the file server. Falls through to
retreat_y_by_4.""")


d.subroutine(0x9A7F, 'retreat_y_by_4', title='Retreat Y by 4', description="""Four consecutive DEY instructions. Companion to
advance_y_by_4 for reverse traversal of address
structures.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 4'})


d.subroutine(0x9A80, 'retreat_y_by_3', title='Retreat Y by 3', description="""Three consecutive DEY instructions. Used by
setup_transfer_workspace to step back through
interleaved address pairs in the FS options block.""", on_entry={'y': 'current offset'}, on_exit={'y': 'offset - 3'})


d.subroutine(0x9A88, 'check_and_setup_txcb', title='Set up data transfer TXCB and dispatch reply', description="""Compares the 5-byte handle; if unchanged,
returns. Otherwise computes start/end addresses
with overflow clamping, sets the port and control
byte, sends the packet, and dispatches on the
reply sub-operation code.""")


d.subroutine(0x9B86, 'format_filename_field', title='Format filename into fixed-width display field', description="""Builds a 12-character space-padded filename at
&10F3 for directory listing output. Sources the
name from either the command line or the l0f05
reply buffer depending on the value in l0f03.
Truncates or pads to exactly 12 characters.""")


d.subroutine(0x9E03, 'update_addr_from_offset9', title='Update both address fields in FS options', description="""Calls add_workspace_to_fsopts for offset 9 (the
high address / exec address field), then falls
through to update_addr_from_offset1 to process
offset 1 (the low address / load address field).""")


d.subroutine(0x9E08, 'update_addr_from_offset1', title='Update low address field in FS options', description="""Sets Y=1 and falls through to
add_workspace_to_fsopts to add the workspace
adjustment bytes to the load address field at
offset 1 in the FS options block.""", on_entry={'c': 'carry state passed to add_workspace_to_fsopts'})


d.subroutine(0x9E0A, 'add_workspace_to_fsopts', title='Add workspace bytes to FS options with clear carry', description="""Clears carry and falls through to
adjust_fsopts_4bytes. Provides a convenient entry
point when the caller needs addition without a
preset carry.""", on_entry={'y': 'FS options offset for first byte'})


d.subroutine(0x9E0B, 'adjust_fsopts_4bytes', title='Add or subtract 4 workspace bytes from FS options', description="""Processes 4 consecutive bytes at (fs_options)+Y,
adding or subtracting the corresponding workspace
bytes from &0E0A-&0E0D. The direction is controlled
by bit 7 of fs_load_addr_2: set for subtraction,
clear for addition. Carry propagates across all 4
bytes for correct multi-byte arithmetic.""", on_entry={'y': 'FS options offset for first byte', 'c': 'carry input for first byte'})


d.subroutine(0x9EC0, 'lookup_cat_entry_0', title='Look up channel from FS options offset 0', description="""Loads the channel handle from (fs_options) at
offset 0, then falls through to lookup_cat_slot_data
to find the corresponding FCB entry.""", on_exit={'a': 'FCB flag byte from &1030+X', 'x': 'channel slot index'})


d.subroutine(0x9EC4, 'lookup_cat_slot_data', title='Look up channel and return FCB flag byte', description="""Calls lookup_chan_by_char to find the channel
slot for handle A in the channel table, then
loads the FCB flag byte from &1030+X.""", on_entry={'a': 'channel handle'}, on_exit={'a': 'FCB flag byte', 'x': 'channel slot index'})


d.subroutine(0x9ECB, 'setup_transfer_workspace', title='Prepare workspace for OSGBPB data transfer', description="""Orchestrates the setup for OSGBPB (get/put
multiple bytes) operations. Looks up the channel,
copies the 6-byte address structure from FS options
(skipping the hole at offset 8), determines transfer
direction from the operation code (even=read,
odd=write), selects port &91 or &92 accordingly,
and sends the FS request. Then configures the TXCB
address pairs for the actual data transfer phase
and dispatches to the appropriate handler.""")


d.subroutine(0x9FB8, 'write_data_block', title='Write data block to destination or Tube', description="""If no Tube present, copies directly from
the l0f05 buffer via (fs_crc_lo). If Tube
is active, claims the Tube, sets up the
transfer address, and writes via R3.""")


d.subroutine(0xA05B, 'tube_claim_c3', title='Claim the Tube via protocol &C3', description="""Loops calling tube_addr_data_dispatch with
protocol byte &C3 until the claim succeeds
(carry set on return). Used before Tube data
transfers to ensure exclusive access to the
Tube co-processor interface.""")


d.subroutine(0xA086, 'print_fs_info_newline', title='Print station address and newline', description="""Sets V (suppressing leading-zero padding on
the network number) then prints the station
address followed by a newline via OSNEWL.
Used by *FS and *PS output formatting.""")


d.subroutine(0xA08F, 'parse_fs_ps_args', title='Parse station address from *FS/*PS arguments', description="""Reads a station address in 'net.station' format
from the command line, with the network number
optional (defaults to local network). Calls
init_bridge_poll to ensure the bridge routing
table is populated, then validates the parsed
address against known stations.""")


d.subroutine(0xA0B4, 'get_pb_ptr_as_index', title='Convert parameter block pointer to table index', description="""Reads the first byte from the OSWORD parameter
block pointer and falls through to
byte_to_2bit_index to produce a 12-byte-aligned
table index in Y.""")


d.subroutine(0xA0B6, 'byte_to_2bit_index', title='Convert byte to 12-byte-aligned table index', description="""Computes Y = A * 6 (via A*12/2) for indexing
into the OSWORD handler workspace tables.
Clamps Y to zero if the result exceeds &48,
preventing out-of-bounds access.""", on_entry={'a': 'table entry number'}, on_exit={'y': 'byte offset (0, 6, 12, ... up to &42)'})


d.subroutine(0xA128, 'match_fs_cmd', title='Match command name against FS command table', description="""Case-insensitive compare of the command line
against table entries with bit-7-terminated
names. Returns with the matched entry address
on success.""")


d.subroutine(0xA2E8, 'find_station_bit2', title='Find printer server station in table (bit 2)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 2 set (printer server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""")


d.subroutine(0xA313, 'find_station_bit3', title='Find file server station in table (bit 3)', description="""Scans the 16-entry station table for a slot
matching the current station/network address
with bit 3 set (file server active). Sets V
if found, clears V if not. Falls through to
allocate or update the matching slot with the
new station address and status flags.""")


d.subroutine(0xA34A, 'flip_set_station_boot', title='Set boot option for a station in the table', description="""Scans up to 16 station table entries for one
matching the current address with bit 4 set
(boot-eligible). Stores the requested boot type
in the matching entry and calls
restore_fs_context to re-establish the filing
system state.""")


d.subroutine(0xA4EF, 'osword_setup_handler', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD dispatch table by X to
push a handler address (hi then lo) onto the
stack. Copies 3 bytes from the osword_flag
workspace into the RX buffer, loads PB byte 0
(the OSWORD sub-code), and clears svc_state.
The subsequent RTS dispatches to the pushed
handler address.""", on_entry={'x': 'OSWORD handler index (0-6)'})


d.subroutine(0xA57C, 'bin_to_bcd', title='Convert binary byte to BCD', description="""Uses decimal mode (SED) with a count-up loop:
starts at BCD 0 and adds 1 in decimal mode for
each decrement of the binary input. Saves and
restores the processor flags to avoid leaving
decimal mode active. Called 6 times by
save_txcb_and_convert for clock date/time
conversion.""", on_entry={'a': 'binary value (0-99)'}, on_exit={'a': 'BCD equivalent'})


d.subroutine(0xA601, 'store_osword_pb_ptr', title='Store OSWORD parameter block pointer+1 to workspace', description="""Computes PB pointer + 1 and stores the resulting
16-bit address at workspace offset &1C via
store_ptr_at_ws_y. Then reads PB byte 1 (the
transfer length) and adds the PB low byte to
compute the buffer end pointer, stored at
workspace offset &20.""")


d.subroutine(0xA612, 'store_ptr_at_ws_y', title='Store 16-bit pointer at workspace offset Y', description="""Writes a 16-bit address to (nfs_workspace)+Y.
The low byte comes from A; the high byte is
computed from osword_pb_ptr_hi plus carry,
supporting pointer arithmetic across page
boundaries.""", on_entry={'a': 'pointer low byte', 'y': 'workspace offset', 'c': 'carry for high byte addition'})


d.subroutine(0xA6FB, 'copy_pb_byte_to_ws', title='Conditionally copy parameter block byte to workspace', description="""If carry is set, loads a byte from the OSWORD
parameter block at offset Y; if clear, uses
the value already in A. Stores the result to
workspace at the current offset. Decrements X
and loops until the requested byte count is
transferred.""", on_entry={'c': 'set to load from PB, clear to use A', 'x': 'byte count', 'y': 'PB source offset'})


d.subroutine(0xA663, 'osword_13_read_station', title='OSWORD &13 sub 0: read file server station', description="""Returns the current file server station and
network numbers in PB[1..2]. If the NFS is not
active (l0d6c bit 7 clear), returns zero in
PB[0] instead.""")


d.subroutine(0xA676, 'osword_13_set_station', title='OSWORD &13 sub 1: set file server station', description="""Sets the file server station and network
numbers from PB[1..2]. Processes all FCBs,
then scans the 16-entry FCB table to
reassign handles matching the new station.
If the NFS is not active, returns zero.""")


d.subroutine(0xA6EB, 'osword_13_read_csd', title='OSWORD &13 sub 12: read CSD path', description="""Reads 5 current selected directory path bytes
from the RX workspace at offset &1B into
PB[1..5]. Sets carry clear to select the
workspace-to-PB copy direction.""")


d.subroutine(0xA6EE, 'osword_13_write_csd', title='OSWORD &13 sub 13: write CSD path', description="""Writes 5 current selected directory path bytes
from PB[1..5] into the RX workspace at offset
&1B. Sets carry to select the PB-to-workspace
copy direction.""")


d.subroutine(0xA70A, 'osword_13_read_ws_pair', title='OSWORD &13 sub 2: read workspace byte pair', description="""Reads 2 bytes from the NFS workspace page
starting at offset 1 into PB[1..2]. Uses
nfs_workspace_hi as the page and
copy_pb_byte_to_ws with carry clear for the
workspace-to-PB direction.""")


d.subroutine(0xA716, 'osword_13_write_ws_pair', title='OSWORD &13 sub 3: write workspace byte pair', description="""Writes 2 bytes from PB[1..2] into the NFS
workspace at offsets 2 and 3. Then calls
init_bridge_poll and conditionally clears
the workspace byte if the bridge status
changed.""")


d.subroutine(0xA72B, 'osword_13_read_prot', title='OSWORD &13 sub 4: read protection mask', description="""Returns the current protection mask (ws_0d68)
in PB[1].""")


d.subroutine(0xA731, 'osword_13_write_prot', title='OSWORD &13 sub 5: write protection mask', description="""Sets the protection mask from PB[1] via
store_prot_mask.""")


d.subroutine(0xA737, 'osword_13_read_handles', title='OSWORD &13 sub 6: read FCB handle info', description="""Returns the 3-byte FCB handle/port data from
l1071[1..3] in PB[1..3]. If the NFS is not
active, returns zero in PB[0].""")


d.subroutine(0xA747, 'osword_13_set_handles', title='OSWORD &13 sub 7: set FCB handles', description="""Validates and assigns up to 3 FCB handles
from PB[1..3]. Each handle value (&20-&2F)
indexes the l1010/l1040 tables. For valid
handles with bit 2 set in l1040, stores the
station to l0e01+Y and FCB index to l1071+Y,
then updates flag bits across all FCB entries
via update_fcb_flag_bits.""")


d.subroutine(0xA7C2, 'update_fcb_flag_bits', title='Update FCB flag bits across all entries', description="""Scans all 16 FCB entries in l1060. For each
entry with bit 6 set, tests the Y-specified
bit mask: if matching, ORs bit 5 into the
flags; if not, leaves bit 5 clear. In both
cases, inverts and clears the tested bits.
Preserves X.""", on_entry={'y': 'flag bit mask to test', 'x': 'current FCB index (preserved)'})


d.subroutine(0xA7E7, 'osword_13_read_rx_flag', title='OSWORD &13 sub 8: read RX control block flag', description="""Returns byte 5 of the current RX control
block in PB[1].""")


d.subroutine(0xA7F0, 'osword_13_read_rx_port', title='OSWORD &13 sub 9: read RX port byte', description="""Returns byte &7F of the current RX control
block in PB[1], and stores &80 in PB[2].""")


d.subroutine(0xA7FE, 'osword_13_read_error', title='OSWORD &13 sub 10: read error flag', description='Returns the error flag (l0e09) in PB[1].')


d.subroutine(0xA804, 'osword_13_read_context', title='OSWORD &13 sub 11: read context byte', description='Returns the context byte (l0d6d) in PB[1].')


d.subroutine(0xA80A, 'osword_13_read_free_bufs', title='OSWORD &13 sub 14: read printer buffer free space', description="""Returns the number of free bytes remaining in
the printer spool buffer (&6F minus spool_buf_idx)
in PB[1]. The buffer starts at offset &25 and can
hold up to &4A bytes of spool data.""")


d.subroutine(0xA814, 'osword_13_read_ctx_3', title='OSWORD &13 sub 15: read retry counts', description="""Returns the three retry count values in
PB[1..3]: PB[1] = transmit retry count
(default &FF = 255), PB[2] = receive poll
count (default &28 = 40), PB[3] = machine
peek retry count (default &0A = 10). Setting
transmit retries to 0 means retry forever.""")


d.subroutine(0xA81F, 'osword_13_write_ctx_3', title='OSWORD &13 sub 16: write retry counts', description="""Sets the three retry count values from
PB[1..3]: PB[1] = transmit retry count,
PB[2] = receive poll count, PB[3] = machine
peek retry count.""")


d.subroutine(0xA82A, 'osword_13_bridge_query', title='OSWORD &13 sub 17: query bridge status', description="""Calls init_bridge_poll, then returns the
bridge status. If l0d72 is &FF (no bridge),
stores 0 in PB[0]. Otherwise stores l0d72
in PB[1] and conditionally updates PB[3]
based on station comparison.""")


d.subroutine(0xA868, 'init_bridge_poll', title='Initialise Econet bridge routing table', description="""Checks the bridge status byte: if &FF
(uninitialised), broadcasts a bridge query
packet and polls for replies. Each reply
adds a network routing entry to the bridge
table. Skips the broadcast if the table has
already been populated from a previous call.""")


d.subroutine(0xA964, 'enable_irq_and_poll', title='Enable interrupts and send Econet packet', description="""Executes CLI to re-enable interrupts, then
falls through to send_net_packet. Used after
a sequence that ran with interrupts disabled
to ensure the packet is sent with normal
interrupt handling active.""")


d.subroutine(0xA968, 'netv_handler', title='NETV handler: OSWORD dispatch', description="""Installed as the NETV handler via
write_vector_entry. Saves all registers, reads
the OSWORD number from the stack, and dispatches
OSWORDs 0-8 via push_osword_handler_addr. OSWORDs
>= 9 are ignored (registers restored, RTS returns
to MOS). Address stored at netv_handler_addr
(&8E74) in the extended vector data area.""")


d.subroutine(0xA981, 'push_osword_handler_addr', title='Push OSWORD handler address for RTS dispatch', description="""Indexes the OSWORD handler dispatch table
using the current OSWORD number to push the
handler's address (hi/lo) onto the stack.
Reloads the OSWORD number from osbyte_a_copy
so the dispatched handler can identify the
specific call.""")


d.subroutine(0xA99E, 'osword_4_handler', title='OSWORD 4 handler: clear carry and send abort', description="""Clears the carry flag in the stacked processor
status, stores the original Y to workspace at
offset &DA, and falls through to tx_econet_abort
with A=0. Called via OSWORD handler dispatch
table for OSWORD 4 (write interval timer).""")


d.subroutine(0xA9AC, 'tx_econet_abort', title='Send Econet abort/disconnect packet', description="""Stores the abort code in workspace, configures
the TX control block with control byte &80
(immediate operation flag), and transmits the
abort packet. Used to cleanly disconnect from
a remote station during error recovery.""")


d.subroutine(0xA9D0, 'netv_claim_release', title='OSWORD 7 handler: claim/release network resources', description="""Handles OSWORD 7 (SOUND) intercepted via NETV.
Searches the claim code table in two passes:
first 11 entries (state 2), then all 18 (state
3). On match, saves 3 tube state bytes to
workspace and sends an abort with the state
code. For state 3 matches, also polls workspace
for a response and restores the caller's stack
frame from the saved bytes.""")


d.subroutine(0xAA24, 'match_rx_code', title='Search receive code table for match', description="""Scans a table of receive operation codes
starting at index X, comparing each against A.
Returns with Z set if a match is found, Z clear
if the end-of-table marker is reached.""", on_entry={'a': 'receive code to match', 'x': 'starting table index'}, on_exit={'z': 'set if match found'})


d.subroutine(0xAA3F, 'osword_8_handler', title='OSWORD 7/8 handler: copy PB to workspace and abort', description="""Handles OSWORD 7 or 8 by copying 15 bytes from
the parameter block to workspace at offset &DB,
storing the OSWORD number at offset &DA, setting
control value &E9, and sending an abort packet.
Returns via tx_econet_abort. Rejects other
OSWORD numbers by returning immediately.""")


d.subroutine(0xAA6A, 'init_ws_copy_wide', title='Initialise workspace copy in wide mode (14 bytes)', description="""Copies 14 bytes to workspace offset &7C.
Falls through to the template-driven copy
loop which handles &FD (skip), &FE (end),
and &FC (page pointer) markers.""")


d.subroutine(0xAA73, 'init_ws_copy_narrow', title='Initialise workspace copy in narrow mode (27 bytes)', description="""Sets up a 27-byte copy to workspace offset &17,
then falls through to ws_copy_vclr_entry for
the template-driven copy loop. Used for the
compact workspace initialisation variant.""")


d.subroutine(0xAA77, 'ws_copy_vclr_entry', title='Template-driven workspace copy with V clear', description="""Processes a template byte array to initialise
workspace. Special marker bytes: &FE terminates
the copy, &FD skips the current offset, and &FC
substitutes the workspace page pointer. All
other values are stored directly to the
workspace at the current offset.""")


d.subroutine(0xAAC6, 'netv_spool_check', title='OSWORD 5 handler: check spool PB and reset buffer', description="""Handles OSWORD 5 intercepted via NETV. Checks
if X-1 matches osword_pb_ptr and bit 0 of
&00D0 is clear. If both conditions are met,
falls through to reset_spool_buf_state to
reinitialise the spool buffer for new data.""")


d.subroutine(0xAADB, 'netv_print_data', title='OSWORD 1-3 handler: drain printer buffer', description="""Handles OSWORDs 1-3 intercepted via NETV.
When X=1, drains the printer buffer (OSBYTE
&91, buffer 3) into the receive buffer, sending
packets via process_spool_data when the buffer
exceeds &6E bytes. When X>1, routes to
handle_spool_ctrl_byte for spool state control.""")


d.subroutine(0xAAD0, 'reset_spool_buf_state', title='Reset spool buffer to initial state', description="""Sets the spool buffer pointer to &25 (first
available data position) and the control state
byte to &41 (ready for new data). Called after
processing a complete spool data block.""")


d.subroutine(0xAB00, 'append_byte_to_rxbuf', title='Append byte to receive buffer', description="""Stores A in the receive buffer at the current
buffer index (ws_ptr_lo), then increments the
index. Used to accumulate incoming spool data
bytes before processing.""", on_entry={'a': 'byte to append'})


d.subroutine(0xAB09, 'handle_spool_ctrl_byte', title='Handle spool control byte and flush buffer', description="""Rotates bit 0 of the control byte into carry
for mode selection (print vs spool), appends
the byte to the buffer, calls process_spool_data
to transmit the accumulated data, and resets
the buffer state ready for the next block.""")


d.subroutine(0xAB24, 'process_spool_data', title='Transmit accumulated spool buffer data', description="""Copies the workspace state to the TX control
block, sends a disconnect reply if the previous
transfer requires acknowledgment, then handles
the spool output sequence by setting up and
sending the pass-through TX buffer.""")


d.subroutine(0xAC12, 'send_disconnect_reply', title='Send Econet disconnect reply packet', description="""Sets up the TX pointer, copies station
addresses, matches the station in the table,
and sends the response. Waits for
acknowledgment before returning.""")


d.subroutine(0xACCB, 'commit_state_byte', title='Copy current state byte to committed state', description="""Reads the working state byte from workspace and
stores it to the committed state location. Used
to finalise a state transition after all related
workspace fields have been updated.""")


d.subroutine(0xACD2, 'serialise_palette_entry', title='Serialise palette register to workspace', description="""Reads the current logical colour for a palette
register via OSBYTE &0B and stores both the
palette value and the display mode information
in the workspace block. Used during remote
screen state capture.""")


d.subroutine(0xACE5, 'read_osbyte_to_ws_x0', title='Read OSBYTE with X=0 and store to workspace', description="""Sets X=0 then falls through to read_osbyte_to_ws
to issue the OSBYTE call and store the result.
Used when the OSBYTE parameter X must be zero.""")


d.subroutine(0xACE7, 'read_osbyte_to_ws', title='Issue OSBYTE from table and store result', description="""Loads the OSBYTE function code from the next
entry in the OSBYTE table, issues the call, and
stores the Y result in workspace at the current
offset. Advances the table pointer for the next
call.""")


d.subroutine(0xAE70, 'print_10_chars', title='Print 10 characters from reply buffer', description="""Sets Y=10 and falls through to
print_chars_from_buf. Used by cmd_ex to print
fixed-width directory title, directory name, and
library name fields.""", on_entry={'x': 'buffer offset to start printing from'})


d.subroutine(0xAE72, 'print_chars_from_buf', title='Print Y characters from buffer via OSASCI', description="""Loops Y times, loading each byte from l0f05+X
and printing it via OSASCI. Advances X after
each character, leaving X pointing past the
last printed byte.""", on_entry={'x': 'buffer offset', 'y': 'character count'})


d.subroutine(0xAE80, 'parse_cmd_arg_y0', title='Parse command argument from offset zero', description="""Sets Y=0 and falls through to parse_filename_arg
for GSREAD-based filename parsing with prefix
character handling.""")


d.subroutine(0xAE82, 'parse_filename_arg', title='Parse filename via GSREAD with prefix handling', description="""Calls gsread_to_buf to read the command line
string into the &0E30 buffer, then falls through
to parse_access_prefix to process '&', ':', '.',
and '#' prefix characters.""")


d.subroutine(0xAE85, 'parse_access_prefix', title='Parse access and FS selection prefix characters', description="""Examines the first character(s) of the parsed
buffer at &0E30 for prefix characters: '&' sets
the FS selection flag (bit 6 of l1071) and strips
the prefix, ':' with '.' also triggers FS
selection, '#' is accepted as a channel prefix.
Raises 'Bad file name' for invalid combinations
like '&.' followed by CR.""")


d.subroutine(0xAEA5, 'strip_token_prefix', title='Strip first character from parsed token buffer', description="""Shifts all bytes in the &0E30 buffer left by
one position (removing the first character),
then trims any trailing spaces by replacing
them with CR terminators. Used after consuming
a prefix character like '&' or ':'.""")


d.subroutine(0xAEF0, 'copy_arg_to_buf_x0', title='Copy argument to TX buffer from offset zero', description="""Sets X=0 and falls through to copy_arg_to_buf
then copy_arg_validated. Provides the simplest
entry point for copying a single parsed argument
into the TX buffer at position zero.""")


d.subroutine(0xAEF2, 'copy_arg_to_buf', title='Copy argument to TX buffer with Y=0', description="""Sets Y=0 and falls through to copy_arg_validated
with carry set, enabling '&' character validation.
X must already contain the destination offset
within the TX buffer.""")


d.subroutine(0xAEF4, 'copy_arg_validated', title='Copy command line characters to TX buffer', description="""Copies characters from (fs_crc_lo)+Y to l0f05+X
until a CR terminator is reached. With carry set,
validates each character against '&' — raising
'Bad file name' if found — to prevent FS selector
characters from being embedded in filenames.""", on_entry={'x': 'TX buffer destination offset', 'y': 'command line source offset', 'c': "set to enable '&' validation"})


d.subroutine(0xAF12, 'mask_owner_access', title='Clear FS selection flags from options word', description="""ANDs the l1071 flags byte with &1F, clearing
the FS selection flag (bit 6) and other high
bits to retain only the 5-bit owner access
mask. Called before parsing to reset the prefix
state from a previous command.""")


d.subroutine(0xAF27, 'ex_print_col_sep', title='Print column separator or newline for *Ex/*Cat', description="""In *Cat mode, increments a column counter modulo 4
and prints a two-space separator between entries,
with a newline at the end of each row. In *Ex
mode (fs_spool_handle negative), prints a newline
after every entry. Scans the entry data and loops
back to print the next entry's characters.""")


d.subroutine(0xAF65, 'print_num_no_leading', title='Print decimal number with leading zero suppression', description="""Sets V via BIT bit_test_ff to enable leading
zero suppression, then falls through to
print_decimal_3dig. Used by print_station_id
for compact station number display.""", on_entry={'a': 'number to print (0-255)'})


d.subroutine(0xAF68, 'print_decimal_3dig', title='Print byte as 3-digit decimal via OSASCI', description="""Extracts hundreds, tens and units digits by
successive calls to print_decimal_digit. The V
flag controls leading zero suppression: if set,
zero digits are skipped until a non-zero digit
appears. V is always cleared before the units
digit to ensure at least one digit is printed.""", on_entry={'a': 'number to print (0-255)', 'v': 'set to suppress leading zeros'})


d.subroutine(0xAF76, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Initialises X to '0'-1 and loops, incrementing X
while subtracting the divisor from Y. On underflow,
adds back the divisor to get the remainder in Y.
If V is set, suppresses leading zeros by skipping
the OSASCI call when the digit is '0'.""", on_entry={'a': 'divisor', 'y': 'value to divide'}, on_exit={'y': 'remainder after division'})


d.subroutine(0xAF95, 'save_ptr_to_os_text', title='Copy text pointer to OS text pointer workspace', description="""Saves fs_crc_lo/hi into the MOS text pointer
locations at &00F2/&00F3. Preserves A on the
stack. Called before GSINIT/GSREAD sequences
that need to parse from the current command
line position.""")


d.subroutine(0xAFA1, 'skip_to_next_arg', title='Advance past spaces to the next command argument', description="""Scans (fs_crc_lo)+Y for space characters,
advancing Y past each one. Returns with A
holding the first non-space character, or CR
if the end of line is reached. Used by *CDir
and *Remove to detect extra arguments.""", on_exit={'a': 'first non-space character or CR', 'y': 'offset of that character'})


d.subroutine(0xAFB5, 'save_ptr_to_spool_buf', title='Copy text pointer to spool buffer pointer', description="""Saves fs_crc_lo/hi into fs_options/fs_block_offset
for use as the spool buffer pointer. Preserves A
on the stack. Called by *PS and *PollPS before
parsing their arguments.""")


d.subroutine(0xAFC0, 'init_spool_drive', title='Initialise spool drive page pointers', description="""Calls get_ws_page to read the workspace page
number for the current ROM slot, stores it as
the spool drive page high byte (l00af), and
clears the low byte (l00ae) to zero. Preserves
Y on the stack.""")


d.subroutine(0xAFF7, 'copy_ps_data_y1c', title='Copy printer server template at offset &1C', description="""Sets Y=&1C and falls through to copy_ps_data.
Called during workspace initialisation
(svc_2_private_workspace) to set up the printer
server template at the standard offset.""")


d.subroutine(0xAFF9, 'copy_ps_data', title='Copy 8-byte printer server template to RX buffer', description="""Copies 8 bytes of default printer server data
into the RX buffer at the current Y offset.
Uses indexed addressing: LDA ps_template_base,X
with X starting at &F8, so the effective read
address is ps_template_base+&F8 = ps_template_data
(&8E43). This 6502 trick reaches data 248 bytes
past the base label using a single instruction.""")


d.subroutine(0xB0A1, 'print_file_server_is', title="Print 'File server ' prefix", description="""Uses print_inline to output 'File' then falls through
to the shared ' server is ' suffix at
print_printer_server_is.""")


d.subroutine(0xB0AB, 'print_printer_server_is', title="Print 'Printer server is ' prefix", description="""Uses print_inline to output the full label
'Printer server is ' with trailing space.""")


d.subroutine(0xB0C6, 'load_ps_server_addr', title='Load printer server address from workspace', description="""Reads the station and network bytes from workspace
offsets 2 and 3 into the station/network variables.""")


d.subroutine(0xB0D2, 'pop_requeue_ps_scan', title='Pop return address and requeue PS slot scan', description="""Converts the PS slot flags to a workspace index,
writes slot data, and jumps back into the PS scan
loop to continue processing.""")


d.subroutine(0xB13A, 'write_ps_slot_byte_ff', title='Write buffer page byte and two &FF markers', description="""Stores the buffer page byte at the current Y offset
in workspace, followed by two &FF sentinel bytes.
Advances Y after each write.""")


d.subroutine(0xB141, 'write_two_bytes_inc_y', title='Write A to two consecutive workspace bytes', description="""Stores A at the current Y offset via (nfs_workspace),Y
then again at Y+1, advancing Y after each write.""", on_entry={'a': 'byte to store', 'y': 'workspace offset'})


d.subroutine(0xB149, 'reverse_ps_name_to_tx', title='Reverse-copy printer server name to TX buffer', description="""Copies 8 bytes from the RX buffer (offsets &1C-&23)
to the TX buffer (offsets &13-&1B) in reversed byte
order, pushing onto the stack then popping back.""")


d.subroutine(0xB174, 'print_station_addr', title='Print station address as decimal net.station', description="""If the network number is zero, prints only the
station number. Otherwise prints network.station
separated by a dot. V flag controls padding with
leading spaces for column alignment.""")


d.subroutine(0xB2C4, 'init_ps_slot_from_rx', title='Initialise PS slot buffer from template data', description="""Copies the 12-byte ps_slot_txcb_template (&B193)
into workspace at offsets &78-&83 via indexed
addressing from write_ps_slot_link_addr (write_ps_slot_hi_link+1).
Substitutes net_rx_ptr_hi at offsets &7D and &81
(the hi bytes of the two buffer pointers) so they
point into the current RX buffer page.""")


d.subroutine(0xB2DB, 'store_char_uppercase', title='Convert to uppercase and store in RX buffer', description="""If the character in A is lowercase (&61-&7A), converts
to uppercase by clearing bit 5. Stores the result in
the RX buffer at the current position, advances the
buffer pointer, and decrements the character count.""", on_entry={'a': 'character to store'})


d.subroutine(0xB41F, 'flush_and_read_char', title='Flush keyboard buffer and read one character', description="""Calls OSBYTE &0F to flush the input buffer, then
OSRDCH to read a single character. Raises an escape
error if escape was pressed (carry set on return).""")


d.subroutine(0xB42F, 'unused_clear_ws_78', title='Dead code: clear 120 bytes of workspace', description="""Unreferenced subroutine. Zeroes offsets &00-&77
(120 bytes) of the workspace page pointed to by
l00cc. Superseded by loop_zero_workspace (&8ED5)
which clears a full 256-byte page via both l00cc
and nfs_workspace pointers.""")


d.subroutine(0xB439, 'init_channel_table', title='Initialise channel allocation table', description="""Clears all 256 bytes of the table, then marks
available channel slots based on the count from
the receive buffer. Sets the first slot to &C0
(active channel marker).""")


d.subroutine(0xB45B, 'attr_to_chan_index', title='Convert channel attribute to table index', description="""Subtracts &20 from the attribute byte and clamps
to the range 0-&0F. Returns &FF if out of range.
Preserves processor flags via PHP/PLP.""", on_entry={'a': 'channel attribute byte'}, on_exit={'a': 'table index (0-&0F) or &FF if invalid'})


d.subroutine(0xB46A, 'check_chan_char', title='Validate channel character and look up entry', description="""Characters below '0' are looked up directly in
the channel table. Characters '0' and above are
converted to a table index via attr_to_chan_index.
Raises 'Net channel' error if invalid.""", on_entry={'a': 'channel character'})


d.subroutine(0xB49D, 'lookup_chan_by_char', title='Look up channel by character code', description="""Converts the character to a table index via
attr_to_chan_index, checks the station/network
match via match_station_net, and returns the
channel flags in A.""", on_entry={'a': 'channel character'}, on_exit={'a': 'channel flags'})


d.subroutine(0xB4DC, 'store_result_check_dir', title='Store channel attribute and check not directory', description="""Writes the current channel attribute to the receive
buffer, then tests the directory flag (bit 1). Raises
'Is a dir.' error if the attribute refers to a
directory rather than a file.""")


d.subroutine(0xB4E3, 'check_not_dir', title='Validate channel is not a directory', description="""Calls check_chan_char to validate the channel, then
tests the directory flag (bit 1). Raises 'Is a dir.'
error if the channel refers to a directory.""")


d.subroutine(0xB4FA, 'alloc_fcb_slot', title='Allocate a free file control block slot', description="""Scans FCB slots &20-&2F for an empty entry.
Returns Z=0 with X=slot index on success, or
Z=1 with A=0 if all slots are occupied.""", on_exit={'x': 'slot index (if Z=0)', 'z': '0=success, 1=no free slot'})


d.subroutine(0xB52E, 'alloc_fcb_or_error', title='Allocate FCB slot or raise error', description="""Calls alloc_fcb_slot and raises 'No more FCBs'
if no free slot is available. Preserves the
caller's argument on the stack.""")


d.subroutine(0xB54A, 'close_all_net_chans', title='Close all network channels for current station', description="""Scans FCB slots &0F down to 0, closing those
matching the current station. C=0 closes all
matching entries; C=1 closes with write-flush.""", on_entry={'c': '0=close all, 1=close with write-flush'})


d.subroutine(0xB551, 'scan_fcb_flags', title='Scan FCB slot flags from &10 downward', description="""Iterates through FCB slots starting at &10,
checking each slot's flags byte. Returns when
all slots have been processed.""")


d.subroutine(0xB57A, 'match_station_net', title='Check FCB slot matches current station/network', description="""Compares the station and network numbers in the
FCB at slot X against the current values using
EOR. Returns Z=1 if both match, Z=0 if either
differs.""", on_entry={'x': 'FCB slot index'}, on_exit={'z': '1=match, 0=no match'})


d.subroutine(0xB589, 'find_open_fcb', title='Find next open FCB slot for current connection', description="""Scans from the current index, wrapping around at
the end. On the first pass finds active entries
matching the station; on the second pass finds
empty slots for new allocations.""")


d.subroutine(0xB5CC, 'init_wipe_counters', title='Initialise byte counters for wipe/transfer', description="""Clears the pass counter, byte counter, offset
counter, and transfer flag. Stores &FF sentinels
in l10cd/l10ce. Returns with X/Y pointing at
workspace offset &10CA.""", on_exit={'x': '&CA (workspace offset low)', 'y': '&10 (workspace page)'})


d.subroutine(0xB5EF, 'start_wipe_pass', title='Start wipe pass for current FCB', description="""Verifies the workspace checksum, saves the station
context (pushing station low/high), initialises
transfer counters via init_wipe_counters, and sends
the initial request via send_and_receive. Clears the
active and offset flags on completion.""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xB660, 'save_fcb_context', title='Save FCB context and process pending slots', description="""Copies 13 bytes from the TX buffer (&0F00) and
fs_load_addr workspace to temporary storage at
&10D9. If Y=0, skips to the restore loop. Otherwise
scans for pending FCB slots (bits 7+6 set), flushes
each via start_wipe_pass, allocates new slots via
find_open_fcb, and sends directory requests. Falls
through to restore_catalog_entry.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xB729, 'restore_catalog_entry', title='Restore saved catalog entry to TX buffer', description="""Copies 13 bytes from the context buffer at &10D9
back to the TX buffer at &0F00. Falls through to
find_matching_fcb.""")


d.subroutine(0xB738, 'find_matching_fcb', title='Find FCB slot matching channel attribute', description="""Scans FCB slots 0-&0F for an active entry whose
attribute reference matches l10c9. Converts the
attribute to a channel index, then verifies the
station and network numbers. On the first scan
past slot &0F, saves context via save_fcb_context
and restarts. Returns Z=0 if the FCB has saved
offset data (bit 5 set).""", on_exit={'x': 'matching FCB index', 'z': '0=has offset data, 1=no offset'})


d.subroutine(0xB791, 'inc_fcb_byte_count', title='Increment 3-byte FCB transfer count', description="""Increments l1000+X (low), cascading overflow to
l1010+X (mid) and l1020+X (high).""", on_entry={'x': 'FCB slot index'})


d.subroutine(0xB79F, 'process_all_fcbs', title='Process all active FCB slots', description="""Saves fs_options, fs_block_offset, and X/Y on the
stack, then scans FCB slots &0F down to 0. Calls
start_wipe_pass for each active entry matching the
filter attribute in Y (0=match all). Restores all
saved context on completion. Also contains the
OSBGET/OSBPUT inline logic for reading and writing
bytes through file channels.""", on_entry={'y': 'filter attribute (0=process all)'})


d.subroutine(0xB920, 'send_wipe_request', title='Send wipe/close request packet', description="""Sets up the TX control block with function code
&90, the reply port from Y, and the data byte from
A. Sends via send_disconnect_reply, then checks the
error code — raises the server error if non-zero.""", on_entry={'a': 'data byte to send', 'y': 'reply port'})


d.subroutine(0xB979, 'send_and_receive', title='Set up FS options and transfer workspace', description="""Calls set_options_ptr to configure the FS options
pointer, then jumps to setup_transfer_workspace to
initialise the transfer and send the request.""", on_entry={'a': 'transfer mode', 'x': 'workspace offset low', 'y': 'workspace page'})


d.subroutine(0xB9EA, 'abort_if_escape', title='Test escape flag and abort if pressed', description="""Checks the escape flag byte; returns immediately
if bit 7 is clear. If escape has been pressed,
falls through to the escape abort handler which
acknowledges the escape via OSBYTE &7E.""")


d.subroutine(0xBACE, 'print_dump_header', title='Print hex dump column header line', description="""Outputs the starting address followed by 16 hex
column numbers (00-0F), each separated by a space.
Provides the column alignment header for *Dump
output.""")


d.subroutine(0xBB0C, 'close_ws_file', title='Close file handle stored in workspace', description="""Loads the file handle from ws_page and closes it
via OSFIND with A=0.""")


d.subroutine(0xBB13, 'open_file_for_read', title='Open file for reading via OSFIND', description="""Computes the filename address from the command text
pointer plus the Y offset, calls OSFIND with A=&40
(open for input). Stores the handle in ws_page.
Raises 'Not found' if the returned handle is zero.""")


d.subroutine(0xBB55, 'parse_dump_range', title='Parse hex address for dump range', description="""Reads up to 4 hex digits from the command line
into a 4-byte accumulator, stopping at CR or
space. Each digit shifts the accumulator left
by 4 bits before ORing in the new nybble.""")


d.subroutine(0xBBBE, 'init_dump_buffer', title='Initialise dump buffer and parse address range', description="""Parses the start and end addresses from the command
line via parse_dump_range. If no end address is given,
defaults to the file extent. Validates both addresses
against the file size, raising 'Outside file' if either
exceeds the extent.""")


d.subroutine(0xBC84, 'advance_x_by_8', title='Advance X by 8 via nested JSR chain', description="""Calls advance_x_by_4 (which itself JSRs inx4 then
falls through to inx4), then falls through to inx4
for a total of 4+4=8 INX operations.""")


d.subroutine(0xBC87, 'advance_x_by_4', title='Advance X by 4 via JSR and fall-through', description="""JSRs to inx4 for 4 INX operations, then falls
through to inx4 for another 4 — but when called
directly (not from advance_x_by_8), the caller
returns after the first inx4, yielding X+4.""")


d.subroutine(0xBC8A, 'inx4', title='Increment X four times', description="""Four consecutive INX instructions. Used as a
building block by advance_x_by_4 and
advance_x_by_8 via JSR/fall-through chaining.""")
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
d.comment(0x048C, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x048E, 'Y=&FF for OSBYTE', align=Align.INLINE)
d.comment(0x0490, 'OSBYTE &FD: what type of reset was this?', align=Align.INLINE)
d.comment(0x0496, 'Soft break (X=0): re-init Tube and restart', align=Align.INLINE)
d.comment(0x0498, 'Claim address &FF (startup = highest prio)', align=Align.INLINE)
d.comment(0x049A, 'Request address claim from Tube system', align=Align.INLINE)
d.comment(0x049D, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x049F, 'Init reloc pointers from ROM header', align=Align.INLINE)
d.comment(0x04A2, 'R4 cmd 7: SENDW to send ROM to parasite', align=Align.INLINE)
d.comment(0x04A4, 'Set up Tube for SENDW transfer', align=Align.INLINE)
d.comment(0x04A7, 'Y=0: start at beginning of page', align=Align.INLINE)
d.comment(0x04A9, 'Store to zero page pointer low byte', align=Align.INLINE)
d.comment(0x04AB, 'Send 256-byte page via R3, byte at a time', align=Align.INLINE)
d.comment(0x04AD, 'Write byte to Tube R3 data register', align=Align.INLINE)
d.comment(0x04B0, 'Timing delay: Tube data register needs NOPs', align=Align.INLINE)
d.comment(0x04B1, 'NOP delay (2)', align=Align.INLINE)
d.comment(0x04B2, 'NOP delay (3)', align=Align.INLINE)
d.comment(0x04B3, 'Next byte in page', align=Align.INLINE)
d.comment(0x04B4, 'Loop for all 256 bytes', align=Align.INLINE)
d.comment(0x04B6, 'Increment 24-bit destination addr', align=Align.INLINE)
d.comment(0x04B8, 'No carry: skip higher bytes', align=Align.INLINE)
d.comment(0x04BA, 'Carry into second byte', align=Align.INLINE)
d.comment(0x04BC, 'No carry: skip third byte', align=Align.INLINE)
d.comment(0x04BE, 'Carry into third byte', align=Align.INLINE)
d.comment(0x04C0, 'Increment page counter', align=Align.INLINE)
d.comment(0x04C2, 'Bit 6 set = all pages transferred', align=Align.INLINE)
d.comment(0x04C4, 'More pages: loop back to SENDW', align=Align.INLINE)
d.comment(0x04C6, 'Re-init reloc pointers for final claim', align=Align.INLINE)
d.comment(0x04C9, 'A=4: transfer type for final address claim', align=Align.INLINE)
d.comment(0x04CB, 'Y=0: transfer address low byte', align=Align.INLINE)
d.comment(0x04CD, 'X=&53: transfer address high byte (&0053)', align=Align.INLINE)
d.comment(0x04CF, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x04D2, 'Init: start sending from &8000', align=Align.INLINE)
d.comment(0x04D4, 'Store &80 as source page high byte', align=Align.INLINE)
d.comment(0x04D6, 'Store &80 as page counter initial value', align=Align.INLINE)
d.comment(0x04D8, 'A=&20: bit 5 mask for ROM type check', align=Align.INLINE)
d.comment(0x04DA, 'ROM type bit 5: reloc address in header?', align=Align.INLINE)
d.comment(0x04DD, 'Y = 0 or &20 (reloc flag)', align=Align.INLINE)
d.comment(0x04DE, 'Store as transfer address selector', align=Align.INLINE)
d.comment(0x04E0, 'No reloc addr: use defaults', align=Align.INLINE)
d.comment(0x04E2, 'Skip past copyright string to find reloc addr', align=Align.INLINE)
d.comment(0x04E5, 'Skip past null-terminated copyright string', align=Align.INLINE)
d.comment(0x04E6, 'Load next byte from ROM header', align=Align.INLINE)
d.comment(0x04E9, 'Loop until null terminator found', align=Align.INLINE)
d.comment(0x04EB, 'Read 4-byte reloc address from ROM header', align=Align.INLINE)
d.comment(0x04EE, 'Store reloc addr byte 1 as transfer addr', align=Align.INLINE)
d.comment(0x04F0, 'Load reloc addr byte 2', align=Align.INLINE)
d.comment(0x04F3, 'Store as source page start', align=Align.INLINE)
d.comment(0x04F5, 'Load reloc addr byte 3', align=Align.INLINE)
d.comment(0x04F8, 'Load reloc addr byte 4 (highest)', align=Align.INLINE)
d.comment(0x04FB, 'Store high byte of end address', align=Align.INLINE)
d.comment(0x04FD, 'Store byte 3 of end address', align=Align.INLINE)
d.comment(0x04FF, 'Return with pointers initialised', align=Align.INLINE)
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
d.comment(0x8014, 'Null terminator before copyright', align=Align.INLINE)
d.comment(0x8023, 'A=4: SR bit mask for IFR test', align=Align.INLINE)
d.comment(0x8025, 'Test IFR bit 2: SR complete', align=Align.INLINE)
d.comment(0x8028, 'SR set: shift register complete', align=Align.INLINE)
d.comment(0x802A, 'A=5: not our interrupt, pass on', align=Align.INLINE)
d.comment(0x802C, 'Return service code 5 to MOS', align=Align.INLINE)
d.comment(0x802D, 'Save X on stack', align=Align.INLINE)
d.comment(0x802E, 'Push saved X', align=Align.INLINE)
d.comment(0x802F, 'Save Y on stack', align=Align.INLINE)
d.comment(0x8030, 'Push saved Y', align=Align.INLINE)
d.comment(0x8031, 'Read ACR for shift register restore', align=Align.INLINE)
d.comment(0x8034, 'Clear SR mode bits (2-4)', align=Align.INLINE)
d.comment(0x8036, 'Restore saved SR mode from ws_0d64', align=Align.INLINE)
d.comment(0x8039, 'Write restored ACR to system VIA', align=Align.INLINE)
d.comment(0x803C, 'Read SR to clear shift register IRQ', align=Align.INLINE)
d.comment(0x803F, 'A=4: SR bit mask', align=Align.INLINE)
d.comment(0x8041, 'Clear SR interrupt flag in IFR', align=Align.INLINE)
d.comment(0x8044, 'Disable SR interrupt in IER', align=Align.INLINE)
d.comment(0x8047, 'Load TX operation type for dispatch', align=Align.INLINE)
d.comment(0x804A, 'Copy to A for sign test', align=Align.INLINE)
d.comment(0x804B, 'Bit 7 set: dispatch via table', align=Align.INLINE)
d.comment(0x804D, 'Y=&FE: Econet receive event', align=Align.INLINE)
d.comment(0x804F, 'Fire event (enable: *FX52,150)', align=Align.INLINE)
d.comment(0x8052, 'Y >= &86: above dispatch range', align=Align.INLINE)
d.comment(0x8054, 'Out of range: skip protection', align=Align.INLINE)
d.comment(0x8056, 'Save current JSR protection mask', align=Align.INLINE)
d.comment(0x8059, 'Backup to saved_jsr_mask', align=Align.INLINE)
d.comment(0x805C, 'Set protection bits 2-4', align=Align.INLINE)
d.comment(0x805E, 'Apply protection during dispatch', align=Align.INLINE)
d.comment(0x8061, 'Push return addr high (&85)', align=Align.INLINE)
d.comment(0x8063, 'High byte on stack for RTS', align=Align.INLINE)
d.comment(0x8064, 'Load dispatch target low byte', align=Align.INLINE)
d.comment(0x8067, 'Low byte on stack for RTS', align=Align.INLINE)
d.comment(0x8068, "RTS = dispatch to PHA'd address", align=Align.INLINE)
d.comment(0x8069, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x806C, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x806F, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x8071, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x8073, 'Clear Econet init flag before setup', align=Align.INLINE)
d.comment(0x807C, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x807E, 'X=&0C: NMI claim service', align=Align.INLINE)
d.comment(0x8076, 'Check Tube presence via OSBYTE &EA', align=Align.INLINE)
d.comment(0x8079, 'Store Tube presence flag from OSBYTE &EA', align=Align.INLINE)
d.comment(0x8080, 'Issue NMI claim service request', align=Align.INLINE)
d.comment(0x8083, 'Y=5: NMI claim service number', align=Align.INLINE)
d.comment(0x8085, 'Check if NMI service was claimed (Y changed)', align=Align.INLINE)
d.comment(0x8087, 'Service claimed by other ROM: skip init', align=Align.INLINE)
d.comment(0x8089, 'Copy 32 bytes of NMI shim from ROM to &0D00', align=Align.INLINE)
d.comment(0x808B, 'Read byte from NMI shim ROM source', align=Align.INLINE)
d.comment(0x808E, 'Write to NMI shim RAM at &0D00', align=Align.INLINE)
d.comment(0x8091, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8092, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x8094, 'Patch current ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x8096, 'Self-modifying code: ROM bank at &0D07', align=Align.INLINE)
d.comment(0x8099, 'Clear source network (Y=0 from copy loop)', align=Align.INLINE)
d.comment(0x809C, 'Clear Tube release flag', align=Align.INLINE)
d.comment(0x809E, 'Clear TX operation type', align=Align.INLINE)
d.comment(0x80A1, 'Read station ID (and disable NMIs)', align=Align.INLINE)
d.comment(0x80A4, 'Set own station as TX source', align=Align.INLINE)
d.comment(0x80A7, '&80 = Econet initialised', align=Align.INLINE)
d.comment(0x80A9, 'Mark TX as complete (ready)', align=Align.INLINE)
d.comment(0x80AC, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x80AF, 'INTON: re-enable NMIs (&FE20 read side effect)', align=Align.INLINE)
d.comment(0x80B2, 'Return', align=Align.INLINE)
d.comment(0x80B3, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x80B5, 'BIT SR2: Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x80B8, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x80BA, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x80BD, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x80C0, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x80C2, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x80C4, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x80C6, 'Flag &40 = broadcast frame', align=Align.INLINE)
d.comment(0x80C8, 'Store broadcast flag in rx_src_net', align=Align.INLINE)
d.comment(0x80CB, 'Install nmi_rx_scout_net NMI handler', align=Align.INLINE)
d.comment(0x80CD, 'Install next handler and RTI', align=Align.INLINE)
d.comment(0x80D0, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x80D3, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x80D5, 'Read destination network byte', align=Align.INLINE)
d.comment(0x80D8, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x80DA, 'EOR &FF: test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x80DC, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x80DE, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x80E0, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x80E3, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x80E6, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x80E9, 'Store Y offset for scout data buffer', align=Align.INLINE)
d.comment(0x80EB, 'Install scout data handler (&8102)', align=Align.INLINE)
d.comment(0x80ED, 'High byte of scout data handler', align=Align.INLINE)
d.comment(0x80EF, 'Install scout data loop and RTI', align=Align.INLINE)
d.comment(0x80F2, 'Read SR2', align=Align.INLINE)
d.comment(0x80F5, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x80F7, 'Neither set -- clean end, discard frame', align=Align.INLINE)
d.comment(0x80F9, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x80FC, 'Discard and return to idle', align=Align.INLINE)
d.comment(0x80FF, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x8102, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x8104, 'Read SR2', align=Align.INLINE)
d.comment(0x8107, 'No RDA -- error handler', align=Align.INLINE)
d.comment(0x8109, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x810C, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x810F, 'Advance buffer index', align=Align.INLINE)
d.comment(0x8110, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x8113, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x8115, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x8117, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x811A, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x811D, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x811E, 'Copied all 12 scout bytes?', align=Align.INLINE)
d.comment(0x8120, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x8122, 'Save final buffer offset', align=Align.INLINE)
d.comment(0x8124, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x8127, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x8129, 'SR2 = 0 -- RTI, wait for next NMI', align=Align.INLINE)
d.comment(0x812C, 'Save Y for next iteration', align=Align.INLINE)
d.comment(0x812E, 'Write CR1', align=Align.INLINE)
d.comment(0x8131, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x8133, 'Write CR2', align=Align.INLINE)
d.comment(0x8136, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x8138, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x813B, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x813D, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x813F, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x8142, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x8145, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x8147, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x814A, 'Set bit7 of need_release_tube flag', align=Align.INLINE)
d.comment(0x814B, 'Rotate C=1 into bit7: mark Tube release needed', align=Align.INLINE)
d.comment(0x814D, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x8150, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x8152, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x8155, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x8158, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x815A, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x815C, 'Write CR2: broadcast frame prep', align=Align.INLINE)
d.comment(0x815F, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x8162, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x8164, 'Start scanning port list at page &C0', align=Align.INLINE)
d.comment(0x8166, 'Y=0: start offset within each port slot', align=Align.INLINE)
d.comment(0x8168, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x816A, 'Store page high byte for slot scanning', align=Align.INLINE)
d.comment(0x816C, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x816E, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x8170, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x8172, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x8174, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x8176, 'Y=1: advance to port byte in slot', align=Align.INLINE)
d.comment(0x8177, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x8179, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x817B, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x817E, 'Port mismatch -- try next slot', align=Align.INLINE)
d.comment(0x8180, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x8181, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x8183, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x8185, 'Check if source station matches', align=Align.INLINE)
d.comment(0x8188, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x818A, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x818B, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x818D, 'Zero = accept any network', align=Align.INLINE)
d.comment(0x818F, 'Check if source network matches', align=Align.INLINE)
d.comment(0x8192, 'Network matches or zero = accept', align=Align.INLINE)
d.comment(0x8194, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x8196, 'No NFS workspace -- try fallback path', align=Align.INLINE)
d.comment(0x8198, 'Load current slot base address', align=Align.INLINE)
d.comment(0x819A, 'CLC for 12-byte slot advance', align=Align.INLINE)
d.comment(0x819B, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x819D, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x819F, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.comment(0x81A1, 'No match found -- discard frame', align=Align.INLINE)
d.comment(0x81A4, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x81A7, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x81A9, 'NFS workspace starts at offset 0 in page', align=Align.INLINE)
d.comment(0x81AB, 'NFS workspace high byte for port list', align=Align.INLINE)
d.comment(0x81AD, 'Scan NFS workspace port list', align=Align.INLINE)
d.comment(0x81AF, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x81B1, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x81B4, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x81B7, 'C=0: no Tube claimed -- discard', align=Align.INLINE)
d.comment(0x81B9, 'Check broadcast flag for ACK path', align=Align.INLINE)
d.comment(0x81BC, 'Not broadcast -- normal ACK path', align=Align.INLINE)
d.comment(0x81BE, 'Broadcast: different completion path', align=Align.INLINE)
d.comment(0x81C1, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x81C3, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x81C6, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x81C8, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x81CB, 'Install data_rx_setup at &81D2', align=Align.INLINE)
d.comment(0x81CD, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x81CF, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x81D2, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x81D4, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x81D7, 'Install nmi_data_rx at &81DC', align=Align.INLINE)
d.comment(0x81D9, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)
d.comment(0x81DC, 'A=1: AP mask for SR2 bit test', align=Align.INLINE)
d.comment(0x81DE, 'BIT SR2: test AP bit', align=Align.INLINE)
d.comment(0x81E1, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x81E3, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x81E6, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x81E9, 'Not for us: error path', align=Align.INLINE)
d.comment(0x81EB, 'Install net check handler at &81F0', align=Align.INLINE)
d.comment(0x81ED, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x81F0, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x81F3, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x81F5, 'Read dest network byte', align=Align.INLINE)
d.comment(0x81F8, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x81FA, 'Install skip handler at &8206', align=Align.INLINE)
d.comment(0x81FC, 'High byte of &8206 handler', align=Align.INLINE)
d.comment(0x81FE, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x8201, 'Data ready: skip directly, no RTI', align=Align.INLINE)
d.comment(0x8203, 'Install handler and return via RTI', align=Align.INLINE)
d.comment(0x8206, 'Skip control and port bytes (already known from scout)', align=Align.INLINE)
d.comment(0x8209, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x820B, 'Discard control byte', align=Align.INLINE)
d.comment(0x820E, 'Discard port byte', align=Align.INLINE)
d.comment(0x8211, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x8213, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x8216, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x8218, 'Install bulk read at &8239', align=Align.INLINE)
d.comment(0x821A, 'High byte of &8239 handler', align=Align.INLINE)
d.comment(0x821C, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x821F, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x8221, 'No: install handler and RTI', align=Align.INLINE)
d.comment(0x8224, 'Tube: install Tube RX at &8296', align=Align.INLINE)
d.comment(0x8226, 'High byte of &8296 handler', align=Align.INLINE)
d.comment(0x8228, 'Install Tube handler and RTI', align=Align.INLINE)
d.comment(0x822B, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x822E, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x8230, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x8233, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x8236, 'Discard and return to idle listen', align=Align.INLINE)
d.comment(0x8239, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x823B, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x823E, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x8240, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x8243, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x8245, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8246, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x8248, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x824A, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x824C, 'No pages left: handle as complete', align=Align.INLINE)
d.comment(0x824E, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x8251, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x8253, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)
d.comment(0x8255, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x8258, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x825A, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x825B, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x825D, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x825F, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x8261, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x8263, 'No pages left: frame complete', align=Align.INLINE)
d.comment(0x8265, 'Read SR2 for next iteration', align=Align.INLINE)
d.comment(0x8268, 'SR2 non-zero: more data, loop back', align=Align.INLINE)
d.comment(0x826A, 'SR2=0: no more data yet, wait for NMI', align=Align.INLINE)
d.comment(0x826D, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x826F, 'Write CR2: disable PSE for bit testing', align=Align.INLINE)
d.comment(0x8272, 'CR2=&84: disable PSE for individual bit testing', align=Align.INLINE)
d.comment(0x8274, 'Write CR1: disable all interrupts', align=Align.INLINE)
d.comment(0x8277, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x8279, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x827B, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x827E, 'No FV -- error', align=Align.INLINE)
d.comment(0x8280, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x8282, 'Check if buffer space remains', align=Align.INLINE)
d.comment(0x8284, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x8286, 'FV+RDA: read and store last data byte', align=Align.INLINE)
d.comment(0x8289, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x828B, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x828D, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x828F, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x8291, 'Page boundary: advance buffer page', align=Align.INLINE)
d.comment(0x8293, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x8296, 'Read SR2 for Tube data receive path', align=Align.INLINE)
d.comment(0x8299, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x829B, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x829E, 'Check buffer limits and transfer size', align=Align.INLINE)
d.comment(0x82A1, 'Zero: buffer full, handle as error', align=Align.INLINE)
d.comment(0x82A3, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x82A6, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x82A9, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x82AC, 'Check limits after byte pair', align=Align.INLINE)
d.comment(0x82AF, 'Zero: Tube transfer complete', align=Align.INLINE)
d.comment(0x82B1, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x82B4, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x82B6, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x82B9, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x82BB, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x82BE, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x82C0, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x82C3, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x82C5, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x82C8, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x82CA, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x82CC, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x82CE, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x82D0, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x82D2, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x82D4, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x82D6, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x82D9, 'Save extra byte at &0D5D for later use', align=Align.INLINE)
d.comment(0x82DC, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x82DE, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x82E1, 'Store updated flags', align=Align.INLINE)
d.comment(0x82E4, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x82E7, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x82E9, 'Final ACK: call completion handler', align=Align.INLINE)
d.comment(0x82EC, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x82EF, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x82F1, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x82F4, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x82F6, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x82F9, 'Install saved next handler (&838B for scout ACK)', align=Align.INLINE)
d.comment(0x82FB, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x82FD, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x8300, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x8303, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x8306, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x8309, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x830B, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x830E, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x8311, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x8314, 'Install handler at &831B (write src addr)', align=Align.INLINE)
d.comment(0x8316, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x8318, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)
d.comment(0x831B, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x831E, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x8321, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x8323, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x8326, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x8328, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x832B, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x832E, 'bit7 set: start data TX phase', align=Align.INLINE)
d.comment(0x8330, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x8332, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x8335, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x8338, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x833B, 'Install next NMI handler', align=Align.INLINE)
d.comment(0x833E, 'Jump to start data TX phase', align=Align.INLINE)
d.comment(0x8341, 'Jump to error handler', align=Align.INLINE)
d.comment(0x8344, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x8346, 'BIT tx_flags: check data transfer bit', align=Align.INLINE)
d.comment(0x8349, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x834B, 'CLC: init carry for 4-byte add', align=Align.INLINE)
d.comment(0x834C, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x834D, 'Y=8: RXCB high pointer offset', align=Align.INLINE)
d.comment(0x834F, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x8351, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x8352, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x8355, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x8357, 'Next byte', align=Align.INLINE)
d.comment(0x8358, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x8359, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x835B, 'No: continue adding', align=Align.INLINE)
d.comment(0x835D, 'Discard final carry', align=Align.INLINE)
d.comment(0x835E, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x8360, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x8363, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x8365, 'Save X on stack', align=Align.INLINE)
d.comment(0x8366, 'Push X', align=Align.INLINE)
d.comment(0x8367, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x8369, 'CLC for address calculation', align=Align.INLINE)
d.comment(0x836A, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x836C, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x836D, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x836F, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x8371, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x8374, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x8377, 'Send to Tube via R3', align=Align.INLINE)
d.comment(0x837A, 'SEC: init carry for increment', align=Align.INLINE)
d.comment(0x837B, 'Y=8: start at high pointer', align=Align.INLINE)
d.comment(0x837D, 'A=0: add carry only (increment)', align=Align.INLINE)
d.comment(0x837F, 'Add carry to pointer byte', align=Align.INLINE)
d.comment(0x8381, 'Store back to RXCB', align=Align.INLINE)
d.comment(0x8383, 'Next byte', align=Align.INLINE)
d.comment(0x8384, 'Keep going while carry propagates', align=Align.INLINE)
d.comment(0x8386, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8387, 'Transfer to X register', align=Align.INLINE)
d.comment(0x8388, 'A=&FF: return value (transfer done)', align=Align.INLINE)
d.comment(0x838A, 'Return', align=Align.INLINE)
d.comment(0x838B, 'Load received port byte', align=Align.INLINE)
d.comment(0x838E, 'Port != 0: data transfer frame', align=Align.INLINE)
d.comment(0x8390, 'Port=0: load control byte', align=Align.INLINE)
d.comment(0x8393, 'Ctrl = &82 (POKE)?', align=Align.INLINE)
d.comment(0x8395, 'Yes: POKE also needs data transfer', align=Align.INLINE)
d.comment(0x8397, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)
d.comment(0x839A, 'Update buffer pointer and check for Tube', align=Align.INLINE)
d.comment(0x839D, 'Transfer not done: skip buffer update', align=Align.INLINE)
d.comment(0x839F, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x83A1, 'CLC for address add', align=Align.INLINE)
d.comment(0x83A2, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x83A4, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x83A6, 'Carry: increment buffer high byte', align=Align.INLINE)
d.comment(0x83A8, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x83AA, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x83AC, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x83AD, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x83AF, 'Store high byte to RXCB', align=Align.INLINE)
d.comment(0x83B1, 'Check port byte again', align=Align.INLINE)
d.comment(0x83B4, 'Port=0: immediate op, discard+listen', align=Align.INLINE)
d.comment(0x83B6, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x83B9, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x83BB, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x83BD, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x83BE, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x83C1, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x83C3, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x83C4, 'Load port byte', align=Align.INLINE)
d.comment(0x83C7, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x83C9, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x83CA, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x83CD, 'Set bit7: signals wait_net_tx_ack that reply arrived', align=Align.INLINE)
d.comment(0x83CF, 'Store to RXCB byte 0 (bit 7 set = complete)', align=Align.INLINE)
d.comment(0x83D1, 'Load callback event flags', align=Align.INLINE)
d.comment(0x83D4, 'Shift bit 0 into carry', align=Align.INLINE)
d.comment(0x83D5, 'Bit 0 clear: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83D7, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x83D8, 'Load RXCB workspace pointer low byte', align=Align.INLINE)
d.comment(0x83DA, 'Count slots', align=Align.INLINE)
d.comment(0x83DB, 'Subtract 12 bytes per RXCB slot', align=Align.INLINE)
d.comment(0x83DD, 'Loop until pointer exhausted', align=Align.INLINE)
d.comment(0x83DF, 'Adjust for off-by-one', align=Align.INLINE)
d.comment(0x83E0, 'Check slot index >= 3', align=Align.INLINE)
d.comment(0x83E2, 'Slot < 3: no callback, skip to reset', align=Align.INLINE)
d.comment(0x83E4, 'Discard scout and reset listen state', align=Align.INLINE)
d.comment(0x83E7, 'Pass slot index as callback parameter', align=Align.INLINE)
d.comment(0x83E8, 'Jump to TX completion with slot index', align=Align.INLINE)
d.comment(0x83EB, 'Discard scout and reset RX listen', align=Align.INLINE)
d.comment(0x83EE, 'Reset ADLC and return to RX listen', align=Align.INLINE)
d.comment(0x83F1, 'A=&B3: low byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83F3, 'Y=&80: high byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x83F5, 'Install nmi_rx_scout as NMI handler', align=Align.INLINE)
d.comment(0x83F8, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x83FA, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x83FD, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x8400, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x8402, 'Release Tube claim before discarding', align=Align.INLINE)
d.comment(0x8405, 'Return', align=Align.INLINE)
d.comment(0x8406, 'Save X on stack', align=Align.INLINE)
d.comment(0x8407, 'Push X', align=Align.INLINE)
d.comment(0x8408, 'X=4: start at scout byte offset 4', align=Align.INLINE)
d.comment(0x840A, 'A=2: Tube transfer check mask', align=Align.INLINE)
d.comment(0x840C, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x840F, 'Tube active: use R3 write path', align=Align.INLINE)
d.comment(0x8411, 'Y = current buffer position', align=Align.INLINE)
d.comment(0x8413, 'Load scout data byte', align=Align.INLINE)
d.comment(0x8416, 'Store to port buffer', align=Align.INLINE)
d.comment(0x8418, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x8419, 'No page crossing', align=Align.INLINE)
d.comment(0x841B, 'Page crossing: inc buffer high byte', align=Align.INLINE)
d.comment(0x841D, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x841F, 'No pages left: overflow', align=Align.INLINE)
d.comment(0x8421, 'Next scout data byte', align=Align.INLINE)
d.comment(0x8422, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8424, 'Done all scout data? (X reaches &0C)', align=Align.INLINE)
d.comment(0x8426, 'No: continue copying', align=Align.INLINE)
d.comment(0x8428, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8429, 'Transfer to X register', align=Align.INLINE)
d.comment(0x842A, 'Jump to completion handler', align=Align.INLINE)
d.comment(0x842D, 'Tube path: load scout data byte', align=Align.INLINE)
d.comment(0x8430, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x8433, 'Increment buffer position counters', align=Align.INLINE)
d.comment(0x8436, 'Counter overflow: handle end of buffer', align=Align.INLINE)
d.comment(0x8438, 'Next scout data byte', align=Align.INLINE)
d.comment(0x8439, 'Done all scout data?', align=Align.INLINE)
d.comment(0x843B, 'No: continue Tube writes', align=Align.INLINE)
d.comment(0x843F, 'Check if Tube needs releasing', align=Align.INLINE)
d.comment(0x8441, 'Bit7 set: already released', align=Align.INLINE)
d.comment(0x8443, 'A=&82: Tube release claim type', align=Align.INLINE)
d.comment(0x8445, 'Release Tube address claim', align=Align.INLINE)
d.comment(0x8448, 'Clear release flag (LSR clears bit7)', align=Align.INLINE)
d.comment(0x844A, 'Return', align=Align.INLINE)
d.comment(0x844B, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x844E, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x8450, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x8452, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x8454, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x8456, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x8458, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x845A, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x845B, 'SEC for subtract', align=Align.INLINE)
d.comment(0x845C, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x845E, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x845F, 'Load protection mask from LSTAT', align=Align.INLINE)
d.comment(0x8462, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x8463, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x8464, 'Loop until bit aligned', align=Align.INLINE)
d.comment(0x8466, 'Bit set = operation disabled, discard', align=Align.INLINE)
d.comment(0x8468, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x846B, 'Hi byte: all handlers are in page &84', align=Align.INLINE)
d.comment(0x846D, 'Push hi byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x846E, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x8471, 'Push handler low byte', align=Align.INLINE)
d.comment(0x8472, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0x8473, 'Increment port buffer length', align=Align.INLINE)
d.comment(0x8475, 'Check if scout data index reached 11', align=Align.INLINE)
d.comment(0x8477, 'Yes: loop back to continue reading', align=Align.INLINE)
d.comment(0x8479, 'Restore A from stack', align=Align.INLINE)
d.comment(0x847A, 'Transfer to X', align=Align.INLINE)
d.comment(0x847B, 'Jump to discard handler', align=Align.INLINE)
d.comment(0x8486, 'A=0: port buffer lo at page boundary', align=Align.INLINE)
d.comment(0x8488, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x848A, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x848C, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x848E, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x8490, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x8492, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x8494, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x8496, 'Y=1: copy 2 bytes (1 down to 0)', align=Align.INLINE)
d.comment(0x8498, 'Load remote address byte', align=Align.INLINE)
d.comment(0x849B, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x849E, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x849F, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x84A1, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x84A2, 'Svc 5 dispatch table low bytes', align=Align.INLINE)
d.comment(0x84A4, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x84A6, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x84A8, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84AA, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x84AC, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x84AF, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x84B1, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x84B3, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x84B5, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x84B7, 'Buffer start lo = &25', align=Align.INLINE)
d.comment(0x84B9, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x84BB, 'Buffer hi = &7F (below screen)', align=Align.INLINE)
d.comment(0x84BD, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x84C1, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x84C3, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x84C5, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x84C7, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x84C9, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x84CB, 'Store scout status', align=Align.INLINE)
d.comment(0x84CE, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x84D1, 'C=0: transfer not set up, discard', align=Align.INLINE)
d.comment(0x84D3, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x84D6, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x84D8, 'Store updated TX flags', align=Align.INLINE)
d.comment(0x84DB, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x84DD, 'Write CR1: enable TX interrupts', align=Align.INLINE)
d.comment(0x84E0, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x84E2, 'Write CR2 for TX setup', align=Align.INLINE)
d.comment(0x84E5, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x84E7, 'Y=&85: NMI handler high byte', align=Align.INLINE)
d.comment(0x84E9, 'Acknowledge and write TX dest', align=Align.INLINE)
d.comment(0x84EC, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x84EE, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x84EF, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x84F1, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x84F3, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x84F5, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x84F7, 'Load requesting station number', align=Align.INLINE)
d.comment(0x84FA, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x84FD, 'Load requesting network number', align=Align.INLINE)
d.comment(0x8500, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x8502, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x8505, 'Save TX operation type for SR dispatch', align=Align.INLINE)
d.comment(0x8508, 'IER bit 2: disable SR interrupt', align=Align.INLINE)
d.comment(0x850A, 'Write IER to disable SR', align=Align.INLINE)
d.comment(0x850D, 'Read ACR for shift register config', align=Align.INLINE)
d.comment(0x8510, 'Isolate shift register mode bits (2-4)', align=Align.INLINE)
d.comment(0x8512, 'Save original SR mode for later restore', align=Align.INLINE)
d.comment(0x8515, 'Reload ACR for modification', align=Align.INLINE)
d.comment(0x8518, 'Clear SR mode bits (keep other bits)', align=Align.INLINE)
d.comment(0x851A, 'SR mode 2: shift in under φ2', align=Align.INLINE)
d.comment(0x851C, 'Apply new shift register mode', align=Align.INLINE)
d.comment(0x851F, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x8522, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x8525, 'Increment buffer length low byte', align=Align.INLINE)
d.comment(0x8527, 'No overflow: done', align=Align.INLINE)
d.comment(0x8529, 'Increment buffer length high byte', align=Align.INLINE)
d.comment(0x852B, 'No overflow: done', align=Align.INLINE)
d.comment(0x852D, 'Increment buffer pointer low byte', align=Align.INLINE)
d.comment(0x852F, 'No overflow: done', align=Align.INLINE)
d.comment(0x8531, 'Increment buffer pointer high byte', align=Align.INLINE)
d.comment(0x8533, 'Return', align=Align.INLINE)
d.comment(0x8539, 'Hi byte of tx_done_exit-1', align=Align.INLINE)
d.comment(0x853B, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x853C, 'Push lo of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x853E, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x853F, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)
d.comment(0x8534, """TX done dispatch table (lo bytes)

Low bytes of PHA/PHA/RTS dispatch targets for TX
operation types &83-&87. Read by the dispatch at
&8064 via LDA set_rx_buf_len_hi,Y (base &84B1
+ Y). High byte is always &85, so targets are
&85xx+1. Entries for Y < &83 read from preceding
code bytes and are not valid operation types.""")
d.comment(0x8534, 'Y=&83: lo &38 -> tx_done_jsr (&8539)', align=Align.INLINE)
d.comment(0x8535, 'Y=&84: lo &41 -> tx_done_econet_event', align=Align.INLINE)
d.comment(0x8536, 'Y=&85: lo &4F -> tx_done_os_proc', align=Align.INLINE)
d.comment(0x8537, 'Y=&86: lo &5B -> tx_done_halt', align=Align.INLINE)
d.comment(0x8538, 'Y=&87: lo &72 -> tx_done_continue', align=Align.INLINE)
d.comment(0x8542, 'X = remote address lo from l0d66', align=Align.INLINE)
d.comment(0x8545, 'A = remote address hi from l0d67', align=Align.INLINE)
d.comment(0x8548, 'Y = 8: Econet event number', align=Align.INLINE)
d.comment(0x854D, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x8550, 'X = remote address lo', align=Align.INLINE)
d.comment(0x8553, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x8556, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x8559, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x855C, 'A=&04: bit 2 mask for rx_flags', align=Align.INLINE)
d.comment(0x855E, 'Test if already halted', align=Align.INLINE)
d.comment(0x8561, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x8563, 'Set bit 2 in rx_flags', align=Align.INLINE)
d.comment(0x8566, 'Store halt flag', align=Align.INLINE)
d.comment(0x8569, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x856B, 'Enable interrupts during halt wait', align=Align.INLINE)
d.comment(0x856C, 'Test halt flag', align=Align.INLINE)
d.comment(0x856F, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x8573, 'Load current RX flags', align=Align.INLINE)
d.comment(0x8576, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x8578, 'Store updated flags', align=Align.INLINE)
d.comment(0x857B, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x857C, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x857D, 'Restore X from stack', align=Align.INLINE)
d.comment(0x857E, 'Transfer to X register', align=Align.INLINE)
d.comment(0x857F, 'A=0: success status', align=Align.INLINE)
d.comment(0x8581, 'Return with A=0 (success)', align=Align.INLINE)
d.comment(0x8582, 'Save X on stack', align=Align.INLINE)
d.comment(0x8583, 'Push X', align=Align.INLINE)
d.comment(0x8584, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x8586, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x8588, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x858C, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x858E, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x8591, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x8593, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x8595, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x8597, 'Bit7 clear: normal data transfer', align=Align.INLINE)
d.comment(0x859A, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x859D, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x859E, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x859F, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x85A1, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x85A4, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x85A6, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x85A8, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x85AA, 'SEC: init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x85AB, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x85AC, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)
d.comment(0x85AE, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x85B0, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x85B1, '(continued)', align=Align.INLINE)
d.comment(0x85B2, '(continued)', align=Align.INLINE)
d.comment(0x85B3, '(continued)', align=Align.INLINE)
d.comment(0x85B4, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x85B5, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x85B7, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x85BA, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x85BB, '(continued)', align=Align.INLINE)
d.comment(0x85BC, '(continued)', align=Align.INLINE)
d.comment(0x85BD, '(continued)', align=Align.INLINE)
d.comment(0x85BE, '(continued)', align=Align.INLINE)
d.comment(0x85BF, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x85C0, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x85C2, 'No: next byte pair', align=Align.INLINE)
d.comment(0x85C4, 'Discard final borrow', align=Align.INLINE)
d.comment(0x85C5, 'Ctrl < &81: not an immediate op', align=Align.INLINE)
d.comment(0x85C7, 'Below range: normal data transfer', align=Align.INLINE)
d.comment(0x85C9, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x85CB, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x85CD, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)
d.comment(0x85CF, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x85D1, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x85D4, 'Next byte', align=Align.INLINE)
d.comment(0x85D5, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x85D7, 'No: continue copying', align=Align.INLINE)
d.comment(0x85D9, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x85DB, 'BIT SR2: test if line is idle', align=Align.INLINE)
d.comment(0x85DE, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x85E0, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x85E2, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x85E3, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x85E5, 'Store scout frame length', align=Align.INLINE)
d.comment(0x85E8, 'A=0: init low byte of timeout counter', align=Align.INLINE)
d.comment(0x85EA, 'Save TX index', align=Align.INLINE)
d.comment(0x85ED, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x85EE, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x85EF, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x85F1, 'A=&04: INACTIVE bit mask for SR2 test', align=Align.INLINE)
d.comment(0x85F3, 'Save interrupt state', align=Align.INLINE)
d.comment(0x85F4, 'Disable interrupts for ADLC access', align=Align.INLINE)
d.comment(0x85F5, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x85F8, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x85FB, 'BIT SR2: Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x85FE, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x8600, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x8603, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x8605, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x8608, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x860A, 'BIT SR1: tests CTS present', align=Align.INLINE)
d.comment(0x860D, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x860F, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x8612, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x8613, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x8614, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x8617, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8619, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x861C, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x861E, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x8621, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x8625, 'Error &44: control byte out of valid range', align=Align.INLINE)
d.comment(0x8629, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x862B, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x862E, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x862F, 'Pop saved register', align=Align.INLINE)
d.comment(0x8630, 'Pop saved register', align=Align.INLINE)
d.comment(0x8631, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x8633, 'ALWAYS branch to shared error handler', align=Align.INLINE)
d.comment(0x8635, "Error &43 = 'No Clock'", align=Align.INLINE)
d.comment(0x8637, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x8639, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x863B, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x863D, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x8640, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x8641, 'Move to X register', align=Align.INLINE)
d.comment(0x8642, 'Return to TX caller', align=Align.INLINE)
d.comment(0x8643, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x8646, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x8648, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x864B, 'Install NMI handler at &86E0 (TX data handler)', align=Align.INLINE)
d.comment(0x864D, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x864F, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x8652, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x8655, 'Set need_release_tube flag (SEC/ROR = bit7)', align=Align.INLINE)
d.comment(0x8656, 'Rotate carry into bit 7 of flag', align=Align.INLINE)
d.comment(0x8658, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)
d.comment(0x865B, 'Load destination port number', align=Align.INLINE)
d.comment(0x865E, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x8660, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x8663, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x8666, 'Store operation flags', align=Align.INLINE)
d.comment(0x8669, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x866C, 'Store expected transfer length', align=Align.INLINE)
d.comment(0x866F, 'Push high byte of return address (&9C)', align=Align.INLINE)
d.comment(0x8671, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8672, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x8675, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x8676, 'RTS dispatches to control-byte handler', align=Align.INLINE)
d.comment(0x8677, """TX ctrl dispatch table (lo bytes)

Low bytes of PHA/PHA/RTS dispatch targets for TX
control byte types &81-&88. Read by the dispatch
at &8672 via LDA intoff_disable_nmi_op,Y (base
intoff_test_inactive+1). High byte is always &86,
so targets are &86xx+1. Last entry dispatches to
tx_ctrl_machine_type at &867F, immediately after
the table.""")
d.comment(0x8677, 'Ctrl &81 PEEK: tx_ctrl_peek', align=Align.INLINE)
d.comment(0x8678, 'Ctrl &82 POKE: tx_ctrl_poke', align=Align.INLINE)
d.comment(0x8679, 'Ctrl &83 JSR: proc_op_status2', align=Align.INLINE)
d.comment(0x867A, 'Ctrl &84 UserProc: proc_op_status2', align=Align.INLINE)
d.comment(0x867B, 'Ctrl &85 OSProc: proc_op_status2', align=Align.INLINE)
d.comment(0x867C, 'Ctrl &86 HALT: tx_ctrl_exit', align=Align.INLINE)
d.comment(0x867D, 'Ctrl &87 CONTINUE: tx_ctrl_exit', align=Align.INLINE)
d.comment(0x867E, 'Ctrl &88 MachType: tx_ctrl_machine_type', align=Align.INLINE)
d.comment(0x867F, 'scout_status=3 (machine type query)', align=Align.INLINE)
d.comment(0x8681, 'Skip address addition, store status', align=Align.INLINE)
d.comment(0x8683, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x8687, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)
d.comment(0x8689, 'Store scout status', align=Align.INLINE)
d.comment(0x868C, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x868D, 'Save carry on stack', align=Align.INLINE)
d.comment(0x868E, 'Y=&0C: start at offset 12', align=Align.INLINE)
d.comment(0x8690, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x8693, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x8694, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x8696, 'Store updated address byte', align=Align.INLINE)
d.comment(0x8699, 'Next byte', align=Align.INLINE)
d.comment(0x869A, 'Save carry for next addition', align=Align.INLINE)
d.comment(0x869B, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x869D, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x869F, 'Restore processor flags', align=Align.INLINE)
d.comment(0x86A0, 'Skip buffer setup if transfer size is zero', align=Align.INLINE)
d.comment(0x86A2, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x86A5, 'AND with dest network', align=Align.INLINE)
d.comment(0x86A8, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x86AA, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x86AC, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x86AE, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x86B1, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x86B3, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x86B6, 'Y=4: start of address data in TXCB', align=Align.INLINE)
d.comment(0x86B8, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x86BA, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x86BD, 'Next byte', align=Align.INLINE)
d.comment(0x86BE, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x86C0, 'No: continue copying', align=Align.INLINE)
d.comment(0x86C4, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x86C6, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x86C9, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x86CB, 'Store scout status', align=Align.INLINE)
d.comment(0x86CE, 'Copy TX block pointer to workspace ptr', align=Align.INLINE)
d.comment(0x86D0, 'Store low byte', align=Align.INLINE)
d.comment(0x86D2, 'Copy TX block pointer high byte', align=Align.INLINE)
d.comment(0x86D4, 'Store high byte', align=Align.INLINE)
d.comment(0x86D6, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x86D9, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x86DA, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x86DB, 'Second PLA', align=Align.INLINE)
d.comment(0x86DC, 'Third PLA', align=Align.INLINE)
d.comment(0x86DD, 'Fourth PLA', align=Align.INLINE)
d.comment(0x86DE, 'Restore X from A', align=Align.INLINE)
d.comment(0x86DF, 'Return to caller', align=Align.INLINE)
d.comment(0x86E0, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x86E3, 'BIT SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x86E6, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x86E8, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x86EB, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x86EE, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x86EF, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x86F2, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x86F3, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x86F6, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x86F9, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x86FC, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x86FE, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x8701, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x8703, 'RTI -- wait for next NMI', align=Align.INLINE)
d.comment(0x8706, 'Error &42', align=Align.INLINE)
d.comment(0x870A, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x870C, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x870F, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x8711, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x8714, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)
d.comment(0x8715, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x8716, 'Increment delay counter', align=Align.INLINE)
d.comment(0x8717, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x8719, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x871C, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x871E, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x8721, 'Install NMI handler at &8728 (TX completion)', align=Align.INLINE)
d.comment(0x8723, 'High byte of handler address', align=Align.INLINE)
d.comment(0x8725, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x8728, 'Jump to error handler', align=Align.INLINE)
d.comment(0x872A, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x872D, 'Test workspace flags', align=Align.INLINE)
d.comment(0x8730, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x8732, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x8735, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x8737, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x873A, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x873C, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)
d.comment(0x873F, 'Install RX reply handler at &8744', align=Align.INLINE)
d.comment(0x8741, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x8744, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x8746, 'BIT SR2: test AP (Address Present)', align=Align.INLINE)
d.comment(0x8749, 'No AP -- error', align=Align.INLINE)
d.comment(0x874B, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x874E, 'Compare to our station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x8751, 'Not our station -- error/reject', align=Align.INLINE)
d.comment(0x8753, 'Install next handler at &8758 (reply continuation)', align=Align.INLINE)
d.comment(0x8755, 'Install continuation handler', align=Align.INLINE)
d.comment(0x8758, 'Read RX byte (destination station)', align=Align.INLINE)
d.comment(0x875B, 'No RDA -- error', align=Align.INLINE)
d.comment(0x875D, 'Read destination network byte', align=Align.INLINE)
d.comment(0x8760, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x8762, 'Install next handler at &876F (reply validation)', align=Align.INLINE)
d.comment(0x8764, 'BIT SR1: test IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x8767, 'IRQ set -- fall through to &876F without RTI', align=Align.INLINE)
d.comment(0x8769, 'IRQ not set -- install handler and RTI', align=Align.INLINE)
d.comment(0x876C, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x876F, 'BIT SR2: test RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x8772, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x8774, 'Read source station', align=Align.INLINE)
d.comment(0x8777, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x877A, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x877C, 'Read source network', align=Align.INLINE)
d.comment(0x877F, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x8782, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x8784, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x8786, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x8789, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x878B, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x878D, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x8790, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x8792, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x8795, 'Install next handler at &886E (four-way data phase) into &0D43/&0D44', align=Align.INLINE)
d.comment(0x8797, 'High byte &88 of next handler address', align=Align.INLINE)
d.comment(0x8799, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x879C, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x879F, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x87A2, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87A5, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87A7, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x87AA, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87AD, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x87B0, 'Install handler at &87B7 (write src addr for scout ACK)', align=Align.INLINE)
d.comment(0x87B2, 'High byte &87 of handler address', align=Align.INLINE)
d.comment(0x87B4, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x87B7, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x87BA, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x87BD, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87BF, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x87C2, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x87C4, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x87C7, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x87C9, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x87CC, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x87CE, 'Install nmi_data_tx at &87E4', align=Align.INLINE)
d.comment(0x87D0, 'High byte of handler address', align=Align.INLINE)
d.comment(0x87D2, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87D5, 'Install nmi_imm_data at &882D', align=Align.INLINE)
d.comment(0x87D7, 'High byte of handler address', align=Align.INLINE)
d.comment(0x87D9, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x87DC, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x87DE, 'No pages left: send final partial page', align=Align.INLINE)
d.comment(0x87E0, 'Load remaining byte count', align=Align.INLINE)
d.comment(0x87E2, 'Zero bytes left: skip to TDRA check', align=Align.INLINE)
d.comment(0x87E4, 'Load remaining byte count (alt entry)', align=Align.INLINE)
d.comment(0x87E6, 'Zero: loop back to top of handler', align=Align.INLINE)
d.comment(0x87E8, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x87EB, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x87ED, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x87EF, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x87F2, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x87F3, 'No page crossing', align=Align.INLINE)
d.comment(0x87F5, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x87F7, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x87F9, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x87FB, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x87FD, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x8800, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x8801, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x8803, 'No page crossing', align=Align.INLINE)
d.comment(0x8805, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x8807, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x8809, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x880B, 'BIT SR1: test IRQ (N=bit7) for tight loop', align=Align.INLINE)
d.comment(0x880E, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x8810, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x8813, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)
d.comment(0x8815, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x8818, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x881B, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x881D, 'Install discard_reset_listen at &83EB', align=Align.INLINE)
d.comment(0x881F, 'High byte of &83EB handler', align=Align.INLINE)
d.comment(0x8821, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x8824, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x8827, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x882A, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x882D, 'Tube TX: BIT SR1 test TDRA', align=Align.INLINE)
d.comment(0x8830, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x8832, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x8835, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x8838, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x883A, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x883C, 'Carry into second byte', align=Align.INLINE)
d.comment(0x883E, 'No further carry', align=Align.INLINE)
d.comment(0x8840, 'Carry into third byte', align=Align.INLINE)
d.comment(0x8842, 'No further carry', align=Align.INLINE)
d.comment(0x8844, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x8846, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x8848, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x884B, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x884E, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x8850, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x8852, 'Carry into second byte', align=Align.INLINE)
d.comment(0x8854, 'No further carry', align=Align.INLINE)
d.comment(0x8856, 'Carry into third byte', align=Align.INLINE)
d.comment(0x8858, 'No further carry', align=Align.INLINE)
d.comment(0x885A, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x885C, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x885E, 'BIT SR1: test IRQ for tight loop', align=Align.INLINE)
d.comment(0x8861, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x8863, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x8866, 'TX error: check flags for path', align=Align.INLINE)
d.comment(0x8869, 'Bit7 clear: TX result = not listening', align=Align.INLINE)
d.comment(0x886B, 'Bit7 set: discard and return to listen', align=Align.INLINE)
d.comment(0x886E, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)
d.comment(0x8870, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x8873, 'Install nmi_final_ack handler', align=Align.INLINE)
d.comment(0x8875, 'High byte of handler address', align=Align.INLINE)
d.comment(0x8877, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x887A, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x887C, 'BIT SR2: test AP', align=Align.INLINE)
d.comment(0x887F, 'No AP -- error', align=Align.INLINE)
d.comment(0x8881, 'Read dest station', align=Align.INLINE)
d.comment(0x8884, 'Compare to our station (INTOFF side effect)', align=Align.INLINE)
d.comment(0x8887, 'Not our station -- error', align=Align.INLINE)
d.comment(0x8889, 'Install nmi_final_ack_net handler', align=Align.INLINE)
d.comment(0x888B, 'Install continuation handler', align=Align.INLINE)
d.comment(0x888E, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x8891, 'No RDA -- error', align=Align.INLINE)
d.comment(0x8893, 'Read dest network', align=Align.INLINE)
d.comment(0x8896, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x8898, 'Install nmi_final_ack_validate handler', align=Align.INLINE)
d.comment(0x889A, 'BIT SR1: test IRQ -- more data ready?', align=Align.INLINE)
d.comment(0x889D, 'IRQ set -- fall through to validate', align=Align.INLINE)
d.comment(0x889F, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x88A2, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x88A5, 'No RDA -- error', align=Align.INLINE)
d.comment(0x88A7, 'Read source station', align=Align.INLINE)
d.comment(0x88AA, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x88AD, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88AF, 'Read source network', align=Align.INLINE)
d.comment(0x88B2, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x88B5, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x88B7, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x88BA, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x88BC, 'Install data RX handler', align=Align.INLINE)
d.comment(0x88BF, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x88C1, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x88C4, 'No FV -- error', align=Align.INLINE)
d.comment(0x88C6, 'A=0: success result code', align=Align.INLINE)
d.comment(0x88C8, 'BEQ: always taken (A=0)', align=Align.INLINE)
d.comment(0x88CA, 'A=&41: not listening error code', align=Align.INLINE)
d.comment(0x88CC, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x88CE, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x88D0, '&80: completion flag for &0D3A', align=Align.INLINE)
d.comment(0x88D2, 'Signal TX complete', align=Align.INLINE)
d.comment(0x88D5, 'Full ADLC reset and return to idle listen', align=Align.INLINE)
d.comment(0x88D8, """Unreferenced dead data (16 bytes)

16 bytes between JMP discard_reset_rx (&88D5) and
tx_calc_transfer (&88E8). Unreachable as code (after
an unconditional JMP) and unreferenced as data. No
label, index, or indirect pointer targets any address
in the &88D8-&88E7 range. Likely unused remnant from
development.""")
d.comment(0x88D8, 'Dead data: &0E', align=Align.INLINE)
d.comment(0x88D9, 'Dead data: &0E', align=Align.INLINE)
d.comment(0x88DA, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88DB, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88DC, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88DD, 'Dead data: &06', align=Align.INLINE)
d.comment(0x88DE, 'Dead data: &06', align=Align.INLINE)
d.comment(0x88DF, 'Dead data: &0A', align=Align.INLINE)
d.comment(0x88E0, 'Dead data: &81', align=Align.INLINE)
d.comment(0x88E1, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88E2, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88E3, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88E4, 'Dead data: &00', align=Align.INLINE)
d.comment(0x88E5, 'Dead data: &01', align=Align.INLINE)
d.comment(0x88E6, 'Dead data: &01', align=Align.INLINE)
d.comment(0x88E7, 'Dead data: &81', align=Align.INLINE)
d.comment(0x88E8, 'Y=7: offset to RXCB buffer addr byte 3', align=Align.INLINE)
d.comment(0x88EA, 'Read RXCB[7] (buffer addr high byte)', align=Align.INLINE)
d.comment(0x88EC, 'Compare to &FF', align=Align.INLINE)
d.comment(0x88EE, 'Not &FF: normal buffer, skip Tube check', align=Align.INLINE)
d.comment(0x88F1, 'Read RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x88F3, 'Check if addr byte 2 >= &FE (Tube range)', align=Align.INLINE)
d.comment(0x88F5, 'Tube/IO address: use fallback path', align=Align.INLINE)
d.comment(0x88F7, 'Transmit in progress?', align=Align.INLINE)
d.comment(0x88FA, 'No: fallback path', align=Align.INLINE)
d.comment(0x88FC, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x88FF, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x8901, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x8904, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x8905, 'Save carry on stack', align=Align.INLINE)
d.comment(0x8906, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x8908, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x890A, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x890B, '(continued)', align=Align.INLINE)
d.comment(0x890C, '(continued)', align=Align.INLINE)
d.comment(0x890D, '(continued)', align=Align.INLINE)
d.comment(0x890E, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x890F, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x8911, 'Store result byte', align=Align.INLINE)
d.comment(0x8914, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x8915, '(continued)', align=Align.INLINE)
d.comment(0x8916, '(continued)', align=Align.INLINE)
d.comment(0x8917, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x8918, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x891A, 'No: next byte pair', align=Align.INLINE)
d.comment(0x891C, 'Discard final borrow', align=Align.INLINE)
d.comment(0x891D, 'Save X', align=Align.INLINE)
d.comment(0x891E, 'Save X', align=Align.INLINE)
d.comment(0x891F, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x8921, 'CLC for base pointer addition', align=Align.INLINE)
d.comment(0x8922, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x8924, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x8925, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x8927, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x8929, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x892C, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x892E, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x8931, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x8934, 'Release Tube claim after reclaim', align=Align.INLINE)
d.comment(0x8937, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x8938, 'Restore X', align=Align.INLINE)
d.comment(0x8939, 'Restore X from stack', align=Align.INLINE)
d.comment(0x893A, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x893B, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x893D, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x893F, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x8941, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x8942, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x8944, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x8946, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x8948, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x894A, 'Propagate borrow only', align=Align.INLINE)
d.comment(0x894C, 'Temp store of adjusted hi byte', align=Align.INLINE)
d.comment(0x894E, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x8950, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x8952, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x8954, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x8956, 'Load RXCB[9]', align=Align.INLINE)
d.comment(0x8958, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x8959, 'Subtract adjusted hi byte', align=Align.INLINE)
d.comment(0x895B, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x895D, 'Return with C=1', align=Align.INLINE)
d.comment(0x895E, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x895F, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x8961, 'Write CR1 to ADLC register 0', align=Align.INLINE)
d.comment(0x8964, 'CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding', align=Align.INLINE)
d.comment(0x8966, 'Write CR4 to ADLC register 3', align=Align.INLINE)
d.comment(0x8969, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)
d.comment(0x896B, 'Write CR3 to ADLC register 1', align=Align.INLINE)
d.comment(0x896E, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x8970, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x8973, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x8975, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x8978, 'Return; ADLC now in RX listen mode', align=Align.INLINE)
d.comment(0x8979, 'Check if Econet has been initialised', align=Align.INLINE)
d.comment(0x897C, 'Not initialised: skip to RX listen', align=Align.INLINE)
d.comment(0x897E, 'Read current NMI handler low byte', align=Align.INLINE)
d.comment(0x8981, 'Expected: &B3 (nmi_rx_scout low)', align=Align.INLINE)
d.comment(0x8983, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x8985, 'Read current NMI handler high byte', align=Align.INLINE)
d.comment(0x8988, 'Test if high byte = &80 (page of nmi_rx_scout)', align=Align.INLINE)
d.comment(0x898A, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x898C, 'INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x898F, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x8992, 'TX not in progress', align=Align.INLINE)
d.comment(0x8995, 'Econet not initialised', align=Align.INLINE)
d.comment(0x8998, 'Y=5: service call workspace page', align=Align.INLINE)
d.comment(0x899A, 'Set ADLC to RX listen mode', align=Align.INLINE)
d.comment(0x899D, 'INTOFF: force /NMI high (IC97 flip-flop clear)', align=Align.INLINE)
d.comment(0x89A0, 'Save A', align=Align.INLINE)
d.comment(0x89A1, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x89A2, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x89A3, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x89A5, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x89A8, 'Jump to scout handler in ROM', align=Align.INLINE)
d.comment(0x89AB, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x89AE, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x89B1, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x89B3, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x89B6, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x89B7, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x89B8, 'Restore A from stack', align=Align.INLINE)
d.comment(0x89B9, 'INTON: guaranteed /NMI edge if ADLC IRQ asserted', align=Align.INLINE)
d.comment(0x89BC, 'Return from interrupt', align=Align.INLINE)
d.comment(0x89BD, """Unreferenced dead data (3 bytes)

3 bytes between the RTI at &89BC (end of the NMI
shim ROM source) and svc_dispatch_lo at &89C0.
The init copy loop (Y=1..&20) copies &899D-&89BC
to &0D00-&0D1F; these bytes are outside that range
and unreferenced. Likely unused development remnant.""")
d.comment(0x89BD, 'Dead data: &01', align=Align.INLINE)
d.comment(0x89BE, 'Dead data: &00', align=Align.INLINE)
d.comment(0x89BF, 'Dead data: &08', align=Align.INLINE)
d.comment(0x8A0B, 'Save service call number', align=Align.INLINE)
d.comment(0x8A0C, 'Is it service 15 (vectors claimed)?', align=Align.INLINE)
d.comment(0x8A0E, 'No: skip vectors-claimed handling', align=Align.INLINE)
d.comment(0x8A10, 'Save Y parameter', align=Align.INLINE)
d.comment(0x8A11, 'Save Y on stack', align=Align.INLINE)
d.comment(0x8A12, 'OSBYTE 0: read OS version', align=Align.INLINE)
d.comment(0x8A14, 'X=1 to request version number', align=Align.INLINE)
d.comment(0x8A19, 'OS 1.20?', align=Align.INLINE)
d.comment(0x8A1B, 'Yes: skip workspace setup', align=Align.INLINE)
d.comment(0x8A1D, 'OS 2.00 (BBC B+)?', align=Align.INLINE)
d.comment(0x8A1F, 'Yes: skip workspace setup', align=Align.INLINE)
d.comment(0x8A21, 'Transfer OS version to A', align=Align.INLINE)
d.comment(0x8A22, 'Save flags (Z set if OS 1.00)', align=Align.INLINE)
d.comment(0x8A23, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8A25, 'Restore flags', align=Align.INLINE)
d.comment(0x8A26, 'OS 1.00: skip INX', align=Align.INLINE)
d.comment(0x8A28, 'Adjust index for OS 3+ workspace', align=Align.INLINE)
d.comment(0x8A29, 'A=0', align=Align.INLINE)
d.comment(0x8A2B, 'Clear workspace byte for this ROM', align=Align.INLINE)
d.comment(0x8A2E, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8A30, 'Restore Y parameter', align=Align.INLINE)
d.comment(0x8A31, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8A32, 'Restore service call number', align=Align.INLINE)
d.comment(0x8A33, 'Check relocated code service dispatch', align=Align.INLINE)
d.comment(0x8A36, 'Save service call number', align=Align.INLINE)
d.comment(0x8A37, 'Service 1 (workspace claim)?', align=Align.INLINE)
d.comment(0x8A39, 'No: skip ADLC check', align=Align.INLINE)
d.comment(0x8A3B, 'Read ADLC status register 1', align=Align.INLINE)
d.comment(0x8A3E, 'Mask relevant status bits', align=Align.INLINE)
d.comment(0x8A40, 'Non-zero: ADLC absent, set flag', align=Align.INLINE)
d.comment(0x8A42, 'Read ADLC status register 2', align=Align.INLINE)
d.comment(0x8A45, 'Mask relevant status bits', align=Align.INLINE)
d.comment(0x8A47, 'Zero: ADLC present, skip', align=Align.INLINE)
d.comment(0x8A49, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0x8A4C, 'Set carry to mark ADLC absent', align=Align.INLINE)
d.comment(0x8A4D, 'Rotate carry into bit 7 of slot flag', align=Align.INLINE)
d.comment(0x8A50, 'Load ROM slot flag byte', align=Align.INLINE)
d.comment(0x8A53, 'Shift bit 7 (ADLC absent) into carry', align=Align.INLINE)
d.comment(0x8A54, 'Restore service call number', align=Align.INLINE)
d.comment(0x8A55, 'ADLC present: continue dispatch', align=Align.INLINE)
d.comment(0x8A57, 'ADLC absent: decline service, return', align=Align.INLINE)
d.comment(0x8A58, 'Service 15 (vectors claimed)?', align=Align.INLINE)
d.comment(0x8A5A, 'No: handle other services', align=Align.INLINE)
d.comment(0x8A5C, 'Already initialised?', align=Align.INLINE)
d.comment(0x8A5F, 'Yes: skip first-time init', align=Align.INLINE)
d.comment(0x8A61, 'X=1 (mark as initialised)', align=Align.INLINE)
d.comment(0x8A62, 'Set ROM present flag', align=Align.INLINE)
d.comment(0x8A65, 'Store service number as ROM counter', align=Align.INLINE)
d.comment(0x8A68, 'Point to ROM header copyright offset', align=Align.INLINE)
d.comment(0x8A6A, 'Set high byte of OSRDSC pointer', align=Align.INLINE)
d.comment(0x8A6C, 'Offset &0C: copyright string offset', align=Align.INLINE)
d.comment(0x8A6E, 'Set low byte of OSRDSC pointer', align=Align.INLINE)
d.comment(0x8A70, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A73, "First char 'N'?", align=Align.INLINE)
d.comment(0x8A75, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A77, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A7A, "Second char 'E'?", align=Align.INLINE)
d.comment(0x8A7C, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A7E, 'Read next ROM title char', align=Align.INLINE)
d.comment(0x8A81, "Third char 'T'?", align=Align.INLINE)
d.comment(0x8A83, 'No: not a NET ROM, try next', align=Align.INLINE)
d.comment(0x8A85, 'Get ROM slot being checked', align=Align.INLINE)
d.comment(0x8A88, 'Load its slot flag byte', align=Align.INLINE)
d.comment(0x8A8B, 'Set bit 7 to mark as NET ROM', align=Align.INLINE)
d.comment(0x8A8D, 'Store updated flag', align=Align.INLINE)
d.comment(0x8A90, 'Decrement ROM counter', align=Align.INLINE)
d.comment(0x8A93, 'More ROMs to check: loop', align=Align.INLINE)
d.comment(0x8A97, 'Advance read pointer to next byte', align=Align.INLINE)
d.comment(0x8A9F, 'Transfer service number to X', align=Align.INLINE)
d.comment(0x8AA0, 'Save current service state', align=Align.INLINE)
d.comment(0x8AA2, 'Push old state', align=Align.INLINE)
d.comment(0x8AA3, 'Restore service number to A', align=Align.INLINE)
d.comment(0x8AA4, 'Store as current service state', align=Align.INLINE)
d.comment(0x8AA6, 'Service < 13?', align=Align.INLINE)
d.comment(0x8AA8, 'Yes: use as dispatch index directly', align=Align.INLINE)
d.comment(0x8AAA, 'Subtract 5 (map 13-17 to 8-12)', align=Align.INLINE)
d.comment(0x8AAC, 'Mapped value = 13? (original was 18)', align=Align.INLINE)
d.comment(0x8AAE, 'Yes: valid service 18 (FS select)', align=Align.INLINE)
d.comment(0x8AB0, 'Unknown service: set index to 0', align=Align.INLINE)
d.comment(0x8AB2, 'Transfer dispatch index to X', align=Align.INLINE)
d.comment(0x8AB3, 'Index 0: unhandled service, skip', align=Align.INLINE)
d.comment(0x8AB5, 'Save current workspace page', align=Align.INLINE)
d.comment(0x8AB7, 'Push old page', align=Align.INLINE)
d.comment(0x8AB8, 'Set workspace page from Y parameter', align=Align.INLINE)
d.comment(0x8ABA, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8ABB, 'Y=0 for dispatch offset', align=Align.INLINE)
d.comment(0x8ABD, 'Dispatch to service handler via table', align=Align.INLINE)
d.comment(0x8AC0, 'Restore old workspace page', align=Align.INLINE)
d.comment(0x8AC1, 'Store it back', align=Align.INLINE)
d.comment(0x8AC3, 'Get service state (return code)', align=Align.INLINE)
d.comment(0x8AC5, 'Restore old service state', align=Align.INLINE)
d.comment(0x8AC6, 'Store it back', align=Align.INLINE)
d.comment(0x8AC8, 'Transfer return code to A', align=Align.INLINE)
d.comment(0x8AC9, 'Restore ROM slot to X', align=Align.INLINE)
d.comment(0x8ACB, 'Return to MOS', align=Align.INLINE)
d.comment(0x8ACC, 'Offset 4 in receive block', align=Align.INLINE)
d.comment(0x8ACE, 'Load remote operation flag', align=Align.INLINE)
d.comment(0x8AD0, 'Zero: already off, skip to cleanup', align=Align.INLINE)
d.comment(0x8AD2, 'A=0', align=Align.INLINE)
d.comment(0x8AD5, 'Clear remote operation flag', align=Align.INLINE)
d.comment(0x8AD8, 'OSBYTE &C9: keyboard disable', align=Align.INLINE)
d.comment(0x8ADD, 'A=&0A: workspace init parameter', align=Align.INLINE)
d.comment(0x8ADF, 'Initialise workspace area', align=Align.INLINE)
d.comment(0x8AE2, 'Save X in workspace', align=Align.INLINE)
d.comment(0x8AE4, 'A=&CE: start of key range', align=Align.INLINE)
d.comment(0x8AE6, 'Restore X from workspace', align=Align.INLINE)
d.comment(0x8AE8, 'Y=&7F: OSBYTE scan parameter', align=Align.INLINE)
d.comment(0x8AEA, 'OSBYTE: scan keyboard', align=Align.INLINE)
d.comment(0x8AED, 'Advance to next key code', align=Align.INLINE)
d.comment(0x8AEF, 'Reached &D0?', align=Align.INLINE)
d.comment(0x8AF1, 'No: loop back (scan &CE and &CF)', align=Align.INLINE)
d.comment(0x8AF3, 'A=0', align=Align.INLINE)
d.comment(0x8AF5, 'Clear service state', align=Align.INLINE)
d.comment(0x8AF7, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8AF9, 'Return', align=Align.INLINE)
d.comment(0x8AFA, 'Save A', align=Align.INLINE)
d.comment(0x8AFB, 'Copy OS text pointer low', align=Align.INLINE)
d.comment(0x8AFD, 'to fs_crc_lo', align=Align.INLINE)
d.comment(0x8AFF, 'Copy OS text pointer high', align=Align.INLINE)
d.comment(0x8B01, 'to fs_crc_hi', align=Align.INLINE)
d.comment(0x8B03, 'Restore A', align=Align.INLINE)
d.comment(0x8B04, 'Return', align=Align.INLINE)
d.comment(0x8B05, 'Y=5 (Econet filing system)?', align=Align.INLINE)
d.comment(0x8B07, 'No: not ours, return unclaimed', align=Align.INLINE)
d.comment(0x8B09, 'Already selected?', align=Align.INLINE)
d.comment(0x8B0C, 'Yes (bit 7 set): return unclaimed', align=Align.INLINE)
d.comment(0x8B0E, 'Get workspace page for this ROM slot', align=Align.INLINE)
d.comment(0x8B11, 'Store as high byte of load address', align=Align.INLINE)
d.comment(0x8B13, 'A=0', align=Align.INLINE)
d.comment(0x8B15, 'Clear low byte of load address', align=Align.INLINE)
d.comment(0x8B17, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8B18, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8B1A, 'Add byte to running checksum', align=Align.INLINE)
d.comment(0x8B1C, 'Decrement index', align=Align.INLINE)
d.comment(0x8B1D, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8B1F, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8B21, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x8B23, 'Match: checksum valid', align=Align.INLINE)
d.comment(0x8B25, 'Mismatch: raise checksum error', align=Align.INLINE)
d.comment(0x8B28, 'Call FSCV with A=6 (new FS)', align=Align.INLINE)
d.comment(0x8B2B, 'Y=&0D: end of FS context block', align=Align.INLINE)
d.comment(0x8B2D, 'Load byte from receive block', align=Align.INLINE)
d.comment(0x8B2F, 'Store into FS workspace', align=Align.INLINE)
d.comment(0x8B32, 'Decrement index', align=Align.INLINE)
d.comment(0x8B33, 'Reached offset 5?', align=Align.INLINE)
d.comment(0x8B35, 'No: continue copying', align=Align.INLINE)
d.comment(0x8B37, 'Shift bit 7 of FS flags into carry', align=Align.INLINE)
d.comment(0x8B3A, 'Clear carry', align=Align.INLINE)
d.comment(0x8B3B, 'Clear bit 7 of FS flags', align=Align.INLINE)
d.comment(0x8B3E, 'Y=&0D: vector table size - 1', align=Align.INLINE)
d.comment(0x8B40, 'Load FS vector address', align=Align.INLINE)
d.comment(0x8B43, 'Store into FILEV vector table', align=Align.INLINE)
d.comment(0x8B46, 'Decrement index', align=Align.INLINE)
d.comment(0x8B47, 'Loop until all vectors installed', align=Align.INLINE)
d.comment(0x8B49, 'Initialise ADLC and NMI workspace', align=Align.INLINE)
d.comment(0x8B4C, 'Y=&1B: extended vector offset', align=Align.INLINE)
d.comment(0x8B4E, 'X=7: two more vectors to set up', align=Align.INLINE)
d.comment(0x8B50, 'Set up extended vectors', align=Align.INLINE)
d.comment(0x8B53, 'A=0', align=Align.INLINE)
d.comment(0x8B55, 'Clear FS state byte', align=Align.INLINE)
d.comment(0x8B58, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B5B, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B5E, 'Clear service state', align=Align.INLINE)
d.comment(0x8B60, 'Offset &0E in receive block', align=Align.INLINE)
d.comment(0x8B62, 'Clear receive block flag', align=Align.INLINE)
d.comment(0x8B64, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8B67, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8B6A, 'Initialise FS state', align=Align.INLINE)
d.comment(0x8B6D, 'Y=&77: workspace block size - 1', align=Align.INLINE)
d.comment(0x8B6F, 'Load byte from source workspace', align=Align.INLINE)
d.comment(0x8B71, 'Store to page &10 shadow copy', align=Align.INLINE)
d.comment(0x8B74, 'Decrement index', align=Align.INLINE)
d.comment(0x8B75, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8B77, 'A=&80: FS selected flag', align=Align.INLINE)
d.comment(0x8B79, 'Set bit 7 of FS flags', align=Align.INLINE)
d.comment(0x8B7C, 'Store updated flags', align=Align.INLINE)
d.comment(0x8B7F, 'Issue service 15 (FS initialised)', align=Align.INLINE)
d.comment(0x8B82, 'X=&4A: NFS command table offset', align=Align.INLINE)
d.comment(0x8B84, 'Print help for NFS commands', align=Align.INLINE)
d.comment(0x8B87, 'X=0: utility command table offset', align=Align.INLINE)
d.comment(0x8B8B, 'X=&4A: NFS command table offset', align=Align.INLINE)
d.comment(0x8B8D, 'V clear: need to print header first', align=Align.INLINE)
d.comment(0x8B8F, 'Save X (table offset)', align=Align.INLINE)
d.comment(0x8B90, 'Push it', align=Align.INLINE)
d.comment(0x8B91, 'Save Y', align=Align.INLINE)
d.comment(0x8B92, 'Push it', align=Align.INLINE)
d.comment(0x8B93, 'Print version string header', align=Align.INLINE)
d.comment(0x8B96, 'Restore Y', align=Align.INLINE)
d.comment(0x8B97, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8B98, 'Restore X', align=Align.INLINE)
d.comment(0x8B99, 'Transfer to X', align=Align.INLINE)
d.comment(0x8B9A, 'Clear overflow flag', align=Align.INLINE)
d.comment(0x8BA0, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0x8BA1, 'Push it', align=Align.INLINE)
d.comment(0x8BA2, 'Save processor status', align=Align.INLINE)
d.comment(0x8BA3, 'Load byte from command table', align=Align.INLINE)
d.comment(0x8BA6, 'Bit 7 clear: valid entry, continue', align=Align.INLINE)
d.comment(0x8BA8, 'End of table: finish up', align=Align.INLINE)
d.comment(0x8BAB, 'Print two-space indent', align=Align.INLINE)
d.comment(0x8BB0, 'Y=9: max command name length', align=Align.INLINE)
d.comment(0x8BB2, 'Load first char of command name', align=Align.INLINE)
d.comment(0x8BB8, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8BB9, 'Decrement padding counter', align=Align.INLINE)
d.comment(0x8BBA, 'Load next character', align=Align.INLINE)
d.comment(0x8BBD, 'Bit 7 clear: more chars, continue', align=Align.INLINE)
d.comment(0x8BBF, 'Pad with spaces', align=Align.INLINE)
d.comment(0x8BC4, 'Decrement remaining pad count', align=Align.INLINE)
d.comment(0x8BC5, 'More padding needed: loop', align=Align.INLINE)
d.comment(0x8BC7, 'Load syntax descriptor byte', align=Align.INLINE)
d.comment(0x8BCA, 'Mask to get syntax string index', align=Align.INLINE)
d.comment(0x8BCC, 'Index &0E: shared commands?', align=Align.INLINE)
d.comment(0x8BCE, 'Yes: handle shared commands list', align=Align.INLINE)
d.comment(0x8BD0, 'Use index as Y', align=Align.INLINE)
d.comment(0x8BD1, 'Look up syntax string offset', align=Align.INLINE)
d.comment(0x8BD4, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x8BD5, 'Advance to next character', align=Align.INLINE)
d.comment(0x8BD6, 'Load syntax string character', align=Align.INLINE)
d.comment(0x8BD9, 'Zero terminator: end of syntax', align=Align.INLINE)
d.comment(0x8BDB, 'Carriage return: line continuation', align=Align.INLINE)
d.comment(0x8BDD, 'No: print the character', align=Align.INLINE)
d.comment(0x8BDF, 'Handle line wrap in syntax output', align=Align.INLINE)
d.comment(0x8BE2, 'Continue with next character', align=Align.INLINE)
d.comment(0x8BE8, 'Continue with next character', align=Align.INLINE)
d.comment(0x8BEB, 'Save table pointer', align=Align.INLINE)
d.comment(0x8BEC, 'Push it', align=Align.INLINE)
d.comment(0x8BED, 'Print opening parenthesis', align=Align.INLINE)
d.comment(0x8BF1, 'Y=0: shared command counter', align=Align.INLINE)
d.comment(0x8BF3, 'X=&D3: shared command table start', align=Align.INLINE)
d.comment(0x8BF5, 'Load byte from shared command table', align=Align.INLINE)
d.comment(0x8BF8, 'Bit 7 set: end of shared commands', align=Align.INLINE)
d.comment(0x8BFA, 'Back up one position', align=Align.INLINE)
d.comment(0x8BFB, 'Advance to next character', align=Align.INLINE)
d.comment(0x8BFC, 'Load command name character', align=Align.INLINE)
d.comment(0x8BFF, 'Bit 7 set: end of this name', align=Align.INLINE)
d.comment(0x8C04, 'Print more characters of name', align=Align.INLINE)
d.comment(0x8C07, 'Strip bit 7 from final character', align=Align.INLINE)
d.comment(0x8C0C, 'Count this shared command', align=Align.INLINE)
d.comment(0x8C0D, 'Printed 4 commands?', align=Align.INLINE)
d.comment(0x8C0F, 'No: continue on same line', align=Align.INLINE)
d.comment(0x8C11, 'Handle line wrap after 4 commands', align=Align.INLINE)
d.comment(0x8C14, 'X += 3: skip syntax descriptor and address', align=Align.INLINE)
d.comment(0x8C15, '(continued)', align=Align.INLINE)
d.comment(0x8C16, '(continued)', align=Align.INLINE)
d.comment(0x8C17, 'Loop for more shared commands', align=Align.INLINE)
d.comment(0x8C19, 'Restore original table pointer', align=Align.INLINE)
d.comment(0x8C1A, 'Transfer to X', align=Align.INLINE)
d.comment(0x8C1E, 'X += 3: skip syntax descriptor and address', align=Align.INLINE)
d.comment(0x8C1F, '(continued)', align=Align.INLINE)
d.comment(0x8C20, '(continued)', align=Align.INLINE)
d.comment(0x8C21, 'Loop for next command', align=Align.INLINE)
d.comment(0x8C24, 'Restore processor status', align=Align.INLINE)
d.comment(0x8C25, 'Restore Y', align=Align.INLINE)
d.comment(0x8C26, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8C27, 'Return', align=Align.INLINE)
d.comment(0x8C28, 'Read output stream type', align=Align.INLINE)
d.comment(0x8C2B, 'Stream 0 (VDU): no wrapping', align=Align.INLINE)
d.comment(0x8C2D, 'Stream 3 (printer)?', align=Align.INLINE)
d.comment(0x8C2F, 'Yes: no wrapping', align=Align.INLINE)
d.comment(0x8C31, 'Save Y', align=Align.INLINE)
d.comment(0x8C32, 'Push it', align=Align.INLINE)
d.comment(0x8C36, 'Y=&0B: indent width - 1', align=Align.INLINE)
d.comment(0x8C38, 'Space character', align=Align.INLINE)
d.comment(0x8C3D, 'Decrement indent counter', align=Align.INLINE)
d.comment(0x8C3E, 'More spaces needed: loop', align=Align.INLINE)
d.comment(0x8C40, 'Restore Y', align=Align.INLINE)
d.comment(0x8C41, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8C42, 'Return', align=Align.INLINE)
d.comment(0x8C43, 'X=0: start of utility command table', align=Align.INLINE)
d.comment(0x8C45, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C47, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C4A, 'Try to match command in table', align=Align.INLINE)
d.comment(0x8C4D, 'No match: return to caller', align=Align.INLINE)
d.comment(0x8C4F, 'Match found: execute command', align=Align.INLINE)
d.comment(0x8C52, 'Check for credits Easter egg', align=Align.INLINE)
d.comment(0x8C55, 'Get command line offset', align=Align.INLINE)
d.comment(0x8C57, 'Load character at offset', align=Align.INLINE)
d.comment(0x8C59, 'Is it CR (bare *HELP)?', align=Align.INLINE)
d.comment(0x8C5B, 'No: check for specific topic', align=Align.INLINE)
d.comment(0x8C5D, 'Print version string', align=Align.INLINE)
d.comment(0x8C60, 'X=&C4: start of help command list', align=Align.INLINE)
d.comment(0x8C62, 'Print command list from table', align=Align.INLINE)
d.comment(0x8C65, 'Restore Y (command line offset)', align=Align.INLINE)
d.comment(0x8C67, 'Return unclaimed', align=Align.INLINE)
d.comment(0x8C68, 'Test for topic match (sets flags)', align=Align.INLINE)
d.comment(0x8C6B, "Is first char '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C6D, 'No: try topic-specific help', align=Align.INLINE)
d.comment(0x8C6F, "'.' found: show full command list", align=Align.INLINE)
d.comment(0x8C72, 'Save text pointer to fs_crc', align=Align.INLINE)
d.comment(0x8C75, 'Save flags', align=Align.INLINE)
d.comment(0x8C76, 'X=&C4: help command table start', align=Align.INLINE)
d.comment(0x8C78, 'Try to match help topic in table', align=Align.INLINE)
d.comment(0x8C7B, 'No match: try next topic', align=Align.INLINE)
d.comment(0x8C7D, 'Restore flags', align=Align.INLINE)
d.comment(0x8C7E, 'Push return address high (&8C)', align=Align.INLINE)
d.comment(0x8C80, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C81, 'Push return address low (&74)', align=Align.INLINE)
d.comment(0x8C83, 'Push it for RTS dispatch', align=Align.INLINE)
d.comment(0x8C84, 'Load dispatch address high', align=Align.INLINE)
d.comment(0x8C87, 'Push dispatch high for RTS', align=Align.INLINE)
d.comment(0x8C88, 'Load dispatch address low', align=Align.INLINE)
d.comment(0x8C8B, 'Push dispatch low for RTS', align=Align.INLINE)
d.comment(0x8C8C, 'Dispatch via RTS (returns to &8C75)', align=Align.INLINE)
d.comment(0x8C8D, 'Restore flags from before match', align=Align.INLINE)
d.comment(0x8C8E, 'End of command line?', align=Align.INLINE)
d.comment(0x8C90, 'No: try matching next topic', align=Align.INLINE)
d.comment(0x8C94, 'Print version string via inline', align=Align.INLINE)
d.comment(0x8CAA, 'NOP (string terminator)', align=Align.INLINE)
d.comment(0x8CAB, 'Print station number', align=Align.INLINE)
d.comment(0x8CAE, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8CB0, 'Load workspace page for this slot', align=Align.INLINE)
d.comment(0x8CB3, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8CB4, 'Return with page in A and Y', align=Align.INLINE)
d.comment(0x8CB5, 'Get workspace page for ROM slot', align=Align.INLINE)
d.comment(0x8CB8, 'Store page in nfs_temp', align=Align.INLINE)
d.comment(0x8CBA, 'A=0', align=Align.INLINE)
d.comment(0x8CBC, 'Clear low byte of pointer', align=Align.INLINE)
d.comment(0x8CBE, 'Return', align=Align.INLINE)
d.comment(0x8CBF, 'OSBYTE &7A: scan keyboard from key 16', align=Align.INLINE)
d.comment(0x8CC5, 'No key pressed: select Net FS', align=Align.INLINE)
d.comment(0x8CC7, 'Key &19 (N)?', align=Align.INLINE)
d.comment(0x8CC9, 'Yes: write key state and boot', align=Align.INLINE)
d.comment(0x8CCB, "EOR with &55: maps to zero if 'N'", align=Align.INLINE)
d.comment(0x8CCD, 'Not N key: return unclaimed', align=Align.INLINE)
d.comment(0x8CD0, 'OSBYTE &78: write keys pressed', align=Align.INLINE)
d.comment(0x8CD5, 'Select NFS as current filing system', align=Align.INLINE)
d.comment(0x8CD8, 'Print station number', align=Align.INLINE)
d.comment(0x8CDE, 'Get workspace page', align=Align.INLINE)
d.comment(0x8CE0, 'Non-zero: already initialised, return', align=Align.INLINE)
d.comment(0x8CE2, 'Load boot flags', align=Align.INLINE)
d.comment(0x8CE5, 'Set bit 2 (auto-boot in progress)', align=Align.INLINE)
d.comment(0x8CE7, 'Store updated boot flags', align=Align.INLINE)
d.comment(0x8CEA, 'X=4: boot filename parameter', align=Align.INLINE)
d.comment(0x8CEC, 'Y=&8D: boot filename address high', align=Align.INLINE)
d.comment(0x8CEE, 'Execute boot file', align=Align.INLINE)
d.comment(0x8CF1, 'A=6: notify new filing system', align=Align.INLINE)
d.comment(0x8CF3, 'Call FSCV', align=Align.INLINE)
d.comment(0x8CF6, 'X=&0A: service 10 parameter', align=Align.INLINE)
d.comment(0x8CFA, 'Dispatch via FSCV', align=Align.INLINE)
d.comment(0x8CFD, 'X=&0F: service 15 parameter', align=Align.INLINE)
d.comment(0x8CFF, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8D0C, 'Get command line offset', align=Align.INLINE)
d.comment(0x8D0E, 'X=5: start of credits keyword', align=Align.INLINE)
d.comment(0x8D10, 'Load character from command line', align=Align.INLINE)
d.comment(0x8D12, 'Compare with credits keyword', align=Align.INLINE)
d.comment(0x8D15, 'Mismatch: check if keyword complete', align=Align.INLINE)
d.comment(0x8D17, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x8D18, 'Advance keyword pointer', align=Align.INLINE)
d.comment(0x8D19, 'Continue matching', align=Align.INLINE)
d.comment(0x8D1B, 'Reached end of keyword (X=&0D)?', align=Align.INLINE)
d.comment(0x8D1D, 'No: keyword not fully matched, return', align=Align.INLINE)
d.comment(0x8D1F, 'X=0: start of credits text', align=Align.INLINE)
d.comment(0x8D21, 'Load character from credits string', align=Align.INLINE)
d.comment(0x8D24, 'Zero terminator: done printing', align=Align.INLINE)
d.comment(0x8D29, 'Advance string pointer', align=Align.INLINE)
d.comment(0x8D2A, 'Continue printing', align=Align.INLINE)
d.comment(0x8D2C, 'Return', align=Align.INLINE)
d.comment(0x8D6E, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0x8D6F, 'Push it', align=Align.INLINE)
d.comment(0x8D70, 'OSBYTE &77: close SPOOL/EXEC', align=Align.INLINE)
d.comment(0x8D72, 'Store as pending operation marker', align=Align.INLINE)
d.comment(0x8D78, 'Y=0', align=Align.INLINE)
d.comment(0x8D7A, 'Clear password entry flag', align=Align.INLINE)
d.comment(0x8D7C, 'Reset FS connection state', align=Align.INLINE)
d.comment(0x8D7F, 'A=0', align=Align.INLINE)
d.comment(0x8D81, 'Clear pending operation marker', align=Align.INLINE)
d.comment(0x8D84, 'Restore command line offset', align=Align.INLINE)
d.comment(0x8D85, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8D86, 'Load first option byte', align=Align.INLINE)
d.comment(0x8D88, 'Parse station number if present', align=Align.INLINE)
d.comment(0x8D8B, 'Not a digit: skip to password entry', align=Align.INLINE)
d.comment(0x8D8D, 'Parse user ID string', align=Align.INLINE)
d.comment(0x8D90, 'No user ID: go to password', align=Align.INLINE)
d.comment(0x8D9C, 'No FS address: skip to password', align=Align.INLINE)
d.comment(0x8D92, 'Store file server station low', align=Align.INLINE)
d.comment(0x8D95, 'Check and store FS network', align=Align.INLINE)
d.comment(0x8D98, 'Skip separator', align=Align.INLINE)
d.comment(0x8D99, 'Parse next argument', align=Align.INLINE)
d.comment(0x8D9E, 'Store file server station high', align=Align.INLINE)
d.comment(0x8DA1, 'X=&FF: pre-decrement for loop', align=Align.INLINE)
d.comment(0x8DA3, 'Advance index', align=Align.INLINE)
d.comment(0x8DA4, 'Load logon command template byte', align=Align.INLINE)
d.comment(0x8DA7, 'Store into transmit buffer', align=Align.INLINE)
d.comment(0x8DAA, 'Bit 7 clear: more bytes, loop', align=Align.INLINE)
d.comment(0x8DAC, 'Send logon with file server lookup', align=Align.INLINE)
d.comment(0x8DAF, 'Success: skip to password entry', align=Align.INLINE)
d.comment(0x8DB1, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8DB4, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x8DB6, 'Advance to next byte', align=Align.INLINE)
d.comment(0x8DB7, 'Load byte from reply buffer', align=Align.INLINE)
d.comment(0x8DBA, 'Is it CR (end of prompt)?', align=Align.INLINE)
d.comment(0x8DBC, 'Yes: no colon found, skip to send', align=Align.INLINE)
d.comment(0x8DBE, "Is it ':' (password prompt)?", align=Align.INLINE)
d.comment(0x8DC0, 'No: keep scanning', align=Align.INLINE)
d.comment(0x8DC5, 'Save position of colon', align=Align.INLINE)
d.comment(0x8DC7, 'A=&FF: mark as escapable', align=Align.INLINE)
d.comment(0x8DC9, 'Set escape flag', align=Align.INLINE)
d.comment(0x8DCB, 'Check for escape condition', align=Align.INLINE)
d.comment(0x8DD3, 'Not NAK (&15): check other chars', align=Align.INLINE)
d.comment(0x8DD5, 'Restore colon position', align=Align.INLINE)
d.comment(0x8DD7, 'Non-zero: restart from colon', align=Align.INLINE)
d.comment(0x8DD9, 'At colon position?', align=Align.INLINE)
d.comment(0x8DDB, 'Yes: restart password input', align=Align.INLINE)
d.comment(0x8DDD, 'Backspace: move back one character', align=Align.INLINE)
d.comment(0x8DDE, 'If not at start: restart input', align=Align.INLINE)
d.comment(0x8DE0, 'Delete key (&7F)?', align=Align.INLINE)
d.comment(0x8DE2, 'Yes: handle backspace', align=Align.INLINE)
d.comment(0x8DE4, 'Store character in password buffer', align=Align.INLINE)
d.comment(0x8DE7, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x8DE8, 'Is it CR (end of password)?', align=Align.INLINE)
d.comment(0x8DEA, 'No: read another character', align=Align.INLINE)
d.comment(0x8DEF, 'Transfer string length to A', align=Align.INLINE)
d.comment(0x8DF0, 'Save string length', align=Align.INLINE)
d.comment(0x8DF1, 'Set up transmit control block', align=Align.INLINE)
d.comment(0x8DF4, 'Send to file server and get reply', align=Align.INLINE)
d.comment(0x8DF7, 'Restore string length', align=Align.INLINE)
d.comment(0x8DF8, 'Transfer to X (byte count)', align=Align.INLINE)
d.comment(0x8DF9, 'Include terminator', align=Align.INLINE)
d.comment(0x8DFA, 'Y=0', align=Align.INLINE)
d.comment(0x8DFE, 'Parse station number from cmd line', align=Align.INLINE)
d.comment(0x8E01, 'Compare with expected station', align=Align.INLINE)
d.comment(0x8E04, 'Different: return without clearing', align=Align.INLINE)
d.comment(0x8E06, 'Same: clear station byte', align=Align.INLINE)
d.comment(0x8E09, 'Return', align=Align.INLINE)
d.comment(0x8E0A, 'Build FS command packet', align=Align.INLINE)
d.comment(0x8E0D, 'Transfer result to Y', align=Align.INLINE)
d.comment(0x8E0E, 'Set up command and send to FS', align=Align.INLINE)
d.comment(0x8E11, 'Load reply function code', align=Align.INLINE)
d.comment(0x8E14, 'Zero: no reply, return', align=Align.INLINE)
d.comment(0x8E16, 'Load first reply byte', align=Align.INLINE)
d.comment(0x8E19, 'Y=&17: logon dispatch offset', align=Align.INLINE)
d.comment(0x8E1D, 'Parse reply as decimal number', align=Align.INLINE)
d.comment(0x8E20, 'Result >= 8?', align=Align.INLINE)
d.comment(0x8E22, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E24, 'Transfer handle to X', align=Align.INLINE)
d.comment(0x8E25, 'Look up in open files table', align=Align.INLINE)
d.comment(0x8E28, 'Transfer result to A', align=Align.INLINE)
d.comment(0x8E29, 'Y=&13: handle dispatch offset', align=Align.INLINE)
d.comment(0x8E2D, 'Handle >= 5?', align=Align.INLINE)
d.comment(0x8E2F, 'Yes: out of range, return', align=Align.INLINE)
d.comment(0x8E31, 'Y=&0E: directory dispatch offset', align=Align.INLINE)
d.comment(0x8E33, 'Advance X to target index', align=Align.INLINE)
d.comment(0x8E35, 'Y still positive: continue counting', align=Align.INLINE)
d.comment(0x8E34, 'Decrement Y offset counter', align=Align.INLINE)
d.comment(0x8E37, 'Y=&FF: will be ignored by caller', align=Align.INLINE)
d.comment(0x8E38, 'Load dispatch address high byte', align=Align.INLINE)
d.comment(0x8E3B, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E3C, 'Load dispatch address low byte', align=Align.INLINE)
d.comment(0x8E3F, 'Push low byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E40, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x8E42, 'Dispatch via RTS', align=Align.INLINE)
d.comment(0x8E43, """Printer server template (8 bytes)

Default printer server configuration data, read
indirectly by copy_ps_data via LDA ps_template_base,X
with X=&F8..&FF (reaching ps_template_base+&F8 =
&8E43). Contains "PRINT " (6 bytes) as the default
printer server name, followed by &01 and &00 as
default status bytes. Absent from NFS versions;
unique to ANFS.""")
d.comment(0x8E43, 'PS template: default name "PRINT "', align=Align.INLINE)
d.comment(0x8E49, 'PS template: status &01', align=Align.INLINE)
d.comment(0x8E4A, 'PS template: terminator &00', align=Align.INLINE)
d.comment(0x8E6D, 'X=0', align=Align.INLINE)
d.comment(0x8E6F, 'Y=&FF', align=Align.INLINE)
d.comment(0x8E71, 'Execute OSBYTE and return', align=Align.INLINE)
d.comment(0x8E74, """NETV handler address

2-byte handler address for the NETV extended
vector, read by write_vector_entry at Y=&36
from svc_dispatch_lo_offset (push_dispatch_lo+2).
Points to netv_handler (&A968) which dispatches
OSWORDs 0-8 to Econet handlers. Interleaved with
the OSBYTE wrapper code in the data area.""")
d.comment(0x8E74, 'NETV handler: netv_handler (&A968)', align=Align.INLINE)
d.comment(0x8E76, 'X=0', align=Align.INLINE)
d.comment(0x8E78, 'Y=0', align=Align.INLINE)
d.comment(0x8E7C, 'Get original OSBYTE A parameter', align=Align.INLINE)
d.comment(0x8E7E, 'Subtract &31 (map &32-&35 to 1-4)', align=Align.INLINE)
d.comment(0x8E80, 'In range 0-3?', align=Align.INLINE)
d.comment(0x8E82, 'No: not ours, return unclaimed', align=Align.INLINE)
d.comment(0x8E84, 'Transfer to X as dispatch index', align=Align.INLINE)
d.comment(0x8E85, 'A=0: claim the service call', align=Align.INLINE)
d.comment(0x8E87, 'Set return value to 0 (claimed)', align=Align.INLINE)
d.comment(0x8E89, 'Transfer Y to A (OSBYTE Y param)', align=Align.INLINE)
d.comment(0x8E8A, 'Y=&21: OSBYTE dispatch offset', align=Align.INLINE)
d.comment(0x8E8C, 'Dispatch to OSBYTE handler via table', align=Align.INLINE)
d.comment(0x8E8F, 'Need at least &16 pages?', align=Align.INLINE)
d.comment(0x8E91, 'Already enough: return', align=Align.INLINE)
d.comment(0x8E93, 'Request &16 pages of workspace', align=Align.INLINE)
d.comment(0x8E95, 'Return', align=Align.INLINE)
d.comment(0x8E96, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8E97, 'Y >= &21?', align=Align.INLINE)
d.comment(0x8E99, 'No: use Y as-is', align=Align.INLINE)
d.comment(0x8E9B, 'Cap at &21', align=Align.INLINE)
d.comment(0x8E9D, 'Offset &0F in receive block', align=Align.INLINE)
d.comment(0x8E9F, 'Store workspace page count', align=Align.INLINE)
d.comment(0x8EA1, 'Return', align=Align.INLINE)
d.comment(0x8EA2, 'Store Y as receive block page', align=Align.INLINE)
d.comment(0x8EA4, 'Advance to next page', align=Align.INLINE)
d.comment(0x8EA5, 'Store as NFS workspace page', align=Align.INLINE)
d.comment(0x8EA7, 'Advance to next page', align=Align.INLINE)
d.comment(0x8EA8, 'Transfer page to A', align=Align.INLINE)
d.comment(0x8EA9, 'Get current ROM slot number', align=Align.INLINE)
d.comment(0x8EAB, 'Store workspace page for this slot', align=Align.INLINE)
d.comment(0x8EAE, 'A=0', align=Align.INLINE)
d.comment(0x8EB0, 'Clear receive block pointer low', align=Align.INLINE)
d.comment(0x8EB2, 'Clear NFS workspace pointer low', align=Align.INLINE)
d.comment(0x8EB4, 'Clear workspace page counter', align=Align.INLINE)
d.comment(0x8EB6, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8EB9, 'Offset 4 in receive block', align=Align.INLINE)
d.comment(0x8EBB, 'Clear remote operation flag', align=Align.INLINE)
d.comment(0x8EBD, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x8EBF, 'X=1: workspace claim service', align=Align.INLINE)
d.comment(0x8EC1, 'Y=&0E: requested pages', align=Align.INLINE)
d.comment(0x8EC6, 'Record final workspace allocation', align=Align.INLINE)
d.comment(0x8EC9, 'Load ROM present flag', align=Align.INLINE)
d.comment(0x8ECC, 'Zero: first ROM init, skip FS setup', align=Align.INLINE)
d.comment(0x8ECE, 'Set up workspace pointers', align=Align.INLINE)
d.comment(0x8ED1, 'Clear FS flags', align=Align.INLINE)
d.comment(0x8ED4, 'A=0, transfer to Y', align=Align.INLINE)
d.comment(0x8ED5, 'Clear byte in FS workspace', align=Align.INLINE)
d.comment(0x8ED7, 'Clear byte in NFS workspace', align=Align.INLINE)
d.comment(0x8ED9, 'Advance index', align=Align.INLINE)
d.comment(0x8EDA, 'Loop until full page zeroed', align=Align.INLINE)
d.comment(0x8EDC, 'Offset &0C in receive block', align=Align.INLINE)
d.comment(0x8EDE, 'Clear protection flags', align=Align.INLINE)
d.comment(0x8EE0, 'Initialise station identity block', align=Align.INLINE)
d.comment(0x8EE3, 'Offset 6 in receive block', align=Align.INLINE)
d.comment(0x8EE5, 'A=&FE: default station ID marker', align=Align.INLINE)
d.comment(0x8EE7, 'Store default station low', align=Align.INLINE)
d.comment(0x8EEA, 'Store into receive block', align=Align.INLINE)
d.comment(0x8EEC, 'A=0', align=Align.INLINE)
d.comment(0x8EEE, 'Clear station high byte', align=Align.INLINE)
d.comment(0x8EF2, 'Store into receive block', align=Align.INLINE)
d.comment(0x8EF4, 'Offset 3 in NFS workspace', align=Align.INLINE)
d.comment(0x8EF6, 'Clear NFS workspace byte 3', align=Align.INLINE)
d.comment(0x8EF9, 'A=&EB: default listen state', align=Align.INLINE)
d.comment(0x8EFB, 'Store at NFS workspace offset 2', align=Align.INLINE)
d.comment(0x8EFD, 'X=3: init data byte count', align=Align.INLINE)
d.comment(0x8EFF, 'Load initialisation data byte', align=Align.INLINE)
d.comment(0x8F02, 'Store in workspace', align=Align.INLINE)
d.comment(0x8F05, 'Decrement counter', align=Align.INLINE)
d.comment(0x8F06, 'More bytes: loop', align=Align.INLINE)
d.comment(0x8F08, 'Clear workspace flag', align=Align.INLINE)
d.comment(0x8F0B, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x8F2C, """Workspace init data

3 bytes read via LDA ws_init_data,X with X=3
down to 1. ws_init_data overlaps the high byte
of JMP err_bad_station_num; byte 0 is the JMP
operand (&92), never read (BNE exits when X=0).
Stores to l0d6e, l0d6f, l0d70.""")
d.comment(0x8F2C, 'l0d6e: init=&FF (retry count)', align=Align.INLINE)
d.comment(0x8F2D, 'l0d6f: init=&28 (40, receive poll count)', align=Align.INLINE)
d.comment(0x8F2E, 'l0d70: init=&0A (10, machine peek retries)', align=Align.INLINE)
d.comment(0x8F0E, 'Initialise ADLC protection table', align=Align.INLINE)
d.comment(0x8F11, 'Get current workspace page', align=Align.INLINE)
d.comment(0x8F13, 'Allocate FS handle page', align=Align.INLINE)
d.comment(0x8F16, 'Allocation failed: finish init', align=Align.INLINE)
d.comment(0x8F18, 'A=&3F: default handle permissions', align=Align.INLINE)
d.comment(0x8F1A, 'Store handle permissions', align=Align.INLINE)
d.comment(0x8F1C, 'Advance to next page', align=Align.INLINE)
d.comment(0x8F1E, 'Continue allocating: loop', align=Align.INLINE)
d.comment(0x8F20, 'Restore FS context from saved state', align=Align.INLINE)
d.comment(0x8F23, 'Read station ID from hardware', align=Align.INLINE)
d.comment(0x8F26, 'Transfer to A', align=Align.INLINE)
d.comment(0x8F27, 'Non-zero: station ID valid', align=Align.INLINE)
d.comment(0x8F29, 'Station 0: report error', align=Align.INLINE)
d.comment(0x8F2F, 'Increment station ID', align=Align.INLINE)
d.comment(0x8F30, 'Overflow to 0: report error', align=Align.INLINE)
d.comment(0x8F32, 'Offset 5: station ID in recv block', align=Align.INLINE)
d.comment(0x8F34, 'Store station ID', align=Align.INLINE)
d.comment(0x8F36, 'X=&40: Econet flag byte', align=Align.INLINE)
d.comment(0x8F38, 'Store Econet control flag', align=Align.INLINE)
d.comment(0x8F3B, 'A=3: protection level', align=Align.INLINE)
d.comment(0x8F3D, 'Set up Econet protection', align=Align.INLINE)
d.comment(0x8F40, 'Initialise ADLC hardware', align=Align.INLINE)
d.comment(0x8F43, 'OSBYTE &A8: read ROM pointer table', align=Align.INLINE)
d.comment(0x8F45, 'Read ROM pointer table address', align=Align.INLINE)
d.comment(0x8F48, 'Store table pointer low', align=Align.INLINE)
d.comment(0x8F4A, 'Store table pointer high', align=Align.INLINE)
d.comment(0x8F4C, 'Y=&36: NETV vector offset', align=Align.INLINE)
d.comment(0x8F4E, 'Set NETV address', align=Align.INLINE)
d.comment(0x8F51, 'X=1: one more vector pair to set', align=Align.INLINE)
d.comment(0x8F53, 'Load vector address low byte', align=Align.INLINE)
d.comment(0x8F56, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x8F58, 'Advance to high byte', align=Align.INLINE)
d.comment(0x8F59, 'Load vector address high byte', align=Align.INLINE)
d.comment(0x8F5C, 'Store into extended vector table', align=Align.INLINE)
d.comment(0x8F5E, 'Advance to ROM ID byte', align=Align.INLINE)
d.comment(0x8F5F, 'Load current ROM slot number', align=Align.INLINE)
d.comment(0x8F61, 'Store ROM ID in extended vector', align=Align.INLINE)
d.comment(0x8F63, 'Advance to next vector entry', align=Align.INLINE)
d.comment(0x8F64, 'Decrement vector counter', align=Align.INLINE)
d.comment(0x8F65, 'More vectors to set: loop', align=Align.INLINE)
d.comment(0x8F67, 'X=&FF', align=Align.INLINE)
d.comment(0x8F68, 'Store &FF in workspace flag', align=Align.INLINE)
d.comment(0x8F6B, 'Restore FS state if previously active', align=Align.INLINE)
d.comment(0x8F6E, 'Get workspace page for ROM slot', align=Align.INLINE)
d.comment(0x8F71, 'Advance Y past workspace page', align=Align.INLINE)
d.comment(0x8F72, 'Return', align=Align.INLINE)
d.comment(0x8F73, 'Y=&0D: end of FS context block', align=Align.INLINE)
d.comment(0x8F75, 'Load FS context byte', align=Align.INLINE)
d.comment(0x8F78, 'Store into receive block', align=Align.INLINE)
d.comment(0x8F7A, 'Decrement index', align=Align.INLINE)
d.comment(0x8F7B, 'Reached offset 5?', align=Align.INLINE)
d.comment(0x8F7D, 'No: continue copying', align=Align.INLINE)
d.comment(0x8F7F, 'Return', align=Align.INLINE)
d.comment(0x8F80, 'FS currently selected?', align=Align.INLINE)
d.comment(0x8F83, 'No (bit 7 clear): return', align=Align.INLINE)
d.comment(0x8F85, 'Y=0', align=Align.INLINE)
d.comment(0x8F87, 'Reset FS connection state', align=Align.INLINE)
d.comment(0x8F8A, 'OSBYTE &77: close SPOOL/EXEC', align=Align.INLINE)
d.comment(0x8F8F, 'Restore FS context to receive block', align=Align.INLINE)
d.comment(0x8F92, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8F94, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x8F96, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8F97, 'Add byte from page &10 shadow', align=Align.INLINE)
d.comment(0x8F9A, 'Decrement index', align=Align.INLINE)
d.comment(0x8F9B, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8F9D, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8FA1, 'Load byte from page &10 shadow', align=Align.INLINE)
d.comment(0x8FA4, 'Copy to FS workspace', align=Align.INLINE)
d.comment(0x8FA6, 'Decrement index', align=Align.INLINE)
d.comment(0x8FA7, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8FA9, 'Load FS flags', align=Align.INLINE)
d.comment(0x8FAC, 'Clear bit 7 (FS no longer selected)', align=Align.INLINE)
d.comment(0x8FAE, 'Store updated flags', align=Align.INLINE)
d.comment(0x8FB1, 'Return', align=Align.INLINE)
d.comment(0x8FB2, 'Save processor status', align=Align.INLINE)
d.comment(0x8FB3, 'Save A', align=Align.INLINE)
d.comment(0x8FB4, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x8FB5, 'Save Y', align=Align.INLINE)
d.comment(0x8FB6, 'Y=&76: checksum range end', align=Align.INLINE)
d.comment(0x8FB8, 'A=0: checksum accumulator', align=Align.INLINE)
d.comment(0x8FBA, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x8FBB, 'Add byte from FS workspace', align=Align.INLINE)
d.comment(0x8FBD, 'Decrement index', align=Align.INLINE)
d.comment(0x8FBE, 'Loop until all bytes summed', align=Align.INLINE)
d.comment(0x8FC0, 'Y=&77: checksum storage offset', align=Align.INLINE)
d.comment(0x8FC2, 'Compare with stored checksum', align=Align.INLINE)
d.comment(0x8FC4, 'Mismatch: raise checksum error', align=Align.INLINE)
d.comment(0x8FC6, 'Restore Y', align=Align.INLINE)
d.comment(0x8FC7, 'Transfer to Y', align=Align.INLINE)
d.comment(0x8FC8, 'Restore A', align=Align.INLINE)
d.comment(0x8FC9, 'Restore processor status', align=Align.INLINE)
d.comment(0x8FCA, 'Return (checksum valid)', align=Align.INLINE)
d.comment(0x8FCB, 'Error number &AA', align=Align.INLINE)
d.comment(0x8FCD, "Raise 'net checksum' error", align=Align.INLINE)
d.comment(0x8FDD, "Print 'Econet Station ' via inline", align=Align.INLINE)
d.comment(0x8FEF, 'Offset 5: station ID', align=Align.INLINE)
d.comment(0x8FF1, 'Load station ID from receive block', align=Align.INLINE)
d.comment(0x8FF3, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x8FF6, 'Space character', align=Align.INLINE)
d.comment(0x8FF8, 'Check ADLC status register 2', align=Align.INLINE)
d.comment(0x8FFB, 'Clock present: skip warning', align=Align.INLINE)
d.comment(0x8FFD, "Print ' No Clock' via inline", align=Align.INLINE)
d.comment(0x9009, 'NOP (string terminator)', align=Align.INLINE)
d.comment(0x900D, 'Return', align=Align.INLINE)
d.comment(0x900E, """*HELP command syntax strings

13 null-terminated syntax help strings displayed
by *HELP after each command name. Multi-line
entries use &0D as a line break. Indexed by
cmd_syntax_table via the low 5 bits of each
command's syntax descriptor byte.""")
d.comment(0x900E, 'Syn 1: *Dir, *LCat, *LEx, *Wipe', align=Align.INLINE)
d.comment(0x9015, 'Null terminator', align=Align.INLINE)
d.comment(0x9016, 'Syn 2: *I Am (login)', align=Align.INLINE)
d.comment(0x902E, 'Line break', align=Align.INLINE)
d.comment(0x902F, 'Syn 2 continued: password clause', align=Align.INLINE)
d.comment(0x9042, 'Null terminator', align=Align.INLINE)
d.comment(0x9043, 'Syn 3: *Delete, *FS, *Remove', align=Align.INLINE)
d.comment(0x904B, 'Null terminator', align=Align.INLINE)
d.comment(0x904C, 'Syn 4: *Dump', align=Align.INLINE)
d.comment(0x9061, 'Line break', align=Align.INLINE)
d.comment(0x9062, 'Syn 4 continued: address clause', align=Align.INLINE)
d.comment(0x906E, 'Null terminator', align=Align.INLINE)
d.comment(0x906F, 'Syn 5: *Lib', align=Align.INLINE)
d.comment(0x9074, 'Null terminator', align=Align.INLINE)
d.comment(0x9075, 'Syn 6: *CDir', align=Align.INLINE)
d.comment(0x9085, 'Null terminator', align=Align.INLINE)
d.comment(0x9086, 'Syn 7: *Pass', align=Align.INLINE)
d.comment(0x9099, 'Line break', align=Align.INLINE)
d.comment(0x909A, 'Syn 7 continued: new password', align=Align.INLINE)
d.comment(0x90A8, 'Null terminator', align=Align.INLINE)
d.comment(0x90A9, 'Syn 8: *PS, *Pollps', align=Align.INLINE)
d.comment(0x90BF, 'Null terminator', align=Align.INLINE)
d.comment(0x90C0, 'Syn 9: *Access', align=Align.INLINE)
d.comment(0x90DB, 'Null terminator', align=Align.INLINE)
d.comment(0x90DC, 'Syn 10: *Rename', align=Align.INLINE)
d.comment(0x90F5, 'Null terminator', align=Align.INLINE)
d.comment(0x90F6, 'Syn 11: (station id. argument)', align=Align.INLINE)
d.comment(0x9102, 'Null terminator', align=Align.INLINE)
d.comment(0x9103, 'Syn 12: *Print, *Type', align=Align.INLINE)
d.comment(0x910D, 'Null terminator', align=Align.INLINE)
d.comment(0x910E, """Command syntax string offset table

13 offsets into cmd_syntax_strings (&900E).
Indexed by the low 5 bits of each command table
syntax descriptor byte. Index &0E is handled
separately as a shared-commands list. The print
loop at &8BD5 does INY before LDA, so each offset
points to the byte before the first character.""")
d.comment(0x910E, 'Idx 0: (no syntax)', align=Align.INLINE)
d.comment(0x910F, 'Idx 1: "(<dir>)" (Y wraps via &FF)', align=Align.INLINE)
d.comment(0x9110, 'Idx 2: "(<stn.id.>) <user id.>..."', align=Align.INLINE)
d.comment(0x9111, 'Idx 3: "<object>"', align=Align.INLINE)
d.comment(0x9112, 'Idx 4: "<filename> (<offset>...)"', align=Align.INLINE)
d.comment(0x9113, 'Idx 5: "<dir>"', align=Align.INLINE)
d.comment(0x9114, 'Idx 6: "<dir> (<number>)"', align=Align.INLINE)
d.comment(0x9115, 'Idx 7: "(:<CR>) <password>..."', align=Align.INLINE)
d.comment(0x9116, 'Idx 8: "(<stn.id.>|<ps type>)"', align=Align.INLINE)
d.comment(0x9117, 'Idx 9: "<object> (L)(W)(R)..."', align=Align.INLINE)
d.comment(0x9118, 'Idx 10: "<filename> <new filename>"', align=Align.INLINE)
d.comment(0x9119, 'Idx 11: "(<stn. id.>)"', align=Align.INLINE)
d.comment(0x911A, 'Idx 12: "<filename>"', align=Align.INLINE)
d.comment(0x911B, 'Save full byte', align=Align.INLINE)
d.comment(0x911C, 'Shift high nybble to low', align=Align.INLINE)
d.comment(0x911D, 'Continue shifting', align=Align.INLINE)
d.comment(0x911E, 'Continue shifting', align=Align.INLINE)
d.comment(0x911F, 'High nybble now in bits 0-3', align=Align.INLINE)
d.comment(0x9120, 'Print high nybble as hex digit', align=Align.INLINE)
d.comment(0x9123, 'Restore full byte', align=Align.INLINE)
d.comment(0x9124, 'Mask to low nybble', align=Align.INLINE)
d.comment(0x9126, 'Digit >= &0A?', align=Align.INLINE)
d.comment(0x9128, 'No: skip letter adjustment', align=Align.INLINE)
d.comment(0x912A, "Add 7 to get 'A'-'F' (6 + carry)", align=Align.INLINE)
d.comment(0x912C, "Add &30 for ASCII '0'-'9' or 'A'-'F'", align=Align.INLINE)
d.comment(0x9477, """TXCB initialisation template (12 bytes)

Copied by init_txcb into the TXCB workspace at
&00C0. For offsets 0-1, the destination station
bytes are also copied from l0e00 into txcb_dest.

The &FF byte at offset 6 (bit_test_ff, &947D)
serves double duty: it is part of this template
AND a BIT target used by 22 callers to set the
V and N flags without clobbering A.""")
d.comment(0x9477, 'Offset 0: txcb_ctrl = &80 (transmit)', align=Align.INLINE)
d.comment(0x9478, 'Offset 1: txcb_port = &99 (FS reply)', align=Align.INLINE)
d.comment(0x9479, 'Offset 2: txcb_dest lo (overwritten)', align=Align.INLINE)
d.comment(0x947A, 'Offset 3: txcb_dest hi (overwritten)', align=Align.INLINE)
d.comment(0x947B, 'Offset 4: txcb_start = 0', align=Align.INLINE)
d.comment(0x947C, 'Offset 5: buffer start hi (page &0F)', align=Align.INLINE)
d.comment(0x947D, 'Offset 6: BIT target / buffer end lo', align=Align.INLINE)
d.comment(0x947E, 'Offset 7: txcb_pos = &FF', align=Align.INLINE)
d.comment(0x947F, 'Offset 8: txcb_end = &FF', align=Align.INLINE)
d.comment(0x9480, 'Offset 9: buffer end hi (page &0F)', align=Align.INLINE)
d.comment(0x9481, 'Offset 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x9482, 'Offset 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x89C0, """Service dispatch table (37 entries, split lo/hi).
PHA/PHA/RTS dispatch used by svc_dispatch.
Indices 0-14: service calls (index = service + 1).
Indices 15-36: FS command and OSWORD routing.
Indices 1, 7, 11 point to return_4 (no-op RTS).""")

d.label(0x89C0, 'svc_dispatch_lo')

d.label(0x89E5, 'svc_dispatch_hi')
for i in range(1, 37):
    d.rts_code_ptr(0x89C0 + i, 0x89E5 + i)
svc_dispatch_comments = ['dummy entry (outside ROM range)', 'Svc 0: already claimed (no-op)', 'Svc 1: absolute workspace', 'Svc 2: private workspace', 'Svc 3: auto-boot', 'Svc 4: unrecognised star command', 'Svc 5: unrecognised interrupt', 'Svc 6: BRK (no-op)', 'Svc 7: unrecognised OSBYTE', 'Svc 8: unrecognised OSWORD', 'Svc 9: *HELP', 'Svc 10: static workspace (no-op)', 'Svc 11: NMI release (reclaim NMIs)', 'Svc 12: NMI claim (save NMI state)', 'Svc 18: filing system selection', 'Lang 0: no language / Tube', 'Lang 1: normal startup', 'Lang 2: softkey byte (Electron)', 'Lang 3: softkey length (Electron)', 'Lang 4: remote validated', 'FSCV 0: *OPT', 'FSCV 1: EOF check', 'FSCV 2: */ (run)', 'FSCV 3: unrecognised star command', 'FSCV 4: *RUN', 'FSCV 5: *CAT', 'FSCV 6: shutdown', 'FSCV 7: read handle range', 'FS reply: print directory name', 'FS reply: copy handles + boot', 'FS reply: copy handles', 'FS reply: set CSD handle', 'FS reply: notify + execute', 'FS reply: set library handle', '*NET1: read handle from packet', '*NET2: read handle from workspace', '*NET3: close handle']
for i, body in enumerate(svc_dispatch_comments):
    d.comment(0x89C0 + i, f'lo - {body}', align=Align.INLINE)
    d.comment(0x89E5 + i, f'hi - {body}', align=Align.INLINE)
d.entry(0x8E8F)
d.entry(0x8EA2)
d.entry(0x8CBF)
d.entry(0x8C43)
d.entry(0x8E7C)
d.entry(0xA4D6)
d.entry(0x8C52)
d.entry(0x8B05)

d.label(0x8E8F, 'svc_1_abs_workspace')

d.label(0x8EA2, 'svc_2_private_workspace')

d.label(0x8CBF, 'svc_3_autoboot')

d.label(0x8C43, 'svc_4_star_command')

d.label(0x8E7C, 'svc_7_osbyte')

d.label(0xA4D6, 'svc_8_osword')

d.label(0x8C52, 'svc_9_help')

d.label(0x8B05, 'svc_18_fs_select')


d.subroutine(0x8E8F, 'svc_1_abs_workspace', title='Service 1: absolute workspace claim', description="""Ensures the NFS workspace allocation is at least
&16 pages by checking Y on entry. If Y < &16,
sets Y = &16 to claim the required pages;
otherwise returns Y unchanged. This is a passive
claim — NFS only raises the allocation, never
lowers it.""", on_entry={'y': 'current highest workspace page claim'}, on_exit={'y': '>= &16 (NFS minimum requirement)'})


d.subroutine(0x8EA2, 'svc_2_private_workspace', title='Service 2: claim private workspace and initialise NFS', description="""Handles MOS service call 2 (private workspace
claim). Allocates two workspace pages starting
at Y: the receive block page (net_rx_ptr_hi) and
NFS workspace page (nfs_workspace_hi), plus a
per-ROM workspace page stored at &0DF0+ROM slot.
Zeroes all workspace, initialises the station ID
from the Econet hardware register at &FE18,
allocates FS handle pages, copies initial state
to page &10, and falls through to
init_adlc_and_vectors.""", on_entry={'y': 'first available private workspace page'})


d.subroutine(0x8CBF, 'svc_3_autoboot', title='Service 3: auto-boot on reset', description="""Scans the keyboard via OSBYTE &7A for the 'N' key
(&19 or &55 EOR'd with &55). If pressed, records
the key state via OSBYTE &78. Selects the network
filing system by calling cmd_net_fs, prints the
station ID, then checks if this is the first boot
(ws_page = 0). If so, sets the auto-boot flag in
&1071 and JMPs to cmd_fs_entry to execute the boot
file.""")


d.subroutine(0x8C43, 'svc_4_star_command', title='Service 4: unrecognised star command', description="""Saves the OS text pointer, then calls match_fs_cmd
to search the command table starting at offset 0
(all command sub-tables). If no match is found (carry
set), returns with the service call unclaimed. On
a match, JMPs to cmd_fs_reentry to execute the
matched command handler via the PHA/PHA/RTS
dispatch mechanism.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8E7C, 'svc_7_osbyte', title='Service 7: unrecognised OSBYTE', description="""Maps Econet OSBYTE codes &32-&35 to dispatch
indices 0-3 by subtracting &31 (with carry from
a preceding SBC). Returns unclaimed if the OSBYTE
number is outside this range. For valid codes,
claims the service (sets svc_state to 0) and
JMPs to svc_dispatch with Y=&21 to reach the
Econet OSBYTE handler table.""", on_entry={'a': 'OSBYTE number (from osbyte_a_copy at &EF)'})


d.subroutine(0xA4D6, 'svc_8_osword', title='Filing system OSWORD entry', description="""Handles MOS service call 8 (unrecognised OSWORD).
Filters OSWORD codes &0E-&14 by subtracting &0E (via
CLC/SBC &0D) and rejecting values outside 0-6. For
valid codes, calls osword_setup_handler to push the
dispatch address, then copies 3 bytes from the RX
buffer to osword_flag workspace.""")


d.subroutine(0x8C52, 'svc_9_help', title='Service 9: *HELP', description="""Handles MOS service call 9 (*HELP). First checks
for the credits Easter egg. For bare *HELP (CR
at text pointer), prints the version header and
full command list starting at table offset &C4.
For *HELP with an argument, handles '.' as a
shortcut to list all NFS commands, otherwise
iterates through help topics using PHA/PHA/RTS
dispatch to print matching command groups.
Returns with Y = ws_page (unclaimed).""")


d.subroutine(0x8B05, 'svc_18_fs_select', title='Service 18: filing system selection request', description="""Checks if Y=5 (Econet filing system number);
returns unclaimed if not. Also returns if bit 7
of &0D6C is already set, indicating the FS is
already selected. Otherwise falls through to
cmd_net_fs to perform the full network filing
system selection sequence.""", on_entry={'y': 'filing system number requested'})
d.entry(0x95B8)
d.entry(0x956A)
d.entry(0xAC86)
d.entry(0x9598)
d.entry(0x95A8)
d.entry(0x9DBC)
d.entry(0x9B83)
d.entry(0x9DE2)
d.entry(0xA1A9)
d.entry(0xA0FC)
d.entry(0xAD6E)
d.entry(0x8F80)
d.entry(0x929C)
d.entry(0xAF1E)
d.entry(0xA379)
d.entry(0xA383)
d.entry(0xA2DC)
d.entry(0xA2E2)
d.entry(0xA0CC)
d.entry(0xA0D2)
d.entry(0xA0E2)
d.comment(0xA3D8, """Star command table (4 interleaved sub-tables).
Each entry: ASCII name + flag byte (&80+) +
dispatch address word (PHA/PHA/RTS, addr-1).
Sub-tables separated by &80 sentinel bytes.
Flag byte: bit 7 = end of name marker,
bit 6 = set V on return if no argument,
bits 0-4 = *HELP syntax string index.
1: Utility cmds  2: NFS commands
3: Help topics  4: Copro/attributes""")

d.label(0xA3D8, 'cmd_table_fs')

d.label(0xA422, 'cmd_table_nfs')

d.label(0xA49A, 'cmd_table_help')

d.label(0xA4AB, 'cmd_table_copro')
d.string(0xA3D8, 1)
d.string(0xA3D9, 1)
d.string(0xA405, 2)
d.byte(0xA407)
d.string(0xA447, 2)
d.byte(0xA449)
d.string(0xA453, 2)
d.byte(0xA455)
d.entry(0xB97F)
d.entry(0xBA06)
d.entry(0x8B0E)
d.entry(0xB19F)
d.entry(0xB988)
d.entry(0xB2F0)
d.entry(0xAFCE)
d.entry(0xB985)
d.entry(0xB321)
d.entry(0x8ACC)
_cmd_entries = [(0xA3DE, 'cmd_close'), (0xA3E5, 'cmd_dump'), (0xA3EB, 'cmd_net_fs'), (0xA3F4, 'cmd_pollps'), (0xA3FC, 'cmd_print'), (0xA403, 'cmd_prot'), (0xA408, 'cmd_ps'), (0xA40F, 'cmd_roff'), (0xA416, 'cmd_type'), (0xA41F, 'cmd_unprot'), (0xA429, 'cmd_fs_operation'), (0xA42F, 'cmd_bye'), (0xA436, 'cmd_cdir'), (0xA43F, 'cmd_fs_operation'), (0xA445, 'cmd_dir'), (0xA44A, 'cmd_ex'), (0xA451, 'cmd_flip'), (0xA456, 'cmd_fs'), (0xA45D, 'cmd_fs_operation'), (0xA464, 'cmd_iam'), (0xA46B, 'cmd_lcat'), (0xA471, 'cmd_lex'), (0xA477, 'cmd_fs_operation'), (0xA47E, 'cmd_pass'), (0xA487, 'cmd_remove'), (0xA490, 'cmd_rename'), (0xA497, 'cmd_wipe'), (0xA4A0, 'help_net'), (0xA4A8, 'help_utils')]
for addr, target_label in _cmd_entries:
    d.word(addr)
    d.expr(addr, target_label + '-1')
d.comment(0xA3D8, '*Close (first char)', align=Align.INLINE)
d.comment(0xA3D9, '*Close cont (dispatch lo base)', align=Align.INLINE)
d.comment(0xA3DA, '*Close cont (dispatch hi base)', align=Align.INLINE)
d.comment(0xA3DD, 'No syntax', align=Align.INLINE)
d.comment(0xA3DE, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA3E0, '*Dump', align=Align.INLINE)
d.comment(0xA3E4, 'V no arg; syn 4: <filename> ...', align=Align.INLINE)
d.comment(0xA3E5, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA3E7, '*Net (select NFS)', align=Align.INLINE)
d.comment(0xA3EA, 'No syntax', align=Align.INLINE)
d.comment(0xA3EB, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA3ED, '*Pollps', align=Align.INLINE)
d.comment(0xA3F3, 'Syn 8: (<stn. id.>|<ps type>)', align=Align.INLINE)
d.comment(0xA3F4, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA3F6, '*Print', align=Align.INLINE)
d.comment(0xA3FB, 'V no arg; syn 12: <filename>', align=Align.INLINE)
d.comment(0xA3FC, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA3FE, '*Prot', align=Align.INLINE)
d.comment(0xA402, 'Syn 14: (attribute keywords)', align=Align.INLINE)
d.comment(0xA403, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA405, '*PS; syn 8: (<stn. id.>|<ps type>)', align=Align.INLINE)
d.comment(0xA408, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA40A, '*Roff', align=Align.INLINE)
d.comment(0xA40E, 'No syntax', align=Align.INLINE)
d.comment(0xA40F, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA411, '*Type', align=Align.INLINE)
d.comment(0xA415, 'V no arg; syn 12: <filename>', align=Align.INLINE)
d.comment(0xA416, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA418, '*Unprot', align=Align.INLINE)
d.comment(0xA41E, 'Syn 14: (attribute keywords)', align=Align.INLINE)
d.comment(0xA41F, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA421, 'End of utility sub-table', align=Align.INLINE)
d.comment(0xA422, '*Access', align=Align.INLINE)
d.comment(0xA428, 'V no arg; syn 9: <obj> (L)(W)(R)...', align=Align.INLINE)
d.comment(0xA429, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA42B, '*Bye', align=Align.INLINE)
d.comment(0xA42E, 'No syntax', align=Align.INLINE)
d.comment(0xA42F, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA431, '*Cdir', align=Align.INLINE)
d.comment(0xA435, 'V no arg; syn 6: <dir> (<number>)', align=Align.INLINE)
d.comment(0xA436, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA438, '*Delete', align=Align.INLINE)
d.comment(0xA43E, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA43F, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA441, '*Dir', align=Align.INLINE)
d.comment(0xA444, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA445, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA447, '*Ex; syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA44A, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA44C, '*Flip', align=Align.INLINE)
d.comment(0xA450, 'No syntax', align=Align.INLINE)
d.comment(0xA451, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA453, '*FS; syn 11: (<stn. id.>)', align=Align.INLINE)
d.comment(0xA456, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA458, '*Info', align=Align.INLINE)
d.comment(0xA45C, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA45D, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA45F, '*I am', align=Align.INLINE)
d.comment(0xA463, 'V no arg; syn 2: (<stn>) <user>...', align=Align.INLINE)
d.comment(0xA464, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA466, '*Lcat', align=Align.INLINE)
d.comment(0xA46A, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA46B, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA46D, '*Lex', align=Align.INLINE)
d.comment(0xA470, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA471, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA473, '*Lib', align=Align.INLINE)
d.comment(0xA476, 'V no arg; syn 5: <dir>', align=Align.INLINE)
d.comment(0xA477, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA479, '*Pass', align=Align.INLINE)
d.comment(0xA47D, 'V no arg; syn 7: <pass> ...', align=Align.INLINE)
d.comment(0xA47E, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA480, '*Remove', align=Align.INLINE)
d.comment(0xA486, 'V no arg; syn 3: <object>', align=Align.INLINE)
d.comment(0xA487, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA489, '*Rename', align=Align.INLINE)
d.comment(0xA48F, 'V no arg; syn 10: <file> <new file>', align=Align.INLINE)
d.comment(0xA490, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA492, '*Wipe', align=Align.INLINE)
d.comment(0xA496, 'Syn 1: (<dir>)', align=Align.INLINE)
d.comment(0xA497, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA499, 'End of NFS sub-table', align=Align.INLINE)
d.comment(0xA49A, '&09/&8E: before help-only entries', align=Align.INLINE)
d.comment(0xA49C, '*Net (local)', align=Align.INLINE)
d.comment(0xA49F, 'No syntax', align=Align.INLINE)
d.comment(0xA4A0, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA4A2, '*Utils', align=Align.INLINE)
d.comment(0xA4A7, 'No syntax', align=Align.INLINE)
d.comment(0xA4A8, 'Dispatch addr-1', align=Align.INLINE)
d.comment(0xA4AA, 'End of help topic sub-table', align=Align.INLINE)
d.comment(0xA4AB, """Protection attribute keyword table. Each entry:
ASCII name + flag byte (&80+) + OR mask + AND mask.
Used by *Prot (ORA lo byte) and *Unprot (AND hi
byte) to set/clear individual protection bits.
Also listed by *HELP Prot/*HELP Unprot via the
shared commands handler (syntax index 14).
Bits: 0=Peek 1=Poke 2=JSR 3=Proc 4=Utils 5=Halt""")
_attr_entries = [(0xA4AF, 0xA4B0, 0xA4B1), (0xA4B5, 0xA4B6, 0xA4B7), (0xA4BC, 0xA4BD, 0xA4BE), (0xA4C3, 0xA4C4, 0xA4C5), (0xA4CA, 0xA4CB, 0xA4CC), (0xA4D2, 0xA4D3, 0xA4D4)]
for flag_addr, or_addr, and_addr in _attr_entries:
    d.byte(flag_addr)
    d.byte(or_addr)
    d.byte(and_addr)
d.byte(0xA4D5)
d.comment(0xA4AB, 'Halt', align=Align.INLINE)
d.comment(0xA4AF, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4B0, '*Prot OR mask: bit 5', align=Align.INLINE)
d.comment(0xA4B1, '*Unprot AND mask: ~bit 5', align=Align.INLINE)
d.comment(0xA4B2, 'JSR', align=Align.INLINE)
d.comment(0xA4B5, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4B6, '*Prot OR mask: bit 2', align=Align.INLINE)
d.comment(0xA4B7, '*Unprot AND mask: ~bit 2', align=Align.INLINE)
d.comment(0xA4B8, 'Peek', align=Align.INLINE)
d.comment(0xA4BC, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4BD, '*Prot OR mask: bit 0', align=Align.INLINE)
d.comment(0xA4BE, '*Unprot AND mask: ~bit 0', align=Align.INLINE)
d.comment(0xA4BF, 'Poke', align=Align.INLINE)
d.comment(0xA4C3, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4C4, '*Prot OR mask: bit 1', align=Align.INLINE)
d.comment(0xA4C5, '*Unprot AND mask: ~bit 1', align=Align.INLINE)
d.comment(0xA4C6, 'Proc', align=Align.INLINE)
d.comment(0xA4CA, 'Flag &FC: V no arg, syn 28 (unused)', align=Align.INLINE)
d.comment(0xA4CB, '*Prot OR mask: bit 3', align=Align.INLINE)
d.comment(0xA4CC, '*Unprot AND mask: ~bit 3', align=Align.INLINE)
d.comment(0xA4CD, 'Utils', align=Align.INLINE)
d.comment(0xA4D2, 'Flag &A9: syn 9 (unused)', align=Align.INLINE)
d.comment(0xA4D3, '*Prot OR mask: bit 4', align=Align.INLINE)
d.comment(0xA4D4, '*Unprot AND mask: ~bit 4', align=Align.INLINE)
d.comment(0xA4D5, 'End of attribute keyword table', align=Align.INLINE)

d.label(0xB97F, 'cmd_close')

d.label(0xBA06, 'cmd_dump')

d.label(0x8B0E, 'cmd_net_fs')

d.label(0xB19F, 'cmd_pollps')

d.label(0xB988, 'cmd_print')

d.label(0xB2F0, 'cmd_prot')

d.label(0xAFCE, 'cmd_ps')

d.label(0xB985, 'cmd_type')

d.label(0xB321, 'cmd_unprot')

d.label(0x8ACC, 'cmd_roff')


d.subroutine(0xB97F, 'cmd_close', title='*Close command handler', description="""Loads A=0 and Y=0, then jumps to OSFIND to close
all open files on the current file server (equivalent
to CLOSE#0). Files open on other file servers are
not affected.""")


d.subroutine(0xBA06, 'cmd_dump', title='*Dump command handler', description="""Opens the file via open_file_for_read, allocates a
21-byte buffer on the stack, and parses the address
range via init_dump_buffer. Loops reading 16 bytes
per line, printing each as a 4-byte hex address,
16 hex bytes with spaces, and a 16-character ASCII
column (non-printable chars shown as '.'). Prints
a column header at every 256-byte boundary.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8B0E, 'cmd_net_fs', title='Select Econet network filing system', description="""Computes a checksum over the first &77 bytes of
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


d.subroutine(0xB19F, 'cmd_pollps', title='*Pollps command handler', description="""Initialises the spool drive, copies the PS name to
the TX buffer, and parses an optional station number
or PS name argument. Sends a poll request, then
prints the server address and name. Iterates through
PS slots, displaying each station's status as
'ready', 'busy' (with client station), or 'jammed'.
Marks processed slots with &3F.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB988, 'cmd_print', title='*Print command handler', description="""Sets V flag (distinguishing from *Type which clears V),
then opens the file for reading. Loops reading bytes
via OSBGET, checking for escape between each. In type
mode (V clear), normalises CR/LF pairs to single
newlines by tracking the previous character. In print
mode (V set), outputs all bytes raw via OSWRCH. Closes
the file and prints a final newline on EOF.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB2F0, 'cmd_prot', title='*Prot command handler', description="""With no arguments, sets all protection bits (&FF).
Otherwise parses attribute keywords via match_fs_cmd
with table offset &D3, accumulating bits via ORA.
Stores the final protection mask in ws_0d68 and
ws_0d69.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xAFCE, 'cmd_ps', title='*PS command handler', description="""Checks the printer server availability flag; raises
'Printer busy' if unavailable. Initialises the spool
drive and buffer pointer, then dispatches on argument
type: no argument branches to no_ps_name_given, a
leading digit branches to save_ps_cmd_ptr as a station
number, otherwise parses a named PS address via
load_ps_server_addr and parse_fs_ps_args.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB985, 'cmd_type', title='*Type command handler', description="""Clears V and branches to the shared open_and_read_file
entry in cmd_print. The V-clear state selects line-
ending normalisation mode: CR, LF, CR+LF, and LF+CR
are all treated as a single newline. Designed for
displaying text files.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xB321, 'cmd_unprot', title='*Unprot command handler', description="""With no arguments, clears all protection bits (EOR
yields 0). Otherwise parses attribute keywords, clearing
bits via AND with the complement. Shares the protection
mask storage path with cmd_prot. Falls through to
cmd_wipe.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8ACC, 'cmd_roff', title='*ROFF command handler', description="""Disables remote operation by clearing the flag at
offset 4 in the receive block. If remote operation
was active, re-enables the keyboard via OSBYTE &C9
(with X=0, Y=0) and calls tx_econet_abort with
A=&0A to reinitialise the workspace area. Falls
through to scan_remote_keys which clears svc_state
and nfs_workspace.""")
d.entry(0x92D2)
d.entry(0x948A)
d.entry(0xACFE)
d.entry(0x93C9)
d.entry(0xAD59)
d.entry(0xA33E)
d.entry(0xA063)
d.entry(0x8D6E)
d.entry(0xAD4D)
d.entry(0xAD53)
d.entry(0x8DB1)
d.entry(0xAF46)
d.entry(0x9377)
d.entry(0xB33D)

d.label(0x92D2, 'cmd_fs_operation')

d.label(0x948A, 'cmd_bye')

d.label(0xACFE, 'cmd_cdir')

d.label(0x93C9, 'cmd_dir')

d.label(0xAD59, 'cmd_ex')

d.label(0xA33E, 'cmd_flip')

d.label(0xA063, 'cmd_fs')

d.label(0x8D6E, 'cmd_iam')

d.label(0xAD4D, 'cmd_lcat')

d.label(0xAD53, 'cmd_lex')

d.label(0x8DB1, 'cmd_pass')

d.label(0xAF46, 'cmd_remove')

d.label(0x9377, 'cmd_rename')

d.label(0xB33D, 'cmd_wipe')


d.subroutine(0x92D2, 'cmd_fs_operation', title='Shared *Access/*Delete/*Info/*Lib command handler', description="""Copies the command name to the TX buffer, parses a
quoted filename argument via parse_quoted_arg, and
checks the access prefix. Validates the filename
does not start with '&', then falls through to
read_filename_char to copy remaining characters and
send the request. Raises 'Bad file name' if a bare
CR is found where a filename was expected.""")


d.subroutine(0x948A, 'cmd_bye', title='*Bye command handler', description="""Closes all open file control blocks via
process_all_fcbs, shuts down any *SPOOL/*EXEC files
with OSBYTE &77, and closes all network channels.
Falls through to save_net_tx_cb with function code
&17 to send the bye request to the file server.""")


d.subroutine(0xACFE, 'cmd_cdir', title='*CDir command handler', description="""Parses an optional allocation size argument: if absent,
defaults to index 2 (standard 19-entry directory, &200
bytes); if present, parses the decimal value and searches
a 26-entry threshold table to find the matching allocation
size index. Parses the directory name via parse_filename_arg,
copies it to the TX buffer, and sends FS command code &1B
to create the directory.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x93C9, 'cmd_dir', title='*Dir command handler', description="""Handles three argument syntaxes: a plain path
(delegates to pass_send_cmd), '&' alone for the root
directory, and '&N.dir' for cross-filesystem directory
changes. The cross-FS form sends a file server
selection command (code &12) to locate the target
server, raising 'Not found' on failure, then sends
the directory change (code 6) and calls
find_fs_and_exit to update the active FS context.""")


d.subroutine(0xAD59, 'cmd_ex', title='*Ex command handler', description="""Unified handler for *Ex, *LCat, and *LEx. Sets the
library flag from carry (CLC for current, SEC for library).
Configures column format: 1 entry per line for Ex
(command 3), 3 per column for Cat (command &0B). Sends the
examine request (code &12), then prints the directory
header: title, cycle number, Owner/Public label, option
name, Dir. and Lib. paths. Paginates through entries,
printing each via ex_print_col_sep until the server
returns zero entries.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA33E, 'cmd_flip', title='*Flip command handler', description="""Exchanges the CSD and CSL (library) handles.
Saves the current CSD handle (&0E03), loads the
library handle (&0E04) into Y, and calls
find_station_bit3 to install it as the new CSD.
Restores the original CSD handle and falls through
to flip_set_station_boot to install it as the new
library. Useful when files to be LOADed are in the
library and *DIR/*LIB would be inconvenient.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xA063, 'cmd_fs', title='*FS command handler', description="""Saves the current file server station address, then
checks for a command-line argument. With no argument,
falls through to print_current_fs to display the active
server. With an argument, parses the station number via
parse_fs_ps_args and issues OSWORD &13 (sub-function 1)
to select the new file server.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8D6E, 'cmd_iam', title='*I AM command handler (file server logon)', description="""Closes any *SPOOL/*EXEC files via OSBYTE &77,
resets all file control blocks via
process_all_fcbs, then parses the command line
for an optional station number and file server
address. If a station number is present, stores
it and calls clear_if_station_match to validate.
Copies the logon command template from
cmd_table_nfs_iam into the transmit buffer and
sends via copy_arg_validated. Falls through to
cmd_pass for password entry.""")


d.subroutine(0xAD4D, 'cmd_lcat', title='*LCat command handler', description="""Sets the library flag by rotating SEC into bit 7 of
l1071, then branches to cat_set_lib_flag inside cmd_ex
to catalogue the library directory with three entries
per column.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0xAD53, 'cmd_lex', title='*LEx command handler', description="""Sets the library flag by rotating SEC into bit 7 of
l1071, then branches to ex_set_lib_flag inside cmd_ex
to examine the library directory with one entry per line.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x8DB1, 'cmd_pass', title='*PASS command handler (change password)', description="""Builds the FS command packet via copy_arg_to_buf_x0,
then scans the reply buffer for a ':' separator
indicating a password prompt. If found, reads
characters from the keyboard without echo, handling
Delete (&7F) for backspace and NAK (&15) to restart
from the colon position. Sends the completed
password to the file server via save_net_tx_cb and
branches to send_cmd_and_dispatch for the reply.""")


d.subroutine(0xAF46, 'cmd_remove', title='*Remove command handler', description="""Like *Delete but suppresses the 'Not found' error,
making it suitable for use in programs where a missing
file should not cause an unexpected error. Validates
that exactly one argument is present — raises 'Syntax'
if extra arguments follow. Parses the filename via
parse_filename_arg, copies it to the TX buffer, and
sends FS command code &14 with the V flag set via BIT
for save_net_tx_cb_vset dispatch.""", on_entry={'y': 'command line offset in text pointer'})


d.subroutine(0x9377, 'cmd_rename', title='*Rename command handler', description="""Parses two space-separated filenames from the
command line, each with its own access prefix.
Sets the owner-only access mask before parsing each
name. Validates that both names resolve to the same
file server by comparing the FS options word —
raises 'Bad rename' if they differ. Falls through
to read_filename_char to copy the second filename
into the TX buffer and send the request.""")


d.subroutine(0xB33D, 'cmd_wipe', title='*Wipe command handler', description="""Masks owner access, parses a wildcard filename, and
loops sending examine requests to the file server.
Skips locked files and non-empty directories. Shows
each filename with a '(Y/N/?) ' prompt — '?' shows
full file info with a '(Y/N) ' reprompt, 'Y' builds
the delete command in the TX buffer. Falls through to
flush_and_read_char on completion.""", on_entry={'y': 'command line offset in text pointer'})
d.entry(0x8B8B)
d.entry(0x8B87)

d.label(0x8B8B, 'help_net')

d.label(0x8B87, 'help_utils')


d.subroutine(0x8B8B, 'help_net', title='*HELP NET topic handler', description="""Sets X to &4A (the NFS command sub-table offset)
and falls through to print_cmd_table to display
the NFS command list with version header.""")


d.subroutine(0x8B87, 'help_utils', title='*HELP UTILS topic handler', description="""Sets X=0 to select the utility command sub-table
and branches to print_cmd_table to display the
command list. Prints the version header followed
by all utility commands.""")
d.entry(0x8C28)
d.entry(0x92A1)
d.entry(0x9921)
d.entry(0x9BAF)
d.entry(0x9CC8)
d.entry(0x9E23)
d.entry(0x9F55)
d.entry(0xA8D0)
d.entry(0xA9D0)
d.entry(0xAADB)
d.entry(0xB7CF)
d.entry(0x8542)
for i in range(5):
    d.byte(0x8534 + i)
d.expr(0x8534, '<(tx_done_jsr-1)')
d.expr(0x8535, '<(tx_done_econet_event-1)')
d.expr(0x8536, '<(tx_done_os_proc-1)')
d.expr(0x8537, '<(tx_done_halt-1)')
d.expr(0x8538, '<(tx_done_continue-1)')
d.entry(0x867F)
for i in range(8):
    d.byte(0x8677 + i)
d.expr(0x8677, '<(tx_ctrl_peek-1)')
d.expr(0x8678, '<(tx_ctrl_poke-1)')
d.expr(0x8679, '<(proc_op_status2-1)')
d.expr(0x867A, '<(proc_op_status2-1)')
d.expr(0x867B, '<(proc_op_status2-1)')
d.expr(0x867C, '<(tx_ctrl_exit-1)')
d.expr(0x867D, '<(tx_ctrl_exit-1)')
d.expr(0x867E, '<(tx_ctrl_machine_type-1)')
for i in range(16):
    d.byte(0x88D8 + i)
for i in range(3):
    d.byte(0x89BD + i)
d.entry(0x84B1)
d.entry(0x84C1)
d.entry(0x88D8)
d.entry(0xA58B)
d.entry(0xA61C)
d.entry(0xA968)
d.entry(0xB850)
d.entry(0xB42F)
d.entry(0x0542)
d.entry(0x0564)
d.entry(0x05AB)
d.entry(0x05D3)


d.subroutine(0x8E4B, 'fs_vector_table', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by loop_set_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the extended vector table.

Bytes 14-33: handler address pairs read by write_vector_entry.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (write_vector_entry writes the current ROM
bank number instead). The last entry (FSCV) has no padding
byte.""")
for i, name in enumerate(['FILEV', 'ARGSV', 'BGETV', 'BPUTV', 'GBPBV', 'FINDV', 'FSCV']):
    addr = 0x8E4B + i * 2
    d.word(addr)
    d.comment(addr, f'{name} dispatch (&FF{0x1B + i * 3:02X})', align=Align.INLINE)
handler_names = [('FILEV', 0x9921), ('ARGSV', 0x9BAF), ('BGETV', 0xB7CF), ('BPUTV', 0xB850), ('GBPBV', 0x9E23), ('FINDV', 0x9D42), ('FSCV', 0x8E1D)]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x8E59 + i * 3
    d.word(base_addr)
    d.comment(base_addr, f'{name} handler (&{handler_addr:04X})', align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, '(ROM bank — not read)', align=Align.INLINE)

d.label(0x8E43, 'ps_template_data')
d.byte(0x8E49)
d.byte(0x8E4A)

d.label(0x8E74, 'netv_handler_addr')

d.label(0xA968, 'netv_handler')
d.word(0x8E74)
d.expr(0x8E74, 'netv_handler')

d.label(0x900D, 'syntax_strings')

d.label(0x97A4, 'error_msg_table')

d.label(0x97B1, 'msg_net_error')

d.label(0x97BC, 'msg_station')

d.label(0x97C5, 'msg_no_clock')

d.label(0x97CF, 'msg_escape')

d.label(0x97D7, 'msg_bad_option')

d.label(0x97E3, 'msg_no_reply')

d.label(0x97FA, 'msg_not_listening')

d.label(0x9809, 'msg_on_channel')

d.label(0x9815, 'msg_not_present')
d.byte(0x97A4)
d.byte(0x97B0)
d.byte(0x97B1)
d.byte(0x97BB)
d.byte(0x97BC)
d.byte(0x97C4)
d.byte(0x97C5)
d.byte(0x97CE)
d.byte(0x97CF)
d.byte(0x97D6)
d.byte(0x97D7)
d.byte(0x97E2)
d.byte(0x97E3)
d.byte(0x97F9)
d.byte(0x9808)
d.byte(0x9814)
d.byte(0x9821)

d.label(0x8C98, 'version_string')

d.label(0x8D2E, 'credits_string')
d.byte(0x8D2D)
d.comment(0x8D2D, 'CR', align=Align.INLINE)
d.byte(0x8D46)
d.comment(0x8D46, 'CR', align=Align.INLINE)
d.byte(0x8D51)
d.comment(0x8D51, 'CR', align=Align.INLINE)
d.byte(0x8D58)
d.comment(0x8D58, 'CR', align=Align.INLINE)
d.byte(0x8D64)
d.comment(0x8D64, 'CR', align=Align.INLINE)
d.byte(0x8D6C)
d.comment(0x8D6C, 'CR', align=Align.INLINE)
d.byte(0x8D6D)
d.comment(0x8D6D, 'String terminator', align=Align.INLINE)

d.label(0xA3B6, 'boot_load_cmd')

d.label(0xA3BF, 'boot_exec_cmd')


d.subroutine(0x8E33, 'svc_dispatch', title='PHA/PHA/RTS table dispatch', description="""Computes a target index by incrementing X and
decrementing Y until Y goes negative, effectively
calculating X+Y+1. Pushes the target address
(high then low byte) from svc_dispatch_lo/hi
tables onto the stack, loads fs_options into X,
then returns via RTS to dispatch to the target
subroutine. Used for all service dispatch, FS
command execution, and OSBYTE handler routing.""", on_entry={'x': 'base dispatch index', 'y': 'additional offset'}, on_exit={'x': 'fs_options value'})

d.label(0x8E33, 'svc_dispatch')


d.subroutine(0x8A97, 'read_paged_rom', title='Read next byte from paged ROM via OSRDSC', description="""Increments the read pointer at osrdsc_ptr (&F6)
first, then calls OSRDSC (&FFB9) with the ROM
number from error_block (&0100) in Y. Called
three times by service_handler during ROM
identification to read the copyright string and
ROM type byte.""", on_exit={'a': 'byte read from ROM'})

d.label(0x8A97, 'read_paged_rom')


d.subroutine(0x8E6D, 'osbyte_x0', title='OSBYTE wrapper with X=0, Y=&FF', description="""Sets X=0 and falls through to osbyte_yff to also
set Y=&FF. Provides a single call to execute
OSBYTE with A as the function code. Used by
adlc_init, init_adlc_and_vectors, and Econet
OSBYTE handling.""", on_entry={'a': 'OSBYTE function code'}, on_exit={'x': '0', 'y': '&FF'})


d.subroutine(0x8E6F, 'osbyte_yff', title='OSBYTE wrapper with Y=&FF', description="""Sets Y=&FF and JMPs to the MOS OSBYTE entry
point. X must already be set by the caller. The
osbyte_x0 entry point falls through to here after
setting X=0.""", on_entry={'a': 'OSBYTE function code', 'x': 'OSBYTE X parameter'}, on_exit={'y': '&FF'})

d.label(0x8E6D, 'osbyte_x0')

d.label(0x8E6F, 'osbyte_yff')


d.subroutine(0x9131, 'print_inline', title='Print inline string, high-bit terminated', description="""Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. Common terminators are
&EA (NOP) for fall-through and &B8 (CLV) followed by BVC for an
unconditional forward branch.""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})
d.comment(0x9131, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x9134, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x9139, 'Advance pointer to next character', align=Align.INLINE)
d.comment(0x913F, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x9141, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x9149, 'Reload character (pointer may have been clobbered)', align=Align.INLINE)
d.comment(0x914B, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x9157, 'Jump to address of high-bit byte (resumes code)', align=Align.INLINE)


d.subroutine(0x96BE, 'error_inline', title='Generate BRK error from inline string', description="""Pops the return address from the stack and copies the null-terminated
inline string into the error block at &0100. The error number is
passed in A. Never returns — triggers the error via JMP error_block.""", on_entry={'a': 'error number'})
d.comment(0x96BE, 'Save error number in Y', align=Align.INLINE)
d.comment(0x96BF, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x96C2, 'Pop return address (high)', align=Align.INLINE)


d.subroutine(0x96BB, 'error_inline_log', title='Generate BRK error from inline string (with logging)', description="""Like error_inline, but first conditionally logs the error code to
workspace via sub_c95fb before building the error block.""", on_entry={'a': 'error number'})
d.comment(0x96BB, 'Conditionally log error code to workspace', align=Align.INLINE)


d.subroutine(0x96A2, 'error_bad_inline', title="Generate 'Bad ...' BRK error from inline string", description="""Like error_inline, but prepends 'Bad ' to the error message. Copies
the prefix from a lookup table, then appends the null-terminated
inline string. The error number is passed in A. Never returns.""", on_entry={'a': 'error number'})
d.comment(0x96A2, 'Conditionally log error code to workspace', align=Align.INLINE)
d.comment(0x96A5, 'Save error number in Y', align=Align.INLINE)
d.comment(0x96A6, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x96A7, 'Store return address low', align=Align.INLINE)
d.comment(0x96A9, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x96AA, 'Store return address high', align=Align.INLINE)
d.comment(0x96AC, 'X=0: start of prefix string', align=Align.INLINE)
d.comment(0x96AE, "Copy 'Bad ' prefix from lookup table", align=Align.INLINE)
d.comment(0x96AF, 'Get next prefix character', align=Align.INLINE)
d.comment(0x96B2, 'Store in error text buffer', align=Align.INLINE)
d.comment(0x96B5, "Is it space (end of 'Bad ')?", align=Align.INLINE)
d.comment(0x96B7, 'No: copy next prefix character', align=Align.INLINE)
d.comment(0x96C7, 'Store error number in error block', align=Align.INLINE)
d.comment(0x96CE, 'Zero the BRK byte at &0100', align=Align.INLINE)
d.comment(0x96D1, 'Copy inline string into error block', align=Align.INLINE)
d.comment(0x96D3, 'Read next byte from inline string', align=Align.INLINE)
d.comment(0x96D8, 'Loop until null terminator', align=Align.INLINE)

d.label(0x969E, 'bad_prefix')
d.comment(0xACFE, 'Save command line offset', align=Align.INLINE)
d.comment(0xACFF, 'Push onto stack', align=Align.INLINE)
d.comment(0xAD00, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xAD03, 'Skip to optional size argument', align=Align.INLINE)
d.comment(0xAD06, 'End of line?', align=Align.INLINE)
d.comment(0xAD08, 'No: parse size argument', align=Align.INLINE)
d.comment(0xAD0A, 'Default allocation size index = 2', align=Align.INLINE)
d.comment(0xAD0E, 'A=&FF: mark as decimal parse', align=Align.INLINE)
d.comment(0xAD10, 'Store decimal parse flag', align=Align.INLINE)
d.comment(0xAD12, 'Parse numeric size argument', align=Align.INLINE)
d.comment(0xAD15, 'X=&1B: top of 26-entry size table', align=Align.INLINE)
d.comment(0xAD17, 'Try next lower index', align=Align.INLINE)
d.comment(0xAD18, 'Compare size with threshold', align=Align.INLINE)
d.comment(0xAD1B, 'A < threshold: keep searching', align=Align.INLINE)
d.comment(0xAD1D, 'Store allocation size index', align=Align.INLINE)
d.comment(0xAD20, 'Restore command line offset', align=Align.INLINE)
d.comment(0xAD21, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAD22, 'Save text pointer for filename parse', align=Align.INLINE)
d.comment(0xAD25, 'Parse directory name argument', align=Align.INLINE)
d.comment(0xAD28, 'X=1: one argument to copy', align=Align.INLINE)
d.comment(0xAD2A, 'Copy directory name to TX buffer', align=Align.INLINE)
d.comment(0xAD2D, 'Y=&1B: *CDir FS command code', align=Align.INLINE)
d.comment(0xAD2F, 'Send command to file server', align=Align.INLINE)
d.comment(0xAD32, """*CDir allocation size threshold table

26 thresholds dividing 0-255 into size classes.
Table base overlaps with the JMP high byte at
cdir_dispatch_col+2 (entry 0 = &94, never reached). Searched
from index 26 down to 0; the result index (1-26)
is stored as the directory allocation size class.
Default when no size argument given: index 2.""")
d.comment(0xAD32, 'Index 1: threshold 0 (catch-all)', align=Align.INLINE)
d.comment(0xAD33, 'Index 2: threshold 10 (default)', align=Align.INLINE)
d.comment(0xAD34, 'Index 3: threshold 20', align=Align.INLINE)
d.comment(0xAD35, 'Index 4: threshold 29', align=Align.INLINE)
d.comment(0xAD36, 'Index 5: threshold 39', align=Align.INLINE)
d.comment(0xAD37, 'Index 6: threshold 49', align=Align.INLINE)
d.comment(0xAD38, 'Index 7: threshold 59', align=Align.INLINE)
d.comment(0xAD39, 'Index 8: threshold 69', align=Align.INLINE)
d.comment(0xAD3A, 'Index 9: threshold 79', align=Align.INLINE)
d.comment(0xAD3B, 'Index 10: threshold 88', align=Align.INLINE)
d.comment(0xAD3C, 'Index 11: threshold 98', align=Align.INLINE)
d.comment(0xAD3D, 'Index 12: threshold 108', align=Align.INLINE)
d.comment(0xAD3E, 'Index 13: threshold 118', align=Align.INLINE)
d.comment(0xAD3F, 'Index 14: threshold 128', align=Align.INLINE)
d.comment(0xAD40, 'Index 15: threshold 138', align=Align.INLINE)
d.comment(0xAD41, 'Index 16: threshold 148', align=Align.INLINE)
d.comment(0xAD42, 'Index 17: threshold 157', align=Align.INLINE)
d.comment(0xAD43, 'Index 18: threshold 167', align=Align.INLINE)
d.comment(0xAD44, 'Index 19: threshold 177', align=Align.INLINE)
d.comment(0xAD45, 'Index 20: threshold 187', align=Align.INLINE)
d.comment(0xAD46, 'Index 21: threshold 197', align=Align.INLINE)
d.comment(0xAD47, 'Index 22: threshold 207', align=Align.INLINE)
d.comment(0xAD48, 'Index 23: threshold 216', align=Align.INLINE)
d.comment(0xAD49, 'Index 24: threshold 226', align=Align.INLINE)
d.comment(0xAD4A, 'Index 25: threshold 236', align=Align.INLINE)
d.comment(0xAD4B, 'Index 26: threshold 246', align=Align.INLINE)
d.comment(0xAD4C, 'Unused (index 27, never accessed)', align=Align.INLINE)
d.comment(0xAD4D, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD50, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xAD53, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD56, 'Set carry (= library directory)', align=Align.INLINE)
d.comment(0xB2F0, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB2F2, 'Compare with CR (end of line)', align=Align.INLINE)
d.comment(0xB2F4, 'Not CR: attribute keywords follow', align=Align.INLINE)
d.comment(0xB2F6, 'A=&FF: protect all attributes', align=Align.INLINE)
d.comment(0xB2FA, 'Load current protection mask', align=Align.INLINE)
d.comment(0xB2FD, 'Save as starting value', align=Align.INLINE)
d.comment(0xB2FE, 'X=&D3: attribute keyword table offset', align=Align.INLINE)
d.comment(0xB300, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB302, 'Save for end-of-args check', align=Align.INLINE)
d.comment(0xB304, 'Match attribute keyword in table', align=Align.INLINE)
d.comment(0xB307, 'No match: check if end of arguments', align=Align.INLINE)
d.comment(0xB309, 'Retrieve accumulated mask', align=Align.INLINE)
d.comment(0xB30A, 'OR in attribute bit for keyword', align=Align.INLINE)
d.comment(0xB30D, 'Save updated mask', align=Align.INLINE)
d.comment(0xB30E, 'Always non-zero after ORA: loop', align=Align.INLINE)
d.comment(0xB310, 'Get the unmatched character', align=Align.INLINE)
d.comment(0xB312, 'Is it CR?', align=Align.INLINE)
d.comment(0xB314, 'Yes: arguments ended correctly', align=Align.INLINE)
d.comment(0xB316, 'No: invalid attribute keyword', align=Align.INLINE)
d.comment(0xB319, 'Retrieve final protection mask', align=Align.INLINE)
d.comment(0xB31A, 'Store protection mask', align=Align.INLINE)
d.comment(0xB31D, 'Store protection mask copy', align=Align.INLINE)
d.comment(0xB320, 'Return', align=Align.INLINE)
d.comment(0xB321, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB323, 'Compare with CR (end of line)', align=Align.INLINE)
d.comment(0xB325, 'No args: A=0 clears all protection', align=Align.INLINE)
d.comment(0xB327, 'Load current protection mask', align=Align.INLINE)
d.comment(0xB32A, 'Save as starting value', align=Align.INLINE)
d.comment(0xB32B, 'X=&D3: attribute keyword table offset', align=Align.INLINE)
d.comment(0xB32D, 'Get next char from command line', align=Align.INLINE)
d.comment(0xB32F, 'Save for end-of-args check', align=Align.INLINE)
d.comment(0xB331, 'Match attribute keyword in table', align=Align.INLINE)
d.comment(0xB334, 'No match: check if end of arguments', align=Align.INLINE)
d.comment(0xB336, 'Retrieve accumulated mask', align=Align.INLINE)
d.comment(0xB337, 'AND to clear matched attribute bit', align=Align.INLINE)
d.comment(0xB33A, 'Save updated mask', align=Align.INLINE)
d.comment(0x92D2, 'Copy command name to TX buffer', align=Align.INLINE)
d.comment(0x92D5, 'Save buffer position', align=Align.INLINE)
d.comment(0x92D6, 'Push it', align=Align.INLINE)
d.comment(0x92D7, 'Parse filename (handles quoting)', align=Align.INLINE)
d.comment(0x92DA, 'Parse owner/public access prefix', align=Align.INLINE)
d.comment(0x92DD, 'Restore buffer position', align=Align.INLINE)
d.comment(0x92DE, 'Transfer to X', align=Align.INLINE)
d.comment(0x92DF, "Reject '&' character in filename", align=Align.INLINE)
d.comment(0x92E2, 'End of line?', align=Align.INLINE)
d.comment(0x92E4, 'No: copy filename chars to buffer', align=Align.INLINE)
d.comment(0x92E6, 'Error number &CC', align=Align.INLINE)
d.comment(0x92E8, "Raise 'Bad file name' error", align=Align.INLINE)
d.comment(0x92F5, 'Load first parsed character', align=Align.INLINE)
d.comment(0x92F8, "Is it '&'?", align=Align.INLINE)
d.comment(0x92FA, 'Yes: invalid filename', align=Align.INLINE)
d.comment(0x92FC, 'Return', align=Align.INLINE)
d.comment(0x92FD, "Reject '&' in current char", align=Align.INLINE)
d.comment(0x9300, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x9303, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9304, 'End of line?', align=Align.INLINE)
d.comment(0x9306, 'Yes: send request to file server', align=Align.INLINE)
d.comment(0x9308, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x930B, 'Continue reading filename chars', align=Align.INLINE)
d.comment(0x930E, 'Y=0: no extra dispatch offset', align=Align.INLINE)
d.comment(0x9310, 'Send command and dispatch reply', align=Align.INLINE)
d.comment(0x9313, 'Save command line offset', align=Align.INLINE)
d.comment(0x9314, 'Push it', align=Align.INLINE)
d.comment(0x9315, 'Scan backwards in command table', align=Align.INLINE)
d.comment(0x9316, 'Load table byte', align=Align.INLINE)
d.comment(0x9319, 'Bit 7 clear: keep scanning', align=Align.INLINE)
d.comment(0x931B, 'Point past flag byte to name start', align=Align.INLINE)
d.comment(0x931C, 'Y=0: TX buffer offset', align=Align.INLINE)
d.comment(0x931E, 'Load command name character', align=Align.INLINE)
d.comment(0x9321, 'Bit 7 set: end of name', align=Align.INLINE)
d.comment(0x9323, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x9326, 'Advance table pointer', align=Align.INLINE)
d.comment(0x9327, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9328, 'Continue copying name', align=Align.INLINE)
d.comment(0x932A, 'Space separator', align=Align.INLINE)
d.comment(0x932C, 'Append space after command name', align=Align.INLINE)
d.comment(0x932F, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9330, 'Transfer length to A', align=Align.INLINE)
d.comment(0x9331, 'And to X (buffer position)', align=Align.INLINE)
d.comment(0x9332, 'Restore command line offset', align=Align.INLINE)
d.comment(0x9333, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9334, 'Return', align=Align.INLINE)
d.comment(0x9335, 'A=0: no quote mode', align=Align.INLINE)
d.comment(0x9338, 'Clear quote tracking flag', align=Align.INLINE)
d.comment(0x933B, 'Load char from command line', align=Align.INLINE)
d.comment(0x933D, 'Space?', align=Align.INLINE)
d.comment(0x933F, 'No: check for opening quote', align=Align.INLINE)
d.comment(0x9341, 'Skip leading space', align=Align.INLINE)
d.comment(0x9342, 'Continue skipping spaces', align=Align.INLINE)
d.comment(0x9344, 'Double-quote character?', align=Align.INLINE)
d.comment(0x9346, 'No: start reading filename', align=Align.INLINE)
d.comment(0x9348, 'Skip opening quote', align=Align.INLINE)
d.comment(0x9349, 'Toggle quote mode flag', align=Align.INLINE)
d.comment(0x934C, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x934F, 'Load char from command line', align=Align.INLINE)
d.comment(0x9351, 'Double-quote?', align=Align.INLINE)
d.comment(0x9353, 'No: store character as-is', align=Align.INLINE)
d.comment(0x9355, 'Toggle quote mode', align=Align.INLINE)
d.comment(0x9358, 'Store updated quote mode', align=Align.INLINE)
d.comment(0x935B, 'Replace closing quote with space', align=Align.INLINE)
d.comment(0x935D, 'Store character in parse buffer', align=Align.INLINE)
d.comment(0x9360, 'Advance command line pointer', align=Align.INLINE)
d.comment(0x9361, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9362, 'End of line?', align=Align.INLINE)
d.comment(0x9364, 'No: continue parsing', align=Align.INLINE)
d.comment(0x9366, 'Check quote balance flag', align=Align.INLINE)
d.comment(0x9369, 'Balanced: return OK', align=Align.INLINE)
d.comment(0x936B, 'Unbalanced: use BRK ptr for error', align=Align.INLINE)
d.comment(0x936D, "Raise 'Bad string' error", align=Align.INLINE)
d.comment(0x9377, "Copy 'Rename ' to TX buffer", align=Align.INLINE)
d.comment(0x937A, 'Save buffer position', align=Align.INLINE)
d.comment(0x937B, 'Push it', align=Align.INLINE)
d.comment(0x937C, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x937F, 'Parse first filename (quoted)', align=Align.INLINE)
d.comment(0x9382, 'Parse access prefix', align=Align.INLINE)
d.comment(0x9385, 'Restore buffer position', align=Align.INLINE)
d.comment(0x9386, 'Transfer to X', align=Align.INLINE)
d.comment(0x9387, 'Load next parsed character', align=Align.INLINE)
d.comment(0x938A, 'End of line?', align=Align.INLINE)
d.comment(0x938C, 'No: store character', align=Align.INLINE)
d.comment(0x938E, 'Error number &B0', align=Align.INLINE)
d.comment(0x9390, "Raise 'Bad rename' error", align=Align.INLINE)
d.comment(0x939A, 'Store character in TX buffer', align=Align.INLINE)
d.comment(0x939D, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x939E, 'Space (name separator)?', align=Align.INLINE)
d.comment(0x93A0, 'Yes: first name complete', align=Align.INLINE)
d.comment(0x93A2, 'Strip BASIC token prefix byte', align=Align.INLINE)
d.comment(0x93A5, 'Continue copying first filename', align=Align.INLINE)
d.comment(0x93A8, 'Strip token from next char', align=Align.INLINE)
d.comment(0x93AB, 'Load next parsed character', align=Align.INLINE)
d.comment(0x93AE, 'Still a space?', align=Align.INLINE)
d.comment(0x93B0, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0x93B2, 'Save current FS options', align=Align.INLINE)
d.comment(0x93B5, 'Push them', align=Align.INLINE)
d.comment(0x93B6, 'Reset access mask for second name', align=Align.INLINE)
d.comment(0x93B9, 'Save buffer position', align=Align.INLINE)
d.comment(0x93BA, 'Push it', align=Align.INLINE)
d.comment(0x93BB, 'Parse access prefix for second name', align=Align.INLINE)
d.comment(0x93BE, 'Restore buffer position', align=Align.INLINE)
d.comment(0x93BF, 'Transfer to X', align=Align.INLINE)
d.comment(0x93C0, 'Restore original FS options', align=Align.INLINE)
d.comment(0x93C1, 'Options changed (cross-FS)?', align=Align.INLINE)
d.comment(0x93C4, "Yes: error (can't rename across FS)", align=Align.INLINE)
d.comment(0x93C6, 'Copy second filename and send', align=Align.INLINE)
d.comment(0x93C9, 'Get first char of argument', align=Align.INLINE)
d.comment(0x93CB, "Is it '&' (FS selector prefix)?", align=Align.INLINE)
d.comment(0x93CD, 'No: simple dir change', align=Align.INLINE)
d.comment(0x93CF, "Skip '&'", align=Align.INLINE)
d.comment(0x93D0, "Get char after '&'", align=Align.INLINE)
d.comment(0x93D2, 'End of line?', align=Align.INLINE)
d.comment(0x93D4, "Yes: '&' alone (root directory)", align=Align.INLINE)
d.comment(0x93D6, 'Space?', align=Align.INLINE)
d.comment(0x93D8, "No: check for '.' separator", align=Align.INLINE)
d.comment(0x93DA, 'Y=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0x93DC, 'Advance index', align=Align.INLINE)
d.comment(0x93DD, 'Load char from command line', align=Align.INLINE)
d.comment(0x93DF, 'Copy to TX buffer', align=Align.INLINE)
d.comment(0x93E2, "Is it '&' (end of FS path)?", align=Align.INLINE)
d.comment(0x93E4, 'No: keep copying', align=Align.INLINE)
d.comment(0x93E6, "Replace '&' with CR terminator", align=Align.INLINE)
d.comment(0x93E8, 'Store CR in buffer', align=Align.INLINE)
d.comment(0x93EB, 'Point past CR', align=Align.INLINE)
d.comment(0x93EC, 'Transfer length to A', align=Align.INLINE)
d.comment(0x93ED, 'And to X (byte count)', align=Align.INLINE)
d.comment(0x93EE, 'Send directory request to server', align=Align.INLINE)
d.comment(0x93F1, "Is char after '&' a dot?", align=Align.INLINE)
d.comment(0x93F3, 'Yes: &FS.dir format', align=Align.INLINE)
d.comment(0x93F5, 'No: invalid syntax', align=Align.INLINE)
d.comment(0x93F8, "Skip '.'", align=Align.INLINE)
d.comment(0x93F9, 'Save dir path start position', align=Align.INLINE)
d.comment(0x93FB, 'FS command 4: examine directory', align=Align.INLINE)
d.comment(0x93FD, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x9400, 'Load FS flags', align=Align.INLINE)
d.comment(0x9403, 'Set bit 6 (FS selection active)', align=Align.INLINE)
d.comment(0x9405, 'Store updated flags', align=Align.INLINE)
d.comment(0x9408, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x940A, 'Copy FS number to buffer', align=Align.INLINE)
d.comment(0x940D, 'Y=&12: select FS command code', align=Align.INLINE)
d.comment(0x940F, 'Send FS selection command', align=Align.INLINE)
d.comment(0x9412, 'Load reply status', align=Align.INLINE)
d.comment(0x9415, 'Status 2 (found)?', align=Align.INLINE)
d.comment(0x9417, 'Yes: proceed to dir change', align=Align.INLINE)
d.comment(0x9419, 'Error number &D6', align=Align.INLINE)
d.comment(0x941B, "Raise 'Not found' error", align=Align.INLINE)
d.comment(0x9428, 'Load current FS station byte', align=Align.INLINE)
d.comment(0x942B, 'Store in TX buffer', align=Align.INLINE)
d.comment(0x942E, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9430, 'Y=7: change directory command code', align=Align.INLINE)
d.comment(0x9432, 'Send directory change request', align=Align.INLINE)
d.comment(0x9435, 'X=1', align=Align.INLINE)
d.comment(0x9437, 'Store start marker in buffer', align=Align.INLINE)
d.comment(0x943A, 'Store start marker in buffer+1', align=Align.INLINE)
d.comment(0x943E, 'Restore dir path start position', align=Align.INLINE)
d.comment(0x9440, 'Copy directory path to buffer', align=Align.INLINE)
d.comment(0x9443, 'Y=6: set directory command code', align=Align.INLINE)
d.comment(0x9445, 'Send set directory command', align=Align.INLINE)
d.comment(0x9448, 'Load reply handle', align=Align.INLINE)
d.comment(0x944B, 'Select FS and return', align=Align.INLINE)
d.comment(0x944E, 'Simple: pass command to FS', align=Align.INLINE)
d.comment(0x9451, 'A=&90: bye command port', align=Align.INLINE)
d.comment(0x9453, 'Initialise TXCB from template', align=Align.INLINE)
d.comment(0x9456, 'Set transmit port', align=Align.INLINE)
d.comment(0x9458, 'A=3: data start offset', align=Align.INLINE)
d.comment(0x945A, 'Set TXCB start offset', align=Align.INLINE)
d.comment(0x945C, 'Open receive: &80->&7F (bit 7 clear = awaiting reply)', align=Align.INLINE)
d.comment(0x945E, 'Return', align=Align.INLINE)
d.comment(0x945F, 'Save A', align=Align.INLINE)
d.comment(0x9460, 'Y=&0B: template size - 1', align=Align.INLINE)
d.comment(0x9462, 'Load byte from TXCB template', align=Align.INLINE)
d.comment(0x9465, 'Store to TXCB workspace', align=Align.INLINE)
d.comment(0x9468, 'Index >= 2?', align=Align.INLINE)
d.comment(0x946A, 'Yes: skip dest station copy', align=Align.INLINE)
d.comment(0x946C, 'Load dest station byte', align=Align.INLINE)
d.comment(0x946F, 'Store to TXCB destination', align=Align.INLINE)
d.comment(0x9472, 'Decrement index', align=Align.INLINE)
d.comment(0x9473, 'More bytes: continue', align=Align.INLINE)
d.comment(0x9475, 'Restore A', align=Align.INLINE)
d.comment(0x9476, 'Return', align=Align.INLINE)
d.comment(0x9483, 'Save A', align=Align.INLINE)
d.comment(0x9484, 'Set carry (read-only mode)', align=Align.INLINE)
d.comment(0x9487, 'Clear V', align=Align.INLINE)
d.comment(0xA33E, 'Load current CSD handle', align=Align.INLINE)
d.comment(0xA341, 'Save CSD handle', align=Align.INLINE)
d.comment(0xA342, 'Load library handle into Y', align=Align.INLINE)
d.comment(0xA345, 'Install library as new CSD', align=Align.INLINE)
d.comment(0xA348, 'Restore original CSD handle', align=Align.INLINE)
d.comment(0xA349, 'Y = original CSD (becomes library)', align=Align.INLINE)
d.comment(0xA34A, 'X=&10: max 16 station entries', align=Align.INLINE)
d.comment(0xA34C, 'Clear V (no match found yet)', align=Align.INLINE)
d.comment(0xA34D, 'Decrement station index', align=Align.INLINE)
d.comment(0xA34E, 'All searched: exit loop', align=Align.INLINE)
d.comment(0xA350, 'Check if station[X] matches', align=Align.INLINE)
d.comment(0xA353, 'No match: try next station', align=Align.INLINE)
d.comment(0xA355, 'Load station flags byte', align=Align.INLINE)
d.comment(0xA358, 'Test bit 4 (active flag)', align=Align.INLINE)
d.comment(0xA35A, 'Not active: try next station', align=Align.INLINE)
d.comment(0xA35C, 'Transfer boot type to A', align=Align.INLINE)
d.comment(0xA35D, 'Store boot setting for station', align=Align.INLINE)
d.comment(0xA360, 'Set V flag (station match found)', align=Align.INLINE)
d.comment(0xA363, 'Store boot type', align=Align.INLINE)
d.comment(0xA366, 'V set (matched): skip allocation', align=Align.INLINE)
d.comment(0xA368, 'Boot type to A', align=Align.INLINE)
d.comment(0xA369, 'Allocate FCB slot for new entry', align=Align.INLINE)
d.comment(0xA36C, 'Store allocation result', align=Align.INLINE)
d.comment(0xA36F, 'Zero: allocation failed, exit', align=Align.INLINE)
d.comment(0xA371, 'A=&32: station flags (active+boot)', align=Align.INLINE)
d.comment(0xA373, 'Store station flags', align=Align.INLINE)
d.comment(0xA376, 'Restore FS context and return', align=Align.INLINE)
d.comment(0xA379, 'Close all network channels', align=Align.INLINE)
d.comment(0xA37C, 'Set carry flag', align=Align.INLINE)
d.comment(0xA37D, 'Load reply boot type', align=Align.INLINE)
d.comment(0xA380, 'Store as current boot type', align=Align.INLINE)
d.comment(0xA383, 'Save processor status', align=Align.INLINE)
d.comment(0xA384, 'Load station number from reply', align=Align.INLINE)
d.comment(0xA387, 'Find station entry with bit 2', align=Align.INLINE)
d.comment(0xA38A, 'Load network number from reply', align=Align.INLINE)
d.comment(0xA38D, 'Find station entry with bit 3', align=Align.INLINE)
d.comment(0xA390, 'Load boot type from reply', align=Align.INLINE)
d.comment(0xA393, 'Set boot config for station', align=Align.INLINE)
d.comment(0xA396, 'Restore processor status', align=Align.INLINE)
d.comment(0xA397, 'Carry set: proceed with boot', align=Align.INLINE)
d.comment(0xA399, 'Return with last flag', align=Align.INLINE)
d.comment(0xA39C, 'Load config flags', align=Align.INLINE)
d.comment(0xA39F, 'Save copy in X', align=Align.INLINE)
d.comment(0xA3A0, 'Test bit 2 (auto-boot flag)', align=Align.INLINE)
d.comment(0xA3A2, 'Save bit 2 test result', align=Align.INLINE)
d.comment(0xA3A3, 'Restore full flags', align=Align.INLINE)
d.comment(0xA3A4, 'Clear bit 2 (consume flag)', align=Align.INLINE)
d.comment(0xA3A6, 'Store cleared flags', align=Align.INLINE)
d.comment(0xA3A9, 'Restore bit 2 test result', align=Align.INLINE)
d.comment(0xA3AA, 'Bit 2 was set: skip to boot cmd', align=Align.INLINE)
d.comment(0xA3AC, 'OSBYTE &79: scan keyboard', align=Align.INLINE)
d.comment(0xA3B4, 'CTRL not pressed: proceed to boot', align=Align.INLINE)
d.comment(0xA3B6, 'CTRL pressed: cancel boot, return', align=Align.INLINE)
d.comment(0xA3C7, """Boot option OSCLI address table

Low bytes of boot command string addresses,
all in page &A3. Indexed by boot option 0-3
(option 0 is never reached due to BEQ).
Entry 2 reuses the tail of 'L.!BOOT' to
get '!BOOT' (*RUN equivalent).""")
d.comment(0xA3C7, "Opt 0: &A3C6 (don't-care, unused)", align=Align.INLINE)
d.comment(0xA3C8, "Opt 1: &A3B7 'L.!BOOT' (*LOAD)", align=Align.INLINE)
d.comment(0xA3C9, "Opt 2: &A3B9 '!BOOT' (*RUN)", align=Align.INLINE)
d.comment(0xA3CA, "Opt 3: &A3BF 'E.!BOOT' (*EXEC)", align=Align.INLINE)
d.comment(0xA3CB, 'Load boot type', align=Align.INLINE)
d.comment(0xA3CE, 'Type 0: no command, just return', align=Align.INLINE)
d.comment(0xA3D0, 'Look up boot command address low', align=Align.INLINE)
d.comment(0xA3D3, 'Boot command address high (&A3xx)', align=Align.INLINE)
d.comment(0xA3D5, 'Execute boot command via OSCLI', align=Align.INLINE)
d.comment(0xAF46, 'Save command line offset', align=Align.INLINE)
d.comment(0xAF47, 'Push onto stack', align=Align.INLINE)
d.comment(0xAF48, 'Skip to check for extra arguments', align=Align.INLINE)
d.comment(0xAF4B, 'End of line?', align=Align.INLINE)
d.comment(0xAF4D, 'Yes: single arg, proceed', align=Align.INLINE)
d.comment(0xAF4F, 'No: extra args, syntax error', align=Align.INLINE)
d.comment(0xAF52, 'Restore command line offset', align=Align.INLINE)
d.comment(0xAF53, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAF54, 'Save text pointer for parsing', align=Align.INLINE)
d.comment(0xAF57, 'Parse filename argument', align=Align.INLINE)
d.comment(0xAF5A, 'Copy filename to TX buffer', align=Align.INLINE)
d.comment(0xAF5D, 'Y=&14: *Delete FS command code', align=Align.INLINE)
d.comment(0xAF5F, 'Set V flag (via BIT #&FF)', align=Align.INLINE)
d.comment(0xAF62, 'Send to FS with V-flag dispatch', align=Align.INLINE)
d.comment(0xAF65, 'Set V (suppress leading zeros)', align=Align.INLINE)
d.comment(0xAF68, 'Transfer value to Y (remainder)', align=Align.INLINE)
d.comment(0xAF69, 'A=100: hundreds divisor', align=Align.INLINE)
d.comment(0xAF6B, 'Print hundreds digit', align=Align.INLINE)
d.comment(0xAF6E, 'A=10: tens divisor', align=Align.INLINE)
d.comment(0xAF70, 'Print tens digit', align=Align.INLINE)
d.comment(0xAF73, 'Clear V (always print units)', align=Align.INLINE)
d.comment(0xAF74, 'A=1: units divisor', align=Align.INLINE)
d.comment(0xAF76, 'Store divisor', align=Align.INLINE)
d.comment(0xAF78, 'Get remaining value', align=Align.INLINE)
d.comment(0xAF79, "X='0'-1: digit counter", align=Align.INLINE)
d.comment(0xAF7B, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xAF7C, 'Save V flag for leading zero check', align=Align.INLINE)
d.comment(0xAF7D, 'Count quotient digit', align=Align.INLINE)
d.comment(0xAF7E, 'Subtract divisor', align=Align.INLINE)
d.comment(0xAF80, 'No underflow: continue dividing', align=Align.INLINE)
d.comment(0xAF82, 'Add back divisor (get remainder)', align=Align.INLINE)
d.comment(0xAF84, 'Remainder to Y for next digit', align=Align.INLINE)
d.comment(0xAF85, 'Digit character to A', align=Align.INLINE)
d.comment(0xAF86, 'Restore V flag', align=Align.INLINE)
d.comment(0xAF87, 'V clear: always print digit', align=Align.INLINE)
d.comment(0xAF89, "V set: is digit '0'?", align=Align.INLINE)
d.comment(0xAF8B, 'Yes: suppress leading zero', align=Align.INLINE)
d.comment(0xAF8D, 'Save divisor across OSASCI call', align=Align.INLINE)
d.comment(0xAF92, 'Restore divisor', align=Align.INLINE)
d.comment(0xAF94, 'Return', align=Align.INLINE)
d.comment(0xAF95, 'Save A', align=Align.INLINE)
d.comment(0xAF96, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xAF98, 'To OS text pointer low', align=Align.INLINE)
d.comment(0xAF9A, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xAF9C, 'To OS text pointer high', align=Align.INLINE)
d.comment(0xAF9E, 'Restore A', align=Align.INLINE)
d.comment(0xAF9F, 'Return', align=Align.INLINE)
d.comment(0xAFA0, 'Advance past current character', align=Align.INLINE)
d.comment(0xAFA1, 'Load char from command line', align=Align.INLINE)
d.comment(0xAFA3, 'Space?', align=Align.INLINE)
d.comment(0xAFA5, 'Yes: skip trailing spaces', align=Align.INLINE)
d.comment(0xAFA7, 'CR (end of line)?', align=Align.INLINE)
d.comment(0xAFA9, 'Yes: return (at end)', align=Align.INLINE)
d.comment(0xAFAD, 'Advance past space', align=Align.INLINE)
d.comment(0xAFAE, 'Load next character', align=Align.INLINE)
d.comment(0xAFB0, 'Still a space?', align=Align.INLINE)
d.comment(0xAFB2, 'Yes: skip multiple spaces', align=Align.INLINE)
d.comment(0xAFB4, 'Return (at next argument)', align=Align.INLINE)
d.comment(0xAFB5, 'Save A', align=Align.INLINE)
d.comment(0xAFB6, 'Copy text pointer low byte', align=Align.INLINE)
d.comment(0xAFB8, 'To spool buffer pointer low', align=Align.INLINE)
d.comment(0xAFBA, 'Copy text pointer high byte', align=Align.INLINE)
d.comment(0xAFBC, 'To spool buffer pointer high', align=Align.INLINE)
d.comment(0xAFBE, 'Restore A', align=Align.INLINE)
d.comment(0xAFBF, 'Return', align=Align.INLINE)
d.comment(0xAFC0, 'Save Y', align=Align.INLINE)
d.comment(0xAFC1, 'Push it', align=Align.INLINE)
d.comment(0xAFC2, 'Get workspace page number', align=Align.INLINE)
d.comment(0xAFC5, 'Store as spool drive page high', align=Align.INLINE)
d.comment(0xAFC7, 'Restore Y', align=Align.INLINE)
d.comment(0xAFC8, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAFC9, 'A=0', align=Align.INLINE)
d.comment(0xAFCB, 'Clear spool drive page low', align=Align.INLINE)
d.comment(0xAFCD, 'Return', align=Align.INLINE)
d.comment(0xB97F, 'A=0: close all open files', align=Align.INLINE)
d.comment(0xB985, 'Clear V for unconditional BVC', align=Align.INLINE)
d.comment(0xB988, 'Set V flag (= print mode)', align=Align.INLINE)
d.comment(0xB98B, 'Open file for reading', align=Align.INLINE)
d.comment(0xB990, 'A = 0', align=Align.INLINE)
d.comment(0xB992, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB994, 'Save V flag (print/type mode)', align=Align.INLINE)
d.comment(0xB998, 'Branch if not end of file', align=Align.INLINE)
d.comment(0xB99A, 'EOF: restore processor status', align=Align.INLINE)
d.comment(0xB99B, 'Close the file', align=Align.INLINE)
d.comment(0xB9A1, 'Check for escape key pressed', align=Align.INLINE)
d.comment(0xB9A4, 'Restore V (print/type mode)', align=Align.INLINE)
d.comment(0xB9A5, 'Re-save for next iteration', align=Align.INLINE)
d.comment(0xB9A6, 'Print mode: skip CR/LF handling', align=Align.INLINE)
d.comment(0xB9A8, 'Is it a carriage return?', align=Align.INLINE)
d.comment(0xB9AA, 'Yes: handle line ending', align=Align.INLINE)
d.comment(0xB9AC, 'Is it a line feed?', align=Align.INLINE)
d.comment(0xB9AE, 'Yes: handle line ending', align=Align.INLINE)
d.comment(0xB9B0, 'Save as previous character', align=Align.INLINE)
d.comment(0xB9B5, 'Loop for next byte', align=Align.INLINE)
d.comment(0xB9B8, 'Save the CR or LF character', align=Align.INLINE)
d.comment(0xB9B9, 'Check output destination flag', align=Align.INLINE)
d.comment(0xB9BC, 'Zero: normalise line endings', align=Align.INLINE)
d.comment(0xB9BE, 'Non-zero: output raw', align=Align.INLINE)
d.comment(0xB9C0, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB9C2, 'Retrieve CR/LF', align=Align.INLINE)
d.comment(0xB9C3, 'Output it directly; ALWAYS branch', align=Align.INLINE)
d.comment(0xB9C5, 'Get previous character', align=Align.INLINE)
d.comment(0xB9C7, 'Was previous a CR?', align=Align.INLINE)
d.comment(0xB9C9, 'Yes: check for CR+LF pair', align=Align.INLINE)
d.comment(0xB9CB, 'Was previous a LF?', align=Align.INLINE)
d.comment(0xB9CD, 'Yes: check for LF+CR pair', align=Align.INLINE)
d.comment(0xB9CF, 'Retrieve CR/LF from stack', align=Align.INLINE)
d.comment(0xB9D0, 'Save as previous character', align=Align.INLINE)
d.comment(0xB9D5, 'Loop for next byte', align=Align.INLINE)
d.comment(0xB9D8, 'Retrieve current character', align=Align.INLINE)
d.comment(0xB9D9, 'Is it LF? (CR+LF pair)', align=Align.INLINE)
d.comment(0xB9DB, 'Yes: consume LF, no extra newline', align=Align.INLINE)
d.comment(0xB9DD, 'No: output extra newline', align=Align.INLINE)
d.comment(0xB9DF, 'Retrieve current character', align=Align.INLINE)
d.comment(0xB9E0, 'Is it CR? (LF+CR pair)', align=Align.INLINE)
d.comment(0xB9E2, 'No: output extra newline', align=Align.INLINE)
d.comment(0xB9E4, 'Pair consumed: A = 0', align=Align.INLINE)
d.comment(0xB9E6, 'Clear previous-character tracker', align=Align.INLINE)
d.comment(0xB9E8, 'Loop for next byte; ALWAYS branch', align=Align.INLINE)
d.comment(0xB9EA, 'Test bit 7 of escape flag', align=Align.INLINE)
d.comment(0xB9EC, 'Escape pressed: handle abort', align=Align.INLINE)
d.comment(0xB9EE, 'No escape: return', align=Align.INLINE)
d.comment(0xB9EF, 'Close the open file', align=Align.INLINE)
d.comment(0xB9F5, 'Acknowledge escape condition', align=Align.INLINE)
d.comment(0xB9FA, 'Error number &11', align=Align.INLINE)
d.comment(0xB9FC, "Generate 'Escape' BRK error", align=Align.INLINE)
d.comment(0xB19F, 'Save command line pointer high', align=Align.INLINE)
d.comment(0xB1A1, 'Initialise spool/print drive', align=Align.INLINE)
d.comment(0xB1A4, 'Save spool drive number', align=Align.INLINE)
d.comment(0xB1A6, 'Copy PS name to TX buffer', align=Align.INLINE)
d.comment(0xB1A9, 'Init PS slot from RX data', align=Align.INLINE)
d.comment(0xB1AC, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB1AE, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xB1B1, 'Get first argument character', align=Align.INLINE)
d.comment(0xB1B3, 'End of command line?', align=Align.INLINE)
d.comment(0xB1B5, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xB1B7, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xB1B8, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xB1BB, 'Yes: station number, skip PS name', align=Align.INLINE)
d.comment(0xB1BD, 'PS name follows', align=Align.INLINE)
d.comment(0xB1BE, 'Save Y', align=Align.INLINE)
d.comment(0xB1BF, 'Load PS server address', align=Align.INLINE)
d.comment(0xB1C2, 'Restore Y', align=Align.INLINE)
d.comment(0xB1C3, 'Back to Y register', align=Align.INLINE)
d.comment(0xB1C4, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xB1C7, 'Offset &7A in slot buffer', align=Align.INLINE)
d.comment(0xB1C9, 'Get parsed station low', align=Align.INLINE)
d.comment(0xB1CB, 'Store station number low', align=Align.INLINE)
d.comment(0xB1CE, 'Get parsed network number', align=Align.INLINE)
d.comment(0xB1D0, 'Store station number high', align=Align.INLINE)
d.comment(0xB1D2, 'Offset &14 in TX buffer', align=Align.INLINE)
d.comment(0xB1D4, 'Copy PS data to TX buffer', align=Align.INLINE)
d.comment(0xB1D7, 'Get buffer page high', align=Align.INLINE)
d.comment(0xB1D9, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0xB1DB, 'Offset &78 in buffer', align=Align.INLINE)
d.comment(0xB1DD, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0xB1E1, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB1E4, 'V set (no arg): skip to send', align=Align.INLINE)
d.comment(0xB1E6, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB1E8, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB1EA, 'Space character', align=Align.INLINE)
d.comment(0xB1EC, 'Fill buffer position with space', align=Align.INLINE)
d.comment(0xB1EE, 'Next position', align=Align.INLINE)
d.comment(0xB1EF, 'Count down', align=Align.INLINE)
d.comment(0xB1F0, 'Loop until 6 spaces filled', align=Align.INLINE)
d.comment(0xB1F2, 'Save pointer to OS text', align=Align.INLINE)
d.comment(0xB1F5, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB1F7, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB1FA, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB1FC, 'Max 6 characters', align=Align.INLINE)
d.comment(0xB1FE, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB200, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB202, 'Save buffer position', align=Align.INLINE)
d.comment(0xB204, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB206, 'Read next char from string', align=Align.INLINE)
d.comment(0xB209, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB20B, 'End of string: go to send', align=Align.INLINE)
d.comment(0xB20D, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB210, 'Loop if more chars to copy', align=Align.INLINE)
d.comment(0xB212, 'Enable escape checking', align=Align.INLINE)
d.comment(0xB214, 'Set escapable flag', align=Align.INLINE)
d.comment(0xB216, 'Send the poll request packet', align=Align.INLINE)
d.comment(0xB219, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB21C, "Print 'Printer server '", align=Align.INLINE)
d.comment(0xB21F, 'Load PS server address', align=Align.INLINE)
d.comment(0xB222, 'Set V and N flags', align=Align.INLINE)
d.comment(0xB225, 'Print station address', align=Align.INLINE)
d.comment(0xB228, 'Print \' "\'', align=Align.INLINE)
d.comment(0xB22D, 'Start of PS name in buffer', align=Align.INLINE)
d.comment(0xB22F, 'Get character from name field', align=Align.INLINE)
d.comment(0xB231, 'Is it a space?', align=Align.INLINE)
d.comment(0xB233, 'Yes: end of name', align=Align.INLINE)
d.comment(0xB238, 'Next character', align=Align.INLINE)
d.comment(0xB239, 'Past end of name field?', align=Align.INLINE)
d.comment(0xB23B, 'No: continue printing name', align=Align.INLINE)
d.comment(0xB23D, 'Print \'"\' + CR', align=Align.INLINE)
d.comment(0xB242, 'Padding byte', align=Align.INLINE)
d.comment(0xB243, 'Get slot offset from stack', align=Align.INLINE)
d.comment(0xB244, 'Zero: all slots done, return', align=Align.INLINE)
d.comment(0xB246, 'Save slot offset', align=Align.INLINE)
d.comment(0xB247, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB248, 'Read slot status byte', align=Align.INLINE)
d.comment(0xB24A, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB24C, 'Advance to station number', align=Align.INLINE)
d.comment(0xB24D, 'Offset+2 in slot', align=Align.INLINE)
d.comment(0xB24E, 'Read station number low', align=Align.INLINE)
d.comment(0xB250, 'Store station low', align=Align.INLINE)
d.comment(0xB252, 'Next byte (offset+3)', align=Align.INLINE)
d.comment(0xB253, 'Read network number', align=Align.INLINE)
d.comment(0xB255, 'Store network number', align=Align.INLINE)
d.comment(0xB257, 'Next byte (offset+4)', align=Align.INLINE)
d.comment(0xB258, 'Read status page pointer', align=Align.INLINE)
d.comment(0xB25A, 'Store pointer low', align=Align.INLINE)
d.comment(0xB25C, 'Clear V flag', align=Align.INLINE)
d.comment(0xB25D, 'Print station address (V=0)', align=Align.INLINE)
d.comment(0xB260, "Print ' is '", align=Align.INLINE)
d.comment(0xB267, 'X=0 for indirect indexed access', align=Align.INLINE)
d.comment(0xB269, 'Read printer status byte', align=Align.INLINE)
d.comment(0xB26B, 'Non-zero: not ready', align=Align.INLINE)
d.comment(0xB26D, "Print 'ready'", align=Align.INLINE)
d.comment(0xB275, 'Clear V', align=Align.INLINE)
d.comment(0xB278, 'Status = 2?', align=Align.INLINE)
d.comment(0xB27A, 'No: check for busy', align=Align.INLINE)
d.comment(0xB27C, "Print 'jammed'", align=Align.INLINE)
d.comment(0xB285, 'Clear V', align=Align.INLINE)
d.comment(0xB288, 'Status = 1?', align=Align.INLINE)
d.comment(0xB28A, 'Not 1 or 2: default to jammed', align=Align.INLINE)
d.comment(0xB28C, "Print 'busy'", align=Align.INLINE)
d.comment(0xB293, 'Advance past status byte', align=Align.INLINE)
d.comment(0xB295, 'Read client station number', align=Align.INLINE)
d.comment(0xB297, 'Store station low', align=Align.INLINE)
d.comment(0xB299, 'Zero: no client info, skip', align=Align.INLINE)
d.comment(0xB29B, "Print ' with station '", align=Align.INLINE)
d.comment(0xB2AC, 'Advance past station low', align=Align.INLINE)
d.comment(0xB2AE, 'Read client network number', align=Align.INLINE)
d.comment(0xB2B0, 'Store network number', align=Align.INLINE)
d.comment(0xB2B2, 'Set V flag', align=Align.INLINE)
d.comment(0xB2B5, 'Print client station address', align=Align.INLINE)
d.comment(0xB2BB, 'Retrieve slot offset', align=Align.INLINE)
d.comment(0xB2BC, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB2BD, 'Mark slot as processed (&3F)', align=Align.INLINE)
d.comment(0xB2BF, 'Write marker to workspace', align=Align.INLINE)
d.comment(0xB2C3, 'Return', align=Align.INLINE)
d.comment(0xB2C4, 'Start at offset &78', align=Align.INLINE)
d.comment(0xB2C6, 'Load template byte', align=Align.INLINE)
d.comment(0xB2C9, 'At offset &7D?', align=Align.INLINE)
d.comment(0xB2CB, 'Yes: substitute RX page', align=Align.INLINE)
d.comment(0xB2CD, 'At offset &81?', align=Align.INLINE)
d.comment(0xB2CF, 'No: use template byte', align=Align.INLINE)
d.comment(0xB2D1, 'Use RX buffer page instead', align=Align.INLINE)
d.comment(0xB2D3, 'Store byte in slot buffer', align=Align.INLINE)
d.comment(0xB2D5, 'Next offset', align=Align.INLINE)
d.comment(0xB2D6, 'Past end of slot (&84)?', align=Align.INLINE)
d.comment(0xB2D8, 'No: continue copying', align=Align.INLINE)
d.comment(0xB2DA, 'Return', align=Align.INLINE)
d.comment(0xB2DB, 'Y = current buffer position', align=Align.INLINE)
d.comment(0xB2DD, 'Strip high bit', align=Align.INLINE)
d.comment(0xB2DF, "Is it lowercase 'a' or above?", align=Align.INLINE)
d.comment(0xB2E1, "Below 'a': not lowercase", align=Align.INLINE)
d.comment(0xB2E3, "Above 'z'?", align=Align.INLINE)
d.comment(0xB2E5, 'Yes: not lowercase', align=Align.INLINE)
d.comment(0xB2E7, 'Convert to uppercase', align=Align.INLINE)
d.comment(0xB2E9, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB2EB, 'Next buffer position', align=Align.INLINE)
d.comment(0xB2EC, 'Update buffer position', align=Align.INLINE)
d.comment(0xB2EE, 'Decrement character count', align=Align.INLINE)
d.comment(0xB2EF, 'Return (Z set if count=0)', align=Align.INLINE)
d.comment(0xAD59, 'Rotate carry into lib flag bit 7', align=Align.INLINE)
d.comment(0xAD5C, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xAD5D, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xAD60, 'A=&FF: initial column counter', align=Align.INLINE)
d.comment(0xAD62, 'Store column counter', align=Align.INLINE)
d.comment(0xAD64, 'One entry per line (Ex format)', align=Align.INLINE)
d.comment(0xAD66, 'Store entries per page', align=Align.INLINE)
d.comment(0xAD68, 'FS command code 3: Examine', align=Align.INLINE)
d.comment(0xAD6A, 'Store command code', align=Align.INLINE)
d.comment(0xAD6E, 'Set transfer parameters', align=Align.INLINE)
d.comment(0xAD71, 'Y=0: start from entry 0', align=Align.INLINE)
d.comment(0xAD73, 'Rotate carry into lib flag', align=Align.INLINE)
d.comment(0xAD76, 'Clear carry (= current directory)', align=Align.INLINE)
d.comment(0xAD77, 'Rotate carry back, clearing bit 7', align=Align.INLINE)
d.comment(0xAD7A, 'Three entries per column (Cat)', align=Align.INLINE)
d.comment(0xAD7C, 'Store column counter', align=Align.INLINE)
d.comment(0xAD7E, 'Store entries per page', align=Align.INLINE)
d.comment(0xAD80, 'FS command code &0B: Catalogue', align=Align.INLINE)
d.comment(0xAD82, 'Store command code', align=Align.INLINE)
d.comment(0xAD84, 'Save text pointer', align=Align.INLINE)
d.comment(0xAD87, 'A=&FF: enable escape checking', align=Align.INLINE)
d.comment(0xAD89, 'Set escapable flag', align=Align.INLINE)
d.comment(0xAD8B, 'Command code 6', align=Align.INLINE)
d.comment(0xAD8D, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xAD90, 'Parse directory argument', align=Align.INLINE)
d.comment(0xAD93, 'X=1: offset in buffer', align=Align.INLINE)
d.comment(0xAD95, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0xAD98, 'Get library/FS flags', align=Align.INLINE)
d.comment(0xAD9B, 'Shift bit 0 to carry', align=Align.INLINE)
d.comment(0xAD9C, 'Bit 0 clear: skip', align=Align.INLINE)
d.comment(0xAD9E, 'Set bit 6 (owner access flag)', align=Align.INLINE)
d.comment(0xADA0, 'Rotate back', align=Align.INLINE)
d.comment(0xADA1, 'Store modified flags', align=Align.INLINE)
d.comment(0xADA4, 'Y=&12: FS command for examine', align=Align.INLINE)
d.comment(0xADA6, 'Send request to file server', align=Align.INLINE)
d.comment(0xADA9, 'X=3: offset to directory title', align=Align.INLINE)
d.comment(0xADAB, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0xADAE, "Print '('", align=Align.INLINE)
d.comment(0xADB2, 'Get cycle number', align=Align.INLINE)
d.comment(0xADB5, 'Print as 3-digit decimal', align=Align.INLINE)
d.comment(0xADB8, "Print ')     '", align=Align.INLINE)
d.comment(0xADC1, 'Get owner/public flag', align=Align.INLINE)
d.comment(0xADC4, 'Non-zero: public access', align=Align.INLINE)
d.comment(0xADC6, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0xADCF, 'Skip public; ALWAYS branch', align=Align.INLINE)
d.comment(0xADD1, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0xADDB, 'Get flags', align=Align.INLINE)
d.comment(0xADDE, 'Save flags', align=Align.INLINE)
d.comment(0xADDF, 'Mask owner access bits', align=Align.INLINE)
d.comment(0xADE2, 'Y=&15: FS command for dir info', align=Align.INLINE)
d.comment(0xADE4, 'Send request to file server', align=Align.INLINE)
d.comment(0xADE7, 'Advance X past header', align=Align.INLINE)
d.comment(0xADE8, 'Y=&10: print 16 chars', align=Align.INLINE)
d.comment(0xADEA, 'Print file entry', align=Align.INLINE)
d.comment(0xADED, "Print '    Option '", align=Align.INLINE)
d.comment(0xADFB, 'Get option byte', align=Align.INLINE)
d.comment(0xADFE, 'Transfer to X for table lookup', align=Align.INLINE)
d.comment(0xADFF, 'Print option as hex', align=Align.INLINE)
d.comment(0xAE02, "Print ' ('", align=Align.INLINE)
d.comment(0xAE07, 'Index into option string table', align=Align.INLINE)
d.comment(0xAE0A, 'Get option name character', align=Align.INLINE)
d.comment(0xAE0D, 'High bit set: end of string', align=Align.INLINE)
d.comment(0xAE12, 'Next character', align=Align.INLINE)
d.comment(0xAE13, 'Loop; ALWAYS branch', align=Align.INLINE)
d.comment(0xAE15, "Print ')' + CR + 'Dir. '", align=Align.INLINE)
d.comment(0xAE1F, 'Offset &11: directory name', align=Align.INLINE)
d.comment(0xAE21, 'Print directory name (10 chars)', align=Align.INLINE)
d.comment(0xAE24, "Print '     Lib. '", align=Align.INLINE)
d.comment(0xAE31, 'Offset &1B: library name', align=Align.INLINE)
d.comment(0xAE33, 'Print library name (10 chars)', align=Align.INLINE)
d.comment(0xAE39, 'Restore flags', align=Align.INLINE)
d.comment(0xAE3A, 'Store restored flags', align=Align.INLINE)
d.comment(0xAE3D, 'Store entry count', align=Align.INLINE)
d.comment(0xAE40, 'Also store in work_4', align=Align.INLINE)
d.comment(0xAE42, 'Get command code', align=Align.INLINE)
d.comment(0xAE44, 'Store in buffer', align=Align.INLINE)
d.comment(0xAE47, 'Get entries per page', align=Align.INLINE)
d.comment(0xAE49, 'Store in buffer', align=Align.INLINE)
d.comment(0xAE4C, 'X=3: buffer offset', align=Align.INLINE)
d.comment(0xAE4E, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xAE51, 'Y=3: FS command for examine/cat', align=Align.INLINE)
d.comment(0xAE53, 'Send request to file server', align=Align.INLINE)
d.comment(0xAE56, 'Advance past header', align=Align.INLINE)
d.comment(0xAE57, 'Get number of entries returned', align=Align.INLINE)
d.comment(0xAE5A, 'Zero: no more entries', align=Align.INLINE)
d.comment(0xAE5C, 'Save entry count', align=Align.INLINE)
d.comment(0xAE5D, 'Advance Y', align=Align.INLINE)
d.comment(0xAE5E, 'Get entry data byte', align=Align.INLINE)
d.comment(0xAE61, 'Bit 7 clear: more data', align=Align.INLINE)
d.comment(0xAE63, 'Store terminator byte', align=Align.INLINE)
d.comment(0xAE66, 'Print entry with column separator', align=Align.INLINE)
d.comment(0xAE69, 'Restore entry count', align=Align.INLINE)
d.comment(0xAE6A, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xAE6B, 'Add entries processed', align=Align.INLINE)
d.comment(0xAE6D, 'Transfer to Y', align=Align.INLINE)
d.comment(0xAE6E, 'More entries: loop', align=Align.INLINE)
d.comment(0xAE70, 'Y=10: characters to print', align=Align.INLINE)
d.comment(0xAE72, 'Get character from buffer', align=Align.INLINE)
d.comment(0xAE78, 'Next buffer position', align=Align.INLINE)
d.comment(0xAE79, 'Decrement count', align=Align.INLINE)
d.comment(0xAE7A, 'Loop until 10 printed', align=Align.INLINE)
d.comment(0xAE7C, 'Return', align=Align.INLINE)
d.comment(0xAE80, 'Y=0: start of command line', align=Align.INLINE)
d.comment(0xAE82, 'Read string to buffer via GSREAD', align=Align.INLINE)
d.comment(0xAE85, 'Get first parsed character', align=Align.INLINE)
d.comment(0xAE88, "Is it '&'?", align=Align.INLINE)
d.comment(0xAE8A, "No: check for ':' prefix", align=Align.INLINE)
d.comment(0xAE8C, 'Get flags', align=Align.INLINE)
d.comment(0xAE8F, 'Set FS selection flag (bit 6)', align=Align.INLINE)
d.comment(0xAE91, 'Store updated flags', align=Align.INLINE)
d.comment(0xAE94, "Remove '&' prefix character", align=Align.INLINE)
d.comment(0xAE97, 'Get next character', align=Align.INLINE)
d.comment(0xAE9A, "Is it '.'?", align=Align.INLINE)
d.comment(0xAE9C, "No: check for '#'", align=Align.INLINE)
d.comment(0xAE9E, "Get char after '.'", align=Align.INLINE)
d.comment(0xAEA1, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEA3, "Yes: '&.' + CR only = bad filename", align=Align.INLINE)
d.comment(0xAEA5, 'Save X', align=Align.INLINE)
d.comment(0xAEA6, 'Push X', align=Align.INLINE)
d.comment(0xAEA7, 'X=&FF, will increment to 0', align=Align.INLINE)
d.comment(0xAEA9, 'Increment X', align=Align.INLINE)
d.comment(0xAEAA, 'Get character at offset+1', align=Align.INLINE)
d.comment(0xAEAD, 'Store at offset (shift left)', align=Align.INLINE)
d.comment(0xAEB0, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEB2, 'No: continue shifting', align=Align.INLINE)
d.comment(0xAEB4, 'Get shifted string length', align=Align.INLINE)
d.comment(0xAEB5, 'Zero length: skip trailing trim', align=Align.INLINE)
d.comment(0xAEB7, 'Get character at end of string', align=Align.INLINE)
d.comment(0xAEBA, 'Is it a space?', align=Align.INLINE)
d.comment(0xAEBC, 'No: done trimming', align=Align.INLINE)
d.comment(0xAEBE, 'Replace trailing space with CR', align=Align.INLINE)
d.comment(0xAEC0, 'Store CR', align=Align.INLINE)
d.comment(0xAEC3, 'Move back', align=Align.INLINE)
d.comment(0xAEC4, 'Loop while more trailing spaces', align=Align.INLINE)
d.comment(0xAEC6, 'Restore X', align=Align.INLINE)
d.comment(0xAEC7, 'Transfer back to X', align=Align.INLINE)
d.comment(0xAEC8, 'Return', align=Align.INLINE)
d.comment(0xAEC9, "Is it '#'?", align=Align.INLINE)
d.comment(0xAECB, "Yes: '#' prefix accepted", align=Align.INLINE)
d.comment(0xAECD, 'Bad filename error', align=Align.INLINE)
d.comment(0xAED0, "Check for ':' prefix", align=Align.INLINE)
d.comment(0xAED2, "Neither '&' nor ':': no prefix", align=Align.INLINE)
d.comment(0xAED4, "Get character after ':'", align=Align.INLINE)
d.comment(0xAED7, "Is it '.'?", align=Align.INLINE)
d.comment(0xAED9, "Yes: ':.' qualified prefix", align=Align.INLINE)
d.comment(0xAEDB, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAEDD, 'No: no FS prefix, return', align=Align.INLINE)
d.comment(0xAEDF, 'Get flags', align=Align.INLINE)
d.comment(0xAEE2, 'Set FS selection flag (bit 6)', align=Align.INLINE)
d.comment(0xAEE4, 'Store updated flags', align=Align.INLINE)
d.comment(0xAEE9, 'Data: option string offset table', align=Align.INLINE)
d.comment(0xAEF0, 'X=0: start of buffer', align=Align.INLINE)
d.comment(0xAEF2, 'Y=0: start of argument', align=Align.INLINE)
d.comment(0xAEF4, "Set carry: enable '&' validation", align=Align.INLINE)
d.comment(0xAEF5, 'Get character from command line', align=Align.INLINE)
d.comment(0xAEF7, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xAEFA, 'Carry clear: skip validation', align=Align.INLINE)
d.comment(0xAEFC, "Is it '!' or above?", align=Align.INLINE)
d.comment(0xAEFE, "Is it '&'?", align=Align.INLINE)
d.comment(0xAF00, 'No: continue copying', align=Align.INLINE)
d.comment(0xAF02, "'&' in filename: bad filename", align=Align.INLINE)
d.comment(0xAF05, "Restore A (undo '&' EOR)", align=Align.INLINE)
d.comment(0xAF07, 'Advance buffer position', align=Align.INLINE)
d.comment(0xAF08, 'Advance source position', align=Align.INLINE)
d.comment(0xAF09, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xAF0B, 'No: continue copying', align=Align.INLINE)
d.comment(0xAF0D, 'Return', align=Align.INLINE)
d.comment(0xAF12, 'Get flags', align=Align.INLINE)
d.comment(0xAF15, 'Mask to low 5 bits only', align=Align.INLINE)
d.comment(0xAF17, 'Store masked flags', align=Align.INLINE)
d.comment(0xAF1A, 'Return', align=Align.INLINE)
d.comment(0xAF1E, 'X=0: start from first entry', align=Align.INLINE)
d.comment(0xAF20, 'Get entry byte from buffer', align=Align.INLINE)
d.comment(0xAF23, 'High bit set: end of entries', align=Align.INLINE)
d.comment(0xAF25, 'Non-zero: printable character', align=Align.INLINE)
d.comment(0xAF27, 'Get column counter', align=Align.INLINE)
d.comment(0xAF29, 'Negative: newline mode (Ex)', align=Align.INLINE)
d.comment(0xAF2B, 'Increment column counter', align=Align.INLINE)
d.comment(0xAF2C, 'Transfer to A', align=Align.INLINE)
d.comment(0xAF2D, 'Modulo 4 (Cat: 3 per row)', align=Align.INLINE)
d.comment(0xAF2F, 'Store updated counter', align=Align.INLINE)
d.comment(0xAF31, 'Zero: row full, print newline', align=Align.INLINE)
d.comment(0xAF33, "Print '  ' column separator", align=Align.INLINE)
d.comment(0xAF38, 'Skip newline; ALWAYS branch', align=Align.INLINE)
d.comment(0xAF3A, 'CR character for newline', align=Align.INLINE)
d.comment(0xAF3F, 'Advance to next entry', align=Align.INLINE)
d.comment(0xAF40, 'Loop for more entries', align=Align.INLINE)
d.comment(0xAF42, "Embedded string data 'Exec'", align=Align.INLINE)
d.comment(0xAF44, 'Embedded string data (contd)', align=Align.INLINE)
d.comment(0xAFCE, 'A=1: check printer ready', align=Align.INLINE)
d.comment(0xAFD0, 'Test printer server workspace flag', align=Align.INLINE)
d.comment(0xAFD3, 'Non-zero: printer available', align=Align.INLINE)
d.comment(0xAFD5, 'Printer not available: error', align=Align.INLINE)
d.comment(0xAFD8, 'Initialise spool drive', align=Align.INLINE)
d.comment(0xAFDB, 'Save pointer to spool buffer', align=Align.INLINE)
d.comment(0xAFDE, 'Get first argument character', align=Align.INLINE)
d.comment(0xAFE0, 'End of command line?', align=Align.INLINE)
d.comment(0xAFE2, 'Yes: no argument given', align=Align.INLINE)
d.comment(0xAFE4, 'Clear V (= explicit PS name given)', align=Align.INLINE)
d.comment(0xAFE5, 'Is first char a decimal digit?', align=Align.INLINE)
d.comment(0xAFE8, 'Yes: station number, skip PS name', align=Align.INLINE)
d.comment(0xAFEA, 'PS name follows', align=Align.INLINE)
d.comment(0xAFEB, 'Save Y', align=Align.INLINE)
d.comment(0xAFEC, 'Load PS server address', align=Align.INLINE)
d.comment(0xAFEF, 'Restore Y', align=Align.INLINE)
d.comment(0xAFF0, 'Back to Y register', align=Align.INLINE)
d.comment(0xAFF1, 'Parse FS/PS arguments', align=Align.INLINE)
d.comment(0xAFF4, 'Jump to store station address', align=Align.INLINE)
d.comment(0xAFF7, 'Start at offset &1C', align=Align.INLINE)
d.comment(0xAFF9, 'X=&F8: offset into template', align=Align.INLINE)
d.comment(0xAFFB, 'Get template byte', align=Align.INLINE)
d.comment(0xAFFE, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB000, 'Next destination offset', align=Align.INLINE)
d.comment(0xB001, 'Next source offset', align=Align.INLINE)
d.comment(0xB002, 'Loop until X wraps to 0', align=Align.INLINE)
d.comment(0xB004, 'Return', align=Align.INLINE)
d.comment(0xB005, 'Set V (= no explicit PS name)', align=Align.INLINE)
d.comment(0xB008, 'Save command line pointer', align=Align.INLINE)
d.comment(0xB00A, 'V set: skip PS name parsing', align=Align.INLINE)
d.comment(0xB00C, 'Max 6 characters for PS name', align=Align.INLINE)
d.comment(0xB00E, 'Buffer offset &1C for PS name', align=Align.INLINE)
d.comment(0xB010, 'Space character', align=Align.INLINE)
d.comment(0xB012, 'Fill buffer with space', align=Align.INLINE)
d.comment(0xB014, 'Next position', align=Align.INLINE)
d.comment(0xB015, 'Count down', align=Align.INLINE)
d.comment(0xB016, 'Loop until 6 spaces filled', align=Align.INLINE)
d.comment(0xB018, 'Save text pointer', align=Align.INLINE)
d.comment(0xB01B, 'Restore command line pointer', align=Align.INLINE)
d.comment(0xB01D, 'Initialise string reading', align=Align.INLINE)
d.comment(0xB020, 'Empty string: skip to send', align=Align.INLINE)
d.comment(0xB022, 'Max 6 characters', align=Align.INLINE)
d.comment(0xB024, 'Save updated string pointer', align=Align.INLINE)
d.comment(0xB026, 'Buffer offset for PS name', align=Align.INLINE)
d.comment(0xB028, 'Save buffer position', align=Align.INLINE)
d.comment(0xB02A, 'Restore string pointer', align=Align.INLINE)
d.comment(0xB02C, 'Read next character', align=Align.INLINE)
d.comment(0xB02F, 'Save updated pointer', align=Align.INLINE)
d.comment(0xB031, 'End of string: go to send', align=Align.INLINE)
d.comment(0xB033, 'Store char uppercased in buffer', align=Align.INLINE)
d.comment(0xB036, 'Loop for more characters', align=Align.INLINE)
d.comment(0xB038, 'Copy reversed PS name to TX', align=Align.INLINE)
d.comment(0xB03B, 'Send PS status request', align=Align.INLINE)
d.comment(0xB03E, 'Pop and requeue PS scan', align=Align.INLINE)
d.comment(0xB041, 'Load PS server address', align=Align.INLINE)
d.comment(0xB044, 'A=0', align=Align.INLINE)
d.comment(0xB047, 'Offset &24 in buffer', align=Align.INLINE)
d.comment(0xB049, 'Clear PS status byte', align=Align.INLINE)
d.comment(0xB04B, 'Get slot offset from stack', align=Align.INLINE)
d.comment(0xB04C, 'Zero: all slots done', align=Align.INLINE)
d.comment(0xB04E, 'Save slot offset', align=Align.INLINE)
d.comment(0xB04F, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB050, 'Read slot status', align=Align.INLINE)
d.comment(0xB052, 'Bit 7 clear: slot inactive', align=Align.INLINE)
d.comment(0xB054, 'Advance Y by 4 (to status page)', align=Align.INLINE)
d.comment(0xB057, 'Read status page pointer', align=Align.INLINE)
d.comment(0xB059, 'Store pointer low', align=Align.INLINE)
d.comment(0xB05B, 'Read printer status byte', align=Align.INLINE)
d.comment(0xB05D, 'Non-zero (busy): skip', align=Align.INLINE)
d.comment(0xB05F, 'Back to network number', align=Align.INLINE)
d.comment(0xB060, 'Read network number', align=Align.INLINE)
d.comment(0xB062, 'Store network number', align=Align.INLINE)
d.comment(0xB064, 'Back to station number', align=Align.INLINE)
d.comment(0xB065, 'Read station number', align=Align.INLINE)
d.comment(0xB067, 'Store station low', align=Align.INLINE)
d.comment(0xB069, 'Offset &24 in buffer', align=Align.INLINE)
d.comment(0xB06B, 'Store ready station in buffer', align=Align.INLINE)
d.comment(0xB06D, 'Retrieve slot offset', align=Align.INLINE)
d.comment(0xB06E, 'Transfer to Y', align=Align.INLINE)
d.comment(0xB06F, 'Mark slot as processed (&3F)', align=Align.INLINE)
d.comment(0xB071, 'Write marker to workspace', align=Align.INLINE)
d.comment(0xB075, "Print 'Printer server is '", align=Align.INLINE)
d.comment(0xB078, 'Offset &24: PS station number', align=Align.INLINE)
d.comment(0xB07A, 'Get stored station number', align=Align.INLINE)
d.comment(0xB07C, 'Non-zero: server changed', align=Align.INLINE)
d.comment(0xB07E, "Print 'still '", align=Align.INLINE)
d.comment(0xB087, 'Clear V', align=Align.INLINE)
d.comment(0xB08A, "Print 'now '", align=Align.INLINE)
d.comment(0xB091, 'Padding', align=Align.INLINE)
d.comment(0xB092, 'Print FS info and newline', align=Align.INLINE)
d.comment(0xB095, 'Workspace offset 2', align=Align.INLINE)
d.comment(0xB097, 'Get station low', align=Align.INLINE)
d.comment(0xB099, 'Store in workspace', align=Align.INLINE)
d.comment(0xB09C, 'Get network number', align=Align.INLINE)
d.comment(0xB09E, 'Store in workspace', align=Align.INLINE)
d.comment(0xB0A0, 'Return', align=Align.INLINE)
d.comment(0xB0A1, "Print 'File'", align=Align.INLINE)
d.comment(0xB0A8, 'Clear V', align=Align.INLINE)
d.comment(0xB0AB, "Print 'Printer'", align=Align.INLINE)
d.comment(0xB0B5, 'Padding', align=Align.INLINE)
d.comment(0xB0B6, "Print ' server is '", align=Align.INLINE)
d.comment(0xB0C4, 'Padding', align=Align.INLINE)
d.comment(0xB0C5, 'Return', align=Align.INLINE)
d.comment(0xB0C6, 'Workspace offset 2', align=Align.INLINE)
d.comment(0xB0C8, 'Read station low', align=Align.INLINE)
d.comment(0xB0CA, 'Store station low', align=Align.INLINE)
d.comment(0xB0CD, 'Read network number', align=Align.INLINE)
d.comment(0xB0CF, 'Store network number', align=Align.INLINE)
d.comment(0xB0D1, 'Return', align=Align.INLINE)
d.comment(0xB0D2, 'Pop return address low', align=Align.INLINE)
d.comment(0xB0D3, 'Save return address low', align=Align.INLINE)
d.comment(0xB0D5, 'Pop return address high', align=Align.INLINE)
d.comment(0xB0D6, 'Save return address high', align=Align.INLINE)
d.comment(0xB0D8, 'Push 0 as end-of-list marker', align=Align.INLINE)
d.comment(0xB0DA, 'Push it', align=Align.INLINE)
d.comment(0xB0DB, 'Start scanning from offset &84', align=Align.INLINE)
d.comment(0xB0DD, 'Store scan position', align=Align.INLINE)
d.comment(0xB0DF, 'Shift PS slot flags right', align=Align.INLINE)
d.comment(0xB0E2, 'Counter: 3 PS slots', align=Align.INLINE)
d.comment(0xB0E4, 'Convert to 2-bit workspace index', align=Align.INLINE)
d.comment(0xB0E7, 'Carry set: no more slots', align=Align.INLINE)
d.comment(0xB0E9, 'Shift right twice', align=Align.INLINE)
d.comment(0xB0EA, 'To get slot offset', align=Align.INLINE)
d.comment(0xB0EB, 'Transfer to X', align=Align.INLINE)
d.comment(0xB0EC, 'Read slot status byte', align=Align.INLINE)
d.comment(0xB0EE, 'Zero: empty slot, done', align=Align.INLINE)
d.comment(0xB0F0, 'Is it processed marker (&3F)?', align=Align.INLINE)
d.comment(0xB0F2, 'Yes: re-initialise this slot', align=Align.INLINE)
d.comment(0xB0F4, 'Try next slot', align=Align.INLINE)
d.comment(0xB0F5, 'Transfer slot index to A', align=Align.INLINE)
d.comment(0xB0F6, 'Loop for more slots', align=Align.INLINE)
d.comment(0xB0F8, 'Y = workspace offset of slot', align=Align.INLINE)
d.comment(0xB0F9, 'Push slot offset for scan list', align=Align.INLINE)
d.comment(0xB0FA, 'Set active status (&7F)', align=Align.INLINE)
d.comment(0xB0FC, 'Write status byte', align=Align.INLINE)
d.comment(0xB0FE, 'Next byte', align=Align.INLINE)
d.comment(0xB0FF, 'Low byte: workspace page', align=Align.INLINE)
d.comment(0xB101, 'Write workspace pointer low', align=Align.INLINE)
d.comment(0xB103, 'A=0', align=Align.INLINE)
d.comment(0xB105, 'Write two zero bytes + advance Y', align=Align.INLINE)
d.comment(0xB108, 'Get current scan page', align=Align.INLINE)
d.comment(0xB10A, 'Write RX buffer page low', align=Align.INLINE)
d.comment(0xB10C, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xB10D, 'Save processor status', align=Align.INLINE)
d.comment(0xB10E, 'Advance by 3 pages', align=Align.INLINE)
d.comment(0xB110, 'Restore processor status', align=Align.INLINE)
d.comment(0xB111, 'Update scan position', align=Align.INLINE)
d.comment(0xB113, 'Write buffer page + &FF bytes', align=Align.INLINE)
d.comment(0xB116, 'Get updated scan position', align=Align.INLINE)
d.comment(0xB118, 'Write RX buffer page high', align=Align.INLINE)
d.comment(0xB11A, 'Write another page + &FF bytes', align=Align.INLINE)
d.comment(0xB11D, 'Continue scanning slots', align=Align.INLINE)
d.comment(0xB120, 'Shift PS slot flags back', align=Align.INLINE)
d.comment(0xB123, 'Restore return address high', align=Align.INLINE)
d.comment(0xB125, 'Push onto stack', align=Align.INLINE)
d.comment(0xB126, 'Restore return address low', align=Align.INLINE)
d.comment(0xB128, 'Push onto stack', align=Align.INLINE)
d.comment(0xB129, 'Delay counter: 10', align=Align.INLINE)
d.comment(0xB12D, 'Outer loop counter = 10', align=Align.INLINE)
d.comment(0xB12F, 'Decrement Y (inner loop)', align=Align.INLINE)
d.comment(0xB130, 'Inner loop: 10 iterations', align=Align.INLINE)
d.comment(0xB132, 'Decrement X (middle loop)', align=Align.INLINE)
d.comment(0xB133, 'Middle loop: 10 iterations', align=Align.INLINE)
d.comment(0xB135, 'Decrement outer counter', align=Align.INLINE)
d.comment(0xB137, 'Outer loop: ~1000 delay cycles', align=Align.INLINE)
d.comment(0xB139, 'Return', align=Align.INLINE)
d.comment(0xB13A, 'Advance Y', align=Align.INLINE)
d.comment(0xB13B, 'Get buffer page', align=Align.INLINE)
d.comment(0xB13D, 'Store in workspace', align=Align.INLINE)
d.comment(0xB13F, 'A=&FF', align=Align.INLINE)
d.comment(0xB141, 'Advance Y', align=Align.INLINE)
d.comment(0xB142, 'Write byte to workspace', align=Align.INLINE)
d.comment(0xB144, 'Advance Y', align=Align.INLINE)
d.comment(0xB145, 'Write byte to workspace', align=Align.INLINE)
d.comment(0xB147, 'Advance Y', align=Align.INLINE)
d.comment(0xB148, 'Return', align=Align.INLINE)
d.comment(0xB149, 'Start of PS name at offset &1C', align=Align.INLINE)
d.comment(0xB14B, 'Load byte from RX buffer', align=Align.INLINE)
d.comment(0xB14D, 'Push to stack (for reversal)', align=Align.INLINE)
d.comment(0xB14E, 'Next source byte', align=Align.INLINE)
d.comment(0xB14F, 'End of PS name field (&24)?', align=Align.INLINE)
d.comment(0xB151, 'No: continue pushing', align=Align.INLINE)
d.comment(0xB153, 'End of TX name field at &1B', align=Align.INLINE)
d.comment(0xB155, 'Pop byte (reversed order)', align=Align.INLINE)
d.comment(0xB156, 'Store in RX buffer', align=Align.INLINE)
d.comment(0xB158, 'Previous position', align=Align.INLINE)
d.comment(0xB159, 'Start of TX field (&13)?', align=Align.INLINE)
d.comment(0xB15B, 'No: continue popping', align=Align.INLINE)
d.comment(0xB15D, 'Copy RX page to TX', align=Align.INLINE)
d.comment(0xB15F, 'Set TX pointer high', align=Align.INLINE)
d.comment(0xB161, 'TX offset &10', align=Align.INLINE)
d.comment(0xB163, 'Set TX pointer low', align=Align.INLINE)
d.comment(0xB165, 'Copy 4 header bytes', align=Align.INLINE)
d.comment(0xB167, 'Get header template byte', align=Align.INLINE)
d.comment(0xB16A, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB16C, 'Previous byte', align=Align.INLINE)
d.comment(0xB16D, 'Loop until all 4 copied', align=Align.INLINE)
d.comment(0xB16F, 'Return', align=Align.INLINE)
d.comment(0xB170, """Printer server TX header template

4-byte header copied to the TX control block by
reverse_ps_name_to_tx. Sets up an immediate
transmit on port &9F (PS port) to any station.""")
d.comment(0xB170, 'Control byte &80 (immediate TX)', align=Align.INLINE)
d.comment(0xB171, 'Port &9F (printer server)', align=Align.INLINE)
d.comment(0xB172, 'Station &FF (any)', align=Align.INLINE)
d.comment(0xB173, 'Network &FF (any)', align=Align.INLINE)
d.comment(0xB174, 'Save V flag (controls padding)', align=Align.INLINE)
d.comment(0xB175, 'Get network number', align=Align.INLINE)
d.comment(0xB177, 'Zero: no network prefix', align=Align.INLINE)
d.comment(0xB179, 'Print network as 3 digits', align=Align.INLINE)
d.comment(0xB17C, "'.' separator", align=Align.INLINE)
d.comment(0xB181, 'Set V (suppress station padding)', align=Align.INLINE)
d.comment(0xB184, 'V set: skip padding spaces', align=Align.INLINE)
d.comment(0xB186, 'Print 4 spaces (padding)', align=Align.INLINE)
d.comment(0xB18D, 'Get station number', align=Align.INLINE)
d.comment(0xB18F, 'Restore flags', align=Align.INLINE)
d.comment(0xB190, 'Print station as 3 digits', align=Align.INLINE)
d.comment(0xB193, """PS slot transmit control block template

12-byte Econet TXCB initialisation template for
printer server slot buffers. Not referenced by
label; accessed indirectly by init_ps_slot_from_rx
via LDA write_ps_slot_link_addr,Y where the base
address write_ps_slot_hi_link+1 plus Y offset &78 computes to &B193.

Structure: 4-byte header (control, port, station,
network) followed by two 4-byte buffer descriptors
(lo address, hi page, end lo, end hi). The hi page
bytes at positions 5 and 9 are overwritten with
net_rx_ptr_hi during the copy to point into the
actual RX buffer page. End bytes &FF are
placeholders filled in later by the caller.""")
d.comment(0xB193, 'Control byte &80 (immediate TX)', align=Align.INLINE)
d.comment(0xB194, 'Port &9F (printer server)', align=Align.INLINE)
d.comment(0xB195, 'Station 0 (filled in later)', align=Align.INLINE)
d.comment(0xB196, 'Network 0 (filled in later)', align=Align.INLINE)
d.comment(0xB197, 'Data buffer start lo (&14)', align=Align.INLINE)
d.comment(0xB198, 'Data buffer start hi (= rx page)', align=Align.INLINE)
d.comment(0xB199, 'Data buffer end lo (placeholder)', align=Align.INLINE)
d.comment(0xB19A, 'Data buffer end hi (placeholder)', align=Align.INLINE)
d.comment(0xB19B, 'Reply buffer start lo (&1C)', align=Align.INLINE)
d.comment(0xB19C, 'Reply buffer start hi (= rx page)', align=Align.INLINE)
d.comment(0xB19D, 'Reply buffer end lo (placeholder)', align=Align.INLINE)
d.comment(0xB19E, 'Reply buffer end hi (placeholder)', align=Align.INLINE)
d.comment(0x948A, 'Y=0: close all files', align=Align.INLINE)
d.comment(0x948C, 'Process all file control blocks', align=Align.INLINE)
d.comment(0x948F, 'OSBYTE &77: close spool/exec', align=Align.INLINE)
d.comment(0x9494, 'Close all network channels', align=Align.INLINE)
d.comment(0x9497, 'Y=&17: *Bye function code', align=Align.INLINE)
d.comment(0x9499, 'Clear V (standard mode)', align=Align.INLINE)
d.comment(0x949A, 'Copy FS station to TX control block', align=Align.INLINE)
d.comment(0x949D, 'Store in TXCB', align=Align.INLINE)
d.comment(0x94A0, 'Clear carry', align=Align.INLINE)
d.comment(0x94A1, 'Save flags (carry = mode)', align=Align.INLINE)
d.comment(0x94A2, 'Store function code in TXCB', align=Align.INLINE)
d.comment(0x94A5, 'Copy 2 bytes (indices 0-1)', align=Align.INLINE)
d.comment(0x94A7, 'Load source byte', align=Align.INLINE)
d.comment(0x94AA, 'Store to TXCB', align=Align.INLINE)
d.comment(0x94AD, 'Next byte', align=Align.INLINE)
d.comment(0x94AE, 'Loop until all copied', align=Align.INLINE)
d.comment(0x94B0, 'Test library flag bits 6-7', align=Align.INLINE)
d.comment(0x94B3, 'Bit 6 set: use station as port', align=Align.INLINE)
d.comment(0x94B5, 'Bit 7 clear: skip port override', align=Align.INLINE)
d.comment(0x94B7, 'Bit 7 set: load alternative port', align=Align.INLINE)
d.comment(0x94BA, 'Override TXCB port byte', align=Align.INLINE)
d.comment(0x94BF, 'Bit 6: load station byte', align=Align.INLINE)
d.comment(0x94C2, 'Use station as TXCB port', align=Align.INLINE)
d.comment(0x94C5, 'Restore flags (carry = mode)', align=Align.INLINE)
d.comment(0x94C6, 'Save flags', align=Align.INLINE)
d.comment(0x94C7, 'Port &90: FS command port', align=Align.INLINE)
d.comment(0x94C9, 'Set reply port in TXCB', align=Align.INLINE)
d.comment(0x94CC, 'Initialise TXCB workspace', align=Align.INLINE)
d.comment(0x94CF, 'Get TXCB data end offset', align=Align.INLINE)
d.comment(0x94D0, 'Add 5 for header size', align=Align.INLINE)
d.comment(0x94D2, 'Set TXCB end pointer', align=Align.INLINE)
d.comment(0x94D4, 'Restore flags', align=Align.INLINE)
d.comment(0x94D5, 'C set: send disconnect instead', align=Align.INLINE)
d.comment(0x94D7, 'Save flags', align=Align.INLINE)
d.comment(0x94D8, 'Initialise TX pointer and send', align=Align.INLINE)
d.comment(0x94DB, 'Restore flags', align=Align.INLINE)
d.comment(0x94DC, 'Save flags', align=Align.INLINE)
d.comment(0x94DD, 'Set up receive TXCB', align=Align.INLINE)
d.comment(0x94E0, 'Wait for TX acknowledgment', align=Align.INLINE)
d.comment(0x94E3, 'Restore flags', align=Align.INLINE)
d.comment(0x94E4, 'Advance to next reply byte', align=Align.INLINE)
d.comment(0x94E5, 'Load reply byte', align=Align.INLINE)
d.comment(0x94E7, 'Save in X', align=Align.INLINE)
d.comment(0x94E8, 'Zero: no more replies, return', align=Align.INLINE)
d.comment(0x94EA, 'V clear: use code directly', align=Align.INLINE)
d.comment(0x94EC, 'V set: adjust reply code (+&2B)', align=Align.INLINE)
d.comment(0x94EE, 'Non-zero: process reply', align=Align.INLINE)
d.comment(0x94F0, 'Return', align=Align.INLINE)
d.comment(0x94F1, 'Discard saved flags', align=Align.INLINE)
d.comment(0x94F2, 'X=&C0: disconnect command', align=Align.INLINE)
d.comment(0x94F4, 'Advance reply offset', align=Align.INLINE)
d.comment(0x94F5, 'Send disconnect reply', align=Align.INLINE)
d.comment(0x94F8, 'Successful: process next reply', align=Align.INLINE)
d.comment(0x94FA, 'Store reply status code', align=Align.INLINE)
d.comment(0x94FD, 'Load pending operation marker', align=Align.INLINE)
d.comment(0x9500, 'Pending: go to data loss check', align=Align.INLINE)
d.comment(0x9502, 'Reply &BF (normal bye response)?', align=Align.INLINE)
d.comment(0x9504, 'No: build error from reply', align=Align.INLINE)
d.comment(0x9506, 'A=&40: initial data-loss flag', align=Align.INLINE)
d.comment(0x9508, 'Push data-loss accumulator', align=Align.INLINE)
d.comment(0x9509, 'Scan 16 channel entries (15 to 0)', align=Align.INLINE)
d.comment(0x950B, 'Pop accumulator', align=Align.INLINE)
d.comment(0x950C, 'OR in channel status bits', align=Align.INLINE)
d.comment(0x950F, 'Push updated accumulator', align=Align.INLINE)
d.comment(0x9510, 'Load channel status', align=Align.INLINE)
d.comment(0x9513, 'Keep only bits 6-7 (close flags)', align=Align.INLINE)
d.comment(0x9515, 'Clear data bits, keep state flags', align=Align.INLINE)
d.comment(0x9518, 'Next channel', align=Align.INLINE)
d.comment(0x9519, 'Loop all 16 channels', align=Align.INLINE)
d.comment(0x951B, 'Close all network channels', align=Align.INLINE)
d.comment(0x951E, 'Pop data-loss accumulator', align=Align.INLINE)
d.comment(0x951F, 'Bit 0 to carry (data lost?)', align=Align.INLINE)
d.comment(0x9520, 'No data lost: skip message', align=Align.INLINE)
d.comment(0x9522, "Print 'Data Lost' + CR", align=Align.INLINE)
d.comment(0x952F, 'Reload reply status code', align=Align.INLINE)
d.comment(0x9532, 'Check pending operation', align=Align.INLINE)
d.comment(0x9535, 'No pending: build error from reply', align=Align.INLINE)
d.comment(0x9537, 'Pending: clean up stack (3 bytes)', align=Align.INLINE)
d.comment(0x9538, '(second byte)', align=Align.INLINE)
d.comment(0x9539, '(third byte)', align=Align.INLINE)
d.comment(0x953A, 'Return to pending operation caller', align=Align.INLINE)
d.comment(0x953B, 'Y=1: error code offset in reply', align=Align.INLINE)
d.comment(0x953D, 'Reply code >= &A8?', align=Align.INLINE)
d.comment(0x953F, 'Yes: keep server error code', align=Align.INLINE)
d.comment(0x9541, 'No: use minimum error code &A8', align=Align.INLINE)
d.comment(0x9543, 'Overwrite error code in reply', align=Align.INLINE)
d.comment(0x9545, 'Y=&FF: pre-increment index', align=Align.INLINE)
d.comment(0x9547, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9548, 'Load reply byte', align=Align.INLINE)
d.comment(0x954A, 'Copy to error block', align=Align.INLINE)
d.comment(0x954D, 'Is it CR (end of message)?', align=Align.INLINE)
d.comment(0x954F, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9551, 'Store null terminator (A=0 from EOR)', align=Align.INLINE)
d.comment(0x9554, 'Get message length', align=Align.INLINE)
d.comment(0x9555, 'Transfer to A', align=Align.INLINE)
d.comment(0x9556, 'Length in X', align=Align.INLINE)
d.comment(0x9557, 'Go to error dispatch', align=Align.INLINE)
d.comment(0x955A, 'Load MOS escape flag', align=Align.INLINE)
d.comment(0x955C, 'Mask with escape-enabled flag', align=Align.INLINE)
d.comment(0x955E, 'No escape: return', align=Align.INLINE)
d.comment(0x9560, 'OSBYTE &7E: acknowledge escape', align=Align.INLINE)
d.comment(0x9565, 'Error class 6: Escape', align=Align.INLINE)
d.comment(0x9567, 'Classify as network error', align=Align.INLINE)
d.comment(0x956A, 'Offset 4: remote state byte', align=Align.INLINE)
d.comment(0x956C, 'Load remote state', align=Align.INLINE)
d.comment(0x956E, 'Zero: initialise remote session', align=Align.INLINE)
d.comment(0x9570, 'Non-zero: commit state and return', align=Align.INLINE)
d.comment(0x9573, 'Set bits 0,3: remote active flags', align=Align.INLINE)
d.comment(0x9575, 'Store updated remote state', align=Align.INLINE)
d.comment(0x9577, 'X=&80: flag for vector setup', align=Align.INLINE)
d.comment(0x9579, 'Offset &80 in RX buffer', align=Align.INLINE)
d.comment(0x957B, 'Load remote station low', align=Align.INLINE)
d.comment(0x957D, 'Save on stack', align=Align.INLINE)
d.comment(0x957F, 'Load remote station high', align=Align.INLINE)
d.comment(0x9581, 'Workspace offset &0F', align=Align.INLINE)
d.comment(0x9583, 'Store remote station high', align=Align.INLINE)
d.comment(0x9585, 'Y=&0E', align=Align.INLINE)
d.comment(0x9586, 'Restore remote station low', align=Align.INLINE)
d.comment(0x9587, 'Store remote station low', align=Align.INLINE)
d.comment(0x9589, 'Set up remote keyboard scanning', align=Align.INLINE)
d.comment(0x958C, 'Initialise workspace copy', align=Align.INLINE)
d.comment(0x958F, 'X=1: disable keyboard', align=Align.INLINE)
d.comment(0x9591, 'Y=0', align=Align.INLINE)
d.comment(0x9593, 'OSBYTE &C9: Econet keyboard disable', align=Align.INLINE)
d.comment(0x9598, 'Commit state change', align=Align.INLINE)
d.comment(0x959B, 'Error code 0', align=Align.INLINE)
d.comment(0x959D, "Generate 'Remoted' error", align=Align.INLINE)
d.comment(0x95A8, 'Offset 4: remote state byte', align=Align.INLINE)
d.comment(0x95AA, 'Load remote state', align=Align.INLINE)
d.comment(0x95AC, 'Zero: reinitialise session', align=Align.INLINE)
d.comment(0x95AE, 'Offset &80: station low', align=Align.INLINE)
d.comment(0x95B0, 'Load station low from RX', align=Align.INLINE)
d.comment(0x95B2, 'Workspace offset &0E', align=Align.INLINE)
d.comment(0x95B4, 'Compare with stored station', align=Align.INLINE)
d.comment(0x95B6, 'Different station: commit state', align=Align.INLINE)
d.comment(0x95B8, 'Offset &82: keypress byte', align=Align.INLINE)
d.comment(0x95BA, 'Load remote keypress', align=Align.INLINE)
d.comment(0x95BC, 'Key code to Y', align=Align.INLINE)
d.comment(0x95BD, 'X=0: keyboard buffer', align=Align.INLINE)
d.comment(0x95BF, 'Commit state change', align=Align.INLINE)
d.comment(0x95C2, 'OSBYTE &99: insert into buffer', align=Align.INLINE)
d.comment(0x95C7, 'Save TX timeout counter', align=Align.INLINE)
d.comment(0x95CA, 'Push (used as outer loop counter)', align=Align.INLINE)
d.comment(0x95CB, 'Save TX control state', align=Align.INLINE)
d.comment(0x95CE, 'Push (preserved during wait)', align=Align.INLINE)
d.comment(0x95CF, 'Check if TX in progress', align=Align.INLINE)
d.comment(0x95D1, 'Non-zero: skip force-wait', align=Align.INLINE)
d.comment(0x95D3, 'Set bit 7 to force wait mode', align=Align.INLINE)
d.comment(0x95D5, 'Store updated control state', align=Align.INLINE)
d.comment(0x95D8, 'A=0: initial counter values', align=Align.INLINE)
d.comment(0x95DA, 'Push inner loop counter', align=Align.INLINE)
d.comment(0x95DB, 'Push middle loop counter', align=Align.INLINE)
d.comment(0x95DD, 'X=SP for stack-relative DECs', align=Align.INLINE)
d.comment(0x95DE, 'Poll TX completion status', align=Align.INLINE)
d.comment(0x95E0, 'Bit 7 set: TX complete', align=Align.INLINE)
d.comment(0x95E2, 'Decrement inner counter', align=Align.INLINE)
d.comment(0x95E5, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x95E7, 'Decrement middle counter', align=Align.INLINE)
d.comment(0x95EA, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x95EC, 'Decrement outer counter', align=Align.INLINE)
d.comment(0x95EF, 'Not zero: keep polling', align=Align.INLINE)
d.comment(0x95F1, 'Discard inner counter', align=Align.INLINE)
d.comment(0x95F2, 'Discard middle counter', align=Align.INLINE)
d.comment(0x95F3, 'Restore l0d61 control state', align=Align.INLINE)
d.comment(0x95F4, 'Write back TX control state', align=Align.INLINE)
d.comment(0x95F7, 'Pop outer counter (0 if timed out)', align=Align.INLINE)
d.comment(0x95F8, 'Zero: TX timed out', align=Align.INLINE)
d.comment(0x95FA, 'Return (TX acknowledged)', align=Align.INLINE)
d.comment(0x95FB, 'Test error logging flag', align=Align.INLINE)
d.comment(0x95FE, 'Bit 7 clear: skip save', align=Align.INLINE)
d.comment(0x9600, 'Save error code to workspace', align=Align.INLINE)
d.comment(0x9603, 'Return', align=Align.INLINE)
d.comment(0x9604, "X=8: 'No reply' error index", align=Align.INLINE)
d.comment(0x9606, 'Look up message table offset', align=Align.INLINE)
d.comment(0x9609, 'X=0: error text start', align=Align.INLINE)
d.comment(0x960B, 'Clear BRK byte in error block', align=Align.INLINE)
d.comment(0x960E, 'Load error number from table', align=Align.INLINE)
d.comment(0x9611, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x9614, 'Load message byte', align=Align.INLINE)
d.comment(0x9617, 'Store in error text buffer', align=Align.INLINE)
d.comment(0x961A, 'Null terminator?', align=Align.INLINE)
d.comment(0x961C, 'Advance destination', align=Align.INLINE)
d.comment(0x961D, 'Advance source', align=Align.INLINE)
d.comment(0x961E, 'Loop until end of message', align=Align.INLINE)
d.comment(0x9620, "Append ' net.station' to message", align=Align.INLINE)
d.comment(0x9623, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x9625, 'Terminate error text', align=Align.INLINE)
d.comment(0x9628, 'Check and raise network error', align=Align.INLINE)
d.comment(0x962B, 'Load first reply byte', align=Align.INLINE)
d.comment(0x962D, "Is it 'A' (status &41)?", align=Align.INLINE)
d.comment(0x962F, 'No: keep original', align=Align.INLINE)
d.comment(0x9631, "Yes: change to 'B' (&42)", align=Align.INLINE)
d.comment(0x9633, 'Clear V flag', align=Align.INLINE)
d.comment(0x9636, 'Load first reply byte', align=Align.INLINE)
d.comment(0x9638, 'Set V flag (via BIT &FF)', align=Align.INLINE)
d.comment(0x963B, 'Mask to error class (0-7)', align=Align.INLINE)
d.comment(0x963D, 'Save error class on stack', align=Align.INLINE)
d.comment(0x963E, 'Class 2 (station error)?', align=Align.INLINE)
d.comment(0x9640, 'No: build simple error message', align=Align.INLINE)
d.comment(0x9642, 'Save flags (V state for suffix)', align=Align.INLINE)
d.comment(0x9643, 'Error class to X', align=Align.INLINE)
d.comment(0x9644, 'Look up message table offset', align=Align.INLINE)
d.comment(0x9647, 'Load error number from table', align=Align.INLINE)
d.comment(0x964A, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x964D, 'X=0: error text start', align=Align.INLINE)
d.comment(0x964F, 'Clear BRK byte', align=Align.INLINE)
d.comment(0x9652, 'Load message byte', align=Align.INLINE)
d.comment(0x9655, 'Store in error text', align=Align.INLINE)
d.comment(0x9658, 'Null terminator?', align=Align.INLINE)
d.comment(0x965A, 'Advance source', align=Align.INLINE)
d.comment(0x965B, 'Advance destination', align=Align.INLINE)
d.comment(0x965C, 'Loop until end of message', align=Align.INLINE)
d.comment(0x965E, "Append ' net.station' suffix", align=Align.INLINE)
d.comment(0x9661, 'Restore flags', align=Align.INLINE)
d.comment(0x9662, "V set: append 'not listening'", align=Align.INLINE)
d.comment(0x9664, 'Error code &A4', align=Align.INLINE)
d.comment(0x9666, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x9669, 'Replace error number in block', align=Align.INLINE)
d.comment(0x966C, "Y=&0B: 'not present' suffix index", align=Align.INLINE)
d.comment(0x9670, "Y=9: 'not listening' suffix index", align=Align.INLINE)
d.comment(0x9672, 'Look up suffix table offset', align=Align.INLINE)
d.comment(0x9675, 'Offset to Y for indexing', align=Align.INLINE)
d.comment(0x9676, 'Load suffix byte', align=Align.INLINE)
d.comment(0x9679, 'Append to error text', align=Align.INLINE)
d.comment(0x967C, 'Null terminator?', align=Align.INLINE)
d.comment(0x967E, 'Advance source', align=Align.INLINE)
d.comment(0x967F, 'Advance destination', align=Align.INLINE)
d.comment(0x9680, 'Loop until end of suffix', align=Align.INLINE)
d.comment(0x9682, 'ALWAYS branch to error dispatch', align=Align.INLINE)
d.comment(0x9684, 'Error class to X', align=Align.INLINE)
d.comment(0x9685, 'Look up message table offset', align=Align.INLINE)
d.comment(0x9688, 'X=0: error text start', align=Align.INLINE)
d.comment(0x968A, 'Clear BRK byte', align=Align.INLINE)
d.comment(0x968D, 'Load error number from table', align=Align.INLINE)
d.comment(0x9690, 'Conditionally save error code', align=Align.INLINE)
d.comment(0x9693, 'Load message byte', align=Align.INLINE)
d.comment(0x9696, 'Store in error text', align=Align.INLINE)
d.comment(0x9699, 'Null terminator? Go to error', align=Align.INLINE)
d.comment(0x969B, 'Advance source', align=Align.INLINE)
d.comment(0x969C, 'Advance destination', align=Align.INLINE)
d.comment(0x969D, 'Loop until end of message', align=Align.INLINE)
d.comment(0xA063, 'Load current FS station high', align=Align.INLINE)
d.comment(0xA066, 'Save to fs_work_5', align=Align.INLINE)
d.comment(0xA068, 'Load current FS station low', align=Align.INLINE)
d.comment(0xA06B, 'Save to l00b6', align=Align.INLINE)
d.comment(0xA06D, 'Get first character of argument', align=Align.INLINE)
d.comment(0xA06F, 'Is it CR (no argument)?', align=Align.INLINE)
d.comment(0xA071, 'No arg: print current FS info', align=Align.INLINE)
d.comment(0xA073, 'Parse FS/PS station arguments', align=Align.INLINE)
d.comment(0xA076, 'A=1: write NFS info', align=Align.INLINE)
d.comment(0xA078, 'Store OSWORD sub-function', align=Align.INLINE)
d.comment(0xA07A, 'OSWORD &13: NFS information', align=Align.INLINE)
d.comment(0xA07C, 'Parameter block low', align=Align.INLINE)
d.comment(0xA07E, 'Parameter block high', align=Align.INLINE)
d.comment(0xA083, "Print 'File server '", align=Align.INLINE)
d.comment(0xA086, 'Set V (suppress padding)', align=Align.INLINE)
d.comment(0xA089, 'Print station address', align=Align.INLINE)
d.comment(0xA08F, 'Save X on stack', align=Align.INLINE)
d.comment(0xA090, 'Push X', align=Align.INLINE)
d.comment(0xA091, 'A=0: initialise dot-seen flag', align=Align.INLINE)
d.comment(0xA093, 'Clear dot-seen flag', align=Align.INLINE)
d.comment(0xA095, 'Parse first number (network)', align=Align.INLINE)
d.comment(0xA098, 'C set: number found, check for dot', align=Align.INLINE)
d.comment(0xA09A, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0xA09B, 'Push Y', align=Align.INLINE)
d.comment(0xA09C, 'Initialise bridge polling', align=Align.INLINE)
d.comment(0xA09F, 'Compare bridge result with parsed value', align=Align.INLINE)
d.comment(0xA0A1, 'Same: keep bridge result', align=Align.INLINE)
d.comment(0xA0A3, 'Different: use parsed value', align=Align.INLINE)
d.comment(0xA0A5, 'Store station low byte', align=Align.INLINE)
d.comment(0xA0A7, 'Restore Y', align=Align.INLINE)
d.comment(0xA0A8, 'Transfer back to Y', align=Align.INLINE)
d.comment(0xA0A9, 'Skip dot separator', align=Align.INLINE)
d.comment(0xA0AA, 'Parse second number (station)', align=Align.INLINE)
d.comment(0xA0AD, 'Zero result: skip store', align=Align.INLINE)
d.comment(0xA0AF, 'Store station high byte', align=Align.INLINE)
d.comment(0xA0B1, 'Restore X', align=Align.INLINE)
d.comment(0xA0B2, 'Transfer back to X', align=Align.INLINE)
d.comment(0xA0B3, 'Return', align=Align.INLINE)
d.comment(0xA0B4, 'Load parameter block pointer', align=Align.INLINE)
d.comment(0xA0B6, 'Shift left (A * 2)', align=Align.INLINE)
d.comment(0xA0B7, 'Shift left (A * 4)', align=Align.INLINE)
d.comment(0xA0B8, 'Save A * 4 on stack', align=Align.INLINE)
d.comment(0xA0B9, 'Shift left (A * 8)', align=Align.INLINE)
d.comment(0xA0BA, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA0BB, 'Save flags (carry from shift)', align=Align.INLINE)
d.comment(0xA0BC, 'A*8 + A*4 (from stack) = A*12', align=Align.INLINE)
d.comment(0xA0BF, 'Divide by 2 with carry', align=Align.INLINE)
d.comment(0xA0C0, 'Restore original flags', align=Align.INLINE)
d.comment(0xA0C1, 'Shift left again', align=Align.INLINE)
d.comment(0xA0C2, 'Result to Y as index', align=Align.INLINE)
d.comment(0xA0C3, 'Pop saved A * 4', align=Align.INLINE)
d.comment(0xA0C4, 'A * 4 >= &48 (out of range)?', align=Align.INLINE)
d.comment(0xA0C6, 'In range: return', align=Align.INLINE)
d.comment(0xA0C8, 'Out of range: Y=0', align=Align.INLINE)
d.comment(0xA0CA, 'A=&00', align=Align.INLINE)
d.comment(0xA0CB, 'Return with A=index, Y=index', align=Align.INLINE)
d.comment(0xA0CC, 'Y=&6F: source offset', align=Align.INLINE)
d.comment(0xA0CE, 'Load byte from RX buffer', align=Align.INLINE)
d.comment(0xA0D0, 'C clear: store directly', align=Align.INLINE)
d.comment(0xA0D2, 'Get index from PB pointer', align=Align.INLINE)
d.comment(0xA0D5, 'C set (out of range): clear value', align=Align.INLINE)
d.comment(0xA0D7, 'Load workspace byte at index', align=Align.INLINE)
d.comment(0xA0D9, "Is it '?' (uninitialised)?", align=Align.INLINE)
d.comment(0xA0DB, 'No: use value from RX buffer', align=Align.INLINE)
d.comment(0xA0DD, 'A=0: return zero for uninitialised', align=Align.INLINE)
d.comment(0xA0DF, 'Store result to PB pointer', align=Align.INLINE)
d.comment(0xA0E1, 'Return', align=Align.INLINE)
d.comment(0xA0E2, 'Get index from PB pointer', align=Align.INLINE)
d.comment(0xA0E5, 'C clear: store to workspace', align=Align.INLINE)
d.comment(0xA0E7, 'Save carry to l0d6c bit 7', align=Align.INLINE)
d.comment(0xA0EA, 'Load PB pointer value', align=Align.INLINE)
d.comment(0xA0EC, 'Shift carry back in', align=Align.INLINE)
d.comment(0xA0ED, 'Restore l0d6c bit 7', align=Align.INLINE)
d.comment(0xA0F0, 'Return', align=Align.INLINE)
d.comment(0xA0F1, 'Save carry to l0d61 bit 7', align=Align.INLINE)
d.comment(0xA0F4, "A='?': mark as uninitialised", align=Align.INLINE)
d.comment(0xA0F6, "Store '?' to workspace", align=Align.INLINE)
d.comment(0xA0F8, 'Restore l0d61 bit 7', align=Align.INLINE)
d.comment(0xA0FB, 'Return', align=Align.INLINE)
d.comment(0xA0FC, 'Set text and transfer pointers', align=Align.INLINE)
d.comment(0xA0FF, 'Y=&FF: prepare for INY to 0', align=Align.INLINE)
d.comment(0xA101, 'Clear spool handle (no spool active)', align=Align.INLINE)
d.comment(0xA103, 'Set escapable flag (&FF)', align=Align.INLINE)
d.comment(0xA106, 'X=&4A: FS command table offset', align=Align.INLINE)
d.comment(0xA108, 'Match command in FS table', align=Align.INLINE)
d.comment(0xA10B, 'C set: command found', align=Align.INLINE)
d.comment(0xA10D, 'V clear: syntax error', align=Align.INLINE)
d.comment(0xA10F, 'Error code &DC', align=Align.INLINE)
d.comment(0xA111, "Generate 'Syntax' error", align=Align.INLINE)
d.comment(0xA11B, 'A=0: clear service state', align=Align.INLINE)
d.comment(0xA11D, 'Store cleared service state', align=Align.INLINE)
d.comment(0xA11F, 'Load command handler address high', align=Align.INLINE)
d.comment(0xA122, 'Push high byte', align=Align.INLINE)
d.comment(0xA123, 'Load command handler address low', align=Align.INLINE)
d.comment(0xA126, 'Push low byte', align=Align.INLINE)
d.comment(0xA127, 'RTS dispatches to command handler', align=Align.INLINE)
d.comment(0xA128, 'Save Y (command line offset)', align=Align.INLINE)
d.comment(0xA129, 'Push on stack', align=Align.INLINE)
d.comment(0xA12A, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA12B, 'Push back (keep on stack)', align=Align.INLINE)
d.comment(0xA12C, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA12D, 'Load table entry byte', align=Align.INLINE)
d.comment(0xA130, 'Bit 7 set: end of table names', align=Align.INLINE)
d.comment(0xA132, 'Load table byte', align=Align.INLINE)
d.comment(0xA135, 'Bit 7 set: end of this name', align=Align.INLINE)
d.comment(0xA137, 'Compare with command line char', align=Align.INLINE)
d.comment(0xA139, 'Case-insensitive compare', align=Align.INLINE)
d.comment(0xA13B, 'Mismatch: skip to next entry', align=Align.INLINE)
d.comment(0xA13D, 'Match: advance command line', align=Align.INLINE)
d.comment(0xA13E, 'Advance table pointer', align=Align.INLINE)
d.comment(0xA13F, 'Loop for next character', align=Align.INLINE)
d.comment(0xA141, 'Advance past remaining table chars', align=Align.INLINE)
d.comment(0xA142, 'Load next table byte', align=Align.INLINE)
d.comment(0xA145, 'Bit 7 clear: more chars to skip', align=Align.INLINE)
d.comment(0xA147, 'Check command line terminator', align=Align.INLINE)
d.comment(0xA149, "Is it '.' (abbreviation)?", align=Align.INLINE)
d.comment(0xA14B, 'Yes: skip spaces after dot', align=Align.INLINE)
d.comment(0xA14D, 'X += 3: skip flags and address bytes', align=Align.INLINE)
d.comment(0xA14E, '(continued)', align=Align.INLINE)
d.comment(0xA14F, '(continued)', align=Align.INLINE)
d.comment(0xA150, 'Try next table entry', align=Align.INLINE)
d.comment(0xA152, 'Save Y (end of matched name)', align=Align.INLINE)
d.comment(0xA153, 'Push position', align=Align.INLINE)
d.comment(0xA154, 'Load char after matched portion', align=Align.INLINE)
d.comment(0xA156, 'Y=9: check 10 separator chars', align=Align.INLINE)
d.comment(0xA158, 'Compare with separator table', align=Align.INLINE)
d.comment(0xA15B, 'Match: valid command separator', align=Align.INLINE)
d.comment(0xA15D, 'Try next separator', align=Align.INLINE)
d.comment(0xA15E, 'Loop through separator list', align=Align.INLINE)
d.comment(0xA160, 'No separator match: restore Y', align=Align.INLINE)
d.comment(0xA161, 'Transfer back to Y', align=Align.INLINE)
d.comment(0xA162, 'Try next table entry', align=Align.INLINE)
d.comment(0xA164, """Command separator table (9 bytes)

Characters that terminate a command name in the
star command parser. loop_check_sep_table scans
Y down from 8 to 0, comparing each input char
against this table.""")
d.comment(0xA164, 'Space', align=Align.INLINE)
d.comment(0xA165, '\'"\' double quote', align=Align.INLINE)
d.comment(0xA166, "'#' hash", align=Align.INLINE)
d.comment(0xA167, "'$' dollar", align=Align.INLINE)
d.comment(0xA168, "'&' ampersand", align=Align.INLINE)
d.comment(0xA169, "'*' asterisk", align=Align.INLINE)
d.comment(0xA16A, "':' colon", align=Align.INLINE)
d.comment(0xA16B, "'@' at-sign", align=Align.INLINE)
d.comment(0xA16C, 'CR (carriage return)', align=Align.INLINE)
d.comment(0xA16D, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA16E, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA16F, 'Load next char', align=Align.INLINE)
d.comment(0xA171, 'Is it space?', align=Align.INLINE)
d.comment(0xA173, 'No: done skipping', align=Align.INLINE)
d.comment(0xA175, 'Advance past space', align=Align.INLINE)
d.comment(0xA176, 'Loop for more spaces', align=Align.INLINE)
d.comment(0xA179, 'Load command flags byte', align=Align.INLINE)
d.comment(0xA17C, "Shift: check 'no-arg' bit", align=Align.INLINE)
d.comment(0xA17D, 'Bit clear: allow arguments', align=Align.INLINE)
d.comment(0xA17F, 'Check if line ends here', align=Align.INLINE)
d.comment(0xA181, 'Is it CR?', align=Align.INLINE)
d.comment(0xA183, 'No: argument present, V clear', align=Align.INLINE)
d.comment(0xA185, 'CR found: set V (no argument)', align=Align.INLINE)
d.comment(0xA188, 'V set: command is valid', align=Align.INLINE)
d.comment(0xA18A, 'Clear V (argument present)', align=Align.INLINE)
d.comment(0xA18B, 'C=0: command not found', align=Align.INLINE)
d.comment(0xA18C, 'Pop saved Y from stack', align=Align.INLINE)
d.comment(0xA18D, 'Load command line char at Y', align=Align.INLINE)
d.comment(0xA18F, 'Return (C and V set per result)', align=Align.INLINE)
d.comment(0xA190, 'Advance past character', align=Align.INLINE)
d.comment(0xA191, 'Load current char', align=Align.INLINE)
d.comment(0xA193, 'Is it CR (end of line)?', align=Align.INLINE)
d.comment(0xA195, 'Yes: end of input', align=Align.INLINE)
d.comment(0xA197, "Is it '.' (abbreviation dot)?", align=Align.INLINE)
d.comment(0xA199, 'Yes: skip to next word', align=Align.INLINE)
d.comment(0xA19B, 'Is it space?', align=Align.INLINE)
d.comment(0xA19D, 'No: keep scanning', align=Align.INLINE)
d.comment(0xA19F, 'Skip past separator', align=Align.INLINE)
d.comment(0xA1A0, 'Load next char', align=Align.INLINE)
d.comment(0xA1A2, 'Is it space?', align=Align.INLINE)
d.comment(0xA1A4, 'Yes: skip consecutive spaces', align=Align.INLINE)
d.comment(0xA1A6, 'C=1: have more text to match', align=Align.INLINE)
d.comment(0xA1A9, 'Save text pointer', align=Align.INLINE)
d.comment(0xA1AC, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA1AF, 'Parse command argument (Y=0)', align=Align.INLINE)
d.comment(0xA1B2, 'X=1: buffer index', align=Align.INLINE)
d.comment(0xA1B4, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xA1B7, 'A=2: open for update', align=Align.INLINE)
d.comment(0xA1B9, 'Store open mode', align=Align.INLINE)
d.comment(0xA1BC, 'Y=&12: open file command', align=Align.INLINE)
d.comment(0xA1BE, 'Send open request to server', align=Align.INLINE)
d.comment(0xA1C1, 'Load reply status', align=Align.INLINE)
d.comment(0xA1C4, 'Status 1 (success)?', align=Align.INLINE)
d.comment(0xA1C6, 'No: file not found, try library', align=Align.INLINE)
d.comment(0xA1C8, 'X=3: check 4 handle bytes', align=Align.INLINE)
d.comment(0xA1CA, 'Increment handle byte', align=Align.INLINE)
d.comment(0xA1CD, 'Was &FF (overflow to 0): try next', align=Align.INLINE)
d.comment(0xA1CF, 'Non-zero: handle valid, execute', align=Align.INLINE)
d.comment(0xA1D2, 'Try next handle byte', align=Align.INLINE)
d.comment(0xA1D3, 'Loop until all checked', align=Align.INLINE)
d.comment(0xA1D5, 'Allocate new FCB or raise error', align=Align.INLINE)
d.comment(0xA1D8, 'X=1: open mode index', align=Align.INLINE)
d.comment(0xA1DA, 'Store in l0f05', align=Align.INLINE)
d.comment(0xA1DD, 'Store in l0f06', align=Align.INLINE)
d.comment(0xA1E0, 'X=2', align=Align.INLINE)
d.comment(0xA1E1, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0xA1E4, 'Y=6: re-open command', align=Align.INLINE)
d.comment(0xA1E6, 'Send re-open request', align=Align.INLINE)
d.comment(0xA1E9, 'C set: error on re-open', align=Align.INLINE)
d.comment(0xA1EB, 'C clear: finalise file opening', align=Align.INLINE)
d.comment(0xA1EE, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0xA1F1, 'Load first char of filename', align=Align.INLINE)
d.comment(0xA1F4, "Is it '$' (root dir)?", align=Align.INLINE)
d.comment(0xA1F6, 'Yes: no library search, error', align=Align.INLINE)
d.comment(0xA1F8, 'Load library flag byte', align=Align.INLINE)
d.comment(0xA1FB, 'Bit 7 set: library already tried', align=Align.INLINE)
d.comment(0xA1FD, 'Rotate bits to check library state', align=Align.INLINE)
d.comment(0xA1FE, 'Rotate again', align=Align.INLINE)
d.comment(0xA1FF, 'Bit 7 set: restore from backup', align=Align.INLINE)
d.comment(0xA201, 'Carry set: bad command', align=Align.INLINE)
d.comment(0xA203, 'X=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0xA205, 'Find end of filename', align=Align.INLINE)
d.comment(0xA206, 'Load filename byte', align=Align.INLINE)
d.comment(0xA209, 'Is it CR (end)?', align=Align.INLINE)
d.comment(0xA20B, 'No: continue scanning', align=Align.INLINE)
d.comment(0xA20D, 'Shift filename right by 8 bytes', align=Align.INLINE)
d.comment(0xA210, 'Store shifted byte', align=Align.INLINE)
d.comment(0xA213, 'Previous byte', align=Align.INLINE)
d.comment(0xA214, 'Loop until all shifted', align=Align.INLINE)
d.comment(0xA216, "X=7: 'Library.' is 8 bytes", align=Align.INLINE)
d.comment(0xA218, "Copy 'Library.' prefix", align=Align.INLINE)
d.comment(0xA21B, 'Store prefix byte', align=Align.INLINE)
d.comment(0xA21E, 'Previous byte', align=Align.INLINE)
d.comment(0xA21F, 'Loop until prefix copied', align=Align.INLINE)
d.comment(0xA221, 'Load library flag', align=Align.INLINE)
d.comment(0xA224, 'Set bits 5-6: library path active', align=Align.INLINE)
d.comment(0xA226, 'Store updated flag', align=Align.INLINE)
d.comment(0xA229, 'Retry file open with library path', align=Align.INLINE)
d.comment(0xA22B, 'X=&FF: pre-increment for loop', align=Align.INLINE)
d.comment(0xA22D, 'Restore original filename', align=Align.INLINE)
d.comment(0xA22E, 'Load backup byte', align=Align.INLINE)
d.comment(0xA231, 'Store to filename buffer', align=Align.INLINE)
d.comment(0xA234, 'Is it CR (end)?', align=Align.INLINE)
d.comment(0xA236, 'No: continue restoring', align=Align.INLINE)
d.comment(0xA238, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA23B, 'Set bit 7: library tried', align=Align.INLINE)
d.comment(0xA23D, 'Store updated flag', align=Align.INLINE)
d.comment(0xA242, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0xA245, 'Error code &FE', align=Align.INLINE)
d.comment(0xA247, "Generate 'Bad command' error", align=Align.INLINE)
d.comment(0xA252, 'X=3: check 4 execution bytes', align=Align.INLINE)
d.comment(0xA254, 'Increment execution address byte', align=Align.INLINE)
d.comment(0xA257, 'Non-zero: valid, go to OSCLI', align=Align.INLINE)
d.comment(0xA259, 'Try next byte', align=Align.INLINE)
d.comment(0xA25A, 'Loop until all checked', align=Align.INLINE)
d.comment(0xA25C, 'Error code &93', align=Align.INLINE)
d.comment(0xA25E, "Generate 'No!' error", align=Align.INLINE)
d.comment(0xA265, 'Load open mode result', align=Align.INLINE)
d.comment(0xA268, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA26B, 'Transfer to Y', align=Align.INLINE)
d.comment(0xA26C, 'A=0: clear channel status', align=Align.INLINE)
d.comment(0xA26E, 'Clear status in channel table', align=Align.INLINE)
d.comment(0xA271, 'Store handle in l1070', align=Align.INLINE)
d.comment(0xA274, 'Y=3: OSCLI execution', align=Align.INLINE)
d.comment(0xA276, 'Execute via boot/OSCLI path', align=Align.INLINE)
d.comment(0xA281, 'Copy argument to buffer (X=0)', align=Align.INLINE)
d.comment(0xA284, 'Y=0', align=Align.INLINE)
d.comment(0xA286, 'C=0 for GSINIT', align=Align.INLINE)
d.comment(0xA287, 'Initialise GS string read', align=Align.INLINE)
d.comment(0xA28A, 'Read next GS character', align=Align.INLINE)
d.comment(0xA28D, 'C clear: more chars', align=Align.INLINE)
d.comment(0xA28F, 'Back up one position', align=Align.INLINE)
d.comment(0xA290, 'Skip trailing spaces', align=Align.INLINE)
d.comment(0xA291, 'Load next char', align=Align.INLINE)
d.comment(0xA293, 'Is it space?', align=Align.INLINE)
d.comment(0xA295, 'Yes: skip it', align=Align.INLINE)
d.comment(0xA297, 'Check for CR (end of line)', align=Align.INLINE)
d.comment(0xA299, 'C=0 for addition', align=Align.INLINE)
d.comment(0xA29A, 'Transfer Y offset to A', align=Align.INLINE)
d.comment(0xA29B, 'Add to text pointer low', align=Align.INLINE)
d.comment(0xA29D, 'Store as command tail pointer low', align=Align.INLINE)
d.comment(0xA2A0, 'Load text pointer high', align=Align.INLINE)
d.comment(0xA2A2, 'Add carry', align=Align.INLINE)
d.comment(0xA2A4, 'Store as command tail pointer high', align=Align.INLINE)
d.comment(0xA2A7, 'Save text pointer for later', align=Align.INLINE)
d.comment(0xA2AA, 'X=&0E: OSWORD parameter offset', align=Align.INLINE)
d.comment(0xA2AC, 'Store as block offset high', align=Align.INLINE)
d.comment(0xA2AE, 'A=&10: OSWORD parameter size', align=Align.INLINE)
d.comment(0xA2B0, 'Store as options pointer', align=Align.INLINE)
d.comment(0xA2B2, 'Store to l0e16', align=Align.INLINE)
d.comment(0xA2B5, 'X=&4A: FS command table offset', align=Align.INLINE)
d.comment(0xA2B7, 'Y=5', align=Align.INLINE)
d.comment(0xA2B9, 'Execute FS command iteration', align=Align.INLINE)
d.comment(0xA2BC, 'Load tube flag', align=Align.INLINE)
d.comment(0xA2BF, 'Zero: no tube transfer needed', align=Align.INLINE)
d.comment(0xA2C1, 'AND with l0f0b', align=Align.INLINE)
d.comment(0xA2C4, 'AND with l0f0c', align=Align.INLINE)
d.comment(0xA2C7, 'All &FF?', align=Align.INLINE)
d.comment(0xA2C9, 'Yes: no tube transfer needed', align=Align.INLINE)
d.comment(0xA2CB, 'Claim tube for data transfer', align=Align.INLINE)
d.comment(0xA2CE, 'X=9: parameter count', align=Align.INLINE)
d.comment(0xA2D0, 'Y=&0F: parameter offset', align=Align.INLINE)
d.comment(0xA2D2, 'A=4: tube transfer type', align=Align.INLINE)
d.comment(0xA2D4, 'Dispatch tube address/data', align=Align.INLINE)
d.comment(0xA2D7, 'A=1', align=Align.INLINE)
d.comment(0xA2D9, 'Dispatch via indirect vector', align=Align.INLINE)
d.comment(0xA2DC, 'Find station with bit 3 set', align=Align.INLINE)
d.comment(0xA2DF, 'Return with last flag state', align=Align.INLINE)
d.comment(0xA2E2, 'Flip/set station boot config', align=Align.INLINE)
d.comment(0xA2E5, 'Return with last flag state', align=Align.INLINE)
d.comment(0xA2E8, 'X=&10: scan 16 slots (15 to 0)', align=Align.INLINE)
d.comment(0xA2EA, 'Clear V', align=Align.INLINE)
d.comment(0xA2EB, 'Try next slot', align=Align.INLINE)
d.comment(0xA2EC, 'All slots checked: not found', align=Align.INLINE)
d.comment(0xA2EE, 'Compare station/network', align=Align.INLINE)
d.comment(0xA2F1, 'No match: try next', align=Align.INLINE)
d.comment(0xA2F3, 'Load slot status byte', align=Align.INLINE)
d.comment(0xA2F6, 'Test bit 2 (PS active flag)?', align=Align.INLINE)
d.comment(0xA2F8, 'Not set: try next', align=Align.INLINE)
d.comment(0xA2FA, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA2FB, 'Store Y in slot data', align=Align.INLINE)
d.comment(0xA2FE, 'Set V (found match)', align=Align.INLINE)
d.comment(0xA301, 'Store Y to l0e02', align=Align.INLINE)
d.comment(0xA304, 'V set: found, skip allocation', align=Align.INLINE)
d.comment(0xA306, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA307, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA30A, 'Store allocation result', align=Align.INLINE)
d.comment(0xA30D, 'Zero: failed, restore context', align=Align.INLINE)
d.comment(0xA30F, 'A=&26: station flags value', align=Align.INLINE)
d.comment(0xA313, 'X=&10: scan 16 slots (15 to 0)', align=Align.INLINE)
d.comment(0xA315, 'Clear V', align=Align.INLINE)
d.comment(0xA316, 'Try next slot', align=Align.INLINE)
d.comment(0xA317, 'All slots checked: not found', align=Align.INLINE)
d.comment(0xA319, 'Compare station/network', align=Align.INLINE)
d.comment(0xA31C, 'No match: try next', align=Align.INLINE)
d.comment(0xA31E, 'Load slot status byte', align=Align.INLINE)
d.comment(0xA321, 'Test bit 3 (FS active flag)?', align=Align.INLINE)
d.comment(0xA323, 'Not set: try next', align=Align.INLINE)
d.comment(0xA325, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA326, 'Store Y in slot data', align=Align.INLINE)
d.comment(0xA329, 'Set V (found match)', align=Align.INLINE)
d.comment(0xA32C, 'Store Y to l0e03', align=Align.INLINE)
d.comment(0xA32F, 'V set: found, skip allocation', align=Align.INLINE)
d.comment(0xA331, 'Transfer Y to A', align=Align.INLINE)
d.comment(0xA332, 'Allocate FCB slot', align=Align.INLINE)
d.comment(0xA335, 'Store allocation result', align=Align.INLINE)
d.comment(0xA338, 'Zero: failed, restore context', align=Align.INLINE)
d.comment(0xA33A, 'A=&2A: station flags value', align=Align.INLINE)
d.comment(0x9132, 'Store as string pointer low', align=Align.INLINE)
d.comment(0x9135, 'Store as string pointer high', align=Align.INLINE)
d.comment(0x9137, 'Y=0: index for indirect loads', align=Align.INLINE)
d.comment(0x913B, 'No page crossing', align=Align.INLINE)
d.comment(0x913D, 'Carry into high byte', align=Align.INLINE)
d.comment(0x9143, 'Save string pointer on stack', align=Align.INLINE)
d.comment(0x9145, '(push low byte)', align=Align.INLINE)
d.comment(0x9146, 'Save pointer high byte', align=Align.INLINE)
d.comment(0x9148, '(push high byte)', align=Align.INLINE)
d.comment(0x914E, 'Restore string pointer high', align=Align.INLINE)
d.comment(0x914F, 'Store pointer high', align=Align.INLINE)
d.comment(0x9151, 'Restore string pointer low', align=Align.INLINE)
d.comment(0x9152, 'Store pointer low', align=Align.INLINE)
d.comment(0x9154, 'Loop for next character', align=Align.INLINE)
d.comment(0x915A, 'Clear accumulator', align=Align.INLINE)
d.comment(0x915C, 'Initialise result to zero', align=Align.INLINE)
d.comment(0x915E, 'Get first character of argument', align=Align.INLINE)
d.comment(0x9160, "Is it '&' (hex prefix)?", align=Align.INLINE)
d.comment(0x9162, 'No: try decimal path', align=Align.INLINE)
d.comment(0x9164, "Skip '&' prefix", align=Align.INLINE)
d.comment(0x9165, 'Get first hex digit', align=Align.INLINE)
d.comment(0x9167, 'C always set from CMP: validate digit', align=Align.INLINE)
d.comment(0x9169, 'Advance to next character', align=Align.INLINE)
d.comment(0x916A, 'Get next character', align=Align.INLINE)
d.comment(0x916C, "Is it '.' (net.station separator)?", align=Align.INLINE)
d.comment(0x916E, 'Yes: handle dot separator', align=Align.INLINE)
d.comment(0x9170, "Below '!' (space/control)?", align=Align.INLINE)
d.comment(0x9172, 'Yes: end of number', align=Align.INLINE)
d.comment(0x9174, "Below '0'?", align=Align.INLINE)
d.comment(0x9176, 'Not a digit: bad hex', align=Align.INLINE)
d.comment(0x9178, "Above '9'?", align=Align.INLINE)
d.comment(0x917A, 'Decimal digit: extract value', align=Align.INLINE)
d.comment(0x917C, 'Force uppercase', align=Align.INLINE)
d.comment(0x917E, "Map 'A'-'F' to &FA-&FF", align=Align.INLINE)
d.comment(0x9180, 'Overflow: not A-F', align=Align.INLINE)
d.comment(0x9182, 'Valid hex letter (A-F)?', align=Align.INLINE)
d.comment(0x9184, 'Below A: bad hex', align=Align.INLINE)
d.comment(0x9186, 'Extract digit value (0-15)', align=Align.INLINE)
d.comment(0x9188, 'Save current digit', align=Align.INLINE)
d.comment(0x918A, 'Load running result', align=Align.INLINE)
d.comment(0x918C, 'Would shift overflow a byte?', align=Align.INLINE)
d.comment(0x918E, 'Yes: overflow error', align=Align.INLINE)
d.comment(0x9190, 'Shift result left 4 (x16)', align=Align.INLINE)
d.comment(0x9191, '(shift 2)', align=Align.INLINE)
d.comment(0x9192, '(shift 3)', align=Align.INLINE)
d.comment(0x9193, '(shift 4)', align=Align.INLINE)
d.comment(0x9194, 'Add new hex digit', align=Align.INLINE)
d.comment(0x9196, 'Store updated result', align=Align.INLINE)
d.comment(0x9198, 'Loop for next hex digit', align=Align.INLINE)
d.comment(0x919A, 'Get current character', align=Align.INLINE)
d.comment(0x919C, "Is it '.' (net.station separator)?", align=Align.INLINE)
d.comment(0x919E, 'Yes: handle dot separator', align=Align.INLINE)
d.comment(0x91A0, "Below '!' (space/control)?", align=Align.INLINE)
d.comment(0x91A2, 'Yes: end of number', align=Align.INLINE)
d.comment(0x91A4, 'Is it a decimal digit?', align=Align.INLINE)
d.comment(0x91A7, "No: 'Bad number' error", align=Align.INLINE)
d.comment(0x91A9, 'Extract digit value (0-9)', align=Align.INLINE)
d.comment(0x91AB, 'Save current digit', align=Align.INLINE)
d.comment(0x91AD, 'result * 2', align=Align.INLINE)
d.comment(0x91AF, 'Overflow', align=Align.INLINE)
d.comment(0x91B1, 'Load result * 2', align=Align.INLINE)
d.comment(0x91B3, 'result * 4', align=Align.INLINE)
d.comment(0x91B4, 'Overflow', align=Align.INLINE)
d.comment(0x91B6, 'result * 8', align=Align.INLINE)
d.comment(0x91B7, 'Overflow', align=Align.INLINE)
d.comment(0x91B9, '* 8 + * 2 = result * 10', align=Align.INLINE)
d.comment(0x91BB, 'Overflow', align=Align.INLINE)
d.comment(0x91BD, 'result * 10 + new digit', align=Align.INLINE)
d.comment(0x91BF, 'Overflow', align=Align.INLINE)
d.comment(0x91C1, 'Store updated result', align=Align.INLINE)
d.comment(0x91C3, 'Advance to next character', align=Align.INLINE)
d.comment(0x91C4, 'Loop (always branches)', align=Align.INLINE)
d.comment(0x91C6, 'Check parsing mode', align=Align.INLINE)
d.comment(0x91C8, 'Bit 7 clear: net.station mode', align=Align.INLINE)
d.comment(0x91CA, 'Decimal-only mode: get result', align=Align.INLINE)
d.comment(0x91CC, "Zero: 'Bad parameter'", align=Align.INLINE)
d.comment(0x91CE, 'Return with result in A', align=Align.INLINE)
d.comment(0x91CF, 'Get parsed station number', align=Align.INLINE)
d.comment(0x91D1, 'Station 255 is reserved', align=Align.INLINE)
d.comment(0x91D3, "255: 'Bad station number'", align=Align.INLINE)
d.comment(0x91D5, 'Reload result', align=Align.INLINE)
d.comment(0x91D7, 'Non-zero: valid station', align=Align.INLINE)
d.comment(0x91D9, 'Zero result: check if dot was seen', align=Align.INLINE)
d.comment(0x91DB, "No dot and zero: 'Bad station number'", align=Align.INLINE)
d.comment(0x91DD, 'Check character before current pos', align=Align.INLINE)
d.comment(0x91DE, 'Load previous character', align=Align.INLINE)
d.comment(0x91E0, 'Restore Y', align=Align.INLINE)
d.comment(0x91E1, "Was previous char '.'?", align=Align.INLINE)
d.comment(0x91E3, "No: 'Bad station number'", align=Align.INLINE)
d.comment(0x91E5, 'C=1: number was parsed', align=Align.INLINE)
d.comment(0x91E6, 'Return (result in fs_load_addr_2)', align=Align.INLINE)
d.comment(0x91E7, 'Check if dot already seen', align=Align.INLINE)
d.comment(0x91E9, "Already seen: 'Bad number'", align=Align.INLINE)
d.comment(0x91EB, 'Set dot-seen flag', align=Align.INLINE)
d.comment(0x91ED, 'Get network number (before dot)', align=Align.INLINE)
d.comment(0x91EF, 'Network 255 is reserved', align=Align.INLINE)
d.comment(0x91F1, "255: 'Bad network number'", align=Align.INLINE)
d.comment(0x91F3, 'Return to caller with network part', align=Align.INLINE)
d.comment(0x91F4, 'Error code &F1', align=Align.INLINE)
d.comment(0x91F6, "Generate 'Bad hex' error", align=Align.INLINE)
d.comment(0x91FD, 'Test parsing mode', align=Align.INLINE)
d.comment(0x91FF, "Decimal mode: 'Bad parameter'", align=Align.INLINE)
d.comment(0x9201, 'Error code &D0', align=Align.INLINE)
d.comment(0x9203, "Generate 'Bad station number' error", align=Align.INLINE)
d.comment(0x9215, 'Error code &F0', align=Align.INLINE)
d.comment(0x9217, "Generate 'Bad number' error", align=Align.INLINE)
d.comment(0x9221, 'Error code &94', align=Align.INLINE)
d.comment(0x9223, "Generate 'Bad parameter' error", align=Align.INLINE)
d.comment(0x9230, 'Error code &D1', align=Align.INLINE)
d.comment(0x9232, "Generate 'Bad network number' error", align=Align.INLINE)
d.comment(0x9244, "Is it '&' (hex prefix)?", align=Align.INLINE)
d.comment(0x9246, 'Yes: return C set (not decimal)', align=Align.INLINE)
d.comment(0x9248, "Is it '.' (separator)?", align=Align.INLINE)
d.comment(0x924A, 'Yes: return C set (not decimal)', align=Align.INLINE)
d.comment(0x924C, "Above '9'?", align=Align.INLINE)
d.comment(0x924E, 'Yes: not a digit', align=Align.INLINE)
d.comment(0x9250, "Below '0'? C clear if so", align=Align.INLINE)
d.comment(0x9252, "Return: C set if '0'-'9'", align=Align.INLINE)
d.comment(0x9253, 'C=0: not a digit', align=Align.INLINE)
d.comment(0x9254, 'Return', align=Align.INLINE)
d.comment(0x9255, 'Offset &0E in directory entry', align=Align.INLINE)
d.comment(0x9257, 'Load raw access byte', align=Align.INLINE)
d.comment(0x9259, 'Mask to 6 access bits', align=Align.INLINE)
d.comment(0x925B, 'X=4: start encoding at bit 4', align=Align.INLINE)
d.comment(0x925D, 'ALWAYS branch to encoder', align=Align.INLINE)
d.comment(0x925F, 'Mask to 5 protection bits', align=Align.INLINE)
d.comment(0x9261, 'X=&FF: start encoding at bit 0', align=Align.INLINE)
d.comment(0x9263, 'Save remaining bits', align=Align.INLINE)
d.comment(0x9265, 'Clear encoded result', align=Align.INLINE)
d.comment(0x9267, 'Advance to next table position', align=Align.INLINE)
d.comment(0x9268, 'Shift out lowest source bit', align=Align.INLINE)
d.comment(0x926A, 'Bit clear: skip this position', align=Align.INLINE)
d.comment(0x926C, 'Bit set: OR in encoded value', align=Align.INLINE)
d.comment(0x926F, 'More bits to process', align=Align.INLINE)
d.comment(0x9271, 'Return encoded access in A', align=Align.INLINE)
d.comment(0x9272, """Protection/access bit encode table

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
d.comment(0x9272, 'Bit 0: &50 = %01010000 (bits 4,6)', align=Align.INLINE)
d.comment(0x9273, 'Bit 1: &20 = %00100000 (bit 5)', align=Align.INLINE)
d.comment(0x9274, 'Bit 2: &05 = %00000101 (bits 0,2)', align=Align.INLINE)
d.comment(0x9275, 'Bit 3: &02 = %00000010 (bit 1)', align=Align.INLINE)
d.comment(0x9276, 'Bit 4: &88 = %10001000 (bits 3,7)', align=Align.INLINE)
d.comment(0x9277, 'Bit 0: &04 = %00000100 (bit 2)', align=Align.INLINE)
d.comment(0x9278, 'Bit 1: &08 = %00001000 (bit 3)', align=Align.INLINE)
d.comment(0x9279, 'Bit 2: &80 = %10000000 (bit 7)', align=Align.INLINE)
d.comment(0x927A, 'Bit 3: &10 = %00010000 (bit 4)', align=Align.INLINE)
d.comment(0x927B, 'Bit 4: &01 = %00000001 (bit 0)', align=Align.INLINE)
d.comment(0x927C, 'Bit 5: &02 = %00000010 (bit 1)', align=Align.INLINE)
d.comment(0x927D, 'Set text pointer low', align=Align.INLINE)
d.comment(0x927F, 'Set text pointer high', align=Align.INLINE)
d.comment(0x9281, 'Store transfer byte count', align=Align.INLINE)
d.comment(0x9283, 'Store source pointer low', align=Align.INLINE)
d.comment(0x9285, 'Store source pointer high', align=Align.INLINE)
d.comment(0x9287, 'Store options pointer low', align=Align.INLINE)
d.comment(0x9289, 'Store options pointer high', align=Align.INLINE)
d.comment(0x928B, 'Save processor flags', align=Align.INLINE)
d.comment(0x928C, 'Clear bit 0 of escape flag', align=Align.INLINE)
d.comment(0x928E, 'Restore processor flags', align=Align.INLINE)
d.comment(0x928F, 'Return', align=Align.INLINE)
d.comment(0x9290, 'Compare 5 bytes (indices 4 down to 1)', align=Align.INLINE)
d.comment(0x9292, 'Load byte from handle buffer', align=Align.INLINE)
d.comment(0x9294, 'Compare with channel handle', align=Align.INLINE)
d.comment(0x9296, 'Mismatch: return Z=0', align=Align.INLINE)
d.comment(0x9298, 'Next byte', align=Align.INLINE)
d.comment(0x9299, 'Loop until all compared', align=Align.INLINE)
d.comment(0x929B, 'Return: Z=1 if all 5 matched', align=Align.INLINE)
d.comment(0x929C, 'Unreachable code', align=Align.INLINE)
d.comment(0x929E, '(dead)', align=Align.INLINE)
d.comment(0x92A0, '(dead)', align=Align.INLINE)
d.comment(0x92A1, 'Save processor flags', align=Align.INLINE)
d.comment(0x92A2, 'Save A', align=Align.INLINE)
d.comment(0x92A3, 'Transfer X to A', align=Align.INLINE)
d.comment(0x92A4, 'Save original X', align=Align.INLINE)
d.comment(0x92A5, 'Get stack pointer', align=Align.INLINE)
d.comment(0x92A6, 'Read original A from stack', align=Align.INLINE)
d.comment(0x92A9, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92AC, 'No channel found: skip', align=Align.INLINE)
d.comment(0x92AE, 'Bit 6: connection active flag', align=Align.INLINE)
d.comment(0x92B0, 'Set active flag in channel table', align=Align.INLINE)
d.comment(0x92B3, 'Store updated status', align=Align.INLINE)
d.comment(0x92B6, 'ALWAYS branch to exit', align=Align.INLINE)
d.comment(0x92B8, 'Save processor flags', align=Align.INLINE)
d.comment(0x92B9, 'Save A', align=Align.INLINE)
d.comment(0x92BA, 'Transfer X to A', align=Align.INLINE)
d.comment(0x92BB, 'Save original X', align=Align.INLINE)
d.comment(0x92BC, 'Get stack pointer', align=Align.INLINE)
d.comment(0x92BD, 'Read original A from stack', align=Align.INLINE)
d.comment(0x92C0, 'Convert to channel index', align=Align.INLINE)
d.comment(0x92C3, 'No channel found: skip', align=Align.INLINE)
d.comment(0x92C5, 'Bit 6 clear mask (&BF = ~&40)', align=Align.INLINE)
d.comment(0x92C7, 'Clear active flag in channel table', align=Align.INLINE)
d.comment(0x92CA, 'Store updated status', align=Align.INLINE)
d.comment(0x92CD, 'Restore X', align=Align.INLINE)
d.comment(0x92CE, 'Transfer back to X', align=Align.INLINE)
d.comment(0x92CF, 'Restore A', align=Align.INLINE)
d.comment(0x92D0, 'Restore processor flags', align=Align.INLINE)
d.comment(0x92D1, 'Return', align=Align.INLINE)
d.comment(0xA4D6, 'CLC so SBC subtracts value+1', align=Align.INLINE)
d.comment(0xA4D7, 'A = OSWORD number', align=Align.INLINE)
d.comment(0xA4D9, 'A = OSWORD - &0E (CLC+SBC = -&0E)', align=Align.INLINE)
d.comment(0xA4DB, 'Below &0E: not ours, return', align=Align.INLINE)
d.comment(0xA4DD, 'Index >= 7? (OSWORD > &14)', align=Align.INLINE)
d.comment(0xA4DF, 'Above &14: not ours, return', align=Align.INLINE)
d.comment(0xA4E1, 'Set up dispatch and save state', align=Align.INLINE)
d.comment(0xA4E4, 'Copy 3 bytes (Y=2,1,0)', align=Align.INLINE)
d.comment(0xA4E6, 'Load from RX buffer', align=Align.INLINE)
d.comment(0xA4E8, 'Store to osword_flag workspace', align=Align.INLINE)
d.comment(0xA4EB, 'Next byte down', align=Align.INLINE)
d.comment(0xA4EC, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0xA4EE, 'Return from svc_8_osword', align=Align.INLINE)
d.comment(0xA4EF, 'X = OSWORD index (0-6)', align=Align.INLINE)
d.comment(0xA4F0, 'Load handler address high byte', align=Align.INLINE)
d.comment(0xA4F3, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0xA4F4, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA4F7, 'Push low byte for RTS dispatch', align=Align.INLINE)
d.comment(0xA4F8, 'Copy 3 bytes (Y=2,1,0)', align=Align.INLINE)
d.comment(0xA4FA, 'Load from osword_flag workspace', align=Align.INLINE)
d.comment(0xA4FD, 'Store to RX buffer', align=Align.INLINE)
d.comment(0xA4FF, 'Next byte down', align=Align.INLINE)
d.comment(0xA500, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0xA502, 'Y=0 (INY from -1)', align=Align.INLINE)
d.comment(0xA503, 'Load PB byte 0 (OSWORD sub-code)', align=Align.INLINE)
d.comment(0xA505, 'Clear service state', align=Align.INLINE)
d.comment(0xA507, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0xA516, 'Save A for later test', align=Align.INLINE)
d.comment(0xA517, 'Test station active flag', align=Align.INLINE)
d.comment(0xA51A, 'Not active: just return', align=Align.INLINE)
d.comment(0xA51C, 'Restore A (OSWORD sub-code)', align=Align.INLINE)
d.comment(0xA51D, 'Sub-code = 4? (read clock)', align=Align.INLINE)
d.comment(0xA51F, 'Yes: handle clock read', align=Align.INLINE)
d.comment(0xA521, 'Other sub-codes: set state = 8', align=Align.INLINE)
d.comment(0xA523, 'Store service state', align=Align.INLINE)
d.comment(0xA525, 'Return', align=Align.INLINE)
d.comment(0xA526, 'X=0: start of TX control block', align=Align.INLINE)
d.comment(0xA528, 'Y=&10: length of TXCB to save', align=Align.INLINE)
d.comment(0xA52A, 'Save current TX control block', align=Align.INLINE)
d.comment(0xA52D, 'Load seconds from clock workspace', align=Align.INLINE)
d.comment(0xA530, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA533, 'Store BCD seconds', align=Align.INLINE)
d.comment(0xA536, 'Load minutes from clock workspace', align=Align.INLINE)
d.comment(0xA539, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA53C, 'Store BCD minutes', align=Align.INLINE)
d.comment(0xA53F, 'Load hours from clock workspace', align=Align.INLINE)
d.comment(0xA542, 'Convert binary to BCD', align=Align.INLINE)
d.comment(0xA545, 'Store BCD hours', align=Align.INLINE)
d.comment(0xA548, 'Clear hours high position', align=Align.INLINE)
d.comment(0xA54A, 'Store zero', align=Align.INLINE)
d.comment(0xA54D, 'Load day+month byte', align=Align.INLINE)
d.comment(0xA550, 'Save for later high nibble extract', align=Align.INLINE)
d.comment(0xA551, 'Load day value', align=Align.INLINE)
d.comment(0xA554, 'Convert day to BCD', align=Align.INLINE)
d.comment(0xA557, 'Store BCD day', align=Align.INLINE)
d.comment(0xA55A, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA55B, 'Save again for month extract', align=Align.INLINE)
d.comment(0xA55C, 'Mask low nibble (month low bits)', align=Align.INLINE)
d.comment(0xA55E, 'Convert to BCD', align=Align.INLINE)
d.comment(0xA561, 'Store BCD month', align=Align.INLINE)
d.comment(0xA564, 'Restore day+month byte', align=Align.INLINE)
d.comment(0xA565, 'Shift high nibble down', align=Align.INLINE)
d.comment(0xA566, 'Continue shifting', align=Align.INLINE)
d.comment(0xA567, 'Continue shifting', align=Align.INLINE)
d.comment(0xA568, '4th shift: isolate high nibble', align=Align.INLINE)
d.comment(0xA569, 'Add &51 for year offset + carry', align=Align.INLINE)
d.comment(0xA56B, 'Convert year to BCD', align=Align.INLINE)
d.comment(0xA56E, 'Store BCD year', align=Align.INLINE)
d.comment(0xA571, 'Copy 7 bytes (Y=6 down to 0)', align=Align.INLINE)
d.comment(0xA573, 'Load BCD byte from workspace', align=Align.INLINE)
d.comment(0xA576, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA578, 'Next byte down', align=Align.INLINE)
d.comment(0xA579, 'Loop for all 7 bytes', align=Align.INLINE)
d.comment(0xA57B, 'Return', align=Align.INLINE)
d.comment(0xA57C, 'Save processor flags (decimal mode)', align=Align.INLINE)
d.comment(0xA57D, 'X = binary count', align=Align.INLINE)
d.comment(0xA57E, 'Zero: result is 0, skip loop', align=Align.INLINE)
d.comment(0xA580, 'Set decimal mode for BCD add', align=Align.INLINE)
d.comment(0xA581, 'Start BCD result at 0', align=Align.INLINE)
d.comment(0xA583, 'Clear carry for BCD add', align=Align.INLINE)
d.comment(0xA584, 'Add 1 in decimal mode', align=Align.INLINE)
d.comment(0xA586, 'Count down binary value', align=Align.INLINE)
d.comment(0xA587, 'Loop until zero', align=Align.INLINE)
d.comment(0xA589, 'Restore flags (clears decimal mode)', align=Align.INLINE)
d.comment(0xA58A, 'Return with BCD result in A', align=Align.INLINE)
d.comment(0xA58B, 'Shift ws_0d60 left (status flag)', align=Align.INLINE)
d.comment(0xA58E, 'A = Y (saved index)', align=Align.INLINE)
d.comment(0xA58F, 'C=1: transmit active path', align=Align.INLINE)
d.comment(0xA591, 'C=0: store Y to parameter block', align=Align.INLINE)
d.comment(0xA593, 'Return (transmit not active)', align=Align.INLINE)
d.comment(0xA594, 'Set workspace high byte', align=Align.INLINE)
d.comment(0xA596, 'Copy to ws_ptr_hi', align=Align.INLINE)
d.comment(0xA598, 'Also set as NMI TX block high', align=Align.INLINE)
d.comment(0xA59A, 'Low byte = &6F', align=Align.INLINE)
d.comment(0xA59C, 'Set ws_ptr_lo', align=Align.INLINE)
d.comment(0xA59E, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xA5A0, 'X=&0F: byte count for copy', align=Align.INLINE)
d.comment(0xA5A2, 'Copy data and begin transmission', align=Align.INLINE)
d.comment(0xA5A5, 'Jump to begin Econet transmission', align=Align.INLINE)
d.comment(0xA5A8, 'Load NFS workspace page high byte', align=Align.INLINE)
d.comment(0xA5AA, 'Set workspace pointer high', align=Align.INLINE)
d.comment(0xA5AC, 'Set workspace pointer low from Y', align=Align.INLINE)
d.comment(0xA5AE, 'Rotate Econet flags (save interrupt state)', align=Align.INLINE)
d.comment(0xA5B1, 'Load PB byte 0 (OSWORD flag)', align=Align.INLINE)
d.comment(0xA5B3, 'Store OSWORD flag', align=Align.INLINE)
d.comment(0xA5B5, 'Non-zero: use specified slot', align=Align.INLINE)
d.comment(0xA5B7, 'A=3: start searching from slot 3', align=Align.INLINE)
d.comment(0xA5B9, 'Convert slot to 2-bit workspace index', align=Align.INLINE)
d.comment(0xA5BC, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5BE, 'Shift index right (divide by 4)', align=Align.INLINE)
d.comment(0xA5BF, 'Continue shift', align=Align.INLINE)
d.comment(0xA5C0, 'Transfer to X as workspace offset', align=Align.INLINE)
d.comment(0xA5C1, 'Load workspace byte at offset', align=Align.INLINE)
d.comment(0xA5C3, 'Zero: slot empty, store result', align=Align.INLINE)
d.comment(0xA5C5, "Compare with &3F ('?' marker)", align=Align.INLINE)
d.comment(0xA5C7, 'Match: slot found for receive', align=Align.INLINE)
d.comment(0xA5C9, 'Try next slot index', align=Align.INLINE)
d.comment(0xA5CA, 'Transfer back to A', align=Align.INLINE)
d.comment(0xA5CB, 'Loop back (A != 0)', align=Align.INLINE)
d.comment(0xA5CD, 'Transfer found slot to A', align=Align.INLINE)
d.comment(0xA5CE, 'X=0: index for indirect store', align=Align.INLINE)
d.comment(0xA5D0, 'Store slot number to PB byte 0', align=Align.INLINE)
d.comment(0xA5D2, 'Convert specified slot to workspace index', align=Align.INLINE)
d.comment(0xA5D5, 'C set: slot invalid, store result', align=Align.INLINE)
d.comment(0xA5D7, 'Y=Y-1: adjust workspace offset', align=Align.INLINE)
d.comment(0xA5D8, 'Update workspace pointer low', align=Align.INLINE)
d.comment(0xA5DA, 'A=&C0: slot active marker', align=Align.INLINE)
d.comment(0xA5DC, 'Y=1: workspace byte offset', align=Align.INLINE)
d.comment(0xA5DE, 'X=&0B: byte count for PB copy', align=Align.INLINE)
d.comment(0xA5E0, 'Compare Y with OSWORD flag', align=Align.INLINE)
d.comment(0xA5E2, 'Add workspace byte (check slot state)', align=Align.INLINE)
d.comment(0xA5E4, 'Zero: slot ready, copy PB and mark', align=Align.INLINE)
d.comment(0xA5E6, 'Negative: slot busy, increment and retry', align=Align.INLINE)
d.comment(0xA5E8, 'Clear carry for PB copy', align=Align.INLINE)
d.comment(0xA5E9, 'Copy PB byte to workspace slot', align=Align.INLINE)
d.comment(0xA5EC, 'C set: copy done, finish', align=Align.INLINE)
d.comment(0xA5EE, "A=&3F: mark slot as pending ('?')", align=Align.INLINE)
d.comment(0xA5F0, 'Y=1: workspace flag offset', align=Align.INLINE)
d.comment(0xA5F2, 'Store pending marker to workspace', align=Align.INLINE)
d.comment(0xA5F6, 'Increment retry counter', align=Align.INLINE)
d.comment(0xA5F8, 'Non-zero: retry copy loop', align=Align.INLINE)
d.comment(0xA5FA, 'Decrement Y (adjust offset)', align=Align.INLINE)
d.comment(0xA5FB, 'Store result A to PB via Y', align=Align.INLINE)
d.comment(0xA5FD, 'Rotate Econet flags back (restore state)', align=Align.INLINE)
d.comment(0xA600, 'Return from OSWORD 11 handler', align=Align.INLINE)
d.comment(0xA601, 'Y=&1C: workspace offset', align=Align.INLINE)
d.comment(0xA603, 'Load PB pointer low byte', align=Align.INLINE)
d.comment(0xA605, 'Add 1 (C from earlier operation)', align=Align.INLINE)
d.comment(0xA607, 'Store ptr at workspace+Y', align=Align.INLINE)
d.comment(0xA60A, 'Y=1: read PB byte 1', align=Align.INLINE)
d.comment(0xA60C, 'Load transfer length from PB', align=Align.INLINE)
d.comment(0xA60E, 'Y=&20: second workspace offset', align=Align.INLINE)
d.comment(0xA610, 'Add PB low byte to get end ptr', align=Align.INLINE)
d.comment(0xA612, 'Store low byte to workspace+Y', align=Align.INLINE)
d.comment(0xA614, 'Next byte', align=Align.INLINE)
d.comment(0xA615, 'Load PB pointer high byte', align=Align.INLINE)
d.comment(0xA617, 'Add carry', align=Align.INLINE)
d.comment(0xA619, 'Store high byte to workspace+Y+1', align=Align.INLINE)
d.comment(0xA61B, 'Return', align=Align.INLINE)
d.comment(0xA61C, 'Set workspace from RX ptr high', align=Align.INLINE)
d.comment(0xA61E, 'Store to ws_ptr_hi', align=Align.INLINE)
d.comment(0xA620, 'Y=&7F: last byte of RX buffer', align=Align.INLINE)
d.comment(0xA622, 'Load port/count from RX buffer', align=Align.INLINE)
d.comment(0xA624, 'Y=&80: set workspace pointer', align=Align.INLINE)
d.comment(0xA625, 'Store as ws_ptr_lo', align=Align.INLINE)
d.comment(0xA627, 'X = port/count value', align=Align.INLINE)
d.comment(0xA628, 'X-1: adjust count', align=Align.INLINE)
d.comment(0xA629, 'Y=0 for copy', align=Align.INLINE)
d.comment(0xA62B, 'Copy workspace data', align=Align.INLINE)
d.comment(0xA62E, 'Update state and return', align=Align.INLINE)
d.comment(0xA631, 'X = sub-code', align=Align.INLINE)
d.comment(0xA632, 'Sub-code < &13?', align=Align.INLINE)
d.comment(0xA634, 'Out of range: return', align=Align.INLINE)
d.comment(0xA636, 'Load handler address high byte', align=Align.INLINE)
d.comment(0xA639, 'Push high byte', align=Align.INLINE)
d.comment(0xA63A, 'Load handler address low byte', align=Align.INLINE)
d.comment(0xA63D, 'Push low byte', align=Align.INLINE)
d.comment(0xA63E, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0xA63F, 'lo-sub 0: read FS station', align=Align.INLINE)
d.comment(0xA640, 'lo-sub 1: set FS station', align=Align.INLINE)
d.comment(0xA641, 'lo-sub 2: read workspace pair', align=Align.INLINE)
d.comment(0xA642, 'lo-sub 3: write workspace pair', align=Align.INLINE)
d.comment(0xA643, 'lo-sub 4: read protection mask', align=Align.INLINE)
d.comment(0xA644, 'lo-sub 5: write protection mask', align=Align.INLINE)
d.comment(0xA645, 'lo-sub 6: read FCB handles', align=Align.INLINE)
d.comment(0xA646, 'lo-sub 7: set FCB handles', align=Align.INLINE)
d.comment(0xA647, 'lo-sub 8: read RX flag', align=Align.INLINE)
d.comment(0xA648, 'lo-sub 9: read RX port', align=Align.INLINE)
d.comment(0xA649, 'lo-sub 10: read error flag', align=Align.INLINE)
d.comment(0xA64A, 'lo-sub 11: read context byte', align=Align.INLINE)
d.comment(0xA64B, 'lo-sub 12: read CSD path', align=Align.INLINE)
d.comment(0xA64C, 'lo-sub 13: write CSD path', align=Align.INLINE)
d.comment(0xA64D, 'lo-sub 14: read free buffers', align=Align.INLINE)
d.comment(0xA64E, 'lo-sub 15: read 3 context bytes', align=Align.INLINE)
d.comment(0xA64F, 'lo-sub 16: write 3 context bytes', align=Align.INLINE)
d.comment(0xA650, 'lo-sub 17: query bridge status', align=Align.INLINE)
d.comment(0xA651, 'hi-sub 0: read FS station', align=Align.INLINE)
d.comment(0xA652, 'hi-sub 1: set FS station', align=Align.INLINE)
d.comment(0xA653, 'hi-sub 2: read workspace pair', align=Align.INLINE)
d.comment(0xA654, 'hi-sub 3: write workspace pair', align=Align.INLINE)
d.comment(0xA655, 'hi-sub 4: read protection mask', align=Align.INLINE)
d.comment(0xA656, 'hi-sub 5: write protection mask', align=Align.INLINE)
d.comment(0xA657, 'hi-sub 6: read FCB handles', align=Align.INLINE)
d.comment(0xA658, 'hi-sub 7: set FCB handles', align=Align.INLINE)
d.comment(0xA659, 'hi-sub 8: read RX flag', align=Align.INLINE)
d.comment(0xA65A, 'hi-sub 9: read RX port', align=Align.INLINE)
d.comment(0xA65B, 'hi-sub 10: read error flag', align=Align.INLINE)
d.comment(0xA65C, 'hi-sub 11: read context byte', align=Align.INLINE)
d.comment(0xA65D, 'hi-sub 12: read CSD path', align=Align.INLINE)
d.comment(0xA65E, 'hi-sub 13: write CSD path', align=Align.INLINE)
d.comment(0xA65F, 'hi-sub 14: read free buffers', align=Align.INLINE)
d.comment(0xA660, 'hi-sub 15: read 3 context bytes', align=Align.INLINE)
d.comment(0xA661, 'hi-sub 16: write 3 context bytes', align=Align.INLINE)
d.comment(0xA662, 'hi-sub 17: query bridge status', align=Align.INLINE)
d.comment(0xA6FB, 'C=0: skip PB-to-WS copy', align=Align.INLINE)
d.comment(0xA6FD, 'C=1: load from parameter block', align=Align.INLINE)
d.comment(0xA6FF, 'Store to workspace', align=Align.INLINE)
d.comment(0xA701, 'Load from workspace', align=Align.INLINE)
d.comment(0xA703, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA705, 'Next byte', align=Align.INLINE)
d.comment(0xA706, 'Count down', align=Align.INLINE)
d.comment(0xA707, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xA709, 'Return', align=Align.INLINE)
d.comment(0xA663, 'NFS active?', align=Align.INLINE)
d.comment(0xA666, 'Yes: read station data', align=Align.INLINE)
d.comment(0xA668, 'No: return zero', align=Align.INLINE)
d.comment(0xA66B, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA66D, 'Load station byte', align=Align.INLINE)
d.comment(0xA670, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA672, 'Previous byte', align=Align.INLINE)
d.comment(0xA673, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA675, 'Return', align=Align.INLINE)
d.comment(0xA676, 'NFS active?', align=Align.INLINE)
d.comment(0xA679, 'No: return zero', align=Align.INLINE)
d.comment(0xA67B, 'Y=0 for process_all_fcbs', align=Align.INLINE)
d.comment(0xA67D, 'Close all open FCBs', align=Align.INLINE)
d.comment(0xA680, 'Y=2: copy 2 bytes', align=Align.INLINE)
d.comment(0xA682, 'Load new station byte from PB', align=Align.INLINE)
d.comment(0xA684, 'Store to l0dff', align=Align.INLINE)
d.comment(0xA687, 'Previous byte', align=Align.INLINE)
d.comment(0xA688, 'Loop for bytes 2..1', align=Align.INLINE)
d.comment(0xA68A, 'Clear handles if station matches', align=Align.INLINE)
d.comment(0xA68D, 'X=&0F: scan 16 FCB entries', align=Align.INLINE)
d.comment(0xA68F, 'Load FCB flags', align=Align.INLINE)
d.comment(0xA692, 'Save flags in Y', align=Align.INLINE)
d.comment(0xA693, 'Test bit 1 (FCB allocated?)', align=Align.INLINE)
d.comment(0xA695, 'No: skip to next entry', align=Align.INLINE)
d.comment(0xA697, 'Restore flags', align=Align.INLINE)
d.comment(0xA698, 'Clear bit 5 (pending update)', align=Align.INLINE)
d.comment(0xA69A, 'Store updated flags', align=Align.INLINE)
d.comment(0xA69D, 'Save in Y', align=Align.INLINE)
d.comment(0xA69E, 'Does FCB match new station?', align=Align.INLINE)
d.comment(0xA6A1, 'No match: skip to next', align=Align.INLINE)
d.comment(0xA6A3, 'Clear carry for ADC', align=Align.INLINE)
d.comment(0xA6A4, 'Restore flags', align=Align.INLINE)
d.comment(0xA6A5, 'Test bit 2 (handle 1 active?)', align=Align.INLINE)
d.comment(0xA6A7, 'No: check handle 2', align=Align.INLINE)
d.comment(0xA6A9, 'Restore flags', align=Align.INLINE)
d.comment(0xA6AA, 'Set bit 5 (handle reassigned)', align=Align.INLINE)
d.comment(0xA6AC, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6AD, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6B0, 'Store as handle 1 station', align=Align.INLINE)
d.comment(0xA6B3, 'FCB index', align=Align.INLINE)
d.comment(0xA6B4, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6B6, 'Store as handle 1 FCB index', align=Align.INLINE)
d.comment(0xA6B9, 'Restore flags', align=Align.INLINE)
d.comment(0xA6BA, 'Test bit 3 (handle 2 active?)', align=Align.INLINE)
d.comment(0xA6BC, 'No: check handle 3', align=Align.INLINE)
d.comment(0xA6BE, 'Restore flags', align=Align.INLINE)
d.comment(0xA6BF, 'Set bit 5', align=Align.INLINE)
d.comment(0xA6C1, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6C2, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6C5, 'Store as handle 2 station', align=Align.INLINE)
d.comment(0xA6C8, 'FCB index', align=Align.INLINE)
d.comment(0xA6C9, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6CB, 'Store as handle 2 FCB index', align=Align.INLINE)
d.comment(0xA6CE, 'Restore flags', align=Align.INLINE)
d.comment(0xA6CF, 'Test bit 4 (handle 3 active?)', align=Align.INLINE)
d.comment(0xA6D1, 'No: store final flags', align=Align.INLINE)
d.comment(0xA6D3, 'Restore flags', align=Align.INLINE)
d.comment(0xA6D4, 'Set bit 5', align=Align.INLINE)
d.comment(0xA6D6, 'Save updated flags', align=Align.INLINE)
d.comment(0xA6D7, 'Get FCB high byte', align=Align.INLINE)
d.comment(0xA6DA, 'Store as handle 3 station', align=Align.INLINE)
d.comment(0xA6DD, 'FCB index', align=Align.INLINE)
d.comment(0xA6DE, 'Add &20 for FCB table offset', align=Align.INLINE)
d.comment(0xA6E0, 'Store as handle 3 FCB index', align=Align.INLINE)
d.comment(0xA6E3, 'Store final flags for this FCB', align=Align.INLINE)
d.comment(0xA6E4, 'Update l1060[X]', align=Align.INLINE)
d.comment(0xA6E7, 'Next FCB entry', align=Align.INLINE)
d.comment(0xA6E8, 'Loop for all 16 entries', align=Align.INLINE)
d.comment(0xA6EA, 'Return', align=Align.INLINE)
d.comment(0xA6EB, 'C=0: workspace-to-PB direction', align=Align.INLINE)
d.comment(0xA6EC, 'Skip SEC', align=Align.INLINE)
d.comment(0xA6EE, 'C=1: PB-to-workspace direction', align=Align.INLINE)
d.comment(0xA6EF, 'Workspace offset &1B', align=Align.INLINE)
d.comment(0xA6F1, 'Set ws_ptr_lo', align=Align.INLINE)
d.comment(0xA6F3, 'Page from RX pointer high byte', align=Align.INLINE)
d.comment(0xA6F5, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xA6F7, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xA6F9, 'X=5: copy 5 bytes', align=Align.INLINE)
d.comment(0xA70A, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0xA70C, 'Set ws_ptr_hi', align=Align.INLINE)
d.comment(0xA70E, 'Y=1', align=Align.INLINE)
d.comment(0xA70F, 'A=1', align=Align.INLINE)
d.comment(0xA710, 'Set ws_ptr_lo = 1', align=Align.INLINE)
d.comment(0xA712, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0xA713, 'C=0: workspace-to-PB direction', align=Align.INLINE)
d.comment(0xA714, 'Copy via copy_pb_byte_to_ws', align=Align.INLINE)
d.comment(0xA716, 'Y=1: first PB data byte', align=Align.INLINE)
d.comment(0xA717, 'Load PB[1]', align=Align.INLINE)
d.comment(0xA719, 'Y=2', align=Align.INLINE)
d.comment(0xA71A, 'Store to (nfs_workspace)+2', align=Align.INLINE)
d.comment(0xA71C, 'Load PB[2]', align=Align.INLINE)
d.comment(0xA71E, 'Y=3', align=Align.INLINE)
d.comment(0xA71F, 'Store to (nfs_workspace)+3', align=Align.INLINE)
d.comment(0xA721, 'Reinitialise bridge routing', align=Align.INLINE)
d.comment(0xA724, 'Compare result with workspace', align=Align.INLINE)
d.comment(0xA726, 'Different: leave unchanged', align=Align.INLINE)
d.comment(0xA728, 'Same: clear workspace byte', align=Align.INLINE)
d.comment(0xA72A, 'Return', align=Align.INLINE)
d.comment(0xA72B, 'Load protection mask', align=Align.INLINE)
d.comment(0xA72E, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA731, 'Y=1: PB data offset', align=Align.INLINE)
d.comment(0xA732, 'Load new mask from PB[1]', align=Align.INLINE)
d.comment(0xA734, 'Store via store_prot_mask', align=Align.INLINE)
d.comment(0xA737, 'NFS active?', align=Align.INLINE)
d.comment(0xA73A, 'No: return zero', align=Align.INLINE)
d.comment(0xA73C, 'Y=3: copy 3 bytes', align=Align.INLINE)
d.comment(0xA73E, 'Load handle byte', align=Align.INLINE)
d.comment(0xA741, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA743, 'Previous byte', align=Align.INLINE)
d.comment(0xA744, 'Loop for bytes 3..1', align=Align.INLINE)
d.comment(0xA746, 'Return', align=Align.INLINE)
d.comment(0xA74C, 'A=0', align=Align.INLINE)
d.comment(0xA74F, 'Store 0 to PB[0]', align=Align.INLINE)
d.comment(0xA751, 'Return', align=Align.INLINE)
d.comment(0xA747, 'NFS active?', align=Align.INLINE)
d.comment(0xA74A, 'Yes: process handles', align=Align.INLINE)
d.comment(0xA752, 'Y=1: first handle in PB', align=Align.INLINE)
d.comment(0xA754, 'Load handle value from PB[Y]', align=Align.INLINE)
d.comment(0xA756, 'Must be >= &20', align=Align.INLINE)
d.comment(0xA758, 'Below range: invalid', align=Align.INLINE)
d.comment(0xA75A, 'Must be < &30', align=Align.INLINE)
d.comment(0xA75C, 'Above range: invalid', align=Align.INLINE)
d.comment(0xA75E, 'X = handle value', align=Align.INLINE)
d.comment(0xA75F, 'Load l1010[handle]', align=Align.INLINE)
d.comment(0xA762, 'Non-zero: FCB exists', align=Align.INLINE)
d.comment(0xA764, 'Invalid: store 0 to PB[0]', align=Align.INLINE)
d.comment(0xA767, 'Clear PB[0] status', align=Align.INLINE)
d.comment(0xA769, 'Skip to next handle', align=Align.INLINE)
d.comment(0xA76B, 'Load l1040[handle] flags', align=Align.INLINE)
d.comment(0xA76E, 'Test bit 1 (allocated?)', align=Align.INLINE)
d.comment(0xA770, 'Not allocated: invalid', align=Align.INLINE)
d.comment(0xA772, 'X = handle value', align=Align.INLINE)
d.comment(0xA773, 'Store handle to l1071+Y', align=Align.INLINE)
d.comment(0xA776, 'Load station from l1010', align=Align.INLINE)
d.comment(0xA779, 'Store station to l0e01+Y', align=Align.INLINE)
d.comment(0xA77C, 'Is this handle 1 (Y=1)?', align=Align.INLINE)
d.comment(0xA77E, 'No: check handle 2', align=Align.INLINE)
d.comment(0xA780, 'Save Y', align=Align.INLINE)
d.comment(0xA781, 'Push Y', align=Align.INLINE)
d.comment(0xA782, 'Bit mask &04 for handle 1', align=Align.INLINE)
d.comment(0xA784, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA787, 'Restore Y', align=Align.INLINE)
d.comment(0xA788, 'Back to Y', align=Align.INLINE)
d.comment(0xA789, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA78C, 'Set bits 2+5 (active+updated)', align=Align.INLINE)
d.comment(0xA78E, 'Store updated flags', align=Align.INLINE)
d.comment(0xA791, 'Next handle slot', align=Align.INLINE)
d.comment(0xA792, 'Done all 3 handles?', align=Align.INLINE)
d.comment(0xA794, 'No: process next handle', align=Align.INLINE)
d.comment(0xA796, 'Y=3 for return', align=Align.INLINE)
d.comment(0xA797, 'Return', align=Align.INLINE)
d.comment(0xA798, 'Is this handle 2 (Y=2)?', align=Align.INLINE)
d.comment(0xA79A, 'No: must be handle 3', align=Align.INLINE)
d.comment(0xA79C, 'Save Y', align=Align.INLINE)
d.comment(0xA79D, 'Push Y', align=Align.INLINE)
d.comment(0xA79E, 'Bit mask &08 for handle 2', align=Align.INLINE)
d.comment(0xA7A0, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA7A3, 'Restore Y', align=Align.INLINE)
d.comment(0xA7A4, 'Back to Y', align=Align.INLINE)
d.comment(0xA7A5, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA7A8, 'Set bits 3+5 (active+updated)', align=Align.INLINE)
d.comment(0xA7AA, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7AD, 'Next handle slot', align=Align.INLINE)
d.comment(0xA7AF, 'Handle 3: save Y', align=Align.INLINE)
d.comment(0xA7B0, 'Push Y', align=Align.INLINE)
d.comment(0xA7B1, 'Bit mask &10 for handle 3', align=Align.INLINE)
d.comment(0xA7B3, 'Update flags across all FCBs', align=Align.INLINE)
d.comment(0xA7B6, 'Restore Y', align=Align.INLINE)
d.comment(0xA7B7, 'Back to Y', align=Align.INLINE)
d.comment(0xA7B8, 'Reload l1040 flags', align=Align.INLINE)
d.comment(0xA7BB, 'Set bits 4+5 (active+updated)', align=Align.INLINE)
d.comment(0xA7BD, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7C0, 'Next handle slot', align=Align.INLINE)
d.comment(0xA7C2, 'Save X (current FCB index)', align=Align.INLINE)
d.comment(0xA7C3, 'Push X', align=Align.INLINE)
d.comment(0xA7C4, 'X=&0F: scan 16 FCB entries', align=Align.INLINE)
d.comment(0xA7C6, 'Load FCB flags', align=Align.INLINE)
d.comment(0xA7C9, 'Shift bits 6-7 into bits 7-0', align=Align.INLINE)
d.comment(0xA7CA, 'Bit 6 now in bit 7 (N flag)', align=Align.INLINE)
d.comment(0xA7CB, 'Bit 6 clear: skip entry', align=Align.INLINE)
d.comment(0xA7CD, 'Restore Y (bit mask)', align=Align.INLINE)
d.comment(0xA7CE, 'Test mask bits against flags', align=Align.INLINE)
d.comment(0xA7D1, 'Zero: no matching bits', align=Align.INLINE)
d.comment(0xA7D3, 'Matching: restore Y', align=Align.INLINE)
d.comment(0xA7D4, 'Set bit 5 (updated)', align=Align.INLINE)
d.comment(0xA7D6, 'Skip clear path', align=Align.INLINE)
d.comment(0xA7D8, 'No match: restore Y', align=Align.INLINE)
d.comment(0xA7D9, 'Invert all bits', align=Align.INLINE)
d.comment(0xA7DB, 'Clear tested bits in flags', align=Align.INLINE)
d.comment(0xA7DE, 'Store updated flags', align=Align.INLINE)
d.comment(0xA7E1, 'Next FCB entry', align=Align.INLINE)
d.comment(0xA7E2, 'Loop for all 16 entries', align=Align.INLINE)
d.comment(0xA7E4, 'Restore original X', align=Align.INLINE)
d.comment(0xA7E5, 'Back to X', align=Align.INLINE)
d.comment(0xA7E6, 'Return', align=Align.INLINE)
d.comment(0xA7E7, 'Y=5: RX control block offset', align=Align.INLINE)
d.comment(0xA7E9, 'Load (net_rx_ptr)+5', align=Align.INLINE)
d.comment(0xA7EB, 'Y=0', align=Align.INLINE)
d.comment(0xA7ED, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA7F0, 'Y=&7F: port byte offset', align=Align.INLINE)
d.comment(0xA7F2, 'Load (net_rx_ptr)+&7F', align=Align.INLINE)
d.comment(0xA7F4, 'Y=1', align=Align.INLINE)
d.comment(0xA7F6, 'Store to PB[1]', align=Align.INLINE)
d.comment(0xA7F9, 'A=&80', align=Align.INLINE)
d.comment(0xA7FB, 'Store &80 to PB[2]', align=Align.INLINE)
d.comment(0xA7FD, 'Return', align=Align.INLINE)
d.comment(0xA7FE, 'Load error flag', align=Align.INLINE)
d.comment(0xA801, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA804, 'Load context byte', align=Align.INLINE)
d.comment(0xA807, 'Store to PB[1] and return', align=Align.INLINE)
d.comment(0xA80A, 'Total buffers = &6F', align=Align.INLINE)
d.comment(0xA80C, 'Subtract used count', align=Align.INLINE)
d.comment(0xA80D, 'Free = &6F - l0d6b', align=Align.INLINE)
d.comment(0xA810, 'Y=1', align=Align.INLINE)
d.comment(0xA811, 'Store A to PB[1]', align=Align.INLINE)
d.comment(0xA813, 'Return', align=Align.INLINE)
d.comment(0xA814, 'Next byte offset', align=Align.INLINE)
d.comment(0xA815, 'Load l0d6d[Y]', align=Align.INLINE)
d.comment(0xA818, 'Store to PB[Y]', align=Align.INLINE)
d.comment(0xA81A, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xA81C, 'No: loop', align=Align.INLINE)
d.comment(0xA81E, 'Return', align=Align.INLINE)
d.comment(0xA81F, 'Next byte offset', align=Align.INLINE)
d.comment(0xA820, 'Load PB[Y]', align=Align.INLINE)
d.comment(0xA822, 'Store to l0d6d[Y]', align=Align.INLINE)
d.comment(0xA825, 'Done 3 bytes?', align=Align.INLINE)
d.comment(0xA827, 'No: loop', align=Align.INLINE)
d.comment(0xA829, 'Return', align=Align.INLINE)
d.comment(0xA82A, 'Poll for bridge', align=Align.INLINE)
d.comment(0xA82D, 'Y=0', align=Align.INLINE)
d.comment(0xA82F, 'Load bridge status', align=Align.INLINE)
d.comment(0xA832, 'Is it &FF (no bridge)?', align=Align.INLINE)
d.comment(0xA834, 'No: bridge found', align=Align.INLINE)
d.comment(0xA837, 'PB[0] = 0 (no bridge)', align=Align.INLINE)
d.comment(0xA839, 'Return', align=Align.INLINE)
d.comment(0xA83A, 'Y=1', align=Align.INLINE)
d.comment(0xA83B, 'PB[1] = bridge status', align=Align.INLINE)
d.comment(0xA83D, 'Y=2', align=Align.INLINE)
d.comment(0xA83E, 'Y=3', align=Align.INLINE)
d.comment(0xA83F, 'Load PB[3] (caller value)', align=Align.INLINE)
d.comment(0xA841, 'Zero: use default station', align=Align.INLINE)
d.comment(0xA843, 'Compare with bridge status', align=Align.INLINE)
d.comment(0xA846, 'Different: return unchanged', align=Align.INLINE)
d.comment(0xA848, 'Same: confirm station', align=Align.INLINE)
d.comment(0xA84A, 'Load default from l0e01', align=Align.INLINE)
d.comment(0xA84D, 'Store to PB[3]', align=Align.INLINE)
d.comment(0xA84F, 'Return', align=Align.INLINE)
d.comment(0xA850, """Bridge discovery init data (24 bytes)

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
d.comment(0xA850, 'TX 0: ctrl = &82 (immediate mode)', align=Align.INLINE)
d.comment(0xA851, 'TX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xA852, 'TX 2: dest station = &FF (broadcast)', align=Align.INLINE)
d.comment(0xA853, 'TX 3: dest network = &FF (all nets)', align=Align.INLINE)
d.comment(0xA854, 'TX 4-9: immediate data payload', align=Align.INLINE)
d.comment(0xA85A, 'TX 10: &9C (port echo)', align=Align.INLINE)
d.comment(0xA85B, 'TX 11: &00 (terminator)', align=Align.INLINE)
d.comment(0xA85C, 'RX 0: ctrl = &7F (receive)', align=Align.INLINE)
d.comment(0xA85D, 'RX 1: port = &9C (bridge discovery)', align=Align.INLINE)
d.comment(0xA85E, 'RX 2: station = &00 (any)', align=Align.INLINE)
d.comment(0xA85F, 'RX 3: network = &00 (any)', align=Align.INLINE)
d.comment(0xA860, 'RX 4: buf start lo (&72)', align=Align.INLINE)
d.comment(0xA861, 'RX 5: buf start hi (&0D) -> &0D72', align=Align.INLINE)
d.comment(0xA862, 'RX 6: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA863, 'RX 7: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA864, 'RX 8: buf end lo (&74)', align=Align.INLINE)
d.comment(0xA865, 'RX 9: buf end hi (&0D) -> &0D74', align=Align.INLINE)
d.comment(0xA866, 'RX 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA867, 'RX 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0xA868, 'Check bridge status', align=Align.INLINE)
d.comment(0xA86B, 'Is it &FF (uninitialised)?', align=Align.INLINE)
d.comment(0xA86D, 'No: bridge already active, return', align=Align.INLINE)
d.comment(0xA86F, 'Save Y', align=Align.INLINE)
d.comment(0xA870, 'Preserve Y on stack', align=Align.INLINE)
d.comment(0xA871, 'Y=&18: workspace offset for init', align=Align.INLINE)
d.comment(0xA873, 'X=&0B: 12 bytes to copy', align=Align.INLINE)
d.comment(0xA875, 'Rotate l0d61 right (save flag)', align=Align.INLINE)
d.comment(0xA878, 'Load init data byte', align=Align.INLINE)
d.comment(0xA87B, 'Store to workspace', align=Align.INLINE)
d.comment(0xA87D, 'Load TXCB template byte', align=Align.INLINE)
d.comment(0xA880, 'Store to TX control block', align=Align.INLINE)
d.comment(0xA882, 'Next workspace byte', align=Align.INLINE)
d.comment(0xA883, 'Next template byte', align=Align.INLINE)
d.comment(0xA884, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0xA886, 'Store X (-1) as bridge counter', align=Align.INLINE)
d.comment(0xA889, 'Restore l0d61 flag', align=Align.INLINE)
d.comment(0xA88C, 'Shift ws_0d60 left (check status)', align=Align.INLINE)
d.comment(0xA88F, 'C=0: status clear, retry', align=Align.INLINE)
d.comment(0xA891, 'Control byte &82 for TX', align=Align.INLINE)
d.comment(0xA893, 'Set in TX control block', align=Align.INLINE)
d.comment(0xA895, 'Data block at &00C0', align=Align.INLINE)
d.comment(0xA897, 'Set NMI TX block low', align=Align.INLINE)
d.comment(0xA899, 'High byte = 0 (page 0)', align=Align.INLINE)
d.comment(0xA89B, 'Set NMI TX block high', align=Align.INLINE)
d.comment(0xA89D, 'Begin Econet transmission', align=Align.INLINE)
d.comment(0xA8A0, 'Test TX control block bit 7', align=Align.INLINE)
d.comment(0xA8A2, 'Negative: TX still in progress', align=Align.INLINE)
d.comment(0xA8A4, 'X = result status', align=Align.INLINE)
d.comment(0xA8A5, 'Save TX status', align=Align.INLINE)
d.comment(0xA8A6, 'Save PB pointer high', align=Align.INLINE)
d.comment(0xA8A8, 'Push for later restore', align=Align.INLINE)
d.comment(0xA8A9, 'X = PB pointer low', align=Align.INLINE)
d.comment(0xA8AB, 'OSBYTE &13: wait for VSYNC', align=Align.INLINE)
d.comment(0xA8AD, 'Wait for vertical sync', align=Align.INLINE)
d.comment(0xA8B0, 'Restore PB pointer high', align=Align.INLINE)
d.comment(0xA8B1, 'Restore to osword_pb_ptr_hi', align=Align.INLINE)
d.comment(0xA8B3, 'Restore TX status', align=Align.INLINE)
d.comment(0xA8B4, 'Back to X', align=Align.INLINE)
d.comment(0xA8B5, 'Y=&18: check workspace response', align=Align.INLINE)
d.comment(0xA8B7, 'Load bridge response', align=Align.INLINE)
d.comment(0xA8B9, 'Negative: bridge responded', align=Align.INLINE)
d.comment(0xA8BB, 'Advance retry counter by 8', align=Align.INLINE)
d.comment(0xA8BE, 'Positive: retry poll loop', align=Align.INLINE)
d.comment(0xA8C0, 'Set response to &3F (OK)', align=Align.INLINE)
d.comment(0xA8C2, 'Store to workspace', align=Align.INLINE)
d.comment(0xA8C4, 'Restore saved Y', align=Align.INLINE)
d.comment(0xA8C5, 'Back to Y', align=Align.INLINE)
d.comment(0xA8C6, 'Load bridge status', align=Align.INLINE)
d.comment(0xA8C9, 'X = bridge status', align=Align.INLINE)
d.comment(0xA8CA, 'Complement status', align=Align.INLINE)
d.comment(0xA8CC, 'Status was &FF: return (no bridge)', align=Align.INLINE)
d.comment(0xA8CE, 'Return bridge station in A', align=Align.INLINE)
d.comment(0xA8CF, 'Return', align=Align.INLINE)
d.comment(0xA8D0, 'Compare sub-code with 1', align=Align.INLINE)
d.comment(0xA8D2, 'Sub-code >= 1: handle TX request', align=Align.INLINE)
d.comment(0xA8D4, 'Test station active flag', align=Align.INLINE)
d.comment(0xA8D7, 'Not active: return', align=Align.INLINE)
d.comment(0xA8D9, 'Y=&23: workspace offset for params', align=Align.INLINE)
d.comment(0xA8DB, 'Set owner access mask', align=Align.INLINE)
d.comment(0xA8DE, 'Load TXCB init byte', align=Align.INLINE)
d.comment(0xA8E1, 'Non-zero: use template value', align=Align.INLINE)
d.comment(0xA8E3, 'Zero: use workspace default value', align=Align.INLINE)
d.comment(0xA8E6, 'Store to workspace', align=Align.INLINE)
d.comment(0xA8E8, 'Next byte down', align=Align.INLINE)
d.comment(0xA8E9, 'Until Y reaches &17', align=Align.INLINE)
d.comment(0xA8EB, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xA8ED, 'Y=&18 (INY from &17)', align=Align.INLINE)
d.comment(0xA8EE, 'Set net_tx_ptr low byte', align=Align.INLINE)
d.comment(0xA8F0, 'Store PB pointer to workspace', align=Align.INLINE)
d.comment(0xA8F3, 'Y=2: parameter offset', align=Align.INLINE)
d.comment(0xA8F5, 'Control byte &90', align=Align.INLINE)
d.comment(0xA8F7, 'Set escapable flag', align=Align.INLINE)
d.comment(0xA8F9, 'Store control byte to PB', align=Align.INLINE)
d.comment(0xA8FD, 'Load workspace data', align=Align.INLINE)
d.comment(0xA900, 'Store to parameter block', align=Align.INLINE)
d.comment(0xA902, 'Next byte', align=Align.INLINE)
d.comment(0xA903, 'Until Y reaches 7', align=Align.INLINE)
d.comment(0xA905, 'Loop for 3 bytes (Y=4,5,6)', align=Align.INLINE)
d.comment(0xA907, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0xA909, 'Store to net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xA90B, 'Enable interrupts', align=Align.INLINE)
d.comment(0xA90C, 'Send the network packet', align=Align.INLINE)
d.comment(0xA90F, 'Y=&20: workspace offset', align=Align.INLINE)
d.comment(0xA911, 'Set to &FF (pending)', align=Align.INLINE)
d.comment(0xA913, 'Mark send pending in workspace', align=Align.INLINE)
d.comment(0xA916, 'Also mark offset &21', align=Align.INLINE)
d.comment(0xA918, 'Y=&19: control offset', align=Align.INLINE)
d.comment(0xA91A, 'Control byte &90', align=Align.INLINE)
d.comment(0xA91C, 'Store to workspace', align=Align.INLINE)
d.comment(0xA91E, 'Y=&18: RX control offset', align=Align.INLINE)
d.comment(0xA91F, 'Control byte &7F', align=Align.INLINE)
d.comment(0xA921, 'Store RX control', align=Align.INLINE)
d.comment(0xA923, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xA926, 'Save processor flags', align=Align.INLINE)
d.comment(0xA927, 'Y=1: PB offset for station', align=Align.INLINE)
d.comment(0xA929, 'Load station number from PB', align=Align.INLINE)
d.comment(0xA92B, 'X = station number', align=Align.INLINE)
d.comment(0xA92D, 'Load network number from PB', align=Align.INLINE)
d.comment(0xA92F, 'Y=3: workspace start offset', align=Align.INLINE)
d.comment(0xA930, 'Store Y as ws_ptr_lo', align=Align.INLINE)
d.comment(0xA932, 'Y=&72: workspace offset for dest', align=Align.INLINE)
d.comment(0xA934, 'Store network to workspace', align=Align.INLINE)
d.comment(0xA936, 'Y=&71', align=Align.INLINE)
d.comment(0xA937, 'A = station (from X)', align=Align.INLINE)
d.comment(0xA938, 'Store station to workspace', align=Align.INLINE)
d.comment(0xA93A, 'Restore flags from PHP', align=Align.INLINE)
d.comment(0xA93B, 'Non-zero sub-code: handle burst', align=Align.INLINE)
d.comment(0xA93D, 'Load current offset', align=Align.INLINE)
d.comment(0xA93F, 'Advance offset for next byte', align=Align.INLINE)
d.comment(0xA941, 'Load next char from PB', align=Align.INLINE)
d.comment(0xA943, 'Zero: end of data, return', align=Align.INLINE)
d.comment(0xA945, 'Y=&7D: workspace char offset', align=Align.INLINE)
d.comment(0xA947, 'Store char to RX buffer', align=Align.INLINE)
d.comment(0xA949, 'Save char for later test', align=Align.INLINE)
d.comment(0xA94A, 'Init workspace copy for wide xfer', align=Align.INLINE)
d.comment(0xA94D, 'Enable IRQ and send packet', align=Align.INLINE)
d.comment(0xA950, 'Delay countdown', align=Align.INLINE)
d.comment(0xA951, 'Loop for short delay', align=Align.INLINE)
d.comment(0xA953, 'Restore char', align=Align.INLINE)
d.comment(0xA954, 'Test if char was CR (&0D)', align=Align.INLINE)
d.comment(0xA956, 'Not CR: send next char', align=Align.INLINE)
d.comment(0xA958, 'CR sent: return', align=Align.INLINE)
d.comment(0xA959, 'Init workspace for wide copy', align=Align.INLINE)
d.comment(0xA95C, 'Y=&7B: workspace offset', align=Align.INLINE)
d.comment(0xA95E, 'Load buffer size', align=Align.INLINE)
d.comment(0xA960, 'Add 3 for header', align=Align.INLINE)
d.comment(0xA962, 'Store adjusted size', align=Align.INLINE)
d.comment(0xA964, 'Enable interrupts', align=Align.INLINE)
d.comment(0xA965, 'Send packet and return', align=Align.INLINE)
d.comment(0xA968, 'Save processor flags', align=Align.INLINE)
d.comment(0xA969, 'Save A', align=Align.INLINE)
d.comment(0xA96A, 'Save X', align=Align.INLINE)
d.comment(0xA96B, 'Push X', align=Align.INLINE)
d.comment(0xA96C, 'Save Y', align=Align.INLINE)
d.comment(0xA96D, 'Push Y', align=Align.INLINE)
d.comment(0xA96E, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA96F, 'Read OSWORD number from stack', align=Align.INLINE)
d.comment(0xA972, 'OSWORD >= 9?', align=Align.INLINE)
d.comment(0xA974, 'Yes: out of range, restore + return', align=Align.INLINE)
d.comment(0xA976, 'X = OSWORD number', align=Align.INLINE)
d.comment(0xA977, 'Push handler address for dispatch', align=Align.INLINE)
d.comment(0xA97A, 'Restore Y', align=Align.INLINE)
d.comment(0xA97B, 'Back to Y', align=Align.INLINE)
d.comment(0xA97C, 'Restore X', align=Align.INLINE)
d.comment(0xA97D, 'Back to X', align=Align.INLINE)
d.comment(0xA97E, 'Restore A', align=Align.INLINE)
d.comment(0xA97F, 'Restore processor flags', align=Align.INLINE)
d.comment(0xA980, 'RTS dispatches via pushed address', align=Align.INLINE)
d.comment(0xA981, 'Load handler high byte from table', align=Align.INLINE)
d.comment(0xA984, 'Push for RTS dispatch', align=Align.INLINE)
d.comment(0xA985, 'Load handler low byte from table', align=Align.INLINE)
d.comment(0xA988, 'Push for RTS dispatch', align=Align.INLINE)
d.comment(0xA989, 'Reload OSWORD number for handler', align=Align.INLINE)
d.comment(0xA98B, 'RTS will dispatch to handler', align=Align.INLINE)
d.comment(0xA9AC, 'Y=&D9: workspace abort offset', align=Align.INLINE)
d.comment(0xA9AE, 'Store abort code to workspace', align=Align.INLINE)
d.comment(0xA9B0, 'Control byte &80 (abort)', align=Align.INLINE)
d.comment(0xA9B2, 'Y=&0C: control offset', align=Align.INLINE)
d.comment(0xA9B4, 'Store control byte', align=Align.INLINE)
d.comment(0xA9B6, 'Save current TX ptr low', align=Align.INLINE)
d.comment(0xA9B8, 'Push on stack', align=Align.INLINE)
d.comment(0xA9B9, 'Save current TX ptr high', align=Align.INLINE)
d.comment(0xA9BB, 'Push on stack', align=Align.INLINE)
d.comment(0xA9BC, 'Set TX ptr to workspace offset', align=Align.INLINE)
d.comment(0xA9BE, 'Load workspace high byte', align=Align.INLINE)
d.comment(0xA9C0, 'Set TX ptr high', align=Align.INLINE)
d.comment(0xA9C2, 'Send the abort packet', align=Align.INLINE)
d.comment(0xA9C5, 'Set status to &3F (complete)', align=Align.INLINE)
d.comment(0xA9C7, 'Store at TX ptr offset 0', align=Align.INLINE)
d.comment(0xA9C9, 'Restore TX ptr high', align=Align.INLINE)
d.comment(0xA9CA, 'Back to net_tx_ptr_hi', align=Align.INLINE)
d.comment(0xA9CC, 'Restore TX ptr low', align=Align.INLINE)
d.comment(0xA9CD, 'Back to net_tx_ptr', align=Align.INLINE)
d.comment(0xA9CF, 'Return', align=Align.INLINE)
d.comment(0xA9D0, 'Load PB pointer high', align=Align.INLINE)
d.comment(0xA9D2, 'Compare with &81 (special case)', align=Align.INLINE)
d.comment(0xA9D4, 'Match: skip to processing', align=Align.INLINE)
d.comment(0xA9D6, 'Y=1: first claim code position', align=Align.INLINE)
d.comment(0xA9D8, 'X=&0A: 11 codes to check', align=Align.INLINE)
d.comment(0xA9DA, 'Search claim code table', align=Align.INLINE)
d.comment(0xA9DD, 'Found: skip to processing', align=Align.INLINE)
d.comment(0xA9DF, 'Try second table range', align=Align.INLINE)
d.comment(0xA9E0, 'Y=-1: flag second range', align=Align.INLINE)
d.comment(0xA9E1, 'X=&11: 18 codes to check', align=Align.INLINE)
d.comment(0xA9E3, 'Search claim code table', align=Align.INLINE)
d.comment(0xA9E6, 'Found: skip to processing', align=Align.INLINE)
d.comment(0xA9E8, 'Not found: increment Y', align=Align.INLINE)
d.comment(0xA9E9, 'X=2: default state', align=Align.INLINE)
d.comment(0xA9EB, 'A = Y (search result)', align=Align.INLINE)
d.comment(0xA9EC, 'Zero: not found, return', align=Align.INLINE)
d.comment(0xA9EE, 'Save result flags', align=Align.INLINE)
d.comment(0xA9EF, 'Positive: use state X=2', align=Align.INLINE)
d.comment(0xA9F2, 'Y=&DC: workspace offset for save', align=Align.INLINE)
d.comment(0xA9F4, 'Load tube claim ID byte', align=Align.INLINE)
d.comment(0xA9F7, 'Store to workspace', align=Align.INLINE)
d.comment(0xA9F9, 'Next byte down', align=Align.INLINE)
d.comment(0xA9FA, 'Until Y reaches &DA', align=Align.INLINE)
d.comment(0xA9FC, 'Loop for 3 bytes', align=Align.INLINE)
d.comment(0xA9FE, 'A = state (2 or 3)', align=Align.INLINE)
d.comment(0xA9FF, 'Send abort with state code', align=Align.INLINE)
d.comment(0xAA02, 'Restore flags', align=Align.INLINE)
d.comment(0xAA03, 'Positive: return without poll', align=Align.INLINE)
d.comment(0xAA05, 'Set control to &7F', align=Align.INLINE)
d.comment(0xAA07, 'Y=&0C: control offset', align=Align.INLINE)
d.comment(0xAA09, 'Store control byte', align=Align.INLINE)
d.comment(0xAA0B, 'Load status from workspace', align=Align.INLINE)
d.comment(0xAA0D, 'Positive: keep waiting', align=Align.INLINE)
d.comment(0xAA0F, 'Get stack pointer', align=Align.INLINE)
d.comment(0xAA10, 'Y=&DD: workspace result offset', align=Align.INLINE)
d.comment(0xAA12, 'Load result byte', align=Align.INLINE)
d.comment(0xAA14, 'Set bit 6 and bit 2', align=Align.INLINE)
d.comment(0xAA16, 'Always branch (NZ from ORA)', align=Align.INLINE)
d.comment(0xAA18, 'Previous workspace byte', align=Align.INLINE)
d.comment(0xAA19, 'Previous stack position', align=Align.INLINE)
d.comment(0xAA1A, 'Load workspace byte', align=Align.INLINE)
d.comment(0xAA1C, "Store to caller's stack frame", align=Align.INLINE)
d.comment(0xAA1F, 'Reached start of save area?', align=Align.INLINE)
d.comment(0xAA21, 'No: copy next byte', align=Align.INLINE)
d.comment(0xAA23, 'Return', align=Align.INLINE)
d.comment(0xAA24, 'Compare A with code at index X', align=Align.INLINE)
d.comment(0xAA27, 'Match: return with Z set', align=Align.INLINE)
d.comment(0xAA29, 'Try next code', align=Align.INLINE)
d.comment(0xAA2A, 'More codes: continue search', align=Align.INLINE)
d.comment(0xAA2C, 'Return (Z clear = not found)', align=Align.INLINE)
d.comment(0xAA2D, """OSWORD claim code table

Table of OSWORD numbers that trigger NMI
claim processing. Searched in two passes by
the OSWORD 7 handler: first the 11-entry
range (indices 0-&0A), then the full 18-entry
range (indices 0-&11). A match in the first
range sets state 2 (standard claim); a match
only in the extended range sets state 3.""")
d.comment(0xAA2D, 'Range 1+2: OSWORD &04', align=Align.INLINE)
d.comment(0xAA2E, 'Range 1+2: OSWORD &09', align=Align.INLINE)
d.comment(0xAA2F, 'Range 1+2: OSWORD &0A', align=Align.INLINE)
d.comment(0xAA30, 'Range 1+2: OSWORD &14', align=Align.INLINE)
d.comment(0xAA31, 'Range 1+2: OSWORD &15', align=Align.INLINE)
d.comment(0xAA32, 'Range 1+2: OSWORD &9A', align=Align.INLINE)
d.comment(0xAA33, 'Range 1+2: OSWORD &9B', align=Align.INLINE)
d.comment(0xAA34, 'Range 1+2: OSWORD &E1', align=Align.INLINE)
d.comment(0xAA35, 'Range 1+2: OSWORD &E2', align=Align.INLINE)
d.comment(0xAA36, 'Range 1+2: OSWORD &E3', align=Align.INLINE)
d.comment(0xAA37, 'Range 1+2: OSWORD &E4', align=Align.INLINE)
d.comment(0xAA38, 'Range 2 only: OSWORD &0B', align=Align.INLINE)
d.comment(0xAA39, 'Range 2 only: OSWORD &0C', align=Align.INLINE)
d.comment(0xAA3A, 'Range 2 only: OSWORD &0F', align=Align.INLINE)
d.comment(0xAA3B, 'Range 2 only: OSWORD &79', align=Align.INLINE)
d.comment(0xAA3C, 'Range 2 only: OSWORD &7A', align=Align.INLINE)
d.comment(0xAA3D, 'Range 2 only: OSWORD &86', align=Align.INLINE)
d.comment(0xAA3E, 'Range 2 only: OSWORD &87', align=Align.INLINE)
d.comment(0xAA3F, 'Y=&0E: copy 15 bytes (0-14)', align=Align.INLINE)
d.comment(0xAA41, 'OSWORD 7?', align=Align.INLINE)
d.comment(0xAA43, 'Yes: handle', align=Align.INLINE)
d.comment(0xAA45, 'OSWORD 8?', align=Align.INLINE)
d.comment(0xAA47, 'No: return', align=Align.INLINE)
d.comment(0xAA49, 'Workspace low = &DB', align=Align.INLINE)
d.comment(0xAA4B, 'Set nfs_workspace low byte', align=Align.INLINE)
d.comment(0xAA4D, 'Load PB[Y]', align=Align.INLINE)
d.comment(0xAA4F, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0xAA51, 'Next byte down', align=Align.INLINE)
d.comment(0xAA52, 'Loop for 15 bytes', align=Align.INLINE)
d.comment(0xAA54, 'Y=0', align=Align.INLINE)
d.comment(0xAA55, 'Workspace low = &DA', align=Align.INLINE)
d.comment(0xAA57, 'Load OSWORD number', align=Align.INLINE)
d.comment(0xAA59, 'Store at workspace+0 (= &DA)', align=Align.INLINE)
d.comment(0xAA5B, 'Workspace low = 0 (restore)', align=Align.INLINE)
d.comment(0xAA5D, 'Y=&14: control offset', align=Align.INLINE)
d.comment(0xAA5F, 'Control value &E9', align=Align.INLINE)
d.comment(0xAA61, 'Store to workspace+&14', align=Align.INLINE)
d.comment(0xAA63, 'Abort code = 1', align=Align.INLINE)
d.comment(0xAA65, 'Send abort packet', align=Align.INLINE)
d.comment(0xAA68, 'Restore nfs_workspace low', align=Align.INLINE)
d.comment(0xA99E, 'Get stack pointer', align=Align.INLINE)
d.comment(0xA99F, 'Clear bit 0 of stacked P (carry)', align=Align.INLINE)
d.comment(0xA9A2, 'Shift back (clears carry flag)', align=Align.INLINE)
d.comment(0xA9A5, 'A = original Y', align=Align.INLINE)
d.comment(0xA9A6, 'Y=&DA: workspace offset', align=Align.INLINE)
d.comment(0xA9A8, 'Store Y to workspace', align=Align.INLINE)
d.comment(0xA9AA, 'Abort code = 0', align=Align.INLINE)
d.comment(0xAA6A, 'X=&0D: 14 bytes to copy', align=Align.INLINE)
d.comment(0xAA6C, 'Y=&7C: workspace destination offset', align=Align.INLINE)
d.comment(0xAA6E, 'Test bit 6 via BIT (V flag check)', align=Align.INLINE)
d.comment(0xAA71, 'V=1: skip to wide mode copy', align=Align.INLINE)
d.comment(0xAA73, 'Y=&17: narrow mode dest offset', align=Align.INLINE)
d.comment(0xAA75, 'X=&1A: 27 bytes to copy', align=Align.INLINE)
d.comment(0xAA77, 'Clear V flag for narrow mode', align=Align.INLINE)
d.comment(0xAA78, 'Load template byte', align=Align.INLINE)
d.comment(0xAA7B, 'Is it &FE? (end marker)', align=Align.INLINE)
d.comment(0xAA7D, 'Yes: finished, set TX ptr', align=Align.INLINE)
d.comment(0xAA7F, 'Is it &FD? (skip marker)', align=Align.INLINE)
d.comment(0xAA81, 'Yes: skip store, just advance', align=Align.INLINE)
d.comment(0xAA83, 'Is it &FC? (page ptr marker)', align=Align.INLINE)
d.comment(0xAA85, 'No: use literal value', align=Align.INLINE)
d.comment(0xAA87, '&FC: load RX buffer page', align=Align.INLINE)
d.comment(0xAA89, 'V=1: use net_rx_ptr_hi', align=Align.INLINE)
d.comment(0xAA8B, 'V=0: use nfs_workspace_hi', align=Align.INLINE)
d.comment(0xAA8D, 'Store as TX ptr high', align=Align.INLINE)
d.comment(0xAA8F, 'V=1: store to net_rx_ptr target', align=Align.INLINE)
d.comment(0xAA91, 'V=0: store to nfs_workspace', align=Align.INLINE)
d.comment(0xAA93, 'Continue to next byte', align=Align.INLINE)
d.comment(0xAA95, 'V=1: store to net_rx_ptr', align=Align.INLINE)
d.comment(0xAA97, 'Advance workspace offset down', align=Align.INLINE)
d.comment(0xAA98, 'Advance template index', align=Align.INLINE)
d.comment(0xAA99, 'More bytes: continue copy', align=Align.INLINE)
d.comment(0xAA9B, 'Adjust Y for start of TX data', align=Align.INLINE)
d.comment(0xAA9C, 'Set net_tx_ptr from Y', align=Align.INLINE)
d.comment(0xAA9E, 'Return', align=Align.INLINE)
d.comment(0xAA9F, """Workspace TXCB init template

39-byte template with three overlapping
regions, each a TXCB/RXCB structure:
  Wide  [0..13]:  ws+&6F..&7C via net_rx_ptr
  Narrow [14..26]: ws+&0C..&17 via workspace
  Spool [27..38]:  ws+&01..&0B via workspace
Markers: &FE=end, &FD=skip, &FC=page ptr.""")
d.comment(0xAA9F, 'Wide &6F: ctrl=&85', align=Align.INLINE)
d.comment(0xAAA0, 'Wide &70: port=&00', align=Align.INLINE)
d.comment(0xAAA1, 'Wide &71: skip (dest station)', align=Align.INLINE)
d.comment(0xAAA2, 'Wide &72: skip (dest network)', align=Align.INLINE)
d.comment(0xAAA3, 'Wide &73: buf start lo=&7D', align=Align.INLINE)
d.comment(0xAAA4, 'Wide &74: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAAA5, 'Wide &75: buf start ext lo', align=Align.INLINE)
d.comment(0xAAA6, 'Wide &76: buf start ext hi', align=Align.INLINE)
d.comment(0xAAA7, 'Wide &77: buf end lo=&7E', align=Align.INLINE)
d.comment(0xAAA8, 'Wide &78: buf end hi=page ptr', align=Align.INLINE)
d.comment(0xAAA9, 'Wide &79: buf end ext lo', align=Align.INLINE)
d.comment(0xAAAA, 'Wide &7A: buf end ext hi', align=Align.INLINE)
d.comment(0xAAAB, 'Wide &7B: zero', align=Align.INLINE)
d.comment(0xAAAC, 'Wide &7C: zero', align=Align.INLINE)
d.comment(0xAAAD, 'Narrow stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAAAE, 'Narrow &0C: ctrl=&80 (standard)', align=Align.INLINE)
d.comment(0xAAAF, 'Narrow &0D: port=&93', align=Align.INLINE)
d.comment(0xAAB0, 'Narrow &0E: skip (dest station)', align=Align.INLINE)
d.comment(0xAAB1, 'Narrow &0F: skip (dest network)', align=Align.INLINE)
d.comment(0xAAB2, 'Narrow &10: buf start lo=&D9', align=Align.INLINE)
d.comment(0xAAB3, 'Narrow &11: buf start hi=page ptr', align=Align.INLINE)
d.comment(0xAAB4, 'Narrow &12: buf start ext lo', align=Align.INLINE)
d.comment(0xAAB5, 'Narrow &13: buf start ext hi', align=Align.INLINE)
d.comment(0xAAB6, 'Narrow &14: buf end lo=&DE', align=Align.INLINE)
d.comment(0xAAB7, 'Narrow &15: buf end hi=page ptr', align=Align.INLINE)
d.comment(0xAAB8, 'Narrow &16: buf end ext lo', align=Align.INLINE)
d.comment(0xAAB9, 'Narrow &17: buf end ext hi', align=Align.INLINE)
d.comment(0xAABA, 'Spool stop (&FE terminator)', align=Align.INLINE)
d.comment(0xAABB, 'Spool &01: port=&D1', align=Align.INLINE)
d.comment(0xAABC, 'Spool &02: skip (dest station)', align=Align.INLINE)
d.comment(0xAABD, 'Spool &03: skip (dest network)', align=Align.INLINE)
d.comment(0xAABE, 'Spool &04: buf start lo=&25', align=Align.INLINE)
d.comment(0xAABF, 'Spool &05: skip (buf start hi)', align=Align.INLINE)
d.comment(0xAAC0, 'Spool &06: buf start ext lo', align=Align.INLINE)
d.comment(0xAAC1, 'Spool &07: buf start ext hi', align=Align.INLINE)
d.comment(0xAAC2, 'Spool &08: skip (buf end lo)', align=Align.INLINE)
d.comment(0xAAC3, 'Spool &09: skip (buf end hi)', align=Align.INLINE)
d.comment(0xAAC4, 'Spool &0A: buf end ext lo', align=Align.INLINE)
d.comment(0xAAC5, 'Spool &0B: buf end ext hi', align=Align.INLINE)
d.comment(0xAAC6, 'X = X - 1', align=Align.INLINE)
d.comment(0xAAC7, 'Match osword_pb_ptr?', align=Align.INLINE)
d.comment(0xAAC9, 'No: return (not our PB)', align=Align.INLINE)
d.comment(0xAACB, 'Load spool state byte', align=Align.INLINE)
d.comment(0xAACD, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAACE, 'C=1: already active, return', align=Align.INLINE)
d.comment(0xAAD0, 'Buffer start at &25', align=Align.INLINE)
d.comment(0xAAD2, 'Store as buffer pointer', align=Align.INLINE)
d.comment(0xAAD5, 'Control state &41', align=Align.INLINE)
d.comment(0xAAD7, 'Store as spool control state', align=Align.INLINE)
d.comment(0xAADA, 'Return', align=Align.INLINE)
d.comment(0xAADB, 'Check Y == 4', align=Align.INLINE)
d.comment(0xAADD, 'No: return', align=Align.INLINE)
d.comment(0xAADF, 'A = X (control byte)', align=Align.INLINE)
d.comment(0xAAE0, 'Decrement X', align=Align.INLINE)
d.comment(0xAAE1, 'Non-zero: handle spool ctrl byte', align=Align.INLINE)
d.comment(0xAAE3, 'Get stack pointer', align=Align.INLINE)
d.comment(0xAAE4, 'OR with stack value', align=Align.INLINE)
d.comment(0xAAE7, 'Store back to stack', align=Align.INLINE)
d.comment(0xAAEA, 'OSBYTE &91: read buffer', align=Align.INLINE)
d.comment(0xAAEC, 'X=3: printer buffer', align=Align.INLINE)
d.comment(0xAAEE, 'Read character from buffer', align=Align.INLINE)
d.comment(0xAAF1, 'C=1: buffer empty, return', align=Align.INLINE)
d.comment(0xAAF3, 'A = extracted character', align=Align.INLINE)
d.comment(0xAAF4, 'Add byte to RX buffer', align=Align.INLINE)
d.comment(0xAAF7, 'Buffer past &6E limit?', align=Align.INLINE)
d.comment(0xAAF9, 'No: read more from buffer', align=Align.INLINE)
d.comment(0xAAFB, 'Buffer full: send packet', align=Align.INLINE)
d.comment(0xAAFE, 'More room: continue reading', align=Align.INLINE)
d.comment(0xAB00, 'Load current buffer index', align=Align.INLINE)
d.comment(0xAB03, 'Store byte at buffer position', align=Align.INLINE)
d.comment(0xAB05, 'Advance buffer index', align=Align.INLINE)
d.comment(0xAB08, 'Return', align=Align.INLINE)
d.comment(0xAB09, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAB0A, 'Bit 0 clear: not active path', align=Align.INLINE)
d.comment(0xAB0C, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB0F, 'Save for bit test', align=Align.INLINE)
d.comment(0xAB10, 'Rotate bit 0 into carry', align=Align.INLINE)
d.comment(0xAB11, 'Restore state', align=Align.INLINE)
d.comment(0xAB12, 'C=1: already started, reset', align=Align.INLINE)
d.comment(0xAB14, 'Set bits 0-1 (active + pending)', align=Align.INLINE)
d.comment(0xAB16, 'Store updated state', align=Align.INLINE)
d.comment(0xAB19, 'Control byte 3 for header', align=Align.INLINE)
d.comment(0xAB1B, 'Add to RX buffer', align=Align.INLINE)
d.comment(0xAB1E, 'Send current buffer', align=Align.INLINE)
d.comment(0xAB21, 'Reset spool buffer state', align=Align.INLINE)
d.comment(0xAB24, 'Y=8: workspace offset for length', align=Align.INLINE)
d.comment(0xAB26, 'Load buffer index (=length)', align=Align.INLINE)
d.comment(0xAB29, 'Store length to workspace', align=Align.INLINE)
d.comment(0xAB2B, 'Set data page high byte', align=Align.INLINE)
d.comment(0xAB2E, 'Store to workspace+9', align=Align.INLINE)
d.comment(0xAB30, 'Y=5: workspace offset', align=Align.INLINE)
d.comment(0xAB32, 'Store page to workspace+5', align=Align.INLINE)
d.comment(0xAB34, 'Y=&0B: template start offset', align=Align.INLINE)
d.comment(0xAB36, 'X=&26: template index', align=Align.INLINE)
d.comment(0xAB38, 'Copy template to workspace', align=Align.INLINE)
d.comment(0xAB3B, 'Adjust Y down', align=Align.INLINE)
d.comment(0xAB3C, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB3F, 'Save state', align=Align.INLINE)
d.comment(0xAB40, 'Rotate to get carry (bit 7)', align=Align.INLINE)
d.comment(0xAB41, 'Restore state', align=Align.INLINE)
d.comment(0xAB42, 'Toggle bit 7', align=Align.INLINE)
d.comment(0xAB44, 'Store updated state', align=Align.INLINE)
d.comment(0xAB47, 'Shift to get both flag bits', align=Align.INLINE)
d.comment(0xAB48, 'Store flags to workspace', align=Align.INLINE)
d.comment(0xAB4A, 'Save l00d0 (exec flag)', align=Align.INLINE)
d.comment(0xAB4C, 'Push for later restore', align=Align.INLINE)
d.comment(0xAB4D, 'Clear bit 0 of exec flag', align=Align.INLINE)
d.comment(0xAB4F, 'Store modified exec flag', align=Align.INLINE)
d.comment(0xAB51, 'Reset buffer start to &25', align=Align.INLINE)
d.comment(0xAB53, 'Store reset buffer index', align=Align.INLINE)
d.comment(0xAB56, 'A=0 for disconnect reply', align=Align.INLINE)
d.comment(0xAB58, 'X=0', align=Align.INLINE)
d.comment(0xAB59, 'Y = workspace page', align=Align.INLINE)
d.comment(0xAB5B, 'Enable interrupts', align=Align.INLINE)
d.comment(0xAB5C, 'Send disconnect reply packet', align=Align.INLINE)
d.comment(0xAB5F, 'Restore exec flag', align=Align.INLINE)
d.comment(0xAB60, 'Store original exec flag', align=Align.INLINE)
d.comment(0xAB62, 'Return', align=Align.INLINE)
d.comment(0xAB63, 'Load spool control state', align=Align.INLINE)
d.comment(0xAB66, 'Rotate bit 0 to carry', align=Align.INLINE)
d.comment(0xAB67, 'C=0: send current buffer', align=Align.INLINE)
d.comment(0xAB69, 'Save exec flag', align=Align.INLINE)
d.comment(0xAB6B, 'Push for restore', align=Align.INLINE)
d.comment(0xAB6C, 'Clear bit 0', align=Align.INLINE)
d.comment(0xAB6E, 'Store modified flag', align=Align.INLINE)
d.comment(0xAB70, 'Control byte &14 (repeat count)', align=Align.INLINE)
d.comment(0xAB72, 'Save retry count', align=Align.INLINE)
d.comment(0xAB73, 'X=&0B: 12 bytes of template', align=Align.INLINE)
d.comment(0xAB75, 'Y=&30: workspace offset for TXCB', align=Align.INLINE)
d.comment(0xAB77, 'Load template byte', align=Align.INLINE)
d.comment(0xAB7A, 'Store to workspace', align=Align.INLINE)
d.comment(0xAB7C, 'Next byte down', align=Align.INLINE)
d.comment(0xAB7D, 'Next template byte', align=Align.INLINE)
d.comment(0xAB7E, 'Loop for 12 bytes', align=Align.INLINE)
d.comment(0xAB80, 'X=-1: disable escape checking', align=Align.INLINE)
d.comment(0xAB82, 'Y=2: workspace offset for station', align=Align.INLINE)
d.comment(0xAB84, 'Load station number', align=Align.INLINE)
d.comment(0xAB86, 'Save station', align=Align.INLINE)
d.comment(0xAB88, 'Load network number', align=Align.INLINE)
d.comment(0xAB8A, 'Y=&28: TXCB dest network offset', align=Align.INLINE)
d.comment(0xAB8C, 'Store network to TXCB', align=Align.INLINE)
d.comment(0xAB8E, 'Y=&27', align=Align.INLINE)
d.comment(0xAB8F, 'Restore station', align=Align.INLINE)
d.comment(0xAB90, 'Store station to TXCB', align=Align.INLINE)
d.comment(0xAB92, 'X=&0B: 12 bytes of RX template', align=Align.INLINE)
d.comment(0xAB94, 'Y=&0B: workspace RX offset', align=Align.INLINE)
d.comment(0xAB96, 'Load RX template byte', align=Align.INLINE)
d.comment(0xAB99, 'Is it &FD? (skip marker)', align=Align.INLINE)
d.comment(0xAB9B, 'Yes: skip store', align=Align.INLINE)
d.comment(0xAB9D, 'Is it &FC? (page ptr marker)', align=Align.INLINE)
d.comment(0xAB9F, 'No: use literal value', align=Align.INLINE)
d.comment(0xABA1, '&FC: substitute RX buffer page', align=Align.INLINE)
d.comment(0xABA3, 'Store to workspace', align=Align.INLINE)
d.comment(0xABA5, 'Next byte down', align=Align.INLINE)
d.comment(0xABA6, 'Next template byte', align=Align.INLINE)
d.comment(0xABA7, 'Loop for 12 bytes', align=Align.INLINE)
d.comment(0xABA9, 'TX data start at &25', align=Align.INLINE)
d.comment(0xABAB, 'Set net_tx_ptr low', align=Align.INLINE)
d.comment(0xABAD, 'Set data page high byte', align=Align.INLINE)
d.comment(0xABAF, 'Set net_tx_ptr high', align=Align.INLINE)
d.comment(0xABB1, 'Set up password in TX buffer', align=Align.INLINE)
d.comment(0xABB4, 'Send the packet', align=Align.INLINE)
d.comment(0xABB7, 'Clear net_tx_ptr low (page base)', align=Align.INLINE)
d.comment(0xABB9, 'Store zero', align=Align.INLINE)
d.comment(0xABBB, 'Set TX high to workspace page', align=Align.INLINE)
d.comment(0xABBD, 'Store workspace high byte', align=Align.INLINE)
d.comment(0xABBF, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xABC2, 'Y=&31: check reply status', align=Align.INLINE)
d.comment(0xABC4, 'Load reply byte', align=Align.INLINE)
d.comment(0xABC6, 'Zero: success', align=Align.INLINE)
d.comment(0xABC8, 'Status = 3? (busy, can retry)', align=Align.INLINE)
d.comment(0xABCA, 'Other error: handle failure', align=Align.INLINE)
d.comment(0xABCC, 'Discard retry count', align=Align.INLINE)
d.comment(0xABCD, 'Discard saved exec flag', align=Align.INLINE)
d.comment(0xABCE, 'Restore l00d0', align=Align.INLINE)
d.comment(0xABD0, 'A=0: null terminator', align=Align.INLINE)
d.comment(0xABD2, 'Add zero to RX buffer (end marker)', align=Align.INLINE)
d.comment(0xABD5, 'Send final buffer', align=Align.INLINE)
d.comment(0xABD8, 'Load spool state', align=Align.INLINE)
d.comment(0xABDB, 'Clear low nibble', align=Align.INLINE)
d.comment(0xABDD, 'Store cleaned state', align=Align.INLINE)
d.comment(0xABE0, 'Return', align=Align.INLINE)
d.comment(0xABE1, 'X = error code', align=Align.INLINE)
d.comment(0xABE2, 'Restore retry count', align=Align.INLINE)
d.comment(0xABE3, 'Set carry for subtract', align=Align.INLINE)
d.comment(0xABE4, 'Decrement retry count', align=Align.INLINE)
d.comment(0xABE6, 'Non-zero: retry send', align=Align.INLINE)
d.comment(0xABE8, 'Error code = 1? (busy)', align=Align.INLINE)
d.comment(0xABEA, 'No: printer jammed error', align=Align.INLINE)
d.comment(0xABEC, 'A=&A6: printer busy error number', align=Align.INLINE)
d.comment(0xABEE, "Generate 'Printer busy' error", align=Align.INLINE)
d.comment(0xABFE, 'A=&A7: printer jammed error number', align=Align.INLINE)
d.comment(0xAC00, "Generate 'Printer jammed' error", align=Align.INLINE)
d.comment(0xAC12, 'Set TX ptr low byte', align=Align.INLINE)
d.comment(0xAC14, 'Set TX ptr high byte', align=Align.INLINE)
d.comment(0xAC16, 'Save disconnect code', align=Align.INLINE)
d.comment(0xAC17, 'Test if zero', align=Align.INLINE)
d.comment(0xAC19, 'Zero: skip station search', align=Align.INLINE)
d.comment(0xAC1B, 'X=&FF: start search from -1', align=Align.INLINE)
d.comment(0xAC1D, 'Y = disconnect code', align=Align.INLINE)
d.comment(0xAC1E, 'A = disconnect code', align=Align.INLINE)
d.comment(0xAC1F, 'Next station index', align=Align.INLINE)
d.comment(0xAC20, 'Compare with station table entry', align=Align.INLINE)
d.comment(0xAC23, 'Match: verify station/network', align=Align.INLINE)
d.comment(0xAC25, 'Past last station?', align=Align.INLINE)
d.comment(0xAC27, 'No: try next', align=Align.INLINE)
d.comment(0xAC29, 'Not found: A=0', align=Align.INLINE)
d.comment(0xAC2B, 'Skip to status update', align=Align.INLINE)
d.comment(0xAC2D, 'Y = disconnect code for compare', align=Align.INLINE)
d.comment(0xAC2E, 'Check station and network match', align=Align.INLINE)
d.comment(0xAC31, 'No match: try next station', align=Align.INLINE)
d.comment(0xAC33, 'Load station status flags', align=Align.INLINE)
d.comment(0xAC36, 'Isolate bit 0 (active flag)', align=Align.INLINE)
d.comment(0xAC38, 'Y=0: TX buffer status offset', align=Align.INLINE)
d.comment(0xAC3A, 'OR with existing status byte', align=Align.INLINE)
d.comment(0xAC3C, 'Save combined status', align=Align.INLINE)
d.comment(0xAC3D, 'Store to TX buffer', align=Align.INLINE)
d.comment(0xAC3F, 'Send the packet', align=Align.INLINE)
d.comment(0xAC42, 'Set end markers to &FF', align=Align.INLINE)
d.comment(0xAC44, 'Y=8: first end marker offset', align=Align.INLINE)
d.comment(0xAC46, 'Store &FF', align=Align.INLINE)
d.comment(0xAC49, 'Store &FF at offset 9 too', align=Align.INLINE)
d.comment(0xAC4B, 'Restore disconnect code', align=Align.INLINE)
d.comment(0xAC4C, 'X = status for control byte', align=Align.INLINE)
d.comment(0xAC4D, 'Y=&D1: default control', align=Align.INLINE)
d.comment(0xAC4F, 'Check original disconnect code', align=Align.INLINE)
d.comment(0xAC50, 'Peek but keep on stack', align=Align.INLINE)
d.comment(0xAC51, 'Zero: use &D1 control', align=Align.INLINE)
d.comment(0xAC53, 'Non-zero: use &90 control', align=Align.INLINE)
d.comment(0xAC55, 'A = control byte (Y)', align=Align.INLINE)
d.comment(0xAC56, 'Y=1: control byte offset', align=Align.INLINE)
d.comment(0xAC58, 'Store control byte', align=Align.INLINE)
d.comment(0xAC5A, 'A = X (status)', align=Align.INLINE)
d.comment(0xAC5B, 'Y=0', align=Align.INLINE)
d.comment(0xAC5C, 'Save status on stack', align=Align.INLINE)
d.comment(0xAC5D, 'Set status to &7F (waiting)', align=Align.INLINE)
d.comment(0xAC5F, 'Store at TX buffer offset 0', align=Align.INLINE)
d.comment(0xAC61, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0xAC64, 'Restore status', align=Align.INLINE)
d.comment(0xAC65, 'Keep on stack for next check', align=Align.INLINE)
d.comment(0xAC66, 'Compare with current TX buffer', align=Align.INLINE)
d.comment(0xAC68, 'Rotate result bit 0 to carry', align=Align.INLINE)
d.comment(0xAC69, 'C=1: status changed, retry', align=Align.INLINE)
d.comment(0xAC6B, 'Done: discard status', align=Align.INLINE)
d.comment(0xAC6C, 'Discard disconnect code', align=Align.INLINE)
d.comment(0xAC6D, 'Return', align=Align.INLINE)
d.comment(0xAC6E, """Spool TX control block template

12-byte TXCB template copied directly (no
marker processing) to workspace at offset
&25..&30. Destination station and network
(&27/&28) are filled in from (nfs_workspace)
after the copy.""")
d.comment(0xAC6E, 'ctrl=&80 (standard TX)', align=Align.INLINE)
d.comment(0xAC6F, 'port=&9F', align=Align.INLINE)
d.comment(0xAC70, 'dest station=&00 (filled later)', align=Align.INLINE)
d.comment(0xAC71, 'dest network=&00 (filled later)', align=Align.INLINE)
d.comment(0xAC72, 'buf start lo=&43', align=Align.INLINE)
d.comment(0xAC73, 'buf start hi=&8E', align=Align.INLINE)
d.comment(0xAC74, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xAC75, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xAC76, 'buf end lo=&4B', align=Align.INLINE)
d.comment(0xAC77, 'buf end hi=&8E', align=Align.INLINE)
d.comment(0xAC78, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xAC79, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xAC7A, """Spool RX control block template

12-byte RXCB template with marker processing:
&FD skips the offset (preserves existing value)
and &FC substitutes net_rx_ptr_hi. Copied to
workspace at offset &00..&0B. Sets up a 3-byte
receive buffer at &xx31..&xx34.""")
d.comment(0xAC7A, 'ctrl=&7F (RX listen)', align=Align.INLINE)
d.comment(0xAC7B, 'port=&9E', align=Align.INLINE)
d.comment(0xAC7C, 'skip: preserve dest station', align=Align.INLINE)
d.comment(0xAC7D, 'skip: preserve dest network', align=Align.INLINE)
d.comment(0xAC7E, 'buf start lo=&31', align=Align.INLINE)
d.comment(0xAC7F, 'buf start hi=page ptr (&FC)', align=Align.INLINE)
d.comment(0xAC80, 'buf start ext lo=&FF', align=Align.INLINE)
d.comment(0xAC81, 'buf start ext hi=&FF', align=Align.INLINE)
d.comment(0xAC82, 'buf end lo=&34', align=Align.INLINE)
d.comment(0xAC83, 'buf end hi=page ptr (&FC)', align=Align.INLINE)
d.comment(0xAC84, 'buf end ext lo=&FF', align=Align.INLINE)
d.comment(0xAC85, 'buf end ext hi=&FF', align=Align.INLINE)
d.comment(0xAC86, 'Save l00ad counter', align=Align.INLINE)
d.comment(0xAC88, 'Push for later restore', align=Align.INLINE)
d.comment(0xAC89, 'Set workspace low to &E9', align=Align.INLINE)
d.comment(0xAC8B, 'Store to nfs_workspace low', align=Align.INLINE)
d.comment(0xAC8D, 'Y=0: initial palette index', align=Align.INLINE)
d.comment(0xAC8F, 'Clear palette counter', align=Align.INLINE)
d.comment(0xAC91, 'Load current screen mode', align=Align.INLINE)
d.comment(0xAC94, 'Store mode to workspace', align=Align.INLINE)
d.comment(0xAC96, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xAC98, 'Load video ULA copy', align=Align.INLINE)
d.comment(0xAC9B, 'Save for later restore', align=Align.INLINE)
d.comment(0xAC9C, 'A=0 for first palette entry', align=Align.INLINE)
d.comment(0xAC9D, 'Store logical colour to workspace', align=Align.INLINE)
d.comment(0xAC9F, 'X = workspace ptr low', align=Align.INLINE)
d.comment(0xACA1, 'Y = workspace ptr high', align=Align.INLINE)
d.comment(0xACA3, 'OSWORD &0B: read palette', align=Align.INLINE)
d.comment(0xACA5, 'Read palette entry', align=Align.INLINE)
d.comment(0xACA8, 'Restore previous ULA value', align=Align.INLINE)
d.comment(0xACA9, 'Y=0: reset index', align=Align.INLINE)
d.comment(0xACAB, 'Store ULA value to workspace', align=Align.INLINE)
d.comment(0xACAD, 'Y=1: physical colour offset', align=Align.INLINE)
d.comment(0xACAE, 'Load physical colour', align=Align.INLINE)
d.comment(0xACB0, 'Save for next iteration', align=Align.INLINE)
d.comment(0xACB1, 'X = workspace ptr', align=Align.INLINE)
d.comment(0xACB3, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACB5, 'Advance palette counter', align=Align.INLINE)
d.comment(0xACB7, 'Y=0', align=Align.INLINE)
d.comment(0xACB8, 'Load counter', align=Align.INLINE)
d.comment(0xACBA, 'Reached &F9 workspace limit?', align=Align.INLINE)
d.comment(0xACBC, 'No: read next palette entry', align=Align.INLINE)
d.comment(0xACBE, 'Discard last ULA value', align=Align.INLINE)
d.comment(0xACBF, 'Clear counter', align=Align.INLINE)
d.comment(0xACC1, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACC3, 'Store extra palette info', align=Align.INLINE)
d.comment(0xACC6, 'Advance workspace ptr again', align=Align.INLINE)
d.comment(0xACC8, 'Restore original l00ad', align=Align.INLINE)
d.comment(0xACC9, 'Store restored counter', align=Align.INLINE)
d.comment(0xACCB, 'Load current state', align=Align.INLINE)
d.comment(0xACCE, 'Store as committed state', align=Align.INLINE)
d.comment(0xACD1, 'Return', align=Align.INLINE)
d.comment(0xACD2, 'Load palette register value', align=Align.INLINE)
d.comment(0xACD5, 'Store to workspace', align=Align.INLINE)
d.comment(0xACD7, 'X = palette register', align=Align.INLINE)
d.comment(0xACDA, 'Read OSBYTE for this mode', align=Align.INLINE)
d.comment(0xACDD, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACDF, 'A=0', align=Align.INLINE)
d.comment(0xACE0, 'Store zero to workspace', align=Align.INLINE)
d.comment(0xACE2, 'Read OSBYTE with X=0', align=Align.INLINE)
d.comment(0xACE5, 'X=0: read mode info', align=Align.INLINE)
d.comment(0xACE7, 'Load OSBYTE code index', align=Align.INLINE)
d.comment(0xACE9, 'Advance index counter', align=Align.INLINE)
d.comment(0xACEB, 'Advance workspace ptr', align=Align.INLINE)
d.comment(0xACED, 'Load OSBYTE number from table', align=Align.INLINE)
d.comment(0xACF0, 'Y=&FF: read current value', align=Align.INLINE)
d.comment(0xACF2, 'Call OSBYTE to read value', align=Align.INLINE)
d.comment(0xACF5, 'A = result (from X)', align=Align.INLINE)
d.comment(0xACF6, 'X=0 for indexed store', align=Align.INLINE)
d.comment(0xACF8, 'Store result to workspace', align=Align.INLINE)
d.comment(0xACFA, 'Return', align=Align.INLINE)
d.comment(0xACFB, """OSBYTE mode read codes

Three OSBYTE numbers used by read_osbyte_to_ws
to save display mode state to workspace before
a language 2 file transfer.""")
d.comment(0xACFB, 'OSBYTE &85: read display start addr', align=Align.INLINE)
d.comment(0xACFC, 'OSBYTE &C2: read video ULA ctrl', align=Align.INLINE)
d.comment(0xACFD, 'OSBYTE &C3: read video ULA palette', align=Align.INLINE)
d.comment(0xBA06, 'Open file for reading, set ws_page', align=Align.INLINE)
d.comment(0xBA09, '21 bytes to push (0-&14)', align=Align.INLINE)
d.comment(0xBA0B, 'Zero fill value', align=Align.INLINE)
d.comment(0xBA0D, 'Push zero onto stack', align=Align.INLINE)
d.comment(0xBA0E, 'Count down', align=Align.INLINE)
d.comment(0xBA0F, 'Loop until all 21 bytes pushed', align=Align.INLINE)
d.comment(0xBA11, 'X = stack pointer (buffer base - 1)', align=Align.INLINE)
d.comment(0xBA12, 'Set up buffer pointer and parse args', align=Align.INLINE)
d.comment(0xBA15, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBA17, 'Test high nibble', align=Align.INLINE)
d.comment(0xBA19, 'Skip header if 16-byte aligned', align=Align.INLINE)
d.comment(0xBA1B, 'Print column header for offset start', align=Align.INLINE)
d.comment(0xBA1E, 'Check for Escape key', align=Align.INLINE)
d.comment(0xBA21, 'Start byte counter at -1', align=Align.INLINE)
d.comment(0xBA23, 'Reset counter', align=Align.INLINE)
d.comment(0xBA2A, 'C=1 from OSBGET: end of file', align=Align.INLINE)
d.comment(0xBA2C, 'Increment byte counter (0-15)', align=Align.INLINE)
d.comment(0xBA2E, 'Use counter as buffer index', align=Align.INLINE)
d.comment(0xBA30, 'Store byte in data buffer', align=Align.INLINE)
d.comment(0xBA32, 'Read 16 bytes? (index 0-15)', align=Align.INLINE)
d.comment(0xBA34, 'No: read next byte', align=Align.INLINE)
d.comment(0xBA36, 'C=0: not EOF, full line read', align=Align.INLINE)
d.comment(0xBA37, 'Save C: EOF status', align=Align.INLINE)
d.comment(0xBA38, 'Check byte counter', align=Align.INLINE)
d.comment(0xBA3A, 'Counter >= 0: have data to display', align=Align.INLINE)
d.comment(0xBA3C, '22 bytes to pop (21 buffer + PHP)', align=Align.INLINE)
d.comment(0xBA3E, 'Pop one byte from stack', align=Align.INLINE)
d.comment(0xBA3F, 'Count down', align=Align.INLINE)
d.comment(0xBA40, 'Loop until stack cleaned up', align=Align.INLINE)
d.comment(0xBA42, 'Close file and return', align=Align.INLINE)
d.comment(0xBA45, 'Point to display address low byte', align=Align.INLINE)
d.comment(0xBA47, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBA49, 'Test high nibble', align=Align.INLINE)
d.comment(0xBA4B, 'Non-zero: header already current', align=Align.INLINE)
d.comment(0xBA4D, 'Crossed 256-byte boundary: new header', align=Align.INLINE)
d.comment(0xBA50, 'Start from highest address byte', align=Align.INLINE)
d.comment(0xBA52, 'Load address byte', align=Align.INLINE)
d.comment(0xBA54, 'Save for address increment later', align=Align.INLINE)
d.comment(0xBA55, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBA58, 'Restore address byte', align=Align.INLINE)
d.comment(0xBA59, 'Next byte down', align=Align.INLINE)
d.comment(0xBA5A, 'Printed all 4 address bytes?', align=Align.INLINE)
d.comment(0xBA5C, 'No: print next address byte', align=Align.INLINE)
d.comment(0xBA5E, 'Y=&10: point to address byte 0', align=Align.INLINE)
d.comment(0xBA5F, 'Prepare for 16-byte add', align=Align.INLINE)
d.comment(0xBA60, 'Add 16 to lowest address byte', align=Align.INLINE)
d.comment(0xBA62, 'Save carry for propagation', align=Align.INLINE)
d.comment(0xBA63, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0xBA64, 'Store updated address byte', align=Align.INLINE)
d.comment(0xBA66, 'Next address byte up', align=Align.INLINE)
d.comment(0xBA67, 'Load next address byte', align=Align.INLINE)
d.comment(0xBA69, 'Add carry', align=Align.INLINE)
d.comment(0xBA6B, 'Save carry for next byte', align=Align.INLINE)
d.comment(0xBA6C, 'Past all 4 address bytes?', align=Align.INLINE)
d.comment(0xBA6E, 'No: continue propagation', align=Align.INLINE)
d.comment(0xBA70, 'Discard final carry', align=Align.INLINE)
d.comment(0xBA71, 'Print address/data separator', align=Align.INLINE)
d.comment(0xBA77, 'Start from first data byte', align=Align.INLINE)
d.comment(0xBA79, 'X = bytes read (counter for display)', align=Align.INLINE)
d.comment(0xBA7B, 'Load data byte from buffer', align=Align.INLINE)
d.comment(0xBA7D, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBA80, 'Space separator', align=Align.INLINE)
d.comment(0xBA82, 'Print space between hex bytes', align=Align.INLINE)
d.comment(0xBA85, 'Next column', align=Align.INLINE)
d.comment(0xBA86, 'All 16 columns done?', align=Align.INLINE)
d.comment(0xBA88, 'Yes: go to ASCII separator', align=Align.INLINE)
d.comment(0xBA8A, 'Decrement remaining data bytes', align=Align.INLINE)
d.comment(0xBA8B, 'More data: print next hex byte', align=Align.INLINE)
d.comment(0xBA8D, 'Save column position', align=Align.INLINE)
d.comment(0xBA8E, 'Preserve Y across print', align=Align.INLINE)
d.comment(0xBA8F, 'Print 3-space padding', align=Align.INLINE)
d.comment(0xBA95, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xBA96, 'Restore column position', align=Align.INLINE)
d.comment(0xBA97, 'Back to Y', align=Align.INLINE)
d.comment(0xBA98, 'Check next column', align=Align.INLINE)
d.comment(0xBA9B, 'Adjust X for advance_x_by_8', align=Align.INLINE)
d.comment(0xBA9C, 'Print hex/ASCII separator', align=Align.INLINE)
d.comment(0xBAA1, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xBAA2, 'X += 16: restore byte count for ASCII', align=Align.INLINE)
d.comment(0xBAA5, 'Start from first data byte', align=Align.INLINE)
d.comment(0xBAA7, 'Load data byte', align=Align.INLINE)
d.comment(0xBAA9, 'Strip high bit', align=Align.INLINE)
d.comment(0xBAAB, 'Printable? (>= space)', align=Align.INLINE)
d.comment(0xBAAD, 'Yes: check for DEL', align=Align.INLINE)
d.comment(0xBAAF, "Non-printable: substitute '.'", align=Align.INLINE)
d.comment(0xBAB1, 'Is it DEL (&7F)?', align=Align.INLINE)
d.comment(0xBAB3, "Yes: substitute '.'", align=Align.INLINE)
d.comment(0xBAB5, 'Print ASCII character', align=Align.INLINE)
d.comment(0xBAB8, 'Next column', align=Align.INLINE)
d.comment(0xBAB9, 'All 16 columns done?', align=Align.INLINE)
d.comment(0xBABB, 'Yes: end of line', align=Align.INLINE)
d.comment(0xBABD, 'Decrement remaining data bytes', align=Align.INLINE)
d.comment(0xBABE, 'More data: print next ASCII char', align=Align.INLINE)
d.comment(0xBAC0, 'Print newline', align=Align.INLINE)
d.comment(0xBAC3, 'Restore EOF status from &BA37', align=Align.INLINE)
d.comment(0xBAC4, 'C=1: EOF reached, clean up', align=Align.INLINE)
d.comment(0xBAC6, 'Not EOF: continue with next line', align=Align.INLINE)
d.comment(0xBAC9, '21 bytes to pop (buffer only, PHP done)', align=Align.INLINE)
d.comment(0xBACB, 'Reuse stack cleanup loop', align=Align.INLINE)
d.comment(0xBACE, 'Load display address low byte', align=Align.INLINE)
d.comment(0xBAD0, 'Save as starting column number', align=Align.INLINE)
d.comment(0xBAD1, 'Print header label with leading CR', align=Align.INLINE)
d.comment(0xBAE0, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xBAE1, 'Restore starting column number', align=Align.INLINE)
d.comment(0xBAE2, '16 column headers to print', align=Align.INLINE)
d.comment(0xBAE4, 'Save current column number', align=Align.INLINE)
d.comment(0xBAE5, 'Print as two hex digits', align=Align.INLINE)
d.comment(0xBAE8, 'Space separator', align=Align.INLINE)
d.comment(0xBAEA, 'Print space after column number', align=Align.INLINE)
d.comment(0xBAED, 'Restore column number', align=Align.INLINE)
d.comment(0xBAEE, 'SEC for +1 via ADC', align=Align.INLINE)
d.comment(0xBAEF, 'Increment column number (SEC+ADC 0=+1)', align=Align.INLINE)
d.comment(0xBAF1, 'Wrap to low nibble (0-F)', align=Align.INLINE)
d.comment(0xBAF3, 'Count down', align=Align.INLINE)
d.comment(0xBAF4, 'Loop for all 16 columns', align=Align.INLINE)
d.comment(0xBAF6, 'Print trailer with ASCII label', align=Align.INLINE)
d.comment(0xBB0A, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xBB0B, 'Return', align=Align.INLINE)
d.comment(0xBB0C, 'Y = file handle from ws_page', align=Align.INLINE)
d.comment(0xBB0E, 'A=0: close file', align=Align.INLINE)
d.comment(0xBB10, 'Close file and return', align=Align.INLINE)
d.comment(0xBB13, 'Save processor flags', align=Align.INLINE)
d.comment(0xBB14, 'A = filename offset', align=Align.INLINE)
d.comment(0xBB15, 'Add to command text pointer', align=Align.INLINE)
d.comment(0xBB16, 'Low byte of filename address', align=Align.INLINE)
d.comment(0xBB18, 'Save on stack for later restore', align=Align.INLINE)
d.comment(0xBB19, 'X = filename address low', align=Align.INLINE)
d.comment(0xBB1A, 'Carry into high byte', align=Align.INLINE)
d.comment(0xBB1C, 'High byte of filename address', align=Align.INLINE)
d.comment(0xBB1E, 'Save on stack for later restore', align=Align.INLINE)
d.comment(0xBB1F, 'Y = filename address high', align=Align.INLINE)
d.comment(0xBB20, 'Open for input', align=Align.INLINE)
d.comment(0xBB22, 'OSFIND: open file', align=Align.INLINE)
d.comment(0xBB26, 'Store file handle', align=Align.INLINE)
d.comment(0xBB28, 'Non-zero: file opened OK', align=Align.INLINE)
d.comment(0xBB2A, 'Error number &D6', align=Align.INLINE)
d.comment(0xBB2C, "Generate 'Not found' error", align=Align.INLINE)
d.comment(0xBB39, 'Restore saved text pointer high', align=Align.INLINE)
d.comment(0xBB3A, 'Restore os_text_ptr high byte', align=Align.INLINE)
d.comment(0xBB3C, 'Restore saved text pointer low', align=Align.INLINE)
d.comment(0xBB3D, 'Restore os_text_ptr low byte', align=Align.INLINE)
d.comment(0xBB3F, 'Start scanning from offset 0', align=Align.INLINE)
d.comment(0xBB41, 'Advance past current char', align=Align.INLINE)
d.comment(0xBB42, 'Load next char from command line', align=Align.INLINE)
d.comment(0xBB44, 'CR: end of command line', align=Align.INLINE)
d.comment(0xBB46, 'Yes: done scanning', align=Align.INLINE)
d.comment(0xBB48, 'Space: end of filename', align=Align.INLINE)
d.comment(0xBB4A, 'No: keep scanning filename', align=Align.INLINE)
d.comment(0xBB4C, 'Advance past space', align=Align.INLINE)
d.comment(0xBB4D, 'Load next char', align=Align.INLINE)
d.comment(0xBB4F, 'Still a space?', align=Align.INLINE)
d.comment(0xBB51, 'Yes: skip it', align=Align.INLINE)
d.comment(0xBB53, 'Restore processor flags', align=Align.INLINE)
d.comment(0xBB54, 'Return; Y = offset to next argument', align=Align.INLINE)
d.comment(0xBB55, 'Save command line offset to X', align=Align.INLINE)
d.comment(0xBB56, 'X tracks current position', align=Align.INLINE)
d.comment(0xBB57, 'Zero for clearing accumulator', align=Align.INLINE)
d.comment(0xBB59, 'Y=0 for buffer indexing', align=Align.INLINE)
d.comment(0xBB5A, 'Clear accumulator byte', align=Align.INLINE)
d.comment(0xBB5C, 'Next byte', align=Align.INLINE)
d.comment(0xBB5D, 'All 4 bytes cleared?', align=Align.INLINE)
d.comment(0xBB5F, 'No: clear next', align=Align.INLINE)
d.comment(0xBB61, 'Restore pre-increment offset to A', align=Align.INLINE)
d.comment(0xBB62, 'Advance X to next char position', align=Align.INLINE)
d.comment(0xBB63, 'Y = pre-increment offset for indexing', align=Align.INLINE)
d.comment(0xBB64, 'Load character from command line', align=Align.INLINE)
d.comment(0xBB66, 'CR: end of input', align=Align.INLINE)
d.comment(0xBB68, 'Done: skip trailing spaces', align=Align.INLINE)
d.comment(0xBB6A, 'Space: end of this parameter', align=Align.INLINE)
d.comment(0xBB6C, 'Done: skip trailing spaces', align=Align.INLINE)
d.comment(0xBB6E, "Below '0'?", align=Align.INLINE)
d.comment(0xBB70, 'Yes: not a hex digit, error', align=Align.INLINE)
d.comment(0xBB72, "Below ':'? (i.e. '0'-'9')", align=Align.INLINE)
d.comment(0xBB74, 'Yes: is a decimal digit', align=Align.INLINE)
d.comment(0xBB76, 'Force uppercase for A-F', align=Align.INLINE)
d.comment(0xBB78, "Map 'A'-'F' → &FA-&FF (C=0 here)", align=Align.INLINE)
d.comment(0xBB7A, "Carry set: char > 'F', error", align=Align.INLINE)
d.comment(0xBB7C, "Below &FA? (i.e. was < 'A')", align=Align.INLINE)
d.comment(0xBB7E, "Yes: gap between '9' and 'A', error", align=Align.INLINE)
d.comment(0xBB80, 'Mask to low nibble (0-15)', align=Align.INLINE)
d.comment(0xBB82, 'Save hex digit value', align=Align.INLINE)
d.comment(0xBB83, 'Save current offset', align=Align.INLINE)
d.comment(0xBB84, 'Preserve on stack', align=Align.INLINE)
d.comment(0xBB85, '4 bits to shift in', align=Align.INLINE)
d.comment(0xBB87, 'Start from byte 0 (LSB)', align=Align.INLINE)
d.comment(0xBB89, 'Clear A; C from PHA/PLP below', align=Align.INLINE)
d.comment(0xBB8A, 'Transfer carry bit to flags via stack', align=Align.INLINE)
d.comment(0xBB8B, 'PLP: C = bit shifted out of prev iter', align=Align.INLINE)
d.comment(0xBB8C, 'Load accumulator byte', align=Align.INLINE)
d.comment(0xBB8E, 'Rotate left through carry', align=Align.INLINE)
d.comment(0xBB8F, 'Store shifted byte', align=Align.INLINE)
d.comment(0xBB91, 'Save carry for next byte', align=Align.INLINE)
d.comment(0xBB92, 'Transfer to A for PHA/PLP trick', align=Align.INLINE)
d.comment(0xBB93, 'Next accumulator byte', align=Align.INLINE)
d.comment(0xBB94, 'All 4 bytes rotated?', align=Align.INLINE)
d.comment(0xBB96, 'No: rotate next byte', align=Align.INLINE)
d.comment(0xBB98, 'Transfer carry to flags', align=Align.INLINE)
d.comment(0xBB99, 'C = overflow bit', align=Align.INLINE)
d.comment(0xBB9A, 'Overflow: address too large', align=Align.INLINE)
d.comment(0xBB9C, 'Count bits shifted', align=Align.INLINE)
d.comment(0xBB9D, '4 bits shifted? No: shift again', align=Align.INLINE)
d.comment(0xBB9F, 'Restore command line offset', align=Align.INLINE)
d.comment(0xBBA0, 'Back to X', align=Align.INLINE)
d.comment(0xBBA1, 'Restore hex digit value', align=Align.INLINE)
d.comment(0xBBA2, 'Point to LSB of accumulator', align=Align.INLINE)
d.comment(0xBBA4, 'OR digit into low nibble', align=Align.INLINE)
d.comment(0xBBA6, 'Store updated LSB', align=Align.INLINE)
d.comment(0xBBA8, 'Parse next character', align=Align.INLINE)
d.comment(0xBBAB, 'Discard saved offset', align=Align.INLINE)
d.comment(0xBBAC, 'Discard saved digit', align=Align.INLINE)
d.comment(0xBBAD, 'C=1: overflow', align=Align.INLINE)
d.comment(0xBBAE, 'Return with C=1', align=Align.INLINE)
d.comment(0xBBAF, 'Close open file before error', align=Align.INLINE)
d.comment(0xBBB2, "Generate 'Bad hex' error", align=Align.INLINE)
d.comment(0xBBB5, 'Advance past space', align=Align.INLINE)
d.comment(0xBBB6, 'Load next char', align=Align.INLINE)
d.comment(0xBBB8, 'Space?', align=Align.INLINE)
d.comment(0xBBBA, 'Yes: skip it', align=Align.INLINE)
d.comment(0xBBBC, 'C=0: valid parse (no overflow)', align=Align.INLINE)
d.comment(0xBBBD, 'Return; Y past trailing spaces', align=Align.INLINE)
d.comment(0xBBBE, 'X+1: first byte of buffer', align=Align.INLINE)
d.comment(0xBBBF, 'Set buffer pointer low byte', align=Align.INLINE)
d.comment(0xBBC1, 'Buffer is on stack in page 1', align=Align.INLINE)
d.comment(0xBBC3, 'Set buffer pointer high byte', align=Align.INLINE)
d.comment(0xBBC5, 'Parse start offset from command line', align=Align.INLINE)
d.comment(0xBBC8, "Overflow: 'Outside file' error", align=Align.INLINE)
d.comment(0xBBCA, 'A = command line offset after parse', align=Align.INLINE)
d.comment(0xBBCB, 'Save for later (past start addr)', align=Align.INLINE)
d.comment(0xBBD0, 'A=2: read file extent (length)', align=Align.INLINE)
d.comment(0xBBD5, 'Check from MSB down', align=Align.INLINE)
d.comment(0xBBD7, 'Load file length byte', align=Align.INLINE)
d.comment(0xBBDA, 'Compare with start offset byte', align=Align.INLINE)
d.comment(0xBBDC, 'Mismatch: check which is larger', align=Align.INLINE)
d.comment(0xBBDE, 'Next byte down', align=Align.INLINE)
d.comment(0xBBDF, 'More bytes to compare', align=Align.INLINE)
d.comment(0xBBE1, 'All equal: start = length, within file', align=Align.INLINE)
d.comment(0xBBE3, 'Length < start: outside file', align=Align.INLINE)
d.comment(0xBBE5, 'Y=&FF: length > start, flag for later', align=Align.INLINE)
d.comment(0xBBE7, 'Continue to copy start address', align=Align.INLINE)
d.comment(0xBBE9, 'Close file before error', align=Align.INLINE)
d.comment(0xBBEC, 'Error number &B7', align=Align.INLINE)
d.comment(0xBBEE, "Generate 'Outside file' error", align=Align.INLINE)
d.comment(0xBBFE, 'Load start address byte from buffer', align=Align.INLINE)
d.comment(0xBC00, 'Store to osword_flag (&AA-&AD)', align=Align.INLINE)
d.comment(0xBC03, 'Next byte', align=Align.INLINE)
d.comment(0xBC04, 'All 4 bytes copied?', align=Align.INLINE)
d.comment(0xBC06, 'No: copy next byte', align=Align.INLINE)
d.comment(0xBC0C, 'A=1: write file pointer', align=Align.INLINE)
d.comment(0xBC0E, 'OSARGS: set file pointer', align=Align.INLINE)
d.comment(0xBC11, 'Restore saved command line offset', align=Align.INLINE)
d.comment(0xBC12, 'Back to Y for command line indexing', align=Align.INLINE)
d.comment(0xBC13, 'Load next char from command line', align=Align.INLINE)
d.comment(0xBC15, 'End of command? (CR)', align=Align.INLINE)
d.comment(0xBC17, 'No: parse display base address', align=Align.INLINE)
d.comment(0xBC19, 'Copy 2 bytes: os_text_ptr to buffer', align=Align.INLINE)
d.comment(0xBC1B, 'Load os_text_ptr byte', align=Align.INLINE)
d.comment(0xBC1E, 'Store as filename pointer in OSFILE CB', align=Align.INLINE)
d.comment(0xBC20, 'Next byte', align=Align.INLINE)
d.comment(0xBC21, 'Copy both low and high bytes', align=Align.INLINE)
d.comment(0xBC23, 'Read catalogue information', align=Align.INLINE)
d.comment(0xBC25, 'X = control block low', align=Align.INLINE)
d.comment(0xBC27, 'Y = control block high', align=Align.INLINE)
d.comment(0xBC29, 'OSFILE: read file info', align=Align.INLINE)
d.comment(0xBC2C, 'Start at OSFILE +2 (load addr byte 0)', align=Align.INLINE)
d.comment(0xBC2E, 'Load from OSFILE result offset', align=Align.INLINE)
d.comment(0xBC30, 'Y-2: destination is 2 bytes earlier', align=Align.INLINE)
d.comment(0xBC31, 'Continue decrement', align=Align.INLINE)
d.comment(0xBC32, 'Store to buf[Y-2]', align=Align.INLINE)
d.comment(0xBC34, 'Y += 3: advance source index', align=Align.INLINE)
d.comment(0xBC35, '(continued)', align=Align.INLINE)
d.comment(0xBC36, '(continued)', align=Align.INLINE)
d.comment(0xBC37, 'Copied all 4 load address bytes?', align=Align.INLINE)
d.comment(0xBC39, 'No: copy next byte', align=Align.INLINE)
d.comment(0xBC3B, 'Y=6 after loop exit', align=Align.INLINE)
d.comment(0xBC3C, 'Y=4: check from buf[4] downward', align=Align.INLINE)
d.comment(0xBC3D, 'Load address byte', align=Align.INLINE)
d.comment(0xBC3F, 'Is it &FF?', align=Align.INLINE)
d.comment(0xBC41, 'No: valid load address, use it', align=Align.INLINE)
d.comment(0xBC43, 'Check next byte down', align=Align.INLINE)
d.comment(0xBC44, 'More bytes to check', align=Align.INLINE)
d.comment(0xBC46, 'Clear all 4 bytes', align=Align.INLINE)
d.comment(0xBC48, 'Zero value', align=Align.INLINE)
d.comment(0xBC4A, 'Clear byte', align=Align.INLINE)
d.comment(0xBC4C, 'Next byte down', align=Align.INLINE)
d.comment(0xBC4D, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC4F, 'Continue to compute display address', align=Align.INLINE)
d.comment(0xBC51, 'Parse second hex parameter', align=Align.INLINE)
d.comment(0xBC54, 'Valid: use as display base', align=Align.INLINE)
d.comment(0xBC56, 'Invalid: close file before error', align=Align.INLINE)
d.comment(0xBC59, 'Error number &FC', align=Align.INLINE)
d.comment(0xBC5B, "Generate 'Bad address' error", align=Align.INLINE)
d.comment(0xBC66, 'Start from LSB', align=Align.INLINE)
d.comment(0xBC68, '4 bytes to add', align=Align.INLINE)
d.comment(0xBC6A, 'Clear carry for addition', align=Align.INLINE)
d.comment(0xBC6B, 'Load display base byte', align=Align.INLINE)
d.comment(0xBC6D, 'Add start offset byte', align=Align.INLINE)
d.comment(0xBC70, 'Store result in osword_flag', align=Align.INLINE)
d.comment(0xBC73, 'Next byte', align=Align.INLINE)
d.comment(0xBC74, 'Count down', align=Align.INLINE)
d.comment(0xBC75, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC77, 'Point past end of address area', align=Align.INLINE)
d.comment(0xBC79, 'Start from MSB (byte 3)', align=Align.INLINE)
d.comment(0xBC7B, 'Pre-decrement Y', align=Align.INLINE)
d.comment(0xBC7C, 'Load computed display address byte', align=Align.INLINE)
d.comment(0xBC7E, 'Store to buf[&10-&13]', align=Align.INLINE)
d.comment(0xBC80, 'Next byte down', align=Align.INLINE)
d.comment(0xBC81, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0xBC83, 'Return; Y=&10 (address low byte)', align=Align.INLINE)
d.comment(0xBC84, 'JSR+fall-through: 8+8=16 INXs total', align=Align.INLINE)
d.comment(0xBC87, 'JSR+fall-through: 4+4=8 INXs', align=Align.INLINE)
d.comment(0xBC8A, 'X += 4', align=Align.INLINE)
d.comment(0xBC8B, '(continued)', align=Align.INLINE)
d.comment(0xBC8C, '(continued)', align=Align.INLINE)
d.comment(0xBC8D, '(continued)', align=Align.INLINE)
d.comment(0xBC8E, 'Return', align=Align.INLINE)
d.comment(0xBC8F, 'Padding; next byte is reloc_p5_src', align=Align.INLINE)
d.comment(0xB33D, 'Mask owner access flags to 5 bits', align=Align.INLINE)
d.comment(0xB340, 'Initialise file index to 0', align=Align.INLINE)
d.comment(0xB342, 'Store file counter', align=Align.INLINE)
d.comment(0xB344, 'Save pointer to command text', align=Align.INLINE)
d.comment(0xB347, 'Parse wildcard filename argument', align=Align.INLINE)
d.comment(0xB34A, 'Advance past CR terminator', align=Align.INLINE)
d.comment(0xB34B, 'Save end-of-argument buffer position', align=Align.INLINE)
d.comment(0xB34D, 'Command code 1 = examine directory', align=Align.INLINE)
d.comment(0xB34F, 'Store command in TX buffer byte 0', align=Align.INLINE)
d.comment(0xB352, 'Store flag in TX buffer byte 2', align=Align.INLINE)
d.comment(0xB355, 'Load current file index', align=Align.INLINE)
d.comment(0xB357, 'Store file index in TX buffer byte 1', align=Align.INLINE)
d.comment(0xB35A, 'X=3: copy from TX buffer offset 3', align=Align.INLINE)
d.comment(0xB35C, 'Copy filename argument to TX buffer', align=Align.INLINE)
d.comment(0xB35F, 'Function code 3 = examine', align=Align.INLINE)
d.comment(0xB361, 'Flag &80 = escapable', align=Align.INLINE)
d.comment(0xB363, 'Mark operation as escapable', align=Align.INLINE)
d.comment(0xB365, 'Send examine request to file server', align=Align.INLINE)
d.comment(0xB368, 'Get server response status', align=Align.INLINE)
d.comment(0xB36B, 'Non-zero: file found, process it', align=Align.INLINE)
d.comment(0xB36D, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0xB36F, 'X=1: flush input buffers', align=Align.INLINE)
d.comment(0xB371, 'Flush keyboard buffer', align=Align.INLINE)
d.comment(0xB374, 'OSBYTE &7A: keyboard scan from 16', align=Align.INLINE)
d.comment(0xB376, 'Scan keyboard to clear state', align=Align.INLINE)
d.comment(0xB379, 'Y=0: no key pressed', align=Align.INLINE)
d.comment(0xB37B, 'OSBYTE &78: write keys pressed', align=Align.INLINE)
d.comment(0xB37D, 'Clear keyboard state and return', align=Align.INLINE)
d.comment(0xB380, 'Load first attribute char of response', align=Align.INLINE)
d.comment(0xB383, 'Is file locked?', align=Align.INLINE)
d.comment(0xB385, 'No: check if directory', align=Align.INLINE)
d.comment(0xB387, 'Skip locked file, advance index', align=Align.INLINE)
d.comment(0xB389, 'Request next file from server', align=Align.INLINE)
d.comment(0xB38C, 'Is it a directory entry?', align=Align.INLINE)
d.comment(0xB38E, 'No: regular file, show prompt', align=Align.INLINE)
d.comment(0xB390, 'Check directory contents flag', align=Align.INLINE)
d.comment(0xB393, 'Non-empty dir: treat as locked, skip', align=Align.INLINE)
d.comment(0xB395, 'X=1: start from response byte 1', align=Align.INLINE)
d.comment(0xB397, 'Y = destination index in delete buffer', align=Align.INLINE)
d.comment(0xB399, 'Load filename char from response', align=Align.INLINE)
d.comment(0xB39C, 'Print filename character to screen', align=Align.INLINE)
d.comment(0xB39F, 'Store in delete command buffer too', align=Align.INLINE)
d.comment(0xB3A2, 'Advance destination index', align=Align.INLINE)
d.comment(0xB3A3, 'Advance source index', align=Align.INLINE)
d.comment(0xB3A4, 'Copied all 11 filename characters?', align=Align.INLINE)
d.comment(0xB3A6, 'No: continue copying', align=Align.INLINE)
d.comment(0xB3A8, "Print '(Y/N/?) ' prompt", align=Align.INLINE)
d.comment(0xB3B3, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xB3B4, 'Read user response character', align=Align.INLINE)
d.comment(0xB3B7, "User pressed '?'?", align=Align.INLINE)
d.comment(0xB3B9, 'No: check for Y/N response', align=Align.INLINE)
d.comment(0xB3BB, 'Carriage return before full info', align=Align.INLINE)
d.comment(0xB3BD, 'Print CR', align=Align.INLINE)
d.comment(0xB3C0, 'X=2: start from response byte 2', align=Align.INLINE)
d.comment(0xB3C2, 'Load file info character', align=Align.INLINE)
d.comment(0xB3C5, 'Print file info character', align=Align.INLINE)
d.comment(0xB3C8, 'Advance to next character', align=Align.INLINE)
d.comment(0xB3C9, 'Printed all &3C info bytes?', align=Align.INLINE)
d.comment(0xB3CB, 'No: continue printing', align=Align.INLINE)
d.comment(0xB3CD, "Print ' (Y/N) ' prompt (no '?')", align=Align.INLINE)
d.comment(0xB3D7, 'Inline string terminator (NOP)', align=Align.INLINE)
d.comment(0xB3D8, 'Read user response (Y/N only)', align=Align.INLINE)
d.comment(0xB3DB, 'Force uppercase', align=Align.INLINE)
d.comment(0xB3DD, "User said 'Y' (yes)?", align=Align.INLINE)
d.comment(0xB3DF, 'No: print newline, skip to next file', align=Align.INLINE)
d.comment(0xB3E1, "Echo 'Y' to screen", align=Align.INLINE)
d.comment(0xB3E4, 'X=0: start of stored filename', align=Align.INLINE)
d.comment(0xB3E6, 'Check first byte of stored name', align=Align.INLINE)
d.comment(0xB3E9, 'Is first byte CR (empty first field)?', align=Align.INLINE)
d.comment(0xB3EB, 'Yes: use second filename field', align=Align.INLINE)
d.comment(0xB3ED, 'Load byte from stored filename', align=Align.INLINE)
d.comment(0xB3F0, 'Is it CR (field separator)?', align=Align.INLINE)
d.comment(0xB3F2, 'No: check for space', align=Align.INLINE)
d.comment(0xB3F4, "Replace CR with '.' directory sep", align=Align.INLINE)
d.comment(0xB3F6, 'Is it a space (name terminator)?', align=Align.INLINE)
d.comment(0xB3F8, 'No: keep character as-is', align=Align.INLINE)
d.comment(0xB3FA, 'Replace space with CR (end of name)', align=Align.INLINE)
d.comment(0xB3FC, 'Store in delete command TX buffer', align=Align.INLINE)
d.comment(0xB3FF, 'Advance to next character', align=Align.INLINE)
d.comment(0xB400, 'Was it the CR terminator?', align=Align.INLINE)
d.comment(0xB402, 'No: continue building delete command', align=Align.INLINE)
d.comment(0xB404, 'Function code &14 = delete file', align=Align.INLINE)
d.comment(0xB406, 'Send delete request to file server', align=Align.INLINE)
d.comment(0xB409, 'Adjust file index after deletion', align=Align.INLINE)
d.comment(0xB40B, 'Print newline after user response', align=Align.INLINE)
d.comment(0xB40E, 'Advance index, process next file', align=Align.INLINE)
d.comment(0xB411, 'DEX to offset following INX', align=Align.INLINE)
d.comment(0xB412, 'Advance to next byte', align=Align.INLINE)
d.comment(0xB413, 'Load byte from second field', align=Align.INLINE)
d.comment(0xB416, 'Store in delete command TX buffer', align=Align.INLINE)
d.comment(0xB419, 'Is it a space (field terminator)?', align=Align.INLINE)
d.comment(0xB41B, 'No: continue copying second field', align=Align.INLINE)
d.comment(0xB41D, 'Space found: terminate with CR', align=Align.INLINE)
d.comment(0xB41F, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0xB421, 'X=1: flush input buffers', align=Align.INLINE)
d.comment(0xB423, 'Flush keyboard buffer before read', align=Align.INLINE)
d.comment(0xB426, 'Read character from input stream', align=Align.INLINE)
d.comment(0xB429, 'C clear: character read OK', align=Align.INLINE)
d.comment(0xB42B, 'Escape pressed: raise error', align=Align.INLINE)
d.comment(0xB42E, 'Return with character in A', align=Align.INLINE)
d.comment(0xB42F, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB431, 'Y=&78: clear offsets &00-&77', align=Align.INLINE)
d.comment(0xB433, 'Decrement index', align=Align.INLINE)
d.comment(0xB434, 'Clear workspace byte via l00cc', align=Align.INLINE)
d.comment(0xB436, 'Loop until Y=0', align=Align.INLINE)
d.comment(0xB438, 'Return', align=Align.INLINE)
d.comment(0xB439, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB43B, 'Y=0: start index', align=Align.INLINE)
d.comment(0xB43C, 'Clear channel table entry', align=Align.INLINE)
d.comment(0xB43F, 'Next entry', align=Align.INLINE)
d.comment(0xB440, 'Loop until all 256 bytes cleared', align=Align.INLINE)
d.comment(0xB442, 'Offset &0F in receive buffer', align=Align.INLINE)
d.comment(0xB444, 'Get number of available channels', align=Align.INLINE)
d.comment(0xB446, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB447, "Subtract 'Z' to get negative count", align=Align.INLINE)
d.comment(0xB449, 'Y = negative channel count (index)', align=Align.INLINE)
d.comment(0xB44A, 'Channel marker &40 (available)', align=Align.INLINE)
d.comment(0xB44C, 'Mark channel slot as available', align=Align.INLINE)
d.comment(0xB44F, 'Previous channel slot', align=Align.INLINE)
d.comment(0xB450, 'Reached start of channel range?', align=Align.INLINE)
d.comment(0xB452, 'No: continue marking channels', align=Align.INLINE)
d.comment(0xB454, 'Point to first channel slot', align=Align.INLINE)
d.comment(0xB455, 'Active channel marker &C0', align=Align.INLINE)
d.comment(0xB457, 'Mark first channel as active', align=Align.INLINE)
d.comment(0xB45A, 'Return', align=Align.INLINE)
d.comment(0xB45B, 'Save flags', align=Align.INLINE)
d.comment(0xB45C, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB45D, 'Subtract &20 to get table index', align=Align.INLINE)
d.comment(0xB45F, 'Negative: out of valid range', align=Align.INLINE)
d.comment(0xB461, 'Above maximum channel index &0F?', align=Align.INLINE)
d.comment(0xB463, 'In range: valid index', align=Align.INLINE)
d.comment(0xB465, 'Out of range: return &FF (invalid)', align=Align.INLINE)
d.comment(0xB467, 'Restore flags', align=Align.INLINE)
d.comment(0xB468, 'X = channel index (or &FF)', align=Align.INLINE)
d.comment(0xB469, 'Return', align=Align.INLINE)
d.comment(0xB46A, 'Below space?', align=Align.INLINE)
d.comment(0xB46C, 'Yes: invalid channel character', align=Align.INLINE)
d.comment(0xB46E, "Below '0'?", align=Align.INLINE)
d.comment(0xB470, 'In range &20-&2F: look up channel', align=Align.INLINE)
d.comment(0xB472, 'Save channel character', align=Align.INLINE)
d.comment(0xB473, 'Error code &DE', align=Align.INLINE)
d.comment(0xB475, "Generate 'Net channel' error", align=Align.INLINE)
d.comment(0xB484, 'Error string continuation (unreachable)', align=Align.INLINE)
d.comment(0xB49D, 'Save channel character', align=Align.INLINE)
d.comment(0xB49E, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB49F, 'Convert char to table index', align=Align.INLINE)
d.comment(0xB4A1, 'X = channel table index', align=Align.INLINE)
d.comment(0xB4A2, 'Look up network number for channel', align=Align.INLINE)
d.comment(0xB4A5, 'Zero: channel not found, raise error', align=Align.INLINE)
d.comment(0xB4A7, 'Check station/network matches current', align=Align.INLINE)
d.comment(0xB4AA, 'No match: build detailed error msg', align=Align.INLINE)
d.comment(0xB4AC, 'Discard saved channel character', align=Align.INLINE)
d.comment(0xB4AD, 'Load channel status flags', align=Align.INLINE)
d.comment(0xB4B0, 'Return; A = channel flags', align=Align.INLINE)
d.comment(0xB4B1, 'Error code &DE', align=Align.INLINE)
d.comment(0xB4B3, 'Store error code in error block', align=Align.INLINE)
d.comment(0xB4B6, 'BRK opcode', align=Align.INLINE)
d.comment(0xB4B8, 'Store BRK at start of error block', align=Align.INLINE)
d.comment(0xB4BB, 'X=0: copy index', align=Align.INLINE)
d.comment(0xB4BC, 'Advance copy position', align=Align.INLINE)
d.comment(0xB4BD, "Load 'Net channel' string byte", align=Align.INLINE)
d.comment(0xB4C0, 'Copy to error text', align=Align.INLINE)
d.comment(0xB4C3, 'Continue until NUL terminator', align=Align.INLINE)
d.comment(0xB4C5, 'Save end-of-string position', align=Align.INLINE)
d.comment(0xB4C7, 'Save for suffix append', align=Align.INLINE)
d.comment(0xB4C9, 'Retrieve channel character', align=Align.INLINE)
d.comment(0xB4CA, "Append ' N' (channel number)", align=Align.INLINE)
d.comment(0xB4CD, "Load 'Net channel' end position", align=Align.INLINE)
d.comment(0xB4CF, 'Skip past NUL to suffix string', align=Align.INLINE)
d.comment(0xB4D0, 'Advance destination position', align=Align.INLINE)
d.comment(0xB4D1, "Load ' not on this...' suffix byte", align=Align.INLINE)
d.comment(0xB4D4, 'Append to error message', align=Align.INLINE)
d.comment(0xB4D7, 'Continue until NUL', align=Align.INLINE)
d.comment(0xB4D9, 'Raise the constructed error', align=Align.INLINE)
d.comment(0xB4DC, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xB4DF, 'Offset &0E in receive buffer', align=Align.INLINE)
d.comment(0xB4E1, 'Store attribute in receive buffer', align=Align.INLINE)
d.comment(0xB4E3, 'Validate and look up channel', align=Align.INLINE)
d.comment(0xB4E6, 'Test directory flag (bit 1)', align=Align.INLINE)
d.comment(0xB4E8, 'Not a directory: return OK', align=Align.INLINE)
d.comment(0xB4EA, 'Error code &A8', align=Align.INLINE)
d.comment(0xB4EC, "Generate 'Is a dir.' error", align=Align.INLINE)
d.comment(0xB4F9, 'Return', align=Align.INLINE)
d.comment(0xB4FA, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB4FB, 'Start scanning from FCB slot &20', align=Align.INLINE)
d.comment(0xB4FD, 'Load FCB station byte', align=Align.INLINE)
d.comment(0xB500, 'Zero: slot is free, use it', align=Align.INLINE)
d.comment(0xB502, 'Try next slot', align=Align.INLINE)
d.comment(0xB503, 'Past last FCB slot &2F?', align=Align.INLINE)
d.comment(0xB505, 'No: check next slot', align=Align.INLINE)
d.comment(0xB507, 'No free slot: discard saved attribute', align=Align.INLINE)
d.comment(0xB508, 'A=0: return failure (Z set)', align=Align.INLINE)
d.comment(0xB50A, 'Return', align=Align.INLINE)
d.comment(0xB50B, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB50C, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xB50F, 'A=0: clear value', align=Align.INLINE)
d.comment(0xB511, 'Clear FCB transfer count low', align=Align.INLINE)
d.comment(0xB514, 'Clear FCB transfer count mid', align=Align.INLINE)
d.comment(0xB517, 'Clear FCB transfer count high', align=Align.INLINE)
d.comment(0xB51A, 'Load current station number', align=Align.INLINE)
d.comment(0xB51D, 'Store station in FCB', align=Align.INLINE)
d.comment(0xB520, 'Load current network number', align=Align.INLINE)
d.comment(0xB523, 'Store network in FCB', align=Align.INLINE)
d.comment(0xB526, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB527, 'Save slot index', align=Align.INLINE)
d.comment(0xB528, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB529, 'Convert slot to channel index (0-&0F)', align=Align.INLINE)
d.comment(0xB52B, 'X = channel index', align=Align.INLINE)
d.comment(0xB52C, 'Restore A = FCB slot index', align=Align.INLINE)
d.comment(0xB52D, 'Return; A=slot, X=channel, Z clear', align=Align.INLINE)
d.comment(0xB52E, 'Save argument', align=Align.INLINE)
d.comment(0xB52F, 'A=0: allocate any available slot', align=Align.INLINE)
d.comment(0xB531, 'Try to allocate an FCB slot', align=Align.INLINE)
d.comment(0xB534, 'Success: slot allocated', align=Align.INLINE)
d.comment(0xB536, 'Error code &C0', align=Align.INLINE)
d.comment(0xB538, "Generate 'No more FCBs' error", align=Align.INLINE)
d.comment(0xB548, 'Restore argument', align=Align.INLINE)
d.comment(0xB549, 'Return', align=Align.INLINE)
d.comment(0xB54A, 'C=0: close all matching channels', align=Align.INLINE)
d.comment(0xB54B, 'Branch always to scan entry', align=Align.INLINE)
d.comment(0xB54D, 'C=1: close with write-flush', align=Align.INLINE)
d.comment(0xB54E, 'Set V flag via BIT (alternate mode)', align=Align.INLINE)
d.comment(0xB551, 'Start from FCB slot &10', align=Align.INLINE)
d.comment(0xB553, 'Previous FCB slot', align=Align.INLINE)
d.comment(0xB554, 'More slots to check', align=Align.INLINE)
d.comment(0xB556, 'All FCB slots processed, return', align=Align.INLINE)
d.comment(0xB557, 'Load channel flags for this slot', align=Align.INLINE)
d.comment(0xB55A, 'Save flags in Y', align=Align.INLINE)
d.comment(0xB55B, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xB55D, 'Not active: check station match', align=Align.INLINE)
d.comment(0xB55F, 'V clear (close all): next slot', align=Align.INLINE)
d.comment(0xB561, 'C clear: check station match', align=Align.INLINE)
d.comment(0xB563, 'Restore original flags', align=Align.INLINE)
d.comment(0xB564, 'Clear write-pending flag (bit 5)', align=Align.INLINE)
d.comment(0xB566, 'Update channel flags', align=Align.INLINE)
d.comment(0xB569, 'Next slot (V always set here)', align=Align.INLINE)
d.comment(0xB56B, 'Check if channel belongs to station', align=Align.INLINE)
d.comment(0xB56E, 'No match: skip to next slot', align=Align.INLINE)
d.comment(0xB570, 'A=0: clear channel', align=Align.INLINE)
d.comment(0xB572, 'Clear channel flags (close it)', align=Align.INLINE)
d.comment(0xB575, 'Clear network number', align=Align.INLINE)
d.comment(0xB578, 'Continue to next slot', align=Align.INLINE)
d.comment(0xB57A, 'Load FCB station number', align=Align.INLINE)
d.comment(0xB57D, 'Compare with current station (EOR)', align=Align.INLINE)
d.comment(0xB580, 'Different: Z=0, no match', align=Align.INLINE)
d.comment(0xB582, 'Load FCB network number', align=Align.INLINE)
d.comment(0xB585, 'Compare with current network (EOR)', align=Align.INLINE)
d.comment(0xB588, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)
d.comment(0xB589, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB58C, 'Set V flag (first pass marker)', align=Align.INLINE)
d.comment(0xB58F, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB590, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xB592, 'No: continue checking', align=Align.INLINE)
d.comment(0xB594, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB596, 'Back to starting slot?', align=Align.INLINE)
d.comment(0xB599, 'No: check this slot', align=Align.INLINE)
d.comment(0xB59B, 'V clear (second pass): scan empties', align=Align.INLINE)
d.comment(0xB59D, 'Clear V for second pass', align=Align.INLINE)
d.comment(0xB59E, 'Continue scanning', align=Align.INLINE)
d.comment(0xB5A0, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5A3, 'Shift bit 7 (in-use) into carry', align=Align.INLINE)
d.comment(0xB5A4, 'Not in use: skip', align=Align.INLINE)
d.comment(0xB5A6, 'Test bit 2 (modified flag)', align=Align.INLINE)
d.comment(0xB5A8, 'Modified: check further conditions', align=Align.INLINE)
d.comment(0xB5AA, 'Adjust for following INX', align=Align.INLINE)
d.comment(0xB5AB, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB5AC, 'Past end of table?', align=Align.INLINE)
d.comment(0xB5AE, 'No: continue', align=Align.INLINE)
d.comment(0xB5B0, 'Wrap around to slot 0', align=Align.INLINE)
d.comment(0xB5B2, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5B5, 'Shift bit 7 into carry', align=Align.INLINE)
d.comment(0xB5B6, 'Not in use: continue scanning', align=Align.INLINE)
d.comment(0xB5B8, 'Set carry for ROR restore', align=Align.INLINE)
d.comment(0xB5B9, 'Restore original flags', align=Align.INLINE)
d.comment(0xB5BA, 'Save flags back (mark as found)', align=Align.INLINE)
d.comment(0xB5BD, 'Restore original FCB index', align=Align.INLINE)
d.comment(0xB5C0, 'Return with found slot in X', align=Align.INLINE)
d.comment(0xB5C1, 'V set (first pass): skip modified', align=Align.INLINE)
d.comment(0xB5C3, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5C6, 'Test bit 5 (offset pending)', align=Align.INLINE)
d.comment(0xB5C8, 'Bit 5 set: skip this slot', align=Align.INLINE)
d.comment(0xB5CA, 'Use this slot', align=Align.INLINE)
d.comment(0xB5CC, 'Initial pass count = 1', align=Align.INLINE)
d.comment(0xB5CE, 'Store pass counter', align=Align.INLINE)
d.comment(0xB5D1, 'Y=0', align=Align.INLINE)
d.comment(0xB5D2, 'Clear byte counter low', align=Align.INLINE)
d.comment(0xB5D5, 'Clear offset counter', align=Align.INLINE)
d.comment(0xB5D8, 'Clear transfer flag', align=Align.INLINE)
d.comment(0xB5DB, 'A=0', align=Align.INLINE)
d.comment(0xB5DC, 'Clear 3 counter bytes', align=Align.INLINE)
d.comment(0xB5DE, 'Clear counter byte', align=Align.INLINE)
d.comment(0xB5E1, 'Next byte', align=Align.INLINE)
d.comment(0xB5E2, 'Loop for indices 2, 1, 0', align=Align.INLINE)
d.comment(0xB5E4, 'Store &FF as sentinel in l10cd', align=Align.INLINE)
d.comment(0xB5E7, 'Store &FF as sentinel in l10ce', align=Align.INLINE)
d.comment(0xB5EA, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB5EC, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB5EE, 'Return; X/Y point to &10CA', align=Align.INLINE)
d.comment(0xB5EF, 'Verify workspace checksum integrity', align=Align.INLINE)
d.comment(0xB5F2, 'Save current FCB index', align=Align.INLINE)
d.comment(0xB5F5, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB5F8, 'Shift bit 0 (active) into carry', align=Align.INLINE)
d.comment(0xB5F9, 'Not active: clear status and return', align=Align.INLINE)
d.comment(0xB5FB, 'Save current station low to stack', align=Align.INLINE)
d.comment(0xB5FE, 'Push station low', align=Align.INLINE)
d.comment(0xB5FF, 'Save current station high', align=Align.INLINE)
d.comment(0xB602, 'Push station high', align=Align.INLINE)
d.comment(0xB603, 'Load FCB station low', align=Align.INLINE)
d.comment(0xB606, 'Set as working station low', align=Align.INLINE)
d.comment(0xB609, 'Load FCB station high', align=Align.INLINE)
d.comment(0xB60C, 'Set as working station high', align=Align.INLINE)
d.comment(0xB60F, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xB612, 'Set offset to &FF (no data yet)', align=Align.INLINE)
d.comment(0xB615, 'Set pass counter to 0 (flush mode)', align=Align.INLINE)
d.comment(0xB618, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB61B, 'Transfer to A', align=Align.INLINE)
d.comment(0xB61C, 'Prepare addition', align=Align.INLINE)
d.comment(0xB61D, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB61F, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xB622, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB625, 'Test bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xB627, 'No offset: skip restore', align=Align.INLINE)
d.comment(0xB629, 'Load saved byte offset', align=Align.INLINE)
d.comment(0xB62C, 'Restore offset counter', align=Align.INLINE)
d.comment(0xB62F, 'Load FCB attribute reference', align=Align.INLINE)
d.comment(0xB632, 'Store as current reference', align=Align.INLINE)
d.comment(0xB635, 'Transfer to X', align=Align.INLINE)
d.comment(0xB636, 'Offset &0E in receive buffer', align=Align.INLINE)
d.comment(0xB638, 'Save current receive attribute', align=Align.INLINE)
d.comment(0xB63A, 'Push to stack', align=Align.INLINE)
d.comment(0xB63B, 'Restore attribute to A', align=Align.INLINE)
d.comment(0xB63C, 'Set attribute in receive buffer', align=Align.INLINE)
d.comment(0xB63E, 'X=&CA: workspace offset', align=Align.INLINE)
d.comment(0xB640, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB642, 'A=0: standard transfer mode', align=Align.INLINE)
d.comment(0xB644, 'Send data and receive response', align=Align.INLINE)
d.comment(0xB647, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB64A, 'Restore saved receive attribute', align=Align.INLINE)
d.comment(0xB64B, 'Offset &0E', align=Align.INLINE)
d.comment(0xB64D, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB64F, 'Restore station high', align=Align.INLINE)
d.comment(0xB650, 'Store station high', align=Align.INLINE)
d.comment(0xB653, 'Restore station low', align=Align.INLINE)
d.comment(0xB654, 'Store station low', align=Align.INLINE)
d.comment(0xB657, 'Mask &DC: clear bits 0, 1, 5', align=Align.INLINE)
d.comment(0xB659, 'Clear active and offset flags', align=Align.INLINE)
d.comment(0xB65C, 'Update FCB status', align=Align.INLINE)
d.comment(0xB65F, 'Return', align=Align.INLINE)
d.comment(0xB660, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xB662, 'Load TX buffer byte', align=Align.INLINE)
d.comment(0xB665, 'Save to context buffer at &10D9', align=Align.INLINE)
d.comment(0xB668, 'Load workspace byte from fs_load_addr', align=Align.INLINE)
d.comment(0xB66A, 'Save to stack', align=Align.INLINE)
d.comment(0xB66B, 'Next byte down', align=Align.INLINE)
d.comment(0xB66C, 'Loop for all 13 bytes', align=Align.INLINE)
d.comment(0xB66E, 'Y=0? (no FCB to process)', align=Align.INLINE)
d.comment(0xB670, 'Non-zero: scan and process FCBs', align=Align.INLINE)
d.comment(0xB672, 'Y=0: skip to restore workspace', align=Align.INLINE)
d.comment(0xB675, 'Save flags', align=Align.INLINE)
d.comment(0xB676, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xB678, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB679, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB67C, 'Bit 7 clear: not pending, skip', align=Align.INLINE)
d.comment(0xB67E, 'Shift bit 6 to bit 7', align=Align.INLINE)
d.comment(0xB67F, 'Bit 6 clear: skip', align=Align.INLINE)
d.comment(0xB681, "Flush this FCB's pending data", align=Align.INLINE)
d.comment(0xB684, 'Pending marker &40', align=Align.INLINE)
d.comment(0xB686, 'Mark FCB as pending-only', align=Align.INLINE)
d.comment(0xB689, 'Save flags', align=Align.INLINE)
d.comment(0xB68A, 'Find next available FCB slot', align=Align.INLINE)
d.comment(0xB68D, 'Restore flags', align=Align.INLINE)
d.comment(0xB68E, 'Load current channel attribute', align=Align.INLINE)
d.comment(0xB691, 'Store as current reference', align=Align.INLINE)
d.comment(0xB694, 'Save attribute', align=Align.INLINE)
d.comment(0xB695, 'Y = attribute index', align=Align.INLINE)
d.comment(0xB696, 'Load station for this attribute', align=Align.INLINE)
d.comment(0xB699, 'Store station in TX buffer', align=Align.INLINE)
d.comment(0xB69C, 'Restore attribute', align=Align.INLINE)
d.comment(0xB69D, 'Store attribute in FCB slot', align=Align.INLINE)
d.comment(0xB6A0, 'Load working station low', align=Align.INLINE)
d.comment(0xB6A3, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6A6, 'Store station low in FCB', align=Align.INLINE)
d.comment(0xB6A9, 'Load working station high', align=Align.INLINE)
d.comment(0xB6AC, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6AF, 'Store station high in FCB', align=Align.INLINE)
d.comment(0xB6B2, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB6B3, 'Prepare addition', align=Align.INLINE)
d.comment(0xB6B4, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB6B6, 'Store buffer address high byte', align=Align.INLINE)
d.comment(0xB6B9, 'Restore flags', align=Align.INLINE)
d.comment(0xB6BA, 'V clear: skip directory request', align=Align.INLINE)
d.comment(0xB6BC, 'Command byte = 0', align=Align.INLINE)
d.comment(0xB6BE, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6C1, 'X=1: flag byte', align=Align.INLINE)
d.comment(0xB6C2, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB6C5, 'Function code &0D', align=Align.INLINE)
d.comment(0xB6C7, 'X=5: copy 5 bytes to TX', align=Align.INLINE)
d.comment(0xB6C9, 'Send directory request to server', align=Align.INLINE)
d.comment(0xB6CC, 'Reset transfer counters', align=Align.INLINE)
d.comment(0xB6CF, 'Offset &0E', align=Align.INLINE)
d.comment(0xB6D1, 'Save current receive attribute', align=Align.INLINE)
d.comment(0xB6D3, 'Push to stack', align=Align.INLINE)
d.comment(0xB6D4, 'Load current reference', align=Align.INLINE)
d.comment(0xB6D7, 'Set in receive buffer', align=Align.INLINE)
d.comment(0xB6D9, 'Y=&10: page &10', align=Align.INLINE)
d.comment(0xB6DB, 'A=2: transfer mode 2', align=Align.INLINE)
d.comment(0xB6DD, 'Send and receive data', align=Align.INLINE)
d.comment(0xB6E0, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB6E1, 'Offset &0E', align=Align.INLINE)
d.comment(0xB6E3, 'Restore receive attribute', align=Align.INLINE)
d.comment(0xB6E5, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB6E8, 'Load pass counter', align=Align.INLINE)
d.comment(0xB6EB, 'Non-zero: data received, calc offset', align=Align.INLINE)
d.comment(0xB6ED, 'Load offset counter', align=Align.INLINE)
d.comment(0xB6F0, 'Zero: no data received at all', align=Align.INLINE)
d.comment(0xB6F2, 'Load offset counter', align=Align.INLINE)
d.comment(0xB6F5, 'Negate (ones complement)', align=Align.INLINE)
d.comment(0xB6F7, 'Clear carry for add', align=Align.INLINE)
d.comment(0xB6F8, 'Complete twos complement negation', align=Align.INLINE)
d.comment(0xB6FA, 'Store negated offset in FCB', align=Align.INLINE)
d.comment(0xB6FD, 'Set bit 5 (has saved offset)', align=Align.INLINE)
d.comment(0xB6FF, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xB702, 'Update FCB status', align=Align.INLINE)
d.comment(0xB705, 'Load buffer address high byte', align=Align.INLINE)
d.comment(0xB708, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB70A, 'A=0: pointer low byte and clear val', align=Align.INLINE)
d.comment(0xB70C, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB70E, 'Load negated offset (start of clear)', align=Align.INLINE)
d.comment(0xB711, 'Clear buffer byte', align=Align.INLINE)
d.comment(0xB713, 'Next byte', align=Align.INLINE)
d.comment(0xB714, 'Loop until page boundary', align=Align.INLINE)
d.comment(0xB716, 'Set bit 1 (active flag)', align=Align.INLINE)
d.comment(0xB718, 'Add active flag to status', align=Align.INLINE)
d.comment(0xB71B, 'Update FCB status', align=Align.INLINE)
d.comment(0xB71E, 'Y=0: start restoring workspace', align=Align.INLINE)
d.comment(0xB720, 'Restore workspace byte from stack', align=Align.INLINE)
d.comment(0xB721, 'Store to fs_load_addr workspace', align=Align.INLINE)
d.comment(0xB724, 'Next byte', align=Align.INLINE)
d.comment(0xB725, 'Restored all 13 bytes?', align=Align.INLINE)
d.comment(0xB727, 'No: continue restoring', align=Align.INLINE)
d.comment(0xB729, 'Copy 13 bytes (indices 0 to &0C)', align=Align.INLINE)
d.comment(0xB72B, 'Load saved catalog byte from &10D9', align=Align.INLINE)
d.comment(0xB72E, 'Restore to TX buffer', align=Align.INLINE)
d.comment(0xB731, 'Next byte down', align=Align.INLINE)
d.comment(0xB732, 'Loop for all bytes', align=Align.INLINE)
d.comment(0xB734, 'Return', align=Align.INLINE)
d.comment(0xB735, 'Save current context first', align=Align.INLINE)
d.comment(0xB738, 'X=&FF: start scanning from -1', align=Align.INLINE)
d.comment(0xB73A, 'Load channel attribute to match', align=Align.INLINE)
d.comment(0xB73D, 'Next FCB slot', align=Align.INLINE)
d.comment(0xB73E, 'Past end of table (&10)?', align=Align.INLINE)
d.comment(0xB740, 'No: check this slot', align=Align.INLINE)
d.comment(0xB742, 'Load channel attribute', align=Align.INLINE)
d.comment(0xB745, 'Convert to channel index', align=Align.INLINE)
d.comment(0xB748, 'Load station for this channel', align=Align.INLINE)
d.comment(0xB74B, 'Store as match target station high', align=Align.INLINE)
d.comment(0xB74E, 'Load port for this channel', align=Align.INLINE)
d.comment(0xB751, 'Store as match target station low', align=Align.INLINE)
d.comment(0xB754, 'Save context and rescan from start', align=Align.INLINE)
d.comment(0xB757, 'Load FCB status flags', align=Align.INLINE)
d.comment(0xB75A, 'Test active flag (bit 1)', align=Align.INLINE)
d.comment(0xB75C, 'Not active: skip to next', align=Align.INLINE)
d.comment(0xB75E, 'Get attribute to match', align=Align.INLINE)
d.comment(0xB75F, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xB762, 'No attribute match: skip', align=Align.INLINE)
d.comment(0xB764, 'Save matching FCB index', align=Align.INLINE)
d.comment(0xB767, 'Prepare subtraction', align=Align.INLINE)
d.comment(0xB768, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0xB76A, 'Y = channel index', align=Align.INLINE)
d.comment(0xB76B, 'Reload FCB index', align=Align.INLINE)
d.comment(0xB76E, 'Load channel station byte', align=Align.INLINE)
d.comment(0xB771, 'Compare with FCB station', align=Align.INLINE)
d.comment(0xB774, 'Station mismatch: try next', align=Align.INLINE)
d.comment(0xB776, 'Load channel network byte', align=Align.INLINE)
d.comment(0xB779, 'Compare with FCB network', align=Align.INLINE)
d.comment(0xB77C, 'Network mismatch: try next', align=Align.INLINE)
d.comment(0xB77E, 'Load FCB flags', align=Align.INLINE)
d.comment(0xB781, 'Bit 7 clear: no pending flush', align=Align.INLINE)
d.comment(0xB783, 'Clear pending flag (bit 7)', align=Align.INLINE)
d.comment(0xB785, 'Update FCB status', align=Align.INLINE)
d.comment(0xB788, 'Find new open FCB slot', align=Align.INLINE)
d.comment(0xB78B, 'Reload FCB flags', align=Align.INLINE)
d.comment(0xB78E, 'Test bit 5 (has offset data)', align=Align.INLINE)
d.comment(0xB790, 'Return; Z=1 no offset, Z=0 has data', align=Align.INLINE)
d.comment(0xB791, 'Increment byte count low', align=Align.INLINE)
d.comment(0xB794, 'No overflow: done', align=Align.INLINE)
d.comment(0xB796, 'Increment byte count mid', align=Align.INLINE)
d.comment(0xB799, 'No overflow: done', align=Align.INLINE)
d.comment(0xB79B, 'Increment byte count high', align=Align.INLINE)
d.comment(0xB79E, 'Return', align=Align.INLINE)
d.comment(0xB79F, 'Save X', align=Align.INLINE)
d.comment(0xB7A0, 'Push X to stack', align=Align.INLINE)
d.comment(0xB7A1, 'Save Y', align=Align.INLINE)
d.comment(0xB7A2, 'Push Y to stack', align=Align.INLINE)
d.comment(0xB7A3, 'Save fs_options', align=Align.INLINE)
d.comment(0xB7A5, 'Push fs_options', align=Align.INLINE)
d.comment(0xB7A6, 'Save fs_block_offset', align=Align.INLINE)
d.comment(0xB7A8, 'Push fs_block_offset', align=Align.INLINE)
d.comment(0xB7A9, 'Start from FCB slot &0F', align=Align.INLINE)
d.comment(0xB7AB, 'Store as current FCB index', align=Align.INLINE)
d.comment(0xB7AE, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB7B1, 'Get filter attribute', align=Align.INLINE)
d.comment(0xB7B2, 'Zero: process all FCBs', align=Align.INLINE)
d.comment(0xB7B4, 'Compare with FCB attribute ref', align=Align.INLINE)
d.comment(0xB7B7, 'No match: skip this FCB', align=Align.INLINE)
d.comment(0xB7B9, 'Save filter attribute', align=Align.INLINE)
d.comment(0xB7BA, 'Flush pending data for this FCB', align=Align.INLINE)
d.comment(0xB7BD, 'Restore filter', align=Align.INLINE)
d.comment(0xB7BE, 'Y = filter attribute', align=Align.INLINE)
d.comment(0xB7BF, 'Previous FCB index', align=Align.INLINE)
d.comment(0xB7C2, 'More slots: continue loop', align=Align.INLINE)
d.comment(0xB7C4, 'Restore fs_block_offset', align=Align.INLINE)
d.comment(0xB7C5, 'Store fs_block_offset', align=Align.INLINE)
d.comment(0xB7C7, 'Restore fs_options', align=Align.INLINE)
d.comment(0xB7C8, 'Store fs_options', align=Align.INLINE)
d.comment(0xB7CA, 'Restore Y', align=Align.INLINE)
d.comment(0xB7CB, 'Y restored', align=Align.INLINE)
d.comment(0xB7CC, 'Restore X', align=Align.INLINE)
d.comment(0xB7CD, 'X restored', align=Align.INLINE)
d.comment(0xB7CE, 'Return', align=Align.INLINE)
d.comment(0xB7CF, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB7D2, "Save caller's X", align=Align.INLINE)
d.comment(0xB7D3, 'Push X', align=Align.INLINE)
d.comment(0xB7D4, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xB7D7, 'Load channel flags', align=Align.INLINE)
d.comment(0xB7DA, 'Test write-only flag (bit 5)', align=Align.INLINE)
d.comment(0xB7DC, 'Not write-only: proceed with read', align=Align.INLINE)
d.comment(0xB7DE, 'Error code &D4', align=Align.INLINE)
d.comment(0xB7E0, "Generate 'Write only' error", align=Align.INLINE)
d.comment(0xB7EE, 'Clear V (first-pass matching)', align=Align.INLINE)
d.comment(0xB7EF, 'Find FCB matching this channel', align=Align.INLINE)
d.comment(0xB7F2, 'No offset: read byte from buffer', align=Align.INLINE)
d.comment(0xB7F4, 'Load byte count for matching FCB', align=Align.INLINE)
d.comment(0xB7F7, 'Compare with buffer offset limit', align=Align.INLINE)
d.comment(0xB7FA, 'Below offset: data available', align=Align.INLINE)
d.comment(0xB7FC, 'Load channel flags for FCB', align=Align.INLINE)
d.comment(0xB7FF, 'Transfer to X for testing', align=Align.INLINE)
d.comment(0xB800, 'Test bit 6 (EOF already signalled)', align=Align.INLINE)
d.comment(0xB802, 'EOF already set: raise error', align=Align.INLINE)
d.comment(0xB804, 'Restore flags', align=Align.INLINE)
d.comment(0xB805, 'Set EOF flag (bit 6)', align=Align.INLINE)
d.comment(0xB807, 'Update channel flags with EOF', align=Align.INLINE)
d.comment(0xB80A, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB80C, 'Offset &0E', align=Align.INLINE)
d.comment(0xB80E, 'Clear attribute in receive buffer', align=Align.INLINE)
d.comment(0xB810, "Restore caller's X", align=Align.INLINE)
d.comment(0xB811, 'X restored', align=Align.INLINE)
d.comment(0xB812, 'A=&FE: EOF marker byte', align=Align.INLINE)
d.comment(0xB814, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB817, 'C=1: end of file', align=Align.INLINE)
d.comment(0xB818, 'Return', align=Align.INLINE)
d.comment(0xB819, 'Error code &DF', align=Align.INLINE)
d.comment(0xB81B, "Generate 'End of file' error", align=Align.INLINE)
d.comment(0xB82A, 'Load current byte count (= offset)', align=Align.INLINE)
d.comment(0xB82D, 'Save byte count', align=Align.INLINE)
d.comment(0xB82E, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB82F, 'X = FCB slot for byte count inc', align=Align.INLINE)
d.comment(0xB830, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB832, 'Offset &0E', align=Align.INLINE)
d.comment(0xB834, 'Clear attribute in receive buffer', align=Align.INLINE)
d.comment(0xB836, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xB839, 'Restore byte count (= buffer offset)', align=Align.INLINE)
d.comment(0xB83A, 'Y = offset into data buffer', align=Align.INLINE)
d.comment(0xB83B, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB83E, 'Prepare addition', align=Align.INLINE)
d.comment(0xB83F, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB841, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB843, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xB845, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB847, "Restore caller's X", align=Align.INLINE)
d.comment(0xB848, 'X restored', align=Align.INLINE)
d.comment(0xB849, 'Read data byte from buffer', align=Align.INLINE)
d.comment(0xB84B, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB84E, 'C=0: byte read successfully', align=Align.INLINE)
d.comment(0xB84F, 'Return; A = data byte', align=Align.INLINE)
d.comment(0xB850, 'Save channel attribute', align=Align.INLINE)
d.comment(0xB853, 'Save data byte', align=Align.INLINE)
d.comment(0xB854, 'Y = data byte', align=Align.INLINE)
d.comment(0xB855, "Save caller's X", align=Align.INLINE)
d.comment(0xB856, 'Push X', align=Align.INLINE)
d.comment(0xB857, 'Restore data byte to A', align=Align.INLINE)
d.comment(0xB858, 'Push data byte for later', align=Align.INLINE)
d.comment(0xB859, 'Save data byte in workspace', align=Align.INLINE)
d.comment(0xB85C, 'Store result and check not directory', align=Align.INLINE)
d.comment(0xB85F, 'Load channel flags', align=Align.INLINE)
d.comment(0xB862, 'Bit 7 set: channel open, proceed', align=Align.INLINE)
d.comment(0xB864, 'Error &C1: Not open for update', align=Align.INLINE)
d.comment(0xB866, 'Raise error with inline string', align=Align.INLINE)
d.comment(0xB87D, 'Test write flag (bit 5)', align=Align.INLINE)
d.comment(0xB87F, 'Not write-capable: use buffer path', align=Align.INLINE)
d.comment(0xB881, 'Load reply port for this channel', align=Align.INLINE)
d.comment(0xB884, 'Restore data byte', align=Align.INLINE)
d.comment(0xB885, 'Send byte directly to server', align=Align.INLINE)
d.comment(0xB888, 'Update byte count and return', align=Align.INLINE)
d.comment(0xB88B, 'Set V flag (alternate match mode)', align=Align.INLINE)
d.comment(0xB88E, 'Find matching FCB for channel', align=Align.INLINE)
d.comment(0xB891, 'Load byte count for FCB', align=Align.INLINE)
d.comment(0xB894, 'Buffer full (&FF bytes)?', align=Align.INLINE)
d.comment(0xB896, 'No: store byte in buffer', align=Align.INLINE)
d.comment(0xB898, 'Save X', align=Align.INLINE)
d.comment(0xB899, 'Push X', align=Align.INLINE)
d.comment(0xB89A, 'Save Y (FCB slot)', align=Align.INLINE)
d.comment(0xB89B, 'Push Y', align=Align.INLINE)
d.comment(0xB89C, 'Load reply port for FCB', align=Align.INLINE)
d.comment(0xB89F, 'Save reply port', align=Align.INLINE)
d.comment(0xB8A0, 'Y=0: no nested context', align=Align.INLINE)
d.comment(0xB8A2, 'Save context and flush FCB data', align=Align.INLINE)
d.comment(0xB8A5, 'Restore reply port', align=Align.INLINE)
d.comment(0xB8A6, 'Store reply port in TX buffer', align=Align.INLINE)
d.comment(0xB8A9, 'X = reply port', align=Align.INLINE)
d.comment(0xB8AA, 'Restore Y (FCB slot)', align=Align.INLINE)
d.comment(0xB8AB, 'Y restored', align=Align.INLINE)
d.comment(0xB8AC, 'Save Y again for later restore', align=Align.INLINE)
d.comment(0xB8AD, 'A = reply port', align=Align.INLINE)
d.comment(0xB8AE, 'Save reply port for send', align=Align.INLINE)
d.comment(0xB8AF, 'Command byte = 0', align=Align.INLINE)
d.comment(0xB8B1, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB8B4, 'X=&FF: flag byte', align=Align.INLINE)
d.comment(0xB8B5, 'Store &FF in TX buffer', align=Align.INLINE)
d.comment(0xB8B8, 'Load station for FCB', align=Align.INLINE)
d.comment(0xB8BB, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB8BE, 'Load network for FCB', align=Align.INLINE)
d.comment(0xB8C1, 'Store in TX buffer', align=Align.INLINE)
d.comment(0xB8C4, 'Function code &0D', align=Align.INLINE)
d.comment(0xB8C6, 'X=5: copy 5 bytes to TX', align=Align.INLINE)
d.comment(0xB8C8, 'Send flush request to server', align=Align.INLINE)
d.comment(0xB8CB, 'Restore reply port', align=Align.INLINE)
d.comment(0xB8CC, 'Y = reply port', align=Align.INLINE)
d.comment(0xB8CD, 'Load saved data byte', align=Align.INLINE)
d.comment(0xB8D0, 'Send data byte to server', align=Align.INLINE)
d.comment(0xB8D3, 'Restore TX buffer from saved context', align=Align.INLINE)
d.comment(0xB8D6, 'Restore Y (FCB slot)', align=Align.INLINE)
d.comment(0xB8D7, 'Y restored', align=Align.INLINE)
d.comment(0xB8D8, 'Restore X', align=Align.INLINE)
d.comment(0xB8D9, 'X restored', align=Align.INLINE)
d.comment(0xB8DA, 'Reload byte count after flush', align=Align.INLINE)
d.comment(0xB8DD, 'Compare count with buffer offset', align=Align.INLINE)
d.comment(0xB8E0, 'Below offset: skip offset update', align=Align.INLINE)
d.comment(0xB8E2, 'Add carry (count + 1)', align=Align.INLINE)
d.comment(0xB8E4, 'Update buffer offset in FCB', align=Align.INLINE)
d.comment(0xB8E7, 'Non-zero: keep offset flag', align=Align.INLINE)
d.comment(0xB8E9, 'Mask &DF: clear bit 5', align=Align.INLINE)
d.comment(0xB8EB, 'Clear offset flag', align=Align.INLINE)
d.comment(0xB8EE, 'Update FCB status', align=Align.INLINE)
d.comment(0xB8F1, 'Set bit 0 (dirty/active)', align=Align.INLINE)
d.comment(0xB8F3, 'Add to FCB flags', align=Align.INLINE)
d.comment(0xB8F6, 'Update FCB status', align=Align.INLINE)
d.comment(0xB8F9, 'Load byte count (= write position)', align=Align.INLINE)
d.comment(0xB8FC, 'Save count', align=Align.INLINE)
d.comment(0xB8FD, 'Get FCB slot index', align=Align.INLINE)
d.comment(0xB8FE, 'X = FCB slot', align=Align.INLINE)
d.comment(0xB8FF, 'Restore byte count', align=Align.INLINE)
d.comment(0xB900, 'Y = buffer write offset', align=Align.INLINE)
d.comment(0xB901, 'Load current FCB index', align=Align.INLINE)
d.comment(0xB904, 'Prepare addition', align=Align.INLINE)
d.comment(0xB905, 'Add &11 for buffer page offset', align=Align.INLINE)
d.comment(0xB907, 'Set pointer high byte', align=Align.INLINE)
d.comment(0xB909, 'A=0: pointer low byte', align=Align.INLINE)
d.comment(0xB90B, 'Set pointer low byte', align=Align.INLINE)
d.comment(0xB90D, 'Restore data byte', align=Align.INLINE)
d.comment(0xB90E, 'Write data byte to buffer', align=Align.INLINE)
d.comment(0xB910, 'Increment byte count for this FCB', align=Align.INLINE)
d.comment(0xB913, 'A=0: clear receive attribute', align=Align.INLINE)
d.comment(0xB915, 'Offset &0E', align=Align.INLINE)
d.comment(0xB917, 'Clear attribute in receive buffer', align=Align.INLINE)
d.comment(0xB919, "Restore caller's X", align=Align.INLINE)
d.comment(0xB91A, 'X restored', align=Align.INLINE)
d.comment(0xB91B, 'Discard saved data byte', align=Align.INLINE)
d.comment(0xB91C, 'Restore channel attribute', align=Align.INLINE)
d.comment(0xB91F, 'Return', align=Align.INLINE)
d.comment(0xB920, 'Store reply port', align=Align.INLINE)
d.comment(0xB923, 'Store data byte', align=Align.INLINE)
d.comment(0xB926, 'Save Y', align=Align.INLINE)
d.comment(0xB927, 'Push Y to stack', align=Align.INLINE)
d.comment(0xB928, 'Save X', align=Align.INLINE)
d.comment(0xB929, 'Push X to stack', align=Align.INLINE)
d.comment(0xB92A, 'Function code &90', align=Align.INLINE)
d.comment(0xB92C, 'Store in send buffer', align=Align.INLINE)
d.comment(0xB92F, 'Initialise TX control block', align=Align.INLINE)
d.comment(0xB932, 'TX start address low = &DC', align=Align.INLINE)
d.comment(0xB934, 'Set TX start in control block', align=Align.INLINE)
d.comment(0xB936, 'TX end address low = &E0', align=Align.INLINE)
d.comment(0xB938, 'Set TX end in control block', align=Align.INLINE)
d.comment(0xB93A, 'Expected reply port = 9', align=Align.INLINE)
d.comment(0xB93C, 'Store reply port in buffer', align=Align.INLINE)
d.comment(0xB93F, 'TX control = &C0', align=Align.INLINE)
d.comment(0xB941, 'Y=0: no timeout', align=Align.INLINE)
d.comment(0xB943, 'Load reply port for addressing', align=Align.INLINE)
d.comment(0xB946, 'Send packet to server', align=Align.INLINE)
d.comment(0xB949, 'Load reply status', align=Align.INLINE)
d.comment(0xB94C, 'Zero: success', align=Align.INLINE)
d.comment(0xB94E, 'Store error code', align=Align.INLINE)
d.comment(0xB951, 'X=0: copy index', align=Align.INLINE)
d.comment(0xB953, 'Load error message byte', align=Align.INLINE)
d.comment(0xB956, 'Copy to error block', align=Align.INLINE)
d.comment(0xB959, 'Is it CR (end of message)?', align=Align.INLINE)
d.comment(0xB95B, 'Yes: terminate string', align=Align.INLINE)
d.comment(0xB95D, 'Next byte', align=Align.INLINE)
d.comment(0xB95E, 'Continue copying error message', align=Align.INLINE)
d.comment(0xB960, 'NUL terminator', align=Align.INLINE)
d.comment(0xB962, 'Terminate error string in block', align=Align.INLINE)
d.comment(0xB965, 'Back up position for error check', align=Align.INLINE)
d.comment(0xB966, 'Process and raise network error', align=Align.INLINE)
d.comment(0xB969, 'Load channel attribute index', align=Align.INLINE)
d.comment(0xB96C, 'Load station number for channel', align=Align.INLINE)
d.comment(0xB96F, 'Toggle bit 0 (alternate station)', align=Align.INLINE)
d.comment(0xB971, 'Update station number', align=Align.INLINE)
d.comment(0xB974, 'Restore X', align=Align.INLINE)
d.comment(0xB975, 'X restored', align=Align.INLINE)
d.comment(0xB976, 'Restore Y', align=Align.INLINE)
d.comment(0xB977, 'Y restored', align=Align.INLINE)
d.comment(0xB978, 'Return', align=Align.INLINE)
d.comment(0xB979, 'Set up FS options pointer', align=Align.INLINE)
d.comment(0xB97C, 'Set up transfer workspace and return', align=Align.INLINE)
d.comment(0x96C0, 'Store return address low', align=Align.INLINE)
d.comment(0x96C3, 'Store return address high', align=Align.INLINE)
d.comment(0x96C5, 'X=0: error text index', align=Align.INLINE)
d.comment(0x96CA, 'Copy error number to A', align=Align.INLINE)
d.comment(0x96CB, 'Push error number on stack', align=Align.INLINE)
d.comment(0x96CC, 'Y=0: inline string index', align=Align.INLINE)
d.comment(0x96D2, 'Advance string index', align=Align.INLINE)
d.comment(0x96D5, 'Store byte in error block', align=Align.INLINE)
d.comment(0x96DA, 'Y=&0E: offset to error code in RX buffer', align=Align.INLINE)
d.comment(0x96DC, 'Load network error code from reply', align=Align.INLINE)
d.comment(0x96DE, 'Non-zero: network returned an error', align=Align.INLINE)
d.comment(0x96E0, 'Pop saved error number', align=Align.INLINE)
d.comment(0x96E1, 'Was it &DE (file server error)?', align=Align.INLINE)
d.comment(0x96E3, 'Yes: append error number and trigger BRK', align=Align.INLINE)
d.comment(0x96E5, 'Jump to BRK via error block', align=Align.INLINE)
d.comment(0x96E8, 'Store error code in workspace', align=Align.INLINE)
d.comment(0x96EB, 'Push error code', align=Align.INLINE)
d.comment(0x96EC, 'Save X (error text index)', align=Align.INLINE)
d.comment(0x96ED, 'Push X', align=Align.INLINE)
d.comment(0x96EE, 'Y=&0E: error code offset', align=Align.INLINE)
d.comment(0x96F0, 'Load error code from RX buffer', align=Align.INLINE)
d.comment(0x96F2, 'Save to fs_load_addr as spool handle', align=Align.INLINE)
d.comment(0x96F4, 'A=0: clear error code in RX buffer', align=Align.INLINE)
d.comment(0x96F6, 'Zero the error code byte in buffer', align=Align.INLINE)
d.comment(0x96F8, 'A=&C6: OSBYTE read spool handle', align=Align.INLINE)
d.comment(0x96FA, 'Read current spool file handle', align=Align.INLINE)
d.comment(0x96FD, 'Compare Y result with saved handle', align=Align.INLINE)
d.comment(0x96FF, 'Match: close the spool file', align=Align.INLINE)
d.comment(0x9701, 'Compare X result with saved handle', align=Align.INLINE)
d.comment(0x9703, 'No match: skip spool close', align=Align.INLINE)
d.comment(0x9705, 'Push A (preserved)', align=Align.INLINE)
d.comment(0x9706, 'A=&C6: disable spool with OSBYTE', align=Align.INLINE)
d.comment(0x9708, 'ALWAYS branch to close spool', align=Align.INLINE)
d.comment(0x970A, 'Push A (preserved)', align=Align.INLINE)
d.comment(0x970B, 'A=&C7: disable exec with OSBYTE', align=Align.INLINE)
d.comment(0x970D, 'OSBYTE with X=0, Y=0 to close', align=Align.INLINE)
d.comment(0x9710, 'Pull saved handle', align=Align.INLINE)
d.comment(0x9711, 'Transfer to Y for OSFIND', align=Align.INLINE)
d.comment(0x9712, 'A=0: close file', align=Align.INLINE)
d.comment(0x9714, 'Close the spool/exec file', align=Align.INLINE)
d.comment(0x9717, 'Pull saved X (error text index)', align=Align.INLINE)
d.comment(0x9718, 'Restore X', align=Align.INLINE)
d.comment(0x9719, "Y=&0A: lookup index for 'on channel'", align=Align.INLINE)
d.comment(0x971B, 'Load message offset from lookup table', align=Align.INLINE)
d.comment(0x971E, 'Transfer offset to Y', align=Align.INLINE)
d.comment(0x971F, 'Load error message byte', align=Align.INLINE)
d.comment(0x9722, 'Append to error text buffer', align=Align.INLINE)
d.comment(0x9725, 'Null terminator: done copying', align=Align.INLINE)
d.comment(0x9727, 'Advance error text index', align=Align.INLINE)
d.comment(0x9728, 'Advance message index', align=Align.INLINE)
d.comment(0x9729, 'Loop until full message copied', align=Align.INLINE)
d.comment(0x972B, 'Save error text end position', align=Align.INLINE)
d.comment(0x972D, 'Pull saved error number', align=Align.INLINE)
d.comment(0x972E, "Append ' nnn' error number suffix", align=Align.INLINE)
d.comment(0x9731, 'A=0: null terminator', align=Align.INLINE)
d.comment(0x9733, 'Terminate error text string', align=Align.INLINE)
d.comment(0x9736, 'ALWAYS branch to trigger BRK error', align=Align.INLINE)
d.comment(0x9738, "A=' ': space separator", align=Align.INLINE)
d.comment(0x973A, 'Append space to error text', align=Align.INLINE)
d.comment(0x973D, 'Advance error text index', align=Align.INLINE)
d.comment(0x973E, 'Save position for number formatting', align=Align.INLINE)
d.comment(0x9740, 'Y=3: offset to network number in TX CB', align=Align.INLINE)
d.comment(0x9742, 'Load network number', align=Align.INLINE)
d.comment(0x9744, 'Zero: skip network part (local)', align=Align.INLINE)
d.comment(0x9746, 'Append network number as decimal', align=Align.INLINE)
d.comment(0x9749, 'Reload error text position', align=Align.INLINE)
d.comment(0x974B, "A='.': dot separator", align=Align.INLINE)
d.comment(0x974D, 'Append dot to error text', align=Align.INLINE)
d.comment(0x9750, 'Advance past dot', align=Align.INLINE)
d.comment(0x9752, 'Y=2: offset to station number in TX CB', align=Align.INLINE)
d.comment(0x9754, 'Load station number', align=Align.INLINE)
d.comment(0x9756, 'Append station number as decimal', align=Align.INLINE)
d.comment(0x9759, 'Reload error text position', align=Align.INLINE)
d.comment(0x975B, 'Return', align=Align.INLINE)
d.comment(0x975C, 'Save number in Y', align=Align.INLINE)
d.comment(0x975D, "A=' ': space prefix", align=Align.INLINE)
d.comment(0x975F, 'Load current error text position', align=Align.INLINE)
d.comment(0x9761, 'Append space to error text', align=Align.INLINE)
d.comment(0x9764, 'Advance position past space', align=Align.INLINE)
d.comment(0x9766, 'Restore number to A', align=Align.INLINE)
d.comment(0x9767, 'Save number in Y for division', align=Align.INLINE)
d.comment(0x9768, 'Set V: suppress leading zeros', align=Align.INLINE)
d.comment(0x976B, 'A=100: hundreds digit divisor', align=Align.INLINE)
d.comment(0x976D, 'Extract and append hundreds digit', align=Align.INLINE)
d.comment(0x9770, 'A=10: tens digit divisor', align=Align.INLINE)
d.comment(0x9772, 'Extract and append tens digit', align=Align.INLINE)
d.comment(0x9775, 'A=1: units digit (remainder)', align=Align.INLINE)
d.comment(0x9777, 'Clear V: always print units digit', align=Align.INLINE)
d.comment(0x9778, 'Store divisor', align=Align.INLINE)
d.comment(0x977A, 'Copy number to A for division', align=Align.INLINE)
d.comment(0x977B, "X='0'-1: digit counter (ASCII offset)", align=Align.INLINE)
d.comment(0x977D, 'Save V flag (leading zero suppression)', align=Align.INLINE)
d.comment(0x977E, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x977F, 'Increment digit counter', align=Align.INLINE)
d.comment(0x9780, 'Subtract divisor', align=Align.INLINE)
d.comment(0x9782, 'Not negative yet: continue counting', align=Align.INLINE)
d.comment(0x9784, 'Add back divisor (restore remainder)', align=Align.INLINE)
d.comment(0x9786, 'Restore V flag', align=Align.INLINE)
d.comment(0x9787, 'Save remainder back to Y', align=Align.INLINE)
d.comment(0x9788, 'Digit counter to A (ASCII digit)', align=Align.INLINE)
d.comment(0x9789, "Is digit '0'?", align=Align.INLINE)
d.comment(0x978B, 'Non-zero: always print', align=Align.INLINE)
d.comment(0x978D, 'V set (suppress leading zeros): skip', align=Align.INLINE)
d.comment(0x978F, 'Clear V: first non-zero digit seen', align=Align.INLINE)
d.comment(0x9790, 'Load current text position', align=Align.INLINE)
d.comment(0x9792, 'Store ASCII digit in error text', align=Align.INLINE)
d.comment(0x9795, 'Advance text position', align=Align.INLINE)
d.comment(0x9797, 'Return', align=Align.INLINE)
d.comment(0x9798, """Network error lookup table (12 bytes)

Each byte is an offset into error_msg_table.
Indices 0-7 are keyed by error class (reply AND 7).
Index 8 is used by build_no_reply_error.
Indices 9-11 point to suffix strings appended
after the station address in compound errors.""")
d.comment(0x9798, 'Class 0: &A0 "Line jammed"', align=Align.INLINE)
d.comment(0x9799, 'Class 1: &A1 "Net error"', align=Align.INLINE)
d.comment(0x979A, 'Class 2: &A2 "Station"', align=Align.INLINE)
d.comment(0x979B, 'Class 3: &A3 "No clock"', align=Align.INLINE)
d.comment(0x979C, 'Class 4: &11 "Escape"', align=Align.INLINE)
d.comment(0x979D, 'Class 5: &11 "Escape" (duplicate)', align=Align.INLINE)
d.comment(0x979E, 'Class 6: &11 "Escape" (duplicate)', align=Align.INLINE)
d.comment(0x979F, 'Class 7: &CB "Bad option"', align=Align.INLINE)
d.comment(0x97A0, 'Index 8: &A5 "No reply from station"', align=Align.INLINE)
d.comment(0x97A1, 'Index 9: " not listening" suffix', align=Align.INLINE)
d.comment(0x97A2, 'Index 10: " on channel" suffix', align=Align.INLINE)
d.comment(0x97A3, 'Index 11: " not present" suffix', align=Align.INLINE)
d.comment(0x97A4, """Network error message table

Each entry is [error_number][string...][null].
The error number is the BRK error code stored in
the error block at &0100. Entries 0-6 are complete
error messages. The last 3 are suffix strings
(no error number) appended to class 2 "Station"
errors to form compound messages like
"Station 1.254 not listening".""")
d.comment(0x97A4, 'Error &A0: Line jammed', align=Align.INLINE)
d.comment(0x97B0, 'Null terminator', align=Align.INLINE)
d.comment(0x97B1, 'Error &A1: Net error', align=Align.INLINE)
d.comment(0x97BB, 'Null terminator', align=Align.INLINE)
d.comment(0x97BC, 'Error &A2: Station', align=Align.INLINE)
d.comment(0x97C4, 'Null terminator', align=Align.INLINE)
d.comment(0x97C5, 'Error &A3: No clock', align=Align.INLINE)
d.comment(0x97CE, 'Null terminator', align=Align.INLINE)
d.comment(0x97CF, 'Error &11: Escape', align=Align.INLINE)
d.comment(0x97D6, 'Null terminator', align=Align.INLINE)
d.comment(0x97D7, 'Error &CB: Bad option', align=Align.INLINE)
d.comment(0x97E2, 'Null terminator', align=Align.INLINE)
d.comment(0x97E3, 'Error &A5: No reply from station', align=Align.INLINE)
d.comment(0x97F9, 'Null terminator', align=Align.INLINE)
d.comment(0x97FA, 'Suffix: " not listening"', align=Align.INLINE)
d.comment(0x9808, 'Null terminator', align=Align.INLINE)
d.comment(0x9809, 'Suffix: " on channel"', align=Align.INLINE)
d.comment(0x9814, 'Null terminator', align=Align.INLINE)
d.comment(0x9815, 'Suffix: " not present"', align=Align.INLINE)
d.comment(0x9821, 'Null terminator', align=Align.INLINE)
d.comment(0x9822, 'X=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9824, 'Set TX pointer low', align=Align.INLINE)
d.comment(0x9826, 'X=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x9828, 'Set TX pointer high (page 0)', align=Align.INLINE)
d.comment(0x982A, 'Load retry count from workspace', align=Align.INLINE)
d.comment(0x982D, 'Non-zero: use configured retry count', align=Align.INLINE)
d.comment(0x982F, 'A=&FF: default retry count (255)', align=Align.INLINE)
d.comment(0x9831, 'Y=&60: timeout value', align=Align.INLINE)
d.comment(0x9833, 'Push retry count', align=Align.INLINE)
d.comment(0x9834, 'A=&60: copy timeout to A', align=Align.INLINE)
d.comment(0x9835, 'Push timeout', align=Align.INLINE)
d.comment(0x9836, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x9838, 'Load first byte of TX control block', align=Align.INLINE)
d.comment(0x983A, 'Restore control byte (overwritten by result code on retry)', align=Align.INLINE)
d.comment(0x983C, 'Push control byte', align=Align.INLINE)
d.comment(0x983D, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x9840, 'ASL: bit 6 (error flag) into N', align=Align.INLINE)
d.comment(0x9841, 'N=0 (bit 6 clear): success', align=Align.INLINE)
d.comment(0x9843, 'ASL: shift away error flag, keep error type', align=Align.INLINE)
d.comment(0x9844, 'Z=1 (no type bits): fatal; Z=0: retryable', align=Align.INLINE)
d.comment(0x9846, 'Check for escape condition', align=Align.INLINE)
d.comment(0x9849, 'Pull control byte', align=Align.INLINE)
d.comment(0x984A, 'Restore to X', align=Align.INLINE)
d.comment(0x984B, 'Pull timeout', align=Align.INLINE)
d.comment(0x984C, 'Restore to Y', align=Align.INLINE)
d.comment(0x984D, 'Pull retry count', align=Align.INLINE)
d.comment(0x984E, 'Zero retries remaining: try alternate', align=Align.INLINE)
d.comment(0x9850, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x9852, 'Push updated retry count', align=Align.INLINE)
d.comment(0x9853, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x9854, 'Push timeout for delay loop', align=Align.INLINE)
d.comment(0x9855, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x9856, 'Inner delay: decrement X', align=Align.INLINE)
d.comment(0x9857, 'Loop until X=0', align=Align.INLINE)
d.comment(0x9859, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x985A, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x985C, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x985E, 'Compare retry count with alternate', align=Align.INLINE)
d.comment(0x9861, 'Different: go to error handling', align=Align.INLINE)
d.comment(0x9863, 'A=&80: set escapable flag', align=Align.INLINE)
d.comment(0x9865, 'Mark as escapable for second phase', align=Align.INLINE)
d.comment(0x9867, 'ALWAYS branch: retry with escapable', align=Align.INLINE)
d.comment(0x9869, 'Result code to X', align=Align.INLINE)
d.comment(0x986A, 'Jump to classify reply and return', align=Align.INLINE)
d.comment(0x986D, 'Pull control byte', align=Align.INLINE)
d.comment(0x986E, 'Pull timeout', align=Align.INLINE)
d.comment(0x986F, 'Pull retry count', align=Align.INLINE)
d.comment(0x9870, 'Clear escapable flag and return', align=Align.INLINE)
d.comment(0x9873, """Pass-through TX buffer template (12 bytes)

Overlaid onto the TX control block by
setup_pass_txbuf for pass-through operations.
Offsets marked &FD are skipped, preserving the
existing destination station and network. Buffer
addresses point to &0D3A-&0D3E in NMI workspace.
Original TX buffer values are pushed on the stack
and restored after transmission.""")
d.comment(0x9873, 'Offset 0: ctrl = &88 (immediate TX)', align=Align.INLINE)
d.comment(0x9874, 'Offset 1: port = &00 (immediate op)', align=Align.INLINE)
d.comment(0x9875, 'Offset 2: &FD skip (preserve dest stn)', align=Align.INLINE)
d.comment(0x9876, 'Offset 3: &FD skip (preserve dest net)', align=Align.INLINE)
d.comment(0x9877, 'Offset 4: buf start lo (&3A)', align=Align.INLINE)
d.comment(0x9878, 'Offset 5: buf start hi (&0D) -> &0D3A', align=Align.INLINE)
d.comment(0x9879, 'Offset 6: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x987A, 'Offset 7: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x987B, 'Offset 8: buf end lo (&3E)', align=Align.INLINE)
d.comment(0x987C, 'Offset 9: buf end hi (&0D) -> &0D3E', align=Align.INLINE)
d.comment(0x987D, 'Offset 10: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x987E, 'Offset 11: extended addr fill (&FF)', align=Align.INLINE)
d.comment(0x987F, 'Y=&C0: TX control block base (low)', align=Align.INLINE)
d.comment(0x9881, 'Set TX pointer low byte', align=Align.INLINE)
d.comment(0x9883, 'Y=0: TX control block base (high)', align=Align.INLINE)
d.comment(0x9885, 'Set TX pointer high byte', align=Align.INLINE)
d.comment(0x9887, 'Y=&0B: 12 bytes to process (0-11)', align=Align.INLINE)
d.comment(0x9889, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x988C, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x988E, "Yes: skip this offset, don't modify", align=Align.INLINE)
d.comment(0x9890, 'Load existing TX buffer byte', align=Align.INLINE)
d.comment(0x9892, 'Save original value on stack', align=Align.INLINE)
d.comment(0x9893, 'Copy template value to A', align=Align.INLINE)
d.comment(0x9894, 'Store template value to TX buffer', align=Align.INLINE)
d.comment(0x9896, 'Next offset (descending)', align=Align.INLINE)
d.comment(0x9897, 'Loop until all 12 bytes processed', align=Align.INLINE)
d.comment(0x9899, 'Load pass-through control value', align=Align.INLINE)
d.comment(0x989C, 'Push control value', align=Align.INLINE)
d.comment(0x989D, 'A=&FF (Y is &FF after loop)', align=Align.INLINE)
d.comment(0x989E, 'Push &FF as timeout', align=Align.INLINE)
d.comment(0x989F, 'X=0: TX pointer index', align=Align.INLINE)
d.comment(0x98A1, 'Load control byte from TX CB', align=Align.INLINE)
d.comment(0x98A3, 'Write control byte to start TX', align=Align.INLINE)
d.comment(0x98A5, 'Save control byte on stack', align=Align.INLINE)
d.comment(0x98A6, 'Poll ADLC until line idle', align=Align.INLINE)
d.comment(0x98A9, 'Shift result: check bit 6 (success)', align=Align.INLINE)
d.comment(0x98AA, 'Bit 6 clear: transmission complete', align=Align.INLINE)
d.comment(0x98AC, 'Shift result: check bit 5 (fatal)', align=Align.INLINE)
d.comment(0x98AD, 'Non-zero (not fatal): retry', align=Align.INLINE)
d.comment(0x98AF, 'X=0: clear error status', align=Align.INLINE)
d.comment(0x98B1, 'Jump to fix up reply status', align=Align.INLINE)
d.comment(0x98B4, 'Shift ws_0d60 left to poll ADLC', align=Align.INLINE)
d.comment(0x98B7, 'Bit not set: keep polling', align=Align.INLINE)
d.comment(0x98B9, 'Copy TX pointer low to NMI TX block', align=Align.INLINE)
d.comment(0x98BB, 'Store in NMI TX block low', align=Align.INLINE)
d.comment(0x98BD, 'Copy TX pointer high', align=Align.INLINE)
d.comment(0x98BF, 'Store in NMI TX block high', align=Align.INLINE)
d.comment(0x98C1, 'Begin Econet frame transmission', align=Align.INLINE)
d.comment(0x98C4, 'Read TX status byte', align=Align.INLINE)
d.comment(0x98C6, 'Bit 7 set: still transmitting', align=Align.INLINE)
d.comment(0x98C8, 'Return with result in A', align=Align.INLINE)
d.comment(0x98C9, 'Pull control byte', align=Align.INLINE)
d.comment(0x98CA, 'Restore to X', align=Align.INLINE)
d.comment(0x98CB, 'Pull timeout', align=Align.INLINE)
d.comment(0x98CC, 'Restore to Y', align=Align.INLINE)
d.comment(0x98CD, 'Pull retry count', align=Align.INLINE)
d.comment(0x98CE, 'Zero retries: go to error handling', align=Align.INLINE)
d.comment(0x98D0, 'Decrement retry counter', align=Align.INLINE)
d.comment(0x98D2, 'Push updated retry count', align=Align.INLINE)
d.comment(0x98D3, 'Copy timeout to A', align=Align.INLINE)
d.comment(0x98D4, 'Push timeout', align=Align.INLINE)
d.comment(0x98D5, 'Copy control byte to A', align=Align.INLINE)
d.comment(0x98D6, 'Inner delay loop: decrement X', align=Align.INLINE)
d.comment(0x98D7, 'Loop until X=0', align=Align.INLINE)
d.comment(0x98D9, 'Decrement outer counter Y', align=Align.INLINE)
d.comment(0x98DA, 'Loop until Y=0', align=Align.INLINE)
d.comment(0x98DC, 'ALWAYS branch: retry transmission', align=Align.INLINE)
d.comment(0x98DE, 'Pull control byte (discard)', align=Align.INLINE)
d.comment(0x98DF, 'Pull timeout (discard)', align=Align.INLINE)
d.comment(0x98E0, 'Pull retry count (discard)', align=Align.INLINE)
d.comment(0x98E1, 'Y=0: start restoring from offset 0', align=Align.INLINE)
d.comment(0x98E3, 'Load template byte for this offset', align=Align.INLINE)
d.comment(0x98E6, 'Is it &FD (skip marker)?', align=Align.INLINE)
d.comment(0x98E8, "Yes: don't restore this offset", align=Align.INLINE)
d.comment(0x98EA, 'Pull original value from stack', align=Align.INLINE)
d.comment(0x98EB, 'Restore original TX buffer byte', align=Align.INLINE)
d.comment(0x98ED, 'Next offset (ascending)', align=Align.INLINE)
d.comment(0x98EE, 'Processed all 12 bytes?', align=Align.INLINE)
d.comment(0x98F0, 'No: continue restoring', align=Align.INLINE)
d.comment(0x98F2, 'Return with TX buffer restored', align=Align.INLINE)
d.comment(0x98F3, 'Y=1: start at second byte of pointer', align=Align.INLINE)
d.comment(0x98F5, 'Load pointer byte from FS options', align=Align.INLINE)
d.comment(0x98F7, 'Store in OS text pointer', align=Align.INLINE)
d.comment(0x98FA, 'Decrement index', align=Align.INLINE)
d.comment(0x98FB, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0x98FD, 'Y=0: reset command line offset', align=Align.INLINE)
d.comment(0x98FF, 'X=&FF: pre-increment for buffer index', align=Align.INLINE)
d.comment(0x9901, 'C=0: initialise for string input', align=Align.INLINE)
d.comment(0x9902, 'GSINIT: initialise string reading', align=Align.INLINE)
d.comment(0x9905, 'Z set (empty string): store terminator', align=Align.INLINE)
d.comment(0x9907, 'GSREAD: read next character', align=Align.INLINE)
d.comment(0x990A, 'C set: end of string reached', align=Align.INLINE)
d.comment(0x990C, 'Advance buffer index', align=Align.INLINE)
d.comment(0x990D, 'Store character in l0e30 buffer', align=Align.INLINE)
d.comment(0x9910, 'ALWAYS branch: read next character', align=Align.INLINE)
d.comment(0x9912, 'Advance past last character', align=Align.INLINE)
d.comment(0x9913, 'A=CR: terminate filename', align=Align.INLINE)
d.comment(0x9915, 'Store CR terminator in buffer', align=Align.INLINE)
d.comment(0x9918, 'A=&30: low byte of l0e30 buffer', align=Align.INLINE)
d.comment(0x991A, 'Set command text pointer low', align=Align.INLINE)
d.comment(0x991C, 'A=&0E: high byte of l0e30 buffer', align=Align.INLINE)
d.comment(0x991E, 'Set command text pointer high', align=Align.INLINE)
d.comment(0x9920, 'Return with buffer filled', align=Align.INLINE)
d.comment(0x9921, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9924, 'Load text pointer and parse filename', align=Align.INLINE)
d.comment(0x9927, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x992A, 'Parse access prefix from filename', align=Align.INLINE)
d.comment(0x992D, 'Load last byte flag', align=Align.INLINE)
d.comment(0x992F, 'Positive (not last): display file info', align=Align.INLINE)
d.comment(0x9931, 'Is it &FF (last entry)?', align=Align.INLINE)
d.comment(0x9933, 'Yes: copy arg and iterate', align=Align.INLINE)
d.comment(0x9935, 'Other value: return with flag', align=Align.INLINE)
d.comment(0x9938, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x993B, 'Y=2: enumerate directory command', align=Align.INLINE)
d.comment(0x993D, 'A=&92: FS port number', align=Align.INLINE)
d.comment(0x993F, 'Set escapable flag to &92', align=Align.INLINE)
d.comment(0x9941, 'Store port number in TX buffer', align=Align.INLINE)
d.comment(0x9944, 'Send request to file server', align=Align.INLINE)
d.comment(0x9947, 'Y=6: offset to response cycle flag', align=Align.INLINE)
d.comment(0x9949, 'Load cycle flag from FS options', align=Align.INLINE)
d.comment(0x994B, 'Non-zero: already initialised', align=Align.INLINE)
d.comment(0x994D, 'Copy FS options to zero page first', align=Align.INLINE)
d.comment(0x9950, 'Then copy workspace to FS options', align=Align.INLINE)
d.comment(0x9953, 'Branch to continue (C clear from JSR)', align=Align.INLINE)
d.comment(0x9955, 'Copy workspace to FS options first', align=Align.INLINE)
d.comment(0x9958, 'Then copy FS options to zero page', align=Align.INLINE)
d.comment(0x995B, 'Y=4: loop counter', align=Align.INLINE)
d.comment(0x995D, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x995F, 'Save to TXCB end pointer', align=Align.INLINE)
d.comment(0x9961, 'Add offset from buffer', align=Align.INLINE)
d.comment(0x9964, 'Store sum in fs_work area', align=Align.INLINE)
d.comment(0x9966, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9967, 'Decrement counter', align=Align.INLINE)
d.comment(0x9968, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x996A, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x996B, 'Subtract high offset', align=Align.INLINE)
d.comment(0x996E, 'Store result in fs_work_7', align=Align.INLINE)
d.comment(0x9970, 'Format filename for display', align=Align.INLINE)
d.comment(0x9973, 'Send TXCB and swap addresses', align=Align.INLINE)
d.comment(0x9976, 'X=2: copy 3 offset bytes', align=Align.INLINE)
d.comment(0x9978, 'Load offset byte from l0f10', align=Align.INLINE)
d.comment(0x997B, 'Store in l0f05 for next iteration', align=Align.INLINE)
d.comment(0x997E, 'Decrement counter', align=Align.INLINE)
d.comment(0x997F, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9981, 'Jump to receive and process reply', align=Align.INLINE)
d.comment(0x9984, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x9987, 'Match: no need to send, return', align=Align.INLINE)
d.comment(0x9989, 'A=&92: FS reply port number', align=Align.INLINE)
d.comment(0x998B, 'Set TXCB port', align=Align.INLINE)
d.comment(0x998D, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x998F, 'Load TXCB end pointer byte', align=Align.INLINE)
d.comment(0x9991, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x9993, 'Load new end address from fs_work', align=Align.INLINE)
d.comment(0x9995, 'Store in TXCB end pointer', align=Align.INLINE)
d.comment(0x9997, 'Decrement counter', align=Align.INLINE)
d.comment(0x9998, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x999A, 'A=&7F: control byte for data transfer', align=Align.INLINE)
d.comment(0x999C, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x999E, 'Wait for network TX acknowledgement', align=Align.INLINE)
d.comment(0x99A1, 'Y=3: compare 4 bytes', align=Align.INLINE)
d.comment(0x99A3, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0x99A6, 'Compare with expected end address', align=Align.INLINE)
d.comment(0x99A9, 'Mismatch: resend from start', align=Align.INLINE)
d.comment(0x99AB, 'Decrement counter', align=Align.INLINE)
d.comment(0x99AC, 'Loop until all 4 bytes match', align=Align.INLINE)
d.comment(0x99AE, 'Return (all bytes match)', align=Align.INLINE)
d.comment(0x99AF, 'Z set: directory entry display', align=Align.INLINE)
d.comment(0x99B1, 'Non-zero: jump to OSWORD dispatch', align=Align.INLINE)
d.comment(0x99B4, 'X=4: loop counter for 4 iterations', align=Align.INLINE)
d.comment(0x99B6, 'Y=&0E: FS options offset for addresses', align=Align.INLINE)
d.comment(0x99B8, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x99B9, 'Load address byte from FS options', align=Align.INLINE)
d.comment(0x99BB, 'Save to workspace (port_ws_offset)', align=Align.INLINE)
d.comment(0x99BE, 'Y -= 4 to point to paired offset', align=Align.INLINE)
d.comment(0x99C1, 'Subtract paired value', align=Align.INLINE)
d.comment(0x99C3, 'Store difference in l0f03 buffer', align=Align.INLINE)
d.comment(0x99C6, 'Push difference', align=Align.INLINE)
d.comment(0x99C7, 'Load paired value from FS options', align=Align.INLINE)
d.comment(0x99C9, 'Save to workspace', align=Align.INLINE)
d.comment(0x99CC, 'Pull difference back', align=Align.INLINE)
d.comment(0x99CD, 'Store in FS options for display', align=Align.INLINE)
d.comment(0x99CF, 'Advance Y by 5 for next field', align=Align.INLINE)
d.comment(0x99D2, 'Decrement loop counter', align=Align.INLINE)
d.comment(0x99D3, 'Loop for all 4 address pairs', align=Align.INLINE)
d.comment(0x99D5, 'Y=9: copy 9 bytes of options data', align=Align.INLINE)
d.comment(0x99D7, 'Load FS options byte', align=Align.INLINE)
d.comment(0x99D9, 'Store in l0f03 buffer', align=Align.INLINE)
d.comment(0x99DC, 'Decrement index', align=Align.INLINE)
d.comment(0x99DD, 'Loop until all 9 bytes copied', align=Align.INLINE)
d.comment(0x99DF, 'A=&91: FS port for info request', align=Align.INLINE)
d.comment(0x99E1, 'Set escapable flag', align=Align.INLINE)
d.comment(0x99E3, 'Store port in TX buffer', align=Align.INLINE)
d.comment(0x99E6, 'Store in fs_error_ptr', align=Align.INLINE)
d.comment(0x99E8, 'X=&0B: copy argument at offset 11', align=Align.INLINE)
d.comment(0x99EA, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x99ED, 'Y=1: info sub-command', align=Align.INLINE)
d.comment(0x99EF, 'Load last byte flag', align=Align.INLINE)
d.comment(0x99F1, 'Is it 7 (catalogue info)?', align=Align.INLINE)
d.comment(0x99F3, 'Save comparison result', align=Align.INLINE)
d.comment(0x99F4, 'Not 7: keep Y=1', align=Align.INLINE)
d.comment(0x99F6, 'Y=&1D: extended info command', align=Align.INLINE)
d.comment(0x99F8, 'Send request to file server', align=Align.INLINE)
d.comment(0x99FB, 'Format filename for display', align=Align.INLINE)
d.comment(0x99FE, 'Restore comparison flags', align=Align.INLINE)
d.comment(0x99FF, 'Not catalogue info: show short format', align=Align.INLINE)
d.comment(0x9A01, 'X=0: start at first byte', align=Align.INLINE)
d.comment(0x9A03, 'ALWAYS branch to store and display', align=Align.INLINE)
d.comment(0x9A05, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9A08, 'Check and set up TXCB for transfer', align=Align.INLINE)
d.comment(0x9A0B, 'Receive and process reply', align=Align.INLINE)
d.comment(0x9A0E, 'Store result byte in l0f08', align=Align.INLINE)
d.comment(0x9A11, 'Y=&0E: protection bits offset', align=Align.INLINE)
d.comment(0x9A13, 'Load access byte from l0f05', align=Align.INLINE)
d.comment(0x9A16, 'Extract protection bit flags', align=Align.INLINE)
d.comment(0x9A19, 'Zero: use reply buffer data', align=Align.INLINE)
d.comment(0x9A1B, 'Load file info byte from l0ef7', align=Align.INLINE)
d.comment(0x9A1E, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9A20, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9A21, 'Y=&12: end of protection fields?', align=Align.INLINE)
d.comment(0x9A23, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A25, 'Load display flag from l0e06', align=Align.INLINE)
d.comment(0x9A28, 'Zero: skip display, return', align=Align.INLINE)
d.comment(0x9A2A, 'Y=0: filename character index', align=Align.INLINE)
d.comment(0x9A2C, 'Load filename character from l10f3', align=Align.INLINE)
d.comment(0x9A2F, 'Print character via OSASCI', align=Align.INLINE)
d.comment(0x9A32, 'Advance to next character', align=Align.INLINE)
d.comment(0x9A33, 'Printed all 12 characters?', align=Align.INLINE)
d.comment(0x9A35, 'No: print next character', align=Align.INLINE)
d.comment(0x9A37, 'Y=5: offset for access string', align=Align.INLINE)
d.comment(0x9A39, 'Print 5 hex bytes (access info)', align=Align.INLINE)
d.comment(0x9A3C, 'Print load and exec addresses', align=Align.INLINE)
d.comment(0x9A3F, 'Print newline', align=Align.INLINE)
d.comment(0x9A42, 'Jump to return with last flag', align=Align.INLINE)
d.comment(0x9A45, 'Y=9: offset for exec address', align=Align.INLINE)
d.comment(0x9A47, 'Print 5 hex bytes (exec address)', align=Align.INLINE)
d.comment(0x9A4A, 'Y=&0C: offset for length (3 bytes)', align=Align.INLINE)
d.comment(0x9A4C, 'X=3: print 3 bytes only', align=Align.INLINE)
d.comment(0x9A4E, 'ALWAYS branch to print routine', align=Align.INLINE)
d.comment(0x9A50, 'X=4: print 5 bytes (4 to 0)', align=Align.INLINE)
d.comment(0x9A52, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9A54, 'Print as 2-digit hex', align=Align.INLINE)
d.comment(0x9A57, 'Decrement byte offset', align=Align.INLINE)
d.comment(0x9A58, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9A59, 'Loop until all bytes printed', align=Align.INLINE)
d.comment(0x9A5B, "A=' ': space separator", align=Align.INLINE)
d.comment(0x9A5D, 'Print space via OSASCI and return', align=Align.INLINE)
d.comment(0x9A60, 'Y=5: copy 4 bytes (offsets 2-5)', align=Align.INLINE)
d.comment(0x9A62, 'Load byte from FS options', align=Align.INLINE)
d.comment(0x9A64, 'Store in zero page at l00ae+Y', align=Align.INLINE)
d.comment(0x9A67, 'Decrement index', align=Align.INLINE)
d.comment(0x9A68, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9A6A, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A6C, 'Y += 5', align=Align.INLINE)
d.comment(0x9A6D, 'Y += 4', align=Align.INLINE)
d.comment(0x9A6E, '(continued)', align=Align.INLINE)
d.comment(0x9A6F, '(continued)', align=Align.INLINE)
d.comment(0x9A70, '(continued)', align=Align.INLINE)
d.comment(0x9A71, 'Return', align=Align.INLINE)
d.comment(0x9A72, 'Y=&0D: copy bytes from offset &0D down', align=Align.INLINE)
d.comment(0x9A74, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9A75, 'Store byte in FS options at offset Y', align=Align.INLINE)
d.comment(0x9A77, 'Load next workspace byte from l0f02+Y', align=Align.INLINE)
d.comment(0x9A7A, 'Decrement index', align=Align.INLINE)
d.comment(0x9A7B, 'Below offset 2?', align=Align.INLINE)
d.comment(0x9A7D, 'No: copy next byte', align=Align.INLINE)
d.comment(0x9A7F, 'Y -= 4', align=Align.INLINE)
d.comment(0x9A80, 'Y -= 3', align=Align.INLINE)
d.comment(0x9A81, '(continued)', align=Align.INLINE)
d.comment(0x9A82, '(continued)', align=Align.INLINE)
d.comment(0x9A83, 'Return', align=Align.INLINE)
d.comment(0x9A84, 'Discard stacked value', align=Align.INLINE)
d.comment(0x9A85, 'Restore Y from fs_block_offset', align=Align.INLINE)
d.comment(0x9A87, 'Return (handle already matches)', align=Align.INLINE)
d.comment(0x9A88, 'Save port/sub-function on stack', align=Align.INLINE)
d.comment(0x9A89, 'Compare 5-byte handle with current', align=Align.INLINE)
d.comment(0x9A8C, 'Match: discard port and return', align=Align.INLINE)
d.comment(0x9A8E, 'X=0: loop start', align=Align.INLINE)
d.comment(0x9A90, 'Y=4: copy 4 bytes', align=Align.INLINE)
d.comment(0x9A92, 'Clear l0f08 (transfer size low)', align=Align.INLINE)
d.comment(0x9A95, 'Clear l0f09 (transfer size high)', align=Align.INLINE)
d.comment(0x9A98, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9A99, 'Load address byte from zero page', align=Align.INLINE)
d.comment(0x9A9B, 'Store in TXCB start pointer', align=Align.INLINE)
d.comment(0x9A9D, 'Add offset from l0f06', align=Align.INLINE)
d.comment(0x9AA0, 'Store sum in TXCB end pointer', align=Align.INLINE)
d.comment(0x9AA2, 'Also update load address', align=Align.INLINE)
d.comment(0x9AA4, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9AA5, 'Decrement counter', align=Align.INLINE)
d.comment(0x9AA6, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9AA8, 'Carry set: overflow, use limit', align=Align.INLINE)
d.comment(0x9AAA, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9AAB, 'Load computed end address', align=Align.INLINE)
d.comment(0x9AAE, 'Subtract maximum from fs_work_4', align=Align.INLINE)
d.comment(0x9AB1, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9AB2, 'Decrement counter', align=Align.INLINE)
d.comment(0x9AB3, 'Loop for all bytes', align=Align.INLINE)
d.comment(0x9AB5, 'Below limit: keep computed end', align=Align.INLINE)
d.comment(0x9AB7, 'X=3: copy 4 bytes of limit', align=Align.INLINE)
d.comment(0x9AB9, 'Load limit from fs_work_4', align=Align.INLINE)
d.comment(0x9ABB, 'Store as TXCB end', align=Align.INLINE)
d.comment(0x9ABD, 'Decrement counter', align=Align.INLINE)
d.comment(0x9ABE, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9AC0, 'Pull port from stack', align=Align.INLINE)
d.comment(0x9AC1, 'Push back (keep for later)', align=Align.INLINE)
d.comment(0x9AC2, 'Save flags (carry = overflow state)', align=Align.INLINE)
d.comment(0x9AC3, 'Set TXCB port number', align=Align.INLINE)
d.comment(0x9AC5, 'A=&80: control byte for data request', align=Align.INLINE)
d.comment(0x9AC7, 'Set TXCB control byte', align=Align.INLINE)
d.comment(0x9AC9, 'Init TX pointer and send packet', align=Align.INLINE)
d.comment(0x9ACC, 'Load error pointer', align=Align.INLINE)
d.comment(0x9ACE, 'Init TXCB port from error pointer', align=Align.INLINE)
d.comment(0x9AD1, 'Restore overflow flags', align=Align.INLINE)
d.comment(0x9AD2, 'Carry set: discard and return', align=Align.INLINE)
d.comment(0x9AD4, 'A=&91: FS reply port', align=Align.INLINE)
d.comment(0x9AD6, 'Set TXCB port for reply', align=Align.INLINE)
d.comment(0x9AD8, 'Wait for TX acknowledgement', align=Align.INLINE)
d.comment(0x9ADB, 'Non-zero (not done): retry send', align=Align.INLINE)
d.comment(0x9ADD, 'Store sub-operation code', align=Align.INLINE)
d.comment(0x9AE0, 'Compare with 7', align=Align.INLINE)
d.comment(0x9AE2, 'Below 7: handle operations 1-6', align=Align.INLINE)
d.comment(0x9AE4, 'Above 7: jump to handle via finalise', align=Align.INLINE)
d.comment(0x9AE6, 'Equal to 7: jump to directory display', align=Align.INLINE)
d.comment(0x9AE9, 'Compare with 6', align=Align.INLINE)
d.comment(0x9AEB, '6: delete file operation', align=Align.INLINE)
d.comment(0x9AED, 'Compare with 5', align=Align.INLINE)
d.comment(0x9AEF, '5: read catalogue info', align=Align.INLINE)
d.comment(0x9AF1, 'Compare with 4', align=Align.INLINE)
d.comment(0x9AF3, '4: write file attributes', align=Align.INLINE)
d.comment(0x9AF5, 'Compare with 1', align=Align.INLINE)
d.comment(0x9AF7, '1: read file info', align=Align.INLINE)
d.comment(0x9AF9, 'Shift left twice: A*4', align=Align.INLINE)
d.comment(0x9AFA, 'A*4', align=Align.INLINE)
d.comment(0x9AFB, 'Copy to Y as index', align=Align.INLINE)
d.comment(0x9AFC, 'Y -= 3 to get FS options offset', align=Align.INLINE)
d.comment(0x9AFF, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9B01, 'Load byte from FS options at offset Y', align=Align.INLINE)
d.comment(0x9B03, 'Store in l0f06 buffer', align=Align.INLINE)
d.comment(0x9B06, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9B07, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9B08, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9B0A, 'X=5: copy arg to buffer at offset 5', align=Align.INLINE)
d.comment(0x9B0C, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9B0E, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9B11, 'Store access byte in l0f0e', align=Align.INLINE)
d.comment(0x9B14, 'Y=9: source offset in FS options', align=Align.INLINE)
d.comment(0x9B16, 'X=8: copy 8 bytes to buffer', align=Align.INLINE)
d.comment(0x9B18, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9B1A, 'Store in l0f05 buffer', align=Align.INLINE)
d.comment(0x9B1D, 'Decrement source offset', align=Align.INLINE)
d.comment(0x9B1E, 'Decrement byte count', align=Align.INLINE)
d.comment(0x9B1F, 'Loop for all 8 bytes', align=Align.INLINE)
d.comment(0x9B21, 'X=&0A: buffer offset for argument', align=Align.INLINE)
d.comment(0x9B23, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9B26, 'Y=&13: OSWORD &13 (NFS operation)', align=Align.INLINE)
d.comment(0x9B28, 'ALWAYS branch to send request', align=Align.INLINE)
d.comment(0x9B2A, 'Copy argument to buffer at X=0', align=Align.INLINE)
d.comment(0x9B2D, 'Y=&14: delete file command', align=Align.INLINE)
d.comment(0x9B2F, 'Set V flag (no directory check)', align=Align.INLINE)
d.comment(0x9B32, 'Send request with V set', align=Align.INLINE)
d.comment(0x9B35, 'Carry set: error, jump to finalise', align=Align.INLINE)
d.comment(0x9B37, 'No error: return with last flag', align=Align.INLINE)
d.comment(0x9B3A, 'Get access bits for file', align=Align.INLINE)
d.comment(0x9B3D, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9B40, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9B42, 'ALWAYS branch to copy and send', align=Align.INLINE)
d.comment(0x9B44, 'X=1: buffer offset', align=Align.INLINE)
d.comment(0x9B46, 'Copy argument to buffer', align=Align.INLINE)
d.comment(0x9B49, 'Y=&12: open file command', align=Align.INLINE)
d.comment(0x9B4B, 'Send open file request', align=Align.INLINE)
d.comment(0x9B4E, 'Load reply handle from l0f11', align=Align.INLINE)
d.comment(0x9B51, 'Clear l0f11', align=Align.INLINE)
d.comment(0x9B54, 'Clear l0f14', align=Align.INLINE)
d.comment(0x9B57, 'Get protection bits', align=Align.INLINE)
d.comment(0x9B5A, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9B5D, 'Zero: file not found, return', align=Align.INLINE)
d.comment(0x9B5F, 'Y=&0E: store access bits', align=Align.INLINE)
d.comment(0x9B61, 'Store access byte in FS options', align=Align.INLINE)
d.comment(0x9B63, 'Y=&0D', align=Align.INLINE)
d.comment(0x9B64, 'X=&0C: copy 12 bytes of file info', align=Align.INLINE)
d.comment(0x9B66, 'Load reply byte from l0f05+X', align=Align.INLINE)
d.comment(0x9B69, 'Store in FS options at offset Y', align=Align.INLINE)
d.comment(0x9B6B, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9B6C, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9B6D, 'Loop for all 12 bytes', align=Align.INLINE)
d.comment(0x9B6F, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0x9B70, 'X=2', align=Align.INLINE)
d.comment(0x9B71, 'Y=&11: FS options offset', align=Align.INLINE)
d.comment(0x9B73, 'Load extended info byte from l0f12', align=Align.INLINE)
d.comment(0x9B76, 'Store in FS options', align=Align.INLINE)
d.comment(0x9B78, 'Decrement destination offset', align=Align.INLINE)
d.comment(0x9B79, 'Decrement source counter', align=Align.INLINE)
d.comment(0x9B7A, 'Loop until all copied', align=Align.INLINE)
d.comment(0x9B7C, 'Reload file handle', align=Align.INLINE)
d.comment(0x9B7F, 'Transfer to A', align=Align.INLINE)
d.comment(0x9B80, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9B83, """Unreachable dead code (3 bytes)

Duplicate of the JMP at &9B80 immediately above.
Unreachable after the unconditional JMP and
unreferenced. Likely a development remnant.""")
d.comment(0x9B83, 'Dead: duplicate JMP finalise_and_return', align=Align.INLINE)
d.comment(0x9B86, 'Y=0: destination index', align=Align.INLINE)
d.comment(0x9B88, 'Load source offset from l0f03', align=Align.INLINE)
d.comment(0x9B8B, 'Non-zero: copy from l0f05 buffer', align=Align.INLINE)
d.comment(0x9B8D, 'Load character from command line', align=Align.INLINE)
d.comment(0x9B8F, "Below '!' (control/space)?", align=Align.INLINE)
d.comment(0x9B91, 'Yes: pad with spaces', align=Align.INLINE)
d.comment(0x9B93, 'Store printable character in l10f3', align=Align.INLINE)
d.comment(0x9B96, 'Advance to next character', align=Align.INLINE)
d.comment(0x9B97, 'Loop for more characters', align=Align.INLINE)
d.comment(0x9B99, "A=' ': space for padding", align=Align.INLINE)
d.comment(0x9B9B, 'Store space in display buffer', align=Align.INLINE)
d.comment(0x9B9E, 'Advance index', align=Align.INLINE)
d.comment(0x9B9F, 'Filled all 12 characters?', align=Align.INLINE)
d.comment(0x9BA1, 'No: pad more spaces', align=Align.INLINE)
d.comment(0x9BA3, 'Return with field formatted', align=Align.INLINE)
d.comment(0x9BA4, 'Advance source and destination', align=Align.INLINE)
d.comment(0x9BA5, 'INY', align=Align.INLINE)
d.comment(0x9BA6, 'Load byte from l0f05 buffer', align=Align.INLINE)
d.comment(0x9BA9, 'Store in display buffer l10f3', align=Align.INLINE)
d.comment(0x9BAC, 'Bit 7 clear: more characters', align=Align.INLINE)
d.comment(0x9BAE, 'Return (bit 7 set = terminator)', align=Align.INLINE)
d.comment(0x9BAF, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9BB2, 'Store result as last byte flag', align=Align.INLINE)
d.comment(0x9BB4, 'Set FS options pointer', align=Align.INLINE)
d.comment(0x9BB7, 'OR with 0 to set flags', align=Align.INLINE)
d.comment(0x9BB9, 'Positive: handle sub-operations', align=Align.INLINE)
d.comment(0x9BBB, 'Shift left to check bit 6', align=Align.INLINE)
d.comment(0x9BBC, 'Zero (was &80): close channel', align=Align.INLINE)
d.comment(0x9BBE, 'Other: process all FCBs first', align=Align.INLINE)
d.comment(0x9BC1, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9BC2, 'Compare with &20 (space)', align=Align.INLINE)
d.comment(0x9BC4, 'Above &20: check further', align=Align.INLINE)
d.comment(0x9BC6, 'Below &20: invalid channel char', align=Align.INLINE)
d.comment(0x9BC9, "Compare with '0'", align=Align.INLINE)
d.comment(0x9BCB, "Above '0': invalid channel char", align=Align.INLINE)
d.comment(0x9BCD, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9BD0, 'Transfer Y to A (FCB index)', align=Align.INLINE)
d.comment(0x9BD1, 'Push FCB index', align=Align.INLINE)
d.comment(0x9BD2, 'Copy to X', align=Align.INLINE)
d.comment(0x9BD3, 'Y=0: clear counter', align=Align.INLINE)
d.comment(0x9BD5, 'Clear last byte flag', align=Align.INLINE)
d.comment(0x9BD7, 'Clear block offset', align=Align.INLINE)
d.comment(0x9BD9, 'Load channel data from l1010+X', align=Align.INLINE)
d.comment(0x9BDC, 'Store in FS options at Y', align=Align.INLINE)
d.comment(0x9BDE, 'Advance X by 8 (next FCB field)', align=Align.INLINE)
d.comment(0x9BE1, 'Advance destination index', align=Align.INLINE)
d.comment(0x9BE2, 'Copied all 4 channel fields?', align=Align.INLINE)
d.comment(0x9BE4, 'No: copy next field', align=Align.INLINE)
d.comment(0x9BE6, 'Pull saved FCB index', align=Align.INLINE)
d.comment(0x9BE7, 'Restore to fs_block_offset', align=Align.INLINE)
d.comment(0x9BE9, 'Compare with 5', align=Align.INLINE)
d.comment(0x9BEB, '5 or above: return with last flag', align=Align.INLINE)
d.comment(0x9BED, 'Compare Y with 0', align=Align.INLINE)
d.comment(0x9BEF, 'Non-zero: handle OSFIND with channel', align=Align.INLINE)
d.comment(0x9BF1, 'Y=0 (close): jump to OSFIND open', align=Align.INLINE)
d.comment(0x9BF4, 'Push sub-function', align=Align.INLINE)
d.comment(0x9BF5, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9BF6, 'Push X (FCB slot)', align=Align.INLINE)
d.comment(0x9BF7, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9BF8, 'Push Y (channel char)', align=Align.INLINE)
d.comment(0x9BF9, 'Check file is not a directory', align=Align.INLINE)
d.comment(0x9BFC, 'Pull channel char', align=Align.INLINE)
d.comment(0x9BFD, 'Y=&0E: error code offset', align=Align.INLINE)
d.comment(0x9BFF, 'Store channel char in RX buffer', align=Align.INLINE)
d.comment(0x9C01, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9C04, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9C07, 'Pull X (FCB slot)', align=Align.INLINE)
d.comment(0x9C08, 'Restore X', align=Align.INLINE)
d.comment(0x9C09, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9C0A, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0x9C0B, 'Zero (OSFIND close): handle close', align=Align.INLINE)
d.comment(0x9C0D, 'Save flags (carry from LSR)', align=Align.INLINE)
d.comment(0x9C0E, 'Push sub-function', align=Align.INLINE)
d.comment(0x9C0F, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9C11, 'Load block offset', align=Align.INLINE)
d.comment(0x9C13, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9C16, 'Load updated data from l1010', align=Align.INLINE)
d.comment(0x9C19, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9C1C, 'Pull sub-function', align=Align.INLINE)
d.comment(0x9C1D, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9C20, 'Restore flags', align=Align.INLINE)
d.comment(0x9C21, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9C22, 'Push Y (offset)', align=Align.INLINE)
d.comment(0x9C23, 'Carry clear: read operation', align=Align.INLINE)
d.comment(0x9C25, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9C27, 'Load zero page data', align=Align.INLINE)
d.comment(0x9C29, 'Store in l0f07 buffer', align=Align.INLINE)
d.comment(0x9C2C, 'Decrement source', align=Align.INLINE)
d.comment(0x9C2D, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C2E, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C30, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9C32, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9C34, 'Send TX control block to server', align=Align.INLINE)
d.comment(0x9C37, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9C39, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9C3A, 'Set connection active flag', align=Align.INLINE)
d.comment(0x9C3D, 'Return with last flag', align=Align.INLINE)
d.comment(0x9C40, 'Y=&0C: TX buffer size (smaller)', align=Align.INLINE)
d.comment(0x9C42, 'X=2: argument offset', align=Align.INLINE)
d.comment(0x9C44, 'Send TX control block', align=Align.INLINE)
d.comment(0x9C47, 'Store A in last byte flag', align=Align.INLINE)
d.comment(0x9C49, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9C4B, 'Y=2: zero page offset', align=Align.INLINE)
d.comment(0x9C4D, 'Store A in zero page', align=Align.INLINE)
d.comment(0x9C4F, 'Load buffer byte from l0f05+Y', align=Align.INLINE)
d.comment(0x9C52, 'Store in zero page at offset', align=Align.INLINE)
d.comment(0x9C54, 'Decrement source X', align=Align.INLINE)
d.comment(0x9C55, 'Decrement counter Y', align=Align.INLINE)
d.comment(0x9C56, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9C58, 'Pull saved offset', align=Align.INLINE)
d.comment(0x9C59, 'Return with last flag', align=Align.INLINE)
d.comment(0x9C5C, 'Carry set: write file pointer', align=Align.INLINE)
d.comment(0x9C5E, 'Load block offset', align=Align.INLINE)
d.comment(0x9C60, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9C63, 'Load FS options pointer', align=Align.INLINE)
d.comment(0x9C65, 'Load FCB low byte from l1000', align=Align.INLINE)
d.comment(0x9C68, 'Store in zero page pointer low', align=Align.INLINE)
d.comment(0x9C6B, 'Load FCB high byte from l1010', align=Align.INLINE)
d.comment(0x9C6E, 'Store in zero page pointer high', align=Align.INLINE)
d.comment(0x9C71, 'Load FCB extent from l1020', align=Align.INLINE)
d.comment(0x9C74, 'Store in zero page work area', align=Align.INLINE)
d.comment(0x9C77, 'A=0: clear high byte', align=Align.INLINE)
d.comment(0x9C79, 'Store zero in work area high', align=Align.INLINE)
d.comment(0x9C7C, 'ALWAYS branch to return with flag', align=Align.INLINE)
d.comment(0x9C7E, 'Store write value in l0f06', align=Align.INLINE)
d.comment(0x9C81, 'Transfer X to A', align=Align.INLINE)
d.comment(0x9C82, 'Push X (zero page offset)', align=Align.INLINE)
d.comment(0x9C83, 'Y=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x9C85, 'Load zero page data at offset', align=Align.INLINE)
d.comment(0x9C87, 'Store in l0f07 buffer', align=Align.INLINE)
d.comment(0x9C8A, 'Decrement source', align=Align.INLINE)
d.comment(0x9C8B, 'Decrement counter', align=Align.INLINE)
d.comment(0x9C8C, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x9C8E, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9C90, 'X=5: argument offset', align=Align.INLINE)
d.comment(0x9C92, 'Send TX control block', align=Align.INLINE)
d.comment(0x9C95, 'Store X in last byte flag', align=Align.INLINE)
d.comment(0x9C97, 'Pull saved zero page offset', align=Align.INLINE)
d.comment(0x9C98, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9C99, 'Load block offset (attribute)', align=Align.INLINE)
d.comment(0x9C9B, 'Clear connection active flag', align=Align.INLINE)
d.comment(0x9C9E, 'Convert attribute to channel index', align=Align.INLINE)
d.comment(0x9CA1, 'Load zero page pointer low', align=Align.INLINE)
d.comment(0x9CA4, 'Store back to FCB l1000', align=Align.INLINE)
d.comment(0x9CA7, 'Load zero page pointer high', align=Align.INLINE)
d.comment(0x9CAA, 'Store back to FCB l1010', align=Align.INLINE)
d.comment(0x9CAD, 'Load zero page work byte', align=Align.INLINE)
d.comment(0x9CB0, 'Store back to FCB l1020', align=Align.INLINE)
d.comment(0x9CB3, 'Return with last flag', align=Align.INLINE)
d.comment(0x9CB6, 'Process all matching FCBs first', align=Align.INLINE)
d.comment(0x9CB9, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9CBB, 'Push result on stack', align=Align.INLINE)
d.comment(0x9CBC, 'A=0: clear error flag', align=Align.INLINE)
d.comment(0x9CBE, 'Y=&0E: error code offset', align=Align.INLINE)
d.comment(0x9CC0, 'Clear error code in RX buffer', align=Align.INLINE)
d.comment(0x9CC2, 'Pull result back', align=Align.INLINE)
d.comment(0x9CC3, 'Restore X from FS options pointer', align=Align.INLINE)
d.comment(0x9CC5, 'Restore Y from block offset', align=Align.INLINE)
d.comment(0x9CC7, 'Return to caller', align=Align.INLINE)
d.comment(0x9CC8, 'Compare with 2 (open for output)', align=Align.INLINE)
d.comment(0x9CCA, '2 or above: handle file open', align=Align.INLINE)
d.comment(0x9CCC, 'Transfer to Y (Y=0 or 1)', align=Align.INLINE)
d.comment(0x9CCD, 'Non-zero (1 = read pointer): copy data', align=Align.INLINE)
d.comment(0x9CCF, 'A=5: return code for close-all', align=Align.INLINE)
d.comment(0x9CD1, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0x9CD3, 'Load reply data byte at Y', align=Align.INLINE)
d.comment(0x9CD6, 'Store in FS options', align=Align.INLINE)
d.comment(0x9CD8, 'Decrement index', align=Align.INLINE)
d.comment(0x9CD9, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9CDB, 'Clear zero page work low', align=Align.INLINE)
d.comment(0x9CDD, 'Clear zero page work high', align=Align.INLINE)
d.comment(0x9CDF, 'Z set: jump to clear A and return', align=Align.INLINE)
d.comment(0x9CE1, 'A=0: clear result', align=Align.INLINE)
d.comment(0x9CE3, 'Shift right (always positive)', align=Align.INLINE)
d.comment(0x9CE4, 'Positive: jump to finalise', align=Align.INLINE)
d.comment(0x9CE6, 'Mask to 6-bit access value', align=Align.INLINE)
d.comment(0x9CE8, 'Non-zero: clear A and finalise', align=Align.INLINE)
d.comment(0x9CEA, 'Transfer X to A (options pointer)', align=Align.INLINE)
d.comment(0x9CEB, 'Allocate FCB slot or raise error', align=Align.INLINE)
d.comment(0x9CEE, 'Toggle bit 7', align=Align.INLINE)
d.comment(0x9CF0, 'Shift left: build open mode', align=Align.INLINE)
d.comment(0x9CF1, 'Store open mode in l0f05', align=Align.INLINE)
d.comment(0x9CF4, 'Rotate to complete mode byte', align=Align.INLINE)
d.comment(0x9CF5, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9CF8, 'Parse command argument (Y=0)', align=Align.INLINE)
d.comment(0x9CFB, 'X=2: buffer offset', align=Align.INLINE)
d.comment(0x9CFD, 'Copy argument to TX buffer', align=Align.INLINE)
d.comment(0x9D00, 'Y=6: open file command', align=Align.INLINE)
d.comment(0x9D02, 'Set V flag (skip directory check)', align=Align.INLINE)
d.comment(0x9D05, 'Set carry', align=Align.INLINE)
d.comment(0x9D06, 'Rotate carry into escapable flag bit 7', align=Align.INLINE)
d.comment(0x9D08, 'Send open request with V set', align=Align.INLINE)
d.comment(0x9D0B, 'Carry set (error): jump to finalise', align=Align.INLINE)
d.comment(0x9D0D, 'A=&FF: mark as newly opened', align=Align.INLINE)
d.comment(0x9D0F, 'Y=&0E: error code offset', align=Align.INLINE)
d.comment(0x9D11, 'Store &FF as error flag in RX buffer', align=Align.INLINE)
d.comment(0x9D13, 'Load handle from l0f05', align=Align.INLINE)
d.comment(0x9D16, 'Push handle', align=Align.INLINE)
d.comment(0x9D17, 'A=4: file info sub-command', align=Align.INLINE)
d.comment(0x9D19, 'Store sub-command', align=Align.INLINE)
d.comment(0x9D1C, 'X=1: shift filename', align=Align.INLINE)
d.comment(0x9D1E, 'Load filename byte from l0f06+X', align=Align.INLINE)
d.comment(0x9D21, 'Shift down to l0f05+X', align=Align.INLINE)
d.comment(0x9D24, 'Advance source index', align=Align.INLINE)
d.comment(0x9D25, 'Is it CR (end of filename)?', align=Align.INLINE)
d.comment(0x9D27, 'No: continue shifting', align=Align.INLINE)
d.comment(0x9D29, 'Y=&12: file info request', align=Align.INLINE)
d.comment(0x9D2B, 'Send file info request', align=Align.INLINE)
d.comment(0x9D2E, 'Load last byte flag', align=Align.INLINE)
d.comment(0x9D30, 'Clear bit 6 (read/write bits)', align=Align.INLINE)
d.comment(0x9D32, 'OR with reply access byte', align=Align.INLINE)
d.comment(0x9D35, 'Set bit 0 (file is open)', align=Align.INLINE)
d.comment(0x9D37, 'Transfer to Y (access flags)', align=Align.INLINE)
d.comment(0x9D38, 'Check bit 1 (write access)', align=Align.INLINE)
d.comment(0x9D3A, 'No write access: check read-only', align=Align.INLINE)
d.comment(0x9D3C, 'Pull handle from stack', align=Align.INLINE)
d.comment(0x9D3D, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0x9D40, 'Non-zero: FCB allocated, store flags', align=Align.INLINE)
d.comment(0x9D42, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9D45, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9D48, 'Transfer A to X', align=Align.INLINE)
d.comment(0x9D49, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9D4C, 'Transfer X back to A', align=Align.INLINE)
d.comment(0x9D4D, 'Zero: close file, process FCBs', align=Align.INLINE)
d.comment(0x9D4F, 'Save text pointer for OS', align=Align.INLINE)
d.comment(0x9D52, 'Load current directory handle', align=Align.INLINE)
d.comment(0x9D55, 'Zero: allocate new FCB', align=Align.INLINE)
d.comment(0x9D57, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9D58, 'X=0: clear directory handle', align=Align.INLINE)
d.comment(0x9D5A, 'Store zero (clear handle)', align=Align.INLINE)
d.comment(0x9D5D, 'ALWAYS branch to finalise', align=Align.INLINE)
d.comment(0x9D5F, 'Load access/open mode byte', align=Align.INLINE)
d.comment(0x9D62, 'Rotate right: check bit 0', align=Align.INLINE)
d.comment(0x9D63, 'Carry set (bit 0): check read permission', align=Align.INLINE)
d.comment(0x9D65, 'Rotate right: check bit 1', align=Align.INLINE)
d.comment(0x9D66, 'Carry clear (no write): skip', align=Align.INLINE)
d.comment(0x9D68, 'Test bit 7 of l0f07 (lock flag)', align=Align.INLINE)
d.comment(0x9D6B, 'Not locked: skip', align=Align.INLINE)
d.comment(0x9D6D, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0x9D6E, 'Set bit 5 (locked file flag)', align=Align.INLINE)
d.comment(0x9D70, 'Transfer back to Y', align=Align.INLINE)
d.comment(0x9D71, 'Pull handle from stack', align=Align.INLINE)
d.comment(0x9D72, 'Allocate FCB slot for channel', align=Align.INLINE)
d.comment(0x9D75, 'Transfer to X', align=Align.INLINE)
d.comment(0x9D76, 'Transfer Y to A (flags)', align=Align.INLINE)
d.comment(0x9D77, 'Store flags in FCB table l1040', align=Align.INLINE)
d.comment(0x9D7A, 'Transfer X back to A (handle)', align=Align.INLINE)
d.comment(0x9D7B, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9D7E, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9D81, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9D82, 'Non-zero channel: close specific', align=Align.INLINE)
d.comment(0x9D84, 'Load FS options pointer low', align=Align.INLINE)
d.comment(0x9D86, 'Push (save for restore)', align=Align.INLINE)
d.comment(0x9D87, 'A=&77: OSBYTE close spool/exec files', align=Align.INLINE)
d.comment(0x9D89, 'Close any *SPOOL and *EXEC files', align=Align.INLINE)
d.comment(0x9D8C, 'Pull saved options pointer', align=Align.INLINE)
d.comment(0x9D8D, 'Restore FS options pointer', align=Align.INLINE)
d.comment(0x9D8F, 'A=0: clear flags', align=Align.INLINE)
d.comment(0x9D91, 'Clear last byte flag', align=Align.INLINE)
d.comment(0x9D93, 'Clear block offset', align=Align.INLINE)
d.comment(0x9D95, 'ALWAYS branch to send close request', align=Align.INLINE)
d.comment(0x9D97, 'Validate channel character', align=Align.INLINE)
d.comment(0x9D9A, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9D9D, 'Store as l0f05 (file handle)', align=Align.INLINE)
d.comment(0x9DA0, 'X=1: argument size', align=Align.INLINE)
d.comment(0x9DA2, 'Y=7: close file command', align=Align.INLINE)
d.comment(0x9DA4, 'Send close file request', align=Align.INLINE)
d.comment(0x9DA7, 'Load block offset', align=Align.INLINE)
d.comment(0x9DA9, 'Non-zero: clear single FCB', align=Align.INLINE)
d.comment(0x9DAB, 'Clear V flag', align=Align.INLINE)
d.comment(0x9DAC, 'Scan and clear all FCB flags', align=Align.INLINE)
d.comment(0x9DAF, 'Return with last flag', align=Align.INLINE)
d.comment(0x9DB2, 'A=0: clear FCB entry', align=Align.INLINE)
d.comment(0x9DB4, 'Clear l1010 (FCB high byte)', align=Align.INLINE)
d.comment(0x9DB7, 'Clear l1040 (FCB flags)', align=Align.INLINE)
d.comment(0x9DBA, 'ALWAYS branch to return', align=Align.INLINE)
d.comment(0x9DBC, 'Z set: handle OSARGS 0', align=Align.INLINE)
d.comment(0x9DBE, 'Compare X with 4 (number of args)', align=Align.INLINE)
d.comment(0x9DC0, 'Not 4: check for error', align=Align.INLINE)
d.comment(0x9DC2, 'Compare Y with 4', align=Align.INLINE)
d.comment(0x9DC4, 'Below 4: handle special OSARGS', align=Align.INLINE)
d.comment(0x9DC6, 'Decrement X', align=Align.INLINE)
d.comment(0x9DC7, 'X was 1: store display flag', align=Align.INLINE)
d.comment(0x9DC9, 'Store Y in display control flag l0e06', align=Align.INLINE)
d.comment(0x9DCC, 'Carry clear: return with flag', align=Align.INLINE)
d.comment(0x9DCE, 'A=7: error code', align=Align.INLINE)
d.comment(0x9DD0, 'Jump to classify reply error', align=Align.INLINE)
d.comment(0x9DD3, 'Store Y in l0f05', align=Align.INLINE)
d.comment(0x9DD6, 'Y=&16: OSARGS save command', align=Align.INLINE)
d.comment(0x9DD8, 'Send OSARGS request', align=Align.INLINE)
d.comment(0x9DDB, 'Reload block offset', align=Align.INLINE)
d.comment(0x9DDD, 'Store in l0e05', align=Align.INLINE)
d.comment(0x9DE0, 'Positive: return with flag', align=Align.INLINE)
d.comment(0x9DE2, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9DE5, 'Push result on stack', align=Align.INLINE)
d.comment(0x9DE6, 'Load block offset', align=Align.INLINE)
d.comment(0x9DE8, 'Push block offset', align=Align.INLINE)
d.comment(0x9DE9, 'Store X in l10c9', align=Align.INLINE)
d.comment(0x9DEC, 'Find matching FCB entry', align=Align.INLINE)
d.comment(0x9DEF, 'Zero: no match found', align=Align.INLINE)
d.comment(0x9DF1, 'Load FCB low byte from l1000', align=Align.INLINE)
d.comment(0x9DF4, 'Compare with stored offset l1098', align=Align.INLINE)
d.comment(0x9DF7, 'Below stored: no match', align=Align.INLINE)
d.comment(0x9DF9, 'X=&FF: mark as found (all bits set)', align=Align.INLINE)
d.comment(0x9DFB, 'ALWAYS branch (negative)', align=Align.INLINE)
d.comment(0x9DFD, 'X=0: mark as not found', align=Align.INLINE)
d.comment(0x9DFF, 'Restore block offset from stack', align=Align.INLINE)
d.comment(0x9E00, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9E01, 'Restore result from stack', align=Align.INLINE)
d.comment(0x9E02, 'Return', align=Align.INLINE)
d.comment(0x9E03, 'Y=9: FS options offset for high address', align=Align.INLINE)
d.comment(0x9E05, 'Add workspace values to FS options', align=Align.INLINE)
d.comment(0x9E08, 'Y=1: FS options offset for low address', align=Align.INLINE)
d.comment(0x9E0A, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9E0B, 'X=&FC: loop counter (-4 to -1)', align=Align.INLINE)
d.comment(0x9E0D, 'Load FS options byte at offset Y', align=Align.INLINE)
d.comment(0x9E0F, 'Test fs_load_addr_2 bit 7 (add/subtract)', align=Align.INLINE)
d.comment(0x9E11, 'Bit 7 set: subtract instead', align=Align.INLINE)
d.comment(0x9E13, 'Add workspace byte to FS options', align=Align.INLINE)
d.comment(0x9E16, 'Jump to store result', align=Align.INLINE)
d.comment(0x9E19, 'Subtract workspace byte from FS options', align=Align.INLINE)
d.comment(0x9E1C, 'Store result back to FS options', align=Align.INLINE)
d.comment(0x9E1E, 'Advance to next byte', align=Align.INLINE)
d.comment(0x9E1F, 'Advance counter', align=Align.INLINE)
d.comment(0x9E20, 'Loop until 4 bytes processed', align=Align.INLINE)
d.comment(0x9E22, 'Return', align=Align.INLINE)
d.comment(0x9E23, 'Verify workspace checksum', align=Align.INLINE)
d.comment(0x9E26, 'Set up transfer parameters', align=Align.INLINE)
d.comment(0x9E29, 'Push transfer type on stack', align=Align.INLINE)
d.comment(0x9E2A, 'Set owner-only access mask', align=Align.INLINE)
d.comment(0x9E2D, 'Pull transfer type', align=Align.INLINE)
d.comment(0x9E2E, 'Transfer to X', align=Align.INLINE)
d.comment(0x9E2F, 'Zero: no valid operation, return', align=Align.INLINE)
d.comment(0x9E31, 'Decrement (convert 1-based to 0-based)', align=Align.INLINE)
d.comment(0x9E32, 'Compare with 8 (max operation)', align=Align.INLINE)
d.comment(0x9E34, 'Below 8: valid operation', align=Align.INLINE)
d.comment(0x9E36, 'Out of range: return with flag', align=Align.INLINE)
d.comment(0x9E39, 'Transfer operation code to A', align=Align.INLINE)
d.comment(0x9E3A, 'Y=0: buffer offset', align=Align.INLINE)
d.comment(0x9E3C, 'Push operation code', align=Align.INLINE)
d.comment(0x9E3D, 'Compare with 4 (write operations)', align=Align.INLINE)
d.comment(0x9E3F, 'Below 4: read operation', align=Align.INLINE)
d.comment(0x9E41, '4 or above: write data block', align=Align.INLINE)
d.comment(0x9E44, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9E46, 'Push handle', align=Align.INLINE)
d.comment(0x9E47, 'Check file is not a directory', align=Align.INLINE)
d.comment(0x9E4A, 'Pull handle', align=Align.INLINE)
d.comment(0x9E4B, 'Transfer to Y', align=Align.INLINE)
d.comment(0x9E4C, 'Process all matching FCBs', align=Align.INLINE)
d.comment(0x9E4F, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9E52, 'Store file handle in l0f05', align=Align.INLINE)
d.comment(0x9E55, 'A=0: clear direction flag', align=Align.INLINE)
d.comment(0x9E57, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9E5A, 'Load FCB low byte (position)', align=Align.INLINE)
d.comment(0x9E5D, 'Store in l0f07', align=Align.INLINE)
d.comment(0x9E60, 'Load FCB high byte', align=Align.INLINE)
d.comment(0x9E63, 'Store in l0f08', align=Align.INLINE)
d.comment(0x9E66, 'Load FCB extent byte', align=Align.INLINE)
d.comment(0x9E69, 'Store in l0f09', align=Align.INLINE)
d.comment(0x9E6C, 'Y=&0D: TX buffer size', align=Align.INLINE)
d.comment(0x9E6E, 'X=5: argument count', align=Align.INLINE)
d.comment(0x9E70, 'Send TX control block to server', align=Align.INLINE)
d.comment(0x9E73, 'Pull operation code', align=Align.INLINE)
d.comment(0x9E74, 'Set up transfer workspace', align=Align.INLINE)
d.comment(0x9E77, 'Save flags (carry from setup)', align=Align.INLINE)
d.comment(0x9E78, 'Y=0: index for channel handle', align=Align.INLINE)
d.comment(0x9E7A, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9E7C, 'Carry set (write): set active', align=Align.INLINE)
d.comment(0x9E7E, 'Read: clear connection active', align=Align.INLINE)
d.comment(0x9E81, 'Branch to continue (always positive)', align=Align.INLINE)
d.comment(0x9E83, 'Write: set connection active', align=Align.INLINE)
d.comment(0x9E86, 'Clear l0f06 (Y=0)', align=Align.INLINE)
d.comment(0x9E89, 'Look up channel slot data', align=Align.INLINE)
d.comment(0x9E8C, 'Store flag byte in l0f05', align=Align.INLINE)
d.comment(0x9E8F, 'Y=&0C: TX buffer size (short)', align=Align.INLINE)
d.comment(0x9E91, 'X=2: argument count', align=Align.INLINE)
d.comment(0x9E93, 'Send TX control block', align=Align.INLINE)
d.comment(0x9E96, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0x9E99, 'Y=9: FS options offset for position', align=Align.INLINE)
d.comment(0x9E9B, 'Load new position low from l0f05', align=Align.INLINE)
d.comment(0x9E9E, 'Update FCB low byte in l1000', align=Align.INLINE)
d.comment(0x9EA1, 'Store in FS options at Y=9', align=Align.INLINE)
d.comment(0x9EA3, 'Y=&0A', align=Align.INLINE)
d.comment(0x9EA4, 'Load new position high from l0f06', align=Align.INLINE)
d.comment(0x9EA7, 'Update FCB high byte in l1010', align=Align.INLINE)
d.comment(0x9EAA, 'Store in FS options at Y=&0A', align=Align.INLINE)
d.comment(0x9EAC, 'Y=&0B', align=Align.INLINE)
d.comment(0x9EAD, 'Load new extent from l0f07', align=Align.INLINE)
d.comment(0x9EB0, 'Update FCB extent in l1020', align=Align.INLINE)
d.comment(0x9EB3, 'Store in FS options at Y=&0B', align=Align.INLINE)
d.comment(0x9EB5, 'A=0: clear high byte of extent', align=Align.INLINE)
d.comment(0x9EB7, 'Y=&0C', align=Align.INLINE)
d.comment(0x9EB8, 'Store zero in FS options at Y=&0C', align=Align.INLINE)
d.comment(0x9EBA, 'Restore flags', align=Align.INLINE)
d.comment(0x9EBB, 'A=0: success', align=Align.INLINE)
d.comment(0x9EBD, 'Jump to finalise and return', align=Align.INLINE)
d.comment(0x9EC0, 'Y=0: offset for channel handle', align=Align.INLINE)
d.comment(0x9EC2, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9EC4, 'Look up channel by character', align=Align.INLINE)
d.comment(0x9EC7, 'Load FCB flag byte from l1030', align=Align.INLINE)
d.comment(0x9ECA, 'Return with flag in A', align=Align.INLINE)
d.comment(0x9ECB, 'Push operation code on stack', align=Align.INLINE)
d.comment(0x9ECC, 'Look up channel entry at Y=0', align=Align.INLINE)
d.comment(0x9ECF, 'Store flag byte in l0f05', align=Align.INLINE)
d.comment(0x9ED2, 'Y=&0B: source offset in FS options', align=Align.INLINE)
d.comment(0x9ED4, 'X=6: copy 6 bytes', align=Align.INLINE)
d.comment(0x9ED6, 'Load FS options byte', align=Align.INLINE)
d.comment(0x9ED8, 'Store in l0f06 buffer', align=Align.INLINE)
d.comment(0x9EDB, 'Decrement source index', align=Align.INLINE)
d.comment(0x9EDC, 'Skip offset 8?', align=Align.INLINE)
d.comment(0x9EDE, 'No: continue copy', align=Align.INLINE)
d.comment(0x9EE0, 'Skip offset 8 (hole in structure)', align=Align.INLINE)
d.comment(0x9EE1, 'Decrement destination counter', align=Align.INLINE)
d.comment(0x9EE2, 'Loop until all 6 bytes copied', align=Align.INLINE)
d.comment(0x9EE4, 'Pull operation code', align=Align.INLINE)
d.comment(0x9EE5, 'Shift right: check bit 0 (direction)', align=Align.INLINE)
d.comment(0x9EE6, 'Push updated code', align=Align.INLINE)
d.comment(0x9EE7, 'Carry clear: OSBGET (read)', align=Align.INLINE)
d.comment(0x9EE9, 'Carry set: OSBPUT (write), X=1', align=Align.INLINE)
d.comment(0x9EEA, 'Store direction flag in l0f06', align=Align.INLINE)
d.comment(0x9EED, 'Y=&0B: TX buffer size', align=Align.INLINE)
d.comment(0x9EEF, 'X=&91: port for OSBGET', align=Align.INLINE)
d.comment(0x9EF1, 'Pull operation code', align=Align.INLINE)
d.comment(0x9EF2, 'Push back (keep on stack)', align=Align.INLINE)
d.comment(0x9EF3, 'Zero (OSBGET): keep port &91', align=Align.INLINE)
d.comment(0x9EF5, 'X=&92: port for OSBPUT', align=Align.INLINE)
d.comment(0x9EF7, 'Y=&0A: adjusted buffer size', align=Align.INLINE)
d.comment(0x9EF8, 'Store port in l0f02', align=Align.INLINE)
d.comment(0x9EFB, 'Store port in fs_error_ptr', align=Align.INLINE)
d.comment(0x9EFD, 'X=8: argument count', align=Align.INLINE)
d.comment(0x9EFF, 'Load file handle from l0f05', align=Align.INLINE)
d.comment(0x9F02, 'Send request (no write data)', align=Align.INLINE)
d.comment(0x9F05, 'X=0: index', align=Align.INLINE)
d.comment(0x9F07, 'Load channel handle from FS options', align=Align.INLINE)
d.comment(0x9F09, 'Transfer to X as index', align=Align.INLINE)
d.comment(0x9F0A, 'Load FCB flags from l1040', align=Align.INLINE)
d.comment(0x9F0D, 'Toggle bit 0 (transfer direction)', align=Align.INLINE)
d.comment(0x9F0F, 'Store updated flags', align=Align.INLINE)
d.comment(0x9F12, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9F13, 'X=4: process 4 address bytes', align=Align.INLINE)
d.comment(0x9F15, 'Load FS options address byte', align=Align.INLINE)
d.comment(0x9F17, 'Store in zero page address area', align=Align.INLINE)
d.comment(0x9F1A, 'Store in TXCB position', align=Align.INLINE)
d.comment(0x9F1D, 'Advance Y by 4', align=Align.INLINE)
d.comment(0x9F20, 'Add offset from FS options', align=Align.INLINE)
d.comment(0x9F22, 'Store computed end address', align=Align.INLINE)
d.comment(0x9F25, 'Retreat Y by 3 for next pair', align=Align.INLINE)
d.comment(0x9F28, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9F29, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x9F2B, 'X=1 (INX from 0)', align=Align.INLINE)
d.comment(0x9F2C, 'Load offset from l0f03', align=Align.INLINE)
d.comment(0x9F2F, 'Copy to l0f06', align=Align.INLINE)
d.comment(0x9F32, 'Decrement counter', align=Align.INLINE)
d.comment(0x9F33, 'Loop until both bytes copied', align=Align.INLINE)
d.comment(0x9F35, 'Pull operation code', align=Align.INLINE)
d.comment(0x9F36, 'Non-zero (OSBPUT): swap addresses', align=Align.INLINE)
d.comment(0x9F38, 'Load port from l0f02', align=Align.INLINE)
d.comment(0x9F3B, 'Check and set up TXCB', align=Align.INLINE)
d.comment(0x9F3E, 'Carry set: skip swap', align=Align.INLINE)
d.comment(0x9F40, 'Send TXCB and swap start/end addresses', align=Align.INLINE)
d.comment(0x9F43, 'Receive and process reply', align=Align.INLINE)
d.comment(0x9F46, 'Store result in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F48, 'Update addresses from offset 9', align=Align.INLINE)
d.comment(0x9F4B, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F4D, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9F4E, 'Adjust FS options by 4 bytes', align=Align.INLINE)
d.comment(0x9F51, 'Shift l0f05 left (update status)', align=Align.INLINE)
d.comment(0x9F54, 'Return', align=Align.INLINE)
d.comment(0x9F55, 'Y=&15: TX buffer size for OSBPUT data', align=Align.INLINE)
d.comment(0x9F57, 'Send TX control block', align=Align.INLINE)
d.comment(0x9F5A, 'Load display flag from l0e05', align=Align.INLINE)
d.comment(0x9F5D, 'Store in l0f16', align=Align.INLINE)
d.comment(0x9F60, 'Clear fs_load_addr (X=0)', align=Align.INLINE)
d.comment(0x9F62, 'Clear fs_load_addr_hi', align=Align.INLINE)
d.comment(0x9F64, 'A=&12: byte count for data block', align=Align.INLINE)
d.comment(0x9F66, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9F68, 'ALWAYS branch to write data block', align=Align.INLINE)
d.comment(0x9F6A, 'Y=4: offset for station comparison', align=Align.INLINE)
d.comment(0x9F6C, 'Load stored station from l0d63', align=Align.INLINE)
d.comment(0x9F6F, 'Zero: skip station check', align=Align.INLINE)
d.comment(0x9F71, 'Compare with FS options station', align=Align.INLINE)
d.comment(0x9F73, 'Mismatch: skip subtraction', align=Align.INLINE)
d.comment(0x9F75, 'Y=3', align=Align.INLINE)
d.comment(0x9F76, 'Subtract FS options value', align=Align.INLINE)
d.comment(0x9F78, 'Store result in svc_state', align=Align.INLINE)
d.comment(0x9F7A, 'Load FS options byte at Y', align=Align.INLINE)
d.comment(0x9F7C, 'Store in workspace at fs_last_byte_flag+Y', align=Align.INLINE)
d.comment(0x9F7F, 'Decrement index', align=Align.INLINE)
d.comment(0x9F80, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9F82, 'Pull operation code', align=Align.INLINE)
d.comment(0x9F83, 'Mask to 2-bit sub-operation', align=Align.INLINE)
d.comment(0x9F85, 'Zero: send OSBPUT data', align=Align.INLINE)
d.comment(0x9F87, 'Shift right: check bit 0', align=Align.INLINE)
d.comment(0x9F88, 'Zero (bit 0 clear): handle read', align=Align.INLINE)
d.comment(0x9F8A, 'Carry set: handle catalogue update', align=Align.INLINE)
d.comment(0x9F8C, 'Transfer to Y (Y=0)', align=Align.INLINE)
d.comment(0x9F8D, 'Load data byte from l0e03', align=Align.INLINE)
d.comment(0x9F90, 'Store in l0f03', align=Align.INLINE)
d.comment(0x9F93, 'Load high data byte from l0e04', align=Align.INLINE)
d.comment(0x9F96, 'Store in l0f04', align=Align.INLINE)
d.comment(0x9F99, 'Load port from l0e02', align=Align.INLINE)
d.comment(0x9F9C, 'Store in l0f02', align=Align.INLINE)
d.comment(0x9F9F, 'X=&12: buffer size marker', align=Align.INLINE)
d.comment(0x9FA1, 'Store in l0f01', align=Align.INLINE)
d.comment(0x9FA4, 'A=&0D: count value', align=Align.INLINE)
d.comment(0x9FA6, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9FA9, 'Store in fs_load_addr_2', align=Align.INLINE)
d.comment(0x9FAB, 'Shift right (A=6)', align=Align.INLINE)
d.comment(0x9FAC, 'Store in l0f05', align=Align.INLINE)
d.comment(0x9FAF, 'Clear carry for addition', align=Align.INLINE)
d.comment(0x9FB0, 'Prepare and send TX control block', align=Align.INLINE)
d.comment(0x9FB3, 'Store X in fs_load_addr_hi (X=0)', align=Align.INLINE)
d.comment(0x9FB5, 'X=1 (INX)', align=Align.INLINE)
d.comment(0x9FB6, 'Store X in fs_load_addr', align=Align.INLINE)
d.comment(0x9FB8, 'Load svc_state (tube flag)', align=Align.INLINE)
d.comment(0x9FBA, 'Non-zero: write via tube', align=Align.INLINE)
d.comment(0x9FBC, 'Load source index from fs_load_addr', align=Align.INLINE)
d.comment(0x9FBE, 'Load destination index from fs_load_addr_hi', align=Align.INLINE)
d.comment(0x9FC0, 'Load data byte from l0f05 buffer', align=Align.INLINE)
d.comment(0x9FC3, 'Store to destination via fs_crc pointer', align=Align.INLINE)
d.comment(0x9FC5, 'Advance source index', align=Align.INLINE)
d.comment(0x9FC6, 'Advance destination index', align=Align.INLINE)
d.comment(0x9FC7, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9FC9, 'Loop until all bytes transferred', align=Align.INLINE)
d.comment(0x9FCB, 'ALWAYS branch to update catalogue', align=Align.INLINE)
d.comment(0x9FCD, 'Claim tube with call &C3', align=Align.INLINE)
d.comment(0x9FD0, 'A=1: tube transfer type (write)', align=Align.INLINE)
d.comment(0x9FD2, 'Load destination low from fs_options', align=Align.INLINE)
d.comment(0x9FD4, 'Load destination high from fs_block_offset', align=Align.INLINE)
d.comment(0x9FD6, 'Increment low byte', align=Align.INLINE)
d.comment(0x9FD7, 'No wrap: skip high increment', align=Align.INLINE)
d.comment(0x9FD9, 'Carry: increment high byte', align=Align.INLINE)
d.comment(0x9FDA, 'Set up tube transfer address', align=Align.INLINE)
d.comment(0x9FDD, 'Load source index', align=Align.INLINE)
d.comment(0x9FDF, 'Load data byte from buffer', align=Align.INLINE)
d.comment(0x9FE2, 'Write to tube data register 3', align=Align.INLINE)
d.comment(0x9FE5, 'Advance source index', align=Align.INLINE)
d.comment(0x9FE6, 'Y=6: tube write delay', align=Align.INLINE)
d.comment(0x9FE8, 'Delay loop: decrement Y', align=Align.INLINE)
d.comment(0x9FE9, 'Loop until delay complete', align=Align.INLINE)
d.comment(0x9FEB, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9FED, 'Loop until all bytes written to tube', align=Align.INLINE)
d.comment(0x9FEF, 'A=&83: release tube claim', align=Align.INLINE)
d.comment(0x9FF1, 'Release tube', align=Align.INLINE)
d.comment(0x9FF4, 'Jump to clear A and finalise return', align=Align.INLINE)
d.comment(0x9FF7, 'Y=9: offset for position byte', align=Align.INLINE)
d.comment(0x9FF9, 'Load position from FS options', align=Align.INLINE)
d.comment(0x9FFB, 'Store in l0f06', align=Align.INLINE)
d.comment(0x9FFE, 'Y=5: offset for extent byte', align=Align.INLINE)
d.comment(0xA000, 'Load extent byte from FS options', align=Align.INLINE)
d.comment(0xA002, 'Store in l0f07', align=Align.INLINE)
d.comment(0xA005, 'X=&0D: byte count', align=Align.INLINE)
d.comment(0xA007, 'Store in l0f08', align=Align.INLINE)
d.comment(0xA00A, 'Y=2: command sub-type', align=Align.INLINE)
d.comment(0xA00C, 'Store in fs_load_addr', align=Align.INLINE)
d.comment(0xA00E, 'Store in l0f05', align=Align.INLINE)
d.comment(0xA011, 'Y=3: TX buffer command byte', align=Align.INLINE)
d.comment(0xA012, 'Send TX control block', align=Align.INLINE)
d.comment(0xA015, 'Store X (0) in fs_load_addr_hi', align=Align.INLINE)
d.comment(0xA017, 'Load data offset from l0f06', align=Align.INLINE)
d.comment(0xA01A, 'Store as first byte of FS options', align=Align.INLINE)
d.comment(0xA01C, 'Load data count from l0f05', align=Align.INLINE)
d.comment(0xA01F, 'Y=9: position offset in FS options', align=Align.INLINE)
d.comment(0xA021, 'Add to current position', align=Align.INLINE)
d.comment(0xA023, 'Store updated position', align=Align.INLINE)
d.comment(0xA025, 'Load TXCB end byte', align=Align.INLINE)
d.comment(0xA027, 'Subtract 7 (header overhead)', align=Align.INLINE)
d.comment(0xA029, 'Store remaining data size', align=Align.INLINE)
d.comment(0xA02C, 'Store in fs_load_addr_2 (byte count)', align=Align.INLINE)
d.comment(0xA02E, 'Zero bytes: skip write', align=Align.INLINE)
d.comment(0xA030, 'Write data block to host/tube', align=Align.INLINE)
d.comment(0xA033, 'X=2: clear 3 bytes (indices 0-2)', align=Align.INLINE)
d.comment(0xA035, 'Clear l0f07+X', align=Align.INLINE)
d.comment(0xA038, 'Decrement index', align=Align.INLINE)
d.comment(0xA039, 'Loop until all cleared', align=Align.INLINE)
d.comment(0xA03B, 'Update addresses from offset 1', align=Align.INLINE)
d.comment(0xA03E, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0xA03F, 'Decrement fs_load_addr_2', align=Align.INLINE)
d.comment(0xA041, 'Load data count from l0f05', align=Align.INLINE)
d.comment(0xA044, 'Copy to l0f06', align=Align.INLINE)
d.comment(0xA047, 'Adjust FS options by 4 bytes (subtract)', align=Align.INLINE)
d.comment(0xA04A, 'X=3: check 4 bytes', align=Align.INLINE)
d.comment(0xA04C, 'Y=5: starting offset', align=Align.INLINE)
d.comment(0xA04E, 'Set carry for comparison', align=Align.INLINE)
d.comment(0xA04F, 'Load FS options byte', align=Align.INLINE)
d.comment(0xA051, 'Non-zero: more data remaining', align=Align.INLINE)
d.comment(0xA053, 'Advance to next byte', align=Align.INLINE)
d.comment(0xA054, 'Decrement counter', align=Align.INLINE)
d.comment(0xA055, 'Loop until all bytes checked', align=Align.INLINE)
d.comment(0xA057, 'All zero: clear carry (transfer complete)', align=Align.INLINE)
d.comment(0xA058, 'Jump to update catalogue and return', align=Align.INLINE)
d.comment(0xA05B, 'A=&C3: tube claim protocol', align=Align.INLINE)
d.comment(0xA05D, 'Dispatch tube address/data claim', align=Align.INLINE)
d.comment(0xA060, 'Carry clear: claim failed, retry', align=Align.INLINE)
d.comment(0xA062, 'Return (tube claimed)', align=Align.INLINE)
d.comment(0xBE90, """Resume normal ROM address space

The preceding 512 bytes are the source data for
two relocated code blocks (see move() calls):
  page 5 source -> &0500-&05FF (Tube host code)
  page 6 source -> &0600-&06FF (Econet handlers)
py8dis assembles those blocks at their runtime
addresses (&0500/&0600) via org directives. This
org restores the origin to the actual ROM address
for the remaining non-relocated code.""")
d.comment(0xBE90, 'Store BRK vector high byte', align=Align.INLINE)
d.comment(0xBE93, 'A=&8E: Tube control register value', align=Align.INLINE)
d.comment(0xBE95, 'Write Tube control register', align=Align.INLINE)
d.comment(0xBE98, 'Y=0: copy 256 bytes per page', align=Align.INLINE)
d.comment(0xBE9A, 'Load page 4 source byte', align=Align.INLINE)
d.comment(0xBE9D, 'Store to page 4 destination', align=Align.INLINE)
d.comment(0xBEA0, 'Load page 5 source byte', align=Align.INLINE)
d.comment(0xBEA3, 'Store to page 5 destination', align=Align.INLINE)
d.comment(0xBEA6, 'Load page 6 source byte', align=Align.INLINE)
d.comment(0xBEA9, 'Store to page 6 destination', align=Align.INLINE)
d.comment(0xBEAC, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xBEAD, 'Non-zero: continue copying', align=Align.INLINE)
d.comment(0xBEAF, 'Clear tube claim state', align=Align.INLINE)
d.comment(0xBEB2, 'X=&41: copy 66 bytes of ZP workspace', align=Align.INLINE)
d.comment(0xBEB4, 'Load ZP source byte from ROM', align=Align.INLINE)
d.comment(0xBEB7, 'Store to NMI workspace at &16+X', align=Align.INLINE)
d.comment(0xBEB9, 'Decrement byte counter', align=Align.INLINE)
d.comment(0xBEBA, 'More bytes: continue copying', align=Align.INLINE)
d.comment(0xBEBC, 'A=0: return success', align=Align.INLINE)
d.comment(0xBEBE, 'Return to caller', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'anfs-4.08.53.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'anfs-4.08.53.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
