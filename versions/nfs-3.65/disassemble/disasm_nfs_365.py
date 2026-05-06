import os
from pathlib import Path
import dasmos
from dasmos import Align
from dasmos.hooks import stringhi_hook
_script_dirpath = Path(__file__).resolve().parent
_version_dirpath = _script_dirpath.parent
_rom_filepath = os.environ.get('FANTASM_ROM', str(_version_dirpath / 'rom' / 'nfs-3.65.rom'))
_output_dirpath = Path(os.environ.get('FANTASM_OUTPUT_DIR', str(_version_dirpath / 'output')))
d = dasmos.Disassembler.create(cpu='6502', auto_label_data_prefix='l', auto_label_code_prefix='c', auto_label_subroutine_prefix='sub_c', auto_label_loop_prefix='loop_c')
d.load(_rom_filepath, 0x8000)
d.add_move(0x0016, 0x9324, 0x61)
d.add_move(0x0400, 0x9365, 0x100)
d.add_move(0x0500, 0x9465, 0x100)
d.add_move(0x0600, 0x9565, 0x100)

d.label(0x9324, 'reloc_zp_src')

d.label(0x9365, 'reloc_p4_src')

d.label(0x9465, 'reloc_p5_src')

d.label(0x9565, 'reloc_p6_src')
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
d.hook_subroutine(0x864A, 'print_inline', stringhi_hook)
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

d.label(0x00B7, 'fs_work_7')

d.label(0x00B8, 'fs_error_ptr')

d.label(0x00B9, 'fs_crflag')

d.label(0x00BA, 'fs_spool_handle')

d.label(0x00BB, 'fs_options')

d.label(0x00BC, 'fs_block_offset')

d.label(0x00BD, 'fs_last_byte_flag')

d.label(0x00BE, 'fs_crc_lo')

d.label(0x00BF, 'fs_crc_hi')

d.label(0x00C0, 'txcb_ctrl')

d.label(0x00C1, 'txcb_port')

d.label(0x00C2, 'txcb_dest')

d.label(0x00C4, 'txcb_start')

d.label(0x00C7, 'txcb_pos')

d.label(0x00C8, 'txcb_end')

d.label(0x00CD, 'nfs_temp')

d.label(0x00CE, 'rom_svc_num')

d.label(0x00CF, 'fs_spool0')

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

d.label(0x005F, 'zp_63')

d.label(0x00EF, 'osbyte_a_copy')

d.label(0x00F0, 'osword_pb_ptr')

d.label(0x00F1, 'osword_pb_ptr_hi')

d.label(0x00F3, 'os_text_ptr_hi')

d.label(0x00F7, 'osrdsc_ptr_hi')

d.label(0x00FD, 'brk_ptr')

d.label(0x00FF, 'escape_flag')

d.label(0x0100, 'error_block')

d.label(0x0101, 'error_text')

d.label(0x0102, 'stk_timeout_mid')

d.label(0x0103, 'stk_frame_3')

d.label(0x0104, 'stk_timeout_hi')

d.label(0x0106, 'stk_frame_p')

d.label(0x0128, 'tube_osword_pb')

d.label(0x0350, 'vdu_screen_mode')

d.label(0x0351, 'vdu_colours')

d.label(0x0355, 'vdu_cursor_edit')

d.label(0x0700, 'string_buf')

d.label(0x0CFF, 'nmi_code_base')

d.label(0x0D0C, 'nmi_jmp_lo')

d.label(0x0D0D, 'nmi_jmp_hi')

d.label(0x0D0E, 'set_nmi_vector')

d.label(0x0D11, 'install_nmi_handler')

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

d.label(0x0DE6, 'nmi_sub_table')

d.label(0x0DF0, 'rom_ws_table')

d.label(0x0DFE, 'fs_context_base')

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

d.label(0x0E0B, 'fs_context_hi')

d.label(0x0E0D, 'fs_reply_status')

d.label(0x0E0E, 'fs_target_stn')

d.label(0x0E10, 'fs_cmd_ptr')

d.label(0x0E16, 'fs_work_16')

d.label(0x0E30, 'fs_filename_buf')

d.label(0x0EF7, 'fs_reply_data')

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
d.entry(0x0016)
d.entry(0x0032)
d.entry(0x0036)
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

d.label(0x0403, 'tube_escape_entry')

d.label(0x0406, 'tube_addr_claim')

d.label(0x0414, 'tube_release_claim')

d.label(0x0428, 'addr_claim_external')

d.label(0x0471, 'tube_sendw_complete')

d.label(0x0435, 'tube_transfer_setup')

d.label(0x0421, 'tube_post_init')

d.label(0x0434, 'return_tube_init')

d.label(0x0483, 'return_tube_xfer')

d.label(0x0484, 'tube_begin')

d.label(0x04CB, 'tube_claim_default')

d.label(0x04D2, 'tube_init_reloc')
d.entry(0x0400)
d.entry(0x0403)
d.entry(0x0406)
d.entry(0x0421)
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
d.comment(0x043B, 'Send transfer type byte to co-processor', align=Align.INLINE)
d.comment(0x043E, 'X = transfer type for table lookup', align=Align.INLINE)
d.comment(0x043F, 'Y=3: send 4 bytes (address + claimed addr)', align=Align.INLINE)
d.comment(0x0441, 'Send our claimed address + 4-byte xfer addr', align=Align.INLINE)
d.comment(0x0446, 'Load transfer address byte from (X,Y)', align=Align.INLINE)
d.comment(0x0448, 'Send address byte to co-processor via R4', align=Align.INLINE)
d.comment(0x044B, 'Previous byte (big-endian: 3,2,1,0)', align=Align.INLINE)
d.comment(0x044C, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x044E, 'Y=&18: enable Tube control register', align=Align.INLINE)
d.comment(0x0450, 'Enable Tube interrupt generation', align=Align.INLINE)
d.comment(0x0453, 'Look up Tube control bits for this xfer type', align=Align.INLINE)
d.comment(0x0456, 'Apply transfer-specific control bits', align=Align.INLINE)
d.comment(0x0459, 'LSR: check bit 2 (2-byte flush needed?)', align=Align.INLINE)
d.comment(0x045A, 'LSR: shift bit 2 to carry', align=Align.INLINE)
d.comment(0x045B, 'C=0: no flush needed, skip R3 reads', align=Align.INLINE)
d.comment(0x045D, 'Dummy R3 reads: flush for 2-byte transfers', align=Align.INLINE)
d.comment(0x0460, 'Second dummy read to flush R3 FIFO', align=Align.INLINE)
d.comment(0x0463, 'Trigger co-processor ack via R4', align=Align.INLINE)
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

d.label(0x0518, 'tube_ctrl_values')

d.label(0x05A9, 'tube_osfile')

d.label(0x05D1, 'tube_osgbpb')

d.label(0x05F2, 'tube_osbyte_2param')
for addr in [0x0537, 0x0596, 0x05F2, 0x0607, 0x0627, 0x0668, 0x055E, 0x052D, 0x0520, 0x0542, 0x05A9, 0x05D1]:
    d.entry(addr)
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
d.comment(0x0523, 'Y=channel handle from R2', align=Align.INLINE)
d.comment(0x0524, 'Read data byte from R2 for BPUT', align=Align.INLINE)
d.comment(0x052A, 'BPUT done: send acknowledge, return', align=Align.INLINE)
d.comment(0x052D, 'Read channel handle from R2 for BGET', align=Align.INLINE)
d.comment(0x0530, 'Y=channel handle for OSBGET', align=Align.INLINE)
d.comment(0x0534, 'Send carry+byte reply (BGET result)', align=Align.INLINE)
d.comment(0x053A, 'ROR A: encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x053B, 'Send carry+data byte to Tube R2', align=Align.INLINE)
d.comment(0x053E, 'ROL A: restore carry flag', align=Align.INLINE)
d.comment(0x053F, 'Return via tube_reply_byte', align=Align.INLINE)
d.comment(0x0542, 'Read open mode from R2 for OSFIND', align=Align.INLINE)
d.comment(0x0545, 'A=0: close file, else open with filename', align=Align.INLINE)
d.comment(0x0547, 'Save open mode while reading filename', align=Align.INLINE)
d.comment(0x0548, 'Read filename string from R2 into &0700', align=Align.INLINE)
d.comment(0x054B, 'Recover open mode from stack', align=Align.INLINE)
d.comment(0x054F, 'Send file handle result to co-processor', align=Align.INLINE)
d.comment(0x0552, 'OSFIND close: read handle from R2', align=Align.INLINE)
d.comment(0x0555, 'Y=handle to close', align=Align.INLINE)
d.comment(0x0556, 'A=0: close command for OSFIND', align=Align.INLINE)
d.comment(0x055B, 'Close done: send acknowledge, return', align=Align.INLINE)
d.comment(0x055E, 'Read file handle from R2 for OSARGS', align=Align.INLINE)
d.comment(0x0561, 'Y=file handle for OSARGS', align=Align.INLINE)
d.comment(0x0562, 'Read 4-byte arg + reason from R2 into ZP', align=Align.INLINE)
d.comment(0x0564, 'Read next param byte from R2', align=Align.INLINE)
d.comment(0x0567, 'Params stored at &00-&03 (little-endian)', align=Align.INLINE)
d.comment(0x0569, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x056A, 'Loop for 4 bytes', align=Align.INLINE)
d.comment(0x056C, 'Read OSARGS reason code from R2', align=Align.INLINE)
d.comment(0x0572, 'Send result A back to co-processor', align=Align.INLINE)
d.comment(0x0575, 'Return 4-byte result from ZP &00-&03', align=Align.INLINE)
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
d.comment(0x0593, 'Y=7: set XY=&0700 for OSCLI/OSFIND', align=Align.INLINE)
d.comment(0x0595, 'Return with XY pointing to &0700', align=Align.INLINE)
d.comment(0x0596, 'Read command string from R2 into &0700', align=Align.INLINE)
d.comment(0x0599, 'Execute * command via OSCLI', align=Align.INLINE)
d.comment(0x059C, '&7F = success acknowledgement', align=Align.INLINE)
d.comment(0x059E, 'Poll R2 status until ready', align=Align.INLINE)
d.comment(0x05A1, 'Bit 6 clear: not ready, loop', align=Align.INLINE)
d.comment(0x05A3, 'Write byte to R2 data register', align=Align.INLINE)
d.comment(0x05A6, 'Return to Tube main loop', align=Align.INLINE)
d.comment(0x05A9, 'Read 16-byte OSFILE control block from R2', align=Align.INLINE)
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
d.comment(0x05C7, 'Load control block byte', align=Align.INLINE)
d.comment(0x05C9, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05CC, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05CD, 'Loop for all 16 bytes', align=Align.INLINE)
d.comment(0x05CF, 'ALWAYS branch to main loop', align=Align.INLINE)
d.comment(0x05D1, 'Read 13-byte OSGBPB control block from R2', align=Align.INLINE)
d.comment(0x05D3, 'Read next control block byte from R2', align=Align.INLINE)
d.comment(0x05D6, 'Store at &FF+X (descending into &00-&0C)', align=Align.INLINE)
d.comment(0x05D8, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05D9, 'Loop for all 13 bytes', align=Align.INLINE)
d.comment(0x05DB, 'Read OSGBPB reason code from R2', align=Align.INLINE)
d.comment(0x05DE, 'Y=0 for OSGBPB control block', align=Align.INLINE)
d.comment(0x05E3, 'Save A (completion status) for later', align=Align.INLINE)
d.comment(0x05E4, 'Return 13-byte result block to co-processor', align=Align.INLINE)
d.comment(0x05E6, 'Load result byte from zero page', align=Align.INLINE)
d.comment(0x05E8, 'Send byte to co-processor via R2', align=Align.INLINE)
d.comment(0x05EB, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x05EC, 'Loop for 13 bytes (X=12..0)', align=Align.INLINE)
d.comment(0x05EE, 'Recover completion status from stack', align=Align.INLINE)
d.comment(0x05EF, 'Send carry+status as RDCH-style reply', align=Align.INLINE)
d.comment(0x05F2, 'Read X param from R2 for 2-param OSBYTE', align=Align.INLINE)
d.comment(0x05F5, 'X = first parameter', align=Align.INLINE)
d.comment(0x05F6, 'Read A (OSBYTE number) from R2', align=Align.INLINE)
d.comment(0x05F9, 'Execute OSBYTE call', align=Align.INLINE)
d.comment(0x05FC, 'Poll R2 status for result send', align=Align.INLINE)
d.comment(0x05FF, 'BVC: page 5/6 boundary straddle', align=Align.INLINE)
d.comment(0x0600, 'Send carry+status to co-processor via R2', align=Align.INLINE)
d.comment(0x0615, 'Test for OSBYTE &9D (fast Tube BPUT)', align=Align.INLINE)
d.comment(0x0601, 'Send X result for 2-param OSBYTE', align=Align.INLINE)
d.comment(0x0607, 'Read X, Y, A from R2 for 3-param OSBYTE', align=Align.INLINE)
d.comment(0x0617, 'OSBYTE &9D (fast Tube BPUT): no result needed', align=Align.INLINE)
d.comment(0x0619, 'Encode carry (error flag) into bit 7', align=Align.INLINE)
d.comment(0x0622, 'Send Y result, then fall through to send X', align=Align.INLINE)
d.comment(0x0625, 'BVS &05FC: overlapping code — loops back to page 5 R2 poll to send X after Y', align=Align.INLINE)
d.comment(0x0627, 'Overlapping entry: &20 = JSR c06c5 (OSWORD)', align=Align.INLINE)
d.comment(0x0630, 'Read param block length from R2', align=Align.INLINE)
d.comment(0x0633, 'DEX: length 0 means no params to read', align=Align.INLINE)
d.comment(0x063E, 'Store param bytes into block at &0128', align=Align.INLINE)
d.comment(0x0644, 'Restore OSWORD number from Y', align=Align.INLINE)
d.comment(0x0645, 'XY=&0128: param block address for OSWORD', align=Align.INLINE)
d.comment(0x0651, 'Read result block length from R2', align=Align.INLINE)
d.comment(0x0655, 'No results to send: return to main loop', align=Align.INLINE)
d.comment(0x0657, 'Send result block bytes from &0128 via R2', align=Align.INLINE)
d.comment(0x0668, 'Read 5-byte OSWORD 0 control block from R2', align=Align.INLINE)
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

d.label(0x0625, 'tube_osbyte_short')

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

d.label(0x05FC, 'tube_poll_r2_result')

d.label(0x0600, 'tube_page6_start')

d.label(0x06C5, 'tube_read_r2')

d.label(0x0446, 'send_xfer_addr_bytes')

d.label(0x0466, 'poll_r4_copro_ack')

d.label(0x04AB, 'send_rom_page_bytes')

d.label(0x04E5, 'scan_copyright_end')

d.label(0x0564, 'read_osargs_params')

d.label(0x0577, 'send_osargs_result')

d.label(0x05C7, 'send_osfile_ctrl_blk')

d.label(0x05D3, 'read_osgbpb_ctrl_blk')

d.label(0x05E6, 'send_osgbpb_result')

d.label(0x064C, 'poll_r2_osword_result')

d.label(0x066A, 'read_rdln_ctrl_block')

d.label(0x0432, 'accept_new_claim')

d.label(0x0463, 'skip_r3_flush')

d.label(0x047A, 'copro_ack_nmi_check')

d.label(0x0482, 'skip_nmi_release')

d.label(0x048C, 'check_break_type')

d.label(0x0498, 'claim_addr_ff')

d.label(0x04A2, 'next_rom_page')

d.label(0x04C0, 'skip_addr_carry')

d.label(0x04FB, 'store_xfer_end_addr')

d.label(0x0593, 'string_buf_done')

d.label(0x0645, 'skip_param_read')
d.entry(0x0600)
d.entry(0x0625)
d.entry(0x0607)
d.entry(0x0627)
d.entry(0x0668)
d.entry(0x06A7)
d.entry(0x06AD)
d.entry(0x06BC)
d.comment(0x06CE, '&FF padding (29 bytes before trampolines)', align=Align.INLINE)

d.label(0x0DEB, 'fs_state_deb')
d.comment(0x800D, """The 'ROFF' suffix at &8014 is reused by the *ROFF
command matcher (svc_star_command) — a space-saving
trick that shares ROM bytes between the copyright
string and the star command table.""")

d.label(0x8001, 'language_handler_lo')

d.label(0x8002, 'language_handler_hi')

d.label(0x8004, 'service_handler_lo')

d.label(0x800D, 'copyright_string')

d.label(0x8014, 'error_offsets')

d.label(0x8021, 'dispatch_0_lo')

d.label(0x8046, 'dispatch_0_hi')
d.expr_label(0x8020, 'dispatch_0_lo-1')
d.expr_label(0x8045, 'dispatch_0_hi-1')

d.label(0x8EAA, 'fs_osword_tbl_lo')

d.label(0x8EC0, 'fs_osword_tbl_hi')

d.label(0x8E56, 'load_handle_calc_offset')

d.label(0x8EF4, 'read_args_size')

d.label(0x8F04, 'osword_12_dispatch')

d.label(0x8F1F, 'copy_param_workspace')

d.label(0x8FE9, 'store_16bit_at_y')

d.label(0x907F, 'enable_irq_and_tx')

d.label(0x909C, 'osword_trampoline')

d.label(0x90A7, 'osword_tbl_lo')

d.label(0x90B0, 'osword_tbl_hi')

d.label(0x90B9, 'net_write_char_handler')

d.label(0x9161, 'copy_params_rword')

d.label(0x921B, 'toggle_print_flag')

d.label(0x9157, 'remote_osword_handler')

d.label(0x913F, 'match_osbyte_code')

d.label(0x9147, 'return_match_osbyte')

d.label(0x9148, 'remote_osbyte_table')

d.label(0x848E, 'return_remote_cmd')
d.comment(0x848F, 'Read escape flag from MOS workspace', align=Align.INLINE)
d.comment(0x8491, 'Mask with escapable: bit 7 set if active', align=Align.INLINE)
d.comment(0x8493, 'No escape pending: return', align=Align.INLINE)
d.comment(0x8495, 'OSBYTE &7E: acknowledge escape condition', align=Align.INLINE)
d.comment(0x849A, 'Report escape error via error message table', align=Align.INLINE)

d.label(0x84A3, 'rchex')

d.label(0x918F, 'ctrl_block_setup_clv')

d.label(0x92F3, 'clear_jsr_protection')

d.label(0x930B, 'read_vdu_osbyte_x0')

d.label(0x930D, 'read_vdu_osbyte')

d.label(0x9321, 'vdu_osbyte_table')

d.label(0x0695, 'tube_send_r2')

d.label(0x069E, 'tube_send_r4')

d.label(0x80F2, 'return_1')

d.label(0x81A2, 'return_2')

d.label(0x82B0, 'return_3')

d.label(0x856D, 'return_4')

d.label(0x8D7F, 'return_5')

d.label(0x8E69, 'return_6')

d.label(0x8EBA, 'return_7')

d.label(0x8EBB, 'osword_handler_lo')

d.label(0x9073, 'return_8')

d.label(0x8D41, 'return_9')

d.label(0x8D42, 'option_name_offsets')

d.label(0x8D56, 'boot_string_offsets')

d.label(0x99B6, 'return_10')

d.label(0x807D, 'skip_cmd_spaces')

d.label(0x8094, 'got_station_num')

d.label(0x8099, 'skip_stn_parse')

d.label(0x809C, 'scan_for_colon')

d.label(0x80A9, 'read_remote_cmd_line')

d.label(0x80C1, 'prepare_cmd_dispatch')

d.label(0x80DF, 'svc_dispatch_range')

d.label(0x8106, 'set_adlc_disable')

d.label(0x810D, 'check_disable_flag')

d.label(0x8116, 'check_svc_high')

d.label(0x8127, 'poll_tube_ready')

d.label(0x8174, 'tube_chars_done')

d.label(0x8176, 'check_svc_12')

d.label(0x8182, 'not_svc_12_nfs')

d.label(0x8186, 'do_svc_dispatch')

d.label(0x8184, 'svc_unhandled_return')

d.label(0x81A3, 'svc_4_star_command')

d.label(0x81D1, 'skip_kbd_reenable')

d.label(0x81D8, 'match_net_cmd')

d.label(0x8203, 'restore_ws_return')

d.label(0x06EB, 'trampoline_tx_setup')

d.label(0x06EE, 'trampoline_adlc_init')

d.label(0x06F1, 'svc_12_nmi_release')

d.label(0x06F4, 'svc_11_nmi_claim')

d.label(0x9650, 'start_adlc_tx')

d.label(0x9653, 'init_adlc_hw')

d.label(0x9656, 'econet_save')

d.label(0x9659, 'econet_restore')

d.label(0x965C, 'svc5_irq_check')

d.label(0x9699, 'svc_5_unknown_irq')
d.entry(0x06EB)
d.entry(0x06EE)

d.label(0x824D, 'skip_no_clock_msg')

d.label(0x8304, 'read_station_id')

d.label(0x8551, 'bgetv_handler')

d.label(0x8567, 'bgetv_shared_jsr')

d.label(0x8568, 'error_table_base')

d.label(0x8401, 'bputv_handler')
d.entry(0x8551)
d.entry(0x8401)
d.entry(0x86CC)
d.entry(0x86FA)

d.label(0x81CF, 'cmd_name_matched')

d.label(0x8352, 'match_cmd_chars')

d.label(0x8365, 'check_rom_end')

d.label(0x8327, 'store_rom_ptr_pair')

d.label(0x836B, 'skip_space_next')

d.label(0x836C, 'skip_spaces')

d.label(0x8375, 'init_tx_reply_port')

d.label(0x83B6, 'init_tx_ctrl_data')

d.label(0x8377, 'init_tx_ctrl_port')

d.label(0x83BC, 'store_fs_hdr_clc')

d.label(0x83BD, 'store_fs_hdr_fn')

d.label(0x83C2, 'copy_dir_handles')

d.label(0x83AB, 'prepare_cmd_clv')

d.label(0x83F3, 'check_fs_error')

d.label(0x83B6, 'prepare_fs_cmd_v')

d.label(0x83E1, 'send_fs_reply_cmd')

d.label(0x845B, 'close_spool_exec')

d.label(0x8461, 'dispatch_fs_error')

d.label(0x8475, 'error_code_clamped')

d.label(0x8477, 'copy_error_to_brk')

d.label(0x84D2, 'zero_exec_header')

d.label(0x84D8, 'execute_downloaded')

d.label(0x8402, 'bgetv_entry')

d.label(0x848F, 'check_escape')

d.label(0x842F, 'store_retry_count')

d.label(0x8486, 'update_sequence_return')
d.comment(0x8486, 'Save updated sequence number', align=Align.INLINE)
d.comment(0x8489, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x848B, 'Restore X from stack', align=Align.INLINE)
d.comment(0x848D, 'Restore A from stack', align=Align.INLINE)
d.comment(0x848E, 'Return to caller', align=Align.INLINE)

d.label(0x850B, 'copy_error_message')

d.label(0x84FA, 'error_not_listening')

d.label(0x8502, 'set_listen_offset')
d.comment(0x84FA, 'Error code 8: "Not listening" error', align=Align.INLINE)
d.comment(0x84FC, 'ALWAYS branch to set_listen_offset', align=Align.INLINE)
d.comment(0x84FE, 'Load TX status byte for error lookup', align=Align.INLINE)
d.comment(0x8500, 'Mask to 3-bit error code (0-7)', align=Align.INLINE)
d.comment(0x8502, 'X = error code index', align=Align.INLINE)
d.comment(0x8503, 'Look up error message offset from table', align=Align.INLINE)
d.comment(0x8506, 'X=0: start writing at &0101', align=Align.INLINE)
d.comment(0x8508, 'Store BRK opcode at &0100', align=Align.INLINE)
d.comment(0x850B, 'Load error message byte', align=Align.INLINE)
d.comment(0x850E, 'Build error message at &0101+', align=Align.INLINE)
d.comment(0x8511, 'Zero byte = end of message; go execute BRK', align=Align.INLINE)
d.comment(0x8513, 'Next source byte', align=Align.INLINE)
d.comment(0x8514, 'Next dest byte', align=Align.INLINE)
d.comment(0x8515, 'Continue copying message', align=Align.INLINE)
d.comment(0x8517, '"SP." remote spool command string', align=Align.INLINE)
d.comment(0x851A, 'CR + "E." + CR remote exec strings', align=Align.INLINE)
d.comment(0x851E, "A = '*' for FS command prefix", align=Align.INLINE)

d.label(0x85CF, 'map_attrib_bits')

d.label(0x85D7, 'skip_set_attrib_bit')

d.label(0x85FB, 'poll_tx_semaphore')

d.label(0x85F8, 'rearm_tx_attempt')

d.label(0x8625, 'tx_retry_delay')

d.label(0x862D, 'tx_abort')

d.label(0x8631, 'tx_success_exit')

d.label(0x8652, 'print_inline_char')

d.label(0x8658, 'print_next_char')

d.label(0x8662, 'jump_via_addr')

d.label(0x8669, 'scan_decimal_digit')

d.label(0x8684, 'no_dot_exit')

d.label(0x8685, 'parse_decimal_rts')

d.label(0x86A1, 'handle_mask_exit')

d.label(0x86AF, 'compare_addr_byte')

d.label(0x851E, 'waitfs')

d.label(0x8521, 'send_to_fs_star')

d.label(0x852E, 'skip_rx_flag_set')

d.label(0x8547, 'fs_wait_cleanup')

d.label(0x8829, 'add_5_to_y')

d.label(0x882A, 'add_4_to_y')

d.label(0x883C, 'sub_4_from_y')

d.label(0x883D, 'sub_3_from_y')

d.label(0x81C0, 'clear_osbyte_ce_cf')

d.label(0x81C4, 'clear_osbyte_masks')

d.label(0x0F00, 'fs_cmd_type')

d.label(0x0F01, 'fs_cmd_y_param')

d.label(0x0F02, 'fs_cmd_urd')

d.label(0x0F03, 'fs_cmd_csd')

d.label(0x0F04, 'fs_cmd_lib')

d.label(0x0F05, 'fs_cmd_data')

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

d.label(0x0FDC, 'fs_putb_buf')

d.label(0x0FDD, 'fs_getb_buf')

d.label(0x0FDE, 'fs_handle_mask')

d.label(0x0FDF, 'fs_error_flags')

d.label(0x0FE0, 'fs_error_buf')

d.label(0x85CB, 'attrib_shift_bits')

d.label(0x85DA, 'access_bit_table')

d.label(0x8DCA, 'print_hex_byte')

d.label(0x8DD5, 'print_hex_nibble')

d.label(0x86B8, 'return_compare')

d.label(0x86B9, 'fscv_7_read_handles')

d.label(0x86BD, 'return_fscv_handles')

d.label(0x86C8, 'store_fs_flag')

d.label(0x86CC, 'copy_filename_ptr')

d.label(0x86D8, 'parse_filename_gs_y')

d.label(0x86EB, 'terminate_filename')

d.label(0x8645, 'clear_escapable')

d.label(0x8D5E, 'print_hex_bytes')

d.label(0x8D69, 'print_space')

d.label(0x85EF, 'tx_poll_timeout')

d.label(0x872E, 'skip_lodfil')

d.label(0x8730, 'copy_load_end_addr')

d.label(0x875C, 'send_block_loop')

d.label(0x875E, 'copy_block_addrs')

d.label(0x87A5, 'copy_save_params')

d.label(0x87C6, 'save_csd_display')

d.label(0x87DD, 'print_filename_char')

d.label(0x87E9, 'pad_filename_space')

d.label(0x87F1, 'print_addresses')

d.label(0x8805, 'skip_catalogue_msg')

d.label(0x8810, 'copy_attribs_reply')

d.label(0x8847, 'transfer_loop_top')

d.label(0x8857, 'setup_block_addrs')

d.label(0x8875, 'clamp_dest_addr')

d.label(0x887C, 'send_block')

d.label(0x88BB, 'restore_ay_return')

d.label(0x897C, 'copy_fileptr_reply')

d.label(0x898B, 'copy_fileptr_to_cmd')

d.label(0x8985, 'argsv_check_return')

d.label(0x89A3, 'restore_xy_return')

d.label(0x89A8, 'argsv_fs_query')

d.label(0x89B3, 'halve_args_a')

d.label(0x890A, 'send_fs_cmd_v1')

d.label(0x8910, 'check_attrib_result')

d.label(0x8954, 'attrib_error_exit')

d.label(0x88E9, 'get_file_protection')

d.label(0x88FE, 'copy_filename_to_cmd')

d.label(0x893B, 'copy_fs_reply_to_cb')

d.label(0x89C2, 'return_a_zero')

d.label(0x8987, 'save_args_handle')

d.label(0x8A18, 'close_opt_return')

d.label(0x8A24, 'check_opt1')

d.label(0x8A27, 'set_messages_flag')

d.label(0x8A3E, 'opt_return')

d.label(0x8A08, 'close_single_handle')

d.label(0x8A4A, 'adjust_addr_byte')

d.label(0x8A56, 'subtract_adjust')

d.label(0x8A6B, 'gbpb_invalid_exit')

d.label(0x8A40, 'adjust_addrs_9')

d.label(0x8A45, 'adjust_addrs_1')

d.label(0x8A47, 'adjust_addrs_clc')

d.label(0x8B0A, 'get_disc_title')

d.label(0x8AA7, 'gbpb_write_path')

d.label(0x8AE6, 'gbpb_read_path')

d.label(0x8AE9, 'wait_fs_reply')

d.label(0x8AF6, 'skip_clear_flag')

d.label(0x8B2D, 'store_tube_flag')

d.label(0x8B41, 'gbpb6_read_name')

d.label(0x8B6D, 'copy_reply_to_caller')

d.label(0x8B82, 'tube_transfer')

d.label(0x8B8F, 'no_page_wrap')

d.label(0x8BA9, 'gbpb_done')

d.label(0x8BAC, 'gbpb8_read_dir')

d.label(0x8BE8, 'skip_copy_reply')

d.label(0x8B75, 'copy_reply_bytes')

d.label(0x8B9D, 'wait_tube_delay')

d.label(0x8BEA, 'zero_cmd_bytes')

d.label(0x8C01, 'tube_claim_loop')

d.label(0x8C12, 'scan_cmd_table')

d.label(0x8C33, 'dispatch_cmd')

d.label(0x8C60, 'init_cat_params')

d.label(0x8C9E, 'print_public')

d.label(0x8CA8, 'print_user_env')

d.label(0x8CD0, 'print_option_name')

d.label(0x8CDB, 'done_option_name')

d.label(0x8CFF, 'fetch_dir_batch')

d.label(0x8D21, 'process_entries')

d.label(0x8D22, 'scan_entry_terminator')

d.label(0x8D35, 'print_reply_bytes')

d.label(0x8D37, 'print_reply_counted')

d.label(0x8D74, 'copy_string_from_offset')

d.label(0x8DA0, 'print_cr')

d.label(0x8DA2, 'print_newline')

d.label(0x8DA5, 'next_dir_entry')

d.label(0x8DBE, 'divide_subtract')

d.label(0x8DC7, 'print_digit')

d.label(0x8DEB, 'skip_gs_filename')

d.label(0x8D8D, 'cat_column_separator')

d.label(0x8E2C, 'exec_local')

d.label(0x8E46, 'copy_handles_loop')

d.label(0x8E38, 'jmp_restore_args')

d.label(0x8E7D, 'store_handle_return')

d.label(0x8E99, 'copy_param_ptr')

d.label(0x8F40, 'read_local_station_id')

d.label(0x8F5A, 'copy_handles_to_ws')

d.label(0x8FBF, 'copy_rxcb_to_param')

d.label(0x8F14, 'set_workspace_page')

d.label(0x8F25, 'skip_param_write')

d.label(0x8F6C, 'return_last_error')

d.label(0x8FA9, 'read_rxcb')

d.label(0x8FD4, 'reenable_rx')

d.label(0x9001, 'store_txcb_byte')

d.label(0x9018, 'copy_fs_addr')

d.label(0x9058, 'send_data_bytes')

d.label(0x906B, 'delay_between_tx')

d.label(0x9041, 'handle_tx_result')

d.label(0x9104, 'dispatch_remote_osbyte')

d.label(0x9126, 'poll_rxcb_flag')

d.label(0x9165, 'copy_osword_params')

d.label(0x922D, 'skip_flush')

d.label(0x92C5, 'save_palette_entry')

d.label(0x96B8, 'init_nmi_workspace')

d.label(0x9692, 'dispatch_svc5')

d.label(0x96BA, 'copy_nmi_shim')

d.label(0x970A, 'scout_reject')

d.label(0x972B, 'scout_discard')

d.label(0x9733, 'scout_loop_rda')

d.label(0x9743, 'scout_loop_second')

d.label(0x977E, 'scout_no_match')

d.label(0x9781, 'scout_match_port')

d.label(0x96F7, 'accept_frame')

d.label(0x9712, 'accept_local_net')

d.label(0x9715, 'accept_scout_net')

d.label(0x978B, 'scan_port_list')

d.label(0x9794, 'scan_nfs_port_list')

d.label(0x9798, 'check_port_slot')

d.label(0x97AC, 'check_station_filter')

d.label(0x97BE, 'next_port_slot')

d.label(0x97CB, 'discard_no_match')

d.label(0x97CE, 'try_nfs_port_list')

d.label(0x97D9, 'port_match_found')

d.label(0x97EB, 'send_data_rx_ack')

d.label(0x97FC, 'data_rx_setup')

d.label(0x981C, 'nmi_data_rx_net')

d.label(0x9832, 'nmi_data_rx_skip')

d.label(0x983D, 'install_data_rx_handler')

d.label(0x9850, 'install_tube_rx')

d.label(0x9857, 'nmi_error_dispatch')

d.label(0x985F, 'rx_error')

d.label(0x985F, 'rx_error_reset')

d.label(0x98C2, 'nmi_data_rx_tube')

d.label(0x986A, 'data_rx_loop')

d.label(0x987A, 'read_sr2_between_pairs')

d.label(0x9881, 'read_second_rx_byte')

d.label(0x9891, 'check_sr2_loop_again')

d.label(0x98B0, 'read_last_rx_byte')

d.label(0x98BF, 'send_ack')

d.label(0x98C5, 'rx_tube_data')

d.label(0x98E5, 'data_rx_tube_complete')

d.label(0x98E2, 'data_rx_tube_error')

d.label(0x991B, 'ack_tx_configure')

d.label(0x9929, 'ack_tx_write_dest')

d.label(0x996A, 'start_data_tx')

d.label(0x996D, 'dispatch_nmi_error')

d.label(0x9970, 'advance_rx_buffer_ptr')

d.label(0x997B, 'add_rxcb_ptr')

d.label(0x99A9, 'inc_rxcb_ptr')

d.label(0x99B4, 'skip_tube_update')

d.label(0x99D4, 'store_buf_ptr_lo')

d.label(0x99DD, 'skip_buf_ptr_update')

d.label(0x99C6, 'rx_complete_update_rxcb')

d.label(0x9A0D, 'install_rx_scout_handler')

d.label(0x9A14, 'copy_scout_to_buffer')

d.label(0x9A21, 'copy_scout_bytes')
d.expr_label(0x9A1A, 'imm_op_dispatch_lo-&81')

d.label(0x9A4D, 'release_tube')

d.label(0x9A2F, 'next_scout_byte')

d.label(0x9A36, 'scout_copy_done')

d.label(0x9A3B, 'copy_scout_via_tube')

d.label(0x9A56, 'clear_release_flag')

d.label(0x9A59, 'inc_buf_counter_32')

d.label(0x9A90, 'scout_page_overflow')

d.label(0x9A92, 'check_scout_done')

d.label(0x9A7F, 'rotate_prot_mask')

d.label(0x9A85, 'dispatch_imm_op')

d.label(0x9A98, 'imm_op_out_of_range')

d.label(0x9B09, 'imm_op_build_reply')

d.label(0x9BBC, 'calc_peek_poke_size')

d.label(0x9BDD, 'copy_imm_params')

d.label(0x9BA8, 'tx_imm_op_setup')

d.label(0x9BD3, 'tx_ctrl_range_check')

d.label(0x9BE7, 'tx_line_idle_check')

d.label(0x9B90, 'tx_begin')

d.label(0x9BFF, 'test_inactive_retry')

d.label(0x9C06, 'intoff_test_inactive')

d.label(0x9C24, 'inactive_retry')

d.label(0x9C3A, 'tx_active_start')

d.label(0x9CE3, 'setup_unicast_xfer')

d.label(0x9C4A, 'tx_no_clock_error')

d.label(0x9C4C, 'store_tx_error')

d.label(0x9CC1, 'setup_data_xfer')

d.label(0x9CD7, 'copy_bcast_addr')

d.label(0x9D05, 'tx_fifo_write')

d.label(0x9D33, 'delay_nmi_disable')

d.label(0x9D25, 'tx_error')

d.label(0x9D29, 'tx_fifo_not_ready')

d.label(0x9D30, 'tx_store_error')

d.label(0x9D54, 'check_handshake_bit')

d.label(0x9D5E, 'install_reply_scout')

d.label(0x9D8B, 'reject_reply')

d.label(0x9DE6, 'data_tx_begin')

d.label(0x9DF4, 'install_imm_data_nmi')

d.label(0x9E00, 'data_tx_check_fifo')

d.label(0x9E10, 'write_second_tx_byte')

d.label(0x9E20, 'check_irq_loop')

d.label(0x9E28, 'data_tx_last')

d.label(0x9E39, 'data_tx_error')

d.label(0x9E39, 'install_saved_handler')

d.label(0x9E42, 'nmi_data_tx_tube')

d.label(0x9E45, 'tube_tx_fifo_write')

d.label(0x9E5D, 'write_second_tube_byte')

d.label(0x9E73, 'check_tube_irq_loop')

d.label(0x9E7B, 'tx_tdra_error')

d.label(0x9E6B, 'tube_tx_inc_byte3')

d.label(0x9E6C, 'tube_tx_inc_operand')

d.label(0x9E74, 'tube_tx_sr1_operand')

d.label(0x9EA3, 'nmi_final_ack_net')

d.label(0x9ED4, 'check_fv_final_ack')

d.label(0x9F19, 'calc_transfer_size')

d.label(0x9F49, 'restore_x_and_return')

d.label(0x9F4C, 'fallback_calc_transfer')

d.label(0x9EDF, 'tx_result_fail')

d.label(0x9F8F, 'poll_nmi_idle')

d.label(0x9F8A, 'wait_idle_and_reset')

d.label(0x9FAF, 'reset_enter_listen')

d.label(0x9FB1, 'listen_jmp_hi')

d.label(0x9F6F, 'nmi_shim_rom_src')

d.label(0x0586, 'strnh')

d.label(0x05A6, 'mj')

d.label(0x05AB, 'argsw')

d.label(0x0604, 'bytex')

d.label(0x8152, 'cloop')

d.label(0x816C, 'copy_nmi_workspace')

d.label(0x81EA, 'initl')

d.label(0x81D5, 'skpspi')

d.label(0x823E, 'dofsl1')

d.label(0x8288, 'fs_dispatch_addrs')

d.label(0x8254, 'copy_fs_vectors')

d.label(0x82F5, 'init_rxcb_entries')

d.label(0x8341, 'fsdiel')

d.label(0x8386, 'fstxl1')

d.label(0x8396, 'fstxl2')

d.label(0x83A1, 'tx_ctrl_upper')

d.label(0x83E9, 'dofsl7')

d.label(0x83F5, 'return_dofsl7')

d.label(0x83F6, 'dofsl5')

d.label(0x8440, 'error1')

d.label(0x84FE, 'nlistn')

d.label(0x8500, 'nlisne')

d.label(0x8534, 'incpx')

d.label(0x8692, 'y2fsl5')

d.label(0x8698, 'y2fsl2')

d.label(0x86A7, 'fs2al1')

d.label(0x8D60, 'num01')

d.label(0x860B, 'poll_tx_complete')

d.label(0x86CE, 'file1')

d.label(0x86E0, 'quote1')

d.label(0x870B, 'loadop')

d.label(0x8728, 'lodfil')

d.label(0x8748, 'floop')

d.label(0x8772, 'lodchk')

d.label(0x877D, 'return_lodchk')

d.label(0x877E, 'saveop')

d.label(0x8787, 'savsiz')

d.label(0x881F, 'lodrl1')

d.label(0x8832, 'lodrl2')

d.label(0x8867, 'savchk')

d.label(0x88DC, 'chalp1')

d.label(0x88F3, 'chalp2')

d.label(0x8905, 'cha6')

d.label(0x8914, 'cha4')

d.label(0x891E, 'cha5')

d.label(0x8948, 'cha5lp')

d.label(0x89B6, 'osarg1')

d.label(0x8A2C, 'opter1')

d.label(0x8A31, 'optl1')

d.label(0x8A59, 'gbpbx')

d.label(0x8A90, 'gbpbx0')

d.label(0x8A6E, 'gbpbx1')

d.label(0x8A79, 'gbpbe1')

d.label(0x8A85, 'gbpbf1')

d.label(0x8A90, 'gbpbf2')

d.label(0x8A99, 'gbpbl1')

d.label(0x8ABB, 'gbpbl3')

d.label(0x8AD2, 'gbpbf3')

d.label(0x8B2F, 'info2')

d.label(0x8B94, 'tbcop1')

d.label(0x8C14, 'decfir')

d.label(0x8C16, 'decmor')

d.label(0x8C22, 'decmin')

d.label(0x8C3A, 'cmd_match_data')

d.label(0x8E40, 'logon2')

d.label(0x8F2D, 'logon3')

d.label(0x8D86, 'print_dir_from_offset')

d.label(0x8D70, 'infol2')

d.label(0x8E7B, 'rxpol2')

d.label(0x8EAD, 'save1')

d.label(0x8EFF, 'readry')

d.label(0x8F02, 'osword_12_offsets')

d.label(0x8F2E, 'rssl1')

d.label(0x8F39, 'rssl2')

d.label(0x8F49, 'rsl1')

d.label(0x8F73, 'readc1')

d.label(0x8F90, 'scan0')

d.label(0x8FA4, 'scan1')

d.label(0x8FC0, 'openl6')

d.label(0x8FCD, 'openl7')

d.label(0x8FD2, 'openl4')

d.label(0x8FF9, 'dofs01')

d.label(0x9074, 'dofs2')

d.label(0x9095, 'entry1')

d.label(0x910D, 'nbyte6')

d.label(0x910F, 'nbyte1')

d.label(0x9133, 'nbyte4')

d.label(0x9137, 'nbyte5')

d.label(0x913E, 'return_nbyte')

d.label(0x84A6, 'remot1')

d.label(0x9190, 'cbset2')

d.label(0x91A7, 'cbset3')

d.label(0x91AD, 'cbset4')

d.label(0x91AF, 'cb_template_main_start')

d.label(0x91B3, 'cb_template_tail')

d.label(0x91EA, 'setup1')

d.label(0x91EC, 'return_printer_select')

d.label(0x91FC, 'prlp1')

d.label(0x9275, 'bsxl1')

d.label(0x9292, 'bspsx')

d.label(0x929A, 'bsxl0')

d.label(0x92AD, 'return_bspsx')
d.comment(0x8000, """NFS ROM 3.65 disassembly (Acorn Econet filing system)
====================================================""")
d.comment(0x8000, 'JMP language_handler', align=Align.INLINE)
d.comment(0x8003, 'JMP service_handler', align=Align.INLINE)
d.comment(0x8006, 'ROM type: service + language', align=Align.INLINE)
d.comment(0x8007, 'Copyright string offset from &8000', align=Align.INLINE)
d.comment(0x8008, 'Binary version number', align=Align.INLINE)
d.comment(0x8009, 'ROM title string "NET"', align=Align.INLINE)
d.comment(0x800C, 'Null terminator before copyright', align=Align.INLINE)
d.comment(0x800D, 'Copyright string "(C)ROFF"', align=Align.INLINE)
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
d.comment(0x8018, '"Escape"', align=Align.INLINE)
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
for i in range(0, 14):
    d.rts_code_ptr(0x8021 + i, 0x8046 + i)
for i in range(14, 19):
    d.rts_code_ptr(0x8021 + i, 0x8046 + i)
for i in range(19, 27):
    d.rts_code_ptr(0x8021 + i, 0x8046 + i)
for i in range(27, 31):
    d.rts_code_ptr(0x8021 + i, 0x8046 + i)
for i in range(31, 37):
    d.rts_code_ptr(0x8021 + i, 0x8046 + i)
for i in range(5):
    d.rts_code_ptr(0x8EBB + i, 0x8EC0 + i)
d.entry(0x96D9)
d.entry(0x96DF)
d.entry(0x9BF8)
d.entry(0x9CFF)
d.entry(0x9D25)
d.entry(0x9D3B)
d.entry(0x9D47)
d.entry(0x9D63)
d.entry(0x9D77)
d.entry(0x9D8E)
d.entry(0x9E83)
d.entry(0x9E8F)
d.entry(0x9EA3)
d.entry(0x9EDB)
d.entry(0x9EE1)
d.entry(0x9EB7)
d.entry(0x96FC)
d.entry(0x972E)
d.entry(0x9808)
d.entry(0x981C)
d.entry(0x9832)
d.entry(0x9865)
d.entry(0x98C2)
d.entry(0x9947)
d.entry(0x9F4C)
d.entry(0x9FB2)
d.entry(0x9FC0)
d.entry(0x9DD6)
d.entry(0x9DFB)
d.entry(0x9E42)
d.entry(0x821A)
d.entry(0x8239)
d.entry(0x823B)
d.entry(0x8272)
d.entry(0x835F)
d.entry(0x86B9)
d.entry(0x8D2E)
d.entry(0x8DDF)
d.entry(0x8E6A)
d.entry(0x9318)
d.entry(0x9659)
d.entry(0x9699)
d.entry(0x99B7)
d.entry(0x9B09)
d.entry(0x06F7)
d.entry(0x8829)
d.entry(0x883C)
d.entry(0x8841)
d.entry(0x88BF)
d.entry(0x89AE)
d.entry(0x8A60)
d.entry(0x90EB)
d.entry(0x9991)
d.entry(0x8FF3)
d.entry(0x909C)
for i in range(9):
    d.rts_code_ptr(0x90A7 + i, 0x90B0 + i)

d.label(0x9A67, 'return_inc_port_buf')

d.label(0x9AB5, 'copy_addr_loop')

d.label(0x9ABF, 'svc5_dispatch_lo')

d.label(0x9A9B, 'imm_op_dispatch_lo')
for addr in range(0x9A9B, 0x9AA3):
    d.byte(addr)
d.expr(0x9A9B, '<(rx_imm_peek-1)')
d.expr(0x9A9C, '<(rx_imm_poke-1)')
d.expr(0x9A9D, '<(rx_imm_exec-1)')
d.expr(0x9A9E, '<(rx_imm_exec-1)')
d.expr(0x9A9F, '<(rx_imm_exec-1)')
d.expr(0x9AA0, '<(rx_imm_halt_cont-1)')
d.expr(0x9AA1, '<(rx_imm_halt_cont-1)')
d.expr(0x9AA2, '<(rx_imm_machine_type-1)')
d.comment(0x9A9B, 'Ctrl &81: PEEK', align=Align.INLINE)
d.comment(0x9A9C, 'Ctrl &82: POKE', align=Align.INLINE)
d.comment(0x9A9D, 'Ctrl &83: JSR', align=Align.INLINE)
d.comment(0x9A9E, 'Ctrl &84: UserProc', align=Align.INLINE)
d.comment(0x9A9F, 'Ctrl &85: OSProc', align=Align.INLINE)
d.comment(0x9AA0, 'Ctrl &86: HALT', align=Align.INLINE)
d.comment(0x9AA1, 'Ctrl &87: CONTINUE', align=Align.INLINE)
d.comment(0x9AA2, 'Ctrl &88: machine type query', align=Align.INLINE)


d.subroutine(0x9AA3, 'rx_imm_exec', title='RX immediate: JSR/UserProc/OSProc setup', description="""Sets up the port buffer to receive remote procedure data.
Copies the 4-byte remote address from rx_remote_addr into
the execution address workspace at &0D58, then jumps to
the common receive path at c9826. Used for operation types
&83 (JSR), &84 (UserProc), and &85 (OSProc).""")


d.subroutine(0x9AC1, 'rx_imm_poke', title='RX immediate: POKE setup', description="""Sets up workspace offsets for receiving POKE data.
port_ws_offset=&3D, rx_buf_offset=&0D, then jumps to
the common data-receive path at port_match_found.""")


d.subroutine(0x9ACC, 'rx_imm_machine_type', title='RX immediate: machine type query', description="""Sets up a reply buffer (open_port_buf=&21, page &7F,
length &01FC) for the machine type query response, then
branches to set_tx_reply_flag. Returns system identification
data to the remote station.""")


d.subroutine(0x9ADE, 'rx_imm_peek', title='RX immediate: PEEK setup', description="""Writes &0D3D to port_ws_offset/rx_buf_offset, sets
scout_status=2, then calls tx_calc_transfer to send the
PEEK response data back to the requesting station.
Uses workspace offsets (&A6/&A7) for nmi_tx_block.""")


d.subroutine(0x9B47, 'tx_done_jsr', title='TX done: remote JSR execution', description="""Pushes tx_done_exit-1 on the stack (so RTS returns to
tx_done_exit), then does JMP (l0d58) to call the remote
JSR target routine. When that routine returns via RTS,
control resumes at tx_done_exit.""")


d.subroutine(0x9B50, 'tx_done_user_proc', title='TX done: UserProc event', description="""Generates a network event (event 8) via OSEVEN with
X=l0d58, A=l0d59 (the remote address). This notifies
the user program that a UserProc operation has completed.""")


d.subroutine(0x9B5E, 'tx_done_os_proc', title='TX done: OSProc call', description="""Calls the ROM entry point at &8000 (rom_header) with
X=l0d58, Y=l0d59. This invokes an OS-level procedure
on behalf of the remote station.""")


d.subroutine(0x9B6A, 'tx_done_halt', title='TX done: HALT', description="""Sets bit 2 of rx_flags (&0D64), enables interrupts, and
spin-waits until bit 2 is cleared (by a CONTINUE from the
remote station). If bit 2 is already set, skips to exit.""")


d.subroutine(0x9B81, 'tx_done_continue', title='TX done: CONTINUE', description="""Clears bit 2 of rx_flags (&0D64), releasing any station
that is halted and spinning in tx_done_halt.""")
d.comment(0x9B90, 'Save X on stack', align=Align.INLINE)
d.comment(0x9B91, 'Push X', align=Align.INLINE)
d.comment(0x9B92, 'Y=2: TXCB offset for dest station', align=Align.INLINE)
d.comment(0x9B94, 'Load dest station from TX control block', align=Align.INLINE)
d.comment(0x9B96, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9B9A, 'Load dest network from TX control block', align=Align.INLINE)
d.comment(0x9B9C, 'Store to TX scout buffer', align=Align.INLINE)
d.comment(0x9B9F, 'Y=0: first byte of TX control block', align=Align.INLINE)
d.comment(0x9BA1, 'Load control/flag byte', align=Align.INLINE)
d.comment(0x9BA3, 'Bit7 set: immediate operation ctrl byte', align=Align.INLINE)
d.comment(0x9BA5, 'Bit7 clear: normal data transfer', align=Align.INLINE)
d.comment(0x9BA8, 'Store control byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9BAB, 'X = control byte for range checks', align=Align.INLINE)
d.comment(0x9BAC, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x9BAD, 'Load port byte from TX control block', align=Align.INLINE)
d.comment(0x9BAF, 'Store port byte to TX scout buffer', align=Align.INLINE)
d.comment(0x9BB2, 'Port != 0: skip immediate op setup', align=Align.INLINE)
d.comment(0x9BB4, 'Ctrl < &83: PEEK/POKE need address calc', align=Align.INLINE)
d.comment(0x9BB6, 'Ctrl >= &83: skip to range check', align=Align.INLINE)
d.comment(0x9BB8, 'SEC: init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9BB9, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x9BBA, 'Y=8: high pointer offset in TXCB', align=Align.INLINE)
d.comment(0x9BBC, 'Load TXCB[Y] (end addr byte)', align=Align.INLINE)
d.comment(0x9BBE, 'Y -= 4: back to start addr offset', align=Align.INLINE)
d.comment(0x9BC2, 'Restore borrow from stack', align=Align.INLINE)
d.comment(0x9BC3, 'end - start = transfer size byte', align=Align.INLINE)
d.comment(0x9BC5, 'Store result to tx_data_start', align=Align.INLINE)
d.comment(0x9BCD, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9BCE, 'Done all 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9BD0, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9BD2, 'Discard final borrow', align=Align.INLINE)
d.comment(0x9BD3, 'Ctrl < &81: not an immediate op', align=Align.INLINE)
d.comment(0x9BD5, 'Below range: normal data transfer', align=Align.INLINE)
d.comment(0x9BD7, 'Ctrl >= &89: out of immediate range', align=Align.INLINE)
d.comment(0x9BD9, 'Above range: normal data transfer', align=Align.INLINE)
d.comment(0x9BDB, 'Y=&0C: start of extra data in TXCB', align=Align.INLINE)
d.comment(0x9BDD, 'Load extra parameter byte from TXCB', align=Align.INLINE)
d.comment(0x9BDF, 'Copy to NMI shim workspace at &0D1A+Y', align=Align.INLINE)
d.comment(0x9BE2, 'Next byte', align=Align.INLINE)
d.comment(0x9BE3, 'Done 4 bytes? (Y reaches &10)', align=Align.INLINE)
d.comment(0x9BE5, 'No: continue copying', align=Align.INLINE)
d.comment(0x9BE7, 'A=&20: mask for SR2 INACTIVE bit', align=Align.INLINE)
d.comment(0x9BE9, 'BIT SR2: test if line is idle', align=Align.INLINE)
d.comment(0x9BEC, 'Line not idle: handle as line jammed', align=Align.INLINE)
d.comment(0x9BEE, 'A=&FD: high byte of timeout counter', align=Align.INLINE)
d.comment(0x9BF0, 'Push timeout high byte to stack', align=Align.INLINE)
d.comment(0x9BF1, 'Scout frame = 6 address+ctrl bytes', align=Align.INLINE)
d.comment(0x9BF3, 'Store scout frame length', align=Align.INLINE)
d.comment(0x9BF6, 'A=0: init low byte of timeout counter', align=Align.INLINE)

d.label(0x9B89, 'tx_done_exit')


d.subroutine(0x9CA2, 'tx_ctrl_peek', title='TX ctrl: PEEK transfer setup', description="""Sets scout_status=3, then performs a 4-byte addition of
bytes from the TX block into the transfer parameter
workspace at &0D1E-&0D21 (with carry propagation).
Calls tx_calc_transfer to finalise, then exits via
tx_ctrl_exit.""")


d.subroutine(0x9CA6, 'tx_ctrl_poke', title='TX ctrl: POKE transfer setup', description="""Sets scout_status=2 and shares the 4-byte addition and
transfer calculation path with tx_ctrl_peek.""")


d.subroutine(0x9CBA, 'tx_ctrl_proc', title='TX ctrl: JSR/UserProc/OSProc setup', description="""Sets scout_status=2 and calls tx_calc_transfer directly
(no 4-byte address addition needed for procedure calls).
Shared by operation types &83-&85.""")
d.comment(0x9CC1, 'Load dest station for broadcast check', align=Align.INLINE)
d.comment(0x9CC4, 'AND with dest network', align=Align.INLINE)
d.comment(0x9CC7, 'Both &FF = broadcast address?', align=Align.INLINE)
d.comment(0x9CC9, 'Not broadcast: unicast path', align=Align.INLINE)
d.comment(0x9CCB, 'Broadcast scout: 14 bytes total', align=Align.INLINE)
d.comment(0x9CCD, 'Store broadcast scout length', align=Align.INLINE)
d.comment(0x9CD0, 'A=&40: broadcast flag', align=Align.INLINE)
d.comment(0x9CD2, 'Set broadcast flag in tx_flags', align=Align.INLINE)
d.comment(0x9CD5, 'Y=4: start of address data in TXCB', align=Align.INLINE)
d.comment(0x9CD7, 'Copy TXCB address bytes to scout buffer', align=Align.INLINE)
d.comment(0x9CD9, 'Store to TX source/data area', align=Align.INLINE)
d.comment(0x9CDC, 'Next byte', align=Align.INLINE)
d.comment(0x9CDD, 'Done 8 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9CDF, 'No: continue copying', align=Align.INLINE)
d.comment(0x9CE3, 'A=0: clear flags for unicast', align=Align.INLINE)
d.comment(0x9CE5, 'Clear tx_flags', align=Align.INLINE)
d.comment(0x9CE8, 'scout_status=2: data transfer pending', align=Align.INLINE)
d.comment(0x9CEA, 'Store scout status', align=Align.INLINE)
d.comment(0x9CED, 'Copy TX block pointer to workspace ptr', align=Align.INLINE)
d.comment(0x9CEF, 'Store low byte', align=Align.INLINE)
d.comment(0x9CF1, 'Copy TX block pointer high byte', align=Align.INLINE)
d.comment(0x9CF3, 'Store high byte', align=Align.INLINE)
d.comment(0x9CF5, 'Calculate transfer size from RXCB', align=Align.INLINE)
d.comment(0x9CF8, 'Restore processor status from stack', align=Align.INLINE)
d.comment(0x9CF9, 'Restore stacked registers (4 PLAs)', align=Align.INLINE)
d.comment(0x9CFA, 'Second PLA', align=Align.INLINE)
d.comment(0x9CFB, 'Third PLA', align=Align.INLINE)
d.comment(0x9CFC, 'Fourth PLA', align=Align.INLINE)
d.comment(0x9CFD, 'Restore X from A', align=Align.INLINE)
d.comment(0x9CFE, 'Return to caller', align=Align.INLINE)

d.label(0x9CF8, 'tx_ctrl_exit')
d.entry(0x9182)
d.entry(0x91ED)
d.entry(0x915F)
d.entry(0x877E)
d.entry(0x8FD8)
d.entry(0x97FC)
d.entry(0x8637)


d.subroutine(0x8637, 'save_fscv_args_with_ptrs', title='Save FSCV arguments with text pointers', description="""Extended entry used by FSCV, FINDV, and fscv_3_star_cmd.
Copies X/Y into os_text_ptr/&F3 and fs_cmd_ptr/&0E11, then
falls through to save_fscv_args to store A/X/Y in the FS
workspace.""", on_entry={'a': 'function code', 'x': 'text pointer low', 'y': 'text pointer high'})
d.comment(0x8637, 'Set os_text_ptr low = X', align=Align.INLINE)
d.comment(0x8639, 'Set os_text_ptr high = Y', align=Align.INLINE)


d.subroutine(0x863B, 'save_fscv_args', title='Save FSCV/vector arguments', description="""Stores A, X, Y into the filing system workspace. Called at the
start of every FS vector handler (FILEV, ARGSV, BGETV, BPUTV,
GBPBV, FINDV, FSCV). NFS repurposes CFS/RFS workspace locations:
  &BD (fs_last_byte_flag) = A (function code / command)
  &BB (fs_options)        = X (control block ptr low)
  &BC (fs_block_offset)   = Y (control block ptr high)
  &BE/&BF (fs_crc_lo/hi)  = X/Y (duplicate for indexed access)""", on_entry={'a': 'function code', 'x': 'control block pointer low', 'y': 'control block pointer high'})
d.comment(0x863B, 'Save A = function code / command', align=Align.INLINE)
d.comment(0x863D, 'Save X = control block ptr low', align=Align.INLINE)
d.comment(0x863F, 'Save Y = control block ptr high', align=Align.INLINE)
d.comment(0x8641, 'Duplicate X for indirect indexed access', align=Align.INLINE)
d.comment(0x8643, 'Duplicate Y for indirect indexed access', align=Align.INLINE)
d.comment(0x8645, 'Clear escapable flag, preserving processor flags', align=Align.INLINE)
d.comment(0x8646, 'Reset: this operation is not escapable yet', align=Align.INLINE)
d.comment(0x8648, 'Restore flags (caller may need N/Z/C)', align=Align.INLINE)
d.comment(0x8649, 'Return', align=Align.INLINE)


d.subroutine(0x85BD, 'decode_attribs_6bit', title='Decode file attributes: FS → BBC format (FSBBC, 6-bit variant)', description="""Reads attribute byte at offset &0E from the parameter block,
masks to 6 bits, then falls through to the shared bitmask
builder. Converts fileserver protection format (5-6 bits) to
BBC OSFILE attribute format (8 bits) via the lookup table at
&85DA. The two formats use different bit layouts for file
protection attributes.""", on_exit={'a': 'BBC attribute bitmask (8-bit)', 'x': 'corrupted', 'y': '&0E'})
d.comment(0x85BD, 'Y=&0E: attribute byte offset in param block', align=Align.INLINE)
d.comment(0x85BF, 'Load FS attribute byte', align=Align.INLINE)
d.comment(0x85C1, 'Mask to 6 bits (FS → BBC direction)', align=Align.INLINE)
d.comment(0x85C3, 'X=4: skip first 4 table entries (BBC→FS half)', align=Align.INLINE)
d.comment(0x85C5, 'ALWAYS branch to shared bitmask builder', align=Align.INLINE)


d.subroutine(0x85C7, 'decode_attribs_5bit', title='Decode file attributes: BBC → FS format (BBCFS, 5-bit variant)', description="""Masks A to 5 bits and builds an access bitmask via the
lookup table at &85DA. Each input bit position maps to a
different output bit via the table. The conversion is done
by iterating through the source bits and OR-ing in the
corresponding destination bits from the table, translating
between BBC (8-bit) and fileserver (5-bit) protection formats.""", on_entry={'a': 'BBC attribute byte (bits 0-4 used)'}, on_exit={'a': 'FS attribute bitmask (5-bit)', 'x': 'corrupted'})
d.comment(0x85C7, 'Mask to 5 bits (BBC → FS direction)', align=Align.INLINE)
d.comment(0x85C9, 'X=&FF: INX makes 0; start from table index 0', align=Align.INLINE)
d.comment(0x85CB, 'Temp storage for source bitmask to shift out', align=Align.INLINE)
d.comment(0x85CD, 'A=0: accumulate destination bits here', align=Align.INLINE)
d.comment(0x85CF, 'Next table entry', align=Align.INLINE)
d.comment(0x85D0, 'Shift out source bits one at a time', align=Align.INLINE)
d.comment(0x85D2, 'Bit was 0: skip this destination bit', align=Align.INLINE)
d.comment(0x85D4, 'OR in destination bit from lookup table', align=Align.INLINE)
d.comment(0x85D7, 'Loop while source bits remain (A != 0)', align=Align.INLINE)
d.comment(0x85D9, 'Return; A = converted attribute bitmask', align=Align.INLINE)
d.comment(0x85DA, 'Attribute bit mapping table (11 entries)', align=Align.INLINE)


d.subroutine(0x8665, 'parse_decimal', title='Parse decimal number from (fs_options),Y (DECIN)', description="""Reads ASCII digits and accumulates in &B2 (fs_load_addr_2).
Multiplication by 10 uses the identity: n*10 = n*8 + n*2,
computed as ASL &B2 (x2), then A = &B2*4 via two ASLs,
then ADC &B2 gives x10.
Terminates on "." (pathname separator), control chars, or space.
The delimiter handling was revised to support dot-separated path
components (e.g. "1.$.PROG") -- originally stopped on any char
>= &40 (any letter), but the revision allows numbers followed
by dots.""", on_entry={'y': 'offset into (fs_options) buffer'}, on_exit={'a': 'parsed value (accumulated in &B2)', 'x': 'preserved', 'y': 'offset past last digit parsed'})
d.comment(0x8665, 'Zero accumulator', align=Align.INLINE)
d.comment(0x8669, 'Load next char from buffer', align=Align.INLINE)
d.comment(0x866B, 'Dot separator?', align=Align.INLINE)
d.comment(0x866D, 'Yes: exit with C=1 (dot found)', align=Align.INLINE)
d.comment(0x866F, 'Control char or space: done', align=Align.INLINE)
d.comment(0x8671, 'Mask ASCII digit to 0-9', align=Align.INLINE)
d.comment(0x8673, 'Save new digit', align=Align.INLINE)
d.comment(0x8675, 'Running total * 2', align=Align.INLINE)
d.comment(0x8677, 'A = running total * 2', align=Align.INLINE)
d.comment(0x8679, 'A = running total * 4', align=Align.INLINE)
d.comment(0x867A, 'A = running total * 8', align=Align.INLINE)
d.comment(0x867B, '+ total*2 = total * 10', align=Align.INLINE)
d.comment(0x867D, '+ digit = total*10 + digit', align=Align.INLINE)
d.comment(0x867F, 'Store new running total', align=Align.INLINE)
d.comment(0x8681, 'Advance to next char', align=Align.INLINE)
d.comment(0x8682, "Loop (always: Y won't wrap to 0)", align=Align.INLINE)
d.comment(0x8684, 'No dot found: C=0', align=Align.INLINE)
d.comment(0x8685, 'Return result in A', align=Align.INLINE)


d.subroutine(0x8688, 'handle_to_mask_a', title='Convert handle in A to bitmask', description="""Transfers A to Y via TAY, then falls through to
handle_to_mask_clc to clear carry and convert.""", on_entry={'a': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})
d.comment(0x8688, 'Handle number to Y for conversion', align=Align.INLINE)


d.subroutine(0x8689, 'handle_to_mask_clc', title='Convert handle to bitmask (carry cleared)', description="""Clears carry to ensure handle_to_mask converts
unconditionally. Falls through to handle_to_mask.""", on_entry={'y': 'file handle number (&20-&27, or 0)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if invalid'})
d.comment(0x8689, 'Force unconditional conversion', align=Align.INLINE)


d.subroutine(0x868A, 'handle_to_mask', title='Convert file handle to bitmask (Y2FS)', description="""Converts fileserver handles to single-bit masks segregated inside
the BBC. NFS handles occupy the &20-&27 range (base HAND=&20),
which cannot collide with local filing system or cassette handles
-- the MOS routes OSFIND/OSBGET/OSBPUT to the correct filing
system based on the handle value alone. The power-of-two encoding
allows the EOF hint byte to track up to 8 files simultaneously
with one bit per file, and enables fast set operations (ORA to
add, EOR to toggle, AND to test) without loops. Handle 0 passes
through unchanged (means "no file"). The bit-shift conversion loop
has a built-in validity check: if the handle is out of range, the
repeated ASL shifts all bits out, leaving A=0, which is converted
to Y=&FF as a sentinel -- bad handles fail gracefully rather than
indexing into garbage.
Callers needing to move the handle from A use handle_to_mask_a;
callers needing carry cleared use handle_to_mask_clc.""", on_entry={'y': 'handle number', 'c': '0: convert, 1 with Y=0: skip, 1 with Y!=0: convert'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'bitmask (single bit set) or &FF if handle invalid'})
d.comment(0x868A, 'Save A (will be restored on exit)', align=Align.INLINE)
d.comment(0x868B, 'Save X (will be restored on exit)', align=Align.INLINE)
d.comment(0x868C, '  (second half of X save)', align=Align.INLINE)
d.comment(0x868D, 'A = handle from Y', align=Align.INLINE)
d.comment(0x868E, 'C=0: always convert', align=Align.INLINE)
d.comment(0x8690, 'C=1 and Y=0: skip (handle 0 = none)', align=Align.INLINE)
d.comment(0x8692, 'C=1 and Y!=0: convert', align=Align.INLINE)
d.comment(0x8693, 'A = handle - &1F (1-based bit position)', align=Align.INLINE)
d.comment(0x8695, 'X = shift count', align=Align.INLINE)
d.comment(0x8696, 'Start with bit 0 set', align=Align.INLINE)
d.comment(0x8698, 'Shift bit left', align=Align.INLINE)
d.comment(0x8699, 'Count down', align=Align.INLINE)
d.comment(0x869A, 'Loop until correct position', align=Align.INLINE)
d.comment(0x869C, 'Undo final extra shift', align=Align.INLINE)
d.comment(0x869D, 'Y = resulting bitmask', align=Align.INLINE)
d.comment(0x869E, 'Non-zero: valid mask, skip to exit', align=Align.INLINE)
d.comment(0x86A0, 'Zero: invalid handle, set Y=&FF', align=Align.INLINE)
d.comment(0x86A1, 'Restore X', align=Align.INLINE)
d.comment(0x86A3, 'Restore A', align=Align.INLINE)


d.subroutine(0x86A5, 'mask_to_handle', title='Convert bitmask to handle number (FS2A)', description="""Inverse of Y2FS. Converts from the power-of-two FS format
back to a sequential handle number by counting right shifts
until A=0. Adds &1E to convert the 1-based bit position to
a handle number (handles start at &1F+1 = &20). Used when
receiving handle values from the fileserver in reply packets.""", on_entry={'a': 'single-bit bitmask'}, on_exit={'a': 'handle number (&20-&27)', 'x': 'corrupted', 'y': 'preserved'})
d.comment(0x86A5, 'X = &1F (handle base - 1)', align=Align.INLINE)
d.comment(0x86A7, 'Count this bit position', align=Align.INLINE)
d.comment(0x86A8, 'Shift mask right; C=0 when done', align=Align.INLINE)
d.comment(0x86A9, 'Loop until all bits shifted out', align=Align.INLINE)
d.comment(0x86AB, 'A = X = &1F + bit position = handle', align=Align.INLINE)


d.subroutine(0x8DAB, 'print_decimal', title='Print byte as 3-digit decimal number', description="""Prints A as a decimal number using repeated subtraction
for each digit position (100, 10, 1). Leading zeros are
printed (no suppression). Used to display station numbers.""", on_entry={'a': 'byte value to print'}, on_exit={'a': 'last digit character', 'x': 'corrupted', 'y': '0 (remainder after last division)'})
d.comment(0x8DAB, 'Y = value to print', align=Align.INLINE)
d.comment(0x8DAC, 'Divisor = 100 (hundreds digit)', align=Align.INLINE)
d.comment(0x8DAE, 'Print hundreds digit', align=Align.INLINE)
d.comment(0x8DB1, 'Divisor = 10 (tens digit)', align=Align.INLINE)
d.comment(0x8DB3, 'Print tens digit', align=Align.INLINE)
d.comment(0x8DB6, 'Divisor = 1; fall through to units', align=Align.INLINE)


d.subroutine(0x8DB8, 'print_decimal_digit', title='Print one decimal digit by repeated subtraction', description="""Divides Y by A using repeated subtraction. Prints the
quotient as an ASCII digit ('0'-'9') via OSASCI. Returns
with the remainder in Y. X starts at &2F ('0'-1) and
increments once per subtraction, giving the ASCII digit
directly.""", on_entry={'a': 'divisor (stored to &B8)', 'y': 'dividend'}, on_exit={'y': 'remainder'})
d.comment(0x8DB8, 'Save divisor to workspace', align=Align.INLINE)
d.comment(0x8DBA, 'A = dividend (from Y)', align=Align.INLINE)
d.comment(0x8DBB, "X = &2F = ASCII '0' - 1", align=Align.INLINE)
d.comment(0x8DBD, 'Prepare for subtraction', align=Align.INLINE)
d.comment(0x8DBE, 'Count one subtraction (next digit value)', align=Align.INLINE)
d.comment(0x8DBF, 'A = A - divisor', align=Align.INLINE)
d.comment(0x8DC1, 'Loop while A >= 0 (borrow clear)', align=Align.INLINE)
d.comment(0x8DC3, 'Undo last subtraction: A = remainder', align=Align.INLINE)
d.comment(0x8DC5, 'Y = remainder for caller', align=Align.INLINE)
d.comment(0x8DC6, 'A = X = ASCII digit character', align=Align.INLINE)


d.subroutine(0x8DCA, 'print_hex_byte', title='Print A as two hexadecimal digits', description="""Prints the byte in A as two hex digits (e.g. &3F prints "3F").
Saves A, shifts high nibble down, prints it via print_hex_nibble,
then recovers the original A and prints the low nibble.
The nibble-to-hex conversion uses ORA #&30 / CMP #&3A to
distinguish 0-9 (ASCII &30-&39) from A-F (add 7 more).
New in 3.65: moved inline from &9F9D (end of ROM in 3.62).""")
d.comment(0x8DCA, 'Save original byte', align=Align.INLINE)
d.comment(0x8DCB, 'Shift high nibble to low position', align=Align.INLINE)
d.comment(0x8DCC, 'LSR (continued)', align=Align.INLINE)
d.comment(0x8DCD, 'LSR (continued)', align=Align.INLINE)
d.comment(0x8DCE, 'LSR (continued): A = high nibble', align=Align.INLINE)
d.comment(0x8DCF, 'Print high nibble as hex digit', align=Align.INLINE)
d.comment(0x8DD2, 'Recover original byte', align=Align.INLINE)
d.comment(0x8DD3, 'Mask to low nibble', align=Align.INLINE)
d.comment(0x8DD5, "Convert nibble to ASCII: &00-&09 -> '0'-'9'", align=Align.INLINE)
d.comment(0x8DD7, "Digit or letter? &3A = ':'", align=Align.INLINE)
d.comment(0x8DD9, 'Digit 0-9: print directly', align=Align.INLINE)
d.comment(0x8DDB, 'Letter A-F: add 7 (carry already set)', align=Align.INLINE)
d.comment(0x8DDD, 'ALWAYS branch to print_digit', align=Align.INLINE)


d.subroutine(0x86AD, 'compare_addresses', title='Compare two 4-byte addresses', description="""Compares bytes at &B0-&B3 against &B4-&B7 using EOR.
Used by the OSFILE save handler to compare the current
transfer address (&C8-&CB, copied to &B0) against the end
address (&B4-&B7) during multi-block file data transfers.""", on_exit={'a': 'corrupted (EOR result)', 'x': 'corrupted', 'y': 'preserved'})
d.comment(0x86AD, 'Compare 4 bytes (index 4,3,2,1)', align=Align.INLINE)
d.comment(0x86AF, 'Load byte from first address', align=Align.INLINE)
d.comment(0x86B1, 'XOR with corresponding byte', align=Align.INLINE)
d.comment(0x86B3, 'Mismatch: Z=0, return unequal', align=Align.INLINE)
d.comment(0x86B6, 'Continue comparing', align=Align.INLINE)
d.comment(0x86B9, 'X=first handle (&20)', align=Align.INLINE)
d.comment(0x86BB, 'Y=last handle (&27)', align=Align.INLINE)


d.subroutine(0x86BE, 'set_fs_flag', title='Set bit(s) in EOF hint flags (&0E07)', description="""ORs A into fs_eof_flags then stores the result via
store_fs_flag. Each bit represents one of up to 8 open file
handles. When clear, the file is definitely NOT at EOF. When
set, the fileserver must be queried to confirm EOF status.
This negative-cache optimisation avoids expensive network
round-trips for the common case. The hint is cleared when
the file pointer is updated (since seeking away from EOF
invalidates the hint) and set after BGET/OPEN/EOF operations
that might have reached the end.""", on_entry={'a': 'bitmask of bits to set'}, on_exit={'a': 'updated fs_eof_flags value'})
d.comment(0x86BE, 'Merge new bits into flags', align=Align.INLINE)
d.comment(0x86C1, 'Store updated flags (always taken)', align=Align.INLINE)


d.subroutine(0x86C3, 'clear_fs_flag', title='Clear bit(s) in FS flags (&0E07)', description="""Inverts A (EOR #&FF), then ANDs the result into fs_eof_flags
to clear the specified bits.""", on_entry={'a': 'bitmask of bits to clear'}, on_exit={'a': 'updated fs_eof_flags value'})
d.comment(0x86C3, 'Invert mask: set bits become clear bits', align=Align.INLINE)
d.comment(0x86C5, 'Clear specified bits in flags', align=Align.INLINE)
d.comment(0x86C8, 'Write back updated flags', align=Align.INLINE)
d.comment(0x86CB, 'Return', align=Align.INLINE)
d.comment(0x86CC, 'Y=1: copy 2 bytes (high then low)', align=Align.INLINE)
d.comment(0x86CE, 'Load filename ptr from control block', align=Align.INLINE)
d.comment(0x86D0, 'Store to MOS text pointer (&F2/&F3)', align=Align.INLINE)
d.comment(0x86D3, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x86D4, 'Loop for both bytes', align=Align.INLINE)


d.subroutine(0x85E5, 'setup_tx_ptr_c0', title='Set up TX pointer to control block at &00C0', description="""Points net_tx_ptr to &00C0 where the TX control block has
been built by init_tx_ctrl_block. Falls through to tx_poll_ff
to initiate transmission with full retry.""", on_exit={'a': '&FF (retry count, restored)', 'x': '0', 'y': '0'})
d.comment(0x85E5, 'TX control block low byte', align=Align.INLINE)
d.comment(0x85E7, 'Set net_tx_ptr = &00C0', align=Align.INLINE)
d.comment(0x85E9, 'TX control block high byte', align=Align.INLINE)
d.comment(0x85EB, 'Set net_tx_ptr+1 = &00', align=Align.INLINE)


d.subroutine(0x85ED, 'tx_poll_ff', title='Transmit and poll for result (full retry)', description="""Sets A=&FF (retry count) and Y=&60 (timeout parameter).
Falls through to tx_poll_core.""", on_exit={'a': '&FF (retry count, restored)', 'x': '0', 'y': '0'})


d.subroutine(0x85F1, 'tx_poll_core', title='Core transmit and poll routine (XMIT)', description="""Claims the TX semaphore (tx_clear_flag) via ASL -- a busy-wait
spinlock where carry=0 means the semaphore is held by another
operation. Only after claiming the semaphore is the TX pointer
copied to nmi_tx_block, ensuring the low-level transmit code
sees a consistent pointer. Then calls the ADLC TX setup routine
and polls the control byte for completion:
  bit 7 set = still busy (loop)
  bit 6 set = error (check escape or report)
  bit 6 clear = success (clean return)
On error, checks for escape condition and handles retries.
Two entry points: setup_tx_ptr_c0 (&85E5) always uses the
standard TXCB; tx_poll_core (&85F1) is general-purpose.""", on_entry={'a': 'retry count (&FF = full retry)', 'y': 'timeout parameter (&60 = standard)'}, on_exit={'a': 'entry A (retry count, restored from stack)', 'x': '0', 'y': '0'})
d.comment(0x85F1, 'Save retry count and timeout on stack', align=Align.INLINE)
d.comment(0x85F2, 'Transfer timeout to A', align=Align.INLINE)
d.comment(0x85F3, 'Push timeout parameter', align=Align.INLINE)
d.comment(0x85F4, 'X=0 for (zp,X) indirect addressing', align=Align.INLINE)
d.comment(0x85F6, 'Read control byte from TX block', align=Align.INLINE)
d.comment(0x85F8, 'Write back control byte (re-arm for TX)', align=Align.INLINE)
d.comment(0x85FA, 'Save control byte for error recovery', align=Align.INLINE)
d.comment(0x85FB, 'Spin until TX semaphore is free (C=1)', align=Align.INLINE)
d.comment(0x85FE, 'C=0: still held, keep spinning', align=Align.INLINE)
d.comment(0x8600, 'Copy TX pointer to NMI block while locked', align=Align.INLINE)
d.comment(0x8602, 'Store low byte to NMI TX block', align=Align.INLINE)
d.comment(0x8604, 'Load TX pointer high byte', align=Align.INLINE)
d.comment(0x8606, 'Store high byte to NMI TX block', align=Align.INLINE)
d.comment(0x8608, 'Initiate ADLC transmission', align=Align.INLINE)
d.comment(0x860B, 'Poll: wait for bit 7 to clear (TX done)', align=Align.INLINE)
d.comment(0x860D, 'Bit 7 set: still busy, keep polling', align=Align.INLINE)
d.comment(0x860F, 'Bit 6 into sign: 0=success, 1=error', align=Align.INLINE)
d.comment(0x8610, 'Success: clean up stack and exit', align=Align.INLINE)
d.comment(0x8612, 'Bit 5: escape condition?', align=Align.INLINE)
d.comment(0x8613, 'Yes (Z=1): abort via nlistn', align=Align.INLINE)
d.comment(0x8615, 'Check for escape key pressed', align=Align.INLINE)
d.comment(0x8618, 'Recover saved control byte', align=Align.INLINE)
d.comment(0x8619, 'Move to X for retry', align=Align.INLINE)
d.comment(0x861A, 'Recover timeout parameter', align=Align.INLINE)
d.comment(0x861B, 'Move to Y for delay loop', align=Align.INLINE)
d.comment(0x861C, 'Recover retry count', align=Align.INLINE)
d.comment(0x861D, 'Retries exhausted: abort via nlistn', align=Align.INLINE)
d.comment(0x861F, 'Decrement retry count (C=1 from CMP)', align=Align.INLINE)
d.comment(0x8621, 'Re-push retry count and timeout for retry', align=Align.INLINE)
d.comment(0x8622, 'Transfer timeout to A', align=Align.INLINE)
d.comment(0x8623, 'Push timeout for next attempt', align=Align.INLINE)
d.comment(0x8624, 'Restore control byte for retry', align=Align.INLINE)
d.comment(0x8625, 'Delay loop: X*Y iterations before retry', align=Align.INLINE)
d.comment(0x8626, 'Inner loop: decrement X', align=Align.INLINE)
d.comment(0x8628, 'Outer loop: decrement Y', align=Align.INLINE)
d.comment(0x8629, 'Continue delay until Y=0', align=Align.INLINE)
d.comment(0x862B, 'ALWAYS branch', align=Align.INLINE)
d.comment(0x862D, 'A = error code for nlistn', align=Align.INLINE)
d.comment(0x862E, 'Report net error via nlistn', align=Align.INLINE)
d.comment(0x8631, 'Success: discard 3 saved bytes from stack', align=Align.INLINE)
d.comment(0x8632, 'Discard timeout', align=Align.INLINE)
d.comment(0x8633, 'Discard retry count', align=Align.INLINE)
d.comment(0x8634, 'Jump to clear escapable flag and return', align=Align.INLINE)


d.subroutine(0x864A, 'print_inline', title='Print inline string, high-bit terminated (VSTRNG)', description="""Pops the return address from the stack, prints each byte via OSASCI
until a byte with bit 7 set is found, then jumps to that address.
The high-bit byte serves as both the string terminator and the opcode
of the first instruction after the string. N.B. Cannot be used for
BRK error messages -- the stack manipulation means a BRK in the
inline data would corrupt the stack rather than invoke the error
handler.""", on_exit={'a': 'terminator byte (bit 7 set, also next opcode)', 'x': 'corrupted (by OSASCI)', 'y': '0'})
d.comment(0x864A, 'Pop return address (low) — points to last byte of JSR', align=Align.INLINE)
d.comment(0x864D, 'Pop return address (high)', align=Align.INLINE)
d.comment(0x8652, 'Advance pointer past return address / to next char', align=Align.INLINE)
d.comment(0x8658, 'Load next byte from inline string', align=Align.INLINE)
d.comment(0x865A, 'Bit 7 set? Done — this byte is the next opcode', align=Align.INLINE)
d.comment(0x8662, 'Jump to address of high-bit byte (resumes code after string)', align=Align.INLINE)
d.comment(0x8021, """Dispatch table: low bytes of (handler_address - 1)
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
&8040-&8045, immediately before the hi bytes. Their hi
bytes are at &8065-&806A, after dispatch_0_hi.""")
dispatch_comments = ['Svc 0: already claimed (no-op)', 'Svc 1: absolute workspace', 'Svc 2: private workspace', 'Svc 3: auto-boot', 'Svc 4: unrecognised star command', 'Svc 5: unrecognised interrupt', 'Svc 6: BRK (no-op)', 'Svc 7: unrecognised OSBYTE', 'Svc 8: unrecognised OSWORD', 'Svc 9: *HELP', 'Svc 10: static workspace (no-op)', 'Svc 11: NMI release (reclaim NMIs)', 'Svc 12: NMI claim (save NMI state)', 'Svc 13: select NFS (intercepted before dispatch)', 'Lang 0: no language / Tube', 'Lang 1: normal startup', 'Lang 2: softkey byte (Electron)', 'Lang 3: softkey length (Electron)', 'Lang 4: remote validated', 'FSCV 0: *OPT', 'FSCV 1: EOF check', 'FSCV 2: */ (run)', 'FSCV 3: unrecognised star command', 'FSCV 4: *RUN', 'FSCV 5: *CAT', 'FSCV 6: shutdown', 'FSCV 7: read handle range', 'FS reply: print directory name', 'FS reply: copy handles + boot', 'FS reply: copy handles', 'FS reply: set CSD handle', 'FS reply: notify + execute', 'FS reply: set library handle', '*NET1: read handle from packet', '*NET2: read handle from workspace', '*NET3: close handle', '*NET4: resume remote']
for i, body in enumerate(dispatch_comments):
    d.comment(0x8021 + i, f'lo - {body}', align=Align.INLINE)
    d.comment(0x8046 + i, f'hi - {body}', align=Align.INLINE)


d.subroutine(0x806B, 'dispatch_net_cmd', title='*NET command dispatcher', description="""Parses the character after *NET as '1'-'4', maps to table
indices 33-36 via base offset Y=&21, and dispatches via &80E3.
Characters outside '1'-'4' fall through to return_1 (RTS).

These are internal sub-commands used only by the ROM itself,
not user-accessible star commands. The MOS command parser
requires a space or terminator after 'NET', so *NET1 typed
at the command line does not match; these are reached only
via OSCLI calls within the ROM.

*NET1 (&8E6A): read file handle from received
packet (net_1_read_handle)

*NET2 (&8E70): read handle entry from workspace
(net_2_read_handle_entry)

*NET3 (&8E80): close handle / mark as unused
(net_3_close_handle)

*NET4 (&81AA): resume after remote operation
(net_4_resume_remote)""")
d.comment(0x806B, 'Read command character following *NET', align=Align.INLINE)
d.comment(0x806D, "Subtract ASCII '1' to get 0-based command index", align=Align.INLINE)
d.comment(0x806F, 'Command index >= 4: invalid *NET sub-command', align=Align.INLINE)
d.comment(0x8071, 'Out of range: return via c80e3/RTS', align=Align.INLINE)
d.comment(0x8073, 'X = command index (0-3)', align=Align.INLINE)
d.comment(0x8074, 'Clear &A9 (used by dispatch)', align=Align.INLINE)
d.comment(0x8076, 'Store zero to &A9', align=Align.INLINE)
d.comment(0x8078, 'Preserve A before dispatch', align=Align.INLINE)
d.comment(0x8079, 'Y=&21: base offset for *NET commands (index 33+)', align=Align.INLINE)
d.comment(0x807B, 'ALWAYS branch to dispatch', align=Align.INLINE)


d.subroutine(0x80E3, 'dispatch', title='PHA/PHA/RTS computed dispatch', description="""X = command index within caller's group (e.g. service number)
Y = base offset into dispatch table (0, &0E, &13, &21, etc.)
The loop adds Y+1 to X, so final X = command index + base + 1.
Then high and low bytes of (handler-1) are pushed onto the stack,
and RTS pops them and jumps to handler_address.

This is a standard 6502 trick: RTS increments the popped address
by 1 before jumping, so the table stores (address - 1) to
compensate. Multiple callers share one table via different Y
base offsets.""")
d.comment(0x80E3, 'Add base offset Y to index X (loop: X += Y+1)', align=Align.INLINE)
d.comment(0x80E4, 'Decrement base offset counter', align=Align.INLINE)
d.comment(0x80E5, 'Loop until Y exhausted', align=Align.INLINE)
d.comment(0x80E7, 'Y=&FF (no further use)', align=Align.INLINE)
d.comment(0x80E8, 'Load high byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80EB, 'Push high byte onto stack', align=Align.INLINE)
d.comment(0x80EC, 'Load low byte of (handler - 1) from table', align=Align.INLINE)
d.comment(0x80EF, 'Push low byte onto stack', align=Align.INLINE)
d.comment(0x80F0, 'Restore X (fileserver options) for use by handler', align=Align.INLINE)
d.comment(0x80F2, 'RTS pops address, adds 1, jumps to handler', align=Align.INLINE)


d.subroutine(0x80DD, 'lang_entry_dispatch', title='Language entry dispatcher', description="""Called when the NFS ROM is entered as a language. Although rom_type
(&82) does not set the language bit, the MOS enters this point
after NFS claims service &FE (Tube post-init). X = reason code
(0-4). Dispatches via table indices 15-19 (base offset Y=&0E).""")
d.comment(0x80DD, 'X >= 5: invalid reason code, return', align=Align.INLINE)
d.comment(0x80DF, 'Out of range: return via RTS', align=Align.INLINE)
d.comment(0x80E1, 'Y=&0E: base offset for language handlers (index 15+)', align=Align.INLINE)
d.comment(0x80F3, 'Save service call number', align=Align.INLINE)
d.comment(0x80F4, 'Only probe ADLC on service 1 (workspace claim)', align=Align.INLINE)
d.comment(0x80F6, 'Not service 1: skip probe', align=Align.INLINE)
d.comment(0x80F8, 'Probe ADLC SR1: non-zero = absent (bus noise)', align=Align.INLINE)
d.comment(0x80FB, 'Mask SR1 status bits (ignore bits 4,1)', align=Align.INLINE)
d.comment(0x80FD, 'Non-zero: ADLC absent, set disable flag', align=Align.INLINE)
d.comment(0x80FF, 'Probe ADLC SR2 if SR1 was all zeros', align=Align.INLINE)
d.comment(0x8102, 'Mask SR2 status bits (ignore bits 5,2)', align=Align.INLINE)
d.comment(0x8104, 'Both zero: ADLC present, skip', align=Align.INLINE)
d.comment(0x8106, 'Set bit 7 of per-ROM workspace = disable flag', align=Align.INLINE)
d.comment(0x8109, 'SEC for ROR to set bit 7', align=Align.INLINE)
d.comment(0x810A, 'Rotate carry into bit 7 of workspace', align=Align.INLINE)
d.comment(0x810D, 'Read back flag; ASL puts bit 7 into carry', align=Align.INLINE)
d.comment(0x8110, 'C into bit 7 of A', align=Align.INLINE)
d.comment(0x8111, 'Restore service call number', align=Align.INLINE)
d.comment(0x8112, 'Service >= &80: always handle (Tube/init)', align=Align.INLINE)
d.comment(0x8114, 'C=1 (no ADLC): disable ROM, skip', align=Align.INLINE)
d.comment(0x8116, 'Service >= &FE?', align=Align.INLINE)
d.comment(0x8118, 'Service < &FE: skip to &12/dispatch check', align=Align.INLINE)
d.comment(0x811A, 'Service &FF: full init (vectors + RAM copy)', align=Align.INLINE)
d.comment(0x811C, 'Service &FE: Y=0?', align=Align.INLINE)
d.comment(0x811E, 'Y=0: no Tube data, skip to &12 check', align=Align.INLINE)
d.comment(0x8120, 'X=6 extra pages for char definitions', align=Align.INLINE)
d.comment(0x8122, 'OSBYTE &14: explode character RAM', align=Align.INLINE)
d.comment(0x8127, 'Poll Tube status register 1', align=Align.INLINE)
d.comment(0x812A, 'Loop until Tube ready (bit 7 set)', align=Align.INLINE)
d.comment(0x812C, 'Read byte from Tube data register 1', align=Align.INLINE)
d.comment(0x812F, 'Zero byte: Tube transfer complete', align=Align.INLINE)
d.comment(0x8131, 'Send Tube char to screen via OSWRCH', align=Align.INLINE)
d.comment(0x8134, 'Loop for next Tube byte', align=Align.INLINE)
d.comment(0x8137, 'EVNTV low = &AD (event handler address)', align=Align.INLINE)
d.comment(0x8139, 'Set EVNTV low byte at &0220', align=Align.INLINE)
d.comment(0x813C, 'EVNTV high = &06 (page 6)', align=Align.INLINE)
d.comment(0x813E, 'Set EVNTV high byte at &0221', align=Align.INLINE)
d.comment(0x8141, 'BRKV low = &16 (NMI workspace)', align=Align.INLINE)
d.comment(0x8143, 'Set BRKV low byte at &0202', align=Align.INLINE)
d.comment(0x8146, 'BRKV high = &00 (zero page)', align=Align.INLINE)
d.comment(0x8148, 'Set BRKV high byte at &0203', align=Align.INLINE)
d.comment(0x814B, 'Tube control register init value &8E', align=Align.INLINE)
d.comment(0x814D, 'Write to Tube control register', align=Align.INLINE)
d.comment(0x8150, 'Y=0: copy 256 bytes per page', align=Align.INLINE)
d.comment(0x8152, 'Load ROM byte from page &93', align=Align.INLINE)
d.comment(0x8155, 'Store to page &04 (Tube code)', align=Align.INLINE)
d.comment(0x8158, 'Load ROM byte from page &94', align=Align.INLINE)
d.comment(0x815B, 'Store to page &05 (dispatch table)', align=Align.INLINE)
d.comment(0x815E, 'Load ROM byte from page &95', align=Align.INLINE)
d.comment(0x8161, 'Store to page &06', align=Align.INLINE)
d.comment(0x8164, 'DEY wraps 0 -> &FF on first iteration', align=Align.INLINE)
d.comment(0x8165, 'Loop until 256 bytes copied per page', align=Align.INLINE)
d.comment(0x8167, 'Run post-init routine in copied code', align=Align.INLINE)
d.comment(0x816A, 'X=&60: copy 97 bytes (&60..&00)', align=Align.INLINE)
d.comment(0x816C, 'Load NMI workspace init byte from ROM', align=Align.INLINE)
d.comment(0x816F, 'Store to zero page &16+X', align=Align.INLINE)
d.comment(0x8171, 'Next byte', align=Align.INLINE)
d.comment(0x8172, 'Loop until all workspace bytes copied', align=Align.INLINE)
d.comment(0x8174, 'A=0: fall through to service &12 check', align=Align.INLINE)
d.comment(0x8176, 'Is this service &12 (select FS)?', align=Align.INLINE)
d.comment(0x8178, 'No: check if service < &0D', align=Align.INLINE)
d.comment(0x817A, 'Service &12: Y=5 (NFS)?', align=Align.INLINE)
d.comment(0x817C, 'Not NFS: check if service < &0D', align=Align.INLINE)
d.comment(0x817E, 'A=&0D: dispatch index for svc_13_select_nfs', align=Align.INLINE)
d.comment(0x8180, 'ALWAYS branch to dispatch', align=Align.INLINE)
d.comment(0x8182, 'Service >= &0D?', align=Align.INLINE)
d.comment(0x8184, 'Service >= &0D: not handled, return', align=Align.INLINE)
d.comment(0x8186, 'X = service number (dispatch index)', align=Align.INLINE)
d.comment(0x8187, 'Save &A9 (current service state)', align=Align.INLINE)
d.comment(0x8189, 'Push saved &A9', align=Align.INLINE)
d.comment(0x818A, 'Save &A8 (workspace page number)', align=Align.INLINE)
d.comment(0x818C, 'Push saved &A8', align=Align.INLINE)
d.comment(0x818D, 'Store service number to &A9', align=Align.INLINE)
d.comment(0x818F, 'Store Y (page number) to &A8', align=Align.INLINE)
d.comment(0x8191, 'A = Y for dispatch table offset', align=Align.INLINE)
d.comment(0x8192, 'Y=0: base offset for service dispatch', align=Align.INLINE)
d.comment(0x8194, 'Dispatch to service handler', align=Align.INLINE)
d.comment(0x8197, 'Recover service claim status from &A9', align=Align.INLINE)
d.comment(0x8199, 'Restore saved &A8 from stack', align=Align.INLINE)
d.comment(0x819A, 'Write back &A8', align=Align.INLINE)


d.subroutine(0x8116, 'service_handler_entry', title='Service handler entry', description="""On service 1 only, probes ADLC status registers SR1 (&FEA0)
and SR2 (&FEA1) to detect whether Econet hardware is present.
Non-zero reads indicate bus noise from absent hardware; sets
bit 7 of per-ROM workspace as a disable flag. For services
< &80, the flag causes an early return (disabling this ROM).
Services >= &80 (&FE, &FF) are always handled regardless.

Intercepts three service calls before normal dispatch:
  &FE: Tube init — explode character definitions
  &FF: Full init — vector setup, copy code to RAM, select NFS
  &12 (Y=5): Select NFS as active filing system
All other service calls < &0D dispatch via c8146.""")

d.label(0x8137, 'init_vectors_and_copy')


d.subroutine(0x81DF, 'svc_13_select_nfs', title='Select NFS as active filing system (INIT)', description="""Reached from service &12 (select FS) with Y=5, or when *NET command
selects NFS. Notifies the current FS of shutdown via FSCV A=6 —
this triggers the outgoing FS to save its context back to its
workspace page, allowing restoration if re-selected later (the
FSDIE handoff mechanism). Then sets up the standard OS vector
indirections (FILEV through FSCV) to NFS entry points, claims the
extended vector table entries, and issues service &0F (vectors
claimed) to notify other ROMs. If nfs_temp is zero (auto-boot
not inhibited), injects the synthetic command "I .BOOT" through
the command decoder to trigger auto-boot login.""")
d.comment(0x81DF, 'Notify current FS of shutdown (FSCV A=6)', align=Align.INLINE)
d.comment(0x81E2, 'C=1 for ROR', align=Align.INLINE)
d.comment(0x81E3, 'Set bit 7 of l00a8 (inhibit auto-boot)', align=Align.INLINE)
d.comment(0x81E5, 'Claim OS vectors, issue service &0F', align=Align.INLINE)
d.comment(0x81E8, 'Y=&1D: top of FS state range', align=Align.INLINE)
d.comment(0x81EA, 'Copy FS state from RX buffer...', align=Align.INLINE)
d.comment(0x81EC, '...to workspace (offsets &15-&1D)', align=Align.INLINE)
d.comment(0x81EF, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x81F0, 'Loop until offset &14 done', align=Align.INLINE)
d.comment(0x81F2, 'Continue loop', align=Align.INLINE)
d.comment(0x81F4, 'ALWAYS branch to init_fs_vectors', align=Align.INLINE)


d.subroutine(0x8216, 'check_boot_key', title='Check boot key', description="""Checks if the pressed key (in A) is 'N' (matrix address &55). If
not 'N', returns to the MOS without claiming the service call
(another ROM may boot instead). If 'N', forgets the keypress via
OSBYTE &78 and falls through to print_station_info.""")
d.comment(0x8216, "XOR with &55: result=0 if key is 'N'", align=Align.INLINE)
d.comment(0x8218, "Not 'N': return without claiming", align=Align.INLINE)
d.comment(0x821B, 'OSBYTE &78: clear key-pressed state', align=Align.INLINE)


d.subroutine(0x8220, 'print_station_info', title='Print station identification', description="""Prints "Econet Station <n>" using the station number from the net
receive buffer, then tests ADLC SR2 for the network clock signal —
prints " No Clock" if absent. Falls through to init_fs_vectors.""")
d.comment(0x8220, "Print 'Econet Station ' banner", align=Align.INLINE)
d.comment(0x8223, '"Econet Station " inline string data', align=Align.INLINE)
d.comment(0x8232, 'Y=&14: station number offset in RX buf', align=Align.INLINE)
d.comment(0x8234, 'Load station number', align=Align.INLINE)
d.comment(0x8236, 'Print as 3-digit decimal', align=Align.INLINE)
d.comment(0x8239, 'BIT trick: bit 5 of SR2 = clock present', align=Align.INLINE)
d.comment(0x823B, 'Test DCD: clock present if bit 5 clear', align=Align.INLINE)
d.comment(0x823E, 'Clock present: skip warning', align=Align.INLINE)
d.comment(0x8240, "Print ' No Clock' warning", align=Align.INLINE)
d.comment(0x8243, '" No Clock" inline string data', align=Align.INLINE)
d.comment(0x824C, 'NOP (padding after inline string)', align=Align.INLINE)
d.comment(0x824D, 'Print two CRs (blank line)', align=Align.INLINE)
d.comment(0x8250, 'CR CR inline string data', align=Align.INLINE)


d.subroutine(0x8252, 'init_fs_vectors', title='Initialise filing system vectors', description="""Copies 14 bytes from l8288 (&8288) into FILEV-FSCV (&0212),
setting all 7 filing system vectors to the extended vector dispatch
addresses (&FF1B-&FF2D). Calls setup_rom_ptrs_netv to install the
ROM pointer table entries with the actual NFS handler addresses. Also
reached directly from svc_13_select_nfs, bypassing the station display.
Falls through to issue_vectors_claimed.""")
d.comment(0x8252, 'Copy 14 bytes: FS vector addresses to FILEV-FSCV', align=Align.INLINE)
d.comment(0x8254, 'Load extended vector dispatch address', align=Align.INLINE)
d.comment(0x8257, 'Write to FILEV-FSCV vector table', align=Align.INLINE)
d.comment(0x825A, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x825B, 'Loop until all 14 bytes copied', align=Align.INLINE)
d.comment(0x825D, 'Read ROM ptr table addr, install NETV', align=Align.INLINE)
d.comment(0x8260, 'Install 7 handler entries in ROM ptr table', align=Align.INLINE)
d.comment(0x8262, '7 FS vectors to install', align=Align.INLINE)
d.comment(0x8264, 'Install each 3-byte vector entry', align=Align.INLINE)
d.comment(0x8267, 'X=0 after loop; store as workspace offset', align=Align.INLINE)
d.string(0x8280, 6)
d.comment(0x827C, """Synthetic auto-boot command string. "I " does not match any
entry in NFS's local command table — "I." requires a dot, and
"I AM" requires 'A' after the space — so fscv_3_star_cmd
forwards the entire string to the fileserver, which executes
the .BOOT file.""")


d.subroutine(0x8286, 'fs_vector_addrs', title='FS vector dispatch and handler addresses (34 bytes)', description="""Bytes 0-13: extended vector dispatch addresses, copied to
FILEV-FSCV (&0212) by init_fs_vectors. Each 2-byte pair is
a dispatch address (&FF1B-&FF2D) that the MOS uses to look up
the handler in the ROM pointer table.

Bytes 14-33: handler address pairs read by store_rom_ptr_pair.
Each entry has addr_lo, addr_hi, then a padding byte that is
not read at runtime (store_rom_ptr_pair writes the current ROM
bank number without reading). The last entry (FSCV) has no
padding byte.""")
d.byte(0x8286, 2)
d.comment(0x8286, 'Auto-boot string tail / vector table header', align=Align.INLINE)
for i, name in enumerate(['FILEV', 'ARGSV', 'BGETV', 'BPUTV', 'GBPBV', 'FINDV', 'FSCV']):
    addr = 0x8288 + i * 2
    d.word(addr)
    d.comment(addr, f'{name} dispatch (&FF{0x1B + i * 3:02X})', align=Align.INLINE)
handler_names = [('FILEV', 0x86FA), ('ARGSV', 0x8956), ('BGETV', 0x8551), ('BPUTV', 0x8401), ('GBPBV', 0x8A60), ('FINDV', 0x89C6), ('FSCV', 0x80D0)]
for i, (name, handler_addr) in enumerate(handler_names):
    base_addr = 0x8296 + i * 3
    d.word(base_addr)
    d.comment(base_addr, f'{name} handler (&{handler_addr:04X})', align=Align.INLINE)
    if i < 6:
        d.byte(base_addr + 2, 1)
        d.comment(base_addr + 2, '(ROM bank — not read)', align=Align.INLINE)


d.subroutine(0x82AA, 'svc_1_abs_workspace', title='Service 1: claim absolute workspace', description="""Claims pages up to &10 for NMI workspace (&0D), FS state (&0E),
and FS command buffer (&0F). If Y >= &10, workspace already
allocated — returns unchanged.""", on_entry={'y': 'current top of absolute workspace'}, on_exit={'y': 'updated top of absolute workspace (max of input and &10)'})
d.comment(0x82AA, 'Already at page &10 or above?', align=Align.INLINE)
d.comment(0x82AC, 'Yes: nothing to claim', align=Align.INLINE)
d.comment(0x82AE, 'Claim pages &0D-&0F (3 pages)', align=Align.INLINE)


d.subroutine(0x82B3, 'svc_2_private_workspace', title='Service 2: claim private workspace and initialise NFS', description="""Y = next available workspace page on entry.
Sets up net_rx_ptr (Y) and nfs_workspace (Y+1) page pointers.
On soft break (OSBYTE &FD returns 0): skips FS state init,
preserving existing login state, file server selection, and
control block configuration — this is why pressing BREAK
keeps the user logged in.
On power-up/CTRL-BREAK (result non-zero):
  - Sets FS server station to &FE (no server selected)
  - Sets printer server station to &FE (no server selected)
  - Clears FS handles, OPT byte, message flag, SEQNOS
  - Initialises all RXCBs with &3F flag (available)
In both cases: reads station ID from &FE18 (only valid during
reset), calls adlc_init, enables user-level RX (LFLAG=&40).""", on_entry={'y': 'next available workspace page'}, on_exit={'y': 'next available workspace page after NFS (input + 2)'})
d.comment(0x82B3, 'RX buffer page = first claimed page', align=Align.INLINE)
d.comment(0x82B5, 'Advance to next page', align=Align.INLINE)
d.comment(0x82B6, 'Workspace page = second claimed page', align=Align.INLINE)
d.comment(0x82B8, 'A=0 for clearing workspace', align=Align.INLINE)
d.comment(0x82BA, 'Y=4: remote status offset', align=Align.INLINE)
d.comment(0x82BC, 'Clear status byte in net receive buffer', align=Align.INLINE)
d.comment(0x82BE, 'Y=&FF: used for later iteration', align=Align.INLINE)
d.comment(0x82C0, 'Clear RX ptr low byte', align=Align.INLINE)
d.comment(0x82C2, 'Clear workspace ptr low byte', align=Align.INLINE)
d.comment(0x82C4, 'Clear RXCB iteration counter', align=Align.INLINE)
d.comment(0x82C6, 'Clear TX semaphore (no TX in progress)', align=Align.INLINE)
d.comment(0x82C9, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x82CA, 'OSBYTE &FD: read type of last reset', align=Align.INLINE)
d.comment(0x82CF, 'X = break type from OSBYTE result', align=Align.INLINE)
d.comment(0x82D0, 'Soft break (X=0): skip FS init', align=Align.INLINE)
d.comment(0x82D2, 'Y=&15: printer station offset in RX buffer', align=Align.INLINE)
d.comment(0x82D4, '&FE = no server selected', align=Align.INLINE)
d.comment(0x82D6, 'Station &FE = no server selected', align=Align.INLINE)
d.comment(0x82D9, 'Store &FE at printer station offset', align=Align.INLINE)
d.comment(0x82DB, 'A=0 for clearing workspace fields', align=Align.INLINE)
d.comment(0x82DD, 'Clear network number', align=Align.INLINE)
d.comment(0x82E0, 'Clear protection status', align=Align.INLINE)
d.comment(0x82E3, 'Clear message flag', align=Align.INLINE)
d.comment(0x82E6, 'Clear boot option', align=Align.INLINE)
d.comment(0x82E9, 'Y=&16', align=Align.INLINE)
d.comment(0x82EA, 'Clear net number at RX buffer offset &16', align=Align.INLINE)
d.comment(0x82EC, 'Init printer server: station &FE, net 0', align=Align.INLINE)
d.comment(0x82EE, 'Store net 0 at workspace offset 3', align=Align.INLINE)
d.comment(0x82F0, 'Y=2: printer station offset', align=Align.INLINE)
d.comment(0x82F1, '&FE = no printer server', align=Align.INLINE)
d.comment(0x82F3, 'Store &FE at printer station in workspace', align=Align.INLINE)
d.comment(0x82F5, 'Load RXCB counter', align=Align.INLINE)
d.comment(0x82F7, 'Convert to workspace byte offset', align=Align.INLINE)
d.comment(0x82FA, 'C=1: past max handles, done', align=Align.INLINE)
d.comment(0x82FC, 'Mark RXCB as available', align=Align.INLINE)
d.comment(0x82FE, 'Write &3F flag to workspace', align=Align.INLINE)
d.comment(0x8300, 'Next RXCB number', align=Align.INLINE)
d.comment(0x8302, 'Loop for all RXCBs', align=Align.INLINE)
d.comment(0x8304, 'Read station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x8307, 'Y=&14: station ID offset in RX buffer', align=Align.INLINE)
d.comment(0x8309, 'Store our station number', align=Align.INLINE)
d.comment(0x830B, 'Initialise ADLC hardware', align=Align.INLINE)
d.comment(0x830E, 'Enable user-level RX (LFLAG=&40)', align=Align.INLINE)
d.comment(0x8310, 'Store to rx_flags', align=Align.INLINE)


d.subroutine(0x820B, 'svc_3_autoboot', title='Service 3: auto-boot', description="""Notifies current FS of shutdown via FSCV A=6. Scans keyboard
(OSBYTE &7A): if no key is pressed, auto-boot proceeds directly
via print_station_info. If a key is pressed, falls through to
check_boot_key: the 'N' key (matrix address &55) proceeds with
auto-boot, any other key causes the auto-boot to be declined.""")
d.comment(0x820B, 'Notify current FS of shutdown', align=Align.INLINE)
d.comment(0x820E, 'OSBYTE &7A: scan keyboard', align=Align.INLINE)
d.comment(0x8214, 'No key pressed: proceed with auto-boot', align=Align.INLINE)


d.subroutine(0x819C, 'svc_dispatch_epilogue', title='Service dispatch epilogue', description="""Common return path for all dispatched service handlers.
Restores rom_svc_num from the stack (pushed by dispatch_service),
transfers X (ROM number) to A, then returns via RTS.""")
d.comment(0x819C, 'Restore saved A from service dispatch', align=Align.INLINE)
d.comment(0x819D, 'Save to workspace &A9', align=Align.INLINE)
d.comment(0x819F, 'Return ROM number in A', align=Align.INLINE)
d.comment(0x81A0, 'Restore X from MOS ROM select copy', align=Align.INLINE)
d.comment(0x81A3, 'ROM offset for "ROFF" (copyright suffix)', align=Align.INLINE)
d.comment(0x81A5, 'Try matching *ROFF command', align=Align.INLINE)
d.comment(0x81A8, 'No match: try *NET', align=Align.INLINE)


d.subroutine(0x81F6, 'svc_9_help', title='Service 9: *HELP', description='Prints the ROM identification string using print_inline.', on_exit={'y': 'workspace page number (from ws_page)'})
d.comment(0x81F6, 'Print ROM identification string', align=Align.INLINE)
d.comment(0x81F9, '"NFS 3.65" version string + CRs', align=Align.INLINE)
d.comment(0x8203, 'Restore Y (workspace page number)', align=Align.INLINE)
d.comment(0x8205, 'Return (service not claimed)', align=Align.INLINE)

d.label(0x8350, 'match_rom_string')
d.comment(0x8350, 'Y = saved text pointer offset', align=Align.INLINE)
d.comment(0x8352, 'Load next input character', align=Align.INLINE)
d.comment(0x8354, "Is it a '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8356, 'Yes: skip to space skipper (match)', align=Align.INLINE)
d.comment(0x8358, 'Force uppercase (clear bit 5)', align=Align.INLINE)
d.comment(0x835A, 'Input char is NUL/space: check ROM byte', align=Align.INLINE)
d.comment(0x835C, 'Compare with ROM string byte', align=Align.INLINE)
d.comment(0x835F, 'Mismatch: check if ROM string ended', align=Align.INLINE)
d.comment(0x8361, 'Advance input pointer', align=Align.INLINE)
d.comment(0x8362, 'Advance ROM string pointer', align=Align.INLINE)
d.comment(0x8363, 'Continue matching (always taken)', align=Align.INLINE)
d.comment(0x8365, 'Load ROM string byte at match point', align=Align.INLINE)
d.comment(0x8368, 'Zero = end of ROM string = full match', align=Align.INLINE)
d.comment(0x836A, 'Non-zero = partial/no match; Z=0', align=Align.INLINE)
d.comment(0x836B, 'Skip this space', align=Align.INLINE)
d.comment(0x836C, 'Load next input character', align=Align.INLINE)
d.comment(0x836E, 'Is it a space?', align=Align.INLINE)
d.comment(0x8370, 'Yes: keep skipping', align=Align.INLINE)
d.comment(0x8372, 'XOR with CR: Z=1 if end of line', align=Align.INLINE)


d.subroutine(0x8206, 'call_fscv_shutdown', title='Notify filing system of shutdown', description="""Loads A=6 (FS shutdown notification) and JMP (FSCV).
The FSCV handler's RTS returns to the caller of this routine
(JSR/JMP trick saves one level of stack).""")
d.comment(0x8206, 'FSCV reason 6 = FS shutdown', align=Align.INLINE)
d.comment(0x8208, 'Tail-call via filing system control vector', align=Align.INLINE)


d.subroutine(0x8269, 'issue_vectors_claimed', title="Issue 'vectors claimed' service and optionally auto-boot", description="""Issues service &0F (vectors claimed) via OSBYTE &8F, then
service &0A. If l00a8 is zero (soft break — RXCBs already
initialised), sets up the command string "I .BOOT" at &828E
and jumps to the FSCV 3 unrecognised-command handler (which
matches against the command table at &8C4B). The "I." prefix
triggers the catch-all entry which forwards the command to
the fileserver. Falls through to run_fscv_cmd.""")
d.comment(0x8272, 'Issue service &0A', align=Align.INLINE)
d.comment(0x8275, 'Non-zero after hard reset: skip auto-boot', align=Align.INLINE)
d.comment(0x8279, 'X = lo byte of auto-boot string at &8292', align=Align.INLINE)


d.subroutine(0x827B, 'run_fscv_cmd', title='Run FSCV command from ROM', description="""Sets Y to the ROM page high byte (&82) and jumps to fscv_3_star_cmd
to execute the command string at (X, Y). X is pre-loaded by the
caller with the low byte of the string address. Also used as a
data base address by store_rom_ptr_pair for Y-indexed access to
the handler address table.""")


d.subroutine(0x8313, 'setup_rom_ptrs_netv', title='Set up ROM pointer table and NETV', description="""Reads the ROM pointer table base address via OSBYTE &A8, stores
it in osrdsc_ptr (&F6). Sets NETV low byte to &36. Then copies
one 3-byte extended vector entry (addr=&9080, rom=current) into
the ROM pointer table at offset &36, installing osword_dispatch
as the NETV handler.""")
d.comment(0x8313, 'OSBYTE &A8: read ROM pointer table address', align=Align.INLINE)
d.comment(0x8315, 'X=0: read low byte', align=Align.INLINE)
d.comment(0x8317, 'Y=&FF: read high byte', align=Align.INLINE)
d.comment(0x8319, 'Returns table address in X (lo) Y (hi)', align=Align.INLINE)
d.comment(0x831C, 'Store table base address low byte', align=Align.INLINE)
d.comment(0x831E, 'Store table base address high byte', align=Align.INLINE)
d.comment(0x8320, 'NETV extended vector offset in ROM ptr table', align=Align.INLINE)
d.comment(0x8322, 'Set NETV low byte = &36 (vector dispatch)', align=Align.INLINE)
d.comment(0x8325, 'Install 1 entry (NETV) in ROM ptr table', align=Align.INLINE)
d.comment(0x8327, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x832A, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x832C, 'Next byte', align=Align.INLINE)
d.comment(0x832D, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x8330, 'Store to ROM pointer table', align=Align.INLINE)
d.comment(0x8332, 'Next byte', align=Align.INLINE)
d.comment(0x8333, 'Write current ROM bank number', align=Align.INLINE)
d.comment(0x8335, 'Store ROM number to ROM pointer table', align=Align.INLINE)
d.comment(0x8337, 'Advance to next entry position', align=Align.INLINE)
d.comment(0x8338, 'Count down entries', align=Align.INLINE)
d.comment(0x8339, 'Loop until all entries installed', align=Align.INLINE)
d.comment(0x833B, 'Y = workspace high byte + 1 = next free page', align=Align.INLINE)
d.comment(0x833D, 'Advance past workspace page', align=Align.INLINE)
d.comment(0x833E, 'Return; Y = page after NFS workspace', align=Align.INLINE)


d.subroutine(0x836C, 'skip_spaces', title='Skip spaces and test for end of line', description="""Advances Y past leading spaces in the text at (os_text_ptr),Y.
Returns Z=1 if the next non-space character is CR (end of line),
Z=0 otherwise with A holding the character.""", on_entry={'y': 'offset into (os_text_ptr) buffer'}, on_exit={'a': 'character EOR &0D (0 if CR)', 'y': 'offset of first non-space character', 'z': 'set if end of line (CR)'})


d.subroutine(0x8375, 'init_tx_reply_port', title='Initialise TX control block for FS reply on port &90', description="""Loads port &90 (PREPLY) into A, calls init_tx_ctrl_block to set
up the TX control block, stores the port and control bytes, then
decrements the control flag. Used by send_fs_reply_cmd to prepare
for receiving the fileserver's reply.""")
d.comment(0x8375, 'A=&90: FS reply port (PREPLY)', align=Align.INLINE)
d.comment(0x8377, 'Init TXCB from template', align=Align.INLINE)
d.comment(0x837A, 'Store port number in TXCB', align=Align.INLINE)
d.comment(0x837C, 'Control byte: 3 = transmit', align=Align.INLINE)
d.comment(0x837E, 'Store control byte in TXCB', align=Align.INLINE)
d.comment(0x8380, 'Decrement TXCB flag to arm TX', align=Align.INLINE)


d.subroutine(0x833F, 'fscv_6_shutdown', title='FSCV 6: Filing system shutdown / save state (FSDIE)', description="""Called when another filing system (e.g. DFS) is selected. Saves
the current NFS context (FSLOCN station number, URD/CSD/LIB
handles, OPT byte, etc.) from page &0E into the dynamic workspace
backup area. This allows the state to be restored when *NET is
re-issued later, without losing the login session. Finally calls
OSBYTE &77 (close SPOOL/EXEC files) to release the
Econet network printer on FS switch.""")
d.comment(0x833F, 'Copy 10 bytes: FS state to workspace backup', align=Align.INLINE)
d.comment(0x8347, 'Offsets &15-&1D: server, handles, OPT, etc.', align=Align.INLINE)


d.subroutine(0x8383, 'init_tx_ctrl_block', title='Initialise TX control block at &00C0 from template', description="""Copies 12 bytes from tx_ctrl_template (&839B) to &00C0.
For the first 2 bytes (Y=0,1), also copies the fileserver
station/network from &0E00/&0E01 to &00C2/&00C3.
The template sets up: control=&80, port=&99 (FS command port),
command data length=&0F, plus padding bytes.""", on_exit={'a': 'preserved', 'y': '&FF (decremented past 0)'})
d.comment(0x8383, 'Preserve A across call', align=Align.INLINE)
d.comment(0x8384, 'Copy 12 bytes (Y=11..0)', align=Align.INLINE)
d.comment(0x8386, 'Load template byte', align=Align.INLINE)
d.comment(0x8389, 'Store to TX control block at &00C0', align=Align.INLINE)
d.comment(0x838C, 'Y < 2: also copy FS server station/network', align=Align.INLINE)
d.comment(0x838E, 'Skip station/network copy for Y >= 2', align=Align.INLINE)
d.comment(0x8390, 'Load FS server station (Y=0) or network (Y=1)', align=Align.INLINE)
d.comment(0x8393, 'Store to dest station/network at &00C2', align=Align.INLINE)
d.comment(0x8396, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8397, 'Loop until all 12 bytes copied', align=Align.INLINE)
d.comment(0x8399, 'Restore A', align=Align.INLINE)
d.comment(0x839A, 'Return', align=Align.INLINE)


d.subroutine(0x839B, 'tx_ctrl_template', title='TX control block template (TXTAB, 12 bytes)', description="""12-byte template copied to &00C0 by init_tx_ctrl. Defines the
TX control block for FS commands: control flag, port, station/
network, and data buffer pointers (&0F00-&0FFF). The 4-byte
Econet addresses use only the low 2 bytes; upper bytes are &FF.""")
d.comment(0x83A7, 'Save flag byte for command', align=Align.INLINE)
d.comment(0x83A8, 'C=1: include flag in FS command', align=Align.INLINE)
d.comment(0x83A9, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)
d.comment(0x83AB, 'V=0: command has no flag byte', align=Align.INLINE)
d.comment(0x83AC, 'ALWAYS branch to prepare_fs_cmd', align=Align.INLINE)


d.subroutine(0x83B5, 'prepare_fs_cmd', title='Prepare FS command buffer (12 references)', description="""Builds the 5-byte FS protocol header at &0F00:
  &0F00 HDRREP = reply port (set downstream, typically &90/PREPLY)
  &0F01 HDRFN  = Y parameter (function code)
  &0F02 HDRURD = URD handle (from &0E02)
  &0F03 HDRCSD = CSD handle (from &0E03)
  &0F04 HDRLIB = LIB handle (from &0E04)
Command-specific data follows at &0F05 (TXBUF). Also clears V flag.
Called before building specific FS commands for transmission.""", on_entry={'y': 'function code for HDRFN', 'x': 'preserved through header build'}, on_exit={'a': '0 on success (from build_send_fs_cmd)', 'x': '0 on success, &D6 on not-found', 'y': '1 (offset past command code in reply)'})
d.comment(0x83B5, 'V=0: standard FS command path', align=Align.INLINE)
d.comment(0x83B6, 'Copy URD handle from workspace to buffer', align=Align.INLINE)
d.comment(0x83B9, 'Store URD at &0F02', align=Align.INLINE)
d.comment(0x83BC, 'CLC: no byte-stream path', align=Align.INLINE)
d.comment(0x83BD, 'Store function code at &0F01', align=Align.INLINE)
d.comment(0x83C0, 'Y=1: copy CSD (offset 1) then LIB (offset 0)', align=Align.INLINE)
d.comment(0x83C2, 'Copy CSD and LIB handles to command buffer', align=Align.INLINE)
d.comment(0x83C5, 'Store at &0F03 (CSD) and &0F04 (LIB)', align=Align.INLINE)
d.comment(0x83C8, 'Y=function code', align=Align.INLINE)
d.comment(0x83C9, 'Loop for both handles', align=Align.INLINE)


d.subroutine(0x83CB, 'build_send_fs_cmd', title='Build and send FS command (DOFSOP)', description="""Sets reply port to &90 (PREPLY) at &0F00, initialises the TX
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
command code to read the return code. Error &D6 ("not found")
is detected via ADC #(&100-&D6) with C=0 -- if the return code
was exactly &D6, the result wraps to zero (Z=1). This is a
branchless comparison returning C=1, A=0 as a soft error that
callers can handle, vs hard errors which go through FSERR.""", on_entry={'x': 'buffer extent (command-specific data bytes)', 'y': 'function code', 'c': '0 for standard FS path, 1 for byte-stream (BSXMIT)'}, on_exit={'a': '0 on success', 'x': '0 on success, &D6 on not-found', 'y': '1 (offset past command code in reply)'})
d.comment(0x83CB, 'Save carry (FS path vs byte-stream)', align=Align.INLINE)
d.comment(0x83CC, 'Reply port &90 (PREPLY)', align=Align.INLINE)
d.comment(0x83CE, 'Store at &0F00 (HDRREP)', align=Align.INLINE)
d.comment(0x83D1, 'Copy TX template to &00C0', align=Align.INLINE)
d.comment(0x83D4, 'A = X (buffer extent)', align=Align.INLINE)
d.comment(0x83D5, 'HPTR = header (5) + data (X) bytes to send', align=Align.INLINE)
d.comment(0x83D7, 'Store to TXCB end-pointer low', align=Align.INLINE)
d.comment(0x83D9, 'Restore carry flag', align=Align.INLINE)
d.comment(0x83DA, 'C=1: byte-stream path (BSXMIT)', align=Align.INLINE)
d.comment(0x83DC, 'Save flags for send_fs_reply_cmd', align=Align.INLINE)
d.comment(0x83DD, 'Point net_tx_ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x83E0, 'Restore flags', align=Align.INLINE)
d.comment(0x83E1, 'Save flags (V flag state)', align=Align.INLINE)
d.comment(0x83E2, 'Set up RX wait for FS reply', align=Align.INLINE)
d.comment(0x83E5, 'Transmit and wait (BRIANX)', align=Align.INLINE)
d.comment(0x83E8, 'Restore flags', align=Align.INLINE)
d.comment(0x83E9, 'Y=1: skip past command code byte', align=Align.INLINE)
d.comment(0x83EA, 'Load return code from FS reply', align=Align.INLINE)
d.comment(0x83EC, 'X = return code', align=Align.INLINE)
d.comment(0x83ED, 'Zero: success, return', align=Align.INLINE)
d.comment(0x83EF, 'V=0: standard path, error is fatal', align=Align.INLINE)
d.comment(0x83F1, 'ADC #&2A: test for &D6 (not found)', align=Align.INLINE)
d.comment(0x83F3, 'Non-zero: hard error, go to FSERR', align=Align.INLINE)
d.comment(0x83F5, 'Return (success or soft &D6 error)', align=Align.INLINE)
d.comment(0x83F6, 'Discard saved flags from stack', align=Align.INLINE)
d.comment(0x83F7, 'X=&C0: TXCB address for byte-stream TX', align=Align.INLINE)
d.comment(0x83F9, 'Y++ past command code', align=Align.INLINE)
d.comment(0x83FA, 'Byte-stream transmit with retry', align=Align.INLINE)
d.comment(0x83FD, 'Store result to &B3', align=Align.INLINE)
d.comment(0x83FF, 'C=0: success, check reply code', align=Align.INLINE)


d.subroutine(0x8468, 'store_fs_error', title='Handle fileserver error replies (FSERR)', description="""The fileserver returns errors as: zero command code + error number +
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
d.comment(0x8468, 'Remember raw FS error code', align=Align.INLINE)
d.comment(0x846B, 'Y=1: point to error number byte in reply', align=Align.INLINE)
d.comment(0x846D, 'Clamp FS errors below &A8 to standard &A8', align=Align.INLINE)
d.comment(0x846F, 'Error >= &A8: keep original value', align=Align.INLINE)
d.comment(0x8471, 'Error < &A8: override with standard &A8', align=Align.INLINE)
d.comment(0x8473, 'Write clamped error number to reply buffer', align=Align.INLINE)
d.comment(0x8475, 'Start scanning from offset &FF (will INY to 0)', align=Align.INLINE)
d.comment(0x8477, 'Next byte in reply buffer', align=Align.INLINE)
d.comment(0x8478, 'Copy reply buffer to &0100 for BRK execution', align=Align.INLINE)
d.comment(0x847A, 'Build BRK error block at &0100', align=Align.INLINE)
d.comment(0x847D, 'Scan for CR terminator (&0D)', align=Align.INLINE)
d.comment(0x847F, 'Continue until CR found', align=Align.INLINE)
d.comment(0x8481, 'Replace CR with zero = BRK error block end', align=Align.INLINE)
d.comment(0x8484, 'Execute as BRK error block at &0100; ALWAYS', align=Align.INLINE)


d.subroutine(0x8402, 'bgetv_entry', title='BGETV entry point', description="""Clears the escapable flag via clear_escapable, then falls
through to handle_bput_bget with carry set (SEC by caller)
to indicate a BGET operation.""", on_entry={'y': 'file handle', 'c': '1 (set by MOS before calling BGETV)'}, on_exit={'a': 'byte read from file', 'c': '1 if EOF, 0 otherwise'})


d.subroutine(0x848F, 'check_escape', title='Check for pending escape condition', description="""Tests bit 7 of the MOS escape flag (&FF) ANDed with the
escapable flag. If no escape is pending, returns immediately.
If escape is active, acknowledges it via OSBYTE &7E and jumps
to the escape error handler.""", on_exit={'a': 'corrupted (AND result on normal return)'})


d.subroutine(0x8405, 'handle_bput_bget', title='Handle BPUT/BGET file byte I/O', description="""BPUTV enters at &8413 (CLC; fall through) and BGETV enters
at &8551 (SEC; JSR here). The carry flag is preserved via
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
d.comment(0x840E, 'Save handle for SPOOL/EXEC comparison later', align=Align.INLINE)
d.comment(0x8418, '&90 = data port (PREPLY)', align=Align.INLINE)
d.comment(0x8420, 'CB reply buffer at &0FDC', align=Align.INLINE)
d.comment(0x8424, 'Error buffer at &0FE0', align=Align.INLINE)
d.comment(0x842B, 'Restore C: selects BPUT (0) vs BGET (1)', align=Align.INLINE)
d.comment(0x843C, 'Zero reply = success, skip error handling', align=Align.INLINE)
d.comment(0x843E, 'Copy 32-byte reply to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x844A, 'A=&C6: read *EXEC file handle', align=Align.INLINE)
d.comment(0x844F, '\')\': offset into "SP." string at &8529', align=Align.INLINE)
d.comment(0x8451, 'Y=value of *SPOOL file handle', align=Align.INLINE)
d.comment(0x8455, 'A=&1B: low byte of "E." string address', align=Align.INLINE)
d.comment(0x8457, 'X=value of *EXEC file handle', align=Align.INLINE)
d.comment(0x845C, 'Y=&85: high byte of OSCLI string in ROM', align=Align.INLINE)
d.comment(0x845E, 'Close SPOOL/EXEC via "*SP." or "*E."', align=Align.INLINE)
d.comment(0x8461, 'Reset CB pointer to error buffer at &0FE0', align=Align.INLINE)
d.comment(0x8405, 'Save A (BPUT byte) on stack', align=Align.INLINE)
d.comment(0x8406, 'Also save byte at &0FDF for BSXMIT', align=Align.INLINE)
d.comment(0x8409, 'Transfer X for stack save', align=Align.INLINE)
d.comment(0x840A, 'Save X on stack', align=Align.INLINE)
d.comment(0x840B, 'Transfer Y (handle) for stack save', align=Align.INLINE)
d.comment(0x840C, 'Save Y (handle) on stack', align=Align.INLINE)
d.comment(0x840D, 'Save P (C = BPUT/BGET selector) on stack', align=Align.INLINE)
d.comment(0x8410, 'Convert handle Y to single-bit mask', align=Align.INLINE)
d.comment(0x8413, 'Store handle bitmask at &0FDE', align=Align.INLINE)
d.comment(0x8416, 'Store handle bitmask for sequence tracking', align=Align.INLINE)
d.comment(0x841A, 'Store reply port in command buffer', align=Align.INLINE)
d.comment(0x841D, 'Set up 12-byte TXCB from template', align=Align.INLINE)
d.comment(0x8422, 'Store reply buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x8426, 'Store error buffer ptr low in TXCB', align=Align.INLINE)
d.comment(0x8428, 'Y=1 (from init_tx_ctrl_block exit)', align=Align.INLINE)
d.comment(0x8429, 'X=9: BPUT function code', align=Align.INLINE)
d.comment(0x842C, 'C=0 (BPUT): keep X=9', align=Align.INLINE)
d.comment(0x842F, 'Store function code at &0FDD', align=Align.INLINE)
d.comment(0x8432, 'Load handle bitmask for BSXMIT', align=Align.INLINE)
d.comment(0x8434, 'X=&C0: TXCB address for econet_tx_retry', align=Align.INLINE)
d.comment(0x8436, 'Transmit via byte-stream protocol', align=Align.INLINE)
d.comment(0x8439, 'Load reply byte from buffer', align=Align.INLINE)
d.comment(0x8440, 'Load reply byte at offset Y', align=Align.INLINE)
d.comment(0x8443, 'Store to error buffer at &0FE0+Y', align=Align.INLINE)
d.comment(0x8446, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8447, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x8453, 'Handle matches SPOOL -- close it', align=Align.INLINE)
d.comment(0x8459, 'No EXEC match -- skip close', align=Align.INLINE)
d.comment(0x845B, 'X = string offset for OSCLI close', align=Align.INLINE)
d.comment(0x8463, 'Reset reply ptr to error buffer', align=Align.INLINE)
d.comment(0x8465, 'Reload reply byte for error dispatch', align=Align.INLINE)


d.subroutine(0x851E, 'waitfs', title="Load '*' prefix and send FS command (WAITFS)", description="""Loads A with &2A ('*') as the FS command prefix byte, then
falls through to send_to_fs to perform a full fileserver
transaction: transmit and wait for reply.""", on_exit={'a': 'reply command code'})


d.subroutine(0x8645, 'clear_escapable', title='Clear escapable flag preserving processor status', description="""PHP/LSR escapable/PLP: clears bit 7 of the escapable flag
while preserving the processor status register. Used at the
start of FS vector operations to mark them as not yet
escapable.""")


d.subroutine(0x8520, 'send_to_fs', title='Send command to fileserver and handle reply (WAITFS)', description="""Performs a complete FS transaction: transmit then wait for reply.
Sets bit 7 of rx_flags (mark FS transaction in progress),
builds a TX frame from the data at (net_tx_ptr), and transmits
it. The system RX flag (LFLAG bit 7) is only set when receiving
into the page-zero control block — if RXCBP's high byte is
non-zero, setting the system flag would interfere with other RX
operations. The timeout counter uses the stack (indexed via TSX)
rather than memory to avoid bus conflicts with Econet hardware
during the tight polling loop. Handles multi-block replies and
checks for escape conditions between blocks.""", on_entry={'a': 'function code / command prefix byte'}, on_exit={'a': 'reply command code'})
d.comment(0x8520, 'Save function code on stack', align=Align.INLINE)
d.comment(0x8521, 'Load current rx_flags', align=Align.INLINE)
d.comment(0x8524, 'Save rx_flags on stack for restore', align=Align.INLINE)
d.comment(0x8525, 'Only flag rx_flags if using page-zero CB', align=Align.INLINE)
d.comment(0x8527, 'High byte != 0: skip flag set', align=Align.INLINE)
d.comment(0x8529, 'Set bit7: FS transaction in progress', align=Align.INLINE)
d.comment(0x852B, 'Write back updated rx_flags', align=Align.INLINE)
d.comment(0x852E, 'Push two zero bytes as timeout counters', align=Align.INLINE)
d.comment(0x8530, 'First zero for timeout', align=Align.INLINE)
d.comment(0x8531, 'Second zero for timeout', align=Align.INLINE)
d.comment(0x8532, 'Y=0: index for flag byte check', align=Align.INLINE)
d.comment(0x8533, 'TSX: index stack-based timeout via X', align=Align.INLINE)
d.comment(0x8534, 'Read flag byte from TX control block', align=Align.INLINE)
d.comment(0x8536, 'Bit 7 set = reply received', align=Align.INLINE)
d.comment(0x8538, 'Three-stage nested timeout: inner loop', align=Align.INLINE)
d.comment(0x853B, 'Inner not expired: keep polling', align=Align.INLINE)
d.comment(0x853D, 'Middle timeout loop', align=Align.INLINE)
d.comment(0x8540, 'Middle not expired: keep polling', align=Align.INLINE)
d.comment(0x8542, 'Outer timeout loop (slowest)', align=Align.INLINE)
d.comment(0x8545, 'Outer not expired: keep polling', align=Align.INLINE)
d.comment(0x8547, 'Pop first timeout byte', align=Align.INLINE)
d.comment(0x8548, 'Pop second timeout byte', align=Align.INLINE)
d.comment(0x8549, 'Pop saved rx_flags into A', align=Align.INLINE)
d.comment(0x854A, 'Restore saved rx_flags from stack', align=Align.INLINE)
d.comment(0x854D, 'Pop saved function code', align=Align.INLINE)
d.comment(0x854E, 'A=saved func code; zero would mean no reply', align=Align.INLINE)
d.comment(0x8550, 'Return to caller', align=Align.INLINE)
d.comment(0x8551, 'C=1: flag for BGET mode', align=Align.INLINE)
d.comment(0x8552, 'Handle BGET via FS command', align=Align.INLINE)
d.comment(0x8555, 'SEC: set carry for error check', align=Align.INLINE)
d.comment(0x8556, 'A=&FE: mask for EOF check', align=Align.INLINE)
d.comment(0x8558, 'BIT l0fdf: test error flags', align=Align.INLINE)
d.comment(0x855B, 'V=1: error, return early', align=Align.INLINE)
d.comment(0x855D, 'CLC: no error', align=Align.INLINE)
d.comment(0x855E, 'Save flags for EOF check', align=Align.INLINE)
d.comment(0x855F, 'Load BGET result byte', align=Align.INLINE)
d.comment(0x8561, 'Restore flags', align=Align.INLINE)
d.comment(0x8562, 'Bit7 set: skip FS flag clear', align=Align.INLINE)
d.comment(0x8564, 'Clear FS flag for handle', align=Align.INLINE)

d.label(0x856E, 'error_msg_table')
d.comment(0x856E, """Econet error message table (ERRTAB, 7 entries).
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
Indexed via c84FA/nlistn/nlisne at &84FA-&850B.""")
addr = 0x8579
for _ in range(7):
    d.byte(addr, 1)
    addr = d.stringz(addr + 1)
d.comment(0x856E, 'Error &A0: Line Jammed', align=Align.INLINE)
d.comment(0x856F, '"Line Jammed" string', align=Align.INLINE)
d.comment(0x8579, 'Terminator + error &A1', align=Align.INLINE)
d.comment(0x857A, 'NUL terminator', align=Align.INLINE)
d.comment(0x857B, 'Error &A1: Net Error', align=Align.INLINE)
d.comment(0x857C, '"Net Error" string', align=Align.INLINE)
d.comment(0x8586, 'Error &A2: Not listening', align=Align.INLINE)
d.comment(0x8587, '"Not listening" string', align=Align.INLINE)
d.comment(0x8595, 'Error &A3: No Clock', align=Align.INLINE)
d.comment(0x8596, '"No Clock" string', align=Align.INLINE)
d.comment(0x859F, 'Error &11: Escape', align=Align.INLINE)
d.comment(0x85A0, '"Escape" string', align=Align.INLINE)
d.comment(0x85A7, 'Error &CB: Bad Option', align=Align.INLINE)
d.comment(0x85A8, '"Bad Option" string', align=Align.INLINE)
d.comment(0x85B3, 'Error &A5: No reply', align=Align.INLINE)
d.comment(0x85B4, '"No reply" string', align=Align.INLINE)


d.subroutine(0x81AA, 'net_4_resume_remote', title='Resume after remote operation / *ROFF handler (NROFF)', description="""Checks byte 4 of (net_rx_ptr): if non-zero, the keyboard was
disabled during a remote operation (peek/poke/boot). Clears
the flag, re-enables the keyboard via OSBYTE &C9, and sends
function &0A to notify completion. Also handles *ROFF and the
triple-plus escape sequence (+++), which resets system masks
via OSBYTE &CE and returns control to the MOS, providing an
escape route when a remote session becomes unresponsive.""")
d.comment(0x81AA, 'Y=4: offset of keyboard disable flag', align=Align.INLINE)
d.comment(0x81AC, 'Read flag from RX buffer', align=Align.INLINE)
d.comment(0x81AE, 'Zero: keyboard not disabled, skip', align=Align.INLINE)
d.comment(0x81B0, 'A=0: value to clear flag and re-enable', align=Align.INLINE)
d.comment(0x81B3, 'Clear keyboard disable flag in buffer', align=Align.INLINE)
d.comment(0x81B6, 'OSBYTE &C9: Econet keyboard disable', align=Align.INLINE)
d.comment(0x81B8, 'Re-enable keyboard (X=0, Y=0)', align=Align.INLINE)
d.comment(0x81BB, 'Function &0A: remote operation complete', align=Align.INLINE)
d.comment(0x81BD, 'Send notification to controlling station', align=Align.INLINE)
d.comment(0x81C0, 'Save X (return value from TX)', align=Align.INLINE)
d.comment(0x81C2, 'OSBYTE &CE: first system mask to reset', align=Align.INLINE)
d.comment(0x81C4, 'Restore X for OSBYTE call', align=Align.INLINE)
d.comment(0x81C6, 'Y=&7F: AND mask (clear bit 7)', align=Align.INLINE)
d.comment(0x81C8, 'Reset system mask byte', align=Align.INLINE)
d.comment(0x81CB, 'Advance to next OSBYTE (&CE -> &CF)', align=Align.INLINE)
d.comment(0x81CD, 'Reached &D0? (past &CF)', align=Align.INLINE)
d.comment(0x81CF, 'No: reset &CF too', align=Align.INLINE)
d.comment(0x81D1, 'A=0: clear remote state', align=Align.INLINE)
d.comment(0x81D3, 'Clear &A9 (service dispatch state)', align=Align.INLINE)
d.comment(0x81D5, 'Clear workspace byte', align=Align.INLINE)
d.comment(0x81D7, 'Return', align=Align.INLINE)
d.comment(0x81D8, 'X=1: ROM offset for "NET" match', align=Align.INLINE)
d.comment(0x81DA, 'Try matching *NET command', align=Align.INLINE)
d.comment(0x81DD, 'No match: return unclaimed', align=Align.INLINE)


d.subroutine(0x80D0, 'fscv_handler', title='FSCV dispatch entry', description="""Entered via the extended vector table when the MOS calls FSCV.
Stores A/X/Y via save_fscv_args, compares A (function code) against 8,
and dispatches codes 0-7 via the shared dispatch table at &8024
with base offset Y=&13 (table indices 20-27).
Function codes: 0=*OPT, 1=EOF, 2=*/, 3=unrecognised *,
4=*RUN, 5=*CAT, 6=shutdown, 7=read handles.""", on_entry={'a': 'function code (0-7)', 'x': 'depends on function', 'y': 'depends on function'}, on_exit={'a': 'depends on handler (preserved if A >= 8)', 'x': 'depends on handler (preserved if A >= 8)', 'y': 'depends on handler (preserved if A >= 8)'})
d.comment(0x80D0, 'Store A/X/Y in FS workspace', align=Align.INLINE)
d.comment(0x80D5, 'Function code >= 8? Return (unsupported)', align=Align.INLINE)
d.comment(0x80D9, 'Y=&13: base offset for FSCV dispatch (indices 20+)', align=Align.INLINE)


d.subroutine(0x86CC, 'copy_filename_ptr', title='Copy filename pointer to os_text_ptr and parse', description="""Copies the 2-byte filename pointer from (fs_options),Y into
os_text_ptr (&F2/&F3), then falls through to parse_filename_gs
to parse the filename via GSINIT/GSREAD into the &0E30 buffer.""", on_exit={'x': 'length of parsed string', 'y': '0'})


d.subroutine(0x86D8, 'parse_filename_gs_y', title='Parse filename via GSINIT/GSREAD from offset Y', description="""Sub-entry of parse_filename_gs that accepts a non-zero Y offset
into the (os_text_ptr) string. Initialises GSINIT, reads chars
via GSREAD into &0E30, CR-terminates the result, and sets up
fs_crc_lo/hi to point at the buffer.""", on_entry={'y': 'offset into (os_text_ptr) string'}, on_exit={'x': 'length of parsed string', 'y': 'preserved'})


d.subroutine(0x86D6, 'parse_filename_gs', title='Parse filename using GSINIT/GSREAD into &0E30', description="""Uses the MOS GSINIT/GSREAD API to parse a filename string from
(os_text_ptr),Y, handling quoted strings and |-escaped characters.
Stores the parsed result CR-terminated at &0E30 and sets up
fs_crc_lo/hi to point to that buffer. Sub-entry at &86D8 allows
a non-zero starting Y offset.""", on_entry={'y': 'offset into (os_text_ptr) buffer (0 at &86D6)'}, on_exit={'x': 'length of parsed string', 'y': 'preserved'})
d.comment(0x86D6, 'Start from beginning of string', align=Align.INLINE)
d.comment(0x86D8, 'X=&FF: next INX wraps to first char index', align=Align.INLINE)
d.comment(0x86DA, 'C=0 for GSINIT: parse from current position', align=Align.INLINE)
d.comment(0x86DB, 'Initialise GS string parser', align=Align.INLINE)
d.comment(0x86DE, 'Empty string: skip to CR terminator', align=Align.INLINE)
d.comment(0x86E0, 'Read next character via GSREAD', align=Align.INLINE)
d.comment(0x86E3, 'C=1 from GSREAD: end of string reached', align=Align.INLINE)
d.comment(0x86E5, 'Advance buffer index', align=Align.INLINE)
d.comment(0x86E6, 'Store parsed character to &0E30+X', align=Align.INLINE)
d.comment(0x86E9, 'ALWAYS loop (GSREAD clears C on success)', align=Align.INLINE)
d.comment(0x86EB, 'Terminate parsed string with CR', align=Align.INLINE)
d.comment(0x86EC, 'CR = &0D', align=Align.INLINE)
d.comment(0x86EE, 'Store CR terminator at end of string', align=Align.INLINE)
d.comment(0x86F1, 'Point fs_crc_lo/hi at &0E30 parse buffer', align=Align.INLINE)
d.comment(0x86F3, 'fs_crc_lo = &30', align=Align.INLINE)
d.comment(0x86F5, 'fs_crc_hi = &0E → buffer at &0E30', align=Align.INLINE)
d.comment(0x86F7, 'Store high byte', align=Align.INLINE)
d.comment(0x86F9, 'Return; X = string length', align=Align.INLINE)


d.subroutine(0x86FA, 'filev_handler', title='FILEV handler (OSFILE entry point)', description="""Calls save_fscv_args (&863B) to preserve A/X/Y, then JSR &86CC
to copy the 2-byte filename pointer from the parameter block to
os_text_ptr and fall through to parse_filename_gs (&86D6) which
parses the filename into &0E30+. Sets fs_crc_lo/hi to point at
the parsed filename buffer.
Dispatches by function code A:
  A=&FF: load file (send_fs_examine at &8710)
  A=&00: save file (filev_save at &8783)
  A=&01-&06: attribute operations (filev_attrib_dispatch at &88BF)
  Other: restore_args_return (unsupported, no-op)""", on_entry={'a': 'function code (&FF=load, &00=save, &01-&06=attrs)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'restored', 'x': 'restored', 'y': 'restored'})
d.comment(0x86FD, 'Copy filename ptr from param block to os_text_ptr', align=Align.INLINE)
d.comment(0x8700, 'Recover function code from saved A', align=Align.INLINE)
d.comment(0x8702, 'A >= 0: save (&00) or attribs (&01-&06)', align=Align.INLINE)
d.comment(0x8704, 'A=&FF? Only &FF is valid for load', align=Align.INLINE)
d.comment(0x8708, 'Unknown negative code: no-op return', align=Align.INLINE)


d.subroutine(0x8710, 'send_fs_examine', title='Send FS examine command', description="""Sends an FS examine/load command to the fileserver. The function
code in Y is set by the caller (Y=2 for load, Y=5 for examine).
Overwrites fs_cmd_urd (&0F02) with &92 (PLDATA port number) to
repurpose the URD header field for the data transfer port. Sets
escapable to &92 so escape checking is active during the transfer.
Calls prepare_cmd_clv to build the FS header (which skips the
normal URD copy, preserving &92). The FS reply contains load/exec
addresses and file length used to set up the data transfer.
Byte 6 of the parameter block selects load address handling:
non-zero uses the address from the FS reply (load to file's own
address); zero uses the caller-supplied address.""", on_entry={'y': 'FS function code (2=load, 5=examine)', 'x': 'TX buffer extent'})
d.comment(0x8710, 'Port &92 = PLDATA (data transfer port)', align=Align.INLINE)
d.comment(0x8712, 'Mark transfer as escapable', align=Align.INLINE)
d.comment(0x8714, 'Overwrite URD field with data port number', align=Align.INLINE)
d.comment(0x8717, 'Build FS header (V=1: CLV path)', align=Align.INLINE)
d.comment(0x871A, 'Y=6: param block byte 6', align=Align.INLINE)
d.comment(0x871C, "Byte 6: use file's own load address?", align=Align.INLINE)
d.comment(0x871E, 'Non-zero: use FS reply address (lodfil)', align=Align.INLINE)
d.comment(0x8720, "Zero: copy caller's load addr first", align=Align.INLINE)
d.comment(0x8723, 'Then copy FS reply to param block', align=Align.INLINE)
d.comment(0x8726, 'Carry clear from prepare_cmd_clv: skip lodfil', align=Align.INLINE)
d.comment(0x8728, 'Copy FS reply addresses to param block', align=Align.INLINE)
d.comment(0x872B, 'Then copy load addr from param block', align=Align.INLINE)
d.comment(0x872E, 'Compute end address = load + file length', align=Align.INLINE)
d.comment(0x8730, 'Load address byte', align=Align.INLINE)
d.comment(0x8732, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x8734, 'Add file length byte', align=Align.INLINE)
d.comment(0x8737, 'Store as end position', align=Align.INLINE)
d.comment(0x8739, 'Next address byte', align=Align.INLINE)
d.comment(0x873A, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x873B, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x873D, 'Adjust high byte for 3-byte length overflow', align=Align.INLINE)
d.comment(0x873E, 'Subtract 4th length byte from end addr', align=Align.INLINE)
d.comment(0x8741, 'Store adjusted end address high byte', align=Align.INLINE)
d.comment(0x8743, 'Transfer file data in &80-byte blocks', align=Align.INLINE)
d.comment(0x8746, 'Copy 3-byte file length to FS reply cmd buffer', align=Align.INLINE)
d.comment(0x8748, 'Load file length byte', align=Align.INLINE)
d.comment(0x874B, 'Store in FS command data buffer', align=Align.INLINE)
d.comment(0x874E, 'Next byte (count down)', align=Align.INLINE)
d.comment(0x874F, 'Loop for 3 bytes (X=2,1,0)', align=Align.INLINE)
d.comment(0x8751, 'ALWAYS branch', align=Align.INLINE)


d.subroutine(0x8753, 'send_data_blocks', title='Send file data in multi-block chunks', description="""Repeatedly sends &80-byte (128-byte) blocks of file data to the
fileserver using command &7F. Compares current address (&C8-&CB)
against end address (&B4-&B7) via compare_addresses, and loops
until the entire file has been transferred. Each block is sent
via send_to_fs_star.""")
d.comment(0x8756, 'Addresses match: transfer complete', align=Align.INLINE)
d.comment(0x8758, 'Port &92 for data block transfer', align=Align.INLINE)
d.comment(0x875A, 'Store port to TXCB command byte', align=Align.INLINE)
d.comment(0x875C, 'Set up next &80-byte block for transfer', align=Align.INLINE)
d.comment(0x875E, 'Swap: current addr -> source, end -> current', align=Align.INLINE)
d.comment(0x8760, 'Source addr = current position', align=Align.INLINE)
d.comment(0x8762, 'Load end address byte', align=Align.INLINE)
d.comment(0x8764, 'Dest = end address (will be clamped)', align=Align.INLINE)
d.comment(0x8766, 'Next address byte', align=Align.INLINE)
d.comment(0x8767, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8769, 'Command &7F = data block transfer', align=Align.INLINE)
d.comment(0x876B, 'Store to TXCB control byte', align=Align.INLINE)
d.comment(0x876D, 'Send this block to the fileserver', align=Align.INLINE)
d.comment(0x8770, 'Y=3: compare 4 bytes (3..0)', align=Align.INLINE)
d.comment(0x8772, 'Compare current vs end address (4 bytes)', align=Align.INLINE)
d.comment(0x8775, 'XOR with end address byte', align=Align.INLINE)
d.comment(0x8778, 'Not equal: more blocks to send', align=Align.INLINE)
d.comment(0x877A, 'Next byte', align=Align.INLINE)
d.comment(0x877B, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x877D, 'All equal: transfer complete', align=Align.INLINE)
d.comment(0x877E, 'A=0: SAVE handler', align=Align.INLINE)
d.comment(0x8780, 'A!=0: attribute dispatch (A=1-6)', align=Align.INLINE)


d.subroutine(0x8783, 'filev_save', title='OSFILE save handler (A=&00)', description="""Copies 4-byte load/exec/length addresses from the parameter block
to the FS command buffer, along with the filename. The savsiz loop
computes data-end minus data-start for each address byte to derive
the transfer length, saving both the original address and the
difference. Sends FS command with port &91, function code Y=1,
and the filename via copy_string_to_cmd. After transfer_file_blocks
sends the data, calls send_fs_reply_cmd for the final handshake.
If fs_messages_flag is set, prints the catalogue line inline:
filename (padded to 12 chars), load address, exec address, and
file length. Finally decodes the FS attributes and copies the
reply data back into the caller's parameter block.""")
d.comment(0x8783, 'Process 4 address bytes (load/exec/start/end)', align=Align.INLINE)
d.comment(0x8785, 'Y=&0E: start from end-address in param block', align=Align.INLINE)
d.comment(0x8787, 'Read end-address byte from param block', align=Align.INLINE)
d.comment(0x8789, 'Save to port workspace for transfer setup', align=Align.INLINE)
d.comment(0x878F, 'end - start = transfer length byte', align=Align.INLINE)
d.comment(0x8791, 'Store length byte in FS command buffer', align=Align.INLINE)
d.comment(0x8795, 'Read corresponding start-address byte', align=Align.INLINE)
d.comment(0x8797, 'Save to port workspace', align=Align.INLINE)
d.comment(0x879B, 'Replace param block entry with length', align=Align.INLINE)
d.comment(0x87A3, 'Copy load/exec addresses to FS command buffer', align=Align.INLINE)
d.comment(0x87AD, 'Port &91 for save command', align=Align.INLINE)
d.comment(0x87AF, 'Mark as escapable during save', align=Align.INLINE)
d.comment(0x87B1, 'Overwrite URD field with port number', align=Align.INLINE)
d.comment(0x87B6, 'Append filename at offset &0B in cmd buffer', align=Align.INLINE)
d.comment(0x87BB, 'Y=1: function code for save', align=Align.INLINE)
d.comment(0x87C0, 'Read FS reply command code for transfer type', align=Align.INLINE)
d.comment(0x87C3, 'Send file data blocks to server', align=Align.INLINE)
d.comment(0x87C6, 'Save CSD from reply for catalogue display', align=Align.INLINE)
d.comment(0x87CA, 'Send final reply acknowledgement', align=Align.INLINE)
d.comment(0x87CE, 'Check if file info messages enabled', align=Align.INLINE)
d.comment(0x87D1, 'Messages off: skip catalogue display', align=Align.INLINE)
d.comment(0x878C, 'Y = Y-4: point to start-address byte', align=Align.INLINE)
d.comment(0x8794, 'Save length byte for param block restore', align=Align.INLINE)
d.comment(0x879A, 'Restore length byte from stack', align=Align.INLINE)
d.comment(0x879D, 'Y = Y+5: advance to next address group', align=Align.INLINE)
d.comment(0x87A0, 'Decrement address byte counter', align=Align.INLINE)
d.comment(0x87A1, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x87A5, 'Read load/exec address byte from params', align=Align.INLINE)
d.comment(0x87A7, 'Copy to FS command buffer', align=Align.INLINE)
d.comment(0x87AA, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x87AB, 'Loop for bytes 9..1', align=Align.INLINE)
d.comment(0x87B4, 'Save port &91 for flow control ACK', align=Align.INLINE)
d.comment(0x87B8, 'Append filename to cmd buffer at offset X', align=Align.INLINE)
d.comment(0x87BD, 'Build header and send FS save command', align=Align.INLINE)
d.comment(0x87C9, 'Save CSD byte from reply for display', align=Align.INLINE)
d.comment(0x87CD, 'Restore CSD byte after reply command', align=Align.INLINE)
d.comment(0x87D3, 'Y=0: start of filename in reply', align=Align.INLINE)
d.comment(0x87D5, 'A = CSD; test for directory prefix', align=Align.INLINE)
d.comment(0x87D6, 'CSD=0: no directory prefix', align=Align.INLINE)
d.comment(0x87D8, 'Print directory prefix from reply', align=Align.INLINE)
d.comment(0x87DB, 'Dir printed: skip to address display', align=Align.INLINE)
d.comment(0x87DD, 'Load filename character from reply', align=Align.INLINE)
d.comment(0x87DF, 'Check for control character or space', align=Align.INLINE)
d.comment(0x87E1, 'Below &21: pad with spaces to column 12', align=Align.INLINE)
d.comment(0x87E6, 'Next character in filename', align=Align.INLINE)
d.comment(0x87E7, 'Loop for more filename characters', align=Align.INLINE)
d.comment(0x87E9, 'Print space to pad filename to 12 chars', align=Align.INLINE)
d.comment(0x87EC, 'Advance column counter', align=Align.INLINE)
d.comment(0x87ED, 'Reached column 12?', align=Align.INLINE)
d.comment(0x87EF, 'No: keep padding with spaces', align=Align.INLINE)
d.comment(0x87F1, 'Y=5: load address offset in reply', align=Align.INLINE)
d.comment(0x87F3, 'Print 4-byte load address in hex', align=Align.INLINE)
d.comment(0x87F6, 'Y=9: exec address offset in reply', align=Align.INLINE)
d.comment(0x87F8, 'Print 4-byte exec address in hex', align=Align.INLINE)
d.comment(0x87FB, 'Y=&0C: file length offset in reply', align=Align.INLINE)
d.comment(0x87FD, 'X=3: print 3 bytes of length', align=Align.INLINE)
d.comment(0x87FF, 'Print file length in hex', align=Align.INLINE)
d.comment(0x8805, 'Store reply command for attr decode', align=Align.INLINE)
d.comment(0x8808, 'Y=&0E: access byte offset in param block', align=Align.INLINE)
d.comment(0x880A, 'Load access byte from FS reply', align=Align.INLINE)
d.comment(0x880D, 'Convert FS access to BBC attribute format', align=Align.INLINE)
d.comment(0x8810, 'Store decoded access in param block', align=Align.INLINE)
d.comment(0x8812, 'Next attribute byte', align=Align.INLINE)
d.comment(0x8813, 'Load remaining reply data for param block', align=Align.INLINE)
d.comment(0x8816, 'Copied all 4 bytes? (Y=&0E..&11)', align=Align.INLINE)
d.comment(0x8818, 'Loop for 4 attribute bytes', align=Align.INLINE)
d.comment(0x881A, 'Restore A/X/Y and return to caller', align=Align.INLINE)


d.subroutine(0x881D, 'copy_load_addr_from_params', title='Copy load address from parameter block', description="""Copies 4 bytes from (fs_options)+2..5 (the load address in the
OSFILE parameter block) to &AE-&B3 (local workspace).""", on_exit={'y': '8 (final offset)', 'a': 'last byte copied'})
d.comment(0x881D, 'Start at offset 5 (top of 4-byte addr)', align=Align.INLINE)
d.comment(0x881F, 'Read from parameter block', align=Align.INLINE)
d.comment(0x8821, 'Store to local workspace', align=Align.INLINE)
d.comment(0x8824, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8825, 'Copy offsets 5,4,3,2 (4 bytes)', align=Align.INLINE)
d.comment(0x8827, 'Loop while Y >= 2', align=Align.INLINE)
d.comment(0x8829, 'Y += 5', align=Align.INLINE)
d.comment(0x882A, 'Y += 4', align=Align.INLINE)
d.comment(0x882E, 'Return', align=Align.INLINE)


d.subroutine(0x882F, 'copy_reply_to_params', title='Copy FS reply data to parameter block', description="""Copies bytes from the FS command reply buffer (&0F02+) into the
parameter block at (fs_options)+2..13. Used to fill in the OSFILE
parameter block with information returned by the fileserver.""", on_entry={'x': 'attribute byte (stored first at offset &0D)'})
d.comment(0x882F, 'Start at offset &0D (top of range)', align=Align.INLINE)
d.comment(0x8831, 'First store uses X (attrib byte)', align=Align.INLINE)
d.comment(0x8832, 'Write to parameter block', align=Align.INLINE)
d.comment(0x8834, 'Read next byte from reply buffer', align=Align.INLINE)
d.comment(0x8838, 'Copy offsets &0D down to 2', align=Align.INLINE)
d.comment(0x883C, 'Y -= 4', align=Align.INLINE)


d.subroutine(0x8841, 'transfer_file_blocks', title='Multi-block file data transfer', description="""Manages the transfer of file data in chunks between the local
machine and the fileserver. Entry conditions: WORK (&B0-&B3) and
WORK+4 (&B4-&B7) hold the low and high addresses of the data
being sent/received. Sets up source (&C4-&C7) and destination
(&C8-&CB) from the FS reply, sends &80-byte (128-byte) blocks
with command &91, and continues until all data has been
transferred. Handles address overflow and Tube co-processor
transfers. For SAVE, WORK+8 holds the port on which to receive
byte-level ACKs for each data block (flow control).""")
d.comment(0x8841, 'Save FS command byte on stack', align=Align.INLINE)
d.comment(0x8845, 'Addresses equal: nothing to transfer', align=Align.INLINE)
d.comment(0x8847, 'A=0: high bytes of block size', align=Align.INLINE)
d.comment(0x8849, 'Push 4-byte block size: 0, 0, hi, lo', align=Align.INLINE)
d.comment(0x884A, 'Push second zero byte', align=Align.INLINE)
d.comment(0x884C, 'Load block size high byte from &0F07', align=Align.INLINE)
d.comment(0x884F, 'Push block size high', align=Align.INLINE)
d.comment(0x8850, 'Load block size low byte from &0F06', align=Align.INLINE)
d.comment(0x8853, 'Push block size low', align=Align.INLINE)
d.comment(0x8854, 'Y=4: process 4 address bytes', align=Align.INLINE)
d.comment(0x8856, 'CLC for ADC in loop', align=Align.INLINE)
d.comment(0x8857, 'Source = current position', align=Align.INLINE)
d.comment(0x8859, 'Store source address byte', align=Align.INLINE)
d.comment(0x885B, 'Pop block size byte from stack', align=Align.INLINE)
d.comment(0x885C, 'Dest = current pos + block size', align=Align.INLINE)
d.comment(0x885E, 'Store dest address byte', align=Align.INLINE)
d.comment(0x8860, 'Advance current position', align=Align.INLINE)
d.comment(0x8862, 'Next address byte', align=Align.INLINE)
d.comment(0x8863, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8864, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8866, 'SEC for SBC in overshoot check', align=Align.INLINE)
d.comment(0x8867, 'Check if new pos overshot end addr', align=Align.INLINE)
d.comment(0x886A, 'Subtract end address byte', align=Align.INLINE)
d.comment(0x886D, 'Next byte', align=Align.INLINE)
d.comment(0x886E, 'Decrement counter', align=Align.INLINE)
d.comment(0x886F, 'Loop for 4-byte comparison', align=Align.INLINE)
d.comment(0x8871, 'C=0: no overshoot, proceed', align=Align.INLINE)
d.comment(0x8873, 'Overshot: clamp dest to end address', align=Align.INLINE)
d.comment(0x8875, 'Load end address byte', align=Align.INLINE)
d.comment(0x8877, 'Replace dest with end address', align=Align.INLINE)
d.comment(0x8879, 'Next byte', align=Align.INLINE)
d.comment(0x887A, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x887C, 'Recover original FS command byte', align=Align.INLINE)
d.comment(0x887D, 'Re-push for next iteration', align=Align.INLINE)
d.comment(0x887E, 'Save processor flags (C from cmp)', align=Align.INLINE)
d.comment(0x887F, 'Store command byte in TXCB', align=Align.INLINE)
d.comment(0x8881, '128-byte block size for data transfer', align=Align.INLINE)
d.comment(0x8883, 'Store size in TXCB control byte', align=Align.INLINE)
d.comment(0x8885, 'Point TX ptr to &00C0; transmit', align=Align.INLINE)
d.comment(0x8888, 'ACK port for flow control', align=Align.INLINE)
d.comment(0x888A, 'Set reply port for ACK receive', align=Align.INLINE)
d.comment(0x888D, 'Restore flags (C=overshoot status)', align=Align.INLINE)
d.comment(0x888E, 'C=1: all data sent (overshot), done', align=Align.INLINE)
d.comment(0x8890, 'Command &91 = data block transfer', align=Align.INLINE)
d.comment(0x8892, 'Store command &91 in TXCB', align=Align.INLINE)
d.comment(0x8894, 'Skip command code byte in TX buffer', align=Align.INLINE)
d.comment(0x8896, 'Transmit block and wait (BRIANX)', align=Align.INLINE)
d.comment(0x8899, 'More blocks? Loop back', align=Align.INLINE)


d.subroutine(0x889B, 'fscv_1_eof', title='FSCV 1: EOF handler', description="""Checks whether a file handle has reached end-of-file. Converts
the handle via handle_to_mask_clc, tests the result against the
EOF hint byte (&0E07). If the hint bit is clear, returns X=0
immediately (definitely not at EOF — no network call needed).
If the hint bit is set, sends FS command &11 (FCEOF) to query
the fileserver for definitive EOF status. Returns X=&FF if at
EOF, X=&00 if not. This two-level check avoids an expensive
network round-trip when the file is known to not be at EOF.""", on_entry={'x': 'file handle to check'}, on_exit={'x': '&FF if at EOF, &00 if not'})
d.comment(0x889B, 'Save A (function code)', align=Align.INLINE)
d.comment(0x889C, 'X = file handle to check', align=Align.INLINE)
d.comment(0x889D, 'Convert handle to bitmask in A', align=Align.INLINE)
d.comment(0x88A0, 'Y = handle bitmask from conversion', align=Align.INLINE)
d.comment(0x88A1, 'Local hint: is EOF possible for this handle?', align=Align.INLINE)
d.comment(0x88A4, 'X = result of AND (0 = not at EOF)', align=Align.INLINE)
d.comment(0x88A5, 'Hint clear: definitely not at EOF', align=Align.INLINE)
d.comment(0x88A7, 'Save bitmask for clear_fs_flag', align=Align.INLINE)
d.comment(0x88A8, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x88AB, 'Y=&11: FS function code FCEOF', align=Align.INLINE)
d.comment(0x88B2, 'Restore bitmask', align=Align.INLINE)
d.comment(0x88B3, 'FS reply: non-zero = at EOF', align=Align.INLINE)
d.comment(0x88B6, 'At EOF: skip flag clear', align=Align.INLINE)
d.comment(0x88B8, 'Not at EOF: clear the hint bit', align=Align.INLINE)
d.comment(0x88BB, 'Restore A', align=Align.INLINE)
d.comment(0x88BC, 'Restore Y', align=Align.INLINE)
d.comment(0x88BE, 'Return; X=0 (not EOF) or X=&FF (EOF)', align=Align.INLINE)


d.subroutine(0x88BF, 'filev_attrib_dispatch', title='FILEV attribute dispatch (A=1-6)', description="""Dispatches OSFILE operations by function code:
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
d.comment(0x88BF, 'Store function code in FS cmd buffer', align=Align.INLINE)
d.comment(0x88C2, 'A=6? (delete)', align=Align.INLINE)
d.comment(0x88C4, 'Yes: jump to delete handler', align=Align.INLINE)
d.comment(0x88C6, 'A>=7: unsupported, fall through to return', align=Align.INLINE)
d.comment(0x88C8, 'A=5? (read catalogue info)', align=Align.INLINE)
d.comment(0x88CA, 'Yes: jump to read info handler', align=Align.INLINE)
d.comment(0x88CC, 'A=4? (write attributes only)', align=Align.INLINE)
d.comment(0x88CE, 'Yes: jump to write attrs handler', align=Align.INLINE)
d.comment(0x88D0, 'A=1? (write all catalogue info)', align=Align.INLINE)
d.comment(0x88D2, 'Yes: jump to write-all handler', align=Align.INLINE)
d.comment(0x88D4, 'A=2 or 3: convert to param block offset', align=Align.INLINE)
d.comment(0x88D5, 'A*4: 2->8, 3->12', align=Align.INLINE)
d.comment(0x88D6, 'Y = A*4', align=Align.INLINE)
d.comment(0x88D7, 'Y = A*4 - 3 (load addr offset for A=2)', align=Align.INLINE)
d.comment(0x88DA, 'X=3: copy 4 bytes', align=Align.INLINE)
d.comment(0x88DC, 'Load address byte from param block', align=Align.INLINE)
d.comment(0x88DE, 'Store to FS cmd data area', align=Align.INLINE)
d.comment(0x88E1, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x88E2, 'Next dest byte', align=Align.INLINE)
d.comment(0x88E3, 'Loop for 4 bytes', align=Align.INLINE)
d.comment(0x88E5, 'X=5: data extent for filename copy', align=Align.INLINE)
d.comment(0x88E9, 'A=1: encode protection from param block', align=Align.INLINE)
d.comment(0x88EC, 'Store encoded attrs at &0F0E', align=Align.INLINE)
d.comment(0x88EF, 'Y=9: source offset in param block', align=Align.INLINE)
d.comment(0x88F1, 'X=8: dest offset in cmd buffer', align=Align.INLINE)
d.comment(0x88F3, 'Load byte from param block', align=Align.INLINE)
d.comment(0x88F5, 'Store to FS cmd buffer', align=Align.INLINE)
d.comment(0x88F8, 'Next source byte (descending)', align=Align.INLINE)
d.comment(0x88F9, 'Next dest byte', align=Align.INLINE)
d.comment(0x88FA, 'Loop until X=0 (8 bytes copied)', align=Align.INLINE)
d.comment(0x88FC, 'X=&0A: data extent past attrs+addrs', align=Align.INLINE)
d.comment(0x88FE, 'Append filename to cmd buffer', align=Align.INLINE)
d.comment(0x8901, 'Y=&13: fn code for FCSAVE (write attrs)', align=Align.INLINE)
d.comment(0x8903, 'ALWAYS branch to send command', align=Align.INLINE)
d.comment(0x8905, 'A=6: copy filename (delete)', align=Align.INLINE)
d.comment(0x8908, 'Y=&14: fn code for FCDEL (delete)', align=Align.INLINE)
d.comment(0x890A, 'Set V=1 (BIT trick: &B3 has bit 6 set)', align=Align.INLINE)
d.comment(0x890D, 'Send via prepare_fs_cmd_v (V=1 path)', align=Align.INLINE)
d.comment(0x8910, 'C=1: &D6 not-found, skip to return', align=Align.INLINE)
d.comment(0x8912, 'C=0: success, copy reply to param block', align=Align.INLINE)
d.comment(0x8914, 'A=4: encode attrs from param block', align=Align.INLINE)
d.comment(0x8917, 'Store encoded attrs at &0F06', align=Align.INLINE)
d.comment(0x891A, 'X=2: data extent (1 attr byte + fn)', align=Align.INLINE)
d.comment(0x891C, 'ALWAYS branch to append filename', align=Align.INLINE)
d.comment(0x891E, 'X=1: filename only, no data extent', align=Align.INLINE)
d.comment(0x8920, 'Copy filename to cmd buffer', align=Align.INLINE)
d.comment(0x8923, 'Y=&12: fn code for FCEXAM (read info)', align=Align.INLINE)
d.comment(0x8928, 'Save object type from FS reply', align=Align.INLINE)
d.comment(0x892B, 'Clear reply byte (X=0 on success)', align=Align.INLINE)
d.comment(0x892E, 'Clear length high byte in reply', align=Align.INLINE)
d.comment(0x8931, 'Decode 5-bit access byte from FS reply', align=Align.INLINE)
d.comment(0x8934, 'Y=&0E: attrs offset in param block', align=Align.INLINE)
d.comment(0x8936, 'Store decoded attrs at param block +&0E', align=Align.INLINE)
d.comment(0x8938, 'Y=&0D: start copy below attrs', align=Align.INLINE)
d.comment(0x8939, 'X=&0C: copy from reply offset &0C down', align=Align.INLINE)
d.comment(0x893B, 'Load reply byte (load/exec/length)', align=Align.INLINE)
d.comment(0x893E, 'Store to param block', align=Align.INLINE)
d.comment(0x8940, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x8941, 'Next source byte', align=Align.INLINE)
d.comment(0x8942, 'Loop until X=0 (12 bytes copied)', align=Align.INLINE)
d.comment(0x8944, 'X=0 -> X=2 for length high copy', align=Align.INLINE)
d.comment(0x8945, 'INX again: X=2', align=Align.INLINE)
d.comment(0x8946, 'Y=&11: length high dest in param block', align=Align.INLINE)
d.comment(0x8948, 'Load length high byte from reply', align=Align.INLINE)
d.comment(0x894B, 'Store to param block', align=Align.INLINE)
d.comment(0x894D, 'Next dest byte (descending)', align=Align.INLINE)
d.comment(0x894E, 'Next source byte', align=Align.INLINE)
d.comment(0x894F, 'Loop for 3 length-high bytes', align=Align.INLINE)
d.comment(0x8951, 'Return object type in A', align=Align.INLINE)
d.comment(0x8954, 'A>=0: branch to restore_args_return', align=Align.INLINE)


d.subroutine(0x89C2, 'return_a_zero', title='Return with A=0 via register restore', description="""Loads A=0 and branches (always taken) to the common register
restore exit at restore_args_return. Used as a shared exit
point by ARGSV, FINDV, and GBPBV when an operation is
unsupported or should return zero.""", on_exit={'a': '0', 'x': 'restored from fs_options (&BB)', 'y': 'restored from fs_block_offset (&BC)'})


d.subroutine(0x89A1, 'restore_args_return', title='Restore arguments and return', description="""Common exit point for FS vector handlers. Reloads A from
fs_last_byte_flag (&BD), X from fs_options (&BB), and Y from
fs_block_offset (&BC) — the values saved at entry by
save_fscv_args — and returns to the caller.""", on_exit={'a': 'restored from fs_last_byte_flag (&BD)', 'x': 'restored from fs_options (&BB)', 'y': 'restored from fs_block_offset (&BC)'})
d.comment(0x89A1, 'A = saved function code / command', align=Align.INLINE)
d.comment(0x89A3, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x89A5, 'Y = saved control block ptr high', align=Align.INLINE)
d.comment(0x89A7, 'Return to MOS with registers restored', align=Align.INLINE)
d.comment(0x89AA, 'A=2: FS-level ensure (write extent)', align=Align.INLINE)
d.comment(0x89AC, 'A>=3: FS command (ARGSV write)', align=Align.INLINE)
d.comment(0x89AE, 'Y = A = byte count for copy loop', align=Align.INLINE)
d.comment(0x89AF, 'A!=0: copy command context block', align=Align.INLINE)
d.comment(0x89B3, 'Shared: halve A (A=0 or A=2 paths)', align=Align.INLINE)
d.comment(0x89B4, 'Return with A = FS number or 1', align=Align.INLINE)
d.comment(0x89B9, "Store to caller's parameter block", align=Align.INLINE)
d.comment(0x89BB, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x89BC, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x89BE, 'Y=&FF after loop; fill high bytes', align=Align.INLINE)
d.comment(0x89C0, 'Set 32-bit result bytes 2-3 to &FF', align=Align.INLINE)

d.label(0x8A1A, 'fscv_0_opt_entry')


d.subroutine(0x8A1C, 'fscv_0_opt', title='FSCV 0: *OPT handler (OPTION)', description="""Handles *OPT X,Y to set filing system options:
  *OPT 1,Y (Y=0/1): set local user option in &0E06 (OPT)
  *OPT 4,Y (Y=0-3): set boot option via FS command &16 (FCOPT)
Other combinations generate error &CB (OPTER: "bad option").""", on_entry={'x': 'option number (1 or 4)', 'y': 'option value'})
d.comment(0x8A1C, 'Is it *OPT 4,Y?', align=Align.INLINE)
d.comment(0x8A1E, 'No: check for *OPT 1', align=Align.INLINE)
d.comment(0x8A20, 'Y must be 0-3 for boot option', align=Align.INLINE)
d.comment(0x8A22, 'Y < 4: valid boot option', align=Align.INLINE)
d.comment(0x8A24, 'Not *OPT 4: check for *OPT 1', align=Align.INLINE)
d.comment(0x8A25, 'Not *OPT 1 either: bad option', align=Align.INLINE)
d.comment(0x8A27, 'Set local messages flag (*OPT 1,Y)', align=Align.INLINE)
d.comment(0x8A2A, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x8A2C, 'Error index 7 (Bad option)', align=Align.INLINE)
d.comment(0x8A2E, 'Generate BRK error', align=Align.INLINE)
d.comment(0x8A31, 'Boot option value in FS command', align=Align.INLINE)
d.comment(0x8A34, 'Y=&16: FS function code FCOPT', align=Align.INLINE)
d.comment(0x8A39, 'Restore Y from saved value', align=Align.INLINE)
d.comment(0x8A3B, 'Cache boot option locally', align=Align.INLINE)
d.comment(0x8A3E, 'Return via restore_args_return', align=Align.INLINE)
d.comment(0x8A40, 'Y=9: adjust 9 address bytes', align=Align.INLINE)
d.comment(0x8A42, 'Adjust with carry clear', align=Align.INLINE)
d.comment(0x8A45, 'Y=1: adjust 1 address byte', align=Align.INLINE)
d.comment(0x8A47, 'C=0 for address adjustment', align=Align.INLINE)


d.subroutine(0x8A48, 'adjust_addrs', title='Bidirectional 4-byte address adjustment', description="""Adjusts a 4-byte value in the parameter block at (fs_options)+Y:
  If fs_load_addr_2 (&B2) is positive: adds fs_lib_handle+X values
  If fs_load_addr_2 (&B2) is negative: subtracts fs_lib_handle+X
Starting offset X=&FC means it reads from &0E06-&0E09 area.
Used to convert between absolute and relative file positions.""", on_entry={'y': 'starting offset into (fs_options) parameter block'}, on_exit={'a': 'corrupted (last adjusted byte)', 'x': '0', 'y': 'entry Y + 4'})
d.comment(0x8A48, 'X=&FC: index into &0E06 area (wraps to 0)', align=Align.INLINE)
d.comment(0x8A4A, 'Load byte from param block', align=Align.INLINE)
d.comment(0x8A4C, 'Test sign of adjustment direction', align=Align.INLINE)
d.comment(0x8A4E, 'Negative: subtract instead', align=Align.INLINE)
d.comment(0x8A50, 'Add adjustment value', align=Align.INLINE)
d.comment(0x8A53, 'Skip to store result', align=Align.INLINE)
d.comment(0x8A56, 'Subtract adjustment value', align=Align.INLINE)
d.comment(0x8A59, 'Store adjusted byte back', align=Align.INLINE)
d.comment(0x8A5B, 'Next param block byte', align=Align.INLINE)
d.comment(0x8A5C, 'Next adjustment byte (X wraps &FC->&00)', align=Align.INLINE)
d.comment(0x8A5D, 'Loop 4 times (X=&FC,&FD,&FE,&FF,done)', align=Align.INLINE)


d.subroutine(0x8956, 'argsv_handler', title='ARGSV handler (OSARGS entry point)', description="""  A=0, Y=0: return filing system number (5 = network FS)
  A=0, Y>0: read file pointer via FS command &0C (FCRDSE)
  A=1, Y>0: write file pointer via FS command &0D (FCWRSE)
  A=2, Y=0: return &01 (command-line tail supported)
  A>=3 (ensure): silently returns -- NFS has no local write buffer
     to flush, since all data is sent to the fileserver immediately
The handle in Y is converted via handle_to_mask_clc. For writes
(A=1), the carry flag from the mask conversion is used to branch
to save_args_handle, which records the handle for later use.""", on_entry={'a': 'function code (0=query, 1=write ptr, >=3=ensure)', 'y': 'file handle (0=FS-level query, >0=per-file)'}, on_exit={'a': 'filing system number if A=0/Y=0 query, else restored', 'x': 'restored', 'y': 'restored'})
d.comment(0x8956, 'Save A/X/Y registers for later restore', align=Align.INLINE)
d.comment(0x8959, 'Function >= 3?', align=Align.INLINE)
d.comment(0x895B, 'A>=3 (ensure/flush): no-op for NFS', align=Align.INLINE)
d.comment(0x895D, 'Test file handle', align=Align.INLINE)
d.comment(0x895F, 'Y=0: FS-level query, not per-file', align=Align.INLINE)
d.comment(0x8961, 'Convert handle to bitmask', align=Align.INLINE)
d.comment(0x8964, 'Store bitmask as first cmd data byte', align=Align.INLINE)
d.comment(0x8967, 'LSR splits A: C=1 means write (A=1)', align=Align.INLINE)
d.comment(0x8968, 'Store function code to cmd data byte 2', align=Align.INLINE)
d.comment(0x896B, 'C=1: write path, copy ptr from caller', align=Align.INLINE)
d.comment(0x896D, 'Y=&0C: FCRDSE (read sequential pointer)', align=Align.INLINE)
d.comment(0x896F, 'X=2: 3 data bytes in command', align=Align.INLINE)
d.comment(0x8971, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8974, 'Clear last-byte flag on success', align=Align.INLINE)
d.comment(0x8976, 'X = saved control block ptr low', align=Align.INLINE)
d.comment(0x8978, 'Y=2: copy 3 bytes of file pointer', align=Align.INLINE)
d.comment(0x897A, 'Zero high byte of 3-byte pointer', align=Align.INLINE)
d.comment(0x897C, 'Read reply byte from FS cmd data', align=Align.INLINE)
d.comment(0x897F, "Store to caller's control block", align=Align.INLINE)
d.comment(0x8981, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8982, 'Next source byte', align=Align.INLINE)
d.comment(0x8983, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8985, 'C=0 (read): return to caller', align=Align.INLINE)
d.comment(0x8987, 'Save bitmask for set_fs_flag later', align=Align.INLINE)
d.comment(0x8988, 'Push bitmask', align=Align.INLINE)
d.comment(0x8989, 'Y=3: copy 4 bytes of file pointer', align=Align.INLINE)
d.comment(0x898B, "Read caller's pointer byte", align=Align.INLINE)
d.comment(0x898D, 'Store to FS command data area', align=Align.INLINE)
d.comment(0x8990, 'Next source byte', align=Align.INLINE)
d.comment(0x8991, 'Next destination byte', align=Align.INLINE)
d.comment(0x8992, 'Loop for all 4 bytes', align=Align.INLINE)
d.comment(0x8994, 'Y=&0D: FCWRSE (write sequential pointer)', align=Align.INLINE)
d.comment(0x8996, 'X=5: 6 data bytes in command', align=Align.INLINE)
d.comment(0x8998, 'Build and send FS command', align=Align.INLINE)
d.comment(0x899B, 'Save not-found status from X', align=Align.INLINE)
d.comment(0x899D, 'Recover bitmask for EOF hint update', align=Align.INLINE)
d.comment(0x899E, 'Set EOF hint bit for this handle', align=Align.INLINE)
d.comment(0x89A8, 'Y=0: FS-level queries (no file handle)', align=Align.INLINE)
d.comment(0x89B1, "FS number 5 (loaded as &0A, LSR'd)", align=Align.INLINE)
d.comment(0x89B6, "Copy command context to caller's block", align=Align.INLINE)


d.subroutine(0x89C6, 'findv_handler', title='FINDV handler (OSFIND entry point)', description="""  A=0: close file -- delegates to close_handle (&89FE)
  A>0: open file -- modes &40=read, &80=write/update, &C0=read/write
For open: the mode byte is converted to the fileserver's two-flag
format by flipping bit 7 (EOR #&80) and shifting. This produces
Flag 1 (read/write direction) and Flag 2 (create/existing),
matching the fileserver protocol. After a successful open, the
new handle's bit is OR'd into the EOF hint byte (marks it as
"might be at EOF, query the server"), and into the sequence
number tracking byte for the byte-stream protocol.""", on_entry={'a': 'operation (0=close, &40=read, &80=write, &C0=R/W)', 'x': 'filename pointer low (open)', 'y': 'file handle (close) or filename pointer high (open)'}, on_exit={'a': 'handle on open, 0 on close-all, restored on close-one', 'x': 'restored', 'y': 'restored'})
d.comment(0x89C6, 'Save A/X/Y and set up pointers', align=Align.INLINE)
d.comment(0x89C9, 'SEC distinguishes open (A>0) from close', align=Align.INLINE)
d.comment(0x89CE, 'A=0: close file(s)', align=Align.INLINE)
d.comment(0x89D0, 'Valid open modes: &40, &80, &C0 only', align=Align.INLINE)
d.comment(0x89D2, 'Invalid mode bits: return', align=Align.INLINE)
d.comment(0x89D4, 'A = original mode byte', align=Align.INLINE)
d.comment(0x89D5, 'Convert MOS mode to FS protocol flags', align=Align.INLINE)
d.comment(0x89D7, 'ASL: shift mode bits left', align=Align.INLINE)
d.comment(0x89D8, 'Flag 1: read/write direction', align=Align.INLINE)
d.comment(0x89DB, 'ROL: Flag 2 into bit 0', align=Align.INLINE)
d.comment(0x89DC, 'Flag 2: create vs existing file', align=Align.INLINE)
d.comment(0x89DF, 'Parse filename from command line', align=Align.INLINE)
d.comment(0x89E2, 'X=2: copy after 2-byte flags', align=Align.INLINE)
d.comment(0x89E4, 'Copy filename to FS command buffer', align=Align.INLINE)
d.comment(0x89E7, 'Y=6: FS function code FCOPEN', align=Align.INLINE)
d.comment(0x89E9, 'Set V flag from l83b3 bit 6', align=Align.INLINE)
d.comment(0x89EC, 'Build and send FS open command', align=Align.INLINE)
d.comment(0x89EF, 'Error: restore and return', align=Align.INLINE)
d.comment(0x89F1, 'Load reply handle from FS', align=Align.INLINE)
d.comment(0x89F4, 'X = new file handle', align=Align.INLINE)
d.comment(0x89F5, 'Set EOF hint + sequence bits', align=Align.INLINE)
d.comment(0x89FC, 'ALWAYS branch to restore and return', align=Align.INLINE)
d.comment(0x89F8, """OR handle bit into fs_sequence_nos
(&0E08). Without this, a newly opened file could
inherit a stale sequence number from a previous
file using the same handle, causing byte-stream
protocol errors.""")


d.subroutine(0x89FE, 'close_handle', title='Close file handle(s) (CLOSE)', description="""  Y=0: close all files — first calls OSBYTE &77 (close SPOOL and
       EXEC files) to coordinate with the MOS before sending the
       close-all command to the fileserver. This ensures locally-
       managed file handles are released before the server-side
       handles are invalidated, preventing the MOS from writing to
       a closed spool file.
  Y>0: close single handle — sends FS close command and clears
       the handle's bit in both the EOF hint byte and the sequence
       number tracking byte.""", on_entry={'y': 'file handle (0=close all, >0=close single)'})
d.comment(0x89FE, 'A = handle (Y preserved in A)', align=Align.INLINE)
d.comment(0x89FF, 'Y>0: close single file', align=Align.INLINE)
d.comment(0x8A01, 'Close SPOOL/EXEC before FS close-all', align=Align.INLINE)
d.comment(0x8A06, 'Y=0: close all handles on server', align=Align.INLINE)
d.comment(0x8A08, 'Handle byte in FS command buffer', align=Align.INLINE)
d.comment(0x8A12, 'Reply handle for flag update', align=Align.INLINE)
d.comment(0x8A15, 'Update EOF/sequence tracking bits', align=Align.INLINE)
d.comment(0x8A18, 'C=0: restore A/X/Y and return', align=Align.INLINE)
d.comment(0x8A1A, 'Entry from fscv_0_opt (close-all path)', align=Align.INLINE)


d.subroutine(0x8A60, 'gbpbv_handler', title='GBPBV handler (OSGBPB entry point)', description="""  A=1-4: file read/write operations (handle-based)
  A=5-8: info queries (disc title, current dir, lib, filenames)
Calls 1-4 are standard file data transfers via the fileserver.
Calls 5-8 were a late addition to the MOS spec and are the only
NFS operations requiring Tube data transfer -- described in the
original source as "untidy but useful in theory." The data format
uses length-prefixed strings (<name length><object name>) rather
than the CR-terminated strings used elsewhere in the FS.""", on_entry={'a': 'call number (1-8)', 'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': '0 after FS operation, else restored', 'x': 'restored', 'y': 'restored'})
d.comment(0x8A60, 'Save A/X/Y to FS workspace', align=Align.INLINE)
d.comment(0x8A63, 'X = call number for range check', align=Align.INLINE)
d.comment(0x8A64, 'A=0: invalid, restore and return', align=Align.INLINE)
d.comment(0x8A66, 'Convert to 0-based (A=0..7)', align=Align.INLINE)
d.comment(0x8A67, 'Range check: must be 0-7', align=Align.INLINE)
d.comment(0x8A69, 'In range: continue to handler', align=Align.INLINE)
d.comment(0x8A6B, 'Out of range: restore args and return', align=Align.INLINE)
d.comment(0x8A6E, 'Recover 0-based function code', align=Align.INLINE)
d.comment(0x8A6F, 'Y=0: param block byte 0 (file handle)', align=Align.INLINE)
d.comment(0x8A71, 'Save function code on stack', align=Align.INLINE)
d.comment(0x8A72, 'A>=4: info queries, dispatch separately', align=Align.INLINE)
d.comment(0x8A74, 'A<4: file read/write operations', align=Align.INLINE)
d.comment(0x8A76, 'Dispatch to OSGBPB 5-8 info handler', align=Align.INLINE)
d.comment(0x8A79, 'Get file handle from param block byte 0', align=Align.INLINE)
d.comment(0x8A7B, 'Convert handle to bitmask for EOF flags', align=Align.INLINE)
d.comment(0x8A7E, 'Store handle in FS command data', align=Align.INLINE)
d.comment(0x8A81, 'Y=&0B: start at param block byte 11', align=Align.INLINE)
d.comment(0x8A83, 'X=6: copy 6 bytes of transfer params', align=Align.INLINE)
d.comment(0x8A85, 'Load param block byte', align=Align.INLINE)
d.comment(0x8A87, 'Store to FS command buffer at &0F06+X', align=Align.INLINE)
d.comment(0x8A8A, 'Previous param block byte', align=Align.INLINE)
d.comment(0x8A8B, 'Skip param block offset 8 (the handle)', align=Align.INLINE)
d.comment(0x8A8D, 'Not at handle offset: continue', align=Align.INLINE)
d.comment(0x8A8F, 'Extra DEY to skip handle byte', align=Align.INLINE)
d.comment(0x8A90, 'Decrement copy counter', align=Align.INLINE)
d.comment(0x8A91, 'Loop for all 6 bytes', align=Align.INLINE)
d.comment(0x8A93, 'Recover function code from stack', align=Align.INLINE)
d.comment(0x8A94, 'LSR: odd=read (C=1), even=write (C=0)', align=Align.INLINE)
d.comment(0x8A95, 'Save function code again (need C later)', align=Align.INLINE)
d.comment(0x8A96, 'Even (write): X stays 0', align=Align.INLINE)
d.comment(0x8A98, 'Odd (read): X=1', align=Align.INLINE)
d.comment(0x8A99, 'Store FS direction flag', align=Align.INLINE)
d.comment(0x8A9C, 'Y=&0B: command data extent', align=Align.INLINE)
d.comment(0x8A9E, 'Command &91=put, &92=get', align=Align.INLINE)
d.comment(0x8AA0, 'Recover function code', align=Align.INLINE)
d.comment(0x8AA1, 'Save again for later direction check', align=Align.INLINE)
d.comment(0x8AA2, 'Even (write): keep &91 and Y=&0B', align=Align.INLINE)
d.comment(0x8AA4, 'Odd (read): use &92 (get) instead', align=Align.INLINE)
d.comment(0x8AA6, 'Read: one fewer data byte in command', align=Align.INLINE)
d.comment(0x8AA7, 'Store port to FS command URD field', align=Align.INLINE)
d.comment(0x8AAA, 'Save port for error recovery', align=Align.INLINE)
d.comment(0x8AAC, 'X=8: command data bytes', align=Align.INLINE)
d.comment(0x8AAE, 'Load handle from FS command data', align=Align.INLINE)
d.comment(0x8AB1, 'Build FS command with handle+flag', align=Align.INLINE)
d.comment(0x8AB4, 'Save seq# for byte-stream flow control', align=Align.INLINE)
d.comment(0x8AB6, 'Store to FS sequence number workspace', align=Align.INLINE)
d.comment(0x8AB9, 'X=4: copy 4 address bytes', align=Align.INLINE)
d.comment(0x8ABB, 'Set up source/dest from param block', align=Align.INLINE)
d.comment(0x8ABD, 'Store as source address', align=Align.INLINE)
d.comment(0x8AC0, 'Store as current transfer position', align=Align.INLINE)
d.comment(0x8AC3, 'Skip 4 bytes to reach transfer length', align=Align.INLINE)
d.comment(0x8AC6, 'Dest = source + length', align=Align.INLINE)
d.comment(0x8AC8, 'Store as end address', align=Align.INLINE)
d.comment(0x8ACB, 'Back 3 to align for next iteration', align=Align.INLINE)
d.comment(0x8ACE, 'Decrement byte counter', align=Align.INLINE)
d.comment(0x8ACF, 'Loop for all 4 address bytes', align=Align.INLINE)
d.comment(0x8AD1, 'X=1 after loop', align=Align.INLINE)
d.comment(0x8AD2, 'Copy CSD data to command buffer', align=Align.INLINE)
d.comment(0x8AD5, 'Store at &0F06+X', align=Align.INLINE)
d.comment(0x8AD8, 'Decrement counter', align=Align.INLINE)
d.comment(0x8AD9, 'Loop for X=1,0', align=Align.INLINE)
d.comment(0x8ADB, 'Odd (read): send data to FS first', align=Align.INLINE)
d.comment(0x8ADC, 'Non-zero: skip write path', align=Align.INLINE)
d.comment(0x8ADE, 'Load port for transfer setup', align=Align.INLINE)
d.comment(0x8AE1, 'Transfer data blocks to fileserver', align=Align.INLINE)
d.comment(0x8AE4, 'Carry set: transfer error', align=Align.INLINE)
d.comment(0x8AE6, 'Read path: receive data blocks from FS', align=Align.INLINE)
d.comment(0x8AE9, 'Wait for FS reply command', align=Align.INLINE)
d.comment(0x8AEC, 'Load handle mask for EOF flag update', align=Align.INLINE)
d.comment(0x8AEE, 'Check FS reply: bit 7 = not at EOF', align=Align.INLINE)
d.comment(0x8AF1, 'Bit 7 set: not EOF, skip clear', align=Align.INLINE)
d.comment(0x8AF3, 'At EOF: clear EOF hint for this handle', align=Align.INLINE)
d.comment(0x8AF6, 'Set EOF hint flag (may be at EOF)', align=Align.INLINE)
d.comment(0x8AF9, 'Direction=0: forward adjustment', align=Align.INLINE)
d.comment(0x8AFB, 'Adjust param block addrs by +9 bytes', align=Align.INLINE)
d.comment(0x8AFE, 'Direction=&FF: reverse adjustment', align=Align.INLINE)
d.comment(0x8B00, 'SEC for reverse subtraction', align=Align.INLINE)
d.comment(0x8B01, 'Adjust param block addrs (reverse)', align=Align.INLINE)
d.comment(0x8B04, 'Shift bit 7 into C for return flag', align=Align.INLINE)
d.comment(0x8B07, 'Return via restore_args path', align=Align.INLINE)
d.comment(0x8B0A, 'Y=&15: function code for disc title', align=Align.INLINE)
d.comment(0x8B0C, 'Build and send FS command', align=Align.INLINE)
d.comment(0x8B0F, 'Load boot option from FS workspace', align=Align.INLINE)
d.comment(0x8B12, 'Store boot option in reply area', align=Align.INLINE)
d.comment(0x8B15, 'X=0: reply data start offset', align=Align.INLINE)
d.comment(0x8B17, 'Clear reply buffer high byte', align=Align.INLINE)
d.comment(0x8B19, 'A=&12: 18 bytes of reply data', align=Align.INLINE)
d.comment(0x8B1B, 'Store as byte count for copy', align=Align.INLINE)
d.comment(0x8B1D, 'ALWAYS branch to copy_reply_to_caller', align=Align.INLINE)


d.subroutine(0x8B1F, 'osgbpb_info', title='OSGBPB 5-8 info handler (OSINFO)', description="""Handles the "messy interface tacked onto OSGBPB" (original source).
Checks whether the destination address is in Tube space by comparing
the high bytes against TBFLAG. If in Tube space, data must be
copied via the Tube FIFO registers (with delays to accommodate the
slow 16032 co-processor) instead of direct memory access.""")
d.comment(0x8B1F, 'Y=4: check param block byte 4', align=Align.INLINE)
d.comment(0x8B21, 'Check if destination is in Tube space', align=Align.INLINE)
d.comment(0x8B24, 'No Tube: skip Tube address check', align=Align.INLINE)
d.comment(0x8B26, 'Compare Tube flag with addr byte 4', align=Align.INLINE)
d.comment(0x8B28, 'Mismatch: not Tube space', align=Align.INLINE)
d.comment(0x8B2B, 'Y=3: subtract addr byte 3 from flag', align=Align.INLINE)
d.comment(0x8B2D, 'Non-zero = Tube transfer required', align=Align.INLINE)
d.comment(0x8B2F, 'Copy param block bytes 1-4 to workspace', align=Align.INLINE)
d.comment(0x8B31, 'Store to &BD+Y workspace area', align=Align.INLINE)
d.comment(0x8B34, 'Previous byte', align=Align.INLINE)
d.comment(0x8B35, 'Loop for bytes 3,2,1', align=Align.INLINE)
d.comment(0x8B37, 'Sub-function: AND #3 of (original A - 4)', align=Align.INLINE)
d.comment(0x8B38, 'Mask to 0-3 (OSGBPB 5-8 → 0-3)', align=Align.INLINE)
d.comment(0x8B3A, 'A=0 (OSGBPB 5): read disc title', align=Align.INLINE)
d.comment(0x8B3C, 'LSR: A=0 (OSGBPB 6) or A=1 (OSGBPB 7)', align=Align.INLINE)
d.comment(0x8B3D, 'A=0 (OSGBPB 6): read CSD/LIB name', align=Align.INLINE)
d.comment(0x8B3F, 'C=1 (OSGBPB 8): read filenames from dir', align=Align.INLINE)
d.comment(0x8B41, 'Y=0 for CSD or carry for fn code select', align=Align.INLINE)
d.comment(0x8B42, 'Get CSD/LIB/URD handles for FS command', align=Align.INLINE)
d.comment(0x8B45, 'Store CSD handle in command buffer', align=Align.INLINE)
d.comment(0x8B48, 'Load LIB handle from workspace', align=Align.INLINE)
d.comment(0x8B4B, 'Store LIB handle in command buffer', align=Align.INLINE)
d.comment(0x8B4E, 'Load URD handle from workspace', align=Align.INLINE)
d.comment(0x8B51, 'Store URD handle in command buffer', align=Align.INLINE)
d.comment(0x8B54, 'X=&12: buffer extent for command data', align=Align.INLINE)
d.comment(0x8B56, 'Store X as function code in header', align=Align.INLINE)
d.comment(0x8B59, '&0D = 13 bytes of reply data expected', align=Align.INLINE)
d.comment(0x8B5B, 'Store reply length in command buffer', align=Align.INLINE)
d.comment(0x8B5E, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8B60, 'LSR: &0D >> 1 = 6', align=Align.INLINE)
d.comment(0x8B61, 'Store as command data byte', align=Align.INLINE)
d.comment(0x8B64, 'CLC for standard FS path', align=Align.INLINE)
d.comment(0x8B6A, 'INX: X=1 after build_send_fs_cmd', align=Align.INLINE)
d.comment(0x8B6B, 'Store X as reply start offset', align=Align.INLINE)
d.comment(0x8B6D, "Copy FS reply to caller's buffer", align=Align.INLINE)
d.comment(0x8B6F, 'Non-zero: use Tube transfer path', align=Align.INLINE)
d.comment(0x8B71, 'X = reply start offset', align=Align.INLINE)
d.comment(0x8B73, 'Y = reply buffer high byte', align=Align.INLINE)
d.comment(0x8B75, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B78, "Store to caller's buffer", align=Align.INLINE)
d.comment(0x8B7A, 'Next source byte', align=Align.INLINE)
d.comment(0x8B7B, 'Next destination byte', align=Align.INLINE)
d.comment(0x8B7C, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8B7E, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x8B80, 'ALWAYS branch to exit', align=Align.INLINE)
d.comment(0x8B82, 'Claim Tube transfer channel', align=Align.INLINE)
d.comment(0x8B85, 'A=1: Tube claim type 1 (write)', align=Align.INLINE)
d.comment(0x8B87, 'X = param block address low', align=Align.INLINE)
d.comment(0x8B89, 'Y = param block address high', align=Align.INLINE)
d.comment(0x8B8B, 'INX: advance past byte 0', align=Align.INLINE)
d.comment(0x8B8C, 'No page wrap: keep Y', align=Align.INLINE)
d.comment(0x8B8E, 'Page wrap: increment high byte', align=Align.INLINE)
d.comment(0x8B8F, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x8B92, 'X = reply data start offset', align=Align.INLINE)
d.comment(0x8B94, 'Load reply data byte', align=Align.INLINE)
d.comment(0x8B97, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x8B9A, 'Next source byte', align=Align.INLINE)
d.comment(0x8B9B, 'Delay loop for slow Tube co-processor', align=Align.INLINE)
d.comment(0x8B9D, 'Decrement delay counter', align=Align.INLINE)
d.comment(0x8B9E, 'Loop until delay complete', align=Align.INLINE)
d.comment(0x8BA0, 'Decrement remaining bytes', align=Align.INLINE)
d.comment(0x8BA2, 'Loop until all bytes sent to Tube', align=Align.INLINE)
d.comment(0x8BA4, 'Release Tube after transfer complete', align=Align.INLINE)
d.comment(0x8BA6, 'Release Tube address claim', align=Align.INLINE)
d.comment(0x8BA9, 'Return via restore_args path', align=Align.INLINE)
d.comment(0x8BAC, 'OSGBPB 8: read filenames from dir', align=Align.INLINE)
d.comment(0x8BAE, 'Byte 9: number of entries to read', align=Align.INLINE)
d.comment(0x8BB0, 'Store as reply count in command buffer', align=Align.INLINE)
d.comment(0x8BB3, 'Y=5: byte 5 = starting entry number', align=Align.INLINE)
d.comment(0x8BB5, 'Load starting entry number', align=Align.INLINE)
d.comment(0x8BB7, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8BBA, 'X=&0D: command data extent', align=Align.INLINE)
d.comment(0x8BBC, 'Store extent in command buffer', align=Align.INLINE)
d.comment(0x8BBF, 'Y=2: function code for dir read', align=Align.INLINE)
d.comment(0x8BC1, 'Store 2 as reply data start offset', align=Align.INLINE)
d.comment(0x8BC3, 'Store 2 as command data byte', align=Align.INLINE)
d.comment(0x8BC6, 'Y=3: function code for header read', align=Align.INLINE)
d.comment(0x8BCA, 'X=0 after FS command completes', align=Align.INLINE)
d.comment(0x8BCC, 'Load reply entry count', align=Align.INLINE)
d.comment(0x8BCF, 'Store at param block byte 0 (X=0)', align=Align.INLINE)
d.comment(0x8BD1, 'Load entries-read count from reply', align=Align.INLINE)
d.comment(0x8BD4, 'Y=9: param block byte 9', align=Align.INLINE)
d.comment(0x8BD6, 'Add to starting entry number', align=Align.INLINE)
d.comment(0x8BD8, 'Update param block with new position', align=Align.INLINE)
d.comment(0x8BDA, 'Load total reply length', align=Align.INLINE)
d.comment(0x8BDC, 'Subtract header (7 bytes) from reply len', align=Align.INLINE)
d.comment(0x8BDE, 'Store adjusted length in command buffer', align=Align.INLINE)
d.comment(0x8BE1, 'Store as byte count for copy loop', align=Align.INLINE)
d.comment(0x8BE3, 'Zero bytes: skip copy', align=Align.INLINE)
d.comment(0x8BE5, "Copy reply data to caller's buffer", align=Align.INLINE)
d.comment(0x8BE8, 'X=2: clear 3 bytes', align=Align.INLINE)
d.comment(0x8BEA, 'Zero out &0F07+X area', align=Align.INLINE)
d.comment(0x8BED, 'Next byte', align=Align.INLINE)
d.comment(0x8BEE, 'Loop for X=2,1,0', align=Align.INLINE)
d.comment(0x8BF0, 'Adjust pointer by +1 (one filename read)', align=Align.INLINE)
d.comment(0x8BF3, 'SEC for reverse adjustment', align=Align.INLINE)
d.comment(0x8BF4, 'Reverse adjustment for updated counter', align=Align.INLINE)
d.comment(0x8BF6, 'Load entries-read count', align=Align.INLINE)
d.comment(0x8BF9, 'Store in command buffer', align=Align.INLINE)
d.comment(0x8BFC, 'Adjust param block addresses', align=Align.INLINE)
d.comment(0x8BFF, 'Z=1: all done, exit', align=Align.INLINE)
d.comment(0x8C01, 'A=&C3: Tube claim with retry', align=Align.INLINE)
d.comment(0x8C03, 'Request Tube address claim', align=Align.INLINE)
d.comment(0x8C06, 'C=0: claim failed, retry', align=Align.INLINE)
d.comment(0x8C08, 'Tube claimed successfully', align=Align.INLINE)


d.subroutine(0x80BD, 'forward_star_cmd', title='Forward unrecognised * command to fileserver (COMERR)', description="""Copies command text from (fs_crc_lo) to &0F05+ via copy_filename,
prepares an FS command with function code 0, and sends it to the
fileserver to request decoding. The server returns a command code
indicating what action to take (e.g. code 4=INFO, 7=DIR, 9=LIB,
5=load-as-command). This mechanism allows the fileserver to extend
the client's command set without ROM updates. Called from the "I."
and catch-all entries in the command match table at &8C4B, and
from FSCV 2/3/4 indirectly. If CSD handle is zero (not logged
in), returns without sending.""")


d.subroutine(0x83AE, 'bye_handler', title='*BYE handler (logoff)', description="""Closes any open *SPOOL and *EXEC files via OSBYTE &77 (FXSPEX),
then falls into prepare_fs_cmd with Y=&17 (FCBYE: logoff code).
Dispatched from the command match table at &8C4B for "BYE".""")


d.subroutine(0x8C09, 'fscv_3_star_cmd', title='FSCV 2/3/4: unrecognised * command handler (DECODE)', description="""CLI parser originally by Sophie Wilson (co-designer of ARM). Matches command text against the table
at &8C4B using case-insensitive comparison with abbreviation
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
d.comment(0x8C09, 'Save A/X/Y and set up command ptr', align=Align.INLINE)
d.comment(0x8C0C, 'X=&FF: table index (pre-incremented)', align=Align.INLINE)
d.comment(0x8C0E, 'Disable column formatting', align=Align.INLINE)
d.comment(0x8C10, 'Enable escape checking', align=Align.INLINE)
d.comment(0x8C12, 'Y=&FF: input index (pre-incremented)', align=Align.INLINE)
d.comment(0x8C14, 'Advance input pointer', align=Align.INLINE)
d.comment(0x8C15, 'Advance table pointer', align=Align.INLINE)
d.comment(0x8C16, 'Load table character', align=Align.INLINE)
d.comment(0x8C19, 'Bit 7: end of name, dispatch', align=Align.INLINE)
d.comment(0x8C1B, 'XOR input char with table char', align=Align.INLINE)
d.comment(0x8C1D, 'Case-insensitive (clear bit 5)', align=Align.INLINE)
d.comment(0x8C1F, 'Match: continue comparing', align=Align.INLINE)
d.comment(0x8C21, 'Mismatch: back up table pointer', align=Align.INLINE)
d.comment(0x8C22, 'Skip to end of table entry', align=Align.INLINE)
d.comment(0x8C23, 'Load table byte', align=Align.INLINE)
d.comment(0x8C26, 'Loop until bit 7 set (end marker)', align=Align.INLINE)
d.comment(0x8C28, "Check input for '.' abbreviation", align=Align.INLINE)
d.comment(0x8C2A, 'Skip past handler high byte', align=Align.INLINE)
d.comment(0x8C2B, "Is input '.' (abbreviation)?", align=Align.INLINE)
d.comment(0x8C2D, 'No: try next table entry', align=Align.INLINE)
d.comment(0x8C2F, "Yes: skip '.' in input", align=Align.INLINE)
d.comment(0x8C30, 'Back to handler high byte', align=Align.INLINE)
d.comment(0x8C31, 'ALWAYS branch; dispatch via BMI', align=Align.INLINE)
d.comment(0x8C33, 'Push handler address high byte', align=Align.INLINE)
d.comment(0x8C34, 'Load handler address low byte', align=Align.INLINE)
d.comment(0x8C37, 'Push handler address low byte', align=Align.INLINE)
d.comment(0x8C38, 'Dispatch via RTS (addr-1 on stack)', align=Align.INLINE)


d.subroutine(0x8C39, 'fs_cmd_match_table', title='FS command match table (COMTAB)', description="""Format: command letters (bit 7 clear), then dispatch address
as two big-endian bytes: high|(bit 7 set), low. The bit 7 set
on the high byte marks the end of the command string. The
PHA/PHA/RTS trick adds 1 to the stored (address-1). Matching
is case-insensitive (AND &DF) and supports '.' abbreviation.

Entries:
  "I."     → &80BD (forward_star_cmd) — placed first as a fudge
             to catch *I. abbreviation before matching *I AM
  "I AM"   → &8082 (i_am_handler: parse station.net, logon)
  "}EX"    → &8C4F (ex_handler: } terminator rejects *EXEC)
  "BYE"\\r  → &83AE (bye_handler: logoff)
  <catch-all> → &80BD (forward anything else to FS)""")
d.comment(0x8C39, "Match last char against '.' for *I. abbreviation", align=Align.INLINE)
d.byte(0x8C3B)
d.byte(0x8C3C)
d.string(0x8C3D, 4)
d.byte(0x8C41)
d.string(0x8C42, 3)
d.byte(0x8C45)
d.string(0x8C46, 4)
d.byte(0x8C4A)
d.byte(0x8C4B)
d.byte(0x8C4C)
d.byte(0x8C4D)
d.byte(0x8C4E)
d.comment(0x8C3B, 'I. handler hi → &80BD (forward_star_cmd)', align=Align.INLINE)
d.comment(0x8C3C, 'I. handler lo', align=Align.INLINE)
d.comment(0x8C3D, '"I AM" command string', align=Align.INLINE)
d.comment(0x8C41, 'I AM handler hi (shared lo for I.)', align=Align.INLINE)
d.comment(0x8C42, '"}EX" command (} = special terminator)', align=Align.INLINE)
d.comment(0x8C45, 'EX handler hi → &8C4F (ex_handler)', align=Align.INLINE)
d.comment(0x8C46, '"NBYE" command (BYE with N prefix)', align=Align.INLINE)
d.comment(0x8C4A, 'CR terminator for BYE', align=Align.INLINE)
d.comment(0x8C4B, 'BYE handler hi → &83AE (bye_handler)', align=Align.INLINE)
d.comment(0x8C4C, 'BYE handler lo', align=Align.INLINE)
d.comment(0x8C4D, 'Catch-all hi → &80BD (forward_star_cmd)', align=Align.INLINE)
d.comment(0x8C4E, 'Catch-all lo', align=Align.INLINE)
d.comment(0x8C4F, 'X=1: force one entry per line for *EX', align=Align.INLINE)
d.comment(0x8C51, 'A=3: examine format code', align=Align.INLINE)
d.entry(0x8C4F)

d.label(0x8C4F, 'ex_handler')


d.subroutine(0x8C55, 'fscv_5_cat', title='*CAT handler (directory catalogue)', description="""Initialises &B5=&0B (examine arg count) and &B7=&03 (column
count). The catalogue protocol is multi-step: first sends
FCREAD (&12: examine) to get the directory header, then sends
FCUSER (&15: read user environment) to get CSD, disc, and
library names, then sends FC &03 (examine entries) repeatedly
to fetch entries in batches until zero are returned (end of dir).
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
  - Directory entries: CRFLAG (&B9) cycles 0-3 for multi-column
    layout; at count 0 a newline is printed, others get spaces.
    *EX sets CRFLAG=&FF to force one entry per line.""")
d.comment(0x8C57, 'CRFLAG=3: first entry will trigger newline', align=Align.INLINE)
d.comment(0x8C8E, 'Access level byte: 0=Owner, non-zero=Public', align=Align.INLINE)
d.comment(0x8D1C, 'Zero entries returned = end of directory', align=Align.INLINE)
d.comment(0x8C55, 'X=3: column count for multi-column layout', align=Align.INLINE)
d.comment(0x8C59, 'Y=&FF: mark as escapable', align=Align.INLINE)
d.comment(0x8C5B, 'Store escapable flag for Escape checking', align=Align.INLINE)
d.comment(0x8C5E, 'A=&0B: examine argument count', align=Align.INLINE)
d.comment(0x8C60, 'Store examine argument count', align=Align.INLINE)
d.comment(0x8C62, 'Store column count', align=Align.INLINE)
d.comment(0x8C64, 'A=6: examine format type in command', align=Align.INLINE)
d.comment(0x8C66, 'Store format type at &0F05', align=Align.INLINE)
d.comment(0x8C69, 'Set up command parameter pointers', align=Align.INLINE)
d.comment(0x8C6C, 'X=1: copy dir name at cmd offset 1', align=Align.INLINE)
d.comment(0x8C6E, 'Copy directory name to command buffer', align=Align.INLINE)
d.comment(0x8C76, 'X=3: start printing from reply offset 3', align=Align.INLINE)
d.comment(0x8C78, 'Print directory title (10 chars)', align=Align.INLINE)
d.comment(0x8C7B, "Print '('", align=Align.INLINE)
d.comment(0x8C7E, '"(" inline string data', align=Align.INLINE)
d.comment(0x8C7F, 'Load station number from FS reply', align=Align.INLINE)
d.comment(0x8C82, 'Print station number as decimal', align=Align.INLINE)
d.comment(0x8C85, "Print ')     '", align=Align.INLINE)
d.comment(0x8C88, '")     " inline string data', align=Align.INLINE)
d.comment(0x8C91, 'Non-zero: Public access', align=Align.INLINE)
d.comment(0x8C93, "Print 'Owner' + CR", align=Align.INLINE)
d.comment(0x8C96, '"Owner" + CR inline string data', align=Align.INLINE)
d.comment(0x8C9C, 'Always branches (print_inline sets N=1)', align=Align.INLINE)
d.comment(0x8C9E, "Print 'Public' + CR", align=Align.INLINE)
d.comment(0x8CA1, '"Public" + CR inline string data', align=Align.INLINE)
d.comment(0x8CAD, 'X=1: past command code byte', align=Align.INLINE)
d.comment(0x8CAE, 'Y=&10: print 16 characters', align=Align.INLINE)
d.comment(0x8CB0, 'Print disc/CSD name from reply', align=Align.INLINE)
d.comment(0x8CB3, "Print '    Option '", align=Align.INLINE)
d.comment(0x8CB6, '"    Option " inline string data', align=Align.INLINE)
d.comment(0x8CC1, 'Load boot option from workspace', align=Align.INLINE)
d.comment(0x8CC4, 'X = boot option for name table lookup', align=Align.INLINE)
d.comment(0x8CC5, 'Print boot option as hex digit', align=Align.INLINE)
d.comment(0x8CC8, "Print ' ('", align=Align.INLINE)
d.comment(0x8CCB, '" (" inline string data', align=Align.INLINE)
d.comment(0x8CCD, 'Load string offset for option name', align=Align.INLINE)
d.comment(0x8CD0, 'Load character from option name string', align=Align.INLINE)
d.comment(0x8CD3, 'Bit7 set: string terminated, done', align=Align.INLINE)
d.comment(0x8CD8, 'Next character', align=Align.INLINE)
d.comment(0x8CD9, 'Continue printing option name', align=Align.INLINE)
d.comment(0x8CDB, "Print ')' + CR + 'Dir. '", align=Align.INLINE)
d.comment(0x8CDE, '") CR Dir. " inline string data', align=Align.INLINE)
d.comment(0x8CE5, 'X=&11: directory name offset in reply', align=Align.INLINE)
d.comment(0x8CE7, 'Print current directory name', align=Align.INLINE)
d.comment(0x8CEA, "Print '     Lib. '", align=Align.INLINE)
d.comment(0x8CED, '"     Lib. " inline string data', align=Align.INLINE)
d.comment(0x8CF7, 'X=&1B: library name offset in reply', align=Align.INLINE)
d.comment(0x8CF9, 'Print library name', align=Align.INLINE)
d.comment(0x8CFF, 'Store entry start offset for request', align=Align.INLINE)
d.comment(0x8D02, 'Save start offset in zero page for loop', align=Align.INLINE)
d.comment(0x8D04, 'Load examine arg count for batch size', align=Align.INLINE)
d.comment(0x8D06, 'Store as request count at &0F07', align=Align.INLINE)
d.comment(0x8D09, 'Load column count for display format', align=Align.INLINE)
d.comment(0x8D0B, 'Store column count in command data', align=Align.INLINE)
d.comment(0x8D0E, 'X=3: copy directory name at offset 3', align=Align.INLINE)
d.comment(0x8D10, 'Append directory name to examine command', align=Align.INLINE)
d.comment(0x8D18, 'X past command code byte in reply', align=Align.INLINE)
d.comment(0x8D19, 'Load entry count from reply', align=Align.INLINE)
d.comment(0x8D21, 'Save entry count for batch processing', align=Align.INLINE)
d.comment(0x8D22, 'Advance Y past entry data bytes', align=Align.INLINE)
d.comment(0x8D23, 'Read entry byte from reply buffer', align=Align.INLINE)
d.comment(0x8D26, 'Loop until high-bit terminator found', align=Align.INLINE)
d.comment(0x8D28, 'Store terminator as print boundary', align=Align.INLINE)
d.comment(0x8D2B, 'Print/format this directory entry', align=Align.INLINE)
d.comment(0x8D2E, 'Restore entry count from stack', align=Align.INLINE)
d.comment(0x8D2F, 'CLC for addition', align=Align.INLINE)
d.comment(0x8D30, 'Advance start offset by entry count', align=Align.INLINE)
d.comment(0x8D32, 'Y = new entry start offset', align=Align.INLINE)
d.comment(0x8D33, 'More entries: fetch next batch', align=Align.INLINE)
d.comment(0x8D35, 'Y=&0A: default print 10 characters', align=Align.INLINE)
d.comment(0x8D37, 'Load reply byte at offset X', align=Align.INLINE)
d.comment(0x8D3D, 'Next reply byte', align=Align.INLINE)
d.comment(0x8D3E, 'Decrement character count', align=Align.INLINE)
d.comment(0x8D3F, 'Loop for remaining characters', align=Align.INLINE)
d.comment(0x8D42, 'Boot option name offsets (4 entries)', align=Align.INLINE)
d.comment(0x8D45, 'Offset &18: Exec option name start', align=Align.INLINE)
d.comment(0x8D46, 'Boot option name string data "L.!"', align=Align.INLINE)


d.subroutine(0x8D49, 'boot_cmd_strings', title='Boot command strings for auto-boot', description="""The four boot options use OSCLI strings at offsets within page &8D.
The offset table at boot_option_offsets+1 is indexed by
the boot option value (0-3); each byte is the low byte of the
string address, with the page high byte loaded separately:
  Option 0 (Off):  offset &55 → boot_option_offsets = bare CR
  Option 1 (Load): offset &46 → "L.!BOOT" (the bytes
      &4C='L', &2E='.', &21='!' precede "BOOT" + CR at &8D4D)
  Option 2 (Run):  offset &48 → boot_cmd_strings-1 = "!BOOT"
  Option 3 (Exec): offset &4E → &8D4E = "E.!BOOT"

This is a classic BBC ROM space optimisation: the string data
overlaps with other byte sequences to save space. The &0D byte
at &8D55 terminates "E.!BOOT" AND doubles as the bare-CR
command for boot option 0.""")
d.comment(0x8D49, '"BOOT" command string tail', align=Align.INLINE)
d.comment(0x8D4D, 'CR terminator for BOOT string', align=Align.INLINE)
d.comment(0x8D4E, '"E.!BOOT" exec boot command', align=Align.INLINE)


d.subroutine(0x8D55, 'boot_option_offsets', title='Boot option → OSCLI string offset table', description="""Five bytes: the first byte (&0D) is the bare-CR target for boot
option 0; bytes 1-4 are the offset table indexed by boot option
(0-3). Each offset is the low byte of a pointer into page &8D.
The code reads from boot_option_offsets+1 (&8D68) via
LDX l8d56,Y with Y=boot_option, then LDY #&8D, JMP oscli.
See boot_cmd_strings for the target strings.""")
for i in range(5):
    d.byte(0x8D67 + i)
d.comment(0x8D56, 'Opt 0 (Off): bare CR at &8D55', align=Align.INLINE)
d.comment(0x8D57, 'Opt 1 (Load): L.!BOOT at &8D46', align=Align.INLINE)
d.comment(0x8D58, 'Opt 2 (Run): !BOOT at boot_cmd_strings-1', align=Align.INLINE)
d.comment(0x8D59, 'Opt 3 (Exec): E.!BOOT at &8D4E', align=Align.INLINE)
d.comment(0x8D5C, 'Boot string overlap: "ec" tail of "Exec"', align=Align.INLINE)
d.comment(0x8D5E, 'X=4: print 4 hex bytes', align=Align.INLINE)
d.comment(0x8D60, 'Load byte from parameter block', align=Align.INLINE)
d.comment(0x8D62, 'Print as two hex digits', align=Align.INLINE)
d.comment(0x8D65, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8D66, 'Count down', align=Align.INLINE)
d.comment(0x8D67, 'Loop until 4 bytes printed', align=Align.INLINE)
d.comment(0x8D68, 'BNE operand (also boot offset data)', align=Align.INLINE)
d.comment(0x8D69, 'A=space character', align=Align.INLINE)
d.comment(0x8D6A, 'LDA #&20 operand (space)', align=Align.INLINE)
d.comment(0x8D6B, 'BNE opcode (also string overlap)', align=Align.INLINE)
d.comment(0x8D6C, 'Boot option name "Exec" starts here', align=Align.INLINE)
d.comment(0x8D41, """Option name encoding: the boot option names ("Off", "Load",
"Run", "Exec") are scattered through the code rather than
stored as a contiguous table. They are addressed via base+offset
from option_name_offsets (&8D42), whose four bytes are offsets:
  &2B→option_name_offsets+&2B "Off",
  &3E→option_name_offsets+&3E "Load",
  &66→option_name_offsets+&66 "Run",
  &18→option_name_offsets+&18 "Exec"
Each string is terminated by the next instruction's opcode
having bit 7 set (e.g. LDA #imm = &A9, RTS = &60).""")


d.subroutine(0x807E, 'i_am_handler', title='"I AM" command handler', description="""Dispatched from the command match table when the user types
"*I AM <station>" or "*I AM <network>.<station>". Also used as
the station number parser for "*NET <network>.<station>".
Skips leading spaces, then calls parse_decimal for the first
number. If a dot separator was found (carry set), it stores the
result directly as the network (&0E01) and calls parse_decimal
again for the station (&0E00). With a single number, it is stored
as the station and the network defaults to 0 (local). If a colon
follows, reads interactive input via OSRDCH and appends it to
the command buffer. Finally jumps to forward_star_cmd.""")
d.comment(0x807E, 'Load next char from command line', align=Align.INLINE)
d.comment(0x8080, 'Skip spaces', align=Align.INLINE)
d.comment(0x8082, 'Loop back to skip leading spaces', align=Align.INLINE)
d.comment(0x8084, 'Colon = interactive remote command prefix', align=Align.INLINE)
d.comment(0x8086, "Char >= ':': skip number parsing", align=Align.INLINE)
d.comment(0x808B, 'C=1: dot found, first number was network', align=Align.INLINE)
d.comment(0x808D, 'Store network number (n.s = network.station)', align=Align.INLINE)
d.comment(0x8094, 'Z=1: no station parsed (empty or non-numeric)', align=Align.INLINE)
d.comment(0x8099, 'Copy command text to FS buffer', align=Align.INLINE)
d.comment(0x809C, "Scan backward for ':' (interactive prefix)", align=Align.INLINE)
d.comment(0x809D, 'Y=0: no colon found, send command', align=Align.INLINE)
d.comment(0x809F, 'Read char from FS command buffer', align=Align.INLINE)
d.comment(0x80A2, 'Test for colon separator', align=Align.INLINE)
d.comment(0x80A4, 'Not colon: keep scanning backward', align=Align.INLINE)
d.comment(0x80A6, 'Echo colon, then read user input from keyboard', align=Align.INLINE)
d.comment(0x80A9, 'Check for escape condition', align=Align.INLINE)
d.comment(0x80AF, 'Append typed character to command buffer', align=Align.INLINE)
d.comment(0x80B2, 'Advance write pointer', align=Align.INLINE)
d.comment(0x80B3, 'Increment character count', align=Align.INLINE)
d.comment(0x80B4, 'Test for CR (end of line)', align=Align.INLINE)
d.comment(0x80B6, 'Not CR: continue reading input', align=Align.INLINE)
d.comment(0x80BB, 'After OSNEWL: loop back to scan for colon', align=Align.INLINE)


d.subroutine(0x8E30, 'fsreply_5_set_lib', title='Set library handle', description="""Stores Y into &0E04 (library directory handle in FS workspace).
Falls through to JMP restore_args_return if Y is non-zero.""", on_entry={'y': 'library handle from FS reply'})
d.comment(0x8E30, 'Save library handle from FS reply', align=Align.INLINE)
d.comment(0x8E33, 'SDISC path: skip CSD, jump to return', align=Align.INLINE)


d.subroutine(0x8E35, 'fsreply_3_set_csd', title='Set CSD handle', description="""Stores Y into &0E03 (current selected directory handle).
Falls through to JMP restore_args_return.""", on_entry={'y': 'CSD handle from FS reply'})
d.comment(0x8E35, 'Store CSD handle from FS reply', align=Align.INLINE)
d.comment(0x8E38, 'Restore A/X/Y and return to caller', align=Align.INLINE)


d.subroutine(0x8E3B, 'fsreply_1_copy_handles_boot', title='Copy FS reply handles to workspace and execute boot command', description="""SEC entry (LOGIN): copies 4 bytes from &0F05-&0F08 (FS reply) to
&0E02-&0E05 (URD, CSD, LIB handles and boot option), then
looks up the boot option in boot_option_offsets to get the
OSCLI command string and executes it via JMP oscli.
The carry flag distinguishes LOGIN (SEC) from SDISC (CLC) — both
share the handle-copying code, but only LOGIN executes the boot
command. This use of the carry flag to select behaviour between
two callers avoids duplicating the handle-copy loop.""")
d.comment(0x8E3B, 'Set carry: LOGIN path (copy + boot)', align=Align.INLINE)


d.subroutine(0x8E3C, 'fsreply_2_copy_handles', title='Copy FS reply handles to workspace (no boot)', description="""CLC entry (SDISC): copies handles only, then jumps to
restore_args_return via jmp_restore_args. Called when the FS reply contains
updated handle values but no boot action is needed.""")
d.comment(0x8E3C, 'Copy 4 bytes: boot option + 3 handles', align=Align.INLINE)
d.comment(0x8E3E, 'SDISC: skip boot option, copy handles only', align=Align.INLINE)
d.comment(0x8E40, 'Load from FS reply (&0F05+X)', align=Align.INLINE)
d.comment(0x8E43, 'Store to handle workspace (&0E02+X)', align=Align.INLINE)
d.comment(0x8E46, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8E47, 'Loop while X >= 0', align=Align.INLINE)
d.comment(0x8E49, 'SDISC: done, restore args and return', align=Align.INLINE)


d.subroutine(0x8D70, 'copy_filename', title='Copy filename to FS command buffer', description="""Entry with X=0: copies from (fs_crc_lo),Y to &0F05+X until CR.
Used to place a filename into the FS command buffer before
sending to the fileserver. Falls through to copy_string_to_cmd.""", on_exit={'x': 'next free position in cmd buffer', 'y': 'string length (incl CR)', 'a': '0 (from EOR &0D with final CR)'})
d.comment(0x8D70, 'Start writing at &0F05 (after cmd header)', align=Align.INLINE)


d.subroutine(0x8D72, 'copy_string_to_cmd', title='Copy string to FS command buffer', description="""Entry with X and Y specified: copies bytes from (fs_crc_lo),Y
to &0F05+X, stopping when a CR (&0D) is encountered. The CR
itself is also copied. Returns with X pointing past the last
byte written.""", on_entry={'x': 'destination offset in fs_cmd_data (&0F05+X)'}, on_exit={'x': 'next free position past CR', 'y': 'string length (incl CR)', 'a': '0 (from EOR &0D with final CR)'})
d.comment(0x8D76, 'Store to FS command buffer (&0F05+X)', align=Align.INLINE)
d.comment(0x8D7A, 'Advance source pointer', align=Align.INLINE)
d.comment(0x8D7B, 'XOR with CR: result=0 if byte was CR', align=Align.INLINE)
d.comment(0x8D7D, 'Loop until CR copied', align=Align.INLINE)
d.comment(0x8D7F, 'Return; X = next free position in buffer', align=Align.INLINE)
d.comment(0x8D80, '"Load" boot option name string', align=Align.INLINE)


d.subroutine(0x8D8D, 'cat_column_separator', title='Print catalogue column separator or newline', description="""Handles column formatting for *CAT display. On a null byte
separator, advances the column counter modulo 4: prints a
2-space separator between columns, or a CR at column 0.
Called from fsreply_0_print_dir.""")


d.subroutine(0x8D84, 'fsreply_0_print_dir', title='Print directory name from reply buffer', description="""Prints characters from the FS reply buffer (&0F05+X onwards).
Null bytes (&00) are replaced with CR (&0D) for display.
Stops when a byte with bit 7 set is encountered (high-bit
terminator). Used by fscv_5_cat to display Dir. and Lib. paths.""")
d.comment(0x8D84, 'X=0: start from first reply byte', align=Align.INLINE)
d.comment(0x8D86, 'Load byte from FS reply buffer', align=Align.INLINE)
d.comment(0x8D89, 'Bit 7 set: end of string, return', align=Align.INLINE)
d.comment(0x8D8B, 'Non-zero: print character', align=Align.INLINE)
d.comment(0x8D8D, 'Null byte: check column counter', align=Align.INLINE)
d.comment(0x8D8F, 'Negative: print CR (no columns)', align=Align.INLINE)
d.comment(0x8D91, 'Advance column counter', align=Align.INLINE)
d.comment(0x8D92, 'Transfer to A for modulo', align=Align.INLINE)
d.comment(0x8D93, 'Modulo 4 columns', align=Align.INLINE)
d.comment(0x8D95, 'Update column counter', align=Align.INLINE)
d.comment(0x8D97, 'Column 0: start new line', align=Align.INLINE)
d.comment(0x8D99, 'Print 2-space column separator', align=Align.INLINE)
d.comment(0x8D9C, '"  " column separator string', align=Align.INLINE)
d.comment(0x8D9E, 'ALWAYS branch to next byte', align=Align.INLINE)
d.comment(0x8DA0, 'CR = carriage return', align=Align.INLINE)
d.comment(0x8DA5, 'Next byte in reply buffer', align=Align.INLINE)
d.comment(0x8DA6, 'Loop until end of buffer', align=Align.INLINE)
d.comment(0x8DA8, '"Run" boot option name string', align=Align.INLINE)


d.subroutine(0x8DDF, 'fscv_2_star_run', title='FSCV 2/4: */ (run) and *RUN handler', description="""Parses the filename via parse_filename_gs and calls infol2,
then falls through to fsreply_4_notify_exec to set up and
send the FS load-as-command request.""")
d.comment(0x8DDF, 'Parse filename from command line', align=Align.INLINE)
d.comment(0x8DE2, 'Copy filename to FS command buffer', align=Align.INLINE)


d.subroutine(0x8DE5, 'fsreply_4_notify_exec', title='FS reply 4: send FS load-as-command and execute response', description="""Initialises a GS reader to skip past the filename and
calculate the command context address, then sets up an FS
command with function code &05 (FCCMND: load as command)
using send_fs_examine. If a Tube co-processor is present
(tube_flag != 0), transfers the response data to the Tube
via tube_addr_claim. Otherwise jumps via the indirect
pointer at (&0F09) to execute at the load address.""")
d.comment(0x8DE5, 'Y=0: start of text for GSINIT', align=Align.INLINE)
d.comment(0x8DE7, 'CLC before GSINIT call', align=Align.INLINE)
d.comment(0x8DE8, 'GSINIT/GSREAD: skip past the filename', align=Align.INLINE)
d.comment(0x8DEB, 'Read next filename character', align=Align.INLINE)
d.comment(0x8DEE, 'C=0: more characters, keep reading', align=Align.INLINE)
d.comment(0x8DF0, 'Skip spaces after filename', align=Align.INLINE)
d.comment(0x8DF3, 'Calculate context addr = text ptr + Y', align=Align.INLINE)
d.comment(0x8DF4, 'Y = offset past filename end', align=Align.INLINE)
d.comment(0x8DF5, 'Add text pointer low byte', align=Align.INLINE)
d.comment(0x8DF7, 'Store context address low byte', align=Align.INLINE)
d.comment(0x8DFA, 'Load text pointer high byte', align=Align.INLINE)
d.comment(0x8DFC, 'Add carry from low byte addition', align=Align.INLINE)
d.comment(0x8DFE, 'Store context address high byte', align=Align.INLINE)
d.comment(0x8E01, 'X=&0E: FS command buffer offset', align=Align.INLINE)
d.comment(0x8E03, 'Store block offset for FS command', align=Align.INLINE)
d.comment(0x8E05, 'A=&10: 16 bytes of command data', align=Align.INLINE)
d.comment(0x8E07, 'Store options byte', align=Align.INLINE)
d.comment(0x8E09, 'Store to FS workspace', align=Align.INLINE)
d.comment(0x8E0C, 'X=&4A: TXCB size for load command', align=Align.INLINE)
d.comment(0x8E0E, 'Y=5: FCCMND (load as command)', align=Align.INLINE)
d.comment(0x8E10, 'Send FS examine/load command', align=Align.INLINE)
d.comment(0x8E13, 'Check for Tube co-processor', align=Align.INLINE)
d.comment(0x8E16, 'No Tube: execute locally', align=Align.INLINE)
d.comment(0x8E18, 'Check load address upper bytes', align=Align.INLINE)
d.comment(0x8E1B, 'Continue address range check', align=Align.INLINE)
d.comment(0x8E1E, 'Carry set: not Tube space, exec locally', align=Align.INLINE)
d.comment(0x8E20, 'Claim Tube transfer channel', align=Align.INLINE)
d.comment(0x8E23, 'X=9: source offset in FS reply', align=Align.INLINE)
d.comment(0x8E25, 'Y=&0F: page &0F (FS command buffer)', align=Align.INLINE)
d.comment(0x8E27, 'A=4: Tube transfer type 4 (256-byte)', align=Align.INLINE)
d.comment(0x8E29, 'Transfer data to Tube co-processor', align=Align.INLINE)
d.comment(0x8E2C, 'ROL: restore A (undo ADC carry)', align=Align.INLINE)
d.comment(0x8E2D, 'Execute at load address via indirect JMP', align=Align.INLINE)


d.subroutine(0x8E56, 'load_handle_calc_offset', title='Load handle from &F0 and calculate workspace offset', description="""Loads the file handle byte from &F0, then falls through to
calc_handle_offset which converts handle * 12 to a workspace
byte offset. Validates offset < &48.""", on_exit={'a': 'handle*12 or 0 if invalid', 'y': 'workspace offset or 0 if invalid', 'c': 'clear if valid, set if invalid'})


d.subroutine(0x8E4B, 'boot_cmd_execute', title='Execute boot command via OSCLI', description="""Reached from fsreply_1_copy_handles_boot when carry is set (LOGIN
path). Reads the boot option from fs_boot_option (&0E05),
looks up the OSCLI command string offset from boot_option_offsets+1,
and executes the boot command via JMP oscli with page &8D.""")
d.comment(0x8E4B, 'Y = boot option from FS workspace', align=Align.INLINE)
d.comment(0x8E4E, 'X = command string offset from table', align=Align.INLINE)
d.comment(0x8E51, 'Y = &8D (high byte of command address)', align=Align.INLINE)
d.comment(0x8E53, 'Execute boot command string via OSCLI', align=Align.INLINE)
d.comment(0x8E56, 'Load handle from &F0', align=Align.INLINE)
d.entry(0x8E6A)

d.label(0x8E6A, 'net_1_read_handle')
d.comment(0x8E6A, """*NET1: read file handle from received packet.
Reads a byte from offset &6F of the RX buffer (net_rx_ptr)
and falls through to net_2_read_handle_entry's common path.""")


d.subroutine(0x8E58, 'calc_handle_offset', title='Calculate handle workspace offset', description="""Converts a file handle number (in A) to a byte offset (in Y)
into the NFS handle workspace. The calculation is A*12:
  ASL A (A*2), ASL A (A*4), PHA, ASL A (A*8),
  ADC stack (A*8 + A*4 = A*12).
Validates that the offset is < &48 (max 6 handles × 12 bytes
per handle entry = 72 bytes). If invalid (>= &48), returns
with C set and Y=0, A=0 as an error indicator.""", on_entry={'a': 'file handle number'}, on_exit={'a': 'handle*12 or 0 if invalid', 'y': 'workspace offset or 0 if invalid', 'c': 'clear if valid, set if invalid'})
d.comment(0x8E58, 'A = handle * 2', align=Align.INLINE)
d.comment(0x8E59, 'A = handle * 4', align=Align.INLINE)
d.comment(0x8E5A, 'Push handle*4 onto stack', align=Align.INLINE)
d.comment(0x8E5B, 'A = handle * 8', align=Align.INLINE)
d.comment(0x8E5D, 'A = handle*8 + handle*4 = handle*12', align=Align.INLINE)
d.comment(0x8E60, 'Y = offset into handle workspace', align=Align.INLINE)
d.comment(0x8E61, 'Clean up stack (discard handle*4)', align=Align.INLINE)
d.comment(0x8E62, 'Offset >= &48? (6 handles max)', align=Align.INLINE)
d.comment(0x8E64, 'Valid: return with C clear', align=Align.INLINE)

d.label(0x8E69, 'return_calc_handle')
d.entry(0x8E70)


d.subroutine(0x8E70, 'net_2_read_handle_entry', title='*NET2: read handle entry from workspace', description="""Looks up the handle in &F0 via calc_handle_offset. If the
workspace slot contains &3F ('?', meaning unused/closed),
returns 0. Otherwise returns the stored handle value.
Clears rom_svc_num on exit.""", on_exit={'a': 'handle value (0 if closed/invalid)'})
d.comment(0x8E70, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8E73, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8E75, 'Load stored handle value', align=Align.INLINE)
d.comment(0x8E77, '&3F = unused/closed slot marker', align=Align.INLINE)
d.comment(0x8E79, 'Slot in use: return actual value', align=Align.INLINE)
d.comment(0x8E7B, 'Return 0 for closed/invalid handle', align=Align.INLINE)
d.comment(0x8E7D, 'Store result back to &F0', align=Align.INLINE)
d.comment(0x8E7F, 'Return', align=Align.INLINE)
d.entry(0x8E80)


d.subroutine(0x8E80, 'net_3_close_handle', title='*NET3: close handle (mark as unused)', description="""Looks up the handle in &F0 via calc_handle_offset. Writes
&3F ('?') to mark the handle slot as closed in the NFS
workspace. Returns via RTS (earlier versions preserved the
carry flag across the write using ROL/ROR on rx_flags, but
3.60 simplified this).""", on_exit={'a': '&3F (close marker) or 0 if invalid'})
d.comment(0x8E80, 'Look up handle &F0 in workspace', align=Align.INLINE)
d.comment(0x8E83, 'Invalid handle: return 0', align=Align.INLINE)
d.comment(0x8E85, "&3F = '?' marks slot as unused", align=Align.INLINE)
d.comment(0x8E87, 'Write close marker to workspace slot', align=Align.INLINE)
d.comment(0x8E89, 'Return', align=Align.INLINE)


d.subroutine(0x8E8A, 'svc_8_osword', title='Filing system OSWORD entry', description="""Subtracts &0F from the command code in &EF, giving a 0-4 index
for OSWORD calls &0F-&13 (15-19). Falls through to the range
check and dispatch at osword_12_handler (&8E90).""")
d.comment(0x8E8A, 'Command code from &EF', align=Align.INLINE)
d.comment(0x8E8C, 'Subtract &0F: OSWORD &0F-&13 become indices 0-4', align=Align.INLINE)


d.subroutine(0x8EA2, 'fs_osword_dispatch', title='PHA/PHA/RTS dispatch for filing system OSWORDs', description="""Saves the param block pointer (&AA-&AC) to (net_rx_ptr) and
reads the sub-function code from (&F0)+1, then dispatches via
the 5-entry table at &8EB8 (low) / &8EBD (high) using
PHA/PHA/RTS. The RTS at the end of the dispatched handler
returns here, after which the caller restores &AA-&AC.""")
d.comment(0x8EA2, 'X = sub-function code for table lookup', align=Align.INLINE)
d.comment(0x8EA3, 'Load handler address high byte from table', align=Align.INLINE)
d.comment(0x8EA6, 'Push high byte for RTS dispatch', align=Align.INLINE)
d.comment(0x8EA7, 'Load handler address low byte from table', align=Align.INLINE)
d.comment(0x8EAA, 'Dispatch table: low bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x8EAB, 'Y=2: save 3 bytes (&AA-&AC)', align=Align.INLINE)
d.comment(0x8EAD, 'Load param block pointer byte', align=Align.INLINE)
d.comment(0x8EB0, 'Save to NFS workspace via (net_rx_ptr)', align=Align.INLINE)
d.comment(0x8EB2, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8EB3, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8EB5, 'Y=0 after BPL exit; INY makes Y=1', align=Align.INLINE)
d.comment(0x8EB6, 'Read sub-function code from (&F0)+1', align=Align.INLINE)
d.comment(0x8EB8, 'Store Y=1 to &A9', align=Align.INLINE)
d.comment(0x8EBA, 'RTS dispatches to pushed handler address', align=Align.INLINE)
d.comment(0x8EBB, 'lo(osword_0f_handler-1): OSWORD &0F', align=Align.INLINE)
d.comment(0x8EBC, 'lo(osword_10_handler-1): OSWORD &10', align=Align.INLINE)
d.comment(0x8EBD, 'lo(osword_11_handler-1): OSWORD &11', align=Align.INLINE)
d.comment(0x8EBE, 'lo(osword_12_dispatch-1): OSWORD &12', align=Align.INLINE)
d.comment(0x8EBF, 'lo(econet_tx_rx-1): OSWORD &13', align=Align.INLINE)
d.comment(0x8EC0, 'Dispatch table: high bytes for OSWORD &0F-&13 handlers', align=Align.INLINE)
d.comment(0x8EC1, 'hi(osword_10_handler-1): OSWORD &10', align=Align.INLINE)
d.comment(0x8EC2, 'hi(osword_11_handler-1): OSWORD &11', align=Align.INLINE)
d.comment(0x8EC3, 'hi(osword_12_dispatch-1): OSWORD &12', align=Align.INLINE)
d.comment(0x8EC4, 'hi(econet_tx_rx-1): OSWORD &13', align=Align.INLINE)
d.comment(0x8152, 'Copy NMI handler code from ROM to RAM pages &04-&06')
d.comment(0x816C, 'Copy NMI workspace initialiser from ROM to &0016-&0076')


d.subroutine(0x8FF3, 'econet_tx_rx', title='Econet transmit/receive handler', description="""A=0: Initialise TX control block from ROM template at &8383
     (init_tx_ctrl_block+Y, zero entries substituted from NMI
     workspace &0DE6), transmit it, set up RX control block,
     and receive reply.
A>=1: Handle transmit result (branch to cleanup at &903E).""", on_entry={'a': '0=set up and transmit, >=1=handle TX result'})
d.comment(0x8FF3, 'A=0: set up and transmit; A>=1: handle result', align=Align.INLINE)
d.comment(0x8FF5, 'A >= 1: handle TX result', align=Align.INLINE)
d.comment(0x8FF7, 'Y=&23: start of template (descending)', align=Align.INLINE)
d.comment(0x8FF9, 'Load ROM template byte', align=Align.INLINE)
d.comment(0x8FFC, 'Non-zero = use ROM template byte as-is', align=Align.INLINE)
d.comment(0x8FFE, 'Zero = substitute from NMI workspace', align=Align.INLINE)
d.comment(0x9001, 'Store to dynamic workspace', align=Align.INLINE)
d.comment(0x9003, 'Descend through template', align=Align.INLINE)
d.comment(0x9004, 'Stop at offset &17', align=Align.INLINE)
d.comment(0x9006, 'Loop until all bytes copied', align=Align.INLINE)
d.comment(0x9008, 'Y=&18: TX block starts here', align=Align.INLINE)
d.comment(0x9009, 'Point net_tx_ptr at workspace+&18', align=Align.INLINE)
d.comment(0x900B, 'Set up RX buffer start/end pointers', align=Align.INLINE)
d.comment(0x900E, 'Y=2: port byte offset in RXCB', align=Align.INLINE)
d.comment(0x9010, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x9012, 'Mark as escapable operation', align=Align.INLINE)
d.comment(0x9014, 'Store port &90 at (&F0)+2', align=Align.INLINE)
d.comment(0x9018, 'Copy FS station addr from workspace', align=Align.INLINE)
d.comment(0x901B, 'Store to RX param block', align=Align.INLINE)
d.comment(0x901D, 'Next byte', align=Align.INLINE)
d.comment(0x901E, 'Done 3 bytes (Y=4,5,6)?', align=Align.INLINE)
d.comment(0x9020, 'No: continue copying', align=Align.INLINE)
d.comment(0x9022, 'High byte of workspace for TX ptr', align=Align.INLINE)
d.comment(0x9024, 'Store as TX pointer high byte', align=Align.INLINE)
d.comment(0x9026, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x9027, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x902A, 'Y=&20: RX end address offset', align=Align.INLINE)
d.comment(0x902C, 'Set RX end address to &FFFF (accept any length)', align=Align.INLINE)
d.comment(0x902E, 'Store end address low byte (&FF)', align=Align.INLINE)
d.comment(0x9031, 'Store end address high byte (&FF)', align=Align.INLINE)
d.comment(0x9033, 'Y=&19: port byte in workspace RXCB', align=Align.INLINE)
d.comment(0x9035, 'A=&90: FS reply port', align=Align.INLINE)
d.comment(0x9037, 'Store port to workspace RXCB', align=Align.INLINE)
d.comment(0x903A, 'A=&7F: flag byte = waiting for reply', align=Align.INLINE)
d.comment(0x903C, 'Store flag byte to workspace RXCB', align=Align.INLINE)
d.comment(0x903E, 'Jump to RX poll (BRIANX)', align=Align.INLINE)
d.comment(0x9041, 'Save processor flags', align=Align.INLINE)
d.comment(0x9042, 'Y=1: first data byte offset', align=Align.INLINE)
d.comment(0x9044, 'Load first data byte from RX buffer', align=Align.INLINE)
d.comment(0x906F, 'Test for end-of-data marker (&0D)', align=Align.INLINE)


d.subroutine(0x9083, 'osword_dispatch', title='NETVEC dispatch handler (ENTRY)', description="""Indirected from NETVEC at &0224. Saves all registers and flags,
retrieves the reason code from the stacked A, and dispatches to
one of 9 handlers (codes 0-8) via the PHA/PHA/RTS trampoline at
&9099. Reason codes >= 9 are ignored.

Dispatch targets (from NFS09):
  0:   no-op (RTS)
  1-3: PRINT -- chars in printer buffer / Ctrl-B / Ctrl-C
  4:   NWRCH -- write character to screen (net write char)
  5:   SELECT -- printer selection changed
  6:   no-op (net read char -- not implemented)
  7:   NBYTE -- remote OSBYTE call
  8:   NWORD -- remote OSWORD call""", on_entry={'a': 'reason code (0-8)'}, on_exit={'a': 'preserved', 'x': 'preserved', 'y': 'preserved'})
d.comment(0x9083, 'Save processor status', align=Align.INLINE)
d.comment(0x9084, 'Save A (reason code)', align=Align.INLINE)
d.comment(0x9085, 'Save X', align=Align.INLINE)
d.comment(0x9086, 'Push X to stack', align=Align.INLINE)
d.comment(0x9087, 'Save Y', align=Align.INLINE)
d.comment(0x9088, 'Push Y to stack', align=Align.INLINE)
d.comment(0x9089, 'Get stack pointer for indexed access', align=Align.INLINE)
d.comment(0x908A, 'Retrieve original A (reason code) from stack', align=Align.INLINE)
d.comment(0x908D, 'Reason codes 0-8 only', align=Align.INLINE)
d.comment(0x908F, 'Code >= 9: skip dispatch, restore regs', align=Align.INLINE)
d.comment(0x9091, 'X = reason code for table lookup', align=Align.INLINE)
d.comment(0x9092, 'Dispatch to handler via trampoline', align=Align.INLINE)
d.comment(0x9095, 'Restore Y', align=Align.INLINE)
d.comment(0x9096, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x9097, 'Restore X', align=Align.INLINE)
d.comment(0x9098, 'Transfer to X register', align=Align.INLINE)
d.comment(0x9099, 'Restore A', align=Align.INLINE)
d.comment(0x909A, 'Restore processor status flags', align=Align.INLINE)
d.comment(0x909B, 'Return with all registers preserved', align=Align.INLINE)
d.comment(0x909C, 'PHA/PHA/RTS trampoline: push handler addr-1, RTS jumps to it', align=Align.INLINE)
d.comment(0x909F, 'Push high byte of handler address', align=Align.INLINE)
d.comment(0x90A0, 'Load handler low byte from table', align=Align.INLINE)
d.comment(0x90A3, 'Push low byte of handler address', align=Align.INLINE)
d.comment(0x90A4, 'Load workspace byte &EF for handler', align=Align.INLINE)
d.comment(0x90A6, 'RTS dispatches to pushed handler', align=Align.INLINE)
d.comment(0x90A7, 'lo(return_1-1): fn 0 (null handler)', align=Align.INLINE)
d.comment(0x90A8, 'lo(remote_print_handler-1): fn 1', align=Align.INLINE)
d.comment(0x90A9, 'lo(remote_print_handler-1): fn 2', align=Align.INLINE)
d.comment(0x90AA, 'lo(remote_print_handler-1): fn 3', align=Align.INLINE)
d.comment(0x90AB, 'lo(net_write_char_handler-1): fn 4', align=Align.INLINE)
d.comment(0x90AC, 'lo(printer_select_handler-1): fn 5', align=Align.INLINE)
d.comment(0x90AD, 'lo(return_1-1): fn 6 (null handler)', align=Align.INLINE)
d.comment(0x90AE, 'lo(remote_cmd_dispatch-1): fn 7', align=Align.INLINE)
d.comment(0x90AF, 'lo(remote_osword_handler-1): fn 8', align=Align.INLINE)
d.comment(0x90B0, 'hi(return_1-1): fn 0 (null handler)', align=Align.INLINE)
d.comment(0x90B1, 'hi(remote_print_handler-1): fn 1', align=Align.INLINE)
d.comment(0x90B2, 'hi(remote_print_handler-1): fn 2', align=Align.INLINE)
d.comment(0x90B3, 'hi(remote_print_handler-1): fn 3', align=Align.INLINE)
d.comment(0x90B4, 'hi(net_write_char_handler-1): fn 4', align=Align.INLINE)
d.comment(0x90B5, 'hi(printer_select_handler-1): fn 5', align=Align.INLINE)
d.comment(0x90B6, 'hi(return_1-1): fn 6 (null handler)', align=Align.INLINE)
d.comment(0x90B7, 'hi(remote_cmd_dispatch-1): fn 7', align=Align.INLINE)
d.comment(0x90B8, 'hi(remote_osword_handler-1): fn 8', align=Align.INLINE)
d.comment(0x90B9, 'Get stack pointer for P register access', align=Align.INLINE)
d.comment(0x90BD, 'ASL: restore P after ROR zeroed carry', align=Align.INLINE)
d.comment(0x90C0, 'Y = character to write', align=Align.INLINE)
d.comment(0x90C3, 'Store char at workspace offset &DA', align=Align.INLINE)
d.comment(0x90C5, 'A=0: command type for net write char', align=Align.INLINE)


d.subroutine(0x907F, 'enable_irq_and_tx', title='Enable interrupts and transmit via tx_poll_ff', description="""CLI to enable interrupts, then JMP tx_poll_ff. A short
tail-call wrapper used after building the TX control block.""")


d.subroutine(0x90B9, 'net_write_char_handler', title='NETVEC fn 4: handle net write character (NWRCH)', description="""Zeros the carry flag in the stacked processor status to
signal success, stores the character from Y into workspace
offset &DA, loads A=0 as the command type, and falls through
to setup_tx_and_send.""", on_entry={'y': 'character to write'})


d.subroutine(0x9046, 'net_write_char', title='FS response data relay (DOFS)', description="""Entered from the econet_tx_rx response handler at &903E after
loading the first data byte from the RX buffer. Saves the
command byte and station address from the received packet into
(net_rx_ptr)+&71/&72, then iterates through remaining data
bytes. Each byte is stored at (net_rx_ptr)+&7D, the control
block is set up via ctrl_block_setup_alt, and the packet is
transmitted. Loops until a &0D terminator or &00 null is found.
The branch at &9053 (BNE dofs2) handles the first-packet case
where the data length field at (net_rx_ptr)+&7B is adjusted.""")
d.comment(0x9046, 'X = first data byte (command code)', align=Align.INLINE)
d.comment(0x9047, 'Advance to next data byte', align=Align.INLINE)
d.comment(0x9048, 'Load station address high byte', align=Align.INLINE)
d.comment(0x904A, 'Advance past station addr', align=Align.INLINE)
d.comment(0x904B, 'Save Y as data index', align=Align.INLINE)
d.comment(0x904D, 'Store station addr hi at (net_rx_ptr)+&72', align=Align.INLINE)
d.comment(0x904F, 'Store to workspace', align=Align.INLINE)
d.comment(0x9052, 'A = command code (from X)', align=Align.INLINE)
d.comment(0x9053, 'Store station addr lo at (net_rx_ptr)+&71', align=Align.INLINE)
d.comment(0x9055, 'Restore flags from earlier PHP', align=Align.INLINE)
d.comment(0x9056, 'First call: adjust data length', align=Align.INLINE)
d.comment(0x9058, 'Reload data index', align=Align.INLINE)
d.comment(0x905A, 'Advance data index for next iteration', align=Align.INLINE)
d.comment(0x905C, 'Load next data byte', align=Align.INLINE)
d.comment(0x905E, 'Zero byte: end of data, return', align=Align.INLINE)
d.comment(0x9060, 'Y=&7D: store byte for TX at offset &7D', align=Align.INLINE)
d.comment(0x9062, 'Store data byte at (net_rx_ptr)+&7D for TX', align=Align.INLINE)
d.comment(0x9064, 'Save data byte for &0D check after TX', align=Align.INLINE)
d.comment(0x9065, 'Set up TX control block', align=Align.INLINE)
d.comment(0x9068, 'Enable IRQs and transmit', align=Align.INLINE)
d.comment(0x906B, 'Short delay loop between TX packets', align=Align.INLINE)
d.comment(0x906C, 'Spin until X reaches 0', align=Align.INLINE)
d.comment(0x906E, 'Restore data byte for terminator check', align=Align.INLINE)
d.comment(0x9071, 'Not &0D: continue with next byte', align=Align.INLINE)
d.comment(0x9073, 'Return (data complete)', align=Align.INLINE)
d.comment(0x9074, 'First-packet: set up control block', align=Align.INLINE)
d.comment(0x9077, 'Y=&7B: data length offset', align=Align.INLINE)
d.comment(0x9079, 'Load current data length', align=Align.INLINE)
d.comment(0x907D, 'Store adjusted length', align=Align.INLINE)
d.comment(0x907F, 'Enable interrupts', align=Align.INLINE)
d.comment(0x9080, 'Transmit via tx_poll_ff', align=Align.INLINE)
d.comment(0x907B, 'Adjust data length by 3 for header bytes', align=Align.INLINE)
d.comment(0x90BA, 'ROR/ASL on stacked P: zeros carry to signal success', align=Align.INLINE)
d.comment(0x90C1, 'Store character at workspace offset &DA', align=Align.INLINE)


d.subroutine(0x90C7, 'setup_tx_and_send', title='Set up TX control block and send', description="""Stores A at workspace offset &D9 (command type), then sets byte
&0C to &80 (TX active flag). Saves the current net_tx_ptr,
temporarily redirects it to (nfs_workspace)+&0C so tx_poll_ff
transmits from the workspace TX control block. After transmission
completes, writes &3F (TX deleted) at (net_tx_ptr)+&00 to mark
the control block as free, then restores net_tx_ptr to its
original value.""", on_entry={'a': 'command type byte'})
d.comment(0x90C7, 'Y=&D9: command type offset', align=Align.INLINE)
d.comment(0x90C9, 'Store command type at ws+&D9', align=Align.INLINE)
d.comment(0x90CB, 'Mark TX control block as active (&80)', align=Align.INLINE)
d.comment(0x90CD, 'Y=&0C: TXCB start offset', align=Align.INLINE)
d.comment(0x90CF, 'Set TX active flag at ws+&0C', align=Align.INLINE)
d.comment(0x90D1, 'Save net_tx_ptr; redirect to workspace TXCB', align=Align.INLINE)
d.comment(0x90D3, 'Save net_tx_ptr low', align=Align.INLINE)
d.comment(0x90D4, 'Load net_tx_ptr high', align=Align.INLINE)
d.comment(0x90D6, 'Save net_tx_ptr high', align=Align.INLINE)
d.comment(0x90D7, 'Redirect net_tx_ptr low to workspace', align=Align.INLINE)
d.comment(0x90D9, 'Load workspace page high byte', align=Align.INLINE)
d.comment(0x90DB, 'Complete ptr redirect', align=Align.INLINE)
d.comment(0x90DD, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x90E0, 'Mark TXCB as deleted (&3F) after transmit', align=Align.INLINE)
d.comment(0x90E2, 'Write &3F to TXCB byte 0', align=Align.INLINE)
d.comment(0x90E4, 'Restore net_tx_ptr high', align=Align.INLINE)
d.comment(0x90E5, 'Write back', align=Align.INLINE)
d.comment(0x90E7, 'Restore net_tx_ptr low', align=Align.INLINE)
d.comment(0x90E8, 'Write back', align=Align.INLINE)
d.comment(0x90EA, 'Return', align=Align.INLINE)


d.subroutine(0x9182, 'ctrl_block_setup_alt', title='Alternate entry into control block setup', description="""Sets X=&0D, Y=&7C. Tests bit 6 of &83B3 to choose target:
  V=0 (bit 6 clear): stores to (nfs_workspace)
  V=1 (bit 6 set):   stores to (net_rx_ptr)""")
d.comment(0x9182, 'X=&0D: template offset for alt entry', align=Align.INLINE)
d.comment(0x9184, 'Y=&7C: target workspace offset for alt entry', align=Align.INLINE)
d.comment(0x9186, 'BIT test: V flag = bit 6 of &83B3', align=Align.INLINE)
d.comment(0x9189, 'V=1: store to (net_rx_ptr) instead', align=Align.INLINE)


d.subroutine(0x918B, 'ctrl_block_setup', title='Control block setup — main entry', description="""Sets X=&1A, Y=&17, clears V (stores to nfs_workspace).
Reads the template table at &91B4 indexed by X, storing each
value into the target workspace at offset Y. Both X and Y
are decremented on each iteration.

Template sentinel values:
  &FE = stop (end of template for this entry path)
  &FD = skip (leave existing value unchanged)
  &FC = use page high byte of target pointer""")
d.comment(0x918B, 'Y=&17: workspace target offset (main entry)', align=Align.INLINE)
d.comment(0x918D, 'X=&1A: template table index (main entry)', align=Align.INLINE)
d.comment(0x918F, 'V=0: target is (nfs_workspace)', align=Align.INLINE)
d.comment(0x9190, 'Load template byte from ctrl_block_template[X]', align=Align.INLINE)
d.comment(0x9193, '&FE = stop sentinel', align=Align.INLINE)
d.comment(0x9195, 'End of template: jump to exit', align=Align.INLINE)
d.comment(0x9197, '&FD = skip sentinel', align=Align.INLINE)
d.comment(0x9199, "Skip: don't store, just decrement Y", align=Align.INLINE)
d.comment(0x919B, '&FC = page byte sentinel', align=Align.INLINE)
d.comment(0x919D, 'Not sentinel: store template value directly', align=Align.INLINE)


d.subroutine(0x91B7, 'ctrl_block_template', title='Control block initialisation template', description="""Read by the loop at &918D, indexed by X from a starting value
down to 0. Values are stored into either (nfs_workspace) or
(net_rx_ptr) at offset Y, depending on the V flag.

Two entry paths read different slices of this table:
  ctrl_block_setup:   X=&1A (26) down, Y=&17 (23) down, V=0
  ctrl_block_setup_alt: X=&0D (13) down, Y=&7C (124) down, V from BIT &83B3

Sentinel values:
  &FE = stop processing
  &FD = skip this offset (decrement Y but don't store)
  &FC = substitute the page byte (net_rx_ptr_hi or nfs_workspace_hi)""")
d.comment(0x919F, 'V=1: use (net_rx_ptr) page', align=Align.INLINE)
d.comment(0x91A1, 'V=1: skip to net_rx_ptr page', align=Align.INLINE)
d.comment(0x91A3, 'V=0: use (nfs_workspace) page', align=Align.INLINE)
d.comment(0x91A5, 'PAGE byte → Y=&02 / Y=&74', align=Align.INLINE)
d.comment(0x91A7, '→ Y=&04 / Y=&76', align=Align.INLINE)
d.comment(0x91A9, 'PAGE byte → Y=&06 / Y=&78', align=Align.INLINE)
d.comment(0x91AB, '→ Y=&08 / Y=&7A', align=Align.INLINE)
d.comment(0x91AD, 'Alt-path only → Y=&70', align=Align.INLINE)
d.comment(0x91AF, '→ Y=&0C (main only)', align=Align.INLINE)
d.comment(0x91B0, '→ Y=&0D (main only)', align=Align.INLINE)
d.comment(0x91B1, 'Loop until all template bytes done', align=Align.INLINE)
d.comment(0x91B3, '→ Y=&10 (main only)', align=Align.INLINE)
d.comment(0x91B4, 'Store final offset as net_tx_ptr', align=Align.INLINE)
d.comment(0x91B6, '→ Y=&07 / Y=&79', align=Align.INLINE)
d.comment(0x91B7, 'Alt-path only → Y=&6F', align=Align.INLINE)


d.subroutine(0x8F04, 'osword_12_dispatch', title='OSWORD &12 handler: dispatch sub-functions 0-9', description="""Range-checks the sub-function code from the param block and
dispatches:
  0: read FS server station/network (from &0E00/&0E01)
  1: set  FS server station/network
  2: read printer server station/network (from dynamic ws)
  3: set  printer server station/network
  4: read JSR protection mask (LSTAT at &0D63)
  5: set  JSR protection mask
  6: read context handles (URD/CSD/LIB)
  7: set  context handles
  8: read cached local station number (from (net_rx_ptr)+&14,
     populated at init by reading the &FE18 station-ID latch)
  9: read JSR argument buffer size
Sub-functions 0-3 select the appropriate workspace page
(static &0D or dynamic) and offset, then fall through to the
bidirectional param block copy loop. Sub-functions >= 6 are
re-dispatched via rsl1; values >= 10 return the last FS error.
Note: there is no sub-function that *sets* the local station
number -- on the Model B that is hardwired via the 8 station
ID links read from &FE18.""")


d.subroutine(0x8F1F, 'copy_param_workspace', title='Bidirectional copy loop between param block and workspace', description="""If C=1, copies from OSWORD param block (&F0),Y to workspace
(&AB),Y. In either case, loads from workspace and stores to
param block. Loops for X+1 bytes. Used by OSWORD &0F, &10,
&11, and &12 handlers.""", on_entry={'c': '1=copy param to workspace first, 0=workspace to param only', 'x': 'byte count minus 1', 'y': 'starting offset'}, on_exit={'a': 'last byte copied', 'x': '&FF', 'y': 'start + count + 1'})


d.subroutine(0x8F27, 'copy_param_block', title='Bidirectional block copy between OSWORD param block and workspace.', description="""C=1: copy X+1 bytes from (&F0),Y to (&AB),Y (param to workspace)
C=0: copy X+1 bytes from (&AB),Y to (&F0),Y (workspace to param)""", on_entry={'c': '1=param to workspace, 0=workspace to param', 'x': 'byte count minus 1', 'y': 'starting offset'}, on_exit={'a': 'last byte copied', 'x': '&FF', 'y': 'start + count + 1'})
d.comment(0x8F1F, 'C=0: skip param-to-workspace copy', align=Align.INLINE)
d.comment(0x8F27, 'Store to param block (no-op if C=1)', align=Align.INLINE)
d.comment(0x8F29, 'Advance to next byte', align=Align.INLINE)
d.comment(0x8F2A, 'Decrement remaining count', align=Align.INLINE)
d.comment(0x8F2B, 'Loop while bytes remain', align=Align.INLINE)
d.comment(0x8F2D, 'Return', align=Align.INLINE)
d.comment(0x8F2E, 'LSR A: test bit 0 of sub-function', align=Align.INLINE)
d.comment(0x8F2F, 'Y=1: offset for protection byte', align=Align.INLINE)
d.comment(0x8F30, 'Load protection byte from param block', align=Align.INLINE)
d.comment(0x8F32, 'C=1 (odd sub): set protection', align=Align.INLINE)
d.comment(0x8F34, 'C=0 (even sub): read current status', align=Align.INLINE)
d.comment(0x8F37, 'Return current value to param block', align=Align.INLINE)
d.comment(0x8F39, 'Update protection status', align=Align.INLINE)
d.comment(0x8F3C, 'Also save as JSR mask backup', align=Align.INLINE)
d.comment(0x8F3F, 'Return', align=Align.INLINE)
d.comment(0x8F40, 'Y=&14: RX buf offset of cached station ID', align=Align.INLINE)
d.comment(0x8F42, 'Read cached local station number', align=Align.INLINE)
d.comment(0x8F44, 'Y=1: param block byte 1', align=Align.INLINE)
d.comment(0x8F46, "Return handle to caller's param block", align=Align.INLINE)
d.comment(0x8F48, 'Return', align=Align.INLINE)
d.comment(0x8F49, 'Sub-function 8: read local station number', align=Align.INLINE)
d.comment(0x8F4B, 'Match: read cached station ID from RX buffer', align=Align.INLINE)
d.comment(0x8F4D, 'Sub-function 9: read args size', align=Align.INLINE)
d.comment(0x8F4F, 'Match: read ARGS buffer info', align=Align.INLINE)
d.comment(0x8F51, 'Sub >= 10 (bit 7 clear): read error', align=Align.INLINE)
d.comment(0x8F53, 'Y=3: start from handle 3 (descending)', align=Align.INLINE)
d.comment(0x8F55, 'LSR: test read/write bit', align=Align.INLINE)
d.comment(0x8F56, 'C=0: read handles from workspace', align=Align.INLINE)
d.comment(0x8F58, 'Init loop counter at Y=3', align=Align.INLINE)
d.comment(0x8F5A, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8F5C, "Read handle from caller's param block", align=Align.INLINE)
d.comment(0x8F5E, 'Convert handle number to bitmask', align=Align.INLINE)
d.comment(0x8F61, 'TYA: get bitmask result', align=Align.INLINE)
d.comment(0x8F62, 'Reload loop counter', align=Align.INLINE)
d.comment(0x8F64, 'Store bitmask to FS server table', align=Align.INLINE)
d.comment(0x8F67, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8F69, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8F6B, 'Return', align=Align.INLINE)
d.comment(0x8F6C, 'Y=1 (post-INY): param block byte 1', align=Align.INLINE)
d.comment(0x8F6D, 'Read last FS error code', align=Align.INLINE)
d.comment(0x8F70, "Return error to caller's param block", align=Align.INLINE)
d.comment(0x8F72, 'Return', align=Align.INLINE)
d.comment(0x8F7B, 'Next handle (descending)', align=Align.INLINE)
d.comment(0x8F7C, 'Loop for handles 3,2,1', align=Align.INLINE)
d.comment(0x8F7E, 'Return', align=Align.INLINE)

d.label(0x8F2D, 'return_copy_param')


d.subroutine(0x8EC5, 'osword_0f_handler', title='OSWORD &0F handler: initiate transmit (CALLTX)', description="""Checks the TX semaphore (TXCLR at &0D62) via ASL -- if carry is
clear, a TX is already in progress and the call returns an error,
preventing user code from corrupting a system transmit. Otherwise
copies 16 bytes from the caller's OSWORD parameter block into the
user TX control block (UTXCB) in static workspace. The TXCB
pointer is copied to LTXCBP only after the semaphore is claimed,
ensuring the low-level transmit code (BRIANX) sees a consistent
pointer -- if copied before claiming, another transmitter could
modify TXCBP between the copy and the claim.""", on_entry={'x': 'parameter block address low byte', 'y': 'parameter block address high byte'}, on_exit={'a': 'corrupted', 'x': 'corrupted', 'y': '&FF'})
d.comment(0x8EC5, 'ASL TXCLR: C=1 means TX free to claim', align=Align.INLINE)
d.comment(0x8EC8, 'Save Y (param block high) for later', align=Align.INLINE)
d.comment(0x8EC9, 'C=0: TX busy, return error status', align=Align.INLINE)
d.comment(0x8ECB, 'User TX CB in workspace page (high byte)', align=Align.INLINE)
d.comment(0x8ECD, 'Set param block high byte', align=Align.INLINE)
d.comment(0x8ECF, 'Set LTXCBP high byte for low-level TX', align=Align.INLINE)
d.comment(0x8ED1, '&6F: offset into workspace for user TXCB', align=Align.INLINE)
d.comment(0x8ED3, 'Set param block low byte', align=Align.INLINE)
d.comment(0x8ED5, 'Set LTXCBP low byte for low-level TX', align=Align.INLINE)
d.comment(0x8ED7, 'X=15: copy 16 bytes (OSWORD param block)', align=Align.INLINE)
d.comment(0x8ED9, 'Copy param block to user TX control block', align=Align.INLINE)
d.comment(0x8EDC, 'Start user transmit via BRIANX', align=Align.INLINE)


d.subroutine(0x8EDF, 'osword_11_handler', title='OSWORD &11 handler: read JSR arguments (READRA)', description="""Copies the JSR (remote procedure call) argument buffer from the
static workspace page back to the caller's OSWORD parameter block.
Reads the buffer size from workspace offset JSRSIZ, then copies
that many bytes. After the copy, clears the old LSTAT byte via
CLRJSR to reset the protection status. Also provides READRB as
a sub-entry (&8EE7) to return just the buffer size and args size
without copying the data.""")
d.comment(0x8EDF, 'Set source high byte from workspace page', align=Align.INLINE)
d.comment(0x8EE1, 'Store as copy source high byte in &AC', align=Align.INLINE)
d.comment(0x8EE3, 'JSRSIZ at workspace offset &7F', align=Align.INLINE)
d.comment(0x8EE5, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8EE7, 'Y=&80: start of JSR argument data', align=Align.INLINE)
d.comment(0x8EE8, 'Store &80 as copy source low byte', align=Align.INLINE)
d.comment(0x8EEA, 'X = buffer size (loop counter)', align=Align.INLINE)
d.comment(0x8EEB, 'X = size-1 (0-based count for copy)', align=Align.INLINE)
d.comment(0x8EEC, 'Y=0: start of destination param block', align=Align.INLINE)
d.comment(0x8EEE, 'Copy X+1 bytes from workspace to param', align=Align.INLINE)
d.comment(0x8EF1, 'Clear JSR protection status (CLRJSR)', align=Align.INLINE)
d.comment(0x8EF4, 'Y=&7F: JSRSIZ offset (READRB entry)', align=Align.INLINE)
d.comment(0x8EF6, 'Load buffer size from workspace', align=Align.INLINE)
d.comment(0x8EF8, 'Y=1: param block offset for size byte', align=Align.INLINE)
d.comment(0x8EFA, 'Store buffer size to (&F0)+1', align=Align.INLINE)
d.comment(0x8EFC, 'Y=2: param block offset for args size', align=Align.INLINE)
d.comment(0x8EFD, 'A=&80: argument data starts at offset &80', align=Align.INLINE)
d.comment(0x8EFF, 'Store args start offset to (&F0)+2', align=Align.INLINE)
d.comment(0x8F01, 'Return', align=Align.INLINE)
d.comment(0x8F02, 'OSWORD &12 workspace offset table', align=Align.INLINE)
d.comment(0x8F04, 'OSWORD &12: range check sub-function', align=Align.INLINE)
d.comment(0x8F06, 'Sub-function >= 6: not supported', align=Align.INLINE)
d.comment(0x8F08, 'Check for sub-functions 4-5', align=Align.INLINE)
d.comment(0x8F0A, 'Sub-function 4 or 5: read/set protection', align=Align.INLINE)
d.comment(0x8F0C, 'LSR: 0->0, 1->0, 2->1, 3->1', align=Align.INLINE)
d.comment(0x8F0D, 'X=&0D: default to static workspace page', align=Align.INLINE)
d.comment(0x8F0F, 'Transfer LSR result to Y for indexing', align=Align.INLINE)
d.comment(0x8F10, 'Y=0 (sub 0-1): use page &0D', align=Align.INLINE)
d.comment(0x8F12, 'Y=1 (sub 2-3): use dynamic workspace', align=Align.INLINE)
d.comment(0x8F14, 'Store workspace page in &AC (hi byte)', align=Align.INLINE)
d.comment(0x8F16, 'Load offset: &FF (sub 0-1) or &01 (sub 2-3)', align=Align.INLINE)
d.comment(0x8F19, 'Store offset in &AB (lo byte)', align=Align.INLINE)
d.comment(0x8F1B, 'X=1: copy 2 bytes', align=Align.INLINE)
d.comment(0x8F1D, 'Y=1: start at param block offset 1', align=Align.INLINE)
d.comment(0x8F21, 'C=1: copy from param to workspace', align=Align.INLINE)
d.comment(0x8F23, 'Store param byte to workspace', align=Align.INLINE)


d.subroutine(0x8E90, 'osword_12_handler', title='OSWORD range check, dispatch, and register restore', description="""Reached by fall-through from svc_8_osword with A = OSWORD
number minus &0F. Rejects indices >= 5 (only OSWORDs &0F-&13
are handled). Dispatches to the appropriate handler via
fs_osword_dispatch, then on return copies 3 bytes from
(net_rx_ptr)+0..2 back to &AA-&AC (restoring the param block
pointer that was saved by fs_osword_dispatch before dispatch).

The actual OSWORD &12 sub-function dispatch (FS/printer server
station/network, protection mask, context handles, local
station number read-back etc.) lives in osword_12_dispatch.""")
d.comment(0x8E90, 'Only OSWORDs &0F-&13 (index 0-4)', align=Align.INLINE)
d.comment(0x8E92, 'Index >= 5: not ours, return', align=Align.INLINE)
d.comment(0x8E94, 'Dispatch via PHA/PHA/RTS table', align=Align.INLINE)
d.comment(0x8E97, 'Y=2: restore 3 bytes (&AA-&AC)', align=Align.INLINE)
d.comment(0x8E99, 'Load saved param block byte', align=Align.INLINE)
d.comment(0x8E9B, 'Restore to &AA-&AC', align=Align.INLINE)
d.comment(0x8E9E, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x8E9F, 'Loop for all 3 bytes', align=Align.INLINE)
d.comment(0x8EA1, 'Return to service handler', align=Align.INLINE)


d.subroutine(0x8F7F, 'osword_10_handler', title='OSWORD &10 handler: open/read RX control block (OPENRX)', description="""If the first byte of the caller's parameter block is zero, scans
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
d.comment(0x8F7F, 'Workspace page high byte', align=Align.INLINE)
d.comment(0x8F81, 'Set up pointer high byte in &AC', align=Align.INLINE)
d.comment(0x8F83, 'Save param block high byte in &AB', align=Align.INLINE)
d.comment(0x8F85, 'Disable user RX during CB operation', align=Align.INLINE)
d.comment(0x8F88, 'Read first byte of param block', align=Align.INLINE)
d.comment(0x8F8A, 'Save: 0=open new, non-zero=read RXCB', align=Align.INLINE)
d.comment(0x8F8C, 'Non-zero: read specified RXCB', align=Align.INLINE)
d.comment(0x8F8E, 'Start scan from RXCB #3 (0-2 reserved)', align=Align.INLINE)
d.comment(0x8F90, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8F93, 'Invalid RXCB: return zero', align=Align.INLINE)
d.comment(0x8F95, 'LSR twice: byte offset / 4', align=Align.INLINE)
d.comment(0x8F96, 'Yields RXCB number from offset', align=Align.INLINE)
d.comment(0x8F97, 'X = RXCB number for iteration', align=Align.INLINE)
d.comment(0x8F98, 'Read flag byte from RXCB workspace', align=Align.INLINE)
d.comment(0x8F9A, 'Zero = end of CB list', align=Align.INLINE)
d.comment(0x8F9C, '&3F = deleted slot, free for reuse', align=Align.INLINE)
d.comment(0x8F9E, 'Found free slot', align=Align.INLINE)
d.comment(0x8FA0, 'Try next RXCB', align=Align.INLINE)
d.comment(0x8FA1, 'A = next RXCB number', align=Align.INLINE)
d.comment(0x8FA2, 'Continue scan (always branches)', align=Align.INLINE)
d.comment(0x8FA4, 'A = free RXCB number', align=Align.INLINE)
d.comment(0x8FA5, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x8FA7, "Return RXCB number to caller's byte 0", align=Align.INLINE)
d.comment(0x8FA9, 'Convert RXCB number to workspace offset', align=Align.INLINE)
d.comment(0x8FAC, 'Invalid: write zero to param block', align=Align.INLINE)
d.comment(0x8FAE, 'Y = offset-1: points to flag byte', align=Align.INLINE)
d.comment(0x8FAF, 'Set &AB = workspace ptr low byte', align=Align.INLINE)
d.comment(0x8FB1, '&C0: test mask for flag byte', align=Align.INLINE)
d.comment(0x8FB3, 'Y=1: flag byte offset in RXCB', align=Align.INLINE)
d.comment(0x8FB7, 'Compare Y(1) with saved byte (open/read)', align=Align.INLINE)
d.comment(0x8FB9, 'ADC flag: test if slot is in use', align=Align.INLINE)
d.comment(0x8FBD, 'Negative: slot has received data', align=Align.INLINE)
d.comment(0x8FBF, 'C=0: workspace-to-param direction', align=Align.INLINE)
d.comment(0x8FC0, 'Copy RXCB data to param block', align=Align.INLINE)
d.comment(0x8FC3, 'Done: skip deletion on error', align=Align.INLINE)
d.comment(0x8FC5, 'Mark CB as consumed (consume-once)', align=Align.INLINE)
d.comment(0x8FC7, 'Y=1: flag byte offset', align=Align.INLINE)
d.comment(0x8FC9, 'Write &3F to mark slot deleted', align=Align.INLINE)
d.comment(0x8FCB, 'Branch to exit (always taken)', align=Align.INLINE)
d.comment(0x8FCD, 'Advance through multi-byte field', align=Align.INLINE)
d.comment(0x8FCF, 'Loop until all bytes processed', align=Align.INLINE)
d.comment(0x8FD1, 'Y=-1 → Y=0 after STA below', align=Align.INLINE)
d.comment(0x8FD2, 'Return zero (no free RXCB found)', align=Align.INLINE)
d.comment(0x8FD4, 'Re-enable user RX', align=Align.INLINE)
d.comment(0x8FD7, 'Return', align=Align.INLINE)


d.subroutine(0x849D, 'lang_1_remote_boot', title='Remote boot/execute handler', description="""Checks byte 4 of the RX control block (remote status flag).
If zero (not currently remoted), falls through to remot1 to
set up a new remote session. If non-zero (already remoted),
jumps to clear_jsr_protection and returns.""")
d.comment(0x849D, 'Y=4: remote status flag offset', align=Align.INLINE)
d.comment(0x849F, 'Read remote status from RX CB', align=Align.INLINE)
d.comment(0x84A1, 'Zero: not remoted, set up session', align=Align.INLINE)
d.comment(0x84A3, 'Already remoted: clear and return', align=Align.INLINE)
d.comment(0x84A6, 'Set remote status: bits 0+3 (ORA #9)', align=Align.INLINE)
d.comment(0x84A8, 'Store updated remote status', align=Align.INLINE)
d.comment(0x84AA, 'X=&80: RX data area offset', align=Align.INLINE)
d.comment(0x84AC, 'Y=&80: read source station low', align=Align.INLINE)
d.comment(0x84AE, 'Read source station lo from RX data at &80', align=Align.INLINE)
d.comment(0x84B0, 'Save source station low byte', align=Align.INLINE)
d.comment(0x84B1, 'Y=&81', align=Align.INLINE)
d.comment(0x84B2, 'Read source station hi from RX data at &81', align=Align.INLINE)
d.comment(0x84B4, 'Save controlling station to workspace &0E/&0F', align=Align.INLINE)
d.comment(0x84B6, 'Store station high to ws+&0F', align=Align.INLINE)
d.comment(0x84B8, 'Y=&0E', align=Align.INLINE)
d.comment(0x84B9, 'Restore source station low', align=Align.INLINE)
d.comment(0x84BA, 'Store station low to ws+&0E', align=Align.INLINE)
d.comment(0x84BC, 'Clear OSBYTE &CE/&CF flags', align=Align.INLINE)
d.comment(0x84BF, 'Set up TX control block', align=Align.INLINE)
d.comment(0x84C2, 'X=1: disable keyboard', align=Align.INLINE)
d.comment(0x84C4, 'Y=0 for OSBYTE', align=Align.INLINE)
d.comment(0x84C6, 'Disable keyboard for remote session', align=Align.INLINE)


d.subroutine(0x84CB, 'lang_3_execute_at_0100', title='Execute code at &0100', description="""Clears JSR protection, zeroes &0100-&0102 (creating a BRK
instruction at &0100 as a safe default), then JMP &0100 to
execute code received over the network. If no code was loaded,
the BRK triggers an error handler.""")
d.comment(0x84CB, 'Allow JSR to page 1 (stack page)', align=Align.INLINE)
d.comment(0x84CE, 'Zero bytes &0100-&0102', align=Align.INLINE)
d.comment(0x84D2, 'BRK at &0100 as safe default', align=Align.INLINE)
d.comment(0x84D8, 'Execute downloaded code', align=Align.INLINE)


d.subroutine(0x84DB, 'lang_4_remote_validated', title='Remote operation with source validation', description="""Validates that the source station in the received packet matches
the controlling station stored in the NFS workspace. If byte 4 of
the RX control block is zero (not currently remoted), allows the
new remote session via remot1. If non-zero, compares the source
station at RX offset &80 against workspace offset &0E -- rejects
mismatched stations via clear_jsr_protection, accepts matching
stations by falling through to lang_0_insert_remote_key.""")
d.comment(0x84DB, 'Y=4: RX control block byte 4 (remote status)', align=Align.INLINE)
d.comment(0x84DD, 'Read remote status flag', align=Align.INLINE)
d.comment(0x84DF, 'Zero = not remoted; allow new session', align=Align.INLINE)
d.comment(0x84E1, 'Read source station from RX data at &80', align=Align.INLINE)
d.comment(0x84E3, 'A = source station number', align=Align.INLINE)
d.comment(0x84E5, 'Compare against controlling station at &0E', align=Align.INLINE)
d.comment(0x84E7, 'Check if source matches controller', align=Align.INLINE)
d.comment(0x84E9, 'Reject: source != controlling station', align=Align.INLINE)


d.subroutine(0x84EB, 'lang_0_insert_remote_key', title='Insert remote keypress', description="""Reads a character from RX block offset &82 and inserts it into
keyboard input buffer 0 via OSBYTE &99.""")
d.comment(0x84EB, 'Read keypress from RX data at &82', align=Align.INLINE)
d.comment(0x84ED, 'Load character byte', align=Align.INLINE)
d.comment(0x84EF, 'Y = character to insert', align=Align.INLINE)
d.comment(0x84F0, 'X = buffer 0 (keyboard input)', align=Align.INLINE)
d.comment(0x84F2, 'Release JSR protection before inserting key', align=Align.INLINE)
d.comment(0x84F5, 'OSBYTE &99: insert char into input buffer', align=Align.INLINE)
d.comment(0x84F7, 'Tail call: insert character Y into buffer X', align=Align.INLINE)


d.subroutine(0x8FD8, 'setup_rx_buffer_ptrs', title='Set up RX buffer pointers in NFS workspace', description="""Calculates the start address of the RX data area (&F0+1) and stores
it at workspace offset &1C. Also reads the data length from (&F0)+1
and adds it to &F0 to compute the end address at offset &20.""", on_entry={'c': 'clear for ADC'})
d.comment(0x8FD8, 'Y=&1C: workspace offset for RX data start', align=Align.INLINE)
d.comment(0x8FDA, 'A = base address low byte', align=Align.INLINE)
d.comment(0x8FDC, 'A = base + 1 (skip length byte)', align=Align.INLINE)
d.comment(0x8FE1, 'Read data length from (&F0)+1', align=Align.INLINE)
d.comment(0x8FE3, 'A = data length byte', align=Align.INLINE)
d.comment(0x8FE5, 'Workspace offset &20 = RX data end', align=Align.INLINE)
d.comment(0x8FE7, 'A = base + length = end address low', align=Align.INLINE)
d.comment(0x8FE9, 'Store low byte of 16-bit address', align=Align.INLINE)
d.comment(0x8FEB, 'Advance to high byte offset', align=Align.INLINE)
d.comment(0x8FEC, 'A = high byte of base address', align=Align.INLINE)
d.comment(0x8FEE, 'Add carry for 16-bit addition', align=Align.INLINE)
d.comment(0x8FF0, 'Store high byte', align=Align.INLINE)
d.comment(0x8FF2, 'Return', align=Align.INLINE)


d.subroutine(0x90EB, 'remote_cmd_dispatch', title='Fn 7: remote OSBYTE handler (NBYTE)', description="""Full RPC mechanism for OSBYTE calls across the network. When a
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
d.comment(0x90EB, 'Load original Y (OSBYTE secondary param)', align=Align.INLINE)
d.comment(0x90ED, 'OSBYTE &81 (INKEY): always forward to terminal', align=Align.INLINE)
d.comment(0x90F1, 'Y=1: search NCTBPL table (execute on both)', align=Align.INLINE)
d.comment(0x90FA, 'Y=-1: search NCTBMI table (terminal only)', align=Align.INLINE)
d.comment(0x9103, 'Y=0: OSBYTE not recognised, ignore', align=Align.INLINE)
d.comment(0x9104, 'X=2 bytes to copy (default for RBYTE)', align=Align.INLINE)
d.comment(0x9109, 'Y>0 (NCTBPL): send only, no result expected', align=Align.INLINE)
d.comment(0x910C, 'Y<0 (NCTBMI): X=3 bytes (result + P flags)', align=Align.INLINE)
d.comment(0x910F, 'Copy OSBYTE args from stack frame to workspace', align=Align.INLINE)
d.comment(0x9120, 'Set up RX control block to wait for reply', align=Align.INLINE)
d.comment(0x9126, 'Poll for TX completion (wait for bit 7 set)', align=Align.INLINE)
d.comment(0x912F, 'Force V=1 (claimed) and I=1 (no IRQ) in saved P', align=Align.INLINE)
d.comment(0x9131, 'ALWAYS branch (ORA #&44 never zero)', align=Align.INLINE)
d.comment(0x9137, 'Write result bytes to stacked registers', align=Align.INLINE)
d.comment(0x90EF, 'Forward &81 to terminal for keyboard read', align=Align.INLINE)
d.comment(0x90F3, 'X=9: 10-entry NCTBPL table size', align=Align.INLINE)
d.comment(0x90F5, 'Search for OSBYTE code in NCTBPL table', align=Align.INLINE)
d.comment(0x90F8, 'Match found: dispatch with Y=1 (both)', align=Align.INLINE)
d.comment(0x90FB, 'Second DEY: Y=&FF (from 1 via 0)', align=Align.INLINE)
d.comment(0x90FC, 'X=&0E: 15-entry NCTBMI table size', align=Align.INLINE)
d.comment(0x90FE, 'Search for OSBYTE code in NCTBMI table', align=Align.INLINE)
d.comment(0x9101, 'Match found: dispatch with Y=&FF (terminal)', align=Align.INLINE)
d.comment(0x9106, 'A=Y: check table match result', align=Align.INLINE)
d.comment(0x9107, 'Y=0: not recognised, return unhandled', align=Align.INLINE)
d.comment(0x910A, 'Y>0 (NCTBPL): no result expected, skip RX', align=Align.INLINE)
d.comment(0x910D, 'Y=&DC: top of 3-byte stack frame region', align=Align.INLINE)
d.comment(0x9112, 'Store to NFS workspace for transmission', align=Align.INLINE)
d.comment(0x9114, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9115, 'Copied all 3 bytes? (&DC, &DB, &DA)', align=Align.INLINE)
d.comment(0x9117, 'Loop for remaining bytes', align=Align.INLINE)
d.comment(0x9119, 'A = byte count for setup_tx_and_send', align=Align.INLINE)
d.comment(0x911A, 'Build TXCB and transmit to terminal', align=Align.INLINE)
d.comment(0x911D, 'Restore N flag from table match type', align=Align.INLINE)
d.comment(0x911E, 'Y was positive (NCTBPL): done, no result', align=Align.INLINE)
d.comment(0x9122, 'Y=&0C: RX control block offset in workspace', align=Align.INLINE)
d.comment(0x9124, 'Write &7F (waiting) to RXCB flag byte', align=Align.INLINE)
d.comment(0x9128, 'Bit7 clear: still waiting, poll again', align=Align.INLINE)
d.comment(0x912A, 'X = stack pointer for register restoration', align=Align.INLINE)
d.comment(0x912B, 'Y=&DD: saved P byte offset in workspace', align=Align.INLINE)
d.comment(0x912D, 'Load remote processor status from reply', align=Align.INLINE)
d.comment(0x9133, 'Previous workspace offset', align=Align.INLINE)
d.comment(0x9134, 'Previous stack register slot', align=Align.INLINE)
d.comment(0x9135, 'Load next result byte (X, then Y)', align=Align.INLINE)
d.comment(0x913A, 'Copied all result bytes? (P at &DA)', align=Align.INLINE)
d.comment(0x913C, 'Loop for remaining result bytes', align=Align.INLINE)
d.comment(0x913E, 'Return to OSBYTE dispatcher', align=Align.INLINE)


d.subroutine(0x913F, 'match_osbyte_code', title='Search remote OSBYTE table for match (NCALLP)', description="""Searches remote_osbyte_table for OSBYTE code A. X indexes the
last entry to check (table is scanned X..0). Returns Z=1 if
found. Called twice by remote_cmd_dispatch:

  X=9  → first 10 entries (NCTBPL: execute on both machines)
  X=14 → all 15 entries (NCTBMI: execute on terminal only)

The last 5 entries (&0B, &0C, &0F, &79, &7A) are terminal-only
because they affect the local keyboard or buffers.

On entry: A = OSBYTE code, X = table size - 1
On exit:  Z=1 if match found, Z=0 if not""")
d.comment(0x913F, 'Compare OSBYTE code with table entry', align=Align.INLINE)
d.comment(0x9142, 'Match found: return with Z=1', align=Align.INLINE)
d.comment(0x9144, 'Next table entry (descending)', align=Align.INLINE)
d.comment(0x9145, 'Loop for remaining entries', align=Align.INLINE)
d.comment(0x9147, 'Return; Z=1 if match, Z=0 if not', align=Align.INLINE)
for addr in range(0x9148, 0x9157):
    d.byte(addr)
d.comment(0x9148, 'OSBYTE &04: cursor key status', align=Align.INLINE)
d.comment(0x9149, 'OSBYTE &09: flash duration (1st colour)', align=Align.INLINE)
d.comment(0x914A, 'OSBYTE &0A: flash duration (2nd colour)', align=Align.INLINE)
d.comment(0x914B, 'OSBYTE &15: flush specific buffer', align=Align.INLINE)
d.comment(0x914C, 'OSBYTE &9A: video ULA control register', align=Align.INLINE)
d.comment(0x914D, 'OSBYTE &9B: video ULA palette', align=Align.INLINE)
d.comment(0x914E, 'OSBYTE &E1: function key &C0-&CF', align=Align.INLINE)
d.comment(0x914F, 'OSBYTE &E2: function key &D0-&DF', align=Align.INLINE)
d.comment(0x9150, 'OSBYTE &E3: function key &E0-&EF', align=Align.INLINE)
d.comment(0x9151, 'OSBYTE &E4: function key &F0-&FF', align=Align.INLINE)
d.comment(0x9152, 'OSBYTE &0B: auto-repeat delay', align=Align.INLINE)
d.comment(0x9153, 'OSBYTE &0C: auto-repeat rate', align=Align.INLINE)
d.comment(0x9154, 'OSBYTE &0F: flush buffer class', align=Align.INLINE)
d.comment(0x9155, 'OSBYTE &79: keyboard scan from X', align=Align.INLINE)
d.comment(0x9156, 'OSBYTE &7A: keyboard scan from 16', align=Align.INLINE)
d.comment(0x915B, 'OSWORD 7 (sound): handle via common path', align=Align.INLINE)


d.subroutine(0x9157, 'remote_osword_handler', title='NETVEC fn 8: remote OSWORD dispatch (NWORD)', description="""Only accepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope), rejecting all others. Sets Y=14 as the maximum
parameter byte count, then falls through to remote_cmd_data.""")


d.subroutine(0x915F, 'remote_cmd_data', title='Fn 8: remote OSWORD handler (NWORD)', description="""Only intercepts OSWORD 7 (make a sound) and OSWORD 8 (define an
envelope). Unlike NBYTE which returns results, NWORD is entirely
fire-and-forget -- no return path is implemented. The developer
explicitly noted this was acceptable since sound/envelope commands
don't return meaningful results. Copies up to 14 parameter bytes
from the RX buffer to workspace, tags the message as RWORD, and
transmits.""")
d.comment(0x9157, 'Y=&0E: max 14 parameter bytes for OSWORD', align=Align.INLINE)
d.comment(0x9159, 'OSWORD 7 = make a sound', align=Align.INLINE)
d.comment(0x915D, 'OSWORD 8 = define an envelope', align=Align.INLINE)
d.comment(0x915F, 'Not OSWORD 7 or 8: ignore (BNE exits)', align=Align.INLINE)
d.comment(0x9161, 'Point workspace to offset &DB for params', align=Align.INLINE)
d.comment(0x9163, 'Store workspace ptr offset &DB', align=Align.INLINE)
d.comment(0x9165, 'Load param byte from OSWORD param block', align=Align.INLINE)
d.comment(0x9167, 'Write param byte to workspace', align=Align.INLINE)
d.comment(0x9169, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x916A, 'Loop for all parameter bytes', align=Align.INLINE)
d.comment(0x916C, 'Y=0 after loop', align=Align.INLINE)
d.comment(0x916D, 'Point workspace to offset &DA', align=Align.INLINE)
d.comment(0x916F, 'Load original OSWORD code', align=Align.INLINE)
d.comment(0x9171, 'Store OSWORD code at ws+0', align=Align.INLINE)
d.comment(0x9173, 'Reset workspace ptr to base', align=Align.INLINE)
d.comment(0x9175, 'Y=&14: command type offset', align=Align.INLINE)
d.comment(0x9177, 'Tag as RWORD (port &E9)', align=Align.INLINE)
d.comment(0x9179, 'Store port tag at ws+&14', align=Align.INLINE)
d.comment(0x917B, 'A=1: single-byte TX', align=Align.INLINE)
d.comment(0x9180, 'Restore workspace ptr', align=Align.INLINE)


d.subroutine(0x91DE, 'printer_select_handler', title='Fn 5: printer selection changed (SELECT)', description="""Called when the printer selection changes. Compares X against
the network printer buffer number (&F0). If it matches,
initialises the printer buffer pointer (&0D61 = &1F) and
sets the initial flag byte (&0D60 = &41). Otherwise falls
through to return.""", on_entry={'x': '1-based buffer number'})
d.comment(0x91DE, 'X-1: convert 1-based buffer to 0-based', align=Align.INLINE)
d.comment(0x91DF, 'Is this the network printer buffer?', align=Align.INLINE)
d.comment(0x91E1, 'No: skip printer init', align=Align.INLINE)
d.comment(0x91E3, '&1F = initial buffer pointer offset', align=Align.INLINE)
d.comment(0x91E5, 'Reset printer buffer write position', align=Align.INLINE)
d.comment(0x91E8, '&41 = initial PFLAGS (bit 6 set, bit 0 set)', align=Align.INLINE)
d.comment(0x91EA, 'Store A to printer status byte', align=Align.INLINE)
d.comment(0x91EC, 'Return', align=Align.INLINE)


d.subroutine(0x91ED, 'remote_print_handler', title='Fn 1/2/3: network printer handler (PRINT)', description="""Handles network printer output. Reason 1 = chars in buffer (extract
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
d.comment(0x91ED, 'Only handle buffer 4 (network printer)', align=Align.INLINE)
d.comment(0x91EF, 'Not buffer 4: ignore', align=Align.INLINE)
d.comment(0x91F1, 'A = reason code', align=Align.INLINE)
d.comment(0x91F2, 'Reason 1? (DEX: 1->0)', align=Align.INLINE)
d.comment(0x91F3, 'Not reason 1: handle Ctrl-B/C', align=Align.INLINE)
d.comment(0x91F5, 'Get stack pointer for P register', align=Align.INLINE)
d.comment(0x91F6, 'Force I flag in stacked P to block IRQs', align=Align.INLINE)
d.comment(0x91F9, 'Write back modified P register', align=Align.INLINE)
d.comment(0x91FC, 'OSBYTE &91: extract char from MOS buffer', align=Align.INLINE)
d.comment(0x91FE, 'X=3: printer buffer number', align=Align.INLINE)
d.comment(0x9203, 'Buffer empty: return', align=Align.INLINE)
d.comment(0x9205, 'Y = extracted character', align=Align.INLINE)
d.comment(0x9206, 'Store char in output buffer', align=Align.INLINE)
d.comment(0x9209, 'Buffer nearly full? (&6E = threshold)', align=Align.INLINE)
d.comment(0x920B, 'Not full: get next char', align=Align.INLINE)
d.comment(0x920D, 'Buffer full: flush to network', align=Align.INLINE)
d.comment(0x9210, 'Continue after flush', align=Align.INLINE)
d.comment(0x921D, 'EOR #1: toggle print-active flag (bit 0)', align=Align.INLINE)
d.comment(0x9224, 'Test if sequence changed (bit 7 mismatch)', align=Align.INLINE)
d.comment(0x922F, 'Extract upper nibble of PFLAGS', align=Align.INLINE)
d.comment(0x9234, 'Merge print-active bit from original A', align=Align.INLINE)
d.comment(0x9236, 'Recombine into new PFLAGS value', align=Align.INLINE)


d.subroutine(0x9212, 'store_output_byte', title='Store output byte to network buffer', description="""Stores byte A at the current output offset in the RX buffer
pointed to by (net_rx_ptr). Advances the offset counter and
triggers a flush if the buffer is full.""", on_entry={'a': 'byte to store'}, on_exit={'y': 'buffer offset before store'})
d.comment(0x9212, 'Load current buffer offset', align=Align.INLINE)
d.comment(0x9215, 'Store byte at current position', align=Align.INLINE)
d.comment(0x9217, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x921A, 'Return; Y = buffer offset', align=Align.INLINE)
d.comment(0x921B, 'Save reason code', align=Align.INLINE)
d.comment(0x921C, 'A = reason code', align=Align.INLINE)
d.comment(0x921F, 'Store toggled flag as output byte', align=Align.INLINE)
d.comment(0x9222, 'XOR with PFLAGS', align=Align.INLINE)
d.comment(0x9225, 'Sequence unchanged: skip flush', align=Align.INLINE)
d.comment(0x9227, 'Undo ROR', align=Align.INLINE)
d.comment(0x9228, 'Update PFLAGS', align=Align.INLINE)
d.comment(0x922A, 'Flush current output block', align=Align.INLINE)
d.comment(0x922D, 'Load PFLAGS', align=Align.INLINE)
d.comment(0x9231, 'Shift for bit extraction', align=Align.INLINE)
d.comment(0x9232, 'Save in X', align=Align.INLINE)
d.comment(0x9233, 'Restore original reason code', align=Align.INLINE)
d.comment(0x9235, 'Retrieve shifted PFLAGS', align=Align.INLINE)
d.comment(0x9237, 'Update PFLAGS', align=Align.INLINE)
d.comment(0x9239, 'Return', align=Align.INLINE)


d.subroutine(0x923A, 'flush_output_block', title='Flush output block', description="""Sends the accumulated output block over the network, resets the
buffer pointer, and prepares for the next block of output data.""")
d.comment(0x923A, 'Store buffer length at workspace offset &08', align=Align.INLINE)
d.comment(0x923C, 'Current buffer fill position', align=Align.INLINE)
d.comment(0x923F, 'Write to workspace offset &08', align=Align.INLINE)
d.comment(0x9241, 'Store page high byte at offset &09', align=Align.INLINE)
d.comment(0x9243, 'Y=&09', align=Align.INLINE)
d.comment(0x9244, 'Write page high byte at offset &09', align=Align.INLINE)
d.comment(0x9246, 'Also store at offset &05', align=Align.INLINE)
d.comment(0x9248, '(end address high byte)', align=Align.INLINE)
d.comment(0x924A, 'Y=&0B: flag byte offset', align=Align.INLINE)
d.comment(0x924C, 'X=&26: start from template entry &26', align=Align.INLINE)
d.comment(0x924E, 'Reuse ctrl_block_setup with CLV entry', align=Align.INLINE)
d.comment(0x9251, 'Y=&0A: sequence flag byte offset', align=Align.INLINE)
d.comment(0x9252, 'Load protocol flags (PFLAGS)', align=Align.INLINE)
d.comment(0x9254, 'Save current PFLAGS', align=Align.INLINE)
d.comment(0x9255, 'Carry = current sequence (bit 7)', align=Align.INLINE)
d.comment(0x9256, 'Restore original PFLAGS', align=Align.INLINE)
d.comment(0x9257, 'Toggle sequence number (bit 7 of PFLAGS)', align=Align.INLINE)
d.comment(0x9259, 'Save toggled PFLAGS', align=Align.INLINE)
d.comment(0x925B, 'Old sequence bit into bit 0', align=Align.INLINE)
d.comment(0x925C, 'Store sequence flag at offset &0A', align=Align.INLINE)
d.comment(0x925E, 'Y=&1F: buffer start offset', align=Align.INLINE)
d.comment(0x9260, 'Reset printer buffer to start (&1F)', align=Align.INLINE)
d.comment(0x9263, 'A=0: printer output flag', align=Align.INLINE)
d.comment(0x9265, 'X=0: workspace low byte', align=Align.INLINE)
d.comment(0x9266, 'Y = workspace page high byte', align=Align.INLINE)
d.comment(0x9268, 'Enable interrupts before TX', align=Align.INLINE)


d.subroutine(0x92FA, 'save_vdu_state', title='Save VDU workspace state', description="""Stores the cursor position value from &0355 into NFS workspace,
then reads cursor position (OSBYTE &85), shadow RAM (OSBYTE &C2),
and screen start (OSBYTE &C3) via read_vdu_osbyte, storing
each result into consecutive workspace bytes. The JSR to
read_vdu_osbyte_x0 is a self-calling trick: it executes
read_vdu_osbyte twice (once for &C2, once for &C3) because the
RTS returns to the instruction at read_vdu_osbyte_x0 itself.""")
d.comment(0x92FA, 'Read cursor editing state', align=Align.INLINE)
d.comment(0x92FD, 'Store to workspace[Y]', align=Align.INLINE)
d.comment(0x92FF, 'Preserve in X for OSBYTE', align=Align.INLINE)
d.comment(0x9300, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.comment(0x9303, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x9305, 'Y result from OSBYTE &85', align=Align.INLINE)
d.comment(0x9306, 'Store Y pos to workspace (X=0)', align=Align.INLINE)
d.comment(0x9308, 'Self-call trick: executes twice', align=Align.INLINE)
d.comment(0x930B, 'X=0 for (zp,X) addressing', align=Align.INLINE)
d.comment(0x930D, 'Index into OSBYTE number table', align=Align.INLINE)
d.comment(0x930F, 'Next table entry next time', align=Align.INLINE)
d.comment(0x9311, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x9313, 'Read OSBYTE number from table', align=Align.INLINE)
d.comment(0x9316, 'Y=&FF: read current value', align=Align.INLINE)
d.comment(0x9318, 'Call OSBYTE', align=Align.INLINE)
d.comment(0x931B, 'Result in X to A', align=Align.INLINE)
d.comment(0x931C, 'X=0 for indexed indirect store', align=Align.INLINE)
d.comment(0x931E, 'Store result to workspace', align=Align.INLINE)
d.comment(0x92AE, 'Save current table index', align=Align.INLINE)
d.comment(0x92B0, 'Push for later restore', align=Align.INLINE)
d.comment(0x92B1, 'Point workspace to palette save area (&E9)', align=Align.INLINE)
d.comment(0x92B3, 'Set workspace low byte', align=Align.INLINE)
d.comment(0x92B5, 'Y=0: first palette entry', align=Align.INLINE)
d.comment(0x92B7, 'Clear table index counter', align=Align.INLINE)
d.comment(0x92B9, 'Save current screen MODE to workspace', align=Align.INLINE)
d.comment(0x92BC, 'Store MODE at workspace[0]', align=Align.INLINE)
d.comment(0x92BE, 'Advance workspace pointer past MODE byte', align=Align.INLINE)
d.comment(0x92C0, 'Read colour count (from &0351)', align=Align.INLINE)
d.comment(0x92C3, 'Push for iteration count tracking', align=Align.INLINE)
d.comment(0x92C4, 'A=0: logical colour number for OSWORD', align=Align.INLINE)
d.comment(0x92C5, 'Store logical colour at workspace[0]', align=Align.INLINE)
d.comment(0x92C7, 'X = workspace ptr low (param block addr)', align=Align.INLINE)
d.comment(0x92C9, 'Y = workspace ptr high', align=Align.INLINE)
d.comment(0x92CB, 'OSWORD &0B: read palette for logical colour', align=Align.INLINE)
d.comment(0x92D0, 'Recover colour count', align=Align.INLINE)
d.comment(0x92D1, 'Y=0: access workspace[0]', align=Align.INLINE)
d.comment(0x92D3, 'Write colour count back to workspace[0]', align=Align.INLINE)
d.comment(0x92D5, 'Y=1: access workspace[1] (palette result)', align=Align.INLINE)
d.comment(0x92D6, 'Read palette value returned by OSWORD', align=Align.INLINE)
d.comment(0x92D8, 'Push palette value for next iteration', align=Align.INLINE)
d.comment(0x92D9, 'X = current workspace ptr low', align=Align.INLINE)
d.comment(0x92DB, 'Advance workspace pointer', align=Align.INLINE)
d.comment(0x92DD, 'Increment table index', align=Align.INLINE)
d.comment(0x92DF, 'Y=0 for next store', align=Align.INLINE)
d.comment(0x92E0, 'Load table index as logical colour', align=Align.INLINE)
d.comment(0x92E2, 'Loop until workspace wraps past &F9', align=Align.INLINE)
d.comment(0x92E4, 'Continue for all 16 palette entries', align=Align.INLINE)
d.comment(0x92E6, 'Discard last palette value from stack', align=Align.INLINE)
d.comment(0x92E7, 'Reset table index to 0', align=Align.INLINE)
d.comment(0x92E9, 'Advance workspace past palette data', align=Align.INLINE)
d.comment(0x92EB, 'Save cursor pos and OSBYTE state values', align=Align.INLINE)
d.comment(0x92EE, 'Advance workspace past VDU state data', align=Align.INLINE)
d.comment(0x92F0, 'Recover saved table index', align=Align.INLINE)
d.comment(0x92F1, 'Restore table index', align=Align.INLINE)
d.comment(0x92F3, 'Restore LSTAT from saved OLDJSR value', align=Align.INLINE)
d.comment(0x92F6, 'Write to protection status', align=Align.INLINE)
d.comment(0x92F9, 'Return', align=Align.INLINE)


d.subroutine(0x969A, 'adlc_init', title='ADLC initialisation', description="""Reads station ID (INTOFF side effect), performs full ADLC reset,
checks for Tube presence (OSBYTE &EA), then falls through to
adlc_init_workspace.""")
d.comment(0x969A, 'INTOFF: read station ID, disable NMIs', align=Align.INLINE)
d.comment(0x969D, 'Full ADLC hardware reset', align=Align.INLINE)
d.comment(0x96A0, 'OSBYTE &EA: check Tube co-processor', align=Align.INLINE)
d.comment(0x96A2, 'X=0 for OSBYTE', align=Align.INLINE)
d.comment(0x96A4, 'Clear Econet init flag before setup', align=Align.INLINE)
d.comment(0x96A7, 'Y=&FF for OSBYTE', align=Align.INLINE)
d.comment(0x96AF, 'OSBYTE &8F: issue service request', align=Align.INLINE)
d.comment(0x96B1, 'X=&0C: NMI claim service', align=Align.INLINE)
d.comment(0x96B3, 'Y=&FF: pass to adlc_init_workspace', align=Align.INLINE)


d.subroutine(0x96B8, 'init_nmi_workspace', title='Initialise NMI workspace (skip service request)', description="""Sub-entry of adlc_init_workspace that skips the OSBYTE &8F
service request. Copies 32 bytes of NMI shim from ROM to
&0D00, patches the ROM bank number, sets init flags, reads
station ID, and re-enables NMIs.""")


d.subroutine(0x96B5, 'adlc_init_workspace', title='Initialise NMI workspace', description="""Issues OSBYTE &8F with X=&0C (NMI claim service request) before
copying the NMI shim. Sub-entry at &96B8 skips the service
request for quick re-init. Then copies 32 bytes of
NMI shim from ROM (&9FB2) to RAM (&0D00), patches the current
ROM bank number into the shim's self-modifying code at &0D07,
sets TX clear flag and econet_init_flag to &80, reads station ID
from &FE18 (INTOFF side effect), stores it in the TX scout buffer,
and re-enables NMIs by reading &FE20 (INTON side effect).""")
d.comment(0x96B8, 'Copy 32 bytes of NMI shim from ROM to &0D00', align=Align.INLINE)
d.comment(0x96BA, 'Read byte from NMI shim ROM source', align=Align.INLINE)
d.comment(0x96BD, 'Write to NMI shim RAM at &0D00', align=Align.INLINE)
d.comment(0x96C0, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x96C1, 'Loop until all 32 bytes copied', align=Align.INLINE)
d.comment(0x96C3, 'Patch current ROM bank into NMI shim', align=Align.INLINE)
d.comment(0x96C5, 'Self-modifying code: ROM bank at &0D07', align=Align.INLINE)
d.comment(0x96C8, '&80 = Econet initialised', align=Align.INLINE)
d.comment(0x96CA, 'Mark TX as complete (ready)', align=Align.INLINE)
d.comment(0x96CD, 'Mark Econet as initialised', align=Align.INLINE)
d.comment(0x96D0, 'Read station ID (&FE18 = INTOFF side effect)', align=Align.INLINE)
d.comment(0x96D3, 'Store our station ID in TX scout', align=Align.INLINE)
d.comment(0x96D6, 'Y=0 after copy loop: net = local', align=Align.INLINE)
d.comment(0x96D9, 'Clear Tube release flag', align=Align.INLINE)
d.comment(0x96DB, 'INTON: re-enable NMIs (&FE20 read side effect)', align=Align.INLINE)
d.comment(0x96DE, 'Return', align=Align.INLINE)
d.comment(0x9F8A, 'Econet not initialised -- skip to adlc_rx_listen', align=Align.INLINE)
d.comment(0x9F8F, 'Spin until NMI handler = &96DF (nmi_rx_scout)', align=Align.INLINE)


d.subroutine(0x9FA2, 'save_econet_state', title='Reset Econet flags and enter RX listen', description="""Disables NMIs via INTOFF (BIT &FE18), clears tx_clear_flag and
econet_init_flag to zero, then falls through to adlc_rx_listen
with Y=5.""")
d.comment(0x9FA2, 'INTOFF: disable NMIs', align=Align.INLINE)
d.comment(0x9FA5, 'Clear both flags', align=Align.INLINE)
d.comment(0x9FA7, 'TX not in progress', align=Align.INLINE)
d.comment(0x9FAA, 'Econet not initialised', align=Align.INLINE)
d.comment(0x9FAD, 'Y=5: service call workspace page', align=Align.INLINE)
d.comment(0x9FAF, 'Set ADLC to RX listen mode', align=Align.INLINE)


d.subroutine(0x0016, 'tube_brk_handler', title='Tube BRK handler (BRKV target) — reference: NFS11 NEWBR', description="""Sends error information to the Tube co-processor via R2 and R4:
  1. Sends &FF to R4 (WRIFOR) to signal error
  2. Reads R2 data (flush any pending byte)
  3. Sends &00 via R2, then error number from (&FD),0
  4. Loops sending error string bytes via R2 until zero terminator
  5. Falls through to tube_reset_stack → tube_main_loop
The main loop continuously polls R1 for WRCH requests (forwarded
to OSWRITCH &FFCB) and R2 for command bytes (dispatched via the
12-entry table at &0500). The R2 command byte is stored at &51
(self-modifying the JMP indirect low byte) before dispatch.""")


d.subroutine(0x0400, 'tube_code_page4', title='Tube host code page 4 — reference: NFS12 (BEGIN, ADRR, SENDW)', description="""Copied from ROM at reloc_p4_src during init. The first 28 bytes (&0400-&041B)
overlap with the end of the ZP block (the same ROM bytes serve both
the ZP copy at &005B-&0076 and this page at &0400-&041B). Contains:
  &0400: JMP &0484 (BEGIN — startup/CLI entry, break type check)
  &0403: JMP &06E2 (tube_escape_check)
  &0406: tube_addr_claim — Tube address claim (ADRR protocol)
  &0414: tube_release_claim — release address claim via R4 cmd 5
  &0421: tube_post_init — reset claimed-address state to &80
  &0435: data transfer setup (SENDW protocol) — &0435-&0483
  &0484: BEGIN — startup entry, sends ROM contents to Tube
  &04CB: tube_claim_default — claim default transfer address
  &04D2: tube_init_reloc — extract relocation address from ROM""")


d.subroutine(0x0414, 'tube_release_claim', title='Release Tube address claim via R4 command 5', description="""Saves interrupt state (PHP/SEI), sends R4 command 5 (release)
followed by the currently-claimed address, then restores
interrupts. Falls through to tube_post_init to reset the
claimed-address state to &80.""")


d.subroutine(0x04CB, 'tube_claim_default', title='Claim default Tube transfer address', description="""Sets Y=0, X=&53 (address &0053), then JMP tube_addr_claim
to initiate a Tube address claim for the default transfer
address. Called from the BEGIN startup path and after the
page transfer loop completes.""")


d.subroutine(0x04D2, 'tube_init_reloc', title='Initialise relocation address for ROM transfer', description="""Sets source page to &8000 and page counter to &80. Checks
ROM type bit 5 for a relocation address in the ROM header;
if present, extracts the 4-byte address from after the
copyright string. Otherwise uses default &8000 start.""")


d.subroutine(0x0484, 'tube_begin', title='Tube host startup entry (BEGIN)', description="""Entry point via JMP from &0400. Enables interrupts, checks
break type via OSBYTE &FD: soft break re-initialises Tube and
restarts, hard break claims address &FF. Sends ROM contents
to co-processor page by page via SENDW, then claims the final
transfer address.""")


d.subroutine(0x0500, 'tube_dispatch_table', title='Tube host code page 5 — reference: NFS13 (TASKS, BPUT-FILE)', description="""Copied from ROM at reloc_p5_src during init. Contains:
  &0500: 12-entry dispatch table (&0500-&0517)
  &0518: 8-byte Tube control register value table
  &0520: tube_osbput — write byte to file
  &052D: tube_osbget — read byte from file
  &0537: tube_osrdch — read character
  &053A: tube_rdch_reply — send carry+data as reply
  &0542: tube_osfind — open/close file
  &055E: tube_osargs — file argument read/write
  &0582: tube_read_string — read string from R2 into &0700
  &0596: tube_oscli — execute * command
  &059C: tube_reply_ack — send &7F acknowledge
  &05A9: tube_osfile — whole file operation
  &05D1: tube_osgbpb — multi-byte file read/write
Code continues seamlessly into page 6 (tube_osbyte_short at &05F2
straddles the page boundary with a BVC at &05FF/&0600).""")


d.subroutine(0x06C5, 'tube_read_r2', title='Read a byte from Tube data register R2', description="""Polls Tube status register 2 until data is available
(bit 7 set), then loads A from Tube data register 2.
Called by all Tube dispatch handlers that receive data
or parameters from the co-processor.""")


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


d.subroutine(0x9269, 'econet_tx_retry', title='Byte-stream transmit (BSXMIT/BSPSX)', description="""Transmits a data packet over econet with sequence number tracking.
Sets up the TX control block pointer from X/Y, computes the
sequence bit from A AND fs_sequence_nos (handle-based tracking),
merges it into the flag byte at (net_tx_ptr)+0, then initiates
transmit via tx_poll_ff. Sets end addresses (offsets 8/9) to
&FF to allow unlimited data. Selects port byte &D1 (print) or
&90 (FS) based on the original A value. Polls the TX result in
a loop via BRIANX (c8530), retrying while the result bit
differs from the expected sequence. On success, toggles the
sequence tracking bit in fs_sequence_nos.""", on_entry={'a': 'handle bitmask (0=printer, non-zero=file)', 'x': 'TX control block address low', 'y': 'TX control block address high'})
d.comment(0x9269, 'Set TX control block ptr low byte', align=Align.INLINE)
d.comment(0x926B, 'Set TX control block ptr high byte', align=Align.INLINE)
d.comment(0x926D, 'Save A (handle bitmask) for later', align=Align.INLINE)
d.comment(0x926E, 'Compute sequence bit from handle', align=Align.INLINE)
d.comment(0x9271, 'Zero: no sequence bit set', align=Align.INLINE)
d.comment(0x9273, 'Non-zero: normalise to bit 0', align=Align.INLINE)
d.comment(0x9275, 'Y=0: flag byte offset in TXCB', align=Align.INLINE)
d.comment(0x9277, 'Merge sequence into existing flag byte', align=Align.INLINE)
d.comment(0x9279, 'Save merged flag byte', align=Align.INLINE)
d.comment(0x927A, 'Write flag+sequence to TXCB byte 0', align=Align.INLINE)
d.comment(0x927C, 'Transmit with full retry', align=Align.INLINE)
d.comment(0x927F, 'End address &FFFF = unlimited data length', align=Align.INLINE)
d.comment(0x9281, 'Y=8: end address low offset in TXCB', align=Align.INLINE)
d.comment(0x9283, 'Store &FF to end addr low', align=Align.INLINE)
d.comment(0x9286, 'Store &FF to end addr high (Y=9)', align=Align.INLINE)
d.comment(0x9288, 'Recover merged flag byte', align=Align.INLINE)
d.comment(0x9289, 'Save in X for sequence compare', align=Align.INLINE)
d.comment(0x928A, 'Y=&D1: printer port number', align=Align.INLINE)
d.comment(0x928C, 'Recover saved handle bitmask', align=Align.INLINE)
d.comment(0x928D, 'Re-save for later consumption', align=Align.INLINE)
d.comment(0x928E, 'A=0: port &D1 (print); A!=0: port &90 (FS)', align=Align.INLINE)
d.comment(0x9290, 'Y=&90: FS data port', align=Align.INLINE)
d.comment(0x9292, 'A = selected port number', align=Align.INLINE)
d.comment(0x9293, 'Y=1: port byte offset in TXCB', align=Align.INLINE)
d.comment(0x9295, 'Write port to TXCB byte 1', align=Align.INLINE)
d.comment(0x9297, 'A = saved flag byte (expected sequence)', align=Align.INLINE)
d.comment(0x9299, 'Push expected sequence for retry loop', align=Align.INLINE)
d.comment(0x929A, 'Flag byte &7F = waiting for reply', align=Align.INLINE)
d.comment(0x929C, 'Write to TXCB flag byte (Y=0)', align=Align.INLINE)
d.comment(0x929E, 'Transmit and wait for reply (BRIANX)', align=Align.INLINE)
d.comment(0x92A1, 'Recover expected sequence', align=Align.INLINE)
d.comment(0x92A2, 'Keep on stack for next iteration', align=Align.INLINE)
d.comment(0x92A3, 'Check if TX result matches expected sequence', align=Align.INLINE)
d.comment(0x92A5, 'Bit 0 to carry (sequence mismatch?)', align=Align.INLINE)
d.comment(0x92A6, 'C=1: mismatch, retry transmit', align=Align.INLINE)
d.comment(0x92A8, 'Clean up: discard expected sequence', align=Align.INLINE)
d.comment(0x92A9, 'Discard saved handle bitmask', align=Align.INLINE)
d.comment(0x92AA, 'Toggle sequence bit on success', align=Align.INLINE)
d.comment(0x92AD, 'Return', align=Align.INLINE)


d.subroutine(0x92AE, 'lang_2_save_palette_vdu', title='Save palette and VDU state (CVIEW)', description="""Part of the VIEW facility (second iteration, started 27/7/82).
Uses dynamically allocated buffer store. The WORKP1 pointer
(&9E,&9F) serves double duty: non-zero indicates data ready AND
provides the buffer address — an efficient use of scarce zero-
page space. This code must be user-transparent as the NFS may not
be the dominant filing system.
Reads all 16 palette entries using OSWORD &0B (read palette) and
stores the results. Then reads cursor position (OSBYTE &85),
shadow RAM allocation (OSBYTE &C2), and screen start address
(OSBYTE &C3) using the 3-entry table at &931E.
On completion, restores the JSR buffer protection bits (LSTAT)
from OLDJSR to re-enable JSR reception, which was disabled during
the screen data capture to prevent interference.""")


d.subroutine(0x995E, 'post_ack_scout', title='Post-ACK scout processing', description="""Called after the scout ACK has been transmitted. Processes the
received scout data stored in the buffer at &0D3D-&0D48.
Checks the port byte (&0D40) against open receive blocks to
find a matching listener. If a match is found, sets up the
data RX handler chain for the four-way handshake data phase.
If no match, discards the frame.""")
d.comment(0x995E, 'Write CR2 to clear status after ACK TX', align=Align.INLINE)
d.comment(0x9964, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x9967, 'Install next NMI handler', align=Align.INLINE)
d.comment(0x996A, 'Jump to start data TX phase', align=Align.INLINE)
d.comment(0x996D, 'Jump to error handler', align=Align.INLINE)
d.comment(0x9970, 'A=2: test bit1 of tx_flags', align=Align.INLINE)
d.comment(0x9972, 'BIT tx_flags: check data transfer bit', align=Align.INLINE)
d.comment(0x9975, 'Bit1 clear: no transfer -- return', align=Align.INLINE)
d.comment(0x9977, 'CLC: init carry for 4-byte add', align=Align.INLINE)
d.comment(0x9978, 'Save carry on stack for loop', align=Align.INLINE)
d.comment(0x9979, 'Y=8: RXCB high pointer offset', align=Align.INLINE)
d.comment(0x997B, 'Load RXCB[Y] (buffer pointer byte)', align=Align.INLINE)
d.comment(0x997D, 'Restore carry from stack', align=Align.INLINE)
d.comment(0x997E, 'Add transfer count byte', align=Align.INLINE)
d.comment(0x9981, 'Store updated pointer back to RXCB', align=Align.INLINE)
d.comment(0x9983, 'Next byte', align=Align.INLINE)
d.comment(0x9984, 'Save carry for next iteration', align=Align.INLINE)
d.comment(0x9985, 'Done 4 bytes? (Y reaches &0C)', align=Align.INLINE)
d.comment(0x9987, 'No: continue adding', align=Align.INLINE)
d.comment(0x9989, 'Discard final carry', align=Align.INLINE)
d.comment(0x998A, 'A=&20: test bit5 of tx_flags', align=Align.INLINE)
d.comment(0x998C, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x998F, 'No Tube: skip Tube update', align=Align.INLINE)
d.comment(0x9991, 'Save X on stack', align=Align.INLINE)
d.comment(0x9992, 'Push X', align=Align.INLINE)
d.comment(0x9993, 'A=8: offset for Tube address', align=Align.INLINE)
d.comment(0x9995, 'CLC for address calculation', align=Align.INLINE)
d.comment(0x9996, 'Add workspace base offset', align=Align.INLINE)
d.comment(0x9998, 'X = address low for Tube claim', align=Align.INLINE)
d.comment(0x9999, 'Y = address high for Tube claim', align=Align.INLINE)
d.comment(0x999B, 'A=1: Tube claim type (read)', align=Align.INLINE)
d.comment(0x999D, 'Claim Tube address for transfer', align=Align.INLINE)
d.comment(0x99A0, 'Load extra RX data byte', align=Align.INLINE)
d.comment(0x99A3, 'Send to Tube via R3', align=Align.INLINE)
d.comment(0x99A6, 'SEC: init carry for increment', align=Align.INLINE)
d.comment(0x99A7, 'Y=8: start at high pointer', align=Align.INLINE)
d.comment(0x99A9, 'A=0: add carry only (increment)', align=Align.INLINE)
d.comment(0x99AB, 'Add carry to pointer byte', align=Align.INLINE)
d.comment(0x99AD, 'Store back to RXCB', align=Align.INLINE)
d.comment(0x99AF, 'Next byte', align=Align.INLINE)
d.comment(0x99B0, 'Keep going while carry propagates', align=Align.INLINE)
d.comment(0x99B2, 'Restore X from stack', align=Align.INLINE)
d.comment(0x99B3, 'Transfer to X register', align=Align.INLINE)
d.comment(0x99B4, 'A=&FF: return value (transfer done)', align=Align.INLINE)
d.comment(0x99B6, 'Return', align=Align.INLINE)
d.comment(0x99B7, 'Load received port byte', align=Align.INLINE)
d.comment(0x99BA, 'Port != 0: data transfer frame', align=Align.INLINE)
d.comment(0x99BC, 'Port=0: load control byte', align=Align.INLINE)
d.comment(0x99BF, 'Ctrl = &82 (POKE)?', align=Align.INLINE)
d.comment(0x99C1, 'Yes: POKE also needs data transfer', align=Align.INLINE)
d.comment(0x99C3, 'Other port-0 ops: immediate dispatch', align=Align.INLINE)
d.comment(0x99C6, 'Update buffer pointer and check for Tube', align=Align.INLINE)
d.comment(0x99C9, 'Transfer not done: skip buffer update', align=Align.INLINE)
d.comment(0x99CB, 'Load buffer bytes remaining', align=Align.INLINE)
d.comment(0x99CD, 'CLC for address add', align=Align.INLINE)
d.comment(0x99CE, 'Add to buffer base address', align=Align.INLINE)
d.comment(0x99D0, 'No carry: skip high byte increment', align=Align.INLINE)
d.comment(0x99D2, 'Carry: increment buffer high byte', align=Align.INLINE)
d.comment(0x99D4, 'Y=8: store updated buffer position', align=Align.INLINE)
d.comment(0x99D6, 'Store updated low byte to RXCB', align=Align.INLINE)
d.comment(0x99D8, 'Y=9: buffer high byte offset', align=Align.INLINE)
d.comment(0x99D9, 'Load updated buffer high byte', align=Align.INLINE)
d.comment(0x99DB, 'Store high byte to RXCB', align=Align.INLINE)
d.comment(0x99DD, 'Check port byte again', align=Align.INLINE)
d.comment(0x99E0, 'Port=0: immediate op, discard+listen', align=Align.INLINE)
d.comment(0x99E2, 'Load source network from scout buffer', align=Align.INLINE)
d.comment(0x99E5, 'Y=3: RXCB source network offset', align=Align.INLINE)
d.comment(0x99E7, 'Store source network to RXCB', align=Align.INLINE)
d.comment(0x99E9, 'Y=2: source station offset', align=Align.INLINE)
d.comment(0x99EA, 'Load source station from scout buffer', align=Align.INLINE)
d.comment(0x99ED, 'Store source station to RXCB', align=Align.INLINE)
d.comment(0x99EF, 'Y=1: port byte offset', align=Align.INLINE)
d.comment(0x99F0, 'Load port byte', align=Align.INLINE)
d.comment(0x99F3, 'Store port to RXCB', align=Align.INLINE)
d.comment(0x99F5, 'Y=0: control/flag byte offset', align=Align.INLINE)
d.comment(0x99F6, 'Load control byte from scout', align=Align.INLINE)
d.comment(0x99F9, 'Set bit7 = reception complete flag', align=Align.INLINE)
d.comment(0x99FB, 'Store to RXCB (marks CB as complete)', align=Align.INLINE)


d.subroutine(0x9A68, 'immediate_op', title='Immediate operation handler (port = 0)', description="""Handles immediate (non-data-transfer) operations received via
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


d.subroutine(0x9970, 'advance_rx_buffer_ptr', title='Advance RX buffer pointer after transfer', description="""Adds the transfer count to the RXCB buffer pointer (4-byte
addition). If a Tube transfer is active, re-claims the Tube
address and sends the extra RX byte via R3, incrementing the
Tube pointer by 1.""")


d.subroutine(0x99C6, 'rx_complete_update_rxcb', title='Complete RX and update RXCB', description="""Post-scout completion for data transfer frames (port != 0)
and POKE (ctrl=&82). Calls advance_rx_buffer_ptr, updates
the open port buffer address, then writes source station/
network, port, and control byte into the RXCB.""")


d.subroutine(0x9A0D, 'install_rx_scout_handler', title='Install RX scout NMI handler', description="""Installs nmi_rx_scout (&96DF) as the NMI handler via
set_nmi_vector, without first calling adlc_rx_listen.
Used when the ADLC is already in the correct RX mode.""")


d.subroutine(0x9A14, 'copy_scout_to_buffer', title='Copy scout data to port buffer', description="""Copies scout data bytes (offsets 4-11) from the RX scout
buffer into the open port buffer, handling both direct memory
and Tube R3 write paths.""")


d.subroutine(0x9A4D, 'release_tube', title='Release Tube co-processor claim', description="""If need_release_tube bit 7 is clear (Tube is claimed), calls
tube_addr_claim with A=&82 to release it, then clears the
release flag via LSR.""")


d.subroutine(0x9A59, 'inc_buf_counter_32', title='Increment 32-bit buffer counter', description="""Increments a 4-byte counter across port_buf_len / port_buf_len_hi
/ open_port_buf / open_port_buf_hi with carry propagation.
Returns Z=1 if the counter wraps to zero.""")


d.subroutine(0x99FD, 'discard_reset_listen', title='Discard with Tube release', description="""Conditionally releases the Tube co-processor before discarding.
If tx_flags bit 1 is set (Tube transfer was active), calls
sub_c9a2b to release the Tube claim, then falls through to
discard_listen. The main teardown path for RX operations that
used the Tube.""")
d.comment(0x99FD, 'Tube flag bit 1 AND tx_flags bit 1', align=Align.INLINE)
d.comment(0x9A05, 'No Tube transfer active -- skip release', align=Align.INLINE)
d.comment(0x9A07, 'Release Tube claim before discarding', align=Align.INLINE)


d.subroutine(0x9A0A, 'discard_listen', title='Discard frame and return to idle listen', description="""Calls adlc_rx_listen to re-enter idle RX mode (CR1=&82, CR2=&67),
then installs nmi_rx_scout (&96DF) as the NMI handler via
set_nmi_vector. Returns to the caller's NMI context. Used as
the common discard tail for both gentle rejection (wrong
station/network) and error recovery paths.""")
d.comment(0x9A0A, 'Re-enter idle RX listen mode', align=Align.INLINE)
d.comment(0x9A0D, 'Install nmi_rx_scout (&96DF) as NMI handler', align=Align.INLINE)
d.comment(0x9A0F, 'High byte of nmi_rx_scout', align=Align.INLINE)
d.comment(0x9A11, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9A14, 'Save X on stack', align=Align.INLINE)
d.comment(0x9A15, 'Push X', align=Align.INLINE)
d.comment(0x9A16, 'X=4: start at scout byte offset 4', align=Align.INLINE)
d.comment(0x9A18, 'A=2: Tube transfer check mask', align=Align.INLINE)
d.comment(0x9A1A, 'BIT tx_flags: check Tube bit', align=Align.INLINE)
d.comment(0x9A1D, 'Tube active: use R3 write path', align=Align.INLINE)
d.comment(0x9A1F, 'Y = current buffer position', align=Align.INLINE)
d.comment(0x9A21, 'Load scout data byte', align=Align.INLINE)
d.comment(0x9A24, 'Store to port buffer', align=Align.INLINE)
d.comment(0x9A26, 'Advance buffer pointer', align=Align.INLINE)
d.comment(0x9A27, 'No page crossing', align=Align.INLINE)
d.comment(0x9A29, 'Page crossing: inc buffer high byte', align=Align.INLINE)
d.comment(0x9A2B, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x9A2D, 'No pages left: overflow', align=Align.INLINE)
d.comment(0x9A2F, 'Next scout data byte', align=Align.INLINE)
d.comment(0x9A30, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x9A32, 'Done all scout data? (X reaches &0C)', align=Align.INLINE)
d.comment(0x9A34, 'No: continue copying', align=Align.INLINE)
d.comment(0x9A36, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9A37, 'Transfer to X register', align=Align.INLINE)
d.comment(0x9A38, 'Jump to completion handler', align=Align.INLINE)
d.comment(0x9A3B, 'Tube path: load scout data byte', align=Align.INLINE)
d.comment(0x9A3E, 'Send byte to Tube via R3', align=Align.INLINE)
d.comment(0x9A41, 'Increment buffer position counters', align=Align.INLINE)
d.comment(0x9A44, 'Counter overflow: handle end of buffer', align=Align.INLINE)
d.comment(0x9A46, 'Next scout data byte', align=Align.INLINE)
d.comment(0x9A47, 'Done all scout data?', align=Align.INLINE)
d.comment(0x9A49, 'No: continue Tube writes', align=Align.INLINE)
d.comment(0x9A4D, 'Check if Tube needs releasing', align=Align.INLINE)
d.comment(0x9A4F, 'Bit7 set: already released', align=Align.INLINE)
d.comment(0x9A51, 'A=&82: Tube release claim type', align=Align.INLINE)
d.comment(0x9A53, 'Release Tube address claim', align=Align.INLINE)
d.comment(0x9A56, 'Clear release flag (LSR clears bit7)', align=Align.INLINE)
d.comment(0x9A58, 'Return', align=Align.INLINE)
d.comment(0x9A59, 'Increment buffer position (4-byte)', align=Align.INLINE)
d.comment(0x9A5B, "Low byte didn't wrap: done", align=Align.INLINE)
d.comment(0x9A5D, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9A5F, 'No further carry: done', align=Align.INLINE)
d.comment(0x9A61, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9A63, 'No further carry: done', align=Align.INLINE)
d.comment(0x9A65, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9A67, 'Return', align=Align.INLINE)
d.comment(0x9A68, 'Control byte &81-&88 range check', align=Align.INLINE)
d.comment(0x9A6B, 'Below &81: not an immediate op', align=Align.INLINE)
d.comment(0x9A6D, 'Out of range low: jump to discard', align=Align.INLINE)
d.comment(0x9A6F, 'Above &88: not an immediate op', align=Align.INLINE)
d.comment(0x9A71, 'Out of range high: jump to discard', align=Align.INLINE)
d.comment(0x9A73, 'HALT(&87)/CONTINUE(&88) skip protection', align=Align.INLINE)
d.comment(0x9A75, 'Ctrl >= &87: dispatch without mask check', align=Align.INLINE)
d.comment(0x9A77, 'Convert ctrl byte to 0-based index for mask', align=Align.INLINE)
d.comment(0x9A78, 'SEC for subtract', align=Align.INLINE)
d.comment(0x9A79, 'A = ctrl - &81 (0-based operation index)', align=Align.INLINE)
d.comment(0x9A7B, 'Y = index for mask rotation count', align=Align.INLINE)
d.comment(0x9A7C, 'Load protection mask from LSTAT', align=Align.INLINE)
d.comment(0x9A7F, 'Rotate mask right by control byte index', align=Align.INLINE)
d.comment(0x9A80, 'Decrement rotation counter', align=Align.INLINE)
d.comment(0x9A81, 'Loop until bit aligned', align=Align.INLINE)
d.comment(0x9A83, 'Bit set = operation disabled, discard', align=Align.INLINE)
d.comment(0x9A85, 'Reload ctrl byte for dispatch table', align=Align.INLINE)
d.comment(0x9A88, 'Hi byte: all handlers are in page &9A', align=Align.INLINE)
d.comment(0x9A8A, 'Push hi byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9A8B, 'Load handler low byte from jump table', align=Align.INLINE)
d.comment(0x9A8E, 'Push handler low byte', align=Align.INLINE)
d.comment(0x9A8F, 'RTS dispatches to handler', align=Align.INLINE)
d.comment(0x9A90, 'Increment port buffer length', align=Align.INLINE)
d.comment(0x9A92, 'Check if scout data index reached 11', align=Align.INLINE)
d.comment(0x9A94, 'Yes: loop back to continue reading', align=Align.INLINE)
d.comment(0x9A96, 'Restore A from stack', align=Align.INLINE)
d.comment(0x9A97, 'Transfer to X', align=Align.INLINE)
d.comment(0x9A98, 'Jump to discard handler', align=Align.INLINE)


d.subroutine(0x9B09, 'imm_op_build_reply', title='Build immediate operation reply header', description="""Stores data length, source station/network, and control byte
into the RX buffer header area for port-0 immediate operations.
Then disables SR interrupts and configures the VIA shift
register for shift-in mode before returning to
idle listen.""")
d.comment(0x9B09, 'Get buffer position for reply header', align=Align.INLINE)
d.comment(0x9B0B, 'Clear carry for offset addition', align=Align.INLINE)
d.comment(0x9B0C, 'Data offset = buf_len + &80 (past header)', align=Align.INLINE)
d.comment(0x9B0E, 'Y=&7F: reply data length slot', align=Align.INLINE)
d.comment(0x9B10, 'Store reply data length in RX buffer', align=Align.INLINE)
d.comment(0x9B12, 'Y=&80: source station slot', align=Align.INLINE)
d.comment(0x9B14, 'Load requesting station number', align=Align.INLINE)
d.comment(0x9B17, 'Store source station in reply header', align=Align.INLINE)
d.comment(0x9B1A, 'Load requesting network number', align=Align.INLINE)
d.comment(0x9B1D, 'Store source network in reply header', align=Align.INLINE)
d.comment(0x9B1F, 'Load control byte from received frame', align=Align.INLINE)
d.comment(0x9B22, 'Save ctrl byte for TX response', align=Align.INLINE)
d.comment(0x9B25, 'IER bit 2: disable SR interrupt', align=Align.INLINE)
d.comment(0x9B27, 'Write IER to disable SR', align=Align.INLINE)
d.comment(0x9B2A, 'Read ACR for shift register config', align=Align.INLINE)
d.comment(0x9B2D, 'Isolate shift register mode bits (2-4)', align=Align.INLINE)
d.comment(0x9B2F, 'Save original SR mode for later restore', align=Align.INLINE)
d.comment(0x9B32, 'Reload ACR for modification', align=Align.INLINE)
d.comment(0x9B35, 'Clear SR mode bits (keep other bits)', align=Align.INLINE)
d.comment(0x9B37, 'SR mode 2: shift in under φ2', align=Align.INLINE)
d.comment(0x9B39, 'Apply new shift register mode', align=Align.INLINE)
d.comment(0x9B3C, 'Read SR to clear pending interrupt', align=Align.INLINE)
d.comment(0x9B3F, 'Return to idle listen mode', align=Align.INLINE)
d.comment(0x9EED, 'Unreferenced data block (purpose unknown)')


d.subroutine(0x9EFD, 'tx_calc_transfer', title='Calculate transfer size', description="""Computes the number of bytes actually transferred during a data
frame reception by subtracting RXCB[8..11] (start address) from
RXCB[4..7] (current pointer), giving the byte count.
Two paths: the main path performs a 4-byte subtraction for Tube
transfers, storing results to port_buf_len..open_port_buf_hi
(&A2-&A5). The fallback path (no Tube or buffer addr = &FFFF)
does a 2-byte subtraction using open_port_buf/open_port_buf_hi
(&A4/&A5) as scratch. Both paths clobber &A4/&A5 as a side
effect of the result area overlapping open_port_buf.""", on_exit={'c': '1 if transfer set up, 0 if not', 'x': 'preserved'})
d.comment(0x9EFD, 'Load RXCB[6] (buffer addr byte 2)', align=Align.INLINE)
d.comment(0x9F02, 'AND with TX block[7] (byte 3)', align=Align.INLINE)
d.comment(0x9F04, 'Both &FF = no buffer?', align=Align.INLINE)
d.comment(0x9F06, 'Yes: fallback path', align=Align.INLINE)
d.comment(0x9F08, 'Tube transfer in progress?', align=Align.INLINE)
d.comment(0x9F0B, 'No: fallback path', align=Align.INLINE)
d.comment(0x9F10, 'Set bit 1 (transfer complete)', align=Align.INLINE)
d.comment(0x9F15, 'Init borrow for 4-byte subtract', align=Align.INLINE)
d.comment(0x9F16, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9F17, 'Y=4: start at RXCB offset 4', align=Align.INLINE)
d.comment(0x9F19, 'Load RXCB[Y] (current ptr byte)', align=Align.INLINE)
d.comment(0x9F1B, 'Y += 4: advance to RXCB[Y+4]', align=Align.INLINE)
d.comment(0x9F1F, 'Restore borrow from previous byte', align=Align.INLINE)
d.comment(0x9F20, 'Subtract RXCB[Y+4] (start ptr byte)', align=Align.INLINE)
d.comment(0x9F22, 'Store result byte', align=Align.INLINE)
d.comment(0x9F25, 'Y -= 3: next source byte', align=Align.INLINE)
d.comment(0x9F28, 'Save borrow for next byte', align=Align.INLINE)
d.comment(0x9F29, 'Done all 4 bytes?', align=Align.INLINE)
d.comment(0x9F2B, 'No: next byte pair', align=Align.INLINE)
d.comment(0x9F2D, 'Discard final borrow', align=Align.INLINE)
d.comment(0x9F2E, 'A = saved X', align=Align.INLINE)
d.comment(0x9F2F, 'Save X', align=Align.INLINE)
d.comment(0x9F30, 'Compute address of RXCB+4', align=Align.INLINE)
d.comment(0x9F35, 'X = low byte of RXCB+4', align=Align.INLINE)
d.comment(0x9F36, 'Y = high byte of RXCB ptr', align=Align.INLINE)
d.comment(0x9F38, 'Tube claim type &C2', align=Align.INLINE)
d.comment(0x9F3D, 'No Tube: skip reclaim', align=Align.INLINE)
d.comment(0x9F3F, 'Tube: reclaim with scout status', align=Align.INLINE)
d.comment(0x9F48, 'C=1: Tube address claimed', align=Align.INLINE)
d.comment(0x9F49, 'Restore X', align=Align.INLINE)
d.comment(0x9F4C, 'Y=4: RXCB current pointer offset', align=Align.INLINE)
d.comment(0x9F4E, 'Load RXCB[4] (current ptr lo)', align=Align.INLINE)
d.comment(0x9F50, 'Y=8: RXCB start address offset', align=Align.INLINE)
d.comment(0x9F52, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9F53, 'Subtract RXCB[8] (start ptr lo)', align=Align.INLINE)
d.comment(0x9F55, 'Store transfer size lo', align=Align.INLINE)
d.comment(0x9F57, 'Y=5: current ptr hi offset', align=Align.INLINE)
d.comment(0x9F59, 'Load RXCB[5] (current ptr hi)', align=Align.INLINE)
d.comment(0x9F5B, 'Propagate borrow from lo subtraction', align=Align.INLINE)
d.comment(0x9F5D, 'Temp store adjusted current ptr hi', align=Align.INLINE)
d.comment(0x9F5F, 'Y=8: start address lo offset', align=Align.INLINE)
d.comment(0x9F63, 'Store to scratch (side effect)', align=Align.INLINE)
d.comment(0x9F65, 'Y=9: start address hi offset', align=Align.INLINE)
d.comment(0x9F67, 'Load RXCB[9] (start ptr hi)', align=Align.INLINE)
d.comment(0x9F69, 'Set carry for subtraction', align=Align.INLINE)
d.comment(0x9F6A, 'start_hi - adjusted current_hi', align=Align.INLINE)
d.comment(0x9F6C, 'Store transfer size hi', align=Align.INLINE)
d.comment(0x9F6E, 'Return with C=1', align=Align.INLINE)


d.subroutine(0x9FB2, 'nmi_bootstrap_entry', title='Bootstrap NMI entry point (in ROM)', description="""An alternate NMI handler that lives in the ROM itself rather than
in the RAM workspace at &0D00. Unlike the RAM shim (which uses a
self-modifying JMP to dispatch to different handlers), this one
hardcodes JMP nmi_rx_scout (&96DF). Used as the initial NMI handler
before the workspace has been properly set up during initialisation.
Same sequence as the RAM shim: BIT &FE18 (INTOFF), PHA, TYA, PHA,
LDA romsel, STA &FE30, JMP &96DF.""")
d.comment(0x9FB2, 'INTOFF: disable NMIs while switching ROM', align=Align.INLINE)
d.comment(0x9FB5, 'Save A', align=Align.INLINE)
d.comment(0x9FB6, 'Transfer Y to A', align=Align.INLINE)
d.comment(0x9FB7, 'Save Y (via A)', align=Align.INLINE)
d.comment(0x9FB8, 'ROM bank 0 (patched during init for actual bank)', align=Align.INLINE)
d.comment(0x9FBA, 'Select Econet ROM bank via ROMSEL', align=Align.INLINE)
d.comment(0x9FBD, 'Jump to scout handler in ROM', align=Align.INLINE)


d.subroutine(0x9FC0, 'rom_set_nmi_vector', title='ROM copy of set_nmi_vector + nmi_rti', description="""A version of the NMI vector-setting subroutine and RTI sequence
that lives in ROM. The RAM workspace copy at &0D0E/&0D14 is the
one normally used at runtime; this ROM copy is used during early
initialisation before the RAM workspace has been set up, and as
the source for the initial copy to RAM.""")
d.comment(0x9FC0, 'Store handler high byte at &0D0D', align=Align.INLINE)
d.comment(0x9FC3, 'Store handler low byte at &0D0C', align=Align.INLINE)
d.comment(0x9FC6, 'Restore NFS ROM bank', align=Align.INLINE)
d.comment(0x9FC8, 'Page in via hardware latch', align=Align.INLINE)
d.comment(0x9FCB, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9FCD, 'Restore A from stack', align=Align.INLINE)
d.comment(0x9FCE, 'INTON: re-enable NMIs', align=Align.INLINE)
d.comment(0x9FD1, 'Return from interrupt', align=Align.INLINE)
d.comment(0x9FD2, '&FF padding (unused ROM space)', align=Align.INLINE)


d.subroutine(0x9F70, 'adlc_full_reset', title='ADLC full reset', description='Aborts all activity and returns to idle RX listen mode.', on_exit={'a': '0'})
d.comment(0x9F70, 'CR1=&C1: TX_RESET | RX_RESET | AC (both sections in reset, address control set)', align=Align.INLINE)
d.comment(0x9F75, 'CR4=&1E (via AC=1): 8-bit RX word length, abort extend enabled, NRZ encoding', align=Align.INLINE)
d.comment(0x9F7A, 'CR3=&00 (via AC=1): no loop-back, no AEX, NRZ, no DTR', align=Align.INLINE)


d.subroutine(0x9F7F, 'adlc_rx_listen', title='Enter RX listen mode', description='TX held in reset, RX active with interrupts. Clears all status.', on_exit={'a': '&67'})
d.comment(0x9F7F, 'CR1=&82: TX_RESET | RIE (TX in reset, RX interrupts enabled)', align=Align.INLINE)
d.comment(0x9F81, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9F84, 'CR2=&67: CLR_TX_ST | CLR_RX_ST | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x9F86, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x9F89, 'Return; ADLC now in RX listen mode', align=Align.INLINE)
d.comment(0x9F8D, 'Not initialised: skip to RX listen', align=Align.INLINE)
d.comment(0x9F92, 'Expected: &DF (nmi_rx_scout low)', align=Align.INLINE)
d.comment(0x9F94, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x9F96, 'Read current NMI handler high byte', align=Align.INLINE)
d.comment(0x9F99, 'Expected: &96 (nmi_rx_scout high)', align=Align.INLINE)
d.comment(0x9F9B, 'Not idle: spin and wait', align=Align.INLINE)
d.comment(0x9F9D, 'A=&40: RTI opcode (disable NMI processing)', align=Align.INLINE)
d.comment(0x9F9F, 'Self-modify NMI shim at &0D1C: disable', align=Align.INLINE)


d.subroutine(0x9F8A, 'wait_idle_and_reset', title='Wait for idle NMI state and reset Econet', description="""Called via svc_12_nmi_release (&06D4). Checks if Econet has been
initialised; if not, skips to adlc_rx_listen. If initialised,
spins until the NMI handler is idle (pointing at nmi_rx_scout),
then falls through to save_econet_state to clear flags and
re-enter RX listen mode.""")


d.subroutine(0x96DF, 'nmi_rx_scout', title='NMI RX scout handler (initial byte)', description="""Default NMI handler for incoming scout frames. Checks if the frame
is addressed to us or is a broadcast. Installed as the NMI target
during idle RX listen mode.
Tests SR2 bit0 (AP = Address Present) to detect incoming data.
Reads the first byte (destination station) from the RX FIFO and
compares against our station ID. Reading &FE18 also disables NMIs
(INTOFF side effect).""")
d.comment(0x96DF, 'A=&01: mask for SR2 bit0 (AP = Address Present)', align=Align.INLINE)
d.comment(0x96E1, 'BIT SR2: Z = A AND SR2 -- tests if AP is set', align=Align.INLINE)
d.comment(0x96E4, 'AP not set, no incoming data -- check for errors', align=Align.INLINE)
d.comment(0x96E6, 'Read first RX byte (destination station address)', align=Align.INLINE)
d.comment(0x96E9, 'Compare to our station ID (&FE18 read = INTOFF, disables NMIs)', align=Align.INLINE)
d.comment(0x96EC, 'Match -- accept frame', align=Align.INLINE)
d.comment(0x96EE, 'Check for broadcast address (&FF)', align=Align.INLINE)
d.comment(0x96F0, 'Neither our address nor broadcast -- reject frame', align=Align.INLINE)
d.comment(0x96F2, 'Flag &40 = broadcast frame', align=Align.INLINE)


d.subroutine(0x96FC, 'nmi_rx_scout_net', title='RX scout second byte handler', description="""Reads the second byte of an incoming scout (destination network).
Checks for network match: 0 = local network (accept), &FF = broadcast
(accept and flag), anything else = reject.
Installs the scout data reading loop handler at &972E.""")
d.comment(0x96FC, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x96FF, 'No RDA -- check errors', align=Align.INLINE)
d.comment(0x9701, 'Read destination network byte', align=Align.INLINE)
d.comment(0x9704, 'Network = 0 -- local network, accept', align=Align.INLINE)
d.comment(0x9706, 'EOR &FF: test if network = &FF (broadcast)', align=Align.INLINE)
d.comment(0x9708, 'Broadcast network -- accept', align=Align.INLINE)
d.comment(0x970A, 'Reject: wrong network. CR1=&A2: RIE|RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x9715, 'Store Y offset for scout data buffer', align=Align.INLINE)


d.subroutine(0x971E, 'scout_error', title='Scout error/discard handler', description="""Reached when the scout data loop sees no RDA (BPL at &9733) or
when scout completion finds unexpected SR2 state.
If SR2 & &81 is non-zero (AP or RDA still active), performs full
ADLC reset and discards. If zero (clean end), discards via &9A0A.
This path is a common landing for any unexpected ADLC state during
scout reception.""")
d.comment(0x971E, 'Read SR2', align=Align.INLINE)
d.comment(0x9721, 'Test AP (b0) | RDA (b7)', align=Align.INLINE)
d.comment(0x9725, 'Unexpected data/status: full ADLC reset', align=Align.INLINE)
d.comment(0x9728, 'Discard and return to idle', align=Align.INLINE)


d.subroutine(0x972E, 'scout_data_loop', title='Scout data reading loop', description="""Reads the body of a scout frame, two bytes per iteration. Stores
bytes at &0D3D+Y (scout buffer: src_stn, src_net, ctrl, port, ...).
Between each pair it checks SR2:
  - At entry (&9730): SR2 read, BPL tests RDA (bit7)
    - No RDA (BPL) -> error (&971E)
    - RDA set (BMI) -> read byte
  - After first byte (&973C): full SR2 tested
    - SR2 non-zero (BNE) -> scout completion (&9758)
      This is the FV detection point: when FV is set (by inline refill
      of the last byte during the preceding RX FIFO read), SR2 is
      non-zero and the branch is taken.
    - SR2 = 0 -> read second byte and loop
  - After second byte (&9750): re-test full SR2
    - SR2 non-zero (BNE) -> loop back to &9733
    - SR2 = 0 -> RTI, wait for next NMI
The loop ends at Y=&0C (12 bytes max in scout buffer).""")
d.comment(0x972E, 'Y = buffer offset', align=Align.INLINE)
d.comment(0x9730, 'Read SR2', align=Align.INLINE)
d.comment(0x9735, 'Read data byte from RX FIFO', align=Align.INLINE)
d.comment(0x9738, 'Store at &0D3D+Y (scout buffer)', align=Align.INLINE)
d.comment(0x973B, 'Advance buffer index', align=Align.INLINE)
d.comment(0x973C, 'Read SR2 again (FV detection point)', align=Align.INLINE)
d.comment(0x973F, 'RDA set -- more data, read second byte', align=Align.INLINE)
d.comment(0x9741, 'SR2 non-zero (FV or other) -- scout completion', align=Align.INLINE)
d.comment(0x9743, 'Read second byte of pair', align=Align.INLINE)
d.comment(0x9746, 'Store at &0D3D+Y', align=Align.INLINE)
d.comment(0x9749, 'Advance and check buffer limit', align=Align.INLINE)
d.comment(0x974C, 'Buffer full (Y=12) -- force completion', align=Align.INLINE)
d.comment(0x9750, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x9753, 'SR2 non-zero -- loop back for more bytes', align=Align.INLINE)
d.comment(0x9755, 'SR2 = 0 -- RTI, wait for next NMI', align=Align.INLINE)


d.subroutine(0x9758, 'scout_complete', title='Scout completion handler', description="""Reached from the scout data loop when SR2 is non-zero (FV detected).
Disables PSE to allow individual SR2 bit testing:
  CR1=&00 (clear all enables)
  CR2=&84 (RDA_SUPPRESS_FV | FC_TDRA) -- no PSE, no CLR bits
Then checks FV (bit1) and RDA (bit7):
  - No FV (BEQ) -> error &971E (not a valid frame end)
  - FV set, no RDA (BPL) -> error &971E (missing last byte)
  - FV set, RDA set -> read last byte, process scout
After reading the last byte, the complete scout buffer (&0D3D-&0D48)
contains: src_stn, src_net, ctrl, port [, extra_data...].
The port byte at &0D40 determines further processing:
  - Port = 0 -> immediate operation (&9A46)
  - Port non-zero -> check if it matches an open receive block""")
d.comment(0x9758, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x975D, 'CR2=&84: disable PSE, enable RDA_SUPPRESS_FV', align=Align.INLINE)
d.comment(0x9762, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9764, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x9767, 'No FV -- not a valid frame end, error', align=Align.INLINE)
d.comment(0x9769, 'FV set but no RDA -- missing last byte, error', align=Align.INLINE)
d.comment(0x976B, 'Read last byte from RX FIFO', align=Align.INLINE)
d.comment(0x976E, 'Store last byte at &0D3D+Y', align=Align.INLINE)
d.comment(0x9771, 'CR1=&44: RX_RESET | TIE (switch to TX for ACK)', align=Align.INLINE)
d.comment(0x9779, 'Check port byte: 0 = immediate op, non-zero = data transfer', align=Align.INLINE)
d.comment(0x977C, 'Port non-zero -- look for matching receive block', align=Align.INLINE)
d.comment(0x977E, 'Port = 0 -- immediate operation handler', align=Align.INLINE)
d.comment(0x9776, 'Set bit7 of need_release_tube flag', align=Align.INLINE)
d.comment(0x9781, 'Check if broadcast (bit6 of tx_flags)', align=Align.INLINE)
d.comment(0x9786, 'CR2=&07: broadcast prep', align=Align.INLINE)
d.comment(0x978B, 'Check if RX port list active (bit7)', align=Align.INLINE)
d.comment(0x978E, 'No active ports -- try NFS workspace', align=Align.INLINE)
d.comment(0x9790, 'Start scanning port list at page &C0', align=Align.INLINE)
d.comment(0x979A, 'Read port control byte from slot', align=Align.INLINE)
d.comment(0x979C, 'Zero = end of port list, no match', align=Align.INLINE)
d.comment(0x979E, '&7F = any-port wildcard', align=Align.INLINE)
d.comment(0x97A7, 'Check if port matches this slot', align=Align.INLINE)
d.comment(0x97B1, 'Check if source station matches', align=Align.INLINE)
d.comment(0x97B9, 'Check if source network matches', align=Align.INLINE)
d.comment(0x97C5, 'Advance to next 12-byte port slot', align=Align.INLINE)
d.comment(0x97CE, 'Try NFS workspace if paged list exhausted', align=Align.INLINE)
d.comment(0x97D5, 'NFS workspace high byte for port list', align=Align.INLINE)
d.comment(0x97D9, 'Match found: set scout_status = 3', align=Align.INLINE)
d.comment(0x97DE, 'Calculate transfer parameters', align=Align.INLINE)
d.comment(0x97EB, 'CR1=&44: RX_RESET | TIE', align=Align.INLINE)
d.comment(0x97F0, 'CR2=&A7: RTS | CLR_TX_ST | FC_TDRA | PSE', align=Align.INLINE)
d.comment(0x97F5, 'Install data_rx_setup at &97FC', align=Align.INLINE)
d.comment(0x975A, 'Write CR1', align=Align.INLINE)
d.comment(0x975F, 'Write CR2', align=Align.INLINE)
d.comment(0x9773, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x9777, 'Rotate C=1 into bit7: mark Tube release needed', align=Align.INLINE)
d.comment(0x9784, 'Not broadcast -- skip CR2 setup', align=Align.INLINE)
d.comment(0x9788, 'Write CR2: broadcast frame prep', align=Align.INLINE)
d.comment(0x9792, 'Y=0: start offset within each port slot', align=Align.INLINE)
d.comment(0x9794, 'Store page to workspace pointer low', align=Align.INLINE)
d.comment(0x9796, 'Store page high byte for slot scanning', align=Align.INLINE)
d.comment(0x9798, 'Y=0: read control byte from start of slot', align=Align.INLINE)
d.comment(0x97A0, 'Not wildcard -- check specific port match', align=Align.INLINE)
d.comment(0x97A3, 'Read port number from slot (offset 1)', align=Align.INLINE)
d.comment(0x97A5, 'Zero port in slot = match any port', align=Align.INLINE)
d.comment(0x97AA, 'Port mismatch -- try next slot', align=Align.INLINE)
d.comment(0x97AC, 'Y=2: advance to station byte', align=Align.INLINE)
d.comment(0x97AD, 'Read station filter from slot (offset 2)', align=Align.INLINE)
d.comment(0x97AF, 'Zero station = match any station, accept', align=Align.INLINE)
d.comment(0x97B4, 'Station mismatch -- try next slot', align=Align.INLINE)
d.comment(0x97B6, 'Y=3: advance to network byte', align=Align.INLINE)
d.comment(0x97B7, 'Read network filter from slot (offset 3)', align=Align.INLINE)
d.comment(0x97BC, 'Network matches or zero = accept', align=Align.INLINE)
d.comment(0x97BE, 'Check if NFS workspace search pending', align=Align.INLINE)
d.comment(0x97C0, 'No NFS workspace -- try fallback path', align=Align.INLINE)
d.comment(0x97C2, 'Load current slot base address', align=Align.INLINE)
d.comment(0x97C4, 'CLC for 12-byte slot advance', align=Align.INLINE)
d.comment(0x97C7, 'Update workspace pointer to next slot', align=Align.INLINE)
d.comment(0x97C9, "Always branches (page &C0 won't overflow)", align=Align.INLINE)
d.comment(0x97CB, 'No match found -- discard frame', align=Align.INLINE)
d.comment(0x97D1, 'No NFS workspace RX (bit6 clear) -- discard', align=Align.INLINE)
d.comment(0x97D3, 'NFS workspace starts at offset 0 in page', align=Align.INLINE)
d.comment(0x97D7, 'Scan NFS workspace port list', align=Align.INLINE)
d.comment(0x97DB, 'Record match for completion handler', align=Align.INLINE)
d.comment(0x97E1, 'C=0: no Tube claimed -- discard', align=Align.INLINE)
d.comment(0x97E3, 'Check broadcast flag for ACK path', align=Align.INLINE)
d.comment(0x97E6, 'Not broadcast -- normal ACK path', align=Align.INLINE)
d.comment(0x97E8, 'Broadcast: different completion path', align=Align.INLINE)
d.comment(0x97ED, 'Write CR1: TX mode for ACK', align=Align.INLINE)
d.comment(0x97F2, 'Write CR2: enable TX with PSE', align=Align.INLINE)
d.comment(0x97F7, 'High byte of data_rx_setup handler', align=Align.INLINE)
d.comment(0x97F9, 'Send ACK with data_rx_setup as next NMI', align=Align.INLINE)
d.comment(0x97FE, 'Write CR1: switch to RX for data frame', align=Align.INLINE)
d.comment(0x9805, 'Install nmi_data_rx and return from NMI', align=Align.INLINE)


d.subroutine(0x983D, 'install_data_rx_handler', title='Install data RX bulk or Tube handler', description="""Selects either the normal bulk RX handler (&9865) or the Tube
RX handler (&98C2) based on the Tube transfer flag in tx_flags,
and installs the appropriate NMI handler.""")


d.subroutine(0x9857, 'nmi_error_dispatch', title='NMI error handler dispatch', description="""Common error/abort entry used by 12 call sites. Checks
tx_flags bit 7: if clear, does a full ADLC reset and returns
to idle listen (RX error path); if set, jumps to tx_result_fail
(TX not-listening path).""")


d.subroutine(0x9808, 'nmi_data_rx', title='Data frame RX handler (four-way handshake)', description="""Receives the data frame after the scout ACK has been sent.
First checks AP (Address Present) for the start of the data frame.
Reads and validates the first two address bytes (dest_stn, dest_net)
against our station address, then installs continuation handlers
to read the remaining data payload into the open port buffer.

Handler chain: &9808 (AP+addr check) -> &981C (net=0 check) ->
&9832 (skip ctrl+port) -> &9865 (bulk data read) -> &9899 (completion)""")
d.comment(0x97FC, 'CR1=&82: TX_RESET | RIE (switch to RX for data frame)', align=Align.INLINE)
d.comment(0x9801, 'Install nmi_data_rx at &9808', align=Align.INLINE)
d.comment(0x9803, 'Y=&98: NMI handler high byte', align=Align.INLINE)
d.comment(0x9808, 'A=&01: mask for AP (Address Present)', align=Align.INLINE)
d.comment(0x980A, 'BIT SR2: test AP bit', align=Align.INLINE)
d.comment(0x980D, 'No AP: wrong frame or error', align=Align.INLINE)
d.comment(0x980F, 'Read first byte (dest station)', align=Align.INLINE)
d.comment(0x9812, 'Compare to our station ID (INTOFF)', align=Align.INLINE)
d.comment(0x9815, 'Not for us: error path', align=Align.INLINE)
d.comment(0x9817, 'Install net check handler at &981C', align=Align.INLINE)
d.comment(0x9819, 'Set NMI vector via RAM shim', align=Align.INLINE)
d.comment(0x981C, 'Validate source network = 0', align=Align.INLINE)
d.comment(0x981F, 'SR2 bit7 clear: no data ready -- error', align=Align.INLINE)
d.comment(0x9821, 'Read dest network byte', align=Align.INLINE)
d.comment(0x9824, 'Network != 0: wrong network -- error', align=Align.INLINE)
d.comment(0x9826, 'Install skip handler at &9832', align=Align.INLINE)
d.comment(0x9828, 'High byte of &9832 handler', align=Align.INLINE)
d.comment(0x982A, 'SR1 bit7: IRQ, data already waiting', align=Align.INLINE)
d.comment(0x982D, 'Data ready: skip directly, no RTI', align=Align.INLINE)
d.comment(0x982F, 'Install handler and return via RTI', align=Align.INLINE)
d.comment(0x9832, 'Skip control and port bytes (already known from scout)', align=Align.INLINE)
d.comment(0x9835, 'SR2 bit7 clear: error', align=Align.INLINE)
d.comment(0x9837, 'Discard control byte', align=Align.INLINE)
d.comment(0x983A, 'Discard port byte', align=Align.INLINE)
d.comment(0x983D, 'A=2: Tube transfer flag mask', align=Align.INLINE)
d.comment(0x983F, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x9842, 'Tube active: use Tube RX path', align=Align.INLINE)
d.comment(0x9844, 'Install bulk read at &9865', align=Align.INLINE)
d.comment(0x9846, 'High byte of &9865 handler', align=Align.INLINE)
d.comment(0x9848, 'SR1 bit7: more data already waiting?', align=Align.INLINE)
d.comment(0x984B, 'Yes: enter bulk read directly', align=Align.INLINE)
d.comment(0x984D, 'No: install handler and RTI', align=Align.INLINE)
d.comment(0x9850, 'Tube: install Tube RX at &98C2', align=Align.INLINE)
d.comment(0x9852, 'High byte of &98C2 handler', align=Align.INLINE)
d.comment(0x9854, 'Install Tube handler and RTI', align=Align.INLINE)
d.comment(0x9857, 'Check tx_flags for error path', align=Align.INLINE)
d.comment(0x985A, 'Bit7 clear: RX error path', align=Align.INLINE)
d.comment(0x985C, 'Bit7 set: TX result = not listening', align=Align.INLINE)
d.comment(0x985F, 'Full ADLC reset on RX error', align=Align.INLINE)
d.comment(0x9862, 'Discard and return to idle listen', align=Align.INLINE)


d.subroutine(0x9865, 'nmi_data_rx_bulk', title='Data frame bulk read loop', description="""Reads data payload bytes from the RX FIFO and stores them into
the open port buffer at (open_port_buf),Y. Reads bytes in pairs
(like the scout data loop), checking SR2 between each pair.
SR2 non-zero (FV or other) -> frame completion at &9899.
SR2 = 0 -> RTI, wait for next NMI to continue.""")
d.comment(0x9865, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x9867, 'Read SR2 for next pair', align=Align.INLINE)
d.comment(0x986A, 'SR2 bit7 clear: frame complete (FV)', align=Align.INLINE)
d.comment(0x986C, 'Read first byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x986F, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x9871, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9872, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x9874, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x9876, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x9878, 'No pages left: handle as complete', align=Align.INLINE)
d.comment(0x987A, 'Read SR2 between byte pairs', align=Align.INLINE)
d.comment(0x987D, 'SR2 bit7 set: more data available', align=Align.INLINE)
d.comment(0x987F, 'SR2 non-zero, bit7 clear: frame done', align=Align.INLINE)
d.comment(0x9881, 'Read second byte of pair from RX FIFO', align=Align.INLINE)
d.comment(0x9884, 'Store byte to buffer', align=Align.INLINE)
d.comment(0x9886, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9887, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x9889, 'Y != 0: no page boundary crossing', align=Align.INLINE)
d.comment(0x988B, 'Crossed page: increment buffer high byte', align=Align.INLINE)
d.comment(0x988D, 'Decrement remaining page count', align=Align.INLINE)
d.comment(0x988F, 'No pages left: frame complete', align=Align.INLINE)
d.comment(0x9891, 'Read SR2 for next iteration', align=Align.INLINE)
d.comment(0x9894, 'SR2 non-zero: more data, loop back', align=Align.INLINE)
d.comment(0x9896, 'SR2=0: no more data yet, wait for NMI', align=Align.INLINE)


d.subroutine(0x9899, 'data_rx_complete', title='Data frame completion', description="""Reached when SR2 non-zero during data RX (FV detected).
Same pattern as scout completion (&9758): disables PSE (CR2=&84,
CR1=&00), then tests FV and RDA. If FV+RDA, reads the last byte.
If extra data available and buffer space remains, stores it.
Proceeds to send the final ACK via &9910.""")
d.comment(0x98A5, 'A=&02: FV mask', align=Align.INLINE)
d.comment(0x98A7, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x98AA, 'No FV -- error', align=Align.INLINE)
d.comment(0x98AC, 'FV set, no RDA -- proceed to ACK', align=Align.INLINE)
d.comment(0x98B2, 'FV+RDA: read and store last data byte', align=Align.INLINE)
d.comment(0x989B, 'Write CR2', align=Align.INLINE)
d.comment(0x98A0, 'Write CR1', align=Align.INLINE)
d.comment(0x98A3, 'Save Y (byte count from data RX loop)', align=Align.INLINE)
d.comment(0x98AE, 'Check if buffer space remains', align=Align.INLINE)
d.comment(0x98B0, 'No buffer space: error/discard frame', align=Align.INLINE)
d.comment(0x98B5, 'Y = current buffer write offset', align=Align.INLINE)
d.comment(0x98B7, 'Store last byte in port receive buffer', align=Align.INLINE)
d.comment(0x98B9, 'Advance buffer write offset', align=Align.INLINE)
d.comment(0x98BB, 'No page wrap: proceed to send ACK', align=Align.INLINE)
d.comment(0x98BD, 'Page boundary: advance buffer page', align=Align.INLINE)
d.comment(0x98BF, 'Send ACK frame to complete handshake', align=Align.INLINE)
d.comment(0x98C2, 'Read SR2 for Tube data receive path', align=Align.INLINE)
d.comment(0x98C5, 'RDA clear: no more data, frame complete', align=Align.INLINE)
d.comment(0x98C7, 'Read data byte from ADLC RX FIFO', align=Align.INLINE)
d.comment(0x98CA, 'Check buffer limits and transfer size', align=Align.INLINE)
d.comment(0x98CD, 'Zero: buffer full, handle as error', align=Align.INLINE)
d.comment(0x98CF, 'Send byte to Tube data register 3', align=Align.INLINE)
d.comment(0x98D2, 'Read second data byte (paired transfer)', align=Align.INLINE)
d.comment(0x98D5, 'Send second byte to Tube', align=Align.INLINE)
d.comment(0x98D8, 'Check limits after byte pair', align=Align.INLINE)
d.comment(0x98DB, 'Zero: Tube transfer complete', align=Align.INLINE)
d.comment(0x98DD, 'Re-read SR2 for next byte pair', align=Align.INLINE)
d.comment(0x98E0, 'More data available: continue loop', align=Align.INLINE)
d.comment(0x98E2, 'Unexpected end: return from NMI', align=Align.INLINE)
d.comment(0x98E5, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x98E7, 'Write CR1 for individual bit testing', align=Align.INLINE)
d.comment(0x98EA, 'CR2=&84: disable PSE', align=Align.INLINE)
d.comment(0x98EC, 'Write CR2: same pattern as main path', align=Align.INLINE)
d.comment(0x98EF, 'A=&02: FV mask for Tube completion', align=Align.INLINE)
d.comment(0x98F1, 'BIT SR2: test FV (Z) and RDA (N)', align=Align.INLINE)
d.comment(0x98F4, 'No FV: incomplete frame, error', align=Align.INLINE)
d.comment(0x98F6, 'FV set, no RDA: proceed to ACK', align=Align.INLINE)
d.comment(0x98F8, 'Check if any buffer was allocated', align=Align.INLINE)
d.comment(0x98FA, 'OR all 4 buffer pointer bytes together', align=Align.INLINE)
d.comment(0x98FC, 'Check buffer low byte', align=Align.INLINE)
d.comment(0x98FE, 'Check buffer high byte', align=Align.INLINE)
d.comment(0x9900, 'All zero (null buffer): error', align=Align.INLINE)
d.comment(0x9902, 'Read extra trailing byte from FIFO', align=Align.INLINE)
d.comment(0x9905, 'Save extra byte at &0D5D for later use', align=Align.INLINE)
d.comment(0x9908, 'Bit5 = extra data byte available flag', align=Align.INLINE)
d.comment(0x990A, 'Set extra byte flag in tx_flags', align=Align.INLINE)
d.comment(0x990D, 'Store updated flags', align=Align.INLINE)


d.subroutine(0x9910, 'ack_tx', title='ACK transmission', description="""Sends a scout ACK or final ACK frame as part of the four-way handshake.
If bit7 of &0D4A is set, this is a final ACK -> completion (&9EDB).
Otherwise, configures for TX (CR1=&44, CR2=&A7) and sends the ACK
frame (dst_stn, dst_net from &0D3D, src_stn from &FE18, src_net=0).
The ACK frame has no data payload -- just address bytes.

After writing the address bytes to the TX FIFO, installs the next
NMI handler from &0D4B/&0D4C (saved by the scout/data RX handler)
and sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x9910, 'Load TX flags to check ACK type', align=Align.INLINE)
d.comment(0x9913, 'Bit7 clear: normal scout ACK', align=Align.INLINE)
d.comment(0x9915, 'Final ACK: call completion handler', align=Align.INLINE)
d.comment(0x9918, 'Jump to TX success result', align=Align.INLINE)
d.comment(0x991B, 'CR1=&44: RX_RESET | TIE (switch to TX mode)', align=Align.INLINE)
d.comment(0x991D, 'Write CR1: switch to TX mode', align=Align.INLINE)
d.comment(0x9920, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9922, 'Write CR2: enable TX with status clear', align=Align.INLINE)
d.comment(0x9927, 'High byte of post-ACK handler', align=Align.INLINE)
d.comment(0x9929, 'Store next handler low byte', align=Align.INLINE)
d.comment(0x992C, 'Store next handler high byte', align=Align.INLINE)
d.comment(0x992F, 'Load dest station from RX scout buffer', align=Align.INLINE)
d.comment(0x9932, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9935, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9937, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x993A, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x993D, 'Write dest net byte to FIFO', align=Align.INLINE)
d.comment(0x9942, 'High byte of nmi_ack_tx_src', align=Align.INLINE)
d.comment(0x9944, 'Set NMI vector to ack_tx_src handler', align=Align.INLINE)


d.subroutine(0x9947, 'nmi_ack_tx_src', title='ACK TX continuation', description="""Writes source station and network to TX FIFO, completing the 4-byte
ACK frame. Then sends TX_LAST_DATA (CR2=&3F) to close the frame.""")
d.comment(0x9947, 'Load our station ID (also INTOFF)', align=Align.INLINE)
d.comment(0x994A, 'BIT SR1: test TDRA', align=Align.INLINE)
d.comment(0x994D, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x994F, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x9952, 'Write network=0 to TX FIFO', align=Align.INLINE)
d.comment(0x9961, 'Install saved handler from &0D4B/&0D4C', align=Align.INLINE)


d.subroutine(0x9B90, 'tx_begin', title='Begin TX operation', description="""Main TX initiation entry point (called via trampoline at &06CE).
Copies dest station/network from the TXCB to the scout buffer,
dispatches to immediate op setup (ctrl >= &81) or normal data
transfer, calculates transfer sizes, copies extra parameters,
then enters the INACTIVE polling loop.""")


d.subroutine(0x9C06, 'intoff_test_inactive', title='Disable NMIs and test INACTIVE', description="""Mid-instruction label within the INACTIVE polling loop. The
address &9BE2 is referenced as a constant for self-modifying
code. Disables NMIs twice (belt-and-braces) then tests SR2
for INACTIVE before proceeding with TX.""")


d.subroutine(0x9BF8, 'inactive_poll', title='INACTIVE polling loop', description="""Polls SR2 for INACTIVE (bit2) to confirm the network line is idle before
attempting transmission. Uses a 3-byte timeout counter on the stack.
The timeout (~256^3 iterations) generates "Line Jammed" if INACTIVE
never appears.
The CTS check at &9C18-&9C1D works because CR2=&67 has RTS=0, so
cts_input_ is always true, and SR1_CTS reflects presence of clock hardware.""")
d.comment(0x9BFD, 'Y=&E7: CR2 value for TX prep (RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9BFF, 'A=&04: INACTIVE mask for SR2 bit2', align=Align.INLINE)
d.comment(0x9C06, 'INTOFF -- disable NMIs', align=Align.INLINE)
d.comment(0x9C08, 'INTOFF again (belt-and-braces)', align=Align.INLINE)
d.comment(0x9C09, 'A=4: INACTIVE mask for SR2 bit 2', align=Align.INLINE)
d.comment(0x9C0B, 'BIT SR2: Z = &04 AND SR2 -- tests INACTIVE', align=Align.INLINE)
d.comment(0x9C0E, 'INACTIVE not set -- re-enable NMIs and loop', align=Align.INLINE)
d.comment(0x9C10, 'Read SR1 (acknowledge pending interrupt)', align=Align.INLINE)
d.comment(0x9C13, 'CR2=&67: CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE', align=Align.INLINE)
d.comment(0x9C18, 'A=&10: CTS mask for SR1 bit4', align=Align.INLINE)
d.comment(0x9C1A, 'BIT SR1: tests CTS present', align=Align.INLINE)
d.comment(0x9C1D, 'CTS set -- clock hardware detected, start TX', align=Align.INLINE)
d.comment(0x9C1F, 'A=&2C: BIT opcode (re-enable NMI processing)', align=Align.INLINE)
d.comment(0x9C21, 'Self-modify NMI shim at &0D1C: enable', align=Align.INLINE)
d.comment(0x9C24, 'INTON -- re-enable NMIs (&FE20 read)', align=Align.INLINE)
d.comment(0x9C28, '3-byte timeout counter on stack', align=Align.INLINE)
d.comment(0x9C3A, 'TX_ACTIVE branch (A=&44 = CR1 value for TX active)')


d.subroutine(0x9C3E, 'tx_line_jammed', title='TX timeout error handler (Line Jammed)', description="""Writes CR2=&07 to abort TX, cleans 3 bytes from stack (the
timeout loop's state), then stores error code &40 ("Line
Jammed") into the TX control block and signals completion.""")
d.comment(0x9C3E, 'CR2=&07: FC_TDRA | 2_1_BYTE | PSE (abort TX)', align=Align.INLINE)
d.comment(0x9C40, 'Write CR2 to abort TX', align=Align.INLINE)
d.comment(0x9C43, 'Clean 3 bytes of timeout loop state', align=Align.INLINE)
d.comment(0x9C46, "Error &40 = 'Line Jammed'", align=Align.INLINE)
d.comment(0x9C48, 'ALWAYS branch to shared error handler', align=Align.INLINE)
d.comment(0x9C4A, "Error &43 = 'No Clock'", align=Align.INLINE)
d.comment(0x9C4C, 'Offset 0 = error byte in TX control block', align=Align.INLINE)
d.comment(0x9C4E, 'Store error code in TX CB byte 0', align=Align.INLINE)
d.comment(0x9C50, '&80 = TX complete flag', align=Align.INLINE)
d.comment(0x9C52, 'Signal TX operation complete', align=Align.INLINE)
d.comment(0x9C55, 'Restore X saved by caller', align=Align.INLINE)
d.comment(0x9C56, 'Move to X register', align=Align.INLINE)
d.comment(0x9C57, 'Return to TX caller', align=Align.INLINE)
d.comment(0x9C58, 'X=&C0: CR1 = AC | RX_RESET', align=Align.INLINE)
d.comment(0x9C5A, 'Write CR1: reset RX before TX (new in 3.65)', align=Align.INLINE)


d.subroutine(0x9C5D, 'tx_prepare', title='TX preparation', description="""Configures ADLC for transmission: asserts RTS via CR2, enables TIE via CR1,
installs NMI TX handler at &9CFF (nmi_tx_data), and re-enables NMIs.
For port-0 (immediate) operations, dispatches via a lookup table indexed
by control byte to set tx_flags, tx_length, and a per-operation handler.
For port non-zero, branches to c9c8e for standard data transfer setup.""")
d.comment(0x9C5D, 'Write CR2 = Y (&E7: RTS|CLR_TX_ST|CLR_RX_ST|FC_TDRA|2_1_BYTE|PSE)', align=Align.INLINE)
d.comment(0x9C60, 'CR1=&44: RX_RESET | TIE (TX active, TX interrupts enabled)', align=Align.INLINE)
d.comment(0x9C62, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9C67, 'High byte of NMI handler address', align=Align.INLINE)
d.comment(0x9C69, 'Write NMI vector low byte directly', align=Align.INLINE)
d.comment(0x9C6C, 'Write NMI vector high byte directly', align=Align.INLINE)
d.comment(0x9C6F, 'Set need_release_tube flag (SEC/ROR = bit7)', align=Align.INLINE)
d.comment(0x9C70, 'Rotate carry into bit 7 of flag', align=Align.INLINE)
d.comment(0x9C72, 'A=&2C: BIT opcode (re-enable NMI processing)', align=Align.INLINE)
d.comment(0x9C74, 'Self-modify NMI shim at &0D1C: enable', align=Align.INLINE)
d.comment(0x9C77, 'INTON -- NMIs now fire for TDRA (&FE20 read)', align=Align.INLINE)
d.comment(0x9C7A, 'Load destination port number', align=Align.INLINE)
d.comment(0x9C7D, 'Port != 0: standard data transfer', align=Align.INLINE)
d.comment(0x9C7F, 'Port 0: load control byte for table lookup', align=Align.INLINE)
d.comment(0x9C82, 'Look up tx_flags from table', align=Align.INLINE)
d.comment(0x9C85, 'Store operation flags', align=Align.INLINE)
d.comment(0x9C88, 'Look up tx_length from table', align=Align.INLINE)
d.comment(0x9C8B, 'Store expected transfer length', align=Align.INLINE)
d.comment(0x9C8E, 'Push high byte of return address (&9C)', align=Align.INLINE)
d.comment(0x9C90, 'Push high byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9C91, 'Look up handler address low from table', align=Align.INLINE)
d.comment(0x9C94, 'Push low byte for PHA/PHA/RTS dispatch', align=Align.INLINE)
d.comment(0x9C95, 'RTS dispatches to control-byte handler', align=Align.INLINE)
d.comment(0x9C96, 'Control byte → CR2 value lookup table', align=Align.INLINE)


d.subroutine(0x9CFF, 'nmi_tx_data', title='NMI TX data handler', description="""Writes 2 bytes per NMI invocation to the TX FIFO at &FEA2. Uses the
BIT instruction on SR1 to test TDRA (V flag = bit6) and IRQ (N flag = bit7).
After writing 2 bytes, checks if the frame is complete. If more data,
tests SR1 bit7 (IRQ) via BMI -- if IRQ still asserted, writes 2 more bytes
without returning from NMI (tight loop). Otherwise returns via RTI.""")
d.comment(0x9CFF, 'Load TX buffer index', align=Align.INLINE)
d.comment(0x9D02, 'BIT SR1: V=bit6(TDRA), N=bit7(IRQ)', align=Align.INLINE)
d.comment(0x9D05, 'TDRA not set -- TX error', align=Align.INLINE)
d.comment(0x9D07, 'Load byte from TX buffer', align=Align.INLINE)
d.comment(0x9D0A, 'Write to TX_DATA (continue frame)', align=Align.INLINE)
d.comment(0x9D15, 'Write second byte to TX_DATA', align=Align.INLINE)
d.comment(0x9D18, 'Compare index to TX length', align=Align.INLINE)
d.comment(0x9D1B, 'Frame complete -- go to TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9D1D, 'Check if we can send another pair', align=Align.INLINE)
d.comment(0x9D20, 'IRQ set -- send 2 more bytes (tight loop)', align=Align.INLINE)
d.comment(0x9D22, 'RTI -- wait for next NMI', align=Align.INLINE)
d.comment(0x9D25, 'TX error path')
d.comment(0x9D25, 'Error &42', align=Align.INLINE)
d.comment(0x9D29, 'CR2=&67: clear status, return to listen', align=Align.INLINE)
d.comment(0x9D2E, 'Error &41 (TDRA not ready)', align=Align.INLINE)
d.comment(0x9D30, 'INTOFF (also loads station ID)', align=Align.INLINE)
d.comment(0x9D33, 'PHA/PLA delay loop (256 iterations for NMI disable)', align=Align.INLINE)


d.subroutine(0x9D3B, 'tx_last_data', title='TX_LAST_DATA and frame completion', description="""Signals end of TX frame by writing CR2=&3F (TX_LAST_DATA). Then installs
the TX completion NMI handler at &9D47 (nmi_tx_complete).
CR2=&3F = 0011_1111:
  bit5: CLR_RX_ST -- clears fv_stored_ (prepares for RX of reply)
  bit4: TX_LAST_DATA -- tells ADLC this is the final data byte
  bit3: FLAG_IDLE -- send flags/idle after frame
  bit2: FC_TDRA -- force clear TDRA
  bit1: 2_1_BYTE -- two-byte transfer mode
  bit0: PSE -- prioritised status enable
Note: NO CLR_TX_ST (bit6=0), NO RTS (bit7=0 -- drops RTS after frame)""")
d.comment(0x9D3B, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)
d.comment(0x9D3D, 'Write to ADLC CR2', align=Align.INLINE)
d.comment(0x9D42, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9D44, 'Install and return via set_nmi_vector', align=Align.INLINE)


d.subroutine(0x9D47, 'nmi_tx_complete', title='TX completion: switch to RX mode', description="""Called via NMI after the frame (including CRC and closing flag) has been
fully transmitted. Switches from TX mode to RX mode by writing CR1=&82.
CR1=&82 = 1000_0010: TX_RESET | RIE (listen for reply).
Checks workspace flags to decide next action:
  - bit6 set at &0D4A -> tx_result_ok at &9EDB
  - bit0 set at &0D4A -> handshake_await_ack at &9E83
  - Otherwise -> install nmi_reply_scout at &9D63""")
d.comment(0x9D47, 'CR1=&82: TX_RESET | RIE (now in RX mode)', align=Align.INLINE)
d.comment(0x9D4C, 'Test workspace flags', align=Align.INLINE)
d.comment(0x9D4F, 'bit6 not set -- check bit0', align=Align.INLINE)
d.comment(0x9D51, 'bit6 set -- TX completion', align=Align.INLINE)
d.comment(0x9D5B, 'bit0 set -- four-way handshake data phase', align=Align.INLINE)


d.subroutine(0x9D63, 'nmi_reply_scout', title='RX reply scout handler', description="""Handles reception of the reply scout frame after transmission.
Checks SR2 bit0 (AP) for incoming data, reads the first byte
(destination station) and compares to our station ID via &FE18
(which also disables NMIs as a side effect).""")
d.comment(0x9D63, 'A=&01: AP mask for SR2', align=Align.INLINE)
d.comment(0x9D65, 'BIT SR2: test AP (Address Present)', align=Align.INLINE)
d.comment(0x9D68, 'No AP -- error', align=Align.INLINE)
d.comment(0x9D6A, 'Read first RX byte (destination station)', align=Align.INLINE)
d.comment(0x9D6D, 'Compare to our station ID (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9D70, 'Not our station -- error/reject', align=Align.INLINE)


d.subroutine(0x9D77, 'nmi_reply_cont', title='RX reply continuation handler', description="""Reads the second byte of the reply scout (destination network) and
validates it is zero (local network). Installs nmi_reply_validate
(&9D8E) for the remaining two bytes (source station and network).
Optimisation: checks SR1 bit7 (IRQ still asserted) via BMI at &9D86.
If IRQ is still set, falls through directly to &9D8E without an RTI,
avoiding NMI re-entry overhead for short frames where all bytes arrive
in quick succession.""")
d.comment(0x9D77, 'BIT SR2: test for RDA (bit7 = data available)', align=Align.INLINE)
d.comment(0x9D7A, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9D7C, 'Read destination network byte', align=Align.INLINE)
d.comment(0x9D7F, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9D83, 'BIT SR1: test IRQ (N=bit7) -- more data ready?', align=Align.INLINE)
d.comment(0x9D88, 'IRQ not set -- install handler and RTI', align=Align.INLINE)


d.subroutine(0x9D8E, 'nmi_reply_validate', title='RX reply validation (Path 2 for FV/PSE interaction)', description="""Reads the source station and source network from the reply scout and
validates them against the original TX destination (&0D20/&0D21).
Sequence:
  1. Check SR2 bit7 (RDA) at &9D8E -- must see data available
  2. Read source station at &9D93, compare to &0D20 (tx_dst_stn)
  3. Read source network at &9D9B, compare to &0D21 (tx_dst_net)
  4. Check SR2 bit1 (FV) at &9DA5 -- must see frame complete
If all checks pass, the reply scout is valid and the ROM proceeds
to send the scout ACK (CR2=&A7 for RTS, CR1=&44 for TX mode).""")
d.comment(0x9D8E, 'BIT SR2: test RDA (bit7). Must be set for valid reply.', align=Align.INLINE)
d.comment(0x9D91, 'No RDA -- error (FV masking RDA via PSE would cause this)', align=Align.INLINE)
d.comment(0x9D93, 'Read source station', align=Align.INLINE)
d.comment(0x9D96, 'Compare to original TX destination station (&0D20)', align=Align.INLINE)
d.comment(0x9D99, 'Mismatch -- not the expected reply, error', align=Align.INLINE)
d.comment(0x9D9B, 'Read source network', align=Align.INLINE)
d.comment(0x9D9E, 'Compare to original TX destination network (&0D21)', align=Align.INLINE)
d.comment(0x9DA1, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9DA3, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9DA5, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9DA8, 'No FV -- incomplete frame, error', align=Align.INLINE)
d.comment(0x9DAA, 'CR2=&A7: RTS|CLR_TX_ST|FC_TDRA|2_1_BYTE|PSE (TX in handshake)', align=Align.INLINE)
d.comment(0x9DAC, 'Write CR2: enable RTS for TX handshake', align=Align.INLINE)
d.comment(0x9DAF, 'CR1=&44: RX_RESET | TIE (TX active for scout ACK)', align=Align.INLINE)
d.comment(0x9DB1, 'Write CR1: reset RX, enable TX interrupt', align=Align.INLINE)
d.comment(0x9DD9, 'BIT SR1: check TDRA before writing', align=Align.INLINE)
d.comment(0x9DDC, 'TDRA not ready: TX error', align=Align.INLINE)
d.comment(0x9DDE, 'Write our station to TX FIFO', align=Align.INLINE)
d.comment(0x9DE1, 'Network = 0 (local network)', align=Align.INLINE)
d.comment(0x9DE3, 'Write network byte to TX FIFO', align=Align.INLINE)
d.comment(0x9DE6, 'Test bit 1 of tx_flags', align=Align.INLINE)
d.comment(0x9DE8, 'Check if immediate-op or data-transfer', align=Align.INLINE)
d.comment(0x9DEB, 'Bit 1 set: immediate op, use alt handler', align=Align.INLINE)
d.comment(0x9DED, 'Install nmi_data_tx at &9DFB', align=Align.INLINE)
d.comment(0x9DEF, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9DF1, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x9DF4, 'Install nmi_imm_data at &9E42', align=Align.INLINE)
d.comment(0x9DF6, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9DF8, 'Install and return via set_nmi_vector', align=Align.INLINE)
d.comment(0x9DB6, 'High byte &9E of next handler address', align=Align.INLINE)
d.comment(0x9DB8, 'Store low byte to nmi_next_lo', align=Align.INLINE)
d.comment(0x9DBB, 'Store high byte to nmi_next_hi', align=Align.INLINE)
d.comment(0x9DBE, 'Load dest station for scout ACK TX', align=Align.INLINE)
d.comment(0x9DC1, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9DC4, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9DC6, 'Write dest station to TX FIFO', align=Align.INLINE)
d.comment(0x9DC9, 'Load dest network for scout ACK TX', align=Align.INLINE)
d.comment(0x9DCC, 'Write dest network to TX FIFO', align=Align.INLINE)
d.comment(0x9DD1, 'High byte &9D of handler address', align=Align.INLINE)
d.comment(0x9DD3, 'Set NMI vector and return', align=Align.INLINE)


d.subroutine(0x9DD6, 'nmi_scout_ack_src', title='TX scout ACK: write source address', description="""Writes our station ID and network=0 to TX FIFO, completing the
4-byte scout ACK frame. Then proceeds to send the data frame.""")
d.comment(0x9DD6, 'Load our station ID (also INTOFF)', align=Align.INLINE)


d.subroutine(0x9DFB, 'nmi_data_tx', title='TX data phase: send payload', description="""Sends the data frame payload from (open_port_buf),Y in pairs per NMI.
Same pattern as the NMI TX handler at &9CFF but reads from the port
buffer instead of the TX workspace. Writes two bytes per iteration,
checking SR1 IRQ between pairs for tight looping.""")
d.comment(0x9DFB, 'Y = buffer offset, resume from last position', align=Align.INLINE)
d.comment(0x9DFD, 'BIT SR1: test TDRA (V=bit6)', align=Align.INLINE)
d.comment(0x9E00, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E02, 'Write data byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E04, 'Write first byte of pair to FIFO', align=Align.INLINE)
d.comment(0x9E07, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E08, 'No page crossing', align=Align.INLINE)
d.comment(0x9E0A, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E0C, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E0E, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x9E10, 'Load second byte of pair', align=Align.INLINE)
d.comment(0x9E12, 'Write second byte to FIFO', align=Align.INLINE)
d.comment(0x9E15, 'Advance buffer offset', align=Align.INLINE)
d.comment(0x9E16, 'Save updated buffer position', align=Align.INLINE)
d.comment(0x9E18, 'No page crossing', align=Align.INLINE)
d.comment(0x9E1A, 'Page crossing: decrement page count', align=Align.INLINE)
d.comment(0x9E1C, 'No pages left: send last data', align=Align.INLINE)
d.comment(0x9E1E, 'Increment buffer high byte', align=Align.INLINE)
d.comment(0x9E20, 'BIT SR1: test IRQ (N=bit7) for tight loop', align=Align.INLINE)
d.comment(0x9E23, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9E25, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9E28, 'CR2=&3F: TX_LAST_DATA (close data frame)', align=Align.INLINE)
d.comment(0x9E2A, 'Write CR2 to close frame', align=Align.INLINE)
d.comment(0x9E2D, 'Check tx_flags for next action', align=Align.INLINE)
d.comment(0x9E30, 'Bit7 clear: error, install saved handler', align=Align.INLINE)
d.comment(0x9E32, 'Install discard_reset_listen at &99DB', align=Align.INLINE)
d.comment(0x9E34, 'High byte of &99DB handler', align=Align.INLINE)
d.comment(0x9E36, 'Set NMI vector and return', align=Align.INLINE)
d.comment(0x9E39, 'Load saved next handler low byte', align=Align.INLINE)
d.comment(0x9E3C, 'Load saved next handler high byte', align=Align.INLINE)
d.comment(0x9E3F, 'Install saved handler and return', align=Align.INLINE)
d.comment(0x9E42, 'Tube TX: BIT SR1 test TDRA', align=Align.INLINE)
d.comment(0x9E45, 'TDRA not ready -- error', align=Align.INLINE)
d.comment(0x9E47, 'Read byte from Tube R3', align=Align.INLINE)
d.comment(0x9E4A, 'Write to TX FIFO', align=Align.INLINE)
d.comment(0x9E4D, 'Increment 4-byte buffer counter', align=Align.INLINE)
d.comment(0x9E4F, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9E51, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9E53, 'No further carry', align=Align.INLINE)
d.comment(0x9E55, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9E57, 'No further carry', align=Align.INLINE)
d.comment(0x9E59, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9E5B, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x9E5D, 'Read second Tube byte from R3', align=Align.INLINE)
d.comment(0x9E60, 'Write second byte to TX FIFO', align=Align.INLINE)
d.comment(0x9E63, 'Increment 4-byte counter (second byte)', align=Align.INLINE)
d.comment(0x9E65, "Low byte didn't wrap", align=Align.INLINE)
d.comment(0x9E67, 'Carry into second byte', align=Align.INLINE)
d.comment(0x9E69, 'No further carry', align=Align.INLINE)
d.comment(0x9E6B, 'Carry into third byte', align=Align.INLINE)
d.comment(0x9E6D, 'No further carry', align=Align.INLINE)
d.comment(0x9E6F, 'Carry into fourth byte', align=Align.INLINE)
d.comment(0x9E71, 'Counter wrapped to zero: last data', align=Align.INLINE)
d.comment(0x9E73, 'BIT SR1: test IRQ for tight loop', align=Align.INLINE)
d.comment(0x9E76, 'IRQ still set: write 2 more bytes', align=Align.INLINE)
d.comment(0x9E78, 'No IRQ: return, wait for next NMI', align=Align.INLINE)
d.comment(0x9E7B, 'TX error: check flags for path', align=Align.INLINE)
d.comment(0x9E7E, 'Bit7 clear: TX result = not listening', align=Align.INLINE)
d.comment(0x9E80, 'Bit7 set: discard and return to listen', align=Align.INLINE)


d.subroutine(0x9E83, 'handshake_await_ack', title='Four-way handshake: switch to RX for final ACK', description="""After the data frame TX completes, switches to RX mode (CR1=&82)
and installs &9E8F to receive the final ACK from the remote station.""")
d.comment(0x9E83, 'CR1=&82: TX_RESET | RIE (switch to RX for final ACK)', align=Align.INLINE)
d.comment(0x9E85, 'Write to ADLC CR1', align=Align.INLINE)
d.comment(0x9E8A, 'High byte of handler address', align=Align.INLINE)
d.comment(0x9E8C, 'Install and return via set_nmi_vector', align=Align.INLINE)


d.subroutine(0x9E8F, 'nmi_final_ack', title='RX final ACK handler', description="""Receives the final ACK in a four-way handshake. Same validation
pattern as the reply scout handler (&9D63-&9D8E):
  &9E8F: Check AP, read dest_stn, compare to our station
  &9EA3: Check RDA, read dest_net, validate = 0
  &9EB7: Check RDA, read src_stn/net, compare to TX dest
  &9ED6: Check FV for frame completion
On success, stores result=0 at tx_result_ok. On failure, error &41.""")
d.comment(0x9E8F, 'A=&01: AP mask', align=Align.INLINE)
d.comment(0x9E91, 'BIT SR2: test AP', align=Align.INLINE)
d.comment(0x9E94, 'No AP -- error', align=Align.INLINE)
d.comment(0x9E96, 'Read dest station', align=Align.INLINE)
d.comment(0x9E99, 'Compare to our station (INTOFF side effect)', align=Align.INLINE)
d.comment(0x9E9C, 'Not our station -- error', align=Align.INLINE)
d.comment(0x9EA3, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9EA6, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9EA8, 'Read dest network', align=Align.INLINE)
d.comment(0x9EAB, 'Non-zero -- network mismatch, error', align=Align.INLINE)
d.comment(0x9EAF, 'BIT SR1: test IRQ -- more data ready?', align=Align.INLINE)


d.subroutine(0x9EB7, 'nmi_final_ack_validate', title='Final ACK validation', description="""Reads and validates src_stn and src_net against original TX dest.
Then checks FV for frame completion.""")
d.comment(0x9EB7, 'BIT SR2: test RDA', align=Align.INLINE)
d.comment(0x9EBA, 'No RDA -- error', align=Align.INLINE)
d.comment(0x9EBC, 'Read source station', align=Align.INLINE)
d.comment(0x9EBF, 'Compare to TX dest station (&0D20)', align=Align.INLINE)
d.comment(0x9EC2, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9EC4, 'Read source network', align=Align.INLINE)
d.comment(0x9EC7, 'Compare to TX dest network (&0D21)', align=Align.INLINE)
d.comment(0x9ECA, 'Mismatch -- error', align=Align.INLINE)
d.comment(0x9ED4, 'A=&02: FV mask for SR2 bit1', align=Align.INLINE)
d.comment(0x9ED6, 'BIT SR2: test FV -- frame must be complete', align=Align.INLINE)
d.comment(0x9ED9, 'No FV -- error', align=Align.INLINE)


d.subroutine(0x9EDB, 'tx_result_ok', title='TX completion handler', description="""Stores result code 0 (success) into the first byte of the TX control
block (nmi_tx_block),Y=0. Then sets &0D3A bit7 to signal completion
and calls discard_reset_listen to return to idle.""")
d.comment(0x9EDB, 'A=0: success result code', align=Align.INLINE)
d.comment(0x9EDD, 'BEQ: always taken (A=0)', align=Align.INLINE)


d.subroutine(0x9EDF, 'tx_result_fail', title='TX failure: not listening', description="""Loads error code &41 (not listening) and falls through to
tx_store_result. The most common TX error path — reached from
11 sites across the final-ACK validation chain when the remote
station doesn't respond or the frame is malformed.""")
d.comment(0x9EDF, 'A=&41: not listening error code', align=Align.INLINE)


d.subroutine(0x9EE1, 'tx_store_result', title='TX result store and completion', description="""Stores result code (A) into the TX control block at
(nmi_tx_block),0 and sets bit 7 of &0D3A to signal completion.
Returns to idle via discard_reset_listen. Reached from
tx_result_ok (A=0, success), tx_result_fail (A=&41, not
listening), and directly with other codes (A=&40 line jammed,
A=&42 net error).""")
d.comment(0x9EE1, 'Y=0: index into TX control block', align=Align.INLINE)
d.comment(0x9EE3, 'Store result/error code at (nmi_tx_block),0', align=Align.INLINE)
d.comment(0x9EE5, '&80: completion flag for &0D3A', align=Align.INLINE)
d.comment(0x9EE7, 'Signal TX complete', align=Align.INLINE)
d.comment(0x9EEA, 'Full ADLC reset and return to idle listen', align=Align.INLINE)
d.comment(0x9EED, 'Unreferenced data block (purpose unknown)', align=Align.INLINE)

d.label(0x0020, 'tube_send_zero_r2')

d.label(0x0437, 'setup_data_transfer')
d.comment(0x0443, 'Send transfer address byte', align=Align.INLINE)
d.comment(0x0604, 'Return to main event loop', align=Align.INLINE)
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
d.comment(0x807D, 'Advance past matched command text', align=Align.INLINE)
d.comment(0x80AC, 'Test escape flag before FS reply', align=Align.INLINE)
d.comment(0x80BD, 'Copy command text to FS buffer', align=Align.INLINE)
d.comment(0x80C7, 'CSD handle zero: not logged in', align=Align.INLINE)
d.comment(0x80D3, 'FSCV function >= 8?', align=Align.INLINE)
d.comment(0x80D7, 'X = function code for dispatch', align=Align.INLINE)
d.comment(0x80D8, 'Save Y (command text ptr hi)', align=Align.INLINE)
d.comment(0x81A2, 'Return to MOS service handler', align=Align.INLINE)
d.comment(0x8269, 'A=&8F: issue service request', align=Align.INLINE)
d.comment(0x826B, "X=&0F: 'vectors claimed' service", align=Align.INLINE)
d.comment(0x8270, 'X=&0A: service &0A', align=Align.INLINE)
d.comment(0x8277, 'Non-zero: skip auto-boot', align=Align.INLINE)
d.comment(0x827B, 'Y=&82: ROM page high byte', align=Align.INLINE)
d.comment(0x827D, 'Execute command string at (X, Y)', align=Align.INLINE)
d.comment(0x82B0, 'Return (workspace claim done)', align=Align.INLINE)
d.comment(0x8341, 'Load FS state byte at offset Y', align=Align.INLINE)
d.comment(0x8344, 'Store to workspace backup area', align=Align.INLINE)
d.comment(0x8346, 'Next byte down', align=Align.INLINE)
d.comment(0x8349, 'Loop for offsets &1D..&15', align=Align.INLINE)
d.comment(0x834B, 'A=&77: OSBYTE close spool/exec', align=Align.INLINE)
d.comment(0x8374, 'Return with Z flag result', align=Align.INLINE)
d.comment(0x8382, 'Return after port setup', align=Align.INLINE)
d.comment(0x839B, 'Control flag', align=Align.INLINE)
d.comment(0x839C, 'Port (FS command = &99)', align=Align.INLINE)
d.comment(0x839F, 'Buffer start low', align=Align.INLINE)
d.comment(0x83A0, 'Buffer start high (page &0F)', align=Align.INLINE)
d.comment(0x83A1, 'Buffer start pad (4-byte Econet addr)', align=Align.INLINE)
d.comment(0x83A2, 'Buffer start pad', align=Align.INLINE)
d.comment(0x83A3, 'Buffer end low', align=Align.INLINE)
d.comment(0x83A4, 'Buffer end high (page &0F)', align=Align.INLINE)
d.comment(0x83A5, 'Buffer end pad', align=Align.INLINE)
d.comment(0x83A6, 'Buffer end pad', align=Align.INLINE)


d.subroutine(0x83A7, 'prepare_cmd_with_flag', title='Prepare FS command with carry set', description="""Alternate entry to prepare_fs_cmd that pushes A, loads &2A
into fs_error_ptr, and enters with carry set (SEC). The carry
flag is later tested by build_send_fs_cmd to select the
byte-stream (BSXMIT) transmission path.""", on_entry={'a': 'flag byte to include in FS command', 'y': 'function code for FS header'})
d.comment(0x83AE, 'A=&77: OSBYTE close spool/exec', align=Align.INLINE)
d.comment(0x8401, 'CLC for address addition', align=Align.INLINE)
d.comment(0x848A, 'Transfer A to Y for indexing', align=Align.INLINE)
d.comment(0x848C, 'Transfer to X for return', align=Align.INLINE)
d.comment(0x84D0, 'A=0: zero execution header bytes', align=Align.INLINE)
d.comment(0x84D5, 'Next byte', align=Align.INLINE)
d.comment(0x84D6, 'Loop until all zeroed', align=Align.INLINE)
d.comment(0x8567, 'Set EOF flag for this handle', align=Align.INLINE)

d.label(0x856A, 'load_handle_mask')
d.comment(0x856A, 'Load handle bitmask for caller', align=Align.INLINE)
d.comment(0x856D, 'Return with handle mask in A', align=Align.INLINE)
d.comment(0x864B, 'Store return addr low as string ptr', align=Align.INLINE)
d.comment(0x864E, 'Store return addr high as string ptr', align=Align.INLINE)
d.comment(0x8650, 'Y=0: offset for indirect load', align=Align.INLINE)
d.comment(0x8654, 'No page wrap: skip high byte inc', align=Align.INLINE)
d.comment(0x8656, 'Handle page crossing in pointer', align=Align.INLINE)
d.comment(0x865F, 'Continue printing next character', align=Align.INLINE)
d.comment(0x8667, 'Initialise accumulator to zero', align=Align.INLINE)
d.comment(0x8687, 'Return with result in A', align=Align.INLINE)
d.comment(0x86A2, 'Restore X from stack', align=Align.INLINE)
d.comment(0x86A4, 'Return with mask in X', align=Align.INLINE)
d.comment(0x86AC, 'Return with handle in A', align=Align.INLINE)
d.comment(0x86B5, 'Next byte', align=Align.INLINE)
d.comment(0x86B8, 'Return with Z flag result', align=Align.INLINE)
d.comment(0x86BD, 'Return (FSCV 7 read handles)', align=Align.INLINE)
d.comment(0x86FA, 'Save A/X/Y in FS workspace', align=Align.INLINE)
d.comment(0x8706, 'A=&FF: branch to load path', align=Align.INLINE)
d.comment(0x870B, 'Copy parsed filename to cmd buffer', align=Align.INLINE)
d.comment(0x870E, 'Y=2: FS function code offset', align=Align.INLINE)

d.label(0x8802, 'send_fs_reply')
d.comment(0x8802, 'Send FS reply acknowledgement', align=Align.INLINE)
d.comment(0x882B, '(continued)', align=Align.INLINE)
d.comment(0x882C, '(continued)', align=Align.INLINE)
d.comment(0x882D, '(continued)', align=Align.INLINE)
d.comment(0x8837, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x883A, 'Loop until offset 2 reached', align=Align.INLINE)
d.comment(0x883D, 'Y -= 3', align=Align.INLINE)
d.comment(0x883E, '(continued)', align=Align.INLINE)
d.comment(0x883F, '(continued)', align=Align.INLINE)
d.comment(0x8840, 'Return to caller', align=Align.INLINE)

d.label(0x8873, 'clamp_dest_setup')
d.comment(0x89F8, 'A=handle bitmask for new file', align=Align.INLINE)
d.comment(0x8A5F, 'Return (unsupported function)', align=Align.INLINE)
d.comment(0x8CFC, 'Print two CRs (blank line)', align=Align.INLINE)

d.label(0x8D09, 'cat_examine_loop')
d.comment(0x8D41, 'Return from column separator', align=Align.INLINE)
d.comment(0x8D72, 'Start copying from offset 0', align=Align.INLINE)
d.comment(0x8D74, 'Load next byte from source string', align=Align.INLINE)
d.comment(0x8D79, 'Advance write position', align=Align.INLINE)

d.label(0x8E2D, 'exec_at_load_addr')
d.comment(0x8E5C, 'X = stack pointer', align=Align.INLINE)
d.comment(0x8E66, 'Invalid: Y = 0', align=Align.INLINE)
d.comment(0x8E68, 'A = 0, C set (error)', align=Align.INLINE)
d.comment(0x8E69, 'Return after calculation', align=Align.INLINE)
d.comment(0x8E6A, 'Y=&6F: RX buffer handle offset', align=Align.INLINE)
d.comment(0x8E6C, 'Read handle from RX packet', align=Align.INLINE)
d.comment(0x8E6E, 'Valid handle: store and return', align=Align.INLINE)
d.comment(0x8E8E, 'Outside our OSWORD range, exit', align=Align.INLINE)
d.comment(0x8F25, 'Load byte from workspace', align=Align.INLINE)
d.comment(0x8FB5, 'Enable interrupts before transmit', align=Align.INLINE)
d.comment(0x8FBB, 'Dest station = &FFFF (accept reply from any station)', align=Align.INLINE)
d.comment(0x8FDE, 'Receive data blocks until command byte = &00 or &0D', align=Align.INLINE)
d.comment(0x9017, 'Y=&04: advance to station address', align=Align.INLINE)
d.comment(0x917D, 'Load template byte from ctrl_block_template[X]', align=Align.INLINE)

d.label(0x91A5, 'rxcb_matched')
d.comment(0x91BC, '→ Y=&0D (main only)', align=Align.INLINE)
d.comment(0x91BD, '→ Y=&03 / Y=&75', align=Align.INLINE)
d.comment(0x91BE, 'SKIP (main only)', align=Align.INLINE)
d.comment(0x91BF, '→ Y=&10 (main only)', align=Align.INLINE)
d.comment(0x91C2, '→ Y=&08 / Y=&7A', align=Align.INLINE)
d.comment(0x91C3, '→ Y=&09 / Y=&7B', align=Align.INLINE)
d.comment(0x91C4, 'PAGE byte → Y=&15 (main only)', align=Align.INLINE)
d.comment(0x91C5, '→ Y=&16 (main only)', align=Align.INLINE)
d.comment(0x91C8, 'SKIP (main only)', align=Align.INLINE)
d.comment(0x91CB, 'PAGE byte → Y=&11 (main only)', align=Align.INLINE)
d.comment(0x91CC, '→ Y=&12 (main only)', align=Align.INLINE)
d.comment(0x91CD, '→ Y=&13 (main only)', align=Align.INLINE)
d.comment(0x91CE, '→ Y=&14 (main only)', align=Align.INLINE)
d.comment(0x91D1, '→ Y=&17 (main only)', align=Align.INLINE)
d.comment(0x9320, 'Return after storing result', align=Align.INLINE)
d.comment(0x9321, 'OSBYTE &85: read cursor position', align=Align.INLINE)
d.comment(0x9323, 'OSBYTE &C3: read screen start address', align=Align.INLINE)
d.comment(0x9665, 'RTS (end of save_vdu_state data)', align=Align.INLINE)
d.comment(0x96F4, 'Store broadcast flag in TX flags', align=Align.INLINE)
d.comment(0x96F7, 'Install next NMI handler at &9715 (RX scout second byte)', align=Align.INLINE)
d.comment(0x96F9, 'Install next handler and RTI', align=Align.INLINE)
d.comment(0x970C, 'Write CR1 to discontinue RX', align=Align.INLINE)
d.comment(0x970F, 'Return to idle scout listening', align=Align.INLINE)
d.comment(0x9712, 'Network = 0 (local): clear tx_flags', align=Align.INLINE)
d.comment(0x9717, 'Install scout data reading loop at &972E', align=Align.INLINE)
d.comment(0x9719, 'High byte of scout data handler', align=Align.INLINE)
d.comment(0x971B, 'Install scout data loop and RTI', align=Align.INLINE)
d.comment(0x9723, 'Neither set -- clean end, discard via &972B', align=Align.INLINE)
d.comment(0x972B, 'Gentle discard: RX_DISCONTINUE', align=Align.INLINE)
d.comment(0x9733, 'No RDA -- error handler &971E', align=Align.INLINE)
d.comment(0x974A, 'Copied all 12 scout bytes?', align=Align.INLINE)
d.comment(0x974E, 'Save final buffer offset', align=Align.INLINE)

d.label(0x979A, 'scout_ctrl_check')
d.comment(0x97A2, 'Y=1: advance to port byte in slot', align=Align.INLINE)

d.label(0x97B6, 'scout_port_match')
d.comment(0x9899, 'CR2=&84: disable PSE for bit testing', align=Align.INLINE)
d.comment(0x989E, 'CR1=&00: disable all interrupts', align=Align.INLINE)
d.comment(0x9925, 'Install saved next handler (&99B7 for scout ACK)', align=Align.INLINE)
d.comment(0x9940, 'Install handler at &9992 (write src addr)', align=Align.INLINE)
d.comment(0x9954, 'Write network=0 (local) to TX FIFO', align=Align.INLINE)
d.comment(0x9957, 'Check tx_flags for data phase', align=Align.INLINE)
d.comment(0x995A, 'bit7 set: start data TX phase', align=Align.INLINE)
d.comment(0x995C, 'CR2=&3F: TX_LAST_DATA | CLR_RX_ST | FLAG_IDLE | FC_TDRA | 2_1_BYTE | PSE', align=Align.INLINE)

d.label(0x99CB, 'add_buf_to_base')

d.label(0x99D2, 'inc_rxcb_buf_hi')

d.label(0x99D6, 'store_rxcb_buf_ptr')

d.label(0x99DB, 'store_rxcb_buf_hi')
d.comment(0x99FF, 'Check if Tube transfer active', align=Align.INLINE)
d.comment(0x9A02, 'Test tx_flags for Tube transfer', align=Align.INLINE)
d.comment(0x9AA3, 'A=0: port buffer lo at page boundary', align=Align.INLINE)
d.comment(0x9AA5, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9AA7, 'Buffer length lo = &82', align=Align.INLINE)
d.comment(0x9AA9, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9AAB, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9AAD, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9AAF, 'Load RX page hi for buffer', align=Align.INLINE)
d.comment(0x9AB1, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9AB3, 'Y=3: copy 4 bytes (3 down to 0)', align=Align.INLINE)
d.comment(0x9AB5, 'Load remote address byte', align=Align.INLINE)
d.comment(0x9AB8, 'Store to exec address workspace', align=Align.INLINE)
d.comment(0x9ABB, 'Next byte (descending)', align=Align.INLINE)
d.comment(0x9ABC, 'Loop until all 4 bytes copied', align=Align.INLINE)
d.comment(0x9ABE, 'Enter common data-receive path', align=Align.INLINE)
d.comment(0x9ABF, 'Svc 5 dispatch table low bytes', align=Align.INLINE)
d.comment(0x9AC1, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9AC3, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AC5, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AC7, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9AC9, 'Enter POKE data-receive path', align=Align.INLINE)
d.comment(0x9ACC, 'Buffer length hi = 1', align=Align.INLINE)
d.comment(0x9ACE, 'Set buffer length hi', align=Align.INLINE)
d.comment(0x9AD0, 'Buffer length lo = &FC', align=Align.INLINE)
d.comment(0x9AD2, 'Set buffer length lo', align=Align.INLINE)
d.comment(0x9AD4, 'Buffer start lo = &21', align=Align.INLINE)
d.comment(0x9AD6, 'Set port buffer lo', align=Align.INLINE)
d.comment(0x9AD8, 'Buffer hi = &7F (below screen)', align=Align.INLINE)
d.comment(0x9ADA, 'Set port buffer hi', align=Align.INLINE)
d.comment(0x9ADE, 'Port workspace offset = &3D', align=Align.INLINE)
d.comment(0x9AE0, 'Store workspace offset lo', align=Align.INLINE)
d.comment(0x9AE2, 'RX buffer page = &0D', align=Align.INLINE)
d.comment(0x9AE4, 'Store workspace offset hi', align=Align.INLINE)
d.comment(0x9AE6, 'Scout status = 2 (PEEK response)', align=Align.INLINE)
d.comment(0x9AE8, 'Store scout status', align=Align.INLINE)
d.comment(0x9AEB, 'Calculate transfer size for response', align=Align.INLINE)
d.comment(0x9AEE, 'C=0: transfer not set up, discard', align=Align.INLINE)

d.label(0x9AF0, 'set_tx_reply_flag')
d.comment(0x9AF0, 'Mark TX flags bit 7 (reply pending)', align=Align.INLINE)
d.comment(0x9AF3, 'Set reply pending flag', align=Align.INLINE)
d.comment(0x9AF5, 'Store updated TX flags', align=Align.INLINE)

d.label(0x9AF8, 'rx_imm_halt_cont')
d.comment(0x9AF8, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9AFA, 'Write CR1: enable TX interrupts', align=Align.INLINE)

d.label(0x9AFD, 'tx_cr2_setup')
d.comment(0x9AFD, 'CR2=&A7: RTS|CLR_RX_ST|FC_TDRA|PSE', align=Align.INLINE)
d.comment(0x9AFF, 'Write CR2 for TX setup', align=Align.INLINE)

d.label(0x9B02, 'tx_nmi_setup')
d.comment(0x9B02, 'NMI handler lo byte (self-modifying)', align=Align.INLINE)
d.comment(0x9B04, 'Y=&9B: dispatch table page', align=Align.INLINE)
d.comment(0x9B06, 'Acknowledge and write TX dest', align=Align.INLINE)

d.label(0x9B3F, 'imm_op_discard')
d.comment(0x9B42, 'Unreferenced data (reply tail bytes)', align=Align.INLINE)
d.comment(0x9B46, 'Terminator byte (&80)', align=Align.INLINE)
d.comment(0x9B47, 'Hi byte of tx_done_exit-1', align=Align.INLINE)
d.comment(0x9B49, 'Push hi byte on stack', align=Align.INLINE)
d.comment(0x9B4A, 'Push lo of (tx_done_exit-1)', align=Align.INLINE)
d.comment(0x9B4C, 'Push lo byte on stack', align=Align.INLINE)
d.comment(0x9B4D, 'Call remote JSR; RTS to tx_done_exit', align=Align.INLINE)
d.comment(0x9B4F, 'ORA opcode (dead code / data overlap)', align=Align.INLINE)
d.comment(0x9B50, 'Y=8: network event type', align=Align.INLINE)
d.comment(0x9B52, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9B55, 'A = remote address hi', align=Align.INLINE)
d.comment(0x9B5B, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9B5E, 'X = remote address lo', align=Align.INLINE)
d.comment(0x9B61, 'Y = remote address hi', align=Align.INLINE)
d.comment(0x9B64, 'Call ROM entry point at &8000', align=Align.INLINE)
d.comment(0x9B67, 'Exit TX done handler', align=Align.INLINE)
d.comment(0x9B6A, 'A=&04: bit 2 mask for rx_flags', align=Align.INLINE)
d.comment(0x9B6C, 'Test if already halted', align=Align.INLINE)
d.comment(0x9B6F, 'Already halted: skip to exit', align=Align.INLINE)
d.comment(0x9B71, 'Set bit 2 in rx_flags', align=Align.INLINE)
d.comment(0x9B74, 'Store halt flag', align=Align.INLINE)
d.comment(0x9B77, 'A=4: re-load halt bit mask', align=Align.INLINE)
d.comment(0x9B79, 'Enable interrupts during halt wait', align=Align.INLINE)

d.label(0x9B7A, 'halt_spin_loop')
d.comment(0x9B7A, 'Test halt flag', align=Align.INLINE)
d.comment(0x9B7D, 'Still halted: keep spinning', align=Align.INLINE)
d.comment(0x9B81, 'Load current RX flags', align=Align.INLINE)
d.comment(0x9B84, 'Clear bit 2: release halted station', align=Align.INLINE)
d.comment(0x9B86, 'Store updated flags', align=Align.INLINE)
d.comment(0x9B89, 'Restore Y from stack', align=Align.INLINE)
d.comment(0x9B8A, 'Transfer to Y register', align=Align.INLINE)
d.comment(0x9B8B, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9B8C, 'Transfer to X register', align=Align.INLINE)
d.comment(0x9B8D, 'A=0: success status', align=Align.INLINE)
d.comment(0x9B8F, 'Return with A=0 (success)', align=Align.INLINE)
d.comment(0x9BBF, '(continued)', align=Align.INLINE)
d.comment(0x9BC0, '(continued)', align=Align.INLINE)
d.comment(0x9BC1, '(continued)', align=Align.INLINE)
d.comment(0x9BC8, 'Y += 5: advance to next end byte', align=Align.INLINE)
d.comment(0x9BC9, '(continued)', align=Align.INLINE)
d.comment(0x9BCA, '(continued)', align=Align.INLINE)
d.comment(0x9BCB, '(continued)', align=Align.INLINE)
d.comment(0x9BCC, '(continued)', align=Align.INLINE)

d.label(0x9BD7, 'check_imm_range')
d.comment(0x9BF8, 'Save TX index', align=Align.INLINE)
d.comment(0x9BFB, 'Push timeout byte 1 on stack', align=Align.INLINE)
d.comment(0x9BFC, 'Push timeout byte 2 on stack', align=Align.INLINE)
d.comment(0x9C00, 'Disable interrupts for ADLC access', align=Align.INLINE)
d.comment(0x9C01, 'A=&40: BIT &FE18 becomes RTI (disable NMI)', align=Align.INLINE)
d.comment(0x9C03, 'Self-modify NMI shim at &0D1C: disable', align=Align.INLINE)

d.label(0x9C0B, 'test_line_idle')
d.comment(0x9C15, 'Write CR2: clear status, prepare TX', align=Align.INLINE)
d.comment(0x9C27, 'Restore interrupt state', align=Align.INLINE)
d.comment(0x9C29, 'Increment timeout counter byte 1', align=Align.INLINE)
d.comment(0x9C2C, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C2E, 'Increment timeout counter byte 2', align=Align.INLINE)
d.comment(0x9C31, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C33, 'Increment timeout counter byte 3', align=Align.INLINE)
d.comment(0x9C36, 'Not overflowed: retry INACTIVE test', align=Align.INLINE)
d.comment(0x9C3A, 'CR1=&44: TIE | TX_LAST_DATA', align=Align.INLINE)
d.comment(0x9C44, 'Pop saved register', align=Align.INLINE)
d.comment(0x9C45, 'Pop saved register', align=Align.INLINE)
d.comment(0x9C65, 'Install NMI handler at &9D4C (TX data handler)', align=Align.INLINE)

d.label(0x9C9E, 'imm_op_status3')
d.comment(0x9C9E, 'A=3: scout_status for PEEK', align=Align.INLINE)
d.comment(0x9CA2, 'A=3: scout_status for PEEK op', align=Align.INLINE)
d.comment(0x9CA6, 'Scout status = 2 (POKE transfer)', align=Align.INLINE)

d.label(0x9CA8, 'store_status_add4')
d.comment(0x9CA8, 'Store scout status', align=Align.INLINE)
d.comment(0x9CAB, 'Clear carry for 4-byte addition', align=Align.INLINE)
d.comment(0x9CAC, 'Save carry on stack', align=Align.INLINE)
d.comment(0x9CAD, 'Y=&0C: start at offset 12', align=Align.INLINE)

d.label(0x9CAF, 'add_bytes_loop')
d.comment(0x9CAF, 'Load workspace address byte', align=Align.INLINE)
d.comment(0x9CB2, 'Restore carry from previous byte', align=Align.INLINE)
d.comment(0x9CB3, 'Add TXCB address byte', align=Align.INLINE)
d.comment(0x9CB5, 'Store updated address byte', align=Align.INLINE)
d.comment(0x9CB8, 'Next byte', align=Align.INLINE)
d.comment(0x9CB9, 'Save carry for next addition', align=Align.INLINE)
d.comment(0x9CBA, 'Compare Y with 16-byte boundary', align=Align.INLINE)
d.comment(0x9CBC, 'Below boundary: continue addition', align=Align.INLINE)
d.comment(0x9CBE, 'Restore processor flags', align=Align.INLINE)
d.comment(0x9CBF, 'Skip buffer setup if transfer size is zero', align=Align.INLINE)

d.label(0x9CE8, 'proc_op_status2')

d.label(0x9CEA, 'store_status_copy_ptr')

d.label(0x9CED, 'skip_buf_setup')
d.comment(0x9D0D, 'Next TX buffer byte', align=Align.INLINE)
d.comment(0x9D0E, 'Load second byte from TX buffer', align=Align.INLINE)
d.comment(0x9D11, 'Advance TX index past second byte', align=Align.INLINE)
d.comment(0x9D12, 'Save updated TX buffer index', align=Align.INLINE)
d.comment(0x9D2B, 'Write CR2: clear status, idle listen', align=Align.INLINE)
d.comment(0x9D34, 'PHA/PLA delay (~7 cycles each)', align=Align.INLINE)
d.comment(0x9D35, 'Increment delay counter', align=Align.INLINE)
d.comment(0x9D36, 'Loop 256 times for NMI disable', align=Align.INLINE)
d.comment(0x9D38, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x9D40, 'Install NMI handler at &9D47 (TX completion)', align=Align.INLINE)
d.comment(0x9D49, 'Write CR1 to switch from TX to RX', align=Align.INLINE)
d.comment(0x9D54, 'A=1: mask for bit0 test', align=Align.INLINE)
d.comment(0x9D56, 'Test tx_flags bit0 (handshake)', align=Align.INLINE)
d.comment(0x9D59, 'bit0 clear: install reply handler', align=Align.INLINE)
d.comment(0x9D5E, 'Install RX reply handler at &9D63', align=Align.INLINE)
d.comment(0x9D60, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9D72, 'Install next handler at &9D77 (reply continuation)', align=Align.INLINE)
d.comment(0x9D74, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9D81, 'Install next handler at &9DE3 (reply validation)', align=Align.INLINE)
d.comment(0x9D86, 'IRQ set: validate reply immediately', align=Align.INLINE)
d.comment(0x9D8B, 'Store error and return to idle', align=Align.INLINE)
d.comment(0x9DB4, 'Install next handler at &9E83 into &0D4B/&0D4C', align=Align.INLINE)
d.comment(0x9DCF, 'Install handler at &9DD6 (write src addr for scout ACK)', align=Align.INLINE)

d.label(0x9E67, 'tube_tx_inc_byte2')

d.label(0x9E6F, 'tube_tx_inc_byte4')
d.comment(0x9E88, 'Install handler at &9E8F (RX final ACK)', align=Align.INLINE)
d.comment(0x9E9E, 'Install handler at &9EFF (final ACK continuation)', align=Align.INLINE)
d.comment(0x9EA0, 'Install continuation handler', align=Align.INLINE)
d.comment(0x9EAD, 'Install handler at &9F15 (final ACK validation)', align=Align.INLINE)
d.comment(0x9EB2, 'IRQ set: validate final ACK immediately', align=Align.INLINE)
d.comment(0x9EB4, 'Install handler and RTI', align=Align.INLINE)
d.comment(0x9ECC, 'Load TX flags for next action', align=Align.INLINE)
d.comment(0x9ECF, 'bit7 clear: no data phase', align=Align.INLINE)
d.comment(0x9ED1, 'Install data RX handler', align=Align.INLINE)
d.comment(0x9F0D, 'Load TX flags for transfer setup', align=Align.INLINE)
d.comment(0x9F12, 'Store with bit 1 set (Tube xfer)', align=Align.INLINE)
d.comment(0x9F1C, '(continued)', align=Align.INLINE)
d.comment(0x9F1D, '(continued)', align=Align.INLINE)
d.comment(0x9F1E, '(continued)', align=Align.INLINE)
d.comment(0x9F26, '(continued)', align=Align.INLINE)
d.comment(0x9F27, '(continued)', align=Align.INLINE)
d.comment(0x9F32, 'CLC for base pointer addition', align=Align.INLINE)
d.comment(0x9F33, 'Add RXCB base to get RXCB+4 addr', align=Align.INLINE)
d.comment(0x9F3A, 'Claim Tube transfer address', align=Align.INLINE)
d.comment(0x9F42, 'Reclaim with scout status type', align=Align.INLINE)
d.comment(0x9F4A, 'Restore X from stack', align=Align.INLINE)
d.comment(0x9F4B, 'Return with C = transfer status', align=Align.INLINE)
d.comment(0x9F61, 'Copy RXCB[8] to open port buffer lo', align=Align.INLINE)
d.comment(0x9F6F, 'Return with C=1 (success)', align=Align.INLINE)
d.comment(0x9FCC, 'Transfer ROM bank to Y', align=Align.INLINE)
d.comment(0x85ED, 'A=&FF: full retry count', align=Align.INLINE)
d.comment(0x8402, 'Clear escapable flag before BGET', align=Align.INLINE)
d.comment(0x9EFF, 'Load workspace byte at offset Y', align=Align.INLINE)
d.comment(0x9F45, 'Release Tube claim after reclaim', align=Align.INLINE)
d.comment(0x9F72, 'Write CR1 to ADLC register 0', align=Align.INLINE)
d.comment(0x9F77, 'Write CR4 to ADLC register 3', align=Align.INLINE)
d.comment(0x9F7C, 'Write CR3 to ADLC register 1', align=Align.INLINE)
d.comment(0x9683, 'Y >= &86: above dispatch range', align=Align.INLINE)
d.comment(0x9685, 'Out of range: skip protection', align=Align.INLINE)
d.comment(0x9687, 'Save current JSR protection mask', align=Align.INLINE)
d.comment(0x968A, 'Backup to saved_jsr_mask', align=Align.INLINE)
d.comment(0x968D, 'Set protection bits 2-4', align=Align.INLINE)
d.comment(0x968F, 'Apply protection during dispatch', align=Align.INLINE)
d.comment(0x9692, 'Push return addr high (&9B)', align=Align.INLINE)
d.comment(0x9694, 'High byte on stack for RTS', align=Align.INLINE)
d.comment(0x9695, 'Load dispatch target low byte', align=Align.INLINE)
d.comment(0x9698, 'Low byte on stack for RTS', align=Align.INLINE)
d.comment(0x9699, "RTS = dispatch to PHA'd address", align=Align.INLINE)
d.comment(0x06C5, 'Poll R2 status (bit 7 = ready)', align=Align.INLINE)
d.comment(0x06C8, 'Not ready: keep polling', align=Align.INLINE)
d.comment(0x06CA, 'Read data byte from R2', align=Align.INLINE)
d.comment(0x06CD, 'Return with byte in A', align=Align.INLINE)
d.comment(0x06EB, 'Trampoline: begin TX operation', align=Align.INLINE)
d.comment(0x06EE, 'Trampoline: full ADLC init', align=Align.INLINE)
d.comment(0x06F1, 'Trampoline: wait idle and reset', align=Align.INLINE)
d.comment(0x06F4, 'Trampoline: init NMI workspace', align=Align.INLINE)
d.comment(0x06F7, 'A=4: SR interrupt bit mask', align=Align.INLINE)
d.comment(0x06F9, 'Test SR flag in VIA IFR', align=Align.INLINE)
d.comment(0x06FC, 'SR active: handle interrupt', align=Align.INLINE)
d.comment(0x06FE, 'A=5: NMI not for us', align=Align.INLINE)
import sys
ir = d.disassemble()
output = str(ir.render('beebasm', boundary_label_prefix='pydis_', byte_column=True, byte_column_format='py8dis', default_byte_cols=12, default_word_cols=6))
_output_dirpath.mkdir(parents=True, exist_ok=True)
output_filepath = _output_dirpath / 'nfs-3.65.asm'
output_filepath.write_text(output, encoding='utf-8')
print(f'Wrote {output_filepath}', file=sys.stderr)
json_filepath = _output_dirpath / 'nfs-3.65.json'
json_filepath.write_text(str(ir.render('json')), encoding='utf-8')
print(f'Wrote {json_filepath}', file=sys.stderr)
