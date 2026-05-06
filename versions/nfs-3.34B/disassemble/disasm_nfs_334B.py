import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'nfs-3.34B.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='6502', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.add_move(0x0016, 0x9308, 0x61)
d.add_move(0x0400, 0x934D, 0x100)
d.add_move(0x0500, 0x944D, 0x100)
d.add_move(0x0600, 0x954D, 0x100)
d.use_environment('acorn_mos')
d.use_environment('acorn_model_b_hardware')
d.use_environment('acorn_sideways_rom')
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
d.hook_subroutine(0x853C, 'print_inline', stringhi_hook)
d.constant(20, 'osbyte_explode_chars')
d.constant(120, 'osbyte_write_keys_pressed')
d.constant(143, 'osbyte_issue_service_request')
d.constant(168, 'osbyte_read_rom_ptr_table_low')

d.label(0x97, 'escapable')

d.label(0x98, 'need_release_tube')

d.label(0x9A, 'net_tx_ptr')

d.label(0x9B, 'net_tx_ptr_hi')

d.label(0x9C, 'net_rx_ptr')

d.label(0x9D, 'net_rx_ptr_hi')

d.label(0x9E, 'nfs_workspace')

d.label(0x9F, 'nfs_workspace_hi')

d.label(0xA0, 'nmi_tx_block')

d.label(0xA1, 'nmi_tx_block_hi')

d.label(0xA2, 'port_buf_len')

d.label(0xA3, 'port_buf_len_hi')

d.label(0xA4, 'open_port_buf')

d.label(0xA5, 'open_port_buf_hi')

d.label(0xA6, 'port_ws_offset')

d.label(0xA7, 'rx_buf_offset')

d.label(0xB0, 'fs_load_addr')

d.label(0xB1, 'fs_load_addr_hi')

d.label(0xB2, 'fs_load_addr_2')

d.label(0xB8, 'fs_error_ptr')

d.label(0xBB, 'fs_options')

d.label(0xBC, 'fs_block_offset')

d.label(0xBD, 'fs_last_byte_flag')

d.label(0xBE, 'fs_crc_lo')

d.label(0xBF, 'fs_crc_hi')

d.label(0xCD, 'nfs_temp')

d.label(0xCE, 'rom_svc_num')

d.label(0x10, 'zp_temp_10')

d.label(0x11, 'zp_temp_11')

d.label(0x16, 'nmi_workspace_start')

d.label(0x63, 'zp_63')

d.label(0x0D0C, 'nmi_jmp_lo')

d.label(0x0D0D, 'nmi_jmp_hi')

d.label(0x0D0E, 'set_nmi_vector')

d.label(0x0D14, 'nmi_rti')

d.label(0x0D1A, 'nmi_shim_1a')

d.label(0x0D20, 'tx_dst_stn')

d.label(0x0D21, 'tx_dst_net')

d.label(0x0D22, 'tx_src_stn')

d.label(0x0D23, 'tx_src_net')

d.label(0x0D24, 'tx_ctrl_byte')

d.label(0x0D25, 'tx_port')

d.label(0x0D26, 'tx_data_start')

d.label(0x0D2A, 'tx_data_len')

d.label(0x0D3A, 'tx_ctrl_status')

d.label(0x0D3D, 'rx_src_stn')

d.label(0x0D3E, 'rx_src_net')

d.label(0x0D3F, 'rx_ctrl')

d.label(0x0D40, 'rx_port')

d.label(0x0D41, 'rx_remote_addr')

d.label(0x0D4A, 'tx_flags')

d.label(0x0D4B, 'nmi_next_lo')

d.label(0x0D4C, 'nmi_next_hi')

d.label(0x0D4F, 'tx_index')

d.label(0x0D50, 'tx_length')

d.label(0x0D51, 'tx_work_51')

d.label(0x0D57, 'tx_work_57')

d.label(0x0D07, 'nmi_shim_07')

d.label(0x0D38, 'rx_status_flags')

d.label(0x0D3B, 'rx_ctrl_copy')

d.label(0x0D52, 'tx_in_progress')

d.label(0x0D5C, 'scout_status')

d.label(0x0D5D, 'rx_extra_byte')

d.label(0x0D61, 'printer_buf_ptr')

d.label(0x0D62, 'tx_clear_flag')

d.label(0x0D63, 'prot_status')

d.label(0x0D64, 'rx_flags')

d.label(0x0D65, 'saved_jsr_mask')

d.label(0x0D66, 'econet_init_flag')

d.label(0x0D67, 'tube_flag')

d.label(0x0E00, 'fs_server_stn')

d.label(0x0E01, 'fs_server_net')

d.label(0x0E02, 'fs_urd_handle')

d.label(0x0E03, 'fs_csd_handle')

d.label(0x0E04, 'fs_lib_handle')

d.label(0x0E05, 'fs_boot_option')

d.label(0x0E06, 'fs_messages_flag')

d.label(0x0E07, 'fs_eof_flags')

d.label(0x0E08, 'fs_sequence_nos')

d.label(0x0E09, 'fs_last_error')

d.label(0x0E0A, 'fs_cmd_context')

d.label(0x0E0D, 'fs_reply_status')

d.label(0x0E0E, 'fs_target_stn')

d.label(0x0E10, 'fs_cmd_ptr')

d.label(0x0029, 'tube_brk_send_loop')

d.label(0x0032, 'tube_reset_stack')

d.label(0x003A, 'tube_main_loop')

d.label(0x003F, 'tube_handle_wrch')

d.label(0x0045, 'tube_poll_r2')

d.label(0x0054, 'tube_dispatch_cmd')

d.label(0x0057, 'tube_transfer_addr')
d.entry(0x0016)
d.entry(0x0032)
d.entry(0x003A)

d.label(0x0403, 'tube_escape_entry')

d.label(0x0406, 'tube_addr_claim')

d.label(0x0414, 'tube_post_init')

d.label(0x0425, 'return_tube_init')

d.label(0x0472, 'return_tube_xfer')

d.label(0x04E0, 'tube_setup_transfer')

d.label(0x04E7, 'tube_rdch_handler')

d.label(0x04EF, 'tube_restore_regs')

d.label(0x04F7, 'tube_read_r2')
d.entry(0x0400)
d.entry(0x0403)
d.entry(0x0406)
d.entry(0x0414)
d.entry(0x04E0)
d.entry(0x04E7)
d.entry(0x04EF)
d.entry(0x04F7)

d.label(0x051C, 'tube_wrch_handler')

d.label(0x051F, 'tube_send_and_poll')

d.label(0x0527, 'tube_poll_r4_wrch')

d.label(0x0532, 'tube_resume_poll')

d.label(0x053D, 'tube_release_return')

d.label(0x0543, 'tube_osbput')

d.label(0x0550, 'tube_osbget')

d.label(0x055B, 'tube_osrdch')

d.label(0x0561, 'tube_rdch_reply')

d.label(0x0569, 'tube_osfind')

d.label(0x0580, 'tube_osfind_close')

d.label(0x058C, 'tube_osargs')

d.label(0x0590, 'tube_read_params')

d.label(0x05B1, 'tube_read_string')

d.label(0x05C5, 'tube_oscli')

d.label(0x05CB, 'tube_reply_ack')

d.label(0x05CD, 'tube_reply_byte')

d.label(0x05D8, 'tube_osfile')
d.entry(0x051C)
for addr in [0x055B, 0x05C5, 0x0626, 0x063B, 0x065D, 0x06A3, 0x04EF, 0x053D, 0x058C, 0x0550, 0x0543, 0x0569, 0x05D8, 0x0602]:
    d.entry(addr)
_tube_r2_entries = [(0x0500, 'tube_osrdch', 'cmd 0: OSRDCH'), (0x0502, 'tube_oscli', 'cmd 1: OSCLI'), (0x0504, 'tube_osbyte_short', 'cmd 2: OSBYTE (2-param)'), (0x0506, 'tube_osbyte_long', 'cmd 3: OSBYTE (3-param)'), (0x0508, 'tube_osword', 'cmd 4: OSWORD'), (0x050A, 'tube_osword_rdln', 'cmd 5: OSWORD 0 (read line)'), (0x050C, 'tube_restore_regs', 'cmd 6: release/restore regs'), (0x050E, 'tube_release_return', 'cmd 7: restore regs, RTS'), (0x0510, 'tube_osargs', 'cmd 8: OSARGS'), (0x0512, 'tube_osbget', 'cmd 9: OSBGET'), (0x0514, 'tube_osbput', 'cmd 10: OSBPUT'), (0x0516, 'tube_osfind', 'cmd 11: OSFIND'), (0x0518, 'tube_osfile', 'cmd 12: OSFILE'), (0x051A, 'tube_osgbpb', 'cmd 13: OSGBPB')]
for addr, target_label, desc in _tube_r2_entries:
    d.word(addr)
    d.expr(addr, target_label)
    d.comment(addr, desc, align=Align.INLINE)

d.label(0x0602, 'tube_osgbpb')

d.label(0x0626, 'tube_osbyte_short')

d.label(0x0630, 'tube_osbyte_send_x')

d.label(0x063B, 'tube_osbyte_long')

d.label(0x0653, 'tube_osbyte_send_y')

d.label(0x065D, 'tube_osword')

d.label(0x0661, 'tube_osword_read')

d.label(0x066C, 'tube_osword_read_lp')

d.label(0x0692, 'tube_osword_write')

d.label(0x0695, 'tube_osword_write_lp')

d.label(0x06A0, 'tube_return_main')

d.label(0x06A3, 'tube_osword_rdln')

d.label(0x06BB, 'tube_rdln_send_line')

d.label(0x06C2, 'tube_rdln_send_loop')

d.label(0x06C5, 'tube_rdln_send_byte')

d.label(0x06E2, 'tube_escape_check')

d.label(0x06E8, 'tube_event_handler')

d.label(0x06F7, 'tube_send_r1')
d.entry(0x0600)
d.entry(0x0602)
d.entry(0x0626)
d.entry(0x063B)
d.entry(0x065D)
d.entry(0x06A3)
d.entry(0x06E2)
d.entry(0x06E8)
d.entry(0x06F7)

d.label(0x0DEB, 'fs_state_deb')
d.comment(0x800D, """The 'ROFF' suffix at copyright_string+3 is reused by
the *ROFF command matcher (svc_4_star_command) — a
space-saving trick that shares ROM bytes between the
copyright string and the star command table.""")

d.label(0x800D, 'copyright_string')

d.label(0x8014, 'error_offsets')
d.comment(0x8014, """Error message offset table (9 entries).
Each byte is a Y offset into error_msg_table.
Entry 0 (Y=0, "Line Jammed") doubles as the
copyright string null terminator.
Indexed by TXCB status (AND #7), or hardcoded 8.""")
d.comment(0x8014, '"Line Jammed"', align=Align.INLINE)
for addr in range(0x8015, 0x801D):
    d.byte(addr)
d.comment(0x8015, '"Net Error"', align=Align.INLINE)
d.comment(0x8016, '"Not listening"', align=Align.INLINE)
d.comment(0x8017, '"No Clock"', align=Align.INLINE)
d.comment(0x8018, '"Bad Txcb"', align=Align.INLINE)
d.comment(0x8019, '"Escape"', align=Align.INLINE)
d.comment(0x801A, '"Escape"', align=Align.INLINE)
d.comment(0x801B, '"Bad Option"', align=Align.INLINE)
d.comment(0x801C, '"No reply"', align=Align.INLINE)
d.comment(0x801D, 'Four bytes with unknown purpose.')
for addr in range(0x801D, 0x8021):
    d.byte(addr)
d.comment(0x801D, 'Purpose unknown', align=Align.INLINE)
d.comment(0x801E, 'Purpose unknown', align=Align.INLINE)
d.comment(0x801F, 'Purpose unknown', align=Align.INLINE)
d.comment(0x8020, 'Purpose unknown', align=Align.INLINE)

d.label(0x8021, 'dispatch_0_lo')

d.label(0x8045, 'dispatch_0_hi')
d.expr_label(0x8020, 'dispatch_0_lo-1')
d.expr_label(0x8044, 'dispatch_0_hi-1')

d.label(0x8E19, 'fs_osword_tbl_lo')

d.label(0x8E1E, 'fs_osword_tbl_hi')

d.label(0x8E6B, 'read_args_size')

d.label(0x8F69, 'store_16bit_at_y')

d.label(0x9021, 'osword_trampoline')

d.label(0x902C, 'osword_tbl_lo')

d.label(0x9035, 'osword_tbl_hi')

d.label(0x90BE, 'return_match_osbyte')

d.label(0x90FC, 'return_remote_cmd')

d.label(0x9167, 'ctrl_block_setup_clv')

d.label(0x92D7, 'clear_jsr_protection')

d.label(0x92EF, 'read_vdu_osbyte_x0')

d.label(0x92F1, 'read_vdu_osbyte')

d.label(0x06D0, 'tube_send_r2')

d.label(0x06D9, 'tube_send_r4')

d.label(0x80AE, 'return_1')

d.label(0x8145, 'return_2')

d.label(0x8276, 'return_3')

d.label(0x9660, 'trampoline_tx_setup')

d.label(0x9663, 'trampoline_adlc_init')

d.label(0x9666, 'svc_12_nmi_release')

d.label(0x9669, 'svc_11_nmi_claim')

d.label(0x966C, 'svc_5_unknown_irq')
d.entry(0x9660)
d.entry(0x9663)

d.label(0x824E, 'fs_vector_addrs')

d.label(0x8486, 'bgetv_handler')

d.label(0x83A3, 'bputv_handler')
d.entry(0x8486)
d.entry(0x83A3)

d.label(0x81AC, 'cmd_name_matched')

d.label(0x81B3, 'skip_cmd_spaces')

d.label(0x82E6, 'store_rom_ptr_pair')

d.label(0x830F, 'init_tx_ctrl_data')

d.label(0x8311, 'init_tx_ctrl_port')

d.label(0x8341, 'prepare_cmd_with_flag')

d.label(0x8347, 'prepare_cmd_clv')

d.label(0x8352, 'prepare_fs_cmd_v')

d.label(0x8381, 'send_fs_reply_cmd')

d.label(0x83CC, 'store_retry_count')

d.label(0x841C, 'update_sequence_return')

d.label(0x842D, 'set_listen_offset')

d.label(0x8449, 'send_to_fs_star')

d.label(0x8471, 'fs_wait_cleanup')

d.label(0x84A4, 'return_bget')

d.label(0x84A5, 'add_5_to_y')

d.label(0x84A6, 'add_4_to_y')

d.label(0x84AB, 'sub_4_from_y')

d.label(0x84AC, 'sub_3_from_y')

d.label(0x815C, 'clear_osbyte_ce_cf')

d.label(0x0F00, 'fs_cmd_type')

d.label(0x0F01, 'fs_cmd_y_param')

d.label(0x0F02, 'fs_cmd_urd')

d.label(0x0F03, 'fs_cmd_csd')

d.label(0x0F04, 'fs_cmd_lib')

d.label(0x0F05, 'fs_cmd_data')

d.label(0x0FDC, 'fs_putb_buf')

d.label(0x0FDD, 'fs_getb_buf')

d.label(0x8531, 'access_bit_table')

d.label(0x85F7, 'print_hex_nibble')

d.label(0x85DA, 'return_compare')

d.label(0x85DB, 'fscv_7_read_handles')

d.label(0x85DF, 'return_fscv_handles')

d.label(0x8618, 'pad_filename_spaces')

d.label(0x862B, 'print_exec_and_len')

d.label(0x8636, 'print_hex_bytes')

d.label(0x8641, 'print_space')

d.label(0x864F, 'tx_poll_timeout')

d.label(0x8685, 'delay_1ms')

d.label(0x886F, 'get_file_protection')

d.label(0x8884, 'copy_filename_to_cmd')

d.label(0x88C6, 'copy_fs_reply_to_cb')

d.label(0x8913, 'save_args_handle')

d.label(0x8990, 'close_single_handle')

d.label(0x89CB, 'adjust_addrs_9')

d.label(0x89D0, 'adjust_addrs_1')

d.label(0x89D2, 'adjust_addrs_clc')

d.label(0x8AFC, 'copy_reply_to_caller')

d.label(0x8B8B, 'tube_claim_loop')

d.label(0x8D52, 'print_reply_counted')

d.label(0x8D68, 'copy_string_from_offset')

d.label(0x8D73, 'return_copy_string')

d.label(0x8D76, 'print_dir_from_offset')

d.label(0x9723, 'scout_reject')

d.label(0x9744, 'scout_discard')

d.label(0x974C, 'scout_loop_rda')

d.label(0x975C, 'scout_loop_second')

d.label(0x9797, 'scout_no_match')

d.label(0x979A, 'scout_match_port')

d.label(0x982D, 'data_rx_setup')

d.label(0x984F, 'nmi_data_rx_net')

d.label(0x9865, 'nmi_data_rx_skip')

d.label(0x988A, 'rx_error')

d.label(0x9894, 'rx_error_reset')

d.label(0x98F7, 'nmi_data_rx_tube')

d.label(0x9933, 'data_rx_tube_complete')

d.label(0x9930, 'data_rx_tube_error')

d.label(0x9966, 'ack_tx_configure')

d.label(0x9974, 'ack_tx_write_dest')

d.label(0x9C84, 'tx_active_start')

d.label(0x9D72, 'tx_error')

d.label(0x9DDE, 'reply_error')

d.label(0x9E3B, 'data_tx_begin')

d.label(0x9E7D, 'data_tx_last')

d.label(0x9E8E, 'data_tx_error')

d.label(0x9E9B, 'install_saved_handler')

d.label(0x9EA4, 'nmi_data_tx_tube')

d.label(0x9EFF, 'nmi_final_ack_net')

d.label(0x9FCA, 'nmi_shim_rom_src')

d.label(0x9FEB, 'rom_nmi_tail')

d.label(0x04AE, 'begink')

d.label(0x04BA, 'beginr')

d.label(0x05B5, 'strnh')

d.label(0x05D5, 'mj')

d.label(0x05DA, 'argsw')

d.label(0x0638, 'bytex')

d.label(0x80F9, 'cloop')

d.label(0x818F, 'initl')

d.label(0x81B2, 'skpspi')

d.label(0x821A, 'dofsl1')

d.label(0x8300, 'fsdiel')

d.label(0x8320, 'fstxl1')

d.label(0x8330, 'fstxl2')

d.label(0x838B, 'dofsl7')

d.label(0x8397, 'return_dofsl7')

d.label(0x8398, 'dofsl5')

d.label(0x83DE, 'error1')

d.label(0x8429, 'nlistn')

d.label(0x842B, 'nlisne')

d.label(0x845B, 'incpx')

d.label(0x8593, 'y2fsl5')

d.label(0x8599, 'y2fsl2')

d.label(0x85A8, 'fs2al1')

d.label(0x8638, 'num01')

d.label(0x866B, 'poll_txcb_status')

d.label(0x869A, 'file1')

d.label(0x86A9, 'quote1')

d.label(0x86CC, 'loadop')

d.label(0x86E9, 'lodfil')

d.label(0x870C, 'floop')

d.label(0x8736, 'lodchk')

d.label(0x8741, 'return_lodchk')

d.label(0x8742, 'saveop')

d.label(0x874B, 'savsiz')

d.label(0x87B0, 'lodrl1')

d.label(0x87BE, 'lodrl2')

d.label(0x87EC, 'savchk')

d.label(0x8862, 'chalp1')

d.label(0x8879, 'chalp2')

d.label(0x888B, 'cha6')

d.label(0x889A, 'cha4')

d.label(0x88A4, 'cha5')

d.label(0x88D3, 'cha5lp')

d.label(0x893E, 'osarg1')

d.label(0x89B7, 'opter1')

d.label(0x89BC, 'optl1')

d.label(0x89E4, 'gbpbx')

d.label(0x89F6, 'gbpbx0')

d.label(0x89F9, 'gbpbx1')

d.label(0x8A04, 'gbpbe1')

d.label(0x8A10, 'gbpbf1')

d.label(0x8A1B, 'gbpbf2')

d.label(0x8A24, 'gbpbl1')

d.label(0x8A46, 'gbpbl3')

d.label(0x8A5D, 'gbpbf3')

d.label(0x8ABE, 'info2')

d.label(0x8B23, 'tbcop1')

d.label(0x8B9A, 'decfir')

d.label(0x8B9C, 'decmor')

d.label(0x8BA8, 'decmin')

d.label(0x8D25, 'logon2')

d.label(0x8D2B, 'logon3')

d.label(0x8D7F, 'infol2')

d.label(0x8DD7, 'rxpol2')

d.label(0x8E0D, 'save1')

d.label(0x8E2F, 'copyl3')

d.label(0x8E76, 'readry')

d.label(0x8E9C, 'rssl1')

d.label(0x8EA7, 'rssl2')

d.label(0x8EB8, 'rsl1')

d.label(0x8EE4, 'readc1')

d.label(0x8F02, 'scan0')

d.label(0x8F16, 'scan1')

d.label(0x8F32, 'openl6')

d.label(0x8F3F, 'openl7')

d.label(0x8F44, 'openl4')

d.label(0x8F4F, 'rest1')

d.label(0x8F79, 'dofs01')

d.label(0x8FF6, 'dofs2')

d.label(0x901A, 'entry1')

d.label(0x9086, 'nbyte6')

d.label(0x9088, 'nbyte1')

d.label(0x90AA, 'nbyte4')

d.label(0x90AE, 'nbyte5')

d.label(0x90B5, 'return_nbyte')

d.label(0x9103, 'rchex')

d.label(0x9106, 'remot1')

d.label(0x9168, 'cbset2')

d.label(0x917F, 'cbset3')

d.label(0x9185, 'cbset4')

d.label(0x91C4, 'setup1')

d.label(0x91C7, 'return_printer_select')

d.label(0x91D7, 'prlp1')

d.label(0x9255, 'bsxl1')

d.label(0x9272, 'bspsx')

d.label(0x927A, 'bsxl0')

d.label(0x9291, 'return_bspsx')
d.comment(0x8000, """NFS ROM 3.34B disassembly (Acorn Econet filing system)
=====================================================""")
d.comment(0x8000, 'JMP language_handler', align=Align.INLINE)
d.comment(0x8003, 'JMP service_handler', align=Align.INLINE)
for i in range(1, 14):
    d.rts_code_ptr(0x8020 + i, 0x8044 + i)
for i in range(14, 19):
    d.rts_code_ptr(0x8020 + i, 0x8044 + i)
for i in range(19, 27):
    d.rts_code_ptr(0x8020 + i, 0x8044 + i)
for i in range(27, 33):
    d.rts_code_ptr(0x8020 + i, 0x8044 + i)
for i in range(33, 37):
    d.rts_code_ptr(0x8020 + i, 0x8044 + i)
for i in range(5):
    d.rts_code_ptr(0x8E19 + i, 0x8E1E + i)
d.entry(0x96F0)
d.entry(0x96F6)
d.entry(0x9C48)
d.entry(0x9D4C)
d.entry(0x9D72)
d.entry(0x9D88)
d.entry(0x9D94)
d.entry(0x9DB2)
d.entry(0x9DC8)
d.entry(0x9DE3)
d.entry(0x9EDD)
d.entry(0x9EE9)
d.entry(0x9EFF)
d.entry(0x9F39)
d.entry(0x9F3F)
d.entry(0x9F15)
d.entry(0x9715)
d.entry(0x9747)
d.entry(0x9839)
d.entry(0x984F)
d.entry(0x9865)
d.entry(0x989A)
d.entry(0x98F7)
d.entry(0x9992)
d.entry(0x9FCB)
d.entry(0x9FD9)
d.entry(0x9FEB)
d.entry(0x9E2B)
d.entry(0x9E50)
d.entry(0x9EA4)
d.entry(0x81D1)
d.entry(0x81E1)
d.entry(0x81FF)
d.entry(0x8201)
d.entry(0x84A5)
d.entry(0x84AB)
d.entry(0x87C9)
d.entry(0x8845)
d.entry(0x8934)
d.entry(0x89EB)
d.entry(0x9064)
d.entry(0x99BB)
d.entry(0x8F73)
d.entry(0x9021)
for i in range(9):
    d.rts_code_ptr(0x902C + i, 0x9035 + i)
for y in range(0x81, 0x89):
    d.rts_code_ptr(0x9A0E + y, 0x9A16 + y)
for y in range(0x83, 0x88):
    d.rts_code_ptr(0x9B0E + y, 0x9B13 + y)
for y in range(0x81, 0x89):
    d.rts_code_ptr(0x9C53 + y, 0x9C5B + y)


d.label(0x9A9F, 'rx_imm_exec')
d.subroutine(0x9A9F, 'rx_imm_exec', title='RX immediate: JSR/UserProc/OSProc setup', description="""Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace, then jumps to the common
receive path. Used for operation types &83-&85.""")


d.label(0x9ABD, 'rx_imm_poke')
d.subroutine(0x9ABD, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data, then
jumps to the common data-receive path.""")


d.label(0x9AC8, 'rx_imm_machine_type')
d.subroutine(0x9AC8, 'rx_imm_machine_type', title='RX immediate: machine type query', description="""Sets up a buffer in high memory (length #&01FC) for the
machine type query response. Returns system identification
data to the remote station.""")


d.label(0x9ADB, 'rx_imm_peek')
d.subroutine(0x9ADB, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Saves the current TX block pointer, replaces it with a
pointer to the workspace, and prepares to send the PEEK
response data back to the requesting station.""")


d.label(0x9B9B, 'tx_done_jsr')
d.subroutine(0x9B9B, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes a return address on the stack (pointing to
tx_done_exit), then does JMP indirect to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")


d.label(0x9BA4, 'tx_done_user_proc')
d.subroutine(0x9BA4, 'tx_done_user_proc', title='TX done: UserProc event', description="""Generates a network event (event 8) via OSEVEN with the
remote address. This notifies the user program that a
UserProc operation has completed.""")


d.label(0x9BB2, 'tx_done_os_proc')
d.subroutine(0x9BB2, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM entry point at &8000 (rom_header) with
X/Y from the remote address workspace. This invokes an
OS-level procedure on behalf of the remote station.""")


d.label(0x9BBE, 'tx_done_halt')
d.subroutine(0x9BBE, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of rx_flags, enables interrupts, and spin-waits
until bit 2 is cleared (by a CONTINUE from the remote
station). If bit 2 is already set, skips to exit.""")


d.label(0x9BD5, 'tx_done_continue')
d.subroutine(0x9BD5, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of rx_flags, releasing any station that is
halted and spinning in tx_done_halt.""")

d.label(0x9BDD, 'tx_done_exit')


d.label(0x9CE8, 'tx_ctrl_peek')
d.subroutine(0x9CE8, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace (with carry propagation). Calls tx_calc_transfer
to finalise, then exits via tx_ctrl_exit.""")


d.label(0x9CEC, 'tx_ctrl_poke')
d.subroutine(0x9CEC, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")


d.label(0x9D0B, 'tx_ctrl_proc')
d.subroutine(0x9D0B, 'tx_ctrl_proc', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

d.label(0x9D45, 'tx_ctrl_exit')
d.entry(0x915A)
d.entry(0x91B6)
d.entry(0x91C8)
d.entry(0x90CE)
d.entry(0x8742)
d.entry(0x8E7C)
d.entry(0x8F58)
d.entry(0x8D5D)
d.entry(0x8BF3)
d.entry(0x8D07)
d.entry(0x982D)


d.subroutine(0x8509, 'save_fscv_args', title='Save FSCV/vector arguments', description="""Stores A, X, Y into the filing system workspace. Called at the
start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
  &BD (fs_last_byte_flag) = A (function code / command)
  &BB (fs_options)        = X (control block ptr low)
  &BC (fs_block_offset)   = Y (control block ptr high)
  &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)""", on_entry={'a': 'function code', 'x': 'control block pointer low', 'y': 'control block pointer high'})


d.subroutine(0x8514, 'decode_attribs_6bit', title='Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)', description="""Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&8531. The two formats use different bit layouts for file
protection attributes.""")


d.subroutine(0x851E, 'decode_attribs_5bit', title='Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)', description="""Masks A to 5 bits and builds an access bitmask via the
lookup table at &8531. Each input bit position maps to a
different output bit via the table. The conversion is done
by iterating through the source bits and OR-ing in the
corresponding destination bits from the table, translating
between BBC (8-bit) and fileserver (5-bit) protection formats.""", on_entry={'a': 'BBC attribute byte (bits 0-4 used)'}, on_exit={'a': 'FS attribute bitmask (5-bit)', 'x': 'corrupted'})


d.subroutine(0x8556, 'skip_spaces', title='Skip leading spaces in parameter block', description="""Advances Y past space characters in (fs_options),Y.
Returns with the first non-space character in A.
Sets carry if the character is >= 'A' (alphabetic).""")


d.subroutine(0x8561, 'parse_decimal', title='Parse decimal number from (fs_options),Y (DECIN)', description="""Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
then ADC &B2 gives x10.
Terminates on "." (pathname separator), control chars, or space.
The delimiter handling was revised to support dot-separated path
components (e.g. "1.$.PROG",
    on_entry={"y": "offset into (fs_options) buffer"},
    on_exit={"a": "parsed value (accumulated in &B2)", "x": "initial A value (saved by TAX)", "y": "offset past last digit parsed"})
>= &40 (any letter), but the revision allows numbers followed
by dots.""", on_entry={'y': 'offset into (fs_options) buffer'}, on_exit={'a': 'parsed value (accumulated in &B2)', 'x': 'initial A value (saved by TAX)', 'y': 'offset past last digit parsed'})
d.comment(0x8561, 'Save A in X for caller', align=Align.INLINE)
d.comment(0x8562, 'Zero accumulator', align=Align.INLINE)
d.comment(0x8566, 'Load next char from buffer', align=Align.INLINE)
d.comment(0x8568, 'Letter or above?', align=Align.INLINE)
d.comment(0x856A, 'Yes: not a digit, done', align=Align.INLINE)
d.comment(0x856C, 'Dot separator?', align=Align.INLINE)
d.comment(0x856E, 'Yes: exit with C=1 (dot found)', align=Align.INLINE)
d.comment(0x8570, 'Control char or space: done', align=Align.INLINE)
d.comment(0x8572, 'Mask ASCII digit to 0-9', align=Align.INLINE)
d.comment(0x8574, 'Save new digit', align=Align.INLINE)
d.comment(0x8576, 'Running total * 2', align=Align.INLINE)
d.comment(0x8578, 'A = running total * 2', align=Align.INLINE)
d.comment(0x857A, 'A = running total * 4', align=Align.INLINE)
d.comment(0x857B, 'A = running total * 8', align=Align.INLINE)
d.comment(0x857C, '+ total*2 = total * 10', align=Align.INLINE)
d.comment(0x857E, '+ digit = total*10 + digit', align=Align.INLINE)
d.comment(0x8580, 'Store new running total', align=Align.INLINE)
d.comment(0x8582, 'Advance to next char', align=Align.INLINE)
d.comment(0x8583, "Loop (always: Y won't wrap to 0)", align=Align.INLINE)
d.comment(0x8585, 'No dot found: C=0', align=Align.INLINE)
d.comment(0x8586, 'Return result in A', align=Align.INLINE)


d.subroutine(0x8589, 'handle_to_mask_a', title='Convert handle in A to bitmask', description="""Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""", on_entry={'a': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})


d.subroutine(0x858A, 'handle_to_mask_clc', title='Convert handle to bitmask (carry cleared)', description="""Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""", on_entry={'y': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})


d.subroutine(0x858B, 'handle_to_mask', title='Convert file handle to bitmask (Y2FS)', description="""Converts fileserver handles to single-bit masks segregated inside
the BBC. NFS handles occupy the &20-&27 range (base HAND=&20),
which cannot collide with local filing system or cassette handles
-- the MOS routes OSFIND/OSBGET/OSBPUT to the correct filing
system based on the handle value alone. The power-of-two encoding
allows the EOF hint byte to track up to 8 files simultaneously
with one bit per file, and enables fast set operations (ORA to
add, EOR to toggle, AND to test) without loops. Handle 0 passes
through unchanged (means "no file",
    on_entry={"y": "handle number", "c": "0: convert, 1 with Y=0: skip, 1 with Y!=0: convert"},
    on_exit={"a": "preserved", "x": "preserved", "y": "bitmask (single bit set) or &FF if handle invalid"})
has a built-in validity check: if the handle is out of range, the
repeated ASL shifts all bits out, leaving A=0, which is converted
to Y=&FF as a sentinel -- bad handles fail gracefully rather than
indexing into garbage.
Callers needing to move the handle from A use handle_to_mask_a;
callers needing carry cleared use handle_to_mask_clc.""", on_entry={'y': 'handle number', 'c': '0: convert, 1 with Y=0: skip, 1 with Y!=0: convert'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if handle invalid'})
d.comment(0x858B, 'Save A (will be restored on exit)', align=Align.INLINE)
d.comment(0x858C, 'Save X (will be restored on exit)', align=Align.INLINE)
d.comment(0x858D, '  (second half of X save)', align=Align.INLINE)
d.comment(0x858E, 'A = handle from Y', align=Align.INLINE)
d.comment(0x858F, 'C=0: always convert', align=Align.INLINE)
d.comment(0x8591, 'C=1 and Y=0: skip (handle 0 = none)', align=Align.INLINE)
d.comment(0x8593, 'C=1 and Y!=0: convert', align=Align.INLINE)
d.comment(0x8594, 'A = handle - &1F (1-based bit position)', align=Align.INLINE)
d.comment(0x8596, 'X = shift count', align=Align.INLINE)
d.comment(0x8597, 'Start with bit 0 set', align=Align.INLINE)
d.comment(0x8599, 'Shift bit left', align=Align.INLINE)
d.comment(0x859A, 'Count down', align=Align.INLINE)
d.comment(0x859B, 'Loop until correct position', align=Align.INLINE)
d.comment(0x859D, 'Undo final extra shift', align=Align.INLINE)
d.comment(0x859E, 'Y = resulting bitmask', align=Align.INLINE)
d.comment(0x859F, 'Non-zero: valid mask, skip to exit', align=Align.INLINE)
d.comment(0x85A1, 'Zero: invalid handle, set Y=&FF', align=Align.INLINE)
d.comment(0x85A2, 'Restore X', align=Align.INLINE)
d.comment(0x85A4, 'Restore A', align=Align.INLINE)


d.subroutine(0x85A6, 'mask_to_handle', title='Convert bitmask to handle number (FS2A)', description="""Inverse of Y2FS. Converts from the power-of-two FS format
back to a sequential handle number by counting right shifts
until A=0. Adds &1E to convert the 1-based bit position to
a handle number (handles start at &1F+1 = &20). Used when
receiving handle values from the fileserver in reply packets.""", on_entry={'a': 'single-bit bitmask'}, on_exit={'a': 'handle number (&20-&27)', 'x': 'corrupted', 'y': 'preserved'})
d.comment(0x85A6, 'X = 0 (bit position counter)', align=Align.INLINE)
d.comment(0x85A8, 'Count this bit position', align=Align.INLINE)
d.comment(0x85A9, 'Shift mask right; C=0 when done', align=Align.INLINE)
d.comment(0x85AA, 'Loop until all bits shifted out', align=Align.INLINE)
d.comment(0x85AD, 'Add &1E+C(=0) = &1E; handle=&1F+pos', align=Align.INLINE)


d.subroutine(0x85B0, 'print_decimal', title='Print byte as 3-digit decimal number', description="""Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""", on_entry={'a': 'byte value to print'}, on_exit={'a': 'last digit character', 'x': 'corrupted', 'y': '0 (remainder after last division)'})


d.subroutine(0x85BD, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Divides Y by A using repeated subtraction. Prints the
quotient as an ASCII digit ('0'-'9'). Returns with the
remainder in Y. X starts at &2F ('0'-1) and increments
once per subtraction, giving the ASCII digit directly.""", on_entry={'a': 'divisor (stored to &B8)', 'y': 'dividend'}, on_exit={'y': 'remainder'})


d.subroutine(0x85CF, 'compare_addresses', title='Compare two 4-byte addresses', description="""Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
Used by the OSFILE save handler to compare the current
transfer address (&C8-&CB, copied to &B0) against the end
address (&B4-&B7) during multi-block file data transfers.""", on_exit={'a': 'corrupted (EOR result)', 'x': 'corrupted', 'y': 'preserved'})


d.subroutine(0x85E0, 'clear_fs_flag', title='Clear bit(s) in FS flags (&0E07)', description="""Inverts A (EOR #&FF), then ANDs into fs_work_0e07 to clear
the specified bits. Falls through to set_fs_flag to store.""", on_entry={'a': 'bitmask of bits to clear'}, on_exit={'a': 'updated fs_eof_flags value'})


d.subroutine(0x85E5, 'set_fs_flag', title='Set bit(s) in FS flags (&0E07)', description="""ORs A into fs_work_0e07 (EOF hint byte). Each bit represents
one of up to 8 open file handles. When clear, the file is
definitely NOT at EOF. When set, the fileserver must be queried
to confirm EOF status. This negative-cache optimisation avoids
expensive network round-trips for the common case. The hint is
cleared when the file pointer is updated (since seeking away
from EOF invalidates the hint) and set after BGET/OPEN/EOF
operations that might have reached the end.""", on_entry={'a': 'bitmask of bits to set'}, on_exit={'a': 'updated fs_eof_flags value'})


d.subroutine(0x8601, 'print_file_info', title='Print file catalogue line', description="""Displays a formatted catalogue entry: filename (padded to 12
chars with spaces), load address (4 hex bytes at offset 5-2),
exec address (4 hex bytes at offset 9-6), and file length
(3 hex bytes at offset &0C-&0A), followed by a newline.
Data is read from (fs_crc_lo) for the filename and from
(fs_options) for the numeric fields. Returns immediately
if fs_messages_flag is zero (no info available).""")


d.subroutine(0x85EC, 'print_hex', title='Print byte as two hex digits', description="""Prints the high nibble first (via 4× LSR), then the low
nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
and output via OSASCI.""", on_entry={'a': 'byte to print as two hex digits'}, on_exit={'a': 'preserved (original byte)', 'x': 'corrupted (by OSASCI)'})


d.subroutine(0x8645, 'setup_tx_ptr_c0', title='Set up TX pointer to control block at &00C0', description="""Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""")


d.subroutine(0x864D, 'tx_poll_ff', title='Transmit and poll for result (full retry)', description="""Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""")


d.subroutine(0x8651, 'tx_poll_core', title='Core transmit and poll routine (XMIT)', description="""Claims the TX semaphore (tx_ctrl_status) via ASL -- a busy-wait
spinlock where carry=0 means the semaphore is held by another
operation. Only after claiming the semaphore is the TX pointer
copied to nmi_tx_block, ensuring the low-level transmit code
sees a consistent pointer. Then calls the ADLC TX setup routine
and polls the control byte for completion:
  bit 7 set = still busy (loop)
  bit 6 set = error (check escape or report)
  bit 6 clear = success (clean return)
On error, checks for escape condition and handles retries.
Two entry points: setup_tx_ptr_c0 (&8645) always uses the
standard TXCB; tx_poll_core (&8651) is general-purpose.""", on_entry={'a': 'retry count (&FF = full retry)', 'y': 'timeout parameter (&60 = standard)'}, on_exit={'a': 'entry A (retry count, restored from stack)', 'x': '0', 'y': '0'})


d.subroutine(0x853C, 'print_inline', title='Print inline string, high-bit terminated (VSTRNG)', description="""Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. N.B. Cannot be used for
BRK error messages -- the stack manipulation means a BRK in the
inline data would corrupt the stack rather than invoke the error
handler.""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})
d.comment(0x853C, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x853F, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x8544, 'Advance pointer past return address / to next char', align=Align.INLINE)
d.comment(0x854A, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x854C, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x8553, 'Jump to address of high-bit byte (resumes code after string)', align=Align.INLINE)
d.comment(0x8021, """Dispatch table: low bytes of (handler_address - 1)
Each entry stores the low byte of a handler address minus 1,
for use with the PHA/PHA/RTS dispatch trick at &809F.
See dispatch_0_hi (&8045) for the corresponding high bytes.

Five callers share this table via different Y base offsets:
  Y=&00  Service calls 0-12       (indices 1-13)
  Y=&0D  Language entry reasons    (indices 14-18)
  Y=&12  FSCV codes 0-7           (indices 19-26)
  Y=&16  FS reply handlers        (indices 27-32)
  Y=&20  *NET1-4 sub-commands     (indices 33-36)""")
d.comment(0x8045, """Dispatch table: high bytes of (handler_address - 1)
Paired with dispatch_0_lo (&8021). Together they form a table
of 37 handler addresses, used via the PHA/PHA/RTS trick at
&809F.""")
dispatch_comments = ['Svc 0: already claimed (no-op)', 'Svc 1: absolute workspace', 'Svc 2: private workspace', 'Svc 3: auto-boot', 'Svc 4: unrecognised star command', 'Svc 5: unrecognised interrupt', 'Svc 6: BRK (no-op)', 'Svc 7: unrecognised OSBYTE', 'Svc 8: unrecognised OSWORD', 'Svc 9: *HELP', 'Svc 10: static workspace (no-op)', 'Svc 11: NMI release (reclaim NMIs)', 'Svc 12: NMI claim (save NMI state)', 'Lang 0: no language / Tube', 'Lang 1: normal startup', 'Lang 2: softkey byte (Electron)', 'Lang 3: softkey length (Electron)', 'Lang 4: remote validated', 'FSCV 0: *OPT', 'FSCV 1: EOF check', 'FSCV 2: */ (run)', 'FSCV 3: unrecognised star command', 'FSCV 4: *RUN', 'FSCV 5: *CAT', 'FSCV 6: shutdown', 'FSCV 7: read handle range', 'FS reply: print directory name', 'FS reply: copy handles + boot', 'FS reply: copy handles', 'FS reply: set CSD handle', 'FS reply: notify + execute', 'FS reply: set library handle', '*NET1: read handle from packet', '*NET2: read handle from workspace', '*NET3: close handle', '*NET4: resume remote']
for i, body in enumerate(dispatch_comments):
    d.comment(0x8021 + i, f'lo - {body}', align=Align.INLINE)
    d.comment(0x8045 + i, f'hi - {body}', align=Align.INLINE)


d.subroutine(0x8069, 'dispatch_net_cmd', title='*NET command dispatcher', description="""Parses the character after *NET as '1'-'4', maps to table
indices 33-36 via base offset Y=&20, and dispatches via &809F.
Characters outside '1'-'4' fall through to return_1 (RTS).

These are internal sub-commands used only by the ROM itself,
not user-accessible star commands. The MOS command parser
requires a space or terminator after 'NET', so *NET1 typed
at the command line does not match; these are reached only
via OSCLI calls within the ROM.

*NET1 (&8DB0): read file handle from received
packet (net_1_read_handle)

*NET2 (&8DCA): read handle entry from workspace
(net_2_read_handle_entry)

*NET3 (&8DE0): close handle / mark as unused
(net_3_close_handle)

*NET4 (&8DF3): resume after remote operation
(net_4_resume_remote)""")
d.comment(0x8069, 'Read command character following *NET', align=Align.INLINE)
d.comment(0x806B, "Subtract ASCII '1' to get 0-based command index", align=Align.INLINE)
d.comment(0x8075, 'Y=&20: base offset for *NET commands (index 33+)', align=Align.INLINE)


d.subroutine(0x809F, 'dispatch', title='PHA/PHA/RTS computed dispatch', description="""X = command index within caller's group (e.g. service number)
Y = base offset into dispatch table (0, &0D, &20, etc.)
The loop adds Y+1 to X, so final X = command index + base + 1.
Then high and low bytes of (handler-1) are pushed onto the stack,
and RTS pops them and jumps to handler_address.

This is a standard 6502 trick: RTS increments the popped address
by 1 before jumping, so the table stores (address - 1) to
compensate. Multiple callers share one table via different Y
base offsets.""")
d.comment(0x809F, 'Add base offset Y to index X (loop: X += Y+1)', align=Align.INLINE)
d.comment(0x80A4, 'Load high byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80A7, 'Push high byte onto stack', align=Align.INLINE)
d.comment(0x80A8, 'Load low byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80AB, 'Push low byte onto stack', align=Align.INLINE)
d.comment(0x80AC, 'Restore X (fileserver options) for use by handler', align=Align.INLINE)
d.comment(0x80AE, 'RTS pops address, adds 1, jumps to handler', align=Align.INLINE)


d.subroutine(0x8099, 'lang_entry_dispatch', title='Language entry dispatcher', description="""Called when the NFS ROM is entered as a language. Although rom_type
(&82) does not set the language bit, the MOS enters this point
after NFS claims service &FE (Tube post-init). X = reason code
(0-4). Dispatches via table indices 14-18 (base offset Y=&0D).""")
d.comment(0x809D, 'Y=&0D: base offset for language handlers (index 14+)', align=Align.INLINE)


d.subroutine(0x8127, 'dispatch_service', title='Service call dispatcher', description="""Dispatches MOS service calls 0-12 via the shared dispatch table.
Uses base offset Y=0, so table index = service number + 1.
Service numbers >= 13 are ignored (branch to return_2).
Called via JSR &809F rather than fall-through, so it returns
to &813C to restore saved registers.""")
d.comment(0x8139, 'JSR to dispatcher (returns here after handler completes)', align=Align.INLINE)


d.subroutine(0x80AF, 'service_handler_entry', title='Service handler entry', description="""Intercepts three special service calls before normal dispatch:
  &FE: Tube init — explode character definitions (OSBYTE &14, X=6)
  &FF: Full init — set up WRCHV/RDCHV/BRKV/EVNTV, copy NMI handler
       code from ROM to RAM pages &04-&06, copy workspace init to
       &0016-&0076, then fall through to select NFS.
  &12 with Y=5: Select NFS as active filing system.
All other service calls dispatch via dispatch_service (&8127).""")


d.subroutine(0x80C8, 'init_vectors_and_copy', title='NFS initialisation (service &FF: full reset)', description="""Sets up OS vectors for Tube co-processor support:
  WRCHV = &051C (page 5 — WRCH handler)
  RDCHV = &04E7 (page 4 — RDCH handler)
  BRKV  = &0016 (workspace — BRK/error handler)
  EVNTV = &06E8 (page 6 — event handler)
Writes &8E to Tube control register (&FEE0).
Then copies 3 pages of Tube host code from ROM (tube_code_page4,
tube_dispatch_table, tube_code_page6) to RAM (&0400/&0500/&0600),
calls tube_post_init (&0414), and copies 97 bytes of workspace
init from ROM (nmi_workspace_start) to &0016-&0076.""")
d.comment(0x80C8, 'Set WRCHV = &051C (Tube WRCH handler)', align=Align.INLINE)
d.comment(0x80D2, 'Set RDCHV = &04E7 (Tube RDCH handler)', align=Align.INLINE)
d.comment(0x80DC, 'Set BRKV = &0016 (BRK handler in workspace)', align=Align.INLINE)
d.comment(0x80E6, 'Set EVNTV = &06E8 (event handler in page 6)', align=Align.INLINE)
d.comment(0x80F0, 'Write &8E to Tube control register', align=Align.INLINE)


d.subroutine(0x8184, 'select_nfs', title='Select NFS as active filing system (INIT)', description="""Reached from service &12 (select FS) with Y=5, or when *NET command
selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
this triggers the outgoing FS to save its context back to its
workspace page, allowing restoration if re-selected later (the
FSDIE handoff mechanism). Then sets up the standard OS vector
indirections (FILEV through FSCV) to NFS entry points, claims the
extended vector table entries, and issues service &0F (vectors
claimed) to notify other ROMs. If nfs_temp is zero (auto-boot
not inhibited), injects the synthetic command "I .BOOT" through
the command decoder to trigger auto-boot login.""")


d.subroutine(0x81E7, 'print_station_info', title='Print station identification', description="""Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")


d.subroutine(0x8218, 'init_fs_vectors', title='Initialise filing system vectors', description="""Copies 14 bytes from fs_vector_addrs (&824E) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")
d.comment(0x8218, 'Copy 14 bytes: FS vector addresses → FILEV-FSCV', align=Align.INLINE)


d.subroutine(0x824E, 'fs_vector_addrs', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by init_fs_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the ROM pointer table.

Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
Each entry has addr_lo, addr_hi, then a padding byte that is
overwritten with the current ROM bank number at runtime. The
last entry (FSCV) has no padding byte.""")
d.byte(0x824E, 1)
d.comment(0x824E, 'FILEV dispatch lo', align=Align.INLINE)
d.byte(0x824F, 1)
d.comment(0x824F, 'FILEV dispatch hi', align=Align.INLINE)
d.byte(0x8250, 1)
d.comment(0x8250, 'ARGSV dispatch lo', align=Align.INLINE)
d.byte(0x8251, 1)
d.comment(0x8251, 'ARGSV dispatch hi', align=Align.INLINE)
d.byte(0x8252, 1)
d.comment(0x8252, 'BGETV dispatch lo', align=Align.INLINE)
d.byte(0x8253, 1)
d.comment(0x8253, 'BGETV dispatch hi', align=Align.INLINE)
d.byte(0x8254, 1)
d.comment(0x8254, 'BPUTV dispatch lo', align=Align.INLINE)
d.byte(0x8255, 1)
d.comment(0x8255, 'BPUTV dispatch hi', align=Align.INLINE)
d.byte(0x8256, 1)
d.comment(0x8256, 'GBPBV dispatch lo', align=Align.INLINE)
d.byte(0x8257, 1)
d.comment(0x8257, 'GBPBV dispatch hi', align=Align.INLINE)
d.byte(0x8258, 1)
d.comment(0x8258, 'FINDV dispatch lo', align=Align.INLINE)
d.byte(0x8259, 1)
d.comment(0x8259, 'FINDV dispatch hi', align=Align.INLINE)
d.byte(0x825A, 1)
d.comment(0x825A, 'FSCV dispatch lo', align=Align.INLINE)
d.byte(0x825B, 1)
d.comment(0x825B, 'FSCV dispatch hi', align=Align.INLINE)
d.byte(0x825C, 1)
d.comment(0x825C, 'FILEV handler lo (&8695)', align=Align.INLINE)
d.byte(0x825D, 1)
d.comment(0x825D, 'FILEV handler hi', align=Align.INLINE)
d.byte(0x825E, 1)
d.comment(0x825E, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x825F, 1)
d.comment(0x825F, 'ARGSV handler lo (&88E2)', align=Align.INLINE)
d.byte(0x8260, 1)
d.comment(0x8260, 'ARGSV handler hi', align=Align.INLINE)
d.byte(0x8261, 1)
d.comment(0x8261, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x8262, 1)
d.comment(0x8262, 'BGETV handler lo (&8486)', align=Align.INLINE)
d.byte(0x8263, 1)
d.comment(0x8263, 'BGETV handler hi', align=Align.INLINE)
d.byte(0x8264, 1)
d.comment(0x8264, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x8265, 1)
d.comment(0x8265, 'BPUTV handler lo (&83A3)', align=Align.INLINE)
d.byte(0x8266, 1)
d.comment(0x8266, 'BPUTV handler hi', align=Align.INLINE)
d.byte(0x8267, 1)
d.comment(0x8267, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x8268, 1)
d.comment(0x8268, 'GBPBV handler lo (&89EB)', align=Align.INLINE)
d.byte(0x8269, 1)
d.comment(0x8269, 'GBPBV handler hi', align=Align.INLINE)
d.byte(0x826A, 1)
d.comment(0x826A, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x826B, 1)
d.comment(0x826B, 'FINDV handler lo (&894A)', align=Align.INLINE)
d.byte(0x826C, 1)
d.comment(0x826C, 'FINDV handler hi', align=Align.INLINE)
d.byte(0x826D, 1)
d.comment(0x826D, '(ROM bank — overwritten)', align=Align.INLINE)
d.byte(0x826E, 1)
d.comment(0x826E, 'FSCV handler lo (&808C)', align=Align.INLINE)
d.byte(0x826F, 1)
d.comment(0x826F, 'FSCV handler hi', align=Align.INLINE)


d.subroutine(0x8270, 'svc_1_abs_workspace', title='Service 1: claim absolute workspace', description="""Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""", on_entry={'y': 'current top of absolute workspace'}, on_exit={'y': 'updated top of absolute workspace (max of input and &10)'})


d.subroutine(0x8279, 'svc_2_private_workspace', title='Service 2: claim private workspace and initialise NFS', description="""Y = next available workspace page on entry.
Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
On soft break (OSBYTE &FD returns 0): skips FS state init,
preserving existing login state, file server selection, and
control block configuration — this is why pressing BREAK
keeps the user logged in.
On power-up/CTRL-BREAK (result non-zero):
  - Sets FS server station to &FE (FS, the default; no server)
  - Sets printer server to &EB (PS, the default)
  - Clears FS handles, OPT byte, message flag, SEQNOS
  - Initialises all RXCBs with &3F flag (available)
In both cases: reads station ID from &FE18 (only valid during
reset), calls adlc_init, enables user-level RX (LFLAG=&40).""", on_entry={'y': 'next available workspace page'}, on_exit={'y': 'next available workspace page after NFS (input + 2)'})
d.comment(0x8290, 'OSBYTE &FD: read type of last reset', align=Align.INLINE)
d.comment(0x8296, 'Soft break (X=0): skip FS init', align=Align.INLINE)
d.comment(0x829C, 'Station &FE = no server selected', align=Align.INLINE)
d.comment(0x82C4, 'Read station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x82CA, 'Initialise ADLC hardware', align=Align.INLINE)


d.subroutine(0x81D2, 'svc_3_autoboot', title='Service 3: auto-boot', description="""Notifies current FS of shutdown via FSCV A=6. Scans keyboard
(OSBYTE &7A): if the 'N' key is pressed (matrix address &55),
the keypress is forgotten via OSBYTE &78 and auto-boot proceeds.
Any other key causes the auto-boot to be declined. If no key is
pressed, auto-boot proceeds directly. Falls through to
print_station_info, then init_fs_vectors.""")


d.subroutine(0x8172, 'svc_4_star_command', title='Service 4: unrecognised * command', description="""Matches the command text against ROM string table entries.
Both entries reuse bytes from the ROM header to save space:

  X=8: matches "ROFF" at copyright_string+3 — the suffix
       of "(C)ROFF" → *ROFF (Remote Off,
       end remote session) — jumps to resume_after_remote

  X=1: matches "NET" at &8009 — the ROM title string
       → *NET (select NFS) — falls through to select_nfs

If neither matches, returns with the service call
unclaimed.""")


d.subroutine(0x81BC, 'svc_9_help', title='Service 9: *HELP', description='Prints the ROM identification string using print_inline.')


d.subroutine(0x819B, 'match_rom_string', title='Match command text against ROM string table', description="""Compares characters from (os_text_ptr)+Y against bytes starting
at binary_version+X (&8008+X). Input is uppercased via AND &DF.
Returns with Z=1 if the ROM string's NUL terminator was reached
(match), or Z=0 if a mismatch was found. On match, Y points
past the matched text; on return, skips trailing spaces.""")
d.comment(0x819B, 'Y = saved text pointer offset', align=Align.INLINE)
d.comment(0x819D, 'Load next input character', align=Align.INLINE)
d.comment(0x819F, 'Force uppercase (clear bit 5)', align=Align.INLINE)
d.comment(0x81A1, 'Input char is NUL/space: check ROM byte', align=Align.INLINE)
d.comment(0x81A3, 'Compare with ROM string byte', align=Align.INLINE)
d.comment(0x81A6, 'Mismatch: check if ROM string ended', align=Align.INLINE)
d.comment(0x81A8, 'Advance input pointer', align=Align.INLINE)
d.comment(0x81A9, 'Advance ROM string pointer', align=Align.INLINE)
d.comment(0x81AA, 'Continue matching (always taken)', align=Align.INLINE)
d.comment(0x81AC, 'Load ROM string byte at match point', align=Align.INLINE)
d.comment(0x81AF, 'Zero = end of ROM string = full match', align=Align.INLINE)
d.comment(0x81B1, 'Non-zero = partial/no match; Z=0', align=Align.INLINE)
d.comment(0x81B2, 'Skip this space', align=Align.INLINE)
d.comment(0x81B3, 'Load next input character', align=Align.INLINE)
d.comment(0x81B5, 'Is it a space?', align=Align.INLINE)
d.comment(0x81B7, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0x81B9, 'XOR with CR: Z=1 if end of line', align=Align.INLINE)


d.subroutine(0x81CD, 'call_fscv_shutdown', title='Notify filing system of shutdown', description="""Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")


d.subroutine(0x822F, 'issue_vectors_claimed', title="Issue 'vectors claimed' service and optionally auto-boot", description="""Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If nfs_temp is zero (auto-boot not inhibited),
sets up the command string "I .BOOT" at &8246 and jumps to
the FSCV 3 unrecognised-command handler (which matches against
the command table at &8BD7). The "I." prefix triggers the
catch-all entry which forwards the command to the fileserver.
Falls through to run_fscv_cmd.""")


d.subroutine(0x8241, 'run_fscv_cmd', title='Run FSCV command from ROM', description="""Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
to execute the command string at (X, Y). X is pre-loaded by the
caller with the low byte of the string address. Also used as a
data base address by store_rom_ptr_pair for Y-indexed access to
the handler address table.""")
d.string(0x8246, 8)
d.comment(0x8246, """Synthetic auto-boot command string. "I " does not match any
entry in NFS's local command table — "I." requires a dot, and
"I AM" requires 'A' after the space — so fscv_3_star_cmd
forwards the entire string to the fileserver, which executes
the .BOOT file.""")


d.subroutine(0x82D2, 'setup_rom_ptrs_netv', title='Set up ROM pointer table and NETV', description="""Reads the ROM pointer table base address via OSBYTE &A8, stores
it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
one 3-byte extended vector entry (addr=&9008, rom=current) into
the ROM pointer table at offset &36, installing osword_dispatch
as the NETV handler.""")


d.subroutine(0x82FE, 'fscv_6_shutdown', title='FSCV 6: Filing system shutdown / save state (FSDIE)', description="""Called when another filing system (e.g. DFS) is selected. Saves
the current NFS context (FSLOCN station number, URD/CSD/LIB
handles, OPT byte, etc.) from page &0E into the dynamic workspace
backup area. This allows the state to be restored when *NET is
re-issued later, without losing the login session. Finally calls
OSBYTE &7B (printer driver going dormant) to release the
Econet network printer on FS switch.""")


d.subroutine(0x831D, 'init_tx_ctrl_block', title='Initialise TX control block at &00C0 from template', description="""Copies 12 bytes from tx_ctrl_template (&8335) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""")


d.subroutine(0x8335, 'tx_ctrl_template', title='TX control block template (TXTAB, 12 bytes)', description="""12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")
d.byte(0x8335, 1)
d.comment(0x8335, 'Control flag', align=Align.INLINE)
d.byte(0x8336, 1)
d.comment(0x8336, 'Port (FS command = &99)', align=Align.INLINE)
d.byte(0x8337, 1)
d.comment(0x8337, 'Station (filled at runtime)', align=Align.INLINE)
d.byte(0x8338, 1)
d.comment(0x8338, 'Network (filled at runtime)', align=Align.INLINE)
d.byte(0x8339, 1)
d.comment(0x8339, 'Buffer start low', align=Align.INLINE)
d.byte(0x833A, 1)
d.comment(0x833A, 'Buffer start high (page &0F)', align=Align.INLINE)
d.byte(0x833B, 1)
d.comment(0x833B, 'Buffer start pad (4-byte Econet addr)', align=Align.INLINE)
d.byte(0x833C, 1)
d.comment(0x833C, 'Buffer start pad', align=Align.INLINE)
d.byte(0x833D, 1)
d.comment(0x833D, 'Buffer end low', align=Align.INLINE)
d.byte(0x833E, 1)
d.comment(0x833E, 'Buffer end high (page &0F)', align=Align.INLINE)
d.byte(0x833F, 1)
d.comment(0x833F, 'Buffer end pad', align=Align.INLINE)
d.byte(0x8340, 1)
d.comment(0x8340, 'Buffer end pad', align=Align.INLINE)


d.subroutine(0x8341, 'prepare_cmd_with_flag', title='Prepare FS command with carry set', description="""Alternate entry to prepare_fs_cmd that pushes A, loads &2A
into fs_error_ptr, and enters with carry set (SEC). The carry
flag is later tested by build_send_fs_cmd to select the
byte-stream (BSXMIT) transmission path.""", on_entry={'a': 'flag byte to include in FS command', 'y': 'function code for FS header'})


d.subroutine(0x8351, 'prepare_fs_cmd', title='Prepare FS command buffer (12 references)', description="""Builds the 5-byte FS protocol header at &0F00:
  &0F00 HDRREP = reply port (set downstream, typically &90/PREPLY)
  &0F01 HDRFN  = Y parameter (function code)
  &0F02 HDRURD = URD handle (from &0E02)
  &0F03 HDRCSD = CSD handle (from &0E03)
  &0F04 HDRLIB = LIB handle (from &0E04)
Command-specific data follows at &0F05 (TXBUF). Also clears V flag.
Called before building specific FS commands for transmission.""", on_entry={'y': 'function code for HDRFN', 'x': 'preserved through header build'}, on_exit={'a': '0 on success (from build_send_fs_cmd)', 'x': '0 on success, &D6 on not-found', 'y': '1 (offset past command code in reply)'})


d.subroutine(0x836B, 'build_send_fs_cmd', title='Build and send FS command (DOFSOP)', description="""Sets reply port to &90 (PREPLY) at &0F00, initialises the TX
control block, then adjusts TXCB's high pointer (HPTR) to X+5
-- the 5-byte FS header (reply port, function code, URD, CSD,
LIB) plus the command data -- so only meaningful bytes are
transmitted, conserving Econet bandwidth. If carry is set on
entry (DOFSBX byte-stream path), takes the alternate path
through econet_tx_retry for direct BSXMIT transmission.
Otherwise sets up the TX pointer via setup_tx_ptr_c0 and falls
through to send_fs_reply_cmd for reply handling. The carry flag
is the sole discriminator between byte-stream and standard FS
protocol paths -- set by SEC at the BPUTV/BGETV entry points.
On return from WAITFS/BSXMIT, Y=0; INY advances past the
command code to read the return code. Error &D6 ("not found",
    on_entry={"x": "buffer extent (command-specific data bytes)", "y": "function code", "a": "timeout period for FS reply", "c": "0 for standard FS path, 1 for byte-stream (BSXMIT)"},
    on_exit={"a": "0 on success", "x": "0 on success, &D6 on not-found", "y": "1 (offset past command code in reply)"})
is detected via ADC #(&100-&D6) with C=0 -- if the return code
was exactly &D6, the result wraps to zero (Z=1). This is a
branchless comparison returning C=1, A=0 as a soft error that
callers can handle, vs hard errors which go through FSERR.""", on_entry={'x': 'buffer extent (command-specific data bytes)', 'y': 'function code', 'a': 'timeout period for FS reply', 'c': '0 for standard FS path, 1 for byte-stream (BSXMIT)'}, on_exit={'a': '0 on success', 'x': '0 on success, &D6 on not-found', 'y': '1 (offset past command code in reply)'})


d.subroutine(0x8403, 'store_fs_error', title='Handle fileserver error replies (FSERR)', description="""The fileserver returns errors as: zero command code + error number +
CR-terminated message string. This routine converts the reply buffer
in-place to a standard MOS BRK error packet by:
  1. Storing the error code at fs_last_error (&0E09)
  2. Normalizing error codes below &A8 to &A8 (the standard FS error
     number), since the MOS error space below &A8 has other meanings
  3. Scanning for the CR terminator and replacing it with &00
  4. JMPing indirect through (l00c4) to execute the buffer as a BRK
     instruction — the zero command code serves as the BRK opcode
N.B. This relies on the fileserver always returning a zero command
code in position 0 of the reply buffer.""")


d.subroutine(0x83A4, 'handle_bput_bget', title='Handle BPUT/BGET file byte I/O', description="""BPUTV enters at &83A3 (CLC; fall through) and BGETV enters
at &8486 (SEC; JSR here). The carry flag is preserved via
PHP/PLP through the call chain and tested later (BCS) to
select byte-stream transmission (BSXMIT) vs normal FS
transmission (FSXMIT) -- a control-flow encoding using
processor flags to avoid an extra flag variable.

BSXMIT uses handle=0 for print stream transactions (which
sidestep the SEQNOS sequence number manipulation) and non-zero
handles for file operations. After transmission, the high
pointer bytes of the CB are reset to &FF -- "The BGET/PUT byte
fix" which prevents stale buffer pointers corrupting subsequent
byte-level operations.""", on_entry={'c': '0 for BPUT (write byte), 1 for BGET (read byte)', 'a': 'byte to write (BPUT only)', 'y': 'file handle'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'preserved'})


d.subroutine(0x844B, 'send_to_fs', title='Send command to fileserver and handle reply (WAITFS)', description="""Performs a complete FS transaction: transmit then wait for reply.
Sets bit 7 of rx_status_flags (mark FS transaction in progress),
builds a TX frame from the data at (net_tx_ptr), and transmits
it. The system RX flag (LFLAG bit 7) is only set when receiving
into the page-zero control block — if RXCBP's high byte is
non-zero, setting the system flag would interfere with other RX
operations. The timeout counter uses the stack (indexed via TSX)
rather than memory to avoid bus conflicts with Econet hardware
during the tight polling loop. Handles multi-block replies and
checks for escape conditions between blocks.""")


d.subroutine(0x847B, 'check_escape', title='Check and handle escape condition (ESC)', description="""Two-level escape gating: the MOS escape flag (&FF bit 7) is ANDed
with the software enable flag ESCAP. Both must have bit 7 set for
escape to fire. ESCAP is set non-zero during data port operations
(LOADOP stores the data port &90, serving double duty as both the
port number and the escape-enable flag). ESCAP is disabled via LSR
in the ENTER routine, which clears bit 7 — PHP/PLP around the LSR
preserves the carry flag since ENTER is called from contexts where
carry has semantic meaning (e.g., PUTBYT vs BGET distinction).
This architecture allows escape between retransmission attempts
but prevents interruption during critical FS transactions. If
escape fires: acknowledges via OSBYTE &7E, then checks whether
the failing handle is the current SPOOL or EXEC handle (OSBYTE
&C6/&C7); if so, issues "*SP." or "*E." via OSCLI to gracefully
close the channel before raising the error — preventing the system
from continuing to spool output to a broken file handle.""")

d.label(0x84B0, 'error_msg_table')
d.comment(0x84B0, """Econet error message table (ERRTAB, 8 entries).
Each entry: error number byte followed by NUL-terminated string.
  &A0: "Line Jammed"     &A1: "Net Error"
  &A2: "Not listening"   &A3: "No Clock"
  &A4: "Bad Txcb"        &11: "Escape"
  &CB: "Bad Option"      &A5: "No reply"
Indexed by the low 3 bits of the TXCB flag byte (AND #&07),
which encode the specific Econet failure reason. The NREPLY
and NLISTN routines build a MOS BRK error block at &100 on the
stack page: NREPLY fires when the fileserver does not respond
within the timeout period; NLISTN fires when the destination
station actively refused the connection.
Indexed via the error dispatch at c8424/c842c.""")
addr = 0x84B0
for _ in range(8):
    d.byte(addr, 1)
    addr = d.stringz(addr + 1)


d.subroutine(0x8146, 'resume_after_remote', title='Resume after remote operation / *ROFF handler (NROFF)', description="""Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
disabled during a remote operation (peek/poke/boot). Clears
the flag, re-enables the keyboard via OSBYTE &C9, and sends
function &0A to notify completion. Also handles *ROFF and the
triple-plus escape sequence (+++), which resets system masks
via OSBYTE &CE and returns control to the MOS, providing an
escape route when a remote session becomes unresponsive.""")


d.subroutine(0x808C, 'fscv_handler', title='FSCV dispatch entry', description="""Entered via the extended vector table when the MOS calls FSCV.
Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
and dispatches codes 0-7 via the shared dispatch table at &8020
with base offset Y=&12 (table indices 19-26).
Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.""", on_entry={'a': 'function code (0-7)', 'x': 'depends on function', 'y': 'depends on function'}, on_exit={'a': 'depends on handler (preserved if A >= 8)', 'x': 'depends on handler (preserved if A >= 8)', 'y': 'depends on handler (preserved if A >= 8)'})
d.comment(0x808C, 'Store A/X/Y in FS workspace', align=Align.INLINE)
d.comment(0x808F, 'Function code >= 8? Return (unsupported)', align=Align.INLINE)
d.comment(0x8095, 'Y=&12: base offset for FSCV dispatch (indices 19+)', align=Align.INLINE)


d.subroutine(0x8695, 'filev_handler', title='FILEV handler (OSFILE entry point)', description="""Saves A/X/Y, copies the filename pointer from the parameter block
to os_text_ptr, then uses GSINIT/GSREAD to parse the filename into
&0FC5+. Sets fs_crc_lo/hi to point at the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &86D1)
  A=&00: save file (filev_save at &8747)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &8845)
  Other: restore_args_return (unsupported, no-op)""", on_entry={'a': 'function code (&FF=load, &00=save, &01-&06=attrs)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x86D1, 'send_fs_examine', title='Send FS examine command', description="""Sends FS command &03 (FCEXAM: examine file) to the fileserver.
Sets &0F02=&03 and error pointer to '*'. Called for OSFILE &FF
(load file) with the filename already in the command buffer.
The FS reply contains load/exec addresses and file length which
are used to set up the data transfer. The header URD field
is repurposed to carry the Econet data port number (PLDATA=&92)
for the subsequent block data transfer.""", on_entry={'y': 'FS function code (2=load, 5=examine)', 'x': 'TX buffer extent'})


d.subroutine(0x8717, 'send_data_blocks', title='Send file data in multi-block chunks', description="""Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")


d.subroutine(0x8747, 'filev_save', title='OSFILE save handler (A=&00)', description="""Copies 4-byte load/exec/length addresses from the parameter block
to the FS command buffer, along with the filename. Sends FS
command &91 with function &14 to initiate the save, then
calls print_file_info to display the filename being saved.
Handles both host and Tube-based data sources.
When receiving the save acknowledgement, the RX low pointer is
incremented by 1 to skip the command code (CC) byte, which
indicates the FS type and must be preserved. N.B. this assumes
the RX buffer does not cross a page boundary.""")


d.subroutine(0x87AE, 'copy_load_addr_from_params', title='Copy load address from parameter block', description="""Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""")


d.subroutine(0x87BB, 'copy_reply_to_params', title='Copy FS reply data to parameter block', description="""Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""", on_entry={'x': 'attribute byte (stored first at offset &0D)'})


d.subroutine(0x87C9, 'transfer_file_blocks', title='Multi-block file data transfer', description="""Manages the transfer of file data in chunks between the local
machine and the fileserver. Entry conditions: WORK (&B0-&B3) and
WORK+4 (&B4-&B7) hold the low and high addresses of the data
being sent/received. Sets up source (&C4-&C7) and destination
(&C8-&CB) from the FS reply, sends &80-byte (128-byte) blocks
with command &91, and continues until all data has been
transferred. Handles address overflow and Tube co-processor
transfers. For SAVE, WORK+8 holds the port on which to receive
byte-level ACKs for each data block (flow control).""")


d.subroutine(0x8820, 'fscv_1_eof', title='FSCV 1: EOF handler', description="""Checks whether a file handle has reached end-of-file. Converts
the handle via handle_to_mask_clc, tests the result against the
EOF hint byte (&0E07). If the hint bit is clear, returns X=0
immediately (definitely not at EOF — no network call needed).
If the hint bit is set, sends FS command &11 (FCEOF) to query
the fileserver for definitive EOF status. Returns X=&FF if at
EOF, X=&00 if not. This two-level check avoids an expensive
network round-trip when the file is known to not be at EOF.""", on_entry={'x': 'file handle to check'}, on_exit={'x': '&FF if at EOF, &00 if not'})


d.subroutine(0x8845, 'filev_attrib_dispatch', title='FILEV attribute dispatch (A=1-6)', description="""Dispatches OSFILE operations by function code:
  A=1: write catalogue info (load/exec/length/attrs) — FS &14
  A=2: write load address only
  A=3: write exec address only
  A=4: write file attributes
  A=5: read catalogue info, returns type in A — FS &12
  A=6: delete named object — FS &14 (FCDEL)
  A>=7: falls through to restore_args_return (no-op)
Each handler builds the appropriate FS command, sends it to
the fileserver, and copies the reply into the parameter block.
The control block layout uses dual-purpose fields: the 'data
start' field doubles as 'length' and 'data end' doubles as
'protection' depending on whether reading or writing attrs.""", on_entry={'a': 'function code (1-6)'}, on_exit={'a': 'object type (A=5 read info) or restored'})


d.subroutine(0x892D, 'restore_args_return', title='Restore arguments and return', description="""Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""")


d.subroutine(0x89A2, 'fscv_0_opt', title='FSCV 0: *OPT handler (OPTION)', description="""Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""", on_entry={'x': 'option number (1 or 4)', 'y': 'option value'})


d.subroutine(0x89D3, 'adjust_addrs', title='Bidirectional 4-byte address adjustment', description="""Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""", on_entry={'y': 'starting offset into (fs_options) parameter block'}, on_exit={'a': 'corrupted (last adjusted byte)', 'x': '0', 'y': 'entry Y + 4'})
d.comment(0x89D3, 'X=&FC: index into &0E06 area (wraps to 0)', align=Align.INLINE)
d.comment(0x89D5, 'Load byte from param block', align=Align.INLINE)
d.comment(0x89D7, 'Test sign of adjustment direction', align=Align.INLINE)
d.comment(0x89D9, 'Negative: subtract instead', align=Align.INLINE)
d.comment(0x89DB, 'Add adjustment value', align=Align.INLINE)
d.comment(0x89DE, 'Skip to store result', align=Align.INLINE)
d.comment(0x89E1, 'Subtract adjustment value', align=Align.INLINE)
d.comment(0x89E4, 'Store adjusted byte back', align=Align.INLINE)
d.comment(0x89E6, 'Next param block byte', align=Align.INLINE)
d.comment(0x89E7, 'Next adjustment byte (X wraps &FC->&00)', align=Align.INLINE)
d.comment(0x89E8, 'Loop 4 times (X=&FC,&FD,&FE,&FF,done)', align=Align.INLINE)


d.subroutine(0x88E2, 'argsv_handler', title='ARGSV handler (OSARGS entry point)', description="""  A=0, Y=0: return filing system number (10 = network FS)
  A=0, Y>0: read file pointer via FS command &0A (FCRDSE)
  A=1, Y>0: write file pointer via FS command &14 (FCWRSE)
  A>=3 (ensure): silently returns -- NFS has no local write buffer
     to flush, since all data is sent to the fileserver immediately
The handle in Y is converted via handle_to_mask_clc. For writes
(A=1), the carry flag from the mask conversion is used to branch
to save_args_handle, which records the handle for later use.""", on_entry={'a': 'function code (0=query, 1=write ptr, >=3=ensure)', 'y': 'file handle (0=FS-level query, >0=per-file)'}, on_exit={'a': 'filing system number if A=0/Y=0 query, else restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x894A, 'findv_handler', title='FINDV handler (OSFIND entry point)', description="""  A=0: close file -- delegates to close_handle (&8986)
  A>0: open file -- modes &40=read, &80=write/update, &C0=read/write
For open: the mode byte is converted to the fileserver's two-flag
format by flipping bit 7 (EOR #&80) and shifting. This produces
Flag 1 (read/write direction) and Flag 2 (create/existing),
matching the fileserver protocol. After a successful open, the
new handle's bit is OR'd into the EOF hint byte (marks it as
"might be at EOF, query the server",
    on_entry={"a": "operation (0=close, &40=read, &80=write, &C0=R/W)", "x": "filename pointer low (open)", "y": "file handle (close) or filename pointer high (open)"},
    on_exit={"a": "handle on open, 0 on close-all, restored on close-one", "x": "restored", "y": "restored"})
number tracking byte for the byte-stream protocol.""", on_entry={'a': 'operation (0=close, &40=read, &80=write, &C0=R/W)', 'x': 'filename pointer low (open)', 'y': 'file handle (close) or filename pointer high (open)'}, on_exit={'a': 'handle on open, 0 on close-all, restored on close-one', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x8986, 'close_handle', title='Close file handle(s) (CLOSE)', description="""  Y=0: close all files — first calls OSBYTE &77 (close SPOOL and
       EXEC files) to coordinate with the MOS before sending the
       close-all command to the fileserver. This ensures locally-
       managed file handles are released before the server-side
       handles are invalidated, preventing the MOS from writing to
       a closed spool file.
  Y>0: close single handle — sends FS close command and clears
       the handle's bit in both the EOF hint byte and the sequence
       number tracking byte.""", on_entry={'y': 'file handle (0=close all, >0=close single)'})


d.subroutine(0x89EB, 'gbpbv_handler', title='GBPBV handler (OSGBPB entry point)', description="""  A=1-4: file read/write operations (handle-based)
  A=5-8: info queries (disc title, current dir, lib, filenames)
Calls 1-4 are standard file data transfers via the fileserver.
Calls 5-8 were a late addition to the MOS spec and are the only
NFS operations requiring Tube data transfer -- described in the
original source as "untidy but useful in theory." The data format
uses length-prefixed strings (<name length><object name>) rather
than the CR-terminated strings used elsewhere in the FS.""", on_entry={'a': 'call number (1-8)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': '0 after FS operation, else restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x8AAE, 'osgbpb_info', title='OSGBPB 5-8 info handler (OSINFO)', description="""Handles the "messy interface tacked onto OSGBPB" (original source).
Checks whether the destination address is in Tube space by comparing
the high bytes against TBFLAG. If in Tube space, data must be
copied via the Tube FIFO registers (with delays to accommodate the
slow 16032 co-processor) instead of direct memory access.""")


d.subroutine(0x8079, 'forward_star_cmd', title='Forward unrecognised * command to fileserver (COMERR)', description="""Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
prepares an FS command with function code 0, and sends it to the
fileserver to request decoding. The server returns a command code
indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
5=load-as-command). This mechanism allows the fileserver to extend
the client's command set without ROM updates. Called from the "I."
and catch-all entries in the command match table at &8BD7, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")


d.subroutine(0x834A, 'bye_handler', title='*BYE handler (logoff)', description="""Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8BD7 for "BYE".""")


d.subroutine(0x8B93, 'fscv_3_star_cmd', title='FSCV 2/3/4: unrecognised * command handler (DECODE)', description="""CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8BD7 using case-insensitive comparison with abbreviation
support — commands can be shortened with '.' (e.g. "I." for
"INFO"). The "I." entry is a special fudge placed first in the
table: since "I." could match multiple commands, it jumps to
forward_star_cmd to let the fileserver resolve the ambiguity.

The matching loop compares input characters against table
entries. On mismatch, it skips to the next entry. On match
of all table characters, or when '.' abbreviation is found,
it dispatches via PHA/PHA/RTS to the entry's handler address.

After matching, adjusts fs_crc_lo/fs_crc_hi to point past
the matched command text.""")


d.subroutine(0x8BD7, 'fs_cmd_match_table', title='FS command match table (COMTAB)', description="""Format: command letters (bit 7 clear), then dispatch address
as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
adds 1 to the stored (address-1). Matching is case-insensitive
(AND &DF) and supports '.' abbreviation (standard Acorn pattern).

Entries:
  "I."     → &8079 (forward_star_cmd) — placed first as a fudge
             to catch *I. abbreviation before matching *I AM
  "I AM"   → &8D07 (i_am_handler: parse station.net, logon)
  "EX "    → &8BF3 (ex_handler: extended catalogue)
  "EX"\\r   → &8BF3 (same, exact match at end of line)
  "BYE"\\r  → &834A (bye_handler: logoff)
  <catch-all> → &8079 (forward anything else to FS)""")


d.subroutine(0x8BF3, 'ex_handler', title='*EX handler (extended catalogue)', description="""Sets column width &B6=&50 (80 columns, one file per line with
full details) and &B7=&01, then branches into fscv_5_cat at
&8C08, bypassing fscv_5_cat's default 20-column setup.""")


d.subroutine(0x8BFE, 'fscv_5_cat', title='*CAT handler (directory catalogue)', description="""Sets column width &B6=&14 (20 columns, four files per 80-column
line) and &B7=&03. The catalogue protocol is multi-step: first
sends FCUSER (&15: read user environment) to get CSD, disc, and
library names, then sends FCREAD (&12: examine) repeatedly to
fetch entries in batches until zero are returned (end of dir).
The receive buffer abuts the examine request buffer and ends at
RXBUFE, allowing seamless data handling across request cycles.

The command code byte in the fileserver reply indicates FS type:
zero means an old-format FS (client must format data locally),
non-zero means new-format (server returns pre-formatted strings).
This enables backward compatibility with older Acorn fileservers.

Display format:
  - Station number in parentheses
  - "Owner" or "Public" access level
  - Boot option with name (Off/Load/Run/Exec)
  - Current directory and library paths
  - Directory entries: CRFLAG (&CF) cycles 0-3 for multi-column
    layout; at count 0 a newline is printed, others get spaces.
    *EX sets CRFLAG=&FF to force one entry per line.""")


d.subroutine(0x8CEB, 'boot_cmd_strings', title='Boot command strings for auto-boot', description="""The four boot options use OSCLI strings at offsets within page &8C:
  Option 0 (Off):  offset &F7 → &8CF7 = bare CR (empty command)
  Option 1 (Load): offset &E8 → &8CE8 = "L.!BOOT" (dual-purpose:
      the JMP &212E instruction at &8CE8 has opcode &4C='L' and
      operand bytes &2E='.' &21='!', forming the string "L.!")
  Option 2 (Run):  offset &EA → boot_cmd_strings-1 = "!BOOT" (bare filename = *RUN)
  Option 3 (Exec): offset &F0 → &8CF0 = "E.!BOOT"

This is a classic BBC ROM space optimisation: the JMP instruction's
bytes serve double duty as both executable code and ASCII text.""")


d.subroutine(0x8CF8, 'fsreply_5_set_lib', title='Set library handle', description="""Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to set_handle_return (JMP restore_args_return) if Y is non-zero.""", on_entry={'y': 'library handle from FS reply'})


d.subroutine(0x8CFD, 'fsreply_3_set_csd', title='Set CSD handle', description="""Stores Y into &0E03 (current selected directory handle).
Falls through to set_handle_return (JMP restore_args_return).""", on_entry={'y': 'CSD handle from FS reply'})


d.subroutine(0x8D03, 'boot_option_offsets', title='Boot option → OSCLI string offset table', description="""Four bytes indexed by the boot option value (0-3). Each byte
is the low byte of a pointer into page &8C, where the OSCLI
command string for that boot option lives. See boot_cmd_strings.""")
d.byte(0x8D03, 1)
d.comment(0x8D03, 'Opt 0 (Off): bare CR', align=Align.INLINE)
d.byte(0x8D04, 1)
d.comment(0x8D04, 'Opt 1 (Load): L.!BOOT', align=Align.INLINE)
d.byte(0x8D05, 1)
d.comment(0x8D05, 'Opt 2 (Run): !BOOT', align=Align.INLINE)
d.byte(0x8D06, 1)
d.comment(0x8D06, 'Opt 3 (Exec): E.!BOOT', align=Align.INLINE)


d.subroutine(0x8D07, 'i_am_handler', title='"I AM" command handler', description="""Dispatched from the command match table when the user types
"*I AM <station>" or "*I AM <network>.<station>".
Skips leading spaces via skip_spaces, then calls parse_decimal
twice if a dot separator is present. The first number becomes the
network (&0E01, via TAX pass-through in parse_decimal) and the
second becomes the station (&0E00). With a single number, it is
stored as the station and the network defaults to 0 (local).
Then forwards the command to the fileserver via forward_star_cmd.""")


d.subroutine(0x8D20, 'fsreply_1_copy_handles_boot', title='Copy FS reply handles to workspace and execute boot command', description="""SEC entry (LOGIN): copies 4 bytes from &0F05-&0F08 (FS reply) to
&0E02-&0E05 (URD, CSD, LIB handles and boot option), then
looks up the boot option in boot_option_offsets to get the
OSCLI command string and executes it via JMP oscli.
The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
share the handle-copying code, but only LOGIN executes the boot
command. This use of the carry flag to select behaviour between
two callers avoids duplicating the handle-copy loop.""")


d.subroutine(0x8D21, 'fsreply_2_copy_handles', title='Copy FS reply handles to workspace (no boot)', description="""CLC entry (SDISC): copies handles only, then jumps to set_handle_return.
Called when the FS reply contains updated handle values
but no boot action is needed.""")


d.subroutine(0x8D3B, 'option_name_strings', title='Option name strings', description="""Null-terminated strings for the four boot option names:
  "Off", "Load", "Run", "Exec"
Used by fscv_5_cat to display the current boot option setting.""")


d.subroutine(0x8D4C, 'option_name_offsets', title='Option name offsets', description="""Four-byte table of offsets into option_name_strings:
  0, 4, 9, &0D — one per boot option value (0-3).""")


d.subroutine(0x8D50, 'print_reply_bytes', title='Print reply buffer bytes', description="""Prints Y characters from the FS reply buffer (&0F05+X) to
the screen via OSASCI. X = starting offset, Y = count.
Used by fscv_5_cat to display directory and library names.""")


d.subroutine(0x8D5D, 'print_spaces', title='Print spaces', description="""Prints X space characters via print_space. Used by fscv_5_cat
to align columns in the directory listing.""")


d.subroutine(0x8D64, 'copy_filename', title='Copy filename to FS command buffer', description="""Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""")


d.subroutine(0x8D66, 'copy_string_to_cmd', title='Copy string to FS command buffer', description="""Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""", on_entry={'x': 'destination offset in fs_cmd_data (&0F05+X)'}, on_exit={'x': 'next free position past CR', 'y': 'string length (incl CR)', 'a': '0 (from EOR &0D with final CR)'})
d.comment(0x8D66, 'Start copying from offset 0', align=Align.INLINE)
d.comment(0x8D68, 'Load next byte from source string', align=Align.INLINE)
d.comment(0x8D6A, 'Store to command buffer', align=Align.INLINE)
d.comment(0x8D6D, 'Advance write position', align=Align.INLINE)
d.comment(0x8D6E, 'Advance read position', align=Align.INLINE)
d.comment(0x8D6F, 'XOR with CR: result=0 if byte was CR', align=Align.INLINE)
d.comment(0x8D71, 'Loop until CR copied', align=Align.INLINE)


d.subroutine(0x8D74, 'fsreply_0_print_dir', title='Print directory name from reply buffer', description="""Prints characters from the FS reply buffer (&0F05+X onwards).
Null bytes (&00) are replaced with CR (&0D) for display.
Stops when a byte with bit 7 set is encountered (high-bit
terminator). Used by fscv_5_cat to display Dir. and Lib. paths.""")


d.subroutine(0x8D85, 'fsreply_4_notify_exec', title='Send FS load-as-command and execute response', description="""Sets up an FS command with function code &05 (FCCMND: load as
command) using send_fs_examine. If a Tube co-processor is
present (tx_in_progress != 0), transfers the response data
to the Tube via tube_addr_claim. Otherwise jumps via the
indirect pointer at (&0F09) to execute at the load address.""")


d.subroutine(0x8DB0, 'net_1_read_handle', title='*NET1: read file handle from received packet', description="""Reads a file handle byte from offset &6F in the RX buffer
(net_rx_ptr), stores it in &F0, then falls through to the
common handle workspace cleanup at clear_svc_return.""")


d.subroutine(0x8DB8, 'calc_handle_offset', title='Calculate handle workspace offset', description="""Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""", on_entry={'a': 'file handle number'}, on_exit={'a': 'handle*12 or 0 if invalid', 'y': 'workspace offset or 0 if invalid', 'c': 'clear if valid, set if invalid'})
d.comment(0x8DB8, 'A = handle * 2', align=Align.INLINE)
d.comment(0x8DB9, 'A = handle * 4', align=Align.INLINE)
d.comment(0x8DBA, 'Push handle*4 onto stack', align=Align.INLINE)
d.comment(0x8DBB, 'A = handle * 8', align=Align.INLINE)
d.comment(0x8DBC, 'X = stack pointer', align=Align.INLINE)
d.comment(0x8DBD, 'A = handle*8 + handle*4 = handle*12', align=Align.INLINE)
d.comment(0x8DC0, 'Y = offset into handle workspace', align=Align.INLINE)
d.comment(0x8DC1, 'Clean up stack (discard handle*4)', align=Align.INLINE)
d.comment(0x8DC2, 'Offset >= &48? (6 handles max)', align=Align.INLINE)
d.comment(0x8DC4, 'Valid: return with C clear', align=Align.INLINE)
d.comment(0x8DC6, 'Invalid: Y = 0', align=Align.INLINE)
d.comment(0x8DC8, 'A = 0, C set (error)', align=Align.INLINE)

d.label(0x8DC9, 'return_calc_handle')


d.subroutine(0x8DCA, 'net_2_read_handle_entry', title='*NET2: read handle entry from workspace', description="""Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""")


d.subroutine(0x8DE0, 'net_3_close_handle', title='*NET3: close handle (mark as unused)', description="""Looks up the handle in &F0 via calc_handle_offset. Writes
&3F ('?') to mark the handle slot as closed in the NFS
workspace. Preserves the carry flag state across the write
using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.""")


d.subroutine(0x8DF3, 'net_4_resume_remote', title='*NET4: resume after remote operation', description="""Calls resume_after_remote (&8146) to re-enable the keyboard
and send a completion notification. The BVC always branches
to clear_svc_return since resume_after_remote
returns with V clear (from CLV in prepare_cmd_clv).""")


d.subroutine(0x8DF8, 'svc_8_osword', title='Filing system OSWORD entry', description="""Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the
PHA/PHA/RTS dispatch at &8E02.""")
d.comment(0x8DF8, 'Command code from &EF', align=Align.INLINE)
d.comment(0x8DFA, 'Subtract &0F: OSWORD &0F-&13 become indices 0-4', align=Align.INLINE)


d.subroutine(0x8E02, 'fs_osword_dispatch', title='PHA/PHA/RTS dispatch for filing system OSWORDs', description="""X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
at &8E19 (low) / &8E1E (high).""")
d.comment(0x8E19, 'Dispatch table: low bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x8E1E, 'Dispatch table: high bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x80F9, 'Copy NMI handler code from ROM to RAM pages &04-&06')
d.comment(0x8113, 'Copy NMI workspace initialiser from ROM to &0016-&0076')


d.subroutine(0x8F73, 'econet_tx_rx', title='Econet transmit/receive handler', description="""A=0: Initialise TX control block from ROM template at &8311
     (zero entries substituted from NMI workspace &0DDA), transmit
     it, set up RX control block, and receive reply.
A>=1: Handle transmit result (branch to cleanup at &8F49).""", on_entry={'a': '0=set up and transmit, >=1=handle TX result'})
d.comment(0x8F73, 'A=0: set up and transmit; A>=1: handle result', align=Align.INLINE)
d.comment(0x8F79, 'Load from ROM template (zero = use NMI workspace value)', align=Align.INLINE)
d.comment(0x8FA4, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x8FAA, 'Dest station = &FFFF (accept reply from any station)', align=Align.INLINE)
d.comment(0x8FBC, 'Initiate receive with timeout', align=Align.INLINE)
d.comment(0x8FBF, 'Non-zero = error/timeout: jump to cleanup', align=Align.INLINE)
d.comment(0x8FD8, 'Receive data blocks until command byte = &00 or &0D', align=Align.INLINE)
d.comment(0x8FF0, 'Test for end-of-data marker (&0D)', align=Align.INLINE)


d.subroutine(0x9008, 'osword_dispatch', title='NETVEC dispatch handler (ENTRY)', description="""Indirected from NETVEC at &0224. Saves all registers and flags,
retrieves the reason code from the stacked A, and dispatches to
one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
&9021. Reason codes >= 9 are ignored.

Dispatch targets (from NFS09):
  0:   no-op (RTS)
  1-3: PRINT -- chars in printer buffer / Ctrl-B / Ctrl-C
  4:   NWRCH -- write character to screen (net write char)
  5:   SELECT -- printer selection changed
  6:   no-op (net read char -- not implemented)
  7:   NBYTE -- remote OSBYTE call
  8:   NWORD -- remote OSWORD call""", on_entry={'a': 'reason code (0-8)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'preserved'})
d.comment(0x900F, 'Retrieve original A (function code) from stack', align=Align.INLINE)
d.comment(0x9021, 'PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it', align=Align.INLINE)


d.subroutine(0x903E, 'net_write_char', title='Fn 4: net write character (NWRCH)', description="""Writes a character (passed in Y) to the screen via OSWRITCH.
Before the write, uses TSX to reach into the stack and zero the
carry flag in the caller's saved processor status byte -- ROR
followed by ASL on the stacked P byte (&0106,X) shifts carry
out and back in as zero. This ensures the calling code's PLP
restores carry=0, signalling "character accepted" without needing
a separate CLC/PHP sequence. A classic 6502 trick for modifying
return flags without touching the actual processor status.""", on_entry={'y': 'character to write'}, on_exit={'a': '&3F', 'x': '0', 'y': '0'})
d.comment(0x903F, 'ROR/ASL on stacked P: zeros carry to signal success', align=Align.INLINE)


d.subroutine(0x904C, 'setup_tx_and_send', title='Set up TX control block and send', description="""Builds a TX control block at (nfs_workspace)+&0C from the current
workspace state, then initiates transmission via the ADLC TX path.
This is the common send routine used after command data has been
prepared. The exact control block layout and field mapping need
further analysis.""", on_entry={'a': 'command type byte'})


d.subroutine(0x915A, 'ctrl_block_setup_alt', title='Alternate entry into control block setup', description="""Sets X=&0D, Y=&7C. Tests bit 6 of &833B to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")


d.subroutine(0x9163, 'ctrl_block_setup', title='Control block setup — main entry', description="""Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &918F indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")
d.comment(0x9168, 'Load template byte from ctrl_block_template[X]', align=Align.INLINE)


d.subroutine(0x918F, 'ctrl_block_template', title='Control block initialisation template', description="""Read by the loop at &9168, indexed by X from a starting value
down to 0. Values are stored into either (nfs_workspace) or
(net_rx_ptr) at offset Y, depending on the V flag.

Two entry paths read different slices of this table:
  ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
  ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &833B

Sentinel values:
  &FE = stop processing
  &FD = skip this offset (decrement Y but don't store)
  &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)""")
d.byte(0x918F, 1)
d.comment(0x918F, 'Alt-path only → Y=&6F', align=Align.INLINE)
d.byte(0x9190, 1)
d.comment(0x9190, 'Alt-path only → Y=&70', align=Align.INLINE)
d.byte(0x9191, 1)
d.comment(0x9191, 'SKIP', align=Align.INLINE)
d.byte(0x9192, 1)
d.comment(0x9192, 'SKIP', align=Align.INLINE)
d.byte(0x9193, 1)
d.comment(0x9193, '→ Y=&01 / Y=&73', align=Align.INLINE)
d.byte(0x9194, 1)
d.comment(0x9194, 'PAGE byte → Y=&02 / Y=&74', align=Align.INLINE)
d.byte(0x9195, 1)
d.comment(0x9195, '→ Y=&03 / Y=&75', align=Align.INLINE)
d.byte(0x9196, 1)
d.comment(0x9196, '→ Y=&04 / Y=&76', align=Align.INLINE)
d.byte(0x9197, 1)
d.comment(0x9197, '→ Y=&05 / Y=&77', align=Align.INLINE)
d.byte(0x9198, 1)
d.comment(0x9198, 'PAGE byte → Y=&06 / Y=&78', align=Align.INLINE)
d.byte(0x9199, 1)
d.comment(0x9199, '→ Y=&07 / Y=&79', align=Align.INLINE)
d.byte(0x919A, 1)
d.comment(0x919A, '→ Y=&08 / Y=&7A', align=Align.INLINE)
d.byte(0x919B, 1)
d.comment(0x919B, '→ Y=&09 / Y=&7B', align=Align.INLINE)
d.byte(0x919C, 1)
d.comment(0x919C, '→ Y=&0A / Y=&7C', align=Align.INLINE)
d.byte(0x919D, 1)
d.comment(0x919D, 'STOP — main-path boundary', align=Align.INLINE)
d.byte(0x919E, 1)
d.comment(0x919E, '→ Y=&0C (main only)', align=Align.INLINE)
d.byte(0x919F, 1)
d.comment(0x919F, '→ Y=&0D (main only)', align=Align.INLINE)
d.byte(0x91A0, 1)
d.comment(0x91A0, 'SKIP (main only)', align=Align.INLINE)
d.byte(0x91A1, 1)
d.comment(0x91A1, 'SKIP (main only)', align=Align.INLINE)
d.byte(0x91A2, 1)
d.comment(0x91A2, '→ Y=&10 (main only)', align=Align.INLINE)
d.byte(0x91A3, 1)
d.comment(0x91A3, 'PAGE byte → Y=&11 (main only)', align=Align.INLINE)
d.byte(0x91A4, 1)
d.comment(0x91A4, '→ Y=&12 (main only)', align=Align.INLINE)
d.byte(0x91A5, 1)
d.comment(0x91A5, '→ Y=&13 (main only)', align=Align.INLINE)
d.byte(0x91A6, 1)
d.comment(0x91A6, '→ Y=&14 (main only)', align=Align.INLINE)
d.byte(0x91A7, 1)
d.comment(0x91A7, 'PAGE byte → Y=&15 (main only)', align=Align.INLINE)
d.byte(0x91A8, 1)
d.comment(0x91A8, '→ Y=&16 (main only)', align=Align.INLINE)
d.byte(0x91A9, 1)
d.comment(0x91A9, '→ Y=&17 (main only)', align=Align.INLINE)


d.subroutine(0x8E23, 'copy_param_block', title='Bidirectional block copy between OSWORD param block and workspace.', description="""C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)""")
d.comment(0x8E23, 'C=0: workspace to param direction', align=Align.INLINE)
d.comment(0x8E25, 'Load byte from param block', align=Align.INLINE)
d.comment(0x8E27, 'Store to workspace', align=Align.INLINE)
d.comment(0x8E29, 'Always taken (C still set)', align=Align.INLINE)
d.comment(0x8E2B, 'Load byte from workspace', align=Align.INLINE)
d.comment(0x8E2F, 'Advance to next byte', align=Align.INLINE)
d.comment(0x8E30, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8E31, 'Loop while X >= 0', align=Align.INLINE)

d.label(0x8E33, 'return_copy_param')


d.subroutine(0x8E34, 'osword_0f_handler', title='OSWORD &0F handler: initiate transmit (CALLTX)', description="""Checks the TX semaphore (TXCLR at &0D62) via ASL -- if carry is
clear, a TX is already in progress and the call returns an error,
preventing user code from corrupting a system transmit. Otherwise
copies 16 bytes from the caller's OSWORD parameter block into the
user TX control block (UTXCB) in static workspace. The TXCB
pointer is copied to LTXCBP only after the semaphore is claimed,
ensuring the low-level transmit code (BRIANX) sees a consistent
pointer -- if copied before claiming, another transmitter could
modify TXCBP between the copy and the claim.""", on_entry={'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'corrupted', 'x': 'corrupted', 'y': '&FF'})


d.subroutine(0x8E54, 'osword_11_handler', title='OSWORD &11 handler: read JSR arguments (READRA)', description="""Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8E6B) to return just the buffer size and args size
without copying the data.""")


d.subroutine(0x8E7C, 'osword_12_handler', title='OSWORD &12 handler: read/set state information (RS)', description="""Dispatches on the sub-function code (0-9):
  0: read FS station (FSLOCN at &0E00)
  1: set FS station
  2: read printer server station (PSLOCN)
  3: set printer server station
  4: read protection masks (LSTAT at &D63)
  5: set protection masks
  6: read context handles (URD/CSD/LIB, converted from
     internal single-bit form back to handle numbers)
  7: set context handles (converted to internal form)
  8: read local station number
  9: read JSR arguments buffer size
Even-numbered sub-functions read; odd-numbered ones write.
Uses the bidirectional copy at &8E23 for station read/set.""")


d.subroutine(0x8EF1, 'osword_10_handler', title='OSWORD &10 handler: open/read RX control block (OPENRX)', description="""If the first byte of the caller's parameter block is zero, scans
for a free RXCB (flag byte = &3F = deleted) starting from RXCB #3
(RXCBs 0-2 are dedicated: printer, remote, FS). Returns the RXCB
number in the first byte, or zero if none free. If the first byte
is non-zero, reads the specified RXCB's data back into the caller's
parameter block (12 bytes) and then deletes the RXCB by setting
its flag byte to &3F -- a consume-once semantic so user code reads
received data and frees the CB in a single atomic operation,
preventing double-reads. The low-level user RX flag (LFLAG) is
temporarily disabled via ROR/ROL during the operation to prevent
the interrupt-driven receive code from modifying a CB that is
being read or opened.""", on_entry={'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'corrupted', 'x': 'corrupted', 'y': '&FF'})


d.subroutine(0x90FD, 'lang_1_remote_boot', title='Remote boot/execute handler', description="""Validates byte 4 of the RX control block (must be zero), copies the
2-byte execution address from RX offsets &80/&81 into NFS workspace,
sets up a control block, disables keyboard (OSBYTE &C9), then falls
through to lang_3_execute_at_0100.""")


d.subroutine(0x912B, 'lang_3_execute_at_0100', title='Execute downloaded code at &0100', description="""Zeroes &0100-&0102 (safe BRK default), restores the protection mask,
and JMP &0100 to execute code received over the network.""")


d.subroutine(0x913B, 'lang_4_remote_validated', title='Remote operation with source validation (REMOT)', description="""Validates that the source station/network in the received packet
matches the controlling station stored in the remote RXCB. This
ensures that only the station that initiated the remote session
can send commands — characters from other stations are rejected.
Full init sequence: 1) disable keyboard, 2) set workspace ptr,
3) set status busy, 4) set R/W/byte/word masks, 5) set up CB,
6) set MODE 7 (the only mode guaranteed for terminal emulation),
7) set auto repeat rates, 8) enter current language. This is
essentially a "thin terminal" setup — the local machine becomes
a remote display/keyboard for the controlling station.
Bit 0 of the status byte disallows further remote takeover
attempts (preventing re-entrant remote control), while bit 3
marks the machine as currently remoted.""")


d.subroutine(0x914B, 'lang_0_insert_remote_key', title='Insert remote keypress', description="""Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")


d.subroutine(0x8F58, 'setup_rx_buffer_ptrs', title='Set up RX buffer pointers in NFS workspace', description="""Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &28. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &2C.""", on_entry={'c': 'clear for ADC'})


d.subroutine(0x9064, 'remote_cmd_dispatch', title='Fn 7: remote OSBYTE handler (NBYTE)', description="""Full RPC mechanism for OSBYTE calls across the network. When a
machine is remoted, OSBYTE/OSWORD calls that affect terminal-side
hardware (keyboard scanning, flash rates, etc.) must be indirected
across the net. OSBYTE calls are classified into three categories:
  Y>0 (NCTBPL table): executed on BOTH machines (flash rates etc.)
  Y<0 (NCTBMI table): executed on terminal only, result sent back
  Y=0: not recognised, passed through unhandled
Results returned via stack manipulation: the saved processor status
byte at &0106 has V-flag (bit 6) forced on to tell the MOS the
call was claimed (preventing dispatch to other ROMs), and the I-bit
(bit 2) forced on to disable interrupts during register restoration,
preventing race conditions. The carry flag in the saved P is also
manipulated via ROR/ASL to zero it, signaling success to the caller.
OSBYTE &81 (INKEY) gets special handling as it must read the
terminal's keyboard.""")


d.subroutine(0x90B6, 'match_osbyte_code', title='Search remote OSBYTE table for match (NCALLP)', description="""Searches remote_osbyte_table for OSBYTE code A. X indexes the
last entry to check (table is scanned X..0). Returns Z=1 if
found. Called twice by remote_cmd_dispatch:

  X=7  -> first 8 entries (NCTBPL: execute on both machines)
  X=14 -> all 15 entries (NCTBMI: execute on terminal only)

The last 7 entries (&0B, &0C, &0F, &79, &7A, &E3, &E4) are terminal-only
because they affect the local keyboard, buffers, or function keys.

On entry: A = OSBYTE code, X = table size - 1
On exit:  Z=1 if match found, Z=0 if not""")


d.subroutine(0x90CE, 'remote_cmd_data', title='Fn 8: remote OSWORD handler (NWORD)', description="""Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget — no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")


d.subroutine(0x91B6, 'printer_select_handler', title='Fn 5: printer selection changed (SELECT)', description="""Called when the printer selection changes. Compares the new
selection (in PARMX) against the network printer (buffer 4).
If it matches, initialises the printer buffer pointer (PBUFFP)
and sets the initial flag byte (&41). Otherwise just updates
the printer status flags (PFLAGS).""", on_entry={'x': '1-based buffer number'})


d.subroutine(0x91C8, 'remote_print_handler', title='Fn 1/2/3: network printer handler (PRINT)', description="""Handles network printer output. Reason 1 = chars in buffer (extract
from MOS buffer 3 and accumulate), reason 2 = Ctrl-B (start print),
reason 3 = Ctrl-C (end print). The printer status byte PFLAGS uses:
  bit 7 = sequence number (toggles per packet for dup detection)
  bit 6 = always 1 (validity marker)
  bit 0 = 0 when print active
Print streams reuse the BSXMIT (byte-stream transmit) code with
handle=0, which causes the AND SEQNOS to produce zero and sidestep
per-file sequence tracking. After transmission, TXCB pointer bytes
are filled with &FF to prevent stale values corrupting subsequent
BGET/BPUT operations (a historically significant bug fix).
N.B. The printer and REMOTE facility share the same dynamically
allocated static workspace page via WORKP1 (&9E,&9F) — care must
be taken to never leave the pointer corrupted, as corruption would
cause one subsystem to overwrite the other's data.
Only handles buffer 4 (network printer); others are ignored.""", on_entry={'x': 'reason code (1=chars, 2=Ctrl-B, 3=Ctrl-C)', 'y': 'buffer number (must be 4 for network printer)'})


d.subroutine(0x91ED, 'store_output_byte', title='Store output byte to network buffer', description="""Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""", on_entry={'a': 'byte to store'}, on_exit={'y': 'buffer offset before store'})


d.subroutine(0x9218, 'flush_output_block', title='Flush output block', description="""Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")


d.subroutine(0x92DE, 'save_vdu_state', title='Save VDU workspace state', description="""Stores the cursor position value from &0355 into NFS workspace,
then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
each result into consecutive workspace bytes.""")


d.subroutine(0x966F, 'adlc_init', title='ADLC initialisation', description="""Reads station ID (INTOFF side effect), performs full ADLC reset,
checks for Tube presence (OSBYTE &EA), then falls through to
adlc_init_workspace.""")


d.subroutine(0x9681, 'adlc_init_workspace', title='Initialise NMI workspace', description="""Copies NMI shim from ROM to &0D00, stores current ROM bank number
into shim self-modifying code, sets TX status to &80 (idle/complete),
saves station ID from &FE18 into TX scout buffer, re-enables NMIs
by reading &FE20.""")


d.subroutine(0x969D, 'save_econet_state', title='Save Econet state to RX control block', description="""Stores rx_status_flags, protection_mask, and tx_in_progress
to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.""")


d.subroutine(0x96B4, 'restore_econet_state', title='Restore Econet state from RX control block', description="""Loads rx_status_flags, protection_mask, and tx_in_progress
from (net_rx_ptr) at offsets 8-10, then reinitialises via
adlc_init_workspace.""")


d.subroutine(0x96CD, 'install_nmi_shim', title='Copy NMI shim from ROM (&9FCA) to RAM (&0D00)', description='Copies 32 bytes. Interrupts are enabled during the copy.')


d.subroutine(0x0016, 'tube_brk_handler', title='Tube BRK handler (BRKV target) — reference: NFS11 NEWBR', description="""Sends error information to the Tube co-processor via R2 and R4:
  1. Sends &FF to R4 (WRIFOR) to signal error
  2. Reads R2 data (flush any pending byte)
  3. Sends &00 via R2, then error number from (&FD),0
  4. Loops sending error string bytes via R2 until zero terminator
  5. Falls through to tube_reset_stack → tube_main_loop
The main loop continuously polls R4 for WRCH requests (forwarded
to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
14-entry table at &0500). The R2 command byte is stored at &55
before dispatch via JMP (&0500).""")


d.subroutine(0x0400, 'tube_code_page4', title='Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)', description="""Copied from ROM (tube_code_page4) during init. The first 28 bytes (&0400-&041B)
overlap with the end of the ZP block (the same ROM bytes serve both
the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
  &0400: JMP &0473 (BEGIN — CLI parser / startup entry)
  &0403: JMP &06E2 (tube_escape_check)
  &0406: tube_addr_claim — Tube address claim protocol (ADRR)
  &0414: tube_post_init — called after ROM→RAM copy
  &0473: BEGIN — startup/CLI entry, break type check
  &04E7: tube_rdch_handler — RDCHV target
  &04EF: tube_restore_regs — restore X,Y, dispatch entry 6
  &04F7: tube_read_r2 — poll R2 status, read data byte to A""")


d.subroutine(0x0500, 'tube_dispatch_table', title='Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)', description="""Copied from ROM (tube_dispatch_table) during init. Contains:
  &0500: tube_dispatch_table — 14-entry handler address table
  &051C: tube_wrch_handler — WRCHV target
  &051F: tube_send_and_poll — send byte via R2, poll for reply
  &0527: tube_poll_r4_wrch — service R4 WRCH while waiting for R2
  &053D: tube_release_return — restore regs and RTS
  &0543: tube_osbput — write byte to file
  &0550: tube_osbget — read byte from file
  &055B: tube_osrdch — read character
  &0569: tube_osfind — open file
  &0580: tube_osfind_close — close file (A=0)
  &058C: tube_osargs — file argument read/write
  &05B1: tube_read_string — read CR-terminated string into &0700
  &05C5: tube_oscli — execute * command
  &05CB: tube_reply_ack — send &7F acknowledge
  &05CD: tube_reply_byte — send byte and return to main loop
  &05D8: tube_osfile — whole file operation""")


d.subroutine(0x0600, 'tube_code_page6', title='Tube host code page 6 — reference: NFS13 (GBPB-ESCA)', description="""Copied from ROM (tube_code_page6) during init. &0600-&0601 is the tail
of tube_osfile (BEQ to tube_reply_byte when done). Contains:
  &0602: tube_osgbpb — multi-byte file I/O
  &0626: tube_osbyte_short — 2-param OSBYTE (returns X)
  &063B: tube_osbyte_long — 3-param OSBYTE (returns carry+Y+X)
  &065D: tube_osword — variable-length OSWORD (buffer at &0130)
  &06A3: tube_osword_rdln — OSWORD 0 (read line, 5-byte params)
  &06BB: tube_rdln_send_line — send input line from &0700
  &06D0: tube_send_r2 — poll R2 status, write A to R2 data
  &06D9: tube_send_r4 — poll R4 status, write A to R4 data
  &06E2: tube_escape_check — check &FF, forward escape to R1
  &06E8: tube_event_handler — EVNTV: forward event (A,X,Y) via R1
  &06F7: tube_send_r1 — poll R1 status, write A to R1 data""")

d.label(0x9305, 'osbyte_vdu_table')
d.comment(0x9305, '3-entry OSBYTE table for lang_2_save_palette_vdu (&9292)')
d.byte(0x9305, 1)
d.comment(0x9305, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.byte(0x9306, 1)
d.comment(0x9306, 'OSBYTE &C2: read shadow RAM allocation', align=Align.INLINE)
d.byte(0x9307, 1)
d.comment(0x9307, 'OSBYTE &C3: read screen start address', align=Align.INLINE)


d.subroutine(0x9249, 'econet_tx_retry', title='Transmit with retry loop (XMITFS/XMITFY)', description="""Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
retries and FSDELY (&60 = 96) ms delay between attempts. On each
iteration, checks the result code: zero means success, non-zero
means retry. After all retries exhausted, reports a 'Net error'.
Entry point XMITFY allows a custom delay in Y.""", on_entry={'a': 'handle bitmask (0=printer, non-zero=file)', 'x': 'TX control block address low', 'y': 'TX control block address high'})


d.subroutine(0x9292, 'lang_2_save_palette_vdu', title='Save palette and VDU state (CVIEW)', description="""Part of the VIEW facility (second iteration, started 27/7/82).
Uses dynamically allocated buffer store. The WORKP1 pointer
(&9E,&9F) serves double duty: non-zero indicates data ready AND
provides the buffer address — an efficient use of scarce zero-
page space. This code must be user-transparent as the NFS may not
be the dominant filing system.
Reads all 16 palette entries using OSWORD &0B (read palette) and
stores the results. Then reads cursor position (OSBYTE &85),
shadow RAM allocation (OSBYTE &C2), and screen start address
(OSBYTE &C3) using the 3-entry table at &9305 (osbyte_vdu_table).
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")


d.subroutine(0x99BB, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")


d.subroutine(0x9A59, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Handles immediate (non-data-transfer) operations received via
scout frames with port byte = 0. The control byte (&0D3F)
determines the operation type:
  &81 = PEEK (read memory)
  &82 = POKE (write memory)
  &83 = JSR (remote procedure call)
  &84 = user procedure
  &85 = OS procedure
  &86 = HALT
  &87 = CONTINUE
The protection mask (LSTAT at &D63) controls which operations
are permitted — each bit enables or disables an operation type.
If the operation is not permitted by the mask, it is silently
ignored. LSTAT can be read/set via OSWORD &12 sub-functions 4/5.""")


d.subroutine(0x9A34, 'discard_reset_listen', title='Discard with full ADLC reset', description="""Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
then falls through to discard_after_reset. Used when the ADLC is
in an unexpected state and needs a hard reset before returning
to idle listen mode. 5 references — the main error recovery path.""")


d.subroutine(0x9A40, 'discard_listen', title='Discard frame (gentle)', description="""Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
current frame reception without a full reset, then falls through
to discard_after_reset. Used for clean rejection of frames that
are correctly formatted but not for us (wrong station/network).""")


d.subroutine(0x9A43, 'discard_after_reset', title='Return to idle listen after reset/discard', description="""Just calls adlc_rx_listen (CR1=&82, CR2=&67) to re-enter idle
RX mode, then RTI. The simplest of the three discard paths —
used as the tail of both discard_reset_listen and discard_listen.""")
d.comment(0x9F4B, 'Unreferenced data block (purpose unknown)')
d.byte(0x9F4B, 16)


d.subroutine(0x9F5B, 'tx_calc_transfer', title='Calculate transfer size', description="""Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")
d.comment(0x9F5B, 'Load RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x9F60, 'AND with TX block[7] (byte 3)', align=Align.INLINE)
d.comment(0x9F62, 'Both &FF = no buffer?', align=Align.INLINE)
d.comment(0x9F64, 'Yes: fallback path', align=Align.INLINE)
d.comment(0x9F69, 'No: fallback path', align=Align.INLINE)
d.comment(0x9F6E, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x9F73, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9F74, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9F75, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x9F77, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x9F79, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x9F7D, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x9F7E, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x9F80, 'Store result byte', align=Align.INLINE)
d.comment(0x9F83, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x9F86, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9F87, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x9F89, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9F8B, 'Discard final borrow', align=Align.INLINE)
d.comment(0x9F8E, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x9F93, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x9F94, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x9F96, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x9F9B, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x9F9D, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x9FA3, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x9FA4, 'Restore X', align=Align.INLINE)
d.comment(0x9FA9, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x9FAE, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x9FB0, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x9FB4, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x9FBC, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x9FC7, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x9FC9, 'Return with C=1', align=Align.INLINE)


d.subroutine(0x9FCB, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&96F6). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &96F6.""")


d.subroutine(0x9FD9, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""A version of the NMI vector-setting subroutine and RTI sequence
that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
one normally used at runtime; this ROM copy is used during early
initialisation before the RAM workspace has been set up, and as
the source for the initial copy to RAM.""")


d.subroutine(0x96DC, 'adlc_full_reset', title='ADLC full reset', description='Aborts all activity and returns to idle RX listen mode.')
d.comment(0x96DC, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x96E1, 'CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding', align=Align.INLINE)
d.comment(0x96E6, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)


d.subroutine(0x96EB, 'adlc_rx_listen', title='Enter RX listen mode', description='TX held in reset, RX active with interrupts. Clears all status.')
d.comment(0x96EB, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x96F0, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)


d.subroutine(0x96F6, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")
d.comment(0x96F6, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x96F8, 'BIT SR2: Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x96FB, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x96FD, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x9700, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x9703, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x9705, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x9707, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x9709, 'Flag &40 = broadcast frame', align=Align.INLINE)
d.comment(0x970E, 'Install next NMI handler at &9715 (RX scout second byte)', align=Align.INLINE)


d.subroutine(0x9715, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &9747.""")
d.comment(0x9715, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x9718, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x971A, 'Read destination network byte', align=Align.INLINE)
d.comment(0x971D, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x971F, 'EOR &FF: test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x9721, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x9723, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x972B, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x972E, 'Store Y offset for scout data buffer', align=Align.INLINE)
d.comment(0x9730, 'Install scout data reading loop at &9747', align=Align.INLINE)


d.subroutine(0x9737, 'scout_error', title='Scout error/discard handler', description="""Reached when the scout data loop sees no RDA (BPL at &974C) or
when scout completion finds unexpected SR2 state.
If SR2 & &81 is non-zero (AP or RDA still active), performs full
ADLC reset and discards. If zero (clean end), discards via &9A40.
This path is a common landing for any unexpected ADLC state during
scout reception.""")
d.comment(0x9737, 'Read SR2', align=Align.INLINE)
d.comment(0x973A, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x973E, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x9741, 'Discard and return to idle', align=Align.INLINE)


d.subroutine(0x9747, 'scout_data_loop', title='Scout data reading loop', description="""Reads the body of a scout frame, two bytes per iteration. Stores
bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
Between each pair it checks SR2:
  - At entry (&9749): LDA SR2, BPL tests RDA (bit7)
    - No RDA (BPL) -> error (&9737)
    - RDA set (BMI) -> read byte
  - After first byte (&9755): LDA SR2
    - RDA set (BMI) -> read second byte
    - SR2 non-zero (BNE) -> scout completion (&9771)
      This is the FV detection point: when FV is set (by inline refill
      of the last byte during the preceding RX FIFO read), SR2 is
      non-zero and the branch is taken.
    - SR2 = 0 -> RTI, wait for next NMI
  - After second byte (&9769): LDA SR2
    - SR2 non-zero (BNE) -> loop back to &974C
    - SR2 = 0 -> RTI, wait for next NMI
The loop ends at Y=&0C (12 bytes max in scout buffer).""")
d.comment(0x9747, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x9749, 'Read SR2', align=Align.INLINE)
d.comment(0x974E, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x9751, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x9754, 'Advance buffer index', align=Align.INLINE)
d.comment(0x9755, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x9758, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x975A, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x975C, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x975F, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x9762, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x9765, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x9767, 'Save Y for next iteration', align=Align.INLINE)
d.comment(0x9769, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x976C, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x976E, 'SR2 = 0 -- RTI, wait for next NMI', align=Align.INLINE)


d.subroutine(0x9771, 'scout_complete', title='Scout completion handler', description="""Reached from the scout data loop when SR2 is non-zero (FV detected).
Disables PSE to allow individual SR2 bit testing:
  CR1=&00 (clear all enables)
  CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
Then checks FV (bit1) and RDA (bit7):
  - No FV (BEQ) -> error &9737 (not a valid frame end)
  - FV set, no RDA (BPL) -> error &9737 (missing last byte)
  - FV set, RDA set -> read last byte, process scout
After reading the last byte, the complete scout buffer (&0D3D-&0D48)
contains: src_stn, src_net, ctrl, port [, extra_data...].
The port byte at &0D40 determines further processing:
  - Port = 0 -> immediate operation (&9A59)
  - Port non-zero -> check if it matches an open receive block""")
d.comment(0x9771, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x9776, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x977B, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x977D, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x9780, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x9782, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x9784, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x9787, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x978A, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x978F, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x9792, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x9794, 'Port = 0 -- immediate operation handler', align=Align.INLINE)


d.subroutine(0x9839, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &9839 (AP+addr check) -> &984F (net=0 check) ->
&9865 (skip ctrl+port) -> &989A (bulk data read) -> &98CE (completion)""")
d.comment(0x982D, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x984F, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x9865, 'Skip control and port bytes (already known from scout)', align=Align.INLINE)
d.comment(0x986A, 'Discard control byte', align=Align.INLINE)
d.comment(0x986D, 'Discard port byte', align=Align.INLINE)


d.subroutine(0x989A, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &98CE.
SR2 = 0 -> RTI, wait for next NMI to continue.""")
d.comment(0x989A, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x989C, 'Read SR2 for next pair', align=Align.INLINE)


d.subroutine(0x98CE, 'data_rx_complete', title='Data frame completion', description="""Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&9771): disables PSE (CR1=&00,
CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &995E.""")
d.comment(0x98CE, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x98D3, 'CR2=&84: disable PSE for individual bit testing', align=Align.INLINE)
d.comment(0x98DA, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x98DC, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x98DF, 'No FV -- error', align=Align.INLINE)
d.comment(0x98E1, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x98E7, 'FV+RDA: read and store last data byte', align=Align.INLINE)


d.subroutine(0x995E, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&9F39).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x9966, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x996B, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9970, 'Install saved next handler (&99BB for scout ACK)', align=Align.INLINE)
d.comment(0x997A, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x997D, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9980, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9982, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x9985, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x998B, 'Install handler at &9992 (write src addr)', align=Align.INLINE)


d.subroutine(0x9992, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x9992, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x9995, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x9998, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x999A, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x999D, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x99A7, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x99AC, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)


d.subroutine(0x9C48, 'inactive_poll', title='INACTIVE polling loop', description="""Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9C66-&9C6B works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")
d.comment(0x9C4D, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9C4F, 'A=&04: INACTIVE mask for SR2 bit2', align=Align.INLINE)
d.comment(0x9C53, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x9C56, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x9C59, 'BIT SR2: Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x9C5C, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x9C5E, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x9C61, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9C66, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x9C68, 'BIT SR1: tests CTS present', align=Align.INLINE)
d.comment(0x9C6B, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x9C6D, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x9C71, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x9C84, 'TX_ACTIVE branch (A=&44 = CR1 value for TX active)')


d.subroutine(0x9C88, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")
d.comment(0x9C88, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x9C90, "Error &40 = 'Line Jammed'", align=Align.INLINE)


d.subroutine(0x9CA2, 'tx_prepare', title='TX preparation', description="""Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9D4C, and re-enables NMIs.""")
d.comment(0x9CA2, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9CA5, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x9CAA, 'Install NMI handler at &9D4C (TX data handler)', align=Align.INLINE)
d.comment(0x9CB4, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)


d.subroutine(0x9D4C, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")
d.comment(0x9D4C, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x9D4F, 'BIT SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x9D52, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x9D54, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x9D57, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x9D62, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x9D65, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x9D68, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9D6A, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x9D6D, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x9D6F, 'RTI -- wait for next NMI', align=Align.INLINE)
d.comment(0x9D72, 'TX error path')
d.comment(0x9D72, 'Error &42', align=Align.INLINE)
d.comment(0x9D76, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x9D7B, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x9D7D, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x9D80, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)
d.comment(0x9D85, 'Jump to error handler', align=Align.INLINE)


d.subroutine(0x9D88, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &9D94 which switches to RX mode.
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)""")
d.comment(0x9D88, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x9D8D, 'Install NMI handler at &9D94 (TX completion)', align=Align.INLINE)


d.subroutine(0x9D94, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> completion at &9F39
  - bit0 set at &0D4A -> four-way handshake data phase at &9EDD
  - Otherwise -> install RX reply handler at &9DB2""")
d.comment(0x9D94, 'CR1=&82: TX_RESET | RIE (now in RX mode)', align=Align.INLINE)
d.comment(0x9D99, 'Test workspace flags', align=Align.INLINE)
d.comment(0x9D9C, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x9D9E, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x9DA8, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)
d.comment(0x9DAB, 'Install RX reply handler at &9DB2', align=Align.INLINE)


d.subroutine(0x9DB2, 'nmi_reply_scout', title='RX reply scout handler', description="""Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")
d.comment(0x9DB2, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x9DB4, 'BIT SR2: test AP (Address Present)', align=Align.INLINE)
d.comment(0x9DB7, 'No AP -- error', align=Align.INLINE)
d.comment(0x9DBC, 'Compare to our station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9DBF, 'Not our station -- error/reject', align=Align.INLINE)
d.comment(0x9DC1, 'Install next handler at &9DC8 (reply continuation)', align=Align.INLINE)


d.subroutine(0x9DC8, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs &9DE3 for the
remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DD9.
If IRQ is still set, falls through directly to &9DE3 without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")
d.comment(0x9DC8, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x9DCB, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9DCD, 'Read destination network byte', align=Align.INLINE)
d.comment(0x9DD0, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9DD2, 'Install next handler at &9DE3 (reply validation)', align=Align.INLINE)
d.comment(0x9DD6, 'BIT SR1: test IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x9DDB, 'IRQ not set -- install handler and RTI', align=Align.INLINE)


d.subroutine(0x9DE3, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &9DE3 -- must see data available
  2. Read source station at &9DE8, compare to &0D20 (tx_dst_stn)
  3. Read source network at &9DF0, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &9DFA -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")
d.comment(0x9DE3, 'BIT SR2: test RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x9DE6, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x9DE8, 'Read source station', align=Align.INLINE)
d.comment(0x9DEB, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x9DEE, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x9DF0, 'Read source network', align=Align.INLINE)
d.comment(0x9DF3, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x9DF6, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9DF8, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9DFA, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9DFD, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x9DFF, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x9E04, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x9E09, 'Install next handler at &9EDD (four-way data phase) into &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x9E13, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x9E16, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9E19, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E1B, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x9E24, 'Install handler at &9E2B (write src addr for scout ACK)', align=Align.INLINE)


d.subroutine(0x9E2B, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
d.comment(0x9E33, 'Write our station to TX FIFO', align=Align.INLINE)


d.subroutine(0x9E50, 'nmi_data_tx', title='TX data phase: send payload', description="""Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9D4C but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
d.comment(0x9E50, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x9E52, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9E55, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E57, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E7D, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)


d.subroutine(0x9EDD, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9EE9 to receive the final ACK from the remote station.""")
d.comment(0x9EDD, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)
d.comment(0x9EE2, 'Install handler at &9EE9 (RX final ACK)', align=Align.INLINE)


d.subroutine(0x9EE9, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9DB2-&9DE3):
  &9EE9: Check AP, read dest_stn, compare to our station
  &9EFF: Check RDA, read dest_net, validate = 0
  &9F15: Check RDA, read src_stn/net, compare to TX dest
  &9F32: Check FV for frame completion
On success, stores result=0 at &9F39. On any failure, error &41.""")
d.comment(0x9EE9, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x9EEB, 'BIT SR2: test AP', align=Align.INLINE)
d.comment(0x9EEE, 'No AP -- error', align=Align.INLINE)
d.comment(0x9EF0, 'Read dest station', align=Align.INLINE)
d.comment(0x9EF3, 'Compare to our station (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9EF6, 'Not our station -- error', align=Align.INLINE)
d.comment(0x9EF8, 'Install handler at &9EFF (final ACK continuation)', align=Align.INLINE)
d.comment(0x9EFF, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9F02, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9F04, 'Read dest network', align=Align.INLINE)
d.comment(0x9F07, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9F09, 'Install handler at &9F15 (final ACK validation)', align=Align.INLINE)
d.comment(0x9F0D, 'BIT SR1: test IRQ -- more data ready?', align=Align.INLINE)


d.subroutine(0x9F15, 'nmi_final_ack_validate', title='Final ACK validation', description="""Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
d.comment(0x9F15, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9F18, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9F1A, 'Read source station', align=Align.INLINE)
d.comment(0x9F1D, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x9F20, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9F22, 'Read source network', align=Align.INLINE)
d.comment(0x9F25, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x9F28, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9F32, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9F34, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9F37, 'No FV -- error', align=Align.INLINE)


d.subroutine(0x9F39, 'tx_result_ok', title='TX completion handler', description="""Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls full ADLC reset + idle listen via &9A34.""")
d.comment(0x9F39, 'A=0: success result code', align=Align.INLINE)
d.comment(0x9F3B, 'BEQ: always taken (A=0)', align=Align.INLINE)


d.subroutine(0x9F3F, 'tx_store_result', title='TX error handler', description="""Stores error code (A) into the TX control block, sets &0D3A bit7
for completion, and returns to idle via &9A34.
Error codes: &00=success, &40=line jammed, &41=not listening,
&42=net error.""")
d.comment(0x9F3F, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x9F41, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x9F43, '&80: completion flag for &0D3A', align=Align.INLINE)
d.comment(0x9F45, 'Signal TX complete', align=Align.INLINE)
d.comment(0x9F48, 'Full ADLC reset and return to idle listen', align=Align.INLINE)

d.label(0x0000, 'zp_ptr_lo')

d.label(0x0001, 'zp_ptr_hi')

d.label(0x0002, 'zp_work_2')

d.label(0x0003, 'zp_work_3')

d.label(0x0012, 'tube_data_ptr')

d.label(0x0013, 'tube_data_ptr_hi')

d.label(0x0014, 'tube_claim_flag')

d.label(0x0015, 'tube_claimed_id')
d.comment(0x0016, 'A=&FF: signal error to co-processor via R4', align=Align.INLINE)
d.comment(0x0018, 'Send &FF error signal to Tube R4', align=Align.INLINE)
d.comment(0x001B, 'Flush any pending R2 byte', align=Align.INLINE)
d.comment(0x001E, 'A=0: send zero prefix to R2', align=Align.INLINE)
d.comment(0x0020, 'Send zero prefix byte via R2', align=Align.INLINE)
d.comment(0x0023, 'Y=0: start of error block at (&FD)', align=Align.INLINE)
d.comment(0x0024, 'Load error number from (&FD),0', align=Align.INLINE)
d.comment(0x0026, 'Send error number via R2', align=Align.INLINE)
d.comment(0x0029, 'Advance to next error string byte', align=Align.INLINE)

d.label(0x002A, 'tube_send_error_byte')
d.comment(0x002A, 'Load next error string byte', align=Align.INLINE)
d.comment(0x002C, 'Send error string byte via R2', align=Align.INLINE)
d.comment(0x002F, 'Zero byte = end of error string', align=Align.INLINE)
d.comment(0x0030, 'Loop until zero terminator sent', align=Align.INLINE)
d.comment(0x0032, 'Reset stack pointer to top', align=Align.INLINE)
d.comment(0x0034, 'TXS: set stack pointer from X', align=Align.INLINE)
d.comment(0x0035, 'Enable interrupts for main loop', align=Align.INLINE)
d.comment(0x003A, 'BIT R4 status: check WRCH request', align=Align.INLINE)
d.comment(0x003D, 'R1 not ready: check R2 instead', align=Align.INLINE)
d.comment(0x003F, 'Read character from Tube R4 data', align=Align.INLINE)
d.comment(0x0045, 'BIT R2 status: check command byte', align=Align.INLINE)
d.comment(0x0048, 'R2 not ready: loop back to R1 check', align=Align.INLINE)
d.comment(0x004A, 'Re-check R4: WRCH has priority over R2', align=Align.INLINE)
d.comment(0x004D, 'R1 ready: handle WRCH first', align=Align.INLINE)
d.comment(0x004F, 'Read command byte from Tube R2 data', align=Align.INLINE)
d.comment(0x0052, 'Self-modify JMP low byte for dispatch', align=Align.INLINE)
d.comment(0x0054, 'Dispatch to handler via indirect JMP', align=Align.INLINE)

d.label(0x0058, 'tube_xfer_page')

d.label(0x0059, 'tube_xfer_addr_2')

d.label(0x005A, 'tube_xfer_addr_3')

d.label(0x0099, 'prot_flags')

d.label(0x00A8, 'ws_page')

d.label(0x00A9, 'svc_state')

d.label(0x00AA, 'osword_flag')

d.label(0x00AB, 'ws_ptr_lo')

d.label(0x00AC, 'ws_ptr_hi')

d.label(0x00AD, 'table_idx')

d.label(0x00AE, 'work_ae')

d.label(0x00AF, 'addr_work')

d.label(0x00B3, 'fs_load_addr_3')

d.label(0x00B4, 'fs_work_4')

d.label(0x00B5, 'fs_work_5')

d.label(0x00B7, 'fs_work_7')

d.label(0x00B9, 'fs_crflag')

d.label(0x00BA, 'fs_spool_handle')

d.label(0x00C0, 'txcb_ctrl')

d.label(0x00C1, 'txcb_port')

d.label(0x00C2, 'txcb_dest')

d.label(0x00C4, 'txcb_start')

d.label(0x00C7, 'txcb_pos')

d.label(0x00C8, 'txcb_end')

d.label(0x00CF, 'fs_spool0')

d.label(0x00EF, 'osbyte_a_copy')

d.label(0x00F0, 'osword_pb_ptr')

d.label(0x00F1, 'osword_pb_ptr_hi')

d.label(0x00F3, 'os_text_ptr_hi')

d.label(0x00F7, 'osrdsc_ptr_hi')

d.label(0x00FD, 'brk_ptr')

d.label(0x00FF, 'escape_flag')
d.comment(0x0400, 'JMP to BEGIN startup entry', align=Align.INLINE)
d.comment(0x0403, 'JMP to tube_escape_check (&06A7)', align=Align.INLINE)
d.comment(0x0406, 'A>=&80: address claim; A<&80: data transfer', align=Align.INLINE)
d.comment(0x0408, 'A<&80: data transfer setup (SENDW)', align=Align.INLINE)
d.comment(0x040A, 'A>=&C0: new address claim from another host', align=Align.INLINE)
d.comment(0x040C, 'C=1: external claim, check ownership', align=Align.INLINE)
d.comment(0x040E, 'Map &80-&BF range to &C0-&FF for comparison', align=Align.INLINE)
d.comment(0x0410, 'Is this for our currently-claimed address?', align=Align.INLINE)
d.comment(0x0412, 'Not our address: return', align=Align.INLINE)
d.comment(0x0416, 'Store to claim-in-progress flag', align=Align.INLINE)
d.comment(0x0418, 'Return from tube_post_init', align=Align.INLINE)

d.label(0x0419, 'addr_claim_external')
d.comment(0x0419, "Another host claiming; check if we're owner", align=Align.INLINE)
d.comment(0x041B, 'C=1: we have an active claim', align=Align.INLINE)
d.comment(0x041D, 'Compare with our claimed address', align=Align.INLINE)
d.comment(0x041F, 'Match: return (we already have it)', align=Align.INLINE)
d.comment(0x0421, "Not ours: CLC = we don't own this address", align=Align.INLINE)
d.comment(0x0422, 'Return with C=0 (claim denied)', align=Align.INLINE)

d.label(0x0423, 'accept_new_claim')
d.comment(0x0423, 'Accept new claim: update our address', align=Align.INLINE)
d.comment(0x0425, 'Return with address updated', align=Align.INLINE)
d.comment(0x0426, 'Save 16-bit transfer address from (X,Y)', align=Align.INLINE)
d.comment(0x0428, 'Store address pointer low byte', align=Align.INLINE)
d.comment(0x042A, 'Send transfer type byte to co-processor', align=Align.INLINE)
d.comment(0x042D, 'X = transfer type for table lookup', align=Align.INLINE)
d.comment(0x042E, 'Y=3: send 4 bytes (address + claimed addr)', align=Align.INLINE)

d.label(0x0430, 'send_xfer_addr_bytes')
d.comment(0x0430, 'Load transfer address byte from (X,Y)', align=Align.INLINE)
d.comment(0x0432, 'Send address byte to co-processor via R4', align=Align.INLINE)
d.comment(0x0435, 'Previous byte (big-endian: 3,2,1,0)', align=Align.INLINE)
d.comment(0x0436, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x0459, 'Not SENDW type: skip release path', align=Align.INLINE)
d.comment(0x0461, 'Restart Tube main loop', align=Align.INLINE)
d.comment(0x047A, 'Init: start sending from &8000', align=Align.INLINE)
d.comment(0x047C, 'Store &80 as source page high byte', align=Align.INLINE)
d.comment(0x047E, 'Store &80 as page counter initial value', align=Align.INLINE)
d.comment(0x0480, 'A=&20: bit 5 mask for ROM type check', align=Align.INLINE)
d.comment(0x0482, 'ROM type bit 5: reloc address in header?', align=Align.INLINE)
d.comment(0x0485, 'No reloc addr: use defaults', align=Align.INLINE)
d.comment(0x0487, 'Skip past copyright string to find reloc addr', align=Align.INLINE)

d.label(0x048A, 'scan_copyright_end')
d.comment(0x048A, 'Skip past null-terminated copyright string', align=Align.INLINE)
d.comment(0x048B, 'Load next byte from ROM header', align=Align.INLINE)
d.comment(0x048E, 'Loop until null terminator found', align=Align.INLINE)
d.comment(0x0490, 'Read 4-byte reloc address from ROM header', align=Align.INLINE)
d.comment(0x0493, 'Store reloc addr byte 1 as transfer addr', align=Align.INLINE)
d.comment(0x0495, 'Load reloc addr byte 2', align=Align.INLINE)
d.comment(0x0498, 'Store as source page start', align=Align.INLINE)
d.comment(0x049A, 'Load reloc addr byte 3', align=Align.INLINE)
d.comment(0x049D, 'Load reloc addr byte 4 (highest)', align=Align.INLINE)

d.label(0x04A0, 'store_xfer_end_addr')
d.comment(0x04A0, 'Store high byte of end address', align=Align.INLINE)
d.comment(0x04A2, 'Store byte 3 of end address', align=Align.INLINE)
d.comment(0x0546, 'Y=channel handle from R2', align=Align.INLINE)
d.comment(0x0547, 'Read data byte from R2 for BPUT', align=Align.INLINE)

d.label(0x054A, 'tube_poll_r1_wrch')
d.comment(0x054D, 'BPUT done: send acknowledge, return', align=Align.INLINE)
d.comment(0x0553, 'Y=channel handle for OSBGET', align=Align.INLINE)
d.comment(0x0566, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x056C, 'A=0: close file, else open with filename', align=Align.INLINE)
d.comment(0x056E, 'Save open mode while reading filename', align=Align.INLINE)
d.comment(0x056F, 'Read filename string from R2 into &0700', align=Align.INLINE)
d.comment(0x0572, 'Recover open mode from stack', align=Align.INLINE)
d.comment(0x057D, 'Send file handle result to co-processor', align=Align.INLINE)
d.comment(0x0580, 'OSFIND close: read handle from R2', align=Align.INLINE)
d.comment(0x0583, 'Y=handle to close', align=Align.INLINE)
d.comment(0x0584, 'A=0: close command for OSFIND', align=Align.INLINE)
d.comment(0x0589, 'Close done: send acknowledge, return', align=Align.INLINE)
d.comment(0x058F, 'Y=file handle for OSARGS', align=Align.INLINE)
d.comment(0x0590, 'Read 4-byte arg + reason from R2 into ZP', align=Align.INLINE)

d.label(0x0592, 'read_osargs_params')
d.comment(0x0592, 'Read next param byte from R2', align=Align.INLINE)
d.comment(0x0595, 'Params stored at &00-&03 (little-endian)', align=Align.INLINE)
d.comment(0x0597, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x059B, 'Read OSARGS reason code from R2', align=Align.INLINE)
d.comment(0x05A1, 'Send result A back to co-processor', align=Align.INLINE)
d.comment(0x05A4, 'Return 4-byte result from ZP &00-&03', align=Align.INLINE)

d.label(0x05A6, 'send_osargs_result')
d.comment(0x05A6, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x05A8, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05AB, 'Previous byte (count down)', align=Align.INLINE)
d.comment(0x05AC, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x05AE, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x05B1, 'X=0: initialise string buffer index', align=Align.INLINE)
d.comment(0x05B3, 'Y=0: string buffer offset 0', align=Align.INLINE)
d.comment(0x05B5, 'Read next string byte from R2', align=Align.INLINE)
d.comment(0x05B8, 'Store byte in string buffer at &0700+Y', align=Align.INLINE)
d.comment(0x05BB, 'Next buffer position', align=Align.INLINE)
d.comment(0x05BC, 'Y overflow: string too long, truncate', align=Align.INLINE)
d.comment(0x05BE, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x05C0, 'Not CR: continue reading string', align=Align.INLINE)

d.label(0x05C2, 'string_buf_done')
d.comment(0x05C2, 'Y=7: set XY=&0700 for OSCLI/OSFIND', align=Align.INLINE)
d.comment(0x05C4, 'Return with XY pointing to &0700', align=Align.INLINE)
d.comment(0x05C8, 'Execute * command via OSCLI', align=Align.INLINE)
d.comment(0x05CB, '&7F = success acknowledgement', align=Align.INLINE)
d.comment(0x05CD, 'Poll R2 status until ready', align=Align.INLINE)
d.comment(0x05D0, 'Bit 6 clear: not ready, loop', align=Align.INLINE)
d.comment(0x05D2, 'Write byte to R2 data register', align=Align.INLINE)
d.comment(0x05D5, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x05DA, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05DD, 'Store at &01+X (descending)', align=Align.INLINE)
d.comment(0x05DF, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05E0, 'Loop for all 16 bytes', align=Align.INLINE)
d.comment(0x05E2, 'Read filename string from R2 into &0700', align=Align.INLINE)
d.comment(0x05E5, 'XY=&0700: filename pointer for OSFILE', align=Align.INLINE)
d.comment(0x05E7, 'Store Y=7 as pointer high byte', align=Align.INLINE)
d.comment(0x05E9, 'Y=0 for OSFILE control block offset', align=Align.INLINE)
d.comment(0x05EB, 'Read OSFILE reason code from R2', align=Align.INLINE)
d.comment(0x05EE, 'Execute OSFILE operation', align=Align.INLINE)
d.comment(0x05F3, 'Send result A (object type) to co-processor', align=Align.INLINE)
d.comment(0x05F6, 'Return 16-byte control block to co-processor', align=Align.INLINE)

d.label(0x05F8, 'send_osfile_ctrl_blk')
d.comment(0x05F8, 'Load control block byte', align=Align.INLINE)
d.comment(0x05FA, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05FD, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05FE, 'Loop for all 16 bytes', align=Align.INLINE)
d.comment(0x0635, 'Send X result for 2-param OSBYTE', align=Align.INLINE)
d.comment(0x0649, 'Test for OSBYTE &9D (fast Tube BPUT)', align=Align.INLINE)
d.comment(0x064B, 'OSBYTE &9D (fast Tube BPUT): no result needed', align=Align.INLINE)
d.comment(0x064F, 'Encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x0658, 'Send Y result, then fall through to send X', align=Align.INLINE)
d.comment(0x0666, 'Read param block length from R2', align=Align.INLINE)
d.comment(0x0669, 'DEX: length 0 means no params to read', align=Align.INLINE)
d.comment(0x0674, 'Store param bytes into block at &0130', align=Align.INLINE)
d.comment(0x067A, 'Restore OSWORD number from Y', align=Align.INLINE)

d.label(0x067B, 'skip_param_read')
d.comment(0x067B, 'XY=&0130: param block address for OSWORD', align=Align.INLINE)

d.label(0x0687, 'poll_r2_osword_result')
d.comment(0x068C, 'Read result block length from R2', align=Align.INLINE)
d.comment(0x0690, 'No results to send: return to main loop', align=Align.INLINE)
d.comment(0x0692, 'Send result block bytes from &0128 via R2', align=Align.INLINE)

d.label(0x06A5, 'read_rdln_ctrl_block')
d.comment(0x06AD, 'X=0 after loop, A=0 for OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x06B4, 'C=0: line read OK; C=1: escape pressed', align=Align.INLINE)
d.comment(0x06B6, '&FF = escape/error signal to co-processor', align=Align.INLINE)
d.comment(0x06BD, '&7F = line read successfully', align=Align.INLINE)
d.comment(0x06C9, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x06E2, 'Check OS escape flag at &FF', align=Align.INLINE)
d.comment(0x06E4, 'SEC+ROR: put bit 7 of &FF into carry+bit 7', align=Align.INLINE)
d.comment(0x06E6, 'Escape set: forward to co-processor via R1', align=Align.INLINE)
d.comment(0x06E8, 'EVNTV: forward event A, Y, X to co-processor', align=Align.INLINE)
d.comment(0x06E9, 'Send &00 prefix (event notification)', align=Align.INLINE)

d.label(0x0D11, 'install_nmi_handler')

d.label(0x0DE6, 'nmi_sub_table')

d.label(0x0DF0, 'rom_ws_table')

d.label(0x0DFE, 'fs_context_base')

d.label(0x0E0B, 'fs_context_hi')

d.label(0x0E16, 'fs_work_16')

d.label(0x0E30, 'fs_filename_buf')

d.label(0x0EF7, 'fs_reply_data')

d.label(0x0F06, 'fs_func_code')

d.label(0x0F07, 'fs_data_count')

d.label(0x0F08, 'fs_reply_cmd')

d.label(0x0F09, 'fs_load_vector')

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

d.label(0x0FDE, 'fs_handle_mask')

d.label(0x0FDF, 'fs_error_flags')

d.label(0x0FE0, 'fs_error_buf')
d.comment(0x806F, 'Command index >= 4: invalid *NET sub-command', align=Align.INLINE)
d.comment(0x8071, 'Out of range: return via c80e3/RTS', align=Align.INLINE)
d.comment(0x8073, 'X = command index (0-3)', align=Align.INLINE)

d.label(0x807D, 'prepare_cmd_dispatch')
d.comment(0x8091, 'Function code >= 8? Return (unsupported)', align=Align.INLINE)
d.comment(0x8099, 'X >= 5: invalid reason code, return', align=Align.INLINE)

d.label(0x809B, 'svc_dispatch_range')
d.comment(0x809B, 'Out of range: return via RTS', align=Align.INLINE)
d.comment(0x80A0, 'Decrement base offset counter', align=Align.INLINE)
d.comment(0x80A1, 'Loop until Y exhausted', align=Align.INLINE)
d.comment(0x80A3, 'Y=&FF (no further use)', align=Align.INLINE)

d.label(0x80AF, 'check_svc_high')
d.comment(0x80AF, 'Service >= &FE?', align=Align.INLINE)
d.comment(0x80B1, 'Service < &FE: skip to &12/dispatch check', align=Align.INLINE)
d.comment(0x80B3, 'Service &FF: full init (vectors + RAM copy)', align=Align.INLINE)
d.comment(0x80B5, 'Service &FE: Y=0?', align=Align.INLINE)
d.comment(0x80B7, 'Y=0: no Tube data, skip to &12 check', align=Align.INLINE)
d.comment(0x80F9, 'Load ROM byte from page &93', align=Align.INLINE)
d.comment(0x80FC, 'Store to page &04 (Tube code)', align=Align.INLINE)
d.comment(0x80FF, 'Load ROM byte from page &94', align=Align.INLINE)
d.comment(0x8102, 'Store to page &05 (dispatch table)', align=Align.INLINE)
d.comment(0x8105, 'Load ROM byte from page &95', align=Align.INLINE)
d.comment(0x8108, 'Store to page &06', align=Align.INLINE)
d.comment(0x810B, 'DEY wraps 0 -> &FF on first iteration', align=Align.INLINE)
d.comment(0x810C, 'Loop until 256 bytes copied per page', align=Align.INLINE)
d.comment(0x810E, 'Run post-init routine in copied code', align=Align.INLINE)
d.comment(0x8111, 'X=&60: copy 97 bytes (&60..&00)', align=Align.INLINE)

d.label(0x8113, 'copy_nmi_workspace')
d.comment(0x8113, 'Load NMI workspace init byte from ROM', align=Align.INLINE)
d.comment(0x8116, 'Store to zero page &16+X', align=Align.INLINE)
d.comment(0x8118, 'Next byte', align=Align.INLINE)
d.comment(0x8119, 'Loop until all workspace bytes copied', align=Align.INLINE)

d.label(0x8127, 'not_svc_12_nfs')
d.comment(0x8127, 'Service >= &0D?', align=Align.INLINE)

d.label(0x8129, 'svc_unhandled_return')
d.comment(0x8129, 'Service >= &0D: not handled, return', align=Align.INLINE)

d.label(0x812B, 'do_svc_dispatch')
d.comment(0x812B, 'X = service number (dispatch index)', align=Align.INLINE)
d.comment(0x812C, 'Save &A9 (current service state)', align=Align.INLINE)
d.comment(0x812E, 'Push saved &A9', align=Align.INLINE)
d.comment(0x812F, 'Save &A8 (workspace page number)', align=Align.INLINE)
d.comment(0x8131, 'Push saved &A8', align=Align.INLINE)
d.comment(0x8132, 'Store service number to &A9', align=Align.INLINE)
d.comment(0x8134, 'Store Y (page number) to &A8', align=Align.INLINE)
d.comment(0x8136, 'A = Y for dispatch table offset', align=Align.INLINE)
d.comment(0x8137, 'Y=0: base offset for service dispatch', align=Align.INLINE)
d.comment(0x813C, 'Recover service claim status from &A9', align=Align.INLINE)
d.comment(0x813E, 'Restore saved &A8 from stack', align=Align.INLINE)
d.comment(0x813F, 'Write back &A8', align=Align.INLINE)


d.subroutine(0x8141, 'svc_dispatch_epilogue', title='Service dispatch epilogue', description="""Common return path for all dispatched service handlers.
Restores rom_svc_num from the stack (pushed by dispatch_service),
transfers X (ROM number) to A, then returns via RTS.""")
d.comment(0x8141, 'Restore saved A from service dispatch', align=Align.INLINE)
d.comment(0x8142, 'Save to workspace &A9', align=Align.INLINE)
d.comment(0x8144, 'Return ROM number in A', align=Align.INLINE)
d.comment(0x8146, 'Y=4: offset of keyboard disable flag', align=Align.INLINE)
d.comment(0x8148, 'Read flag from RX buffer', align=Align.INLINE)
d.comment(0x814A, 'Zero: keyboard not disabled, skip', align=Align.INLINE)
d.comment(0x814C, 'A=0: value to clear flag and re-enable', align=Align.INLINE)
d.comment(0x814F, 'Clear keyboard disable flag in buffer', align=Align.INLINE)
d.comment(0x8152, 'OSBYTE &C9: Econet keyboard disable', align=Align.INLINE)
d.comment(0x8154, 'Re-enable keyboard (X=0, Y=0)', align=Align.INLINE)
d.comment(0x8157, 'Function &0A: remote operation complete', align=Align.INLINE)
d.comment(0x8159, 'Send notification to controlling station', align=Align.INLINE)
d.comment(0x815C, 'Save X (return value from TX)', align=Align.INLINE)
d.comment(0x815E, 'OSBYTE &CE: first system mask to reset', align=Align.INLINE)

d.label(0x8160, 'clear_osbyte_masks')
d.comment(0x8160, 'Restore X for OSBYTE call', align=Align.INLINE)
d.comment(0x8162, 'Y=&7F: AND mask (clear bit 7)', align=Align.INLINE)
d.comment(0x8164, 'Reset system mask byte', align=Align.INLINE)
d.comment(0x8167, 'Advance to next OSBYTE (&CE -> &CF)', align=Align.INLINE)
d.comment(0x8169, 'Reached &D0? (past &CF)', align=Align.INLINE)
d.comment(0x816B, 'No: reset &CF too', align=Align.INLINE)

d.label(0x816D, 'skip_kbd_reenable')
d.comment(0x816D, 'A=0: clear remote state', align=Align.INLINE)
d.comment(0x816F, 'Clear &A9 (service dispatch state)', align=Align.INLINE)

d.label(0x817D, 'match_net_cmd')
d.comment(0x817D, 'X=1: ROM offset for "NET" match', align=Align.INLINE)
d.comment(0x817F, 'Try matching *NET command', align=Align.INLINE)
d.comment(0x8182, 'No match: return unclaimed', align=Align.INLINE)
d.comment(0x8184, 'Notify current FS of shutdown (FSCV A=6)', align=Align.INLINE)
d.comment(0x8187, 'C=1 for ROR', align=Align.INLINE)
d.comment(0x8188, 'Set bit 7 of l00a8 (inhibit auto-boot)', align=Align.INLINE)
d.comment(0x818A, 'Claim OS vectors, issue service &0F', align=Align.INLINE)
d.comment(0x818D, 'Y=&1D: top of FS state range', align=Align.INLINE)
d.comment(0x818F, 'Copy FS state from RX buffer...', align=Align.INLINE)
d.comment(0x8191, '...to workspace (offsets &15-&1D)', align=Align.INLINE)
d.comment(0x8194, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8195, 'Loop until offset &14 done', align=Align.INLINE)
d.comment(0x8197, 'Continue loop', align=Align.INLINE)
d.comment(0x8199, 'ALWAYS branch to init_fs_vectors', align=Align.INLINE)
d.comment(0x81CC, 'Return (service not claimed)', align=Align.INLINE)
d.comment(0x81CD, 'FSCV reason 6 = FS shutdown', align=Align.INLINE)
d.comment(0x81CF, 'Tail-call via filing system control vector', align=Align.INLINE)
d.comment(0x81D2, 'Notify current FS of shutdown', align=Align.INLINE)
d.comment(0x81D5, 'OSBYTE &7A: scan keyboard', align=Align.INLINE)
d.comment(0x81DB, 'No key pressed: proceed with auto-boot', align=Align.INLINE)


d.subroutine(0x81DD, 'check_boot_key', title='Check boot key', description="""Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")
d.comment(0x81DD, "XOR with &55: result=0 if key is 'N'", align=Align.INLINE)
d.comment(0x81DF, "Not 'N': return without claiming", align=Align.INLINE)
d.comment(0x81E2, 'OSBYTE &78: clear key-pressed state', align=Align.INLINE)
d.comment(0x81E7, "Print 'Econet Station ' banner", align=Align.INLINE)
d.comment(0x8206, "Print ' No Clock' warning", align=Align.INLINE)
d.comment(0x8212, 'NOP (padding after inline string)', align=Align.INLINE)

d.label(0x8213, 'skip_no_clock_msg')
d.comment(0x8213, 'Print two CRs (blank line)', align=Align.INLINE)
d.comment(0x821D, 'Write to FILEV-FSCV vector table', align=Align.INLINE)
d.comment(0x8220, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8221, 'Loop until all 14 bytes copied', align=Align.INLINE)
d.comment(0x8223, 'Read ROM ptr table addr, install NETV', align=Align.INLINE)
d.comment(0x8226, 'Install 7 handler entries in ROM ptr table', align=Align.INLINE)
d.comment(0x8228, '7 FS vectors to install', align=Align.INLINE)
d.comment(0x822A, 'Install each 3-byte vector entry', align=Align.INLINE)
d.comment(0x822D, 'X=0 after loop; store as workspace offset', align=Align.INLINE)
d.comment(0x8238, 'Issue service &0A', align=Align.INLINE)
d.comment(0x823B, 'Non-zero after hard reset: skip auto-boot', align=Align.INLINE)
d.comment(0x823F, 'X = lo byte of auto-boot string at &8292', align=Align.INLINE)
d.comment(0x824C, 'Auto-boot string tail / NETV handler data', align=Align.INLINE)
d.comment(0x827E, 'A=0 for clearing workspace', align=Align.INLINE)
d.comment(0x8280, 'Y=4: remote status offset', align=Align.INLINE)
d.comment(0x8282, 'Clear status byte in net receive buffer', align=Align.INLINE)
d.comment(0x8284, 'Y=&FF: used for later iteration', align=Align.INLINE)
d.comment(0x8286, 'Clear RX ptr low byte', align=Align.INLINE)
d.comment(0x8288, 'Clear workspace ptr low byte', align=Align.INLINE)
d.comment(0x828A, 'Clear RXCB iteration counter', align=Align.INLINE)
d.comment(0x828C, 'Clear TX semaphore (no TX in progress)', align=Align.INLINE)
d.comment(0x828F, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x8295, 'X = break type from OSBYTE result', align=Align.INLINE)
d.comment(0x8298, 'Y=&15: printer station offset in RX buffer', align=Align.INLINE)
d.comment(0x829A, '&FE = no server selected', align=Align.INLINE)
d.comment(0x829F, 'Store &FE at printer station offset', align=Align.INLINE)

d.label(0x82B5, 'init_rxcb_entries')
d.comment(0x82B5, 'Load RXCB counter', align=Align.INLINE)
d.comment(0x82B7, 'Convert to workspace byte offset', align=Align.INLINE)
d.comment(0x82BA, 'C=1: past max handles, done', align=Align.INLINE)
d.comment(0x82BC, 'Mark RXCB as available', align=Align.INLINE)
d.comment(0x82BE, 'Write &3F flag to workspace', align=Align.INLINE)
d.comment(0x82C0, 'Next RXCB number', align=Align.INLINE)
d.comment(0x82C2, 'Loop for all RXCBs', align=Align.INLINE)

d.label(0x82C4, 'read_station_id')
d.comment(0x82CD, 'Enable user-level RX (LFLAG=&40)', align=Align.INLINE)
d.comment(0x82CF, 'Store to rx_flags', align=Align.INLINE)
d.comment(0x82D2, 'OSBYTE &A8: read ROM pointer table address', align=Align.INLINE)
d.comment(0x82D4, 'X=0: read low byte', align=Align.INLINE)
d.comment(0x82D6, 'Y=&FF: read high byte', align=Align.INLINE)
d.comment(0x82D8, 'Returns table address in X (lo) Y (hi)', align=Align.INLINE)
d.comment(0x82DB, 'Store table base address low byte', align=Align.INLINE)
d.comment(0x82DD, 'Store table base address high byte', align=Align.INLINE)
d.comment(0x82DF, 'NETV extended vector offset in ROM ptr table', align=Align.INLINE)
d.comment(0x82E1, 'Set NETV low byte = &36 (vector dispatch)', align=Align.INLINE)
d.comment(0x82E4, 'Install 1 entry (NETV) in ROM ptr table', align=Align.INLINE)
d.comment(0x82E6, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x82E9, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x82EB, 'Next byte', align=Align.INLINE)
d.comment(0x82EC, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x82EF, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x82F1, 'Next byte', align=Align.INLINE)
d.comment(0x82F2, 'Write current ROM bank number', align=Align.INLINE)
d.comment(0x82F4, 'Store ROM number to ROM pointer table', align=Align.INLINE)
d.comment(0x82F6, 'Advance to next entry position', align=Align.INLINE)
d.comment(0x82F7, 'Count down entries', align=Align.INLINE)
d.comment(0x82F8, 'Loop until all entries installed', align=Align.INLINE)
d.comment(0x82FA, 'Y = workspace high byte + 1 = next free page', align=Align.INLINE)
d.comment(0x82FC, 'Advance past workspace page', align=Align.INLINE)
d.comment(0x82FD, 'Return; Y = page after NFS workspace', align=Align.INLINE)
d.comment(0x82FE, 'Copy 10 bytes: FS state to workspace backup', align=Align.INLINE)
d.comment(0x8306, 'Offsets &15-&1D: server, handles, OPT, etc.', align=Align.INLINE)


d.subroutine(0x830F, 'init_tx_reply_port', title='Initialise TX control block for FS reply on port &90', description="""Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
up the TX control block, stores the port and control bytes, then
decrements the control flag. Used by send_fs_reply_cmd to prepare
for receiving the fileserver's reply.""")
d.comment(0x830F, 'A=&90: FS reply port (PREPLY)', align=Align.INLINE)
d.comment(0x8311, 'Init TXCB from template', align=Align.INLINE)
d.comment(0x8314, 'Store port number in TXCB', align=Align.INLINE)
d.comment(0x8316, 'Control byte: 3 = transmit', align=Align.INLINE)
d.comment(0x8318, 'Store control byte in TXCB', align=Align.INLINE)
d.comment(0x831A, 'Decrement TXCB flag to arm TX', align=Align.INLINE)
d.comment(0x831D, 'Preserve A across call', align=Align.INLINE)
d.comment(0x831E, 'Copy 12 bytes (Y=11..0)', align=Align.INLINE)
d.comment(0x8320, 'Load template byte', align=Align.INLINE)
d.comment(0x8323, 'Store to TX control block at &00C0', align=Align.INLINE)
d.comment(0x8326, 'Y < 2: also copy FS server station/network', align=Align.INLINE)
d.comment(0x8328, 'Skip station/network copy for Y >= 2', align=Align.INLINE)
d.comment(0x832A, 'Load FS server station (Y=0) or network (Y=1)', align=Align.INLINE)
d.comment(0x832D, 'Store to dest station/network at &00C2', align=Align.INLINE)
d.comment(0x8330, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8331, 'Loop until all 12 bytes copied', align=Align.INLINE)
d.comment(0x8333, 'Restore A', align=Align.INLINE)
d.comment(0x8334, 'Return', align=Align.INLINE)

d.label(0x833B, 'tx_ctrl_upper')
d.comment(0x8341, 'Save flag byte for command', align=Align.INLINE)
d.comment(0x8344, 'C=1: include flag in FS command', align=Align.INLINE)
d.comment(0x8345, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)
d.comment(0x8347, 'V=0: command has no flag byte', align=Align.INLINE)
d.comment(0x8348, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)
d.comment(0x8351, 'V=0: standard FS command path', align=Align.INLINE)
d.comment(0x8352, 'Copy URD handle from workspace to buffer', align=Align.INLINE)
d.comment(0x8355, 'Store URD at &0F02', align=Align.INLINE)
d.comment(0x8360, 'Y=1: copy CSD (offset 1) then LIB (offset 0)', align=Align.INLINE)

d.label(0x8362, 'copy_dir_handles')
d.comment(0x8362, 'Copy CSD and LIB handles to command buffer', align=Align.INLINE)
d.comment(0x8365, 'Store at &0F03 (CSD) and &0F04 (LIB)', align=Align.INLINE)
d.comment(0x8368, 'Y=function code', align=Align.INLINE)
d.comment(0x8369, 'Loop for both handles', align=Align.INLINE)
d.comment(0x836B, 'Save carry (FS path vs byte-stream)', align=Align.INLINE)
d.comment(0x836C, 'Reply port &90 (PREPLY)', align=Align.INLINE)
d.comment(0x836E, 'Store at &0F00 (HDRREP)', align=Align.INLINE)
d.comment(0x8371, 'Copy TX template to &00C0', align=Align.INLINE)
d.comment(0x8374, 'A = X (buffer extent)', align=Align.INLINE)
d.comment(0x8375, 'HPTR = header (5) + data (X) bytes to send', align=Align.INLINE)
d.comment(0x8377, 'Store to TXCB end-pointer low', align=Align.INLINE)
d.comment(0x8379, 'Restore carry flag', align=Align.INLINE)
d.comment(0x837A, 'C=1: byte-stream path (BSXMIT)', align=Align.INLINE)
d.comment(0x837C, 'Save flags for send_fs_reply_cmd', align=Align.INLINE)
d.comment(0x837D, 'Point net_tx_ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x8380, 'Restore flags', align=Align.INLINE)
d.comment(0x8381, 'Save flags (V flag state)', align=Align.INLINE)
d.comment(0x8382, 'Set up RX wait for FS reply', align=Align.INLINE)
d.comment(0x8387, 'Transmit and wait (BRIANX)', align=Align.INLINE)
d.comment(0x838A, 'Restore flags', align=Align.INLINE)
d.comment(0x838B, 'Y=1: skip past command code byte', align=Align.INLINE)
d.comment(0x838C, 'Load return code from FS reply', align=Align.INLINE)
d.comment(0x838E, 'X = return code', align=Align.INLINE)
d.comment(0x838F, 'Zero: success, return', align=Align.INLINE)
d.comment(0x8391, 'V=0: standard path, error is fatal', align=Align.INLINE)
d.comment(0x8393, 'ADC #&2A: test for &D6 (not found)', align=Align.INLINE)

d.label(0x8395, 'check_fs_error')
d.comment(0x8395, 'Non-zero: hard error, go to FSERR', align=Align.INLINE)
d.comment(0x8397, 'Return (success or soft &D6 error)', align=Align.INLINE)
d.comment(0x8398, 'Discard saved flags from stack', align=Align.INLINE)
d.comment(0x8399, 'X=&C0: TXCB address for byte-stream TX', align=Align.INLINE)
d.comment(0x839B, 'Y++ past command code', align=Align.INLINE)
d.comment(0x839C, 'Byte-stream transmit with retry', align=Align.INLINE)
d.comment(0x839F, 'Store result to &B3', align=Align.INLINE)
d.comment(0x83A1, 'C=0: success, check reply code', align=Align.INLINE)
d.comment(0x83A4, 'Save A (BPUT byte) on stack', align=Align.INLINE)
d.comment(0x83A5, 'Also save byte at &0FDF for BSXMIT', align=Align.INLINE)
d.comment(0x83A8, 'Transfer X for stack save', align=Align.INLINE)
d.comment(0x83A9, 'Save X on stack', align=Align.INLINE)
d.comment(0x83AA, 'Transfer Y (handle) for stack save', align=Align.INLINE)
d.comment(0x83AB, 'Save Y (handle) on stack', align=Align.INLINE)
d.comment(0x83AC, 'Save P (C = BPUT/BGET selector) on stack', align=Align.INLINE)
d.comment(0x83AD, 'Convert handle Y to single-bit mask', align=Align.INLINE)
d.comment(0x83B0, 'Store handle bitmask at &0FDE', align=Align.INLINE)
d.comment(0x83B3, 'Store handle bitmask for sequence tracking', align=Align.INLINE)
d.comment(0x83B5, '&90 = data port (PREPLY)', align=Align.INLINE)
d.comment(0x83B7, 'Store reply port in command buffer', align=Align.INLINE)
d.comment(0x83BA, 'Set up 12-byte TXCB from template', align=Align.INLINE)
d.comment(0x83BD, 'CB reply buffer at &0FDC', align=Align.INLINE)
d.comment(0x83BF, 'Store reply buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x83C1, 'Error buffer at &0FE0', align=Align.INLINE)
d.comment(0x83C3, 'Store error buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x83C5, 'Y=1 (from init_tx_ctrl_block exit)', align=Align.INLINE)
d.comment(0x83C6, 'X=9: BPUT function code', align=Align.INLINE)
d.comment(0x83C8, 'Restore C: selects BPUT (0) vs BGET (1)', align=Align.INLINE)
d.comment(0x83C9, 'C=0 (BPUT): keep X=9', align=Align.INLINE)
d.comment(0x83CC, 'Store function code at &0FDD', align=Align.INLINE)
d.comment(0x83D2, 'X=&C0: TXCB address for econet_tx_retry', align=Align.INLINE)
d.comment(0x83D4, 'Transmit via byte-stream protocol', align=Align.INLINE)
d.comment(0x83D7, 'Load reply byte from buffer', align=Align.INLINE)
d.comment(0x83DA, 'Zero reply = success, skip error handling', align=Align.INLINE)
d.comment(0x83DC, 'Copy 32-byte reply to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x83DE, 'Load reply byte at offset Y', align=Align.INLINE)
d.comment(0x83E1, 'Store to error buffer at &0FE0+Y', align=Align.INLINE)
d.comment(0x83E4, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x83E5, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x83E8, 'A=&C7: read *SPOOL file handle', align=Align.INLINE)
d.comment(0x83F7, 'Y=&85: high byte of OSCLI string in ROM', align=Align.INLINE)
d.comment(0x83F9, 'Close SPOOL/EXEC via "*SP." or "*E."', align=Align.INLINE)

d.label(0x83FC, 'dispatch_fs_error')
d.comment(0x83FC, 'Reset CB pointer to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x83FE, 'Reset reply ptr to error buffer', align=Align.INLINE)
d.comment(0x8400, 'Reload reply byte for error dispatch', align=Align.INLINE)
d.comment(0x8403, 'Remember raw FS error code', align=Align.INLINE)
d.comment(0x8406, 'Y=1: point to error number byte in reply', align=Align.INLINE)
d.comment(0x8408, 'Clamp FS errors below &A8 to standard &A8', align=Align.INLINE)
d.comment(0x840A, 'Error >= &A8: keep original value', align=Align.INLINE)
d.comment(0x840C, 'Error < &A8: override with standard &A8', align=Align.INLINE)
d.comment(0x840E, 'Write clamped error number to reply buffer', align=Align.INLINE)
d.comment(0x841C, 'Save updated sequence number', align=Align.INLINE)
d.comment(0x841F, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8421, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8423, 'Restore A from stack', align=Align.INLINE)
d.comment(0x8424, 'Return to caller', align=Align.INLINE)

d.label(0x8425, 'error_not_listening')
d.comment(0x8425, 'Error code 8: "Not listening" error', align=Align.INLINE)
d.comment(0x8427, 'ALWAYS branch to set_listen_offset', align=Align.INLINE)
d.comment(0x8429, 'Load TX status byte for error lookup', align=Align.INLINE)
d.comment(0x842B, 'Mask to 3-bit error code (0-7)', align=Align.INLINE)
d.comment(0x842D, 'X = error code index', align=Align.INLINE)
d.comment(0x842E, 'Look up error message offset from table', align=Align.INLINE)
d.comment(0x8431, 'X=0: start writing at &0101', align=Align.INLINE)
d.comment(0x8433, 'Store BRK opcode at &0100', align=Align.INLINE)

d.label(0x8436, 'copy_error_message')
d.comment(0x8436, 'Load error message byte', align=Align.INLINE)
d.comment(0x8439, 'Build error message at &0101+', align=Align.INLINE)
d.comment(0x843C, 'Zero byte = end of message; go execute BRK', align=Align.INLINE)
d.comment(0x844B, 'Save function code on stack', align=Align.INLINE)
d.comment(0x844C, 'Load current rx_flags', align=Align.INLINE)
d.comment(0x844F, 'Save rx_flags on stack for restore', align=Align.INLINE)
d.comment(0x8450, 'Set bit7: FS transaction in progress', align=Align.INLINE)
d.comment(0x8452, 'Write back updated rx_flags', align=Align.INLINE)

d.label(0x8455, 'skip_rx_flag_set')
d.comment(0x8455, 'Push two zero bytes as timeout counters', align=Align.INLINE)
d.comment(0x8457, 'First zero for timeout', align=Align.INLINE)
d.comment(0x8458, 'Second zero for timeout', align=Align.INLINE)
d.comment(0x8459, 'Y=0: index for flag byte check', align=Align.INLINE)
d.comment(0x845A, 'TSX: index stack-based timeout via X', align=Align.INLINE)
d.comment(0x8462, 'Three-stage nested timeout: inner loop', align=Align.INLINE)
d.comment(0x8465, 'Inner not expired: keep polling', align=Align.INLINE)
d.comment(0x8467, 'Middle timeout loop', align=Align.INLINE)
d.comment(0x846A, 'Middle not expired: keep polling', align=Align.INLINE)
d.comment(0x846C, 'Outer timeout loop (slowest)', align=Align.INLINE)
d.comment(0x846F, 'Outer not expired: keep polling', align=Align.INLINE)
d.comment(0x8471, 'Pop first timeout byte', align=Align.INLINE)
d.comment(0x8472, 'Pop second timeout byte', align=Align.INLINE)
d.comment(0x8473, 'Pop saved rx_flags into A', align=Align.INLINE)
d.comment(0x8474, 'Restore saved rx_flags from stack', align=Align.INLINE)
d.comment(0x8477, 'Pop saved function code', align=Align.INLINE)
d.comment(0x8478, 'A=saved func code; zero would mean no reply', align=Align.INLINE)
d.comment(0x847A, 'Return to caller', align=Align.INLINE)
d.comment(0x8486, 'C=1: flag for BGET mode', align=Align.INLINE)
d.comment(0x8487, 'Handle BGET via FS command', align=Align.INLINE)
d.comment(0x848A, 'SEC: set carry for error check', align=Align.INLINE)
d.comment(0x848B, 'A=&FE: mask for EOF check', align=Align.INLINE)
d.comment(0x848D, 'BIT l0fdf: test error flags', align=Align.INLINE)
d.comment(0x8490, 'V=1: error, return early', align=Align.INLINE)
d.comment(0x8492, 'CLC: no error', align=Align.INLINE)

d.label(0x84AF, 'return_4')
d.comment(0x8514, 'Y=&0E: attribute byte offset in param block', align=Align.INLINE)
d.comment(0x8516, 'Load FS attribute byte', align=Align.INLINE)
d.comment(0x8518, 'Mask to 6 bits (FS → BBC direction)', align=Align.INLINE)
d.comment(0x851A, 'X=4: skip first 4 table entries (BBC→FS half)', align=Align.INLINE)
d.comment(0x851C, 'ALWAYS branch to shared bitmask builder', align=Align.INLINE)
d.comment(0x851E, 'Mask to 5 bits (BBC → FS direction)', align=Align.INLINE)
d.comment(0x8520, 'X=&FF: INX makes 0; start from table index 0', align=Align.INLINE)

d.label(0x8522, 'attrib_shift_bits')
d.comment(0x8522, 'Temp storage for source bitmask to shift out', align=Align.INLINE)
d.comment(0x8524, 'A=0: accumulate destination bits here', align=Align.INLINE)

d.label(0x8526, 'map_attrib_bits')
d.comment(0x8526, 'Next table entry', align=Align.INLINE)
d.comment(0x8527, 'Shift out source bits one at a time', align=Align.INLINE)
d.comment(0x8529, 'Bit was 0: skip this destination bit', align=Align.INLINE)
d.comment(0x852B, 'OR in destination bit from lookup table', align=Align.INLINE)

d.label(0x852E, 'skip_set_attrib_bit')
d.comment(0x852E, 'Loop while source bits remain (A != 0)', align=Align.INLINE)
d.comment(0x8530, 'Return; A = converted attribute bitmask', align=Align.INLINE)

d.label(0x8544, 'print_inline_char')

d.label(0x854A, 'print_next_char')

d.label(0x8585, 'no_dot_exit')

d.label(0x8586, 'parse_decimal_rts')
d.comment(0x8589, 'Handle number to Y for conversion', align=Align.INLINE)
d.comment(0x858A, 'Force unconditional conversion', align=Align.INLINE)

d.label(0x85A2, 'handle_mask_exit')
d.comment(0x85AC, 'A = X = &1F + bit position = handle', align=Align.INLINE)
d.comment(0x85CF, 'Compare 4 bytes (index 4,3,2,1)', align=Align.INLINE)

d.label(0x85D1, 'compare_addr_byte')
d.comment(0x85D1, 'Load byte from first address', align=Align.INLINE)
d.comment(0x85D3, 'XOR with corresponding byte', align=Align.INLINE)
d.comment(0x85D5, 'Mismatch: Z=0, return unequal', align=Align.INLINE)
d.comment(0x85D8, 'Continue comparing', align=Align.INLINE)
d.comment(0x85DB, 'X=first handle (&20)', align=Align.INLINE)
d.comment(0x85DD, 'Y=last handle (&27)', align=Align.INLINE)
d.comment(0x8698, 'Y=1: copy 2 bytes (high then low)', align=Align.INLINE)
d.comment(0x869A, 'Load filename ptr from control block', align=Align.INLINE)
d.comment(0x869C, 'Store to MOS text pointer (&F2/&F3)', align=Align.INLINE)
d.comment(0x869F, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x86A0, 'Loop for both bytes', align=Align.INLINE)
d.comment(0x86A9, 'Read next character via GSREAD', align=Align.INLINE)
d.comment(0x86AC, 'C=1 from GSREAD: end of string reached', align=Align.INLINE)
d.comment(0x86AE, 'Advance buffer index', align=Align.INLINE)
d.comment(0x86AF, 'Store parsed character to &0E30+X', align=Align.INLINE)
d.comment(0x86B2, 'ALWAYS loop (GSREAD clears C on success)', align=Align.INLINE)
d.comment(0x86B4, 'CR = &0D', align=Align.INLINE)
d.comment(0x86B6, 'Store CR terminator at end of string', align=Align.INLINE)
d.comment(0x86B9, 'Point fs_crc_lo/hi at &0E30 parse buffer', align=Align.INLINE)
d.comment(0x86BB, 'fs_crc_lo = &30', align=Align.INLINE)
d.comment(0x86BD, 'fs_crc_hi = &0E → buffer at &0E30', align=Align.INLINE)
d.comment(0x86BF, 'Store high byte', align=Align.INLINE)
d.comment(0x86C1, 'Recover function code from saved A', align=Align.INLINE)
d.comment(0x86C3, 'A >= 0: save (&00) or attribs (&01-&06)', align=Align.INLINE)
d.comment(0x86C5, 'A=&FF? Only &FF is valid for load', align=Align.INLINE)
d.comment(0x86C9, 'Unknown negative code: no-op return', align=Align.INLINE)
d.comment(0x86D1, 'Port &92 = PLDATA (data transfer port)', align=Align.INLINE)
d.comment(0x86D3, 'Overwrite URD field with data port number', align=Align.INLINE)
d.comment(0x86D8, 'Build FS header (V=1: CLV path)', align=Align.INLINE)
d.comment(0x86DB, 'Y=6: param block byte 6', align=Align.INLINE)
d.comment(0x86DD, "Byte 6: use file's own load address?", align=Align.INLINE)
d.comment(0x86DF, 'Non-zero: use FS reply address (lodfil)', align=Align.INLINE)
d.comment(0x86E1, "Zero: copy caller's load addr first", align=Align.INLINE)
d.comment(0x86E4, 'Then copy FS reply to param block', align=Align.INLINE)
d.comment(0x86E7, 'Carry clear from prepare_cmd_clv: skip lodfil', align=Align.INLINE)
d.comment(0x86E9, 'Copy FS reply addresses to param block', align=Align.INLINE)
d.comment(0x86EC, 'Then copy load addr from param block', align=Align.INLINE)

d.label(0x86EF, 'skip_lodfil')
d.comment(0x86EF, 'Compute end address = load + file length', align=Align.INLINE)

d.label(0x86F1, 'copy_load_end_addr')
d.comment(0x86F1, 'Load address byte', align=Align.INLINE)
d.comment(0x86F3, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x86F5, 'Add file length byte', align=Align.INLINE)
d.comment(0x86F8, 'Store as end position', align=Align.INLINE)
d.comment(0x86FA, 'Next address byte', align=Align.INLINE)
d.comment(0x86FB, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x86FC, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x86FE, 'Adjust high byte for 3-byte length overflow', align=Align.INLINE)
d.comment(0x86FF, 'Subtract 4th length byte from end addr', align=Align.INLINE)
d.comment(0x8702, 'Store adjusted end address high byte', align=Align.INLINE)
d.comment(0x8707, 'Transfer file data in &80-byte blocks', align=Align.INLINE)
d.comment(0x870A, 'Copy 3-byte file length to FS reply cmd buffer', align=Align.INLINE)
d.comment(0x870C, 'Load file length byte', align=Align.INLINE)
d.comment(0x870F, 'Store in FS command data buffer', align=Align.INLINE)
d.comment(0x8712, 'Next byte (count down)', align=Align.INLINE)
d.comment(0x8713, 'Loop for 3 bytes (X=2,1,0)', align=Align.INLINE)
d.comment(0x8715, 'ALWAYS branch', align=Align.INLINE)
d.comment(0x871A, 'Addresses match: transfer complete', align=Align.INLINE)
d.comment(0x871C, 'Port &92 for data block transfer', align=Align.INLINE)
d.comment(0x871E, 'Store port to TXCB command byte', align=Align.INLINE)

d.label(0x8720, 'send_block_loop')
d.comment(0x8720, 'Set up next &80-byte block for transfer', align=Align.INLINE)

d.label(0x8722, 'copy_block_addrs')
d.comment(0x8722, 'Swap: current addr -> source, end -> current', align=Align.INLINE)
d.comment(0x8724, 'Source addr = current position', align=Align.INLINE)
d.comment(0x8726, 'Load end address byte', align=Align.INLINE)
d.comment(0x8728, 'Dest = end address (will be clamped)', align=Align.INLINE)
d.comment(0x872A, 'Next address byte', align=Align.INLINE)
d.comment(0x872B, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x872D, 'Command &7F = data block transfer', align=Align.INLINE)
d.comment(0x872F, 'Store to TXCB control byte', align=Align.INLINE)
d.comment(0x8731, 'Send this block to the fileserver', align=Align.INLINE)
d.comment(0x8734, 'Y=3: compare 4 bytes (3..0)', align=Align.INLINE)
d.comment(0x8736, 'Compare current vs end address (4 bytes)', align=Align.INLINE)
d.comment(0x8739, 'XOR with end address byte', align=Align.INLINE)
d.comment(0x873C, 'Not equal: more blocks to send', align=Align.INLINE)
d.comment(0x873E, 'Next byte', align=Align.INLINE)
d.comment(0x873F, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8741, 'All equal: transfer complete', align=Align.INLINE)
d.comment(0x8742, 'A=0: SAVE handler', align=Align.INLINE)
d.comment(0x8744, 'A!=0: attribute dispatch (A=1-6)', align=Align.INLINE)
d.comment(0x8747, 'Process 4 address bytes (load/exec/start/end)', align=Align.INLINE)
d.comment(0x8749, 'Y=&0E: start from end-address in param block', align=Align.INLINE)
d.comment(0x874B, 'Read end-address byte from param block', align=Align.INLINE)
d.comment(0x874D, 'Save to port workspace for transfer setup', align=Align.INLINE)
d.comment(0x8750, 'Y = Y-4: point to start-address byte', align=Align.INLINE)
d.comment(0x8753, 'end - start = transfer length byte', align=Align.INLINE)
d.comment(0x8755, 'Store length byte in FS command buffer', align=Align.INLINE)
d.comment(0x8758, 'Save length byte for param block restore', align=Align.INLINE)
d.comment(0x8759, 'Read corresponding start-address byte', align=Align.INLINE)
d.comment(0x875B, 'Save to port workspace', align=Align.INLINE)
d.comment(0x875E, 'Restore length byte from stack', align=Align.INLINE)
d.comment(0x875F, 'Replace param block entry with length', align=Align.INLINE)
d.comment(0x8761, 'Y = Y+5: advance to next address group', align=Align.INLINE)
d.comment(0x8764, 'Decrement address byte counter', align=Align.INLINE)
d.comment(0x8765, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8767, 'Copy load/exec addresses to FS command buffer', align=Align.INLINE)

d.label(0x8769, 'copy_save_params')
d.comment(0x8769, 'Read load/exec address byte from params', align=Align.INLINE)
d.comment(0x876B, 'Copy to FS command buffer', align=Align.INLINE)
d.comment(0x876E, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x876F, 'Loop for bytes 9..1', align=Align.INLINE)
d.comment(0x8771, 'Port &91 for save command', align=Align.INLINE)
d.comment(0x8773, 'Overwrite URD field with port number', align=Align.INLINE)
d.comment(0x8776, 'Save port &91 for flow control ACK', align=Align.INLINE)
d.comment(0x8778, 'Append filename at offset &0B in cmd buffer', align=Align.INLINE)
d.comment(0x877A, 'Append filename to cmd buffer at offset X', align=Align.INLINE)
d.comment(0x877D, 'Y=1: function code for save', align=Align.INLINE)

d.label(0x8794, 'skip_catalogue_msg')
d.comment(0x8794, 'Store reply command for attr decode', align=Align.INLINE)
d.comment(0x8797, 'Y=&0E: access byte offset in param block', align=Align.INLINE)
d.comment(0x8799, 'Load access byte from FS reply', align=Align.INLINE)
d.comment(0x879C, 'Convert FS access to BBC attribute format', align=Align.INLINE)
d.comment(0x87A7, 'Copied all 4 bytes? (Y=&0E..&11)', align=Align.INLINE)
d.comment(0x87A9, 'Loop for 4 attribute bytes', align=Align.INLINE)
d.comment(0x87AB, 'Restore A/X/Y and return to caller', align=Align.INLINE)
d.comment(0x87AE, 'Start at offset 5 (top of 4-byte addr)', align=Align.INLINE)
d.comment(0x87B0, 'Read from parameter block', align=Align.INLINE)
d.comment(0x87B2, 'Store to local workspace', align=Align.INLINE)
d.comment(0x87B5, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x87B6, 'Copy offsets 5,4,3,2 (4 bytes)', align=Align.INLINE)
d.comment(0x87B8, 'Loop while Y >= 2', align=Align.INLINE)
d.comment(0x87BA, 'Return', align=Align.INLINE)
d.comment(0x87BB, 'Start at offset &0D (top of range)', align=Align.INLINE)
d.comment(0x87BD, 'First store uses X (attrib byte)', align=Align.INLINE)
d.comment(0x87BE, 'Write to parameter block', align=Align.INLINE)
d.comment(0x87C0, 'Read next byte from reply buffer', align=Align.INLINE)
d.comment(0x87C4, 'Copy offsets &0D down to 2', align=Align.INLINE)
d.comment(0x87C9, 'Save FS command byte on stack', align=Align.INLINE)
d.comment(0x87CD, 'Addresses equal: nothing to transfer', align=Align.INLINE)
d.comment(0x87E1, 'Store dest address byte', align=Align.INLINE)
d.comment(0x87E3, 'Advance current position', align=Align.INLINE)
d.comment(0x87E5, 'Next address byte', align=Align.INLINE)
d.comment(0x87E6, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x87E7, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x87EB, 'SEC for SBC in overshoot check', align=Align.INLINE)
d.comment(0x87EC, 'Check if new pos overshot end addr', align=Align.INLINE)
d.comment(0x87EF, 'Subtract end address byte', align=Align.INLINE)
d.comment(0x87F2, 'Next byte', align=Align.INLINE)
d.comment(0x87F3, 'Decrement counter', align=Align.INLINE)
d.comment(0x87F4, 'Loop for 4-byte comparison', align=Align.INLINE)
d.comment(0x87F6, 'C=0: no overshoot, proceed', align=Align.INLINE)
d.comment(0x87F8, 'Overshot: clamp dest to end address', align=Align.INLINE)

d.label(0x87FA, 'clamp_dest_addr')
d.comment(0x87FA, 'Load end address byte', align=Align.INLINE)
d.comment(0x87FC, 'Replace dest with end address', align=Align.INLINE)
d.comment(0x87FE, 'Next byte', align=Align.INLINE)
d.comment(0x87FF, 'Loop for all 4 bytes', align=Align.INLINE)

d.label(0x8801, 'send_block')
d.comment(0x8801, 'Recover original FS command byte', align=Align.INLINE)
d.comment(0x8802, 'Re-push for next iteration', align=Align.INLINE)
d.comment(0x8803, 'Save processor flags (C from cmp)', align=Align.INLINE)
d.comment(0x8804, 'Store command byte in TXCB', align=Align.INLINE)
d.comment(0x8806, '128-byte block size for data transfer', align=Align.INLINE)
d.comment(0x8808, 'Store size in TXCB control byte', align=Align.INLINE)
d.comment(0x880A, 'Point TX ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x880D, 'ACK port for flow control', align=Align.INLINE)
d.comment(0x880F, 'Set reply port for ACK receive', align=Align.INLINE)
d.comment(0x8812, 'Restore flags (C=overshoot status)', align=Align.INLINE)
d.comment(0x8813, 'C=1: all data sent (overshot), done', align=Align.INLINE)
d.comment(0x8815, 'Command &91 = data block transfer', align=Align.INLINE)
d.comment(0x8817, 'Store command &91 in TXCB', align=Align.INLINE)
d.comment(0x881B, 'Transmit block and wait (BRIANX)', align=Align.INLINE)
d.comment(0x881E, 'More blocks? Loop back', align=Align.INLINE)
d.comment(0x8820, 'Save A (function code)', align=Align.INLINE)
d.comment(0x8823, 'Convert handle to bitmask in A', align=Align.INLINE)
d.comment(0x8826, 'Y = handle bitmask from conversion', align=Align.INLINE)
d.comment(0x8827, 'Local hint: is EOF possible for this handle?', align=Align.INLINE)
d.comment(0x882A, 'X = result of AND (0 = not at EOF)', align=Align.INLINE)
d.comment(0x882B, 'Hint clear: definitely not at EOF', align=Align.INLINE)
d.comment(0x882D, 'Save bitmask for clear_fs_flag', align=Align.INLINE)
d.comment(0x882E, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x8831, 'Y=&11: FS function code FCEOF', align=Align.INLINE)
d.comment(0x8838, 'Restore bitmask', align=Align.INLINE)
d.comment(0x8839, 'FS reply: non-zero = at EOF', align=Align.INLINE)
d.comment(0x883C, 'At EOF: skip flag clear', align=Align.INLINE)
d.comment(0x883E, 'Not at EOF: clear the hint bit', align=Align.INLINE)

d.label(0x8841, 'restore_ay_return')
d.comment(0x8841, 'Restore A', align=Align.INLINE)
d.comment(0x8842, 'Restore Y', align=Align.INLINE)
d.comment(0x8844, 'Return; X=0 (not EOF) or X=&FF (EOF)', align=Align.INLINE)
d.comment(0x8845, 'Store function code in FS cmd buffer', align=Align.INLINE)
d.comment(0x8848, 'A=6? (delete)', align=Align.INLINE)
d.comment(0x884A, 'Yes: jump to delete handler', align=Align.INLINE)
d.comment(0x884C, 'A>=7: unsupported, fall through to return', align=Align.INLINE)
d.comment(0x884E, 'A=5? (read catalogue info)', align=Align.INLINE)
d.comment(0x8850, 'Yes: jump to read info handler', align=Align.INLINE)
d.comment(0x8852, 'A=4? (write attributes only)', align=Align.INLINE)
d.comment(0x8854, 'Yes: jump to write attrs handler', align=Align.INLINE)
d.comment(0x8856, 'A=1? (write all catalogue info)', align=Align.INLINE)
d.comment(0x8858, 'Yes: jump to write-all handler', align=Align.INLINE)
d.comment(0x885A, 'A=2 or 3: convert to param block offset', align=Align.INLINE)
d.comment(0x885B, 'A*4: 2->8, 3->12', align=Align.INLINE)
d.comment(0x885C, 'Y = A*4', align=Align.INLINE)
d.comment(0x885D, 'Y = A*4 - 3 (load addr offset for A=2)', align=Align.INLINE)
d.comment(0x8860, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x8862, 'Load address byte from param block', align=Align.INLINE)
d.comment(0x8864, 'Store to FS cmd data area', align=Align.INLINE)
d.comment(0x8867, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x8868, 'Next dest byte', align=Align.INLINE)
d.comment(0x8869, 'Loop for 4 bytes', align=Align.INLINE)
d.comment(0x886B, 'X=5: data extent for filename copy', align=Align.INLINE)
d.comment(0x886F, 'A=1: encode protection from param block', align=Align.INLINE)
d.comment(0x8872, 'Store encoded attrs at &0F0E', align=Align.INLINE)
d.comment(0x8875, 'Y=9: source offset in param block', align=Align.INLINE)
d.comment(0x8877, 'X=8: dest offset in cmd buffer', align=Align.INLINE)
d.comment(0x8879, 'Load byte from param block', align=Align.INLINE)
d.comment(0x887B, 'Store to FS cmd buffer', align=Align.INLINE)
d.comment(0x887E, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x887F, 'Next dest byte', align=Align.INLINE)
d.comment(0x8880, 'Loop until X=0 (8 bytes copied)', align=Align.INLINE)
d.comment(0x8882, 'X=&0A: data extent past attrs+addrs', align=Align.INLINE)
d.comment(0x8884, 'Append filename to cmd buffer', align=Align.INLINE)
d.comment(0x8887, 'Y=&13: fn code for FCSAVE (write attrs)', align=Align.INLINE)
d.comment(0x8889, 'ALWAYS branch to send command', align=Align.INLINE)
d.comment(0x888B, 'A=6: copy filename (delete)', align=Align.INLINE)
d.comment(0x888E, 'Y=&14: fn code for FCDEL (delete)', align=Align.INLINE)

d.label(0x8890, 'send_fs_cmd_v1')
d.comment(0x8890, 'Set V=1 (BIT trick: &B3 has bit 6 set)', align=Align.INLINE)
d.comment(0x8893, 'Send via prepare_fs_cmd_v (V=1 path)', align=Align.INLINE)

d.label(0x8896, 'check_attrib_result')
d.comment(0x8896, 'C=1: &D6 not-found, skip to return', align=Align.INLINE)
d.comment(0x8898, 'C=0: success, copy reply to param block', align=Align.INLINE)
d.comment(0x889A, 'A=4: encode attrs from param block', align=Align.INLINE)
d.comment(0x889D, 'Store encoded attrs at &0F06', align=Align.INLINE)
d.comment(0x88A0, 'X=2: data extent (1 attr byte + fn)', align=Align.INLINE)
d.comment(0x88A2, 'ALWAYS branch to append filename', align=Align.INLINE)
d.comment(0x88A4, 'X=1: filename only, no data extent', align=Align.INLINE)
d.comment(0x88A6, 'Copy filename to cmd buffer', align=Align.INLINE)
d.comment(0x88A9, 'Y=&12: fn code for FCEXAM (read info)', align=Align.INLINE)
d.comment(0x88AE, 'Save object type from FS reply', align=Align.INLINE)
d.comment(0x88B1, 'Clear reply byte (X=0 on success)', align=Align.INLINE)
d.comment(0x88B4, 'Clear length high byte in reply', align=Align.INLINE)
d.comment(0x88B7, 'Decode 5-bit access byte from FS reply', align=Align.INLINE)
d.comment(0x88BF, 'Y=&0E: attrs offset in param block', align=Align.INLINE)
d.comment(0x88C1, 'Store decoded attrs at param block +&0E', align=Align.INLINE)
d.comment(0x88C3, 'Y=&0D: start copy below attrs', align=Align.INLINE)
d.comment(0x88C4, 'X=&0C: copy from reply offset &0C down', align=Align.INLINE)
d.comment(0x88C6, 'Load reply byte (load/exec/length)', align=Align.INLINE)
d.comment(0x88C9, 'Store to param block', align=Align.INLINE)
d.comment(0x88CB, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x88CC, 'Next source byte', align=Align.INLINE)
d.comment(0x88CD, 'Loop until X=0 (12 bytes copied)', align=Align.INLINE)
d.comment(0x88CF, 'X=0 -> X=2 for length high copy', align=Align.INLINE)
d.comment(0x88D0, 'INX again: X=2', align=Align.INLINE)
d.comment(0x88D1, 'Y=&11: length high dest in param block', align=Align.INLINE)
d.comment(0x88D3, 'Load length high byte from reply', align=Align.INLINE)
d.comment(0x88D6, 'Store to param block', align=Align.INLINE)
d.comment(0x88D8, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x88D9, 'Next source byte', align=Align.INLINE)
d.comment(0x88DA, 'Loop for 3 length-high bytes', align=Align.INLINE)

d.label(0x88E0, 'attrib_error_exit')
d.comment(0x88E0, 'A>=0: branch to restore_args_return', align=Align.INLINE)
d.comment(0x88E2, 'Save A/X/Y registers for later restore', align=Align.INLINE)
d.comment(0x88E5, 'Function >= 3?', align=Align.INLINE)
d.comment(0x88E7, 'A>=3 (ensure/flush): no-op for NFS', align=Align.INLINE)
d.comment(0x88E9, 'Test file handle', align=Align.INLINE)
d.comment(0x88EB, 'Y=0: FS-level query, not per-file', align=Align.INLINE)
d.comment(0x88ED, 'Convert handle to bitmask', align=Align.INLINE)
d.comment(0x88F0, 'Store bitmask as first cmd data byte', align=Align.INLINE)
d.comment(0x88F3, 'LSR splits A: C=1 means write (A=1)', align=Align.INLINE)
d.comment(0x88F4, 'Store function code to cmd data byte 2', align=Align.INLINE)
d.comment(0x88F7, 'C=1: write path, copy ptr from caller', align=Align.INLINE)
d.comment(0x88F9, 'Y=&0C: FCRDSE (read sequential pointer)', align=Align.INLINE)
d.comment(0x88FB, 'X=2: 3 data bytes in command', align=Align.INLINE)
d.comment(0x88FD, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8900, 'Clear last-byte flag on success', align=Align.INLINE)
d.comment(0x8902, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x8904, 'Y=2: copy 3 bytes of file pointer', align=Align.INLINE)
d.comment(0x8906, 'Zero high byte of 3-byte pointer', align=Align.INLINE)

d.label(0x8908, 'copy_fileptr_reply')
d.comment(0x8908, 'Read reply byte from FS cmd data', align=Align.INLINE)
d.comment(0x890B, "Store to caller's control block", align=Align.INLINE)
d.comment(0x890D, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x890E, 'Next source byte', align=Align.INLINE)
d.comment(0x890F, 'Loop for all 3 bytes', align=Align.INLINE)

d.label(0x8911, 'argsv_check_return')
d.comment(0x8911, 'C=0 (read): return to caller', align=Align.INLINE)
d.comment(0x8913, 'Save bitmask for set_fs_flag later', align=Align.INLINE)
d.comment(0x8914, 'Push bitmask', align=Align.INLINE)
d.comment(0x8915, 'Y=3: copy 4 bytes of file pointer', align=Align.INLINE)

d.label(0x8917, 'copy_fileptr_to_cmd')
d.comment(0x8917, "Read caller's pointer byte", align=Align.INLINE)
d.comment(0x8919, 'Store to FS command data area', align=Align.INLINE)
d.comment(0x891C, 'Next source byte', align=Align.INLINE)
d.comment(0x891D, 'Next destination byte', align=Align.INLINE)
d.comment(0x891E, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8920, 'Y=&0D: FCWRSE (write sequential pointer)', align=Align.INLINE)
d.comment(0x8922, 'X=5: 6 data bytes in command', align=Align.INLINE)
d.comment(0x8924, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8927, 'Save not-found status from X', align=Align.INLINE)
d.comment(0x8929, 'Recover bitmask for EOF hint update', align=Align.INLINE)
d.comment(0x892A, 'Set EOF hint bit for this handle', align=Align.INLINE)
d.comment(0x892D, 'A = saved function code / command', align=Align.INLINE)

d.label(0x892F, 'restore_xy_return')
d.comment(0x892F, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x8931, 'Y = saved control block ptr high', align=Align.INLINE)
d.comment(0x8933, 'Return to MOS with registers restored', align=Align.INLINE)

d.label(0x893B, 'halve_args_a')
d.comment(0x893B, 'Shared: halve A (A=0 or A=2 paths)', align=Align.INLINE)
d.comment(0x893C, 'Return with A = FS number or 1', align=Align.INLINE)
d.comment(0x893E, "Copy command context to caller's block", align=Align.INLINE)
d.comment(0x8941, "Store to caller's parameter block", align=Align.INLINE)
d.comment(0x8943, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8944, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x894A, 'Save A/X/Y and set up pointers', align=Align.INLINE)
d.comment(0x894D, 'SEC distinguishes open (A>0) from close', align=Align.INLINE)
d.comment(0x8952, 'A=0: close file(s)', align=Align.INLINE)
d.comment(0x8954, 'Valid open modes: &40, &80, &C0 only', align=Align.INLINE)
d.comment(0x8956, 'Invalid mode bits: return', align=Align.INLINE)
d.comment(0x8958, 'A = original mode byte', align=Align.INLINE)
d.comment(0x8959, 'Convert MOS mode to FS protocol flags', align=Align.INLINE)
d.comment(0x895B, 'ASL: shift mode bits left', align=Align.INLINE)
d.comment(0x895C, 'Flag 1: read/write direction', align=Align.INLINE)
d.comment(0x895F, 'ROL: Flag 2 into bit 0', align=Align.INLINE)
d.comment(0x8960, 'Flag 2: create vs existing file', align=Align.INLINE)
d.comment(0x8963, 'X=2: copy after 2-byte flags', align=Align.INLINE)
d.comment(0x8965, 'Copy filename to FS command buffer', align=Align.INLINE)
d.comment(0x8968, 'Y=6: FS function code FCOPEN', align=Align.INLINE)
d.comment(0x896A, 'Set V flag from l83b3 bit 6', align=Align.INLINE)
d.comment(0x896D, 'Build and send FS open command', align=Align.INLINE)
d.comment(0x8970, 'Error: restore and return', align=Align.INLINE)
d.comment(0x8972, 'Load reply handle from FS', align=Align.INLINE)
d.comment(0x8975, 'X = new file handle', align=Align.INLINE)
d.comment(0x8976, 'Set EOF hint + sequence bits', align=Align.INLINE)
d.comment(0x8984, 'ALWAYS branch to restore and return', align=Align.INLINE)
d.comment(0x8986, 'A = handle (Y preserved in A)', align=Align.INLINE)
d.comment(0x8987, 'Y>0: close single file', align=Align.INLINE)
d.comment(0x8989, 'Close SPOOL/EXEC before FS close-all', align=Align.INLINE)
d.comment(0x898E, 'Y=0: close all handles on server', align=Align.INLINE)
d.comment(0x8990, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x899A, 'Reply handle for flag update', align=Align.INLINE)
d.comment(0x899D, 'Update EOF/sequence tracking bits', align=Align.INLINE)

d.label(0x89A0, 'close_opt_return')
d.comment(0x89A0, 'C=0: restore A/X/Y and return', align=Align.INLINE)
d.comment(0x89A2, 'Is it *OPT 4,Y?', align=Align.INLINE)
d.comment(0x89A4, 'No: check for *OPT 1', align=Align.INLINE)
d.comment(0x89A6, 'Y must be 0-3 for boot option', align=Align.INLINE)
d.comment(0x89A8, 'Y < 4: valid boot option', align=Align.INLINE)

d.label(0x89B2, 'set_messages_flag')
d.comment(0x89B2, 'Set local messages flag (*OPT 1,Y)', align=Align.INLINE)
d.comment(0x89B5, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x89B7, 'Error index 7 (Bad option)', align=Align.INLINE)
d.comment(0x89B9, 'Generate BRK error', align=Align.INLINE)
d.comment(0x89BC, 'Boot option value in FS command', align=Align.INLINE)
d.comment(0x89BF, 'Y=&16: FS function code FCOPT', align=Align.INLINE)
d.comment(0x89C4, 'Restore Y from saved value', align=Align.INLINE)
d.comment(0x89C6, 'Cache boot option locally', align=Align.INLINE)

d.label(0x89C9, 'opt_return')
d.comment(0x89C9, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x89CB, 'Y=9: adjust 9 address bytes', align=Align.INLINE)
d.comment(0x89CD, 'Adjust with carry clear', align=Align.INLINE)
d.comment(0x89D0, 'Y=1: adjust 1 address byte', align=Align.INLINE)
d.comment(0x89D2, 'C=0 for address adjustment', align=Align.INLINE)

d.label(0x89D5, 'adjust_addr_byte')

d.label(0x89E1, 'subtract_adjust')
d.comment(0x89EB, 'Save A/X/Y to FS workspace', align=Align.INLINE)
d.comment(0x89EE, 'X = call number for range check', align=Align.INLINE)
d.comment(0x89EF, 'A=0: invalid, restore and return', align=Align.INLINE)
d.comment(0x89F1, 'Convert to 0-based (A=0..7)', align=Align.INLINE)
d.comment(0x89F2, 'Range check: must be 0-7', align=Align.INLINE)
d.comment(0x89F4, 'In range: continue to handler', align=Align.INLINE)
d.comment(0x89F6, 'Out of range: restore args and return', align=Align.INLINE)
d.comment(0x89F9, 'Recover 0-based function code', align=Align.INLINE)
d.comment(0x89FA, 'Y=0: param block byte 0 (file handle)', align=Align.INLINE)
d.comment(0x89FC, 'Save function code on stack', align=Align.INLINE)
d.comment(0x89FD, 'A>=4: info queries, dispatch separately', align=Align.INLINE)
d.comment(0x89FF, 'A<4: file read/write operations', align=Align.INLINE)
d.comment(0x8A01, 'Dispatch to OSGBPB 5-8 info handler', align=Align.INLINE)
d.comment(0x8A04, 'Get file handle from param block byte 0', align=Align.INLINE)
d.comment(0x8A06, 'Convert handle to bitmask for EOF flags', align=Align.INLINE)
d.comment(0x8A09, 'Store handle in FS command data', align=Align.INLINE)
d.comment(0x8A0C, 'Y=&0B: start at param block byte 11', align=Align.INLINE)
d.comment(0x8A0E, 'X=6: copy 6 bytes of transfer params', align=Align.INLINE)
d.comment(0x8A10, 'Load param block byte', align=Align.INLINE)
d.comment(0x8A12, 'Store to FS command buffer at &0F06+X', align=Align.INLINE)
d.comment(0x8A15, 'Previous param block byte', align=Align.INLINE)
d.comment(0x8A16, 'Skip param block offset 8 (the handle)', align=Align.INLINE)
d.comment(0x8A18, 'Not at handle offset: continue', align=Align.INLINE)
d.comment(0x8A1A, 'Extra DEY to skip handle byte', align=Align.INLINE)
d.comment(0x8A1B, 'Decrement copy counter', align=Align.INLINE)
d.comment(0x8A1C, 'Loop for all 6 bytes', align=Align.INLINE)
d.comment(0x8A1E, 'Recover function code from stack', align=Align.INLINE)
d.comment(0x8A1F, 'LSR: odd=read (C=1), even=write (C=0)', align=Align.INLINE)
d.comment(0x8A20, 'Save function code again (need C later)', align=Align.INLINE)
d.comment(0x8A21, 'Even (write): X stays 0', align=Align.INLINE)
d.comment(0x8A23, 'Odd (read): X=1', align=Align.INLINE)
d.comment(0x8A24, 'Store FS direction flag', align=Align.INLINE)
d.comment(0x8A27, 'Y=&0B: command data extent', align=Align.INLINE)
d.comment(0x8A29, 'Command &91=put, &92=get', align=Align.INLINE)
d.comment(0x8A2B, 'Recover function code', align=Align.INLINE)
d.comment(0x8A2C, 'Save again for later direction check', align=Align.INLINE)
d.comment(0x8A2D, 'Even (write): keep &91 and Y=&0B', align=Align.INLINE)
d.comment(0x8A2F, 'Odd (read): use &92 (get) instead', align=Align.INLINE)
d.comment(0x8A31, 'Read: one fewer data byte in command', align=Align.INLINE)

d.label(0x8A32, 'gbpb_write_path')
d.comment(0x8A32, 'Store port to FS command URD field', align=Align.INLINE)
d.comment(0x8A35, 'Save port for error recovery', align=Align.INLINE)
d.comment(0x8A37, 'X=8: command data bytes', align=Align.INLINE)
d.comment(0x8A39, 'Load handle from FS command data', align=Align.INLINE)
d.comment(0x8A3C, 'Build FS command with handle+flag', align=Align.INLINE)
d.comment(0x8A3F, 'Save seq# for byte-stream flow control', align=Align.INLINE)
d.comment(0x8A41, 'Store to FS sequence number workspace', align=Align.INLINE)
d.comment(0x8A44, 'X=4: copy 4 address bytes', align=Align.INLINE)
d.comment(0x8A46, 'Set up source/dest from param block', align=Align.INLINE)
d.comment(0x8A48, 'Store as source address', align=Align.INLINE)
d.comment(0x8A4B, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x8A4E, 'Skip 4 bytes to reach transfer length', align=Align.INLINE)
d.comment(0x8A51, 'Dest = source + length', align=Align.INLINE)
d.comment(0x8A53, 'Store as end address', align=Align.INLINE)
d.comment(0x8A56, 'Back 3 to align for next iteration', align=Align.INLINE)
d.comment(0x8A59, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8A5A, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8A5C, 'X=1 after loop', align=Align.INLINE)
d.comment(0x8A5D, 'Copy CSD data to command buffer', align=Align.INLINE)
d.comment(0x8A60, 'Store at &0F06+X', align=Align.INLINE)
d.comment(0x8A63, 'Decrement counter', align=Align.INLINE)
d.comment(0x8A64, 'Loop for X=1,0', align=Align.INLINE)
d.comment(0x8A66, 'Odd (read): send data to FS first', align=Align.INLINE)
d.comment(0x8A67, 'Non-zero: skip write path', align=Align.INLINE)
d.comment(0x8A69, 'Load port for transfer setup', align=Align.INLINE)
d.comment(0x8A6C, 'Transfer data blocks to fileserver', align=Align.INLINE)

d.label(0x8A78, 'wait_fs_reply')
d.comment(0x8A78, 'Wait for FS reply command', align=Align.INLINE)
d.comment(0x8A7B, 'Load handle mask for EOF flag update', align=Align.INLINE)
d.comment(0x8A7D, 'Check FS reply: bit 7 = not at EOF', align=Align.INLINE)
d.comment(0x8A80, 'Bit 7 set: not EOF, skip clear', align=Align.INLINE)
d.comment(0x8A82, 'At EOF: clear EOF hint for this handle', align=Align.INLINE)

d.label(0x8A85, 'skip_clear_flag')
d.comment(0x8A85, 'Set EOF hint flag (may be at EOF)', align=Align.INLINE)
d.comment(0x8A88, 'Direction=0: forward adjustment', align=Align.INLINE)
d.comment(0x8A8A, 'Adjust param block addrs by +9 bytes', align=Align.INLINE)
d.comment(0x8A8D, 'Direction=&FF: reverse adjustment', align=Align.INLINE)
d.comment(0x8A8F, 'SEC for reverse subtraction', align=Align.INLINE)
d.comment(0x8A90, 'Adjust param block addrs (reverse)', align=Align.INLINE)
d.comment(0x8A93, 'Shift bit 7 into C for return flag', align=Align.INLINE)
d.comment(0x8A96, 'Return via restore_args path', align=Align.INLINE)

d.label(0x8A99, 'get_disc_title')
d.comment(0x8A99, 'Y=&15: function code for disc title', align=Align.INLINE)
d.comment(0x8A9B, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8A9E, 'Load boot option from FS workspace', align=Align.INLINE)
d.comment(0x8AA1, 'Store boot option in reply area', align=Align.INLINE)
d.comment(0x8AA4, 'X=0: reply data start offset', align=Align.INLINE)
d.comment(0x8AA6, 'Clear reply buffer high byte', align=Align.INLINE)
d.comment(0x8AA8, 'A=&12: 18 bytes of reply data', align=Align.INLINE)
d.comment(0x8AAA, 'Store as byte count for copy', align=Align.INLINE)
d.comment(0x8AAC, 'ALWAYS branch to copy_reply_to_caller', align=Align.INLINE)
d.comment(0x8AAE, 'Y=4: check param block byte 4', align=Align.INLINE)
d.comment(0x8AB0, 'Check if destination is in Tube space', align=Align.INLINE)
d.comment(0x8AB3, 'No Tube: skip Tube address check', align=Align.INLINE)
d.comment(0x8AB5, 'Compare Tube flag with addr byte 4', align=Align.INLINE)
d.comment(0x8AB7, 'Mismatch: not Tube space', align=Align.INLINE)
d.comment(0x8ABA, 'Y=3: subtract addr byte 3 from flag', align=Align.INLINE)

d.label(0x8ABC, 'store_tube_flag')
d.comment(0x8ABC, 'Non-zero = Tube transfer required', align=Align.INLINE)
d.comment(0x8ABE, 'Copy param block bytes 1-4 to workspace', align=Align.INLINE)
d.comment(0x8AC0, 'Store to &BD+Y workspace area', align=Align.INLINE)
d.comment(0x8AC3, 'Previous byte', align=Align.INLINE)
d.comment(0x8AC4, 'Loop for bytes 3,2,1', align=Align.INLINE)
d.comment(0x8AC6, 'Sub-function: AND #3 of (original A - 4)', align=Align.INLINE)
d.comment(0x8AC7, 'Mask to 0-3 (OSGBPB 5-8 → 0-3)', align=Align.INLINE)
d.comment(0x8AC9, 'A=0 (OSGBPB 5): read disc title', align=Align.INLINE)
d.comment(0x8ACB, 'LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)', align=Align.INLINE)
d.comment(0x8ACC, 'A=0 (OSGBPB 6): read CSD/LIB name', align=Align.INLINE)
d.comment(0x8ACE, 'C=1 (OSGBPB 8): read filenames from dir', align=Align.INLINE)

d.label(0x8AD0, 'gbpb6_read_name')
d.comment(0x8AD0, 'Y=0 for CSD or carry for fn code select', align=Align.INLINE)
d.comment(0x8AD1, 'Get CSD/LIB/URD handles for FS command', align=Align.INLINE)
d.comment(0x8AD4, 'Store CSD handle in command buffer', align=Align.INLINE)
d.comment(0x8AD7, 'Load LIB handle from workspace', align=Align.INLINE)
d.comment(0x8ADA, 'Store LIB handle in command buffer', align=Align.INLINE)
d.comment(0x8ADD, 'Load URD handle from workspace', align=Align.INLINE)
d.comment(0x8AE0, 'Store URD handle in command buffer', align=Align.INLINE)
d.comment(0x8AE3, 'X=&12: buffer extent for command data', align=Align.INLINE)
d.comment(0x8AE5, 'Store X as function code in header', align=Align.INLINE)
d.comment(0x8AE8, '&0D = 13 bytes of reply data expected', align=Align.INLINE)
d.comment(0x8AEA, 'Store reply length in command buffer', align=Align.INLINE)
d.comment(0x8AED, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8AEF, 'LSR: &0D >> 1 = 6', align=Align.INLINE)
d.comment(0x8AF0, 'Store as command data byte', align=Align.INLINE)
d.comment(0x8AF3, 'CLC for standard FS path', align=Align.INLINE)
d.comment(0x8AF9, 'INX: X=1 after build_send_fs_cmd', align=Align.INLINE)
d.comment(0x8AFA, 'Store X as reply start offset', align=Align.INLINE)
d.comment(0x8AFC, "Copy FS reply to caller's buffer", align=Align.INLINE)
d.comment(0x8AFE, 'Non-zero: use Tube transfer path', align=Align.INLINE)
d.comment(0x8B00, 'X = reply start offset', align=Align.INLINE)
d.comment(0x8B02, 'Y = reply buffer high byte', align=Align.INLINE)

d.label(0x8B04, 'copy_reply_bytes')
d.comment(0x8B04, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B07, "Store to caller's buffer", align=Align.INLINE)
d.comment(0x8B09, 'Next source byte', align=Align.INLINE)
d.comment(0x8B0A, 'Next destination byte', align=Align.INLINE)
d.comment(0x8B0B, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8B0D, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8B0F, 'ALWAYS branch to exit', align=Align.INLINE)

d.label(0x8B11, 'tube_transfer')
d.comment(0x8B11, 'Claim Tube transfer channel', align=Align.INLINE)
d.comment(0x8B14, 'A=1: Tube claim type 1 (write)', align=Align.INLINE)
d.comment(0x8B16, 'X = param block address low', align=Align.INLINE)
d.comment(0x8B18, 'Y = param block address high', align=Align.INLINE)
d.comment(0x8B1A, 'INX: advance past byte 0', align=Align.INLINE)
d.comment(0x8B1B, 'No page wrap: keep Y', align=Align.INLINE)
d.comment(0x8B1D, 'Page wrap: increment high byte', align=Align.INLINE)

d.label(0x8B1E, 'no_page_wrap')
d.comment(0x8B1E, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x8B21, 'X = reply data start offset', align=Align.INLINE)
d.comment(0x8B23, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B26, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x8B29, 'Next source byte', align=Align.INLINE)
d.comment(0x8B2A, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8B2C, 'Loop until all bytes sent to Tube', align=Align.INLINE)
d.comment(0x8B2E, 'Release Tube after transfer complete', align=Align.INLINE)
d.comment(0x8B30, 'Release Tube address claim', align=Align.INLINE)

d.label(0x8B33, 'gbpb_done')
d.comment(0x8B33, 'Return via restore_args path', align=Align.INLINE)

d.label(0x8B36, 'gbpb8_read_dir')
d.comment(0x8B36, 'OSGBPB 8: read filenames from dir', align=Align.INLINE)
d.comment(0x8B38, 'Byte 9: number of entries to read', align=Align.INLINE)
d.comment(0x8B3A, 'Store as reply count in command buffer', align=Align.INLINE)
d.comment(0x8B3D, 'Y=5: byte 5 = starting entry number', align=Align.INLINE)
d.comment(0x8B3F, 'Load starting entry number', align=Align.INLINE)
d.comment(0x8B41, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8B44, 'X=&0D: command data extent', align=Align.INLINE)
d.comment(0x8B46, 'Store extent in command buffer', align=Align.INLINE)
d.comment(0x8B49, 'Y=2: function code for dir read', align=Align.INLINE)
d.comment(0x8B4B, 'Store 2 as reply data start offset', align=Align.INLINE)
d.comment(0x8B4D, 'Store 2 as command data byte', align=Align.INLINE)
d.comment(0x8B50, 'Y=3: function code for header read', align=Align.INLINE)
d.comment(0x8B54, 'X=0 after FS command completes', align=Align.INLINE)
d.comment(0x8B56, 'Load reply entry count', align=Align.INLINE)
d.comment(0x8B59, 'Store at param block byte 0 (X=0)', align=Align.INLINE)
d.comment(0x8B5B, 'Load entries-read count from reply', align=Align.INLINE)
d.comment(0x8B5E, 'Y=9: param block byte 9', align=Align.INLINE)
d.comment(0x8B60, 'Add to starting entry number', align=Align.INLINE)
d.comment(0x8B62, 'Update param block with new position', align=Align.INLINE)
d.comment(0x8B64, 'Load total reply length', align=Align.INLINE)
d.comment(0x8B66, 'Subtract header (7 bytes) from reply len', align=Align.INLINE)
d.comment(0x8B68, 'Store adjusted length in command buffer', align=Align.INLINE)
d.comment(0x8B6B, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8B6D, 'Zero bytes: skip copy', align=Align.INLINE)
d.comment(0x8B6F, "Copy reply data to caller's buffer", align=Align.INLINE)

d.label(0x8B72, 'skip_copy_reply')
d.comment(0x8B72, 'X=2: clear 3 bytes', align=Align.INLINE)

d.label(0x8B74, 'zero_cmd_bytes')
d.comment(0x8B74, 'Zero out &0F07+X area', align=Align.INLINE)
d.comment(0x8B77, 'Next byte', align=Align.INLINE)
d.comment(0x8B78, 'Loop for X=2,1,0', align=Align.INLINE)
d.comment(0x8B7A, 'Adjust pointer by +1 (one filename read)', align=Align.INLINE)
d.comment(0x8B7D, 'SEC for reverse adjustment', align=Align.INLINE)
d.comment(0x8B7E, 'Reverse adjustment for updated counter', align=Align.INLINE)
d.comment(0x8B80, 'Load entries-read count', align=Align.INLINE)
d.comment(0x8B83, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8B86, 'Adjust param block addresses', align=Align.INLINE)
d.comment(0x8B89, 'Z=1: all done, exit', align=Align.INLINE)
d.comment(0x8B8B, 'A=&C3: Tube claim with retry', align=Align.INLINE)
d.comment(0x8B8D, 'Request Tube address claim', align=Align.INLINE)
d.comment(0x8B90, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x8B92, 'Tube claimed successfully', align=Align.INLINE)
d.comment(0x8B93, 'Save A/X/Y and set up command ptr', align=Align.INLINE)
d.comment(0x8B96, 'X=&FF: table index (pre-incremented)', align=Align.INLINE)

d.label(0x8B98, 'scan_cmd_table')
d.comment(0x8B98, 'Y=&FF: input index (pre-incremented)', align=Align.INLINE)
d.comment(0x8B9A, 'Advance input pointer', align=Align.INLINE)
d.comment(0x8B9B, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8B9C, 'Load table character', align=Align.INLINE)
d.comment(0x8B9F, 'Bit 7: end of name, dispatch', align=Align.INLINE)
d.comment(0x8BA1, 'XOR input char with table char', align=Align.INLINE)
d.comment(0x8BA3, 'Case-insensitive (clear bit 5)', align=Align.INLINE)
d.comment(0x8BA5, 'Match: continue comparing', align=Align.INLINE)
d.comment(0x8BA7, 'Mismatch: back up table pointer', align=Align.INLINE)
d.comment(0x8BA8, 'Skip to end of table entry', align=Align.INLINE)
d.comment(0x8BA9, 'Load table byte', align=Align.INLINE)
d.comment(0x8BAC, 'Loop until bit 7 set (end marker)', align=Align.INLINE)
d.comment(0x8BAE, "Check input for '.' abbreviation", align=Align.INLINE)
d.comment(0x8BB0, 'Skip past handler high byte', align=Align.INLINE)
d.comment(0x8BB1, "Is input '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8BB3, 'No: try next table entry', align=Align.INLINE)
d.comment(0x8BB5, "Yes: skip '.' in input", align=Align.INLINE)
d.comment(0x8BB6, 'Back to handler high byte', align=Align.INLINE)
d.comment(0x8BB7, 'ALWAYS branch; dispatch via BMI', align=Align.INLINE)

d.label(0x8BB9, 'dispatch_cmd')
d.comment(0x8BB9, 'Push handler address high byte', align=Align.INLINE)
d.comment(0x8BBA, 'Load handler address low byte', align=Align.INLINE)
d.comment(0x8BBD, 'Push handler address low byte', align=Align.INLINE)
d.comment(0x8C12, 'X=1: copy dir name at cmd offset 1', align=Align.INLINE)
d.comment(0x8C14, 'Copy directory name to command buffer', align=Align.INLINE)
d.comment(0x8C1C, 'X=3: start printing from reply offset 3', align=Align.INLINE)
d.comment(0x8C1E, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0x8C21, "Print '('", align=Align.INLINE)
d.comment(0x8C25, 'Load station number from FS reply', align=Align.INLINE)
d.comment(0x8C28, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x8C2B, "Print ')     '", align=Align.INLINE)
d.comment(0x8C37, 'Non-zero: Public access', align=Align.INLINE)
d.comment(0x8C39, "Print 'Owner' + CR", align=Align.INLINE)

d.label(0x8C44, 'print_public')
d.comment(0x8C44, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0x8C53, 'X=1: past command code byte', align=Align.INLINE)
d.comment(0x8C54, 'Y=&10: print 16 characters', align=Align.INLINE)
d.comment(0x8C56, 'Print disc/CSD name from reply', align=Align.INLINE)
d.comment(0x8C6B, 'X = boot option for name table lookup', align=Align.INLINE)
d.comment(0x8C6C, 'Print boot option as hex digit', align=Align.INLINE)
d.comment(0x8C6F, "Print ' ('", align=Align.INLINE)
d.comment(0x8C7F, 'Next character', align=Align.INLINE)
d.comment(0x8C80, 'Continue printing option name', align=Align.INLINE)

d.label(0x8C82, 'done_option_name')
d.comment(0x8C82, "Print ')' + CR + 'Dir. '", align=Align.INLINE)
d.comment(0x8CA0, 'Print library name', align=Align.INLINE)
d.comment(0x8CAB, 'Save start offset in zero page for loop', align=Align.INLINE)
d.comment(0x8CBD, 'Load column count for display format', align=Align.INLINE)
d.comment(0x8CBF, 'Store column count in command data', align=Align.INLINE)
d.comment(0x8CC2, 'X=3: copy directory name at offset 3', align=Align.INLINE)
d.comment(0x8CC4, 'Append directory name to examine command', align=Align.INLINE)

d.label(0x8D1D, 'jmp_restore_args')
d.comment(0x8D1D, 'Restore A/X/Y and return to caller', align=Align.INLINE)
d.comment(0x8D20, 'Set carry: LOGIN path (copy + boot)', align=Align.INLINE)
d.comment(0x8D21, 'Copy 4 bytes: boot option + 3 handles', align=Align.INLINE)
d.comment(0x8D23, 'SDISC: skip boot option, copy handles only', align=Align.INLINE)
d.comment(0x8D25, 'Load from FS reply (&0F05+X)', align=Align.INLINE)
d.comment(0x8D28, 'Store to handle workspace (&0E02+X)', align=Align.INLINE)
d.comment(0x8D2B, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8D2C, 'Loop while X >= 0', align=Align.INLINE)
d.comment(0x8D2E, 'SDISC: done, restore args and return', align=Align.INLINE)


d.subroutine(0x8D30, 'boot_cmd_execute', title='Execute boot command via OSCLI', description="""Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")
d.comment(0x8D30, 'Y = boot option from FS workspace', align=Align.INLINE)
d.comment(0x8D33, 'X = command string offset from table', align=Align.INLINE)
d.comment(0x8D36, 'Y = &8D (high byte of command address)', align=Align.INLINE)
d.comment(0x8D38, 'Execute boot command string via OSCLI', align=Align.INLINE)
d.comment(0x8DCC, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8DCF, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8DD1, 'Load stored handle value', align=Align.INLINE)
d.comment(0x8DD3, '&3F = unused/closed slot marker', align=Align.INLINE)
d.comment(0x8DD5, 'Slot in use: return actual value', align=Align.INLINE)
d.comment(0x8DD7, 'Return 0 for closed/invalid handle', align=Align.INLINE)

d.label(0x8DD9, 'store_handle_return')
d.comment(0x8DD9, 'Store result back to &F0', align=Align.INLINE)
d.comment(0x8DE2, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8DE5, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8DFE, 'Only OSWORDs &0F-&13 (index 0-4)', align=Align.INLINE)
d.comment(0x8E00, 'Index >= 5: not ours, return', align=Align.INLINE)
d.comment(0x8E03, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x8E06, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E07, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x8E0A, 'Dispatch table: low bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x8E0B, 'Y=2: save 3 bytes (&AA-&AC)', align=Align.INLINE)
d.comment(0x8E0D, 'Load param block pointer byte', align=Align.INLINE)
d.comment(0x8E10, 'Save to NFS workspace via (net_rx_ptr)', align=Align.INLINE)
d.comment(0x8E12, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8E13, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8E15, 'Y=0 after BPL exit; INY makes Y=1', align=Align.INLINE)
d.comment(0x8E16, 'Read sub-function code from (&F0)+1', align=Align.INLINE)
d.comment(0x8E39, 'User TX CB in workspace page (high byte)', align=Align.INLINE)
d.comment(0x8E3B, 'Set param block high byte', align=Align.INLINE)
d.comment(0x8E3D, 'Set LTXCBP high byte for low-level TX', align=Align.INLINE)
d.comment(0x8E3F, '&6F: offset into workspace for user TXCB', align=Align.INLINE)
d.comment(0x8E41, 'Set param block low byte', align=Align.INLINE)
d.comment(0x8E43, 'Set LTXCBP low byte for low-level TX', align=Align.INLINE)
d.comment(0x8E45, 'X=15: copy 16 bytes (OSWORD param block)', align=Align.INLINE)
d.comment(0x8E47, 'Copy param block to user TX control block', align=Align.INLINE)
d.comment(0x8E54, 'Set source high byte from workspace page', align=Align.INLINE)
d.comment(0x8E56, 'Store as copy source high byte in &BF', align=Align.INLINE)
d.comment(0x8E58, 'JSRSIZ at workspace offset &7F', align=Align.INLINE)
d.comment(0x8E5A, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8E5C, 'Y=&80: start of JSR argument data', align=Align.INLINE)
d.comment(0x8E5D, 'Store &80 as copy source low byte', align=Align.INLINE)
d.comment(0x8E5F, 'X = buffer size (loop counter)', align=Align.INLINE)
d.comment(0x8E60, 'X = size-1 (0-based count for copy)', align=Align.INLINE)
d.comment(0x8E61, 'Y=0: start of destination param block', align=Align.INLINE)
d.comment(0x8E63, 'Copy X+1 bytes from workspace to param', align=Align.INLINE)
d.comment(0x8E6B, 'Y=&7F: JSRSIZ offset (READRB entry)', align=Align.INLINE)
d.comment(0x8E6D, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8E6F, 'Y=1: param block offset for size byte', align=Align.INLINE)
d.comment(0x8E71, 'Store buffer size to (&F0)+1', align=Align.INLINE)
d.comment(0x8E73, 'Y=2: param block offset for args size', align=Align.INLINE)
d.comment(0x8E74, 'A=&80: argument data starts at offset &80', align=Align.INLINE)
d.comment(0x8E76, 'Store args start offset to (&F0)+2', align=Align.INLINE)
d.comment(0x8E82, 'Sub-function 4 or 5: read/set protection', align=Align.INLINE)
d.comment(0x8E84, 'LSR: 0->0, 1->0, 2->1, 3->1', align=Align.INLINE)
d.comment(0x8E85, 'X=&0D: default to static workspace page', align=Align.INLINE)
d.comment(0x8E87, 'Transfer LSR result to Y for indexing', align=Align.INLINE)
d.comment(0x8E88, 'Y=0 (sub 0-1): use page &0D', align=Align.INLINE)
d.comment(0x8E8A, 'Y=1 (sub 2-3): use dynamic workspace', align=Align.INLINE)

d.label(0x8E8C, 'set_workspace_page')
d.comment(0x8E8C, 'Store workspace page in &BF (hi byte)', align=Align.INLINE)
d.comment(0x8E8E, 'Load offset: &FF (sub 0-1) or &01 (sub 2-3)', align=Align.INLINE)
d.comment(0x8E91, 'Store offset in &BE (lo byte)', align=Align.INLINE)
d.comment(0x8E93, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0x8E95, 'Y=1: start at param block offset 1', align=Align.INLINE)
d.comment(0x8E9C, 'LSR A: test bit 0 of sub-function', align=Align.INLINE)
d.comment(0x8E9D, 'Y=1: offset for protection byte', align=Align.INLINE)
d.comment(0x8E9E, 'Load protection byte from param block', align=Align.INLINE)
d.comment(0x8EA0, 'C=1 (odd sub): set protection', align=Align.INLINE)
d.comment(0x8EA2, 'C=0 (even sub): read current status', align=Align.INLINE)
d.comment(0x8EA5, 'Return current value to param block', align=Align.INLINE)
d.comment(0x8EA7, 'Update protection status', align=Align.INLINE)
d.comment(0x8EAA, 'Also save as JSR mask backup', align=Align.INLINE)
d.comment(0x8EB8, 'Sub-function 8: read local station number', align=Align.INLINE)
d.comment(0x8EBA, 'Match: read cached station ID from RX buffer', align=Align.INLINE)
d.comment(0x8EBC, 'Sub-function 9: read args size', align=Align.INLINE)
d.comment(0x8EBE, 'Match: read ARGS buffer info', align=Align.INLINE)
d.comment(0x8EC0, 'Sub >= 10 (bit 7 clear): read error', align=Align.INLINE)
d.comment(0x8EC2, 'Y=3: start from handle 3 (descending)', align=Align.INLINE)
d.comment(0x8EC4, 'LSR: test read/write bit', align=Align.INLINE)
d.comment(0x8EC5, 'C=0: read handles from workspace', align=Align.INLINE)
d.comment(0x8EC7, 'Init loop counter at Y=3', align=Align.INLINE)

d.label(0x8EC9, 'copy_handles_to_ws')
d.comment(0x8EC9, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8ECB, "Read handle from caller's param block", align=Align.INLINE)
d.comment(0x8ECD, 'Convert handle number to bitmask', align=Align.INLINE)
d.comment(0x8ED0, 'TYA: get bitmask result', align=Align.INLINE)
d.comment(0x8ED1, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8ED3, 'Store bitmask to FS server table', align=Align.INLINE)
d.comment(0x8ED6, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8ED8, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8EEC, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8EED, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8EF1, 'Workspace page high byte', align=Align.INLINE)
d.comment(0x8EF3, 'Set up pointer high byte in &AC', align=Align.INLINE)
d.comment(0x8EF5, 'Save param block high byte in &AB', align=Align.INLINE)
d.comment(0x8EF7, 'Disable user RX during CB operation', align=Align.INLINE)
d.comment(0x8EFA, 'Read first byte of param block', align=Align.INLINE)
d.comment(0x8EFC, 'Save: 0=open new, non-zero=read RXCB', align=Align.INLINE)
d.comment(0x8EFE, 'Non-zero: read specified RXCB', align=Align.INLINE)
d.comment(0x8F00, 'Start scan from RXCB #3 (0-2 reserved)', align=Align.INLINE)
d.comment(0x8F02, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8F05, 'Invalid RXCB: return zero', align=Align.INLINE)
d.comment(0x8F07, 'LSR twice: byte offset / 4', align=Align.INLINE)
d.comment(0x8F08, 'Yields RXCB number from offset', align=Align.INLINE)
d.comment(0x8F09, 'X = RXCB number for iteration', align=Align.INLINE)
d.comment(0x8F0A, 'Read flag byte from RXCB workspace', align=Align.INLINE)
d.comment(0x8F0C, 'Zero = end of CB list', align=Align.INLINE)
d.comment(0x8F0E, '&3F = deleted slot, free for reuse', align=Align.INLINE)
d.comment(0x8F10, 'Found free slot', align=Align.INLINE)
d.comment(0x8F12, 'Try next RXCB', align=Align.INLINE)
d.comment(0x8F13, 'A = next RXCB number', align=Align.INLINE)
d.comment(0x8F14, 'Continue scan (always branches)', align=Align.INLINE)
d.comment(0x8F16, 'A = free RXCB number', align=Align.INLINE)
d.comment(0x8F17, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x8F19, "Return RXCB number to caller's byte 0", align=Align.INLINE)

d.label(0x8F1B, 'read_rxcb')
d.comment(0x8F1B, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8F1E, 'Invalid: write zero to param block', align=Align.INLINE)
d.comment(0x8F20, 'Y = offset-1: points to flag byte', align=Align.INLINE)
d.comment(0x8F21, 'Set &AB = workspace ptr low byte', align=Align.INLINE)
d.comment(0x8F23, '&C0: test mask for flag byte', align=Align.INLINE)
d.comment(0x8F25, 'Y=1: flag byte offset in RXCB', align=Align.INLINE)
d.comment(0x8F29, 'Compare Y(1) with saved byte (open/read)', align=Align.INLINE)
d.comment(0x8F2B, 'ADC flag: test if slot is in use', align=Align.INLINE)
d.comment(0x8F2F, 'Negative: slot has received data', align=Align.INLINE)

d.label(0x8F31, 'copy_rxcb_to_param')
d.comment(0x8F31, 'C=0: workspace-to-param direction', align=Align.INLINE)
d.comment(0x8F32, 'Copy RXCB data to param block', align=Align.INLINE)
d.comment(0x8F35, 'Done: skip deletion on error', align=Align.INLINE)
d.comment(0x8F37, 'Mark CB as consumed (consume-once)', align=Align.INLINE)
d.comment(0x8F39, 'Y=1: flag byte offset', align=Align.INLINE)
d.comment(0x8F3B, 'Write &3F to mark slot deleted', align=Align.INLINE)
d.comment(0x8F3D, 'Branch to exit (always taken)', align=Align.INLINE)
d.comment(0x8F3F, 'Advance through multi-byte field', align=Align.INLINE)
d.comment(0x8F41, 'Loop until all bytes processed', align=Align.INLINE)
d.comment(0x8F43, 'Y=-1 → Y=0 after STA below', align=Align.INLINE)
d.comment(0x8F44, 'Return zero (no free RXCB found)', align=Align.INLINE)

d.label(0x8F46, 'reenable_rx')
d.comment(0x8F46, 'Re-enable user RX', align=Align.INLINE)
d.comment(0x8F4D, 'Y=2: copy 3 bytes (indices 2,1,0)', align=Align.INLINE)
d.comment(0x8F5A, 'A = base address low byte', align=Align.INLINE)
d.comment(0x8F5C, 'A = base + 1 (skip length byte)', align=Align.INLINE)
d.comment(0x8F61, 'Read data length from (&F0)+1', align=Align.INLINE)
d.comment(0x8F63, 'A = data length byte', align=Align.INLINE)
d.comment(0x8F65, 'Workspace offset &20 = RX data end', align=Align.INLINE)
d.comment(0x8F67, 'A = base + length = end address low', align=Align.INLINE)
d.comment(0x8F69, 'Store low byte of 16-bit address', align=Align.INLINE)
d.comment(0x8F6B, 'Advance to high byte offset', align=Align.INLINE)
d.comment(0x8F6C, 'A = high byte of base address', align=Align.INLINE)
d.comment(0x8F6E, 'Add carry for 16-bit addition', align=Align.INLINE)
d.comment(0x8F70, 'Store high byte', align=Align.INLINE)
d.comment(0x8F72, 'Return', align=Align.INLINE)
d.comment(0x8F75, 'A >= 1: handle TX result', align=Align.INLINE)
d.comment(0x8F77, 'Y=&2F: start of template (descending)', align=Align.INLINE)
d.comment(0x8F7C, 'Non-zero = use ROM template byte as-is', align=Align.INLINE)
d.comment(0x8F7E, 'Zero = substitute from NMI workspace', align=Align.INLINE)

d.label(0x8F81, 'store_txcb_byte')
d.comment(0x8F81, 'Store to dynamic workspace', align=Align.INLINE)
d.comment(0x8F83, 'Descend through template', align=Align.INLINE)
d.comment(0x8F84, 'Stop at offset &17', align=Align.INLINE)
d.comment(0x8F86, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8F88, 'Y=&18: TX block starts here', align=Align.INLINE)
d.comment(0x8F89, 'Point net_tx_ptr at workspace+&18', align=Align.INLINE)
d.comment(0x8F8B, 'Set up RX buffer start/end pointers', align=Align.INLINE)
d.comment(0x8F8E, 'Y=2: port byte offset in RXCB', align=Align.INLINE)
d.comment(0x8F90, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x8F92, 'Store port &90 at (&F0)+2', align=Align.INLINE)

d.label(0x8F96, 'copy_fs_addr')
d.comment(0x8F96, 'Copy FS station addr from workspace', align=Align.INLINE)
d.comment(0x8F99, 'Store to RX param block', align=Align.INLINE)
d.comment(0x8F9B, 'Next byte', align=Align.INLINE)
d.comment(0x8F9C, 'Done 3 bytes (Y=4,5,6)?', align=Align.INLINE)
d.comment(0x8F9E, 'No: continue copying', align=Align.INLINE)
d.comment(0x8FA0, 'High byte of workspace for TX ptr', align=Align.INLINE)
d.comment(0x8FA2, 'Store as TX pointer high byte', align=Align.INLINE)
d.comment(0x8FA5, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x8FA8, 'Y=&2C: RX end address offset', align=Align.INLINE)
d.comment(0x8FAC, 'Store end address low byte (&FF)', align=Align.INLINE)
d.comment(0x8FAF, 'Store end address high byte (&FF)', align=Align.INLINE)
d.comment(0x8FB1, 'Y=&25: port byte in workspace RXCB', align=Align.INLINE)
d.comment(0x8FB3, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x8FB5, 'Store port to workspace RXCB', align=Align.INLINE)
d.comment(0x8FB8, 'A=&7F: flag byte = waiting for reply', align=Align.INLINE)
d.comment(0x8FBA, 'Store flag byte to workspace RXCB', align=Align.INLINE)

d.label(0x8FC1, 'handle_tx_result')
d.comment(0x8FC1, 'Save processor flags', align=Align.INLINE)
d.comment(0x8FC2, 'Y=1: first data byte offset', align=Align.INLINE)
d.comment(0x8FC4, 'Load first data byte from RX buffer', align=Align.INLINE)
d.comment(0x8FC6, 'X = first data byte (command code)', align=Align.INLINE)
d.comment(0x8FC7, 'Advance to next data byte', align=Align.INLINE)
d.comment(0x8FC8, 'Load station address high byte', align=Align.INLINE)
d.comment(0x8FCA, 'Advance past station addr', align=Align.INLINE)
d.comment(0x8FCB, 'Save Y as data index', align=Align.INLINE)
d.comment(0x8FCD, 'Store station addr hi at (net_rx_ptr)+&72', align=Align.INLINE)
d.comment(0x8FCF, 'Store to workspace', align=Align.INLINE)
d.comment(0x8FD2, 'A = command code (from X)', align=Align.INLINE)
d.comment(0x8FD3, 'Store station addr lo at (net_rx_ptr)+&71', align=Align.INLINE)
d.comment(0x8FD5, 'Restore flags from earlier PHP', align=Align.INLINE)
d.comment(0x8FD6, 'First call: adjust data length', align=Align.INLINE)

d.label(0x8FD8, 'send_data_bytes')
d.comment(0x8FDA, 'Advance data index for next iteration', align=Align.INLINE)
d.comment(0x8FDC, 'Load next data byte', align=Align.INLINE)
d.comment(0x8FF2, 'Not &0D: continue with next byte', align=Align.INLINE)
d.comment(0x8FF6, 'First-packet: set up control block', align=Align.INLINE)
d.comment(0x8FF9, 'Y=&7B: data length offset', align=Align.INLINE)
d.comment(0x8FFB, 'Load current data length', align=Align.INLINE)
d.comment(0x8FFD, 'Adjust data length by 3 for header bytes', align=Align.INLINE)
d.comment(0x8FFF, 'Store adjusted length', align=Align.INLINE)
d.comment(0x9001, 'Enable interrupts', align=Align.INLINE)
d.comment(0x9005, 'Transmit via tx_poll_ff', align=Align.INLINE)
d.comment(0x9008, 'Save processor status', align=Align.INLINE)
d.comment(0x9009, 'Save A (reason code)', align=Align.INLINE)
d.comment(0x900A, 'Save X', align=Align.INLINE)
d.comment(0x900B, 'Push X to stack', align=Align.INLINE)
d.comment(0x900C, 'Save Y', align=Align.INLINE)
d.comment(0x900D, 'Push Y to stack', align=Align.INLINE)
d.comment(0x900E, 'Get stack pointer for indexed access', align=Align.INLINE)
d.comment(0x9012, 'Reason codes 0-8 only', align=Align.INLINE)
d.comment(0x9014, 'Code >= 9: skip dispatch, restore regs', align=Align.INLINE)
d.comment(0x9016, 'X = reason code for table lookup', align=Align.INLINE)
d.comment(0x9017, 'Dispatch to handler via trampoline', align=Align.INLINE)
d.comment(0x901A, 'Restore Y', align=Align.INLINE)
d.comment(0x901B, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x901C, 'Restore X', align=Align.INLINE)
d.comment(0x901D, 'Transfer to X register', align=Align.INLINE)
d.comment(0x901E, 'Restore A', align=Align.INLINE)
d.comment(0x901F, 'Restore processor status flags', align=Align.INLINE)
d.comment(0x9020, 'Return with all registers preserved', align=Align.INLINE)
d.comment(0x9024, 'Push high byte of handler address', align=Align.INLINE)
d.comment(0x9025, 'Load handler low byte from table', align=Align.INLINE)
d.comment(0x9028, 'Push low byte of handler address', align=Align.INLINE)
d.comment(0x9029, 'Load workspace byte &EF for handler', align=Align.INLINE)
d.comment(0x902B, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0x9042, 'ASL: restore P after ROR zeroed carry', align=Align.INLINE)
d.comment(0x9045, 'Y = character to write', align=Align.INLINE)
d.comment(0x9046, 'Store character at workspace offset &DA', align=Align.INLINE)
d.comment(0x9048, 'Store char at workspace offset &DA', align=Align.INLINE)
d.comment(0x904A, 'A=0: command type for net write char', align=Align.INLINE)
d.comment(0x904C, 'Y=&D9: command type offset', align=Align.INLINE)
d.comment(0x904E, 'Store command type at ws+&D9', align=Align.INLINE)
d.comment(0x9050, 'Mark TX control block as active (&80)', align=Align.INLINE)
d.comment(0x9052, 'Y=&0C: TXCB start offset', align=Align.INLINE)
d.comment(0x9054, 'Set TX active flag at ws+&0C', align=Align.INLINE)
d.comment(0x9056, 'Redirect net_tx_ptr low to workspace', align=Align.INLINE)
d.comment(0x9058, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0x905A, 'Complete ptr redirect', align=Align.INLINE)
d.comment(0x905C, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x905F, 'Mark TXCB as deleted (&3F) after transmit', align=Align.INLINE)
d.comment(0x9061, 'Write &3F to TXCB byte 0', align=Align.INLINE)
d.comment(0x9063, 'Return', align=Align.INLINE)
d.comment(0x9064, 'Load original Y (OSBYTE secondary param)', align=Align.INLINE)
d.comment(0x9066, 'OSBYTE &81 (INKEY): always forward to terminal', align=Align.INLINE)
d.comment(0x9068, 'Forward &81 to terminal for keyboard read', align=Align.INLINE)
d.comment(0x906A, 'Y=1: search NCTBPL table (execute on both)', align=Align.INLINE)
d.comment(0x906C, 'X=7: 8-entry NCTBPL table size', align=Align.INLINE)
d.comment(0x906E, 'Search for OSBYTE code in NCTBPL table', align=Align.INLINE)
d.comment(0x9071, 'Match found: dispatch with Y=1 (both)', align=Align.INLINE)
d.comment(0x9073, 'Y=-1: search NCTBMI table (terminal only)', align=Align.INLINE)
d.comment(0x9074, 'Second DEY: Y=&FF (from 1 via 0)', align=Align.INLINE)
d.comment(0x9075, 'X=&0E: 15-entry NCTBMI table size', align=Align.INLINE)
d.comment(0x9077, 'Search for OSBYTE code in NCTBMI table', align=Align.INLINE)
d.comment(0x907A, 'Match found: dispatch with Y=&FF (terminal)', align=Align.INLINE)
d.comment(0x907C, 'Y=0: OSBYTE not recognised, ignore', align=Align.INLINE)

d.label(0x907D, 'dispatch_remote_osbyte')
d.comment(0x907D, 'X=2 bytes to copy (default for RBYTE)', align=Align.INLINE)
d.comment(0x907F, 'A=Y: check table match result', align=Align.INLINE)
d.comment(0x9080, 'Y=0: not recognised, return unhandled', align=Align.INLINE)
d.comment(0x9082, 'Y>0 (NCTBPL): send only, no result expected', align=Align.INLINE)
d.comment(0x9083, 'Y>0 (NCTBPL): no result expected, skip RX', align=Align.INLINE)
d.comment(0x9085, 'Y<0 (NCTBMI): X=3 bytes (result + P flags)', align=Align.INLINE)
d.comment(0x9086, 'Y=&DC: top of 3-byte stack frame region', align=Align.INLINE)
d.comment(0x9088, 'Copy OSBYTE args from stack frame to workspace', align=Align.INLINE)
d.comment(0x908B, 'Store to NFS workspace for transmission', align=Align.INLINE)
d.comment(0x908D, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x908E, 'Copied all 3 bytes? (&DC, &DB, &DA)', align=Align.INLINE)
d.comment(0x9090, 'Loop for remaining bytes', align=Align.INLINE)
d.comment(0x9092, 'A = byte count for setup_tx_and_send', align=Align.INLINE)
d.comment(0x9093, 'Build TXCB and transmit to terminal', align=Align.INLINE)
d.comment(0x9096, 'Restore N flag from table match type', align=Align.INLINE)
d.comment(0x9097, 'Y was positive (NCTBPL): done, no result', align=Align.INLINE)
d.comment(0x9099, 'Set up RX control block to wait for reply', align=Align.INLINE)
d.comment(0x909F, 'Bit7 clear: still waiting, poll again', align=Align.INLINE)
d.comment(0x90A1, 'X = stack pointer for register restoration', align=Align.INLINE)
d.comment(0x90A2, 'Y=&DD: saved P byte offset in workspace', align=Align.INLINE)
d.comment(0x90A4, 'Load remote processor status from reply', align=Align.INLINE)
d.comment(0x90A6, 'Force V=1 (claimed) and I=1 (no IRQ) in saved P', align=Align.INLINE)
d.comment(0x90A8, 'ALWAYS branch (ORA #&44 never zero)', align=Align.INLINE)
d.comment(0x90AA, 'Previous workspace offset', align=Align.INLINE)
d.comment(0x90AB, 'Previous stack register slot', align=Align.INLINE)
d.comment(0x90AC, 'Load next result byte (X, then Y)', align=Align.INLINE)
d.comment(0x90AE, 'Write result bytes to stacked registers', align=Align.INLINE)
d.comment(0x90B1, 'Copied all result bytes? (P at &DA)', align=Align.INLINE)
d.comment(0x90B3, 'Loop for remaining result bytes', align=Align.INLINE)
d.comment(0x90B5, 'Return to OSBYTE dispatcher', align=Align.INLINE)
d.comment(0x90B6, 'Compare OSBYTE code with table entry', align=Align.INLINE)
d.comment(0x90B9, 'Match found: return with Z=1', align=Align.INLINE)
d.comment(0x90BB, 'Next table entry (descending)', align=Align.INLINE)
d.comment(0x90BC, 'Loop for remaining entries', align=Align.INLINE)
d.comment(0x90BE, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)

d.label(0x90BF, 'remote_osbyte_table')
for addr in range(0x90BF, 0x90CE):
    d.byte(addr)
d.comment(0x90BF, 'OSBYTE &04: cursor key status', align=Align.INLINE)
d.comment(0x90C0, 'OSBYTE &09: flash duration (1st colour)', align=Align.INLINE)
d.comment(0x90C1, 'OSBYTE &0A: flash duration (2nd colour)', align=Align.INLINE)
d.comment(0x90C2, 'OSBYTE &14: explode soft character RAM', align=Align.INLINE)
d.comment(0x90C3, 'OSBYTE &9A: video ULA control register', align=Align.INLINE)
d.comment(0x90C4, 'OSBYTE &9B: video ULA palette', align=Align.INLINE)
d.comment(0x90C5, 'OSBYTE &9C: ACIA control register', align=Align.INLINE)
d.comment(0x90C6, 'OSBYTE &E2: function key &D0-&DF', align=Align.INLINE)
d.comment(0x90C7, 'OSBYTE &0B: auto-repeat delay', align=Align.INLINE)
d.comment(0x90C8, 'OSBYTE &0C: auto-repeat rate', align=Align.INLINE)
d.comment(0x90C9, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0x90CA, 'OSBYTE &79: keyboard scan from X', align=Align.INLINE)
d.comment(0x90CB, 'OSBYTE &7A: keyboard scan from &10', align=Align.INLINE)
d.comment(0x90CC, 'OSBYTE &E3: function key &E0-&EF', align=Align.INLINE)
d.comment(0x90CD, 'OSBYTE &E4: function key &F0-&FF', align=Align.INLINE)
d.comment(0x90D2, 'OSWORD 7 (sound): handle via common path', align=Align.INLINE)
d.comment(0x90D4, 'OSWORD 8 = define an envelope', align=Align.INLINE)
d.comment(0x90D6, 'Not OSWORD 7 or 8: ignore (BNE exits)', align=Align.INLINE)

d.label(0x90D8, 'copy_params_rword')
d.comment(0x90D8, 'Point workspace to offset &DB for params', align=Align.INLINE)
d.comment(0x90DA, 'Store workspace ptr offset &DB', align=Align.INLINE)

d.label(0x90DC, 'copy_osword_params')
d.comment(0x90DC, 'Load param byte from OSWORD param block', align=Align.INLINE)
d.comment(0x90DE, 'Write param byte to workspace', align=Align.INLINE)
d.comment(0x90E0, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x90E1, 'Loop for all parameter bytes', align=Align.INLINE)
d.comment(0x90E3, 'Y=0 after loop', align=Align.INLINE)
d.comment(0x90E4, 'Point workspace to offset &DA', align=Align.INLINE)
d.comment(0x90E6, 'Load original OSWORD code', align=Align.INLINE)
d.comment(0x90E8, 'Store OSWORD code at ws+0', align=Align.INLINE)
d.comment(0x90EA, 'Reset workspace ptr to base', align=Align.INLINE)
d.comment(0x90EC, 'Y=&14: command type offset', align=Align.INLINE)
d.comment(0x90EE, 'Tag as RWORD (port &E9)', align=Align.INLINE)
d.comment(0x90F0, 'Store port tag at ws+&14', align=Align.INLINE)
d.comment(0x90F2, 'A=1: single-byte TX', align=Align.INLINE)
d.comment(0x90F7, 'Restore workspace ptr', align=Align.INLINE)
d.comment(0x915A, 'X=&0D: template offset for alt entry', align=Align.INLINE)
d.comment(0x915C, 'Y=&7C: target workspace offset for alt entry', align=Align.INLINE)
d.comment(0x915E, 'BIT test: V flag = bit 6 of &83B3', align=Align.INLINE)
d.comment(0x9161, 'V=1: store to (net_rx_ptr) instead', align=Align.INLINE)
d.comment(0x9163, 'Y=&17: workspace target offset (main entry)', align=Align.INLINE)
d.comment(0x9165, 'X=&1A: template table index (main entry)', align=Align.INLINE)
d.comment(0x9167, 'V=0: target is (nfs_workspace)', align=Align.INLINE)
d.comment(0x916B, '&FE = stop sentinel', align=Align.INLINE)
d.comment(0x916D, 'End of template: jump to exit', align=Align.INLINE)
d.comment(0x916F, '&FD = skip sentinel', align=Align.INLINE)
d.comment(0x9171, "Skip: don't store, just decrement Y", align=Align.INLINE)
d.comment(0x9173, '&FC = page byte sentinel', align=Align.INLINE)
d.comment(0x9175, 'Not sentinel: store template value directly', align=Align.INLINE)
d.comment(0x917D, 'PAGE byte → Y=&02 / Y=&74', align=Align.INLINE)
d.comment(0x917F, '→ Y=&04 / Y=&76', align=Align.INLINE)
d.comment(0x9181, 'PAGE byte → Y=&06 / Y=&78', align=Align.INLINE)
d.comment(0x9183, '→ Y=&08 / Y=&7A', align=Align.INLINE)
d.comment(0x9185, 'Alt-path only → Y=&70', align=Align.INLINE)

d.label(0x9187, 'cb_template_main_start')
d.comment(0x9187, '→ Y=&0C (main only)', align=Align.INLINE)
d.comment(0x9188, '→ Y=&0D (main only)', align=Align.INLINE)

d.label(0x918B, 'cb_template_tail')
d.comment(0x918B, '→ Y=&10 (main only)', align=Align.INLINE)
d.comment(0x918E, '→ Y=&07 / Y=&79', align=Align.INLINE)
d.comment(0x91B8, 'X-1: convert 1-based buffer to 0-based', align=Align.INLINE)
d.comment(0x91B9, 'Is this the network printer buffer?', align=Align.INLINE)
d.comment(0x91BB, 'No: skip printer init', align=Align.INLINE)
d.comment(0x91BD, '&1F = initial buffer pointer offset', align=Align.INLINE)
d.comment(0x91BF, 'Reset printer buffer write position', align=Align.INLINE)
d.comment(0x91C2, '&41 = initial PFLAGS (bit 6 set, bit 0 set)', align=Align.INLINE)
d.comment(0x91C7, 'Return', align=Align.INLINE)
d.comment(0x91C8, 'Only handle buffer 4 (network printer)', align=Align.INLINE)
d.comment(0x91CA, 'Not buffer 4: ignore', align=Align.INLINE)
d.comment(0x91CC, 'A = reason code', align=Align.INLINE)
d.comment(0x91CD, 'Reason 1? (DEX: 1->0)', align=Align.INLINE)
d.comment(0x91CE, 'Not reason 1: handle Ctrl-B/C', align=Align.INLINE)
d.comment(0x91D0, 'Get stack pointer for P register', align=Align.INLINE)
d.comment(0x91D1, 'Force I flag in stacked P to block IRQs', align=Align.INLINE)
d.comment(0x91D4, 'Write back modified P register', align=Align.INLINE)
d.comment(0x91D7, 'OSBYTE &91: extract char from MOS buffer', align=Align.INLINE)
d.comment(0x91D9, 'X=3: printer buffer number', align=Align.INLINE)
d.comment(0x91DE, 'Buffer empty: return', align=Align.INLINE)
d.comment(0x91E0, 'Y = extracted character', align=Align.INLINE)
d.comment(0x91E1, 'Store char in output buffer', align=Align.INLINE)
d.comment(0x91E4, 'Buffer nearly full? (&6E = threshold)', align=Align.INLINE)
d.comment(0x91E6, 'Not full: get next char', align=Align.INLINE)
d.comment(0x91E8, 'Buffer full: flush to network', align=Align.INLINE)
d.comment(0x91F0, 'Store byte at current position', align=Align.INLINE)
d.comment(0x91F2, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x91F5, 'Return; Y = buffer offset', align=Align.INLINE)

d.label(0x91F6, 'toggle_print_flag')
d.comment(0x91F6, 'Save reason code', align=Align.INLINE)
d.comment(0x9217, 'Return', align=Align.INLINE)
d.comment(0x9218, 'Store buffer length at workspace offset &08', align=Align.INLINE)
d.comment(0x921A, 'Current buffer fill position', align=Align.INLINE)
d.comment(0x921D, 'Write to workspace offset &08', align=Align.INLINE)
d.comment(0x921F, 'Store page high byte at offset &09', align=Align.INLINE)
d.comment(0x9221, 'Y=&09', align=Align.INLINE)
d.comment(0x9222, 'Write page high byte at offset &09', align=Align.INLINE)
d.comment(0x9224, 'Also store at offset &05', align=Align.INLINE)
d.comment(0x9226, '(end address high byte)', align=Align.INLINE)
d.comment(0x9228, 'Y=&0B: flag byte offset', align=Align.INLINE)
d.comment(0x922A, 'X=&26: start from template entry &26', align=Align.INLINE)
d.comment(0x922C, 'Reuse ctrl_block_setup with CLV entry', align=Align.INLINE)
d.comment(0x922F, 'Y=&0A: sequence flag byte offset', align=Align.INLINE)
d.comment(0x923B, 'Old sequence bit into bit 0', align=Align.INLINE)
d.comment(0x923C, 'Store sequence flag at offset &0A', align=Align.INLINE)
d.comment(0x923E, 'Y=&1F: buffer start offset', align=Align.INLINE)
d.comment(0x9240, 'Reset printer buffer to start (&1F)', align=Align.INLINE)
d.comment(0x9243, 'A=0: printer output flag', align=Align.INLINE)
d.comment(0x9245, 'X=0: workspace low byte', align=Align.INLINE)
d.comment(0x9246, 'Y = workspace page high byte', align=Align.INLINE)
d.comment(0x9248, 'Enable interrupts before TX', align=Align.INLINE)
d.comment(0x9249, 'Set TX control block ptr low byte', align=Align.INLINE)
d.comment(0x924B, 'Set TX control block ptr high byte', align=Align.INLINE)
d.comment(0x924D, 'Save A (handle bitmask) for later', align=Align.INLINE)
d.comment(0x924E, 'Compute sequence bit from handle', align=Align.INLINE)
d.comment(0x9251, 'Zero: no sequence bit set', align=Align.INLINE)
d.comment(0x9253, 'Non-zero: normalise to bit 0', align=Align.INLINE)
d.comment(0x9255, 'Y=0: flag byte offset in TXCB', align=Align.INLINE)
d.comment(0x9257, 'Merge sequence into existing flag byte', align=Align.INLINE)
d.comment(0x9259, 'Save merged flag byte', align=Align.INLINE)
d.comment(0x925A, 'Write flag+sequence to TXCB byte 0', align=Align.INLINE)
d.comment(0x925C, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x925F, 'End address &FFFF = unlimited data length', align=Align.INLINE)
d.comment(0x9261, 'Y=8: end address low offset in TXCB', align=Align.INLINE)
d.comment(0x9263, 'Store &FF to end addr low', align=Align.INLINE)
d.comment(0x9266, 'Store &FF to end addr high (Y=9)', align=Align.INLINE)
d.comment(0x9268, 'Recover merged flag byte', align=Align.INLINE)
d.comment(0x9269, 'Save in X for sequence compare', align=Align.INLINE)
d.comment(0x926A, 'Y=&D1: printer port number', align=Align.INLINE)
d.comment(0x926C, 'Recover saved handle bitmask', align=Align.INLINE)
d.comment(0x926D, 'Re-save for later consumption', align=Align.INLINE)
d.comment(0x926E, 'A=0: port &D1 (print); A!=0: port &90 (FS)', align=Align.INLINE)
d.comment(0x9270, 'Y=&90: FS data port', align=Align.INLINE)
d.comment(0x9272, 'A = selected port number', align=Align.INLINE)
d.comment(0x9273, 'Y=1: port byte offset in TXCB', align=Align.INLINE)
d.comment(0x9275, 'Write port to TXCB byte 1', align=Align.INLINE)
d.comment(0x9277, 'A = saved flag byte (expected sequence)', align=Align.INLINE)
d.comment(0x9279, 'Push expected sequence for retry loop', align=Align.INLINE)
d.comment(0x927A, 'Flag byte &7F = waiting for reply', align=Align.INLINE)
d.comment(0x927C, 'Write to TXCB flag byte (Y=0)', align=Align.INLINE)
d.comment(0x927E, 'Transmit and wait for reply (BRIANX)', align=Align.INLINE)
d.comment(0x9281, 'Recover expected sequence', align=Align.INLINE)
d.comment(0x9282, 'Keep on stack for next iteration', align=Align.INLINE)
d.comment(0x9283, 'Check if TX result matches expected sequence', align=Align.INLINE)
d.comment(0x9285, 'Bit 0 to carry (sequence mismatch?)', align=Align.INLINE)
d.comment(0x9286, 'C=1: mismatch, retry transmit', align=Align.INLINE)
d.comment(0x9288, 'Clean up: discard expected sequence', align=Align.INLINE)
d.comment(0x9289, 'Discard saved handle bitmask', align=Align.INLINE)
d.comment(0x928E, 'Toggle sequence bit on success', align=Align.INLINE)
d.comment(0x9291, 'Return', align=Align.INLINE)
d.comment(0x9292, 'Save current table index', align=Align.INLINE)
d.comment(0x9294, 'Push for later restore', align=Align.INLINE)
d.comment(0x9295, 'Point workspace to palette save area (&E9)', align=Align.INLINE)
d.comment(0x9297, 'Set workspace low byte', align=Align.INLINE)
d.comment(0x9299, 'Y=0: first palette entry', align=Align.INLINE)
d.comment(0x929B, 'Clear table index counter', align=Align.INLINE)
d.comment(0x929D, 'Save current screen MODE to workspace', align=Align.INLINE)
d.comment(0x92A0, 'Store MODE at workspace[0]', align=Align.INLINE)
d.comment(0x92A2, 'Advance workspace pointer past MODE byte', align=Align.INLINE)
d.comment(0x92A4, 'Read colour count (from &0351)', align=Align.INLINE)
d.comment(0x92A7, 'Push for iteration count tracking', align=Align.INLINE)
d.comment(0x92A8, 'A=0: logical colour number for OSWORD', align=Align.INLINE)

d.label(0x92A9, 'save_palette_entry')
d.comment(0x92A9, 'Store logical colour at workspace[0]', align=Align.INLINE)
d.comment(0x92AB, 'X = workspace ptr low (param block addr)', align=Align.INLINE)
d.comment(0x92AD, 'Y = workspace ptr high', align=Align.INLINE)
d.comment(0x92AF, 'OSWORD &0B: read palette for logical colour', align=Align.INLINE)
d.comment(0x92B4, 'Recover colour count', align=Align.INLINE)
d.comment(0x92B5, 'Y=0: access workspace[0]', align=Align.INLINE)
d.comment(0x92B7, 'Write colour count back to workspace[0]', align=Align.INLINE)
d.comment(0x92B9, 'Y=1: access workspace[1] (palette result)', align=Align.INLINE)
d.comment(0x92BA, 'Read palette value returned by OSWORD', align=Align.INLINE)
d.comment(0x92BC, 'Push palette value for next iteration', align=Align.INLINE)
d.comment(0x92BD, 'X = current workspace ptr low', align=Align.INLINE)
d.comment(0x92BF, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92C1, 'Increment table index', align=Align.INLINE)
d.comment(0x92C3, 'Y=0 for next store', align=Align.INLINE)
d.comment(0x92C4, 'Load table index as logical colour', align=Align.INLINE)
d.comment(0x92C6, 'Loop until workspace wraps past &F9', align=Align.INLINE)
d.comment(0x92C8, 'Continue for all 16 palette entries', align=Align.INLINE)
d.comment(0x92CA, 'Discard last palette value from stack', align=Align.INLINE)
d.comment(0x92CB, 'Reset table index to 0', align=Align.INLINE)
d.comment(0x92CD, 'Advance workspace past palette data', align=Align.INLINE)
d.comment(0x92CF, 'Save cursor pos and OSBYTE state values', align=Align.INLINE)
d.comment(0x92D2, 'Advance workspace past VDU state data', align=Align.INLINE)
d.comment(0x92D4, 'Recover saved table index', align=Align.INLINE)
d.comment(0x92D5, 'Restore table index', align=Align.INLINE)
d.comment(0x92D7, 'Restore LSTAT from saved OLDJSR value', align=Align.INLINE)
d.comment(0x92DA, 'Write to protection status', align=Align.INLINE)
d.comment(0x92DD, 'Return', align=Align.INLINE)
d.comment(0x92DE, 'Read cursor editing state', align=Align.INLINE)
d.comment(0x92E1, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0x92E3, 'Preserve in X for OSBYTE', align=Align.INLINE)
d.comment(0x92E4, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.comment(0x92E7, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92E9, 'Y result from OSBYTE &85', align=Align.INLINE)
d.comment(0x92EA, 'Store Y pos to workspace (X=0)', align=Align.INLINE)
d.comment(0x92EC, 'Self-call trick: executes twice', align=Align.INLINE)
d.comment(0x92EF, 'X=0 for (zp,X) addressing', align=Align.INLINE)
d.comment(0x92F1, 'Index into OSBYTE number table', align=Align.INLINE)
d.comment(0x92F3, 'Next table entry next time', align=Align.INLINE)
d.comment(0x92F5, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92F7, 'Read OSBYTE number from table', align=Align.INLINE)
d.comment(0x92FA, 'Y=&FF: read current value', align=Align.INLINE)
d.comment(0x92FC, 'Call OSBYTE', align=Align.INLINE)
d.comment(0x92FF, 'Result in X to A', align=Align.INLINE)
d.comment(0x9300, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x9302, 'Store result to workspace', align=Align.INLINE)

d.label(0x9308, 'reloc_zp_src')

d.label(0x934D, 'reloc_p4_src')
d.comment(0x966F, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x9672, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x9675, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x9677, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x9679, 'Y=&FF for OSBYTE', align=Align.INLINE)
d.comment(0x968B, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x968E, 'Read station ID (&FE18 = INTOFF side effect)', align=Align.INLINE)
d.comment(0x9691, 'Store our station ID in TX scout', align=Align.INLINE)
d.comment(0x96F5, 'Return', align=Align.INLINE)

d.label(0x970E, 'accept_frame')

d.label(0x972B, 'accept_local_net')

d.label(0x972E, 'accept_scout_net')
d.comment(0x973C, 'Neither set -- clean end, discard via &9744', align=Align.INLINE)
d.comment(0x974C, 'No RDA -- error handler &9737', align=Align.INLINE)
d.comment(0x9773, 'Write CR1', align=Align.INLINE)
d.comment(0x9778, 'Write CR2', align=Align.INLINE)
d.comment(0x978C, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x9797, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x979A, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x979D, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x979F, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x97A1, 'Write CR2: broadcast frame prep', align=Align.INLINE)

d.label(0x97A4, 'scan_port_list')
d.comment(0x97A4, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x97A7, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x97A9, 'Start scanning port list at page &C0', align=Align.INLINE)

d.label(0x97B1, 'check_port_slot')
d.comment(0x97B1, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x97B3, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x97B5, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x97B7, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x97B9, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x97BC, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x97BE, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x97C0, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x97C3, 'Port mismatch -- try next slot', align=Align.INLINE)

d.label(0x97C5, 'check_station_filter')
d.comment(0x97C5, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x97C6, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x97C8, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x97CA, 'Check if source station matches', align=Align.INLINE)
d.comment(0x97CD, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x97CF, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x97D0, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x97D2, 'Check if source network matches', align=Align.INLINE)
d.comment(0x97D5, 'Network matches or zero = accept', align=Align.INLINE)

d.label(0x97D7, 'next_port_slot')
d.comment(0x97D7, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x9819, 'Broadcast: different completion path', align=Align.INLINE)

d.label(0x981C, 'send_data_rx_ack')
d.comment(0x981C, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x981E, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x9821, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x9823, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x9826, 'Install data_rx_setup at &982D', align=Align.INLINE)
d.comment(0x9828, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x982A, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x982F, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x9832, 'Install nmi_data_rx at &9839', align=Align.INLINE)
d.comment(0x9836, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)
d.comment(0x9839, 'A=&01: mask for AP (Address Present)', align=Align.INLINE)
d.comment(0x983B, 'BIT SR2: test AP bit', align=Align.INLINE)
d.comment(0x983E, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x9840, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x9843, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x9846, 'Not for us: error path', align=Align.INLINE)
d.comment(0x9848, 'Install net check handler at &984F', align=Align.INLINE)
d.comment(0x984C, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x9852, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x9854, 'Read dest network byte', align=Align.INLINE)
d.comment(0x9857, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x9859, 'Install skip handler at &9865', align=Align.INLINE)
d.comment(0x985B, 'High byte of &9865 handler', align=Align.INLINE)
d.comment(0x985D, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x9860, 'Data ready: skip directly, no RTI', align=Align.INLINE)
d.comment(0x9862, 'Install handler and return via RTI', align=Align.INLINE)
d.comment(0x9868, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x9870, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x9872, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x9875, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x9877, 'Install bulk read at &989A', align=Align.INLINE)
d.comment(0x9879, 'High byte of &989A handler', align=Align.INLINE)
d.comment(0x987B, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x987E, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x9880, 'No: install handler and RTI', align=Align.INLINE)

d.label(0x9883, 'install_tube_rx')
d.comment(0x9883, 'Tube: install Tube RX at &98F7', align=Align.INLINE)
d.comment(0x9885, 'High byte of &98F7 handler', align=Align.INLINE)
d.comment(0x9887, 'Install Tube handler and RTI', align=Align.INLINE)


d.subroutine(0x988A, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")
d.comment(0x988A, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x988D, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x9891, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x9894, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x9897, 'Discard and return to idle listen', align=Align.INLINE)

d.label(0x989F, 'data_rx_loop')
d.comment(0x989F, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x98A1, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x98A4, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x98A6, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x98A7, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x98A9, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x98AB, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x98AD, 'No pages left: handle as complete', align=Align.INLINE)

d.label(0x98AF, 'read_sr2_between_pairs')
d.comment(0x98AF, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x98B2, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x98B4, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)

d.label(0x98B6, 'read_second_rx_byte')
d.comment(0x98B6, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x98B9, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x98BB, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x98BC, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x98BE, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x98C0, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x98C2, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x98C4, 'No pages left: frame complete', align=Align.INLINE)

d.label(0x98C6, 'check_sr2_loop_again')
d.comment(0x98C6, 'Read SR2 for next iteration', align=Align.INLINE)
d.comment(0x98C9, 'SR2 non-zero: more data, loop back', align=Align.INLINE)
d.comment(0x98CB, 'SR2=0: no more data yet, wait for NMI', align=Align.INLINE)
d.comment(0x98D0, 'Write CR1', align=Align.INLINE)
d.comment(0x98D5, 'Write CR2', align=Align.INLINE)
d.comment(0x98D8, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x98E3, 'Check if buffer space remains', align=Align.INLINE)

d.label(0x98E5, 'read_last_rx_byte')
d.comment(0x98E5, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x98EA, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x98EC, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x98EE, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x98F0, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x98F2, 'Page boundary: advance buffer page', align=Align.INLINE)

d.label(0x98F4, 'send_ack')
d.comment(0x98F4, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x98F7, 'Read SR2 for Tube data receive path', align=Align.INLINE)

d.label(0x98FA, 'rx_tube_data')
d.comment(0x98FA, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x98FC, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x9930, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x9933, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x9935, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x9938, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x993A, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x993D, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x993F, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x9942, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x9944, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x9946, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x9948, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x994A, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x994C, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x994E, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x9950, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x9953, 'Save extra byte at &0D5D for later use', align=Align.INLINE)
d.comment(0x9956, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x9958, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x995B, 'Store updated flags', align=Align.INLINE)
d.comment(0x995E, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x9961, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x9963, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x9968, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x996D, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x9972, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x9974, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x9977, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x9988, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x998D, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x998F, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)
d.comment(0x99A9, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x99AF, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x99B2, 'Install next NMI handler', align=Align.INLINE)

d.label(0x99B5, 'start_data_tx')
d.comment(0x99B5, 'Jump to start data TX phase', align=Align.INLINE)

d.label(0x99C0, 'dispatch_nmi_error')
d.comment(0x99C0, 'Jump to error handler', align=Align.INLINE)
d.comment(0x99C3, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x99C5, 'BIT tx_flags: check data transfer bit', align=Align.INLINE)
d.comment(0x99C8, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x99CA, 'CLC: init carry for 4-byte add', align=Align.INLINE)
d.comment(0x99CB, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x99CC, 'Y=8: RXCB high pointer offset', align=Align.INLINE)

d.label(0x99CE, 'add_rxcb_ptr')
d.comment(0x99CE, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x99D0, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x99D1, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x99D4, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x99D6, 'Next byte', align=Align.INLINE)
d.comment(0x99D7, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x99D8, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x99DA, 'No: continue adding', align=Align.INLINE)
d.comment(0x99DC, 'Discard final carry', align=Align.INLINE)
d.comment(0x99DD, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x99DF, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x99E2, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x99E4, 'Save X on stack', align=Align.INLINE)
d.comment(0x99E5, 'Push X', align=Align.INLINE)
d.comment(0x99E6, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x99E8, 'CLC for address calculation', align=Align.INLINE)
d.comment(0x99E9, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x99EB, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x99EC, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x99EE, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x99F0, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x99F3, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x99F6, 'Send to Tube via R3', align=Align.INLINE)
d.comment(0x9A07, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x9A09, 'CLC for address add', align=Align.INLINE)
d.comment(0x9A0A, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x9A0C, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x9A0E, 'Carry: increment buffer high byte', align=Align.INLINE)

d.label(0x9A10, 'store_buf_ptr_lo')
d.comment(0x9A10, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x9A12, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x9A14, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x9A15, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x9A17, 'Store high byte to RXCB', align=Align.INLINE)
d.comment(0x9A19, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x9A1C, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x9A1E, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x9A20, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x9A21, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x9A24, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x9A26, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x9A27, 'Load port byte', align=Align.INLINE)
d.comment(0x9A2A, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x9A2C, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x9A2D, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x9A30, 'Set bit7 = reception complete flag', align=Align.INLINE)
d.comment(0x9A32, 'Store to RXCB (marks CB as complete)', align=Align.INLINE)
d.comment(0x9A34, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x9A39, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x9A3D, 'Release Tube claim before discarding', align=Align.INLINE)
d.comment(0x9A40, 'Re-enter idle RX listen mode', align=Align.INLINE)

d.label(0x9A43, 'install_rx_scout_handler')
d.comment(0x9A43, 'Install nmi_rx_scout (&96F6) as NMI handler', align=Align.INLINE)
d.comment(0x9A45, 'High byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x9A47, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9A59, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x9A5C, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x9A5E, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x9A60, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x9A62, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x9A64, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x9A66, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x9A6F, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x9A70, 'SEC for subtract', align=Align.INLINE)
d.comment(0x9A71, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x9A73, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x9A74, 'Load protection mask from LSTAT', align=Align.INLINE)

d.label(0x9A77, 'rotate_prot_mask')
d.comment(0x9A77, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x9A78, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x9A79, 'Loop until bit aligned', align=Align.INLINE)


d.subroutine(0x9AE1, 'rx_imm_peek_setup', title='RX immediate: PEEK setup', description="""Writes &0D3D to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send the
PEEK response data back to the requesting station.
Uses workspace offsets (&A6/&A7) for nmi_tx_block.""")
d.comment(0x9B19, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x9B1B, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x9B1C, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x9B1E, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x9B20, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x9B22, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x9B24, 'Load requesting station number', align=Align.INLINE)
d.comment(0x9B27, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x9B2A, 'Load requesting network number', align=Align.INLINE)
d.comment(0x9B2D, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x9B2F, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x9B32, 'Save ctrl byte for TX response', align=Align.INLINE)
d.comment(0x9B35, 'IER bit 2: disable SR interrupt', align=Align.INLINE)
d.comment(0x9B37, 'Write IER to disable SR', align=Align.INLINE)
d.comment(0x9B3A, 'Read ACR for shift register config', align=Align.INLINE)
d.comment(0x9B3D, 'Isolate shift register mode bits (2-4)', align=Align.INLINE)
d.comment(0x9B3F, 'Save original SR mode for later restore', align=Align.INLINE)
d.comment(0x9B42, 'Reload ACR for modification', align=Align.INLINE)
d.comment(0x9B45, 'Clear SR mode bits (keep other bits)', align=Align.INLINE)
d.comment(0x9B47, 'SR mode 2: shift in under φ2', align=Align.INLINE)
d.comment(0x9B49, 'Apply new shift register mode', align=Align.INLINE)
d.comment(0x9B4C, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x9B4F, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x9BE4, 'Save X on stack', align=Align.INLINE)
d.comment(0x9BE5, 'Push X', align=Align.INLINE)
d.comment(0x9BE6, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x9BE8, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x9BEA, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9BEE, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x9BF0, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9BF3, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x9BF5, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x9BF7, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x9BF9, 'Bit7 clear: normal data transfer', align=Align.INLINE)

d.label(0x9BFC, 'tx_imm_op_setup')
d.comment(0x9BFC, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9BFF, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x9C00, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x9C01, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x9C03, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9C06, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x9C08, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x9C0A, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x9C0C, 'SEC: init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9C0D, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x9C0E, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)

d.label(0x9C10, 'calc_peek_poke_size')
d.comment(0x9C10, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x9C12, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x9C16, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x9C17, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x9C19, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x9C21, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9C22, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9C24, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9C26, 'Discard final borrow', align=Align.INLINE)
d.comment(0x9C27, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x9C29, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x9C2B, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)

d.label(0x9C2D, 'copy_imm_params')
d.comment(0x9C2D, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x9C2F, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x9C32, 'Next byte', align=Align.INLINE)
d.comment(0x9C33, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x9C35, 'No: continue copying', align=Align.INLINE)

d.label(0x9C37, 'tx_line_idle_check')
d.comment(0x9C37, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x9C39, 'BIT SR2: test if line is idle', align=Align.INLINE)
d.comment(0x9C3C, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x9C3E, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x9C40, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x9C41, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x9C43, 'Store scout frame length', align=Align.INLINE)
d.comment(0x9C46, 'A=0: init low byte of timeout counter', align=Align.INLINE)

d.label(0x9C4F, 'test_inactive_retry')

d.label(0x9C6D, 'inactive_retry')
d.comment(0x9C8A, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x9C8D, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x9C92, 'ALWAYS branch to shared error handler', align=Align.INLINE)

d.label(0x9C94, 'tx_no_clock_error')
d.comment(0x9C94, "Error &43 = 'No Clock'", align=Align.INLINE)

d.label(0x9C96, 'store_tx_error')
d.comment(0x9C96, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x9C98, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x9C9A, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x9C9C, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x9C9F, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x9CA0, 'Move to X register', align=Align.INLINE)
d.comment(0x9CA1, 'Return to TX caller', align=Align.INLINE)
d.comment(0x9CA7, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9CAC, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x9CAE, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x9CB1, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x9CB7, 'Load destination port number', align=Align.INLINE)
d.comment(0x9CBA, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x9CBC, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x9CBF, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x9CC2, 'Store operation flags', align=Align.INLINE)
d.comment(0x9CC5, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x9CC8, 'Store expected transfer length', align=Align.INLINE)


d.subroutine(0x9D00, 'tx_ctrl_add_done', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

d.label(0x9D16, 'setup_data_xfer')
d.comment(0x9D16, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x9D19, 'AND with dest network', align=Align.INLINE)
d.comment(0x9D1C, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x9D1E, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x9D20, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x9D22, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x9D25, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x9D27, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x9D2A, 'Y=4: start of address data in TXCB', align=Align.INLINE)

d.label(0x9D2C, 'copy_bcast_addr')
d.comment(0x9D2C, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x9D2E, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x9D31, 'Next byte', align=Align.INLINE)
d.comment(0x9D32, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9D34, 'No: continue copying', align=Align.INLINE)

d.label(0x9D38, 'setup_unicast_xfer')
d.comment(0x9D38, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x9D3A, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x9D3D, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x9D3F, 'Store scout status', align=Align.INLINE)
d.comment(0x9D42, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x9D45, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x9D46, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x9D47, 'Second PLA', align=Align.INLINE)
d.comment(0x9D48, 'Third PLA', align=Align.INLINE)
d.comment(0x9D49, 'Fourth PLA', align=Align.INLINE)
d.comment(0x9D4A, 'Restore X from A', align=Align.INLINE)
d.comment(0x9D4B, 'Return to caller', align=Align.INLINE)

d.label(0x9D52, 'tx_fifo_write')

d.label(0x9D76, 'tx_fifo_not_ready')

d.label(0x9D7D, 'tx_store_error')

d.label(0x9D80, 'delay_nmi_disable')
d.comment(0x9D8A, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x9D8F, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9D91, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9DA1, 'check_handshake_bit')

d.label(0x9DAB, 'install_reply_scout')
d.comment(0x9DB9, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x9DD9, 'IRQ set -- fall through to &9D5B without RTI', align=Align.INLINE)

d.label(0x9DE0, 'reject_reply')
d.comment(0x9E01, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x9E06, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x9E0B, 'High byte &9E of next handler address', align=Align.INLINE)
d.comment(0x9E0D, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x9E10, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x9E1E, 'Load dest network for scout ACK TX', align=Align.INLINE)
d.comment(0x9E21, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x9E26, 'High byte &9D of handler address', align=Align.INLINE)
d.comment(0x9E28, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9E2B, 'Read our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x9E2E, 'BIT SR1: check TDRA before writing', align=Align.INLINE)
d.comment(0x9E31, 'TDRA not ready: TX error', align=Align.INLINE)
d.comment(0x9E36, 'Network = 0 (local network)', align=Align.INLINE)
d.comment(0x9E38, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E3B, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x9E3D, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x9E40, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x9E42, 'Install nmi_data_tx at &9E50', align=Align.INLINE)
d.comment(0x9E44, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9E46, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9E49, 'install_imm_data_nmi')
d.comment(0x9E49, 'Install nmi_data_tx_tube at &9EA4', align=Align.INLINE)
d.comment(0x9E4B, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9E4D, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9E55, 'data_tx_check_fifo')
d.comment(0x9E59, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x9E5C, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E5D, 'No page crossing', align=Align.INLINE)
d.comment(0x9E5F, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E61, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E63, 'Increment buffer high byte', align=Align.INLINE)

d.label(0x9E65, 'write_second_tx_byte')
d.comment(0x9E65, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x9E67, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x9E6A, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E6B, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x9E6D, 'No page crossing', align=Align.INLINE)
d.comment(0x9E6F, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E71, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E73, 'Increment buffer high byte', align=Align.INLINE)

d.label(0x9E75, 'check_irq_loop')
d.comment(0x9E75, 'BIT SR1: test IRQ (N=bit7) for tight loop', align=Align.INLINE)
d.comment(0x9E78, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9E7A, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9E7F, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x9E82, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x9E85, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x9E87, 'Install discard_reset_listen at &9A34', align=Align.INLINE)
d.comment(0x9E89, 'High byte of &9A34 handler', align=Align.INLINE)
d.comment(0x9E8B, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9E8E, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x9E9E, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x9EA1, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x9EA4, 'Tube TX: BIT SR1 test TDRA', align=Align.INLINE)

d.label(0x9EA7, 'tube_tx_fifo_write')
d.comment(0x9EA7, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9EA9, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x9EAC, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x9EAF, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x9EB1, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9EB3, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9EB5, 'No further carry', align=Align.INLINE)
d.comment(0x9EB7, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9EB9, 'No further carry', align=Align.INLINE)
d.comment(0x9EBB, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9EBD, 'Counter wrapped to zero: last data', align=Align.INLINE)

d.label(0x9EBF, 'write_second_tube_byte')
d.comment(0x9EBF, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x9EC2, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x9EC5, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x9EC7, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9EC9, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9ECB, 'No further carry', align=Align.INLINE)

d.label(0x9ECD, 'tube_tx_inc_byte3')
d.comment(0x9ECD, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9ECF, 'No further carry', align=Align.INLINE)
d.comment(0x9ED1, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9ED3, 'Counter wrapped to zero: last data', align=Align.INLINE)

d.label(0x9ED5, 'check_tube_irq_loop')
d.comment(0x9ED5, 'BIT SR1: test IRQ for tight loop', align=Align.INLINE)
d.comment(0x9ED8, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9EDA, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9EDF, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9EE4, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9EE6, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x9F10, 'IRQ set -- fall through to &9F15 without RTI', align=Align.INLINE)

d.label(0x9F32, 'check_fv_final_ack')


d.subroutine(0x9F3D, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")
d.comment(0x9F3D, 'A=&41: not listening error code', align=Align.INLINE)
d.comment(0x9F66, 'Tube transfer in progress?', align=Align.INLINE)

d.label(0x9F77, 'calc_transfer_size')
d.comment(0x9F8C, 'A = saved X', align=Align.INLINE)
d.comment(0x9F8D, 'Save X', align=Align.INLINE)

d.label(0x9FA4, 'restore_x_and_return')

d.label(0x9FA7, 'fallback_calc_transfer')
d.comment(0x9FA7, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x9FAB, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x9FAD, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9FB2, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x9FB6, 'Propagate borrow from lo subtraction', align=Align.INLINE)
d.comment(0x9FB8, 'Temp store adjusted current ptr hi', align=Align.INLINE)
d.comment(0x9FBA, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x9FBE, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x9FC0, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x9FC2, 'Load RXCB[9] (start ptr hi)', align=Align.INLINE)
d.comment(0x9FC4, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9FC5, 'start_hi - adjusted current_hi', align=Align.INLINE)
d.comment(0x9FCB, 'INTOFF: disable NMIs while switching ROM', align=Align.INLINE)
d.comment(0x9FCE, 'Save A', align=Align.INLINE)
d.comment(0x9FCF, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9FD0, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x9FD1, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x9FD3, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x9FD6, 'Jump to scout handler in ROM', align=Align.INLINE)
d.comment(0x9FD9, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x9FDC, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x9FDF, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x9FE1, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x9FE4, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9FE6, 'Restore A from stack', align=Align.INLINE)
d.comment(0x9FE7, 'INTON: re-enable NMIs', align=Align.INLINE)
d.comment(0x9FEA, 'Return from interrupt', align=Align.INLINE)

d.label(0x0020, 'tube_send_zero_r2')


d.label(0x0036, 'tube_enter_main_loop')
d.subroutine(0x0036, 'tube_enter_main_loop', title='Save registers and enter Tube polling loop', description="""Saves X and Y to zp_temp_11/zp_temp_10, then falls through
to tube_main_loop which polls Tube R1 (WRCH) and R2 (command)
registers in an infinite loop. Called from tube_init_reloc
after ROM relocation and from tube_dispatch_table handlers
that need to restart the main loop.""")
d.comment(0x0036, 'Save X to temporary', align=Align.INLINE)
d.comment(0x0038, 'Save Y to temporary', align=Align.INLINE)
d.comment(0x0414, '&80 sentinel: clear address claim', align=Align.INLINE)

d.label(0x0426, 'setup_data_transfer')
d.comment(0x045B, 'Discard return address (low byte)', align=Align.INLINE)
d.comment(0x045C, 'Discard return address (high byte)', align=Align.INLINE)

d.label(0x045D, 'release_claim_restart')
d.comment(0x045D, 'A=&80: reset claim flag sentinel', align=Align.INLINE)
d.comment(0x045F, 'Clear claim-in-progress flag', align=Align.INLINE)

d.label(0x0464, 'flush_r3_nmi_check')
d.comment(0x0464, 'Poll R4 status: wait for transfer ready', align=Align.INLINE)

d.label(0x0473, 'tube_begin')
d.comment(0x0473, 'BEGIN: enable interrupts for Tube host code', align=Align.INLINE)
d.comment(0x0474, 'Save processor status', align=Align.INLINE)
d.comment(0x0475, 'Save A on stack', align=Align.INLINE)
d.comment(0x0476, 'Y=0: start at beginning of page', align=Align.INLINE)
d.comment(0x0478, 'Store to zero page pointer low byte', align=Align.INLINE)


d.subroutine(0x047A, 'tube_init_reloc', title='Initialise relocation address for ROM transfer', description="""Sets source page to &8000 and page counter to &80. Checks
ROM type bit 5 for a relocation address in the ROM header;
if present, extracts the 4-byte address from after the
copyright string. Otherwise uses default &8000 start.""")
d.comment(0x04A4, 'Restore A from stack', align=Align.INLINE)
d.comment(0x04A5, 'Restore processor status', align=Align.INLINE)
d.comment(0x04A6, 'Carry set: language entry (claim Tube)', align=Align.INLINE)
d.comment(0x04A8, 'X = A (preserved from entry)', align=Align.INLINE)
d.comment(0x04A9, 'Non-zero: check break type', align=Align.INLINE)
d.comment(0x04AB, 'A=0: acknowledge and return', align=Align.INLINE)
d.comment(0x04AE, 'X=0 for OSBYTE read', align=Align.INLINE)
d.comment(0x04B0, 'Y=&FF for OSBYTE read', align=Align.INLINE)
d.comment(0x04B2, 'OSBYTE &FD: read last break type', align=Align.INLINE)
d.comment(0x04B8, 'Soft break (0): skip ROM transfer', align=Align.INLINE)
d.comment(0x04BA, 'A=&FF: claim Tube for all operations', align=Align.INLINE)
d.comment(0x04BC, 'Claim Tube address via R4', align=Align.INLINE)
d.comment(0x04BF, 'Not claimed: retry until claimed', align=Align.INLINE)
d.comment(0x04C1, 'Transfer type 1 (parasite to host)', align=Align.INLINE)
d.comment(0x04C3, 'Set up Tube transfer parameters', align=Align.INLINE)
d.comment(0x04C6, 'Y=0: start at page boundary', align=Align.INLINE)
d.comment(0x04C8, 'Source ptr low = 0', align=Align.INLINE)
d.comment(0x04CA, 'X=&40: 64 pages (16KB) to transfer', align=Align.INLINE)

d.label(0x04CC, 'send_rom_byte')
d.comment(0x04CC, 'Read byte from source address', align=Align.INLINE)
d.comment(0x04CE, 'Send byte to Tube via R3', align=Align.INLINE)

d.label(0x04D1, 'poll_r3_ready')
d.comment(0x04D1, 'Check R3 status', align=Align.INLINE)
d.comment(0x04D4, 'Not ready: wait for Tube', align=Align.INLINE)
d.comment(0x04D6, 'Next byte in page', align=Align.INLINE)
d.comment(0x04D7, 'More bytes in page: continue', align=Align.INLINE)
d.comment(0x04D9, 'Next source page', align=Align.INLINE)
d.comment(0x04DB, 'Decrement page counter', align=Align.INLINE)
d.comment(0x04DC, 'More pages: continue transfer', align=Align.INLINE)
d.comment(0x04DE, 'Transfer type 4 (host to parasite burst)', align=Align.INLINE)
d.comment(0x04E0, 'Y=0: low byte of param block ptr', align=Align.INLINE)
d.comment(0x04E2, 'X=&57: param block at &0057', align=Align.INLINE)
d.comment(0x04E4, 'Claim Tube and start transfer', align=Align.INLINE)
d.comment(0x04E7, 'R2 command: OSRDCH request', align=Align.INLINE)
d.comment(0x04E9, 'Send OSRDCH request to host', align=Align.INLINE)
d.comment(0x04EC, 'Jump to RDCH completion handler', align=Align.INLINE)
d.comment(0x04F1, 'Restore X from saved value', align=Align.INLINE)
d.comment(0x04F3, 'Read result byte from R2', align=Align.INLINE)
d.comment(0x04F6, 'Shift carry into C flag', align=Align.INLINE)
d.comment(0x04F7, 'Poll R2 status register', align=Align.INLINE)
d.comment(0x04FA, 'Bit 7 clear: R2 not ready, wait', align=Align.INLINE)
d.comment(0x04FC, 'Read byte from R2 data register', align=Align.INLINE)
d.comment(0x04FF, 'Return with pointers initialised', align=Align.INLINE)
d.comment(0x051D, 'A=0: send null prefix via R2', align=Align.INLINE)
d.comment(0x051F, 'Send prefix byte to co-processor', align=Align.INLINE)

d.label(0x0522, 'poll_r2_reply')
d.comment(0x0522, 'Poll R2 for co-processor reply', align=Align.INLINE)
d.comment(0x0525, 'R2 ready: go process reply', align=Align.INLINE)
d.comment(0x0527, 'Check R4 for pending WRCH request', align=Align.INLINE)
d.comment(0x052A, 'No R4 data: back to polling R2', align=Align.INLINE)
d.comment(0x052C, 'Read WRCH character from R4', align=Align.INLINE)
d.comment(0x0532, 'Resume R2 polling after servicing', align=Align.INLINE)

d.label(0x0535, 'wrch_echo_reply')
d.comment(0x0535, 'Recover original character', align=Align.INLINE)
d.comment(0x0536, 'Echo character back via R2', align=Align.INLINE)
d.comment(0x0539, 'Push for dispatch loop re-entry', align=Align.INLINE)
d.comment(0x053A, 'Enter main dispatch loop', align=Align.INLINE)
d.comment(0x0541, 'Restore saved A', align=Align.INLINE)
d.comment(0x0542, 'Return to caller', align=Align.INLINE)
d.comment(0x0557, 'Save byte read from file', align=Align.INLINE)
d.comment(0x0558, 'Send carry+byte reply (BGET result)', align=Align.INLINE)

d.label(0x055F, 'send_reply_ok')
d.comment(0x055F, 'Set bit 7 (no-error flag)', align=Align.INLINE)
d.comment(0x0561, 'ROR A: encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x0562, '= JSR tube_send_r2 (overlaps &053D entry)', align=Align.INLINE)
d.comment(0x0565, 'Restore read character/byte', align=Align.INLINE)
d.comment(0x0576, 'Save file handle result', align=Align.INLINE)
d.comment(0x0577, 'A=&FF: success marker', align=Align.INLINE)
d.comment(0x0579, 'Send success marker via R2', align=Align.INLINE)
d.comment(0x057C, 'Restore file handle', align=Align.INLINE)
d.comment(0x0598, 'Loop until all 4 bytes read', align=Align.INLINE)
d.comment(0x059A, 'X=0: reset index after loop', align=Align.INLINE)
d.comment(0x05F1, 'Set bit 7: mark result as present', align=Align.INLINE)
d.comment(0x0600, 'OSGBPB done: return to main loop', align=Align.INLINE)

d.label(0x0604, 'read_gbpb_params')
d.comment(0x0604, 'Read param byte from Tube R2', align=Align.INLINE)
d.comment(0x0607, 'Store in zero page param block', align=Align.INLINE)
d.comment(0x0609, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x060A, 'Loop until all 13 bytes read', align=Align.INLINE)
d.comment(0x060C, 'Read A (OSGBPB function code)', align=Align.INLINE)
d.comment(0x060F, 'X=0 after loop', align=Align.INLINE)
d.comment(0x0610, 'Y=0 for OSGBPB call', align=Align.INLINE)
d.comment(0x0619, 'X=12: send 13 updated param bytes', align=Align.INLINE)

d.label(0x061B, 'send_gbpb_params')
d.comment(0x061B, 'Load updated param byte', align=Align.INLINE)
d.comment(0x061D, 'Send param byte via R2', align=Align.INLINE)
d.comment(0x0620, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x0621, 'Loop until all 13 bytes sent', align=Align.INLINE)
d.comment(0x0623, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0629, 'Save in X', align=Align.INLINE)
d.comment(0x062A, 'Read A (OSBYTE function code)', align=Align.INLINE)
d.comment(0x062D, 'Execute OSBYTE A,X', align=Align.INLINE)
d.comment(0x0630, 'Poll R2 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x0633, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0638, 'Return to main event loop', align=Align.INLINE)
d.comment(0x063E, 'Save in X', align=Align.INLINE)
d.comment(0x063F, 'Read Y parameter from co-processor', align=Align.INLINE)
d.comment(0x0642, 'Save in Y', align=Align.INLINE)
d.comment(0x0643, 'Read A (OSBYTE function code)', align=Align.INLINE)
d.comment(0x0646, 'Execute OSBYTE A,X,Y', align=Align.INLINE)
d.comment(0x064D, 'A=&40: high bit will hold carry', align=Align.INLINE)
d.comment(0x0650, 'Send carry+status byte via R2', align=Align.INLINE)
d.comment(0x0653, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x0656, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0660, 'Save OSWORD number in Y', align=Align.INLINE)
d.comment(0x0661, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x0664, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x066A, 'No params (length=0): skip read loop', align=Align.INLINE)
d.comment(0x066C, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x066F, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0671, 'Read param byte from R2', align=Align.INLINE)
d.comment(0x0677, 'Next param byte (descending)', align=Align.INLINE)
d.comment(0x0678, 'Loop until all params read', align=Align.INLINE)
d.comment(0x067D, 'Y=&01: param block at &0130', align=Align.INLINE)
d.comment(0x067F, 'Execute OSWORD with XY=&0130', align=Align.INLINE)
d.comment(0x0682, 'A=&FF: result marker for co-processor', align=Align.INLINE)
d.comment(0x0684, 'Send result marker via R2', align=Align.INLINE)
d.comment(0x0687, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x068A, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x068F, 'Decrement result byte counter', align=Align.INLINE)
d.comment(0x0695, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x0698, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x069A, 'Send result byte via R2', align=Align.INLINE)
d.comment(0x069D, 'Next result byte (descending)', align=Align.INLINE)
d.comment(0x069E, 'Loop until all results sent', align=Align.INLINE)
d.comment(0x06A0, 'Return to main event loop', align=Align.INLINE)
d.comment(0x06A5, 'Read control block byte from R2', align=Align.INLINE)
d.comment(0x06A8, 'Store in zero page params', align=Align.INLINE)
d.comment(0x06AA, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x06AB, 'Loop until all 5 bytes read', align=Align.INLINE)
d.comment(0x06AE, 'Y=0 for OSWORD 0', align=Align.INLINE)
d.comment(0x06B0, 'A=0: OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x06B1, 'Read input line from keyboard', align=Align.INLINE)
d.comment(0x06B8, 'Escape: send &FF error to co-processor', align=Align.INLINE)
d.comment(0x06BB, 'X=0: start of input buffer at &0700', align=Align.INLINE)
d.comment(0x06BF, 'Send &7F (success) to co-processor', align=Align.INLINE)
d.comment(0x06C2, 'Load char from input buffer', align=Align.INLINE)
d.comment(0x06C5, 'Send char to co-processor', align=Align.INLINE)
d.comment(0x06C8, 'Next character', align=Align.INLINE)
d.comment(0x06CB, 'Loop until CR terminator sent', align=Align.INLINE)
d.comment(0x06CD, 'Return to main event loop', align=Align.INLINE)
d.comment(0x06D0, 'Poll R2 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06D3, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06D5, 'Write A to Tube R2 data register', align=Align.INLINE)
d.comment(0x06D8, 'Return to caller', align=Align.INLINE)
d.comment(0x06D9, 'Poll R4 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06DC, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06DE, 'Write A to Tube R4 data register', align=Align.INLINE)
d.comment(0x06E1, 'Return to caller', align=Align.INLINE)
d.comment(0x06E5, 'ROR: shift escape bit 7 to carry', align=Align.INLINE)
d.comment(0x06EB, 'Send zero prefix via R1', align=Align.INLINE)
d.comment(0x06EE, 'Y value for event', align=Align.INLINE)
d.comment(0x06EF, 'Send Y via R1', align=Align.INLINE)
d.comment(0x06F2, 'X value for event', align=Align.INLINE)
d.comment(0x06F3, 'Send X via R1', align=Align.INLINE)
d.comment(0x06F6, 'Restore A (event type)', align=Align.INLINE)
d.comment(0x06F7, 'Poll R1 status (bit 6 = ready)', align=Align.INLINE)
d.comment(0x06FA, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06FC, 'Write A to Tube R1 data register', align=Align.INLINE)
d.comment(0x06FF, 'Return to caller', align=Align.INLINE)
d.comment(0x806D, 'Negative: not a net command, exit', align=Align.INLINE)
d.comment(0x8079, 'Copy command text to FS buffer', align=Align.INLINE)
d.comment(0x8083, 'CSD handle zero: not logged in', align=Align.INLINE)
d.comment(0x8093, 'X = function code for dispatch', align=Align.INLINE)
d.comment(0x8094, 'Save Y (command text ptr hi)', align=Align.INLINE)
d.comment(0x80B9, 'Save ROM number across OSBYTE', align=Align.INLINE)
d.comment(0x80BB, 'Save Tube address across OSBYTE', align=Align.INLINE)
d.comment(0x80BD, 'X=6 extra pages for char definitions', align=Align.INLINE)
d.comment(0x80BF, 'OSBYTE &14: explode character RAM', align=Align.INLINE)
d.comment(0x80C4, 'Restore ROM number', align=Align.INLINE)
d.comment(0x80C6, 'Continue to vector setup', align=Align.INLINE)

d.label(0x811B, 'restore_y_check_svc')
d.comment(0x811B, 'Restore Y (ROM number)', align=Align.INLINE)

d.label(0x811D, 'tube_chars_done')
d.comment(0x811D, 'A=0: fall through to service &12 check', align=Align.INLINE)

d.label(0x811F, 'check_svc_12')
d.comment(0x811F, 'Is this service &12 (select FS)?', align=Align.INLINE)
d.comment(0x8121, 'No: check if service < &0D', align=Align.INLINE)
d.comment(0x8123, 'Service &12: Y=5 (NFS)?', align=Align.INLINE)
d.comment(0x8125, 'Y=5: select NFS', align=Align.INLINE)
d.comment(0x8145, 'Return (not our command)', align=Align.INLINE)

d.label(0x819D, 'match_next_char')
d.comment(0x81BB, 'Return (not our service call)', align=Align.INLINE)
d.comment(0x81BC, 'Print inline ROM identification string', align=Align.INLINE)
d.comment(0x822F, 'A=&8F: issue service request', align=Align.INLINE)
d.comment(0x8231, "X=&0F: 'vectors claimed' service", align=Align.INLINE)
d.comment(0x8236, 'X=&0A: service &0A', align=Align.INLINE)
d.comment(0x823D, 'Non-zero: skip auto-boot', align=Align.INLINE)
d.comment(0x8241, 'Y=&82: ROM page high byte', align=Align.INLINE)
d.comment(0x8243, 'Execute command string at (X, Y)', align=Align.INLINE)
d.comment(0x8300, 'Load FS state byte at offset Y', align=Align.INLINE)
d.comment(0x8303, 'Store to workspace backup area', align=Align.INLINE)
d.comment(0x8305, 'Next byte down', align=Align.INLINE)
d.comment(0x8308, 'Loop for offsets &1D..&15', align=Align.INLINE)
d.comment(0x830A, 'A=&7B: printer driver going dormant', align=Align.INLINE)
d.comment(0x831C, 'Return after port setup', align=Align.INLINE)
d.comment(0x8342, 'A=&2A: error ptr for retry', align=Align.INLINE)
d.comment(0x834A, 'A=&77: OSBYTE close spool/exec', align=Align.INLINE)
d.comment(0x8358, 'A=&2A: error ptr for retry', align=Align.INLINE)

d.label(0x835A, 'store_fs_hdr_clc')
d.comment(0x835A, 'CLC: no byte-stream path', align=Align.INLINE)

d.label(0x835B, 'store_fs_hdr_fn')
d.comment(0x835B, 'Store function code at &0F01', align=Align.INLINE)
d.comment(0x835E, 'Store error ptr for TX poll', align=Align.INLINE)
d.comment(0x8385, 'Load error ptr for TX retry', align=Align.INLINE)
d.comment(0x83A3, 'CLC for address addition', align=Align.INLINE)
d.comment(0x8420, 'Transfer A to Y for indexing', align=Align.INLINE)
d.comment(0x8422, 'Transfer to X for return', align=Align.INLINE)
d.comment(0x847B, 'A=&7E: OSBYTE acknowledge escape', align=Align.INLINE)


d.subroutine(0x847D, 'check_escape_handler', title='Test MOS escape flag and abort if pending', description="""Tests MOS escape flag (&FF bit 7). If escape is pending:
acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
the control block via (net_tx_ptr),Y, and branches to the
NLISTN error path. If no escape, returns immediately.""")
d.comment(0x847D, 'Test escape flag (bit 7)', align=Align.INLINE)
d.comment(0x847F, 'Bit 7 clear: no escape, return', align=Align.INLINE)
d.comment(0x8481, 'Acknowledge escape via OSBYTE &7E', align=Align.INLINE)
d.comment(0x8484, "Non-zero: report 'Not listening'", align=Align.INLINE)
d.comment(0x84AF, 'Return with handle mask in A', align=Align.INLINE)
d.comment(0x8509, 'A = function code / command', align=Align.INLINE)
d.comment(0x850B, 'X = control block ptr lo', align=Align.INLINE)
d.comment(0x850D, 'Y = control block ptr hi', align=Align.INLINE)
d.comment(0x850F, 'X dup for indexed access via (fs_crc)', align=Align.INLINE)
d.comment(0x8511, 'Y dup for indexed access', align=Align.INLINE)
d.comment(0x8513, 'Return', align=Align.INLINE)
d.comment(0x853D, 'Store return addr low as string ptr', align=Align.INLINE)
d.comment(0x8540, 'Store return addr high as string ptr', align=Align.INLINE)
d.comment(0x8542, 'Y=0: offset for indirect load', align=Align.INLINE)
d.comment(0x8546, 'No page wrap: skip high byte inc', align=Align.INLINE)
d.comment(0x8548, 'Handle page crossing in pointer', align=Align.INLINE)
d.comment(0x8564, 'Clear accumulator workspace', align=Align.INLINE)

d.label(0x8566, 'scan_decimal_digit')
d.comment(0x8588, 'Return with result in A', align=Align.INLINE)
d.comment(0x85A3, 'Restore X from stack', align=Align.INLINE)
d.comment(0x85A5, 'Return with mask in X', align=Align.INLINE)
d.comment(0x85D7, 'Next byte', align=Align.INLINE)
d.comment(0x85DA, 'Return with Z flag result', align=Align.INLINE)
d.comment(0x85DF, 'Return (FSCV 7 read handles)', align=Align.INLINE)
d.comment(0x8645, 'X=&C0: TX control block at &00C0', align=Align.INLINE)
d.comment(0x8647, 'Set TX pointer lo', align=Align.INLINE)
d.comment(0x8649, 'X=0: page zero', align=Align.INLINE)
d.comment(0x864D, 'A=&FF: full retry count', align=Align.INLINE)
d.comment(0x8651, 'Save retry count on stack', align=Align.INLINE)
d.comment(0x8652, 'Transfer timeout to A', align=Align.INLINE)
d.comment(0x8653, 'Save timeout on stack', align=Align.INLINE)
d.comment(0x8654, 'X=0 for (net_tx_ptr,X) indirect', align=Align.INLINE)
d.comment(0x8656, 'Load TXCB byte 0 (control/status)', align=Align.INLINE)

d.label(0x8658, 'tx_retry')
d.comment(0x8658, 'Write control byte to start TX', align=Align.INLINE)
d.comment(0x865A, 'Save control byte for retry', align=Align.INLINE)

d.label(0x865B, 'tx_semaphore_spin')
d.comment(0x865B, 'Test TX semaphore (C=1 when free)', align=Align.INLINE)
d.comment(0x865E, 'Spin until semaphore released', align=Align.INLINE)
d.comment(0x8660, 'Copy TX ptr lo to NMI block', align=Align.INLINE)
d.comment(0x8662, 'Store for NMI handler access', align=Align.INLINE)
d.comment(0x8664, 'Copy TX ptr hi to NMI block', align=Align.INLINE)
d.comment(0x8666, 'Store for NMI handler access', align=Align.INLINE)
d.comment(0x8668, 'Initiate ADLC TX via trampoline', align=Align.INLINE)
d.comment(0x866B, 'Poll TXCB byte 0 for completion', align=Align.INLINE)
d.comment(0x866D, 'Bit 7 set: still busy, keep polling', align=Align.INLINE)
d.comment(0x866F, 'Shift bit 6 into bit 7 (error flag)', align=Align.INLINE)
d.comment(0x8670, 'Bit 6 clear: success, clean return', align=Align.INLINE)
d.comment(0x8672, 'Shift bit 5 into carry', align=Align.INLINE)
d.comment(0x8673, 'Zero: fatal error, no escape', align=Align.INLINE)
d.comment(0x8675, 'Check for user escape condition', align=Align.INLINE)
d.comment(0x8678, 'Discard saved control byte', align=Align.INLINE)
d.comment(0x8679, 'Save to X for retry delay', align=Align.INLINE)
d.comment(0x867A, 'Restore timeout parameter', align=Align.INLINE)
d.comment(0x867B, 'Back to Y', align=Align.INLINE)
d.comment(0x867C, 'Restore retry count', align=Align.INLINE)
d.comment(0x867D, 'No retries left: report error', align=Align.INLINE)
d.comment(0x867F, 'Decrement retry count', align=Align.INLINE)
d.comment(0x8681, 'Save updated retry count', align=Align.INLINE)
d.comment(0x8682, 'Timeout to A for delay', align=Align.INLINE)
d.comment(0x8683, 'Save timeout parameter', align=Align.INLINE)
d.comment(0x8684, 'Control byte for delay duration', align=Align.INLINE)
d.comment(0x8685, 'Inner delay loop', align=Align.INLINE)
d.comment(0x8686, 'Spin until X=0', align=Align.INLINE)
d.comment(0x8688, 'Outer delay loop', align=Align.INLINE)
d.comment(0x8689, 'Continue delay', align=Align.INLINE)

d.label(0x868D, 'tx_not_listening')
d.comment(0x868D, 'Save error code in X', align=Align.INLINE)
d.comment(0x868E, "Report 'Not listening' error", align=Align.INLINE)

d.label(0x8691, 'tx_success')
d.comment(0x8691, 'Discard saved control byte', align=Align.INLINE)
d.comment(0x8692, 'Discard timeout parameter', align=Align.INLINE)
d.comment(0x8693, 'Discard retry count', align=Align.INLINE)
d.comment(0x8694, 'Return (success)', align=Align.INLINE)


d.subroutine(0x8698, 'copy_filename_ptr', title='Copy filename pointer to os_text_ptr and parse', description="""Copies the 2-byte filename pointer from (fs_options),Y into
os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
to parse the filename via GSINIT/GSREAD into the &0E30 buffer.""")
d.comment(0x86C7, 'A=&FF: branch to load path', align=Align.INLINE)
d.comment(0x86CC, 'Copy parsed filename to cmd buffer', align=Align.INLINE)
d.comment(0x86CF, 'Y=2: FS function code offset', align=Align.INLINE)
d.comment(0x86D6, 'A=&2A: error ptr for retry', align=Align.INLINE)
d.comment(0x8704, 'Display file info after FS reply', align=Align.INLINE)
d.comment(0x877F, 'A=&14: FS function code for SAVE', align=Align.INLINE)
d.comment(0x8781, 'Build header and send FS save command', align=Align.INLINE)
d.comment(0x8784, 'Display filename being saved', align=Align.INLINE)

d.label(0x8787, 'save_csd_display')
d.comment(0x8787, 'Load CSD from FS reply', align=Align.INLINE)
d.comment(0x878A, 'Transfer file data blocks to server', align=Align.INLINE)

d.label(0x8791, 'send_fs_reply')
d.comment(0x8791, 'Send FS reply acknowledgement', align=Align.INLINE)
d.comment(0x879F, 'Z=1: first byte, use A directly', align=Align.INLINE)

d.label(0x87A1, 'copy_attr_loop')
d.comment(0x87A1, 'Load attribute byte from FS reply', align=Align.INLINE)

d.label(0x87A4, 'direct_attr_copy')
d.comment(0x87A4, 'Store decoded access in param block', align=Align.INLINE)
d.comment(0x87A6, 'Next attribute byte', align=Align.INLINE)
d.comment(0x87C3, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x87C6, 'Loop until offset 2 reached', align=Align.INLINE)
d.comment(0x87C8, 'Return to caller', align=Align.INLINE)

d.label(0x87CF, 'next_block')
d.comment(0x87CF, 'X=0: clear hi bytes of block size', align=Align.INLINE)
d.comment(0x87D1, 'Y=4: process 4 address bytes', align=Align.INLINE)
d.comment(0x87D3, 'Clear block size hi byte 1', align=Align.INLINE)
d.comment(0x87D6, 'Clear block size hi byte 2', align=Align.INLINE)
d.comment(0x87D9, 'CLC for ADC in loop', align=Align.INLINE)

d.label(0x87DA, 'block_addr_loop')
d.comment(0x87DA, 'Source = current position', align=Align.INLINE)
d.comment(0x87DC, 'Store source address byte', align=Align.INLINE)
d.comment(0x87DE, 'Add block size to current position', align=Align.INLINE)
d.comment(0x87E9, 'Carry: address overflowed, clamp', align=Align.INLINE)

d.label(0x87F8, 'clamp_dest_setup')
d.comment(0x8819, 'A=&2A: error ptr for retry', align=Align.INLINE)


d.subroutine(0x8946, 'return_a_zero', title='Return with A=0 via register restore', description="""Loads A=0 and branches (always taken) to the common register
restore exit at restore_args_return. Used as a shared exit
point by ARGSV, FINDV, and GBPBV when an operation is
unsupported or should return zero.""")
d.comment(0x89EA, 'Return (unsupported function)', align=Align.INLINE)
d.comment(0x8A6F, 'Non-zero: branch past error ptr', align=Align.INLINE)

d.label(0x8A71, 'gbpb_read_path')
d.comment(0x8A71, 'Read path: receive data blocks from FS', align=Align.INLINE)
d.comment(0x8CA3, 'Print two CRs (blank line)', align=Align.INLINE)

d.label(0x8CBD, 'cat_examine_loop')
d.comment(0x8CCC, 'Load entry count from reply', align=Align.INLINE)
d.comment(0x8CCF, 'Zero entries returned: catalogue done', align=Align.INLINE)
d.comment(0x8CD1, 'X=2: first entry offset in reply', align=Align.INLINE)
d.comment(0x8CD3, 'Print/format this directory entry', align=Align.INLINE)
d.comment(0x8CD6, 'CLC for addition', align=Align.INLINE)
d.comment(0x8CD7, 'Load current examine start offset', align=Align.INLINE)
d.comment(0x8CD9, 'Add entries returned this batch', align=Align.INLINE)
d.comment(0x8CDC, 'Update next examine start offset', align=Align.INLINE)
d.comment(0x8CDF, 'Save updated start offset', align=Align.INLINE)
d.comment(0x8CE1, 'Reload batch size for next request', align=Align.INLINE)
d.comment(0x8CE3, 'Store batch size in command buffer', align=Align.INLINE)
d.comment(0x8CE6, 'Loop for remaining characters', align=Align.INLINE)
d.comment(0x8DC9, 'Return after calculation', align=Align.INLINE)
d.comment(0x8DE7, 'Preserve carry via ROL', align=Align.INLINE)
d.comment(0x8DEA, 'A=&3F: handle closed/unused marker', align=Align.INLINE)
d.comment(0x8DEC, 'Mark handle as closed in workspace', align=Align.INLINE)


d.label(0x8DEE, 'restore_rx_flags')
d.subroutine(0x8DEE, 'restore_rx_flags', title='Restore RX flags after close handle', description="""Performs ROR on rx_flags to restore the carry flag state
that was preserved by the matching ROL in net_3_close_handle.
Falls through to osword_12_handler (clearing fs_temp_ce).""")
d.comment(0x8DEE, 'Restore carry via ROR', align=Align.INLINE)
d.comment(0x8DFC, 'Outside our OSWORD range, exit', align=Align.INLINE)
d.comment(0x8E02, 'X = sub-function code for table lookup', align=Align.INLINE)

d.label(0x8E2B, 'load_workspace_byte')
d.comment(0x8E2D, 'Store to param block (no-op if C=1)', align=Align.INLINE)
d.comment(0x8E33, 'Return after copy', align=Align.INLINE)
d.comment(0x8E34, 'ASL: set C if TX in progress', align=Align.INLINE)
d.comment(0x8E37, 'C=0: read path', align=Align.INLINE)
d.comment(0x8F27, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x8F2D, 'Dest station = &FFFF (accept reply from any station)', align=Align.INLINE)
d.comment(0x8F58, 'Y=&28: RXCB template offset', align=Align.INLINE)
d.comment(0x8F5E, 'Receive data blocks until command byte = &00 or &0D', align=Align.INLINE)
d.comment(0x8F95, 'Y=&04: advance to station address', align=Align.INLINE)
d.comment(0x8FDE, 'Y=&7D: store byte for TX at offset &7D', align=Align.INLINE)
d.comment(0x8FE0, 'Store data byte at (net_rx_ptr)+&7D for TX', align=Align.INLINE)
d.comment(0x8FE2, 'Save data byte for &0D check after TX', align=Align.INLINE)
d.comment(0x8FE3, 'Set up TX control block', align=Align.INLINE)
d.comment(0x8FE6, 'Enable interrupts for TX', align=Align.INLINE)
d.comment(0x8FE7, 'Enable IRQs and transmit', align=Align.INLINE)

d.label(0x8FEA, 'delay_between_tx')
d.comment(0x8FEA, 'Short delay loop between TX packets', align=Align.INLINE)
d.comment(0x8FEB, 'Spin until X reaches 0', align=Align.INLINE)
d.comment(0x8FED, 'Restore data byte for terminator check', align=Align.INLINE)
d.comment(0x8FEE, 'Z=1: not intercepted, pass through', align=Align.INLINE)


d.subroutine(0x9001, 'enable_irq_and_tx', title='Enable interrupts and transmit via tx_poll_ff', description="""CLI to enable interrupts, then JMP tx_poll_ff. A short
tail-call wrapper used after building the TX control block.""")
d.comment(0x909B, 'Write &7F to RXCB (wait for reply)', align=Align.INLINE)

d.label(0x909D, 'poll_rxcb_loop')
d.comment(0x909D, 'Poll RXCB for completion (bit7)', align=Align.INLINE)
d.comment(0x90F4, 'Set up TX and send RWORD packet', align=Align.INLINE)
d.comment(0x9177, 'V=1: use (net_rx_ptr) page', align=Align.INLINE)
d.comment(0x9179, 'V=1: skip to net_rx_ptr page', align=Align.INLINE)
d.comment(0x917B, 'V=0: use (nfs_workspace) page', align=Align.INLINE)

d.label(0x917D, 'rxcb_matched')
d.comment(0x9189, 'Loop until all template bytes done', align=Align.INLINE)
d.comment(0x918C, 'Store final offset as net_tx_ptr', align=Align.INLINE)
d.comment(0x91C4, 'Store initial PFLAGS value', align=Align.INLINE)
d.comment(0x9230, 'Load current PFLAGS', align=Align.INLINE)
d.comment(0x9233, 'Save current PFLAGS', align=Align.INLINE)
d.comment(0x9234, 'Carry = current sequence (bit 7)', align=Align.INLINE)
d.comment(0x9235, 'Restore original PFLAGS', align=Align.INLINE)
d.comment(0x9236, 'Toggle sequence number (bit 7 of PFLAGS)', align=Align.INLINE)
d.comment(0x9238, 'Store toggled sequence number', align=Align.INLINE)
d.comment(0x928A, 'Transfer count to X', align=Align.INLINE)
d.comment(0x928B, 'Test for retry exhaustion', align=Align.INLINE)
d.comment(0x928C, 'X wrapped to 0: retries exhausted', align=Align.INLINE)
d.comment(0x9304, 'Return after storing result', align=Align.INLINE)
d.comment(0x9660, 'Trampoline: forward to tx_begin', align=Align.INLINE)
d.comment(0x9663, 'Trampoline: forward to adlc_init', align=Align.INLINE)
d.comment(0x9666, 'Trampoline: forward to NMI release', align=Align.INLINE)
d.comment(0x9669, 'Trampoline: forward to NMI claim', align=Align.INLINE)
d.comment(0x966C, 'Trampoline: forward to IRQ handler', align=Align.INLINE)
d.comment(0x9694, 'A=0: clear source network', align=Align.INLINE)
d.comment(0x9696, 'Clear TX source network byte', align=Align.INLINE)
d.comment(0x9699, 'INTON: re-enable NMIs (&FE20 read side effect)', align=Align.INLINE)
d.comment(0x969C, 'Return to caller', align=Align.INLINE)
d.comment(0x96DE, 'Write CR1: full reset', align=Align.INLINE)
d.comment(0x96E3, 'Write CR4 via ADLC reg 3 (AC=1)', align=Align.INLINE)
d.comment(0x96E8, 'Write CR3=0: clear loop-back/AEX/DTR', align=Align.INLINE)
d.comment(0x96ED, 'Write CR1: RIE | TX_RESET', align=Align.INLINE)
d.comment(0x96F2, 'Write CR2: listen mode config', align=Align.INLINE)
d.comment(0x970B, 'Store broadcast flag in TX flags', align=Align.INLINE)
d.comment(0x9710, 'High byte of scout net handler', align=Align.INLINE)
d.comment(0x9712, 'Install next handler and RTI', align=Align.INLINE)
d.comment(0x9725, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x9728, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x9732, 'High byte of scout data handler', align=Align.INLINE)
d.comment(0x9734, 'Install scout data loop and RTI', align=Align.INLINE)
d.comment(0x9744, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x9763, 'Copied all 12 scout bytes?', align=Align.INLINE)

d.label(0x97AB, 'scan_nfs_port_list')
d.comment(0x97AB, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x97AD, 'A=0: no NFS workspace offset yet', align=Align.INLINE)
d.comment(0x97AF, 'Clear NFS workspace search flag', align=Align.INLINE)

d.label(0x97B3, 'scout_ctrl_check')
d.comment(0x97BB, 'Y=1: advance to port byte in slot', align=Align.INLINE)

d.label(0x97CF, 'scout_port_match')
d.comment(0x97D9, 'CLC for 12-byte slot advance', align=Align.INLINE)
d.comment(0x97DA, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x97DC, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x97DE, "Always branches (page &C0 won't overflow)", align=Align.INLINE)

d.label(0x97E0, 'scout_station_check')
d.comment(0x97E0, 'Check if NFS workspace already searched', align=Align.INLINE)
d.comment(0x97E2, 'Already searched: no match found', align=Align.INLINE)

d.label(0x97E4, 'scout_network_match')
d.comment(0x97E4, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x97E7, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x97E9, 'Get NFS workspace page number', align=Align.INLINE)
d.comment(0x97EB, 'Mark NFS workspace as search target', align=Align.INLINE)
d.comment(0x97ED, 'Y=0: start at offset 0 in workspace', align=Align.INLINE)
d.comment(0x97EF, 'Reset slot pointer to start', align=Align.INLINE)

d.label(0x97F3, 'scout_accept')
d.comment(0x97F3, 'Check broadcast flag (bit 6)', align=Align.INLINE)
d.comment(0x97F6, 'Not broadcast: ACK and set up RX', align=Align.INLINE)
d.comment(0x97F8, 'Broadcast: copy scout fields directly', align=Align.INLINE)

d.label(0x97FB, 'ack_scout_match')
d.comment(0x97FB, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x97FD, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x9800, 'Save current TX block ptr (low)', align=Align.INLINE)
d.comment(0x9802, 'Push TX block low on stack', align=Align.INLINE)
d.comment(0x9803, 'Save current TX block ptr (high)', align=Align.INLINE)
d.comment(0x9805, 'Push TX block high on stack', align=Align.INLINE)
d.comment(0x9806, 'Use port slot as temp RXCB ptr (lo)', align=Align.INLINE)
d.comment(0x9808, 'Set RXCB low for tx_calc_transfer', align=Align.INLINE)
d.comment(0x980A, 'Use workspace page as temp RXCB (hi)', align=Align.INLINE)
d.comment(0x980C, 'Set RXCB high for tx_calc_transfer', align=Align.INLINE)
d.comment(0x980E, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x9811, 'Restore original TX block (high)', align=Align.INLINE)
d.comment(0x9812, 'Restore TX block ptr (high)', align=Align.INLINE)
d.comment(0x9814, 'Restore original TX block (low)', align=Align.INLINE)
d.comment(0x9815, 'Restore TX block ptr (low)', align=Align.INLINE)
d.comment(0x9817, 'Transfer OK: send data ACK', align=Align.INLINE)
d.comment(0x9834, 'High byte of nmi_data_rx handler', align=Align.INLINE)
d.comment(0x984A, 'High byte of nmi_data_rx_net handler', align=Align.INLINE)


d.subroutine(0x9870, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects either the normal bulk RX handler (&989A) or the Tube
RX handler (&98F7) based on the Tube transfer flag in tx_flags,
and installs the appropriate NMI handler.""")
d.comment(0x988F, "A=&41: 'not listening' error", align=Align.INLINE)
d.comment(0x98FF, 'Advance Tube transfer byte count', align=Align.INLINE)
d.comment(0x9901, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x9904, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x9906, 'Carry to transfer count byte 2', align=Align.INLINE)
d.comment(0x9908, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x990A, 'Carry to transfer count byte 3', align=Align.INLINE)
d.comment(0x990C, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x990E, 'Carry to transfer count byte 4', align=Align.INLINE)
d.comment(0x9910, 'All bytes zero: overflow error', align=Align.INLINE)

d.label(0x9912, 'rx_update_buf')
d.comment(0x9912, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x9915, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x9918, 'Advance count after second byte', align=Align.INLINE)
d.comment(0x991A, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x991C, 'Carry to count byte 2', align=Align.INLINE)
d.comment(0x991E, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x9920, 'Carry to count byte 3', align=Align.INLINE)
d.comment(0x9922, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x9924, 'Carry to count byte 4', align=Align.INLINE)
d.comment(0x9926, 'Zero: Tube transfer complete', align=Align.INLINE)

d.label(0x9928, 'rx_check_error')
d.comment(0x9928, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x992B, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x992D, 'Return from NMI, wait for data', align=Align.INLINE)
d.comment(0x999F, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x99A2, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x99A5, 'bit7 set: start data TX phase', align=Align.INLINE)

d.label(0x99B8, 'tdra_error')
d.comment(0x99B8, 'TDRA error: jump to error handler', align=Align.INLINE)
d.comment(0x99BB, 'Check port byte from scout', align=Align.INLINE)
d.comment(0x99BE, 'Non-zero port: advance RX buffer', align=Align.INLINE)


d.subroutine(0x99C3, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")
d.comment(0x99F9, 'Restore X from stack', align=Align.INLINE)
d.comment(0x99FA, 'Transfer to X register', align=Align.INLINE)
d.comment(0x99FB, 'Y=8: RXCB buffer ptr offset', align=Align.INLINE)
d.comment(0x99FD, 'Load current RXCB buffer ptr lo', align=Align.INLINE)
d.comment(0x99FF, 'SEC for ADC #0 = add carry', align=Align.INLINE)
d.comment(0x9A00, 'Increment by 1 (Tube extra byte)', align=Align.INLINE)
d.comment(0x9A02, 'Store updated ptr back to RXCB', align=Align.INLINE)
d.comment(0x9A04, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)

d.label(0x9A07, 'add_buf_to_base')

d.label(0x9A0E, 'inc_rxcb_buf_hi')

d.label(0x9A12, 'store_rxcb_buf_ptr')

d.label(0x9A17, 'store_rxcb_buf_hi')
d.comment(0x9A36, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x9A3B, 'A=&82: Tube release claim type', align=Align.INLINE)

d.label(0x9A4A, 'copy_scout_fields')
d.comment(0x9A4A, 'Y=4: start at RX CB offset 4', align=Align.INLINE)

d.label(0x9A4C, 'copy_scout_loop')
d.comment(0x9A4C, 'Load scout field (stn/net/ctrl/port)', align=Align.INLINE)
d.comment(0x9A4F, 'Store to port workspace buffer', align=Align.INLINE)
d.comment(0x9A51, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9A52, 'All 8 fields copied?', align=Align.INLINE)
d.comment(0x9A54, 'No: continue copy loop', align=Align.INLINE)
d.comment(0x9A56, 'Jump to completion handler', align=Align.INLINE)
d.comment(0x9A68, 'Load source station number', align=Align.INLINE)
d.comment(0x9A6B, 'Station >= &F0? (privileged)', align=Align.INLINE)
d.comment(0x9A6D, 'Privileged: skip protection check', align=Align.INLINE)
d.comment(0x9A7B, 'Carry clear: operation permitted', align=Align.INLINE)
d.comment(0x9A7D, 'Operation blocked by LSTAT mask', align=Align.INLINE)

d.label(0x9A80, 'imm_op_dispatch')
d.comment(0x9A80, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x9A83, 'Look up handler address high byte', align=Align.INLINE)
d.comment(0x9A86, 'Push handler address high', align=Align.INLINE)
d.comment(0x9A87, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x9A8A, 'Push handler address low', align=Align.INLINE)
d.comment(0x9A8B, 'RTS dispatches to handler', align=Align.INLINE)

d.label(0x9A8C, 'imm_op_out_of_range')
d.comment(0x9A8C, 'Jump to discard handler', align=Align.INLINE)
d.comment(0x9A9F, 'Buffer start lo = &00', align=Align.INLINE)
d.comment(0x9AA1, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9AA3, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x9AA5, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9AA7, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9AA9, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9AAB, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x9AAD, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9AAF, 'Y=3: copy 4 bytes (3 down to 0)', align=Align.INLINE)

d.label(0x9AB1, 'copy_addr_loop')
d.comment(0x9AB1, 'Load remote address byte', align=Align.INLINE)
d.comment(0x9AB4, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x9AB7, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9AB8, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x9ABA, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x9ABD, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9ABF, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AC1, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AC3, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9AC5, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x9AC8, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9ACA, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9ACC, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x9ACE, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9AD0, 'Buffer start lo = &25', align=Align.INLINE)
d.comment(0x9AD2, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9AD4, 'Buffer hi = &7F (below screen)', align=Align.INLINE)
d.comment(0x9AD6, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9AD8, 'Enter reply build path', align=Align.INLINE)
d.comment(0x9ADB, 'Save current TX block low byte', align=Align.INLINE)
d.comment(0x9ADD, 'Push to stack', align=Align.INLINE)
d.comment(0x9ADE, 'Save current TX block high byte', align=Align.INLINE)
d.comment(0x9AE0, 'Push to stack', align=Align.INLINE)
d.comment(0x9AE1, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9AE3, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AE5, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AE7, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9AE9, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x9AEB, 'Store scout status', align=Align.INLINE)
d.comment(0x9AEE, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x9AF1, 'Restore saved nmi_tx_block_hi', align=Align.INLINE)
d.comment(0x9AF2, 'Restore workspace ptr hi byte', align=Align.INLINE)
d.comment(0x9AF4, 'Restore saved nmi_tx_block', align=Align.INLINE)
d.comment(0x9AF5, 'Restore workspace ptr lo byte', align=Align.INLINE)
d.comment(0x9AF7, 'C=0: transfer not set up, discard', align=Align.INLINE)

d.label(0x9AF9, 'set_tx_reply_flag')
d.comment(0x9AF9, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x9AFC, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x9AFE, 'Store updated TX flags', align=Align.INLINE)

d.label(0x9B01, 'rx_imm_halt_cont')
d.comment(0x9B01, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9B03, 'Write CR1: enable TX interrupts', align=Align.INLINE)

d.label(0x9B06, 'tx_cr2_setup')
d.comment(0x9B06, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x9B08, 'Write CR2 for TX setup', align=Align.INLINE)

d.label(0x9B0B, 'tx_nmi_setup')
d.comment(0x9B0B, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x9B0D, 'Y=&9B: dispatch table page', align=Align.INLINE)
d.comment(0x9B0F, 'Acknowledge and write TX dest', align=Align.INLINE)


d.subroutine(0x9B19, 'imm_op_build_reply', title='Build immediate operation reply header', description="""Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")

d.label(0x9B4F, 'imm_op_discard')

d.label(0x9B52, 'check_sr_irq')
d.comment(0x9B52, 'A=&04: IFR bit 2 (SR) mask', align=Align.INLINE)
d.comment(0x9B54, 'Test SR interrupt pending', align=Align.INLINE)
d.comment(0x9B57, 'SR fired: handle TX completion', align=Align.INLINE)
d.comment(0x9B59, 'A=5: no SR, return status 5', align=Align.INLINE)
d.comment(0x9B5B, 'Return (no SR interrupt)', align=Align.INLINE)

d.label(0x9B5C, 'tx_done_error')
d.comment(0x9B5C, 'Save X', align=Align.INLINE)
d.comment(0x9B5D, 'Push X', align=Align.INLINE)
d.comment(0x9B5E, 'Save Y', align=Align.INLINE)
d.comment(0x9B5F, 'Push Y', align=Align.INLINE)
d.comment(0x9B60, 'Read ACR for shift register mode', align=Align.INLINE)
d.comment(0x9B63, 'Clear SR mode bits (2-4)', align=Align.INLINE)
d.comment(0x9B65, 'Restore original SR mode', align=Align.INLINE)
d.comment(0x9B68, 'Write updated ACR', align=Align.INLINE)
d.comment(0x9B6B, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x9B6E, 'A=&04: SR bit mask', align=Align.INLINE)
d.comment(0x9B70, 'Clear SR in IFR', align=Align.INLINE)
d.comment(0x9B73, 'Disable SR in IER', align=Align.INLINE)
d.comment(0x9B76, 'Load ctrl byte for dispatch', align=Align.INLINE)
d.comment(0x9B79, 'Ctrl >= &86? (HALT/CONTINUE)', align=Align.INLINE)
d.comment(0x9B7B, 'Yes: skip protection mask save', align=Align.INLINE)
d.comment(0x9B7D, 'Load current protection mask', align=Align.INLINE)
d.comment(0x9B80, 'Save mask before JSR modification', align=Align.INLINE)
d.comment(0x9B83, 'Enable bits 2-4 (allow JSR ops)', align=Align.INLINE)
d.comment(0x9B85, 'Store modified protection mask', align=Align.INLINE)

d.label(0x9B88, 'tx_done_classify')
d.comment(0x9B88, 'Load handler addr hi from table', align=Align.INLINE)
d.comment(0x9B8B, 'Push handler hi', align=Align.INLINE)
d.comment(0x9B8C, 'Load handler addr lo from table', align=Align.INLINE)
d.comment(0x9B8F, 'Push handler lo', align=Align.INLINE)
d.comment(0x9B90, 'Dispatch via RTS (addr-1 on stack)', align=Align.INLINE)
d.comment(0x9B9B, 'Push hi of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x9B9D, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x9B9E, 'Push lo of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x9BA0, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x9BA1, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)
d.comment(0x9BA4, 'Y=8: network event type', align=Align.INLINE)
d.comment(0x9BA6, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9BA9, 'A = remote address hi', align=Align.INLINE)
d.comment(0x9BAF, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9BB2, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9BB5, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x9BB8, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x9BBB, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9BBE, 'A=&04: bit 2 mask for rx_flags', align=Align.INLINE)
d.comment(0x9BC0, 'Test if already halted', align=Align.INLINE)
d.comment(0x9BC3, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x9BC5, 'Set bit 2 in rx_flags', align=Align.INLINE)
d.comment(0x9BC8, 'Store halt flag', align=Align.INLINE)
d.comment(0x9BCB, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x9BCD, 'Enable interrupts during halt wait', align=Align.INLINE)

d.label(0x9BCE, 'halt_spin_loop')
d.comment(0x9BCE, 'Test halt flag', align=Align.INLINE)
d.comment(0x9BD1, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x9BD5, 'Load current RX flags', align=Align.INLINE)
d.comment(0x9BD8, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x9BDA, 'Store updated flags', align=Align.INLINE)
d.comment(0x9BDD, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9BDE, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x9BDF, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9BE0, 'Transfer to X register', align=Align.INLINE)
d.comment(0x9BE1, 'A=0: success status', align=Align.INLINE)
d.comment(0x9BE3, 'Return with A=0 (success)', align=Align.INLINE)


d.subroutine(0x9BE4, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")
d.comment(0x9C13, '(continued)', align=Align.INLINE)
d.comment(0x9C14, '(continued)', align=Align.INLINE)
d.comment(0x9C15, '(continued)', align=Align.INLINE)
d.comment(0x9C1C, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x9C1D, '(continued)', align=Align.INLINE)
d.comment(0x9C1E, '(continued)', align=Align.INLINE)
d.comment(0x9C1F, '(continued)', align=Align.INLINE)
d.comment(0x9C20, '(continued)', align=Align.INLINE)

d.label(0x9C27, 'check_imm_range')
d.comment(0x9C48, 'Save TX index', align=Align.INLINE)
d.comment(0x9C4B, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x9C4C, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x9C51, 'Save interrupt state', align=Align.INLINE)
d.comment(0x9C52, 'Disable interrupts for ADLC access', align=Align.INLINE)


d.subroutine(0x9C53, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Mid-instruction label within the INACTIVE polling loop.
The operand byte of the LDA before tx_begin is referenced
as a constant for self-modifying code. Disables NMIs twice
(belt-and-braces) then tests SR2 for INACTIVE before
proceeding with TX.""")

d.label(0x9C59, 'test_line_idle')
d.comment(0x9C63, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x9C70, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x9C72, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x9C75, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C77, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x9C7A, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C7C, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x9C7F, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C81, 'All 3 bytes overflowed: line jammed', align=Align.INLINE)
d.comment(0x9C84, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9C8E, 'Pop saved register', align=Align.INLINE)
d.comment(0x9C8F, 'Pop saved register', align=Align.INLINE)
d.comment(0x9CCB, 'Load handler from dispatch table', align=Align.INLINE)
d.comment(0x9CCE, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9CCF, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x9CD2, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9CD3, 'RTS dispatches to control-byte handler', align=Align.INLINE)

d.label(0x9CE4, 'imm_op_status3')
d.comment(0x9CE4, 'A=3: scout_status for PEEK', align=Align.INLINE)
d.comment(0x9CE8, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x9CEC, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)

d.label(0x9CEE, 'store_status_add4')
d.comment(0x9CEE, 'Store scout status', align=Align.INLINE)
d.comment(0x9CF1, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x9CF2, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9CF3, 'Y=&0C: start at offset 12', align=Align.INLINE)

d.label(0x9CF5, 'add_bytes_loop')
d.comment(0x9CF5, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x9CF8, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x9CF9, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x9CFB, 'Store updated address byte', align=Align.INLINE)
d.comment(0x9CFE, 'Next byte', align=Align.INLINE)
d.comment(0x9CFF, 'Save carry for next addition', align=Align.INLINE)
d.comment(0x9D00, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x9D02, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x9D04, 'Restore processor flags', align=Align.INLINE)
d.comment(0x9D05, 'Calculate transfer byte count', align=Align.INLINE)
d.comment(0x9D08, 'Jump to TX control exit', align=Align.INLINE)
d.comment(0x9D0B, 'A=2: scout_status for procedure ops', align=Align.INLINE)

d.label(0x9D0D, 'store_status_calc_xfer')
d.comment(0x9D0D, 'Store scout status', align=Align.INLINE)
d.comment(0x9D10, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x9D13, 'Exit TX ctrl setup', align=Align.INLINE)

d.label(0x9D3D, 'proc_op_status2')

d.label(0x9D3F, 'store_status_copy_ptr')
d.comment(0x9D5A, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x9D5B, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x9D5E, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x9D5F, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x9D78, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x9D81, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x9D82, 'Increment delay counter', align=Align.INLINE)
d.comment(0x9D83, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x9D96, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x9DA1, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x9DA3, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x9DA6, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x9DAD, 'High byte of nmi_reply_scout addr', align=Align.INLINE)
d.comment(0x9DAF, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9DC3, 'High byte of nmi_reply_cont', align=Align.INLINE)
d.comment(0x9DC5, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9DD4, 'High byte of nmi_reply_validate', align=Align.INLINE)
d.comment(0x9DDE, "A=&41: 'not listening' error code", align=Align.INLINE)
d.comment(0x9DE0, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x9E91, 'bit7 clear: error path', align=Align.INLINE)
d.comment(0x9E93, 'ADLC reset and return to idle', align=Align.INLINE)

d.label(0x9E96, 'nmi_tx_not_listening')
d.comment(0x9E96, "A=&41: 'not listening' error", align=Align.INLINE)

d.label(0x9E98, 'jmp_tx_result_fail')
d.comment(0x9E98, 'Store result and return to idle', align=Align.INLINE)
d.comment(0x9E9B, 'Load saved handler low byte', align=Align.INLINE)

d.label(0x9EC9, 'tube_tx_inc_byte2')

d.label(0x9ED1, 'tube_tx_inc_byte4')
d.comment(0x9EFA, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9EFC, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9F0B, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9F12, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9F2A, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x9F2D, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x9F2F, 'Install data RX handler', align=Align.INLINE)

d.label(0x9F3D, 'tx_result_fail')
d.comment(0x9F6B, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x9F70, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x9F7A, '(continued)', align=Align.INLINE)
d.comment(0x9F7B, '(continued)', align=Align.INLINE)
d.comment(0x9F7C, '(continued)', align=Align.INLINE)
d.comment(0x9F84, '(continued)', align=Align.INLINE)
d.comment(0x9F85, '(continued)', align=Align.INLINE)
d.comment(0x9F90, 'CLC for base pointer addition', align=Align.INLINE)
d.comment(0x9F91, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x9F98, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x9FA0, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x9FA5, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9FA6, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x9FCA, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x9FE5, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x0438, 'Y=8: write to Tube control register', align=Align.INLINE)
d.comment(0x043A, 'Configure Tube for data transfer', align=Align.INLINE)
d.comment(0x043D, 'Y=&10: data transfer control value', align=Align.INLINE)
d.comment(0x043F, 'Check transfer type (X=2?)', align=Align.INLINE)
d.comment(0x0441, 'X<2: skip alternate control', align=Align.INLINE)
d.comment(0x0443, 'Y=&90: alternate control for X>=2', align=Align.INLINE)
d.comment(0x0445, 'Write transfer control to Tube', align=Align.INLINE)
d.comment(0x0448, 'Send data byte via Tube R4', align=Align.INLINE)
d.comment(0x044B, 'Y=&88: post-transfer control value', align=Align.INLINE)
d.comment(0x044D, 'Transfer type to A for comparison', align=Align.INLINE)
d.comment(0x044E, 'Type 0: go to NMI flush check', align=Align.INLINE)
d.comment(0x0450, 'Check if type 2', align=Align.INLINE)
d.comment(0x0452, 'Type 2: go to NMI flush check', align=Align.INLINE)
d.comment(0x0454, 'Write post-transfer control', align=Align.INLINE)
d.comment(0x0457, 'Check if type 4 (SENDW)', align=Align.INLINE)
d.comment(0x0467, 'V=0: not ready, poll again', align=Align.INLINE)
d.comment(0x0469, 'Flush Tube R3 data register', align=Align.INLINE)
d.comment(0x046C, 'Flush Tube R3 again', align=Align.INLINE)
d.comment(0x046F, 'Write final control value', align=Align.INLINE)
d.comment(0x0472, 'Return from Tube data setup', align=Align.INLINE)
d.comment(0x053F, 'Restore saved Y from temporary', align=Align.INLINE)
d.comment(0x8074, 'Transfer Y to A for dispatch', align=Align.INLINE)
d.comment(0x80CA, 'Set WRCHV low byte', align=Align.INLINE)
d.comment(0x80CD, 'A=5: WRCHV high byte', align=Align.INLINE)
d.comment(0x80CF, 'Set WRCHV high byte', align=Align.INLINE)
d.comment(0x80D4, 'Set RDCHV low byte', align=Align.INLINE)
d.comment(0x80D7, 'A=4: RDCHV high byte', align=Align.INLINE)
d.comment(0x80D9, 'Set RDCHV high byte', align=Align.INLINE)
d.comment(0x80DE, 'Set BRKV low byte', align=Align.INLINE)
d.comment(0x80E1, 'A=0: BRKV high byte (page zero)', align=Align.INLINE)
d.comment(0x80E3, 'Set BRKV high byte', align=Align.INLINE)
d.comment(0x80E8, 'Set EVNTV low byte', align=Align.INLINE)
d.comment(0x80EB, 'A=6: EVNTV high byte', align=Align.INLINE)
d.comment(0x80ED, 'Set EVNTV high byte', align=Align.INLINE)
d.comment(0x80F2, 'Write &8E to Tube control register', align=Align.INLINE)
d.comment(0x80F5, 'Save Y to temporary', align=Align.INLINE)
d.comment(0x80F7, 'Y=0: start ROM-to-RAM copy loop', align=Align.INLINE)
d.comment(0x8270, 'Compare Y against workspace boundary', align=Align.INLINE)
d.comment(0x8272, 'Y>=&10: already allocated, return', align=Align.INLINE)
d.comment(0x8274, 'Claim workspace up to page &10', align=Align.INLINE)
d.comment(0x8276, 'Return to caller', align=Align.INLINE)
d.comment(0x8410, 'Advance to next reply buffer byte', align=Align.INLINE)
d.comment(0x8411, 'A=CR: terminator to search for', align=Align.INLINE)
d.comment(0x8413, 'XOR with buffer byte (0 when CR)', align=Align.INLINE)
d.comment(0x8415, 'Not CR: continue scanning', align=Align.INLINE)
d.comment(0x8417, 'Store 0 (from XOR) to replace CR', align=Align.INLINE)
d.comment(0x8419, 'Execute error via JMP indirect', align=Align.INLINE)
d.comment(0x843E, 'Advance output buffer position', align=Align.INLINE)
d.comment(0x843F, 'Advance source string pointer', align=Align.INLINE)
d.comment(0x8440, 'Continue copying message bytes', align=Align.INLINE)
d.comment(0x8442, 'Execute constructed BRK error', align=Align.INLINE)
d.comment(0x8551, 'Continue printing loop', align=Align.INLINE)
d.comment(0x8556, 'Load character from parameter string', align=Align.INLINE)
d.comment(0x8558, 'Advance to next character', align=Align.INLINE)
d.comment(0x8559, 'Compare against space (ASCII &20)', align=Align.INLINE)
d.comment(0x855B, 'Space found: keep scanning', align=Align.INLINE)
d.comment(0x855D, 'Back up one (first non-space char)', align=Align.INLINE)
d.comment(0x855E, "Compare against 'A' for case flag", align=Align.INLINE)
d.comment(0x8560, "Return: A=char, C set if >= 'A'", align=Align.INLINE)
d.comment(0x85AF, 'Return with A=handle number', align=Align.INLINE)
d.comment(0x85BD, 'Store divisor in temporary', align=Align.INLINE)
d.comment(0x85BF, 'Transfer dividend (Y) to A', align=Align.INLINE)
d.comment(0x85C0, "X=&2F: ASCII '0'-1 (loop init)", align=Align.INLINE)
d.comment(0x85C2, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x85C3, "Increment digit (ASCII '0'..'9')", align=Align.INLINE)
d.comment(0x85C4, 'Subtract divisor from remainder', align=Align.INLINE)
d.comment(0x85C6, 'Carry set: subtract again', align=Align.INLINE)
d.comment(0x85C8, 'Add back divisor (undo last SBC)', align=Align.INLINE)
d.comment(0x85CA, 'Remainder to Y for next digit', align=Align.INLINE)
d.comment(0x85CB, 'Quotient digit (X) to A for print', align=Align.INLINE)
d.comment(0x85E0, 'Invert A (NOT mask)', align=Align.INLINE)
d.comment(0x85E2, 'AND inverted mask to clear bits', align=Align.INLINE)
d.comment(0x85E5, 'OR mask into EOF flags', align=Align.INLINE)
d.comment(0x85E8, 'Store updated EOF flags', align=Align.INLINE)
d.comment(0x85EB, 'Return to caller', align=Align.INLINE)
d.comment(0x85EC, 'Save full byte on stack', align=Align.INLINE)
d.comment(0x85ED, 'Shift high nibble to low position', align=Align.INLINE)
d.comment(0x85EE, 'Continue shift (4 LSRs total)', align=Align.INLINE)
d.comment(0x85EF, 'Continue shift', align=Align.INLINE)
d.comment(0x85F0, 'High nibble now in bits 0-3', align=Align.INLINE)
d.comment(0x85F1, 'Print high nibble as hex', align=Align.INLINE)
d.comment(0x85F4, 'Restore original byte', align=Align.INLINE)
d.comment(0x85F5, 'Mask to low nibble', align=Align.INLINE)
d.comment(0x85F7, "Convert to ASCII digit ('0'-'9')", align=Align.INLINE)
d.comment(0x85F9, "Compare against ':' (past '9'?)", align=Align.INLINE)
d.comment(0x85FB, 'Digit 0-9: skip A-F adjustment', align=Align.INLINE)
d.comment(0x85FD, "Add 7 to get ASCII 'A'-'F'", align=Align.INLINE)
d.comment(0x85FF, 'ALWAYS branch to print character', align=Align.INLINE)
d.comment(0x8934, 'Transfer A to Y for test', align=Align.INLINE)
d.comment(0x8935, 'Non-zero: halve A', align=Align.INLINE)
d.comment(0x8937, 'A=5: default FS number', align=Align.INLINE)
d.comment(0x8BD7, "XOR with '.' (abbreviation check)", align=Align.INLINE)
d.comment(0x8BF3, 'Pre-decrement Y for parameter', align=Align.INLINE)
d.comment(0x8BF4, 'X=1: boot option display field', align=Align.INLINE)
d.comment(0x8BF6, 'Store to fs_work_7 (&B7)', align=Align.INLINE)
d.comment(0x8BF8, 'X=&50: 80-column display width', align=Align.INLINE)
d.comment(0x8BFA, 'Store column width at &B6', align=Align.INLINE)
d.comment(0x8CF8, 'Store Y (library handle) to &0E04', align=Align.INLINE)
d.comment(0x8CFB, 'Non-zero: continue to set handle', align=Align.INLINE)
d.comment(0x8D4C, 'Offset 0 (BRK opcode as zero byte)', align=Align.INLINE)
d.comment(0x8D50, 'Y=10: default character count', align=Align.INLINE)
d.comment(0x8D52, 'Load character from reply buffer', align=Align.INLINE)
d.comment(0x8D58, 'Advance to next character', align=Align.INLINE)
d.comment(0x8D59, 'Decrement remaining count', align=Align.INLINE)
d.comment(0x8D5A, 'Loop until count exhausted', align=Align.INLINE)
d.comment(0x8D5C, 'Return to caller', align=Align.INLINE)
d.comment(0x8D5D, 'Print one space character', align=Align.INLINE)
d.comment(0x8D60, 'Decrement space count', align=Align.INLINE)
d.comment(0x8D61, 'Loop until all spaces printed', align=Align.INLINE)
d.comment(0x8D63, 'Return to caller', align=Align.INLINE)
d.comment(0x8D64, 'X=0: start of output buffer', align=Align.INLINE)
d.comment(0x8D73, 'Return to caller', align=Align.INLINE)
d.comment(0x8D74, 'X=0: start of reply buffer', align=Align.INLINE)
d.comment(0x8D76, 'Load character from reply', align=Align.INLINE)
d.comment(0x8D79, 'Bit 7 set: end of string', align=Align.INLINE)
d.comment(0x8D7B, 'Non-zero: printable character', align=Align.INLINE)
d.comment(0x8D7D, 'Replace null with CR', align=Align.INLINE)
d.comment(0x8D82, 'Advance to next character', align=Align.INLINE)
d.comment(0x8D83, 'Continue printing directory path', align=Align.INLINE)
d.comment(0x8DB0, 'Y=&6F: handle offset in RX buffer', align=Align.INLINE)
d.comment(0x8DB2, 'Load handle byte from RX data', align=Align.INLINE)
d.comment(0x8DB4, 'Store handle to &F0', align=Align.INLINE)
d.comment(0x8DB6, 'Branch to cleanup path', align=Align.INLINE)
d.comment(0x8DF1, 'C=0: branch to cleanup exit', align=Align.INLINE)
d.comment(0x8E18, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0x903E, 'Get stack pointer for flag access', align=Align.INLINE)
d.comment(0x912B, 'X=2: zero 3 bytes (offsets 2,1,0)', align=Align.INLINE)
d.comment(0x912D, 'A=0: zero / BRK opcode', align=Align.INLINE)
d.comment(0x912F, 'Store zero at &0100+X', align=Align.INLINE)
d.comment(0x9132, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x9133, 'Loop until 3 bytes zeroed', align=Align.INLINE)
d.comment(0x9135, 'Release JSR protection mask', align=Align.INLINE)
d.comment(0x9138, 'Execute downloaded code at &0100', align=Align.INLINE)
d.comment(0x913B, 'Y=4: validation byte offset', align=Align.INLINE)
d.comment(0x913D, 'Load validation byte from RX data', align=Align.INLINE)
d.comment(0x913F, 'Zero: validation passed, continue', align=Align.INLINE)
d.comment(0x9141, 'Y=&80: source station offset', align=Align.INLINE)
d.comment(0x9143, 'Load source station from RX buffer', align=Align.INLINE)
d.comment(0x9145, 'Y=&0E: controlling station offset', align=Align.INLINE)
d.comment(0x9147, 'Compare with controlling station', align=Align.INLINE)
d.comment(0x9149, 'Mismatch: reject remote command', align=Align.INLINE)
d.comment(0x914B, 'Y=&82: character offset in RX data', align=Align.INLINE)
d.comment(0x914D, 'Load remote keypress character', align=Align.INLINE)
d.comment(0x914F, 'Transfer character to Y', align=Align.INLINE)
d.comment(0x9150, 'X=0: keyboard input buffer', align=Align.INLINE)
d.comment(0x9152, 'Release JSR protection before call', align=Align.INLINE)
d.comment(0x9155, 'A=&99: OSBYTE insert into buffer', align=Align.INLINE)
d.comment(0x96CD, 'Save interrupt state on stack', align=Align.INLINE)
d.comment(0x96CE, 'Enable interrupts during copy', align=Align.INLINE)
d.comment(0x96CF, 'Y=&20: copy 32 bytes', align=Align.INLINE)
d.comment(0x96D1, 'Load NMI shim byte from ROM', align=Align.INLINE)
d.comment(0x96D4, 'Store to NMI area at &0D00+Y', align=Align.INLINE)
d.comment(0x96D7, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x96D8, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x96DA, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x96DB, 'Return from shim installation', align=Align.INLINE)
d.comment(0x85B0, 'Y=dividend, A=100: hundreds digit', align=Align.INLINE)
d.comment(0x85B2, 'Print hundreds digit', align=Align.INLINE)
d.comment(0x85B5, 'A=10: tens divisor', align=Align.INLINE)
d.comment(0x85B7, 'Print tens digit', align=Align.INLINE)
d.comment(0x85BA, 'Transfer remainder to A', align=Align.INLINE)
d.comment(0x85BB, 'Convert to ASCII and print', align=Align.INLINE)
d.comment(0x860C, 'CR: pad rest of filename field', align=Align.INLINE)
d.comment(0x8610, 'Space: also ends filename', align=Align.INLINE)
d.comment(0x8616, 'Loop until all chars printed', align=Align.INLINE)
d.comment(0x861C, 'Pad to 12 chars wide', align=Align.INLINE)
d.comment(0x8622, 'Print load address as 2 hex bytes', align=Align.INLINE)
d.comment(0x8634, 'ALWAYS branch', align=Align.INLINE)
d.comment(0x8636, 'X=4: print 4 bytes for address', align=Align.INLINE)
d.comment(0x863F, 'Loop for remaining hex bytes', align=Align.INLINE)
d.comment(0x8695, 'Load FILEV function code from A', align=Align.INLINE)
d.comment(0x8CFD, 'Store Y (CSD handle) to &0E03', align=Align.INLINE)
d.comment(0x8D00, 'Jump to restore_args_return', align=Align.INLINE)
d.comment(0x81F9, 'Load local station number', align=Align.INLINE)
d.comment(0x81FC, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x81FF, 'A=&20: test bit 5 of SR2 (clock)', align=Align.INLINE)
d.comment(0x8201, 'Test ADLC SR2 for network clock', align=Align.INLINE)
d.comment(0x8204, 'Clock present: skip warning msg', align=Align.INLINE)
d.comment(0x84A5, 'Y += 5', align=Align.INLINE)
d.comment(0x8DF3, 'Jump to clear_svc_restore_args', align=Align.INLINE)
d.comment(0x8DF6, 'V always clear: branch to cleanup exit', align=Align.INLINE)
d.comment(0x8D85, 'X=&0E: OSWORD &10 parameter block size', align=Align.INLINE)
d.comment(0x8D87, 'Y=0: param block offset', align=Align.INLINE)
d.comment(0x8D89, 'A=&10: OSWORD &10 (open RXCB)', align=Align.INLINE)
d.comment(0x8D8B, 'Issue OSWORD &10 to open RXCB', align=Align.INLINE)
d.comment(0x8D8E, 'Load RXCB number from result', align=Align.INLINE)
d.comment(0x8D90, 'Zero: no free RXCB, skip', align=Align.INLINE)
d.comment(0x8D92, 'Store RXCB number in exec context', align=Align.INLINE)
d.comment(0x8D94, 'Y=&70: FS workspace offset', align=Align.INLINE)
d.comment(0x8D96, 'Load reply byte from workspace', align=Align.INLINE)
d.comment(0x8D98, 'Store to exec param area', align=Align.INLINE)
d.comment(0x8D9A, 'Advance to next param byte', align=Align.INLINE)
d.comment(0x8D9B, 'Compare against boundary', align=Align.INLINE)
d.comment(0x8D9D, 'Loop for all exec parameters', align=Align.INLINE)
d.comment(0x8D9F, 'Store final byte', align=Align.INLINE)
d.comment(0x8DA1, 'X=&16: OSBYTE param', align=Align.INLINE)
d.comment(0x8DA3, 'A=&C7: OSBYTE read/write flag', align=Align.INLINE)
d.comment(0x8DA5, 'Enable exec notification via OSBYTE', align=Align.INLINE)
d.comment(0x8DA8, 'A=4: Tube claim type (multi-byte transfer)', align=Align.INLINE)


d.label(0x8F49, 'clear_svc_restore_args')
d.subroutine(0x8F49, 'clear_svc_restore_args', title='Clear service number and restore OSWORD args', description="""Shared exit for OSWORD handlers. Zeros rom_svc_num to
release the service claim, then copies 3 bytes from
(net_rx_ptr) back to the fs_last_byte_flag area,
restoring the OSWORD argument state saved at entry.""")


d.label(0x9A19, 'store_rxcb_completion')
d.subroutine(0x9A19, 'store_rxcb_completion', title='Store RXCB completion fields from scout buffer', description="""Writes source network, source station, port, and control
byte from the scout buffer into the active RXCB. Sets
bit 7 of the control byte to mark reception complete.""")


d.label(0x9B12, 'check_imm_op_ctrl')
d.subroutine(0x9B12, 'check_imm_op_ctrl', title='Check control byte for immediate operation type', description="""Loads the RX control byte and compares against &82
(immediate HALT). If HALT, discards the frame via
imm_op_discard. Otherwise falls through to
imm_op_build_reply.""")

d.label(0x9A15, 'load_rxcb_buf_hi')

d.label(0x9B0D, 'tx_nmi_dispatch_page')

d.label(0x81CA, 'restore_y_return')

d.label(0x85CC, 'print_via_osasci')

d.label(0x85FF, 'print_hex_digit')

d.label(0x878D, 'set_star_reply_port')

d.label(0x8934, 'argsv_dispatch_a')

d.label(0x8C08, 'cat_init_display')

d.label(0x8D00, 'set_handle_return')

d.label(0x8DDB, 'clear_svc_return')

d.label(0x8EAD, 'set_carry_dispatch')

d.label(0x8EE2, 'carry_exit_or_read')

d.label(0x9005, 'jmp_clear_svc_restore')

d.label(0x85C3, 'decimal_divide_loop')

d.label(0x8608, 'print_filename_loop')

d.label(0x8C77, 'print_option_char')

d.label(0x8CB0, 'count_columns_loop')

d.label(0x8EB0, 'read_local_station')

d.label(0x912F, 'zero_0100_loop')

d.label(0x96D1, 'copy_nmi_shim_loop')

d.label(0x0445, 'tube_ctrl_write_2')

d.label(0x8410, 'find_cr_terminator')

d.label(0x8442, 'execute_brk_error')

d.label(0x849C, 'tx_flow_control')

d.label(0x84A1, 'tx_error_classify')

d.label(0x8553, 'filev_attrib_code_check')

d.label(0x86B4, 'tx_result_check')

d.label(0x88DF, 'argsv_zero_length')

d.label(0x89AA, 'gbpbv_func_dispatch')

d.label(0x8A74, 'findv_eof_check')

d.label(0x8BCD, 'cmd_match_retry')

d.label(0x8C4E, 'cat_access_setup')

d.label(0x8CBB, 'cat_examine_continue')

d.label(0x8D17, 'fsreply_handle_copy')

d.label(0x8DAD, 'net_handle_validate')

d.label(0x8E50, 'osword_12_subfunc')

d.label(0x8EDC, 'osword_12_error')

d.label(0x8EFF, 'post_reply_check')

d.label(0x8FF4, 'rx_first_packet')

d.label(0x920C, 'rx_imm_discard')

d.label(0x920F, 'rx_data_phase')

d.label(0x9A04, 'jmp_store_rxcb')

d.label(0x8001, 'lang_entry_lo')

d.label(0x8002, 'lang_entry_hi')

d.label(0x8004, 'svc_entry_lo')

d.label(0x0055, 'tube_dispatch_ptr_lo')

d.label(0x8445, 'sp_dot_string')

d.label(0x8BD8, 'cmd_table_entry_1')

d.label(0x8E7A, 'osword_12_ws_offsets')

d.label(0x9A16, 'rxcb_buf_hi_operand')

d.label(0x9B0E, 'tx_dispatch_page_operand')

d.label(0x9B13, 'rx_ctrl_operand')

d.label(0x9C5B, 'sr2_test_operand')

d.label(0x9ECA, 'tube_tx_byte2_operand')

d.label(0x9ED2, 'tube_tx_byte4_operand')

d.label(0x8EFE, 'scan_or_read_rxcb')
d.comment(0x8F49, 'Y=0: clear service claim', align=Align.INLINE)
d.comment(0x8F4B, 'Release ROM service number', align=Align.INLINE)
d.comment(0x8F4F, 'Load saved arg from (net_rx_ptr)+Y', align=Align.INLINE)
d.comment(0x8F51, 'Restore saved OSWORD argument byte', align=Align.INLINE)
d.comment(0x8F54, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8F55, 'Loop for bytes 2,1,0', align=Align.INLINE)
d.comment(0x8F57, 'Return to caller', align=Align.INLINE)
d.comment(0x9B12, 'Load RX control byte', align=Align.INLINE)
d.comment(0x9B15, 'Compare against &82 (HALT)', align=Align.INLINE)
d.comment(0x9B17, 'HALT: discard frame', align=Align.INLINE)
d.comment(0x8172, 'X=8: ROM offset for *ROFF match', align=Align.INLINE)
d.comment(0x8174, 'Match command against ROM string', align=Align.INLINE)
d.comment(0x8177, 'No match: try *NET command', align=Align.INLINE)
d.comment(0x8179, 'Match found: claim service (A=0)', align=Align.INLINE)
d.comment(0x81CA, 'Restore Y from temporary', align=Align.INLINE)
d.comment(0x9002, 'Poll TX until complete', align=Align.INLINE)
d.comment(0x8D07, 'Skip spaces before station number', align=Align.INLINE)
d.comment(0x8D0A, 'C=1: alphabetic, forward to FS', align=Align.INLINE)
d.comment(0x8D0C, 'A=0: default network (local)', align=Align.INLINE)
d.comment(0x8D11, 'C=0: no dot, single number only', align=Align.INLINE)
d.comment(0x9681, 'Copy NMI shim from ROM to &0D00', align=Align.INLINE)
d.comment(0x9684, 'Load current ROM bank number', align=Align.INLINE)
d.comment(0x9686, 'Patch ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x9689, 'A=&80: TX idle/complete status', align=Align.INLINE)
d.comment(0x8DCA, 'Load handle number from &F0', align=Align.INLINE)
d.comment(0x8DDB, 'A=0: clear service claim', align=Align.INLINE)
d.comment(0x8DDD, 'Release ROM service number', align=Align.INLINE)
d.comment(0x8DDF, 'Return to caller', align=Align.INLINE)
d.comment(0x969D, 'INTOFF: disable NMIs for state save', align=Align.INLINE)
d.comment(0x96A0, 'Y=8: RXCB offset for rx_status_flags', align=Align.INLINE)
d.comment(0x96A2, 'Load rx_status_flags', align=Align.INLINE)
d.comment(0x96A5, 'Store to RXCB offset 8', align=Align.INLINE)
d.comment(0x96A8, 'Load prot_status', align=Align.INLINE)
d.comment(0x96AB, 'Store to RXCB offset 9', align=Align.INLINE)
d.comment(0x96AE, 'Load TX in-progress flag', align=Align.INLINE)
d.comment(0x96B4, 'INTOFF: disable NMIs for state restore', align=Align.INLINE)
d.comment(0x96B7, 'Y=8: workspace offset for flags', align=Align.INLINE)
d.comment(0x96B9, 'Load saved rx_status_flags', align=Align.INLINE)
d.comment(0x96BB, 'Restore rx_status_flags', align=Align.INLINE)
d.comment(0x96BF, 'Load saved protection mask', align=Align.INLINE)
d.comment(0x96C1, 'Restore prot_status', align=Align.INLINE)
d.comment(0x96C5, 'Load saved tx_in_progress', align=Align.INLINE)
d.comment(0x96C7, 'Restore TX state', align=Align.INLINE)
d.comment(0x96CA, 'Reinitialise NMI workspace', align=Align.INLINE)
d.comment(0x8DE0, 'Load handle number from &F0', align=Align.INLINE)
d.comment(0x8279, 'Store RX buffer page pointer', align=Align.INLINE)
d.comment(0x827B, 'Advance to next page', align=Align.INLINE)
d.comment(0x827C, 'Store workspace page pointer', align=Align.INLINE)
d.comment(0x82A1, 'Y=2: printer server offset', align=Align.INLINE)
d.comment(0x82A3, 'A=&EB: default printer server', align=Align.INLINE)
d.comment(0x82A5, 'Store printer server at offset 2', align=Align.INLINE)
d.comment(0x82A8, 'A=0: clear remaining fields', align=Align.INLINE)
d.comment(0x82AA, 'Clear FS server network number', align=Align.INLINE)
d.comment(0x82AD, 'Clear workspace byte at offset 3', align=Align.INLINE)
d.comment(0x82AF, 'Clear protection status mask', align=Align.INLINE)
d.comment(0x82B2, 'Clear FS messages flag', align=Align.INLINE)
d.comment(0x82C7, 'Store station ID for TX scout', align=Align.INLINE)
d.comment(0x96B1, 'Store tx_in_progress to offset &0A', align=Align.INLINE)
d.comment(0x96B3, 'Return to caller', align=Align.INLINE)
d.comment(0x91B6, 'A=0: clear printer buffer state', align=Align.INLINE)
d.comment(0x821A, 'Load vector address from ROM table', align=Align.INLINE)
d.comment(0x8493, 'Bit 7 set: set EOF hint flag', align=Align.INLINE)
d.comment(0x8495, 'Load handle bitmask for flag op', align=Align.INLINE)
d.comment(0x8497, 'Clear EOF hint flag for this handle', align=Align.INLINE)
d.comment(0x849A, 'Flag cleared: load handle mask', align=Align.INLINE)
d.comment(0x849C, 'Load handle bitmask for flow control', align=Align.INLINE)
d.comment(0x849E, 'Set EOF hint flag for this handle', align=Align.INLINE)
d.comment(0x84A1, 'Load handle mask for return value', align=Align.INLINE)
d.comment(0x84A4, 'Return with handle mask in A', align=Align.INLINE)
d.comment(0x84A5, 'Y += 5 (entry point)', align=Align.INLINE)
d.comment(0x84A6, 'Y += 4', align=Align.INLINE)
d.comment(0x84A7, '(continued)', align=Align.INLINE)
d.comment(0x84A8, '(continued)', align=Align.INLINE)
d.comment(0x84A9, '(continued)', align=Align.INLINE)
d.comment(0x84AA, 'Return with Y adjusted', align=Align.INLINE)
d.comment(0x84AB, 'Y -= 4', align=Align.INLINE)
d.comment(0x84AC, 'Y -= 3', align=Align.INLINE)
d.comment(0x84AD, '(continued)', align=Align.INLINE)
d.comment(0x84AE, '(continued)', align=Align.INLINE)
d.comment(0x8BBE, 'CLC for pointer calculation', align=Align.INLINE)
d.comment(0x8BBF, 'A = chars consumed from input', align=Align.INLINE)
d.comment(0x8BC0, 'X = command text pointer high', align=Align.INLINE)
d.comment(0x8BC2, 'Add chars consumed to pointer low', align=Align.INLINE)
d.comment(0x8BC4, 'Store adjusted text pointer low', align=Align.INLINE)
d.comment(0x8BC7, 'Duplicate to second pointer copy', align=Align.INLINE)
d.comment(0x8BCA, 'No page overflow: skip INX', align=Align.INLINE)
d.comment(0x8BCC, 'Adjust high byte for page crossing', align=Align.INLINE)
d.comment(0x8BCD, 'Store high byte to context ptr 1', align=Align.INLINE)
d.comment(0x8BD0, 'Store high byte to context ptr 2', align=Align.INLINE)
d.comment(0x8BD3, 'Store high byte to context ptr 3', align=Align.INLINE)
d.comment(0x8BD6, 'Dispatch via PHA/PHA/RTS', align=Align.INLINE)
d.comment(0x9FEB, 'Load current TX flags', align=Align.INLINE)
d.comment(0x9FEE, 'Set bit 1 (transfer mode flag)', align=Align.INLINE)
d.comment(0x9FF0, 'Store updated TX flags', align=Align.INLINE)
d.comment(0x9FF3, 'SEC for subtraction', align=Align.INLINE)
d.comment(0x9FF4, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9FF5, 'Y=4: TXCB data start low offset', align=Align.INLINE)
d.comment(0x9FF7, 'Load data start low byte', align=Align.INLINE)
d.comment(0x9FF9, 'Y += 4: advance to data end low offset', align=Align.INLINE)
d.comment(0x9FFA, '(continued)', align=Align.INLINE)
d.comment(0x9FFB, '(continued)', align=Align.INLINE)
d.comment(0x9FFC, '(continued)', align=Align.INLINE)
d.comment(0x9FFD, 'Restore carry for subtraction', align=Align.INLINE)
d.comment(0x9FFE, 'Subtract buffer end from start', align=Align.INLINE)
d.comment(0x8BFE, 'X=&14 (20): column width for display', align=Align.INLINE)
d.comment(0x8C00, 'Store column width for batch calc', align=Align.INLINE)
d.comment(0x8C02, 'X=3: column count for examine request', align=Align.INLINE)
d.comment(0x8C04, 'Store column count', align=Align.INLINE)
d.comment(0x8C06, 'Y=0: initial entry start offset', align=Align.INLINE)
d.comment(0x8C08, 'A=6: examine format type in command', align=Align.INLINE)
d.comment(0x8C0A, 'Store format type at &0F05', align=Align.INLINE)
d.comment(0x8C0D, 'Skip spaces in dir name argument', align=Align.INLINE)
d.comment(0x8C10, 'Save parameter offset after spaces', align=Align.INLINE)
d.comment(0x8C2F, 'X=5: space padding count', align=Align.INLINE)
d.comment(0x8C31, 'Print 5 spaces for alignment', align=Align.INLINE)
d.comment(0x8C34, 'Access: 0=Owner, non-zero=Public', align=Align.INLINE)
d.comment(0x8C42, 'Always taken (high-bit term. str)', align=Align.INLINE)
d.comment(0x8C59, 'X=4: space padding count', align=Align.INLINE)
d.comment(0x8C5B, 'Print 4 spaces for alignment', align=Align.INLINE)
d.comment(0x8C5E, "Print 'Option ' label", align=Align.INLINE)
d.comment(0x8C68, 'Load boot option from workspace', align=Align.INLINE)
d.comment(0x8C74, 'Load string offset for option name', align=Align.INLINE)
d.comment(0x8C77, 'Load char from option name string', align=Align.INLINE)
d.comment(0x8C7A, 'Zero terminator: name complete', align=Align.INLINE)
d.comment(0x8C8C, 'X=&11: CSD name offset in reply', align=Align.INLINE)
d.comment(0x8C8E, 'Print current directory name', align=Align.INLINE)
d.comment(0x8C91, 'X=5: space padding count', align=Align.INLINE)
d.comment(0x8C93, 'Print 5 spaces for alignment', align=Align.INLINE)
d.comment(0x8C96, "Print 'Lib. ' label", align=Align.INLINE)
d.comment(0x8C9E, 'X=&1B: library name offset in reply', align=Align.INLINE)
d.comment(0x8CA8, 'Y=0: initial examine start position', align=Align.INLINE)
d.comment(0x8CAD, 'A = reply buffer bytes consumed', align=Align.INLINE)
d.comment(0x8CAE, 'Complement for divide-by-subtraction', align=Align.INLINE)
d.comment(0x8CB0, 'SEC for subtraction', align=Align.INLINE)
d.comment(0x8CB1, 'Subtract one column width (20)', align=Align.INLINE)
d.comment(0x8CB3, 'Count another entry that fits', align=Align.INLINE)
d.comment(0x8CB4, 'Loop while space remains', align=Align.INLINE)
d.comment(0x8CB6, 'Store entries per examine batch', align=Align.INLINE)
d.comment(0x8CB9, 'Save batch size for loop reset', align=Align.INLINE)
d.comment(0x8CBB, 'Reload dir name offset for examine', align=Align.INLINE)
d.comment(0x8CE8, "Fallthrough (also boot string 'L.!')", align=Align.INLINE)
d.comment(0x051C, 'Save character for WRCH echo', align=Align.INLINE)
d.comment(0x053D, 'Restore saved X', align=Align.INLINE)
d.comment(0x0543, 'Read file handle from R2', align=Align.INLINE)
d.comment(0x0550, 'Read file handle from R2', align=Align.INLINE)
d.comment(0x0569, 'Read open mode from R2', align=Align.INLINE)
d.comment(0x058C, 'Read file handle from R2', align=Align.INLINE)
d.comment(0x05C5, 'Read command string into &0700', align=Align.INLINE)
d.comment(0x05D8, 'X=&10: read 16-byte control block', align=Align.INLINE)
d.comment(0x0602, 'X=&0C: read 13-byte param block', align=Align.INLINE)
d.comment(0x0615, 'Encode carry into result bit 7', align=Align.INLINE)
d.comment(0x0616, 'Send carry+result byte via R2', align=Align.INLINE)
d.comment(0x0626, 'Read X parameter from R2', align=Align.INLINE)
d.comment(0x063B, 'Read X parameter from R2', align=Align.INLINE)
d.comment(0x065D, 'Read OSWORD number from R2', align=Align.INLINE)
d.comment(0x06A3, 'X=4: read 5-byte RDLN ctrl block', align=Align.INLINE)
d.comment(0x8601, 'Check if file info available', align=Align.INLINE)
d.comment(0x8604, 'No info available: return', align=Align.INLINE)
d.comment(0x8606, 'Y=0: start of filename string', align=Align.INLINE)
d.comment(0x8608, 'Load filename character', align=Align.INLINE)
d.comment(0x860A, 'CR: end of filename', align=Align.INLINE)
d.comment(0x860E, 'Also end name on space character', align=Align.INLINE)
d.comment(0x8615, 'Advance to next filename byte', align=Align.INLINE)
d.comment(0x8618, 'Print padding space', align=Align.INLINE)
d.comment(0x861B, 'Advance past filename position', align=Align.INLINE)
d.comment(0x861E, 'Continue padding if < 12 chars', align=Align.INLINE)
d.comment(0x8620, 'Y=5: high byte of load address', align=Align.INLINE)
d.comment(0x8622, 'Print load address as 2 hex bytes', align=Align.INLINE)
d.comment(0x8625, 'Print exec address and length', align=Align.INLINE)
d.comment(0x862B, 'Y=9: exec address offset', align=Align.INLINE)
d.comment(0x862D, 'Print exec address bytes', align=Align.INLINE)
d.comment(0x8630, 'Y=&0C: file length offset', align=Align.INLINE)
d.comment(0x8632, 'X=3: print 3 bytes for file length', align=Align.INLINE)
d.comment(0x8638, 'Load address/length byte', align=Align.INLINE)
d.comment(0x863A, 'Print as 2 hex digits', align=Align.INLINE)
d.comment(0x863D, 'Move to next lower address byte', align=Align.INLINE)
d.comment(0x863E, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8641, 'A=space: separator character', align=Align.INLINE)
d.comment(0x864B, 'Set TX pointer hi byte to page 0', align=Align.INLINE)
d.comment(0x8E7C, 'Sub-function >= 6? (handle ops)', align=Align.INLINE)
d.comment(0x8E7E, 'Sub >= 6: handle/station/error', align=Align.INLINE)
d.comment(0x8E80, 'Sub-function >= 4? (protection)', align=Align.INLINE)
d.comment(0x8E97, 'Copy station bytes to/from workspace', align=Align.INLINE)
d.comment(0x8E9A, 'Always taken (Y=2 after copy)', align=Align.INLINE)
d.comment(0x8EAD, 'SEC: set carry for exit', align=Align.INLINE)
d.comment(0x8EB0, 'Load local station number', align=Align.INLINE)
d.comment(0x8EB3, 'Y=1: param block offset for result', align=Align.INLINE)
d.comment(0x8EB4, 'Return station number to caller', align=Align.INLINE)
d.comment(0x8EB6, 'Always taken (C set above)', align=Align.INLINE)
d.comment(0x8EDC, 'Y=1: param block offset for error', align=Align.INLINE)
d.comment(0x8EDD, 'Load last FS error number', align=Align.INLINE)
d.comment(0x8EE0, 'Return error code to caller', align=Align.INLINE)
d.comment(0x8EE2, 'Exit with carry set', align=Align.INLINE)
d.comment(0x91ED, 'Load current buffer offset', align=Align.INLINE)
d.comment(0x91F7, 'Decrement transfer count low byte', align=Align.INLINE)
d.comment(0x91FA, 'XOR with transfer count flags', align=Align.INLINE)
d.comment(0x91FD, 'Shift bit 0 into carry', align=Align.INLINE)
d.comment(0x91FE, 'Data phase active: continue', align=Align.INLINE)
d.comment(0x9200, 'Load transfer count flags', align=Align.INLINE)
d.comment(0x9203, 'Shift bit 0 into carry', align=Align.INLINE)
d.comment(0x9206, 'Rotate carry back', align=Align.INLINE)
d.comment(0x9207, 'Mask off control bits', align=Align.INLINE)
d.comment(0x9209, 'Store updated flags', align=Align.INLINE)
d.comment(0x9204, 'Bit 0=0 (active): just flush', align=Align.INLINE)
d.comment(0x920C, 'Flush accumulated output to network', align=Align.INLINE)
d.comment(0x920F, 'Save PFLAGS bit 0 via carry', align=Align.INLINE)
d.comment(0x9212, 'Restore original reason code', align=Align.INLINE)
d.comment(0x9213, 'Old PFLAGS bit 0 to A bit 7', align=Align.INLINE)
d.comment(0x9214, 'Reason bit 0 into PFLAGS bit 0', align=Align.INLINE)
d.comment(0x83CF, 'Load handle bitmask for BPUT/BGET', align=Align.INLINE)
d.comment(0x83EE, 'Convert SPOOL handle to bitmask', align=Align.INLINE)
d.comment(0x83F1, 'Compare SPOOL mask with file mask', align=Align.INLINE)
d.comment(0x83F3, 'Not SPOOL file: dispatch FS error', align=Align.INLINE)
d.comment(0x83F5, "Load '*SP.' command string low", align=Align.INLINE)
d.comment(0x845B, 'Load TX flag byte from ctrl block', align=Align.INLINE)
d.comment(0x845D, 'Bit 7 set: TX complete, clean up', align=Align.INLINE)
d.comment(0x845F, 'Check for Escape during TX wait', align=Align.INLINE)
d.comment(0x86A2, 'Y=1: offset past filename pointer', align=Align.INLINE)
d.comment(0x86A3, 'X=&FF: parse all characters', align=Align.INLINE)
d.comment(0x86A5, 'C=0: normal string parse entry', align=Align.INLINE)
d.comment(0x86A6, 'Init string parsing via GSINIT', align=Align.INLINE)
d.comment(0x8979, 'A = handle bitmask from set_fs_flag', align=Align.INLINE)
d.comment(0x897A, 'Merge handle into sequence tracking', align=Align.INLINE)
d.comment(0x897D, 'Store updated sequence tracking', align=Align.INLINE)
d.comment(0x89AA, 'X=1? (*OPT 1: set messaging)', align=Align.INLINE)
d.comment(0x89AC, 'Not *OPT 1: bad option error', align=Align.INLINE)
d.comment(0x89AE, 'Y < 2? (valid: 0=off, 1=on)', align=Align.INLINE)
d.comment(0x89B0, 'Y >= 2: bad option value error', align=Align.INLINE)
d.comment(0x8DA6, 'Y=&0F: workspace offset for params', align=Align.INLINE)
d.comment(0x8DAA, 'Claim Tube for address transfer', align=Align.INLINE)
d.comment(0x8DAD, 'Execute at load address', align=Align.INLINE)
d.comment(0x8E4A, 'Set up and start low-level transmit', align=Align.INLINE)
d.comment(0x8E4D, 'Exit: release service claim', align=Align.INLINE)
d.comment(0x8E50, 'SEC: alternate entry for OSWORD &11', align=Align.INLINE)
d.comment(0x8E51, 'A = param block high for branch', align=Align.INLINE)
d.comment(0x8E66, 'Reset JSR protection status', align=Align.INLINE)
d.comment(0x8E69, 'Branch to set carry and dispatch', align=Align.INLINE)
d.comment(0x8E78, 'Always taken (SEC set above)', align=Align.INLINE)
d.comment(0x90CE, 'Y=&0E: 14-byte parameter block', align=Align.INLINE)
d.comment(0x90D0, 'OSWORD 7? (make sound)', align=Align.INLINE)
d.comment(0x90F9, 'Set up control block for reply', align=Align.INLINE)
d.comment(0x90FC, 'Return from remote command handler', align=Align.INLINE)
d.comment(0x90FD, 'Y=4: RX control block byte 4', align=Align.INLINE)
d.comment(0x90FF, 'Load first data byte from RX', align=Align.INLINE)
d.comment(0x9101, 'Zero: standard boot, skip code', align=Align.INLINE)
d.comment(0x9103, 'Load language ROM number', align=Align.INLINE)
d.comment(0x9106, 'OR with 9: set remote boot bits', align=Align.INLINE)
d.comment(0x9108, 'Store modified control byte', align=Align.INLINE)
d.comment(0x910A, 'X=&80: exec address offset lo', align=Align.INLINE)
d.comment(0x910C, 'Y=&80: exec address offset hi', align=Align.INLINE)
d.comment(0x910E, 'Load exec address low byte', align=Align.INLINE)
d.comment(0x9112, 'Load exec address high byte', align=Align.INLINE)
d.comment(0x9114, 'Y=&0F: workspace offset for hi', align=Align.INLINE)
d.comment(0x911A, 'Copy command to &0100 area', align=Align.INLINE)
d.comment(0x911C, 'Initialize OSBYTE vectors', align=Align.INLINE)
d.comment(0x911F, 'Set up control block for boot', align=Align.INLINE)
d.comment(0x9122, 'X=1: enable parameter', align=Align.INLINE)
d.comment(0x9110, 'Save boot type on stack', align=Align.INLINE)
d.comment(0x9116, 'Store filename offset at ws+&0F', align=Align.INLINE)
d.comment(0x9119, 'Restore boot type from stack', align=Align.INLINE)
d.comment(0x9124, 'Y=0: second argument for OSBYTE', align=Align.INLINE)
d.comment(0x9126, 'A=&C9: disable keyboard for boot', align=Align.INLINE)
d.comment(0x04EF, 'Restore saved Y register', align=Align.INLINE)
d.comment(0x8449, 'A=&2A: error ptr for FS retry', align=Align.INLINE)
d.comment(0x8171, 'Return from workspace reset', align=Align.INLINE)
d.comment(0x878D, 'A=&2A: error ptr for FS retry', align=Align.INLINE)
d.comment(0x878F, 'Store error ptr for TX poll', align=Align.INLINE)
d.comment(0x8821, 'Save handle for EOF check', align=Align.INLINE)
d.comment(0x88BA, 'Load FS command code from reply', align=Align.INLINE)
d.comment(0x88BD, 'Zero: no attribute data returned', align=Align.INLINE)
d.comment(0x88DC, 'Reload FS command code', align=Align.INLINE)
d.comment(0x88DF, 'A = command code for exit test', align=Align.INLINE)
d.comment(0x8A74, 'A=&2A: error ptr for FS retry', align=Align.INLINE)
d.comment(0x8A76, 'Store error ptr for TX poll', align=Align.INLINE)
d.comment(0x8FF4, 'First packet: exit handler', align=Align.INLINE)
d.comment(0x91EB, 'Flush done: continue loop', align=Align.INLINE)
d.comment(0x9F5D, 'Load TX block byte at offset 6', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'nfs-3.34B.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'nfs-3.34B.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
