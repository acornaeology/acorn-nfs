import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'nfs-3.40.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='6502', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.add_move(0x0016, 0x931C, 0x61)
d.add_move(0x0400, 0x935D, 0xF9)
d.add_move(0x0500, 0x9456, 0x100)
d.add_move(0x0600, 0x9556, 0x100)
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
d.hook_subroutine(0x8605, 'print_inline', stringhi_hook)
d.constant(20, 'osbyte_explode_chars')
d.constant(120, 'osbyte_write_keys_pressed')
d.constant(143, 'osbyte_issue_service_request')
d.constant(168, 'osbyte_read_rom_ptr_table_low')

d.label(0x0097, 'escapable')

d.label(0x0098, 'need_release_tube')

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

d.label(0x00B0, 'fs_load_addr')

d.label(0x00B1, 'fs_load_addr_hi')

d.label(0x00B2, 'fs_load_addr_2')

d.label(0x00B8, 'fs_error_ptr')

d.label(0x00BB, 'fs_options')

d.label(0x00BC, 'fs_block_offset')

d.label(0x00BD, 'fs_last_byte_flag')

d.label(0x00BE, 'fs_crc_lo')

d.label(0x00BF, 'fs_crc_hi')

d.label(0x00CD, 'nfs_temp')

d.label(0x00CE, 'rom_svc_num')

d.label(0x0010, 'zp_temp_10')

d.label(0x0011, 'zp_temp_11')

d.label(0x0016, 'nmi_workspace_start')

d.label(0x005F, 'zp_63')

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

d.label(0x0036, 'tube_main_loop')

d.label(0x003B, 'tube_handle_wrch')

d.label(0x0041, 'tube_poll_r2')

d.label(0x0050, 'tube_dispatch_cmd')

d.label(0x0053, 'tube_transfer_addr')
d.entry(0x0016)
d.entry(0x0032)
d.entry(0x0036)

d.label(0x0403, 'tube_escape_entry')

d.label(0x0406, 'tube_addr_claim')

d.label(0x041E, 'tube_post_init')

d.label(0x042F, 'return_tube_init')

d.label(0x047C, 'return_tube_xfer')
d.entry(0x0400)
d.entry(0x0403)
d.entry(0x0406)
d.entry(0x041E)

d.label(0x0527, 'tube_poll_r1_wrch')

d.label(0x0520, 'tube_osbput')

d.label(0x052D, 'tube_osbget')

d.label(0x0537, 'tube_osrdch')

d.label(0x053A, 'tube_rdch_reply')

d.label(0x0542, 'tube_osfind')

d.label(0x0552, 'tube_osfind_close')

d.label(0x055E, 'tube_osargs')

d.label(0x0562, 'tube_read_params')

d.label(0x0582, 'tube_read_string')

d.label(0x0596, 'tube_oscli')

d.label(0x059C, 'tube_reply_ack')

d.label(0x059E, 'tube_reply_byte')

d.label(0x05A9, 'tube_osfile')

d.label(0x05D1, 'tube_osgbpb')

d.label(0x05F2, 'tube_osbyte_2param')
for addr in [0x0537, 0x0596, 0x0626, 0x0607, 0x0627, 0x0668, 0x04EF, 0x0602, 0x0520, 0x052D, 0x0542, 0x055E, 0x05A9, 0x05F2]:
    d.entry(addr)
_tube_r2_entries = [(0x0500, 'tube_osrdch', 'R2 cmd 0: OSRDCH'), (0x0502, 'tube_oscli', 'R2 cmd 1: OSCLI'), (0x0504, 'tube_osbyte_2param', 'R2 cmd 2: OSBYTE (2-param)'), (0x0506, 'tube_osbyte_long', 'R2 cmd 3: OSBYTE (3-param)'), (0x0508, 'tube_osword', 'R2 cmd 4: OSWORD'), (0x050A, 'tube_osword_rdln', 'R2 cmd 5: OSWORD 0 (read line)'), (0x050C, 'tube_osargs', 'R2 cmd 6: OSARGS'), (0x050E, 'tube_osbget', 'R2 cmd 7: OSBGET'), (0x0510, 'tube_osbput', 'R2 cmd 8: OSBPUT'), (0x0512, 'tube_osfind', 'R2 cmd 9: OSFIND'), (0x0514, 'tube_osfile', 'R2 cmd 10: OSFILE'), (0x0516, 'tube_osgbpb', 'R2 cmd 11: OSGBPB')]
for addr, target_label, desc in _tube_r2_entries:
    d.word(addr)
    d.expr(addr, target_label)
    d.comment(addr, desc, align=Align.INLINE)
d.comment(0x0615, 'Test for OSBYTE &9D (fast Tube BPUT)', align=Align.INLINE)

d.label(0x0626, 'tube_osbyte_short')

d.label(0x0630, 'tube_osbyte_send_x')

d.label(0x0607, 'tube_osbyte_long')

d.label(0x061D, 'tube_osbyte_send_y')

d.label(0x062B, 'tube_osword_read')

d.label(0x0636, 'tube_osword_read_lp')

d.label(0x0657, 'tube_osword_write')

d.label(0x065A, 'tube_osword_write_lp')

d.label(0x0665, 'tube_return_main')

d.label(0x0668, 'tube_osword_rdln')

d.label(0x0680, 'tube_rdln_send_line')

d.label(0x0687, 'tube_rdln_send_loop')

d.label(0x068A, 'tube_rdln_send_byte')

d.label(0x06A7, 'tube_escape_check')

d.label(0x06AD, 'tube_event_handler')

d.label(0x06BC, 'tube_send_r1')
d.entry(0x0600)
d.entry(0x0626)
d.entry(0x0607)
d.entry(0x0627)
d.entry(0x0668)
d.entry(0x06A7)
d.entry(0x06AD)
d.entry(0x06BC)

d.label(0x0DEB, 'fs_state_deb')
d.comment(0x8011, """The 'ROFF' suffix at &8014 is reused by the *ROFF
command matcher (svc_star_command) — a space-saving
trick that shares ROM bytes between the copyright
string and the star command table.""")

d.label(0x8011, 'copyright_string')

d.label(0x8018, 'error_offsets')

d.label(0x8025, 'dispatch_0_lo')

d.label(0x804A, 'dispatch_0_hi')
d.expr_label(0x8024, 'dispatch_0_lo-1')
d.expr_label(0x8049, 'dispatch_0_hi-1')

d.label(0x8E9F, 'fs_osword_tbl_lo')

d.label(0x8EB5, 'fs_osword_tbl_hi')

d.label(0x8EE9, 'read_args_size')

d.label(0x8FDE, 'store_16bit_at_y')

d.label(0x908F, 'osword_trampoline')

d.label(0x909A, 'osword_tbl_lo')

d.label(0x90A1, 'osword_tbl_hi')

d.label(0x9130, 'match_osbyte_code')

d.label(0x9138, 'return_match_osbyte')

d.label(0x8499, 'return_remote_cmd')

d.label(0x84A0, 'rchex')

d.label(0x9180, 'ctrl_block_setup_clv')

d.label(0x92EB, 'clear_jsr_protection')

d.label(0x9303, 'read_vdu_osbyte_x0')

d.label(0x9305, 'read_vdu_osbyte')

d.label(0x0695, 'tube_send_r2')

d.label(0x069E, 'tube_send_r4')


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


d.subroutine(0x0582, 'tube_read_string', title='Read string from Tube R2 into buffer', description="""Loops reading bytes from tube_read_r2 into the
string buffer at &0700, storing at string_buf+Y.
Terminates on CR (&0D) or when Y wraps to zero
(256-byte overflow). Returns with X=0, Y=7 so that
XY = &0700, ready for OSCLI or OSFIND dispatch.
Called by the Tube OSCLI and OSFIND handlers.""")


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


d.subroutine(0x0695, 'tube_send_r2', title='Send byte to Tube data register R2', description="""Polls Tube status register 2 until bit 6 (TDRA)
is set, then writes A to the data register. Uses a
tight BIT/BVC polling loop. Called by 12 sites
across the Tube host code for all R2 data
transmission: command responses, file data, OSBYTE
results, and control block bytes.""")


d.subroutine(0x069E, 'tube_send_r4', title='Send byte to Tube data register R4', description="""Polls Tube status register 4 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R4 is the command/control
channel used for address claims (ADRR), data transfer
setup (SENDW), and release commands. Called by 7
sites, primarily during tube_release_claim and
tube_transfer_setup sequences.""")


d.subroutine(0x06BC, 'tube_send_r1', title='Send byte to Tube data register R1', description="""Polls Tube status register 1 until bit 6 is set,
then writes A to the data register. Uses a tight
BIT/BVC polling loop. R1 is used for asynchronous
event and escape notification to the co-processor.
Called by tube_event_handler to forward event type,
Y, and X parameters, and reached via BMI from
tube_escape_check when the escape flag is set.""")


d.subroutine(0x06C5, 'tube_read_r2', title='Read a byte from Tube data register R2', description="""Polls Tube status register 2 until data is available
(bit 7 set), then loads A from Tube data register 2.
Called by all Tube dispatch handlers that receive data
or parameters from the co-processor.""")

d.label(0x80F6, 'return_1')

d.label(0x81AB, 'return_2')

d.label(0x82BE, 'return_3')

d.label(0x8578, 'return_4')

d.label(0x8D84, 'return_5')

d.label(0x8E58, 'return_6')

d.label(0x8EAF, 'return_7')

d.label(0x9066, 'return_8')

d.label(0x8D07, 'return_9')

d.label(0x99E7, 'return_10')

d.label(0x81B1, 'svc_4_star_command')

d.label(0x9660, 'trampoline_tx_setup')

d.label(0x9663, 'trampoline_adlc_init')

d.label(0x9666, 'svc_12_nmi_release')

d.label(0x9669, 'svc_11_nmi_claim')

d.label(0x966C, 'svc_5_unknown_irq')
d.entry(0x9660)
d.entry(0x9663)

d.label(0x855C, 'bgetv_handler')

d.label(0x840F, 'bputv_handler')
d.entry(0x855C)
d.entry(0x840F)
d.entry(0x86D7)
d.entry(0x8705)

d.label(0x81DD, 'cmd_name_matched')

d.label(0x8335, 'store_rom_ptr_pair')

d.label(0x83C4, 'init_tx_ctrl_data')

d.label(0x8385, 'init_tx_ctrl_port')

d.label(0x83B9, 'prepare_cmd_clv')

d.label(0x83C4, 'prepare_fs_cmd_v')

d.label(0x83EF, 'send_fs_reply_cmd')

d.label(0x843A, 'store_retry_count')

d.label(0x8491, 'update_sequence_return')

d.label(0x84FF, 'set_listen_offset')

d.label(0x851B, 'send_to_fs_star')

d.label(0x8543, 'fs_wait_cleanup')

d.label(0x87FC, 'add_5_to_y')

d.label(0x87FD, 'add_4_to_y')

d.label(0x880F, 'sub_4_from_y')

d.label(0x8810, 'sub_3_from_y')

d.label(0x81CE, 'clear_osbyte_ce_cf')

d.label(0x0F00, 'fs_cmd_type')

d.label(0x0F01, 'fs_cmd_y_param')

d.label(0x0F02, 'fs_cmd_urd')

d.label(0x0F03, 'fs_cmd_csd')

d.label(0x0F04, 'fs_cmd_lib')

d.label(0x0F05, 'fs_cmd_data')

d.label(0x0FDC, 'fs_putb_buf')

d.label(0x0FDD, 'fs_getb_buf')

d.label(0x85FA, 'access_bit_table')

d.label(0x8673, 'return_compare')

d.label(0x8674, 'fscv_7_read_handles')

d.label(0x8678, 'return_fscv_handles')

d.label(0x8683, 'store_fs_flag')

d.label(0x8D45, 'pad_filename_spaces')

d.label(0x8D58, 'print_exec_and_len')

d.label(0x8D63, 'print_hex_bytes')

d.label(0x8D6E, 'print_space')

d.label(0x8691, 'tx_poll_timeout')

d.label(0x88B7, 'get_file_protection')

d.label(0x88CC, 'copy_filename_to_cmd')

d.label(0x8909, 'copy_fs_reply_to_cb')

d.label(0x8955, 'save_args_handle')

d.label(0x89D6, 'close_single_handle')

d.label(0x8A0E, 'adjust_addrs_9')

d.label(0x8A13, 'adjust_addrs_1')

d.label(0x8A15, 'adjust_addrs_clc')

d.label(0x8B3B, 'copy_reply_to_caller')

d.label(0x8BCF, 'tube_claim_loop')

d.label(0x8CFB, 'print_reply_bytes')

d.label(0x8CFD, 'print_reply_counted')

d.label(0x8D79, 'copy_string_from_offset')

d.label(0x971F, 'scout_reject')

d.label(0x9740, 'scout_discard')

d.label(0x9748, 'scout_loop_rda')

d.label(0x9758, 'scout_loop_second')

d.label(0x9793, 'scout_no_match')

d.label(0x9796, 'scout_match_port')

d.label(0x9815, 'data_rx_setup')

d.label(0x9837, 'nmi_data_rx_net')

d.label(0x984D, 'nmi_data_rx_skip')

d.label(0x987A, 'rx_error')

d.label(0x987A, 'rx_error_reset')

d.label(0x98DD, 'nmi_data_rx_tube')

d.label(0x9919, 'data_rx_tube_complete')

d.label(0x9916, 'data_rx_tube_error')

d.label(0x994F, 'ack_tx_configure')

d.label(0x995D, 'ack_tx_write_dest')

d.label(0x9C6B, 'tx_active_start')

d.label(0x9D53, 'tx_error')

d.label(0x9E1A, 'data_tx_begin')

d.label(0x9E5C, 'data_tx_last')

d.label(0x9E6D, 'data_tx_error')

d.label(0x9E78, 'install_saved_handler')

d.label(0x9E81, 'nmi_data_tx_tube')

d.label(0x9EDC, 'nmi_final_ack_net')

d.label(0x9FA7, 'nmi_shim_rom_src')

d.label(0x0586, 'strnh')

d.label(0x05A6, 'mj')

d.label(0x05AB, 'argsw')

d.label(0x0604, 'bytex')

d.label(0x815B, 'cloop')

d.label(0x81F8, 'initl')

d.label(0x81E3, 'skpspi')

d.label(0x824C, 'dofsl1')

d.label(0x834F, 'fsdiel')

d.label(0x8394, 'fstxl1')

d.label(0x83A4, 'fstxl2')

d.label(0x83F7, 'dofsl7')

d.label(0x8403, 'return_dofsl7')

d.label(0x8404, 'dofsl5')

d.label(0x844B, 'error1')

d.label(0x84FB, 'nlistn')

d.label(0x84FD, 'nlisne')

d.label(0x8530, 'incpx')

d.label(0x864D, 'y2fsl5')

d.label(0x8653, 'y2fsl2')

d.label(0x8662, 'fs2al1')

d.label(0x8D65, 'num01')

d.label(0x86AD, 'l4')

d.label(0x86D9, 'file1')

d.label(0x86EB, 'quote1')

d.label(0x8716, 'loadop')

d.label(0x8731, 'lodfil')

d.label(0x8754, 'floop')

d.label(0x877E, 'lodchk')

d.label(0x8789, 'return_lodchk')

d.label(0x878A, 'saveop')

d.label(0x8793, 'savsiz')

d.label(0x87F2, 'lodrl1')

d.label(0x8805, 'lodrl2')

d.label(0x8837, 'savchk')

d.label(0x88AA, 'chalp1')

d.label(0x88C1, 'chalp2')

d.label(0x88D3, 'cha6')

d.label(0x88E2, 'cha4')

d.label(0x88EC, 'cha5')

d.label(0x8916, 'cha5lp')

d.label(0x8984, 'osarg1')

d.label(0x89FA, 'opter1')

d.label(0x89FF, 'optl1')

d.label(0x8A27, 'gbpbx')

d.label(0x8A5E, 'gbpbx0')

d.label(0x8A3C, 'gbpbx1')

d.label(0x8A47, 'gbpbe1')

d.label(0x8A53, 'gbpbf1')

d.label(0x8A5E, 'gbpbf2')

d.label(0x8A67, 'gbpbl1')

d.label(0x8A89, 'gbpbl3')

d.label(0x8AA0, 'gbpbf3')

d.label(0x8AFD, 'info2')

d.label(0x8B62, 'tbcop1')

d.label(0x8BE0, 'decfir')

d.label(0x8BE2, 'decmor')

d.label(0x8BEE, 'decmin')

d.label(0x8E2F, 'logon2')

d.label(0x8F22, 'logon3')

d.label(0x8D8B, 'print_dir_from_offset')

d.label(0x8D75, 'infol2')

d.label(0x8E6A, 'rxpol2')

d.label(0x8EA2, 'save1')

d.label(0x8EB3, 'copyl3')

d.label(0x8EF4, 'readry')

d.label(0x8F23, 'rssl1')

d.label(0x8F2E, 'rssl2')

d.label(0x8F3E, 'rsl1')

d.label(0x8F68, 'readc1')

d.label(0x8F85, 'scan0')

d.label(0x8F99, 'scan1')

d.label(0x8FB5, 'openl6')

d.label(0x8FC2, 'openl7')

d.label(0x8FC7, 'openl4')

d.label(0x8FEE, 'dofs01')

d.label(0x9067, 'dofs2')

d.label(0x9088, 'entry1')

d.label(0x9100, 'nbyte6')

d.label(0x9102, 'nbyte1')

d.label(0x9124, 'nbyte4')

d.label(0x9128, 'nbyte5')

d.label(0x912F, 'return_nbyte')

d.label(0x84A3, 'remot1')

d.label(0x9181, 'cbset2')

d.label(0x9198, 'cbset3')

d.label(0x919E, 'cbset4')

d.label(0x91DB, 'setup1')

d.label(0x91DE, 'return_printer_select')

d.label(0x91EE, 'prlp1')

d.label(0x926D, 'bsxl1')

d.label(0x928A, 'bspsx')

d.label(0x9292, 'bsxl0')

d.label(0x92A5, 'return_bspsx')
d.comment(0x8000, """NFS ROM 3.40 disassembly (Acorn Econet filing system)
====================================================""")
d.comment(0x8000, 'JMP language_handler', align=Align.INLINE)
d.comment(0x8003, 'JMP service_handler', align=Align.INLINE)
d.comment(0x8018, """Error message offset table (9 entries).
Each byte is a Y offset into error_msg_table.
Entry 0 (Y=0, "Line Jammed") doubles as the
copyright string null terminator.
Indexed by TXCB status (AND #7), or hardcoded 8.""")
d.comment(0x8018, '"Line Jammed"', align=Align.INLINE)
for addr in range(0x8019, 0x8021):
    d.byte(addr)
d.comment(0x8019, '"Net Error"', align=Align.INLINE)
d.comment(0x801A, '"Not listening"', align=Align.INLINE)
d.comment(0x801B, '"No Clock"', align=Align.INLINE)
d.comment(0x801C, '"Escape"', align=Align.INLINE)
d.comment(0x801D, '"Escape"', align=Align.INLINE)
d.comment(0x801E, '"Escape"', align=Align.INLINE)
d.comment(0x801F, '"Bad Option"', align=Align.INLINE)
d.comment(0x8020, '"No reply"', align=Align.INLINE)
d.comment(0x8021, 'Four bytes with unknown purpose.')
for addr in range(0x8021, 0x8025):
    d.byte(addr)
d.comment(0x8021, 'Purpose unknown', align=Align.INLINE)
d.comment(0x8022, 'Purpose unknown', align=Align.INLINE)
d.comment(0x8023, 'Purpose unknown', align=Align.INLINE)
d.comment(0x8024, 'Purpose unknown', align=Align.INLINE)
for i in range(0, 14):
    d.rts_code_ptr(0x8025 + i, 0x804A + i)
for i in range(14, 19):
    d.rts_code_ptr(0x8025 + i, 0x804A + i)
for i in range(19, 27):
    d.rts_code_ptr(0x8025 + i, 0x804A + i)
for i in range(27, 31):
    d.rts_code_ptr(0x8025 + i, 0x804A + i)
for i in range(31, 37):
    d.rts_code_ptr(0x8025 + i, 0x804A + i)
for i in range(5):
    d.rts_code_ptr(0x8EB0 + i, 0x8EB5 + i)
d.entry(0x96EC)
d.entry(0x96F2)
d.entry(0x9C2F)
d.entry(0x9D2D)
d.entry(0x9D53)
d.entry(0x9D69)
d.entry(0x9D75)
d.entry(0x9D93)
d.entry(0x9DA9)
d.entry(0x9DC2)
d.entry(0x9EBA)
d.entry(0x9EC6)
d.entry(0x9EDC)
d.entry(0x9F16)
d.entry(0x9F1C)
d.entry(0x9EF2)
d.entry(0x9711)
d.entry(0x9743)
d.entry(0x9821)
d.entry(0x9837)
d.entry(0x984D)
d.entry(0x9880)
d.entry(0x98DD)
d.entry(0x997B)
d.entry(0x9FA8)
d.entry(0x9FB6)
d.entry(0x9E0A)
d.entry(0x9E2F)
d.entry(0x9E81)
d.entry(0x8228)
d.entry(0x8247)
d.entry(0x8249)
d.entry(0x81AC)
d.entry(0x8280)
d.entry(0x836D)
d.entry(0x8674)
d.entry(0x8CF4)
d.entry(0x8DCF)
d.entry(0x8E59)
d.entry(0x919C)
d.entry(0x9310)
d.entry(0x9669)
d.entry(0x966C)
d.entry(0x99E8)
d.entry(0x9AFC)
d.entry(0x9B35)
d.entry(0x87FC)
d.entry(0x880F)
d.entry(0x8814)
d.entry(0x888D)
d.entry(0x897C)
d.entry(0x8A2E)
d.entry(0x90DE)
d.entry(0x99C5)
d.entry(0x8FE8)
d.entry(0x908F)
for i in range(9):
    d.rts_code_ptr(0x909A + i, 0x90A3 + i)
for y in range(0x81, 0x89):
    d.rts_code_ptr(0x9A04 + y, 0x9A0C + y)
for y in range(0x83, 0x88):
    d.rts_code_ptr(0x9AF1 + y, 0x9AF6 + y)
for y in range(0x81, 0x89):
    d.rts_code_ptr(0x9C3A + y, 0x9C42 + y)


d.label(0x9A95, 'rx_imm_exec')
d.subroutine(0x9A95, 'rx_imm_exec', title='RX immediate: JSR/UserProc/OSProc setup', description="""Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace at &0D58, then jumps to
the common receive path at c9826. Used for operation types
&83 (JSR), &84 (UserProc), and &85 (OSProc).""")


d.label(0x9AB3, 'rx_imm_poke')
d.subroutine(0x9AB3, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data.
port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
the common data-receive path at ack_scout_match.""")


d.label(0x9ABE, 'rx_imm_machine_type')
d.subroutine(0x9ABE, 'rx_imm_machine_type', title='RX immediate: machine type query', description="""Sets up a buffer at &7F25 (length #&01FC) for the machine
type query response, then jumps to the query handler at
set_tx_reply_flag. Returns system identification data to the remote
station.""")


d.label(0x9AD1, 'rx_imm_peek')
d.subroutine(0x9AD1, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Writes &0D3D to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send the
PEEK response data back to the requesting station.
Uses workspace offsets (&A6/&A7) for nmi_tx_block.""")


d.label(0x9B7E, 'tx_done_jsr')
d.subroutine(0x9B7E, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes address &9BEB on the stack (so RTS returns to
tx_done_exit), then does JMP (l0d58) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")


d.label(0x9B87, 'tx_done_user_proc')
d.subroutine(0x9B87, 'tx_done_user_proc', title='TX done: UserProc event', description="""Generates a network event (event 8) via OSEVEN with
X=l0d58, A=l0d59 (the remote address). This notifies
the user program that a UserProc operation has completed.""")


d.label(0x9B95, 'tx_done_os_proc')
d.subroutine(0x9B95, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM entry point at &8000 (rom_header) with
X=l0d58, Y=l0d59. This invokes an OS-level procedure
on behalf of the remote station.""")


d.label(0x9BA1, 'tx_done_halt')
d.subroutine(0x9BA1, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of rx_flags (&0D64), enables interrupts, and
spin-waits until bit 2 is cleared (by a CONTINUE from the
remote station). If bit 2 is already set, skips to exit.""")


d.label(0x9BB8, 'tx_done_continue')
d.subroutine(0x9BB8, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of rx_flags (&0D64), releasing any station
that is halted and spinning in tx_done_halt.""")

d.label(0x9BC0, 'tx_done_exit')


d.label(0x9CCF, 'tx_ctrl_peek')
d.subroutine(0x9CCF, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace at &0D1E-&0D21 (with carry propagation).
Calls tx_calc_transfer to finalise, then exits via
tx_ctrl_exit.""")


d.label(0x9CD3, 'tx_ctrl_poke')
d.subroutine(0x9CD3, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")


d.label(0x9CE7, 'tx_ctrl_proc')
d.subroutine(0x9CE7, 'tx_ctrl_proc', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")

d.label(0x9D26, 'tx_ctrl_exit')
d.entry(0x9173)
d.entry(0x91DF)
d.entry(0x9150)
d.entry(0x878A)
d.entry(0x8FCD)
d.entry(0x9815)
d.entry(0x85C8)


d.subroutine(0x85C8, 'save_fscv_args_with_ptrs', title='Save FSCV arguments with text pointers', description="""Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
falls through to save_fscv_args to store A/X/Y in the FS
workspace.""")


d.subroutine(0x85D2, 'save_fscv_args', title='Save FSCV/vector arguments', description="""Stores A, X, Y into the filing system workspace. Called at the
start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
  &BD (fs_last_byte_flag) = A (function code / command)
  &BB (fs_options)        = X (control block ptr low)
  &BC (fs_block_offset)   = Y (control block ptr high)
  &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)""", on_entry={'a': 'function code', 'x': 'control block pointer low', 'y': 'control block pointer high'})


d.subroutine(0x85DD, 'decode_attribs_6bit', title='Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)', description="""Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&85FA. The two formats use different bit layouts for file
protection attributes.""")


d.subroutine(0x85E7, 'decode_attribs_5bit', title='Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)', description="""Masks A to 5 bits and builds an access bitmask via the
lookup table at &85FA. Each input bit position maps to a
different output bit via the table. The conversion is done
by iterating through the source bits and OR-ing in the
corresponding destination bits from the table, translating
between BBC (8-bit) and fileserver (5-bit) protection formats.""", on_entry={'a': 'BBC attribute byte (bits 0-4 used)'}, on_exit={'a': 'FS attribute bitmask (5-bit)', 'x': 'corrupted'})


d.subroutine(0x8620, 'parse_decimal', title='Parse decimal number from (fs_options),Y (DECIN)', description="""Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
then ADC &B2 gives x10.
Terminates on "." (pathname separator), control chars, or space.
The delimiter handling was revised to support dot-separated path
components (e.g. "1.$.PROG",
    on_entry={"y": "offset into (fs_options) buffer"},
    on_exit={"a": "parsed value (accumulated in &B2)", "x": "initial A value (saved by TAX)", "y": "offset past last digit parsed"})
>= &40 (any letter), but the revision allows numbers followed
by dots.""", on_entry={'y': 'offset into (fs_options) buffer'}, on_exit={'a': 'parsed value (accumulated in &B2)', 'x': 'preserved', 'y': 'offset past last digit parsed'})
d.comment(0x8620, 'Zero accumulator', align=Align.INLINE)
d.comment(0x8624, 'Load next char from buffer', align=Align.INLINE)
d.comment(0x8626, 'Dot separator?', align=Align.INLINE)
d.comment(0x8628, 'Yes: exit with C=1 (dot found)', align=Align.INLINE)
d.comment(0x862A, 'Control char or space: done', align=Align.INLINE)
d.comment(0x862C, 'Mask ASCII digit to 0-9', align=Align.INLINE)
d.comment(0x862E, 'Save new digit', align=Align.INLINE)
d.comment(0x8630, 'Running total * 2', align=Align.INLINE)
d.comment(0x8632, 'A = running total * 2', align=Align.INLINE)
d.comment(0x8634, 'A = running total * 4', align=Align.INLINE)
d.comment(0x8635, 'A = running total * 8', align=Align.INLINE)
d.comment(0x8636, '+ total*2 = total * 10', align=Align.INLINE)
d.comment(0x8638, '+ digit = total*10 + digit', align=Align.INLINE)
d.comment(0x863A, 'Store new running total', align=Align.INLINE)
d.comment(0x863C, 'Advance to next char', align=Align.INLINE)
d.comment(0x863D, "Loop (always: Y won't wrap to 0)", align=Align.INLINE)
d.comment(0x863F, 'No dot found: C=0', align=Align.INLINE)
d.comment(0x8640, 'Return result in A', align=Align.INLINE)


d.subroutine(0x8643, 'handle_to_mask_a', title='Convert handle in A to bitmask', description="""Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""", on_entry={'a': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})


d.subroutine(0x8644, 'handle_to_mask_clc', title='Convert handle to bitmask (carry cleared)', description="""Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""", on_entry={'y': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})


d.subroutine(0x8645, 'handle_to_mask', title='Convert file handle to bitmask (Y2FS)', description="""Converts fileserver handles to single-bit masks segregated inside
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
d.comment(0x8645, 'Save A (will be restored on exit)', align=Align.INLINE)
d.comment(0x8646, 'Save X (will be restored on exit)', align=Align.INLINE)
d.comment(0x8647, '  (second half of X save)', align=Align.INLINE)
d.comment(0x8648, 'A = handle from Y', align=Align.INLINE)
d.comment(0x8649, 'C=0: always convert', align=Align.INLINE)
d.comment(0x864B, 'C=1 and Y=0: skip (handle 0 = none)', align=Align.INLINE)
d.comment(0x864D, 'C=1 and Y!=0: convert', align=Align.INLINE)
d.comment(0x864E, 'A = handle - &1F (1-based bit position)', align=Align.INLINE)
d.comment(0x8650, 'X = shift count', align=Align.INLINE)
d.comment(0x8651, 'Start with bit 0 set', align=Align.INLINE)
d.comment(0x8653, 'Shift bit left', align=Align.INLINE)
d.comment(0x8654, 'Count down', align=Align.INLINE)
d.comment(0x8655, 'Loop until correct position', align=Align.INLINE)
d.comment(0x8657, 'Undo final extra shift', align=Align.INLINE)
d.comment(0x8658, 'Y = resulting bitmask', align=Align.INLINE)
d.comment(0x8659, 'Non-zero: valid mask, skip to exit', align=Align.INLINE)
d.comment(0x865B, 'Zero: invalid handle, set Y=&FF', align=Align.INLINE)
d.comment(0x865C, 'Restore X', align=Align.INLINE)
d.comment(0x865E, 'Restore A', align=Align.INLINE)


d.subroutine(0x8660, 'mask_to_handle', title='Convert bitmask to handle number (FS2A)', description="""Inverse of Y2FS. Converts from the power-of-two FS format
back to a sequential handle number by counting right shifts
until A=0. Adds &1E to convert the 1-based bit position to
a handle number (handles start at &1F+1 = &20). Used when
receiving handle values from the fileserver in reply packets.""", on_entry={'a': 'single-bit bitmask'}, on_exit={'a': 'handle number (&20-&27)', 'x': 'corrupted', 'y': 'preserved'})
d.comment(0x8660, 'X = &1F (handle base - 1)', align=Align.INLINE)
d.comment(0x8662, 'Count this bit position', align=Align.INLINE)
d.comment(0x8663, 'Shift mask right; C=0 when done', align=Align.INLINE)
d.comment(0x8664, 'Loop until all bits shifted out', align=Align.INLINE)
d.comment(0x8666, 'A = X = &1F + bit position = handle', align=Align.INLINE)


d.subroutine(0x8DB0, 'print_decimal', title='Print byte as 3-digit decimal number', description="""Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""", on_entry={'a': 'byte value to print'}, on_exit={'a': 'last digit character', 'x': 'corrupted', 'y': '0 (remainder after last division)'})


d.subroutine(0x8DBD, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Divides Y by A using repeated subtraction. Prints the
quotient as an ASCII digit ('0'-'9') via OSASCI. Returns
with the remainder in Y. X starts at &2F ('0'-1) and
increments once per subtraction, giving the ASCII digit
directly.""", on_entry={'a': 'divisor (stored to &B8)', 'y': 'dividend'}, on_exit={'y': 'remainder'})


d.subroutine(0x8668, 'compare_addresses', title='Compare two 4-byte addresses', description="""Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
Used by the OSFILE save handler to compare the current
transfer address (&C8-&CB, copied to &B0) against the end
address (&B4-&B7) during multi-block file data transfers.""", on_exit={'a': 'corrupted (EOR result)', 'x': 'corrupted', 'y': 'preserved'})


d.subroutine(0x8679, 'set_fs_flag', title='Set bit(s) in EOF hint flags (&0E07)', description="""ORs A into fs_eof_flags then stores the result via
store_fs_flag. Each bit represents one of up to 8 open file
handles. When clear, the file is definitely NOT at EOF. When
set, the fileserver must be queried to confirm EOF status.
This negative-cache optimisation avoids expensive network
round-trips for the common case. The hint is cleared when
the file pointer is updated (since seeking away from EOF
invalidates the hint) and set after BGET/OPEN/EOF operations
that might have reached the end.""", on_entry={'a': 'bitmask of bits to set'}, on_exit={'a': 'updated fs_eof_flags value'})


d.subroutine(0x867E, 'clear_fs_flag', title='Clear bit(s) in FS flags (&0E07)', description="""Inverts A (EOR #&FF), then ANDs the result into fs_eof_flags
to clear the specified bits.""", on_entry={'a': 'bitmask of bits to clear'}, on_exit={'a': 'updated fs_eof_flags value'})


d.subroutine(0x8D24, 'print_file_info', title='Print file catalogue line', description="""Displays a formatted catalogue entry: filename (padded to 12
chars with spaces), load address (4 hex bytes at offset 5-2),
exec address (4 hex bytes at offset 9-6), and file length
(3 hex bytes at offset &0C-&0A), followed by a newline.
Data is read from (fs_crc_lo) for the filename and from
(fs_options) for the numeric fields. Returns immediately
if fs_messages_flag is zero (no info available).""")


d.label(0x9FE0, 'print_hex')
d.subroutine(0x9FE0, 'print_hex', title='Print byte as two hex digits', description="""Prints the high nibble first (via 4x LSR), then the low
nibble. Each nibble is converted to ASCII '0'-'9' or 'A'-'F'
and output via OSASCI. Returns with carry set.""", on_entry={'a': 'byte to print as two hex digits'}, on_exit={'a': 'preserved (original byte)', 'x': 'corrupted (by OSASCI)'})


d.label(0x9FE9, 'print_hex_nibble')
d.subroutine(0x9FE9, 'print_hex_nibble', title='Print single hex nibble', description="""Converts the low nibble of A to ASCII hex ('0'-'9' or 'A'-'F')
and prints via OSASCI. Returns with carry set.""")


d.subroutine(0x8687, 'setup_tx_ptr_c0', title='Set up TX pointer to control block at &00C0', description="""Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""")


d.subroutine(0x868F, 'tx_poll_ff', title='Transmit and poll for result (full retry)', description="""Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""")


d.subroutine(0x8693, 'tx_poll_core', title='Core transmit and poll routine (XMIT)', description="""Claims the TX semaphore (tx_ctrl_status) via ASL -- a busy-wait
spinlock where carry=0 means the semaphore is held by another
operation. Only after claiming the semaphore is the TX pointer
copied to nmi_tx_block, ensuring the low-level transmit code
sees a consistent pointer. Then calls the ADLC TX setup routine
and polls the control byte for completion:
  bit 7 set = still busy (loop)
  bit 6 set = error (check escape or report)
  bit 6 clear = success (clean return)
On error, checks for escape condition and handles retries.
Two entry points: setup_tx_ptr_c0 (&8687) always uses the
standard TXCB; tx_poll_core (&8693) is general-purpose.""", on_entry={'a': 'retry count (&FF = full retry)', 'y': 'timeout parameter (&60 = standard)'}, on_exit={'a': 'entry A (retry count, restored from stack)', 'x': '0', 'y': '0'})


d.subroutine(0x8605, 'print_inline', title='Print inline string, high-bit terminated (VSTRNG)', description="""Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. N.B. Cannot be used for
BRK error messages -- the stack manipulation means a BRK in the
inline data would corrupt the stack rather than invoke the error
handler.""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})
d.comment(0x8605, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x8608, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x860D, 'Advance pointer past return address / to next char', align=Align.INLINE)
d.comment(0x8613, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x8615, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x861D, 'Jump to address of high-bit byte (resumes code after string)', align=Align.INLINE)
d.comment(0x8025, """Dispatch table: low bytes of (handler_address - 1)
Each entry stores the low byte of a handler address minus 1,
for use with the PHA/PHA/RTS dispatch trick at &80E7.
See dispatch_0_hi (&804A) for the corresponding high bytes.

Five callers share this table via different Y base offsets:
  Y=&00  Service calls 0-12       (indices 0-13)
  Y=&0E  Language entry reasons    (indices 14-18)
  Y=&13  FSCV codes 0-7           (indices 19-26)
  Y=&17  FS reply handlers        (indices 27-32)
  Y=&21  *NET1-4 sub-commands     (indices 33-36)

Lo bytes for the last 6 entries (indices 31-36) occupy
&8044-&8049, immediately before the hi bytes. Their hi
bytes are at &8069-&806E, after dispatch_0_hi.""")
d.comment(0x804A, """Dispatch table: high bytes of (handler_address - 1)
Paired with dispatch_0_lo (&8025). Together they form a table
of 37 handler addresses, used via the PHA/PHA/RTS trick at
&80E7.""")
dispatch_comments = ['Svc 0: already claimed (no-op)', 'Svc 1: absolute workspace', 'Svc 2: private workspace', 'Svc 3: auto-boot', 'Svc 4: unrecognised star command', 'Svc 5: unrecognised interrupt', 'Svc 6: BRK (no-op)', 'Svc 7: unrecognised OSBYTE', 'Svc 8: unrecognised OSWORD', 'Svc 9: *HELP', 'Svc 10: static workspace (no-op)', 'Svc 11: NMI release (reclaim NMIs)', 'Svc 12: NMI claim (save NMI state)', 'Svc 13: select NFS (intercepted before dispatch)', 'Lang 0: no language / Tube', 'Lang 1: normal startup', 'Lang 2: softkey byte (Electron)', 'Lang 3: softkey length (Electron)', 'Lang 4: remote validated', 'FSCV 0: *OPT', 'FSCV 1: EOF check', 'FSCV 2: */ (run)', 'FSCV 3: unrecognised star command', 'FSCV 4: *RUN', 'FSCV 5: *CAT', 'FSCV 6: shutdown', 'FSCV 7: read handle range', 'FS reply: print directory name', 'FS reply: copy handles + boot', 'FS reply: copy handles', 'FS reply: set CSD handle', 'FS reply: notify + execute', 'FS reply: set library handle', '*NET1: read handle from packet', '*NET2: read handle from workspace', '*NET3: close handle', '*NET4: resume remote']
for i, body in enumerate(dispatch_comments):
    d.comment(0x8025 + i, f'lo - {body}', align=Align.INLINE)
    d.comment(0x804A + i, f'hi - {body}', align=Align.INLINE)


d.subroutine(0x806F, 'dispatch_net_cmd', title='*NET command dispatcher', description="""Parses the character after *NET as '1'-'4', maps to table
indices 33-36 via base offset Y=&21, and dispatches via &80E7.
Characters outside '1'-'4' fall through to return_1 (RTS).

These are internal sub-commands used only by the ROM itself,
not user-accessible star commands. The MOS command parser
requires a space or terminator after 'NET', so *NET1 typed
at the command line does not match; these are reached only
via OSCLI calls within the ROM.

*NET1 (&8E59): read file handle from received
packet (net_1_read_handle)

*NET2 (&8E5F): read handle entry from workspace
(net_2_read_handle_entry)

*NET3 (&8E6F): close handle / mark as unused
(net_3_close_handle)

*NET4 (&81B8): resume after remote operation
(net_4_resume_remote)""")
d.comment(0x806F, 'Read command character following *NET', align=Align.INLINE)
d.comment(0x8071, "Subtract ASCII '1' to get 0-based command index", align=Align.INLINE)
d.comment(0x807D, 'Y=&21: base offset for *NET commands (index 33+)', align=Align.INLINE)


d.subroutine(0x80E7, 'dispatch', title='PHA/PHA/RTS computed dispatch', description="""X = command index within caller's group (e.g. service number)
Y = base offset into dispatch table (0, &0E, &13, &21, etc.)
The loop adds Y+1 to X, so final X = command index + base + 1.
Then high and low bytes of (handler-1) are pushed onto the stack,
and RTS pops them and jumps to handler_address.

This is a standard 6502 trick: RTS increments the popped address
by 1 before jumping, so the table stores (address - 1) to
compensate. Multiple callers share one table via different Y
base offsets.""")
d.comment(0x80E7, 'Add base offset Y to index X (loop: X += Y+1)', align=Align.INLINE)
d.comment(0x80EC, 'Load high byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80EF, 'Push high byte onto stack', align=Align.INLINE)
d.comment(0x80F0, 'Load low byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80F3, 'Push low byte onto stack', align=Align.INLINE)
d.comment(0x80F4, 'Restore X (fileserver options) for use by handler', align=Align.INLINE)
d.comment(0x80F6, 'RTS pops address, adds 1, jumps to handler', align=Align.INLINE)


d.subroutine(0x80E1, 'lang_entry_dispatch', title='Language entry dispatcher', description="""Called when the NFS ROM is entered as a language. Although rom_type
(&82) does not set the language bit, the MOS enters this point
after NFS claims service &FE (Tube post-init). X = reason code
(0-4). Dispatches via table indices 15-19 (base offset Y=&0E).""")
d.comment(0x80E5, 'Y=&0E: base offset for language handlers (index 15+)', align=Align.INLINE)


d.subroutine(0x811F, 'service_handler_entry', title='Service handler entry', description="""Intercepts three service calls before normal dispatch:
  &FE: Tube init -- explode character definitions
  &FF: Full init -- vector setup, copy code to RAM, select NFS
  &12 (Y=5): Select NFS as active filing system
All other service calls < &0D dispatch via dispatch.""")

d.label(0x8140, 'init_vectors_and_copy')


d.subroutine(0x81ED, 'svc_13_select_nfs', title='Select NFS as active filing system (INIT)', description="""Reached from service &12 (select FS) with Y=5, or when *NET command
selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
this triggers the outgoing FS to save its context back to its
workspace page, allowing restoration if re-selected later (the
FSDIE handoff mechanism). Then sets up the standard OS vector
indirections (FILEV through FSCV) to NFS entry points, claims the
extended vector table entries, and issues service &0F (vectors
claimed) to notify other ROMs. If nfs_temp is zero (auto-boot
not inhibited), injects the synthetic command "I .BOOT" through
the command decoder to trigger auto-boot login.""")


d.subroutine(0x8224, 'check_boot_key', title='Check boot key', description="""Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")


d.subroutine(0x822E, 'print_station_info', title='Print station identification', description="""Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")


d.subroutine(0x8260, 'init_fs_vectors', title='Initialise filing system vectors', description="""Copies 14 bytes from fs_vector_addrs (&8296) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from svc_13_select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")
d.comment(0x8260, 'Copy 14 bytes: FS vector addresses → FILEV-FSCV', align=Align.INLINE)
d.string(0x828E, 8)
d.comment(0x828E, """Synthetic auto-boot command string. "I " does not match any
entry in NFS's local command table — "I." requires a dot, and
"I AM" requires 'A' after the space — so fscv_3_star_cmd
forwards the entire string to the fileserver, which executes
the .BOOT file.""")


d.subroutine(0x8296, 'fs_vector_addrs', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by init_fs_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the ROM pointer table.

Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (store_rom_ptr_pair writes the current ROM
bank number without reading). The last entry (FSCV) has no
padding byte.""")
for i, name in enumerate(['FILEV', 'ARGSV', 'BGETV', 'BPUTV', 'GBPBV', 'FINDV', 'FSCV']):
    addr = 0x8296 + i * 2
    d.word(addr)
    d.comment(addr, f'{name} dispatch (&FF{0x1B + i * 3:02X})', align=Align.INLINE)
handler_names = [('FILEV', 0x8705), ('ARGSV', 0x8924), ('BGETV', 0x855C), ('BPUTV', 0x840F), ('GBPBV', 0x8A2E), ('FINDV', 0x8994), ('FSCV', 0x80D4)]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x82A4 + i * 3
    d.word(base_addr)
    d.comment(base_addr, f'{name} handler (&{handler_addr:04X})', align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, '(ROM bank — not read)', align=Align.INLINE)


d.subroutine(0x82B8, 'svc_1_abs_workspace', title='Service 1: claim absolute workspace', description="""Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""", on_entry={'y': 'current top of absolute workspace'}, on_exit={'y': 'updated top of absolute workspace (max of input and &10)'})


d.subroutine(0x82C1, 'svc_2_private_workspace', title='Service 2: claim private workspace and initialise NFS', description="""Y = next available workspace page on entry.
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
d.comment(0x82D8, 'OSBYTE &FD: read type of last reset', align=Align.INLINE)
d.comment(0x82DE, 'Soft break (X=0): skip FS init', align=Align.INLINE)
d.comment(0x82E4, 'Station &FE = no server selected', align=Align.INLINE)
d.comment(0x8312, 'Read station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x8319, 'Initialise ADLC hardware', align=Align.INLINE)


d.subroutine(0x8219, 'svc_3_autoboot', title='Service 3: auto-boot', description="""Notifies current FS of shutdown via FSCV A=6. Scans keyboard
(OSBYTE &7A): if no key is pressed, auto-boot proceeds directly
via print_station_info. If a key is pressed, falls through to
check_boot_key: the 'N' key (matrix address &55) proceeds with
auto-boot, any other key causes the auto-boot to be declined.""")


d.subroutine(0x81A5, 'svc_star_command', title='Service 4: unrecognised * command', description="""The first 7 bytes (&81A5-&81AB) are the service handler epilogue:
PLA/STA restores &A9, TXA/LDX retrieves romsel_copy, then RTS.
This is the return path reached after any dispatched service
handler completes.

The service 4 handler itself is dispatched via the table to
&81B1 (after 5 NOPs of padding). It makes two match_rom_string
calls against the ROM header, reusing header bytes as command
strings:

  X=&0C: matches "ROFF" at &8014 — the suffix of the
         copyright string "(C)ROFF" → *ROFF (Remote Off,
         end remote session) — falls through to net_4_resume_remote

  X=5: matches "NET" at &800D — the ROM title suffix
       → *NET (select NFS) — falls through to svc_13_select_nfs

If neither matches, returns with the service call
unclaimed.""")


d.subroutine(0x8204, 'svc_9_help', title='Service 9: *HELP', description='Prints the ROM identification string using print_inline.')

d.label(0x835E, 'match_rom_string')
d.comment(0x835E, 'Y = saved text pointer offset', align=Align.INLINE)
d.comment(0x8360, 'Load next input character', align=Align.INLINE)
d.comment(0x8362, "Is it a '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8364, 'Yes: skip to space skipper (match)', align=Align.INLINE)
d.comment(0x8366, 'Force uppercase (clear bit 5)', align=Align.INLINE)
d.comment(0x8368, 'Input char is NUL/space: check ROM byte', align=Align.INLINE)
d.comment(0x836A, 'Compare with ROM string byte', align=Align.INLINE)
d.comment(0x836D, 'Mismatch: check if ROM string ended', align=Align.INLINE)
d.comment(0x836F, 'Advance input pointer', align=Align.INLINE)
d.comment(0x8370, 'Advance ROM string pointer', align=Align.INLINE)
d.comment(0x8371, 'Continue matching (always taken)', align=Align.INLINE)
d.comment(0x8373, 'Load ROM string byte at match point', align=Align.INLINE)
d.comment(0x8376, 'Zero = end of ROM string = full match', align=Align.INLINE)
d.comment(0x8378, 'Non-zero = partial/no match; Z=0', align=Align.INLINE)
d.comment(0x8379, 'Skip this space', align=Align.INLINE)
d.comment(0x837A, 'Load next input character', align=Align.INLINE)
d.comment(0x837C, 'Is it a space?', align=Align.INLINE)
d.comment(0x837E, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0x8380, 'XOR with CR: Z=1 if end of line', align=Align.INLINE)


d.subroutine(0x8214, 'call_fscv_shutdown', title='Notify filing system of shutdown', description="""Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")


d.subroutine(0x8277, 'issue_vectors_claimed', title="Issue 'vectors claimed' service and optionally auto-boot", description="""Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If nfs_temp is zero (auto-boot not inhibited),
sets up the command string "I .BOOT" at &828E and jumps to
the FSCV 3 unrecognised-command handler (which matches against
the command table at &8C05). The "I." prefix triggers the
catch-all entry which forwards the command to the fileserver.
Falls through to run_fscv_cmd.""")


d.subroutine(0x8289, 'run_fscv_cmd', title='Run FSCV command from ROM', description="""Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
to execute the command string at (X, Y). X is pre-loaded by the
caller with the low byte of the string address. Also used as a
data base address by store_rom_ptr_pair for Y-indexed access to
the handler address table.""")


d.subroutine(0x8321, 'setup_rom_ptrs_netv', title='Set up ROM pointer table and NETV', description="""Reads the ROM pointer table base address via OSBYTE &A8, stores
it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
one 3-byte extended vector entry (addr=&9076, rom=current) into
the ROM pointer table at offset &36, installing osword_dispatch
as the NETV handler.""")


d.subroutine(0x834D, 'fscv_6_shutdown', title='FSCV 6: Filing system shutdown / save state (FSDIE)', description="""Called when another filing system (e.g. DFS) is selected. Saves
the current NFS context (FSLOCN station number, URD/CSD/LIB
handles, OPT byte, etc.) from page &0E into the dynamic workspace
backup area. This allows the state to be restored when *NET is
re-issued later, without losing the login session. Finally calls
OSBYTE &77 (close SPOOL/EXEC files) to release the
Econet network printer on FS switch.""")


d.subroutine(0x8391, 'init_tx_ctrl_block', title='Initialise TX control block at &00C0 from template', description="""Copies 12 bytes from tx_ctrl_template (&83A9) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""")


d.subroutine(0x83A9, 'tx_ctrl_template', title='TX control block template (TXTAB, 12 bytes)', description="""12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")


d.subroutine(0x83C3, 'prepare_fs_cmd', title='Prepare FS command buffer (12 references)', description="""Builds the 5-byte FS protocol header at &0F00:
  &0F00 HDRREP = reply port (set downstream, typically &90/PREPLY)
  &0F01 HDRFN  = Y parameter (function code)
  &0F02 HDRURD = URD handle (from &0E02)
  &0F03 HDRCSD = CSD handle (from &0E03)
  &0F04 HDRLIB = LIB handle (from &0E04)
Command-specific data follows at &0F05 (TXBUF). Also clears V flag.
Called before building specific FS commands for transmission.""", on_entry={'y': 'function code for HDRFN', 'x': 'preserved through header build'}, on_exit={'a': '0 on success (from build_send_fs_cmd)', 'x': '0 on success, &D6 on not-found', 'y': '1 (offset past command code in reply)'})


d.subroutine(0x83D9, 'build_send_fs_cmd', title='Build and send FS command (DOFSOP)', description="""Sets reply port to &90 (PREPLY) at &0F00, initialises the TX
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


d.subroutine(0x8473, 'store_fs_error', title='Handle fileserver error replies (FSERR)', description="""The fileserver returns errors as: zero command code + error number +
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


d.subroutine(0x8410, 'handle_bput_bget', title='Handle BPUT/BGET file byte I/O', description="""BPUTV enters at &83DC (CLC; fall through) and BGETV enters
at &855C (SEC; JSR here). The carry flag is preserved via
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


d.subroutine(0x851D, 'send_to_fs', title='Send command to fileserver and handle reply (WAITFS)', description="""Performs a complete FS transaction: transmit then wait for reply.
Sets bit 7 of rx_status_flags (mark FS transaction in progress),
builds a TX frame from the data at (net_tx_ptr), and transmits
it. The system RX flag (LFLAG bit 7) is only set when receiving
into the page-zero control block — if RXCBP's high byte is
non-zero, setting the system flag would interfere with other RX
operations. The timeout counter uses the stack (indexed via TSX)
rather than memory to avoid bus conflicts with Econet hardware
during the tight polling loop. Handles multi-block replies and
checks for escape conditions between blocks.""")


d.subroutine(0x854D, 'check_escape_handler', title='Test MOS escape flag and abort if pending', description="""Tests MOS escape flag (&FF bit 7). If escape is pending:
acknowledges via OSBYTE &7E, writes &3F (deleted marker) into
the control block via (net_tx_ptr),Y, and branches to the
NLISTN error path. If no escape, returns immediately.""")

d.label(0x8579, 'error_msg_table')
d.comment(0x8579, """Econet error message table (ERRTAB, 7 entries).
Each entry: error number byte followed by NUL-terminated string.
  &A0: "Line Jammed"     &A1: "Net Error"
  &A2: "Not listening"   &A3: "No Clock"
  &11: "Escape"           &CB: "Bad Option"
  &A5: "No reply"
Indexed by the low 3 bits of the TXCB flag byte (AND #&07),
which encode the specific Econet failure reason. The NREPLY
and NLISTN routines build a MOS BRK error block at &100 on the
stack page: NREPLY fires when the fileserver does not respond
within the timeout period; NLISTN fires when the destination
station actively refused the connection.
Indexed via the error dispatch at c8424/c842c.""")
addr = 0x8579
for _ in range(7):
    d.byte(addr, 1)
    addr = d.stringz(addr + 1)


d.subroutine(0x81B8, 'net_4_resume_remote', title='Resume after remote operation / *ROFF handler (NROFF)', description="""Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
disabled during a remote operation (peek/poke/boot). Clears
the flag, re-enables the keyboard via OSBYTE &C9, and sends
function &0A to notify completion. Also handles *ROFF and the
triple-plus escape sequence (+++), which resets system masks
via OSBYTE &CE and returns control to the MOS, providing an
escape route when a remote session becomes unresponsive.""")


d.subroutine(0x80D4, 'fscv_handler', title='FSCV dispatch entry', description="""Entered via the extended vector table when the MOS calls FSCV.
Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
and dispatches codes 0-7 via the shared dispatch table at &8024
with base offset Y=&13 (table indices 20-27).
Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.""", on_entry={'a': 'function code (0-7)', 'x': 'depends on function', 'y': 'depends on function'}, on_exit={'a': 'depends on handler (preserved if A >= 8)', 'x': 'depends on handler (preserved if A >= 8)', 'y': 'depends on handler (preserved if A >= 8)'})
d.comment(0x80D4, 'Store A/X/Y in FS workspace', align=Align.INLINE)
d.comment(0x80D9, 'Function code >= 8? Return (unsupported)', align=Align.INLINE)
d.comment(0x80DD, 'Y=&13: base offset for FSCV dispatch (indices 20+)', align=Align.INLINE)


d.subroutine(0x86E1, 'parse_filename_gs', title='Parse filename using GSINIT/GSREAD into &0E30', description="""Uses the MOS GSINIT/GSREAD API to parse a filename string from
(os_text_ptr),Y, handling quoted strings and |-escaped characters.
Stores the parsed result CR-terminated at &0E30 and sets up
fs_crc_lo/hi to point to that buffer. Sub-entry at &86C5 allows
a non-zero starting Y offset.""", on_entry={'y': 'offset into (os_text_ptr) buffer (0 at &86C3)'}, on_exit={'x': 'length of parsed string', 'y': 'preserved'})


d.subroutine(0x8705, 'filev_handler', title='FILEV handler (OSFILE entry point)', description="""Calls save_fscv_args (&85D2) to preserve A/X/Y, then JSR &86D7
to copy the 2-byte filename pointer from the parameter block to
os_text_ptr and fall through to parse_filename_gs (&86E1) which
parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &871B)
  A=&00: save file (filev_save at &878F)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &888D)
  Other: restore_args_return (unsupported, no-op)""", on_entry={'a': 'function code (&FF=load, &00=save, &01-&06=attrs)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x871B, 'send_fs_examine', title='Send FS examine command', description="""Sends FS command &03 (FCEXAM: examine file) to the fileserver.
Sets &0F02=&03 and error pointer to '*'. Called for OSFILE &FF
(load file) with the filename already in the command buffer.
The FS reply contains load/exec addresses and file length which
are used to set up the data transfer. The header URD field
is repurposed to carry the Econet data port number (PLDATA=&92)
for the subsequent block data transfer.""", on_entry={'y': 'FS function code (2=load, 5=examine)', 'x': 'TX buffer extent'})


d.subroutine(0x875F, 'send_data_blocks', title='Send file data in multi-block chunks', description="""Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")


d.subroutine(0x878F, 'filev_save', title='OSFILE save handler (A=&00)', description="""Copies 4-byte load/exec/length addresses from the parameter block
to the FS command buffer, along with the filename. Sends FS
command &91 with function &14 to initiate the save, then
calls print_file_info to display the filename being saved.
Handles both host and Tube-based data sources.
When receiving the save acknowledgement, the RX low pointer is
incremented by 1 to skip the command code (CC) byte, which
indicates the FS type and must be preserved. N.B. this assumes
the RX buffer does not cross a page boundary.""")


d.subroutine(0x87F0, 'copy_load_addr_from_params', title='Copy load address from parameter block', description="""Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""")


d.subroutine(0x8802, 'copy_reply_to_params', title='Copy FS reply data to parameter block', description="""Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""", on_entry={'x': 'attribute byte (stored first at offset &0D)'})


d.subroutine(0x8814, 'transfer_file_blocks', title='Multi-block file data transfer', description="""Manages the transfer of file data in chunks between the local
machine and the fileserver. Entry conditions: WORK (&B0-&B3) and
WORK+4 (&B4-&B7) hold the low and high addresses of the data
being sent/received. Sets up source (&C4-&C7) and destination
(&C8-&CB) from the FS reply, sends &80-byte (128-byte) blocks
with command &91, and continues until all data has been
transferred. Handles address overflow and Tube co-processor
transfers. For SAVE, WORK+8 holds the port on which to receive
byte-level ACKs for each data block (flow control).""")


d.subroutine(0x8869, 'fscv_1_eof', title='FSCV 1: EOF handler', description="""Checks whether a file handle has reached end-of-file. Converts
the handle via handle_to_mask_clc, tests the result against the
EOF hint byte (&0E07). If the hint bit is clear, returns X=0
immediately (definitely not at EOF — no network call needed).
If the hint bit is set, sends FS command &11 (FCEOF) to query
the fileserver for definitive EOF status. Returns X=&FF if at
EOF, X=&00 if not. This two-level check avoids an expensive
network round-trip when the file is known to not be at EOF.""", on_entry={'x': 'file handle to check'}, on_exit={'x': '&FF if at EOF, &00 if not'})


d.subroutine(0x888D, 'filev_attrib_dispatch', title='FILEV attribute dispatch (A=1-6)', description="""Dispatches OSFILE operations by function code:
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


d.subroutine(0x896F, 'restore_args_return', title='Restore arguments and return', description="""Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""")

d.label(0x89E8, 'fscv_0_opt_entry')


d.subroutine(0x89EA, 'fscv_0_opt', title='FSCV 0: *OPT handler (OPTION)', description="""Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""", on_entry={'x': 'option number (1 or 4)', 'y': 'option value'})


d.subroutine(0x8A16, 'adjust_addrs', title='Bidirectional 4-byte address adjustment', description="""Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""", on_entry={'y': 'starting offset into (fs_options) parameter block'}, on_exit={'a': 'corrupted (last adjusted byte)', 'x': '0', 'y': 'entry Y + 4'})
d.comment(0x8A16, 'X=&FC: index into &0E06 area (wraps to 0)', align=Align.INLINE)
d.comment(0x8A18, 'Load byte from param block', align=Align.INLINE)
d.comment(0x8A1A, 'Test sign of adjustment direction', align=Align.INLINE)
d.comment(0x8A1C, 'Negative: subtract instead', align=Align.INLINE)
d.comment(0x8A1E, 'Add adjustment value', align=Align.INLINE)
d.comment(0x8A21, 'Skip to store result', align=Align.INLINE)
d.comment(0x8A24, 'Subtract adjustment value', align=Align.INLINE)
d.comment(0x8A27, 'Store adjusted byte back', align=Align.INLINE)
d.comment(0x8A29, 'Next param block byte', align=Align.INLINE)
d.comment(0x8A2A, 'Next adjustment byte (X wraps &FC->&00)', align=Align.INLINE)
d.comment(0x8A2B, 'Loop 4 times (X=&FC,&FD,&FE,&FF,done)', align=Align.INLINE)


d.subroutine(0x8924, 'argsv_handler', title='ARGSV handler (OSARGS entry point)', description="""  A=0, Y=0: return filing system number (10 = network FS)
  A=0, Y>0: read file pointer via FS command &0A (FCRDSE)
  A=1, Y>0: write file pointer via FS command &14 (FCWRSE)
  A>=3 (ensure): silently returns -- NFS has no local write buffer
     to flush, since all data is sent to the fileserver immediately
The handle in Y is converted via handle_to_mask_clc. For writes
(A=1), the carry flag from the mask conversion is used to branch
to save_args_handle, which records the handle for later use.""", on_entry={'a': 'function code (0=query, 1=write ptr, >=3=ensure)', 'y': 'file handle (0=FS-level query, >0=per-file)'}, on_exit={'a': 'filing system number if A=0/Y=0 query, else restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x8994, 'findv_handler', title='FINDV handler (OSFIND entry point)', description="""  A=0: close file -- delegates to close_handle (&89CC)
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
d.comment(0x89C6, """OR handle bit into fs_sequence_nos (&0E08) to prevent
a newly opened file inheriting a stale sequence number
from a previous file using the same handle.""")


d.subroutine(0x89CC, 'close_handle', title='Close file handle(s) (CLOSE)', description="""  Y=0: close all files — first calls OSBYTE &77 (close SPOOL and
       EXEC files) to coordinate with the MOS before sending the
       close-all command to the fileserver. This ensures locally-
       managed file handles are released before the server-side
       handles are invalidated, preventing the MOS from writing to
       a closed spool file.
  Y>0: close single handle — sends FS close command and clears
       the handle's bit in both the EOF hint byte and the sequence
       number tracking byte.""", on_entry={'y': 'file handle (0=close all, >0=close single)'})


d.subroutine(0x8A2E, 'gbpbv_handler', title='GBPBV handler (OSGBPB entry point)', description="""  A=1-4: file read/write operations (handle-based)
  A=5-8: info queries (disc title, current dir, lib, filenames)
Calls 1-4 are standard file data transfers via the fileserver.
Calls 5-8 were a late addition to the MOS spec and are the only
NFS operations requiring Tube data transfer -- described in the
original source as "untidy but useful in theory." The data format
uses length-prefixed strings (<name length><object name>) rather
than the CR-terminated strings used elsewhere in the FS.""", on_entry={'a': 'call number (1-8)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': '0 after FS operation, else restored', 'x': 'restored', 'y': 'restored'})


d.subroutine(0x8AED, 'osgbpb_info', title='OSGBPB 5-8 info handler (OSINFO)', description="""Handles the "messy interface tacked onto OSGBPB" (original source).
Checks whether the destination address is in Tube space by comparing
the high bytes against TBFLAG. If in Tube space, data must be
copied via the Tube FIFO registers (with delays to accommodate the
slow 16032 co-processor) instead of direct memory access.""")


d.subroutine(0x80C1, 'forward_star_cmd', title='Forward unrecognised * command to fileserver (COMERR)', description="""Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
prepares an FS command with function code 0, and sends it to the
fileserver to request decoding. The server returns a command code
indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
5=load-as-command). This mechanism allows the fileserver to extend
the client's command set without ROM updates. Called from the "I."
and catch-all entries in the command match table at &8C05, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")


d.subroutine(0x83BC, 'bye_handler', title='*BYE handler (logoff)', description="""Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8C05 for "BYE".""")


d.subroutine(0x8BD7, 'fscv_3_star_cmd', title='FSCV 2/3/4: unrecognised * command handler (DECODE)', description="""CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8C05 using case-insensitive comparison with abbreviation
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


d.subroutine(0x8C05, 'fs_cmd_match_table', title='FS command match table (COMTAB)', description="""Format: command letters (bit 7 clear), then dispatch address
as two bytes: high|(bit 7 set), low. The PHA/PHA/RTS trick
adds 1 to the stored (address-1). Matching is case-insensitive
(AND &DF) and supports '.' abbreviation (standard Acorn pattern).

Entries:
  "I."     → &80C1 (forward_star_cmd) — placed first as a fudge
             to catch *I. abbreviation before matching *I AM
  "I AM"   → &8082 (i_am_handler: parse station.net, logon)
  "EX"     → &8C1B (ex_handler: embedded in table tail)
  "BYE"\\r  → &83BC (bye_handler: logoff)
  <catch-all> → &80C1 (forward anything else to FS)""")
d.entry(0x8C1B)

d.label(0x8C1B, 'ex_handler')


d.subroutine(0x8C21, 'fscv_5_cat', title='*CAT handler (directory catalogue)', description="""Sets column width &B6=&14 (20 columns, four files per 80-column
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


d.subroutine(0x8D0F, 'boot_cmd_strings', title='Boot command strings for auto-boot', description="""The four boot options use OSCLI strings at offsets within page &8D.
The offset table at boot_option_offsets+1 (&8D1C) is indexed by
the boot option value (0-3); each byte is the low byte of the
string address, with the page high byte &8D loaded separately:
  Option 0 (Off):  offset &1B → &8D1B = bare CR (empty command)
  Option 1 (Load): offset &0C → &8D0C = "L.!BOOT" (the bytes
      &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D0F)
  Option 2 (Run):  offset &0E → &8D0E = "!BOOT" (bare filename = *RUN)
  Option 3 (Exec): offset &14 → &8D14 = "E.!BOOT"

This is a classic BBC ROM space optimisation: the string data
overlaps with other byte sequences to save space. The &0D byte
at &8D1B terminates "E.!BOOT" AND doubles as the bare-CR
command for boot option 0.""")


d.subroutine(0x8D1B, 'boot_option_offsets', title='Boot option → OSCLI string offset table', description="""Five bytes: the first byte (&0D) is the bare-CR target for boot
option 0; bytes 1-4 are the offset table indexed by boot option
(0-3). Each offset is the low byte of a pointer into page &8D.
The code reads from boot_option_offsets+1 (&8D1C) via
LDX l8d1c,Y with Y=boot_option, then LDY #&8D, JMP oscli.
See boot_cmd_strings for the target strings.""")
for i in range(5):
    d.byte(0x8D1B + i)
d.comment(0x8D07, """Option name encoding: the boot option names ("Off",
"Load", "Run", "Exec") are scattered through the code rather
than stored as a contiguous table. They are addressed via
base+offset from boot_option_text (&8D08), whose first four
bytes are the offset table:
  &6A→&8D72 "Off", &7D→&8D85 "Load",
  &A5→&8DAD "Run", &18→&8D20 "Exec"
Each string is terminated by the next instruction's opcode
having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).""")


d.subroutine(0x8082, 'i_am_handler', title='"I AM" command handler', description="""Dispatched from the command match table when the user types
"*I AM <station>" or "*I AM <network>.<station>". Also used as
the station number parser for "*NET <network>.<station>".
Skips leading spaces, then calls parse_decimal for the first
number. If a dot separator was found (carry set), it stores the
result directly as the network (&0E01) and calls parse_decimal
again for the station (&0E00). With a single number, it is stored
as the station and the network defaults to 0 (local). If a colon
follows, reads interactive input via OSRDCH and appends it to
the command buffer. Finally jumps to forward_star_cmd.""")


d.subroutine(0x8E1F, 'fsreply_5_set_lib', title='Set library handle', description="""Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to JMP restore_args_return if Y is non-zero.""", on_entry={'y': 'library handle from FS reply'})


d.subroutine(0x8E24, 'fsreply_3_set_csd', title='Set CSD handle', description="""Stores Y into &0E03 (current selected directory handle).
Falls through to JMP restore_args_return.""", on_entry={'y': 'CSD handle from FS reply'})


d.subroutine(0x8E2A, 'fsreply_1_copy_handles_boot', title='Copy FS reply handles to workspace and execute boot command', description="""SEC entry (LOGIN): copies 4 bytes from &0F05-&0F08 (FS reply) to
&0E02-&0E05 (URD, CSD, LIB handles and boot option), then
looks up the boot option in boot_option_offsets to get the
OSCLI command string and executes it via JMP oscli.
The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
share the handle-copying code, but only LOGIN executes the boot
command. This use of the carry flag to select behaviour between
two callers avoids duplicating the handle-copy loop.""")


d.subroutine(0x8E2B, 'fsreply_2_copy_handles', title='Copy FS reply handles to workspace (no boot)', description="""CLC entry (SDISC): copies handles only, then jumps to
restore_args_return via jmp_restore_args. Called when the FS reply contains
updated handle values but no boot action is needed.""")


d.subroutine(0x8D75, 'copy_filename', title='Copy filename to FS command buffer', description="""Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""")


d.subroutine(0x8D77, 'copy_string_to_cmd', title='Copy string to FS command buffer', description="""Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""", on_entry={'x': 'destination offset in fs_cmd_data (&0F05+X)'}, on_exit={'x': 'next free position past CR', 'y': 'string length (incl CR)', 'a': '0 (from EOR &0D with final CR)'})
d.comment(0x8D77, 'Start copying from offset 0', align=Align.INLINE)
d.comment(0x8D79, 'Load next byte from source string', align=Align.INLINE)
d.comment(0x8D7E, 'Advance write position', align=Align.INLINE)
d.comment(0x8D80, 'XOR with CR: result=0 if byte was CR', align=Align.INLINE)
d.comment(0x8D82, 'Loop until CR copied', align=Align.INLINE)


d.subroutine(0x8D89, 'fsreply_0_print_dir', title='Print directory name from reply buffer', description="""Prints characters from the FS reply buffer (&0F05+X onwards).
Null bytes (&00) are replaced with CR (&0D) for display.
Stops when a byte with bit 7 set is encountered (high-bit
terminator). Used by fscv_5_cat to display Dir. and Lib. paths.""")


d.subroutine(0x8DCF, 'fscv_2_star_run', title='FSCV 2/4: */ (run) and *RUN handler', description="""Parses the filename via parse_filename_gs and calls infol2,
then falls through to fsreply_4_notify_exec to set up and
send the FS load-as-command request.""")


d.subroutine(0x8DD5, 'fsreply_4_notify_exec', title='FS reply 4: send FS load-as-command and execute response', description="""Initialises a GS reader to skip past the filename and
calculate the command context address, then sets up an FS
command with function code &05 (FCCMND: load as command)
using send_fs_examine. If a Tube co-processor is present
(tx_in_progress != 0), transfers the response data to the
Tube via tube_addr_claim. Otherwise jumps via the indirect
pointer at (&0F09) to execute at the load address.""")


d.subroutine(0x8E3A, 'boot_cmd_execute', title='Execute boot command via OSCLI', description="""Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")
d.entry(0x8E59)

d.label(0x8E59, 'net_1_read_handle')
d.comment(0x8E59, """*NET1: read file handle from received packet.
Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
and falls through to net_2_read_handle_entry's common path.""")


d.subroutine(0x8E47, 'calc_handle_offset', title='Calculate handle workspace offset', description="""Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""", on_entry={'a': 'file handle number'}, on_exit={'a': 'handle*12 or 0 if invalid', 'y': 'workspace offset or 0 if invalid', 'c': 'clear if valid, set if invalid'})
d.comment(0x8E47, 'A = handle * 2', align=Align.INLINE)
d.comment(0x8E48, 'A = handle * 4', align=Align.INLINE)
d.comment(0x8E49, 'Push handle*4 onto stack', align=Align.INLINE)
d.comment(0x8E4A, 'A = handle * 8', align=Align.INLINE)
d.comment(0x8E4B, 'X = stack pointer', align=Align.INLINE)
d.comment(0x8E4C, 'A = handle*8 + handle*4 = handle*12', align=Align.INLINE)
d.comment(0x8E4F, 'Y = offset into handle workspace', align=Align.INLINE)
d.comment(0x8E50, 'Clean up stack (discard handle*4)', align=Align.INLINE)
d.comment(0x8E51, 'Offset >= &48? (6 handles max)', align=Align.INLINE)
d.comment(0x8E53, 'Valid: return with C clear', align=Align.INLINE)
d.comment(0x8E55, 'Invalid: Y = 0', align=Align.INLINE)
d.comment(0x8E57, 'A = 0, C set (error)', align=Align.INLINE)

d.label(0x8E58, 'return_calc_handle')
d.entry(0x8E5F)


d.subroutine(0x8E5F, 'net_2_read_handle_entry', title='*NET2: read handle entry from workspace', description="""Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""")
d.entry(0x8E6F)


d.subroutine(0x8E6F, 'net_3_close_handle', title='*NET3: close handle (mark as unused)', description="""Looks up the handle in &F0 via calc_handle_offset. Writes
&3F ('?') to mark the handle slot as closed in the NFS
workspace. Preserves the carry flag state across the write
using ROL/ROR on rx_status_flags. Clears rom_svc_num on exit.""")


d.subroutine(0x8E7F, 'svc_8_osword', title='Filing system OSWORD entry', description="""Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the
PHA/PHA/RTS dispatch at &8E97.""")
d.comment(0x8E7F, 'Command code from &EF', align=Align.INLINE)
d.comment(0x8E81, 'Subtract &0F: OSWORD &0F-&13 become indices 0-4', align=Align.INLINE)


d.subroutine(0x8E97, 'fs_osword_dispatch', title='PHA/PHA/RTS dispatch for filing system OSWORDs', description="""X = OSWORD number - &0F (0-4). Dispatches via the 5-entry table
at &8EB0 (low) / &8EB5 (high).""")
d.comment(0x8E9F, 'Dispatch table: low bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x8EB5, 'Dispatch table: high bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x815B, 'Copy NMI handler code from ROM to RAM pages &04-&06')
d.comment(0x8175, 'Copy NMI workspace initialiser from ROM to &0016-&0076')


d.subroutine(0x8FE8, 'econet_tx_rx', title='Econet transmit/receive handler', description="""A=0: Initialise TX control block from ROM template at &8391
     (zero entries substituted from NMI workspace &0DDA), transmit
     it, set up RX control block, and receive reply.
A>=1: Handle transmit result (branch to cleanup at &9034).""", on_entry={'a': '0=set up and transmit, >=1=handle TX result'})
d.comment(0x8FE8, 'A=0: set up and transmit; A>=1: handle result', align=Align.INLINE)
d.comment(0x8FAA, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x8FB0, 'Dest station = &FFFF (accept reply from any station)', align=Align.INLINE)
d.comment(0x8FD3, 'Receive data blocks until command byte = &00 or &0D', align=Align.INLINE)
d.comment(0x9062, 'Test for end-of-data marker (&0D)', align=Align.INLINE)


d.subroutine(0x9076, 'osword_dispatch', title='NETVEC dispatch handler (ENTRY)', description="""Indirected from NETVEC at &0224. Saves all registers and flags,
retrieves the reason code from the stacked A, and dispatches to
one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
&908D. Reason codes >= 9 are ignored.

Dispatch targets (from NFS09):
  0:   no-op (RTS)
  1-3: PRINT -- chars in printer buffer / Ctrl-B / Ctrl-C
  4:   NWRCH -- write character to screen (net write char)
  5:   SELECT -- printer selection changed
  6:   no-op (net read char -- not implemented)
  7:   NBYTE -- remote OSBYTE call
  8:   NWORD -- remote OSWORD call""", on_entry={'a': 'reason code (0-8)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'preserved'})
d.comment(0x900A, 'Y=&04: advance to station address', align=Align.INLINE)
d.comment(0x908F, 'PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it', align=Align.INLINE)


d.subroutine(0x9039, 'net_write_char', title='Fn 4: net write character (NWRCH)', description="""Writes a character (passed in Y) to the screen via OSWRITCH.
Before the write, uses TSX to reach into the stack and zero the
carry flag in the caller's saved processor status byte -- ROR
followed by ASL on the stacked P byte (&0106,X) shifts carry
out and back in as zero. This ensures the calling code's PLP
restores carry=0, signalling "character accepted" without needing
a separate CLC/PHP sequence. A classic 6502 trick for modifying
return flags without touching the actual processor status.""", on_entry={'y': 'character to write'}, on_exit={'a': '&3F', 'x': '0', 'y': '0'})


d.subroutine(0x90BA, 'setup_tx_and_send', title='Set up TX control block and send', description="""Builds a TX control block at (nfs_workspace)+&0C from the current
workspace state, then initiates transmission via the ADLC TX path.
This is the common send routine used after command data has been
prepared. The exact control block layout and field mapping need
further analysis.""", on_entry={'a': 'command type byte'})


d.subroutine(0x9173, 'ctrl_block_setup_alt', title='Alternate entry into control block setup', description="""Sets X=&0D, Y=&7C. Tests bit 6 of &83AF to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")


d.subroutine(0x917C, 'ctrl_block_setup', title='Control block setup — main entry', description="""Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &91A8 indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")
d.comment(0x916E, 'Load template byte from ctrl_block_template[X]', align=Align.INLINE)


d.subroutine(0x91A8, 'ctrl_block_template', title='Control block initialisation template', description="""Read by the loop at &9181, indexed by X from a starting value
down to 0. Values are stored into either (nfs_workspace) or
(net_rx_ptr) at offset Y, depending on the V flag.

Two entry paths read different slices of this table:
  ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
  ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &83AF

Sentinel values:
  &FE = stop processing
  &FD = skip this offset (decrement Y but don't store)
  &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)""")
d.byte(0x919D, 1)
d.comment(0x91A8, 'Alt-path only → Y=&6F', align=Align.INLINE)
d.byte(0x919E, 1)
d.comment(0x919E, 'Alt-path only → Y=&70', align=Align.INLINE)
d.byte(0x919F, 1)
d.comment(0x91AA, 'SKIP', align=Align.INLINE)
d.byte(0x91A0, 1)
d.comment(0x91A0, 'SKIP', align=Align.INLINE)
d.byte(0x91A1, 1)
d.comment(0x91A1, '→ Y=&01 / Y=&73', align=Align.INLINE)
d.byte(0x91A2, 1)
d.byte(0x91A3, 1)
d.comment(0x91AE, '→ Y=&03 / Y=&75', align=Align.INLINE)
d.byte(0x91A4, 1)
d.byte(0x91A5, 1)
d.byte(0x91A6, 1)
d.comment(0x91A6, 'PAGE byte → Y=&06 / Y=&78', align=Align.INLINE)
d.byte(0x91A7, 1)
d.comment(0x91A7, '→ Y=&07 / Y=&79', align=Align.INLINE)
d.byte(0x91A8, 1)
d.comment(0x91B3, '→ Y=&08 / Y=&7A', align=Align.INLINE)
d.byte(0x91A9, 1)
d.comment(0x91B4, '→ Y=&09 / Y=&7B', align=Align.INLINE)
d.byte(0x91AA, 1)
d.byte(0x91AB, 1)
d.byte(0x91AC, 1)
d.comment(0x91AC, '→ Y=&0C (main only)', align=Align.INLINE)
d.byte(0x91AD, 1)
d.comment(0x91AD, '→ Y=&0D (main only)', align=Align.INLINE)
d.byte(0x91AE, 1)
d.byte(0x91AF, 1)
d.comment(0x91AF, 'SKIP (main only)', align=Align.INLINE)
d.byte(0x91B0, 1)
d.comment(0x91B0, '→ Y=&10 (main only)', align=Align.INLINE)
d.byte(0x91B1, 1)
d.byte(0x91B2, 1)
d.byte(0x91B3, 1)
d.byte(0x91B4, 1)
d.byte(0x91B5, 1)
d.comment(0x91B5, 'PAGE byte → Y=&15 (main only)', align=Align.INLINE)
d.byte(0x91B6, 1)
d.comment(0x91B6, '→ Y=&16 (main only)', align=Align.INLINE)
d.byte(0x91B7, 1)


d.subroutine(0x8F1C, 'copy_param_block', title='Bidirectional block copy between OSWORD param block and workspace.', description="""C=1: copy X+1 bytes from (&F0),Y to (fs_crc_lo),Y (param to workspace)
C=0: copy X+1 bytes from (fs_crc_lo),Y to (&F0),Y (workspace to param)""")
d.comment(0x8F14, 'C=0: skip param-to-workspace copy', align=Align.INLINE)
d.comment(0x8F1A, 'Load byte from workspace', align=Align.INLINE)
d.comment(0x8F1C, 'Store to param block (no-op if C=1)', align=Align.INLINE)
d.comment(0x8F1E, 'Advance to next byte', align=Align.INLINE)

d.label(0x8F22, 'return_copy_param')


d.subroutine(0x8EBA, 'osword_0f_handler', title='OSWORD &0F handler: initiate transmit (CALLTX)', description="""Checks the TX semaphore (TXCLR at &0D62) via ASL -- if carry is
clear, a TX is already in progress and the call returns an error,
preventing user code from corrupting a system transmit. Otherwise
copies 16 bytes from the caller's OSWORD parameter block into the
user TX control block (UTXCB) in static workspace. The TXCB
pointer is copied to LTXCBP only after the semaphore is claimed,
ensuring the low-level transmit code (BRIANX) sees a consistent
pointer -- if copied before claiming, another transmitter could
modify TXCBP between the copy and the claim.""", on_entry={'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'corrupted', 'x': 'corrupted', 'y': '&FF'})


d.subroutine(0x8ED4, 'osword_11_handler', title='OSWORD &11 handler: read JSR arguments (READRA)', description="""Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8EE9) to return just the buffer size and args size
without copying the data.""")


d.subroutine(0x8E85, 'osword_12_handler', title='OSWORD &12 handler: read/set state information (RS)', description="""Dispatches on the sub-function code (0-9):
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
Uses the bidirectional copy at &8EB1 for station read/set.""")


d.subroutine(0x8F74, 'osword_10_handler', title='OSWORD &10 handler: open/read RX control block (OPENRX)', description="""If the first byte of the caller's parameter block is zero, scans
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


d.subroutine(0x849A, 'lang_1_remote_boot', title='Remote boot/execute handler', description="""Checks byte 4 of the RX control block (remote status flag).
If zero (not currently remoted), falls through to remot1 to
set up a new remote session. If non-zero (already remoted),
jumps to clear_jsr_protection and returns.""")


d.subroutine(0x84C8, 'lang_3_execute_at_0100', title='Execute code at &0100', description="""Clears JSR protection, zeroes &0100-&0102 (creating a BRK
instruction at &0100 as a safe default), then JMP &0100 to
execute code received over the network. If no code was loaded,
the BRK triggers an error handler.""")


d.subroutine(0x84D8, 'lang_4_remote_validated', title='Remote operation with source validation', description="""Validates that the source station in the received packet matches
the controlling station stored in the NFS workspace. If byte 4 of
the RX control block is zero (not currently remoted), allows the
new remote session via remot1. If non-zero, compares the source
station at RX offset &80 against workspace offset &0E -- rejects
mismatched stations via clear_jsr_protection, accepts matching
stations by falling through to lang_0_insert_remote_key.""")


d.subroutine(0x84E8, 'lang_0_insert_remote_key', title='Insert remote keypress', description="""Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")


d.subroutine(0x8FCD, 'setup_rx_buffer_ptrs', title='Set up RX buffer pointers in NFS workspace', description="""Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &28. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &2C.""", on_entry={'c': 'clear for ADC'})


d.subroutine(0x90DE, 'remote_cmd_dispatch', title='Fn 7: remote OSBYTE handler (NBYTE)', description="""Full RPC mechanism for OSBYTE calls across the network. When a
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


d.subroutine(0x9150, 'remote_cmd_data', title='Fn 8: remote OSWORD handler (NWORD)', description="""Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget -- no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")


d.subroutine(0x91CF, 'printer_select_handler', title='Fn 5: printer selection changed (SELECT)', description="""Called when the printer selection changes. Compares X against
the network printer buffer number (&F0). If it matches,
initialises the printer buffer pointer (&0D61 = &1F) and
sets the initial flag byte (&0D60 = &41). Otherwise falls
through to return.""", on_entry={'x': '1-based buffer number'})


d.subroutine(0x91DF, 'remote_print_handler', title='Fn 1/2/3: network printer handler (PRINT)', description="""Handles network printer output. Reason 1 = chars in buffer (extract
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


d.subroutine(0x9204, 'store_output_byte', title='Store output byte to network buffer', description="""Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""", on_entry={'a': 'byte to store'}, on_exit={'y': 'buffer offset before store'})


d.subroutine(0x9230, 'flush_output_block', title='Flush output block', description="""Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")


d.subroutine(0x92F2, 'save_vdu_state', title='Save VDU workspace state', description="""Stores the cursor position value from &0355 into NFS workspace,
then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
each result into consecutive workspace bytes.""")


d.subroutine(0x966F, 'adlc_init', title='ADLC initialisation', description="""Reads station ID (INTOFF side effect), performs full ADLC reset,
checks for Tube presence (OSBYTE &EA), then falls through to
adlc_init_workspace.""")


d.subroutine(0x968A, 'adlc_init_workspace', title='Initialise NMI workspace', description="""Issues OSBYTE &8F with X=&0C (NMI claim service request) before
copying the NMI shim. Sub-entry at &968A skips the service
request for quick re-init. Then copies 32 bytes of
NMI shim from ROM (&9FA8) to RAM (&0D00), patches the current
ROM bank number into the shim's self-modifying code at &0D07,
sets TX clear flag and econet_init_flag to &80, reads station ID
from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
and re-enables NMIs by reading &FE20 (INTON side effect).""")


d.subroutine(0x96C8, 'save_econet_state', title='Save Econet state to RX control block', description="""Stores rx_status_flags, protection_mask, and tx_in_progress
to (net_rx_ptr) at offsets 8-10. INTOFF side effect on entry.""")


d.subroutine(0x0016, 'tube_brk_handler', title='Tube BRK handler (BRKV target) — reference: NFS11 NEWBR', description="""Sends error information to the Tube co-processor via R2 and R4:
  1. Sends &FF to R4 (WRIFOR) to signal error
  2. Reads R2 data (flush any pending byte)
  3. Sends &00 via R2, then error number from (&FD),0
  4. Loops sending error string bytes via R2 until zero terminator
  5. Falls through to tube_reset_stack → tube_main_loop
The main loop continuously polls R1 for WRCH requests (forwarded
to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
12-entry table at &0500). The R2 command byte is stored at &55
before dispatch via JMP (&0500).""")


d.subroutine(0x0400, 'tube_code_page4', title='Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)', description="""Copied from ROM at &935D during init. The first 28 bytes (&0400-&041B)
overlap with the end of the ZP block (the same ROM bytes serve both
the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
  &0400: JMP &0473 (BEGIN — CLI parser / startup entry)
  &0403: JMP &06E2 (tube_escape_check)
  &0406: tube_addr_claim — Tube address claim protocol (ADRR)
  &0414: tube_post_init — called after ROM→RAM copy
  &0473: BEGIN — startup/CLI entry, break type check
  &04CB: tube_init_reloc — initialise relocation address for ROM transfer""")


d.subroutine(0x0500, 'tube_dispatch_table', title='Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)', description="""Copied from ROM at &9456 during init. Contains:
  &0500: tube_dispatch_table — 12-entry handler address table
  &0518: R2 command byte table — 8 even command bytes (&00-&0E)
  &0520: tube_osbput — write byte to file
  &052D: tube_osbget — read byte from file
  &0537: tube_osrdch — read character
  &053A: tube_rdch_reply — ROR carry into byte, send via R2
  &053D: tube_release_return — dead code (unreferenced)
  &0542: tube_osfind — open file
  &0552: tube_osfind_close — close file (A=0)
  &055E: tube_osargs — file argument read/write
  &0582: tube_read_string — read CR-terminated string into &0700
  &0596: tube_oscli — execute * command
  &059C: tube_reply_ack — send &7F acknowledge
  &059E: tube_reply_byte — send byte and return to main loop
  &05A9: tube_osfile — whole file operation""")


d.subroutine(0x9261, 'econet_tx_retry', title='Transmit with retry loop (XMITFS/XMITFY)', description="""Calls the low-level transmit routine (BRIANX) with FSTRY (&FF = 255)
retries and FSDELY (&60 = 96) ms delay between attempts. On each
iteration, checks the result code: zero means success, non-zero
means retry. After all retries exhausted, reports a 'Net error'.
Entry point XMITFY allows a custom delay in Y.""", on_entry={'a': 'handle bitmask (0=printer, non-zero=file)', 'x': 'TX control block address low', 'y': 'TX control block address high'})


d.subroutine(0x92A6, 'lang_2_save_palette_vdu', title='Save palette and VDU state (CVIEW)', description="""Part of the VIEW facility (second iteration, started 27/7/82).
Uses dynamically allocated buffer store. The WORKP1 pointer
(&9E,&9F) serves double duty: non-zero indicates data ready AND
provides the buffer address — an efficient use of scarce zero-
page space. This code must be user-transparent as the NFS may not
be the dominant filing system.
Reads all 16 palette entries using OSWORD &0B (read palette) and
stores the results. Then reads cursor position (OSBYTE &85),
shadow RAM allocation (OSBYTE &C2), and screen start address
(OSBYTE &C3) using the 3-entry table at &9319.
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")


d.subroutine(0x9992, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")


d.subroutine(0x9A56, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Handles immediate (non-data-transfer) operations received via
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


d.subroutine(0x9A2E, 'discard_reset_listen', title='Discard with full ADLC reset', description="""Performs adlc_full_reset (CR1=&C1, reset both TX and RX sections),
then falls through to install_rx_scout_handler. Used when the ADLC is
in an unexpected state and needs a hard reset before returning
to idle listen mode. 5 references — the main error recovery path.""")


d.subroutine(0x9A3D, 'discard_listen', title='Discard frame (gentle)', description="""Sends RX_DISCONTINUE (CR1=&A2: RIE|RX_DISCONTINUE) to abort the
current frame reception without a full reset, then falls through
to install_rx_scout_handler. Used for clean rejection of frames
that are correctly formatted but not for us (wrong station/network).""")
d.comment(0x9F28, 'Unreferenced data block (purpose unknown)')
d.byte(0x9F28, 16)


d.subroutine(0x9F38, 'tx_calc_transfer', title='Calculate transfer size', description="""Computes the number of bytes actually transferred during a data
frame reception. Subtracts the low pointer (LPTR, offset 4 in
the RXCB) from the current buffer position to get the byte count,
and stores it back into the RXCB's high pointer field (HPTR,
offset 8). This tells the caller how much data was received.""")
d.comment(0x9F38, 'Load RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x9F3D, 'AND with TX block[7] (byte 3)', align=Align.INLINE)
d.comment(0x9F3F, 'Both &FF = no buffer?', align=Align.INLINE)
d.comment(0x9F41, 'Yes: fallback path', align=Align.INLINE)
d.comment(0x9F43, 'Tube transfer in progress?', align=Align.INLINE)
d.comment(0x9F46, 'No: fallback path', align=Align.INLINE)
d.comment(0x9F4B, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x9F50, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9F51, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9F52, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x9F54, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x9F56, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x9F5A, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x9F5B, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x9F5D, 'Store result byte', align=Align.INLINE)
d.comment(0x9F60, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x9F63, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9F64, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x9F66, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9F68, 'Discard final borrow', align=Align.INLINE)
d.comment(0x9F69, 'A = saved X', align=Align.INLINE)
d.comment(0x9F6A, 'Save X', align=Align.INLINE)
d.comment(0x9F6B, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x9F70, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x9F71, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x9F73, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x9F78, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x9F7A, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x9F80, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x9F81, 'Restore X', align=Align.INLINE)
d.comment(0x9F86, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x9F8B, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x9F8D, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x9F91, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x9F99, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x9FA4, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x9FA6, 'Return with C=1', align=Align.INLINE)


d.subroutine(0x9FA8, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&96F2). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &96F2.""")


d.subroutine(0x9FB6, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""A version of the NMI vector-setting subroutine and RTI sequence
that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
one normally used at runtime; this ROM copy is used during early
initialisation before the RAM workspace has been set up, and as
the source for the initial copy to RAM.""")


d.subroutine(0x96D8, 'adlc_full_reset', title='ADLC full reset', description='Aborts all activity and returns to idle RX listen mode.')
d.comment(0x96D8, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x96E2, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)


d.subroutine(0x96E7, 'adlc_rx_listen', title='Enter RX listen mode', description='TX held in reset, RX active with interrupts. Clears all status.')
d.comment(0x96E7, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x96EC, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)


d.subroutine(0x96F2, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")
d.comment(0x96F2, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x96F4, 'BIT SR2: Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x96F7, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x96F9, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x96FC, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x96FF, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x9701, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x9703, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x9705, 'Flag &40 = broadcast frame', align=Align.INLINE)


d.subroutine(0x9711, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &9743.""")
d.comment(0x9711, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x9714, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x9716, 'Read destination network byte', align=Align.INLINE)
d.comment(0x9719, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x971B, 'EOR &FF: test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x971D, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x971F, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x9727, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x972A, 'Store Y offset for scout data buffer', align=Align.INLINE)


d.subroutine(0x9733, 'scout_error', title='Scout error/discard handler', description="""Reached when the scout data loop sees no RDA (BPL at &9748) or
when scout completion finds unexpected SR2 state.
Reads SR2 and tests AP|RDA bits. If non-zero, performs full
ADLC reset and discards. If zero (clean end), discards via scout_discard.
This path is a common landing for any unexpected ADLC state during
scout reception.""")
d.comment(0x9733, 'Read SR2', align=Align.INLINE)
d.comment(0x9736, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x973A, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x973D, 'Discard and return to idle', align=Align.INLINE)


d.subroutine(0x9743, 'scout_data_loop', title='Scout data reading loop', description="""Reads the body of a scout frame, two bytes per iteration. Stores
bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
Between each pair it checks SR2:
  - SR2 read at entry (&9745)
    - No RDA (BPL) -> error (&9733)
    - RDA set (BMI) -> read byte
  - After first byte (&9751): full SR2 tested
    - SR2 non-zero (BNE) -> scout completion (&976D)
      This is the FV detection point: when FV is set (by inline refill
      of the last byte during the preceding RX FIFO read), SR2 is
      non-zero and the branch is taken.
    - SR2 = 0 -> read second byte and loop
  - After second byte (&9765): re-test SR2 for next pair
    - RDA set (BMI) -> loop back to &974A
    - Neither set -> RTI, wait for next NMI
The loop ends at Y=&0C (12 bytes max in scout buffer).""")
d.comment(0x9743, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x9745, 'Read SR2', align=Align.INLINE)
d.comment(0x974A, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x974D, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x9750, 'Advance buffer index', align=Align.INLINE)
d.comment(0x9751, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x9754, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x9756, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x9758, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x975B, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x975E, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x9761, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x9765, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x9768, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x976A, 'SR2 = 0 -- RTI, wait for next NMI', align=Align.INLINE)


d.subroutine(0x976D, 'scout_complete', title='Scout completion handler', description="""Reached from the scout data loop when SR2 is non-zero (FV detected).
Disables PSE to allow individual SR2 bit testing:
  CR1=&00 (clear all enables)
  CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
Then checks FV (bit1) and RDA (bit7):
  - No FV (BEQ) -> error &9733 (not a valid frame end)
  - FV set, no RDA (BPL) -> error &9733 (missing last byte)
  - FV set, RDA set -> read last byte, process scout
After reading the last byte, the complete scout buffer (&0D3D-&0D48)
contains: src_stn, src_net, ctrl, port [, extra_data...].
The port byte at &0D40 determines further processing:
  - Port = 0 -> immediate operation (&9A6F)
  - Port non-zero -> check if it matches an open receive block""")
d.comment(0x976D, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x9772, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x9777, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9779, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x977C, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x977E, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x9780, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x9783, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x9786, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x978B, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x978E, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x9790, 'Port = 0 -- immediate operation handler', align=Align.INLINE)


d.subroutine(0x9821, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &9821 (AP+addr check) -> &9837 (net=0 check) ->
&984D (skip ctrl+port) -> &9880 (bulk data read) -> &98B4 (completion)""")
d.comment(0x9815, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x9837, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x984D, 'Skip control and port bytes (already known from scout)', align=Align.INLINE)
d.comment(0x9852, 'Discard control byte', align=Align.INLINE)
d.comment(0x9855, 'Discard port byte', align=Align.INLINE)


d.subroutine(0x9880, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &98B4.
SR2 = 0 -> RTI, wait for next NMI to continue.""")
d.comment(0x9880, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x9882, 'Read SR2 for next pair', align=Align.INLINE)


d.subroutine(0x98B4, 'data_rx_complete', title='Data frame completion', description="""Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&976D): disables PSE (CR1=&00,
CR2=&84), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &9944.""")
d.comment(0x98B4, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x98B9, 'CR2=&84: disable PSE for individual bit testing', align=Align.INLINE)
d.comment(0x98C0, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x98C2, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x98C5, 'No FV -- error', align=Align.INLINE)
d.comment(0x98C7, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x98CD, 'FV+RDA: read and store last data byte', align=Align.INLINE)


d.subroutine(0x9944, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&9F16).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x994F, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x9954, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9959, 'Install saved next handler (&99BB for scout ACK)', align=Align.INLINE)
d.comment(0x9963, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x9966, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9969, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x996B, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x996E, 'Write dest network to TX FIFO', align=Align.INLINE)


d.subroutine(0x997B, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x997B, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x997E, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x9981, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9983, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x9986, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x9990, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x9995, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)


d.subroutine(0x9C2F, 'inactive_poll', title='INACTIVE polling loop', description="""Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9C4D-&9C52 works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")
d.comment(0x9C34, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9C36, 'A=&04: INACTIVE mask for SR2 bit2', align=Align.INLINE)
d.comment(0x9C3A, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x9C3D, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x9C40, 'BIT SR2: Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x9C43, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x9C45, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x9C48, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9C4D, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x9C4F, 'BIT SR1: tests CTS present', align=Align.INLINE)
d.comment(0x9C52, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x9C54, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x9C58, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x9C6B, 'TX_ACTIVE branch (A=&44 = CR1 value for TX active)')


d.subroutine(0x9C6F, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")
d.comment(0x9C6F, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x9C77, "Error &40 = 'Line Jammed'", align=Align.INLINE)


d.subroutine(0x9C89, 'tx_prepare', title='TX preparation', description="""Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9D2D, and re-enables NMIs.""")
d.comment(0x9C89, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9C8C, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x9C9B, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)


d.subroutine(0x9D2D, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")
d.comment(0x9D2D, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x9D30, 'BIT SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x9D33, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x9D35, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x9D38, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x9D43, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x9D46, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x9D49, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9D4B, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x9D4E, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x9D50, 'RTI -- wait for next NMI', align=Align.INLINE)
d.comment(0x9D53, 'TX error path')
d.comment(0x9D53, 'Error &42', align=Align.INLINE)
d.comment(0x9D57, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x9D5C, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x9D5E, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x9D61, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)


d.subroutine(0x9D69, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &9D75 which switches to RX mode.
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)""")
d.comment(0x9D69, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)


d.subroutine(0x9D75, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> completion at &9F16
  - bit0 set at &0D4A -> four-way handshake data phase at &9EBA
  - Otherwise -> install RX reply handler at &9D93""")
d.comment(0x9D75, 'CR1=&82: TX_RESET | RIE (now in RX mode)', align=Align.INLINE)
d.comment(0x9D7A, 'Test workspace flags', align=Align.INLINE)
d.comment(0x9D7D, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x9D7F, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x9D89, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)


d.subroutine(0x9D93, 'nmi_reply_scout', title='RX reply scout handler', description="""Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")
d.comment(0x9D93, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x9D95, 'BIT SR2: test AP (Address Present)', align=Align.INLINE)
d.comment(0x9D98, 'No AP -- error', align=Align.INLINE)
d.comment(0x9D9D, 'Compare to our station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9DA0, 'Not our station -- error/reject', align=Align.INLINE)


d.subroutine(0x9DA9, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs &9DC2 for the
remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9DBA.
If IRQ is still set, falls through directly to &9DC2 without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")
d.comment(0x9DA9, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x9DAC, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9DAE, 'Read destination network byte', align=Align.INLINE)
d.comment(0x9DB1, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9DB7, 'BIT SR1: test IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x9DBC, 'IRQ not set -- install handler and RTI', align=Align.INLINE)


d.subroutine(0x9DC2, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &9DC2 -- must see data available
  2. Read source station at &9DC7, compare to &0D20 (tx_dst_stn)
  3. Read source network at &9DCF, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &9DD9 -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")
d.comment(0x9DC2, 'BIT SR2: test RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x9DC5, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x9DC7, 'Read source station', align=Align.INLINE)
d.comment(0x9DCA, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x9DCD, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x9DCF, 'Read source network', align=Align.INLINE)
d.comment(0x9DD2, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x9DD5, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9DD7, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9DD9, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9DDC, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x9DDE, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x9DE3, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x9DE8, 'Install next handler at &9EBA into &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x9DF2, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x9DF5, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9DF8, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9DFA, 'Write dest station to TX FIFO', align=Align.INLINE)


d.subroutine(0x9E0A, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
d.comment(0x9E12, 'Write our station to TX FIFO', align=Align.INLINE)


d.subroutine(0x9E2F, 'nmi_data_tx', title='TX data phase: send payload', description="""Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9D2D but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
d.comment(0x9E2F, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x9E31, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9E34, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E36, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E5C, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)


d.subroutine(0x9EBA, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9EC6 to receive the final ACK from the remote station.""")
d.comment(0x9EBA, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)


d.subroutine(0x9EC6, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9D93-&9DC2):
  &9EC6: Check AP, read dest_stn, compare to our station
  &9EDC: Check RDA, read dest_net, validate = 0
  &9EF2: Check RDA, read src_stn/net, compare to TX dest
  &9F0F: Check FV for frame completion
On success, stores result=0 at &9F16. On any failure, error &41.""")
d.comment(0x9EC6, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x9EC8, 'BIT SR2: test AP', align=Align.INLINE)
d.comment(0x9ECB, 'No AP -- error', align=Align.INLINE)
d.comment(0x9ECD, 'Read dest station', align=Align.INLINE)
d.comment(0x9ED0, 'Compare to our station (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9ED3, 'Not our station -- error', align=Align.INLINE)
d.comment(0x9EDC, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9EDF, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9EE1, 'Read dest network', align=Align.INLINE)
d.comment(0x9EE4, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9EEA, 'BIT SR1: test IRQ -- more data ready?', align=Align.INLINE)


d.subroutine(0x9EF2, 'nmi_final_ack_validate', title='Final ACK validation', description="""Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
d.comment(0x9EF2, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9EF5, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9EF7, 'Read source station', align=Align.INLINE)
d.comment(0x9EFA, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x9EFD, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9EFF, 'Read source network', align=Align.INLINE)
d.comment(0x9F02, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x9F05, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9F0F, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9F11, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9F14, 'No FV -- error', align=Align.INLINE)


d.subroutine(0x9F16, 'tx_result_ok', title='TX completion handler', description="""Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls full ADLC reset + idle listen via &9A2E.""")
d.comment(0x9F16, 'A=0: success result code', align=Align.INLINE)
d.comment(0x9F18, 'BEQ: always taken (A=0)', align=Align.INLINE)


d.subroutine(0x9F1C, 'tx_store_result', title='TX error handler', description="""Stores error code (A) into the TX control block, sets &0D3A bit7
for completion, and returns to idle via &9A2E.
Error codes: &00=success, &40=line jammed, &41=not listening,
&42=net error.""")
d.comment(0x9F1C, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x9F1E, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x9F20, '&80: completion flag for &0D3A', align=Align.INLINE)
d.comment(0x9F22, 'Signal TX complete', align=Align.INLINE)
d.comment(0x9F25, 'Full ADLC reset and return to idle listen', align=Align.INLINE)

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

d.label(0x0054, 'tube_xfer_page')

d.label(0x0055, 'tube_xfer_addr_2')

d.label(0x0056, 'tube_xfer_addr_3')

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
d.comment(0x0420, 'Store to claim-in-progress flag', align=Align.INLINE)
d.comment(0x0422, 'Return from tube_post_init', align=Align.INLINE)

d.label(0x0423, 'addr_claim_external')
d.comment(0x0423, "Another host claiming; check if we're owner", align=Align.INLINE)
d.comment(0x0425, 'C=1: we have an active claim', align=Align.INLINE)
d.comment(0x0427, 'Compare with our claimed address', align=Align.INLINE)
d.comment(0x0429, 'Match: return (we already have it)', align=Align.INLINE)
d.comment(0x042B, "Not ours: CLC = we don't own this address", align=Align.INLINE)
d.comment(0x042C, 'Return with C=0 (claim denied)', align=Align.INLINE)

d.label(0x042D, 'accept_new_claim')
d.comment(0x042D, 'Accept new claim: update our address', align=Align.INLINE)
d.comment(0x042F, 'Return with address updated', align=Align.INLINE)

d.label(0x0430, 'tube_transfer_setup')
d.comment(0x0430, 'PHP: save interrupt state', align=Align.INLINE)
d.comment(0x0431, 'SEI: disable interrupts for R4 protocol', align=Align.INLINE)
d.comment(0x0432, 'Save 16-bit transfer address from (X,Y)', align=Align.INLINE)
d.comment(0x0434, 'Store address pointer low byte', align=Align.INLINE)
d.comment(0x0436, 'Send transfer type byte to co-processor', align=Align.INLINE)
d.comment(0x0439, 'X = transfer type for table lookup', align=Align.INLINE)
d.comment(0x043A, 'Y=3: send 4 bytes (address + claimed addr)', align=Align.INLINE)
d.comment(0x043C, 'Send our claimed address + 4-byte xfer addr', align=Align.INLINE)

d.label(0x0441, 'send_xfer_addr_bytes')
d.comment(0x0441, 'Load transfer address byte from (X,Y)', align=Align.INLINE)
d.comment(0x0443, 'Send address byte to co-processor via R4', align=Align.INLINE)
d.comment(0x0446, 'Previous byte (big-endian: 3,2,1,0)', align=Align.INLINE)
d.comment(0x0447, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x044C, 'Y=&18: enable Tube control register', align=Align.INLINE)
d.comment(0x044E, 'Enable Tube interrupt generation', align=Align.INLINE)
d.comment(0x0451, 'Look up Tube control bits for this xfer type', align=Align.INLINE)
d.comment(0x0454, 'Apply transfer-specific control bits', align=Align.INLINE)
d.comment(0x0457, 'LSR: check bit 2 (2-byte flush needed?)', align=Align.INLINE)
d.comment(0x0458, 'LSR: shift bit 2 to carry', align=Align.INLINE)

d.label(0x0459, 'poll_r4_copro_ack')
d.comment(0x0459, 'Poll R4 status for co-processor response', align=Align.INLINE)
d.comment(0x045C, 'Bit 6 clear: not ready, keep polling', align=Align.INLINE)
d.comment(0x045E, 'R4 bit 7: co-processor acknowledged transfer', align=Align.INLINE)
d.comment(0x0460, 'Type 4 = SENDW (host-to-parasite word xfer)', align=Align.INLINE)
d.comment(0x0462, 'Not SENDW type: skip release path', align=Align.INLINE)

d.label(0x0464, 'tube_sendw_complete')
d.comment(0x0464, 'SENDW complete: release, sync, restart', align=Align.INLINE)
d.comment(0x0467, 'Sync via R2 send', align=Align.INLINE)
d.comment(0x046A, 'Restart Tube main loop', align=Align.INLINE)

d.label(0x0473, 'copro_ack_nmi_check')
d.comment(0x0473, 'LSR: check bit 0 (NMI used?)', align=Align.INLINE)
d.comment(0x0474, 'C=0: NMI not used, skip NMI release', align=Align.INLINE)
d.comment(0x0476, 'Release Tube NMI (transfer used interrupts)', align=Align.INLINE)
d.comment(0x0478, 'Write &88 to Tube control to release NMI', align=Align.INLINE)

d.label(0x047B, 'skip_nmi_release')
d.comment(0x047B, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x047C, 'Return from transfer setup', align=Align.INLINE)

d.label(0x047D, 'tube_begin')
d.comment(0x047D, 'BEGIN: enable interrupts for Tube host code', align=Align.INLINE)
d.comment(0x047E, 'C=1: hard break, claim addr &FF', align=Align.INLINE)
d.comment(0x0480, 'C=0, A!=0: re-init path', align=Align.INLINE)
d.comment(0x0482, 'Z=1 from C=0 path: just acknowledge', align=Align.INLINE)

d.label(0x0485, 'check_break_type')
d.comment(0x0485, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x0487, 'Y=&FF for OSBYTE', align=Align.INLINE)
d.comment(0x0489, 'OSBYTE &FD: what type of reset was this?', align=Align.INLINE)
d.comment(0x048F, 'Soft break (X=0): re-init Tube and restart', align=Align.INLINE)

d.label(0x0491, 'claim_addr_ff')
d.comment(0x0491, 'Claim address &FF (startup = highest prio)', align=Align.INLINE)
d.comment(0x0493, 'Request address claim from Tube system', align=Align.INLINE)
d.comment(0x0496, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x0498, 'Init reloc pointers from ROM header', align=Align.INLINE)

d.label(0x049B, 'next_rom_page')
d.comment(0x049B, 'R4 cmd 7: SENDW to send ROM to parasite', align=Align.INLINE)
d.comment(0x049D, 'Set up Tube for SENDW transfer', align=Align.INLINE)
d.comment(0x04A0, 'Y=0: start at beginning of page', align=Align.INLINE)
d.comment(0x04A2, 'Store to zero page pointer low byte', align=Align.INLINE)

d.label(0x04A4, 'send_rom_page_bytes')
d.comment(0x04A4, 'Send 256-byte page via R3, byte at a time', align=Align.INLINE)
d.comment(0x04A6, 'Write byte to Tube R3 data register', align=Align.INLINE)
d.comment(0x04AC, 'Next byte in page', align=Align.INLINE)
d.comment(0x04AD, 'Loop for all 256 bytes', align=Align.INLINE)
d.comment(0x04AF, 'Increment 24-bit destination addr', align=Align.INLINE)
d.comment(0x04B1, 'No carry: skip higher bytes', align=Align.INLINE)
d.comment(0x04B3, 'Carry into second byte', align=Align.INLINE)
d.comment(0x04B5, 'No carry: skip third byte', align=Align.INLINE)
d.comment(0x04B7, 'Carry into third byte', align=Align.INLINE)

d.label(0x04B9, 'skip_addr_carry')
d.comment(0x04B9, 'Increment page counter', align=Align.INLINE)
d.comment(0x04BB, 'Bit 6 set = all pages transferred', align=Align.INLINE)
d.comment(0x04BD, 'More pages: loop back to SENDW', align=Align.INLINE)
d.comment(0x04BF, 'Re-init reloc pointers for final claim', align=Align.INLINE)
d.comment(0x04C2, 'A=4: transfer type for final address claim', align=Align.INLINE)

d.label(0x04C4, 'tube_claim_default')
d.comment(0x04C4, 'Y=0: transfer address low byte', align=Align.INLINE)
d.comment(0x04C6, 'X=&53: transfer address high byte (&0053)', align=Align.INLINE)
d.comment(0x04C8, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x04CB, 'Init: start sending from &8000', align=Align.INLINE)
d.comment(0x04CD, 'Store &80 as source page high byte', align=Align.INLINE)
d.comment(0x04CF, 'Store &80 as page counter initial value', align=Align.INLINE)
d.comment(0x04D1, 'A=&20: bit 5 mask for ROM type check', align=Align.INLINE)
d.comment(0x04D3, 'ROM type bit 5: reloc address in header?', align=Align.INLINE)
d.comment(0x04D6, 'Y = 0 or &20 (reloc flag)', align=Align.INLINE)
d.comment(0x04D7, 'Store as transfer address selector', align=Align.INLINE)
d.comment(0x04D9, 'No reloc addr: use defaults', align=Align.INLINE)
d.comment(0x04DB, 'Skip past copyright string to find reloc addr', align=Align.INLINE)

d.label(0x04DE, 'scan_copyright_end')
d.comment(0x04DE, 'Skip past null-terminated copyright string', align=Align.INLINE)
d.comment(0x04DF, 'Load next byte from ROM header', align=Align.INLINE)
d.comment(0x04E2, 'Loop until null terminator found', align=Align.INLINE)
d.comment(0x04E4, 'Read 4-byte reloc address from ROM header', align=Align.INLINE)
d.comment(0x04E7, 'Store reloc addr byte 1 as transfer addr', align=Align.INLINE)
d.comment(0x04E9, 'Load reloc addr byte 2', align=Align.INLINE)
d.comment(0x04EC, 'Store as source page start', align=Align.INLINE)
d.comment(0x04EE, 'Load reloc addr byte 3', align=Align.INLINE)
d.comment(0x04F1, 'Load reloc addr byte 4 (highest)', align=Align.INLINE)

d.label(0x04F4, 'store_xfer_end_addr')
d.comment(0x04F4, 'Store high byte of end address', align=Align.INLINE)
d.comment(0x04F6, 'Store byte 3 of end address', align=Align.INLINE)
d.comment(0x04F8, 'Return with pointers initialised', align=Align.INLINE)
d.comment(0x0523, 'Y=channel handle from R2', align=Align.INLINE)
d.comment(0x0524, 'Read data byte from R2 for BPUT', align=Align.INLINE)
d.comment(0x052A, 'BPUT done: send acknowledge, return', align=Align.INLINE)
d.comment(0x0530, 'Y=channel handle for OSBGET', align=Align.INLINE)
d.comment(0x0534, 'Send carry+byte reply (BGET result)', align=Align.INLINE)
d.comment(0x053A, 'ROR A: encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x053F, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x0545, 'A=0: close file, else open with filename', align=Align.INLINE)
d.comment(0x0547, 'Save open mode while reading filename', align=Align.INLINE)
d.comment(0x0548, 'Read filename string from R2 into &0700', align=Align.INLINE)
d.comment(0x054B, 'Recover open mode from stack', align=Align.INLINE)
d.comment(0x054F, 'Send file handle result to co-processor', align=Align.INLINE)
d.comment(0x0552, 'OSFIND close: read handle from R2', align=Align.INLINE)
d.comment(0x0555, 'Y=handle to close', align=Align.INLINE)
d.comment(0x0556, 'A=0: close command for OSFIND', align=Align.INLINE)
d.comment(0x055B, 'Close done: send acknowledge, return', align=Align.INLINE)
d.comment(0x0561, 'Y=file handle for OSARGS', align=Align.INLINE)
d.comment(0x0562, 'Read 4-byte arg + reason from R2 into ZP', align=Align.INLINE)

d.label(0x0564, 'read_osargs_params')
d.comment(0x0564, 'Read next param byte from R2', align=Align.INLINE)
d.comment(0x0567, 'Params stored at &00-&03 (little-endian)', align=Align.INLINE)
d.comment(0x0569, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x056A, 'Loop for 4 bytes', align=Align.INLINE)
d.comment(0x056C, 'Read OSARGS reason code from R2', align=Align.INLINE)
d.comment(0x0572, 'Send result A back to co-processor', align=Align.INLINE)
d.comment(0x0575, 'Return 4-byte result from ZP &00-&03', align=Align.INLINE)

d.label(0x0577, 'send_osargs_result')
d.comment(0x0577, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x0579, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x057C, 'Previous byte (count down)', align=Align.INLINE)
d.comment(0x057D, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x057F, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x0582, 'X=0: initialise string buffer index', align=Align.INLINE)
d.comment(0x0584, 'Y=0: string buffer offset 0', align=Align.INLINE)
d.comment(0x0586, 'Read next string byte from R2', align=Align.INLINE)
d.comment(0x0589, 'Store byte in string buffer at &0700+Y', align=Align.INLINE)
d.comment(0x058C, 'Next buffer position', align=Align.INLINE)
d.comment(0x058D, 'Y overflow: string too long, truncate', align=Align.INLINE)
d.comment(0x058F, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x0591, 'Not CR: continue reading string', align=Align.INLINE)

d.label(0x0593, 'string_buf_done')
d.comment(0x0593, 'Y=7: set XY=&0700 for OSCLI/OSFIND', align=Align.INLINE)
d.comment(0x0595, 'Return with XY pointing to &0700', align=Align.INLINE)
d.comment(0x0599, 'Execute * command via OSCLI', align=Align.INLINE)
d.comment(0x059C, '&7F = success acknowledgement', align=Align.INLINE)
d.comment(0x059E, 'Poll R2 status until ready', align=Align.INLINE)
d.comment(0x05A1, 'Bit 6 clear: not ready, loop', align=Align.INLINE)
d.comment(0x05A3, 'Write byte to R2 data register', align=Align.INLINE)
d.comment(0x05A6, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x05AB, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05AE, 'Store at &01+X (descending)', align=Align.INLINE)
d.comment(0x05B0, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05B1, 'Loop for all 16 bytes', align=Align.INLINE)
d.comment(0x05B3, 'Read filename string from R2 into &0700', align=Align.INLINE)
d.comment(0x05B6, 'XY=&0700: filename pointer for OSFILE', align=Align.INLINE)
d.comment(0x05B8, 'Store Y=7 as pointer high byte', align=Align.INLINE)
d.comment(0x05BA, 'Y=0 for OSFILE control block offset', align=Align.INLINE)
d.comment(0x05BC, 'Read OSFILE reason code from R2', align=Align.INLINE)
d.comment(0x05BF, 'Execute OSFILE operation', align=Align.INLINE)
d.comment(0x05C2, 'Send result A (object type) to co-processor', align=Align.INLINE)
d.comment(0x05C5, 'Return 16-byte control block to co-processor', align=Align.INLINE)

d.label(0x05C7, 'send_osfile_ctrl_blk')
d.comment(0x05C7, 'Load control block byte', align=Align.INLINE)
d.comment(0x05C9, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05CC, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05CD, 'Loop for all 16 bytes', align=Align.INLINE)
d.comment(0x05CF, 'ALWAYS branch to main loop', align=Align.INLINE)
d.comment(0x05D1, 'Read 13-byte OSGBPB control block from R2', align=Align.INLINE)

d.label(0x05D3, 'read_osgbpb_ctrl_blk')
d.comment(0x05D3, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05D6, 'Store at &FF+X (descending into &00-&0C)', align=Align.INLINE)
d.comment(0x05D8, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05D9, 'Loop for all 13 bytes', align=Align.INLINE)
d.comment(0x05DB, 'Read OSGBPB reason code from R2', align=Align.INLINE)
d.comment(0x05DE, 'Y=0 for OSGBPB control block', align=Align.INLINE)
d.comment(0x05E3, 'Save A (completion status) for later', align=Align.INLINE)
d.comment(0x05E4, 'Return 13-byte result block to co-processor', align=Align.INLINE)

d.label(0x05E6, 'send_osgbpb_result')
d.comment(0x05E6, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x05E8, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05EB, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05EC, 'Loop for 13 bytes (X=12..0)', align=Align.INLINE)
d.comment(0x05EE, 'Recover completion status from stack', align=Align.INLINE)
d.comment(0x05EF, 'Send carry+status as RDCH-style reply', align=Align.INLINE)
d.comment(0x05F5, 'X = first parameter', align=Align.INLINE)
d.comment(0x05F6, 'Read A (OSBYTE number) from R2', align=Align.INLINE)
d.comment(0x05F9, 'Execute OSBYTE call', align=Align.INLINE)

d.label(0x05FC, 'tube_poll_r2_result')
d.comment(0x05FC, 'Poll R2 status for result send', align=Align.INLINE)

d.label(0x0600, 'tube_page6_start')
d.comment(0x0601, 'Send X result for 2-param OSBYTE', align=Align.INLINE)
d.comment(0x0617, 'OSBYTE &9D (fast Tube BPUT): no result needed', align=Align.INLINE)
d.comment(0x0619, 'Encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x0622, 'Send Y result, then fall through to send X', align=Align.INLINE)
d.comment(0x0626, 'Send X result via R2 (data overlap with &70=BVS)', align=Align.INLINE)
d.comment(0x0628, 'Read OSWORD number from R2', align=Align.INLINE)
d.comment(0x062A, 'Save OSWORD number in Y', align=Align.INLINE)
d.comment(0x0630, 'Read param block length from R2', align=Align.INLINE)
d.comment(0x0633, 'DEX: length 0 means no params to read', align=Align.INLINE)
d.comment(0x063E, 'Store param bytes into block at &0128', align=Align.INLINE)
d.comment(0x0644, 'Restore OSWORD number from Y', align=Align.INLINE)

d.label(0x0645, 'skip_param_read')
d.comment(0x0645, 'XY=&0128: param block address for OSWORD', align=Align.INLINE)

d.label(0x064C, 'poll_r2_osword_result')
d.comment(0x0651, 'Read result block length from R2', align=Align.INLINE)
d.comment(0x0655, 'No results to send: return to main loop', align=Align.INLINE)
d.comment(0x0657, 'Send result block bytes from &0128 via R2', align=Align.INLINE)

d.label(0x066A, 'read_rdln_ctrl_block')
d.comment(0x0672, 'X=0 after loop, A=0 for OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x0679, 'C=0: line read OK; C=1: escape pressed', align=Align.INLINE)
d.comment(0x067B, '&FF = escape/error signal to co-processor', align=Align.INLINE)
d.comment(0x0682, '&7F = line read successfully', align=Align.INLINE)
d.comment(0x068E, 'Check for CR terminator', align=Align.INLINE)
d.comment(0x06A7, 'Check OS escape flag at &FF', align=Align.INLINE)
d.comment(0x06A9, 'SEC+ROR: put bit 7 of &FF into carry+bit 7', align=Align.INLINE)
d.comment(0x06AB, 'Escape set: forward to co-processor via R1', align=Align.INLINE)
d.comment(0x06AD, 'EVNTV: forward event A, Y, X to co-processor', align=Align.INLINE)
d.comment(0x06AE, 'Send &00 prefix (event notification)', align=Align.INLINE)

d.label(0x06C5, 'tube_read_r2')

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
d.comment(0x8073, 'Command index >= 4: invalid *NET sub-command', align=Align.INLINE)
d.comment(0x8075, 'Out of range: return via c80e3/RTS', align=Align.INLINE)
d.comment(0x8077, 'X = command index (0-3)', align=Align.INLINE)
d.comment(0x8078, 'Clear &A9 (used by dispatch)', align=Align.INLINE)
d.comment(0x807A, 'Store zero to &A9', align=Align.INLINE)
d.comment(0x807C, 'Preserve A before dispatch', align=Align.INLINE)
d.comment(0x807F, 'ALWAYS branch to dispatch', align=Align.INLINE)

d.label(0x8081, 'skip_cmd_spaces')
d.comment(0x8082, 'Load next char from command line', align=Align.INLINE)
d.comment(0x8084, 'Skip spaces', align=Align.INLINE)
d.comment(0x8086, 'Loop back to skip leading spaces', align=Align.INLINE)
d.comment(0x8088, 'Colon = interactive remote command prefix', align=Align.INLINE)
d.comment(0x808A, "Char >= ':': skip number parsing", align=Align.INLINE)
d.comment(0x808F, 'C=1: dot found, first number was network', align=Align.INLINE)
d.comment(0x8091, 'Store network number (n.s = network.station)', align=Align.INLINE)

d.label(0x8098, 'got_station_num')
d.comment(0x8098, 'Z=1: no station parsed (empty or non-numeric)', align=Align.INLINE)

d.label(0x809D, 'skip_stn_parse')
d.comment(0x809D, 'Copy command text to FS buffer', align=Align.INLINE)

d.label(0x80A0, 'scan_for_colon')
d.comment(0x80A0, "Scan backward for ':' (interactive prefix)", align=Align.INLINE)
d.comment(0x80A1, 'Y=0: no colon found, send command', align=Align.INLINE)
d.comment(0x80A3, 'Read char from FS command buffer', align=Align.INLINE)
d.comment(0x80A6, 'Test for colon separator', align=Align.INLINE)
d.comment(0x80A8, 'Not colon: keep scanning backward', align=Align.INLINE)
d.comment(0x80AA, 'Echo colon, then read user input from keyboard', align=Align.INLINE)

d.label(0x80AD, 'read_remote_cmd_line')
d.comment(0x80AD, 'Check for escape condition', align=Align.INLINE)
d.comment(0x80B3, 'Append typed character to command buffer', align=Align.INLINE)
d.comment(0x80B6, 'Advance write pointer', align=Align.INLINE)
d.comment(0x80B7, 'Increment character count', align=Align.INLINE)
d.comment(0x80B8, 'Test for CR (end of line)', align=Align.INLINE)
d.comment(0x80BA, 'Not CR: continue reading input', align=Align.INLINE)
d.comment(0x80BF, 'After OSNEWL: loop back to scan for colon', align=Align.INLINE)

d.label(0x80C5, 'prepare_cmd_dispatch')
d.comment(0x80E1, 'X >= 5: invalid reason code, return', align=Align.INLINE)

d.label(0x80E3, 'svc_dispatch_range')
d.comment(0x80E3, 'Out of range: return via RTS', align=Align.INLINE)
d.comment(0x80E8, 'Decrement base offset counter', align=Align.INLINE)
d.comment(0x80E9, 'Loop until Y exhausted', align=Align.INLINE)
d.comment(0x80EB, 'Y=&FF (no further use)', align=Align.INLINE)
d.comment(0x80F7, '9 NOPs: bus settling time for ADLC probe', align=Align.INLINE)
d.comment(0x8100, 'Save service call number', align=Align.INLINE)
d.comment(0x8119, 'C into bit 7 of A', align=Align.INLINE)
d.comment(0x811A, 'Restore service call number', align=Align.INLINE)
d.comment(0x811B, 'Service >= &80: always handle (Tube/init)', align=Align.INLINE)
d.comment(0x811D, 'C=1 (no ADLC): disable ROM, skip', align=Align.INLINE)

d.label(0x811F, 'check_svc_high')
d.comment(0x811F, 'Service >= &FE?', align=Align.INLINE)
d.comment(0x8121, 'Service < &FE: skip to &12/dispatch check', align=Align.INLINE)
d.comment(0x8123, 'Service &FF: full init (vectors + RAM copy)', align=Align.INLINE)
d.comment(0x8125, 'Service &FE: Y=0?', align=Align.INLINE)
d.comment(0x8127, 'Y=0: no Tube data, skip to &12 check', align=Align.INLINE)
d.comment(0x8129, 'X=6 extra pages for char definitions', align=Align.INLINE)
d.comment(0x812B, 'OSBYTE &14: explode character RAM', align=Align.INLINE)

d.label(0x8130, 'poll_tube_ready')
d.comment(0x8130, 'Poll Tube status register 1', align=Align.INLINE)
d.comment(0x8133, 'Loop until Tube ready (bit 7 set)', align=Align.INLINE)
d.comment(0x8135, 'Read byte from Tube data register 1', align=Align.INLINE)
d.comment(0x8138, 'Zero byte: Tube transfer complete', align=Align.INLINE)
d.comment(0x813A, 'Send Tube char to screen via OSWRCH', align=Align.INLINE)
d.comment(0x813D, 'Loop for next Tube byte', align=Align.INLINE)
d.comment(0x8140, 'EVNTV low = &AD (event handler address)', align=Align.INLINE)
d.comment(0x8142, 'Set EVNTV low byte at &0220', align=Align.INLINE)
d.comment(0x8145, 'EVNTV high = &06 (page 6)', align=Align.INLINE)
d.comment(0x8147, 'Set EVNTV high byte at &0221', align=Align.INLINE)
d.comment(0x814A, 'BRKV low = &16 (NMI workspace)', align=Align.INLINE)
d.comment(0x814C, 'Set BRKV low byte at &0202', align=Align.INLINE)
d.comment(0x814F, 'BRKV high = &00 (zero page)', align=Align.INLINE)
d.comment(0x8151, 'Set BRKV high byte at &0203', align=Align.INLINE)
d.comment(0x8154, 'Tube control register init value &8E', align=Align.INLINE)
d.comment(0x8156, 'Write to Tube control register', align=Align.INLINE)
d.comment(0x8159, 'Y=0: copy 256 bytes per page', align=Align.INLINE)
d.comment(0x815B, 'Load ROM byte from page &93', align=Align.INLINE)
d.comment(0x815E, 'Store to page &04 (Tube code)', align=Align.INLINE)
d.comment(0x8161, 'Load ROM byte from page &94', align=Align.INLINE)
d.comment(0x8164, 'Store to page &05 (dispatch table)', align=Align.INLINE)
d.comment(0x8167, 'Load ROM byte from page &95', align=Align.INLINE)
d.comment(0x816A, 'Store to page &06', align=Align.INLINE)
d.comment(0x816D, 'DEY wraps 0 -> &FF on first iteration', align=Align.INLINE)
d.comment(0x816E, 'Loop until 256 bytes copied per page', align=Align.INLINE)
d.comment(0x8170, 'Run post-init routine in copied code', align=Align.INLINE)
d.comment(0x8173, 'X=&60: copy 97 bytes (&60..&00)', align=Align.INLINE)

d.label(0x8175, 'copy_nmi_workspace')
d.comment(0x8175, 'Load NMI workspace init byte from ROM', align=Align.INLINE)
d.comment(0x8178, 'Store to zero page &16+X', align=Align.INLINE)
d.comment(0x817A, 'Next byte', align=Align.INLINE)
d.comment(0x817B, 'Loop until all workspace bytes copied', align=Align.INLINE)

d.label(0x817D, 'tube_chars_done')
d.comment(0x817D, 'A=0: fall through to service &12 check', align=Align.INLINE)

d.label(0x817F, 'check_svc_12')
d.comment(0x817F, 'Is this service &12 (select FS)?', align=Align.INLINE)
d.comment(0x8181, 'No: check if service < &0D', align=Align.INLINE)
d.comment(0x8183, 'Service &12: Y=5 (NFS)?', align=Align.INLINE)
d.comment(0x8185, 'Not NFS: check if service < &0D', align=Align.INLINE)
d.comment(0x8187, 'A=&0D: dispatch index for svc_13_select_nfs', align=Align.INLINE)
d.comment(0x8189, 'ALWAYS branch to dispatch', align=Align.INLINE)

d.label(0x818B, 'not_svc_12_nfs')
d.comment(0x818B, 'Service >= &0D?', align=Align.INLINE)

d.label(0x818D, 'svc_unhandled_return')
d.comment(0x818D, 'Service >= &0D: not handled, return', align=Align.INLINE)

d.label(0x818F, 'do_svc_dispatch')
d.comment(0x818F, 'X = service number (dispatch index)', align=Align.INLINE)
d.comment(0x8190, 'Save &A9 (current service state)', align=Align.INLINE)
d.comment(0x8192, 'Push saved &A9', align=Align.INLINE)
d.comment(0x8193, 'Save &A8 (workspace page number)', align=Align.INLINE)
d.comment(0x8195, 'Push saved &A8', align=Align.INLINE)
d.comment(0x8196, 'Store service number to &A9', align=Align.INLINE)
d.comment(0x8198, 'Store Y (page number) to &A8', align=Align.INLINE)
d.comment(0x819A, 'A = Y for dispatch table offset', align=Align.INLINE)
d.comment(0x819B, 'Y=0: base offset for service dispatch', align=Align.INLINE)
d.comment(0x819D, 'Dispatch to service handler', align=Align.INLINE)
d.comment(0x81A0, 'Recover service claim status from &A9', align=Align.INLINE)
d.comment(0x81A2, 'Restore saved &A8 from stack', align=Align.INLINE)
d.comment(0x81A3, 'Write back &A8', align=Align.INLINE)
d.comment(0x81A5, 'Restore saved A from service dispatch', align=Align.INLINE)
d.comment(0x81A6, 'Save to workspace &A9', align=Align.INLINE)
d.comment(0x81A8, 'Return ROM number in A', align=Align.INLINE)
d.comment(0x81A9, 'Restore X from MOS ROM select copy', align=Align.INLINE)
d.comment(0x81AC, 'Padding: dispatch targets &81B1', align=Align.INLINE)
d.comment(0x81B1, 'ROM offset for "ROFF" (copyright suffix)', align=Align.INLINE)
d.comment(0x81B3, 'Try matching *ROFF command', align=Align.INLINE)
d.comment(0x81B6, 'No match: try *NET', align=Align.INLINE)
d.comment(0x81B8, 'Y=4: offset of keyboard disable flag', align=Align.INLINE)
d.comment(0x81BA, 'Read flag from RX buffer', align=Align.INLINE)
d.comment(0x81BC, 'Zero: keyboard not disabled, skip', align=Align.INLINE)
d.comment(0x81BE, 'A=0: value to clear flag and re-enable', align=Align.INLINE)
d.comment(0x81C1, 'Clear keyboard disable flag in buffer', align=Align.INLINE)
d.comment(0x81C4, 'OSBYTE &C9: Econet keyboard disable', align=Align.INLINE)
d.comment(0x81C6, 'Re-enable keyboard (X=0, Y=0)', align=Align.INLINE)
d.comment(0x81C9, 'Function &0A: remote operation complete', align=Align.INLINE)
d.comment(0x81CB, 'Send notification to controlling station', align=Align.INLINE)
d.comment(0x81CE, 'Save X (return value from TX)', align=Align.INLINE)
d.comment(0x81D0, 'OSBYTE &CE: first system mask to reset', align=Align.INLINE)

d.label(0x81D2, 'clear_osbyte_masks')
d.comment(0x81D2, 'Restore X for OSBYTE call', align=Align.INLINE)
d.comment(0x81D4, 'Y=&7F: AND mask (clear bit 7)', align=Align.INLINE)
d.comment(0x81D6, 'Reset system mask byte', align=Align.INLINE)
d.comment(0x81D9, 'Advance to next OSBYTE (&CE -> &CF)', align=Align.INLINE)
d.comment(0x81DB, 'Reached &D0? (past &CF)', align=Align.INLINE)
d.comment(0x81DD, 'No: reset &CF too', align=Align.INLINE)

d.label(0x81DF, 'skip_kbd_reenable')
d.comment(0x81DF, 'A=0: clear remote state', align=Align.INLINE)
d.comment(0x81E1, 'Clear &A9 (service dispatch state)', align=Align.INLINE)
d.comment(0x81E3, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x81E5, 'Return', align=Align.INLINE)

d.label(0x81E6, 'match_net_cmd')
d.comment(0x81E6, 'X=5: ROM offset for "NET" match', align=Align.INLINE)
d.comment(0x81E8, 'Try matching *NET command', align=Align.INLINE)
d.comment(0x81EB, 'No match: return unclaimed', align=Align.INLINE)
d.comment(0x81ED, 'Notify current FS of shutdown (FSCV A=6)', align=Align.INLINE)
d.comment(0x81F0, 'C=1 for ROR', align=Align.INLINE)
d.comment(0x81F1, 'Set bit 7 of l00a8 (inhibit auto-boot)', align=Align.INLINE)
d.comment(0x81F3, 'Claim OS vectors, issue service &0F', align=Align.INLINE)
d.comment(0x81F6, 'Y=&1D: top of FS state range', align=Align.INLINE)
d.comment(0x81F8, 'Copy FS state from RX buffer...', align=Align.INLINE)
d.comment(0x81FA, '...to workspace (offsets &15-&1D)', align=Align.INLINE)
d.comment(0x81FD, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x81FE, 'Loop until offset &14 done', align=Align.INLINE)
d.comment(0x8200, 'Continue loop', align=Align.INLINE)
d.comment(0x8202, 'ALWAYS branch to init_fs_vectors', align=Align.INLINE)
d.comment(0x8204, 'Print ROM identification string', align=Align.INLINE)
d.comment(0x8213, 'Return (service not claimed)', align=Align.INLINE)
d.comment(0x8214, 'FSCV reason 6 = FS shutdown', align=Align.INLINE)
d.comment(0x8216, 'Tail-call via filing system control vector', align=Align.INLINE)
d.comment(0x8219, 'Notify current FS of shutdown', align=Align.INLINE)
d.comment(0x821C, 'OSBYTE &7A: scan keyboard', align=Align.INLINE)
d.comment(0x8222, 'No key pressed: proceed with auto-boot', align=Align.INLINE)
d.comment(0x8224, "XOR with &55: result=0 if key is 'N'", align=Align.INLINE)
d.comment(0x8226, "Not 'N': return without claiming", align=Align.INLINE)
d.comment(0x8229, 'OSBYTE &78: clear key-pressed state', align=Align.INLINE)
d.comment(0x822E, "Print 'Econet Station ' banner", align=Align.INLINE)
d.comment(0x8242, 'Load station number', align=Align.INLINE)
d.comment(0x8244, 'Print as 3-digit decimal', align=Align.INLINE)
d.comment(0x8247, 'BIT trick: bit 5 of SR2 = clock present', align=Align.INLINE)
d.comment(0x8249, 'Test DCD: clock present if bit 5 clear', align=Align.INLINE)
d.comment(0x824C, 'Clock present: skip warning', align=Align.INLINE)
d.comment(0x824E, "Print ' No Clock' warning", align=Align.INLINE)
d.comment(0x825A, 'NOP (padding after inline string)', align=Align.INLINE)

d.label(0x825B, 'skip_no_clock_msg')
d.comment(0x825B, 'Print two CRs (blank line)', align=Align.INLINE)
d.comment(0x8265, 'Write to FILEV-FSCV vector table', align=Align.INLINE)
d.comment(0x8268, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8269, 'Loop until all 14 bytes copied', align=Align.INLINE)
d.comment(0x826B, 'Read ROM ptr table addr, install NETV', align=Align.INLINE)
d.comment(0x826E, 'Install 7 handler entries in ROM ptr table', align=Align.INLINE)
d.comment(0x8270, '7 FS vectors to install', align=Align.INLINE)
d.comment(0x8272, 'Install each 3-byte vector entry', align=Align.INLINE)
d.comment(0x8275, 'X=0 after loop; store as workspace offset', align=Align.INLINE)
d.comment(0x8280, 'Issue service &0A', align=Align.INLINE)
d.comment(0x8283, 'Non-zero after hard reset: skip auto-boot', align=Align.INLINE)
d.comment(0x8287, 'X = lo byte of auto-boot string at &828E', align=Align.INLINE)
d.comment(0x8294, 'Auto-boot string tail / NETV handler data', align=Align.INLINE)
d.comment(0x82B8, 'Already at page &10 or above?', align=Align.INLINE)
d.comment(0x82BA, 'Yes: nothing to claim', align=Align.INLINE)
d.comment(0x82BC, 'Claim pages &0D-&0F (3 pages)', align=Align.INLINE)
d.comment(0x82C6, 'A=0 for clearing workspace', align=Align.INLINE)
d.comment(0x82C8, 'Y=4: remote status offset', align=Align.INLINE)
d.comment(0x82CA, 'Clear status byte in net receive buffer', align=Align.INLINE)
d.comment(0x82CC, 'Y=&FF: used for later iteration', align=Align.INLINE)
d.comment(0x82CE, 'Clear RX ptr low byte', align=Align.INLINE)
d.comment(0x82D0, 'Clear workspace ptr low byte', align=Align.INLINE)
d.comment(0x82D2, 'Clear RXCB iteration counter', align=Align.INLINE)
d.comment(0x82D4, 'Clear TX semaphore (no TX in progress)', align=Align.INLINE)
d.comment(0x82D7, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x82DD, 'X = break type from OSBYTE result', align=Align.INLINE)
d.comment(0x82E0, 'Y=&15: printer station offset in RX buffer', align=Align.INLINE)
d.comment(0x82E2, '&FE = no server selected', align=Align.INLINE)
d.comment(0x82E7, 'Store &FE at printer station offset', align=Align.INLINE)
d.comment(0x82E9, 'A=0 for clearing workspace fields', align=Align.INLINE)
d.comment(0x82EB, 'Clear network number', align=Align.INLINE)
d.comment(0x82EE, 'Clear protection status', align=Align.INLINE)
d.comment(0x82F1, 'Clear message flag', align=Align.INLINE)
d.comment(0x82F4, 'Clear boot option', align=Align.INLINE)
d.comment(0x82F7, 'Y=&16', align=Align.INLINE)
d.comment(0x82F8, 'Clear net number at RX buffer offset &16', align=Align.INLINE)
d.comment(0x82FA, 'Init printer server: station &FE, net 0', align=Align.INLINE)
d.comment(0x82FC, 'Store net 0 at workspace offset 3', align=Align.INLINE)
d.comment(0x82FE, 'Y=2: printer station offset', align=Align.INLINE)
d.comment(0x82FF, '&FE = no printer server', align=Align.INLINE)
d.comment(0x8301, 'Store &FE at printer station in workspace', align=Align.INLINE)

d.label(0x8303, 'init_rxcb_entries')
d.comment(0x8303, 'Load RXCB counter', align=Align.INLINE)
d.comment(0x8305, 'Convert to workspace byte offset', align=Align.INLINE)
d.comment(0x8308, 'C=1: past max handles, done', align=Align.INLINE)
d.comment(0x830A, 'Mark RXCB as available', align=Align.INLINE)
d.comment(0x830C, 'Write &3F flag to workspace', align=Align.INLINE)
d.comment(0x830E, 'Next RXCB number', align=Align.INLINE)
d.comment(0x8310, 'Loop for all RXCBs', align=Align.INLINE)

d.label(0x8312, 'read_station_id')
d.comment(0x8315, 'Y=&14: station ID offset in RX buffer', align=Align.INLINE)
d.comment(0x8317, 'Store our station number', align=Align.INLINE)
d.comment(0x831C, 'Enable user-level RX (LFLAG=&40)', align=Align.INLINE)
d.comment(0x831E, 'Store to rx_flags', align=Align.INLINE)
d.comment(0x8321, 'OSBYTE &A8: read ROM pointer table address', align=Align.INLINE)
d.comment(0x8323, 'X=0: read low byte', align=Align.INLINE)
d.comment(0x8325, 'Y=&FF: read high byte', align=Align.INLINE)
d.comment(0x8327, 'Returns table address in X (lo) Y (hi)', align=Align.INLINE)
d.comment(0x832A, 'Store table base address low byte', align=Align.INLINE)
d.comment(0x832C, 'Store table base address high byte', align=Align.INLINE)
d.comment(0x832E, 'NETV extended vector offset in ROM ptr table', align=Align.INLINE)
d.comment(0x8330, 'Set NETV low byte = &36 (vector dispatch)', align=Align.INLINE)
d.comment(0x8333, 'Install 1 entry (NETV) in ROM ptr table', align=Align.INLINE)
d.comment(0x8335, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x8338, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x833A, 'Next byte', align=Align.INLINE)
d.comment(0x833B, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x833E, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x8340, 'Next byte', align=Align.INLINE)
d.comment(0x8341, 'Write current ROM bank number', align=Align.INLINE)
d.comment(0x8343, 'Store ROM number to ROM pointer table', align=Align.INLINE)
d.comment(0x8345, 'Advance to next entry position', align=Align.INLINE)
d.comment(0x8346, 'Count down entries', align=Align.INLINE)
d.comment(0x8347, 'Loop until all entries installed', align=Align.INLINE)
d.comment(0x8349, 'Y = workspace high byte + 1 = next free page', align=Align.INLINE)
d.comment(0x834B, 'Advance past workspace page', align=Align.INLINE)
d.comment(0x834C, 'Return; Y = page after NFS workspace', align=Align.INLINE)
d.comment(0x834D, 'Copy 10 bytes: FS state to workspace backup', align=Align.INLINE)
d.comment(0x8355, 'Offsets &15-&1D: server, handles, OPT, etc.', align=Align.INLINE)

d.label(0x8360, 'match_cmd_chars')

d.label(0x8373, 'check_rom_end')

d.label(0x8379, 'skip_space_next')

d.label(0x837A, 'skip_spaces')
d.comment(0x8383, 'A=&90: FS reply port (PREPLY)', align=Align.INLINE)
d.comment(0x8385, 'Init TXCB from template', align=Align.INLINE)
d.comment(0x8388, 'Store port number in TXCB', align=Align.INLINE)
d.comment(0x838A, 'Control byte: 3 = transmit', align=Align.INLINE)
d.comment(0x838C, 'Store control byte in TXCB', align=Align.INLINE)
d.comment(0x838E, 'Decrement TXCB flag to arm TX', align=Align.INLINE)
d.comment(0x8391, 'Preserve A across call', align=Align.INLINE)
d.comment(0x8392, 'Copy 12 bytes (Y=11..0)', align=Align.INLINE)
d.comment(0x8394, 'Load template byte', align=Align.INLINE)
d.comment(0x8397, 'Store to TX control block at &00C0', align=Align.INLINE)
d.comment(0x839A, 'Y < 2: also copy FS server station/network', align=Align.INLINE)
d.comment(0x839C, 'Skip station/network copy for Y >= 2', align=Align.INLINE)
d.comment(0x839E, 'Load FS server station (Y=0) or network (Y=1)', align=Align.INLINE)
d.comment(0x83A1, 'Store to dest station/network at &00C2', align=Align.INLINE)
d.comment(0x83A4, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x83A5, 'Loop until all 12 bytes copied', align=Align.INLINE)
d.comment(0x83A7, 'Restore A', align=Align.INLINE)
d.comment(0x83A8, 'Return', align=Align.INLINE)

d.label(0x83AF, 'tx_ctrl_upper')
d.comment(0x83B5, 'Save flag byte for command', align=Align.INLINE)
d.comment(0x83B6, 'C=1: include flag in FS command', align=Align.INLINE)
d.comment(0x83B7, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)
d.comment(0x83B9, 'V=0: command has no flag byte', align=Align.INLINE)
d.comment(0x83BA, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)
d.comment(0x83C3, 'V=0: standard FS command path', align=Align.INLINE)
d.comment(0x83C4, 'Copy URD handle from workspace to buffer', align=Align.INLINE)
d.comment(0x83C7, 'Store URD at &0F02', align=Align.INLINE)

d.label(0x83CA, 'store_fs_hdr_clc')
d.comment(0x83CA, 'CLC: no byte-stream path', align=Align.INLINE)

d.label(0x83CB, 'store_fs_hdr_fn')
d.comment(0x83CB, 'Store function code at &0F01', align=Align.INLINE)
d.comment(0x83CE, 'Y=1: copy CSD (offset 1) then LIB (offset 0)', align=Align.INLINE)

d.label(0x83D0, 'copy_dir_handles')
d.comment(0x83D0, 'Copy CSD and LIB handles to command buffer', align=Align.INLINE)
d.comment(0x83D3, 'Store at &0F03 (CSD) and &0F04 (LIB)', align=Align.INLINE)
d.comment(0x83D6, 'Y=function code', align=Align.INLINE)
d.comment(0x83D7, 'Loop for both handles', align=Align.INLINE)
d.comment(0x83D9, 'Save carry (FS path vs byte-stream)', align=Align.INLINE)
d.comment(0x83DA, 'Reply port &90 (PREPLY)', align=Align.INLINE)
d.comment(0x83DC, 'Store at &0F00 (HDRREP)', align=Align.INLINE)
d.comment(0x83DF, 'Copy TX template to &00C0', align=Align.INLINE)
d.comment(0x83E2, 'A = X (buffer extent)', align=Align.INLINE)
d.comment(0x83E3, 'HPTR = header (5) + data (X) bytes to send', align=Align.INLINE)
d.comment(0x83E5, 'Store to TXCB end-pointer low', align=Align.INLINE)
d.comment(0x83E7, 'Restore carry flag', align=Align.INLINE)
d.comment(0x83E8, 'C=1: byte-stream path (BSXMIT)', align=Align.INLINE)
d.comment(0x83EA, 'Save flags for send_fs_reply_cmd', align=Align.INLINE)
d.comment(0x83EB, 'Point net_tx_ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x83EE, 'Restore flags', align=Align.INLINE)
d.comment(0x83EF, 'Save flags (V flag state)', align=Align.INLINE)
d.comment(0x83F0, 'Set up RX wait for FS reply', align=Align.INLINE)
d.comment(0x83F3, 'Transmit and wait (BRIANX)', align=Align.INLINE)
d.comment(0x83F6, 'Restore flags', align=Align.INLINE)
d.comment(0x83F7, 'Y=1: skip past command code byte', align=Align.INLINE)
d.comment(0x83F8, 'Load return code from FS reply', align=Align.INLINE)
d.comment(0x83FA, 'X = return code', align=Align.INLINE)
d.comment(0x83FB, 'Zero: success, return', align=Align.INLINE)
d.comment(0x83FD, 'V=0: standard path, error is fatal', align=Align.INLINE)
d.comment(0x83FF, 'ADC #&2A: test for &D6 (not found)', align=Align.INLINE)

d.label(0x8401, 'check_fs_error')
d.comment(0x8401, 'Non-zero: hard error, go to FSERR', align=Align.INLINE)
d.comment(0x8403, 'Return (success or soft &D6 error)', align=Align.INLINE)
d.comment(0x8404, 'Discard saved flags from stack', align=Align.INLINE)
d.comment(0x8405, 'X=&C0: TXCB address for byte-stream TX', align=Align.INLINE)
d.comment(0x8407, 'Y++ past command code', align=Align.INLINE)
d.comment(0x8408, 'Byte-stream transmit with retry', align=Align.INLINE)
d.comment(0x840B, 'Store result to &B3', align=Align.INLINE)
d.comment(0x840D, 'C=0: success, check reply code', align=Align.INLINE)
d.comment(0x8410, 'Save A (BPUT byte) on stack', align=Align.INLINE)
d.comment(0x8411, 'Also save byte at &0FDF for BSXMIT', align=Align.INLINE)
d.comment(0x8414, 'Transfer X for stack save', align=Align.INLINE)
d.comment(0x8415, 'Save X on stack', align=Align.INLINE)
d.comment(0x8416, 'Transfer Y (handle) for stack save', align=Align.INLINE)
d.comment(0x8417, 'Save Y (handle) on stack', align=Align.INLINE)
d.comment(0x8418, 'Save P (C = BPUT/BGET selector) on stack', align=Align.INLINE)
d.comment(0x8419, 'Save handle for SPOOL/EXEC comparison later', align=Align.INLINE)
d.comment(0x841B, 'Convert handle Y to single-bit mask', align=Align.INLINE)
d.comment(0x841E, 'Store handle bitmask at &0FDE', align=Align.INLINE)
d.comment(0x8421, 'Store handle bitmask for sequence tracking', align=Align.INLINE)
d.comment(0x8423, '&90 = data port (PREPLY)', align=Align.INLINE)
d.comment(0x8425, 'Store reply port in command buffer', align=Align.INLINE)
d.comment(0x8428, 'Set up 12-byte TXCB from template', align=Align.INLINE)
d.comment(0x842B, 'CB reply buffer at &0FDC', align=Align.INLINE)
d.comment(0x842D, 'Store reply buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x842F, 'Error buffer at &0FE0', align=Align.INLINE)
d.comment(0x8431, 'Store error buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x8433, 'Y=1 (from init_tx_ctrl_block exit)', align=Align.INLINE)
d.comment(0x8434, 'X=9: BPUT function code', align=Align.INLINE)
d.comment(0x8436, 'Restore C: selects BPUT (0) vs BGET (1)', align=Align.INLINE)
d.comment(0x8437, 'C=0 (BPUT): keep X=9', align=Align.INLINE)
d.comment(0x843A, 'Store function code at &0FDD', align=Align.INLINE)
d.comment(0x843D, 'Load handle bitmask for BSXMIT', align=Align.INLINE)
d.comment(0x843F, 'X=&C0: TXCB address for econet_tx_retry', align=Align.INLINE)
d.comment(0x8441, 'Transmit via byte-stream protocol', align=Align.INLINE)
d.comment(0x8444, 'Load reply byte from buffer', align=Align.INLINE)
d.comment(0x8447, 'Zero reply = success, skip error handling', align=Align.INLINE)
d.comment(0x8449, 'Copy 32-byte reply to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x844B, 'Load reply byte at offset Y', align=Align.INLINE)
d.comment(0x844E, 'Store to error buffer at &0FE0+Y', align=Align.INLINE)
d.comment(0x8451, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8452, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x8455, 'A=&C6: read *EXEC file handle', align=Align.INLINE)
d.comment(0x845A, '\')\': offset into "SP." string at &8529', align=Align.INLINE)
d.comment(0x845C, 'Y=value of *SPOOL file handle', align=Align.INLINE)
d.comment(0x845E, 'Handle matches SPOOL -- close it', align=Align.INLINE)
d.comment(0x8460, '\'-\': offset into "E." string at &852D', align=Align.INLINE)
d.comment(0x8462, 'X=value of *EXEC file handle', align=Align.INLINE)
d.comment(0x8464, 'No EXEC match -- skip close', align=Align.INLINE)

d.label(0x8466, 'close_spool_exec')
d.comment(0x8466, 'X = string offset for OSCLI close', align=Align.INLINE)
d.comment(0x8467, 'Y=&85: high byte of OSCLI string in ROM', align=Align.INLINE)
d.comment(0x8469, 'Close SPOOL/EXEC via "*SP." or "*E."', align=Align.INLINE)

d.label(0x846C, 'dispatch_fs_error')
d.comment(0x846C, 'Reset CB pointer to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x846E, 'Reset reply ptr to error buffer', align=Align.INLINE)
d.comment(0x8470, 'Reload reply byte for error dispatch', align=Align.INLINE)
d.comment(0x8473, 'Remember raw FS error code', align=Align.INLINE)
d.comment(0x8476, 'Y=1: point to error number byte in reply', align=Align.INLINE)
d.comment(0x8478, 'Clamp FS errors below &A8 to standard &A8', align=Align.INLINE)
d.comment(0x847A, 'Error >= &A8: keep original value', align=Align.INLINE)
d.comment(0x847C, 'Error < &A8: override with standard &A8', align=Align.INLINE)
d.comment(0x847E, 'Write clamped error number to reply buffer', align=Align.INLINE)

d.label(0x8480, 'error_code_clamped')
d.comment(0x8480, 'Start scanning from offset &FF (will INY to 0)', align=Align.INLINE)

d.label(0x8482, 'copy_error_to_brk')
d.comment(0x8482, 'Next byte in reply buffer', align=Align.INLINE)
d.comment(0x8483, 'Copy reply buffer to &0100 for BRK execution', align=Align.INLINE)
d.comment(0x8485, 'Build BRK error block at &0100', align=Align.INLINE)
d.comment(0x8488, 'Scan for CR terminator (&0D)', align=Align.INLINE)
d.comment(0x848A, 'Continue until CR found', align=Align.INLINE)
d.comment(0x848C, 'Replace CR with zero = BRK error block end', align=Align.INLINE)
d.comment(0x848F, 'Execute as BRK error block at &0100; ALWAYS', align=Align.INLINE)
d.comment(0x8491, 'Save updated sequence number', align=Align.INLINE)
d.comment(0x8494, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x8496, 'Restore X from stack', align=Align.INLINE)
d.comment(0x8498, 'Restore A from stack', align=Align.INLINE)
d.comment(0x8499, 'Return to caller', align=Align.INLINE)
d.comment(0x849A, 'Y=4: remote status flag offset', align=Align.INLINE)
d.comment(0x849C, 'Read remote status from RX CB', align=Align.INLINE)
d.comment(0x849E, 'Zero: not remoted, set up session', align=Align.INLINE)
d.comment(0x84A0, 'Already remoted: clear and return', align=Align.INLINE)
d.comment(0x84A3, 'Set remote status: bits 0+3 (ORA #9)', align=Align.INLINE)
d.comment(0x84A5, 'Store updated remote status', align=Align.INLINE)
d.comment(0x84A7, 'X=&80: RX data area offset', align=Align.INLINE)
d.comment(0x84A9, 'Y=&80: read source station low', align=Align.INLINE)
d.comment(0x84AB, 'Read source station lo from RX data at &80', align=Align.INLINE)
d.comment(0x84AD, 'Save source station low byte', align=Align.INLINE)
d.comment(0x84AE, 'Y=&81', align=Align.INLINE)
d.comment(0x84AF, 'Read source station hi from RX data at &81', align=Align.INLINE)
d.comment(0x84B1, 'Save controlling station to workspace &0E/&0F', align=Align.INLINE)
d.comment(0x84B3, 'Store station high to ws+&0F', align=Align.INLINE)
d.comment(0x84B5, 'Y=&0E', align=Align.INLINE)
d.comment(0x84B6, 'Restore source station low', align=Align.INLINE)
d.comment(0x84B7, 'Store station low to ws+&0E', align=Align.INLINE)
d.comment(0x84B9, 'Clear OSBYTE &CE/&CF flags', align=Align.INLINE)
d.comment(0x84BC, 'Set up TX control block', align=Align.INLINE)
d.comment(0x84BF, 'X=1: disable keyboard', align=Align.INLINE)
d.comment(0x84C1, 'Y=0 for OSBYTE', align=Align.INLINE)
d.comment(0x84C3, 'Disable keyboard for remote session', align=Align.INLINE)
d.comment(0x84C8, 'Allow JSR to page 1 (stack page)', align=Align.INLINE)
d.comment(0x84CB, 'Zero bytes &0100-&0102', align=Align.INLINE)

d.label(0x84CF, 'zero_exec_header')
d.comment(0x84CF, 'BRK at &0100 as safe default', align=Align.INLINE)

d.label(0x84D5, 'execute_downloaded')
d.comment(0x84D5, 'Execute downloaded code', align=Align.INLINE)
d.comment(0x84D8, 'Y=4: RX control block byte 4 (remote status)', align=Align.INLINE)
d.comment(0x84DA, 'Read remote status flag', align=Align.INLINE)
d.comment(0x84DC, 'Zero = not remoted; allow new session', align=Align.INLINE)
d.comment(0x84DE, 'Read source station from RX data at &80', align=Align.INLINE)
d.comment(0x84E0, 'A = source station number', align=Align.INLINE)
d.comment(0x84E2, 'Compare against controlling station at &0E', align=Align.INLINE)
d.comment(0x84E4, 'Check if source matches controller', align=Align.INLINE)
d.comment(0x84E6, 'Reject: source != controlling station', align=Align.INLINE)
d.comment(0x84E8, 'Read keypress from RX data at &82', align=Align.INLINE)
d.comment(0x84EA, 'Load character byte', align=Align.INLINE)
d.comment(0x84EC, 'Y = character to insert', align=Align.INLINE)
d.comment(0x84ED, 'X = buffer 0 (keyboard input)', align=Align.INLINE)
d.comment(0x84EF, 'Release JSR protection before inserting key', align=Align.INLINE)
d.comment(0x84F2, 'OSBYTE &99: insert char into input buffer', align=Align.INLINE)
d.comment(0x84F4, 'Tail call: insert character Y into buffer X', align=Align.INLINE)

d.label(0x84F7, 'error_not_listening')
d.comment(0x84F7, 'Error code 8: "Not listening" error', align=Align.INLINE)
d.comment(0x84F9, 'ALWAYS branch to set_listen_offset', align=Align.INLINE)
d.comment(0x84FB, 'Load TX status byte for error lookup', align=Align.INLINE)
d.comment(0x84FD, 'Mask to 3-bit error code (0-7)', align=Align.INLINE)
d.comment(0x84FF, 'X = error code index', align=Align.INLINE)
d.comment(0x8500, 'Look up error message offset from table', align=Align.INLINE)
d.comment(0x8503, 'X=0: start writing at &0101', align=Align.INLINE)
d.comment(0x8505, 'Store BRK opcode at &0100', align=Align.INLINE)

d.label(0x8508, 'copy_error_message')
d.comment(0x8508, 'Load error message byte', align=Align.INLINE)
d.comment(0x850B, 'Build error message at &0101+', align=Align.INLINE)
d.comment(0x850E, 'Zero byte = end of message; go execute BRK', align=Align.INLINE)
d.comment(0x8510, 'Next source byte', align=Align.INLINE)
d.comment(0x8511, 'Next dest byte', align=Align.INLINE)
d.comment(0x8512, 'Continue copying message', align=Align.INLINE)
d.comment(0x851D, 'Save function code on stack', align=Align.INLINE)
d.comment(0x851E, 'Load current rx_flags', align=Align.INLINE)
d.comment(0x8521, 'Save rx_flags on stack for restore', align=Align.INLINE)
d.comment(0x8522, 'Set bit7: FS transaction in progress', align=Align.INLINE)
d.comment(0x8524, 'Write back updated rx_flags', align=Align.INLINE)

d.label(0x8527, 'skip_rx_flag_set')
d.comment(0x8527, 'Push two zero bytes as timeout counters', align=Align.INLINE)
d.comment(0x8529, 'First zero for timeout', align=Align.INLINE)
d.comment(0x852A, 'Second zero for timeout', align=Align.INLINE)
d.comment(0x852B, 'Y=0: index for flag byte check', align=Align.INLINE)
d.comment(0x852C, 'TSX: index stack-based timeout via X', align=Align.INLINE)
d.comment(0x8530, 'Read flag byte from TX control block', align=Align.INLINE)
d.comment(0x8532, 'Bit 7 set = reply received', align=Align.INLINE)
d.comment(0x8534, 'Three-stage nested timeout: inner loop', align=Align.INLINE)
d.comment(0x8537, 'Inner not expired: keep polling', align=Align.INLINE)
d.comment(0x8539, 'Middle timeout loop', align=Align.INLINE)
d.comment(0x853C, 'Middle not expired: keep polling', align=Align.INLINE)
d.comment(0x853E, 'Outer timeout loop (slowest)', align=Align.INLINE)
d.comment(0x8541, 'Outer not expired: keep polling', align=Align.INLINE)
d.comment(0x8543, 'Pop first timeout byte', align=Align.INLINE)
d.comment(0x8544, 'Pop second timeout byte', align=Align.INLINE)
d.comment(0x8545, 'Pop saved rx_flags into A', align=Align.INLINE)
d.comment(0x8546, 'Restore saved rx_flags from stack', align=Align.INLINE)
d.comment(0x8549, 'Pop saved function code', align=Align.INLINE)
d.comment(0x854A, 'A=saved func code; zero would mean no reply', align=Align.INLINE)
d.comment(0x854C, 'Return to caller', align=Align.INLINE)
d.comment(0x855C, 'C=1: flag for BGET mode', align=Align.INLINE)
d.comment(0x855D, 'Handle BGET via FS command', align=Align.INLINE)
d.comment(0x8560, 'SEC: set carry for error check', align=Align.INLINE)
d.comment(0x8561, 'A=&FE: mask for EOF check', align=Align.INLINE)
d.comment(0x8563, 'BIT l0fdf: test error flags', align=Align.INLINE)
d.comment(0x8566, 'V=1: error, return early', align=Align.INLINE)
d.comment(0x8568, 'CLC: no error', align=Align.INLINE)
d.comment(0x8569, 'Save flags for EOF check', align=Align.INLINE)
d.comment(0x856A, 'Load BGET result byte', align=Align.INLINE)
d.comment(0x856C, 'Restore flags', align=Align.INLINE)
d.comment(0x856D, 'Bit7 set: skip FS flag clear', align=Align.INLINE)
d.comment(0x856F, 'Clear FS flag for handle', align=Align.INLINE)

d.label(0x8572, 'bgetv_shared_jsr')
d.comment(0x85DD, 'Y=&0E: attribute byte offset in param block', align=Align.INLINE)
d.comment(0x85DF, 'Load FS attribute byte', align=Align.INLINE)
d.comment(0x85E1, 'Mask to 6 bits (FS → BBC direction)', align=Align.INLINE)
d.comment(0x85E3, 'X=4: skip first 4 table entries (BBC→FS half)', align=Align.INLINE)
d.comment(0x85E5, 'ALWAYS branch to shared bitmask builder', align=Align.INLINE)
d.comment(0x85E7, 'Mask to 5 bits (BBC → FS direction)', align=Align.INLINE)
d.comment(0x85E9, 'X=&FF: INX makes 0; start from table index 0', align=Align.INLINE)

d.label(0x85EB, 'attrib_shift_bits')
d.comment(0x85EB, 'Temp storage for source bitmask to shift out', align=Align.INLINE)
d.comment(0x85ED, 'A=0: accumulate destination bits here', align=Align.INLINE)

d.label(0x85EF, 'map_attrib_bits')
d.comment(0x85EF, 'Next table entry', align=Align.INLINE)
d.comment(0x85F0, 'Shift out source bits one at a time', align=Align.INLINE)
d.comment(0x85F2, 'Bit was 0: skip this destination bit', align=Align.INLINE)
d.comment(0x85F4, 'OR in destination bit from lookup table', align=Align.INLINE)

d.label(0x85F7, 'skip_set_attrib_bit')
d.comment(0x85F7, 'Loop while source bits remain (A != 0)', align=Align.INLINE)
d.comment(0x85F9, 'Return; A = converted attribute bitmask', align=Align.INLINE)

d.label(0x860D, 'print_inline_char')

d.label(0x8613, 'print_next_char')

d.label(0x861D, 'jump_via_addr')

d.label(0x8624, 'scan_decimal_digit')

d.label(0x863F, 'no_dot_exit')

d.label(0x8640, 'parse_decimal_rts')
d.comment(0x8643, 'Handle number to Y for conversion', align=Align.INLINE)
d.comment(0x8644, 'Force unconditional conversion', align=Align.INLINE)

d.label(0x865C, 'handle_mask_exit')
d.comment(0x8668, 'Compare 4 bytes (index 4,3,2,1)', align=Align.INLINE)

d.label(0x866A, 'compare_addr_byte')
d.comment(0x866A, 'Load byte from first address', align=Align.INLINE)
d.comment(0x866C, 'XOR with corresponding byte', align=Align.INLINE)
d.comment(0x866E, 'Mismatch: Z=0, return unequal', align=Align.INLINE)
d.comment(0x8671, 'Continue comparing', align=Align.INLINE)
d.comment(0x8674, 'X=first handle (&20)', align=Align.INLINE)
d.comment(0x8676, 'Y=last handle (&27)', align=Align.INLINE)
d.comment(0x8679, 'Merge new bits into flags', align=Align.INLINE)
d.comment(0x867C, 'Store updated flags (always taken)', align=Align.INLINE)
d.comment(0x867E, 'Invert mask: set bits become clear bits', align=Align.INLINE)
d.comment(0x8680, 'Clear specified bits in flags', align=Align.INLINE)
d.comment(0x8683, 'Write back updated flags', align=Align.INLINE)
d.comment(0x8686, 'Return', align=Align.INLINE)
d.comment(0x86D7, 'Y=1: copy 2 bytes (high then low)', align=Align.INLINE)
d.comment(0x86D9, 'Load filename ptr from control block', align=Align.INLINE)
d.comment(0x86DB, 'Store to MOS text pointer (&F2/&F3)', align=Align.INLINE)
d.comment(0x86DE, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x86DF, 'Loop for both bytes', align=Align.INLINE)
d.comment(0x86E1, 'Start from beginning of string', align=Align.INLINE)
d.comment(0x86E3, 'X=&FF: next INX wraps to first char index', align=Align.INLINE)
d.comment(0x86E5, 'C=0 for GSINIT: parse from current position', align=Align.INLINE)
d.comment(0x86E6, 'Initialise GS string parser', align=Align.INLINE)
d.comment(0x86E9, 'Empty string: skip to CR terminator', align=Align.INLINE)
d.comment(0x86EB, 'Read next character via GSREAD', align=Align.INLINE)
d.comment(0x86EE, 'C=1 from GSREAD: end of string reached', align=Align.INLINE)
d.comment(0x86F0, 'Advance buffer index', align=Align.INLINE)
d.comment(0x86F1, 'Store parsed character to &0E30+X', align=Align.INLINE)
d.comment(0x86F4, 'ALWAYS loop (GSREAD clears C on success)', align=Align.INLINE)

d.label(0x86F6, 'terminate_filename')
d.comment(0x86F6, 'Terminate parsed string with CR', align=Align.INLINE)
d.comment(0x86F7, 'CR = &0D', align=Align.INLINE)
d.comment(0x86F9, 'Store CR terminator at end of string', align=Align.INLINE)
d.comment(0x86FC, 'Point fs_crc_lo/hi at &0E30 parse buffer', align=Align.INLINE)
d.comment(0x86FE, 'fs_crc_lo = &30', align=Align.INLINE)
d.comment(0x8700, 'fs_crc_hi = &0E → buffer at &0E30', align=Align.INLINE)
d.comment(0x8702, 'Store high byte', align=Align.INLINE)
d.comment(0x8704, 'Return; X = string length', align=Align.INLINE)
d.comment(0x8708, 'Copy filename ptr from param block to os_text_ptr', align=Align.INLINE)
d.comment(0x870B, 'Recover function code from saved A', align=Align.INLINE)
d.comment(0x870D, 'A >= 0: save (&00) or attribs (&01-&06)', align=Align.INLINE)
d.comment(0x870F, 'A=&FF? Only &FF is valid for load', align=Align.INLINE)
d.comment(0x8713, 'Unknown negative code: no-op return', align=Align.INLINE)
d.comment(0x871B, 'Port &92 = PLDATA (data transfer port)', align=Align.INLINE)
d.comment(0x871D, 'Overwrite URD field with data port number', align=Align.INLINE)
d.comment(0x8720, 'Build FS header (V=1: CLV path)', align=Align.INLINE)
d.comment(0x8723, 'Y=6: param block byte 6', align=Align.INLINE)
d.comment(0x8725, "Byte 6: use file's own load address?", align=Align.INLINE)
d.comment(0x8727, 'Non-zero: use FS reply address (lodfil)', align=Align.INLINE)
d.comment(0x8729, "Zero: copy caller's load addr first", align=Align.INLINE)
d.comment(0x872C, 'Then copy FS reply to param block', align=Align.INLINE)
d.comment(0x872F, 'Carry clear from prepare_cmd_clv: skip lodfil', align=Align.INLINE)
d.comment(0x8731, 'Copy FS reply addresses to param block', align=Align.INLINE)
d.comment(0x8734, 'Then copy load addr from param block', align=Align.INLINE)

d.label(0x8737, 'skip_lodfil')
d.comment(0x8737, 'Compute end address = load + file length', align=Align.INLINE)

d.label(0x8739, 'copy_load_end_addr')
d.comment(0x8739, 'Load address byte', align=Align.INLINE)
d.comment(0x873B, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x873D, 'Add file length byte', align=Align.INLINE)
d.comment(0x8740, 'Store as end position', align=Align.INLINE)
d.comment(0x8742, 'Next address byte', align=Align.INLINE)
d.comment(0x8743, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8744, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8746, 'Adjust high byte for 3-byte length overflow', align=Align.INLINE)
d.comment(0x8747, 'Subtract 4th length byte from end addr', align=Align.INLINE)
d.comment(0x874A, 'Store adjusted end address high byte', align=Align.INLINE)
d.comment(0x874F, 'Transfer file data in &80-byte blocks', align=Align.INLINE)
d.comment(0x8752, 'Copy 3-byte file length to FS reply cmd buffer', align=Align.INLINE)
d.comment(0x8754, 'Load file length byte', align=Align.INLINE)
d.comment(0x8757, 'Store in FS command data buffer', align=Align.INLINE)
d.comment(0x875A, 'Next byte (count down)', align=Align.INLINE)
d.comment(0x875B, 'Loop for 3 bytes (X=2,1,0)', align=Align.INLINE)
d.comment(0x875D, 'ALWAYS branch', align=Align.INLINE)
d.comment(0x8762, 'Addresses match: transfer complete', align=Align.INLINE)
d.comment(0x8764, 'Port &92 for data block transfer', align=Align.INLINE)
d.comment(0x8766, 'Store port to TXCB command byte', align=Align.INLINE)

d.label(0x8768, 'send_block_loop')
d.comment(0x8768, 'Set up next &80-byte block for transfer', align=Align.INLINE)

d.label(0x876A, 'copy_block_addrs')
d.comment(0x876A, 'Swap: current addr -> source, end -> current', align=Align.INLINE)
d.comment(0x876C, 'Source addr = current position', align=Align.INLINE)
d.comment(0x876E, 'Load end address byte', align=Align.INLINE)
d.comment(0x8770, 'Dest = end address (will be clamped)', align=Align.INLINE)
d.comment(0x8772, 'Next address byte', align=Align.INLINE)
d.comment(0x8773, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8775, 'Command &7F = data block transfer', align=Align.INLINE)
d.comment(0x8777, 'Store to TXCB control byte', align=Align.INLINE)
d.comment(0x8779, 'Send this block to the fileserver', align=Align.INLINE)
d.comment(0x877C, 'Y=3: compare 4 bytes (3..0)', align=Align.INLINE)
d.comment(0x877E, 'Compare current vs end address (4 bytes)', align=Align.INLINE)
d.comment(0x8781, 'XOR with end address byte', align=Align.INLINE)
d.comment(0x8784, 'Not equal: more blocks to send', align=Align.INLINE)
d.comment(0x8786, 'Next byte', align=Align.INLINE)
d.comment(0x8787, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8789, 'All equal: transfer complete', align=Align.INLINE)
d.comment(0x878A, 'A=0: SAVE handler', align=Align.INLINE)
d.comment(0x878C, 'A!=0: attribute dispatch (A=1-6)', align=Align.INLINE)
d.comment(0x878F, 'Process 4 address bytes (load/exec/start/end)', align=Align.INLINE)
d.comment(0x8791, 'Y=&0E: start from end-address in param block', align=Align.INLINE)
d.comment(0x8793, 'Read end-address byte from param block', align=Align.INLINE)
d.comment(0x8795, 'Save to port workspace for transfer setup', align=Align.INLINE)
d.comment(0x8798, 'Y = Y-4: point to start-address byte', align=Align.INLINE)
d.comment(0x879B, 'end - start = transfer length byte', align=Align.INLINE)
d.comment(0x879D, 'Store length byte in FS command buffer', align=Align.INLINE)
d.comment(0x87A0, 'Save length byte for param block restore', align=Align.INLINE)
d.comment(0x87A1, 'Read corresponding start-address byte', align=Align.INLINE)
d.comment(0x87A3, 'Save to port workspace', align=Align.INLINE)
d.comment(0x87A6, 'Restore length byte from stack', align=Align.INLINE)
d.comment(0x87A7, 'Replace param block entry with length', align=Align.INLINE)
d.comment(0x87A9, 'Y = Y+5: advance to next address group', align=Align.INLINE)
d.comment(0x87AC, 'Decrement address byte counter', align=Align.INLINE)
d.comment(0x87AD, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x87AF, 'Copy load/exec addresses to FS command buffer', align=Align.INLINE)

d.label(0x87B1, 'copy_save_params')
d.comment(0x87B1, 'Read load/exec address byte from params', align=Align.INLINE)
d.comment(0x87B3, 'Copy to FS command buffer', align=Align.INLINE)
d.comment(0x87B6, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x87B7, 'Loop for bytes 9..1', align=Align.INLINE)
d.comment(0x87B9, 'Port &91 for save command', align=Align.INLINE)
d.comment(0x87BB, 'Overwrite URD field with port number', align=Align.INLINE)
d.comment(0x87BE, 'Save port &91 for flow control ACK', align=Align.INLINE)
d.comment(0x87C0, 'Append filename at offset &0B in cmd buffer', align=Align.INLINE)
d.comment(0x87C2, 'Append filename to cmd buffer at offset X', align=Align.INLINE)
d.comment(0x87C5, 'Y=1: function code for save', align=Align.INLINE)
d.comment(0x87C7, 'Build header and send FS save command', align=Align.INLINE)
d.comment(0x87D0, 'Print file length in hex', align=Align.INLINE)

d.label(0x87D6, 'skip_catalogue_msg')
d.comment(0x87D6, 'Store reply command for attr decode', align=Align.INLINE)
d.comment(0x87D9, 'Y=&0E: access byte offset in param block', align=Align.INLINE)
d.comment(0x87DB, 'Load access byte from FS reply', align=Align.INLINE)
d.comment(0x87DE, 'Convert FS access to BBC attribute format', align=Align.INLINE)
d.comment(0x87E9, 'Copied all 4 bytes? (Y=&0E..&11)', align=Align.INLINE)
d.comment(0x87EB, 'Loop for 4 attribute bytes', align=Align.INLINE)
d.comment(0x87ED, 'Restore A/X/Y and return to caller', align=Align.INLINE)
d.comment(0x87F0, 'Start at offset 5 (top of 4-byte addr)', align=Align.INLINE)
d.comment(0x87F2, 'Read from parameter block', align=Align.INLINE)
d.comment(0x87F4, 'Store to local workspace', align=Align.INLINE)
d.comment(0x87F7, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x87F8, 'Copy offsets 5,4,3,2 (4 bytes)', align=Align.INLINE)
d.comment(0x87FA, 'Loop while Y >= 2', align=Align.INLINE)
d.comment(0x87FC, 'Y += 5', align=Align.INLINE)
d.comment(0x87FD, 'Y += 4', align=Align.INLINE)
d.comment(0x8801, 'Return', align=Align.INLINE)
d.comment(0x8802, 'Start at offset &0D (top of range)', align=Align.INLINE)
d.comment(0x8804, 'First store uses X (attrib byte)', align=Align.INLINE)
d.comment(0x8805, 'Write to parameter block', align=Align.INLINE)
d.comment(0x8807, 'Read next byte from reply buffer', align=Align.INLINE)
d.comment(0x880B, 'Copy offsets &0D down to 2', align=Align.INLINE)
d.comment(0x880F, 'Y -= 4', align=Align.INLINE)
d.comment(0x8814, 'Save FS command byte on stack', align=Align.INLINE)
d.comment(0x8818, 'Addresses equal: nothing to transfer', align=Align.INLINE)
d.comment(0x882C, 'Store dest address byte', align=Align.INLINE)
d.comment(0x882E, 'Advance current position', align=Align.INLINE)
d.comment(0x8830, 'Next address byte', align=Align.INLINE)
d.comment(0x8831, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8832, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8836, 'SEC for SBC in overshoot check', align=Align.INLINE)
d.comment(0x8837, 'Check if new pos overshot end addr', align=Align.INLINE)
d.comment(0x883A, 'Subtract end address byte', align=Align.INLINE)
d.comment(0x883D, 'Next byte', align=Align.INLINE)
d.comment(0x883E, 'Decrement counter', align=Align.INLINE)
d.comment(0x883F, 'Loop for 4-byte comparison', align=Align.INLINE)
d.comment(0x8841, 'C=0: no overshoot, proceed', align=Align.INLINE)
d.comment(0x8843, 'Overshot: clamp dest to end address', align=Align.INLINE)

d.label(0x8845, 'clamp_dest_addr')
d.comment(0x8845, 'Load end address byte', align=Align.INLINE)
d.comment(0x8847, 'Replace dest with end address', align=Align.INLINE)
d.comment(0x8849, 'Next byte', align=Align.INLINE)
d.comment(0x884A, 'Loop for all 4 bytes', align=Align.INLINE)

d.label(0x884C, 'send_block')
d.comment(0x884C, 'Recover original FS command byte', align=Align.INLINE)
d.comment(0x884D, 'Re-push for next iteration', align=Align.INLINE)
d.comment(0x884E, 'Save processor flags (C from cmp)', align=Align.INLINE)
d.comment(0x884F, 'Store command byte in TXCB', align=Align.INLINE)
d.comment(0x8851, '128-byte block size for data transfer', align=Align.INLINE)
d.comment(0x8853, 'Store size in TXCB control byte', align=Align.INLINE)
d.comment(0x8855, 'Point TX ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x8858, 'ACK port for flow control', align=Align.INLINE)
d.comment(0x885A, 'Set reply port for ACK receive', align=Align.INLINE)
d.comment(0x885D, 'Restore flags (C=overshoot status)', align=Align.INLINE)
d.comment(0x885E, 'C=1: all data sent (overshot), done', align=Align.INLINE)
d.comment(0x8860, 'Command &91 = data block transfer', align=Align.INLINE)
d.comment(0x8862, 'Store command &91 in TXCB', align=Align.INLINE)
d.comment(0x8864, 'Transmit block and wait (BRIANX)', align=Align.INLINE)
d.comment(0x8867, 'More blocks? Loop back', align=Align.INLINE)
d.comment(0x8869, 'Save A (function code)', align=Align.INLINE)
d.comment(0x886A, 'X = file handle to check', align=Align.INLINE)
d.comment(0x886B, 'Convert handle to bitmask in A', align=Align.INLINE)
d.comment(0x886E, 'Y = handle bitmask from conversion', align=Align.INLINE)
d.comment(0x886F, 'Local hint: is EOF possible for this handle?', align=Align.INLINE)
d.comment(0x8872, 'X = result of AND (0 = not at EOF)', align=Align.INLINE)
d.comment(0x8873, 'Hint clear: definitely not at EOF', align=Align.INLINE)
d.comment(0x8875, 'Save bitmask for clear_fs_flag', align=Align.INLINE)
d.comment(0x8876, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x8879, 'Y=&11: FS function code FCEOF', align=Align.INLINE)
d.comment(0x8880, 'Restore bitmask', align=Align.INLINE)
d.comment(0x8881, 'FS reply: non-zero = at EOF', align=Align.INLINE)
d.comment(0x8884, 'At EOF: skip flag clear', align=Align.INLINE)
d.comment(0x8886, 'Not at EOF: clear the hint bit', align=Align.INLINE)

d.label(0x8889, 'restore_ay_return')
d.comment(0x8889, 'Restore A', align=Align.INLINE)
d.comment(0x888A, 'Restore Y', align=Align.INLINE)
d.comment(0x888C, 'Return; X=0 (not EOF) or X=&FF (EOF)', align=Align.INLINE)
d.comment(0x888D, 'Store function code in FS cmd buffer', align=Align.INLINE)
d.comment(0x8890, 'A=6? (delete)', align=Align.INLINE)
d.comment(0x8892, 'Yes: jump to delete handler', align=Align.INLINE)
d.comment(0x8894, 'A>=7: unsupported, fall through to return', align=Align.INLINE)
d.comment(0x8896, 'A=5? (read catalogue info)', align=Align.INLINE)
d.comment(0x8898, 'Yes: jump to read info handler', align=Align.INLINE)
d.comment(0x889A, 'A=4? (write attributes only)', align=Align.INLINE)
d.comment(0x889C, 'Yes: jump to write attrs handler', align=Align.INLINE)
d.comment(0x889E, 'A=1? (write all catalogue info)', align=Align.INLINE)
d.comment(0x88A0, 'Yes: jump to write-all handler', align=Align.INLINE)
d.comment(0x88A2, 'A=2 or 3: convert to param block offset', align=Align.INLINE)
d.comment(0x88A3, 'A*4: 2->8, 3->12', align=Align.INLINE)
d.comment(0x88A4, 'Y = A*4', align=Align.INLINE)
d.comment(0x88A5, 'Y = A*4 - 3 (load addr offset for A=2)', align=Align.INLINE)
d.comment(0x88A8, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x88AA, 'Load address byte from param block', align=Align.INLINE)
d.comment(0x88AC, 'Store to FS cmd data area', align=Align.INLINE)
d.comment(0x88AF, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x88B0, 'Next dest byte', align=Align.INLINE)
d.comment(0x88B1, 'Loop for 4 bytes', align=Align.INLINE)
d.comment(0x88B3, 'X=5: data extent for filename copy', align=Align.INLINE)
d.comment(0x88B7, 'A=1: encode protection from param block', align=Align.INLINE)
d.comment(0x88BA, 'Store encoded attrs at &0F0E', align=Align.INLINE)
d.comment(0x88BD, 'Y=9: source offset in param block', align=Align.INLINE)
d.comment(0x88BF, 'X=8: dest offset in cmd buffer', align=Align.INLINE)
d.comment(0x88C1, 'Load byte from param block', align=Align.INLINE)
d.comment(0x88C3, 'Store to FS cmd buffer', align=Align.INLINE)
d.comment(0x88C6, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x88C7, 'Next dest byte', align=Align.INLINE)
d.comment(0x88C8, 'Loop until X=0 (8 bytes copied)', align=Align.INLINE)
d.comment(0x88CA, 'X=&0A: data extent past attrs+addrs', align=Align.INLINE)
d.comment(0x88CC, 'Append filename to cmd buffer', align=Align.INLINE)
d.comment(0x88CF, 'Y=&13: fn code for FCSAVE (write attrs)', align=Align.INLINE)
d.comment(0x88D1, 'ALWAYS branch to send command', align=Align.INLINE)
d.comment(0x88D3, 'A=6: copy filename (delete)', align=Align.INLINE)
d.comment(0x88D6, 'Y=&14: fn code for FCDEL (delete)', align=Align.INLINE)

d.label(0x88D8, 'send_fs_cmd_v1')
d.comment(0x88D8, 'Set V=1 (BIT trick: &B3 has bit 6 set)', align=Align.INLINE)
d.comment(0x88DB, 'Send via prepare_fs_cmd_v (V=1 path)', align=Align.INLINE)

d.label(0x88DE, 'check_attrib_result')
d.comment(0x88DE, 'C=1: &D6 not-found, skip to return', align=Align.INLINE)
d.comment(0x88E0, 'C=0: success, copy reply to param block', align=Align.INLINE)
d.comment(0x88E2, 'A=4: encode attrs from param block', align=Align.INLINE)
d.comment(0x88E5, 'Store encoded attrs at &0F06', align=Align.INLINE)
d.comment(0x88E8, 'X=2: data extent (1 attr byte + fn)', align=Align.INLINE)
d.comment(0x88EA, 'ALWAYS branch to append filename', align=Align.INLINE)
d.comment(0x88EC, 'X=1: filename only, no data extent', align=Align.INLINE)
d.comment(0x88EE, 'Copy filename to cmd buffer', align=Align.INLINE)
d.comment(0x88F1, 'Y=&12: fn code for FCEXAM (read info)', align=Align.INLINE)
d.comment(0x88F6, 'Save object type from FS reply', align=Align.INLINE)
d.comment(0x88F9, 'Clear reply byte (X=0 on success)', align=Align.INLINE)
d.comment(0x88FC, 'Clear length high byte in reply', align=Align.INLINE)
d.comment(0x88FF, 'Decode 5-bit access byte from FS reply', align=Align.INLINE)
d.comment(0x8902, 'Y=&0E: attrs offset in param block', align=Align.INLINE)
d.comment(0x8904, 'Store decoded attrs at param block +&0E', align=Align.INLINE)
d.comment(0x8906, 'Y=&0D: start copy below attrs', align=Align.INLINE)
d.comment(0x8907, 'X=&0C: copy from reply offset &0C down', align=Align.INLINE)
d.comment(0x8909, 'Load reply byte (load/exec/length)', align=Align.INLINE)
d.comment(0x890C, 'Store to param block', align=Align.INLINE)
d.comment(0x890E, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x890F, 'Next source byte', align=Align.INLINE)
d.comment(0x8910, 'Loop until X=0 (12 bytes copied)', align=Align.INLINE)
d.comment(0x8912, 'X=0 -> X=2 for length high copy', align=Align.INLINE)
d.comment(0x8913, 'INX again: X=2', align=Align.INLINE)
d.comment(0x8914, 'Y=&11: length high dest in param block', align=Align.INLINE)
d.comment(0x8916, 'Load length high byte from reply', align=Align.INLINE)
d.comment(0x8919, 'Store to param block', align=Align.INLINE)
d.comment(0x891B, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x891C, 'Next source byte', align=Align.INLINE)
d.comment(0x891D, 'Loop for 3 length-high bytes', align=Align.INLINE)
d.comment(0x891F, 'Return object type in A', align=Align.INLINE)

d.label(0x8922, 'attrib_error_exit')
d.comment(0x8922, 'A>=0: branch to restore_args_return', align=Align.INLINE)
d.comment(0x8924, 'Save A/X/Y registers for later restore', align=Align.INLINE)
d.comment(0x8927, 'Function >= 3?', align=Align.INLINE)
d.comment(0x8929, 'A>=3 (ensure/flush): no-op for NFS', align=Align.INLINE)
d.comment(0x892B, 'Test file handle', align=Align.INLINE)
d.comment(0x892D, 'Y=0: FS-level query, not per-file', align=Align.INLINE)
d.comment(0x892F, 'Convert handle to bitmask', align=Align.INLINE)
d.comment(0x8932, 'Store bitmask as first cmd data byte', align=Align.INLINE)
d.comment(0x8935, 'LSR splits A: C=1 means write (A=1)', align=Align.INLINE)
d.comment(0x8936, 'Store function code to cmd data byte 2', align=Align.INLINE)
d.comment(0x8939, 'C=1: write path, copy ptr from caller', align=Align.INLINE)
d.comment(0x893B, 'Y=&0C: FCRDSE (read sequential pointer)', align=Align.INLINE)
d.comment(0x893D, 'X=2: 3 data bytes in command', align=Align.INLINE)
d.comment(0x893F, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8942, 'Clear last-byte flag on success', align=Align.INLINE)
d.comment(0x8944, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x8946, 'Y=2: copy 3 bytes of file pointer', align=Align.INLINE)
d.comment(0x8948, 'Zero high byte of 3-byte pointer', align=Align.INLINE)

d.label(0x894A, 'copy_fileptr_reply')
d.comment(0x894A, 'Read reply byte from FS cmd data', align=Align.INLINE)
d.comment(0x894D, "Store to caller's control block", align=Align.INLINE)
d.comment(0x894F, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8950, 'Next source byte', align=Align.INLINE)
d.comment(0x8951, 'Loop for all 3 bytes', align=Align.INLINE)

d.label(0x8953, 'argsv_check_return')
d.comment(0x8953, 'C=0 (read): return to caller', align=Align.INLINE)
d.comment(0x8955, 'Save bitmask for set_fs_flag later', align=Align.INLINE)
d.comment(0x8956, 'Push bitmask', align=Align.INLINE)
d.comment(0x8957, 'Y=3: copy 4 bytes of file pointer', align=Align.INLINE)

d.label(0x8959, 'copy_fileptr_to_cmd')
d.comment(0x8959, "Read caller's pointer byte", align=Align.INLINE)
d.comment(0x895B, 'Store to FS command data area', align=Align.INLINE)
d.comment(0x895E, 'Next source byte', align=Align.INLINE)
d.comment(0x895F, 'Next destination byte', align=Align.INLINE)
d.comment(0x8960, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8962, 'Y=&0D: FCWRSE (write sequential pointer)', align=Align.INLINE)
d.comment(0x8964, 'X=5: 6 data bytes in command', align=Align.INLINE)
d.comment(0x8966, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8969, 'Save not-found status from X', align=Align.INLINE)
d.comment(0x896B, 'Recover bitmask for EOF hint update', align=Align.INLINE)
d.comment(0x896C, 'Set EOF hint bit for this handle', align=Align.INLINE)
d.comment(0x896F, 'A = saved function code / command', align=Align.INLINE)

d.label(0x8971, 'restore_xy_return')
d.comment(0x8971, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x8973, 'Y = saved control block ptr high', align=Align.INLINE)
d.comment(0x8975, 'Return to MOS with registers restored', align=Align.INLINE)

d.label(0x8976, 'argsv_fs_query')
d.comment(0x8976, 'Y=0: FS-level queries (no file handle)', align=Align.INLINE)
d.comment(0x8978, 'A=2: FS-level ensure (write extent)', align=Align.INLINE)
d.comment(0x897A, 'A>=3: FS command (ARGSV write)', align=Align.INLINE)
d.comment(0x897C, 'Y = A = byte count for copy loop', align=Align.INLINE)
d.comment(0x897D, 'A!=0: copy command context block', align=Align.INLINE)
d.comment(0x897F, "FS number 5 (loaded as &0A, LSR'd)", align=Align.INLINE)

d.label(0x8981, 'halve_args_a')
d.comment(0x8981, 'Shared: halve A (A=0 or A=2 paths)', align=Align.INLINE)
d.comment(0x8982, 'Return with A = FS number or 1', align=Align.INLINE)
d.comment(0x8984, "Copy command context to caller's block", align=Align.INLINE)
d.comment(0x8987, "Store to caller's parameter block", align=Align.INLINE)
d.comment(0x8989, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x898A, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x898C, 'Y=&FF after loop; fill high bytes', align=Align.INLINE)
d.comment(0x898E, 'Set 32-bit result bytes 2-3 to &FF', align=Align.INLINE)
d.comment(0x8994, 'Save A/X/Y and set up pointers', align=Align.INLINE)
d.comment(0x8997, 'SEC distinguishes open (A>0) from close', align=Align.INLINE)
d.comment(0x899C, 'A=0: close file(s)', align=Align.INLINE)
d.comment(0x899E, 'Valid open modes: &40, &80, &C0 only', align=Align.INLINE)
d.comment(0x89A0, 'Invalid mode bits: return', align=Align.INLINE)
d.comment(0x89A2, 'A = original mode byte', align=Align.INLINE)
d.comment(0x89A3, 'Convert MOS mode to FS protocol flags', align=Align.INLINE)
d.comment(0x89A5, 'ASL: shift mode bits left', align=Align.INLINE)
d.comment(0x89A6, 'Flag 1: read/write direction', align=Align.INLINE)
d.comment(0x89A9, 'ROL: Flag 2 into bit 0', align=Align.INLINE)
d.comment(0x89AA, 'Flag 2: create vs existing file', align=Align.INLINE)
d.comment(0x89AD, 'Parse filename from command line', align=Align.INLINE)
d.comment(0x89B0, 'X=2: copy after 2-byte flags', align=Align.INLINE)
d.comment(0x89B2, 'Copy filename to FS command buffer', align=Align.INLINE)
d.comment(0x89B5, 'Y=6: FS function code FCOPEN', align=Align.INLINE)
d.comment(0x89B7, 'Set V flag from l83b3 bit 6', align=Align.INLINE)
d.comment(0x89BA, 'Build and send FS open command', align=Align.INLINE)
d.comment(0x89BD, 'Error: restore and return', align=Align.INLINE)
d.comment(0x89BF, 'Load reply handle from FS', align=Align.INLINE)
d.comment(0x89C2, 'X = new file handle', align=Align.INLINE)
d.comment(0x89C3, 'Set EOF hint + sequence bits', align=Align.INLINE)
d.comment(0x89CA, 'ALWAYS branch to restore and return', align=Align.INLINE)
d.comment(0x89CC, 'A = handle (Y preserved in A)', align=Align.INLINE)
d.comment(0x89CD, 'Y>0: close single file', align=Align.INLINE)
d.comment(0x89CF, 'Close SPOOL/EXEC before FS close-all', align=Align.INLINE)
d.comment(0x89D4, 'Y=0: close all handles on server', align=Align.INLINE)
d.comment(0x89D6, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x89E0, 'Reply handle for flag update', align=Align.INLINE)
d.comment(0x89E3, 'Update EOF/sequence tracking bits', align=Align.INLINE)

d.label(0x89E6, 'close_opt_return')
d.comment(0x89E6, 'C=0: restore A/X/Y and return', align=Align.INLINE)
d.comment(0x89E8, 'Entry from fscv_0_opt (close-all path)', align=Align.INLINE)
d.comment(0x89EA, 'Is it *OPT 4,Y?', align=Align.INLINE)
d.comment(0x89EC, 'No: check for *OPT 1', align=Align.INLINE)
d.comment(0x89EE, 'Y must be 0-3 for boot option', align=Align.INLINE)
d.comment(0x89F0, 'Y < 4: valid boot option', align=Align.INLINE)

d.label(0x89F2, 'check_opt1')
d.comment(0x89F2, 'Not *OPT 4: check for *OPT 1', align=Align.INLINE)
d.comment(0x89F3, 'Not *OPT 1 either: bad option', align=Align.INLINE)

d.label(0x89F5, 'set_messages_flag')
d.comment(0x89F5, 'Set local messages flag (*OPT 1,Y)', align=Align.INLINE)
d.comment(0x89F8, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x89FA, 'Error index 7 (Bad option)', align=Align.INLINE)
d.comment(0x89FC, 'Generate BRK error', align=Align.INLINE)
d.comment(0x89FF, 'Boot option value in FS command', align=Align.INLINE)
d.comment(0x8A02, 'Y=&16: FS function code FCOPT', align=Align.INLINE)
d.comment(0x8A07, 'Restore Y from saved value', align=Align.INLINE)
d.comment(0x8A09, 'Cache boot option locally', align=Align.INLINE)

d.label(0x8A0C, 'opt_return')
d.comment(0x8A0C, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x8A0E, 'Y=9: adjust 9 address bytes', align=Align.INLINE)
d.comment(0x8A10, 'Adjust with carry clear', align=Align.INLINE)
d.comment(0x8A13, 'Y=1: adjust 1 address byte', align=Align.INLINE)
d.comment(0x8A15, 'C=0 for address adjustment', align=Align.INLINE)

d.label(0x8A18, 'adjust_addr_byte')

d.label(0x8A24, 'subtract_adjust')
d.comment(0x8A2E, 'Save A/X/Y to FS workspace', align=Align.INLINE)
d.comment(0x8A31, 'X = call number for range check', align=Align.INLINE)
d.comment(0x8A32, 'A=0: invalid, restore and return', align=Align.INLINE)
d.comment(0x8A34, 'Convert to 0-based (A=0..7)', align=Align.INLINE)
d.comment(0x8A35, 'Range check: must be 0-7', align=Align.INLINE)
d.comment(0x8A37, 'In range: continue to handler', align=Align.INLINE)

d.label(0x8A39, 'gbpb_invalid_exit')
d.comment(0x8A39, 'Out of range: restore args and return', align=Align.INLINE)
d.comment(0x8A3C, 'Recover 0-based function code', align=Align.INLINE)
d.comment(0x8A3D, 'Y=0: param block byte 0 (file handle)', align=Align.INLINE)
d.comment(0x8A3F, 'Save function code on stack', align=Align.INLINE)
d.comment(0x8A40, 'A>=4: info queries, dispatch separately', align=Align.INLINE)
d.comment(0x8A42, 'A<4: file read/write operations', align=Align.INLINE)
d.comment(0x8A44, 'Dispatch to OSGBPB 5-8 info handler', align=Align.INLINE)
d.comment(0x8A47, 'Get file handle from param block byte 0', align=Align.INLINE)
d.comment(0x8A49, 'Convert handle to bitmask for EOF flags', align=Align.INLINE)
d.comment(0x8A4C, 'Store handle in FS command data', align=Align.INLINE)
d.comment(0x8A4F, 'Y=&0B: start at param block byte 11', align=Align.INLINE)
d.comment(0x8A51, 'X=6: copy 6 bytes of transfer params', align=Align.INLINE)
d.comment(0x8A53, 'Load param block byte', align=Align.INLINE)
d.comment(0x8A55, 'Store to FS command buffer at &0F06+X', align=Align.INLINE)
d.comment(0x8A58, 'Previous param block byte', align=Align.INLINE)
d.comment(0x8A59, 'Skip param block offset 8 (the handle)', align=Align.INLINE)
d.comment(0x8A5B, 'Not at handle offset: continue', align=Align.INLINE)
d.comment(0x8A5D, 'Extra DEY to skip handle byte', align=Align.INLINE)
d.comment(0x8A5E, 'Decrement copy counter', align=Align.INLINE)
d.comment(0x8A5F, 'Loop for all 6 bytes', align=Align.INLINE)
d.comment(0x8A61, 'Recover function code from stack', align=Align.INLINE)
d.comment(0x8A62, 'LSR: odd=read (C=1), even=write (C=0)', align=Align.INLINE)
d.comment(0x8A63, 'Save function code again (need C later)', align=Align.INLINE)
d.comment(0x8A64, 'Even (write): X stays 0', align=Align.INLINE)
d.comment(0x8A66, 'Odd (read): X=1', align=Align.INLINE)
d.comment(0x8A67, 'Store FS direction flag', align=Align.INLINE)
d.comment(0x8A6A, 'Y=&0B: command data extent', align=Align.INLINE)
d.comment(0x8A6C, 'Command &91=put, &92=get', align=Align.INLINE)
d.comment(0x8A6E, 'Recover function code', align=Align.INLINE)
d.comment(0x8A6F, 'Save again for later direction check', align=Align.INLINE)
d.comment(0x8A70, 'Even (write): keep &91 and Y=&0B', align=Align.INLINE)
d.comment(0x8A72, 'Odd (read): use &92 (get) instead', align=Align.INLINE)
d.comment(0x8A74, 'Read: one fewer data byte in command', align=Align.INLINE)

d.label(0x8A75, 'gbpb_write_path')
d.comment(0x8A75, 'Store port to FS command URD field', align=Align.INLINE)
d.comment(0x8A78, 'Save port for error recovery', align=Align.INLINE)
d.comment(0x8A7A, 'X=8: command data bytes', align=Align.INLINE)
d.comment(0x8A7C, 'Load handle from FS command data', align=Align.INLINE)
d.comment(0x8A7F, 'Build FS command with handle+flag', align=Align.INLINE)
d.comment(0x8A82, 'Save seq# for byte-stream flow control', align=Align.INLINE)
d.comment(0x8A84, 'Store to FS sequence number workspace', align=Align.INLINE)
d.comment(0x8A87, 'X=4: copy 4 address bytes', align=Align.INLINE)
d.comment(0x8A89, 'Set up source/dest from param block', align=Align.INLINE)
d.comment(0x8A8B, 'Store as source address', align=Align.INLINE)
d.comment(0x8A8E, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x8A91, 'Skip 4 bytes to reach transfer length', align=Align.INLINE)
d.comment(0x8A94, 'Dest = source + length', align=Align.INLINE)
d.comment(0x8A96, 'Store as end address', align=Align.INLINE)
d.comment(0x8A99, 'Back 3 to align for next iteration', align=Align.INLINE)
d.comment(0x8A9C, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8A9D, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8A9F, 'X=1 after loop', align=Align.INLINE)
d.comment(0x8AA0, 'Copy CSD data to command buffer', align=Align.INLINE)
d.comment(0x8AA3, 'Store at &0F06+X', align=Align.INLINE)
d.comment(0x8AA6, 'Decrement counter', align=Align.INLINE)
d.comment(0x8AA7, 'Loop for X=1,0', align=Align.INLINE)
d.comment(0x8AA9, 'Odd (read): send data to FS first', align=Align.INLINE)
d.comment(0x8AAA, 'Non-zero: skip write path', align=Align.INLINE)
d.comment(0x8AAC, 'Load port for transfer setup', align=Align.INLINE)
d.comment(0x8AAF, 'Transfer data blocks to fileserver', align=Align.INLINE)
d.comment(0x8AB2, 'Carry set: transfer error', align=Align.INLINE)

d.label(0x8AB4, 'gbpb_read_path')
d.comment(0x8AB4, 'Read path: receive data blocks from FS', align=Align.INLINE)

d.label(0x8AB7, 'wait_fs_reply')
d.comment(0x8AB7, 'Wait for FS reply command', align=Align.INLINE)
d.comment(0x8ABA, 'Load handle mask for EOF flag update', align=Align.INLINE)
d.comment(0x8ABC, 'Check FS reply: bit 7 = not at EOF', align=Align.INLINE)
d.comment(0x8ABF, 'Bit 7 set: not EOF, skip clear', align=Align.INLINE)
d.comment(0x8AC1, 'At EOF: clear EOF hint for this handle', align=Align.INLINE)

d.label(0x8AC4, 'skip_clear_flag')
d.comment(0x8AC4, 'Set EOF hint flag (may be at EOF)', align=Align.INLINE)
d.comment(0x8AC7, 'Direction=0: forward adjustment', align=Align.INLINE)
d.comment(0x8AC9, 'Adjust param block addrs by +9 bytes', align=Align.INLINE)
d.comment(0x8ACC, 'Direction=&FF: reverse adjustment', align=Align.INLINE)
d.comment(0x8ACE, 'SEC for reverse subtraction', align=Align.INLINE)
d.comment(0x8ACF, 'Adjust param block addrs (reverse)', align=Align.INLINE)
d.comment(0x8AD2, 'Shift bit 7 into C for return flag', align=Align.INLINE)
d.comment(0x8AD5, 'Return via restore_args path', align=Align.INLINE)

d.label(0x8AD8, 'get_disc_title')
d.comment(0x8AD8, 'Y=&15: function code for disc title', align=Align.INLINE)
d.comment(0x8ADA, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8ADD, 'Load boot option from FS workspace', align=Align.INLINE)
d.comment(0x8AE0, 'Store boot option in reply area', align=Align.INLINE)
d.comment(0x8AE3, 'X=0: reply data start offset', align=Align.INLINE)
d.comment(0x8AE5, 'Clear reply buffer high byte', align=Align.INLINE)
d.comment(0x8AE7, 'A=&12: 18 bytes of reply data', align=Align.INLINE)
d.comment(0x8AE9, 'Store as byte count for copy', align=Align.INLINE)
d.comment(0x8AEB, 'ALWAYS branch to copy_reply_to_caller', align=Align.INLINE)
d.comment(0x8AED, 'Y=4: check param block byte 4', align=Align.INLINE)
d.comment(0x8AEF, 'Check if destination is in Tube space', align=Align.INLINE)
d.comment(0x8AF2, 'No Tube: skip Tube address check', align=Align.INLINE)
d.comment(0x8AF4, 'Compare Tube flag with addr byte 4', align=Align.INLINE)
d.comment(0x8AF6, 'Mismatch: not Tube space', align=Align.INLINE)
d.comment(0x8AF9, 'Y=3: subtract addr byte 3 from flag', align=Align.INLINE)

d.label(0x8AFB, 'store_tube_flag')
d.comment(0x8AFB, 'Non-zero = Tube transfer required', align=Align.INLINE)
d.comment(0x8AFD, 'Copy param block bytes 1-4 to workspace', align=Align.INLINE)
d.comment(0x8AFF, 'Store to &BD+Y workspace area', align=Align.INLINE)
d.comment(0x8B02, 'Previous byte', align=Align.INLINE)
d.comment(0x8B03, 'Loop for bytes 3,2,1', align=Align.INLINE)
d.comment(0x8B05, 'Sub-function: AND #3 of (original A - 4)', align=Align.INLINE)
d.comment(0x8B06, 'Mask to 0-3 (OSGBPB 5-8 → 0-3)', align=Align.INLINE)
d.comment(0x8B08, 'A=0 (OSGBPB 5): read disc title', align=Align.INLINE)
d.comment(0x8B0A, 'LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)', align=Align.INLINE)
d.comment(0x8B0B, 'A=0 (OSGBPB 6): read CSD/LIB name', align=Align.INLINE)
d.comment(0x8B0D, 'C=1 (OSGBPB 8): read filenames from dir', align=Align.INLINE)

d.label(0x8B0F, 'gbpb6_read_name')
d.comment(0x8B0F, 'Y=0 for CSD or carry for fn code select', align=Align.INLINE)
d.comment(0x8B10, 'Get CSD/LIB/URD handles for FS command', align=Align.INLINE)
d.comment(0x8B13, 'Store CSD handle in command buffer', align=Align.INLINE)
d.comment(0x8B16, 'Load LIB handle from workspace', align=Align.INLINE)
d.comment(0x8B19, 'Store LIB handle in command buffer', align=Align.INLINE)
d.comment(0x8B1C, 'Load URD handle from workspace', align=Align.INLINE)
d.comment(0x8B1F, 'Store URD handle in command buffer', align=Align.INLINE)
d.comment(0x8B22, 'X=&12: buffer extent for command data', align=Align.INLINE)
d.comment(0x8B24, 'Store X as function code in header', align=Align.INLINE)
d.comment(0x8B27, '&0D = 13 bytes of reply data expected', align=Align.INLINE)
d.comment(0x8B29, 'Store reply length in command buffer', align=Align.INLINE)
d.comment(0x8B2C, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8B2E, 'LSR: &0D >> 1 = 6', align=Align.INLINE)
d.comment(0x8B2F, 'Store as command data byte', align=Align.INLINE)
d.comment(0x8B32, 'CLC for standard FS path', align=Align.INLINE)
d.comment(0x8B38, 'INX: X=1 after build_send_fs_cmd', align=Align.INLINE)
d.comment(0x8B39, 'Store X as reply start offset', align=Align.INLINE)
d.comment(0x8B3B, "Copy FS reply to caller's buffer", align=Align.INLINE)
d.comment(0x8B3D, 'Non-zero: use Tube transfer path', align=Align.INLINE)
d.comment(0x8B3F, 'X = reply start offset', align=Align.INLINE)
d.comment(0x8B41, 'Y = reply buffer high byte', align=Align.INLINE)

d.label(0x8B43, 'copy_reply_bytes')
d.comment(0x8B43, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B46, "Store to caller's buffer", align=Align.INLINE)
d.comment(0x8B48, 'Next source byte', align=Align.INLINE)
d.comment(0x8B49, 'Next destination byte', align=Align.INLINE)
d.comment(0x8B4A, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8B4C, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8B4E, 'ALWAYS branch to exit', align=Align.INLINE)

d.label(0x8B50, 'tube_transfer')
d.comment(0x8B50, 'Claim Tube transfer channel', align=Align.INLINE)
d.comment(0x8B53, 'A=1: Tube claim type 1 (write)', align=Align.INLINE)
d.comment(0x8B55, 'X = param block address low', align=Align.INLINE)
d.comment(0x8B57, 'Y = param block address high', align=Align.INLINE)
d.comment(0x8B59, 'INX: advance past byte 0', align=Align.INLINE)
d.comment(0x8B5A, 'No page wrap: keep Y', align=Align.INLINE)
d.comment(0x8B5C, 'Page wrap: increment high byte', align=Align.INLINE)

d.label(0x8B5D, 'no_page_wrap')
d.comment(0x8B5D, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x8B60, 'X = reply data start offset', align=Align.INLINE)
d.comment(0x8B62, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B65, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x8B68, 'Next source byte', align=Align.INLINE)
d.comment(0x8B69, 'Delay loop for slow Tube co-processor', align=Align.INLINE)

d.label(0x8B6B, 'wait_tube_delay')
d.comment(0x8B6B, 'Decrement delay counter', align=Align.INLINE)
d.comment(0x8B6C, 'Loop until delay complete', align=Align.INLINE)
d.comment(0x8B6E, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8B70, 'Loop until all bytes sent to Tube', align=Align.INLINE)
d.comment(0x8B72, 'Release Tube after transfer complete', align=Align.INLINE)
d.comment(0x8B74, 'Release Tube address claim', align=Align.INLINE)

d.label(0x8B77, 'gbpb_done')
d.comment(0x8B77, 'Return via restore_args path', align=Align.INLINE)

d.label(0x8B7A, 'gbpb8_read_dir')
d.comment(0x8B7A, 'OSGBPB 8: read filenames from dir', align=Align.INLINE)
d.comment(0x8B7C, 'Byte 9: number of entries to read', align=Align.INLINE)
d.comment(0x8B7E, 'Store as reply count in command buffer', align=Align.INLINE)
d.comment(0x8B81, 'Y=5: byte 5 = starting entry number', align=Align.INLINE)
d.comment(0x8B83, 'Load starting entry number', align=Align.INLINE)
d.comment(0x8B85, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8B88, 'X=&0D: command data extent', align=Align.INLINE)
d.comment(0x8B8A, 'Store extent in command buffer', align=Align.INLINE)
d.comment(0x8B8D, 'Y=2: function code for dir read', align=Align.INLINE)
d.comment(0x8B8F, 'Store 2 as reply data start offset', align=Align.INLINE)
d.comment(0x8B91, 'Store 2 as command data byte', align=Align.INLINE)
d.comment(0x8B94, 'Y=3: function code for header read', align=Align.INLINE)
d.comment(0x8B98, 'X=0 after FS command completes', align=Align.INLINE)
d.comment(0x8B9A, 'Load reply entry count', align=Align.INLINE)
d.comment(0x8B9D, 'Store at param block byte 0 (X=0)', align=Align.INLINE)
d.comment(0x8B9F, 'Load entries-read count from reply', align=Align.INLINE)
d.comment(0x8BA2, 'Y=9: param block byte 9', align=Align.INLINE)
d.comment(0x8BA4, 'Add to starting entry number', align=Align.INLINE)
d.comment(0x8BA6, 'Update param block with new position', align=Align.INLINE)
d.comment(0x8BA8, 'Load total reply length', align=Align.INLINE)
d.comment(0x8BAA, 'Subtract header (7 bytes) from reply len', align=Align.INLINE)
d.comment(0x8BAC, 'Store adjusted length in command buffer', align=Align.INLINE)
d.comment(0x8BAF, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8BB1, 'Zero bytes: skip copy', align=Align.INLINE)
d.comment(0x8BB3, "Copy reply data to caller's buffer", align=Align.INLINE)

d.label(0x8BB6, 'skip_copy_reply')
d.comment(0x8BB6, 'X=2: clear 3 bytes', align=Align.INLINE)

d.label(0x8BB8, 'zero_cmd_bytes')
d.comment(0x8BB8, 'Zero out &0F07+X area', align=Align.INLINE)
d.comment(0x8BBB, 'Next byte', align=Align.INLINE)
d.comment(0x8BBC, 'Loop for X=2,1,0', align=Align.INLINE)
d.comment(0x8BBE, 'Adjust pointer by +1 (one filename read)', align=Align.INLINE)
d.comment(0x8BC1, 'SEC for reverse adjustment', align=Align.INLINE)
d.comment(0x8BC2, 'Reverse adjustment for updated counter', align=Align.INLINE)
d.comment(0x8BC4, 'Load entries-read count', align=Align.INLINE)
d.comment(0x8BC7, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8BCA, 'Adjust param block addresses', align=Align.INLINE)
d.comment(0x8BCD, 'Z=1: all done, exit', align=Align.INLINE)
d.comment(0x8BCF, 'A=&C3: Tube claim with retry', align=Align.INLINE)
d.comment(0x8BD1, 'Request Tube address claim', align=Align.INLINE)
d.comment(0x8BD4, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x8BD6, 'Tube claimed successfully', align=Align.INLINE)
d.comment(0x8BD7, 'Save A/X/Y and set up command ptr', align=Align.INLINE)
d.comment(0x8BDA, 'X=&FF: table index (pre-incremented)', align=Align.INLINE)
d.comment(0x8BDC, 'Disable column formatting', align=Align.INLINE)

d.label(0x8BDE, 'scan_cmd_table')
d.comment(0x8BDE, 'Y=&FF: input index (pre-incremented)', align=Align.INLINE)
d.comment(0x8BE0, 'Advance input pointer', align=Align.INLINE)
d.comment(0x8BE1, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8BE2, 'Load table character', align=Align.INLINE)
d.comment(0x8BE5, 'Bit 7: end of name, dispatch', align=Align.INLINE)
d.comment(0x8BE7, 'XOR input char with table char', align=Align.INLINE)
d.comment(0x8BE9, 'Case-insensitive (clear bit 5)', align=Align.INLINE)
d.comment(0x8BEB, 'Match: continue comparing', align=Align.INLINE)
d.comment(0x8BED, 'Mismatch: back up table pointer', align=Align.INLINE)
d.comment(0x8BEE, 'Skip to end of table entry', align=Align.INLINE)
d.comment(0x8BEF, 'Load table byte', align=Align.INLINE)
d.comment(0x8BF2, 'Loop until bit 7 set (end marker)', align=Align.INLINE)
d.comment(0x8BF4, "Check input for '.' abbreviation", align=Align.INLINE)
d.comment(0x8BF6, 'Skip past handler high byte', align=Align.INLINE)
d.comment(0x8BF7, "Is input '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8BF9, 'No: try next table entry', align=Align.INLINE)
d.comment(0x8BFB, "Yes: skip '.' in input", align=Align.INLINE)
d.comment(0x8BFC, 'Back to handler high byte', align=Align.INLINE)
d.comment(0x8BFD, 'ALWAYS branch; dispatch via BMI', align=Align.INLINE)

d.label(0x8BFF, 'dispatch_cmd')
d.comment(0x8BFF, 'Push handler address high byte', align=Align.INLINE)
d.comment(0x8C00, 'Load handler address low byte', align=Align.INLINE)
d.comment(0x8C03, 'Push handler address low byte', align=Align.INLINE)
d.comment(0x8C04, 'Dispatch via RTS (addr-1 on stack)', align=Align.INLINE)
d.comment(0x8C05, "Match last char against '.' for *I. abbreviation", align=Align.INLINE)
d.comment(0x8C21, 'X=3: column count for multi-column layout', align=Align.INLINE)
d.comment(0x8C23, 'CRFLAG=3: first entry will trigger newline', align=Align.INLINE)
d.comment(0x8C25, 'Y=0: initialise column counter', align=Align.INLINE)
d.comment(0x8C27, 'A=&0B: examine argument count', align=Align.INLINE)

d.label(0x8C29, 'init_cat_params')
d.comment(0x8C29, 'Store examine argument count', align=Align.INLINE)
d.comment(0x8C2B, 'Store column count', align=Align.INLINE)
d.comment(0x8C2D, 'A=6: examine format type in command', align=Align.INLINE)
d.comment(0x8C2F, 'Store format type at &0F05', align=Align.INLINE)
d.comment(0x8C32, 'Set up command parameter pointers', align=Align.INLINE)
d.comment(0x8C35, 'X=1: copy dir name at cmd offset 1', align=Align.INLINE)
d.comment(0x8C37, 'Copy directory name to command buffer', align=Align.INLINE)
d.comment(0x8C3F, 'X=3: start printing from reply offset 3', align=Align.INLINE)
d.comment(0x8C41, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0x8C44, "Print '('", align=Align.INLINE)
d.comment(0x8C48, 'Load station number from FS reply', align=Align.INLINE)
d.comment(0x8C4B, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x8C4E, "Print ')     '", align=Align.INLINE)
d.comment(0x8C5A, 'Non-zero: Public access', align=Align.INLINE)
d.comment(0x8C5C, "Print 'Owner' + CR", align=Align.INLINE)

d.label(0x8C67, 'print_public')
d.comment(0x8C67, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0x8C76, 'X=1: past command code byte', align=Align.INLINE)
d.comment(0x8C77, 'Y=&10: print 16 characters', align=Align.INLINE)
d.comment(0x8C79, 'Print disc/CSD name from reply', align=Align.INLINE)
d.comment(0x8C7C, "Print '    Option '", align=Align.INLINE)
d.comment(0x8C8D, 'X = boot option for name table lookup', align=Align.INLINE)
d.comment(0x8C8E, 'Print boot option as hex digit', align=Align.INLINE)
d.comment(0x8C91, "Print ' ('", align=Align.INLINE)
d.comment(0x8CA1, 'Next character', align=Align.INLINE)
d.comment(0x8CA2, 'Continue printing option name', align=Align.INLINE)

d.label(0x8CA4, 'done_option_name')
d.comment(0x8CA4, "Print ')' + CR + 'Dir. '", align=Align.INLINE)
d.comment(0x8CC2, 'Print library name', align=Align.INLINE)

d.label(0x8CC8, 'fetch_dir_batch')
d.comment(0x8CC8, 'Store entry start offset for request', align=Align.INLINE)
d.comment(0x8CCB, 'Save start offset in zero page for loop', align=Align.INLINE)
d.comment(0x8CCD, 'Load examine arg count for batch size', align=Align.INLINE)
d.comment(0x8CCF, 'Store as request count at &0F07', align=Align.INLINE)
d.comment(0x8CD2, 'Load column count for display format', align=Align.INLINE)
d.comment(0x8CD4, 'Store column count in command data', align=Align.INLINE)
d.comment(0x8CD7, 'X=3: copy directory name at offset 3', align=Align.INLINE)
d.comment(0x8CD9, 'Append directory name to examine command', align=Align.INLINE)
d.comment(0x8CE1, 'X past command code byte in reply', align=Align.INLINE)
d.comment(0x8CE2, 'Load entry count from reply', align=Align.INLINE)

d.label(0x8CE7, 'process_entries')
d.comment(0x8CE7, 'Save entry count for batch processing', align=Align.INLINE)

d.label(0x8CE8, 'scan_entry_terminator')
d.comment(0x8CE8, 'Advance Y past entry data bytes', align=Align.INLINE)
d.comment(0x8CE9, 'Read entry byte from reply buffer', align=Align.INLINE)
d.comment(0x8CEC, 'Loop until high-bit terminator found', align=Align.INLINE)
d.comment(0x8CEE, 'Store terminator as print boundary', align=Align.INLINE)
d.comment(0x8CF1, 'Print/format this directory entry', align=Align.INLINE)
d.comment(0x8CF4, 'Restore entry count from stack', align=Align.INLINE)
d.comment(0x8CF5, 'CLC for addition', align=Align.INLINE)
d.comment(0x8CF6, 'Advance start offset by entry count', align=Align.INLINE)
d.comment(0x8CF8, 'Y = new entry start offset', align=Align.INLINE)
d.comment(0x8CF9, 'More entries: fetch next batch', align=Align.INLINE)
d.comment(0x8CFB, 'Y=&0A: default print 10 characters', align=Align.INLINE)
d.comment(0x8CFD, 'Load reply byte at offset X', align=Align.INLINE)
d.comment(0x8D03, 'Next reply byte', align=Align.INLINE)
d.comment(0x8D04, 'Decrement character count', align=Align.INLINE)
d.comment(0x8D05, 'Loop for remaining characters', align=Align.INLINE)
d.comment(0x8D63, 'X=4: print 4 hex bytes', align=Align.INLINE)
d.comment(0x8D65, 'Load byte from parameter block', align=Align.INLINE)
d.comment(0x8D67, 'Print as two hex digits', align=Align.INLINE)
d.comment(0x8D6A, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8D6B, 'Count down', align=Align.INLINE)
d.comment(0x8D6C, 'Loop until 4 bytes printed', align=Align.INLINE)
d.comment(0x8D6E, 'A=space character', align=Align.INLINE)
d.comment(0x8D75, 'Start writing at &0F05 (after cmd header)', align=Align.INLINE)
d.comment(0x8D7B, 'Store to FS command buffer (&0F05+X)', align=Align.INLINE)
d.comment(0x8D7F, 'Advance source pointer', align=Align.INLINE)
d.comment(0x8D84, 'Return; X = next free position in buffer', align=Align.INLINE)
d.comment(0x8D89, 'X=0: start from first reply byte', align=Align.INLINE)
d.comment(0x8D8B, 'Load byte from FS reply buffer', align=Align.INLINE)
d.comment(0x8D8E, 'Bit 7 set: end of string, return', align=Align.INLINE)
d.comment(0x8D90, 'Non-zero: print character', align=Align.INLINE)
d.comment(0x8D92, 'Null byte: check column counter', align=Align.INLINE)
d.comment(0x8D94, 'Negative: print CR (no columns)', align=Align.INLINE)
d.comment(0x8D96, 'Advance column counter', align=Align.INLINE)
d.comment(0x8D97, 'Transfer to A for modulo', align=Align.INLINE)
d.comment(0x8D98, 'Modulo 4 columns', align=Align.INLINE)
d.comment(0x8D9A, 'Update column counter', align=Align.INLINE)
d.comment(0x8D9C, 'Column 0: start new line', align=Align.INLINE)
d.comment(0x8D9E, 'Print 2-space column separator', align=Align.INLINE)

d.label(0x8DAA, 'next_dir_entry')
d.comment(0x8DAA, 'Next byte in reply buffer', align=Align.INLINE)
d.comment(0x8DAB, 'Loop until end of buffer', align=Align.INLINE)
d.comment(0x8DB0, 'Y = value to print', align=Align.INLINE)
d.comment(0x8DB1, 'Divisor = 100 (hundreds digit)', align=Align.INLINE)
d.comment(0x8DB3, 'Print hundreds digit', align=Align.INLINE)
d.comment(0x8DB6, 'Divisor = 10 (tens digit)', align=Align.INLINE)
d.comment(0x8DB8, 'Print tens digit', align=Align.INLINE)
d.comment(0x8DBB, 'Divisor = 1; fall through to units', align=Align.INLINE)
d.comment(0x8DBD, 'Save divisor to workspace', align=Align.INLINE)
d.comment(0x8DBF, 'A = dividend (from Y)', align=Align.INLINE)
d.comment(0x8DC0, "X = &2F = ASCII '0' - 1", align=Align.INLINE)
d.comment(0x8DC2, 'Prepare for subtraction', align=Align.INLINE)

d.label(0x8DC3, 'divide_subtract')
d.comment(0x8DC3, 'Count one subtraction (next digit value)', align=Align.INLINE)
d.comment(0x8DC4, 'A = A - divisor', align=Align.INLINE)
d.comment(0x8DC6, 'Loop while A >= 0 (borrow clear)', align=Align.INLINE)
d.comment(0x8DC8, 'Undo last subtraction: A = remainder', align=Align.INLINE)
d.comment(0x8DCA, 'Y = remainder for caller', align=Align.INLINE)
d.comment(0x8DCB, 'A = X = ASCII digit character', align=Align.INLINE)

d.label(0x8DCC, 'print_digit')
d.comment(0x8DCF, 'Parse filename from command line', align=Align.INLINE)
d.comment(0x8DD2, 'Copy filename to FS command buffer', align=Align.INLINE)
d.comment(0x8DD5, 'Y=0: start of text for GSINIT', align=Align.INLINE)
d.comment(0x8DD7, 'CLC before GSINIT call', align=Align.INLINE)
d.comment(0x8DD8, 'GSINIT/GSREAD: skip past the filename', align=Align.INLINE)

d.label(0x8DDB, 'skip_gs_filename')
d.comment(0x8DDB, 'Read next filename character', align=Align.INLINE)
d.comment(0x8DDE, 'C=0: more characters, keep reading', align=Align.INLINE)
d.comment(0x8DE0, 'Skip spaces after filename', align=Align.INLINE)
d.comment(0x8DE3, 'Calculate context addr = text ptr + Y', align=Align.INLINE)
d.comment(0x8DE4, 'Y = offset past filename end', align=Align.INLINE)
d.comment(0x8DE5, 'Add text pointer low byte', align=Align.INLINE)
d.comment(0x8DE7, 'Store context address low byte', align=Align.INLINE)
d.comment(0x8DEA, 'Load text pointer high byte', align=Align.INLINE)
d.comment(0x8DEC, 'Add carry from low byte addition', align=Align.INLINE)
d.comment(0x8DEE, 'Store context address high byte', align=Align.INLINE)
d.comment(0x8DF1, 'X=&0E: FS command buffer offset', align=Align.INLINE)
d.comment(0x8DF3, 'Store block offset for FS command', align=Align.INLINE)
d.comment(0x8DF5, 'A=&10: 16 bytes of command data', align=Align.INLINE)
d.comment(0x8DF7, 'Store options byte', align=Align.INLINE)
d.comment(0x8DF9, 'Store to FS workspace', align=Align.INLINE)
d.comment(0x8DFC, 'X=&4A: TXCB size for load command', align=Align.INLINE)
d.comment(0x8DFE, 'Y=5: FCCMND (load as command)', align=Align.INLINE)
d.comment(0x8E00, 'Send FS examine/load command', align=Align.INLINE)
d.comment(0x8E03, 'Check for Tube co-processor', align=Align.INLINE)
d.comment(0x8E06, 'No Tube: execute locally', align=Align.INLINE)
d.comment(0x8E08, 'Check load address upper bytes', align=Align.INLINE)
d.comment(0x8E0B, 'Continue address range check', align=Align.INLINE)
d.comment(0x8E0E, 'Carry set: not Tube space, exec locally', align=Align.INLINE)
d.comment(0x8E10, 'Claim Tube transfer channel', align=Align.INLINE)
d.comment(0x8E13, 'X=9: source offset in FS reply', align=Align.INLINE)
d.comment(0x8E15, 'Y=&0F: page &0F (FS command buffer)', align=Align.INLINE)
d.comment(0x8E17, 'A=4: Tube transfer type 4 (256-byte)', align=Align.INLINE)
d.comment(0x8E19, 'Transfer data to Tube co-processor', align=Align.INLINE)
d.comment(0x8E1C, 'Execute at load address via indirect JMP', align=Align.INLINE)
d.comment(0x8E1F, 'Save library handle from FS reply', align=Align.INLINE)
d.comment(0x8E22, 'SDISC path: skip CSD, jump to return', align=Align.INLINE)
d.comment(0x8E24, 'Store CSD handle from FS reply', align=Align.INLINE)

d.label(0x8E27, 'jmp_restore_args')
d.comment(0x8E27, 'Restore A/X/Y and return to caller', align=Align.INLINE)
d.comment(0x8E2A, 'Set carry: LOGIN path (copy + boot)', align=Align.INLINE)
d.comment(0x8E2B, 'Copy 4 bytes: boot option + 3 handles', align=Align.INLINE)
d.comment(0x8E2D, 'SDISC: skip boot option, copy handles only', align=Align.INLINE)
d.comment(0x8E2F, 'Load from FS reply (&0F05+X)', align=Align.INLINE)
d.comment(0x8E32, 'Store to handle workspace (&0E02+X)', align=Align.INLINE)

d.label(0x8E35, 'copy_handles_loop')
d.comment(0x8E35, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8E36, 'Loop while X >= 0', align=Align.INLINE)
d.comment(0x8E38, 'SDISC: done, restore args and return', align=Align.INLINE)
d.comment(0x8E3A, 'Y = boot option from FS workspace', align=Align.INLINE)
d.comment(0x8E3D, 'X = command string offset from table', align=Align.INLINE)
d.comment(0x8E40, 'Y = &8D (high byte of command address)', align=Align.INLINE)
d.comment(0x8E42, 'Execute boot command string via OSCLI', align=Align.INLINE)
d.comment(0x8E45, 'Load handle from &F0', align=Align.INLINE)
d.comment(0x8E5F, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8E62, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8E64, 'Load stored handle value', align=Align.INLINE)
d.comment(0x8E66, '&3F = unused/closed slot marker', align=Align.INLINE)
d.comment(0x8E68, 'Slot in use: return actual value', align=Align.INLINE)
d.comment(0x8E6A, 'Return 0 for closed/invalid handle', align=Align.INLINE)

d.label(0x8E6C, 'store_handle_return')
d.comment(0x8E6C, 'Store result back to &F0', align=Align.INLINE)
d.comment(0x8E6E, 'Return', align=Align.INLINE)
d.comment(0x8E6F, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8E72, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8E7E, 'Return', align=Align.INLINE)
d.comment(0x8E85, 'Only OSWORDs &0F-&13 (index 0-4)', align=Align.INLINE)
d.comment(0x8E87, 'Index >= 5: not ours, return', align=Align.INLINE)
d.comment(0x8E89, 'Dispatch via PHA/PHA/RTS table', align=Align.INLINE)
d.comment(0x8E8C, 'Y=2: restore 3 bytes (&AA-&AC)', align=Align.INLINE)

d.label(0x8E8E, 'copy_param_ptr')
d.comment(0x8E8E, 'Load saved param block byte', align=Align.INLINE)
d.comment(0x8E90, 'Restore to &AA-&AC', align=Align.INLINE)
d.comment(0x8E93, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8E94, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8E96, 'Return to service handler', align=Align.INLINE)
d.comment(0x8E97, 'X = sub-function code for table lookup', align=Align.INLINE)
d.comment(0x8E98, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x8E9B, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8E9C, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x8EA0, 'Y=2: save 3 bytes (&AA-&AC)', align=Align.INLINE)
d.comment(0x8EA2, 'Load param block pointer byte', align=Align.INLINE)
d.comment(0x8EA5, 'Save to NFS workspace via (net_rx_ptr)', align=Align.INLINE)
d.comment(0x8EA7, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8EA8, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8EAA, 'Y=0 after BPL exit; INY makes Y=1', align=Align.INLINE)
d.comment(0x8EAB, 'Read sub-function code from (&F0)+1', align=Align.INLINE)
d.comment(0x8EAD, 'Store Y=1 to &A9', align=Align.INLINE)
d.comment(0x8EAF, 'RTS dispatches to pushed handler address', align=Align.INLINE)
d.comment(0x8EC0, 'User TX CB in workspace page (high byte)', align=Align.INLINE)
d.comment(0x8EC2, 'Set param block high byte', align=Align.INLINE)
d.comment(0x8EC4, 'Set LTXCBP high byte for low-level TX', align=Align.INLINE)
d.comment(0x8EC6, '&6F: offset into workspace for user TXCB', align=Align.INLINE)
d.comment(0x8EC8, 'Set param block low byte', align=Align.INLINE)
d.comment(0x8ECA, 'Set LTXCBP low byte for low-level TX', align=Align.INLINE)
d.comment(0x8ECC, 'X=15: copy 16 bytes (OSWORD param block)', align=Align.INLINE)
d.comment(0x8ECE, 'Copy param block to user TX control block', align=Align.INLINE)
d.comment(0x8ED1, 'Start user transmit via BRIANX', align=Align.INLINE)
d.comment(0x8ED4, 'Set source high byte from workspace page', align=Align.INLINE)
d.comment(0x8ED6, 'Store as copy source high byte in &AC', align=Align.INLINE)
d.comment(0x8ED8, 'JSRSIZ at workspace offset &7F', align=Align.INLINE)
d.comment(0x8EDA, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8EDC, 'Y=&80: start of JSR argument data', align=Align.INLINE)
d.comment(0x8EDD, 'Store &80 as copy source low byte', align=Align.INLINE)
d.comment(0x8EDF, 'X = buffer size (loop counter)', align=Align.INLINE)
d.comment(0x8EE0, 'X = size-1 (0-based count for copy)', align=Align.INLINE)
d.comment(0x8EE1, 'Y=0: start of destination param block', align=Align.INLINE)
d.comment(0x8EE3, 'Copy X+1 bytes from workspace to param', align=Align.INLINE)
d.comment(0x8EE6, 'Clear JSR protection status (CLRJSR)', align=Align.INLINE)
d.comment(0x8EE9, 'Y=&7F: JSRSIZ offset (READRB entry)', align=Align.INLINE)
d.comment(0x8EEB, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8EED, 'Y=1: param block offset for size byte', align=Align.INLINE)
d.comment(0x8EEF, 'Store buffer size to (&F0)+1', align=Align.INLINE)
d.comment(0x8EF1, 'Y=2: param block offset for args size', align=Align.INLINE)
d.comment(0x8EF2, 'A=&80: argument data starts at offset &80', align=Align.INLINE)
d.comment(0x8EF4, 'Store args start offset to (&F0)+2', align=Align.INLINE)
d.comment(0x8EF6, 'Return', align=Align.INLINE)

d.label(0x8EF7, 'osword_12_offsets')
d.comment(0x8EFF, 'Sub-function 4 or 5: read/set protection', align=Align.INLINE)
d.comment(0x8F01, 'LSR: 0->0, 1->0, 2->1, 3->1', align=Align.INLINE)
d.comment(0x8F02, 'X=&0D: default to static workspace page', align=Align.INLINE)
d.comment(0x8F04, 'Transfer LSR result to Y for indexing', align=Align.INLINE)
d.comment(0x8F05, 'Y=0 (sub 0-1): use page &0D', align=Align.INLINE)
d.comment(0x8F07, 'Y=1 (sub 2-3): use dynamic workspace', align=Align.INLINE)

d.label(0x8F09, 'set_workspace_page')
d.comment(0x8F09, 'Store workspace page in &AC (hi byte)', align=Align.INLINE)
d.comment(0x8F0B, 'Load offset: &FF (sub 0-1) or &01 (sub 2-3)', align=Align.INLINE)
d.comment(0x8F0E, 'Store offset in &AB (lo byte)', align=Align.INLINE)
d.comment(0x8F10, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0x8F12, 'Y=1: start at param block offset 1', align=Align.INLINE)

d.label(0x8F14, 'copy_param_workspace')
d.comment(0x8F16, 'C=1: copy from param to workspace', align=Align.INLINE)
d.comment(0x8F18, 'Store param byte to workspace', align=Align.INLINE)

d.label(0x8F1A, 'skip_param_write')
d.comment(0x8F1F, 'Decrement remaining count', align=Align.INLINE)
d.comment(0x8F20, 'Loop while bytes remain', align=Align.INLINE)
d.comment(0x8F22, 'Return', align=Align.INLINE)
d.comment(0x8F23, 'LSR A: test bit 0 of sub-function', align=Align.INLINE)
d.comment(0x8F24, 'Y=1: offset for protection byte', align=Align.INLINE)
d.comment(0x8F25, 'Load protection byte from param block', align=Align.INLINE)
d.comment(0x8F27, 'C=1 (odd sub): set protection', align=Align.INLINE)
d.comment(0x8F29, 'C=0 (even sub): read current status', align=Align.INLINE)
d.comment(0x8F2C, 'Return current value to param block', align=Align.INLINE)
d.comment(0x8F2E, 'Update protection status', align=Align.INLINE)
d.comment(0x8F31, 'Also save as JSR mask backup', align=Align.INLINE)
d.comment(0x8F34, 'Return', align=Align.INLINE)

d.label(0x8F35, 'read_local_station_id')
d.comment(0x8F35, 'Y=&14: RX buf offset of cached station ID', align=Align.INLINE)
d.comment(0x8F37, 'Read cached local station number', align=Align.INLINE)
d.comment(0x8F39, 'Y=1: param block byte 1', align=Align.INLINE)
d.comment(0x8F3B, "Return station number to caller's param block", align=Align.INLINE)
d.comment(0x8F3D, 'Return', align=Align.INLINE)
d.comment(0x8F3E, 'Sub-function 8: read local station number', align=Align.INLINE)
d.comment(0x8F40, 'Match: read cached station ID from RX buffer', align=Align.INLINE)
d.comment(0x8F42, 'Sub-function 9: read args size', align=Align.INLINE)
d.comment(0x8F44, 'Match: read ARGS buffer info', align=Align.INLINE)
d.comment(0x8F46, 'Sub >= 10 (bit 7 clear): read error', align=Align.INLINE)
d.comment(0x8F48, 'Y=3: start from handle 3 (descending)', align=Align.INLINE)
d.comment(0x8F4A, 'LSR: test read/write bit', align=Align.INLINE)
d.comment(0x8F4B, 'C=0: read handles from workspace', align=Align.INLINE)
d.comment(0x8F4D, 'Init loop counter at Y=3', align=Align.INLINE)

d.label(0x8F4F, 'copy_handles_to_ws')
d.comment(0x8F4F, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8F51, "Read handle from caller's param block", align=Align.INLINE)
d.comment(0x8F53, 'Convert handle number to bitmask', align=Align.INLINE)
d.comment(0x8F56, 'TYA: get bitmask result', align=Align.INLINE)
d.comment(0x8F57, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8F59, 'Store bitmask to FS server table', align=Align.INLINE)
d.comment(0x8F5C, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8F5E, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8F60, 'Return', align=Align.INLINE)

d.label(0x8F61, 'return_last_error')
d.comment(0x8F61, 'Y=1 (post-INY): param block byte 1', align=Align.INLINE)
d.comment(0x8F62, 'Read last FS error code', align=Align.INLINE)
d.comment(0x8F65, "Return error to caller's param block", align=Align.INLINE)
d.comment(0x8F67, 'Return', align=Align.INLINE)
d.comment(0x8F70, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8F71, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8F73, 'Return', align=Align.INLINE)
d.comment(0x8F74, 'Workspace page high byte', align=Align.INLINE)
d.comment(0x8F76, 'Set up pointer high byte in &AC', align=Align.INLINE)
d.comment(0x8F78, 'Save param block high byte in &AB', align=Align.INLINE)
d.comment(0x8F7A, 'Disable user RX during CB operation', align=Align.INLINE)
d.comment(0x8F7D, 'Read first byte of param block', align=Align.INLINE)
d.comment(0x8F7F, 'Save: 0=open new, non-zero=read RXCB', align=Align.INLINE)
d.comment(0x8F81, 'Non-zero: read specified RXCB', align=Align.INLINE)
d.comment(0x8F83, 'Start scan from RXCB #3 (0-2 reserved)', align=Align.INLINE)
d.comment(0x8F85, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8F88, 'Invalid RXCB: return zero', align=Align.INLINE)
d.comment(0x8F8A, 'LSR twice: byte offset / 4', align=Align.INLINE)
d.comment(0x8F8B, 'Yields RXCB number from offset', align=Align.INLINE)
d.comment(0x8F8C, 'X = RXCB number for iteration', align=Align.INLINE)
d.comment(0x8F8D, 'Read flag byte from RXCB workspace', align=Align.INLINE)
d.comment(0x8F8F, 'Zero = end of CB list', align=Align.INLINE)
d.comment(0x8F91, '&3F = deleted slot, free for reuse', align=Align.INLINE)
d.comment(0x8F93, 'Found free slot', align=Align.INLINE)
d.comment(0x8F95, 'Try next RXCB', align=Align.INLINE)
d.comment(0x8F96, 'A = next RXCB number', align=Align.INLINE)
d.comment(0x8F97, 'Continue scan (always branches)', align=Align.INLINE)
d.comment(0x8F99, 'A = free RXCB number', align=Align.INLINE)
d.comment(0x8F9A, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x8F9C, "Return RXCB number to caller's byte 0", align=Align.INLINE)

d.label(0x8F9E, 'read_rxcb')
d.comment(0x8F9E, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8FA1, 'Invalid: write zero to param block', align=Align.INLINE)
d.comment(0x8FA3, 'Y = offset-1: points to flag byte', align=Align.INLINE)
d.comment(0x8FA4, 'Set &AB = workspace ptr low byte', align=Align.INLINE)
d.comment(0x8FA6, '&C0: test mask for flag byte', align=Align.INLINE)
d.comment(0x8FA8, 'Y=1: flag byte offset in RXCB', align=Align.INLINE)
d.comment(0x8FAC, 'Compare Y(1) with saved byte (open/read)', align=Align.INLINE)
d.comment(0x8FAE, 'ADC flag: test if slot is in use', align=Align.INLINE)
d.comment(0x8FB2, 'Negative: slot has received data', align=Align.INLINE)

d.label(0x8FB4, 'copy_rxcb_to_param')
d.comment(0x8FB4, 'C=0: workspace-to-param direction', align=Align.INLINE)
d.comment(0x8FB5, 'Copy RXCB data to param block', align=Align.INLINE)
d.comment(0x8FB8, 'Done: skip deletion on error', align=Align.INLINE)
d.comment(0x8FBA, 'Mark CB as consumed (consume-once)', align=Align.INLINE)
d.comment(0x8FBC, 'Y=1: flag byte offset', align=Align.INLINE)
d.comment(0x8FBE, 'Write &3F to mark slot deleted', align=Align.INLINE)
d.comment(0x8FC0, 'Branch to exit (always taken)', align=Align.INLINE)
d.comment(0x8FC2, 'Advance through multi-byte field', align=Align.INLINE)
d.comment(0x8FC4, 'Loop until all bytes processed', align=Align.INLINE)
d.comment(0x8FC6, 'Y=-1 → Y=0 after STA below', align=Align.INLINE)
d.comment(0x8FC7, 'Return zero (no free RXCB found)', align=Align.INLINE)

d.label(0x8FC9, 'reenable_rx')
d.comment(0x8FC9, 'Re-enable user RX', align=Align.INLINE)
d.comment(0x8FCC, 'Return', align=Align.INLINE)
d.comment(0x8FCD, 'Y=&1C: workspace offset for RX data start', align=Align.INLINE)
d.comment(0x8FCF, 'A = base address low byte', align=Align.INLINE)
d.comment(0x8FD1, 'A = base + 1 (skip length byte)', align=Align.INLINE)
d.comment(0x8FD6, 'Read data length from (&F0)+1', align=Align.INLINE)
d.comment(0x8FD8, 'A = data length byte', align=Align.INLINE)
d.comment(0x8FDA, 'Workspace offset &20 = RX data end', align=Align.INLINE)
d.comment(0x8FDC, 'A = base + length = end address low', align=Align.INLINE)
d.comment(0x8FDE, 'Store low byte of 16-bit address', align=Align.INLINE)
d.comment(0x8FE0, 'Advance to high byte offset', align=Align.INLINE)
d.comment(0x8FE1, 'A = high byte of base address', align=Align.INLINE)
d.comment(0x8FE3, 'Add carry for 16-bit addition', align=Align.INLINE)
d.comment(0x8FE5, 'Store high byte', align=Align.INLINE)
d.comment(0x8FE7, 'Return', align=Align.INLINE)
d.comment(0x8FEA, 'A >= 1: handle TX result', align=Align.INLINE)
d.comment(0x8FEC, 'Y=&23: start of template (descending)', align=Align.INLINE)
d.comment(0x8FEE, 'Load ROM template byte', align=Align.INLINE)
d.comment(0x8FF1, 'Non-zero = use ROM template byte as-is', align=Align.INLINE)
d.comment(0x8FF3, 'Zero = substitute from NMI workspace', align=Align.INLINE)

d.label(0x8FF6, 'store_txcb_byte')
d.comment(0x8FF6, 'Store to dynamic workspace', align=Align.INLINE)
d.comment(0x8FF8, 'Descend through template', align=Align.INLINE)
d.comment(0x8FF9, 'Stop at offset &17', align=Align.INLINE)
d.comment(0x8FFB, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8FFD, 'Y=&18: TX block starts here', align=Align.INLINE)
d.comment(0x8FFE, 'Point net_tx_ptr at workspace+&18', align=Align.INLINE)
d.comment(0x9000, 'Set up RX buffer start/end pointers', align=Align.INLINE)
d.comment(0x9003, 'Y=2: port byte offset in RXCB', align=Align.INLINE)
d.comment(0x9005, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x9007, 'Store port &90 at (&F0)+2', align=Align.INLINE)

d.label(0x900B, 'copy_fs_addr')
d.comment(0x900B, 'Copy FS station addr from workspace', align=Align.INLINE)
d.comment(0x900E, 'Store to RX param block', align=Align.INLINE)
d.comment(0x9010, 'Next byte', align=Align.INLINE)
d.comment(0x9011, 'Done 3 bytes (Y=4,5,6)?', align=Align.INLINE)
d.comment(0x9013, 'No: continue copying', align=Align.INLINE)
d.comment(0x9015, 'High byte of workspace for TX ptr', align=Align.INLINE)
d.comment(0x9017, 'Store as TX pointer high byte', align=Align.INLINE)
d.comment(0x9019, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x901A, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x901D, 'Y=&20: RX end address offset', align=Align.INLINE)
d.comment(0x901F, 'Set RX end address to &FFFF (accept any length)', align=Align.INLINE)
d.comment(0x9021, 'Store end address low byte (&FF)', align=Align.INLINE)
d.comment(0x9024, 'Store end address high byte (&FF)', align=Align.INLINE)
d.comment(0x9026, 'Y=&19: port byte in workspace RXCB', align=Align.INLINE)
d.comment(0x9028, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x902A, 'Store port to workspace RXCB', align=Align.INLINE)
d.comment(0x902D, 'A=&7F: flag byte = waiting for reply', align=Align.INLINE)
d.comment(0x902F, 'Store flag byte to workspace RXCB', align=Align.INLINE)
d.comment(0x9031, 'Jump to RX poll (BRIANX)', align=Align.INLINE)

d.label(0x9034, 'handle_tx_result')
d.comment(0x9034, 'Save processor flags', align=Align.INLINE)
d.comment(0x9035, 'Y=1: first data byte offset', align=Align.INLINE)
d.comment(0x9037, 'Load first data byte from RX buffer', align=Align.INLINE)
d.comment(0x9039, 'X = first data byte (command code)', align=Align.INLINE)
d.comment(0x903A, 'Advance to next data byte', align=Align.INLINE)
d.comment(0x903B, 'Load station address high byte', align=Align.INLINE)
d.comment(0x903D, 'Advance past station addr', align=Align.INLINE)
d.comment(0x903E, 'Save Y as data index', align=Align.INLINE)
d.comment(0x9040, 'Store station addr hi at (net_rx_ptr)+&72', align=Align.INLINE)
d.comment(0x9042, 'Store to workspace', align=Align.INLINE)
d.comment(0x9045, 'A = command code (from X)', align=Align.INLINE)
d.comment(0x9046, 'Store station addr lo at (net_rx_ptr)+&71', align=Align.INLINE)
d.comment(0x9048, 'Restore flags from earlier PHP', align=Align.INLINE)
d.comment(0x9049, 'First call: adjust data length', align=Align.INLINE)

d.label(0x904B, 'send_data_bytes')
d.comment(0x904B, 'Reload data index', align=Align.INLINE)
d.comment(0x904D, 'Advance data index for next iteration', align=Align.INLINE)
d.comment(0x904F, 'Load next data byte', align=Align.INLINE)
d.comment(0x9051, 'Zero byte: end of data, return', align=Align.INLINE)
d.comment(0x9053, 'Y=&7D: store byte for TX at offset &7D', align=Align.INLINE)
d.comment(0x9055, 'Store data byte at (net_rx_ptr)+&7D for TX', align=Align.INLINE)
d.comment(0x9057, 'Save data byte for &0D check after TX', align=Align.INLINE)
d.comment(0x9058, 'Set up TX control block', align=Align.INLINE)
d.comment(0x905B, 'Enable IRQs and transmit', align=Align.INLINE)

d.label(0x905E, 'delay_between_tx')
d.comment(0x905E, 'Short delay loop between TX packets', align=Align.INLINE)
d.comment(0x905F, 'Spin until X reaches 0', align=Align.INLINE)
d.comment(0x9061, 'Restore data byte for terminator check', align=Align.INLINE)
d.comment(0x9064, 'Not &0D: continue with next byte', align=Align.INLINE)
d.comment(0x9066, 'Return (data complete)', align=Align.INLINE)
d.comment(0x9067, 'First-packet: set up control block', align=Align.INLINE)
d.comment(0x906A, 'Y=&7B: data length offset', align=Align.INLINE)
d.comment(0x906C, 'Load current data length', align=Align.INLINE)
d.comment(0x906E, 'Adjust data length by 3 for header bytes', align=Align.INLINE)
d.comment(0x9070, 'Store adjusted length', align=Align.INLINE)
d.comment(0x9072, 'Enable interrupts', align=Align.INLINE)
d.comment(0x9073, 'Transmit via tx_poll_ff', align=Align.INLINE)
d.comment(0x9076, 'Save processor status', align=Align.INLINE)
d.comment(0x9077, 'Save A (reason code)', align=Align.INLINE)
d.comment(0x9078, 'Save X', align=Align.INLINE)
d.comment(0x9079, 'Push X to stack', align=Align.INLINE)
d.comment(0x907A, 'Save Y', align=Align.INLINE)
d.comment(0x907B, 'Push Y to stack', align=Align.INLINE)
d.comment(0x907C, 'Get stack pointer for indexed access', align=Align.INLINE)
d.comment(0x907D, 'Retrieve original A (reason code) from stack', align=Align.INLINE)
d.comment(0x9080, 'Reason codes 0-8 only', align=Align.INLINE)
d.comment(0x9082, 'Code >= 9: skip dispatch, restore regs', align=Align.INLINE)
d.comment(0x9084, 'X = reason code for table lookup', align=Align.INLINE)
d.comment(0x9085, 'Dispatch to handler via trampoline', align=Align.INLINE)
d.comment(0x9088, 'Restore Y', align=Align.INLINE)
d.comment(0x9089, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x908A, 'Restore X', align=Align.INLINE)
d.comment(0x908B, 'Transfer to X register', align=Align.INLINE)
d.comment(0x908C, 'Restore A', align=Align.INLINE)
d.comment(0x908D, 'Restore processor status flags', align=Align.INLINE)
d.comment(0x908E, 'Return with all registers preserved', align=Align.INLINE)
d.comment(0x9092, 'Push high byte of handler address', align=Align.INLINE)
d.comment(0x9093, 'Load handler low byte from table', align=Align.INLINE)
d.comment(0x9096, 'Push low byte of handler address', align=Align.INLINE)
d.comment(0x9097, 'Load workspace byte &EF for handler', align=Align.INLINE)
d.comment(0x9099, 'RTS dispatches to pushed handler', align=Align.INLINE)

d.label(0x90AC, 'net_write_char_handler')
d.comment(0x90AC, 'Get stack pointer for P register access', align=Align.INLINE)
d.comment(0x90AD, 'ROR/ASL on stacked P: zeros carry to signal success', align=Align.INLINE)
d.comment(0x90B0, 'ASL: restore P after ROR zeroed carry', align=Align.INLINE)
d.comment(0x90B3, 'Y = character to write', align=Align.INLINE)
d.comment(0x90B4, 'Store character at workspace offset &DA', align=Align.INLINE)
d.comment(0x90B6, 'Store char at workspace offset &DA', align=Align.INLINE)
d.comment(0x90B8, 'A=0: command type for net write char', align=Align.INLINE)
d.comment(0x90BA, 'Y=&D9: command type offset', align=Align.INLINE)
d.comment(0x90BC, 'Store command type at ws+&D9', align=Align.INLINE)
d.comment(0x90BE, 'Mark TX control block as active (&80)', align=Align.INLINE)
d.comment(0x90C0, 'Y=&0C: TXCB start offset', align=Align.INLINE)
d.comment(0x90C2, 'Set TX active flag at ws+&0C', align=Align.INLINE)
d.comment(0x90C4, 'Save net_tx_ptr; redirect to workspace TXCB', align=Align.INLINE)
d.comment(0x90C6, 'Save net_tx_ptr low', align=Align.INLINE)
d.comment(0x90C7, 'Load net_tx_ptr high', align=Align.INLINE)
d.comment(0x90C9, 'Save net_tx_ptr high', align=Align.INLINE)
d.comment(0x90CA, 'Redirect net_tx_ptr low to workspace', align=Align.INLINE)
d.comment(0x90CC, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0x90CE, 'Complete ptr redirect', align=Align.INLINE)
d.comment(0x90D0, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x90D3, 'Mark TXCB as deleted (&3F) after transmit', align=Align.INLINE)
d.comment(0x90D5, 'Write &3F to TXCB byte 0', align=Align.INLINE)
d.comment(0x90D7, 'Restore net_tx_ptr high', align=Align.INLINE)
d.comment(0x90D8, 'Write back', align=Align.INLINE)
d.comment(0x90DA, 'Restore net_tx_ptr low', align=Align.INLINE)
d.comment(0x90DB, 'Write back', align=Align.INLINE)
d.comment(0x90DD, 'Return', align=Align.INLINE)
d.comment(0x90DE, 'Load original Y (OSBYTE secondary param)', align=Align.INLINE)
d.comment(0x90E0, 'OSBYTE &81 (INKEY): always forward to terminal', align=Align.INLINE)
d.comment(0x90E2, 'Forward &81 to terminal for keyboard read', align=Align.INLINE)
d.comment(0x90E4, 'Y=1: search NCTBPL table (execute on both)', align=Align.INLINE)
d.comment(0x90E6, 'X=7: 8-entry NCTBPL table size', align=Align.INLINE)
d.comment(0x90E8, 'Search for OSBYTE code in NCTBPL table', align=Align.INLINE)
d.comment(0x90EB, 'Match found: dispatch with Y=1 (both)', align=Align.INLINE)
d.comment(0x90ED, 'Y=-1: search NCTBMI table (terminal only)', align=Align.INLINE)
d.comment(0x90EE, 'Second DEY: Y=&FF (from 1 via 0)', align=Align.INLINE)
d.comment(0x90EF, 'X=&0E: 15-entry NCTBMI table size', align=Align.INLINE)
d.comment(0x90F1, 'Search for OSBYTE code in NCTBMI table', align=Align.INLINE)
d.comment(0x90F4, 'Match found: dispatch with Y=&FF (terminal)', align=Align.INLINE)
d.comment(0x90F6, 'Y=0: OSBYTE not recognised, ignore', align=Align.INLINE)

d.label(0x90F7, 'dispatch_remote_osbyte')
d.comment(0x90F7, 'X=2 bytes to copy (default for RBYTE)', align=Align.INLINE)
d.comment(0x90F9, 'A=Y: check table match result', align=Align.INLINE)
d.comment(0x90FA, 'Y=0: not recognised, return unhandled', align=Align.INLINE)
d.comment(0x90FC, 'Y>0 (NCTBPL): send only, no result expected', align=Align.INLINE)
d.comment(0x90FD, 'Y>0 (NCTBPL): no result expected, skip RX', align=Align.INLINE)
d.comment(0x90FF, 'Y<0 (NCTBMI): X=3 bytes (result + P flags)', align=Align.INLINE)
d.comment(0x9100, 'Y=&DC: top of 3-byte stack frame region', align=Align.INLINE)
d.comment(0x9102, 'Copy OSBYTE args from stack frame to workspace', align=Align.INLINE)
d.comment(0x9105, 'Store to NFS workspace for transmission', align=Align.INLINE)
d.comment(0x9107, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9108, 'Copied all 3 bytes? (&DC, &DB, &DA)', align=Align.INLINE)
d.comment(0x910A, 'Loop for remaining bytes', align=Align.INLINE)
d.comment(0x910C, 'A = byte count for setup_tx_and_send', align=Align.INLINE)
d.comment(0x910D, 'Build TXCB and transmit to terminal', align=Align.INLINE)
d.comment(0x9110, 'Restore N flag from table match type', align=Align.INLINE)
d.comment(0x9111, 'Y was positive (NCTBPL): done, no result', align=Align.INLINE)
d.comment(0x9113, 'Set up RX control block to wait for reply', align=Align.INLINE)
d.comment(0x9119, 'Bit7 clear: still waiting, poll again', align=Align.INLINE)
d.comment(0x911B, 'X = stack pointer for register restoration', align=Align.INLINE)
d.comment(0x911C, 'Y=&DD: saved P byte offset in workspace', align=Align.INLINE)
d.comment(0x911E, 'Load remote processor status from reply', align=Align.INLINE)
d.comment(0x9120, 'Force V=1 (claimed) and I=1 (no IRQ) in saved P', align=Align.INLINE)
d.comment(0x9122, 'ALWAYS branch (ORA #&44 never zero)', align=Align.INLINE)
d.comment(0x9124, 'Previous workspace offset', align=Align.INLINE)
d.comment(0x9125, 'Previous stack register slot', align=Align.INLINE)
d.comment(0x9126, 'Load next result byte (X, then Y)', align=Align.INLINE)
d.comment(0x9128, 'Write result bytes to stacked registers', align=Align.INLINE)
d.comment(0x912B, 'Copied all result bytes? (P at &DA)', align=Align.INLINE)
d.comment(0x912D, 'Loop for remaining result bytes', align=Align.INLINE)
d.comment(0x912F, 'Return to OSBYTE dispatcher', align=Align.INLINE)
d.comment(0x9130, 'Compare OSBYTE code with table entry', align=Align.INLINE)
d.comment(0x9133, 'Match found: return with Z=1', align=Align.INLINE)
d.comment(0x9135, 'Next table entry (descending)', align=Align.INLINE)
d.comment(0x9136, 'Loop for remaining entries', align=Align.INLINE)
d.comment(0x9138, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)

d.label(0x9139, 'remote_osbyte_table')
d.comment(0x914C, 'OSWORD 7 (sound): handle via common path', align=Align.INLINE)
d.comment(0x914E, 'OSWORD 8 = define an envelope', align=Align.INLINE)
d.comment(0x9150, 'Not OSWORD 7 or 8: ignore (BNE exits)', align=Align.INLINE)

d.label(0x9152, 'copy_params_rword')
d.comment(0x9152, 'Point workspace to offset &DB for params', align=Align.INLINE)
d.comment(0x9154, 'Store workspace ptr offset &DB', align=Align.INLINE)

d.label(0x9156, 'copy_osword_params')
d.comment(0x9156, 'Load param byte from OSWORD param block', align=Align.INLINE)
d.comment(0x9158, 'Write param byte to workspace', align=Align.INLINE)
d.comment(0x915A, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x915B, 'Loop for all parameter bytes', align=Align.INLINE)
d.comment(0x915D, 'Y=0 after loop', align=Align.INLINE)
d.comment(0x915E, 'Point workspace to offset &DA', align=Align.INLINE)
d.comment(0x9160, 'Load original OSWORD code', align=Align.INLINE)
d.comment(0x9162, 'Store OSWORD code at ws+0', align=Align.INLINE)
d.comment(0x9164, 'Reset workspace ptr to base', align=Align.INLINE)
d.comment(0x9166, 'Y=&14: command type offset', align=Align.INLINE)
d.comment(0x9168, 'Tag as RWORD (port &E9)', align=Align.INLINE)
d.comment(0x916A, 'Store port tag at ws+&14', align=Align.INLINE)
d.comment(0x916C, 'A=1: single-byte TX', align=Align.INLINE)
d.comment(0x9171, 'Restore workspace ptr', align=Align.INLINE)
d.comment(0x9173, 'X=&0D: template offset for alt entry', align=Align.INLINE)
d.comment(0x9175, 'Y=&7C: target workspace offset for alt entry', align=Align.INLINE)
d.comment(0x9177, 'BIT test: V flag = bit 6 of &83AF', align=Align.INLINE)
d.comment(0x917A, 'V=1: store to (net_rx_ptr) instead', align=Align.INLINE)
d.comment(0x917C, 'Y=&17: workspace target offset (main entry)', align=Align.INLINE)
d.comment(0x917E, 'X=&1A: template table index (main entry)', align=Align.INLINE)
d.comment(0x9180, 'V=0: target is (nfs_workspace)', align=Align.INLINE)
d.comment(0x9181, 'Load template byte from ctrl_block_template[X]', align=Align.INLINE)
d.comment(0x9184, '&FE = stop sentinel', align=Align.INLINE)
d.comment(0x9186, 'End of template: jump to exit', align=Align.INLINE)
d.comment(0x9188, '&FD = skip sentinel', align=Align.INLINE)
d.comment(0x918A, "Skip: don't store, just decrement Y", align=Align.INLINE)
d.comment(0x918C, '&FC = page byte sentinel', align=Align.INLINE)
d.comment(0x918E, 'Not sentinel: store template value directly', align=Align.INLINE)
d.comment(0x9196, 'PAGE byte → Y=&02 / Y=&74', align=Align.INLINE)
d.comment(0x9198, '→ Y=&04 / Y=&76', align=Align.INLINE)
d.comment(0x919A, 'PAGE byte → Y=&06 / Y=&78', align=Align.INLINE)
d.comment(0x919C, '→ Y=&08 / Y=&7A', align=Align.INLINE)

d.label(0x91A0, 'cb_template_main_start')

d.label(0x91A4, 'cb_template_tail')
d.comment(0x91CF, 'X-1: convert 1-based buffer to 0-based', align=Align.INLINE)
d.comment(0x91D0, 'Is this the network printer buffer?', align=Align.INLINE)
d.comment(0x91D2, 'No: skip printer init', align=Align.INLINE)
d.comment(0x91D4, '&1F = initial buffer pointer offset', align=Align.INLINE)
d.comment(0x91D6, 'Reset printer buffer write position', align=Align.INLINE)
d.comment(0x91D9, '&41 = initial PFLAGS (bit 6 set, bit 0 set)', align=Align.INLINE)
d.comment(0x91DE, 'Return', align=Align.INLINE)
d.comment(0x91DF, 'Only handle buffer 4 (network printer)', align=Align.INLINE)
d.comment(0x91E1, 'Not buffer 4: ignore', align=Align.INLINE)
d.comment(0x91E3, 'A = reason code', align=Align.INLINE)
d.comment(0x91E4, 'Reason 1? (DEX: 1->0)', align=Align.INLINE)
d.comment(0x91E5, 'Not reason 1: handle Ctrl-B/C', align=Align.INLINE)
d.comment(0x91E7, 'Get stack pointer for P register', align=Align.INLINE)
d.comment(0x91E8, 'Force I flag in stacked P to block IRQs', align=Align.INLINE)
d.comment(0x91EB, 'Write back modified P register', align=Align.INLINE)
d.comment(0x91EE, 'OSBYTE &91: extract char from MOS buffer', align=Align.INLINE)
d.comment(0x91F0, 'X=3: printer buffer number', align=Align.INLINE)
d.comment(0x91F5, 'Buffer empty: return', align=Align.INLINE)
d.comment(0x91F7, 'Y = extracted character', align=Align.INLINE)
d.comment(0x91F8, 'Store char in output buffer', align=Align.INLINE)
d.comment(0x91FB, 'Buffer nearly full? (&6E = threshold)', align=Align.INLINE)
d.comment(0x91FD, 'Not full: get next char', align=Align.INLINE)
d.comment(0x91FF, 'Buffer full: flush to network', align=Align.INLINE)
d.comment(0x9202, 'Continue after flush', align=Align.INLINE)
d.comment(0x9204, 'Load current buffer offset', align=Align.INLINE)
d.comment(0x9207, 'Store byte at current position', align=Align.INLINE)
d.comment(0x9209, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x920C, 'Return; Y = buffer offset', align=Align.INLINE)

d.label(0x920D, 'toggle_print_flag')
d.comment(0x920D, 'Save reason code', align=Align.INLINE)
d.comment(0x920E, 'A = reason code', align=Align.INLINE)
d.comment(0x920F, 'EOR #1: toggle print-active flag (bit 0)', align=Align.INLINE)
d.comment(0x9211, 'Store toggled flag as output byte', align=Align.INLINE)
d.comment(0x9224, 'Extract upper nibble of PFLAGS', align=Align.INLINE)
d.comment(0x9226, 'Shift for bit extraction', align=Align.INLINE)
d.comment(0x9227, 'Save in X', align=Align.INLINE)
d.comment(0x9228, 'Restore original reason code', align=Align.INLINE)
d.comment(0x9229, 'Merge print-active bit from original A', align=Align.INLINE)
d.comment(0x922A, 'Retrieve shifted PFLAGS', align=Align.INLINE)
d.comment(0x922B, 'Recombine into new PFLAGS value', align=Align.INLINE)
d.comment(0x922F, 'Return', align=Align.INLINE)
d.comment(0x9230, 'Store buffer length at workspace offset &08', align=Align.INLINE)
d.comment(0x9232, 'Current buffer fill position', align=Align.INLINE)
d.comment(0x9235, 'Write to workspace offset &08', align=Align.INLINE)
d.comment(0x9237, 'Store page high byte at offset &09', align=Align.INLINE)
d.comment(0x9239, 'Y=&09', align=Align.INLINE)
d.comment(0x923A, 'Write page high byte at offset &09', align=Align.INLINE)
d.comment(0x923C, 'Also store at offset &05', align=Align.INLINE)
d.comment(0x923E, '(end address high byte)', align=Align.INLINE)
d.comment(0x9240, 'Y=&0B: flag byte offset', align=Align.INLINE)
d.comment(0x9242, 'X=&26: start from template entry &26', align=Align.INLINE)
d.comment(0x9244, 'Reuse ctrl_block_setup with CLV entry', align=Align.INLINE)
d.comment(0x9247, 'Y=&0A: sequence flag byte offset', align=Align.INLINE)
d.comment(0x9253, 'Old sequence bit into bit 0', align=Align.INLINE)
d.comment(0x9254, 'Store sequence flag at offset &0A', align=Align.INLINE)
d.comment(0x9256, 'Y=&1F: buffer start offset', align=Align.INLINE)
d.comment(0x9258, 'Reset printer buffer to start (&1F)', align=Align.INLINE)
d.comment(0x925B, 'A=0: printer output flag', align=Align.INLINE)
d.comment(0x925D, 'X=0: workspace low byte', align=Align.INLINE)
d.comment(0x925E, 'Y = workspace page high byte', align=Align.INLINE)
d.comment(0x9260, 'Enable interrupts before TX', align=Align.INLINE)
d.comment(0x9261, 'Set TX control block ptr low byte', align=Align.INLINE)
d.comment(0x9263, 'Set TX control block ptr high byte', align=Align.INLINE)
d.comment(0x9265, 'Save A (handle bitmask) for later', align=Align.INLINE)
d.comment(0x9266, 'Compute sequence bit from handle', align=Align.INLINE)
d.comment(0x9269, 'Zero: no sequence bit set', align=Align.INLINE)
d.comment(0x926B, 'Non-zero: normalise to bit 0', align=Align.INLINE)
d.comment(0x926D, 'Y=0: flag byte offset in TXCB', align=Align.INLINE)
d.comment(0x926F, 'Merge sequence into existing flag byte', align=Align.INLINE)
d.comment(0x9271, 'Save merged flag byte', align=Align.INLINE)
d.comment(0x9272, 'Write flag+sequence to TXCB byte 0', align=Align.INLINE)
d.comment(0x9274, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x9277, 'End address &FFFF = unlimited data length', align=Align.INLINE)
d.comment(0x9279, 'Y=8: end address low offset in TXCB', align=Align.INLINE)
d.comment(0x927B, 'Store &FF to end addr low', align=Align.INLINE)
d.comment(0x927E, 'Store &FF to end addr high (Y=9)', align=Align.INLINE)
d.comment(0x9280, 'Recover merged flag byte', align=Align.INLINE)
d.comment(0x9281, 'Save in X for sequence compare', align=Align.INLINE)
d.comment(0x9282, 'Y=&D1: printer port number', align=Align.INLINE)
d.comment(0x9284, 'Recover saved handle bitmask', align=Align.INLINE)
d.comment(0x9285, 'Re-save for later consumption', align=Align.INLINE)
d.comment(0x9286, 'A=0: port &D1 (print); A!=0: port &90 (FS)', align=Align.INLINE)
d.comment(0x9288, 'Y=&90: FS data port', align=Align.INLINE)
d.comment(0x928A, 'A = selected port number', align=Align.INLINE)
d.comment(0x928B, 'Y=1: port byte offset in TXCB', align=Align.INLINE)
d.comment(0x928D, 'Write port to TXCB byte 1', align=Align.INLINE)
d.comment(0x928F, 'A = saved flag byte (expected sequence)', align=Align.INLINE)
d.comment(0x9291, 'Push expected sequence for retry loop', align=Align.INLINE)
d.comment(0x9292, 'Flag byte &7F = waiting for reply', align=Align.INLINE)
d.comment(0x9294, 'Write to TXCB flag byte (Y=0)', align=Align.INLINE)
d.comment(0x9296, 'Transmit and wait for reply (BRIANX)', align=Align.INLINE)
d.comment(0x9299, 'Recover expected sequence', align=Align.INLINE)
d.comment(0x929A, 'Keep on stack for next iteration', align=Align.INLINE)
d.comment(0x929B, 'Check if TX result matches expected sequence', align=Align.INLINE)
d.comment(0x929D, 'Bit 0 to carry (sequence mismatch?)', align=Align.INLINE)
d.comment(0x929E, 'C=1: mismatch, retry transmit', align=Align.INLINE)
d.comment(0x92A0, 'Clean up: discard expected sequence', align=Align.INLINE)
d.comment(0x92A1, 'Discard saved handle bitmask', align=Align.INLINE)
d.comment(0x92A2, 'Toggle sequence bit on success', align=Align.INLINE)
d.comment(0x92A5, 'Return', align=Align.INLINE)
d.comment(0x92A6, 'Save current table index', align=Align.INLINE)
d.comment(0x92A8, 'Push for later restore', align=Align.INLINE)
d.comment(0x92A9, 'Point workspace to palette save area (&E9)', align=Align.INLINE)
d.comment(0x92AB, 'Set workspace low byte', align=Align.INLINE)
d.comment(0x92AD, 'Y=0: first palette entry', align=Align.INLINE)
d.comment(0x92AF, 'Clear table index counter', align=Align.INLINE)
d.comment(0x92B1, 'Save current screen MODE to workspace', align=Align.INLINE)
d.comment(0x92B4, 'Store MODE at workspace[0]', align=Align.INLINE)
d.comment(0x92B6, 'Advance workspace pointer past MODE byte', align=Align.INLINE)
d.comment(0x92B8, 'Read colour count (from &0351)', align=Align.INLINE)
d.comment(0x92BB, 'Push for iteration count tracking', align=Align.INLINE)
d.comment(0x92BC, 'A=0: logical colour number for OSWORD', align=Align.INLINE)

d.label(0x92BD, 'save_palette_entry')
d.comment(0x92BD, 'Store logical colour at workspace[0]', align=Align.INLINE)
d.comment(0x92BF, 'X = workspace ptr low (param block addr)', align=Align.INLINE)
d.comment(0x92C1, 'Y = workspace ptr high', align=Align.INLINE)
d.comment(0x92C3, 'OSWORD &0B: read palette for logical colour', align=Align.INLINE)
d.comment(0x92C8, 'Recover colour count', align=Align.INLINE)
d.comment(0x92C9, 'Y=0: access workspace[0]', align=Align.INLINE)
d.comment(0x92CB, 'Write colour count back to workspace[0]', align=Align.INLINE)
d.comment(0x92CD, 'Y=1: access workspace[1] (palette result)', align=Align.INLINE)
d.comment(0x92CE, 'Read palette value returned by OSWORD', align=Align.INLINE)
d.comment(0x92D0, 'Push palette value for next iteration', align=Align.INLINE)
d.comment(0x92D1, 'X = current workspace ptr low', align=Align.INLINE)
d.comment(0x92D3, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92D5, 'Increment table index', align=Align.INLINE)
d.comment(0x92D7, 'Y=0 for next store', align=Align.INLINE)
d.comment(0x92D8, 'Load table index as logical colour', align=Align.INLINE)
d.comment(0x92DA, 'Loop until workspace wraps past &F9', align=Align.INLINE)
d.comment(0x92DC, 'Continue for all 16 palette entries', align=Align.INLINE)
d.comment(0x92DE, 'Discard last palette value from stack', align=Align.INLINE)
d.comment(0x92DF, 'Reset table index to 0', align=Align.INLINE)
d.comment(0x92E1, 'Advance workspace past palette data', align=Align.INLINE)
d.comment(0x92E3, 'Save cursor pos and OSBYTE state values', align=Align.INLINE)
d.comment(0x92E6, 'Advance workspace past VDU state data', align=Align.INLINE)
d.comment(0x92E8, 'Recover saved table index', align=Align.INLINE)
d.comment(0x92E9, 'Restore table index', align=Align.INLINE)
d.comment(0x92EB, 'Restore LSTAT from saved OLDJSR value', align=Align.INLINE)
d.comment(0x92EE, 'Write to protection status', align=Align.INLINE)
d.comment(0x92F1, 'Return', align=Align.INLINE)
d.comment(0x92F2, 'Read cursor editing state', align=Align.INLINE)
d.comment(0x92F5, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0x92F7, 'Preserve in X for OSBYTE', align=Align.INLINE)
d.comment(0x92F8, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.comment(0x92FB, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92FD, 'Y result from OSBYTE &85', align=Align.INLINE)
d.comment(0x92FE, 'Store Y pos to workspace (X=0)', align=Align.INLINE)
d.comment(0x9300, 'Self-call trick: executes twice', align=Align.INLINE)
d.comment(0x9303, 'X=0 for (zp,X) addressing', align=Align.INLINE)
d.comment(0x9305, 'Index into OSBYTE number table', align=Align.INLINE)
d.comment(0x9307, 'Next table entry next time', align=Align.INLINE)
d.comment(0x9309, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x930B, 'Read OSBYTE number from table', align=Align.INLINE)
d.comment(0x930E, 'Y=&FF: read current value', align=Align.INLINE)
d.comment(0x9310, 'Call OSBYTE', align=Align.INLINE)
d.comment(0x9313, 'Result in X to A', align=Align.INLINE)
d.comment(0x9314, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x9316, 'Store result to workspace', align=Align.INLINE)

d.label(0x9319, 'vdu_osbyte_table')

d.label(0x931C, 'reloc_zp_src')

d.label(0x935D, 'reloc_p4_src')

d.label(0x9456, 'reloc_p5_src')
d.comment(0x966F, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x9672, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x9675, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x9677, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x9679, 'Clear Econet init flag before setup', align=Align.INLINE)
d.comment(0x967C, 'Y=&FF for OSBYTE', align=Align.INLINE)
d.comment(0x9684, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x9686, 'X=&0C: NMI claim service', align=Align.INLINE)
d.comment(0x9688, 'Y=&FF: pass to adlc_init_workspace', align=Align.INLINE)
d.comment(0x968D, 'Copy 32 bytes of NMI shim from ROM to &0D00', align=Align.INLINE)

d.label(0x968F, 'copy_nmi_shim')
d.comment(0x968F, 'Read byte from NMI shim ROM source', align=Align.INLINE)
d.comment(0x9692, 'Write to NMI shim RAM at &0D00', align=Align.INLINE)
d.comment(0x9695, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9696, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x9698, 'Patch current ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x969A, 'Self-modifying code: ROM bank at &0D07', align=Align.INLINE)
d.comment(0x969D, '&80 = Econet initialised', align=Align.INLINE)
d.comment(0x969F, 'Mark TX as complete (ready)', align=Align.INLINE)
d.comment(0x96A2, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x96A5, 'Read station ID (&FE18 = INTOFF side effect)', align=Align.INLINE)
d.comment(0x96A8, 'Store our station ID in TX scout', align=Align.INLINE)
d.comment(0x96AB, 'Y=0 after copy loop: net = local', align=Align.INLINE)
d.comment(0x96F1, 'Return', align=Align.INLINE)

d.label(0x970A, 'accept_frame')
d.comment(0x970A, 'Install next NMI handler at &9711 (RX scout net byte)', align=Align.INLINE)

d.label(0x9727, 'accept_local_net')

d.label(0x972A, 'accept_scout_net')
d.comment(0x972C, 'Install scout data reading loop at &970E', align=Align.INLINE)
d.comment(0x9738, 'Neither set -- clean end, discard via &9740', align=Align.INLINE)
d.comment(0x9748, 'No RDA -- error handler &9733', align=Align.INLINE)
d.comment(0x976F, 'Write CR1', align=Align.INLINE)
d.comment(0x9774, 'Write CR2', align=Align.INLINE)
d.comment(0x9788, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x9793, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x9796, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x9799, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x979B, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x979D, 'Write CR2: broadcast frame prep', align=Align.INLINE)

d.label(0x97A0, 'scan_port_list')
d.comment(0x97A0, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x97A3, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x97A5, 'Start scanning port list at page &C0', align=Align.INLINE)

d.label(0x97AD, 'check_port_slot')
d.comment(0x97AD, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x97AF, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x97B1, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x97B3, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x97B5, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x97B8, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x97BA, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x97BC, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x97BF, 'Port mismatch -- try next slot', align=Align.INLINE)

d.label(0x97C1, 'check_station_filter')
d.comment(0x97C1, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x97C2, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x97C4, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x97C6, 'Check if source station matches', align=Align.INLINE)
d.comment(0x97C9, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x97CB, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x97CC, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x97CE, 'Check if source network matches', align=Align.INLINE)
d.comment(0x97D1, 'Network matches or zero = accept', align=Align.INLINE)

d.label(0x97D3, 'next_port_slot')
d.comment(0x97D3, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x9801, 'Broadcast: different completion path', align=Align.INLINE)

d.label(0x9804, 'send_data_rx_ack')
d.comment(0x9804, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x9806, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x9809, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x980B, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x980E, 'Install data_rx_setup at &97DC', align=Align.INLINE)
d.comment(0x9810, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x9812, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x9817, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x981A, 'Install nmi_data_rx at &9821', align=Align.INLINE)
d.comment(0x981E, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)
d.comment(0x9821, 'A=&01: mask for AP (Address Present)', align=Align.INLINE)
d.comment(0x9823, 'BIT SR2: test AP bit', align=Align.INLINE)
d.comment(0x9826, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x9828, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x982B, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x982E, 'Not for us: error path', align=Align.INLINE)
d.comment(0x9830, 'Install net check handler at &9837', align=Align.INLINE)
d.comment(0x9834, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x983A, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x983C, 'Read dest network byte', align=Align.INLINE)
d.comment(0x983F, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x9841, 'Install skip handler at &9810', align=Align.INLINE)
d.comment(0x9843, 'High byte of &9810 handler', align=Align.INLINE)
d.comment(0x9845, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x9848, 'Data ready: skip directly, no RTI', align=Align.INLINE)
d.comment(0x984A, 'Install handler and return via RTI', align=Align.INLINE)
d.comment(0x9850, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x9858, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x985A, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x985D, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x985F, 'Install bulk read at &9843', align=Align.INLINE)
d.comment(0x9861, 'High byte of &9843 handler', align=Align.INLINE)
d.comment(0x9863, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x9866, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x9868, 'No: install handler and RTI', align=Align.INLINE)

d.label(0x986B, 'install_tube_rx')
d.comment(0x986B, 'Tube: install Tube RX at &98DD', align=Align.INLINE)
d.comment(0x986D, 'High byte of &98DD handler', align=Align.INLINE)
d.comment(0x986F, 'Install Tube handler and RTI', align=Align.INLINE)
d.comment(0x9872, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x9875, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x9877, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x987A, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x987D, 'Discard and return to idle listen', align=Align.INLINE)

d.label(0x9885, 'data_rx_loop')
d.comment(0x9885, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x9887, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x988A, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x988C, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x988D, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x988F, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x9891, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x9893, 'No pages left: handle as complete', align=Align.INLINE)

d.label(0x9895, 'read_sr2_between_pairs')
d.comment(0x9895, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x9898, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x989A, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)

d.label(0x989C, 'read_second_rx_byte')
d.comment(0x989C, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x989F, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x98A1, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x98A2, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x98A4, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x98A6, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x98A8, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x98AA, 'No pages left: frame complete', align=Align.INLINE)

d.label(0x98AC, 'check_sr2_loop_again')
d.comment(0x98AC, 'Read SR2 for next iteration', align=Align.INLINE)
d.comment(0x98AF, 'SR2 non-zero: more data, loop back', align=Align.INLINE)
d.comment(0x98B1, 'SR2=0: no more data yet, wait for NMI', align=Align.INLINE)
d.comment(0x98B6, 'Write CR1', align=Align.INLINE)
d.comment(0x98BB, 'Write CR2', align=Align.INLINE)
d.comment(0x98BE, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x98C9, 'Check if buffer space remains', align=Align.INLINE)

d.label(0x98CB, 'read_last_rx_byte')
d.comment(0x98CB, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x98D0, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x98D2, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x98D4, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x98D6, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x98D8, 'Page boundary: advance buffer page', align=Align.INLINE)

d.label(0x98DA, 'send_ack')
d.comment(0x98DA, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x98DD, 'Read SR2 for Tube data receive path', align=Align.INLINE)

d.label(0x98E0, 'rx_tube_data')
d.comment(0x98E0, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x98E2, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x9916, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x9919, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x991B, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x991E, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x9920, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x9923, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x9925, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x9928, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x992A, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x992C, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x992E, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x9930, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x9932, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x9934, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x9936, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x9939, 'Save extra byte at &0D5D for later use', align=Align.INLINE)
d.comment(0x993C, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x993E, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x9941, 'Store updated flags', align=Align.INLINE)
d.comment(0x9944, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x9947, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x9949, 'Final ACK: call completion handler', align=Align.INLINE)
d.comment(0x994C, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x9951, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x9956, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x995B, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x995D, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x9960, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x9971, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x9974, 'Install nmi_ack_tx_src at &9925', align=Align.INLINE)
d.comment(0x9976, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x9978, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)
d.comment(0x9992, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x9998, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x999B, 'Install next NMI handler', align=Align.INLINE)

d.label(0x999E, 'start_data_tx')
d.comment(0x999E, 'Jump to start data TX phase', align=Align.INLINE)

d.label(0x99A1, 'dispatch_nmi_error')
d.comment(0x99A1, 'Jump to error handler', align=Align.INLINE)
d.comment(0x99A4, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x99A6, 'BIT tx_flags: check data transfer bit', align=Align.INLINE)
d.comment(0x99A9, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x99AB, 'CLC: init carry for 4-byte add', align=Align.INLINE)
d.comment(0x99AC, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x99AD, 'Y=8: RXCB high pointer offset', align=Align.INLINE)

d.label(0x99AF, 'add_rxcb_ptr')
d.comment(0x99AF, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x99B1, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x99B2, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x99B5, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x99B7, 'Next byte', align=Align.INLINE)
d.comment(0x99B8, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x99B9, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x99BB, 'No: continue adding', align=Align.INLINE)
d.comment(0x99BD, 'Discard final carry', align=Align.INLINE)
d.comment(0x99BE, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x99C0, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x99C3, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x99C5, 'Save X on stack', align=Align.INLINE)
d.comment(0x99C6, 'Push X', align=Align.INLINE)
d.comment(0x99C7, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x99C9, 'CLC for address calculation', align=Align.INLINE)
d.comment(0x99CA, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x99CC, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x99CD, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x99CF, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x99D1, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x99D4, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x99D7, 'Send to Tube via R3', align=Align.INLINE)

d.label(0x99E5, 'skip_tube_update')
d.comment(0x99E5, 'A=&FF: return value (transfer done)', align=Align.INLINE)
d.comment(0x99E7, 'Return', align=Align.INLINE)
d.comment(0x99E8, 'Load received port byte', align=Align.INLINE)
d.comment(0x99EB, 'Port != 0: data transfer frame', align=Align.INLINE)
d.comment(0x99ED, 'Port=0: load control byte', align=Align.INLINE)
d.comment(0x99F0, 'Ctrl = &82 (POKE)?', align=Align.INLINE)
d.comment(0x99F2, 'Yes: POKE also needs data transfer', align=Align.INLINE)
d.comment(0x99F4, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)

d.label(0x99F7, 'rx_complete_update_rxcb')
d.comment(0x99F7, 'Update buffer pointer and check for Tube', align=Align.INLINE)
d.comment(0x99FA, 'Transfer not done: skip buffer update', align=Align.INLINE)
d.comment(0x99FC, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x99FE, 'CLC for address add', align=Align.INLINE)
d.comment(0x99FF, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x9A01, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x9A03, 'Carry: increment buffer high byte', align=Align.INLINE)

d.label(0x9A05, 'store_buf_ptr_lo')
d.comment(0x9A05, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x9A07, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x9A09, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x9A0A, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x9A0C, 'Store high byte to RXCB', align=Align.INLINE)

d.label(0x9A0E, 'skip_buf_ptr_update')
d.comment(0x9A0E, 'Check port byte again', align=Align.INLINE)
d.comment(0x9A11, 'Port=0: immediate op, discard+listen', align=Align.INLINE)
d.comment(0x9A13, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x9A16, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x9A18, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x9A1A, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x9A1B, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x9A1E, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x9A20, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x9A21, 'Load port byte', align=Align.INLINE)
d.comment(0x9A24, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x9A26, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x9A27, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x9A2A, 'Set bit7 = reception complete flag', align=Align.INLINE)
d.comment(0x9A2C, 'Store to RXCB (marks CB as complete)', align=Align.INLINE)
d.comment(0x9A2E, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x9A36, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x9A3A, 'Release Tube claim before discarding', align=Align.INLINE)
d.comment(0x9A3D, 'Re-enter idle RX listen mode', align=Align.INLINE)
d.comment(0x9A40, 'Install nmi_rx_scout (&96F2) as NMI handler', align=Align.INLINE)
d.comment(0x9A42, 'High byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x9A44, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9A56, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x9A59, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x9A5B, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x9A5D, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x9A5F, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x9A61, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x9A63, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x9A65, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x9A66, 'SEC for subtract', align=Align.INLINE)
d.comment(0x9A67, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x9A69, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x9A6A, 'Load protection mask from LSTAT', align=Align.INLINE)

d.label(0x9A6D, 'rotate_prot_mask')
d.comment(0x9A6D, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x9A6E, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x9A6F, 'Loop until bit aligned', align=Align.INLINE)
d.comment(0x9AFC, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x9AFE, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x9AFF, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x9B01, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x9B03, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x9B05, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x9B07, 'Load requesting station number', align=Align.INLINE)
d.comment(0x9B0A, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x9B0D, 'Load requesting network number', align=Align.INLINE)
d.comment(0x9B10, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x9B12, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x9B15, 'Save ctrl byte for TX response', align=Align.INLINE)
d.comment(0x9B18, 'IER bit 2: disable SR interrupt', align=Align.INLINE)
d.comment(0x9B1A, 'Write IER to disable SR', align=Align.INLINE)
d.comment(0x9B1D, 'Read ACR for shift register config', align=Align.INLINE)
d.comment(0x9B20, 'Isolate shift register mode bits (2-4)', align=Align.INLINE)
d.comment(0x9B22, 'Save original SR mode for later restore', align=Align.INLINE)
d.comment(0x9B25, 'Reload ACR for modification', align=Align.INLINE)
d.comment(0x9B28, 'Clear SR mode bits (keep other bits)', align=Align.INLINE)
d.comment(0x9B2A, 'SR mode 2: shift in under φ2', align=Align.INLINE)
d.comment(0x9B2C, 'Apply new shift register mode', align=Align.INLINE)
d.comment(0x9B2F, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x9B32, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x9BC7, 'Save X on stack', align=Align.INLINE)
d.comment(0x9BC8, 'Push X', align=Align.INLINE)
d.comment(0x9BC9, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x9BCB, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x9BCD, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9BD1, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x9BD3, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9BD6, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x9BD8, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x9BDA, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x9BDC, 'Bit7 clear: normal data transfer', align=Align.INLINE)

d.label(0x9BDF, 'tx_imm_op_setup')
d.comment(0x9BDF, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9BE2, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x9BE3, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x9BE4, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x9BE6, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9BE9, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x9BEB, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x9BED, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x9BEF, 'SEC: init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9BF0, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x9BF1, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)

d.label(0x9BF3, 'calc_peek_poke_size')
d.comment(0x9BF3, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x9BF5, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x9BF9, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x9BFA, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x9BFC, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x9C04, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9C05, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9C07, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9C09, 'Discard final borrow', align=Align.INLINE)

d.label(0x9C0A, 'tx_ctrl_range_check')
d.comment(0x9C0A, 'Ctrl < &81: not an immediate op', align=Align.INLINE)
d.comment(0x9C0C, 'Below range: normal data transfer', align=Align.INLINE)
d.comment(0x9C0E, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x9C10, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x9C12, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)

d.label(0x9C14, 'copy_imm_params')
d.comment(0x9C14, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x9C16, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x9C19, 'Next byte', align=Align.INLINE)
d.comment(0x9C1A, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x9C1C, 'No: continue copying', align=Align.INLINE)

d.label(0x9C1E, 'tx_line_idle_check')
d.comment(0x9C1E, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x9C20, 'BIT SR2: test if line is idle', align=Align.INLINE)
d.comment(0x9C23, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x9C25, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x9C27, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x9C28, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x9C2A, 'Store scout frame length', align=Align.INLINE)
d.comment(0x9C2D, 'A=0: init low byte of timeout counter', align=Align.INLINE)

d.label(0x9C36, 'test_inactive_retry')

d.label(0x9C54, 'inactive_retry')
d.comment(0x9C71, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x9C74, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x9C79, 'ALWAYS branch to shared error handler', align=Align.INLINE)

d.label(0x9C7B, 'tx_no_clock_error')
d.comment(0x9C7B, "Error &43 = 'No Clock'", align=Align.INLINE)

d.label(0x9C7D, 'store_tx_error')
d.comment(0x9C7D, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x9C7F, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x9C81, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x9C83, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x9C86, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x9C87, 'Move to X register', align=Align.INLINE)
d.comment(0x9C88, 'Return to TX caller', align=Align.INLINE)
d.comment(0x9C8E, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9C91, 'Install NMI handler at &9D2D (nmi_tx_data)', align=Align.INLINE)
d.comment(0x9C93, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x9C95, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x9C98, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x9C9E, 'Load destination port number', align=Align.INLINE)
d.comment(0x9CA1, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x9CA3, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x9CA6, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x9CA9, 'Store operation flags', align=Align.INLINE)
d.comment(0x9CAC, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x9CAF, 'Store expected transfer length', align=Align.INLINE)

d.label(0x9CEF, 'setup_data_xfer')
d.comment(0x9CEF, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x9CF2, 'AND with dest network', align=Align.INLINE)
d.comment(0x9CF5, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x9CF7, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x9CF9, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x9CFB, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x9CFE, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x9D00, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x9D03, 'Y=4: start of address data in TXCB', align=Align.INLINE)

d.label(0x9D05, 'copy_bcast_addr')
d.comment(0x9D05, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x9D07, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x9D0A, 'Next byte', align=Align.INLINE)
d.comment(0x9D0B, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9D0D, 'No: continue copying', align=Align.INLINE)

d.label(0x9D11, 'setup_unicast_xfer')
d.comment(0x9D11, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x9D13, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x9D16, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x9D18, 'Store scout status', align=Align.INLINE)
d.comment(0x9D1B, 'Copy TX block pointer to workspace ptr', align=Align.INLINE)
d.comment(0x9D1D, 'Store low byte', align=Align.INLINE)
d.comment(0x9D1F, 'Copy TX block pointer high byte', align=Align.INLINE)
d.comment(0x9D21, 'Store high byte', align=Align.INLINE)
d.comment(0x9D23, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x9D26, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x9D27, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x9D28, 'Second PLA', align=Align.INLINE)
d.comment(0x9D29, 'Third PLA', align=Align.INLINE)
d.comment(0x9D2A, 'Fourth PLA', align=Align.INLINE)
d.comment(0x9D2B, 'Restore X from A', align=Align.INLINE)
d.comment(0x9D2C, 'Return to caller', align=Align.INLINE)

d.label(0x9D33, 'tx_fifo_write')

d.label(0x9D57, 'tx_fifo_not_ready')

d.label(0x9D5E, 'tx_store_error')

d.label(0x9D61, 'delay_nmi_disable')
d.comment(0x9D6B, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x9D6E, 'Install NMI handler at &9D75 (nmi_tx_complete)', align=Align.INLINE)
d.comment(0x9D70, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9D72, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9D82, 'check_handshake_bit')

d.label(0x9D8C, 'install_reply_scout')
d.comment(0x9D8C, 'Install nmi_reply_scout at &9D30', align=Align.INLINE)
d.comment(0x9D9A, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x9DA2, 'Install nmi_reply_cont at &9DA9', align=Align.INLINE)
d.comment(0x9DB3, 'Install nmi_reply_validate at &9DC2', align=Align.INLINE)
d.comment(0x9DBA, 'IRQ set -- fall through to &9DC2 without RTI', align=Align.INLINE)

d.label(0x9DBF, 'reject_reply')
d.comment(0x9DE0, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x9DE5, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x9DEA, 'High byte &9E of next handler address', align=Align.INLINE)
d.comment(0x9DEC, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x9DEF, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x9DFD, 'Load dest network for scout ACK TX', align=Align.INLINE)
d.comment(0x9E00, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x9E03, 'Install nmi_scout_ack_src at &9E0A', align=Align.INLINE)
d.comment(0x9E05, 'High byte &9D of handler address', align=Align.INLINE)
d.comment(0x9E07, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9E0A, 'Read our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x9E0D, 'BIT SR1: check TDRA before writing', align=Align.INLINE)
d.comment(0x9E10, 'TDRA not ready: TX error', align=Align.INLINE)
d.comment(0x9E15, 'Network = 0 (local network)', align=Align.INLINE)
d.comment(0x9E17, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E1A, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x9E1C, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x9E1F, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x9E21, 'Install nmi_data_tx at &9E2F', align=Align.INLINE)
d.comment(0x9E23, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9E25, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9E28, 'install_imm_data_nmi')
d.comment(0x9E28, 'Install nmi_data_tx_tube at &9E81', align=Align.INLINE)
d.comment(0x9E2A, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9E2C, 'Install and return via set_nmi_vector', align=Align.INLINE)

d.label(0x9E34, 'data_tx_check_fifo')
d.comment(0x9E38, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x9E3B, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E3C, 'No page crossing', align=Align.INLINE)
d.comment(0x9E3E, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E40, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E42, 'Increment buffer high byte', align=Align.INLINE)

d.label(0x9E44, 'write_second_tx_byte')
d.comment(0x9E44, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x9E46, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x9E49, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E4A, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x9E4C, 'No page crossing', align=Align.INLINE)
d.comment(0x9E4E, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E50, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E52, 'Increment buffer high byte', align=Align.INLINE)

d.label(0x9E54, 'check_irq_loop')
d.comment(0x9E54, 'BIT SR1: test IRQ (N=bit7) for tight loop', align=Align.INLINE)
d.comment(0x9E57, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9E59, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9E5E, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x9E61, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x9E64, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x9E66, 'Install discard_reset_listen at &99DB', align=Align.INLINE)
d.comment(0x9E68, 'High byte of &99DB handler', align=Align.INLINE)
d.comment(0x9E6A, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9E6D, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x9E7B, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x9E7E, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x9E81, 'Tube TX: BIT SR1 test TDRA', align=Align.INLINE)

d.label(0x9E84, 'tube_tx_fifo_write')
d.comment(0x9E84, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E86, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x9E89, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x9E8C, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x9E8E, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9E90, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9E92, 'No further carry', align=Align.INLINE)
d.comment(0x9E94, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9E96, 'No further carry', align=Align.INLINE)
d.comment(0x9E98, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9E9A, 'Counter wrapped to zero: last data', align=Align.INLINE)

d.label(0x9E9C, 'write_second_tube_byte')
d.comment(0x9E9C, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x9E9F, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x9EA2, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x9EA4, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9EA6, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9EA8, 'No further carry', align=Align.INLINE)

d.label(0x9EAA, 'tube_tx_inc_byte3')
d.comment(0x9EAA, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9EAC, 'No further carry', align=Align.INLINE)
d.comment(0x9EAE, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9EB0, 'Counter wrapped to zero: last data', align=Align.INLINE)

d.label(0x9EB2, 'check_tube_irq_loop')
d.comment(0x9EB2, 'BIT SR1: test IRQ for tight loop', align=Align.INLINE)
d.comment(0x9EB5, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9EB7, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9EBC, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9EBF, 'Install nmi_final_ack at &9E5C', align=Align.INLINE)
d.comment(0x9EC1, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9EC3, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x9ED5, 'Install nmi_final_ack_net at &9E70', align=Align.INLINE)
d.comment(0x9EE6, 'Install nmi_final_ack_validate at &9E84', align=Align.INLINE)
d.comment(0x9EED, 'IRQ set -- fall through to &9E84 without RTI', align=Align.INLINE)

d.label(0x9F0F, 'check_fv_final_ack')


d.subroutine(0x9F1A, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")
d.comment(0x9F1A, 'A=&41: not listening error code', align=Align.INLINE)

d.label(0x9F54, 'calc_transfer_size')

d.label(0x9F81, 'restore_x_and_return')

d.label(0x9F84, 'fallback_calc_transfer')
d.comment(0x9F84, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x9F88, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x9F8A, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9F8F, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x9F93, 'Propagate borrow from lo subtraction', align=Align.INLINE)
d.comment(0x9F95, 'Temp store adjusted current ptr hi', align=Align.INLINE)
d.comment(0x9F97, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x9F9B, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x9F9D, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x9F9F, 'Load RXCB[9] (start ptr hi)', align=Align.INLINE)
d.comment(0x9FA1, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9FA2, 'start_hi - adjusted current_hi', align=Align.INLINE)
d.comment(0x9FA8, 'INTOFF: disable NMIs while switching ROM', align=Align.INLINE)
d.comment(0x9FAB, 'Save A', align=Align.INLINE)
d.comment(0x9FAC, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9FAD, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x9FAE, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x9FB0, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x9FB3, 'Jump to scout handler in ROM', align=Align.INLINE)
d.comment(0x9FB6, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x9FB9, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x9FBC, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x9FBE, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x9FC1, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9FC3, 'Restore A from stack', align=Align.INLINE)
d.comment(0x9FC4, 'INTON: re-enable NMIs', align=Align.INLINE)
d.comment(0x9FC7, 'Return from interrupt', align=Align.INLINE)
d.comment(0x9FE0, 'Save original byte for low nibble', align=Align.INLINE)
d.comment(0x9FE1, 'Shift high nibble right (4x LSR)', align=Align.INLINE)
d.comment(0x9FE5, 'Print high nibble as hex', align=Align.INLINE)
d.comment(0x9FE8, 'Restore byte; fall through for low nibble', align=Align.INLINE)
d.comment(0x9FE9, 'Mask to low nibble (0-F)', align=Align.INLINE)
d.comment(0x9FEB, 'Digit A-F?', align=Align.INLINE)
d.comment(0x9FED, 'No: skip letter offset', align=Align.INLINE)
d.comment(0x9FEF, 'A-F: ADC #6 + ADC #&30 + C = &41-&46', align=Align.INLINE)

d.label(0x9FF1, 'add_ascii_base')
d.comment(0x9FF1, "Add ASCII '0' base (with carry)", align=Align.INLINE)
d.comment(0x9FF3, 'Write character', align=Align.INLINE)
d.comment(0x9FF6, 'C=1: callers use SEC as sentinel', align=Align.INLINE)
d.comment(0x9FF7, 'Return', align=Align.INLINE)
d.comment(0x80F8, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80F9, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FA, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FB, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FC, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FD, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FE, '(bus settling continued)', align=Align.INLINE)
d.comment(0x80FF, '(bus settling continued)', align=Align.INLINE)
d.comment(0x8101, 'Load workspace byte for this ROM slot', align=Align.INLINE)
d.comment(0x8104, 'Push detection flag', align=Align.INLINE)
d.comment(0x8105, 'Non-zero: ROM already detected, skip probe', align=Align.INLINE)
d.comment(0x8107, 'First call: mark ROM as present', align=Align.INLINE)
d.comment(0x810A, 'Read station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x810D, 'Zero: no ADLC hardware, skip', align=Align.INLINE)
d.comment(0x810F, 'Second read: bus stability check', align=Align.INLINE)
d.comment(0x8112, 'Same value: ADLC present, continue', align=Align.INLINE)
d.comment(0x8114, 'C=1: prepare to set disable flag', align=Align.INLINE)
d.comment(0x8115, 'Bit 7 into workspace: disable this ROM', align=Align.INLINE)
d.comment(0x8118, 'Restore detection flag', align=Align.INLINE)
d.comment(0x8289, 'Y=&82: ROM page high byte', align=Align.INLINE)
d.comment(0x828B, 'Execute command string at (X, Y)', align=Align.INLINE)
d.comment(0x85C8, 'X to os_text_ptr (text ptr lo)', align=Align.INLINE)
d.comment(0x85CA, 'Y to os_text_ptr hi', align=Align.INLINE)
d.comment(0x85CC, 'X to FS command ptr lo', align=Align.INLINE)
d.comment(0x85CF, 'Y to FS command ptr hi', align=Align.INLINE)
d.comment(0x85D2, 'A = function code / command', align=Align.INLINE)
d.comment(0x85D4, 'X = control block ptr lo', align=Align.INLINE)
d.comment(0x85D6, 'Y = control block ptr hi', align=Align.INLINE)
d.comment(0x85D8, 'X dup for indexed access via (fs_crc)', align=Align.INLINE)
d.comment(0x85DA, 'Y dup for indexed access', align=Align.INLINE)
d.comment(0x85DC, 'Return', align=Align.INLINE)
d.comment(0x8687, 'X=&C0: TX control block at &00C0', align=Align.INLINE)
d.comment(0x8689, 'Set TX pointer lo', align=Align.INLINE)
d.comment(0x868B, 'X=0: page zero', align=Align.INLINE)
d.comment(0x868D, 'Set TX pointer hi', align=Align.INLINE)
d.comment(0x8693, 'Save retry count on stack', align=Align.INLINE)
d.comment(0x8694, 'Transfer timeout to A', align=Align.INLINE)
d.comment(0x8695, 'Save timeout on stack', align=Align.INLINE)
d.comment(0x8696, 'X=0 for (net_tx_ptr,X) indirect', align=Align.INLINE)
d.comment(0x8698, 'Load TXCB byte 0 (control/status)', align=Align.INLINE)
d.comment(0x869A, 'Write control byte to start TX', align=Align.INLINE)
d.comment(0x869C, 'Save control byte for retry', align=Align.INLINE)
d.comment(0x869D, 'Test TX semaphore (C=1 when free)', align=Align.INLINE)
d.comment(0x86A0, 'Spin until semaphore released', align=Align.INLINE)
d.comment(0x86A2, 'Copy TX ptr lo to NMI block', align=Align.INLINE)
d.comment(0x86A4, 'Store for NMI handler access', align=Align.INLINE)
d.comment(0x86A6, 'Copy TX ptr hi to NMI block', align=Align.INLINE)
d.comment(0x86A8, 'Store for NMI handler access', align=Align.INLINE)
d.comment(0x86AA, 'Initiate ADLC TX via trampoline', align=Align.INLINE)
d.comment(0x86AD, 'Poll TXCB byte 0 for completion', align=Align.INLINE)
d.comment(0x86AF, 'Bit 7 set: still busy, keep polling', align=Align.INLINE)
d.comment(0x86B1, 'Shift bit 6 into bit 7 (error flag)', align=Align.INLINE)
d.comment(0x86B2, 'Bit 6 clear: success, clean return', align=Align.INLINE)
d.comment(0x86B4, 'Shift bit 5 into carry', align=Align.INLINE)
d.comment(0x86B5, 'Zero: fatal error, no escape', align=Align.INLINE)
d.comment(0x86B7, 'Check for user escape condition', align=Align.INLINE)
d.comment(0x86BA, 'Discard saved control byte', align=Align.INLINE)
d.comment(0x86BB, 'Save to X for retry delay', align=Align.INLINE)
d.comment(0x86BC, 'Restore timeout parameter', align=Align.INLINE)
d.comment(0x86BD, 'Back to Y', align=Align.INLINE)
d.comment(0x86BE, 'Restore retry count', align=Align.INLINE)
d.comment(0x86BF, 'No retries left: report error', align=Align.INLINE)
d.comment(0x86C1, 'Decrement retry count', align=Align.INLINE)
d.comment(0x86C3, 'Save updated retry count', align=Align.INLINE)
d.comment(0x86C4, 'Timeout to A for delay', align=Align.INLINE)
d.comment(0x86C5, 'Save timeout parameter', align=Align.INLINE)
d.comment(0x86C6, 'Control byte for delay duration', align=Align.INLINE)
d.comment(0x86C7, 'Inner delay loop', align=Align.INLINE)
d.comment(0x86C8, 'Spin until X=0', align=Align.INLINE)
d.comment(0x86CA, 'Outer delay loop', align=Align.INLINE)
d.comment(0x86CB, 'Continue delay', align=Align.INLINE)
d.comment(0x86CF, 'Save error code in X', align=Align.INLINE)
d.comment(0x86D0, "Report 'Not listening' error", align=Align.INLINE)
d.comment(0x86D3, 'Discard saved control byte', align=Align.INLINE)
d.comment(0x86D4, 'Discard timeout parameter', align=Align.INLINE)
d.comment(0x86D5, 'Discard retry count', align=Align.INLINE)
d.comment(0x86D6, 'Return (success)', align=Align.INLINE)
d.comment(0x8D21, "Data byte: boot_cmd_strings 'x'", align=Align.INLINE)
d.comment(0x8D22, "Data bytes: boot_cmd_strings 'ec'", align=Align.INLINE)
d.comment(0x8D24, 'Check if messages enabled', align=Align.INLINE)
d.comment(0x8D27, 'Zero: no info to display, return', align=Align.INLINE)
d.comment(0x8D29, 'Y=0: start of filename', align=Align.INLINE)
d.comment(0x8D2B, 'Load current directory prefix flag', align=Align.INLINE)
d.comment(0x8D2E, 'No prefix: skip directory display', align=Align.INLINE)
d.comment(0x8D30, 'Print directory name prefix', align=Align.INLINE)
d.comment(0x8D33, 'N=1: skip to hex fields after dir', align=Align.INLINE)
d.comment(0x8D35, 'Load next filename character', align=Align.INLINE)
d.comment(0x8D37, 'CR: end of filename', align=Align.INLINE)
d.comment(0x8D39, 'CR found: pad remaining with spaces', align=Align.INLINE)
d.comment(0x8D3B, 'Space: end of name field', align=Align.INLINE)
d.comment(0x8D3D, 'Space found: pad with spaces', align=Align.INLINE)
d.comment(0x8D42, 'Advance to next character', align=Align.INLINE)
d.comment(0x8D43, 'Continue printing filename', align=Align.INLINE)
d.comment(0x8D45, 'Print space for padding', align=Align.INLINE)
d.comment(0x8D48, 'Advance column counter', align=Align.INLINE)
d.comment(0x8D49, 'Reached 12 columns?', align=Align.INLINE)
d.comment(0x8D4B, 'No: continue padding', align=Align.INLINE)
d.comment(0x8D4D, 'Y=5: load address offset (4 bytes)', align=Align.INLINE)
d.comment(0x8D4F, 'Print load address', align=Align.INLINE)
d.comment(0x8D52, 'Print exec address and file length', align=Align.INLINE)
d.comment(0x8D58, 'Y=9: exec address offset (4 bytes)', align=Align.INLINE)
d.comment(0x8D5A, 'Print exec address', align=Align.INLINE)
d.comment(0x8D5D, 'Y=&0C: file length offset', align=Align.INLINE)
d.comment(0x8D5F, 'X=3: print 3 bytes (24-bit length)', align=Align.INLINE)
d.comment(0x8E74, 'Save carry via rotate', align=Align.INLINE)
d.comment(0x8E77, 'A=&3F: handle closed/unused marker', align=Align.INLINE)
d.comment(0x8E79, 'Write marker to handle slot', align=Align.INLINE)
d.comment(0x8E7B, 'Restore carry from rotate', align=Align.INLINE)
d.comment(0x96C8, 'INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x96CB, 'A=0: clear TX and init flags', align=Align.INLINE)
d.comment(0x96CD, 'Clear TX semaphore (allow new TX)', align=Align.INLINE)
d.comment(0x96D0, 'Clear Econet init flag', align=Align.INLINE)
d.comment(0x96D3, 'Y=5: status flags offset', align=Align.INLINE)
d.comment(0x96D5, 'Re-enter idle RX listen mode', align=Align.INLINE)
d.comment(0x96DA, 'Write CR1: full reset', align=Align.INLINE)
d.comment(0x96DD, 'CR4=&1E: 8-bit word, abort ext, NRZ', align=Align.INLINE)
d.comment(0x96DF, 'Write CR4 via ADLC reg 3 (AC=1)', align=Align.INLINE)
d.comment(0x96E4, 'Write CR3=0: clear loop-back/AEX/DTR', align=Align.INLINE)
d.comment(0x9A47, 'Y=4: start at RX CB offset 4', align=Align.INLINE)
d.comment(0x9A49, 'Load scout field (stn/net/ctrl/port)', align=Align.INLINE)
d.comment(0x9A4C, 'Store to port workspace buffer', align=Align.INLINE)
d.comment(0x9A4F, 'All 8 fields copied?', align=Align.INLINE)
d.comment(0x9A51, 'No: continue copy loop', align=Align.INLINE)
d.comment(0x9A95, 'Buffer start lo = &00', align=Align.INLINE)
d.comment(0x9A97, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9A99, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x9A9B, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9A9D, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9A9F, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9AA1, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x9AA3, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9AA5, 'Y=3: copy 4 bytes (3 down to 0)', align=Align.INLINE)
d.comment(0x9AA7, 'Load remote address byte', align=Align.INLINE)
d.comment(0x9AAA, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x9AAD, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9AAE, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x9AB0, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x9AB3, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9AB5, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AB7, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AB9, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9ABB, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x9ABE, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9AC0, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9AC2, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x9AC4, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9AC6, 'Buffer start lo = &25', align=Align.INLINE)
d.comment(0x9AC8, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9ACA, 'Buffer hi = &7F (below screen)', align=Align.INLINE)
d.comment(0x9ACC, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9ACE, 'Enter reply build path', align=Align.INLINE)
d.comment(0x9AD1, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9AD3, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AD5, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AD7, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9AD9, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x9ADB, 'Store scout status', align=Align.INLINE)
d.comment(0x9ADE, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x9AE1, 'C=0: transfer not set up, discard', align=Align.INLINE)
d.comment(0x9AE3, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x9AE6, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x9AE8, 'Store updated TX flags', align=Align.INLINE)
d.comment(0x9AEB, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9AED, 'Write CR1: enable TX interrupts', align=Align.INLINE)
d.comment(0x9AF0, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x9AF2, 'Write CR2 for TX setup', align=Align.INLINE)
d.comment(0x9AF5, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x9AF7, 'Y=&9B: dispatch table page', align=Align.INLINE)
d.comment(0x9AF9, 'Acknowledge and write TX dest', align=Align.INLINE)
d.comment(0x9B35, 'A=&04: IFR bit 2 (SR) mask', align=Align.INLINE)
d.comment(0x9B37, 'Test SR interrupt pending', align=Align.INLINE)
d.comment(0x9B3A, 'SR fired: handle TX completion', align=Align.INLINE)
d.comment(0x9B3C, 'A=5: no SR, return status 5', align=Align.INLINE)
d.comment(0x9B3E, 'Return (no SR interrupt)', align=Align.INLINE)
d.comment(0x9B3F, 'Save X', align=Align.INLINE)
d.comment(0x9B40, 'Push X', align=Align.INLINE)
d.comment(0x9B41, 'Save Y', align=Align.INLINE)
d.comment(0x9B42, 'Push Y', align=Align.INLINE)
d.comment(0x9B43, 'Read ACR for shift register mode', align=Align.INLINE)
d.comment(0x9B46, 'Clear SR mode bits (2-4)', align=Align.INLINE)
d.comment(0x9B48, 'Restore original SR mode', align=Align.INLINE)
d.comment(0x9B4B, 'Write updated ACR', align=Align.INLINE)
d.comment(0x9B4E, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x9B51, 'A=&04: SR bit mask', align=Align.INLINE)
d.comment(0x9B53, 'Clear SR in IFR', align=Align.INLINE)
d.comment(0x9B56, 'Disable SR in IER', align=Align.INLINE)
d.comment(0x9B59, 'Load ctrl byte for dispatch', align=Align.INLINE)
d.comment(0x9B5C, 'Ctrl >= &86? (HALT/CONTINUE)', align=Align.INLINE)
d.comment(0x9B5E, 'Yes: skip protection mask save', align=Align.INLINE)
d.comment(0x9B60, 'Load current protection mask', align=Align.INLINE)
d.comment(0x9B63, 'Save mask before JSR modification', align=Align.INLINE)
d.comment(0x9B66, 'Enable bits 2-4 (allow JSR ops)', align=Align.INLINE)
d.comment(0x9B68, 'Store modified protection mask', align=Align.INLINE)
d.comment(0x9B6B, 'Load handler addr hi from table', align=Align.INLINE)
d.comment(0x9B6E, 'Push handler hi', align=Align.INLINE)
d.comment(0x9B6F, 'Load handler addr lo from table', align=Align.INLINE)
d.comment(0x9B72, 'Push handler lo', align=Align.INLINE)
d.comment(0x9B73, 'Dispatch via RTS (addr-1 on stack)', align=Align.INLINE)
d.comment(0x9B7E, 'Push hi of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x9B80, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x9B81, 'Push lo of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x9B83, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x9B84, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)
d.comment(0x9B87, 'Y=8: network event type', align=Align.INLINE)
d.comment(0x9B89, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9B8C, 'A = remote address hi', align=Align.INLINE)
d.comment(0x9B92, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9B95, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9B98, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x9B9B, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x9B9E, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9BA1, 'A=&04: bit 2 mask for rx_flags', align=Align.INLINE)
d.comment(0x9BA3, 'Test if already halted', align=Align.INLINE)
d.comment(0x9BA6, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x9BA8, 'Set bit 2 in rx_flags', align=Align.INLINE)
d.comment(0x9BAB, 'Store halt flag', align=Align.INLINE)
d.comment(0x9BAE, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x9BB0, 'Enable interrupts during halt wait', align=Align.INLINE)
d.comment(0x9BB1, 'Test halt flag', align=Align.INLINE)
d.comment(0x9BB4, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x9C2F, 'Save TX index', align=Align.INLINE)
d.comment(0x9C32, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x9C33, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x9C38, 'Save interrupt state', align=Align.INLINE)
d.comment(0x9C39, 'Disable interrupts for ADLC access', align=Align.INLINE)
d.comment(0x9C4A, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x9C57, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x9C59, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x9C5C, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C5E, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x9C61, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C63, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x9C66, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C68, 'All 3 bytes overflowed: line jammed', align=Align.INLINE)
d.comment(0x9C6B, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9CD3, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)
d.comment(0x9CD5, 'Store scout status', align=Align.INLINE)
d.comment(0x9CD8, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x9CD9, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9CDA, 'Y=&0C: start at offset 12', align=Align.INLINE)
d.comment(0x9CDC, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x9CDF, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x9CE0, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x9CE2, 'Store updated address byte', align=Align.INLINE)
d.comment(0x9CE5, 'Next byte', align=Align.INLINE)
d.comment(0x9CE6, 'Save carry for next addition', align=Align.INLINE)

d.label(0x0414, 'tube_send_release')

d.label(0x8EF9, 'rs')

d.label(0x9148, 'nword')

d.label(0x96B2, 'poll_nmi_ready')

d.label(0x97F7, 'ack_scout_match')

d.label(0x9A03, 'inc_rxcb_buf_hi')

d.label(0x9A47, 'copy_scout_fields')

d.label(0x9AE3, 'set_tx_reply_flag')

d.label(0x9AEB, 'rx_imm_halt_cont')

d.label(0x9AF0, 'tx_cr2_setup')

d.label(0x9AF5, 'tx_nmi_setup')

d.label(0x9B32, 'imm_op_discard')

d.label(0x9B35, 'check_sr_irq')

d.label(0x9C40, 'test_line_idle')

d.label(0x9CCB, 'imm_op_status3')

d.label(0x9D16, 'proc_op_status2')

d.label(0x9EA6, 'tube_tx_inc_byte2')

d.label(0x9EAE, 'tube_tx_inc_byte4')

d.label(0x0020, 'tube_send_zero_r2')

d.label(0x8211, 'return_service')

d.label(0x87D3, 'send_fs_reply')

d.label(0x8D55, 'print_newline')

d.label(0x96D5, 'enter_rx_listen')

d.label(0x9A0C, 'store_rxcb_buf_hi')

d.label(0x9CD5, 'store_status_add4')

d.label(0x9D18, 'store_status_copy_ptr')

d.label(0x8001, 'lang_entry_lo')

d.label(0x8002, 'lang_entry_hi')

d.label(0x8004, 'svc_entry_lo')

d.label(0x0051, 'tube_jmp_target')

d.label(0x0518, 'tube_ctrl_values')

d.label(0x86AD, 'tx_poll_status')

d.label(0x8C06, 'fs_cmd_dispatch_hi')

d.label(0x8D08, 'boot_option_text')

d.label(0x8D1C, 'boot_oscli_offset')

d.label(0x8EB0, 'osword_handler_lo')

d.label(0x90A3, 'netvec_handler_hi')

d.label(0x9A04, 'imm_dispatch_lo')

d.label(0x9AF1, 'tx_done_handler_lo')

d.label(0x9AF6, 'tx_done_handler_hi')

d.label(0x9C42, 'sr2_idle_status')

d.label(0x9EA7, 'tube_tx_count_2')

d.label(0x9EAF, 'tube_tx_count_4')

d.label(0x8262, 'copy_vectors_loop')

d.label(0x869D, 'tx_semaphore_spin')

d.label(0x87E3, 'copy_attr_loop')

d.label(0x8825, 'block_addr_loop')

d.label(0x8C99, 'cattxt')

d.label(0x9117, 'poll_rxcb_loop')

d.label(0x9A49, 'copy_scout_loop')

d.label(0x9AA7, 'copy_addr_loop')

d.label(0x9BB1, 'halt_spin_loop')

d.label(0x9CDC, 'add_bytes_loop')

d.label(0x046D, 'flush_r3_nmi_check')
d.comment(0x046D, 'Flush R3 data (first byte)', align=Align.INLINE)

d.label(0x8114, 'no_adlc_found')

d.label(0x8118, 'adlc_detect_done')

d.label(0x852D, 'fs_reply_poll')

d.label(0x869A, 'tx_retry')

d.label(0x86C7, 'msdely')

d.label(0x86CF, 'tx_not_listening')

d.label(0x86D3, 'tx_success')

d.label(0x87E6, 'direct_attr_copy')

d.label(0x881A, 'next_block')

d.label(0x8843, 'clamp_dest_setup')

d.label(0x8C71, 'cat_check_access')

d.label(0x8D35, 'next_filename_char')

d.label(0x8D4D, 'print_hex_fields')

d.label(0x8DA5, 'dir_column_check')

d.label(0x8DA7, 'dir_print_char')

d.label(0x8E1C, 'exec_at_load_addr')

d.label(0x9196, 'rxcb_matched')

d.label(0x9221, 'pril1')

d.label(0x96B7, 'nmi_vec_lo_match')

d.label(0x97AF, 'scout_ctrl_check')

d.label(0x97CB, 'scout_port_match')

d.label(0x97DC, 'scout_station_check')

d.label(0x97E0, 'scout_network_match')

d.label(0x97EF, 'scout_accept')

d.label(0x98F8, 'rx_update_buf')

d.label(0x990E, 'rx_check_error')

d.label(0x9A76, 'imm_op_dispatch')

d.label(0x9A82, 'imm_op_out_of_range')

d.label(0x9B3F, 'tx_done_error')

d.label(0x9B6B, 'tx_done_classify')

d.label(0x9D1B, 'skip_buf_setup')

d.label(0x9E75, 'jmp_tx_result_fail')
d.comment(0x041E, '&80 sentinel: clear address claim', align=Align.INLINE)

d.label(0x0432, 'setup_data_transfer')
d.comment(0x0449, 'Send claimed address via R4', align=Align.INLINE)
d.comment(0x0470, 'Flush R3 data (second byte)', align=Align.INLINE)


d.subroutine(0x04CB, 'tube_init_reloc', title='Initialise relocation address for ROM transfer', description="""Sets source page to &8000 and page counter to &80. Checks
ROM type bit 5 for a relocation address in the ROM header;
if present, extracts the 4-byte address from after the
copyright string. Otherwise uses default &8000 start.""")
d.comment(0x0604, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0607, 'Read X parameter from co-processor', align=Align.INLINE)
d.comment(0x060A, 'Save in X', align=Align.INLINE)
d.comment(0x060B, 'Read Y parameter from co-processor', align=Align.INLINE)
d.comment(0x060E, 'Save in Y', align=Align.INLINE)
d.comment(0x060F, 'Read A (OSBYTE function code)', align=Align.INLINE)
d.comment(0x0612, 'Execute OSBYTE A,X,Y', align=Align.INLINE)
d.comment(0x061A, 'Send carry+status byte via R2', align=Align.INLINE)
d.comment(0x061D, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x0620, 'Not ready: keep polling', align=Align.INLINE)

d.label(0x0627, 'tube_osword')
d.comment(0x062A, 'Save OSWORD number in Y', align=Align.INLINE)
d.comment(0x062B, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x062E, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0634, 'No params (length=0): skip read loop', align=Align.INLINE)
d.comment(0x0636, 'Poll R2 status for data ready', align=Align.INLINE)
d.comment(0x0639, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x063B, 'Read param byte from R2', align=Align.INLINE)
d.comment(0x0641, 'Next param byte (descending)', align=Align.INLINE)
d.comment(0x0642, 'Loop until all params read', align=Align.INLINE)
d.comment(0x0647, 'Y=&01: param block at &0128', align=Align.INLINE)
d.comment(0x0649, 'Execute OSWORD with XY=&0128', align=Align.INLINE)
d.comment(0x064C, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x064F, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x0654, 'Decrement result byte counter', align=Align.INLINE)
d.comment(0x065A, 'Poll R2 status for ready', align=Align.INLINE)
d.comment(0x065D, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x065F, 'Send result byte via R2', align=Align.INLINE)
d.comment(0x0662, 'Next result byte (descending)', align=Align.INLINE)
d.comment(0x0663, 'Loop until all results sent', align=Align.INLINE)
d.comment(0x0665, 'Return to main event loop', align=Align.INLINE)
d.comment(0x0668, 'X=4: read 5 control block bytes', align=Align.INLINE)
d.comment(0x066A, 'Read control block byte from R2', align=Align.INLINE)
d.comment(0x066D, 'Store in zero page params', align=Align.INLINE)
d.comment(0x066F, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x0670, 'Loop until all 5 bytes read', align=Align.INLINE)
d.comment(0x0673, 'Y=0 for OSWORD 0', align=Align.INLINE)
d.comment(0x0675, 'A=0: OSWORD 0 (read line)', align=Align.INLINE)
d.comment(0x0676, 'Read input line from keyboard', align=Align.INLINE)
d.comment(0x067D, 'Escape: send &FF error to co-processor', align=Align.INLINE)
d.comment(0x0680, 'X=0: start of input buffer at &0700', align=Align.INLINE)
d.comment(0x0684, 'Send &7F (success) to co-processor', align=Align.INLINE)
d.comment(0x0687, 'Load char from input buffer', align=Align.INLINE)
d.comment(0x068A, 'Send char to co-processor', align=Align.INLINE)
d.comment(0x068D, 'Next character', align=Align.INLINE)
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
d.comment(0x06AA, 'ROR: shift escape bit 7 to carry', align=Align.INLINE)
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
d.comment(0x06C5, 'Poll R2 status (bit 7 = data ready)', align=Align.INLINE)
d.comment(0x06C8, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06CA, 'Read byte from Tube R2 data register', align=Align.INLINE)
d.comment(0x06CD, 'Return with byte in A', align=Align.INLINE)
d.comment(0x8081, 'Advance past matched command text', align=Align.INLINE)
d.comment(0x80C1, 'Copy command text to FS buffer', align=Align.INLINE)
d.comment(0x80CB, 'CSD handle zero: not logged in', align=Align.INLINE)
d.comment(0x80D7, 'FSCV function >= 8?', align=Align.INLINE)
d.comment(0x80DB, 'X = function code for dispatch', align=Align.INLINE)
d.comment(0x80DC, 'Save Y (command text ptr hi)', align=Align.INLINE)
d.comment(0x8277, 'A=&8F: issue service request', align=Align.INLINE)
d.comment(0x8279, "X=&0F: 'vectors claimed' service", align=Align.INLINE)
d.comment(0x827E, 'X=&0A: service &0A', align=Align.INLINE)
d.comment(0x8285, 'Non-zero: skip auto-boot', align=Align.INLINE)
d.comment(0x8298, 'ARGSV dispatch lo', align=Align.INLINE)
d.comment(0x829B, 'BGETV dispatch hi', align=Align.INLINE)
d.comment(0x829C, 'BPUTV dispatch lo', align=Align.INLINE)
d.comment(0x829E, 'GBPBV dispatch lo', align=Align.INLINE)
d.comment(0x829F, 'GBPBV dispatch hi', align=Align.INLINE)
d.comment(0x82A0, 'FINDV dispatch lo', align=Align.INLINE)
d.comment(0x82A1, 'FINDV dispatch hi', align=Align.INLINE)
d.comment(0x82A2, 'FSCV dispatch lo', align=Align.INLINE)
d.comment(0x82B7, 'FSCV handler hi', align=Align.INLINE)
d.comment(0x82BE, 'Return (workspace claim done)', align=Align.INLINE)
d.comment(0x834F, 'Load FS state byte at offset Y', align=Align.INLINE)
d.comment(0x8352, 'Store to workspace backup area', align=Align.INLINE)
d.comment(0x8354, 'Next byte down', align=Align.INLINE)
d.comment(0x8357, 'Loop for offsets &1D..&15', align=Align.INLINE)
d.comment(0x8359, 'A=&77: OSBYTE close spool/exec', align=Align.INLINE)


d.subroutine(0x8383, 'init_tx_reply_port', title='Initialise TX control block for FS reply on port &90', description="""Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
up the TX control block, stores the port and control bytes, then
decrements the control flag. Used by send_fs_reply_cmd to prepare
for receiving the fileserver's reply.""")
d.comment(0x8390, 'Return after port setup', align=Align.INLINE)
d.comment(0x83A9, 'Control flag', align=Align.INLINE)
d.comment(0x83AA, 'Port (FS command = &99)', align=Align.INLINE)
d.comment(0x83AD, 'Buffer start low', align=Align.INLINE)
d.comment(0x83AE, 'Buffer start high (page &0F)', align=Align.INLINE)
d.comment(0x83AF, 'Buffer start pad (4-byte Econet addr)', align=Align.INLINE)
d.comment(0x83B0, 'Buffer start pad', align=Align.INLINE)
d.comment(0x83B1, 'Buffer end low', align=Align.INLINE)
d.comment(0x83B2, 'Buffer end high (page &0F)', align=Align.INLINE)
d.comment(0x83B3, 'Buffer end pad', align=Align.INLINE)
d.comment(0x83B4, 'Buffer end pad', align=Align.INLINE)


d.subroutine(0x83B5, 'prepare_cmd_with_flag', title='Prepare FS command with carry set', description="""Alternate entry to prepare_fs_cmd that pushes A, loads &2A
into fs_error_ptr, and enters with carry set (SEC). The carry
flag is later tested by build_send_fs_cmd to select the
byte-stream (BSXMIT) transmission path.""", on_entry={'a': 'flag byte to include in FS command', 'y': 'function code for FS header'})
d.comment(0x83BC, 'A=&77: OSBYTE close spool/exec', align=Align.INLINE)
d.comment(0x840F, 'CLC for address addition', align=Align.INLINE)
d.comment(0x8495, 'Transfer A to Y for indexing', align=Align.INLINE)
d.comment(0x8497, 'Transfer to X for return', align=Align.INLINE)
d.comment(0x84CD, 'A=0: zero execution header bytes', align=Align.INLINE)
d.comment(0x84D2, 'Next byte', align=Align.INLINE)
d.comment(0x84D3, 'Loop until all zeroed', align=Align.INLINE)
d.comment(0x852D, 'Check for user escape condition', align=Align.INLINE)
d.comment(0x8556, 'LSR: get escape result bit', align=Align.INLINE)
d.comment(0x8557, 'Store escape result to TXCB', align=Align.INLINE)
d.comment(0x8559, 'Restore A', align=Align.INLINE)
d.comment(0x855A, "Non-zero: report 'Not listening'", align=Align.INLINE)
d.comment(0x8572, 'Set EOF flag for this handle', align=Align.INLINE)

d.label(0x8575, 'load_handle_mask')
d.comment(0x8575, 'Load handle bitmask for caller', align=Align.INLINE)
d.comment(0x8578, 'Return with handle mask in A', align=Align.INLINE)
d.comment(0x8606, 'Store return addr low as string ptr', align=Align.INLINE)
d.comment(0x8609, 'Store return addr high as string ptr', align=Align.INLINE)
d.comment(0x860B, 'Y=0: offset for indirect load', align=Align.INLINE)
d.comment(0x860F, 'No page wrap: skip high byte inc', align=Align.INLINE)
d.comment(0x8611, 'Handle page crossing in pointer', align=Align.INLINE)
d.comment(0x8642, 'Return with result in A', align=Align.INLINE)
d.comment(0x865D, 'Restore X from stack', align=Align.INLINE)
d.comment(0x865F, 'Return with mask in X', align=Align.INLINE)
d.comment(0x8667, 'Return with handle in A', align=Align.INLINE)
d.comment(0x8670, 'Next byte', align=Align.INLINE)
d.comment(0x8673, 'Return with Z flag result', align=Align.INLINE)
d.comment(0x8678, 'Return (FSCV 7 read handles)', align=Align.INLINE)
d.comment(0x868F, 'A=&FF: full retry count', align=Align.INLINE)


d.subroutine(0x86D7, 'copy_filename_ptr', title='Copy filename pointer to os_text_ptr and parse', description="""Copies the 2-byte filename pointer from (fs_options),Y into
os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
to parse the filename via GSINIT/GSREAD into the &0E30 buffer.""")


d.subroutine(0x86E3, 'parse_filename_gs_y', title='Parse filename via GSINIT/GSREAD from offset Y', description="""Sub-entry of parse_filename_gs that accepts a non-zero Y offset
into the (os_text_ptr) string. Initialises GSINIT, reads chars
via GSREAD into &0E30, CR-terminates the result, and sets up
fs_crc_lo/hi to point at the buffer.""")
d.comment(0x8705, 'Save A/X/Y in FS workspace', align=Align.INLINE)
d.comment(0x8711, 'A=&FF: branch to load path', align=Align.INLINE)
d.comment(0x8716, 'Copy parsed filename to cmd buffer', align=Align.INLINE)
d.comment(0x8719, 'Y=2: FS function code offset', align=Align.INLINE)
d.comment(0x874C, 'Display file info after FS reply', align=Align.INLINE)
d.comment(0x87D3, 'Send FS reply acknowledgement', align=Align.INLINE)
d.comment(0x87E1, 'Z=1: first byte, use A directly', align=Align.INLINE)
d.comment(0x87E3, 'Load attribute byte from FS reply', align=Align.INLINE)
d.comment(0x87E6, 'Store decoded access in param block', align=Align.INLINE)
d.comment(0x87E8, 'Next attribute byte', align=Align.INLINE)
d.comment(0x87FE, '(continued)', align=Align.INLINE)
d.comment(0x87FF, '(continued)', align=Align.INLINE)
d.comment(0x8800, '(continued)', align=Align.INLINE)
d.comment(0x880A, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x880D, 'Loop until offset 2 reached', align=Align.INLINE)
d.comment(0x8810, 'Y -= 3', align=Align.INLINE)
d.comment(0x8811, '(continued)', align=Align.INLINE)
d.comment(0x8812, '(continued)', align=Align.INLINE)
d.comment(0x8813, 'Return to caller', align=Align.INLINE)
d.comment(0x881A, 'X=0: clear hi bytes of block size', align=Align.INLINE)
d.comment(0x881C, 'Y=4: process 4 address bytes', align=Align.INLINE)
d.comment(0x881E, 'Clear block size hi byte 1', align=Align.INLINE)
d.comment(0x8821, 'Clear block size hi byte 2', align=Align.INLINE)
d.comment(0x8824, 'CLC for ADC in loop', align=Align.INLINE)
d.comment(0x8825, 'Source = current position', align=Align.INLINE)
d.comment(0x8827, 'Store source address byte', align=Align.INLINE)
d.comment(0x8829, 'Add block size to current position', align=Align.INLINE)
d.comment(0x8834, 'Carry: address overflowed, clamp', align=Align.INLINE)


d.subroutine(0x8990, 'return_a_zero', title='Return with A=0 via register restore', description="""Loads A=0 and branches (always taken) to the common register
restore exit at restore_args_return. Used as a shared exit
point by ARGSV, FINDV, and GBPBV when an operation is
unsupported or should return zero.""")
d.comment(0x89C6, 'A=handle bitmask for new file', align=Align.INLINE)
d.comment(0x8A2D, 'Return (unsupported function)', align=Align.INLINE)
d.comment(0x8CC5, 'Print two CRs (blank line)', align=Align.INLINE)

d.label(0x8CD2, 'cat_examine_loop')


d.subroutine(0x8D92, 'cat_column_separator', title='Print catalogue column separator or newline', description="""Handles column formatting for *CAT display. On a null byte
separator, advances the column counter modulo 4: prints a
2-space separator between columns, or a CR at column 0.
Called from fsreply_0_print_dir.""")


d.subroutine(0x8E45, 'load_handle_calc_offset', title='Load handle from &F0 and calculate workspace offset', description="""Loads the file handle byte from &F0, then falls through to
calc_handle_offset which converts handle * 12 to a workspace
byte offset. Validates offset < &48.""")
d.comment(0x8E58, 'Return after calculation', align=Align.INLINE)
d.comment(0x8E83, 'Outside our OSWORD range, exit', align=Align.INLINE)


d.subroutine(0x9072, 'enable_irq_and_tx', title='Enable interrupts and transmit via tx_poll_ff', description="""CLI to enable interrupts, then JMP tx_poll_ff. A short
tail-call wrapper used after building the TX control block.""")
d.comment(0x9115, 'Write &7F to RXCB (wait for reply)', align=Align.INLINE)
d.comment(0x9117, 'Poll RXCB for completion (bit7)', align=Align.INLINE)
d.comment(0x9190, 'V=1: use (net_rx_ptr) page', align=Align.INLINE)
d.comment(0x9192, 'V=1: skip to net_rx_ptr page', align=Align.INLINE)
d.comment(0x9194, 'V=0: use (nfs_workspace) page', align=Align.INLINE)
d.comment(0x91B9, 'SKIP (main only)', align=Align.INLINE)
d.comment(0x91BC, 'PAGE byte → Y=&11 (main only)', align=Align.INLINE)
d.comment(0x91BD, '→ Y=&12 (main only)', align=Align.INLINE)
d.comment(0x91BE, '→ Y=&13 (main only)', align=Align.INLINE)
d.comment(0x91BF, '→ Y=&14 (main only)', align=Align.INLINE)
d.comment(0x91C2, '→ Y=&17 (main only)', align=Align.INLINE)
d.comment(0x91DB, 'Store initial PFLAGS value', align=Align.INLINE)
d.comment(0x9214, 'XOR with current PFLAGS', align=Align.INLINE)
d.comment(0x9217, 'Test if sequence changed (bit 7 mismatch)', align=Align.INLINE)
d.comment(0x9218, 'Sequence unchanged: skip flush', align=Align.INLINE)
d.comment(0x921A, 'Undo ROR', align=Align.INLINE)
d.comment(0x921B, 'Store toggled PFLAGS', align=Align.INLINE)
d.comment(0x921E, 'Flush current output block', align=Align.INLINE)
d.comment(0x9221, 'Reload current PFLAGS', align=Align.INLINE)
d.comment(0x922C, 'Store recombined PFLAGS value', align=Align.INLINE)
d.comment(0x9248, 'Load current PFLAGS', align=Align.INLINE)
d.comment(0x924B, 'Save current PFLAGS', align=Align.INLINE)
d.comment(0x924C, 'Carry = current sequence (bit 7)', align=Align.INLINE)
d.comment(0x924D, 'Restore original PFLAGS', align=Align.INLINE)
d.comment(0x924E, 'Toggle sequence number (bit 7 of PFLAGS)', align=Align.INLINE)
d.comment(0x9250, 'Store toggled sequence number', align=Align.INLINE)
d.comment(0x9318, 'Return after storing result', align=Align.INLINE)
d.comment(0x9319, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.comment(0x931B, 'OSBYTE &C3: read screen start address', align=Align.INLINE)
d.comment(0x9660, 'Trampoline: forward to tx_begin', align=Align.INLINE)
d.comment(0x9663, 'Trampoline: forward to adlc_init', align=Align.INLINE)
d.comment(0x9666, 'Trampoline: forward to NMI release', align=Align.INLINE)
d.comment(0x9669, 'Trampoline: forward to NMI claim', align=Align.INLINE)
d.comment(0x966C, 'Trampoline: forward to IRQ handler', align=Align.INLINE)


d.subroutine(0x968D, 'init_nmi_workspace', title='Initialise NMI workspace (skip service request)', description="""Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
service request. Copies 32 bytes of NMI shim from ROM to
&0D00, patches the ROM bank number, sets init flags, reads
station ID, and re-enables NMIs.""")
d.comment(0x96B7, 'Load NMI vector low byte', align=Align.INLINE)
d.comment(0x96BA, 'Check if low byte is expected value', align=Align.INLINE)
d.comment(0x96BC, 'Mismatch: keep polling', align=Align.INLINE)
d.comment(0x96BE, 'Load NMI vector high byte', align=Align.INLINE)
d.comment(0x96C1, 'Check if high byte is &96', align=Align.INLINE)
d.comment(0x96C3, 'Mismatch: keep polling', align=Align.INLINE)
d.comment(0x96C5, 'BIT INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x96E9, 'Write CR1: RIE | TX_RESET', align=Align.INLINE)
d.comment(0x96EE, 'Write CR2: listen mode config', align=Align.INLINE)
d.comment(0x9707, 'Store broadcast flag in TX flags', align=Align.INLINE)
d.comment(0x970C, 'High byte of scout net handler', align=Align.INLINE)
d.comment(0x970E, 'Install next handler and RTI', align=Align.INLINE)
d.comment(0x9721, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x9724, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x972E, 'High byte of scout data handler', align=Align.INLINE)
d.comment(0x9730, 'Install scout data loop and RTI', align=Align.INLINE)
d.comment(0x9740, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x975F, 'Copied all 12 scout bytes?', align=Align.INLINE)
d.comment(0x9763, 'Save final buffer offset', align=Align.INLINE)

d.label(0x97A7, 'scan_nfs_port_list')
d.comment(0x97A7, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x97A9, 'A=0: no NFS workspace offset yet', align=Align.INLINE)
d.comment(0x97AB, 'Clear NFS workspace search flag', align=Align.INLINE)
d.comment(0x97B7, 'Y=1: advance to port byte in slot', align=Align.INLINE)
d.comment(0x97D5, 'CLC for 12-byte slot advance', align=Align.INLINE)
d.comment(0x97D6, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x97D8, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x97DA, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.comment(0x97DC, 'Check if NFS workspace already searched', align=Align.INLINE)
d.comment(0x97DE, 'Already searched: no match found', align=Align.INLINE)
d.comment(0x97E0, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x97E3, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x97E5, 'Get NFS workspace page number', align=Align.INLINE)
d.comment(0x97E7, 'Mark NFS workspace as search target', align=Align.INLINE)
d.comment(0x97E9, 'Y=0: start at offset 0 in workspace', align=Align.INLINE)
d.comment(0x97EB, 'Reset slot pointer to start', align=Align.INLINE)
d.comment(0x97EF, 'Check broadcast flag (bit 6)', align=Align.INLINE)
d.comment(0x97F2, 'Not broadcast: ACK and set up RX', align=Align.INLINE)
d.comment(0x97F4, 'Broadcast: copy scout fields directly', align=Align.INLINE)
d.comment(0x97F7, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x97F9, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x97FF, 'Transfer OK: send data ACK', align=Align.INLINE)
d.comment(0x981C, 'High byte of nmi_data_rx handler', align=Align.INLINE)
d.comment(0x9832, 'High byte of nmi_data_rx handler', align=Align.INLINE)


d.subroutine(0x9858, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects either the normal bulk RX handler (&9880) or the Tube
RX handler (&98DD) based on the Tube transfer flag in tx_flags,
and installs the appropriate NMI handler.""")


d.subroutine(0x9872, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")
d.comment(0x98E5, 'Advance Tube transfer byte count', align=Align.INLINE)
d.comment(0x98E7, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x98EA, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x98EC, 'Carry to transfer count byte 2', align=Align.INLINE)
d.comment(0x98EE, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x98F0, 'Carry to transfer count byte 3', align=Align.INLINE)
d.comment(0x98F2, 'No overflow: read second byte', align=Align.INLINE)
d.comment(0x98F4, 'Carry to transfer count byte 4', align=Align.INLINE)
d.comment(0x98F6, 'All bytes zero: overflow error', align=Align.INLINE)
d.comment(0x98F8, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x98FB, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x98FE, 'Advance count after second byte', align=Align.INLINE)
d.comment(0x9900, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x9902, 'Carry to count byte 2', align=Align.INLINE)
d.comment(0x9904, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x9906, 'Carry to count byte 3', align=Align.INLINE)
d.comment(0x9908, 'No overflow: check for more data', align=Align.INLINE)
d.comment(0x990A, 'Carry to count byte 4', align=Align.INLINE)
d.comment(0x990C, 'Zero: Tube transfer complete', align=Align.INLINE)
d.comment(0x990E, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x9911, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x9913, 'Return from NMI, wait for data', align=Align.INLINE)
d.comment(0x9988, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x998B, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x998E, 'bit7 set: start data TX phase', align=Align.INLINE)


d.subroutine(0x99A4, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")
d.comment(0x99DA, 'Restore X from stack', align=Align.INLINE)
d.comment(0x99DB, 'Transfer to X register', align=Align.INLINE)
d.comment(0x99DC, 'Y=8: RXCB buffer ptr offset', align=Align.INLINE)
d.comment(0x99DE, 'Load current RXCB buffer ptr lo', align=Align.INLINE)
d.comment(0x99E0, 'SEC for ADC #0 = add carry', align=Align.INLINE)
d.comment(0x99E1, 'Increment by 1 (Tube extra byte)', align=Align.INLINE)
d.comment(0x99E3, 'Store updated ptr back to RXCB', align=Align.INLINE)

d.label(0x99FC, 'add_buf_to_base')

d.label(0x9A07, 'store_rxcb_buf_ptr')
d.comment(0x9A33, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x9A38, 'A=&82: Tube release claim type', align=Align.INLINE)


d.subroutine(0x9A40, 'install_rx_scout_handler', title='Install RX scout NMI handler', description="""Installs nmi_rx_scout (&96F2) as the NMI handler via
set_nmi_vector, without first calling adlc_rx_listen.
Used when the ADLC is already in the correct RX mode.""")
d.comment(0x9A4E, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9A53, 'Jump to completion handler', align=Align.INLINE)
d.comment(0x9A71, 'Carry clear: operation permitted', align=Align.INLINE)
d.comment(0x9A73, 'Operation blocked by LSTAT mask', align=Align.INLINE)
d.comment(0x9A76, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x9A79, 'Look up handler address high byte', align=Align.INLINE)
d.comment(0x9A7C, 'Push handler address high', align=Align.INLINE)
d.comment(0x9A7D, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x9A80, 'Push handler address low', align=Align.INLINE)
d.comment(0x9A81, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0x9A82, 'Jump to discard handler', align=Align.INLINE)


d.subroutine(0x9AFC, 'imm_op_build_reply', title='Build immediate operation reply header', description="""Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")
d.comment(0x9BB8, 'Load current RX flags', align=Align.INLINE)
d.comment(0x9BBB, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x9BBD, 'Store updated flags', align=Align.INLINE)
d.comment(0x9BC0, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9BC1, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x9BC2, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9BC3, 'Transfer to X register', align=Align.INLINE)
d.comment(0x9BC4, 'A=0: success status', align=Align.INLINE)
d.comment(0x9BC6, 'Return with A=0 (success)', align=Align.INLINE)


d.subroutine(0x9BC7, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")
d.comment(0x9BF6, '(continued)', align=Align.INLINE)
d.comment(0x9BF7, '(continued)', align=Align.INLINE)
d.comment(0x9BF8, '(continued)', align=Align.INLINE)
d.comment(0x9BFF, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x9C00, '(continued)', align=Align.INLINE)
d.comment(0x9C01, '(continued)', align=Align.INLINE)
d.comment(0x9C02, '(continued)', align=Align.INLINE)
d.comment(0x9C03, '(continued)', align=Align.INLINE)

d.label(0x9C0E, 'check_imm_range')


d.subroutine(0x9C3A, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Mid-instruction label within the INACTIVE polling loop. The
address &9BE2 is referenced as a constant for self-modifying
code. Disables NMIs twice (belt-and-braces) then tests SR2
for INACTIVE before proceeding with TX.""")
d.comment(0x9C75, 'Pop saved register', align=Align.INLINE)
d.comment(0x9C76, 'Pop saved register', align=Align.INLINE)
d.comment(0x9CB2, 'Load handler from dispatch table', align=Align.INLINE)
d.comment(0x9CB5, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9CB6, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x9CB9, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9CBA, 'RTS dispatches to control-byte handler', align=Align.INLINE)
d.comment(0x9CCB, 'A=3: scout_status for PEEK', align=Align.INLINE)
d.comment(0x9CCF, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x9CE7, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x9CE9, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x9CEB, 'Restore processor flags', align=Align.INLINE)
d.comment(0x9CEC, 'Exit TX ctrl setup', align=Align.INLINE)
d.comment(0x9D3B, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x9D3C, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x9D3F, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x9D40, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x9D59, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x9D62, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x9D63, 'Increment delay counter', align=Align.INLINE)
d.comment(0x9D64, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x9D66, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x9D77, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x9D82, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x9D84, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x9D87, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x9D8E, 'High byte of nmi_reply_scout addr', align=Align.INLINE)
d.comment(0x9D90, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9DA4, 'High byte of nmi_reply_cont', align=Align.INLINE)
d.comment(0x9DA6, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9DB5, 'High byte of nmi_reply_validate', align=Align.INLINE)
d.comment(0x9DBF, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x9E70, 'bit7 clear: error path', align=Align.INLINE)
d.comment(0x9E72, 'ADLC reset and return to idle', align=Align.INLINE)
d.comment(0x9E75, 'Store result and return to idle', align=Align.INLINE)
d.comment(0x9E78, 'Load saved handler low byte', align=Align.INLINE)
d.comment(0x9ED7, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9ED9, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9EE8, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9EEF, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9F07, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x9F0A, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x9F0C, 'Install data RX handler', align=Align.INLINE)

d.label(0x9F1A, 'tx_result_fail')
d.comment(0x9F48, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x9F4D, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x9F57, '(continued)', align=Align.INLINE)
d.comment(0x9F58, '(continued)', align=Align.INLINE)
d.comment(0x9F59, '(continued)', align=Align.INLINE)
d.comment(0x9F61, '(continued)', align=Align.INLINE)
d.comment(0x9F62, '(continued)', align=Align.INLINE)
d.comment(0x9F6D, 'CLC for base pointer addition', align=Align.INLINE)
d.comment(0x9F6E, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x9F75, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x9F7D, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x9F82, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9F83, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x9FA7, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x9FC2, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x80B0, 'Test escape flag before FS reply', align=Align.INLINE)
d.comment(0x81AB, 'Return to MOS service handler', align=Align.INLINE)
d.comment(0x81AD, 'NOP padding for command table', align=Align.INLINE)
d.comment(0x81AE, 'NOP padding', align=Align.INLINE)
d.comment(0x81AF, 'NOP padding', align=Align.INLINE)
d.comment(0x81B0, 'NOP padding', align=Align.INLINE)
d.comment(0x8211, 'Load workspace page for printing', align=Align.INLINE)
d.comment(0x8240, 'Y=&14: offset for station number', align=Align.INLINE)
d.comment(0x8262, 'Load vector address from table', align=Align.INLINE)
d.comment(0x82C1, 'Store page as RX buffer high byte', align=Align.INLINE)
d.comment(0x82C3, 'Next page for NFS workspace', align=Align.INLINE)
d.comment(0x82C4, 'Store page as NFS workspace high', align=Align.INLINE)
d.comment(0x8382, 'Return with Z flag result', align=Align.INLINE)
d.comment(0x854D, 'Test escape flag (bit 7)', align=Align.INLINE)
d.comment(0x854F, 'Bit 7 clear: no escape, return', align=Align.INLINE)
d.comment(0x8551, 'A=&7E: acknowledge escape OSBYTE', align=Align.INLINE)
d.comment(0x851B, 'A=&2A: error ptr for FS send', align=Align.INLINE)
d.comment(0x861A, 'Continue printing next character', align=Align.INLINE)
d.comment(0x8622, 'Initialise accumulator to zero', align=Align.INLINE)
d.comment(0x87CA, 'Display save info (addr/len)', align=Align.INLINE)
d.comment(0x87CD, 'Load reply byte for transfer', align=Align.INLINE)
d.comment(0x8C1B, 'X=1: *EX single-entry examine', align=Align.INLINE)
d.comment(0x8C1D, 'A=3: column count for *EX mode', align=Align.INLINE)
d.comment(0x8C57, 'Load access level from reply', align=Align.INLINE)
d.comment(0x8C65, "ALWAYS branch past 'Owner'", align=Align.INLINE)
d.comment(0x8C8A, 'Load boot option from reply', align=Align.INLINE)
d.comment(0x8C96, 'Y=string offset for this option', align=Align.INLINE)
d.comment(0x8C99, 'Load next char of option name', align=Align.INLINE)
d.comment(0x8C9C, 'Bit 7 set: end of option name', align=Align.INLINE)
d.comment(0x8CAE, 'X=&11: Dir. name offset in reply', align=Align.INLINE)
d.comment(0x8CB0, 'Print directory name (10 chars)', align=Align.INLINE)
d.comment(0x8CB3, "Print '     Lib. ' header", align=Align.INLINE)
d.comment(0x8CC0, 'X=&1B: Lib. name offset in reply', align=Align.INLINE)
d.comment(0x8CE5, 'Zero entries: catalogue complete', align=Align.INLINE)
d.comment(0x8D07, 'Return from column separator', align=Align.INLINE)
d.comment(0x8DA3, 'More entries: skip final newline', align=Align.INLINE)
d.comment(0x8DA5, 'A=CR: print newline separator', align=Align.INLINE)
d.comment(0x8E59, 'Y=&6F: RX buffer handle offset', align=Align.INLINE)
d.comment(0x8E5B, 'Read handle from RX packet', align=Align.INLINE)
d.comment(0x8E5D, 'Valid handle: store and return', align=Align.INLINE)
d.comment(0x8EBA, 'Test TX semaphore (bit 7 to C)', align=Align.INLINE)
d.comment(0x8EBD, 'Save Y for return value', align=Align.INLINE)
d.comment(0x8EBE, 'C=0: TX busy, return error', align=Align.INLINE)
d.comment(0x8EF9, 'Sub-function >= 6?', align=Align.INLINE)
d.comment(0x8EFB, 'Yes: jump to sub 6-9 handler', align=Align.INLINE)
d.comment(0x8EFD, 'Sub-function >= 4?', align=Align.INLINE)
d.comment(0x9148, 'Y=14: max OSWORD parameter bytes', align=Align.INLINE)
d.comment(0x914A, 'OSWORD 7 = make a sound', align=Align.INLINE)
d.comment(0x96AE, 'BIT VULA: enable NMIs via latch', align=Align.INLINE)
d.comment(0x96B1, 'Return from NMI workspace init', align=Align.INLINE)
d.comment(0x96B2, 'Test Econet init complete flag', align=Align.INLINE)
d.comment(0x96B5, 'Init done: enter RX listen mode', align=Align.INLINE)
d.comment(0x97FC, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x9A30, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x9F3A, 'Load workspace byte at offset Y', align=Align.INLINE)
d.comment(0x9FE2, 'Shift high nibble to low', align=Align.INLINE)
d.comment(0x9FE3, 'Shift high nibble to low', align=Align.INLINE)
d.comment(0x9FE4, 'Shift high nibble to low', align=Align.INLINE)
d.comment(0x0414, 'A=5: Tube release request code', align=Align.INLINE)
d.comment(0x0416, 'Send release code via R4', align=Align.INLINE)
d.comment(0x0419, 'Load current Tube claim ID', align=Align.INLINE)
d.comment(0x041B, 'Send claim ID via R4', align=Align.INLINE)
d.comment(0x043E, 'Send transfer address byte', align=Align.INLINE)
d.comment(0x04A9, 'Load ROM header byte for TX', align=Align.INLINE)
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
d.comment(0x0520, 'Read channel handle from R2', align=Align.INLINE)
d.comment(0x052D, 'Read channel handle from R2', align=Align.INLINE)
d.comment(0x053B, 'Send carry+data byte to Tube R2', align=Align.INLINE)
d.comment(0x053E, 'ROL A: restore carry flag', align=Align.INLINE)
d.comment(0x0542, 'Read open mode from R2', align=Align.INLINE)
d.comment(0x055E, 'Read file handle from R2', align=Align.INLINE)
d.comment(0x0596, 'Read command string from R2', align=Align.INLINE)
d.comment(0x05A9, 'X=&10: 16 bytes for OSFILE CB', align=Align.INLINE)
d.comment(0x05F2, 'Read OSWORD number from R2', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'nfs-3.40.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'nfs-3.40.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
